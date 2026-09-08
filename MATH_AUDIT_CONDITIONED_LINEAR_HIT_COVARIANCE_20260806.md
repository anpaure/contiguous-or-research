# Audit: conditioned linear-hit covariance and two-hit remainder

**Date:** 2026-08-06  
**Object:**
MATH_THEOREM_CONDITIONED_LINEAR_HIT_COVARIANCE_AND_TWO_HIT_REMAINDER_20260806.md  
**Verdict:** **PASS AS AN EXACT REDUCTION; SCOV4 REMAINS OPEN.**

## 1. Sign and conditioning

On \(L_x\),

\[
 \theta_A^G-\mathbb E(\theta_A^G\mid L_x)
 =-t_A\left({\bf1}_{\{n_A^x>0\}}
       -\mathbb E({\bf1}_{\{n_A^x>0\}}\mid L_x)\right).
\]

Thus (1.4) has the correct sign, which disappears after squaring. The
denominator is replaced only after imposing \(c_x'\ge c_rc_x\).

## 2. Linearization

For \(n=0,1\), \(r(n)=0\). For \(n\ge2\), \(r(n)=n-1\) and

\[
 r(n)^2=(n-1)^2\le n(n-1)=2{n\choose2}.
\]

Hence the nonlinear correction is genuinely first-two-hit. The weighted
Cauchy step is

\[
 \left(\sum_Aw_Ar_A\right)^2
 \le\left(\sum_Aw_A\right)\left(\sum_Aw_Ar_A^2\right),
\]

which gives (2.7) with no maximum row count.

## 3. Covariance normalization

The accepted-edge law is \(a_G/X\). Therefore

\[
 \mathbb E[{\bf1}_{L_x}(L^{\rm lin})^2]
 ={1\over X}\sum_{y,z}Y_{y,z\mid\bar x}\lambda_y\lambda_z,
\]

while

\[
 \Pr(L_x)\mathbb E(L^{\rm lin}\mid L_x)^2
 ={1\over XX_x}\left(\sum_yY_{y\mid\bar x}\lambda_y\right)^2.
\]

Their difference is exactly \(X^{-1}\lambda^*K_x\lambda\). There is no
missing factor \(X_x\) or \(X\).

## 4. Nullspace

Within a fixed literal macro stratum, every type count is deterministic.
The covariance between a deterministic count and every incidence
coordinate is zero, so \(K_x^\sigma{\bf1}_T=0\). If macro strata are
mixed, the law of total variance leaves the finite between-stratum term;
the theorem does not silently discard it.

## 5. Scope exclusions

The note does **not** claim:

* that the stopped covariance operator has a dimension-free norm;
* that ROc or FE3 alone proves SCOV4;
* that \(g_x^{(t)}/c_x\) is pointwise bounded; or
* that the centered part of the two-hit remainder is already absorbed.

It proves only that the older positive PINC4 form overcounts a
deterministic fixed-count baseline and that the nonlinear
OR-versus-count error has exactly a two-hit factorial weight.
