# Errors and failure

*HML Standard 1.0 — 2026-08-27*

ErrorClass, Finding, Verdict and the refusal discipline.

[NORMATIVE] Failure is a first-class outcome. A verifier returns a `Verdict` of VALID,
INVALID or **UNRESOLVED**, and UNRESOLVED MUST NOT be reported as INVALID (HML-TRANS-001).

Violations are reported as findings carrying an `ErrorClass` drawn from a closed vocabulary
of ten values. A reader that cannot represent an object MUST refuse it rather than return a
partial result: a half-parsed state that looks plausible is worse than no state, because
nothing downstream can tell the difference.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
