# Semantic atlas — mathematics into HML

*HML Standard 1.0 — 2026-08-27*

**The question is not whether HML proves a concept.** Its kernel has 20 rules and proves almost nothing by itself. The question is whether HML can **losslessly carry the reasoning state** for that concept.

**110 concepts** mapped across **22 domains**.

## Result

| Verdict | Count |
|---|---:|
| **LIBRARY_GAP** | 61 |
| **NO_GAP** | 41 |
| **BACKEND_GAP** | 7 |
| **UNSUPPORTED** | 1 |

### 0 CORE_GAPs

No mapped concept was found whose reasoning state the frozen semantic core cannot carry. The 61 `LIBRARY_GAP` entries are the honest shape of the remaining work, and it is **library work, not language work**. A `LIBRARY_GAP` MUST NOT be used to justify a semantic unfreeze.

This is a claim about representational adequacy at HML 1.0 over the concepts listed, reviewed against the frozen implementation. It is not a proof that no `CORE_GAP` exists anywhere in mathematics.

## Domains

| Domain | Concepts | NO_GAP | LIBRARY_GAP | BACKEND_GAP |
|---|---:|---:|---:|---:|
| [Logic](atlas/logic.md) | 12 | 9 | 3 | 0 |
| [Set Theory](atlas/set_theory.md) | 7 | 2 | 5 | 0 |
| [Algebra](atlas/algebra.md) | 6 | 3 | 3 | 0 |
| [Linear Algebra](atlas/linear_algebra.md) | 7 | 4 | 2 | 1 |
| [Number Theory](atlas/number_theory.md) | 5 | 1 | 4 | 0 |
| [Combinatorics](atlas/combinatorics.md) | 4 | 1 | 3 | 0 |
| [Graph Theory](atlas/graph_theory.md) | 4 | 0 | 3 | 1 |
| [Calculus](atlas/calculus.md) | 5 | 2 | 3 | 0 |
| [Real Analysis](atlas/real_analysis.md) | 5 | 2 | 3 | 0 |
| [Complex Analysis](atlas/complex_analysis.md) | 3 | 1 | 2 | 0 |
| [Measure Theory](atlas/measure_theory.md) | 5 | 0 | 5 | 0 |
| [Probability](atlas/probability.md) | 8 | 7 | 1 | 0 |
| [Statistics](atlas/statistics.md) | 5 | 1 | 3 | 1 |
| [Stochastic Processes](atlas/stochastic_processes.md) | 3 | 0 | 3 | 0 |
| [Geometry](atlas/geometry.md) | 3 | 0 | 3 | 0 |
| [Topology](atlas/topology.md) | 5 | 0 | 5 | 0 |
| [Functional Analysis](atlas/functional_analysis.md) | 4 | 0 | 4 | 0 |
| [Differential Equations](atlas/differential_equations.md) | 3 | 1 | 1 | 1 |
| [Optimization](atlas/optimization.md) | 4 | 3 | 0 | 1 |
| [Numerical Analysis](atlas/numerical_analysis.md) | 4 | 2 | 1 | 1 |
| [Category Theory](atlas/category_theory.md) | 4 | 0 | 3 | 0 |
| [Constructive Mathematics](atlas/constructive_mathematics.md) | 4 | 2 | 1 | 1 |

## How to use it when something fails

The atlas is the first step of the diagnostic chain in `ARCHITECTURE.md`. Before concluding that a model failure is a language failure, find the concept here. If it says `LIBRARY_GAP`, the language is not the problem.
