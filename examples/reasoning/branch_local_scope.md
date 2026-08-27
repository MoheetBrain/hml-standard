# branch_local_scope

A branch-local claim lives in its own scope. It is invisible until that scope is active, and cannot escape without a join.

Round-trips: `parse(render(t)) == t`.

```
transition EX-REA-2
  schema "semantic-firewall-case-0.1.0"

state before
  scopes global, branch_1
  claim b_fact
    proposition "x ≤ 1"
    status ASSUMED
    scope branch_1
  claim h1
    proposition "x : ℝ"
    status GIVEN
  branch b1
    predicate "x ≤ 1"
    status OPEN
    scope branch_1
    partition split_1

action a1
  operation "OPEN_BRANCH"
  scope_effect {"opens": "branch_1"}
  branch_effect {"opens": "b1"}

state after
  scopes global, branch_1
  claim b_fact
    proposition "x ≤ 1"
    status ASSUMED
    scope branch_1
  claim h1
    proposition "x : ℝ"
    status GIVEN
  branch b1
    predicate "x ≤ 1"
    status OPEN
    scope branch_1
    partition split_1

```
