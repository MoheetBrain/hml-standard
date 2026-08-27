# Backends

*HML Standard 1.0 — 2026-08-27*

Translation targets and the obligation to declare loss.

## Normative rules (1)

#### HML-BACK-001 — backends  `[NORMATIVE]`

A backend that cannot express a construct MUST declare the loss through drop(), approximate() or weaken(). Silent omission MUST NOT occur.

Implementation: `src/hamiltonian_lang/backends/base.py` · `Backend`
  ·  Conformance: `conformance/valid/backend_declares_loss`
