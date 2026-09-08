# Self-audit: first residual socket endpoint decrease

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`  
**Verdict:** GO.  The derivative identity, endpoint branch choices, and
strict sign are correct.  The conclusion excludes only use of the whole
residual socket density as one nondecreasing Wang--Wang role.

## 1. Differentiation check

At equal-level endpoints, let

\[
 a=K'(r)>0,\qquad q=-K'(\ell)>0,
 \qquad H={aq\over a+q}=u'(t).
\]

Because `d r/d u=1/a` and `d ell/d u=-1/q`,

\[
 {da\over du}={K''(r)\over a},
 \qquad
 {dq\over du}={K''(\ell)\over q}.
\]

Also

\[
 H_a={q^2\over(a+q)^2},
 \qquad
 H_q={a^2\over(a+q)^2}.
\]

Thus

\[
 {dH\over du},{du\over dt}
 =\left(
 {q^2K''(r)/a+a^2K''(\ell)/q\over(a+q)^2}
 \right){aq\over a+q}
 ={q^3K''(r)+a^3K''(\ell)\over(a+q)^3}.
\]

This verifies the source formula for `u''`.

## 2. Sign check

At `t=b`, the certified locations are

\[
 b\in(0.46,0.48),\quad
 \ell\in(0.55,0.60),\quad
 r\in(1.01,1.08).
\]

They place `b,ell` on the compact branch and `r` on the noncompact
branch.  The rational Gaussian bounds give

\[
 K''(b)>.19,quad K''(\ell)>0,quad -K''(r)<.35,
 \quad a>.075,quad q<.28.
\]

The positive `a^3K''(ell)` term can only increase `u''`, hence

\[
 -u''(b)
 <.35\left({q\over a+q}\right)^3
 <.35\left({56\over71}\right)^3
 <.172.
\]

Therefore

\[
 g_2'(b-)=-K''(b)-u''(b)<-.19+.172<0.
\]

All inequalities have slack; no endpoint equality is being rounded.

## 3. Scope check

A density with negative left derivative at `b` cannot be nondecreasing on
the whole interval `(0,b)`.  This invalidates the unsplit-role monotonicity
premise.  It says nothing about expressing that density as a barycenter of
several monotone densities or interval-uniform layers.  The source states
exactly this limited conclusion.

