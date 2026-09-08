# Audit of the PBBS low-target one-cell Hall reduction

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_PBBS_LOW_TARGET_ONE_CELL_GATE_AND_HOOK_SECTOR_HALL_REDUCTION_20260806.md`  
**Verdict:** **PASS**, with the explicit width-one and Hall scope below.

## 1. Local equivalence

For every depth-resident component, any antecedent is coordinatewise
bounded by the maximal envelope and contains every mandatory core.  Hence
`F_t subseteq S subseteq P_t` is necessary for setting one literal letter
to `S`.  With one free position it is sufficient by the already-proved
short-gap theorem.  The multi-position statement invokes only the same
theorem on maximal changed blocks of length at most `d`.

No matching, action-angle, or probabilistic premise enters this local
equivalence.

## 2. Counting ledger

The envelope rank is `R=m-d`.  A mandatory core of size `f in {1,2}`
belongs to exactly

\[
                         \binom{R-f}{s-f}
\]

rank-`s` subsets of its envelope.  The maximum occurs at `f=1` in the
stated range.  A gamma-one height-`d+1` hook component has length
`L=n(2d+1)`.  This verifies the support upper bound and the exact ratio in
Section 4.

Even if every cyclic interval, rather than only one-cell tickets, is
allowed, one component has at most `L^2` occurrence-labelled intervals.
Thus the fixed-few-component no-go remains valid independently of the
mandatory-core model.

## 3. Hook-sector supply ledger

For `p=2d+1` and `b=m-d-1`, weak compositions number

\[
 \binom{b+p-1}{p-1}.
\]

Fixing the terminal coordinate to zero leaves `p-1` coordinates and gives

\[
 \Omega_0=\binom{b+p-2}{p-2}
          =\binom{m+d-2}{2d-1}.
\]

Each relative rooted shape has `n` physical root placements.  The native
hook theorem makes every such zero-terminal phase an exact-run loop, so
the total `n Omega_0` is exact.  Multiplication by
`binom(R-1,s-1)` gives the candidate-incidence count.

For `s=d=Theta(sqrt(m))`, standard binomial logarithms give

\[
 \log\Omega_0=2d\log(m/d)+O(d),
\]

while

\[
 \log\left(
 {n\binom{R-1}{d-1}\over\binom nd}
 \right)=-d\log2+O(d).
\]

Their sum is the claimed
`2d log(m/d)+O(d)`.

## 4. Hall scope

The theorem does not infer minimum target degree from average degree.
The hook host has cyclic, not full symmetric, coordinate invariance.  The
later exact survivor classification shows that the naive loop-only Hall
statement is false: adjacent and distance-two pairs have zero loop degree.
Those two structural-zero orbits are nevertheless repaired by native
multi-cell/nonloop tickets, closing rank two.

The open Hall statement is now the short-interval component graph for
ranks `3,...,d`.  If it holds, matching each target to a distinct component
makes the short-block condition automatic.  Failure would refute only that
native hook-interval route; it would not refute nonhook PBBS sectors or a
bounded rethread.

## 5. Global scope exclusions

The reduction does not claim:

1. that every hook survivor envelope contains every low target;
2. that average multiplicity implies an SDR;
3. residence of nonhook components;
4. a completed global source word or common cap; or
5. `nu(k)<=B(k)+O(1)`.

Within those exclusions, the local criterion, few-component obstruction,
exact hook-sector supply, and final Hall formulation are proof-safe.
