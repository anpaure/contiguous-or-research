# K16 WIDTH45: the base scale-two face fails, while a new scale-four dual and parity lock prove 103 cuts

Date: 2026-07-30  
Lane: R  
Status: **exact source-relative theorem; strongest proved WIDTH45/global-Sep5 floor is 103**

## 0. Executive statement

For the frozen K16 length-eight source, consider the complete catalogue of
211,604 direction-coherent, positive-residence-safe seams and the exact
WIDTH45 isolated-seam service interface.  Assume global cyclic five-position
cut separation and endpoint balance.  Then every Boolean selected-seam
circulation that services all 45 lower-q2 and 48 upper-q3 defects has at
least

\[
                              \boxed{103}
\]

selected nonold seams/cuts.

The proof is not a transfer of the base-catalogue floor 104.  The old
scale-two target prices have no WIDTH45 port potential: an exact positive
directed cycle obstructs every such potential.  A different, independently
replayed scale-four certificate gives 102, and a 35-row GF(2) lock excludes
equality.

Consequently the old count-104 two-case split does **not** survive WIDTH45.
At the new scale, count 104 has six restitution types, not two.  No claim of
floor 104 or 105 is made here.

## 1. Exact WIDTH45 service interface

Let `P` be the 12,870 transition ports and `E` the 211,604 directed seams.
The compact binary assigns to every seam `e=(u,v)` its Boolean q<=3 defect
set.  The authenticated WIDTH45 audit adds exactly 150 width-five-only
singleton upper providers.  These records are joined to the binary by the
physical ordered endpoint pair `(u,v)`, not by serialized seam id; 142 of
the 150 serialized ids differ between the two catalogues.

The 150 added records have split histogram

```text
split 2: 75
split 3: 75.
```

Each record has one service activator `w` and three collateral cut positions
`z_1,z_2,z_3`.  Its exact one-occurrence rows are

\[
 w\le x_e,\qquad w+c_{z_j}\le1\ (j=1,2,3),\qquad
 w\ge x_e-c_{z_1}-c_{z_2}-c_{z_3}.                 \tag{1.1}
\]

For every source-cycle position `p`, global Sep5 is

\[
                 \sum_{h=0}^{4}c_{p+h}\le1,        \tag{1.2}
\]

with indices cyclic inside that source component.  If `x_e=1`, (1.2)
forces all three collateral cuts in (1.1) to zero, so `w=x_e`.  Therefore
the fixed augmented Boolean service set `H_45(e)` is exact under (1.2).

Formally, the physical theorem uses Boolean seam and cut indicators
`x_e,c_p in {0,1}` and the incidence links

\[
                         x_{(u,v)}\le c_u,c_v.         \tag{1.3}
\]

Thus selecting a seam marks both deleted endpoint positions as cuts.  Port
capacity is not otherwise assumed in the lower-bound proof.

Under weaker separation, (1.1) remains a fail-closed exact interface for
the listed one-seam occurrences, but compound two-seam width-five windows
have not been enumerated.  Every theorem below is explicitly in the global
Sep5 class.

## 2. Why the base scale-two certificate cannot be imported

The base catalogue has target prices `b_t in {1,2,4}`, total 207, and a port
potential satisfying

\[
 b(H_3(e))\le2+y_v-y_u.                             \tag{2.1}
\]

On the 150 added WIDTH45 columns, the old-potential slack histogram is

```text
-2: 5
-1: 24
 0: 41
 1: 62
 2: 18.
```

Thus 29 individually admissible added columns violate (2.1).  More strongly,
exact difference-constraint closure produces a simple directed 135-cycle
`Z` with

\[
 \sum_{e\in Z}\bigl(b(H_{45}(e))-2\bigr)=15.        \tag{2.2}
\]

If any replacement potential `y'` satisfied the scale-two inequality on all
WIDTH45 arcs, summing it around `Z` would give the left side of (2.2) at most
zero.  Hence:

### Proposition 2.1

For the old 207-price vector, no port potential exists on the unrestricted
WIDTH45 per-arc service graph.

Two independent integer implementations return the same directed 135-cycle
up to cyclic rotation (their seam sets agree exactly).  Its service ledger
covers all 93 defects: 75 once, 15 twice, and the
three targets `46811,56173,60854` five times each.  Its old weighted service
is `285=2*135+15`.

This cycle is not a physical Sep5 counterexample.  It has exactly 15 mutual
Sep5 conflicts, all at source distance three.  The 15 added width-five
occurrences used by it satisfy their own three collateral-zero rows, but the
whole cut set violates (1.2).  Proposition 2.1 therefore rules out the old
**unrestricted per-arc potential class**; it neither refutes a Sep5-aware
dual nor constructs a WIDTH45 carrier.

In particular, the base equality identity `R+S=1` at count 104 is unavailable.
Its no-repeat/one-slack and one-price-one-repeat/tight cases cannot be
transplanted.

## 3. A new exact symmetric scale-four certificate

Rotate the low 15 coordinates cyclically while fixing the distinguished
coordinate.  The 93 defects split into six size-15 orbits and one size-3
orbit.  Assign the following integral prices at denominator four:

| representative | orbit size | price | contribution |
|---:|---:|---:|---:|
| 33337 | 15 | 3 | 45 |
| 33609 | 15 | 4 | 60 |
| 34069 | 15 | 8 | 120 |
| 36343 | 15 | 4 | 60 |
| 36599 | 15 | 3 | 45 |
| 39791 | 15 | 4 | 60 |
| 46811 | 3 | 6 | 18 |

The orbit union is exactly the frozen defect bank, and

\[
                         \sum_t a_t=408.             \tag{3.1}
\]

Exact difference closure gives an integral potential `Phi:P->{0,...,7}`
such that every one of the 211,604 augmented arcs satisfies

\[
       a(H_{45}(e))\le4+\Phi(v)-\Phi(u).             \tag{3.2}
\]

The complete exact slack histogram is

| slack | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| seams | 7742 | 9484 | 10003 | 19880 | 124707 | 20019 | 8489 | 7467 | 2175 | 1081 | 332 | 225 |

### Theorem 3.1 (direct WIDTH45 floor 102)

Let `x_e` be a Boolean balanced seam circulation, linked to Boolean cut
indicators by (1.3), whose global
Sep5 service covers every defect at least once.  Put

\[
 C=\sum_e x_e,\qquad m_t=\sum_{e:t\in H_{45}(e)}x_e.
\]

Then `C>=102`.

### Proof

Write

\[
 s_e=4+\Phi(v)-\Phi(u)-a(H_{45}(e))\ge0.
\]

Multiplying by `x_e`, summing, and using endpoint balance cancels every
potential coefficient.  Hence

\[
4C=\sum_t a_t m_t+\sum_e s_ex_e
    \ge\sum_t a_t=408.                              \tag{3.3}
\]

Thus `C>=102`.  The WIDTH45 interpretation of each added incidence in
(3.3) is justified by (1.1)--(1.2).  QED.

## 4. The exact GF(2) lock excluding equality 102

If `C=102`, equality holds throughout (3.3).  All target prices are positive,
so every target is serviced exactly once, and every selected seam has slack
zero.  Every edge of an integral balanced circulation lies on a directed
cycle.  It is therefore enough to retain tight arcs whose endpoints lie in
one cyclic strongly connected component of the tight graph.

The exact tight census is:

```text
tight arcs:                         7,742
strong components:                 12,490
nontrivial cyclic components:          31
cyclic vertices:                       411
cycle-eligible tight arcs:              438
cycle-eligible tight providers:         321
largest cyclic component:               135
cyclic SCC sizes: 2^3, 5^18, 15^7, 30, 45, 135.
```

Every target has a tight cycle provider, so targetwise SCC absence alone
does not exclude equality.  The decisive lock is

\[
 T=\{33337,33609,57201\}              \tag{4.1}
\]

and

\[
\begin{split}
V=\{&3554,3982,3990,4426,4448,5229,6585,7021,7397,7773,7774,8120,\\
    &8765,8778,9222,9658,10170,10207,10234,10520,10609,10676,11397,\\
    &11551,11553,11682,12554,12557,12560,12563,12566,12569\}.
\end{split}                                             \tag{4.2}
\]

For every one of the 438 cycle-eligible tight arcs `e=(u,v)`, raw replay
checks

\[
  1_{u\in V}+1_{v\in V}
     \equiv |H_{45}(e)\cap T|\pmod2.                 \tag{4.3}
\]

The exact `(boundary parity,service parity)` histogram is

```text
(0,0): 427
(1,1):  11
failures: 0.
```

### Theorem 4.1 (WIDTH45/global-Sep5 floor 103)

Under the hypotheses of Theorem 3.1, `C>=103`.

### Proof

Suppose `C=102`.  Sum (4.3), with selected multiplicities, over the balanced
tight circulation.  Each port in `V` occurs equally often as a tail and a
head, so the left side is zero modulo two.  Equality in (3.3) makes every
target occur once, so the right side is `|T|=3`, which is one modulo two.
Contradiction.  QED.

This proof does not need port capacity: Boolean seam support, endpoint
balance, complete service and global Sep5 occurrence validity suffice.

## 5. Exact remaining equality faces

For any count `C`, define

\[
 R=\sum_ta_t(m_t-1),\qquad S=\sum_es_ex_e.           \tag{5.1}
\]

Then

\[
                       R+S=4C-408.                   \tag{5.2}
\]

At `C=103`, the only possibilities are

```text
(R,S)=(0,4),
(R,S)=(3,1): one extra service of a price-3 target,
(R,S)=(4,0): one extra service of a price-4 target.
```

Three tight parity locks eliminate the last branch.  Their target triples
are

```text
{33337,33609,57201},
{33337,34450,50939},
{33337,36132,60983}.
```

Their common intersection is `{33337}`, whose price is three, not four.
The first two `C=103` branches remain open.  In particular, tight-SCC pruning
cannot be applied to their non-tight seam: tight arcs may traverse the tight
condensation DAG and be returned by that seam.

This warning is quantitatively sharp for the modular relaxation.  Exactly
43 of the 9,484 slack-one seams have a directed tight return.  Pairing them
with the 30 price-three repeat choices gives 1,290 branches.  A full
tight-DAG incidence audit over GF(`p`) for `p=2,3,5,7,11` finds all 1,290
right-hand sides consistent with the necessary signed linear system.  Hence
no modular cycle-space argument closes the
`(R,S)=(3,1)` face; Boolean capacity, global Sep5, or genuine integer-semigroup
structure is required.

The full integral tight-cycle lattice sharpens this negative result.  Its
service lattice in `Z^93` has rank 93 and index four, with Hermite factors
`1^92,4`.  An explicit mod-four quotient has coefficient one on 30 targets,
coefficient two on `{46811,56173,60854}`, and coefficient zero on the other
60.  Every one of the 1,290 slack-one/price-three residual vectors has
quotient zero and belongs to the full integer lattice.  Thus all divisibility
obstructions, not merely the five tested prime fields, are exhausted; any
closure must use nonnegativity, Boolean capacity, or Sep5 geometry.

Two independently implemented one-worker CP-SAT models add Boolean port
capacity and all 12,870 Sep5 rows to this branch.  Both return presolve
`INFEASIBLE` with zero branches.  One uses all 7,742 tight arcs plus the 43
return-capable slack-one arcs; the other uses the equivalent 1,681 cyclic
arcs of the slack-at-most-one graph.  Their equations and status agree, but
no DRAT/LRAT or standalone linear-combination certificate is frozen.
Accordingly this is evidence, not part of Theorem 4.1, and the branch remains
open at theorem level.

At `C=104`, equation (5.2) gives `R+S=8`, with the exhaustive weight types

```text
R=0,3,4,6,7,8 and S=8-R.
```

Here `R=6` may be one price-6 repeat or two additional price-3 service
occurrences, possibly on the same target; `R=8` may similarly be one price-8
repeat or two additional price-4 occurrences.  Thus count 104 has six
numerical types, with subcases, rather than the two base scale-two cases.  The requested
base equality-104 elimination therefore does not survive WIDTH45.

## 6. Audited failed strengthening routes

1. The three price-six targets `46811,56173,60854` have zero exact
   singleton, pair and triple cycle restitution under the scale-four
   potential, both in the all-arc relaxation and in the individually
   Sep5-compatible subgraph, which here equals the full 211,604-arc set.
   The earlier special-cycle-cost method adds nothing to (3.3).

2. All 93 targets are serviceable in tight cyclic SCCs.  The GF(2) lock, not
   targetwise tight-SCC absence, is what raises 102 to 103.

3. A floating direct dual augmented by all 12,870 global Sep5 inequalities
   returns objective 102 with every Sep5 dual price zero.  This is discovery
   evidence only; no rational optimality claim is made.  The exact theorem is
   Theorem 4.1.

4. The two independent C103 price-three/slack-one CP-SAT encodings both die
   in presolve, as described in Section 5.  Without a proof certificate this
   does not raise the exact floor.

## 7. Scope and sharp remaining obstruction

The proved result is source-relative to:

* the frozen length-eight K16 source factor;
* its complete 211,604 direction-coherent seam catalogue;
* the 150 authenticated isolated width-five service occurrences;
* global cyclic Sep5; and
* Boolean seam/cut support, endpoint balance and complete service of the 93 defects.

It omits reverse-edge, q1, survivor, residence, compiler, connectivity and
literal-word rows, so adding those rows cannot weaken the lower bound.  It
does not cover close-cut compound width-five windows, another carrier, or an
unrestricted rethread.

The exact next gate is to settle the two surviving `C=103` branches in
Section 5.  Until that is done, 103 is the strongest exact WIDTH45 floor and
no assertion of 104 or 105 is justified.

## 8. Frozen artifacts

Base scale-two obstruction:

```text
scratch/derive_k16_width45_scale2_potential_20260730.py
  SHA-256 b1c47266840e58868662ae84da1f5a0b655fcf4a288c68a640183574bf71f289
scratch/k16_width45_scale2_potential_20260730.audit.json
  SHA-256 41d2454dd937d14a71e2242ddf21970bcbfc4bb5c7c26735a57eeeb1933860ed
  payload 2cf249b9b27189e987ae31ddc1db7d1bdbadc016358da3ccc5c9cd982c63dd52
scratch/audit_r_k16_width45_direct_scale2_floor104_20260730.py
  SHA-256 824197a46bc4be5088b2ea97d7708149e5acab254d69ba9191c057641cc54682
scratch/k16_width45_direct_scale2_floor104_20260730.audit.json
  SHA-256 f15974be3eeb8ad730c14ce7c21fef036390097d45d968e466bcb2a447c95646
  payload 2c8a529a5ff089a69dca690c476218b8bab075d9a238c0a427647d1267923c88
```

Scale-four certificate and independent floor-103 replay:

```text
scratch/derive_k16_width45_symmetric_scale4_potential_20260730.py
  SHA-256 4d93326fcb0fa7464f66efa30ef17366fe2402c8aa1fac7cc26177501abd63af
scratch/k16_width45_symmetric_scale4_potential_20260730.audit.json
  SHA-256 1b7676e70e209dd2437c042e93eb11a853e35da2899452c1200c188b82d42920
  payload 363ec96250b94db88d907e148ec1317462cf6f5238ccfac94ca15142d93d9456
scratch/audit_r_k16_width45_symmetric_scale4_raw_gf2_frozen_20260730.py
  SHA-256 2298189df06f7ac1cb5c4d8c82b4df99c10990bc7ebc037121bd7fe68425ba26
scratch/k16_width45_symmetric_scale4_raw_gf2_20260730.audit.json
  SHA-256 68c8af66c69a43096392b871e0215130fd0426faed74d0f3961fd6ba78c34c63
  payload 796799562580c0989f351eef36c70d6dff2c10dafda8eaa6025d4345a4bf5d73
scratch/audit_r_k16_width45_symmetric_scale4_raw_20260730.py
  SHA-256 7c3f3d7f300940189ded871dd6b099b3427ffaea4954a045b550f1c419085195
scratch/k16_width45_symmetric_scale4_raw_c103_20260730.audit.json
  SHA-256 784a66aaea470989aacebbf8d0c48885200313ad2ba164289275cea47323009b
  payload eb4da6c93a1e65452f7d196ca87b2c0a795fdc851e1edc4fd76f8b06e41cdc77
scratch/audit_r_k16_width45_c103_modular_dag_20260730.py
  SHA-256 8b174dbb7a43d45253f16115f72186cccbd35fc41f30de21cde03269500ddd0a
scratch/k16_width45_c103_modular_dag_20260730.audit.json
  SHA-256 7539b702ba8cc73d8c0527bd9d6d221b7376968e6c18441925f1377270f2bf90
  payload 317bdd3a97fcf3245f1c0a624798c5f237018dfc27e2ed893f3e5f5d1966c594
scratch/k16_width45_c103_integer_lattice_v2_20260730.audit.json
  SHA-256 b1a24b88f579e69c2a96dbf2ae06e0bf5df95b246b6265d2f41d1dcd17ae438a
  payload 4d25ca32cbd09439261d87fc05e4689658a6d55e9bd7159fbea2a5e85d027ec3
scratch/audit_r_k16_width45_c103_integer_lattice_20260730.py
  SHA-256 d0880e016c2e453b7eb7352d51257540060698087f51681c9709e62adfcf0095
scratch/solve_k16_width45_scale4_c103_price3_slack1_20260730.py
  SHA-256 4031ee835035f1aa53157547268cf8a772c75f134e8ef7a8af0e5bb1a7fbf0c6
scratch/k16_width45_scale4_c103_price3_slack1_20260730.audit.json
  SHA-256 37937e923005909702daac8af777e120d6a31bf9000b9df458ea79ef4fbe0e29
  payload 0660f2ab617322bfa31f09f913f8f4a1917b0365c3272a6f3c84f3a628a44820
scratch/r_k16_width45_c103_branch_b_20260730.audit.json
  SHA-256 be48915b6a2601bdb983d3d1076b6b2e01724d70448cc3bce6523f4cddce5e06
  payload 85ce5213fbf05f6ddd5fdc1a0261028b516cafec31963d25856c595554516fa8
scratch/solve_r_k16_width45_c103_branch_b_20260730.py
  SHA-256 3db882a74a69ba679b63febeb33590b867d72a32ee5d29a74e24175f947813ab
```

The frozen one-lock independent raw replay used one H100 CPU, a 768 MiB
address-space cap, 42,632 KiB maximum RSS and 1.15 seconds elapsed time.  It
independently parses the binary, maps all 150 endpoint pairs, checks all
activator rows, replays all 211,604 integer inequalities, rebuilds tight
SCCs, and verifies the first identity on all 438 cycle-eligible tight arcs.
The three-lock C103 replay used 66,780 KiB and 1.33798 seconds and checks
three identities on those 438 arcs.

Exploratory/negative strengthening artifacts, not theorem certificates:

```text
scratch/k16_width45_scale4_special_cycle_cost_20260730.audit.json
  SHA-256 7866ded48edb079656f88b9659c8bc611b8e05b72019f840870b647e5cc4634f
scratch/k16_width45_sep5_direct_dual_20260730.exploratory.json
  SHA-256 845e216287ae8169f71a345c1559116ffd592425234f8818bb16823c23525cd9
```

Shared frozen inputs:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
scratch/k16_width45_provider_path_dual_20260730.audit.json
  SHA-256 115ce4dfbcfdbd652c0696f21c6f44b5ed58737f16752fa1e5bd203477c12f4a
source factor
  SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```
