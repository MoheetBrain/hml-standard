# Differential Equations

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| differential equation | relation involving derivatives | proposition over FunctionType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| initial condition | value at a point | Claim with ClaimStatus.GIVEN | yes | yes | CORE | **NO_GAP** |
| solution | function satisfying the equation | Claim; existence/uniqueness as Obligations | yes | yes | BACKEND | **BACKEND_GAP** |

## Notes

- **solution** — numeric solution needs a backend
