# Epistemic status

*HML Standard 1.0 — 2026-08-27*

The closed status vocabularies and the UNKNOWN discipline.

## Normative rules (11)

#### HML-ENUM-001 — BranchStatus  `[NORMATIVE]`

`BranchStatus` is a closed vocabulary. A conforming implementation MUST accept exactly ['OPEN', 'CLOSED', 'JOINED', 'ABANDONED', 'UNKNOWN'] and MUST reject any other value.

Closed vocabulary: `['OPEN', 'CLOSED', 'JOINED', 'ABANDONED', 'UNKNOWN']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `BranchStatus`
  ·  Conformance: `conformance/invalid/enum_branchstatus_unknown_member`

#### HML-ENUM-002 — CandidateStatus  `[NORMATIVE]`

`CandidateStatus` is a closed vocabulary. A conforming implementation MUST accept exactly ['PROPOSED', 'UNVERIFIED', 'VERIFIED', 'REJECTED', 'UNKNOWN'] and MUST reject any other value.

Closed vocabulary: `['PROPOSED', 'UNVERIFIED', 'VERIFIED', 'REJECTED', 'UNKNOWN']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `CandidateStatus`
  ·  Conformance: `conformance/invalid/enum_candidatestatus_unknown_member`

#### HML-ENUM-003 — ClaimStatus  `[NORMATIVE]`

`ClaimStatus` is a closed vocabulary. A conforming implementation MUST accept exactly ['GIVEN', 'ASSUMED', 'DERIVED', 'VERIFIED', 'REFUTED', 'UNRESOLVED', 'UNKNOWN'] and MUST reject any other value.

Closed vocabulary: `['GIVEN', 'ASSUMED', 'DERIVED', 'VERIFIED', 'REFUTED', 'UNRESOLVED', 'UNKNOWN']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `ClaimStatus`
  ·  Conformance: `conformance/invalid/enum_claimstatus_unknown_member`

#### HML-ENUM-004 — ErrorClass  `[NORMATIVE]`

`ErrorClass` is a closed vocabulary. A conforming implementation MUST accept exactly ['MISSING_DEPENDENCY', 'SCOPE_VIOLATION', 'PRECONDITION_VIOLATION', 'OBLIGATION_VIOLATION', 'CANDIDATE_PROMOTION', 'INVALID_BRANCH_JOIN', 'WARRANT_VIOLATION', 'EPISTEMIC_VIOLATION', 'GOAL_DISCHARGE', 'TYPE_DOMAIN_VIOLATION'] and MUST reject any other value.

Closed vocabulary: `['MISSING_DEPENDENCY', 'SCOPE_VIOLATION', 'PRECONDITION_VIOLATION', 'OBLIGATION_VIOLATION', 'CANDIDATE_PROMOTION', 'INVALID_BRANCH_JOIN', 'WARRANT_VIOLATION', 'EPISTEMIC_VIOLATION', 'GOAL_DISCHARGE', 'TYPE_DOMAIN_VIOLATION']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `ErrorClass`
  ·  Conformance: `conformance/invalid/enum_errorclass_unknown_member`

#### HML-ENUM-005 — GoalStatus  `[NORMATIVE]`

`GoalStatus` is a closed vocabulary. A conforming implementation MUST accept exactly ['OPEN', 'DISCHARGED', 'UNKNOWN'] and MUST reject any other value.

Closed vocabulary: `['OPEN', 'DISCHARGED', 'UNKNOWN']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `GoalStatus`
  ·  Conformance: `conformance/invalid/enum_goalstatus_unknown_member`

#### HML-ENUM-006 — ObligationState  `[NORMATIVE]`

`ObligationState` is a closed vocabulary. A conforming implementation MUST accept exactly ['OPEN', 'DISCHARGED', 'FAILED', 'UNKNOWN'] and MUST reject any other value.

Closed vocabulary: `['OPEN', 'DISCHARGED', 'FAILED', 'UNKNOWN']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `ObligationState`
  ·  Conformance: `conformance/invalid/enum_obligationstate_unknown_member`

#### HML-ENUM-007 — Verdict  `[NORMATIVE]`

`Verdict` is a closed vocabulary. A conforming implementation MUST accept exactly ['VALID', 'INVALID', 'UNRESOLVED'] and MUST reject any other value.

Closed vocabulary: `['VALID', 'INVALID', 'UNRESOLVED']`

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `Verdict`
  ·  Conformance: `conformance/invalid/enum_verdict_unknown_member`

#### HML-EPIS-001 — epistemic  `[NORMATIVE]`

UNKNOWN is a value, not an absence. An implementation MUST NOT map UNKNOWN to FALSE, to a default, or to a missing field.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `ClaimStatus.UNKNOWN`
  ·  Conformance: `conformance/invalid/unknown_collapsed_to_false`

#### HML-EPIS-002 — epistemic  `[NORMATIVE]`

A candidate MUST NOT acquire the epistemic standing of a claim without an action whose candidate_effect promotes it and whose warrant licenses the promotion.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `CANDIDATES`
  ·  Conformance: `conformance/invalid/candidate_promoted_without_warrant`

#### HML-EPIS-003 — epistemic  `[NORMATIVE]`

Evidence trust and claim status are independent. An EvidenceRecord being present MUST NOT by itself raise a claim's status, and trusted=False evidence MUST NOT discharge a mandatory obligation.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `EvidenceRecord.trusted`
  ·  Conformance: `conformance/invalid/untrusted_evidence_discharge`

#### HML-EPIS-004 — epistemic  `[NORMATIVE]`

A generator MUST NOT self-certify. An actor proposing a transition MUST NOT assert its own verification status; only the verifier assigns a Verdict.

Implementation: `src/hamiltonian_lang/semantic_state/trust.py` · `attest`
  ·  Conformance: `conformance/invalid/self_certification`
