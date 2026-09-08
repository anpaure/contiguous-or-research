# The Greene--Kleitman two-sided rainbow forest

This note gives a fully general central-layer object for every even dimension.
It is a theorem, not a computational observation.  Its components need not be
paths; that remaining distinction is stated explicitly at the end.

Let the ground set have size `2m`, and put

\[
W=\binom{2m}{m},\qquad
C=\binom{2m}{m-1},\qquad
\operatorname{Cat}_m=W-C=\frac{W}{m+1}.
\]

## 1. From an SCD to a two-sided colored graph

Fix any saturated symmetric-chain decomposition `D` of the Boolean lattice.
For every `(m-1)`-set `S`, its chain contains the consecutive segment

\[
S\subset T\subset U,
\qquad |T|=m,quad |U|=m+1.
\]

There are exactly two `m`-sets strictly between `S` and `U`.  Let `T'` be the
one different from `T`.  Put an edge

\[
e_S=TT'
\]

in the Johnson graph `J(2m,m)`.

### Lemma 1 (two simultaneous rainbow colourings)

As `S` ranges over the entire `(m-1)`st layer:

1. the intersections of the edges `e_S` are precisely all `(m-1)`-sets,
   each once;
2. the unions of the edges `e_S` are precisely all `(m+1)`-sets, each once.

#### Proof

By construction,

\[
T\cap T'=S,
\qquad T\cup T'=U.
\]

The lower colours are distinct because the edges are indexed by `S`.
Every chain that meets rank `m-1` also meets rank `m+1`, and contains exactly
one set in each of those ranks.  Since the SCD partitions both layers, sending
`S` to the member `U` two ranks above it in the same chain is a bijection.
Thus the upper colours are also all distinct and complete.  QED.

Consequently the graph has exactly

\[
C=W-\operatorname{Cat}_m
\]

edges and is simultaneously rainbow in the lower and upper edge colours.

## 2. Acyclicity for the Greene--Kleitman SCD

Now use the standard Greene--Kleitman SCD.  A chain template has a fixed-one
set `B` and star coordinates

\[
e_1<e_2<\cdots<e_h,
\]

and its members are obtained by adjoining the stars from left to right.

Every chain that meets rank `m-1` has, for a suitable `q`,

\[
\begin{aligned}
S&=B\cup\{e_1,\ldots,e_{q-1}\},\\
T&=S\cup\{e_q\},\\
U&=T\cup\{e_{q+1}\},\\
T'&=S\cup\{e_{q+1}\}.
\end{aligned}
\]

Orient `e_S` from `T` to `T'`.

### Theorem 2 (two-sided rainbow forest)

The oriented graph above is acyclic.  Its underlying graph is a spanning
forest on the middle layer with exactly `Cat_m` components.  Every non-root
middle set has outdegree one, and the roots are precisely the middle sets
whose Greene--Kleitman chains are singletons.

#### Proof

Use the potential

\[
\Phi(X)=\sum_{x\in X}x.
\]

Along the oriented edge `T -> T'`, the coordinate `e_q` is replaced by the
strictly larger coordinate `e_(q+1)`.  Hence

\[
\Phi(T')-\Phi(T)=e_{q+1}-e_q>0.
\]

There can therefore be no directed cycle.  Each middle set whose SCD chain
also meets rank `m-1` is the unique `T` of that chain and has exactly one
outgoing edge.  A singleton middle chain does not meet rank `m-1` and has no
outgoing edge.  Following outgoing edges must terminate, by acyclicity, at
one of these roots.  Thus the underlying graph is a forest.

It has `W` vertices and `C` edges, so its number of components is

\[
W-C=\operatorname{Cat}_m.
\]

Equivalently, the number of singleton middle chains in any SCD is
`W-C=Cat_m`, confirming the root count.  QED.

## 3. Exact significance for universal OR arrays

A linear ordering of all `W` middle sets has `W-1` transitions.  The forest
uses

\[
W-\operatorname{Cat}_m
\]

transitions to cover every rank-`m-1` intersection and every rank-`m+1`
union exactly once.  It leaves exactly

\[
\operatorname{Cat}_m-1
\]

transitions for joining its components.  Those are precisely the generalized
bridges that must generate the more distant lower and upper shadows.

For `k=14`, this gives

\[
W=3432,
\quad C=3003,
\quad \operatorname{Cat}_7=429,
\]

so the central skeleton has 429 components and needs 428 bridges.  This is the
same slack found independently from the optimal-length interval count.

## 4. The exact remaining lemma

The theorem gives a forest, not necessarily a **linear** forest.  A component
may branch because several non-root vertices can point to the same parent.
A word that lists every middle set once cannot traverse a branching tree using
all its edges.

The next construction theorem should therefore prove one of the following.

1. There is an inclusion bijection from rank `m-1` to rank `m+1` whose induced
   two-sided rainbow graph is a linear forest with `Cat_m` components.
2. The Greene--Kleitman matching can be changed by colour-preserving
   alternating exchanges until every degree is at most two, without creating
   a cycle.
3. Branching edges can be represented in other derivative rows while the
   resulting extra component joins remain within the available rank slack.

After linearization, the `Cat_m-1` joins must be chosen recursively so their
consecutive intersections/unions cover the outer Boolean layers and so the
resulting central row is pinnable.  This is a global Catalan recursion target,
not a finite-mask repair problem.

## 5. Correction: the former `W/2` linear-subforest claim is retracted

The branching left open above can in fact be counted exactly.  If `a_j`
denotes the number of middle vertices of indegree `j`, then

\[
 a_j=\binom{2m-j-1}{m-j}\qquad(0\le j\le m).
\]

In particular,

\[
 \#\{\deg^-\ge1\}=W/2,
 \qquad
 \#\{\deg^-\ge2\}=\binom{2m-2}{m-2}\sim W/4.
\]

The next inference in the former version of this note was false.  A linear
subforest need not retain a vertex's outgoing edge; after deleting it, two
incoming edges may both be retained.  A star already refutes the assertion
that every vertex can retain at most one incoming edge.  Consequently the
former `W/2` edge bound and its exact deletion/path-count formulae are
withdrawn.

The indegree census above remains correct.  Exact tree dynamic programming
gives retained-edge values

    13, 44, 159, 588, 2188

for `m=3,...,7`, strictly larger than the obsolete
`10,35,126,462,1716`.  The two-state recurrence and deterministic replay are
in `MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`.
The plane-tree generating function and asymptotic analysis are now completed
in `MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md`:

\[
 {\Delta_m\over m\operatorname{Cat}_m}
 \longrightarrow0.356895867892\ldots .
\]

Thus the corrected edit barrier is still `Theta(W)`.
