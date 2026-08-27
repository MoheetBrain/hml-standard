# conditional_probability_obligation

P(A|B) carries a P(B) > 0 obligation. Probability is its own quantity type and is not PositiveReal.

Round-trips: `parse(render(t)) == t`.

```
transition EX-PROB-1
  schema "semantic-firewall-case-0.1.0"

state before
  scopes global
  claim h1
    proposition "A, B : Event"
    status GIVEN
    domain "Event"
  claim h2
    proposition "P(B) > 0"
    status GIVEN
  obligation o1
    proposition "P(B) > 0"
    status OPEN
    mandatory true
    origin "conditional_probability"
    depends h2

action a1
  operation "DEFINE"
  summary "P(A|B) = P(A ∩ B) / P(B)"
  output d1
  depends h1, h2
  typing {"result": "Probability"}

state after
  scopes global
  claim h1
    proposition "A, B : Event"
    status GIVEN
    domain "Event"
  claim h2
    proposition "P(B) > 0"
    status GIVEN
  obligation o1
    proposition "P(B) > 0"
    status OPEN
    mandatory true
    origin "conditional_probability"
    depends h2

```
