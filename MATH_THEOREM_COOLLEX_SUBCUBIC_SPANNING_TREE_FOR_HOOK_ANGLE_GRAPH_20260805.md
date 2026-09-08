# The cool-lex recursion gives a subcubic spanning tree of every hook-angle graph

**Date:** 2026-08-05  
**Method:** first-10 bubble recursion and adjacent-swap algebra; no search  
**Status:** unconditional, using the published Sawada--Williams theorem that
fixed-density binary necklaces form a first-10 bubble language and that the
stated recursion visits every necklace exactly once.  The theorem constructs
a plane spanning tree; it does not prove compatibility of its contour with
the promoted PBBS parent-port orders.

**External source used:** J. Sawada and A. Williams, *A Gray Code for
Fixed-Density Necklaces and Lyndon Words in Constant Amortized Time*,
recurrence `C(s,t,gamma)` and Theorem 2,
https://www.socs.uoguelph.ca/~sawada/papers/bubble4.pdf .

## 1. Binary form of the hook-angle graph

Fix `q>=1` and `b>=1`.  A cyclic weak composition

\[
                         x=(x_0,\ldots,x_{q-1}),
                         \qquad \sum_i x_i=b,
\]

is represented by the binary necklace

\[
                         0,1^{x_0}0,1^{x_1}\cdots0,1^{x_{q-1}}.
\tag{1.1}
\]

This is a bijection between cyclic weak compositions of mass `b` in `q`
slots and binary necklaces with `q` zeros and `b` ones.  Moving one chip
between adjacent slots changes

\[
                    1^{a+1}0,1^c
                    \longleftrightarrow
                    1^a0,1^{c+1},
\tag{1.2}
\]

which is exactly one adjacent interchange `10<->01` in the binary word.
Thus the PBBS hook-angle graph `G_(q,b)` is the adjacent-interchange graph
on these fixed-density necklaces.

## 2. The first-10 recursion

Write a canonical necklace representative at one recursive node as

\[
                         r=0^s1^t\gamma,
                         \qquad s>0.
\tag{2.1}
\]

The first-10 bubble recurrence has a terminal index `j` determined by its
necklace oracle and recursive children whose output roots are

\[
 r_i=0^{s-1}1^{t-i}0,1^i\gamma,
                  \qquad j\le i\le t-1.
\tag{2.2}
\]

The children occur in the order

\[
                         r_{t-1},r_{t-2},\ldots,r_j.
\tag{2.3}
\]

Sawada--Williams prove that, after the necklace oracle suppresses invalid
calls, this recursion outputs every fixed-density necklace once and only
once.

## 3. A path through every sibling family

Join the node root and its child roots by

\[
             r-r_{t-1}-r_{t-2}-\cdots-r_j.
\tag{3.1}
\]

Every displayed edge is an edge of `G_(q,b)`.

For the first edge, the only change is

\[
 0^s1^t\gamma
 =0^{s-1}\,01\,1^{t-1}\gamma
 \longleftrightarrow
 0^{s-1}\,10\,1^{t-1}\gamma=r_{t-1}.
\tag{3.2}
\]

For consecutive children,

\[
\begin{aligned}
 r_i&=0^{s-1}1^{t-i}\,01\,1^{i-1}\gamma,\\
 r_{i-1}&=0^{s-1}1^{t-i}\,10\,1^{i-1}\gamma,
\end{aligned}
\tag{3.3}
\]

again one adjacent interchange.

## 4. Recursive assembly

### Theorem 4.1 (cool-lex subcubic tree)

For every `q,b`, the graph `G_(q,b)` contains a spanning tree `T_(q,b)`
of maximum degree at most three.  It comes with a canonical plane order.

#### Proof

For every node of the recursion tree, insert the sibling-root path (3.1),
and recursively insert the corresponding construction inside each child
call.

The node sets of distinct recursive child calls are disjoint, and together
with the current root they partition the node set below the current call.
The path (3.1) joins the roots of all those child trees to the current root.
Consequently the union is connected and has

\[
 \sum_i(|V_i|-1)+\#\{i\}
 =\sum_i|V_i|
\]

vertices minus one edges.  It is therefore a tree.  At the top call it
spans every necklace by the published recursion theorem.

A node root has at most two incident edges in the sibling-root path of its
parent call, and at most one edge to the first child root of its own call.
Thus its degree is at most three.  The child order (2.3), recursively,
defines a plane rotation system.  `square`

### Corollary 4.2 (bounded child-side packet load)

Under the PBBS leaf-plucking lift, no hook torus is a child shore of more
than three tree connectors.  Hence all child-side six-owner and companion
halo conflicts have bounded combinatorial degree.  The possible unbounded
load remains only on promoted parent components, where the marked-`00`
port theorem supplies distinct occurrence coordinates.

This corollary is a capacity reduction, not a simultaneous packing proof.

## 5. The remaining order equation

Let `alpha,beta` be the two shore rotations of the plane tree `T_(q,b)`.
Its contour permutation

\[
                         \pi=\beta\alpha
\tag{5.1}
\]

is one cycle.  The PBBS tree-contour reconnection theorem would collapse
the entire hook row to at most two cycles if the marked promoted-parent
cuts could be arranged in cyclic order

\[
                         \gamma=\pi,
\tag{5.2}
\]

because the return permutation would be `pi^2`.

The cool-lex tree proves the child-tree half of this statement with maximum
degree three.  It does **not** prove (5.2): distinct marked parent ports may
belong to several promoted tori, and marked-port injectivity does not
permit their cyclic orders to be assigned arbitrarily.

Thus the exact remaining general-hook topology is now:

> Compare the recursive contour word of `T_(q,b)` with the inherited
> cyclic orders of the marked double-zero ports `iota_j(y)`; either prove
> they agree after coherent reflection choices, or bound the cycle count of
> `gamma beta alpha` uniformly.

## 6. Scope

Proved:

1. an explicit adjacent-transfer spanning tree for every hook-angle row;
2. maximum child degree three;
3. a canonical plane contour to test against parent-port order.

Not proved:

1. the promoted-port contour equation;
2. global q2-halo separation on repeated parent components;
3. non-hook angle packing or any post-q2 compiler gate;
4. `nu(k)<=B(k)+O(1)`.
