# Rayleigh bounded-arity equal splitting misses the small-socket bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional scoped no-go.  After the first Rayleigh transform
and overlap cancellation, no equal-piece policy with a uniformly bounded
number of pieces can reproduce the residual socket measure.  In particular,
the proposed two/three dilation equation has no solution.  Unequal-piece
two/three packets and unbounded-arity equal splitting are not excluded.

## 1. General support lemma

Let `mu` be a positive job measure supported in `[B,infinity)` for some
`B>0`.  An equal-split kernel assigns to a job of size `x` an integer
arity `n` and `n` copies of `x/n`.

### Lemma 1.1

If every selected arity satisfies `1<=n<=M`, then the aggregate socket
measure of the kernel is supported in `[B/M,infinity)`.

### Proof

Every produced socket has size

\[
 {x\over n}\ge {B\over M}.
\]

Taking mixtures over jobs and arities cannot create mass outside the union
of those supports. `square`

Thus any target socket measure which charges every interval `(0,epsilon)`
requires unbounded arity within the equal-split ansatz.

## 2. Application to the first transformed Rayleigh pair

After the first equal-level subtraction and cancellation of the one-piece
overlap, the job and socket densities are

\[
 f_2(x)=u'(x){\bf1}_{(b,\infty)}(x),
 \qquad
 g_2(y)=(-K'(y)-u'(y)){\bf1}_{(0,b)}(y).
\]

The one-well theorem proves

\[
 -K'(y)>u'(y)\qquad(0<y<b),
\]

so `g_2(y)>0` throughout `(0,b)`.  Consequently its measure charges every
interval `(0,epsilon)`.

Taking `B=b` in Lemma 1.1 proves that no bounded-arity equal-split kernel
can have socket marginal `g_2(y)dy`.

## 3. Exact failure of the two/three dilation equation

The concrete two/three ansatz asks for a measurable `h` with

\[
 g_2(y)
 =4(1-h(2y))f_2(2y)+9h(3y)f_2(3y).              \tag{3.1}
\]

For `0<y<b/3`, both `2y<b` and `3y<b`, hence

\[
 f_2(2y)=f_2(3y)=0.
\]

The right side of (3.1) is zero, while `g_2(y)>0`.  Therefore (3.1) has no
solution, even before imposing `0<=h<=1`.

The same argument applies after truncating the jobs to any compact subset
of `[b,infinity)` if one still asks the bounded equal-split kernel to use
the entire original socket bank down to zero.

## 4. Scope

The obstruction is geometric, not a count obstruction.  It does not touch
an unequal-piece packet: a two- or three-piece configuration may contain
one arbitrarily small socket and compensate with its other pieces.  Nor
does it touch the already proved Gaussian-tail kernel, whose arity grows
with job size.  A finite-role continuation must therefore use unequal
pieces, or first remove/reserve the vanishing-socket bank by a separate
exact reduction.

## 5. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
2. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA at use
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.
