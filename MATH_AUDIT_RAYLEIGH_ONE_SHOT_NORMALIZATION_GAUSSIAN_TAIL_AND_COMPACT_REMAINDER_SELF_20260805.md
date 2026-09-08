# Self-audit: Rayleigh one-shot normalization and compact remainder

**Date:** 2026-08-05  
**Method:** pure mathematical replay; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_ONE_SHOT_NORMALIZATION_GAUSSIAN_TAIL_AND_COMPACT_REMAINDER_20260805.md`  
**Verdict:** **GO.**  The overlap cancellation, terminal socket density,
generic Gaussian-tail domination, transformed-job tail estimate, and
lifting chain are valid.  The theorem leaves one compact configuration
problem and does not reuse the prefix-Hall-failing second equal-level
policy.

## 1. First overlap cancellation

The first transformed job and socket densities are `u'` and `-K'`.
The independently audited one-well theorem proves

\[
                         -K'(t)>u'(t)
 \qquad(0<t<b).
\]

Therefore cancelling `u'(t)dt` on the full overlap is legitimate and
leaves the nonnegative density `g_2=-K'-u'` below `b`, while all remaining
jobs lie above `b`.  The strict endpoint form gives `g_2(b-)>0`.
Subtracting the same one-piece measure from both marginals preserves equal
work.

## 2. Generic tail estimate

For jobs in `((n-1)C,nC)`, equal splitting into `n+1` pieces produces the
density (2.3).  With `m=n+1` and `L=C/(C-y)`, the active inequalities are

\[
                         L<m<2L,
 \qquad my>(m-2)C.
\]

A polynomial times a Gaussian at `my` is consequently bounded by a
polynomial times `exp(-gamma_1 m^2)`.  Its active sum is
`O(L^(d+2)exp(-gamma_1 L^2/2))`, uniformly superexponentially small as the
socket endpoint is approached.  For bands `n>=N`, all demand lies within
`2C/(N+1)` of that endpoint.  A positive terminal socket density therefore
dominates it for all sufficiently large `N`.  This proof is qualitative
and contains no unreported finite check.

## 3. Transformed Gaussian tail

The exact transformed density is the parallel sum `u'=aq/(a+q)`, so
`u'<=a`.  On the far right, `a=K'(r)=j(r)`.  Since `r=t+ell>t` and `j` is
decreasing,

\[
                         u'(t)\le j(t)
                         \le2(A+t)e^{-t^2}.
\]

Thus the generic lemma applies with no asymptotic equivalence assumption.

## 4. Positivity, work, and lifting

Pointwise tail domination makes the removed socket occurrence measure a
literal submeasure.  Equal splitting preserves the first moment of every
band, so the compact remainders retain equal work.  Their supports are
bounded as stated.

To lift a compact solution, first add the explicit equal-split tail, then
the cancelled transformed one-piece density, then one first equal-level
socket per transformed job, and finally the original one-piece density.
Each path receives finitely many additions.  All aggregate marginals are
restored exactly.

The second equal-level subtraction is nowhere used.  Its known prefix-Hall
failure therefore does not affect this compact reduction.  Conversely, the
audit confirms that compactness alone is not being asserted as a
configuration theorem.

