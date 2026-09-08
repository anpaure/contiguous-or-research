# Independent audit of the full-line wedge-cover seal

## Verdict

**PASS.**  The finite cover lemma, saturation passage, positive-line count,
absorbed-mass cap, and uniform `1/4` margin are correct.  The theorem's scope
is exactly the edge-mass-three (`ell(1+)=3`) branch; it is not by itself a
proof for profiles retaining positive missing edge/gap mass.

## Finite cover check

If the selected directed plateau edge sum is `(3-o(1))a^2`, their word-edge
intervals are disjoint and their vertex union has at least that many points.
It lies in the union of the selected complete coordinate lines.  Since
`|H_a|=3a^2+O(a)`, the number `D_a` of points missed by those lines is
`o(a^2)`.

For an unselected positive level `x` in one direction, the `x-1` points

\[
(x,-y,-(x-y)),\qquad1\le y<x,
\]

must, except for uncovered points, lie on selected negative levels in one of
the other directions.  If their total negative-line count is `q`, at least
`(x-1-q)_+` points of this slice are uncovered.  Splitting the missing
positive levels at excess `h` and summing the three disjoint sign wedges gives

\[
3a-P_a\le2N_a+3h+3+D_a/h.
\]

Taking `h` of order `sqrt(D_a)` proves `P+2N>=3`.  An independent additive-
combinatorial proof via arithmetic triangle removal and Cauchy--Davenport
gives the same limiting inequality.

## Seam algebra check

Same-line uniqueness gives `P+N=f`, and every absorbed successor uses a
distinct strictly positive selected line, so

\[
A\le P\le2f-3.
\]

With `C=int_alpha(p+s-1)`, absorption legality gives `C<=2A`, while the two
common marginal moments give `C<=A+2(3-f)`.  Therefore

\[
C-R_\beta\le C\le\min(4f-6,3).
\]

On `3/2<=f<=3`,

\[
1+f-\min(4f-6,3)\ge1/4,
\]

with the envelope meeting at `f=9/4`.  Substitution in the exact zero-gap
identity yields `U(1+)<=15/4`.

## Boundary of the result

The hypothesis `ell(1+)=3` is essential to the present proof.  It makes the
selected line union an almost cover.  If `ell=3-delta` with fixed positive
`delta`, the uncovered set can have positive density and the square-root
error in the robust cover inequality must be paid together with the exact gap
functional.  That quantitative extension remains open.
