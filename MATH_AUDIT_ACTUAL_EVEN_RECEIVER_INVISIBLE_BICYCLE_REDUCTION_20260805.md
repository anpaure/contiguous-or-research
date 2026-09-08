# Audit: actual even receiver Hall to invisible-bicycle escape

**Date:** 2026-08-05  
**Audited reduction:**
`MATH_REDUCTION_ACTUAL_EVEN_RECEIVER_HALL_TO_INVISIBLE_BICYCLE_ESCAPE_20260805.md`  
**Method:** Hall-neighbour and multigraph-rank replay; no computation  
**Verdict:** PASS.  The escape inequality is equivalent to even augmented
Hall, not presently proved from necklace geometry.

## 1. Visible-job cancellation

If `A_j` meets `U`, rectangle completeness puts all of `B_j` inside
`N_G(U)`.  The residual `B`-list is empty.  In the augmented Hall row that
job contributes one private neighbour and one unit of list deficiency;
the two cancel exactly.  The remaining jobs are precisely those whose
`A`-lists avoid `U`.

## 2. Bicircular rank

For lists of size at most two, use one labelled edge per job and one
receiver vertex per surviving option.  An injective endpoint assignment is
an orientation with distinct heads.  A connected component of `e` edges
and `v` vertices assigns `min(e,v)` jobs, so its deficiency is `(e-v)_+`.
This proves the displayed sum and retains parallel edges, loops, empty
lists, and quotient coalescence exactly.

## 3. Kernel replay

A positive nonempty component has cyclomatic number at least two.  Its
minimum-degree-two core contains either a theta, two cycles sharing one
vertex, or two disjoint cycles joined by a path.  Tree branches and
degree-two subdivisions do not change `e-v`.  An empty invisible list is
correctly separated as a zero-vertex one-edge defect.

Distinct passive pairs over one fixed literal hub have disjoint pointed
receiver squares, so a nondegenerate bicycle needs cross-hub incidence or
rotation coalescence.  This statement is deliberately pointed: the audit
does not infer disjointness after quotienting.

## 4. Remaining claim

The unproved row is exactly that every invisible empty job/bicycle unit is
paid by a distinct unit of ordinary Hall slack.  Ordinary Hall of the
sector only says this slack is nonnegative and does not establish the
required domination.
