# Audit of the equal-amplitude mountain angle transfer

**Date:** 2026-08-05  
**Method:** independent height, vacancy, and gap-necklace check; no
computation or search

## Verdict

The theorem in
`MATH_THEOREM_PBBS_EQUAL_AMPLITUDE_MOUNTAIN_ANGLE_TRANSFER_20260805.md`
is proof-safe.

The dominant-mountain inequalities give the same first and second reverse
survivors `c,d` in all three phases.  Peak pruning gives exactly
`(h,t+1,t^(s-1))` twice and `(h+1,t^s)` once.  For the first action,

\[
 p_t=n-2\{t(s-1)+t+t\}=2(h-t)+3.
\]

Concatenating `M_t` changes length and twice `Q_t` by the same `2t`, while
the two wrapper letters account for the two adjacent rigging levels in
(3.3).  The cyclic gap comparison is identical to the audited amplitude-one
case and separates the tori unless there is only one remaining `t`-string.

No claim is made for arbitrary multi-gap amplitude-`t` riggings or for a
simultaneous physical packing of the displayed connectors.

