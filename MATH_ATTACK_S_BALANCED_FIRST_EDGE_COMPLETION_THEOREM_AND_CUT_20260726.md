# Lane S: prescribed balanced first edges, exact residual completion, and the first Hall obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Outcome

Fix \(s\ge2\). Let \(J=[2s]\), let

\[
 \mathcal X=\binom Js,
 \qquad \mathcal Y=\binom J{s+1},
 \qquad \mathcal D=\mathcal D_s,
 \qquad N=|\mathcal D|=\operatorname{Cat}_s,
\]

and put

\[
 \overline{\mathcal D}=\{J\setminus P:P\in\mathcal D\}.
\]

The required local object is a vertex partition of the middle-levels
inclusion graph into the prescribed paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s=J\setminus P,
 \qquad P\in\mathcal D.                              \tag{0.1}
\]

Suppose the first two edges

\[
 P\subset U_P\supset Q_P                              \tag{0.2}
\]

are prescribed for every root, with

\[
 U_P=P\cup\{b_P\},
 \qquad Q_P=P\setminus\{a_P\}\cup\{b_P\},
 \qquad a_P\in P,\quad b_P\notin P.                  \tag{0.3}
\]

This note proves the following exact boundary.

1. After the prescribed prefixes are contracted, completion is equivalent
   to one integral residual \(b\)-factor together with all labelled
   complement-pair cuts. This handles every \(X/Y\) resource exactly once
   and enforces identity endpoint monodromy.
2. The unlabelled degree part is an ordinary integral network-flow problem.
   Its necessary-and-sufficient residual Gale--Hall inequalities are given
   explicitly.
3. An acyclic Ordered-Hall support with unique diagonal reachability is a
   concrete sufficient theorem which enforces the same monodromy.
4. Pure first-insertion balance is automatic in every completed factor:

   \[
     \#\{P:b_1(P)=j\}\le \operatorname{Cat}_{s-1}
     \quad(j\in J),
     \qquad
     \#\{P:b_1(P)=2s\}=\operatorname{Cat}_{s-1}.       \tag{0.4}
   \]

5. Nevertheless, a clean prefix layer with the exact canonical, optimally
   balanced histogram can fail completion. At \(s=3\) a singleton residual
   \(X\)-cut has demand \(2\) and capacity \(1\). The deficit is exactly one.
   This is the smallest possible nonempty cut and the first possible rank.

Thus the proposed implication

\[
 \text{balanced clean first-edge layer}
 \quad\Longrightarrow\quad
 \text{complete port path factor}                     \tag{0.5}
\]

is false. The first missing condition is residual Hall restitution; after
that, labelled complement monodromy remains a separate condition. No
constant-one conclusion follows from balance alone.

## 1. Clean prescribed prefixes

The counts

\[
 |\mathcal X|=\binom{2s}s=(s+1)N,
 \qquad
 |\mathcal Y|=\binom{2s}{s+1}=sN                     \tag{1.1}
\]

will be used throughout. Every Dyck word starts with \(1\), while the
complement of a Dyck word starts with \(0\), so

\[
 \mathcal D\cap\overline{\mathcal D}=\varnothing.     \tag{1.2}
\]

Call the prescription (0.2) **clean** when

\[
 \begin{aligned}
  &U_P\ne U_R &&(P\ne R),\\
  &Q_P\ne Q_R &&(P\ne R),\\
  &Q_P\notin\mathcal D\cup\overline{\mathcal D}
       &&(P\in\mathcal D).
 \end{aligned}                                        \tag{1.3}
\]

These conditions are necessary. Distinct paths cannot own the same upper
vertex \(U\) or the same lower vertex \(Q\), and every member of
\(\mathcal D\cup\overline{\mathcal D}\) is already reserved as a prescribed
endpoint.

Write

\[
 \mathcal U_0=\{U_P:P\in\mathcal D\},
 \qquad
 \mathcal Q=\{Q_P:P\in\mathcal D\}.                  \tag{1.4}
\]

Delete the saturated root and first-upper vertices and retain the induced
residual graph

\[
 G_\eta=M(J)-\bigl(\mathcal D\cup\mathcal U_0\bigr), \tag{1.5}
\]

whose shores are

\[
 \mathcal X'=\mathcal X\setminus\mathcal D,
 \qquad
 \mathcal Y'=\mathcal Y\setminus\mathcal U_0.        \tag{1.6}
\]

Define the residual demand

\[
 r_\eta(X)=2-\mathbf1_{\{X\in\mathcal Q\}}
              -\mathbf1_{\{X\in\overline{\mathcal D}\}}
       \quad(X\in\mathcal X'),
 \qquad
 r_\eta(Y)=2\quad(Y\in\mathcal Y').                  \tag{1.7}
\]

Cleanliness makes the two indicator families in (1.7) disjoint. Thus the
new residual starts \(Q_P\) and the terminal ports \(J\setminus P\) have
demand one, while every other residual lower vertex and every residual
upper vertex have demand two.

### Lemma 1.1 (exact residual totals and distances)

Both residual shore-demand totals equal

\[
                  2(s-1)N.                            \tag{1.8}
\]

Moreover

\[
 d_{M(J)}(Q_P,J\setminus P)=2(s-1)                    \tag{1.9}
\]

for every \(P\in\mathcal D\).

#### Proof

There are \(sN\) residual lower vertices. The \(N\) vertices in
\(\mathcal Q\), the \(N\) terminal ports, and the remaining
\((s-2)N\) lower vertices contribute

\[
 N+N+2(s-2)N=2(s-1)N.                                 \tag{1.10}
\]

There are \((s-1)N\) residual upper vertices, all of demand two, proving
(1.8).

Since \(Q_P=P-a_P+b_P\), while \(J\setminus P\) is disjoint from \(P\)
and contains \(b_P\), one has

\[
                  Q_P\cap(J\setminus P)=\{b_P\}.      \tag{1.11}
\]

The Johnson distance between the two \(s\)-sets is therefore \(s-1\), and
the corresponding distance in the bipartite middle-levels graph is twice
that number. This proves (1.9). \(\square\)

## 2. Exact residual paired-factor theorem

For a residual vertex set \(S\subseteq V(G_\eta)\), define

\[
 \kappa_\eta(S)=
 \#\left\{P\in\mathcal D:
   \left|\{Q_P,J\setminus P\}\cap S\right|=1\right\}. \tag{2.1}
\]

Thus \(\kappa_\eta(S)\) is the number of prescribed labelled residual
endpoint pairs separated by \(S\).

### Theorem 2.1 (exact completion theorem)

A clean prefix prescription (0.2) extends to a path partition (0.1) if and
only if there is a simple residual edge set

\[
                         F'\subseteq E(G_\eta)          \tag{2.2}
\]

such that

\[
 d_{F'}(v)=r_\eta(v)\qquad(v\in V(G_\eta))             \tag{2.3}
\]

and, for every residual vertex set \(S\),

\[
 \boxed{
 |F'\cap\delta_{G_\eta}(S)|\ge\kappa_\eta(S).}       \tag{2.4}
\]

#### Proof

If a completion exists, delete the two prescribed first edges from every
path. The remaining paths run from \(Q_P\) to \(J\setminus P\), give the
degrees (2.3), and every path whose two endpoints are separated by \(S\)
uses a distinct edge of the cut. Hence (2.4) is necessary.

Conversely, (2.3) makes every component of \(F'\) a path or a cycle. Its
degree-one vertices are exactly

\[
                  \mathcal Q\mathbin{\dot\cup}
                  \overline{\mathcal D},               \tag{2.5}
\]

so there are \(N\) path components. Let \(K\) be one such component and
take \(S=V(K)\). No selected edge leaves \(S\), so (2.4) gives

\[
                         \kappa_\eta(S)=0.              \tag{2.6}
\]

The two degree-one vertices of \(K\) must consequently be one prescribed
pair \(Q_P,J\setminus P\). Indeed, two starts, two terminals, or a start
\(Q_P\) and a wrong terminal \(J\setminus R\) with \(R\ne P\) would give
\(\kappa_\eta(S)=2\).

By (1.8), the residual edge count is

\[
                         |F'|=2(s-1)N.                  \tag{2.7}
\]

Each of the \(N\) correctly paired paths has length at least \(2(s-1)\) by
(1.9). Equality in (2.7) therefore forces every path to have exactly that
length and leaves no edge for a cycle component. Prepending
\(P-U_P-Q_P\) gives \(N\) length-\(2s\) complement paths. Their degree
partition owns every lower and upper vertex exactly once. This is (0.1).
\(\square\)

### Monodromy interpretation

Any residual degree factor induces a permutation \(\pi\) of the roots by

\[
             Q_P\leadsto J\setminus\pi(P).             \tag{2.8}
\]

The port requirement often denoted \(p_0=p_s\) is exactly

\[
                         \pi=\mathrm{id}.               \tag{2.9}
\]

The degree equations do not imply (2.9). If one component joins \(Q_P\)
to \(J\setminus R\), \(P\ne R\), its vertex set has cut size zero and
paired-cut demand two. Thus (2.4) is the exact labelled subtour condition,
not a histogram or marginal condition.

Equivalently, adjoin virtual edges

\[
                  Q_P(J\setminus P),\qquad P\in\mathcal D. \tag{2.10}
\]

Then a desired completion is precisely a spanning two-factor in which every
cycle contains exactly one virtual edge.

### Literal realizability

Write a completed path as

\[
 X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s.                                  \tag{2.11}
\]

On \(J\sqcup\{\infty\}\), put

\[
                   Z_t=\{\infty\}\cup(J\setminus Y_t). \tag{2.12}
\]

If \(X_{t+1}=X_t-p_{t+1}+q_{t+1}\), the omitted-coordinate sequence of

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{s-1},X_s,X_0              \tag{2.13}
\]

is

\[
 q_1,p_1,q_2,p_2,\ldots,q_s,p_s,\infty,               \tag{2.14}
\]

a permutation of all \(2s+1\) coordinates. Hence (2.13) is a literal
minimum odd-graph wreath. The theorem stays integral inside one exact
factor and does not replace literal contiguous-OR states by fractional or
unlabelled surrogates.

## 3. The exact network-flow part

For \(A\subseteq\mathcal X'\) and \(Y\in\mathcal Y'\), write

\[
 d_A(Y)=|\{X\in A:X\subset Y\}|.                       \tag{3.1}
\]

### Theorem 3.1 (residual Gale--Hall theorem)

The residual graph contains a simple integral edge set satisfying all
degree equations (2.3) if and only if, for every
\(A\subseteq\mathcal X'\),

\[
 \boxed{
 2|A|-|A\cap\mathcal Q|-|A\cap\overline{\mathcal D}|
 \le
 \sum_{Y\in\mathcal Y'}\min\{2,d_A(Y)\}.}             \tag{3.2}
\]

Equivalently, for every \(A\subseteq\mathcal X'\) and
\(B\subseteq\mathcal Y'\),

\[
 r_\eta(A)
 \le e_{G_\eta}(A,\mathcal Y'\setminus B)+2|B|.       \tag{3.3}
\]

#### Proof

Use the network

\[
 \sigma\longrightarrow\mathcal X'
       \longrightarrow\mathcal Y'\longrightarrow\tau, \tag{3.4}
\]

with capacities \(r_\eta(X)\) on the first arcs, capacity one on every
allowed inclusion edge, and capacity two on the last arcs. The total
required flow is \(2(s-1)N\) on both shores by Lemma 1.1.

A cut whose source side contains \(A\) on the lower shore and \(B\) on the
upper shore has capacity

\[
 r_\eta(\mathcal X'\setminus A)
 +e_{G_\eta}(A,\mathcal Y'\setminus B)+2|B|.           \tag{3.5}
\]

Max-flow/min-cut gives (3.3). Minimizing its right side independently at
each upper vertex gives (3.2). Integral capacities give an integral flow,
and the unit inclusion-edge capacities make the resulting \(b\)-factor
simple. \(\square\)

Theorem 3.1 uses every residual \(X/Y\) vertex with its exact required
degree. It does **not** enforce the labelled endpoint permutation; Theorem
2.1 still requires (2.4).

### Corollary 3.2 (exact restitution form)

For \(A\subseteq\mathcal X'\), put

\[
 \begin{aligned}
 \chi_{\mathcal U_0}(A)
   &=\sum_{Y\in\mathcal U_0}\min\{2,d_A(Y)\},\\
 \Sigma(A)
   &=\sum_{Y\in\mathcal Y}\min\{2,d_A(Y)\}
       -\bigl(2|A|-|A\cap\overline{\mathcal D}|\bigr).
 \end{aligned}                                        \tag{3.6}
\]

Then residual degree completion is equivalent to

\[
 \boxed{
 \chi_{\mathcal U_0}(A)
 \le \Sigma(A)+|A\cap\mathcal Q|
 \quad(A\subseteq\mathcal X').}                       \tag{3.7}
\]

Moreover

\[
 \Sigma(A)=(s-2)|A|+|A\cap\overline{\mathcal D}|
   -\sum_{Y\in\mathcal Y}(d_A(Y)-2)_+.                \tag{3.8}
\]

#### Proof

Separate the selected upper vertices from the sum in (3.2) and rearrange.
For (3.8), use

\[
 \sum_{Y\in\mathcal Y}d_A(Y)=s|A|,
 \qquad
 \min\{2,d\}=d-(d-2)_+.                               \tag{3.9}
\]

\(\square\)

For a singleton \(A=\{X\}\), let

\[
 c_0(X)=|\{U\in\mathcal U_0:X\subset U\}|.           \tag{3.10}
\]

Since every \(s\)-set has exactly \(s\) upper neighbours, (3.2) becomes

\[
 \boxed{
 c_0(X)\le s-2+
       \mathbf1_{\{X\in\mathcal Q\}}+
       \mathbf1_{\{X\in\overline{\mathcal D}\}}.}  \tag{3.11}
\]

Thus an ordinary internal \(X\)-vertex incident with \(s-1\) selected
first colours must itself be selected as one of the restitution vertices
\(Q_P\); if all \(s\) of its upper neighbours are selected, completion is
impossible.

### Corollary 3.3 (forced root-saturated first colours)

Exactly \(\operatorname{Cat}_{s-1}\) upper vertices have \(s\) Dyck
facets. They are

\[
 \mathcal F^+=\{\,11w:w\in\mathcal D_{s-1}\,\}.       \tag{3.12}
\]

Every completed first-edge layer must contain all of \(\mathcal F^+\) in
\(\mathcal U_0\). If \(U=11w\), its first segment is necessarily

\[
                 (U\setminus\{b\})-U-(U\setminus\{1\}) \tag{3.13}
\]

for one selected \(b\in U\setminus\{1\}\).

#### Proof

An \((s+1)\)-set \(U\) has \(s+1\) lower facets. At least the facet obtained
by removing coordinate \(1\) is non-Dyck whenever \(U\) has Dyck facets,
so it has at most \(s\) Dyck facets.

For \(U=11w\), deleting coordinate \(1\) gives the non-Dyck word \(01w\).
Deleting coordinate \(2\) gives \(10w\), which is Dyck, and deleting a
selected coordinate inside \(w\) lowers all later heights by two while the
initial \(11\) supplies exactly that buffer. Hence all other \(s\) facets
are Dyck.

Conversely, suppose \(U\) has \(s\) Dyck facets. It contains coordinate
\(1\). If its second selected coordinate were later than position \(2\),
deleting that coordinate would leave only one selected position in a
prefix too long to satisfy the Dyck inequalities. Hence \(U\) begins
\(11\). Deleting the second coordinate produces \(10w\); its being Dyck
forces \(w\in\mathcal D_{s-1}\). This proves (3.12).

If such a \(U\) were not selected as a first upper vertex, then after all
Dyck roots are deleted it would have only one residual lower neighbour but
residual demand two, violating the upper singleton flow cut. Thus it is
selected. Its \(s\) Dyck facets are possible roots, while its unique
non-Dyck facet \(U\setminus\{1\}\) is the only possible clean \(Q\), proving
(3.13). Here \(s\ge2\), so \(w\) ends in \(0\); consequently \(01w\)
ends in \(0\), whereas every member of \(\overline{\mathcal D}\) ends in
\(1\). Thus this last facet is not a complementary port. \(\square\)

This forced Catalan tranche is already a quarter of all roots
asymptotically. Choosing its insertion targets changes the required
terminal pairing, even though its residual start \(U\setminus\{1\}\) is
fixed. It is therefore a terminal-rematching problem, not independent
rootwise balancing.

## 4. Ordered-Hall completion with identity monodromy

The paired cuts have a useful constructive sufficient form. Let
\(\vec G\) be an acyclic directed subgraph of \(G_\eta\), with no arc
entering \(\mathcal Q\) and no arc leaving
\(\overline{\mathcal D}\). Form the successor bipartite graph

\[
 B_{\vec G}:
 (V(G_\eta)\setminus\overline{\mathcal D})_L
 \longleftrightarrow
 (V(G_\eta)\setminus\mathcal Q)_R,                    \tag{4.1}
\]

joining \(u_L\) to \(v_R\) when \(u\to v\) is an arc of \(\vec G\). Both
shores have \(2(s-1)N\) vertices.

Also form the labelled reachability graph from \(\mathcal Q\) to
\(\overline{\mathcal D}\), joining \(Q_P\) to \(J\setminus R\) when
\(\vec G\) contains a directed path between them.

### Theorem 4.1 (residual Ordered-Hall theorem)

Assume

\[
 |N_{B_{\vec G}}(S)|\ge |S|
 \quad\text{for every subset of the left shore},       \tag{4.2}
\]

and assume that the unique perfect matching of the reachability graph is

\[
                         Q_P\longmapsto J\setminus P.   \tag{4.3}
\]

Then the prescribed first-edge layer completes to (0.1).

#### Proof

Hall's theorem gives a perfect matching in (4.1). Select its directed
arcs. Every nonterminal vertex has one successor, and every nonsource
vertex has one predecessor. Acyclicity makes these arcs a spanning path
cover with sources exactly \(\mathcal Q\) and sinks exactly
\(\overline{\mathcal D}\).

Its endpoint pairing is a perfect matching in the reachability graph, so
(4.3) makes it the diagonal complement pairing. There are \(N\) paths and
\(2(s-1)N\) selected arcs. Lemma 1.1 forces every path to have its minimum
length \(2(s-1)\). Prepending the prescribed prefixes proves the result.
\(\square\)

For checking (4.3), it is enough that every diagonal reachability is
present and that the off-diagonal root digraph

\[
 P\longrightarrow R
 \quad\Longleftrightarrow\quad
 Q_P\leadsto J\setminus R,\quad P\ne R               \tag{4.4}
\]

is acyclic. A directed cycle in (4.4) produces a second perfect matching;
conversely, the symmetric difference of any second perfect matching with
the diagonal contains such a cycle.

## 5. Sharp first-insertion balance in every completed factor

For a completed row rooted at \(P\), let \(d_P(i)\) be the deletion time of
\(i\in P\), and let \(u_P(j)\) be the insertion time of \(j\notin P\). Thus

\[
                         b_1(P)=j
 \quad\Longleftrightarrow\quad u_P(j)=1.               \tag{5.1}
\]

### Lemma 5.1 (exact pair-time law)

For distinct \(i,j\in J\), every complete port factor satisfies

\[
\begin{aligned}
 \operatorname{Cat}_{s-1}
 ={}&\#\{P:i\in P,\ j\notin P,\ u_P(j)\le d_P(i)\}\\
 &+\#\{P:j\in P,\ i\notin P,\ u_P(i)\le d_P(j)\}.
                                                               \tag{5.2}
\end{aligned}
\]

#### Proof

Exact \(X\)-ownership and \(Y\)-ownership give respectively

\[
 \binom{2s-2}{s-2},
 \qquad
 \binom{2s-2}{s-1}                                    \tag{5.3}
\]

occurrences containing both \(i\) and \(j\). If the two coordinates start
on the same side of a row, their \(Y\)- and \(X\)-pair counts agree. If
\(i\in P\) and \(j\notin P\), the \(Y\)-count exceeds the \(X\)-count by
one exactly when \(u_P(j)\le d_P(i)\). The symmetric statement holds after
interchanging \(i,j\). Summing rowwise and subtracting gives (5.2), because

\[
 \binom{2s-2}{s-1}-\binom{2s-2}{s-2}
 =\frac1s\binom{2s-2}{s-1}
 =\operatorname{Cat}_{s-1}.                            \tag{5.4}
\]

\(\square\)

### Theorem 5.2 (universal sharp coordinate cap)

Let

\[
                   h_j=\#\{P\in\mathcal D:b_1(P)=j\}. \tag{5.5}
\]

Then every completed factor satisfies

\[
 h_1=0,
 \qquad h_j\le\operatorname{Cat}_{s-1}\quad(j\ne1),
 \qquad h_{2s}=\operatorname{Cat}_{s-1}.               \tag{5.6}
\]

Consequently

\[
                    \max_j h_j=\operatorname{Cat}_{s-1}. \tag{5.7}
\]

#### Proof

Every Dyck port contains coordinate \(1\), so \(h_1=0\). Apply Lemma 5.1
to the pair \(1,j\). Its second term is absent, because no port omits
coordinate \(1\). Every row with first insertion \(j\) belongs to the first
event in (5.2), proving \(h_j\le\operatorname{Cat}_{s-1}\).

Every Dyck port omits coordinate \(2s\). Put

\[
 d_P=d_P(1),\qquad u_P=u_P(2s).                        \tag{5.8}
\]

Lemma 5.1 gives

\[
 \#\{P:u_P\le d_P\}=\operatorname{Cat}_{s-1}.         \tag{5.9}
\]

In one row, the number of lower states containing both \(1\) and \(2s\)
is \((d_P-u_P)_+\). Exact lower-state ownership therefore gives

\[
 \sum_P(d_P-u_P)_+
 =\binom{2s-2}{s-2}
 =(s-1)\operatorname{Cat}_{s-1}.                       \tag{5.10}
\]

Only the rows counted in (5.9) can contribute, and each contribution is at
most \(s-1\). Equality in (5.10) forces all
\(\operatorname{Cat}_{s-1}\) counted rows to have

\[
                         u_P=1,\qquad d_P=s.            \tag{5.11}
\]

Thus exactly that many rows insert \(2s\) first. This proves (5.6)--(5.7).
\(\square\)

The exact ratio is

\[
 \frac{\operatorname{Cat}_{s-1}}{\operatorname{Cat}_s}
 =\frac{s+1}{2(2s-1)}
 =\frac14+\frac{3}{4(2s-1)}.                          \tag{5.12}
\]

Hence first-insertion coordinate balance is not the missing theorem: every
completed factor already has the sharp cap, while coordinate \(2s\) is
forced to attain it.

## 6. A clean optimally balanced layer which cannot complete

Take \(s=3\), \(J=[6]\), and

\[
                 \mathcal D_3=\{123,124,125,134,135\}. \tag{6.1}
\]

Prescribe the five first segments

\[
\begin{array}{c}
 123-1236-136,\\
 124-1246-146,\\
 125-1245-245,\\
 134-1234-234,\\
 135-1235-235.
\end{array}                                             \tag{6.2}
\]

### Proposition 6.1 (singleton obstruction of deficit one)

The prescription (6.2) is clean and has the exact canonical
first-insertion histogram

\[
                         2e_2+e_4+2e_6.                 \tag{6.3}
\]

Nevertheless it has no degree completion, and hence no port path-factor
completion. The failed residual Hall cut is the singleton

\[
                         A=\{126\},                     \tag{6.4}
\]

on which (3.2) reads \(2\le1\).

#### Proof

The selected upper vertices are

\[
             1236,1246,1245,1234,1235,                 \tag{6.5}
\]

all distinct. The selected internal lower vertices are

\[
             136,146,245,234,235,                       \tag{6.6}
\]

all distinct. None belongs to

\[
 \mathcal D_3\cup\overline{\mathcal D_3}
 =\{123,124,125,134,135,456,356,346,256,246\}.         \tag{6.7}
\]

Thus (6.2) is clean.

Its first inserted coordinates are \(6,6,4,2,2\), proving (6.3). The
canonical first-return counts are

\[
 \operatorname{Cat}_0\operatorname{Cat}_2=2,
 \quad
 \operatorname{Cat}_1\operatorname{Cat}_1=1,
 \quad
 \operatorname{Cat}_2\operatorname{Cat}_0=2,          \tag{6.8}
\]

at targets \(2,4,6\), respectively. Hence (6.3) is the canonical sharp-cap
histogram, with maximum \(2=\operatorname{Cat}_2\).

The lower vertex \(126\) is neither selected in (6.6) nor a terminal port,
so its residual demand is two. Its three upper neighbours are

\[
                         1236,1246,1256.                 \tag{6.9}
\]

The first two have been saturated and deleted by (6.5), leaving only the
edge \(126-1256\). Thus the right side of (3.2) is one while the left side
is two. \(\square\)

This obstruction is minimal in three senses:

* its Hall set has one vertex, the least possible nonempty cardinality;
* its integral deficit is one, the least possible positive deficit;
* \(s=3\) is the first rank at which a clean prescribed layer can fail.

For the last claim, the separate rank-\(1\) problem is forced. At \(s=2\), with

\[
 \mathcal D_2=\{12,13\},\quad
 \overline{\mathcal D}_2=\{34,24\},                   \tag{6.10}
\]

the clean internal vertices are \(14,23\). Direct cleanliness, not a search,
leaves exactly two possible complete prefix systems:

\[
 \begin{array}{ll}
 12-123-23,&13-134-14,\\
 \text{or}\qquad
 12-124-14,&13-123-23.
 \end{array}                                            \tag{6.11}
\]

Indeed, root \(12\) can cleanly use only \(123-23\) or \(124-14\):
the alternative second facets are respectively the root \(13\) and the
terminal \(24\). Root \(13\) can cleanly use only \(123-23\) or
\(134-14\), for the same reason. Distinctness of both first-upper and
first-lower resources forces the two cross-pairings displayed in (6.11).

They complete, respectively, as

\[
 \begin{array}{ll}
 12-123-23-234-34,&13-134-14-124-24,\\
 \text{or}\qquad
 12-124-14-134-34,&13-123-23-234-24.
 \end{array}                                            \tag{6.12}
\]

Thus no smaller rank supplies a clean counterexample.

## 7. Exact proved and conditional boundary

The following statements are proved.

1. A clean prescribed first-edge layer completes exactly when the residual
   degree equations and all labelled pair cuts (2.4) have a common integral
   solution.
2. The degree equations alone have the exact integral network-flow
   criterion (3.2), equivalently the restitution inequalities (3.7).
3. The paired cuts enforce the identity endpoint permutation
   \(Q_P\leadsto J\setminus P\); ordinary Hall does not.
4. The Ordered-Hall hypotheses (4.2)--(4.3) are sufficient for a literal,
   vertex-exact completion.
5. Every completed factor automatically has the sharp first-insertion cap
   \(\operatorname{Cat}_{s-1}\), attained at coordinate \(2s\).
6. The rank-three prescription (6.2) meets that optimal balance and all
   prefix injectivity/cleanliness conditions, but fails a singleton
   residual cut by one.

Accordingly, any positive root-scale theorem must construct the first
layer and prove, simultaneously,

\[
 \begin{array}{ll}
 \text{(i)}&\text{all residual Gale--Hall restitution cuts},\\
 \text{(ii)}&\text{all labelled complement-pair cuts, or an Ordered-Hall}\\
             &\text{support with unique diagonal reachability}.
 \end{array}                                            \tag{7.1}
\]

Cap balance, point histograms, distinct \(U_P\)'s, and distinct clean
\(Q_P\)'s do not imply (i), as (6.2) proves. Even (i) does not imply (ii),
because it permits a nonidentity endpoint permutation. The exact missing
gate is therefore a paired residual expansion theorem, not a scalar
balanced-matching theorem.
