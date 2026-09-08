# Audit of `SHIFT_COMPATIBLE_SCD_ALGEBRA.md`

## 1. Verdict

Both obstruction theorems are correct with their stated quantifiers.

* The affine theorem concerns one affine permutation of a complete
  orientation cube (or a set of density `1-o(1)` in that cube).  It does not
  apply to a piecewise-affine tiling.
* The coordinate-action theorem concerns bundles which are literal full
  orbits of fixed coordinate permutations drawn from a specified template
  family.  It does not apply to a wreath factor using exponentially many
  unrelated orders.

The exhaustive checker independently confirms every finite identity in the
tested ranges.  The asymptotic SCD consequence follows from the standard
radius histogram and does not assume an unproved matching theorem.

## 2. Shift-period audit

For a saturated radius-`d` chain, the labels

\[
 r_0,\ldots,r_{d-1},u_0,\ldots,u_{d-1}
\]

are pairwise distinct between the two respective ground-set sides.  The
shift recurrence gives

\[
 f^jX=X-\{r_0,\ldots,r_{j-1}\}
       +\{u_0,\ldots,u_{j-1}\}
\]

through `j=d`.  Therefore no period `j<=d` is possible.  The strict
inequality `period>d`, rather than merely `period>=d`, is correct.

The radius count telescopes exactly:

\[
 \sum_{d=D}^{E}
 \left[\binom{2m}{m-d}-\binom{2m}{m-d-1}\right]
 =\binom{2m}{m-D}-\binom{2m}{m-E-1}.
\]

For `D=a sqrt(m)` and `E=b sqrt(m)`, the local central-binomial estimate
gives a fixed positive multiple of `W` whenever `0<a<b` are fixed.

## 3. Affine-flat audit

Let `M=A+I` have rank `r`.  The displacement `Mx+b` is uniform on one
`r`-dimensional affine flat.  Distinct unit vectors are affinely independent
up to the obvious `t-1` dimension, so that flat contains at most `r+1` unit
vectors.  This proves

\[
 \Pr(|F(x)+x|=1)\le(r+1)/2^r.
\]

The threshold is exact: an affine hyperplane of odd parity in `F_2^s` has
dimension `s-1` and contains all `s=r+1` unit vectors.  Thus the proof is not
silently using a stronger false intersection bound.

For `r=1` and full adjacency, the displacement flat is exactly
`{e_i,e_j}`.  Writing `M=(e_i+e_j)phi`, invertibility of
`I+M` is equivalent to `phi(e_i+e_j)=0`.  Direct squaring gives

\[
 F^2x=x+(e_i+e_j)\phi(e_i),
\]

so the affine order divides four.  This checks every characteristic-two
sign and rules out a hidden order-eight case.

## 4. Coordinate-cycle audit

For one cycle of a coordinate permutation, the Hamming contribution between
`X` and `gX` is the number of transitions in the cyclic binary incidence
word.  Total contribution two has a unique active coordinate cycle.  On a
cycle of length `ell`, a binary word with exactly two transitions is a
single nonempty proper cyclic interval, of which there are exactly
`ell(ell-1)`.

Such an interval has no nontrivial rotational stabilizer.  Hence its orbit
length is exactly `ell`, including the endpoint case `ell=2`.  Other
coordinate cycles are constant and contribute the factor `2^(c-1)`.  This
proves the exact formula, not merely an upper bound.

For every active cycle,

\[
 c-1\le n-\ell,
\]

because the remaining `n-ell` points support at most that many cycles.
Therefore

\[
 2^{c-1}\ell(\ell-1)
 \le2^{n-\ell}\ell^2.
\]

After restricting to `ell>=L`, summing `ell_i^2<=n^2` proves
`n^2 2^(n-L)`.  Restricting to the middle rank can only decrease the count.

## 5. Quantifier and counterexample audit

Three nearby constructions evade the theorems for legitimate reasons.

1. The standard partial pair-flip cycle is a long orbit only on its small
   tile, not a global affine neighbour permutation of the entire
   orientation cube.
2. A nonlinear Hamilton or circuit code in an orientation cube is not
   constrained by the affine-rank theorem.
3. A full wreath factor may use `Theta(W/m)` distinct cyclic orders, far
   above the lower bound `2^(Omega(sqrt(m)))`; it is not a small template
   family.

Conversely, the following tempting routes really are covered:

* one affine map per orientation stratum;
* one coordinate rotation, or one coordinate permutation, per radius;
* any `exp(o(sqrt(m)))` library of fixed coordinate generators whose
  bundles are their literal orbits.

No claim is made about arbitrary state-dependent choices of generators.

## 6. Checker audit

The command

```text
g++ -O2 -std=c++20 scratch/verify_shift_scd_algebra.cpp \
    -o /tmp/verify_shift_scd_algebra
/tmp/verify_shift_scd_algebra
```

checks:

* every invertible affine map and translation in dimensions `1,...,4`;
* the exact neighbour-fraction bound;
* the cycle-length-at-most-four conclusion in every full-neighbour case;
* every coordinate permutation through `n=8`;
* every cutoff `L`, the exact two-transition orbit formula and its global
  upper bound.

The observed output ends with

```text
coordinate n=8 permutations=40320 OK
all shift-compatible algebra checks passed
```

The checker is corroborative; the proofs above establish the results for all
dimensions.

## 7. Final ledger

Proved:

* affine-neighbour density bound `(r+1)/2^r`;
* affine full-neighbour order at most four;
* exact fixed-coordinate-action orbit formula;
* exponential template lower bound at typical SCD radius.

Still open:

* a nonlinear orientation-cube successor with coherent higher flags;
* a large Baranyai/wreath resolution with nested radii;
* the desired near shift-compatible SCD itself.

