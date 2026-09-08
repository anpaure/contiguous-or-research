# Audit of the 80-owner overlapping two-seed Q2 completion

Date: 2026-07-26

Audited file:
MATH_ATTACK_K_Q2_OVERLAPPING_TWO_SEED_COMPLETION_20260726.md.

Method: pure mathematics only.

## Verdict

**PASS, with two scope clarifications and one omitted injectivity argument.**

The 80-owner count, twenty-cell factor construction, canonical-edge
criterion, no-four-canonical-edge theorem within the
\(\mathscr D(M;r)\) family, and signed ledger
\[
                         48\to32\to40\to32
\]
are all correct.

## 1. Factor count and exactness

For a matching \(M=\{r,p,q\}\), the special three-sets consist of eight
all-split states and twelve states which fill one \(M\)-pair, empty one,
and split one.  On the all-split \(Q_3\), fixing an orientation of \(r\)
leaves a \(Q_2\) in the \(p,q\) directions.  There are two such faces for
each of four reservoir orientations, hence eight cells.  Every remaining
special state supports one reservoir \(Q_2\), hence twelve more cells.
Thus
\[
                         8+12=20
\]
physical \(Q_2\)'s cover \(20\cdot4=80\) owners exactly once.

The assertion that different parameter pairs \((M,r)\) give different
factors is valid but not proved in the report.  From the factor, the twelve
vertical reservoir cells recover the complementary eight special states.
Those eight states are exactly the transversals of \(M\); the three
coordinate pairs which never co-occur in a transversal recover \(M\).
The parallel-face axis on this recovered \(Q_3\) then recovers \(r\).
Hence
\[
                         (M,r)\longmapsto\mathscr D(M;r)
\]
is injective.

## 2. Canonical-edge criterion

If adjacent matchings \(M,M'\) share \(r\), restricting to one orientation
of the split pair \(r\) leaves the standard 24-owner carrier on the other
four special coordinates and the two reservoir pairs.  The two orientations
of \(r\) therefore give two disjoint literal canonical associators.  When
\(r\) is full or empty, both factors use the same vertical reservoir square,
so the 32-owner complement is unchanged.

Conversely, on the old all-split \(Q_3\), the canonical \(r\)-slab trade
uses the two parallel faces fixing the \(r\)-coordinate.  A partition of
\(Q_3\) into two physical two-faces has a unique fixed coordinate.  Hence
\(\mathscr D(M;a)\) can supply that shore only when \(a=r\), and similarly
the new shore forces \(b=r\).

At corner \(00\), the edge to \(10\) consequently forces distinguished
pair \(56\), while the edge to \(01\) forces \(12\).  This proves the
four-edge incompatibility.  The result is only for the
\(\mathscr D(M;r)\) family; arbitrary twenty-\(Q_2\) retilings of the
80-owner carrier remain open, as the report states.

## 3. Signed ledgers

Measure lower full-pair type in
\[
                         M_{00}=12\mid34\mid56.
\]

For \(\mathscr D(M_{00};56)\), all twelve vertical special states contain
one base full pair and contribute four edges each; the all-split faces
contribute zero.  The total is \(48\).

The canonical \(56\)-slab trade to
\(\mathscr D(M_{10};56)\) consists of two 24-owner associators and removes
\(2\cdot8=16\), leaving \(32\).

For \(\mathscr D(M_{10};13)\), eight of the twelve vertical special states
contain a base pair, contributing \(32\).  Across the two all-split faces,
there are two base-pair edge intersections per reservoir orientation,
contributing eight.  The total is \(40\).

For \(\mathscr D(M_{11};13)\), six vertical special states contain a base
pair, contributing \(24\), and the all-split faces again contribute eight.
The total is \(32\).  Therefore
\[
                         48\to32\to40\to32
\]
is exact: re-axising restores eight units before the second canonical
trade removes those eight.

This is a path ledger relative to the fixed base frame.  It illustrates
the forced-axis theorem but is not a universal invariant for arbitrary
retilings or a monodromic long row.

## 4. Scope clarifications

1. The four matchings form a square in the matching-switch graph.  Its edge
   recouplings are state-dependent and coordinate-overlapping; the theorem
   should not be read as exhibiting two globally defined commuting
   coordinate involutions.
2. The \(q/3\) drift calculation is exact for the stated fully
   product-transversal tensor.  The general \(2tqW/h\) row bound remains
   the correct theorem for arbitrary phase-correlated radius-\(t\)
   pair-geodesic rows.

No correction to the numerical ledgers or factor counts is required.

