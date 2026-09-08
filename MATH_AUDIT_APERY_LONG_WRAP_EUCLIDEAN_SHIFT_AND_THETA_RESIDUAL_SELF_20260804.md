# Self-audit: long-wrap Euclidean shift and theta residual

**Date:** 2026-08-04  
**Status:** proof-level self-audit, not an independent audit.  The audited
theorem is
`MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md`
at SHA-256
`0f0e92bba693360a785cf8264cb009698bac7d6ce5fa3d8ccaf98dbb5b49b339`.
No numerical enumeration, finite search, solver, or remote computation was
used.

## 1. Scope checked

The theorem makes exactly two positive claims:

1. the narrow exact-first-carry long-wrap band is positive for
   `4<=h<=1000`;
2. for `h>=1001`, positivity follows from the displayed pure theta gate
   `R_h(x)>=-1/40`.

It does **not** assert the latter gate for all `h`, does not close
multidefect cyclic gaps, threshold overshoot, later first crossing, finite
shoulders, arbitrary Bellman tables, or any OR-word construction.

## 2. Literal clock and endpoint checks

For `x=a/A`,

\[
 W_{qh+r}/A=q(1-x)+rx=q+(r-q)x,
\]

which verifies the normalized functional (0.9) and its derivative (0.10).
At `x=1/(h+1)`, this is `(qh+r)/(h+1)`; the division algorithm with
divisor `h` verifies that `qh+r`, `q>=0`, `0<=r<h`, enumerates every
nonnegative integer once.  Thus the endpoint is the authenticated
arithmetic clock `C(A/(h+1))>0`.

## 3. Euclidean index audit

Put `1/x=2m+lambda`, `0<=lambda<2`, `n=h-1-m`, and `k=m-n`.

* `x>1/[2(h-1)]` gives `m<=h-2`, hence `n>=1`.
* `x<1/(h+1)` gives `2m+lambda>h+1=m+n+2`, hence
  `k+lambda>2`.
* `ix<=1/2` exactly for `i<=m`.
* For `i=m+1,...,h-1=m+n`, the reflected indices
  `(1-ix)/x=2m+lambda-i` are, in increasing order,
  `k+lambda,...,m-1+lambda`.

These checks reproduce (1.6), including exactly `n` reflected terms and
exactly `n+1` theta errors after the initial reflected pair is included.

## 4. Translation-block audit

Writing `lambda=s+theta`, `s in {0,1}`, `0<=theta<1`, the unshifted
comparison block is `k+s,...,m-1+s`.

* If `s=0`, then `k+lambda>2` and `lambda<1` force `k>=2`.
* If `s=1`, then `k+lambda>2` and `lambda<2` force `k>=1`, so
  `k+s>=2`.
* Its last index is at most `m`.

Thus the full comparison block occurs among the positive terms
`2,...,m`.  The shifted intervals have disjoint interiors because their
length is `theta x<x`.  On the increasing side of the unique mode, their
total positive increment is at most `M-f(start)<=M-C`; on the decreasing
side every increment is nonpositive.  This verifies the loss bound
`M-C`, with

\[
 C>{43\over1000},\qquad M<{61\over1000}.
\]

Consequently the non-theta margin is strictly larger than

\[
 2C-M>{86-61\over1000}={1\over40}.
\]

The one-mode deduction is valid because the train is analytic and every
interior critical point is a strict local maximum: two critical maxima
would force an interior critical minimum between them.

## 5. Period cutoff audit

There are `n+1=h-m` theta terms.  The strict pointwise estimate
`|rho|<1/20000` yields

\[
 R_h(x)>-{h-m\over20000}.
\]

If `h=2s`, then `1/(2x)>s+1/2`, so `m>=s`; if `h=2s+1`, then
`1/(2x)>s+1`, so `m>=s+1`.  Therefore

\[
 h-m\le\lfloor h/2\rfloor.
\]

For `h<=1000` this is at most `500`, giving

\[
 S_h(a)>{1\over40}-{500\over20000}=0.
\]

Strictness is retained at `h=1000`.  For larger periods the audit retains
the exact Fourier expression (4.1) and makes no sign claim.

## 6. Verdict

**PASS_SELF_AUDIT.**  The `h<=1000` closure and the `h>=1001` residual
scope follow algebraically from the frozen dependencies listed in the
theorem.  Independent review is still required before treating this
self-audit as external authentication.

