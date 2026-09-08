# Self-audit: first-exit paired bank, one-Hall reduction, and two-wrap reset

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_FIRST_EXIT_PAIRED_BANK_SINGLE_HALL_AND_TWO_WRAP_RESET_20260803.md`  
**Method:** independent symbolic audit of interval addresses, upper-label
runs, and opening cuts.  No solver or finite search is used.

## 0. Verdict

**GO at the stated conditional regeneration scope.**

The complete cyclic bundle and the exact two-loss opening are unconditional
under the theorem's owner, source, and upper-surjectivity hypotheses.  The
single-Hall reduction is exact only after one complete cap/background state
defines which seam bundles each ticket accepts.  The recurrence remains
conditional on the independently required Pascal overlay.

## 1. Bundle audit

The port, owner, and plateau/exit interval lengths are respectively

\[
                         d,\quad d+1,\quad d+t+1.
\]

For `t>=1` these length classes are distinct.  At a fixed plateau length,
the cyclic start recovers `i` because the length is below `W`.  Thus no two
different seam bundles share a finite interval-address vertex in one
phase.  The phase-one owner shift is a permutation, so it is equally
injective.

The q1 diamond gives the port-to-owner-to-immediate-upper part.  Minimality
of `h_i` makes all `z_(i,t)` for `t<h_i` have value `R_i`, and the last one
has value `V_i` of rank `r+2`.  The theorem correctly records the plateau
as same-value occurrence transport, not as a sequence of strict Boolean
Hasse steps.

## 2. Run audit

If `R_i` stays constant for `L` edges, the corresponding `L+1` owners are
distinct facets of one rank-`(r+1)` set.  Hence `L<=r`.  At position `q`
of the run, exactly `L-q` upper edges beginning there retain the label,
and the first outside owner is one step later; therefore
`h_i=L-q+1`.  The run contribution is

\[
                         (L+1)+L+\cdots+2={L(L+3)\over2}.
\]

Upper surjectivity implies at least
`U=binom(2r-1,r+1)` runs, since one run has only one label.  Consequently

\[
 \sum_j(L_j-1)=W-J\le W-U={2W\over r+1}.
\]

Using `L_j<=r` gives

\[
 {1\over W}\sum_i h_i
 \le2+{r\over r+1}<3.
\]

All inequalities have the correct direction; multiple separated runs with
the same upper value only increase `J` and strengthen the bound.

## 3. Opening audit

After a cut, the standard linear source word has one revolution plus `d`
repeated letters.  A longest bundle interval starting at relative position
`t` ends at `t+d+h_i`; the last available index is `W+d-1`.  Thus the
bundle is lost exactly when

\[
                         t+h_i\ge W.
\]

For fixed `i`, exactly `h_i` of the `W` cuts satisfy this inequality.
Therefore the average loss is `sum_i h_i/W<3`.  At every cut the starts in
positions `W-1,W-2` are lost because `h_i>=2`; hence every loss count is at
least two.  An integer average below three forces a cut of loss exactly
two.  This proves the sharp opening statement.

The result depends on upper surjectivity.  A simple Johnson row alone only
gives `h_i<=r+1`, hence an `O(r)` generic opening bound.

The q1-only wrap count is one because its extra extension beyond the owner
window is one.  The paired bank's first-exit extension is at least two, so
its wrap count cannot be one.  The theorem correctly distinguishes these
two statements.

## 4. Acceptance-graph audit

Once a complete state is fixed, an accepted edge `x i` means the entire
two-coordinate route at seam `i` is legal.  Distinct seam indices give
disjoint bundles, so the only remaining selection constraint is choosing
distinct indices.  This is exactly bipartite matching, and Hall's formula
is exact.

This reduction would be false if the two coordinates were selected
independently, if a cross-ticket resource remained unpriced, or if cap
states were mixed.  All three cases are explicitly excluded in the graph
definition.

## 5. Recurrence scope audit

The paired bank uses existing child intervals and so charges no fresh split
position.  Nevertheless it does not map inherited charged positions into
the child baseline.  The recurrence therefore retains the explicit
quantity `kappa_m`.  One omitted logical ticket has two declared occurrence
coordinates and, without an extra coalescing theorem, is repaired safely by
at most two appended literal target masks.  This justifies the coefficient
`2e_m` in (5.1).  Adding the previously named reset/background/upper defects
then gives the displayed append-only recurrence.

Only the additional hypothesis `kappa_m=0` produces a true reset.  The
theorem does not assert that hypothesis.  It therefore proves that the
two-cross socket **capacity** row is replaced, but not that same-parity
regeneration is complete.
