# Independent audit: protected Middle-Levels occurrence lift and opening parity

**Date:** 2026-08-04  
**Method:** direct symbolic audit only; no search or finite computation.

**Audited theorem:**
`MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md`.

## 1. Component normal form

An oriented factor component has the unique alternating form

\[
 U_j-L_j-U_{j+1}.
\]

Since `|L_j|=m-1` and the two adjacent owners are distinct rank-`m` sets,

\[
 U_j=L_j+a_j,\qquad U_{j+1}=L_j+b_j,\qquad a_j\ne b_j.
\]

Therefore suppression gives exactly

\[
 U_j\cap U_{j+1}=L_j,qquad
 U_j\cup U_{j+1}=L_j+a_j+b_j.
\]

Every incidence edge is exactly one of the two sides of exactly one such
turn.  This verifies the edge-to-halfport bijection and the singleton label.

The no-four-cycle assertion is also exact.  If distinct lower sets `L,L'`
had two common rank-`m` neighbours, both neighbours would have to equal the
unique rank-`m` set `L union L'`.  Hence a simple factor component has at
least three lower vertices.

## 2. Collision audit

The canonical incidence-skeleton prefix is one arc, so it has no interior.
Edge labels make its halfport terminal unique.  Forgetting the edge-side
label can identify terminals only at a common upper owner; identifying
starts occurs only at a common lower turn.  Hence the exact multiplicities
are `d_P(U)` and `d_P(L)` respectively.

This proves the theorem's positive local-privacy statement and also checks
its scope guard: `Delta(P)<=2` gives endpoint load at most two, not unit
disjointness.  In particular, two selected incidences sharing an owner are
different halfports but one owner-cell alias.  No abstract degree argument
decides whether the compiler's capacity lives on the halfports or on that
alias.

## 3. Phase audit

Relative to one reference orientation, reversing a component swaps the two
turn sides at every lower vertex.  It therefore toggles every edge's binary
role by the same component bit.  The simultaneous equations are

\[
 q(e)=\sigma_C(e)\oplus\eta_C.
\]

They are soluble exactly when `q(e) xor sigma_C(e)` is constant on the
component.  A cyclic root shift does not reverse the local order and hence
does not add another degree of freedom.

This also shows why two preselected matchings do not automatically become
the two globally named alternating phases.  They are locally opposite at
every fully prescribed lower turn, but disconnected prescribed pieces can
land in one completed component with inconsistent parity.

## 4. Opening audit

Cutting at lower vertex `K_C` removes exactly the transition between its two
adjacent owner occurrences.  The two factor incidences at `K_C` are exactly
the two halfports which cease to be internal.  Thus the protected loss is
`d_P(K_C)` and minimization separates componentwise.

For component `C`, write

\[
 b_C=|P\cap E(C)|,qquad \ell_C=|\mathcal L(C)|.
\]

Each protected edge has exactly one lower endpoint, so

\[
 \sum_{L\in\mathcal L(C)}d_P(L)=b_C.
\]

Therefore

\[
 \min_Ld_P(L)\le b_C/\ell_C\le b_C/3.
\]

Summing and using integrality verifies the bound `floor(|P|/3)`.  The
lossless criterion is exactly the existence of a degree-zero lower cut in
each component.  In a Hamilton factor, `|P|<|mathcal L|` forces such a cut.

The theorem correctly does not count the two exposed endpoint remnants as
internal q1 occurrences.  Reusing them requires a separate endpoint
interface.

## 5. Preselection audit

For one selected matching, left and right endpoints are distinct, so the
serialized selected incidences have distinct turn occurrences and distinct
owner values.

For two selected matchings, the same lower endpoint receives two distinct
edges.  Since the completed factor has degree two, those edges exhaust its
turn and become its two opposite halfports.  Each matching is right
injective, so a right value occurs at most twice across their union.  If it
does occur twice, the factor gives two edge-halfport addresses but one
owner-cell occurrence.  This exactly matches the theorem's collision
distinction.

## 6. Fail-closed scope checks

The following tempting inferences are rejected by the audited theorem.

1. **Occurrence does not imply active cap capacity.**  The compensation
   linkage may delete the occurrence, or two halfports may alias one cell.
2. **A local prefix does not imply a suffix router.**  All ports may still
   meet one unit suffix bottleneck.
3. **An uncoloured factor does not imply requested phase labels.**  The
   component parity equations can be inconsistent.
4. **A two-factor does not imply a global linear carrier.**  Opening gives
   path segments; their seams are not automatically Johnson-adjacent,
   upper-transparent, or resident.
5. **A protected edge need not survive every opening.**  Survival is
   exactly the lower-cut condition of Theorem 4.1.

Accordingly, the new theorem genuinely closes the support-level occurrence
and local-prefix gap while leaving only capacity activation, typed suffix
expansion, product closure, and global carrier joining to the appropriate
compiler/common-cap and topology theorems.

