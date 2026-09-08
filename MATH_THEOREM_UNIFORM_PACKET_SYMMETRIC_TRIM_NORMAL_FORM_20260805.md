# Uniform packets are symmetric trims of Minkowski sums

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact normal form.  The endpoint rows for a
uniform job layer and finitely many uniform socket layers collapse to one
common trim scalar.  This linearizes the compact layer packet still
further; it does not construct the required marginal transport.

## 1. Exact normal form

Let

\[
 J=[A,B],\qquad S_i=[a_i,b_i]\quad(1\le i\le n)
\]

be nondegenerate compact intervals on the nonnegative line.  Put

\[
 \ell_i=b_i-a_i,
 \qquad
 L=\sum_i a_i,
 \qquad
 U=\sum_i b_i=L+\sum_i\ell_i.                     \tag{1.1}
\]

Thus `[L,U]` is the Minkowski sum of the socket supports.

### Theorem 1.1 (symmetric-trim packet criterion)

The interval-uniform laws on `J,S_1,...,S_n` admit a coupling

\[
 X=Y_1+\cdots+Y_n
\]

almost surely if and only if there is a scalar `p` such that

\[
 \boxed{J=[L+p,U-p]}                               \tag{1.2}
\]

and

\[
 \boxed{
 p\ge0,
 \qquad
 2p<\sum_i\ell_i,
 \qquad
 p\le\sum_{j\ne i}\ell_j\quad(1\le i\le n).}    \tag{1.3}
\]

Endpoint-null/degenerate layers use weak inequality in the middle row.

### Proof

The endpoint packet criterion is

\[
 A+B=\sum_i(a_i+b_i),                              \tag{1.4}
\]

\[
 \sum_i a_i\le A,                                 \tag{1.5}
\]

and

\[
 a_i+\sum_{j\ne i}b_j\ge A\quad(1\le i\le n).   \tag{1.6}
\]

Define

\[
 p=A-L.
\]

Equation (1.5) is `p>=0`.  Equation (1.4) then gives

\[
 B=U-p,
\]

which is (1.2).  Nondegeneracy of `J` is exactly

\[
 B-A=\sum_i\ell_i-2p>0.
\]

Finally, subtracting `A=L+p` from the left side of (1.6) gives

\[
 a_i+\sum_{j\ne i}b_j-A
 =\sum_{j\ne i}\ell_j-p.
\]

Thus (1.6) is precisely the final family in (1.3).  Every step is
reversible, proving the theorem. `square`

## 2. Useful special cases

### Corollary 2.1 (two socket roles)

For two socket intervals,

\[
 J=[a_1+a_2+p,\ b_1+b_2-p]
\]

is legal exactly when

\[
 0\le p\le\min\{\ell_1,\ell_2\}.                 \tag{2.1}
\]

The nondegenerate job-width row is automatic from the strict version of
the displayed bounds unless both widths and `p` meet at the degenerate
endpoint.

### Corollary 2.2 (balanced widths)

Suppose

\[
 \max_i\ell_i\le{1\over2}\sum_i\ell_i.           \tag{2.2}
\]

Then every symmetric trim with

\[
 0\le p<{1\over2}\sum_i\ell_i                    \tag{2.3}
\]

is legal.

### Proof

Condition (2.2) gives, for every `i`,

\[
 \sum_{j\ne i}\ell_j
 =\sum_j\ell_j-\ell_i
 \ge{1\over2}\sum_j\ell_j>p.
\]

Apply Theorem 1.1. `square`

Thus once socket layers are refined into width-balanced groups, the entire
polygon condition disappears: the job interval may be any nondegenerate
symmetric trim of their Minkowski sum.

### Corollary 2.3 (homothetic packets)

If positive numbers `lambda_i` sum to one and

\[
 S_i=D_{\lambda_i}J,
\]

then the Minkowski sum of the socket intervals is exactly `J`, so `p=0`.
This recovers the proportional-role Monge packet.

## 3. Consequence for the compact layer transport

The finite-arity Rayleigh layer polytope can equivalently be parametrized
by:

1. a group of `n<=R` socket layers;
2. their additive endpoint pair `(L,U)`;
3. one trim scalar `p` satisfying (1.3); and
4. the job layer `[L+p,U-p]`.

Hence the remaining layer problem is an exact two-coordinate additive
transport with a one-dimensional local trim, not a nonlinear polygon
system.  On the balanced-width face it is simply:

\[
 (a_1,b_1)+\cdots+(a_n,b_n)
 \longmapsto
 (L+p,U-p),qquad0\le p<(U-L)/2.                  \tag{3.1}
\]

This is the natural coordinate system for a northwest-corner or Monge
attempt.  Such a global marginal construction is not supplied here;
ordinary endpoint-sum transport still has to respect that all endpoints
grouped in (3.1) belong to the same finite packet.

## 4. Frozen dependencies

1. `MATH_THEOREM_UNIFORM_PACKET_ENDPOINT_CRITERION_AND_COMPACT_LAYER_GATE_20260805.md`,
   SHA at use
   `5e5747db237b3001a08619b0d48384b7ec00bfbd55c3f034f6f02704dc9db4fd`.
2. `MATH_THEOREM_COMPACT_GAPPED_UNIFORM_LAYER_FINITE_ARITY_POLYTOPE_20260805.md`,
   SHA at use
   `952c99e878046d81d46bd2bc8125a51ed1c10e99626e46a19b4bec4a10bfeb41`.

