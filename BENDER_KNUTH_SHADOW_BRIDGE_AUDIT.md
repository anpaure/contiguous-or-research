# Adversarial audit: Bender--Knuth shadow bridge

This note audits `BENDER_KNUTH_SHADOW_BRIDGE.md`.  The outcome is:

* the last-`DU` orbit partition is valid and upgrades the overlapping
  host-cube theorem to a genuine near-partition;
* the inverse-RSK permutation criterion and both shadow obstructions are
  valid with the scopes stated;
* the native-pair partition is subject to the one-fixed-matching capacity
  obstruction and therefore cannot by itself prove `nu(2m)=W+o(W)`;
* no claim is made that conjugated or nonlocal BK reservoirs can yet be
  rounded integrally.

## 1. Inputs used from the carrier theorem

The bridge uses exactly the following proved facts from
`BENDER_KNUTH_ISOMETRIC_CUBES.md`.

1. An odd-BK orbit fixes the block-height path, active mixed blocks, radius,
   and critical sequences.
2. In a critical sequence with orientation bits `x_1,...,x_a`, generator
   `r` has native support whenever some later bit is `1`.
3. Outside critical sequences every active generator always has native
   support `{2j-1,2j}`.
4. There are at most `floor(d/2)` critical sequences at radius `d`.
5. Outside `o(W)` vertices, `d<=m^(2/3)` and the number of `DU` blocks is at
   least `m/8`.

No false `3^m` twist-incidence estimate is used.

## 2. Last-`DU` cells really partition an orbit

For one critical word `x in {0,1}^a`, exactly one of the following holds:

* `x=0^a`; or
* it has a unique last `1` at `l`.

Thus the sets `R_0,R_1,...,R_a` in (1.4) are disjoint and cover the
orientation cube.  In `R_l`, precisely `x_1,...,x_(l-1)` are free.  Every
free index `r<l` sees the fixed later `1` at `l`, so the carrier formula
forces native support at every point of the cell.  Native supports from
different odd blocks are disjoint.  Products over critical sequences, with
all noncritical active directions free, remain disjoint and cover the whole
odd-BK orbit.

The construction does not merely choose one cube through each point.  It is
a literal partition into subcubes.

## 3. Dimension calculation

For a sequence of length `a`, the dimension deficit is `a` on the all-zero
cell and `a-l+1` when the last `1` is at `l`.  Under the uniform measure on
the orbit orientations,

\[
 a2^{-a}+\sum_{t=1}^a t2^{-t}=2-2^{1-a}<2.
\]

Summing over at most `d/2` critical sequences gives `E Delta<d`.  This is an
orbitwise expectation, so Markov may be applied inside every orbit and then
summed with orbit-size weights.

An orbit with fewer than `m/8` active directions contains no word with
`m/8` `DU` blocks, because every `DU` is active.  Hence all vertices of such
orbits belong to the already proved `o(W)` lower-tail family.  On the
remaining radius-`<=m^(2/3)` orbits,

\[
 \Pr(\Delta>m^{5/6})\le m^{-1/6}.
\]

Therefore deleting `o(W)+m^(-1/6)W=o(W)` vertices leaves cell dimension at
least `m/8-m^(5/6)`.  No independence between critical sequences is needed;
linearity of expectation suffices.

## 4. RSK permutation criterion

At depth `q`, both the certified start set and either target layer have size

\[
 \sum_{d\ge q}(N_d-N_{d+1})=N_q.
\]

Inverse RSK with insertion vector `P_(d,q)` is a bijection on each shape.
Thus composing the physical shadow with inverse RSK changes no collision
multiplicity.  Injectivity is equivalent to bijectivity.  This criterion is
exact, but it is a reformulation rather than an existence theorem.

The no-identity proposition is also exact: prescribing both canonical
depth-one flags determines the canonical crystal projection, whose radius is
`d-1`, not `d`.  It rules out retaining both standard flags at the same
tableau; it does not rule out a nontrivial permutation of flags.

## 5. Depth-one random barrier

Inside one fixed-coordinate cube, an edge is uniquely determined by either
its lower or its upper face.  Consequently candidate events for one target
occur in distinct cubes.  A symmetric random cycle factor of an `s`-cube
uses a fraction `2/s` of its edges.  Under independent cube choices, the miss
probability is therefore the product in (5.5).

The sum of candidate means over all targets is exactly the number of
positive-radius middle vertices, namely `N_1`.  Convexity then gives the
`e^(-1)-o(1)` expected missing fraction when the minimum cube dimension
tends to infinity.

This is an obstruction only to **independent orbitwise rounding**.  It is not
a deterministic lower bound on optimally coordinated cycle factors.

## 6. Direction-catalog bound

A fixed `q`-direction set has only `2^(s-q)` faces in an `s`-cube.  Therefore
a catalog of `K_q` direction sets yields at most `K_q2^(s-q)` distinct
shadows.  One common cyclic order supplies at most `ell` such sets.  The
bound is independent of the linear-code kernel and remains true for every
same-order cycle tiling.

It does not rule out tilings whose cyclic direction orders vary from cycle
to cycle.  Such diversity is precisely what the next construction would
need.

## 7. Native-pair capacity obstruction

Every free support in the last-`DU` partition is one of the single global
matching pairs `{2j-1,2j}`.  Therefore the exact type counts `T_(f,q)` and
`V_f` from `FIXED_PAIR_RESIDUAL_SCD.md`, Section 8, apply to every possible
cycle factor of this partition, regardless of local order.

For `q=c sqrt(m)` and a sufficiently large fixed `c`, a positive fraction of
the target-type mass has `V_f/T_(f,q)<=1/2`, while

\[
 N_q/W=e^{-c^2+o(1)}.
\]

Thus the missing count is `Omega(W)`, with a constant depending on `c` but
not on `m`.  This is enough to violate the required `o(W)` total central-band
defect.  At the intended `ell>>sqrt(m)`, cycle seams add only
`O(qW/ell)=o(W)` extra windows and cannot absorb the deficit.

This obstruction does **not** cover all Bender--Knuth subcubes.  An arbitrary
twist-graph vertex-cover cube may retain a nonlocal carrier support, and a
coordinate conjugate of the whole partition uses another perfect matching.
The theorem only rejects the single native-pair partition as the final
all-depth construction.

## 8. Checker audit

Two independent scripts cover the finite claims.

* `scratch/verify_bk_isometric_cubes.py` checks the carrier formula, twist
  graph, and per-vertex canonical cubes.
* `scratch/verify_bk_orbit_partition.py` constructs the last-`DU` cells,
  checks their disjoint union is the full middle layer, and checks every free
  support at every cell state.
* `scratch/check_bk_shadow_bridge.py` independently computes RSK from binary
  words, enumerates first-face collisions, compares with `P_(d,1)`, and
  audits face multiplicities of linear cycle tilings.

All three pass through `m=8`.  These computations verify definitions and
small cases; the asymptotic proofs do not extrapolate from the data.

## 9. Final status table

| statement | status | scope |
|---|---|---|
| linear-dimensional isometric cube through almost every tableau | proved | overlapping host cubes |
| linear-dimensional isometric cube partition of `W-o(W)` vertices | proved here | native odd-pair supports |
| locally geodesic pair-flip cycle factor | proved | inside each retained cell |
| RSK shadow maps are permutations | open | equivalent global Stage B |
| independent cube choices solve first shadows | false | expected miss at least `e^(-1)-o(1)` |
| one common direction order reaches growing depth | false | catalog bound |
| one native coordinate matching reaches full useful band | false | fixed-pair type capacity |
| mixed conjugated/nonlocal BK reservoir has an `o(W)`-defect matching | open | decisive next theorem |
