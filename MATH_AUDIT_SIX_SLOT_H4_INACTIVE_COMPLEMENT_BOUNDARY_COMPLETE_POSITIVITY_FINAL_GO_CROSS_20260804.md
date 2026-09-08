# Independent GO audit: six-slot `h=4` inactive complement boundary

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_INACTIVE_COMPLEMENT_BOUNDARY_COMPLETE_POSITIVITY_20260804.md`  
**Audited SHA256:**
`6df92f87cad113a2d26f3405e2ce51285a91f3d1865fb092b2d0fecc40a04e45`

## Verdict

**PASS / GO in the exact stated scope.**  On `u=A-P`, the domain gives
`P>=4A/5`, while the original lower bound gives `P>=2tau/3`; both `P` and
`A` therefore lie in the range of the independently verified brace bound

\[
H_\tau(w)=C(\tau)+F_\tau(w)>{11\over20000}.
\]

For fixed `w`, increasing the period moves every negative tail away, so
`F_tau(w)>F_A(w)`.  With `a=A-P`, Jacobi reflection consequently gives

\[
F_\tau(a)+F_\tau(P)>
F_A(a)+F_A(A-a)=\rho(a)>-{1\over20000}.
\]

If the low minimum is `C(tau)`, the gate is bounded by

\[
H_\tau(P)+H_\tau(A)-{1\over20000}
>{21\over20000}.
\]

If the low minimum is `F_tau(a)`, it is bounded by

\[
H_\tau(A)+F_\tau(P)+F_\tau(a)-{1\over20000}
>{9\over20000}.
\]

The two cases exhaust the low minimum and include its switch.  Together
with the closed active-side predecessor they close the complete complement
boundary.  The result does not sign the interior of `u=P/4`, the moving
boundary `P=2tau/3`, or the remaining low-switch face.  No broader
six-slot positivity claim is made.
