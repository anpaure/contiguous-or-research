# Four-transversal matroids and the exact turn-augmentation graph

Date: 2026-07-31  
Status: exact equivalences, augmenting-path theorem, and circuit/determinant
obstructions; no all-\(m\) Catalan linear matching or suitable decorable
middle-levels cycle is claimed

## 1. The arbitrary ordered four-transversal is five-fold common independence

Fix \(|\Omega|=2m\), and put

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},
\]

\[
 K=\operatorname {Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 M=|\mathcal X|=(m+1)K.
\]

Let the oriented-diamond ground set be

\[
 \mathcal Q_m={q=(L,a,b):L\in\mathcal L,\ a,b\notin L,\ a\ne b\}.
\]

For \(q=(L,a,b)\), define

\[
 \lambda(q)=L,\quad
 \upsilon(q)=L+a+b,\quad
 \tau(q)=L+a,\quad
 \eta(q)=L+b,                              \tag{1.1}
\]

and let \(e(q)=\{\tau(q),\eta(q)\}\) be its undirected Johnson edge.
For each \(c\in\{\lambda,\upsilon,\tau,\eta\}\), let \(P_c\) be the
rank-one partition matroid whose classes are the fibres of \(c\).  Let
\(G\) be the graphic matroid of the multigraph on \(\mathcal X\) whose
edge copies are the \(e(q)\)'s.

### Theorem 1.1 (five-matroid normal form)

The Catalan Linear Matching assertion is equivalent to finding
\(I\subseteq\mathcal Q_m\) such that

\[
 |I|=N,\qquad
 I\in P_\lambda\cap P_\upsilon\cap P_\tau\cap P_\eta\cap G. \tag{1.2}
\]

#### Proof

At cardinality \(N\), independence in \(P_\lambda\) and \(P_\upsilon\)
forces both maps to be bijections, because each has exactly \(N\) fibres.
Independence in \(P_\tau\) and \(P_\eta\) makes the selected oriented
Johnson graph have outdegree and indegree at most one.  Graphic independence
makes its underlying graph acyclic.  These are exactly the ordered
four-transversal conditions.

Conversely, orient every path of a Catalan linear matching.  Its lower,
upper, tail and head maps obey the four partition constraints, and its
physical path forest is graphic-independent. \(\square\)

There is an equivalent block-parity statement.  Replace each \(q\) by five
clones

\[
 B_q=\{q^\lambda,q^\upsilon,q^\tau,q^\eta,q^G\}.
\]

Take the direct sum of the four clone partition matroids and the graphic
matroid on the \(G\)-clones.  Selecting \(N\) whole blocks \(B_q\) whose
union is independent is exactly (1.2).  Thus the problem is matroid
five-parity (four-parity before acyclicity), not ordinary pair parity.

The global quotient-perfect-matching theorem closes only
\(P_\lambda\cap P_\upsilon\).  The tail, head and graphic correlations in
(1.2) are the remaining integral gate.

The five-matroid formulation itself, a four-blocker non-3-extendibility
witness, a determinant-three minor and fractional-polytope obstructions are
already proved in
`MATH_THEOREM_CATALAN_FOUR_TRANSVERSAL_ROUNDING_NOGOS_20260731.md`.
Sections 2--3 below add an exchange-circuit view; they are not presented as
stronger numerical rounding no-gos.

## 2. Why ordinary two-matroid intersection does not encode (1.2)

The failure is intrinsic on the natural ground set, not merely a poor
choice of the five displayed matroids.

Fix \(R\subset\Omega\) with \(|R|=m-2\), and choose four further points
\(0,1,2,3\).  Write, for example, \(R013=R\cup\{0,1,3\}\).  Consider the
five oriented diamonds

\[
\begin{array}{c|cccc}
 &\lambda&\upsilon&\tau&\eta\\ \hline
q_0&R0&R012&R01&R02\\
q_1&R0&R013&R01&R03\\
q_2&R3&R013&R03&R13\\
q_3&R1&R123&R12&R13\\
q_4&R1&R012&R12&R01.
\end{array}                                             \tag{2.1}
\]

Their same-role conflict graph is exactly the induced five-cycle

\[
                       q_0q_1q_2q_3q_4q_0.             \tag{2.2}
\]

The consecutive conflicts come respectively from

\[
 (\lambda,\tau),\quad\upsilon,\quad\eta,\quad
 (\lambda,\tau),\quad\upsilon,
\]

and no nonconsecutive pair shares a same-role colour.  Every nonconflicting
pair also has two distinct physical edges and is graphic-independent.

### Proposition 2.1 (odd-cycle matroid obstruction)

The hereditary feasibility system in (1.2), restricted to the five
elements (2.1), is the stable-set system of \(C_5\).  It is not the
intersection of the independent-set systems of two matroids on those five
elements.

#### Proof

Suppose it were \(\mathcal I(M_1)\cap\mathcal I(M_2)\).  Every singleton is
independent, so each dependent pair forming an edge of (2.2) is a
two-element circuit, hence a parallel pair, in at least one \(M_i\).
Two incident edges of the five-cycle cannot be parallel pairs in the same
matroid: transitivity of parallelism would make the intervening
nonedge-pair dependent.  The five cycle edges would therefore need a proper
two-edge-colouring, impossible for an odd cycle. \(\square\)

This rules out an exact two-matroid representation on the natural oriented
diamonds.  It does not rule out a nonlocal gadget expansion designed only to
reproduce full solutions.

The companion rounding theorem gives the stronger cardinal statement that
the same feasibility system is not the intersection of even three matroids.
The value of (2.2) is its minimal odd-circuit anatomy and the explicit
missing inequality (2.4).

The same fixture gives a determinant obstruction.  On the five columns in
(2.1), take the rows

\[
 \lambda=R0,\quad\upsilon=R013,\quad\eta=R13,\quad
 \lambda=R1,\quad\upsilon=R012.
\]

The resulting submatrix is

\[
 \begin{pmatrix}
 1&1&0&0&0\\
 0&1&1&0&0\\
 0&0&1&1&0\\
 0&0&0&1&1\\
 1&0&0&0&1
 \end{pmatrix},
 \qquad |\det|=2.                                    \tag{2.3}
\]

The half-vector \(x_{q_i}=1/2\) satisfies all four palette capacities and
all graphic-forest inequalities: the five physical edges form a four-cycle
with one pendant edge.  An integral feasible subset has size at most two.
The missing valid inequality on this restriction is the odd-cycle row

\[
                       \sum_{i=0}^4x_{q_i}\le2.        \tag{2.4}
\]

Even a three-column ordered incidence minor has determinant two.  Use

\[
 (R0,R012,R01,R02),\quad
 (R0,R023,R02,R03),\quad
 (R2,R012,R02,R12)
\]

and the rows \(\lambda=R0,\upsilon=R012,\tau=R02\).  The minor is

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad\det=-2.                                      \tag{2.5}
\]

Thus separating tails from heads does not restore total unimodularity.
The determinant-three minor in the companion rounding theorem is the
stronger matrix obstruction; (2.3) records the odd-cycle circuit responsible
for this particular exchange failure.

## 3. The exact exchange object is an AND/OR hypergraph

Let \(I\) be any set independent in the five matroids.  For
\(q\notin I\), let \(b_c(q)\) be the unique incumbent in \(I\) having
the same \(c\)-colour, when it exists, for
\(c\in\{\lambda,\upsilon,\tau,\eta\}\).  Let \(F_I\) be the selected
physical forest.  If the endpoints of \(e(q)\) are connected in \(F_I\),
write \(P_I(q)\) for their unique path; otherwise put
\(P_I(q)=\varnothing\).

### Theorem 3.1 (literal insertion/deletion criterion)

For \(D\subseteq I\), the set

\[
                         (I\setminus D)\cup\{q\}       \tag{3.1}
\]

is independent in all five matroids if and only if

\[
 b_c(q)\in D
 \quad\hbox{for every occupied }c\in
 \{\lambda,\upsilon,\tau,\eta\},                     \tag{3.2}
\]

and

\[
 P_I(q)\ne\varnothing\quad\Longrightarrow\quad
                         D\cap P_I(q)\ne\varnothing.  \tag{3.3}
\]

#### Proof

Each occupied partition fibre has exactly one blocker, and every such
blocker must be removed; this is (3.2).  In the graphic matroid, inserting
\(e(q)\) creates no circuit when its endpoints are disconnected.  When they
are connected, its fundamental circuit is
\(P_I(q)\cup\{e(q)\}\), so the insertion is independent exactly when at
least one old edge of that path is removed. \(\square\)

All palette blockers in (3.2) are mandatory simultaneously, whereas any
one edge of the graphic fundamental circuit in (3.3) is sufficient.  The
exchange object is therefore an AND/OR hypergraph.  One insertion can force
four different palette deletions plus a choice on a fifth circuit; there is
no ordinary alternating-path augmentation theorem for (1.2).

At the outer-colour level alone, two perfect matchings differ by disjoint
alternating cycles in the diamond graph.  A four-cycle is a hinge rotation
inside one middle rectangle and leaves the pivot load unchanged.  Hence a
square-only exchange walk cannot repair an overload at that pivot.  Larger
alternating cycles remain exact candidates, but their degree changes and
acyclicity must pass the rectangle and contraction tests in
`MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md`.

## 4. A fixed middle-levels cycle collapses to one bipartite matching

Now let \(\Omega_0=[2m-1]\), and fix a Hamilton cycle of
\({\rm ML}(2m-1)\), written

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1},                \tag{4.1}
\]

where

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P=\operatorname {Cat}_m.                         \tag{4.2}
\]

Its turn colours are

\[
 \ell_i=A_i\cap A_{i+1}\in\binom{\Omega_0}{m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in\binom{\Omega_0}{m+1}.        \tag{4.3}
\]

Build the **turn-augmentation graph** \(H_C\).  Its shores are

\[
 \mathscr A={A_i:i\in\mathbb Z_Q\}
       \sqcup\binom{\Omega_0}{m-2},
 \qquad
 \mathscr B={B_j:j\in\mathbb Z_Q\}
       \sqcup\binom{\Omega_0}{m+1}.                  \tag{4.4}
\]

Add three kinds of edges:

1. the literal cycle incidences \(A_iB_{i-1}\) and \(A_iB_i\);
2. the upper occurrence edge \(A_i u_i\);
3. the lower occurrence edge \(\ell_j B_j\).

Parallel labels are not merged: every position has its own occurrence edge.

### Theorem 4.1 (one matching equals the alternating occurrence SDR)

Perfect matchings of \(H_C\) are in bijection with Catalan decorations of
the fixed cycle \(C\).

#### Proof

Every upper-colour vertex is matched to exactly one occurrence \(A_i\), and
every lower-colour vertex to exactly one occurrence \(B_j\).  Call these
positions marked.  Every remaining position vertex must be matched by a
cycle edge.  Thus the unmarked induced paths have a perfect matching, which
is equivalent to even zero-runs and hence to alternation of the marked rail
types.  Each residual path matching is unique.

Conversely, the two turn transversals of a Catalan decoration match every
colour vertex to its selected occurrence.  Its forced residual cycle
matching covers all remaining positions, giving a perfect matching of
\(H_C\). \(\square\)

Thus the fixed-cycle problem is exactly the common-base problem for the two
shore partition matroids on \(E(H_C)\), equivalently ordinary bipartite
perfect matching.  Its signed node-edge incidence matrix is totally
unimodular.  There is no determinant-two obstruction in this fixed-cycle
subclass.  Hall in \(H_C\), rather than separate turn surjectivity, is the
complete representative-selection gate.

Any two decorations differ by disjoint even alternating circuits of
\(H_C\).  This is the genuine exchange graph missing from the arbitrary
five-fold formulation.

## 5. Exact Berge augmentation

Choose either of the two perfect matchings of the bare position cycle in
(4.1).  Regard it as a matching \(M_0\) of \(H_C\); it saturates all
\(2Q\) position vertices and leaves all \(2P\) colour vertices unmatched.

### Theorem 5.1 (turn-augmentation path theorem)

The cycle \(C\) has a Catalan decoration if and only if one can perform
exactly \(P\) ordinary Berge augmentations, starting from \(M_0\), where
each augmenting path begins at an unmatched lower-colour vertex and ends at
an unmatched upper-colour vertex.

After \(r\) augmentations:

* every position vertex remains saturated;
* exactly \(r\) lower and \(r\) upper colour vertices are saturated; and
* the matching contains exactly \(Q-r\) literal cycle edges.

#### Proof

The assertions are true for \(M_0\).  Its only unmatched vertices are
colour vertices, split equally between the two shores.  Any augmenting path
therefore has one unmatched colour endpoint on each shore; flipping it
saturates those two endpoints and leaves every internal position or colour
vertex saturated.  The number of occurrence matches rises by two while the
total matching size rises by one, so the number of literal cycle matches
falls by one.  This gives the displayed counts by induction.

If a perfect matching of \(H_C\) exists, Berge's theorem supplies an
augmenting path from every nonmaximum intermediate matching, until size
\(Q+P\) is reached after \(P\) steps.  Conversely, after \(P\) such steps
all \(2(Q+P)\) vertices are saturated, so Theorem 4.1 gives a decoration.
\(\square\)

This is a literal polynomial augmenting-path theorem for the fixed-cycle
architecture.  It is not an augmentation theorem for arbitrary ordered
four-transversals.

## 6. The gap--Hall theorem is the fixed-upper fibre of \(H_C\)

Fix an upper SDR \(I\subseteq\mathbb Z_Q\), and force the occurrence edges
\(A_i u_i\) for \(i\in I\).  Consecutive selected \(A\)-positions split the
remaining position cycle into \(P\) odd paths.  In each path exactly one
\(B\)-position must be matched to a lower-colour vertex; after that choice,
the remaining cycle matching is unique.

Contract each such path to its gap.  The residual perfect-matching problem
is exactly the gap--lower-colour graph \(\Gamma_I\) from
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`:

\[
 G\sim L
 \quad\Longleftrightarrow\quad
 \text{some }B_j\text{ in gap }G\text{ has }\ell_j=L. \tag{6.1}
\]

### Corollary 6.1 (global matching/fibre Hall equivalence)

The following are equivalent:

1. \(H_C\) has a perfect matching;
2. there is an upper SDR \(I\) for which \(\Gamma_I\) has a perfect
   matching;
3. there are upper and lower turn representatives alternating around \(C\).

For a fixed \(I\), Hall deficiency in \(\Gamma_I\) is exactly the
obstruction to extending the forced upper occurrence edges inside \(H_C\).

The explicit \({\rm ML}(7)\) counterexample has three consecutive globally
unique upper turns.  Every upper SDR therefore contains those three
positions.  The two singleton intervening gaps both see the same lower
colour \(96\), so those two gap vertices have a one-colour neighbourhood.
This is a literal Hall deficiency one.  Both turn maps are nevertheless
surjective; all \(12{,}288\) upper SDRs fail, with maximum gap matching
\(20/21\).  By contrast, the exhaustive \({\rm ML}(5)\) census finds all
24 canonical cycles decorable.

Hence a recursive middle-levels construction must preserve gap Hall, or
equivalently perfect matchability of \(H_C\).  Preserving the two turn
surjections separately is insufficient.

## 7. The remaining topology is one parity class

Let \(M\) be a perfect matching of \(H_C\), and put

\[
                         R=M\cap E(C).
\]

Then \(|R|=K\).  Number the position vertices cyclically as
\(v_0,\ldots,v_{2Q-1}\), and give the cycle edge
\(c_t=v_tv_{t+1}\) the type \(t\bmod2\).

### Lemma 7.1 (residual-edge parity form)

The physical diamond lift of the decoration contains its exceptional one
cycle if and only if the types of the edges of \(R\), read cyclically in
their occurrence order, alternate.

#### Proof

For consecutive residual edges \(c_p,c_q\), the number of marked vertices
strictly between them is \(q-p-2\) in the corresponding cyclic lift.  Their
types differ exactly when this number is odd.  Two residual edges lying in
one zero-run of length at least four are consecutive and have the same type.
Thus type alternation is equivalent to every zero-run having length two and
every intervening marked run having odd length.  This is exactly the
one-cycle criterion in
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`.
\(\square\)

### Corollary 7.2

If \(K=\operatorname {Cat}_m\) is odd, every perfect matching of \(H_C\)
gives a spanning \(K\)-path forest.  If \(K\) is even, a decoration is a
forest exactly when two consecutive residual cycle edges have the same
type.

Indeed, a cyclic alternating binary sequence has even length.

## 8. A polynomial forest-decision reduction on a fixed cycle

The parity class can be excluded using only ordinary bipartite matching.
For two distinct same-type cycle edges \(c_p,c_q\), orient the cyclic arc
from \(c_p\) to \(c_q\).  Define the residual graph \(H_C[p,q]\) after
committing to those two forced edges: delete their four endpoints and every
incident edge, then delete every remaining cycle edge whose two endpoints
lie strictly between them on that arc.

### Theorem 8.1 (forced-pair matching criterion)

For \(K\ge2\), the fixed cycle \(C\) has a forest decoration if and only if
\(H_C[p,q]\) is perfect-matchable for some ordered pair of distinct
same-type cycle edges \((c_p,c_q)\).

#### Proof

A perfect matching of \(H_C[p,q]\), together with the two forced edges,
has no residual cycle edge on the open arc between them.  Hence
\(c_p,c_q\) are consecutive residual edges of the same type, and Corollary
7.2 gives a forest.

Conversely, in any forest decoration choose consecutive same-type residual
edges \(c_p,c_q\) and orient the empty residual arc from the first to the
second.  Its matching uses no internal cycle edge there, so after removing
the two forced edges it is a perfect matching of \(H_C[p,q]\). \(\square\)

There are at most \(2Q(Q-1)\) ordered same-type pairs.  Thus, measured in
the explicitly supplied cycle/graph size \(Q\), fixed-cycle forest existence
is decided by one perfect-matching test when \(K\) is odd and by
\(O(Q^2)\) ordinary bipartite matching tests when \(K\) is even.  Every
test has the standard Hall and augmenting-path certificates.

## 9. Exact scope

The turn-augmentation graph solves the alternating occurrence correlation
for one chosen middle-levels Hamilton cycle.  It does not show that a
**decorable**, equivalently \(H_C\)-perfect-matchable, Hamilton cycle exists
in every dimension.  The authenticated \(m=4\) cycle proves
that even two turn-surjections need not pass its Hall gate.

Nor does it normalize arbitrary Catalan linear matchings.  The explicit
\(m=3\) path-forest matching in
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
has forced middle-levels support of degree three and therefore lies in no
middle-levels Hamilton cycle.  The general five-matroid problem is strictly
broader than the fixed-cycle two-matroid subclass.

## 10. Hexagon gluing as bounded matching transfer

The positive \(m=4\) repair in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
fits the augmentation graph exactly.  Let \(C'=C\mathbin\triangle Z\) be a
standard incidence-hexagon toggle which is Hamilton-to-Hamilton.  The graphs
\(H_C,H_{C'}\) have the same vertices.  Their only different edges are:

* the three old versus three new cycle incidences of \(Z\); and
* turn-occurrence edges incident with the six hexagon positions whose
  neighbour pair changed.

### Theorem 10.1 (hexagon transfer trichotomy)

Let \(M\) be a perfect matching of \(H_C\), and delete from it every edge
absent from \(H_{C'}\), obtaining \(M^\cap\).  Then:

1. at most six edges are deleted, so \(M^\cap\) is repaired to a maximum
   matching of \(H_{C'}\) by at most six Berge augmentations;
2. \(C'\) has some Catalan decoration if and only if those augmentations can
   reach a perfect matching, equivalently iff \(H_{C'}\) has no Hall
   deficiency;
3. the selected vertex sets of \(M\) themselves transfer to a decoration of
   \(C'\) exactly under the two transparent-hexagon conditions: equality of
   the selected local turn-colour multisets separately on both shores, and
   alternation of the retained-fragment boundary mark types after
   reconnection; and
4. a transferred or repaired decoration has a physical path-forest lift
   exactly when its residual cycle-edge types escape the alternating parity
   class of Lemma 7.1, decidable by Theorem 8.1.

#### Proof

Every edge of \(H_C\setminus H_{C'}\) is incident with one of the six
hexagon position vertices.  Since \(M\) matches each such vertex once, at
most six members of \(M\) disappear.  Standard augmentation from
\(M^\cap\) reaches a maximum matching of \(H_{C'}\), proving statements 1
and 2 by Berge's theorem and Theorem 4.1.

For fixed selected vertex sets, only the six local turn colours and the
three fragment seams can change.  Exact restoration of the two colour
bijections is therefore equality of the two local selected-colour
multisets; exact restoration of mark alternation is the fragment-boundary
test.  This is precisely the transparent-hexagon lemma, proving statement
3.  Statement 4 is Lemma 7.1 and Theorem 8.1. \(\square\)

Thus every Hamilton-preserving hexagon lies in exactly one of three matching
classes relative to a supplied state:

* **transparent:** the same selected occurrences pass the local palette and
  boundary tests;
* **repairable:** the supplied state is not transparent, but a perfect
  matching of \(H_{C'}\) exists and can be reached by at most six
  augmentations; or
* **Hall-blocked:** \(H_{C'}\) is not perfect-matchable.

The forest parity test is then imposed on the transparent or repairable
class.  In the authenticated \(m=4\) census, 31 alternating hexagons give
16 Hamilton outputs; ten are decorable, and six have a common forest
decoration on both sides.  The latter six are the literal transparent
toggle types which admit transparent state transitions (2,412 common
decoration transitions in total), not six individual state-graph edges.
Four further Hamilton outputs require changing representatives, while six
are Hall-blocked.

### Corollary 10.2 (recursive state invariant)

A sufficient recursive object is a tree whose nodes carry a perfect
matching of the appropriate turn-augmentation graph plus the forest-parity
bit, and whose gluing edges satisfy the transparent local transfer
relation.  Equivalently one may carry the full feasible-matching relation
and allow the bounded augmentation repair of Theorem 10.1 at each edge.

Hence the correct Middle Levels recursion target is a **joint alternating
SDR plus transparent gluing tree**.  A frozen arbitrary SDR is too rigid,
while an undecorated published gluing tree does not preserve gap Hall.
The finite positive \(m=4\) toggle proves that the transparent relation is
nonempty; it does not prove that an accepting state exists at every
recursive root.

## 11. Leaf-peelable gap Hall is a second graphic transfer

Fix the upper SDR \(I\) of a decoration and its contracted gap--colour graph
\(\Gamma_I\) from Section 6.  Call the decoration **leaf-peelable** when
\(\Gamma_I\) is a forest.  Because the decoration already supplies a
perfect matching of this balanced bipartite graph, that matching is then
unique: the symmetric difference of two perfect matchings would be a cycle,
and the unique matching is recovered by repeatedly deleting matched leaves.

Here \(\Gamma_I\) means the **simple support** graph: an edge \(gL\) records
that lower colour \(L\) occurs at least once in gap \(g\), and repeated
occurrences are coalesced.  Its contraction is still a multigraph: two
distinct support edges that acquire the same contracted endpoints remain
parallel and form a genuine two-cycle.

Let a transparent hexagon carry the fixed decoration from \(C\) to \(C'\).
Name every gap by the unordered pair of selected \(A\)-positions at its
ends, and put

\[
 D=E(\Gamma_I)\setminus E(\Gamma'_I),\qquad
 S=E(\Gamma'_I)\setminus E(\Gamma_I).                 \tag{11.1}
\]

Only the three old and three new seam-crossing gaps and the lower turns at
the three upper-shore hexagon positions can change.

### Theorem 11.1 (exact gap-forest transfer row)

Assume \(\Gamma_I\) is a forest and the palette/boundary transparency rows
hold.  Delete \(D\), contract every component of \(\Gamma_I-D\), retain
each new gap vertex occurring in \(S\), and let \(A_S\) be the resulting
attachment multigraph of the new edges.  Then the transferred decoration is
leaf-peelable if and only if

\[
             A_S\text{ is loopless and acyclic}.       \tag{11.2}
\]

Equivalently, after loops are excluded, the exact additional local rows are
the graphic inequalities

\[
 |S[W]|\le |W|-1
 \qquad(\varnothing\ne W\subseteq V(A_S)),             \tag{11.3}
\]

where \(S[W]\) denotes new attachment edges with both contracted endpoints
in \(W\).

#### Proof

The edge identity

\[
                     \Gamma'_I=(\Gamma_I-D)+S         \tag{11.4}
\]

is literal after gaps are named by their selected endpoints.  The retained
graph \(\Gamma_I-D\) is a forest.  Adding \(S\) creates a cycle precisely
when some new edge is a loop after contraction or the contracted attachment
multigraph contains a cycle.  This proves (11.2), and (11.3) is the standard
graphic-matroid rank description.  Transparency already preserves a
perfect matching of \(\Gamma'_I\); if (11.2) holds, forest acyclicity makes
that matching unique and leaf-peelable. \(\square\)

This is the exact extra cycle-avoidance row requested by the component-Hall
formulation.  It is formally the same delete--contract--insert test as the
physical graphic exchange in Section 3, now applied to the contracted
gap--colour fibre of \(H_C\).

The same criterion is the leaf-transparent switch theorem in
`MATH_THEOREM_K_GAP_HALL_PASCAL_DECORATION_RECURSION_20260731.md`, where it
is also composed with internal block matchings and a residual boundary Hall
graph.  The contribution here is its placement inside the single
turn-augmentation matching/exchange system.

Palette transparency alone does not imply (11.2).  In the authenticated
\(m=4\) toggle with \(H=66,(a,b,c)=(0,3,4)\), one transferred boundary gap
and one unchanged gap both see lower colours \(65,68\), creating a literal
four-cycle.  Exactly 72 of the 144 common decorations remain leaf-peelable
and 72 fail leaf-peelability on \(C'\), while remaining valid common
decorations with physically linear lifts.  Nevertheless every one of the
six transparent Hamilton toggle types has at least one common leaf-peelable
forest decoration.

Consequently the stronger recursive state is:

\[
 \boxed{\text{joint alternating SDR}
 +\text{ transparent gluing tree}
 +\text{ gap-graphic row (11.2)}
 +\text{ physical forest-parity bit}.}
\]

The positive \(m=2,3,4\) fixtures and all 1,728 decorations of the repaired
\(m=4\) cycle satisfy the leaf-peelable condition.  This is finite evidence,
not an all-\(m\) existence theorem.
