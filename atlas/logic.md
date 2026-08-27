# Logic

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| variable | a name bound in a context | binder in a Claim proposition; identity by binding ID, not spelling | yes | yes | CORE | **NO_GAP** |
| constant | a fixed term | term inside a proposition; ScalarType or a declared Object | yes | yes | CORE | **NO_GAP** |
| equality | a = b | proposition; kernel rules reflexivity, symmetry, transitivity, substitute, congruence | yes | yes | CORE | **NO_GAP** |
| implication | P => Q | proposition; kernel modus_ponens, modus_tollens | yes | yes | CORE | **NO_GAP** |
| conjunction | P and Q | proposition; kernel and_intro, and_elim_left, and_elim_right | yes | yes | CORE | **NO_GAP** |
| disjunction | P or Q | proposition; case analysis via Branch with a partition_id | yes | yes | LIBRARY | **LIBRARY_GAP** |
| negation | not P | proposition; ClaimStatus.REFUTED records a refuted claim | yes | yes | LIBRARY | **LIBRARY_GAP** |
| universal quantifier | forall x, P x | proposition; kernel forall_intro, forall_elim with freshness side conditions | yes | yes | CORE | **NO_GAP** |
| existential quantifier | exists x, P x | proposition; kernel exists_intro | yes | yes | CORE | **NO_GAP** |
| existential witness | the term proving exists | the instantiating term recorded in the action's args | yes | yes | CORE | **NO_GAP** |
| induction | proof by induction | a Goal plus Branches for base and step, with Obligations | yes | yes | LIBRARY | **LIBRARY_GAP** |
| UNKNOWN / unresolved | truth value not determined | ClaimStatus.UNKNOWN, Verdict.UNRESOLVED, ObligationState.UNKNOWN | yes | yes | CORE | **NO_GAP** |

## Notes

- **equality** — five of the 20 kernel rules are equality rules
- **disjunction** — branches carry the case split; no disjunction elimination rule in the kernel
- **existential quantifier** — exists_elim (witness extraction) is not a kernel rule
- **induction** — the schema is representable; the induction principle is library-level
- **UNKNOWN / unresolved** — first-class, never collapsed to FALSE
