# Audit of the adjacent-necklace first-inversion contour reduction

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_FIRST_INVERSION_CONTOUR_REDUCTION_20260805.md`  
**Method:** independent algebraic and matching-state audit; no search  
**Verdict:** **PASS as a reduction; the parity and halo premises remain
open.**

## 1. Strict adjacency

In the separator encoding

\[
                         0\,1^{x_0}\cdots0\,1^{x_{q-1}},
\]

moving one unit from slot `j` to `j+1` changes only the final `1` of the
`j`-th run and its following `0`.  It is exactly `10 -> 01`, including at
the cyclic boundary.  Therefore the reduction does not import the broader
Johnson-graph transposition adjacency.

## 2. First-inversion scope

The parent of a nonroot lexicographically least necklace swaps its
leftmost inversion.  The published necklace lemma guarantees the output
is still the least rotation.  Inversion number drops, so the parent graph
is acyclic and reaches the sole sorted root.  The theorem uses only these
parent edges, not the longer shifts between consecutive cool-lex outputs.

## 3. Root-contour algebra

For consecutive child roots,

\[
 0^{s-1}1^{t-i}0\,1^i\gamma
 \quad\hbox{and}\quad
 0^{s-1}1^{t-i-1}0\,1^{i+1}\gamma,
\]

the differing factor is `10/01`.  The standard necklace recursion makes
the child families disjoint and the valid indices contiguous.  Hence the
path-of-rooted-blocks model is literal.

## 4. Matching recurrence

At the final block, a perfect matching either avoids the final contour
edge, requiring `(P_i,F_(i-1))`, or uses it, requiring both root-deleted
block matchings and `F_(i-2)`.  This gives exactly

\[
 F_i=P_iF_{i-1}\vee D_{i-1}D_iF_{i-2}.
\]

Under parity-completeness, even blocks are monomers and odd blocks are
forced dimer endpoints.  Therefore each odd-length run leaves one socket
and each even-length run closes.  The theorem correctly does not assert
that all recursive calls are parity-complete or that their odd runs have
the desired parity.

The min-plus extension has the same exhaustive split.  \(U_i\) reserves
the final root and therefore costs \(C_{i-1}+e_i\); \(C_i\) either closes
\(B_i\) internally or consumes the one previously reserved root.  No
third case exists because a matching uses at most one of the two contour
edges incident with a root.

## 5. Port and halo scope

Marked-port injectivity follows by deleting the marked `00`, which
recovers the rooted parent datum.  This does not imply disjoint constant
halos on a repeated physical parent cycle.  The theorem retains halo
packing as a separate list inequality and does not substitute the known
individual two-lift result for a simultaneous packing theorem.

## 6. No overclaim

The note proves a strict-adjacency spanning structure and an exact
one-dimensional matching transfer.  It does not prove the near-perfect
necklace matching itself, the marked-halo packing, the non-hook sectors,
or any post-q2 gate.  Its cited Gray-code boundary is correct: arbitrary
transposition and substring-shift Gray codes are not adjacent-swap Gray
codes.
