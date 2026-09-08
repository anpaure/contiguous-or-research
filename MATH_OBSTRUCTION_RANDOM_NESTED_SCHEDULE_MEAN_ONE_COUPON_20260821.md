# Random nested schedules spread the rank loads but leave a mean-one labelled coupon barrier

**Status (2026-08-21).**  Every assertion below is proved, conditional on
the one-copy tight-cycle factors explicitly invoked.  A uniformly random
nested permutation schedule makes every individual central payload weight
small.  This removes the particular one/two-macroscopic-bank mechanism of
the inverse-step-two affine schedule.  It does **not** give labelled target
coverage under independent rank-by-rank factor conjugations.

If

\[
 q\longrightarrow\infty,
 \qquad q=o\!\left(\sqrt{b/\log b}\right),          \tag{0.1}
\]

then, with probability `1-o(1)` over the random nested schedule, every
individual payload source has mean target load `o(1)`, while the sum of all
payload means is at most `1+o(1)`.  Independence between payload-rank
conjugations and Markov's inequality then give

\[
 \boxed{
 \mathbb E_{\rm factors} Z_q
 \ge(e^{-1}-o(1)){2b\choose b+q}.}                 \tag{0.2}
\]

In particular (0.2) applies to every `q=log^C b` with fixed `C>0`.
Thus disappearance of marginal zero rows and columns is not enough: the
joint labelled occurrences become a mean-one coupon experiment and retain
an asymptotic `e^(-1)` miss fraction.

The theorem is scoped to mutually independent rank-and-side conjugations.
It does not obstruct correlated rank banks, a matched full-orbit selector,
or a deterministic construction which deliberately anti-aligns the target
holes.

## 1. Nested permutation schedules and exact source means

Let `b` be an odd prime and write

\[
 C_j={b\choose j},\qquad
 M_q={2b\choose b+q}.
\]

Let `Z_q` denote the number of missed labelled rank-`(b+q)` targets.

Choose a permutation

\[
 R:\mathbb Z_b\longrightarrow\{0,1,\ldots,b-1\}
\]

and define the nested phase sets

\[
 P_r=\{x:R(x)<r\},\qquad 0\le r\le b.             \tag{1.1}
\]

For a phase `p`, let

\[
 J_p^q=\{p+1,\ldots,p+q\}\pmod b,
 \qquad
 \phi_p^q(r)=r+|P_r\cap J_p^q|.                   \tag{1.2}
\]

Passing from `r` to `r+1` inserts one phase, so

\[
 \phi_p^q(r+1)-\phi_p^q(r)\in\{1,2\}.             \tag{1.3}
\]

Thus a fixed phase contributes to at most one payload rank for a prescribed
upper split `s`.  Put

\[
 m_r(q,s)=\#\{p:\phi_p^q(r)=s\}.                  \tag{1.4}
\]

Fix a rank-`(b+q)` target `V`, let

\[
 s=|V\cap A|,
 \qquad t=s-q,
 \qquad P_{q,s}^{\rm tar}=C_sC_t,                 \tag{1.5}
\]

and conditionally fix one-copy tight-cycle factors at every rank
`r=s-z`, `0<=z<=q`.  Independently conjugate the factors at distinct
rank-and-side pairs by uniform label permutations.  Let `N_r(V)` be the
number of occurrences of `V` supplied by payload `r`, across all its factor
order pairs, contributing phases, and counter points.

### Lemma 1.1 (exact independent source means)

The random variables `(N_r(V))_r` are mutually independent and

\[
 \boxed{
 \lambda_r:=\mathbb EN_r(V)
 ={m_r(q,s)\over b}
  {C_r^2\over C_sC_t}.}                            \tag{1.6}
\]

Consequently

\[
 \Lambda_{q,s}:=\sum_r\lambda_r
 ={1\over bC_sC_t}\sum_r m_r(q,s)C_r^2.           \tag{1.7}
\]

#### Proof

The rank-`r` product bank contains `C_r^2/b^2` order pairs.  One phase in
one order pair contains `b` counter points, so the source has exactly
`m_rC_r^2/b` occurrences in the profile.  Uniform label conjugation is
transitive on its `C_sC_t` targets, which proves (1.6).  The variable
`N_r(V)` uses only the rank-and-side conjugations `(r,A)` and `(r,B)`.
Those coordinates are disjoint at different `r`, proving independence.
Summing (1.6) gives (1.7).  \(\square\)

This calculation includes every repeated longer/shorter window inside one
factor.  Such repetitions can increase the variance of `N_r`, but cannot
invalidate its mean or the Markov bound used below.

## 2. Every central nested schedule has total mean at most one

Write

\[
 s={b+q\over2}+x.
\]

Let `L=L(b)->infinity` satisfy

\[
 {qL\over\sqrt b}\longrightarrow0,
 \qquad {L^4\over b}\longrightarrow0.              \tag{2.1}
\]

For example, when `q=o(sqrt b)`, one may take
`L=min((sqrt(b)/q)^(1/2),b^(1/16))`.  Uniformly for
`|x|<=L sqrt(b)` and every candidate
`r=s-z`, `0<=z<=q`, the central binomial expansion gives

\[
 {C_r^2\over C_sC_t}=1+o(1).                       \tag{2.2}
\]

Indeed, putting `delta=z-q/2`, the logarithm of the ratio in (2.2) is

\[
 {q^2+8x\delta-4\delta^2\over b}+o(1),             \tag{2.3}
\]

uniformly on this range, and (2.1) makes it `o(1)`.

On the other hand, strict increase (1.3) gives the deterministic bound

\[
 \sum_r m_r(q,s)\le b.                             \tag{2.4}
\]

Equations (1.7), (2.2), and (2.4) prove

### Lemma 2.1 (mean-one ceiling)

For every nested schedule, uniformly on the central window above,

\[
 \boxed{\Lambda_{q,s}\le1+o(1).}                  \tag{2.5}
\]

No lower bound is needed.  Phase holes only reduce `Lambda` and strengthen
the eventual miss estimate.

## 3. A random permutation makes every individual source small

Now take `R` uniformly from all `b!` permutations.  For fixed `r,z`, define

\[
 M_{r,z}=\#\{p:|P_r\cap J_p^q|=z\}.               \tag{3.1}
\]

Then `m_r(q,s)=M_(r,s-r)`.  At one fixed phase, `P_r` is a uniform
`r`-subset of `Z_b`, and therefore

\[
 {\mathbb EM_{r,z}\over b}
 ={ {r\choose z}{b-r\choose q-z}\over {b\choose q}}.           \tag{3.2}
\]

Uniformly for `r in [b/4,3b/4]`, the largest hypergeometric atom in (3.2)
is `O(q^(-1/2))`.  This follows directly from the adjacent-probability
ratio

\[
 {\Pr(Z=z+1)\over\Pr(Z=z)}
 ={(r-z)(q-z)\over(z+1)(b-r-q+z+1)}                \tag{3.3}
\]

and Stirling's bounds in a `Theta(sqrt q)` neighborhood of its mode; outside
that neighborhood the ratio test only decreases the mass.

Transposing two values of `R` changes membership in `P_r` at at most two
phase positions.  Only cyclic `q`-windows containing one of those positions
can change their indicator in (3.1), so

\[
 |M_{r,z}(R)-M_{r,z}(R')|\le2q                    \tag{3.4}
\]

under one transposition.  The permutation exposure martingale, coupling two
completions by one transposition at each reveal, therefore gives

\[
 \Pr\{|M_{r,z}-\mathbb EM_{r,z}|\ge u\}
 \le2\exp\left\{-{u^2\over Cbq^2}\right\}         \tag{3.5}
\]

for an absolute constant `C`.

Take `u=Kq sqrt(b log b)` with a sufficiently large fixed `K`, and union
bound over all `r,z`.  With probability `1-o(1)`,

\[
 \boxed{
 \max_{b/4\le r\le3b/4}\max_{0\le z\le q}
 {M_{r,z}\over b}
 \le {C_1\over\sqrt q}
       +C_2q\sqrt{\log b\over b}=:\varepsilon_b.} \tag{3.6}
\]

Under (0.1), `epsilon_b=o(1)`.  Combining (1.6), (2.2), and (3.6) yields,
uniformly on the central split window,

\[
 \boxed{\max_r\lambda_r=o(1)}.                    \tag{3.7}
\]

The schedule has therefore eliminated every macroscopic single-rank
coupon.  The next section shows why this is still insufficient.

## 4. The mean-one coupon lower bound

Condition on any schedule for which (2.5) and (3.7) hold.  Markov's
inequality and Lemma 1.1 give, for every central target `V`,

\[
 \begin{aligned}
 \Pr(V\text{ is uncovered})
 &=\prod_r\Pr(N_r(V)=0)\\
 &\ge\prod_r(1-\lambda_r).                         \tag{4.1}
 \end{aligned}
\]

Since

\[
 \sum_r\lambda_r^2
 \le(\max_r\lambda_r)\Lambda_{q,s}=o(1),          \tag{4.2}
\]

we obtain

\[
 \log\prod_r(1-\lambda_r)
 =-\Lambda_{q,s}-o(1)\ge-1-o(1).                  \tag{4.3}
\]

Thus every target in the central split window is missed with probability at
least `e^(-1)-o(1)` over the independent factor conjugations.

For a uniform rank-`(b+q)` target, its split coordinate has variance
`Theta(b)`.  The choice `L->infinity` makes the central window contain a
`1-o(1)` fraction of all `M_q` targets.  Summing (4.3) proves (0.2).

### Theorem 4.1 (random nested schedule coupon obstruction)

Under (0.1), with probability `1-o(1)` over the uniform nested permutation
schedule,

\[
 \boxed{
 \mathbb E_{\rm factors} Z_q
 \ge(e^{-1}-o(1))M_q.}                             \tag{4.4}
\]

The `o(1)` is uniform for any prescribed sequence of offsets satisfying
(0.1).  A union bound also makes the conclusion simultaneous over any
polynomial-size list of such offsets after increasing the constant in
(3.6).

### Corollary 4.2 (aggregate low/mesoscopic band obstruction)

Let

\[
 Q_0\longrightarrow\infty,
 \qquad Q_0\le Q_1=o\!\left(\sqrt{b/\log b}\right). \tag{4.5}
\]

Put `W_b=binom(2b,b)`.  With probability `1-o(1)` over the same random
schedule,

\[
 \boxed{
 \mathbb E_{\rm factors}\sum_{q=Q_0}^{Q_1}Z_q
 \ge(e^{-1}-o(1))\sum_{q=Q_0}^{Q_1}M_q
 =(e^{-1}-o(1))(Q_1-Q_0+1)W_b,}                   \tag{4.6}
\]

The last equality uses `M_q/W_b=1-o(1)` uniformly for `q<=Q_1`.  No independence between
different offsets is needed, because expectations are simply summed.

The mechanism is exact.  The schedule turns the two large endpoint coupons
of the clustered word into many small independent coupons, but it does not
raise their total mean above one.  In the small-coupon limit the old
one-quarter endpoint bound converges to the stronger `e^(-1)` miss bound.

## 5. Scope and audit

This theorem does not say that random nested schedules are geometrically
useless.  Their marginal row and column supports can be much better spread
than those of the half-step affine schedule.  It says that independent
rank-by-rank label conjugations cannot turn that marginal improvement into
joint target coverage while the total occurrence mean remains `1+o(1)`.

A possible escape must violate at least one hypothesis used in (4.1): it
must correlate the rank banks, match the source occurrences to targets
instead of independently conjugating them, or move to offsets large enough
that `W_b/M_q` supplies a genuinely growing mean.  The theorem makes no
claim in the top regime `q` comparable to `sqrt(b log b)`.

The H100 checker
`scratch/audit_random_nested_schedule_mean_one_coupon_20260821.py`
performs the following finite checks.

- For every permutation through `b=7`, and for every permutation at
  `b=8` with `q<=3`, it verifies the exact histogram identity (3.2),
  strict phase injection, and (2.4).
- It checks the exact binomial-ratio exponent (2.3) against factorial
  formulas throughout small central cases.
- For seeded random schedules up to `b=4001`, it records the largest window
  histogram and verifies the two terms in (3.6).
- It audits the product inequality in (4.1)--(4.3) on every finite
  histogram generated in the exhaustive cases.

These computations check the indexing and limiting scales.  The proof is
independent of them.
