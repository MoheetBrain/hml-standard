# divide_creates_obligation

Dividing both sides is a kernel rule that emits a nonzero obligation. Partiality is discharged through proof debt, never assumed.

Round-trips: `parse(render(t)) == t`.

```
transition EX-ALG-1
  schema "semantic-firewall-case-0.1.0"

state before
  scopes global
  claim h1
    proposition "a * x = b"
    status GIVEN
  claim h2
    proposition "a ≠ 0"
    status GIVEN
  obligation o1
    proposition "a ≠ 0"
    status OPEN
    mandatory true
    origin "divide_both_sides"
    depends h2

action a1
  operation "KERNEL_RULE"
  summary "divide_both_sides"
  output d1
  depends h1
  obligations_created [{"id": "o1", "proposition": "a ≠ 0"}]
  warrant {"rule": "divide_both_sides"}

state after
  scopes global
  claim h1
    proposition "a * x = b"
    status GIVEN
  claim h2
    proposition "a ≠ 0"
    status GIVEN
  obligation o1
    proposition "a ≠ 0"
    status OPEN
    mandatory true
    origin "divide_both_sides"
    depends h2

```
