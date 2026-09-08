# The recentered `k=16` palette-safe transversal has value at least 98

Date: 2026-07-29

Let `F` be the persisted radius-147 quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`.  It is a
loopless quotient 2-factor with both `q1` palettes complete and with
top-coordinate biresidence.  Its positive short-residence motif hypergraph
has 147 edges.  The independently replayed min-max certificate gives 97
pairwise edge-disjoint motifs and a 97-edge transversal.

## The palette obstruction

In the certificate's fixed motif ordering,

\[
 M_5=\{22511,22520\},\qquad
 M_{66}=\{22511,22692,25634\}.
\]

The ordinary 97-edge transversal hits both motifs by the shared edge 22511.
However, catalogue edge 22511 is the only represented provider of upper
`q1` colour `(1,1907)` on the source-relative radius face.  No fixed source
edge and no admissible off-source seam provides this colour.  Exact upper
`q1` coverage therefore forces

\[
 r_{22511}=0.
\]

The two motif rows then reduce to

\[
 r_{22520}=1,
 \qquad
 r_{22692}+r_{25634}\ge1.                 \tag{1}
\]

## Theorem

Every source-relative edit that hits all current residence motifs and
preserves the upper `q1` palette deletes at least 98 source edge orbits.

### Proof

The certified disjoint packing consists of `M_5` and 96 other motifs.  Each
of those 96 motifs requires a distinct deletion.  Since edge 22511 must be
retained, (1) requires two further, distinct deletions: edge 22520 and one of
22692, 25634.  The latter two edges lie outside the union of the 97 packed
motifs, while 22520 lies only in `M_5`.  None of these two required deletions
can serve any of the other 96 packed motifs.  Hence at least

\[
 96+2=98
\]

deletions are necessary. ∎

This is a solver-free obstruction.  It explains the zero-branch presolve
infeasibility of the exact radius-97 degree/palette/top model; no CP-SAT
trust is needed for the radius-97 conclusion.  Here the endpoint restriction
is complete because every radius-97 motif transversal is contained in the
certified packing union.

## Sharp hitting witnesses and the radius-98 face

Let `T` be the explicit 97-edge ordinary transversal.  Both sets

\[
 T_{98}^{(a)}=(T\setminus\{22511\})\cup\{22520,22692\},
\]

\[
 T_{98}^{(b)}=(T\setminus\{22511\})\cup\{22520,25634\}
\]

have size 98 and hit all 147 current motifs.  Direct replay verifies both
claims.  They are the two canonical deletion hints for the radius-98 solve.

Within the endpoint bank exposed by the full 390-edge current-motif union,
the same proof makes 98 the exact palette-safe hitting value.  The modeled
radius-98 subface has

- cut variables on all 390 current motif edges,
- exactly 98 cuts and 98 insertions,
- all 147 motif rows,
- degree two and both `q1` palettes,

and the two displayed 98-edge hitting sets are exact witnesses for that
subface.

This is **not** completeness for every global radius-98 repair.  At radius
98 the extra cut may lie outside the current motif union, thereby exposing a
new endpoint and an off-domain replacement provider for colour `(1,1907)`.
For example, catalogue edge 22512 joins nodes 611 and 620; cutting outside
source edge 22775 or 22790 can expose node 620.  Thus a global radius-98
model must allow all source edges as possible extra cuts (and rebuild the
endpoint-dependent seam bank), or separately prove that no such exterior
provider can complete degree and the other constraints.  The present
390-edge model is the instructed minimal motif-union subface only.

## Iterative context

More generally, if a rethread `F -> G` deletes a set meeting every motif of
`F`, then every motif of `G` contains an added edge.  Otherwise it would use
only retained literal edge orbits and would already be a motif of `F`.
Consequently

\[
 \tau(\mathcal H(G))\le |G\setminus F|.
\]

Re-centering is therefore a weak transversal descent.  Strict descent is
not automatic and must be audited after each feasible step.
