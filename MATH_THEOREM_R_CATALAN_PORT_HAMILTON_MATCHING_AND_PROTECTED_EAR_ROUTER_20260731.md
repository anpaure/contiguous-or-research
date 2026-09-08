# Catalan port Hamilton matchings and protected ear routers

Date: 2026-07-31  
Lane: R, protected connectivity  
Status: unconditional occurrence-level characterization and constructive
sufficient theorems.  The Catalan cap-two and rainbow hypotheses do not by
themselves imply the new ear hypotheses.  Deeper-shadow and residence
protection are conclusions only under the literal guard assumptions in
Section 8.  No K17 or all-dimensional equality claim is made.

## 0. Verdict

Fix a Catalan endpoint-complement pair of path forests.  There are \(K\)
marked fragments and \(K\) unmarked fragments, hence \(2K\) occurrence
ports on each shore.  Let \(P\) pair the two ports of each retained
fragment, and let \(G\) be the bipartite port containment graph.

The exact surviving connectivity problem has three useful forms.

1. A perfect matching \(M\) is Hamilton-compatible exactly when it satisfies
   the ordinary port degree equations and every balanced \(P\)-block
   subtour inequality.  This is an exact integral characterization, not an
   ordinary Hall theorem.
2. After orienting the fragments, a connected matching is exactly an entry
   matching followed by one directed Hamilton cycle in an exit-containment
   digraph.  A three-seam insertion replaces one old seam and inserts one
   marked and one unmarked fragment while preserving one cycle.  Iterating
   these insertions is a constructive certificate which cut selection can
   enforce directly.
3. Starting from any safe perfect matching, a directed socket cycle using
   one old rung from each of distinct factor components is a clean long
   ear and merges those components.  A port-disjoint incidence-tree bank
   of such ears Hamiltonizes monotonically.

The Boolean containment geometry sharpens the third form.  If
\(e_i=(L_i,U_i)\) is a current rung, where

\[
 L_i\in\binom{[2m]}m,\qquad
 U_i\in\binom{[2m]}{m+1},\qquad L_i\subset U_i,
\]

then the socket transition \(e_i\to e_j\) is exactly
\(L_j\subset U_i\).  For distinct labels this forces

\[
                         U_i=L_i\cup L_j.              \tag{0.1}
\]

Thus simple socket ears are literal cyclic Johnson necklaces of marked
endpoint labels, with the required unmarked occurrence at each adjacent
union.

There is no nondegenerate physical C4 in this rank-gap-one containment
graph.  Consequently a generic C4-descent or dense matching-exchange
argument is not the correct Boolean mechanism.  The first simple exchanges
are C6s, C8s and longer necklaces.

The \(m=2\) chordless-C8 example remains sharp.  Its port graph is connected,
matching-covered and satisfies strict Hall on every proper nonempty marked
port set, but both perfect matchings give two factor components.  Its sole
socket cycle has component word \(ABAB\), rather than one rung from each
component.  Hence ordinary expansion, socket strong connectivity, lower
rainbowness and marked upper q1 do not force the required topology.

The new positive all-\(m\) target is precise:

> choose the Catalan cuts and endpoint sides so that EC1--EC3 hold and the
> resulting protected port catalogue contains either a literal paired-ear
> insertion certificate or a port-disjoint component-transversal socket-ear
> hypertree.

Existence of that protected certificate for PBBS or Pascal rails remains
open.

## 1. Occurrence-labelled port model

Let

\[
 {\cal A}=\{a_i^0,a_i^1:1\le i\le K\},\qquad
 {\cal B}=\{b_j^0,b_j^1:1\le j\le K\}.                \tag{1.1}
\]

The pair \(\{a_i^0,a_i^1\}\) consists of the endpoints of marked fragment
\(A_i\); the pair \(\{b_j^0,b_j^1\}\) consists of the endpoints of unmarked
fragment \(B_j\).  These are occurrence tokens.  Adjacent cuts may give two
different tokens at the same physical owner.

Let \(P_{\cal A}\) and \(P_{\cal B}\) be the fixed-point-free involutions
which exchange the two ports of every fragment, and put

\[
                         P=P_{\cal A}\sqcup P_{\cal B}. \tag{1.2}
\]

Every marked occurrence \(a\) has a distinct label

\[
                L(a)\in\binom{[2m]}m,                 \tag{1.3}
\]

and every unmarked occurrence \(b\) has a physical owner

\[
                U(b)\in\binom{[2m]}{m+1}.             \tag{1.4}
\]

The endpoint-complement hypotheses used below are:

* **EC1.**  The marked retained forest has \(K\) nontrivial paths and its
  internal lower colours enumerate the complete tagged lower palette.
* **EC2.**  The unmarked retained forest has \(K\) paths and its internal
  lower colours are pairwise distinct and form a set \({\cal L}\).
* **EC3.**  The \(2K\) marked endpoint labels are pairwise distinct and are
  exactly the complementary unmarked lower-colour set
  \(\binom{[2m]}m\setminus{\cal L}\).

Define

\[
 G=({\cal A},{\cal B};E),\qquad
 ab\in E\quad\Longleftrightarrow\quad L(a)\subset U(b).
                                                               \tag{1.5}
\]

A perfect matching \(M\) of \(G\) produces the degree-two factor

\[
                            F(M)=P\cup M.              \tag{1.6}
\]

This is the fixed-fragment port theorem of
MATH_THEOREM_R_CATALAN_TWO_RAIL_PORT_MATCHING_AND_C8_CONNECTIVITY_OBSTRUCTION_20260731.md.
In particular, because every marked port and every unmarked occurrence is
used once, all such \(M\) have the same exact lower-q1 multiset and the same
complete immediate-upper multiplicity vector.

The occurrence convention in (1.1) is essential.  The graph \(F(M)\) is
formed on tokens and then expanded through the retained physical fragments.
Two endpoint tokens at the same physical owner are not interchangeable
unless the resulting physical edge set is also simple.

## 2. Exact block-subtour characterization

For \(I,J\subseteq[K]\), put

\[
 {\cal A}_I=\{a_i^0,a_i^1:i\in I\},\qquad
 {\cal B}_J=\{b_j^0,b_j^1:j\in J\}.                   \tag{2.1}
\]

For an edge set \(x\), write \(x(X,Y)\) for the number of selected edges
between \(X\) and \(Y\).

### Theorem 2.1 (Hamilton-compatible port matching)

The port graph has a Hamilton-compatible matching if and only if the
following binary system is feasible:

\[
\begin{aligned}
 &x_e\in\{0,1\} &&(e\in E),\\
 &\sum_{e\ni v}x_e=1 &&(v\in{\cal A}\sqcup{\cal B}),  \tag{2.2}\\
 &x({\cal A}_I,{\cal B}\setminus{\cal B}_J)
  +x({\cal A}\setminus{\cal A}_I,{\cal B}_J)\ge2
 &&(1\le |I|=|J|<K).
\end{aligned}
\]

Equivalently, after contracting all fragment pairs, the selected edges have
graphic rank \(2K-1\).

#### Proof

The degree equations select a perfect matching \(M\).  Contract the \(K\)
marked and \(K\) unmarked fragment edges of \(P\).  Every contracted vertex
has degree two, so the resulting multigraph is a disjoint union of
alternating cycles.

Let \(S={\cal A}_I\sqcup{\cal B}_J\).  The selected matching cut of \(S\)
has size

\[
 x({\cal A}_I,{\cal B}\setminus{\cal B}_J)
 +x({\cal A}\setminus{\cal A}_I,{\cal B}_J).          \tag{2.3}
\]

If \(|I|\ne|J|\), the degree equations give

\[
                         x(\delta S)\ge2\,\bigl||I|-|J|\bigr|,   \tag{2.4}
\]

so only balanced block cuts can be empty.  A disconnected cycle component
contains the same number of marked and unmarked fragments and gives a
proper balanced block cut of value zero.  Conversely, a zero proper
balanced cut is a union of components.  The cut size is always even, so
nonzero is equivalent to at least two.  This proves (2.2).

The contracted graph has \(2K\) vertices.  Its graphic rank is \(2K-1\)
exactly when it is connected. \(\square\)

### Corollary 2.2 (involution form)

Regard a matching as a bijection \(f:{\cal A}\to{\cal B}\), and define the
fixed-point-free involution

\[
                         Q_f=f^{-1}P_{\cal B}f          \tag{2.5}
\]

on \({\cal A}\).  Then \(F(M)\) is connected if and only if
\(P_{\cal A}\cup Q_f\) is one \(2K\)-cycle.  Equivalently,
\(P_{\cal A}Q_f\) has exactly two cycles, both of length \(K\).

#### Proof

Contract every matching edge \(a f(a)\).  The \(P_{\cal B}\)-edges become
the \(Q_f\)-edges and the \(P_{\cal A}\)-edges are unchanged.  This
contraction preserves components.  On one alternating \(2s\)-cycle, the
product of its two involutions advances two positions and hence has two
\(s\)-cycles. \(\square\)

Theorem 2.1 is an exact characterization, but it is not an integrality
claim for the linear relaxation of (2.2).

## 3. Exact universal-connectivity and forced-separation tests

The following criterion is stronger than existence but is often easier to
certify after choosing the cuts.

### Theorem 3.1 (block indecomposability)

Assume \(G\) has a perfect matching.  Every perfect matching of \(G\) is
Hamilton-compatible if and only if there are no \(I,J\) with

\[
 1\le |I|=|J|<K                                      \tag{3.1}
\]

for which both induced graphs

\[
 G[{\cal A}_I,{\cal B}_J],\qquad
 G[{\cal A}\setminus{\cal A}_I,
   {\cal B}\setminus{\cal B}_J]                       \tag{3.2}
\]

have perfect matchings.

In particular, the sufficient inequalities

\[
 \nu\bigl(G[{\cal A}_I,{\cal B}_J]\bigr)<2|I|
 \quad(1\le |I|=|J|<K)                               \tag{3.3}
\]

make every port perfect matching connected.

Here \(\nu(H)\) denotes the maximum matching cardinality of a bipartite
graph \(H\).

#### Proof

If both graphs in (3.2) have perfect matchings, their union is a perfect
matching of \(G\) with no edge across the proper \(P\)-closed block cut, so
it is disconnected.

Conversely, any disconnected perfect matching has a nonempty proper union
of cycle components.  Its marked and unmarked fragment sets \(I,J\) have
equal size, and the restrictions of the matching to that block and its
complement are the two perfect matchings in (3.2).  Inequality (3.3)
excludes the first one. \(\square\)

### Proposition 3.2 (guard-created tight-shore obstruction)

Let \(G_{\rm safe}\subseteq G\) be the port graph after deleting seams
forbidden by selected upper witnesses, residence states or compiler pins.
Suppose a nonempty proper union \({\cal S}\) of current factor components
has marked and unmarked port sets \(A_{\cal S},B_{\cal S}\), and

\[
             N_{G_{\rm safe}}(A_{\cal S})\subseteq B_{\cal S}.    \tag{3.4}
\]

Then every perfect matching of \(G_{\rm safe}\) isolates \({\cal S}\).
In particular no protected Hamilton-compatible matching exists in this
guarded fixed-fragment fibre.

#### Proof

Every factor component contains equally many marked and unmarked port
tokens, so \(|A_{\cal S}|=|B_{\cal S}|\).  A perfect matching must map all
of \(A_{\cal S}\) into \(B_{\cal S}\), consuming the whole latter set.
No selected matching edge crosses the \(P\)-closed cut. \(\square\)

This is the precise way an upper-witness or residence restriction can
become a topology obstruction.  Absence of (3.4) is not sufficient; the
strict-Hall example in Section 9 has no such elementary forced shore.

## 4. Oriented fragment ladder

Choose an orientation of every fragment and write its entry and exit ports
as

\[
 A_i=(a_i^-,a_i^+),\qquad B_j=(b_j^-,b_j^+).          \tag{4.1}
\]

Define the entry graph

\[
 i\sim_- j\quad\Longleftrightarrow\quad
 L(a_i^+)\subset U(b_j^-).                            \tag{4.2}
\]

For a perfect matching \(\alpha:[K]\to[K]\) in this graph, define a
directed graph \(D_\alpha\) on the marked fragment indices by

\[
 i\longrightarrow h
 \quad\Longleftrightarrow\quad
 L(a_h^-)\subset U(b_{\alpha(i)}^+).                  \tag{4.3}
\]

### Theorem 4.1 (oriented ladder equivalence)

There is a Hamilton-compatible port matching if and only if one can choose
fragment orientations, an entry perfect matching \(\alpha\), and a directed
Hamilton cycle \(\pi\) in \(D_\alpha\).

For these data the seams are

\[
 a_i^+b_{\alpha(i)}^-,
 \qquad
 b_{\alpha(i)}^+a_{\pi(i)}^-
 \quad(1\le i\le K).                                  \tag{4.4}
\]

More generally, the cycles of the resulting factor are exactly the cycles
of the permutation \(\pi\).

#### Proof

The two families in (4.4) use every marked and unmarked port exactly once,
so they are a perfect matching.  Traverse \(A_i\) in its orientation, take
the first seam to \(B_{\alpha(i)}\), traverse that fragment, and take the
second seam to \(A_{\pi(i)}\).  Thus contracted factor components are
exactly permutation cycles of \(\pi\).

Conversely, orient a connected factor cycle and orient each retained
fragment in the direction in which the cycle traverses it.  Every marked
fragment is followed by a unique unmarked fragment, defining the bijection
\(\alpha\).  That unmarked fragment is followed by a unique marked
fragment, defining a single-cycle permutation \(\pi\).  All seams belong
to \(G\), so (4.2)--(4.3) hold. \(\square\)

Theorem 4.1 isolates the extra topology after ordinary containment Hall:
one must choose the entry matching so that its exit digraph has a directed
Hamilton cycle.

## 5. A constructive paired-fragment insertion theorem

The next theorem gives a certificate smaller than the full subtour family.

### Theorem 5.1 (three-seam ear insertion)

Suppose a set of marked and unmarked fragments has already been joined by a
perfect port matching into one cycle.  Let \(ab\) be one selected seam, with
\(a\in{\cal A}\), \(b\in{\cal B}\).  Let new fragments have oriented ports

\[
 A_*=(a_*^-,a_*^+),\qquad B_*=(b_*^-,b_*^+).          \tag{5.1}
\]

If the three literal containments

\[
 L(a)\subset U(b_*^-),\qquad
 L(a_*^-)\subset U(b_*^+),\qquad
 L(a_*^+)\subset U(b)                                \tag{5.2}
\]

hold, replace \(ab\) by

\[
             ab_*^-,\qquad a_*^-b_*^+,\qquad a_*^+b. \tag{5.3}
\]

Assume also that the three displayed physical seams are distinct and do not
duplicate a retained physical edge.  The enlarged matching is perfect and
its union with all fragment pairings is again one cycle.  Under EC3 this
physical-simplicity condition is automatic for distinct occurrence ports.

#### Proof

Deleting \(ab\) opens the old cycle into one path with endpoints \(a,b\).
The inserted chain is

\[
 a-b_*^--P_{\cal B}-b_*^+-a_*^-
 -P_{\cal A}-a_*^+-b.                                \tag{5.4}
\]

Every old port other than \(a,b\) is unchanged; \(a,b\) are used once in
(5.3), and every new port is used once.  Thus the new seams form a perfect
matching.  Equation (5.4) closes the old path through both new fragments
and gives one cycle. \(\square\)

### Corollary 5.2 (ear-decomposable cut certificate)

Assume one marked/unmarked fragment pair has a compatible two-seam cycle.
If the remaining \(K-1\) marked and unmarked fragments can be paired,
oriented and ordered so that Theorem 5.1 applies successively, then the
final port matching is Hamilton-compatible.

This is a literal cut-selection target: every induction step asks for only
the three containments in (5.2), while the endpoint-complement palette
conditions are checked globally once.  It is sufficient, not necessary;
a Hamilton factor need not admit this paired-ear elimination order.

## 6. Protected component-transversal socket ears

Fix a perfect matching \(M_0\).  Its selected rungs are occurrence-labelled
edges

\[
                         e=(a_e,b_e).                 \tag{6.1}
\]

Define the socket digraph on these rungs by

\[
 e\longrightarrow f
 \quad\Longleftrightarrow\quad
 a_f b_e\in G
 \quad\Longleftrightarrow\quad
 L(a_f)\subset U(b_e).                                \tag{6.2}
\]

### Theorem 6.1 (clean socket ear)

Let

\[
                 e_0\to e_1\to\cdots\to e_{\ell-1}\to e_0       \tag{6.3}
\]

be a directed simple cycle in the socket digraph.  Suppose the old rungs
\(e_i\) lie in \(\ell\) distinct components of \(F(M_0)\), and suppose the
new physical edges below are simple.  Replace

\[
 \{a_{e_i}b_{e_i}:0\le i<\ell\}
\quad\hbox{by}\quad
 \{a_{e_{i+1}}b_{e_i}:0\le i<\ell\},                 \tag{6.4}
\]

with indices modulo \(\ell\).  Then (6.4) is a perfect-matching exchange
and merges those \(\ell\) components into exactly one.

#### Proof

The directed-cycle condition makes every new edge legal.  Cyclic shifting
uses every selected marked port and every selected unmarked port once, so
the new edge set is a matching.

Deleting one old rung from each of the \(\ell\) distinct factor cycles
opens them into \(\ell\) paths from \(a_{e_i}\) to \(b_{e_i}\).  The shifted
rungs concatenate these paths in the cyclic order (6.3), producing one
cycle. \(\square\)

### Corollary 6.2 (one-shot necklace)

If (6.3) contains exactly one old rung from every component of \(F(M_0)\),
one switch Hamiltonizes the factor.

### Theorem 6.3 (fresh protected-ear hypertree)

Let the components of \(F(M_0)\) be \({\cal C}_1,\ldots,{\cal C}_c\).
Suppose there is a family \({\cal T}\) of socket cycles satisfying:

1. their port supports are pairwise disjoint;
2. every cycle is clean relative to the initial components, with component
   support \(S_T\subseteq\{{\cal C}_1,\ldots,{\cal C}_c\}\); and
3. the bipartite incidence graph with component vertices on one shore,
   ear vertices on the other, and incidences
   \({\cal C}_iT\) for \({\cal C}_i\in S_T\), is a tree spanning all
   \(c\) component vertices.

Then the ear switches can be ordered so that every switch is clean relative
to the current factor and the final factor is one cycle.

The exact component ledger is

\[
                         \sum_{T\in{\cal T}}(|S_T|-1)=c-1.        \tag{6.5}
\]

#### Proof

Root the incidence tree at one component vertex.  Process ear vertices
outward from the root.  When an ear is reached, its parent component vertex
already lies in the accumulated merged cycle, while all its child component
vertices still lie in distinct untouched cycles.  Pairwise disjoint port
supports ensure that every old rung required by the ear is still present.
Theorem 6.1 therefore merges the accumulated cycle with all those child
cycles.  Induction reaches every component.

The incidence tree has
\(\sum_T|S_T|\) edges and \(c+|{\cal T}|\) vertices.  Its tree identity is
exactly (6.5). \(\square\)

Within the class of fresh, old-supported, component-monotone switch
sequences in which every switch is clean relative to the current factor
and selects exactly one untouched \(M_0\)-rung from each current component
it meets, an ordered ear hypertree is also necessary: record the original
components met by every switch.  This converse does not cover a general
sequence which uses several old rungs from one current component or reuses
a newly created rung in a later switch.

If only clean C8 ears are admitted, every \(|S_T|=4\), so (6.5) forces

\[
                              c\equiv1\pmod3.          \tag{6.6}
\]

This is an arity restriction of the clean-C8 architecture.  It is not the
false universal assertion that every C8 changes component parity.

## 7. Boolean socket geometry

For a rung \(e=(a_e,b_e)\), abbreviate

\[
                         L_e=L(a_e),\qquad U_e=U(b_e). \tag{7.1}
\]

### Lemma 7.1 (Johnson-necklace normal form)

If \(e\ne f\), \(L_e\ne L_f\), and \(e\to f\), then

\[
                  |L_e\cap L_f|=m-1,\qquad
                  U_e=L_e\cup L_f.                   \tag{7.2}
\]

Consequently a simple socket cycle is a cyclic Johnson walk

\[
 L_{e_0},L_{e_1},\ldots,L_{e_{\ell-1}},L_{e_0},       \tag{7.3}
\]

and it requires, occurrence by occurrence,

\[
                         U_{e_i}=L_{e_i}\cup L_{e_{i+1}}.         \tag{7.4}
\]

#### Proof

The old rung gives \(L_e\subset U_e\), while \(e\to f\) gives
\(L_f\subset U_e\).  Two distinct \(m\)-subsets contained in one
\((m+1)\)-set have intersection size \(m-1\), and their union is the whole
\((m+1)\)-set. \(\square\)

### Lemma 7.2 (no nondegenerate physical C4)

Let \(L,L'\) be distinct \(m\)-sets and let \(U,U'\) be distinct
\((m+1)\)-sets.  It is impossible that all four containments

\[
                         L,L'\subset U,U'             \tag{7.5}
\]

hold.  If two occurrence tokens have \(U=U'\), swapping their token
assignments does not change the physical set of cross edges.

#### Proof

The union of the distinct \(m\)-sets in (7.5) has size at least \(m+1\),
while the intersection of the distinct \((m+1)\)-sets has size at most
\(m\).  Yet (7.5) would put the former inside the latter.  If \(U=U'\),
the two physical edges are determined only by their marked labels and the
common owner; exchanging occurrence tokens leaves that edge set
unchanged. \(\square\)

Thus a reciprocal C4 bank cannot be the scalable Boolean proof.  The
nondegenerate clean atoms begin with directed 3-cycles, giving C6 switches,
and continue with the C8/long Johnson necklaces of Lemma 7.1.

## 8. Literal protected version

The topology theorems above become protected theorems only with one of the
following explicit guard packages.

### Guard package A: frozen literal support

Choose a fixed edge support \(Q\subseteq F(M_0)\) such that:

1. for every required deeper target, \(Q\) contains the complete edge span
   of one literal interval witness which avoids the eventual word opening;
2. \(Q\) contains a corridor bank satisfying all hypotheses of a stated
   protected-residence theorem for every completion under consideration,
   including that theorem's required conditions on all new seam collars;
   and
3. every physical edge deleted at every step of the actual construction is
   outside \(Q\).  For a one-shot reference-to-final transformation this is
   equivalently

   \[
                         Q\subseteq F(M_0)\cap F(M_{\rm final}).   \tag{8.1}
   \]

Then every factor reached by the ear sequence contains every chosen witness
and corridor literally, and the cited protected-residence theorem supplies
the claimed residence conclusion.  This package is naturally applicable to
the explicit exchange sequence of Theorem 6.3.  For a direct construction
from Theorem 4.1 or Corollary 5.2, condition (8.1) is an additional
reference-to-final requirement; otherwise use package B.

### Guard package B: final replay

Alternatively require:

1. every deeper target has either a witness internal to one retained
   fragment or an explicitly listed suffix--whole-fragments--prefix witness
   in the final oriented order;
2. the exact product of the oriented fragment residence states and new seam
   collars is accepting, including cyclic closure; and
3. the eventual opening and common-cap compiler are replayed on the same
   physical chronology.

Under either package, also retain the endpoint-complement hypotheses:

* the \(2K\) marked labels are pairwise distinct and are exactly the missing
  unmarked lower colours;
* the marked internal forest has the complete tagged lower palette; and
* the unmarked internal lower colours are distinct.

### Theorem 8.1 (protected ear router)

Under EC1--EC3, let a Hamilton-compatible matching be given by Theorem 4.1,
Corollary 5.2 or Theorem 6.3.  Assume either package B, or package A with
every intermediate deletion avoiding \(Q\) (equivalently (8.1) for a
one-shot construction).  Then the matching produces one literal two-rail
cycle which:

1. has the complete lower-q1 palette exactly once;
2. preserves the complete immediate-upper multiplicity vector;
3. retains every selected deeper witness and residence corridor certified
   by the chosen guard package; and
4. is eligible for the separately stated opening/common-cap compiler.

#### Proof

The endpoint-complement theorem proves (1).  Every marked port label and
every unmarked occurrence is used once; the cross lower colour is the
marked label and the cross upper colour at \(b\) is \(z+U(b)\).  This proves
(2), independent of the matching.

Under package A no changed edge belongs to a chosen witness or corridor, so
the full physical path remains in the new factor.  Under package B the
literal final intervals and the exact DFA product are hypotheses.  This
proves (3).  The compiler is deliberately not inferred from topology,
giving (4). \(\square\)

Pairwise seam safety is not substituted for the cyclic residence product.
Likewise, an upper target having many old witnesses is not substituted for
one surviving literal occurrence.

## 9. Sharp Hall and endpoint-choice limitations

For the \(m=2\) split-switch instance, the port graph is the chordless C8

\[
 p_{23}-U_0-p_{13}-U_2-p_{14}-U_1-p_{24}-U_3-p_{23}. \tag{9.1}
\]

It satisfies

\[
 |N(X)|\ge |X|+1                                     \tag{9.2}
\]

for every nonempty proper subset \(X\) of its four marked ports.  It is
connected and every edge belongs to a perfect matching.  Nevertheless its
two perfect matchings both give two factor cycles.

The socket digraph has a directed four-cycle, but its old rungs alternate
between the two factor components.  Its component word is \(ABAB\), so it
is not component-transversal; toggling it gives \(2\to2\).

Even the local endpoint sides are forced in this fixed hosting.  The two
unmatched blocks already supply marked lower colours \(3,4\).  To complete
\(\{1,2,3,4\}\), the hosted sets \(13,24\) must both retain endpoint \(12\),
supplying colours \(1,2\).  Hence the alternative split sides cannot repair
the topology.

This proves simultaneously:

* strict Hall is insufficient;
* matching-coveredness is insufficient;
* socket strong connectivity is insufficient;
* choosing split sides after fixing these hosts is insufficient; and
* marked upper q1 is not the obstruction.

The obstruction is the relative interlacing of \(P\) and the available
matchings.

## 10. Why no general Hall or two-matroid theorem is expected

Let \(H\) be any balanced bipartite graph with \(K\) vertices on each shore.
Replace every vertex by a paired pair of ports, and put all four port edges
between two pairs exactly when the corresponding vertices are adjacent in
\(H\).  Pair the two ports inside every blown-up vertex.

For \(K\ge2\), this port instance has a Hamilton-compatible perfect matching
if and only if \(H\) has a spanning alternating cycle.

Indeed, a spanning cycle in \(H\) assigns its two incident edges to the two
ports at every vertex.  Conversely, contracting the fixed port pairs in a
connected solution gives a connected degree-two spanning multigraph
supported on \(H\).  With at least four contracted vertices it cannot use a
parallel two-cycle, so it is a spanning cycle of \(H\).

Thus the arbitrary port problem already contains the full bipartite
Hamilton-cycle problem.  The Boolean rank structure, protected PBBS
chronology and explicit ear certificates are substantive extra hypotheses;
ordinary Hall cannot replace them.

## 11. Exact remaining Catalan theorem

The split-switch theorem supplies EC1--EC3 and one perfect matching only
when its signed colour/endpoint system is feasible.  Connectivity now has a
strictly sharper constructive target.

> **Protected Catalan port-ear existence lemma.**  For every required
> dimension, choose the saturating rails, hosts, cut endpoints and
> orientations so that:
>
> 1. the endpoint-complement lower-palette equations hold with distinct
>    marked labels;
> 2. the chosen fragments carry a literal all-depth witness/corridor guard;
> 3. their Boolean containment ports admit either the paired insertion
>    certificate of Corollary 5.2 or the component-transversal ear
>    hypertree of Theorem 6.3; and
> 4. the resulting oriented cycle passes the exact residence product,
>    opening and common-cap compiler.

Theorem 8.1 proves that this lemma is sufficient for the two-rail
connectivity/protection interface.  The \(m=2\) example proves that neither
the cap-two injection, the lower-rainbow split matching, strict Hall nor
marked upper-q1 can imply clause 3.  No unconditional PBBS/Pascal
construction of clauses 2--4 is claimed here.
