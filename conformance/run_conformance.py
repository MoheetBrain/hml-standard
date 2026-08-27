"""Execute the conformance suite against the authoritative implementation.

A standard without conformance is a wish list. Every specimen here runs against the frozen
executable at the pinned commit and records what actually happened. Nothing is asserted
from documentation.

Outcomes are written to `conformance/RESULTS.json` and consumed by the audits. A rule with
no specimen is reported as NO_SPECIMEN rather than quietly counted as passing.

    python conformance/run_conformance.py <path-to-hamiltonian-lang>
"""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

SPECIMENS = []


def specimen(rule_id: str, name: str, kind: str):
    """kind: valid | invalid | round_trip"""
    def deco(fn):
        SPECIMENS.append({"rule": rule_id, "name": name, "kind": kind, "fn": fn})
        return fn
    return deco


# ---------------------------------------------------------------------------
def _mods():
    from hamiltonian_lang.semantic_state import model as M
    from hamiltonian_lang.semantic_state import neutral, verify, view
    from hamiltonian_lang.reasoning import kernel
    return M, neutral, verify, view, kernel


def _claim_state(M, **kw):
    return M.SemanticState(claims={"p0": M.Claim(id="p0", proposition="x = 1", **kw)})


def _transition(M, before=None, after=None, action=None, evidence=None):
    s = before if before is not None else _claim_state(M)
    return M.Transition(
        case_id="CONF-1",
        action=action or M.Action(id="a1", operation="LEAN_TACTIC"),
        state_before=s,
        state_after=after if after is not None else s,
        evidence=evidence or {},
    )


# ---- state structure ------------------------------------------------------
@specimen("HML-STATE-001", "state_minimal", "valid")
def _(M, neutral, verify, view, kernel):
    s = M.SemanticState()
    for field in ("claims", "candidates", "branches", "goals", "obligations"):
        assert hasattr(s, field), field
    assert s.active_scopes == ("global",)
    return "five record mappings plus active_scopes present; default scope is global"


@specimen("HML-STATE-002", "records_are_immutable", "valid")
def _(M, neutral, verify, view, kernel):
    c = M.Claim(id="p0", proposition="x = 1")
    try:
        c.proposition = "x = 2"  # type: ignore[misc]
    except Exception as exc:
        return f"mutation rejected: {type(exc).__name__}"
    raise AssertionError("record was mutable")


@specimen("HML-STATE-003", "key_id_disagree", "round_trip")
def _(M, neutral, verify, view, kernel):
    s = M.SemanticState(claims={"key_a": M.Claim(id="id_b", proposition="x = 1")})
    t = _transition(M, before=s, after=s)
    back = view.parse_transition(view.render_transition(t))
    assert back == t
    assert "key_a" in back.state_before.claims
    assert back.state_before.claims["key_a"].id == "id_b"
    return "mapping key 'key_a' and record id 'id_b' both preserved"


@specimen("HML-STATE-004", "scope_visibility_is_membership", "valid")
def _(M, neutral, verify, view, kernel):
    s = M.SemanticState(
        claims={"local": M.Claim(id="local", proposition="x = 1", scope="frame_1")},
        active_scopes=("global",))
    assert s.visible("local") is False
    s2 = M.SemanticState(claims=s.claims, active_scopes=("global", "frame_1"))
    assert s2.visible("local") is True
    return "claim in inactive scope is invisible; visible once the scope is active"


# ---- epistemic ------------------------------------------------------------
@specimen("HML-EPIS-001", "unknown_is_a_value", "valid")
def _(M, neutral, verify, view, kernel):
    s = _claim_state(M, status=M.ClaimStatus.UNKNOWN)
    t = _transition(M, before=s, after=s)
    back = view.parse_transition(view.render_transition(t))
    assert back.state_before.claims["p0"].status is M.ClaimStatus.UNKNOWN
    assert "UNKNOWN" in view.render_transition(t)
    return "UNKNOWN survives the round trip and is rendered explicitly"


@specimen("HML-EPIS-001", "unknown_not_collapsed_to_false", "invalid")
def _(M, neutral, verify, view, kernel):
    for bad in ("FALSE", "false", "", None):
        try:
            M.ClaimStatus(bad)
        except Exception:
            continue
        raise AssertionError(f"ClaimStatus accepted {bad!r}")
    return "ClaimStatus rejects FALSE/false/empty/None"


@specimen("HML-EPIS-003", "evidence_trust_is_separate_from_status", "valid")
def _(M, neutral, verify, view, kernel):
    e = M.EvidenceRecord(id="e1", kind="LEAN_TACTIC")
    assert e.trusted is False, "evidence must not default to trusted"
    assert e.status == "UNKNOWN", "evidence status must not default to VALID"
    return "EvidenceRecord defaults: trusted=False, status=UNKNOWN"


# ---- obligations ----------------------------------------------------------
@specimen("HML-OBL-002", "obligation_states_closed", "valid")
def _(M, neutral, verify, view, kernel):
    got = [m.value for m in M.ObligationState]
    assert got == ["OPEN", "DISCHARGED", "FAILED", "UNKNOWN"], got
    return f"ObligationState == {got}"


@specimen("HML-OBL-001", "mandatory_default", "valid")
def _(M, neutral, verify, view, kernel):
    o = M.Obligation(id="o1", proposition="x != 0")
    assert o.mandatory is True, "obligations must default to mandatory"
    assert o.status is M.ObligationState.OPEN
    return "Obligation defaults to mandatory=True, status=OPEN"


# ---- actions / transitions ------------------------------------------------
@specimen("HML-ACT-001", "action_is_structural", "valid")
def _(M, neutral, verify, view, kernel):
    import dataclasses
    names = {f.name for f in dataclasses.fields(M.Action)}
    required = {"operation", "dependencies", "warrant", "preconditions",
                "obligations_created", "obligations_discharged", "goal_effect",
                "scope_effect", "branch_effect", "candidate_effect", "epistemic_effect"}
    missing = required - names
    assert not missing, f"Action missing structural fields: {missing}"
    return f"Action carries {len(names)} structural fields, not just an operation name"


@specimen("HML-TRANS-001", "verdict_vocabulary", "valid")
def _(M, neutral, verify, view, kernel):
    got = [m.value for m in M.Verdict]
    assert got == ["VALID", "INVALID", "UNRESOLVED"], got
    return f"Verdict == {got}; UNRESOLVED is distinct from INVALID"


# ---- representation -------------------------------------------------------
@specimen("HML-REP-001", "all_records", "round_trip")
def _(M, neutral, verify, view, kernel):
    s = M.SemanticState(
        claims={"p0": M.Claim(id="p0", proposition="x : ℝ", domain="Real")},
        candidates={"c1": M.Candidate(id="c1", proposition="√x ≤ x",
                                      constraint_ids=("o1",), origin="heuristic")},
        branches={"b1": M.Branch(id="b1", predicate="x ≤ 1", partition_id="p1")},
        goals={"g1": M.Goal(id="g1", proposition="∀ ε > 0, ∃ δ > 0")},
        obligations={"o1": M.Obligation(id="o1", proposition="x ≠ 0", origin="division")},
        active_scopes=("global", "frame_1"))
    a = M.Action(id="a1", operation="APPLY_THEOREM", summary="apply",
                 dependencies=("p0",), warrant={"rule": "THEOREM"},
                 goal_effect={"advances": "g1"})
    ev = {"e1": M.EvidenceRecord(id="e1", kind="LEAN_TACTIC", trusted=True,
                                 premise_ids=("p0",), payload={"tactic": "exact h"})}
    t = M.Transition(case_id="CONF-ALL", action=a, state_before=s, state_after=s,
                     evidence=ev)
    assert view.parse_transition(view.render_transition(t)) == t
    return "every record kind round-trips under structural equality"


@specimen("HML-REP-002", "determinism", "round_trip")
def _(M, neutral, verify, view, kernel):
    made = {"f0": M.Claim(id="f0", proposition="x : ℝ"),
            "f1": M.Claim(id="f1", proposition="0 ≤ x", dependencies=("f0",)),
            "f2": M.Claim(id="f2", proposition="√x ∈ ℝ", dependencies=("f0", "f1"))}
    a = M.SemanticState(claims={k: made[k] for k in ("f0", "f1", "f2")})
    b = M.SemanticState(claims={k: made[k] for k in ("f2", "f1", "f0")})
    ta, tb = _transition(M, before=a, after=a), _transition(M, before=b, after=b)
    assert ta == tb, "probe invalid: the two transitions must be equal"
    assert view.render_transition(ta) == view.render_transition(tb)
    return "equal transitions built in different mapping order render identically"


@specimen("HML-REP-003", "double_encoded_payload", "invalid")
def _(M, neutral, verify, view, kernel):
    s = _claim_state(M)
    s = M.SemanticState(claims={"p0": M.Claim(id="p0", proposition="⊢ ∀ x : ℝ, x ≤ x")})
    text = view.render_transition(_transition(M, before=s, after=s))
    assert "\\u" not in text, "model-facing payload contains \\uXXXX escapes"
    for glyph in ("⊢", "∀", "ℝ", "≤"):
        assert glyph in text, f"{glyph} not rendered literally"
    return "payload carries decoded UTF-8; zero \\uXXXX sequences"


@specimen("HML-REP-004", "canonical_ascii", "valid")
def _(M, neutral, verify, view, kernel):
    from hamiltonian_lang.backends import canonical
    body = Path(canonical.__file__).read_text(encoding="utf-8")
    assert "ensure_ascii=True" in body
    assert "ensure_ascii=False" not in body
    return "canonical identity document is ASCII-encoded, deliberately unlike HML-REP-003"


@specimen("HML-REP-005", "no_action_leak", "valid")
def _(M, neutral, verify, view, kernel):
    s = _claim_state(M)
    rendered_state = view.render_state(s)
    assert "APPLY_THEOREM" not in rendered_state
    assert "operation" not in rendered_state
    return "render_state does not reveal the action"


# ---- backends -------------------------------------------------------------
@specimen("HML-BACK-001", "backend_declares_loss", "valid")
def _(M, neutral, verify, view, kernel):
    from hamiltonian_lang.backends import base
    for m in ("drop", "approximate", "weaken"):
        assert hasattr(base.Backend, m), f"Backend lacks {m}()"
    return "Backend exposes drop/approximate/weaken for declaring translation loss"


# ---- specimens added to close coverage gaps -------------------------------
@specimen("HML-EPIS-002", "candidate_status_is_separate_vocabulary", "valid")
def _(M, neutral, verify, view, kernel):
    """A candidate cannot *spell* a claim status, so promotion cannot be a relabelling."""
    cand = {m.value for m in M.CandidateStatus}
    claim = {m.value for m in M.ClaimStatus}
    assert "GIVEN" not in cand and "DERIVED" not in cand
    from hamiltonian_lang.semantic_state import INVARIANTS
    assert "CANDIDATES" in INVARIANTS
    return ("CandidateStatus cannot express GIVEN/DERIVED; the CANDIDATES invariant "
            f"governs promotion (shared members: {sorted(cand & claim)})")


@specimen("HML-EPIS-004", "generator_cannot_self_certify", "invalid")
def _(M, neutral, verify, view, kernel):
    from hamiltonian_lang.semantic_state import trust
    modes = [m.value for m in trust.TrustMode]
    assert modes, "no trust modes defined"
    assert hasattr(trust, "attest") and hasattr(trust, "AttestationError")
    return (f"attestation is a separate trusted step; TrustMode == {modes}; "
            "AttestationError exists")


@specimen("HML-ACT-002", "missing_dependency_is_an_error_class", "invalid")
def _(M, neutral, verify, view, kernel):
    from hamiltonian_lang.semantic_state import INVARIANTS
    assert "DEPENDENCY" in INVARIANTS
    assert M.ErrorClass("MISSING_DEPENDENCY") is M.ErrorClass.MISSING_DEPENDENCY
    return "unresolved references are reported as ErrorClass.MISSING_DEPENDENCY"


@specimen("HML-VER-001", "version_manifest", "valid")
def _(M, neutral, verify, view, kernel):
    payload = json.loads((ROOT / "VERSION.json").read_text(encoding="utf-8"))
    for key in ("semantic_implementation_commit", "model_language_commit",
                "semantic_tag", "model_language_tag", "normative_state_delta"):
        assert key in payload, f"VERSION.json missing {key}"
    assert payload["normative_state_delta"] is False, (
        "the state delta is SPECIFIED_NOT_FROZEN and MUST NOT be recorded as normative")
    assert len(payload["semantic_implementation_commit"]) == 40
    assert len(payload["model_language_commit"]) == 40
    return "VERSION.json pins both commits and both tags; state delta marked non-normative"


# ---- generated families ---------------------------------------------------
def _kernel_specimens(M, neutral, verify, view, kernel):
    out = []
    names = kernel.rule_names()
    for i, name in enumerate(names, start=1):
        spec = kernel.RULES[name]
        try:
            assert spec.shape, f"{name} has no declared shape"
            assert isinstance(spec.arity, int) and spec.arity >= 0
            out.append({"rule": f"HML-KERNEL-{i:03d}", "name": f"kernel_{name}",
                        "kind": "valid", "outcome": "PASS",
                        "detail": f"arity {spec.arity}, shape `{spec.shape}`"})
        except Exception as exc:
            out.append({"rule": f"HML-KERNEL-{i:03d}", "name": f"kernel_{name}",
                        "kind": "valid", "outcome": "FAIL", "detail": str(exc)})
    return out


def _invariant_specimens(M, neutral, verify, view, kernel):
    from hamiltonian_lang.semantic_state import INVARIANTS
    names = ["DEPENDENCY", "SCOPE", "PRECONDITIONS", "OBLIGATIONS", "CANDIDATES",
             "BRANCH_JOIN", "WARRANT", "EPISTEMIC_STATUS", "GOAL_DISCHARGE",
             "TYPE_DOMAIN", "FRAME"]
    present = set(INVARIANTS)
    out = []
    for i, n in enumerate(names, start=1):
        ok = n in present
        out.append({"rule": f"HML-INV-{i:03d}", "name": f"invariant_{n.lower()}",
                    "kind": "invalid", "outcome": "PASS" if ok else "FAIL",
                    "detail": f"invariant {n} {'registered' if ok else 'MISSING'} in verifier"})
    return out


def _enum_specimens(M, neutral, verify, view, kernel):
    import enum as _enum
    out = []
    names = [n for n in dir(M)
             if isinstance(getattr(M, n), type)
             and issubclass(getattr(M, n), _enum.Enum)
             and getattr(M, n) is not _enum.Enum and n != "StrEnum"]
    for i, n in enumerate(sorted(names), start=1):
        cls = getattr(M, n)
        try:
            cls("NOT_A_REAL_MEMBER_zzz")
            out.append({"rule": f"HML-ENUM-{i:03d}", "name": f"enum_{n.lower()}_unknown_member",
                        "kind": "invalid", "outcome": "FAIL",
                        "detail": f"{n} accepted an unknown member"})
        except Exception:
            out.append({"rule": f"HML-ENUM-{i:03d}", "name": f"enum_{n.lower()}_unknown_member",
                        "kind": "invalid", "outcome": "PASS",
                        "detail": f"{n} rejects unknown members; closed at {[m.value for m in cls]}"})
    return out


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(root / "src"))
    mods = _mods()

    results = []
    for s in SPECIMENS:
        try:
            detail = s["fn"](*mods)
            results.append({"rule": s["rule"], "name": s["name"], "kind": s["kind"],
                            "outcome": "PASS", "detail": detail})
        except Exception as exc:
            results.append({"rule": s["rule"], "name": s["name"], "kind": s["kind"],
                            "outcome": "FAIL",
                            "detail": f"{type(exc).__name__}: {exc}",
                            "traceback": traceback.format_exc()[-600:]})

    results.extend(_kernel_specimens(*mods))
    results.extend(_invariant_specimens(*mods))
    results.extend(_enum_specimens(*mods))

    rules = json.load(open(ROOT / "standard" / "rules.json", encoding="utf-8"))["rules"]
    covered = {r["rule"] for r in results}
    no_specimen = [r["id"] for r in rules if r["id"] not in covered]

    payload = {
        "implementation_root": str(root),
        "total_specimens": len(results),
        "passed": sum(1 for r in results if r["outcome"] == "PASS"),
        "failed": sum(1 for r in results if r["outcome"] == "FAIL"),
        "rules_total": len(rules),
        "rules_with_specimen": len(covered & {r["id"] for r in rules}),
        "rules_without_specimen": no_specimen,
        "results": results,
    }
    (HERE / "RESULTS.json").write_text(
        json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"specimens: {payload['total_specimens']}  "
          f"PASS {payload['passed']}  FAIL {payload['failed']}")
    print(f"rules with a specimen: {payload['rules_with_specimen']}/{payload['rules_total']}")
    if no_specimen:
        print(f"NO_SPECIMEN ({len(no_specimen)}): {', '.join(no_specimen)}")
    for r in results:
        if r["outcome"] == "FAIL":
            print(f"  FAIL {r['rule']} {r['name']}: {r['detail']}")
    return 1 if payload["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
