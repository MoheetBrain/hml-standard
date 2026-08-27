# Branches

*HML Standard 1.0 — 2026-08-27*

Case analysis, branch-local state and joins.

[NORMATIVE] A `Branch` carries a predicate, a `BranchStatus` (OPEN, CLOSED, JOINED,
ABANDONED, UNKNOWN), a scope and an optional `partition_id` grouping the cases of one split.

Branch-local conclusions MUST NOT escape without a join; the BRANCH_JOIN invariant
(HML-INV-006) checks it. Disjunction elimination itself is library-level -- the branch
records the case split, the kernel does not discharge it.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
