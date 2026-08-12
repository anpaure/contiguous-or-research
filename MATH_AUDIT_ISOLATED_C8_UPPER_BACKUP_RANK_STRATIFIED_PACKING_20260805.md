# Audit of rank-stratified isolated-`C8` upper-backup packing

**Date:** 2026-08-05  
**Method:** independent symbolic inequality and quantifier replay; no
computation or search  
**Audited theorem:**
`MATH_THEOREM_ISOLATED_C8_UPPER_BACKUP_RANK_STRATIFIED_PACKING_20260805.md`

## 0. Verdict

**PASS at stated scope.**  The rank-two bottleneck is no longer borderline.
There are at most `2L` distinct casualties of each fixed excess rank, not
`2L^2`, and a rank-ordered greedy stabilizer choice gives pairwise
vertex-disjoint alternative witnesses for the complete isolated-collar
damage set when `L=Theta(sqrt r)`.

The result is a path-packing theorem.  It does not invoke the small
protected-factor theorem outside its `m-2` edge range and does not claim to
protect grafted exterior intervals.

## 1. Rank census replay

For one cyclic start, endpoint extension gives a nested sequence of union
sets.  Equal ranks inside a nested sequence imply equal sets.  Thus one start
contributes at most one distinct rank-`(r+s)` target.  Two cycles with `L`
starts each give `|cal D_s|<=2L`.

A cyclic interval of `ell` owners can be cut to an incidence path on `ell`
owners and `ell-1` facets without changing its owner union.  Therefore each
stratum contributes at most `2L^2` vertices to either shore.  A Johnson path
of at most `L` owners has union rank at most `r+L-1`, so fewer than `L`
strata occur.

For the literal screen lattice, all occurrences of a coordinate occupy one
source residue modulo `d+1`.  The incoming coordinates of any `d` consecutive
Johnson transitions are therefore distinct and absent from the initial
owner.  Hence an `ell<=d+1` owner interval has rank `r+ell-1`, and every
shortest excess-`s` witness for `s<=d` has exactly `s+1` owners.

Every casualty witness crosses one of the four changed hinge edges.  An
`s+1`-owner interval contains `s` cycle edges, so at most `s` starts cross a
fixed hinge.  Therefore `|cal D_s|<=4s` and the complete span mass in the
low stratum is at most `4s(s+1)`.  In particular there are at most eight
excess-two casualties.

## 2. Greedy denominator replay

At excess two, every backup has three owners and two facets, and there are at
most eight such targets.  Only the collar and earlier members of the same
stratum have been selected.  The forbidden owner and facet shores have size
less than

\[
                         2L+24\quad\hbox{and}\quad2L+16.
\]

The two avoidance terms are `O(L/r^2)` and `O(L/r^3)`.  Thus the formerly
borderline stratum actually has substantial polynomial room.

For every excess at least three, the complete earlier path bank has at most
`2L^3` vertices per shore.  The smallest owner and facet orbits are
`binom(r+3,3)` and `binom(r+3,4)`.  The two avoidance terms are therefore
`O(L^4/r^3)` and `O(L^4/r^4)`, again tending to zero.

The greedy forbidden bank contains every previously selected owner and
facet, so the resulting paths are genuinely pairwise vertex-disjoint, not
merely target-distinct.

## 3. Scope replay

The path union can have `O(L^3)=O(d^3)` incidence length.  Since
`d=Theta(sqrt r)`, this is not bounded by the `m-2` hypothesis of the
currently available protected-factor extension theorem.  No factor-extension
claim is made.

The `2L`-per-rank argument depends on the two finite cyclic address spaces of
the isolated collar.  It does not apply to intervals with arbitrary exterior
endpoints after a PBBS graft.  The theorem states this limitation.
