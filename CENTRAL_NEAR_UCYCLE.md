# Central near-Ucycles: a uniformity audit

This note audits the difference-form construction of Curtis, Hines,
Hurlbert, and Moyer (CHHM),
[*Near universal cycles for subsets exist*](https://arxiv.org/abs/0809.3725),
in the central regime

\[
 n=2m,\qquad k=m.                                          \tag{0.1}
\]

Only proved claims are included.  The conclusion is negative for this
specific construction:

> The CHHM theorem is a fixed-`k` theorem and its proof is not uniform at
> `k=n/2`.  More strongly, the family that its Euler tour actually lists
> omits a positive proportion of the central layer.  Hence the construction
> does not produce a near-width queue row in the central regime.

This does **not** prove that central near-Ucycles do not exist.  It proves
that the published difference-form argument does not establish them and
that its chosen family of forms cannot do so.

## 1. What the published theorem says

For fixed `k`, CHHM construct an `(n,k)` Ucycle packing whose windows are
precisely the **awesome** `k`-subsets.  If

\[
 S=\{s_1,\ldots,s_k\}\subseteq\mathbb Z/n\mathbb Z
\]

is written in cyclic order, its gap composition is

\[
 d(S)=(d_1,\ldots,d_k),\qquad d_i\ge1,\qquad
 \sum_i d_i=n.                                             \tag{1.1}
\]

A composition is good if some part size has multiplicity exactly one.  It
is awesome if some such unique part is greater than one.  The Eulerian
transition graph in CHHM lists all awesome subsets.

The asymptotic statement proved in the paper is

\[
 p_{n,k}=(1-o(1))\binom nk\qquad(n\longrightarrow\infty)
                                                               \tag{1.2}
\]

for each fixed `k`.  Fixed `k` is part of both the definition and the proof.
The later paper
[*Universal Cycle Packings and Coverings for k-Subsets of an n-Set*](https://doi.org/10.1007/s00373-016-1727-6)
explicitly notes that Schur's theorem is the reason the CHHM argument works
only for constant `k`; its growing-`k` result reaches `k=o(n)`, not linear
`k`.

## 2. Exact central composition model

There is no approximation in the following reduction.

### Proposition 1 (rooted subsets are uniform compositions)

Choose an `m`-subset `S` of the cyclic set `[2m]` and then distinguish one
element of `S`.  Reading clockwise from that root gives a composition of
`2m` into `m` positive parts.  Conversely, a root and such a composition
reconstruct the subset.

Consequently, for every rotation-invariant property `P` of the gap
composition,

\[
 \frac{\#\{S\in\binom{[2m]}m:d(S)\text{ has }P\}}
      {\binom{2m}m}
 =
 \frac{\#\{(d_1,\ldots,d_m)>0:\sum d_i=2m, P\}}
      {\binom{2m-1}{m-1}}.                                \tag{2.1}
\]

#### Proof

There are `m binom{2m}{m}` rooted subsets.  There are `2m` choices of root
and `binom{2m-1}{m-1}` positive compositions.  The identity

\[
 m\binom{2m}m=2m\binom{2m-1}{m-1}
\]

and the explicit clockwise bijection prove the assertion.  QED.

Subtracting one from every gap turns (1.1) into a uniform weak composition

\[
 y_1+\cdots+y_m=m,\qquad y_i\ge0.                          \tag{2.2}
\]

There is also an exact probabilistic representation.  Let `X_1,...,X_m` be
independent with

\[
 \Pr(X_i=r)=2^{-r},\qquad r=1,2,\ldots .                  \tag{2.3}
\]

For every positive vector with sum `2m`, its probability under (2.3) is
`2^{-2m}`.  Therefore

\[
 (X_1,\ldots,X_m)\ \big|\ \sum_iX_i=2m                  \tag{2.4}
\]

is exactly the uniform gap composition in Proposition 1.

This is the central phenomenon hidden by the fixed-dimensional Schur
calculation: part sizes around `log_2 m` have occupancy of constant order.
Singleton multiplicities at those sizes do not disappear automatically.

## 3. Exact points where the fixed-`k` proof loses uniformity

There are three independent failures.

### 3.1 Pointwise Schur asymptotics are summed over growing patterns

For a multiplicity pattern

\[
 P=\langle p_1,\ldots,p_t\rangle,\qquad \sum p_i=k,
\]

CHHM invoke Schur's fixed-dimensional asymptotic for the number of positive,
distinct solutions of

\[
 p_1x_1+\cdots+p_tx_t=n.                                  \tag{3.1}
\]

They compare a bad pattern with a good pattern having one additional
singleton and obtain, pointwise,

\[
 \frac{c(P)}{c(\phi(P))}\sim
 \frac{t(p_t-1)}{p_t n}.                                  \tag{3.2}
\]

For fixed `k`, both `t` and the coefficients `p_i` are fixed, and (3.2) is
`o(1)`.  At `k=m=n/2`, one may have `t=Theta(n)`, in which case the right
side is only `O(1)`.  Moreover, the number of patterns itself grows with
`m`; pointwise asymptotic errors cannot be summed without a uniform estimate.

Thus (3.2) contains no central-regime conclusion.

### 3.2 The non-awesome estimate is outside its stated domain

The final CHHM count of good but non-awesome classes transforms its equation
to one with residual parameter

\[
 n-2k-1                                                    \tag{3.3}
\]

and explicitly assumes `n>2k`.  At the central point `n=2k`, (3.3) equals
`-1`.  The displayed Schur estimate is not merely weak there; it is being
applied outside the feasible domain of the transformed composition problem.

### 3.3 The available error term becomes vacuous

As recorded in the later audit by Dębski and Lonc, the CHHM proof gives, for
fixed `k`, an error of order `O(n^(k-1))`.  Substituting `n=2m,k=m` into a
fixed-parameter big-O statement is not logically valid.  Even as a formal
expression,

\[
 (2m)^{m-1}\gg \binom{2m}m\asymp\frac{4^m}{\sqrt{m}},     \tag{3.4}
\]

so it would give no nontrivial central estimate.

## 4. A positive-density obstruction for the CHHM family

The loss of uniformity reflects a real obstruction in the selected family,
not just an incomplete estimate.

### Theorem 2 (non-good central compositions have positive density)

There is an absolute constant `delta>0` such that, for all sufficiently
large `m`, at least

\[
 \delta\binom{2m-1}{m-1}                                  \tag{4.1}
\]

compositions of `2m` into `m` positive parts have no part size of
multiplicity exactly one.

Equivalently, by Proposition 1, at least

\[
 \delta\binom{2m}m                                        \tag{4.2}
\]

central subsets are non-good, and hence non-awesome.

#### Proof

Use the geometric representation (2.3)--(2.4).  Fix a sufficiently large
integer `C`, and put

\[
 J=\lfloor\log_2m\rfloor-C,\qquad q=2^{-J},\qquad
 \lambda=mq.                                               \tag{4.3}
\]

Then

\[
 2^C\le\lambda<2^{C+1}.                                   \tag{4.4}
\]

Let `E` be the event that every `X_i` is at most `J`.  Since
`Pr(X_i>J)=q`,

\[
 \Pr(E)=(1-q)^m                                             \tag{4.5}
\]

is bounded below by a positive constant depending only on `C`.

Conditioned on `E`, the variables remain independent, with truncated law

\[
 \Pr(Y=r)=\frac{2^{-r}}{1-q},\qquad 1\le r\le J.          \tag{4.6}
\]

Its mean is

\[
 \mu_J=2-\frac{Jq}{1-q},                                  \tag{4.7}
\]

its variance tends to `2`, its third absolute moment is uniformly bounded,
and its lattice span is one.  The target `2m` differs from `m mu_J` by

\[
 \frac{Jmq}{1-q}=O(\log m)=o(\sqrt m).                    \tag{4.8}
\]

The lattice local central limit theorem, uniformly for this truncated
triangular array, therefore gives

\[
 \Pr\left(\sum_{i=1}^mY_i=2m\right)\ge\frac{c_0}{\sqrt m} \tag{4.9}
\]

for an absolute `c_0>0` and all large `m`.

Let `N_r` be the number of occurrences of value `r` among the `Y_i`.  Put

\[
 u_r=m\Pr(Y=r).
\]

Writing `r=J-s`, (4.4) gives

\[
 u_{J-s}\ge2^{C+s}.                                       \tag{4.10}
\]

Consequently

\[
 \sum_{r=1}^J\Pr(N_r=1)
 \le
 \sup_{u\ge2^C}\sum_{s\ge0}2^su\exp(-2^su/2)
 =:\eta_C,                                                 \tag{4.11}
\]

where `eta_C -> 0` as `C -> infinity`.

We need the same estimate on the local event in (4.9), rather than only
unconditionally.  If `N_r=1`, expose the unique index having value `r`.
The other `m-1` variables have the law (4.6) conditioned not to equal `r`.
These laws have uniformly bounded moments and uniformly positive variance.
More directly, their largest atom is at most `2/3+o(1)`, uniformly in `r`:
removing `r=1` leaves value `2` with limiting mass `1/2`, removing `r=2`
leaves value `1` with limiting mass `2/3`, and every other removal is less
concentrated.  The Kolmogorov--Rogozin lattice concentration inequality
therefore bounds every atom of their sum by `O(m^(-1/2))`, uniformly in `r`
and `J`.  Hence, for an absolute `C_1`,

\[
 \Pr\left(N_r=1,\ \sum_iY_i=2m\right)
 \le \frac{C_1}{\sqrt m}\Pr(N_r=1).                      \tag{4.12}
\]

Summing (4.12), then choosing the fixed `C` so large that
`C_1 eta_C<c_0/2`, yields

\[
 \Pr\left(\sum_iY_i=2m,\ N_r\ne1\text{ for every }r\right)
 \ge\frac{c_0}{2\sqrt m}.                                \tag{4.13}
\]

Multiplying by `Pr(E)` gives the corresponding lower bound for the original
geometric variables.  Finally,

\[
 \Pr\left(\sum_iX_i=2m\right)
 =2^{-2m}\binom{2m-1}{m-1}
 \sim\frac{1}{2\sqrt{\pi m}}.                             \tag{4.14}
\]

Dividing (4.13), with the factor (4.5), by (4.14) proves that the conditional
probability of having no singleton part size is bounded below by a positive
constant.  Equations (4.1)--(4.2) follow.  QED.

### Corollary 3 (the CHHM central packing is not near-width)

Let `A_m` be the number of awesome `m`-subsets of `[2m]`.  Then

\[
 A_m\le(1-\delta)\binom{2m}m                               \tag{4.15}
\]

for all sufficiently large `m`.  Since the CHHM Euler tour lists precisely
the awesome subsets, its central specialization has a linear, not
`o(W(2m))`, deficit.

## 5. What a genuine central near-Ucycle would give

Although CHHM does not supply one, the queue implication itself is exact.

### Proposition 4 (near-Ucycle to queue row)

Suppose a cyclic word

\[
 w=(w_0,\ldots,w_{L-1})\in[2m]^L                          \tag{5.1}
\]

has the property that its cyclic windows of length `m` are distinct
`m`-subsets.  Define

\[
 T_i=\{w_i,w_{i+1},\ldots,w_{i+m-1}\}.                    \tag{5.2}
\]

Then:

1. `T` is a simple cycle in `J(2m,m)`;
2. its adjacent shadows are the pure-rank windows

   \[
   T_i\cap T_{i+1}=\{w_{i+1},\ldots,w_{i+m-1}\},\qquad
   T_i\cup T_{i+1}=\{w_i,\ldots,w_{i+m}\};                \tag{5.3}
   \]

3. every maximal coordinate 1-run in the incidence word of `T` has length
   exactly `m`;
4. the singleton-mask word

   \[
    A_i=\{w_i\}                                             \tag{5.4}
   \]

   satisfies `D^(m-1) A=T`.

If `L=(1-o(1)) binom{2m}{m}`, this is a near-width queue-type middle row with
the strongest possible uniform run structure.

#### Proof

Every length-`m` word segment has distinct symbols.  Equal symbols therefore
have cyclic distance at least `m`.  Distance exactly `m` is also impossible:
if `w_i=w_(i+m)`, then the windows starting at `i` and `i+1` have the same
underlying set, contrary to distinctness.  Hence equal occurrences are at
cyclic distance at least `m+1`.

It follows that

\[
 T_{i+1}=T_i\setminus\{w_i\}\cup\{w_{i+m}\}
\]

is a Johnson transition and the `T_i` are distinct.  The same separation
gives (5.3).  One occurrence of a symbol belongs to exactly the `m`
consecutive middle windows whose starting indices range from `i-m+1`
through `i`.  The separation just proved makes these blocks disjoint and
separated by at least one zero, so every maximal 1-run has length exactly
`m`.  Finally, (5.4) makes every `m`-window OR equal to (5.2), proving
`D^(m-1)A=T`.  QED.

## 6. Consequences and non-consequences for contiguous OR arrays

Proposition 4 would solve one important part of the OR problem:

* nearly every middle mask would occur;
* factorization would be automatic, using singleton entries; and
* the coordinate-run obstruction would disappear completely.

It would **not by itself** prove an asymptotically optimal universal OR
array.  The lower and upper derivative rows of (5.3) are the sets of symbols
appearing in shorter and longer word windows.  Coverage of almost every
length-`m` window does not imply that every rank `m-j` and `m+j` subset occurs
as a window.  In particular, the Ucycle condition supplies Johnson adjacency
and the first intersection/union shadows, but no complete deep-shadow
theorem.

For the CHHM word there is an earlier obstruction: Corollary 3 says the
middle row itself already misses `Omega(W(2m))` vertices.  Adding those
missing middle masks literally costs order `W(2m)`, so this construction
cannot yield a `W(2m)+o(W(2m))` OR array.

## 7. The exact remaining question

The correct central Ucycle statement is separate from the CHHM theorem:

> Does there exist a cyclic word on `[2m]` with
> `(1-o(1)) binom{2m}{m}` distinct length-`m` subset windows?

The 2016 paper cited above proves near-Ucycles for `k=o(n)` and explicitly
leaves the linear regime open.  Nothing in the audited difference-form proof
settles this question at `k=n/2`.

Even a positive answer would still require a simultaneous-shadow theorem to
finish the OR construction.  The defensible ledger is therefore:

\[
\begin{array}{c|c}
\text{claim}&\text{status}\\ \hline
\text{CHHM near-Ucycle for fixed }k&\text{proved}\\
\text{same proof uniformly for }k=n/2&\text{fails at Sections 3--4 above}\\
\text{CHHM awesome family near-width at }k=n/2&\text{false}\\
\text{central near-Ucycle by another construction}&\text{open}\\
\text{central near-Ucycle implies queue row with runs }m&\text{proved}\\
\text{that queue row alone implies universal OR coverage}&\text{not proved}
\end{array}
\]
