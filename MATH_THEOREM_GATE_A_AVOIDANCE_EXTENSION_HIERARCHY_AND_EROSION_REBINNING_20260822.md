# Gate A carrier avoidance: an approximately log-concave extension hierarchy and the erosion-rebinning gate

**Date:** 2026-08-22  
**Status:** unconditional finite-hypergraph theorem and punctured-scale
reduction.  This does not prove the remaining erosion-rebinning estimate.

The rootwise identity

\[
 R_m(v)=\sum_{G\not\ni v}{(d_v-a_G(v))_m\over(d_v)_m},
 \qquad
 \zeta_m(v)=|E(H)|-R_m(v)
\]

turns the Gate-A carrier hazard into a zero-overlap extension count.  This
note develops that count one level further.  The result is useful for two
reasons.

1. For every fixed current degree bucket, the mean avoidance count of its
   surviving descendant carriers has positive logarithmic drift at most
   `O(Delta_C^2/Z)`.  In the stopped punctured range this is
   `O(z r^3/n)=o(z)`, and its contribution over the entire density clock is
   summably negligible.
2. Consequently, the unresolved part of the downward-regression lemma is
   not survival selection inside an old degree bucket.  It is the sorting
   of those descendants into *new* degree buckets by their realized
   erosion.  The final section gives the exact two-extension matrix and the
   erosion-decorated covariance which must be controlled.

No independence, regularity, or punctured geometry is used in the extension
theorem.  Punctured geometry enters only in converting its error to `o(z)`
and in the proposed boundary-polymer attack on the remaining decorated
statistic.

## 1. Ordered carrier--matching extensions

Let `H` be a finite simple hypergraph, let

\[
 Z=|E(H)|,\qquad
 \Gamma(F)=\{G\in E(H):G\cap F\ne\varnothing\},\qquad
 \Delta_C=\max_F|\Gamma(F)|.                       \tag{1.1}
\]

Fix a root shore, an integer `m>=1`, and an arbitrary tagged root set
`B`.  An ordered `m`-carrier is

\[
 \gamma=(v;F_1,\ldots,F_m),\qquad
 v\in B,\quad F_i\ne F_j,\quad v\in F_i.           \tag{1.2}
\]

The carrier rows need not be mutually disjoint; in fact they all contain
the root.  For `t>=0`, let `Omega_t(B;H)` be the set of objects

\[
 \omega=(v;F_1,\ldots,F_m;G_1,\ldots,G_t)           \tag{1.3}
\]

in which `gamma` is an ordered carrier and the `G_j` are ordered,
pairwise target-disjoint, and target-disjoint from every `F_i`.  Put

\[
 X_t(B;H)=|\Omega_t(B;H)|.                          \tag{1.4}
\]

For `omega in Omega_t`, define its extension set and extension count by

\[
 \mathcal D(\omega)=
 \{K\in E(H):K\cap F_i=\varnothing\ (1\le i\le m),\ 
                 K\cap G_j=\varnothing\ (1\le j\le t)\},
 \qquad r(\omega)=|\mathcal D(\omega)|.             \tag{1.5}
\]

Appending the last row is a bijection, so

\[
 \boxed{X_{t+1}=\sum_{\omega\in\Omega_t}r(\omega).} \tag{1.6}
\]

Whenever `X_t>0`, write

\[
 q_t={X_{t+1}\over X_t}
     =\mathbb E_{\omega\in\Omega_t}r(\omega).      \tag{1.7}
\]

The union of the closed conflict neighbourhoods of the `m+t` constituent
rows contains every nonextension.  Therefore

\[
                 Z-(m+t)\Delta_C\le r(\omega)\le Z. \tag{1.8}
\]

The lower bound is useful only when positive, which will always be the case
in the punctured range below.

## 2. Exact curvature and approximate log concavity

Choose `omega` uniformly from `Omega_t` and then choose `K` uniformly from
`mathcal D(omega)`, with the resulting pair understood under its natural
size-biased law.  Equivalently, `(omega,K)` is uniform on `Omega_(t+1)`.
Put

\[
 \kappa(\omega,K)=|\mathcal D(\omega)\cap\Gamma(K)|. \tag{2.1}
\]

Since appending `K` removes precisely these extensions,

\[
 r(\omega,K)=r(\omega)-\kappa(\omega,K).            \tag{2.2}
\]

### Theorem 2.1 (extension-ratio curvature)

If `X_(t+1)>0`, then

\[
 \boxed{
 q_{t+1}-q_t
 ={\operatorname {Var}_{\Omega_t}r(\omega)\over q_t}
  -\mathbb E_{\Omega_{t+1}}\kappa(\omega,K).}       \tag{2.3}
\]

In particular, if `Z>(m+t)Delta_C`, then

\[
 \boxed{
 (q_{t+1}-q_t)_+
 \le{(m+t)^2\Delta_C^2
       \over4\{Z-(m+t)\Delta_C\}}.}                \tag{2.4}
\]

Equivalently,

\[
 {X_tX_{t+2}\over X_{t+1}^2}
 \le1+{(m+t)^2\Delta_C^2
          \over4\{Z-(m+t)\Delta_C\}^2}.            \tag{2.5}
\]

#### Proof

Under the uniform law on `Omega_(t+1)`, the prefix `omega` is biased by
`r(omega)`.  Consequently

\[
 \mathbb E_{\Omega_{t+1}}r(\omega)
 ={\mathbb E_{\Omega_t}r(\omega)^2
    \over\mathbb E_{\Omega_t}r(\omega)}
 =q_t+{\operatorname {Var}_{\Omega_t}r(\omega)\over q_t}. \tag{2.6}
\]

Average (2.2) and use (2.6), proving (2.3).  The variable `r(omega)` lies
in an interval of length at most `(m+t)Delta_C`.  Popoviciu's variance
inequality and (1.8) give

\[
 \operatorname {Var}r(\omega)\le{(m+t)^2\Delta_C^2\over4},
 \qquad q_t\ge Z-(m+t)\Delta_C.                    \tag{2.7}
\]

The last term in (2.3) is nonnegative (indeed `kappa>=1`), so (2.4)
follows.  Dividing (2.4) by `q_t` proves (2.5).  \(\square\)

Thus exact log concavity can fail only when variation between the
carrier-specific extension counts overcomes the internal conflict charge
`E kappa`.  Even without proving the favourable sign, the possible failure
has additive size `O(Delta_C^2/Z)`.

There is a stronger affine form.  Put

\[
                         \overline C={1\over Z}\sum_{K\in E(H)}
                                           |\Gamma(K)|.       \tag{2.8}
\]

### Theorem 2.2 (common conflict decrement)

Under the hypotheses of Theorem 2.1, with `s=m+t`,

\[
 \boxed{
 |q_{t+1}-(q_t-\overline C)|
 \le \left({s^2\over4}+3s\right)
       {\Delta_C^2\over Z-s\Delta_C}.}              \tag{2.9}
\]

#### Proof

For a fixed `omega`, put

\[
 \mathcal B(\omega)=E(H)-\mathcal D(\omega),\qquad
 h(\omega)=|\mathcal B(\omega)|=Z-r(\omega)\le s\Delta_C. \tag{2.10}
\]

If `K` is uniform on `mathcal D(omega)`, then

\[
 \kappa(\omega,K)
 =|\Gamma(K)|-|\Gamma(K)\cap\mathcal B(\omega)|.    \tag{2.11}
\]

Deleting `h` terms, each at most `Delta_C`, from an average of `Z` terms
in `[0,Delta_C]` changes that average by at most

\[
 {2h\Delta_C\over Z-h}.                            \tag{2.12}
\]

Moreover, double counting conflict pairs gives

\[
 {1\over Z-h}\sum_{K\in\mathcal D(\omega)}
       |\Gamma(K)\cap\mathcal B(\omega)|
 \le {h\Delta_C\over Z-h}.                         \tag{2.13}
\]

Equations (2.11)--(2.13) show, uniformly in `omega`,

\[
 \left|\mathbb E[\kappa(\omega,K)\mid\omega]-\overline C\right|
 \le{3s\Delta_C^2\over Z-s\Delta_C}.               \tag{2.14}
\]

The `Omega_(t+1)` law is obtained by weighting `omega` by `r(omega)`, so
the same uniform bound holds after averaging.  Insert it in (2.3) and use
(2.7).  \(\square\)

Thus adding one disjoint external row subtracts the same global mean
conflict degree from every tagged carrier population, up to
`O_s(Delta_C^2/Z)`.  In particular, passing from `q_0(B_d)` to
`q_1(B_d)` preserves all differences between old degree buckets to that
additive accuracy.  The unresolved issue is the subsequent sorting by
their *new* degrees, not the unconditioned extra-row decrement.

Explicitly, if `B_d` and `B_e` are nonempty old degree buckets and `d<e`,
then, with

\[
 \varepsilon_m=\left({m^2\over4}+3m\right)
              {\Delta_C^2\over Z-m\Delta_C},        \tag{2.15}
\]

\[
 \boxed{
 \bigl(q_1(B_e)-q_1(B_d)\bigr)_+
 \le\bigl(q_0(B_e)-q_0(B_d)\bigr)_+ +2\varepsilon_m.} \tag{2.16}
\]

Thus the desired upward-regression inequality is stable under one
unconditioned extension.  Equation (2.16) is not yet a statement about
the child degree buckets, because those are the columns of the matrix in
Section 7 rather than its old-degree rows.

## 3. The first ratio is exactly the Gate-A avoidance statistic

For a root `v` of degree at least `m`, let

\[
 a_G(v)=|\{F\ni v:F\cap G\ne\varnothing\}|.         \tag{3.1}
\]

A uniform ordered carrier at `v` avoids `G` with probability

\[
 {(d_v-a_G(v))_m\over(d_v)_m}.                      \tag{3.2}
\]

The expression is zero when `G` contains `v`.  Hence, with

\[
 R_m(v)=\sum_{G\not\ni v}{(d_v-a_G(v))_m\over(d_v)_m}, \tag{3.3}
\]

one has

\[
 X_0(B;H)=\sum_{v\in B}(d_v)_m,
 \qquad
 X_1(B;H)=\sum_{v\in B}(d_v)_mR_m(v).              \tag{3.4}
\]

Therefore

\[
 \boxed{q_0(B;H)=
 {\sum_{v\in B}(d_v)_mR_m(v)\over
  \sum_{v\in B}(d_v)_m}.}                          \tag{3.5}
\]

If `B=B_d={v:d_v=d}`, (3.5) is precisely the degree-conditioned mean
avoidance count in (G.122a): all roots in the bucket have the same Palm
weight `(d)_m`.  Since `zeta_m=Z-R_m`, upward regression of `R_m` is the
same as downward regression of the mean carrier hazard.

## 4. Exact deletion recursion and a finite isolated bite

For `K in E(H)`, let

\[
 H_K=H[V(H)-K],\qquad E(H_K)=E(H)-\Gamma(K),         \tag{4.1}
\]

and retain the original root tags `B`; a deleted root contributes no
object.  An object of `Omega_t(B;H)` survives in `H_K` exactly when `K` is
one of its extensions.  Thus

\[
 \boxed{
 \sum_{K\in E(H)}X_t(B;H_K)=X_{t+1}(B;H).}          \tag{4.2}
\]

In particular, if `K` is uniform on `E(H)`,

\[
 \mathbb E_KX_t(B;H_K)={X_{t+1}\over Z}.            \tag{4.3}
\]

Now mark every row independently with probability `p`, accept exactly the
isolated marked rows, delete their targets, and call the residual `H_p`.
For a fixed `omega in Omega_t`, let

\[
 h(\omega)=Z-r(\omega)                              \tag{4.4}
\]

be the union of the conflict neighbourhoods of its constituent rows.
Exactly as in the finite carrier-survival lemma, if
`p Delta_C<=1`,

\[
 \Pr(\omega\text{ survives})=1-ph(\omega)+\rho_p(\omega),
 \qquad
 0\le\rho_p(\omega)
 \le C_{m+t}(p\Delta_C)^2,                          \tag{4.5}
\]

where one may take

\[
                         C_s={s^2\over2}+s.          \tag{4.6}
\]

Indeed, no mark in the union hazard is sufficient.  The quadratic part of
`(1-p)^h-(1-ph)` is at most `s^2(p Delta_C)^2/2`.  Any additional survival
requires a marked hazard row and a second marked conflict neighbour, whose
ordered-pair union bound is at most `s(p Delta_C)^2`.

Summing (4.5) over all objects gives the two-sided finite-bite formula

\[
 \boxed{
 1-p(Z-q_t)
 \le{\mathbb E X_t(B;H_p)\over X_t(B;H)}
 \le1-p(Z-q_t)+C_{m+t}(p\Delta_C)^2.}               \tag{4.7}
\]

At the tangent,

\[
 {d\over dp}\mathbb E X_t(B;H_p)\bigg|_{p=0}
 =X_{t+1}-ZX_t.                                     \tag{4.8}
\]

Equations (4.2) and (4.8) are the discrete and infinitesimal forms of the
same extension recursion.

### Corollary 4.1 (negligible within-bucket selection inflation)

Assume `X_0,X_1>0`, `Z>m Delta_C`, and
`p(m+1)Delta_C<=1/4`.  Define the descendant ratio

\[
 \widetilde R_{m,B}(p)=
 {\mathbb E X_1(B;H_p)\over\mathbb E X_0(B;H_p)}.   \tag{4.9}
\]

Then

\[
 \boxed{
 \left(\log{\widetilde R_{m,B}(p)\over q_0(B;H)}\right)_+
 \le C_m\left{
 {p\,m^2\Delta_C^2\over Z-m\Delta_C}
 +(p\Delta_C)^2\right}.}                          \tag{4.10}
\]

At `p=0` the exact logarithmic derivative is

\[
 {d\over dp}\log\widetilde R_{m,B}(p)\bigg|_{p=0}
 =q_1-q_0.                                          \tag{4.11}
\]

#### Proof

Apply the upper side of (4.7) at `t=1` and the lower side at `t=0`:

\[
 {\widetilde R_{m,B}(p)\over q_0}
 \le {1-p(Z-q_1)+C_{m+1}(p\Delta_C)^2
       \over1-p(Z-q_0)}.                            \tag{4.12}
\]

The denominator is at least `3/4`.  Use `log(1+x)<=x`, discard a
favourable negative part of `q_1-q_0`, and apply (2.4) at `t=0`.  This
proves (4.10).  Differentiating the quotient using (4.8) proves (4.11).
\(\square\)

The set `B` in this corollary is fixed at the start of the bite.  In
particular it may be one current degree bucket.  No claim is made that its
descendants remain in one degree bucket.

## 5. Predictable state-dependent marking

The preceding theorem is conditional on the current deterministic state,
so a predictable scalar marking probability `p(H)` may be inserted
pathwise without any change.  For clarity, there is also an exact
state-mixture formula.

Let `nu` be a law of current states, let

\[
 \mathcal X_t=\mathbb E_\nu X_t(H),\qquad
 \langle f\rangle_t={\mathbb E_\nu[X_t(H)f(H)]\over\mathcal X_t},
 \qquad q_t(H)={X_{t+1}(H)\over X_t(H)},             \tag{5.1}
\]

on the positive fibres.  If

\[
                 \theta=\sup_Hp(H)\Delta_C(H)       \tag{5.2}
\]

is sufficiently small, (4.7) gives

\[
 {\mathbb E_{\nu P}X_t\over\mathcal X_t}
 =1-\langle p(H)\{Z(H)-q_t(H)\}\rangle_t+O_{m+t}(\theta^2). \tag{5.3}
\]

Consequently, for
`bar q_t=mathcal X_(t+1)/mathcal X_t`,

\[
\begin{aligned}
 \log{\bar q_t(\nu P)\over\bar q_t(\nu)}
  ={}&\langle p(H)\{Z(H)-q_t(H)\}\rangle_t\\
    &-\langle p(H)\{Z(H)-q_{t+1}(H)\}\rangle_{t+1}
      +O_{m+t}(\theta^2).                           \tag{5.4}
\end{aligned}
\]

Thus choosing `p(H)Z(H)` constant removes the global edge-count term from
(5.4) exactly.  It does **not** identify the two different state-Palm laws
in (5.4).  For a deterministic current state they coincide as point masses,
and (5.4) reduces to `p(q_(t+1)-q_t)+O(theta^2)`, which is controlled by
Theorem 2.1.  This is the precise scope of predictable state-dependent
marking in the avoidance hierarchy.

## 6. Punctured scale

In a stopped directed punctured residual, every row has `4r` targets, with
`2r` in each shore.  Suppose the maximum target degrees are at most a fixed
multiple of their shore averages and the two averages are comparable.  If
`z` is either average scale and `n` is either current shore size, then

\[
 \Delta_C\le\max_F\sum_{u\in F}d(u)\le C_Krz,
 \qquad
 Z={nz\over2r}.                                     \tag{6.1}
\]

For fixed `m`, (2.4) therefore gives

\[
 \boxed{\bigl(q_1-q_0\bigr)_+
        \le C_{m,K}{r^3\over n}\,z.}               \tag{6.2}
\]

Until density `x>=r^(-alpha)`, the punctured target shores have

\[
 n\ge r^{-\alpha}\min\left\{{2r+1\choose r},
                              {2r+1\choose r-1}\right\}
   =\exp(\Omega(r)),                                \tag{6.3}
\]

so the right side of (6.2) is `z exp(-Omega(r))`, in particular `o(z)`.
At the Taylor-safe rate

\[
                         p_j\le {C\epsilon_j\over rz_j},     \tag{6.4}
\]

the linear term in (4.10) is at most

\[
                         C\epsilon_j{r^2\over n_j}.           \tag{6.5}
\]

The density clock gives `sum_j epsilon_j=O(r log r)`.  Hence, uniformly
through the stopped range,

\[
 \sum_j C\epsilon_j{r^2\over n_j}
 \le C{r^3\log r\over n_{\min}}=e^{-\Omega(r)}.     \tag{6.6}
\]

The quadratic term in (4.10) is the already isolated finite-microbite
remainder.  Thus survival selection cannot create a cumulatively relevant
increase of the mean `R_m` among descendants of any fixed current degree
bucket.

## 7. The exact remaining erosion-rebinning matrix

The qualification “fixed current degree bucket” is essential.  After
deleting `K`, a root of old degree `d` has new degree

\[
                         e=d-a_K(v).                 \tag{7.1}
\]

For old bucket `B_d`, define

\[
 Y_{d,e}=|\{(v,\gamma,K):v\in B_d,\ K\in\mathcal D(\gamma),
                         d-a_K(v)=e\}|,             \tag{7.2}
\]

and

\[
 W_{d,e}=\sum_{\substack{(v,\gamma,K)\text{ counted by }Y_{d,e}}}
       |\mathcal D(\gamma)\setminus\Gamma(K)|.      \tag{7.3}
\]

Every child carrier in `H_K` has a unique old carrier prefix.  Therefore,
in the uniform-singleton mixture,

\[
 \boxed{
 \Pr_{\rm child\ carrier}(D_{\rm old}=d,D_{\rm new}=e)
 \ \propto\ Y_{d,e},}                              \tag{7.4}
\]

and its degree-conditioned mean avoidance count is

\[
 \boxed{
 \mathbb E[R_m^{\rm child}\mid D_{\rm new}=e]
 ={\sum_dW_{d,e}\over\sum_dY_{d,e}}.}              \tag{7.5}
\]

On the other hand,

\[
 \sum_eY_{d,e}=X_1(B_d;H),\qquad
 \sum_eW_{d,e}=X_2(B_d;H).                          \tag{7.6}
\]

Theorem 2.1 controls the ratios of the two **row sums** in (7.6), but row
sums do not control the column ratios in (7.5).  This is the exact place
where realized erosion can sort descendant carriers and recreate a
degree regression even though survival selection inside every old bucket
is harmless.

There is an equivalent covariance form.  Under the uniform law on triples
`(v,gamma,K)` counted by `X_1`, put

\[
 E=d_v-a_K(v),\qquad
 Q=|\mathcal D(\gamma)\setminus\Gamma(K)|.          \tag{7.7}
\]

For every increasing test function `psi`, including the Gate-A
`varphi_c`, the newly created signed selection term is

\[
 \boxed{\operatorname {Cov}(Q,\psi(E)).}            \tag{7.8}
\]

Conditioning first on the old degree decomposes it as

\[
 \mathbb E\operatorname {Cov}(Q,\psi(E)\mid D_{\rm old})
 +\operatorname {Cov}
   (\mathbb E[Q\mid D_{\rm old}],
    \mathbb E[\psi(E)\mid D_{\rm old}]).           \tag{7.9}
\]

For one accepted singleton, the extension theorem controls the means in
the second term up to `o(z)`.  The first term is the corresponding
**erosion-sorting covariance**.  Neither assertion yet controls a complete
macro bite or its accumulation along the stopped history.

At the singleton level even that within-row term has a deterministic
`o(z)` bound.  This identifies the local mechanism, but it does not close
the macro-bite rebinning: a bite contains many accepted rows, and its child
columns are formed only after all of their erosions have been combined.

### Lemma 7.1 (within-old-bucket erosion sorting)

Fix one old bucket `B_d`.  Suppose `d<=Kz`, `Z>m Delta_C`, and let `psi`
be nondecreasing on the relevant integer degrees with

\[
                         |\psi(a)-\psi(b)|\le {L\over z}|a-b|. \tag{7.10a}
\]

Under the uniform triple law in (7.7),

\[
 \boxed{
 |\operatorname {Cov}(Q,\psi(E))|
 \le C_{m,K}L{\Delta_C^2\over Z-m\Delta_C}.}        \tag{7.10b}
\]

For the Gate-A weight

\[
 \varphi_c(d)={(d-c)_+^m\over(d)_m},\qquad
 c\ge(1+\delta)z,qquad d\le Kz,                   \tag{7.10c}
\]

(7.10a) holds with `L=C_(m,delta,K)` once `z` is large enough.

#### Proof

For each carrier `gamma` rooted at `v`,

\[
 \sum_{K\in\mathcal D(\gamma)}a_K(v)
 \le\sum_{K\in E(H)}a_K(v)
 =\sum_{F\ni v}|\Gamma(F)|\le d\Delta_C.           \tag{7.10d}
\]

Also `r(gamma)>=Z-m Delta_C`.  Averaging first over `K` and then over
carriers gives

\[
                         \mathbb E a_K(v)
 \le{d\Delta_C\over Z-m\Delta_C}.                  \tag{7.10e}
\]

Throughout the triple space,

\[
 Z-(m+1)\Delta_C\le Q\le Z,                        \tag{7.10f}
\]

so the range of `Q` is at most `(m+1)Delta_C`.  Since the old degree `d`
is fixed,

\[
\begin{aligned}
 |\operatorname {Cov}(Q,\psi(E))|
 &=|\operatorname {Cov}(Q,\psi(E)-\psi(d))|\\
 &\le(m+1)\Delta_C\,{L\over z}\,\mathbb E a_K(v),
\end{aligned}                                       \tag{7.10g}
\]

and (7.10b) follows from (7.10e) and `d<=Kz`.

For completeness, continuously extend `varphi_c` on `x>c`.  It is
nondecreasing, and

\[
 0\le\varphi_c'(x)
 \le {m(x-c)^{m-1}\over(x-m+1)^m}
 \le {C_{m,\delta,K}\over z}.                       \tag{7.10h}
\]

The last bound follows by maximizing
`u^(m-1)/(delta z+u)^m`.  Integrating (7.10h), including across the zero
part, proves (7.10a).  \(\square\)

There is also a useful covariance-stability formulation for this same
fixed bucket `B_d`.  Let `mu_0` be uniform on its old carriers and `mu_1`
uniform on their one-row extensions.  The marginal density of `mu_1` on carriers is
`r(gamma)/q_0`; it differs from one by at most
`m Delta_C/(Z-m Delta_C)`.  Equations (2.14), (7.10e), and the range
bounds therefore give

\[
 \left|
 \operatorname {Cov}_{\mu_1}(Q,\varphi_c(E))
 -\operatorname {Cov}_{\mu_0}(r(\gamma),\varphi_c(d))
 \right|
 \le C_{m,\delta,K}{\Delta_C^2\over Z-m\Delta_C}.  \tag{7.10i}
\]

The second covariance is zero because `B_d` is one fixed old degree
bucket.  Equation (7.10i) is not asserted for a union of buckets; there the
second covariance need not vanish, and its propagation includes the
old-bucket mixing term in (7.9).  Likewise, iterating a singleton estimate once per
accepted row would lose the exponentially small denominator in (7.10b),
because there are exponentially many accepted rows.  A successful Gate-A
proof must retain the macro-bite factor `p(H)` (or prove a contractive
stopped recurrence) rather than sum (7.10b) naively over accepted rows.

### 7.2 The predictable-rate macro-bite gate

Here is the exact statement which remains after the singleton reductions.
Let \(\nu\) be the current stopped state law, perform the isolated bite
with its predictable marking rate \(p_-(H)\), and write \(H^+\) for the
child state.  Let \(p_+(H^+)\) be the predictable rate to be used at the
next bite.  Tag a child ordered carrier \(\gamma\) by its old and new root
degrees

\[
 D_-=d_H(v),\qquad D_+=d_{H^+}(v),                  \tag{7.11}
\]

and put

\[
 Q^+(\gamma)=|\{G\in E(H^+):G\text{ is target-disjoint from }\gamma\}|.
                                                               \tag{7.12}
\]

Define the macro transition matrices

\[
 Y^+_{d,e}=\mathbb E\#\{\gamma:D_-=d,D_+=e\},       \tag{7.13}
\]

\[
 W^+_{d,e}=\mathbb E\sum_{\gamma:D_-=d,D_+=e}
                         p_+(H^+)Q^+(\gamma),        \tag{7.14}
\]

\[
 U^+_{d,e}=\mathbb E\sum_{\gamma:D_-=d,D_+=e}
                         p_+(H^+)|E(H^+)|.           \tag{7.15}
\]

The expectations include the old state law and the entire isolated bite;
deleted roots contribute no carriers.  Whenever the denominator is
positive, the next degree-conditioned scaled avoidance and hazard are

\[
 \mathcal R_+(e)={\sum_dW^+_{d,e}\over\sum_dY^+_{d,e}},
 \qquad
 \zeta_+(e)={\sum_d(U^+_{d,e}-W^+_{d,e})
                    \over\sum_dY^+_{d,e}}.          \tag{7.16}
\]

This is the exact predictable-rate analogue of (7.5).  If
\(p_+(H^+)|E(H^+)|\) is constant on the relevant size fibre, the \(U\)
column is common and only upward regression of \(\mathcal R_+\) matters.
Without that normalization, its column regression must be retained as a
separate global-size term, exactly as in (5.4).

Equivalently, let \(\mu_+\) be the child carrier-Palm law and set

\[
 \Pi=p_+(H^+),\qquad E=D_+,\qquad Q=Q^+(\gamma).     \tag{7.17}
\]

For an increasing Gate-A weight \(\varphi_c\), the avoidance contribution
to the next signed selection drift is exactly

\[
 \boxed{
 {\operatorname {Cov}_{\mu_+}(\Pi Q,\varphi_c(E))
       \over\mathbb E_{\mu_+}\varphi_c(E)}.}        \tag{7.18}
\]

The positive part is dangerous; the corresponding
\(\Pi|E(H^+)|\) covariance is added with the opposite sign when it is not
fibrewise constant.  In the pairwise notation of (G.120), an exact
sufficient stopped statement is

\[
 \boxed{
 \sum_{j<J}\mathfrak J_{j,c}
   \left(e\mapsto
    \mathbb E[\,p_j(H_j)(|E(H_j)|-Q_j)\mid D_j=e]\right)
 =o(\log r),}                                      \tag{7.19}
\]

uniformly over the relevant fixed terminal thresholds \(c\).  An
\(O(z_j)\) one-bite upward-regression bound gives a coefficient-level
version of the same gate; an \(o(z_j)\) bound gives (7.19) directly through
the density clock.

Theorems 2.1--2.2 and Lemma 7.1 prove the singleton row-sum and
within-row estimates underlying (7.13)--(7.18).  What is not proved is a
macro-bite theorem transporting those bounds to the fully formed columns
of \(Y^+,W^+,U^+\), with the stopped state-Palm weighting and without
summing once per accepted row.  This is the precise remaining
**predictable-rate erosion-rebinning gate**.

The singleton tangent of the remaining macro mixing statistic is
bounded-order and has a direct boundary interpretation:

\[
 a_K(v)=|\mathcal S_v\cap\Gamma(K)|,
 \qquad
 Q=r(\gamma)-|\mathcal D(\gamma)\cap\Gamma(K)|.    \tag{7.10}
\]

Thus (7.8) is a joint flower consisting of one root star, the fixed
`m`-carrier, one external row `K`, and one further extension row.  The
existing one-carrier boundary-polymer estimates control its unconditioned
overlap moments, but do not presently control them after decorating by the
realized erosion `a_K(v)` or after sorting into the columns (7.1).

Accordingly, the remaining Gate-A regression input is the macro statement
(7.19), or the stronger columnwise version (7.16).  No further
carrier-survival comparison inside one fixed old degree bucket is needed;
(4.10)--(6.6) make its positive extension-curvature contribution summably
negligible.  The macro erosion/rebinning and state-Palm transfer are still
open and are not implied by the singleton estimates.

The companion checker

`scratch/verify_gate_a_avoidance_extension_hierarchy_20260822.py`

enumerates finite simple hypergraphs, carriers, extensions, singleton
deletions, and isolated-mark bites.  It checks (1.6), (2.3)--(2.5), (2.9),
(3.4)--(3.5), (4.2)--(4.8), the row/column identities (7.2)--(7.6), and
the Lipschitz erosion-covariance bound (7.10b).
It is a regression test only; all implications are proved above.
