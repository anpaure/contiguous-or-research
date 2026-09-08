# Independent audit: multi-slab cross-SCD sockets and first failing cut

**Date:** 2026-08-04  
**Scope:** line-by-line pure-mathematical audit of
`MATH_THEOREM_MULTI_SLAB_CROSS_SCD_EXACT_HALL_AND_TOP_SLAB_CUT_20260804.md`.
No computation or finite search is used.

## A. Socket histogram

An SCD has `C_b-C_(b-1)` chains beginning at rank `b`: rank `b` is met by
`C_b` chains and rank `b-1` by `C_(b-1)`.  A chain beginning at `b>t=r-d`
uses `r-b` collar targets and leaves capacity `d-r+b=b-t`.  Hence capacity
`u` occurs `H_(t+u)` times.  At `u=d`, this is
`H_r=W-C_(r-1)`.  PASS.

## B. Total capacity

There are `W` owner bins of original capacity `d`.  The collar consumes
exactly one cell for every target in ranks `t,...,r-1`, so unused owner
capacity is `dW-sum_(s=t)^(r-1)C_s`.  Boundary capacity is
`1+...+d=binom(d+1,2)`.  Subtracting the lower demand
`sum_(s=1)^(t-1)C_s` leaves `dW+binom(d+1,2)-Lambda`.  PASS.

## C. Named Hall theorem

For an owner socket, `top(F) subset bottom(D)` is exactly the condition that
the two chains concatenate.  The load inequality reduces to
`|F|<=b-t`.  Distinct sockets enforce chain disjointness at the receiving
level.  Boundary chunks need only respect their clipped capacity.  Hall and
its deficiency formula apply without an omitted side condition.  PASS.

## D. Rank-density thresholds

The number of owner sockets with capacity at least `q` is

\[
 \sum_{u=q}^d(C_{t+u}-C_{t+u-1})=W-C_{t+q-1}.
\]

Adding the `d-q+1` boundary sockets gives the right side of (3.3).  Since
chunk eligibility is the nested condition `a<=u`, threshold cuts are the
complete Hall family for the aggregate transportation graph.  PASS.

The audit confirms the qualification: these aggregate cuts do not imply
the named Hall theorem for one fixed SCD minimum-set family.  The uniform
containment argument is valid only after symmetrizing both SCD roles (or if
an equivalent literal uniformity theorem is separately proved).  PASS.

## E. Maximal-slab obstruction

In a full block `[a,a+d-1]`, exactly the SCD chains beginning at rank at most
`a` traverse all `d` ranks; their number telescopes to `C_a`.  For the top
block `a=t-d=r-2d`.  Load-`d` receiving sockets number
`H_r+1=W-C_(r-1)+1`, proving (4.4).  PASS.

For `k=2r`, `C_(r-1)=rW/(r+1)`, so the socket count apart from the boundary
is `W/(r+1)`.  The local central-binomial estimate
`C_(r-a)/W -> exp(-a^2/r)` for `a=O(sqrt(r))`, together with
`d/sqrt(r)->sqrt(pi)/2`, gives `C_(r-2d)/W->e^(-pi)`.  The claimed linear
failure follows.  PASS.

## F. Scope verdict

For the common-slab strengthening, the audit checks the two decisive cuts.
If `[a,t-1]` is the top slab of length `L`, the top two slabs contribute at
least `C_(t-1)+C_(a-1)` chunks to the `q=1` cut, while exactly `C_a` chunks
from the top slab reach length `L`.  These give (4.9) and (4.10).

On writing `L/sqrt(r)->x` and `A=sqrt(pi)/2`, the offsets from the middle
rank are respectively `A`, `A+x`, and `A-x`, so the Gaussian limits
(4.12)--(4.13) are correct.  The first forces
`x>=sqrt(-log(1-2exp(-pi/4)))-A`.  The function
`f(x)=exp(-(A+x)^2)+exp(-(A-x)^2)` is unimodal because
`A tanh(2Ax)-x` is strictly concave after the origin and has at most one
positive zero.  Both endpoints of the forced interval have `f>1`,
contradicting the second cut.  PASS.

This obstruction assumes common consecutive rank boundaries.  It does not
apply to cuts chosen separately on different SCD chains.  PASS.

## G. Scope verdict

The note proves neither that a chain-adaptive chunking passes (3.3) nor that a
fixed pair of SCDs passes the literal cuts (2.4).  It correctly identifies
the first failure of the canonical maximal-slab scheme and rules out all
common rank-slab grids, without promoting either result to a no-go for the
full chain-adaptive multi-slab programme.  PASS.
