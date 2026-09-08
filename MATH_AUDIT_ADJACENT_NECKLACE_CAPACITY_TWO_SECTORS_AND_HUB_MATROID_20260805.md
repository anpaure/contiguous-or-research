# Audit: capacity-two sectors and the hub partition constraint

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_CAPACITY_TWO_SECTORS_AND_HUB_MATROID_20260805.md`  
**Method:** residue, local-path, and path-parity replay; no search  
**Verdict:** PASS.

## 1. Residue replay

The allowed residues `4,5,0` are represented uniquely by digits `0,1,2`
in `H=6a+4+t`.  A one-unit boundary move stays allowed exactly when one
digit falls and its neighbour rises inside `[0,2]`.  This gives precisely
`01-10`, `12-21`, and the length-two path `02-11-20`.  The background
quotients do not change.  Since all discarded terms in the total are
even, the digit mass is odd.

## 2. Hub replay

For a fixed merged sum, increasing the left split by one produces the
three residue blocks shown in (2.3).  The reset from residue zero to the
next residue four jumps by four, so different blocks do not touch.

The hub map is many-to-one.  The two edges over `(21,4,6)` in (2.5) are
vertex-disjoint split blocks of the same merged part and coarsen to exactly
the same rooted word `(21,4,6)`.  Thus the partition-matroid correction is
necessary, not merely cautious wording.

## 3. Rooted matching replay

At one paired coordinate block, the fixed-sum graphs have orders
`1,2,3,2,1`.  Matching `02` to `11` leaves `20`; together with the two
singleton sums, the local critical set is `{00,20,22}`.  Every member has
even mass.  A tensor scan therefore has no critical state at odd total
mass when all coordinates are paired.

With one protected coordinate, the tensor critical pairs still have even
mass, forcing the protected digit to equal one.  This proves (4.2).

## 4. Special-path replay

For `q=3 mod 6`, shifting a `3 | (q-3r)` boundary gives macro parts
`3r+1` and `q-3r-1`.  Their residues are `(4,5)` for odd `r` and `(1,2)`
for even `r`.  Hence all critical exits have odd path index.

An internally matched path with externally removed vertices requires its
first removed index to be even.  Since no such direct critical exit
exists, the special odd path cannot be covered this way.  The small
`q=9,11` examples are consistent and are used only as warnings, not as a
computational proof.

For the one-product ear, the entry `(2s-1,0)` has odd parity in an
even-by-even grid.  A balanced two-vertex deletion therefore forces an
even-parity exit `(i,j)`.  Repairing both base residues necessarily changes
`(1,2)` to `(0,4,5)` and shifts the target expansion parity to `i+j-1`.
The target is an odd-by-odd product whose even shore is larger, so this
odd-parity entry is on the minority shore and cannot be its sole external
deletion.  This verifies Theorem 5.2's stated two-tail scope.

## 5. Scope audit

The theorem does not claim that the rooted matching descends through
rotations, that it is hub-rainbow, or that a folded circulation blossom
already supplies the missing special ear.  These are exactly the listed
open rows.
