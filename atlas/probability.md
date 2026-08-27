# Probability

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| probability | measure of an event | QuantityType Probability -- NOT PositiveReal | yes | yes | CORE | **NO_GAP** |
| event | measurable subset | EventType | yes | yes | CORE | **NO_GAP** |
| random variable | measurable function on a sample space | RandomVariableType | yes | yes | CORE | **NO_GAP** |
| distribution | law of a random variable | DistributionType | yes | yes | CORE | **NO_GAP** |
| conditional probability | P(A|B) | proposition with a P(B) > 0 Obligation | yes | yes | CORE | **NO_GAP** |
| expectation | mean of an RV | FunctionType RandomVariableType -> Real | yes | yes | LIBRARY | **NO_GAP** |
| variance | second central moment | FunctionType | yes | yes | LIBRARY | **NO_GAP** |
| independence | joint factorises | Predicate over RandomVariableTypes | yes | yes | LIBRARY | **LIBRARY_GAP** |

## Notes

- **probability** — Probability and PositiveReal are incomparable by design
- **random variable** — an RV is not a Distribution and not a value of T
- **conditional probability** — partiality machinery carries the positivity obligation
- **expectation** — libraries/probability.py
