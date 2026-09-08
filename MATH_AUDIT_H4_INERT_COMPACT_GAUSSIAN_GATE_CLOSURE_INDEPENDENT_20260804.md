# Independent audit: closure of the h=4 inert compact Gaussian gate

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md`  
**Method:** exact analytic replay; no sampled minimization or numerical
search.

## Verdict

**PASS.**  The quarter-shift mismatch, compact-kernel slope and range
bounds, ceiling concavity, and three-interval endpoint argument together
prove the scalar gate.  Consequently both inert h=4 faces, and hence the
complete five-slot size-four-efficient branch, are closed.

## 1. Quarter-shift arithmetic

The exact series are

\[
C=1-2e^{-\pi/4}-e^{-\pi}-e^{-9\pi/4}
  -\sum_{n\ge4}e^{-\pi n^2/4},
\]

and

\[
F_A(A/4)=1-e^{-9\pi/64}-e^{-25\pi/64}
-e^{-81\pi/64}-e^{-169\pi/64}-R_q.
\]

Replaying the rational bounds in (1.2)--(1.3) gives exactly

\[
5503/125000<C<221/5000
\]

and

\[
44739/1000000<F_A(A/4)<1129/25000.
\]

The first lower endpoint exceeds the second upper endpoint in the required
order:

\[
44739/1000000>221/5000.
\]

Thus `F_q>C`, and

\[
F_q-C<142/125000<1/800.
\]

The Taylor certificates use only rational bounds on `pi` and alternating
or geometric remainder estimates; the two infinite tails decrease at the
claimed geometric rates.  No decimal premise enters the proof.

## 2. Kernel slope audit

For `t=w/A`, direct algebra gives

\[
h(1-t)-h(1+t)
=\bigl(e^{-a(1-t)^2}+e^{-a(1+t)^2}\bigr)
  (\tanh(\pi t/2)-t).
\]

The Gaussian factor is below one because `K(At)>0` through `A/2`.
The function `tanh(pi t/2)-t` is strictly concave.  Its two endpoint
bounds are correct.  At an interior critical point,

\[
\operatorname{sech}^2(\pi t/2)=2/\pi,
\]

so the substitution `p=2/pi`, `q=sqrt(1-p)` gives the stated value
`q-p arctanh(q)`.  Truncating the positive arctanh series through `q^5`
gives (2.5).  Its right side decreases with `p`; at `p=7/11`, squaring
the positive inequality verifies it is below `1/6`.

Therefore

\[
0<-K'(w)<A/3<8/27<3/10.
\]

The mean-value bound `Delta_K<3 delta/10` follows.  Monotonicity of `K`
and the rational exponential bounds give independently

\[
\Delta_K\le K(A/4)-K(A/2)<569/10000<57/1000.
\]

Both halves of Lemma 2.2 are correct.

## 3. Ceiling concavity and endpoint estimate

For each `q>=1`, the term

\[
-e^{-(A+q\tau)^2}
\]

has positive first derivative and negative second derivative for
`tau>=A`.  Absolute Gaussian convergence permits termwise
differentiation.  Hence `C(tau)` is increasing and strictly concave.

At `tau=6A/5`, the first tail term is below `1/44`, while successive
ratios are below `1/100`.  Thus the tail is below `25/1089<1/40`.
Together with `M>11/125`, this gives

\[
C(6A/5)>63/1000.
\]

## 4. Three-interval gate replay

The preceding lemmas imply

\[
\Xi(\delta)
<{A-4\delta\over30}
+\max\left\{1/800,\min(3\delta/10,57/1000)\right\}.
\]

- On `[0,1/240]`, the loss bound decreases while the ceiling increases;
  the exact margin at zero is `36797/3780000`.
- On `[1/240,19/100]`, the loss is `A/30+delta/6`.  Ceiling minus this
  affine function is concave, so its minimum is at an endpoint.  The first
  endpoint is below the frozen `C(A)` margin.  At the second,
  `19/100>A/5`, so `C(A+delta)>C(6A/5)>63/1000`, while the charged side is
  `16577/270000<63/1000`.
- On `[19/100,A/4]`, the compact range cap is active.  The charged side
  decreases and the ceiling increases, so the already checked left
  endpoint is worst.

This proves the scalar gate uniformly.

## 5. Logical consequence and scope

The previous one-dimensional reduction proves that this scalar gate is
sufficient for both inert faces.  The active face was already independently
closed.  Endpoint normalization is monotone in the correct direction, so
every original size-four-efficient five-slot table is positive.

No statement is made about the other five-slot efficiency branches, all
finite grids, the universal Bellman inequality, or OR words.
