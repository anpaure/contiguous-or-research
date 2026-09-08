# Rooted path-cover coefficient, ordered Hall, and the fixed-matching pull-parity boundary

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reduction and scoped no-go.  After one
perfect matching of a bipartite factor is fixed, the requirement that every
factor cycle meet the common-core hinge bank is equivalent to a rooted
spanning linear-path cover followed by one root-to-start matching.  It has
both a positive-coefficient matrix-tree formulation and an exact ordered
Hall formulation.  The natural integral system is an intersection of three
matroid independence systems, not the ordinary two-matroid intersection
suggested by the residual Ore theorem.  Fixed-matching `C_6` and `C_8`
switches obey a sharp parity law.  Finally, a common-core ring can never make
the entire residual successor host acyclic when `m >= 4`; hence topology
must be correlated with the selected second matching.  The theorem does not
prove that the required ordered Hall instance exists for the current
protected reservoir.

## 0. Fixed-matching setting

Let `G=(L,U;E)` be bipartite with

\[
                         |L|=|U|=N,
\]

and fix a perfect matching `M_0`.  Write `u_y` for the member of `U`
matched by `M_0` to `y in L`.  Delete the matching edges of `M_0`, together
with every occurrence-labelled edge forbidden by the protected phase, and
form the loopless successor digraph `Q` on `L`:

\[
                    x\longrightarrow y
       \quad\Longleftrightarrow\quad xu_y\in E-M_0.
\tag{0.1}
\]

A second perfect matching `M_1`, disjoint from `M_0`, is exactly a cycle
cover `pi` of `Q`, where

\[
                            \pi(x)=y
              \quad\Longleftrightarrow\quad xu_y\in M_1.
\tag{0.2}
\]

Let `R subseteq L` be the lower hinge-root set.  As in the rooted
fixed-matching theorem, the factor `M_0 union M_1` has forest complement
after deleting the hinge incidences precisely when every cycle of `pi`
meets `R`.

## 1. Exact rooted path-cover decomposition

For a directed edge set `F`, write `h(F)` for its set of heads.

### Theorem 1.1 (rooted linear-forest factorization)

The following objects are in bijection.

1. Cycle covers `pi` of `Q` for which every cycle meets `R`.
2. Pairs `(F,C)` with the following properties:
   * `F` contains exactly one outgoing arc from every vertex of `L-R` and
     no outgoing arc from a vertex of `R`;
   * the heads in `F` are all distinct;
   * `F` is acyclic;
   * if

     \[
                         S=L\setminus h(F),
     \tag{1.1}
     \]

     then `C` is a matching of the root tails `R` bijectively onto the head
     set `S`.

In every such pair, `F` is a spanning union of exactly `|R|` vertex-disjoint
directed paths, each ending at one member of `R`; the arcs of `C` close
those paths into cycles, every one of which contains a root.

#### Proof

Let `pi` be a cycle cover whose cycles all meet `R`, and delete from `pi`
the outgoing arc of every root.  Each old cycle is cut at all of its root
tails.  What remains is a collection of directed paths ending at roots.
It has one outgoing arc at every nonroot, no repeated head, and no directed
cycle.  Its unused heads are exactly

\[
                          S=\pi(R),
\]

and the deleted root arcs form a matching `C:R -> S`.

Conversely, an acyclic directed graph with indegree and outdegree at most
one is a disjoint union of directed paths.  In `F`, only roots can have
outdegree zero.  Since `F` has `N-|R|` edges, it has exactly `|R|`
components, so every component contains exactly one root and ends there.
The unused-head set `S` also has size `|R|`.  Adding the matching `C`
gives indegree and outdegree one at every vertex, hence a cycle cover.
Every resulting cycle uses at least one arc of `C`, whose tail is a root.
The two operations are inverse.  \(\square\)

This factorization separates the same-factor topology gate into a rooted
linear-path cover and a closure matching.  It is stronger than an ordinary
cycle-cover Hall condition and weaker than demanding one Hamilton cycle.

## 2. An exact ordered-Hall theorem

For a total order `prec` on `L`, a successor arc `x -> y` is called
**descending** when `y prec x`.

### Theorem 2.1 (ordered-Hall equivalence)

There is a cycle cover of `Q` every cycle of which meets `R` if and only if
there exist a set `S subseteq L` with `|S|=|R|` and a total order `prec` on
`L` such that both of the following bipartite graphs have perfect
matchings:

\[
 Q^{\rm cl}_{R,S}
   =\{x\to y\in E(Q):x\in R,\ y\in S\},
\tag{2.1}
\]

and

\[
 Q^-_{\prec,S}
   =\{x\to y\in E(Q):x\in L-R,\ y\in L-S,\ y\prec x\}.
\tag{2.2}
\]

Equivalently, after `S,prec` are fixed, the exact topology gate is the two
ordinary Hall systems

\[
 |N_Q(X)\cap S|\ge |X|
       \qquad(X\subseteq R),
\tag{2.3}
\]

and

\[
 |N^-_{\prec}(Y)\cap(L-S)|\ge |Y|
       \qquad(Y\subseteq L-R).
\tag{2.4}
\]

#### Proof

Given a rooted cycle cover, take `(F,C)` from Theorem 1.1 and put
`S=L-h(F)`.  The directed forest `F` has a topological order in which every
arc descends.  Its arcs give the perfect matching in (2.2), and `C` gives
the perfect matching in (2.1).

Conversely, take perfect matchings `C` and `F` in (2.1) and (2.2).
The strict decrease along every arc of `F` makes `F` acyclic.  Its tails
are exactly `L-R`, and its heads are exactly `L-S`, so Theorem 1.1 applies.
Hall's theorem gives the equivalence with (2.3)--(2.4).  \(\square\)

Thus the hard quantifier is no longer hidden: one must choose the missing
head set and one topological order **jointly** with the two matchings.  Once
they are chosen, no subtour inequalities remain.

Forced protected arcs fit this statement literally.  A forced arc whose
tail is outside `R` must occur in (2.2) and imposes its order inequality; a
forced arc whose tail lies in `R` must occur in (2.1) and forces its head
into `S`.  Delete their occupied tails and heads and apply (2.3)--(2.4) to
the residual instance.  Incompatible forced arcs, or a directed cycle among
the forced nonroot arcs, are exact immediate obstructions.

## 3. Positive-coefficient matrix-tree criterion

Give every allowed successor arc `x -> y` an edge variable `t_xy` and give
every possible head `y` a variable `z_y`.  Define the weighted out-Laplacian

\[
 \begin{aligned}
  \mathcal L_{xx}&=\sum_{x\to y\in Q}t_{xy}z_y,\\
  \mathcal L_{xy}&=-t_{xy}z_y
       \quad(x\ne y,\ x\to y\in Q),
 \end{aligned}
\tag{3.1}
\]

with all other off-diagonal entries zero.  Delete the rows and columns
indexed by `R` and put

\[
                \mathcal T_R(\mathbf z,\mathbf t)
                =\det \mathcal L[L-R,L-R].
\tag{3.2}
\]

Also define the root-closure matching polynomial

\[
 \mathcal C_R(\mathbf z,\mathbf t)
 =\sum_{\substack{f:R\hookrightarrow L\\x\to f(x)\in Q\ (x\in R)}}
       \prod_{x\in R}t_{x,f(x)}z_{f(x)}.
\tag{3.3}
\]

The sum is over injections, so every monomial in `mathcal C_R` is
squarefree in the head variables.

### Theorem 3.1 (exact positive coefficient)

The number of cycle covers of `Q` every cycle of which meets `R` is exactly

\[
 \boxed{
 [\prod_{v\in L}z_v]\,
 \mathcal T_R(\mathbf z,\mathbf 1)
 \mathcal C_R(\mathbf z,\mathbf 1).}
\tag{3.4}
\]

In particular, a rooted cycle cover exists if and only if the coefficient
in (3.4) is positive.

#### Proof

The directed matrix-tree/forest theorem expands `mathcal T_R` as the sum
over all spanning directed forests in which every nonroot has one outgoing
arc and every directed path ends in `R`.  An arc `x -> y` contributes the
factor `z_y`, so the exponent of `z_y` is the indegree of `y` in the forest.
Although (3.2) is written as a determinant, the forest expansion has
nonnegative integral coefficients.

A monomial contributing to the full squarefree head monomial in (3.4) must
use every head at most once in the forest.  Its forest is therefore a
rooted linear forest.  The closure monomial must use exactly the complementary
head set, and (3.3) says precisely that those heads receive a matching from
`R`.  Theorem 1.1 then gives one rooted cycle cover.  Conversely, deleting
the root-tail arcs of any rooted cycle cover gives exactly one such forest
monomial and its complementary closure monomial.  This correspondence is
bijective.  \(\square\)

Forbidden arcs are handled by setting their `t` variables to zero.  A
partial protected matching is forced by differentiating once in each of its
arc variables before setting every remaining allowed `t` variable to one.
Since every selected arc set is simple, the polynomial is multilinear in
the `t` variables.  This gives an exact occurrence-labelled nonvanishing
test, not merely an aggregate factor count.

## 4. The natural object is a three-matroid intersection

On the successor arcs of `Q`, let `P_tail` and `P_head` be the two partition
matroids imposing at most one selected arc at each tail and head.  Let
`G_R` be the direct sum of

* the graphic matroid on the underlying multigraph of arcs whose tails lie
  in `L-R`; and
* the free matroid on arcs whose tails lie in `R`.

### Theorem 4.1 (exact three-matroid form)

A rooted cycle cover is exactly an `N`-element set which is a common base of
`P_tail` and `P_head` and is independent in `G_R`.

#### Proof

The two partition bases say exactly that the selected arcs are a cycle
cover.  After deleting root-tail arcs, indegree and outdegree are at most
one.  In such a directed graph, an undirected graphic circuit is exactly a
directed cycle (with a directed two-cycle represented by two parallel
underlying edges).  Independence in `G_R` therefore says precisely that no
cycle survives after the root-tail arcs are deleted.  By Theorem 1.1 this is
equivalent to every original cycle meeting `R`.  \(\square\)

This explains why adding a graphic rank inequality to the protected
Ore--Ryser matching theorem is not an ordinary matroid-intersection
corollary: the matching already uses two partition matroids.

The common-independent-set system is not itself a matroid.  On vertices
`1,2,3,4,5`, consider

\[
 I=\{1\to2,2\to3\},
 \qquad
 J=\{4\to2,2\to5,1\to3\}.
\tag{4.1}
\]

Both are tail/head matchings and underlying forests.  But no member of
`J-I` can be added to `I`: `4->2` repeats head `2`, `2->5` repeats tail
`2`, and `1->3` repeats both tail `1` and head `3`.  Thus augmentation
fails.  This rules out treating the combined feasible sets as one hidden
matroid; it does not rule out a problem-specific lift or an additional
Boolean theorem.

## 5. Exact `C_6/C_8` parity after one matching is fixed

Let `pi` be the successor permutation of a second matching.  Suppose an
alternating `2t`-cycle supported wholly in the second-matching coordinate
replaces

\[
 x_i\to y_i
 \quad\text{by}\quad
 x_i\to y_{i+1}
 \qquad(i\in\mathbb Z_t),
\tag{5.1}
\]

where `y_i=pi(x_i)`.  Let `pi'` be the new permutation.

### Theorem 5.1 (head-cycle rank and parity)

If `c(pi)` denotes the number of permutation cycles, then

\[
 \boxed{
 |c(\pi')-c(\pi)|\le t-1,
 \qquad
 c(\pi')-c(\pi)\equiv t-1\pmod2.}
\tag{5.2}
\]

If the `t` moved heads lie in `t` distinct cycles of `pi`, the switch merges
those cycles into one and

\[
                         c(\pi')-c(\pi)=-(t-1).
\tag{5.3}
\]

#### Proof

The switch left-multiplies `pi` by the `t`-cycle
`(y_1 y_2 ... y_t)`.  A `t`-cycle is a product of `t-1`
transpositions, and multiplication by one transposition changes the number
of permutation cycles by exactly one.  This gives the bound and parity in
(5.2).  When the moved points lie in distinct cycles, the standard cycle
splicing rule joins all `t` cycles into one, proving (5.3).  \(\square\)

### Corollary 5.2 (the fixed-matching local-actuator boundary)

1. A second-matching `C_6` (`t=3`) changes the factor-component count by an
   even number.  It can merge three distinct cycles into one, but cannot
   merge exactly two cycles into one.
2. A second-matching `C_8` (`t=4`) changes the component count by an odd
   number.  In the Middle-Levels incidence graph, `C_8` is the first circuit
   length not ruled out from a rank-one fixed-matching move by girth and
   parity: that graph has no `C_4`, while `C_6` has the even-parity
   obstruction in item 1.  At the permutation level, a suitable incumbent
   order lets a `C_8` absorb one rootless cycle into one rooted cycle.  (For
   a general bipartite host admitting a `C_4`, the corresponding `t=2`
   switch can already have rank one.)
3. The coherent canonical `C_6` which changes a two-component factor into
   a Hamilton factor cannot preserve either perfect-matching coordinate:
   if it did, item 1 would force an even component-count change.  Its binary
   pull action intrinsically uses recolouring of both matching coordinates.

Thus the fixed-`M_0` normal form is exact for selecting a terminal factor,
but it is not a coordinate system in which the successful coherent `C_6`
pull remains a one-coordinate move.

For literal confirmation of the rank-one possibility in item 2, take
`pi=(1 2)(3 4)` and left-multiply by the four-cycle
`(1 3 2 4)`.  The result is the single cycle `(1 4 2 3)`.

## 6. A common-core ring cannot make the whole successor host acyclic

The ordered-Hall theorem needs only the **selected** nonroot arcs to
descend.  A tempting stronger shortcut is to choose `M_0` and `R` so that
the entire induced successor digraph `Q[L-R]` is acyclic.  Then every
second perfect matching would automatically be rooted.  The common-core
ring can never do this.

### Theorem 6.1 (common-core forcing-set no-go)

Let `G=ML_m`, let `M_0` be any perfect matching, and form its **full**
successor digraph `Q^{\rm full}` before any additional protected-edge
deletions.  Let

\[
 R=\{K\cup\{a\}:a\in A\}\subseteq\binom{[2m-1]}{m-1},
\tag{6.1}
\]

where `|K|=m-2`, `A` is an `m`-set disjoint from `K`, and the one remaining
coordinate outside `K union A` is the omitted common-ring label.  For every
`m>=4`,

\[
             \boxed{Q^{\rm full}[L-R]\text{ contains a directed cycle}.}
\tag{6.2}
\]

Equivalently, after deleting the `m` matched pairs indexed by `R`, the
restriction of `M_0` is never a unique perfect matching.

#### Proof

Assume `Q^{\rm full}[L-R]` is acyclic.  It has a source `y`.  Let `u_y` be the upper
vertex matched to `y` by `M_0`.  In the bipartite graph obtained by deleting
`R` and the upper vertices `M_0(R)`, every nonmatching lower neighbour `x`
of `u_y` would give an incoming arc `x->y`.  Since `y` is a source,
`u_y` has degree one in this residual graph.

On the other hand, an upper `m`-set contains at most two members of `R`.
Indeed, containing even one member `K+a` forces it to contain all of `K`,
leaving only two positions outside `K`.  Deleting `R` therefore removes at
most two of the original `m` lower facets of `u_y`.  Since `u_y` itself was
not deleted, its residual degree is at least

\[
                              m-2\ge2,
\]

a contradiction.  The equivalence with uniqueness is the standard
alternating-cycle criterion: directed cycles of `Q[L-R]` are exactly
`M_0`-alternating cycles in the residual bipartite graph.  \(\square\)

This no-go is stronger than the elementary lower bound `|R|>=m-1` obtained
from unique-perfect-matching leaf stripping.  It uses the punctured-star
geometry of the actual common-core roots.  It does **not** say that no
single rooted second matching exists; it says that root safety cannot be
made automatic for the whole unpruned residual matching fibre.  A protected
forbidden-edge bank could delete all such cycles, but that is an additional
correlated phase assertion rather than a consequence of the root geometry.

## 7. Exact remaining same-factor theorem

Let the audited core-pinned reservoir be extended to one two-factor and
edge-colour that factor as `M_0 dotunion M_1`.  Retain one colour as
`M_0`; its successor graph already contains the protected arcs of the other
colour as forced arcs.  Then the remaining same-factor topology question is
exactly either of the following equivalent statements.

1. The forced/forbidden version of the coefficient in (3.4) is positive.
2. There are `S,prec` extending all forced nonroot order relations for
   which both residual Hall systems (2.3)--(2.4) pass.
3. The two partition bases and the rooted graphic constraint of Theorem 4.1
   have one common integral point containing the forced protected arcs.

This is the correct strengthening of protected Hall.  The protected
Ore--Ryser theorem proves existence of a two-factor, but it does not prove
the squarefree-head coefficient in (3.4), and Theorem 6.1 shows that one
cannot remove the correlation by making the entire common-core residual
host acyclic.

There are consequently two proof-safe local routes.

* **Fixed matching:** build an ordered-Hall terminal state; `C_8` is the
  first local rank-one circuit, while `C_6` circuits must be organized as
  ternary rooted hypertree steps.
* **Coherent pull:** allow both matching coordinates to change and use the
  already proved binary coherent `C_6`; then accessibility and phase cover
  must be proved in the common pull orbit rather than in one fixed-successor
  graph.

The theorem isolates this choice without claiming either remaining
existence statement.

## 8. Dependencies

| role | file |
|---|---|
| protected factor extension | `MATH_THEOREM_CORE_PINNED_UNIFORM_SPREAD_AND_EXACT_RESIDUAL_HOST_CUTS_20260804.md` |
| rooted fixed-matching equivalence | `MATH_THEOREM_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_20260804.md` |
| coherent binary `C_6` ring pull | `MATH_THEOREM_COHERENT_SINGLE_PULL_THREE_RING_HAMILTON_PLANTING_20260804.md` |
| exact protected pull phase cut | `MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md` |
