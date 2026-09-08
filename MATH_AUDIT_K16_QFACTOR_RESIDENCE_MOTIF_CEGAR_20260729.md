# Audit of the `k=16` quotient-factor residence motif CEGAR

Date: 2026-07-29  
Scope: `scratch/run_k16_qfactor_warm_component_cegar_20260729.py`, with seed
`scratch/k16_qfactor_q1_topresident_hamilton_20260729.json`.  This is a
solver-free mathematical audit.

## 1. Verdict

Every residence motif row produced by `residence_motif_edge_sets` is a
necessary no-good.  There is no entering-phase or quotient-voltage defect:
an edge-orbit variable selects all fifteen physical rotations, so retaining
all quotient edge ids in a motif retains the particular physical boundary
and internal edges witnessing the short run.

For the stated seed, independent light replay gives one quotient cycle of
voltage 11, hence one physical cycle.  It has 3390 old-coordinate short
runs, in the histogram

\[
1:330,\qquad 2:1620,\qquad 3:1440.
\]

These form exactly 226 rotation classes, with quotient motif sizes

\[
2:22,\qquad 3:108,\qquad 4:96.
\]

Thus every motif has the expected `ell+1` distinct quotient edge ids in this
seed.  The factor's hard top-residence rows leave no `z`-coordinate motif;
the 226 motifs are old-coordinate motifs.

## 2. Local persistence lemma

Let `F` be a selected equivariant quotient 2-factor and suppose one physical
cycle of its lift contains the coordinate-`x` pattern

\[
0,\underbrace{1,\ldots,1}_{\ell},0,
\qquad 1\le\ell\le3.
\tag{2.1}
\]

Let `f_0,...,f_ell` be, in order, the left boundary edge, the internal
edges, and the right boundary edge, and let `e_i` be the quotient edge-orbit
id of `f_i`.  Put `M={e_0,...,e_ell}`.

### Lemma 2.1

Every quotient factor `F'` which selects every id in `M` contains the same
physical short run (2.1).  Consequently

\[
\sum_{e\in M}x_e\le |M|-1
\tag{2.2}
\]

is necessary for residence.

#### Proof

Selecting an edge-orbit id selects each of its fifteen fixed physical
rotates, not an existentially chosen phase.  Hence `F'` contains every
specific physical edge `f_i`.  Consecutive `f_i` share the same fixed middle
vertex as in `F`.  The two boundary edges retain their coordinate-zero
endpoints, and the internal vertices retain coordinate one.  At every
internal run vertex the two retained edges already give its full degree two;
there is no alternative local re-pairing.  Changes elsewhere may alter the
component containing this path, or the voltage of its quotient component,
but cannot change these endpoints or their coordinate labels.  Thus (2.1)
survives in `F'`, proving (2.2).  ∎

The code's index formula is exact.  If `edge_ids[i]` joins physical cycle
vertices `i` and `i+1`, a run beginning at `start` and having length `ell`
uses precisely indices

\[
start-1,start,\ldots,start+\ell-1,
\]

which is the implemented `range(ell+1)`.

## 3. Orbit collapse and phase quantifiers

Replacing the physical list `(e_0,...,e_ell)` by a `frozenset` is sound even
if an orbit id repeats: the Boolean conjunction containing the same variable
twice equals the conjunction containing it once, while selecting that orbit
still supplies both physical rotated edges.  Likewise, distinct rotated
witnesses may collapse to one quotient motif row.  This removes duplicate
logical clauses; it does not weaken their meaning.

For the present voltage-11 seed the numerical identity `3390=15*226`,
together with the exact motif-size histogram above, shows that collapse is
only the intended fifteenfold rotation collapse: there is no within-motif
id repetition and no additional collision between nonrotational witnesses.

The usual phase objection does not apply to this model.  Quotient selection
does not choose a phase for an edge after the factor is assembled.  Each
chosen undirected edge orbit installs all phases simultaneously.  Global
voltage controls how the already fixed physical edges are partitioned into
cycles; it cannot erase a local path.  This is different from a model whose
variables choose one voltage-labelled directed occurrence rather than the
whole edge orbit.

The same argument also covers a short all-one physical component: selecting
all projected ids retains the entire component.  No zero-boundary argument
is then needed.

## 4. Strong compressed consequences for the seed

The 226 motifs are cyclic intervals in the 858-edge quotient cycle.  Their
union contains 558 selected edge ids and leaves 300 quotient-cycle edges
uncovered.  Cutting at an uncovered edge makes an ordinary interval
hypergraph.  Earliest-finish interval packing gives both packing and
transversal number 147.

Therefore every resident replacement must omit at least 147 currently
selected motif edges.  Two useful compressed necessary rows are:

1. On the union `U` of all 558 motif edges,
   \[
   \sum_{e\in U}(1-x_e)\ge147,
   \quad\text{equivalently}\quad
   \sum_{e\in U}x_e\le411.
   \]
2. The certified maximum disjoint packing consists of 147 motifs whose
   union `P` has 476 edges.  The stronger one-row packing consequence is
   \[
   \sum_{e\in P}(1-x_e)\ge147,
   \quad\text{equivalently}\quad
   \sum_{e\in P}x_e\le329.
   \]

For stronger propagation while remaining compressed, apply the analogous
packing bound separately to each of the 112 motif-intersection components;
their optimum histogram is `1:85, 2:21, 3:4, 4:2` and sums to 147.  None of
these aggregates logically dominates all 226 individual motif rows, so the
individual rows remain the exact local formulation.  A complementary valid
single weighted row is obtained by summing them:

\[
\sum_e d_e(1-x_e)\ge226,
\]

where `d_e` is the number of motifs containing edge `e` (here at most three).

## 5. Complete lazy-separation theorem

Fix an old coordinate `x` and `ell` in `{1,2,3}`.  A forbidden physical
bracket walk is a phase-consistent walk

\[
v_0v_1\cdots v_{\ell+1}
\]

whose coordinate pattern is `0,1^ell,0` and whose physical edges form a
simple path, allowing the two zero endpoints to coincide when the walk
closes a triangle or quadrilateral.  If `D` is the set of quotient
edge-orbit ids of those physical edges, attach the row

\[
\sum_{e\in D}x_e\le |D|-1. \tag{5.1}
\]

### Theorem 5.1

Under the quotient degree-two equations, the conjunction of (5.1) over all
phase-consistent bracket walks is equivalent to positive residence at least
four in all fifteen old coordinates.

### Proof

Necessity is Lemma 2.1.  Conversely, a short positive run in a component
containing a zero has its preceding and following zero vertices and hence
gives a bracket walk.  A short positive run filling its whole component can
only occur on a physical triangle.  Every Johnson triangle is either formed
by three sets with one common rank-seven core, or by three sets inside one
common rank-nine union.  In the first case at least two varying old
coordinates have pattern `100`; in the second at least two have pattern
`011`.  Thus another old coordinate has a bracketed run of length one or
two, already excluded by (5.1).  Repeated quotient ids are deduplicated
because selecting one orbit installs every one of its physical phases. ∎

It is essential to enumerate physical phases, not bare quotient walks.
Quotient adjacency alone does not certify that the chosen edge occurrences
meet in the required physical order.

By rotating `x` to zero, one coordinate represents all old coordinates.
Before duplicate and subsumption removal, the exact counts are

\[
\begin{array}{c|r}
\ell&\text{bracket walks}\\
1&180180\\
2&11531520\\
3&634233600
\end{array}
\]

for a total of `645945300`.  Already at length one there are 180126 distinct
rows: 180120 binary rows and six unary rows.  A full eager encoding is
therefore the wrong scale.  `residence_motif_edge_sets` is an exact lazy
separation oracle for Theorem 5.1.

## 6. Exact q1 coupling at the retained seed

Let `I_c` be the selected seed providers of a lower or upper q1 colour `c`.
For a seed-edge deletion set `R`, call `c` currently lost when
\(I_c\subseteq R\).

The audited finite transversal certificates establish:

### Theorem 6.1 (current-provider coupling)

Every deletion set meeting all 226 seed residence motifs loses at least one
current q1 colour.  In fact, the minimum possible total number of currently
lost lower-plus-upper colours is 180.  Subject to that minimum, the minimum
deletion count is 148; one optimum loses 88 lower and 92 upper colours.

The preserving-all instance is exactly infeasible in
`scratch/k16_residence_motif_palette_safe_hitting_20260729.json`.  The
lexicographic optimum is recorded in
`scratch/k16_residence_motif_minholes_hitting_20260729.json`.

This is not an obstruction to a new factor: an added off-seed edge may
restore its lower and upper colours.  It proves that residence repair cannot
be treated as deletion-only collar surgery.  The exact global model must
simultaneously choose replacement providers.

For propagation, introduce a Boolean `h_c` satisfying

\[
h_c=1\quad\Longleftrightarrow\quad \sum_{e\in I_c}x_e=0,
\]

and retain the ordinary global q1 row.  Equivalently one may write

\[
\sum_{e\in P_c\setminus I_c}x_e\ge h_c,
\qquad \sum_c h_c\ge180. \tag{6.1}
\]

Rows (6.1) expose, but do not weaken, the joint reconstruction obligation.

## 7. Exact computational boundary

The first H100 CEGAR round used the 226 individual motif rows with the
canonical seed and returned `UNKNOWN` after 600 seconds; its fail-closed
artifact contains no selected factor.  Thus it proves neither feasibility
nor infeasibility.

The strengthened model adds the 147-motif packing consequences from Section
4 and the explicit global provider-loss coupling (6.1).  Any accepted output
must still pass, in this order:

1. exact quotient degree and both q1 decks;
2. one quotient cycle with unit `C_15` voltage, hence one physical cycle;
3. literal top one- and zero-residence;
4. literal old-coordinate residence; and
5. fresh motif separation until no violated run remains.

## 8. Reproducibility

The driver now imports the archived boundary-strengthened H100 module when
present and otherwise falls back to the canonical local module
`k16_even_necklace_q1_factor_20260729.py`.  Both reconstruct catalogue
SHA-256
`e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

## 9. Minimum-distance cross-pattern consequence

The same-shore minimum transversal shows that the 80 AB edges can be kept
while hitting the seed motifs, but q1 reconstruction cannot then be
completed at radius 147.  The free-cut fixed-cross model—440 possible
same-shore cuts, 10266 possible replacements, exact degree and 729
nonconstant q1 rows—is infeasible even after all top-residence constraints
are removed.

Therefore every radius-147 resident rethread must change the AB cross
pattern.  The full statement and exact finite ledger are in
`MATH_THEOREM_K16_RESIDENCE_Q1_RADIUS147_CROSS_GATE_20260729.md`.
