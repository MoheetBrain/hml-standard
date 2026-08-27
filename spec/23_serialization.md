# Serialization

*HML Standard 1.0 — 2026-08-27*

The neutral JSON form and canonical identity documents.

[NORMATIVE] Two serializations exist and they have different jobs.

The **neutral JSON form** (`semantic_state/neutral.py`) is the corpus interchange format.
The **canonical identity document** (`backends/canonical.py`) is the hashing form and is
deliberately ASCII-encoded (HML-REP-004); every recorded example hash depends on those
bytes.

The model-facing surface is specified separately in `24_model_language.md` and is
deliberately **not** ASCII (HML-REP-003). Identity documents stay ASCII; model-facing
surfaces stay literal.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
