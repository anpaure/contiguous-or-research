# Audit of the explicit connector rotation hyperstar

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_THREE_COMPONENT_C6_ROTATION_HYPERSTAR_20260805.md`  
**Method:** independent shape enumeration and skew-product replay; no
computation or search  
**Verdict:** **PASS** after the exact companion-voltage evaluation.  The
rotation family is component-rigid; physical-disjointness remains relevant
only for positional uses of several translates.

A two-peak Dyck word has four positive runs as in (1.2).  Parallel peak
deletion leaves one mountain only when the interior zero-run or interior
one-run has length one.  This yields the A/B list of size
`(m-1)+(m-1)-1=2m-3`.

Direct first-maximum complementation gives the shape cycle (1.4).  Its
voltage is one modulo `2m+1`, so the full `(m-1,1)` action sector is one
`f`-cycle and, by odd length, one `f^2` component.  The rotation identity
`rho=f^p=g^(p(m+1))` follows because

\[
 2p(m+1)-p=p(2m+1).
\]

Rotating the literal C6 preserves PBBS incidence, max-height selection,
common deletion, and q2 neutrality.  Therefore its triples are exactly
`{A_k,B_k,T}`.  The standard voltage lift gives orbit sizes
`gcd(v_A,n),gcd(v_B,n)`.  If an `f`-lift has even length, its two
`g=f^2` parity components are not interchanged by rotation: rotation has odd
order `n`, so its induced action on the two-element parity quotient is
trivial.  Hence the same gcd formula holds for each `g`-component orbit.

For the actual displayed states, normalization gives
`D_A=1^t0^t1010` and `D_B=1100 1^t0^t`.  Replaying the shape families
(2.8) and (2.11) yields periods `2t-1,2t-3` and voltages

\[
 (t-1)(2t+5)+1,
 \qquad
 (t-2)(2t+5)+2.
\]

Both are coprime to `n=2t+5`; both periods are odd.  Thus `A_k=A_0` and
`B_k=B_0` for every `k`.  All rotated connectors project to the same one
hyperedge `{A_0,B_0,T}`.  Any claim of a growing component-level hyperstar
from this rotation orbit would be false.

The rotated T-edge set is one residue class modulo `p`, so its cyclic gaps
are `p`.  Both rigid-cut arcs in (4.1) are longer than `p` for `m>=6`,
giving interior positions on both.  This is positional supply only: one
rotated connector touches only one of the two arcs, and its companions stay
on the same `A_0,B_0` cycles.  Nothing here proves a straddling connector,
disjoint physical supports, or global action-sector coverage.
