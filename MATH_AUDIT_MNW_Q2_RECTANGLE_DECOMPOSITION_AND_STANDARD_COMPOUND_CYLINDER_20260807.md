# Audit of MNW q2 rectangle decomposition and compound cylinder

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_Q2_RECTANGLE_DECOMPOSITION_AND_STANDARD_COMPOUND_CYLINDER_20260807.md`  
**Verdict:** PASS.

## 1. Rectangle identity

Two isolated changes `a->c` and `b->d` give

\[
[Xbc]+[Xad]-2[Xab],
\]

whereas their simultaneous final turn gives `[Xcd]-[Xab]`.  Subtraction is
exactly `[Xcd]+[Xab]-[Xbc]-[Xad]`.  Zero-, one-, and two-change cases exhaust
every lower centre.

**Result:** PASS.

## 2. `F_4` contact

For `x=11010010`, concatenation of the canonical flip orders gives

\[
\pi(x)=(6,4,5,2,3,1,8,7).
\]

The marks of `alpha(empty)10` and `alpha(10)` are six and four, hence edge
positions one and two.  Their common upper centre is `11010110`.  Directly
from the two alpha cycles, the neighbour replacements are

\[
11010010\to10010110,
\qquad
11000110\to11010100.
\]

The coturn changes from `11000010` to `10010100`.

**Result:** PASS.

## 3. Wrapper and suffix checks

Applying `F(A)=1 revcomp(A) 1` gives

\[
F(10010100)=1110101101,
\qquad
F(11000010)=1101111001.
\]

The first word is canonically missing by the exhaustive height/ordinal
inverse test recorded in the mirror-wrapper theorem.  A Dyck suffix starts
at height four and cannot alter that test.

**Result:** PASS.

## 4. Membership in one MNW tree

The published recursion for `F_(m,5)` includes
`1 revcomp(F_4) 0 v` for every `v in D_(m-5)`.  The fixed `F_4` tree includes
both alpha tuples used above.  Hence all suffix-indexed compound contacts
are literally selected in one recursively defined spanning tree.  Distinct
suffix fibres are disjoint.

**Result:** PASS.

## 5. Scope

The theorem proves creation of one complete Catalan cylinder of canonical
holes.  It does not assert that no other selected current deletes those
targets later (none can change the same centre because marks are distinct),
nor that all other q2 targets remain covered.  Its conclusion is exact
support mobility and coexistence, not global q2 completeness.

**Overall verdict:** PASS.
