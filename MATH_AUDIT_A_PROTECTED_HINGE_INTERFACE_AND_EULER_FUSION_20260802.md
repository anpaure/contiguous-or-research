# Audit of the protected hinge one-copy and Euler-fusion theorem

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_A_PROTECTED_HINGE_INTERFACE_AND_EULER_FUSION_20260802.md`,
SHA-256
`7e073e470b65462679493248f9050c844409fdaddcffa7f669b24c08711dc6ff`.

## Verdict

PASS in its stated completed-interface scope.  The theorem is an exact
min--max/physical-lift implication; it does not assert that the required
Cartesian protected packet atlas exists in the Boolean construction.

The lightweight verifier
`scratch/audit_a_protected_hinge_interface_20260802.py`, SHA-256
`175f493c7e645fa711dd5f0deb7cb3449857488d150937982ce786dbe17faf3a`,
returns

```text
PASS protected hinge interface audit (hoffman_systems=2401
hoffman_boundaries=45619 connected_systems=343)
```

## Semantic checks

1. The literal residence state is the coordinate membership bit together
   with run age clipped at `d+1`.  It is exact only on a carried physical
   binary trace; owner-mask endpoints alone do not determine it.
2. Because every role exposes the full product `A_i x H_i`, tail and head
   choices separate.  Eliminating the two integral transversal-polymatroid
   bases gives exactly

   ```text
   ell_A(X)-r_H(X) <= eta(X)  for every X subset V.
   ```

   This is the necessary-and-sufficient fixed-table one-copy row.
3. Reserving distinct-role packets that span the exact non-isolated support,
   and then applying the shifted inequalities, is necessary and sufficient
   for the stated component bound.  Connected physical interiors and the
   privacy hypothesis are needed to lift contracted connectivity.
4. A cyclic head permutation among selected packets from distinct Euler
   components preserves the boundary.  Full Cartesian completion makes the
   replacement physical and role-resource identical; the complete history
   and named-witness guards are therefore retained literally.

The verifier first exhausts all `7^4=2,401` two-role, three-state tail/head
list systems and all 45,619 possible zero-sum boundaries in the role range;
literal selection exists exactly when every displayed Hoffman cut passes.
It then exhausts all `7^3=343` nonempty three-state fixed-head list systems
and confirms that a connected integral selector exists exactly when some
distinct-role spanning skeleton leaves a feasible residual matching.  It
also replays the two minimal obstructions:

* a two-state diagonal protected relation whose separate endpoint
  projections falsely pass; and
* a three-state completed-rectangle system with connected rational support
  but no connected integral selector.

## Finite K17 calibration

The independently replayed K17 descent now reaches a connected factor
covering all `19,412/19,412` required ordinary q1 colours.  This validates
the usefulness of alternating incidence circulations but not the completed
interface hypothesis.  Its passive replay has 5,584 cyclic short ordinary
residence components; the best reported linear opening has 5,586 short runs
and 1,848 upper holes.  The stronger all-opening endpoint adapter reports
22/22 opened q1 holes (21 cyclic) and short-run counts 5,586/5,587, so it
emits no common-cap instance.  Thus the finite evidence closes
only ordinary q1; residence, deeper upper rows, source, and compiler remain
outside this theorem.

## Exact open row

For an all-dimensional consequence one must construct, on one integral
triangular table, an unsaturated completed packet relation carrying all
literal histories and named upper witnesses, and then verify the shifted
Hoffman cuts after reserving a connected distinct-role skeleton.  A rational
stationary pull clock, endpoint projections, or connected fractional support
does not imply this common certificate.
