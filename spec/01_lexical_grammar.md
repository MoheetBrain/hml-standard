# Lexical grammar

*HML Standard 1.0 — 2026-08-27*

Token-level structure of the surface language.

[INFORMATIVE] The HML surface language has a conventional lexical structure implemented in
`src/hamiltonian_lang/lexer/`. It is **not** the model-facing boundary: a model reads the
serialization specified in `24_model_language.md`, which is a separate surface with its own
reader and is not routed through this grammar.

No normative rule in HML 1.0 depends on surface token spelling. Identity is carried by
binding IDs and record keys, not by how a name is written.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
