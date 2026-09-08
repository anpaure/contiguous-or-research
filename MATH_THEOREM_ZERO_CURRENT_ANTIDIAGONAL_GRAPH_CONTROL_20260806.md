# Zero-current antidiagonal edges give full independent row control

**Date:** 2026-08-06  
**Method:** pure group theory  
**Status:** unconditional abstract theorem, with an exact conditional
physical corollary.  It does not assert that the required zero-current
macros have already been realized by the anchored `D_3` pentagon.

## 1. Antidiagonal edge actions

Let `G` be a perfect group and let `Gamma` be a graph on a finite row set
`V`.  For an oriented edge `u->v` and `g in G`, put

\[
 A_{uv}(g)_x=
 \begin{cases}
 g,&x=u,\\
 g^{-1},&x=v,\\
 1,&x\notin\{u,v\}.
 \end{cases}                                                \tag{1.1}
\]

Reversing the orientation replaces `g` by `g^{-1}`, so the generated
subgroup depends only on the underlying graph.

### Theorem 1.1 (connected antidiagonal generation)

If `Gamma` is connected and has at least three vertices, then

\[
 \left\langle A_{uv}(g):uv\in E(\Gamma),\ g\in G\right\rangle
 =G^V.                                                       \tag{1.2}
\]

#### Proof

Choose a length-two path `u-v-w`.  The two actions
`A_uv(g)` and `A_vw(h)` have disjoint supports except at `v`.  Their
commutator is therefore supported only at `v`, where it is

\[
                         [g^{-1},h]                           \tag{1.3}
\]

up to the harmless choice of commutator convention.  Since `G` is
perfect, its commutators generate `G`; hence every isolated action at `v`
belongs to the generated subgroup.

If isolated actions are available at `v` and `xv` is an edge, multiply
`A_xv(g)` by the isolated action `g` at `v`.  The two `v`-coordinates
cancel and leave `g` isolated at `x`.  Propagating along a spanning tree
isolates arbitrary elements at every vertex.  These coordinate copies
generate `G^V`.  \(\square\)

For the shortest-wreath application, `G=A_(2m+1)`, which is perfect for
`2m+1>=5`.

## 2. How an antidiagonal macro arises from two phase edges

Let `e=uv` and `f=uw` be companion edges in two guarded phases, sharing
the tracked row `u`.  Suppose that, after transport to one common reference
frame,

1. the first phase supplies the diagonal action `D_e(g)`;
2. the second supplies `D_f(g^{-1})`; and
3. the two literal moves have opposite **complete** protected resource
   currents, including every q1, all-width boundary, provider, endpoint,
   and common-cap occurrence coordinate.

Then their paired macro has zero complete current and row action

\[
             D_{uv}(g)D_{uw}(g^{-1})=A_{vw}(g),         \tag{2.1}
\]

where the common `u`-coordinate cancels.  Notice that this is an
antidiagonal action on the two *unshared* endpoints.

The equality in item 3 must be literal after the occurrence transport.  An
abstract relabelling of the two currents is insufficient.

### Corollary 2.1 (zero-current phase-difference control)

Suppose finitely many pairs of phase companion edges satisfy the three
conditions above, and let `Delta` be the graph on tracked rows whose edges
are the resulting unshared endpoint pairs.  If `Delta` is connected and
has at least three vertices, then zero-complete-current macros generate
the full independent row action `G^V`.

#### Proof

Each physical macro realizes one generator (1.1) without changing the
complete protected resource ledger.  Apply Theorem 1.1.  Every product and
commutator of these macros remains zero-current because each factor is a
literal guarded self-map of the same complete exact fibre.  \(\square\)

## 3. Relation to the anchored `D_3` pentagon

The suffix-stable companion matchings in the two pentagon phases are

\[
 M^- =\{12,54\},\qquad M^+=\{14,32\},                 \tag{3.1}
\]

whose union is the connected path `3-2-1-4-5`.  Equation (3.1) closes the
abstract phase-switched companion-connectivity row.

The especially promising pair `12` in the negative phase and `14` in the
positive phase shares row `1`; in the audited tensor alignments the two
edges use the same displayed common blocks

\[
                         X=(V,\infty),\qquad Y=(1,U,6). \tag{3.2}
\]

If their complete literal currents are opposite under the pentagon
transport, (2.1) gives the zero-current antidiagonal edge `2-4`.
Analogous phase-edge pairings must be audited.  Neither (3.2) nor equality
of abstract tensor types alone proves the literal current identity required
in item 3.

There is, however, an exact parity warning.  The four possible cross-phase
edge pairs have the following unshared endpoints:

\[
\begin{array}{c|c}
(12,14)&24\\
(12,32)&13\\
(54,14)&51\\
(54,32)&\text{disjoint}.
\end{array}                                                \tag{3.3}
\]

The first three derived edges lie in the two classes

\[
                         \{2,4\},\qquad\{1,3,5\}.       \tag{3.4}
\]

For the disjoint pair, if the same `g` identifies the two currents, its
row action factors as

\[
 D_{54}(g)D_{32}(g^{-1})
       =A_{24}(g^{-1})A_{53}(g),                         \tag{3.5}
\]

which again stays inside the two classes (3.4).  Thus the two displayed
phase matchings alone cannot produce a connected antidiagonal graph by
pairwise phase-current cancellation.  This is the distance-two parity
partition of the path `3-2-1-4-5`.

Thus the next exact test is smaller than a general orbit router:

> **Pentagon phase-difference test.**  Determine all cross-phase pairs in
> `M^- x M^+` whose complete occurrence-labelled currents are opposite,
> and then supply one additional zero-current action crossing the partition
> (3.4), for example from a third suffix-compatible phase or one routed
> marked generator.

If that augmented test is positive, Corollary 2.1 supplies guarded
zero-current row control directly.  The important reduction is that a
general endpoint-halo development is then needed for at most one
parity-bridging generator rather than for the whole control subsystem.  A
terminal common-cap matching would still remain.
