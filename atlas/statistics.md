# Statistics

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| estimator | function of a sample | FunctionType; RandomVariableType output | yes | yes | LIBRARY | **LIBRARY_GAP** |
| hypothesis | a claim under test | Claim with ClaimStatus.ASSUMED | yes | yes | CORE | **NO_GAP** |
| p-value | tail probability | QuantityType Probability | yes | yes | LIBRARY | **LIBRARY_GAP** |
| confidence interval | interval estimate | term with a coverage Claim | yes | yes | LIBRARY | **LIBRARY_GAP** |
| regression model | structural relation | ConceptType; examples/statistics | yes | yes | BACKEND | **BACKEND_GAP** |

## Notes

- **hypothesis** — a hypothesis is not a fact -- status carries the distinction
- **regression model** — fitting is a backend concern (Stan)
