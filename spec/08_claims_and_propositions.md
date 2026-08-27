# Claims and propositions

*HML Standard 1.0 — 2026-08-27*

The Claim record and the proposition it carries.

[NORMATIVE] A `Claim` is the primary carrier of mathematical
content. It has an `id`, a `proposition`, a `ClaimStatus`, a `scope`, an optional `domain`,
and `dependencies`.

**Status is not decoration.** `ClaimStatus` is a closed vocabulary — GIVEN, ASSUMED, DERIVED,
VERIFIED, REFUTED, UNRESOLVED, UNKNOWN (HML-ENUM-003) — and it is the field that separates a
hypothesis from a fact. An action MUST NOT change a claim's status except through an
`epistemic_effect` that the `EPISTEMIC_STATUS` invariant (HML-INV-008) accepts.

**The proposition may be opaque.** In the current corpus a proposition is the pretty-printed
text of a Lean goal state, and HML carries it verbatim rather than routing it through the AST
printer. This is deliberate: routing it would make the view lossless only up to canonical
form and would couple the Standard to a grammar the corpus never agreed to. The consequence
is stated plainly in `07_binders_and_scope.md` — binder identity *inside* an opaque
proposition is Lean's, not HML's.

**Visibility.** A claim is citable only if its `scope` is a member of `active_scopes`
(HML-STATE-004). Ordering is irrelevant; membership is decisive.

**Dependencies.** A claim's `dependencies` are the claims it was derived from. They MUST
resolve (HML-INV-001), and the model-facing serialization emits claims in
dependency-topological order so a claim appears after everything it cites.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
