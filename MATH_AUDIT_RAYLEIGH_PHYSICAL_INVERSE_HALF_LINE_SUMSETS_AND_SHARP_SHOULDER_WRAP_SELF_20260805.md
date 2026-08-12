# Self-audit: physical inverse half-line sumsets and the shoulder-wrap barrier

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_PHYSICAL_INVERSE_HALF_LINE_SUMSETS_AND_SHARP_SHOULDER_WRAP_BARRIER_20260805.md`  
**Method:** independent symbolic replay of every displayed identity; pure
mathematics, with no computation, enumeration, search, or solver  
**Verdict:** **PASS SELF-AUDIT after two corrected typographical statements.**
The physical generalized inverse is subadditive on the half-line, but is
not monotone after subtracting the identity; the theorem now states
monotonicity only for the inverse `B`.  The inverse shoulder is nonnegative;
the missing backslash in that displayed inequality has also been repaired.
The Bellman counterfamily is exact and proves that an unsigned finite-circle
variance extension is false in the intended saturated first-minimum class.

## 1. Half-line inverse

For

\[
 B(t)=\min\{n:A_n\ge t\},
\]

superadditivity gives

\[
 A_{B(s)+B(t)}\ge A_{B(s)}+A_{B(t)}\ge s+t.
\]

Thus `B(s+t)<=B(s)+B(t)`.  Subtracting `s+t` proves subadditivity of
`u=B-id`.  The bound `A_n<=n` excludes every integer `n<t`, hence
`B(t)>=t` and `u>=0`.  Notice that `u` is generally a descending sawtooth
between jumps and is not nondecreasing.  The corrected source does not
claim otherwise.

If `A<=bar A`, the hitting time for `A` is no earlier than that for
`bar A`, so `u>=bar u`.  No Bellman recurrence beyond superadditivity is
needed for these assertions.

## 2. Tail translation

Choose `N` divisible by the formal period `g` and beyond the index
conductor.  Then

\[
 A_{N+m}=\bar A_{N+m}=N+\bar A_m.
\]

The candidate `N+bar B(t)` reaches `N+t`.  An index below `N` cannot,
because `A_n<=n<N+t`; among indices at least `N`, subtracting `N` gives
exactly the formal inverse problem.  Therefore

\[
 B(N+t)=N+\bar B(t),\qquad u(N+t)=\bar u(t).
\]

Since `bar u` is `N`-periodic, this also proves `u=bar u` for every
argument at least `N`.  Hence `eta=u-bar u` is nonnegative and compactly
supported.

For almost every `t`, `B(t)` is the number of clock points strictly below
`t`.  Subtracting the two counting functions and integrating the resulting
finite interval indicators proves

\[
 \int eta=\sum_n(\bar A_n-A_n).
\]

Restoring physical units multiplies the right side by `1/lambda`, exactly
as stated.

## 3. Wrapped sums

For a nonwrapped pair, half-line subadditivity applies directly.  If
`x+y=N+z`, tail translation gives

\[
 \bar u(z)=u(N+z)=u(x+y)\le u(x)+u(y).
\]

Adding `eta(z)=u(z)-bar u(z)` proves the displayed wrapped inequality.
In index coordinates, half-line subadditivity gives

\[
 d_z=e_{N+z}\le e_r+e_s,
\]

and `e_z=d_z+delta_z`, proving the equivalent formula.  The source calls
`eta` the canonical error term, not the minimum error for every fixed
representation.

## 4. Sumset and quantile inequalities

If `x` and `y` lie in two block sublevel sets, their real sum lies in one
of two adjacent output strips.  One-dimensional Brunn--Minkowski gives

\[
 |E+F|\ge |E|+|F|,
\]

and splitting the sumset at the period boundary proves the two-block
inequality.  Iteration gives `p` adjacent output strips and the stated
multi-block formula.  The positive-measure hypothesis avoids the empty-set
convention in Brunn--Minkowski.

If one input is translated into the formal tail, both carry outcomes have
the same formal phase modulo `g`.  Connected-circle Kneser then gives the
mixed formula and its generalized-quantile version.

This mixed result is correctly identified as one-sided: `u_q>=u_infty`
implies `Q_q>=Q_infty`, so formal quantile subadditivity already implies
the mixed bound.  No physical upper-quantile conclusion is smuggled into
the theorem.

## 5. Finite inverse moments

On the cell

\[
 n-e_n<t<n+1-e_{n+1},
\]

one has `u(t)=n+1-t`.  Therefore

\[
 \int u={1\over2}\sum_n((1+e_n)^2-e_{n+1}^2)
       ={N\over2}+\sum_{n<N}e_n,
\]

and

\[
 \int u^2={1\over3}\sum_n((1+e_n)^3-e_{n+1}^3)
       ={N\over3}+\sum_{n<N}(e_n+e_n^2),
\]

using `e_0=e_N=0`.  Normalization and subtraction of the squared mean give
the exact `1/12+Var(e)` formula.

For prefix sublevel sets, subadditivity of `e` gives set inclusion under
ordinary integer addition.  The torsion-free inequality
`|X+Y|>=|X|+|Y|-1` proves the CDF and ordered-quantile statements with the
correct `-1` index.

## 6. Counterfamily audit

Let `N>=2M`, `lambda=zeta/N`, and use the table

\[
 c_j=0\ (j<M),\qquad c_j=\lambda j\ (M\le j\le N).
\]

For `i+j<=N`, the left side of internal superadditivity is either zero or
`lambda(i+j)`, while the right side is at most `lambda(i+j)`.  Every
proper displayed value is below `zeta`, and the endpoint is `zeta`.
The proper partition `N=M+(N-M)` is legal because both parts are at least
`M`; maximum density bounds its value from above by `zeta`, so saturation
is exact.

The consecutive critical set `M,...,N` has gcd one.  Every capacity in
`[M,N]` is a critical denomination.  For `n>N`, repeatedly subtract `M`;
the first remainder at most `N` is strictly greater than `N-M>=M`.
Therefore every `n>=M` is critically representable, while every `n<M`
has only zero-valued fills.  This proves

\[
 V_n=0\ (n<M),\qquad V_n=\lambda n\ (n\ge M).
\]

The normalized defects are `0,1,...,M-1,0,...`.  With

\[
 S_1={M(M-1)\over2},\qquad
 S_2={M(M-1)(2M-1)\over6},
\]

the proposed cyclic variance inequality becomes

\[
 N(3S_2-S_1)\le4S_1^2.
\]

Both sides contain `M(M-1)^2`, and cancellation gives exactly `N<=M`.
Thus it fails throughout the asserted range `N>=2M`.

For each `1<=z<M`, the wrapped decomposition

\[
 M+(N-M+z)=N+z
\]

has two zero-defect inputs and output defect `z`, so the wrap shoulder is
attained exactly.

Finally `lambda m<lambda M<=zeta/2` for every defective index.  Strict
decrease of `K` before its minimum gives

\[
 K(0)-K(\lambda m)>0.
\]

Thus the large unsigned variance failure is entirely favorable in the
signed Rayleigh functional.  This validates the source's conclusion that
the remaining theorem must distinguish sub-minimum credit from
post-minimum debt.

## 7. Scope

The theorem proves:

1. physical half-line inverse subadditivity;
2. exact inverse-shoulder area and tail translation;
3. the canonical wrap-error identity;
4. expanding-horizon connected-sumset and quantile inequalities; and
5. a saturated Bellman no-go to direct finite variance closure.

It does **not** prove a two-sided physical quantile majorization, sign the
finite shoulder, prove all-price positivity, or imply an OR-word upper
bound.  The surviving target is the signed transport of above-minimum
shoulder debt into below-minimum credit plus the strict formal reserve.

