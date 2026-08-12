# The \(K=11\) phi-repair graph: exact regularity and a 74-repair theorem

Date: 2026-07-25

Scope: the exact \(c=6,d=0\) certificate branch only. This is a pure
hand proof; no enumeration or solver output is used.

## 0. Exact branch and outcome

Let \(\Omega=[11]\), let \(\mathcal H\) be a simple
\(4\)-\((11,5,2)\) design, and put

\[
 \mathcal K=\binom{\Omega}{5}\setminus\mathcal H.
\]

Thus \(|\mathcal H|=132\) and \(|\mathcal K|=330\).

In the exact branch under consideration:

* the four external \(\mathcal H\)-paths use \(128\) distinct upper
  \(\mathcal K\)-labels;
* the central quotient uses the complementary \(202\) members of
  \(\mathcal K\) as connector source colors;
* its \(126\) \(\mathcal H\)-source turns are pairwise disjoint on their
  \(252\) incident \(\mathcal K\)-vertices;
* all six unused source colors lie in \(\mathcal H\).

There is a canonical bijection

\[
 \phi:\binom{\Omega}{4}\longrightarrow\mathcal K.              \tag{0.1}
\]

The directed phi-repair graph \(\mathcal R\) on the \(330\) four-sets is
defined by the possible lower intersection colors of a central
\(\mathcal K\)-connector source. The main theorem is

\[
 \boxed{
 d^+_{\mathcal R}(C)=d^-_{\mathcal R}(C)=6
 \quad\text{for every }C.
 }                                                               \tag{0.2}
\]

Moreover, \(\mathcal R\) has no directed \(2\)-cycle.

Let \(E\) be the \(128\)-set of four-colors covered by the external paths,
and let \(M\) be its \(202\)-element complement. Equivalently,
\(\phi(E)\) are the external upper labels and \(\phi(M)\) are the central
\(\mathcal K\)-connector colors. Then the bipartite version of the induced
repair graph satisfies

\[
 \boxed{
 \operatorname{match}\bigl(\mathcal R[M,M]\bigr)\ge74.
 }                                                               \tag{0.3}
\]

Only \(191\) of the \(202\) externally missing four-colors must be repaired
to reach upper support \(319\). Even if all \(126\) H-star turns repair
distinct missing colors, the K-connectors must supply only

\[
 191-126=65                                                     \tag{0.4}
\]

distinct cross-repairs. Equation (0.3) guarantees \(74\), leaving nine
units of worst-case slack.

Therefore the K-connector color-level Hall/cut structure cannot obstruct
the residual demand of \(65\) obtained when at least \(126\) (or, using
the nine units of slack, at least \(117\)) distinct useful H repairs are
available. Any color-level obstruction must first force fewer than \(117\)
useful H repairs; otherwise it must use the simultaneous quotient-path,
port, lower-shadow, or no-lazy constraints.

## 1. The phi bijection

Fix a four-set \(C\subset\Omega\). Since \(\mathcal H\) is a
\(4\)-\((11,5,2)\) design, exactly two design blocks contain \(C\). Write
them uniquely as

\[
 C\cup\{x\},
 \qquad C\cup\{y\},
 \qquad x\ne y.                                                  \tag{1.1}
\]

Define

\[
 \boxed{
 \phi(C)=\Omega\setminus(C\cup\{x,y\}).
 }                                                               \tag{1.2}
\]

The two blocks in (1.1) are adjacent vertices of the design graph
\(G=J(11,5)[\mathcal H]\). Their edge label is exactly (1.2). The
certified identity \(E(G)\cong\mathcal K\) therefore shows both that
\(\phi(C)\in\mathcal K\) and that \(\phi\) is a bijection: intersection
\(C\) and complementary-union label \(\phi(C)\) are the two labels of the
same edge of \(G\).

Put

\[
 Q=\phi(C),
 \qquad L=\Omega\setminus Q=C\sqcup\{x,y\}.                     \tag{1.3}
\]

The six five-subsets of \(L\) are its facets. Exactly two are in
\(\mathcal H\), namely

\[
 L\setminus\{x\}=C\cup\{y\},
 \qquad
 L\setminus\{y\}=C\cup\{x\}.                                   \tag{1.4}
\]

The remaining four are in \(\mathcal K\):

\[
 \boxed{
 D_c=L\setminus\{c\}
 =(C\setminus\{c\})\cup\{x,y\},
 \qquad c\in C.
 }                                                               \tag{1.5}
\]

These are precisely the four vertices of the K4 transition class with
source color \(Q\).

## 2. The six exact repairs and the derangement

A central transition with source \(Q=\phi(C)\) chooses two distinct class
vertices \(D_c,D_d\). Its lower intersection color is

\[
\begin{aligned}
 Y_{c,d}
 &=D_c\cap D_d\\
 &=L\setminus\{c,d\}\\
 &=(C\setminus\{c,d\})\cup\{x,y\}.
\end{aligned}                                                    \tag{2.1}
\]

Thus there are exactly \(\binom42=6\) allowed repairs. Define a directed
edge

\[
 C\longrightarrow Y_{c,d}                                     \tag{2.2}
\]

for every pair \(\{c,d\}\subset C\). This defines the repair graph
\(\mathcal R\) and proves

\[
 d^+_{\mathcal R}(C)=6.                                        \tag{2.3}
\]

Every repair in (2.1) contains \(x,y\) and omits \(c,d\), so
\(Y_{c,d}\ne C\). This is the phi-derangement: source \(\phi(C)\) can
never repair its own dual four-color \(C\). Realizing intersection \(C\)
would require the two facets in (1.4), and those are the H facets excluded
from the central K4 class.

There is also no directed two-cycle. Inside \(L\), the two H facets are
exactly those missing \(x\) and \(y\). If \(C\to Y_{c,d}\), reversing the
arrow would require the facets missing \(c\) and \(d\) to lie in
\(\mathcal H\). By (1.5) both lie in \(\mathcal K\), a contradiction.

## 3. Exact indegree six

Fix a target four-set \(Y\). For a two-set
\(Z\subset\Omega\setminus Y\), put \(L=Y\cup Z\) and define

\[
 n(Y,Z)
 =\#\{H\in\mathcal H:Z\subset H\subset L\}.                    \tag{3.1}
\]

Because \(L\) has size six, its H facets number one when
\(\Omega\setminus L\in\mathcal H\) and two when
\(\Omega\setminus L\in\mathcal K\). Hence \(n(Y,Z)\in\{0,1,2\}\).
An incoming repair \(C\to Y\) with union \(L=C\cup Y=Y\cup Z\)
occurs exactly when the two H facets of \(L\) both contain \(Z\), namely
when

\[
 n(Y,Z)=2.                                                       \tag{3.2}
\]

We count such \(Z\)'s without symmetry assumptions on the design.

Let

\[
 N_j(Y)=\#\{H\in\mathcal H:|H\cap Y|=j\}.
\]

The derived parameters are

\[
 \lambda_4=2,\qquad \lambda_3=8.
\]

Therefore \(N_4(Y)=2\), and double-counting triples of \(Y\) gives

\[
 N_3(Y)+4N_4(Y)=\binom43\lambda_3=32,
\]

so

\[
 N_3(Y)=24.                                                      \tag{3.3}
\]

The two blocks containing \(Y\) are adjacent in \(G\), contributing one
edge whose two endpoints both have intersection four with \(Y\).
Each of these two vertices has degree five in \(G\). Besides their common
edge, each has four neighbors obtained by deleting one point of \(Y\),
and hence having intersection three with \(Y\). Thus there are exactly

\[
 2\cdot4=8                                                       \tag{3.4}
\]

edges of \(G\) between an \(N_4\)-block and an \(N_3\)-block.

Now consider the \(21\) six-sets \(L=Y\cup Z\), equivalently the five-set
labels \(Q=\Omega\setminus L\) disjoint from \(Y\). Among the \(21\)
five-sets disjoint from \(Y\), exactly six lie in \(\mathcal H\), because
\(N_0(Y)=6\). Hence exactly

\[
 21-6=15                                                        \tag{3.5}
\]

are K labels, and therefore correspond to two-H-facet six-sets.

Classify these fifteen K-labeled six-sets by how many of their two missing
H-facet indices lie in \(Y\):

* zero indices in \(Y\): the unique edge between the two \(N_4\)-blocks,
  so there is one;
* one index in \(Y\): exactly the eight \(N_4\)--\(N_3\) edges in (3.4);
* two indices in \(Y\): exactly the incoming repairs in (3.2).

Consequently their number is

\[
 15-1-8=6.                                                       \tag{3.6}
\]

This proves \(d^-_{\mathcal R}(Y)=6\), and establishes (0.2).

For completeness, the value \(N_0(Y)=6\) follows from the standard
intersection equations. With

\[
 \lambda_2=24,\quad\lambda_1=60,\quad|\mathcal H|=132,
\]

successive inversion gives

\[
 (N_4,N_3,N_2,N_1,N_0)=(2,24,60,40,6).                         \tag{3.7}
\]

## 4. The 202/128 cut and a matching of size 74

Let

\[
 E\sqcup M=\binom{\Omega}{4},
 \qquad |E|=128,\quad |M|=202,                                 \tag{4.1}
\]

where \(\phi(E)\) are the external K labels and \(\phi(M)\) are the
central K connector source colors.

Because \(\mathcal R\) is \(6\)-in/\(6\)-out regular, every vertex cut is
balanced:

\[
 e_{\mathcal R}(M,E)=e_{\mathcal R}(E,M).                       \tag{4.2}
\]

The right side is at most the full outdegree mass of \(E\):

\[
 e_{\mathcal R}(E,M)\le6|E|=768.                               \tag{4.3}
\]

The total number of arcs leaving \(M\) is \(6|M|=1212\). Therefore

\[
 \boxed{
 e_{\mathcal R}(M,M)\ge1212-768=444.
 }                                                               \tag{4.4}
\]

View \(\mathcal R[M,M]\) as a bipartite graph, with a left copy of \(M\)
for connector sources and a right copy for repaired four-colors. Both
maximum degrees are at most six.

By Konig's theorem, a maximum matching and a minimum vertex cover have
the same size, say \(q\). A vertex cover of size \(q\) meets at most
\(6q\) edges. Equation (4.4) therefore gives \(6q\ge444\), and hence

\[
 \boxed{q\ge74.}                                                \tag{4.5}
\]

This proves (0.3).

## 5. Consequence for the upper-support route

The external paths already cover the \(128\) colors in \(E\). Upper
support at least \(319\) requires at least

\[
 319-128=191
\]

distinct colors from \(M\).

The \(126\) disjoint H-star turns can contribute at most \(126\) distinct
members of \(M\). Even granting all of them distinct and useful, the K
connectors must contribute at least \(65\) additional distinct members of
\(M\). The matching (4.5) assigns \(74\) distinct connector sources in
\(\phi(M)\) to \(74\) distinct repair targets in \(M\).

Thus the isolated phi-repair Hall problem has nine units of slack. It
cannot prove impossibility of the exact branch unless a separate argument
first limits the 126 H turns to fewer than 117 useful distinct repairs.

This is a color-level theorem. It does not assert that the matched repairs
can simultaneously be realized inside the required two quotient paths.
It ignores:

* which of the four class vertices are free ports after the H segments;
* degree two and acyclicity in the 204-node quotient;
* the lower \(B\)-shadow choices at the same ports;
* the physical inequalities \(a_i\ne b_{i+1}\) and
  \(a_i\ne b_{i+2}\).

Those coupled constraints are now the only possible source of an
obstruction along this route.

## 6. The analogous lower derangement

The same phi-polarity gives an unconditional lower-shadow fact. Fix a
central K vertex

\[
 D=\phi(C),
 \qquad \Omega\setminus D=C\sqcup\{x,y\}.
\]

The two H source colors disjoint from \(D\) are

\[
 C\cup\{x\},\qquad C\cup\{y\},
\]

and the four K source colors are

\[
 (C\setminus\{c\})\cup\{x,y\},
 \qquad c\in C.
\]

Because the \(126\) H-star segments are disjoint on K vertices, the two
neighbors of \(D\) in the central source path can never be the two H
colors simultaneously. But their intersection would equal \(C\) only
for precisely that H--H pair. Therefore every defined central lower
shadow at \(D\) obeys

\[
 \boxed{B(D)\ne\phi^{-1}(D).}                                  \tag{6.1}
\]

More exactly:

* at an internal singleton K vertex, both neighboring source colors are K, and the
  six possible lower shadows are the same six distance-two repairs in
  (2.1);
* at an internal segmented K vertex, one source neighbor is a fixed H color and the
  other is K. If the H facet is \(L\setminus\{x\}\), its four possible
  lower shadows are

  \[
  L\setminus\{x,c\}
  =(C\setminus\{c\})\cup\{y\},
  \qquad c\in C,                                                 \tag{6.2}
  \]

  and similarly with \(x,y\) interchanged.

Thus the lower side is also a derangement, but it is not governed solely
by the 6-regular repair graph: \(252\) segmented ports use four-choice
mixed H--K repairs, while \(78\) singleton ports use six-choice K--K
repairs. The H-segment allocation couples these choices to the same
quotient ports used by the upper matching.

This explains why the upper 74-matching does not settle lower support
\(319\). A genuine obstruction, if one exists, must be a coupled
two-shadow port theorem, not an upper-color Hall deficiency.

## 7. A 252-port lower-shadow SDR

There is likewise no Hall obstruction if one retains the H-segment port
lists but temporarily forgets that two ports must be paired by one common
K connector.

Each of the \(126\) selected H colors contributes two endpoint ports. Fix
one such port: it is an incident design-graph edge \(D\) at a block
\(H\). Among the five facets of \(H\), exactly one is forbidden at this
port, namely

\[
 C_D=H\cap H',
\]

where \(H'\) is the other endpoint of the design edge labelled \(D\).
Choosing the H--H pair would reproduce \(C_D\), but disjointness of the
H-star segments forbids using \(H'\) as the other source neighbor at
\(D\). The four K source neighbors give exactly the other four facets of
\(H\).

Form the bipartite port--facet graph:

* the left side consists of the \(252\) selected H-segment ports;
* a port at \(H\) is adjacent to the four facets of \(H\) other than its
  forbidden \(C_D\);
* the right side is \(\binom{\Omega}{4}\).

Every left vertex has degree four. Every four-set belongs to exactly two
H blocks, and each selected H block contributes only two ports. Therefore
every right vertex has degree at most four.

For every set \(X\) of ports, edge counting gives

\[
 4|X|=e(X,N(X))\le4|N(X)|.
\]

Thus \(|N(X)|\ge|X|\), and Hall's theorem yields:

\[
 \boxed{
 \text{the 252 H-segment ports admit pairwise distinct lower }B
 \text{ colors from their exact four-element lists.}
 }                                                               \tag{7.1}
\]

This automatically gives distinct B facets at the two ports of each H
turn, the color-level form of the first no-lazy inequality.

Equation (7.1) is again a relaxation. At a real connector, the K source
color is shared by its two endpoint ports, and all 202 connector colors
must be distinct. A choice of one B facet at a port uniquely determines
which of its four local K sources is used, but an arbitrary SDR need not
pair equal source choices at two compatible ports. Hence (7.1) proves
only:

> lower facet availability by itself has no Hall deficiency.

Together, the 74 upper repairs and the 252 lower port SDR eliminate both
one-sided color-list routes. Any obstruction must couple the same
connector simultaneously to:

1. two compatible quotient ports;
2. its upper repair \(Y\);
3. the two adjacent lower facets \(B\);
4. global degree-two, acyclicity, and both no-lazy inequalities.

## 8. Exact coupled shadow-count constraints

Although they do not yet contradict the 74-repair and 252-port SDRs, the
two support requirements impose the following unconditional common
structure.

In this branch the \(456\) source colors are distinct: \(126\) are in
\(\mathcal H\) and all \(330\) members of \(\mathcal K\) occur once.
Along each source path,

\[
 B_i=S_i\cap S_{i+1}.
\]

If \(B_i=B_{i+1}=C\), then

\[
 S_i=C\cup\{b_i\},\qquad
 S_{i+1}=C\cup\{a_i\},
\]

and the next equality forces \(b_{i+1}=a_i\). This violates the first
physical inequality. Hence equal B colors never occur on consecutive
source edges.

For a fixed four-set \(C\), all five-set extensions of \(C\) form a
seven-vertex clique. Since the source vertices are globally distinct and
two consecutive C-colored edges are forbidden, the C-colored source
edges form a matching on these seven extensions. Therefore

\[
 \boxed{\operatorname{mult}_B(C)\le3.}                          \tag{8.1}
\]

Now let a multiset of \(456\) values have support \(s\ge319\). If \(u\)
support colors occur exactly once, then the \(s-u\) nonsingleton colors
consume at least one unit of the duplicate excess \(456-s\). Thus

\[
 s-u\le456-s,
\]

and

\[
 \boxed{u\ge2s-456\ge182.}                                     \tag{8.2}
\]

Apply this separately to the B and Y shadow multisets. Each has at least
182 singleton colors. Since the full color universe has size330, at least

\[
 182+182-330=34                                                \tag{8.3}
\]

four-colors occur exactly once as B and exactly once as Y. More broadly,
the two supports intersect in at least

\[
 319+319-330=308                                               \tag{8.4}
\]

colors.

At every paired turn,

\[
 B_i\subseteq S_i,\qquad Y_i\subseteq D_i,\qquad S_i\cap D_i=\varnothing,
\]

so

\[
 B_i\cap Y_i=\varnothing.                                      \tag{8.5}
\]

In fact

\[
 B_i\cup Y_i
 =\Omega\setminus\{a_i,b_i,a_{i+1}\}.                           \tag{8.6}
\]

Consequently the unique B and Y occurrences of each of the at least34
colors in (8.3) lie at different turns.

Equations (8.1)--(8.6) are the strongest immediate counting/parity
consequences of the two \(319\)-support conditions. They are mutually
consistent with the one-sided Hall constructions above; no contradiction
follows without using which upper and lower choices share the same
connector ports.
