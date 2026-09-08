# Independent audit: the canonical MSW common-history model has an absolute alternating upper portal hole

**Date:** 2026-08-13  
**Audited source:**
`MATH_OBSTRUCTION_CANONICAL_MSW_COMMON_HISTORY_HAS_ABSOLUTE_ALTERNATING_UPPER_PORTAL_HOLE_20260813.md`  
**Audited source SHA-256:**
`d250704102a482450127f589bef889087d734c7fb0118d993fb657756ea60379`  
**Verifier SHA-256:**
`41d1c194b2bab1d0292181b229c847e92aa05b2c497ffd606dc68ca558c58976`  
**Frozen replay SHA-256:**
`2dd82901cc6683c9d41a3a23f1e41eb7ab479aba5cf7b199e0c717e9d9c4112f`  
**Verdict:** **PASS.**

## 1. Owner words and provenance

Every word `a_x` in (1.2) has length `R=m+1` and underlying set
`U_m-{x}`.  The fixed roots in (1.3) and the moving-`00` roots in (1.4)
are Dyck words of semilength `m`.  Independent H100 replay of the exact
canonical `g/h` recurrence confirms that each displayed `a_x`, or its
reversal, is a cyclic interval of the corresponding tight row.  This is a
provenance check of the explicit roots, not a Catalan-factor enumeration.

The last line of (1.2) has the correct two boundary cases: for the smallest
even `e`, the `E_(<e)` block is empty, and for the largest it is the
`E_(>e)` block that is empty.  No length or endpoint exception appears at
`m=8`.

## 2. Depth-four states

For an ordered owner interval `a=(a_0,...,a_(R-1))`, the tight-row
history-letter rank at depth four is `s=R-4`.  A left-boundary occurrence
uses starts `1,...,4`, giving

\[
 P^L_j=\{a_{j+1},\ldots,a_{j+R-4}\},\qquad
 F^L_j=\{a_{j+1},a_{j+R-4}\}.
\]

A right-boundary occurrence uses starts `0,...,3`, giving

\[
 P^R_j=\{a_j,\ldots,a_{j+R-5}\},\qquad
 F^R_j=\{a_j,a_{j+R-5}\}.
\]

Thus (2.1)--(2.3) have the correct one-position offset and inclusive
endpoints.  All four independent orientation choices are tested.

Projecting the incompatibility condition onto
`C={0,1,4,5,8,9,10,11}` gives exactly the survivor table (2.4).  An
independent H100 census at `m=8,...,12` found:

* no survivor in the mixed orientations;
* in `(+,+)`, only `(e,10)` with `e` excluding the largest two evens;
* in `(-,-)`, only `(10,e)` with the same range; and
* no survivor at all for `m=8`.

For each nominal survivor, `e_*=2m-2` lies in the claimed forced set and
outside the opposite maximal set, so the full condition fails.  The
finite replay through `m=60` verifies the displayed symbolic boundary
classification; the proof remains the explicit boundary calculation.

## 3. Erosion and global consequence

The erosion identity is correctly indexed.  Applying `D^(d-4)` to a
shared block of `d` letters gives four letters

\[
 H'_i=\bigcup_{t=i}^{i+d-4}H_t,qquad1\le i\le4,
\]

and `D^4 D^(d-4)=D^d`.  Hence a literal depth-`d` port with `d>=4`
would produce the excluded literal depth-four port at the same oriented
boundary.

For the global corollary, a witnessing consecutive-owner interval whose
union is `U_m` can contain only rank-`R` subsets of `U_m`.  At the first
change between distinct owners, its two endpoints are necessarily
`U_m-{x}` and `U_m-{y}` for distinct `x,y`.  An old adjacency would already
witness `U_m`, contradicting canonical absence.  A new adjacency in the
stated rethreading model is paired at a literal common history and is
excluded by the portal theorem.  This argument covers arbitrary Euler
tours, repeated ports, and edge-dependent shared states.

The scope is exact: it excludes common-history successor rethreading of
the fixed canonical owner occurrence bank.  It does not exclude a prior
owner-changing incidence trade or an independently planted upper witness.

