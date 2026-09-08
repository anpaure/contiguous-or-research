# Average scale and maximum degree suffice for the punctured nibble

**Date:** 2026-08-21  
**Status:** analytic conditional theorem; preservation of the maximum-degree
hypothesis is not claimed

## 1. Residual shores and the weak gate

Let `H_j` be a residual directed punctured-configuration hypergraph.  Its
edges are configurations, each containing `2r` middle targets and `2r`
lower targets.  Write

\[
 Z_j=|E(H_j)|,
 \qquad
 \bar d_j^M={2rZ_j\over |M_j|},
 \qquad
 \bar d_j^L={2rZ_j\over |L_j|}.                         \tag{1.1}
\]

Initially

\[
 {|M_0|\over|L_0|}={r+2\over r}.                       \tag{1.2}
\]

Every accepted configuration removes exactly `2r` targets from each
shore.  Consequently, if `x_j=|L_j|/|L_0|`, then

\[
 y_j={|M_j|\over|M_0|}={rx_j+2\over r+2},
 \qquad
 {\bar d_j^L\over\bar d_j^M}
 ={ |M_j|\over |L_j|}=1+{2\over r x_j}.                 \tag{1.3}
\]

Fix constants `K>=1`, `gamma>0`, and `0<alpha<1`.  The weak gate used in
this note consists only of the following two conditions, required while
`x_j>=r^{-alpha}`:

\[
 \max_{v\in M_j}d_j(v)\le K\bar d_j^M,
 \qquad
 \max_{v\in L_j}d_j(v)\le K\bar d_j^L,                 \tag{1.4}
\]

and, for some fixed `c>0`,

\[
                         \bar d_j^M\ge e^{c r\log r}.   \tag{1.5}
\]

No lower bound on an individual target degree and no duplicate-excess
condition are assumed.

## 2. Every good state supplies a macroscopic bite

In a good residual state, mark each configuration independently with

\[
                         p_j={\gamma\over r\bar d_j^M}, \tag{2.1}
\]

and accept a marked configuration exactly when it meets no other marked
configuration.  Let `A_j` be the number accepted.

### Lemma 2.1 (conditional bite bounds)

There are constants `a=a(K,gamma)>0` and `b=b(gamma)>0` such that,
conditionally on every state satisfying (1.3)--(1.5),

\[
 \Pr\left(
   {aZ_jp_j}\le A_j\le {bZ_jp_j}
   \ \middle|\ H_j\right)=1-e^{-\Omega(r)}.             \tag{2.2}
\]

The constant in `\Omega(r)` is uniform over all such states with
`x_j>=r^{-alpha}`.

#### Proof

Let `G_j` be the conflict graph on the configurations of `H_j`, and write
`g_e` for the degree of `e` in `G_j`.  From (1.3)--(1.4),

\[
 \Delta(G_j)
 \le 2rK\bar d_j^M+2rK\bar d_j^L
 \le (4K+o(1))r\bar d_j^M.                             \tag{2.3}
\]

Moreover,

\[
 \begin{aligned}
 {1\over Z_j}\sum_e g_e
 &\le {1\over Z_j}\sum_v d_j(v)(d_j(v)-1)\\
 &\le {1\over Z_j}\left(
       K\bar d_j^M\sum_{v\in M_j}d_j(v)
      +K\bar d_j^L\sum_{v\in L_j}d_j(v)\right)\\
 &=2Kr(\bar d_j^M+\bar d_j^L)
  \le(4K+o(1))r\bar d_j^M.                             \tag{2.4}
 \end{aligned}
\]

The first inequality merely overcounts a conflicting configuration once
for every shared target; duplicate overlaps can only improve it.

Put `\mu_j=\mathbb E(A_j\mid H_j)`.  Since
`u\mapsto(1-p_j)^u` is convex, Jensen's inequality and (2.4) give

\[
 \begin{aligned}
 {\mu_j\over Z_jp_j}
 &= {1\over Z_j}\sum_e(1-p_j)^{g_e}\\
 &\ge (1-p_j)^{Z_j^{-1}\sum_e g_e}
 \ge \exp(-(4K+o(1))\gamma).                           \tag{2.5}
 \end{aligned}
\]

Here (1.5) implies `p_j=o(1)`.  The conflict-graph covariance theorem in
`MATH_THEOREM_ISOLATED_EDGE_BITE_COUNT_CONCENTRATION_20260821.md`, applied
using (2.3), gives

\[
 {\operatorname {Var}(A_j\mid H_j)\over\mu_j^2}
 \le C_{K,\gamma}\left(
      {1\over Z_jp_j}+{p_j\Delta(G_j)^2\over Z_j}\right)
 =O_{K,\gamma}\left({r^2\over|M_j|}\right).            \tag{2.6}
\]

For `x_j>=r^{-alpha}`, (1.3) and the central-binomial estimate give
`|M_j|=\exp(\Omega(r))`.  Thus Chebyshev's inequality and (2.5) imply

\[
                         A_j\ge {1\over2}e^{-5K\gamma}Z_jp_j  \tag{2.7}
\]

except with probability `e^{-\Omega(r)}`.  On the other hand, `A_j` is at
most the total number of marked configurations.  A binomial Chernoff
bound, using

\[
                         Z_jp_j={\gamma|M_j|\over2r^2}, \tag{2.8}
\]

gives `A_j<=2Z_jp_j` with a still smaller failure probability.  This
proves (2.2), for example with

\[
                         a={1\over2}e^{-5K\gamma},
 \qquad b=2.                                           \tag{2.9}
\]

`square`

## 3. Conditional descent theorem

### Theorem 3.1

Start from the full directed punctured-configuration hypergraph and run
the isolated-edge nibble (2.1), deleting the targets of every accepted
configuration after each round.  Stop on first reaching
`x_j<=r^{-alpha}`, or on first failure of (1.4) or (1.5).

With probability `1-e^{-\Omega(r)}`, either a regularity hypothesis fails,
or the accepted configurations form a matching that reaches
`x_j<=r^{-alpha}` within `O_{K,gamma}(r log r)` rounds.  If (1.4)--(1.5)
persist until the density threshold, the latter alternative holds and the
matching leaves

\[
 r^{-\alpha}(1+O_{K,\gamma}(r^{-1}))
 \quad\hbox{of the lower shore},
 \qquad o(1)\quad\hbox{of the middle shore}.            \tag{3.1}
\]

#### Proof

Accepted configurations in one round are pairwise disjoint by definition,
and deleting their targets makes accepted configurations from different
rounds disjoint as well.

From (1.1), (2.1), and (2.2), every good round removes a fraction between

\[
 {a\gamma\over r}
 \quad\hbox{and}\quad
 {b\gamma\over r}                                     \tag{3.2}
\]

of the residual middle shore.  By (1.3), the lower-shore fraction differs
by the factor `1+2/(rx_j)=1+o(1)`.  A conditional union bound over
`O(r log r)` stopped rounds makes (3.2) simultaneous with probability
`1-e^{-\Omega(r)}`.  Repeated multiplication by
`1-(a\gamma+o(1))/r` reaches `r^{-\alpha}` within
`O_{K,\gamma}(r\log r)` rounds.  The upper bound in (3.2) shows that the
one-round overshoot is a factor `1+O_{K,gamma}(1/r)`.

Finally, the exact relation (1.3) gives

\[
                         y_j={rx_j+2\over r+2}=o(1),    \tag{3.3}
\]

which proves (3.1).  `square`

## 4. The empirical floor bootstraps from the maximum-degree cap

The exponential floor in Theorem 3.1 need not be assumed separately if a
sufficiently small fixed target exponent is enough.

### Corollary 4.1 (one-gate bootstrap)

Fix `K>=1`, and set

\[
                         \gamma={1\over96K},
 \qquad 0<\alpha\le {1\over256K}.                      \tag{4.1}
\]

Run the nibble from the full directed punctured-configuration hypergraph,
but stop if the one-sided maximum-degree cap (1.4) fails.  With probability
`1-e^{-\Omega(r)}`, either that cap fails, or the process reaches
`x_j<=r^{-\alpha}` in `O_K(r\log r)` rounds and produces the matching leave
in (3.1).  Along the latter trajectory,

\[
                         \bar d_j^M\ge e^{r\log r}      \tag{4.2}
\]

for all sufficiently large `r`.  Thus the empirical floor is automatic;
the only remaining conditional gate is persistence of (1.4).

#### Proof

Suppose `x_j>=r^{-\alpha}` and (1.4) holds.  By (1.3), for all sufficiently
large `r`,

\[
                         1\le {\bar d_j^L\over\bar d_j^M}\le2. \tag{4.3}
\]

Every configuration has `2r` targets on each shore.  Therefore its closed
conflict neighbourhood satisfies

\[
 \begin{aligned}
 |\Gamma_j(e)|
 &\le\sum_{v\in e}d_j(v)\\
 &\le2rK\bar d_j^M+2rK\bar d_j^L
 \le6Kr\bar d_j^M.                                    \tag{4.4}
 \end{aligned}
\]

This is the required `4r`-incidence count; a configuration meeting `e` in
several targets is only overcounted.

We prove the floor and the bite estimates together by induction.  The full
hypergraph has

\[
 Z_0={|M_0|D_M\over2r}=(2r+1)!,
 \qquad \log Z_0=(2+o(1))r\log r.                     \tag{4.5}
\]

Assume the preceding good rounds satisfy the bounds below.  The resulting
lower bound on `Z_j`, proved momentarily, gives
`\bar d_j^M>=e^{r\log r}` and hence `p_j=o(1)`.  Equations (2.4), (4.1),
and (4.3) then give

\[
 {\mathbb E(A_j\mid H_j)\over Z_jp_j}
 \ge (1-p_j)^{6Kr\bar d_j^M}
 \ge e^{-12K\gamma}=e^{-1/8}.                         \tag{4.6}
\]

The covariance bound (2.6) and the binomial marked-edge bound consequently
give, except with conditional probability `e^{-\Omega(r)}`,

\[
                         {1\over2}Z_jp_j\le A_j\le2Z_jp_j.     \tag{4.7}
\]

In particular, every good round removes between `\gamma/(2r)` and
`2\gamma/r` of the middle shore, and, by (4.3), between `\gamma/(2r)` and
`4\gamma/r` of the lower shore.  Thus, if the cap persists, the density
threshold is reached within

\[
                         J_*=\left\lceil{2\alpha r\log r\over\gamma}\right\rceil
                         =O_K(r\log r)                 \tag{4.8}
\]

rounds.

It remains to justify the simultaneous floor used above.  Deleting the
targets of the `A_j` accepted configurations removes at most the union of
their closed conflict neighbourhoods.  Equations (2.1), (4.4), and the
upper bound in (4.7) give

\[
 \begin{aligned}
 Z_j-Z_{j+1}
 &\le A_j\,6Kr\bar d_j^M\\
 &\le2Z_j{\gamma\over r\bar d_j^M}\,6Kr\bar d_j^M
 =12K\gamma Z_j={1\over8}Z_j.                         \tag{4.9}
 \end{aligned}
\]

Hence, for every `j<=J_*`,

\[
 \log Z_j
 \ge\log Z_0+j\log(7/8)
 \ge(2-o(1))r\log r-{J_*\over7}.                      \tag{4.10}
\]

Here `-\log(7/8)<1/7`.  From (4.1) and (4.8),

\[
 {J_*\over7}
 \le {192\over7}K\alpha r\log r+O(1)
 \le {3\over28}r\log r+O(1).                         \tag{4.11}
\]

Since `|M_j|<=|M_0|={2r+1\choose r}=e^{O(r)}`, equations
(1.1), (4.10), and (4.11) imply (4.2), closing the induction.  The
conditional failure probabilities in (4.7) union-bound over the
`O_K(r\log r)` stopped rounds.  The descent and overshoot argument from
Theorem 3.1 completes the proof.  `square`

## 5. What remains

This theorem removes both uniform duplicate-excess control and lower
target-degree regularity from the *sufficiency* side of the punctured
nibble.  Those quantities may still be useful in proving that the maximum
degree bound (1.4) persists, but they are not themselves needed to turn a
good trajectory into a near-perfect matching.

For any fixed `K`, Corollary 4.1 reduces the remaining dynamic gate to
preserving only the one-sided maximum-degree bound (1.4) down to the small
fixed power `x=r^{-alpha}` in (4.1).  The empirical exponential floor then
follows deterministically from the conflict-neighbourhood count.  The
proved independent-residual estimates do not yet supply this adaptive
maximum-degree statement.
