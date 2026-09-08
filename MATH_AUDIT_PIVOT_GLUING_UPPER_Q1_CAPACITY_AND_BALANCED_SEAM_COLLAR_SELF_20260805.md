# Self-audit: pivot-gluing upper-q1 capacity and balanced seam collar

**Date:** 2026-08-05  
**Method:** independent symbolic re-derivation inside the same pure-math
lane; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`

## Verdict

`GO` at the stated scope.  One wording error was found before freezing and
corrected: `W-1-U` counts transitions which are either above-q1 or duplicate
q1 providers, not duplicate q1 providers alone.  After this correction the
transition ledger, the even/odd specializations, every local owner/union/
intersection formula, and the punctured-forest equivalence agree.

No complementary factor, cross-collar palette matching, higher upper deck,
or all-dimensional word is inferred.

## 1. Witness-to-transition check

Let an interval of distinct rank-`r` owners have union `Z` of rank `r+1`.
Its first two owners are distinct rank-`r` subsets of `Z`; their union has
rank at least `r+1` and is contained in `Z`, so it equals `Z`.  Therefore
every upper-q1 interval witness can be charged to an adjacent transition,
and one transition has only one possible charged value, its union.  This
validates the capacity argument even when a declared witness interval has
more than two owner windows.

## 2. Transition ledger

With `c` components, `b=c-1` bridges, and `s` owners per bridge:

* component owners: `W-bs`;
* component internal transitions: `W-bs-c`;
* bridge internal transitions: `b(s-1)`;
* seams: `2b`;
* total: `W-bs-c+b(s-1)+2b=W-1`.

Thus the collar must contribute at least

\[
 U-(W-bs-c)=U-W+bs+c.
\]

Among `W-1` transitions at most `U` are first providers of distinct q1
targets.  If every q1 target occurs, exactly `W-1-U` transitions are waste;
each waste transition is either above q1 or a repeated q1 occurrence.

Finally

\[
 b(s+1)-(U-W+bs+c)=W-U+b-c=W-1-U.
\]

For `k=2r`, `U/W=r/(r+1)` and `c=W/(r+1)`, yielding collar demand `bs` and
waste `b`.  For `k=2r-1`, `U/W=(r-1)/(r+1)`, yielding the displayed odd
formulas.

## 3. Local collar check

Put `Q'=Q\setminus{q}`.  The full owner sequence is

\[
 P=Q'\cup L\cup\{\rho_1\},\quad
 M_0,\ldots,M_h,\quad
 N=Q'\cup R\cup\{\lambda_1\}.
\]

The left transition removes `rho_1` and inserts `q`; every internal
transition removes `lambda_j` and inserts `rho_j`; the right transition
removes `q` and inserts `lambda_1`.  Hence all are Johnson edges.

The internal upper values are

\[
 U_j=Q\cup\lambda_{j..h}\cup\rho_{1..j}.
\]

Their rho-prefix lengths distinguish them.  The left seam equals `U_1`.
The right seam is `Q union R union {lambda_1}`; the only internal value with
all of `R` is `U_h=Q union R union {lambda_h}`, and `h>=2` makes these
different.  Therefore there are `h+1=s` distinct values in `h+2=s+1`
slots, with one repeat.

The two seam intersections omit `q`, while all internal intersections
contain `q`.  Internal rho-prefix lengths distinguish the latter, and
disjointness of `L,R` distinguishes the two seam intersections.  This
validates complete local lower-q1 distinctness.

The source-state claim is literal: the letter immediately before the
lambda state is `Q' union {rho_1}`, and the letter immediately after the rho
state is `Q' union {lambda_1}`.  Both are nonempty even when `|Q|=1`.

For the prospective protected-endpoint extension, every complete collar has
`h+3=s+2` distinct owners by the preceding checks.  Coordinate symmetry is
transitive on the rank-`r` owner layer, so deduplication leaves a simple
regular `(s+2)`-uniform hypergraph.  The sparse-marking theorem applies with
the unchanged containment-star family.  Since `(s+2)^2/r -> pi/4`, its
`gamma=5` coefficient remains strictly above the even Catalan requirement;
the odd requirement is smaller.  This verifies the conditional endpoint-
protected spread corollary.  It adds no upper-palette resource.

For the unconditional two-shore packing, after `t` collars the even
incidence graph loses at most

\[
 t((s+2)r+s(r+1))
\]

edges.  At `t<W/(r+1)` the residual average degree exceeds `r-2s-2`, so a
subgraph has minimum degree greater than `(r-2s-2)/2>=s+3`.  In the odd
case the exact loss coefficient is
`(s+2)(r-1)+s(r+1)=2r(s+1)-2`; at
`t<W/(2r-1)` the residual average degree exceeds `r-s-3`, again leaving
minimum degree greater than `s`.

Inside a bipartite subgraph of minimum degree greater than `s`, the greedy
collar is valid.  At owner step `j`, at most `j-1` available additions are
deleted original labels.  At upper step `j`, at most the `j` inserted
labels and one protected core label are forbidden.  The final upper choice
forbids one label, and the final owner choice forbids the `h` inserted
labels plus the new label.  Every forbidden count is at most `s`, strictly
below the available degree.  Deleting all chosen vertices after each step
makes both owner resources and the `s` new upper resources globally
disjoint.  This verifies Theorem 2.4 in both parities.  It supplies no
containment-star concentration.

## 4. Even punctured-forest count

The bridge owner bank has `bs` vertices and its sharp service set has `bs`
upper colours.  Hence

\[
 |V_0|-C=W-bs-C=(W-C)-bs=|\mathcal U_0|.
\]

A `C`-component spanning linear forest on `V_0` has exactly that many
edges.  Since the balanced collars have already spent all `b=C-1` allowed
waste transitions, global q1 coverage is equivalent to bijectivity of the
forest edge-union map onto `mathcal U_0`.  This proves both directions of
the reduction.

## 5. Scope exclusions

The following are not consequences of the source theorem:

1. owner-disjoint pivots have upper-disjoint service sets;
2. a deterministic spread owner complement has a prescribed-end rainbow
   linear forest;
3. a Johnson forest lifts to an order-`h` resident literal trace;
4. q1 completeness implies wider upper completeness; or
5. the spread-bank theorem plus this collar proves `B+O(1)`.

In particular, the note narrows the complementary-factor target but does
not close it.
