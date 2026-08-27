# Project Status

Snapshot date: 2026-08-27. Maintained per the commit continuity protocol.

## Project Objective

`hml-standard` is the **normative documentation authority** for Hamiltonian Lang. It answers
what the language *means*. It does not contain the implementation and does not contain
experimental data.

**The Standard describes frozen executable semantics; it does not invent them.**

## Current Stage

**HML Standard 1.0 built and frozen.** `HML_STANDARD_FREEZE_READY = YES`.

All four pre-freeze audits pass: completeness, traceability, consistency, conformance.

| | |
|---|---:|
| normative rules | **59** |
| rules with a passing conformance specimen | **58/59** |
| conformance specimens | **59**, 0 failing |
| kernel inference rules documented | **20** |
| transition invariants documented | **11** |
| closed status vocabularies | **7** |
| reference dictionary entries | **66** |
| atlas concepts / domains | **110 / 22** |
| CORE_GAPs found | **0** |

## Current Branch

`main`.

## Current System Architecture

    tools/extract_implementation.py   pulls the frozen inventory out of the executable
    tools/build_rules.py              generates the normative rule registry
    tools/build_standard.py           generates REFERENCE, spec/, atlas/, machine/, schemas/
    tools/build_examples.py           renders examples through the real renderer
    tools/audit_standard.py           the four pre-freeze audits, executed
    conformance/run_conformance.py    59 specimens against the real implementation

Three sources of truth: `machine/_extracted.json` (what the implementation contains),
`standard/rules.json` (the normative registry), `standard/atlas_source.py` (the maths map).
Everything else is generated, which is what makes the consistency audit meaningful — the
documents cannot disagree because there is only one copy of each fact.

## Capabilities Implemented

Normative specification, complete reference dictionary, 28 spec sections, 22-domain semantic
atlas, compact model reference, executable conformance suite, traceability matrix,
machine-readable artifacts with stable IDs, JSON schemas, worked examples rendered by the
frozen implementation, four executed audits.

## Data Sources and Provenance

| | |
|---|---|
| semantic implementation | `b3d0af9ce5ed8d7c4d87086ceedd7e4fa5e74ad5` |
| semantic tag | `hml-semantic-freeze-vnext-2026-08-27` |
| model language | `b011511e72572608eb7836d3b8a1a6bb794c890d` |
| model language tag | `hml-model-language-v1-freeze-2026-08-27` |

Nothing was written from summaries. The rule registry, dictionary, kernel rules, invariants,
vocabularies and schemas are extracted from the executable at those commits.

**Provenance is recorded by commit, never by local path.** A pre-publication scan found three
generated artifacts embedding the absolute path of the implementation checkout; the
generators now emit `source_commit` and `implementation_commit` instead. A path describes
whoever ran the extraction, a commit describes what was extracted. `grep` for `/Users/`
across all tracked files returns zero.

## Decisions and Rationale

- **Generate rather than transcribe.** Hand-written documentation drifts from code; the
  consistency audit would then be checking prose against prose.
- **The atlas asks about carrying state, not proving theorems.** A concept whose theorems
  live in a library is not a language defect. This is why 61 `LIBRARY_GAP`s are recorded as
  work remaining rather than as failures.
- **A rule with no specimen is reported as NO_SPECIMEN**, never quietly counted as passing.
- **The state delta is not normative.** It is `SPECIFIED_NOT_FROZEN`; `VERSION.json` records
  `"normative_state_delta": false`.

## Verification and Test Results

| check | command | result |
|---|---|---|
| conformance | `conformance/run_conformance.py` | **59 specimens, 59 PASS, 0 FAIL** |
| completeness | `tools/audit_standard.py` | **PASS** — 0 extracted objects undocumented |
| traceability | `tools/audit_standard.py` | **PASS** — 58/59 rules traced to a passing specimen |
| consistency | `tools/audit_standard.py` | **PASS** — 0 contradictions |
| clean rebuild | all `tools/*` in sequence | reproduces every artifact |
| implementation untouched | `git status` in `hamiltonian-lang` | clean at `b011511` |

## Known Failures and Limitations

- **`HML-VER-002` has no conformance specimen and cannot have one.** It is a governance rule
  about how the Standard may change. Recorded as `not_mechanically_testable`.
- **Four of five state record kinds have zero corpus support.** Candidates, branches, goals
  and obligations are specified and proved lossless but are not measured against data
  (mean 0.00 per state against 1.00 claims). A data limitation, not a language limitation.
- **The 0 CORE_GAP result is a claim about the 110 mapped concepts**, reviewed against the
  frozen implementation. It is not a proof that no CORE_GAP exists anywhere in mathematics.
- Category theory, filtrations, causal intervention and numerical approximation families
  remain library-level by decision of the semantic closure audit.

## Risks and Technical Debt

- The atlas verdicts are reviewed judgements, not executed proofs. They carry an
  `evidence_confidence` field and should be revisited when libraries are built.
- 61 `LIBRARY_GAP`s are the real backlog. None of them justifies a semantic unfreeze.

## Current Blockers

None for the Standard. Downstream, the 50K corpus remains double-encoded and must be
regenerated once from the frozen renderer before any scaling test.

## Exact Next Actions

1. Hand the frozen renderer commit `b011511` and this Standard version to
   `hml-reasoning-corpus`.
2. Regenerate the 50K HML views **once** from `semantic_state.view.render_transition`.
3. Validate UTF-8 **at the decoded payload level**, per the normative rule in
   `CONFORMANCE.md` — the previous audit checked encoder flags and passed bad data.
4. Rebuild hashes and manifests; re-run parity and leakage audits.
5. Only then design the matched GPU experiment.
