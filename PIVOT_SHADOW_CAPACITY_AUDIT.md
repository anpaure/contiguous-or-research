# Independent-style audit of `PIVOT_SHADOW_CAPACITY.md`

## Verdict

The nonlocal-pivot cells are valid, but their pivots remain too sparse in
every `H`-geodesic factor with `H` above the RSK radius cutoff.  The claimed
`Omega(W)` lower- and upper-shadow deficit follows.  The conclusion is
correctly restricted to this one BK partition and does not cover mixed
coordinate conjugates or arbitrary non-geodesic factors.

## 1. Cell audit

For a critical orientation word of length `a`, the prefix of length `a-1`
has either no `DU` or one unique last `DU` at `b`.  Hence the cells `S_b`
are disjoint and exhaustive while the final bit remains free.

When `b>0`, every free prefix generator has the fixed later `DU` at `b`, so
the exact carrier formula makes it native throughout the cell.  The final
generator sees the fixed last earlier carrier `p_b+1`.  When `b=0`, all
earlier bits are fixed `UD`, so it sees the fixed initial carrier.  The
carrier belongs to a nonfree block and cannot overlap a free native pair.
Different critical levels use different stack carriers.  Thus the supports
are fixed and pairwise disjoint.

There is exactly one final pivot per nonempty critical level and at most
`floor(d/2)` such levels.  This verifies the central structural input rather
than assuming it.

## 2. Pivot-density audit

In an `H`-geodesic cyclic direction word, a fixed direction occurs at most
once per full length-`H` arc, plus one boundary occurrence.  Thus `R` pivot
directions contribute at most `RL/H+R` transitions in a cycle of length `L`.
Every transition belongs to exactly `q` cyclic depth-`q` windows.  Markov
therefore gives a high-pivot fraction at most

\[
 R/(\epsilon H)+O(R/(\epsilon L)).
\]

With `D=sqrt(mg)`, `H=sqrt(m)g`, and `R<=D/2`, the main fraction is
`O(g^(-1/2))`.  Since every cycle has length at least `H`, the boundary terms
sum to `O(DW/H)=o(W)`.  The radius-`>D` family is
`exp(-g+o(1))W=o(W)`.  These estimates are uniform over all cycle orders and
couplings.

## 3. Type-Lipschitz audit

The lower intersection deletes one initially selected endpoint for every
transition direction.  A native direction starts from a split native pair,
so its deletion cannot change the number of full native pairs.  A cross-pair
pivot deletes only one selected coordinate and can destroy at most one full
native pair.  Therefore

\[
 F(L)\le F(X)\le F(L)+r.
\]

The constant is one, not two.  The argument does not require the pivot
supports to form a perfect matching of all ground coordinates.

## 4. Type-count audit

The exact multinomial counts `V_g` and `T_(f,q)` sum respectively to `W` and
`N_q`.  Their means follow by counting fully selected native pairs.  The
variance formula uses the one-pair and two-pair inclusion probabilities and
has leading term `m/16` for `q=O(sqrt(m))`.

Stirling expansion therefore gives the stated Gaussian local limits.  At
`q=c sqrt(m)`, the source and target means differ by
`(c/2+o(1))sqrt(m)`, while `N_q/W->e^(-c^2)`.

Choose `epsilon=1/32`.  A target in a fixed positive-mass band and a window
with at most `epsilon q` pivots require a source in a middle-type left tail
whose Gaussian exponent is

\[
 8(1/2-\epsilon)^2c^2+O(c).
\]

This coefficient exceeds `1`, whereas the target-layer exponent relative
to `W` is `c^2`.  Taking one sufficiently large **fixed** `c` makes all such
sources fewer than a fixed fraction of the target band.  High-pivot and
exceptional starts contribute `o(W)`.  The resulting deficit is a positive
constant times `N_q`, hence a positive constant times `W` because `c` is
fixed before `m->infinity`.

## 5. Boundary and scope checks

* Complementation converts the upper problem to the same lower-intersection
  argument with the same transition supports.
* At most `W/H` cycles occur, so linearization introduces
  `O(qW/H)=o(W)` seam-crossing depth-`q` windows.
* No random independence or common direction order is assumed.
* The proof does assume `H`-geodesicity.  A construction allowing frequent
  reuse of pivot directions inside `H` transitions lies outside its scope.
* Coordinate-conjugated BK partitions do not share one native type statistic
  `F`; the obstruction does not apply to a globally mixed reservoir.

The checker `scratch/check_pivot_shadow_capacity.py` independently verifies
the pivot cells, fixed supports, pairwise disjointness, exact type totals,
and the type-Lipschitz inequality through depth three for every tableau with
`m<=8`.

