# Optimization

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| objective function | quantity to optimise | FunctionType -> Real | yes | yes | CORE | **NO_GAP** |
| constraint | restriction on the feasible set | Obligation or a constraint Claim | yes | yes | CORE | **NO_GAP** |
| feasible point | satisfies all constraints | Candidate with CandidateStatus | yes | yes | CORE | **NO_GAP** |
| optimality | no better feasible point | Claim; certificate as evidence | yes | yes | BACKEND | **BACKEND_GAP** |

## Notes

- **constraint** — Candidate.constraint_ids links a candidate to its constraints
