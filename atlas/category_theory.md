# Category Theory

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| category | objects and morphisms | ConceptType -- explicitly library-level | yes | yes | LIBRARY | **LIBRARY_GAP** |
| morphism | structure-preserving arrow | FunctionType or declared relation | yes | yes | LIBRARY | **LIBRARY_GAP** |
| functor | map between categories | FunctionType over ConceptTypes | yes | no | LIBRARY | **LIBRARY_GAP** |
| natural transformation | map between functors | not represented in 1.0 | no | no | UNSUPPORTED | **UNSUPPORTED** |

## Notes

- **category** — the closure audit placed category theory at library level, not kernel
- **natural transformation** — no counterexample has demonstrated a need
