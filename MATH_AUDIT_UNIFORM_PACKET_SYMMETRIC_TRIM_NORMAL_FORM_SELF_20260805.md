# Self-audit: uniform packet symmetric-trim normal form

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_UNIFORM_PACKET_SYMMETRIC_TRIM_NORMAL_FORM_20260805.md`  
**Verdict:** GO.  The common trim parameter is equivalent to all endpoint
packet rows; the two-role and balanced-width corollaries have the stated
scope.

Let `L=sum a_i`, `U=sum b_i`, `ell_i=b_i-a_i`, and define `p=A-L`.
The lower-endpoint packet row is exactly `p>=0`.  Center equality gives

\[
 B=U-p,
\]

so the job is `[L+p,U-p]` and has width `sum ell_i-2p`.  For socket `i`,

\[
 a_i+\sum_{j\ne i}b_j-A
 =\sum_{j\ne i}\ell_j-p.
\]

Thus all socket polygon rows are precisely

\[
 p\le\sum_{j\ne i}\ell_j.
\]

The strict job-width inequality is `2p<sum ell_i`.  These transformations
are reversible.

For two roles, the socket rows reduce to `p<=ell_1,ell_2`; equality in
both simultaneously is the only degenerate-width endpoint.  If every
socket width is at most half the total, then every `p` below half the total
satisfies every socket row.  Finally, homothetic roles have Minkowski sum
equal to the job interval and hence `p=0`.  No global marginal transport
is inferred, matching the source scope.

