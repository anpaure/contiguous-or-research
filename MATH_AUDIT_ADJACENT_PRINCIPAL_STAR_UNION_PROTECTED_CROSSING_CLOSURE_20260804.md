# Self-audit: adjacent principal-star union protected closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_PRINCIPAL_STAR_UNION_PROTECTED_CROSSING_CLOSURE_20260804.md`  
**Method:** second symbolic derivation.  No computation, search, or solver
is used.  
**Verdict:** author self-audit **GO**, pending independent review.

## 1. Fibre and cardinality audit

With `|H|=c-1` and `r=m-c`, an owner over `H` has `r+1` deletable
coordinates outside `H`.  With one pivot, one deletion destroys the last
pivot, giving fibre `r`; with at least two pivots, every outside deletion
is valid, giving `r+1`.

For two pivots the owner counts are

\[
                         2{m+r-2\choose r},\qquad
                         {m+r-2\choose r-1}.
\]

Writing `B=binom(m+r-2,r-1)`, inclusion--exclusion gives

\[
 |A|=2B+{m+r-2\choose r-2}
     ={2m+r-1\over m}B.
\]

The weighted owner contributions at fibres `r,r+1` are
`2(m-r)/m` and `2(m-r-1)/m`.  Substitution gives (1.7), and
`binom(m+r-2,r)=(m-1)B/r` gives (1.8).  At `r=1`, all owner multiplicities
are one or two, so capped mass is additive and `sigma=2(m-2)`.

## 2. Crossing identity audit

For `r>=2`, every selected owner fibre is at least two, so local protected
loss is the number of protected incidences leading to an unselected lower
facet.  A crossing owner edge gives one such incidence.  If both owners
are selected but their intersection is not, both contain `H`; adjacency
then forces their pivot sets to be two different singletons.  This is
exactly one pivot exchange and contributes both incidences.  No third case
exists.  Thus `lambda=boundary+2 swaps` is exact.

Ownerwise, every incidence lost by the union is lost by every individual
star active there.  Hence union loss on one path is at most the sum of the
two individual-star losses.  Each star is an interval on the path and has
at most two crossings, giving the sharp per-path bound four.  This
sharpens the original safe bound six.  A contributing low path
meets at least one principal star, giving the union bound `2H_r`; top and
high totals are `m,H_d`.  This verifies (2.2).

## 3. Safety regimes

For `r>=2`, nonzero fibres are at most `r+1`.  Since

\[
 {a-2\over a}\le {r-1\over r+1},
 \qquad
 \sum_Ua_U=m|A|,
\]

one gets

\[
                         \sigma\ge(2m/(r+1)-2)|A|.
\]

At `r<=m/10,m>=190`, the coefficient is at least 17; since
`|A|>=m+1`, this strictly dominates `15|A|+2m`.

For `r>=m/10`, the exact formula gives

\[
                         \sigma\ge {4\over m}
                         {m+r-2\choose r-1}.
\]

On `r<=m/2`, its ratio to `binom(m,r)` contains the exponential factor
`(1+(r-1)/m)^r`; on `r>=m/2`, its binary exponent is at least
`(3/2)H_2(2/3)>1`.  These dominate respectively
`H_r<=(r+1)binom(m,r)` and `H_r<=2^m`, as well as `m+H_d`.

At `r=1`, owner-by-owner comparison with the two singleton cuts shows
that only the shared degree-one protected endpoint can add one unit.
Thus `lambda<=21`, while `sigma=2m-4`.

## 4. Fixed-h audit

Outside `H` there are `R=m+r-h` residual nonpivot coordinates.  Choosing
`s` pivots and `r+1-s` residual coordinates gives the owner census; choosing
`s` pivots and `r-s` residual coordinates gives the lower-family census.

The same local domination bounds union loss by the sum of the `h`
individual-star losses.  Each is at most two on one path, giving the sharp
per-path bound `2h`; the former `4h-2` estimate was valid but loose.  For fixed
`h`, the `s=1` owner term retains the same exponential comparison, with
only polynomial/fixed factors changed.  The `r=1` singleton comparison
adds at most one endpoint discrepancy for each of the `binom(h,2)` shared
owners.

## 5. Scope verdict

The theorem closes exactly the scalar partial-colex obstruction and every
fixed-centre extension.  It does not address a growing number of centres,
arbitrary shifted sections, component distribution, or the common cap.
