# Independent audit of transversal-cube packing

## 1. Verdict

`TRANSVERSAL_CUBE_PACKING.md` is correct with its stated scope.

The decisive full-cube conclusion is exact, not asymptotic:

\[
                  \nu_{\rm match}(H_m)=1.
\]

Every two perfect-matching transversal cubes share at least two middle
sets.  Therefore full cubes cover at most `2^m=o(W)` vertices in a disjoint
packing.

The subdivided positive result is also valid.  For every fixed free
dimension `s`, the hypergraph of all distinct `s`-faces is fixed-uniform,
regular, and has relative maximum pair codegree `s/m^2`; the classical
almost-perfect matching theorem applies.  A diagonal argument gives an
unspecified `s(m)->infinity`, but no prescribed rate.

The document correctly does not infer a radius-resolved or shadow-resolved
construction.

## 2. Full-cube incidence audit

A middle set `S` belongs to `C(P)` precisely when `P` is a perfect matching
across `(S,S^c)`.  This is the same as a bijection `S->S^c`, yielding degree
`m!`.

For two middle sets with intersection size `a`, the four Venn classes have
sizes

\[
                         a,m-a,m-a,a.
\]

An edge crossing both cuts must join the first class to the fourth or the
second to the third.  The two bijections yield `a!(m-a)!`.  In particular,
`S` and `S^c` lie in exactly the same matching cubes.  This alone gives
maximum relative pair codegree one and prevents a raw small-codegree nibble.

The higher-signature formula is also complete.  Crossing every selected
cut pairs a membership signature only with its bitwise complement.  Equal
class sizes are necessary and sufficient, and each complementary class
pair contributes one factorial number of bijections.  No compatibility
condition between different signature pairs is missing.

## 3. Alternating-cycle audit

In the two-coloured multigraph `P union Q`, every vertex has one incident
edge of each colour.  Components are alternating even cycles; if `P,Q`
share an edge, retaining its two colours makes it a legitimate alternating
two-cycle.

A common transversal must alternate zero and one around each component.
Both phases work and no other assignment does.  Independent components
give exactly

\[
                              2^{c(P,Q)}.
\]

There is always at least one component.  Thus no pair of full cubes is
disjoint.  For distinct matchings, at least one component has length at
least four, so `c<=m-1` and the upper intersection bound `2^(m-1)` is also
correct.

Passing to antipodal vertex pairs divides every intersection by two but
does not make it empty.

## 4. Face-phase criterion

Each fixed orientation selects one of the two alternating phases on the
component containing that edge.  Multiple constraints on one component
are either all consistent or rule out the component entirely.  If `u`
components are consistently constrained, the other `c-u` phase bits remain
free.  Hence the claimed intersection size `2^(c-u)` follows.

This supports the two “weakest” statements, which must not be conflated.

* Against a full cube, one fixed orientation never suffices for
  disjointness; two contradictory constraints on one component are the
  first possibility.
* If both objects are subdivided, codimension one on each side can already
  be disjoint.

The note labels codimension one as the weakest **uniform** viable
subdivision and separately identifies the much deeper subdivision currently
handled by a theorem.

## 5. Distinct-face parameter audit

Put `r=m-s`.  A distinct face is determined by fixed selected coordinates
`U`, fixed excluded coordinates `V`, and a perfect matching `R` on the
remaining `2s` coordinates.  Pairing `U` to `V` is invisible in the face and
must not be counted.  This is why the distinct-edge count is

\[
 { (2m)!\over r!^2\,2^s s!}.
\]

For a fixed middle vertex, choose `s` varying coordinates on either side of
its cut and match them, giving

\[
                         D_s=\binom ms^2s!.
\]

For two vertices at Johnson distance `j`, their fixed positive and negative
sets must be selected from the two common Venn classes.  The free matching
then independently pairs the two `j`-element symmetric-difference classes
and the two `(s-j)`-element residual classes.  This gives

\[
 d_s(j)=\binom{m-j}{s-j}^2j!(s-j)!,
\]

with zero codegree at `j>s`.

After division by `D_s`,

\[
 \rho_j={\binom sj(j!)^2\over(m)_{\underline j}^2}.
\]

For `1<=j<=s<m`,

\[
 {\rho_j\over\rho_1}
 ={(s-1)_{\underline{j-1}}j!
   \over(m-1)_{\underline{j-1}}^2}\le1.
\]

The two needed comparisons are

\[
 (s-1)_{\underline{j-1}}le(m-1)_{\underline{j-1}},
 \qquad
 j!\le(m-1)_{\underline{j-1}},
\]

the second following from `m>=j+1`.  Thus the maximum really occurs at
distance one and equals `s/m^2`.

## 6. Matching-theorem quantifiers

For each fixed integer `s`, the edge size `2^s` is fixed before
`m->infinity`, all degrees equal `D_s->infinity`, and

\[
                         \Delta_2=o(D_s).
\]

These are exactly the fixed-uniformity hypotheses of the standard
Pippenger--Frankl--Rodl almost-perfect matching theorem.  Its conclusion is
an edge matching covering all but `o(W)` vertices, not merely `o(|E|)`
faces.

The diagonal corollary is logically valid despite lacking a uniform rate.
For each `h`, choose a threshold large enough for free dimension `h` and
error at most `1/h`; make the thresholds strictly increasing and at least
`h`.  Selecting the largest eligible `h` gives `s(m)->infinity` and vertex
error at most `1/s(m)`.

This does not justify any specified growing function.  In particular, it
does not establish `s>>sqrt(m)`, or even `s>>log m`.

## 7. Why the half-face case is not settled

At `s=m-1`, the uniformity is `2^(m-1)`, so the fixed-uniformity theorem is
inapplicable.  Although the relative pair codegree is `Theta(1/m)`, current
growing-uniformity estimates have explicit exponential dependence on the
edge size.  The cited Alon--Bollobas--Kim--Vu condition fails by an
`exp(2^m)` factor.  Fixed-rank conflict-free and full-codegree theorems
cannot be invoked with a rank depending on `m` without an additional
uniform statement.

Small pair codegree alone is insufficient in growing rank: finite projective
planes furnish intersecting regular hypergraphs with relative codegree
tending to zero.  Thus the note correctly records the half-face packing as
open rather than extrapolating Theorem 7.

## 8. Shadow-usefulness audit

The positive face packing establishes only middle-vertex disjointness.

* It assigns no standard binary-RSK radius to a face.
* It does not prescribe how many cells may certify each depth.
* It does not control equality of lower or upper shadows across cells.
* The diagonal dimension has no useful quantitative rate.

Moreover, an `s`-face remembers only the matching on its varying `2s`
coordinates.  The `(m-s)!` possible matchings between fixed `U,V` all give
the same geometric face.  Therefore a large number of nominal full-matching
extensions is not evidence of useful active-pair diversity.

For codimension one, almost the whole matching remains active, so a positive
near-packing theorem there would genuinely diversify pair systems.  That is
precisely the case not proved by available nibble results.

## 9. Machine audit

`scratch/check_transversal_cube_packing.py` enumerates all perfect matchings
through `m=5`.  It verifies every pairwise full-cube intersection, all full
degrees and pair codegrees, and the complete degree/codegree tables for all
distinct `s`-faces.  At `m=5` it checks 945 matchings and 446,985 matching
pairs.  All checks pass.

The checker validates the exact finite identities.  The asymptotic face
packing relies on the fixed-uniformity theorem, not on computation.
