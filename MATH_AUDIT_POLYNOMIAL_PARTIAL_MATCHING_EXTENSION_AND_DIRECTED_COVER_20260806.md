# Audit of polynomial partial-matching extension and the directed-cover boundary

**Date:** 2026-08-06  
**Method:** independent Hall, Johnson-spectrum, and partial-shadow audit; no
computation or search  
**Audited file:**
`MATH_THEOREM_POLYNOMIAL_PARTIAL_MATCHING_EXTENSION_AND_DIRECTED_FOREST_COVER_20260806.md`  
**Verdict:** PASS after one notation/scope correction in Corollary 6.1.
The matching-extension theorem is unconditional.  Separate completion of
the two protected colours gives a directed **coloured multigraph** cycle
cover, not yet a simple directed two-factor.

## 1. Spectral localization

For `A subseteq L`, put `a_U=|A cap N(U)|`.  The identity

\[
 r\bigl(|N(A)|-|A|\bigr)
   =\sum_{U\in N(A)}(r-a_U)
\]

is exact: both sides count the incidences from `N(A)` to `L\A`.
The Johnson boundary identity

\[
 |\partial_JA|=\sum_Ua_U(r-a_U)
\]

is also exact, since one Johnson edge has one common rank-`r` upper set.
As `a_U<=r`,

\[
 |\partial_JA|\le r^2\bigl(|N(A)|-|A|\bigr).
\]

The Laplacian gap of `J(2r-1,r-1)` is `2r-1`, so

\[
 |N(A)|-|A|
 \ge {2r-1\over r^2}{|A|(W-|A|)\over W}.
\]

If `A` fails Hall after deleting a protected matching of size `f`, then

\[
 |N(A)|-|A|<f.
\]

Writing `q=min{|A|,W-|A|}` and using
`|A|(W-|A|)/W>=q/2` gives exactly

\[
 q<{2r^2\over2r-1}f.
\]

No strictness or factor of two is lost.

## 2. Small-shore threshold

Let `F` be the protected matching, let `Y` be its upper endpoints, and let
`A` be a residual failed lower shore.  With

\[
 \mathcal C=N_G(A)\setminus Y,
\]

Hall failure gives `|C|<|A|`.  Every `x in A` has at least

\[
 D_\alpha=r-\alpha(F)
\]

neighbours in `C`, because at most `alpha(F)` of its `r` neighbours lie in
`Y`.  After complementation, the family

\[
 \mathcal J=\{[2r-1]\setminus x:x\in A\}
       \subseteq{[2r-1]\choose r}
\]

has at least `D_alpha` lower members from the complemented `C` family below
each of its elements, while that lower family is strictly smaller than
`J`.  This is exactly the orientation of the side-ratio-one sharp
partial-shadow threshold.  It yields

\[
 |A|\ge {2D_\alpha-1\choose D_\alpha}.
\]

The shift relative to the capacity-two protected-factor theorem is
correct: here it is `r-alpha`, not `r-alpha-1`, because there is no loose
capacity-two owner to discard.

Minimality is unnecessary for this capacity-one argument, but invoking an
inclusion-minimal failed subset and then passing back to `A` is harmless.

## 3. Co-small threshold

Put `B=X\A` and

\[
 \mathcal Q=(\mathcal U\setminus Y)\setminus N_{G_F}(A).
\]

The two residual shores both have size `W-f`, so

\[
 |\mathcal Q|\ge|B|+1.
\]

Every `U in Q` has no lower neighbour in `A`.  At most `beta(F)` of its
lower facets lie in the protected lower endpoint set `Z`; hence at least

\[
 D_\beta=r-\beta(F)
\]

facets lie in `B`.  The strict-imbalance sharp partial-shadow theorem is
therefore applied in its correct orientation: `B` is the rank-`r-1`
family, `Q` the larger rank-`r` family.  It gives

\[
 |B|\ge {2D_\beta-1\choose D_\beta-1}+1
       ={2D_\beta-1\choose D_\beta}+1.
\]

Thus both partial-shadow uses and both definitions of `D` are correct.

## 4. Polynomial matching extension

The spectral lemma localizes a failed shore to a polynomial small or
co-small side:

\[
 O(rf)=O(r^{C+1}).
\]

Under

\[
 \alpha(F),\beta(F)\le(1/2-\epsilon)r,
\]

both sharp thresholds are at least

\[
 2^{(1+2\epsilon)r-O(\log r)},
\]

which eventually dominates that polynomial.  The Hall contradiction is
valid on both sides.  Equivalently, the proof only needs both threshold
binomials to dominate `rf`, as stated in the theorem.

The sharp partial-shadow theorems require their depth parameter to be in
the nontrivial range; the sub-half hypothesis places
`D_alpha,D_beta>=2` automatically for all sufficiently large `r`.

## 5. Directed forest corollary

For the incidence lift of an **owner-path** forest, every protected lower
vertex has degree two.  Alternating the edge colours along each oriented
component therefore puts exactly one edge of each colour at every used
lower vertex.  Consequently the lower endpoint set of each partial
matching `F_i` is exactly the used-lower set of the full forest, while its
upper endpoint set is a subset of the protected owners.  This proves

\[
 \alpha(F_i)\le\alpha(P),
 \qquad
 \beta(F_i)\le\beta(P).
\]

The original proof said only that all endpoint sets were subsets; that
would not by itself control `alpha`, because enlarging the residual lower
domain can expose a new maximum.  The audited theorem has been patched to
record the exact equality of the lower endpoint sets.

Applying the matching theorem separately produces perfect matchings
`M_0,M_1` respecting the protected colours.  Orienting them oppositely
gives indegree and outdegree one at every vertex.  However an unprotected
edge may belong to both perfect matchings.  Such an edge is used twice with
opposite colours and forms a directed two-cycle.  Therefore the correct
notation is the coloured multiset union

\[
 M_0\uplus_{\rm col}M_1,
\]

not a disjoint union of underlying edge sets.  This notation/scope
correction has been applied to the audited theorem.

## 6. PBBS scope

For the PBBS five-collar forest plus the rank-stratified upper backup bank,
the owner-rank parameter in this theorem is the collar parameter `R=r+1`.
The bank has polynomial edge count and, for large `R`, exposure at most
`R/3`.  Hence each prescribed alternating colour class extends separately.
This unconditionally closes the two **one-colour Hall** rows.

It does not imply any of the following:

1. `M_0 cap M_1=emptyset` on unprotected edges;
2. a simple directed owner factor;
3. a prescribed number of components;
4. compatible cyclic source histories or clipped residence;
5. the literal common-history lower-cell map; or
6. the typed common-cap suffix rank.

An independently supplied uncoloured simple two-factor containing the same
forest does not solve item 2: its cycle two-colourings may induce mutually
inconsistent orientations on several pre-oriented protected components in
one cycle.  Conversely, the directed multicover from this theorem may
contain common-edge two-cycles.  Synchronizing these two outputs is the
exact remaining simple/component theorem.

Three proof-sufficient forms of that theorem are:

* choose the second perfect matching in `G-M_0` while retaining `F_1`;
* produce a simple protected two-factor whose every cycle has consistent
  protected orientation parity; or
* connect all pre-oriented protected pieces on each eventual cycle into
  one oriented protected path before the simple-factor completion.

None follows from the matching-extension theorem alone.

## 7. Files and scope

Audited and patched:

* `MATH_THEOREM_POLYNOMIAL_PARTIAL_MATCHING_EXTENSION_AND_DIRECTED_FOREST_COVER_20260806.md`.

Partial-shadow inputs:

* `MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`.

No finite search, solver result, or unproved conversion from a coloured
multicover to a simple directed factor is used.
