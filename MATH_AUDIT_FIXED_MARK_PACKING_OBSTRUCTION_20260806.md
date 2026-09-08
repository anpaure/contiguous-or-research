# Audit: orientation-robust fixed-mark fresh-path obstruction

**Date:** 2026-08-06  
**Audited file:**
`MATH_OBSTRUCTION_FIXED_MARK_FRESH_PATH_PACKING_DEFEATS_SEPARATOR_PRUNING_20260806.md`  
**Method:** symbolic parameter, role-signature, and counting replay; no
computation or search

## 1. Smaller-slice packing hypotheses

The middle slice is `binom([k-8],t-4)` and the requested path length is
`d-4`.  For `t=ceil(k/2)-d`, `d=o(k)`, and large `d`,

\[
 {k-8\over3}\le t-4\le{k-8\over2},
 \qquad (d-4)^2\le k-8.
\]

Hence the cited spectral fresh-path theorem applies.  The exact slice ratio
is

\[
 {\binom{k-8}{t-4}\over\binom{k}{t}}
 ={(t)_4(k-t)_4\over(k)_8}=\Theta(1),
\]

so the number of packed middle paths is `Theta(M/d)`.

## 2. Role and freshness replay

The five fixed-coordinate signatures in the theorem are pairwise distinct.
Therefore no prepended or appended vertex can collide with a middle vertex
or with a vertex in another outer role.  The four outer maps are injective,
and the middle packing is disjoint.

The collar event labels are exactly

\[
                         e,c,u,z,w,v,x,y,
\]

all distinct.  The middle packing lives after deleting those eight
coordinates, so none can recur internally.  Thus the completed paths are
fresh.

Forward event two inserts `z`.  Reversing a path turns old deletion
`a_(d-2)=w` into the new event-two insertion.  Hence every orientation has
second insertion in `{z,w}`.

## 3. Extension replay

The proof of the spectral maximal-packing theorem works from any initial
matching: if at least `30M/d` vertices remain, the uncovered induced family
contains another fresh path.  Thus the trapped family extends to a packing
with leave below `30M/d` without deleting a trapped path.

## 4. Cylinder contradiction

Deleting one frozen block releases all `d` of its lower vertices.  An
`O(M/d)` deletion-only separator can remove only `O(M/d^2)` blocks, leaving
`Theta(M/d)` trapped blocks.  Each contributes at least two level-two
marked occurrences with label in `{z,w}`.  Since `W=Theta(M)`, averaging
over the `2W` possible marked owners forces an atom `Omega(1/d)`.

At the central deadline, `r=Theta(d^2)`, so every fixed-factor admissible
root atom is `O(1/[r(d+1)])=O(d^-3)`.  The gap is `Omega(d^2)`.

To reduce the total two-label mass to `O(W/d^3)` one must delete
`Theta(M/d)` trapped blocks, releasing `Theta(M)` lower vertices.  This is
strictly beyond separator scale.

## 5. Scope

The result rules out deletion-only cleanup of an arbitrary oriented or
unoriented spectral packing.  It does not rule out selecting a balanced
packing initially or globally rethreading a positive fraction of the
blocks.  No claim about impossibility of the marked-ratio extension itself
is made.

## 6. Verdict

**PASS.**  The obstruction is exact in its stated scope.

