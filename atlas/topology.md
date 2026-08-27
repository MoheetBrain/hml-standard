# Topology

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| topological space | set with open sets | ConceptType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| open set | member of the topology | SetType with a Predicate | yes | yes | LIBRARY | **LIBRARY_GAP** |
| continuity (topological) | preimages of opens are open | Predicate over FunctionType | yes | yes | LIBRARY | **LIBRARY_GAP** |
| homeomorphism | topological isomorphism | FunctionType with inverse Claims | yes | yes | LIBRARY | **LIBRARY_GAP** |
| compactness | finite subcover property | Predicate | yes | yes | LIBRARY | **LIBRARY_GAP** |
