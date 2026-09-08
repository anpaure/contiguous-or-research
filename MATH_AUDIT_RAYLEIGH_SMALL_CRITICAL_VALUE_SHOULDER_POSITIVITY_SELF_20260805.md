# Self-audit: small-critical-value Rayleigh shoulder positivity

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_SMALL_CRITICAL_VALUE_SHOULDER_POSITIVITY_20260805.md`  
**Method:** independent symbolic replay; pure mathematics, no computation,
enumeration, search, or solver  
**Verdict:** **PASS SELF-AUDIT.**  The theorem gives a genuine uniform
physical-shoulder closure for an absolute small critical-value interval.
It does not assert that the threshold reaches the Rayleigh minimum.

## 1. Critical-chain geometry

Let `H` be the least maximum-density denomination and `L=H lambda`.  If
`H<N`, first-minimum normalization gives `L=c_H<zeta`.  Since every
critical index is divisible by the formal gcd, formal periodicity gives

\[
 U_{r+qH}=U_r+qL.
\]

The Apéry shift is nonpositive, so for `r<H`,

\[
 0\le U_r\le\lambda r<L.
\]

Physical nonnegativity gives

\[
 0\le\Delta_r=U_r-V_r\le U_r.
\]

Therefore every active layer argument `y=U_r-t` lies in `[0,L)`.  This is
the essential physical input and is stronger than abstract monotonicity of
one deficit chain.

## 2. BV quadrature

On each interval `I_q=[y+qL,y+(q+1)L]`,

\[
 \left|LK'(y+qL)-\int_{I_q}K'\right|
 \le L\operatorname {Var}_{I_q}(K').
\]

The interval interiors are disjoint.  Summing and using `K(infinity)=0`
gives

\[
 LJ_{L,\infty}(y)\le-K(y)+L\mathcal V.
\]

For `L<=L_*`, Lipschitz continuity gives

\[
 K(y)\ge M-RL\ge M/2,
 \qquad L\mathcal V\le M/2.
\]

Hence the infinite derivative train is nonpositive.

Because `L<=zeta/2` and `0<=y<L`, the sampled derivative terms are zero
or negative until the unique crossing of `zeta`, then positive forever.
Thus their partial sums first decrease and then increase to their
nonpositive infinite limit.  Every finite prefix is nonpositive.  The
`y=0` endpoint merely makes the first term zero and causes no exception.

## 3. Shoulder sign

For a critical denomination, the exact layer-cake theorem is

\[
 \Phi(V)-\Phi(U)
 =-\sum_r\int J_{L,N_r(t)}(U_r-t)dt.
\]

Section 2 makes every displayed `J` nonpositive, so the shoulder is
nonnegative.  The independently audited inverse-circle and Fourier
theorems give strict positivity of the complete formal clock.  Therefore
the physical clock is strictly positive.

No uniformity issue is hidden: the proof never uses the period, conductor,
number of denominations, number of active chains, or a bound on an
individual deficit.

## 4. Boundary audit

The theorem requires `H<N`.  When `H=N`, least-critical normalization has
`L=zeta`, outside the small-value argument.  When `L_*<L<zeta`, the chain
start remains before `zeta`, but the BV error can exceed `K(y)` and the
proof gives no sign.  The source explicitly leaves both regimes open.

The conclusion concerns the analytic Bellman/Rayleigh inequality only.
It gives no Boolean occurrence reserve, finite integral rounding, carrier,
compiler, or OR-word theorem.

