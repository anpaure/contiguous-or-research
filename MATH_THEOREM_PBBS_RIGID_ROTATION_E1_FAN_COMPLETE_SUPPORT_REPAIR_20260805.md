# The braid and residual seams repair the complete remaining `E_1` inverse fan

**Date:** 2026-08-05  
**Method:** exact q1-row intersection formulas; no computation or search  
**Status:** unconditional target-support theorem for `m>=4`.  Every
correct-rank target in the sole remaining `E_1` inverse-fan orbit of the
rigid full-rotation rethread has an explicit target-equal, equal-width
replacement on either the braid cycle or a seam between two residual
two-soliton blocks.  Together with the preceding block-transport theorems,
the complete named lower whole-fan support and its paired complementary upper
support survive the full rigid orbit.

## 1. The old `E_1` inverse fan

Work on `Z_n`, `n=2m+1`.  Fix the old separator edge `E_1(s)`.  Its central
q1 row is

\[
 R_1(s)=[s+1,s+m-2]\cup\{s+m\},                 \tag{1.1}
\]

where all displayed intervals use the unique local integer lift of length
less than `n`.

For the first `m-3` rows to its left, the rooted `B`-shape formula gives

\[
 H_{s,-j}=[s+j+1,s+j+m]\setminus\{s+m-1\},
 \qquad 1\le j\le m-3.                           \tag{1.2}
\]

For the rows to its right, the rooted `A`-shape formula gives

\[
 H_{s,j}=[s-j+1,s-j+m-2]\cup\{s+m\},
 \qquad 1\le j\le m-1.                           \tag{1.3}
\]

Consequently, for `0<=u<=m-3`,

\[
 R_1(s)\cap\bigcap_{j=1}^{u}H_{s,-j}
   =[s+u+1,s+m-2]\cup\{s+m\},                   \tag{1.4}
\]

and for `0<=v<=m-2`,

\[
 R_1(s)\cap\bigcap_{j=1}^{v}H_{s,j}
   =[s+1,s+m-v-2]\cup\{s+m\}.                   \tag{1.5}
\]

### Lemma 1.1 (complete correct-rank target list)

For

\[
 0\le u\le m-3,qquad 0\le v,qquad u+v\le m-2,
\]

the old inverse-fan target is

\[
 T_s(u,v)
   =[s+u+1,s+m-v-2]\cup\{s+m\}.                 \tag{1.6}
\]

It has width `q=u+v+1` and rank `m-q`.

The only further correct-rank boundary targets are

\[
                         T_s(m-2,0)=\{s+m-2\},    \tag{1.7}
\]

and

\[
                         T_s(m-2,1)=\varnothing.  \tag{1.8}
\]

Every other formal pair with `q<=m` fails the correct-rank condition.

#### Proof

Equations (1.4)--(1.5) give (1.6).  Its interval part has
`m-2-u-v` elements when nonempty, and the separated singleton contributes
one, for total `m-1-u-v=m-q`.  When `u+v=m-2`, only the singleton remains,
still of the correct rank.

At left depth `m-2`, the next predecessor is the `A_(m-1)` row

\[
                         \rho^{s-m-1}K^A_{m-1}.
\]

It retains `s+m-2` and deletes the former common singleton `s+m`, giving
(1.7).  Intersecting the first right row deletes `s+m-2`, giving (1.8).
One additional left step retains `s+m-2`, so the formal left-only depth
`m-1` is not rank zero and is not a named correct-rank corridor.  There are
no other pairs with `u+v+1<=m`.  `square`

## 2. The braid repairs every `v=0` target

On the terminal braid, the rows immediately preceding `R_1(s)` are

\[
 R_0(s+1),R_1(s+2),R_0(s+3),R_1(s+4),\ldots .   \tag{2.1}
\]

For `1<=j<=m-2`, the `j`-th preceding row contains `s+m`.  Its ordinary
interval part starts at `s+j+1`, while the interval part of the central row
ends at `s+m-2`.  Therefore

\[
 R_1(s)\cap\{\text{the preceding `u` braid rows}\}
  =[s+u+1,s+m-2]\cup\{s+m\}.                     \tag{2.2}
\]

### Lemma 2.1

For every `0<=u<=m-3`, the `q=u+1` braid segment ending at `R_1(s)` has
target `T_s(u,0)`.

For `u=m-2`, that braid segment has target the singleton `{s+m}`.  This
will repair the exceptional two-sided case in Section 4.

#### Proof

Equation (2.2) is (1.6) with `v=0`.  At `u=m-2` the interval part is empty
and the common singleton remains.  `square`

## 3. A residual seam repairs every genuinely two-sided interior target

Recall that the final two-soliton residue is concatenated from blocks

\[
                         \cdots W_t,W_{t+3},\cdots . \tag{3.1}
\]

Fix `s`.  At the seam

\[
                         W_{s-4}\mid W_{s-1},      \tag{3.2}
\]

take the final `u+1` `B` rows of `W_(s-4)` and the first `v` `A` rows of
`W_(s-1)`.

For `0<=h<=u`, the selected `B_(m-3-h)` row has root `s+h`, hence is

\[
 [s+h+1,s+h+m]\setminus\{s+m-2\}.                \tag{3.3}
\]

Their intersection is

\[
 [s+u+1,s+m]\setminus\{s+m-2\}.                  \tag{3.4}
\]

The first `v` rows of the next `A` block have intersection

\[
                         [s,s+m-v-2]\cup\{s+m\}.  \tag{3.5}
\]

When `v>=1`, the interval in (3.5) ends no later than `s+m-3`, so the
deleted point `s+m-2` in (3.4) is irrelevant.

### Lemma 3.1 (two-sided seam repair)

For

\[
 0\le u\le m-4,qquad v\ge1,qquad u+v\le m-2,
\]

the `u+v+1` consecutive rows across the seam (3.2) have intersection

\[
                         [s+u+1,s+m-v-2]\cup\{s+m\}
                         =T_s(u,v).               \tag{3.6}
\]

#### Proof

Intersect (3.4) and (3.5).  Their row count is `(u+1)+v=u+v+1`, equal to
the old corridor width, and (3.6) has the required rank by Lemma 1.1.
`square`

## 4. The three endpoint cases

Only three correct-rank targets are not covered by Lemmas 2.1 and 3.1.

1. For `(u,v)=(m-3,1)`, equation (1.6) gives

   \[
                              T_s(m-3,1)=\{s+m\}. \tag{4.1}
   \]

   The `m-1` row braid segment from Lemma 2.1 with parameter `u=m-2`
   has exactly this target and the same width.

2. Equation (1.7) is the singleton `{s+m-2}` at width `m-1`.  The
   all-depth braid interval theorem supplies every singleton cyclic interval
   at width `m-1`, hence supplies this one.

3. Equation (1.8) is the empty target at width `m`.  The braid theorem
   supplies the empty intersection at width `m`.

Thus every boundary case has a target-equal, equal-width replacement.

## 5. Complete fan-support theorem

### Theorem 5.1 (rigid full-orbit whole-fan support)

After applying all `n` rigid clean-`C6` rotations:

1. every named lower whole-fan target formerly carried by the
   single-soliton component has a target-equal, equal-width replacement on
   the braid;
2. every old two-soliton corridor avoiding `E_1` survives literally inside
   a residual block;
3. every correct-rank corridor containing `E_1` has the braid or residual-
   seam replacement constructed in Sections 2--4; and
4. every paired complementary upper target has the corresponding complemented
   replacement.

Hence the full rigid rotation rethread creates **no target-support hole** in
the complete named lower whole-fan bank or its paired upper bank, at any
depth.

#### Proof

Item 1 is the braid interval theorem.  Item 2 is the two-soliton block
transport theorem.  The latter localizes every remaining correct-rank target
to Lemma 1.1; Lemmas 2.1, 3.1 and Section 4 exhaust that list.  Complementing
each replacement proves item 4.  `square`

This theorem is about target support with width retained.  It does not give
the old occurrence addresses back.  An occurrence-capacitated compiler or
typed common-cap router still requires a new integral assignment to the
replacement cells.

## 6. What remains after the support repair

The full rigid rotation orbit now has the following exact ledger:

| gate | status |
|---|---|
| owner, q1, upper-q1, selected q2 | exact throughout |
| complete named lower whole-fan support | exact after rethread |
| paired complementary upper support | exact after rethread |
| occurrence-labelled compiler/cap assignment | open reassignment |
| generalized consecutive source decoration | impossible on this rail |
| arbitrary exterior upper witnesses not in the paired bank | open |
| positive/zero-gap residence on a literal antecedent | open |
| topology | `2` or `4` cycles, not one |
| protected constant-charge opening | open |

Thus the former polynomial two-soliton support leave is zero.  The remaining
obstructions are genuinely physical: source serialization, occurrence
capacity, arbitrary exterior witnesses, residence, and opening.  They are no
longer missing target values in the canonical whole-fan bank.

## 7. Dependencies

This theorem completes the leave isolated in

`MATH_THEOREM_PBBS_RIGID_ROTATION_TWO_SOLITON_BLOCK_TRANSPORT_AND_ONE_ORBIT_LEAVE_20260805.md`.

It uses the braid interval bank from

`MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_ALL_DEPTH_INTERVAL_FAN_TRANSPORT_20260805.md`

and the rooted q1-row formulas from

`MATH_THEOREM_PBBS_CLEAN_C6_Q2_NEUTRAL_GRAPHIC_NEUTRAL_20260805.md`.
