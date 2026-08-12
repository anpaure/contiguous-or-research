# Independent audit of the quartet diffusion catalog

## 1. Verdict

`QUARTET_DIFFUSION_CATALOG.md` is valid with its stated pointwise scope.

For each fixed central density margin `rho<1`, a constant number of quartet
partitions suffices so that every set in the corresponding band has a linear
number of two-selected quartets in at least one catalog member.  In an
`o(m)` band, both the linear constant and catalog size can be absolute.

Conditional on one quartet partition, independent uniform choice among the
three local perfect matchings gives the exact shifted-binomial full-pair
law and variance `2N_2/9`.

The theorem does not make a simultaneous frame choice, and no cube or
shadow conclusion follows.

## 2. Quartet expectation and odd boundary

A random quartet is a uniform four-subset of `[2m]`, whether `2m` is a
multiple of four or two coordinates are left over.  Therefore, for
`|S|=t`,

\[
 \Pr(|B\cap S|=2)
 ={\binom t2\binom{2m-t}2\over\binom{2m}4}.
\]

There are `g=floor(m/2)` quartet blocks, so linearity of expectation gives
the claimed exact mean.  No independence between quartet indicators is
being assumed.

Writing `t=m+delta`, direct expansion gives, uniformly for
`|delta|<=rho m` with fixed `rho<1`,

\[
 p_2(t)={3\over8}(1-\delta^2/m^2)^2+o(1).
\]

Multiplication by `g/m=1/2+O(1/m)` yields the lower limiting density

\[
 a_\rho={3\over16}(1-\rho^2)^2>0.
\]

For odd `m`, a random permutation followed by `g` four-blocks and one
two-block is uniform over all such set partitions.  Transpositions involving
the leftover block affect no more quartet indicators than in the even case.
Thus neither expectation nor concentration acquires an unhandled boundary
term.

## 3. Exponential lower-tail audit

As a function of the underlying uniform permutation, `N_2(S)` changes by at
most two under a transposition: only the two blocks containing the exchanged
coordinates can change.  The standard bounded-difference theorem for random
permutations therefore gives

\[
 \Pr(N_2\le\mathbb EN_2-x)
 \le2\exp(-b x^2/m)
\]

for an absolute `b>0`.  The source deliberately leaves `b` unspecified, so
there is no fragile constant transcription.

With `c_rho=a_rho/2`, the uniform mean is at least `3a_rho m/4` for all
sufficiently large `m`; the gap to `c_rho m` is at least `a_rho m/4`.
Consequently the failure probability is `2exp(-gamma_rho m)` for a positive
constant depending only on `rho`.

For an `o(m)` band, the mean density tends uniformly to `3/16`.  The fixed
threshold `1/8` leaves a linear gap, so one absolute exponential constant
works eventually for every prescribed such band.

## 4. Catalog union-bound quantifiers

For one fixed target, failure of all `K` independently sampled quartet
partitions has probability at most

\[
                         2^K e^{-K\gamma m}.
\]

Union bounding over all subsets, not merely the central band, costs at most
`4^m`.  Thus

\[
 \Pr(\text{some target has no good catalog member})
 \le\exp((\log4-K\gamma)m+K\log2).
\]

Any fixed integer `K>log(4)/gamma` makes this tend to zero.  This proves
existence of a deterministic constant-size catalog.

Increasing `K` helps because the required event is “at least one good
catalog member for each target.”  It would not prove that every catalog
member is good, and the source explicitly records the correct quantifier.

The catalog may depend on `m` and on the fixed margin `rho`; only its
cardinality is bounded independently of `m`.

## 5. Shifted-binomial law

On a quartet containing `j` selected coordinates:

* `j=0,1` contributes no full pair under any local matching;
* `j=3` contributes exactly one;
* `j=4` contributes exactly two;
* `j=2` contributes one under exactly one of the three local perfect
  matchings and zero under the other two.

Independent uniform local frames therefore make the rank-two contributions
independent Bernoulli variables of parameter `1/3`.  The odd leftover pair
is fixed and contributes one exactly when both its coordinates lie in `S`.
This proves

\[
 F(S)=n_3+2n_4+1_{\rm leftover\subseteq S}
       +\operatorname{Bin}(n_2,1/3).
\]

Hence

\[
 \operatorname{Var}F(S)=n_2(1/3)(2/3)=2n_2/9.
\]

The empty-pair identity is also correctly signed.  From
`2F+R=|S|` and `F+E+R=m`,

\[
                              E=F+m-|S|.
\]

For the target's good catalog partition, `n_2>=c_rho m`, so the frame law
has variance `Omega_rho(m)` and standard deviation `Theta_rho(sqrt(m))`.

## 6. Scope audit

A fixed frame has a deterministic type and therefore cannot itself “have
variance.”  The accepted statement is:

> for every target, at least one catalog quartet partition supports a
> conditional random-frame distribution with variance `Omega(m)`.

The good partition may differ with the target.  Choosing target-dependent
partitions or frames does not yield one global cube partition.  The theorem
also gives no joint source-target coupling, discrepancy control,
standard-RSK radius ledger, cyclic order, or shadow injectivity.

The phrase “pointwise type diffusion” accurately captures the result.  A
joint diffusion or matching theorem remains open.

## 7. Machine audit

`scratch/check_quartet_diffusion_catalog.py` exhaustively enumerates all
quartet partitions through `m=5`, including odd leftover pairs.  It checks
the exact average of `N_2(S)` for every subset and the complete local-frame
full-pair distribution against the shifted binomial law on a deterministic
sample of structures.

The outputs include 1,575 quartet-plus-leftover structures at `m=5`; all
checks pass.  The asymptotic catalog theorem uses the analytic tail and
union bound, not a search.
