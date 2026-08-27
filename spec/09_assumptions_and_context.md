# Assumptions and context

*HML Standard 1.0 — 2026-08-27*

Assumed claims, refinement context and active frames.

[NORMATIVE] An assumption is a `Claim` with `ClaimStatus.ASSUMED`. It is not a fact, and no
action may silently relabel it. Refinement context, scoped assumptions and active frames
are carried explicitly; the FRAME invariant (HML-INV-011) checks that a transition does not
alter state it did not declare it would.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
