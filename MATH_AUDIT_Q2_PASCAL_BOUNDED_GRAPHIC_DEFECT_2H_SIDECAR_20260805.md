# Audit of the bounded-graphic-defect q2 Pascal lift

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_Q2_PASCAL_BOUNDED_GRAPHIC_DEFECT_2H_SIDECAR_20260805.md`  
**Method:** independent edge/component/palette replay; no computation or
search  
**Verdict:** **PASS** at the stated q2/owner interface.

Removing one selected turn from each of `h` wholly selected cycles changes
the selected-position count from `Q` to `Q-h` and the omission count from
`kappa` to `kappa+h`.  Hence the A forest has `kappa+h` components and
`Q-h` edges.  The Z forest has `s+h` components and `Q-h-s` edges.  After
the `s` ordinary crosses, the totals are `kappa+2h` and `2Q-2h`.

For each puncture, the edge

\[
 (z+Y_{p-1})(z+Y_p)
\]

attaches an isolated vertex to the free Z endpoint.  It has the fresh
union `z+X_(p-1)` and restores one of the two possibly lost q2 targets.
Thus the final totals are `kappa+h` components, `2Q-h` edges, and at most
`h` q2 holes.  The no-z q1 label at the puncture is retained by the
singleton-run A surgery; the following selected q1 label is restored by
the ordinary cross.

There are `2kappa+2h` endpoint roles and `2kappa+h` distinct unused owner
colours.  Locally the repair edge consumes the former endpoint owner
`z+X_(p-1)`; `U_p` still serves `X_(p+1)`, while one repeated occurrence
of the already used `z+X_p` serves `z+Y_p`.  This gives exactly one owner
repeat per puncture, matching the global deficit.

The aggregate sidecar is therefore `h` owner repeats plus at most `h`
literal q2 masks.  No downstream residence/compiler assertion is silently
included.  The scope and constant `2h` are exact.

