# Cyclic-splice incremental shadow and dual-residence theorem

Date: 2026-07-29  
Lane: AD  
Status: proved, with the scope distinctions below mandatory

## 1. Setup and ledger convention

Let \(\Omega\) be a finite coordinate set and let
\(\Gamma\leq\operatorname{Sym}(\Omega)\).  The cyclic word

\[
W=(X_0,\ldots,X_{N-1}),\qquad X_i\subseteq\Omega,
\]

is cut into directed linear arcs \(P_1,\ldots,P_t\).  A *\(\Gamma\)-splice*
reglues the same arcs in a new cyclic order after replacing each arc by
\(g_iP_i\) or \(g_i\operatorname{rev}(P_i)\), where \(g_i\in\Gamma\).

For an interval statistic \(f\), its exact orbit ledger is the occurrence
counter

\[
M_f(W)(c)=\#\{I:\ [f(W[I])]_{\Gamma}=c\}.                 \tag{1.1}
\]

The counter, not merely its support set, is the primitive object.  Once the
counter has been updated, the covered-colour set is
\(\{c:M_f(W)(c)>0\}\).  Directly subtracting sets is unsound when an old
seam colour also has an internal occurrence.

The application below has \(\Omega=[16]\) and
\(\Gamma=C_{15}\), rotating coordinates \(0,\ldots,14\) and fixing
coordinate \(15\).  No claim below silently enlarges this group to
\(S_{16}\).

## 2. Exact seam-support identity

### Theorem 2.1 (splice counter identity)

Suppose that \(f\) is equivariant under \(\Gamma\) and invariant under
reversal of the entries in its interval.  This holds for intersection and
union.  Let \(\operatorname{Cross}_{f}(W;P_1,\ldots,P_t)\) be the orbit
counter over precisely those cyclic intervals of \(W\) that are not wholly
contained in a single cut arc.  If \(W'\) is a \(\Gamma\)-splice of the
arcs, then, in the free abelian group on orbit colours,

\[
M_f(W')-M_f(W)
=
\operatorname{Cross}_{f}(W';P'_1,\ldots,P'_t)
-
\operatorname{Cross}_{f}(W;P_1,\ldots,P_t).              \tag{2.1}
\]

This remains exact after restricting both sides to any prescribed set of
interval widths.

#### Proof

Partition the old interval occurrences into arc-internal and seam-crossing
occurrences.  Do the same in the new word.  Every old interval internal to
\(P_i\) has a unique new occurrence internal to \(g_iP_i\) or
\(g_i\operatorname{rev}(P_i)\).  Equivariance and reversal invariance give
the same \(\Gamma\)-orbit colour.  Hence the two internal occurrence
counters cancel exactly.  What remains is (2.1).  The bijection preserves
width, proving the final assertion. \(\square\)

### Corollary 2.2 (fixed-width locality)

For intervals of width \(w\), at most \(w-1\) starting positions per seam
are seam-crossing.  Thus a fixed depth-\(q\) row, whose window has
\(w=q+1\) vertices, requires at most \(q\) old and \(q\) new evaluations
per seam.  In particular, a lower-\(q=2\) intersection ledger changes only
through the two triples spanning each seam.

For a connected 2-opt, there are two old cuts and two new seams.  Therefore
at most four old and four new lower-\(q=2\) triples need evaluation.  A
triple wholly inside the reversed arc has exactly its old unordered set of
vertices and hence exactly its old intersection and union.

## 3. What is and is not bounded for arbitrary widths

### Proposition 3.1 (exact saturation compiler)

For arbitrary-width unions, (2.1) is evaluated from prefix/suffix union
tables on the cut arcs.  An interval crossing one seam is a suffix of its
left arc, zero or more complete intermediate arcs, and a prefix of its
right arc.  These pieces determine its union exactly.  Extensions may stop
once the old and new unions have both reached \(\Omega\): all further
extensions contribute only the full colour.  For occurrence multiplicities,
the number of such tail intervals is added arithmetically; for mere support,
one full-colour occurrence suffices.

The dual assertion holds for arbitrary-width intersections, with the empty
set replacing \(\Omega\).

#### Proof

Union is monotone under interval extension.  Once an extension has union
\(\Omega\), every longer extension has the same union.  Intersection is
dually monotone, and once empty remains empty.  Every seam-crossing interval
has the stated unique arc-piece decomposition after its two endpoint arcs
are fixed.  Apply Theorem 2.1. \(\square\)

### Scope warning 3.2 (no universal radius)

There is no universal \(O(1)\) locality radius for the all-upper ledger.
A seam-crossing interval can remain nonfull for arbitrarily many positions.
The exact cost is controlled by the actual saturation tables.  The same
warning applies to arbitrary-width lower intersections: only a fixed-width
lower row such as \(q=2\) has the numerical locality of Corollary 2.2.

For a 2-opt, endpoint arcs lying in different pieces give the usual
prefix/suffix rectangles.  Intervals that contain one or more complete arcs
must also be included.  Omitting these full-arc cores is not an exact
all-upper update.

## 4. Exact dual-residence update

For a binary string \(s\), define its run summary to contain

* its length;
* its first and last bits;
* its first- and last-run lengths;
* whether it is constant; and
* the run-length counters, separately for bits \(0\) and \(1\), of all runs
  not touching its two endpoints.

### Theorem 4.1 (run-summary gluing)

For every arc and every coordinate, the above summaries determine exactly
the cyclic positive- and negative-run histograms after an arbitrary
\(\Gamma\)-splice.  A coordinate permutation reindexes summaries by
\(x\mapsto g_i^{-1}x\); reversal swaps the two endpoint summaries and leaves
internal run lengths unchanged.  Concatenation merges the last run of the
left summary with the first run of the right summary exactly when their bits
agree.  After all arcs are concatenated, the same rule performs cyclic
closure.

#### Proof

Every run wholly inside an arc is unchanged, up to coordinate reindexing and
reversal.  The only runs not already recorded as internal are the two
boundary runs of each arc.  At a concatenation boundary they either remain
separate, when their bits differ, or form one run whose length is the sum of
their lengths.  The constant flag is needed because a boundary run can pass
through a whole constant arc and merge again at the next seam.  Repeating
this deterministic operation and finally closing the cycle accounts for
every run exactly once. \(\square\)

This theorem treats both orientations.  A positive-run-only audit gives no
information about negative residence.  There is also no universal numeric
residence radius: a boundary run may be arbitrarily long, although only the
boundary summaries participate in the update.

## 5. Voltage-cycle specializations

### Corollary 5.1 (one parallel quotient replacement)

Let a quotient Hamilton cycle be lifted through a regular \(C_g\)-cover
(so \(C_g\) acts freely on every physical fibre), with dart voltages in
\(C_g\).  Delete one selected quotient edge orbit.  Its physical lift becomes
\(g\) translated copies of one quotient path.  If the old and new total lap
voltages are \(\omega\) and \(\omega'\), the old and new seam gluings act on
path sheets by

\[
t\longmapsto t+\omega,qquad t\longmapsto t+\omega'.      \tag{5.1}
\]

Thus the lift has \(\gcd(g,\omega)\) old and
\(\gcd(g,\omega')\) new components.  Theorems 2.1, 3.1, and 4.1 applied to
the \(g\) path summaries give exact incremental shadow and dual-residence
scores.  By equivariance, the two lower-\(q=2\) seam triples in the quotient
represent all \(g\) physical copies.

The quotient vertex order is unchanged.  Immediate lower and upper q1 loads
change only by subtracting the removed edge's colours and adding the new
edge's colours.  Equal quotient endpoints do not imply equal lower or upper
colours; those colours must be read from the physical edge orbits.

### Corollary 5.2 (connected 2-opt)

Delete two edges of a voltage cycle and reconnect their four ports by the
connected 2-opt pairing.  The new cycle is a splice of the two old arcs, one
possibly reversed and each carrying the coordinate/voltage alignment forced
by the new darts.  The total voltage is the signed sum of the two internal
arc voltages and the two new dart voltages.  Theorems 2.1--4.1 therefore give
an exact incremental scorer.  Quotient connectedness does not imply a
connected physical lift; the final total voltage must still be coprime to
\(g\).

## 6. Audited application: edge 13230 to 13232

The independently replayed artifacts are

* source `scratch/k16_connected_q1_lower2_radius13_seed1.json`, SHA-256
  `39ce5fe54cac6b0199a2b2e02949c90041128915d3f9d271284714e9d26f7109`;
* final `scratch/k16_connected_q1_lower2_hamilton_20260729.json`, SHA-256
  `16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8`.

The latter is correctly labelled `PARTIAL_Q1_PHYSICAL_HAMILTON`: its two
missing lower quotient-colour orbits expand to 20 literal rank-seven masks,
so they do not fit the two COMP\(_3\) endpoint cells.  The word "final" in
this section means only the endpoint of the voltage-repair replay.

Edges `13230` and `13232` have the same quotient endpoints `(322,408)` and
the same upper colour `6587`.  Their lower colours are respectively `4915`
and `2459`; the corresponding selected loads change `2 -> 1` and `1 -> 2`,
so no lower q1 hole is created.  Their stored dart voltages are `12` and
`1`.  The cycle traverses this dart in the reverse direction in the chosen
orientation, so total voltage changes

\[
12\longmapsto 8\pmod {15}.                               \tag{6.1}
\]

The physical lift consequently changes from three cycles of length `4290`
to one cycle of length `12870`.

The two old seam triples have canonical intersections

\[
0\mathrm{xcc9}\ (\text{rank }6),\qquad
0\mathrm{x1333}\ (\text{rank }7),                       \tag{6.2}
\]

and the two new seam triples have

\[
0\mathrm{x91b}\ (\text{rank }6),\qquad
0\mathrm{x999}\ (\text{rank }6).                        \tag{6.3}
\]

In the full q2 occurrence support, old-only colour `4915` has rank seven and
is irrelevant to the rank-six target set, while new-only colours `2331` and
`2457` are both rank six.  The q2 orbit-hole count therefore improves
`91 -> 89`.

The complete arbitrary-width upper orbit set is exactly unchanged: it has
`1634` colours and `129` target holes both before and after.  This is an
audited equality for this move, not a consequence that every parallel move
preserves all-upper support.

The short-run ledgers change as follows:

\[
\begin{array}{c|ccc}
 &1&2&3\\ \hline
\text{old positive}&390&1635&1425\\
\text{new positive}&375&1635&1410\\
\text{old negative}&345&1545&1680\\
\text{new negative}&345&1560&1680
\end{array}                                                \tag{6.4}
\]

The multiples of fifteen are the fifteen translated seam copies predicted
by Corollary 5.1.

Reproducible independent audit:

* `scratch/audit_ad_k16_parallel_13230_13232_locality_20260729.py`, SHA-256
  `6f2a02c9e7e4c8c1a3cdf47948b3e6f87cf913a8c0dd9268dbc4facfd1a54bf6`;
* `scratch/ad_k16_parallel_13230_13232_locality_20260729.audit.json`, SHA-256
  `ab4caee86b26b05b11dae379eee2f0d7b4775cd887163464022d4b833dda1ad0`.

## 7. Exact scope of the rigid-3000 parallel no-go

Fix a quotient adjacency cycle and allow only replacement of a selected edge
orbit by another catalogue edge orbit with the same unordered quotient
endpoints.  A positive run of length \(r\) has a local physical witness
consisting of its entering edge, its \(r-1\) internal edges, and its exiting
edge.  If every quotient adjacency in that witness has a singleton parallel
menu, every allowed reassignment keeps those physical edge orbits.  The two
boundary zeros and the internal ones are unchanged, so that positive short
run persists.

Applied to
`scratch/k16_connected_q1_lower2_hamilton_20260729.json` (the post-13230 to
13232 Hamilton artifact, but before any subsequent residence-directed
quotient-adjacency-changing 2-opt),
the exact positive short-run histogram is

\[
(375,1635,1410)
\]

at lengths \(1,2,3\), and the witnesses touching no parallel-variable
adjacency are

\[
(360,1455,1185),
\]

totalling exactly `3000`.  Therefore every parallel-only reassignment on
that fixed quotient cycle retains at least `3000` positive short runs.

This statement is:

1. **positive-run only** -- it proves no negative-run lower bound;
2. **fixed quotient adjacency only** -- a 2-opt can delete a formerly rigid
   witness edge, so the bound does not survive an un-audited 2-opt;
3. **artifact-pinned** -- it applies to SHA-256
   `16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8`;
4. independent of whether another parallel assignment has unit voltage or
   remains connected -- the local witnesses persist even if the lift splits.

The replay script is
`scratch/audit_k16_fixed_qcycle_parallel_residence_no_go_20260729.py`,
SHA-256
`29601428e8c21f3c312c855f7a93fb804e4b0f1bb9f20737c4e582aa9668f861`.
