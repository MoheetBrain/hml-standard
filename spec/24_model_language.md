# Model language

*HML Standard 1.0 — 2026-08-27*

The frozen model-facing representation.

## Normative rules (5)

#### HML-REP-001 — representation  `[NORMATIVE]`

The model-facing serialization MUST be lossless: parse(render(S)) == S under structural equality of the whole transition.

Implementation: `src/hamiltonian_lang/semantic_state/view.py` · `render_transition/parse_transition`
  ·  Conformance: `conformance/round_trip/all_records`

#### HML-REP-002 — representation  `[NORMATIVE]`

The model-facing serialization MUST be deterministic: if A == B then render(A) == render(B). Emission order MUST NOT depend on mapping construction order.

Implementation: `src/hamiltonian_lang/semantic_state/view.py` · `_emit_order`
  ·  Conformance: `conformance/round_trip/determinism`

#### HML-REP-003 — representation  `[NORMATIVE]`

The model-facing boundary MUST carry decoded UTF-8. A model-facing payload MUST NOT contain \uXXXX escape sequences standing for mathematical characters.

Implementation: `src/hamiltonian_lang/semantic_state/view.py` · `_dumps`
  ·  Conformance: `conformance/invalid/double_encoded_payload`

#### HML-REP-004 — representation  `[NORMATIVE]`

Canonical identity documents MUST remain ASCII-encoded. This is deliberately the opposite of HML-REP-003: identity documents and model-facing surfaces are different artifacts with different consumers.

Implementation: `src/hamiltonian_lang/backends/canonical.py` · `ensure_ascii=True`
  ·  Conformance: `conformance/valid/canonical_ascii`

#### HML-REP-005 — representation  `[NORMATIVE]`

The serialization MUST NOT leak the action into the state rendering. Rendering a state MUST NOT reveal the action that is to be predicted from it.

Implementation: `src/hamiltonian_lang/semantic_state/view.py` · `render_state`
  ·  Conformance: `conformance/valid/no_action_leak`
