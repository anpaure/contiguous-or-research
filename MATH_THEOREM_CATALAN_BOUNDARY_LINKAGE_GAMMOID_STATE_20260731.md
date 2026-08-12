# Boundary linkage is the exact finite state for bounded Catalan switches

Date: 2026-07-31  
Status: exact matching/linkage equivalence and finite-boundary composition;
no all-m accepting-glue existence theorem

## 1. Alternating repair as a directed linkage

Let \(G=(L,R;E)\) be bipartite and let \(M\subseteq E\) be a matching.
Write \(L_0,R_0\) for its exposed vertices.  Form the auxiliary digraph
\(D_M(G)\) by orienting

\[
 E\setminus M:L\longrightarrow R,qquad
 M:R\longrightarrow L.
\tag{1.1}
\]

### Theorem 1.1 (matching gain equals linkage number)

The maximum number of pairwise vertex-disjoint directed paths from
\(L_0\) to \(R_0\) in \(D_M(G)\) is

\[
                         \nu(G)-|M|,
\tag{1.2}
\]

where \(\nu(G)\) is the maximum matching size.  In particular, if
\(|L|=|R|=N\) and \(|M|=N-r\), then \(G\) has a perfect matching
iff all \(r\) exposed left vertices can be linked to the \(r\) exposed
right vertices by vertex-disjoint paths.  The source--sink bijection is not
prescribed.

#### Proof

Directed \(L_0\)-to-\(R_0\) paths are exactly \(M\)-augmenting paths.
Toggling \(t\) disjoint paths increases the matching size by \(t\).  In the
other direction, the symmetric difference of \(M\) with any maximum
matching decomposes into alternating cycles and exactly
\(\nu(G)-|M|\) vertex-disjoint augmenting paths.  \(\square\)

For fixed sinks, the linkable source subsets form a gammoid after the
standard vertex-splitting reduction: under the standard terminology this is
the restriction to the source ground of the strict gammoid on all split
vertices.  The complete unpaired linkage number and every prescribed source
subset against the fixed sink bank are computable by vertex-capacitated
max-flow.  A prescribed source--sink pairing is a different, generally
multicommodity question.

## 2. Bounded switches have bounded state

Let two middle-levels trace graphs differ by one Hamilton-safe alternating
\(2t\)-circuit.  Such a switch changes at most \(t\) physical-incidence,
\(t\) upper-turn and \(t\) lower-turn augmented edges.  If the old
graph has deficiency \(e\), restrict one old maximum matching to the
common graph.  At most \(3t\) of its edges are deleted, so the common
deficiency satisfies

\[
                            r\le e+3t.
\tag{2.1}
\]

Combining (2.1) with Theorem 1.1 gives:

### Corollary 2.1

A bounded \(2t\) gluing polygon from a decorated parent has an exact
augmenting state on at most \(3t\) exposed pairs.  From a parent of
deficiency \(e\) the width is at most \(e+3t\).

The paths may traverse globally.  Equation (2.1) proves bounded **width**,
not bounded path length or automatic existence.

## 3. Exact finite-boundary signature

Let a recursive block have boundary terminal set \(B\).  Its
**linkage signature** records every collection of pairwise vertex-disjoint
directed path fragments whose endpoints lie in \(B\) together with the
exposed source/sink terminals, including their orientations and which
boundary vertices are used.  Internal vertices may not appear as fragment
endpoints.

If at most \(r\) exposed terminals occur on each shore, put

\[
                              p=b+2r.                 \tag{3.1}
\]

There are finitely many endpoint patterns; a safe crude bound is

\[
                         4^p p!=2^{O(p\log p)}.       \tag{3.2}
\]

If endpoints of new edges have not already been assigned inside blocks,
they must also be included in \(p\).  The unpaired source-set subrelation is
computed by vertex-capacitated flow, or by the corresponding gammoid oracle.
The full pairing-resolved signature is not in general one gammoid query: it
must be supplied, enumerated by an exact disjoint-path routine, or generated
compositionally by the boundary dynamic program below.

### Theorem 3.1 (exact tree composition)

Suppose blocks have disjoint interiors and are glued along a tree of
boundary adhesions of size at most \(b\).  The linkage signature of their
union is obtained exactly by joining compatible child path fragments at
each adhesion and rejecting:

1. a boundary vertex used more than once;
2. an internal directed cycle; or
3. a fragment with an illegal source/sink orientation.

Consequently existence of the complete common-core augmenting linkage is
decidable by a finite-state tree dynamic program whose state size depends
only on the total named-terminal parameter \(p\).  For bounded switch width,
bounded adhesion and internally assigned new edges this is
\(2^{O(p\log p)}\).

#### Proof

Restrict any global disjoint linkage to each block.  Cutting at adhesion
vertices gives one recorded child pattern per block, and disjointness and
orientation give conditions 1--3.  Conversely, compatible child fragments
join uniquely through the identified adhesion vertices.  Conditions 1--3
make their union a collection of vertex-disjoint directed paths with the
required external endpoints.  Induction over the gluing tree proves both
directions.  \(\square\)

The scalar deficiency is therefore not the recursive state.  The exact
state is the bounded terminal-linkage relation.  On the direct/private face
where endpoint pairings are forced, it collapses to ordinary matching or a
single source-set gammoid; in general it is a pairing-resolved linkage
signature, not one matroid.

## 4. Relation to the other recursive rows

This theorem closes only the matching-repair bookkeeping for a supplied
bounded switch.  A Catalan gluing state must still carry, independently,

* the graphic connectivity partition of the leaf-peelable gap forest;
* the physical trace-run and endpoint-socket labels;
* primitive voltage; and
* the deeper-shadow and compiler guards.

Thus a transparent polygon plus a passing gap-forest contraction test can
be augmented by an exact bounded linkage signature.  What remains open is
an all-m gluing tree whose every node has a nonempty joint state.

## 5. Reproducible finite audit

The companion audit exhausts every bipartite graph on \(3+3\) vertices
and every matching it contains.  For each pair it compares maximum matching
gain with a node-capacitated max-flow in (1.1).  It also checks all balanced
perfect-matching cases.  This is a finite regression for Theorem 1.1 only;
it does not audit the pairing-resolved boundary table or the tree dynamic
program and is not the proof of the general statement.
