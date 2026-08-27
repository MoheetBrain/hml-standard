# Binders and scope

*HML Standard 1.0 — 2026-08-27*

Binding, alpha-equivalence, capture avoidance and scope visibility.

[NORMATIVE] Binders are locally nameless. Alpha-renaming MUST NOT change meaning, and
capture MUST be avoided by construction rather than by hygiene convention.

Scope visibility is decided by **membership** in `SemanticState.active_scopes`, not by
ordering (HML-STATE-004). A fact established inside a frame that is no longer active is not
visible, which is what stops a branch-local conclusion leaking into global state without a
join.

Binder identity *inside a proposition* is not HML's when the proposition is opaque source
text -- see `MODEL_REFERENCE.md` and the identifier policy in the model-language freeze.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
