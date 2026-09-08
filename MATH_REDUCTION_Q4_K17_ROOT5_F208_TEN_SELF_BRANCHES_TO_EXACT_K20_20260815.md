# Reduction: the q=4, k=17 root5 F208 leaf is ten exact K20 decisions

Date: 2026-08-15  
Status: exact reduction; leaf6254 has nine UNSAT branches and one UNKNOWN;
three later hard-branch reruns remain UNKNOWN

## 0. Scope

This note concerns one frozen root5 defect-cover leaf in the reflection
owner-factor search.  The retained incumbent is simple, its free row set
`F` has size 208, and the destroyed profile consists of two self columns
and twenty reflected-pair columns.  This is a statement about the frozen
column catalogue only.  A SAT witness remains valid after enlarging the
catalogue; an UNSAT verdict does not.

## 1. Ten self-conditioned branches

The two destroyed self groups are 30 and 31.  Their eligible four-row
menus are

```
group 30: 3309, 3316
group 31: 3361, 3425, 3428, 3429, 3438, 3439.
```

Exactly ten cross-group pairs have disjoint row sets:

```
(3309,3361) (3309,3425) (3309,3428) (3309,3429) (3309,3438)
(3309,3439) (3316,3361) (3316,3425) (3316,3428) (3316,3439).
```

Every legal patch chooses exactly one menu from each destroyed group, so
these ten choices are exhaustive and mutually exclusive.

## 2. Exact K20 reduction

Fix one of the ten compatible self pairs, with eight-row union `S`.
Put

```
U = F \ S,                  |U| = 200,
P(U) = {catalogue pair columns C : C subset U}.
```

Every reflected-pair column has ten distinct rows.  Hence a completion of
this branch consists of exactly twenty members of `P(U)`, and it is exact
if and only if those twenty ten-sets are pairwise disjoint.  Equivalently,
form the graph `G_U` on `P(U)` in which two vertices are adjacent exactly
when their row sets are disjoint.  The branch is completable if and only
if `G_U` contains a clique of size twenty.

This is an equivalence, not merely a relaxation: twenty disjoint ten-sets
inside a 200-set have union exactly `U`.

## 3. Exact bitset recurrence

For a remaining-row mask `R subset U`, let `D(R)` mean that `R` is exactly
partitionable by catalogue ten-sets.  Select canonically a row `r in R`
of minimum current incidence degree.  Then

```
D(empty) = true,
D(R) = OR[D(R \ C) : C in P(U), r in C, C subset R].              (3.1)
```

Thus the remaining-row mask alone is a complete memoization key.  The
candidate bank at a node is precisely the set of original columns
contained in `R`; it does not depend on the route to `R`.

Two lossless cuts are used.

1. Properly greedily color the disjointness graph induced by the current
   candidates.  Every clique uses at most one vertex per color.  Fewer
   than `|R|/10` colors proves the node impossible.
2. Split the row--column incidence hypergraph into connected components.
   Any component whose row cardinality is not divisible by ten is
   impossible; otherwise the components are independent exact-cover
   instances and may be solved separately.

Branching in (3.1), memoization, the coloring upper bound, and component
splitting therefore preserve both SAT and UNSAT.  A wall-clock cutoff
returns `UNKNOWN`; it is never promoted to a mathematical verdict.

## 4. Frozen H100 interface

The builder regenerates the ten complete self-conditioned pair banks from
the frozen instance.  The independent replay regenerates them a second
time, checks every graph column's literal row payload, binds graph and
solver hashes, and directly checks any SAT patch against all 208 free
rows.  The executable was additionally compared with a separate brute
force exact-cover recursion on deterministic synthetic SAT, UNSAT, and
disconnected instances of 20, 30, and 40 rows.

## 5. Bounded verdict

The frozen leaf6254 instance has SHA-256

```
491e2503f2d76d6e16d73a1159696123f9cd60c2625f1c24509776fb05a95ecc
```

and its ten-branch manifest has SHA-256

```
a58299caf8c73f040256a34ac064ff91b2e5644f37186069db49ffb57e8cb3ce.
```

The exact solver source/binary hashes are respectively
`5f5ff9e59a5718faca50f9f6fa27d514a51bf272279bf844f329aa15b7238caf`
and
`b4b0fc0f5cb403cccf7d6a37536ad092b9be6752a723219f129fc3c6cdc41e07`.
The bounded 600-second-per-branch result is:

| self pair | columns | verdict | seconds | nodes |
|---|---:|---|---:|---:|
| 3309,3361 | 3,224 | UNSAT | 463.401 | 41,689,917 |
| 3309,3425 | 3,263 | UNSAT | 451.811 | 40,077,162 |
| 3309,3428 | 3,352 | UNSAT | 546.839 | 49,673,924 |
| 3309,3429 | 3,462 | UNKNOWN | 600.030 | 55,050,240 |
| 3309,3438 | 3,486 | UNSAT | 552.938 | 50,177,242 |
| 3309,3439 | 3,361 | UNSAT | 446.512 | 42,986,928 |
| 3316,3361 | 3,203 | UNSAT | 381.025 | 35,006,074 |
| 3316,3425 | 3,271 | UNSAT | 368.915 | 30,959,256 |
| 3316,3428 | 3,368 | UNSAT | 500.291 | 44,555,343 |
| 3316,3439 | 3,393 | UNSAT | 424.992 | 37,729,291 |

Thus leaf6254 has nine exact branch no-gos but no global verdict: the one
UNKNOWN branch keeps the complete F208 patch question open.  The
independent complete-bank replay is PASS, with report SHA-256
`c6df5e6e20b6e7e54dbff1651480dabe9b66585d0f672fcae9d7aabea90c7e27`;
the complete graph/result hash ledger has SHA-256
`2d7a158a1ffb986ac514e97ca1e0c1e5698ee769a9c8f27a42294ce40db783c3`.

The separate 28-case brute-force synthetic replay is PASS.  Its verifier
and output hashes are respectively
`6330c85a3b18f426d91ffb41f30d859343473cc8c3fffa25b0220dd197e6e32b`
and
`91a79bb7d3d14ba193d77d7eb52b0bf670f08d09eca1f92b2a1ec467409adea7`.

The prescribed three-branch rerun on the enlarged leaf7137 snapshot did
not yield a false negative or a promoted timeout: all three answers are
`UNKNOWN` at the 600-second cap.  Their node counts are 59,887,616 for
`(3309,3428)`, 59,670,528 for `(3309,3429)`, and 60,067,840 for
`(3309,3438)`.  The selected-branch literal replay is PASS, with report
SHA-256
`0fa4ea8a2e41f7e4d526c2fd0fee7731918221bf5c6ff001d352c1b47f7d2a4b`.

## 6. Latest-snapshot bottleneck rows

On the later immutable leaf7137 snapshot (instance SHA-256
`f9465574135bfcc55f0eeefc6ecce4299e933e6540ae00ccfeb6b8b63f92e4f5`),
the three formerly hardest branches have the following exact minimum
row-incidence data:

| self pair | pair columns | minimum row | degree | increase from leaf6254 |
|---|---:|---:|---:|---:|
| 3309,3428 | 3,891 | 661 | 101 | 0 |
| 3309,3429 | 4,031 | 516 | 100 | 11 |
| 3309,3438 | 4,063 | 516 | 83 | 9 |

Rows 595, 642, 585, and 274 are common secondary bottlenecks.  Moreover,
the global F208 catalogue through row 661 was already exhaustive before
leaf6254.  Its zero increase in branch `(3309,3428)` is therefore a
residual-set filtering obstruction, not an invitation to regenerate the
same row.  The incidence report has SHA-256
`dd95d06fe65ef3ad48364229e1bb2e4bce88777ccb0b69c20a48c9b481187636`.

Row 516 was then generated exhaustively and appended in the immutable
leaf7372 snapshot.  The updated hard-branch counts/minima are

| self pair | pair columns | minimum row | degree |
|---|---:|---:|---:|
| 3309,3428 | 4,033 | 661 | 101 |
| 3309,3429 | 4,161 | 661 | 104 |
| 3309,3438 | 4,190 | 661 | 106 |

Thus exhaustive row 661 is now the common irreducible first pivot.  The
next incomplete common rows, in exact priority order, are 642 (degrees
107/112/114), 595 (110/114/115), and 585 (118/122/123).  The leaf7372
bottleneck report has SHA-256
`0040057cda02c0f587261c3a8a029f801b72d45d03108f7a56c7f4d6df806e27`.
Neither old UNSAT branch admits a one-step incremental cut at row 661:
every one of its pivot choices is compatible with at least 319 newly
added columns.  The exact incremental report has SHA-256
`f764638e6d79682ecc71125ab7672e43f9133e3ba1eae485295a70e855418cb5`.

Continuing exact forced-row generation gives the following numbers of new
columns surviving the three hard residual sets, in branch order
`3428/3429/3438`:

```
row 642: 34 / 37 / 40
row 595: 77 / 78 / 80
row 585: 35 / 39 / 40
row 284: 64 / 64 / 74.
```

After appending these banks, immutable leaf7796 has 4,243/4,379/4,424
pair columns in the three hard branches.  Rows 661 remain the respective
minima at degrees 101/104/106.  Several subsequent low rows (including
row 28 in the first branch) are also already exhaustive, so their low
degree is a residual-set obstruction.  The next incomplete common target
is row 431, at degrees 140/138/141; row 144 is the next branch-specific
target for `(3309,3438)`.  The leaf7796 bottleneck report has SHA-256
`4f6ef266f534e7683a6ef9c49a51610f797d5a93c63ac32a076d8f446264983e`.

## 7. Diversified SAT-first boundary

A separate seeded solver changes only the exhaustive traversal order.  It
chooses reproducibly among near-minimum rows and uses four candidate-order
modes (random, maximum continuation, minimum continuation, and noisy
maximum continuation).  An UNSAT memo is written only after a state is
fully exhausted; a cutoff propagates `UNKNOWN`.  Thus the randomization
cannot create a false SAT or UNSAT.

On immutable leaf8418, eight 120-second seeds were run for each of the
three hard branches, with row slacks `0,0,2,2,4,4,8,8`.  All 24 results
are `UNKNOWN`; none is a witness or a no-go.  Nevertheless, this is a
genuinely diversified negative search result: every branch has eight
distinct root-order hashes and five, five, and six distinct first pair
choices.  The unique root local row 194 is global row 661 in all runs.
The source/binary hashes are

```
f38bef5693ae0cdba614c1d3c75af84632a9aed8a4a360ec3b74d41fe035a995
4f303814939a5f199ecc241c6099223c865e895ddaf19f07e1314fded72177d3
```

The 28-case brute-force replay is PASS.  The literal 24-result replay and
campaign summary hashes are respectively
`825a97dd3427c140c3fad649bebe75cecb8a0fcbe8f752f204bab41935e2ff96`
and
`8d7cfd8ac1a85ea4194b9769f95199854e528416ecb0f2ad4aa6cdcd42dbb43a`;
the complete result hash ledger has SHA-256
`3b9f619ea4311c5f58d730cf5f28aa4bae076a2b3c903348243a69407e55dcbe`.

## 8. Exact mandatory-row pivot partition

Because every exact cover uses exactly one column through exhaustive row
661, the hard search is the disjoint union of its row-661 pivot
subproblems.  On immutable leaf8570 the three branch counts are
101, 104, and 106, hence 311 independent residual decisions.  Each has
190 rows and target clique size 19.  Their pair-column counts range from
2,610 to 3,460, and their minimum residual row degrees range from 27 to
87.

This partition produces no immediate Hall/component certificate: every
one of the 311 residual incidence graphs is connected, and none has a
zero row or a component of order nonzero modulo ten.  Its value is exact
parallelism.  A SAT-first campaign can batch the 311 disjoint subtrees;
any 19-column witness is combined with its unique pivot and replayed on
all 208 rows.  Exact UNSAT would require exhausting every pivot, but each
can be proved independently.  The builder and complete partition-report
hashes are respectively
`9c4fc92a24daf1b1b2ead21c70836204e5181b41661f611118124aa19c1e4e42`
and
`822c68e8afa40d2c7c926b7da99c979ac7c463136f49efc35e538c6a5c94ff36`.
