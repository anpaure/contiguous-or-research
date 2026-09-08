# A constant quartet catalog gives pointwise pair-type diffusion

## 1. Result and scope

Partition `[2m]` randomly into disjoint quartets, leaving one additional
pair when `m` is odd.  For a set `S`, let `N_2(S)` be the number of quartets
containing exactly two elements of `S`.

For every fixed density margin `0<=rho<1`, there are constants

\[
                         c_\rho>0,\qquad K_\rho<\infty \tag{1.1}
\]

and a deterministic catalog of `K_rho` quartet partitions such that every
set satisfying

\[
                         ||S|-m|\le\rho m            \tag{1.2}
\]

has

\[
                         N_2(S)\ge c_\rho m           \tag{1.3}
\]

in at least one catalog member.

For the narrower band `||S|-m|=o(m)`, the constants can be absolute; for
example one may take

\[
                              c_*=1/8                \tag{1.4}
\]

and some absolute catalog size `K_*` for all sufficiently large `m`.

On each quartet choose independently and uniformly among its three perfect
matchings.  Conditional on a quartet partition and `S`, the number `F(S)`
of full matching pairs has the exact law

\[
                       F(S)=c(S)+\operatorname{Bin}(N_2(S),1/3). \tag{1.5}
\]

Consequently, for every central-band target, at least one catalog
**quartet partition** supports a random-frame type law with variance
`Omega(m)`.

This is pointwise type diffusion.  The good quartet partition may depend on
`S`, and the variance in (1.5) is over local frames.  The theorem does not
select one frame simultaneously for all targets, partition the middle
layer into cubes, or prove shadow coverage.

## 2. Random quartet partitions

Put

\[
                         g=\lfloor m/2\rfloor.       \tag{2.1}
\]

Take a uniform random permutation of `[2m]`, group the first `4g`
coordinates into consecutive unordered quartets, and, when `m` is odd,
leave the final two coordinates as an unordered leftover pair.  This gives
the uniform distribution on the corresponding set partitions.

Fix a set `S` of size `t`.  Each quartet is a uniform four-subset, so

\[
 p_2(t):=\Pr(|B\cap S|=2)
 ={\binom t2\binom{2m-t}2\over\binom{2m}4}.          \tag{2.2}
\]

Therefore

\[
                         \mathbb E N_2(S)=g p_2(t).  \tag{2.3}
\]

If `t=m+delta` and `|delta|<=rho m`, then uniformly in that band,

\[
 p_2(t)
 ={3\over8}\left(1-{\delta^2\over m^2}\right)^2+o(1), \tag{2.4}
\]

and hence

\[
 {\mathbb E N_2(S)\over m}
 \ge a_\rho-o(1),\qquad
 a_\rho:={3\over16}(1-\rho^2)^2.                    \tag{2.5}
\]

The formulas and asymptotics are unchanged by the odd leftover pair,
because `g=m/2+O(1)` and every quartet marginal remains uniform.

## 3. Uniform exponential lower tail

### Lemma 1 (quartet lower tail)

There is an absolute constant `b>0` such that, for every fixed `S` and every
`x>0`,

\[
 \Pr\{N_2(S)\le\mathbb EN_2(S)-x\}
 \le2\exp(-b x^2/m).                                \tag{3.1}
\]

#### Proof

View `N_2` as a function of the uniform permutation used in Section 2.
Transposing two permutation values changes at most two quartet blocks, and
hence changes `N_2` by at most two.  The standard bounded-difference
inequality for uniform random permutations gives (3.1), after absorbing its
absolute constant.  If one transposed value lies in the odd leftover pair,
only one quartet indicator can change, so the same bound applies.  QED.

For a fixed `rho<1`, take

\[
                         c_\rho={a_\rho\over2}
 ={3\over32}(1-\rho^2)^2.                            \tag{3.2}
\]

For all sufficiently large `m`, (2.5) gives
`E N_2(S)>=3a_rho m/4` uniformly in the band.  Thus (3.1) implies

\[
 \Pr\{N_2(S)<c_\rho m\}
 \le2e^{-\gamma_\rho m}                             \tag{3.3}
\]

for some `gamma_rho>0` depending only on `rho`.

In an `o(m)` band, (2.5) tends to `3/16`.  For all sufficiently large `m`,
the gap between the mean and `m/8` is bounded below by a fixed positive
multiple of `m`; hence

\[
 \Pr\{N_2(S)<m/8\}\le2e^{-\gamma_*m}                \tag{3.4}
\]

with one absolute `gamma_*>0`.

## 4. Constant-catalog theorem

### Theorem 2 (pointwise balanced-quartet catalog)

For every fixed `rho<1`, choose an integer

\[
                         K_\rho>{\log4\over\gamma_\rho}. \tag{4.1}
\]

Then for all sufficiently large `m` there exist `K_rho` quartet partitions
such that every set in the band (1.2) satisfies (1.3) in at least one of
them.

#### Proof

Choose the `K_rho` partitions independently.  For one fixed `S`, failure in
all catalog members has probability at most

\[
                         2^{K_\rho}e^{-K_\rho\gamma_\rho m}. \tag{4.2}
\]

There are at most `2^(2m)=4^m` sets to test.  The union-bound failure
probability is at most

\[
 \exp\{(\log4-K_\rho\gamma_\rho)m+K_\rho\log2\},    \tag{4.3}
\]

which tends to zero by (4.1).  Hence a deterministic catalog exists.  QED.

Using (3.4) instead gives an absolute

\[
                         K_*>{\log4\over\gamma_*}    \tag{4.4}
\]

for every prescribed `o(m)` central band, once `m` is sufficiently large.
The constants are deliberately not optimized.

The quantifier is

\[
 \boxed{\text{for every }S\text{, at least one catalog partition is good}.} \tag{4.5}
\]

It is not asserted that one catalog partition is good for every `S`, or
that every catalog member is good for a fixed `S`.

## 5. Exact local-frame law

Fix one quartet partition.  On every quartet independently choose one of
its three perfect matchings with probability `1/3`; use the unique leftover
pair when `m` is odd.  Let `n_j(S)` count quartets containing `j` elements
of `S`.

The full-pair contribution of one quartet is:

\[
\begin{array}{c|ccccc}
j&0&1&2&3&4\\ \hline
\text{full pairs}&0&0&\operatorname{Bernoulli}(1/3)&1&2.
\end{array}                                          \tag{5.1}
\]

At `j=2`, exactly one of the three local perfect matchings pairs the two
selected coordinates together; the other two match selected to unselected.
Different quartets are independent.  Therefore, exactly,

\[
 F(S)=c(S)+\operatorname{Bin}(n_2(S),1/3),           \tag{5.2}
\]

where

\[
 c(S)=n_3(S)+2n_4(S)
       +1_{\{\text{the odd leftover pair is contained in }S\}}. \tag{5.3}
\]

In particular,

\[
 \mathbb EF(S)=c(S)+{n_2(S)\over3},\qquad
 \operatorname{Var}F(S)={2n_2(S)\over9}.            \tag{5.4}
\]

For the good catalog member supplied by Theorem 2,

\[
                         \operatorname{Var}F(S)
 \ge {2c_\rho\over9}m=\Omega_\rho(m).               \tag{5.5}
\]

The number of empty pairs is then determined by rank:

\[
                         E(S)=F(S)+m-|S|.            \tag{5.6}
\]

Thus the local full/empty type moves over a window of natural width
`Theta(sqrt(m))`, instead of being frozen by one global matching.

## 6. Boundary of the conclusion

Theorem 2 and (5.2) jointly say:

> Every central-band set has at least one member of a constant quartet
> catalog for which uniform independent local frames give a full-pair type
> distribution of variance `Omega(m)`.

They do not say:

* that the same catalog member is good for all targets;
* that one fixed local frame gives variance--a fixed frame is deterministic;
* that a constant number of sampled frames realizes the binomial law
  uniformly over all targets;
* that target-dependent choices can be combined into one cube partition;
* that source and target types admit a joint matching;
* that radius, shift, pinning, or shadow constraints are satisfied.

Accordingly this is a pointwise type-diffusion catalog, not a joint cube
partition or a shadow theorem.

## 7. Finite checker

`scratch/check_quartet_diffusion_catalog.py` verifies the exact quartet
expectation and the conditional shifted-binomial law by exhaustive
enumeration for small even and odd `m`.  The catalog existence proof is the
large-deviation and union-bound argument above, not a computational search.
