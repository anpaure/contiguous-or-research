# Fixed-slice high moments and the exact stopped-Palm form of Gate A

**Date:** 2026-08-22  
**Status:** proved de-Poissonization and proved filtration reduction; Gate A
is not claimed closed

The independent-residual theorem leaves two superficially similar
conditioning issues:

1. the residual shores have prescribed cardinalities; and
2. their shapes were produced by the preceding matching history.

This note separates them rigorously.  Exact cardinality conditioning is
harmless: the fixed even moments and the sixth-moment bad-incidence bound
survive on every uniform two-shore slice, with an exponentially small
finite-population error.  The actual matching history, however, is very far
from uniform on a full slice.  An exact Palm identity shows that a full
quenched theorem is unnecessary: Gate A only needs a stopped, one-statistic
comparison for the aggregate high-degree incidence.  A support count proves
that this comparison cannot be obtained from total variation or a bounded
full-state likelihood ratio.

Thus the remaining Gate A statement is narrower than “transfer product
measure to every history”:

> compare one stopped bad-incidence event under the actual residual law and
> the uniform fixed-slice law, without comparing the full residual states.

## 1. A finite-population inclusion lemma

Let `Omega` have size `N`, and let `R` be a uniformly random `m`-subset of
`Omega`.  Put `p=m/N`.  For `0<=a<=m`, write

\[
 h_{N,m}(a)=\Pr(A\subseteq R)={(m)_a\over(N)_a}
 \qquad(|A|=a).                                      \tag{1.1}
\]

### Lemma 1.1 (uniform inclusion comparison)

If `1<=q<=m/2`, then, uniformly for `0<=a<=q`,

\[
 \left|\log {h_{N,m}(a)\over p^a}\right|
       \le {2q^2\over m}.                            \tag{1.2}
\]

The left side is zero when `m=N`.  Consequently, if

\[
                         \epsilon={4q^2\over m}\le1, \tag{1.3}
\]

then

\[
                    h_{N,m}(a)=p^a(1+O(\epsilon))     \tag{1.4}
\]

with an absolute implied constant.

#### Proof

For `m<N`,

\[
 \log {h_{N,m}(a)\over p^a}
 =\sum_{i=0}^{a-1}\left\{
       \log(1-i/m)-\log(1-i/N)\right\}.              \tag{1.5}
\]

Both logarithms have arguments at least `1/2`.  The mean-value theorem and
`|d\log(1-z)/dz|<=2` on `[0,1/2]` give an absolute value at most

\[
 2\sum_{i=0}^{a-1}{i\over m}
 \le {a^2\over m}\le {q^2\over m}.                   \tag{1.6}
\]

The weaker constant in (1.2) leaves room for the endpoints.  Equation
(1.4) follows from `|e^u-1|<=2|u|` for `|u|<=1`.
\(\square\)

The same proof applies independently on two shores.  If their sizes are
`N_1,N_2`, their retained sizes are `m_1,m_2`, and

\[
 x=\min_\sigma {m_\sigma\over N_\sigma},\qquad
 N_*=\min_\sigma N_\sigma,                           \tag{1.7}
\]

then every query involving at most `q` coordinates on each shore has
relative inclusion error

\[
                  O\left({q^2\over xN_*}\right).      \tag{1.8}
\]

No factor `(1-x)^{-1}` occurs.  In particular, the statement remains
uniform as a shore density tends to one.

## 2. Centered tuple comparison

Let \(\mathcal F\) be a family of configurations.  Configuration \(F\) asks for
fixed sets \(A_{F,1},A_{F,2}\) on the two shores, with the cardinality on each
shore independent of `F`.  Let

\[
 I_F=\mathbf1_{\{A_{F,1}\cup A_{F,2}\subseteq R_1\cup R_2\}}. \tag{2.1}
\]

Write `P_prod` for independent Bernoulli retention with probabilities
`p_1,p_2`, and `P_sl` for independent uniform `m_sigma`-subsets on the two
shores.  Their common one-configuration means are denoted by `w` and
`tilde w`, respectively.  For distinct configurations put

\[
 t(F,G)=\sum_{\sigma=1}^2|A_{F,\sigma}\cap A_{G,\sigma}|. \tag{2.2}
\]

### Lemma 2.1 (fixed tuple)

Fix `j`.  Suppose the union of any `j` configurations queries at most `q`
coordinates on either shore and `q<=min(m_1,m_2)/2`.  Set

\[
                  \varepsilon_q=C_j{q^2\over xN_*}.    \tag{2.3}
\]

For pairwise distinct `F_1,...,F_j`,

\[
\begin{aligned}
 &\left|
 \mathbb E_{\rm sl}\prod_{i=1}^j(I_{F_i}-\widetilde w)
 -\mathbb E_{\rm prod}\prod_{i=1}^j(I_{F_i}-w)
 \right|                                                     \\
 &\hspace{35mm}\le
 \varepsilon_q w^j
 x^{-\sum_{a<b}t(F_a,F_b)}.                         \tag{2.4}
\end{aligned}
\]

Also `tilde w=w(1+O_j(q^2/(xN_*)))`.

#### Proof

For \(S\subseteq[j]\), let \(u_\sigma(S)\) be the number of distinct shore
\(\sigma\) coordinates in the union of the configurations indexed by \(S\).
Lemma 1.1 on both shores gives, uniformly in `S`,

\[
 \mathbb E_{\rm sl}\prod_{i\in S}I_{F_i}
 =\mathbb E_{\rm prod}\prod_{i\in S}I_{F_i}
  \left(1+O_j\left({q^2\over xN_*}\right)\right).     \tag{2.5}
\]

The assertion about the one-configuration mean is the case `|S|=1`.
More explicitly, write

\[
 P_S=\mathbb E_{\rm prod}\prod_{i\in S}I_{F_i},\qquad
 \widetilde P_S=\mathbb E_{\rm sl}\prod_{i\in S}I_{F_i}. \tag{2.5a}
\]

Equation (2.5) says
`|tilde P_S-P_S|<=C_j epsilon P_S`, while
`|tilde w-w|<=C_j epsilon w`, where
`epsilon=q^2/(xN_*)`.  Hence, for every `S`,

\[
 \left|(-\widetilde w)^{j-|S|}\widetilde P_S
       -(-w)^{j-|S|}P_S\right|
 \le C_j\epsilon w^{j-|S|}P_S.                       \tag{2.5b}
\]

This uses only the fixed-power inequality
`|a^ell-b^ell|<=ell |a-b|max(a,b)^(ell-1)`; all powers are at most `j`.
Summing (2.5b) is exactly the difference of the two centered products.
If `a_sigma` is the fixed number of queried coordinates of one
configuration on shore `sigma`, then

\[
 {\mathbb E_{\rm prod}\prod_{i\in S}I_{F_i}\over w^{|S|}}
 =\prod_\sigma p_\sigma^{-
       (|S|a_\sigma-u_\sigma(S))}.                   \tag{2.6}
\]

For each coordinate of multiplicity `c`, one has
`c-1<=binom(c,2)`.  Hence

\[
 |S|a_1+|S|a_2-u_1(S)-u_2(S)
 \le\sum_{\{a,b\}\subseteq S}t(F_a,F_b).             \tag{2.7}
\]

Since both retention probabilities are at least `x`, every term in the
centered expansion is bounded by the right side of (2.4), up to a constant
depending only on `j`.  Summing the `2^j` terms proves the lemma.
\(\square\)

The error in (2.4) is the important point.  It is *relative to the rare
joint survival scale* `w^j`; it is not an additive total-variation error.

## 3. Fixed-slice high moments

Fix a target \(v\), condition on retaining it, and let \(\mathcal F_v\) be its
\(D\) incident punctured configurations.  In the root-conditioned shore,
remove \(v\) from the population and from every query.  This changes a shore
size and retained size by one and has no asymptotic effect.  Put

\[
 X_v=\sum_{F\in\mathcal F_v}I_F,\qquad
 \mu=Dw,\qquad \widetilde\mu=D\widetilde w.           \tag{3.1}
\]

For fixed `c>=1`, use the rooted kernels

\[
 R_c=\max_F{1\over D}\sum_{G\ne F}
              (x^{-ct(F,G)}-1).                       \tag{3.2}
\]

The already proved punctured boundary-polymer calculation gives, whenever
`c alpha<1/2` and `x>=r^{-alpha}`,

\[
 R_c=O_c\left({1\over rx^{3c}}+{1\over r^2x^{4c}}\right). \tag{3.3}
\]

### Theorem 3.1 (de-Poissonized rooted moment)

Fix `s>=1` and

\[
                         0<\alpha<{1\over6s}.          \tag{3.4}
\]

Let both root-conditioned retained shore sizes be at least
`r^{-alpha}` times their populations.  Then, uniformly over those exact
sizes,

\[
 \boxed{
 {\mathbb E_{\rm sl}(X_v-\widetilde\mu)^{2s}
       \over\widetilde\mu^{2s}}
 =O_s((rx^3)^{-s})+O_s\left({r^2\over xN_*}\right).
 }                                                     \tag{3.5}
\]

For the punctured target shores, \(N_*=\exp(\Omega(r))\); hence the second term
is exponentially small.  In particular, (3.5) has exactly the same
polynomial scale as the independent-residual theorem.

#### Proof

Expand the `2s`th centered power into ordered configuration tuples.  First
consider tuples with all configurations distinct.  Lemma 2.1 has
`q<=8sr`, so its error parameter is

\[
                         \varepsilon=O_s(r^2/(xN_*)).  \tag{3.6}
\]

We sum its overlap weight.  On inserting `F_i` after fixed
`F_1,...,F_(i-1)`, the arithmetic-geometric mean inequality gives

\[
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le {1\over i-1}\sum_{a<i}
           x^{-(i-1)t(F_a,F_i)}.                     \tag{3.7}
\]

Thus (3.2) implies

\[
 \sum_{F_1,\ldots,F_j\ {\rm distinct}}
 x^{-\sum_{a<b}t(F_a,F_b)}
 \le D^j\prod_{i=2}^j(1+R_{i-1})=O_s(D^j),           \tag{3.8}
\]

because (3.4) makes (3.3) valid and `R_c=o(1)` for every
`c<=2s-1`.  The total fixed-slice/product difference over distinct
\(2s\)-tuples is consequently \(O_s(\varepsilon\mu^{2s})\).

For repeated configurations, group equal entries.  For a Bernoulli
indicator `I` of mean `u` and fixed `a>=1`,

\[
 (I-u)^a=A_a(I-u)+B_a,\qquad |A_a|\le1,\quad |B_a|\le u. \tag{3.9}
\]

This is the unique affine representation on `{0,1}`; the bound on `B_a`
follows by taking expectation.  To make the repeated-tuple count explicit,
suppose the tuple has distinct configurations `G_1,...,G_j` with
multiplicities `a_1,...,a_j`.  Applying (3.9) to every group and expanding
gives terms indexed by `T subseteq [j]` of the form

\[
 \left(\prod_{i\in T}A_{a_i}\right)
 \left(\prod_{i\notin T}B_{a_i}\right)
 \mathbb E\prod_{i\in T}(I_{G_i}-u).                 \tag{3.9a}
\]

The coefficient outside the expectation has absolute value at most
`u^(j-|T|)`.  The centered expansion used in Lemma 2.1 bounds the remaining
expectation, under either law, by

\[
 C_su^{|T|}x^{-\sum_{a<b\in T}t(G_a,G_b)}.            \tag{3.9b}
\]

Summing the overlap weight by (3.7)--(3.8), while summing configurations
outside `T` freely, shows that all tuples with exactly `j` distinct entries
contribute `O_s((Du)^j)`.  A repeated tuple has `j<=2s-1`, so its total is
`O_s(mu^(2s-1))`.  The same calculation with (2.4) bounds the slice/product
difference for these tuples.  Thus the entire finite-population comparison
error is at most

\[
 O_s(\varepsilon\mu^{2s})+O_s((1+R_{2s})^{2s}\mu^{2s-1}). \tag{3.10}
\]

The second summand is exponentially negligible because the punctured mean
satisfies

\[
             \mu\ge\exp((2-4\alpha+o(1))r\log r).     \tag{3.11}
\]

The product-measure high-moment theorem gives

\[
 {\mathbb E_{\rm prod}(X_v-\mu)^{2s}\over\mu^{2s}}
                  =O_s((rx^3)^{-s}).                 \tag{3.12}
\]

Finally \(\widetilde\mu/\mu=1+O_s(\varepsilon)\).  Combining
(3.10)--(3.12) proves (3.5).
\(\square\)

Exactly the same comparison applies to the global surviving-edge count
`mathsf Z`.  Using the proved unrooted product-measure moment estimate gives

\[
 {\mathbb E_{\rm sl}(\mathsf Z-\mathbb E_{\rm sl}\mathsf Z)^{2s}
       \over(\mathbb E_{\rm sl}\mathsf Z)^{2s}}
 =O_s((rx)^{-s})+O_s(r^2/(xN_*)).                    \tag{3.13}
\]

The proof is verbatim: the unrooted overlap kernels replace (3.2), and
their row sums are even smaller.

### Corollary 3.2 (uniform fixed-slice purge)

Fix constants `1<K_1<K_0<K`, take `s=3`, and assume `alpha<1/18`.
On every uniform two-shore slice with `x>=r^{-alpha}`, define degrees,
shore averages, bad targets, and the incidence fraction `beta` exactly as
in the independent checkpoint theorem.  With

\[
                         \epsilon_r=r^{-1/2},          \tag{3.14}
\]

one has, uniformly over the exact shore sizes,

\[
 \Pr_{\rm sl}(\beta>\epsilon_r)
       =O(r^{-3/2}x^{-9})+O(r^{-3/2}x^{-3})+e^{-\Omega(r)}. \tag{3.15}
\]

On the complementary event, deleting the bad targets restores the cap and
satisfies the same deterministic trim inequalities as before.

#### Proof

Equation (3.5), the elementary inequality

\[
 y\mathbf1_{y>K_1}
 \le {K_1\over(K_1-1)^6}(y-1)^6,                    \tag{3.16}
\]

and the exact incidence identity

\[
 |V_\sigma|p_\sigma\widetilde\mu_\sigma
                         =2r\mathbb E_{\rm sl}\mathsf Z \tag{3.17}
\]

give expected over-threshold incidence, in edge units,
\(O(r^{-2}x^{-9})+e^{-\Omega(r)}\).  Markov at the threshold
\(\epsilon_r\mathbb E\mathsf Z\) gives the first term in (3.15).  Equation (3.13),
with relative tolerance `r^{-1/4}`, gives the second.  The shore sizes are
fixed, so no binomial shore-size estimate is needed.  Outside this global
count deviation, every target above `K_0` times its realized average is
counted at the `K_1` expected threshold.  The deterministic trimming
calculation is measure-free.
\(\square\)

This proves that exact shore counts are not the quenched obstruction.

### Corollary 3.3 (uncompressed sixth moment and optimized trim scale)

The component proof contains a stronger statement than the compressed
bound (3.5).  Uniformly on fixed slices for `alpha<1/15`,

\[
 {\mathbb E_{\rm sl}(X_v-\widetilde\mu)^6
       \over\widetilde\mu^6}
 =O\left(
 r^{-3}x^{-9}+r^{-4}x^{-21}+r^{-4}x^{-18}
                  +r^{-5}x^{-45}
 \right)+e^{-\Omega(r)}.                              \tag{3.18}
\]

Consequently, if `alpha<1/15`, one may choose a fixed `delta>0` satisfying

\[
 \delta<\min\{1-9\alpha,\ 2-21\alpha,\
                    2-18\alpha,\ 3-45\alpha\}.        \tag{3.19}
\]

With the more economical trim threshold `epsilon_r=r^(-delta)`, the
uniform fixed-slice failure probability is

\[
\begin{aligned}
 \Pr_{\rm sl}(\beta>r^{-\delta})
 =O(&r^{-2+\delta}x^{-9}
     +r^{-3+\delta}x^{-21}
     +r^{-3+\delta}x^{-18} \\
    &+r^{-4+\delta}x^{-45}
     +r^{-3}x^{-3})+e^{-\Omega(r)}.                   \tag{3.20}
\end{aligned}
\]

This is summable over `O(r log r)` prescribed slices under (3.19).

#### Proof

For six distinct configurations, every nonzero dependency-component
partition has type

\[
                         2+2+2,\quad2+4,\quad3+3,
                         \quad\hbox{or}\quad6.         \tag{3.21}
\]

The rooted component bounds therefore give, before finite-population
comparison,

\[
 O\left(R_1^3+R_1Q_2^3+Q_{3/2}^4+Q_3^5\right).       \tag{3.22}
\]

For `alpha<1/15`, the first term in each rooted component-kernel estimate
dominates:

\[
 R_1=O(r^{-1}x^{-3}),\qquad
 Q_c=O(r^{-1}x^{-3c})\quad(c=3/2,2,3).                \tag{3.23}
\]

Substitution in (3.22) gives the four terms of (3.18).  Here is the range
check for the finite-population transfer.  For a six-tuple, (3.7)--(3.8)
uses `R_c` only through `c=5`.  Lemma 1.1 gives, for all those `c`,

\[
 R_c=O_c(r^{-1}x^{-3c}+r^{-2}x^{-4c})=o(1),           \tag{3.23a}
\]

because `alpha<1/15` implies `3c alpha<1` and
`4c alpha<4/3<2`.  Thus the summed fixed-slice error remains
`O(r^2/(xN_*))=e^{-Omega(r)}`.  Repeated configurations cost
`O(mu^5)`, hence are exponentially negligible after division by `mu^6`.

For completeness, the optimized purge also needs the global count beyond
the compressed range of (3.13).  Put

\[
 \vartheta={D_M\over(2r+1)!}=e^{-\Theta(r)}.           \tag{3.23b}
\]

The proved unrooted kernels satisfy, for every fixed `c<=5`,

\[
 \widehat R_c=O_c(\vartheta(ra_c+a_c^2+a_c^4)),\qquad
 \widehat Q_c=O_c(\vartheta(r+ra_c+a_c^2+a_c^4)),     \tag{3.23c}
\]

where `a_c=x^(-c)-1`.  In the present range the factors multiplying
`vartheta` are polynomial in `r`.  Applying the same four component types
and the same fixed-slice comparison therefore gives

\[
 {\mathbb E_{\rm sl}(\mathsf Z-\mathbb E_{\rm sl}\mathsf Z)^6
       \over(\mathbb E_{\rm sl}\mathsf Z)^6}
 =O((rx)^{-3})+e^{-\Omega(r)}                       \tag{3.23d}
\]

uniformly for `alpha<1/15`.  A fixed relative tolerance in (3.23d) gives
the final `r^(-3)x^(-3)` term in (3.20).

Apply (3.16), sum over the two shores, and divide by the trim threshold.
This multiplies (3.18) by `r^(1+delta)`.  A fixed sufficiently small
relative tolerance for the global edge count is enough because
`K_1<K_0`; its failure probability is the last polynomial term of (3.20).
Finally multiply (3.20) by `O(r log r)`.  The four resulting powers of `r`
are negative precisely under (3.19); the global term is smaller.  This
proves the corollary.
\(\square\)

## 4. The exact stopped-Palm identity

Let `H` be any nonempty residual hypergraph, with `Z` configurations and
with exactly `2r` targets from each shore in every configuration.  On shore
`sigma`, define

\[
 \bar d_\sigma={2rZ\over n_\sigma},\qquad
 B_\sigma=\{v:d(v)>K_0\bar d_\sigma\},qquad
 \beta_\sigma={1\over Z}\sum_{v\in B_\sigma}d(v).    \tag{4.1}
\]

Choose `E` uniformly from the configurations of `H`, and then choose
`V_sigma` uniformly from the `2r` shore-`sigma` targets of `E`.

### Proposition 4.1 (incidence Palm formula)

Conditionally on `H`,

\[
 \boxed{
 \Pr(V_\sigma\in B_\sigma\mid H)
       ={\beta_\sigma\over2r}.}                       \tag{4.2}
\]

#### Proof

The two-stage choice selects target `v` with probability
`d(v)/(2rZ)`.  Sum this identity over `B_sigma`.
\(\square\)

Now let `H_j^*` be the provisional residual after round `j` of the actual
isolated-edge process and before cap trimming.  Let `G_j` be any event
measurable before inspecting whether the provisional cap trim is large;
for example, it can say that all earlier bites and trims succeeded and the
density threshold has not yet been reached.  Put
`beta_j=beta_(j,1)+beta_(j,2)`.

### Proposition 4.2 (stopped annealed reduction)

For every deterministic `epsilon>0` and every finite stopped schedule,

\[
 \Pr(\exists j:G_j\ \hbox{and}\ \beta_j>\epsilon)
 \le {1\over\epsilon}\sum_j\mathbb E[
                       \mathbf1_{G_j}\beta_j].        \tag{4.3}
\]

Moreover, under the Palm experiment of Proposition 4.1 applied after
sampling `H_j^*`,

\[
 \mathbb E[\mathbf1_{G_j}\beta_j]
 =2r\sum_{\sigma=1}^2
       \Pr(G_j\ \hbox{and}\ V_{j,\sigma}\in B_{j,\sigma}). \tag{4.4}
\]

#### Proof

Equation (4.3) is Markov's inequality followed by a union bound.  Average
(4.2) over the stopped state law to obtain (4.4).
\(\square\)

Therefore Gate A does **not** require a tail bound conditional on every
fully revealed history.  It is enough to prove the summed, stopped Palm
bound on the right of (4.4).  This is an annealed statement about one
size-biased target root.

There is an equivalent fixed-slice formulation.  Conditional on the two
shore sizes of `H_j^*`, let `U_j` be the law obtained by choosing uniformly
random subsets of those sizes and taking the induced punctured
configuration hypergraph.  Define `beta=0` if that induced hypergraph has
no edge.  This is the correct state space: accepted configurations and cap
trims delete targets together with every incident configuration, while
unaccepted marks are forgotten, so every actual residual is exactly the
subhypergraph induced by its two surviving target sets.  Corollary 3.2 gives

\[
 \Pr_{U_j}(\beta>r^{-1/2})
 =O(r^{-3/2+9\alpha})                                \tag{4.5}
\]

uniformly before the density threshold.  Since there are `O(r log r)`
rounds, the following one-event comparison would close the trim part of
Gate A:

\[
 \Pr(\beta_j>r^{-1/2}\mid G_j,\hbox{ shore sizes})
 \le r^{\kappa+o(1)}
       \Pr_{U_j}(\beta>r^{-1/2})                      \tag{4.6}
\]

for some fixed `kappa` satisfying

\[
                         \kappa+9\alpha<1/2.           \tag{4.7}
\]

Indeed, (4.5)--(4.7) union-bound over the stopped schedule.  More generally
one may compare the Palm expectation in (4.4) directly; neither form asks
for pointwise control on all histories.

Using Corollary 3.3 instead, a comparison factor `r^kappa` is admissible
whenever `alpha<1/15` and one can choose `delta>0` with

\[
 \kappa+\delta<\min\{1-9\alpha,\ 2-21\alpha,\
                         2-18\alpha,\ 3-45\alpha\},
 \qquad \kappa<2-3\alpha.                             \tag{4.7a}
\]

At the much smaller stopping exponent used by the current descent theorem,
this permits almost one full polynomial power of local shape bias.  It is
still a hypothesis on the actual stopped law, not a proved comparison.

### Proposition 4.3 (exact isolated-mark transition kernel)

Fix the current residual hypergraph and let `G` be its conflict graph on
the surviving configurations.  Mark the vertices of `G` independently
with probability `p`, and let `A` be the set of marked vertices having no
marked neighbour.  For an independent set `A_0` of `G`, put

\[
 U_{A_0}=V(G)\setminus N_G[A_0],                       \tag{4.8}
\]

and, for a graph `J`, define

\[
 \zeta_p(J)=\Pr(\text{the Bernoulli-}p\text{ marked set in }J
                 \text{ has no isolated marked vertex}).                \tag{4.9}
\]

The empty marked set is allowed.  Then the exact conditional transition
probability is

\[
 \boxed{
 \Pr(A=A_0\mid G)
 =p^{|A_0|}(1-p)^{|N_G(A_0)|}\zeta_p(G[U_{A_0}]).
 }                                                       \tag{4.10}
\]

After this transition, the surviving configurations are exactly
`U_(A_0)`.

#### Proof

The event `A=A_0` has three disjoint requirements.  Every vertex of `A_0`
is marked; every vertex in its open neighbourhood is unmarked; and the
marks in `U_(A_0)` contain no isolated marked vertex.  The three involved
vertex sets are disjoint, so independence of the fresh marks multiplies
their probabilities and gives (4.10).  A configuration survives target
deletion exactly when it is disjoint from every accepted configuration,
which is exactly membership in `U_(A_0)`.
\(\square\)

In particular, for two candidate accepted matchings of the same size, their
relative transition weight contains both a closed-neighbourhood factor and
the ratio of the two `zeta_p` terms.  Neither factor is determined by the
two new shore sizes.  Formula (4.10) is an exact filtration representation,
not an approximation: a proposed quenched transfer must control its effect
on the Palm statistic, or avoid comparing state laws altogether.

## 5. Why a full-state likelihood transfer along the revealed filtration cannot work

The reduction above is genuinely local.  A comparison of the one-edge
partial residual state with a uniform slice is exponentially false at the
first sequential reveal.

Let

\[
 N_M={2r+1\choose r},\qquad N_L={2r+1\choose r-1}.     \tag{5.1}
\]

Delete the targets of one uniformly selected punctured configuration.
The deleted state consists of `2r` middle and `2r` lower targets.  Let `Q`
be its law.  Let `U` choose those two deleted target sets independently and
uniformly among all subsets of the same sizes.

### Theorem 5.1 (full-slice support obstruction)

The support of `Q` has `U`-mass at most

\[
 { (2r+1)!\over
    {N_M\choose2r}{N_L\choose2r}}
                         =\exp(-\Omega(r^2)).          \tag{5.2}
\]

Consequently

\[
 \|Q-U\|_{\rm TV}\ge1-\exp(-\Omega(r^2)),             \tag{5.3}
\]

and every Radon--Nikodym density `dQ/dU` satisfies

\[
                         \|dQ/dU\|_\infty
                              \ge\exp(\Omega(r^2)).    \tag{5.4}
\]

#### Proof

There are exactly `(2r+1)!` directed punctured configurations, and each
determines one deleted pair of target sets.  Hence the support size is at
most that number, while the uniform slice has the denominator in (5.2)
states.

For an elementary asymptotic bound, the largest coefficient in row
`2r+1` of Pascal's triangle is at least `2^(2r+1)/(2r+2)`, and

\[
 {N_L}={r\over r+2}N_M.
\]

Thus \(\log N_M,\log N_L=\Omega(r)\).  Also

\[
                         {N\choose k}\ge(N/k)^k        \tag{5.5}
\]

for `k<=N`; this follows directly from the product formula.  The logarithm
of the denominator of (5.2) is therefore \(\Omega(r^2)\), whereas
\(\log((2r+1)!)=O(r\log r)\).  This proves (5.2).

If `S=supp(Q)`, then total variation is at least
`Q(S)-U(S)=1-U(S)`, proving (5.3).  Finally
`1=Q(S)<=||dQ/dU||_infty U(S)`, which proves (5.4).
\(\square\)

This obstruction applies to a legitimate sequential refinement of the
isolated-edge filtration: reveal one accepted configuration and its
targets before revealing the rest of the accepted matching.  It does not
say that the bad-incidence statistic is biased by \(\exp(\Omega(r^2))\).
Rather, it proves that a full-state likelihood or total-variation route
cannot be maintained along this sequentially refined filtration.  It does
not rule out a comparison posed only at complete-round boundaries.  The
currently proved reduction asks directly for the Palm/high-degree statistic
in Section 4, or for a small collection of rooted overlap observables
controlling it.

## 6. Exact remaining statement

The conclusions may be summarized without probabilistic ambiguity.

1. Independent Bernoulli retention and uniform exact-size retention have
   the same fixed-target high moments through the required polynomial
   scale.
2. Therefore deterministic shore sizes are not the missing conditioning
   issue.
3. Uniform conditional control over every fully revealed history is
   stronger than needed.
4. Full-state comparison with a uniform slice is impossible along the
   sequential one-edge revealment, by (5.2)--(5.4); no claim is made about
   complete-round boundary laws.
5. What remains is the stopped one-root shape-bias estimate (4.4), or the
   one-event slice comparison (4.6).  The simple threshold gives the budget
   `kappa+9alpha<1/2`; retaining the component types separately gives the
   stronger budget (4.7a).
6. This concerns the existing two-rank punctured descent only.  Even the
   optimized fixed-slice purge range `alpha<1/15` does not reach a density
   `o(r^(-1/3))`; if all-depth capacity requires that smaller leave, a
   separate compatible coverdown or a substantially stronger adaptive
   theorem is still necessary.

No equality in this note identifies the actual history law with a product
or fixed-slice law, and no conditioning on future cap persistence is used.
