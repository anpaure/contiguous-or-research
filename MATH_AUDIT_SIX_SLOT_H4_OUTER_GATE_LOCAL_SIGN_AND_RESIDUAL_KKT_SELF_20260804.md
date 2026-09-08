# Self-audit: six-slot `h=4` outer-gate local sign and residual KKT theorem

**Date:** 2026-08-04  
**Verdict:** **GO**, with the scope restriction stated in the theorem.  The
two relaxed gates are proved positive only on the certified initial
interval, and are proved negative at the formal far endpoint.  This is a
sign theorem for the relaxation, not a complete physical `h=4` closure.

## 1. Audited artifact

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md` | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |

The reduction on which it depends is frozen at
`f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3`
and independently audited at
`f92d2d444c23cbc7366820d367935a9db5bbd304faafcd73e53f445963a5ee0e`.

## 2. Kernel-slope audit

For `w=At`, direct differentiation gives

\[
 {-K'(At)\over2A}
 =h(1-t)-h(1+t),
 \qquad h(s)=se^{-A^2s^2}.
\]

Factoring the difference gives exactly

\[
 \left(e^{-A^2(1-t)^2}+e^{-A^2(1+t)^2}\right)
 \left(\tanh(\pi t/2)-t\right).
\]

On `0<=t<=1/4`, the second factor is nonnegative and smaller than

\[
 (\pi/2-1)t<(4/7)(1/4)=1/7<1/6,
\]

and the first is `1-K(At)<1`.  Together with `A<8/9`, this gives
`-K'<8/27<3/10`.  The weak sign follows from
`arctanh(t)<=pi t/2`, with equality only at `t=0`; the already audited
quarter-to-half lemma supplies the rest of the interval.  This verifies
the corrected (1.2).

For `q>=1`, `K'(qA+w)>0`.  Therefore the negative part of `F'` is bounded
in magnitude by `-K'`, and integration gives the asserted weak `3/10`
downward-variation bound (strict for a nonzero displacement).  The strict
cap `61/1000` follows independently from
`F(s)<61/1000` and `F(t)>0`.  No monotonicity of the whole train on the
first quarter is assumed.

## 3. Envelope audit

### 3.1 Active pair

For `b in [0,B_delta]`,

\[
 b+\delta\le {A+\delta\over3}\le A/2.
\]

Period monotonicity and reflection give

\[
 F_\tau(b+\delta)+F_\tau(A-b)
 >F(b+\delta)-F(b)-\varepsilon,
\]

and the displacement is exactly `delta`.  Hence

\[
 \mathcal H>C(\tau)-D-\varepsilon.
\]

### 3.2 Inactive pair

Both entries of the inner minimum increase when the period is raised.
The exact algebra

\[
 F(b)-\min\{C,F(m)\}
 =\max\{F(b)-C,F(b)-F(m)\}
\]

is correct.  The first member is below

\[
 {61\over1000}-{5503\over125000}
 ={2122\over125000}=\eta,
\]

and the second is at most `D`, because `0<=m-b<=delta`.  The strict
reflection comparison preserves the strict envelope bound.  This verifies
the inactive bound without assuming which branch of the minimum is active.

### 3.3 Singleton and half-period train

When `A/2<w<=tau/2`, the reflected coordinate
`v=A-w` lies in `[(A-delta)/2,A/2]`, a subinterval of `[A/4,A/2]`.
The train is decreasing there, and its loss from `v` to `A/2` is at most
both `3delta/20` and `F(A/4)-F(A/2)`.  This checks (2.8).

The identity

\[
 C(\tau/2)=C(\tau)+F_\tau(\tau/2)
\]

is an exact even/odd split of the `tau/2` train, so the same estimate
checks (2.9).  Adding the envelopes gives (2.11); for the `XY` gate the
only relaxation is `D+max{eta,D}<=2max{eta,D}`.

## 4. Rational interval arithmetic

Concavity first gives a convex combination of the two actual endpoint
values.  Replacing each endpoint separately by its certified lower bound
produces the comparison coefficient

\[
 {45\over8}\left({63\over1000}-{5503\over125000}\right)
 ={45\over8}{2372\over125000}
 ={5337\over50000}.
\]

The switch point is

\[
 {10\over3}{2122\over125000}={1061\over18750}=\delta_0.
\]

Before that switch, the common minorant is

\[
 {5503\over125000}
 -2{2122\over125000}
 -{1\over40000}-{3\over20000}
 +\left({5337\over50000}-{3\over20}\right)\delta
 ={9897\over1000000}-{2163\over50000}\delta.
\]

Using `delta_0<3/50`, its margin is at least

\[
 {9897\over1000000}-{6489\over2500000}
 ={36507\over5000000}>0.
\]

After the switch, the minorant is

\[
 {5503\over125000}-{1\over40000}-{3\over20000}
 -\left({3\over5}+{3\over20}-{5337\over50000}\right)\delta
 ={43849\over1000000}-{32163\over50000}\delta.
\]

Its zero is exactly

\[
 {43849\over1000000}{50000\over32163}
 ={43849\over643260}=\delta_*.
\]

The elementary cross-products verify

\[
 \delta_0<3/50<\delta_*<7/100<A/5,
\]

and `7/100<61/300`, so neither the displacement cap nor the chord domain
is crossed.  Although the displacement bound is weak at zero displacement,
the reflection and certified endpoint comparisons retain strictness in
the gate minorant.  Positivity at `delta_*` is therefore strict.

## 5. Endpoint expansion audit

At `delta=A/2`, `tau=3A/2` and `B_delta=0`.  The chosen envelope test
points give

\[
\begin{aligned}
 \mathfrak G_{XY}(A/2)
 \le{}&C(\tau)+2F_\tau(A/2)+F_\tau(A)\\
 &+F_\tau(2A/3)+F_\tau(3A/4),
\end{aligned}
\]

and

\[
 \mathfrak G_Z(A/2)
 \le C(3A/4)+2F_\tau(2A/3)+2F_\tau(A/2).
\]

The exponents in the compact terms are respectively

\[
 {\pi\over4},\ {\pi\over16},\ {9\pi\over16},\ \pi,
 {\pi\over36},\ {25\pi\over36},\ {\pi\over64},\ {49\pi\over64}.
\]

For `C(3A/4)`, the first tail after the two compact terms has exponent
`25\pi/16`.  Thus the displayed expansions contain neither a missing
positive constant nor an incorrectly signed tail.

Putting the theorem's rational lower bounds over denominator `10000`
gives the exact endpoint ledgers

\[
\begin{aligned}
 XY:quad
 &9118+16432+3412+432+9163+1127+9520+901\\
 &=50105,\\[2mm]
 Z:quad
 &9118+9520+901+73+16432+3412+18326+2254\\
 &=60036.
\end{aligned}
\]

Hence the upper bounds are `5-50105/10000=-21/2000` and
`6-60036/10000=-9/2500`.  The degree-24 exponential majorant has positive
denominator in every row because the largest rational exponent is
`275/56<26`; its geometric-tail estimate is therefore valid.

## 6. Continuity and KKT audit

`mathcal I` is the minimum of a continuous function on a fixed compact
interval.  Parameterizing `b=tB_delta` and `w=t tau/2` puts the other two
minima on fixed compact unit intervals.  Thus both gates are continuous
through `delta=A/2`.  Positivity at `delta_*` and negativity at `A/2`
force a zero strictly between them.

For the residual ledger,

\[
 R_\tau-T_\tau
 =-K'(w)+\sum_{q\ge1}(q-1)K'(q\tau+w)
\]

is obtained by coefficient subtraction term by term.  Every term of
`R_tau` is positive.  Thus `T_tau(w)=0` implies `R_tau(w)>0`; on the half
band, `K'(w)<0` also makes `R_tau-T_tau>0`.  The complementary-pair
identity (5.5) is algebraically exact and is not assigned an unsupported
sign above the half band.

The inner candidate list contains all fixed endpoints, the moving `H`
endpoint, the `I` clip and cap switches, the smooth derivative equations,
and the moving `S` endpoint.  The outer list separately includes smooth
stationarity, the correctly oriented one-sided condition
`partial_-<=0<=partial_+`, outer endpoints, and the gate-zero equation.
The theorem does not confuse this local-minimum condition with the weaker
unordered Clarke convex-hull condition.  No smooth or nonsmooth branch is
omitted.

## 7. Scope audit

The theorem correctly distinguishes three statements:

1. the gates are positive on an explicit initial interval;
2. the gates themselves become negative near the formal far endpoint;
3. negative relaxed gates do not imply a nonpositive physical table,
   because independently minimized envelopes may be incompatible.

Accordingly, **GO** means the local sign theorem and obstruction are
proved.  It does not mean that six-slot `h=4`, the Bellman inequality, or
an OR-word construction is closed.
