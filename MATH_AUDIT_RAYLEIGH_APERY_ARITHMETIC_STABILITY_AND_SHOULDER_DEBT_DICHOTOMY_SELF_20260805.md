# Self-audit: Apéry arithmetic stability and shoulder-debt dichotomy

**Date:** 2026-08-05  
**Method:** pure mathematical audit; no computation or solver  
**Object:**
`MATH_THEOREM_RAYLEIGH_APERY_ARITHMETIC_STABILITY_AND_SHOULDER_DEBT_DICHOTOMY_20260805.md`

## 1. Verdict

**PASS with explicit scope.**  The BV perturbation estimate, positive
small-mesh neighborhood, and either/or shoulder theorem are valid.  The
note does not prove that either defect creates physical Boolean slack.

## 2. Sampling inequality

For `epsilon<=1/2`, the segment between `x_m` and `mh` stays inside the
cell `I_m`.  The elementary BV inequality

\[
 |I|\sup_Iq\le\int_Iq+|I|\operatorname {Var}_I(q)
\]

holds because `sup q <= inf q+Var_I(q)` and
`|I| inf q <= integral_I q`.  The cells for `m>=1` have disjoint interiors.
Also `Var(|f'|)<=Var(f')`.  Thus (1.2) has the stated constant and no
hidden factor depending on the period.

## 3. Rayleigh regularity

The kernel `K` is `C^1` at its matching point `A`.  On each side its
second derivative is Gaussian times a polynomial; it is integrable, and
the finite one-sided second-derivative mismatch gives finite variation of
`K'`.  Hence Lemma 1.1 applies.

## 4. Apéry displacement

Every reduced Apéry weight satisfies `beta_r<=0`, because maximum density
means every reduced denomination weight is nonpositive.  Thus

\[
 |U_m-lambda m|=-beta_{m mod g}\le Delta.
\]

No availability statement is used in Theorem 2.1; it concerns the formal
clock only.

## 5. Comb asymptotic and constants

The endpoint-corrected trapezoidal formula gives

\[
 hC(h)=hK(0)/2+O(h^2),
\]

so `C(h)=K(0)/2+O(h)`.  Since `K(0)>0`, an `h_0` satisfying (3.2) exists.
The definition of `epsilon_0` ensures both the geometric cell condition
and

\[
 epsilon_0B(lambda)<=epsilon_0B_0<=K(0)/16.
\]

This proves (3.5).

## 6. Shoulder sign

The exact conductor identity is

\[
 Phi(V)=Phi(U)+\sum_{m<L}(K(V_m)-K(U_m)).
\]

Replacing the finite correction by minus the sum of its negative parts
gives (0.6).  Therefore if the formal margin is at least `3K(0)/16` but
the actual functional is nonpositive, the adverse shoulder debt is at
least that amount.  The dichotomy direction is correct.

## 7. Exact nonclaims

The theorem does not prove:

1. that `Delta>epsilon_0 lambda` is beneficial rather than adverse;
2. that shoulder debt directly counts unused sockets;
3. positivity for clocks outside the stability ball;
4. the all-price configuration inequality;
5. exact or `O(1)` OR-word constructions.

The Boolean-scale paragraph is conditional on the standard normalization
that multiplies continuum price margin by `W`; it does not replace a
finite-binomial error estimate.
