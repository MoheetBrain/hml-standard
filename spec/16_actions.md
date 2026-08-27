# Actions

*HML Standard 1.0 — 2026-08-27*

The structural action object.

## Normative rules (2)

#### HML-ACT-001 — actions  `[NORMATIVE]`

An action MUST be represented structurally. An implementation MUST NOT treat the operation name alone as the reasoning decision; the decision is the action applied to a specific state.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `Action`
  ·  Conformance: `conformance/valid/action_structural`

#### HML-ACT-002 — actions  `[NORMATIVE]`

Every reference an action makes -- dependencies, output_id, obligations discharged -- MUST resolve in the state it is applied to.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `DEPENDENCY`
  ·  Conformance: `conformance/invalid/missing_dependency`
