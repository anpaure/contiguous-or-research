# Independent code audit: unrestricted triple-preserving cap decision and literal replay

2026-09-08. `exact_equality_structure`. **PASS for the mathematical
encoding and the independent literal checker.** This audit executed
neither a solver nor a candidate replay. Solver/proof-checker outcomes
must be read from their separate execution certificates.

Files read in full:

* [decide_k17_unrestricted_triple_caps_cadical195_20260908.py](decide_k17_unrestricted_triple_caps_cadical195_20260908.py).
* [replay_k17_unrestricted_triple_cap_bank_20260908.py](replay_k17_unrestricted_triple_cap_bank_20260908.py).

The mathematical reference is
[the complete unrestricted CNF theorem](PBBS_UNRESTRICTED_TRIPLE_CAPS_COMPLETE_CNF_AND_SPARSE_RUN_CLAUSES_20260908.md).

## 1. Formula generation

The decision program reconstructs D^min(h,3) from the canonical owners.
It freezes H1/H2, and its fixed lower palette is computed solely from
those frozen components. It checks that this palette has 1,887 rank-seven
labels; it does not import the old anchor-frame fixed palette. Thus the
required lower target set has 39,338 labels.

Optional coordinate bits are shared by physical cyclic positions.
Pins are represented as masks, not Boolean sentinels that could be
confused with variable id 1. Every nonpinned coordinate of every
original triple is supplied by an explicit positive clause. A pinned
coordinate is correctly skipped. The assertion that every remaining
clause has length three exactly matches the sparse source-run theorem.
All modular wraparound triples are included.

Every singleton and cyclic adjacent pair is considered. Its entire
Boolean target interval between the pin union and source union is
enumerated, with 631,992 host incidences as an input-consistency check.
Only fixed lower targets are omitted. Selector implications exclude
all outside-target optional bits and require every inside-target bit
to appear in the selected interval. A pin can satisfy a positive
requirement and cannot be removed by an eligible host. One coverage
clause is added for every unfixed target.

These are exactly the forward-only clauses of the complete theorem.
No unsupported reverse implication, host-disjointness restriction,
anchor, rank-six reservation, or independent-channel relaxation is
introduced. Variable numbering, the streamed DIMACS header, and the
physical cap/selector mappings are consistent with this construction.

## 2. Execution and certificate boundaries

The reviewed implementation has one CaDiCaL195 instance with seed 0
and one call to solve. Formula loading is included in the worker CPU
budget. The parent reserves time for extraction and validation, and
tightens its own remaining CPU allowance after measuring child CPU.
The total wall deadline includes generation, the one worker, and
validation. Parent and worker address-space limits sum to four GiB.
The worker also bounds a single proof/output file to one GiB.

The program refuses an existing output directory rather than reusing
an old result. Worker exhaustion and the overall wall/CPU limit are
reported as INCONCLUSIVE. Two hardening points raised in this review
were incorporated and reread: the exact canonical SHA-256 is asserted,
and driver MemoryError releases an emergency buffer before producing
an INCONCLUSIVE report. Mathematical execution is guarded to h100.

On SAT the complete model and physical capped cycle bank are saved.
The decision script then checks every cap, every native triple, all
cyclic target witnesses, and independently replays those witnesses by
range OR. This physical verification suffices to certify the claimed
bank even though it does not independently re-evaluate every selector
clause of the solver's model.

On UNSAT it preserves the binary proof but explicitly labels the
result SOLVER_REPORTED_UNSAT_UNCHECKED. An independently verified
proof is still required before using the result as a mathematical
infeasibility theorem. The present code-review PASS is not such a
proof check.

## 3. Independent literal-bank checker

The root's separate replay script pins the canonical input hash and
accepts only one candidate row per original cycle. It independently
reconstructs every original D^H, checks nonempty subset caps, keeps
H1/H2 exact, and checks every cyclic H3 triple. It additionally
checks all rank-eight/rank-nine endpoint identities and their global
bijections over the 24,310 source positions.

Its ending-suffix recurrence retains a latest start for each distinct
OR. This is sound because an older start producing the same OR cannot
give a new future OR after appending a letter. Its suffix states are
ordered by nested intervals, so duplicate ORs are consecutive and
the adjacent-equality suppression is complete.

If a retained suffix spans more than one period, replacing its start
by the most recent full-period start preserves its OR: every interval
of at least one period in a periodic word has the same union as one
whole period. Reducing the start modulo the period then gives the
same cyclic witness with length between one and the period. The
second-period endpoint range visits every possible cyclic phase.

Every produced witness is independently queried against a segment
tree on the doubled literal cycle. Hence a PASS requires actual
ordinary OR equality for all 131,071 nonempty target masks. Missing
targets produce an explicit incomplete-cover report rather than a
false success. No CNF, solver model, or trusted selector witness is
needed for this independent replay.

Neither program equates a complete cyclic bank with a single linear
word. A further legal splice/opening remains necessary for an optimal
B(17)-word.
