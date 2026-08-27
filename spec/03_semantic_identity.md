# Semantic identity

*HML Standard 1.0 — 2026-08-27*

What makes two objects the same object: mapping keys, record ids, binding identity and canonical hashing.

## Normative rules (4)

#### HML-STATE-001 — state  `[NORMATIVE]`

A semantic state MUST consist of exactly the five record mappings claims, candidates, branches, goals and obligations, together with an ordered tuple of active scopes.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `SemanticState`
  ·  Conformance: `conformance/valid/state_minimal`

#### HML-STATE-002 — state  `[NORMATIVE]`

Every semantic-state record MUST be immutable. An implementation MUST NOT mutate a record in place; a transition produces a new state.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `frozen=True`
  ·  Conformance: `conformance/valid/state_minimal`

#### HML-STATE-003 — state  `[NORMATIVE]`

The mapping key under which a record is filed MAY differ from the record's own id field. A serializer MUST preserve both; a reader MUST NOT collapse them.

Implementation: `src/hamiltonian_lang/semantic_state/neutral.py` · `import_state`
  ·  Conformance: `conformance/round_trip/key_id_disagree`

#### HML-STATE-004 — state  `[NORMATIVE]`

A claim is visible from the current context if and only if its scope is a member of the state's active scopes. Visibility MUST be decided by membership, not by ordering.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `SemanticState.visible`
  ·  Conformance: `conformance/invalid/scope_leak`
