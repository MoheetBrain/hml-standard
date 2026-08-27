"""Source of truth for the mathematics -> HML semantic atlas.

The central question every entry answers is **not** "can HML prove this?" -- HML proves
almost nothing itself; the kernel has 20 rules and everything else is library, backend or
policy. The question is:

    CAN HML LOSSLESSLY REPRESENT THE MATHEMATICAL REASONING STATE FOR THIS CONCEPT?

So a concept whose theorems live in a library is NOT a CORE_GAP. It is a LIBRARY_GAP at
most, and usually NO_GAP, because carrying the state is what the core is for.

Verdict vocabulary:
    NO_GAP              representable and manipulable with frozen machinery
    LIBRARY_GAP         representable; the reasoning needs a library that does not exist yet
    BACKEND_GAP         representable; checking needs an external backend not wired up
    REPRESENTATION_GAP  the model-facing surface cannot carry it losslessly
    CORE_GAP            the semantic core genuinely cannot represent the state
    POLICY_GAP          representable; what is missing is search/strategy, not language
    UNSUPPORTED         out of scope for HML 1.0

CARRY   -- can the state be represented losslessly?
MANIPULATE -- can an action change it within frozen transition semantics?
VERIFY  -- CORE / LIBRARY / BACKEND / UNSUPPORTED
"""

C = "CORE"; L = "LIBRARY"; B = "BACKEND"; U = "UNSUPPORTED"

# (concept, definition/role, hml_representation, carry, manipulate, verify, verdict, note)
ATLAS = {
"logic": [
 ("variable", "a name bound in a context", "binder in a Claim proposition; identity by binding ID, not spelling", 1,1,C,"NO_GAP",""),
 ("constant", "a fixed term", "term inside a proposition; ScalarType or a declared Object", 1,1,C,"NO_GAP",""),
 ("equality", "a = b", "proposition; kernel rules reflexivity, symmetry, transitivity, substitute, congruence", 1,1,C,"NO_GAP","five of the 20 kernel rules are equality rules"),
 ("implication", "P => Q", "proposition; kernel modus_ponens, modus_tollens", 1,1,C,"NO_GAP",""),
 ("conjunction", "P and Q", "proposition; kernel and_intro, and_elim_left, and_elim_right", 1,1,C,"NO_GAP",""),
 ("disjunction", "P or Q", "proposition; case analysis via Branch with a partition_id", 1,1,L,"LIBRARY_GAP","branches carry the case split; no disjunction elimination rule in the kernel"),
 ("negation", "not P", "proposition; ClaimStatus.REFUTED records a refuted claim", 1,1,L,"LIBRARY_GAP",""),
 ("universal quantifier", "forall x, P x", "proposition; kernel forall_intro, forall_elim with freshness side conditions", 1,1,C,"NO_GAP",""),
 ("existential quantifier", "exists x, P x", "proposition; kernel exists_intro", 1,1,C,"NO_GAP","exists_elim (witness extraction) is not a kernel rule"),
 ("existential witness", "the term proving exists", "the instantiating term recorded in the action's args", 1,1,C,"NO_GAP",""),
 ("induction", "proof by induction", "a Goal plus Branches for base and step, with Obligations", 1,1,L,"LIBRARY_GAP","the schema is representable; the induction principle is library-level"),
 ("UNKNOWN / unresolved", "truth value not determined", "ClaimStatus.UNKNOWN, Verdict.UNRESOLVED, ObligationState.UNKNOWN", 1,1,C,"NO_GAP","first-class, never collapsed to FALSE"),
],
"set_theory": [
 ("set", "a collection", "SetType", 1,1,C,"NO_GAP",""),
 ("membership", "x in S", "proposition over SetType", 1,1,L,"LIBRARY_GAP",""),
 ("subset", "A subset B", "proposition", 1,1,L,"LIBRARY_GAP",""),
 ("union / intersection", "set operations", "term-level operations over SetType", 1,1,L,"LIBRARY_GAP",""),
 ("power set", "set of subsets", "SetType over SetType", 1,0,L,"LIBRARY_GAP",""),
 ("indexed family", "family over an index set", "SymbolicExtent with a resolved finite shape", 1,1,C,"NO_GAP","finite index bounds carry term-level obligations"),
 ("cardinality", "size of a set", "QuantityType; finite cardinality via SymbolicExtent", 1,0,L,"LIBRARY_GAP","infinite cardinal arithmetic is UNSUPPORTED in 1.0"),
],
"algebra": [
 ("group", "set with associative op, identity, inverses", "ConceptType with declared axioms as Claims", 1,1,L,"LIBRARY_GAP","the closure audit explicitly declined to pretend Group into the kernel"),
 ("ring", "two operations", "ConceptType", 1,1,L,"LIBRARY_GAP",""),
 ("field", "ring with division", "ConceptType; division introduces a nonzero Obligation", 1,1,L,"LIBRARY_GAP","partiality machinery carries the x != 0 obligation"),
 ("polynomial", "formal sum", "term; libraries/algebra.py", 1,1,L,"NO_GAP",""),
 ("equation solving", "isolate a variable", "kernel add/subtract/multiply/divide_both_sides", 1,1,C,"NO_GAP","divide_both_sides emits a nonzero obligation"),
 ("inequality", "a <= b", "proposition; kernel weaken_inequality, add_inequality, multiply_inequality", 1,1,C,"NO_GAP","multiply_inequality carries a sign side condition"),
],
"linear_algebra": [
 ("vector", "element of a vector space", "VectorType with Dimension", 1,1,C,"NO_GAP",""),
 ("matrix", "linear map in coordinates", "MatrixType with Dimension", 1,1,C,"NO_GAP",""),
 ("tensor", "multilinear object", "TensorType", 1,1,C,"NO_GAP",""),
 ("vector space", "the ambient structure", "ConceptType", 1,1,L,"LIBRARY_GAP",""),
 ("linear map", "structure-preserving map", "FunctionType between VectorTypes", 1,1,L,"LIBRARY_GAP",""),
 ("matrix product", "composition", "term; dimension compatibility is a type/domain check", 1,1,C,"NO_GAP","TYPE_DOMAIN invariant rejects incompatible shapes"),
 ("eigenvalue", "scalar with an eigenvector", "Claim over MatrixType and ScalarType", 1,0,B,"BACKEND_GAP","numeric spectra need a backend"),
],
"number_theory": [
 ("integer", "element of Z", "ScalarType Integer", 1,1,C,"NO_GAP",""),
 ("divisibility", "a divides b", "proposition", 1,1,L,"LIBRARY_GAP",""),
 ("prime", "irreducible integer", "Predicate over Integer", 1,1,L,"LIBRARY_GAP",""),
 ("modular arithmetic", "congruence", "proposition; term-level mod", 1,1,L,"LIBRARY_GAP",""),
 ("gcd", "greatest common divisor", "FunctionType Integer x Integer -> Integer", 1,1,L,"LIBRARY_GAP",""),
],
"combinatorics": [
 ("finite sequence", "ordered tuple", "ProductType or SymbolicExtent-indexed family", 1,1,C,"NO_GAP",""),
 ("binomial coefficient", "n choose k", "FunctionType with a k <= n obligation", 1,1,L,"LIBRARY_GAP","the bound is a term-level obligation"),
 ("permutation", "bijection of a finite set", "FunctionType with a bijectivity Claim", 1,1,L,"LIBRARY_GAP",""),
 ("counting argument", "bijective/double counting", "Goal plus Claims; no dedicated machinery", 1,1,L,"LIBRARY_GAP",""),
],
"graph_theory": [
 ("graph", "vertices and edges", "ConceptType over SetType", 1,1,L,"LIBRARY_GAP",""),
 ("path", "sequence of adjacent vertices", "SymbolicExtent-indexed family", 1,1,L,"LIBRARY_GAP",""),
 ("connectivity", "existence of paths", "Predicate; existential proposition", 1,1,L,"LIBRARY_GAP",""),
 ("graph algorithm result", "e.g. shortest path", "Claim with BACKEND_CERTIFIED evidence", 1,0,B,"BACKEND_GAP",""),
],
"calculus": [
 ("limit", "lim f(x) as x -> a", "proposition; epsilon-delta as nested quantifiers", 1,1,L,"LIBRARY_GAP",""),
 ("derivative", "instantaneous rate", "FunctionType; libraries/calculus.py", 1,1,L,"NO_GAP",""),
 ("integral", "accumulation", "term; libraries/calculus.py", 1,1,L,"NO_GAP",""),
 ("continuity", "topological/epsilon-delta property", "Predicate over FunctionType", 1,1,L,"LIBRARY_GAP",""),
 ("partial derivative", "derivative in one coordinate", "FunctionType over ProductType", 1,1,L,"LIBRARY_GAP",""),
],
"real_analysis": [
 ("real number", "element of R", "ScalarType Real", 1,1,C,"NO_GAP",""),
 ("supremum", "least upper bound", "term with an existence Obligation", 1,1,L,"LIBRARY_GAP",""),
 ("convergence", "sequence tends to a limit", "proposition over an indexed family", 1,1,L,"LIBRARY_GAP",""),
 ("bounded error", "|x - y| <= eps", "the frozen bounded-error library concept; zero new primitives", 1,1,L,"NO_GAP","explicitly NOT equality -- the closure audit refused that conflation"),
 ("uniform continuity", "delta independent of point", "Predicate; quantifier order is preserved", 1,1,L,"LIBRARY_GAP","quantifier scope is carried, which is the point"),
],
"complex_analysis": [
 ("complex number", "element of C", "ScalarType Complex", 1,1,C,"NO_GAP",""),
 ("holomorphic function", "complex differentiable", "Predicate over FunctionType", 1,1,L,"LIBRARY_GAP",""),
 ("contour integral", "integral along a path", "term", 1,0,L,"LIBRARY_GAP",""),
],
"measure_theory": [
 ("measurable space", "set with a sigma-algebra", "ConceptType", 1,1,L,"LIBRARY_GAP",""),
 ("measure", "sigma-additive set function", "FunctionType SetType -> Real", 1,1,L,"LIBRARY_GAP",""),
 ("measurable function", "preimages measurable", "Predicate over FunctionType", 1,1,L,"LIBRARY_GAP",""),
 ("filtration", "increasing family of sigma-algebras", "indexed family; explicitly library-level", 1,1,L,"LIBRARY_GAP","the closure audit placed filtrations at library level"),
 ("almost everywhere", "up to a null set", "qualified proposition", 1,1,L,"LIBRARY_GAP",""),
],
"probability": [
 ("probability", "measure of an event", "QuantityType Probability -- NOT PositiveReal", 1,1,C,"NO_GAP","Probability and PositiveReal are incomparable by design"),
 ("event", "measurable subset", "EventType", 1,1,C,"NO_GAP",""),
 ("random variable", "measurable function on a sample space", "RandomVariableType", 1,1,C,"NO_GAP","an RV is not a Distribution and not a value of T"),
 ("distribution", "law of a random variable", "DistributionType", 1,1,C,"NO_GAP",""),
 ("conditional probability", "P(A|B)", "proposition with a P(B) > 0 Obligation", 1,1,C,"NO_GAP","partiality machinery carries the positivity obligation"),
 ("expectation", "mean of an RV", "FunctionType RandomVariableType -> Real", 1,1,L,"NO_GAP","libraries/probability.py"),
 ("variance", "second central moment", "FunctionType", 1,1,L,"NO_GAP",""),
 ("independence", "joint factorises", "Predicate over RandomVariableTypes", 1,1,L,"LIBRARY_GAP",""),
],
"statistics": [
 ("estimator", "function of a sample", "FunctionType; RandomVariableType output", 1,1,L,"LIBRARY_GAP",""),
 ("hypothesis", "a claim under test", "Claim with ClaimStatus.ASSUMED", 1,1,C,"NO_GAP","a hypothesis is not a fact -- status carries the distinction"),
 ("p-value", "tail probability", "QuantityType Probability", 1,1,L,"LIBRARY_GAP",""),
 ("confidence interval", "interval estimate", "term with a coverage Claim", 1,1,L,"LIBRARY_GAP",""),
 ("regression model", "structural relation", "ConceptType; examples/statistics", 1,1,B,"BACKEND_GAP","fitting is a backend concern (Stan)"),
],
"stochastic_processes": [
 ("stochastic process", "family of RVs indexed by time", "indexed family of RandomVariableType", 1,1,L,"LIBRARY_GAP",""),
 ("martingale", "conditional-expectation property", "Predicate; needs filtration", 1,1,L,"LIBRARY_GAP",""),
 ("Markov property", "memorylessness", "Predicate", 1,1,L,"LIBRARY_GAP",""),
],
"geometry": [
 ("point / line / plane", "primitive objects", "ConceptType or declared Objects", 1,1,L,"LIBRARY_GAP",""),
 ("distance", "metric between points", "FunctionType -> NonNegativeReal", 1,1,L,"LIBRARY_GAP",""),
 ("congruence / similarity", "geometric equivalence", "Predicate", 1,1,L,"LIBRARY_GAP",""),
],
"topology": [
 ("topological space", "set with open sets", "ConceptType", 1,1,L,"LIBRARY_GAP",""),
 ("open set", "member of the topology", "SetType with a Predicate", 1,1,L,"LIBRARY_GAP",""),
 ("continuity (topological)", "preimages of opens are open", "Predicate over FunctionType", 1,1,L,"LIBRARY_GAP",""),
 ("homeomorphism", "topological isomorphism", "FunctionType with inverse Claims", 1,1,L,"LIBRARY_GAP",""),
 ("compactness", "finite subcover property", "Predicate", 1,1,L,"LIBRARY_GAP",""),
],
"functional_analysis": [
 ("norm", "length function", "FunctionType -> NonNegativeReal", 1,1,L,"LIBRARY_GAP",""),
 ("normed space", "vector space with a norm", "ConceptType", 1,1,L,"LIBRARY_GAP",""),
 ("Banach / Hilbert space", "complete normed / inner-product space", "ConceptType with completeness Claims", 1,1,L,"LIBRARY_GAP",""),
 ("bounded operator", "continuous linear map", "FunctionType with a bound Claim", 1,1,L,"LIBRARY_GAP",""),
],
"differential_equations": [
 ("differential equation", "relation involving derivatives", "proposition over FunctionType", 1,1,L,"LIBRARY_GAP",""),
 ("initial condition", "value at a point", "Claim with ClaimStatus.GIVEN", 1,1,C,"NO_GAP",""),
 ("solution", "function satisfying the equation", "Claim; existence/uniqueness as Obligations", 1,1,B,"BACKEND_GAP","numeric solution needs a backend"),
],
"optimization": [
 ("objective function", "quantity to optimise", "FunctionType -> Real", 1,1,C,"NO_GAP",""),
 ("constraint", "restriction on the feasible set", "Obligation or a constraint Claim", 1,1,C,"NO_GAP","Candidate.constraint_ids links a candidate to its constraints"),
 ("feasible point", "satisfies all constraints", "Candidate with CandidateStatus", 1,1,C,"NO_GAP",""),
 ("optimality", "no better feasible point", "Claim; certificate as evidence", 1,1,B,"BACKEND_GAP",""),
],
"numerical_analysis": [
 ("floating-point value", "finite-precision number", "ScalarType with a bounded-error Claim", 1,1,L,"NO_GAP","approximation is never equality"),
 ("error bound", "|computed - exact| <= eps", "the frozen bounded-error library concept", 1,1,L,"NO_GAP",""),
 ("convergence rate", "how fast error shrinks", "Claim over an indexed family", 1,1,L,"LIBRARY_GAP",""),
 ("numerical method result", "output of an algorithm", "Claim with BACKEND_CERTIFIED evidence", 1,0,B,"BACKEND_GAP",""),
],
"category_theory": [
 ("category", "objects and morphisms", "ConceptType -- explicitly library-level", 1,1,L,"LIBRARY_GAP","the closure audit placed category theory at library level, not kernel"),
 ("morphism", "structure-preserving arrow", "FunctionType or declared relation", 1,1,L,"LIBRARY_GAP",""),
 ("functor", "map between categories", "FunctionType over ConceptTypes", 1,0,L,"LIBRARY_GAP",""),
 ("natural transformation", "map between functors", "not represented in 1.0", 0,0,U,"UNSUPPORTED","no counterexample has demonstrated a need"),
],
"constructive_mathematics": [
 ("constructive existence", "exists with a witness", "kernel exists_intro requires the witness term", 1,1,C,"NO_GAP","the witness is carried, not merely asserted"),
 ("proof relevance", "which proof was used", "evidence graph and warrant; proposition truth is proof-irrelevant", 1,1,C,"NO_GAP","truth is proof-irrelevant while provenance is preserved -- both, deliberately"),
 ("decidability", "an effective decision procedure", "Predicate plus BACKEND evidence", 1,0,B,"BACKEND_GAP",""),
 ("excluded middle", "P or not P", "not assumed by the kernel; no rule introduces it", 1,0,L,"LIBRARY_GAP","its absence is a deliberate kernel-minimality choice, not a gap"),
],
}
