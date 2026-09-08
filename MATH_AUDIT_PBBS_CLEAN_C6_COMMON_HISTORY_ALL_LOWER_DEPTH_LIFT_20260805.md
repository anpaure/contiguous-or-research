# Audit: clean-C6 common-history all-lower-depth lift

**Date:** 2026-08-05  
**Method:** independent symbolic index, width, rank, and scope audit; no
computation or search  
**Audited theorem:**
`MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md`

## Verdict

**PASS at the stated local scope.**

## 1. Index audit

With `B=K`, hinge label `b=c`, and

\[
 X_i=\{c,a_i\},\qquad Y_i=\{a_{i-1},a_i\},
\]

the common-history fragment `(X_i,C_1,...,C_d,Y_i)` has owners

\[
 Q_i=K+c+a_i,\qquad P_{i-1}=K+a_{i-1}+a_i.
\]

Replacing `Y_i` by `Y_(i+1)` changes the second owner to `P_i`.  Hence the
head-rethread direction has edges `Q_iP_(i-1) -> Q_iP_i`; reversing it gives

\[
 \{P_iQ_i\}_i\longrightarrow\{P_iQ_{i+1}\}_i,
\]

exactly the clean C6.  There is no off-by-one or orientation error.

## 2. Parameter audit

The required labels are `K` plus `a_0,a_1,a_2,c`, exactly `r+2`
coordinates.  The hinge theorem requires `r+c_hinge-1=r+2` for three
hinges, so the ground-set bound is exact.  An ordered nonempty depth-`d`
partition of `K` exists exactly under `d<=r-2`, which is stated.

The common q2 pivot coordinate may lie in any one `C_j`; no identity uses
its position, so the PBBS q2 proof and source-history proof coexist.

## 3. Lower-deck audit

Every interval meeting both screens contains all of `K` and one two-label
screen, hence contains a rank-`r` owner.  Therefore every rank-below-`r`
interval is one-sided.  The literal left-fixed/right-permuted mapping is
bijection-valued on physical occurrences, not merely target supports.

At depth `d`, the q1, q2, q3, ... rows are source widths

\[
 d,d-1,d-2,\ldots,1.
\]

All lie in the proved deck.  Composition of occurrence bijections proves
serial exactness without assuming disjoint moves.  Literal availability of
each intermediate decorated move remains an explicit planting hypothesis.

## 4. Compiler and residence audit

An occurrence-labelled lower matching transports along a bijection and
therefore retains injectivity and every target-cell incidence determined by
the transported literal cell.  The theorem correctly excludes additional
cap flags, typed sinks, shared capacities, and state-dependent zeros.

Every source occurrence lies in `d+1` cyclic owner windows.  This proves
positive-run residence only.  The endpoint collar and zero-gap caveats are
necessary and are stated.  The head permutation preserves source count and
the source-letter multiset, so zero length charge is exact.

## 5. Sharp upper boundary audit

Widths at most `d` are covered by the short-deck bijection.  Width `d+1`
is the owner pair and width `d+2` is the full internal hinge value; both
multisets are exact.  Adding one fresh singleton left context creates width
`d+3` values

\[
 K+c+a_{i-1}+a_i+p_i
 \quad\hbox{versus}\quad
 K+c+a_i+a_{i+1}+p_i.
\]

They have rank `(r-2)+4=r+2`.  Since `p_i` is private and the new role lacks
`a_(i-1)`, the old value has no new local occurrence.  Thus the asserted
first possible failure is real and sharp relative to the internal theorem.

Every changed old crossing interval contains the old rank-`r+1` full-hinge
union, proving the three-cone localization.  The theorem correctly does not
turn that exponential cone bound into an `O(1)` sidecar.

## 6. Scope audit

Proved:

1. exact q3 and all lower depths after prospective common-history
   decoration;
2. exact serial lower-deck and lower-matching transport;
3. positive residence and zero source-length charge; and
4. a sharp width-`d+3` context counterexample to local all-upper
   transparency.

Not proved:

1. that every already frozen PBBS occurrence exposes this antecedent;
2. simultaneous protected planting for a global loose forest;
3. arbitrary upper witness survival outside the local packet;
4. zero-gap residence;
5. a typed/shared common-cap router; or
6. `nu(k)=B(k)+O(1)`.
