# Cross-wreath fusion is a `q`-safe alternating-flip hypertree; two-way one-cut fusion is impossible

**Date:** 2026-08-13  
**Status:** unconditional exact reduction and local minimality theorem.  It turns the
remaining MSW middle/lower/residence fusion problem into a conflict-free alternating
hexagon/octagon hypertree with explicit collar tests.  It does not construct that
hypertree and does not repair the canonical upper-deck defect.

## 0. Outcome

Put

\[
 k=2R-1,qquad
 \mathcal O={ [k]\choose R},qquad
 \mathcal L={ [k]\choose R-1}.                         \tag{0.1}
\]

Let `\mathcal B` be the bipartite containment graph between `\mathcal O` and
`\mathcal L`.  Subdividing every Johnson edge by its rank-`(R-1)` intersection turns
the exact MSW owner/lower cycle factor into a spanning two-factor `F` of `\mathcal B`.
It has

\[
                         C=\operatorname {Cat}_{R-1}     \tag{0.2}
\]

components, each with `k` owner vertices and `k` lower vertices.

The containment graph has no four-cycle.  Hence one cannot cut one incidence edge in
each of two factor components and reconnect them by two cross incidences.  Equivalently,
there is no palette-exact two-way one-cut fusion.  The smallest alternating flipping
cycle is a `C_6`, and it can merge three factor components.

More generally, let `\mathscr A` be a conflict-free family of `F`-alternating cycles.
If its component--trade incidence graph is a tree, then toggling all cycles merges the
MSW components into one spanning cycle.  Owner and lower exactness are automatic
because the vertex set of `\mathcal B` never changes.

The remaining residence condition is completely local after imposing separation.
If the changed projected transitions cut every original MSW component into arcs of at
least `q` transitions, then every `q`-window meets at most one new seam.  The output is
`q`-biresident if and only if every new seam passes the exact two-sided transition-
collar test.  Thus a `q`-safe conflict-free flip hypertree would close the one-cycle
middle/lower/residence gate without any hypergraph nibble.

## 1. The exact owner/lower incidence factor

For a Johnson edge `AB` on rank-`R` owners, its label is

\[
                         L=A\cap B\in\mathcal L.          \tag{1.1}
\]

Replace `AB` by the length-two incidence path `A-L-B`.  Since the MSW owner cycles
partition `\mathcal O` and their edge labels partition `\mathcal L`, the resulting
graph `F` is a spanning two-factor of `\mathcal B`.  Conversely, suppressing every
lower vertex of any spanning two-factor of `\mathcal B` gives an owner two-factor
whose owners and immediate-lower labels are separately exact.

If a lower vertex `L` has factor neighbours

\[
                         A=L\cup\{a\},\qquad
                         B=L\cup\{b\},                    \tag{1.2}
\]

then its projected transition support is

\[
                         E_F(L)=A\triangle B=\{a,b\}.     \tag{1.3}
\]

For a cyclic projected owner trace, `q`-biresidence is equivalent to every `q`
consecutive transition supports being pairwise coordinate-disjoint.

## 2. Four-cycle minimality

### Lemma 2.1 (`\mathcal B` is `C_4`-free)

Two distinct owners cannot have two distinct common lower neighbours.  Consequently
`\mathcal B` contains no four-cycle.

#### Proof

Suppose distinct `L,M in \mathcal L` are both contained in owners `A,B`.  If
`|L union M|>R`, no rank-`R` owner contains both.  Otherwise distinctness forces
`|L union M|=R`, and every rank-`R` owner containing both is exactly `L union M`.
Thus `A=B`, a contradiction.  \(\square\)

### Corollary 2.2 (no two-way one-cut fusion)

There is no alternating `C_4` whose two factor edges lie in two distinct components of
`F`.  Hence no operation which deletes one incidence edge in each of two components
and adds two cross incidences can merge them while retaining every owner and lower
resource exactly once.

The same obstruction in the projected owner graph is as follows.  Let old edges
`A_0A_1` and `B_0B_1` have distinct labels `L,M`.  A degree-preserving two-switch
would add either `A_0B_1,B_0A_1` or `A_0B_0,A_1B_1`.  If the two new edge labels were
again `L,M`, two distinct endpoints would both contain `L union M` and hence coincide.
Thus exact label preservation is impossible.

This is a local minimality result, not a no-go for every two-wreath multi-cut trade.
Cutting either wreath more than once lies outside the corollary.

### Lemma 2.3 (hexagons exist)

Let `K` have size `R-2` and choose distinct coordinates `a,b,c` outside `K`.  Then

\[
\begin{aligned}
 A_{ab}&=K\cup\{a,b\},& L_b&=K\cup\{b\},\\
 A_{bc}&=K\cup\{b,c\},& L_c&=K\cup\{c\},\\
 A_{ca}&=K\cup\{c,a\},& L_a&=K\cup\{a\}
\end{aligned}                                           \tag{2.1}
\]

form the incidence hexagon

\[
 A_{ab},L_b,A_{bc},L_c,A_{ca},L_a,A_{ab}.               \tag{2.2}
\]

Thus `C_6` is the first geometrically possible alternating trade.  Whether its three
alternating old incidences occur in three suitable MSW components is a separate
factor-specific selection question.

## 3. One alternating trade

Let `Q` be a `2h`-cycle in `\mathcal B`, alternating between `h` edges of `F` and
`h` edges outside `F`.  Then

\[
                         F'=F\triangle Q                 \tag{3.1}
\]

is again a spanning two-factor: at every vertex of `Q`, one old incidence is removed
and one new incidence is added.

### Lemma 3.1 (distinct-component merge)

If the `h` old edges of `Q` belong to `h` distinct components of `F`, then `F'` replaces
those `h` components by one component and leaves every other component unchanged.

#### Proof

Delete the `h` old incidences.  Each affected factor cycle becomes one path.  The `h`
new incidences appear cyclically around `Q` and join the terminal end of each path to
the initial end of the next.  Their union is one cycle through all `h` paths.  \(\square\)

In particular, an alternating hexagon can merge three MSW components and reduces the
component count by two.  An alternating octagon can merge four and reduces it by
three.

## 4. Conflict-free flip hypertrees

Call a family `\mathscr A` of `F`-alternating cycles **conflict-free** when its cycles
are vertex-disjoint.  This is stronger than necessary but makes all toggles commute.
For every `Q in \mathscr A`, suppose its old edges lie in distinct original components
of `F`.  Form the bipartite incidence graph `J(\mathscr A)` whose left vertices are
the components of `F`, whose right vertices are the trades `Q`, and where a component
is incident with a trade when that trade removes one of its edges.

### Theorem 4.1 (flip-hypertree Hamiltonization)

If `J(\mathscr A)` is a tree spanning all `C` original MSW components, then

\[
                         H=F\triangle
                         \bigtriangleup_{Q\in\mathscr A}Q \tag{4.1}
\]

is a Hamilton cycle of `\mathcal B`.

Equivalently, if the trade meeting `h_Q` components is assigned weight `h_Q-1`, the
tree identity is

\[
                         \sum_{Q\in\mathscr A}(h_Q-1)=C-1. \tag{4.2}
\]

#### Proof

The conflict-free symmetric difference is a spanning two-factor.  Root the incidence
tree at one component node.  Choose a trade node farthest from the root; all of its
nonparent component neighbours are leaves.  Toggle such trades from the outside
toward the root.  At its turn, each trade joins the current cycle containing its
parent component to the `h_Q-1` mutually distinct current cycles in its child
subtrees.  Lemma 3.1 reduces the number by `h_Q-1`.  Induction leaves one component.
A connected finite
two-regular spanning graph is a Hamilton cycle.  Equation (4.2) is the edge count of
the bipartite tree:

\[
 \sum_Qh_Q=|E(J)|=C+|\mathscr A|-1.                     \tag{4.3}
\]

Subtract `|\mathscr A|`.  \(\square\)

The theorem accommodates the `C_6/C_8` mixture used in published MSW/MNW
Hamiltonizations.  It says nothing yet about residence.

## 5. Exact `q`-collar law

Project any spanning two-factor of `\mathcal B` to its owner cycles by suppressing the
lower vertices.  A lower vertex at which the paired owner neighbours change under
(4.1) is a **new seam**.  Its new transition support is still given by (1.3), with the
new pair of owner neighbours.

For one new seam `e`, list the preceding and following projected transition supports
as

\[
 E^-_{q-1},\ldots,E^-_1, E_e, E^+_1,\ldots,E^+_{q-1}.  \tag{5.1}
\]

Call the seam **`q`-legal** when every consecutive sublist of `q` supports in (5.1)
is pairwise coordinate-disjoint.

### Theorem 5.1 (separated seams are exactly locally checkable)

Assume every inherited path segment between consecutive new seams of `H` contains at
least `q` projected transitions.  Then the projected owner Hamilton cycle is
`q`-biresident if and only if every new seam is `q`-legal.

#### Proof

The separation hypothesis makes every `q`-transition window meet at most one new
seam.  A window meeting none is an unchanged window of an MSW component and is safe.
A window meeting one is one of the sublists tested in (5.1).  The transition-support
criterion for `q`-biresidence gives both directions.  \(\square\)

It is not enough that the new support `E_e` avoid the two collars separately.  A
coordinate in a retained left support and a retained right support can also repeat
inside a crossing `q`-window.  Definition (5.1) is the full exact test.

### Corollary 5.2 (per-wreath port capacity)

If one original MSW component supplies `r` changed sites whose cyclic projected gaps
are all at least `q`, then

\[
                         r\le\left\lfloor{k\over q}\right\rfloor. \tag{5.2}
\]

At `q=Theta(sqrt R)` this is `Theta(sqrt R)`.  Thus a bounded-degree flip hypertree
fits the raw port capacity, whereas a Catalan-degree star cannot.

## 6. Exact surviving theorem target

Combining Theorems 4.1 and 5.1 gives the following sufficient statement.

> **`q`-safe MSW flip-hypertree target.**  Select a conflict-free family of
> `F`-alternating `C_6` and `C_8` trades whose component--trade incidence graph is a
> spanning tree, whose sites have inherited gaps at least `q`, and whose every new
> seam passes (5.1).

Such a selection produces one exact owner/lower Hamilton cycle with `q`-biresidence.
Its maximal `q`-antecedent then gives one literal source chronology realizing every
owner and the complete consecutive-intersection fan, including the exact immediate-
lower row.

This target is strictly stronger than the published connectivity theorem.  An
ordinary MSW/MNW flipping-cycle spanning tree ensures (4.1) is Hamiltonian, but does
not by itself impose the mesoscopic collar equations (5.1).  Conversely, pairwise
collar-compatible trades without the incidence-tree condition need not give one cycle.

The upper/source occurrence bank is an additional current constraint.  A changed seam
alters all source intervals crossing it; exact upper preservation requires the
simultaneous multiset/ticket identities of the long-aperture seam-current theorem, not
merely rank correctness or (5.1).  The canonical MSW upper-deck holes also survive if
one only cuts and restores old edges.  Hence the theorem isolates, but does not hide,
the later upper/compiler gate.

## 7. Final boundary

The generic augmented matching problem is gone.  The exact middle/lower/residence
fusion problem is now a bounded-arity, Catalan-scale selection theorem:

\[
 \boxed{\text{find a conflict-free spanning `C_6/C_8` flip hypertree with legal
 `q`-collars.}}                                         \tag{7.1}
\]

No two-way one-cut shortcut exists because `\mathcal B` is `C_4`-free.  A positive
proof must exploit the actual MSW/MNW flip catalogue, plant additional safe hexagons
or octagons, or allow controlled multi-cut trades.
