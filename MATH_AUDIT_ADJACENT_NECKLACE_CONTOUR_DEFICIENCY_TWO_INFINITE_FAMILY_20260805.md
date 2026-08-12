# Audit of the infinite cool-lex contour obstruction

**Date:** 2026-08-05  
**Audited file:**
`MATH_OBSTRUCTION_ADJACENT_NECKLACE_CONTOUR_DEFICIENCY_TWO_INFINITE_FAMILY_20260805.md`  
**Method:** independent orbit-type, parity, and literal-edge replay; no
search  
**Verdict:** **PASS.**

## 1. Top-call dictionary

For mass four the top necklace recurrence has the singleton concentrated
root and child suffixes `01`, `011`, `0111`.  Therefore the child index is
exactly the last part of the least weak-composition rotation.  The contour
order is root--`B3`--`B2`--`B1` up to reversal.

## 2. Orbit census

The positive-part types are exactly

\[
4,\quad3+1,\quad2+2,\quad2+1+1,\quad1+1+1+1.
\]

The theorem assigns them as follows.

* `3+1`: `h-1` to `B1` and `h-1` to `B3`.
* `2+2`: `h-1` to `B2`.
* `2+1+1`: `T(h-2)` to `B2`, the rest to `B1`.
* `1+1+1+1`: `binom(q,4)/q` to `B1`.

The counts sum to

\[
1+2(h-1)+(h-1)+\binom{q-1}{2}+{1\over q}\binom q4,
\]

which is exactly the elementary orbit census by positive-part type.

For the `2+1+1` type, direct comparison at tied longest zero gaps confirms
that the least rotation ends in 2 iff the gap following the 2 is at least
the other two gaps.  The two-range sum for `T(m)` and all three closed
forms expand correctly.

## 3. Parity

For `h=3 or 11 mod 12`, `h-1` and `binom(q-1,2)` are even,
`T(h-2)` is odd, and

\[
q^{-1}\binom q4=(h-1)(h-2)(2h-3)/6
\]

is odd.  Hence the child parity word is even--odd--even and the singleton
root is odd.

The root has only one edge in the contour.  Using it deletes the root of
an even block, leaving that block with odd order; not using it leaves the
singleton root unmatched.  Thus the even-order contour has no perfect
matching and deficiency at least two.  This argument does not assume
parity-completeness of any recursive child.

## 4. Small literal witness

For `q=5,b=4`, the child sizes are `6,5,2`.  The seven displayed pairs in
the theorem are disjoint and exhaust the fourteen necklaces.  In every
row, one unit moves across one edge of the cyclic five-slot graph; when a
rotation is used, it only restores the least representative.  Thus the
full graph has a perfect matching even though the canonical contour does
not.

## 5. Scope

The obstruction refutes only `mu_contour<=1`.  It does not refute the
near-perfect matching conjecture for the full adjacent-transfer necklace
graph, marked-port injectivity, or any PBBS halo-packing statement.
