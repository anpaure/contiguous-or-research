# Audit: odd capacity-two rooted-path imbalance and wrap-current gate

**Date:** 2026-08-05  
**Audited reduction:**
`MATH_REDUCTION_ODD_CAPACITY_TWO_PATH_IMBALANCE_AND_WRAP_BLOSSOM_GATE_20260805.md`  
**Method:** signed coefficient and local receiver-square replay; no
computation  
**Verdict:** PASS.  The result is a labelled/rooted obstruction.  It does
not assert the same numerical imbalance after taking an unrooted necklace
quotient, but it decisively rules out the proposed labelled path matching
as a uniform proof.

## 1. Coefficient replay

There are `m+1` even-indexed coordinates and `m` odd-indexed coordinates.
Their signed one-coordinate enumerators are respectively

\[
                         1+z+z^2,qquad1-z+z^2.
\]

Their paired product is `1+z^2+z^4`.  At odd total mass only the `z` term
of the one excess even coordinate contributes.  Therefore the shore
difference is exactly

\[
                         [z^{R-1}](1+z^2+z^4)^m.
\]

Every coefficient in the nonempty odd range is positive.  Deleting two
socket vertices changes the difference by at most two, verifying the
unbounded rooted-path no-go.

## 2. Wrap-current replay

The path parity is `sum i t_i mod 2`.  Moving a token between positions
`0` and `2m` changes this sum by `2m`, hence preserves parity.  Each
majority-shore wrap edge removes two majority vertices and changes the
signed difference by minus two; a minority-shore edge changes it by plus
two.  This proves the necessary current equation.

## 3. Actual receiver jobs

In a double-expansion square, sides parallel to a nonwrap parent shift
cross the rooted shores.  Sides parallel to the unique wrap shift stay
within a shore.  Endpoint-disjointness permits at most one wrap petal per
literal hub fan.  Pairing it with one other passive petal gives one mixed
job whose two wrap options lie on opposite rooted shores and whose two
other options are cross-shore.  Every other job is root-regular and adds
one private terminal to each shore.

Thus mixed jobs contribute current `-2,0,+2`, while root-regular jobs
contribute zero.  The reduction correctly requires mixed-job modes plus
additional circulation ears to pay the coefficient imbalance before the
even Hall router is invoked.

## 4. Scope

The rooted calculation does not prove that the required wrap-ear bank
exists, survives rotations, avoids both reset colours, or satisfies the
remaining augmented Hall rows.  It proves that one adaptive radial
monomer cannot replace that bank and that odd-level factor-criticality, if
true, must use the wrap direction macroscopically.
