# Cool-lex gives a subcubic spanning tree of every hook angle graph

**Date:** 2026-08-05  
**Method:** first-`10` bubble recursion and the marked promoted-parent map;
no search  
**Status:** unconditional.  Every cyclic weak-composition transfer graph
`G_(q,b)` has an explicit spanning tree of maximum degree three, and every
tree edge has the literal binary parent-port rule `01/10 -> 000`.  The
remaining topology gate is to compare the plane-tree contour order with the
directed PBBS order of those marked parent ports after lower levels are
spliced.

## 1. Binary encoding of hook angles

Encode a cyclic weak composition

\[
 x=(x_0,\ldots,x_{q-1}),\qquad |x|=b,
\]

by the binary necklace

\[
                         0,1^{x_0}0,1^{x_1}\cdots0,1^{x_{q-1}}.
\tag{1.1}

This is a bijection between `N_(q,b)` and binary necklaces with `q` zeros
and `b` ones.  Moving one chip from a vacancy bank to the next changes one
cyclic factor

\[
                         10\longleftrightarrow01.
\tag{1.2}

Hence the hook angle graph `G_(q,b)` is exactly the graph of fixed-content
binary necklaces under cyclically adjacent `01/10` swaps.

## 2. The necklace bubble recursion

Use the lexicographically least representative of each binary necklace.
Fixed-content necklace representatives form a first-`10` bubble language.
The standard recursion has nodes

\[
                         w=0^s1^t\gamma.
\tag{2.1}

For the oracle value `j=j(w)`, the roots of its recursive child subtrees
are

\[
 w_i=0^{s-1}1^{t-i}0,1^i\gamma,
 \qquad i=t-1,t-2,\ldots,j.
\tag{2.2}

The recursive calls are disjoint and, together with `w`, partition all
necklaces in the subtree rooted at `w`.  The initial root is `0^q1^b`.

For convenience set `w_t=w`.  Consecutive roots satisfy

\[
                         w_i\longleftrightarrow w_{i-1}
\tag{2.3}

by one adjacent swap: with

\[
 P=0^{s-1}1^{t-i},\qquad R=1^{i-1}\gamma,
\]

the two strings are

\[
                         P01R,qquad P10R.
\tag{2.4}

Thus every edge in (2.3) is a literal hook chip-transfer edge.

## 3. Sibling-path replacement

Construct a graph `T(w)` recursively.  At node `w`, replace the star from
`w` to its child roots by the path

\[
                         w_t-w_{t-1}-\cdots-w_j,
\tag{3.1}

and inside every child subtree use the same construction.

### Theorem 3.1

For the initial root `0^q1^b`, `T=T(0^q1^b)` is a spanning tree of
`G_(q,b)` and

\[
                         \Delta(T)\le3.
\tag{3.2}

#### Proof

Induct on the recursion tree.  Contract every already-constructed child
tree to its root.  Equation (3.1) is a path through the parent and every
contracted child root, so adjoining the child trees gives a connected
acyclic graph.  The recursion subtrees partition the necklace set, hence
the graph is spanning.  Every edge is legal by (2.4).

A vertex has degree at most two in the sibling path belonging to its
parent recursion call.  In its own recursion call it is incident only with
the first edge leading into its child-root path.  Therefore its total degree
is at most three.  `square`

This is stronger than mere connectedness of the hook angle graph and does
not invoke the non-adjacent transpositions in the published cool-lex output
Gray code.  Only the elementary recursion tree and its consecutive sibling
roots are used.

## 4. Exact promoted parent of a cool-lex tree edge

For the adjacent pair in (2.4), remove the moving `1`.  The common lower
word is `P0R`.  Promoting the hook parent inserts two consecutive empty
vacancy slots at that cut.  In binary encoding this gives

\[
                         \boxed{P01R,\ P10R\quad\longmapsto\quad P000R.}
\tag{4.1}

The inserted pair is marked inside the displayed `000`.  Deleting the mark
recovers `P0R` and the cut, so different rooted tree edges use different
marked parent ports even when their unmarked promoted necklaces agree.

Equation (4.1) is exactly the binary form of

\[
 \{[y+e_j],[y+e_{j+1}],[\iota_j(y)]\}.
\tag{4.2}

Consequently every edge of the subcubic tree has a literal selected,
common-pivot, q2-neutral PBBS leaf-plucking C6.

## 5. Plane order and the exact remaining gate

The recursion gives `T` a canonical plane embedding: use the linear sibling
order (3.1) and recurse in that same order.  Let `alpha,beta` be the edge
rotation permutations on the two bipartition shores.  Since `T` is a plane
tree,

\[
                         \pi=\beta\alpha
\tag{5.1}

is one edge-contour cycle.

The marked parent ports in (4.1) lie on hook components one chip level
lower.  After those lower components have been joined into a spine, let
`gamma` be their actual directed cyclic order on that spine.  The standard
three-shore cut calculation makes the final component permutation a product
of `gamma,alpha,beta`, with the order fixed by the literal C6 orientation.

Thus the all-angle hook packing is reduced to the following exact
**cool-lex contour compatibility** statement:

> Choose the recursion-plane orientations and the literal rooted lift of
> every edge so that the inherited directed marked-port order `gamma`
> composes with `alpha,beta` into at most `O(1)` cycles, while the constant
> q2 halos remain disjoint.

Theorem 3.1 makes the child-side incidence degree at most three.  The
marked inverse makes every parent occurrence distinct.  Neither fact alone
proves the order identity: reflection of a rooted port also reverses its
two child shores, so port signs and C6 orientations must be audited jointly.

## 6. Scope

Proved here:

1. an explicit spanning adjacent-transfer tree for every hook angle level;
2. maximum child-tree degree three;
3. the exact promoted binary parent-port rule `01/10 -> 000`;
4. distinct marked parent ports for distinct rooted tree edges.

Not proved here:

1. cool-lex contour compatibility with the already assembled parent spine;
2. global halo separation;
3. integration with the rigid/named one-or-two-rail block;
4. non-hook angle sectors or any post-q2 gate.
