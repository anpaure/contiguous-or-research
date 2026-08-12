# Audit of the architecture-free additive-C diagonal normalization

**Date:** 2026-08-03  
**Audited source:**
`MATH_THEOREM_ARCHITECTURE_FREE_ADDITIVE_C_DIAGONAL_RUN_NORMALIZATION_20260803.md`

## 1. Scope checked

The source proves a necessary condition on an arbitrary universal word
`A` of length `W+d(k)+C`.  It does not assume or conclude a cyclic carrier,
a Johnson order, or an exact lower compiler.  Its quantitative conclusion
is only

\[
 \sum_i|A_i|=\Omega_C(rW).
\]

The proof uses no computation and no finite certificate.

## 2. Endpoint ledger

For one selected rank-`r` target per target, shortening at fixed start to
the first rank-`r` prefix preserves its value.  Distinct equal-rank values
cannot occur on nested intervals.  Therefore starts and ends are both
strictly increasing.  For `W` ordered integers in `[W+e]`, their
displacements from `1,...,W` lie in `[0,e]` and are monotone.

Exactly `e` start columns are unselected.  The monotone-deadline depth cap
is `e`, so they contain at most `e^2` lower cells.  This verifies

\[
 \sum_t(e-h_t)\le eW-\Lambda+e^2.
\]

No equality or flatness inference is used.

## 3. Diagonal blocks and trimming

The excess start gaps total at most `e`; the excess end gaps do likewise.
Hence at most `2e` cuts are made.  Inside one block both endpoints advance
by one and the literal row has a fixed depth.

For a depth-`h`, length-`m` block, retaining its first `(m-h)_+` owners
makes its source span end at the last selected **start** of that block.
Successive blocks therefore have disjoint source spans.  At most `h^2`
proper-prefix cells are removed per block, so the total loss is `O(e^3)`.

This disjointness is essential: without the right trim, a physical source
occurrence could be charged in several adjacent blocks.

## 4. Deep-row target coverage

The trimmed proper-prefix cells cover every lower target except those lost
in an unselected column or in the trimmed block tails.  Hence their number
is at least `Lambda-O(e^3)`.

The total depth deficit from `e` is therefore

\[
 O_C(W)+O(e^3).
\]

A block with depth below `e/2` spends more than `e/2` deficit per owner.
Thus shallow blocks have `O_C(W/e)` owners and `O_C(W)` proper-prefix
cells.  Removing them loses at most `O_C(W)` named targets.  Multiplying by
the maximum target rank gives the proof-safe rank-mass loss `O_C(kW)`.

## 5. Clipped-run accounting

For an internal positive owner run `[s,t]` at depth `h`, the first and last
source markers are forced to be `s+h` and `t`; gaps are at most `h+1`.
For a boundary run of length at least `h+1`, adjoining the missing canonical
endpoint marker gives the same gap system.  Actual markers outside the
canonical erosion interval affect at most `h` starts in each of `h` rows,
per touched boundary.  Short runs can only touch a boundary and contribute
at most `h(h+1)` incidences.

There are at most two boundary runs per coordinate per block.  With at
most `2e+1` blocks, the total clipped/short error is `O(ke^3)`, polynomial
and therefore negligible relative to `W`.

## 6. Run and occurrence conclusions

The retained rank mass is `M-O_C(kW)`.  Since

\[
 erW-M
 =r(eW-\Lambda)+(r\Lambda-M)
 =O_C(kW),
\]

and every deep long run pays at least `e^2/8` in the clipped-run upper
ledger, the number of long runs is `O_C(W)`.  Short runs add only a
polynomial term.

The total augmented gap length is

\[
 S=rW-O_C(eW),
\]

while the convex gap energy is `J=O_C(kW)`.  Therefore

\[
 G\ge {S^2\over S+2J}=\Omega_C(rW).
\]

At most `O(ke)` virtual markers were added.  All actual charged markers lie
in disjoint source spans, so they inject into the literal incidences of
`A`.  This verifies the final density conclusion.

## 7. Claims deliberately not made

The proof does not yield:

* a single flat row;
* Johnson adjacency;
* `W+O_C(1)` runs;
* the sharp fixed-carrier density coefficient;
* sufficiency of any dense schedule;
* an additive-constant upper construction.

Those exclusions are mathematically necessary.  The result closes only
the qualitative normalization premise in the lower-density obstruction.

