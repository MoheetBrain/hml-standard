# Dependencies

*HML Standard 1.0 — 2026-08-27*

The citation graph between records.

[NORMATIVE] Dependencies are the citation graph. Every reference an action or record makes
MUST resolve in the state it applies to (HML-ACT-002), enforced by the DEPENDENCY invariant
(HML-INV-001) and reported as `ErrorClass.MISSING_DEPENDENCY`.

The model-facing serialization emits records in dependency-topological order so a citation
appears after what it cites.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
