# Architecture

*HML Standard 1.0 · 2026-08-27*  `[INFORMATIVE]`

## Three repositories, three authorities

```
    hamiltonian-lang            hml-standard              hml-reasoning-corpus
    EXECUTABLE                  NORMATIVE                 EMPIRICAL
    what the machine does       what the language means   what happens when we test it

    parser, AST, types          STANDARD.md               trajectories, datasets
    binders, semantic state     REFERENCE.md              manifests, audits
    reasoning kernel            SEMANTIC_ATLAS.md         experiments
    verification                MODEL_REFERENCE.md        negative results
    libraries, backends         CONFORMANCE.md
    renderer                    machine/*.json
```

The Standard **MUST NOT** silently fork semantics from the implementation. When they
disagree, the executable frozen semantics win, the discrepancy is documented, and the
Standard is corrected.

## The pipeline the Standard describes

```
  source text
      │  parser            src/hamiltonian_lang/parser/
      ▼
  AST                     src/hamiltonian_lang/ast/nodes.py
      │  resolve + type    src/hamiltonian_lang/type_system/
      ▼
  typed object            canonical identity computed here
      │
      ▼
  SEMANTIC STATE  S_t     src/hamiltonian_lang/semantic_state/model.py
      │
      │  action a         structural, not a name
      ▼
  TRANSITION              11 invariants checked
      │  verifier         src/hamiltonian_lang/semantic_state/verify.py
      ▼
  S_t+1  +  Verdict       VALID / INVALID / UNRESOLVED
```

Two serializations branch off the semantic state, and they are **not** interchangeable:

```
  SEMANTIC STATE
      ├── neutral JSON      semantic_state/neutral.py   corpus interchange
      ├── model-facing view semantic_state/view.py      what a model reads   (literal UTF-8)
      └── canonical doc     backends/canonical.py       identity hashing     (ASCII)
```

## The diagnostic chain

The reason the Standard exists in this shape: when something fails, the failure must be
**classifiable**, so that a model's bad day does not trigger a language redesign.

```
  MATHEMATICAL REQUIREMENT
      ↓   SEMANTIC_ATLAS.md  → is the state representable?
  HML SEMANTIC REPRESENTATION
      ↓   STANDARD.md rule   → which rule governs it?
  MODEL-FACING REPRESENTATION
      ↓   spec/24            → is the serialization lossless and deterministic?
  MODEL ACTION
      ↓   MODEL_REFERENCE.md → was the action legal?
  TRANSITION
      ↓   11 invariants      → which invariant fired?
  VERIFICATION
```

Every failure **MUST** be classified as one of:

| class | meaning | authorises a language change? |
|---|---|---|
| `INTERPRETATION_ERROR` | the mathematics was misread | no |
| `CORE_LANGUAGE_GAP` | the state genuinely cannot be represented | **only after adjudication** |
| `LIBRARY_GAP` | representable; the reasoning is not built | no |
| `BACKEND_GAP` | representable; the checker is not wired up | no |
| `REPRESENTATION_ERROR` | the serialization lost or distorted something | representation cycle only |
| `POLICY/MODEL_ERROR` | search or strategy failed | no |
| `VERIFIER_ERROR` | the checker is wrong | no |
| `DATA_ERROR` | the corpus is wrong | no |
| `UNKNOWN` | not yet classified | no |

The project has now recorded real instances of several of these — a `REPRESENTATION_ERROR`
(the `\uXXXX` double-encoding), a `DATA_ERROR` (a corpus whose structural fields were empty),
and a `POLICY/MODEL_ERROR` (relevance annotation that the model ignored). **None of them was
a `CORE_LANGUAGE_GAP`, and none of them justified changing the language.** That is the point
of the classification.
