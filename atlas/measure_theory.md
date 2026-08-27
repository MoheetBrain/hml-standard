# Measure Theory

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| measurable space | set with a sigma-algebra | ConceptType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| measure | sigma-additive set function | FunctionType SetType -> Real | yes | yes | LIBRARY | **LIBRARY_GAP** |
| measurable function | preimages measurable | Predicate over FunctionType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| filtration | increasing family of sigma-algebras | indexed family; explicitly library-level | yes | yes | LIBRARY | **LIBRARY_GAP** |
| almost everywhere | up to a null set | qualified proposition | yes | yes | LIBRARY | **LIBRARY_GAP** |

## Notes

- **filtration** — the closure audit placed filtrations at library level
