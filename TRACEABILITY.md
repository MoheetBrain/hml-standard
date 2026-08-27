# Traceability matrix

*HML Standard 1.0 — 2026-08-27*

Every normative rule, the section that states it, the implementation that enforces it, and the conformance specimen that proves it.

| Rule | Spec section | Implementation | Symbol | Conformance | Status |
|---|---|---|---|---|---|
| `HML-KERNEL-001` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['add_both_sides']` | `conformance/valid/kernel_add_both_sides` | PASS |
| `HML-KERNEL-002` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['add_inequality']` | `conformance/valid/kernel_add_inequality` | PASS |
| `HML-KERNEL-003` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['and_elim_left']` | `conformance/valid/kernel_and_elim_left` | PASS |
| `HML-KERNEL-004` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['and_elim_right']` | `conformance/valid/kernel_and_elim_right` | PASS |
| `HML-KERNEL-005` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['and_intro']` | `conformance/valid/kernel_and_intro` | PASS |
| `HML-KERNEL-006` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['congruence']` | `conformance/valid/kernel_congruence` | PASS |
| `HML-KERNEL-007` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['divide_both_sides']` | `conformance/valid/kernel_divide_both_sides` | PASS |
| `HML-KERNEL-008` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['exists_intro']` | `conformance/valid/kernel_exists_intro` | PASS |
| `HML-KERNEL-009` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['forall_elim']` | `conformance/valid/kernel_forall_elim` | PASS |
| `HML-KERNEL-010` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['forall_intro']` | `conformance/valid/kernel_forall_intro` | PASS |
| `HML-KERNEL-011` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['modus_ponens']` | `conformance/valid/kernel_modus_ponens` | PASS |
| `HML-KERNEL-012` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['modus_tollens']` | `conformance/valid/kernel_modus_tollens` | PASS |
| `HML-KERNEL-013` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['multiply_both_sides']` | `conformance/valid/kernel_multiply_both_sides` | PASS |
| `HML-KERNEL-014` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['multiply_inequality']` | `conformance/valid/kernel_multiply_inequality` | PASS |
| `HML-KERNEL-015` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['reflexivity']` | `conformance/valid/kernel_reflexivity` | PASS |
| `HML-KERNEL-016` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['substitute']` | `conformance/valid/kernel_substitute` | PASS |
| `HML-KERNEL-017` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['subtract_both_sides']` | `conformance/valid/kernel_subtract_both_sides` | PASS |
| `HML-KERNEL-018` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['symmetry']` | `conformance/valid/kernel_symmetry` | PASS |
| `HML-KERNEL-019` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['transitivity']` | `conformance/valid/kernel_transitivity` | PASS |
| `HML-KERNEL-020` | `spec/20_verification.md` | `src/hamiltonian_lang/reasoning/kernel.py` | `RULES['weaken_inequality']` | `conformance/valid/kernel_weaken_inequality` | PASS |
| `HML-INV-001` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['DEPENDENCY']` | `conformance/invalid/invariant_dependency` | PASS |
| `HML-INV-002` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['SCOPE']` | `conformance/invalid/invariant_scope` | PASS |
| `HML-INV-003` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['PRECONDITIONS']` | `conformance/invalid/invariant_preconditions` | PASS |
| `HML-INV-004` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['OBLIGATIONS']` | `conformance/invalid/invariant_obligations` | PASS |
| `HML-INV-005` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['CANDIDATES']` | `conformance/invalid/invariant_candidates` | PASS |
| `HML-INV-006` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['BRANCH_JOIN']` | `conformance/invalid/invariant_branch_join` | PASS |
| `HML-INV-007` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['WARRANT']` | `conformance/invalid/invariant_warrant` | PASS |
| `HML-INV-008` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['EPISTEMIC_STATUS']` | `conformance/invalid/invariant_epistemic_status` | PASS |
| `HML-INV-009` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['GOAL_DISCHARGE']` | `conformance/invalid/invariant_goal_discharge` | PASS |
| `HML-INV-010` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['TYPE_DOMAIN']` | `conformance/invalid/invariant_type_domain` | PASS |
| `HML-INV-011` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `INVARIANTS['FRAME']` | `conformance/invalid/invariant_frame` | PASS |
| `HML-ENUM-001` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `BranchStatus` | `conformance/invalid/enum_branchstatus_unknown_member` | PASS |
| `HML-ENUM-002` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `CandidateStatus` | `conformance/invalid/enum_candidatestatus_unknown_member` | PASS |
| `HML-ENUM-003` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `ClaimStatus` | `conformance/invalid/enum_claimstatus_unknown_member` | PASS |
| `HML-ENUM-004` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `ErrorClass` | `conformance/invalid/enum_errorclass_unknown_member` | PASS |
| `HML-ENUM-005` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `GoalStatus` | `conformance/invalid/enum_goalstatus_unknown_member` | PASS |
| `HML-ENUM-006` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `ObligationState` | `conformance/invalid/enum_obligationstate_unknown_member` | PASS |
| `HML-ENUM-007` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `Verdict` | `conformance/invalid/enum_verdict_unknown_member` | PASS |
| `HML-STATE-001` | `spec/03_semantic_identity.md` | `src/hamiltonian_lang/semantic_state/model.py` | `SemanticState` | `conformance/valid/state_minimal` | PASS |
| `HML-STATE-002` | `spec/03_semantic_identity.md` | `src/hamiltonian_lang/semantic_state/model.py` | `frozen=True` | `conformance/valid/state_minimal` | PASS |
| `HML-STATE-003` | `spec/03_semantic_identity.md` | `src/hamiltonian_lang/semantic_state/neutral.py` | `import_state` | `conformance/round_trip/key_id_disagree` | PASS |
| `HML-STATE-004` | `spec/03_semantic_identity.md` | `src/hamiltonian_lang/semantic_state/model.py` | `SemanticState.visible` | `conformance/invalid/scope_leak` | PASS |
| `HML-EPIS-001` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `ClaimStatus.UNKNOWN` | `conformance/invalid/unknown_collapsed_to_false` | PASS |
| `HML-EPIS-002` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `CANDIDATES` | `conformance/invalid/candidate_promoted_without_warrant` | PASS |
| `HML-EPIS-003` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/model.py` | `EvidenceRecord.trusted` | `conformance/invalid/untrusted_evidence_discharge` | PASS |
| `HML-EPIS-004` | `spec/18_epistemic_status.md` | `src/hamiltonian_lang/semantic_state/trust.py` | `attest` | `conformance/invalid/self_certification` | PASS |
| `HML-OBL-001` | `spec/12_obligations.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `OBLIGATIONS` | `conformance/invalid/obligation_dropped` | PASS |
| `HML-OBL-002` | `spec/12_obligations.md` | `src/hamiltonian_lang/semantic_state/model.py` | `ObligationState` | `conformance/valid/obligation_open` | PASS |
| `HML-ACT-001` | `spec/16_actions.md` | `src/hamiltonian_lang/semantic_state/model.py` | `Action` | `conformance/valid/action_structural` | PASS |
| `HML-ACT-002` | `spec/16_actions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `DEPENDENCY` | `conformance/invalid/missing_dependency` | PASS |
| `HML-TRANS-001` | `spec/17_state_transitions.md` | `src/hamiltonian_lang/semantic_state/verify.py` | `verify` | `conformance/valid/transition_minimal` | PASS |
| `HML-REP-001` | `spec/24_model_language.md` | `src/hamiltonian_lang/semantic_state/view.py` | `render_transition/parse_transition` | `conformance/round_trip/all_records` | PASS |
| `HML-REP-002` | `spec/24_model_language.md` | `src/hamiltonian_lang/semantic_state/view.py` | `_emit_order` | `conformance/round_trip/determinism` | PASS |
| `HML-REP-003` | `spec/24_model_language.md` | `src/hamiltonian_lang/semantic_state/view.py` | `_dumps` | `conformance/invalid/double_encoded_payload` | PASS |
| `HML-REP-004` | `spec/24_model_language.md` | `src/hamiltonian_lang/backends/canonical.py` | `ensure_ascii=True` | `conformance/valid/canonical_ascii` | PASS |
| `HML-REP-005` | `spec/24_model_language.md` | `src/hamiltonian_lang/semantic_state/view.py` | `render_state` | `conformance/valid/no_action_leak` | PASS |
| `HML-BACK-001` | `spec/22_backends.md` | `src/hamiltonian_lang/backends/base.py` | `Backend` | `conformance/valid/backend_declares_loss` | PASS |
| `HML-VER-001` | `spec/27_versioning.md` | `VERSION.json` | `-` | `conformance/valid/version_manifest` | PASS |
| `HML-VER-002` | `spec/27_versioning.md` | `spec/27_versioning.md` | `-` | `—` | N/A — governance |

**58/59 rules have a passing conformance specimen.**

