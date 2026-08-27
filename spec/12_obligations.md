# Obligations

*HML Standard 1.0 — 2026-08-27*

Proof debt: creation, persistence and discharge.

## Normative rules (2)

#### HML-OBL-001 — obligations  `[NORMATIVE]`

A mandatory obligation MUST persist across transitions until an action explicitly discharges it with attested evidence. Silent disappearance MUST be rejected.

Implementation: `src/hamiltonian_lang/semantic_state/verify.py` · `OBLIGATIONS`
  ·  Conformance: `conformance/invalid/obligation_dropped`

#### HML-OBL-002 — obligations  `[NORMATIVE]`

An obligation's state MUST be one of OPEN, DISCHARGED, FAILED or UNKNOWN.

Implementation: `src/hamiltonian_lang/semantic_state/model.py` · `ObligationState`
  ·  Conformance: `conformance/valid/obligation_open`
