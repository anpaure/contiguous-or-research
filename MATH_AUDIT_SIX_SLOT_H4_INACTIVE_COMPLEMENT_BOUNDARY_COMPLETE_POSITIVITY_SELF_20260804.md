# Self-audit: inactive complement boundary

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_SIX_SLOT_H4_INACTIVE_COMPLEMENT_BOUNDARY_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA-256:**
`6df92f87cad113a2d26f3405e2ce51285a91f3d1865fb092b2d0fecc40a04e45`  
**Verdict:** **SELF-AUDIT GO.**  The two low branches and both rational
margins replay exactly.  This is not an independent audit.

## 1. Geometry and transport

On `u=A-P`, put `a=A-P`.  The domain constraint `u<=P/4` gives
`P>=4A/5`; the original lower constraint still gives `P>=2tau/3`.
Therefore both `P` and `A` are legal inputs to the frozen bound

\[
                         H_\tau(w)>{11\over20000}.
\]

For every fixed shift, period monotonicity has the correct strict
direction:

\[
                         F_\tau(w)>F_A(w).
\]

Jacobi reflection at the complementary shifts `a` and `P=A-a` then gives

\[
 F_\tau(a)+F_\tau(P)
 >F_A(a)+F_A(P)=\rho(a)>-{1\over20000}.
\]

No train is counted twice in this comparison.

## 2. Low-branch ledger

If the low minimum is `C(tau)`, the gate is

\[
 H_\tau(P)+H_\tau(A)-{1\over20000}
 >{21\over20000}.
\]

If the low minimum is `F_tau(a)`, the gate is

\[
 H_\tau(A)+F_\tau(P)+F_\tau(a)-{1\over20000}
 >{11-1-1\over20000}={9\over20000}.
\]

These two cases include equality at the branch switch.  Thus the weaker
uniform margin `9/20000` is valid on the whole inactive complement face.

## 3. Scope

The active predecessor includes its switch, so combining the two results
closes the full complement boundary.  The only `P=4A/5` point closed by
this theorem is the geometric junction `u=A-P=P/4`; no claim is made for
smaller `u` at that value of `P`.

