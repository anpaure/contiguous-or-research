# Independent audit: minimum-density run-phase half-defect theorem

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_MINIMUM_DENSITY_RUN_PHASE_HALF_DEFECT_20260803.md`  
**Verdict:** `GO` after scope and marker-notation clarification.

## 1. Marker convention

For a positive coordinate run on the unwrapped carrier vertices
`T_s,...,T_t`, the entry transition is `beta_(s-1)` and the departure
transition is `alpha_t`.  The depth-`d` mandatory source positions are

\[
                         s+d\qquad\hbox{and}\qquad t.
\]

Thus the erosion support `[s+d,t]`, its size `L-d`, and the endpoint span
`L-(d+1)` are correct.  The minimum endpoint-containing owner-window
transversal is

\[
 1+\left\lceil{L-(d+1)\over d+1}\right\rceil
 =\left\lceil{L\over d+1}\right\rceil.
\]

No off-by-one correction is needed.

## 2. Inequality directions

There are exactly `W` positive runs and their total length is `rW`.
Therefore

\[
 P=\sum_R\left\lceil{L(R)\over d+1}\right\rceil
 \le {W(r+d)\over d+1}.
\]

Each occurrence belongs to at most `q` cyclic `q`-cells, so

\[
 H_Z\le {d(d+1)\over2}P.
\]

If `delta` targets are omitted, the retained target rank is at least
`M-delta(r-1)`.  Hence

\[
 M-\delta(r-1)
 \le H_Z+(r-1){d+1\choose2},
\]

which rearranges in the direction stated in Theorem 4.1.  All inequality
directions are correct.

## 3. Exact central-rank masses

For `k=2m+1,r=m+1`,

\[
 \Lambda=4^m-1,
 \qquad
 M={2m+1\over2}\left(4^m-{2m\choose m}\right).
\]

For `k=2m,r=m`,

\[
 \Lambda={4^m-{2m\choose m}\over2}-1,
 \qquad
 M=2m\left(4^{m-1}-{2m-1\choose m-1}\right).
\]

Both follow from

\[
 \sum_{s=1}^{r-1}s{k\choose s}
 =k\sum_{t=0}^{r-2}{k-1\choose t}.
\]

The formulas and the comparison `M/Lambda=r-Theta(sqrt(k))` are correct.

## 4. Half-defect asymptotic

Minimality of `d` gives

\[
 \Lambda-{d(d+1)\over2}\le dW<\Lambda+W,
\]

and hence `Wd=Lambda(1+O(1/d))` with `d=Theta(sqrt(k))`.  Substitution into
either the exact-minimum or canonical-residue bound gives

\[
 M-H_Z
 =\Lambda\left({r\over2}-O(\sqrt{k})\right).
\]

The linear-boundary allowance is `o(Lambda)`.  Division by
`r-1=Theta(k)` yields

\[
 \delta\ge\left({1\over2}-O(k^{-1/2})\right)\Lambda.
\]

The asymptotic coefficient and error scale are correct.

## 5. Scope correction

The half-defect theorem applies to either:

1. one exact minimum owner-hitting net on every positive run; or
2. one residue class modulo `d+1` on every run, with the two mandatory
   endpoints adjoined.

It does not apply to an arbitrary denser signature or to a two-/multi-rail
system.  Independence between run phases is not required: the proof uses
only the deterministic total occurrence bound.  Corollary 4.2 is the
broader statement—it gives a necessary occurrence count for every
signature system, but not half-defect for every such system.

The theorem header, outcome, marker paragraph, and final scope paragraph
were clarified accordingly.  No mathematical formula required correction.

