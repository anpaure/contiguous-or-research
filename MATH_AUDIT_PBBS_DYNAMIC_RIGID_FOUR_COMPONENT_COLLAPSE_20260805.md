# Audit of the dynamic rigid four-component PBBS collapse

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_DYNAMIC_RIGID_FOUR_COMPONENT_COLLAPSE_20260805.md`  
**Method:** exact support count, path reconnection, and permutation parity;
no search  
**Verdict:** **PASS** for all sufficiently large `m`.  The result is local
to the four components `S,T,A,B`.

## 1. Rotation selection

A clean C6 has six changed-shore rank-`m` vertices.  Each of its six q2
turns can require at most one further endpoint on an unchanged companion
edge, so the protected support bound

\[
                         |\Sigma|\le12
\]

is valid.

The rotation action on rank-`m` subsets of `Z_(2m+1)` is free: a nontrivial
stabilizer orbit length would divide both `m` and `2m+1`.  Hence for finite
sets `U,V`, each pair `(u,v)` forbids at most one rotation and at most
`|U||V|` rotations are bad.

The rotated promotion edges on `T` have cyclic gap `p=2m-3`.  The two open
arcs have lengths `p(m+1)` and `pm-2`, so they provide at least `m` and
`m-2` interior candidates respectively.  Avoiding `R` excludes at most
`144` rotations; avoiding `R` and the first promotion excludes at most
`288`.  Thus, for example, `m>=291` is a conservative explicit threshold
for the stated pairwise-disjoint choice.  The theorem only needs existence
for sufficiently large `m`.

## 2. Exact topology

Initially the subsystem consists of four cycles `S,T,A,B`.  The rigid
switch replaces `S,T` by two cycles `H_1,H_2`, leaving four total.  The
first promotion sees one old edge on each of `H_1,A,B`; a three-way clean
switch merges these into one cycle `M`.  The count is now two: `M,H_2`.

The second promotion sees its `T` edge on `H_2` and its `A,B` edges on
`M`.  Physical support disjointness guarantees that all three old edges
still exist and are distinct.  Deleting one edge from `H_2` gives one
directed path; deleting two edges from `M` gives two directed paths.  Thus
the reconnection acts on exactly three paths and can create at most three
cycles.

The successor permutation changes by a 3-cycle.  A 3-cycle is even, and on
the fixed subsystem vertex set

\[
 \operatorname{sgn}(\pi)=(-1)^{N-c(\pi)}.
\]

Therefore the parity of the component count is unchanged.  Starting from
two cycles, the positive post-switch count is even and at most three, hence
is exactly two.  This validates the topology argument without assuming a
particular cyclic order of the two `M` cuts.

## 3. q1/q2 and omission accounting

Each of `R,E_1,E_2` is individually q1- and q2-neutral.  Their protected
supports are pairwise vertex-disjoint, so no earlier switch changes a later
old shore or unchanged companion turn.  The three local multiset identities
therefore compose exactly.

All four input components are wholly selected in the asserted range.  Each
switch removes selected old edges and inserts selected replacement edges;
no unselected edge is introduced.  Both final cycles are consequently
wholly selected.  Puncturing one selected turn on each leaves two named
graphic defects, and the independent bounded-defect Pascal theorem charges
at most `2*2=4` q2/owner sidecar occurrences.

The proof does not attach any other PBBS component and makes no q3,
residence, arbitrary-upper, or common-cap assertion.  Its scope is exact.
