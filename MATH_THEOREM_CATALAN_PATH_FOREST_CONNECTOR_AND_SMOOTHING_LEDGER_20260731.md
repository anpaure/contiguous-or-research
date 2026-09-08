# Catalan path-forest connectors: exact colour, block, orientation, and smoothing gates

Date: 2026-07-31  
Status: solver-independent equivalences for a fixed inclusion matching and
its physical path-forest lift; the newly reported \(m=4\) flag list and
connector order are an input fixture, not authenticated in this note

## 1. Fixed notation and the physical connector object

Fix \(m\geq2\), put \(\Omega=[2m]\), and write

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal M=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1}.
\]

Let

\[
 K=\operatorname {Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 M=|\mathcal M|=N+K.
\]

For every inclusion \(L\subset U\), where
\(L\in\mathcal L\) and \(U\in\mathcal U\), the two members of
\(\mathcal M\) strictly between them form one Johnson edge

\[
 \psi(L,U)=\{L\cup\{a\},L\cup\{b\}\},
 \qquad U\setminus L=\{a,b\}.
 \tag{1.1}
\]

The map \(\psi\) is a bijection from lower--upper inclusions to the edges
of \(J(2m,m)\).  For a Johnson edge \(e=AB\), its inverse colours are

\[
 \ell(e)=A\cap B,\qquad u(e)=A\cup B.                  \tag{1.2}
\]

Let

\[
 \sigma:\mathcal L\longrightarrow\mathcal U,
 \qquad L\subset\sigma(L),                              \tag{1.3}
\]

be a perfect inclusion matching, and let

\[
 F=\{\psi(L,\sigma(L)):L\in\mathcal L\}.              \tag{1.4}
\]

Assume that \(F\), as a graph on all \(M\) middle vertices, is a spanning
linear forest.  It has \(N\) edges, hence exactly

\[
                         M-N=K                           \tag{1.5}
\]

path components.  Trivial one-vertex paths are allowed at this stage.

An **endpoint connector cycle** for \(F\) is a set \(D\) of \(K\)
Johnson edges disjoint from \(F\) such that:

1. every endpoint port of every nontrivial path is incident with exactly
   one edge of \(D\), while a trivial path has two connector incidences;
2. every connector joins two different components; and
3. after contracting each path component, the edges \(D\) form one cycle.

The contracted cycle may be the usual two-parallel-edge cycle when
\(K=2\).  The physical edges themselves remain distinct.

### Theorem 1.1 (path-forest connector equivalence)

Endpoint connector cycles \(D\) for \(F\) are in bijection with Hamilton
cycles \(P\) of \(J(2m,m)\) which contain \(F\) and have
\(E(P)\setminus F=D\).  For every such \(P\), the occurrence set

\[
                             Q:=F                         \tag{1.6}
\]

is simultaneously a lower-colour and an upper-colour transversal of
\(P\).

#### Proof

Inside a nontrivial path, every internal vertex already has degree two in
\(F\), and each endpoint has degree one.  The endpoint conditions give
every middle vertex degree two in \(F\cup D\); for a trivial path its two
connector incidences do the same.  The contracted connector graph is
connected, so \(F\cup D\) is one spanning two-regular graph, hence a
Hamilton cycle.

Conversely, suppose a Hamilton cycle contains \(F\).  Its complementary
edges can meet a nontrivial path only at its two endpoints, once at each;
they meet a trivial path twice.  Contracting the paths leaves a connected
two-regular multigraph, hence one connector cycle.  The complement has
\(M-N=K\) edges.

Finally, (1.3)--(1.4) give exactly one edge of \(Q\) with each lower
colour and exactly one with each upper colour.  Thus \(Q\) is a common
transversal occurrence for occurrence. \(\square\)

This is the exact strength of the physical flag-matching seed.  It is
strictly stronger than an abstract determinant or perfect-matching
certificate, because its lift is already a spanning path forest.  It is
strictly weaker than a directed Catalan repair, because no condition has
yet been put on the colours or local orientations of \(D\).

## 2. Connector repetition never destroys coverage

For \(L\in\mathcal L\) and \(U\in\mathcal U\), put

\[
 c_L=|\{d\in D:\ell(d)=L\}|,
 \qquad
 c_U=|\{d\in D:u(d)=U\}|.                               \tag{2.1}
\]

Because \(Q\) already uses every colour exactly once, the complete colour
ledger of \(P\) is

\[
 \operatorname{mult}_P(L)=1+c_L,
 \qquad
 \operatorname{mult}_P(U)=1+c_U.                        \tag{2.2}
\]

In particular, arbitrary repetitions among connector colours are harmless
for **coverage**: all lower and all upper colours still occur.  They are
not harmless for the floor, complementary-transversal, or block gates
below.

### Theorem 2.1 (intermediate lower and upper floors)

The lower edge-colour word of \(P\) has profile

\[
                         1^{N-K}2^K                      \tag{2.3}
\]

if and only if \(\ell|_D\) is injective.  Symmetrically, the upper word
has this profile if and only if \(u|_D\) is injective.

#### Proof

There are exactly \(K\) connector occurrences.  Starting from the
multiplicity-one ledger supplied by \(Q\), they produce (2.3) exactly
when they hit \(K\) different colours. \(\square\)

The lower assertion is the **intermediate Hamilton-cycle floor**.  It is
not the floor assertion for the shorter cycle obtained later by smoothing
one middle vertex from every doubled upper block; Section 5 gives that
separate ledger.

## 3. The exact tight upper-covering gate

Although \(Q\) itself is an upper transversal, using the same edge set for
both boundary levels leaves every connector edge unmarked and is not a
tight edgewise three-level realization.  The relevant second object is an
upper transversal which, together with \(Q\), covers every edge of \(P\).

Call \(R\subseteq E(P)\) an **upper covering transversal relative to
\(Q\)** if

\[
 |R|=N,\qquad u|_R:R\longrightarrow\mathcal U
 \text{ is bijective},\qquad Q\cup R=E(P).              \tag{3.1}
\]

### Theorem 3.1 (unique complementary upper transversal)

An upper covering transversal relative to \(Q\) exists if and only if
\(u|_D\) is injective.  When it exists it is unique and equals

\[
 R_D=D\ \cup\
 \{q_U:U\in\mathcal U\setminus u(D)\},                 \tag{3.2}
\]

where \(q_U\) is the unique edge of \(Q\) with upper colour \(U\).

#### Proof

The covering condition forces every edge of \(D=E(P)\setminus Q\) into
\(R\).  An upper transversal cannot contain two connectors of the same
upper colour, proving necessity.  If the connector upper colours are
distinct, take every connector and, for each upper colour not represented
by a connector, take its unique \(Q\)-edge.  This is (3.2), is an upper
transversal, and covers \(P\).  The same forced choices prove uniqueness.
\(\square\)

### Corollary 3.2 (tight edgewise three-level enumeration)

Under the condition of Theorem 3.1, use \(Q\) for lower insertions and
\(R_D\) for upper insertions on the oriented middle cycle \(P\).  On an
edge \(AB\), insert

\[
 A,A\cap B,B;\qquad A,A\cup B,B;\qquad
 A,A\cap B,A\cup B,B                              \tag{3.3}
\]

according as the edge is lower-only, upper-only, or belongs to both
transversals.  This enumerates every vertex in ranks
\(m-1,m,m+1\) once and has flip length exactly \(4N\), the bipartite
lower bound.

Conversely, with \(Q\) fixed as the lower transversal, an edgewise
\(P\)-respecting tight enumeration of this covering form yields an upper
covering transversal, and therefore forces \(u|_D\) to be injective.

#### Proof

All lower, middle, and upper vertices occur once by the two transversal
conditions and the Hamilton property.  Since \(Q\cup R_D=E(P)\), no
middle edge is empty.  The two sets have size \(N\), their union has size
\(M=N+K\), and therefore

\[
 |Q\cap R_D|=2N-M=N-K.                                  \tag{3.4}
\]

There are \(K\) lower-only edges, \(K\) upper-only edges, and \(N-K\)
diamonds.  Their respective flip costs are two, two, and four, giving

\[
                     2K+2K+4(N-K)=4N.                   \tag{3.5}
\]

The three levels contain \(M+2N\) vertices and have bipartition imbalance
\(2N-M\), so every cyclic enumeration costs at least
\((M+2N)+(2N-M)=4N\).  Thus (3.5) is tight.  In the converse, tight
covering makes every connector an upper-marked edge.  More explicitly,
for any upper transversal \(R\), if
\(z=|E(P)\setminus(Q\cup R)|\), then

\[
 |Q\cap R|=N-K+z
 \quad\hbox{and}\quad
 \operatorname{cost}(Q,R)=2M+2|Q\cap R|=4N+2z.          \tag{3.6}
\]

Hence equality with \(4N\) forces \(z=0\).  The upper marks then give
(3.1), and Theorem 3.1 applies. \(\square\)

No adjacency of equal upper colours is used here.  Thus a tight
\(P\)-respecting covering enumeration is weaker than a literal cap-two
block realization.

## 4. Cap-two blocks and the exact orientation mark

Assume from now on that \(u|_D\) is injective.  For \(d\in D\), write

\[
 U_d=u(d),\qquad q_d=q_{U_d}\in Q.                      \tag{4.1}
\]

Thus \(d\) and \(q_d\) are the two and only two occurrences of \(U_d\)
on \(P\).

### Theorem 4.1 (cap-two block-coherence criterion)

The upper occurrence word of \(P\) consists of \(K\) contiguous
two-edge blocks and \(N-K\) singleton blocks if and only if, for every
\(d\in D\), the two physical edges \(d\) and \(q_d\) share a middle
endpoint.

Equivalently, if

\[
 L_d=\ell(d),\qquad L_q=\ell(q_d),                       \tag{4.2}
\]

then the local condition is

\[
 |(U_d\setminus L_d)\cap(U_d\setminus L_q)|=1,
 \qquad\text{equivalently}\qquad |L_d\cup L_q|=m.      \tag{4.3}
\]

#### Proof

Injectivity of \(u|_D\) says that every repeated upper colour has exactly
the two occurrences \(d,q_d\).  They are contiguous in the cyclic edge
word precisely when they are incident at one middle vertex of \(P\).

The endpoints of \(\psi(L,U)\) are the two sets \(U\setminus\{x\}\)
with \(x\in U\setminus L\).  The distinct edges \(d,q_d\) therefore
share an endpoint exactly when their two deletion pairs meet in one
element.  This is (4.3), and
\(L_d\cup L_q=U_d\setminus((U_d\setminus L_d)\cap
(U_d\setminus L_q))\) proves the equivalent formula. \(\square\)

When (4.3) holds, let \(t_d\) be the shared middle endpoint.  The edge
\(q_d\in F\) is then a terminal edge of one path component of \(F\).
Mark on the contracted connector cycle the endpoint of \(d\) lying in
that component, and define

\[
 a:D\longrightarrow\mathcal C(F)                       \tag{4.4}
\]

to be the resulting connector-to-path map.  Here \(\mathcal C(F)\) is
the set of the \(K\) path components.

### Theorem 4.2 (uniform-outgoing criterion)

Under the cap-two block condition, the following are equivalent.

1. The Hamilton cycle can be oriented so that at every doubled upper
   block the connector \(d\) is immediately followed by the matching edge
   \(q_d\); equivalently, the retained common transversal \(Q\) is
   uniformly outgoing.
2. The attachment map \(a:D\to\mathcal C(F)\) is bijective.
3. Every path component has exactly one endpoint at which its terminal
   \(Q\)-edge is paired, by upper colour, with the incident connector.

When these conditions hold, the outgoing orientation is unique.  Its
reverse is uniformly incoming.  In particular no trivial path component
can occur.

#### Proof

Contract every path.  The connectors form one cycle on \(K\) component
vertices, and each connector marks one of its two incident vertices via
(4.4).  If \(Q\) is uniformly outgoing, direct a connector toward the
component in which it is followed by \(q_d\).  Every component is entered
once and left once, so it receives exactly one mark.  Thus \(a\) is
bijective.

Conversely, direct each connector toward its marked component.  A directed
version of an undirected cycle in which every vertex has indegree one also
has outdegree one and is one coherently directed cycle.  On entering a
component at its marked endpoint, traverse its entire path to the other
endpoint.  The terminal edge at the entrance is exactly \(q_d\), so every
connector is immediately followed by its matching edge.  The marked
directions force this orientation, and reversal makes every matching edge
incoming instead.  Conditions 2 and 3 are the same literal incidence
statement.  A trivial component contains no terminal \(Q\)-edge and hence
cannot receive a mark. \(\square\)

This is the orientation-free form of the “one omitted tail per path”
condition.  It is stronger than merely finding a connector Hamilton cycle
on the contracted components.  It also proves distinct physical cut
seams: in the outgoing orientation every component has one marked entrance
and one unmarked exit.

## 5. Smoothing and the separate saturating-base floor

Assume the equivalent conditions of Theorem 4.2 and orient \(P\) in the
outgoing direction.  At every doubled upper block write the local segment
as

\[
                         h_d\;\longrightarrow\;t_d
                         \;\longrightarrow\;n_d,        \tag{5.1}
\]

where \(h_dt_d=d\in D\) is the incoming connector and
\(t_dn_d=q_d\in Q\) is the outgoing matching edge.  Both edges have upper
colour \(U_d\).  Define

\[
 \alpha_d=h_d\cap t_d=\ell(d),\qquad
 \beta_d=t_d\cap n_d=\ell(q_d),\qquad
 b_d=h_d\cap n_d.                                      \tag{5.2}
\]

Deleting every \(t_d\) and replacing the two incident edges by
\(h_dn_d\) gives a length-\(N\) middle cycle \(C\).  The edge \(h_dn_d\)
is Johnson and has upper colour \(U_d\), so \(C\) is upper-rainbow.

The two lower ledgers are different:

\[
 \operatorname{low}(P)
   =\mathcal L\mathbin{\dot\cup}\{\alpha_d:d\in D\},   \tag{5.3}
\]

whereas

\[
 \operatorname{low}(C)
   =\mathcal L-\{\beta_d:d\in D\}
                  +\{b_d:d\in D\}                     \tag{5.4}
\]

as multisets.

### Theorem 5.1 (exact separation of the two floor tests)

Under coherent cap-two smoothing:

1. The intermediate Hamilton cycle \(P\) has lower profile
   \(1^{N-K}2^K\) if and only if the incoming colours
   \(\alpha_d\) are pairwise distinct.
2. The suppressed upper-rainbow cycle \(C\) has lower profile
   \(0^K1^{N-2K}2^K\) if and only if the bases \(b_d\) are pairwise
   distinct and

   \[
                         \{b_d:d\in D\}\cap
                         \{\beta_d:d\in D\}=\varnothing. \tag{5.5}
   \]

The first test does not, by its ledger alone, establish the second; the
base colours require the separate literal test in assertion 2.

#### Proof

Identity (5.3) is (2.2), and proves assertion 1.  The \(\beta_d\) are
pairwise distinct because they are lower colours of different edges in
the lower transversal \(Q\).  Starting from one copy of every lower
colour, (5.4) removes these \(K\) distinct colours and adds \(K\) base
colours.  The result has exactly \(K\) zeros and \(K\) twos precisely when
no removed colour is re-added and every addition hits a different
nonremoved colour.  These are exactly (5.5) and pairwise distinctness of
the bases. \(\square\)

Thus a **full uniform-outgoing split-leave floor repair** in this fixed
path-forest coordinate requires all of the following separate gates:

\[
\begin{array}{ll}
\text{upper complement and profile:}&u|_D\text{ injective},\\
\text{literal cap-two blocks:}&d\text{ shares an endpoint with }q_d,\\
\text{uniform direction:}&a:D\to\mathcal C(F)\text{ bijective},\\
\text{intermediate and base floors:}&
 \alpha\text{ injective},\quad b\text{ injective},\quad
 b(D)\cap\beta(D)=\varnothing.
\end{array}                                               \tag{5.6}
\]

The common-transversal property and immediate lower/upper coverage require
none of the extra conditions in (5.6).

### Corollary 5.2 (full fixed-forest equivalence)

Within the hypotheses of Theorem 1.1, conditions (5.6) are jointly
necessary and sufficient for an orientation in which:

1. the upper word of \(P\) is cap-two block coherent and \(Q\) is its
   uniformly outgoing common transversal;
2. the lower word of \(P\) has profile \(1^{N-K}2^K\); and
3. smoothing the \(K\) incoming/outgoing blocks produces an upper-rainbow
   length-\(N\) cycle with lower profile
   \(0^K1^{N-2K}2^K\).

Under these conditions \(R_D\) is also the unique upper covering
transversal and gives the tight \(P\)-respecting enumeration of
Corollary 3.2.

#### Proof

Upper injectivity and Theorem 4.1 are exactly the cap-two block gate.
Theorem 4.2 is exactly the uniform-orientation gate.  In that orientation,
Theorem 5.1 identifies lower injectivity with the intermediate floor and
the two base conditions with the suppressed floor.  These implications
are reversible term by term.  The final statement is Theorem 3.1 and
Corollary 3.2. \(\square\)

## 6. Exact scope for the reported \(m=4\) seed

For \(m=4\), one has \((N,M,K)=(56,70,14)\).  Therefore a literal perfect
inclusion matching whose lift has path sizes

\[
             21,7,7,6,5,5,4,3,2,2,2,2,2,2              \tag{6.1}
\]

and a connector cycle through all fourteen paths immediately proves, by
Theorem 1.1, a Hamilton cycle in \(J(8,4)\) containing a common lower and
upper transversal.  It follows without any connector-colour hypothesis
that all 56 lower and all 56 upper colours occur on that cycle.

What does **not** follow from (6.1) and contracted connectivity alone is:

* the intermediate lower floor (audit \(\ell|_D\));
* the unique tight complementary upper transversal (audit \(u|_D\));
* adjacency of the two occurrences in every doubled upper colour (audit
  (4.3));
* one paired connector incidence on every path (audit (4.4)); or
* the suppressed base floor (audit the two tests in Theorem 5.1(2)).

Accordingly, the frozen flag list and connector order can be used as a
guided physical seed even if connector colours repeat.  Promotion to a
tight diamond enumeration, a cap-two cycle, or a directed floor repair
must cite the corresponding literal tests above.  No all-
\(m\) construction and no claim about a connector list not replayed here
is made.
