# Audit of conditioned survivor coarea

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_CONDITIONED_SURVIVOR_COAREA_AND_SECOND_INCIDENCE_CODEGREE_GATE_20260806.md`  
**Method:** conditional Bernoulli covariance and anchor enumeration; no
computation or search  
**Verdict:** **PASS AS A RAW-SURVIVOR POSITIVE REDUCTION.  `PINC4` IS A
NEW EXPLICIT PREMISE, NOT A CONSEQUENCE OF CURRENT `ROc`/`FE3`.**

## 1. Correct centering

For every row containing \(x\), conditioning on \(L_x\) removes the
common root \(x\) from its kill event.  Under that law,

\[
 \theta_A=t_A(1-1_{H_A^x}).
\]

The covariance of two centered multipliers is \(t_At_B\) times the
covariance of the two hit indicators.  Dropping the nonpositive product
of their means leaves the simultaneous-hit probability.  Lemma 3.1 is
therefore exact.

Unconditional centering would be weaker: the event that \(G\) consumes
\(x\) makes both hit indicators one, although \(x\) is absent from the
next chi-square sum.  The source correctly avoids that artifact.

## 2. Three-part split

Equation (2.3) is an identity.  Applying
\((u+v+w)^2\le3(u^2+v^2+w^2)\) in the literal \(c'^{-1}\) norm gives
(2.5).  No independence between the row and reference multipliers is
assumed.

More sharply, the current likelihood score \(f_x\) is predictable and
the centered multiplier has conditional mean zero on \(L_x\).  Therefore
its linear cross in the exact chi-square identity vanishes before any
absolute-value estimate.  The norm-square cross with the mean/reference
part costs a factor two, but it does not introduce \(h_i^{-1}\) on
\(\mathcal C_i\).  The constants in (2.9)--(2.11) follow from Young with
\(t=h_i/2\) and pass.

## 3. Coarea enumeration

If \(G\in L_x\) kills both rows, it contains an anchor
\(y\in S_A-\{x\}\) and an anchor \(z\in S_B-\{x\}\).  When they coincide,
the exact total clock rate is \(Y_y\); when they differ, it is
\(Y_{y,z}\).  Summing the two row coefficients gives respectively

\[
 (g_{x,y}^{(2)})^2,
 \qquad
 g_{x,y}^{(2)}g_{x,z}^{(2)}.
\]

The union bound may count a transition several times, but only in the
upper direction.  The row sizes are \(O(d)\); that multiplicity is already
present explicitly in the two anchor sums and is not hidden in the
constant.  Theorem 4.1 passes.

## 4. Denominator and multiplier hypotheses

The proof uses \(t_A\le C_t\) and \(c_x'\ge c_rc_x\) on live outputs.
The deterministic future multipliers are bounded on the ordinary density
stop.  The next-reference lower bound must be included in the common
load/scalar stop; it is not derived by the coarea proof.  The theorem
correctly leaves both as explicit hypotheses.

## 5. Scope of existing ledgers

`ROc`/`FE3` contain one composite coefficient followed by one accepted
edge.  `PINC4` contains a product of two composite-incidence codegrees.
Thus citing the former as a proof of the latter would conflate third and
fourth order.  The conjugate and named subfaces may be removed before
applying `PINC4`, but the arbitrary nonconjugate remainder remains.

## 6. Final audited frontier

The raw survivor fluctuation is now supported only on simultaneous
off-root hits and has the positive codegree upper bound (4.4).  Completing
the direct chi-square route requires:

* the mean/reference hazard rows;
* the next-reference lower stop; and
* the cumulative nonconjugate `PINC4` estimate.

No current theorem supplies the last item.  The reduction is nevertheless
strictly sharper than the undifferentiated adjoint fourth-order kernel and
contains no arbitrary conductance normalization.

The cumulative `PINC4` coefficient is \(1/X_i\), not
\(1/(h_iX_i)\).  This is proof-critical and follows exactly from the
vanishing centered linear cross.  Any later citation with the older extra
service denominator is stale.
