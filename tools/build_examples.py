"""Render the worked examples from the frozen implementation.

Hand-written examples drift. These are produced by the actual renderer at the pinned
commit, so an example that stops being valid stops being generated.

    python tools/build_examples.py <path-to-hamiltonian-lang>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    impl = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(impl / "src"))
    from hamiltonian_lang.semantic_state import model as M
    from hamiltonian_lang.semantic_state.view import parse_transition, render_transition

    def T(case, state, action, evidence=None, after=None):
        return M.Transition(case_id=case, action=action, state_before=state,
                            state_after=after if after is not None else state,
                            evidence=evidence or {})

    examples: list[tuple[str, str, str, M.Transition]] = []

    # minimal
    examples.append((
        "minimal", "single_claim",
        "The smallest well-formed transition: one GIVEN claim and one action.",
        T("EX-MIN-1",
          M.SemanticState(claims={"p0": M.Claim(id="p0", proposition="x = 1")}),
          M.Action(id="a1", operation="LEAN_TACTIC", dependencies=("p0",),
                   warrant={"rule": "LEAN_TACTIC"}))))

    examples.append((
        "minimal", "unknown_is_explicit",
        "UNKNOWN is a value. It is rendered, round-trips, and is never a missing field.",
        T("EX-MIN-2",
          M.SemanticState(claims={"p0": M.Claim(id="p0", proposition="P x",
                                                status=M.ClaimStatus.UNKNOWN)}),
          M.Action(id="a1", operation="INSPECT"))))

    # algebra
    examples.append((
        "algebra", "divide_creates_obligation",
        "Dividing both sides is a kernel rule that emits a nonzero obligation. Partiality "
        "is discharged through proof debt, never assumed.",
        T("EX-ALG-1",
          M.SemanticState(
              claims={"h1": M.Claim(id="h1", proposition="a * x = b"),
                      "h2": M.Claim(id="h2", proposition="a ≠ 0")},
              obligations={"o1": M.Obligation(id="o1", proposition="a ≠ 0",
                                              origin="divide_both_sides",
                                              dependencies=("h2",))}),
          M.Action(id="a1", operation="KERNEL_RULE", summary="divide_both_sides",
                   dependencies=("h1",), output_id="d1",
                   warrant={"rule": "divide_both_sides"},
                   obligations_created=({"id": "o1", "proposition": "a ≠ 0"},)))))

    # calculus
    examples.append((
        "calculus", "goal_and_obligation",
        "An open goal alongside outstanding proof debt. Both are visible; neither is "
        "implied by the other.",
        T("EX-CALC-1",
          M.SemanticState(
              claims={"h1": M.Claim(id="h1", proposition="f : ℝ → ℝ"),
                      "h2": M.Claim(id="h2", proposition="f is differentiable at a",
                                    status=M.ClaimStatus.ASSUMED)},
              goals={"g1": M.Goal(id="g1", proposition="f is continuous at a")},
              obligations={"o1": M.Obligation(id="o1", proposition="a ∈ dom f")}),
          M.Action(id="a1", operation="APPLY_THEOREM",
                   dependencies=("h2",), warrant={"rule": "THEOREM",
                                                  "name": "differentiable_implies_continuous"},
                   goal_effect={"advances": "g1"}))))

    # probability
    examples.append((
        "probability", "conditional_probability_obligation",
        "P(A|B) carries a P(B) > 0 obligation. Probability is its own quantity type and is "
        "not PositiveReal.",
        T("EX-PROB-1",
          M.SemanticState(
              claims={"h1": M.Claim(id="h1", proposition="A, B : Event", domain="Event"),
                      "h2": M.Claim(id="h2", proposition="P(B) > 0")},
              obligations={"o1": M.Obligation(id="o1", proposition="P(B) > 0",
                                              origin="conditional_probability",
                                              dependencies=("h2",))}),
          M.Action(id="a1", operation="DEFINE", summary="P(A|B) = P(A ∩ B) / P(B)",
                   dependencies=("h1", "h2"), output_id="d1",
                   typing={"result": "Probability"}))))

    # reasoning
    examples.append((
        "reasoning", "candidate_is_not_a_fact",
        "A candidate sits beside the claims and cannot be promoted by relabelling: "
        "CandidateStatus cannot express GIVEN or DERIVED.",
        T("EX-REA-1",
          M.SemanticState(
              claims={"h1": M.Claim(id="h1", proposition="x > 0")},
              candidates={"c1": M.Candidate(id="c1", proposition="√x < x",
                                            status=M.CandidateStatus.PROPOSED,
                                            origin="heuristic", dependencies=("h1",))},
              goals={"g1": M.Goal(id="g1", proposition="√x < x")}),
          M.Action(id="a1", operation="PROPOSE", output_id="c1",
                   candidate_effect={"proposes": "c1"}))))

    examples.append((
        "reasoning", "branch_local_scope",
        "A branch-local claim lives in its own scope. It is invisible until that scope is "
        "active, and cannot escape without a join.",
        T("EX-REA-2",
          M.SemanticState(
              claims={"h1": M.Claim(id="h1", proposition="x : ℝ"),
                      "b_fact": M.Claim(id="b_fact", proposition="x ≤ 1",
                                        scope="branch_1",
                                        status=M.ClaimStatus.ASSUMED)},
              branches={"b1": M.Branch(id="b1", predicate="x ≤ 1", scope="branch_1",
                                       partition_id="split_1")},
              active_scopes=("global", "branch_1")),
          M.Action(id="a1", operation="OPEN_BRANCH",
                   scope_effect={"opens": "branch_1"},
                   branch_effect={"opens": "b1"}))))

    index = ["# Examples", "",
             "*HML Standard 1.0 — rendered by the frozen implementation at the pinned "
             "commit, not written by hand.*", ""]
    for folder, name, note, t in examples:
        text = render_transition(t)
        assert parse_transition(text) == t, f"{name} does not round-trip"
        d = ROOT / "examples" / folder
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{name}.hml").write_text(text + "\n", encoding="utf-8")
        (d / f"{name}.md").write_text(
            f"# {name}\n\n{note}\n\nRound-trips: `parse(render(t)) == t`.\n\n"
            f"```\n{text}\n```\n", encoding="utf-8")
        index.append(f"- [`{folder}/{name}`]({folder}/{name}.md) — {note}")
    (ROOT / "examples" / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"wrote {len(examples)} examples, all round-tripping")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
