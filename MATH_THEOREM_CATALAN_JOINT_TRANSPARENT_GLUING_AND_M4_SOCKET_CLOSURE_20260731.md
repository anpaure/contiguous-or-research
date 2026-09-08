# Joint transparent gluing and an exact socket closure of the decorable `ML(7)` lift

Date: 2026-07-31  
Status: solver-independent recursive implication; explicit physical
\(m=4\) closure certificate; no all-\(m\) gluing-tree or nontrivial-voltage
existence theorem

## 0. Verdict

The correct recursive state has four successive gates:

\[
\boxed{
 \text{joint gap--Hall decoration}
 +\text{ dynamically transparent hexagon tree}
 +\text{ terminal forest trace}
 +\text{ occurrence-cycle/primitive-voltage closure}.}
\tag{0.1}
\]

The first three gates supply an exact Catalan path forest.  They do not imply
the fourth gate.  If a clean cyclic quotient is available, the fourth gate is
exactly a perfect matching of formal path ports whose union with the path
pairing is one occurrence cycle of primitive total voltage.

The new decorable \({\rm ML}(7)\) fixture is positive at the fourth gate as
well.  Its displayed decoration gives fourteen paths in \(J(8,4)\), and the
fourteen explicit connector edges in Section 5 join them into one physical
Hamilton cycle.  Moreover, the fourteen connector intersection colours are
distinct and the fourteen connector union colours are distinct.  Thus this
fixture is a complete physical \(m=4\) base, not only a forest base.

Transparent moves compatible with decorations exist in its exact hexagon
neighbourhood, but no spanning recursive gluing tree is inferred from that
local census.

This closure is symmetry-broken: it is the \(h=1\) case.  It proves neither a
clean-\(H\) quotient for this fixture nor a nontrivial unit-voltage induction.

## 1. Gate ordering

Five frozen inputs are used.

1. `MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`
   proves that alternating turn representatives are a joint occurrence
   problem.  Separate surjectivity of the two turn words is insufficient.
2. `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
   gives the exact local palette and boundary-type test for a fixed
   decoration to survive an incidence-hexagon toggle.
3. `MATH_THEOREM_CATALAN_SUPPLIED_FOREST_OCCURRENCE_CONNECTOR_VOLTAGE_20260731.md`
   gives the exact occurrence-port and voltage theorem after a path forest
   has been supplied.
4. `MATH_THEOREM_CATALAN_TRACE_LONG_SWITCH_AUGMENTING_LINKAGE_20260731.md`
   gives the exact common-core augmenting-linkage certificate when a switch
   changes, rather than preserves, the chosen representatives.
5. `MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md`
   packages that linkage as an exact oriented path-fragment signature on
   bounded tree adhesions.

The logical order matters.  A transparent gluing operation preserves a
specified joint decoration; it does not manufacture one from two separate
rainbows.  Conversely, decoration transparency records turn palettes and
mark types, not physical forest endpoints or connector gains.

## 2. Joint gap--Hall on a starting factor

Let \(C_0\) be a spanning two-factor of \({\rm ML}(2m-1)\), and let \(I\)
select one occurrence of every upper turn colour.  On each factor cycle
containing an \(I\)-mark, form the cyclic gaps between consecutive
\(I\)-marks.  Take the disjoint union of these gaps and join a gap to every
lower turn colour occurring inside it.  Call the resulting bipartite graph
\(\Gamma_I\).

### Lemma 2.1 (aggregate gap criterion)

A lower turn transversal \(J\) alternating componentwise with \(I\) exists
if and only if \(\Gamma_I\) has a perfect matching.  A component containing
no \(I\)-mark must then contain no \(J\)-mark; its residual even cycle also
requires one of its two alternating cross-edge matching phases to be stored.

#### Proof

On a component with \(I\)-marks, alternation puts exactly one \(J\)-mark in
each cyclic \(I\)-gap.  Bijectivity says that the chosen lower colours are
distinct and exhaust their alphabet.  These choices are precisely a perfect
matching of \(\Gamma_I\).  Conversely, choose one occurrence of the matched
colour in each matched gap.  The selected shore types alternate on every
marked component and use every lower colour once.  An unmarked component has
no turn selection; its even residual incidence cycle has the two stated
alternating perfect matchings. \(\square\)

Thus the recursive object is a joint witness

\[
                            D=(I,J),                  \tag{2.1}
\]

together with the residual phase on any wholly unmarked factor component.
It is not an arbitrary independently chosen pair of turn SDRs.

## 3. Dynamic transparent gluing

Let

\[
                         C_t=C_{t-1}\mathbin\triangle Z_t              \tag{3.1}
\]

be a sequence of standard incidence-hexagon toggles.  Test every toggle in
its current context.  Call it \(D\)-transparent when:

1. the selected local turn-colour multisets agree before and after the
   toggle, separately on the two shores; and
2. after reconnection, discard every retained fragment whose selected
   subsequence is empty; within each newly formed component, the last and
   first selected shore types of every cyclically consecutive pair of
   remaining fragments are opposite.

These are the necessary-and-sufficient conditions of the transparent-
hexagon theorem.  They remain exact when toggles overlap, provided each test
is made against the current \(C_{t-1}\), not the initial factor.

### Theorem 3.1 (joint transparent-gluing implication)

Suppose:

1. \(D=(I,J)\) passes Lemma 2.1 on \(C_0\);
2. every toggle in (3.1) is dynamically \(D\)-transparent;
3. the terminal factor \(C_r\) is one Hamilton cycle; and
4. its terminal binary mark trace is outside the unique cycle face
   \[
       \bigl(\text{every positive zero-run has length }2\bigr)
       \ \land\
       \bigl(\text{every one-run has odd length}\bigr).                \tag{3.2}
   \]

Then \(D\) induces a perfect lower--upper diamond matching whose physical
lift is a spanning \(\operatorname {Cat}_m\)-path forest with both outer
palettes exact.

#### Proof

Lemma 2.1 supplies the initial joint decoration.  Induct over the toggles.
Local palette equality preserves both global bijections, and the fragment
boundary rule preserves alternation.  Hence \(D\) decorates \(C_r\).  The
decorated-cycle equivalence gives the perfect diamond matching and its
degree-two physical lift.  Condition (3.2) is exactly the binary-trace
criterion excluding its sole cycle, so the lift is a spanning linear forest.
Its edge and vertex counts give exactly \(\operatorname {Cat}_m\) paths.
\(\square\)

A protected trace breaker disjoint from every future toggle is a useful
composable sufficient state, but it is stronger than the exact terminal test
(3.2).  Likewise, requiring a prepublished gluing tree is irrelevant unless
its toggles are transparent for the dynamically carried witness \(D\).

The strongest currently proved finite occurrence state is optionally
stronger: require the gap--colour graph to be a balanced forest, so its
perfect matching is unique and recovered by leaf peeling.  Decoration
transparency alone does not preserve this property.  The exact transfer test
deletes the changed old gap edges, contracts the retained gap-forest
components, inserts the new gap edges, and requires the resulting attachment
multigraph to be loopless and acyclic.  This graphic clause makes occurrence
selection deterministic, but it is not needed for Theorem 3.1 and does not
replace the physical socket state below.

### Lemma 3.2 (bounded common-core augmentation width)

Let a Hamilton-safe alternating circuit of length \(2t\) change an augmented
trace graph of shore size \(N\) and old deficiency \(d\).  Let \(H\) be the
intersection of the old and new augmented graphs, and write

\[
                    \nu(H)=N-r.                       \tag{3.3}
\]

Then

\[
                              r\le d+3t.              \tag{3.4}
\]

In particular, a decorated parent has \(d=0\), so a bounded \(2t\)-gluing
polygon exposes an augmenting-linkage state of width at most \(3t\).

#### Proof

The circuit replaces \(t\) physical incidence edges.  It changes at most
\(t\) upper-turn and at most \(t\) lower-turn augmented edges as well.  Thus
at most \(3t\) old augmented edges are absent from \(H\).  Restrict an old
maximum matching of size \(N-d\) to \(H\); at most \(3t\) of its edges are
lost, leaving a matching of size at least \(N-d-3t\).  Hence
\(N-r=\nu(H)\ge N-d-3t\), which is (3.4). \(\square\)

By the common-core augmenting-linkage theorem, the new augmented graph is
perfect exactly when \(r\) vertex-disjoint augmenting paths cover all
vertices exposed by a maximum matching of \(H\).  Therefore a recursion
which permits the decoration to change across a bounded polygon need carry
only at most \(d+3t\) simultaneous augmentation pairs.  This is a width
bound, not a bounded-path-length theorem: the augmenting paths can traverse
the entire retained augmented graph.

### Corollary 3.3 (exact bounded-adhesion linkage state)

Suppose the retained augmented graph is decomposed into blocks with disjoint
interiors and a tree of adhesions of size at most \(b\).  At every block
record the realizable oriented vertex-disjoint path-fragment patterns on its
boundary, including exposed source/sink terminals and used boundary
vertices.  These signatures compose exactly by joining compatible fragments
and rejecting repeated boundary use, an internal directed cycle, or an
illegal terminal orientation.  Their number is at most

\[
                              2^{O(b\log b)}.          \tag{3.5}
\]

Hence common-core matching repair is an exact finite tree-DP coordinate for
bounded adhesion, even though its realized paths may be global.

This is the boundary-linkage/gammoid composition theorem.  It proves
finite-state composition for a supplied bounded-adhesion decomposition; it
does not prove that the desired Catalan gluing tree has bounded adhesion or a
nonempty accepting root state.

For a fixed-\(D\) transparent toggle, the old decoration itself survives and
this reaugmentation state is unnecessary.  Lemma 3.2 is the exact bounded
fallback when a recursive step changes representatives instead of preserving
them.

## 4. What must be added for sockets and voltage

Let \(F\) be the terminal path forest from Theorem 3.1.  If \(F\) is
invariant under a free clean action \(H\cong\mathbb Z_h\), give every quotient
path two formal endpoint occurrences and let \(P_F\) pair the two ports of
each path.  An isolated path contributes two different formal ports at its
one vertex.

By the supplied-forest occurrence theorem, an \(H\)-invariant Hamilton
closure retaining \(F\) edgewise exists if and only if a literal connector
set \(M\) satisfies:

1. every formal port is used exactly once;
2. selected connector developments are distinct, disjoint from \(F\), and
   satisfy every declared literal capacity;
3. \(P_F\cup M\) is one alternating occurrence cycle; and
4. its closed total voltage \(V\) is primitive:
   \[
                              \gcd(h,V)=1.             \tag{4.1}
   \]

Turn-colour transparency does not imply any of these statements.  In
particular it does not imply clean-\(H\) invariance, endpoint Hall, literal
connector injectivity, occurrence connectivity or a gain residue.

Three connectivity coordinates must remain separate.  The gap-forest state
tracks uniqueness/connectivity of the alternating occurrence SDR; the
gammoid signature of Corollary 3.3 repairs the joint turn/incidence matching
after a polygon switch; and the physical socket state below joins the path
components of the resulting forest and carries voltage.  A complete
recursive state is their product, even though all three are naturally
described by exposed occurrences and path pairings.

### Lemma 4.1 (exact socket-profile test at one hexagon)

For a toggled incidence hexagon, let \(x(L)\) be the indicator that one of
its three lower vertices is selected by \(D_A\), and let \(y(U)\) be the
indicator that one of its three upper vertices is selected by \(D_B\).  At
the corresponding physical middle vertices the decorated-forest degrees are

\[
 \deg_F(U)=1-y(U)+\sum_{L\in N_C(U)}x(L),             \tag{4.2}
\]

\[
 \deg_F(\infty+L)=1-x(L)+\sum_{U\in N_C(L)}y(U).     \tag{4.3}
\]

Consequently the hexagon toggle preserves the literal socket multiplicity
\(2-\deg_F(v)\) at every one of its six physical vertices if and only if

\[
 x(L_a)=x(L_b)=x(L_c),\qquad
 y(U_{ab})=y(U_{bc})=y(U_{ca}).                       \tag{4.4}
\]

#### Proof

An unmarked trace vertex has one residual cross edge and a marked trace
vertex has none, giving the first terms in (4.2)--(4.3).  A selected turn at
an adjacent opposite-shore vertex contributes one same-rail chord, giving
the sums.  The toggle changes only the one hexagon neighbour at each of the
six vertices.  Equality of all three upper-vertex degrees says that the
three lower indicators are invariant under the induced three-cycle, hence
are constant.  The other shore is identical. \(\square\)

### Corollary 4.2 (decoration transparency preserves the socket profile)

Every decoration-transparent incidence-hexagon toggle satisfies (4.4), and
therefore preserves the complete literal degree/port multiset of the physical
forest.

#### Proof

Apply \(S\mapsto S\cap\{a,b,c\}\) to the local multiset equality.  On one
selected shore the old/new projected colour triples are

\[
             (ab,bc,ca)\quad\hbox{and}\quad(ac,ab,bc),            \tag{4.5}
\]

while on the other they are

\[
             (a,b,c)\quad\hbox{and}\quad(b,c,a).                  \tag{4.6}
\]

Equality of the selected submultisets before and after the three-cycle forces
the three selection indicators on that shore to be \(000\) or \(111\).
Apply this separately to both shores and then use Lemma 4.1. \(\square\)

For \(h>1\), a quotient-voltage transport statement additionally requires
the toggle to be performed as a full free \(H\)-orbit, or requires both the
old and new forests to be independently audited as \(H\)-invariant.  One
isolated physical toggle generally breaks the quotient action and has no
common voltage interpretation.

Condition (4.4) preserves only the locations and multiplicities of sockets.
It does not preserve the pairing of those sockets into physical forest
paths.  Assuming the post-toggle lift \(F'\) is still a forest, a fixed
connector set \(M\) transports the same closure exactly when \(M\) remains
literal/legal and disjoint from \(F'\), and the new path involution
\(P_{F'}\) satisfies the one-cycle and primitive-voltage tests with \(M\).

### Lemma 4.3 (complete connector-aware boundary state)

Fix a clean \(H\)-quotient, a covered physical vertex domain, a literal
exterior connector catalogue, boundary representatives and one gain gauge.
Let a partial degree-at-most-two physical forest expose every degree-deficit
occurrence on its boundary, and assume every nonempty component meets that
boundary.  Contract every internal path fragment and record:

1. the remaining degree demand at each literal boundary occurrence;
2. the pairing of boundary occurrences joined by retained internal paths;
3. the oriented gain of every paired path; and
4. the usage multiplicity, or equivalently residual capacity, of every
   literal edge-orbit and private resource visible to the fixed exterior
   catalogue.

Relative to these fixed data, two partial forests with the same record are
interchangeable for every exterior connector completion from the catalogue.
Gluing composes the two boundary pairings; a nonterminal sealed component is
a subtour, while an empty terminal boundary is accepted exactly when the
resulting graph is one cycle of primitive voltage.

#### Proof

An exterior edge can see the fixed internal vertex domain only through its
exposed degree deficits.  Once internal paths are contracted, their
connectivity contribution is exactly the boundary pairing and their voltage
contribution is exactly its oriented gain in the fixed gauge.  Literal edge
and private-resource conflicts depend only on the recorded residual
capacities.  Therefore every allowed exterior completion has the same
degrees, component permutation, total gain and capacity feasibility for two
states with identical records.  Conversely, whenever the fixed catalogue can
distinguish one of these fields, it must remain in the state. \(\square\)

This is an information-complete additional state for a connector-aware
transparent gluing recursion.  A fixed finite catalogue may quotient states
which have identical legal exterior behavior.  One may instead postpone
connectors until the root and solve the exact occurrence-cycle condition
there.  Hexagon transparency for \(D\) alone is neither a positive nor a
negative socket certificate.

## 5. Explicit closure of the positive `m=4` forest

Use the \({\rm ML}(7)\) cycle and the occurrence sets \(I,J\) displayed in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.
Its physical diamond matching is the following fourteen paths in
\(J(8,4)\), written as decimal bitmasks:

```text
53 29 15 43 163 225 201 75 71 197 204 156 30 46 106 114 178 154 153
23 51 113 120 108 45 169
101 39 135 147 177 240 232 172
54 102 198 202 216 89 27 58
60 180 149 141 139
83 86 150 166
99 105
195
77 92
165 228 116 85 209 210
57 184
78 90
142 170 226
212
```

Select the fourteen connector edges

\[
\begin{split}
 &(153,169),(23,54),(58,60),(139,195),\\
 &(195,226),(142,78),(90,83),(166,165),\\
 &(210,212),(212,92),(77,105),(99,101),\\
 &(172,184),(57,53).
\end{split}                                           \tag{5.1}
\]

Every displayed connector is a Johnson edge, the connectors are distinct
and avoid the forest, and every path endpoint occurrence is used exactly
once.  Reading the oriented paths and connectors gives the single cycle

```text
53 29 15 43 163 225 201 75 71 197 204 156 30 46 106 114 178 154 153
169 45 108 120 113 51 23
54 102 198 202 216 89 27 58
60 180 149 141 139
195
226 170 142
78 90
83 86 150 166
165 228 116 85 209 210
212
92 77
105 99
101 39 135 147 177 240 232 172
184 57
```

with closing edge \((57,53)\).  This visits all seventy vertices of
\(J(8,4)\) once.

The connector lower colours are

\[
137,22,56,131,194,14,82,164,208,84,73,97,168,49,    \tag{5.2}
\]

and the connector upper colours are

\[
185,55,62,203,227,206,91,167,214,220,109,103,188,61.\tag{5.3}
\]

Both lists are injective.  The retained forest already uses every rank-three
and rank-five edge colour exactly once, so the whole Hamilton cycle has
profile \(1^{42}2^{14}\) on each outer palette.  At \(h=1\), the voltage
condition is vacuous; (5.1) is the required one occurrence cycle.

The complete endpoint audit is also positive rather than witness-fragile.
The forest has 28 formal ports, 67 legal port pairs and 60 distinct physical
endpoint seams.  The sole same-component pair is the edge \((54,58)\); using
it seals that path as a proper subtour.  Deleting this immediately dead pair
leaves the exact cross-component/subtour-pruned graph with 66 port pairs and
59 physical seams.  The unpruned graph has 2,944 formal port perfect
matchings, while the pruned graph has 2,704.  Exactly 1,192 are connected
closures.  Swapping the two formal labels at each of the two isolated
vertices accounts for a factor four, leaving exactly 298 distinct physical
Hamilton closures.  Of these, 137 have connector colours injective on both
shores.  The literal certificate (5.1) is one of those 137.

## 6. Transparent does not mean connector-transparent

The distinction in Lemma 4.1 occurs literally in the same \(m=4\) fixture.
Take the transparent hexagon

\[
                  H=20,\qquad(a,b,c)=(1,3,5),         \tag{6.1}
\]

and the common decoration with base-cycle occurrence sets

```text
I = 1 2 3 4 5 9 10 11 14 15 17 19 21 23 24 26 27 28 31 32 34
J = 0 1 2 3 4 8 9 10 12 14 16 17 19 21 23 25 26 27 29 31 33
```

Exact replay verifies the retained-fragment boundary alternation, so the
toggle is decoration-transparent.  All six hexagon vertices are unmarked;
in particular (4.4) holds on both shores.  The old and new physical forests
differ only by the three-switch

\[
\begin{split}
 &(30,156),(54,150),(60,180)\\
 &\hspace{12mm}\longrightarrow
   (30,150),(54,180),(60,156).                        \tag{6.2}
\end{split}
\]

The literal connector set

\[
\begin{split}
M=\{&(23,86),(46,166),(53,165),(57,169),(60,172),\\
     &(77,101),(86,114),(90,154),(92,212),(99,195),\\
     &(99,226),(139,142),(153,184),(201,209)\}
                                                               \tag{6.3}
\end{split}
\]

is legal and socket-exact for both forests.  With the old forest it gives the
single 70-cycle

```text
15 29 53 165 228 116 85 83 210 150 54 102 78 90 154 153 184 57
169 45 108 120 113 51 23 86 114 106 170 142 139 141 149 180 60 172
232 240 177 147 135 39 101 77 92 212 209 201 195 99 226 178 58 27
89 216 202 198 166 46 30 156 204 197 71 75 105 225 163 43
```

whereas the new forest with the same \(M\) has two cycles, of orders 46 and
24.  Thus even

\[
 \text{decoration transparency}
 +\text{identical literal socket profile}
 +\text{unchanged legal connector set}                \tag{6.4}
\]

does not preserve occurrence connectivity.  This is an \(h=1\) failure, so
it is independent of voltage.  The missing datum is exactly the physical
path pairing/subtour state in Lemma 4.3.

## 7. Exact conclusion and open gate

The positive \(m=4\) fixture passes joint gap--Hall, the forest trace, and a
literal endpoint connector cycle; its neighbourhood also contains genuinely
transparent moves.  It is therefore a rigorous physical base and local
transfer fixture for a connector-aware recursion.  It does not by itself
supply the spanning transparent gluing tree required in (0.1).

What remains open is the uniform recursive statement.  One must construct,
for every \(m\), an accepting joint decoration through a dynamically
transparent gluing tree and either:

* solve the final endpoint occurrence cycle directly; or
* propagate the gain-decorated boundary state of Lemma 4.3.

If representatives are allowed to change at a \(2t\)-polygon, Lemma 3.2
bounds the simultaneous common-core augmentation width by \(d+3t\), and
Corollary 3.3 composes its exact global linkage relation over a supplied
bounded-adhesion tree.  The remaining existence problem is to construct an
all-\(m\) gluing tree whose joint gap-forest, gammoid, socket/voltage and
guard states have a nonempty accepting root.

For a nontrivial clean quotient, primitive voltage remains an additional
root condition.  No arbitrary frozen SDR, arbitrary standard gluing tree, or
decoration-transparent toggle is claimed to satisfy it automatically.

## 8. Audit

Run

```text
python3 scratch/audit_catalan_joint_transparent_m4_socket_closure_20260731.py
python3 scratch/audit_catalan_decorable_ml7_endpoint_closure_20260731.py
python3 scratch/audit_catalan_transparent_hex_connector_transport_20260731.py
python3 scratch/audit_catalan_boundary_linkage_gammoid_20260731.py
```

The first replay reconstructs the displayed joint decoration, its exact
fourteen-path physical forest, the connector certificate, the 70-cycle and
both colour profiles.  The second independently exhausts the full endpoint
graph and every physical closure.  The third checks the local degree formula,
automatic socket-profile preservation, and the one-cycle-to-two-cycles
transparent-toggle counterexample.  The fourth exhaustively checks the
matching-gain/linkage identity on every bipartite graph with shores of size
three.
