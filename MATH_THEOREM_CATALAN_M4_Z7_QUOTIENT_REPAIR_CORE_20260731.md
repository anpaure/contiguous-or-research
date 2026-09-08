# The canonical \(m=4\) repair is a three-orbit \(\mathbb Z_7\)-quotient object

Date: 2026-07-31  
Status: exact theorem for the authenticated canonical \(m=4\) fixture;
generalization to arbitrary \(m\) remains open

## Theorem

Identify the eight coordinates with

\[
[8]=\mathbb Z_7\sqcup\{\infty\},
\]

and let rotation add \(1\) on \(\mathbb Z_7\) while fixing \(\infty\).  In the
canonical uniformly-outgoing repair certified by
'catalan_m4_mixed_split_fixed_forest_closure_20260731.PASS.json', write a
repair-core edge as

\[
(O,D,Z)=(\text{omitted facet},\text{base colour},\text{outgoing colour}).
\]

Then the complete 21-edge occurrence-labelled repair core is the disjoint
union of exactly three free \(\mathbb Z_7\)-orbits:

\[
\begin{aligned}
\mathcal E&=\mathbb Z_7\cdot
  (\{0,2,3,4\},\{0,1,2\},\{0,2,4\}),\\
\mathcal K_0&=\mathbb Z_7\cdot
  (\{0,2,4,\infty\},\{1,2,\infty\},\{0,2,\infty\}),\\
\mathcal K_1&=\mathbb Z_7\cdot
  (\{0,2,4,\infty\},\{0,6,\infty\},\{0,2,\infty\}).
\end{aligned}
\]

For avoidance of ambiguity, the frozen integer-mask representatives used by
the independent audit are

\[
 (29,7,21),\qquad(149,134,133),\qquad(149,193,133).
\]

The orbit \(\mathcal E\) consists of the seven forced ears.  Removing it
leaves the leafless \(7\times7\times7\) kernel
\(\mathcal K_0\sqcup\mathcal K_1\).  That kernel has exactly two perfect
matchings, namely the two whole orbits \(\mathcal K_0\) and
\(\mathcal K_1\).  Consequently the canonical selected repair is

\[
\mathcal E\sqcup\mathcal K_0,
\]

and the only alternate repair matching is

\[
\mathcal E\sqcup\mathcal K_1.
\]

Equivalently, after quotienting by \(\mathbb Z_7\), the complete core has two
components: one \(1\times1\times1\) component carrying one forced edge
orbit, and one \(1\times1\times1\) component carrying two parallel edge
orbits.  The apparently irreducible seven-token kernel is therefore a
one-token binary choice in the cyclic quotient.

Moreover, the *whole physical construction* is equivariant, not only its
repair matching.  Rotation by \(1\in\mathbb Z_7\) advances both authenticated
70-cycles by 40 positions and both authenticated 56-cycles by 32 positions.
The 70-cycle is the voltage-two lift of a ten-cycle; the 56-cycle is the
voltage-two lift of an eight-cycle.  Since \(\gcd(2,7)=1\), both lifts are
connected.

The two-sided-rainbow 14-path forest is also invariant.  Its paths form two
free \(\mathbb Z_7\)-orbits, one consisting of the seven three-vertex paths
and the other of the seven seven-vertex paths.  Its quotient is therefore a
spanning two-path forest on ten vertices, with component sizes three and
seven.  Adding the two closure-edge orbits makes the quotient ten-cycle of
voltage two.

## Proof

Rotate each of the 21 literal triples in the authenticated complete core.
Every stabilizer is trivial, and canonicalization produces exactly the three
representatives above, each with orbit size seven.  The three orbits are
pairwise disjoint and exhaust the core.

Every shore vertex of \(\mathcal E\) avoids \(\infty\) and has degree one in
the complete core, so all seven \(\mathcal E\)-edges are forced.  Every shore
vertex of \(\mathcal K_0\sqcup\mathcal K_1\) contains \(\infty\) and has
degree two.  Each of \(\mathcal K_0,\mathcal K_1\) meets every remaining
shore vertex once, so each is a perfect matching.  Conversely, the
omitted--outgoing projection of the residual kernel consists of seven
doubled pairs, while either of the other two projections is a simple
14-cycle.  Alternation around that cycle forces a perfect matching to be
precisely one of the two orbits.  This gives exactly two.

The producer-independent audit performs these checks directly from the
frozen 21 core edges; it does not trust the producer's orbit labels or its
kernel classification.  For the physical statement, it independently
rotates all cycle and forest edges, reconstructs the induced permutation of
the fourteen paths, contracts the ten middle-set orbits, and computes the
wrap voltage from the literal cycle order.

## Extra cyclic identities

For every selected repair, \(Z\subset O\) and \(O\setminus Z\) is one finite
coordinate.  Across \(\mathcal E\sqcup\mathcal K_0\), every coordinate of
\(\mathbb Z_7\) is the pivot exactly twice.

The symmetric differences \(D\triangle Z\) form fourteen ordinary edges on
\(\mathbb Z_7\).  The ear orbit contributes the step-three heptagon and the
selected kernel orbit contributes the step-one heptagon.  Hence their union
is

\[
K_7\setminus C_7(\pm2).
\]

This supplies a compact algebraic description of both regularity and the
missing seven swaps.  It is the strongest current indication that the
directed Catalan repair should be sought as a cyclic quotient construction,
not as a generic leaf-peeling argument.

## Scope

This theorem proves the exact \(\mathbb Z_7\)-quotient anatomy of one genuine
uniformly-outgoing \(m=4\) repair.  It does **not** yet prove that an
analogous orbit core exists for every \(m\), nor does it settle the
physical Hamilton lift when \(2m-1\) is composite.  Those are the next two
gates.

## Reproduction

Run:

    python3 scratch/audit_catalan_m4_z7_orbit_repair_core_20260731.py

The audit output is
'scratch/catalan_m4_z7_orbit_repair_core_20260731.audit.json'.
