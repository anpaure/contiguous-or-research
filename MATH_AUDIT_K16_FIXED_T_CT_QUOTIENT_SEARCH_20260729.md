# Audit of the fixed-`t` even-equivariant `k=16` quotient search

Date: 2026-07-29  
Status: exact-model audit PASS for the declared fixed-schedule central/`q1`
subclass; H100 model builds reproduced.  No SAT point or impossibility result
is claimed.

Audited source:

```text
scratch/k16_even_ct_quotient_search_20260729.py
SHA-256 7ea4038f644138dcbcb6c07b6abb291f37cd600d13ba72a24553b1b1c12fec5d
```

## 1. Exact variable interpretation and wrap

The fixed schedule is a balanced binary word `t` of length `N=858`.  The
Boolean column variable has the exact meaning

\[
 b_{j,x}=c_{j-xN},
 \qquad 0\le j<N,\quad x\in\mathbb Z_{15}.
\]

The quotient successor is

\[
 (j,x)\longmapsto(j+1,x)\quad(j<N-1),
\]

and at the twisted wrap

\[
 \boxed{(N-1,x)\longmapsto(0,x-1).}
\]

This is exactly `T_N=rho T_0`.  Both the model and the independent decoded
audit use the twisted successor; there is no false untwisted closing seam.

## 2. Exact eager constraints

For every quotient column `j`, the model imposes

\[
 \sum_x b_{j,x}=8-t_j.
\]

It reifies every old-coordinate XOR across the true successor and imposes

\[
 \sum_x (b_{j,x}\mathbin{\rm xor}b_{j+1,x})
 =2-|t_{j+1}-t_j|.
\]

Together with the rank equations this is equivalent to the exact start/end
exception table

\[
00,11:(S,E)=(1,1),\qquad
01:(S,E)=(0,1),\qquad
10:(S,E)=(1,0).
\]

The residence clauses are also exact.  For every physical `c` position
`p`, if `c_(p-1)=0,c_p=1`, the clauses force

\[
 c_{p+1}=c_{p+2}=c_{p+3}=1.
\]

Thus every cyclic old-coordinate one-run has length at least four.  The
fixed coarse schedules have `t`-run minima 429, 214, and 143 at `h=1,2,3`,
respectively, so the distinguished coordinate is resident automatically.

For each column the model constructs all fifteen rotations of its old mask
and takes their exact minimum.  Separate `AllDifferent` constraints on the
429 `t=0` columns and the 429 `t=1` columns are equivalent to the two owner
orbit bijections, because the rank-eight and rank-seven actions are free and
have exactly 429 orbits.  The symmetry row `mask[0]=canon[0]` is valid:
global old-coordinate rotation preserves fixed `t`, voltage one, residence,
and every canonical target label.

## 3. Exact `q1` CEGAR

The optional layer reifies every adjacent intersection and union bit and
its canonical old-coordinate orbit.  A target row is

\[
 \operatorname{Element}(w,(q_j)_{j\in J},Q),
\]

which is exactly the disjunction that one eligible seam has canonical label
`Q`.  Rows are persistent.  The four eligible lists are precisely:

- `BB` for lower old rank six;
- `AA` plus cross for lower old rank seven;
- `AA` for upper old rank nine;
- `BB` plus cross for upper old rank eight.

The CEGAR audit adds only genuinely missing target rows, never removes a row,
and treats `UNKNOWN` as failure.  A CP-SAT `INFEASIBLE` status is still a
solver transcript rather than a proof-producing UNSAT certificate.

## 4. The single-run schedule is admissible to the exact master

For `h=1`, the fixed schedule is

\[
 t=1^{429}0^{429}.
\]

Its quotient seam census is 428 `BB` seams, one `10` seam, 428 `AA`
seams, and the twisted closing `01` seam

\[
 A_{857}\longrightarrow \rho(B_0).
\]

The required old-coordinate symmetric-difference sizes are respectively
`2,1,2,1`, exactly as encoded by the rank and Johnson rows.  The two cross
seams contribute the unique balancing insertion and deletion, so

\[
 \sum_j S_j=\sum_j E_j=857;
\]

there is no unmatched voltage or parity event.

There are exactly 429 slots in each middle sector, equal to the 429 free
rank-seven and rank-eight `C_15` orbits.  The four `q1` inventories, ordered
as lower old rank seven, lower old rank six, upper old rank nine, and upper
old rank eight, are

\[
 (430,428,428,430),
\]

against target counts `(429,335,335,429)`.  Thus every palette has nonnegative
raw slack.  Both cyclic `t` runs have length 429.  The old trace has 6435
ones, 6435 zeros, and 857 runs of each kind, so even two-sided length-four
residence is arithmetically compatible because `4*857<6435` on either shore.

Therefore `h=1` has no rank, Johnson, voltage, parity, ownership, residence,
or raw-`q1` obstruction.  This proves admissibility as an exact search fibre,
not feasibility of the simultaneous routing instance.  The command-line
choices for both `build` and `search` have been corrected from `(2,3)` to
`(1,2,3)`.

## 5. Reproduced model sizes

The exact reproduced build artifacts are:

```text
scratch/even_ct_fixedt_h1.base.build.json
SHA-256 b7253f23254f1c4556a146ec4bced94649ad5ba144ac074b6396e48254db970c

scratch/even_ct_fixedt_h1.q1layer.build.json
SHA-256 920c9d13342813c05d5ecd1c89d9f7bbe6e5a274369b7227fc904f9548f6f457

scratch/even_ct_fixedt_h2.base.build.json
SHA-256 4cacbb0a34f051cc824e4d5f0adaa072b3c3b681546a5762bfb551092456f4b9

scratch/even_ct_fixedt_h2.q1.build.json
SHA-256 45786aaab6d77e0c9f635a39c516b5e7c31e336a1ee1cdb88c72349bce166d06

scratch/even_ct_fixedt_h3.base.build.json
SHA-256 2fdd22ea7d5f238f4b6824b83189da839ad9b39296cbd7ab541c0d6b36a55fee

scratch/even_ct_fixedt_h3.q1.build.json
SHA-256 90622b7aa7f61e82adc39a12a9076d46d683c7f0cf79410d0af3d74f900aa99d
```

All three values of `h` have the same proto size:

\[
\begin{array}{c|r|r}
 &\text{variables}&\text{constraints}\\ \hline
\text{base}&39468&79797\\
\text{materialized q1 layer, no target rows}&92664&158733\\
\text{all 1528 target rows possible}&94192&160261.
\end{array}
\]

The base constraints consist of

```text
38610 BoolOr, 40327 linear, 858 MinEquality, 2 AllDifferent.
```

The materialized `q1` layer has

```text
25740 BoolAnd, 64350 BoolOr, 66067 linear, 2574 MinEquality.
```

## 6. Comparison with the variable-`t` circuit master

The companion model

```text
scratch/search_k16_even_equivariant_quotient_cpsat_20260729.py
```

uses all 858 owner-orbit vertices and 54,856 voltage-labelled directed
Johnson arcs.  Before lazy residence cuts its exact proto has

\[
 54857\text{ variables},\qquad1530\text{ constraints},
\]

namely one `Circuit`, one voltage equation, and 1,528 eager `q1` cover rows.
The four target counts are

\[
 429,335,335,429.
\]

Its support sizes range from 18 to 72 on the two hard short-orbit palettes
and from 70 to 72 on the two free-rank palettes.  Exact short `c`- and
`t`-runs produce persistent selected-arc nogoods.

Thus the fixed-`t` model has fewer raw edge decisions in its base but far
more canonicalization variables and constraints.  More importantly, it
fixes the entire balanced block schedule, not merely the number `h` of
distinguished-coordinate runs.  The circuit model searches all schedules
and owner orders and is the structurally stronger global lane.

## 7. Launch recommendation

The variable-`t` circuit should be the primary search.  The exact `h=1`
fixed schedule is now available as a scout; it maximizes both hard-palette
inventories but has only one surplus slot on each 429-orbit cross palette.
This audit builds but does not solve it.  The `h=2` schedule has

\[
 AA=BB=427,qquad AB=BA=2,
\]

so both hard `q1` palettes still retain ample inventory.  The `h=3`
schedule has

\[
 AA=BB=426,qquad AB=BA=3,
\]

and is the next escape if `h=2` stalls or is scoped-infeasible, because its
extra cross seams give more routing flexibility.  Both are far above the
335-orbit hard capacity threshold.  None of these schedules encodes lower `q2/q3`,
arbitrary-width upper coverage, a safe cut, or `COMP_3`.
