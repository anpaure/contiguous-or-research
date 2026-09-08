# The three-sector residual: growing path packets versus fixed-4 atoms

Date: 2026-07-31  
Status: exact formulation and asymptotic interface.  The arbitrary-puncture
Delcourt--Postle theorem closes the separate near-forest rows.  A robust
fractional **combined** residual factor and an edge-aligned absorber
cover-down are not proved.

## 0. Verdict

The exact three-sector residual has two complementary hypergraph models.

1. As whole paths it is an ordinary perfect-matching problem, but the
   uniformity is `3n+4`, growing with `n`.
2. As individual Johnson steps it is a fixed 4-uniform exact-cover problem,
   but one must add a global topology condition: every augmented component
   must contain exactly one complementary endpoint-pair link.

Thus there is no lossless reduction to a bare fixed-uniformity perfect
matching.  The missing information is precisely the same integral
correlation seen throughout the Catalan programme.  The new arbitrary-`Q`
colouring theorem is nevertheless useful: it gives `P-o(P)` conflict-free
forests separately in all punctured side rows for every chosen common basis.
It supplies the cover-down body, not the exact coupling or absorber finish.

## 1. Exact growing-uniformity path hypergraph

Fix a parent AGCF, an orientation transversal `E`, and the residual resource
sets (3.4)--(3.6) of
`MATH_THEOREM_CATALAN_ANTIPODAL_FILLER_POINTED_WREATH_AND_THREE_SECTOR_RECURSION_20260731.md`.
Let `R_n(E)` be the hypergraph whose vertices are those remaining middle,
lower, and upper resources.  One edge is one monotone-tag complement
geodesic

\[
  00\cdots00\longrightarrow01\cdots01\longrightarrow11\cdots11. \tag{1.1}
\]

It contains `n+2` middle resources and `n+1` resources from each turn
palette, hence is exactly

\[
                         (3n+4)\text{-uniform}.         \tag{1.2}
\]

### Proposition 1.1

A perfect matching of `R_n(E)` is exactly the residual factor required by
the three-sector recursion.

This is the cleanest exact matching formulation.  It also identifies the
limitation: its uniformity is not bounded as `n` grows.  Moreover, although
the complete unpunctured AGCF catalogue is regular and has a uniform
fractional perfect matching, fixing `E` takes a structured induced face.
The linear flux equations survive, but positivity of a fractional perfect
matching on this face is not currently proved for arbitrary `E`.

## 2. Exact fixed-4 atomization

Every physical Johnson step `XY` has four local resources:

\[
       X\cap Y,qquad X\cup Y,qquad (X,i),qquad(Y,j), \tag{2.1}
\]

where the last two are legal capacity slots.  This includes both internal
sector edges and the two seam types.  Directing every residual path from
tag `00` to tag `11` gives a sharper exact-cover version: use an out-slot and
an in-slot at every physical vertex.  A directed step consumes

\[
  \{X\cap Y, X\cup Y, \operatorname{out}(X),
                            \operatorname{in}(Y)\}.      \tag{2.2}
\]

For every allowable initial vertex `A` in the `00` shore, add an artificial
endpoint-pair atom consuming the unused in-slot at `A`, the unused out-slot
at its prescribed complementary `11` vertex, a start label for `A`, and an
end label for its complement.  Thus the pair atom is also literally
4-uniform; the chosen endpoint bank supplies exactly one label of each type.

Exact coverage of both turn palettes, all in/out slots, and all endpoint
labels produces an augmented directed 2-factor.  Deleting the artificial
pair atoms gives spanning directed path components with the right local
degrees and complementary endpoint **supply**.

### Proposition 2.1 (the remaining topology condition)

The atomized exact cover is a genuine residual factor if and only if every
augmented directed cycle contains exactly one artificial endpoint-pair atom.

#### Proof

One artificial atom closes a physical path from `A` to its prescribed
complement.  Such a physical path has at least `n+1` edges.  There are
`K'` pair atoms and exactly `K'(n+1)=2N+P` physical edges in total, so if
every augmented cycle has one pair, every physical path has exactly
`n+1` edges and is a complement geodesic.  A cycle containing two
or more artificial atoms alternates several physical path fragments and
complement resets; no individual fragment need have complementary endpoints.
Conversely, each desired residual path closes to one augmented cycle using
its unique pair atom. `square`

This proves the precise boundary: fixed uniformity captures all local
palettes and degree capacities, but complement-connectedness is a global
one-reset-per-cycle condition.  It cannot be discarded or replaced merely
by acyclicity of each sector.

## 3. What the arbitrary-`Q` Delcourt--Postle theorem supplies

After choosing seam/endpoint banks **and compatible admissible puncture
bases**, each internal sector is a four-resource slot hypergraph of the form audited in
`MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`.
For every puncture basis—not only a random or quasirandom one—it has:

\[
 \Delta=O(n^2),\qquad \Delta_2=O(n),qquad
 {e(G_Q)\over \Delta}=P(1-o(1)),                     \tag{3.1}
\]

and its projected short-cycle configurations obey

\[
 \Delta_i=O_L(\Delta^{i-2}),\qquad
 \Delta_{i,j}=O_L(\Delta^{i-j-1}).                   \tag{3.2}
\]

Corollary 1.17 of Delcourt--Postle plus fixed-`L` diagonalization therefore
gives a `P-o(P)` linear forest in each punctured row.  The conclusion is
uniform in the chosen common basis, because puncturing only deletes atoms
and the edge-count lower bound is uniform.

This is exactly the correct use of the new theorem in the three-sector
recursion.  It does **not** give:

* exact coverage of the `o(P)` leave;
* simultaneous agreement of the three component partitions at both seams;
* the one-endpoint-pair-per-augmented-cycle condition; or
* a fractional perfect matching of the whole path-packet face `R_n(E)`.

## 4. Fractional and absorber ledger

The Catalan type quotas are perfectly balanced in aggregate.  For
`a+b+c=n-1`, give type `(a,b,c)` mass `C_aC_bC_c`.  Then

\[
 \sum aC_aC_bC_c=\sum bC_aC_bC_c=\sum cC_aC_bC_c=P, \tag{4.1}
\]

and adding the `K'=C_(n+1)-C_n` paths themselves gives `P+K'=N` vertex
occurrences in each sector.  This proves that the proposed recursion has no
scalar or type-quota obstruction.  It is not a labelled fractional perfect
matching for fixed `E`; the punctured mask identities still must be
correlated.

There are two relevant absorber mechanisms.

1. The full AGCF resource hypergraph has a universal two-by-two path trade
   `A+B=C+D`.  It absorbs a leave already aligned as one complete candidate
   edge.
2. The fixed-4 atom model has ordinary alternating diamond/cycle switches.
   These repair local palette and slot choices and can change the permutation
   induced on endpoint-pair links.

Neither statement currently proves that the leave of the Delcourt--Postle
body is a disjoint union of residual candidate edges, nor that enough
puncture-compatible switches exist to turn every augmented cycle into a
one-pair cycle.

## 5. Exact remaining theorem

The shortest cover-down target is:

> **Three-sector edge-aligned cover-down.**  Choose an orientation
> transversal `E`, reserve disjoint puncture-compatible two-by-two path
> trades, and select a matching in the remaining fixed-4 atom system such
> that (i) its uncovered resources are a disjoint union of the reserved
> residual path edges, and (ii) its augmented endpoint permutation can be
> reduced to identity by the reserved switches.

The candidate absorbers then fill the leave, and the endpoint switches give
one complementary pair per component.  This theorem would convert the
already available arbitrary-puncture near forests into the exact residual
factor.  It is stronger than a robust fractional matching and is the actual
integral gate.

For induction it is enough to prove this existentially along one recursively
chosen chain of endpoint banks.  Requiring the statement for every parent
AGCF or for a fixed canonical Dyck bank is unnecessary; the complete `n=3`
endpoint-bank census shows that the latter requirement is false.
