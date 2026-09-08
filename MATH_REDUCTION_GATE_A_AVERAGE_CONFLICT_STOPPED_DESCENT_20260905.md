# Gate A alternative: average-conflict stopped descent

**Date:** 2026-09-05

**Status:** proved replacement for the stopped-descent hypothesis, and
proved bounded-test estimate under uniform exact slices. Persistence of
the replacement hypothesis under the actual adaptive law remains **OPEN**.
The original maximum-degree Gate A and the all-depth Gate B are not closed.

## 0. Audit verdict and scope

The proposed reduction is correct with the following qualifications made
explicit.

1. Input marks are independent; the isolated-mark indicators are not.
2. The descent theorem works for fixed `K>=1`. The proposed bounded test
   requires fixed `K>1` because its denominator is `(K-1)^2`.
3. Closed conflict neighborhoods include the edge itself. Graph degrees are
   therefore `g_e=C_e-1`, not `C_e`.
4. The fourth-moment upper bound for the test is a nonempty-state statement.
   Empty states require a separate term and are covered by the lower-tail
   estimate for the realized edge count.
5. An adaptive test bound must include the first newly reached violating
   state. A law already killed on that state's conflict-cap violation does
   not suffice.
6. The exponential bite-error bound is `exp(-Omega(r))`, obtained from
   second moments and exponentially large shores. No general exponential
   concentration inequality in the graph size is asserted.

In fact, no auxiliary degree-floor stop is needed to define the marking
probability: the mean-conflict cap itself implies `p<=1/16` at every live
state. The large average-degree floor is subsequently proved, without a
circular assumption.

The new graph, concentration, descent, denominator-transfer, and adaptive
union-bound arguments are proved below. The only imported reference-law
inputs are the two established exact-slice fourth moments, stated precisely
in Section 6. Their sources are `MASTER_HANDOFF.md`, Appendix C.3ter,
(C.3t.9)--(C.3t.10), using `s=2`. The process and normalization agree with
Section 4.2, Appendix C.5, and the definitions at the start of Appendix G.
The compact self-contained proof is incorporated in Appendix C.5a of the
master. This expanded note is supplemental; no index update is required.

## 1. States, normalization, and the actual process

Let `H` be a finite simple hypergraph with disjoint shores `M,L`, each edge
having exactly `2r` vertices in each shore. Shore sizes count all remaining
targets, including degree-zero targets. For a nonempty edge set define

\[
 Z=|E(H)|,\qquad n_\sigma=|V_\sigma(H)|,\qquad
 z_\sigma=\frac{2rZ}{n_\sigma},\qquad
 d(v)=|\{e\in E(H):v\in e\}|.
 \tag{1.1}
\]

Define the closed conflict neighborhoods and their mean by

\[
 \Gamma_H(e)=\{f\in E(H):e\cap f\ne\varnothing\},\qquad
 C_e=|\Gamma_H(e)|,\qquad
 \bar C=\frac1Z\sum_e C_e.
 \tag{1.2}
\]

The conflict graph has vertex set `E(H)` and joins distinct intersecting
edges. Its open degrees are `g_e=C_e-1`. Put

\[
 \chi(H)=\frac{\bar C}{2r(z_M+z_L)}.
 \tag{1.3}
\]

The former caps `d(v)<=K z_sigma` imply `chi<=K`, since they give
`C_e<=sum_{v in e}d(v)<=2rK(z_M+z_L)` for every edge. No converse
implication is assumed or needed.

If `Z=0`, set `chi(H)=+infinity`; no average or ratio in (1.1)--(1.3) is
then used. A nonempty state automatically has positive shore sizes and
positive `z_M,z_L`.

For the punctured application, the initial state is the complete directed
punctured catalogue on `[2r+1]`. Its parameters are

\[
 \begin{split}
 N_M&=\binom{2r+1}{r},\qquad
 N_L=\binom{2r+1}{r-1}=\frac r{r+2}N_M,\\
 Z_0&=(2r+1)!,\qquad
 D_M=2r\,r!(r+1)!,\qquad D_L=\frac{r+2}{r}D_M.
 \end{split}
 \tag{1.4}
\]

Fix constants

\[
 K\ge1,\qquad \gamma=\frac1{96K},\qquad
 0<\alpha\le\frac1{256K},\qquad x_*=r^{-\alpha}.
 \tag{1.5}
\]

All asymptotic assertions are for sufficiently large `r`, with these
constants fixed. Starting at `H_0`, let `F_j` be the sigma-field containing
the history before the marks for round `j`. In particular, `H_j` and its
statistics are `F_j`-measurable. Write

\[
 x_j=\frac{n_{j,L}}{N_L},\qquad
 \tau=\inf\{j:x_j\le x_*\ \text{or}\ \chi(H_j)>K\}.
 \tag{1.6}
\]

Give the density threshold priority if both conditions hold at the same
checkpoint. When `j<tau`, independently mark each current edge with the
predictable probability

\[
 p_j=\frac{\gamma}{r z_{j,M}}.
 \tag{1.7}
\]

Accept exactly the marked edges with no other marked conflict neighbor.
Delete their targets, and retain all catalogue edges supported on the
remaining targets. There are no purges and no extra deletions of isolated
targets. Freeze the process after `tau` if values at later times are needed.

Accepted edges are disjoint, so a round accepting `A_j` edges removes
exactly `2r A_j` vertices from each shore. Thus, on every history,

\[
 n_{j,M}-n_{j,L}=N_M-N_L=\frac{2N_L}{r},\qquad
 \frac{n_{j,M}}{n_{j,L}}=\frac{z_{j,L}}{z_{j,M}}
 =1+\frac2{rx_j}
 \tag{1.8}
\]

whenever the displayed ratios are defined. At a live checkpoint this
ratio lies in `[1,2]`, for all sufficiently large `r`.

The initial state is live: by regularity and the union bound,
`C_e<=2r(D_M+D_L)`, whence `chi(H_0)<=1`; also `x_0=1>x_*`.

## 2. Cap-free isolated-mark moments in a general graph

Consider any finite simple graph with `Z>0` vertices. Let `g_e` denote its
open degrees, `C_e=g_e+1`, and `bar C=Z^{-1} sum_e C_e`. Mark graph vertices
independently with probability `0<p<1`, and put `a=1-p`. Define

\[
 I_e=\mathbf1_{\{e\text{ is marked and no neighbor is marked}\}},
 \qquad A=\sum_e I_e,\qquad S=\sum_e C_e I_e.
 \tag{2.1}
\]

Then

\[
 \boxed{\begin{split}
 \mathbb EA&\ge Zp(1-p)^{\bar C-1},\\
 \mathbb ES&\le pZ\bar C,\\
 \operatorname{Var}A&\le Zp+p^3\sum_e g_e^2,\\
 \operatorname{Var}S&\le Z\bar C+p\sum_e g_e^2.
 \end{split}}
 \tag{2.2}
\]

These inequalities do not assume a bound on `p max_e g_e`.

### Proof of the expectations

The exact one-vertex probability is `E I_e=p a^{g_e}`. Convexity of
`t -> a^t` gives

\[
 \mathbb EA=p\sum_e a^{g_e}
 \ge Zp\,a^{Z^{-1}\sum_e g_e}=Zp\,a^{\bar C-1}.
 \tag{2.3}
\]

Also `E S=p sum_e C_e a^{g_e}<=p sum_e C_e`.

### Proof of the covariance bounds

Adjacent distinct vertices cannot both be isolated marks, so their
covariance is nonpositive. For nonadjacent distinct `e,f`, let

\[
 c=c_{ef}=|N(e)\cap N(f)|.
\]

Independence of the input marks gives exactly

\[
 \operatorname{Cov}(I_e,I_f)
 =p^2a^{g_e+g_f-c}(1-a^c).
 \tag{2.4}
\]

Since `1-a^c<=pc` and `g_e+g_f-c>=0`,

\[
 \operatorname{Cov}(I_e,I_f)\le p^3c.
 \tag{2.5}
\]

For the weighted estimate, AM--GM applied to the `C` terms
`1,a,...,a^{C-1}` gives, for every integer `C>=1`,

\[
 pC a^{(C-1)/2}
 \le p\sum_{i=0}^{C-1}a^i=1-a^C\le1.
 \tag{2.6}
\]

Also `c<=min(g_e,g_f)`, so
`g_e+g_f-c>=(g_e+g_f)/2`. Therefore (2.4)--(2.6) imply

\[
 \begin{split}
 C_e C_f\operatorname{Cov}(I_e,I_f)
 &\le p^3c C_e C_f a^{(g_e+g_f)/2}\\
 &=pc\,[pC_e a^{g_e/2}][pC_f a^{g_f/2}]
 \le pc.
 \end{split}
 \tag{2.7}
\]

The diagonal contribution for `A` is at most `Zp`. For `S`, (2.6) gives

\[
 C_e^2\operatorname{Var}I_e
 \le C_e^2 p a^{g_e}
 =C_e[pC_e a^{g_e/2}]a^{g_e/2}\le C_e.
 \tag{2.8}
\]

Finally, counting ordered pairs of neighbors of each vertex yields

\[
 \sum_{e,f}|N(e)\cap N(f)|=\sum_h g_h^2.
 \tag{2.9}
\]

The left sum includes diagonal and adjacent pairs, so it bounds the sum
over nonadjacent distinct pairs used in the variance expansion. Dropping
the nonpositive adjacent covariances and using (2.5), (2.7), and (2.8)
proves (2.2). There is no missing factor two: the covariance sums here are
over ordered distinct pairs. The variance bounds also extend to `p=0,1`
by continuity, although those endpoints are not needed below.

## 3. The rank bound and a concentrated deletion envelope

### 3.1 Closed conflict degree from its mean

Let a hypergraph have a nonempty edge set, with every edge of size between
`1` and `q`, and let `Delta_C=max_e C_e`. Then

\[
 \boxed{\Delta_C^2\le qZ\bar C.}
 \tag{3.1}
\]

To prove this, choose an edge `e_0` with `C_{e_0}=Delta_C`. Assign each
member `f` of its closed neighborhood to one witness vertex in
`f intersect e_0`. This includes `f=e_0`. The resulting at most `q`
classes have sizes `t_1,...,t_q`, padding with zeros. Every class is a
clique in the closed conflict relation. Hence

\[
 \sum_i t_i=\Delta_C,\qquad
 \sum_i t_i^2\le\sum_f C_f=Z\bar C.
\]

Cauchy--Schwarz proves (3.1). In particular,

\[
 \sum_e g_e^2\le\Delta_C\sum_e g_e
 \le\Delta_C Z\bar C.
 \tag{3.2}
\]

### 3.2 One live punctured state

Suppose a two-shore state has `n=n_M`, `1<=n_M/n_L<=2`, and `chi<=K`.
Put `z=z_M`, `p=gamma/(rz)`. The cap says

\[
 \bar C\le2rK(z_M+z_L)\le6Kr z,
 \qquad p\bar C\le6K\gamma=\frac1{16}.
 \tag{3.3}
\]

Because `bar C>=1`, this also proves `0<p<=1/16`. Thus the marking rule
is valid without assuming any average-degree floor. The exact incidence
identity gives

\[
 Zp=\frac{\gamma n}{2r^2},\qquad
 \beta:=\frac{\bar C}{Z}\le b:=\frac{12Kr^2}{n}.
 \tag{3.4}
\]

Here the rank is `q=4r`, so by (3.1)

\[
 \frac{\Delta_C}{Z}\le\sqrt{4r\beta}
 \le\delta:=\sqrt{\frac{48Kr^3}{n}}.
 \tag{3.5}
\]

Equations (2.2), (3.2), and (3.3) now give

\[
 \begin{split}
 \frac{\operatorname{Var}A}{(Zp)^2}
 &\le\frac1{Zp}+p\bar C\frac{\Delta_C}{Z}
 \le\frac{2r^2}{\gamma n}+\frac\delta{16},\\
 \frac{\operatorname{Var}S}{Z^2}
 &\le\beta+p\bar C\frac{\Delta_C}{Z}
 \le b+\frac\delta{16}.
 \end{split}
 \tag{3.6}
\]

As `log(1-p)>=-2p` for `p<=1/2`,

\[
 \mathbb EA\ge Zp e^{-2p\bar C}
 \ge e^{-1/8}Zp\ge\frac78Zp,
 \qquad \mathbb ES\le\frac Z{16}.
 \tag{3.7}
\]

Chebyshev, with deviations `3Zp/8` and `Z/16`, respectively, gives

\[
 \begin{split}
 \Pr(A<Zp/2)&\le\frac{64}{9}
       \left(\frac{2r^2}{\gamma n}+\frac\delta{16}\right),\\
 \Pr(S>Z/8)&\le256\left(b+\frac\delta{16}\right).
 \end{split}
 \tag{3.8}
\]

If `Y` is the number of input marks, `A<=Y`, and
`E 2^Y=(1+p)^Z<=exp(Zp)`. Consequently,

\[
 \Pr(A>2Zp)\le\exp(-(2\log2-1)Zp).
 \tag{3.9}
\]

Thus the event

\[
 \mathcal Q(H):\qquad
 \frac12 Zp\le A\le2Zp,\qquad S\le\frac Z8
 \tag{3.10}
\]

has failure probability at most

\[
 \varepsilon_K(r,n):=
 \frac{64}{9}\left(\frac{2r^2}{\gamma n}+\frac\delta{16}\right)
 +256\left(\frac{12Kr^2}{n}+\frac\delta{16}\right)
 +\exp\left(-\frac{(2\log2-1)\gamma n}{2r^2}\right).
 \tag{3.11}
\]

In particular, for exponentially large `n`, this is `exp(-Omega(r))`.
The square-root population term in (3.5) is harmless at this scale.

If `H'` is the child after accepting the isolated marks, its removed
edges are exactly the union of their closed conflict neighborhoods.
Therefore, deterministically,

\[
 Z-Z'=\left|\bigcup_{e:I_e=1}\Gamma_H(e)\right|
 \le\sum_e C_e I_e=S.
 \tag{3.12}
\]

On (3.10), this proves `Z'>=7Z/8`. This weighted envelope, not the
maximum neighborhood size times `A`, replaces the last use of individual
caps in Appendix C.5.

## 4. Proved average-conflict stopped descent

**Theorem.** Run the process of Section 1 and set

\[
 J_*:=\left\lceil\frac{2\alpha r\log r}{\gamma}\right\rceil.
 \tag{4.1}
\]

Outside an event of probability `exp(-Omega(r))`, every performed round
before `min(tau,J_*)` satisfies (3.10), and `tau<=J_*`. All states reached
through that stop have

\[
 z_{j,M}\ge\exp(r\log r).
 \tag{4.2}
\]

There are then exactly two alternatives: the mean-conflict cap fails at a
checkpoint with `x_j>x_*`, or the accepted configurations form a matching
whose terminal densities satisfy

\[
 (1-4\gamma/r)x_*\le x_\tau\le x_*,\qquad
 \frac{n_{\tau,M}}{N_M}=\frac{rx_\tau+2}{r+2}=o(1).
 \tag{4.3}
\]

In particular the lower residual is `r^{-alpha}(1+O_K(1/r))`, with the
same constants `gamma,alpha,J_*` and `7/8` edge-count retention as in
Appendix C.5. No individual target-degree caps are hypotheses.

### Proof

At every live checkpoint, (1.8) gives shore comparability and

\[
 n_{j,M}\ge n_{j,L}>x_*N_L=\exp(\Omega(r)).
 \tag{4.4}
\]

For completeness, the largest binomial coefficient is at least the
average, so `N_M>=2^{2r+1}/(2r+2)`; the formula for `N_L` in (1.4)
proves (4.4). The constants are uniform over live histories. Section 3
applies conditionally on `F_j`: once the current state is fixed, only the
fresh independent marks are random. Hence

\[
 \Pr(\mathcal Q_j^c\mid\mathcal F_j)
 \le e^{-c_K r}\quad\text{on }\{j<\tau\},
 \tag{4.5}
\]

for a fixed positive constant and all sufficiently large `r`. Define
`Q_j` to hold automatically when no round is performed. Since
`{j<tau}` is `F_j`-measurable, the tower property and a union bound give

\[
 \Pr\bigl(\exists j<J_*:j<\tau,\ \mathcal Q_j^c\bigr)
 \le J_*e^{-c_Kr}=e^{-\Omega(r)}.
 \tag{4.6}
\]

This does not condition on the future event of cap persistence.

Work on the complement. In each performed round, the lower and upper
bounds for `A_j`, together with (3.4), give

\[
 \frac{\gamma}{2r}\le\frac{2rA_j}{n_{j,M}}
 \le\frac{2\gamma}{r},\qquad
 \frac{\gamma}{2r}\le\frac{2rA_j}{n_{j,L}}
 \le\frac{4\gamma}{r}.
 \tag{4.7}
\]

In particular,

\[
 (1-4\gamma/r)x_j\le x_{j+1}
 \le(1-\gamma/(2r))x_j.
 \tag{4.8}
\]

If the process were still live after `J_*` rounds, the upper bound would
imply

\[
 x_{J_*}\le\exp(-\gamma J_*/(2r))\le r^{-\alpha},
\]

a contradiction. Thus `tau<=J_*`. If the density threshold is reached,
the last round and (4.8) give (4.3), using the exact shore identity (1.8).

Also (3.12) gives, at every reached checkpoint `j<=tau`,

\[
 Z_j\ge Z_0(7/8)^j.
 \tag{4.9}
\]

Using `log(8/7)<=1/7`, Stirling's formula, and (1.5),

\[
 \begin{split}
 \log Z_j
 &\ge(2-o(1))r\log r-\frac{J_*}{7},\\
 \frac{J_*}{7}
 &\le\frac{192K\alpha}{7}r\log r+\frac17
 \le\frac3{28}r\log r+\frac17.
 \end{split}
 \tag{4.10}
\]

Thus `log Z_j>=(53/28-o(1))r log r`. Since
`n_{j,M}<=N_M=exp(O(r))`, (1.1) proves (4.2), including at the terminal
checkpoint. In particular no edge-empty stop can occur on this good
event. The accepted edges are disjoint within rounds by isolation, and
across rounds by deletion of their targets, so their union is a matching.
This completes the proof.

The theorem is a stopped alternative, not a proof that `chi<=K` persists.
It also applies with `K=1`; the test reduction below uses `K>1`.

## 5. A bounded test for the replacement stop

Now fix `K>1`. On a nonempty state put

\[
 U_{m,\sigma}(H)=\frac1{n_\sigma}
       \sum_{v\in V_\sigma(H)}\left|\frac{d(v)-z_\sigma}{z_\sigma}\right|^m,
 \qquad m\in\{2,4\},
 \tag{5.1}
\]

and define on all states

\[
 T_K(H)=
 \begin{cases}
 \displaystyle\min\left\{1,
      \left[\frac{(\chi(H)-1)_+}{K-1}\right]^2\right\},&Z>0,\\
 1,&Z=0.
 \end{cases}
 \tag{5.2}
\]

Thus `0<=T_K<=1` everywhere and, with the empty-state convention,

\[
 \mathbf1_{\{\chi(H)>K\}}\le T_K(H).
 \tag{5.3}
\]

For nonempty states the stronger pointwise upper bound is

\[
 \boxed{T_K(H)\le
 \frac{\eta_M U_{4,M}(H)+\eta_L U_{4,L}(H)}{(K-1)^2}
 \le\frac{U_{4,M}(H)+U_{4,L}(H)}{(K-1)^2},}
 \qquad \eta_\sigma=\frac{z_\sigma}{z_M+z_L}.
 \tag{5.4}
\]

### Proof

Counting conflicts by witness vertices, allowing overcounting, gives

\[
 \bar C\le\frac1Z\sum_v d(v)^2
 =2r\sum_{\sigma\in\{M,L\}}z_\sigma(1+U_{2,\sigma}).
 \tag{5.5}
\]

The last equality uses the empirical mean identity
`sum_{v in V_sigma}d(v)=n_sigma z_sigma`. Hence

\[
 (\chi-1)_+\le\eta_M U_{2,M}+\eta_L U_{2,L}.
\]

Convexity of the square and Cauchy--Schwarz on each shore yield

\[
 (\chi-1)_+^2
 \le\eta_M U_{2,M}^2+\eta_L U_{2,L}^2
 \le\eta_M U_{4,M}+\eta_L U_{4,L}.
 \tag{5.6}
\]

This proves (5.4). Notice that `chi` need not be at least one; its positive
part in the definition is intentional.

No value of `U_{4,sigma}` is assigned at `Z=0`, where its denominator
vanishes. A globally valid upper bound is instead `1` on that event and
the right side of (5.4) on its complement. Writing (5.4) unqualified at
empty states would be a defect.

## 6. Exact-slice estimate with the realized denominator

Independently choose a uniform `n_M`-subset of the original middle shore
and a uniform `n_L`-subset of the original lower shore. Let `H` contain
all original catalogue edges supported on these two sets. Write

\[
 x=\min\{n_M/N_M,n_L/N_L\}\ge r^{-\alpha},\qquad
 m=\mathbb E_{\rm sl}Z.
 \tag{6.1}
\]

Here `0<alpha<1/12` suffices. In particular it includes the entire range
in (1.5). Both retained shore sizes are exponentially large, so they
exceed all `O(r)` footprints in the fourth-moment estimates. With falling
factorials,

\[
 m=Z_0\prod_{\sigma\in\{M,L\}}
       \frac{(n_\sigma)_{2r}}{(N_\sigma)_{2r}}>0.
 \tag{6.2}
\]

In this range `m>=exp((2-4alpha+o(1))r log r)`. The usual finite-population
comparison has relative error `O(r^2/(x min_sigma N_sigma))`, which is
exponentially small here.

For a fixed original target `v` in shore `sigma`, condition on its
retention and let `X_v` be its degree. Its exact conditional mean is
independent of the label and equals

\[
 \mu_\sigma:=\mathbb E_{\rm sl}[X_v\mid v\text{ retained}]
 =\frac{2rm}{n_\sigma}.
 \tag{6.3}
\]

Indeed, regularity makes the root-conditioned mean constant, and summing
the degree over retained roots gives `2rZ`. Equivalently, (6.3) follows
directly from (6.2) by removing the root from its shore's falling
factorials. There is no replacement of an exact-slice mean by a product
mean in (6.3).

### 6.1 Established reference inputs

Appendix C.3ter, (C.3t.9)--(C.3t.10) with `s=2`, gives uniformly in these
exact sizes and root labels

\[
 \begin{split}
 \frac{\mathbb E_{\rm sl}[(X_v-\mu_\sigma)^4
                    \mid v\text{ retained}]}{\mu_\sigma^4}
 &\le C(rx^3)^{-2}+e^{-\Omega(r)},\\
 \frac{\mathbb E_{\rm sl}(Z-m)^4}{m^4}
 &\le C(rx)^{-2}+e^{-\Omega(r)}.
 \end{split}
 \tag{6.4}
\]

The explicit finite-population remainders are
`O(r^2/(x min_sigma N_sigma))`. Removing the retained root changes a
density by only `O(1/min_sigma N_sigma)`. If necessary, apply the source
theorem with any fixed exponent strictly between `alpha` and `1/12`;
this handles the endpoint without changing the scale in (6.4).

These are uniform-slice facts, not facts about the adaptive process.

### 6.2 Truncation and centering proof

Define the deterministic-center empirical fourth moments

\[
 W_{4,\sigma}(H)=\frac1{n_\sigma\mu_\sigma^4}
       \sum_{v\in V_\sigma(H)}(d(v)-\mu_\sigma)^4.
 \tag{6.5}
\]

They are well-defined even if `Z=0`. Summing first over the original
target labels and using `Pr(v retained)=n_sigma/N_sigma` shows from
(6.4) that

\[
 \mathbb E_{\rm sl}W_{4,\sigma}
 \le C(rx^3)^{-2}+e^{-\Omega(r)}.
 \tag{6.6}
\]

Let `B={Z>=m/2}` and put `theta=Z/m`. On `B`,
`z_sigma=theta mu_sigma>=mu_sigma/2`. Jensen's inequality for the average
over the realized shore gives

\[
 |z_\sigma-\mu_\sigma|^4
 \le\frac1{n_\sigma}\sum_{v\in V_\sigma(H)}
             |d(v)-\mu_\sigma|^4.
 \tag{6.7}
\]

Using `|u+v|^4<=8(|u|^4+|v|^4)` and then (6.7),

\[
 \begin{split}
 U_{4,\sigma}
 &\le16\left(\frac{\mu_\sigma}{z_\sigma}\right)^4
                 W_{4,\sigma}
 \le256 W_{4,\sigma}\qquad\text{on }B.
 \end{split}
 \tag{6.8}
\]

The lower-denominator event is bounded separately, using the unrooted
fourth moment, not a second-moment estimate:

\[
 \Pr_{\rm sl}(B^c)
 \le16\frac{\mathbb E_{\rm sl}(Z-m)^4}{m^4}
 \le C(rx)^{-2}+e^{-\Omega(r)}.
 \tag{6.9}
\]

This event includes every edge-empty state. Since the test is bounded by
one, (5.4) and (6.8)--(6.9) prove

\[
 \begin{split}
 \mathbb E_{\rm sl}T_K(H)
 &\le\Pr_{\rm sl}(B^c)
   +\frac{256}{(K-1)^2}\sum_\sigma\mathbb E_{\rm sl}W_{4,\sigma}\\
 &\le O_K((rx^3)^{-2})+e^{-\Omega(r)}.
 \end{split}
 \tag{6.10}
\]

The last step uses `x<=1`, so `(rx)^{-2}<=(rx^3)^{-2}`. This proves the
claimed test estimate with all denominators and empty states accounted
for. It does not assert an untruncated bound for the expectation of the
empirically normalized `U_4` on the rare event `0<Z<m/2`.

The estimate also holds for any probability or subprobability mixture of
these exact slices with densities at least `x_*`, with `x_*` on the
right side. This follows by summing (6.10) against the nonnegative slice
weights; no division by a small slice probability is involved.

## 7. The precise open adaptive target

Use the actual process, filtration, and stop from Section 1, now with
`K>1`. For `0<=j<J_*`, let

\[
 \mathcal G_j=\{j<\tau\}\in\mathcal F_j.
\]

The state `H_{j+1}` means the raw child produced by the round, before
discarding it because its new value of `chi` violates the cap. A sufficient
open estimate is

\[
 \boxed{
 \mathbb E\left[
   \mathbf1_{\mathcal G_j}
   \mathbf1_{\{x_{j+1}>x_*\}}T_K(H_{j+1})\right]
 \le r^{\kappa+o(1)}(r x_*^3)^{-2}+e^{-\Omega(r)},
 \qquad \kappa<1-6\alpha.}
 \tag{7.1}
\]

The `o(1)` in the exponent and the exponential error must be uniform over
`j<J_*`. Constants may depend on fixed `K,alpha`. The left side is an
expectation under a stopped *arrival* subprobability law. It is not
conditioned on the new state being good. The factor specifying the
child's density is `F_{j+1}`-measurable; it is not used to condition the
independent marking law in advance.

### 7.1 Why this target suffices

The first conflict violation before the density threshold, if it occurs
by time `J_*`, must be one of the events

\[
 \mathcal G_j\cap\{x_{j+1}>x_*,\ \chi(H_{j+1})>K\},
 \qquad 0\le j<J_*.
\]

The initial state is good. By (5.3), a union bound therefore gives

\[
 \begin{split}
 &\Pr(\tau\le J_*,\ x_\tau>x_*)\\
 &\quad\le\sum_{j<J_*}\mathbb E\left[
    \mathbf1_{\mathcal G_j}
    \mathbf1_{\{x_{j+1}>x_*\}}T_K(H_{j+1})\right].
 \end{split}
 \tag{7.2}
\]

By Section 4, `Pr(tau>J_*)<=exp(-Omega(r))`, and the same error covers
any failure of the bite estimates. If (7.1) were proved, the sum in
(7.2) would be at most

\[
 O_K(r\log r)\,r^{\kappa+o(1)}r^{-2+6\alpha}
       +e^{-\Omega(r)}
 =r^{\kappa-1+6\alpha+o(1)}=o(1).
 \tag{7.3}
\]

Thus (7.1) would make the *alternative* conflict stop unlikely and would
give the near-factor conclusion (4.3) with probability `1-o(1)`.
The strict inequality on `kappa` is needed; the endpoint is not covered.

It is also sufficient to impose (7.1) only on histories whose earlier
performed rounds satisfied (3.10). The omitted histories already have
total probability `exp(-Omega(r))` by (4.6).

### 7.2 What is and is not a conditional input

The mark-law statements (2.2)--(3.11) are conditional on the full
pre-round sigma-field `F_j`. They remain valid for the predictable
state-dependent probability `p_j`; no averaging of `p_j` outside its
conditional state is used.

In contrast, (7.1) is an annealed stopped-law target for one bounded
statistic. A uniform bound on

\[
 \mathbb E[\mathbf1_{\{x_{j+1}>x_*\}}T_K(H_{j+1})
                  \mid\mathcal G_j]
\]

for each positive-probability `G_j` would be sufficient and stronger.
A pointwise bound conditional on every full history `F_j` would be
stronger still and is not required here. No assertion conditions on
future persistence of the cap.

One must not replace the arrival law in (7.1) by a law containing the
factor `1_{chi(H_{j+1})<=K}`. That replacement removes the first violating
state from the test and cannot justify (7.2). Likewise, a moment estimate
conditioned only on `j<tau`, evaluated at `H_j` after its cap check, is
not by itself the claimed first-exit estimate.

The exact-slice theorem does not prove (7.1). To see the remaining issue
precisely, assign to each size vector `n` the weight

\[
 w_j(n)=\Pr(\mathcal G_j,\ x_{j+1}>x_*,\
                     (n_{j+1,M},n_{j+1,L})=n).
\]

Replacing the shapes on each such fiber by a uniform exact slice gives
a reference subprobability mixture. By (6.10), its expectation of `T_K`
has the desired lossless scale. However, the actual conditional shapes
inside those same fibers are selected by the matching history, and need
not be uniform. Comparing this single bounded statistic, or proving
(7.1) directly, remains open. No full-state likelihood-ratio bound,
mixing theorem, or adaptive transfer is hidden in this reduction.

## 8. Consequences, nonconsequences, and verification

The proof establishes that an average closed-conflict cap is sufficient
for the same stopped two-shore descent previously obtained from two
maximum-degree caps. It also reduces preservation of this alternative
cap to a bounded fourth-moment-scale test, with sufficient comparison
loss `r^{kappa+o(1)}` for `kappa<1-6alpha`.

It does not prove the original Gate A, whose stated stop uses maximum
target degrees. Small average conflict need not imply those individual
caps. It does not prove persistence of the alternative cap either:
(7.1) is the explicit open adaptive target. No drift sign for `chi` has
been asserted or used.

Even if (7.1) is established, the matching only reaches
`x=r^{-alpha}(1+O_K(1/r))` in the small fixed-exponent range (1.5).
Gate B still requires compatible all-depth cover-down on these same
literal rows. In particular this theorem supplies neither continuation
to `x=o(r^{-1/3})` nor the positive fractional cover required by that
gate's alternative.

Finite checks performed during this audit:

- The existing, unmodified
  `scratch_gate_a_mean_conflict_variance_20260905_a8f13.py` passed 3,297
  exact graph/mark-law checks and 2,189 exact hypergraph checks. Its graph
  audit enumerates all graphs with at most five vertices at
  `p=1/5,1/2,4/5`; its hypergraph audit includes (3.1).
- An independent exact-rational calculation checked (2.5)--(2.7) for
  all `0<=g_e,g_f<=20`, `0<=c<=min(g_e,g_f)`, at
  `p=1/100,1/5,1/2,4/5,99/100`: 16,555 cases.
- An independent exact-rational calculation checked the rank inequality,
  the test inequality, and the deterministic denominator transfer on
  all 511 nonempty subfamilies of the nine two-by-two edges on active
  three-by-three shores, padded to shore sizes `3,8,20`. It used
  `K=3/2,2,3` and deterministic centers `2z,z,z/2`, giving 4,599
  state/test cases.

These finite checks support the algebra but do not replace the general
proofs above and do not test the open adaptive estimate.
