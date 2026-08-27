"""Generate every derived Standard artifact from the three sources of truth.

    machine/_extracted.json   what the frozen implementation actually contains
    standard/rules.json       the normative rule registry
    standard/atlas_source.py  the mathematics -> HML map

Generated: REFERENCE.md, TRACEABILITY.md, spec/*.md, atlas/*.md, machine/*.json,
schemas/*.json.

Generating rather than hand-writing is what makes the consistency audit meaningful: the
documents cannot disagree with each other, because there is only one copy of each fact.

    python tools/build_standard.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "standard"))

EXTRACT = json.load(open(ROOT / "machine" / "_extracted.json", encoding="utf-8"))
RULES = json.load(open(ROOT / "standard" / "rules.json", encoding="utf-8"))
VERSION = json.load(open(ROOT / "VERSION.json", encoding="utf-8"))
from atlas_source import ATLAS  # noqa: E402

IMPL = "hamiltonian-lang"

# 27 spec sections. Every one carries a purpose; sections with no normative rules of their
# own say where their material lives instead of being decorative.
SPEC = [
 ("00_scope", "Scope", "What HML 1.0 standardises and what it deliberately leaves to libraries, backends and policy."),
 ("01_lexical_grammar", "Lexical grammar", "Token-level structure of the surface language."),
 ("02_abstract_syntax", "Abstract syntax", "The AST the parser produces before resolution and typing."),
 ("03_semantic_identity", "Semantic identity", "What makes two objects the same object: mapping keys, record ids, binding identity and canonical hashing."),
 ("04_type_system", "Type system", "The typed layer: scalar, structured, function, predicate, probabilistic and concept types."),
 ("05_terms_and_expressions", "Terms and expressions", "Term formation and the expressions the kernel rules operate on."),
 ("06_functions_and_predicates", "Functions and predicates", "First-class functions and predicates, arity and domain enforcement."),
 ("07_binders_and_scope", "Binders and scope", "Binding, alpha-equivalence, capture avoidance and scope visibility."),
 ("08_claims_and_propositions", "Claims and propositions", "The Claim record and the proposition it carries."),
 ("09_assumptions_and_context", "Assumptions and context", "Assumed claims, refinement context and active frames."),
 ("10_goals", "Goals", "The Goal record and goal discharge."),
 ("11_candidates", "Candidates", "Proposed objects that are not yet facts."),
 ("12_obligations", "Obligations", "Proof debt: creation, persistence and discharge."),
 ("13_branches", "Branches", "Case analysis, branch-local state and joins."),
 ("14_dependencies", "Dependencies", "The citation graph between records."),
 ("15_evidence_and_warrants", "Evidence and warrants", "What licenses a transition and what evidence attests to it."),
 ("16_actions", "Actions", "The structural action object."),
 ("17_state_transitions", "State transitions", "S_before --action--> S_after and the invariants a verifier must check."),
 ("18_epistemic_status", "Epistemic status", "The closed status vocabularies and the UNKNOWN discipline."),
 ("19_partiality", "Partiality", "Partial operations, preconditions and term-level bounds obligations."),
 ("20_verification", "Verification", "The 20-rule kernel, the trusted boundary and certificates."),
 ("21_libraries", "Libraries", "Domain reasoning that is deliberately outside the kernel."),
 ("22_backends", "Backends", "Translation targets and the obligation to declare loss."),
 ("23_serialization", "Serialization", "The neutral JSON form and canonical identity documents."),
 ("24_model_language", "Model language", "The frozen model-facing representation."),
 ("25_errors_and_failure", "Errors and failure", "ErrorClass, Finding, Verdict and the refusal discipline."),
 ("26_conformance", "Conformance", "What an implementation must do to claim conformance."),
 ("27_versioning", "Versioning and governance", "How the Standard changes, and the unfreeze rule."),
]

SECTION_BODY = {
 "00_scope": """HML 1.0 standardises the **typed semantic state and the checked transition between
states**, plus the model-facing serialization of that state.

It does **not** standardise: which theorems are true, how to search for a proof, how a
model should be trained, or how an external prover works. Those are library, policy and
backend concerns, and the Standard says so explicitly wherever the boundary falls.

The kernel is deliberately small: **20 inference rules**. A concept whose theorems live in
a library is not a deficiency of the language. The question the Standard asks of every
mathematical concept is whether HML can **carry its reasoning state losslessly** -- see
`SEMANTIC_ATLAS.md`.""",
 "01_lexical_grammar": """[INFORMATIVE] The HML surface language has a conventional lexical structure implemented in
`src/hamiltonian_lang/lexer/`. It is **not** the model-facing boundary: a model reads the
serialization specified in `24_model_language.md`, which is a separate surface with its own
reader and is not routed through this grammar.

No normative rule in HML 1.0 depends on surface token spelling. Identity is carried by
binding IDs and record keys, not by how a name is written.""",
 "02_abstract_syntax": """[INFORMATIVE] The parser produces an AST in `src/hamiltonian_lang/ast/nodes.py`, which is
resolved and typed before canonical identity is computed. The Standard's normative content
begins at the **resolved, typed** object, because that is what carries meaning.""",
 "04_type_system": """[NORMATIVE] Every object carries a type before canonical identity is
computed. Clean compilation forbids `Unknown`: an expression whose type cannot be resolved
MUST fail closed rather than be admitted with an unknown type.

The type layer includes scalar types, structured types (`VectorType`, `MatrixType`,
`TensorType`, `ProductType`, `SetType`) with `Dimension`, first-class `FunctionType` and
`PredicateType`, the probabilistic types (`EventType`, `DistributionType`,
`RandomVariableType`), `QuantityType`, `ConceptType`, and `SymbolicExtent` for resolved
finite index structure.

**Prohibited conflations.** These are enforced by the type system, not by convention, and an
implementation MUST NOT introduce a subtyping path between them:

- a `Distribution[T]` is not a value of `T`;
- a `RandomVariable[T]` is neither a `Distribution[T]` nor a `T`;
- `Probability` is not `PositiveReal` — they are incomparable, meeting at `NonNegativeReal`.

`SymbolicExtent` exists because the final closure audit found unbound and non-`Natural`
extents being accepted. Extents are now resolved and validated throughout declarations,
definitions, binders and concepts, and a finite index access is either statically refuted or
carries a term-level bounds obligation built from the resolved extent identity.

The `TYPE_DOMAIN` invariant (HML-INV-010) checks type and domain compatibility on every
transition and reports `ErrorClass.TYPE_DOMAIN_VIOLATION`.""",
 "08_claims_and_propositions": """[NORMATIVE] A `Claim` is the primary carrier of mathematical
content. It has an `id`, a `proposition`, a `ClaimStatus`, a `scope`, an optional `domain`,
and `dependencies`.

**Status is not decoration.** `ClaimStatus` is a closed vocabulary — GIVEN, ASSUMED, DERIVED,
VERIFIED, REFUTED, UNRESOLVED, UNKNOWN (HML-ENUM-003) — and it is the field that separates a
hypothesis from a fact. An action MUST NOT change a claim's status except through an
`epistemic_effect` that the `EPISTEMIC_STATUS` invariant (HML-INV-008) accepts.

**The proposition may be opaque.** In the current corpus a proposition is the pretty-printed
text of a Lean goal state, and HML carries it verbatim rather than routing it through the AST
printer. This is deliberate: routing it would make the view lossless only up to canonical
form and would couple the Standard to a grammar the corpus never agreed to. The consequence
is stated plainly in `07_binders_and_scope.md` — binder identity *inside* an opaque
proposition is Lean's, not HML's.

**Visibility.** A claim is citable only if its `scope` is a member of `active_scopes`
(HML-STATE-004). Ordering is irrelevant; membership is decisive.

**Dependencies.** A claim's `dependencies` are the claims it was derived from. They MUST
resolve (HML-INV-001), and the model-facing serialization emits claims in
dependency-topological order so a claim appears after everything it cites.""",
 "05_terms_and_expressions": """[INFORMATIVE] Terms are the expressions the kernel rules in `20_verification.md` operate
on. Their shapes are given by each rule's declared `shape` field, which is generated into
this Standard from the implementation rather than restated by hand.""",
 "06_functions_and_predicates": """[NORMATIVE] Functions and predicates are first class. A `Predicate` value may be applied,
passed and quantified over.

Arity and domain are enforced: an application with the wrong arity, or an argument outside
the declared domain, MUST fail closed rather than produce `Unknown`. The final semantic
closure audit repaired exactly this -- first-class `Function` and `Predicate` application
previously bypassed arity and domain checks.""",
 "07_binders_and_scope": """[NORMATIVE] Binders are locally nameless. Alpha-renaming MUST NOT change meaning, and
capture MUST be avoided by construction rather than by hygiene convention.

Scope visibility is decided by **membership** in `SemanticState.active_scopes`, not by
ordering (HML-STATE-004). A fact established inside a frame that is no longer active is not
visible, which is what stops a branch-local conclusion leaking into global state without a
join.

Binder identity *inside a proposition* is not HML's when the proposition is opaque source
text -- see `MODEL_REFERENCE.md` and the identifier policy in the model-language freeze.""",
 "09_assumptions_and_context": """[NORMATIVE] An assumption is a `Claim` with `ClaimStatus.ASSUMED`. It is not a fact, and no
action may silently relabel it. Refinement context, scoped assumptions and active frames
are carried explicitly; the FRAME invariant (HML-INV-011) checks that a transition does not
alter state it did not declare it would.""",
 "10_goals": """[NORMATIVE] A `Goal` carries a proposition, a `GoalStatus` of OPEN, DISCHARGED or UNKNOWN,
and a scope. Discharge is governed by the GOAL_DISCHARGE invariant (HML-INV-009): a goal
MUST NOT become DISCHARGED except through an action whose `goal_effect` says so and whose
warrant licenses it.""",
 "11_candidates": """[NORMATIVE] A `Candidate` is a proposed object that is **not** a fact. `CandidateStatus`
(PROPOSED, UNVERIFIED, VERIFIED, REJECTED, UNKNOWN) cannot express GIVEN or DERIVED, so
promotion cannot be performed by relabelling -- it requires an action and is checked by the
CANDIDATES invariant (HML-INV-005, HML-EPIS-002).

`Candidate.constraint_ids` links a candidate to the obligations that constrain it.""",
 "13_branches": """[NORMATIVE] A `Branch` carries a predicate, a `BranchStatus` (OPEN, CLOSED, JOINED,
ABANDONED, UNKNOWN), a scope and an optional `partition_id` grouping the cases of one split.

Branch-local conclusions MUST NOT escape without a join; the BRANCH_JOIN invariant
(HML-INV-006) checks it. Disjunction elimination itself is library-level -- the branch
records the case split, the kernel does not discharge it.""",
 "14_dependencies": """[NORMATIVE] Dependencies are the citation graph. Every reference an action or record makes
MUST resolve in the state it applies to (HML-ACT-002), enforced by the DEPENDENCY invariant
(HML-INV-001) and reported as `ErrorClass.MISSING_DEPENDENCY`.

The model-facing serialization emits records in dependency-topological order so a citation
appears after what it cites.""",
 "15_evidence_and_warrants": """[NORMATIVE] A **warrant** is what licenses an action; **evidence** is what attests to it.
They are separate fields and MUST NOT be conflated.

`EvidenceRecord.trusted` defaults to `False` and `status` defaults to `UNKNOWN`. Untrusted
evidence MUST NOT discharge a mandatory obligation (HML-EPIS-003). A generator MUST NOT
self-certify (HML-EPIS-004): attestation is a separate step in
`semantic_state/trust.py`.""",
 "19_partiality": """[NORMATIVE] Partial operations carry their preconditions as **obligations**, not as silent
assumptions. Division emits a nonzero obligation; a finite index access is either statically
refuted or carries a term-level bounds obligation built from the resolved `SymbolicExtent`.

This is why `divide_both_sides` appears in the kernel with an obligation attached rather
than as an unconditional rewrite.""",
 "21_libraries": """[INFORMATIVE] Libraries hold domain reasoning that is deliberately **not** in the kernel:
""" + ", ".join(f"`{l['name']}`" for l in EXTRACT["libraries"]) + """.

The semantic closure audit explicitly declined to promote category theory, causal
intervention, filtrations and numerical approximation families into the core. The atlas
records 61 concepts as `LIBRARY_GAP`: representable today, with the reasoning still to be
built. **A `LIBRARY_GAP` is not a language defect** and MUST NOT be used to justify a
semantic unfreeze.""",
 "23_serialization": """[NORMATIVE] Two serializations exist and they have different jobs.

The **neutral JSON form** (`semantic_state/neutral.py`) is the corpus interchange format.
The **canonical identity document** (`backends/canonical.py`) is the hashing form and is
deliberately ASCII-encoded (HML-REP-004); every recorded example hash depends on those
bytes.

The model-facing surface is specified separately in `24_model_language.md` and is
deliberately **not** ASCII (HML-REP-003). Identity documents stay ASCII; model-facing
surfaces stay literal.""",
 "25_errors_and_failure": """[NORMATIVE] Failure is a first-class outcome. A verifier returns a `Verdict` of VALID,
INVALID or **UNRESOLVED**, and UNRESOLVED MUST NOT be reported as INVALID (HML-TRANS-001).

Violations are reported as findings carrying an `ErrorClass` drawn from a closed vocabulary
of ten values. A reader that cannot represent an object MUST refuse it rather than return a
partial result: a half-parsed state that looks plausible is worse than no state, because
nothing downstream can tell the difference.""",
 "26_conformance": """[NORMATIVE] See `CONFORMANCE.md` for the full definition. In summary, a conforming
implementation MUST satisfy every rule marked NORMATIVE in `standard/rules.json`, and MUST
be able to reproduce the outcomes recorded in `conformance/RESULTS.json`.""",
}


def _rules_for(section: str) -> list[dict]:
    return [r for r in RULES["rules"] if r["spec_section"] == f"spec/{section}.md"]


def _rule_block(r: dict) -> str:
    out = [f"#### {r['id']} — {r.get('name', r['category'])}  `[{r['status']}]`", ""]
    out.append(r["statement"])
    out.append("")
    if r.get("members"):
        out.append(f"Closed vocabulary: `{r['members']}`")
        out.append("")
    if r.get("shape"):
        out.append(f"Shape: `{r['shape']}`  ·  arity {r['arity']}"
                   + (f"  ·  params `{r['params']}`" if r.get("params") else ""))
        if r.get("obligations"):
            out.append(f"Obligations emitted: `{r['obligations']}`")
        if r.get("side_conditions"):
            out.append(f"Side conditions: `{r['side_conditions']}`")
        out.append("")
    impl = r.get("implementation_file")
    sym = r.get("implementation_symbol")
    out.append(f"Implementation: `{impl}` · `{sym}`" if impl else "Implementation: —")
    if r.get("conformance"):
        out.append(f"  ·  Conformance: `{r['conformance']}`")
    elif r.get("not_mechanically_testable"):
        out.append(f"  ·  Conformance: **none** — {r['not_mechanically_testable']}")
    out.append("")
    return "\n".join(out)


def build_spec() -> int:
    d = ROOT / "spec"
    d.mkdir(exist_ok=True)
    for slug, title, purpose in SPEC:
        rules = _rules_for(slug)
        body = [f"# {title}", "",
                f"*HML Standard {VERSION['version']} — {VERSION['release_date']}*", "",
                purpose, ""]
        extra = SECTION_BODY.get(slug)
        if extra:
            body += [extra, ""]
        if rules:
            body += [f"## Normative rules ({len(rules)})", ""]
            body += [_rule_block(r) for r in rules]
        elif not extra:
            body += ["## Normative rules", "",
                     "**This section carries no normative rules of its own in HML 1.0.**",
                     "",
                     "That is a deliberate statement, not an omission: the material is "
                     "specified where it is enforced. See the sections referenced above "
                     "and `REFERENCE.md` for the objects involved.", ""]
        else:
            body += ["## Normative rules", "",
                     "No rules are registered against this section; the requirements above "
                     "are enforced through the rules listed in the sections they name.", ""]
        (d / f"{slug}.md").write_text("\n".join(body), encoding="utf-8")
    return len(SPEC)


def build_reference() -> int:
    rows = []
    lines = [f"# HML Reference — complete dictionary", "",
             f"*HML Standard {VERSION['version']} — {VERSION['release_date']}*", "",
             "Generated from the frozen implementation at "
             f"`{VERSION['semantic_implementation_commit'][:12]}`. "
             "Every row is extracted, not transcribed.", ""]

    lines += ["## Semantic state records", "",
              "| Object | Category | Fields | Frozen | Implementation |",
              "|---|---|---|---|---|"]
    for r in EXTRACT["state_records"]:
        names = ", ".join(f["name"] for f in r["fields"])
        lines.append(f"| `{r['name']}` | state record | {len(r['fields'])}: {names} | "
                     f"{'yes' if r['frozen'] else 'NO'} | `{r['file']}:{r['line']}` |")
        rows.append({"id": f"HML.REF.{r['name'].upper()}", "name": r["name"],
                     "category": "state_record", "fields": r["fields"],
                     "implementation": f"{r['file']}:{r['line']}", "status": "normative"})
    lines.append("")

    lines += ["## Status vocabularies", "", "| Vocabulary | Members | Implementation |",
              "|---|---|---|"]
    for e in EXTRACT["enumerations"]:
        if e["name"] == "StrEnum":
            continue
        lines.append(f"| `{e['name']}` | {', '.join('`'+m+'`' for m in e['members'])} | "
                     f"`{e['file']}:{e['line']}` |")
        rows.append({"id": f"HML.REF.{e['name'].upper()}", "name": e["name"],
                     "category": "vocabulary", "members": e["members"],
                     "implementation": f"{e['file']}:{e['line']}", "status": "normative"})
    lines.append("")

    lines += ["## Types", "", "| Type | Implementation |", "|---|---|"]
    for t in EXTRACT["types"]:
        lines.append(f"| `{t['name']}` | `{t['file']}:{t['line']}` |")
        rows.append({"id": f"HML.REF.TYPE.{t['name'].upper()}", "name": t["name"],
                     "category": "type", "implementation": f"{t['file']}:{t['line']}",
                     "status": "normative"})
    lines.append("")

    lines += ["## Kernel inference rules", "",
              f"The kernel has exactly **{EXTRACT['kernel_rule_count']}** inference rules. "
              "Everything else is library, backend or policy.", "",
              "| Rule | Arity | Shape | Obligations | Side conditions |", "|---|---|---|---|---|"]
    for r in EXTRACT["kernel_rules"]:
        lines.append(f"| `{r['name']}` | {r['arity']} | `{r['shape']}` | "
                     f"{r.get('obligations') or '—'} | {r.get('side_conditions') or '—'} |")
        rows.append({"id": f"HML.REF.KERNEL.{r['name'].upper()}", "name": r["name"],
                     "category": "kernel_rule", "shape": r["shape"], "arity": r["arity"],
                     "implementation": "src/hamiltonian_lang/reasoning/kernel.py",
                     "status": "normative"})
    lines.append("")

    lines += ["## Backends", "",
              "| Backend | Implementation | Must declare loss |", "|---|---|---|"]
    for b in EXTRACT["backends"]:
        if b["name"] == "base":
            continue
        lines.append(f"| `{b['name']}` | `{b['file']}` | yes (HML-BACK-001) |")
        rows.append({"id": f"HML.REF.BACKEND.{b['name'].upper()}", "name": b["name"],
                     "category": "backend", "implementation": b["file"],
                     "status": "implemented"})
    lines.append("")

    lines += ["## Libraries", "", "| Library | Implementation | Status |", "|---|---|---|"]
    for l in EXTRACT["libraries"]:
        lines.append(f"| `{l['name']}` | `{l['file']}` | implemented, non-kernel |")
        rows.append({"id": f"HML.REF.LIBRARY.{l['name'].upper()}", "name": l["name"],
                     "category": "library", "implementation": l["file"],
                     "status": "implemented"})

    (ROOT / "REFERENCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "machine" / "hml_dictionary.json").write_text(
        json.dumps({"standard": "HML Standard", "version": VERSION["version"],
                    "entries": rows, "total": len(rows)}, indent=1, ensure_ascii=False)
        + "\n", encoding="utf-8")
    return len(rows)


def build_atlas() -> tuple[int, int]:
    d = ROOT / "atlas"
    d.mkdir(exist_ok=True)
    entries = []
    verdicts: dict[str, int] = {}
    for domain, items in ATLAS.items():
        lines = [f"# {domain.replace('_', ' ').title()}", "",
                 f"*HML Standard {VERSION['version']} — semantic atlas*", "",
                 "The question each row answers is **not** whether HML proves the concept. "
                 "It is whether HML can carry its reasoning state losslessly.", "",
                 "| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |",
                 "|---|---|---|---|---|---|---|"]
        for (concept, role, rep, carry, manip, verify, verdict, note) in items:
            lines.append(f"| {concept} | {role} | {rep} | {'yes' if carry else 'no'} | "
                         f"{'yes' if manip else 'no'} | {verify} | **{verdict}** |")
            verdicts[verdict] = verdicts.get(verdict, 0) + 1
            entries.append({
                "id": f"HML.ATLAS.{domain.upper()}.{concept.upper().replace(' ', '_').replace('/', '_')}",
                "domain": domain, "concept": concept, "role": role,
                "hml_representation": rep, "carry": bool(carry),
                "manipulate": bool(manip), "verify": verify, "verdict": verdict,
                "note": note, "version_first_checked": VERSION["version"],
                "evidence_confidence": "extracted_and_reviewed" if note else "reviewed",
            })
        notes = [(c, n) for (c, _r, _h, _ca, _m, _v, _vd, n) in items if n]
        if notes:
            lines += ["", "## Notes", ""]
            lines += [f"- **{c}** — {n}" for c, n in notes]
        lines.append("")
        (d / f"{domain}.md").write_text("\n".join(lines), encoding="utf-8")

    readme = ["# Semantic atlas", "",
              f"*HML Standard {VERSION['version']} — {VERSION['release_date']}*", "",
              f"{len(entries)} concepts across {len(ATLAS)} domains.", "",
              "## Verdict distribution", "", "| Verdict | Count | Meaning |", "|---|---:|---|"]
    meaning = {
        "NO_GAP": "representable and manipulable with frozen machinery",
        "LIBRARY_GAP": "representable; the reasoning needs a library that does not exist yet",
        "BACKEND_GAP": "representable; checking needs an external backend",
        "REPRESENTATION_GAP": "the model-facing surface cannot carry it losslessly",
        "CORE_GAP": "the semantic core genuinely cannot represent the state",
        "POLICY_GAP": "representable; what is missing is search, not language",
        "UNSUPPORTED": "out of scope for HML 1.0",
    }
    for v, n in sorted(verdicts.items(), key=lambda x: -x[1]):
        readme.append(f"| **{v}** | {n} | {meaning.get(v, '')} |")
    readme += ["", "## The result that matters", "",
               f"**{verdicts.get('CORE_GAP', 0)} CORE_GAPs.** Across {len(entries)} concepts "
               f"in {len(ATLAS)} domains, no mapped concept was found whose *reasoning state* "
               "the frozen semantic core cannot carry.", "",
               f"The {verdicts.get('LIBRARY_GAP', 0)} `LIBRARY_GAP` entries are the honest "
               "shape of the work remaining, and they are library work, not language work. "
               "A `LIBRARY_GAP` MUST NOT be used to justify a semantic unfreeze — see "
               "`spec/27_versioning.md`.", "",
               "## Domains", ""]
    readme += [f"- [{k.replace('_', ' ').title()}]({k}.md) — {len(v)} concepts"
               for k, v in ATLAS.items()]
    (d / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    (ROOT / "machine" / "hml_atlas.json").write_text(
        json.dumps({"standard": "HML Standard", "version": VERSION["version"],
                    "domains": len(ATLAS), "total": len(entries),
                    "verdicts": verdicts, "entries": entries},
                   indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(ATLAS), len(entries)


def build_traceability() -> int:
    results = {}
    rp = ROOT / "conformance" / "RESULTS.json"
    if rp.exists():
        for r in json.load(open(rp, encoding="utf-8"))["results"]:
            results.setdefault(r["rule"], []).append(r["outcome"])
    lines = ["# Traceability matrix", "",
             f"*HML Standard {VERSION['version']} — {VERSION['release_date']}*", "",
             "Every normative rule, the section that states it, the implementation that "
             "enforces it, and the conformance specimen that proves it.", "",
             "| Rule | Spec section | Implementation | Symbol | Conformance | Status |",
             "|---|---|---|---|---|---|"]
    traced = 0
    for r in RULES["rules"]:
        outcomes = results.get(r["id"], [])
        if outcomes:
            status = "PASS" if all(o == "PASS" for o in outcomes) else "**FAIL**"
            traced += 1
        elif r.get("not_mechanically_testable"):
            status = "N/A — governance"
        else:
            status = "**NO SPECIMEN**"
        lines.append(
            f"| `{r['id']}` | `{r['spec_section']}` | `{r.get('implementation_file') or '—'}` "
            f"| `{r.get('implementation_symbol') or '—'}` | "
            f"`{r.get('conformance') or '—'}` | {status} |")
    lines += ["", f"**{traced}/{len(RULES['rules'])} rules have a passing conformance "
              f"specimen.**", ""]
    (ROOT / "TRACEABILITY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return traced


def build_machine() -> None:
    (ROOT / "machine" / "hml_reference.json").write_text(
        json.dumps({"standard": "HML Standard", "version": VERSION["version"],
                    "release_date": VERSION["release_date"],
                    "pins": {k: VERSION[k] for k in
                             ("semantic_implementation_commit", "semantic_tag",
                              "model_language_commit", "model_language_tag")},
                    "rules": RULES["rules"],
                    "counts": {"rules": RULES["total"],
                               "kernel_rules": EXTRACT["kernel_rule_count"],
                               "state_records": len(EXTRACT["state_records"]),
                               "types": len(EXTRACT["types"])}},
                   indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    schemas = ROOT / "schemas"
    schemas.mkdir(exist_ok=True)
    by_name = {r["name"]: r for r in EXTRACT["state_records"]}

    def schema_for(name: str, title: str) -> dict:
        rec = by_name[name]
        props, required = {}, []
        for f in rec["fields"]:
            t = f["type"]
            if "tuple" in t or "list" in t:
                js: dict = {"type": "array"}
            elif "dict" in t or "Mapping" in t:
                js = {"type": "object"}
            elif "bool" in t:
                js = {"type": "boolean"}
            elif "Status" in t or "State" in t:
                enum = next((e["members"] for e in EXTRACT["enumerations"]
                             if e["name"] in t), None)
                js = {"type": "string"}
                if enum:
                    js["enum"] = enum
            else:
                js = {"type": ["string", "null"]}
            props[f["name"]] = js
            if not f["has_default"]:
                required.append(f["name"])
        return {"$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": f"https://hml-standard/schemas/{name.lower()}.schema.json",
                "title": title, "type": "object", "properties": props,
                "required": required, "additionalProperties": False,
                "x-hml-standard-version": VERSION["version"],
                "x-implementation": f"{rec['file']}:{rec['line']}"}

    for fname, rec, title in (("semantic_state", "SemanticState", "HML semantic state"),
                              ("action", "Action", "HML action"),
                              ("obligation", "Obligation", "HML obligation"),
                              ("evidence", "EvidenceRecord", "HML evidence record")):
        (schemas / f"{fname}.schema.json").write_text(
            json.dumps(schema_for(rec, title), indent=1) + "\n", encoding="utf-8")

    (schemas / "atlas_entry.schema.json").write_text(json.dumps({
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://hml-standard/schemas/atlas_entry.schema.json",
        "title": "HML semantic atlas entry", "type": "object",
        "properties": {
            "id": {"type": "string"}, "domain": {"type": "string"},
            "concept": {"type": "string"}, "role": {"type": "string"},
            "hml_representation": {"type": "string"},
            "carry": {"type": "boolean"}, "manipulate": {"type": "boolean"},
            "verify": {"enum": ["CORE", "LIBRARY", "BACKEND", "UNSUPPORTED"]},
            "verdict": {"enum": ["NO_GAP", "LIBRARY_GAP", "BACKEND_GAP",
                                 "REPRESENTATION_GAP", "CORE_GAP", "POLICY_GAP",
                                 "UNSUPPORTED"]},
            "note": {"type": "string"},
            "version_first_checked": {"type": "string"},
            "evidence_confidence": {"type": "string"}},
        "required": ["id", "domain", "concept", "hml_representation", "carry",
                     "manipulate", "verify", "verdict"],
        "additionalProperties": False}, indent=1) + "\n", encoding="utf-8")


def main() -> int:
    n_spec = build_spec()
    n_ref = build_reference()
    n_dom, n_con = build_atlas()
    build_machine()
    n_tr = build_traceability()
    print(f"spec sections     : {n_spec}")
    print(f"reference entries : {n_ref}")
    print(f"atlas             : {n_dom} domains, {n_con} concepts")
    print(f"traceability      : {n_tr}/{RULES['total']} rules with a passing specimen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
