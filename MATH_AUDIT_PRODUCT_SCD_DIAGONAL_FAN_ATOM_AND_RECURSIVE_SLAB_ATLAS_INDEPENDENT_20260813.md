# Independent audit of the corrected product-SCD diagonal-fan slab atlas

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_PRODUCT_SCD_DIAGONAL_FAN_ATOM_AND_RECURSIVE_SLAB_ATLAS_20260813.md`  
**Source SHA-256:**
`8b95c4784472bc7918ca0a2d83dd050ada7a37047bc808356e1a85e3c38206d3`  
**Audited verifier:** `verify_product_scd_diagonal_slab_fan_atlas.py`  
**Verifier SHA-256:**
`f254a737107289f2551d3c3cd4f361edf953abee1a4c0a90e5c83e366f40838d`  
**Verdict:** PASS at the stated standalone-atlas scope.

## 1. Exact fan atom

The fan word is

\[
                         K,X_{A-1},\ldots,X_1,Y_1,\ldots,Y_{B-1}.
\]

Axis cells use one source letter.  For `i,j>0`, the interval from `X_i`
through `Y_j` contains exactly `i+j` letters and has union

\[
                         C_{i_0+i}\cup D_{j_0+j}.
\]

The two product-chain coordinates recover `(i,j)`, so the assigned
intervals are distinct.  The corrected mixed width is exactly `i+j`, not
`i+j+1`.  Therefore a truncated radius-`s` fan is deadline-safe precisely
under `(2.6)`.

## 2. Slab dimensions and terminal fan

With `B=d+2-A`, a full `A` by `B` rectangle has maximum mixed width

\[
                         (A-1)+(B-1)=d.
\]

The last shortened row slab has height `a_x<=A`, so it remains safe.  The
full-rectangle inequality `(4.6)` is exactly the condition that its
top-right cell lies in the radius-`s` downset.

After `q` rectangles, put `y=qB` and `z=s-x-y`.  If the next rectangle
fails because of the diagonal, then

\[
                         z<a_x+B-2\le d.
\]

If it fails because fewer than `B` columns remain, the residual fan has
dimensions at most `a_x` by `B-1`, hence maximum mixed width at most
`a_x+B-3<=d-1`.  Thus the terminal fan in either failure mode is
deadline-safe.  It covers exactly all remaining local cells satisfying
`i+j<=z`.

## 3. Recursive stop

When no full rectangle was placed, `(4.10)` is

\[
 \min\{s-x,(a-x-1)+(b-1)\}\le d,
\]

which is the maximum attainable local sum in the entire residual product
downset.  One fan rooted at `(x,0)` therefore covers all later slabs, so the
recursive stop is exact.  Otherwise removing the first `a_x` rows
translates the remaining radius from `s` to `s-a_x`, exactly as in `(5.7)`.

The formula for `q` in `(5.2)` counts precisely the number of full
rectangles: `qB<=b` is the column condition, and
`a_0+B-2+(q-1)B<=s` tests the last top-right corner.  Equations
`(5.3)--(5.7)` therefore replay the constructive slab proof without an
off-by-one discrepancy.

## 4. Empty rank-zero core

The only empty core has global indices `(u,v,i_0,j_0)=(0,0,0,0)`.  Any
rectangle or fan rooted there has every value of global rank at most `d`,
because its maximum local sum is at most `d`.  Assigned deep targets have
rank at least `d+1`.  Hence omitting the entire empty-core atom loses no
assigned target.  It can only shorten the constructed word; padding by an
arbitrary nonempty source letter restores the charged upper-bound length
if desired.

## 5. Global product-SCD sum and remote replay

Product-SCD grids partition the Boolean lattice, so choosing one marked
interval for each active cell supplies every deep target once in the
assignment, even though extra shallow values may repeat across atom words.
Concatenating physically disjoint atom words cannot erase an assigned
interval.

The verifier implements `(5.1)--(5.9)` literally.  I reran the eight table
instances on `h100`; the returned ratios agree with `(6.1)` to all printed
digits:

\[
 0.8660069177,\ 0.9083389153,\ 0.9310649027,\ 0.8807843896,
\]

\[
 0.9372249057,\ 0.9308045060,\ 0.9603361153,\ 0.9727518967.
\]

## 6. Scope

This is an exact standalone deep-source atlas and a valid finite recurrence.
The table is not an eventual coefficient-one proof, and the construction
does not yet embed its words in one rank-middle owner chronology.  The
source states those two remaining gates explicitly; no stronger conclusion
is imported by this audit.
