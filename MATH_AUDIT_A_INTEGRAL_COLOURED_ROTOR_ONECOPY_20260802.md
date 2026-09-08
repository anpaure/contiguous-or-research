# Audit of the integral coloured-rotor one-copy theorem

**Date:** 2026-08-02  
**Status:** independent finite replay and scope audit of
`MATH_THEOREM_A_INTEGRAL_COLOURED_ROTOR_ONECOPY_MINMAX_AND_RAINBOW_FUSION_20260802.md`.

## 1. Corrected fractional dependency

The theorem uses only
`MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`, SHA
`7302724eb8b405c2bf1efcc743a1de06809cd1f9b3134e07ba8aa6933b631b21`.
No step uses the reversed-ratio derivation.  The fractional result is used
only as motivation and as a conditional input to Corollary 1.2.

## 2. Exact finite replay

The independent script
`scratch/audit_a_integral_coloured_rotor_onecopy_20260802.py` performs six
checks using exact integer/rational arithmetic.

1. It exhausts all `7^4=2401` two-role tail/head rectangle systems on three
   states and all 19 possible zero-sum integral boundary vectors in
   `[-2,2]^3`.  In all 45,619 cases, a literal one-copy selector exists if
   and only if every Hoffman inequality

   \[
                         \ell_A(X)-r_H(X)\leq\eta(X)
   \]

   holds.
2. It reconstructs the four-edge parity tensor, checks the exact half-unit
   degree equations on all three shores, enumerates both integral
   tail--head matchings, and obtains determinant `2` for the stated minor.
3. It exhausts all `16^4=65,536` quadruples of Boolean sets on a four-point
   universe.  All 4,096 quadruples satisfying the diagonal/crossed equality
   premise have equal two union colours, confirming the intercalate
   exclusion.
4. It enumerates all affine permutations for `2<=N<=8`.  The numbers of
   rainbow covers are respectively

   \[
                         0,3,0,15,0,133,0,
   \]

   and every odd case contains a rainbow Hamilton translation.  Every even
   case contains none.
5. For odd middle-levels incidence graphs with `r=2,3,4`, it reconstructs
   all `3,10,35` vertices per shore and verifies both a perfect matching and
   a perfect matching through every one of the `6,30,140` protected edges.
6. It exhausts all 64 unit-capacity directed packet banks on three owners and
   all ten nonnegative owner-multiplicity vectors of total three.  In all
   640 cases, the owner-contraction cut family is equivalent to an integral
   surplus-to-deficit max flow.

The deterministic output is

```text
PASS
hoffman_systems=2401 hoffman_tests=45619
parity_minor_det=2
union_quadruples=65536 union_equal_grid_antecedents=4096
affine=[(2, 0, 0), (3, 3, 2), (4, 0, 0), (5, 15, 4), (6, 0, 0), (7, 133, 48), (8, 0, 0)]
coatom=[(2, 3, 6), (3, 10, 30), (4, 35, 140)]
owner_contraction_tests=640
```

## 3. Proof-scope audit

The following distinctions are load-bearing.

* The Hoffman theorem fixes one owner/payload table and assumes literal
  Cartesian tail/head menus.  An averaged fractional mixture of several
  tables does not meet that premise.
* The rainbow-cycle theorem is the unattached full-depth zero-boundary face.
  After owners are attached rolewise, the owner row is automatic and the
  problem reduces to ordinary predecessor Hall.
* The parity tensor and affine even family are abstract three-shore
  counterexamples.  They are not claimed to embed in the canonical Boolean
  union-colour atlas; the exhaustive union audit confirms that the smallest
  intercalate cannot embed.
* A colour-neutral `2x2` switch is not a necessary fusion move.  The odd
  affine atlas has a global rainbow Hamilton translation but no nontrivial
  rectangle switch from the rainbow identity cover.
* The owner-contraction cut theorem requires unit packets and hereditary
  serial realizability.  Without those hypotheses, packet-lattice and
  interference obstructions remain.
* The odd coatom theorem begins only after an integral lower-chain table has
  been constructed.  It closes owner assignment, not chainization or
  chronology.
* `O(1)` Euler components generally cost `O(d)` reset arcs.  Only connected
  fusion or total overlap deficit `O(1)` yields an additive constant.

Accordingly the result proves an exact min--max and fusion interface, not
`B(k)+O(1)`, exact `B(k)`, residence, deep upper coverage, or compiler
compatibility.
