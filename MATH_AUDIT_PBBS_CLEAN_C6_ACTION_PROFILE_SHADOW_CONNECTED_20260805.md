# Audit of the deficit-three C6 action-profile shadow

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_CLEAN_C6_ACTION_PROFILE_SHADOW_CONNECTED_20260805.md`  
**Method:** independent pruning and partition replay; no search  
**Verdict:** **PASS**, with the template/physical distinction essential.

Flipping `a_i` in

\[
 0_{a_0}D_0\,0_{a_1}D_1\,0_{a_2}D_2
\]

leaves `a_(i-1)` unmatched and gives the rooted word
`D_(i-1)(1D_i0)D_(i+1)`.  Peak pruning is additive under concatenation,
and the outer pair around a height-`h_i` word survives for exactly one
additional pruning layer.  Hence the profile is
`b+e_(h_i+1)` exactly.

For a partition `b`, the mountain decomposition has
`c_h=b_h-b_(h+1)` factors of height `h`.  Addability of row `j>1` is
equivalent to `c_(j-1)>0`; row one is represented by an empty block.
Therefore any two distinct children of `b` can be assigned to the first
two deficit-three blocks, with the remaining mountains in the third.  This
proves that every sibling adjacency has an abstract template.

Moving one removable nonfirst-row box to the first row follows one sibling
edge and strictly decreases the number of boxes outside row one.  Hence the
sibling graph is connected and reaches `(m)` in at most `m-1` steps.

Nothing in this argument produces the common reverse-deletion coordinate,
max-height selection, directed PBBS incidence, or compatible occurrence
supports.  The source explicitly retains these as the angle/physical
lifting obstruction, so its scope is correct.
