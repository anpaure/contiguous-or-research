# Self-audit: Boolean matching image Strong Rayleigh theorem

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`  
**Verdict:** GO, with the arbitrary-colour limitation in Section 6.

## 1. Uniform edge marginals

The automorphism argument has exactly two edge orbits:

* old inclusion edges, transitive under coordinate permutations;
* dummy edges, transitive under coordinate and dummy permutations.

Every old vertex has `n-q` incident edges and selects one.  Every labelled
dummy has `N` incident edges and selects one.  Hence the probabilities are
exactly `1/(n-q)` and `1/N`; no asymptotic symmetry assertion is used.

## 2. Transversal orientation

Taking `R` as the ground shore, a set `B subset R` is independent precisely
when it can be matched injectively to `L`.  Since `|L|=m`, a base has size
`m` and is exactly the image of a matching saturating `L`.  The Boolean
normalized-matching property guarantees rank `m`.

The coefficient `c_B` counts all saturated old matchings with image `B`.
Every such old matching has exactly `h!` completions by the universal
labelled dummies, independent of `B`.  Thus the image law under a uniform
perfect matching of `J_q` has generating polynomial `P_q/P_q(1)` exactly.

## 3. Stability closure

The restricted Heilmann--Lieb polynomial on the chosen ground shore is
multiaffine and has the open right-half-plane property with positive
matching-count coefficients.
Its maximum degree is `m`; its degree-`m` homogeneous part retains exactly
the matchings saturating `L`.

For `t>0`, `t^{-m}F_q(ty)` has that property.  It converges coefficientwise
and locally uniformly to the nonzero top homogeneous part.  Hurwitz
closure therefore proves the right-half-plane property of `P_q`.  Since
`P_q` is homogeneous, substituting `-iy` turns the upper half-plane into the
right half-plane and contributes only the common factor `(-i)^m`; hence
`P_q` is real stable in the Strong-Rayleigh convention.  This is the
weak-half-plane weighted basis polynomial, not the unweighted basis-
generating polynomial.  The
theorem does not accidentally assert that every transversal matroid has
the strong half-plane property.

## 4. Mean and concentration

Every right vertex has old-occupancy probability

\[
 {q+1\over n-q}={\binom nq\over\binom n{q+1}}.
\]

Summing over `binom(U,q+1)` gives the first expression in (3.2), and

\[
 (q+1)\binom v{q+1}=(v-q)\binom vq
\]

gives the second.  Strong Rayleigh implies negative association; the
usual Bernoulli exponential-moment proof gives the displayed upper and
lower tails.  Dummy occupancy is a deterministic complement of old
occupancy on each fixed owner set, so its two-sided deviation is identical.

## 5. `C6` formula

For a hexagon `(C;a,b,c)`:

* if fewer than two of `a,b,c` are in `U`, no upper hexagon vertex lies in
  `R_U`;
* if all three are in `U`, all three upper vertices lie in `R_U` and the
  total of the three old colours is unchanged;
* if exactly two, say `a,b`, are in `U`, only `C+ab` lies in `R_U`, and its
  provider toggles between `C+a` and `C+b`.

Hence sensitive hexagons are in bijection with a Johnson boundary edge and
one choice of the third label in `[n] \setminus U`, proving the factor
`n-v`.  Orientation would multiply both sides by the same fixed factor;
the theorem explicitly uses unoriented hexagons.

## 6. Scope limitation

The projection `I(M)` forgets which old vertex supplies a selected right
vertex.  Therefore it controls `X_(A,U)` only in cases where the colour is
forced by the endpoint—for example `A=binom(U,q)`—or after summing over all
old colours.

It does not prove:

* Strong Rayleigh for the edge set of the perfect matching;
* concentration for arbitrary persistent old colours;
* concentration conditional on an old image set;
* the complete multi-step coloured-chain oracle; or
* the all-dimensional `B(k)+O(1)` theorem.

The edge Strong-Rayleigh no-go remains valid: a projection of a non-Strong-
Rayleigh law can be Strong Rayleigh.

### 6.1 Fixed-colour support replay

For `n=4,q=1,A={1,2,3}`, both image sets
`B={14,23,34}` and `C={13,24,34}` have the displayed saturated
extensions.  For `e=23`, replacing it by `13` strands old vertex `2`, while
replacing it by `24` consumes all three neighbours of old vertex `4`.
Thus basis exchange fails exactly.  Since the uniform law gives positive
weight to every saturated matching, this is its complete support
obstruction, not a zero-coefficient artefact.

### 6.2 Block-polynomial replay

When `binom(U,q) subset A`, the marked block is exactly the event that an
old image lies in `R_U`; the specialization of `P_q` is therefore exact.

For the conditional negative example, after fixing `7->17`, `8->28`, and
twenty dummy assignments, the six remaining columns are precisely the
edges of the cycle

\[
 1-12-2-23-3-34-4-45-5-56-6-16-1.
\]

Its two alternating matchings have block counts two and zero for
`A={1,4}`, `U={1,2,4,5}`.  Both have positive conditional weight, so the
conditional generating polynomial is a positive scalar multiple of
`a+bz^2`; its roots are nonreal.  The theorem correctly limits this to a
conditioning-stable no-go and does not infer that the unconditional block
polynomial is non-real-rooted.

## 7. Source-scope check

Choe--Oxley--Sokal--Wagner supplies the Heilmann--Lieb matching-polynomial
construction and weak half-plane property for transversal matroids.
Borcea--Branden--Liggett supplies the Strong-Rayleigh/negative-association
implication.  Every Boolean specialization, marginal computation and
`C6` count is proved directly in the audited theorem.
