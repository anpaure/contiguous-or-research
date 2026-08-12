# Audit: root-coded hub fan privacy

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ROOT_CODED_HUBS_GIVE_FAN_PRIVATE_RECEIVER_SHORES_20260805.md`

## 1. Literal state injectivity

For a 2-independent cut set `H`,

\[
 (x_H)_i=1+1_{i\in H}-1_{i-1\in H}.
\]

No two consecutive positions belong to `H`.  Hence `(x_H)_i=2` exactly
at the cut positions `i in H`.  The literal state recovers `H`, and a
rotation equality of states is exactly a rotation equality of cut sets.

This justifies using cyclic gap words in the quotient proof.

## 2. Workspace arithmetic

For `p` petals use starts `c_j=4+6j`, `0<=j<p`, in a gap of length
`W_0=6p+3`.

* the first start is four positions from the left boundary;
* the final right endpoint is
  `c_(p-1)+1=4+6(p-1)+1=6p-1`, four positions from the right boundary;
* consecutive starts differ by six.

Thus every endpoint cut has the required boundary clearance and distinct
petal blocks satisfy the split-block separation used by joint
admissibility.

## 3. Gap and slack count

There are `s` marker gaps, one workspace gap, and `k-s-1` ordinary gaps.
The marker sum is `4s+w`, the workspace has length `6p+3`, and ordinary
gaps have length three.  Therefore

\[
 (4s+w)+(6p+3)+3(k-s-1)
 =3k+s+w+6p.
\]

This verifies (3.4)--(3.5).  Since every marker code has the same number
`w` of entries equal to five, all codes lie in the same `(ell,k)` sector.

## 4. Quotient separation

Each receiver inserts exactly two cuts into the one workspace gap.  It can
therefore replace that gap by no more than three consecutive non-`3`
gaps.  The protected marker is an unchanged run of length `s>=4`; it is
the unique longest non-`3` run.

Any quotient collision must align the start of this run and preserve its
ordered word.  Different hub codes are separated.  For the same hub the
alignment is the identity rotation, after which literal square
disjointness separates distinct passive-pair tasks.

Thus both diagonal endpoint graphs of every one-per-fan selection are
matchings.  The claimed fan privacy is exact at the receiver-orbit level,
not merely at the occurrence level.

## 5. Bicircular rank formula

For an edge set `Y`, every tree component contributes `|V_C|-1` to the
bicircular rank and every component containing a cycle contributes
`|V_C|`.  Summing gives

\[
 r_B(Y)=|V(G_B(Y))|-\tau_B(Y),
\]

where isolated vertices are omitted and `tau_B(Y)` counts tree components
containing an edge.  Substitution into Edmonds' two-matroid formula gives
the exact loss cut (5.2).

## 6. Scope audit

The theorem proves an actual sector-local parent/anchor **design** under
the slack condition.  It does not prove:

1. that the canonical PBBS factor contains those hubs;
2. that arbitrary existing hubs can be re-rooted without changing their
   parent factor;
3. next-level augmented Hall/Tutte extension;
4. cross-level receiver regeneration;
5. upper/residence/common-cap preservation outside the local bank; or
6. an all-`k` additive bound.

No computation, enumeration, or solver was used.

