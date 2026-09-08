# Self-audit: exponential optional core from two-level cube isoperimetry

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_OPTIONAL_BOOTSTRAP_TWO_LEVEL_CUBE_EXPONENTIAL_CORE_20260804.md`

## 0. Verdict

**PASS_SELF_AUDIT.**  The result is a size lower bound only.  It does not
close residual factor extension.

## 1. Induced graph and edge count

The vertices `B` and `Q` lie in ranks `m-1,m` of one Boolean cube.  Thus
the induced hypercube graph on `B union Q` has exactly the selected
containment incidences and no same-shore edges.  The hypothesis
`d_B(U)>=D` gives `E>=D|Q|` without discarding any edge.

Because `|Q|>=|B|`, the right shore has at least half the vertices, so
`E>=D(|B|+|Q|)/2`.  This is the only place where shore balance is used.

## 2. Cube inequality

The induction permits empty sections.  With `a<=b`, the number of crossing
edges is at most `a`.  The scalar inequality is correct because

\[
 f(t)=(1+t)\log(1+t)-t\log t-2t\log2
\]

is concave on `(0,1)` and vanishes at both endpoints.  A concave function
lies above its endpoint chord, hence is nonnegative.  Therefore
`E<=N log_2(N)/2` applies exactly to the selected two-level vertex set.

## 3. Lower-shore extraction

Each rank-`m-1` vertex has full upper degree

\[
 (2m-1)-(m-1)=m.
\]

Hence `E<=m|B|`.  Together with `E>=D|Q|`, this gives
`|Q|<=m|B|/D`; no minimum degree on the lower shore is required.  Combining
with `|B|+|Q|>=2^D` proves the displayed lower-shore bound.

## 4. Bootstrap substitution

The wide-gap theorem gives, for positive-capacity owners,

\[
 |Q|\ge |B^-|+1,
 \qquad
 |N(U)\cap B^-|\ge d-3.
\]

Thus `D=d-3` is legitimate for all sufficiently large `m`, when it is
positive.  Since `d=Theta(sqrt(m))`, one has `m/(d-3)=O(d)`.

## 5. Scope exclusions

The exponential bound is weaker than the proposed sharp central-subcube
bound and remains `2^{o(m)}`.  It neither contradicts the ambient layer
size nor proves that the core intersects a previously closed structural
class.  It is therefore genuine progress on localization, not a factor
extension theorem.

