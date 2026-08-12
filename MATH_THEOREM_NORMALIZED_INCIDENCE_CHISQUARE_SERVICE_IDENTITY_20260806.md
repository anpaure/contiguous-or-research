# Normalized incidence chi-square service identity

**Date:** 2026-08-06  
**Method:** exact perspective/Bregman algebra; no computation or search  
**Status:** unconditional identity and proof-safe reduction.  It gives a
direct service potential for `GDIR`, but its nonlinear likelihood bracket
still needs the same rooted-star/selected-relation coefficient control as
the service-damped Duhamel route.

## 1. The exact potential

Fix one resource type.  Let `Y_x>0` be its live root measure and let
`g_x>=0` be the root-omitted potential-incidence measure.  Put

\[
 S=\sum_xY_x,
 \qquad m=\sum_xg_x,
 \qquad \beta={m\over S},
 \qquad c_x=\beta Y_x,
 \qquad e_x=g_x-c_x.
\tag{1.1}
\]

When `m>0`, define

\[
 \boxed{
 \Psi(g,Y)=\sum_x{e_x^2\over c_x}
 ={\mathfrak G\over\beta}.}
\tag{1.2}
\]

Set `Psi=0` when `m=0`.  Thus the `GDIR` integrand is exactly
`Psi/X`.

The potential has two useful equivalent forms.  With

\[
 f_x={e_x\over c_x}={g_x\over\beta Y_x}-1,
\tag{1.3}
\]

one has

\[
 \Psi=\beta\sum_xY_xf_x^2=\sum_xg_xf_x.
\tag{1.4}
\]

If `g_x=sum_{A:x in U_A^circ}mu_A`, then

\[
 \boxed{
 \Psi=\sum_A\mu_A\sum_{x\in U_A^\circ}f_x.}
\tag{1.5}
\]

Although the summands in (1.5) can have either sign, their sum is the
nonnegative chi-square divergence (1.2).

## 2. Ideal service is exact

Let the ideal one-step scaling be

\[
 g\longmapsto ag,
 \qquad Y\longmapsto bY,
 \qquad a,b>0.
\tag{2.1}
\]

Then `beta` scales by `a/b`, `c` and `e` both scale by `a`, and therefore

\[
 \boxed{\Psi(ag,bY)=a\Psi(g,Y).}
\tag{2.2}
\]

For the pair future potential, `a=rho^2` and `b=rho`.  Hence its exact
ideal service is

\[
 (1-\rho^2)\Psi\asymp{\Psi\over X},
\tag{2.3}
\]

which is precisely `GDIR`.  No Johnson Poincare inequality enters this
calculation.

## 3. Exact adapted Bregman identity

Let `(g',Y')` be any next state, define `beta',c',e'` as in (1.1), and
interpret a coordinate with `c'_x=e'_x=0` by continuity.  Relative to the
ideal numerator service `a`, put

\[
 \delta g_x=g'_x-ag_x,
 \qquad
 \delta c_x=c'_x-ac_x.
\tag{3.1}
\]

Then `e'_x=ae_x+delta g_x-delta c_x`.

### Theorem 3.1 (exact chi-square one-step identity)

One has

\[
 \boxed{
 \begin{aligned}
 \Psi(g',Y')-a\Psi(g,Y)
 =\sum_x\Bigg[{}
 &2f_x(\delta g_x-\delta c_x)-f_x^2\delta c_x\\
 &+{\bigl(\delta g_x-(1+f_x)\delta c_x\bigr)^2
       \over c'_x}
 \Bigg].
 \end{aligned}}
\tag{3.2}
\]

#### Proof

Apply, coordinate by coordinate, the exact perspective identity

\[
 { (ae+u)^2\over ac+v}-{ae^2\over c}
 =2{e\over c}u-{e^2\over c^2}v
   +{(u-(e/c)v)^2\over ac+v}
\tag{3.3}
\]

with `u=delta g-delta c`, `v=delta c`, and `f=e/c`.  If the
next coordinate is dead, then `delta g=-ag`, `delta c=-ac`; the square
remainder is zero and (3.3) still holds by its limiting value.  Sum over
`x`.  \(\square\)

Taking conditional expectations in (3.2) gives

\[
 \boxed{
 \begin{aligned}
 \mathbb E_i\Psi_{i+1}-a_i\Psi_i
 ={}&2\sum_xf_x\mathbb E_i(\delta g_x-\delta c_x)
      -\sum_xf_x^2\mathbb E_i\delta c_x\\
 &+\mathbb E_i\sum_x
 {\bigl(\delta g_x-(1+f_x)\delta c_x\bigr)^2\over c'_x}.
 \end{aligned}}
\tag{3.4}
\]

Thus a proof of

\[
 \text{right side of (3.4)}
 \le\eta(1-a_i)\Psi_i+J_i,
 \qquad\eta<1,
\tag{3.5}
\]

immediately gives

\[
 \mathbb E\sum_{i<\tau}{\Psi_i\over X_i}
 \le C\left(\Psi_0+\mathbb E\sum_{i<\tau}J_i\right).
\tag{3.6}
\]

At the complete orbit `Psi_0=0`.

## 4. Scalar beta motion cancels at first order

Let the ideal denominator scaling be `b`, so the ideal beta is
`beta_0'=(a/b)beta`.  Write

\[
 Y'=bY+v,
 \qquad
 \beta'={a\over b}\beta+\eta.
\tag{4.1}
\]

Then

\[
 \delta c={a\over b}\beta v+b\eta Y+\eta v.
\tag{4.2}
\]

Because

\[
 \sum_xY_xf_x=0,
\tag{4.3}
\]

the pure scalar term `b eta Y` vanishes from the linear expression
`sum f_x delta c_x`.  It remains only in the `f^2` coefficient variation
and the quadratic bracket, where it is a scalar future-weight variation
rather than a Johnson-sector perturbation.  Thus a change of total pair
mass cannot by itself create a first-order spatial gradient.

## 5. Relation to the service-damped resolvent

Linearize (3.4) near the balanced state `f=0`.  In the pristine linearized
model used by the existing `JSEC` formulation, the mean incidence response
to a root deviation `u` is represented, up to its already named
hazard/owner remainders, by

\[
 \mathbb E_i(\delta g-\delta c)
 =-{1\over X}\,\beta B u+\text{hazard/owner remainder},
\tag{5.1}
\]

where `B` is the FIFO covariance operator.  Equation (5.1) is recalled as
the input from that model, not proved anew here.  The dangerous linear term is
therefore

\[
 -{2\beta\over X}\langle f,Bu\rangle.
\tag{5.2}
\]

The affine and degree-two counterexamples say `||B||=Theta(d)` on the
corresponding slow sectors; (5.2) cannot be controlled by a scalar
dimension-free Poincare inequality.  Under `PCAP`, however,

\[
 \beta\le C\varepsilon_P/d^2,
\tag{5.3}
\]

so a service-damped Lyapunov with denominator
`X(1-\rho^2)+2\vartheta_s` pays the square of (5.2) at cost
`\beta\widehat\chi_s^2\le C\varepsilon_P` on both `E_1` and `E_2`.  This is the
spectral reason the service-damped Duhamel operator is compatible with the
chi-square identity.

## 6. Exact remaining nonlinear row

The quadratic term in (3.4) is a likelihood-ratio bracket.  The factor
`1+f_x=g_x/(beta Y_x)` shows the real nonlinear boundary:

\[
 \boxed{
 \mathcal Q_i^\chi=
 \mathbb E_i\sum_x
 {\bigl(\delta g_x-(g_x/(\beta Y_x))\delta c_x\bigr)^2
       \over c'_x}.}
\tag{6.1}
\]

An unweighted row-size Cauchy estimate can create the cubic moment

\[
 \beta\sum_xY_x(1+f_x)f_x^2,
\tag{6.2}
\]

which is not bounded by `Psi=beta sum Yf^2` without a likelihood-ratio
cap.  This is why the identity alone is not a `GDIR` proof.

The proof-safe physical split is the same as in the Duhamel note:

* one physical first blocker, including a whole same-resource switch
  star, must be paid by the rooted one-entry square;
* two distinct physical blockers are `FE3`;
* slots, owner-parallel terms, and marked roots retain their named ledgers.

If those coefficient-faithful rows give

\[
 \mathcal Q_i^\chi+
 \left[2\sum_xf_x\mathbb E_i(\delta g_x-\delta c_x)
 -\sum_xf_x^2\mathbb E_i\delta c_x\right]_+
 \le\eta(1-a_i)\Psi_i+J_i
\tag{6.3}
\]

with `eta<1` and total priced `sum J=O(M/d^4)`, then (3.6) proves `GDIR`
directly.  Establishing (6.3) is exactly the coefficient-faithful
selected-relation row; neither ordinary `FE3` marginals nor `PCAP` alone
imply it.

## 7. Proof boundary

The new unconditional content is the exact service law (2.2), the exact
adapted identity (3.2), and the first-order cancellation of scalar beta
motion.  They show that `GDIR` has the right nonnegative Bellman potential
and no intrinsic `d^2` service loss.

The remaining issue is not the affine or degree-two spectrum.  It is the
nonlinear same-first-resource bracket (6.1), with the actual future and
cylinder coefficients.  Until (6.3) is proved, this note does not close
`GDIR` or the bottom theorem.
