# Versioning and governance

*HML Standard 1.0 — 2026-08-27*

How the Standard changes, and the unfreeze rule.

## Normative rules (2)

#### HML-VER-001 — versioning  `[NORMATIVE]`

A conforming artifact MUST record the semantic implementation commit and the model-language commit it was produced against.

Implementation: `VERSION.json` · `-`
  ·  Conformance: `conformance/valid/version_manifest`

#### HML-VER-002 — versioning  `[NORMATIVE]`

A frozen semantic feature MUST NOT be changed because a model performs badly, a notation looks preferable, or a benchmark disappoints. Unfreeze REQUIRES a demonstrated CORE_GAP as defined in spec/27_versioning.md.

Implementation: `spec/27_versioning.md` · `-`
  ·  Conformance: **none** — Governance rule about the process for changing the Standard. No executable specimen can establish that a future change followed it.
