# Independent audit: core-pinned three-ring reservoir and coordinate-wall pull completion

**Date:** 2026-08-04  
**Method:** independent pure-mathematical proof replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_CORE_PINNED_THREE_RING_RESERVOIR_AND_COORDINATE_WALL_PULL_COMPLETION_20260804.md`  
**Audited SHA-256:**
`ab028b4e04f60adf9df8b7e9f84cadcae62102eb6d767c6cbba3c3e12af72057`

## Verdict

**INDEPENDENT GO at the stated physical-factor scope.**  The core-pinned
reservoir, the complement-conjugate coordinate wall, and the graphic basis
extension are correct.  No source correction was required.  The theorem
does not prove accessibility of the bank, forced-label independence, a
jointly compatible enlarged host, typed/common-cap invariance, global
residence, or an ambient upper-complete carrier.

## 1. Pinned reservoir arithmetic

For a low trace of size `t`, put `h=m-t`.  Since `|K-{q_0}|=m-2`, the
windows

\[
 W_{T,j}=\{k_j,\ldots,k_{j+h-2}\},\qquad 0\le j<t,
\]

have size `h-1`, and the last index used is

\[
 (t-1)+(h-2)=m-3.
\]

Thus there is no wrap.  Every owner has size
`t+1+(h-1)=m`; consecutive owners exchange one coordinate; and the union
of all windows is `K-{q_0}`, so the complete path union is `K union T`.
An internal window-coordinate run has length `h-1`.  The corrected cutoff
`t<=m-d-2` is exactly `h-1>=d+1`.  Moving the single layer
`t=m-d-1` to the high construction is therefore necessary and sufficient
for pinning.

For a high trace, the partition sizes satisfy

\[
 (h+1)+2(t-1)=2m-h-1=|K\cup T|.
\]

Every geodesic owner has rank `m` and contains `q_0`.  Conditional on
`q_0 in C`, stabilizer symmetry is transitive on the pinned owner,
lower-colour, and upper-colour layers.  Hence the hitting denominators are
respectively

\[
 \binom{N-1}{m-1},\qquad \binom{N-1}{m-2},\qquad
 \binom{N-1}{m},
\]

and the numerators `t,t-1,t-1` are exact.  For
`h<=d+1=O(sqrt(m))`, all denominators are `2^(2m-o(m))`, while all
previously forbidden resources number `2^(m+o(m))`.  The greedy union
bound is therefore valid.  Exact external traces separate distinct low
paths; the greedy high step includes all cross-family collisions.

This verifies all five rows of the pinned reservoir theorem.  Its
residence is constituent-path clipped residence only.

## 2. Coordinate and host quantifiers

The proof uses the following order, and no stronger order is available:

1. choose one nonloop all-six-coherent pull `g_0` in the rotational
   canonical factor;
2. choose `q` outside the complete hexagon-plus-stub support of `g_0`;
3. choose the fixed-boundary pull spanning tree `R_q`, every one of whose
   circuit vertices contains `q`;
4. complement the factor, tree, and pull simultaneously.

After complementation, every vertex of `R_q^0` avoids `q`, while every
vertex and unchanged stub of `g=kappa(g_0)` contains `q`.  Complementation
swaps the two Middle-Levels shores but preserves incidence, alternating
phases, nonloopness, coherence, and the auxiliary component labels.  The
new ring's common lower-port intersection therefore contains `q`, so this
same coordinate may be used as `q_0` in the reservoir.

The theorem correctly does **not** start from an arbitrary prescribed
ring.  It also explicitly assumes that any extra pull labels used to
install the bank lie with `R_q^0 union {g}` in one fixed
pairwise-support-disjoint tree-compatible host `H`.  The fixed-boundary
theorem alone does not provide that enlargement.

## 3. Exact basis-extension replay

Let `D` be the common protected bank, let `A_D` be its forced installation
labels in the same host, and put `J=A_D union {g}`.  If `J` is graphic
independent, contract each component of `J`.  The image of the spanning
tree `R_q^0` remains connected.  A spanning tree of this image lifts to

\[
                 J\subseteq T\subseteq J\cup R_q^0.
\]

Every edge of `D` has both endpoints in the `q=1` half, whereas every
complete support used by a label of `R_q^0` lies in the `q=0` half.
Consequently a completing label in `T-J` neither installs nor deletes a
protected edge.  In the notation of the last-ring basis theorem, no such
label belongs to `B_D`.  Accessibility and phase consistency handle the
forced labels in `A_D`, and `D cap Z_g=emptyset` leaves the two ring phases
free.

Since `T` is a spanning tree, `T-{g}` has exactly two auxiliary
components.  Tree compatibility gives exactly two factor cycles before
the final switch and one Hamilton cycle after it.  This proves that the
residual **physical** cographic cut condition is automatic once
accessibility and graphic independence hold in the declared host.

## 4. Pull support and residence scope

Only the completing labels supplied from `R_q^0` are asserted to be
vertex-disjoint from the pinned bank and ring.  Forced labels in `A_D` are
controlled instead by the fixed-host accessibility and phase-consistency
hypotheses; the theorem makes no unproved vertex-disjointness assertion for
them.

Opposite-half completion changes no factor edge incident with a `q=1`
vertex.  It can permute or reconnect the intervening `q=0` pieces, but it
cannot alter the induced `q=1` path segments or their multiset of lengths.
Therefore it cannot repair a short positive `q`-run.  The proposition on
residence is exact.

Physical vertex separation also does not preserve a typed cap, interval
address, global order, or route merely by itself.  The theorem correctly
requires a separate invariance premise for any typed conclusion.

## 5. Audited dependencies

The proof was replayed against the following current sources:

* coherent ring pull, SHA
  `1dbb9d071a19cc5b5193b3e7d6e5c99e9ba840d45337d842c2b054e3f0cd6025`;
* clipped upper reservoir, SHA
  `737b5ece3b7f7d04f5cb69080feacce1616c100b857f07b2c2abf9d88bf5dcf4`;
* exact last-ring basis criterion, SHA
  `77190f0c5eb0dc2caacdce5c5aefc472119695f20722412ba4bc47d452b7cc30`;
* fixed-boundary lollipop theorem, SHA
  `9c2a4a8624115e627aadc9229091d5fff3d5cecd6ba1638603ccd24ecd7e35f0`.

The surviving open rows are exactly the ones stated by the source:
compatible-host accessibility, forced graphic independence, global cyclic
residence, ambient upper completeness, typed/common-cap invariance, the
global antecedent/lower deck, and regeneration.
