# Punctured-wreath co-design is exactly a collision pseudoforest

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** exact compiler and exact one-row augmentation theorem; existence
of a near-optimal pseudoforest row set remains open

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 \mathcal L=\binom{[b]}{r-1},\qquad
 N=|\mathcal M|,
 \tag{0.1}
\]

Throughout, \(r\ge2\).

and let \(\mathscr F\) be an exact middle-wreath factor: its rows are cyclic
orders on \([b]\), and their cyclic rank-\(r\) windows partition
\(\mathcal M\).

For a row \(C\), let \(\mathsf L(C)\) be its \(b\) cyclic
rank-\((r-1)\) windows.  These windows are distinct: their position sets
are distinct proper cyclic intervals, and the row labels are a bijection.
For a set
\(\mathscr S\subseteq\mathscr F\), put

\[
 \mu_{\mathscr S}(T)
   =|\{C\in\mathscr S:T\in\mathsf L(C)\}|.
 \tag{0.2}
\]

The **collision-incidence graph** \(J(\mathscr S)\) is the bipartite graph
with row shore \(\mathscr S\), collision-target shore

\[
 \mathcal D(\mathscr S)
   =\{T\in\mathcal L:\mu_{\mathscr S}(T)\ge2\},
 \tag{0.3}
\]

and edge \(CT\) exactly when \(T\in\mathsf L(C)\).  Isolated row vertices
are retained.

The main result is the following exact compiler.

> **Pseudoforest compiler.**  The rows of \(\mathscr S\) can each be
> punctured at one start so that all clean rank-\((r-1)\) windows are
> distinct if and only if \(J(\mathscr S)\) is a pseudoforest, meaning that
> every connected component has at most one cycle.

Because the middle windows of distinct factor rows are already disjoint,
these punctures are exactly a target-disjoint family of directed punctured
wreaths.  Equivalently, their \((b-1)|\mathscr S|\) same-start flags form a
matching in the middle inclusion graph \(B_r\).

The criterion is constructive.  On a tree component, root at a row; on a
unicyclic component, orient its unique cycle and root every attached tree
towards the cycle.  This chooses, for every repeated target \(T\), exactly
\(\mu_{\mathscr S}(T)-1\) occurrence rows in which \(T\) is made dirty,
and it chooses no row more than once.

It also gives an exact one-row augmentation test.  Suppose
\(J(\mathscr S)\) is a pseudoforest and a new factor row \(C\) has \(t\)
lower windows already present among the rows of \(\mathscr S\).  Each such
window attaches \(C\) to one old component: to its unique old owner if its
old multiplicity is one, and to its collision-target vertex if its old
multiplicity is at least two.  Let the \(t\) attachments meet \(k\) old
components, of cycle ranks \(\beta_1,\ldots,\beta_k\in\{0,1\}\).  Then

\[
 \boxed{\quad
 J(\mathscr S\cup\{C\})\text{ is a pseudoforest}
 \iff
 \sum_{j=1}^k\beta_j+t-k\le1.
 \quad}
 \tag{0.4}
\]

Thus (0.4) is a literal augment-or-bicycle certificate, not merely a
degree heuristic.

Finally define

\[
 \pi(\mathscr F)
   =\max\{|\mathscr S|:\mathscr S\subseteq\mathscr F,
                    \ J(\mathscr S)\text{ is a pseudoforest}\}.
 \tag{0.5}
\]

The maximum number of target-disjoint punctured wreaths obtainable from
the fixed middle factor \(\mathscr F\) is exactly \(\pi(\mathscr F)\).
Consequently this factor closes the middle/first-shadow co-design gate if

\[
 \pi(\mathscr F)
   ={N\over2(r+2)}-o(N/r).
 \tag{0.6}
\]

This replaces the informal instruction “balance the first shadow and then
choose dirty starts” by one exact, polynomially checkable condition.  It
does not prove (0.6) for the MNW/MSW factor or for any switched factor.

## 1. From dirty starts to a capacitated incidence matching

Fix \(\mathscr S\subseteq\mathscr F\).  A dirty-start choice is a function

\[
                 \delta:\mathscr S\longrightarrow\mathcal L,
 \qquad \delta(C)\in\mathsf L(C).
 \tag{1.1}
\]

The clean lower deck of \(C\) is
\(\mathsf L(C)\setminus\{\delta(C)\}\).  Since the windows inside one row
are distinct, all clean lower decks are mutually disjoint if and only if,
for every \(T\in\mathcal D(\mathscr S)\), at least

\[
                  \mu_{\mathscr S}(T)-1
 \tag{1.2}
\]

of its occurrence rows choose \(T\) as their dirty window.

Make \(\mu_{\mathscr S}(T)-1\) identical demand clones of every collision
target \(T\), each adjacent to all occurrence rows of \(T\).  Give each row
capacity one.  Call the resulting bipartite demand graph
\(K(\mathscr S)\).

### Lemma 1.1 (exact dirty-tail matching)

A collision-free dirty-start choice exists if and only if
\(K(\mathscr S)\) has a matching saturating all target-demand clones.

#### Proof

If the clones can be matched, dirty in every matched row the target of its
matched clone.  No row receives two instructions.  For each \(T\), exactly
\(\mu(T)-1\) occurrences are removed, leaving one.  Every still-unmatched
row may be punctured at an arbitrary one of its lower windows; this can only
remove another occurrence and cannot create a collision.

Conversely, suppose a collision-free puncturing is given.  For each
collision target \(T\), at least \(\mu(T)-1\) of its occurrence rows were
punctured at \(T\).  Match the demand clones of \(T\) to any
\(\mu(T)-1\) of those rows.  A row is used at most once because it has one
dirty start. \(\square\)

The matching in Lemma 1.1 is an ordinary integral bipartite matching.  In
particular, there is no phase-switching or multi-commodity caveat in this
compiler.

## 2. Hall is exactly the pseudoforest condition

### Theorem 2.1 (pseudoforest compiler)

For \(\mathscr S\subseteq\mathscr F\), the following are equivalent.

1. Each row of \(\mathscr S\) admits one dirty start and the clean lower
   decks are mutually disjoint.
2. For every \(\mathcal A\subseteq\mathcal D(\mathscr S)\),

   \[
    \sum_{T\in\mathcal A}(\mu_{\mathscr S}(T)-1)
       \le |N_{J(\mathscr S)}(\mathcal A)|.
    \tag{2.1}
   \]

3. The collision-incidence graph \(J(\mathscr S)\) is a pseudoforest.
4. Every row subfamily \(\mathscr A\subseteq\mathscr S\) satisfies the
   clean-deck Hall inequalities

   \[
        (b-1)|\mathscr A|
          \le\left|\bigcup_{C\in\mathscr A}\mathsf L(C)\right|.
    \tag{2.3}
   \]

#### Proof

The equivalence of 1 and 2 is the capacitated Hall theorem applied to the
demand clones of Lemma 1.1.  Equivalently, make \(b-1\) demand clones of
each selected row, all adjacent to its \(b\) lower windows, and give every
lower target capacity one.  Saturating these row clones chooses
\(b-1\) distinct clean windows from every row; because a row has exactly
\(b\) windows, the unused one is its dirty start.  Capacitated Hall for
this second graph is exactly (2.3), proving the equivalence of 1 and 4.

For \(\mathcal A\subseteq\mathcal D(\mathscr S)\), the graph induced by
\(\mathcal A\) and its full row neighborhood has

\[
 e=\sum_{T\in\mathcal A}\mu_{\mathscr S}(T),
 \qquad
 v=|\mathcal A|+|N_{J(\mathscr S)}(\mathcal A)|.
 \tag{2.2}
\]

Thus (2.1) is exactly \(e\le v\).  Every subgraph of a pseudoforest has at
most as many edges as vertices, so 3 implies 2.  Conversely, if a connected
component \(Q\) of \(J(\mathscr S)\) contained two independent cycles,
then \(e(Q)\ge v(Q)+1\).  Taking \(\mathcal A\) to be all collision-target
vertices of \(Q\) makes (2.2) equal to the complete component and violates
(2.1).  Hence 2 implies 3. \(\square\)

Condition (2.3) is the direct inclusion-graph formulation: it asks for one
ordinary capacitated matching, not for separately rounded lower targets.
The pseudoforest form is its sparse topological normal form after all
degree-one target leaves are suppressed.

### Proposition 2.2 (explicit component compiler)

When \(J(\mathscr S)\) is a pseudoforest, dirty starts can be found by
independent leaf peeling in its components.

* In a tree component, root the tree at an arbitrary row vertex.  At every
  collision-target vertex \(T\), retain the occurrence edge from \(T\)
  towards the root and dirty all occurrence edges from \(T\) away from the
  root.
* In a unicyclic component, orient the unique cycle.  At every target on the
  cycle retain its incoming cycle occurrence and dirty every other
  occurrence edge at that target: the outgoing cycle edge and all
  off-cycle edges.  Root every tree attached to the cycle at its attachment
  and, at every off-cycle target, retain the occurrence towards the root
  and dirty the occurrences away from the root.

Every collision target then has exactly one retained occurrence, while
every row is instructed to dirty at most one occurrence.  Rows receiving no
instruction are punctured arbitrarily.

#### Proof

In a rooted bipartite tree, every nonroot row is the child of exactly one
target and is therefore dirtied exactly once; the root row is never
dirtied by the collision compiler.  At a target, precisely its parent edge
is retained.  On a unicyclic component the directed cycle gives every cycle
row exactly one dirty instruction.  Retaining only the incoming occurrence
at each cycle target, and dirtying its outgoing and off-cycle child-row
occurrences, leaves that target exactly once.  The attached rooted trees
behave as in the first case. \(\square\)

## 3. Physical inclusion-deck lift

### Theorem 3.1 (exact factor-restricted co-design)

Let \(\mathscr F\) be an exact middle-wreath factor and
\(\mathscr S\subseteq\mathscr F\).  There is a target-disjoint family of
directed punctured wreaths using exactly the rows of \(\mathscr S\) if and
only if \(J(\mathscr S)\) is a pseudoforest.  Such a family contains
\(|\mathscr S|\) wreaths and covers exactly

\[
                 (b-1)|\mathscr S|=2r|\mathscr S|
 \tag{3.1}
\]

middle targets and the same number of lower targets.

#### Proof

The rank-\(r\) windows of the rows of \(\mathscr F\) are mutually
distinct.  Choose the dirty lower window in each selected row by Theorem
2.1, and linearly orient the cyclic row with that occurrence at start zero.
The same start deletes one of that row's middle windows.  All remaining
middle windows are still distinct, and Theorem 2.1 makes all remaining
lower windows distinct.  The same-start containments are therefore a
matching in the inclusion graph \(B_r\), split into complete
\(2r\)-edge flag decks.

The converse follows by reading the one dirty lower occurrence in every
punctured wreath and applying Theorem 2.1. \(\square\)

### Corollary 3.2 (exact scalar gate inside a factor)

The maximum number of target-disjoint punctured wreaths obtainable from
\(\mathscr F\) is \(\pi(\mathscr F)\) from (0.5).  Since

\[
 { |\mathcal L|\over b-1}
   ={(r/(r+2))N\over2r}
   ={N\over2(r+2)},
 \tag{3.2}
\]

condition (0.6) produces a family missing only \(o(N)\) lower targets and

\[
                   {2N\over r+2}+o(N)=o(N)
 \tag{3.3}
\]

middle targets.

If equality holds in (3.2), its clean flag union is an
\(\mathcal L\)-saturating matching in \(B_r\).  It is one colour class of
a proper \((r+2)\)-edge-colouring of \(B_r\): remove that matching, apply
Kőnig's theorem to the remaining bipartite graph of maximum degree
\(r+1\), and restore the matching as the last colour.

Thus the structured Kőnig-colouring route and the factor-restricted
pseudoforest route coincide at exact lower saturation.

## 4. A literal one-row augmentation test

Assume \(J(\mathscr S)\) is a pseudoforest, and let
\(C\in\mathscr F\setminus\mathscr S\).  For each
\(T\in\mathsf L(C)\) already occurring among \(\mathscr S\), define its
old **attachment vertex** as follows.

* If \(\mu_{\mathscr S}(T)=1\), attach to the unique old row containing
  \(T\).
* If \(\mu_{\mathscr S}(T)\ge2\), attach to the old collision-target
  vertex \(T\) of \(J(\mathscr S)\).

Count attachments with multiplicity.  Let \(t\) be their number, let
\(Q_1,\ldots,Q_k\) be the distinct old components they meet, and put

\[
              \beta_j=e(Q_j)-v(Q_j)+1\in\{0,1\}.
 \tag{4.1}
\]

### Theorem 4.1 (augment-or-bicycle formula)

The component created by adjoining \(C\) has cycle rank

\[
                  \beta_{\rm new}
                    =\sum_{j=1}^k\beta_j+t-k.
 \tag{4.2}
\]

Consequently \(C\) can be added and all rows repunctured collision-free if
and only if \(\beta_{\rm new}\le1\).

#### Proof

A lower target of old multiplicity zero creates no collision vertex.  A
target of old multiplicity one creates a new degree-two target vertex
between \(C\) and its unique old owner; suppressing that vertex gives one
attachment edge and changes no cycle rank.  A target of old multiplicity at
least two contributes one new edge from \(C\) to its existing target
vertex.  Thus, after harmless degree-two suppressions, the new component is
obtained from the disjoint old components \(Q_1,\ldots,Q_k\) by adding one
new row vertex and \(t\) attachment edges.  Hence

\[
 \begin{aligned}
 e_{\rm new}-v_{\rm new}+1
 &=\sum_j e(Q_j)+t-
      \left(\sum_jv(Q_j)+1\right)+1\\
 &=\sum_j\bigl(e(Q_j)-v(Q_j)+1\bigr)+t-k,
 \end{aligned}
\]

which is (4.2).  All untouched components remain pseudoforests, so Theorem
2.1 gives the last assertion. \(\square\)

Formula (4.2) is directly algorithmic.  It allows any number of attachments
to distinct tree components, one repeated hit in total, and no repeated hit
after the available cycle budget has already been spent.  When it fails,
the merged component itself is an explicit Hall/bicycle obstruction.

## 5. Exact optimization and scope

For a fixed row set \(\mathscr S\), the dirty-tail demand graph in Section
1 has at most \(b|\mathscr S|\) edges.  A maximum bipartite matching either
constructs all dirty starts or returns a Hall cut; equivalently, a linear
scan of \(J(\mathscr S)\) either runs Proposition 2.2 or returns a component
with two cycles.  The factor-restricted puncturing problem is therefore
exactly certified in polynomial time.

The theorem proves:

1. an if-and-only-if physical compiler from a selected middle-factor row
   set to target-disjoint punctured wreaths;
2. an explicit componentwise construction of the dirty starts;
3. the exact scalar parameter \(\pi(\mathscr F)\) governing the largest
   such family inside a fixed factor;
4. a one-row augmentation test with an explicit bicycle certificate; and
5. the precise connection to a structured Kőnig colour class at exact
   lower saturation.

It does **not** prove that the canonical MNW/MSW factor, its C8-switch
component, or any other known exact middle factor satisfies (0.6).  It does
not assert that first-shadow multiplicity balance alone implies the
pseudoforest property.  It does not solve the deeper nested-shadow,
factor-order, endpoint-order, or universal-word lifts.

## 6. Checker

The finite audit is

```text
scratch/audit_punctured_wreath_collision_pseudoforest_compiler_20260821.py
```

It constructs the canonical wreath factors through \(b=9\), exhausts their
row subsets, compares the graph criterion with the dirty-tail matching,
materializes the componentwise punctures, and checks (4.2) for every
one-row extension.  The computation is an audit only; none of the proofs
above depends on it.
