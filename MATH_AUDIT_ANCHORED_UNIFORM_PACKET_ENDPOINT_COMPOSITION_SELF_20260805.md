# Self-audit: anchored uniform packet endpoint composition

**Date:** 2026-08-05  
**Method:** proof replay against the uniform joint-mixability criterion; no
search or solver  
**Audited theorem:**
`MATH_THEOREM_ANCHORED_UNIFORM_PACKET_ENDPOINT_COMPOSITION_20260805.md`  
**Verdict:** **GO.**

## Checks

1. Midpoint equality for `U[B,z]` and `U[a_i,B]` is exactly
   `sum a_i=z-(n-1)B`; no factor of two is missing.
2. Under that equality the sum of all `n+1` interval widths is
   `2(n-1)B`.  The job width is at most `(n-1)B` precisely when `z<=nB`,
   and every socket width is at most `B<=(n-1)B`.  Hence the uniform
   polygon condition is automatic and sufficient.
3. The canonical superlevel layers of a decreasing density on
   `[B,infinity)` are lower-anchored; those of an increasing density on
   `[0,B]` are upper-anchored.  Integrating packetwise joint mixes recovers
   the density barycenters exactly.
4. The transformed endpoint work row follows algebraically from outer
   work and count: `int(n-1)=S-J` removes exactly the anchor contribution.
5. A barycenter of upper-anchored interval uniforms is nondecreasing.
   Therefore the certified negative endpoint derivative of the Rayleigh
   socket density forces positive canonical layer mass off that anchored
   face.

Degenerate endpoint intervals may be treated as limits or Dirac uniforms;
they do not alter the criterion or the atomless Rayleigh application.  The
result is an equivalence only inside the stated canonical anchored-layer
ansatz, not for arbitrary coagulations.
