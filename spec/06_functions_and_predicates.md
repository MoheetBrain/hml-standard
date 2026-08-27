# Functions and predicates

*HML Standard 1.0 — 2026-08-27*

First-class functions and predicates, arity and domain enforcement.

[NORMATIVE] Functions and predicates are first class. A `Predicate` value may be applied,
passed and quantified over.

Arity and domain are enforced: an application with the wrong arity, or an argument outside
the declared domain, MUST fail closed rather than produce `Unknown`. The final semantic
closure audit repaired exactly this -- first-class `Function` and `Predicate` application
previously bypassed arity and domain checks.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
