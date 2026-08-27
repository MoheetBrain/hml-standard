# Conformance

*HML Standard 1.0 · 2026-08-27*

## What conformance means  `[NORMATIVE]`

An implementation conforms to HML Standard 1.0 if and only if it satisfies **every** rule
marked `NORMATIVE` in `standard/rules.json` — **59** rules — and can reproduce the outcomes
recorded in `conformance/RESULTS.json`.

Conformance is claimed **against a pinned pair of commits**. A claim that does not name the
semantic implementation commit and the model language commit it was tested against is not a
conformance claim (HML-VER-001).

## Running the suite

```bash
python conformance/run_conformance.py /path/to/hamiltonian-lang
```

It writes `conformance/RESULTS.json` with the actual outcome of every specimen. Nothing is
asserted from documentation; every specimen executes against the implementation.

## Coverage, stated honestly

| | |
|---|---:|
| normative rules | 59 |
| rules with an executable specimen | **58** |
| specimens | **59** |
| specimens passing | **59** |
| specimens failing | **0** |

One rule has **no specimen**: `HML-VER-002`, the unfreeze governance rule. It is a statement
about the process by which the Standard may change, and no executable specimen can establish
that a future change followed it. It is recorded as `not_mechanically_testable` rather than
counted as passing.

**A rule with no specimen is reported as NO_SPECIMEN, never quietly counted as passing.**

## Specimen categories

- `conformance/valid/` — constructions that MUST be accepted.
- `conformance/invalid/` — constructions that MUST be rejected. A specimen here *passes*
  when the implementation refuses it.
- `conformance/round_trip/` — `parse(render(S)) == S` under structural equality.

## The specimens that matter most

These encode the failures this project has actually suffered, and are the reason the suite
exists rather than a checklist:

| specimen | guards against |
|---|---|
| `unknown_not_collapsed_to_false` | UNKNOWN silently becoming FALSE |
| `candidate_status_is_separate_vocabulary` | a proposal being relabelled as a fact |
| `generator_cannot_self_certify` | a model asserting its own verification |
| `evidence_trust_is_separate_from_status` | evidence being read as truth |
| `mandatory_default` | proof debt defaulting to optional |
| `scope_visibility_is_membership` | branch-local facts leaking globally |
| `determinism` | equal states rendering differently |
| `double_encoded_payload` | the `\uXXXX` defect that cost −3.41pp |
| `canonical_ascii` | someone "fixing" the deliberate ASCII asymmetry |
| `no_action_leak` | the answer appearing in the prompt |
| `missing_dependency_is_an_error_class` | dangling references passing silently |

## Unicode conformance  `[NORMATIVE]`

A conforming Unicode audit **MUST** inspect **decoded payload strings**, not encoder flags
and not JSON-level escapes.

This is normative because the inverse has already shipped: an audit reporting `PASS` on
14,039,188 literal non-ASCII codepoints and "zero JSON `\uXXXX` escape sequences" was
correct at the JSON layer and blind to a payload in which 15.2% of every prompt was escape
text. Checking the encoder flag is not checking the payload.
