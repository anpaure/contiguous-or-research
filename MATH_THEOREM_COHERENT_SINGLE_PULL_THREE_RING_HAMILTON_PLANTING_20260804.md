# One coherent canonical pull plants and Hamiltonizes the complete three-ring

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical topology theorem.  For every
`m>=5`, one all-six-coherent standard Middle-Levels pull realizes the two
phases of the complete common-history three-ring.  A canonical pull spanning
tree can be chosen so that every other pull is vertex-disjoint from the
ring.  Holding out the one ring pull leaves exactly two factor components;
its final toggle gives a Hamilton cycle containing the rethreaded ring.

This supersedes the eighteen-edge open-transport bank on the **bare
owner/factor topology row for `c=3`**.  It does not assert preservation of a
full residence collar, arbitrary-width exterior witnesses, or a common cap.
No computation or search is used.

## 0. Canonical factor input

Put `n=m-1`, so the Middle-Levels graph has ground size

\[
                         2n+1=2m-1
\]

and shores of ranks `n=m-1` and `n+1=m`.

Use the rotational canonical cycle factor `C_n` written with the literal
`f,g` word maps in the fixed-boundary lollipop theorem, and its standard
incidence-hexagon pulls.  This choice is deliberate: the external-stub
calculation below is proved on this same rotational factor, so no
GMN-lexical/MMM occurrence-provenance identification is being assumed.  We
use three proved properties.

1. The standard pull auxiliary multigraph on the components of `C_n` is
   connected, and the published construction supplies a compatible pull
   spanning tree.
2. Standard pull hexagons are alternating component mergers in `C_n`; a
   pull whose complete support is vertex-disjoint from a compatible pull
   forest commutes with that forest.
3. For any prescribed coordinate `q`, there is a compatible pull spanning
   tree `R_q` every one of whose gluing-hexagon vertices contains `q`.
   This is the transformed pull tree used in the fixed-boundary lollipop
   theorem; cyclic rotation moves its distinguished coordinate to `q`
   while preserving `C_n`.

A standard pull label has parenthesis form

\[
                 x=110u0v,
          \qquad y=101u0v,
\tag{0.1}
\]

with `u,v` Dyck.  When `u` is empty, the exact external-stub calculation
gives one common insertion label at all three lower ports and one common
deletion label at all three upper ports.  Such a pull is called
**all-six coherent**.

For every `n>=3` there is a nonloop coherent standard label; for example

\[
 x_*=1100(10)^{n-2},
 \qquad
 y_*=1010(10)^{n-2}.
\tag{0.2}
\]

It is the allowed star-bridge label in the standard pull multigraph.

## 1. The three-ring is exactly one coherent pull

Take the literal nonloop coherent standard pull `g` from (0.2).  Name its
rank-`(m-2)` core `B` and name its three active coordinates
`a_0,a_1,a_2`, so its incidence hexagon is

\[
\begin{array}{lll}
 I_0=B+a_0,&I_1=B+a_1,&I_2=B+a_2,\\
 R_0=B+a_2+a_0,&R_1=B+a_0+a_1,&R_2=B+a_1+a_2,
\end{array}
\tag{1.1}
\]

where `|B|=m-2` and `a_0,a_1,a_2` are distinct outside `B`.  Choose the
cyclic order of these three names so that its old factor matching is

\[
               I_0R_0,\qquad I_1R_1,\qquad I_2R_2.
\tag{1.2}
\]

Its opposite matching is then

\[
               I_0R_1,\qquad I_1R_2,\qquad I_2R_0.
\tag{1.3}
\]

Let `b` be the common insertion coordinate of the three unchanged lower
factor stubs.  Put

\[
                         L_i=B+b+a_i.
\tag{1.4}
\]

The unchanged factor edge at `I_i` is exactly `I_iL_i`.

### Lemma 1.1 (literal ring identification)

At the three lower ports, the old local factor state is

\[
 P^-={I_iL_i,I_iR_i:i\in\mathbb Z_3\},
\tag{1.5}
\]

and the toggled local factor state is

\[
 P^+=\{I_iL_i,I_iR_{i+1}:i\in\mathbb Z_3\}.
\tag{1.6}

These are exactly the two phases of the complete common-history
three-ring.

#### Proof

The old matching in the coherent ECO/standard-pull coordinates is

\[
 L_aU_{ca},\qquad L_bU_{ab},\qquad L_cU_{bc}.
\]

Naming `(a,b,c)=(a_0,a_1,a_2)` gives (1.2).  This is only notation for the
already literal pull `g`; no arbitrary coordinate permutation of the
canonical factor is being invoked.  The opposite alternating matching is
(1.3).  All-six coherence
says that the other factor incidence at every lower port inserts one and
the same coordinate, denoted `b`; those are exactly the three edges in
(1.4).  Combining the unchanged stubs with the two hexagon phases gives
(1.5)--(1.6). \(\square\)

Thus for `c=3` the cyclic head rethread is not merely analogous to a local
pull: it is literally one coherent incidence-hexagon toggle.

## 2. Protecting the ring from the completing pull tree

Let `Z_*` be the six vertices of the coherent ring hexagon together with
the three external owners `L_i`.  Their union uses at most

\[
                         |B|+3+1=m+2
\tag{2.1}

ground coordinates.  Since the ground set has size `2m-1`, for `m>=4`
there is a coordinate

\[
                         q\notin\bigcup Z_*.
\tag{2.2}

Every ring vertex therefore has `q=0`.

Choose the transformed canonical pull spanning tree `R_q` whose every
gluing-hexagon vertex has `q=1`.  Its complete pull supports are
vertex-disjoint from `Z_*`.  In particular, toggling any subset of `R_q`
does not change any edge of either ring phase or any unchanged lower stub.

Let `g` be the coherent pull label in Section 1, and let `K_0,K_1` be its
two distinct canonical factor components.  The label is nonloop by (0.2).
The tree `R_q` has a unique `K_0--K_1` path.  Delete any edge `e` on this
path and put

\[
                         T=(R_q-e)+g.
\tag{2.3}

### Lemma 2.1 (protected spanning-tree replacement)

At the auxiliary-component level, `T` is a spanning tree.  Its physical
pulls are compatible: the pulls in `T-g` are the compatible subfamily
`R_q-e`, and `g` is vertex-disjoint from all of them.  Moreover all pulls in
`T-g` are vertex-disjoint from the complete local ring state
`P^- union P^+`.

#### Proof

Adding `g` to the tree `R_q` creates its unique auxiliary cycle, consisting
of `g` and the `K_0--K_1` path.  Deleting `e` from that path restores a
spanning tree.  The family `R_q-e` inherits compatibility from `R_q`.
Equation (2.2) and the defining property of `R_q` make the complete support
of `g` vertex-disjoint from every pull in `R_q-e`; hence its toggle commutes
with the inherited forest. \(\square\)

## 3. Exact two-component and Hamilton states

### Theorem 3.1 (coherent single-pull three-ring Hamilton planting)

For every `m>=5`, `ML_m` has a spanning two-factor `F^-` with exactly two
components which contains the complete ring phase `P^-`.  Replacing the
three `R`-edges in (1.2) by those in (1.3) gives a Hamilton cycle `F^+`
containing the complete rethreaded phase `P^+`.

Both states use the same physical vertex set and no extra source position.

#### Proof

Start from `C_n` and toggle every pull in `T-g=R_q-e`.  This is a spanning
forest of the canonical auxiliary graph with exactly two components:
deleting one edge from a spanning tree leaves two.  Tree compatibility
therefore gives a spanning two-factor `F^-` with exactly two physical
components.

By Lemma 2.1, all these toggles are vertex-disjoint from the ring.  Hence
`F^-` still contains (1.5) literally.

Now toggle `g`.  The full label set becomes the pull spanning tree `T`, so
tree compatibility gives one Hamilton cycle `F^+`.  Lemma 1.1 identifies
the local change as (1.5) to (1.6), while every `L_i` edge is untouched.
No vertex or source position is added. \(\square\)

### Corollary 3.2 (the topology remainder for `c=3` is closed)

On the bare Middle-Levels owner/factor row, a three-ring needs neither the
eighteen-edge external-pair transport bank nor a thirteen-component strict
ternary hypertree.  One coherent standard pull gives the stronger state

\[
 \boxed{
   2\text{ components with }P^-
   \quad\xrightarrow{\text{one zero-length-charge }C_6}\quad
   1\text{ Hamilton component with }P^+.
 }
\tag{3.1}

The old eighteen-edge theorem remains useful when a topology packet must
carry its particular external-pair transport endpoints.  The present result
shows that those endpoints are not intrinsically required for the
three-ring's factor topology.

### Corollary 3.3 (common-history deck interface)

Attach the same ordered depth-`d` history to the three hinges in (1.5).
The change to (1.6) is exactly the cyclic common-history rethread.  Hence
the complete strict-lower interval deck, and in particular every interval
of width at most `d`, is transported with zero deletion number by the
common-history ring theorem.

This corollary is local.  The completing pull tree was selected only to be
vertex-disjoint from the ring vertices; no global residence, arbitrary
upper-deck, occurrence-router, or common-cap property is asserted.

## 4. Why the construction does not contradict the strict-hypertree count

One canonical pull is binary at component level: two of its old hexagon
edges lie in one canonical factor component and the third lies in the other.
After toggling `R_q-e`, those two component blocks remain distinct and the
ring pull joins them.  Thus the occurrence component-incidence multigraph
has one right node with a repeated left incidence, not one strict ternary
node.

The thirteen-component bound for six open transport hexagons counts a
different realization with six ternary switches of capacity two each.  The
single coherent pull realization has one binary switch of capacity one.  It
reaches Hamiltonicity because all other canonical pull-tree edges have
already been toggled.

## 5. Self-audit

1. The active hexagon core has size `m-2`; its three lower ports and three
   upper ports have the correct ranks `m-1,m`.
2. The old matching in (1.2) is exactly the predecessor matching `R_i`, and
   the opposite matching in (1.3) is exactly the successor matching
   `R_(i+1)`.
3. All-six coherence is used only for the three unchanged lower stubs; it
   supplies one common inserted coordinate `b`, giving the exact `L_i` bank.
4. The explicit `u=empty` star-bridge label is nonloop for `n>=3`.
5. The local ring uses at most `m+2` coordinates, leaving an absent
   coordinate `q` for `m>=4`.
6. Every completing pull vertex has `q=1`, while every local ring vertex
   has `q=0`; this is vertex-disjointness, stronger than edge-disjointness.
7. Replacing one edge on the unique auxiliary-tree path by `g` is ordinary
   graphic basis exchange, so `T` is a spanning tree.
8. `R_q-e` has exactly two auxiliary components.  Tree compatibility, not
   a generic component heuristic, gives exactly two physical factor cycles.
9. The theorem closes only the bare topology and local strict-lower-deck
   rows.  No unlisted global guard is inferred.

## 6. Dependencies

| role | file |
|---|---|
| coherent standard-pull criterion and explicit `u=empty` label | `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md` |
| transformed pull tree with an arbitrary distinguished `1` coordinate | `MATH_THEOREM_ODD_MIDDLE_LEVELS_FIXED_BOUNDARY_LOLLIPOP_EXISTENCE_20260802.md` |
| standard pull edge-disjointness and local external-stub table | `MATH_THEOREM_ORDERED_PORTAL_DIRECT_PULL_ZERO_DENSITY_AND_STAR_BRIDGE_20260801.md` |
| exact three-ring phases and short-deck invariance | `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md` |
| six-open-hex comparison and thirteen-component capacity | `MATH_THEOREM_OPEN_HEX_PAIR_TRANSPORT_AND_FIXED_RING_PLANTING_20260804.md` |
