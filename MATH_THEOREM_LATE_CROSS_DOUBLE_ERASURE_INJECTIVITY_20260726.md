# Corrected scope: late-cross augmented-code injectivity

Date: 2026-07-26

The original version of this note contained two false assertions and must
not be cited in that form.

1. The naive crossed partner was not a same-owner double factor.  At
   `(u,v)=(0000,1100)`, its proposed direction is `R3`, whereas the image
   of the zeroth direction is `R1`.
2. A literal lower or upper OR target does not determine the varied-pair
   support `J`.  Thus injectivity of `(J,p|J^c,x|J^c)` is not literal
   target injectivity.

The first defect has an exact controlled-column repair, and the second
fixes the theorem's scope.  The valid result is:

> For `R=8*2^t`, the repaired cross-once-then-parallel certificate is an
> exact double factor.  For both orientations and every `d<=R/8`, the
> externally tagged code
> \[
> (J_d^\pm(S_Rp+x),p|_{(J_d^\pm)^c},x|_{(J_d^\pm)^c})
> \]
> is exactly injective.  The corresponding phase decoder needs no parity
> checksum, and the support catalogue contains at least `4^d` members.

The full proofs and exact boundary are in:

- `MATH_COUNTERAUDIT_CROSSED_RECURSION_CONTROLLED_COLUMN_REPAIR_20260726.md`;
- `MATH_THEOREM_CROSSED_COLUMN_WITNESS_REPAIR_20260726.md`; and
- `MATH_THEOREM_CONTROLLED_CROSS_DOUBLE_FACTOR_AUGMENTED_CODE_20260726.md`.

No literal lower/upper OR injectivity, untagged half-step theorem, outer
packet coupling, or coefficient-one conclusion is claimed.  The next
target-level gate is support recovery after forgetting `J`.
