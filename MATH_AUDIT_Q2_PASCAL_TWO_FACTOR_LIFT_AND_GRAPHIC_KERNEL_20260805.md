# Independent self-audit: the q2 Pascal two-factor lift and graphic kernel

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_Q2_PASCAL_TWO_FACTOR_LIFT_AND_GRAPHIC_KERNEL_20260805.md`  
**Method:** independent component, palette, endpoint, and CSP ledger; no
computation or search  
**Verdict:** **GO**.

## 1. Component and edge ledger

Let `d_a>=1` be the number of omitted turn occurrences on factor cycle
`a`.  Deleting one A-edge per omitted occurrence gives `d_a` paths, even
when every position is omitted (then all A-states are isolated).  Hence

\[
 \sum_a d_a=|S^c|=P-Q=\operatorname {Cat}_r
\]

A-components.  If `s` is the number of nonempty selected runs, the Z-sector
has `s` paths and the construction has exactly `s` cross edges.  Every cross
edge meets a fresh Z-component and an A endpoint role, so all are component-
reducing and none creates degree three.  The final component and edge counts
are therefore

\[
 \operatorname {Cat}_r,
 \qquad Q+(Q-s)+s=2Q.
\]

This confirms that the sole additional topological hypothesis is that every
original factor cycle has an omission.  Without it, a selected run can be a
whole Z-cycle and the argument is invalid.

## 2. Palette audit

The A-union bank is globally injective because the starting object is a
spanning middle-levels two-factor and hence visits every rank-`r` upper
vertex once.  Z-edges use `z+X_i` at selected-selected adjacencies; cross
edges use `z+X_i` at omitted-selected adjacencies.  These index types are
disjoint, and all `X_i` are globally distinct.

On a proper omitted run, the displaced A deletion retains the last omitted
q1 occurrence and removes the following selected one; the cross edge restores
exactly the latter.  On a wholly omitted factor cycle there was no selected
q1 occurrence to preserve.  Thus one copy of every avoiding-`z` q1 colour
survives.  The selected adjacencies supply all z-containing q2 colours by
hypothesis.  No componentwise palette collision is hidden.

## 3. Endpoint audit, including the new case

For a proper omitted run of length `ell`, the source assignment uses
`ell` unused A-bank colours and `ell` unused z-bank colours on exactly
`2 ell` endpoint roles.  Every assignment is a literal containment.

On a wholly omitted cycle of length `p`, all `p` A-edges and all `p`
z-bank colours are unused.  Each isolated state `X_i` has two roles.  The
assignment

\[
 X_i\longmapsto z+X_i,\qquad X_i\longmapsto U_{i-1}
\]

uses each bank exactly once, and both owners contain `X_i`.  Hence the new
case is exact.  Summed globally, the construction assigns all `2 Cat_r`
endpoint roles to all unused owners bijectively.

## 4. Graphic-clause exactness and size

A position carrying a globally unique q1 label is selected in every
one-occurrence section.  At a repeated-label position `p`, the position is
omitted exactly when `a_(Y_p) != p`.  Therefore a factor cycle is hit if
and only if

\[
 \bigvee_{p\in C\cap H}[a_{Y_p}\ne p]
\]

holds.  If `C cap H` is empty, infeasibility is immediate.

Repeated positions partition over the factor cycles and have total order
at most `2 Cat_r`.  Thus there are at most `2 Cat_r` **nonempty** graphic
clauses and at most `2 Cat_r` graphic literal occurrences in total.  Empty
clauses are immediate no-certificates and are not included in the nonempty-
clause count.  Combined with the audited positive kernel, all claimed size
bounds follow.

## 5. PBBS scope

The PBBS max-height theorem supplies a common assignment for every positive
q2 constraint.  It does not imply the graphic clauses.  The scalar comparison
is correctly indexed:

\[
 \#\{f^2\text{-cycles}\}\le\operatorname {Cat}_m,
 \qquad
 \#\{\text{omitted q1 occurrences}\}=\operatorname {Cat}_{m+1}.
\]

The larger total omission count is only capacity.  No componentwise
distribution follows, and the source note does not claim one.

