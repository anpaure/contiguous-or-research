# Self-audit: compressed two-star named-bulk obstruction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_COMPRESSED_TWO_STAR_NAMED_BULK_RADO_COUNTEREXAMPLE_20260805.md`  
**Method:** exact symbolic replay; no computation, search, or solver  
**Verdict:** **GO.**

## 1. Star arithmetic

For a fixed two-set `A`, the rank-`r-1` and rank-`r` stars have sizes

\[
 Y=\binom{2r-2}{r-3},
 \qquad
 U=\binom{2r-2}{r-2},
 \qquad
 {Y\over U}={r-2\over r+1}.
\]

Thus `U-Y=3U/(r+1)`.  With `W=binom(2r,r)`,

\[
 {U\over W}={r-1\over2(2r-1)},
 \qquad
 H_r={W\over r+1}.
\]

Therefore

\[
 H_r-(U-Y)
 ={W\over2(2r-1)}
 ={1\over r}\binom{2r-2}{r-1}
 =\operatorname{Cat}_{r-1}.
\]

All equalities in the obstruction ledger are exact.

## 2. Neighbourhood check

The upper neighbourhood of all rank-`r-1` sets containing `A` is exactly
the rank-`r` star containing `A`.  Every request top also contains `A`, so
every request neighbour lies in that same star.  Consequently the combined
left family has `Y+H_r` vertices but only `U` neighbours, with Hall deficit
`Cat_(r-1)>0`.

The request tops are distinct rank-`s` sets, and each request is a singleton
chunk, so no repeated target or hidden multiplicity is used.

## 3. Low-rank supply check

For `s=r-D-2`, the number of rank-`s` tops containing `A` is

\[
 \binom{2r-2}{r-D-4}.
\]

Relative to `binom(2r-2,r-1)`, its ratio is

\[
 \prod_{j=0}^{D+2}{r-1-j\over r+j}.
\]

With `D=Theta(sqrt(r))`, the sum of the logarithmic losses is
`O(D^2/r)=O(1)`, while every factor is positive eventually.  Hence the
ratio is bounded below by a positive constant.  This supply is
`Theta(W)>W/(r+1)=H_r` for all sufficiently large `r`.

## 4. Scope check

If `p<=r` owner starts are reserved first, replacing `H_r` requests by
`H_r-p` changes the exact Hall deficit from `Cat_(r-1)` to
`Cat_(r-1)-p`, which remains positive eventually.  Since the selected top
rank has `C_s=Theta(W)>H_r`, this partial class contains zero complete
rank-`s` batches.  Maximal complete-orbit extraction therefore leaves the
whole saturated remainder.  The same calculation covers the fewer-than-
`r` maximum-start reserve from the one-depth insurance theorem.

The construction refutes only an automatic theorem for every fixed naming
and prescribed rank-`r` socket class.  It does not prove that the actual
anonymous interval histogram forces this compressed naming, nor that no
co-chosen spread naming satisfies Rado.  The source states this distinction
explicitly.  Audit verdict: GO.
