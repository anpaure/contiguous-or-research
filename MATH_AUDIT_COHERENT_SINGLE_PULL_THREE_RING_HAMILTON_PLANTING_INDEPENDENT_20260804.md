# Independent audit: coherent single-pull three-ring Hamilton planting

**Date:** 2026-08-04  
**Method:** independent dependency and proof audit; no computation or search  
**Verdict:** `GO`, subject only to the theorem's explicit exclusion of
residence, arbitrary-width upper witnesses, and common-cap regeneration.

## 1. Same-factor provenance

The construction consistently uses the rotational canonical factor `C_n`.
The literal maps `f,g`, the standard pull hexagons, the star-bridge label

```text
1100(10)^(n-2) <-> 1010(10)^(n-2),
```

and the transformed distinguished-coordinate pull tree all belong to that
same factor model.  No lexical GMN/MMM identification is used.

The cited star-bridge theorem proves that this label is allowed and nonloop
for `n>=3`.  The coherent-hex theorem proves `u=empty` if and only if all
three lower external stubs use one common insertion coordinate and all
three upper stubs use one common deletion coordinate.

## 2. Literal ring identification

For the pull's own core `B` and active labels `a_0,a_1,a_2`, its old
alternating matching is the predecessor matching `I_i R_i`, and its
opposite matching is the successor matching `I_i R_(i+1)`.  The unchanged
lower factor incidences all insert the same external label `b`, hence are
exactly `I_i L_i`.  Therefore the two local factor states are literally the
two complete three-ring phases.  The revised wording only names coordinates
already present in the pull and does not assume an arbitrary permutation
preserves `C_n`.

## 3. Protected tree exchange

The complete ring support uses at most

\[
 (m-2)+3+1=m+2
\]

coordinates.  Since the ground set has size `2m-1`, an absent coordinate
`q` exists for `m>=4`.  Every ring vertex has `q=0`.

The fixed-boundary lollipop theorem supplies, on the same factor, a pull
spanning tree `R_q` all six vertices of each gluing hexagon of which have
`q=1`.  Consequently every pull support in `R_q` is vertex-disjoint from
the coherent ring pull and from its three unchanged `L_i` stubs.

Let the coherent pull join canonical components `K_0,K_1`.  Adding its
auxiliary edge to `R_q` creates one cycle; deleting an edge on the unique
`K_0--K_1` path gives a spanning tree `T`.  The retained pulls are
compatible because `R_q-e` was compatible and the added pull is physically
vertex-disjoint.

## 4. Component count and Hamilton toggle

Toggling `R_q-e` contracts a spanning forest with exactly two auxiliary
blocks, so tree compatibility gives exactly two factor cycles.  The local
ring remains in its old phase.  Adding the coherent pull restores the
spanning tree `T`, and its toggle merges those two blocks into one Hamilton
cycle while changing exactly the predecessor ring matching to the successor
matching.  No position or vertex is added.

## 5. Scope

The proof closes the bare owner/factor topology and, via the separately
proved common-history theorem, the local short-deck rethread.  Vertex
disjointness from the completing pulls does not establish global residence,
arbitrary-width witness preservation, background compiler coexistence, or
recursive cap regeneration.  The source theorem does not claim those rows.
