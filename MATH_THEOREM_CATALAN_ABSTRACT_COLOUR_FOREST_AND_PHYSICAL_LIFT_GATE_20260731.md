# An all-dimension Catalan colour forest and the exact physical lift gate

Date: 2026-07-31  
Status: unconditional abstract incidence/determinant construction; exact
physical realization criterion; no all-dimension Hamilton realization is
claimed

## 1. Boolean diamond incidence

Fix \(m\ge2\), let \(\Omega=[2m]\), and put

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1}.
\]

Write

\[
 K=\operatorname {Cat}_m={1\over m+1}\binom{2m}m,
 \qquad N=|\mathcal L|=|\mathcal U|=mK,
 \qquad M=|\mathcal X|=(m+1)K=N+K.
 \tag{1.1}
\]

Let \(B_m\) be the bipartite inclusion graph on
\(\mathcal L\sqcup\mathcal U\), with \(L\sim U\) exactly when
\(L\subset U\).  It is regular of degree

\[
                         d=\binom{m+1}2.                 \tag{1.2}
\]

Indeed a lower set has \(m+1\) absent coordinates and chooses two, while an
upper set chooses two of its \(m+1\) coordinates to delete.

Every incidence \(L\subset U\) determines one Boolean diamond and one
Johnson edge.  If \(U\setminus L=\{a,b\}\), put

\[
 \psi(L,U)=
 \bigl\{L\cup\{a\},L\cup\{b\}\bigr\}\in E(J(2m,m)).
 \tag{1.3}
\]

The map \(\psi:E(B_m)\to E(J(2m,m))\) is a bijection, with inverse

\[
             AB\longmapsto(A\cap B,A\cup B).             \tag{1.4}
\]

Thus every abstract colour edge is already a genuine Boolean diamond.  The
remaining issue is whether the resulting Johnson edges assemble into one
physical Hamilton cycle.

## 2. A balanced colour forest exists for every \(m\)

The BTK symmetric-chain decomposition pairs every rank-\((m-1)\) set \(L\)
with the unique rank-\((m+1)\) set two steps above it on its chain.  Every
rank-\((m+1)\) set is paired back to the rank-\((m-1)\) member two steps below
it.  Hence these pairs form a perfect matching \(M_0\) of \(B_m\).

Deleting \(M_0\) leaves a \((d-1)\)-regular bipartite graph, so it has a
perfect matching \(M_1\).  The graph \(M_0\cup M_1\) is a disjoint union of
alternating cycles.  If their numbers of \(M_1\)-edges are
\(r_1,\ldots,r_c\), then every \(r_j\ge2\),

\[
                 \sum_j r_j=N,\qquad c\le N/2.            \tag{2.1}
\]

Consequently

\[
             \sum_j(r_j-1)=N-c\ge N/2\ge K=N/m.          \tag{2.2}
\]

Choose exactly \(K\) edges \(S\subseteq M_1\), taking at most \(r_j-1\)
from the \(j\)-th alternating cycle, and set

\[
                             H_m=M_0\cup S.                \tag{2.3}
\]

Here \(M_0\) is the perfect inclusion matching
\(\sigma:\mathcal L\to\mathcal U\), while \(H_m\) is the strictly larger
degree-\(\{1,2\}\) colour graph containing the \(K\) extra edges \(S\).
The construction is made directly in the full inclusion graph \(B_m\);
it is not the duplicate--hole projection of a preselected repair core.
Nor does it assert that the \(N\) lifted edges \(\Psi(M_0)\) form a
spanning \(K\)-path forest on \(\mathcal X\).  Since
\(|\mathcal X|-|M_0|=M-N=K\), that conclusion would follow if
\(\Psi(M_0)\) were independently proved to be a spanning linear forest,
but this is a separate physical condition.

### Theorem 2.1 (all-\(m\) abstract colour forest)

For every \(m\ge2\), \(H_m\subseteq B_m\) has all of the following
properties.

1. On each shore, exactly \(K\) vertices have degree two and \(N-K\) have
   degree one; equivalently its load profile is \(1^{N-K}2^K\).
2. Every component is a path with one endpoint on each shore.
3. Its unique perfect matching is \(M_0\).
4. Its \(N\times N\) biadjacency determinant is \(\pm1\).

#### Proof

The partial matching \(S\) has \(K\) different endpoints on each shore, so
the degree statement is immediate.  A cycle in \(M_0\cup S\) would have to
be a complete alternating cycle of \(M_0\cup M_1\), which the choice of
\(S\) forbids.  Hence every component is a path.  Since \(M_0\) meets every
vertex, both terminal edges of every path lie in \(M_0\); the path has odd
length and opposite-shore endpoints.  It is balanced and has the forced
alternating matching \(M_0\).  Thus the full graph has exactly one perfect
matching.  In the determinant expansion exactly its permutation term is
nonzero, proving determinant \(\pm1\). \(\square\)

This theorem removes the abstract Hall, balanced-component, and determinant
gates in every dimension.  It does **not** construct the required middle
Hamilton cycle.

## 3. Exact physical lift criterion

For any \(H\subseteq B_m\), let

\[
                  \Psi(H)=(\mathcal X,\{\psi(e):e\in H\})
 \tag{3.1}
\]

be its lifted graph on the rank-\(m\) layer.

### Theorem 3.1 (Hamilton lift equivalence)

There is a Hamilton cycle \(P\) of \(J(2m,m)\) with colour-incidence graph
\(G(P)=H\) if and only if

\[
 \deg_{\Psi(H)}(X)=2\quad(X\in\mathcal X),
 \qquad \Psi(H)\text{ is connected}.                       \tag{3.2}
\]

In that case \(P\) is exactly the unique cycle \(\Psi(H)\).

#### Proof

The inverse formula (1.4) says that an occurrence of a Johnson edge has
exactly the colour incidence from which it came.  Therefore the physical
edge set of any putative \(P\) is forced to be \(\Psi(H)\).  It is a
Hamilton cycle precisely when it is spanning, connected, and two-regular.
\(\square\)

### Corollary 3.2 (the missing \(K\)-path quantifier)

Write \(H=\operatorname{graph}(\sigma)\cup S\), where \(\sigma\) is its
unique inclusion matching and \(|S|=K\).  If \(\Psi(H)\) is Hamiltonian,
then deleting the \(K\) lifted \(S\)-edges leaves
\(\Psi(\operatorname{graph}\sigma)\), a spanning linear forest with
exactly \(K\) path components (trivial paths are allowed).  Conversely,
\(\Psi(H)\) is Hamiltonian exactly when this spanning \(K\)-path forest
condition holds and the \(K\) lifted \(S\)-edges reconnect its path
components cyclically, giving every middle vertex degree two and one
component.

Thus the spanning \(K\)-path property asked of \(\sigma\) is a necessary
physical gate; it is not a consequence of \(\sigma\) being a perfect
inclusion matching.

### Proposition 3.3 (standard BTK matching is physically branched)

Use the standard BTK convention which scans coordinates
\(0,1,\ldots,2m-1\), pairs a one with the latest unmatched zero, and moves
two ranks upward by changing the first two free zeros to ones.  Let

\[
                         E_m=\{0,2,\ldots,2m-2\}.
\]

For every \(j=0,\ldots,m-1\), put \(L_j=E_m\setminus\{2j\}\).  Then the
BTK two-rank matching adds

\[
 \sigma(L_0)\setminus L_0=\{0,2m-1\},\qquad
 \sigma(L_j)\setminus L_j=\{2j-1,2j\}\quad(j\ge1).       \tag{3.4}
\]

Hence all \(m\) lifted Johnson edges
\(\psi(L_j,\sigma(L_j))\) are incident with \(E_m\), and

\[
                  \deg_{\Psi(\operatorname{graph}\sigma)}(E_m)=m.
                                                                  \tag{3.5}
\]

In particular, for every \(m\ge3\) this standard BTK matching does not
lift to a path forest, and no choice of additional \(S\)-edges can turn
its lift into a Hamilton cycle.

#### Proof

For \(j=0\), the unmatched zeros in the indicated scan begin at
coordinates \(0\) and \(2m-1\).  For \(j\ge1\), the first two free zeros
are \(2j-1,2j\).  This gives (3.4) directly.  In each case one of the two
rank-\(m\) endpoints is \(L_j\cup\{2j\}=E_m\).  The \(m\) lower sets are
distinct, and every matching edge incident with \(E_m\) must delete one
of its \(m\) coordinates first, so the degree is exactly \(m\).
\(\square\)

The count is automatically tight:

\[
 |E(H_m)|=N+K=M=|\mathcal X|,
 \qquad
 \sum_{X\in\mathcal X}\deg_{\Psi(H_m)}(X)=2M.              \tag{3.3}
\]

Thus (3.2) is an exact zero-defect endpoint-balance condition, not a scalar
capacity condition.  An overload at one middle set forces a hole elsewhere.

## 4. Cap-two blocks and the outgoing sign

Assume \(H\) has upper degrees one or two.  If a doubled upper vertex \(U\)
has lower neighbours \(L_0,L_1\), then its two lifted Johnson edges share a
middle endpoint exactly when

\[
 |(U\setminus L_0)\cap(U\setminus L_1)|=1,
 \tag{4.1}
\]

or equivalently

\[
                         |L_0\cup L_1|=m.                  \tag{4.2}
\]

Indeed the two two-element deletion sets identify the endpoints of the two
Johnson edges.  Distinct such edges share one endpoint exactly when the
deletion sets share one coordinate.

### Corollary 4.1 (cap-two realization)

Suppose (3.2) holds.  Equal upper colours form the required contiguous
one- or two-edge blocks if and only if (4.1) holds at every doubled upper
vertex.

When it holds, suppose in addition that \(H\) has a specified perfect
matching \(M_0\), unique in the forest \(H_m\) of Theorem 2.1.  At every
doubled upper block, one local edge belongs to \(M_0\) and the other to
\(H\setminus M_0\).  Orient the Hamilton cycle and put

\[
 \varepsilon_U=+1
 \quad\Longleftrightarrow\quad
 \text{the nonmatching edge is traversed before the \(M_0\)-edge}.       \tag{4.3}
\]

There is a uniform outgoing directed repair with retained transversal
\(M_0\) if and only if all \(\varepsilon_U\) have the same sign.  Reversing
the Hamilton cycle reverses every sign simultaneously.  Under this
condition the cut seams are distinct: each doubled block cuts the same
cyclic side, and the boundary middle vertices of different blocks are
different vertices of the Hamilton cycle.

Thus determinant \(\pm1\) does not imply directed repair.  It certifies the
unique common colour transversal but sees neither the middle endpoint
balance (3.2), the local block condition (4.1), nor the global orientation
sign (4.3).  The frozen negative \(m=3\) fixture in
scratch/catalan_directed_repair_finite_m2_m3_20260731.audit.json has a
balanced incidence forest and a unique matching, but its forced block signs
are mixed.

## 5. The exact abstract ear ledger

Write \(K'=\operatorname {Cat}_{m+1}\) and \(N'=(m+1)K'\).  An abstract
balanced-forest lift which retains the old graph and adds vertex pairs has
the following minimal normal form.

* An **isolated pair** adds one new vertex on each shore and their matching
  edge.
* An **attached pair ear** also adds one nonmatching edge from one new
  vertex to an opposite-shore endpoint of an old path.  It extends that path
  by two vertices.  One old endpoint and one new vertex become degree two,
  one on each shore.

To change the degree-two count from \(K\) to \(K'\), exactly

\[
 a=K'-K={3m\over m+2}K                                  \tag{5.1}
\]

attached pair ears are necessary and sufficient.  The total number of new
vertex pairs is \(s=N'-N\), so the remaining

\[
 b=s-a=(N'-K')-(N-K)
   =mK'-(m-1)K={3m^2+m+2\over m+2}K                     \tag{5.2}
\]

pairs are isolated.  The new edge count is

\[
 s+a=(N'+K')-(N+K).                                      \tag{5.3}
\]

Every ear exposes a degree-one pivot in the biadjacency matrix, so Laplace
expansion preserves determinant magnitude one.  If each new matching edge
is designated outgoing and every attachment edge nonmatching, the abstract
orientation label is preserved as well.

For \(m=3\to4\), this ledger is exactly nine attached ears and thirty-two
isolated pairs.  A one-ear recursion which otherwise carries the old forest
intact is therefore short by eight degree-two pairs.  This is an obstruction
to that restricted graph recursion, not to a bulk rethreading.

The unsolved step is now precise: label these abstract ears by incidences of
\(B_{m+1}\) so that their lift satisfies simultaneously (3.2), (4.1), and
(4.3).  BTK supplies \(M_0\), and the regularity argument supplies the
abstract forest, but neither assertion supplies that physical Hamilton
realization.

## 6. Deterministic finite replay and scope

Run

    python3 scratch/audit_catalan_abstract_colour_forest_lift_m2_m6_sparse_20260731.py

The audit constructs the standard BTK matching \(\sigma\), a deterministic
disjoint matching \(\tau\), and the cycle-broken colour forest
\(H=\operatorname{graph}(\sigma)\cup S\) independently for
\(m=2,3,4,5,6\).  Sparse leaf peeling certifies the unique determinant
term without forming a dense \(792\times792\) matrix at \(m=6\).

The lift of \(\sigma\) alone is spanning, acyclic, and has exactly \(K\)
components in all five audited dimensions.  It is a \(K\)-path forest only
at \(m=2\).  Its exact degree histograms for \(m=2,\ldots,6\) are

\[
\begin{array}{c|c}
m&\text{degree histogram of }\Psi(\operatorname{graph}\sigma)\\ \hline
2&1^4\,2^2\\
3&1^{12}\,2^6\,3^2\\
4&1^{40}\,2^{20}\,3^8\,4^2\\
5&1^{140}\,2^{70}\,3^{30}\,4^{10}\,5^2\\
6&1^{504}\,2^{252}\,3^{112}\,4^{42}\,5^{12}\,6^2.
\end{array}
\]

The first literal counterexample is \(m=3\):
\(E_3=\{0,2,4\}=\mathtt{0x15}\) has three incident
\(\sigma\)-edges, exactly as Proposition 3.3 predicts.

For the larger \(H\)-lift the replay gives:

\[
\begin{array}{c|c|c|c|c}
m&\#\text{ components}&\text{degree-deficit units}
 &\text{degree-overload units}&\text{bad doubled }U\\ \hline
2&1&1&1&0\\
3&2&5&5&2\\
4&3&27&27&2\\
5&15&104&104&14\\
6&44&387&387&46.
\end{array}
\]

There are no degree-zero middle vertices in these five deterministic
\(H\)-lifts, but degree-one deficits are balanced by degree-above-two
overloads.  Thus even connectedness at \(m=2\) does not repair endpoint
balance.  At \(m=3,\ldots,6\), connectedness also fails; local cap-two
endpoint sharing fails in the displayed numbers of doubled upper colours.
The orientation-sign test is inapplicable until both earlier gates pass.

Proved here:

* an inclusion-compatible balanced colour forest with determinant
  \(\pm1\) exists for every \(m\ge2\);
* the exact Hamilton, local-block, and orientation-sign realization gates;
* the standard BTK matching is physically branched for every \(m\ge3\);
  and
* the exact abstract two-coordinate ear ledger.

Not proved here:

* that the constructed \(H_m\) has a Hamilton physical lift;
* that a different perfect inclusion matching passes or fails the spanning
  \(K\)-path gate in every dimension;
* that some other forest satisfying the same determinant certificate has
  such a lift in every dimension; or
* an unrestricted directed Catalan repair theorem.
