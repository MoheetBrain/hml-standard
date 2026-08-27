# candidate_is_not_a_fact

A candidate sits beside the claims and cannot be promoted by relabelling: CandidateStatus cannot express GIVEN or DERIVED.

Round-trips: `parse(render(t)) == t`.

```
transition EX-REA-1
  schema "semantic-firewall-case-0.1.0"

state before
  scopes global
  claim h1
    proposition "x > 0"
    status GIVEN
  candidate c1
    proposition "√x < x"
    status PROPOSED
    origin "heuristic"
    depends h1
  goal g1
    proposition "√x < x"
    status OPEN

action a1
  operation "PROPOSE"
  output c1
  candidate_effect {"proposes": "c1"}

state after
  scopes global
  claim h1
    proposition "x > 0"
    status GIVEN
  candidate c1
    proposition "√x < x"
    status PROPOSED
    origin "heuristic"
    depends h1
  goal g1
    proposition "√x < x"
    status OPEN

```
