# The exact hypergraph and flow form of the directed Catalan repair gate

Date: 2026-07-31  
Status: exact reductions and a proved peelability criterion; the all-\(m\)
construction of a peelable repair core remains open

## 1. Directed data

Use the notation of
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`.
Thus

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m=\frac Nm,
\]

and

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0
\]

is a saturating cycle.  Put

\[
 \mathcal E=\binom{[2m]}m\setminus\{C_i:i\in\mathbb Z_N\},
 \qquad
 \mathcal L=\binom{[2m]}{m-1},
\]

and define the base and directed replacement colours

\[
 b_i=C_i\cap C_{i+1},
 \qquad
 t_i(X)=X\cap C_{i+1}\quad(X\subset U_i).
 \tag{1.1}
\]

The directed repair problem is to injectively host every
\(X\in\mathcal E\) at an index \(i\) with \(X\subset U_i\), so that

\[
 \{b_i:i\notin\operatorname{im}\phi\}
 \sqcup
 \{t_i(X):\phi(X)=U_i\}
 =\mathcal L.
 \tag{1.2}
\]

### Lemma 1.1 (all three marginal matchings are free)

If the replacement colour is ignored, \(\mathcal E\) has an injective
matching to host blocks, with the stronger expansion
\[
 |N_{\rm host}(\mathcal A)|
   \ge \frac m{m-1}|\mathcal A|
 \qquad(\mathcal A\subseteq\mathcal E).                     \tag{1.3}
\]
Indeed, every omitted \(m\)-set lies in exactly \(m\) rank-\((m+1)\)
sets, whereas a block \(U_i\) contains at most \(m-1\) omitted facets:
two of its \(m+1\) facets are the distinct seams \(C_i,C_{i+1}\).
Double-count incidences and apply Hall.

Independently, \(\mathcal E\) has a matching to distinct lower facets.
This is the following small-family consequence of Kruskal--Katona: every
\(\mathcal A\subseteq\mathcal E\), with
\(|\mathcal A|\le K=\operatorname{Cat}_m\), satisfies
\[
                         |\partial^-\mathcal A|\ge|\mathcal A|.
 \tag{1.4}
\]
Indeed write \(|\mathcal A|=\binom{x}{m}\) with real \(x\ge m\).
Since
\[
 K=\frac1{m+1}\binom{2m}{m}
   <\binom{2m-1}{m},
\]
we have \(x<2m-1\).  The Lovasz form of Kruskal--Katona gives
\[
 |\partial^-\mathcal A|
   \ge\binom{x}{m-1}
   =\binom{x}{m}\frac{m}{x-m+1}
   >|\mathcal A|.
\]
The weak form (1.4) is all that Hall needs.

Finally, after any injective host set \(H\subsetneq\mathbb Z_N\) is
chosen, its block edges \(\{C_i,C_{i+1}\}\), \(i\in H\), have an SDR of
seam endpoints.  Every proper edge-subgraph of a cycle is a disjoint
union of paths, and every collection of \(r\) such edges has at least
\(r\) incident vertices.

Thus host assignment, lower-shadow assignment, and cut-port assignment
all satisfy Hall separately.  The only obstruction is their coupling by
the literal relation \(t_i(X)=X\cap C_{i+1}\), exactly the three-partite
gate below.

## 2. Exact three-partite formulation

Let \(I=\mathbb Z_N\), and introduce a set \(\mathcal D_0\) of \(N-K\)
formal dummy tokens.  Define a three-partite, three-uniform hypergraph

\[
 \mathscr H\quad\text{on}\quad
 I\sqcup\mathcal L\sqcup(\mathcal E\sqcup\mathcal D_0)
\]

with hyperedges

\[
 \{i,b_i,d\}
 \quad(i\in I,\ d\in\mathcal D_0)
 \tag{2.1}
\]

and

\[
 \{i,t_i(X),X\}
 \quad(X\in\mathcal E,\ X\subset U_i).
 \tag{2.2}
\]

### Theorem 2.1 (perfect-matching equivalence)

The directed replacement identity (1.2) holds if and only if
\(\mathscr H\) has a perfect matching.

#### Proof

Given (1.2), use the repair hyperedge (2.2) at every hosted index.  The
remaining \(N-K\) indices have pairwise distinct base colours, namely the
unused members of \(\mathcal L\).  Match those indices arbitrarily to the
\(N-K\) dummy tokens using (2.1).  This is a perfect matching.

Conversely, every perfect matching covers every \(X\in\mathcal E\) once,
so its \(K\) repair edges give distinct hosts.  It covers all dummy tokens,
so the other \(N-K\) blocks use base edges.  Coverage of the colour part
\(\mathcal L\) is exactly the disjoint-union identity (1.2). \(\square\)

This is a genuine three-dimensional matching problem.  It is not the
intersection of only two partition matroids; generic pairwise Hall
conditions therefore do not suffice.

### Corollary 2.2 (two-stage exact form)

The gate holds if and only if there is a set \(S\subseteq I\),
\(|S|=N-K\), such that

1. the base colours \(\{b_i:i\in S\}\) are distinct; and
2. writing
   \[
      H=I\setminus S,
      \qquad
      Y=\mathcal L\setminus\{b_i:i\in S\},
   \]
   the three-partite hypergraph on \(\mathcal E\sqcup H\sqcup Y\) with
   edges
   \[
      \{X,i,t_i(X)\}: X\subset U_i, i\in H, t_i(X)\in Y
   \]
   has a perfect matching.

In particular,

\[
                  |\{b_i:i\in I\}|\ge N-K                 \tag{2.3}
\]

is the first unavoidable deficiency test.

### Corollary 2.3 (cap-two tight-enumeration equivalence)

Let \(P\) be the cap-two Hamilton cycle on all \(M\) rank-\(m\) sets
obtained by inserting the omitted facets into distinct upper blocks.
In every unmatched block distinguish its sole edge, and in every matched
block distinguish the outgoing edge \(X C_{i+1}\).  Then (1.2) holds if
and only if subdividing the \(N\) distinguished edges by their
rank-\((m-1)\) intersections gives a tight enumeration of the two levels
\(\binom{[2m]}{m-1}\cup\binom{[2m]}m\).

#### Proof

Under (1.2), the distinguished intersections are exactly all \(N\)
rank-\((m-1)\) sets.  Subdivision therefore lists every vertex on the two
levels once.  The \(N\) subdivided edges contribute two one-bit flips
each, and the other \(M-N=K\) Johnson edges contribute two flips each.
The total is

\[
 2N+2(M-N)=2M
   =(M+N)+(M-N),
\]

which is exactly the tight-enumeration budget.

Conversely, consider any tight enumeration of these two levels.  In its
cyclic level-type word, every same-level step costs at least two flips and
every cross-level step at least one.  Since the middle level has \(M-N\)
more vertices, there are at least \(M-N\) same-level steps.  Equality in
the tight budget forces exactly \(M-N\) middle--middle Johnson steps, no
lower--lower step, and all cross steps to be containment edges.  Hence
every lower vertex subdivides one edge of the projected middle Hamilton
cycle.  If the subdivided edges are the distinguished block-transversal
edges above, their intersections give (1.2). \(\square\)

Thus the missing directed matching is precisely a **common refinement**
of two known marginal objects: a tight enumeration on the lower side and
a cap-two Catalan compression on the upper side.  The separate existence
theorems do not supply a common middle projection.

### Corollary 2.4 (three-level diamond normal form)

The same data canonically give a tight enumeration of all three levels
\[
 \binom{[2m]}{m-1}\cup\binom{[2m]}m\cup\binom{[2m]}{m+1}.
\]

Indeed, distinguish one upper edge in every cap-two block: in an unmatched
block use its sole edge, while in a matched block use the incoming edge
\(C_iX\).  The lower distinguished edges are those of Corollary 2.3:
the same sole edge in an unmatched block and the outgoing edge
\(XC_{i+1}\) in a matched block.  These two transversals have sizes \(N,N\),
their union is all \(M=N+K\) edges of \(P\), and their intersection is the
\(N-K\) unmatched edges.

On an edge selected only below, insert its lower intersection; on an edge
selected only above, insert its upper union.  On an unmatched edge,
selected on both sides, replace \(A,B\) by
\[
                A,\ A\cap B,\ A\cup B,\ B.                  \tag{2.4}
\]
The middle step in (2.4) has Hamming distance two.  Every lower and upper
vertex appears exactly once.  The total flip count is
\[
 2\bigl(M-(N-K)\bigr)+4(N-K)=4N,
\]
which equals the three-level tight budget
\[
 (M+2N)+(2N-M)=4N.
\]

Thus directed Catalan repair is a rigid **diamond-tight refinement** of
the published three-level tight-enumeration theorem.

This qualification is load-bearing.  The Gregor--Mütze trimming
construction for a three-level interval explicitly makes every
distance-two step stay *within one boundary level*, never between levels
\(m-1\) and \(m+1\).  The diamond step (2.4) is of the latter type.
Consequently their theorem proves the correct total-distance statement
but not this normal form.  A proof still needs a transformation from
same-boundary jumps to compatible lower--upper diamonds, or a new
construction producing diamonds directly.

Reference: P. Gregor and T. Mütze, *Trimming and Gluing Gray Codes*,
Theorem 8(ii) and its proof, especially the statement that the trimmed
distance-two steps remain inside levels \(k\) and \(l\):
<https://drops.dagstuhl.de/storage/00lipics/lipics-vol066-stacs2017/LIPIcs.STACS.2017.40/LIPIcs.STACS.2017.40.pdf>.

### Corollary 2.5 (complementary triple-window form)

Put \(V_i=[2m]\setminus U_i\), a Hamilton cycle through all
rank-\((m-1)\) sets, and put
\[
 A_i=[2m]\setminus C_i=V_{i-1}\cup V_i.
\]
The \(A_i\) are \(N\) distinct rank-\(m\) sets, and
\(\{[2m]\setminus X:X\in\mathcal E\}\) is precisely their Catalan-sized
leave.  Moreover
\[
 [2m]\setminus b_i=A_i\cup A_{i+1}
      =V_{i-1}\cup V_i\cup V_{i+1},                         \tag{2.5}
\]
and, for \(X\subset U_i\),
\[
 [2m]\setminus t_i(X)
      =([2m]\setminus X)\cup A_{i+1}.                       \tag{2.6}
\]

Hence directed repair has the following equivalent upper-shadow form:
insert the \(K\) omitted rank-\(m\) sets into distinct blocks of the
\(A\)-cycle so that the retained outgoing adjacent unions enumerate every
rank-\((m+1)\) set exactly once.  In particular, the floor invariant of
Section 4 is a \(0/1/2\) law for the triple-window unions of the
rank-\((m-1)\) Gray cycle \(V\).  This is the coordinate in which a
Greene--Kleitman or first-return Catalan recursion would have to preserve
unitriangularity.

### Corollary 2.6 (intrinsic level-word characterization)

Let \(\mathcal T\) be any tight cyclic enumeration of the three levels
\(m-1,m,m+1\), and erase its outer-level vertices while retaining the
cyclic order of the rank-\(m\) vertices.  Then \(\mathcal T\) is in the
diamond normal form of Corollary 2.4 if and only if

1. every open interval between consecutive rank-\(m\) vertices contains
   either one or two outer vertices;
2. an interval containing two outer vertices contains one vertex of each
   outer rank; and
3. all successive distances attain their rank-forced minima (one across
   adjacent ranks and two between the two outer ranks); and
4. the upper unions of the \(K\) middle edges carrying a lower-only
   interval are pairwise distinct and are exactly the upper vertices in
   the \(K\) upper-only intervals.

Under these conditions the erased middle order is a Johnson Hamilton
cycle, and the numbers of lower-only, upper-only, and diamond intervals
are respectively
\[
                         K,\quad K,\quad N-K.               \tag{2.7}
\]

#### Proof

There are \(M+2N\) steps.  If \(s\) joins two vertices on the same parity
shore of the cube, the flip length is at least \(M+2N+s\).  Since the
outer shore has \(2N\) vertices and the middle shore only \(M\), every
cyclic level word has at least \(2N-M=N-K\) same-shore adjacencies.
Tightness forces equality throughout: there is no middle--middle
adjacency, there are exactly \(N-K\) outer--outer adjacencies, and every
step has the minimum distance allowed by its endpoint ranks.

Conditions 1 and 2 now say that the outer block between two consecutive
middle vertices is lower-only, upper-only, or a mixed pair.  A singleton
lower vertex is the intersection of its two middle neighbours, and a
singleton upper vertex is their union.  In a mixed pair \(L,U\), the
distance-two condition gives \(L\subset U\) and \(|U\setminus L|=2\).
The two flanking middle vertices are therefore the two distinct
intermediate \(m\)-sets of this Boolean diamond.  This is exactly (2.4),
up to reversing the local order of \(L,U\).

If the three interval counts are \(a,b,c\), then
\[
 a+c=N,\qquad b+c=N,\qquad a+b+c=M.
\]
Thus \(c=2N-M=N-K\) and \(a=b=M-N=K\), proving (2.7).  The converse is
now local except for block-complementarity.  Condition 4 says precisely
that the induced middle cycle has cap-two upper
loads and that the two occurrences at every duplicated upper colour are
split between the lower and upper transversals.  It supplies the
block-complementarity used in Corollary 2.4.  Reading that construction
backwards proves the converse. \(\square\)

This makes the missing normal form exact.  A generic tight enumeration
can fail it by having a longer outer run, a same-rank outer jump, or the
wrong unlisted union colours; the total flip budget alone forbids none of
these phenomena.

Condition 4 is genuinely independent of the level word.  The finite
replay in
`MATH_AUDIT_CATALAN_COLOUR_INCIDENCE_GRAPH_AND_DIAMOND_NORMAL_FORM_20260731.md`
contains an \(m=3\) tight listing with exactly ten mixed diamonds, five
lower-only intervals, and five upper-only intervals, but its selected
lower and upper edges hit one upper block twice and another zero times.
Thus the projection-only version of Corollary 2.6 is false.

## 3. Exact transshipment form

Regard every selected repair at \(i\) as the directed, occurrence-labelled
arc

\[
                         b_i\longrightarrow t_i(X).          \tag{3.1}
\]

Write \(a(y)=|\{i:b_i=y\}|\) for the base load.  If \(Q\) is a set of
repair arcs using every \(X\in\mathcal E\) once and every host at most
once, then (1.2) is equivalent to

\[
 \boxed{
   \operatorname{out}_Q(y)-\operatorname{in}_Q(y)=a(y)-1
   \quad\text{for every }y\in\mathcal L.
 }
 \tag{3.2}
\]

Indeed the final load at \(y\) is
\(a(y)-\operatorname{out}_Q(y)+\operatorname{in}_Q(y)\).

Consequently every solution decomposes, after cancelling directed cycles,
into paths from excess base colours \(a(y)>1\) to holes \(a(y)=0\).
Intermediate colours of load one are exactly the internal vertices of
these repair paths.  For every \(A\subseteq\mathcal L\), summing (3.2)
gives the sharp cut identity

\[
 |Q(A,\bar A)|-|Q(\bar A,A)|
       =\sum_{y\in A}(a(y)-1).                              \tag{3.3}
\]

This is the precise Hall-deficiency ledger hidden by the palette notation.
It separates the integral transport requirement from the additional
rainbow condition that the \(K\) arc labels are exactly \(\mathcal E\).

## 4. The floor case collapses to a Catalan core

Suppose the base word itself has the exact floor profile

\[
             0^K1^{N-2K}2^K.                               \tag{4.1}
\]

Let \(\mathcal D\) be its \(K\) duplicated colours and \(\mathcal Z\) its
\(K\) holes.  Form the occurrence-labelled three-partite repair core
\(\mathscr R\) on

\[
                   \mathcal E\sqcup\mathcal D\sqcup\mathcal Z
\]

by putting in the hyperedge

\[
          (X,b_i,t_i(X);i)                                  \tag{4.2}
\]

whenever \(X\subset U_i\), \(b_i\in\mathcal D\), and
\(t_i(X)\in\mathcal Z\).  The suffix \(i\) remembers which of the two
occurrences of \(b_i\) is used.

### Theorem 4.1 (floor-core equivalence)

Under (4.1), directed Catalan repair is equivalent to a perfect matching
of \(\mathscr R\).

#### Proof

Every hole needs an incoming selected arc.  There are \(K\) holes and
exactly \(K\) selected arcs, so every selected target is a different hole.
Every duplicated colour needs an outgoing selected arc.  There are \(K\)
duplicated colours and \(K\) arcs, so exactly one occurrence of every
duplicated colour is selected.  The omitted-facet and host conditions are
precisely the remaining coordinates of (4.2).  The converse is immediate
from replacing one copy of every duplicated colour by every hole. \(\square\)

Thus the zero-slack gate has size \(K=\operatorname{Cat}_m\), not \(N\):
it is one perfect matching in a \(K\times K\times K\) repair core.

### Lemma 4.2 (literal square geometry of a repair hyperedge)

A triple \((X,D,Z)\) can occur in the repair core at a directed block
\(C_i,U_i,C_{i+1}\) only in the following form.  Put
\[
                         p=X\setminus Z.
\]
Then
\[
 |D\cap Z|=m-2,qquad Z\subset X,qquad p\notin D,           \tag{4.3}
\]
and the entire directed block is recovered from the triple by
\[
 C_i=D\cup\{p\},\qquad
 C_{i+1}=D\cup Z,\qquad
 U_i=D\cup X.                                               \tag{4.4}
\]
Conversely, (4.3)--(4.4) produce a valid Boolean diamond and satisfy
\[
 D=C_i\cap C_{i+1},\qquad Z=X\cap C_{i+1}.                 \tag{4.5}
\]

#### Proof

Write the three distinct facets of \(U_i\) as
\(C_i=U_i-a\), \(C_{i+1}=U_i-b\), and \(X=U_i-c\).  Then
\[
 D=U_i-\{a,b\},\qquad Z=U_i-\{b,c\},\qquad p=b,
\]
which gives (4.3)--(4.5).  Conversely those formulas have the stated
ranks and reconstruct the same three facets of \(U_i=D\cup Z\cup\{p\}\).
\(\square\)

Thus the three-partite core is not an arbitrary 3-matching instance.
After projection to the duplicate--hole shores, every edge \(D Z\) is a
Johnson edge, and its token is necessarily \(X=Z\cup\{p\}\), where
\(p\) is the element deleted at the directed seam and \(p\notin D\).
For one fixed occurrence of \(D=b_i\), the admissible repair edges form a
directed star of at most \(m-1\) such Johnson neighbours.  This local
square law is the structure an inductive matching argument is allowed to
use; a generic three-partite theorem discards it.

## 5. A constructive sufficient invariant

Call a balanced three-partite hypergraph **leaf-peelable** if it is empty,
or if it has a vertex of degree one whose unique incident edge \(e\) can
be deleted together with all vertices and edges meeting \(e\), leaving a
leaf-peelable balanced hypergraph.

### Lemma 5.1 (peeling lemma)

Every leaf-peelable balanced three-partite hypergraph has a unique perfect
matching, obtained by repeatedly taking the unique edge at a degree-one
vertex.

#### Proof

The unique edge at a degree-one vertex belongs to every perfect matching.
Delete its three vertices and apply induction. \(\square\)

### Lemma 5.2 (unitriangular ear extension)

Let \(\mathscr R_0\) be leaf-peelable.  Adjoin three new shore vertices
\(a,b,c\), the edge \(e=abc\), and any collection of further edges subject
to the single condition that one of \(a,b,c\), say \(a\), occurs only in
\(e\).  The resulting balanced hypergraph is leaf-peelable provided that
deleting the three vertices of \(e\) and every incident edge leaves exactly
\(\mathscr R_0\).

More generally, a sequence of such ears, and a disjoint union of
leaf-peelable cores, is leaf-peelable.

#### Proof

The vertex \(a\) forces \(e\).  Peeling \(e\) leaves
\(\mathscr R_0\), so Lemma 5.1 applies.  Iterate for a sequence of ears;
for disjoint unions, concatenate their peeling orders. \(\square\)

Equivalently, it is enough to exhibit a proposed perfect matching
\(e_1,\ldots,e_K\) and an order in which every \(e_j\) contains a pivot
vertex of degree one after the vertices of
\(e_1,\ldots,e_{j-1}\) have been deleted.  This is the literal
unitriangular certificate sought from a two-coordinate recursion: an
old repair core may be copied intact, while each new Catalan token is
attached as one forced ear.

Combining Theorem 4.1 and Lemma 5.1 gives a concrete sufficient all-\(m\)
target:

> construct a saturating cycle whose second-colour word has profile
> \(0^K1^{N-2K}2^K\) and whose Catalan repair core is leaf-peelable.

This is strictly stronger than asking for an unspecified split-repair
matching, but it is recursive in shape and has a linear-time human
certificate.

## 6. The positive \(m=3\) cycle has exactly this structure

For the positive cycle frozen in
`scratch/audit_catalan_directed_repair_finite_m2_m3_20260731.py`, the
three parts of the repair core are

\[
\begin{aligned}
 \mathcal E&=\{124,234,125,346,156\},\\
 \mathcal D&=\{13,35,45,16,26\},\\
 \mathcal Z&=\{12,14,24,15,36\}.
\end{aligned}
\]

There are only seven viable hyperedges:

\[
\begin{array}{c|c|c|c}
X&b_i&t_i(X)&i\\ \hline
124&13&14&3\\
124&45&14&13\\
234&26&24&7\\
125&13&12&2\\
125&45&15&13\\
346&16&36&9\\
156&35&15&1.
\end{array}
\]

Degree-one peeling forces, in order for example,

\[
 (234,26,24),
 (346,16,36),
 (156,35,15),
 (125,13,12),
 (124,45,14).
\]

This proves the unique all-outgoing solution without enumerating the other
\(4607\) host/orientation states.  The empirical invariant is therefore
not mere density or pairwise Hall: it is a tiny peelable Catalan core.

The case \(m=2\) has no uniform directed solution in either orientation
and must remain a separate base case for this proposed recursion.

## 7. Balanced linear forests and the exact ear induction

In the floor case, project every occurrence-labelled hyperedge
\((X,D,Z;i)\) of \(\mathscr R\) to the bipartite edge \(DZ\), retaining
\((X,i)\) as its label.  Denote the resulting labelled bipartite
multigraph by \(G_{\mathscr R}\).

Call \(G_{\mathscr R}\) a **label-compatible balanced linear forest** if

1. it is simple and every component is a path containing equally many
   vertices of \(\mathcal D\) and \(\mathcal Z\); and
2. the edges in its graph-theoretic perfect matching carry pairwise
   distinct \(X\)-labels, running through all of \(\mathcal E\).

### Theorem 7.1 (linear-forest certificate)

A label-compatible balanced linear forest has a unique uniformly outgoing
directed repair.

Within the class of simple bipartite graphs of maximum degree at most two,
the balanced-linear-forest condition is equivalent to uniqueness of the
graph-theoretic perfect matching.  It is not equivalent to uniqueness of
the labelled three-partite repair outside that class.

#### Proof

A bipartite graph of maximum degree at most two is a disjoint union of
paths and even cycles.  A path has a perfect matching exactly when its two
shores have equal size, and that matching is unique.  An even cycle has
two perfect matchings.  This proves the graph statement.  Condition 2
lifts the unique graph matching to a hypergraph matching covering every
\(X\)-token, so Theorem 4.1 gives the repair.

The unrestricted converse fails even for two tokens.  Take matching
hyperedges
\[
 (x_1,d_1,z_1),\qquad (x_2,d_2,z_2)
\]
and add
\[
 (x_1,d_1,z_2),\qquad (x_1,d_2,z_1).
\]
The projection is a four-cycle, but its second graph perfect matching
uses \(x_1\) twice and is not a hypergraph matching.  The displayed
matching is therefore the unique three-partite repair. \(\square\)

For the positive \(m=3\) fixture, the projected graph consists of
\[
 35-15-45-14-13-12
\]
and the two isolated edges \(26-24\) and \(16-36\).  Its unique matching
edges have labels \(156,124,125,234,346\), respectively.  This gives a
second, purely graph-theoretic proof of the finite result.

### Lemma 7.2 (balanced path-ear extension)

Start with a label-compatible balanced linear forest.  Add a new duplicate
vertex \(D\), a new hole vertex \(Z\), a new token \(X\), and the matching
hyperedge \((X,D,Z)\).  Either leave \(DZ\) as a new component, or attach
one of \(D,Z\) by one additional nonmatching edge to an endpoint on the
opposite shore of an old path.  If the attachment has any admissible
label and creates no parallel edge, the result remains a
label-compatible balanced linear forest, with matching label set enlarged
by \(X\).

The operation may be iterated, and an even path ear containing several
new matched pairs is obtained by iteration.

#### Proof

An isolated \(DZ\) is a balanced path.  Attaching it to an old endpoint
by one nonmatching edge extends that path by two vertices, preserving
acyclicity, maximum degree two, and shore balance.  The unique perfect
matching is the old matching together with \(DZ\); its labels remain
bijective after adjoining \(X\). \(\square\)

Consequently an all-\(m\) construction does not need a new global Hall
argument at every dimension.  It is enough for the two-coordinate lift to
carry the older repair forest intact and add
\[
                  \operatorname{Cat}_{m+1}-\operatorname{Cat}_m
\]
new matched pairs by balanced path ears.  Lemma 7.2 then proves the new
directed repair and simultaneously gives the determinant pivot order.
This is a precise induction target, not yet a construction of the required
saturating cycle.

### Proposition 7.3 (what the forest condition is, and is not)

There are two related incidence graphs, and their conclusions must be kept
separate.

1. For the floor repair core \(\mathscr R\), a label-compatible balanced
   linear forest in the duplicate--hole projection is a sufficient
   certificate for a unique uniformly outgoing repair, by Theorem 7.1.
   It is not necessary: the labelled \(K=2\) four-cycle displayed in that
   theorem has a unique hypergraph repair because its other graph matching
   repeats the token \(x_1\).
2. For the full repaired middle cycle \(P\), the occurrence-colour graph
   whose shores are all lower and upper colours has a unique common
   transversal exactly when it is a balanced linear forest, provided both
   load profiles are at the \(1/2\) floor.  But uniqueness does not force
   uniform orientation.  The frozen negative \(m=3\) fixture is a balanced
   linear forest with a unique common transversal whose five split choices
   are mixed.

The second statement is proved occurrence-for-occurrence in
`MATH_THEOREM_CATALAN_COLOUR_INCIDENCE_AND_DIAMOND_ENUMERATION_20260731.md`.
It is a precise counterexample to the tempting implication
\[
 \text{balanced incidence forest}\Longrightarrow
 \text{uniformly outgoing repair}.                         \tag{7.4}
\]
Orientation coherence is an additional literal condition, not a parity
consequence of forest structure.

### Lemma 7.4 (common-coordinate lifting preserves a repair ear)

Let \((X,D,Z)\) be a literal repair hyperedge on \([2m]\), and adjoin a
new coordinate \(x\).  Then
\[
                  (X+x,\ D+x,\ Z+x)                        \tag{7.5}
\]
is a literal repair hyperedge one rank higher.  The corresponding block is
obtained by adjoining \(x\) to all three vertices in (4.4).

Consequently an old leaf-peelable core can be embedded unchanged in one
Pascal sector of a two-coordinate lift.  What is not automatic is the
global completion: the remaining new tokens must be realized by seams of
one saturating cycle, with its base duplicate and hole sets equal to the
new vertices prescribed by the abstract ears.

#### Proof

All containments and set differences in (4.3)--(4.5) are unchanged after
adjoining the same coordinate.  The final qualification follows because a
repair hyperedge belongs to the core only when its reconstructed directed
block actually occurs in the chosen saturating cycle. \(\square\)

This is the exact boundary of the ear method.  Graph ears and even literal
Boolean squares lift; simultaneous realization of the entire ear bank by
one cycle is the remaining global construction theorem.  The published
single-port adjacent-level recursion cannot supply that bank: the exact
new-coordinate balance requires \(K\) cross-sector ports but that recursion
creates one.  See
`MATH_AUDIT_K_GMM_SINGLE_PORT_GLUE_CATALAN_COMMON_REFINEMENT_OBSTRUCTION_20260731.md`
for the deficiency-\((K-1)\) Hall certificate.

## 8. Algebraic certificate and the limitation of generic rainbow theorems

Let \(A(s,\mathbf x)\) be the \(N\times N\) matrix with rows indexed by
blocks and columns by \(\mathcal L\), where

\[
 A_{i,y}=s\,\mathbf1_{y=b_i}
       +\sum_{\substack{X\in\mathcal E:\ X\subset U_i\\t_i(X)=y}}x_X.
 \tag{7.1}
\]

Then

\[
 \boxed{
 [s^{N-K}\prod_{X\in\mathcal E}x_X]\operatorname{per}A>0
 \iff \text{directed repair exists}.}
 \tag{7.2}
\]

The same coefficient in \(\det A\), if nonzero, is a sufficient signed
certificate.  A leaf-peelable repair core contributes a unique monomial,
so its determinant coefficient is \(\pm1\).  This gives an algebraic
induction target: triangularize the repair core under the two-coordinate
dimension lift.  Lemma 5.2 is exactly Laplace expansion at a pivot entry:
each ear removes one row, one column, and one required token variable,
leaving the determinant coefficient of the older core.

Over \(\mathbb F_2\), determinant and permanent coincide.  Consequently

\[
 [s^{N-K}\prod_{X\in\mathcal E}x_X]\det_{\mathbb F_2}A
 \tag{7.3}
\]

is exactly the parity of the number of directed repairs.  Proving that
(7.3) equals one is therefore an all-\(m\) existence proof even without
uniqueness.  This is the cleanest algebraic version of the recursive
target: establish an odd number of repair matchings by a block-triangular
or ear-expansion identity.

By contrast, the standard Aharoni--Haxell sufficient condition for a
rainbow matching from \(K\) graphs would demand

\[
 \nu\!\left(\bigcup_{X\in\mathcal A}G_X\right)
       >2(|\mathcal A|-1)
\]

for every \(\mathcal A\subseteq\mathcal E\).  At
\(\mathcal A=\mathcal E\), the left side is at most \(K\), whereas the
right side is \(2K-2\).  For \(K\ge3\) this generic criterion cannot even
be satisfied.  The all-(m) proof must exploit the recursive
unitriangular/peelable structure, not a black-box hypergraph expansion
theorem.

## 9. Exact remaining theorem

The strongest direct recursive statement suggested by the finite data is:

> For every \(m\ge3\), there is an oriented saturating cycle between ranks
> \(m,m+1\) of \(Q_{2m}\) whose base word has profile
> \(0^K1^{N-2K}2^K\) and whose all-outgoing Catalan repair core is
> leaf-peelable.

This statement implies the directed split-switch matching immediately.
It is not proved here.  Its advantages over the original gate are that
both claims are literal local invariants of one cycle, the repair
certificate has only \(K\) forced edges, and the \(m=3\) positive fixture
already realizes the exact pattern.

The analysis above rules out three apparent shortcuts:

* the three marginal Hall theorems do not couple their choices;
* a balanced full colour-incidence forest need not orient uniformly; and
* an abstract balanced-ear recursion need not be realizable by a single
  Boolean saturating cycle.

It also leaves one constructive induction interface, with no hidden
matching step: preserve the old core by (7.5), realize every new matched
pair as a literal square (4.3)--(4.4), attach those pairs as balanced path
ears, and braid all reconstructed blocks into one saturating cycle without
changing their directed occurrences.  Proving that bulk Boolean braid, or
exhibiting a dimension where its exact sector-balance equations are
infeasible, is the precise all-\(m\) fork.  No such proof or counterexample
is presently known.
