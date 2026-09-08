# Pair-spread exact factors imply generic multidepth centered energy

Date: 2026-07-25

Method: pure mathematics only.

## 1. Catalogue normalization

Let `n=2m+1`, `W=binom(n,m)`, and let `R_m` be the catalogue of geometric
wreath rows (cyclic orders modulo rotation and reversal).  Put

\[
 T={W\over n},qquad D={m!(m+1)!\over2}.
\]

Every exact factor contains `T` rows, the catalogue has `TD` rows, and
every middle owner belongs to exactly `D` catalogue rows.

At depth `q`, put `N_q=binom(n,m-q)` and `lambda_q=W/N_q`.  Every target
`S` belongs to exactly

\[
                         d_q=\lambda_qD                       \tag{1.1}
\]

catalogue rows, by double counting row--target incidences.

## 2. Pair-spread hypothesis

Let `bold F` be a random exact middle factor.  Assume that, for some
constant `K`, every two distinct catalogue rows satisfy

\[
 \Pr[C,C'\in\boldsymbol F]\le {K\over D^2}.                  \tag{2.1}
\]

Only pairs which are simultaneously incident with an audited lower target
are actually needed below.  Coordinate symmetrization of any distribution
on exact factors makes every one-row marginal exactly `1/D`; condition
(2.1), however, is genuinely additional and is not supplied by
edge-transitivity alone.

## 3. Exact second-moment bridge

For one factor `F`, let `mu_q^F(S)` be its depth-`q` load and put

\[
 E_q(F)=\sum_S(\mu_q^F(S)-\lambda_q)^2.                       \tag{3.1}
\]

### Theorem 3.1

Under (2.1), for every depth `q`,

\[
 \boxed{
 \mathbb E E_q(\boldsymbol F)
 \le\left[1+(K-1)\lambda_q-{K\over D}\right]W.}             \tag{3.2}
\]

In particular, for every fixed `A`, uniformly for `q<=A sqrt(m)`,

\[
                         \mathbb E E_q=O_{A,K}(W).             \tag{3.3}
\]

#### Proof

Write

\[
 P_q(F)=\sum_S\binom{\mu_q^F(S)}2.
\]

For every exact factor,

\[
 E_q(F)=2P_q(F)-(\lambda_q-1)W.                               \tag{3.4}
\]

For a fixed target `S`, its incident catalogue has size `d_q`.  Hence
(2.1) gives

\[
 \begin{aligned}
 \mathbb E P_q
 &\le {K\over D^2}N_q\binom{\lambda_qD}{2}\\
 &={K\over2}\left(\lambda_qW-{W\over D}\right).
 \end{aligned}                                                \tag{3.5}
\]

Substitution in (3.4) proves (3.2). \(\square\)

## 4. One common factor over a Gaussian window

Let `H=ceil(A sqrt(m))`.  Summing (3.2) and using
`lambda_q<=exp(A^2+o_A(1))` yields

\[
 \mathbb E\sum_{q\le H}E_q(\boldsymbol F)
 =O_{A,K}(\sqrt m\,W).                                       \tag{4.1}
\]

Therefore some exact factor `F` satisfies (4.1).  In the notation of the
prime-cycle aggregate theorem,

\[
                         \mathcal K={1\over W}\sum_{q\le H}E_q
                         =O_{A,K}(\sqrt m).                    \tag{4.2}
\]

The one-cycle optimization then gives

\[
 \sum_{q\le H}\mathfrak D_{\sigma,q}
 \le C W\mathcal K^{3/5}n^{-2/5}
 =O_{A,K}(Wm^{-1/10})=o(W).                                  \tag{4.3}
\]

Thus constant pair spread is already strong enough for the entire fixed
Gaussian window; no union bound producing a pointwise energy estimate is
needed.

## 5. Exact remaining interfaces

The theorem does not manufacture the distribution in (2.1), and a
near-matching distribution is not enough by itself.  A longitudinal
construction must supply both:

1. extendibility or absorption into exact middle factors; and
2. the pair-inclusion estimate (2.1), or merely its aggregate version over
   pairs of rows sharing audited lower targets.

After (4.3), the same legal prime-cycle lift/quotient-cover gate remains as
in the orbit-smoothing theorem.  The value of the bridge is that the
pre-smoothing matching stage is reduced to a natural second-order
pseudorandomness statement at the random scale.

