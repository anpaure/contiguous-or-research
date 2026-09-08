# Audit of sibling promoted-parent multiplicity two

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_COOLLEX_SIBLING_PARENT_TORUS_MULTIPLICITY_TWO_20260805.md`  
**Method:** independent cyclic run/bank multiset replay; no search  
**Verdict:** **PASS**.

## 1. Bank decomposition

In

\[
 0^{s-1}1^a0001^{T-a}\gamma,
\]

only the vacancy bank immediately before the displayed triple-zero block
and the bank immediately after it depend on `a`.  Cyclic merging with an
exterior one-run merely adds constants `L,R`.  Retaining zero bank entries
gives the exact multiset `S union {L+a,R+T-a}` at endpoints as well as in
the interior.  The hook assumption gives at least one exterior zero, so
the two varying sides are distinct banks; the degenerate three-zero circle
is outside scope.

## 2. Cancellation

If two words are cyclic rotations, their complete bank-count multisets are
equal.  Cancelling the common finite multiset `S` is valid even when a
variable count equals an entry already in `S`.  Equality of the remaining
two-element multisets gives either `a=b` or
`b=R+T-L-a`.  Hence there is at most one distinct partner.

Because the exterior constants are common to the complete sibling call,
the partner formula uses one common reflection center.  Its chords are
nested, and identifying them folds a path; this justifies Corollary 2.3.

## 3. Scope

The result is confined to the ports from one sibling call, whose exterior
word is fixed.  A promoted torus may still receive ports from many
different calls.  The theorem does not solve their global order.  It
correctly reduces each local sibling incidence to singleton and pair
blocks under one reflection and leaves their marked positional recursive
splice open.
