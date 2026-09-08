# Audit of the equal-height PBBS angle-transfer C6

**Date:** 2026-08-05  
**Method:** independent symbolic audit; no computation or search

## Verdict

The theorem
`MATH_THEOREM_PBBS_EQUAL_HEIGHT_LEAF_ANGLE_TRANSFER_C6_20260805.md`
is proof-safe for `h>=4`, `u,v>=1`, `u+v>=3`.

The literal PBBS/common-pivot row is the two-tail specialization of the
dominant-mountain calculation: the three center maxima have heights
`h,h,h+1`, and the predecessor maxima have heights `h+1,h,h`.  The first
two mountain down-steps are therefore the common reverse labels `c,d`.

The KKR scan can be checked factorwise:

* `M_h` creates an `h`-string of rigging zero;
* `W_u` after it leaves `u-1` unit riggings `2h-1`;
* every following ground leaf creates rigging `2h`;
* ground leaves before `W_v` have rigging zero;
* `W_v` leaves `v-1` unit riggings one;
* the final `M_h` creates a new long string without changing those old
  unit riggings.

Since the unit vacancy is `q=2h+1`, these are exactly the rows in (3.3).
Their cyclic gaps are (4.2)--(4.3).  Higher-string slides add a common
constant to unit riggings and unit slides rotate the extended rigging
index, so the gap necklace is a valid torus invariant.  The two necklaces
are unequal unless `u=v=1`.

The audit does **not** promote the angle chain (5.3) to a simultaneous
loose connector forest, does not cover arbitrary multi-gap necklaces, and
does not assert that the exceptional `u=v=1` centers lie on different
cycles.

