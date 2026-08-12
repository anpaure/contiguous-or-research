# K16 nine-circuit hybrid-cube no-go (2026-07-30)

## Switching theorem

Let (P,Q) be spanning paths on the same vertex set, and colour the edges of
(P\setminus Q) red and those of (Q\setminus P) blue.  Switching a coloured
subgraph (C) in (P) preserves the complete degree vector—and therefore the
same endpoint set—if and only if

\[
\deg_{C\cap P}(v)=\deg_{C\cap Q}(v)\qquad\text{for every }v.
\]

If (P,Q) have the same endpoints, their full symmetric difference is
balanced and decomposes into alternating circuits.  Any edge-disjoint
collection of those circuits preserves the endpoint-degree vector.  The
switched graph is a Hamilton path exactly when it is connected: otherwise its
degree vector describes the endpoint path plus one or more disjoint cycles.

## Exact cube result

Nine G0- and upper-complete parents were collapsed to their 12,870-vertex
Hamilton-path skeletons.  Pairwise symmetric differences against atom 43389
gave nine distinct primitive alternating circuits and two observed flat-value
schemes.

- nominal cube: (2^9=512);
- pairwise edge-compatible switch sets: 160;
- connected Hamilton skeletons: 92;
- generalized-envelope-valid rows after both flat schemes: 184;
- all-upper-complete rows: 182.

Exact maximum matching was run on every emitted row.  The minimum Hall
deficiency is 92, attained only by the unswitched atom-43389 base with its
original flat scheme.  Every nontrivial hybrid is worse.

Thus the small hybrid lattice is mathematically real but does not pay the
compiler debt.  Any continuation must mine a materially larger and
witness-directed circuit catalogue rather than compose the same local
3-opt circuits indiscriminately.

The compact audit is at `scratch/k16_hybrid_cube9_nogo_20260730/`; the exact
enumerator is `scratch/search_k16_hybrid_component_cube_20260730.cpp`.
