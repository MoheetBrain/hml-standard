# Scope

*HML Standard 1.0 — 2026-08-27*

What HML 1.0 standardises and what it deliberately leaves to libraries, backends and policy.

HML 1.0 standardises the **typed semantic state and the checked transition between
states**, plus the model-facing serialization of that state.

It does **not** standardise: which theorems are true, how to search for a proof, how a
model should be trained, or how an external prover works. Those are library, policy and
backend concerns, and the Standard says so explicitly wherever the boundary falls.

The kernel is deliberately small: **20 inference rules**. A concept whose theorems live in
a library is not a deficiency of the language. The question the Standard asks of every
mathematical concept is whether HML can **carry its reasoning state losslessly** -- see
`SEMANTIC_ATLAS.md`.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
