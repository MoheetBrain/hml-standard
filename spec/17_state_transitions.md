# State transitions

*HML Standard 1.0 — 2026-08-27*

S_before --action--> S_after and the invariants a verifier must check.

## Normative rules (12)

#### HML-INV-001 — DEPENDENCY  `[NORMATIVE]`

A conforming verifier MUST check the DEPENDENCY invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['DEPENDENCY']`
  ·  Conformance: `conformance/invalid/invariant_dependency`

#### HML-INV-002 — SCOPE  `[NORMATIVE]`

A conforming verifier MUST check the SCOPE invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['SCOPE']`
  ·  Conformance: `conformance/invalid/invariant_scope`

#### HML-INV-003 — PRECONDITIONS  `[NORMATIVE]`

A conforming verifier MUST check the PRECONDITIONS invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['PRECONDITIONS']`
  ·  Conformance: `conformance/invalid/invariant_preconditions`

#### HML-INV-004 — OBLIGATIONS  `[NORMATIVE]`

A conforming verifier MUST check the OBLIGATIONS invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['OBLIGATIONS']`
  ·  Conformance: `conformance/invalid/invariant_obligations`

#### HML-INV-005 — CANDIDATES  `[NORMATIVE]`

A conforming verifier MUST check the CANDIDATES invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['CANDIDATES']`
  ·  Conformance: `conformance/invalid/invariant_candidates`

#### HML-INV-006 — BRANCH_JOIN  `[NORMATIVE]`

A conforming verifier MUST check the BRANCH_JOIN invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['BRANCH_JOIN']`
  ·  Conformance: `conformance/invalid/invariant_branch_join`

#### HML-INV-007 — WARRANT  `[NORMATIVE]`

A conforming verifier MUST check the WARRANT invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['WARRANT']`
  ·  Conformance: `conformance/invalid/invariant_warrant`

#### HML-INV-008 — EPISTEMIC_STATUS  `[NORMATIVE]`

A conforming verifier MUST check the EPISTEMIC_STATUS invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['EPISTEMIC_STATUS']`
  ·  Conformance: `conformance/invalid/invariant_epistemic_status`

#### HML-INV-009 — GOAL_DISCHARGE  `[NORMATIVE]`

A conforming verifier MUST check the GOAL_DISCHARGE invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['GOAL_DISCHARGE']`
  ·  Conformance: `conformance/invalid/invariant_goal_discharge`

#### HML-INV-010 — TYPE_DOMAIN  `[NORMATIVE]`

A conforming verifier MUST check the TYPE_DOMAIN invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['TYPE_DOMAIN']`
  ·  Conformance: `conformance/invalid/invariant_type_domain`

#### HML-INV-011 — FRAME  `[NORMATIVE]`

A conforming verifier MUST check the FRAME invariant on every transition and MUST report a violation as a Finding carrying an ErrorClass.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `INVARIANTS['FRAME']`
  ·  Conformance: `conformance/invalid/invariant_frame`

#### HML-TRANS-001 — transitions  `[NORMATIVE]`

A transition MUST be the triple (state_before, action, state_after) together with the evidence offered for it. The verifier returns a Verdict of VALID, INVALID or UNRESOLVED; UNRESOLVED MUST NOT be reported as INVALID.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `verify`
  ·  Conformance: `conformance/valid/transition_minimal`
