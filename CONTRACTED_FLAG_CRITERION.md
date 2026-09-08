# Contracting two one-sided forests: the exact flag-alignment criterion

This note gives the exact reduction requested by the middle-four-level
route.  It applies to any two spanning linear forests on consecutive Boolean
layers, and then specializes it to the lexical forests of
Gregor--Jäger--Mütze--Sawada--Wille (GJM).

The principal conclusion is that a perfect containment matching is not by
itself enough.  What is needed is a containment-preserving **near-isomorphism
of path forests**.  For fixed cuts this has an ordinary Hall criterion on
path fragments.  With `q` cuts it leaves exactly `D+q` connector slots, of
which `q` must repair lost colours and `D` are true Catalan/component slack.

## 1. Abstract setup

Let

\[
 \mathcal A=\binom{[2r+1]}r,
 \qquad
 \mathcal B=\binom{[2r+1]}{r+1},
 \qquad |mathcal A|=|mathcal B|=W.                     \tag{1.1}
\]

Let `F_-` be a spanning linear forest on `mathcal A`, and `F_+` a spanning
linear forest on `mathcal B`.  Assume both have

\[
                         W-D                              \tag{1.2}
\]

edges, hence `D` path components, with isolated vertices counted as paths.
In the intended application, the edges of `F_-` have distinct lower colours
and the edges of `F_+` have distinct upper colours.

A **flag matching** is a bijection

\[
 \phi:\mathcal A\longrightarrow\mathcal B,
 \qquad X\subset\phi(X).                                \tag{1.3}
\]

Pull `F_+` back to `mathcal A` through `phi`, and define the common-edge
forest

\[
 C_\phi=F_-\cap\phi^{-1}(F_+).                           \tag{1.4}
\]

Write

\[
 t_\phi=|E(C_\phi)|,
 \qquad
 q_\phi=(W-D)-t_\phi.                                   \tag{1.5}
\]

Thus `q_phi` is the number of edges lost from **each** one-sided forest when
we retain only simultaneous transitions.

## 2. Exact cut-and-Hall theorem

### Theorem 1 (contracted-flag equivalence)

For an integer `q>=0`, the following are equivalent.

1. There is a flag matching `phi` with `q_phi<=q`.
2. One can delete at most `q` edges from each of `F_-` and `F_+` so that the
   resulting spanning path forests admit a graph isomorphism `phi` satisfying
   `X subset phi(X)` at every vertex.
3. One can cut the paths of both forests into path fragments, using at most
   `q` cuts on each side, and biject the fragments so that paired fragments
   have the same number of vertices and, in one of the two orientations,

   \[
                   X_i\subset Y_i\quad\hbox{for every }i. \tag{2.1}
   \]

#### Proof

Given `phi`, retain exactly the common edges (1.4).  The retained graph is a
spanning subforest of `F_-`, and its image is a spanning subforest of `F_+`.
Exactly `q_phi` edges were deleted from either forest, and `phi` is an
isomorphism between the retained graphs.  This proves `1=>2`.

Every component of a spanning subforest of a path forest is a path fragment.
An isomorphism between two paths is either order-preserving or order-
reversing, giving (2.1), so `2=>3`.

Conversely, concatenate the vertexwise containments on the paired fragments
to obtain a bijection `phi` from `mathcal A` to `mathcal B`.  It is a flag
matching, and every retained fragment edge is common.  Thus at most the cut
edges fail to be common, proving `3=>1`.  QED.

### Corollary 2 (ordinary Hall criterion after the cuts are fixed)

Fix the cut locations.  For every fragment size `s`, form a bipartite graph
whose left vertices are the `s`-vertex fragments of `F_-`, whose right
vertices are the `s`-vertex fragments of `F_+`, and where two fragments are
adjacent when (2.1) holds in at least one orientation.

The fixed cuts admit a flag alignment if and only if every one of these
bipartite graphs has a perfect matching, equivalently if and only if it
satisfies Hall's inequalities.

In particular, with `q=0`, full contraction is possible exactly when the
original path components can be perfectly matched, length by length, by
coordinatewise containment.

The optimization over cut locations is not an ordinary vertex matching.  It
is a path-segment packing problem: possible matched fragments are diagonal
runs in the grids `P times Q` of pairs `(X,Y)` satisfying `X subset Y`, and
the selected runs must partition every vertex of both forests.  Theorem 1 is
an exact finite formulation of that problem.

## 3. Exact repair ledger

The common forest `C_phi` has

\[
             W-t_\phi=D+q_\phi                          \tag{3.1}
\]

components.  A cyclic common order containing all its edges therefore needs
exactly `D+q_phi` connector transitions.

There are `q_phi` lower-colour edges of `F_-` and `q_phi` upper-colour edges
of `F_+` not retained in `C_phi`.  A new simultaneous flag transition

\[
                  (X\subset\phi(X))longrightarrow
                  (X'\subset\phi(X'))                   \tag{3.2}
\]

is legal at the first-shadow level when

\[
 XX'\in J(2r+1,r),qquad
 \phi(X)\phi(X')\in J(2r+1,r+1).                        \tag{3.3}
\]

It carries one lower and one upper colour.

### Theorem 3 (coloured endpoint completion)

For a fixed flag matching `phi`, there is a cyclic common Johnson order that
contains `C_phi` and repairs every lost colour if and only if one can choose
`D+q_phi` transitions (3.2)--(3.3) between fragment endpoints such that:

1. after every fragment is contracted, the chosen transitions form one
   cycle through the `D+q_phi` fragments, with a consistent orientation of
   each fragment;
2. their lower colours contain all `q_phi` lower colours lost from `F_-`;
3. their upper colours contain all `q_phi` upper colours lost from `F_+`.

#### Proof

Cut a desired cyclic order at the edges not belonging to `C_phi`.  What
remains is exactly the set of oriented common fragments, and the cut edges
give the stated transitions and colour coverage.  Conversely, concatenate
the oriented fragments using the selected transitions.  Conditions 1--3
give a cyclic common Johnson order containing the common forest and every
lost first-shadow colour.  QED.

The count is sharp:

\[
 \underbrace{D+q_\phi}_{\text{connector slots}}
 =\underbrace{q_\phi}_{\text{mandatory colour repairs}}
  +\underbrace{D}_{\text{component/Catalan slack}}.      \tag{3.4}
\]

Thus `q_phi=O(D)` is exactly the regime in which the two lexical forests
would give an `O(Cat_r)`-repair construction.  Ordinary Hall handles only
the fragment pairing in Corollary 2; Theorem 3 is the additional coloured
endpoint gate.

A move-to-front realization is stronger still.  Condition (3.3) gives two
simultaneous Johnson flags, but it does not by itself choose compatible
ordered-partition states.  Any MTF claim needs that extra state-transition
certificate and cannot be inferred merely by contracting the flags.

## 4. The exact near-isomorphism threshold

Theorem 1 gives an immediate necessary overlap bound.  If only `O(D)` repairs
are allowed, then

\[
 t_\phi=(W-D)-O(D)=W-O(D).                               \tag{4.1}
\]

In words:

> A successful containment matching must identify the two one-sided forests
> on all but `O(D)` of their edges.

This is much stronger than an arbitrary perfect containment matching.  It is
a constrained near-isomorphism between two exponentially large labelled path
forests.

Equivalently, define the compatibility graph of oriented path fragments.
The required theorem is not just expansion of the rank-`r`/rank-`r+1`
incidence graph; it is a Hall theorem for a near-spanning collection of long
diagonal fragment alignments.

## 5. Specialization to the GJM lexical forests

For the GJM four-level factor, let `f` be reverse-complementation.  The paper
constructs the lower outer paths as `f(mathcal P)` from the upper outer paths
`mathcal P`.  After suppressing the outer vertices, this gives an exact graph
isomorphism

\[
                         F_-=f(F_+).                     \tag{5.1}
\]

At first sight, (5.1) appears to solve the alignment problem.  The canonical
vertex map is not a containment flag.

### Proposition 4 (canonical-alignment obstruction)

Among all `W=binom(2r+1,r)` vertices `X in mathcal A`, exactly `2^r` satisfy

\[
                         X\subset f(X).                  \tag{5.2}
\]

Consequently the canonical isomorphism (5.1) violates containment on a
`1-o(1)` fraction of the vertices.

#### Proof

Pair coordinate `i` with coordinate `2r+2-i`; the middle coordinate is
`r+1`.  In bit notation, (5.2) says

\[
 x_i=1\Longrightarrow x_{2r+2-i}=0.                     \tag{5.3}
\]

It also forces the middle bit to be zero.  There are `r` mirrored coordinate
pairs.  Since `X` has size `r`, (5.3) forces it to choose exactly one member
of every pair and not the middle coordinate.  There are exactly `2^r` such
choices.  QED.

This does not rule out a different component permutation.  It converts full
overlap into a precise Hall problem.  Since `F_+=f(F_-)`, every full-overlap
flag matching has the form

\[
                         \phi=f\circ\alpha,              \tag{5.4}
\]

where `alpha` is a graph automorphism from `F_-` to itself.  Such an
automorphism permutes path components of equal length and independently
reverses them.  Therefore full overlap exists if and only if, for every path
length, the two copies of the component family have a perfect matching in
which a source path `X_0,...,X_s` may be matched to a target path
`Y_0,...,Y_s` precisely when, in one orientation,

\[
                         X_i\subset f(Y_i)
                     \quad(0\le i\le s).                 \tag{5.5}
\]

This is the exact Hall test that the published lexical construction does not
prove.

For `q>0`, paths may first be cut into fragments and the same Hall test is
applied to those fragments.  The least number of cuts for which all these
tests pass is exactly

\[
                         \min_\phi q_\phi.                \tag{5.6}
\]

No general `O(Cat_r)` bound on (5.6) follows from the GJM paper.

## 6. Relation to the lexical colour collisions

There are two different uses of a contraction, and they must not be
confused.

If one discards the upper flags and tries to use `F_-` itself as a rank-`r`
Johnson skeleton, its upper colours are the ordinary unions of the endpoints
of its edges.  `GJM_FOUR_LEVEL_AUDIT.md` proves the symbolic collision bound

\[
 \delta_r\ge\operatorname {Cat}_{r-1}.                  \tag{6.1}
\]

Thus at least `Cat_(r-1)` lower-forest edges must be cut before its retained
ordinary union colours can all be distinct.

This does **not** by itself lower-bound `q_phi` in the two-flag formulation.
On a common flag transition, the upper colour is the union of
`phi(X),phi(X')`, inherited from `F_+`, rather than necessarily the union of
`X,X'`.  Since `F_+` is upper-colour-rainbow, a successful flag alignment can
avoid the collision obstruction by retaining the upper flag data.  Dropping
those flags brings the obstruction back.

This is still `O(Cat_r)`, but it rules out the zero-repair dream and shows
that the simpler **unflagged** endpoint-completion route needs a positive
Catalan-scale repair.  The flagged Hall problem (5.6) has a different, as yet
unproved, repair threshold.

## 7. Resulting all-dimensional target

The four-level route is now reduced to the following theorem.

> **Lexical fragment-alignment theorem.**  Cut `O(Cat_r)` edges from each of
> the two GJM outer path forests so that their fragments satisfy the Hall
> condition of Corollary 2 under containment, and so that the coloured
> endpoint graph in Theorem 3 has a spanning rainbow cycle.

This theorem would yield a common two-sided central skeleton with only
`O(Cat_r)=o(W)` repairs.  It is not proved by the existing lexical-matching
analysis.  The canonical reverse-complement alignment fails on almost every
vertex.  If one tries to avoid the flag alignment and use only the lower
forest, at least `Cat_(r-1)` cuts are separately forced by explicit colour
collisions.  These are the two distinct obstacles a successful component
permutation or absorber must address.
