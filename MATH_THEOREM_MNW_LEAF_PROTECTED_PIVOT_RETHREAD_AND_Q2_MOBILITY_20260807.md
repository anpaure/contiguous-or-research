# MNW leaf protection: one pivot survives in the rethreaded half

**Date:** 2026-08-07  
**Method:** pure mathematics; MNW flippability hypertrees and exact turn
calculus  
**Status:** unconditional protected-path theorem and exact full-path no-go
inside the MNW spanning-tree architecture.  One prescribed short owner
geodesic can be retained in the **rethreaded** half of a middle-levels
Hamilton cycle.  The rethreading is Catalan-scale and genuinely changes
the upper-\(q2\) turn map.  Upper-\(q2\) surjectivity remains a colored
spanning-hypertree condition and is not proved here.

## 0. Outcome

Let \(\Omega\) be a \(2m\)-set and let \(z\notin\Omega\).  Given a shortest
rank-\((m+1)\) Johnson geodesic

\[
 Y_0,Y_1,\ldots,Y_t\in\binom\Omega{m+1},             \tag{0.1}
\]

assume

\[
                         2t+1\le m.                  \tag{0.2}
\]

Then there is a Hamilton cycle of \(ML_{m+1}\) on
\(\Omega\cup\{z\}\) whose **rethreaded \(z\)-free half** contains the
complete incidence lift

\[
 Y_0,\ Y_0\cap Y_1,\ Y_1,\ldots,
 Y_{t-1}\cap Y_t,\ Y_t.                              \tag{0.3}
\]

In particular, the buffered sharp-pivot path with \(3h\) owner
transitions from
`MATH_THEOREM_SINGLE_SHARP_PIVOT_MSW_PROTECTED_HAMILTON_HOST_20260807.md`
may be placed in the rethreaded half whenever

\[
                         6h+1\le m.                  \tag{0.4}
\]

For \(h=\Theta(\sqrt m)\), (0.4) holds in every sufficiently large
dimension.

This is strictly different from preserving the whole canonical MSW half.
Indeed, within the MNW spanning-hypertree construction, no complete
canonical complementary path can remain untouched: every path loses at
least one incidence edge.  A short interval can survive because a leaf
path loses exactly one edge, and that edge can be placed outside the
protected interval by orienting the path.

## 1. The incidence graph of an MNW hypertree is a tree

Let

\[
 \mathcal H_m=(\mathcal D_m,\Psi_m)
\]

be the marked flippability hypergraph of Mütze--Nummenpalo--Walczak.
Every hyperedge has support size three or four.  If \(\mathcal T\) is a
spanning tree in their recursive sense, form its incidence graph
\(I(\mathcal T)\), with one shore \(\mathcal D_m\), the other shore
\(\mathcal T\), and ordinary incidence edges.

### Lemma 1.1 (incidence-tree identity)

The graph \(I(\mathcal T)\) is an ordinary tree.  Consequently it has a
leaf \(x_*\in\mathcal D_m\), and \(x_*\) belongs to exactly one selected
flippable tuple.

Moreover,

\[
 \sum_{\tau\in\mathcal T}(|\operatorname{supp}\tau|-1)
 =|\mathcal D_m|-1.                                  \tag{1.1}
\]

#### Proof

Induct on the recursive definition of an MNW spanning tree.  At the top
step, a tuple \(\tau\) of support size \(\ell\) meets each of \(\ell\)
disjoint recursively spanned vertex blocks in exactly one vertex.  By the
induction hypothesis their incidence graphs are trees.  Adding the new
tuple-node and its \(\ell\) incidence edges joins those \(\ell\) trees
without creating a cycle.  This proves that the full incidence graph is a
tree.  Every tuple-node has degree three or four, so every ordinary leaf is
on the Dyck-word shore.  The edge count of this ordinary tree gives (1.1).
\(\square\)

MNW prove that every spanning tree of \(\mathcal H_m\) is conflict-free.
Thus, if several selected tuples meet one Dyck word, their marks are
different.  At the leaf \(x_*\), there is exactly one mark and hence
exactly one selected flipping cycle removes an edge of the canonical path
\(P(x_*)\).

## 2. Exact full-path no-go

### Theorem 2.1 (a complete rethreaded path cannot be fixed)

Let \(\mathcal T\) be any MNW spanning tree on more than one Dyck word,
and Hamiltonize the canonical cycle factor by symmetric difference with
the selected flipping cycles.  For every \(x\in\mathcal D_m\), at least
one incidence edge of \(P(x)\) is absent from the resulting Hamilton
cycle.

#### Proof

The ordinary incidence graph \(I(\mathcal T)\) is connected, so every
Dyck-word vertex \(x\) has positive degree.  A selected tuple incident
with \(x\) has one mark \(a\), and its witnessing flipping cycle removes
the canonical edge \(e(x,a)\).  The replacement edges of a flipping cycle
join different canonical paths, so none can reinsert \(e(x,a)\).  Hence
at least one edge of \(P(x)\) is lost. \(\square\)

Equivalently, deleting from \(\mathcal H_m\) every marked tuple touching
one whole \(P(x)\) isolates \(x\) and destroys every spanning tree.  This
is the exact reason that the desired new host must protect only the pivot
interval, not its entire completed complementary path.

## 3. A leaf gives a protected interval of half-path length

Fix a spanning tree \(\mathcal T\) supplied by MNW, and let \(x_*\) be a
leaf from Lemma 1.1.  The path \(P(x_*)\) has \(2m\) incidence edges.  Let
its unique selected marked edge occur in position \(j\), read from one
endpoint.  Reversing the path replaces \(j\) by \(2m+1-j\).  Therefore
one of the two orientations has at least \(m\) initial edges before the
marked edge.

### Lemma 3.1 (restricted-hypergraph survival)

Let \(S\) be any initial edge interval of that orientation with
\(|S|\le m\).  Delete from \(\mathcal H_m\) every marked tuple whose
witness uses an edge in \(S\).  The original \(\mathcal T\) is still a
conflict-free spanning tree of the restricted marked hypergraph.

#### Proof

The only selected tuple meeting \(x_*\) uses its unique marked edge,
which lies outside \(S\).  No other selected tuple touches any edge of
\(P(x_*)\), because it does not contain \(x_*\) in its support.  Hence no
member of \(\mathcal T\) is deleted. \(\square\)

This is an existential protected-connectivity theorem.  It does not say
that deleting an arbitrary interval from an arbitrarily named canonical
path preserves connectivity.  We first choose a leaf of one MNW tree and
then conjugate the whole construction by a coordinate permutation.

## 4. Embed an arbitrary short owner geodesic

The owner-geodesic completion lemma gives a complementary rank-\(m\)
geodesic

\[
 X_0,X_1,\ldots,X_m,\qquad X_m=\Omega\setminus X_0, \tag{4.1}
\]

such that

\[
 X_j\cup X_{j+1}=Y_j\qquad(0\le j\le t).            \tag{4.2}
\]

Its incidence path starts

\[
 X_0,Y_0,X_1,Y_1,\ldots,X_t,Y_t,X_{t+1}.            \tag{4.3}
\]

The desired lift (0.3) occupies edge positions \(2,\ldots,2t+1\).  Under
(0.2), the entire prefix through position \(2t+1\) has length at most
\(m\), so Lemma 3.1 protects it.

Every complementary rank-\(m\) geodesic is a coordinate image of every
other one: map its ordered leaving and entering banks coordinatewise.
Choose the orientation of \(P(x_*)\) from Section 3 and apply a coordinate
permutation of \(\Omega\) sending it to (4.1).  Apply the same permutation
to the complete MNW Hamiltonization.

Remove the retained complement matching from the resulting odd-graph
Hamilton cycle.  This gives the rethreaded spanning path forest \(Q\) in
the incidence graph on ranks \(m,m+1\) of \(\Omega\).  The protected
prefix (4.3) remains in \(Q\).  MNW's Section 6 middle-levels lift places
\(Q\) in the \(z=0\) half and the unchanged complementary MSW forest in
the other half, joining them through the vertical endpoint edges.  The
result is one Hamilton cycle and contains (0.3).  This proves Section 0.

## 5. What rethreading preserves automatically

The rethreaded forest \(Q\) spans the complete incidence graph layers:

\[
 \binom\Omega m\longleftrightarrow\binom\Omega{m+1}.
\]

Every rank-\((m+1)\) vertex has degree two.  Suppressing that shore
therefore gives a Johnson path forest on all rank-\(m\) owners in which
each immediate upper colour occurs exactly once.  Thus rethreading
preserves, without an additional theorem,

1. every owner exactly once;
2. the complete immediate-upper (\(q1\)) palette; and
3. the protected pivot interval from Section 4.

It is free to change the pairing of consecutive immediate-upper colours
at rank-\(m\) owners.  That pairing is precisely the upper-\(q2\) turn
map.

## 6. The MNW moves are genuinely q2-active

The smallest \(\alpha\)-flip already changes the turn map.  In the
canonical \(m=3\) paths, its old path edges are

\[
 \begin{aligned}
 &(100101,100111),\\
 &(100110,110110),\\
 &(110100,110101),
 \end{aligned}                                      \tag{6.1}
\]

and its new cross-edges are

\[
 (100101,110101),\quad
 (100110,100111),\quad
 (110100,110110).                                   \tag{6.2}
\]

At the two internal rank-three vertices, the untouched other neighbours
are \(101101\) and \(101110\).  Hence the two q2 turns change as

\[
 \begin{array}{c|c|c}
 \text{centre}&\text{old turn}&\text{new turn}\\ \hline
 100101&101111&111101\\
 100110&111110&101111.
 \end{array}                                        \tag{6.3}
\]

Thus, at the occurrence-labelled level,

\[
 \{101111,111110\}\longmapsto
 \{111101,101111\}.                                 \tag{6.4}
\]

Appending a Dyck suffix \(v\) preserves the whole calculation:

\[
 \{101111v,111110v\}\longmapsto
 \{111101v,101111v\}.                               \tag{6.5}
\]

The recursive MNW tree contains the connector
\(\alpha(\varnothing)v\) for every
\(v\in\mathcal D_{m-3}\).  These suffix-indexed flip cycles have disjoint
supports.  Therefore the standard construction contains a
Catalan-scale q2-active bank of size

\[
                         \operatorname{Cat}_{m-3}.   \tag{6.6}
\]

There is an important target-level caution.  The newly introduced target
\(111101v\) is already in the canonical q2 image.  In the inverse criterion
for the prefix \(111101\), take the low-height up-step in position two and
the height-three up-step in position four.  The interval between them has
no forbidden height-two/three down-step, and the two ordinal counts are
both one: the height-zero up-step in position one on the left and the
height-three up-step in position six on the right.  A Dyck suffix \(v\),
read from height four, changes none of these data.  Thus

\[
                         111101v
 \quad\text{is canonically present for every }v.     \tag{6.7}
\]

So the explicit \(\alpha\)-bank proves mobility of the occurrence map,
but by itself only moves mass among already represented targets.  It is
not a repair of the certified missing family.

Later selected flips may also alter the other incident edge of one of
these centres, so (6.5) is not by itself a target-level certificate for
the **final** Hamilton cycle.  It proves the exact point needed here: the
canonical q2 map is not invariant under MNW rethreading, and the movable
bank is Catalan-scale rather than bounded.

For comparison, the certified canonical missing family has size
\(\operatorname{Cat}_{m-6}\).  Since

\[
 \frac{\operatorname{Cat}_{m-3}}
      {\operatorname{Cat}_{m-6}}\longrightarrow4^3=64,            \tag{6.8}
\]

there is no *numerical-scale* obstruction to repairing that family with
the available rethreads.  Equations (6.7)--(6.8) show why scale alone is
far from sufficient: the first explicit Catalan bank points at the wrong
target support.  A successful tree must use other patterns or compound
centres at which both incident canonical edges are rethreaded.

## 7. Exact remaining q2 selector

Let \(C=\operatorname{Cat}_m\).  Removing the \(C\) retained closure edges
from an MNW Hamilton cycle gives \(C\) incidence paths.  Exactly

\[
 (m-1)C                                                     \tag{7.1}
\]

rank-\(m\) owners are internal and hence carry a q2 turn.  The target
layer has size

\[
 \binom{2m}{m+2}=\frac{m(m-1)}{m+2}C.                \tag{7.2}
\]

Thus the raw occurrence surplus is

\[
 \frac{2(m-1)}{m+2}C,                               \tag{7.3}
\]

again Catalan-scale.

For a conflict-free spanning tree \(\mathcal T\) avoiding the protected
edge interval, let \(Q_{\mathcal T}\) be its rethreaded incidence forest.
If an internal rank-\(m\) owner \(X\) has its two rank-\((m+1)\)
neighbours \(U^-_{\mathcal T}(X),U^+_{\mathcal T}(X)\), define

\[
 \Gamma_{\mathcal T}(X)
 =U^-_{\mathcal T}(X)\cup U^+_{\mathcal T}(X).       \tag{7.4}
\]

The exact remaining condition is

\[
 \boxed{
 \forall R\in\binom\Omega{m+2}\quad
 \exists X\text{ internal in }Q_{\mathcal T}
 \text{ with }\Gamma_{\mathcal T}(X)=R.}            \tag{7.5}
\]

Accordingly the canonical infinite-family obstruction no longer applies
to the protected-pivot host: its hypothesis that the entire MSW half is
fixed has been removed.  What remains is a genuine colored spanning-tree
theorem:

> choose an MNW conflict-free spanning hypertree, avoiding the protected
> leaf interval, whose induced turn colours satisfy (7.5).

The present theorem proves protected connectivity, q1 exactness,
Catalan-scale q2 mobility, and scalar surplus.  It does not prove (7.5),
global residence, deeper upper rows, or the literal antecedent/compiler.
