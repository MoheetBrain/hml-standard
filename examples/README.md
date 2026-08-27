# Examples

*HML Standard 1.0 — rendered by the frozen implementation at the pinned commit, not written by hand.*

- [`minimal/single_claim`](minimal/single_claim.md) — The smallest well-formed transition: one GIVEN claim and one action.
- [`minimal/unknown_is_explicit`](minimal/unknown_is_explicit.md) — UNKNOWN is a value. It is rendered, round-trips, and is never a missing field.
- [`algebra/divide_creates_obligation`](algebra/divide_creates_obligation.md) — Dividing both sides is a kernel rule that emits a nonzero obligation. Partiality is discharged through proof debt, never assumed.
- [`calculus/goal_and_obligation`](calculus/goal_and_obligation.md) — An open goal alongside outstanding proof debt. Both are visible; neither is implied by the other.
- [`probability/conditional_probability_obligation`](probability/conditional_probability_obligation.md) — P(A|B) carries a P(B) > 0 obligation. Probability is its own quantity type and is not PositiveReal.
- [`reasoning/candidate_is_not_a_fact`](reasoning/candidate_is_not_a_fact.md) — A candidate sits beside the claims and cannot be promoted by relabelling: CandidateStatus cannot express GIVEN or DERIVED.
- [`reasoning/branch_local_scope`](reasoning/branch_local_scope.md) — A branch-local claim lives in its own scope. It is invisible until that scope is active, and cannot escape without a join.
