# Self-audit of the period-five Apéry extreme classification

**Date:** 2026-08-05  
**Method:** independent facet and phase replay; pure mathematics; no
computation, search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_PERIOD_FIVE_APERY_EXTREME_CLASSIFICATION_AND_POSITIVITY_20260805.md`  
**Verdict:** **PASS.**  The normalized facet description, eight-vertex
enumeration, primitivity, and both nonmechanical phase decompositions are
exact.

## 1. Facet reduction

Subtracting the minimum increment preserves every equal-length cyclic
block comparison.  For a nonconstant ray the final increment remains
positive, so normalization to `(0,a,b,c,1)` is valid.

Length one and four give the cube inequalities.  Length two contributes
only `a<=b+c`; length three contributes only `a+b<=c+1`.  Direct listing
of all cyclic blocks confirms that every other inequality follows from
these.  Thus the three-dimensional polytope in the source is exact.

## 2. Vertex enumeration

The six surviving cube vertices are

\[
 000,001,010,011,101,111.
\]

The simultaneous oblique equalities give

\[
 b={1\over2},
 \qquad a=c+{1\over2},
 \qquad0\le c\le{1\over2},
\]

whose endpoints are `(1/2,1/2,0)` and `(1,1/2,1/2)`.  A point on only one
oblique facet needs two cube facets to become a vertex; checking those
intersections yields no additional point.  Hence the list of eight is
complete.

The corresponding integral nonmechanical rays are

\[
 u=(0,1,1,0,2),
 \qquad
 v=(0,2,1,1,2).
\]

Their proper prefix shifts are strictly below the endpoint-density line,
so both are primitive.  Their three distinct increment levels exclude a
binary lower-mechanical representation.

## 3. First nonmechanical phase decomposition

For `u`, the phases modulo `P=4eta` are

\[
 0,0,\eta,2\eta,2\eta.
\]

The two brackets

\[
 \{0,2\eta\}
 \quad\text{and}\quad
 \{0,\eta,2\eta\}
\]

are respectively the full residue set for mesh `2eta` and the sparse
Beatty set `floor(4 ell/3)eta`, `ell=0,1,2`.  They reproduce the phase
multiset exactly, including the double occurrences of zero and `2eta`.
Thus

\[
 \Phi_u=C(2\eta)+R_{4,3}(\eta)>0.
\]

## 4. Second nonmechanical phase decomposition

For `v`, the phases modulo `P=6eta` are

\[
 0,0,2\eta,3\eta,4\eta.
\]

The complete mesh-`2eta` residues are `{0,2eta,4eta}`, and the complete
mesh-`3eta` residues are `{0,3eta}`.  Their multiset union is exactly the
displayed phase multiset.  Hence

\[
 \Phi_v=C(2\eta)+C(3\eta)>2{377\over108000}.
\]

No sign estimate beyond the already audited comb and mechanical theorems
is used.

## 5. Scope

Every extreme ray of the period-five increment cone is positive, but the
phase functional is nonlinear in the increments.  The source correctly
does not infer positivity of the full period-five cross-section or of
higher-period cones.  It also makes no finite-shoulder claim.

**Final verdict: PASS.**
