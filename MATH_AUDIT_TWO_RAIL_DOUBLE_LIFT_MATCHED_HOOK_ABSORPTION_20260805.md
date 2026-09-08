# Audit of two-rail double-lift matched hook absorption

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_TWO_RAIL_DOUBLE_LIFT_MATCHED_HOOK_ABSORPTION_20260805.md`  
**Method:** independent cut-path replay; no search  
**Verdict:** **PASS** for the exact topology and conditional hook lift.

## 1. Topology replay

The first C6 uses one cut on each of `R_0,U,V`, so it merges those three
cycles.  The second has two cuts on that merged cycle and one on `R_1`.
A `2+1` C6 leaves two cycles for either orientation.  Since each of `U,V`
was cut once by each C6, its two complementary path fragments lie in the
two output cycles.  Thus both children are split across the rails.

## 2. Palette replay

The two old-edge sets and protected halos are disjoint by hypothesis, so
their isolated clean-C6 q1/q2 identities compose.  No physical ordering of
their third-shore cuts on one cycle is used because the third shores are on
different input rails.

## 3. Hook scope

A matching makes all child pairs disjoint.  The theorem still requires one
literal lift on each parent rail with disjoint halos; the known existence of
two vertex-disjoint rotations on the same component triple does not alone
prove that rail assignment.  The matching-deficiency statement is also an
explicit open premise.  The theorem's conditional scope is correct.
