# K16 RF495: exact source kernel, three-hole provider normal form, and radius-three no-go

Date: 2026-07-30  
Status: **proved, solver-independent and source-relative; the full tri-window fibre remains open**

## 1. Authenticated source and exact scope

Let `x` be the RF495 length-12,873 word

```text
scratch/k16_rf495_score3_threehole_20260730.word
SHA-256 9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6
```

reconstructed from

```text
scratch/k15_repeatfree_parents_20260730/K15_REPEATFREE_SEED.word
SHA-256 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6

scratch/k16_rf495_score3_20260730.cells
SHA-256 6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

by the exact layout

```text
[4 free] parent[6:6436] [9 free] (0x8000 | parent[7:6432]) [5 free].
```

The eighteen free positions are

```text
A = {0,1,2,3,
     6434,6435,6436,6437,6438,6439,6440,6441,6442,
     12868,12869,12870,12871,12872}.
```

An exact start-by-start OR replay gives precisely the three holes

```text
H1 = 0x18e7,    H2 = 0x3de7,    H3 = 0x9e20.
```

Every theorem below concerns substitutions of `x` at positions in `A`.
It is not an unrestricted length-12,873 or K16 no-go.

## 2. The 70-row fixed-body kernel

The two fixed bodies cover all but 70 nonzero masks.  Let this exact residual
family be `R`, so `|R|=70`.  For `t in R`, let

```text
W_x(t) = {literal source intervals I : OR_x(I)=t}.
```

Every member of `W_x(t)` meets `A`.  For an edit set `P subseteq A`, define

```text
K(P) = {t in R : every I in W_x(t) meets P}.                     (2.1)
```

The empty-family convention is intentional, so all three holes belong to
every `K(P)`.

### Theorem 2.1 (exact active-kernel reduction)

Let `y` agree with `x` outside `P subseteq A`.  Then

```text
y is universal  <=>  y covers every target in K(P).             (2.2)
```

#### Proof

A target outside `R` has a witness wholly inside one fixed body and therefore
avoids all of `A`.  If `t` lies in `R \ K(P)`, a literal source witness of `t`
avoids `P` and is unchanged in `y`.  Thus every target outside `K(P)` is
automatic.  The remaining targets are exactly the rows in `K(P)`, proving
(2.2).

This is the RF495 analogue of the item-1999 source-kernel reduction, but here
the complete fixed-body kernel has only 70 rows.

## 3. Exact source hypergraph and Hall floors

There are two distinct multiplicity censuses; they must not be conflated.

```text
literal source-interval count per target:       0:3, 1:60, 2:6, 3:1
deduplicated A-trace count per target:           0:3, 1:64, 2:2, 3:1
```

The first line counts all 75 literal intervals.  The second first intersects
each interval with `A` and then deduplicates equal traces.

Every one of the 67 nonhole rows has a nonempty trace core

```text
C_t = intersection {I intersect A : I in W_x(t)}.
```

Their size histogram is

```text
|C_t|     1   2   3   4   5   7
count    24  17  18   6   1   1.
```

In the displayed order of the eighteen positions of `A`, the core-incidence
loads are

```text
3,6,8,9,  8,7,7,8,11,11,11,13,14,  11,8,6,4,3.                (3.1)
```

Consequently, if `d(p)` is this load, then the elementary weighted Hall bound
is

```text
|K(P)| >= 3 + ceil((sum_{p in P} d(p))/7).                     (3.2)
```

Indeed, every core meeting `P` supplies a distinct nonhole member of `K(P)`,
while one core contains at most seven charged positions.

The complete 18-bit trace hypergraph gives the much sharper exact minimum
profile:

| `e=|P|` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `min |K(P)|` | 3 | 6 | 8 | 11 | 14 | 17 | 21 | 24 | 28 | 33 |

| `e=|P|` | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `min |K(P)|` | 38 | 41 | 45 | 50 | 53 | 57 | 61 | 65 | 70 |

This table is an exhaustive hit test over all `2^18` subsets, not an
optimization-solver result.  For three sites, kernel sizes range from 11 to
37.  Exactly two supports attain 11:

```text
{0,12871,12872},        {12870,12871,12872}.                    (3.3)
```

## 4. Exact three-hole provider support

For fixed `P subseteq A`, normalize a possible interval witness of target `T`
to a pair

```text
(Q,F),
```

where `Q` is the nonempty subset of `P` lying in the interval and `F` is the
OR of every unchanged interval entry.  This form is feasible for values
`v_p`, `p in P`, exactly when

```text
v_p subseteq T                  for p in Q,
F OR (OR_{p in Q} v_p) = T.                                    (4.1)
```

Intervals with the same `(Q,F)` are logically identical after the inactive
free cells are fixed to their source values and are deliberately collapsed.

### Theorem 4.1 (sharp simultaneous hole-service support)

The minimum number of tri-window cells that can simultaneously service all
three RF495 holes is exactly three.

#### Proof

For one changed site, the 18 supports yield 111 selected normalized
three-form systems; every system has a contradictory bit.  For two sites,
the 153 supports yield 7,702 selected normalized systems; every system is
again bit-infeasible under (4.1).  These are complete finite enumerations of
the exact interval forms, so one and two sites are impossible.

Conversely, choose any three distinct sites and assign `H1`, `H2`, `H3` to
them in any order.  Their singleton intervals supply the three holes.  Thus
every one of the `C(18,3)=816` three-site supports works, proving sharpness.

### Complete singleton provider-site normal form

With hole order `(H1,H2,H3)`, the complete family of ordered distinct
singleton provider-site tuples is

```text
{(p1,p2,p3) in A^3 : p1,p2,p3 are pairwise distinct}.          (4.2)
```

It has

```text
18*17*16 = 4,896
```

members.  The audited catalogue explicitly lists all 4,896 tuples.

For clarity, a second number in the audit counts a different object.  Across
all 816 three-site supports there are

```text
24,215
```

compatible triples of **deduplicated logical forms**

```text
((Q1,F1),(Q2,F2),(Q3,F3)).
```

This is complete after semantic `(Q,F)` normalization.  It is not the number
of raw literal-interval triples, and it is not the number of value
assignments.  No claim equating those three objects is made.  The incidence
patterns `(Q1,Q2,Q3)` and their exact multiplicities are preserved in the
audit and per-support catalogue.

## 5. Solver-free radius-three no-go

Hole service alone is insufficient: changing a site can make some of the 67
source-covered residual rows active.  The exact kernels of Section 3 expose
all such collateral.

First, the interval-form catalogue is exhaustive.  A witness of a residual
target cannot span the first long fixed body because that body has OR
`0x7fff`, contained in no member of `R`; it cannot span the second because
that body has OR `0xffff`.  A residual-compatible fixed extension adjacent
to one free window has length at most seven.  Therefore the frozen
`maxext=40` catalogue of 395 canonical shapes contains every possible
residual witness, with substantial margin.  Exactly 227 of those shapes host
at least one of the 70 residual targets; the other 168 are harmless generic
geometry rows retained by the full compiler.

Fix a three-site support `P={p0,p1,p2}`.  Select one normalized form `(Q,F)`
for every target `T in K(P)`.  Define

```text
U_i = intersection of all selected T with p_i in Q,
R_Q = union of (T \ F) over selected forms having incidence Q. (5.1)
```

### Lemma 5.1 (maximal-intersection identity)

The selected form system has a common nonzero assignment if and only if

```text
U_i != 0                                              for i=0,1,2,
R_Q subseteq OR_{i in Q} U_i       for every nonempty Q subseteq {0,1,2}.
                                                               (5.2)
```

#### Proof

Any realizing value at site `i` is a submask of every target whose selected
form contains that site, hence is a submask of `U_i`.  Every needed bit in
`R_Q` must therefore occur in `OR_{i in Q} U_i`, proving necessity.

Conversely, assign the maximal value `v_i=U_i`.  It has no forbidden bit in
any selected target.  Condition (5.2) supplies every bit absent from the
fixed OR `F`, so (4.1) holds for every selected form.  This proves
sufficiency.

### Theorem 5.2 (exact tri-window radius-three no-go)

No universal word differs from RF495 in at most three of the eighteen
tri-window cells.

#### Proof

One or two sites cannot service the three holes by Theorem 4.1.  For three
sites, enumerate the 816 supports.  For each support compute `K(P)`, order its
11--37 targets by normalized form count, and extend the finite state

```text
(U_0,U_1,U_2,R_1,...,R_7)
```

by one selected form.  Reject a state exactly when (5.2) fails.  Lemma 5.1
shows that this is an exact Boolean-lattice enumeration, not a relaxation.

Every one of the 816 state sets becomes empty.  The optimized ordering has at
most 34 live states at any layer.  Hence every three-site support is
infeasible, completing the proof.

Equivalently, any universal completion inside the RF495 tri-window fibre must
change at least four cells.  This does **not** prove that the full 18-cell
fibre is infeasible.

## 6. Exact normalized full-fibre model

The independently cross-checked exact model for all eighteen free cells is

```text
scratch/k16_triwindow_rf495_lead_20260730/model/model.cnf
SHA-256 2fc9333bc069a60ad85d39a409f35725e1941b66765407cf9b3276ffeff31e7a
```

with semantic map

```text
scratch/k16_triwindow_rf495_lead_20260730/model/model.map.json
SHA-256 af3818bcc249b84cb3f99e8fd0b90aca7c4031e57bd2013570514beb4377a6b0
```

and exact dimensions

```text
70 target rows,
395 canonical interval shapes,
227 residual-relevant shapes,
288 cell-bit variables,
6,081 witness variables,
6,369 total variables,
205,557 clauses.
```

The source-kernel audit independently reconstructs all 395 shapes, all 70
rows, and all 6,081 target--shape hosts before comparing the map.  No solver
verdict is used in this theorem.

## 7. Auditable artifacts and exact boundary

```text
scratch/audit_k16_rf495_source_kernel_radius3_20260730.py
SHA-256 1d0a5c742a99872ce59316c461155edf6494793c07e2c838509fe37982460d24

scratch/k16_rf495_source_kernel_radius3_20260730.audit.json
SHA-256 4b1fcb39813321450fc392c09e96f9a17d406c3db16b1d2bfae2a999cef9ee08
payload SHA-256 f8625aa65885e2b9bf21c6bbc5d806ee0aa993ea781f5fc4c5663a417a8844e8

scratch/k16_rf495_radius3_support_kernel_20260730.catalogue.json
SHA-256 ac7c4511cddf2ebfd478fa238e9be1fafea0fa500940215e09eb5b0dbfdd42b7
payload SHA-256 6a5bbef4bd007a04b22529229be7ac8287ab6752139b217d26b658d962ace8de
```

The catalogue contains all 4,896 ordered distinct singleton provider-site
tuples and one exact kernel/normalized-provider/DP row for each of the 816
three-site supports.

The proved boundary is therefore:

```text
three-hole service distance inside A = 3,
universal completion distance inside A >= 4,
full arbitrary 18-cell RF495 fibre = open in this theorem,
unrestricted length-12873 K16 existence = open.
```
