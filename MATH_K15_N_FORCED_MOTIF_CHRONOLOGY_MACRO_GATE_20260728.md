# k=15 forced-motif chronology: exact contraction, residence automata, and the polynomial macro boundary

Date: 2026-07-28

Method: pure mathematics.  No new finite search, solver run, or web input is
used.  The numerical data quoted in Sections 8--9 are read from the frozen
audited k=15 artifacts.

## 0. Outcome

Put

\[
 V=\binom{[15]}8,\qquad W=|V|=6435.
\]

Let \(P_1,\ldots,P_p\) be parent Hamilton paths on \(V\), let \(A\) be
the union of their directed successor arcs, and let \(F\subseteq A\) be
the arcs forced by selected local compiler-target motifs.

This note proves the following exact boundary.

1. **A completely selected successor set is easy to certify.**  It is one
   residence-safe Hamilton path if and only if it has the exact path degree
   profile, is acyclic, and its unique directed word is accepted by the
   last-three-insertions residence automaton.  This is linear time and is the
   sharp direct strengthening of degree compatibility.

2. **Partial extension contracts exactly to forced path fragments.**  If
   \(F\) has indegree and outdegree at most one, contains no directed cycle,
   and is internally residence-safe, then its components are fixed directed
   paths \(C_1,\ldots,C_r\).  Every Hamilton extension is exactly a
   permutation of these fragments joined by exposed parent arcs.

3. **There is no unrestricted arbitrary-digraph polynomial-time criterion
   unless \(P=NP\).**  The preceding fragment-ordering problem already
   contains directed Hamilton path when \(F\) is a single harmless forced
   prefix and there are no residence clauses.  This does not prove hardness
   under the special promise that the allowed arcs are the union of four
   individually Hamilton parents.

4. **There is an exact polynomial necessary-and-sufficient theorem on the
   acyclic quotient.**  Form the exposed successor digraph \(Q_F\) on the
   fragments.  If \(Q_F\) is acyclic, a residence-safe Hamilton extension
   exists if and only if the product of \(Q_F\) with the residence automaton
   has an accepting path using all \(r\) fragments.  Equivalently,
   \(Q_F\) has its unique topological order and the corresponding literal
   concatenation is residence-safe.  For four parents the quotient has at
   most \(4r\) arcs.

5. **SCC macro contraction is exact with one missing hypothesis.**  In a
   cyclic quotient, every Hamilton path traverses each strongly connected
   component contiguously.  If every SCC is supplied with its complete
   ingress/egress residence-transfer table for internal spanning paths, then
   extendability is decided by a polynomial layered dynamic program on the
   SCC condensation.  Producing that table for a large branching SCC is the
   residual Hamilton problem; strong connectivity alone is not a contraction
   certificate.

6. **There is a second genuinely polynomial escape.**  A mutually
   collar-disjoint family of certified two-break switches fuses the cycles of
   a parent cover according to its interaction forest.  It gives one
   Hamilton cycle exactly when the chosen switches form a spanning tree.
   With seven prescribed targets, witness selection followed by this test is
   polynomial of degree seven.  Whole alternating assignment cycles do not
   automatically satisfy the two-break hypothesis.

7. **The frozen Hall-29 seven-motif tuple is literally impossible.**  Its
   forced arcs contain

   \[
       30128\longrightarrow30001\longrightarrow30008.
   \]

   The first edge removes coordinate \(7\) and inserts coordinate \(0\);
   the next removes coordinate \(0\) and inserts coordinate \(3\).
   Coordinate \(0\) therefore has residence one.  No choice of seams,
   endpoints, parent arcs, or macro schedule can repair this forced internal
   violation.

8. **The fourth-parent catalogue solves local motif supply, not global
   extendability or Hall.**  Several single relabel parents contain interior
   witnesses for all seven Hall-29 zeros, and every one of the 28 p3-screened
   parents has a unique retained motif for each of targets \(5801\) and
   \(13620\).  When such a parent is assigned to witness those targets within
   the retained p3 catalogue, those two fragments should be forced and
   contracted first.
   The existing summaries do not contain the SCC, port-transfer, or
   precedence data needed by the theorem.

Thus there is no honest universal polynomial replacement for the current
Hamilton/subtour layer.  There is, however, an exact polynomial gate for the
acyclic or explicitly tabulated-macro regimes, and the Hall-29 diagnostic
tuple already fails that gate before any global topology calculation.

## 1. Directed Johnson words and the residence automaton

For a directed Johnson edge \(e=(u,v)\), write

\[
 a(e)\in u\setminus v,\qquad b(e)\in v\setminus u
\tag{1.1}
\]

for its deleted and inserted coordinates.  Coordinates are numbered
\(0,\ldots,14\), with coordinate \(i\) represented by \(2^i\).

The k=15 depth-three residence rule says:

> if coordinate \(b(e_i)\) is inserted at transition \(i\), it may not be
> deleted at any of transitions \(i+1,i+2,i+3\).

Equivalently, every forbidden residence word has between two and four
consecutive directed edges.

Let

\[
 \mathscr Q_3=\bigcup_{j=0}^{3}[15]^j
\]

be the raw ordered queue-state set, and add one rejecting state
\(\bot\).  Its crude size bound is

\[
 |\mathscr Q_3|
 \le 1+15+15^2+15^3=3616.
\tag{1.2}
\]

For \(q\in\mathscr Q_3\) and a Johnson edge \(e\), define

\[
 \delta(q,e)=
 \begin{cases}
   \bot,&a(e)\in q,\\
   \operatorname{suf}_3(q\,b(e)),&a(e)\notin q,
 \end{cases}
\tag{1.3}
\]

and \(\delta(\bot,e)=\bot\).  Here \(\operatorname{suf}_3\) retains the
last at most three entries.

### Lemma 1.1 (exact queue recognition)

A directed Johnson word is depth-three residence-safe if and only if its
edge word, read from the empty queue through (1.3), never reaches
\(\bot\).

#### Proof

Immediately before transition \(j\), the queue contains exactly the
coordinates inserted at transitions \(j-3,j-2,j-1\), omitting nonexistent
indices.  If \(a(e_j)\) is in the queue, it was inserted one, two, or three
transitions earlier and is now removed too soon.  Conversely, every
residence violation has precisely this form. \(\square\)

If one wants to recognize selected target motifs at the same time, take the
product with the deterministic prefix automaton for their finite edge words
and a seven-bit “seen target” mask.  Since seven is fixed at k=15, this
changes all running times only by a factor at most \(2^7\).

## 2. The fixed-successor criterion

First remove an ambiguity in the phrase “given parent successor arcs.”
Suppose a complete successor set \(S\subseteq A\) has already been selected,
rather than merely made available.

### Theorem 2.1 (linear-time exact chronology test)

The directed graph \((V,S)\) is one depth-three residence-safe Hamilton path
from prescribed start \(s\) to prescribed end \(t\) if and only if:

1. \(s\) has \((d^-,d^+)=(0,1)\), \(t\) has
   \((d^-,d^+)=(1,0)\), and every other vertex has
   \((d^-,d^+)=(1,1)\);
2. \((V,S)\) is acyclic; and
3. the unique directed word beginning at \(s\) is accepted by (1.3).

The condition is checkable in \(O(W+|S|)\) time.

#### Proof

Necessity is immediate.  Conversely, the degree profile makes every weak
component a directed path or directed cycle.  Acyclicity removes every cycle.
There is only one indegree-zero vertex and one outdegree-zero vertex, so only
one path component remains; it contains all \(W\) vertices.  Lemma 1.1 gives
residence safety. \(\square\)

Degree compatibility alone can miss subtours.  Under the exact degree profile
in Theorem 2.1, adding weak connectivity does remove them, but it still does
not detect a forced short residence word.

## 3. Exact forced-fragment contraction

Let \(\mathcal M\) be a selected family of target motifs.  Each motif is a
literal directed path in the parent-arc union \(A\).  Put

\[
 F=\bigcup_{M\in\mathcal M}E(M).
\tag{3.1}
\]

Endpoint motifs of type TL or TR prescribe the global first or last
fragment.

The following preliminary conditions are necessary:

\[
 d_F^+(v)\le1,\qquad d_F^-(v)\le1
 \qquad(v\in V);
\tag{3.2}
\]

\(F\) contains no directed cycle at all; all prescribed starts and ends are
consistent; and no directed component of \(F\) contains a residence
violation wholly inside its fixed edge word.  Equivalently, each component's
incoming-queue transfer relation is nonempty.  It need not accept every
incoming queue; exact boundary compatibility is retained in that transfer
relation and handled in Section 5.

Under (3.2) and acyclicity, the components of \(F\), with unused vertices
included as singleton components, are fixed directed paths

\[
 C_i=(c_{i,0},c_{i,1},\ldots,c_{i,\ell_i}),
 \qquad 1\le i\le r.
\tag{3.3}
\]

Write

\[
 h_i=c_{i,0},\qquad t_i=c_{i,\ell_i}.
\]

Discard every allowed arc entering an internal vertex of a nontrivial
fragment or leaving an internal vertex.  Also discard every arc entering a
prescribed global-start fragment or leaving a prescribed global-end
fragment.  Define the exposed successor
digraph \(Q_F\) on \([r]\) by

\[
 i\longrightarrow j
 \quad\Longleftrightarrow\quad
 i\ne j\ \hbox{ and }\ (t_i,h_j)\in A.
\tag{3.4}
\]

Parallel parent tags on the same literal arc may be retained as labels, but
they do not create different physical seams.  Since each parent has at most
one successor arc leaving \(t_i\),

\[
 |E(Q_F)|\le pr.
\tag{3.5}
\]

### Theorem 3.1 (forced-fragment bijection)

Hamilton paths in \(A\) which contain every arc of \(F\) are in bijection
with permutations \(\pi\in S_r\) such that

\[
 C_{\pi(1)}\longrightarrow C_{\pi(2)}
 \longrightarrow\cdots\longrightarrow C_{\pi(r)}
\tag{3.6}
\]

is a directed Hamilton path in \(Q_F\).  Under the bijection, residence
safety is exactly acceptance of the literal concatenated fragment-and-seam
word by (1.3).

#### Proof

Every internal vertex of \(C_i\) already has its forced predecessor and
successor.  A Hamilton path containing \(F\) must therefore traverse all of
\(C_i\) contiguously and in the displayed orientation.  The global path
orders the fragments and joins each exit \(t_i\) to the next entry \(h_j\),
giving (3.6).

Conversely, concatenate the pairwise vertex-disjoint fragment words using
the seams in (3.6).  Every vertex occurs once, every forced arc remains, and
the result is a Hamilton path.  Lemma 1.1 gives the final assertion.
\(\square\)

Theorem 3.1 is an exact macro contraction, but it has not yet made the
problem easy: directed Hamilton path in \(Q_F\) remains in the statement.

## 4. Why no unrestricted polynomial-time criterion exists

Let \(\operatorname{FMHP}(D,F,\mathcal R)\) ask whether a digraph \(D\)
has a Hamilton path containing a prescribed forced arc set \(F\) and
avoiding every supplied forbidden directed word in \(\mathcal R\).  The
k=15 residence problem is the specialization in which \(\mathcal R\)
contains the depth-three forbidden words.

### Theorem 4.1 (arbitrary-digraph complexity obstruction)

\(\operatorname{FMHP}\) is NP-complete even when:

1. \(F\) is one nonempty degree-compatible directed path;
2. \(F\) contains no directed cycle; and
3. there are no residence restrictions.

#### Proof

Membership in NP is immediate.  Start from an arbitrary directed Hamilton
path instance \(G=(U,E)\).  Add two new vertices \(s_0,s_1\), force

\[
 s_0\longrightarrow s_1,
\]

give \(s_0\) indegree zero, add every arc \(s_1\to u\) for \(u\in U\), and
retain the arcs \(E\).  Every Hamilton path of the new instance must begin
with the forced prefix \(s_0,s_1\); deleting it leaves a Hamilton path of
\(G\).  Conversely every Hamilton path of \(G\) extends by this prefix.
\(\square\)

The standard NP-completeness of directed Hamilton path is the only external
complexity input in this theorem.  This reduction does not prove hardness
under the stronger special promise “the arc set is a union of four paths
which are each Hamilton.”  It does prove that degree, blossom, connectivity,
and bounded-memory tests cannot form a universally sufficient
polynomial-time criterion.

There is nevertheless a polynomial-size exact integer formulation.  Adjoin
a dummy endpoint \(\star\), select arc variables \(x_e\in\{0,1\}\), impose
one incoming and one outgoing arc at every vertex of \(V+\star\), set
\(x_e=1\) for \(e\in F\), and impose

\[
 \sum_{e\in R}x_e\le |R|-1
\tag{4.1}
\]

for every forbidden residence path \(R\).  A single-commodity flow of
\(W\) units from \(\star\), with one unit consumed at each vertex of \(V\)
and capacity

\[
 0\le f_e\le W x_e,
\tag{4.2}
\]

forces the selected cycle cover to be one cycle.  Deleting \(\star\) gives
the Hamilton path.  This is a polynomial-size necessary-and-sufficient
integer criterion, not a polynomial-time algorithm; integrality is the hard
part.

## 5. The acyclic polynomial theorem

The exact tractable regime begins when the exposed quotient \(Q_F\) is
acyclic.

For an incoming queue state \(q\), let

\[
 \tau_i(q)
\]

be the state obtained by reading the internal edge word of \(C_i\), or
\(\bot\) if that word is unsafe from \(q\).  For a seam
\(e_{ij}=(t_i,h_j)\), define

\[
 T_{ij}(q)=\tau_j\bigl(\delta(q,e_{ij})\bigr).
\tag{5.1}
\]

### Theorem 5.1 (acyclic product-DAG criterion)

Assume \(Q_F\) is acyclic.  Then \(F\) extends to a residence-safe Hamilton
path if and only if the product state graph on pairs

\[
 (i,q),\qquad i\in[r],\ q\in\mathscr Q_3,
\]

has an accepting directed path whose projection uses \(r\) fragments.

Equivalently, in a topological order of \(Q_F\), set

\[
 D(i,q)=
 \max\{\hbox{number of fragments in a safe quotient path ending at }
        (i,q)\}.
\tag{5.2}
\]

Initialize with every permitted first fragment \(i\) for which
\(\tau_i(\varnothing)\ne\bot\), and update

\[
 D(j,T_{ij}(q))
 \ge D(i,q)+1
\tag{5.3}
\]

whenever \(i\to j\) and \(T_{ij}(q)\ne\bot\).  With prescribed endpoint
conditions,

\[
 \boxed{
 F\text{ extends residence-safely}
 \iff
 \max_{\text{permitted terminal }(i,q)}D(i,q)=r.}
\tag{5.4}
\]

#### Proof

A product-state path projects to a directed path in \(Q_F\).  Because
\(Q_F\) is acyclic, no fragment can repeat.  A projected path of length
\(r\) therefore uses every fragment exactly once.  The state transitions
are exactly the queue evolution of the literal concatenation, so Theorem
3.1 and Lemma 1.1 give a residence-safe Hamilton path.

Conversely, every desired extension orders all \(r\) fragments along a path
in \(Q_F\).  Reading its internal words and seams gives the corresponding
accepting product-state path, which is generated by (5.3). \(\square\)

For \(p=4\), the raw scale is

\[
 O\!\left(
 3616\bigl(r+|E(Q_F)|+\sum_i\ell_i\bigr)
 \right)
 =
 O(3616\,W),
\tag{5.5}
\]

up to deterministic word-processing factors.  If the seven target motifs
are not fixed in advance, include their seen-mask at an additional factor
\(2^7=128\).

### Corollary 5.2 (unique precedence order)

Before residence is imposed, an acyclic \(Q_F\) has a Hamilton path if and
only if it has a unique topological ordering.  In that case every consecutive
pair in the order is joined by a quotient arc, and scanning that one
concatenation through (1.3) decides residence.  Prescribed endpoints add the
requirement that this order begin and end with their fragments.

#### Proof

A Hamilton path in a DAG makes every earlier vertex reach every later one,
so every topological order is the path order.  Conversely, a DAG has a unique
topological order precisely when every two consecutive vertices in that
order are joined by an arc. \(\square\)

This gives a small literal obstruction certificate: Kahn's algorithm either
exposes two simultaneously available fragments, proving nonuniqueness, or
produces the one forced order.

### Corollary 5.3 (a sufficient reset regime where blossom is exact)

Let

\[
 \rho=\max\{|R|:R\text{ is a forbidden residence edge word}\}=4.
\]

Assume every fragment which can occur internally has at least
\(\rho-1=3\) internal arcs.  Filter each possible seam by its complete
suffix/seam/prefix residence collar, and let \(B_F\) be the bipartite graph
between fragment-exit and fragment-entry copies.

For prescribed start fragment \(s\) and end fragment \(t\), delete the
entry copy \(s_R\) and the exit copy \(t_L\).  If \(Q_F\) is acyclic, then
a residence-safe Hamilton extension with those endpoints exists if and only
if

\[
 \boxed{\nu\bigl(B_F-\{t_L,s_R\}\bigr)=r-1.}
\tag{5.6}
\]

#### Proof

A forbidden word of at most four edges cannot cross two seams: doing so
through an internal fragment \(C_i\) uses at least

\[
 1+\ell_i+1\ge5
\]

edges.  Hence internal safety plus the pairwise collar filter is exact in
this reset regime.
A matching gives every fragment indegree and outdegree at most one.
Acyclicity removes directed cycles.  A matching of \(r-1\) seams on \(r\)
fragments consequently gives one path component, and conversely every
Hamilton path gives such a matching. \(\square\)

The Hall-29 forced decomposition has thousands of singleton fragments, so
the length hypothesis fails.  Pairwise port compatibility is not exact
there: a four-edge forbidden word may cross several short-fragment seams.
The queue product in Theorem 5.1 is required.

## 6. SCC transfer tables: the exact macro-contraction theorem

For general \(Q_F\), let

\[
 S_1,\ldots,S_c
\]

be its strongly connected components, and let \(K\) be the condensation
DAG.

### Lemma 6.1 (SCC contiguity)

Every Hamilton path of \(Q_F\) visits all vertices of each \(S_\alpha\)
in one contiguous interval.  Its SCC order is a Hamilton path of \(K\).
Consequently \(K\) must have a unique topological ordering.

#### Proof

After a directed path leaves an SCC it cannot return: a return path would
make a directed cycle in the condensation.  A Hamilton path must therefore
finish the SCC before leaving it.  Contracting the contiguous intervals
gives a Hamilton path through \(K\), and Corollary 5.2 applies. \(\square\)

For an SCC \(S\), let \(\operatorname{Ent}(S)\) be the fragments of \(S\)
which can receive an inter-SCC seam (together with a dummy global ingress
when \(S\) is first), and define \(\operatorname{Exit}(S)\) dually.  Define
its complete transfer table

\[
 \mathcal T_S
 \subseteq
 (\operatorname{Ent}(S)\times\mathscr Q_3)
 \times
 (\operatorname{Exit}(S)\times\mathscr Q_3)
\tag{6.1}
\]

as follows.  A record \((i,q_{\rm in};j,q_{\rm out})\) belongs to
\(\mathcal T_S\) precisely when there is a literal directed path which:

1. starts with fragment \(i\), with queue \(q_{\rm in}\) immediately before
   reading \(i\)'s internal word;
2. visits every fragment of \(S\) exactly once;
3. ends after reading fragment \(j\), with queue \(q_{\rm out}\); and
4. is nonrejecting throughout.

The table consumes only the internal SCC traversal.  It does not consume
the incoming or outgoing inter-SCC seam.  Endpoint flags and target-seen
bits can be appended to each record.

### Theorem 6.2 (complete-table macro contraction)

Suppose every \(\mathcal T_{S_\alpha}\) is supplied completely.  Then the
original instance has a residence-safe Hamilton extension if and only if:

1. the condensation \(K\) has its unique topological order
   \(S_{\alpha_1},\ldots,S_{\alpha_c}\); and
2. the layered composition of the tables

   \[
   \mathcal T_{S_{\alpha_1}},
   \ E_{\alpha_1,\alpha_2},
   \ \mathcal T_{S_{\alpha_2}},\ldots,
   E_{\alpha_{c-1},\alpha_c},
   \ \mathcal T_{S_{\alpha_c}}
   \tag{6.2}
   \]

   has an accepting start-to-end state.

Here \(E_{\alpha,\beta}\) consumes exactly one literal inter-SCC seam and
updates the queue; dummy start/end relations impose the global endpoint
conditions.  Thus no boundary seam is processed twice.  The test is
polynomial in the total explicit table size.

#### Proof

Lemma 6.1 forces the SCC order and makes the restriction of a global
Hamilton path to each SCC one of its table records.  Its inter-SCC seams
give a state trail through (6.2).

Conversely, concatenate the literal internal spanning paths recorded by an
accepting trail through (6.2).  SCC supports are disjoint, the unique
condensation order visits every SCC once, and the stored queue transfers
prove residence across every boundary. \(\square\)

This theorem is polynomial and necessary-and-sufficient only because the
tables are explicit.  Computing a complete table for an unrestricted large
branching SCC is itself an internal Hamilton-selection problem and may be
exponential.  Theorem 4.1 proves hardness of unrestricted fragment ordering;
it does not, by itself, prove hardness under an additional
strong-connectivity promise.

Useful polynomial cases include:

1. every SCC is a singleton;
2. every nontrivial SCC is a directed simple cycle, whose table is obtained
   by testing its possible cuts;
3. SCC size is bounded; or
4. the branch core

   \[
   B(S)=\{v\in S:d_S^+(v)\ne1\ \hbox{or}\ d_S^-(v)\ne1\}
   \]

   has uniformly bounded size.

In Case 4, after choosing ingress and egress, transitions away from the
branch core are forced.  With at most \(p\) parent choices at a branch, the
crude complete enumeration bound

\[
 |S|^2p^{\,2|B(S)|}
\tag{6.3}
\]

is polynomial for fixed \(p\) and bounded \(|B(S)|\).

Strong connectivity by itself is not a macro certificate.  Replacing an SCC
by one unlabeled supervertex would forget its correlated ingress, egress, and
residence state and would make the theorem false.

## 7. A polynomial forest-fusion theorem

There is a different tractable class which uses the assignment-cycle idea
constructively.

Adjoin the dummy endpoint and let \(\sigma\) be a directed cycle cover which
is residence-safe also across every cyclic boundary.  A two-break switch
with distinct tails \(x,y\) replaces

\[
 x\to\sigma(x),\qquad y\to\sigma(y)
\]

by

\[
 x\to\sigma(y),\qquad y\to\sigma(x).
\tag{7.1}
\]

Assume every allowed switch has a certified complete radius-four physical
collar.  Assume also that the candidate switch catalogue is mutually
collar-disjoint in the strong sense: different switches use distinct tails
and successor heads, their complete old/new collars are disjoint, and each
collar certificate remains valid after all other selected switches are
applied.  Thus selected switches commute and cannot create a cross-switch
residence violation.

Let \(\Gamma\) have one vertex for each cycle of \(\sigma\), and one edge for
each switch whose two tails lie in the corresponding two distinct base
cycles.

### Theorem 7.1 (forest fusion)

For every forest \(T\subseteq E(\Gamma)\), applying the switches of \(T\)
leaves exactly

\[
 c(\sigma)-|T|
\tag{7.2}
\]

successor cycles, one for each connected component of \(\Gamma[T]\).
It gives one Hamilton cycle if and only if \(T\) is a spanning tree.

#### Proof

Order the forest edges so that each new edge joins two components formed by
the earlier edges.  Before its switch, its two tails lie in two distinct
current successor cycles.  Swapping their successors merges those cycles
into one and cannot split either.  Induction gives (7.2). \(\square\)

Hence a forced switch forest \(T_0\) extends to a Hamilton cycle if and only
if the allowed interaction graph remains connected after the components of
\(T_0\) are contracted.  This is a union-find/connectivity test.  Removing
the dummy gives the Hamilton path, subject to its endpoint collar.

If each of the seven Hall-29 targets has a finite family of labelled
certified switches, enumerate one witness per target, reject collar conflicts
and cycles, and apply Theorem 7.1.  The running time is

\[
 O(M^7\operatorname{poly}(W))
\]

when there are at most \(M\) choices per target, hence polynomial because
seven is fixed.

The hypotheses are substantive.  A whole alternating assignment cycle may
change many successors and may split as well as merge current cycles; it is
not automatically a two-break edge of \(\Gamma\).  Pairwise collar conflicts
among the remaining candidate switches would also turn the spanning-tree
extension into a constrained problem not covered by Theorem 7.1.

## 8. Literal application to the Hall-29 zero tuple

The source data are
scratch/k15_h29_zero7_minimal_tuple.json and
scratch/k15_hall29_zero_targets.json.

The frozen Hall-29 zero family is

\[
 \mathcal Z=
 \{2575,5801,13616,13620,17738,21641,29776\}.
\tag{8.1}
\]

The diagnostic minimum-novelty selection has 60 distinct forced arcs and
five directed components:

\[
\begin{array}{c|c|c|c}
\text{component}&\text{targets}&\text{type}&
(\text{first},\text{last};\text{ arc count})\\ \hline
A&2575&TL&(2479,23194;11)\\
B&5801,\ 21641&TR&(3383,22185;11)\\
C&13616&T&(25814,5479;9)\\
D&13620&T&(9683,29816;11)\\
E&29776,\ 17738&T&(32136,19599;18).
\end{array}
\tag{8.2}
\]

The two TR targets in \(B\) use the identical forced interval.  In \(E\),
the \(29776\) interval concatenates compatibly into the \(17738\) interval.
Thus the five components have \(60+5=65\) vertices.  Adding the other
\(6435-65=6370\) middle vertices as singleton fragments gives

\[
 r=6375.
\tag{8.3}
\]

The forced set is degree-compatible and acyclic.  Nevertheless it is
nonextendable for a two-edge literal reason.  Component \(C\) contains

\[
 30128\longrightarrow30001\longrightarrow30008.
\tag{8.4}
\]

Indeed,

\[
 30128-2^7+2^0=30001,
\qquad
 30001-2^0+2^3=30008.
\tag{8.5}
\]

The first transition inserts coordinate \(0\); the next transition removes
it.  Starting immediately before (8.4), the queue transition is

\[
 q\longmapsto\operatorname{suf}_3(q,0)
 \longmapsto\bot.
\]

Therefore the internal transfer relation \(\tau_C\) is empty for every
incoming queue state.  This proves:

### Corollary 8.1 (Hall-29 tuple obstruction)

The diagnostic Hall-29 seven-motif tuple has no residence-safe Hamilton
extension in any successor catalogue containing it.  This remains true
after arbitrary endpoint choices, seams, parent additions, SCC contractions,
or event-precedence macro contractions.

The frozen audit's count of 23 selected residence-forbidden motifs is
consistent with this conclusion, but is not needed for the proof.

## 9. What the fourth-parent catalogue does and does not prove

The source summaries are scratch/fourth_parent_analytic_screen.json and
scratch/fourth_parent_p3_screen.json.

Order the count vectors by the targets in (8.1).  The analytic screen
contains, among others, the following four single-transposition parents:

\[
\begin{array}{c|c|c}
\text{parent}&\text{interior motif counts}&\text{total}\\ \hline
t10\_11&(4,1,2,1,3,3,3)&17\\
t1\_12 &(4,1,4,1,2,1,3)&16\\
t3\_4  &(3,1,2,1,3,2,2)&14\\
t3\_13 &(1,1,2,1,2,1,4)&12.
\end{array}
\tag{9.1}
\]

Each row is one coordinate relabelling of the Hall-29 Hamilton carrier.
Consequently all its listed motifs occur simultaneously as literal
subintervals of one already residence-safe Hamilton path.  This proves
parent-coherent chronology and residence supply for the old seven target
labels.  It does **not** prove seven distinct compiler-cell owners, a Hall
matching, or Hall zero.

Relabelling transports the entire Hall-29 obstruction as well.  For example,
the \(t1\_12\) parent transports the seven-zero family to

\[
 \{1707,6669,9522,9526,17547,21832,25682\}.
\tag{9.2}
\]

Using the fourth parent wholesale therefore retains deficiency 29 and merely
moves its obstructing block.  A mixed carrier must retain witnesses for the
old and transported obligations unless the mixing changes the DM block
itself.

Every one of the 28 parents retained in the p3 screen has second and fourth
count equal to one.  Hence it has a unique retained interior motif for target
\(5801\) and a unique retained interior motif for target \(13620\).  In any
mixed search using that parent to serve these targets, those two literal
fragments are forced and should be contracted before any subtour or Hall
model is built.

The existing analytic and p3 summaries record motif counts, new-arc totals,
and static DM-neighbourhood totals.  They do not record:

1. parent-tagged motif interval order;
2. the union \(F\) for a joint motif selection;
3. the SCC decomposition and unique-order status of \(Q_F\);
4. SCC ingress/egress queue-transfer tables;
5. cross-macro collar conflicts; or
6. a matching of the selected motifs to distinct compiler cells.

Therefore static positivity of all seven coordinates is rigorously
insufficient for mixed-parent extendability.

### Exact next catalogue audit

For every proposed fourth parent:

1. force its unique \(5801\) and \(13620\) intervals;
2. select alternatives for the other five targets;
3. reject (3.2), every forced cycle, endpoint conflict, and every forced
   queue rejection;
4. contract the surviving forced paths;
5. build \(Q_F\) with parent labels;
6. if \(Q_F\) is acyclic, apply Theorem 5.1;
7. otherwise compute the SCC condensation and either provide the complete
   tables of Theorem 6.2 or expose the large branching SCC which remains;
8. use Theorem 7.1 only for assignment components proved to be
   collar-disjoint two-break mergers; and
9. only after a Hamilton/residence extension survives, audit upper shadows,
   distinct compiler owners, and the full DM neighbourhood.

This order prevents local motif supply from being mistaken for a coherent
chronology.

## 10. Primitive switch precedence versus final successor topology

There are two different DAG gates.

1. The **successor quotient** \(Q_F\) asks whether the final selected carrier
   can be one Hamilton path.
2. The **switch-event precedence graph** asks whether a chosen carrier can
   be reached from a parent by a sequential history of exact switches.

A final carrier can be specified and verified directly, in which case only
the first gate is logically needed.  If a proof uses primitive switches,
then complete output-input state equalities impose the event-precedence
arcs.

### Theorem 10.1 (certified event-macro contraction)

Fix selected literal switch events and their complete local state trails.
Assume:

1. every source row with no declared predecessor occurs exactly once in one
   common initial exact factor, and the untouched exterior is fixed;
2. every noninitial source row is produced by a unique predecessor target
   equal to it as a complete state;
3. every state occurrence is consumed and produced at most once;
4. unmatched final target rows are mutually owner-disjoint and disjoint from
   the untouched exterior;
5. events incomparable in the resulting precedence relation act on disjoint
   row occurrences, or are certified to commute; and
6. every event separately preserves the exact owner/target ledgers and
   residence constraints.

Under these hypotheses, a sequential primitive history exists if and only if
the event-precedence digraph is acyclic.

More generally, contract a pairwise boundary-disjoint family of event SCCs
only when each SCC has a literal simultaneous-macro certificate: its internal
states cancel, its boundary source rows occur in one exact factor, its target
rows preserve the exact owner/target ledgers, and its physical endpoint
replacement is residence-safe.  The same unique-consumption,
unique-production, final-disjointness, and commutation hypotheses are imposed
on the exposed macro boundary states.  Execution by those atomic macros
exists if and only if the contracted precedence graph is acyclic.

#### Proof

Without contractions this is the topological-scheduling theorem: every local
successor state forces its event order, and every topological order is
executable by induction.

For a certified SCC macro, simultaneous replacement realizes all internal
dependencies atomically and exposes only its boundary states.  Contracting
it therefore preserves exactly the external precedence relations.  The same
topological induction applies to the quotient.  Conversely, every atomic
execution order induces an acyclic order of the quotient. \(\square\)

Strong connectivity alone is never enough: blindly contracting every SCC
would make every condensation acyclic and erase the circular-wait
obstruction.  Likewise, event-precedence acyclicity does not prove that the
final successor set is Hamilton; Theorems 3.1, 5.1, or 6.2 remain necessary.

## 11. Exact proved and open boundary

Proved here:

1. the exact last-three-insertions automaton;
2. the linear-time criterion for a fully selected successor set;
3. the exact forced-fragment contraction;
4. NP-completeness of unrestricted arbitrary-digraph partial extension;
5. the acyclic product-DAG necessary-and-sufficient theorem;
6. the sufficient three-internal-arc reset condition under which pairwise
   collar-filtered blossom becomes exact;
7. the complete-SCC-table macro theorem;
8. the collar-disjoint forest-fusion theorem;
9. the literal residence-one obstruction (8.4)--(8.5) to the frozen
   Hall-29 tuple; and
10. the precise information still missing from the four-parent summaries.

Not proved here:

1. that any mixed four-parent \(Q_F\) is acyclic;
2. complete transfer tables for any large branching SCC in that union;
3. that its alternating assignment components are collar-disjoint
   cycle-merging two-breaks;
4. a joint distinct-cell matching for the old and transported Hall blocks;
5. Hall deficiency zero; or
6. \(\nu(15)=6438\).

The rigorous polynomial lane is now sharply identified:

\[
\boxed{
\text{forced-motif contraction}
\;+\;
\text{residence automaton}
\;+\;
\begin{cases}
\text{acyclic quotient},\\
\text{complete SCC transfer tables},\\
\text{or certified collar-disjoint forest fusion}
\end{cases}}
\]

Beyond those regimes, the remaining object is the genuine Hamilton-selection
core rather than a missing degree or Hall relaxation.

## 12. Independent audit record

An independent adversarial audit checked the residence off-by-one,
\(3616\)-state bound, fixed-successor theorem, forced-fragment bijection,
product-DAG criterion, SCC contiguity, Hall-29 mask arithmetic, five-component
ledger, and transported target family.  Its scope corrections have been
incorporated:

1. residence transfer is state-dependent rather than universally safe at a
   fragment boundary;
2. the complexity theorem is restricted to arbitrary allowed digraphs;
3. prescribed endpoints are built into the blossom minor in (5.6);
4. the three-arc condition is stated as a sufficient reset regime;
5. inter-SCC seams are consumed only by the relations \(E_{\alpha,\beta}\);
6. forest fusion uses the strong mutually collar-disjoint hypothesis; and
7. event-precedence sufficiency assumes a linear, uniquely produced and
   consumed complete-state system.
