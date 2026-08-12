# Algebraic audit: small-period Rayleigh duty-cycle Fourier positivity

**Date:** 2026-08-05  
**Method:** pure mathematical replay of Fourier normalizations, BV
integration, Gaussian variation, and constants; no computation, search, or
solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_SMALL_PERIOD_FOURIER_POSITIVITY_20260805.md`  
**Verdict:** **SELF-GO.**  Every factor of `P`, `2 pi`, and two from the
negative Fourier modes replays correctly.  The strict constant comparison
closes all nontrivial duty cycles for `P<=1/2`.

## 1. Tent Fourier coefficient

With convention

\[
 \widehat D_n={1\over P}\int_0^P D(x)e^{-2\pi inx/P}dx,
\]

the periodic second derivative is `delta_0-delta_alpha`.  Therefore

\[
 -\left({2\pi n\over P}\right)^2\widehat D_n
 ={1\over P}(1-e^{-2\pi in\rho}),
\]

which gives the source formula.  The bound

\[
 |1-e^{-2\pi in\rho}|
 =2|\sin(\pi n\rho)|
 \le2\pi n\min(\rho,1-\rho)
\]

is valid by replacing `rho` with `1-rho` if necessary and using
`|sin(nx)|<=n|sin x|<=n x` on `[0,pi/2]` (or directly
`|sin(pi n rho)|<=pi n min(rho,1-rho)`).  Thus the weakened coefficient is
`Pm/(2 pi n)` exactly.

The tent area is one half times base times height:

\[
 {1\over P}\int_0^P D
 ={1\over P}{P(P\rho(1-\rho))\over2}
 ={P\rho(1-\rho)\over2}.
\]

## 2. Deviation transform

For `q=-K'`, one has `q(0)=q(infinity)=0`.  Its derivative jump at `A` is

\[
 [-\varphi'(2A)]-[-\varphi'(0)-\varphi'(2A)]
 =\varphi'(0)=2.
\]

Away from the jump,

\[
 q''=\varphi''(A-x)-\varphi''(A+x)quad(x<A),
\]

and `q''=-varphi''(A+x)` after `A`.  Triangle integration covers the
disjoint ranges `[0,A]`, `[A,2A]`, and `[2A,infinity)`, hence

\[
 \int|q''|\le\int_0^\infty|\varphi''|.
\]

The variation of `varphi'` is exact:

\[
 \int|\varphi''|=2+8e^{-3/2}<{19\over5}.
\]

Together with the jump and
`|q'(0)|=2(pi-2)e^(-pi/4)<912/875`, this is strictly less than seven.
The two BV integrations by parts therefore yield `7/t^2` with no missing
boundary atom.

## 3. Pairing and zero mode

Integration by parts gives

\[
 J=\int Hq.
\]

Since `H=rho x+D` and

\[
 \int xq(x)dx=\int K(x)dx=0,
\]

one has `J=integral Dq`.  The constant Fourier coefficient pairs with
`integral q=M`, producing

\[
 {MP\rho(1-\rho)\over2}\ge {MPm\over4}.
\]

Both nonzero signs contribute, so their absolute total is

\[
 2\sum_{n\ge1}{Pm\over2\pi n}
 {7P^2\over4\pi^2n^2}
 ={7P^3m\over4\pi^3}\zeta(3).
\]

No factor two is omitted.

## 4. Rational constant comparison

After dividing the error comparison by `Pm/4`, it is enough that

\[
 7P^2\zeta(3)<M\pi^3.
\]

For `P<=1/2`, the left side is strictly less than

\[
 7\cdot{1\over4}\cdot{5\over4}={35\over16}.
\]

The right side is strictly greater than

\[
 {11\over125}\cdot27={297\over125}.
\]

Cross multiplication gives

\[
 {35\over16}<{297\over125}
 \quad\Longleftrightarrow\quad
 4375<4752.
\]

Thus the zero mode strictly dominates for every `0<rho<1`.

## 5. Scope

The proof signs the continuum duty-cycle functional, hence large-period
long-wrap clocks, only for `P<=1/2`.  It does not claim that each finite
clock is positive, nor does it extend the absolute Fourier bound through
`P=zeta`.  Those exclusions are explicit in the source.
