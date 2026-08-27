"""Build the normative rule registry.

Mechanical rules -- the 20 kernel inference rules and the 11 transition invariants -- are
GENERATED from the extraction, so the Standard cannot claim a rule the implementation does
not have, or miss one it does. Cross-cutting rules that no extraction can produce are
curated below, and every one of them names the conformance specimen that proves it.

    python tools/build_rules.py
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
EXTRACT = json.load(open(HERE / "machine" / "_extracted.json", encoding="utf-8"))

IMPL = "src/hamiltonian_lang"

# ---------------------------------------------------------------------------
# Curated cross-cutting rules. Each is normative, testable, and traced.
# ---------------------------------------------------------------------------
CURATED = [
    # -- semantic state structure ------------------------------------------
    ("HML-STATE-001", "state", "NORMATIVE",
     "A semantic state MUST consist of exactly the five record mappings claims, "
     "candidates, branches, goals and obligations, together with an ordered tuple of "
     "active scopes.",
     f"{IMPL}/semantic_state/model.py", "SemanticState", "conformance/valid/state_minimal"),
    ("HML-STATE-002", "state", "NORMATIVE",
     "Every semantic-state record MUST be immutable. An implementation MUST NOT mutate a "
     "record in place; a transition produces a new state.",
     f"{IMPL}/semantic_state/model.py", "frozen=True", "conformance/valid/state_minimal"),
    ("HML-STATE-003", "state", "NORMATIVE",
     "The mapping key under which a record is filed MAY differ from the record's own id "
     "field. A serializer MUST preserve both; a reader MUST NOT collapse them.",
     f"{IMPL}/semantic_state/neutral.py", "import_state", "conformance/round_trip/key_id_disagree"),
    ("HML-STATE-004", "state", "NORMATIVE",
     "A claim is visible from the current context if and only if its scope is a member of "
     "the state's active scopes. Visibility MUST be decided by membership, not by ordering.",
     f"{IMPL}/semantic_state/model.py", "SemanticState.visible", "conformance/invalid/scope_leak"),

    # -- epistemic status ---------------------------------------------------
    ("HML-EPIS-001", "epistemic", "NORMATIVE",
     "UNKNOWN is a value, not an absence. An implementation MUST NOT map UNKNOWN to FALSE, "
     "to a default, or to a missing field.",
     f"{IMPL}/semantic_state/model.py", "ClaimStatus.UNKNOWN",
     "conformance/invalid/unknown_collapsed_to_false"),
    ("HML-EPIS-002", "epistemic", "NORMATIVE",
     "A candidate MUST NOT acquire the epistemic standing of a claim without an action "
     "whose candidate_effect promotes it and whose warrant licenses the promotion.",
     f"{IMPL}/semantic_state/verify.py", "CANDIDATES",
     "conformance/invalid/candidate_promoted_without_warrant"),
    ("HML-EPIS-003", "epistemic", "NORMATIVE",
     "Evidence trust and claim status are independent. An EvidenceRecord being present "
     "MUST NOT by itself raise a claim's status, and trusted=False evidence MUST NOT "
     "discharge a mandatory obligation.",
     f"{IMPL}/semantic_state/model.py", "EvidenceRecord.trusted",
     "conformance/invalid/untrusted_evidence_discharge"),
    ("HML-EPIS-004", "epistemic", "NORMATIVE",
     "A generator MUST NOT self-certify. An actor proposing a transition MUST NOT assert "
     "its own verification status; only the verifier assigns a Verdict.",
     f"{IMPL}/semantic_state/trust.py", "attest", "conformance/invalid/self_certification"),

    # -- obligations --------------------------------------------------------
    ("HML-OBL-001", "obligations", "NORMATIVE",
     "A mandatory obligation MUST persist across transitions until an action explicitly "
     "discharges it with attested evidence. Silent disappearance MUST be rejected.",
     f"{IMPL}/semantic_state/verify.py", "OBLIGATIONS",
     "conformance/invalid/obligation_dropped"),
    ("HML-OBL-002", "obligations", "NORMATIVE",
     "An obligation's state MUST be one of OPEN, DISCHARGED, FAILED or UNKNOWN.",
     f"{IMPL}/semantic_state/model.py", "ObligationState", "conformance/valid/obligation_open"),

    # -- actions and transitions -------------------------------------------
    ("HML-ACT-001", "actions", "NORMATIVE",
     "An action MUST be represented structurally. An implementation MUST NOT treat the "
     "operation name alone as the reasoning decision; the decision is the action applied "
     "to a specific state.",
     f"{IMPL}/semantic_state/model.py", "Action", "conformance/valid/action_structural"),
    ("HML-ACT-002", "actions", "NORMATIVE",
     "Every reference an action makes -- dependencies, output_id, obligations discharged -- "
     "MUST resolve in the state it is applied to.",
     f"{IMPL}/semantic_state/verify.py", "DEPENDENCY",
     "conformance/invalid/missing_dependency"),
    ("HML-TRANS-001", "transitions", "NORMATIVE",
     "A transition MUST be the triple (state_before, action, state_after) together with "
     "the evidence offered for it. The verifier returns a Verdict of VALID, INVALID or "
     "UNRESOLVED; UNRESOLVED MUST NOT be reported as INVALID.",
     f"{IMPL}/semantic_state/verify.py", "verify", "conformance/valid/transition_minimal"),

    # -- serialization / model-facing --------------------------------------
    ("HML-REP-001", "representation", "NORMATIVE",
     "The model-facing serialization MUST be lossless: parse(render(S)) == S under "
     "structural equality of the whole transition.",
     f"{IMPL}/semantic_state/view.py", "render_transition/parse_transition",
     "conformance/round_trip/all_records"),
    ("HML-REP-002", "representation", "NORMATIVE",
     "The model-facing serialization MUST be deterministic: if A == B then "
     "render(A) == render(B). Emission order MUST NOT depend on mapping construction order.",
     f"{IMPL}/semantic_state/view.py", "_emit_order",
     "conformance/round_trip/determinism"),
    ("HML-REP-003", "representation", "NORMATIVE",
     "The model-facing boundary MUST carry decoded UTF-8. A model-facing payload MUST NOT "
     "contain \\uXXXX escape sequences standing for mathematical characters.",
     f"{IMPL}/semantic_state/view.py", "_dumps",
     "conformance/invalid/double_encoded_payload"),
    ("HML-REP-004", "representation", "NORMATIVE",
     "Canonical identity documents MUST remain ASCII-encoded. This is deliberately the "
     "opposite of HML-REP-003: identity documents and model-facing surfaces are different "
     "artifacts with different consumers.",
     f"{IMPL}/backends/canonical.py", "ensure_ascii=True",
     "conformance/valid/canonical_ascii"),
    ("HML-REP-005", "representation", "NORMATIVE",
     "The serialization MUST NOT leak the action into the state rendering. Rendering a "
     "state MUST NOT reveal the action that is to be predicted from it.",
     f"{IMPL}/semantic_state/view.py", "render_state",
     "conformance/valid/no_action_leak"),

    # -- backends -----------------------------------------------------------
    ("HML-BACK-001", "backends", "NORMATIVE",
     "A backend that cannot express a construct MUST declare the loss through drop(), "
     "approximate() or weaken(). Silent omission MUST NOT occur.",
     f"{IMPL}/backends/base.py", "Backend", "conformance/valid/backend_declares_loss"),

    # -- versioning ---------------------------------------------------------
    ("HML-VER-001", "versioning", "NORMATIVE",
     "A conforming artifact MUST record the semantic implementation commit and the "
     "model-language commit it was produced against.",
     "VERSION.json", "-", "conformance/valid/version_manifest"),
    ("HML-VER-002", "versioning", "NORMATIVE",
     "A frozen semantic feature MUST NOT be changed because a model performs badly, a "
     "notation looks preferable, or a benchmark disappoints. Unfreeze REQUIRES a "
     "demonstrated CORE_GAP as defined in spec/27_versioning.md.",
     "spec/27_versioning.md", "-", "-"),
]


def main() -> int:
    rules = []

    # ---- generated: the 20 kernel inference rules -------------------------
    for i, r in enumerate(EXTRACT["kernel_rules"], start=1):
        rules.append({
            "id": f"HML-KERNEL-{i:03d}",
            "category": "kernel",
            "status": "NORMATIVE",
            "name": r["name"],
            "statement": (
                f"The kernel rule `{r['name']}` MUST have arity {r['arity']} and the shape "
                f"`{r['shape']}`. "
                + (f"It MUST emit the obligations {r['obligations']}. "
                   if r.get("obligations") else "")
                + (f"It MUST enforce the side conditions {r['side_conditions']}. "
                   if r.get("side_conditions") else "")
                + (r.get("doc") or "")
            ).strip(),
            "arity": r["arity"],
            "params": r.get("params", []),
            "shape": r["shape"],
            "obligations": r.get("obligations", []),
            "side_conditions": r.get("side_conditions", []),
            "spec_section": "spec/20_verification.md",
            "implementation_file": f"{IMPL}/reasoning/kernel.py",
            "implementation_symbol": f"RULES[{r['name']!r}]",
            "conformance": f"conformance/valid/kernel_{r['name']}",
            "generated": True,
        })

    # ---- generated: the 11 transition invariants --------------------------
    invariants = ["DEPENDENCY", "SCOPE", "PRECONDITIONS", "OBLIGATIONS", "CANDIDATES",
                  "BRANCH_JOIN", "WARRANT", "EPISTEMIC_STATUS", "GOAL_DISCHARGE",
                  "TYPE_DOMAIN", "FRAME"]
    for i, name in enumerate(invariants, start=1):
        rules.append({
            "id": f"HML-INV-{i:03d}",
            "category": "invariants",
            "status": "NORMATIVE",
            "name": name,
            "statement": (
                f"A conforming verifier MUST check the {name} invariant on every transition "
                f"and MUST report a violation as a Finding carrying an ErrorClass."
            ),
            "spec_section": "spec/17_state_transitions.md",
            "implementation_file": f"{IMPL}/semantic_state/verify.py",
            "implementation_symbol": f"INVARIANTS[{name!r}]",
            "conformance": f"conformance/invalid/invariant_{name.lower()}",
            "generated": True,
        })

    # ---- generated: status vocabularies are closed ------------------------
    for i, e in enumerate(
            [x for x in EXTRACT["enumerations"] if x["name"] != "StrEnum"], start=1):
        rules.append({
            "id": f"HML-ENUM-{i:03d}",
            "category": "vocabulary",
            "status": "NORMATIVE",
            "name": e["name"],
            "statement": (
                f"`{e['name']}` is a closed vocabulary. A conforming implementation MUST "
                f"accept exactly {e['members']} and MUST reject any other value."
            ),
            "members": e["members"],
            "spec_section": "spec/18_epistemic_status.md",
            "implementation_file": e["file"],
            "implementation_symbol": e["name"],
            "conformance": f"conformance/invalid/enum_{e['name'].lower()}_unknown_member",
            "generated": True,
        })

    # ---- curated ----------------------------------------------------------
    for rid, cat, status, statement, impl_file, impl_sym, conf in CURATED:
        rules.append({
            "id": rid, "category": cat, "status": status, "statement": statement,
            "spec_section": None, "implementation_file": impl_file,
            "implementation_symbol": impl_sym, "conformance": conf, "generated": False,
        })

    spec_for = {
        "state": "spec/03_semantic_identity.md",
        "epistemic": "spec/18_epistemic_status.md",
        "obligations": "spec/12_obligations.md",
        "actions": "spec/16_actions.md",
        "transitions": "spec/17_state_transitions.md",
        "representation": "spec/24_model_language.md",
        "backends": "spec/22_backends.md",
        "versioning": "spec/27_versioning.md",
    }
    for r in rules:
        if r.get("spec_section") is None:
            r["spec_section"] = spec_for.get(r["category"], "spec/00_scope.md")

    # HML-VER-002 is a governance rule about how the Standard may change. It is not
    # mechanically testable, and marking it so is more honest than writing a test that
    # asserts the text of a policy back to itself.
    for r in rules:
        if r["id"] == "HML-VER-002":
            r["conformance"] = None
            r["not_mechanically_testable"] = (
                "Governance rule about the process for changing the Standard. No executable "
                "specimen can establish that a future change followed it.")

    out = {
        "standard": "HML Standard",
        "version": "1.0",
        "release_date": "2026-08-27",
        "total": len(rules),
        "by_category": {},
        "rules": rules,
    }
    for r in rules:
        out["by_category"][r["category"]] = out["by_category"].get(r["category"], 0) + 1

    (HERE / "standard" / "rules.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote standard/rules.json: {len(rules)} normative rules")
    for k, v in sorted(out["by_category"].items()):
        print(f"  {k:<16} {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
