# Hostile audit of the flat D5 router--token incidence pseudoforest

**Date:** 2026-08-14  
**Verdict:** **PASS after one scope repair.**  The incidence graph has exactly
25 tree components and eight unicyclic components, each with two-core
`K2,2=C4`.  The counts `461` prospective C6 collars and `16` prospective C8
collars follow from the token-degree census only; no q1-exact collar,
resource-disjoint propagation rule, or holonomy solution follows from the
graph theorem.

Audited source:

```text
MATH_THEOREM_D5_FLAT_ROUTER_TOKEN_INCIDENCE_IS_A_THIRTY_THREE_COMPONENT_PSEUDOFOREST_20260814.md
```

## 1. Symbolic component proof

For an odd target cycle of length `2r+1`, the flat word has `r` router
vertices, `2r+1` token vertices, and `3r` incidences.  Consecutive routers
share the single chain-junction token, so the block is connected.  Its
vertex/edge counts are `3r+1` and `3r`, hence it is a tree.  Disjoint target
cycles use disjoint token sets, so the 25 odd cycles give 25 distinct tree
components.

For paired even cycles of lengths `2r,2s`, the two prefix chains and the two
residual bridge routers have

```text
routers  r+s,   tokens  2r+2s,   incidences  3(r+s).
```

The block is connected, so its cycle rank is one.  After leaf-peeling both
prefix chains and the bridge-only leaf tokens `b,d`, the two bridge routers
remain adjacent to exactly the two penultimate tokens `a,c`.  The two-core
is therefore the simple bipartite graph `K2,2`, not merely an unspecified
four-vertex cycle.  Eight even-cycle pairs give eight such components.

Adding the blocks yields exactly 33 connected components and global cycle
rank eight.  No hidden edge can join two provenance blocks because the 41
target cycles are token-disjoint and the even factorization couples only the
declared pairs.

## 2. Degree and collar-count replay

The H100 verifier reconstructs the graph directly from the flat certificate,
without using the symbolic formulas.  It gives

```text
router nodes                              226, all degree 3
token nodes                               477
token degree histogram          1:292, 2:169, 3:16
incidences                                 678
components                                  33
cycle-rank histogram                    0:25, 1:8.
```

It also checks that each certificate provenance interval is exactly one
graph component and leaf-peels every unicyclic component to a four-vertex
degree-two bipartite core with two router and two token vertices.  In a
simple bipartite graph this is necessarily `K2,2=C4`.

The prospective collar counts are then arithmetic:

```text
degree-one or degree-two tokens   292+169 = 461
degree-three tokens                            16.
```

Thus the proposed menu has one prospective C6-class collar for each of the
first 461 token vertices and one prospective C8-class collar for each of the
16 degree-three vertices.  The 292 degree-one tokens are precisely the ones
for which the proposal adds a dummy identity role.

## 3. Scope of the physical reduction

The graph theorem proves only where compatibility constraints can live.  It
does not prove any of the following.

1. A prescribed degree-one or degree-two token admits a q1-exact resident C6
   collar with the required dummy/active roles.
2. A prescribed degree-three token admits the analogous C8 collar.
3. The extension relation is nonempty for every boundary state encountered
   while traversing a tree component.
4. Greedy local choices remain owner/lower/upper/q2-disjoint globally.
5. Each unicyclic core contributes only one scalar equation; in general it
   is a finite-state closure problem.
6. Any collar embeds into the native MSW factor or repairs the literal
   zero-site obstruction without added occurrences.

The source already labels all 477 collars “prospective” and lists the missing
Johnson, palette, q2, residence, and native-factor checks.  During audit its
one overcompressed sentence about “eight compatibility equations” was
repaired to say “eight independent four-cycle closure subproblems” and to
make totality and global-resource preservation explicit.  With that repair,
the `461/16` statement is a valid target reduction rather than a collar
existence claim.

The bare-splice obstruction remains fully compatible with this theorem.  It
rules out omitting the coupled collar layer; it neither constructs nor rules
out the prospective C6/C8 menus.

## 4. Frozen H100 artifacts

```text
audited theorem
  cb6257156b3a905ad6ebd775efdf9958fbb136db462b7c49413c3ea92289b7e5

verifier
  scratch/verify_d5_flat_router_token_pseudoforest_20260814.py
  016d9cd911363e8a5bc0de9f61a0da495906c0d37f8ed687b6bcaf5f92848393

H100 output
  scratch/verify_d5_flat_router_token_pseudoforest_20260814.h100.out
  d7a7f39e13e2543344f9c5eb6bf321e113c9511f79e5976f7053aa9358e672c1

flat atlas certificate
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.h100.out
  2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc
```

All verification and hashing were performed via SSH on H100.

