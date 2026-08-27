# Combinatorics

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| finite sequence | ordered tuple | ProductType or SymbolicExtent-indexed family | yes | yes | CORE | **NO_GAP** |
| binomial coefficient | n choose k | FunctionType with a k <= n obligation | yes | yes | LIBRARY | **LIBRARY_GAP** |
| permutation | bijection of a finite set | FunctionType with a bijectivity Claim | yes | yes | LIBRARY | **LIBRARY_GAP** |
| counting argument | bijective/double counting | Goal plus Claims; no dedicated machinery | yes | yes | LIBRARY | **LIBRARY_GAP** |

## Notes

- **binomial coefficient** — the bound is a term-level obligation
