# Audit of the endpoint-critical all-row odd tropical hierarchy

**Date:** 2026-08-12
**Audited file:**
`MATH_THEOREM_ENDPOINT_CRITICAL_ALL_ROW_ODD_TROPICAL_HIERARCHY_20260812.md`
**Verdict:** **PASS self-audit.**  The greedy grouping, inverse formula,
and Stieltjes constants all retain literal physical availability.  The note
does not prove the final signed inequality.

## 1. Greedy block count

For total \(m<(q+1)n\), greedily maximal blocks have size at most \(n\).
If there were \(2q+2\) blocks, each pair consisting of an odd block and
its successor would have total greater than \(n\), because even the first
part of the successor could not be added to the odd block.  The first
\(2q+2\) blocks would therefore exceed \((q+1)n\).  Hence there are at
most \(2q+1\) blocks.  Internal superadditivity collapses each block.

At the boundary \(m=(q+1)n\), density gives the upper bound \(q+1\), and
\(q+1\) endpoint parts attain it.  Since \(q+1\le2q+1\), including at
\(q=0\), the same formula holds.  This separately handles the only point
where greedy grouping could require \(2q+2\) blocks.

## 2. Inverse formula

The first hit of level \(q+z\), \(0<z<1\), lies strictly above \(qn\) by
density and no later than \(qn+C_0(z)\) by using \(q\) endpoint parts.
It is therefore in the row to which the grouping theorem applies.  Every
continuous reward tuple in the inverse minimum produces literal parts via
the left inverse \(C_0\); conversely the grouped first-hit partition gives
one admissible reward tuple.  These two maps give the opposite inequalities
and hence equality.  Repeated phases and zero padding are harmless.

Subtracting \(n(q+z)\) gives the overshoot term in the tropical formula.
That term is nonnegative and cannot be dropped.  The direct and equal-part
bounds use tuples whose reward sums equal exactly \(q+z\).

## 3. Complete functional

Writing \(m=qn+r\), \(0\le r<n\), partitions every clock index exactly
once.  The head kernel is \(1-B(v_r)\).  For \(q\ge1\), the outer kernel is

\[
 -f(1+q+P_q(r)).
\]

Stieltjes integration gives \(n\int\phi-\sum\phi\) in every row.  The
identity

\[
 B(y)+\sum_{q\ge1}f(q+1+y)
 =e^{-a(1-y)^2}+\sum_{\ell\ge1}e^{-a(\ell+y)^2}
\]

has integral one.  Consequently the baseline constants sum to \(n\), not
to zero, and reproduce the literal head constant exactly.  Gaussian decay
and \(0\le U_q\le n\) justify termwise integration.

## 4. Saturation and scope

Lowering an unconstrained late head phase preserves the table polytope,
weakly lowers every max-plus Bellman value, and therefore weakly lowers
every outer-kernel term.  Its own compact term decreases strictly on the
post-minimum branch.  This proves the late additive/plateau saturation for
the complete functional.

For an upward unit perturbation at coordinate \(j\), the directional
derivative of a maximum of partition-linear forms is the maximum number of
\(j\)-parts among its active optimizers.  Strict outgoing
superadditivity ensures that no other head index has nonzero derivative.
The endpoint lower bound \(L(m)\ge\lfloor m/n\rfloor\), together with the
linear bound on multiplicity, makes the Gaussian occupation series
absolutely convergent.  Hence termwise one-sided differentiation is valid
and gives the stated occupation-compensation inequality.

The rowwise certificate is an integer semigroup statement only for scalar
size/reward signatures.  It supplies neither named target disjointness nor
packet topology.  The remaining analytic gate is the sign of the exact
odd-tropical series, while protected rail normality remains a separate
multidimensional gate.
