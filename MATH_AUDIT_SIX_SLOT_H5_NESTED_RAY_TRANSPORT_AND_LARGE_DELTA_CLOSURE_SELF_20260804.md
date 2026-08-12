# Self-audit: six-slot `h=5` nested-ray transport and large-excess closure

**Date:** 2026-08-04  
**Verdict:** **SELF-AUDIT GO.**  The theorem closes the full physical
subrange `A/15<=delta<A/5`; it does not close `0<delta<A/15`.

## 1. Target and scope

The target is

`MATH_THEOREM_SIX_SLOT_H5_NESTED_RAY_TRANSPORT_AND_LARGE_DELTA_CLOSURE_20260804.md`.

Its audited SHA-256 is
`34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a`.

The proof is a uniform analytic lower bound on the already-audited exact
reflected gate.  No face is silently discarded, and no formal-period
statement is promoted to a physical-word claim.

## 2. Two-fifths anchor

At `w=2A/5`, the first four adverse exponents are

\[
 {9\pi\over100},
 \quad {49\pi\over100},
 \quad {36\pi\over25},
 \quad {289\pi\over100}.
\]

With `pi<355/113`, exact `U_24` cross multiplication verifies the lower
Gaussian bounds

\[
 {7535\over10000},
 \quad {2143\over10000},
 \quad {107\over10000},
 \quad {1\over10000}.
\]

Their sum is `9786/10000`, so retaining only them gives

\[
 F(2A/5)<{214\over10000}={107\over5000}.
\]

For the lower bound, the finite positive exponential polynomials at the
lower rational exponents from `pi>333/106` give

\[
 e^{-9\pi/100}<{151\over200},
 \quad
 e^{-49\pi/100}<{43\over200},
\]

\[
 e^{-36\pi/25}<{11\over1000},
 \quad
 e^{-289\pi/100}<{3\over25000}.
\]

The first omitted term is below `1/2000000`, and its successor ratio is
below `1/1000`, so the complete omitted tail is below `1/1000000`.
The complete adverse upper numerator is therefore

\[
 755000+215000+11000+120+1=981121
\]

over one million.  Hence

\[
 F(2A/5)>{18879\over1000000}>{1\over100}.
\]

Both directions in the two-sided anchor are correct.

## 3. Physical ray ordering

The reflected physical polytope gives

\[
 u\le A/6,
 \quad x\le v,
 \quad y\le m,
 \quad v\ge A/5,
 \quad m\ge2A/5,
\]

and

\[
 x\le A/5,
 \qquad y\le2A/5.
\]

Thus the compact part of the exact reflection identity is precisely

\[
 T_5=F(0)-F(u)+F(x)-F(v)+F(y)-F(m),
\]

an ordered three-ray transport.  These inequalities use density and
internal superadditivity only; no endpoint face choice is made.

## 4. Compact prices

The first ray satisfies

\[
 F(0)-F(u)>L-G
 ={44024-53300\over10^6}
 =-{9276\over10^6}.
\]

For the second ray, if `x>=4A/25`, monotonicity handles `v<=A/2`, while
reflection gives \(F(v)<\varepsilon<F(x)\) for `v>A/2`.  If `x<4A/25`, the left
floor is `L`; `v>=A/5` and fixed-threshold monotonicity give the right
price `V_5`, with reflection stronger beyond one half.  Therefore

\[
 F(x)-F(v)>L-V_5
 ={44024-49730\over10^6}
 =-{5706\over10^6}.
\]

For the third ray, the two-sided two-fifths anchor closes both cases.  If
`y>=4A/25`, monotonicity applies up to one half and
\(F(y)\ge F(2A/5)>1/100>\varepsilon\) handles `m>A/2`.  If `y<4A/25`, then
`F(y)>L`, while `m>=2A/5` gives
`F(m)<=F(2A/5)<11/500<L` up to one half and reflection is stronger beyond
it.  Hence

\[
 F(y)-F(m)>0.
\]

Adding yields

\[
                         T_5>-{14982\over10^6}.
\]

The three theta terms cost strictly less than `150/10^6`, producing the
exact adverse constant `15132/10^6`.

## 5. Uniform gain grid

For fixed positive `delta`, the `q`-th summand of `D_delta(w)` is

\[
 e^{-s^2}-e^{-(s+q\delta)^2},
 \qquad s=A+qA+w\ge2A.
\]

Its derivative in `w` is negative because
`s exp(-s^2)` decreases beyond `1/sqrt(2)`.  Thus `D_delta` decreases in
its shift.

The six exact gain arguments have the upper bounds

\[
 0, A/5, A, 2A/5, 4A/5, 3A/5.
\]

After reordering, their gain sum is therefore at least

\[
 \mathcal P_5(\delta)=\sum_{j=0}^{5}D_\delta(jA/5).
\]

This verifies the lower-bound direction in the one-dimensional gate.

## 6. The (A/15) price

The gain increases in `delta`, so the residual interval is minimized at
`delta=A/15`.  Keeping only `q=1` and integrating its Gaussian derivative
gives, with `t_j=(31+3j)/15`,

\[
 D_{A/15}(jA/5)
 >{\pi\over30}t_j e^{-\pi t_j^2/4}.
\]

Exact `U_24` cross multiplication verifies the six lower bounds

\[
 {349\over10000},
 {176\over10000},
 {835\over100000},
 {37\over10000},
 {155\over100000},
 {61\over100000}.
\]

Their `t_j`-weighted sum is exactly

\[
                         {55799\over375000}.
\]

Using `pi>333/106`,

\[
 \mathcal P_5(A/15)
 >{333\over3180}{55799\over375000}
 ={2064563\over132500000}.
\]

The adverse constant is

\[
 {15132\over10^6}={3783\over250000}
 ={2004990\over132500000}.
\]

The exact remaining numerator is

\[
                         2064563-2004990=59573>0.
\]

Hence every point with `delta>=A/15` has

\[
                         \Phi>{59573\over132500000}>0.
\]

## 7. Verdict

**GO** for complete positivity on

\[
                         {A\over15}\le\delta<{A\over5}.
\]

This interval is two thirds, not four fifths, of the positive-excess
range.  The sole remaining inert `h=5` chamber is

\[
                         0<\delta<{A\over15}.
\]
