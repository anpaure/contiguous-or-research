# Self-audit: co-small base-safe q1 forbiddance

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_20260804.md`

No computation or search is used.

## 1. Forbidden-bank size and trace range

An owner with `h` coordinates in `K` can be chosen in

\[
 \binom{m-1}h\binom m{m-h}
\]

ways and has `m` lower facets.  Summing for `h<=2` gives `O(m^5)` even
without deduplication.

Every such facet has external trace at least `m-3`.  Under `d>=4`, low
noninterval traces have size at most `m-d-1<=m-5`, so they cannot hit the
forbidden bank.  Only the high greedy paths must avoid it.  Their
rank-`m-1` denominator is `2^(2m-o(m))`; multiplying by a polynomial
forbidden bank and by the path length still gives `2^(-2m+o(m))`, well
inside the frozen greedy union bound.  The adaptive critical-star owner
avoidance can retain the same fixed lower-resource exclusion.

## 2. Same-trace lemma

On a low sliding path, write
`ell=m-|T|-1>=d>=4` for the common length of the consecutive `K`-windows.
Two such windows at starting-distance `s` have union size
`ell+min(s,ell)`.  An owner with the same external trace contains only
`ell+1` `K`-coordinates, so `min(s,ell)<=1`; for distinct starts this
forces `s=1`.  Their union is therefore the intervening path owner.

On a high monotone geodesic, lower colours `L_t,L_s` have symmetric
difference `2|s-t|`.  Two facets of one owner differ by one exchange, so
again `|s-t|=1`, and their union is the intervening owner.  Exact external
trace separates different paths, so two same-trace protected facets always
come from this one path.  The implication `two => d_P(U)=2` is correct.

## 3. Owner aperture count

For an owner with external trace `S` and `h` `K`-coordinates:

* at most `m-h` protected facets arise by deleting an external coordinate,
  because their traces `S-e` are all different;
* at most two arise by deleting a `K`-coordinate, by the same-trace lemma.

Thus `z_U<=m-h+2`.  At `h>=4` this leaves at least two gaps.  At `h=3`,
an almost-full row requires both same-trace facets and is therefore a
protected-degree-two owner; a full row is impossible.

At `h<=2`, non-top paths avoid every facet of the owner.  The top palette
has trace lengths only `1,...,m-2`.  There is no contribution at `h=0`;
for `h=1,2`, there is at most one same-trace colour and at most two
external-deletion colours, because a cyclic interval complement can be
extended at only two endpoints.  Hence `z_U<=3`, far from almost full.

These cases prove `g_U>=1` and `g_U=1 => d_P(U)=2`, which are stronger
than the exact forced-bank base conditions.  Therefore `Omega_P(Z_P)=0`.

## 4. Scope

The refinement closes only the forced base bank.  It does not prove the
harmonic equality or the optional-bank inequality for every `B`.  All
previous reservoir properties survive because the only added resource
exclusion is polynomial.

## 5. Mechanical checks

At freeze time, display-math delimiter balance is zero, no hidden control
byte is present, and `git diff --check` reports no whitespace errors.
