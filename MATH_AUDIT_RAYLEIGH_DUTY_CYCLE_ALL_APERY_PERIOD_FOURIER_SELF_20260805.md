# Self-audit of all-period Rayleigh duty-cycle Fourier positivity

**Date:** 2026-08-05  
**Method:** independent line-by-line algebraic audit; pure mathematics; no
search, solver, or numerical sign oracle  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_ALL_APERY_PERIOD_FOURIER_POSITIVITY_20260805.md`  
**Verdict:** **PASS.**  The Fourier coefficient, exact variation, harmonic
square-sum, Rayleigh-minimum bound, and final strict rational margin all
check.  The theorem proves

\[
 J_P(\alpha)>0
 \qquad(0<P\le\zeta,\ 0<\alpha<P).
\]

It closes the continuum one-kink/long-wrap family, but not finite residue
periods uniformly near the duty endpoints, multi-kink Apéry profiles,
finite shoulders, or the occurrence-faithful Boolean reserve.

## 1. Duty tent and Fourier normalization

On one period,

\[
 D(x)=
 \begin{cases}
 (1-\rho)x,&0\le x\le \rho P,\\
 \rho(P-x),&\rho P\le x\le P.
 \end{cases}
\]

Its mean is `P rho(1-rho)/2`.  Distributionally,

\[
 D''=\delta_0-\delta_{\rho P}.
\]

With frequency `omega_n=2pi n/P`, this gives

\[
 \widehat D_n
 =-{1-e^{-2\pi i n\rho}\over P\omega_n^2},
 \qquad
 |\widehat D_n|
 ={P|\sin(\pi n\rho)|\over2\pi^2n^2}.
\]

Thus the factor in the audited theorem is exact.  The coefficients are
`O(n^-2)`, so the periodic Fourier series is absolutely and uniformly
convergent.  Since the Rayleigh deviation density `q` is absolutely
integrable, termwise integration is justified.

## 2. Exact variation of the Rayleigh transform density

For `0<x<A`,

\[
 q(x)=\varphi(A-x)-\varphi(A+x),
 \qquad
 q''(x)=\varphi''(A-x)-\varphi''(A+x).
\]

The reflected-curvature lemma, together with the elementary sign split at
`x=A/2`, gives

\[
 \varphi''(A+x)>\varphi''(A-x),
\]

so `q'` is strictly decreasing on `(0,A)`.  Its endpoint data are

\[
 q'(0)=b_0=2(\pi-2)e^{-\pi/4},
\]

\[
 q'(A-)=-2+c_0,
 \qquad
 q'(A+)=c_0,
 \qquad
 c_0=-\varphi'(2A)>0.
\]

Therefore the variation before the jump is `b_0+2-c_0`, and the jump has
size two.  On the tail,

\[
 q'(x)=-\varphi'(A+x),
 \qquad
 q''(x)=-\varphi''(A+x)<0,
\]

because `A+x>2A=sqrt(pi)>sqrt(3/2)`.  Hence the tail variation is exactly
`c_0`, and

\[
 \operatorname {Var}(q')=b_0+4.
\]

Both boundary terms in the first integration by parts vanish because
`q(0)=q(infinity)=0`.  The second, Stieltjes, integration has the boundary
term `q'(0)=b_0`.  Thus

\[
 \left|\int_0^\infty q(x)e^{itx}dx\right|
 \le {b_0+\operatorname {Var}(q')\over t^2}
 ={4+2b_0\over t^2}.
\]

Using `pi<22/7` and `exp(-pi/4)<57/125`,

\[
 4+2b_0
 =4+4(\pi-2)e^{-\pi/4}
 <4+4{8\over7}{57\over125}
 ={5324\over875}=:B.
\]

No sign or endpoint term is missing.

## 3. Endpoint-uniform harmonic estimate

The exact identity

\[
 \sum_{n\ge1}{\sin^2(nx)\over n^4}
 ={x^2(\pi-x)^2\over6}
 \qquad(0\le x\le\pi)
\]

and Cauchy--Schwarz with `zeta(4)=pi^4/90` give

\[
 \sum_{n\ge1}{|\sin(\pi n\rho)|\over n^4}
 \le {\pi^4\over6\sqrt{15}}\rho(1-\rho).
\]

The exact quadratic factor `rho(1-rho)` is essential: it matches the
zeroth Fourier mode at both duty endpoints.

## 4. The rational bound on the minimum location

For `0<x<A`, writing `u=x/A` gives

\[
 K'(x)>0
 \quad\Longleftrightarrow\quad
 \log {A+x\over A-x}>4Ax
 \quad\Longleftrightarrow\quad
 2\operatorname {arctanh}(u)>\pi u.
\]

At `x=sqrt(2/3)`, the prerequisite `x<A` follows from `pi>8/3`, and

\[
 u^2={8\over3\pi}>{28\over33}>{21\over25}.
\]

The finite positive-series lower bound used in the source is exactly

\[
 2\sum_{k=0}^{5}{(21/25)^k\over2k+1}
 ={343563152\over107421875}.
\]

Its difference from `22/7` is

\[
 {41660814\over751953125}>0.
\]

Therefore `K'(sqrt(2/3))>0`.  The authenticated uniqueness and sign change
of the Rayleigh minimum then imply

\[
 \zeta^2<{2\over3}.
\]

## 5. Final mode comparison

Pairing positive and negative frequencies, the full nonzero contribution
is bounded by

\[
 {BP^3\over4\pi^4}
 \sum_{n\ge1}{|\sin(\pi n\rho)|\over n^4}
 \le
 {BP^3\rho(1-\rho)\over24\sqrt{15}}.
\]

The zeroth mode is

\[
 {MP\rho(1-\rho)\over2}.
\]

It is therefore enough that

\[
 BP^2<12\sqrt{15}M.
\]

The allowed period range and the preceding minimum bound give

\[
 BP^2
 <{5324\over875}{2\over3}
 ={10648\over2625}.
\]

The authenticated `M>11/125` and elementary `sqrt(15)>387/100` give

\[
 12\sqrt{15}M>{51084\over12500}.
\]

Finally,

\[
 {10648\over2625}<{51084\over12500},
\]

because

\[
 133100000<134095500.
\]

The margin is strict, so cancellation among nonzero modes is not needed.
The zeroth mode dominates their total absolute value for every
`0<P<=zeta` and `0<rho<1`.

## 6. Scope audit

The proved conclusion is exactly continuum positivity for the one-kink
duty-cycle price.  Combined with the long-wrap Riemann-sum theorem, it
implies positive linear reserve for every fixed interior pair `(P,alpha)`
once the residue period is sufficiently large.  It does not supply a
threshold uniform as `alpha` approaches zero or `P`.

Nothing in the argument decomposes a general cyclic-superadditive Apéry
queue into positive duty cycles.  In particular, genuine multi-kink
profiles, the finite-availability shoulder, and the occurrence-labelled
Boolean realization remain outside the theorem.  The source states all
three exclusions explicitly.

## 7. Final audit verdict

**PASS.**  Subject to its stated scope, the theorem is unconditional and
the strict constant comparison is valid.  The complete continuum
long-wrap/two-slope obstruction is closed on the full normalized period
range `0<P<=zeta`.
