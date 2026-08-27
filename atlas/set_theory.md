# Set Theory

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| set | a collection | SetType | yes | yes | CORE | **NO_GAP** |
| membership | x in S | proposition over SetType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| subset | A subset B | proposition | yes | yes | LIBRARY | **LIBRARY_GAP** |
| union / intersection | set operations | term-level operations over SetType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| power set | set of subsets | SetType over SetType | yes | no | LIBRARY | **LIBRARY_GAP** |
| indexed family | family over an index set | SymbolicExtent with a resolved finite shape | yes | yes | CORE | **NO_GAP** |
| cardinality | size of a set | QuantityType; finite cardinality via SymbolicExtent | yes | no | LIBRARY | **LIBRARY_GAP** |

## Notes

- **indexed family** — finite index bounds carry term-level obligations
- **cardinality** — infinite cardinal arithmetic is UNSUPPORTED in 1.0
