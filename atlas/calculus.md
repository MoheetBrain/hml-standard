# Calculus

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| limit | lim f(x) as x -> a | proposition; epsilon-delta as nested quantifiers | yes | yes | LIBRARY | **LIBRARY_GAP** |
| derivative | instantaneous rate | FunctionType; libraries/calculus.py | yes | yes | LIBRARY | **NO_GAP** |
| integral | accumulation | term; libraries/calculus.py | yes | yes | LIBRARY | **NO_GAP** |
| continuity | topological/epsilon-delta property | Predicate over FunctionType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| partial derivative | derivative in one coordinate | FunctionType over ProductType | yes | yes | LIBRARY | **LIBRARY_GAP** |
