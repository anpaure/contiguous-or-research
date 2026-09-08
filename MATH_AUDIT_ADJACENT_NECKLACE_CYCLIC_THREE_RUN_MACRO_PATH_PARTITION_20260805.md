# Audit: cyclic three-run macro path partition

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_CYCLIC_THREE_RUN_MACRO_PATH_PARTITION_20260805.md`
  
**Method:** unique-factorization, path-order, and stabilizer audit; no
search  
**Verdict:** PASS.

## 1. Normal-form uniqueness

Away from the all-three word, every non-three gap uniquely terminates the
maximal run of threes immediately before it.  These runs partition the
cycle.  Collapsing `3^r,h` to `3r+h` is therefore canonical and
rotation-equivariant.

For fixed macro value `H`, the possible run lengths are exactly

\[
                    0\le r\le\lfloor(H-4)/3\rfloor.
\]

Changing `r` by one is one split/merge edge, so the factor is a path of
the asserted order.  Independent macroblocks give the Cartesian product.

## 2. Quotient audit

A rotation between two expansions must rotate their canonical macro bases,
so no identification lies outside the base stabilizer.  A stabilizer of
order `a` repeats the macro word `a` times, hence `a|q`; it is odd.  The
odd-group path-product theorem applies exactly.

## 3. All-three endpoint

For `q=3a`, the ordinary single-base expansions stop at `3^(a-2),6`.
Splitting the final six gives `3^a`, adding one endpoint and producing a
path of `a` vertices.  Since `q` is odd, `a` is odd.  No other macro fibre
contains the delimiter-free all-three word.

## 4. Residue audit

For `H=3u`, the local path length parameter is `u-2`; for residues one and
two modulo three it is `u-1`.  Requiring the path order `L+1` to be odd
gives exactly

\[
                              H=0,4,5\pmod6.
\]

The special divisible-by-three single base contributes residue three only
because of the extra all-three endpoint, exactly as separately stated.

An odd total of parts from residues `0,4,5` must contain an odd number of
five-residue parts.  At `q=15`, the ordinary list is
`(555),(4,5,6),(4,6,5),(4,11),(5,10)`, and the all-three attachment
contributes `(15)`.  The two orientations of `{4,5,6}` are distinct
modulo rotation, so this macro matching has six critical orbits.  The
four vertices in the earlier circulation calibration came from a
different vertical matching.

## 5. Scope

The theorem matches within each canonical macro fibre.  It does not assert
that the remaining critical macro bases already have a hub-rainbow
matching or that their blossom interiors are unoccupied.  The claimed
advance is the exact unrooted reduction to that smaller residue problem.
