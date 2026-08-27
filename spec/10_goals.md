# Goals

*HML Standard 1.0 — 2026-08-27*

The Goal record and goal discharge.

[NORMATIVE] A `Goal` carries a proposition, a `GoalStatus` of OPEN, DISCHARGED or UNKNOWN,
and a scope. Discharge is governed by the GOAL_DISCHARGE invariant (HML-INV-009): a goal
MUST NOT become DISCHARGED except through an action whose `goal_effect` says so and whose
warrant licenses it.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
