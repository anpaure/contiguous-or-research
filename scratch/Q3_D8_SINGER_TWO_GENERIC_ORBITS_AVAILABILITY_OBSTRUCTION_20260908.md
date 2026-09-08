# Two Singer orbits leave an unrepairable core in every case

2026-09-08. A complete structural inventory, one solver call, and an
independent exact availability check. The availability check excludes
all 54 possible source pairs without optimization. This is a result
for the specified Singer construction, not the unrestricted ternary
cover problem.

## 1. The restricted construction

Use the admissible translation/complement catalogue from
`Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_BOUNDED_ATTEMPT_20260908.md`.
Its 3024 generic short bundles each contain eight physical rectangles.
Exactly 1008 bundles contain two of the 28 previously missing critical
vertices, called class C in
`Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md`.

Let S multiply coordinate labels by alpha in F_8, with
alpha^3=alpha+1. Its literal coordinate permutation is

    S = [0,2,4,6,3,1,7,5].                            (1)

This is linear, fixes zero, and cycles the seven nonzero labels.
It acts freely on the seven linear hyperplanes. Every generic bundle
therefore has a seven-element orbit under S.

The proposed construction chooses two Singer orbits of seven generic
two-C bundles, thirteen size-four self-complementary short orbits,
and one of the 336 allowed size-four full orbits. Its row count and
actual charge would be

    14*8 + 13*4 + 4 = 168,
    164*14 + 4*18 = 2368.                             (2)

The 1016 available rank-seven occurrences force every critical target
to be covered exactly once. A Singer aggregate must therefore have
42 distinct critical vertices, and two selected aggregates must be
critically disjoint.

## 2. Complete inventory

In canonical Fano coordinates, class C consists of the 28 antiflags
(L,a), where L is a Fano line and a is a nonzero point outside L.
The two-C incidence graph of the 1008 generic bundles is exactly

    (L,a) adjacent to (L',a') iff a in L' and a' in L.

It has 84 edges, every vertex has degree six, and each graph edge
has twelve physical generic-bundle variants. The complete class
multisets of these variants are:

| Critical classes in a generic bundle | Number |
| --- | ---: |
| B + 2C + 2D + F | 672 |
| 2C + 4D | 336 |

The 1008 bundles give 144 Singer aggregates before screening. Exactly
75 have no internal critical repetition:

| Critical classes in an admissible aggregate | Number |
| --- | ---: |
| 7B + 14C + 14D + 7F | 60 |
| 14C + 28D | 15 |

Exactly 54 unordered pairs of these aggregates are critically
disjoint. Each pair covers all 28 C vertices and passes all eight
self-family binary parity conditions. Every pair leaves the same
43-vertex class inventory:

    A + 7B + 14D + 7E + 14F.                         (3)

All 54 pairs have full candidates critically disjoint from their
generic part: 30 pairs have 42 compatible full choices, 21 have 35,
and three have 28. The complete Singer source space is thus these
54 pairs, not a sampled subset.

## 3. Solver outcome and independent replacement

One CP-SAT model used a selector for the source pair, thirteen self
short choices, and one full choice. It retained all 891 target-orbit
coverage constraints and exact coverage on the 127 critical target
orbits. It reported INFEASIBLE during presolve, with zero branches
and zero conflicts, after 0.073018947 solver seconds.

That status alone was not treated as an independently replayed
mathematical certificate. A separate exact availability check was
then authorized and run, without an optimizer.

For each of the 54 source pairs, the check read the complete original
pool of 2184 self short candidates and all 336 full candidates. It
retained every candidate whose critical set is disjoint from the
84 fixed generic critical vertices. This filtering is necessary for
any cover meeting (2). It then took the union of:

* all targets already covered by the fourteen fixed generic bundles;
* all targets covered by every retained self short candidate;
* all targets covered by every retained full candidate.

For every one of the 54 pairs, this entire union still misses a
target. Hence no selection of compatible self/full candidates can
repair that pair. The argument even permits arbitrarily many such
compatible repair candidates; their proposed counts thirteen and
one need not be used in the final exclusion.

The diagnostic exported a literal missing target for each pair,
along with compatible-candidate counts and the number of missing
target orbits. It selected a critical missing target whenever one
was available. The selected witnesses have ranks five for 36 pairs,
six for six pairs, and seven for twelve pairs.

For source pair zero, consisting of aggregate indices 0 and 62,
there are 168 compatible self candidates and 42 compatible full
candidates. Even their complete union misses

    (2,1,1,1,0,0,0,0),                              (4)

of rank five and little-endian ternary code 41. This pair misses
84 target orbits despite having no missing critical orbit in the
complete compatible union. Thus an exclusively critical-layer
construction would not resolve the full-cover requirement.

All 54 source pairs failed at this first availability stage. No
full-specific second stage was needed or run. No mathematical
restart, second solve, or DFS ran.

## 4. Source audit, files, and runtime

The cover_selectors agent independently audited the entire Singer
inventory/model source. Its audit passed the linear order-seven
action, canonical complement keys, exhaustive orbit partition,
critical filters, parity filters, complete target model, and literal
replay code. No witness was returned, so the witness replay code was
not executed.

The same agent separately audited the independent availability
source and saved summary. That audit passed its use of all original
self/full candidates, the enlarged-union exclusion, all 54 exported
failures, and the unused full-specific stage.

The three mathematical processes ran only on h100:

| Process | Runtime | Outer cap |
| --- | ---: | ---: |
| Complete Singer inventory | 0.08147604996338487 s | 3 s |
| Solver process including setup | 0.42511450685560703 s | 14 s |
| Independent availability check | 0.07448701513931155 s | 2 s |

The solver itself had a ten-second limit but terminated in presolve.
All processes used two-CPU affinity. The inventory/solver used a
3 GiB address-space limit; the availability check used 1 GiB.

Files:

* `q3_d8_singer_two_generic_orbits_attempt_20260908.py`;
* `Q3_D8_SINGER_TWO_GENERIC_ORBITS_CATALOGUE_SUMMARY_20260908.json`;
* `Q3_D8_SINGER_TWO_GENERIC_ORBITS_CATALOGUE_20260908.json`;
* `Q3_D8_SINGER_TWO_GENERIC_ORBITS_SOLVER_SUMMARY_20260908.json`;
* `q3_d8_singer_availability_certificate_20260908.py`;
* `Q3_D8_SINGER_AVAILABILITY_SUMMARY_20260908.json`;
* `Q3_D8_SINGER_AVAILABILITY_CERTIFICATE_20260908.json`.

The source-pair catalogue identifies every constituent generic
bundle by its index in the complete relaxed catalogue. The final
availability certificate identifies every one of the 54 source
pairs and supplies its explicit missing-target witness. Replaying
the availability source against the saved complete catalogue
requires only exact set/bitset unions and comparisons.

The result excludes the two-Singer-orbit construction specified in
Section 1. It does not exclude general choices of fourteen generic
bundles or constructions using generic bundles that contain only
one C vertex.
