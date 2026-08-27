# HML model reference

*HML Standard 1.0 · what a model needs to operate the language.*

Mechanically traceable to `STANDARD.md`. Where this file states a rule it cites the rule ID;
there is no independent prose to drift.

## What HML is

A typed representation of mathematical **reasoning state**. You read a state, choose an
action, and the action produces the next state. You do not decide what is true — a verifier
does. Your job is to propose a **useful, legal** next action.

## The state you will see

```
transition <case_id>
  schema "semantic-firewall-case-0.1.0"
  source {...}

state before
  scopes global
  claim p0
    proposition "x : ℝ\n0 ≤ x\n⊢ √x ≤ x"
    status GIVEN
    domain "Proposition"
  goal g1
    proposition "..."
    status OPEN
  obligation o1
    proposition "x ≠ 0"
    status OPEN
    mandatory true

action a1
  operation "LEAN_TACTIC"
  depends p0
  warrant {"rule": "LEAN_TACTIC"}

evidence e1
  kind "FORMAL_TRACE"
  status "VALID"

state after
  ...
```

Records appear in dependency-topological order: a record comes after everything it cites.
The same state always renders the same way (HML-REP-002).

## The five record kinds and what they mean

| you see | it means | it is NOT |
|---|---|---|
| `claim` | something asserted in a scope | necessarily true — check `status` |
| `candidate` | something **proposed** | a fact |
| `branch` | one case of a split | globally true |
| `goal` | what is being proved | already proved |
| `obligation` | outstanding proof debt | optional, if `mandatory true` |

## Statuses — closed vocabularies

- `ClaimStatus` — GIVEN · ASSUMED · DERIVED · VERIFIED · REFUTED · UNRESOLVED · UNKNOWN
- `CandidateStatus` — PROPOSED · UNVERIFIED · VERIFIED · REJECTED · UNKNOWN
- `BranchStatus` — OPEN · CLOSED · JOINED · ABANDONED · UNKNOWN
- `GoalStatus` — OPEN · DISCHARGED · UNKNOWN
- `ObligationState` — OPEN · DISCHARGED · FAILED · UNKNOWN
- `Verdict` — VALID · INVALID · UNRESOLVED

Nothing outside these lists is legal (HML-ENUM-*).

## The action you produce

Structural, never a bare operation name (HML-ACT-001):

```
action a2
  operation "APPLY_THEOREM"
  output d1
  depends p0, h2
  warrant {"rule": "THEOREM", "name": "Real.sqrt_le_self"}
  obligations_created [{"id": "o2", "proposition": "0 ≤ x"}]
  goal_effect {"advances": "g1"}
```

Every id you cite **must** already exist in `state before` (HML-ACT-002).

## Rules you must not break

1. **UNKNOWN is a value.** Never treat it as false, missing, or a default (HML-EPIS-001).
2. **A candidate is not a fact.** You may propose promotion; you may not assert it
   (HML-EPIS-002).
3. **You cannot certify yourself.** Never assert your own verification status
   (HML-EPIS-004).
4. **Obligations do not vanish.** A mandatory obligation persists until discharged with
   attested evidence (HML-OBL-001).
5. **Scope is membership.** A claim in an inactive scope is not available to you
   (HML-STATE-004).
6. **Evidence is not truth.** `trusted false` evidence discharges nothing (HML-EPIS-003).
7. **Cite only what exists.** An unresolvable reference is `MISSING_DEPENDENCY`
   (HML-ACT-002).
8. **Write real glyphs.** `⊢`, `∀`, `ℝ`, `√` — never `⊢`-style escapes (HML-REP-003).

## Distinctions that are enforced, not stylistic

- a `Distribution[T]` is not a value of `T`
- a `RandomVariable[T]` is neither a `Distribution[T]` nor a `T`
- `=` is not `~` and is not approximation
- `=>` is not correlation and is not causation
- `Probability` is not `PositiveReal`

## When you do not know

Say so. `UNRESOLVED` and `UNKNOWN` are legal, useful answers. A confidently wrong action is
worse than an honest refusal, because the verifier can act on a refusal and cannot detect
misplaced confidence.

## The 20 kernel rules available

Equality — `reflexivity` `symmetry` `transitivity` `substitute` `congruence`
Propositional — `modus_ponens` `modus_tollens` `and_intro` `and_elim_left` `and_elim_right`
Quantifier — `forall_intro` `forall_elim` `exists_intro`
Arithmetic / order — `add_both_sides` `subtract_both_sides` `multiply_both_sides`
`divide_both_sides` `add_inequality` `multiply_inequality` `weaken_inequality`

`divide_both_sides` creates a nonzero obligation. `multiply_inequality` has a sign side
condition. `forall_intro` has a freshness side condition.

Anything else is a library or backend concern, not a kernel step.

## Tasks the interface supports

| task | input | output |
|---|---|---|
| `STATE_COMPREHENSION` | `(S, P)` | ENTAILED / CONTRADICTED / INFORMATIVE / UNRESOLVED |
| `ACTION_VALIDITY` | `(S, a)` | VALID / INVALID / UNKNOWN |
| `ACTION_RANKING` | `(S, a, G)` | usefulness |
| `TRANSITION` | `(S, a)` | ΔS |
| `OBLIGATION_PREDICTION` | `(S, a)` | obligations |

**Caveat that must travel with this table.** On current data `ACTION_VALIDITY` distinguishes
`FORMAL_TRACE` from `UNRESOLVED`, not valid from invalid — distractors are plausible and
unexecuted, never labelled invalid. `OBLIGATION_PREDICTION` has no corpus support at all.
