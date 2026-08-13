# The MSW coalesced-port gate is an exact conflict-CSP, not an ordinary Hall matching

**Date:** 2026-08-14  
**Status:** unconditional finite characterization. The Catalan recursive
extension statement in Section 4 is a sharp remaining gate, not a theorem.

## 0. Setup

Fix \(m,d\), \(n=2m+1\), a root row \(r\), and a directed
area-increasing common-history option catalogue. Let \(V\) be the MSW rows and
let \(r\) be the mountain. An option is a tuple

\[
 o=(u,v,\epsilon,a,\delta,b),
\]

where \(u\ne r\) is the child demand, \(v\) is an allowed parent,
\(\epsilon,\delta\in\{0,1\}\) are endpoint orientations, and

\[
 F^{u,\epsilon}_j(a)\cup F^{v,\delta}_j(b)
 \subseteq P^{u,\epsilon}_j(a)\cap P^{v,\delta}_j(b)
 \qquad(0\le j<d).
\]

For a row \(w\), two distinct starts conflict when their cyclic distance is
at most \(d\). Repeated use of one start is allowed only when all endpoint
ports in that class admit one common word, equivalently

\[
 \bigcup_iF^{(i)}_j\subseteq\bigcap_iP^{(i)}_j
 \qquad(0\le j<d).
\]

## 1. Exact conflict-CSP theorem

### Theorem 1.1

A coalesced separated-port arborescence exists if and only if one can choose
one option \(o_u\) for every \(u\in V\setminus\{r\}\) such that:

1. all chosen incidences at each row use one common orientation;
2. every same-start incidence class passes the multiway common-history test;
   and
3. the set of distinct chosen starts incident at each row is independent in
   the \(d\)-th power of the cyclic graph \(C_n\).

Whenever every catalogue option strictly increases area and \(r\) is the
only row with no parent demand, no further global connectivity constraint is
needed: the selected parent map is automatically an arborescence rooted at
\(r\).

#### Proof

Necessity is exactly the definition of one global row orientation and
coalesced separated ports. Conversely, realize each distinct row-start class
once. Independence in \(C_n^d\) says that two different starts have cyclic
distance at least \(d+1\), so the local simultaneous freedom theorem applies.
For a same-start class, use the union of all endpoint forced sets as its
common word; condition 2 places it inside every maximal set. The common-
history Euler theorem then fuses the selected component graph.

The selected graph has outdegree one at every nonroot row. Along every
selected arc area strictly increases, so a directed cycle is impossible.
Every maximal parent chain terminates at a row with no parent demand, hence
at \(r\). Thus the graph is the claimed arborescence. \(\square\)

## 2. Minimal exact obstruction

For each demand \(u\), let \({\cal O}_u\) be its options. Define the conflict
hypergraph \({\cal K}\) on the disjoint union

\[
 \bigsqcup_{u\ne r}{\cal O}_u
\]

with forbidden hyperedges:

1. pairs recording different orientations at a shared endpoint row;
2. pairs using distinct starts at a shared endpoint row with cyclic distance
   at most \(d\); and
3. every inclusion-minimal set of options for which one connected component
   of the following coalescence relation fails the multiway test: two selected
   edge options are related when they use the same row-start at a common
   endpoint, and one takes the transitive closure of this relation.

Options belonging to the same child demand are placed in one colour class.

### Corollary 2.1 (independent-transversal form)

The gate is feasible if and only if \({\cal K}\) has an independent
transversal of the colour classes \((\mathcal O_u)_{u\ne r}\).

Equivalently, infeasibility has a minimal finite certificate consisting of a
nonempty demand set \(X\subseteq V\setminus\{r\}\) for which the induced
coloured conflict hypergraph on

\[
 \bigcup_{u\in X}{\cal O}_u
\]

has no independent set meeting every colour in \(X\). One may take \(X\)
inclusion-minimal; then deleting any one demand restores a transversal.

#### Proof

An independent transversal selects exactly one option of every child colour
and contains no forbidden hyperedge from Theorem 1.1. This proves
the equivalence. If the finite CSP is infeasible, choose an inclusion-minimal
set of colour classes whose induced instance remains infeasible. \(\square\)

This is the exact Hall analogue. The higher-order hyperedges are necessary:
pairwise common-history compatibility does not imply one joint class word.
The transitive closure is also necessary. If \(e,f\) coalesce at one row and
\(f,g\) coalesce at another, the edge histories force
\(H^e=H^f=H^g\); choosing two unrelated local witnesses for the two hubs
would not define one literal history on \(f\).
Counting the union of `(parent,start)`
classes is only a necessary relaxation: one option consumes starts at **both**
endpoints, and options at different rows are coupled by their shared global
orientation. Likewise, replacing the conflict hypergraph by raw cyclic capacity
\(\lfloor n/(d+1)\rfloor\) loses the geometry of which separated subsets are
simultaneously available.

## 3. A configuration formulation

Let a row configuration be

\[
 c=(\epsilon,S,(H_a)_{a\in S}),
\]

where \(\epsilon\in\{0,1\}\), \(S\subseteq\mathbb Z_n\) has pairwise
cyclic distance at least \(d+1\), and \(H_a\) is a literal word lying between
the row's forced and maximal letters at start \(a\). An option is admitted at
an endpoint when it records orientation \(\epsilon\), a start \(a\in S\),
and the opposite endpoint can use the same \(H_a\).

The gate is therefore also equivalent to choosing one configuration \(c_v\)
per row and then choosing one parent option per nonroot demand from the
options admitted at both endpoint configurations. After configurations are
fixed, the remaining condition is an ordinary choice of one nonempty option
list per child; before they are fixed, it is a coupled configuration CSP.

This formulation isolates the only honest Hall-style route. For a partial
row-configuration assignment \(c), every demand set \(X\) must retain at
least one product-compatible choice per colour in the induced option lists.
But there is no scalar neighbourhood cardinality that is both necessary and
sufficient before the configurations are known; the obstruction lives in a
coloured conflict hypergraph.

## 4. Catalan first-return recursion: exact extension gate

Write a Dyck root uniquely as

\[
 w=1u0v.
\]

Lemma 2.1 of the highest-valley four-packet theorem shows that its **specific
packet permutations** transport through a fixed context by translation or
reversal, with all exterior positions in one fixed cyclic interval. This does
not imply that an arbitrary common-history option transports when a Catalan
recursion increases \(m\): the interval length \(s=m+1-d\) also changes.

### Proposition 4.1 (fixed-parameter dihedral transport)

At fixed \((m,d)\), a dihedral relabelling of every row, cut, and literal
coordinate in a feasible jointly coalesced assignment remains feasible.

#### Proof

A dihedral relabelling carries forced and maximal sets to their images and is
an isometry of \(C_n\). It therefore preserves every containment, common
class word, coalescence equality, and start distance. \(\square\)

Primitive wrapping is not covered by Proposition 4.1. An H100 audit found
full-compatible edges at \((m,d)=(7,2)\) whose wrapped pair at \((8,2)\) has
no common history at any cuts or orientations. One example is

```text
u = 11111000110000,   v = 11011000110100;
1u0 and 1v0 are incompatible at (8,2).
```

Hence a Catalan induction must prove context stability as part of a stronger
state invariant. It cannot translate an arbitrary already feasible assignment
and then handle only cross-branch edges. A complete induction would need the
following uniform statement.

There is a useful restricted finite diagnostic. Require equality of the full
depth-\(d\) forced profile and, at the same cuts, full compatibility (or
forced-profile equality) at depth \(d+1\). At \((7,2)\), the base
equality-only graph has 3,172 edges and is connected, and every edge has some
wrapped equality witness. The one-collar containment graph has only 191 edges
and 270 components; the equality version has the same counts. Thus one collar
is context-stable at the edge-existence level there but destroys connectivity.

At \((10,3)\), by contrast, the containment one-collar graph has 91,083 edges
and one component, while the equality one-collar graph has 67,709 edges and
one component. Every one-collar edge in both graphs has a wrapped one-collar
witness after cuts are reselected. Requiring the next full profile as well
(depth \(d+2\)) leaves no transposition edge in either version. These facts
are finite diagnostics, not a monotone-in-\(d\) theorem.

The audit distinguishes two notions of transport. The **same old cut** often
does not transport: at \((10,3)\), only 47,245 containment-collar edges and
27,885 equality-collar edges have a witness whose old cut maps to a witness
after wrapping. What is preserved in the counts above is only existential
edge membership after reselecting cuts. A recursive port assignment therefore
still needs a transition rule for its boundary state; graph connectivity and
edge survival alone do not supply simultaneous inherited ports.

> **Boundary-configuration extension gate.** There is a constant \(B\),
> independent of \(m\), and a finite family of boundary configuration states
> such that every recursive branch has an assignment in a context-stable
> state after primitive wrapping or insertion, can reserve at most \(B\)
> additional start classes in the exterior interval, and the
> cross-branch common-history options can be selected using only these classes,
> compatibly at both endpoints and under reversal.

The existing residue proof supplies at least one cut per individual
highest-valley packet in its fixed ambient context; it does not supply this
finite context-stable boundary state or prove simultaneous compatibility with
inherited internal ports. The deterministic,
packet-universal, and standard-PR failures in
`MATH_OBSTRUCTION_MSW_CANONICAL_PARENT_PACKET_PORT_AND_PR_PATH_20260814.md`
show that the boundary gate cannot be discharged merely by:

- one fixed cut per packet type;
- the least available residue gap; or
- the unmodified standard PR cross-branch seam.

## 5. Exact remaining alternatives

An all-parameter proof can now take either of two forms.

1. Prove the boundary-configuration extension gate with a finite state set
   closed under the left-branch reversal and right-branch translation.
2. Exhibit an infinite family of demand sets \(X_d\) whose induced coloured
   option-conflict hypergraphs have no independent transversal. Such a family is
   the exact capacity-cut obstruction; a count of children or packet types
   alone is insufficient.

The finite \((10,3)\) certificate proves that no obstruction family can
include that complete threshold instance. No infinite obstruction or finite
recursive boundary-state construction is claimed here.
