# K16 `G=0x3ccc` return: exact Hall obstruction and minimal upper-repair audit

Date: 2026-07-31  
Scope: the authenticated `G=0x3ccc` return carrier and its complete
three-hole monotone schedule; single path-2-opt upper repairs of span at most
eight.  This note makes no claim about larger, compound, or non-reversal
braids.

## 1. Authentication

The source is

```text
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452
```

Apply these three operations in order.

1. Move the old value `0x29ce` immediately after the value in old row 6478,
   namely `0xb84e`.
2. Move `0x38ce` to the endpoint.
3. Keep the prefix through `0x3ccc` and reverse the strict suffix.

The resulting permutation of all 12,870 rank-eight masks has word-byte digest

```text
6477dd09ef429ae1f76d1a131af98bb0e23264284fd81aedeb846b81d85b5592.
```

Its distinguished positions are

```text
3ccc:1261, 38ce:1262, 89ce:7653, 29ce:7654, b84e:7655.
```

Direct interval replay gives every one of the 11,440 rank-nine adjacent-union
colours.  Among arbitrary upper intervals the only missing masks are

\[
        \mathtt{3cef},\qquad \mathtt{7bce},
\]

both of rank 11.

## 2. Complete schedule and literal scalar budget

The complete finite-state dynamic program over all monotone schedules with
three omitted starts and three omitted deadlines returns maximum selected area

\[
                  A=26408
\]

with displayed maximizing holes

\[
 X=\{12006,12871,12872\},\qquad
 Y=\{0,3684,7657\}.
\]

The nominal omitted-start credit is nine, so the usual scalar upper bound is

\[
                 A+9=26417>26332.
\]

This is not the literal number of available cells.  The last two omitted
starts have only two and one physical prefixes.  Consequently the exact cell
count is

\[
                 26414=26332+82.
\]

Thus three units of the nominal nine-credit budget are boundary-truncated.
The schedule is exact: it has no empty envelope and no failed middle row.  Its
span histogram is

\[
  n_1=3683,\qquad n_2=4836,\qquad n_3=4351.
\]

## 3. Exact lower Hall/DM theorem

For every selected middle row, include all proper-prefix cells of its physical
interval.  For every omitted start, include every physically present prefix of
length at most three.  A lower target is adjacent to a cell exactly when:

1. it is contained in the OR of that cell's envelope values;
2. it meets every envelope value in the cell; and
3. it contains every bit for which this cell contains all physical hosts of a
   required middle-row bit.

These are precisely the individually feasible lower pins for the displayed
schedule.  The resulting bipartite graph has

\[
 |L|=26332,\quad |R|=26414,\quad |E|=363280.
\]

### Theorem 3.1 (fixed-schedule Hall obstruction)

The maximum matching has size

\[
                         25634,
\]

and hence deficiency

\[
                         698.
\]

The five zero-host targets are exactly

\[
 \mathtt{29cc},\quad \mathtt{30ce},\quad \mathtt{38c6},
 \quad \mathtt{8000},\quad \mathtt{898d}.
\]

The alternating Dulmage--Mendelsohn shores have sizes

\[
 |L^+|/|R^+|=4659/3961,
 \qquad
 |L^-|/|R^-|=11702/12482,
\]

while the balanced core has 9971 vertices on each shore.  Thus

\[
 |L^+|-|R^+|=698,qquad
 |R^-|-|L^-|=780,qquad
 780-698=82=|R|-|L|.
\]

In particular, the apparent scalar slack is wholly stored in the backward
surplus shore and does not reach the forward deficit.

The forward shore has 159 ordinary bipartite connected components.  Its
dominant component has size

\[
                       3730/3211
\]

and deficiency 519; its least lower mask is `0x00be`.  The five isolated
`1/0` components are exactly the five zero-host targets.  The complete shape
histogram is

```text
1/0:5, 2/1:2, 3/2:12, 4/3:31, 5/4:37,
6/4:1, 6/5:27, 7/5:1, 7/6:16, 8/7:8,
9/7:3, 10/8:4, 11/9:1, 11/10:1, 12/10:1,
13/11:2, 14/12:1, 15/13:2, 17/14:2,
19/17:1, 3730/3211:1.
```

#### Proof

The schedule is reconstructed from the stated hole sets.  Intersecting every
row over its physical lifetime gives the maximal envelope.  The three
conditions above are necessary and sufficient for an individual cap: (1) is
containment, (2) is nonemptiness at each letter, and (3) is exact middle-row
replay.  Enumerating all nonempty submasks of each cell OR therefore gives the
complete individual-pin graph.

Hopcroft--Karp augmentations occur in rounds of sizes

```text
17359, 6601, 1297, 275, 82, 17, 3,
```

ending at 25,634.  Alternating reachability from every unmatched lower target
gives the forward shore; reverse alternating reachability from every unmatched
cell gives the backward shore.  Each displayed shore identity was checked
directly, including equality of the forward right shore with the full
neighbourhood of the forward left shore.  Connected-component traversal inside
that induced graph gives the stated component census.  This proves the
theorem.  \(\square\)

The conclusion is unconditional for this schedule: no simultaneous choice of
caps can exist when even the individual-pin graph has deficiency 698.

## 4. Minimal single-reversal repair theorem

A path 2-opt with cuts \(a<b\) is

\[
  T_0\cdots T_a\;T_{a+1}\cdots T_b\;T_{b+1}\cdots
  \longmapsto
  T_0\cdots T_a\;T_b\cdots T_{a+1}\;T_{b+1}\cdots.
\]

Its span is \(b-a\).  It changes only the two adjacent-union seams.  Call it
q1-safe when deleting the old two seams and adding the new two leaves every
rank-nine colour represented.

### Theorem 4.1 (minimal 2-opt obstruction)

Among all q1-safe path 2-opts:

1. no move of span at most six supplies either missing upper target;
2. exactly two moves of span seven supply one missing target;
3. each span-seven move creates a new rank-eleven hole, so neither decreases
   the number of upper holes;
4. exactly four moves of span eight strictly decrease the upper-hole count
   from two to one; and
5. every one of these six minimal moves fails the complete scalar gate
   \(A+9\ge26332\).

The exact rows are:

| span | cuts | supplied | resulting upper holes | maximum area |
|---:|---:|---:|---:|---:|
| 7 | 1015,1022 | `3cef` | `6caf,7bce` | 25393 |
| 7 | 12682,12689 | `7bce` | `3cef,7eca` | 26049 |
| 8 | 1016,1024 | `3cef` | `7bce` | 25383 |
| 8 | 10572,10580 | `7bce` | `3cef` | 20381 |
| 8 | 10998,11006 | `3cef` | `7bce` | 21659 |
| 8 | 12680,12688 | `7bce` | `3cef` | 26030 |

In particular, no span-minimal single-reversal upper repair preserves the
scalar lower budget, and hence none can preserve both the scalar budget and
Hall feasibility.

#### Proof

Reversal preserves every interval wholly inside or wholly outside the reversed
block.  It also preserves the OR of every interval containing the whole block.
Therefore a newly supplied upper target must have a witnessing target-facet run
meeting one of the two changed seams.  For each cut pair of span at most eight,
the audit:

1. updates the two old and two new q1 colour multiplicities exactly;
2. keeps the pair iff all 11,440 q1 colours remain;
3. extends the target-contained run maximally across each changed seam and
   tests whether its OR is `3cef` or `7bce`;
4. recomputes all upper interval ORs; and
5. runs the complete three-hole schedule dynamic program on every survivor.

The repair counts by span 2 through 8 are

```text
0, 0, 0, 0, 0, 2, 4.
```

The six rows above are the complete survivor list.  Their maximum area is at
most 26,049, so even the nominal nine-credit upper bound is at most 26,058,
strictly below 26,332.  \(\square\)

## 5. Sharp boundary

The return candidate is valuable as an upper/q1 chronology, but it is not a
compiler-ready carrier under its maximum-area schedule: the Hall loss 698 is
far larger than its literal scalar slack 82.  Moreover, the first one-reversal
upper repairs necessarily destroy scalar feasibility.

What remains open is a larger rethreading which simultaneously:

1. supplies `3cef` and `7bce` without new upper debt;
2. retains at least 26,323 selected area (or an equivalent literal cell
   budget); and
3. transports incidences from the 780-surplus backward shore into the
   698-deficient forward shore.

The theorem does not rule out such a compound braid.

## 6. Reproducibility

```text
scratch/audit_k16_g3ccc_return_hall_and_minimal_upper_repair_20260731.py
SHA-256 00cbbf1773411964deb3f1f731688d43a0a1dde2b43c3b10f938bce2f4941b56

scratch/k16_g3ccc_return_hall_and_minimal_upper_repair_20260731.audit.json
SHA-256 714b7ea02219669acdeca39d9373765678d8885504229c443418e8355298f6a5
payload SHA-256 7ad8f24d61e86004e12f745c96cc35eb590755459069b55fc98bae2f78ac3e80
```
