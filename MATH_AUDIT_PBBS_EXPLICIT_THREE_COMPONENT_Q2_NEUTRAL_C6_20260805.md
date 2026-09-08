# Audit of the explicit three-component q2-neutral PBBS C6

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_EXPLICIT_THREE_COMPONENT_Q2_NEUTRAL_C6_20260805.md`  
**Method:** independent literal cancellation; no computation or search  
**Verdict:** **PASS** for `m>=6`.

The partition (1.2) and all ranks are exact.  The forward decomposition of
`H` is literally `empty,10,mountain`, so its three forward survivors are
`0,1,4`.  The regional reverse maxima are the displayed triples (2.4),
and all choose the first down-step `m+3` of the mountain.  Complementing
then gives `f(Z_i)=Q_(i+1)` and `f^(-1)(Z_i)=P_(i+1)`.

For the companion table, prefix-height replay gives reverse survivors
`4,5,5` on `P_0,P_1,P_2`.  Complementing and deleting those survivors
gives exactly the three middle sets in (3.1).  Each has rightmost maximum
immediately before `m+4` when `m>=6`, proving the common deletion.

The old-row max-height comparisons select following steps `1,4,0`; the
companion comparisons select `4,5,5`.  These recover the displayed old and
incoming factor edges, so the common-deletion theorem applies to six
actually selected occurrences.

Finally, the base peak profile is the sum of the profiles of `10` and the
semilength-`m-2` mountain, namely `(2,1,...,1)`.  Adding units in positions
`1,2,m-1` gives the three partitions in (5.3), hence three distinct PBBS
components.  No quotient-connectivity conclusion is inferred.  The scope
is exact.

