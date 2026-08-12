# Audit: BCAP quarantine cascade and boundary-star service

**Date:** 2026-08-06  
**Object:**
MATH_THEOREM_BCAP_QUARANTINE_CASCADE_AND_BOUNDARY_STAR_SERVICE_REDUCTION_20260806.md  
**Verdict:** **PASS AS AN ABSTRACT REDUCTION; BIRTHSTAR AND THE LITERAL
SERVICE ROW REMAIN OPEN.**

## 1. Quarantine

Mate closure is constancy of the live indicator along switch-graph edges.
On a connected graph it is all or nothing. A spanning tree remains
connected, so sparsifying to a generating tree does not avoid the cascade.

## 2. Service normalization

From

\[
 \mathbb E_iZ_{i+1}\le(1-c_sd/X_i)Z_i+B_i+E_i
\]

one obtains

\[
 \sum_i(c_sd/X_i)\mathbb EZ_i
 \le Z_0+\sum_i\mathbb E(B_i+E_i).
\]

Multiplication by \(d/c_s\) gives (2.2), so the required birth scale is
exactly \(\mathsf A/d\).

## 3. Literal service aperture

Under an internal \(C_2/d\) pair cap, use only
\(m=\epsilon d\) blockers. Bonferroni gives
\(c_0\epsilon d-C_2\epsilon^2d/2\), which is positive after choosing
\(\epsilon<c_0/(2C_2)\). Thus the weak pair scale is sufficient.
What remains is to supply or charge such a private subbank for every
asymmetric composite row.

Complete-row first-kill still gives the coefficient of each toggled row,
not the adjoint square of all toggled rows sharing one output.

Lemma 4.1 is algebraically correct, but its positive BMASS input is too
strong. Proposition 4.2 checks the product-residual law exactly:
compensation cancels the \(p^R\) survival probability, leaving absolute
mate-boundary mass \(2w(1-p^{R-s})=\Theta(w)\). Thus the route must retain
signed boundary covariance; an absolute first-kill count destroys the
needed cancellation.

The note retains both as explicit gates and makes no unconditional ANG4
claim.
