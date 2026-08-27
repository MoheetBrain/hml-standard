# Graph Theory

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| graph | vertices and edges | ConceptType over SetType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| path | sequence of adjacent vertices | SymbolicExtent-indexed family | yes | yes | LIBRARY | **LIBRARY_GAP** |
| connectivity | existence of paths | Predicate; existential proposition | yes | yes | LIBRARY | **LIBRARY_GAP** |
| graph algorithm result | e.g. shortest path | Claim with BACKEND_CERTIFIED evidence | yes | no | BACKEND | **BACKEND_GAP** |
