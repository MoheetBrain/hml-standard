# Linear Algebra

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| vector | element of a vector space | VectorType with Dimension | yes | yes | CORE | **NO_GAP** |
| matrix | linear map in coordinates | MatrixType with Dimension | yes | yes | CORE | **NO_GAP** |
| tensor | multilinear object | TensorType | yes | yes | CORE | **NO_GAP** |
| vector space | the ambient structure | ConceptType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| linear map | structure-preserving map | FunctionType between VectorTypes | yes | yes | LIBRARY | **LIBRARY_GAP** |
| matrix product | composition | term; dimension compatibility is a type/domain check | yes | yes | CORE | **NO_GAP** |
| eigenvalue | scalar with an eigenvector | Claim over MatrixType and ScalarType | yes | no | BACKEND | **BACKEND_GAP** |

## Notes

- **matrix product** — TYPE_DOMAIN invariant rejects incompatible shapes
- **eigenvalue** — numeric spectra need a backend
