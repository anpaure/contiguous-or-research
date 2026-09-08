# Self-audit: clean `C6` repair through the rigid PBBS edge

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`  
**Verdict:** **PASS** for the local palette/q2 theorem and conditional
component criterion.  Global acyclicity remains explicitly unproved.

## 1. Rank and distinctness audit

The common core `C={1,...,m-2}` has rank `m-2`.  The four active labels
`a_0,a_1,a_2,c` are outside it and pairwise distinct.  Thus `R_i` has
rank `m-1`, all `P_i,Q_i` have rank `m`, and the six owners correspond to
the six two-subsets of the four active labels.  They are pairwise distinct.

Old and new intersections replay as

\[
 P_i\cap Q_i=C+a_i=R_i,
 \qquad
 P_i\cap Q_{i+1}=C+a_{i+1}=R_{i+1}.
\]

The old-to-new incidence difference is exactly the alternating `C6` on
the three `P` owners and three `R` rows; every `R_i--Q_i` incidence is
common to both phases.

## 2. PBBS occurrence audit

For `R_0`, the unique nonempty deficit-three block is the mountain of
semilength `m-1`, yielding endpoints `P_0,Q_0`.

For `R_1`, cutting at `0` gives one block through position `2m-2` and two
empty blocks.  Its height reaches `m-2` first after the initial
`m-2` ones and last after the isolated one at `m`; the next down-step is
`m+1`.  The max-height rule therefore gives `P_1=R_1+(m+1)` and
`Q_1=R_1+0`.

For `R_2`, the same cut gives initial height `m-2`, followed by two
down-steps and one up-step.  For `m>=4` that later up-step reaches only
`m-3`, so the rightmost maximum is followed by `m-1`.  This gives
`P_2=R_2+(m-1)` and `Q_2=R_2+0`.

The rooted Dyck words of the three `P_i` have backward distinguished
deletion `1`, so their other turn rows are `L_i=P_i-1`.  Directly cutting
each `L_i` word at the unmatched zero `1` leaves a unique nonempty block
and two terminal empty blocks.  Hence all six rows `R_i,L_i` used in the
q2 calculation are selected by the max-height rule.

## 3. Palette identities

The new q1 rows are a cyclic permutation of the old rows.  For every `i`,

\[
 P_i\cup Q_i=C+a_i+a_{i+1}+c=P_i\cup Q_{i+1},
\]

so the upper q1 colour is fixed edgewise, not just as a multiset.

With `C'=C-1`,

\[
 L_i=C'+a_i+a_{i+1}.
\]

Therefore

\[
 R_i\cap L_i=C'+a_i,
 \qquad
 R_{i+1}\cap L_i=C'+a_{i+1}.
\]

The three q2 colours are cyclically permuted.  At `Q_i`, the same lower row
`R_i` remains incident before and after the switch, so every other local
turn is unchanged.  This verifies exact global q2-multiset preservation
within any fixed exterior.

## 4. Rigid-cycle and topology scope

`P_0,Q_0` are consecutive cyclic `m`-intervals.  None of the other four
owners is: each has a hole between active labels.  Thus removing
`P_0Q_0` cuts the single-soliton cycle, and the two new incidences at its
exposed ends leave that owner set.

This alone does not rule out a larger cycle after splicing.  The source
correctly contracts the components of the old graph after the three edge
deletions and requires the three new links to form a forest.  That
criterion is necessary and sufficient whenever the affected old pieces
are forests.  The source does not assert that the canonical exterior
automatically passes it.

No q3, residence, or arbitrary-width preservation follows from these
local identities.  The stated scope is exact.
