# Glossary

*HML Standard 1.0*  `[INFORMATIVE]` — normative definitions live in `STANDARD.md` and `spec/`.

**Action** — a structural description of a reasoning step: operation, dependencies, warrant,
preconditions, obligations created and discharged, and five effect maps. Not a name.

**Active scope** — a member of `SemanticState.active_scopes`. A claim is visible only if its
scope is active.

**Atlas** — the mathematics→HML map. Answers whether HML can *carry* a concept's reasoning
state, not whether HML can prove it.

**Attestation** — the separate, trusted step by which evidence is certified. A generator
cannot perform it on its own behalf.

**Backend** — a translation target (Lean, LaTeX, SymPy, Stan, English…). Must declare
translation loss through `drop`/`approximate`/`weaken`.

**Branch** — one case of a split, grouped with its siblings by `partition_id`. Branch-local
conclusions require a join to escape.

**Candidate** — a proposed object that is not a fact. Its status vocabulary cannot express
GIVEN or DERIVED, so it cannot be promoted by relabelling.

**Canonical identity document** — the ASCII-encoded hashing form in `backends/canonical.py`.
Deliberately not the model-facing surface.

**Claim** — a proposition asserted in a scope, carrying a `ClaimStatus`.

**CORE_GAP** — a demonstrated inability of the semantic core to represent a mathematical
reasoning state. The only class of finding that can justify a semantic unfreeze. **Zero**
were found across the 110 atlas concepts.

**Determinism (of the renderer)** — if `A == B` then `render(A) == render(B)`. Not automatic:
mappings compare by content, so a renderer walking insertion order violates it.

**Evidence** — what attests to a transition. Distinct from the **warrant**, which is what
licenses it. Defaults to `trusted=False`, `status=UNKNOWN`.

**Goal** — what is being proved. Discharge is governed by the `GOAL_DISCHARGE` invariant.

**Invariant** — one of the 11 checks a conforming verifier runs on every transition.

**Kernel** — the 20 inference rules. Deliberately small; everything else is library, backend
or policy.

**LIBRARY_GAP** — representable today; the domain reasoning is not built. **Not** a language
defect and **not** grounds for unfreezing.

**Lossless** — `parse(render(S)) == S` under structural equality of the whole object.

**Obligation** — proof debt. Defaults to `mandatory=True`, `status=OPEN`. Persists until
discharged with attested evidence.

**Semantic state** — five record mappings plus active scopes. Immutable.

**State delta** — the `S_t + Δ → S_t+1` form. `SPECIFIED_NOT_FROZEN`; **not normative** in
1.0.

**UNKNOWN** — a value, not an absence. Never FALSE, never a default, never a missing field.

**UNRESOLVED** — a `Verdict` distinct from INVALID. "I could not decide" is not "this is
wrong."

**Warrant** — what licenses an action: a rule, a theorem name, a reference to evidence.
