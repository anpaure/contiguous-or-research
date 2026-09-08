# Catalan colour incidence, balanced paths, and diamond-tight enumerations

Date: 2026-07-31  
Status: exact equivalences, finite audits, and an all-dimension abstract
forest; the coherent physical construction remains open

## 1. The incidence multigraph

Fix \(m\ge2\), and let

\[
 P=(T_0,T_1,\ldots,T_{M-1},T_0)
\]

be a Hamilton cycle of the Johnson graph \(J(2m,m)\).  For its edge
\(e_i=T_iT_{i+1}\), write

\[
 \ell(e_i)=T_i\cap T_{i+1}\in\binom{[2m]}{m-1},\qquad
 u(e_i)=T_i\cup T_{i+1}\in\binom{[2m]}{m+1}.
\]

Put

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

Define the occurrence-labelled bipartite multigraph \(G(P)\) as follows.
Its left vertices are the \(N\) lower colours
\(\binom{[2m]}{m-1}\), its right vertices are the \(N\) upper colours
\(\binom{[2m]}{m+1}\), and every occurrence \(e_i\) is one graph edge

\[
                 \ell(e_i)\;---\;u(e_i).                 \tag{1.1}
\]

Parallel graph edges are retained as different occurrences.

Call \(Q\subseteq E(P)\) a **common colour transversal** if both maps

\[
 e\mapsto\ell(e),\qquad e\mapsto u(e)
\]

restrict to bijections from \(Q\) onto their respective colour layers.

### Theorem 1.1 (common-transversal equivalence)

Common colour transversals of \(P\) are exactly the perfect matchings of
\(G(P)\), occurrence for occurrence.  If \(A_P=(a_{L,U})\) is the
biadjacency matrix whose entries count physical occurrences, then their
number is

\[
                         \operatorname {per} A_P.        \tag{1.2}
\]

#### Proof

A perfect matching selects one occurrence at every lower vertex and one
occurrence at every upper vertex.  This is precisely the two bijection
conditions in the definition.  The converse is the same statement read
backwards.  In the permanent expansion, \(a_{L,U}\) records the choice of
one of the parallel physical occurrences with colours \((L,U)\), proving
the counting assertion. \(\square\)

For an exact determinant certificate, give each physical occurrence \(e\)
its own indeterminate \(x_e\) and replace \(a_{L,U}\) by

\[
       \mathsf E(P)_{L,U}
          =\sum_{e:\,\ell(e)=L,\,u(e)=U}x_e.            \tag{1.3}
\]

Then \(\det\mathsf E(P)\) is a nonzero polynomial if and only if a common
transversal exists: different occurrence matchings have different
squarefree monomials.  The unsigned integer determinant \(\det A_P\) may
cancel and is only a sufficient certificate when nonzero.

This elementary observation packages the entire post-insertion palette
gate into one graph.  It is stronger than two separate Hall tests because
the same middle edge must serve both colours.

## 2. The degree-two case is a path-and-cycle theorem

Assume first only that every occurrence degree of \(G(P)\) is at most two.
Every component is an isolated vertex, a path, or an even cycle; two
parallel physical occurrences form the allowed two-cycle.  In the
Catalan floor case the two colour-load profiles are

\[
                         1^{N-K}2^K.                       \tag{2.1}
\]

There are then no isolated vertices and the maximum-degree-two hypothesis
holds.  The multiplicity qualification is essential: bounding only the
number of distinct neighbours is not enough.

Call a bipartite path **balanced** if it has equally many vertices on its
two shores.  Equivalently, its two endpoints lie on opposite shores, or
its number of graph edges is odd.

### Theorem 2.1 (balanced-component criterion)

Under occurrence degree at most two:

1. \(G(P)\) has a perfect matching if and only if every component is
   balanced.  Equivalently, there is no isolated vertex and every
   nontrivial path has endpoints on opposite shores.
2. If this holds and \(c\) is the number of cycle components, then
   \(G(P)\) has exactly \(2^c\) perfect matchings.
3. In particular, the common colour transversal is unique if and only if
   \(G(P)\) is a disjoint union of balanced paths.

#### Proof

An even cycle has its two alternating perfect matchings.  A path has a
perfect matching precisely when its endpoints lie on opposite shores;
then the matching is forced by either leaf and is unique.  Components are
independent, so their matching counts multiply. \(\square\)

Thus the matching gate is not an opaque global Hall condition in the
floor case.  Its complete obstruction is an unbalanced path.  A balanced
linear forest is also literally leaf-peelable: successively match and
delete the two endpoints of each path.

### Corollary 2.2 (ordinary determinant and signing)

Suppose the degree-two graph is feasible.  A balanced path block has
determinant of absolute value one.  A cycle of length \(2q\), with a
parallel two-cycle interpreted as \(q=1\), has

\[
 |\det A_{C_{2q}}|=
 \begin{cases}
 2,&q\text{ odd},\\
 0,&q\text{ even}.
 \end{cases}                                             \tag{2.2}
\]

Consequently the ordinary determinant is nonzero precisely when no cycle
has length divisible by four, and then its absolute value is \(2^c\).
For every feasible degree-two graph one can instead sign one occurrence
on each cancelling \(C_{4t}\); the signed determinant then has absolute
value \(2^c\).  In particular a balanced path forest has determinant
\(\pm1\), while a four-cycle has two perfect matchings and ordinary
determinant zero.

#### Proof

After alternating row and column order, a \(2q\)-cycle block is \(I+S\),
where \(S\) is a cyclic permutation matrix.  Hence
\(\det(I+S)=1-(-1)^q\).  Flipping one occurrence reverses the relative
sign of its two alternating determinant terms.  Path blocks have one
term, and component determinants multiply. \(\square\)

## 3. Relation to the directed Catalan split

Now suppose \(P\) comes from a saturating cycle

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0
\]

by injecting each omitted middle set \(X\) into a distinct block
\(C_i,U_i,C_{i+1}\).  An unmatched block contributes the sole edge
\(C_iC_{i+1}\); a matched block contributes the incoming and outgoing
edges

\[
                    C_iX,\qquad XC_{i+1}.                 \tag{3.1}
\]

The upper colour of every edge in that block is \(U_i\).  Consequently,
every perfect matching of \(G(P)\) chooses the sole edge in every
unmatched block and exactly one of the two edges in every matched block.
Write \(H\subsetneq\mathbb Z_N\) for the hosted block indices and \(X_i\)
for the omitted set hosted at \(i\).

### Theorem 3.1 (orientation-exact repair criterion)

For a fixed injection of omitted sets into blocks:

1. a perfect matching of \(G(P)\) is exactly a choice of one retained
   edge per block whose lower colours enumerate
   \(\binom{[2m]}{m-1}\);
2. it is an all-outgoing directed Catalan repair exactly when it chooses
   \(X_iC_{i+1}\) in every matched block;
3. it is an all-incoming repair exactly when it chooses \(C_iX_i\) in every
   matched block.

In either uniform case the opposite cut seams are automatically distinct,
because different hosted blocks cut different consistently oriented
endpoints.  A mixed perfect matching still solves the common-colour
problem, but its cut endpoints require the separate port-injectivity test:
two adjacent hosted blocks may cut their shared \(C_i\).

#### Proof

At an upper vertex \(U_i\), the incident occurrences are exactly the one
or two edges of its block.  The upper-perfect-matching condition therefore
chooses one retained edge in that block.  The lower-perfect-matching
condition says that the retained intersections enumerate the lower layer.
This proves (1); (2) and (3) are the definitions of the two directed
choices.  Under a uniform orientation, the map from hosted block indices
to their cut endpoint indices is a fixed cyclic shift, hence injective.
\(\square\)

Equivalently, define the canonical outgoing set

\[
 T_{\to}=\{C_iC_{i+1}:i\notin H\}
          \sqcup\{X_iC_{i+1}:i\in H\}.                  \tag{3.2}
\]

Uniform outgoing repair exists if and only if \(T_{\to}\) itself is a
perfect matching, or, equivalently,

\[
 \{C_i\cap C_{i+1}:i\notin H\}
 \sqcup\{X_i\cap C_{i+1}:i\in H\}
       =\binom{[2m]}{m-1}                               \tag{3.3}
\]

as a literal multiplicity-one identity.  In the degree-two component
coordinate, this says that the unique matching of every balanced path is
the distinguished outgoing phase, and that on every cycle the
distinguished outgoing edges form one of its two alternating phases.
There is at most one uniformly outgoing matching because the upper-block
choices already determine it.

### Theorem 3.2 (exact cut-seam criterion)

For a common transversal put \(\varepsilon_i=0\) when it retains the
outgoing edge \(X_iC_{i+1}\), and \(\varepsilon_i=1\) when it retains the
incoming edge \(C_iX_i\).  The opposite cut seam is respectively \(C_i\)
or \(C_{i+1}\).  These cut seams are pairwise distinct if and only if no
two cyclically consecutive hosted blocks have orientation pattern

\[
                         \varepsilon_i\varepsilon_{i+1}=10.  \tag{3.4}
\]

Since \(H\ne\mathbb Z_N\), this is equivalent to the word on every maximal
cyclic hosted run having form \(0^*1^*\).  Uniform outgoing and uniform
incoming are the two constant special cases.

#### Proof

The distinct \(C_i\) can collide as cut seams only at the common boundary
of adjacent hosted blocks.  Block \(i\) cuts \(C_{i+1}\) exactly for bit
one, while block \(i+1\) cuts \(C_{i+1}\) exactly for bit zero.  This is
the forbidden descent \(10\), and a binary word with no descent has form
\(0^*1^*\). \(\square\)

This separates two facts that must not be conflated:

* a balanced incidence forest proves a unique retained-edge choice;
* the recursive two-rail construction additionally needs that forced
  choice to have coherent orientation (or, more generally, distinct cut
  ports).

The negative and positive \(m=3\) fixtures below both have balanced
incidence forests.  Only the positive one has uniformly outgoing forced
edges.

### Lemma 3.3 (the lower floor is the unused-colour condition)

Suppose \(Q\) is a common transversal.  The lower load profile of all
\(M=N+K\) edges of \(P\) is (2.1) if and only if the \(K\) lower colours
of the unselected edges \(E(P)\setminus Q\) are pairwise distinct.

#### Proof

The selected edges already contribute one occurrence of every lower
colour.  The remaining \(K\) occurrences therefore create the profile
\(1^{N-K}2^K\) exactly when they hit \(K\) distinct colours. \(\square\)

In the directed notation these unselected colours are the discarded split
colours \(\alpha_X\).  This recovers the floor condition in
`MATH_THEOREM_CATALAN_DIRECTED_DEFECT_TRANSPORT_20260731.md`.

## 4. Exact diamond-tight enumeration

Assume only that the upper load profile is cap-two,
\(1^{N-K}2^K\), and let \(Q\) be a common colour transversal.  Define the
**upper complement transversal** \(Q^\uparrow\) blockwise:

* at an upper colour of degree one, take the same sole occurrence as
  \(Q\);
* at an upper colour of degree two, take the other occurrence.

Then

\[
 |Q|=|Q^\uparrow|=N,\qquad
 Q\cup Q^\uparrow=E(P),\qquad
 |Q\cap Q^\uparrow|=N-K.                                  \tag{4.1}
\]

Call a three-level enumeration **rigid cap-two \(P\)-respecting** if its
rank-\(m\) projection is \(P\), every degree-one upper block inserts both
its lower intersection and its upper union on the sole edge, and every
degree-two upper block inserts the lower vertex on one split edge and the
upper vertex on the other.  These block rules are part of the definition;
a generic tight covering pair need not obey them.

### Theorem 4.1 (rigid diamondization equivalence)

Replace every directed middle edge \(A,B\) of \(P\) locally as follows:

\[
\begin{array}{c|c}
 e\in Q\setminus Q^\uparrow&A,\ A\cap B,\ B,\\
 e\in Q^\uparrow\setminus Q&A,\ A\cup B,\ B,\\
 e\in Q\cap Q^\uparrow&A,\ A\cap B,\ A\cup B,\ B.
\end{array}                                                \tag{4.2}
\]

The resulting cyclic listing is a rigid cap-two \(P\)-respecting tight
enumeration of all vertices in
the three levels

\[
 \binom{[2m]}{m-1}\cup\binom{[2m]}m\cup\binom{[2m]}{m+1}.
\]

It has total flip length \(4N\).  Conversely, the lower-marked edges of
every rigid cap-two \(P\)-respecting diamond-tight enumeration form a
common transversal, hence a perfect matching of \(G(P)\).  This is a
bijection, up to the two local orders of the two inserted vertices in each
diamond.

#### Proof

The middle vertices occur once because their cyclic order is \(P\).
The intersections on \(Q\) occur once because \(Q\) is a lower-colour
transversal.  The unions on \(Q^\uparrow\) occur once because
\(Q^\uparrow\) selects one occurrence at every upper colour.

There are \(K\) lower-only edges, \(K\) upper-only edges, and \(N-K\)
diamond edges.  The first two types cost two flips each; a diamond costs
\(1+2+1=4\).  Hence the total is

\[
                  2K+2K+4(N-K)=4N.                        \tag{4.3}
\]

The three-level vertex count is \(M+2N\), and its bipartition imbalance is
\(2N-M\), so its tight lower bound is

\[
                 (M+2N)+(2N-M)=4N.                        \tag{4.4}
\]

Thus (4.2) is tight.  In the converse normal form, the edges carrying
lower vertices select every lower colour once.  They also contain the
sole edge of every degree-one upper block and exactly one edge of every
degree-two upper block, so they select every upper colour once.  They are
therefore a common transversal. \(\square\)

The blockwise opposite is load-bearing.  If one uses the same common
transversal \(Q\) for both boundary levels, then \(K\) middle edges carry
no insertion and \(N\) carry two; the cyclic distance is
\(4N+2K\), not the tight value \(4N\).  Conversely, a generic tight pair
of lower and upper transversals need not make its lower set an upper
transversal unless the rigid block rule is imposed.

This is the exact common-refinement problem left open by the separate
published existence theorems for cap-two middle cycles and tight
enumerations.  A generic three-level tight enumeration need not have the
local diamond form (4.2), and a generic cap-two cycle need not have a
common transversal.

## 5. The abstract all-\(m\) forest exists

Let \(B_m\) be the bipartite inclusion graph between
\(\binom{[2m]}{m-1}\) and \(\binom{[2m]}{m+1}\).  Both shores have
\[
             N=\binom{2m}{m+1}=m\operatorname {Cat}_m=mK
\]
vertices, and \(B_m\) is
\[
                         d=\binom{m+1}{2}
\]
regular.  Every edge \(L\subset U\) is the colour pair of the unique
physical Johnson edge
\[
                   \psi(L,U)=(L+a)(L+b),
             \qquad U\setminus L=\{a,b\}.                \tag{5.1}
\]

### Theorem 5.1 (all-dimensional abstract forest)

For every \(m\ge2\), \(B_m\) contains a spanning subgraph \(H_m\) with
exact shore profiles \(1^{N-K}2^K\) such that:

1. \(H_m\) is a disjoint union of balanced paths;
2. it has a unique perfect matching \(M_0\);
3. its biadjacency determinant is \(\pm1\).

One may take \(M_0\) to be the two-rank matching supplied by a fixed BTK
symmetric-chain decomposition.

The quantifiers are important.  The perfect inclusion matching is
\[
 \sigma=M_0:\binom{[2m]}{m-1}\longrightarrow
                 \binom{[2m]}{m+1}.
\]
The degree-\(\{1,2\}\) forest is the larger colour graph
\(H_m=\operatorname{graph}(\sigma)\cup S\), with \(|S|=K\); it is not
\(\sigma\) alone and is not the projection of a prechosen repair core.
Nothing in Theorem 5.1 asserts that the \(N\) Johnson edges
\(\Psi(\operatorname{graph}\sigma)\) form a spanning \(K\)-path forest on
rank \(m\).  That would be an additional physical theorem: because
\(M=N+K\), a spanning linear forest with those \(N\) edges would indeed
have exactly \(K\) components.

#### Proof

Choose a perfect matching \(M_0\) of \(B_m\); BTK supplies one by matching
each rank-\((m-1)\) set to the rank-\((m+1)\) set two steps above it in
its symmetric chain.  The graph \(B_m-M_0\) is \((d-1)\)-regular and
bipartite, hence has a perfect matching \(M_1\).

The graph \(M_0\cup M_1\) is a disjoint union of alternating cycles.  If
there are \(c\) cycles, then \(c\le N/2\), because every cycle contains at
least two \(M_1\)-edges.  Since
\[
                         K=N/m\le N/2\le N-c,
\]
one can choose exactly \(K\) edges \(S\subset M_1\) while omitting at
least one \(M_1\)-edge from every alternating cycle: the per-cycle
capacities \(0,\ldots,r_j-1\) have total \(N-c\ge K\), so a greedy fill
reaches every integer through \(K\).  Put
\[
                              H_m=M_0\cup S.              \tag{5.2}
\]
The matching \(M_0\) gives every vertex degree one, and the matching
\(S\) raises exactly \(K\) vertices on each shore to degree two, proving
the profile.  Breaking every alternating cycle at its omitted
\(M_1\)-edges leaves paths of the form
\[
                         M_0,S,M_0,\ldots,S,M_0.
\]
They have odd length, opposite-shore endpoints, and unique matching
\(M_0\).  Theorem 2.1 and Corollary 2.2 finish the proof. \(\square\)

Thus there is no abstract Hall, forest, permanent, or determinant
obstruction in any dimension.  The obstruction is the simultaneous
physical realization.

### Theorem 5.2 (exact physical-lift and orientation obstruction)

For any inclusion subgraph \(H\subseteq B_m\), let \(F(H)\) be the graph
on all rank-\(m\) sets whose physical edges are the unique lifts
\(\psi(L,U)\) of the edges of \(H\).

1. \(H=G(P)\) for a middle Hamilton cycle \(P\) if and only if \(F(H)\)
   is a spanning connected two-regular graph.
2. Suppose additionally that every upper vertex of \(H\) has degree one
   or two.  Such a \(P\) is obtained from a cap-two saturating cycle by
   inserting one omitted middle set in every degree-two upper block if and
   only if, for every degree-two upper colour \(U\), its two lifted
   Johnson edges share a middle endpoint \(X_U\).
3. For the forest \(H_m=M_0\cup S\) of Theorem 5.1 satisfying (1) and
   (2), the unique common transversal \(M_0\) is uniformly outgoing if and
   only if the cycle \(F(H_m)\) has an orientation in which, at every
   \(X_U\), the \(M_0\)-edge is directed away from \(X_U\).  Equivalently,
   all doubled-upper blocks have one common cyclic sign.

#### Proof

The lift (5.1) is a bijection between inclusion pairs and physical
Johnson edges, so (1) is immediate.  For (2), the two occurrences of a
split upper block are \(C_iX_U\) and \(X_UC_{i+1}\), hence share \(X_U\).
Conversely, in a Hamilton \(F(H)\), the two edges sharing \(X_U\) are its
two cycle edges.  Different doubled upper colours have different
\(X_U\), because both cycle edges at such a vertex have that same upper
colour; for the same reason two different \(X_U\) cannot be adjacent.
Delete all such \(X_U\) and contract each resulting two-edge
segment.  The remaining \(N\) middle vertices alternate with the \(N\)
upper colours, once each, giving the saturating cycle and its cap-two
insertion.  Finally, in each doubled block \(M_0\) chooses exactly one of
the two split edges.  It is the outgoing edge in a chosen cycle
orientation exactly under the sign condition in (3). \(\square\)

### Proposition 5.3 (the missing \(K\)-path gate)

If \(H_m=\operatorname{graph}(\sigma)\cup S\) has Hamilton lift, deleting
the \(K\) lifted \(S\)-edges leaves
\(\Psi(\operatorname{graph}\sigma)\), a spanning linear forest with
exactly \(K\) path components.  Conversely the Hamilton-lift condition is
equivalent to this \(K\)-path property together with the requirement that
the lifted \(S\)-edges reconnect those paths cyclically.

This property is not supplied by BTK.  Under the standard BTK scan, let
\[
                         E_m=\{0,2,\ldots,2m-2\}.
\]
For \(L_j=E_m\setminus\{2j\}\), the two coordinates added by \(\sigma\)
are \(\{0,2m-1\}\) for \(j=0\), and
\(\{2j-1,2j\}\) for \(j\ge1\).  Therefore every one of the \(m\) lifted
edges \(\psi(L_j,\sigma(L_j))\) is incident with \(E_m\), so
\[
          \deg_{\Psi(\operatorname{graph}\sigma)}(E_m)=m. \tag{5.3}
\]
For every \(m\ge3\) this standard BTK matching is physically branched and
cannot be repaired into a Hamilton cycle merely by adding \(S\)-edges.
A different perfect inclusion matching \(\sigma\) is required.

The three exact failure modes are therefore:

* \(\Psi(\operatorname{graph}\sigma)\) is not a spanning \(K\)-path
  forest, or the \(S\)-edges fail to reconnect those paths cyclically;
* a doubled upper colour lifts to two disjoint Johnson edges rather than
  a shared inserted facet;
* the forced \(M_0\)-edges have mixed cyclic signs.

The \(m=3\) mixed fixture below realizes the third obstruction.  A generic
GMM three-level tight enumeration supplies the correct flip budget but may
violate the rigid block rule of Theorem 4.1, so BTK/GMM input alone does
not remove these physical conditions.  An all-\(m\) construction would
have to choose \(M_0,M_1,S\) so that all three lift conditions hold; that
choice remains open.

There is nevertheless an exact abstract ear induction.  If the old forest
is retained and new shore pairs are added either as isolated matching
edges or as two-vertex ears attached to old path endpoints, then the
number of attached ears forced in the step \(m\to m+1\) is

\[
 a=K_{m+1}-K_m=\frac{3m}{m+2}K_m,                       \tag{5.4}
\]

and the number of isolated pairs is

\[
 b=mK_{m+1}-(m-1)K_m
   =\frac{3m^2+m+2}{m+2}K_m.                            \tag{5.5}
\]

Each attached ear raises the number of degree-two vertices by one on each
shore and exposes a determinant pivot.  Thus these counts are necessary
and sufficient for this restricted abstract recursion.  For
\(m=3\to4\) they are \(a=9,b=32\), so a one-ear recursion is short by
eight attached ears.  This is not a physical no-go: the labels of the
bulk ears must still be chosen to pass Theorem 5.2.  Full details and the
\(m=2,3,4\) replay are frozen in
MATH_THEOREM_CATALAN_ABSTRACT_COLOUR_FOREST_AND_PHYSICAL_LIFT_GATE_20260731.md.

## 6. Independent \(m=3,m=4\) replay and scope

The dependency-free audits

* scratch/audit_catalan_colour_incidence_graph_20260731.py, and
* scratch/audit_catalan_colour_incidence_graph_m3_m4_20260731.py

reconstruct the physical occurrence graphs, enumerate every finite host
and orientation case in the listed \(m=3\) fibres, and replay the
determinant, cut-seam, and rigid-diamond statements.

* The positive \(m=3\) fixture has profiles \(1^{10}2^5\) on both shores.
  Its graph is ten balanced paths, its permanent is one, its determinant
  is \(-1\), and the unique matching is uniformly outgoing.  The rigid
  diamond enumeration has all \(15+20+15\) vertices and distance \(60\).
* The mixed \(m=3\) fixture has the same floor profiles and a ten-path
  forest with determinant \(+1\).  Its unique signature is
  outgoing, outgoing, incoming, incoming, incoming.  All five cut seams
  are nevertheless distinct, proving that Theorem 3.2 is strictly weaker
  than uniform orientation.
* For the positive \(m=3\) projection there are 75 tight lower/upper
  transversal pairs, but only one satisfies the rigid block rule and is a
  common transversal.  This independently verifies that the qualifier in
  Theorem 4.1 is necessary.
* The vendored GMM \(m=4\) saturating cycle has base lower profile
  \(0^{17}1^{22}2^{17}\).  A cap-two lift makes only
  \(K=\operatorname {Cat}_4=14\) replacements, each filling at most one
  old hole, so at least \(17-14=3\) lower colours remain missing for every
  host injection and orientation on this fixed cycle.  The deterministic
  lexicographic injection has profile \(0^8 1^{26}2^{22}\), eight isolated
  lower colours, maximum matching 46, and determinant zero.
* The independent sparse replay
  scratch/audit_catalan_abstract_colour_forest_lift_m2_m6_sparse_20260731.py
  constructs the deterministic standard-BTK \(\sigma,\tau,S\) for every
  \(m=2,\ldots,6\).  The colour graph \(H=\sigma\cup S\) passes the
  balanced-forest and determinant theorem in all five cases.  Separately,
  \(\Psi(\sigma)\) is spanning and acyclic with exactly \(K\) components,
  but is a path forest only at \(m=2\); the alternating owner \(E_m\) has
  audited degree \(m\).  Every full \(H\)-lift fails middle degree two.
  Its component counts are \(1,2,3,15,44\), and its local incompatible
  doubled-upper counts are \(0,2,2,14,46\).

The \(m=4\) conclusion is source-relative to that fixed GMM cycle; it is
not an \(m=4\) or all-\(m\) no-go.  Theorem 5.1 is an unconditional
all-\(m\) abstract construction, while a physical all-\(m\) directed
repair still requires all three conditions of Theorem 5.2.
