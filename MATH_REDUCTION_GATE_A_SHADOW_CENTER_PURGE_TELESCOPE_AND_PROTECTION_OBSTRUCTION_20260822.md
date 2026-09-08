# Gate A: exact sixth-mass drift, a shadow-center purge telescope, and the protection obstruction

**Date:** 2026-08-22

**Status:** unconditional first-variation and deterministic purge theorems,
plus an exact cap-and-degree-floor obstruction to a collision-only
self-correction argument.  The results do **not** prove the stopped Gate A
estimate.  They show precisely what an attempted self-correcting proof must
add to the centered collision scalar.

## 1. Summary

Let `H` be a current residual hypergraph and perform one isolated-mark bite.
The existing centered row scalar `mathfrak D` is the nonlinear collision
error in the first variation of the sixth centered degree mass.  It is not,
however, the whole first variation.  The exact normalized identity below
also contains

1. a seventh-moment transport term;
2. an exponentially negligible lattice term at the punctured degree floor;
   and
3. a signed rooted **protection covariance**

\[
 -\sum_v d(v)\Xi_v\nabla_6(d(v)-z),
\]

where `Xi_v` is the rooted conflict-exposure discrepancy from Appendix
C.3quater of the master handoff.  Negative `Xi_v` on a high-degree target is
harmful: conditional on surviving, that target is protected relative to the
shore average.

For the one-sided sixth mass, the seventh-moment term is contractive.  This
leaves an exact positive protection statistic.  If its stopped cumulative
excess and the existing collision scalar have total normalized forcing
`o(1/r)`, then a shadow-center potential can charge every purge by
`Omega(rho/r)`.  Since the reference collision budget is

\[
 O(r^{-2}x_J^{-32}),
\]

this telescope has exactly the natural strict range `alpha<1/32`.

The protection hypothesis cannot be deleted by a formal inequality.  The
graph

\[
                         K_{d,d}\ \dot\cup\ K_{1,d}
\]

has average degree `(2/3+o(1))d`, maximum/average ratio `3/2+o(1)`, and
arbitrarily large degree floor.  It is triangle-free, so every external row
has size at most one and **every centered collision scalar is identically
zero**.  Nevertheless its normalized upper-sixth-mass derivative is

\[
                         (17/288+o(1))d>0.
\]

This example is not asserted to be a punctured residual.  It proves the
logical point needed here: cap, degree floor, and `mathfrak D` do not imply
self-correction in a general shore-uniform residual.  A punctured proof must
use its geometry to control the protection covariance, or use a different
nonperturbative argument.

## 2. The isolated-edge tangent

Let `H` be a finite simple hypergraph.  Fix one shore `V_sigma`, and suppose
every edge contains exactly `k_sigma` vertices of that shore.  Put

\[
 Z=|E(H)|,\qquad n=|V_\sigma|,\qquad
 z={k_\sigma Z\over n}.                                      \tag{2.1}
\]

For an edge `F`, write

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 C_F=|\Gamma(F)|,\qquad
 \bar C={1\over Z}\sum_F C_F.                               \tag{2.2}
\]

For a positive-degree target define

\[
 E_v={1\over d(v)}\sum_{F\ni v}C_F-d(v),\qquad
 B_\sigma=\bar C-z,\qquad
 \Xi_v=E_v-B_\sigma.                                        \tag{2.3}
\]

For a zero-degree target set `d(v)E_v=d(v)Xi_v=0`; its separate values are
irrelevant.  For `v notin G`, let

\[
 a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|.             \tag{2.4}
\]

Mark all edges independently with probability `p`, accept the isolated
marks, delete the vertices in accepted edges, and call the residual `H_p`.
Let

\[
 z^{\rm ann}(p)
 ={k_\sigma\mathbb E|E(H_p)|\over
                   \mathbb E|V_\sigma(H_p)|}.                \tag{2.5}
\]

The single-mark calculation gives

\[
 {d\over dp}\log z^{\rm ann}(p)\bigg|_{p=0}=-B_\sigma,
 \qquad
 {d\over dp}\log\mathbb E|V_\sigma(H_p)|\bigg|_{p=0}=-z.
                                                                    \tag{2.6}
\]

Both are exact derivatives; inhibition needs at least two marks and hence
does not occur in (2.6).

## 3. Exact symmetric sixth-mass identity

Put

\[
 f_z(d)=(d-z)^6,\qquad
 \nabla_6(t)=t^6-(t-1)^6.                                  \tag{3.1}
\]

Define the row defect and its aggregate by

\[
 \phi_z(d,a)=a\nabla_6(d-z)-\{(d-z)^6-(d-a-z)^6\},           \tag{3.2}
\]

\[
 \mathfrak D_{z,\sigma}(H)
 =\sum_{v\in V_\sigma}\sum_{G\not\ni v}
       \phi_z(d(v),a_G(v)).                                 \tag{3.3}
\]

This is the same nonnegative scalar as in Appendix C.12.  Finally define

\[
 P_4(t)=6t^5-\nabla_6(t)
       =15t^4-20t^3+15t^2-6t+1.                             \tag{3.4}
\]

Since

\[
 P_4(t)=6\int_{t-1}^t(t^5-s^5)\,ds,                         \tag{3.5}
\]

one has `P_4(t)>=0` for every real `t`; this is also immediate from the
monotonicity of `6t^5`.

Let

\[
 S_6(p)=\mathbb E\sum_{v\in V_\sigma(H_p)}
       (d_{H_p}(v)-z^{\rm ann}(p))^6,                        \tag{3.6}
\]

and normalize by the annealed shore size and center,

\[
 \Psi_6(p)={S_6(p)\over
  \mathbb E|V_\sigma(H_p)|\,(z^{\rm ann}(p))^6}.             \tag{3.7}
\]

### Theorem 3.1 (exact normalized first variation)

With `t_v=d(v)-z`,

\[
\boxed{
 nz^6\Psi_6'(0)
 =\mathfrak D_{z,\sigma}(H)
  -\sum_v t_v^7
  +B_\sigma\sum_vd(v)P_4(t_v)
  -\sum_vd(v)\Xi_v\nabla_6(t_v).}                          \tag{3.8}
\]

#### Proof

At first order exactly one marked edge `G` is accepted.  At fixed center
`z`, deleting its vertices changes the shore mass by

\[
 -\sum_{v\in G}f_z(d(v))
 -\sum_{v\notin G}\{f_z(d(v))-f_z(d(v)-a_G(v))\}.            \tag{3.9}
\]

Summing (3.9) over `G`, inserting (3.2), and using the exact incidence
identity

\[
 \sum_{G\not\ni v}a_G(v)=d(v)E_v,                            \tag{3.10}
\]

gives the fixed-center derivative

\[
 -\sum_vd(v)t_v^6-\sum_vd(v)E_v\nabla_6(t_v)
 +\mathfrak D_{z,\sigma}(H).                                \tag{3.11}
\]

The center derivative in (2.6) contributes

\[
                         6zB_\sigma\sum_vt_v^5.              \tag{3.12}
\]

The logarithmic derivative of the denominator in (3.7) is
`-z-6B_sigma`.  Thus `nz^6 Psi_6'(0)` equals (3.11)--(3.12)
plus `(z+6B_sigma)sum_v t_v^6`.  Substitute
`E_v=B_sigma+Xi_v`.  For every `t`, with `d=z+t`,

\[
 (z+6B-d)t^6-dB\nabla_6(t)+6zBt^5
 =-t^7+Bd\{6t^5-\nabla_6(t)\}.                      \tag{3.13}
\]

Equations (3.4) and (3.13) prove (3.8).  \(\square\)

The third term of (3.8) is a lattice correction, not a new adaptive
profile.  Under the punctured cap, `B_sigma=O_K(rz)`.  Moreover

\[
 P_4(t)\le C(1+|t|^4).                                      \tag{3.14}
\]

If `Delta_sigma<=Kz` and `Psi_6<=1`, then Holder gives

\[
 \sum_vd(v)P_4(t_v)
 \le C_Knz\{1+z^4\Psi_6^{2/3}\}.                            \tag{3.15}
\]

At `p=O((rz)^{-1})`, division by `nz^6` makes (3.15)

\[
 O_K(z^{-5}+z^{-1}\Psi_6^{2/3}),                            \tag{3.16}
\]

which is exponentially small at the proved stopped degree floor
`z>=exp(r log r)`.  The last term of (3.8) has no such automatic bound.

## 4. The one-sided potential and the exact harmful statistic

For the upper cap the symmetric mass contains an unnecessary low-degree
tail.  Put

\[
 g_z(d)=(d-z)_+^6,
 \qquad \nabla_+(t)=t_+^6-(t-1)_+^6,                         \tag{4.1}
\]

\[
 P_4^+(t)=6t_+^5-\nabla_+(t).                                \tag{4.2}
\]

Convexity of `t_+^6` gives `P_4^+(t)>=0`.  For `t>=1`,

\[
 P_4^+(t)=P_4(t)\le15t^4.                                   \tag{4.3}
\]

Define `mathfrak D^+` by replacing `f_z` with `g_z` in (3.2)--(3.3),
and define `Psi_+` as in (3.6)--(3.7) with `g_z`.

Exactly the same proof gives

\[
\boxed{
 nz^6\Psi_+'(0)
 =\mathfrak D^+_{z,\sigma}(H)
  -\sum_v(t_v)_+^7
  +B_\sigma\sum_vd(v)P_4^+(t_v)
  -\sum_vd(v)\Xi_v\nabla_+(t_v).}                         \tag{4.4}
\]

The existing symmetric collision scalar dominates this one.  Indeed, with
`U,V` independent uniform variables on `[0,1]`,

\[
 \Delta^2(t^6)=30\mathbb E(t-U-V)^4,\qquad
 \Delta^2(t_+^6)=30\mathbb E(t-U-V)_+^4.                    \tag{4.5}
\]

Therefore `0<=Delta^2(t_+^6)<=Delta^2(t^6)` pointwise.  The shifted
second-difference representation of the row defect then proves

\[
                         0\le\mathfrak D^+_{z,\sigma}(H)
                         \le\mathfrak D_{z,\sigma}(H).        \tag{4.6}
\]

There is also a cross-center version needed below.  If `c>=z`, then

\[
 \boxed{0\le\mathfrak D^+_{c,\sigma}(H)
                  \le\mathfrak D_{z,\sigma}(H).}              \tag{4.6a}
\]

Indeed, in the shifted second-difference representation, put
`delta=c-z>=0`.  Pointwise,

\[
 (x-\delta-U-V)_+^4\le(x-U-V)^4.
\]

The row weights are the same and nonnegative, proving (4.6a).

Only the negative part of `Xi_v` is harmful.  A sharp statistic which lets
half of the seventh-moment contraction pay for that part is

\[
 \boxed{
 \mathcal R_{z,\sigma}(H)
 =\sum_{v:t_v>0}
 \left[d(v)(B_\sigma-E_v)_+\nabla_+(t_v)
                  -{1\over2}t_v^7\right]_+.}                \tag{4.7}
\]

Equations (4.4)--(4.7) imply

\[
 nz^6\Psi_+'(0)
 \le \mathfrak D_{z,\sigma}(H)+\mathcal R_{z,\sigma}(H)
 -{1\over2}\sum_v(t_v)_+^7
 +B_\sigma\sum_vd(v)P_4^+(t_v).                            \tag{4.8}
\]

Thus `mathcal R`, rather than another factorial collision order, is the
precise first-order obstruction to a self-correcting upper-tail proof.

### 4.1 Exact covariance and frozen-compensator form

The protection term has a second exact compression.  Let `w_v` be any
real target weight on the shore and put

\[
                         W_F=\sum_{v\in F\cap V_\sigma}w_v.   \tag{4.9}
\]

Under the uniform distribution on current edges,

\[
\boxed{
 -\sum_vd(v)\Xi_vw_v
 =\sum_vd(v)(d(v)-z)w_v
       -Z\operatorname {Cov}_{F}(C_F,W_F).}                  \tag{4.10}
\]

Indeed `Xi_v=A_v-bar C-(d(v)-z)`, where
`d(v)A_v=sum_(F ni v)C_F`.  Interchanging `v,F` gives

\[
 \sum_vd(v)(\bar C-A_v)w_v
 =\bar C\sum_FW_F-\sum_FC_FW_F
 =-Z\operatorname {Cov}_F(C_F,W_F),                           \tag{4.11}
\]

which proves (4.10).  In (4.4), take `w_v=nabla_+(t_v)`.  The first term
on the right of (4.10) is the ordinary size-bias contribution; the truly
history-sensitive part is a negative correlation between conflict degree
`C_F` and upper-tail load `W_F`.

There is an exact mixed-compensator interpretation.  Freeze the current
weights `w_v`, perform an infinitesimal bite, and let `bar W(p)` be the
average of the frozen `W_F` over surviving edges.  Then

\[
                         \boxed{\bar W'(0)
                         =-\operatorname {Cov}_F(C_F,W_F).}   \tag{4.12}
\]

The numerator has derivative `-sum_F C_FW_F`, while the edge count has
derivative `-Z bar C`, proving (4.12).  Thus a mixed center/exposure
compensator can cancel the covariance *algebraically*.  It must still solve
two nonformal problems: the weights themselves change with the degrees,
and subtracting the natural frozen compensator need not leave a
nonnegative Lyapunov function.  Equation (4.12) is therefore a genuine
route to investigate, not a completed cancellation theorem.

For reference, Cauchy gives the rigorous sufficient bound

\[
 |Z\operatorname {Cov}(C,W)|
 \le Z\sqrt{\operatorname {Var}_F C_F\;\mathbb E_FW_F^2}.     \tag{4.13}
\]

Consequently a stopped theorem controlling conflict-degree variance
together with the upper-tail moment would control `mathcal R`.  A cap gives
only `C_F=O(rz)` and is too weak by itself; the example in Section 7 has
the wrong exposure alignment despite zero row collision.

### 4.2 A pathwise protection-to-conflict-variance bound

The covariance reduction gives a positive theorem once the cap threshold
has a fixed margin above the actual average.  Suppose

\[
 c\ge(1+\delta)z,\qquad c\le A_0z,\qquad
 \Delta_\sigma\le Kz,                                      \tag{4.14}
\]

for fixed positive `delta,A_0,K`.  Put

\[
 U_6={1\over nz^6}\sum_v(d(v)-z)^6,qquad
 V_C={\operatorname {Var}_{F\in E(H)}C_F\over z^2}.          \tag{4.15}
\]

Let `t_v=d(v)-c`, `w_v=nabla_+(t_v)`, and let

\[
 \mathcal P_c=-\sum_vd(v)\Xi_vw_v                         \tag{4.16}
\]

be the complete signed protection term in the elevated-center identity
(5.4a).  If the punctured marking rate satisfies `p<=C_p/(rz)`, then

\[
 \boxed{
 {p\over nc^6}(\mathcal P_c)_+
 \le {C_{\delta,A_0,K,C_p}\over r}
       \left(U_6+\sqrt{V_CU_6}\right).}                     \tag{4.17}
\]

This is deterministic conditional on the current residual.

#### Proof

Only targets in

\[
                         T=\{v:d(v)>c\}                       \tag{4.18}
\]

have nonzero `w_v`.  Every such target satisfies
`|d(v)-z|>=delta z`, so

\[
 |T|\le\delta^{-6}nU_6,qquad
 \sum_{v\in T}d(v)\le K\delta^{-6}nzU_6.                    \tag{4.19}
\]

Convexity gives

\[
 0\le w_v\le6(t_v)_+^5\le C_{A_0,K}z^5.                    \tag{4.20}
\]

The size-bias term in (4.10) is consequently at most

\[
 \sum_{v\in T}d(v)|d(v)-z|w_v
 \le Cnz^7U_6.                                               \tag{4.21}
\]

For the covariance term, Cauchy on each edge gives

\[
 W_F^2\le k_\sigma\sum_{v\in F\cap V_\sigma}w_v^2.
\]

Average over `F`, use (4.19)--(4.20), and use `Z=nz/k_sigma`:

\[
 \mathbb E_FW_F^2
 \le {k_\sigma\over Z}\sum_vd(v)w_v^2
 \le Ck_\sigma^2z^{10}U_6.                                  \tag{4.22}
\]

Equations (4.13), (4.15), and (4.22) give

\[
 Z|\operatorname {Cov}(C,W)|
 \le C Z\,z\sqrt{V_C}\,k_\sigma z^5\sqrt{U_6}.              \tag{4.23}
\]

Since `Z/n=z/k_sigma` and `c=Theta(z)`, division by `nc^6`
turns (4.23) into `Cz sqrt(V_CU_6)`.  The same division turns
(4.21) into `CzU_6`.  Multiplication by `p<=C_p/(rz)` proves
(4.17).  \(\square\)

Thus one concrete stopped route is to control `U_6` and `V_C` jointly.
The theorem is not by itself a closure: Cauchy's square-root term may be
larger than the `o(1/r)` shadow-purge budget.  It does, however, replace
the rootwise quantity `Xi_v` by two global nonnegative observables, one of
which is the already familiar sixth degree mass.

## 5. A shadow center removes the purge recentering loss

Recentring at the new average after every purge creates an additive
`rho^6` term.  It is unnecessary.  Carry a shadow center `w_sigma` as
follows.

* Initially `w_sigma=z_sigma`.
* Across a bite, multiply `w_sigma` by the same center ratio as the actual
  provisional average.
* Across a purge, leave `w_sigma` unchanged.

This definition is deterministic once the realized sequence of residuals
is given.  If a purge removes edge fraction `rho` and shore-vertex fraction
`tau_sigma`, then

\[
 {z_\sigma^\circ\over z_\sigma^*}
 ={1-\rho\over1-\tau_\sigma},\qquad
 {w_\sigma^\circ/z_\sigma^\circ
       \over w_\sigma^*/z_\sigma^*}
 ={1-\tau_\sigma\over1-\rho}.                      \tag{5.1}
\]

For the high-degree purge of Appendix C.12a,

\[
                         0\le\tau_\sigma\le{\rho\over K_0}. \tag{5.2}
\]

Hence the exact gap ledger is

\[
 \boxed{
 \log{w_{J,\sigma}\over z_{J,\sigma}}
 =\sum_{j<J}\log{1-\tau_{j,\sigma}\over1-\rho_j}
 \ge\left(1-{1\over K_0}\right)\sum_{j<J}\rho_j.}          \tag{5.3}
\]

The inequality follows by integrating `(1-s)^{-1}` from `tau` to `rho`.
There is no conditioning or expectation in (5.3).

Fix constants

\[
                         1<a<R_*a<K_0.                       \tag{5.4}
\]

The tangent identity remains favorable at the elevated center `c=aw`.
Suppose between purges that `w` is moved with the same relative annealed
rate as the actual average, so `w'/w=-B_sigma`.  Normalize the one-sided
mass by `nc^6` (equivalently by `nw^6`, up to the fixed factor `a^6`).
Repeating Theorem 3.1 with `t=d-c` gives

\[
\begin{aligned}
 nc^6\Psi_{+,c}'(0)
 ={}&\mathfrak D^+_{c,\sigma}(H)
 +(z-c)\sum_v(t_v)_+^6-\sum_v(t_v)_+^7\\
 &+B_\sigma\sum_vd(v)P_4^+(t_v)
 -\sum_vd(v)\Xi_v\nabla_+(t_v).                  \tag{5.4a}
\end{aligned}
\]

The only change in the algebra is

\[
 (z+6B-d)t_+^6-dB\nabla_+(t)+6cBt_+^5
 =(z-c)t_+^6-t_+^7+BdP_4^+(t).                    \tag{5.4b}
\]

Since `w>=z` by (5.1) and `a>1`, the new term `(z-c)sum t_+^6`
is nonpositive.  Moreover (4.6a) bounds its collision term by the existing
symmetric scalar centered at the actual average `z`; moving the shadow
threshold upward does not create a new collision cost.

While `w_sigma/z_sigma<=R_*`, define

\[
 \Phi_\sigma(H;w)
 ={1\over n_\sigma w_\sigma^6}
   \sum_{v\in V_\sigma}(d_H(v)-aw_\sigma)_+^6.              \tag{5.5}
\]

### Lemma 5.1 (fixed-shadow purge charge)

Let `H^*` be provisional, let `H^circ` be its high-degree purge, and assume
`w/z^*<=R_*`.  If `L_sigma` is the bad shore incidence and
`beta_sigma=L_sigma/Z^*`, then

\[
 \sum_{v\in B_\sigma}(d(v)-aw)_+^6
 \ge c_{a,R_*,K_0}\,w^5L_\sigma.                            \tag{5.6}
\]

Moreover, at the *same* shadow center,

\[
 \sum_{v\in V_\sigma(H^\circ)}(d_{H^\circ}(v)-aw)_+^6
 \le
 \sum_{v\in V_\sigma(H^*)}(d_{H^*}(v)-aw)_+^6
 -c_{a,R_*,K_0}w^5L_\sigma.                                \tag{5.7}
\]

Consequently, for `rho<=rho_0<1`,

\[
 \boxed{
 \Phi_\sigma(H^\circ;w)
 \le {1\over1-\rho/K_0}
 \left(\Phi_\sigma(H^*;w)-c{\beta_\sigma\over k_\sigma}
                         {z_\sigma^*\over w_\sigma}\right).} \tag{5.8}
\]

#### Proof

For a bad target, `d>K_0z^*` and `aw<=aR_*z^*`.  Thus

\[
 d-aw\ge(K_0-aR_*)z^*\ge c w,
 \qquad d-aw\ge c d.                                         \tag{5.9}
\]

Therefore `(d-aw)^6>=c w^5d`, and summation proves (5.6).
Induced deletion only lowers every surviving degree, proving (5.7).
Finally `n^circ>=n(1-rho/K_0)` and
`nw=k_sigma Z^*(w/z^*)`; division gives (5.8).  \(\square\)

Summing (5.8) over the two punctured shores, using
`beta_M+beta_L>=rho`, shows that a purge removes

\[
                              \Omega(\rho/r)                  \tag{5.10}
\]

of shadow potential, apart from the harmless multiplicative factor
`1+O(rho Phi)`.  In particular, while `Phi=o(1/r)`, that factor is absorbed
by a fixed fraction of (5.10).

### Corollary 5.2 (abstract telescope)

Suppose that, up to the stopping time `w_sigma/z_sigma=R_*`, the bites and
their concentration errors add total expected shadow potential `F_r`, and
suppose

\[
                              F_r=o(1/r).                       \tag{5.11}
\]

Assume also that the bite analysis preserves `Phi=o(1/r)` on this stopped
event.  Then

\[
 \boxed{
 \sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]
      =O(rF_r)=o(1),}                                         \tag{5.12}
\]

and the shadow-ratio stopping time is reached with probability `o(1)`.

Indeed (5.8)--(5.10) telescope until that stopping time.  If the stopping
time were reached, (5.3) would force a fixed positive cumulative `rho`,
whose potential charge is `Omega(1/r)`, contradicting (5.11) outside an
event of probability `o(1)` by Markov.  This is a stopped-event argument;
it does not condition on future persistence.

The reference collision budget from Appendix C.12 is

\[
 F_r^{\rm coll}=O(r^{-2}x_J^{-32}).                            \tag{5.13}
\]

Therefore

\[
                         rF_r^{\rm coll}
 =O(r^{-1+32\alpha})=o(1)                                    \tag{5.14}
\]

through the exact strict range `alpha<1/32`.  This explains the natural
exponent in the proposed self-correcting alternative.  It does **not**
establish (5.11) under the stopped law, because the protection term in
(4.7) remains.

## 6. Finite bites and the honest microbite reduction

For a fixed marking constant `gamma`, the tangent identity alone is not a
finite-bite theorem.  The uniform expansion in Appendix C.3quater has a
normalized remainder `O((p Delta_C)^2)` per round.  In the punctured capped
state,

\[
                         p\Delta_C=O_K(\gamma).                \tag{6.1}
\]

With fixed `gamma`, summing the displayed Taylor remainder is invalid.

There is a rigorous way to make the first-variation route honest: use a
polynomially small marking coefficient `epsilon_r` and

\[
 p_j={\epsilon_r\over r\bar d_j^M}.                            \tag{6.2}
\]

The density motion per round is `Theta(epsilon_r/r)`, so the number of
rounds is

\[
                         O(r\log r/\epsilon_r).                \tag{6.3}
\]

The aggregate Taylor remainder is then

\[
 O\left({r\log r\over\epsilon_r}\epsilon_r^2\right)
 =O(\epsilon_r r\log r).                                     \tag{6.4}
\]

Thus

\[
                         \epsilon_r=o((r^2\log r)^{-1})        \tag{6.5}

makes (6.4) `o(1/r)`, the budget required by Corollary 5.2.  The accepted
count still has exponential mean because the proved degree and shore-size
floors are exponential, so a polynomial increase in the round count does
not by itself damage the accepted-count union bound.

This reduction removes only the finite-Taylor issue.  For the actual
realized shadow center one must also include its edge-count fluctuation in
the stopped error budget.  Most importantly, (6.5) does not control
`mathcal R`; the next section shows that no cap-only argument can do so.

## 7. Collision defect zero does not imply self-correction

For an integer `d>=2`, let

\[
                         H_d=K_{d,d}\ \dot\cup\ K_{1,d}.       \tag{7.1}

Regard this as a 2-uniform, one-shore hypergraph.  It has

\[
 Z=d^2+d,\qquad n=3d+1,\qquad
 z={2d(d+1)\over3d+1}=\left({2\over3}+o(1)\right)d.           \tag{7.2}

Its maximum degree is `d`, so

\[
                         {\Delta(H_d)\over z}longrightarrow{3\over2}. \tag{7.3}

The degree floor tends to infinity.

The graph is bipartite and hence triangle-free.  If `v notin G` for an
edge `G=xy`, at most one of `vx,vy` is an edge; otherwise `vxy` is a
triangle.  Therefore

\[
                         a_G(v)\le1                               \tag{7.4}

for every external row.  Every convex row defect in (3.2) vanishes at
`a=0,1`, and consequently

\[
                 \boxed{\mathfrak D_{c}(H_d)=0
                         \quad\hbox{for every real center }c.} \tag{7.5}

Nevertheless, the exposure profile is highly nonuniform.  An edge of
`K_(d,d)` has conflict degree `2d-1`, while a star edge has conflict degree
`d`.  Hence

\[
 \bar C={2d^2\over d+1},\qquad B=\bar C-z.                    \tag{7.6}
\]

Each of the `2d` complete-bipartite vertices has `E_v=d-1`; the star
center has `E_v=0`; and each star leaf has `E_v=d-1`.

Apply the one-sided identity (4.4) at center `z`.  The `2d+1`
degree-`d` vertices have

\[
                         t=d-z=\left({1\over3}+o(1)\right)d,  \tag{7.7}

while the leaves have negative `t`.  Direct substitution gives

\[
 \Phi_+(H_d)={1\over96}+o(1),\qquad
 \boxed{\Phi_+'(0)=\left({17\over288}+o(1)\right)d>0.}       \tag{7.8}

For completeness, the leading term in the numerator is

\[
 2d\left[-{d^7\over3^7}
 +6d\,{d\over3}\,{d^5\over3^5}\right]
 ={34\over2187}d^8,                                         \tag{7.9}

and `nz^6=(64/243+o(1))d^7`, which yields `17/288`.

Thus at a marking scale `p=Theta(1/z)`, the normalized upper sixth mass
has a positive constant first-order change even though the collision
forcing is exactly zero.  The positive term is precisely the negative
rooted-exposure/protection covariance in (4.4).

This example does not claim that `H_d` embeds as a stopped punctured
residual.  It rules out the proposed **formal** implication

\[
 \text{degree cap + large degree + small }\mathfrak D
 \quad\Longrightarrow\quad\text{sixth-mass self-correction}. \tag{7.10}

Any proof in the punctured system must establish an additional geometric
bound which fails for (7.1).

## 8. Exact remaining stopped statement for this route

For a post-purge punctured state, use a shadow center `w_(j,sigma)` and a
fixed `a>1` as in Section 5.  Define the corresponding one-sided rooted
exposure quantities with center `aw_(j,sigma)`.  A sufficient
first-variation input is

\[
 \sum_{j,\sigma}\mathbb E\left[\mathbf1_{\mathcal G_j}
 {p_j\over n_{j,\sigma}w_{j,\sigma}^6}
 \left(
   \mathfrak D_{z_{j,\sigma},\sigma}(H_j)
  +\mathcal R_{aw_{j,\sigma},\sigma}(H_j)
 \right)\right]=o(1/r).                                    \tag{8.1}
\]

The cross-center inequality (4.6a) is why the symmetric collision scalar
already studied in Appendix C.12, centered at the *actual* average,
dominates the one-sided shadow-center collision part.  The genuinely new part is
`mathcal R`, or any stronger theorem which absorbs it into the negative
seventh moment.  Together with a summable finite-bite/realized-center error,
(8.1) and the shadow telescope prove

\[
                         \sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]
                         =o(1).                     \tag{8.2}

Thus the self-correcting experiment has a precise outcome.

* It can merge the purge-loss task into a Lyapunov telescope and naturally
  recovers the strict exponent `alpha<1/32`.
* It cannot close from the centered collision scalar alone.
* The missing statistic is the stopped high-degree/low-exposure alignment
  (4.7), plus a finite-bite realized-center remainder if the original fixed
  marking constant is retained.

The companion-degree identity

\[
 E_v={1\over d(v)}\sum_{F\ni v}
 \left(\sum_{u\in F-\{v\}}d(u)-\mathfrak E(F)\right)          \tag{8.3}
\]

shows where punctured geometry could enter: one must prove that a target in
the upper tail cannot simultaneously have an atypically small average
companion-degree/duplicate-excess exposure.  That is narrower than a full
state comparison and strictly stronger than the existing collision scalar.
