# Algebra

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| group | set with associative op, identity, inverses | ConceptType with declared axioms as Claims | yes | yes | LIBRARY | **LIBRARY_GAP** |
| ring | two operations | ConceptType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| field | ring with division | ConceptType; division introduces a nonzero Obligation | yes | yes | LIBRARY | **LIBRARY_GAP** |
| polynomial | formal sum | term; libraries/algebra.py | yes | yes | LIBRARY | **NO_GAP** |
| equation solving | isolate a variable | kernel add/subtract/multiply/divide_both_sides | yes | yes | CORE | **NO_GAP** |
| inequality | a <= b | proposition; kernel weaken_inequality, add_inequality, multiply_inequality | yes | yes | CORE | **NO_GAP** |

## Notes

- **group** — the closure audit explicitly declined to pretend Group into the kernel
- **field** — partiality machinery carries the x != 0 obligation
- **equation solving** — divide_both_sides emits a nonzero obligation
- **inequality** — multiply_inequality carries a sign side condition
