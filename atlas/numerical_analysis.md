# Numerical Analysis

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| floating-point value | finite-precision number | ScalarType with a bounded-error Claim | yes | yes | LIBRARY | **NO_GAP** |
| error bound | |computed - exact| <= eps | the frozen bounded-error library concept | yes | yes | LIBRARY | **NO_GAP** |
| convergence rate | how fast error shrinks | Claim over an indexed family | yes | yes | LIBRARY | **LIBRARY_GAP** |
| numerical method result | output of an algorithm | Claim with BACKEND_CERTIFIED evidence | yes | no | BACKEND | **BACKEND_GAP** |

## Notes

- **floating-point value** — approximation is never equality
