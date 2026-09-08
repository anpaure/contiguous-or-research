# Punctured independent residual: fixed high moments and the bad-incidence tail

**Status (2026-08-22).**  The theorem below upgrades the fixed-target
variance calculation to every fixed even centered moment.  In the
independent residual model it recovers the factor `2r` which was missing
from the naive Chebyshev purge: the sixth moment makes the aggregate
over-threshold incidence mass summable over `O(r log r)` checkpoints.

This does **not** by itself close Gate A.  The actual isolated-edge process
does not regenerate an independent residual after each bite.  The remaining
statement is now precisely a quenched version of the high-moment estimate
along trimmed histories.

## 1. Setup and rooted pair kernels

Use the directed punctured-configuration hypergraph with parameter `r`.
Fix one target `v` and condition on retaining it.  Every other lower target
is retained independently with probability `x`, every other middle target
with probability `y>=x`, and

\[
                         x\ge r^{-\alpha}.           \tag{1.1}
\]

Let `mathcal F_v` be the `D=d(v)` configurations containing `v`.  Put

\[
 X_v=\sum_{F\in\mathcal F_v}I_F,
 \qquad \mu=\mathbb EX_v=Dw,                       \tag{1.2}
\]

where `I_F` says that all targets of `F-{v}` survive.  The mean `w` is the
same for every `F in mathcal F_v`, since every configuration has the same
two shore sizes.  For distinct `F,G in mathcal F_v`, write

\[
                   t(F,G)=|(F\cap G)-\{v\}|.        \tag{1.3}
\]

For each fixed real `c>=1`, define

\[
 R_c=\max_F {1\over D}\sum_{G\ne F}
                 (x^{-c t(F,G)}-1),                 \tag{1.4}
\]

and

\[
 Q_c=\max_F {1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                 x^{-c t(F,G)}.                     \tag{1.5}
\]

### Lemma 1.1 (rooted kernel bounds)

For every fixed `c`, uniformly under (1.1), provided `c alpha<1/2`,

\[
 R_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right),
 \qquad
 Q_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right).   \tag{1.6}
\]

In particular

\[
                         R_1=O((rx^3)^{-1}).         \tag{1.7}
\]

#### Proof

The rooted-polymer proof for the variance applies with retention floor
`x^c`.  With

\[
                         a_c=x^{-c}-1,
\]

its nonnegative overlap expansion gives

\[
 R_c=O_c\left({a_c\over r}+{a_c^3\over r}
                         +{a_c^4\over r^2}\right)
       +e^{-\Omega_c(r\log r)}.                     \tag{1.8}
\]

The exponentially small term is the excluded diagonal `G=F`; it is
negligible because `c alpha<1/2`.  The activity condition in the polymer
estimate is also valid, since `a_c=O(r^(c alpha))=o(sqrt r)`.

To pass from `R_c` to `Q_c`, first note

\[
 {1\over D}\sum_{G\ne F}\mathbf1_{t(F,G)>0}
 \le {1\over D}\sum_{G\ne F}t(F,G)=O(1/r).         \tag{1.9}
\]

The last estimate is the coefficient of the linear activity in the same
rooted overlap polynomial: divide its bound
`O(a/r+a^3/r+a^4/r^2)` by `a` and let `a` decrease to zero.  All
coefficients are nonnegative, so the passage to the limit is valid.
Finally

\[
 \mathbf1_{t>0}x^{-ct}
 \le \mathbf1_{t>0}+(x^{-ct}-1),                   \tag{1.10}
\]

and (1.8)--(1.10), together with `a_c<=x^{-c}`, prove (1.6).
\(\square\)

## 2. Connected overlap tuples

For distinct configurations `F_1,...,F_j`, form their dependency graph on
`[j]`, joining `p,q` when `t(F_p,F_q)>0`.  Put

\[
                         Z_F=I_F-w.                 \tag{2.1}
\]

### Lemma 2.1 (one connected component)

For each fixed integer `j>=3`, the sum over ordered, distinct, connected
`j`-tuples satisfies

\[
 \sum_{\substack{(F_1,\ldots,F_j)\\ \mathrm{connected}}}
       \left|\mathbb E\prod_{i=1}^j Z_{F_i}\right|
 \le C_j(Dw)^j Q_{j/2}^{j-1}.                    \tag{2.2}
\]

For `j=2`, the analogous sum is at most

\[
                         (Dw)^2R_1.                 \tag{2.3}
\]

#### Proof

For a subset `S subseteq [j]`, if a target `u ne v` occurs in `m_u`
members of `S`, then

\[
 {\mathbb E\prod_{i\in S}I_{F_i}\over w^{|S|}}
 =\prod_{\substack{u\ne v\\m_u\ge1}}p_u^{1-m_u}
 \le x^{-\sum_{p<q\in S}t(F_p,F_q)},               \tag{2.4}
\]

because `p_u>=x` and `m_u-1<=binom(m_u,2)`.  Expanding the centered product
into `2^j` terms and enlarging every exponent to include all pairs gives

\[
 \left|\mathbb E\prod_{i=1}^jZ_{F_i}\right|
 \le2^jw^j x^{-\sum_{p<q}t(F_p,F_q)}.              \tag{2.5}
\]

Give the complete graph on `[j]` edge weights `t(F_p,F_q)`.  A uniformly
random spanning tree of `K_j` contains each edge with probability `2/j`.
Hence some spanning tree `T` has weight at least `2/j` times the total
edge weight.  If the dependency graph is connected, a maximum-weight tree
may be chosen with all its edges positive.  Therefore

\[
 x^{-\sum_{p<q}t(F_p,F_q)}
 \le\prod_{pq\in T}
       \mathbf1_{t(F_p,F_q)>0}x^{-(j/2)t(F_p,F_q)}. \tag{2.6}
\]

There are `j^(j-2)` labelled spanning trees.  For each fixed tree, root it
and sum successively from its leaves.  Every leaf sum is at most `DQ_(j/2)`
by (1.5), while the root has `D` choices.  Equations (2.5)--(2.6) prove
(2.2).

For two configurations, positive association of monomials and (2.4) give

\[
 0\le\mathbb E Z_FZ_G
 \le w^2(x^{-t(F,G)}-1).
\]

Summing and applying (1.4) proves (2.3).  \(\square\)

## 3. Every fixed even centered moment

### Theorem 3.1 (high-moment regeneration)

Fix an integer `s>=1` and assume

\[
                         0<\alpha<{1\over6s}.       \tag{3.1}
\]

Then, uniformly for `x>=r^(-alpha)` and `y>=x`,

\[
 \boxed{
 {\mathbb E(X_v-\mu)^{2s}\over\mu^{2s}}
       =O_s\left({1\over r^sx^{3s}}\right).
 }                                                       \tag{3.2}
\]

#### Proof

First take an ordered `2s`-tuple of distinct configurations.  Its centered
expectation is zero if its dependency graph has a singleton component.
Otherwise its connected components have sizes `j_1,...,j_k>=2`.
Independence across components and Lemma 2.1 show that a component of size
two contributes `O((Dw)^2 R_1)` after summation, while one of size `j>=3`
contributes `O_j((Dw)^j Q_(j/2)^(j-1))`.

Put

\[
                         \rho={1\over rx^3}.         \tag{3.3}
\]

Lemma 1.1 gives the size-two bound `O((Dw)^2 rho)`.  For fixed
`3<=j<=2s`, it also gives

\[
 Q_{j/2}^{j-1}
 =O_j\left[
   (r^{-1}x^{-3j/2})^{j-1}
  +(r^{-2}x^{-2j})^{j-1}\right]
 =O_j(\rho^{j/2}).                                  \tag{3.4}
\]

For the first term, division by `rho^(j/2)` leaves at most

\[
 r^{1-j/2+\alpha 3j(j-2)/2}=o(1),                \tag{3.5}
\]

because (3.1) implies `alpha<1/(3j)`.  The second term is smaller under
the same hypothesis: its quotient has exponent at most

\[
 2-3j/2+\alpha j(4j-7)/2<0.                        \tag{3.6}
\]

Multiplying the component estimates gives
`O_s((Dw)^(2s) rho^s)`, because `sum j_i=2s`.  There are only a constant
number, depending on `s`, of component partitions.

It remains to allow repeated configurations.  For a Bernoulli variable
`I` of mean `w` and every fixed integer `m>=1`, its centered power has the
affine form

\[
                         (I-w)^m=A_m(I-w)+B_m,       \tag{3.7}
\]

where `|A_m|<=1` and `|B_m|=|E(I-w)^m|<=w`.  Group equal configurations
in the tuple and apply (3.7).  Every resulting term is a centered moment
of fewer distinct configurations times at most one factor `w` for each
constant group.  The preceding component argument applies to its centered
groups.  Since at most `2s-1` distinct configurations remain, its total
after summation is at most

\[
 O_s((1+\rho)^{s}(Dw)^{2s-1}).                     \tag{3.8}
\]

Appendix C.3's mean bound gives

\[
 \mu=Dw\ge\exp((2-4\alpha+o(1))r\log r),           \tag{3.9}
\]

so (3.8), divided by `mu^(2s)`, is exponentially smaller than `rho^s`.
This proves (3.2).  \(\square\)

## 4. Aggregate bad-incidence consequence

Fix `K_0>1` and put `Y_v=X_v/mu`.  Since

\[
 y\,\mathbf1_{y>K_0}
 \le {K_0\over(K_0-1)^{2s}}(y-1)^{2s}
 \qquad(y\ge0),                                    \tag{4.1}
\]

Theorem 3.1 gives

\[
 \mathbb E[Y_v\mathbf1_{Y_v>K_0}]
       =O_{s,K_0}((rx^3)^{-s}).                    \tag{4.2}
\]

Let `V_sigma` be an original target shore, let `p_sigma` be its retention
probability, and extend `X_v` to be zero when `v` is absent.  Define

\[
 I_{K_0}=\sum_\sigma\sum_{v\in V_\sigma}
 \mathbf1_{\{v\ \text{retained}\}}X_v
 \mathbf1_{\{X_v>K_0\mu_\sigma\}}.                 \tag{4.3}
\]

For each shore,
`|V_sigma|p_sigma mu_sigma=2r E mathsf Z`, where `mathsf Z` is the number
of surviving configurations.  Summing (4.2) over both shores therefore
gives the exact aggregate estimate

\[
 {\mathbb E I_{K_0}\over\mathbb E\mathsf Z}
 =O_{s,K_0}\left(r(rx^3)^{-s}\right).              \tag{4.4}
\]

For `s=3` and `alpha<1/18`, this is

\[
                         O(r^{-2}x^{-9})=o(1).       \tag{4.5}
\]

We next replace expected averages by realized averages.

### Lemma 4.1 (global surviving-edge concentration)

For every fixed `s` under (3.1),

\[
 {\mathbb E(\mathsf Z-\mathbb E\mathsf Z)^{2s}
       \over(\mathbb E\mathsf Z)^{2s}}
 =O_s((rx)^{-s}).                                  \tag{4.6}
\]

#### Proof

Let `mathcal N=(2r+1)!` be the number of full configurations and put

\[
 \vartheta={D_M\over\mathcal N}={2r\over A}=e^{-\Theta(r)}. \tag{4.7}
\]

For full configurations `F,G`, set `t_0(F,G)=|F\cap G|` and define

\[
 \widehat R_c={1\over\mathcal N}\max_F\sum_{G\ne F}
                    (x^{-ct_0(F,G)}-1),
\]

\[
 \widehat Q_c={1\over\mathcal N}\max_F
        \sum_{\substack{G\ne F\\t_0(F,G)>0}}x^{-ct_0(F,G)}. \tag{4.8}
\]

With `a_c=x^(-c)-1`, expand `(1+a_c)^t-1` and double-count subsets
`T\subseteq F\cap G`.  Singleton `T` contribute
`O(vartheta r a_c)`, because `F` has `4r` targets and both target degrees
are `Theta(D_M)`.  For `|T|>=2`, the boundary-codegree estimate and the
polymer sum give

\[
 {1\over\mathcal N}\sum_{\substack{T\subseteq F\\|T|\ge2}}
 a_c^{|T|}\deg(T)
 \le C\vartheta r^2\mathcal P_2(Ca_c)
 =O_c(\vartheta(a_c^2+a_c^4)).                     \tag{4.9}
\]

Also

\[
 {1\over\mathcal N}\sum_{G\ne F}\mathbf1_{t_0(F,G)>0}
 \le {1\over\mathcal N}\sum_{G\ne F}t_0(F,G)
 =O(\vartheta r).                                  \tag{4.10}
\]

Therefore

\[
 \widehat R_c=O_c(\vartheta(ra_c+a_c^2+a_c^4)),
 \qquad
 \widehat Q_c=O_c(\vartheta(r+ra_c+a_c^2+a_c^4)).  \tag{4.11}
\]

These estimates are exponentially smaller than, respectively,
`O_c(a_c/r+a_c^4/r^2)` and
`O_c(1/(rx^c)+1/(r^2x^(4c)))`.  Apply the dependency-component and
maximum-spanning-tree proof of Theorem 3.1 with `D,w,R_c,Q_c` replaced by
`mathcal N,w_0,widehat R_c,widehat Q_c`, where
`w_0=x^(2r)y^(2r)`.  The weakened displayed bounds give (4.6); repeated
configurations are negligible because `mathcal N w_0` is exponential.
\(\square\)

The two shore sizes are independent binomial variables with exponential
means and hence have exponentially small fixed-relative-deviation tails
(the exponential-moment proof is the usual one-line Chernoff argument).
Take `s=3` and `eta_r=r^(-1/4)`.  Equation (4.6) and Markov give

\[
 \Pr\left(
 \left|{\mathsf Z\over\mathbb E\mathsf Z}-1\right|>\eta_r
 \right)=O(r^{-3/2}x^{-3}).                         \tag{4.12}
\]

Thus both realized average target degrees are `(1+O(eta_r))` times their
conditional means, outside the event in (4.12) and an exponentially small
shore-size event.

Fix constants `1<K_1<K_0<K`.  For all sufficiently large `r`, every target
above `K_0` times its realized shore average is counted by `I_(K_1)`.
Equation (4.4), Markov's inequality at threshold
`epsilon_r E mathsf Z`, where `epsilon_r=r^(-1/2)`, and (4.12) show that the
failure probability at one independent checkpoint is

\[
 O(r^{-3/2}x^{-9})+O(r^{-3/2}x^{-3})
 =O(r^{-3/2+9\alpha}).                             \tag{4.13}
\]

On the complementary event, put

\[
 B_\sigma=\{v:X_v>K_0\bar d_\sigma\},\qquad
 \beta_\sigma={1\over\mathsf Z}\sum_{v\in B_\sigma}X_v,
 \qquad \beta=\sum_\sigma\beta_\sigma.            \tag{4.14}
\]

Then `beta<=epsilon_r/(1-eta_r)`.  Delete the targets in `B_sigma` and all
incident configurations.  If primes denote the trimmed hypergraph, then

\[
 \mathsf Z'\ge(1-\beta)\mathsf Z,
 \qquad
 \bar d'_\sigma\ge(1-\beta)\bar d_\sigma,
 \qquad
 {\Delta'_\sigma\over\bar d'_\sigma}
       \le {K_0\over1-\beta}\le K,                 \tag{4.15}
\]

and

\[
 |B_\sigma|\le {\beta_\sigma n_\sigma\over2rK_0}. \tag{4.16}
\]

The inequalities follow by charging every deleted edge to one bad-target
incidence; every retained target has old degree at most
`K_0 bar d_sigma`, and `bar d_sigma=2r mathsf Z/n_sigma`.

For any prescribed geometric density schedule of `O(r log r)` independent
product-measure checkpoints, (4.13) union-bounds when `alpha<1/18`, so all
individual trim bounds hold simultaneously.  The corresponding deterministic
ledger has `sum_j sum_sigma n_(sigma,j)=O(rA)`; hence (4.16) would cost
`O(epsilon_r A)=O(A/sqrt r)=o(A)` targets, while
`sum_j -log(1-beta_j)=O(sqrt r log r)=o(r log r)`.  These trims are
snapshotwise and do not form a nested process.  A quenched version along the
actual trimmed history is still required.

The qualifier "independently regenerated" is essential.  In the actual
isolated-edge nibble, the residual target set is history-dependent and is
not a product measure.  The remaining Gate A input is the quenched analogue
of (4.2)--(4.16), or another argument giving the same aggregate
bad-incidence bound along every trimmed history.
