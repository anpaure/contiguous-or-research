# Audit of the literal FIFO diagonal chi-square update

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_LITERAL_FIFO_DIAGONAL_CHISQUARE_UPDATE_AND_ADJOINT_FOURTH_ORDER_GATE_20260806.md`  
**Method:** survivor-sum reconstruction, perspective algebra, and an
incidence-process counterexample; no computation or search  
**Verdict:** **PASS AS AN EXACT IDENTITY AND A PROOF-SAFE OBSTRUCTION.
THE FOURTH-ORDER SURVIVOR CARRE REMAINS UNBOUNDED.**

## 1. Survivor updates

Both formulas in (1.7) are definitions of the next available sums.  The
multiplier \(\theta_A^G\) absorbs every deterministic coefficient update
of a surviving composite row, while \(\kappa_E^G\) absorbs the analogous
atomic-edge update.  Hence no approximation is hidden in the conditional
means \(u_x^G,v_x^G\).

The scalar \(r_x^G=(\beta'/\beta)v_x^G\) gives
\(c_x'=r_x^Gc_x\) exactly.  This part passes.

## 2. Diagonal residual algebra

Using \(g=c(1+f)\),

\[
 e'=ug-rc=rcf+g(u-r).
\]

Thus (3.3) is correct.  Squaring in the \(c'^{-1}\) norm gives (3.5), and
the mismatch square is exactly (3.6).  There is no missing factor of
\(r\), \(\beta\), or \(Y\).

## 3. Service constants

Young with \(t=h/2\) gives coefficients

\[
 (1+h/2)(1-h)\le1-h/2,
 \qquad 1+h/2\le3/2,
 \qquad 1+2/h\le3/h.
\]

Therefore (4.2)--(4.3) pass.  Under (4.4), the surviving service
coefficient is

\[
 {1\over2}-{3\over2}\eta_D-3\eta_K.
\]

At \(\eta_D=\eta_K=1/12\), it equals \(1/8\), as claimed.

## 4. Adjoint kernel

Substituting

\[
 h_x=\sum_A\mu_Az_A(x)(\theta_A-r_x)
\]

into \(\sum_xh_x^2/c'_x\) gives (5.2) exactly.  The expression is
positive as a whole although its pairwise summands may be signed.  Calling
it fourth order refers to the two composite-row coefficients; exposing the
accepted transition adds the corresponding first-entry role.

## 5. Factorization obstruction

The toy incidence example has current marginal \(g=Y\), so \(f=0\) and
all complete-row scores vanish.  Killing one privately tagged row changes
only the numerator incidence measure.  Recomputing \(\beta'\) gives the
uniform reference \(c'=(1/2,1/2,1/2,1/2)\), and direct calculation gives
\(\Psi'=2\).  Hence a separate innovation term is logically necessary.

The example does not establish that the actual complete orbit has a large
innovation budget.  It correctly refutes only an identity-level claim that
the entire residual must factor through current conjugate row scores.

## 6. Current proof frontier

The exact remaining quantities are the positive diagonal-service defect
\((D_i)_+\) and the adjoint carré \(K_i\).  Their cumulative scales in
(7.2) suffice for `GDIR`.  Existing complete-row, `ROc`, and `FE3` results
cover named subfaces, but the source record does not bound the residual
nonconjugate pair-of-composite-rows kernel.  The theorem therefore closes
the requested literal formula and isolates, rather than solves, the last
fourth-order estimate.
