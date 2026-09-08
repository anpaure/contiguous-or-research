# Actual even receiver banks reduce to an invisible-bicycle escape inequality

**Date:** 2026-08-05  
**Method:** receiver-rectangle completeness, Hall deficiency, bicircular
rank, and the bicycle-kernel classification; no computation  
**Status:** unconditional exact reduction.  It identifies the only
possible even-cut-level obstruction for an actual paired-petal bank.  It
does not prove that the obstruction is absent in every necklace sector.

## 1. Input

Work at an even cut length after:

1. special-reset vertices and its two hub-colour classes are removed;
2. the incoming singleton, if any, is removed and the parity-compatible
   outgoing socket vertex is installed; and
3. every fixed passive-petal pair is replaced by its quotient receiver
   rectangle

   \[
                              A_j\mathbin\square B_j.
   \tag{1.1}
   \]

Let `G=(L,R;E)` be the remaining ordinary bipartite sector graph.  The
augmented matching theorem says that a protected extension exists exactly
when the graph obtained by adding the two private terminals for every job
has a perfect matching.

For `U subseteq L`, put

\[
 D=N_G(U),\qquad
 J_U=\{j:A_j\cap U=\varnothing\}.
\tag{1.2}
\]

For every `j in J_U`, retain the residual option list

\[
                              B_j^U=B_j\setminus D.
\tag{1.3}

\]

Build a labelled multigraph `Q_U` on the surviving `B`-options:

* a two-element list is an edge;
* a one-element list is a loop; and
* an empty list is a zero-vertex edge component.

## 2. Exact min--max

### Theorem 2.1 (invisible-bicycle Hall formula)

The complete left-shore Hall family of the augmented receiver graph is
equivalent to

\[
 \boxed{
 \sum_{C\in\operatorname{Comp}(Q_U)}
       \bigl(|E(C)|-|V(C)|\bigr)_+
 \le |N_G(U)|-|U|
 \qquad(U\subseteq L).}
\tag{2.1}

The complete right-shore family is the symmetric inequality formed from
the `A`-option multigraphs of jobs whose `B`-lists avoid the chosen right
set.

#### Proof

Rectangle completeness gives

\[
 A_j\cap U\ne\varnothing\quad\Longrightarrow\quad B_j\subseteq D.
\tag{2.2}

Every such visible job therefore has an empty residual `B`-list.  Its one
unit of endpoint-list deficiency cancels the one private neighbour
contributed by that same job in the augmented Hall inequality.  Only the
invisible jobs `J_U` remain.

For lists of size at most two, the exact transversal deficiency is the
bicircular surplus.  In a connected endpoint multigraph with `e` job
edges and `v` receiver vertices, at most `v` jobs can choose distinct
endpoints, and `min(e,v)` can: orient a spanning tree away from a root and,
when `e>=v`, add and cyclically orient one extra edge.  Hence the component
deficiency is `(e-v)_+`.  Summing components and comparing with the
ordinary Hall slack `|D|-|U|` proves (2.1).  The other shore is identical.
\(\square\)

This formula is exact after all necklace-orbit coalescence: parallel edges
and loops in `Q_U` are retained with their occurrence/job labels.

## 3. Bicycle kernels are the only nontrivial cores

Call a connected multigraph a **bicycle** when its cyclomatic number is at
least two, equivalently

\[
                              |E|-|V|\ge1.
\tag{3.1}
\]

An empty residual job is the zero-vertex degenerate bicycle and contributes
one directly.

### Lemma 3.1 (minimal bicycle shapes)

Every nondegenerate connected component contributing to the left side of
(2.1) contains one of the following subdivisions:

1. a theta: three internally vertex-disjoint paths with common endpoints;
2. a tight handcuff: two cycles meeting in one vertex; or
3. a loose handcuff: two vertex-disjoint cycles joined by one path.

Conversely each displayed graph has bicircular surplus one after all
inessential tree branches are deleted.

#### Proof

Delete degree-zero and degree-one vertices repeatedly.  A component with
cyclomatic number at least two retains a nonempty minimum-degree-two core.
Take two cycles in that core.  If they share two vertices, their first and
last common vertices give a theta.  If they share exactly one, they give a
tight handcuff.  If they are disjoint, a shortest joining path gives a
loose handcuff.  Suppressing degree-two subdivisions does not change
`|E|-|V|`.  Each minimal shape has cyclomatic number two and hence surplus
one.  \(\square\)

Therefore trees, isolated loops, and unicyclic collision components are
automatically harmless.  A genuine even-level failure needs ordinary Hall
slack too small to pay a collection of **invisible empty jobs or trapped
bicycles**.

## 4. Exact remaining geometric lemma

For a literal paired-petal job over hub `H`, the two endpoints of either
diagonal in (1.1) are double expansions whose rank-two cut difference has
intersection `H`.  Distinct passive pairs over one fixed literal hub have
disjoint four-vertex squares.  Thus a bicycle in `Q_U` cannot be created
inside one pointed hub fan alone, apart from the already separated
degenerate case of a single invisible job whose two options both lie in
`N_G(U)`.  Every nondegenerate multi-edge bicycle must use either:

1. receiver states generated from different literal hubs; or
2. necklace rotations which coalesce different pointed squares.

This yields the precise proof target.

> **Invisible-bicycle escape lemma.**  For every actual even-level
> paired-petal bank and every ordinary shore set `U`, each unit of
> bicircular surplus in `Q_U` injects into a distinct unit of ordinary
> expansion slack
>
> \[
>                         |N_G(U)|-|U|.
> \tag{4.1}
> \]

By Theorem 2.1 and its symmetric version, this lemma is equivalent to the
entire even protected receiver-extension theorem.

It is enough to prove the lemma only on the three bicycle kernels in
Lemma 3.1, with arbitrary subdivided paths and orbit coalescence retained.
One possible certificate is an alternating escape from each kernel to a
receiver vertex outside `N_G(U)`; another is a direct injection into an
unused ordinary mate in a fixed sector matching.

## 5. Why simpler conditions do not suffice

Pairwise distinct receiver-edge orbits do not prevent shared endpoints.
Pairwise edge-disjoint receiver squares do not prevent a projective-plane
type vertex collision pattern.  Pairwise intersection at most one also
does not rule out theta or handcuff kernels.  The quantity in (2.1), not
linear hypergraph sparsity by itself, is the exact invariant.

Similarly, proving ordinary Hall for `G` gives only nonnegative slack in
(4.1); a tight ordinary set must have zero invisible bicycle surplus.
This is the sharp place where actual cyclic interval/sector geometry must
enter.

## 6. Scope

Proved:

1. exact cancellation of all receiver jobs visible from a Hall shore set;
2. exact reduction of the remaining deficit to bicircular surplus;
3. reduction of every nontrivial surplus component to three bicycle
   kernels; and
4. localization of such kernels to cross-hub or quotient-coalescence
   interactions.

Not proved:

1. the invisible-bicycle escape lemma;
2. its odd-level wrap/blossom analogue;
3. simultaneous PBBS halo placement; or
4. the complete adjacent-necklace or universal-word theorem.
