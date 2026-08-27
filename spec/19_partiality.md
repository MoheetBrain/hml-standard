# Partiality

*HML Standard 1.0 — 2026-08-27*

Partial operations, preconditions and term-level bounds obligations.

[NORMATIVE] Partial operations carry their preconditions as **obligations**, not as silent
assumptions. Division emits a nonzero obligation; a finite index access is either statically
refuted or carries a term-level bounds obligation built from the resolved `SymbolicExtent`.

This is why `divide_both_sides` appears in the kernel with an obligation attached rather
than as an unconditional rewrite.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
