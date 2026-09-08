# Audit: four-slot three-efficient pulse normal forms

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_PULSE_NORMAL_FORMS_20260804.md`  
**Verdict:** **PASS** for the exact reductions and stated positive subfaces.
Complete regime positivity remains open.

## 1. Kernel monotonicity

For `x=At`, the sign of `-K'(x)` is the sign of
`pi*t-2*atanh(t)`.  Its second derivative is negative.  Both endpoint
values on `[0,2/3]` are nonnegative, with strict positivity at `2/3`.
The concave-chord argument therefore has the correct direction.

## 2. The `w=y` face

From `y>=2u` and `x<=u`, one gets `u+x<=y`, so `v=y`; both the second
compact transient and the exceptional `m=5` transient vanish.  The gap
inequality `y-u<=z-y` is exactly `T=z+u>=2y`.

For the normalized subface, `(0,u,y,z)` satisfies

\[
 y\ge2u,qquad z\ge u+y,qquad3y\le2z,qquad2y-z\le u.
\]

Hence its exact three-slot residue is `u`, and the cited three-slot theorem
applies when `z>=A`.  The only remaining correction is nonnegative under
`u<=2A/3`.

In the subcritical face, `z+u>=A` and `u<=z/3` imply `z>=3A/4` and
`u>=A-z`.  The upper bound on `y` is `T>=2y`; the lower bound is `w=y`.
Splitting `C(z/3)` into residues `0,z/3,2z/3` proves (2.7).  The two
interval families may overlap, so the occurrence-labelled/multiplicity
wording is necessary and correct.

For period monotonicity, all `q>=2` arguments and both shifted `q=1`
arguments are in the increasing tail.  The upper bounds `u<=P/3` and
`y<=2P/3` have the correct direction because `h` decreases at those tail
arguments.  The rational `rho` certificate yields `R''>101/90`, while its
initial value and slope leave the positive tangent margin `899/20000`.

The boundary period `P_0` dominates every scalar feasibility constraint;
the proof checks separately the alternatives `A-u` and `2y-u`.

## 3. The `w=2u` face

All three orientations in (3.1) follow directly from the definitions.
Again the intervals are occurrence-labelled rather than treated as an
ordinary set union.  Splitting the uniform arithmetic clock proves (3.3).

On the positive subface, `(0,u,2u,z)` is internally superadditive and
regime II because `z>=3u`; its residue-one offset is `u`.  When `v=2u`,
the only negative tail pulse is empty, while `u<=A/3` puts both compact
pulses inside the monotonicity interval.

## 4. Scope

The theorem does not claim that socket-minus-job mass is nonnegative on
arbitrary pulse families.  It preserves the potentially negative tail
pulse and explicitly leaves the two residual pulse systems open.
