# Audit of the clean-C6 q2-neutral common-deletion classification

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_CLEAN_C6_Q2_NEUTRAL_COMMON_DELETION_CLASSIFICATION_20260805.md`  
**Method:** independent set-algebra replay; no computation or search  
**Verdict:** **PASS**, with the sequential-composition scope stated below.

At `P_i`, every companion q1 row has the form `L_i=P_i-d_i`.  Equality
with `R_i=P_i-a_(i+1)` or `R_(i+1)=P_i-a_i` is forbidden by the old or
transported one-occurrence section, so `d_i` lies in `K`.

The only changed q2 turns are therefore

\[
 D_i=(K-d_i)+a_i,
 \qquad
 D'_i=(K-d_i)+a_{i+1}.
\]

Each set contains exactly one active label.  Hence a new set containing
`a_(i+1)` can equal only the old set `D_(i+1)`, and equality forces
`K-d_i=K-d_(i+1)`, equivalently `d_i=d_(i+1)`.  Cycling proves necessity;
common deletion proves sufficiency.  At `Q_i`, the row remains `R_i`, so
there is no omitted endpoint contribution.

The final loose-forest sentence is exact when the switches are physically
disjoint, or more generally when each switch at the moment of application
still has the displayed companion rows and common-deletion property.
Arbitrary overlapping switches cannot be declared transparent solely from
their initial static ledgers.  This is a scope clarification, not a defect
in Theorem 3.1.

