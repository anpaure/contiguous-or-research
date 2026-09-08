# Independent audit: h=4 inert one-dimensional compact Gaussian gate

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_H4_INERT_ONE_DIMENSIONAL_COMPACT_GAUSSIAN_GATE_20260804.md`  
**Method:** exact symbolic audit only; no search or numerical sampling.

## Verdict

**PASS.**  The four-variable shifted-train envelope is reduced correctly to
one ceiling train, two fixed endpoint mismatches, and one compact kernel
difference.  The final scalar gate remains conditional, as stated.

## 1. Derivative budget audit

For `0<=t<=A/5`, differentiation gives

\[
F'(t)=2[h(A+t)-h(A-t)]+2\sum_{n\ge2}h(nA+t).
\]

Because `A-t>=4A/5>1/sqrt(2)`, the bracket is nonpositive and every tail
term is at most `h(nA)`.  The `n=2` contribution is less than `7/45`.
The `n=3` contribution is less than `1/150`, and all subsequent weighted
ratios are below `1/75`.  Hence

\[
2\sum_{n\ge2}nAe^{-n^2A^2}
<{7\over45}+{1\over148}
={1081\over6660}<{1\over6}.
\]

Integration proves `F(t)<=C+t/6`.  The no-interior-minimum theorem on
`[0,A/4]` independently proves

\[
F(x)\ge\min(C,F(A/4)).
\]

Therefore the first pair loss is at most `eta_-+u/6`, plus exactly one
reflection error.  All directions are correct.

## 2. Compact-kernel audit

On `[A/4,A/2]`,

\[
2\operatorname{arctanh}(w/A)<\pi(w/A)
\]

implies `h(A+w)<h(A-w)` and hence `K'(w)<0`.

For the full shifted train,

\[
F'(w)=K'(w)+2\sum_{q\ge1}(A+qA+w)e^{-(A+qA+w)^2}>K'(w).
\]

Thus, whenever `v<y` in this interval,

\[
F(v)-F(y)<K(v)-K(y).
\]

The active endpoint condition gives `y-v<=delta`; the physical upper rank
bound gives `y<=v_1(u)`.  Since `K` decreases, the maximum loss is exactly
bounded by the compact expression `Delta_K(u,delta)`.  The cases
`y<A/4` and `A/4<=y<=v` give respectively the fixed mismatch `eta_+`
and zero.  Hence Lemma 2.1 is correct.

## 3. Scalar reduction audit

The endpoint-efficiency inequality is equivalent to

\[
u\le U(\delta)={A-4\delta\over5}.
\]

Adding the two pair estimates to the one ceiling train yields

\[
\mathscr B_{A+\delta}
>
C(A+\delta)-\eta_- -{u\over6}
-\max(\eta_+,\Delta_K(u,\delta))
-{1\over10000}.
\]

Maximizing the total possible loss over `0<=u<=U(delta)` is precisely
`Xi(delta)`.  Therefore condition (3.3) implies positivity on both inert
faces.  No shifted-train loss or reflection charge is omitted.

## 4. Scope

This is a sufficient reduction, not a proof that (3.3) holds.  It is
strictly smaller than the earlier exact `Gamma(delta)` gate but slightly
relaxes the remaining physical correlations through separate worst-case
bounds.  No complete h=4 or broader result is claimed.
