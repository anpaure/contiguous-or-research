# Audit: root-coded PBBS owner planting and residual cuts

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ROOT_CODED_RECEIVER_BANK_PBBS_OWNER_PLANTING_AND_RESIDUAL_CUTS_20260805.md`

## 1. Hook-angle embedding

For a 2-independent `H subset Z_ell`,

\[
 u_H={\bf1}+\sum_{j\in H}(e_j-e_{j+1})
\]

has one `2` at each cut, one `0` immediately after it, and `1` elsewhere.
Its mass is `ell`.  Adding `c1` gives mass `(c+1)ell`, so it belongs to the
hook angle space `N_(ell,(c+1)ell)` when `ell=2h-1`.

The minimum digit is `c`; subtracting it recovers the cut state.  The
protected marker then fixes the cyclic root exactly as in the earlier
receiver audit.

For arbitrary `b>=2ell`, the theorem instead uses baseline `2` plus the
surplus at one protected quiet coordinate `z`.  At surplus one, `z` is the
unique value-three coordinate not followed by a value one; at larger
surplus it is the unique value at least four.  Aligning `z` and subtracting
the known baseline again recovers the cut state.  Thus no
occurrence/orbit substitution was made in either hook specialization.

For a fixed bank, let `Z` be the union of all possible cut-successor
coordinates.  Adding one chip on `Z` raises every possible cut-state zero;
the same ballast preserves all adjacent-transfer differences.  A further
root spike of size at least four is uniquely at least five, while one
travelling chip can make a nonroot coordinate at most four.  It roots every
cut and circulation state.  This verifies the sharper threshold
`b>=ell+|Z|+4`.

## 2. Positive predecessor and unique parent port

Every elementary edge of the counter-circulation route moves a
distinguished excess chip.  Removing that chip to form the common
predecessor `y` restores the underlying coordinate, whose value is at
least `c`.  No other coordinate falls.  Therefore `c>=1` implies
`y_i>=1` for all `i`.

The promoted-parent theorem inserts exactly two consecutive zeros and
retains every entry of `y`.  The new parent hence has one and only one
adjacent-zero pair.  A necklace rotation must align this pair, after which
deleting it recovers the rooted predecessor and cut.  Distinct rooted
child edges have distinct unmarked parent necklaces.

This argument is false at `c=0`: the predecessor may already contain
zeros.  The theorem records that boundary rather than using marked-port
injectivity as if it implied component separation.

## 3. Simultaneous owner and q2 support

A matching of rooted child edges uses disjoint child angle components.
Section 2 gives disjoint promoted parent components, and action level
separates every parent from every child.  The component triples of the
clean `C6`s are therefore disjoint.

Each old PBBS edge support and its unchanged q2 companion halo lie in that
triple.  Disjoint component triples imply disjoint owner occurrences and
disjoint q2 halos.  The clean switches commute, so their local zero q1/q2
currents sum to zero.  No small-protected-factor theorem or post-hoc
component-degree assumption is used.

## 4. Even proper-cut calculation

After root coding, each residual `B` endpoint-list edge belongs to a
different matching component.  Deleting `D=N(U)` leaves a two-list, a
singleton, or an empty list.  Only the empty list is deficient and each
contributes exactly one.  This verifies

\[
 \delta_B(U)
 =|\{j:A_j\cap U=\varnothing,\ B_j\subseteq D\}|.
\]

The opposite-diagonal certificate is also exact.  For the trapped jobs
let `X` be the union of their surviving `A` lists and
`E_*=N(X)-D`.  Privacy makes the lists disjoint and invisibility gives
`X cap U=emptyset`.  Applying Hall to `U union X` yields

\[
 |D|-|U|\ge |X|-|E_*|.
\]

Thus `|E_*|<=|X|-h_B(U)` is sufficient.  The root code does not imply
this exterior-neighbour inequality, so the proper-cut qualification is
necessary.

## 5. Odd quotient

The selected root marker makes its receiver orbit map injective, stronger
than generic odd-group pseudoforest descent.  Nevertheless an odd hook
sector is not bipartite.  The residual extension theorem is Tutte's
`o(G-S)<=|S|`, not Hall.  No claim in the theorem replaces blossom cuts
by the even proper-cut calculation.

## 6. Scope

The theorem closes every fixed finite rooted hook bank once
`b>=ell+|Z|+4`, and in particular the uniform family
`b>=2(2h-1)`.  It does not prove:

1. root-coded parent existence for every hook mass `b`;
2. a selected clean-C6 lift for every nonhook capacity-two background;
3. zero-ballast parent-port separation;
4. the even trapped-square inequalities for every proper Hall cut;
5. the odd Tutte inequalities;
6. cross-level receiver regeneration; or
7. any all-dimensional OR-word upper bound.

No computation or solver was used.
