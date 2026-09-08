# Audit of hook leaf plucking and adjacent angle transfer

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_HOOK_LEAF_PLUCKING_ADJACENT_TRANSFER_20260805.md`  
**Method:** independent tree-slot and height replay; no search  
**Verdict:** **PASS** for `h>=3`, with loose-forest packing explicitly open.

The inverse leaf-pruning fibre over the mountain of semilength `h-1` is
exactly a path spine with leaves in `2h-1` ordered slots.  Removing the one
compulsory terminal leaf leaves a weak composition of `b`; formula (1.3)
is bijective.  Substitution into the first-maximum formula for `phi` shows
that `phi^2` sends the last slot to the first and shifts every other slot
one place, proving (1.4).

For the C6, the three normalized centers are literally `F10,10F,1F0`.
The first two have type `(h,1^b)` and the third type
`(h+1,1^(b-1))`.  The down-step `c` after the rightmost height-`h`
maximum is the reverse root in all three.

Changing `c` upward raises the post-`c` height profile by two.  Its last
maximum occurs at the last old height-`h-1` visit, so the following
down-step is `d`.  Removing the first up-step lowers this profile by one;
the appended tails `100` and `010` reach height at most two.  Hence `h>=3`
leaves `d` as the rightmost-max successor in all three predecessor words.
This proves the common companion deletion and therefore exact q2
neutrality.

If the last slot of `x` is positive, deleting one final `10` gives `F`.
Prepending that leaf gives the vector `x-e_(q-1)+e_0`.  Changing phase
rotates the slots, so every adjacent transfer occurs.  Adjacent transfers
connect the raw weak-composition graph and hence its necklace quotient.
The physical hook-component identification uses the already established
exact action-angle correspondence behind the `L_gamma` census.

The theorem proves literal incidence connectivity, not a physically
disjoint loose spanning tree.  Repeated donor components and occurrence
capacity remain genuine global constraints; the source states them.
