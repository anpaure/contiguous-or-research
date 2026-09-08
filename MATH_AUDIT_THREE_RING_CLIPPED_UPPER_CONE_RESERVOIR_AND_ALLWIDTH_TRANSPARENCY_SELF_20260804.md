# Self-audit: three-ring clipped upper-cone reservoir

**Date:** 2026-08-04  
**Method:** proof audit only; no computation, search, or solver  
**Verdict:** `GO` as a protected-bank and conditional-transparency theorem.
It does not assert the remaining joint factor/cap extension.

## Checks

1. The damage cone has one common rank-`(m-1)` core `K=B+b`; every trace
   contains one of the three ring pairs.
2. The only size-two traces are the seam bases, and the three old/new ring
   upper colours permute them exactly.
3. A low shortened path has rank `m`, exact external trace, simple immediate
   palettes, union `K+T`, and internal run length `m-|T|>=d+1`.
4. Distinct low traces cannot collide.  Ring resources have external trace
   of size at most two, so they cannot collide with low paths.
5. The high tail has `2^o(m)` targets.  Its symmetric geodesic resource
   probabilities and `2^(2m-o(m))` binomial supply are the exact estimates
   used in the audited hybrid-reservoir theorem.  Adding three ring paths
   changes only the negligible forbidden constant.
6. Monotone high geodesics have no internal positive run; the size-two
   ring paths have only clipped endpoint runs.
7. The arbitrary-width conclusion is conditional on literal planting of
   the whole protected bank.  It does not use sublinearity as a substitute
   for protected Ore--Ryser extension.
