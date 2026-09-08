# Audit: full GK root-hinge catalogue

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_FULL_GK_ROOT_HINGE_CHARACTERIZATION_AND_LINEAR_MINIMUM_20260807.md`  
**Verdict:** **GO.**

The height identity

\[
H_{B_x}=H_U-2[\cdot\ge u]-2[\cdot\ge b]+2[\cdot\ge x]
\]

forces `u<b<x`.  If `b` ends at original height `h`, its modified height is
`h-4`; being the last unmatched zero forces `h=1` or `h=2`.  The pre-`b`
record condition gives respectively an earlier top-level component or an
earlier position in the same top-level component.  The post-`b` record
condition is equivalent to choosing `x` inside the subtree opened by `b`.

Counting these choices in an ordered forest gives formula (3.3).  Dropping
the nonnegative sibling products yields `|L_U|>=m-1`, and the mountain
`1^m0^m` attains equality because only its height-two opener is available,
while `x` may be any of the `m-1` downsteps in that child subtree.

The same equality holds for every `11E00`, with `E` any Dyck word of
semilength `m-2`; this gives exactly `Cat_{m-2}` linear-menu roots and the
ratio in (3.8).  Thus the theorem explicitly rules out treating all
subquadratic menus as an `o(Cat_m)` exceptional family.

The polynomial resource loads in Section 4 are deliberately coarse and
are not claimed sharp.  In particular the note makes no Aharoni--Haxell or
global transversal claim.
