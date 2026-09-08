# The entire two-chip hook row collapses to at most two q2-exact rails

**Date:** 2026-08-05  
**Method:** marked double-zero ports, path-contour permutations, and bounded
shape-local packing; no search  
**Status:** **WITHDRAWN; DO NOT CITE THEOREM 5.1.**  The undirected marked
port list is correct, but Sections 2--5 failed to couple two orientations:
reflecting a `+d` port to `-d` also reverses the order of the two child
shores, and the directed PBBS time order on the promoted parent must be
computed from its action-angle velocity rather than identified without
proof with the geometric vacancy-slot order.  Under the coherent sign
pattern the first symbolic check gives the inverse contour order.  A
possible repair using the inverse clean-C6 reconnection requires a literal
return-map and velocity audit and is not asserted here.  Section 1 and the
abstract path-contour calculation in Lemma 2.1 remain valid separately.

## 1. The two-chip angle path

Put `h=m-2`, `q=2h-1`, and `E=h-1`.  The hook action `(h,1^2)` has exactly
the components

\[
                         C_0,C_1,\ldots,C_E,
\tag{1.1}
\]

where `C_0` has both chips in one vacancy and `C_d` has two singleton chips
at shorter cyclic distance `d`.  Its adjacent-transfer graph is the path

\[
                         C_0-C_1-\cdots-C_E.
\tag{1.2}

Every edge `e_d=C_(d-1)C_d`, `1<=d<=E`, has two reflected rooted
leaf-plucking realizations.  Their promoted shore is the unique one-chip
hook component `S` of action `(h+1,1)`.  In the length-`2h+1` vacancy
circle of `S`, the two marked `00` ports occur, up to one common additive
offset, at positions

\[
                         +d\quad\hbox{and}\quad-d.
\tag{1.3}
\]

Indeed, delete the transferred chip.  The remaining chip and the chosen
cut have cyclic separation `d`; inserting the promoted `00` pair at that
cut gives (1.3).  Reflection reverses the separation.  The marked-port
inverse theorem shows that these are distinct literal parent ports.

## 2. The contour permutation of the path

Bipartition the vertices of (1.2) by parity.  On the edge labels
`1,...,E`, the cyclic cut orders at even and odd internal vertices are

\[
 \alpha=(2\ 3)(4\ 5)\cdots,
 \qquad
 \beta=(1\ 2)(3\ 4)\cdots.
\tag{2.1}
\]

Put `pi=beta alpha`, with the rightmost permutation acting first.

### Lemma 2.1

`pi` is the `E`-cycle whose cyclic order is

\[
 1,2,4,6,\ldots,2\lfloor E/2\rfloor,
 \quad\text{then the positive odd labels in decreasing order}.
\tag{2.2}

#### Proof

The map sends `1` to `2`; every nonterminal even label to the next even
label; the largest even label to the largest odd label; and every odd label
at least three to the preceding odd label.  The last label `3` returns to
`1`.  This is exactly (2.2).  `square`

Choose the `+d` parent port in (1.3) for `d=1` and every even `d`, and the
`-d` port for every odd `d>=3`.  In the positive orientation around `S`,
the positive positions occur in increasing order and the negative positions
in decreasing absolute value.  Their cyclic order is therefore precisely
the cycle (2.2).

## 3. Simultaneous physical separation

The selected parent ports are distinct rooted shape positions on `S`.
The hook action-angle evolution rotates the vacancy slots by one, so this
vacancy order is the literal rooted-shape order along `S`.

One connector's protected support meets a given old component only on its
changed factor edge and the bounded predecessor/companion halo used by the
q2 identity.  Its projection to the rooted-shape cycle consequently has
bounded size and bounded diameter, independently of `m`.  Because the
chosen ports form a subset of one cyclic list, a fixed connector has
shape-overlap with only `O(1)` other parent supports.  On a child component
`C_d`, it can overlap only the connector on the other incident path edge.

For two potentially overlapping protected supports, freeness of ground
rotation on rank-`m` states excludes at most `B^2` relative rotations, with
`B=12`.  The resulting conflict graph has bounded maximum degree.  Greedily
choose one of the `n=2m+1` ground rotations for each connector.  For all
sufficiently large `m`, a legal rotation remains at every step.  Hence all
`E` clean C6 supports can be made pairwise vertex-disjoint while retaining
the parent-port cyclic order (2.2).

## 4. Tree-contour reconnection lemma

We use the following elementary permutation fact.

### Lemma 4.1

Let a bipartite plane tree have edge-rotation permutations `alpha,beta` on
its two shores, and put `pi=beta alpha`.  Then `pi` is one cycle.  Suppose
one coherently oriented clean C6 is placed on every tree edge, with its
first two old shores on the edge's endpoints and its third old shore on a
single additional cycle.  If the third-shore cuts have cyclic order
`gamma`, then the cycles after all switches are counted by the cycles of

\[
                         \gamma\beta\alpha.
\tag{4.1}

#### Proof

The product `beta alpha` is the usual one-face contour permutation of a
plane tree.  This may also be proved by deleting a leaf: reinserting its
edge inserts one new symbol next to its incident edge in the unique contour
cycle.

Follow a directed path fragment through three consecutive C6
reconnections.  It moves successively to the next cut at its first child
shore, its second child shore, and the additional cycle.  On the tree-edge
label this is exactly `gamma beta alpha`.  Returning to the same shore
after three steps gives a bijection between final factor cycles and cycles
of (4.1).  `square`

## 5. Exact two-chip collapse

For the path (1.2), Section 2 gives `pi=beta alpha`, and the chosen parent
ports give `gamma=pi`.  Lemma 4.1 therefore reduces the final component
permutation to

\[
                         \pi^2.
\tag{5.1}

Since `pi` is an `E`-cycle, `pi^2` has exactly

\[
                         \gcd(E,2)\le2
\tag{5.2}

cycles.

### Theorem 5.1

For all sufficiently large `m`, the unique action-`(m-1,1)` PBBS component
and every action-`(m-2,1^2)` angle torus admit a simultaneous family of
selected, common-pivot, q2-neutral leaf-plucking switches whose result has
one cycle if `m-3` is odd and two cycles if `m-3` is even.

Every local q1/q2 identity composes exactly because the protected supports
are disjoint.  In particular, the parity residue in a purely loose
two-chip hyperstar is not a genuine topological obstruction: the contour-
ordered nonloose tree absorbs the complete row with at most two rails.

## 6. Scope

This theorem closes the first nontrivial all-angle hook row.  It proves that
the promoted-port order can equal the child-tree contour order in a literal
family, rather than assuming arbitrary port reorderability.

For `b>=3`, a fixed promoted parent can contain several chips and several
marked `00` ports.  The remaining all-hook theorem is to choose a spanning
tree in each adjacent-transfer necklace graph whose contour order agrees,
simultaneously, with the inherited orders of all promoted-parent port
fibres.  Connectivity and marked-port injectivity alone do not imply that
order compatibility.

No splice with the already switched rigid/named block, and no q3,
residence, arbitrary-upper, or common-cap claim, is included.
