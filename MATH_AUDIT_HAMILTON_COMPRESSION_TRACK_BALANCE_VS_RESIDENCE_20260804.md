# Hamilton compression, one-track balance, and residence are independent

**Date:** 2026-08-04  
**Status:** exact counterexample and scope audit for the Johnson long-run
route.

## 1. Exact counterexample

In `J(5,2)`, consider the cyclic Hamilton ordering

\[
 12,13,23,24,34,35,45,14,15,25.                         \tag{1.1}
\]

Every consecutive pair (including `25,12`) intersects in one coordinate,
and the ten vertices are all the two-subsets of `[5]`.

Let `rho=(1 2 3 4 5)`.  Advancing two positions in (1.1) applies `rho`.
Thus the cycle is `5`-symmetric, which is the maximum possible compression
for `J(5,2)`.  Its five incidence columns are cyclic shifts of one another,
so it is one-track; consequently every coordinate is flipped equally often.

Nevertheless the coordinate-1 column is

\[
                         1100000110,                     \tag{1.2}
\]

cyclically.  It has a zero-run of length one (the final zero) and hence
minimum coordinate residence one.  Therefore maximal linear Hamilton
compression, one-track structure, and exact flip balance do not imply any
nontrivial minimum run floor.

## 2. Why the invariants miss the needed datum

For an `n`-symmetric Johnson cycle under a cyclic coordinate permutation,
one wedge determines the other wedges.  The one-track statement says that
the coordinate columns are cyclic shifts of a common binary column.  Flip
balance fixes only the number of transitions of that column.  Residence is
the minimum cyclic distance between successive transitions, which is not
controlled by either the number of transitions or the shifts.

Thus the high-compression constructions of Gregor--Merino--Mütze are useful
for topology, symmetry, and balance, but they cannot be cited as a
residence theorem.  A separate wedge-spacing certificate is necessary.

## 3. Relation to the pair-stratified factor

Inside a fixed pair cell, the Goddyn--Gvozdjak theorem supplies precisely
the missing spacing certificate.  Across cells, compression again controls
only repeated geometry, not the distance between two uses of the same
physical coordinate.  Any cross-cell splice theorem must therefore state
and verify transition-label separation explicitly.

Primary source for the compression claims: P. Gregor, A. Merino and
T. Mutz(e), *The Hamilton compression of highly symmetric graphs*,
arXiv:2205.08126 (2023 revision).
