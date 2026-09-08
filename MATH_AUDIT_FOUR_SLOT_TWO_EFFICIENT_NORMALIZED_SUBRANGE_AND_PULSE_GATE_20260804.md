# Audit: four-slot normalized subrange and pulse gate

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_FOUR_SLOT_TWO_EFFICIENT_NORMALIZED_SUBRANGE_AND_PULSE_GATE_20260804.md`  
**Verdict:** **PASS** for the complete two-slot-efficient regime, subject
to independent rechecking of the displayed rational cross-multiplications.

## 1. Parameter and transient checks

The source four-slot normal form gives

\[
 T=2y,\qquad x\le r=z-y\le y/2.
\]

In the only source-open range, `A/2<=y<A`; hence `x,r` lie in
`[0,A/2]`, where the previously proved derivative calculation makes `K`
decreasing.  Therefore `K(x)-K(r)>=0` has the stated direction.

## 2. Three-slot reuse

For `(0,x,y,y+r)`, all three required inequalities are present:

\[
 y\ge2x,\qquad y+r\ge x+y,\qquad 2(y+r)\le3y.
\]

The middle one is `r>=x`, and the last is `r<=y/2`.  Under `y+r>=A`,
the endpoint normalization required by the three-slot theorem is valid.
Its regime-I shift is exactly `(y+r)-y=r`, so its Bellman sum is literally
the four-slot expression, including the exceptional first value `x`.
There is no comparison or dropped term in this reuse.

## 3. Gaussian expansion

For `1/2<=t<1`, the unshifted train has exactly the compact values `0`
and `At` (with a zero net boundary contribution at `t=1/2`).  The shifted
train has compact values `As` and `A(t+s)` precisely when `s+t<=1`.
Expanding these values and the remaining Gaussian tails gives (3.2) and
(3.3).  At equality the additional compact contribution is
`1-e^0=0`, so the formulas match.

## 4. Pulse identity

Direct integration of (4.1) gives

\[
 \sigma([v,\infty))=
 \begin{cases}
  1-e^{-(A-v)^2}-e^{-(A+v)^2},&v\le A,\\
  -e^{-(A+v)^2},&v>A,
 \end{cases}
\]

which is `K(v)`.  The even/odd split
`C(y/2)=C(y)+F_y(y/2)` is exact.  Subtracting threshold tails converts
each difference into the corresponding half-cell interval, proving the
pulse formula.  Absolute convergence follows from Gaussian decay and
linear threshold density.

## 5. Low-period proof audit

The low-period derivative proof uses only the following sign-safe steps.
The tail integral in (5.2) starts one mesh interval before the first
discarded term, so its inequality has the correct direction for decreasing
`h`.  The concavity calculation places `1-s` and `1+s` inside
`[2/3,4/3]`, the
small argument `v` inside `[0,1/2]`, and both tail arguments above `3/2`;
these are exactly the sign ranges of `h''` used in the proof.

For the endpoint certificate, `157/200<pi/4<11/14`.  Odd Taylor truncation
gives the lower bound `Q_5<=exp(-u)`, while the positive Taylor series for
`exp(u)` gives `exp(-u)<=1/P_8(u)`.  The eight intervals in (5.10) exactly
partition `[1/2,2/3]`.  Substitution in (5.11)--(5.12) and rational
cross-multiplication gives the displayed strict margins.  Concavity then
propagates endpoint positivity to the full `s` interval.

Equation (5.14) has the correct scale and sign: differentiating with
respect to normalized `s` contributes one factor `A`, while each kernel
derivative contributes `-2A W_t`; hence `-2A^2W_t`.

## 6. Thin-triangle audit

The extension to `[2/3,4/5]` uses the same strict concavity and the correct
new endpoint `s=1-t`.  In (6.5), `h(t)` is bounded below by the minimum of
its endpoint lower bounds because `h` is unimodal; every negative tail
term is bounded where its argument is smallest.  The `P_10` certificate
retains a positive rational margin even in its final interval.

At an interior critical point, (6.9) is valid because every omitted
argument is at least `d=w+t`.  Multiplying by `d` gives exactly the
coefficients `2+t`, `2`, and `t`; no tail is discarded without being paid
by the critical identity.

The change `(q,p)=(1-t,s)` has domain `0<=p<=q<=1/5`.  The bound
`2/3+1/2+22/35<2` makes (6.12) strictly decreasing in `q`, so `q=1/5` is
the correct worst boundary.  Strong convexity then has margin

\[
 {27\over10}-{14\over5}{5\over12}
 -{4\over5}{13\over20}={76\over75}>1.
\]

Together with `G_*(0)>3/200` and `G_*'(0)>-1/20`, the quadratic minimum
is larger than `11/800`.  The factor `1/2` in that loss is correct.

## 7. Scope audit

The theorem does **not** infer that every pulse has nonnegative `sigma`
mass.  It proves the required pulse-plus-ceiling expression by monotonicity
through `t=4/5` and by direct critical-point pricing above that threshold.
Only the two-slot-efficient regime is closed; the other two `n=4`
efficiency regimes remain open.
