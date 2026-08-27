# HML Standard 1.0 — the normative specification

**The Standard describes frozen executable semantics; it does not invent them.**

*Version 1.0 · 2026-08-27 · semantic source `b3d0af9` · model language `b011511`*

---

## 0. Requirement vocabulary  `[NORMATIVE]`

**MUST**, **REQUIRED**, **SHALL** — an absolute requirement.
**MUST NOT**, **SHALL NOT** — an absolute prohibition.
**SHOULD**, **SHOULD NOT** — a recommendation; ignoring it requires a stated reason.
**MAY**, **OPTIONAL** — genuinely at the implementer's discretion.

Every section is labelled `[NORMATIVE]` or `[INFORMATIVE]`. Only `[NORMATIVE]` sections
bind conformance.

## 1. What HML is  `[INFORMATIVE]`

Hamiltonian Lang is a typed semantic intermediate representation and verifier-facing
reasoning protocol for machine mathematics. It represents mathematical reasoning as explicit
typed state — scoped claims, goals, candidates, dependencies, obligations, evidence — and as
checked transitions between states.

The model-facing language is a serialization of this semantic state, **not the source of
mathematical truth**.

### What HML deliberately is not

HML is **not** a theorem prover. Its kernel has **20** inference rules and is intended to
stay that size. Domain reasoning lives in libraries; checking may be delegated to backends;
search and strategy are policy. A concept whose theorems live in a library is **not** a
language defect.

The question the Standard asks of every mathematical concept is not "can HML prove it?" but:

> **Can HML losslessly carry the reasoning state for it?**

Across 110 concepts in 22 domains, the answer was yes in every case — **zero `CORE_GAP`s**.
See `SEMANTIC_ATLAS.md`.

## 2. The three semantics  `[NORMATIVE]`

For every construct where the distinction is meaningful, three questions are answered
separately and **MUST NOT** be collapsed into a single "valid" bit:

- **Denotational** — what the construct means.
- **Operational** — how it changes `S_t --action--> S_{t+1}`.
- **Axiomatic / proof** — what licenses the claim or transition.

Where one view is delegated, the Standard says so. Example: for a `Claim` whose proposition
is opaque Lean text, the denotation is Lean's and HML carries it verbatim; the operational
and proof views remain HML's.

## 3. Semantic state  `[NORMATIVE]`

A semantic state consists of exactly five record mappings — `claims`, `candidates`,
`branches`, `goals`, `obligations` — and an ordered tuple of `active_scopes`
(**HML-STATE-001**).

Every record **MUST** be immutable; a transition produces a new state (**HML-STATE-002**).

The mapping key a record is filed under **MAY** differ from the record's own `id`. Both
**MUST** be preserved (**HML-STATE-003**).

A claim is visible if and only if its scope is a **member** of `active_scopes` — by
membership, never by ordering (**HML-STATE-004**). This is what stops a branch-local
conclusion leaking into global state without a join.

### The five record kinds

| record | carries | status vocabulary |
|---|---|---|
| `Claim` | a proposition asserted in a scope | `ClaimStatus` — GIVEN, ASSUMED, DERIVED, VERIFIED, REFUTED, UNRESOLVED, UNKNOWN |
| `Candidate` | a **proposed** object, not a fact | `CandidateStatus` — PROPOSED, UNVERIFIED, VERIFIED, REJECTED, UNKNOWN |
| `Branch` | a case in a split | `BranchStatus` — OPEN, CLOSED, JOINED, ABANDONED, UNKNOWN |
| `Goal` | what is being proved | `GoalStatus` — OPEN, DISCHARGED, UNKNOWN |
| `Obligation` | proof debt | `ObligationState` — OPEN, DISCHARGED, FAILED, UNKNOWN |

Each vocabulary is **closed**: an implementation **MUST** reject any other value
(**HML-ENUM-001**…**HML-ENUM-007**).

## 4. Epistemic discipline  `[NORMATIVE]`

This is where most of the value of the language sits, and where most of the ways to get it
wrong are.

**UNKNOWN is a value, not an absence.** An implementation **MUST NOT** map UNKNOWN to
FALSE, to a default, or to a missing field (**HML-EPIS-001**).

**A candidate is not a fact.** `CandidateStatus` cannot express GIVEN or DERIVED, so
promotion cannot be done by relabelling: it requires an action whose `candidate_effect`
promotes it and whose warrant licenses it (**HML-EPIS-002**, invariant `CANDIDATES`).

**Evidence is not truth.** `EvidenceRecord.trusted` defaults to `False` and `status` to
`UNKNOWN`. Evidence being present **MUST NOT** by itself raise a claim's status, and
untrusted evidence **MUST NOT** discharge a mandatory obligation (**HML-EPIS-003**).

**A generator MUST NOT self-certify.** An actor proposing a transition **MUST NOT** assert
its own verification status; only the verifier assigns a `Verdict` (**HML-EPIS-004**).

**Proof debt persists.** A mandatory obligation **MUST** survive across transitions until
explicitly discharged with attested evidence; silent disappearance **MUST** be rejected
(**HML-OBL-001**).

## 5. Actions  `[NORMATIVE]`

An action **MUST** be structural. An implementation **MUST NOT** treat the operation name
alone as the reasoning decision — the decision is *the action applied to a specific state*
(**HML-ACT-001**).

`Action` carries: `operation`, `output_id`, `dependencies`, `preconditions`, `warrant`,
`typing`, `obligations_created`, `obligations_discharged`, and five effect maps —
`goal_effect`, `scope_effect`, `branch_effect`, `candidate_effect`, `epistemic_effect`.

Every reference an action makes **MUST** resolve in the state it applies to
(**HML-ACT-002**), reported as `ErrorClass.MISSING_DEPENDENCY`.

## 6. Transitions and verification  `[NORMATIVE]`

A transition is `(state_before, action, state_after)` plus the evidence offered. The
verifier returns a `Verdict` of **VALID**, **INVALID** or **UNRESOLVED**, and UNRESOLVED
**MUST NOT** be reported as INVALID (**HML-TRANS-001**).

A conforming verifier **MUST** check all **11** invariants and report violations as findings
carrying an `ErrorClass` (**HML-INV-001**…**HML-INV-011**):

`DEPENDENCY` · `SCOPE` · `PRECONDITIONS` · `OBLIGATIONS` · `CANDIDATES` · `BRANCH_JOIN` ·
`WARRANT` · `EPISTEMIC_STATUS` · `GOAL_DISCHARGE` · `TYPE_DOMAIN` · `FRAME`

### The kernel

**20** inference rules, no more (**HML-KERNEL-001**…**HML-KERNEL-020**). Full shapes,
arities, obligations and side conditions are in `REFERENCE.md` and `spec/20_verification.md`,
generated from the implementation.

Equality: `reflexivity`, `symmetry`, `transitivity`, `substitute`, `congruence`.
Propositional: `modus_ponens`, `modus_tollens`, `and_intro`, `and_elim_left`,
`and_elim_right`. Quantifier: `forall_intro`, `forall_elim`, `exists_intro`.
Arithmetic/order: `add_both_sides`, `subtract_both_sides`, `multiply_both_sides`,
`divide_both_sides`, `add_inequality`, `multiply_inequality`, `weaken_inequality`.

`divide_both_sides` emits a nonzero obligation; `multiply_inequality` carries a sign side
condition. Partiality is discharged through obligations, never assumed.

## 7. Model-facing language  `[NORMATIVE]`

Frozen at `b011511` as `R6_SHIPPED_VIEW` = `src/hamiltonian_lang/semantic_state/view.py`.

The serialization **MUST** be **lossless**: `parse(render(S)) == S` under structural
equality of the whole transition (**HML-REP-001**).

It **MUST** be **deterministic**: if `A == B` then `render(A) == render(B)`. Emission order
**MUST NOT** depend on mapping construction order (**HML-REP-002**). Records are emitted in
dependency-topological order within canonical role blocks.

It **MUST** carry **decoded UTF-8**. A model-facing payload **MUST NOT** contain `\uXXXX`
escape sequences standing for mathematical characters (**HML-REP-003**).

Canonical identity documents **MUST** remain ASCII (**HML-REP-004**). This is deliberately
the opposite of the previous rule: **identity documents stay ASCII, model-facing surfaces
stay literal.** They are different artifacts with different consumers, and the asymmetry is
intentional.

The state rendering **MUST NOT** leak the action to be predicted from it (**HML-REP-005**).

### Why HML-REP-003 exists

A shipped 50K corpus carried a view *named* `HML_WORKED_UTF8` in which 500/500 sampled rows
contained literal `\uXXXX` text — 31 sequences per row, **15.2% of every prompt** — while
the matched neutral view carried real glyphs. Under the Qwen3-8B tokenizer `⊢` is **1**
token and its escaped spelling is **5**. The same defect was previously measured at
**−3.41pp** of task accuracy, 2.5× the effect the experiment existed to detect, landing
asymmetrically on HML.

The corpus's own Unicode audit reported PASS on that data, because it counted *JSON-level*
escapes while the escaping had happened upstream inside the string value. **A conforming
Unicode audit MUST inspect decoded payload strings, not encoder flags.**

## 8. Backends  `[NORMATIVE]`

A backend that cannot express a construct **MUST** declare the loss through `drop()`,
`approximate()` or `weaken()`. Silent omission **MUST NOT** occur (**HML-BACK-001**) — a
backend that quietly drops a construct produces authoritative-looking output that is wrong,
which is the worst available failure mode.

## 9. Libraries and policy  `[INFORMATIVE]`

Implemented libraries: `algebra`, `calculus`, `numerical`, `probability`, `theorem`.

The semantic closure audit deliberately declined to promote category theory, causal
intervention, filtrations and numerical approximation families into the kernel. The atlas
records **61** concepts as `LIBRARY_GAP` — representable today, reasoning still to be built.

## 10. Prohibited conflations  `[NORMATIVE]`

These **MUST NOT** be given a subtyping path or collapsed by any implementation:

- a `Distribution[T]` is not a value of `T`;
- a `RandomVariable[T]` is not a `Distribution[T]` and is not a `T`;
- `=` is not `~` and is not approximation;
- `=>` is not correlation and is not causation;
- `Probability` is not `PositiveReal` — they are incomparable, meeting at `NonNegativeReal`;
- a candidate is not a claim; evidence is not truth; UNKNOWN is not FALSE.

## 11. Status of the state-delta language  `[EXPERIMENTAL]`

The state-delta form is **SPECIFIED_NOT_FROZEN** and is **NOT normative in 1.0**.
`VERSION.json` records `"normative_state_delta": false`.

It is specified because it is measurably worth doing — **18.8%** of every model-facing
prompt re-emits records unchanged between `state_before` and `state_after` — and it is not
frozen because it changes the task rather than the surface, and because that measurement
was taken on states carrying 1.00 claims.

## 12. Governance  `[NORMATIVE]`

A frozen semantic feature **MUST NOT** be changed because a model performs badly, another
notation looks prettier, an LLM proposes a feature, a book uses another abstraction, or a
benchmark disappoints (**HML-VER-002**).

Unfreezing **REQUIRES** all of: a concrete mathematical state; proof that current HML cannot
represent it losslessly; independent mathematical validation; a minimal failing executable
counterexample; classification as a genuine `CORE_GAP`; a regression test; an explicit
version bump.

A conforming artifact **MUST** record the semantic implementation commit and the model
language commit it was produced against (**HML-VER-001**).

---

Full rule text, implementation pointers and conformance specimens: `standard/rules.json`,
`TRACEABILITY.md`, `spec/`.
