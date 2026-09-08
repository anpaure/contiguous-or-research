# Decoration-conditioned coherent routing and the rethread/merge separation

Date: 2026-07-31  
Status: exact postrepair selection theorem and exact marginal obstruction;
constructive private-tree corollary; no all-\(m\) coherent catalogue

## 0. Verdict

The three rows of handoff item 2192 compose only after one quantifier is
fixed correctly.  One must choose a single occurrence-labelled joint
decoration \(D\), retain only coherent all-six hexagons whose six ports
belong to \(D\), and test router resilience on the resulting **nonloop
component-edge graph**.

Under the prepared private/aligned hypotheses, a fixed-decoration
component-spanning transparent list exists exactly when

\[
 \boxed{\quad
 \exists D\quad
 c(K^D_Y)\le |Y|+1
 \quad\hbox{for every router deletion }Y.
 \quad}                                             \tag{0.1}
\]

Here \(K^D_Y\) keeps only \(D\)-supported coherent component edges whose
sources still reach the sink bank after deleting \(Y\).  The forced-port
theorem gives an exact residual gap-Hall oracle for the existential choice
of \(D\).

The conditioning on the same \(D\) is essential.  Full-catalogue router
resilience and the existence of some port-compatible component tree do not
imply (0.1): a three-component, four-label fixture below has both marginal
certificates but no joint tree.

Topology is also separate.  A transparent Hamilton rethread is a loop in
the component graph and contributes nothing to (0.1).  The six transparent
rows of the repaired \(ML(7)\) cycle are all Hamilton rethreads; only four
lie on the all-six coherent face, while the other two mark none of the
hexagon ports.  Every one of the 15 splitting rows has zero common
componentwise decoration.  The item 2171 private \(m=4\) glue is a distinct
positive merge certificate.  Neither certificate can be substituted for
the other.

## 1. Prepared catalogue

Fix a postrepair middle-levels factor \(F\).  Assume the prepared
private/aligned hypotheses of item 2189:

1. every catalogue label \(t\) is a legal alternating incidence hexagon;
2. on the selected face it has one effective edge \(c_t\) in the multigraph
   on factor components;
3. its occurrence-gap effect is private or aligned with \(c_t\);
4. its linkage source \(s_t\) lies in one fixed vertex-capacitated router
   \(N\) with sink bank \(Z\);
5. the selected collar cube is component-faithful and prefix-closed; and
6. the directed reachability and protected trace-breaker rows pass.

In particular, for every decoration \(D\) admitted below, H0
order-independent superposition and H1 fixed-\(D\) transparency hold on
every component-forest subset of the restricted catalogue \({\cal E}_D\).
Coherence of isolated hexagons is not being used as a substitute for this
compatibility hypothesis.

Assume also that every catalogue hexagon is **coherent**: its three lower
external-add labels agree and its three upper external-delete labels agree.
By item 2192, whenever one decoration marks all six ports, this is necessary
and sufficient for fixed-decoration palette transparency; boundary
alternation is automatic.

Let \({\mathfrak D}(F)\) be the set of occurrence-labelled joint alternating
decorations of \(F\).  For \(D\in{\mathfrak D}(F)\), define

\[
 {\cal E}_D
 =\{t:\hbox{all six ports of }t\hbox{ belong to }D\}. \tag{1.1}
\]

Discard labels whose effective component edge is a loop.  Let \(K^D\) be
the resulting labelled multigraph on the factor components.

For a router-vertex set \(Y\), put

\[
 {\cal E}_{D,Y}
 =\{t\in{\cal E}_D:s_t\hbox{ reaches }Z\hbox{ in }N-Y\},
\qquad
 K^D_Y=(V(K^D),\{c_t:t\in{\cal E}_{D,Y}\}).          \tag{1.2}
\]

Isolated factor components are counted in \(c(K^D_Y)\).

### Theorem 1.1 (coherent-edge supply is a directed-triangle problem)

Let \(\Omega=[2m-1]\), \(m\ge3\), and let \(F\) be a spanning two-factor of
the middle-levels graph.  For

\[
 H\in{\Omega\choose m-2},\qquad d\in\Omega\setminus H,\qquad e\in H,
\]

define a loopless digraph \(\Gamma_{H,d,e}\) on
\(\Omega\setminus(H\cup\{d\})\).  Put \(x\to y\) when \(F\) contains the
three-edge factor path

\[
 H+x+d\;-\;H+x\;-\;H+x+y\;-\;(H-e)+x+y.             \tag{1.3}
\]

Then:

1. \(\Gamma_{H,d,e}\) is partial-functional: every vertex has outdegree at
   most one.  It has neither loops nor directed two-cycles.
2. Coherent all-six hexagons with common core \(H\), common external-add
   label \(d\), common external-delete label \(e\), and the displayed
   orientation are in bijection with directed three-cycles of
   \(\Gamma_{H,d,e}\).  If \(A_{H,d,e}\) is its adjacency matrix, their
   number is

   \[
   {1\over3}\operatorname {tr}(A_{H,d,e}^3).         \tag{1.4}
   \]
3. Summed over every chart,

   \[
   \sum_{H,d,e}|E(\Gamma_{H,d,e})|
      =2{2m-1\choose m-1}(m-2).                     \tag{1.5}
   \]

   Since the number of charts is

   \[
   {2m-1\choose m-2}(m+1)(m-2),
   \]

   the exact average is only \(2/(m-1)\) arcs per chart.
4. Directed three-cycles in one chart are vertex-disjoint.  Their six port
   occurrences are disjoint, and their two forced colour faces are
   mutually injective.

#### Proof

Fix \(H,d,e,x\).  The first edge in (1.3) consumes one of the two factor
edges at the lower vertex \(H+x\).  Its other upper neighbour is therefore
unique, determining \(y\); that upper vertex's other factor edge determines
whether the deleted label is \(e\).  Hence outdegree is at most one.

A directed cycle \(a\to b\to c\to a\) supplies exactly the three lower
ports \(H+a,H+b,H+c\), the three upper ports
\(H+a+b,H+b+c,H+c+a\), their alternating hex matching, and external labels
\(d,d,d\) and \(e,e,e\).  It is therefore coherent.  Reading a coherent
hexagon in its factor orientation gives the three arcs back.  Since the
digraph is loopless, every closed walk of length three is such a directed
triangle, proving (1.4).

For (1.5), choose a lower factor vertex \(L\), orient its two incident
factor edges in two ways as

\[
 U_0-L-U_1-L',
\]

and choose \(x\in L\cap L'\), of which there are \(m-2\).  Then

\[
 H=L-\{x\},\quad d=U_0-L,\quad y=U_1-L,\quad e=L-L'
\]

give one unique chart arc, and every chart arc arises uniquely this way.
This proves (1.5) and the average.

Cycles in a partial functional digraph are vertex-disjoint.  For disjoint
triples, the ports \(H+x\), \(H+x+y\) are distinct.  The forced colour
faces

\[
 H+d+\{ab,bc,ca\},\qquad (H-e)+\{a,b,c\}
\]

are also disjoint across the triples. \(\square\)

This theorem gives an exact coherent-edge generator, not a positive supply
bound.  Even a locally degree-valid directed \(m\)-cycle chart has no
directed triangle for every \(m\ge4\).  Such a chart is realizable as a
conflict-free local factor fragment by using the paths (1.3), but no claim
is made that this isolated fragment extends to a global factor with all
other required rows.  Thus degree regularity or the arc average cannot
replace a triangle-supply theorem.

The topology of a triangle is not recorded by \((H,d,e)\).  The same local
coherent hex can be a component-neutral rethread, an effective merge edge,
or a split according to the exterior path pairing.  Only its genuine
nonloop occurrences enter \(K^D\).

The absence of directed two-cycles used above is also literal.  If both
\(x\to y\) and \(y\to x\) existed, the upper vertex \(H+x+y\) would need
factor edges to the three distinct lower vertices

\[
 H+x,\qquad H+y,\qquad (H-e)+x+y,
\]

contradicting degree two.

### Corollary 1.2 (exact supply and port-packing bounds)

Let \(Q={2m-1\choose m-1}\).  The total number \(R\) of coherent all-six
hexagons in \(F\) satisfies

\[
 R\le {2Q(m-2)\over3}
    ={(m+1)(m-2)\operatorname {Cat}_m\over3}.        \tag{1.6}
\]

Every fixed lower or upper factor vertex lies in at most \(2(m-2)\)
coherent hexagons.  Consequently the closed port-conflict neighbourhood of
one coherent hexagon has size at most

\[
 B_m=1+6(2(m-2)-1)=12m-29.                          \tag{1.7}
\]

Therefore:

1. every \(R_0\)-element coherent candidate bank has a pairwise
   port-disjoint subbank of size at least
   \(\lceil R_0/B_m\rceil\);
2. \(s\) labelled requests have a greedy port-disjoint assignment whenever
   every request has more than \((s-1)B_m\) eligible candidates; and
3. within one fixed chart, distinct triangles are already port-disjoint, so
   assignment of requested interface types to eligible chart triangles is
   governed exactly by ordinary bipartite Hall.

#### Proof

The upper bound (1.6) follows because every directed triangle consumes three
of the arcs in (1.5).  For a fixed port, choose which of its two factor edges
is external and then one of the \(m-2\) retained core positions; the chart
arc and any containing directed triangle are forced.  This gives the port
load \(2(m-2)\), and the union bound over six ports gives (1.7).

Greedily choose a triangle and discard its closed conflict neighbourhood.
This proves item 1.  At the \(j\)-th request, the earlier choices have
discarded at most \(jB_m\) of its candidates, proving item 2.  Item 3 follows
from the same-chart disjointness in Theorem 1.1. \(\square\)

Across different charts the exact assignment object is instead the
seven-uniform hypergraph whose edge consists of one request and the six
physical ports.  Ordinary candidate Hall need not control these overlaps.

If a fraction \(\theta\) of all chart arcs belongs to coherent triangles of
one desired topology class, that class has

\[
 {\theta(m+1)(m-2)\operatorname {Cat}_m\over3}
\]

candidates and hence a port-disjoint bank of at least its quotient by
\(B_m\), rounded up.  In particular, a Catalan-scale port bank follows from

\[
 \theta\ge {3(12m-29)\over(m+1)(m-2)}.              \tag{1.8}
\]

This is only physical port supply.  It says nothing about one common
decoration, safe topology, router resilience or downstream protection.

## 2. Exact conditioned resilience theorem

### Theorem 2.1

Under the prepared hypotheses, the following are equivalent.

1. There are one joint decoration \(D\), a component-spanning set of
   coherent all-six toggles transparent for \(D\), vertex-disjoint linkage
   routes for its labels, and an executable ordered transparent gluing list.
2. There is a decoration \(D\in{\mathfrak D}(F)\) such that

   \[
   c(K^D_Y)\le |Y|+1
   \qquad(Y\subseteq V(N)).                          \tag{2.1}
   \]
3. There is a decoration \(D\in{\mathfrak D}(F)\) such that, for every
   factor-component partition \(\Pi\) and every router deletion \(Y\),

   \[
   |\delta_{K^D_Y}(\Pi)|
      \ge |\Pi|-1-|Y|.                              \tag{2.2}
   \]

#### Proof

Fix \(D\).  Coherence and the all-six condition make every label in
\({\cal E}_D\) locally \(D\)-transparent, with no remaining local palette
choice.  The prepared private/aligned hypotheses put their effective
component edges in the graphic matroid and their sources in the fixed
linkage gammoid.  Item 2192's router-resilience theorem says that these two
matroids have a common component-spanning tree exactly when (2.1) holds.
Item 2189 then makes every ordering of such a tree an executable
fixed-\(D\) transparent list.  This proves \(1\Longleftrightarrow2\).

For fixed \(D,Y\), every \(p\)-block partition satisfies

\[
 |\delta_{K^D_Y}(\Pi)|\ge p-c(K^D_Y).
\]

Thus (2.1) implies (2.2).  Conversely, choose \(\Pi\) to be the component
partition of \(K^D_Y\).  Its crossing set is empty, so (2.2) gives
\(c(K^D_Y)\le|Y|+1\). \(\square\)

The theorem is an exact existential criterion.  It is not a polynomial-time
claim and does not supply the decoration or coherent edges.

## 3. Forced-port Hall is the exact decoration oracle

Fix a proposed coherent label set \(S\).  Let \(P_A(S)\) and \(P_B(S)\) be
its forced upper- and lower-shore port occurrences on the repaired cycle.

### Theorem 3.1

There is a joint alternating decoration containing all ports of \(S\) if
and only if there is an upper occurrence transversal \(I\supseteq P_A(S)\)
such that:

1. the forced upper colours are distinct;
2. the forced lower colours are distinct;
3. distinct forced lower ports occupy distinct cyclic \(I\)-gaps; and
4. after deleting those forced gaps and forced lower colours, the residual
   gap--lower-colour graph satisfies

   \[
   |N_{\rm res}(X)|\ge |X|
   \quad\hbox{for every residual gap set }X.         \tag{3.1}
   \]

#### Proof

This is the occurrence-labelled forced-port theorem of item 2192.
Necessity follows because a joint decoration selects one lower occurrence
in each cyclic upper-transversal gap and uses every lower colour once.
Conversely, a perfect matching of the residual graph, together with the
forced occurrences, selects exactly one lower occurrence per gap and every
lower colour once. \(\square\)

For construction one may therefore choose a coherent component-tree
candidate \(S\), apply Theorem 3.1, obtain \(D\), enlarge to the full
\({\cal E}_D\), and finally test (2.1).  The last enlargement matters:
router resilience may select a different \(D\)-supported tree from the
initial seed \(S\).

### Corollary 3.2 (two checkable residual-Hall certificates)

Let \(f\) forced gaps and \(f\) forced colours be deleted.

1. If the predeletion gap graph obeys

   \[
   |N(X)|\ge |X|+f
   \]

   for every set \(X\) of gaps which survives the forcing, then the residual
   graph satisfies (3.1).
2. In the residual balanced bipartite graph, it is enough that the minimum
   gap degree is positive and at least the maximum colour degree.

Indeed, deleting \(f\) colours removes at most \(f\) neighbours from any
surviving \(X\).  For the second claim, if the two degrees are
\(\delta_L,\Delta_R\), then

\[
 \delta_L|X|\le e(X,N(X))\le\Delta_R|N(X)|,
\]

so \(\delta_L\ge\Delta_R>0\) implies Hall.

Colour injectivity and global turn surjectivity alone are insufficient.
With two gaps \(G_1,G_2\) and colours \(\alpha,\beta\), force an
\(\alpha\)-occurrence in \(G_1\), also place a \(\beta\)-occurrence there,
and let \(G_2\) contain only \(\alpha\)-occurrences.  After deleting
\((G_1,\alpha)\), the residual gap \(G_2\) has no \(\beta\)-edge.

## 4. Constructive private-tree corollary

### Corollary 4.1

Suppose there is a set \(T\) of coherent nonloop labels such that:

1. the component edges \(\{c_t:t\in T\}\) form a spanning tree;
2. Theorem 3.1 extends all six ports of every \(t\in T\) to one decoration
   \(D\);
3. the sources \(\{s_t:t\in T\}\) have mutually vertex-disjoint paths to
   distinct sinks in \(N\); and
4. all prepared private/aligned, reachability and trace-breaker rows hold.

Then every tree order is an executable fixed-\(D\) transparent
component-spanning list.

#### Proof

The disjoint router paths show directly that \(T\) is independent in the
linkage gammoid.  Equivalently, deleting \(Y\) router vertices destroys at
most \(|Y|\) of those paths.  The surviving edges of the spanning tree have
at most \(|Y|+1\) components, and \(K^D_Y\) contains them.  Hence (2.1)
holds.  Apply Theorem 2.1. \(\square\)

This is the cleanest positive catalogue target: one coherent component tree,
one residual forced-port Hall certificate, and one private linkage routing.
The exact resilience theorem permits much more sharing than this corollary.

## 5. Marginal certificates do not compose

The same-decoration quantifier in Theorem 2.1 cannot be removed.

### Proposition 5.1 (three-component/four-label obstruction)

There is an abstract support/router interface with three factor components and
four coherent labels such that:

1. the full coherent catalogue satisfies router resilience;
2. every label is contained in some valid decoration;
3. one decoration contains a component-spanning coherent tree; but
4. no decoration-conditioned catalogue has a common
   graphic--linkage spanning tree.

#### Construction and proof

Let the component vertices be \(U,V,W\), and use four labels

\[
 a=UV,\qquad c=UV,\qquad b=VW,\qquad d=UW.           \tag{5.1}
\]

The router has two unit sinks \(z_1,z_2\).  Sources \(a,c,d\) can reach only
\(z_1\), while source \(b\) can reach only \(z_2\).  Thus the full catalogue
has a common graphic--linkage spanning tree, for example \(\{a,b\}\), and
passes the resilience criterion.

Now use a rich fixed upper-transversal gap system.  Put one of \(b\)'s
forced lower ports in each of three gaps \(G_1,G_2,G_3\).  Put an additional
forced port of \(a\) in \(G_1\), of \(c\) in \(G_2\), and of \(d\) in
\(G_3\).  Place every remaining forced port in a mutually private gap with
a distinct colour, and make the residual gap graph complete.

Every spanning tree containing \(b\) must use one of \(a,c,d\), and hence
has two forced lower ports in \(G_1,G_2\), or \(G_3\).  It fails the
at-most-one forced-port row before residual Hall.  Conversely,
\(\{a,d\}\) and \(\{c,d\}\) are port-compatible graphic spanning trees and
their residual gap graphs are complete, but both selected sources can reach
only the single sink \(z_1\).  They fail the linkage row.

Thus the full catalogue is router-resilient and a port-compatible coherent
tree exists, yet no one tree satisfies both rows. \(\square\)

This is an abstract quantifier obstruction, not a claimed physical
middle-levels fixture.  It proves that coherent-edge supply, forced-port
Hall and router resilience must be certified on one correlated label set.

## 6. Transparent rethreads are not merge certificates

At a fixed factor state and decoration \(D\), a \(D\)-transparent
Hamilton-to-Hamilton toggle preserves the component partition.  Its
effective edge in the component multigraph is a loop.  Loops cross no
component partition and cannot improve (2.1) or contribute to a spanning
tree.

A component-merging toggle is different: on the prepared single-effective-
edge face it contributes a nonloop \(c_t\), and it must pass the same
all-six coherence, forced-port and router rows on the factor state where it
will actually be used.

### Lemma 6.1 (safe rethread-before-merge composition)

Let \(R\) be a family of fixed-\(D\) transparent component-neutral
rethreads, and let \({\cal G}\) be a prepared coherent nonloop merge
catalogue.  Suppose:

1. the combined toggles form one legal static Boolean cube;
2. no rethread changes an old hex edge or any of the six external factor
   edges which define the coherent labels of a member of \({\cal G}\);
3. rethreads preserve the factor-component partition; and
4. router, gap-private and trace-guard resources of the two families are
   disjoint or explicitly capacity-checked.

Then applying any subset of \(R\) preserves \(D\), the coherent labels and
component edges of \({\cal G}\), its forced port set, and every graph
\(K^D_Y\).  Consequently Theorem 2.1 holds after the rethreads if and only
if it held before them.

#### Proof

Fixed-\(D\) transparency preserves the occurrence-labelled decoration.
The closed-star disjointness in item 2 preserves all six external labels and
the alternating old matching of every merge hex.  Item 3 preserves the
component endpoints of its effective edge, and item 4 preserves its router
and prepared physical state.  Hence (1.1)--(1.2) are literally unchanged.
\(\square\)

Without this static-cube or an explicit occurrence-labelled transport
isomorphism, a rethread may change the later hex adjacencies, cyclic gaps or
router state.  The merge catalogue must then be rebuilt; transparency of
the rethread alone gives no inheritance theorem.

## 7. Exact finite calibration

For the repaired \(ML(7)\) Hamilton cycle:

* 31 alternating incidence hexagons exist;
* 16 toggles have Hamilton output;
* six Hamilton toggles have at least one common decoration and are
  transparent rethreads;
* four of those six mark all six ports and satisfy the coherent external
  label equalities;
* the other two mark none of the six ports; and
* all 15 toggles producing two or three components have zero common
  componentwise decorations.

Thus this cycle supplies a useful rethread neighbourhood but no
fixed-decoration nonloop merge edge.

At \(m=3\), each of the five splitting hexagons has 12 common
componentwise decorations, so its inverse is a genuine merge calibration.
Independently, item 2171 supplies the positive standard \(m=4\) prepared
private merge path

\[
 [18]-g-[20]-g-[24].
\]

These are distinct factors and distinct certificates.  A recursive proof
still needs either Lemma 6.1 on one common factor or a separate transport
theorem carrying the merge catalogue through the repaired entrance.

## 8. Sharp all-\(m\) supply target

The postrepair catalogue gate is now exactly:

> construct a repaired entrance \(F_m\), one occurrence-labelled joint
> decoration \(D_m\), and enough coherent **nonloop** all-six hexagons that
> the conditioned graphs \(K^{D_m}_Y\) satisfy
> \(c(K^{D_m}_Y)\le|Y|+1\) for every router deletion \(Y\).

Equivalently, the stronger constructive target is the private-tree package
of Corollary 4.1.  A preliminary transparent rethread packet is allowed,
but the merge catalogue must survive by Lemma 6.1 or be reconstructed and
retested afterwards.

This closes the prepared palette/SDR/router implication.  It does not
supply residence redistribution, deeper-shadow preservation,
socket/primitive voltage, Pascal reachability, or the common-\(Q\)
compiler.  No all-\(m\) coherent-edge supply and no coefficient-one theorem
is claimed.

## 9. Authoritative dependencies

This theorem uses:

* MATH_THEOREM_CATALAN_TRANSPARENT_ROUTER_RESILIENCE_CRITERION_20260731.md;
* MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md;
* MATH_THEOREM_CATALAN_FORCED_PORT_GAP_HALL_20260731.md;
* MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md;
* MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md;
* MATH_THEOREM_CATALAN_LEAF_PEELABLE_TRANSPARENT_GLUING_STATE_20260731.md.
