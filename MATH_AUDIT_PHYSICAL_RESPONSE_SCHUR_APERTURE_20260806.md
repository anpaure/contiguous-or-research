# Audit of the physical-response Schur aperture

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_PHYSICAL_RESPONSE_SCHUR_APERTURE_AND_ACTUAL_VECTOR_GATE_20260806.md`  
**Method:** weighted Cauchy--Schwarz, coefficient-scale audit, and minimal
matrix counterexamples; no computation or search  
**Verdict:** **PASS AS A SUFFICIENT OPERATOR/ACTUAL-VECTOR THEOREM.  THE
FIFO RESPONSE EXPANSION REMAINS ABSENT, SO THIS DOES NOT CLOSE `GDIR`.**

## 1. Weighted Schur calculation

For each output \(y\),

\[
 \left(\sum_br_{yb}q_b\right)^2
 \le\left(\sum_bu_{yb}s_{yb}\right)
      \left(\sum_bu_{yb}q_b^2/s_{yb}\right).
\]

The first maximum in (2.1) pays the output denominator \(c'_y\); after
summing outputs, the second maximum pays each input coefficient \(w_b\).
Therefore the product \(AB\), rather than either factor separately, is
the exact Schur constant.  Theorem 2.1 passes.

## 2. Sufficiency of the actual-vector form

The direct chi-square theorem uses the physical response only at the one
current vector \(q_i\).  Consequently `(AVA)` is sufficient; no
polarization or all-vector extension is used afterward.  Splitting
\(h=Rq+r\) with the factor-two inequality produces

\[
 H_i\le2C h_i(\beta_Td/X_i)\mathcal E_i^{\rm row}
       +2\eta_0h_i^2\Psi_i+2h_iJ_i.
\]

The service threshold in the parent theorem is \(\eta<1/4\), so
\(\eta_0<1/8\) is correct.  This implication passes.

## 3. Coefficient scale

The complete-row ledger is weighted by \(\beta_Td/X_i\).  The mismatch
recurrence divides by \(h_i=1-a_i\).  Thus the local response must carry

\[
 h_i\beta_Td/X_i.
\]

On the stopped clock this is \(\Theta(\beta_Td/X_i^2)\).  The source has
the same factor.  No factor of \(X_i\), \(d\), or \(\beta_T\) is missing.

## 4. Current model audit

The existing first-kill theorem defines \(w_b\) exactly, and the
complete-row theorem defines and pays \(q_b^2\).  Neither theorem expands
the next normalized incidence residual as a matrix applied to \(q\).
The Bregman note defines the aggregate differences \(\delta g,\delta c\),
but does not disintegrate them into the occurrence-labelled first-entry
coordinates with the same \(w_b\).

Therefore the statement that the current FIFO model satisfies `(AVA)` or
`(SCHA)` would be unsupported.  The theorem correctly marks (6.1) as the
next required literal identity.

## 5. Counterexamples

The one-entry example proves that support size, even support one, gives no
small coefficient.  The rank-one example has normalized trace \(1/n\)
but operator norm one, proving that an orbit-average scalar does not imply
the response aperture.  Both calculations are exact and use positive
reference/input weights.

These examples do not refute the actual FIFO geometry.  They verify the
logical claim that the currently listed scalar and support hypotheses are
insufficient.

## 6. Final audited frontier

The weakest sufficient remaining statement is the actual-vector response
inequality `(AVA)`, after the literal decomposition (6.1).  A weighted
Schur claim ledger is a transparent stronger route.  The response entries,
not their asymptotic bound, are currently missing from the source record.
No auxiliary normalization theorem is needed once that expansion and one
of these apertures are proved.
