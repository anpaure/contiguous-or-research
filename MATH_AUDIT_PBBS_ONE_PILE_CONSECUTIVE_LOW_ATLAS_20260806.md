# Audit of the one-pile consecutive low atlas

**Date:** 2026-08-06  
**Verdict:** **PASS**.

The one-pile composition has slot period `p=2d+1`, exactly `2d`
consecutive zero terminal occupancies, and one occupancy `b`.  On a zero
phase the hook formula gives a singleton mandatory core and decrements the
root by one.  Hence any `d` consecutive zero phases have literal core word

\[
                         r,r-1,\ldots,r-d+1.
\]

Repeating the same selected subblock once per slot period gives changed
blocks of length `d` separated by `p-d=d+1` unchanged cells.  This is
exactly within the mandatory-core short-gap theorem, including the cyclic
last-to-first junction.

The period root displacement is

\[
 -(2b+p)=-(2m-1)=2\pmod{2m+1}.
\]

Thus the `n` block starts enumerate all coordinates.  Prefixes of lengths
`1,...,d` yield all cyclic coordinate intervals in one fixed thinned word.

No claim is made for targets with multiple cyclic runs or for global
residence outside this component.
