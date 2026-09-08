# RETRACTED — the claimed Latin-direction shallow solution is false

Date: 2026-07-26

The theorem formerly in this file is retracted. It must not be cited as a
construction or as evidence for the constant-one argument.

There are two independent fatal errors.

1. The crossed `Q_4 x Q_4` recursion does not preserve the same-owner
   direction identity. At

   \[
   u=0000,\qquad v=1100,
   \]

   the zeroth child uses direction `L1`, so the proposed involution sends it
   to `R1`, whereas the crossed first child uses `R3`. Hence the recursive
   double factor and the column-Latin equations do not follow.

2. The physical lower/upper target does not determine the completed-pair
   support `J`. On one coordinate pair, the lower trace `00` may come from
   either an untouched empty pair or a completed move
   `00 -> 01 -> 11`; similarly for the upper trace `11`. Consequently the
   augmented code `(J,p|J^c,x|J^c)` is not the physical trace, and the claimed
   half-step decoder is invalid.

What survives is only the conditional algebraic puncturing calculation when
`J` is supplied externally. It does not solve the physical trace problem.

The full audit, including the explicit counterexample and the surviving
conditional statements, is in
`MATH_AUDIT_LATIN_DIRECTION_ARRAY_COMPLETE_SHALLOW_SOLUTION_20260726.md`.
