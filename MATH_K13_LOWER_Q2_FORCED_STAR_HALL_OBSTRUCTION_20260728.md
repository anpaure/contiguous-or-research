# Lower-q2 holes force Hall stars in the depth-three compiler

## Statement

Let `T=(T_i)` be a cyclic rank-7 Johnson word on `[13]` with

1. no residence return at distance at most three; and
2. perfect lower-q1 coverage, so the 1,716 masks `T_i cap T_{i+1}` are all
   rank-6 masks, each exactly once.

Let `P` be the coordinatewise maximal depth-three preimage, so
`D^3 P=T`, where `D` is adjacent union.  Consider the usual compiler Hall
graph: the left vertices are lower targets of ranks 1 through 6, and the
right vertices are cells of depths 0, 1, and 2 in `P`.  An edge means that
the target can be realized on that cell while retaining all coordinates
forced by `D^3P=T`.

Then every cyclic lower-q2 hole

```text
R not in {T_i cap T_{i+1} cap T_{i+2}}
```

creates a Hall-deficient forced star.  In particular, the cyclic compiler
cannot cover all lower targets unless lower q2 is exact.

For a linear cut, the same conclusion holds for every star whose cells are
interior.  Only the `O(1)` cells meeting the erosion seam can evade the
argument.  Thus a cut may rescue only `O(1)` physical roots; it cannot repair
a translation orbit of lower-q2 holes.

## Proof

Residence at least four gives the interior maximal erosion explicitly:

```text
P_i = T_i cap T_{i+1} cap T_{i+2} cap T_{i+3}.
```

Consequently:

* a depth-0 envelope has rank 4, hence cannot contain a rank-5 target;
* a depth-1 envelope satisfies

  ```text
  P_i union P_{i+1}
      subset T_{i+1} cap T_{i+2} cap T_{i+3}.
  ```

  The right-hand side has rank 5, because the two consecutive deletions are
  distinct and neither is reinserted within distance three.  Therefore a
  rank-5 target realizable on this depth-1 cell is exactly that lower-q2
  colour.  A lower-q2 hole has no depth-1 candidate.

It follows that every compiler candidate for a missing rank-5 target `R` is
a depth-2 cell.  For such a cell `J_i=(P_i,P_{i+1},P_{i+2})`,

```text
P_i union P_{i+1} union P_{i+2}
    = T_{i+2} cap T_{i+3} =: Y_i.
```

The equality is the standard maximal-preimage identity; the inclusion from
left to right is immediate, and every coordinate of the rank-6 target
`Y_i` needs a carrier in `J_i` to reconstruct `T_{i+2}` and `T_{i+3}`.
Perfect lower-q1 coverage makes the `Y_i` pairwise distinct.  Hence each
rank-6 target `Y_i` has the unique forced compiler cell `J_i`.

Let `C(R)` be the depth-2 candidate cells of `R`, and let
`Y(R)={Y_i:J_i in C(R)}`.  In the Hall graph, the target set

```text
{R} union Y(R)
```

has neighborhood exactly `C(R)`: `R` has no other candidate cells, and each
`Y_i` has only its forced cell `J_i`.  Therefore

```text
|{R} union Y(R)| = |C(R)|+1 > |C(R)|,
```

which is a Hall obstruction of deficiency one.  Taking all missing roots at
once preserves the same count: add every distinct forced rank-6 neighbour
and its unique cell, obtaining one excess target for each missing root.

At a linear cut, only cells touching the first or last three carrier
positions fail the cyclic erosion identity.  These boundary cells account
for the finite seam exception.

## Exact k=13 audits

The three independently reached q1-hole-four branches instantiate three
different forced-star arities.

| branch | lower-q2 root orbit | forced rank-6 neighbour orbits | Hall targets | depth-2 cells | deficiency |
|---|---:|---|---:|---:|---:|
| A | `233` | `235,745` | 36 | 24 | 12 |
| B | `339` | `467,851,1357` | 52 | 39 | 13 |
| C | `121` | `123,125,249,377,969` | 72 | 60 | 12 |

Branches A and C have one physical rotation rescued by the chosen linear
seam, leaving deficiency 12.  Branch B has no seam rescue and retains all 13
translated stars.

Primary certificates and Hall witnesses:

* `scratch/k13_q1h4_branchA_l3.certificate.json`
* `scratch/k13_q1h4_branchA_l3.alllower_hall.json`
* `scratch/k13_q1h4_branchB_l5.certificate.json`
* `scratch/k13_q1h4_branchB_l5.alllower_hall.json`
* `scratch/k13_q1h4_branchC_l7.certificate.json`
* `scratch/k13_q1h4_branchC_l7.alllower_hall.json`

An additional remote k=11-derived trade moves branch A's root `233` to the
two roots `121,199`.  Its Hall witness has 138 targets and 113 depth-2 cells,
again deficiency 25, exactly one per physical missing root after one seam
rescue:

* `scratch/k13_branchC_q1h4_q2l121_199_res0_k11motif.certificate.json`
* `scratch/k13_branchC_q1h4_q2l121_199_res0_k11motif.hall.json`

## Consequence for search

Lower-q2 defect is not a soft objective and cannot be delegated to the
compiler.  Search states should be ordered lexicographically as follows:

1. exact lower q2;
2. residence at least four;
3. upper-q1 defect;
4. lower-q3/compiler seam quality.

Any move that merely transports a lower-q2 hole (`233 -> 339`, `233 -> 121`,
and so on) changes the shape of the Hall witness but not the obstruction.
The only useful remote bridge is one that eliminates the last root entirely.

## Exact-q2 disconnected model: three cuts suffice to merge

The hard-CNF model

```text
scratch/k13_q1h3_repair_q2res_hamming17_fulllazy.round0.disconnected.json
```

already has three upper-q1 hole orbits and exact lower and upper q2, but its
quotient 2-factor has components of sizes 81 and 51.  Exhaustive enumeration
of the 484 directed endpoint 3-cycles gives:

* 325 circuits meeting both components;
* 131 circuits merging them into one quotient component; and
* 5 merged Hamilton lifts retaining q1 defect three and exact q2 on both
  sides.

The best merge cuts the selected support edges at lower representatives
`599,921,615` and replaces them as follows:

```text
lower 599: {5,7}   -> {7,10}    endpoint 31  -> 106   (component 0)
lower 921: {10,11} -> {10,12}   endpoint 106 -> 119   (component 0)
lower 615: {3,10}  -> {3,4}     endpoint 119 -> 31    (component 1)
```

Thus the support changes form the directed endpoint triangle
`31 -> 106 -> 119 -> 31`.  The merged lift has voltage 1, upper-q1 holes
`255,893,1851`, exact q2, and sole lower-q3 hole `195`.

Artifacts:

* `scratch/k13_q1h3_disconnected_merge_l3.json`
* `scratch/k13_q1h3_exactq2_connected_l3merge.certificate.json`
* `scratch/k13_q1h3_exactq2_connected_l3merge.full_audit.json`

This proves that connectivity is not the remaining obstruction.  The merged
seed's only serious debt is short residence; subsequent exact-q2 endpoint
circuits reduce its quotient residence count from 7 to 3 while also reducing
upper-q1 holes from 3 to 1:

```text
scratch/k13_q1h1_exactq2_connected_res3_l4.certificate.json
```
