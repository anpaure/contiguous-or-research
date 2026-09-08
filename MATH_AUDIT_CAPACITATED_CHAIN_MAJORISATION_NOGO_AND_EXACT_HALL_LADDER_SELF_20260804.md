# Self-audit: capacitated-chain no-go, Hall ladder, and Boolean interval lift

**Date:** 2026-08-04  
**Method:** independent proof replay from the definitions; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_20260804.md`

## Verdict

**GO**, with the scope restrictions stated in the theorem.

The audit confirms four logically separate claims.

1. Truncated Greene--Kleitman/rank-majorisation cuts are necessary but not
   sufficient for a capacitated chain partition.
2. Once named time slices are fixed, the exact remaining condition is a
   ladder of ordinary Hall matchings plus the conjugate capacity bounds.
3. In the nondecreasing half of the Boolean lattice, a capacity-compatible
   interval rank schedule lifts unconditionally to adaptively chosen named
   skipless chains.
4. Atomic rank schedules need not be interval schedules; the displayed
   connected normal strong-Sperner example separates them strictly.

No claim of an all-`k` atomic-to-interval theorem, prescribed-puncture lift,
literal serialization, or `B(k)+O(1)` follows.

## 1. Necessary cut replay

If `X` is a union of `p` antichains and `C` is a chain, then
`|X cap C|<=p`.  A chain placed in capacity `c_i` also contributes at most
`c_i`.  Summing `min(p,c_i)` is therefore valid for every chain partition.
In a strongly Sperner ranked poset the maximum `p`-family is the union of
the `p` largest ranks, so the theorem uses exactly the proposed cuts.

The quoted Greene--Kleitman formula is pointwise in `p`.  It does not state
that one chain partition simultaneously realizes an externally prescribed
capacity vector.  The counterexample independently verifies that this
quantifier distinction is substantive.

## 2. Hall-ladder replay

From a chain packing, placing the `q`-th element below each chain maximum in
`A_q` gives `|A_q|` equal to the number of chain lengths at least `q`, hence
`|A_q|<=K_q`.  Consecutive chain members give the required injections.

Conversely, the union of the adjacent injections has outdegree one away
from `A_1`, indegree at most one, and strictly decreasing slice index.  Its
components are paths and cannot cycle.  Their conjugate length sequence is
exactly `(|A_q|)`.  If the `j`-th largest path length exceeded `c_j`, taking
`q=c_j+1` would give at least `j` paths but at most `j-1` capacities of
height `q`.  Thus sorted path lengths fit sorted capacities.  This checks
both directions and all zero-capacity cases.

For fixed slices each interface uses disjoint shores at adjacent levels;
the matchings may be selected independently.  Hall is exact.  Selecting
the slices themselves is not encoded by these individual flows.

## 3. Boolean interval-lift replay

For `X subseteq B_s`, the number of upward incidences from `X` is

\[
                              (k-s)|X|.
\]

Every rank-`s+1` set receives at most `s+1` of them, so

\[
 |N(X)|\ge {k-s\over s+1}|X|
          ={C_{s+1}\over C_s}|X|.
\]

On the nondecreasing half this is at least `|X|`.  Hence the current sets
on all labels continuing across a rank boundary have distinct containing
successors.  If `q` labels continue, precisely `n_(s+1)-q` labels start at
the next rank, while at least `C_(s+1)-q` sets remain unused.  The inequality
`n_(s+1)<=C_(s+1)` completes the induction.

The proof chooses the retained named subsets.  It does not prove Hall into
an arbitrary pre-frozen punctured layer.  Complete layers are covered
exactly because their selected cardinality equals the whole rank size.

## 4. Interval formulations replay

For the heterogeneous integer system, the coverage equations count every
interval containing a rank.  The threshold rows count intervals of length
at least `q`.  Conjugate dominance matches the sorted interval lengths to
the sorted capacities, so the system is equivalent to an unlabeled
capacity-compatible interval family.

For equal capacity `D`, the position-by-interval incidence matrix has
consecutive ones in every column and is totally unimodular.  Integral rank
demands therefore give an integral optimum to the minimum-number LP.
Duality yields unrestricted rank weights with every length-`D`-or-shorter
window sum at most one.  Singletons guarantee primal feasibility.

For a nondecreasing histogram, its cells at each fixed height occupy one
suffix of the rank line.  Cutting each suffix into length-`D` pieces uses

\[
 \sum_y\lceil L_y/D\rceil
 =\sum_{j\ge0}n_{m-jD}
\]

intervals.  The ranks `m,m-D,m-2D,...` are pairwise too far apart for one
length-`D` interval to hit twice, so the same expression is a lower bound.
This independently verifies the exact monotone formula.

For any separated rank set `S`, one bin contributes at most
`alpha_(c_i)(S)`, proving the geometric cut.  This cut is only asserted as
necessary in the heterogeneous case; no unsupported total-unimodularity
claim is made for the matrix after the nested length-threshold rows are
added.

For the triangular binomial profile, monotonicity makes the highest
`D`-spaced comb extremal.  The local central estimate gives normalized
mass `sum_(j>=1)exp(-(pi/4)j^2)`, while the active-socket density tends to
`1-exp(-pi/4)`.  Their difference is positive.  The theorem supplies an
elementary bound: twice the first Gaussian term is below `0.946`, the
second is below `0.05`, and the remaining geometric tail is below
`7/2400`; the total is below one.  A product-ratio Gaussian majorant
justifies dominated convergence.  Therefore every separated-spike cut has
a fixed linear margin.  This proves only the all-capacities-upgraded row
count, not compatibility with the true heterogeneous capacity histogram.

## 5. Counterexample replay

The poset has ranks

\[
                              1,3,3,3,3,1.
\]

It is pure and connected.  The three middle-to-middle cover graphs are
perfect matchings; the endpoint interfaces are complete stars.  These
graphs satisfy normalized matching.  The arm with both endpoints plus the
other two bare arms is a symmetric-chain decomposition.

For a union of `p<=4` antichains, using an endpoint consumes a singleton
antichain and leaves at most `3(p-1)` internal elements; without endpoints
there are at most `3p`.  At `p=5` the maximum is twelve internal elements
plus one endpoint, and at `p=6` it is all fourteen elements.  Thus

\[
                         a_p=(3,6,9,12,13,14).
\]

Five capacity-three bins have truncated sums

\[
                         (5,10,15,15,15,15),
\]

so all cuts, including total capacity, pass strictly.  The displayed five
atomic row supports have column sums `1,3,3,3,3,1` and row sizes at most
three.

Ranks one and four are four consecutive positions apart: an interval
containing both has length four.  Hence a length-three row meets at most one
of them, but their combined demand is six.  Five interval rows cannot
work.  At poset level, every chain meets internal elements from only one
arm, and each four-element arm needs two capacity-three chains.  Six chains
are necessary.  Both obstructions agree.

## 6. Boolean-frontier replay

For `N=2^k`, Boolean width `W`, `a=floor(N/W)`, and `b=N-aW`, the balanced
capacity multiset has `b` entries `a+1` and `W-b` entries `a`.

For `p<=a`, its truncated sum is `pW`, which dominates the sum of the `p`
largest Boolean ranks.  For `p>=a+1`, its truncated sum is `N`.  Thus all
rank cuts pass.  A chain packing under these capacities has total chain
size `N`, equal to total capacity, so every bin is saturated and the chain
sizes are exactly floor/ceiling.  This is the stated Furedi frontier.

The direct hypothetical majorisation implication already contains the
uniform-chain frontier.  The interval-lift theorem is only one-sided and
does not, without an additional middle-rank gluing argument, lift an
arbitrary full-lattice balanced interval histogram.  In the actual
lower-ideal application all ranks are in the nondecreasing half, where the
interval-lift theorem applies exactly.

## 7. Final scope

The theorem validly replaces the false implication

\[
 \text{rank majorisation}\Longrightarrow\text{named chains}
\]

by the proof-safe chain

\[
 \text{heterogeneous interval integer system}
 \Longrightarrow
 \text{adaptively named Boolean chains},
\]

or, for fixed literal target families, by the exact named Hall ladder.
The actual triangular binomial histogram still has to be shown feasible in
the interval integer system, and its chain maxima still have to be attached
to compatible literal collar sockets.  Those are not inferred here.
