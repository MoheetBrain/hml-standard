# HML Standard 1.0

**The Standard describes frozen executable semantics; it does not invent them.**

*Version 1.0 · Released 2026-08-27*

Hamiltonian Lang (HML) is a **typed semantic intermediate representation and verifier-facing
reasoning protocol for machine mathematics**. It represents mathematical reasoning as
explicit typed state — scoped claims, goals, candidates, dependencies, obligations, evidence
— and as checked transitions between states. The model-facing language is a *serialization*
of that semantic state, **not the source of mathematical truth**.

## What this repository is

The **normative documentation authority** for HML. It does not contain the implementation
and it does not contain experimental data. Three repositories, three jobs:

| repository | authority | answers |
|---|---|---|
| `hamiltonian-lang` | executable | what the machine does |
| **`hml-standard`** | **normative** | **what the language means** |
| `hml-reasoning-corpus` | empirical | what happens when we test it |

If documentation and executable semantics ever disagree, **the executable frozen semantics
win**, the discrepancy is documented, and the Standard is corrected to describe actual
behaviour.

## Pinned sources

| | |
|---|---|
| semantic implementation | `b3d0af9ce5ed8d7c4d87086ceedd7e4fa5e74ad5` |
| semantic tag | `hml-semantic-freeze-vnext-2026-08-27` |
| model language | `b011511e72572608eb7836d3b8a1a6bb794c890d` |
| model language tag | `hml-model-language-v1-freeze-2026-08-27` |

## What HML 1.0 contains

| | |
|---|---:|
| normative rules | **59** |
| kernel inference rules | **20** |
| transition invariants | **11** |
| closed status vocabularies | **7** |
| semantic state records | 9 |
| types | 18 |
| atlas concepts mapped | **110** across **22** domains |
| conformance specimens | **59**, all passing |

## Which document to read

| you want | read |
|---|---|
| the normative language, construct by construct | [STANDARD.md](STANDARD.md) |
| a dictionary of every object | [REFERENCE.md](REFERENCE.md) |
| how mathematics maps into HML | [SEMANTIC_ATLAS.md](SEMANTIC_ATLAS.md) · [atlas/](atlas/) |
| what to hand a model | [MODEL_REFERENCE.md](MODEL_REFERENCE.md) |
| how to claim conformance | [CONFORMANCE.md](CONFORMANCE.md) |
| rule → code → test | [TRACEABILITY.md](TRACEABILITY.md) |
| the three repositories and their seams | [ARCHITECTURE.md](ARCHITECTURE.md) |
| terms of art | [GLOSSARY.md](GLOSSARY.md) |

## Normative vs informative

Every section is labelled `[NORMATIVE]` or `[INFORMATIVE]`. Requirement words —
**MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHOULD**, **MAY** — carry RFC 2119
meanings, defined once in [STANDARD.md](STANDARD.md).

Four statuses are kept distinct and **MUST NOT** be conflated:

- **NORMATIVE** — required for conformance.
- **IMPLEMENTED** — present in the frozen implementation, not required of others.
- **EXPERIMENTAL** — specified, deliberately not frozen. The **state-delta language** is
  the only one in 1.0: it is `SPECIFIED_NOT_FROZEN` and is **not** normative.
- **INFORMATIVE** — explanation, not requirement.

## How to implement

Read `STANDARD.md`, then satisfy every rule in `standard/rules.json`. Run
`conformance/run_conformance.py` against your implementation and compare to
`conformance/RESULTS.json`. Machine-readable rules, dictionary and atlas are in
[machine/](machine/) with stable IDs.

## How to teach a model

Give it [MODEL_REFERENCE.md](MODEL_REFERENCE.md). It is mechanically traceable to
`STANDARD.md`; there is no independent prose to drift.

## How to report a gap

Classify it first. A gap is one of `DOCUMENTATION_GAP`, `LIBRARY_GAP`, `BACKEND_GAP`,
`POLICY_GAP`, `REPRESENTATION_GAP` or `POSSIBLE_CORE_GAP`.

**A `POSSIBLE_CORE_GAP` does not authorise modifying the language.** It requires separate
adjudication against the unfreeze rule in [spec/27_versioning.md](spec/27_versioning.md).

## Governance

A frozen semantic feature **MUST NOT** be changed because a model performs badly, another
notation looks prettier, an LLM proposes a feature, or a benchmark disappoints. Unfreezing
requires a concrete mathematical state, proof that HML cannot represent it losslessly,
independent validation, a minimal failing executable counterexample, classification as a
genuine `CORE_GAP`, a regression test, and an explicit version bump.

## Known limitation carried into 1.0

The corpus that HML has been measured on populates **only** the `claims` mapping — mean
1.00 claims per state and **0.00** candidates, branches, goals and obligations. Four of the
five state record kinds are therefore specified and proved lossless but **not measured
against data**. This is recorded wherever those constructs appear. It is a data limitation,
not a language limitation, and no representation change fixes it.
