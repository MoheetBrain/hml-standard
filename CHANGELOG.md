# Changelog

## HML Standard 1.0 — 2026-08-27

The first normative HML standard.

### Sources pinned

| | |
|---|---|
| semantic implementation | `b3d0af9ce5ed8d7c4d87086ceedd7e4fa5e74ad5` |
| semantic tag | `hml-semantic-freeze-vnext-2026-08-27` |
| model language | `b011511e72572608eb7836d3b8a1a6bb794c890d` |
| model language tag | `hml-model-language-v1-freeze-2026-08-27` |

### What is standardised

- **59 normative rules**, each traced to implementation and — for 58 of them — to a passing
  executable conformance specimen.
- The **20-rule kernel** and the **11 transition invariants**, generated from the
  implementation rather than transcribed.
- **7 closed status vocabularies**, and the epistemic discipline around them.
- The **frozen model-facing representation** and its encoding requirements.
- A **mathematics→HML semantic atlas**: 110 concepts across 22 domains.

### What is NOT normative in 1.0

- **The state-delta language.** `SPECIFIED_NOT_FROZEN`. `VERSION.json` records
  `"normative_state_delta": false`. It is specified because 18.8% of every model-facing
  prompt re-emits unchanged records; it is not frozen because it changes the task rather
  than the surface.
- Surface lexical grammar and abstract syntax sections are `[INFORMATIVE]`: no normative
  rule in 1.0 depends on token spelling.

### Historical defect recorded, not hidden

The 50K corpus shipped a model-facing view named `HML_WORKED_UTF8` that was
**double-encoded**: 500/500 sampled rows carried literal `\uXXXX` text, 31 sequences per
row, 15.2% of every prompt, while the matched neutral view carried real glyphs. The corpus's
own Unicode audit reported `PASS` because it counted JSON-level escapes and the escaping had
already happened upstream inside the string value.

The same class of defect had previously been measured at **−3.41pp** of task accuracy — 2.5×
the representation effect the experiment existed to detect — landing asymmetrically on HML.

The renderer was repaired at `c8964e7`; **HML-REP-003** and the normative Unicode-audit rule
in `CONFORMANCE.md` exist to prevent recurrence. **The corpus itself has not been
regenerated** — that belongs to `hml-reasoning-corpus`, once, from the frozen renderer.

### Current limitations

- Four of the five state record kinds — candidates, branches, goals, obligations — have
  **zero corpus support** (mean 0.00 per state against 1.00 claims). They are specified and
  proved lossless but are **not measured against data**.
- `HML-VER-002` has no conformance specimen and cannot have one: it is a governance rule
  about how the Standard may change.
- Category theory, filtrations, causal intervention and numerical approximation families
  remain library-level by deliberate decision of the semantic closure audit.

### Provenance

Nothing in 1.0 was written from summaries. The rule registry, reference dictionary, kernel
rules, invariants, vocabularies and JSON schemas are **generated** from the frozen
implementation by `tools/extract_implementation.py` and `tools/build_standard.py`, so the
documents cannot disagree with the code or with each other.
