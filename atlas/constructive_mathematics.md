# Constructive Mathematics

*HML Standard 1.0 — semantic atlas*

The question each row answers is **not** whether HML proves the concept. It is whether HML can carry its reasoning state losslessly.

| Concept | Role | HML representation | Carry | Manipulate | Verify | Verdict |
|---|---|---|---|---|---|---|
| constructive existence | exists with a witness | kernel exists_intro requires the witness term | yes | yes | CORE | **NO_GAP** |
| proof relevance | which proof was used | evidence graph and warrant; proposition truth is proof-irrelevant | yes | yes | CORE | **NO_GAP** |
| decidability | an effective decision procedure | Predicate plus BACKEND evidence | yes | no | BACKEND | **BACKEND_GAP** |
| excluded middle | P or not P | not assumed by the kernel; no rule introduces it | yes | no | LIBRARY | **LIBRARY_GAP** |

## Notes

- **constructive existence** — the witness is carried, not merely asserted
- **proof relevance** — truth is proof-irrelevant while provenance is preserved -- both, deliberately
- **excluded middle** — its absence is a deliberate kernel-minimality choice, not a gap
