# Real Analysis

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| real number | element of R | ScalarType Real | yes | yes | CORE | **NO_GAP** |
| supremum | least upper bound | term with an existence Obligation | yes | yes | LIBRARY | **LIBRARY_GAP** |
| convergence | sequence tends to a limit | proposition over an indexed family | yes | yes | LIBRARY | **LIBRARY_GAP** |
| bounded error | |x - y| <= eps | the frozen bounded-error library concept; zero new primitives | yes | yes | LIBRARY | **NO_GAP** |
| uniform continuity | delta independent of point | Predicate; quantifier order is preserved | yes | yes | LIBRARY | **LIBRARY_GAP** |

## Notes

- **bounded error** — explicitly NOT equality -- the closure audit refused that conflation
- **uniform continuity** — quantifier scope is carried, which is the point
