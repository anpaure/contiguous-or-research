# K17 PBBS integrated double-rainbow factor (2026-07-31)

## Result

There is an explicit spanning 2-factor of `J(17,9)` with both immediate
shadows complete:

- its 24,310 edges have pairwise distinct rank-8 intersections, hence
  enumerate every member of `binom([17],8)` exactly once;
- its rank-10 unions cover every member of `binom([17],10)` at least once.

This is a literal finite certificate, not a solver lower bound or an orbit
count.  It is the first integrated K17 carrier in this project to close both
q1 shadow gates simultaneously.

It is **not yet a length-24,313 universal word**.  The certified factor has
21 components, 3,705 cyclic coordinate runs of length 2, 2,268 of length 3,
and 1,937 deeper upper misses.  Residence, component opening/splicing,
deeper upper coverage, and the depth-3 lower compiler remain separate gates.

## Construction

The fixed core bank contains 1,430 disjoint local paths.  It integrates all
5,005 U-sector owners, one X and one Y anchor per core, and one outer A owner.
The remaining A, X, and Y incidences form three exact bipartite b-matchings.

Starting from any feasible exact b-matching, an alternating cycle in a
consecutive-layer Boolean incidence graph rotates selected owners while
preserving every row and owner degree.  Consequently it preserves:

1. all 24,310 middle vertices and their degree 2;
2. all 24,310 distinct rank-8 lower colours.

The incidence graph has girth 6, so the primitive move is an alternating
6-cycle, not a 4-cycle.  A neutral-only walk in this exact fibre reduced the
rank-10 hole count

`4413 -> 902 -> 730 -> 1 -> 0`.

The final step from one hole to zero took 48,533,804 proposals (1,248,157
valid alternating-6 moves and 106,685 accepted neutral/improving moves),
19.8 seconds on one low-priority CPU core.

## Authenticated artifacts

- residual flow ledger:
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.tsv`
  
  SHA-256 `30501377d3186135d85e984330d50fbf0356de37f6351c15ae2e40766056af78`
- literal component list:
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components`
  
  SHA-256 `6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702`
- independent materialization audit:
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.audit.json`
  
  payload SHA-256 `8dbc822e6cf3ed4349baa92159b9b7badd36b6e0eeed339f6490f714466bc567`
- exact extension map `sigma(C)=left(C) union right(C)`:
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_extension_map_20260731.tsv`
  
  SHA-256 `4df887b944eba57f3a7a935b5d5df4c6ab6bb3b944f29b3889de7aecc1e748d7`

The independent audit reconstructs every physical edge from the fixed cores
and residual flow, checks all vertex degrees, checks the exact rank-8 rainbow,
checks the complete rank-10 image, and recomputes components and cyclic run
statistics.

## Extension-map census

The map from rank-8 intersections to rank-10 unions is total, containment
preserving, rank-raising by exactly two, and surjective.  Its load histogram
is

| load | targets |
|---:|---:|
| 1 | 15,166 |
| 2 | 3,733 |
| 3 | 519 |
| 4 | 29 |
| 5 | 1 |

Thus immediate-upper completeness does not force the stronger simple-design
profile `{1,2}`.  There are 549 upper targets of load greater than 2.

## Protected-transport Pareto checkpoint

Allowing protected alternating circuits of lengths 3 through 8 on the
bipartite incidence side produced a strictly stronger physical factor while
preserving both q1 gates.  The authenticated checkpoint has:

- q1 lower holes: 0;
- q1 upper holes: 0;
- residence potential `Phi_3 = 2*2212 + 1387 = 5811`;
- 16 components;
- 1,854 deeper upper holes, by rank `11:1528, 12:318, 13:8`.

Artifacts:

- flow `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_pareto5811_20260731.tsv`,
  SHA-256 `d8a68f29d71b564bbf616dcdc9402d0bfbb891a6fe4618e9e5f6b96f3535c936`;
- components
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_pareto5811_20260731.components`,
  SHA-256 `5a1239bec49192b354a968fd7b312e091e7843f0748866e6240879a7bf2b6231`;
- independent audit
  `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_pareto5811_20260731.audit.json`,
  payload SHA-256
  `b0a1c51f9e8a3a38bd780a994059386e2f523813422751c54c1e62703fd24934`.

This checkpoint remains a factor, not a universal word.  Its value is that
all four secondary metrics moved in the correct direction inside the exact
double-rainbow fibre.

### Variable-staircase support threshold

Continuing protected transport produced a second checkpoint adapted to the
correct variable-deadline criterion (strong minimum run four is not
necessary).  It has:

- q1 lower and upper holes: 0;
- run-2 count 2,025 and run-3 count 1,221;
- 7,115 distinct carrier vertices lying in a run of length 2 or 3;
- K17 scalar slack 7,401, hence support-cardinality margin 286;
- 11 components and 1,838 deeper upper holes.

Artifacts:

- flow `scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.tsv`,
  SHA-256 `0706e325c71e97a98cc09363e9526121cde9a54dba36a2130ecc6740cb9bd1b4`;
- components SHA-256
  `3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e`;
- factor audit payload
  `c8a091333429973fb145e14f4a72fb567a5fef819b6c982f95bd842d7a9f0221`;
- run-support audit payload
  `7fcb2f80579ad5593fdaa1641783be1c946daf9a160ef9eac8207ed31606264f`.

This passes only the **support cardinality** necessary for a plausible
span-2 staircase.  It does not yet order those vertices into monotone
start/deadline corridors, prove chain alignment, or pass the common-cap
compiler.  In fact the support is presently dispersed: after taking the
best single cyclic cut in each of the 11 components, the sum of the minimal
cyclic hull spans is 23,525 for run-2-or-run-3 support and 23,341 for run-3
support alone, both far above 7,401.  A genuine rethreading/clustering step
is therefore required; the cardinality threshold is not corridor
feasibility.

## Scope discipline

This result proves an exact double-rainbow **2-factor** at K17.  It does not
by itself prove `nu(17)=24313`, and it does not replace the independently
verified general explicit upper bound `nu(17) <= 25746`.
