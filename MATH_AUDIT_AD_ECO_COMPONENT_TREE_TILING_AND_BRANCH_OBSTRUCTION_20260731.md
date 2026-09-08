# ECO incidence trees as ordinary-tree tilings

Date: 2026-07-31  
Status: exact combinatorial equivalence, exact path-network theorem, and
smallest abstract branching obstruction; no physical ECO-selection theorem

## 0. Scope

This note concerns only the **incidence-tree skeleton** of an ECO
hypertree.  It does not by itself prove any of the following physical rows:

* a common product cube or dynamic availability of the selected hexagons;
* component faithfulness of every literal toggle;
* owner alignment or extension to an upper transversal;
* private/laminar occurrence routing;
* residence, deeper-shadow, socket, voltage, or compiler preservation.

Consequently, throughout this note the word `hypertree` means the
combinatorial incidence condition unless all those extra hypotheses are
stated separately.

## 1. Exact ordinary-tree tiling equivalence

Let \(V\) be a finite set with \(|V|\ge2\).  Let \({\cal T}\) be a finite
family of labelled atoms, and let

\[
                   S_t\subseteq V,\qquad r_t=|S_t|\ge2
                                                        \tag{1.1}
\]

be the component support of atom \(t\).  Write \(B(V,{\cal T})\) for the
bipartite incidence graph with parts \(V,{\cal T}\).

An **ordinary-tree tiling certificate** consists of a tree \(A\) on
vertex set \(V\) such that, for every \(t\),

\[
                         Q_t:=A[S_t]                   \tag{1.2}
\]

is connected and

\[
               E(A)=\mathop{\dot\bigcup}_{t\in{\cal T}}E(Q_t).
                                                        \tag{1.3}
\]

Thus \(Q_t\) is an induced subtree on exactly \(r_t\) vertices and has
exactly \(r_t-1\) edges.  The phrase "size \(r_t-1\)" below always means
edge size.

### Theorem 1.1 (incidence tree iff ordinary-tree tiling)

The incidence graph \(B(V,{\cal T})\) is a tree if and only if an
ordinary-tree tiling certificate exists.

More precisely, in the forward direction one may choose an arbitrary
tree \(R_t\) on each set \(S_t\), and then

\[
                         A=\bigcup_{t\in{\cal T}}R_t     \tag{1.4}
\]

is an ordinary-tree tiling certificate.

#### Proof

Suppose first that \(B(V,{\cal T})\) is a tree.  Two distinct supports
intersect in at most one vertex: if \(x,y\in S_t\cap S_u\) with
\(x\ne y\), then

\[
                         x-t-y-u-x
\]

is a cycle in \(B\).  In particular, edges chosen in two different
\(R_t\)'s cannot coincide.

The incidence-tree edge count gives

\[
 \sum_t r_t=|V|+|{\cal T}|-1,
 \qquad
 \sum_t(r_t-1)=|V|-1.                                \tag{1.5}
\]

The graph \(A\) in (1.4) is connected.  Indeed, replace every length-two
piece \(x-t-y\) of an incidence path in \(B\) by the \(x\)-to-\(y\) path
inside \(R_t\).  By (1.5), \(A\) has \(|V|-1\) distinct edges, and hence
is a tree.

It remains to check inducedness.  If an edge \(xy\in R_u\), with
\(u\ne t\), had both endpoints in \(S_t\), then \(x,y\in S_u\cap S_t\),
contrary to the first paragraph.  Therefore

\[
                            A[S_t]=R_t,
\]

and the edge sets of these induced subtrees partition \(E(A)\).

Conversely, suppose (1.2)--(1.3) hold.  Each \(Q_t\) is a subtree, so

\[
                          |S_t|=|E(Q_t)|+1.             \tag{1.6}
\]

The incidence graph \(B\) is connected: if \(xy\) is an edge of \(A\),
then it lies in a unique \(Q_t\), and the two-edge walk \(x-t-y\) in
\(B\) replaces \(xy\); lifting an \(A\)-path in this way connects any two
vertices of \(V\).  Finally,

\[
 |E(B)|=\sum_t|S_t|
       =\sum_t\bigl(|E(Q_t)|+1\bigr)
       =|V|-1+|{\cal T}|
       =|V(B)|-1.                                     \tag{1.7}
\]

A connected graph with one fewer edge than vertices is a tree.  This
proves the converse. \(\square\)

### Corollary 1.2 (ECO unit expansion)

For an ECO family, where \(r_t\le3\), a binary atom has one possible local
tree, while a ternary atom has three possible two-edge local trees.  Once
these local trees have been chosen, incidence acyclicity is exactly the
assertion that their edges form a disjoint partition of one ordinary
component tree.

This corollary audits a necessary convention in any unit-expanded
formulation: merely writing a set-theoretic union of local trees and asking
that the union be a tree is insufficient unless edge-disjointness/rank
faithfulness is also imposed.  For example, two identical binary local
trees have a tree as their set-theoretic union but a four-cycle in their
bipartite incidence graph.

## 2. A fixed component path gives a unit-flow polytope

Fix the ordinary component tree to be the path

\[
                    A=v_0v_1\cdots v_N,
\]

with edges \(e_i=v_{i-1}v_i\), \(1\le i\le N\).  Let \({\cal C}\) be any
catalogue of allowed atoms whose supports induce connected subpaths.  For
each \(t\in{\cal C}\), write

\[
 E(Q_t)=\{e_{a_t+1},e_{a_t+2},\ldots,e_{b_t}\},
 \qquad 0\le a_t<b_t\le N.                           \tag{2.1}
\]

Parallel labelled atoms with the same pair \((a_t,b_t)\) are allowed.
Consider the exact-cover relaxation

\[
 P_A=\left\{x\in\mathbb R_{\ge0}^{\cal C}:
       \sum_{t:\,a_t<i\le b_t}x_t=1
       \quad(1\le i\le N)\right\}.                  \tag{2.2}
\]

### Theorem 2.1 (exact unit-flow representation)

Make a directed acyclic multigraph \(D_A\) on nodes \(0,1,\ldots,N\),
with one arc \(a_t\to b_t\) for every \(t\in{\cal C}\).  Then \(P_A\)
is exactly the nonnegative unit \(0\)-to-\(N\) flow polytope of \(D_A\).
In particular, \(P_A\) is integral; every vertex is the incidence vector
of a directed \(0\)-to-\(N\) path, equivalently an exact consecutive
tiling of \(E(A)\) by atom supports.

#### Proof

Let

\[
                       c_i(x)=\sum_{a_t<i\le b_t}x_t
                                                        \tag{2.3}
\]

be the load across the \(i\)-th path cut.  At an internal node
\(i\in\{1,\ldots,N-1\}\), subtraction gives

\[
             c_i(x)-c_{i+1}(x)
             =\operatorname{in}_x(i)-\operatorname{out}_x(i).       \tag{2.4}
\]

Moreover,

\[
                     c_1(x)=\operatorname{out}_x(0),
 \qquad             c_N(x)=\operatorname{in}_x(N).                 \tag{2.5}
\]

Thus (2.2) implies unit source flow, unit sink flow, and conservation at
every internal node.  Conversely, summing flow conservation over the
prefix \(\{0,\ldots,i-1\}\) shows that every cut load \(c_i\) of a unit
flow equals one.  Hence the two polytopes coincide.

The directed graph is acyclic, and the standard network-flow matrix is
totally unimodular.  Therefore every vertex of its unit-flow polytope is
integral.  Equivalently, an integral unit flow is a single directed path,
whose successive arcs partition the path edges. \(\square\)

### Scope of Theorem 2.1

Removing forbidden atoms from the catalogue merely deletes arcs and
preserves integrality.  Thus the theorem applies after any **fixed unary
filter** (for example a separately fixed owner mask).  It does not say
that adding simultaneous conflict, decoration, or route variables
preserves total unimodularity.  In particular, imposing a collision
independent-set system jointly with (2.2) needs a separate proof; one may
not infer it from either system being integral alone.

## 3. The smallest branching obstruction

Let \(A=K_{1,3}\) have centre \(o\), leaves \(1,2,3\), and edges
\(e_1,e_2,e_3\).  Admit precisely the three connected induced supports

\[
 Q_{12}=A[\{o,1,2\}],\quad
 Q_{13}=A[\{o,1,3\}],\quad
 Q_{23}=A[\{o,2,3\}].                                \tag{3.1}
\]

Their edge-versus-atom matrix is

\[
 M=\begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det M=-2.                                   \tag{3.2}
\]

The exact-cover equations have the unique solution

\[
                x_{12}=x_{13}=x_{23}=\tfrac12.        \tag{3.3}
\]

Hence the native connected-subtree exact-cover relaxation is not integral
on a branching component tree, even when every candidate has ECO-allowed
arity three.

This is smallest in both row order and underlying-tree size.  A square
zero-one matrix of order at most two has determinant in
\(\{-1,0,1\}\), so determinant magnitude two needs at least three rows
and columns.  Every tree with fewer than three edges is a path.  Among
three-edge trees, the path is covered by Theorem 2.1, while the only
branching tree is \(K_{1,3}\), on which (3.2) occurs.

The example is an abstract catalogue obstruction.  It does **not** assert
that one physical ECO factor realizes all three displayed atoms with a
common decoration and common product cube.

## 4. Exact usefulness and non-WLOG boundary

The path theorem yields a useful sufficient selection mechanism after the
correct upstream preparation:

1. repair/rethread the carrier so the required global palettes exist;
2. fix a component order \(v_0,\ldots,v_N\);
3. retain only component-faithful ECO atoms whose supports are intervals
   and which satisfy the already fixed unary owner/physical guards;
4. solve the unit-flow problem (2.2);
5. certify the remaining global product-cube and private/laminar route
   rows for the selected path.

It is not a WLOG reduction.  The incidence hypertree with component set
\(\{o,1,2,3\}\) and three binary atoms supported on
\(\{o,i\}\), \(i=1,2,3\), has a unique ordinary-tree expansion, namely
the three-edge star.  No component ordering turns all three supports into
an edge partition of a path.

Finally, the fixed-rotation ECO owner-collision graph proved elsewhere to
be a path forest is a graph on **atom labels/collisions**, whereas \(A\)
here is a tree on **factor components**.  There is no canonical
identification between them.  Its independent-set theorem clears local
collisions but does not supply the component path required by Theorem 2.1.
The raw \(m=5\) palette obstruction likewise occurs before this tiling
problem and cannot be repaired by path integrality.  The live order is
therefore

\[
 \text{controlled repair/rethread}
 \longrightarrow\text{ collision-free ECO selection}
 \longrightarrow\text{ owner-aligned residual Hall}
 \longrightarrow\text{ private/laminar occurrence routing},
\]

with the path-flow theorem available only as a sufficient topological
selector inside the second step.
