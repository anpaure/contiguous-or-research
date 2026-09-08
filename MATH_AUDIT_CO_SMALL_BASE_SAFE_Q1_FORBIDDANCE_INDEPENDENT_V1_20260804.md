# Independent audit V1: co-small base-safe q1 forbiddance

**Date:** 2026-08-04  
**Verdict:** **GO** after the corrected sliding-window calculation.  No
computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_20260804.md`,
SHA-256
`c17615960cf7a9ff551125d72b69849b97181b41e1cd234d8a3b58820d7faf7a`.

Author self-audit:
`MATH_AUDIT_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_SELF_20260804.md`,
SHA-256
`b35140999dd21b9c48c0e4e2a683dc2fdb95150145d6d52cdf5c85add56bfa9a`.

## 1. Polynomial forbidden bank and trace separation

An owner with exactly `h` coordinates in `K` can be chosen in

\[
 {m-1\choose h}{m\choose m-h}
\]

ways and has `m` lower facets.  Summing this over `h=0,1,2` gives the valid
overcount `O(m^5)` for `F_(<=2)`.

Every facet of such an owner has external trace at least `m-3`: deleting a
`K` coordinate leaves trace size `m-h`, and deleting an external coordinate
leaves `m-h-1`.  A low noninterval path has trace size at most

\[
 m-d-1\le m-5
\]

under `d>=4`, so no low path can meet the new forbidden bank.  The fixed
bank must only be added to the high-tail avoidance ledger.

Its polynomial size is negligible relative to the high geodesic
rank-`m-1` resource denominator `2^(2m-o(m))` and to the already tolerated
`2^(m+o(m))` adaptive resource bank.  Thus the high greedy and
spread-preserving choices retain all previously proved disjointness,
residence, singleton, and endpoint properties.  Only deterministic top
lower colours may remain in the forbidden family, proving (1.1).

## 2. Same-trace two-facet lemma

On a low sliding path, let

\[
 \ell=m-|T|-1\ge d\ge4
\]

be the common length of the consecutive `K`-windows.  Two windows at start
distance `s` have union size

\[
 \ell+\min(s,\ell).
\]

An owner with the same external trace has only `ell+1` `K` coordinates.
Therefore two distinct lower colours can fit in it only when
`min(s,ell)<=1`, which forces `s=1`.  Their union is the intervening owner.

For a high monotone geodesic, lower colours `L_t,L_s` have symmetric
difference `2|s-t|`.  Two facets of one owner differ by one exchange, so
again `|s-t|=1`, and their union is the intervening owner.

Exact external trace assigns all non-top colours of one trace to one path.
The deterministic top lower palette is itself simple by exact trace.  Hence
two same-trace protected facets of one owner are consecutive incidence
colours at that owner, forcing its protected degree to be two.

## 3. Forced-bank aperture count

Fix an owner `U`, let `S=U cap E`, and put `h=|U cap K|`.  Deleting an
external coordinate gives at most `m-h` protected facets, one for each
distinct trace `S-e`.  Deleting a `K` coordinate gives same-trace facets,
of which the preceding lemma allows at most two.  Therefore

\[
 z_U\le m-h+2.
\]

For `h>=4`, this gives `z_U<=m-2`.  For `h=3`, a row with
`z_U=m-1` must use both same-trace facets, so `d_P(U)=2`; a full row is
impossible.

For `h<=2`, every non-top path avoids all facets of `U`, leaving only the
top palette.  Its trace lengths are `1,...,m-2`.

* At `h=0`, traces `S` and `S-e` have sizes `m` and `m-1`, so none occurs.
* At `h=1`, no same-trace top colour occurs, and at most two external
  deletions extend the fixed one-point complement to a cyclic two-interval.
* At `h=2`, at most one same-trace colour occurs, and at most two external
  deletions extend the fixed two-point complement to a cyclic three-interval.

Thus `z_U<=3<m-1` in this range for sufficiently large `m`.

The three cases prove

\[
 g_U=m-z_U\ge1,
 \qquad
 g_U=1\Longrightarrow d_P(U)=2.
\]

## 4. Base co-small load

In the exact co-small optional-bank formula, `B=emptyset` leaves
`b_U=0`.  A contribution to `Omega_P(Z_P)` could arise only from a full
forced clique `g_U=0`, or from an almost-full unprotected clique
`g_U=1,d_P(U)=0`.  The two aperture conclusions exclude both cases.
Therefore

\[
 \Omega_P(Z_P)=0.
\]

This closes precisely the forced-base row.  It does not control optional
gap saturation for arbitrary `B` or prove the harmonic balance condition.

The independent V1 verdict is **GO** at the corrected hashes above.
