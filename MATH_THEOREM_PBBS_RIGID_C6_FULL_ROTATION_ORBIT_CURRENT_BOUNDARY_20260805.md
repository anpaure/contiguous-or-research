# The canonical rigid PBBS `C6` is rotation-balanced below the owner layer, but not universally above it

**Date:** 2026-08-05  
**Method:** exact common-history transport plus binary-necklace current
compression; no computation or search  
**Status:** unconditional at the stated local scope.  After the prospective
common-history decoration, the canonical rigid `C6` has zero owner,
immediate-palette, q2, and complete strict-lower current before any rotation
averaging.  A full coordinate-rotation orbit nevertheless has no
context-free all-upper cancellation theorem: an explicit private-prefix
exterior gives a nonzero rank-`(m+2)` necklace current for every `m>=4`.

## 1. Canonical rigid packet

Work on `Z_n`, where

\[
                         n=2m+1,\qquad m\ge4.
\tag{1.1}
\]

The unique q2-neutral clean `C6` through the single-soliton PBBS edge has

\[
 \begin{aligned}
 K&=\{1,2,\ldots,m-2\},& c&=0,\\
 a_0&=m-1,&a_1&=m,&a_2&=m+1.
 \end{aligned}
\tag{1.2}
\]

Put

\[
 R_i=K+a_i,\qquad
 P_i=K+a_i+a_{i+1},\qquad
 Q_i=K+a_i+c,
\tag{1.3}
\]

with indices modulo three.  The packet replaces `P_iQ_i` by
`P_iQ_(i+1)`.

Choose any prospective depth-`d` common-history decoration

\[
                         K=C_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d,
\tag{1.4}
\]

with all `C_j` nonempty.  Such a decoration is a planting datum; an
arbitrary already-frozen PBBS antecedent need not expose it.

## 2. Exact current through every lower depth

### Theorem 2.1

For the decorated canonical packet, each of the following signed currents
is zero occurrencewise or by an explicit occurrence bijection:

1. the owner current;
2. the lower-q1 and upper-q1 currents;
3. the selected q2 current; and
4. the complete strict-lower interval current at every width, hence q3 and
   every deeper lower derivative row.

The strict-lower compiler matching transports through the same bijection.
Consequently every full coordinate-rotation orbit of the packet also has
zero current in these rows.

#### Proof

The owner and two immediate-palette statements are the clean-`C6`
identities.  The common companion deletion `1 in K` makes the q2 turns a
cyclic permutation.  Finally, the fragments

\[
 X_i=(\{c,a_i\}),\quad C_1,\ldots,C_d,\quad
 Y_i=(\{a_{i-1},a_i\})
\tag{2.1}
\]

identify the packet with the inverse three-hinge common-history rethread.
Every strict-lower interval meets at most one screen: an interval meeting
both screens contains the rank-`m` owner `K+c+a_i`.  Left intervals stay
fixed and complete right histories move with their heads, giving the
occurrence-preserving bijection.  Rotating a zero current remains zero.
`square`

Thus the q3 flag current seen in an undecorated frozen exterior is not an
intrinsic obstruction of the rigid `C6`; it disappears under the exact
prospective common-history lift.

## 3. Exact necklace test for a rotation orbit

For any remaining signed literal current

\[
                         \Delta=\sum_S c_S[S],
\tag{3.1}
\]

let `rho` denote cyclic coordinate rotation.  Its full orbit current is

\[
                         \mathcal R\Delta
                         =\sum_{j=0}^{n-1}\rho^j\Delta.
\tag{3.2}
\]

For every binary-necklace class `O`, the coefficient of any member of `O`
in (3.2) is a positive stabilizer factor times

\[
                         \sum_{S\in O}c_S.
\tag{3.3}
\]

Hence (3.2) vanishes exactly when the old-only and new-only targets have
equal signed multiplicity in every necklace class.  Equality of ranks,
ordinary cardinalities, or total positive and negative mass is not enough.

## 4. A sharp private-prefix obstruction at the first upper boundary

The common-history packet is internally exact through source width `d+2`.
The first context-dependent window has width `d+3` and rank `m+2`.

Adjoin the coordinate

\[
                              p=2m
\tag{4.1}
\]

as a singleton left prefix only in role `i=0`.  It occurs nowhere else in
the displayed local exterior.  In one orientation of the rethread the
changed full-window values are

\[
 \begin{aligned}
 T^-&=K\cup\{c,a_2,a_0,p\}
     =\{0,1,\ldots,m-1,m+1,2m\},\\
 T^+&=K\cup\{c,a_0,a_1,p\}
     =\{0,1,\ldots,m,2m\}.
 \end{aligned}
\tag{4.2}
\]

Reversing the PBBS comparison only reverses the sign of this pair.

### Theorem 4.1 (nonzero full-orbit upper current)

The two sets in (4.2) lie in different binary-necklace classes.  Therefore
the full rotation orbit of this decorated canonical rigid packet has
nonzero rank-`(m+2)` upper current in this exterior.

#### Proof

Read cyclic runs of occupied coordinates.  The set `T^+` is one cyclic
run,

\[
                         2m,0,1,\ldots,m,
\tag{4.3}
\]

of length `m+2`.  The set `T^-` has two cyclic runs: one of length `m+1`,

\[
                         2m,0,1,\ldots,m-1,
\tag{4.4}
\]

and the singleton `m+1`.  Cyclic rotation preserves the number and lengths
of runs, so `T^-` and `T^+` are not rotations of one another.

The private-prefix construction changes exactly this displayed first-upper
full window in role zero; the other displayed roles carry no copy of `p`.
Thus its signed necklace vector has coefficient `-1` on the necklace of
`T^-` and `+1` on the necklace of `T^+` (or the opposite signs after
reversal).  By (3.3), rotation averaging cannot cancel either coefficient.
`square`

### Corollary 4.2

There is no context-free theorem saying that the full coordinate-rotation
orbit of the canonical rigid `C6` preserves every arbitrary-width upper
occurrence.  Coordinate rotation moves the defect around its necklace; it
does not turn one necklace into another.

## 5. What rotation can still do

Theorem 4.1 is not a no-go for a completed global word.  A complete upper
target bank can survive by either of two stronger mechanisms.

1. **Uniform bank twist.**  Transport one chosen occurrence of every upper
   target by the same coordinate rotation and reindex the targets.
2. **Protected alternative witnesses.**  Keep a witness for every target
   outside all packet cuts, so the nonzero local occurrence current is not
   a support defect.

What fails is only the weaker claim that orbit averaging of the packet's
local current supplies upper transparency automatically.

## 6. Exact frontier

For the canonical rigid packet with prospective common history:

| row | status |
|---|---|
| owner, lower q1, upper q1 | zero current per packet |
| selected q2 | zero current per packet |
| q3 and every strict-lower row | zero occurrence current per packet |
| strict-lower compiler | exact transported matching |
| source length and positive residence | exact locally |
| arbitrary upper exterior | not rotation-balanced in general |
| typed common cap, zero gaps, protected opening | separate global gates |

Thus the full rotation-orbit idea genuinely closes no additional lower
row: those rows are already exact after common-history decoration.  Its
remaining possible value is global physical handoff/topology or transport
of an independently complete upper bank.  It cannot replace the protected
upper-witness theorem.

## 7. Dependencies and scope

This note uses the exact canonical rigid packet from

`MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`,

the common-history lift from

`MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md`,

and the necklace projection criterion from

`MATH_THEOREM_PBBS_ROTATION_ORBIT_CURRENT_BALANCE_CRITERION_20260805.md`.

It proves neither simultaneous planting of a rotation orbit nor a serial
moving-soliton handoff.  The private-prefix exterior is a universal-claim
counterexample, not an assertion that every natural PBBS exterior has the
same nonzero necklace current.
