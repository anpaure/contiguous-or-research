# Self-audit: MSW single-coordinate puncture and the centered-q2 gate

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_MSW_SINGLE_COORDINATE_PUNCTURE_DUAL_CATALAN_FORESTS_AND_CENTERED_Q2_GATE_20260805.md`  
**Method:** independent symbolic replay of every local path, count, palette,
and completion implication; no computation or search  
**Verdict:** **GO**, with the explicit scope that neither lower injectivity
of `A_z` nor upper surjectivity of `B_z` is asserted.

## 1. Local path replay

For

\[
 M_j=\lambda_{j+1}\cdots\lambda_r\;\rho_1\cdots\rho_j,
\]

the membership tests are literal:

* `lambda_a in M_j` exactly for `j<a`;
* `rho_b in M_j` exactly for `j>=b`.

Thus each membership sector is one interval and both it and its complement
are nonempty.  The upper vertex `Y_j=M_j union M_(j+1)` contains a deleted
`lambda_a` at the crossing `j=a-1`, and contains an inserted `rho_b` at
the crossing `j=b-1`.  Hence the z-present alternating sector has one more
upper vertex at exactly the boundary and consequently equal shore sizes.
No edge or vertex is double-assigned.

## 2. Count replay

The even middle layer splits evenly:

\[
 {2r-1\choose r}+{2r-1\choose r-1}
 =2{2r-1\choose r}={2r\choose r}.
\]

Both summands equal `V`.  Since there are `C` nonempty sectors of each
type, both internal-edge totals are `V-C`.  Finally

\[
 V-C
 =V\left(1-{2\over r+1}\right)
 =V{r-1\over r+1}
 ={2r-1\choose r+1}.
\]

This verifies every count in (0.1)--(0.2), (1.3)--(1.4), and the component
counts in Theorems 2.1 and 3.1.

## 3. A-palette replay

An original upper vertex `Y=X union X'` avoids `z` if and only if both
rank-r endpoints avoid `z`.  The canonical MSW upper vertices enumerate
all of `binom(Omega,r+1)` once.  Therefore restricting to `z notin Y`
enumerates all of `binom(Omega_z,r+1)` once.  This proves upper exactness of
`A_z` without any appeal to its lower intersections.

Crucially, this implication says nothing about the map
`XX' -> X intersection X'`.  The source note correctly labels that row
uncontrolled and never infers lower injectivity from equal cardinalities.

For the sharper fibre criterion, an edge of intersection `q` is determined
by a two-set `{a,b} subseteq Omega-q`.  If two such pairs shared `a`, the
owner `q+a` would have two incident geodesic edges both changing coordinate
`a` from present to absent.  This would give the membership trace
`0,1,0` locally, contradicting the one-change property of a complementary
geodesic.  Hence the pairs are disjoint.  A fixed puncture outside `q`
therefore deletes either zero or one occurrence from that fibre, proving
(2.3).  The stated heavy-fibre transversal criterion is exactly the
inequality `mu_z^A(q)<=1` in the three cases.

## 4. B-cover and suppression replay

Every lower vertex `q in binom(Omega_z,r-1)` lifts uniquely to the original
owner `q+z`.  Every owner vertex `R in binom(Omega_z,r)` lifts uniquely to
the original upper vertex `R+z`.  Since the original owner and upper
palettes are partitions, the z-present alternating sectors cover both
punctured shores once.

In one component with `b` vertices per shore, the endpoint order is

\[
 R_0,q_0,R_1,q_1,\ldots,R_{b-1},q_{b-1}
\]

up to reversal.  Suppression uses `q_0,...,q_(b-2)` and omits only the
terminal `q_(b-1)`.  The resulting Johnson edges have pairwise distinct
intersections because their suppressed lower occurrences are distinct.
Summing gives `V-C` edges and exactly `C` omitted lower colours.

Reading the rail formulas away from the crossing exchanges distinct
successive rail labels.  A prefix of such exchanges has Johnson distance
equal to its length, proving the claimed outward-geodesic property.

## 5. Centered-q2 replay

For an internal lower owner `M_j-z`, its two incident punctured upper
vertices are `Y_(j-1)-z` and `Y_j-z`.  Their union is

\[
 (M_{j-1}\cup M_j\cup M_{j+1})-z.
\]

Thus an edge of `B_z` with colour `T-z` is exactly a q2 occurrence of `T`
whose middle owner contains `z`.  The edge and target counts both equal
`U`, so surjective is equivalent to multiplicity one.

For fixed `T`, every occurrence has a rank-r middle owner and is counted
for exactly its `r` coordinates.  Therefore

\[
 \sum_{z\in T}c_z(T)=r m(T).
\]

If all `r+2` punctures were exact, the left side would be `r+2`.  For
`r>=3`, `r` does not divide `r+2`.  The puncture-uniform no-go is therefore
correct.  It is not promoted to a no-go for one selected coordinate.

## 6. Completion criterion replay and correction made during audit

The first draft described only nontrivial right-hand components in the
cap graph, which would mishandle trivial A-sectors.  The frozen theorem was
corrected before hashing: it now fixes an arbitrary protected set `I` of
nontrivial components and includes **all** A-component entrances in an
edge-coloured completion graph.  Components outside `I` may use arbitrary
Johnson connectors; components in `I` must use cap-two clean connectors.

A spanning two-factor adds exactly `C` edges to the `V-C`-edge forest.
If the old lower colours are injective, their complement has exactly `C`
members.  A rainbow perfect matching restricted to complementary colours
therefore uses every missing colour once.  Conversely any lower-exact
direct completion induces just such a matching.  Since `A_z` already
contains every upper colour, additional connector occurrences cannot
destroy upper surjectivity.  The criterion is exact.

## 7. Semilength-three calibration replay

The five displayed paths in (6.1) contain all `20` rank-three owners of
`[6]` exactly once and their `15` edge unions are the `15` rank-four sets.
After puncturing `1`, the nontrivial A-sectors are

\[
 345-346,qquad 234-236-256,qquad235-245-246.
\]

Their intersections are respectively

\[
 34;\quad23,26;\quad25,24.
\]

The five A/B crossing intersections are

\[
 46,56,45,34,35.
\]

The overlap is exactly `34`, and `36` occurs in neither list.  Thus the
natural-crossing shortcut really fails even though the retained A-edge
intersections in this calibration are injective.

## 8. Audit of the adjacent q2 marginal theorem

The construction in
`MATH_THEOREM_Q2_SATURATING_CYCLE_CLIQUE_INSERTION_AND_CATALAN_PATH_FOREST_20260805.md`
also audits correctly in its stated scope:

1. all rank-`(r-1)` supersets of one rank-`(r-2)` set form a clique in the
   Johnson graph and every clique edge has that intersection;
2. inserting all unused vertices into the corresponding cycle edges gives
   a Hamilton cycle with every lower colour represented;
3. the redundant-edge count is

   \[
   {2r\choose r-1}-{2r\choose r-2}
   ={3Wr\over(r+1)(r+2)}>{W\over r+1}=C;
   \]

4. deleting `C` redundant edges gives `C` path components and leaves every
   lower colour represented.

That theorem does not price union labels or MSW endpoints.  The puncture
theorem identifies those omitted data precisely with the centered-q2 and
endpoint-correlation rows; there is no scope conflict.

## 9. Final scope verdict

The source may be cited for:

* the exact A/B sector ledger;
* the upper-exact A Catalan forest;
* the exact heavy-lower-fibre puncture criterion for A-injectivity;
* the spanning punctured incidence path cover;
* the lower-injective B Catalan forest;
* the centered-q2 equivalence and puncture-uniform divisibility no-go;
* the rainbow endpoint-matching criterion for a direct protected
  completion.

It must not be cited as proving a selected good puncture, a lower-exact
upper-surjective factor, the cap-two segmentation, arbitrary-width upper
coverage, residence, or the final OR-word theorem.
