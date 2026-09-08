# The fixed 21-coordinate candidate graph has a certified Hall deficiency of 462

Date: 2026-09-09. One independently implemented, source-reviewed h100
build and one fixed-graph execution completed. All claimed numerical
values were comparisons, not premises of the computation.

**Result.** For the three cyclic components extracted from the supplied
353,297-letter word, the complete individual single/pair candidate graph
has maximum matching size 695,397 against 695,859 lower targets. Its exact
deficiency is 462. A concrete Hall family has 31,185 physical targets and
only 30,723 physical candidate cells.

This is an obstruction within that fixed cyclic carrier with every native
rank 10 triple preserved. It is NOT a lower bound of B(21)+462 for general
words, and no simultaneously realizable cap assignment is certified.
The supplied repair suffix and cross-component linear seams are outside
this cyclic candidate graph.

## Observed counts

| Quantity | Exact result |
|---|---:|
| Physical cyclic positions |352,716|
| Target orbits, ranks1 through9 |33,143|
| Total physical target demand |695,859|
| Single/pair cell orbits |33,592|
| Capacity of each cell orbit |21|
| Accepted local masks before orbit deduplication |2,011,584|
| Deduplicated orbit graph edges |1,997,177|
| Maximum weighted flow |695,397|
| Physical candidate matching deficiency |462|
| Hall target orbits |1,485|
| Hall physical target weight |31,185|
| Complete neighbor cell orbits |1,463|
| Complete physical neighbor capacity |30,723|
| Positive flow records independently replayed |33,243|

The complete graph, primal flow, dual Hall set and full expanded physical
target/neighbor lists are saved in the artifact bundle. This is not a
sampled neighborhood or an extrapolation from an orbit count.

## Exact input and reconstruction

The only literal input has SHA256

    0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7.

The checker verified the fixed split into periods 352,548, 105 and 63, each
followed by its own first three letters, followed by 572 repair letters.
Their period sum is 352,716. With cyclic indices on each component C,

    R_i=OR(C_i,C_(i+1),C_(i+2)),
    U_i=OR(C_i,...,C_(i+3)),
    E_i=AND(U_(i-3),...,U_i).

It re-established every rank 10 R and every rank 11 U exactly once,
canonical outgoing Phi, both owner-incidence identities, containment of
the actual letters in E, and exact future triple/four identities for E.
Successor, U and E commute with coordinate rotation. Every middle orbit
has 21 members. Actual capped letters were not assumed equivariant.

For each single/pair cell I, the exact forced set K_I is the union of
the deficits of every affected R triple after all positions outside I
are left at E. The available set is V_I=OR_(i in I)E_i. The full menu
consists of all nonempty S of rank at most 9 with

    K_I subset S subset V_I,
    E_i intersect S nonempty for every i in I.

Every one of the 2,011,584 accepted masks was directly checked by replacing
the cell letters with E_i intersect S and replaying every affected triple.
The exact deficit proof establishes necessity as well as sufficiency;
see the [review specification](K21_FIXED_THREE_CYCLE_CANDIDATE_HALL_CHECKER_SPECIFICATION_20260909.md).

## Why the saved primal and dual certify the answer

Target orbit demand is its actual size 21, 7 or 3; each cell orbit contains
21 physical cells. The code ran Dinic once. A separate replay phase in
the same reviewed program reread the exported graph, positive flow and
cut files. It checked edge membership, uniqueness, nonnegative integral
values, every capacity, and reconstructed conservation independently of
Dinic's residual/source/sink bookkeeping.

For every cell orbit, it then regenerated the ENTIRE menu from the native
triple deficits, rather than trusting the saved adjacency row. This
re-established the full Hall neighborhood and checked the exact equality

    695859-695397 = 31185-21*1463 = 462.

Thus a feasible flow and a matching upper bound prove the optimum even
without trusting that Dinic found a maximum. The regeneration shares the
reviewed candidate kernel; it is a separate logical replay phase, not a
claim of two independently written host-enumeration implementations.

The orbit optimum equals the expanded physical candidate matching optimum.
For each orbit-pair incidence, rotation makes the physical bipartite graph
biregular. Distributing any orbit flow uniformly over those edges yields
a feasible fractional physical matching of the same value; bipartite
integrality supplies an integral matching. Conversely any physical
matching aggregates to an orbit flow. The Hall family also proves the
physical obstruction directly, without this lifting argument.

Any globally triple-preserving cap of these cycles needs a length-one
or length-two witness for a target of rank at most 9. Each physical cell has
only one OR value, so the 31,185 targets in the exported family cannot
all fit in their 30,723 possible cells. At least 462 must remain uncovered
by the cyclic bank, whatever the simultaneous cap choices are. Overlap
between cells can only add constraints; the feasible matching does not
remove those constraints.

## Build, run, and artifacts

Root, induction and structure independently read the complete sources
before root authorized the one build and run. These are internal source
reviews, not an external formal verification claim.

* [C++ source](certify_k21_fixed_three_cycle_candidate_hall_20260909.cpp), SHA256
  `26fb17223bcd5ef0d79ac27a90b37d2c7b52b1c7cf706622f7c22f624fdee120`.
* [Runner](run_k21_fixed_three_cycle_candidate_hall_20260909.py), SHA256
  `e615be577c4e43427fc022b7e88eb0616299d460f70e226b8886bb58d1651d33`.
* Executed binary SHA256
  `f6595344c18876165034bec17e0d8c9a629736a151b98a283ba63cfea0d9f591`.

One C++17 build used `g++ -std=c++17 -O2 -Wall -Wextra`, under CPU 60,
wall 90 seconds and 2 GiB. It exited with code 0; the single misleading-indentation
warning concerned a correctly placed offset update outside a collar loop.
No source change or rebuild followed that warning.

The one run used a pinned immutable input snapshot and a copied, hashed
binary. Limits were aggregate CPU 120 seconds (driver 5 plus child 115),
wall 150 seconds, 2 GiB address space, and 512 MiB per file. It returned
`PASS_FIXED_GRAPH_AND_INDEPENDENT_CERTIFICATE_REPLAY`, exit code 0. Actual
aggregate CPU was 2.877601905 seconds and wall was 2.879199883900583 seconds.
There was no retry, alternate cut, graph change, word search or extra flow.

Complete local bundle:
[k21_fixed_candidate_hall_20260909/](k21_fixed_candidate_hall_20260909/).
Principal reports are `run_complete.json` and `candidate_hall_certificate.json`.
The binary graph format and orbit mappings are retained alongside positive
flows, cut lists, complete physical Hall masks/cells, input snapshot,
executed sources/binary, build/run logs, commands, provenance and hashes.

Remote output:
`/home/amodo/exact-b-k21-fixed-candidate-hall-20260909/`.
