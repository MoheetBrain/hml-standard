"""The four pre-freeze audits, executed rather than asserted.

Completeness, traceability, consistency and conformance. Each writes a report under
`reports/` recording what was actually checked and what was found. An audit that cannot
check something says so instead of passing it.

    python tools/audit_standard.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "standard"))

EXTRACT = json.load(open(ROOT / "machine" / "_extracted.json", encoding="utf-8"))
RULES = json.load(open(ROOT / "standard" / "rules.json", encoding="utf-8"))
VERSION = json.load(open(ROOT / "VERSION.json", encoding="utf-8"))
RESULTS = json.load(open(ROOT / "conformance" / "RESULTS.json", encoding="utf-8"))
from atlas_source import ATLAS  # noqa: E402

REFERENCE = (ROOT / "REFERENCE.md").read_text(encoding="utf-8")
STANDARD = (ROOT / "STANDARD.md").read_text(encoding="utf-8")
MODELREF = (ROOT / "MODEL_REFERENCE.md").read_text(encoding="utf-8")


def _w(name: str, title: str, lines: list[str], ok: bool) -> bool:
    body = [f"# {title}", "",
            f"*HML Standard {VERSION['version']} — {VERSION['release_date']}*", "",
            f"**Result: {'PASS' if ok else 'FAIL'}**", ""] + lines + [""]
    (ROOT / "reports" / name).write_text("\n".join(body), encoding="utf-8")
    return ok


def completeness() -> bool:
    """Every public frozen semantic object must appear in STANDARD or REFERENCE."""
    lines, missing = [], []
    objects = (
        [(r["name"], "state record") for r in EXTRACT["state_records"]]
        + [(e["name"], "vocabulary") for e in EXTRACT["enumerations"] if e["name"] != "StrEnum"]
        + [(t["name"], "type") for t in EXTRACT["types"]]
        + [(k["name"], "kernel rule") for k in EXTRACT["kernel_rules"]]
        + [(b["name"], "backend") for b in EXTRACT["backends"] if b["name"] != "base"]
        + [(l["name"], "library") for l in EXTRACT["libraries"]]
    )
    for name, kind in objects:
        if name not in REFERENCE and name not in STANDARD:
            missing.append((name, kind))
    lines += [f"Frozen public objects checked: **{len(objects)}**",
              f"Objects absent from both STANDARD.md and REFERENCE.md: **{len(missing)}**", ""]
    if missing:
        lines += ["| Object | Kind |", "|---|---|"]
        lines += [f"| `{n}` | {k} |" for n, k in missing]
    else:
        lines.append("Every extracted object is documented.")
    lines += ["", "## Atlas coverage", "",
              f"Domains: **{len(ATLAS)}** · concepts: "
              f"**{sum(len(v) for v in ATLAS.values())}**"]
    return _w("STANDARD_COMPLETENESS_AUDIT.md", "Completeness audit", lines, not missing)


def traceability() -> bool:
    """Every normative rule must name an implementation and a specimen, or say why not."""
    lines, bad = [], []
    for r in RULES["rules"]:
        has_impl = bool(r.get("implementation_file"))
        has_conf = bool(r.get("conformance")) or bool(r.get("not_mechanically_testable"))
        has_spec = bool(r.get("spec_section"))
        if not (has_impl and has_conf and has_spec):
            bad.append(r["id"])
    covered = {x["rule"] for x in RESULTS["results"]}
    untested = [r["id"] for r in RULES["rules"]
                if r["id"] not in covered and not r.get("not_mechanically_testable")]
    lines += [f"Normative rules: **{RULES['total']}**",
              f"Rules missing an implementation, spec section or conformance link: "
              f"**{len(bad)}**",
              f"Rules with no specimen and no stated reason: **{len(untested)}**", ""]
    if bad:
        lines.append("Incomplete: " + ", ".join(f"`{x}`" for x in bad))
    if untested:
        lines.append("Untested: " + ", ".join(f"`{x}`" for x in untested))
    governance = [r["id"] for r in RULES["rules"] if r.get("not_mechanically_testable")]
    lines += ["", "## Deliberately untestable", ""]
    for g in governance:
        r = next(x for x in RULES["rules"] if x["id"] == g)
        lines.append(f"- `{g}` — {r['not_mechanically_testable']}")
    if not governance:
        lines.append("None.")
    return _w("STANDARD_TRACEABILITY_AUDIT.md", "Traceability audit", lines,
              not bad and not untested)


def consistency() -> bool:
    """The documents must not contradict each other or the extraction."""
    lines, problems = [], []

    n_kernel = EXTRACT["kernel_rule_count"]
    for doc, name in ((STANDARD, "STANDARD.md"), (MODELREF, "MODEL_REFERENCE.md"),
                      (REFERENCE, "REFERENCE.md")):
        if f"**{n_kernel}**" not in doc and f"{n_kernel} " not in doc:
            problems.append(f"{name} does not state the kernel rule count {n_kernel}")

    counted = sum(1 for _ in re.finditer(r"HML-[A-Z]+-\d{3}", STANDARD))
    lines.append(f"Kernel rule count in extraction: **{n_kernel}**")
    lines.append(f"Rule references in STANDARD.md: **{counted}**")

    # every rule ID cited in prose must exist in the registry
    ids = {r["id"] for r in RULES["rules"]}
    for doc, name in ((STANDARD, "STANDARD.md"), (MODELREF, "MODEL_REFERENCE.md"),
                      ((ROOT / "CONFORMANCE.md").read_text(encoding="utf-8"),
                       "CONFORMANCE.md")):
        for cited in set(re.findall(r"HML-[A-Z]+-\d{3}", doc)):
            if cited not in ids:
                problems.append(f"{name} cites unknown rule {cited}")

    # the state delta must be non-normative everywhere it is mentioned
    if VERSION["normative_state_delta"] is not False:
        problems.append("VERSION.json marks the state delta normative")
    if "SPECIFIED_NOT_FROZEN" not in STANDARD:
        problems.append("STANDARD.md does not mark the state delta SPECIFIED_NOT_FROZEN")

    # vocabularies must match the extraction exactly
    for e in EXTRACT["enumerations"]:
        if e["name"] == "StrEnum":
            continue
        for m in e["members"]:
            if m not in REFERENCE:
                problems.append(f"REFERENCE.md missing {e['name']} member {m}")

    # machine artifacts must agree with the registry
    md = json.load(open(ROOT / "machine" / "hml_dictionary.json", encoding="utf-8"))
    mr = json.load(open(ROOT / "machine" / "hml_reference.json", encoding="utf-8"))
    ma = json.load(open(ROOT / "machine" / "hml_atlas.json", encoding="utf-8"))
    if mr["counts"]["rules"] != RULES["total"]:
        problems.append("machine/hml_reference.json rule count disagrees with the registry")
    if ma["total"] != sum(len(v) for v in ATLAS.values()):
        problems.append("machine/hml_atlas.json concept count disagrees with the atlas")

    lines += ["", f"Dictionary entries: **{md['total']}** · atlas entries: **{ma['total']}** "
              f"· registry rules: **{mr['counts']['rules']}**", "",
              f"Contradictions found: **{len(problems)}**", ""]
    lines += [f"- {p}" for p in problems] or ["No contradictions found."]
    return _w("STANDARD_CONSISTENCY_AUDIT.md", "Consistency audit", lines, not problems)


def conformance() -> bool:
    lines = [f"Specimens executed: **{RESULTS['total_specimens']}**",
             f"Passed: **{RESULTS['passed']}** · Failed: **{RESULTS['failed']}**",
             f"Rules with a specimen: **{RESULTS['rules_with_specimen']}"
             f"/{RESULTS['rules_total']}**", "",
             f"Implementation under test: `{RESULTS['implementation_root']}`", "",
             "## Failures", ""]
    fails = [r for r in RESULTS["results"] if r["outcome"] == "FAIL"]
    lines += [f"- `{r['rule']}` {r['name']}: {r['detail']}" for r in fails] or ["None."]
    lines += ["", "## Rules with no specimen", ""]
    ns = RESULTS["rules_without_specimen"]
    if ns:
        for rid in ns:
            r = next(x for x in RULES["rules"] if x["id"] == rid)
            why = r.get("not_mechanically_testable", "**no reason recorded**")
            lines.append(f"- `{rid}` — {why}")
    else:
        lines.append("None.")
    return _w("STANDARD_CONFORMANCE_AUDIT.md", "Conformance audit", lines,
              RESULTS["failed"] == 0)


def main() -> int:
    checks = [("completeness", completeness()), ("traceability", traceability()),
              ("consistency", consistency()), ("conformance", conformance())]
    for name, ok in checks:
        print(f"  {name:<14} {'PASS' if ok else 'FAIL'}")
    allok = all(ok for _n, ok in checks)
    print(f"\nHML_STANDARD_FREEZE_READY = {'YES' if allok else 'NO'}")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
