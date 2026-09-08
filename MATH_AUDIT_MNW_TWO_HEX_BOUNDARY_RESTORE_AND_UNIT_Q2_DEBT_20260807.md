# Audit of the two-hex boundary restore

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_TWO_HEX_BOUNDARY_RESTORE_AND_UNIT_Q2_DEBT_20260807.md`  
**Verdict:** PASS.

## 1. Phase choices

For `c=3`, the two auxiliary states select precisely the required additions
`9` and `3`, so the face is alternating.  For `c=7`, alpha has removed the
needed addition `9`; for `c=8`, mirror gamma selects additions `4,6`; for
`c=10`, the Dyck endpoint selects addition `10`.  None has the required
phase.  `c=2` is the first face in reverse.

**Result:** PASS.

## 2. Current cancellation

The second face contributes
`+[0110101111]-[1100101111]`.  Adding the first-face current cancels
`0110101111` and leaves (3.5).

**Result:** PASS.

## 3. Multiplicity

`1100101111` has only the inverse pair `(5,9)`; the candidate exhaustion in
Section 4 is complete.  Therefore its canonical load is one and the
two-face macro is not q2-support-closed.

**Overall verdict:** PASS.
