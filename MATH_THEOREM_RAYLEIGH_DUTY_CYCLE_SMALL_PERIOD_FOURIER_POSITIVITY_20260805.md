# Rayleigh duty-cycle prices are strictly positive for every period at most one half

**Date:** 2026-08-05  
**Method:** pure mathematics; exact Fourier and bounded-variation estimates,
no computation, search, or solver  
**Status:** unconditional sign theorem.  The continuum long-wrap obstruction
`J_P(alpha)` is strictly positive for every nontrivial duty cycle whenever
`P<=1/2`.  Consequently every such long-wrap family has a linear positive
reserve for all sufficiently large residue periods.  Periods in
`(1/2,zeta]`, finite-period zero-limit effects, general multi-kink profiles,
and finite shoulders remain open.

## 1. The triangular discrepancy

Fix

\[
 0<P\le {1\over2},
 \qquad 0<\alpha<P,
 \qquad \rho={\alpha\over P},
 \qquad m=\min\{\rho,1-\rho\}.
\tag{1.1}

Recall the duty-cycle price

\[
 H_{P,\alpha}(x)
 =\alpha\lfloor x/P\rfloor+\min\{x\bmod P,\alpha\}.
\tag{1.2}

Write

\[
 H_{P,\alpha}(x)=\rho x+D_{P,\rho}(x),
\tag{1.3}

where `D` is `P`-periodic and on one period

\[
 D(x)=
 \begin{cases}
 (1-\rho)x,&0\le x\le\alpha,\\
 \rho(P-x),&\alpha\le x\le P.
 \end{cases}
\tag{1.4}

It is a nonnegative triangular tent with mean

\[
 \widehat D_0={1\over P}\int_0^P D(x)dx
 ={P\rho(1-\rho)\over2}.
\tag{1.5}

For `n!=0`, with `omega_n=2pi n/P`, its Fourier coefficients are

\[
 \boxed{
 \widehat D_n
 =-{1-e^{-2\pi i n\rho}\over P\omega_n^2}.}
\tag{1.6}

Indeed, in the periodic distribution sense,

\[
 D''=\delta_0-\delta_\alpha.
\]

Since

\[
 |1-e^{-2\pi i n\rho}|
 =2|\sin(\pi n\rho)|
 \le2\pi n m,
\]

one has

\[
 \boxed{
 |\widehat D_n|\le {Pm\over2\pi |n|}.}
\tag{1.7}

The exact formula (1.6), rather than the weaker bound (1.7), also shows
`widehat D_n=O(n^-2)`, so the Fourier series converges absolutely and
uniformly.

## 2. A two-integration transform bound for the Rayleigh deviation density

Put

\[
 \varphi(r)=2r e^{-r^2}\qquad(r\ge0)
\tag{2.1}

and

\[
 q(x)=-K'(x)=
 \begin{cases}
 \varphi(A-x)-\varphi(A+x),&0<x<A,\\
 -\varphi(A+x),&x>A.
 \end{cases}
\tag{2.2}

Thus

\[
 q(0)=0,
 \qquad
 \int_0^\infty q(x)dx=K(0)=:M.
\tag{2.3}

### Lemma 2.1

For every real `t!=0`,

\[
 \boxed{
 \left|\int_0^\infty q(x)e^{itx}dx\right|
 <{7\over t^2}.}
\tag{2.4}

#### Proof

The function `q` is continuous, piecewise smooth, and vanishes at both
endpoints.  Its derivative has one jump at `x=A`, of magnitude

\[
 |q'(A+)-q'(A-)|=\varphi'(0)=2.
\tag{2.5}

Two integrations by parts, the second in the bounded-variation sense, give

\[
 \left|\int_0^\infty q(x)e^{itx}dx\right|
 \le {|q'(0)|+\operatorname {Var}(q')\over t^2}.
\tag{2.6}

Now

\[
 |q'(0)|=2|\varphi'(A)|=2(\pi-2)e^{-\pi/4}.
\tag{2.7}

Using `pi<22/7` and the authenticated bound
`exp(-pi/4)<57/125`,

\[
 |q'(0)|<{912\over875}.
\tag{2.8}

Away from the single jump,

\[
 \int_0^\infty |q''(x)|dx
 \le\int_0^\infty|\varphi''(r)|dr.
\tag{2.9}

Since

\[
 \varphi'(r)=2(1-2r^2)e^{-r^2},
 \qquad
 \varphi''(r)=4r(2r^2-3)e^{-r^2},
\]

`φ'` decreases from `2` to `-4 exp(-3/2)` and then increases to zero.
Therefore

\[
 \int_0^\infty|\varphi''(r)|dr
 =2+8e^{-3/2}.
\tag{2.10}

The positive exponential series gives

\[
 e^{3/2}>
 1+{3\over2}+{(3/2)^2\over2!}+{(3/2)^3\over3!}
 +{(3/2)^4\over4!}+{(3/2)^5\over5!}
 >{40\over9},
\]

so `e^(-3/2)<9/40` and

\[
 \int_0^\infty|\varphi''|<{19\over5}.
\tag{2.11}

Equations (2.5), (2.8), (2.9), and (2.11) give

\[
 |q'(0)|+\operatorname {Var}(q')
 <{912\over875}+2+{19\over5}<7.
\]

Substitution in (2.6) proves (2.4). \(\square\)

## 3. The positive zero mode dominates every Fourier mode

The equal-work identity gives

\[
 \int_0^\infty xq(x)dx=\int_0^\infty K(x)dx=0.
\tag{3.1}

Hence the linear part in (1.3) cancels, and the duty-cycle scalar is

\[
 J_P(\alpha)=\int_0^\infty D_{P,\rho}(x)q(x)dx.
\tag{3.2}

The zeroth Fourier mode contributes

\[
 M\widehat D_0
 ={MP\rho(1-\rho)\over2}
 \ge {MPm\over4}.
\tag{3.3}

For `n>=1`, apply Lemma 2.1 at `t=omega_n` and (1.7):

\[
 \left|
 \widehat D_n\int_0^\infty q(x)e^{i\omega_nx}dx
 \right|
 <{Pm\over2\pi n}
   {7P^2\over4\pi^2n^2}.
\]

Summing both signs of `n` and using `zeta(3)<5/4`,

\[
 \left|\text{all nonzero modes}\right|
 <{7P^3m\over4\pi^3}\zeta(3).
\tag{3.4}

The authenticated bound `M>11/125`, together with `pi^3>27` and
`P^2<=1/4`, gives

\[
 7P^2\zeta(3)
 <{35\over16}
 <{297\over125}
 <M\pi^3.
\tag{3.5}

Comparison of (3.3)--(3.5) yields the strict inequality

\[
 \boxed{
 J_P(\alpha)>0
 \qquad
 \left(0<P\le{1\over2},\ 0<\alpha<P\right).}
\tag{3.6}

This signs the complete duty-cycle price, not merely its centered Fourier
part.

## 4. Consequences for long-wrap Apéry clocks

For fixed `P<=1/2` and `0<alpha<P`, the long-wrap continuum theorem gives

\[
 \Phi_g(P,\alpha)
 ={g\over\alpha}J_P(\alpha)+O_{P,\alpha}(1).
\tag{4.1}

Therefore

\[
 \boxed{
 \Phi_g(P,\alpha)>0
 \quad\text{for every sufficiently large }g,}
\tag{4.2}

with linear reserve.  The arithmetic boundary `alpha=P` is positive for
every `g` by the all-mesh comb theorem, and the endpoint-only boundary
`alpha=0` is `gC(P)>0`.

The Fourier estimate does not supply a uniform finite threshold in `g`
when `alpha` approaches an endpoint, because `J_P(alpha)` then tends to
zero.  It also does not address `1/2<P<=zeta`; improving the transform
bound or exploiting phase rather than absolute Fourier values is required
there.

## 5. Dependencies

1. `MATH_THEOREM_RAYLEIGH_LONG_WRAP_CONTINUUM_DUTY_CYCLE_DICHOTOMY_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`;
3. authenticated rational Rayleigh bounds cited there.
