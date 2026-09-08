# Every Rayleigh duty-cycle price is positive throughout the Apéry period range

**Date:** 2026-08-05  
**Method:** pure mathematics; exact Fourier, variation, and rational bounds;
no computation, search, or solver  
**Status:** unconditional sign theorem.  For every period no larger than the
Rayleigh minimum and every nontrivial duty cycle, the continuum long-wrap
functional is strictly positive.  Hence no large-period long-wrap Apéry
counterclock exists.  This strengthens the earlier `P<=1/2` theorem.  It
does not give a uniform finite residue-period threshold near the duty
endpoints, sign general primitive multi-kink profiles, or treat finite
availability shoulders.

## 1. Setup and the exact Fourier criterion

Let

\[
 0<P\le\zeta,
 \qquad 0<\alpha<P,
 \qquad \rho={\alpha\over P}.
\tag{1.1}
\]

The continuum long-wrap functional is

\[
 J_P(\alpha)=\int_0^\alpha F_P(x)dx,
 \qquad
 F_P(x)=\sum_{q\ge0}K(qP+x).
\tag{1.2}
\]

Write the duty-cycle price as

\[
 H_{P,\alpha}(x)=\rho x+D_{P,\rho}(x),
\tag{1.3}
\]

where `D` is the nonnegative `P`-periodic triangular tent.  Its mean and
nonzero Fourier coefficients are

\[
 \widehat D_0={P\rho(1-\rho)\over2},
\tag{1.4}
\]

\[
 \boxed{
 |\widehat D_n|
 ={P|\sin(\pi n\rho)|\over2\pi^2n^2}
 \qquad(n\ne0).}
\tag{1.5}
\]

Put

\[
 q(x)=-K'(x),
 \qquad
 M=\int_0^\infty q(x)dx=K(0).
\tag{1.6}
\]

Equal work cancels the linear term, so

\[
 J_P(\alpha)=\int_0^\infty D_{P,\rho}(x)q(x)dx.
\tag{1.7}
\]

## 2. The sharp elementary variation bound

Let

\[
 \varphi(r)=2r e^{-r^2}.
\tag{2.1}
\]

Then

\[
 q(x)=
 \begin{cases}
 \varphi(A-x)-\varphi(A+x),&0<x<A,\\
 -\varphi(A+x),&x>A.
 \end{cases}
\tag{2.2}
\]

### Lemma 2.1 (reflected second-derivative order)

For every `0<x<A`,

\[
 \boxed{
 \varphi''(A+x)>\varphi''(A-x).}
\tag{2.3}
\]

#### Proof

Put `u=x/A` and `h(t)=t exp(-pi t^2/4)`.  Since
`varphi(At)=2A h(t)`, comparison of the two `varphi''` values is equivalent
to

\[
 h''(1+u)>h''(1-u).
\]

The independently proved reflected-curvature lemma gives this strict
inequality for `0<u<=1/2`.  If `1/2<u<1`, then
`1+u>3/2` and `0<1-u<1/2`.  From

\[
 h''(t)={\pi\over2}t\left({\pi t^2\over2}-3\right)
 e^{-\pi t^2/4},
\]

the first value is positive (`pi(3/2)^2>6`) and the second negative
(`pi(1/2)^2<6`).  This proves (2.3). \(\square\)

Consequently `q'` is strictly decreasing on `(0,A)`.  Put

\[
 b_0=q'(0)=2(\pi-2)e^{-\pi/4}>0,
\tag{2.4}
\]

and

\[
 c_0=-\varphi'(2A)>0.
\tag{2.5}
\]

The endpoint values are

\[
 q'(A-)=-2+c_0,
 \qquad
 q'(A+)=c_0.
\tag{2.6}
\]

Indeed, on the tail `x>A` one has

\[
 q''(x)=-\varphi''(A+x)<0,
\]

because `A+x>2A=sqrt(pi)>sqrt(3/2)`.  Thus the compact variation is
`b_0+2-c_0`, the jump has size two, and the tail variation is exactly
`c_0`.  Hence

\[
 \boxed{
 \operatorname {Var}(q')=b_0+4.}
\tag{2.7}
\]

Two bounded-variation integrations by parts now give, for `t!=0`,

\[
 \left|\int_0^\infty q(x)e^{itx}dx\right|
 \le {b_0+\operatorname {Var}(q')\over t^2}
 ={4+2b_0\over t^2}.
\tag{2.8}
\]

Using `pi<22/7` and `exp(-pi/4)<57/125`,

\[
 \boxed{
 4+2b_0=4+4(\pi-2)e^{-\pi/4}
 <4+{1824\over875}
 ={5324\over875}.}
\tag{2.9}
\]

## 3. Exact square-sum control of all tent harmonics

For `x=pi rho in(0,pi)`, the classical cosine series gives

\[
 \boxed{
 \sum_{n\ge1}{\sin^2(nx)\over n^4}
 ={x^2(\pi-x)^2\over6}.}
\tag{3.1}
\]

Indeed, use `sin^2(nx)=(1-cos(2nx))/2` and the fourth Bernoulli-polynomial
Fourier series.  Cauchy--Schwarz and
`zeta(4)=pi^4/90` yield

\[
\begin{aligned}
 \sum_{n\ge1}{|\sin(\pi n\rho)|\over n^4}
 &\le
 \left(\sum_{n\ge1}{\sin^2(\pi n\rho)\over n^4}\right)^{1/2}
 \zeta(4)^{1/2}\\
 &=\boxed{
 {\pi^4\over6\sqrt{15}}\rho(1-\rho).}
\end{aligned}
\tag{3.2}
\]

This retains the exact quadratic vanishing needed at both duty endpoints.

## 4. A rational upper bound for the Rayleigh minimum

### Lemma 4.1

\[
 \boxed{\zeta^2<{2\over3}.}
\tag{4.1}
\]

#### Proof

For `0<x<A`, put `u=x/A`.  Since

\[
 K'(x)=\varphi(A+x)-\varphi(A-x),
\]

one has `K'(x)>0` exactly when

\[
 2\operatorname {arctanh}(u)>\pi u.
\tag{4.2}
\]

Take `x=sqrt(2/3)`.  This lies below `A`, because
`A^2=pi/4>2/3`.  Moreover

\[
 u^2={8\over3\pi}>{28\over33}>{21\over25},
\tag{4.3}
\]

using `pi<22/7`.  The positive power series gives

\[
 {2\operatorname {arctanh}(u)\over u}
 =2\sum_{k\ge0}{u^{2k}\over2k+1}
 >2\sum_{k=0}^{5}{(21/25)^k\over2k+1}
 >{22\over7}>\pi.
\tag{4.4}
\]

The penultimate inequality is a direct rational cross-multiplication.
Thus `K'(sqrt(2/3))>0`.  Since `K'` changes sign only once, from negative
to positive at its minimum `zeta`, (4.1) follows. \(\square\)

## 5. Positivity on the complete normalized period range

The zeroth mode in (1.7) is

\[
 {MP\rho(1-\rho)\over2}.
\tag{5.1}
\]

The Fourier series of `D` is absolutely and uniformly convergent by
(1.5), while `q` is absolutely integrable.  It may therefore be integrated
term by term against `q`.  Pairing frequencies `n` and `-n`, and using
complex conjugacy, reduces the nonzero contribution to the following
absolute bound.

For frequency `t_n=2pi n/P`, equations (1.5), (2.8), and (3.2) bound the
absolute sum of all nonzero modes by

\[
\begin{aligned}
 2\sum_{n\ge1}|\widehat D_n|
 \left|\int q(x)e^{it_nx}dx\right|
 &<{B P^3\over4\pi^4}
 \sum_{n\ge1}{|\sin(\pi n\rho)|\over n^4}\\
 &\le {B P^3\rho(1-\rho)\over24\sqrt{15}},
\end{aligned}
\tag{5.2}
\]

where

\[
 B={5324\over875}.
\tag{5.3}
\]

It remains to compare coefficients.  By (4.1),

\[
 BP^2<{10648\over2625}.
\tag{5.4}
\]

Also `sqrt(15)>387/100` and the authenticated `M>11/125` give

\[
 12\sqrt{15}M
 >{51084\over12500}.
\tag{5.5}
\]

Finally

\[
 {10648\over2625}
 <{51084\over12500}
\tag{5.6}
\]

because cross multiplication gives
`133100000<134095500`.  Therefore

\[
 BP^2<12\sqrt{15}M.
\tag{5.7}
\]

Equations (5.1)--(5.2) now show that the positive zero mode strictly
dominates every nonzero Fourier mode:

\[
 \boxed{
 J_P(\alpha)>0
 \qquad
 (0<P\le\zeta,\ 0<\alpha<P).}
\tag{5.8}
\]

## 6. Consequences and exact boundary

For every fixed `(P,alpha)` in (5.8), the primitive long-wrap clocks

\[
 s_r={r\alpha\over g},\qquad s_g=P
\]

satisfy

\[
 \Phi_g(P,\alpha)
 ={g\over\alpha}J_P(\alpha)+O_{P,\alpha}(1)>0
\]

for all sufficiently large `g`, with a linear reserve.  Thus the continuum
duty-cycle obstruction isolated by the preceding theorem is closed on the
entire period range forced by least-critical first-minimum normalization.

This conclusion is specific to the long-wrap/two-slope price.  Positivity
of `J` does **not** sign:

1. every finite `g` uniformly as `alpha` approaches zero or `P`;
2. a primitive Apéry profile with two or more independent internal kinks;
3. the signed finite-availability shoulder; or
4. the occurrence-faithful Boolean reserve.

Those are separate gates.

## 7. Dependencies

1. `MATH_THEOREM_RAYLEIGH_LONG_WRAP_CONTINUUM_DUTY_CYCLE_DICHOTOMY_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_SMALL_PERIOD_FOURIER_POSITIVITY_20260805.md`;
3. reflected-curvature lemma in
   `MATH_THEOREM_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_ELIMINATION_AND_LONG_WRAP_CURVE_20260804.md`;
4. authenticated rational Rayleigh bounds in
   `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`.
