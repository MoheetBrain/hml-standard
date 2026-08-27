# unknown_is_explicit

UNKNOWN is a value. It is rendered, round-trips, and is never a missing field.

Round-trips: `parse(render(t)) == t`.

```
transition EX-MIN-2
  schema "semantic-firewall-case-0.1.0"

state before
  scopes global
  claim p0
    proposition "P x"
    status UNKNOWN

action a1
  operation "INSPECT"

state after
  scopes global
  claim p0
    proposition "P x"
    status UNKNOWN

```
