# Evidence and warrants

*HML Standard 1.0 — 2026-08-27*

What licenses a transition and what evidence attests to it.

[NORMATIVE] A **warrant** is what licenses an action; **evidence** is what attests to it.
They are separate fields and MUST NOT be conflated.

`EvidenceRecord.trusted` defaults to `False` and `status` defaults to `UNKNOWN`. Untrusted
evidence MUST NOT discharge a mandatory obligation (HML-EPIS-003). A generator MUST NOT
self-certify (HML-EPIS-004): attestation is a separate step in
`semantic_state/trust.py`.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
