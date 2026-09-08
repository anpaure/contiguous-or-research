# Current-scale external rows: product means, exact slices, and the three-carrier gate

**Date:** 2026-08-22  
**Status:** unconditional product/slice order-two row energy and summable
signed sixth-moment collision forcing. Gate A still needs stopped-law
control of this collision scalar and, separately, of the purge
high-degree-incidence scalar.

This note studies the external conflict-row variable at the *current*
independent-residual degree scale.  It proves four facts.

1. Conditional on a configuration `G` and an external target `v`
   surviving, the mean of `a_G(v)` has an exact powered-overlap formula.
   The sum of these powered means over all external `v` is controlled by
   the existing one-carrier boundary polymer theorem.
2. Every factorial moment through order six, and the aggregate collision
   scalar used by the microbite hierarchy, transfers term by term from
   product measure to uniform exact shore slices with exponentially small
   relative error.
3. The core three-carrier flower is `O(1/(rx^5))` relative to its linear
   scale.  Absolute control of every higher factorial order would require
   a decorated-flower kernel.
4. Recombining those orders with their signed centered-sixth coefficients
   gives an exact shifted second-difference formula.  Its product and
   exact-slice forcing, including the random moving-center correction, is
   summable through `alpha<1/18`; transfer of this nonnegative collision
   scalar to the stopped adaptive law remains open. This does not replace
   the separate stopped purge-incidence comparison.

No time-zero absolute degree is used as a proxy for a current degree.

## 1. Product residual and the external row

Let `mathcal C_r` be the directed punctured-configuration hypergraph.
Each configuration contains `2r` middle and `2r` lower targets.  Write

\[
 d_M=D_M=2r\,r!(r+1)!,\qquad
 d_L=D_L={r+2\over r}D_M.                            \tag{1.1}
\]

Retain middle targets independently with probability `y` and lower
targets independently with probability `x`, where

\[
                         1\ge y\ge x\ge r^{-\alpha}. \tag{1.2}
\]

Put `p_M=y`, `p_L=x`, and

\[
 q_0=x^{2r}y^{2r},\qquad
 \mu_\sigma={d_\sigma q_0\over p_\sigma}.            \tag{1.3}
\]

Thus `mu_sigma` is the product-law mean residual degree conditional on a
fixed shore-`sigma` target being retained.

Fix an original configuration `G` and a target `v in V_sigma-G`.
Conditional on retaining every target of `G` and retaining `v`, let

\[
 A_{G,v}=a_G(v)
 =|\{F\in\mathcal C_r:v\in F,\ F\cap G\ne\varnothing,
                         \ F\hbox{ survives}\}|.      \tag{1.4}
\]

For real `c>=1`, define the deterministic powered external kernel

\[
 K_c(G,v)={1\over d_\sigma}
 \sum_{\substack{F\ni v\\F\cap G\ne\varnothing}}
 \prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.  \tag{1.5}
\]

### Proposition 1.1 (exact conditional mean)

\[
 \boxed{\mathbb E[A_{G,v}\mid G\cup\{v\}\text{ retained}]
       =\mu_\sigma K_1(G,v).}                        \tag{1.6}
\]

#### Proof

For `F ni v`, the unconditional survival probability is `q_0`.  Since
`v notin G`, conditioning on `G union {v}` removes from that monomial the
factor `p_sigma` and one factor `p_(sh(u))` for each `u in F cap G`.
Hence

\[
 \Pr(F\text{ survives}\mid G\cup\{v\}\text{ retained})
 ={q_0\over p_\sigma}
   \prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-1}. \tag{1.7}
\]

Sum (1.7) over the family in (1.4) and use (1.3).  \(\square\)

## 2. Aggregate powered-mean theorem

We use the proved boundary-codegree estimate.  If `T` is a target family
inside one configuration, `t=|T|>=2`, and its boundary subgraph has `q(T)`
vertices, then for an absolute `C`,

\[
                         {\deg(T)\over D_M}
                    \le C^t r^{2-q(T)}.              \tag{2.1}
\]

The associated bounded-degree polymer estimate says, for sufficiently
small absolute `c_0` and `0<=z<=c_0 sqrt(r)`,

\[
 \sum_{\substack{T\subseteq G\\|T|\ge2}}
 |T|^2z^{|T|}r^{-q(T)}
 =O\left({z^2\over r^2}+{z^4\over r^2}\right).       \tag{2.2}
\]

### Theorem 2.1 (aggregate current-scale external means)

Fix `c>=1` and assume

\[
                              c\alpha<{1\over3}.       \tag{2.3}
\]

Uniformly in the configuration `G` and in either shore,

\[
 \boxed{
 \sum_{v\in V_\sigma-G}K_c(G,v)=O_c(r^2x^{-c}).}     \tag{2.4}
\]

In particular, (2.4) holds simultaneously for `1<=c<=6` when
`alpha<1/18`.  It holds through `c=5` in the larger optimized range
`alpha<1/15`.

#### Proof

For `F`, put `t_F=|F cap G|` and define

\[
 W_c(G)=\sum_{F:t_F>0}
              \prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.
                                                               \tag{2.5}
\]

Since all retention probabilities are at least `x`, with
`a_c=x^{-c}-1`,

\[
 W_c(G)\le\sum_{F:t_F>0}x^{-ct_F}
 =|\Gamma(G)|+
   \sum_{\varnothing\ne T\subseteq G}a_c^{|T|}\deg(T).       \tag{2.6}
\]

Here `Gamma(G)` is the closed conflict neighbourhood.  The elementary
incidence bound and (1.1) give

\[
 |\Gamma(G)|\le\sum_{u\in G}d(u)=4(r+1)D_M,          \tag{2.7}
\]

and the singleton part of the last sum in (2.6) is at most
`4(r+1)D_M a_c`.  For `|T|>=2`, (2.1)--(2.2), with `z=Ca_c`, give

\[
 \sum_{|T|\ge2}a_c^{|T|}\deg(T)
 \le D_Mr^2
   \sum_{|T|\ge2}(Ca_c)^{|T|}r^{-q(T)}
 =O_c(D_M(a_c^2+a_c^4)).                             \tag{2.8}
\]

The activity condition follows from `c alpha<1/3<1/2`.  Moreover
`a_c^4=O(x^{-4c})=O(rx^{-c})` under (2.3).  Thus

\[
                         W_c(G)=O_c(D_Mrx^{-c}).       \tag{2.9}
\]

Now interchange `v` and `F` in (1.5).  A configuration contains at most
`2r` external targets of a prescribed shore, so

\[
 \begin{aligned}
 sum_{v\in V_\sigma-G}K_c(G,v)
 &={1\over d_\sigma}
   \sum_{F:t_F>0}|(F-G)\cap V_\sigma|
      \prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}\\
 &\le {2r\over d_\sigma}W_c(G)
 =O_c(r^2x^{-c}),
 \end{aligned}                                       \tag{2.10}
\]

because `d_sigma>=D_M`.  \(\square\)

Theorem 2.1 is an aggregate theorem for conditional *means*.  It does not
assert a maximum bound for `K_c(G,v)`, and it does not turn the realized
random variable `A_(G,v)` into its mean.

The complete initial pair profile supplies one more deterministic fact:

\[
 a_G^{(0)}(v):=|\{F\in\mathcal C_r:v\in F,\ F\cap G\ne\varnothing\}|
 \le {32D_M\over r},\qquad v\notin G.                \tag{2.11}
\]

This is only a cap on the number of candidate configurations.  The next
argument thins those candidates at the current product scale; it does not
identify `D_M/r` with a residual degree.

### Theorem 2.2 (aggregate second-factorial row energy)

Assume `alpha<1/6`.  Uniformly in `G` and either shore,

\[
 \boxed{
 \sum_{v\in V_\sigma-G}
 \mathbb E[(A_{G,v})_2\mid G\cup\{v\}\text{ retained}]
 =O(\mu_\sigma^2 r x^{-5}).}                         \tag{2.12}
\]

Moreover,

\[
 \sum_{v\in V_\sigma-G}
 \mathbb E[A_{G,v}\mid G\cup\{v\}\text{ retained}]
 =\Omega(\mu_\sigma r^2),                            \tag{2.13}
\]

and consequently

\[
 \boxed{
 {\sum_v\mathbb E(A_{G,v})_2
       \over
   \mu_\sigma\sum_v\mathbb EA_{G,v}}
 =O\left({1\over r x^5}\right)=o(1).}               \tag{2.14}
\]

All expectations in (2.12)--(2.14) have the conditioning displayed in
(2.12).

#### Proof

For a candidate `F`, put

\[
 s_F=\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-1},
 \qquad w_\sigma={q_0\over p_\sigma}={\mu_\sigma\over d_\sigma}.
                                                               \tag{2.15}
\]

Thus its conditional survival probability is `w_sigma s_F`.  Cauchy's
inequality and (2.11) give, pointwise in `G,v`,

\[
 K_1(G,v)^2
 \le {a_G^{(0)}(v)\over d_\sigma}K_2(G,v)
 \le {32\over r}K_2(G,v).                            \tag{2.16}
\]

Summing and applying Theorem 2.1 with `c=2` yields

\[
                         \sum_vK_1(G,v)^2=O(rx^{-2}). \tag{2.17}
\]

For two distinct candidates `F,H`, independence of target retentions
gives the exact conditional factorization

\[
 \Pr(F,H\text{ survive}\mid G,v)
 =w_\sigma^2s_Fs_H
 \prod_{u\in(F\cap H)-(G\cup\{v\})}
             p_{\operatorname{sh}(u)}^{-1}.          \tag{2.18}
\]

The product `1` part of (2.18), summed over ordered `F ne H`, is at most
`mu_sigma^2 K_1(G,v)^2`.  For the remaining correction, put
`t(F,H)=|(F cap H)-{v}|`.  Since all `p_u>=x` and
`s_Fs_H<=(s_F^2+s_H^2)/2`, symmetry gives

\[
 \begin{aligned}
 &w_\sigma^2\sum_{F\ne H}s_Fs_H
 \left[
  \prod_{u\in(F\cap H)-(G\cup\{v\})}p_u^{-1}-1
 \right]\\
 &\quad\le
 w_\sigma^2\sum_Fs_F^2
       \sum_{H\ni v,\ H\ne F}(x^{-t(F,H)}-1).       \tag{2.19}
 \end{aligned}
\]

In the outer sum `F` remains restricted to the candidates, while enlarging
the inner sum to the whole star of `v` only increases it.  The proved
rooted overlap kernel gives

\[
 {1\over d_\sigma}\sum_{H\ni v,\ H\ne F}
       (x^{-t(F,H)}-1)=O((rx^3)^{-1}).                \tag{2.20}
\]

Also `sum_F s_F^2=d_sigma K_2(G,v)`.  Since
`w_sigma d_sigma=mu_sigma`, (2.18)--(2.20) imply

\[
 \mathbb E(A_{G,v})_2
 \le\mu_\sigma^2
 \left[K_1(G,v)^2+O((rx^3)^{-1})K_2(G,v)\right].     \tag{2.21}
\]

Sum (2.21), use (2.17), and use (2.4) with `c=2` once more.  This gives

\[
 \sum_v\mathbb E(A_{G,v})_2
 =O\left(\mu_\sigma^2
   [rx^{-2}+rx^{-5}]\right)
 =O(\mu_\sigma^2rx^{-5}),                            \tag{2.22}
\]

which is (2.12).

It remains to prove the denominator bound.  All weights in `K_1` are at
least one, so, with `C_G=|Gamma(G)|`,

\[
 \begin{aligned}
 \sum_{v\in V_\sigma-G}K_1(G,v)
 &\ge {1\over d_\sigma}
       \sum_{F:F\cap G\ne\varnothing}|(F-G)\cap V_\sigma|\\
 &={2r(C_G-d_\sigma)\over d_\sigma}=\Omega(r^2).     \tag{2.23}
 \end{aligned}
\]

The equality uses
`sum_F |F cap G cap V_sigma|=2r d_sigma`.  Finally
`C_G=4rD_M+O(D_M)` follows from
`sum_(u in G)d(u)=4(r+1)D_M` and the proved pair-mass bound
`sum_F binom(|F cap G|,2)=O(D_M)`.  Equations (1.6) and (2.23) prove
(2.13), and division proves (2.14).  \(\square\)

## 3. Exact factorial-moment de-Poissonization

Let `N_sigma=|V_sigma|`, and independently choose a uniform
`m_sigma`-subset of each shore, where

\[
 p_\sigma={m_\sigma\over N_\sigma}\ge x.             \tag{3.1}
\]

The resulting induced hypergraph is the exact-slice residual.  Product
measure below always uses the same two densities `p_sigma`.

### Theorem 3.1 (one external row, exact slice)

Fix `G`, `v notin G`, and condition in both models on retaining
`G union {v}`.  For every fixed `1<=j<=6`,

\[
 \boxed{
 \mathbb E_{\rm sl}(A_{G,v})_j
 =\left(1+O_j\left({r^2\over xN_*}\right)\right)
   \mathbb E_{\rm prod}(A_{G,v})_j,}                 \tag{3.2}
\]

where `N_*=min_sigma N_sigma`.  In the punctured shores the error is
`e^{-Omega_j(r)}`.

#### Proof

Expand `(A_(G,v))_j` as a sum over ordered distinct configurations
`F_1,...,F_j` through `v`, each meeting `G`.  A summand is the indicator
that the union of these configurations survives.  After the conditioned
root `G union {v}` is removed, this union queries at most `O_j(r)` targets
on either shore.

For a queried `s`-set on one shore, the exact conditional slice
probability is

\[
 {(m_\sigma-r_\sigma)_s\over(N_\sigma-r_\sigma)_s},  \tag{3.3}
\]

where `r_sigma=|(G union {v}) cap V_sigma|=O(r)`.  Comparing (3.3) with
`p_sigma^s`, termwise logarithmic expansion gives relative error

\[
                  1+O_j(r^2/(xN_\sigma)).             \tag{3.4}
\]

The replacement of `(m-r_sigma)/(N-r_sigma)` by `m/N` has the same
smaller order.  The two shores are independent.  Since all summands are
nonnegative and (3.4) is uniform, it survives summation.  Finally
`N_*=exp(Omega(r))`, proving the last assertion.  \(\square\)

Thus exact cardinalities create no further obstruction for any proposed
sixth-factorial-moment row theorem.

## 4. The aggregate collision scalar

In any residual `H`, define

\[
 \mathcal Q_{\ell,\sigma}(H)=
 \sum_{v\in V_\sigma(H)}\sum_{G\in E(H),\,G\not\ni v}
 (a_G(v))_2(d_H(v)-2)_{\ell-2},\qquad2\le\ell\le6.   \tag{4.1}
\]

This is exactly the upper bound, apart from `binom(ell,2)`, for the
Bonferroni collision defect in the union-exposure hierarchy.

### Proposition 4.1 (positive carrier expansion)

`mathcal Q_(ell,sigma)` is the number of tuples

\[
                  (v,G,F_1,\ldots,F_\ell)             \tag{4.2}
\]

such that

1. `G,F_1,...,F_ell` are surviving configurations;
2. `G notni v`;
3. `F_1,...,F_ell` are ordered and distinct, and all contain `v`; and
4. both `F_1` and `F_2` meet `G`.

#### Proof

Choose the ordered pair `(F_1,F_2)` in `(a_G(v))_2`.  The remaining
falling factorial chooses `ell-2` ordered configurations through `v`
which are distinct from that pair.  Since `G notni v`, it is automatically
distinct from every `F_i`.  \(\square\)

The expansion uses at most `ell+1<=7` configurations.

Define also the positive linearized count

\[
 \begin{aligned}
 \mathcal L_{\ell,\sigma}(H)
 &=\sum_v d_H(v)(d_H(v))_\ell\\
 &\quad+\ell\sum_v(d_H(v)-1)_{\ell-1}
              \sum_{G\not\ni v}a_G(v).
 \end{aligned}                                       \tag{4.3}
\]

This is the same `L_(ell,sigma)` as the exact conflict-row compression,
written without division by `d_H(v)`.

### Theorem 4.2 (aggregate product-to-slice transfer)

For every fixed `2<=ell<=6`,

\[
 \mathbb E_{\rm sl}\mathcal Q_{\ell,\sigma}
 =\left(1+O_\ell\left({r^2\over xN_*}\right)\right)
   \mathbb E_{\rm prod}\mathcal Q_{\ell,\sigma},     \tag{4.4}
\]

and the identical statement holds for `mathcal L_(ell,sigma)`.  Hence

\[
 {\mathbb E_{\rm sl}\mathcal Q_{\ell,\sigma}
       \over\mathbb E_{\rm sl}\mathcal L_{\ell,\sigma}}
 =\left(1+O(e^{-\Omega_\ell(r)})\right)
 {\mathbb E_{\rm prod}\mathcal Q_{\ell,\sigma}
       \over\mathbb E_{\rm prod}\mathcal L_{\ell,\sigma}}. \tag{4.5}
\]

#### Proof

Use Proposition 4.1.  Each positive summand asks that the union of at most
seven configurations survive and therefore queries `O_ell(r)` targets per
shore.  Without conditioning any root, its slice probability is
`(m_sigma)_s/(N_sigma)_s`; comparison with `p_sigma^s` gives the same
uniform relative error as (3.4).  Sum the positive terms.  Both terms of
(4.3) likewise have positive carrier expansions using at most `ell+1`
configurations.  Equation (4.5) follows because `N_*` is exponential.
\(\square\)

This theorem is stronger for Gate A than a pointwise row comparison:
the microbite proof only consumes `mathcal Q_(ell,sigma)`.

## 5. The product collision theorem at order two

The preceding row-energy theorem closes the core three-carrier flower.

### Theorem 5.1 (order-two aggregate collision)

For `alpha<1/6`,

\[
 \boxed{
 {\mathbb E_{\rm prod}\mathcal Q_{2,\sigma}
       \over\mathbb E_{\rm prod}\mathcal L_{2,\sigma}}
 =O\left({1\over rx^5}\right)=o(1).}                \tag{5.1}
\]

The identical estimate holds on every exact slice, up to a factor
`1+e^{-Omega(r)}`.

#### Proof

For fixed `G,v`, conditioned on retaining `G union {v}`, both
`A_(G,v)` and the residual degree `d_R(v)` are increasing functions of the
remaining independent target indicators.  Harris's inequality and
monotonicity under fixing the targets of `G` give

\[
 \begin{aligned}
 \mathbb E[(d_R(v)-1)A_{G,v}\mid G,v]
 &\ge(\mathbb E[d_R(v)\mid G,v]-1)
                         \mathbb E[A_{G,v}\mid G,v]\\
 &\ge(\mu_\sigma-1)\mathbb E[A_{G,v}\mid G,v].       \tag{5.2}
 \end{aligned}
\]

The root event `G union {v}` has the same probability `q_0p_sigma` for
every external pair `(G,v)`.  Sum (2.12)--(2.14) and (5.2) over all such
pairs.  The external-row term of `mathcal L_(2,sigma)` is at least
`2(mu_sigma-1) sum_(G,v) E A_(G,v)`, whereas
`mathcal Q_(2,sigma)` is `sum_(G,v) E(A_(G,v))_2`.  Since `mu_sigma` is
exponentially large, (2.14) proves (5.1).  The slice assertion is Theorem
4.2.  \(\square\)

## 6. The exact remaining higher-order product kernel

The desired remaining product conclusion is

\[
 \boxed{
 \mathbb E_{\rm prod}\mathcal Q_{\ell,\sigma}
 \le\eta_r\,
       \mathbb E_{\rm prod}\mathcal L_{\ell,\sigma},
 \qquad 3\le\ell\le6,\qquad\eta_r=o(1).}             \tag{6.1}
\]

By Theorem 4.2, any bound (6.1) automatically holds on every exact slice
with the same polynomial rate.

The controlled core is the positive three-carrier flower

\[
 \sum_{\substack{v,\,G\not\ni v,\,F_1\ne F_2\ni v\\
                  F_1\cap G\ne\varnothing,\ F_2\cap G\ne\varnothing}}
 \Pr(G,F_1,F_2\text{ all survive}).                  \tag{6.2}
\]

For reference, its exact product split is

\[
 \Pr(F_1,F_2\mid G,v)=
 \Pr(F_1\mid G,v)\Pr(F_2\mid G,v)
 \prod_{u\in(F_1\cap F_2)-(G\cup\{v\})}
                         p_{\operatorname{sh}(u)}^{-1}.       \tag{6.3}
\]

The term `1` in the expansion of the last product is controlled by
(2.16)--(2.17), and its nonconstant part is controlled by the rooted
kernel (2.19)--(2.20).  This is exactly Theorem 2.2 and Theorem 5.1.

For `ell>=3`, the positive expansion in Proposition 4.1 attaches
`ell-2<=4` further, unrestricted members of the star of `v` to this
already controlled flower.  The smallest remaining independent theorem
is therefore a **decorated-flower attachment bound**: under the
`(G,F_1,F_2,v)` size-biased law of (6.2), prove that the factorial moments
of the remaining star through order four are at most a fixed polynomial
factor times `mu_sigma^(ell-2)`, with a total factor small enough to retain
the `1/(rx^5)` saving.

The ordinary rooted high-moment theorem controls these attachments before
conditioning on the external carrier `G`.  Applying it after that
conditioning requires weighted rooted rows of the form

\[
 {1\over d_\sigma}\sum_{H\ni v}
 \prod_{u\in H\cap G}p_{\operatorname{sh}(u)}^{-c}
 \bigl(x^{-c|(H\cap F)-\{v\}|}-1\bigr),              \tag{6.4}
\]

averaged under the flower measure.  Theorem 2.1 controls the first factor
in aggregate and the rooted kernels control the second separately; their
flower-weighted product is the exact unresolved attachment statistic.

Estimate (6.1) would close the untrimmed hierarchy directly.  The next
section tests whether the actual purge-then-cap architecture can bypass it
using only the already proved order-two scalar.

## 7. Capped-hierarchy shortcut: a one-round `mathcal Q_2` reduction

For one round, purge first, use the cap deterministically, and charge the
purged high-degree incidence by the already proved sixth-moment
bad-incidence theorem.  Proposition 7.3 below records why this argument by
itself does not propagate through the full schedule.

Let `H` be a residual in which shore `sigma` has average degree `bar d`
and maximum degree at most `K bar d`.  Let

\[
 c_\ell(a)=\sum_{j=\ell}^6{6\choose j}(-a)^{6-j}S(j,\ell),           \tag{7.1}
\]

where `S(j,ell)` is a Stirling number of the second kind.  These are the
coefficients in

\[
                         \sum_v(d(v)-a)^6
                    =\sum_{\ell=0}^6c_\ell(a)F_\ell. \tag{7.2}
\]

### Theorem 7.1 (deterministic capped collision compression)

For every `2<=ell<=6`,

\[
 \boxed{
 \mathcal Q_{\ell,\sigma}(H)
 \le(K\bar d)^{\ell-2}\mathcal Q_{2,\sigma}(H).}      \tag{7.3}
\]

Consequently the absolute collision contribution to the first-order
evolution of the centered sixth mass is at most

\[
 \boxed{
 \sum_{\ell=2}^6|c_\ell(\bar d)|{\ell\choose2}
          \mathcal Q_{\ell,\sigma}(H)
 \le C_K\bar d^4\mathcal Q_{2,\sigma}(H).}           \tag{7.4}
\]

#### Proof

Termwise in (4.1),

\[
 (d(v)-2)_{\ell-2}\le d(v)^{\ell-2}\le(K\bar d)^{\ell-2},
\]

which proves (7.3).  Since the finite coefficients (7.1) obey
`|c_ell(bar d)|<=C bar d^(6-ell)` for `bar d>=1`, every summand on the
left of (7.4) is at most a constant depending on `K` times
`bar d^4 Q_(2,sigma)`.  There are five summands.  \(\square\)

This argument deliberately makes no assertion such as
`L_ell>=bar d^(ell-2)L_2`; no such lower bound is needed.

### Corollary 7.2 (product/slice error at the nibble scale)

Let `H^*` be a provisional product residual and purge its high-degree
targets to obtain `H^circ`, with maximum degree at most `K bar d_sigma^circ`.
Suppose the purge incidence is `o(Z)` so that the deterministic trimming
recurrence keeps `bar d_sigma^circ` comparable to the provisional average.
Then

\[
                         \mathcal Q_{2,\sigma}(H^\circ)
                    \le\mathcal Q_{2,\sigma}(H^*).    \tag{7.5}
\]

Moreover Theorem 2.2, summed over the original choice of `G`, gives

\[
 \mathbb E\mathcal Q_{2,\sigma}(H^*)
 =O\left((\mathbb E Z^*)p_\sigma\mu_\sigma^2
                    r x^{-5}\right).                 \tag{7.6}
\]

Write the deterministic nominal marking rate as

\[
                    \pi_0={\gamma\over r\mu_M}.       \tag{7.7}
\]

On the scale-concentration event the actual rate
`pi=gamma/(r bar d_M)` is comparable to `pi_0`.  Equations
(7.4)--(7.7) give the following expectation bound at the nominal product
scales:

\[
 {\pi_0 C_K\mu_\sigma^4
       \mathbb E\mathcal Q_{2,\sigma}(H^*)
       \over (N_\sigma p_\sigma)\mu_\sigma^6}
 =O_K\left({p_\sigma\over r x^5}\right).             \tag{7.8}
\]

For the actual paired densities
`p_L=x` and `p_M=(rx+2)/(r+2)=x(1+O(1/(rx)))`, this is

\[
                              O_K((rx^4)^{-1})=o(1)   \tag{7.9}
\]

for one bite through the present stopping range.  Theorem 4.2 gives the
identical expectation estimate on exact slices.  On an event where the
realized edge count, shore size, and post-purge average are within fixed
factors of their nominal values, Markov's inequality therefore gives, for
every `t>0`,

\[
 \Pr\left(
 {\pi C_K(\bar d_\sigma^\circ)^4
       \mathcal Q_{2,\sigma}(H^\circ)
       \over n_\sigma^\circ(\bar d_\sigma^\circ)^6}>t
 \right)
 \le O_K\left({p_\sigma\over r x^5t}\right)
       +\Pr(\text{scale concentration fails}).       \tag{7.10}
\]

Deleting the high-degree targets only decreases `mathcal Q_2`; their lost
incidence and vertices are separately charged by the independent
sixth-moment purge theorem.

#### Proof

Induced deletion can only remove rows and decrease every surviving
`a_G(v)`, proving (7.5).  A fixed original `G` survives with probability
`q_0`; an external shore-`sigma` root survives with the additional factor
`p_sigma`.  Multiply (2.12) by these root probabilities and sum over all
original `G` to get (7.6).  Finally insert (7.6) into (7.4), multiply by
the nominal marking rate (7.7), and use
`(N_sigma p_sigma)mu_sigma=2r E Z^*` and
`mu_sigma/mu_M=Theta(1)` at the paired densities.  This proves
(7.8)--(7.9).
On the scale-concentration event, (7.5) and comparability of the purged
average convert the random normalized quantity to the nominal denominator;
Markov then proves (7.10).  \(\square\)

### Proposition 7.3 (the one-round bound is not summable)

Suppose a geometric descent schedule has

\[
 x_{j+1}=x_j(1-\theta/r+O(r^{-2})),\qquad
 x_J\asymp r^{-\alpha},                              \tag{7.11}
\]

for a fixed `theta>0`.  Then

\[
 \boxed{
 \sum_{j<J}{1\over r x_j^4}=\Theta(x_J^{-4})
 =\Theta(r^{4\alpha}),}                              \tag{7.12}
\]

so (7.9), treated as an additive error at every bite, is not summable and
does not by itself propagate the capped sixth-moment hierarchy.

#### Proof

Equation (7.11) gives
`x_j^{-4}=x_0^{-4}exp((4theta+o(1))j/r)`.  Summing the geometric series and
using `J=Theta(r log(1/x_J))` gives

\[
 {1\over r}\sum_{j<J}x_j^{-4}
 \asymp\int_{x_J}^1x^{-4}\,d\log(1/x)
 ={x_J^{-4}-1\over4}.                                \tag{7.13}
\]

This proves (7.12).  \(\square\)

Thus the capped shortcut is a valid **one-round** compression, but it does
not yet close orders three through six over the full trajectory.  One of
the following additional statements is still required:

1. a contractive normalized-moment recurrence which absorbs the forcing
   `O((rx^4)^-1)` at each round;
2. a genuinely summable forcing estimate, comparable to the existing
   `O(r^-2x^-9)` bad-incidence ledger; or
3. a direct stopped snapshot comparison, in which no additive propagation
   of (7.9) is performed.

No such contraction is proved here.  Thus at the level of the absolute
factorial hierarchy, the interface still consists of the order-two scalar
together with either a contraction or decorated higher-order observables.
The next section obtains a smaller interface by retaining the signs with
which those orders enter the centered sixth moment.

## 8. The signed centered defect and a summable reference-law bound

The absolute-coefficient estimate (7.4) discards a cancellation which is
present after the five factorial orders are recombined.  The cancellation
does not, however, reduce the answer to the first second difference alone.
This section gives the exact identity and retains the shifted remainder.

For a real center `z`, put

\[
 f_z(d)=(d-z)^6,qquad
 \nabla f_z(d)=f_z(d)-f_z(d-1).                     \tag{8.1}
\]

For integers `0<=a<=d`, define the centered row defect

\[
 \mathfrak d_z(d,a)
 =a\nabla f_z(d)-[f_z(d)-f_z(d-a)].                 \tag{8.2}
\]

### Proposition 8.1 (exact shifted second-difference identity)

If `c_ell(z)` are the coefficients in (7.1), then (8.3)--(8.4) hold for
`d>=1`; for `d=a=0` all defects are zero and that case is understood
separately:

\[
\begin{aligned}
 \mathfrak d_z(d,a)
 &=\sum_{\ell=1}^6c_\ell(z)
 \left\{\ell a(d-1)_{\ell-1}
       -[(d)_\ell-(d-a)_\ell]\right\}             \tag{8.3}\\
 &=\sum_{h=0}^{a-2}(a-1-h)\nabla^2f_z(d-h).      \tag{8.4}
\end{aligned}
\]

The sum in (8.4) is empty for `a<=1`.  Writing `t=d-z`,

\[
 \nabla^2f_z(d)
 =30t^4-120t^3+210t^2-180t+62.                    \tag{8.5}
\]

Consequently

\[
 \boxed{
 0\le\mathfrak d_z(d,a)
 \le C(a)_2\{1+|d-z|^4+a^4\}.}                    \tag{8.6}
\]

In particular,

\[
 { (a)_2\over2}\nabla^2f_z(d)
 =(a)_2[15t^4-60t^3+105t^2-90t+31]                \tag{8.7}
\]

is only the `h=0` term with the total quadratic multiplicity substituted.
It equals the full defect for `a<=2`, but not in general.  For example,
`d=z=10` and `a=3` give respectively `726` and `186`.

#### Proof

The elementary identity

\[
 (d)_\ell-(d-1)_\ell=\ell(d-1)_{\ell-1}           \tag{8.8}
\]

and `f_z(d)=sum_ell c_ell(z)(d)_ell` prove (8.3).
Also

\[
\begin{aligned}
 \mathfrak d_z(d,a)
 &=a\nabla f_z(d)-\sum_{j=0}^{a-1}\nabla f_z(d-j)\\
 &=\sum_{h=0}^{a-2}(a-1-h)\nabla^2f_z(d-h),
\end{aligned}                                      \tag{8.9}
\]

which proves (8.4).  Direct expansion gives (8.5).  Since `f_z` is
convex, every second difference in (8.4) is nonnegative.  Moreover
`|\nabla^2f_z(u)|<=C(1+|u-z|^4)` and
`|d-h-z|^4<=8(|d-z|^4+h^4)`.  Finally

\[
 \sum_{h=0}^{a-2}(a-1-h)={(a)_2\over2},\qquad
 \sum_{h=0}^{a-2}(a-1-h)h^4=O((a)_2a^4),           \tag{8.10}
\]

which proves (8.6).  Equation (8.7) is (8.5) divided by two.
\(\square\)

For a residual `H`, define the nonnegative aggregate signed defect

\[
 \mathfrak D_{z,\sigma}(H)
 =\sum_{v\in V_\sigma(H)}\sum_{G\in E(H):G\not\ni v}
        \mathfrak d_z(d_H(v),a_G(v)).               \tag{8.11}
\]

By (8.3), this is exactly the recombined collision error in the
first-order evolution of the sixth centered mass.  It is not the
absolute-coefficient majorant (7.4).

### Lemma 8.2 (centered flower under product retention)

Assume `alpha<1/18`.  Fix an original configuration `G`.  For an external
shore-`sigma` target `v`, condition on retaining `G union {v}`, and write
`X_v` for its residual degree and `A_(G,v)` for (1.4).  Then, uniformly in
`G`,

\[
 \boxed{
 \sum_{v\in V_\sigma-G}
 \mathbb E\left[(A_{G,v})_2
       \{1+|X_v-\mu_\sigma|^4+A_{G,v}^4\}\mid G,v\right]
 =O(\mu_\sigma^6 r^{-1}x^{-33}).}                  \tag{8.12}
\]

#### Proof

For clarity, the rooted kernel used below is

\[
 Q_c=\max_{v,F\ni v}{1\over d_{\operatorname{sh}(v)}}
 \sum_{\substack{H\ni v,\ H\ne F\\
                  |(F\cap H)-\{v\}|>0}}
 x^{-c|(F\cap H)-\{v\}|}.                         \tag{8.12a}
\]

The rooted boundary-polymer estimate proved in the independent
high-moment theorem gives, for every fixed `c` with `c alpha<1/2`,

\[
 Q_c=O_c(r^{-1}x^{-3c}+r^{-2}x^{-4c}).             \tag{8.12b}
\]
Indeed its nonconstant overlap kernel has this bound, while the
unweighted proportion of configurations with a non-root intersection is
`O(1/r)`; adding the two bounds gives (8.12b).

Put

\[
 \theta={32\over r},\qquad
 \lambda=\theta+Q_3=O(r^{-1}x^{-9}).               \tag{8.13}
\]

Here `theta` follows from (2.11), and the rooted-kernel bound (1.6) in
the independent-high-moment theorem gives the estimate for `Q_3`; its
second term is smaller because `rx^3\to\infty` in the stated range.

We first treat the term with four distinct centered star configurations,
all distinct from the ordered pair counted by `(A_(G,v))_2`.  Denote the
six star configurations by `F_1,...,F_6`, where `F_1,F_2` meet `G`, and
put

\[
 s_i=\prod_{u\in F_i\cap G}p_{\operatorname{sh}(u)}^{-1}.
                                                               \tag{8.14}
\]

Let `R` be the set of indices for which `F_i cap G` is nonempty, and put
`h=|R|`; thus `2<=h<=6`.  Conditional on `G union {v}`, expansion of the
four centered indicators gives the absolute bound

\[
 C\,w_\sigma^6\prod_{i\in R}s_i\,
 x^{-\sum_{i<j}|(F_i\cap F_j)-(G\cup\{v\})|},
 \qquad w_\sigma={\mu_\sigma\over d_\sigma}.        \tag{8.15}
\]

Indeed, every omitted centered indicator supplies one factor `w_sigma`,
and adding its powered intersections to an upper bound only enlarges it.

Form the dependency graph on the six star configurations, joining two
when they share a target outside `G union {v}`.  A component consisting of
one centered configuration and containing no member of `R` contributes
zero exactly.  Hence every component disjoint from `R` has at least two
vertices, and there are at most two such components; call their number
`c`.

In each dependency component choose a maximum-weight spanning tree.  A
component has at most six vertices, so its tree has at least one third of
the total overlap weight.  Thus (8.15) is bounded by the corresponding
tree product with every tree-edge activity raised to the third power.
There are only constantly many labelled forests.

Use

\[
 \prod_{i\in R}s_i\le {1\over h}\sum_{j\in R}s_j^h. \tag{8.16}
\]

After choosing the distinguished `j`, its sum is
`d_sigma K_h(G,v)`.  Root a component disjoint from `R` freely.  Root
every other component not containing `j` at a member of `R`, at cost at
most `theta d_sigma`; sum every remaining vertex from a tree leaf, at
cost at most `Q_3d_sigma`.  There are exactly `1+c` free roots, so at
least

\[
                         6-(1+c)\ge3                \tag{8.17}
\]

candidate/tree costs.  Since `lambda=o(1)`, summing all distinct tuples
and then all external `v` gives

\[
 C\mu_\sigma^6\lambda^3
       \sum_{h=2}^6\sum_vK_h(G,v)
 =O(\mu_\sigma^6 r^{-1}x^{-33}),                   \tag{8.18}
\]

by Theorem 2.1.  This proves the centered fourth-power estimate for
distinct labels.

Repeated centered labels do not change the bound.  For a Bernoulli
indicator `I` of mean `w`, every fixed power of `I-w` is affine in `I-w`
plus a constant of modulus `O(w)`.  Merge equal labels, including labels
which equal `F_1` or `F_2`, and apply the same forest sum.  If `m<=5`
distinct star carriers remain, every carrier still supplies one factor
`w_sigma`; allowing all centered-only components to be rooted freely and
using `lambda<=1` bounds the sum by

\[
 O_m\left(\mu_\sigma^m
       \sum_{h=2}^m\sum_vK_h(G,v)\right)
 =O_m(\mu_\sigma^m r^2x^{-m}).                     \tag{8.18a}
\]

From (1.1)--(1.3) and Stirling's formula,

\[
 \mu_\sigma\ge
 \exp((2-4\alpha+o(1))r\log r),                    \tag{8.19}
\]

so the sum of (8.18a) over `2<=m<=5` is exponentially smaller than
(8.18).

It remains to bound the `A_(G,v)^4` term.  For every integer `A>=0`,

\[
 (A)_2A^4
 =16(A)_2+65(A)_3+55(A)_4+14(A)_5+(A)_6.           \tag{8.20}
\]

For `2<=j<=6`, the same AM--GM and forest summation, now with every
carrier constrained to meet `G`, gives

\[
 \sum_v\mathbb E(A_{G,v})_j
 \le C_j\mu_\sigma^j\lambda^{j-1}\sum_vK_j(G,v). \tag{8.21}
\]

The `j=6` term is
`O(mu_sigma^6 r^{-3}x^{-51})`, which is bounded by (8.18) because
`r^{-2}x^{-18}=o(1)` for `alpha<1/18`; the lower orders are absorbed by
(8.19).  The remaining `(A)_2` term is Theorem 2.2 and is absorbed in the
same way.  This proves (8.12).  \(\square\)

### Theorem 8.3 (summable product and exact-slice collision forcing)

Let `H^*` be the product residual.  For `alpha<1/18`,

\[
 \boxed{
 \mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
 =O\left((\mathbb EZ^*)p_\sigma\mu_\sigma^6
                         r^{-1}x^{-33}\right).}     \tag{8.22}
\]

The same estimate holds for the uniform exact two-shore slice, with its
exact conditional mean in place of `mu_sigma` and a `1+e^{-Omega(r)}`
change in the implied reference scales.

At the paired densities and nominal bite rate (7.7), (8.22) implies

\[
 {\pi_0\mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
       \over(N_\sigma p_\sigma)\mu_\sigma^6}
 =O(r^{-3}x^{-32}).                                 \tag{8.23}
\]

Along a geometric schedule (7.11), stopped at `x_J>=r^{-alpha}`,

\[
 \boxed{
 \sum_{j<J}O(r^{-3}x_j^{-32})
 =O(r^{-2}x_J^{-32})=o(1)\qquad(\alpha<1/18).}      \tag{8.24}
\]

#### Proof

Apply (8.6) with `d=X_v`, `a=A_(G,v)`, sum Lemma 8.2 over the original
choice of `G`, and multiply by the common root probability `q_0p_sigma`.
Since the number of original configurations times `q_0` is
`E Z^*`, this proves (8.22).

For exact slices, expand the four centered star factors as in Lemma 8.2
and apply the fixed-tuple comparison from the fixed-slice theorem.  A
queried union uses at most seven configurations.  The comparison error is
`e^{-Omega(r)}` times the same positive carrier envelope.  If the four
centered configurations are allowed to be singleton components, the
forest proof above gives the crude envelope
`O(mu_sigma^6 r x^{-15})`; its exponentially small multiplier is absorbed
by (8.22).  The positive `A^4` terms transfer directly.  This proves the
slice assertion.  More explicitly, the slice-centered factor is
`I_F-tilde w_sigma` rather than `I_F-w_sigma`.  Expanding each difference
and using `tilde w_sigma/w_sigma=1+e^{-Omega(r)}` produces only the same
positive carrier envelopes, each with an additional exponentially small
coefficient.  Thus changing the center from the product marginal to the
exact-slice marginal creates no unaccounted signed term.

Finally use `(N_sigma p_sigma)mu_sigma=2r E Z^*`,
`mu_sigma/mu_M=Theta(1)`, and `p_sigma=Theta(x)` to obtain (8.23).  The
geometric sum in (8.24) is

\[
 O\left(r^{-3}\,r\,x_J^{-32}\right)
 =O(r^{-2}x_J^{-32}),                               \tag{8.25}
\]

which tends to zero because `32/18<2`.  \(\square\)

The center in the actual purge statistic is the realized shore average,
not `mu_sigma`.  The next deterministic comparison and probability ledger
close this last reference-law mismatch.

### Proposition 8.4 (deterministic center shift)

For every residual `H`, shore `sigma`, and real centers `z,z'`,

\[
 \boxed{
 \mathfrak D_{z',\sigma}(H)
 \le C\mathfrak D_{z,\sigma}(H)
       +C|z'-z|^4\mathcal Q_{2,\sigma}(H).}         \tag{8.26}
\]

#### Proof

Let

\[
 P(t)=t^6-2(t-1)^6+(t-2)^6.
\]

If `U,V` are independent uniform random variables on `[0,1]`, twice
integrating the second derivative gives

\[
 P(t)=30\mathbb E(t-U-V)^4.                         \tag{8.27}
\]

Since `Var(U+V)=1/6`, Cauchy's inequality gives
`P(t)>=30(1/6)^2=5/6`.  Jensen also gives
`P(t)>=30(t-1)^4`.  Conversely,
`P(t)<=30(|t|+2)^4`.  Hence there are absolute positive constants
`c,C` such that

\[
                 c(1+|t|^4)\le P(t)\le C(1+|t|^4) \tag{8.28}
\]

for all real `t`.  Therefore, with `delta=z'-z`,

\[
 P(t-\delta)\le C\{P(t)+|\delta|^4\}.              \tag{8.29}
\]

Apply (8.29) term by term to the shifted representation (8.4).  The
weights in that representation sum to `(a)_2/2`, and summing `(a_G(v))_2`
over the external rows is exactly `mathcal Q_(2,sigma)`.  This proves
(8.26).  \(\square\)

### Corollary 8.5 (the realized-center reference schedule is summable)

At a product or uniform exact-slice checkpoint, write

\[
 \bar d_\sigma={2rZ\over n_\sigma},\qquad
 \mathcal E_{\eta,\sigma}
 =\left\{|\bar d_\sigma/\mu_\sigma-1|\le\eta,
          \ |n_\sigma/(N_\sigma p_\sigma)-1|\le\eta\right\},
 \qquad \eta=r^{-1/8}.                              \tag{8.30}
\]

In the exact-slice model the second condition is automatic.
Here and below in this corollary, `mu_sigma` denotes the conditional mean
in the model under discussion; on an exact slice it is the
`widetilde mu_sigma` from the fixed-slice theorem.

For a geometric schedule with `O(r log r)` checkpoints and
`x_J>=r^{-alpha}`, `alpha<1/18`,

\[
 \Pr\left(\bigcup_{j,\sigma}\mathcal E_{\eta,\sigma}^c\right)
 =O\left(r^{-2+6/8+3\alpha}\log r\right)+e^{-\Omega(r)}
 =o(1).                                             \tag{8.31}
\]

The expected normalized center-shift contribution restricted to the
intersection of these good events satisfies

\[
 \boxed{
 \sum_{j<J}
 {\pi_{0,j}\eta^4\mu_{\sigma,j}^4
       \mathbb E\mathcal Q_{2,\sigma}(H_j^*)
  \over (N_\sigma p_{\sigma,j})\mu_{\sigma,j}^6}
 =O(\eta^4x_J^{-4})
 =O(r^{-1/2+4\alpha})=o(1).}                       \tag{8.32}
\]

Consequently (8.24), (8.26), and (8.32) give a summable bound for the
actual realized-center scalar
`mathfrak D_(bar d_sigma,sigma)` under every product or uniform exact-slice
reference checkpoint.  Here and below the reference checkpoint is the
provisional pre-purge residual \(H^*\).  No monotonicity of the centered
defect under the induced deletion \(H^*\to H^\circ\) is asserted: both its
degree argument and its moving center change under that deletion.

#### Proof

The global surviving-edge sixth moment, in both the product and exact-slice
models, is

\[
 {\mathbb E|Z-\mathbb EZ|^6\over(\mathbb EZ)^6}
 =O((rx)^{-3}).                                     \tag{8.33}
\]

The product shore size has an exponentially small `eta`-relative-deviation
tail (its mean is exponential in `r`), and the exact-slice shore size is
deterministic.  If both
`|Z/(mathbb E Z)-1|<=eta/4` and, in the product model,
`|n_sigma/(N_sigma p_sigma)-1|<=eta/4`, then (8.30) holds for all large
`r`, because
`mu_sigma=2r(mathbb E Z)/(N_sigma p_sigma)`.  Markov's inequality in
(8.33)
therefore gives a one-checkpoint failure probability

\[
 O(\eta^{-6}r^{-3}x^{-3})+e^{-\Omega(r)}.           \tag{8.34}
\]

Multiply by `O(r log r)`, use `eta^{-6}=r^{6/8}` and
`x^{-3}<=r^{3alpha}`, and obtain (8.31).

On `mathcal E_(eta,sigma)`, Proposition 8.4 with
`z=mu_sigma`, `z'=bar d_sigma` adds at most
`C eta^4mu_sigma^4mathcal Q_(2,sigma)`.  Equations (7.6)--(7.8) show that
its one-checkpoint normalized expectation is

\[
                         O\left({\eta^4\over rx^4}\right). \tag{8.35}
\]

The same positive-carrier estimate holds on exact slices by Theorem 4.2.
Finally the geometric calculation (7.13) gives
`sum_(j<J)(rx_j^4)^(-1)=O(x_J^(-4))`, proving (8.32).
On (8.30), nominal and realized shore sizes, degrees, sixth-power
normalizations, and the actual rate `gamma/(r bar d_M)` differ from their
nominal counterparts by bounded factors.  Thus the same conclusion holds
with the realized normalization and marking rate.  Since all defects are
nonnegative, Markov's inequality converts the accumulated `o(1)`
expectation into an `o(1)`-in-probability forcing.  \(\square\)

Theorem 8.3 and Corollary 8.5 resolve the collision nonsummability in
Proposition 7.3 for product snapshots and exact uniform slices, including
the realized moving center.  They do **not** transfer this reference-law
bound to the stopped adaptive residual, nor from its provisional pre-purge
snapshot \(H^*\) to the post-purge residual \(H^\circ\).  The remaining
collision part of Gate A is therefore a stopped-law comparison for
`mathfrak D_(bar d_sigma,sigma)` together with a deletion-stability or
purge-charge estimate for \(H^*\to H^\circ\), rather than five absolute
factorial comparisons.  The separate stopped high-degree-incidence
comparison required for defining and charging the purge also remains.
