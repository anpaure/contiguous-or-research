# Independent self-audit: the PBBS max-height q1 section is q2-complete

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_MAX_HEIGHT_Q1_SECTION_IS_Q2_COMPLETE_20260805.md`  
**Method:** a second symbolic derivation from the deficit-three and
deficit-five parenthesis decompositions; no computation or search  
**Verdict:** **GO**.

## 1. Alignment of the two occurrence conventions

For a q1 target `K`, the first-shadow construction chooses a maximum-height
deficit-three block preceded by `z`, lets `w` be the down-step after its
rightmost maximum, and proves

\[
 f(K+w)=f^{-1}(K+z).
\]

Thus the chosen occurrence is the centered edge with endpoints `K+w` and
`K+z`.  For a q2 centre `A`, the incoming and outgoing centered edges have
centres `f^{-1}(A)` and `f(A)` and endpoints

\[
 f^{-2}(A),A\qquad\hbox{and}\qquad A,f^2(A).
\]

These conventions agree exactly; there is no hidden reversal.

## 2. Incoming block check

For the deficit-five target `D`, choose the maximum block `D_0` and the
down-step `u` after its rightmost maximum.  With `A=D+z_0+u`, the incoming
q1 colour is `K_-=D+u`.

After flipping `u`, the proposed block

\[
 E_0=D_0^\uparrow 0_{z_1}D_1 0_{z_2}D_2
\]

has total height zero and nonnegative prefixes.  Its maximum is exactly
`H+1`: the flipped step reaches it, the later part of `D_0` cannot exceed
it because the old rightmost `H` has already passed, `D_1` runs at baseline
one, and `D_2` at baseline zero.  The exterior blocks `D_3,D_4` have height
at most `H`.  Hence `E_0` is uniquely tallest and its predecessor is
`z_0`.  The selected q1 edge contains `K_-+z_0=A`; the occurrence identity
then forces it to be the incoming edge.

## 3. Outgoing block check

For `K_+=D+z_0`, the block

\[
 E_4=D_4 1_{z_0}D_0 0_{z_1}D_1
\]

is Dyck and uniquely reaches height `H+1`.  Its rightmost maximum is the
rightmost maximum of `D_0`, because `D_4,D_1` run at baseline zero and the
part of `D_0` after `u` never returns to height `H`.  Thus its q1 down-step
is precisely `u`, so the selected q1 edge contains `K_++u=A` and is the
outgoing edge.

The argument is immune to all maximum-height ties in the global q1 rule:
the two induced deficit-three words each have a **unique** tallest block.

## 4. Boundary and scope checks

For `m=2`, the word `01100` has adjacent q1 colours `{2}` and `{1}` at
`A={1,2}`.  Each singleton deficit-three word has one nonempty `10` block,
and the q1 rule selects the incident edge at `A`.  This covers the sole
empty q2 target.

The theorem selects exactly one occurrence per q1 target because that is
how the rule is defined; it does not claim uniqueness of the occurrence or
of the tallest block.  The theorem proves section compatibility on the
whole PBBS two-factor.  It correctly leaves unproved whether the complement
of the section intersects every factor component.  No Hamilton-cycle,
residence, q3, or compiler conclusion is inferred.

The exact scalar ledger at that final gate is

\[
 |\overline S|={2m+1\choose m}-{2m+1\choose m-1}
 =\operatorname {Cat}_{m+1},
\]

whereas the PBBS component count is at most `Cat_m`.  An earlier draft used
`Cat_m` for both quantities; that indexing typo is corrected in the audited
source and does not affect the section construction.
