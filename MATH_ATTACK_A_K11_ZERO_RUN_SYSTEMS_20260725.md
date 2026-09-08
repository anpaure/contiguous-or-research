# Exploration line A: the simultaneous \(k=11\) zero-run systems

Date: 2026-07-25

## 0. Verdict

Assume the audited zero-margin normal form for a hypothetical nonzero
\(k=11\) word of length \(465\).  This report does **not** derive a full
contradiction.  Thus it does not improve the certified interval

\[
465\leq \nu(11)\leq477.
\]

It proves four new finite restrictions.

1. The \(330\) central four-coordinate zero-run systems have an exact
   simultaneous parity shadow.  If \(V_Y\) is the number of central
   six-facets contained in the seven-set \(\Omega\setminus Y\), then

   \[
   \mathcal O=\{Y\in\tbinom{\Omega}{4}:V_Y\text{ is even}\}
   \]

   is a binary simplicial \(3\)-cycle.  If the number \(E\) of external
   six-sets is even, then

   \[
   |\mathcal O|=0\quad\hbox{or}\quad |\mathcal O|\geq8.
   \]

   If \(E\) is odd, then either \(\mathcal O\) is the five-facet boundary
   of one five-set, or \(|\mathcal O|\geq9\).

   This immediately disproves both scalar survivor ledgers in Sections
   13.1 and 13.2 of
   `MATH_ATTACK_M3_K11_RANK7_PHYSICAL_LIFT_20260724.md`.

2. For every rank-seven color, the central, external, and interface pieces
   obey an exact sector-component identity.  It implies that at most two
   multiplicity-six colors can have both central and external facets.  An
   interface-free mixed multiplicity-five color is forced to have one
   unbroken central joint-zero-run and no seam correction.

3. Every physical interface has six, and only six, boundary modes: one
   component-start mode and five predecessor-exchange modes.  If one color
   uses both interfaces, then

   \[
   x_Y\leq5-V_Y,\qquad t_{\Omega\setminus Y}\leq5,
   \]

   and its two boundary zero-runs have total length at most \(12\).

4. In the extremal branch \(E=132,\ V_Y=5\) for all \(Y\), the external
   five-set family must be a simple \(4\)-\((11,5,2)\) design.  Its induced
   Johnson graph is \(5\)-regular, and its \(330\) edges are canonically
   labelled by the \(330\) complementary five-sets.  The endpoint-ordered
   external forest is therefore reduced to a spanning linear forest in
   this explicitly labelled design graph, with at most two marked terminal
   components for the inward interfaces.

These are eliminative theorems, not restatements of the previous scalar
constraints.  The first deletes two previously advertised obstruction
models; the second and third delete whole families of saturated and
double-interface forests; the fourth is a certifiable finite reduction of
the most symmetric surviving branch.

No web lookup, solver, finite search, or computational enumeration is used.

## 1. Frozen setup

Let

\[
\Omega=[11].
\]

The physical word has entries \(B_0,\ldots,B_{464}\).  Its central
rank-at-most-three segment is

\[
[L,R],\qquad m=R-L+1,qquad A_i=B_{L+i}.
\]

The audited normal form gives \(m\geq228\).  Put

\[
C_i=A_i\cup A_{i+1}\cup A_{i+2},
\qquad 0\leq i\leq m-3,
\]

and let \(H=C_s\) be the unique seam triple.  The number of postcut
central pieces is

\[
b_H=\mathbf1_{\{s>0\}}+\mathbf1_{\{s<m-3\}}\in\{1,2\}.
\tag{1.0}
\]

When \(s>0\), the left initial piece begins with \(C_0,T_0\) in the
\(02/03\) schedule.  When \(s<m-3\), the right initial piece begins with
\(C_{m-3},T_{m-4}\) in the reversed \(13/03\) schedule.  These are the
only central pieces that can receive an inward interface.

Put

\[
E=465-m,qquad q=m-3=462-E.
\tag{1.1}
\]

The central four-windows

\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
\qquad 0\leq i<q,
\tag{1.2}
\]

are distinct six-sets.  Define their complementary five-sets

\[
D_i=\Omega\setminus T_i
\tag{1.3}
\]

and the omitted, or external, family

\[
\mathcal H
=\binom{\Omega}{5}\setminus\{D_0,\ldots,D_{q-1}\}.
\tag{1.4}
\]

Thus

\[
|\mathcal H|=462-q=E.
\tag{1.5}
\]

For a four-set \(Y\), put

\[
Q=\Omega\setminus Y,
\]

and retain the audited central zero-run quantities

\[
V_Y=\sum_{I}(|I|-3)_+,qquad
W_Y=\sum_I(|I|-4)_+,
\tag{1.6}
\]

where \(I\) ranges over the maximal central joint \(Y\)-zero-runs.  Also
let \(b_Y\) count those runs of length at least five and \(u_{4,Y}\) those
of length exactly four.  Then

\[
V_Y=W_Y+b_Y+u_{4,Y},qquad0\leq V_Y\leq7.
\tag{1.7}
\]

Let \(G_6\) be the endpoint-ordered spanning linear forest on the complete
six-set layer.  It has \(c\leq6\) components.  Complementing its vertices
makes it a spanning linear forest on all \(462\) five-sets.  For the color
\(Q=\Omega\setminus Y\), let

\[
c_Y,\quad x_Y,\quad \rho_Y
\tag{1.8}
\]

be respectively the numbers of central-central, external-external, and
external-to-central \(Q\)-edges.  Hence

\[
t_Q=c_Y+x_Y+\rho_Y,qquad
\sum_Y\rho_Y=d\leq2.
\tag{1.9}
\]

If the internal seam has \(\eta=0\), let \(\sigma_Y=1\) for the complement
of its deleted rank-seven five-window and zero otherwise.  In every other
seam case put \(\sigma_Y=0\).  The exact postcut relation is

\[
c_Y=W_Y-\sigma_Y.
\tag{1.10}
\]

All component counts below include isolated vertices.

## 2. The parity shadow of all \(330\) zero-run systems

For \(Z\subseteq\Omega\), define

\[
d_{\mathcal H}(Z)
=\#\{B\in\mathcal H:Z\subseteq B\}.
\tag{2.1}
\]

For \(Y\in\binom{\Omega}{4}\), abbreviate

\[
h_Y=d_{\mathcal H}(Y).
\tag{2.2}
\]

### Theorem 2.1 (exact simultaneous shadow identities)

For every four-set \(Y\),

\[
\boxed{h_Y=7-V_Y.}
\tag{2.3}
\]

More generally, for every \(Z\subseteq\Omega\), \(|Z|\leq4\),

\[
\boxed{
\sum_{\substack{Y\supseteq Z\\|Y|=4}}h_Y
=(5-|Z|)d_{\mathcal H}(Z).}
\tag{2.4}
\]

Consequently the \(330\) integers \(V_Y\) must satisfy, simultaneously,

\[
\sum_Y(7-V_Y)=5E,
\tag{2.5}
\]

and the sums of \(7-V_Y\) over every point-star, pair-star, and
triple-star are divisible by \(4,3,2\), respectively.

#### Proof

There are exactly seven five-set supersets of a fixed four-set \(Y\).
Exactly \(V_Y\) of them are among the \(D_i\), because

\[
Y\subseteq D_i
\quad\Longleftrightarrow\quad
T_i\subseteq\Omega\setminus Y.
\]

The other \(7-V_Y\) belong to \(\mathcal H\), proving (2.3).

Now count pairs \((Y,B)\) with

\[
Z\subseteq Y\subset B,\qquad |Y|=4,\quad B\in\mathcal H.
\]

For a fixed \(B\supseteq Z\), their number is

\[
\binom{5-|Z|}{4-|Z|}=5-|Z|.
\]

This proves (2.4).  The stated divisibilities and (2.5) are its cases
\(|Z|=0,1,2,3\).  \(\square\)

### Theorem 2.2 (small binary-cycle classification)

Put

\[
\mathcal O
=\{Y\in\tbinom{\Omega}{4}:h_Y\text{ is odd}\}
=\{Y:V_Y\text{ is even}\}.
\tag{2.6}
\]

Then every three-set lies in an even number of members of \(\mathcal O\).
Thus \(\mathcal O\) is a binary simplicial \(3\)-cycle.

A nonempty such cycle has at least five members.  If it has at most seven
members, then it has exactly five and

\[
\boxed{\mathcal O=\binom{B}{4}}
\tag{2.7}
\]

for a unique five-set \(B\).  In particular, the cardinalities

\[
1,2,3,4,6,7
\tag{2.8}
\]

are impossible.

#### Proof

The triple-star case of (2.4) is even.  Reducing it modulo two proves the
cycle assertion.

Choose a facet of a nonempty cycle.  Each of its four triples needs a
second containing facet, and those four facets are distinct.  Hence the
cycle has at least five facets.

For a point \(x\), the link of \(x\) is a binary \(2\)-cycle.  A nonempty
binary \(2\)-cycle has at least four triangles: the three edges of one
triangle require three distinct partner triangles.  Its number of
triangles is even, since every edge has even degree and

\[
3f_2=\sum_{e}\deg(e)
\]

is even.  If the link has exactly four triangles, choose one of them,
\(abc\), and write the partners of its three edges as
\(abp,acq,bcr\).  Parity at the remaining edges forces \(p=q=r\);
hence the four triangles are exactly the boundary of a tetrahedron.
Therefore, in a \(3\)-cycle of size at most seven, every positive
point degree is \(4\) or \(6\).

For five facets, the point-degree sum is \(20\).  The only viable support
has five points, all of degree four, and the facets are all five
four-subsets of that support.  This gives (2.7).

For six facets, the degree sum \(24\) forces either six degree-four points
or a support too small to contain six distinct four-sets.  On six support
points, complement the four-sets to obtain a graph \(J\) with six edges.
The cycle condition says that every induced three-vertex subgraph of \(J\)
has even edge count.  Fixing one vertex \(r\) gives

\[
\mathbf1_{uv\in J}
=\mathbf1_{ur\in J}+\mathbf1_{vr\in J}\pmod2.
\]

Thus \(J\) is a complete bipartite cut.  A cut on six vertices has

\[
0,5,8,\text{ or }9
\]

edges, never six.

For seven facets, the equation

\[
4a+6b=28
\]

leaves support sizes five, six, or seven.  Size five is too small.  On six
points, the same complement argument would give a cut graph with seven
edges, impossible.  On seven points, every point has degree four.  Each
point-link is therefore the four-triangle boundary of a tetrahedron.
Every pair consequently has codegree zero or three.  Join pairs of
codegree three in a graph \(K\).  This graph is \(4\)-regular, and every
cycle facet spans a \(K_4\).  The complement of \(K\) is a \(2\)-regular
graph on seven vertices, hence \(C_7\) or
\(C_3\mathbin{\dot\cup}C_4\).  Both have independence number three,
contradicting the \(K_4\) vertex set, which is an independent four-set in
the complement.  This excludes seven and completes the classification.
\(\square\)

### Corollary 2.3 (parity alternatives)

\[
\boxed{|\mathcal O|\equiv E\pmod2.}
\tag{2.9}
\]

Hence:

* if \(E\) is even, then \(|\mathcal O|=0\) or
  \(|\mathcal O|\geq8\);
* if \(E\) is odd, then either \(|\mathcal O|=5\) with form (2.7), or
  \(|\mathcal O|\geq9\).

If the five-facet alternative occurs, then

\[
\mathcal H\mathbin{\triangle}\{B\}
\]

has even degree on every four-set.

#### Proof

Modulo two,

\[
|\mathcal O|
\equiv\sum_Yh_Y
=5E
\equiv E.
\]

Apply Theorem 2.2.  The final assertion says that the parity boundary of
\(\mathcal H\) is the boundary of the single block \(B\).
\(\square\)

### Corollary 2.4 (both scalar barrier ledgers are impossible)

The central-loaded ledger (13.1) of the physical-lift report has \(E=135\)
and exactly seven even-\(V_Y\) colors, namely its seven colors with
\(V_Y=4\).  This contradicts Corollary 2.3.

The outer-loaded ledger (13.2) has \(E=132\) and exactly four even-\(V_Y\)
colors: two with \(V_Y=4\) and two with \(V_Y=6\).  This also contradicts
Corollary 2.3.

Thus neither ledger is the shadow of any family of distinct central
six-facets, before endpoint matching or physical exposure is considered.

The bound is sharp at the parity-shadow level.  One five-set has the five
facets in (2.7).  The symmetric difference of the boundaries of two
five-sets meeting in four points has eight facets.

### Corollary 2.5 (parity cost of high-star interface colors)

Let \(a\) be the number of globally present colors satisfying

\[
c_Y=0,\qquad V_Y=6.
\]

Then \(a\leq d\leq2\), and all \(a\) corresponding four-sets lie in
\(\mathcal O\).  If \(E\) is even, at least \(8-a\) additional
even-\(V_Y\) colors exist.  If \(E\) is odd, either those colors extend to
the five facets of one five-set, requiring at least \(5-a\) additional
members of \(\mathcal O\), or at least \(9-a\) additional even-\(V_Y\)
colors exist.

#### Proof

A centrally inactive \(V_Y=6\) color has only one external facet.  It
cannot have an external-external edge, so global presence requires an
interface.  Distinct colors use distinct interface edges, proving
\(a\leq d\).  Since \(V_Y\) is even, these four-sets lie in
\(\mathcal O\); now apply Corollary 2.3.  \(\square\)

## 3. Endpoint-ordered sector components

We first record the exact edge encoding supplied by the perfect inclusion
matching.

### Lemma 3.1 (two colors and one head label per forest edge)

Orient a component of the complemented forest as

\[
D\longrightarrow D'.
\]

For an edge, put

\[
Y=D\cap D',qquad
S=\Omega\setminus(D\cup D').
\tag{3.1}
\]

Then \(|Y|=4,\ |S|=5,\ Y\cap S=\varnothing\).  If

\[
a=D\setminus D',qquad b=D'\setminus D,
\]

then

\[
\Omega=Y\mathbin{\dot\cup}S\mathbin{\dot\cup}\{a,b\}.
\tag{3.2}
\]

The rank-seven hull color is \(\Omega\setminus Y\), the intervening
rank-five source is \(S\), and its matching extension coordinate at the
head is \(a\).  The edge sources \(S\) are all distinct; together with the
\(c\) component-start sources they are all \(462\) five-sets.

#### Proof

The two complementary five-sets are adjacent in \(J(11,5)\), giving
(3.2).  Complementing back,

\[
(\Omega\setminus D)\cap(\Omega\setminus D')=S,
\]

and

\[
\Omega\setminus D'=S\mathbin{\dot\cup}\{a\}.
\]

Thus the alternating middle-level path enters the head six-set from the
five-set \(S\), with matching label \(a\).  Every nonstart five-set is
used once as such an intervening source, while each component contributes
one unused start source.  \(\square\)

For fixed \(Q=\Omega\setminus Y\), its seven six-facets are the seven
vertices of the \(Q\)-colored subgraph of \(G_6\).  Split them into the
\(V_Y\) central and \(7-V_Y\) external facets.  Define

\[
Q\text{ to be mixed}\quad\Longleftrightarrow\quad c_Y>0\text{ and }x_Y>0.
\]

Also define

\[
\kappa_C(Y)=V_Y-c_Y,
\qquad
\kappa_E(Y)=7-V_Y-x_Y.
\tag{3.3}
\]

### Theorem 3.2 (exact sector-component identity)

The quantities in (3.3) are the component counts, including isolates, of
the central and external induced \(Q\)-forests.  They satisfy

\[
\boxed{
\kappa_C(Y)+\kappa_E(Y)=7-t_Q+\rho_Y.}
\tag{3.4}
\]

The central count also has the exact zero-run form

\[
\boxed{
\kappa_C(Y)=b_Y+u_{4,Y}+\sigma_Y.}
\tag{3.5}
\]

#### Proof

Every subgraph of the linear forest \(G_6\) is a forest.  A forest with
\(v\) vertices and \(e\) edges has \(v-e\) components, including isolates,
so (3.3) gives the two sector counts.

Before the interface edges are restored, there are
\(\kappa_C+\kappa_E\) components.  Each of the \(\rho_Y\) interface edges
reduces the count by one, since the complete \(Q\)-subgraph is still a
forest.  The final count is \(7-t_Q\), proving (3.4).

Finally, combine

\[
V_Y=W_Y+b_Y+u_{4,Y}
\]

with \(c_Y=W_Y-\sigma_Y\).  \(\square\)

### Theorem 3.3 (multiplicity-six rigidity)

If \(t_Q=6\), then the \(Q\)-subgraph is one path spanning all seven
facets.  Moreover,

\[
\boxed{
0<V_Y<7\quad\Longrightarrow\quad\rho_Y=1.}
\tag{3.6}
\]

Consequently

\[
\boxed{
\#\{Y:t_{\Omega\setminus Y}=6, 0<V_Y<7\}
\leq d\leq2.}
\tag{3.7}
\]

The complete central zero-run classification is:

* if \(V_Y=7\), there is one joint zero-run of length \(10\);
* if \(V_Y=1\) is intermediate, there is one exact length-four run;
* if \(2\leq V_Y\leq6\) is intermediate, there is one joint zero-run of
  length \(V_Y+3\).

There is no seam correction in any of these cases.  For an intermediate
color,

\[
c_Y=V_Y-1,qquad x_Y=6-V_Y.
\tag{3.8}
\]

#### Proof

A six-edge forest on seven vertices is a tree, and maximum degree two
makes it a path.  If it has both central and external vertices, the path
uses an interface.  It cannot use both interfaces: when two interfaces
exist, they enter the two distinct \(02\) and \(13\) postcut state
components.  A connected \(Q\)-subgraph lies in one component of \(G_6\).
Thus \(\rho_Y=1\), proving (3.6)--(3.7).

Deleting the unique interface from an intermediate spanning path leaves
one connected central and one connected external piece.  Hence
\(\kappa_C=\kappa_E=1\), giving (3.8).

Equation (3.5) now rules out \(\sigma_Y=1\): a deleted seam-colored edge
would place central \(Q\)-facets in both postcut central pieces, whereas
\(\kappa_C=1\).  Equivalently, \(b_Y+u_{4,Y}+\sigma_Y=1\), and a positive
\(W_Y\) forces \(b_Y\geq1\).  If \(V_Y=1\), then \(c_Y=W_Y=0\), so
\(u_{4,Y}=1\).  If \(V_Y\geq2\), then

\[
W_Y=c_Y=V_Y-1,qquad b_Y=1,qquad u_{4,Y}=0,
\]

which is exactly one run of length \(V_Y+3\).

If \(V_Y=7\), all six edges are central and connected.  The same seam
argument applies, and

\[
W_Y=6,qquad b_Y=1,qquad u_{4,Y}=0,
\]

giving one run of length ten.  \(\square\)

### Theorem 3.4 (multiplicity-five equality rigidity)

Suppose

\[
t_Q=5,qquad\rho_Y=0,qquad c_Y>0,qquad x_Y>0.
\tag{3.9}
\]

Then

\[
2\leq V_Y\leq5,qquad
c_Y=V_Y-1,qquad
x_Y=6-V_Y,
\tag{3.10}
\]

and the central joint-zero system is exactly one run of length

\[
V_Y+3.
\tag{3.11}
\]

In particular,

\[
b_Y=1,qquad u_{4,Y}=0,qquad\sigma_Y=0.
\tag{3.12}
\]

Thus an interface-free mixed multiplicity-five color cannot have a
separated central return, an exact four-run, or an artificial seam
concatenation.

#### Proof

The \(Q\)-forest has \(7-5=2\) components.  Since there are no interface
edges and both sectors contain an edge, the central and external induced
forests each have exactly one component.  Therefore

\[
\kappa_C=\kappa_E=1,
\]

which gives (3.10).  As in Theorem 3.3, a seam-colored deleted edge would
put central facets in both postcut pieces, contradicting
\(\kappa_C=1\).  Hence \(\sigma_Y=0\).  Equations (1.7) and (1.10) now give
\(W_Y=V_Y-1,\ b_Y=1,\ u_{4,Y}=0\), proving (3.11)--(3.12).
\(\square\)

### Theorem 3.5 (the saturated braid is a linear forest)

Let

\[
\mathscr S=\{Q\in\tbinom{\Omega}{7}:t_Q=6\}.
\]

The graph induced by \(\mathscr S\) in \(J(11,7)\) is a linear forest.
Each of its components, in the inward orientation and up to reversal,
has one of the forms

\[
C^*,\qquad E^*,\qquad E^*-I-C^*,
\tag{3.13}
\]

where \(C\) denotes \(V_Y=7\), \(E\) denotes \(V_Y=0\), and \(I\) is one
intermediate saturated color.  In particular, no saturated component
contains two intermediate colors or two sector changes.

#### Proof

Two distinct seven-sets share a six-facet exactly when they are adjacent
in \(J(11,7)\), and then that facet is unique.  A saturated color uses all
seven of its facets in a six-edge path.  If saturated colors \(Q,Q'\)
share a facet \(U\), then \(U\) has positive degree in both monochromatic
paths.  Since \(G_6\) has maximum degree two, \(U\) is an endpoint of both.
Each saturated path has two endpoints, so the saturated-color graph has
maximum degree two.  A cycle of saturated colors would concatenate their
monochromatic paths into a cycle of \(G_6\), impossible.

A \(C\)-block and an \(E\)-block cannot meet directly, since their common
facet would have to be both central and external.  An intermediate block
uses the unique interface in its component.  Each retained state component
contains at most one inward interface, so the only possible sector-changing
form is \(E^*-I-C^*\), up to reversal.  \(\square\)

## 4. Exact physical interface modes

We now use the offset order, rather than only the abstract forest.

### Theorem 4.1 (six-mode boundary normal form)

Suppose the left interface is retained.  Necessarily \(s>0\) and \(L\geq1\).
Put

\[
C=C_0,qquad T=T_0,qquad \alpha=T\setminus C,
\]

and let \(U\) be its external predecessor.  The selected witnesses are

\[
C:[L,L+2],qquad
T:[L,L+3],qquad
U:[L-1,L+2].
\tag{4.1}
\]

There is a unique \(\beta\) such that

\[
U=C\mathbin{\dot\cup}\{\beta\},qquad
T=C\mathbin{\dot\cup}\{\alpha\},qquad
\alpha\ne\beta.
\tag{4.2}
\]

Writing

\[
Q=U\cup T,qquad Y=\Omega\setminus Q,
\]

we have

\[
Q=C\mathbin{\dot\cup}\{\alpha,\beta\}
=T\mathbin{\dot\cup}\{\beta\},
\qquad
Y=(\Omega\setminus T)\setminus\{\beta\}.
\tag{4.3}
\]

Also

\[
\beta\in B_{L-1},qquad
B_{L-1}\subseteq C\cup\{\beta\},qquad
\alpha\notin B_{L-1},
\tag{4.4}
\]

and the literal five-cell interval \([L-1,L+3]\) has OR exactly \(Q\).

Exactly one of the following six modes occurs.

* **Start mode:** \(U\) is the initial six-vertex of its state component.
* **Predecessor mode \(P_\delta\):** \(U\) has an incoming external-headed
  edge \(V\to U\), where

  \[
  \delta\in Y\cup\{\alpha\}.
  \]

  Its immediately preceding witnesses are

  \[
  S:[L-1,L+1],qquad
  U:[L-1,L+2],qquad
  V:[L-2,L+1],
  \tag{4.5}
  \]

  with

  \[
  \delta=V\setminus S,qquad
  Y'=(Y\cup\{\alpha\})\setminus\{\delta\}
  \tag{4.6}
  \]

  for the incoming color complement \(Y'\).

If \(\delta=\alpha\), then \(Y'=Y\) and the four cells

\[
B_{L-1},A_0,A_1,A_2
\]

form the exact maximal \(\alpha\)-zero-run between occurrences at
\(B_{L-2}\) and \(A_3\).  If \(\delta=y\in Y\), then the boundary
\(y\)-zero-run begins at \(B_{L-1}\), while the \(\alpha\)-zero-run contains

\[
B_{L-2},B_{L-1},A_0,A_1,A_2
\]

and hence has length at least five.

The right-interface theorem is the exact reversal.  It requires
\(s<m-3\) and \(R\leq463\), and its witnesses are

\[
C:[R-2,R],\quad T:[R-3,R],\quad U:[R-2,R+1],
\]

and, in a predecessor mode, \(V:[R-1,R+2]\).

#### Proof

The common five-set of the left interface edge \(U\to T\) is \(C_0\).
In the left-oriented \(02\) block, the physical \(U\)-witness contains
\([L,L+2]\), begins strictly before \(L\), and has span at most three.
This forces \(U=[L-1,L+2]\).  Its OR has rank six while \(C\) has rank
five, giving the unique \(\beta\).  The only cell of \(U\) outside the
\(C\)-interval is \(B_{L-1}\), proving (4.4).  Joining \(U\) to
\(T=[L,L+3]\) gives the displayed literal five-window and (4.3).

If \(U\) is not a component start, its incoming edge remains in the same
\(02\) state block.  The literal \(02\) schedule gives
\(S=[L-1,L+1]\); containment of \(S\), strict predecessor order, and the
span-three bound then force \(V=[L-2,L+1]\).  The unique coordinate
\(\delta=V\setminus S\) lies outside \(U\), so

\[
\delta\in\Omega\setminus U=Y\cup\{\alpha\},
\]

and complementing \(U\cup V\) gives (4.6).  The sole cell of \(V\) outside
\(U\) is \(B_{L-2}\), so it contains \(\delta\).  The cell \(A_3\) contains
\(\alpha\), because \(T=C\cup\{\alpha\}\).  These observations give the
two zero-run conclusions.  Start versus predecessor is exhaustive, and
the five choices of \(\delta\) are disjoint.  The reversed \(13\) schedule
proves the right case.  If \(L=0\), no left interface exists; if \(L=1\),
a left interface can use only start mode.  Symmetrically, \(R=464\)
forbids a right interface, while \(R=463\) permits only its start mode.
No artificial cell is introduced.  \(\square\)

### Theorem 4.2 (two-interface component sharpening)

If one color uses both interfaces, so that \(\rho_Y=2\), then

\[
\boxed{
x_Y\leq5-V_Y,qquad t_Q\leq5.}
\tag{4.7}
\]

In particular, no multiplicity-six color carries both interfaces.

Let \(a_L,a_R\geq4\) be the lengths of its two boundary joint
\(Y\)-zero-runs.  Then

\[
\boxed{
a_L+a_R\leq11+\sigma_Y\leq12.}
\tag{4.8}
\]

If \(c_Y=0\), both runs have length four, except that the unique seam
correction \(\sigma_Y=1\) can supply one total extra cell.

#### Proof

Two interfaces can occur only at an internal seam.  The left interface is
in the \(02\) state component and the right interface in the distinct
\(13\) state component.  Their external endpoints are distinct because
the rank-six row is injective.

There are \(7-V_Y\) external facets of \(Q\).  Its external \(Q\)-forest
has the two interface endpoints in distinct components, and hence at least
two components.  Therefore

\[
x_Y\leq(7-V_Y)-2=5-V_Y.
\]

The complete \(Q\)-forest likewise has at least two components on seven
vertices, so \(t_Q\leq5\).

The two physical boundary runs are distinct: one maximal run meeting both
ends would have length at least \(m\geq228\) and hence would give
\(V_Y\geq m-3>7\).  Each boundary run contributes \(a-4\) to \(W_Y\), so

\[
(a_L-4)+(a_R-4)
\leq W_Y=c_Y+\sigma_Y.
\]

Since \(2+c_Y\leq t_Q\leq5\), inequality (4.8) follows.  If \(c_Y=0\),
then \(W_Y=\sigma_Y\leq1\), giving the final assertion.  \(\square\)

### Corollary 4.3 (high-star lazy mode is forbidden)

If an interface has \(V_Y=6\), its only external \(Q\)-facet cannot support
an external-external \(Q\)-edge.  Hence \(x_Y=0\).  In Theorem 4.1 the
same-color predecessor mode \(\delta=\alpha\) is therefore impossible.
Such an interface is either a component start or one of the four exchange
modes \(\delta=y\in Y\).

## 5. The \(E=132\) design reduction

The parity theorem becomes particularly rigid at the smallest possible
external size.

### Corollary 5.1 (high-star low-parity branch)

Suppose

\[
E=132,qquad V_Y\geq5\quad\text{for every }Y,qquad
|\mathcal O|\leq7.
\tag{5.1}
\]

Then

\[
\boxed{V_Y=5\quad\text{for every }Y.}
\tag{5.2}
\]

#### Proof

Since \(E\) is even, Corollary 2.3 and \(|\mathcal O|\leq7\) give
\(\mathcal O=\varnothing\).  Thus every \(h_Y=7-V_Y\) is even.  The
assumption \(V_Y\geq5\) gives \(h_Y\in\{0,2\}\), while

\[
\sum_Yh_Y=5E=660=2\binom{11}{4}.
\]

Therefore all \(h_Y=2\), proving (5.2).  \(\square\)

### Theorem 5.2 (design and labelled external-forest normal form)

Assume

\[
E=132,qquad V_Y=5\quad\text{for all }Y.
\tag{5.3}
\]

Then \(\mathcal H\) is a simple \(4\)-\((11,5,2)\) design.  Its lower
parameters are

\[
\lambda_3=8,qquad
\lambda_2=24,qquad
\lambda_1=60,qquad
|\mathcal H|=132.
\tag{5.4}
\]

For every five-set \(S\), let

\[
r(S)=\#\{B\in\mathcal H:B\cap S=\varnothing\}.
\]

Then

\[
\boxed{
r(S)=2-\mathbf1_{\{S\in\mathcal H\}}.}
\tag{5.5}
\]

Consequently the graph \(J(11,5)[\mathcal H]\) is \(5\)-regular, and the
map

\[
\{B,B'\}
\longmapsto
S=\Omega\setminus(B\cup B')
\tag{5.6}
\]

is a bijection from its \(330\) edges to the \(330\) five-sets outside
\(\mathcal H\).

The external part of every length-\(465\) survivor in this branch is
therefore an oriented spanning linear forest in this labelled \(5\)-regular
graph.  It has exactly

\[
s_{\rm ext}=c-b_H+d
\tag{5.7}
\]

components and

\[
R_{\rm ext}=E-s_{\rm ext}
\tag{5.8}
\]

edges.  The label in (5.6) of each selected edge is exactly its nonstart
external rank-five source.  At most \(d\leq2\) distinct terminal components
are marked for the inward interfaces, and every marked end must satisfy
one of the six physical modes in Theorem 4.1.

#### Proof

Equation (5.3) says every four-set belongs to exactly

\[
h_Y=7-V_Y=2
\]

blocks of \(\mathcal H\).  This is precisely a simple
\(4\)-\((11,5,2)\) design.  The standard double counts give

\[
\lambda_z
=2\frac{\binom{11-z}{4-z}}{\binom{5-z}{4-z}},
\qquad0\leq z\leq3,
\]

which yields (5.4).

For a fixed five-set \(S\), inclusion-exclusion over its points gives

\[
\begin{aligned}
r(S)
&=132-5\cdot60+\binom52 24
  -\binom53 8+\binom54 2
  -\mathbf1_{\{S\in\mathcal H\}}\\
&=2-\mathbf1_{\{S\in\mathcal H\}},
\end{aligned}
\]

proving (5.5).

If \(S\notin\mathcal H\), its two disjoint design blocks are distinct
five-subsets of the six-set \(\Omega\setminus S\).  They meet in four
points and form one Johnson edge labelled \(S\).  If \(S\in\mathcal H\),
there is only one disjoint design block and no such edge.  This proves the
bijection (5.6).

For regularity, fix \(B\in\mathcal H\).  Each of its five four-subsets
\(Y\) lies in a unique second design block \(B_Y\).  The five partners
\(B_Y\) are distinct, since a different five-set cannot share two
different four-subsets with \(B\).  Thus every \(B\) has degree five.

The complements of the external rank-six vertices are exactly the blocks
of \(\mathcal H\).  Their external-headed edges form a spanning linear
forest with \(R_{\rm ext}\) edges, so its component count is

\[
E-R_{\rm ext}=s_{\rm ext}.
\]

Lemma 3.1 identifies every nonstart source with the edge label (5.6).
The endpoint orientation points at most one terminal of a component into
the central sector; the two possible interfaces lie in distinct state
components.  This proves the final assertions.  \(\square\)

Theorem 5.2 is a necessary finite reduction, not a sufficiency theorem for
a physical word.  It leaves a sharply specified problem: a labelled
spanning path cover of a simple \(4\)-design, compatible with the central
sliding path, the perfect inclusion matching, and at most two six-mode
terminal attachments.

## 6. Why the new restrictions do not yet close \(k=11\)

The parity theorem does not force \(|\mathcal O|\leq7\).  It permits
\(|\mathcal O|\geq8\) for even \(E\) and \(|\mathcal O|\geq9\) for odd
\(E\).  The design branch in Theorem 5.2 is not proved empty.

The sector-component theorems are strongest at multiplicities five and
six, but the global count does not force such a color.  For example,

\[
182\cdot1+137\cdot2=456,
\qquad182+137=319,
\]

so the extreme totals \(c=6,\ M_7=11\) admit a multiplicity profile using
only ones and twos.  Likewise, when \(M_7=0\), the profile

\[
204\cdot1+126\cdot2=456
\]

has all \(330\) colors supported and the required duplicate excess \(126\).
These are only multiplicity ledgers, but they show why the saturated-color
lemmas alone cannot finish the proof.

The exact remaining finite incompatibility can now be stated more tightly.

> **Ordered-shadow gate — unproved.**  There is no family
> \(\mathcal H\subset\binom{\Omega}{5}\), no physical central order
> \(D_0,\ldots,D_{q-1}\), and no endpoint-ordered rainbow spanning linear
> forest simultaneously satisfying:
>
> 1. the shadow identities (2.3)--(2.5) and the parity alternatives of
>    Corollary 2.3;
> 2. the rank-at-most-three sliding-window and seam identities
>    (1.6)--(1.10);
> 3. the two-color edge encoding of Lemma 3.1;
> 4. the sector-component and saturated-braid restrictions of Section 3;
> 5. the six physical boundary modes and double-interface bounds of
>    Section 4; and
> 6. in the branch (5.3), the labelled design-forest reduction of
>    Theorem 5.2.

This gate is genuinely stronger than the remaining gate in the physical
lift: two of its scalar test ledgers are now impossible, and its saturated
and interface sectors have explicit normal forms.  Its nonexistence is not
proved here.

## 7. Adversarial audit

1. **Simultaneity.**  Theorem 2.1 uses one common omitted five-set family
   \(\mathcal H\).  It does not optimize the \(330\) values \(V_Y\)
   independently.

2. **Parity convention.**  Since \(7\) is odd,
   \(h_Y=7-V_Y\) is odd exactly when \(V_Y\) is even.  The total parity is
   \(|\mathcal O|\equiv5E\equiv E\), not its complement.

3. **Small-cycle classification.**  Point links include every incident
   facet and are binary \(2\)-cycles.  The six- and seven-facet exclusions
   treat all possible support sizes; they do not assume the cycle is
   support-minimal.

4. **Ledger audit.**  Ledger (13.1) has seven, not eleven, even-\(V_Y\)
   rows.  Ledger (13.2) has four.  These are forbidden cardinalities for
   the relevant parity of \(E\).

5. **Facet completeness.**  The \(Q\)-subgraph always has all seven
   six-facets as vertices, including isolated ones, because \(G_6\) spans
   the complete six-set layer.  This is why its component count is
   \(7-t_Q\).

6. **Seam accounting.**  The central component identity is
   \(V_Y-c_Y=b_Y+u_{4,Y}+\sigma_Y\).  Equality cases with one central
   component exclude \(\sigma_Y=1\); no deleted seam edge has been
   artificially concatenated.

7. **Two interfaces.**  The two physical interfaces belong to distinct
   \(02\) and \(13\) state components.  Therefore a color using both has
   at least two full \(Q\)-components, not merely two external marked
   vertices.

8. **Boundary witnesses.**  The intervals in Theorem 4.1 follow from
   strict endpoint order and the span-three rank-six bound.  If an outer
   predecessor position is unavailable, that predecessor mode is deleted;
   no virtual entry is used.

9. **Design inclusion-exclusion.**  Formula (5.5) includes its final
   five-point term
   \(-\mathbf1_{\{S\in\mathcal H\}}\).  Omitting it would incorrectly give
   two disjoint design blocks for a design block \(S\) itself.

10. **Scope.**  Theorem 5.2 is necessary only.  No existence of a simple
    \(4\)-\((11,5,2)\) design, of the required labelled path cover, or of a
    common physical word is asserted.

The parity-shadow proof, the endpoint-sector proof, and the physical
interface proof were derived and audited independently.  No identified
seam, endpoint, witness-distinctness, or artificial-concatenation exception
changes the stated conclusions.
