# Verification

*HML Standard 1.0 — 2026-08-27*

The 20-rule kernel, the trusted boundary and certificates.

## Normative rules (20)

#### HML-KERNEL-001 — add_both_sides  `[NORMATIVE]`

The kernel rule `add_both_sides` MUST have arity 1 and the shape `a = b  |-  a + k = b + k`. Adding the same term to both sides preserves equality unconditionally.

Shape: `a = b  |-  a + k = b + k`  ·  arity 1  ·  params `['by']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['add_both_sides']`
  ·  Conformance: `conformance/valid/kernel_add_both_sides`

#### HML-KERNEL-002 — add_inequality  `[NORMATIVE]`

The kernel rule `add_inequality` MUST have arity 1 and the shape `a < b  |-  a + k < b + k`. Translation preserves order for any k.

Shape: `a < b  |-  a + k < b + k`  ·  arity 1  ·  params `['by']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['add_inequality']`
  ·  Conformance: `conformance/valid/kernel_add_inequality`

#### HML-KERNEL-003 — and_elim_left  `[NORMATIVE]`

The kernel rule `and_elim_left` MUST have arity 1 and the shape `P and Q  |-  P`. Conjunction elimination, left.

Shape: `P and Q  |-  P`  ·  arity 1

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['and_elim_left']`
  ·  Conformance: `conformance/valid/kernel_and_elim_left`

#### HML-KERNEL-004 — and_elim_right  `[NORMATIVE]`

The kernel rule `and_elim_right` MUST have arity 1 and the shape `P and Q  |-  Q`. Conjunction elimination, right.

Shape: `P and Q  |-  Q`  ·  arity 1

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['and_elim_right']`
  ·  Conformance: `conformance/valid/kernel_and_elim_right`

#### HML-KERNEL-005 — and_intro  `[NORMATIVE]`

The kernel rule `and_intro` MUST have arity 2 and the shape `P, Q  |-  P and Q`. Conjunction introduction.

Shape: `P, Q  |-  P and Q`  ·  arity 2

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['and_intro']`
  ·  Conformance: `conformance/valid/kernel_and_intro`

#### HML-KERNEL-006 — congruence  `[NORMATIVE]`

The kernel rule `congruence` MUST have arity 1 and the shape `a = b  |-  f(a) = f(b)`. Functions respect equality. f must be a named unary function.

Shape: `a = b  |-  f(a) = f(b)`  ·  arity 1  ·  params `['fn']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['congruence']`
  ·  Conformance: `conformance/valid/kernel_congruence`

#### HML-KERNEL-007 — divide_both_sides  `[NORMATIVE]`

The kernel rule `divide_both_sides` MUST have arity 1 and the shape `a = b  |-  a / k = b / k   [requires k != 0]`. Dividing both sides is sound only for a non-zero divisor. The obligation comes from the term, not from this spec -- see reasoning/partiality.py.

Shape: `a = b  |-  a / k = b / k   [requires k != 0]`  ·  arity 1  ·  params `['by']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['divide_both_sides']`
  ·  Conformance: `conformance/valid/kernel_divide_both_sides`

#### HML-KERNEL-008 — exists_intro  `[NORMATIVE]`

The kernel rule `exists_intro` MUST have arity 1 and the shape `phi(a)  |-  exists a : D . phi(a)   [a is a typed witness]`. Existential introduction from a checked witness fact. The witness is a resolved module-level variable and the binder uses its exact declared domain; this rule does not assert uniqueness.

Shape: `phi(a)  |-  exists a : D . phi(a)   [a is a typed witness]`  ·  arity 1  ·  params `['var']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['exists_intro']`
  ·  Conformance: `conformance/valid/kernel_exists_intro`

#### HML-KERNEL-009 — forall_elim  `[NORMATIVE]`

The kernel rule `forall_elim` MUST have arity 1 and the shape `forall x : D . phi(x)  |-  phi[t/x]   [requires t : D]`. It MUST enforce the side conditions ['instantiation_domain']. Universal instantiation. Substitution is capture-avoiding, and a term mentioning a bound name is refused rather than substituted. The instantiation term must inhabit the binder's declared domain.

Shape: `forall x : D . phi(x)  |-  phi[t/x]   [requires t : D]`  ·  arity 1  ·  params `['at']`
Side conditions: `['instantiation_domain']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['forall_elim']`
  ·  Conformance: `conformance/valid/kernel_forall_elim`

#### HML-KERNEL-010 — forall_intro  `[NORMATIVE]`

The kernel rule `forall_intro` MUST have arity 1 and the shape `phi(a)  |-  forall a : D . phi(a)   [a arbitrary]`. It MUST enforce the side conditions ['eigenvariable']. Universal introduction. The variable must be ARBITRARY: it may not occur free in any assumption in scope, or the proof was about that particular value and generalising it is unsound. Proving phi for many sample values is not this rule and never becomes it.

Shape: `phi(a)  |-  forall a : D . phi(a)   [a arbitrary]`  ·  arity 1  ·  params `['var']`
Side conditions: `['eigenvariable']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['forall_intro']`
  ·  Conformance: `conformance/valid/kernel_forall_intro`

#### HML-KERNEL-011 — modus_ponens  `[NORMATIVE]`

The kernel rule `modus_ponens` MUST have arity 2 and the shape `P, P implies Q  |-  Q`. The antecedent must match the implication's left side exactly.

Shape: `P, P implies Q  |-  Q`  ·  arity 2

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['modus_ponens']`
  ·  Conformance: `conformance/valid/kernel_modus_ponens`

#### HML-KERNEL-012 — modus_tollens  `[NORMATIVE]`

The kernel rule `modus_tollens` MUST have arity 2 and the shape `not Q, P implies Q  |-  not P`. Denying the consequent.

Shape: `not Q, P implies Q  |-  not P`  ·  arity 2

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['modus_tollens']`
  ·  Conformance: `conformance/valid/kernel_modus_tollens`

#### HML-KERNEL-013 — multiply_both_sides  `[NORMATIVE]`

The kernel rule `multiply_both_sides` MUST have arity 1 and the shape `a = b  |-  a * k = b * k`. Multiplying both sides preserves equality for any k, including zero.

Shape: `a = b  |-  a * k = b * k`  ·  arity 1  ·  params `['by']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['multiply_both_sides']`
  ·  Conformance: `conformance/valid/kernel_multiply_both_sides`

#### HML-KERNEL-014 — multiply_inequality  `[NORMATIVE]`

The kernel rule `multiply_inequality` MUST have arity 1 and the shape `a < b  |-  a * k < b * k   [requires k > 0]`. It MUST emit the obligations ["ObligationSpec(build=<function _gt_zero at 0x107dbfc40>, reason='order_preserving_multiplier', mandatory=True)"]. Scaling preserves the direction of an inequality only for a positive multiplier; the obligation is mandatory.

Shape: `a < b  |-  a * k < b * k   [requires k > 0]`  ·  arity 1  ·  params `['by']`
Obligations emitted: `["ObligationSpec(build=<function _gt_zero at 0x107dbfc40>, reason='order_preserving_multiplier', mandatory=True)"]`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['multiply_inequality']`
  ·  Conformance: `conformance/valid/kernel_multiply_inequality`

#### HML-KERNEL-015 — reflexivity  `[NORMATIVE]`

The kernel rule `reflexivity` MUST have arity 0 and the shape `|- t = t`. Equality is reflexive for every well-typed, defined term. Partial terms retain their ordinary term-level definedness obligations.

Shape: `|- t = t`  ·  arity 0  ·  params `['term']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['reflexivity']`
  ·  Conformance: `conformance/valid/kernel_reflexivity`

#### HML-KERNEL-016 — substitute  `[NORMATIVE]`

The kernel rule `substitute` MUST have arity 2 and the shape `a = b, P  |-  P[a := b]`. Substitution of equals. Does not descend into quantifier bodies, so a step that would require capture-avoiding substitution is REJECTED rather than performed unsoundly.

Shape: `a = b, P  |-  P[a := b]`  ·  arity 2

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['substitute']`
  ·  Conformance: `conformance/valid/kernel_substitute`

#### HML-KERNEL-017 — subtract_both_sides  `[NORMATIVE]`

The kernel rule `subtract_both_sides` MUST have arity 1 and the shape `a = b  |-  a - k = b - k`. Subtracting the same term from both sides preserves equality.

Shape: `a = b  |-  a - k = b - k`  ·  arity 1  ·  params `['by']`

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['subtract_both_sides']`
  ·  Conformance: `conformance/valid/kernel_subtract_both_sides`

#### HML-KERNEL-018 — symmetry  `[NORMATIVE]`

The kernel rule `symmetry` MUST have arity 1 and the shape `a = b  |-  b = a`. Equality is symmetric.

Shape: `a = b  |-  b = a`  ·  arity 1

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['symmetry']`
  ·  Conformance: `conformance/valid/kernel_symmetry`

#### HML-KERNEL-019 — transitivity  `[NORMATIVE]`

The kernel rule `transitivity` MUST have arity 2 and the shape `a = b, b = c  |-  a = c`. Equality is transitive. The shared middle term must match exactly.

Shape: `a = b, b = c  |-  a = c`  ·  arity 2

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['transitivity']`
  ·  Conformance: `conformance/valid/kernel_transitivity`

#### HML-KERNEL-020 — weaken_inequality  `[NORMATIVE]`

The kernel rule `weaken_inequality` MUST have arity 1 and the shape `a < b  |-  a <= b`. Strict to non-strict. One-directional by construction: there is no rule in this kernel that strengthens <= to <, because none is sound.

Shape: `a < b  |-  a <= b`  ·  arity 1

Implementation: `src/hamiltonian_lang/reasoning/kernel.py` · `RULES['weaken_inequality']`
  ·  Conformance: `conformance/valid/kernel_weaken_inequality`
