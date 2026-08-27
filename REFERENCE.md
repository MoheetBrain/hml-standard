# HML Reference — complete dictionary

*HML Standard 1.0 — 2026-08-27*

Generated from the frozen implementation at `b3d0af9ce5ed`. Every row is extracted, not transcribed.

## Semantic state records

| Object | Category | Fields | Frozen | Implementation |
|---|---|---|---|---|
| `Action` | state record | 15: id, operation, summary, output_id, dependencies, preconditions, obligations_created, obligations_discharged, typing, warrant, goal_effect, scope_effect, branch_effect, candidate_effect, epistemic_effect | yes | `src/hamiltonian_lang/semantic_state/model.py:285` |
| `Branch` | state record | 6: id, predicate, status, scope, conclusion, partition_id | yes | `src/hamiltonian_lang/semantic_state/model.py:221` |
| `Candidate` | state record | 9: id, proposition, status, scope, constraint_ids, origin, dependencies, evidence_id, verification_result | yes | `src/hamiltonian_lang/semantic_state/model.py:192` |
| `Claim` | state record | 6: id, proposition, status, scope, domain, dependencies | yes | `src/hamiltonian_lang/semantic_state/model.py:180` |
| `EvidenceRecord` | state record | 7: id, kind, status, trusted, supports_rule, premise_ids, payload | yes | `src/hamiltonian_lang/semantic_state/model.py:263` |
| `Goal` | state record | 4: id, proposition, status, scope | yes | `src/hamiltonian_lang/semantic_state/model.py:236` |
| `Obligation` | state record | 7: id, proposition, status, mandatory, origin, dependencies, discharge_evidence_id | yes | `src/hamiltonian_lang/semantic_state/model.py:244` |
| `SemanticState` | state record | 6: claims, candidates, branches, goals, obligations, active_scopes | yes | `src/hamiltonian_lang/semantic_state/model.py:309` |
| `Transition` | state record | 7: case_id, action, state_before, state_after, evidence, schema_version, source | yes | `src/hamiltonian_lang/semantic_state/model.py:333` |

## Status vocabularies

| Vocabulary | Members | Implementation |
|---|---|---|
| `BranchStatus` | `OPEN`, `CLOSED`, `JOINED`, `ABANDONED`, `UNKNOWN` | `src/hamiltonian_lang/semantic_state/model.py:116` |
| `CandidateStatus` | `PROPOSED`, `UNVERIFIED`, `VERIFIED`, `REJECTED`, `UNKNOWN` | `src/hamiltonian_lang/semantic_state/model.py:77` |
| `ClaimStatus` | `GIVEN`, `ASSUMED`, `DERIVED`, `VERIFIED`, `REFUTED`, `UNRESOLVED`, `UNKNOWN` | `src/hamiltonian_lang/semantic_state/model.py:56` |
| `ErrorClass` | `MISSING_DEPENDENCY`, `SCOPE_VIOLATION`, `PRECONDITION_VIOLATION`, `OBLIGATION_VIOLATION`, `CANDIDATE_PROMOTION`, `INVALID_BRANCH_JOIN`, `WARRANT_VIOLATION`, `EPISTEMIC_VIOLATION`, `GOAL_DISCHARGE`, `TYPE_DOMAIN_VIOLATION` | `src/hamiltonian_lang/semantic_state/model.py:165` |
| `GoalStatus` | `OPEN`, `DISCHARGED`, `UNKNOWN` | `src/hamiltonian_lang/semantic_state/model.py:133` |
| `ObligationState` | `OPEN`, `DISCHARGED`, `FAILED`, `UNKNOWN` | `src/hamiltonian_lang/semantic_state/model.py:126` |
| `Verdict` | `VALID`, `INVALID`, `UNRESOLVED` | `src/hamiltonian_lang/semantic_state/model.py:152` |

## Types

| Type | Implementation |
|---|---|
| `ConceptType` | `src/hamiltonian_lang/types.py:603` |
| `Dimension` | `src/hamiltonian_lang/types.py:188` |
| `DistributionType` | `src/hamiltonian_lang/types.py:511` |
| `EventType` | `src/hamiltonian_lang/types.py:580` |
| `FunctionType` | `src/hamiltonian_lang/types.py:471` |
| `MatrixType` | `src/hamiltonian_lang/types.py:402` |
| `PredicateType` | `src/hamiltonian_lang/types.py:485` |
| `ProductType` | `src/hamiltonian_lang/types.py:447` |
| `PropositionType` | `src/hamiltonian_lang/types.py:574` |
| `QuantityType` | `src/hamiltonian_lang/types.py:334` |
| `RandomVariableType` | `src/hamiltonian_lang/types.py:498` |
| `ScalarType` | `src/hamiltonian_lang/types.py:131` |
| `SetType` | `src/hamiltonian_lang/types.py:436` |
| `SymbolicExtent` | `src/hamiltonian_lang/types.py:350` |
| `TensorType` | `src/hamiltonian_lang/types.py:422` |
| `Type` | `src/hamiltonian_lang/types.py:65` |
| `UnknownType` | `src/hamiltonian_lang/types.py:613` |
| `VectorType` | `src/hamiltonian_lang/types.py:387` |

## Kernel inference rules

The kernel has exactly **20** inference rules. Everything else is library, backend or policy.

| Rule | Arity | Shape | Obligations | Side conditions |
|---|---|---|---|---|
| `add_both_sides` | 1 | `a = b  |-  a + k = b + k` | — | — |
| `add_inequality` | 1 | `a < b  |-  a + k < b + k` | — | — |
| `and_elim_left` | 1 | `P and Q  |-  P` | — | — |
| `and_elim_right` | 1 | `P and Q  |-  Q` | — | — |
| `and_intro` | 2 | `P, Q  |-  P and Q` | — | — |
| `congruence` | 1 | `a = b  |-  f(a) = f(b)` | — | — |
| `divide_both_sides` | 1 | `a = b  |-  a / k = b / k   [requires k != 0]` | — | — |
| `exists_intro` | 1 | `phi(a)  |-  exists a : D . phi(a)   [a is a typed witness]` | — | — |
| `forall_elim` | 1 | `forall x : D . phi(x)  |-  phi[t/x]   [requires t : D]` | — | ['instantiation_domain'] |
| `forall_intro` | 1 | `phi(a)  |-  forall a : D . phi(a)   [a arbitrary]` | — | ['eigenvariable'] |
| `modus_ponens` | 2 | `P, P implies Q  |-  Q` | — | — |
| `modus_tollens` | 2 | `not Q, P implies Q  |-  not P` | — | — |
| `multiply_both_sides` | 1 | `a = b  |-  a * k = b * k` | — | — |
| `multiply_inequality` | 1 | `a < b  |-  a * k < b * k   [requires k > 0]` | ["ObligationSpec(build=<function _gt_zero at 0x105ed4a40>, reason='order_preserving_multiplier', mandatory=True)"] | — |
| `reflexivity` | 0 | `|- t = t` | — | — |
| `substitute` | 2 | `a = b, P  |-  P[a := b]` | — | — |
| `subtract_both_sides` | 1 | `a = b  |-  a - k = b - k` | — | — |
| `symmetry` | 1 | `a = b  |-  b = a` | — | — |
| `transitivity` | 2 | `a = b, b = c  |-  a = c` | — | — |
| `weaken_inequality` | 1 | `a < b  |-  a <= b` | — | — |

## Backends

| Backend | Implementation | Must declare loss |
|---|---|---|
| `canonical` | `src/hamiltonian_lang/backends/canonical.py` | yes (HML-BACK-001) |
| `english` | `src/hamiltonian_lang/backends/english.py` | yes (HML-BACK-001) |
| `hml` | `src/hamiltonian_lang/backends/hml.py` | yes (HML-BACK-001) |
| `latex` | `src/hamiltonian_lang/backends/latex.py` | yes (HML-BACK-001) |
| `lean` | `src/hamiltonian_lang/backends/lean.py` | yes (HML-BACK-001) |
| `stan` | `src/hamiltonian_lang/backends/stan.py` | yes (HML-BACK-001) |
| `sympy` | `src/hamiltonian_lang/backends/sympy.py` | yes (HML-BACK-001) |

## Libraries

| Library | Implementation | Status |
|---|---|---|
| `algebra` | `src/hamiltonian_lang/libraries/algebra.py` | implemented, non-kernel |
| `calculus` | `src/hamiltonian_lang/libraries/calculus.py` | implemented, non-kernel |
| `numerical` | `src/hamiltonian_lang/libraries/numerical.py` | implemented, non-kernel |
| `probability` | `src/hamiltonian_lang/libraries/probability.py` | implemented, non-kernel |
| `theorem` | `src/hamiltonian_lang/libraries/theorem.py` | implemented, non-kernel |
