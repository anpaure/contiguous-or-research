# Self-audit: core-pinned reservoir and coordinate-wall pull completion

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_CORE_PINNED_THREE_RING_RESERVOIR_AND_COORDINATE_WALL_PULL_COMPLETION_20260804.md`  
**Method:** line-by-line symbolic audit; no computation or search  
**Verdict:** GO at the stated physical-factor scope.  The audit caught and
corrected two overstatements before freeze: an arbitrary additional pull
catalogue is not automatically compatible with the opposite-half tree, and
physical vertex separation does not by itself preserve a typed cap or
global occurrence order.

## 1. Pinned low paths

For trace size `t` put `h=m-t`.  After removing the pinned coordinate from
`K`, the available linear bank has size `m-2`.  A window of size `h-1`
started at each `j=0,...,t-1` ends at

\[
 (t-1)+(h-2)=m-3,
\]

the last legal index.  Every owner has size

\[
 t+1+(h-1)=m.
\]

Successive windows exchange exactly one coordinate.  Their union has size
`m-2`, hence the complete path union is `K union T`.  An internal window
coordinate has run length `h-1`; the cutoff `t<=m-d-2` is exactly
equivalent to `h-1>=d+1`.  The old cutoff `m-d-1` would be one short after
pinning, so moving that one layer to the high tail is necessary.

All owner, lower-q1, and upper-q1 values contain the pin.  Their respective
ranks are `m,m-1,m+1`, and their starting indices make them simple.

## 2. Pinned high paths

For `t=m-h`, the proposed partition has size

\[
 (h+1)+2(t-1)=2m-h-1=|K\cup T|.
\]

Every owner in the monotone geodesic has size

\[
 (h+1)+(t-1)=m,
\]

contains the pinned coordinate, and the first and last owners have union
`K union T`.  Under the stabilizer of the pin, the relevant resource
layers are transitive.  There are respectively

\[
 \binom{N-1}{m-1},\qquad
 \binom{N-1}{m-2},\qquad
 \binom{N-1}{m}
\]

possible pinned owners, lower colours, and upper colours.  Since the path
uses `t,t-1,t-1` distinct resources, the three displayed hitting
probabilities are exact.

The enlarged high range has `h<=d+1`; its trace count remains
`2^{o(m)}`.  All denominators remain `2^{2m-o(m)}`, whereas the earlier
bank has `2^{m+o(m)}` resources.  The greedy collision probability tends
to zero.  Thus pinning does not change the asymptotic reservoir size.

## 3. Coordinate and ring quantifiers

The proof-safe order is:

1. choose one nonloop coherent pull `g_0` in the uncomplemented canonical
   factor;
2. choose `q` outside its complete local hexagon-plus-stub support;
3. choose the fixed-boundary compatible tree `R_q` whose every pull vertex
   has `q=1`;
4. complement the entire factor, tree, and pull `g_0`.

Then `R_q^0` and `g=kappa(g_0)` lie on the same complemented base factor.
Every tree-pull vertex has `q=0`, while every ring vertex and stub has
`q=1`.  Since the complemented lower ports all contain `q`, their common
intersection—the new ring core `B`—contains `q`.  This aligns exactly with
the pinned-reservoir hypothesis.

The theorem does not claim that an arbitrarily prescribed ring embeds in
this host.  Ring, pin, and reservoir are chosen in the displayed order.

## 4. Auxiliary-graph scope

The fixed-boundary theorem guarantees the compatible tree `R_q^0`; the
coherent-ring theorem guarantees compatibility after adjoining `g` and
performing one basis exchange.  It does not guarantee that every other
canonical pull can be adjoined while preserving pairwise support
disjointness and the rule “every graphic forest is tree-compatible.”

Accordingly, Theorem 4.2 now explicitly assumes a fixed
pairwise-support-disjoint tree-compatible host `H` containing
`R_q^0 union {g}`.  Forced labels `A_D` are defined only in this same `H`.
No cross-host identification is made.

For the guaranteed minimal host `R_q^0 union {g}`, a protected `q=1` edge
outside the base factor cannot be installed by a `q=0` tree pull.  Thus a
nontrivial forced phase needs the stated compatible-host extension; this is
not hidden by the theorem.

## 5. Basis-extension check

Let `J=A_D union {g}`.  If `J` is a forest and `R_q^0` is a spanning tree,
then contraction of `J` leaves the image of `R_q^0` connected.  A spanning
tree of that image lifts to

\[
                         J\subseteq T\subseteq J\cup R_q^0.
\]

Every completion label in `T-J` has all physical vertices in the `q=0`
half, while every protected edge has both endpoints in the `q=1` half.
Therefore no completion label lies in the protected old-edge deletion set
`B_D`.  Accessibility installs every protected nonfactor edge through its
unique forced label; phase consistency preserves protected factor edges.
The explicit condition `D cap Z_g=emptyset` leaves the ring phases free.

Removing `g` from the spanning tree leaves exactly two auxiliary
components; tree compatibility gives exactly two factor cycles.  Restoring
`g` gives one Hamilton cycle.  Thus the residual physical cographic cut is
indeed automatic.

## 6. Typed and residence scope

The original draft incorrectly suggested that physical separation alone
preserves typed occurrence/cap data.  It does not: a remote switch can
change global order, occurrence addresses, or interval routes without
touching a named incidence edge.  The corrected theorem is physical.  A
typed conclusion requires the additional premise that the fixed typed
state is invariant under every opposite-half completion pull.

Likewise, opposite-half pulls change no edge incident with a `q=1` vertex.
For either fixed ring phase they preserve the maximal positive `q`-run
lengths, so they cannot repair a short pinned-coordinate run.  Global
residence must already be supplied by the forced phase/base factor and the
chosen ring phase.

## 7. Exact surviving open rows

After the theorem, the physical pull-host problem for the pinned bank is:

1. prove accessibility in one compatible host containing the opposite-half
   tree;
2. prove `A_D union {g}` is a graphic forest.

The residual cographic row is gone.  Still open are the compatible-host
extension itself, global residence, ambient upper completeness, one global
antecedent, guard-pruned residual Hall, typed common-cap invariance, and
regeneration.

