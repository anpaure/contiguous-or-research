# Post-glue ECO topology and terminal decoration are logically separate

Date: 2026-07-31  
Status: exact conditional all-dimension central-CLMT reduction; exact
project-`m=5` positive replay; no uniform ECO hypertree or forest-decorated
Hamilton construction

## 0. Verdict

For the central Catalan Linear Matching problem, a decoration need not be
transported through the component glues.  The proof-safe order is

\[
 \boxed{
 \text{strict disjoint ECO incidence hypertree}
 \longrightarrow \text{one middle-levels Hamilton cycle}
 \longrightarrow \text{terminal alternating-circuit walk through 2-factors}
 \longrightarrow \text{one terminal joint alternating SDR}.}
 \tag{0.1}
\]

The first implication is purely physical and topological.  It uses no turn
transversal, gap matching, owner alignment, coherence, or occurrence router.
The second implication chooses the decoration only on the terminal Hamilton
cycle.

There is one necessary final qualification.  A terminal joint alternating
SDR gives a spanning physical graph of maximum degree two, but it gives a
linear forest only when its binary trace is off the unique cycle face.  Thus
the exact central-CLMT terminal test is

\[
 \boxed{\text{perfect augmented matching}\quad+\quad
        \text{binary-trace forest test}.}            \tag{0.2}
\]

The trace clause cannot be omitted.  At `m=2`, the valid alternating trace
`100100` gives a joint SDR but its physical lift is a 4-cycle plus two
isolated vertices.

The synchronized project-`m=5` three-`C10` fixture genuinely realizes the
post-glue order.  Its independent audit first toggles the two standard ECO
hexagons on the canonical `36+72+144` factor, obtaining one `252`-vertex
Hamilton cycle, and only then applies `C1,C2,C3`; every intermediate state
is Hamilton and the final augmented matching has order `210`.  The same
literal operations also admit the repair-first presentation because all
thirty `C10` vertices avoid the twelve standard ports.  Post-glue validity
is therefore directly replayed, not inferred only from commutation.

## 1. Strict incidence hypertrees Hamiltonize without decoration

Let `F` be a two-factor with component set `V`.  A physical ECO atom `t` is
an alternating incidence hexagon, with three old edges in `F` and three new
edges outside `F`.  Let

\[
                         S_t\subseteq V              \tag{1.1}
\]

be the set of initial components containing its old edges.  Only atoms with
`|S_t|>=2` are used below.

A family `T` is a **strict disjoint ECO incidence hypertree** when:

1. the six physical ports of distinct atoms are disjoint;
2. the component--atom incidence graph on `V disjoint-union T`, with
   `v--t` iff `v in S_t`, is a tree; and
3. on the common Boolean cube, whenever a pending atom `t` meets
   `|S_t|` distinct current component blocks, its toggle merges exactly
   those blocks and splits no block.

Item 3 is automatic for a three-component hexagon, but is a real phase
condition for a hexagon with two old edges in one component.  Pairwise port
disjointness alone does not imply it.

### Theorem 1.1 (decoration-free ECO Hamiltonization)

Toggling every atom of a strict disjoint ECO incidence hypertree, in any
order, produces one Hamilton cycle.

#### Proof

Port disjointness makes all symmetric differences commute and preserves
degree two.  In a tree incidence graph, the component vertices incident
with a pending atom lie in distinct blocks formed by the earlier atoms:
otherwise an earlier incidence path between two such vertices, together
with the two edges through the pending atom, would make an incidence cycle.
Strictness therefore lowers the current component count by

\[
                          |S_t|-1.                   \tag{1.2}
\]

The incidence-tree edge count gives

\[
                 \sum_{t\in T}(|S_t|-1)=|V|-1.      \tag{1.3}
\]

Starting with `|V|` components, the final two-factor consequently has one
component.  A connected two-factor is a Hamilton cycle.  No decoration was
introduced anywhere in the argument. \(\square\)

For one prescribed order, the common-cube quantifier may be weakened to
literal strictness at the prefixes of that order.  The all-subset form above
is what licenses the phrase “in any order.”

## 2. Terminal circuit packets and the exact SDR implication

Write the Hamilton cycle supplied by Theorem 1.1 as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
 \quad\text{in }{\rm ML}(2m-1).                     \tag{2.1}
\]

### Lemma 2.1 (two-factor difference decomposition)

For any two spanning 2-factors `F,F'` of one graph,
`F symmetric-difference F'` decomposes into edge-disjoint closed alternating
circuits.  Toggling them successively preserves degree two and ends at `F'`.

#### Proof

Colour `F-F'` red and `F'-F` blue.  At every vertex the red and blue degrees
are equal.  Pair red and blue half-edges at each vertex and follow the
pairings.  This partitions the symmetric difference into closed alternating
trails, which may be split at repeated transition states.  Each toggle
deletes and inserts the same number of edges at every incident vertex, so it
preserves degree two.  The circuits are edge-disjoint, hence each
unprocessed circuit remains alternating; after the last toggle the factor is
`F'`. \(\square\)

Consequently, for any terminal Hamilton cycle `C*`, Lemma 2.1 supplies a
packet from the Hamilton cycle of Theorem 1.1 to `C*`.  Intermediate states
need only be 2-factors; they need not be Hamiltonian or decorated.  Demanding
Hamiltonicity at every prefix is an optional stronger routing normal form,
satisfied by the project-`m=5` packet below.

Form the augmented occurrence graph of `C*`: one shore consists of the
`A` occurrences and lower-turn colours, the other of the `B` occurrences
and upper-turn colours, with the two incidence edges at each cycle position
and the two turn edges.  This is the graph in
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`.

### Theorem 2.2 (terminal augmented matching)

If the terminal augmented occurrence graph has a perfect matching, then
`C*` has a joint alternating upper/lower occurrence SDR.  The resulting
diamond matching is perfect, its physical Johnson lift is spanning and has
maximum degree two, and it has exactly `m Cat_m` edges.

If, in addition, the induced cyclic binary mark trace is not on the face

\[
 \text{every zero-run has length two and every one-run has odd length},
                                                               \tag{2.2}
\]

then the lift is a spanning linear forest with exactly `Cat_m` path
components.  Hence Theorems 1.1 and 2.2, with (2.2) excluded, imply the
central Catalan Linear Matching statement.

#### Proof

A perfect augmented matching chooses every upper and lower turn colour
once.  Its unmatched cycle-incidence positions are forced into the unique
perfect matchings of the intervening even paths.  Reading the turn edges
therefore gives the two occurrence SDRs, and reading the residual incidence
edges proves alternation.  This is exactly the decorated-cycle/perfect-
diamond equivalence.

For a fixed upper occurrence transversal, the selected lower occurrences
are obtained from a perfect matching of the occurrence-labelled
gap--lower-colour graph.  Parallel occurrences remain distinct: a
colour-level gap matching with occurrence choices suppressed does not
specify the physical SDR.

The same equivalence gives the spanning degree-two physical lift and its
edge count.  The binary-trace theorem says that this lift has a cycle if and
only if (2.2) holds; in that event it has exactly one cycle.  Off that face
it is a forest, and Euler's identity gives `Cat_m` components. \(\square\)

### Proposition 2.3 (joint SDR alone is insufficient)

The trace clause in Theorem 2.2 is necessary already at `m=2`.

#### Proof

Use the six-cycle

\[
 A_0,B_{01},A_1,B_{12},A_2,B_{02},A_0
 \quad\text{in }{\rm ML}(3).                        \tag{2.3}
\]

Mark `A_0` and `B_{12}`.  The cyclic mark word is `100100`.  The selected
upper turn is the unique rank-three colour and the selected lower turn is
the unique rank-zero colour; the two rail types alternate, so this is a
joint alternating SDR.

In the position model, the two marked turns give edges `(5,1)` and `(2,4)`,
while the two residual zero-runs give edges `(1,2)` and `(4,5)`.  These four
edges make the cycle

\[
                         1-2-4-5-1,                 \tag{2.4}
\]

and leave positions `0,3` isolated.  Thus the lift is not a linear forest.
\(\square\)

## 3. Comparison with the repair-first private collar

The post-glue theorem deliberately drops all of the following repair-first
hypotheses:

* one decoration common to the preglue factor and every glue subset;
* all-six coherence of every glue relative to that decoration;
* pointwise forced-port owner alignment;
* leaf-forest matching transport through every prefix;
* ownership-indexed occurrence-channel export and weighted router
  resilience.

It replaces them by one terminal existential test: after topology is
closed, find a Hamilton endpoint which passes the augmented matching and
trace tests.  Lemma 2.1 then supplies a packet automatically.  Therefore it
is strictly weaker as a certificate
of the **central** Catalan linear forest.  It is not a substitute for the
repair-first private collar as a recursive interface: it exports no
prefix-stable owners, routes, sockets or downstream RSB state.

The implication between outcomes is one-way.  A repair-first private collar
whose final trace is a forest already gives the post-glue central conclusion
(use the empty terminal packet).  A post-glue certificate need not admit any
decoration on the preglue factor or on an intermediate glue state.

For both central routes, the ordinary binary-trace forest test proves only
central acyclicity.  Coordinate residence, all-depth shadow support,
endpoint sockets and primitive voltage, Pascal reachability, and the
common-`Q`/lower compiler remain separate downstream obligations unless
they are independently exported and literally replayed.  In particular,
neither a post-glue terminal matching nor a repair-first central decoration
by itself discharges those obligations.

## 4. Exact project-`m=5` chronology

For the synchronized private three-`C10` fixture, the canonical factor has
component orders

\[
                              36,72,144.             \tag{4.1}
\]

The standard atom `g0` touches the `36`- and `144`-vertex components, and
`g1` touches the `72`- and `144`-vertex components.  Their twelve ports are
disjoint.  Thus their component--atom incidence graph is the five-vertex
tree with component edges

\[
                              36-144-72.             \tag{4.2}
\]

Literal replay gives component profiles

\[
 g0:\ 72+180,\qquad g1:\ 36+216,\qquad
 g0+g1:\ 252.                                      \tag{4.3}
\]

Hence `{g0,g1}` is the required strict binary incidence hypertree and its
toggle is the post-glue Hamilton cycle.

Starting from that literal cycle, the independent replay applies the three
displayed `C10` circuits.  Each circuit alternates at its stage, every
prefix remains Hamilton, and the augmented matching ranks are

\[
                              207,208,209,210.        \tag{4.4}
\]

The terminal forced decoration has `84` marked occurrences on each shore,
its gap graph is a forest, and its binary trace is on the linear side.
It therefore realizes Theorems 1.1 and 2.2 in the post-glue order.

The thirty `C10` vertices are disjoint from the twelve `g0,g1` ports.  Thus
the final symmetric difference is also equal to the repair-first order.  In
that presentation the repaired preglue profile is `120+132`, and either
standard atom alone Hamiltonizes.  This commuted presentation is useful for
the private-collar theorem, but it is not the only authenticated chronology.

This fixture does not prove that a terminal packet exists after an arbitrary
ECO hypertree.  It proves one exact endpoint-specific post-glue packet.
The distinct packet in
`MATH_THEOREM_CATALAN_M5_THREE_C10_PALETTE_REPAIR_20260731.md` must not be
silently combined with the private packet used here.

## 5. The two routes and the weakest exact missing theorem

The choice of the initial undecorated Hamilton cycle is immaterial to the
minimal existential route.  Lemma 2.1 shows that its exact remaining target
is:

> **Decorated Middle Levels theorem.**  For every `m>=2`, `ML(2m-1)` has a
> Hamilton cycle whose augmented occurrence graph has a perfect matching
> and whose induced binary trace is off the cycle face (2.2).

Equivalently, choose one upper-turn transversal, then a perfect matching of
the occurrence-labelled gap--lower-colour graph, and require the resulting
common mark trace to be a forest trace.  A colour-level gap matching with
occurrence labels suppressed is insufficient for the last test.  A
leaf-peelable gap forest is a useful stronger certificate, not a necessary
central condition.  An all-dimensional raw ECO hypertree gives a canonical
starting Hamilton cycle but does not reduce the content of this terminal
theorem.

The recursive transparent route is stronger.  For one incidence-hex toggle
to preserve a fixed decoration, it is necessary and sufficient that

1. the selected local turn-colour multisets agree separately on both shores;
   and
2. the retained-fragment boundary mark types alternate after reconnection.

Leaf-peelable transport additionally requires the changed gap attachments
to remain loopless and acyclic after contraction.  The authenticated
`ML(7)` census has `31` alternating hexagons, `16` Hamilton outputs, `10`
decorable outputs after representatives may change, and only `6` outputs
with a common forest decoration.  Hence fixed-decoration transparency is a
strictly stronger recursive interface, not a necessary existence gate.

Preassigned period-three support is stronger again: the known repaired
project-`m=5` decorated Hamilton endpoint supports none of the `729` complete
complement-paired filter banks.  Terminal decoration must therefore be
chosen jointly with any such forced support, not inferred from it.

## 6. Audit

Run

```text
python3 scratch/audit_catalan_postglue_eco_hypertree_terminal_sdr_20260731.py
```

The audit independently reconstructs the standard `m=5` component supports,
the post-glue Hamilton cycle, all three terminal `C10` stages, the terminal
augmented matching and trace state, the commuted repair-first endpoint, and
the exact `m=2` trace obstruction.  It is finite and solver-free.
