# Candidates

*HML Standard 1.0 — 2026-08-27*

Proposed objects that are not yet facts.

[NORMATIVE] A `Candidate` is a proposed object that is **not** a fact. `CandidateStatus`
(PROPOSED, UNVERIFIED, VERIFIED, REJECTED, UNKNOWN) cannot express GIVEN or DERIVED, so
promotion cannot be performed by relabelling -- it requires an action and is checked by the
CANDIDATES invariant (HML-INV-005, HML-EPIS-002).

`Candidate.constraint_ids` links a candidate to the obligations that constrain it.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
