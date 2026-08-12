# Every clean PBBS `C6` has a resident upper-monotone `q=3` lift

**Date:** 2026-08-05  
**Method:** exact identification with the resident `q`-port role converter;
no computation or search  
**Status:** unconditional local/prospective theorem.  It converts the direct
shore of any clean Boolean-diamond `C6` into three resident port cycles and
fuses them to one cycle without deleting any target from the complete
**internal cyclic** interval-OR deck.  It does not plant a bank of these
augmented packets in one spanning owner factor, serialize their lower
compiler, or protect a later linear opening.

## 1. Clean `C6` data

Let `K` have rank `r-2`, and let

\[
        a_0,a_1,a_2,c\notin K
\]

be distinct.  Read subscripts modulo three and put

\[
 R_i=K+a_i,\qquad
 P_i=K+a_i+a_{i+1},\qquad
 Q_i=K+a_i+c.                                      \tag{1.1}
\]

The two clean shores are

\[
        E_i=P_iQ_i,
        \qquad
        E_i'=P_iQ_{i+1}.                            \tag{1.2}
\]

This includes every selected common-pivot PBBS connector in the current
hook/profile atlas.  The PBBS common-deletion theorem is an additional
property of those occurrences; it is not needed below.

Fix a source deadline `d>=1`.  Assume

\[
                      r\ge d+3,                     \tag{1.3}
\]

and that the ambient coordinate set has at least `r+d+2` labels.  In the
odd middle-layer setting on `2r-1` labels, both conditions reduce to
`r>=d+3`.

## 2. Exact identification with the three-port converter

Specialize the resident `q`-port construction to

\[
             q=3,\qquad S=K,\qquad z=c.             \tag{2.1}
\]

Its direct port owners are

\[
 A_i=S+z+a_i=Q_i,
 \qquad
 B_i=S+a_i+a_{i+1}=P_i.                             \tag{2.2}
\]

Consequently its old direct phase is

\[
 O=\{A_iB_i:i\in\mathbb Z_3\}
   =\{Q_iP_i:i\in\mathbb Z_3\}
   =\{E_i:i\in\mathbb Z_3\},                       \tag{2.3}
\]

while its new direct phase is

\[
 N=\{A_iB_{i-1}:i\in\mathbb Z_3\}
   =\{Q_iP_{i-1}:i\in\mathbb Z_3\}
   =\{E'_{i-1}:i\in\mathbb Z_3\}.                  \tag{2.4}
\]

Thus the direct part of the resident fusion is **literally the clean
`C6` switch**, with only an index shift and edge orientation suppressed.

Choose `X={x_1,...,x_d} subset K`, retain one anchor in `K-X`, and choose
`d` fresh rail labels `Y={y_1,...,y_d}`.  The inequalities in (1.3) give
exactly the coordinate supply required by the resident `q`-port theorem.
Attach its forward return rail from `B_i=P_i` to `A_i=Q_i` at every port.
Denote by `H_2` the three old rail cycles and by `H_3` their clean-shore
fusion.

## 3. Resident upper-monotone lift theorem

### Theorem 3.1

The states `H_2,H_3` have the following properties.

1. They use the same

   \[
                         3(2d+2)=6d+6              \tag{3.1}
   \]

   rank-`r` owner positions.
2. Their complete owner, lower-`q1`, upper-`q1`, tail and head resource
   signatures are identical and simple.
3. `H_2` consists of three cycles and `H_3` consists of one cycle.
4. Every nonconstant positive coordinate run in either state has length at
   least `d+1`.
5. If `Deck_cyc(H)` denotes the set of unions of all nonempty cyclic owner
   intervals in all components of `H`, then

   \[
                         \boxed{
          Deck_{\rm cyc}(H_2)\subseteq Deck_{\rm cyc}(H_3).}    \tag{3.2}
   \]

In particular the fusion deletes no last internal cyclic witness at any
upper rank or width.

#### Proof

Items 1--4 are Theorems 3.1, 4.1 and 5.1 of
`MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md`, after the
substitution (2.1)--(2.2).  Equations (2.3)--(2.4) identify its direct
replacement with (1.2), so this is a lift of the declared clean `C6`, not
merely an isomorphic ternary polygon.

For item 5, Corollary 6.3 of the same theorem proves support monotonicity
for every `q>=3`.  In the present `q=3` specialization, every interval of
width at most `d+2` is preserved even with multiplicity.  At the first
changed width `d+3`, each old saturated two-active-label value still has
another occurrence, while the three nominal new values coincide in one
three-active-label value with multiplicity three.  Every longer interval
on an old port cycle is already saturated at width `d+2` and retains a
witness after fusion.  This is exactly (3.2).  \(\square\)

### Corollary 3.2 (the private-prefix upper counterexample is not intrinsic)

The rank-`r+2`, width-`d+3` casualty exhibited for a raw common-history
clean `C6` is not forced by its owner/q1 topology change.  After adjoining
the three resident return rails above, the same direct clean shore fuses
three cycles to one and is upper-support monotone at every width.

The price is physical rather than additive: the packet prospectively
reserves `6d+6` already-existing middle-owner positions.  No source letter
is appended by the local replacement.

#### Proof

The raw casualty theorem concerns arbitrary private exterior contexts on
the unaugmented three direct edges.  Theorem 3.1 replaces those contexts by
the explicit saturated resident rails and proves (3.2).  Both states use
the same owner positions, so the replacement has zero length charge.
\(\square\)

## 4. Consequence for the PBBS topology programme

Every literal clean PBBS `C6` in the current action-angle atlas therefore
has two distinct forms.

* The **native form** uses six PBBS incidences.  It is q1/q2-neutral and,
  after common-history decoration, transports every strict-lower
  occurrence and lower compiler edge exactly.  Its arbitrary-exterior
  upper deck need not be safe.
* The **resident port form** uses the same direct shore plus three return
  rails.  It is owner/q1 exact, depth-`d` resident, fuses the same three
  declared direct ports, and is internally upper-support monotone at every
  width.  A terminal lower compiler for the fused state is still required.

Hence the local all-width obstruction and the local residence obstruction
do not have to be paid by a target sidecar.  They can be removed together
by a deterministic `O(d)` protected owner bank.  The surviving theorem is
global:

> Select and plant enough resident three-port lifts on pairwise compatible
> owner/q1 resources, with regenerated parent sockets or a loose-tree
> topology, while leaving one terminal lower compiler and a safe linear
> opening.

This is strictly stronger than asking the raw PBBS clean `C6`s themselves
to be arbitrary-exterior transparent, which is false.

## 5. Scope

The theorem is local and prospective.  It does **not** prove:

1. that the canonical PBBS factor already contains the return rails;
2. that a Catalan-scale bank of `6d+6`-owner packets extends to one spanning
   owner/q1 factor;
3. that fused outputs expose parent-ready copies of the same packet;
4. zero-gap residence;
5. a terminal occurrence-labelled lower/common-cap matching; or
6. preservation of intervals crossing a later cut used to linearize the
   final cycle.

Those are exactly the protected-host, regeneration, compiler and opening
rows.  No `B(k)+O(1)` conclusion is claimed here.

## 6. Dependencies

1. `MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md`;
2. `MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md`;
3. the clean Boolean-diamond normal form used throughout the PBBS connector
   atlas.
