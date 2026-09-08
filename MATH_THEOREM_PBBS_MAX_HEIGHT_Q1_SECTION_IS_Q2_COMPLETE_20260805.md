# The PBBS max-height q1 section is q2-complete

**Date:** 2026-08-05  
**Method:** pure symbolic parenthesis matching; no computation or search  
**Status:** unconditional for every `m>=2`.  One globally defined choice of
one occurrence of every rank-`(m-1)` PBBS angle contains, as adjacent chosen
occurrences, a witness for every rank-`(m-2)` target.  Thus the occurrence-
compatibility gate for a q2-complete section is closed on the canonical
PBBS step-two two-factor.  This theorem does not prove that the complement
of the section meets every step-two factor cycle.

## 1. The centered PBBS two-factor and its turn rows

Put

\[
 n=2m+1
\]

and let `f` be the canonical cyclic-parenthesis/PBBS permutation of
`binom([n],m)`.  Consecutive `f`-states are disjoint.  For each middle set
`X`, its two PBBS neighbours are distinct and form the centered Johnson
edge

\[
 e_X=\{f^{-1}(X),f(X)\}.                              \tag{1.1}
\]

Its union is `X^c`; hence the `e_X` form a spanning two-factor of
`J(n,m)` whose rank-`(m+1)` union colours occur exactly once.  Subdividing
`e_X` by `X^c` gives a spanning two-factor of the middle-levels incidence
graph.  The directed successor on its rank-`m` shore is `g=f^2`.

The q1 turn colour at `e_X` is

\[
 K(X)=f^{-1}(X)\cap f(X)\in{[n]\choose m-1}.        \tag{1.2}
\]

Two consecutive q1 turns around a rank-`m` state `A` are the edges centred
at `f^{-1}(A)` and `f(A)`.  Their intersection is

\[
 f^{-2}(A)\cap A\cap f^2(A).                        \tag{1.3}
\]

## 2. The global max-height q1 representative rule

Fix `K in binom([n],m-1)`.  Forward cyclic parenthesis matching leaves
three unmatched zeros.  In cyclic order write

\[
 0_{z_0}E_0\,0_{z_1}E_1\,0_{z_2}E_2,               \tag{2.1}
\]

where each `E_i` is Dyck.  Choose any block of maximum height, call it
`E_i`, and let `w` be the down-step immediately after the rightmost
occurrence of its maximum.

The PBBS first-shadow theorem gives

\[
 f(K+\{w\})=f^{-1}(K+\{z_i\}).                      \tag{2.2}
\]

Consequently

\[
 (K+\{w\})--(K+\{z_i\})                            \tag{2.3}
\]

is a centered edge of (1.1), and its intersection is `K`.  Select this
occurrence.  Make the choice independently for every `K`; ties in (2.1)
may be resolved arbitrarily.  This defines one occurrence of every q1
colour.

The point of the theorem is that these independent choices are nevertheless
coherent at q2.  The q1 blocks forced by the q2 construction below are
uniquely tallest, so no global tie decision enters the proof.

## 3. The canonical q2 witness

Let

\[
 D\in{[n]\choose m-2},\qquad m\ge3.                 \tag{3.1}
\]

Forward matching leaves five unmatched zeros.  Relabel cyclically so that
`D_0` is a block of maximum height `H`:

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2\,
 0_{z_3}D_3\,0_{z_4}D_4.                            \tag{3.2}
\]

Let `u` be the down-step immediately after the rightmost occurrence of
height `H` in `D_0`, and put

\[
 A=D+\{z_0,u\}.                                     \tag{3.3}
\]

The two-sided distinguished-deletion lemma gives

\[
 f^{-2}(A)\cap A=A-\{z_0\}=D+\{u\}=:K_-,           \tag{3.4}
\]

\[
 A\cap f^2(A)=A-\{u\}=D+\{z_0\}=:K_+.             \tag{3.5}
\]

In particular,

\[
 f^{-2}(A)\cap A\cap f^2(A)=D.                     \tag{3.6}
\]

It remains to prove that the global rule of Section 2 chooses both edges
in (3.4)--(3.5).

## 4. The incoming q1 edge is globally selected

Write `D_0^uparrow` for `D_0` with the displayed down-step `u` changed to
an up-step.  The exact deficit-three decomposition of

\[
 K_-=D+\{u\}
\]

is

\[
 0_{z_0}E_0\,0_{z_3}D_3\,0_{z_4}D_4,               \tag{4.1}
\]

where

\[
 E_0=D_0^\uparrow\,0_{z_1}D_1\,0_{z_2}D_2.         \tag{4.2}
\]

Indeed, `D_0^uparrow` is nonnegative and has total height two.  The first
displayed zero lowers its baseline to one, and the second lowers it to
zero, so `E_0` is Dyck.

Changing `u` raises the part of `D_0` after `u` by two.  Since `u` follows
the rightmost old maximum, `D_0^uparrow` has maximum exactly `H+1`.
Inside `D_1` the baseline is one, so its height is at most `H+1`; inside
`D_2` the baseline is zero.  Thus `E_0` has height `H+1`.  The two exterior
blocks `D_3,D_4` have height at most `H`.  Hence `E_0` is the **unique**
maximum-height block in (4.1).

The q1 rule must therefore choose the block preceded by `z_0`.  Its
selected edge has `K_-+{z_0}=A` as one endpoint.  Equation (2.2) then
identifies its centre as `f^{-1}(A)` and its other endpoint as `f^{-2}(A)`.
It is exactly the incoming edge in (3.4).

## 5. The outgoing q1 edge is globally selected

The exact deficit-three decomposition of

\[
 K_+=D+\{z_0\}
\]

is, after a cyclic rotation,

\[
 0_{z_2}D_2\,0_{z_3}D_3\,0_{z_4}E_4,               \tag{5.1}
\]

where

\[
 E_4=D_4\,1_{z_0}D_0\,0_{z_1}D_1.                 \tag{5.2}
\]

This is Dyck.  Its `D_0` segment runs at baseline one, so `E_4` has
height `H+1`, while the two exterior blocks have height at most `H`.
Thus `E_4` is uniquely tallest.

Moreover, the rightmost occurrence of height `H+1` in `E_4` is the
rightmost occurrence of height `H` in `D_0`; it is followed by `u`.
Therefore the q1 rule for `K_+` uses the pair

\[
 K_++\{u\}=A,\qquad K_++\{z_4\}.                   \tag{5.3}
\]

Equation (2.2) identifies its centre as `f(A)` and its other endpoint as
`f^2(A)`.  It is exactly the outgoing edge in (3.5).

The two globally selected q1 occurrences are adjacent around `A`, and
their intersection is `D` by (3.6).

## 6. The boundary case `m=2`

Here the only q2 target is `D=emptyset`.  Number the five cyclic positions
`0,1,2,3,4` and take

\[
 A=\{1,2\},
\]

the rooted word `0 1 1 0 0`.  Its distinguished deletions are the first
and second up-steps, so the two adjacent q1 colours are

\[
 K_-=\{2\},\qquad K_+=\{1\}.                       \tag{6.1}
\]

For `K_-`, the unique nonempty block in its deficit-three decomposition is
the `10` at positions `2,3`, preceded by the unmatched zero at position
`1`.  Its max-height q1 edge therefore contains `K_-+{1}=A`.

For `K_+`, the unique nonempty block is the `10` at positions `1,2`,
preceded by the unmatched zero at position `0`; its down-step is position
`2`.  Its max-height q1 edge contains `K_++{2}=A`.

Thus the two globally selected singleton occurrences are adjacent at `A`
and intersect in the empty target.

## 7. Main theorem and consequence

### Theorem 7.1 (max-height section theorem)

For every `m>=2`, the choices of Section 2 form a q2-complete section of
the lower-turn word of the centered PBBS middle-levels two-factor:

1. exactly one occurrence of every rank-`(m-1)` q1 colour is selected;
2. every rank-`(m-2)` target occurs as the intersection of two adjacent
   selected q1 occurrences.

#### Proof

The first assertion is the construction of Section 2 and the PBBS
first-shadow theorem.  For `m>=3`, Sections 3--5 give an adjacent selected
pair for every `D`; Section 6 handles `m=2`.  `square`

Therefore the independent-transversal/positive-CSP obstruction for section
compatibility vanishes on this explicit two-factor.  To feed the two-factor
Pascal lift, one further graphic condition remains:

\[
 \boxed{\text{the unselected occurrence set must meet every }f^2
 \text{-cycle}.}                                    \tag{7.1}
\]

Condition (7.1) is not proved here.  The PBBS action--angle theorem does
show that every `f`-period is odd, so `f^2` has the same components as `f`
and their number is at most `Cat_m`.  The number of unselected occurrences
is

\[
 {2m+1\choose m}-{2m+1\choose m-1}
 =\frac{2}{m+2}{2m+1\choose m}
 =\operatorname {Cat}_{m+1},
\]

which is larger than `Cat_m`.  This proves scalar capacity for (7.1), not
its componentwise incidence.

## 8. Dependencies and scope

The proof uses only the symbolic statements audited in:

1. `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`, especially the
   max-height q1 construction;
2. `MATH_ATTACK_Y12_DIRECT_ALL_DEPTH_PBBS_DYCK_GATE_20260725 2.md`,
   especially the two-sided distinguished-deletion lemma and complete q2
   construction; and
3. for the final scalar component remark only,
   `MATH_THEOREM_K_ALL_PBBS_ACTION_ANGLE_COMPONENT_CENSUS_AND_SEAM_SLACK_20260731.md`.

It does not prove the cycle-hit condition, the Pascal lift itself, any
q3-or-higher row, residence, or a lower literal compiler.
