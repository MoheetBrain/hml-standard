# Type system

*HML Standard 1.0 — 2026-08-27*

The typed layer: scalar, structured, function, predicate, probabilistic and concept types.

[NORMATIVE] Every object carries a type before canonical identity is
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
transition and reports `ErrorClass.TYPE_DOMAIN_VIOLATION`.

## Normative rules

No rules are registered against this section; the requirements above are enforced through the rules listed in the sections they name.
