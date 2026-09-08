# Audit of the coloured surplus-current Pfaffian

**Date:** 2026-08-06  
**Audited note:**  
MATH_THEOREM_ODD_COLOURED_SURPLUS_CURRENT_PFAFFIAN_GATE_20260806.md  
**Method:** generic-matrix, exterior-power, and colour-algebra replay; no
computation  
**Verdict:** PASS for the boundary-current bank.  It does not certify hub
distinctness of the complementary nonwrap matching.

## 1. Representation check

The generic incidence matrix of a transversal presentation represents the
transversal matroid: every determinant term is one incidence matching and
has its own product of algebraically independent variables.  Its dual is
representable over the same rational function field.  A maximal minor of
the resulting \(\delta\)-row matrix \(A\) is nonzero exactly on a surplus
basis.

## 2. Pfaffian minor summation

For the skew boundary matrix \(\Theta\), the exterior two-form

\[
 \sum_{u<v}\Theta_{uv}a_u\wedge a_v
\]

has top exterior coefficient

\[
 \sum_{|U|=\delta}\pm\det A[U]\operatorname{Pf}\Theta[U].
\]

This is exactly \(\operatorname{Pf}(A\Theta A^{\mathsf T})\).  A term of
\(\operatorname{Pf}\Theta[U]\) is a perfect matching of the boundary graph
on \(U\), together with one pointed occurrence per quotient edge.

Independent occurrence variables separate different pointed matchings.
Commuting square-zero hub variables kill exactly the terms that repeat a
hub colour; squarefree colour monomials remain linearly independent.
Hence no surviving witness can cancel with another.

## 3. Socket extension

The direct sum with one coloop \(\star\) is represented by adjoining a
new coordinate.  Matching \(\star\) to \(s\) forces exactly one allowed
socket and leaves a boundary perfect matching on the other surplus-basis
vertices.  Independent socket variables separate the choices.  This
proves the odd-rank statement.

## 4. Scope correction

The determinant \(\det A[U]\) certifies existence of some complementary
matching in the nonwrap graph.  Its generic representation does not track
the deleted-cut hub colours of that matching.  Therefore the Pfaffian
enforces hub-rainbow only on the selected same-shore boundary current.
The theorem contains this corrected scope and sends nonwrap colour
repetitions to the paired fan/receiver gate.

The construction is not a translation-invariant quadratic current:
\(A\) contains the full target-incidence correlation and \(\Theta\) has
configuration-dependent variables.  The free-fermion nullity obstruction
does not apply.
