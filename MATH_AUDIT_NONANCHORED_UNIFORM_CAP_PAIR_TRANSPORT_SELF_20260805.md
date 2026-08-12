# Self-audit: nonanchored uniform-cap pair transport

**Date:** 2026-08-05  
**Method:** proof replay against uniform joint mixability and compact
measure separation; no search or solver  
**Audited theorem:**
`MATH_THEOREM_NONANCHORED_UNIFORM_CAP_PAIR_TRANSPORT_20260805.md`  
**Verdict:** **GO.**

## 1. Local packet

Midpoint equality for `J=[B,z]`, `C=[a,d]`, and `A=[c,B]` forces
`c=z-a-d`.  Under this identity their width sum is exactly `2d`.  Requiring
the job and anchor widths to be at most `d` gives respectively
`z<=B+d` and `z>=B+a`; the cap width is automatically at most `d`.
These inequalities also put `c` in `[B-d,B-a]`.  Hence the criterion is
both necessary and sufficient, with no missing support row.

The midpoint choice `z=B+(a+d)/2`, `c=B-(a+d)/2` lies in the legal
interval because `a<=(a+d)/2<=d`.

## 2. Measure lift

A cap transport uses exactly one cap layer, one dominated job layer, and
one dominated anchored socket layer per packet.  Uniform layer barycenters
therefore give the intended literal marginals, and packetwise equality of
sums preserves first moment after subtraction.  No count or Jacobian
factor is missing.

The proof needs only an exact interval-uniform barycenter representation,
not the nonlinear canonical decomposition of the unsplit density.  It
therefore applies without change to the future-minimum representation
obtained by separately decomposing `h` and `k`.

## 3. Dual

The legal cap/job relation is compact after restricting job endpoints to
`[B,2B]`.  Measures with fixed cap marginal form a compact convex set, as
does the coordinatewise domination target.  A separating functional is a
pair of continuous resource prices.  Replacing either by its positive part
preserves a strict separator because the target is downward closed and
resource measures are positive.  Minimization over the legal interval of
`z` gives exactly `Xi_(phi,psi)`.  Thus the displayed price family is
complete, not merely necessary.

## 4. Scope

The theorem solves joint mixability *inside* every cap packet and gives an
exact criterion for simultaneous resource use.  It does not verify that
criterion for the Rayleigh layer measures.  Even after cap transport, the
remaining anchored endpoint-composition problem must still be solved.

## 5. Uniform-spreading kernel

For one cap interval `[a,d]`, selecting `x` uniformly and setting
`z=B+x`, `c=B-a-d+x` stays on the exact legal packet relation.  Multiplying
the conditional density `1/(d-a)` by the canonical layer mass
`(d-a)dt` cancels the interval length.  Tonelli then gives job demand
`k(z-B)dz`.  Reflection `x -> a+d-x` preserves uniform measure on the
same interval and gives anchor demand `k(B-c)dc`.

For anchored superlevel layers, differentiation of the barycenter
identities gives `dLambda_f=-(z-B)f'(z)dz` and
`dLambda_anc=(B-c)h'(c)dc`; the signs and endpoint factors are correct.
Therefore the two displayed pointwise inequalities are valid sufficient
domination tests.  They are not asserted necessary, since the full cap
transport may route `z` non-uniformly.
