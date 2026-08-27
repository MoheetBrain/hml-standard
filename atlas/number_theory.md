# Number Theory

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| integer | element of Z | ScalarType Integer | yes | yes | CORE | **NO_GAP** |
| divisibility | a divides b | proposition | yes | yes | LIBRARY | **LIBRARY_GAP** |
| prime | irreducible integer | Predicate over Integer | yes | yes | LIBRARY | **LIBRARY_GAP** |
| modular arithmetic | congruence | proposition; term-level mod | yes | yes | LIBRARY | **LIBRARY_GAP** |
| gcd | greatest common divisor | FunctionType Integer x Integer -> Integer | yes | yes | LIBRARY | **LIBRARY_GAP** |
