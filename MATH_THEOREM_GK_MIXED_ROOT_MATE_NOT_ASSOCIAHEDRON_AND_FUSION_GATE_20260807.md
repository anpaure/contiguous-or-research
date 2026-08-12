# The mixed GK root-mate graph is not the associahedron, and its reverse arcs are not free fusions

**Date:** 2026-08-07  
**Status:** unconditional refutation and exact resource audit.  This note
rules out importing Lucas's Hamilton cycle theorem directly.  It does not
rule out a separate Hamiltonicity theorem for the mixed root-mate graph.

## 1. The mixed root-mate digraph

Let `U` be a Dyck word of semilength `m`, and fix the distinguished first
upstep `u=1`.  Let the first top-level primitive component of `U` have
semilength `n_1`, and let `y` be its closing downstep.

The full GK hinge characterization gives two kinds of root-mate arcs.

* **Depth-two arcs.**  Let `b` open a child subtree of the root of the
  first primitive component, and let `x` be any downstep in that subtree.
  Then
  \[
       V=U-b+x
  \]
  is Dyck and the hinge has
  \[
       B_{x,U}=X_V.
  \]

* **Height-one arcs.**  Let `b` open a later top-level primitive
  component, and let `x` be any downstep in that component.  Then
  \[
       V=U-b+y
  \]
  is Dyck and the hinge has
  \[
       B_{y,U}=X_V.
  \]
  The root mate is independent of `x`, so these are parallel labelled
  arcs when the later component has size greater than one.

Call the resulting directed labelled multigraph `G_m^*`.

There are exactly `n_1-1` depth-two arcs and `m-n_1` height-one arcs out
of `U`, counted with their hinge labels.  Thus

\[
                    d^+_{G_m^*}(U)=m-1.                 \tag{1.1}
\]

This numerical agreement with the degree of the binary-tree rotation
graph is not a graph identification.

## 2. Its simple projection is the depth-two flip graph

Let `H_m` be the undirected simple graph obtained from all depth-two arcs.
Every height-one simple edge is already an edge of `H_m` in the opposite
direction.  Indeed, changing the first closing downstep `y` to an upstep
and the later opener `b` to a downstep makes `y` a depth-two opener in the
new word, with `b` a downstep in its excursion.  The reverse depth-two
flip recovers `U`.

Consequently the simple projection of `G_m^*` is exactly `H_m`; the extra
height-one labels add orientations and parallel arcs, not new simple
edges.

The number of depth-two choices at `U` is `n_1-1`.  Since the number of
Dyck words whose first primitive component has semilength `i` is

\[
                  \operatorname {Cat}_{i-1}
                  \operatorname {Cat}_{m-i},
\]

symmetry of the Catalan convolution gives

\[
 |E(H_m)|
 =\sum_{i=1}^m(i-1)\operatorname {Cat}_{i-1}
                         \operatorname {Cat}_{m-i}
 ={m-1\over2}\operatorname {Cat}_m.                  \tag{2.1}
\]

No depth-two arc is the reverse of another depth-two arc: after the flip,
the old `b` closes the first primitive component.  Hence (2.1) counts
simple undirected edges.

Again, (2.1) equals the edge count of the associahedron, but equality of
the two scalar ledgers is not equality of graphs.

## 3. Exact semilength-four refutation

At `m=4`, list the fourteen Dyck words as follows:

\[
\begin{array}{c|c@{\qquad}c|c}
0&11110000&7&11001100\\
1&11101000&8&11001010\\
2&11100100&9&10111000\\
3&11100010&10&10110100\\
4&11011000&11&10110010\\
5&11010100&12&10101100\\
6&11010010&13&10101010
\end{array}
\]

Directly applying the depth-two flip definition gives the neighbour
table

\[
\begin{array}{c|c@{\qquad}c|c}
0&9,10,11&7&4,5,12\\
1&9,12,13&8&4,6,13\\
2&3,10,12&9&0,1,4\\
3&2,11,13&10&0,2,5\\
4&7,8,9&11&0,3,6\\
5&6,7,10&12&1,2,7\\
6&5,8,11&13&1,3,8.
\end{array}                                             \tag{3.1}
\]

Any two vertices in (3.1) have at most one common neighbour.  Therefore
`H_4` has no four-cycle.

The three-dimensional associahedron does have a four-cycle, coming from
two commuting rotations.  In the standard Dyck encoding one explicit
square is

\[
 11110000-10111000-10110100-11101000-11110000.          \tag{3.2}
\]

Each edge in (3.2) is the usual Tamari move that exchanges a downstep with
the smallest following Dyck factor.

Thus

\[
                 \boxed{H_4\not\cong \operatorname {Assoc}_4}. \tag{3.3}
\]

In particular, `G_m^*` is not the Lucas binary-tree rotation graph, and
Lucas's Hamilton cycle cannot be imported edge-for-edge.

## 4. The directed obstruction is stronger

For a depth-two arc `U -> V`, the two words differ by changing a `1` at
position `b` and a later `0` at position `x` into `0,1`.  If `inv` counts
`1`-before-`0` pairs, then

\[
                    \operatorname {inv}(V)
                    =\operatorname {inv}(U)-(x-b).      \tag{4.1}
\]

Hence the depth-two orientation is acyclic.  Every directed cycle in
`G_m^*` must use height-one arcs.  An undirected Hamilton cycle in `H_m`,
even if one exists, therefore does not automatically orient to a usable
root-mate cycle.

## 5. Exact resource audit

For a depth-two arc, put

\[
 a=U-\{1,b\},\qquad B_x=a+x=X_V,\qquad B_y=a+y.
\]

The fixed SCD edge

\[
                  B_x t(B_x)=X_Vt(X_V)                 \tag{5.1}
\]

is literally the root edge at `V`.  Thus a depth-two overlap cancels a
whole fixed edge and is a legitimate zero-degree-cost fusion socket.

For a height-one arc the equality is instead

\[
                         B_y=X_V.                       \tag{5.2}
\]

But `B_yQ_y(U)` is the prospective second-matching edge of the hinge, not
the fixed SCD edge at `B_y`; in general

\[
                         Q_y(U)\ne t(B_y).              \tag{5.3}
\]

For example, at `m=3` take `U=101100`, `b=3`, `y=2` and `x=5`.
Then `a={4}`, so `B_y={2,4}` and `Q_y(U)={2,3,4}`, whereas the
rightmost-unmatched-zero rule gives `t(B_y)={2,4,6}`.

Therefore (5.2) identifies only one rank-`(m-1)` vertex.  If the next root
hinge is inserted naively, that shared vertex has physical degree three.
Unlike (5.1), it does not give an automatic symmetric-difference fusion.
A separate rethread/cut packet is required for every use of the reverse
orientation.

Finally, the remaining labels are not automatically rainbow.  For fixed
`(U,b)`, varying `x` leaves both

\[
                         a=U-\{1,b\},\qquad B_y=a+y
\]

unchanged.  Across different roots these resources may collide as well.
Thus any usable global selector must simultaneously control

1. the directed root chronology;
2. the `a` colours;
3. the unused `B_x/B_y` physical vertices; and
4. the reverse-arc rethread cost in (5.3).

## 6. Consequence

The associahedron shortcut is closed negatively.  The remaining graph
problem is intrinsic to the GK hinge system:

> construct a directed root path/cycle cover in `G_m^*` together with a
> rainbow choice of the `a` and unused endpoint resources, and replace
> every height-one vertex-only overlap by a certified degree-two
> rethread.

The earlier double-Hall/path-contraction route remains relevant, as does a
direct Hamiltonicity study of `H_m`; neither is supplied by Lucas's theorem.
