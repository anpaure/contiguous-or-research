# Gate B: Palm collision, entropy, and the late-protection obstruction

**Date:** 2026-08-22  
**Status:** unconditional reduction and generic obstruction.  This note does
**not** prove the positive Gate-B tail.  It proves that such a tail would
force an \(\Omega(1/x)\) external-window collision multiplier and
\(\Omega(\log(1/x))\) relative entropy.  It gives an exact one-round
recursion for that collision multiplier, identifies its two possible growth
terms, and shows from the accepted-hit likelihood that qualifying terminal
holes must acquire their protection late or intermittently.  Finally, an
empty-conflict stochastic model shows that the stopped Palm identities,
their conservation law, and the hit compensator do not by themselves force
any positive protection tail.  Additional punctured geometry is essential.
Sections 1--6 are self-contained.  Section 7 explicitly imports the proved
mixed-root gap and complete pair-profile estimates (7.4)--(7.5), which are
restated there; its planting conclusions are unconditional given those
separately established punctured-geometry theorems.

## 1. Terminal external-window Palm law

Fix one tagged depth.  Let \(\mathcal T\) be its target layer and put

\[
 N=|\mathcal T|.
\]

Let \(\mathcal C\) be a nonempty labelled catalogue of \(Z\) cyclic rows.
Every row has exactly \(b\) distinct windows in \(\mathcal T\).  For
\(T\in\mathcal T\), put

\[
 X(T)=|\{F\in\mathcal C:T\text{ is a window of }F\}|,
 \qquad
 \pi(T)={X(T)\over bZ}.                             \tag{1.1}
\]

Then

\[
 \sum_TX(T)=bZ,
 \qquad
 \sum_T\pi(T)=1.                                  \tag{1.2}
\]

In the complete initial labelled catalogue the law in (1.1) is uniform.
For a nested residual catalogue \(\mathcal C_j\), write \(Z_j,X_j,\pi_j\)
for the corresponding quantities and put

\[
 \mathcal S_j(T)=\{F\in\mathcal C_j:T\text{ is a window of }F\},
 \qquad X_j(T)=|\mathcal S_j(T)|.                   \tag{1.2a}
\]

Define

\[
 L_j(T)=N\pi_j(T),\qquad
 \mathscr P_j(T)=\log L_j(T),                       \tag{1.3}
\]

with \(\mathscr P_j(T)=-\infty\) when \(X_j(T)=0\).  Thus

\[
 \sum_Te^{\mathscr P_j(T)}=N.                      \tag{1.4}
\]

For the punctured application,

\[
 b=2r+1,qquad A={b\choose r},\qquad B=A/b,
 \qquad N=B_q={b\choose {r-q}}.                    \tag{1.5}
\]

Fix \(x\in(0,1]\) and \(K>0\).  If every terminal survivor is given common
weight \(KxB/Z\), then a target
is covered to level one precisely when

\[
 X(T)\ge {Z\over KxB},
 \quad\hbox{equivalently}\quad
 \pi(T)\ge {1\over KxA},
 \quad\hbox{equivalently}\quad
 L(T)\ge {N\over KxA}.                             \tag{1.6}
\]

The point of this note is to quantify how nonuniform the Palm law must be
if (1.6) holds on a capacity-sized hole set.

## 2. Collision and entropy forced by a Gate-B floor

Define the external-window collision multiplier

\[
 \boxed{
 \mathcal K(\pi)=N\sum_{T\in\mathcal T}\pi(T)^2
 ={1\over N}\sum_Te^{2\mathscr P(T)}.}             \tag{2.1}
\]

It equals one for the uniform law.  Let

\[
 \overline X={bZ\over N}.
\]

### Theorem 2.1 (exact collision forcing)

Suppose a set \(G\subseteq\mathcal T\), \(|G|=g\), satisfies the
survivor floor (1.6).  Then

\[
 \boxed{
 \mathcal K(\pi)\ge {Ng\over K^2x^2A^2}.}          \tag{2.2}
\]

Moreover

\[
 \boxed{
 \mathcal K(\pi)
 =1+{1\over N}\sum_T
       \left({X(T)-\overline X\over\overline X}\right)^2.}    \tag{2.3}
\]

Consequently, if \(N/A\ge c_1>0\) and \(g\ge c_0xA\), then

\[
 \boxed{
 \mathcal K(\pi)\ge {c_0c_1\over K^2x}.}          \tag{2.4}
\]

Thus Gate B requires squared coefficient of variation
\(\Omega(1/x)\), not ordinary external-degree regularity.

#### Proof

For every \(T\in G\), (1.6) gives
\(\pi(T)^2\ge1/(K^2x^2A^2)\).  Sum over \(G\) and multiply by \(N\)
to obtain (2.2).  Also

\[
 \mathcal K(\pi)
 ={1\over N}\sum_T\left({X(T)\over\overline X}\right)^2.
\]

The average of \(X(T)/\overline X\) is one, so expanding the square about
one proves (2.3).  Equation (2.4) is immediate from (2.2). \(\square\)

There is an exact pair interpretation.  For two labelled rows \(F,G\),
let

\[
 c(F,G)=|\{T\in\mathcal T:T\text{ is a window of both }F\text{ and }G\}|.
                                                               \tag{2.5}
\]

Then \(c(F,F)=b\), and double counting ordered triples \((T,F,G)\)
gives

\[
 \boxed{
 \mathcal K(\pi)
 ={N\over b^2Z^2}\sum_{F,G\in\mathcal C}c(F,G).}   \tag{2.6}
\]

Hence the positive Gate-B tail is equivalently a factor-\(1/x\) excess of
two-survivor common shallow windows.

### Theorem 2.2 (relative-entropy forcing)

Let \(u\) be the uniform law on \(\mathcal T\), put

\[
 a={g\over N},\qquad m_0={g\over KxA},qquad
 t={N\over KxA},                                  \tag{2.7}
\]

and assume \(0<a\le m_0\le1\).  Under the hypotheses of Theorem 2.1, use
the standard convention `0 log 0=0`.  Then

\[
 \boxed{
 D(\pi\Vert u)
 \ge m_0\log{m_0\over a}
 +(1-m_0)\log{1-m_0\over1-a}.}                   \tag{2.8}
\]

In particular,

\[
 \boxed{
 D(\pi\Vert u)\ge m_0\log t-(m_0-a).}            \tag{2.9}
\]

If \(N/A=1+O(x)\), \(g\ge c_0xA\), and \(K,c_0\) are fixed, then

\[
                         D(\pi\Vert u)=\Omega(\log(1/x)).       \tag{2.10}
\]

#### Proof

By (1.6), \(\pi(G)\ge m_0\).  Coarsen both \(\pi\) and \(u\) to the
two cells \(G,\mathcal T-G\).  The log-sum inequality gives

\[
 D(\pi\Vert u)\ge
 d(\pi(G)\Vert a),                                \tag{2.11}
\]

where

\[
 d(m\Vert a)=m\log(m/a)+(1-m)\log((1-m)/(1-a)).
\]

For \(m\ge a\), its derivative in \(m\) is
\(\log(m(1-a)/(a(1-m)))\ge0\).  Thus (2.11) is at least
\(d(m_0\Vert a)\), proving (2.8).  Since \(m_0/a=t\), and, for
\(m_0<1\),

\[
 (1-m_0)\log{1-m_0\over1-a}
 =-(1-m_0)\int_a^{m_0}{ds\over1-s}
 \ge-(m_0-a),                                     \tag{2.12}
\]

(2.9) follows.  The endpoint \(m_0=1\) follows by continuity.  The final assertion uses
\(m_0\ge c_0/K\) and \(\log t=\log(1/x)-O_K(1)\). \(\square\)

### Corollary 2.3 (band form)

Let \(i\) range over any collection of tagged depths and shores, with
target populations \(N_i\ge c_1A\).  Normalize a Palm law \(\pi_i\)
separately on every layer.  If the survivor floor (1.6) holds on \(g_i\)
targets in layer \(i\), then

\[
 \boxed{
 \sum_i\mathcal K(\pi_i)
 \ge {c_1\over K^2x^2A}\sum_i g_i.}               \tag{2.13}
\]

In particular, \(\sum_i g_i\ge c_0xAQ\) forces average collision
multiplier \(\Omega(1/x)\) across the \(Q\) layers.

This is the form relevant when the allowed exceptional set is only
\(o(A)\) in aggregate.  In the range \(xQ\to\infty\), an \(o(A)\)
exception removes only \(o(xAQ)\) of the capacity-sized band.

There is also a floor-free formulation which isolates alignment itself.

### Theorem 2.4 (sharp hole-Palm collision inequality)

Let \(H\subseteq\mathcal T\), put

\[
 a={|H|\over N},\qquad R=\pi(H),                  \tag{2.14}
\]

and assume \(0<a<1\).  Then

\[
 \boxed{
 \mathcal K(\pi)
 \ge {R^2\over a}+{(1-R)^2\over1-a}
 =1+{(R-a)^2\over a(1-a)}.}                       \tag{2.15}
\]

Equality holds exactly when \(\pi\) is constant on \(H\) and constant on
its complement.  More precisely, if

\[
 \mathcal K_H=|H|\sum_{T\in H}\left({\pi(T)\over R}\right)^2,
 \qquad
 \mathcal K_{H^c}=|H^c|\sum_{T\notin H}
                 \left({\pi(T)\over1-R}\right)^2,              \tag{2.16}
\]

with the zero-mass terms omitted, then the exact decomposition is

\[
 \boxed{
 \mathcal K(\pi)
 ={R^2\over a}\mathcal K_H
 +{(1-R)^2\over1-a}\mathcal K_{H^c}.}             \tag{2.17}
\]

In particular, if \(a=\Theta(x)\) and \(R=\Omega(1)\), then
\(\mathcal K(\pi)=\Omega(1/x)\), even without a pointwise survivor
floor.

#### Proof

Split the sum in (2.1) over \(H,H^c\) and factor out the two total masses;
this is (2.17).  Cauchy--Schwarz gives
\(\mathcal K_H,\mathcal K_{H^c}\ge1\), with equality exactly for the
two uniform conditional laws.  This proves the first expression in
(2.15).  Expanding it gives the second. \(\square\)

Thus the ideal capacity vortex is the sharp extremizer: Palm mass one,
uniformly distributed on an \(xN\)-element hole set, has
\(\mathcal K=1/x\).  Any nonuniformity inside that set costs still more
collision mass.

## 3. Exact escort recursion for collision growth

Return to a nested catalogue \(\mathcal C_j\).

All transitions in this section are between nonempty catalogues, so
`Z_j>0` and `Z_(j+1)>0`.  The terminal index `tau` used below is a bounded
stopping time and the catalogues remain nonempty through `tau`.  These are
the exact hypotheses needed for every Palm normalization and telescoping
identity.

Put

\[
 d_j=1-{Z_{j+1}\over Z_j},
 \qquad
 d_j(T)=1-{X_{j+1}(T)\over X_j(T)}                 \tag{3.1}
\]

when \(X_j(T)>0\).  Empty stars have \(\pi_j(T)=0\) and may be omitted.
Define the normalized relative-loss increment

\[
 \zeta_j(T)={d_j-d_j(T)\over1-d_j}.                \tag{3.2}
\]

Then the exact Palm replicator identity is

\[
 \pi_{j+1}(T)=\pi_j(T)(1+\zeta_j(T)),
 \qquad
 \sum_T\pi_j(T)\zeta_j(T)=0.                     \tag{3.3}
\]

Let

\[
 \mathcal K_j=N\sum_T\pi_j(T)^2,qquad
 \rho_j(T)={\pi_j(T)^2\over\sum_S\pi_j(S)^2},
 \qquad L_j(T)=N\pi_j(T).                         \tag{3.4}
\]

The probability law \(\rho_j\) is the order-two escort of the Palm law.

### Theorem 3.1 (collision transport identity)

For every round,

\[
 \boxed{
 {\mathcal K_{j+1}\over\mathcal K_j}
 =\mathbb E_{\rho_j}(1+\zeta_j)^2
 =1+2\mathbb E_{\rho_j}\zeta_j
       +\mathbb E_{\rho_j}\zeta_j^2.}             \tag{3.5}
\]

Equivalently,

\[
 \boxed{
 \mathcal K_{j+1}-\mathcal K_j
 =2\operatorname {Cov}_{\pi_j}(L_j,\zeta_j)
  +\mathbb E_{\pi_j}[L_j\zeta_j^2].}              \tag{3.6}
\]

If \(\pi_0=u\), then \(\mathcal K_0=1\) and the first-round covariance
term vanishes exactly:

\[
                         \mathcal K_1
 =1+\mathbb E_u\zeta_0^2.                         \tag{3.7}
\]

#### Proof

Square (3.3), sum over \(T\), and divide by
\(\sum_T\pi_j(T)^2\) to obtain (3.5).  Also

\[
\begin{aligned}
 \mathcal K_{j+1}-\mathcal K_j
 &=N\sum_T\pi_j(T)^2(2\zeta_j(T)+\zeta_j(T)^2)\\
 &=2\mathbb E_{\pi_j}[L_j\zeta_j]
   +\mathbb E_{\pi_j}[L_j\zeta_j^2].             \tag{3.8}
\end{aligned}
\]

The second identity in (3.3) makes
\(\mathbb E_{\pi_j}[L_j\zeta_j]
=\operatorname {Cov}_{\pi_j}(L_j,\zeta_j)\), proving (3.6).
At time zero, \(L_0\equiv1\), so the covariance is zero and (3.7)
follows. \(\square\)

The two terms in (3.6) have distinct meanings.  The covariance is a
rich-get-richer drift: targets already carrying high Palm mass must be
preferentially spared by the next blocker deletion.  The second term is
quadratic relative-loss energy.  Linear loss balance alone cancels under
\(\pi_j\) and cannot grow the collision multiplier in the first round.

### Corollary 3.2 (exact escort-energy gate)

Put

\[
 \mathcal A_j=
 2(\mathbb E_{\rho_j}\zeta_j)_+
 +\mathbb E_{\rho_j}\zeta_j^2.                   \tag{3.9}
\]

Then

\[
 \boxed{
 \log\mathcal K_\tau\le\sum_{j<\tau}\mathcal A_j.}           \tag{3.10}
\]

Consequently the capacity-sized Gate-B floor of Theorem 2.1 forces

\[
 \boxed{
 \sum_{j<\tau}\mathcal A_j
 \ge\log(1/x)-O_{K,c_0,c_1}(1).}                 \tag{3.11}
\]

#### Proof

Equation (3.5) gives

\[
 {\mathcal K_{j+1}\over\mathcal K_j}
 \le1+\mathcal A_j.
\]

Take logarithms, use \(\log(1+s)\le s\), and telescope.  Combine with
(2.4) for (3.11). \(\square\)

The first-blocker partition makes (3.9) completely explicit.  If accepted
configurations \(G\) have disjoint deletion cells \(\mathcal B_j(G)\), then

\[
 d_j={\sum_G|\mathcal B_j(G)|\over Z_j},
 \qquad
 d_j(T)={\sum_G|\mathcal B_j(G)\cap\mathcal S_j(T)|\over X_j(T)}.
                                                               \tag{3.12}
\]

Thus (3.9) is an escort-weighted row/target/blocker statistic.  An upper
bound \(o(\log(1/x))\) for its stopped sum would rigorously rule out the
full-survivor Gate-B route.  A lower bound of the required order, aligned
with terminal holes, would be genuine positive progress.

## 4. Exact hole-Palm transport

Let \(U_j(T)\) indicate that no accepted row before round \(j\) contains
\(T\), and put

\[
 R_j=\sum_TU_j(T)\pi_j(T).                         \tag{4.1}
\]

Thus \(R_j\) is the Palm mass of the targets which are still unhit.  Write

\[
 H_j(T)=U_j(T)-U_{j+1}(T)\in\{0,1\}.              \tag{4.2}
\]

### Proposition 4.1 (alignment transport identity)

Pathwise,

\[
 \boxed{
 R_{j+1}-R_j
 =\sum_TU_{j+1}(T)\pi_j(T)\zeta_j(T)
  -\sum_TH_j(T)\pi_j(T).}                         \tag{4.3}
\]

Equivalently,

\[
 R_{j+1}-R_j
 =\sum_TU_j(T)\pi_j(T)\zeta_j(T)
  -\sum_TH_j(T)\pi_j(T)(1+\zeta_j(T)).            \tag{4.4}
\]

#### Proof

Substitute \(\pi_{j+1}=\pi_j(1+\zeta_j)\) and
\(U_j=U_{j+1}+H_j\) into \(R_{j+1}-R_j\).  This gives (4.3);
substituting \(U_{j+1}=U_j-H_j\) gives (4.4). \(\square\)

At time zero, \(R_0=1\).  A uniform terminal Palm law would give
\(R_\tau=|\mathcal H|/N=\Theta(x)\).  A successful capacity-sized
Gate-B floor instead gives \(R_\tau=\Omega(1)\).  Equations (4.3)--(4.4)
show the exact required compensation: blocker reweighting of the still-unhit
set must offset the Palm mass removed by accepted hits.  Neither the
unweighted conservation (1.4) nor a marginal bound for \(X_j(T)\) controls
this signed transport.

## 5. Accepted-hit likelihood forces late or intermittent protection

Suppose round \(j\) marks each current configuration independently with
probability \(p_j\), accepts isolated marks in a conflict graph of maximum
degree \(\Delta_j\), and

\[
 p_j\le\tfrac12,qquad p_j\Delta_j\le\beta.        \tag{5.1}
\]

For an unhit target \(T\), let \(a_j(T)\) be the conditional probability
that at least one accepted configuration belongs to its current external
star.  The standard isolated-mark second-moment bound gives

\[
 a_j(T)\ge \kappa{u_j(T)\over1+u_j(T)},
 \qquad
 \kappa=e^{-4\beta},qquad
 u_j(T)=p_jX_j(T).                                 \tag{5.2}
\]

For self-containment, let `K_j(T)` count isolated marked configurations in
the star.  Conditionally on the current catalogue,

\[
 e^{-2\beta}u_j(T)\le
 \lambda_j(T):=\mathbb E K_j(T)
 =\sum_{F\in\mathcal S_j(T)}p_j(1-p_j)^{\deg(F)}
 \le u_j(T),                                       \tag{5.2a}
\]

because `log(1-p)>=-2p` on `[0,1/2]`.  Conflicting rows cannot both be
isolated marks, while a nonconflicting pair is simultaneously isolated with
probability at most `p_j^2`.  Hence

\[
 \mathbb E K_j(T)^2\le\lambda_j(T)+u_j(T)^2.       \tag{5.2b}
\]

The second-moment inequality gives
`a_j(T)>=lambda_j(T)^2/E[K_j(T)^2]`, which is (5.2); the upper bound
`a_j(T)<=min(1,u_j(T))` follows from the union bound.  Thus no external
hit lemma is being assumed here.

Define the base Palm intensity and protected occupation by

\[
 \lambda_j={p_jbZ_j\over N},
 \qquad
 \mathcal O_\tau(T)=
 \sum_{j<\tau}{\lambda_jL_j(T)\over1+\lambda_jL_j(T)}.         \tag{5.3}
\]

The identity \(X_j/Z_j=(b/N)L_j\) gives
\(u_j=\lambda_jL_j\).

### Theorem 5.1 (protected-occupation tail)

For every fixed target, every bounded stopping time `tau` satisfying the
nonemptiness convention of Section 3, and every \(s\ge0\),

\[
 \boxed{
 \Pr\bigl(U_\tau(T)=1,\ \mathcal O_\tau(T)\ge s\bigr)
 \le e^{-\kappa s}.}                              \tag{5.4}
\]

Consequently, for any \(\delta>0\), with

\[
 s_x={1+\delta\over\kappa}\log(1/x),              \tag{5.5}
\]

the expected number of terminal holes satisfying
\(\mathcal O_\tau(T)\ge s_x\) is at most \(Nx^{1+\delta}\).  With
probability at least \(1-x^{\delta/2}\), their number is at most

\[
                         Nx^{1+\delta/2}=o(xN).     \tag{5.6}
\]

#### Proof

On an unhit path, the exact likelihood martingale is

\[
 U_n(T)\exp\left\{\sum_{j<n}-\log(1-a_j(T))\right\}.
                                                               \tag{5.7}
\]

It has mean one.  Indeed, the event that no current row is marked has
positive conditional probability, so `a_j(T)<1`, and multiplication by
`(1-a_j(T))^{-1}` exactly compensates the next no-hit indicator.  Bounded
optional stopping preserves the mean.  Since \(-\log(1-a)\ge a\), (5.2)
implies that the exponent in (5.7) is at least
\(\kappa\mathcal O_\tau(T)\).  Markov's
inequality proves (5.4).  Sum (5.4) over the \(N\) targets and use (5.5).
One more application of Markov at threshold \(Nx^{1+\delta/2}\) proves
(5.6). \(\square\)

There is a concrete late-protection consequence for the punctured schedule.
Fix \(\gamma>0\) and suppose

\[
 p_j={\gamma|M_j|\over2r^2Z_j},qquad
 {|M_j|\over A}={rx_j+2\over r+2},                \tag{5.8}
\]

where `M_j` is the current middle target shore.  Use the Gate-B threshold

\[
                         t={N\over KxA}.            \tag{5.9}
\]

For \(R\ge1\), let

\[
 J_R(T)=\{j<\tau:x_j\ge Rx,\ L_j(T)\ge t\}.       \tag{5.10}
\]

### Corollary 5.2 (late/intermittent threshold occupation)

For every target,

\[
 \boxed{
 \mathcal O_\tau(T)
 \ge |J_R(T)|\,{a_R\over1+a_R},
 \qquad a_R={\gamma R\over2Kr}.}                  \tag{5.11}
\]

Therefore, on the event of probability at least `1-x^(delta/2)` in (5.6),
all but at most `Nx^(1+delta/2)=o(xN)` terminal holes satisfy

\[
 \boxed{
 |J_R(T)|
 \le {1+\delta\over\kappa}\log(1/x)
       \left(1+{2Kr\over\gamma R}\right).}       \tag{5.12}
\]

#### Proof

For \(j\in J_R(T)\), equations (5.3), (5.8), and (5.9) give

\[
\begin{aligned}
 \lambda_jL_j(T)
 &\ge {p_jbZ_j\over N}{N\over KxA}\\
 &= {\gamma b\over2Kr^2x}{|M_j|\over A}\\
 &\ge {\gamma b\over2Kr(r+2)}{x_j\over x}
 \ge {\gamma R\over2Kr}=a_R.                     \tag{5.13}
\end{aligned}
\]

Here \(b=2r+1\ge r+2\) for \(r\ge1\).  Every such round contributes at
least \(a_R/(1+a_R)\) to (5.3), proving (5.11).  Combine (5.11) with
(5.5)--(5.6) to obtain (5.12). \(\square\)

Thus a capacity-sized family of successful terminal holes cannot remain at
the full Gate-B degree threshold for long while the residual density is much
larger than its terminal value.  Its \(\log(1/x)\) protection must be built
near the end of the descent, or by intermittent bursts.  A proof excluding
such late bursts would rule out the uniform-survivor cover; a proof creating
them in the punctured geometry would be the missing positive theorem.

### Proposition 5.3 (the capacity-critical constant is exactly one)

The preceding occupation bound is sharp at the level of the Palm dynamics.
Let

\[
 \mathcal T=H_0\supseteq H_1\supseteq\cdots\supseteq H_\tau,
 \qquad |H_j|=x_jN,qquad x_0=1,                  \tag{5.14}
\]

where every displayed cardinality is an integer, and suppose

\[
 U_j=\mathbf1_{H_j},qquad
 \pi_j(T)={\mathbf1_{H_j}(T)\over x_jN}.           \tag{5.15}
\]

Then, identically,

\[
 L_j(T)={1\over x_j},\quad
 \mathscr P_j(T)=\log(1/x_j)\quad(T\in H_j),       \tag{5.16}
\]

\[
 \mathcal K_j={1\over x_j},qquad R_j=1.          \tag{5.17}
\]

If, conditionally on membership in \(H_j\), the next nested set retains a
fixed target with probability \(x_{j+1}/x_j\), then its accepted-hit hazard
is

\[
 a_j=1-{x_{j+1}\over x_j},                        \tag{5.18}
\]

and the exact no-hit likelihood is

\[
 \prod_{j<\tau}(1-a_j)=\prod_{j<\tau}{x_{j+1}\over x_j}=x_\tau.           \tag{5.19}
\]

Thus the cumulative hazard exponent is exactly
\(-\log x_\tau\), with coefficient one.

#### Proof

Equations (5.16)--(5.17) are direct substitutions in (1.3), (2.1), and
(4.1).  Equation (5.18) is the stated conditional retention probability,
and (5.19) telescopes. \(\square\)

At the first punctured shadow, the exact support half of this model holds:
surviving configurations use only unused central targets.  Uniformity on
that support is a further degree statement, not an automatic identity.
Gate B asks for an approximate copy of the full (5.14)--(5.17) picture
simultaneously at deeper shallow ranks.  At the punctured marking scale,
\(\lambda_jL_j\asymp(\gamma x_j/r)(1/x_j)=\gamma/r\); the number of
rounds per logarithmic density unit is \(\Theta(r/\gamma)\).  Proposition
5.3 explains why the accepted-hit/no-hit balance is capacity-critical rather
than contradictory.  Matching the two implicit constants in the actual
conflict geometry is itself part of the missing theorem.

## 6. A stochastic countermodel to identities-only arguments

The preceding restrictions still do not force a positive tail.  The
following model satisfies the exact Palm conservation, replicator dynamics,
accepted-hit likelihood, and one-sided loss cap, but typically has
\(\Theta(xN)\) holes with \(o(1)\) protection and collision multiplier
\(1+o(1)\).

Let \(\Lambda\to\infty\), put \(x=e^{-\Lambda}\), and choose integers
\(D,N\) such that

\[
 {\Lambda^2\over D}\longrightarrow0,
 \qquad Nx\longrightarrow\infty.                 \tag{6.1}
\]

There are \(N\) targets.  For each target \(T\), create \(D\) labelled
configurations \((T,1),\ldots,(T,D)\), each having the single window
\(T\); thus this is the case \(b=1\).  Let the conflict graph be empty.
In one round mark every configuration independently with probability

\[
                         p={\Lambda\over D}.        \tag{6.2}
\]

Every mark is isolated and accepted, and only the marked configurations
are deleted.  If \(M_T\sim\operatorname {Bin}(D,p)\), then

\[
 X_1(T)=D-M_T,qquad
 U_1(T)=\mathbf1_{\{M_T=0\}}.                     \tag{6.3}
\]

The variables \(M_T\) are independent.  Hence, with probability tending
to one,

\[
 {1\over N}\sum_TU_1(T)
 =(1-p)^D+o(1)=x(1+o(1)),                          \tag{6.4}
\]

and

\[
 {Z_1\over Z_0}=1-p+o(p).                         \tag{6.5}
\]

For every terminal hole, \(X_1(T)/X_0(T)=1\).  Therefore

\[
 e^{\mathscr P_1(T)}
 ={X_1(T)/X_0(T)\over Z_1/Z_0}
 ={1\over1-p+o(p)}=1+o(1),                        \tag{6.6}
\]

whereas the Gate-B threshold is of order \(1/x=e^\Lambda\).  Also the
law of large numbers gives

\[
 \mathcal K_1
 ={\mathbb E[(D-M_T)^2]\over(\mathbb E[D-M_T])^2}+o(1)
 =1+{Dp(1-p)\over D^2(1-p)^2}+o(1)
 =1+o(1).                                         \tag{6.7}
\]

The global catalogue loss is \(d_0=p+o(p)=o(1)\), so in particular it is
below \(1/8\).  The accepted-hit probability of a target is exactly
\(1-(1-p)^D=1-x(1+o(1))\), and the no-hit probability is exactly the
likelihood predicted by the martingale.  Conservation (1.4) holds
identically for every realized outcome, not merely asymptotically.

This countermodel does not imitate the punctured conflict geometry, and is
not claimed to do so.  Its role is logical: no theorem based only on the
replicator identity, \(\sum e^{\mathscr P}=N\), the accepted-hit
compensator, and a global loss cap can force Gate B.  Such a theorem must
use a property absent from the empty graph, for example punctured
first-blocker geometry or a direct all-depth selection rule.

## 7. Planted reserve/vortex audit

A natural attempt is to choose \(s=\Theta(xB)\) pairwise core-disjoint
reserve rows, forbid the main matching from using their punctured central
targets, and append the reserve at the end.  This section records what that
operation proves exactly and why the direct planting signal is too small at
depth at least two.

Here the complete labelled catalogue `C_0` consists of all directed words
on `[2r+1]`.  For a word `F`, `E(F)` is its tagged punctured deck of the
`2r` retained `r`-windows and `2r` retained `(r-1)`-windows.  Two words
conflict when their `E`-decks intersect, `N[G]` is the closed conflict
neighbourhood of `G`, and `Omega_q(T)` is the set of complete words having
the fixed length-`(r-q)` set `T` as a full cyclic window.  These definitions
make every probability below local to this note.

Let \(\mathcal U_R\) be the union of the punctured central targets of a
fixed reserve \(R\).  Let \(\mathcal C_0\) be the complete labelled
configuration catalogue and

\[
 \mathcal C^R=\{F\in\mathcal C_0:E(F)\cap\mathcal U_R=\varnothing\}.
                                                               \tag{7.1}
\]

Write \(Z^R=|\mathcal C^R|\), and for a shallow target \(T\), write
\(X^R(T)\) for its external-star size in \(\mathcal C^R\).  If \(F\) is
uniform in \(\mathcal C_0\), put

\[
 \mathsf A_R=\{E(F)\cap\mathcal U_R=\varnothing\},qquad
 \mathsf W_T=\{T\text{ is a full-row window of }F\}.           \tag{7.2}
\]

### Proposition 7.1 (exact planted likelihood ratio)

Whenever the displayed probabilities are positive,

\[
 \boxed{
 \log{X^R(T)/X_0(T)\over Z^R/Z_0}
 =\log{\Pr(\mathsf A_R\mid\mathsf W_T)\over\Pr(\mathsf A_R)}.}             \tag{7.3}
\]

If the subsequent main descent starts from \(\mathcal C^R\), its total
relative protection with respect to the complete catalogue is the sum of
the planted log-likelihood in (7.3) and the later stopped relative-protection
increments.

#### Proof

Uniform counting gives

\[
 {Z^R\over Z_0}=\Pr(\mathsf A_R),qquad
 {X^R(T)\over X_0(T)}=\Pr(\mathsf A_R\mid\mathsf W_T).
\]

Their quotient proves (7.3).  The additive assertion is telescoping of the
two successive survival ratios. \(\square\)

For one planted row the likelihood signal is quantitatively small.  We use
the separately proved mixed-root gap estimate for the directed
punctured-configuration hypergraph: uniformly for
\(2\le q\le\sqrt r/4\), if \(G\) is a fixed
configuration and \(T\) is a length-\((r-q)\) full-row window of \(G\),
then

\[
 {|N[G]\cap\Omega_q(T)|\over|\Omega_q(T)|}=O(1/r).             \tag{7.4}
\]

For clarity, (7.4) is the direct boundary-gap count: among the central
targets of \(G\), the boundedly many boundary edges meeting an endpoint of
the external root cost \(O(1/r)\), and each of the other \(O(r)\) edges
uses four distinct cuts and costs \(O(1/r^2)\).  A union bound over the
central targets gives (7.4).  The exact punctured pair profile also gives

\[
 {|N[G]|\over|\mathcal C_0|}=O(r^2/A)=e^{-\Omega(r)}.           \tag{7.5}
\]

### Proposition 7.2 (one-row planting is only an \(O(1/r)\) tilt)

Delete the closed conflict neighbourhood of one planted configuration
\(G\), and let \(T\) be as in (7.4).  Then

\[
 \boxed{
 \left|\log{X^{\{G\}}(T)/X_0(T)\over
                  Z^{\{G\}}/Z_0}\right|=O(1/r).}               \tag{7.6}
\]

#### Proof

Put

\[
 \theta_T={|N[G]\cap\Omega_q(T)|\over|\Omega_q(T)|},qquad
 \theta={|N[G]|\over|\mathcal C_0|}.
\]

The ratio in (7.6) is \((1-\theta_T)/(1-\theta)\).  Equations
(7.4)--(7.5) give \(\theta_T=O(1/r)\) and
\(\theta=e^{-\Omega(r)}\).  Since \(|\log(1-z)|\le2z\) for
\(0\le z\le1/2\), (7.6) follows. \(\square\)

At one fixed rank, an \(s=xB\) reserve has only

\[
                         sb=xA                                \tag{7.7}
\]

indexed shallow windows.  If their distinct union has the required
\(\Theta(xA)\) size, its average planted multiplicity is \(\Theta(1)\).
Proposition 7.2 therefore shows that the direct, target-naming contribution
of the reserve is only \(O(1/r)\) per typical reserved target, not
\(\Theta(\log(1/x))\).  A purely additive use of these one-row tilts would
need \(\Theta(r\log(1/x))\) repetitions per target, consuming the same
factor in occurrence capacity and leaving too few distinct reserved
targets.  This additive observation does not exclude nonlinear collective
conditioning by the rest of the reserve.

This does not rule out a collective effect from reserve rows not containing
\(T\).  It identifies the exact extra theorem such a vortex construction
would need: a globally correlated reserve whose avoidance likelihood in
(7.3) separates its entire shallow-window union from the complement, while
using only \(xA\) occurrences per rank.

The same mixed-root estimate shows that ordinary central compatibility does
not itself suppress deeper-window collisions.

### Proposition 7.3 (a uniform compatible pair retains the mean-one collision)

Let \(F\) be a fixed directed punctured configuration and let \(G\) be
uniform in the complete labelled catalogue, conditioned on
\(E(F)\cap E(G)=\varnothing\).  For
\(2\le q\le\sqrt r/4\), let \(c_q(F,G)\) be the number of common
length-\((r-q)\) full-row windows.  Then

\[
 \boxed{
 \mathbb E[c_q(F,G)\mid E(F)\cap E(G)=\varnothing]
 =\left(1+O(1/r)\right){b^2\over B_q}.}            \tag{7.8}
\]

The complementary upper statement is identical.

#### Proof

The row \(F\) has \(b\) distinct targets \(T\) at this rank.  A uniform
labelled configuration contains any fixed \(T\) with probability
\(b/B_q\).  Therefore, without conditioning,

\[
                         \mathbb E c_q(F,G)={b^2\over B_q}.     \tag{7.9}
\]

For each one of the \(b\) windows \(T\) of \(F\), equation (7.4) says
that only an \(O(1/r)\) fraction of the configurations containing \(T\)
conflict with \(F\).  Summing over the windows gives

\[
 \mathbb E[c_q(F,G)\mathbf1_{\{E(F)\cap E(G)\ne\varnothing\}}]
 =O(1/r){b^2\over B_q}.                            \tag{7.10}
\]

Finally, (7.5) gives
\(\Pr(E(F)\cap E(G)\ne\varnothing)=e^{-\Omega(r)}\).
Divide (7.9) minus (7.10) by the compatibility probability. \(\square\)

Thus a uniformly chosen compatible pair still has essentially the
unconditioned shallow collision rate.  A near-rainbow all-depth matching
must impose a global correlation far stronger than pairwise central
compatibility.  Proposition 7.3 is not an impossibility theorem for such a
correlated matching, nor does it assert that the stopped nibble has the
uniform-compatible pair law.

Nor does the existing boundary-codegree theorem automatically preserve
Gate A after conditioning on \(R\).  Pair-codegree bounds are hereditary,
but the required maximum-to-average degree cap is not: deleting a structured
union of target stars can reduce the average much more than a surviving
maximum.  A random or pseudorandom reserve would require a separate
concentration theorem for \(Z^R\) and every surviving central degree.
Consequently the reserve idea is a valid reformulation, but it does not yet
bypass either Gate A or the all-depth selection theorem.

## 8. Exact remaining Gate-B alternatives

For the full-survivor route, a successful proof must establish all of the
following on the actual stopped punctured process:

1. a capacity-sized collection of terminal holes satisfies (1.6), hence
   carries constant Palm mass;
2. the external-window collision multiplier grows from one to
   \(\Omega(1/x)\), equivalently the stopped escort energy in (3.11) is
   \(\Omega(\log(1/x))\);
3. this collision mass is aligned with terminal holes rather than spent on
   already-covered targets; and
4. the required protection is produced by the late/intermittent regime
   permitted by (5.12), despite the first-blocker deletions.

Conversely, either of the following would rigorously rule out this route:

* \(\mathcal K_\tau=o(1/x)\) at one capacity-forcing shallow rank; or
* \(\sum_{j<\tau}\mathcal A_j=o(\log(1/x))\).

These are second-moment statements about two surviving external carriers
and one blocker cell.  They are strictly sharper than marginal external
degree regularity and strictly weaker than comparing the complete stopped
state with a product or uniform-slice law.  The separate long-flag-arc and
hole-dependent subcatalogue alternatives remain available and are not
excluded by this note.
