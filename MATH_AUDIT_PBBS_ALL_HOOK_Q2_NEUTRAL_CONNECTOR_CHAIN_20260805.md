# Audit of the physical all-hook q2-neutral PBBS connector chain

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_ALL_HOOK_Q2_NEUTRAL_CONNECTOR_CHAIN_20260805.md`  
**Method:** independent forward/reverse cancellation and profile replay;
no search  
**Verdict:** **PASS** for `b>=1`, `h=m-1-b>=4`.

The sets in (1.2) are disjoint and have the claimed cardinalities.  Reading
the bits between `a_0,a_1,a_2` gives literally

\[
 \varnothing,
 \qquad
 (10)^b,
 \qquad
 1^h0^h.
\]

After flipping `a_i`, forward cancellation leaves `a_(i-1)` and reverse
cancellation leaves `c`.  Complementing and deleting those roots gives
exactly `Q_(i+1)` and `P_(i+1)`.

For the companion side, reverse roots are

\[
 2b+2,
 \qquad
 2b+3,
 \qquad
 2b+3.
\]

Deleting them from the complements gives the three rows (3.2).  In each,
the next reverse cancellation leaves `d=m+b+3`, proving the common
companion row `P_i-d`.

Forward cancellation of the six q1 rows gives exactly the two triples of
unmatched zeros in (4.1) and (4.3).  Each has two empty blocks.  Direct
prefix sums on the remaining block give heights

\[
 (h,h-1,h-1)
\]

on both shores, with rightmost-max successors respectively

\[
 (a_1,a_2,a_0),
 \qquad
 (a_2,2b+3,2b+3).
\]

These are the old and companion PBBS occurrences.  Hence all six are
selected, and the common-deletion q2 theorem applies.

Finally, `beta((10)^b)=(b)` and
`beta(1^h0^h)=(1^h)`.  Adding the three wrapping units gives the profiles
and conjugate partitions in (5.3).  Substituting `h=m-1-b` yields exactly
`{H_b,H_(b+1),J_b}`.

For the shared hook profile, the two normalized shapes are

\[
 1^h0^h(10)^{b+1},
 \qquad
 (10)^{b+1}1^h0^h.
\]

Two direct `phi` steps join them.  The complete cycle (6.8) has period
`2h-1` and voltage one modulo `2m+1`, so its physical lift is one odd
`g=f^2` component.  Consecutive connector triples therefore share exactly
that component.

Only consecutive triples share a component.  When choosing rotations
along the chain, the next connector must avoid one already chosen cycle
edge.  At most three of its `2m+1` rotated edges meet that edge, so a legal
rotation always remains.  This proves pairwise vertex-disjoint physical
support and validates the loose-tree composition.  The resulting theorem
still concerns only `2m-9` PBBS components, not the full factor.
