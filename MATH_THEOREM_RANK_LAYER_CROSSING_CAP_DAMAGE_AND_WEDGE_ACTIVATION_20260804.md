# Rank-layer crossing bounds force endpoint-factorized wedge activation

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional rank-layer damage theorem and exact regenerative
state invariant.  It proves endpoint-factorized activation from a bounded-
crossing compensation linkage.  The present all-dimensional construction
does not yet prove the required crossing bound or raw typed endpoint face.

## 0. Main result

Fix \(p\) distinct required lower turns in \(ML_m\), with

\[
                         1\le p\le m-1.
\]

Before a fixed compensation linkage is frozen, suppose the cap state has
the following **raw endpoint face**:

* every lower-to-owner-to-own-q1 direct branch is present;
* its type is legal;
* its only finite capacities are the displayed source, owner, terminal,
  and an explicitly listed branch-local bank; and
* different Boolean owner and terminal values use distinct physical
  capacities on the selected face.

Let the compensation/background linkage consist of \(q\) pairwise
vertex-disjoint paths.  Assume first that it avoids every required lower
source occurrence and every branch-local finite capacity other than the
displayed owner and q1 terminal.  Section 2 restores explicitly priced
side-specific hidden losses.  For a path \(R\), let

\[
\lambda_m(R)=
 \#\{\text{rank-}m\text{ owner capacities used by }R\},
\]

and

\[
\lambda_{m+1}(R)=
 \#\{\text{rank-}(m+1)\text{ q1-terminal capacities used by }R\}.
\]

Assume

\[
 \lambda_m(R)\le\lambda_m,\qquad
 \lambda_{m+1}(R)\le\lambda_{m+1}
 \qquad(R\text{ in the linkage}).
\tag{0.1}
\]

### Theorem

After deleting the compensation linkage, every required lower turn has at
least

\[
                         a_i\ge m-\lambda_mq
\tag{0.2}
\]

owner sides not occupied by it, and at most

\[
                         t_i\le\lambda_{m+1}q
\tag{0.3}
\]

occupied q1-terminal values.

Consequently, if

\[
 \boxed{
 \lambda_mq\le m-p,\qquad
 \lambda_{m+1}q\le m-p-1,
 }
\tag{0.4}
\]

the endpoint-only active-wedge theorem selects a zero-defect protected
wedge router.

In particular, with

\[
                         \lambda=\max(\lambda_m,\lambda_{m+1}),
\]

the single row

\[
                         \boxed{\lambda q\le m-p-1}
\tag{0.5}
\]

suffices.

If every compensation path is strictly rank-increasing on its counted
Boolean-capacity vertices (equivalently, after contracting same-rank
transport which contains no counted owner or q1-terminal capacity), then

\[
                         \lambda_m,\lambda_{m+1}\le1.
\tag{0.6}
\]

Hence \(q=O(d)=O(\sqrt m)\) satisfies (0.4) for all sufficiently large
\(m\).

## 1. Proof of the layer counts

The \(q\) compensation paths are vertex-disjoint.  By (0.1), their union
uses at most \(\lambda_mq\) distinct rank-\(m\) owner capacities.  A fixed
lower turn has exactly \(m\) owner neighbours, so at most
\(\lambda_mq\) of its owner sides are occupied.  This proves (0.2).

Likewise the linkage union uses at most \(\lambda_{m+1}q\) distinct q1
terminal capacities globally.  The number belonging to the q1 terminal
menu of any one lower turn is no larger, proving (0.3).

Under (0.4), equations (0.2)--(0.3) give

\[
                         a_i\ge p,\qquad t_i\le m-p-1.
\]

Apply the endpoint-only active-wedge theorem.

A path which is strictly rank-increasing on counted capacity vertices
visits each Boolean rank at most once, proving (0.6).  Plain nondecreasing
rank is insufficient when one same-rank plateau contains several counted
owner capacities.

## 2. Branch-local hidden capacities

Suppose a path may also delete side-specific guard or flag capacities.
For lower turn \(L_i\), let \(h_i\) be the number of otherwise supported
wedge terminals for which all star-active branches are killed by those
hidden deletions.  Then the exact retained-menu lower bound is

\[
                         |W_i^c|
 \ge B_{a_i}(m)-t_i-h_i,
\tag{2.1}
\]

where \(a_i\ge\max\{0,m-\lambda_mq\}\).  Put

\[
                         \bar a=\max\{0,m-\lambda_mq\}.
\]

Thus the exact endpoint-plus-hidden sufficient row is

\[
 \boxed{
 B_{\bar a}(m)
 -\lambda_{m+1}q-h_i
 >B_{p-1}(m)
 \qquad(1\le i\le p).
 }
\tag{2.2}
\]

The clean row (0.4) is the special case \(h_i=0\).  A hidden resource shared
by many branches cannot be charged once per path; it must be counted by the
number \(h_i\) of wedge terminals whose complete branch menu it kills.

## 3. Exact local state invariant

The preceding proof isolates the smallest endpoint-factorized state
invariant needed at one lift.

### Definition 3.1 (rank-layer exposure invariant)

For every required lower turn \(L_i\), a materialized child state satisfies
\(\operatorname{RLE}(p)\) when:

1. its source occurrence survives;
2. at least \(p\) owner sides are star-active in the same state;
3. among the wedges supported by those sides, at most \(m-p-1\) q1
   terminal values are unavailable;
4. all remaining branch-local hidden-capacity losses are already included
   in the terminal count, so no unpriced branch killer remains; and
5. the owner and terminal occurrence maps are completion-stable and
   value-capacity faithful.

The endpoint-only theorem shows

\[
 \boxed{
 \operatorname{RLE}(p)
 \Longrightarrow
 \text{one zero-defect protected-wedge router}.
 }
\tag{3.1}
\]

The inequalities in items 2--3 are sharp for a pure cardinality proof.

### Regenerative RLE lemma sufficient for the all-\(k\) architecture

A sufficient missing induction statement is:

> At every same-parity Pascal transition, after fixing the transported
> background and one compensation linkage, choose the child cap state and
> the \(p=O(d)\) protected task sources so that \(\operatorname{RLE}(p)\)
> holds; after wedge selection and factor completion, export a state of the
> same kind to the next transition without increasing the hidden-capacity
> casualty bank.

Combined with the other protected carrier/compiler/topology gates, this
would make the one-coordinate common-cap row zero-defect at every
dimension.  The present theorem proves the implication, not this
regenerative premise.

## 4. Why current common-cap theorems do not imply RLE

The existing fixed-compensation model records an arbitrary directed
linkage and deletes its complete physical footprint.  It gives no bound on
\(\lambda_m(R)\) or \(\lambda_{m+1}(R)\).

Indeed, for every \(N\), one directed compensation path may visit
\(N\) distinct rank-\(m\) capacities in sequence.  Attach one private
owner-to-sink route through each visited capacity.  Before compensation
the owner-port rank is \(N\); after freezing that one path it is zero.
Thus

\[
 q=1
 \quad\not\Longrightarrow\quad
 \lambda_mq=O(1)
 \quad\text{or}\quad
 \operatorname{RLE}(p).
\tag{4.1}
\]

This is the sharp snake-path obstruction already present in the suffix
router theory, now expressed at the exact wedge-activation rank layers.

The regular private-port theorem also does not imply RLE.  It starts after
one fixed linkage has been deleted and assumes private prefixes plus the
required residual suffix linkage.  It proves the routing consequence of
those premises; it does not bound the deleted path's layer crossings or
construct star-active direct branches.

Therefore the missing premise cannot be reduced to the number of
compensation claims.  It must control either:

* the rank-layer crossing counts of their complete physical paths;
* the exact local owner/terminal damage in Definition 3.1; or
* the residual full-set owner-port cut from the near-full gammoid theorem.

## 5. Bounded-defect post-factor alternative

If RLE cannot be made exact, the paired-turn deletion theorem gives a
weaker regenerative invariant.  Let \(c_F\) count common-core casualties
and \(s_F\) count side hits after a raw dual-branch lift.  The state
condition

\[
                         c_F+\left\lfloor{s_F\over2}\right\rfloor\le C
\tag{5.1}
\]

leaves at most \(C\) claims.  A nonaccumulating sidecar carrying those
claims is sufficient for \(B(k)+O(1)\).

Thus the exact zero-defect route asks for RLE, while the additive-constant
route only asks for bounded paired casualty plus regeneration.

## 6. Exact scope

The theorem proves endpoint activation from bounded rank-layer crossing
and isolates the exact \(\operatorname{RLE}(p)\) state invariant.

It does not prove that compensation paths can be chosen rank-monotone,
that current flags and terminal types factor through endpoints, or that RLE
regenerates.  The snake-path construction proves these conclusions cannot
follow from path count alone.

## 7. Dependencies

| role | file |
|---|---|
| endpoint-only active-wedge margin | MATH_THEOREM_ENDPOINT_ONLY_ACTIVE_WEDGE_MARGIN_20260804.md |
| paired post-factor deletion | MATH_THEOREM_PAIRED_TURN_DIAMOND_DELETION_AND_MINIMAL_OCCURRENCE_LIFT_20260804.md |
| near-full owner-gammoid alternative | MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md |
| fixed-compensation snake obstruction | MATH_THEOREM_BOOLEAN_JOHNSON_PRIVATE_SUFFIX_RADO_ROUTER_20260803.md |
| regular private-port theorem | MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md |
