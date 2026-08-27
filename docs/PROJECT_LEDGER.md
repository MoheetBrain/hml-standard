# Project Ledger

Append-only. One entry per commit.

---

## 2026-08-27 — HML Standard 1.0 built and frozen

**Branch** `main`, following `3a82039` (initial commit, README only).

**Project stage.** Standardisation, after the semantic freeze (`b3d0af9`) and the
model-language freeze (`b011511`). Not a language-design mission: the Standard describes
frozen executable semantics and does not invent them.

**Objective.** Produce the authoritative, versioned, frozen specification of HML — the
single human- and machine-readable answer to what exists in the language, what every
construct means, what is legal, what a model sees, and what a verifier may certify.

**Files and systems changed.** New repository content: `STANDARD.md`, `REFERENCE.md`,
`SEMANTIC_ATLAS.md`, `MODEL_REFERENCE.md`, `CONFORMANCE.md`, `ARCHITECTURE.md`,
`GLOSSARY.md`, `CHANGELOG.md`, `TRACEABILITY.md`, `README.md`, `VERSION`, `VERSION.json`;
`spec/` (28 sections); `atlas/` (22 domains + index); `machine/` (5 artifacts);
`schemas/` (5); `conformance/` (runner, 59 specimens, results, manifest); `examples/`
(7 rendered by the real implementation); `reports/` (4 audits); `standard/` (rule registry,
atlas source); `tools/` (5 generators). **No change to `hamiltonian-lang`. No change to
`hml-reasoning-corpus`. GPU_USED = NO.**

**What was completed.** 59 normative rules with stable IDs, each traced to implementation
and — for 58 — to a passing executable specimen. The 20 kernel rules, 11 transition
invariants and 7 closed status vocabularies are **generated from the executable**, not
transcribed. A 110-concept, 22-domain mathematics→HML atlas. A compact model reference
mechanically traceable to the Standard. Four executed audits.

**Decisions made and why.**

*Generate rather than transcribe.* Three sources of truth — the extraction, the rule
registry, the atlas source — and every document derived from them. Hand-written
documentation drifts from code, and a consistency audit over hand-written prose only checks
prose against prose.

*The atlas asks whether HML can carry the reasoning state, not whether HML can prove the
theorem.* HML's kernel has 20 rules and proves almost nothing by itself. Judging the language
by theorem coverage would have manufactured dozens of false CORE_GAPs.

*A rule with no specimen is reported as NO_SPECIMEN.* `HML-VER-002` is a governance rule and
no executable specimen can establish that a future change followed it. Marking it
`not_mechanically_testable` is more honest than a test that asserts a policy back to itself.

*The state delta is recorded as SPECIFIED_NOT_FROZEN and NOT normative*, matching the
model-language freeze rather than promoting a research label into normative syntax.

**Tests and verification actually executed.**

- `conformance/run_conformance.py` against `hamiltonian-lang` at `b011511`:
  **59 specimens, 59 PASS, 0 FAIL**, 58/59 rules covered.
- `tools/audit_standard.py`: completeness **PASS** (0 of 66 extracted objects undocumented),
  traceability **PASS**, consistency **PASS** (0 contradictions), conformance **PASS**.
- Clean rebuild of every generated artifact from the three sources: reproduces identically.
- All 7 examples assert `parse(render(t)) == t` at generation time.
- `hamiltonian-lang` worktree clean at `b011511` after all work.

**Failures and unresolved uncertainty.**

The consistency audit **failed on its first run**: `REFERENCE.md` did not state the kernel
rule count in a checkable form. Fixed by making the document carry the fact, not by
loosening the check. Two spec sections — type system and claims — initially received the
generic "no normative rules" fallback; both were given real normative content, because §6
forbids decorative files and both are central.

Unresolved: the **0 CORE_GAP** result is a claim about the 110 mapped concepts reviewed
against the frozen implementation, not a proof that no CORE_GAP exists anywhere in
mathematics. Atlas verdicts are reviewed judgements carrying an `evidence_confidence` field,
not executed proofs.

**Effect on the overall project.** The language now has a memory. Any future failure can be
classified — mathematics, atlas, standard rule, executable, representation, model action,
verifier — so that a model's bad day does not trigger a language redesign. The unfreeze rule
is normative and requires a demonstrated CORE_GAP.

**Next intended step.** Hand `b011511` and Standard 1.0 to `hml-reasoning-corpus`; regenerate
the double-encoded 50K HML view once from the frozen renderer; validate UTF-8 at the decoded
payload level; rebuild hashes and manifests; then design the matched GPU experiment.

---

## 2026-08-27 (second) — record provenance by commit, not by local path

**Branch** `main`, following `5e0fc61`.

**Objective.** Pre-publication check before pushing the Standard to its remote.

**Files and systems changed.** `tools/extract_implementation.py`,
`conformance/run_conformance.py`, `tools/audit_standard.py`, plus the regenerated artifacts
they produce (`machine/_extracted.json`, `conformance/RESULTS.json`,
`reports/STANDARD_CONFORMANCE_AUDIT.md`, manifest).

**What was completed.** A scan before publishing found three tracked files embedding the
absolute local path of the implementation checkout. The generators now record the
**implementation commit** instead. That is both the right thing to publish and strictly
better provenance: the path describes whoever ran the extraction, the commit describes what
was extracted. A credential scan found nothing; the `token` matches were all tokenizer prose.

**Decisions made and why.** The repository is private, so the path leak was low-stakes.
The change was kept anyway because commit provenance is more useful than a filesystem
location, and a Standard that pins its sources by commit everywhere else should not make an
exception here.

**Tests and verification actually executed.**

- Full regeneration from the three sources after the change.
- `conformance/run_conformance.py`: **59 specimens, 59 PASS, 0 FAIL**, 58/59 rules covered.
- `tools/audit_standard.py`: completeness, traceability, consistency, conformance — all
  **PASS**. `HML_STANDARD_FREEZE_READY = YES`.
- `grep` for `/Users/` across all tracked files: **zero remaining**.

**Failures and unresolved uncertainty.** None. No normative content changed; the rule
registry, atlas and reference are byte-identical apart from the provenance field.

**Effect on the overall project.** None on the Standard's content. The
`hml-standard-v1.0-2026-08-27` tag continues to point at `5e0fc61`, the commit whose audits
were recorded in the freeze report; this commit is a provenance correction on top of it.

**Next intended step.** Push `main` and the tag to the remote. Then hand `b011511` and
Standard 1.0 to `hml-reasoning-corpus` for the single 50K regeneration.
