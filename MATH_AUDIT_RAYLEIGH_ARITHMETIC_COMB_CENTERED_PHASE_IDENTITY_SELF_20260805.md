# Self-audit: centered-phase proof of all Rayleigh arithmetic combs

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`  
**Verdict:** **SELF-GO**, pending independent replay.

## 1. Tail-sum and floor identity

For `X,Y>=0`, including their atoms at zero,

\[
 \lceil X/h\rceil=\sum_{n\ge0}\mathbf1_{\{X>nh\}}
\]

outside positive lattice boundaries.  Rayleigh continuity makes every
positive boundary null.  With `A=qh+delta` and
`Z=(R-delta)/h`, the two strict half-lines give

\[
 \lceil(A-R)/h\rceil=q-\lfloor Z\rfloor
 \quad(R<A),
\]

and

\[
 -\lceil(R-A)/h\rceil=q-\lfloor Z\rfloor-1
 \quad(R>A).
\]

The exceptional equality points are null.  Since `EZ=q`, expectation is
`E{Z}-P(R>A)`.  The sign and the extra upper-tail indicator are essential;
omitting that indicator would give the false limit `1/2` instead of
`1/2-p`.

The shifted half-Gaussian formula independently replays the same identity.
The joining term at `delta+qh=A` is counted in both Gaussian sums and hence
contributes the separate subtraction `p`.

## 2. Characteristic-function decay

For `varphi(r)=2r exp(-r^2)`, direct differentiation gives the three
displayed derivatives.  The roots of `varphi'''` in the variable `s=r^2`
are `(3+-sqrt(6))/2`.  Therefore `varphi''` has exactly one negative
minimum and one positive maximum.  Its total variation is exactly twice
the sum of their magnitudes.

The coarse estimates in the theorem imply `M<6`, `P<2`, and hence

\[
                         \|\varphi'''\|_1<16<20.
\]

Three integrations by parts are legitimate because every derivative used
is integrable and vanishes at infinity.  The only nonzero boundary datum is
`varphi'(0)=2`, giving

\[
 |\widehat\varphi(t)|\le2/t^2+20/t^3.
\]

The signs of the two terms are irrelevant to the norm bound.

## 3. Fourier sawtooth and constants

Use Fejer sums before expectation; they are uniformly bounded and converge
at every noninteger.  The induced random phase is continuous modulo one.
After expectation, the characteristic-function bound makes the series
absolutely summable (`m^-3` and `m^-4`), so passage to the ordinary Fourier
series is justified.

For `h<=A`, substitution of `t_m=2pi m/h` gives exactly

\[
 {h^2\zeta(3)\over2\pi^3}
 +{20h^3\zeta(4)\over8\pi^4}.
\]

At `h=A`, the first term is at most `5/288`; the second is at most
`5/216`.  Their sum is

\[
                         {35\over864}.
\]

The rational comparisons are

\[
 {397\over864}>{57\over125},
\]

because `397*125=49625>49248=57*864`.  The authenticated
`K(0)>0.088` gives `p<0.456=57/125`.  Thus the phase mean is strictly
larger than `p` for every shift, a statement stronger than needed.

## 4. Large meshes

For `h>A`, only the `n=0` kernel value uses the inner branch.  The negative
tail is strictly below

\[
 \sum_{m>=2}p^{m^2}
 \le p^4/(1-p^5).
\]

At `p<0.456` this is below `0.045`, while `K(0)>0.088`; hence the comb is
strictly positive.  There is no uncovered boundary: `h=A` belongs to the
Fourier case.

## 5. Scope

The theorem proves every one-period arithmetic clock, for every positive
mesh and arbitrary centered phase.  It does not prove positivity of a
multi-residue formal Apery clock or control the finite conductor shoulder.
Those are the remaining nonarithmetic all-price rows.
