# Independent audit: Rayleigh arithmetic comb and global Apéry tube

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, numerical search, or solver  
**Audited files:**

1. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`,
   SHA-256
   `0f1dd78f9ca68d20a0c1564452902527f8dfbfb6b993392c11859a8a6177a1f8`;
2. `MATH_COROLLARY_RAYLEIGH_GLOBAL_APERY_STABILITY_TUBE_20260805.md`,
   SHA-256
   `1f6bdfd16d038b3f7237ddd90a7356256dc093ff4eef401c55ac58c7a1b9cf2`.

**Verdict:** **INDEPENDENT-GO.**  No correction to either audited source is
needed.  The centered fractional-part identity, the shifted Gaussian sum,
all Fourier and integration-by-parts signs and boundary terms, both mesh
ranges, the uniform constant `377/108000`, and the transfer to the global
Apéry stability tube all replay exactly.  The scope remains arithmetic-comb
positivity plus a quantitative near-arithmetic dichotomy; it is not the
full nonarithmetic all-price theorem.

## 1. Exact floor identity and endpoint conventions

For every nonnegative `x`, including `x=0` and positive lattice points,

\[
 \left\lceil{x\over h}\right\rceil
 =\sum_{n\ge0}{\bf1}_{\{x>nh\}}.
\]

Thus the strict tails in the definition of `K` give the signed ceiling
count in (2.3), including the atoms of `X` and `Y` at zero.

Write `A=qh+delta`, `0<=delta<h`, and `Z=(R-delta)/h`.  On `R<A`,

\[
 \left\lceil{A-R\over h}\right\rceil
 =\lceil q-Z\rceil=q-\lfloor Z\rfloor.
\]

On `R>A`, away from the null set on which `Z` is integral,

\[
 -\left\lceil{R-A\over h}\right\rceil
 =-\lceil Z-q\rceil=q-\lfloor Z\rfloor-1.
\]

At `R=A`, both signed ceilings vanish and the combined formula
`q-floor(Z)-1_{R>A}` also vanishes.  The only other endpoint exceptions in
the second display are the countable Rayleigh-null lattice.  Negative `Z`
causes no problem: the ordinary floor convention is exactly the convention
needed, and `Z>-1` at the lower endpoint.

Since `EZ=(A-delta)/h=q`, expectation gives, with the correct upper-tail
indicator and sign,

\[
 C(h)=E\{Z\}-P(R>A).
\]

This verifies (2.1), including the case `delta=0`.

For the shifted Gaussian form, the inner-branch sum reverses to indices
`m=0,...,q`, while the outer-branch sum has indices `m=q,q+1,...`.
Their sole overlap is

\[
 e^{-(\delta+qh)^2}=e^{-A^2}=p.
\]

Therefore (3.1) has exactly one separate subtraction of `p`; there is no
off-by-one at `delta=0` or at `nh=A`.

## 2. Characteristic-function integration by parts

For `varphi(r)=2r exp(-r^2)`, the three displayed derivatives are exact.
The roots of `varphi'''` in `s=r^2` are
`s_+=(3+sqrt(6))/2` and `s_-=(3-sqrt(6))/2`.  Hence `varphi''` travels

\[
 0\longrightarrow-M\longrightarrow P\longrightarrow0,
\]

and its total variation is `2(M+P)`.  The source bounds give `M<6` and
`P<2`, so `||varphi'''||_1<16<20`.

All integrations by parts are legitimate: `varphi`, `varphi'`, and
`varphi''` vanish at infinity, `varphi(0)=varphi''(0)=0`,
`varphi'(0)=2`, and `varphi'''` is integrable.  With the source convention
`exp(itr)`, the exact signs are

\[
 \widehat\varphi(t)
 ={2\over(it)^2}-{1\over(it)^3}
   \int_0^\infty e^{itr}\varphi'''(r)\,dr.
\]

Thus the norm bound `2/t^2+20/t^3` is correct.  In particular, the
nonzero endpoint contribution is quadratic, not linear.

## 3. Sawtooth expectation and the uniform constants

The Fejér means of the sawtooth are uniformly bounded and converge away
from the integers.  The shifted Rayleigh phase has no atoms modulo one, so
dominated convergence applies.  After expectation, Lemma 4.1 makes the
ordinary Fourier series absolutely convergent.  The shift contributes only
a unit-modulus phase.  Substituting `t_m=2*pi*m/h` gives exactly

\[
 {h^2\zeta(3)\over2\pi^3}
 +{20h^3\zeta(4)\over8\pi^4}.
\]

For `h<=A`, `A^2=pi/4`, `zeta(3)<5/4`, `zeta(4)<10/9`,
`pi^2>9`, and `sqrt(pi)>5/3` yield respectively

\[
 {5\over288},\qquad {5\over216};
\]

their sum is `35/864`.  The authenticated rational estimate
`K(0)>11/125` gives `p<57/125`, and

\[
 {397\over864}-{57\over125}
 ={377\over108000}>0.
\]

The cross multiplication is
`397*125-57*864=377`, so the numerator and denominator in the claimed
uniform margin are exact.

## 4. Large meshes

When `h>A`, `q=0` and the direct branch split is

\[
 C(h)=K(0)-\sum_{n\ge1}e^{-(A+nh)^2}.
\]

Because `A+nh>(n+1)A`, its tail is strictly below
`sum_{m>=2}p^{m^2}`.  For `m>=2`,
`m^2>=4+5(m-2)`, giving `p^4/(1-p^5)`.
At `p<57/125`, the exact rational comparison with `9/200` is

\[
 200\,57^4\,125
 <9(125^5-57^5);
\]

the two sides are `263900025000` and `269242974612`.  Hence the tail is
below `0.045`, whereas `K(0)>0.088`.  This proves the stated `0.043`
margin.  The boundary `h=A` is already included in the Fourier case, so
the two cases cover all positive meshes without a gap.

The reciprocal-mesh theta formula also has the correct normalization: the
half-lattice Poisson sum contributes `q+1/2` plus
`2q sum_{m>=1}exp(-4*pi*q^2*m^2)`, producing exactly (5.8).

## 5. Apéry transfer

For a saturated first-`zeta` table, every `a_j` with `j<N` is below
`zeta`.  Its endpoint satisfies `T<2*zeta`; hence, for `N>=2`,
`T/N<zeta`, while for `N=1` saturation gives `T=zeta`.  Therefore

\[
 0<\lambda\le\zeta<A.
\]

The formal Apéry clock used by the sampling theorem is nonnegative.  To
make the implicit domain check explicit, if `g>1`, the walk consisting of
`r` copies of denomination one shows
`beta_r>=r(c_1-lambda)` for `0<=r<g`; hence

\[
 U_{qg+r}=\lambda(qg+r)+\beta_r
 \ge qg\lambda+r c_1\ge0.
\]

If `g=1`, this is immediate.  Also `U_m>=lambda*m-Delta`, so both sampled
series converge absolutely.  The Rayleigh `K` is continuously
differentiable across `A`, with piecewise integrable second derivative;
therefore `K'` is integrable and has finite total variation.  All
hypotheses of the bounded-variation sampling lemma are present.

Since `lambda<A`,

\[
 \|K'\|_1+\lambda\operatorname{Var}(K')\le B_A.
\]

The definition of `epsilon_*` implies both
`Delta<=lambda/2` and `epsilon_* B_A<=c_*/2`.  Combining the strict comb
margin with the sampling estimate gives

\[
 \Phi(U)>c_*/2.
\]

Finally, the shoulder inequality is termwise:
`K(V_m)>=K(U_m)-(K(U_m)-K(V_m))_+` on the finite head and the clocks agree
after the conductor.  Thus `Phi(V)<=0` forces shoulder debt at least
`c_*/2` whenever the displacement alternative fails.  The strict/non-strict
inequalities in (3.5)--(3.7) are therefore consistent.

## 6. Exact scope

The audited theorem proves a dimension-free positive lower bound for every
one-period arithmetic comb.  The audited corollary upgrades the existing
Apéry stability result from a small-mesh neighborhood to every normalized
mesh, and gives the exact displacement-or-shoulder dichotomy.

It does **not** prove positivity for arbitrary nonarithmetic residue
displacements, does not rule out adverse finite shoulder debt, and does not
convert either defect into Boolean configuration reserve.  Those remain
the live all-price steps.
