# Audit: adjacent-necklace free-fermion nullity obstruction

**Date:** 2026-08-05  
**Object audited:**
`MATH_THEOREM_ADJACENT_NECKLACE_FREE_FERMION_NULLITY_OBSTRUCTION_20260805.md`
  
**Method:** independent symbolic checks of every representation-theoretic
and spectral step; no finite search  
**Verdict:** PASS, with the scope that the theorem excludes quadratic/free
fermions, not interacting skew matrices and not the matching itself.

## 1. Parameter and stabilizer check

Let a weight-`b` binary word of length `N=q+b` have rotational orbit length
`p` and stabilizer order `h=N/p`.  Periodicity forces `h|b` and `h|N`, so

\[
                        h\mid N-b=q.
\]

For odd `q`, `h` is odd.  On occupied wedge factors, rotation by `p` is a
product of `b/h` cycles of length `h`; its sign is

\[
                      (-1)^{(h-1)b/h}=1.
\]

Therefore no ordinary necklace orbit is killed by Koszul antisymmetry.
This validates the passage from exterior invariants to ordinary necklace
vertices.

## 2. Quadratic classification check

A number-preserving quadratic operator is the additive compound
`dGamma(A)` of its one-particle matrix.  Support on a one-token adjacent
move forces `A` to be supported on cycle edges.  Cyclic equivariance makes
the clockwise coefficients one orbit, and transpose-skew symmetry fixes
the reverse coefficients with opposite sign.  For `N>=5`, no two cycle
directions coincide, so

\[
                         A=a(R-R^{-1}).
\]

The Reynolds average leaves the invariant compression unchanged.  Hence
allowing nonuniform physical coefficients before compression gives no
extra quadratic parameter.  Pair-creation and pair-annihilation quadratic
terms map out of fixed particle number and have zero compression back to
`wedge^b V`; they cannot change this conclusion.

## 3. Fourier and invariant-sector check

For periodic momentum `j`, the rotation eigenvalue is `omega^j` and the
current eigenvalue is

\[
                         \omega^j-\omega^{-j}.
\]

On a Fourier wedge, rotation eigenvalues multiply and current eigenvalues
add.  Every inverse pair `{j,-j}` therefore contributes both total momentum
zero and total current zero.

* If `b=2s`, then `N` is odd and there are `(N-1)/2` inverse pairs.
  Choosing `s` gives
  `binom((N-1)/2,s)` independent invariant zero modes.
* If `b=2s+1`, then `N` is even.  Include momentum zero and choose `s`
  among the `(N-2)/2` non-self-inverse pairs.  This gives
  `binom((N-2)/2,s)` independent invariant zero modes.

For `q>=3,b>=2`, both the chosen size and its complement are positive, so
the relevant binomial coefficient exceeds one.  The arithmetic in the
theorem is exact.

Skew nullity has the same parity as matrix order.  That may increase the
actual nullity beyond the displayed lower bound, but never weakens the
no-go conclusion.

## 4. Antiperiodic check

The signed shift satisfies `R_-^N=-I`.  On fixed weight `b`, its N-th power
is `(-1)^b`, so it defines a cyclic action only for even `b`.  Since then
`N=q+b` is odd, the roots of `z^N=-1` consist of `-1` and `(N-1)/2`
inverse pairs.  Choosing `b/2` inverse pairs again gives invariant zero
modes with the first binomial count.

For a periodic necklace stabilizer, its action is a real sign `lambda`.
It has odd order `h` and `lambda^h=1`, hence `lambda=1`.  Thus the twisted
orbit basis is still indexed by every ordinary necklace.  This verifies
all assertions of Proposition 4.1.

## 5. Minimal example check

At `(q,b)=(3,2)`, length is five.  Cyclic distance classifies a pair of
ones, giving exactly the adjacent necklace `[11000]` and the separated
necklace `[10100]`.  A single adjacent swap joins them, so the simple graph
is `K_2`.

The lower bound is `binom(2,1)=2`, equal to the invariant-space dimension.
Thus the compressed current is zero.  This is an exact counterexample to
the stronger hope that every simple quotient edge receives a nonzero
coefficient under the free current.

## 6. Logical-scope audit

The theorem proves singularity of every rotation-compatible
nearest-neighbour **quadratic** skew specialization after invariant
compression.  It does not imply that the generic Tutte matrix is singular.
Indeed the `K_2` example proves the distinction sharply: the graph is
perfectly matchable while the free specialization is zero.

An interacting coefficient can depend on the entire occupation pattern
and thereby distinguish two physical edge orbits which the one-body
current cancels.  Such coefficients are outside Fourier/free-fermion
classification and remain viable.

## 7. Final audit verdict

The stabilizer signs, classification, Fourier eigenvalues, zero-mode
counts, twisted-spin statement, and quotient-cancellation example all
check.  The advertised negative scope is exact:

\[
 \boxed{
 \text{quadratic free-fermion route fails, while the necklace matching
 problem remains open.}}
\]

