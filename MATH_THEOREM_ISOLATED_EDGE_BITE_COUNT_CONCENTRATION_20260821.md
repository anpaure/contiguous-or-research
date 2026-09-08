# Isolated-edge bite counts concentrate automatically under empirical regularity

**Date:** 2026-08-21  
**Status:** analytic conditional theorem; preservation of the hypotheses is not
claimed

## 1. A conflict-graph variance lemma

Let `H` be a finite simple hypergraph with `Z` edges, and let `G` be its
conflict graph: the vertices of `G` are the edges of `H`, and two vertices
are adjacent when the corresponding hyperedges meet.  Independently mark
each vertex of `G` with probability `p`.  Let `A` be the number of marked
vertices having no marked neighbour, let `N(e)` be the neighbourhood of
`e` in `G`, and put

\[
 g_e=|N(e)|,\qquad \Delta=\max_e g_e,\qquad
 q_e=p(1-p)^{g_e},\qquad \mu=\mathbb EA=\sum_e q_e.       \tag{1.1}
\]

### Lemma 1.1

If `p<=1/2` and `p\Delta<=K`, then

\[
 \boxed{\qquad
 \operatorname {Var}A
   \le \mu+C_Kp^3Z\Delta^2,
 \qquad
 {\operatorname {Var}A\over\mu^2}
   \le C_K\left({1\over Zp}+{p\Delta^2\over Z}\right).
 \qquad}                                                \tag{1.2}
\]

Here `C_K` depends only on `K`.

#### Proof

Write `I_e` for the indicator counted by `A`.  If `e` and `f` are
adjacent in `G`, they cannot both be counted, and hence their covariance is
nonpositive.  For every pair put

\[
                         c_{ef}=|N(e)\cap N(f)|.         \tag{1.3}
\]

If `e` and `f` are distinct and nonadjacent, the exact joint probability
and covariance are

\[
 \mathbb E(I_eI_f)
   =p^2(1-p)^{g_e+g_f-c_{ef}},
 \qquad
 \operatorname {Cov}(I_e,I_f)
   =q_eq_f\bigl((1-p)^{-c_{ef}}-1\bigr).                \tag{1.4}
\]

Since `c_{ef}<=Delta`, `p<=1/2`, and `p Delta<=K`,

\[
 (1-p)^{-c_{ef}}-1
 \le 2e^{2K}p c_{ef}.                                  \tag{1.5}
\]

Also

\[
 \sum_{e,f}c_{ef}
   =\sum_h |N(h)|^2
   \le Z\Delta^2.                                      \tag{1.6}
\]

Using `q_e q_f<=p^2`, discarding the negative adjacent covariances, and
applying (1.5)--(1.6) gives the first inequality in (1.2).  Finally,

\[
 \mu\ge Zp(1-p)^\Delta\ge Zp e^{-2K},                 \tag{1.7}
\]

so division by `mu^2` gives the second inequality.  `square`

## 2. Application to the punctured isolated-edge nibble

Consider a residual directed punctured-configuration hypergraph `H_j`.
Let `Z_j` be its number of configurations, let `M_j,L_j` be its middle
and lower target shores, and set

\[
 \bar d_j^M={2rZ_j\over|M_j|},\qquad
 \bar d_j^L={2rZ_j\over|L_j|}.                          \tag{2.1}
\]

For a surviving configuration `e`, put `t_F(e)=|F\cap e|` and define its
duplicate excess by

\[
 \mathfrak E_j(e)
   =\sum_{F:t_F(e)>0}(t_F(e)-1).                        \tag{2.2}
\]

Suppose, uniformly over the residual state under consideration, that

1. every target degree is `(1+o(1))` times the appropriate average in
   (2.1);
2. every surviving configuration `e` has duplicate excess
   `\mathfrak E_j(e)=o(r\bar d_j^M)`; and
3. `\bar d_j^M=\exp(\Omega(r\log r))` and
   `\bar d_j^L/\bar d_j^M=1+o(1)`.

Mark each surviving configuration independently with

\[
                         p_j={\gamma\over r\bar d_j^M}, \tag{2.3}
\]

where `\gamma>0` is fixed, and accept precisely the isolated marked
configurations.  Let `A_j` be the number accepted.

### Theorem 2.1

Conditionally on `H_j`,

\[
 \mathbb E(A_j\mid H_j)
   =(1+o(1))Z_jp_j e^{-4\gamma},                        \tag{2.4}
\]

and

\[
 {\operatorname {Var}(A_j\mid H_j)
       \over \mathbb E(A_j\mid H_j)^2}
       =O_\gamma\left({r^2\over|M_j|}\right).          \tag{2.5}
\]

In particular, if `|M_j|=\exp(\Omega(r))`, then for every fixed `B>0`,

\[
 \Pr\left(\left.
   |A_j-\mathbb E(A_j\mid H_j)|
       >r^{-B}\mathbb E(A_j\mid H_j)\ \right|\ H_j\right)
       =\exp(-\Omega(r)).                               \tag{2.6}
\]

#### Proof

For a surviving configuration `e`, its degree in the conflict graph is

\[
 g_e=\sum_{v\in e}d_j(v)-\mathfrak E_j(e)-1
     =(4+o(1))r\bar d_j^M.                              \tag{2.7}
\]

Thus `\Delta<=5r\bar d_j^M` for all sufficiently large `r`, while
`p_j\Delta<=5\gamma`.  The exponential lower bound on `\bar d_j^M` also
gives `p_j=o(1)`.  Equation (2.4) follows from
`p_j(1-p_j)^{g_e}=p_j\exp(-4\gamma+o(1))`, uniformly in `e`.

Apply Lemma 1.1 with `K=5\gamma`.  The identity

\[
                         Z_j={|M_j|\bar d_j^M\over2r}   \tag{2.8}
\]

gives

\[
 {1\over Z_jp_j}={2r^2\over\gamma|M_j|},
 \qquad
 {p_j\Delta^2\over Z_j}
       =O_\gamma\left({r^2\over|M_j|}\right).          \tag{2.9}
\]

This proves (2.5), and Chebyshev's inequality proves (2.6).  `square`

### Corollary 2.2 (uniform polynomial-round conclusion)

Run fresh independent marking rounds along any adaptive history, and let
`tau` be the first round at which one of the three hypotheses above fails
or `|M_j|<\exp(c r)`, for some fixed `c>0`.  For every fixed `C`, with
probability `1-\exp(-\Omega(r))`,

\[
       A_j=(1+o(1))\mathbb E(A_j\mid H_j)              \tag{2.10}
\]

simultaneously in every round `j<min(tau,r^C)`.  In particular, the same
conclusion holds through `r^C` rounds whenever the hypotheses persist.

#### Proof

Take any fixed `B>0` in (2.6), condition successively on the adaptive
history, and union-bound the resulting `r^C\exp(-\Omega(r))` conditional
failure probabilities.  `square`

## 3. Consequence and exact remaining gate

For the renormalized quenched gate in
`MATH_AUDIT_PUNCTURED_PURGE_CLUSTER_DRIFT_AND_RENORMALIZED_GATE_20260821.md`,
the empirical degree floor makes hypothesis 3 valid down to
`x>=r^{-alpha}` for every fixed `alpha<1/2`, while the exact shore relation
gives `|M_j|=\exp(\Omega(r))`.  Therefore its accepted-edge-count
concentration condition is a theorem, not a separate gate.

What remains unproved is preservation, under the adaptive nibble history,
of target-degree regularity, the uniform duplicate-excess bound, and the
empirical degree floor.  This note makes no such trajectory claim.
