# Audit of the future-overlap Gram/Bessel reduction

**Date:** 2026-08-06  
**Verdict:** PASS as an algebraic reduction; final aggregate estimate
(ABESSEL) remains open.

## Checks

1. From \(u_N+m_N=n_E+n_F\) and \(u_S+m_S=s_E+s_F\),

   \[
   \xi_E\xi_F r^{m_N}r_s^{m_S}\rho^{-u_N}\rho_s^{-u_S}
   =(\xi_E\rho^{-n_E}\rho_s^{-s_E})
    (\xi_F\rho^{-n_F}\rho_s^{-s_F})
    (r\rho)^{m_N}(r_s\rho_s)^{m_S}.
   \]

   Thus Proposition 1.1 has the correct non-slot and slot exponents.

2. For every resource coordinate,

   \[
   1+(a-1){\bf1}_{\{u\in E\cap F\}}
   \]

   is a rank-two positive-semidefinite kernel. Their Schur/tensor product
   is \(a^{m_N}b^{m_S}\). Nonnegative diagonal weights and principal
   compression preserve positivity.

3. The Boolean union identity \(e+f-ef\) gives three carrier assignments
   per mark and nine assignments for \(z_A(x)\chi_A(y)\). A monomial is
   an inner product of two atomic feature sums. Marks assigned to both
   constituents occur on both feature vectors, not as an untracked
   multiplicity.

4. If the blocker mark is on both feature vectors, adding and subtracting
   the mixed term gives exactly two differences. Bessel bounds each by a
   product of one ordinary norm and one marked-difference norm. No factor
   depends on the number of roots \(Q\), because the sum over \(Q\) is
   represented in a Hilbert direct sum before Cauchy--Schwarz.

5. Every resulting ordinary norm has zero, one, or two distinct marks.
   Hence it maps to an unmarked rooted moment, a one-entry rooted moment,
   or a marked size-two role pattern. This is the precise reason the
   four-atomic termwise expansion is unnecessary.

6. A difference norm is not deletion-monotone. For vectors \(u,v\) with
   positive Gram entries, deleting a coordinate can remove a negative
   contribution from \(\|u-v\|^2\). The unsigned inequality
   \(\|u-v\|^2\le2\|u\|^2+2\|v\|^2\) is deletion-safe but may lose the
   required aggregate scale. The theorem correctly retains this as the
   final fork rather than claiming a stopped estimate.

7. The rank-one one-completion example confirms that the dimension-free
   local bound \(\Gamma_A=O(1)\) alone cannot supply the missing inverse
   powers of \(d\).

8. Inserting (MCAP-alpha) into (ABESSEL) leaves the prefactor
   \(d^{2-\alpha}\), which is exactly cancelled by (MDIR-alpha).

9. The pair-stop mismatch is exact. The stop controls an un-tilted
   two-resource rate, whereas the needed ratio (10.3) is conditioned on
   one atomic completion and tilted by the future-overlap kernel. The
   exceptional-completion construction has raw marked share \(O(d^{-1})\)
   but kernel-tilted common-mark share \(1-o(1)\).

10. Proposition 7.1 has the factor \(\binom j2\), so a one-hit transition
    is absent from its ledger. Such a transition can create a nonzero
    marked feature difference. Hence the proposition cannot, without an
    additional service argument, imply the occupation row (MDIR1).

## Scope

The audit validates the exact coefficient factorization, slots, finite
mark-role enumeration, Bessel reduction, stopping distinction, and the
formal implication (MCAP-alpha)+(MDIR-alpha) to ANG4. It does not validate
those two aggregate rows for the authenticated stopped process.
