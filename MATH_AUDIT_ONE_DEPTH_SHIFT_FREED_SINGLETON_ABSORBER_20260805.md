# Self-audit: one-depth shift and the freed-singleton absorber

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ONE_DEPTH_SHIFT_FREED_SINGLETON_ABSORBER_20260805.md`  
**Method:** independent symbolic replay inside the same pure-mathematical
lane; no computation, search, or solver  
**Verdict:** SELF-GO for the complete anonymous two-SCD system and for the
stated coherent-boundary variant.  Named containment and the depth-`D`
fractional premise remain open.

## 1. Adjacent-depth arithmetic

At old collar bottom `t=r-D`, a residual bottom `b` has length `t-b` and a
collar bottom `t+u` has capacity `u`.  At new bottom `t-1`, these become
`t-b-1` and `u+1`.  Bottom `t-1` jobs had old length one and no new cell,
while bottom `t` collar chains are genuinely new capacity-one sockets.  The
proof ignores the latter, so no double counting occurs.

The punctured bottom-zero chain loses one terminal nonempty rank just like
every other surviving job.  It creates no singleton exception at the top
boundary.

## 2. Extreme-point and occurrence accounting

The cited basic-support theorem leaves at most `D` fractional old jobs.
All remaining configurations satisfy the old tail bounds and hence admit
one injective assignment to labelled old socket occurrences.  This
assignment is fixed before the shift.

There are only `D` endpoint-triangle occurrences.  Deleting every integral
job which touches one removes at most another `D` jobs.  Hence every
transported assignment is supported on the collar SCD, where the same
occurrence has capacity increased by one.  This avoids treating an
abstract endpoint socket as if it had a same-chain successor.

Shortening the terminal piece of every surviving integral job never adds a
socket and never increases a piece.  Every old socket occurrence gains one
unit of capacity.  Thus the same occurrence assignment remains valid.

An integral length-one job has exactly one positive piece and therefore
exactly one occupied socket.  Different such jobs had different sockets.
After their disappearance those occurrences are pairwise distinct, are
disjoint from every retained assignment, and have capacity at least two.
At most `D` length-one jobs were fractional and at most `D` more were
discarded with the endpoint-touching family, giving the lower bound
`H_(t-1)-2D` exactly.

## 3. Absorption count

At most `2D` new jobs remain.  Their maximum length is `t-2`: the old
nonempty maximum was `t-1`, and every surviving job loses one.  Pieces of
length two plus at most one singleton use at most

\[
                         \left\lceil{t-2\over2}\right\rceil
\]

sockets per job.  Every freed occurrence has capacity at least two, so
(2.1) is sufficient with no type or scalar assumption beyond the displayed
count.

Finally `D=Theta(sqrt r)`, `t=Theta(r)`, and
`H_(t-1)=Theta(W/sqrt r)`.  The left side is exponential and the required
bank polynomial, proving the eventual corollary.

## 4. Scope audit

The theorem does not assume that fractional jobs have occurrence
assignments; they are discarded before the integer packing and absorbed
after the shift.  It does not reuse any freed socket.  It does not infer
named containment from capacity, and it does not claim that arbitrary
triangular deletions commute with the depth shift.

The conclusion is therefore exactly an anonymous integral fragmentation
at `D+1`, conditional on fractional feasibility at `D`.  **SELF-GO.**
