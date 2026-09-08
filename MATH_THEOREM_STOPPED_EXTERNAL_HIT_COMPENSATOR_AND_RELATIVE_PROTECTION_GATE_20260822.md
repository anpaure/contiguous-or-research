# Stopped external hits and the relative-protection gate

**Date:** 2026-08-22  
**Status:** unconditional stopped-process identities and a sharp reduction.
The note does **not** prove the positive Gate-B tail. It identifies the
smallest dynamic statistic which would prove it: a terminal hole's external
star must lose a factor \(x\) less mass than the whole surviving catalogue.
This is a first-blocker, three-carrier statistic, not a marginal external
degree estimate. An exact no-mark likelihood martingale and an exact
accepted-hit compensator are included so that no conditioning on future
holes is used.

## 1. Stopped isolated-edge process and external stars

Let \(\mathcal C_j\) be the residual directed punctured configurations just
before round \(j\), let \(Z_j=|\mathcal C_j|\), and let \(G_j\) be their
conflict graph. Conditional on the past \(\mathcal F_j\), mark every member
of \(\mathcal C_j\) independently with probability \(p_j\). Let
\(\mathcal A_j\) be the isolated marked configurations. Delete the closed
conflict neighbourhood of \(\mathcal A_j\), obtaining \(\mathcal C_{j+1}\).
All stopping times below are bounded; the usual deterministic round cap in
the punctured descent gives this without localization.

Put

\[
 b=2r+1,\qquad A=\binom br,\qquad B=A/b.
\]

Fix also the terminal residual-density parameter \(x\in(0,1]\), the
absolute cover-mass constant \(K>0\), and a shallow cutoff \(Q=o(b)\).
They enter only in the terminal threshold and in the aggregate restoration
charge; the martingale identities themselves hold for every choice.

Fix a shallow depth \(q\), put \(k_q=r-q\) and
\(B_q=\binom b{k_q}\), and use the restored full-row convention. Thus a
tagged lower target is a \(k_q\)-set, and an upper target is identified with
the complementary \(k_q\)-set. For such a target \(T\), define its current
external star and degree by

\[
 \mathcal S_j(T)=\{F\in\mathcal C_j:
       T\text{ is a window of the full row underlying }F\},\qquad
 X_j(T)=|\mathcal S_j(T)|.                         \tag{1.1}
\]

Every configuration has exactly \(b\) full-row windows at this tagged
depth, so

\[
                 \sum_T X_j(T)=bZ_j.              \tag{1.2}
\]

Initially the configuration catalogue is labelled and complete. Hence

\[
 Z_0=b!,\qquad X_0(T)=D_q=b\,k_q!(b-k_q)!,\qquad
 {X_0(T)\over Z_0}={b\over B_q}.                  \tag{1.3}
\]

Let \(U_j(T)\) be the indicator that no previously accepted full row has
contained \(T\). The terminal restored holes are exactly the targets with
\(U_\tau(T)=1\). Passing back to the punctured bank changes at most one
target per accepted row and depth, hence only \(O(QB)=o(A)\) aggregate
targets over \(Q=o(b)\) depths.

## 2. Exact one-round accepted-hit hazard

Let

\[
 K_j(T)=|\mathcal A_j\cap\mathcal S_j(T)|,\qquad
 a_j(T)=\Pr(K_j(T)>0\mid\mathcal F_j).             \tag{2.1}
\]

Write \(\Delta_j\) for the maximum degree of \(G_j\), and put
\(u_j(T)=p_jX_j(T)\).

### Theorem 2.1 (external-star hit bound)

Suppose \(p_j\le1/2\) and \(p_j\Delta_j\le\beta\). Then, conditionally on
\(\mathcal F_j\),

\[
 \boxed{
 e^{-4\beta}{u_j(T)\over1+u_j(T)}
 \le a_j(T)\le\min\{1,u_j(T)\}.}                  \tag{2.2}
\]

In particular, when \(u_j(T)\le1\), the probability of an accepted hit is
within absolute constant factors of \(p_jX_j(T)\). Under the one-cap
punctured descent, \(p_j\Delta_j\le1/16\), so the constants are uniform.

#### Proof

For \(F\in\mathcal S_j(T)\), let \(I_F\) indicate that \(F\) is an isolated
mark. If \(g_j(F)\) is its conflict degree, then

\[
 \lambda_j(T):=\mathbb E[K_j(T)\mid\mathcal F_j]
 =\sum_{F\in\mathcal S_j(T)}p_j(1-p_j)^{g_j(F)}.
\]

Since \(\log(1-p)\ge-2p\) on \([0,1/2]\),

\[
                  e^{-2\beta}u_j(T)\le\lambda_j(T)\le u_j(T). \tag{2.3}
\]

Two conflicting configurations cannot both be isolated marks. For two
nonconflicting configurations, the probability that both are isolated
marks is at most \(p_j^2\). Consequently

\[
 \mathbb E[K_j(T)^2\mid\mathcal F_j]
 \le\lambda_j(T)+u_j(T)^2.                         \tag{2.4}
\]

The second-moment inequality and (2.3) give

\[
 a_j(T)\ge{\lambda_j(T)^2\over
                  \mathbb E K_j(T)^2}
 \ge e^{-4\beta}{u_j(T)^2\over u_j(T)+u_j(T)^2}.
\]

The union bound gives \(a_j(T)\le\lambda_j(T)\le u_j(T)\), and a
probability is at most one. This proves (2.2). \(\square\)

### Theorem 2.2 (stopped external-hit compensator)

For every fixed \(T\), both

\[
 \boxed{
 U_n(T)+\sum_{j<n}U_j(T)a_j(T)}                   \tag{2.5}
\]

and, provided \(p_j<1\) whenever \(Z_j>0\), the exact no-accepted-hit
likelihood

\[
 \boxed{
 U_n(T)\exp\!\left\{\sum_{j<n}-\log(1-a_j(T))\right\}}          \tag{2.5a}
\]

are martingales.  Indeed, when \(Z_j>0\), the conditional event that no
configuration is marked has probability \((1-p_j)^{Z_j}>0\), and on that
event there is no accepted hit.  Hence \(a_j(T)<1\); when \(Z_j=0\), it is
zero.  Thus (2.5a) never invokes an implicit \(0\cdot\infty\) convention.
In particular,

\[
 \Pr\!\left(U_\tau(T)=1,\
       \sum_{j<\tau}-\log(1-a_j(T))\ge s\right)\le e^{-s}.      \tag{2.5b}
\]

If the sum in (2.5b) is at most \(\Lambda\) on every unhit trajectory,
then the same martingale gives

\[
                         \Pr(U_\tau(T)=1)\ge e^{-\Lambda}.      \tag{2.5c}
\]

Therefore, for every bounded stopping time \(\tau\),

\[
 \boxed{
 \mathbb E h_q(\tau)
 =B_q-\mathbb E\sum_{j<\tau}\sum_TU_j(T)a_j(T),}   \tag{2.6}
\]

where \(h_q(\tau)=\sum_TU_\tau(T)\) is the restored hole count on the
tagged shore. Under the hypotheses of Theorem 2.1,

\[
 \begin{aligned}
 e^{-4\beta}\,\mathbb E\sum_{j<\tau}\sum_TU_j(T)
       {p_jX_j(T)\over1+p_jX_j(T)}
 &\le B_q-\mathbb Eh_q(\tau)\\
 &\le\mathbb E\sum_{j<\tau}\sum_TU_j(T)
       \min\{1,p_jX_j(T)\}.                       \tag{2.7}
 \end{aligned}
\]

Thus the relevant Palm observable for external cover during the descent is
the degree on targets which are unhit **at that time**. Replacing \(U_j\)
by the terminal event \(U_\tau\) is a future-conditioning error.

#### Proof

On \(U_j(T)=1\), the next indicator is zero precisely when
\(K_j(T)>0\). Hence

\[
 \mathbb E[U_{j+1}(T)-U_j(T)\mid\mathcal F_j]
 =-U_j(T)a_j(T).
\]

This proves (2.5). Optional stopping and summation over \(T\) give (2.6),
and (2.2) gives (2.7). Conditional on \(U_j(T)=1\), the probability of
remaining unhit for one more round is exactly \(1-a_j(T)\). Multiplying by
its reciprocal proves (2.5a), and Markov's inequality proves (2.5b).
The identical estimate
\(1=\mathbb E[U_\tau\exp\{\sum-\log(1-a_j)\}]
\le e^\Lambda\Pr(U_\tau=1)\) proves (2.5c). \(\square\)

## 3. Exact no-mark likelihood and its limitation

Let \(V_j(T)\) indicate that no member of the successive external stars of
\(T\) has been marked before round \(j\), and put

\[
 L_n(T)=\sum_{j<n}-X_j(T)\log(1-p_j).              \tag{3.1}
\]

Only the value of \(L_n\) on \(V_n=1\) matters.

### Proposition 3.1 (no-mark likelihood martingale)

\[
 \boxed{V_n(T)e^{L_n(T)}}                          \tag{3.2}
\]

is an exact nonnegative martingale. In particular,

\[
 \mathbb E[V_\tau(T)e^{L_\tau(T)}]=1,\qquad
 \Pr(V_\tau(T)=1,\ L_\tau(T)\ge s)\le e^{-s}.       \tag{3.3}
\]

Moreover \(V_\tau(T)\le U_\tau(T)\). If
\(L_\tau(T)\le\Lambda\) on every no-mark trajectory, then

\[
                         \Pr(U_\tau(T)=1)\ge e^{-\Lambda}.      \tag{3.4}
\]

#### Proof

Conditional on \(\mathcal F_j\) and \(V_j(T)=1\), no member of the current
star is marked with probability
\((1-p_j)^{X_j(T)}\). This factor is exactly cancelled by the next factor
in \(e^{L_n(T)}\), proving (3.2). Optional stopping gives the first part of
(3.3), and Markov gives its second part. A no-mark path has no accepted
hit, so \(V_\tau\le U_\tau\). Finally,

\[
 1=\mathbb E[V_\tau e^{L_\tau}]\le e^\Lambda\Pr(V_\tau=1)
\]

under the displayed pathwise hypothesis, proving (3.4). \(\square\)

Equation (3.2) is also the precise warning about terminal conditioning.
An average bound for \(L_\tau(T)\), or a bound holding for targets selected
after the final holes are known, does not imply (3.4). What is needed is a
bound on every relevant no-mark path, or direct control of the likelihood
tail in (3.3).

## 4. Relative star protection is exactly the \(1/x\) Palm factor

Throughout this section assume

\[
                         Z_j>0\qquad(0\le j\le\tau).             \tag{4.0}
\]

This holds on every good trajectory of the stopped punctured descent; in
fact its proved bite bound gives \(Z_{j+1}\ge7Z_j/8\). If
\(Z_\tau=0\), the final survivor catalogue is empty and the survivor-cover
alternative fails trivially, so there is no positive conclusion to study.

For a realized trajectory define the one-round global loss fraction

\[
 d_j=1-{Z_{j+1}\over Z_j}.                         \tag{4.1}
\]

For a target with \(X_j(T)>0\), define its external-star loss fraction

\[
 d_j(T)=1-{X_{j+1}(T)\over X_j(T)}.                \tag{4.2}
\]

If \(X_j(T)=0\), set \(d_j(T)=0\) for bookkeeping; then
\(\pi_j(T)=\pi_{j+1}(T)=0\), so its value does not affect any Palm sum.
If \(X_j(T)>0\) but \(X_{j+1}(T)=0\), set
\(\mathscr P_n(T)=-\infty\) for every \(n\ge j+1\), and set
\(e^{\mathscr P_n(T)}=0\). Since the residual catalogues are nested, the
star remains empty. For a star which remains nonempty, define the
relative-protection logarithm

\[
 \mathscr P_\tau(T)=\sum_{j<\tau}
       \log{1-d_j(T)\over1-d_j}.                   \tag{4.3}
\]

The normalized external-window Palm law is

\[
                         \pi_j(T)={X_j(T)\over bZ_j}.            \tag{4.3a}
\]

By (1.2), this is a probability distribution on the targets at the fixed
tagged depth: sample a uniform surviving labelled configuration and then a
uniform full-row start. It obeys the exact replicator identities

\[
 \boxed{
 \pi_{j+1}(T)=\pi_j(T){1-d_j(T)\over1-d_j},\qquad
 \sum_T\pi_j(T)\bigl(d_j-d_j(T)\bigr)=0.}          \tag{4.3b}
\]

The first equality is substitution of (4.1)--(4.2). For the second, use
(1.2) at times \(j\) and \(j+1\):

\[
 \sum_T X_j(T)d_j(T)=\sum_T(X_j(T)-X_{j+1}(T))
 =b(Z_j-Z_{j+1})=bZ_jd_j.
\]

Thus the *linear* relative-loss increment has zero one-round Palm mean
before the terminal holes are revealed.  The logarithmic increment does
not: Jensen's inequality applied to the first identity in (4.3b) gives

\[
 \sum_T\pi_j(T)\log{1-d_j(T)\over1-d_j}\le0.       \tag{4.3c}
\]

Gate B asks the positive tail of these logarithmic increments to align
with the future holes; no mean-zero assertion for the logarithm is used.

### Theorem 4.1 (exact relative-protection identity)

For every target with \(X_\tau(T)>0\), pathwise,

\[
 \boxed{
 {X_\tau(T)\over Z_\tau}={b\over B_q}\,
                         e^{\mathscr P_\tau(T)}.}   \tag{4.4}
\]

Consequently, give each member of the final labelled survivor catalogue
the common weight \(KxB/Z_\tau\). This weighting has total mass \(KxB\)
and covers \(T\) fractionally to level one if and only if

\[
 \boxed{
 \mathscr P_\tau(T)\ge
 \log{B_q\over Kx\,bB}
 =\log{B_q\over KxA}.}                             \tag{4.5}
\]

For \(q\le\sqrt{rx}/4\), \(B_q/A=1-O(x)\), so the right side is

\[
                         \log(1/x)-O_K(1).          \tag{4.6}
\]

Thus the missing factor \(1/x\) is exactly a \(\log(1/x)\) lower tail for
relative blocker avoidance along terminal holes. It cannot be created by
ordinary marginal regularity, which corresponds to
\(\mathscr P_\tau(T)=O(1)\).

#### Proof

Telescoping (4.1)--(4.3) gives

\[
 e^{\mathscr P_\tau(T)}
 ={X_\tau(T)/X_0(T)\over Z_\tau/Z_0}.
\]

Use (1.3) to obtain (4.4). Giving every final surviving labelled
configuration weight \(1/D_0\), where
\(D_0=Z_\tau/(KxB)\), has total mass \(KxB\). Its coverage of \(T\) is at
least one exactly when \(X_\tau(T)\ge D_0\). Substitute (4.4) and
\(bB=A\) to obtain (4.5). The shallow estimate for \(B_q/A\) gives
(4.6). Labelled rotations may be sampled independently and then
coalesced into physical rows; coverage is unchanged and the physical row
count can only decrease. \(\square\)

### Corollary 4.2 (exact full-catalogue Gate-B criterion)

Let \(\mathcal H\) be the restored tagged shallow-hole universe. Uniform
weight on the final surviving catalogue gives a fractional cover of mass
\(KxB\) outside \(o(A)\) holes if and only if

\[
 \left|\left\{T\in\mathcal H:
 \mathscr P_\tau(T)<\log{B_{q(T)}\over KxA}\right\}\right|=o(A). \tag{4.7}
\]

This criterion is pathwise and contains no comparison with a product or
uniform-slice residual.

For one fixed rank, if its final hole set has size at least \(c_0xA\) and
the exceptional part at that rank is \(o(xA)\), then (4.7) also forces the
aggregate Palm alignment

\[
 \boxed{\sum_{T\in\mathcal H_q}\pi_\tau(T)
             \ge {c_0\over K}+o(1).}               \tag{4.7a}
\]

Indeed every nonexceptional hole has
\(\pi_\tau(T)=X_\tau(T)/(bZ_\tau)\ge1/(KxA)\).
Thus an \(x\)-density target set must carry constant external-window Palm
mass. Equation (4.3b) shows exactly where the factor \(1/x\) must enter.
Under the weaker aggregate exception \(o(A)\) used in Gate B, the valid
band statement is the following: if
\(|\mathcal H|\ge c_0xAQ\) and \(xQ\to\infty\), then

\[
 \sum_{q\le Q}\sum_{\pm}\sum_{T\in\mathcal H_q^\pm}
       \pi_{q,\tau}(T)\ge\left({c_0\over K}+o(1)\right)Q.       \tag{4.7aa}
\]

Here \(\pi_{q,\tau}\) is normalized separately on each tagged depth.
Indeed the \(o(A)\) exceptions are now \(o(xAQ)\), and division of every
remaining floor by \(bZ_\tau\) gives \(1/(KxA)\).

There is essentially no room to waste this tail on nonholes. From
\(\pi_0(T)=1/B_q\) and (4.3b)--(4.4),

\[
                         \sum_Te^{\mathscr P_\tau(T)}=B_q.      \tag{4.7b}
\]

Therefore, pathwise, for every \(s\),

\[
 \boxed{
 |\{T:\mathscr P_\tau(T)\ge s\}|\le B_qe^{-s}.}     \tag{4.7c}
\]

For completeness, targets whose star becomes empty are assigned
\(\mathscr P_\tau(T)=-\infty\) and \(e^{\mathscr P_\tau(T)}=0\). For every
other target, iterating the first identity in (4.3b) gives
\[
 \pi_\tau(T)=\pi_0(T)e^{\mathscr P_\tau(T)}
             ={1\over B_q}e^{\mathscr P_\tau(T)}.
\]
Summing this equality over the nonempty terminal stars and using
\(\sum_T\pi_\tau(T)=1\) proves (4.7b), including the empty-star targets.
If \(\mathscr P_\tau(T)\ge s\), its summand in (4.7b) is at least \(e^s\);
there can therefore be at most \(B_qe^{-s}\) such targets, proving
(4.7c).

At the Gate-B threshold in (4.5), the right side is exactly \(KxA\).
Capacity already supplies \(\Omega(xA)\) holes at each shallow rank.
Hence a successful theorem must align an essentially capacity-sized
upper tail of relative protection with an essentially capacity-sized hole
set; proving the tail without this alignment is insufficient.

### Corollary 4.3 (protection forces flag clustering)

Let \(Q\) be the shallow cutoff, let \(\mathcal H\) contain both tagged
shores through depth \(Q\), and define the final hole score of a surviving
labelled configuration \(F\) by

\[
 S_Q(F)=\sum_{q\le Q}\sum_{\pm}\sum_{s\in\mathbb Z_b}
 \mathbf 1_{\{I_{q,\pm}^F(s)\in\mathcal H_q^\pm\}}.             \tag{4.8}
\]

Here \(I_{q,-}^F(s)\) and \(I_{q,+}^F(s)\) denote its lower and upper
full-row windows at depth \(q\). If

\[
 |\mathcal H|\ge c_0xAQ
\]

and (4.7) holds, then, whenever \(xQ\to\infty\),

\[
 \boxed{{1\over Z_\tau}\sum_{F\in\mathcal C_\tau}S_Q(F)
       \ge\left({c_0\over K}+o(1)\right)bQ.}         \tag{4.9}
\]

Consequently a positive proportion (depending only on \(c_0,K\)) of the
surviving labelled configurations have score \(\Omega(bQ)\). Every such
full row has, for every \(1\le L_0\le b\), some cyclic interval \(J\) of
\(L_0\) starts with flag-arc score \(\Omega(L_0Q)\).

#### Proof

Double counting gives the exact identity

\[
 \sum_{F\in\mathcal C_\tau}S_Q(F)
 =\sum_{q\le Q}\sum_{\pm}\sum_{T\in\mathcal H_q^\pm}X_{q,T}(\tau).
                                                               \tag{4.10}
\]

Outside \(o(A)\) holes, (4.7) gives
\(X_{q,T}(\tau)\ge Z_\tau/(KxB)\). Since
\(|\mathcal H|=\Omega(xAQ)\) and \(xQ\to\infty\), the exceptional
\(o(A)\) targets are negligible in (4.10). Using \(A/B=b\) proves
(4.9). The score is at most \(2bQ\), so an average bounded below by a
positive multiple of \(bQ\) forces a positive proportion of configurations
to have score at least half that multiple.

For a fixed rich row, sum the scores of all \(b\) cyclic intervals of
length \(L_0\). Each start belongs to exactly \(L_0\) of those intervals,
so their average score is \((L_0/b)S_Q(F)=\Omega(L_0Q)\). One interval
has at least its average. \(\square\)

This is genuine clustering along an unaccepted full row, but it is only a
consequence of the protection tail. It does not say that the resulting
arcs collectively cover every hole; that additional covering assertion is
the long-flag-arc gate.

## 5. First-blocker form of the remaining statistic

The loss in (4.2) has an exact carrier expansion. In round \(j\), fix an
arbitrary deterministic order of the accepted configurations. Assign
each configuration deleted in that round to the first accepted
configuration in this order whose closed conflict neighbourhood contains
it (an accepted configuration may therefore be assigned to itself). Let
\(\mathcal B_j(G)\) be the cell assigned to \(G\in\mathcal A_j\). These
cells partition \(\mathcal C_j-\mathcal C_{j+1}\). Hence

\[
 Z_jd_j=\sum_{G\in\mathcal A_j}|\mathcal B_j(G)|,  \tag{5.1}
\]

\[
 X_j(T)d_j(T)=\sum_{G\in\mathcal A_j}
       |\mathcal B_j(G)\cap\mathcal S_j(T)|.       \tag{5.2}
\]

For a terminal hole \(T\), no \(G\in\mathcal A_j\) belongs to
\(\mathcal S_j(T)\). Thus (5.2) counts only triples

\[
             (T,\ F,\ G)                           \tag{5.3}
\]

in which \(T\) is a terminal hole, \(F\) is a current configuration whose
full row contains \(T\), and \(G\) is the accepted outside blocker first
deleting \(F\).

Combining (4.3), (5.1), and (5.2), the exact unresolved positive tail is

\[
 \boxed{
 \left|\left\{T\in\mathcal H:
 \sum_{j<\tau}\log
 {1-\displaystyle{\sum_{G\in\mathcal A_j}
       |\mathcal B_j(G)\cap\mathcal S_j(T)|\over X_j(T)}
  \over
  1-\displaystyle{\sum_{G\in\mathcal A_j}|\mathcal B_j(G)|\over Z_j}}
 <\log{B_{q(T)}\over KxA}\right\}\right|=o(A).}     \tag{5.4}
\]

In (5.4), a target whose star becomes empty is assigned total logarithm
\(-\infty\) at its first extinction round, consistently with Section 4;
no later quotient by \(X_j(T)=0\) is evaluated.

Equation (5.4) is the smallest exact obstruction isolated here. It asks
for a factor-\(x\) relative survival of the external stars of the actual
terminal holes. The numerator is a terminal-hole/row/blocker Palm
statistic; shore cardinalities and one-time external degree marginals do
not determine it.

### Corollary 5.1 (additive excess-loss obstruction)

On every good trajectory of the one-cap descent, the proved edge-count
estimate gives \(d_j\le1/8\). Every target satisfying the survivor floor
in (4.5) necessarily satisfies

\[
 \boxed{
 \sum_{j<\tau}\bigl(d_j-d_j(T)\bigr)_+
 \ge {7\over8}\left(\log{B_q\over KxA}\right)_+.}  \tag{5.5}
\]

Equivalently, using the first-blocker cells, each summand is the positive
part of

\[
 {\sum_{G\in\mathcal A_j}|\mathcal B_j(G)|\over Z_j}
 -
 {\sum_{G\in\mathcal A_j}
       |\mathcal B_j(G)\cap\mathcal S_j(T)|\over X_j(T)}.
                                                               \tag{5.6}
\]

#### Proof

A target satisfying the survivor floor has \(X_\tau(T)>0\), so none of
the star-extinction conventions is invoked. For any round with
\(d_j(T)<d_j\le1/8\),

\[
 \log{1-d_j(T)\over1-d_j}
 =\int_{d_j(T)}^{d_j}{du\over1-u}
 \le {8\over7}\bigl(d_j-d_j(T)\bigr),              \tag{5.7}
\]

because \(1/(1-u)\le1/(1-d_j)\le8/7\) on the integration interval. A
round with \(d_j(T)\ge d_j\) contributes nonpositively to
\(\mathscr P_\tau(T)\). Dropping all such rounds and applying (5.7) gives

\[
 \mathscr P_\tau(T)
 \le {8\over7}\sum_{j<\tau}(d_j-d_j(T))_+.
\]

If the logarithm in (4.5) is positive, combine this inequality with
(4.5) and rearrange. If it is nonpositive, (5.5) is the trivial
nonnegativity bound. Finally substitute (5.1)--(5.2) into
\(d_j-d_j(T)\) to obtain (5.6). \(\square\)

Thus a successful hole must receive logarithmically large cumulative
below-average blocker exposure. This additive occupation tail is a
necessary consequence of (5.4) and may be easier to attack.

The accepted-hit compensator (2.5) and no-mark likelihood (3.2) describe
the other side of the same path: a protected star has more chances to be
marked and accepted, yet a terminal hole has avoided every accepted hit.
A positive proof must therefore couple two facts simultaneously:

1. the star is spared by outside blockers by the logarithmic amount in
   (4.5); and
2. despite that protection, it incurs no accepted hit, as measured by
   (2.5) or (3.2).

This is why neither a marginal external-degree theorem nor conditioning a
uniform-slice estimate on the future hole event can close Gate B.

## 6. The no-hit tangent is only internal-star clustering

The first-order effect of conditioning on no accepted hit can be computed
in an arbitrary conflict graph. This gives a useful audit of whether the
factor in (4.5) is already present at time zero.

Let a finite graph have \(Z\) vertices and let \(S\) be a fixed
\(X\)-vertex external star. For a vertex \(G\), write

\[
 C_G=|N[G]|,\qquad A_G=|N[G]\cap S|.               \tag{6.1}
\]

Mark vertices independently with probability \(p\), accept isolated
marks, and delete their closed neighbourhoods. Let \(Z_p,X_p\) be the
remaining total and star sizes, and let \(\mathsf H_p\) be the event that
no accepted vertex belongs to \(S\).

### Proposition 6.1 (exact no-hit tangent)

Put

\[
 C_{\rm out}=\sum_{G\notin S}C_G,\qquad
 A_{\rm out}=\sum_{G\notin S}A_G.
\]

Then

\[
 \left.{d\over dp}\mathbb E[X_p\mid\mathsf H_p]\right|_{p=0}
 =-A_{\rm out},\qquad
 \left.{d\over dp}\mathbb E[Z_p\mid\mathsf H_p]\right|_{p=0}
 =-C_{\rm out}.                                    \tag{6.2}
\]

If the graph is vertex-transitive with \(C_G=C\), and

\[
                         A_{\rm in}=\sum_{G\in S}A_G,
\]

then

\[
 \boxed{
 \left.{d\over dp}\log
 {\,\mathbb E[X_p\mid\mathsf H_p]\over
    \mathbb E[Z_p\mid\mathsf H_p]}\right|_{p=0}
 ={A_{\rm in}\over X}-{CX\over Z}.}                \tag{6.3}
\]

Thus the only positive first-order source of relative protection is
internal conflict clustering inside the external star.

#### Proof

At \(p=0\), the derivative of the probability of an event under product
marking is the sum, over vertices \(G\), of its value with the singleton
mark \(\{G\}\) minus its value with no marks. A singleton in \(S\) is
accepted and makes \(\mathsf H_p\) false. A singleton outside \(S\) leaves
\(X-A_G\) star vertices and \(Z-C_G\) total vertices. Therefore

\[
 \Pr(\mathsf H_p)'|_{p=0}=-X,
\]

\[
 \left.\frac d{dp}\mathbb E[X_p\mathbf1_{\mathsf H_p}]\right|_{p=0}
 =-X^2-A_{\rm out},
\]

\[
 \left.\frac d{dp}\mathbb E[Z_p\mathbf1_{\mathsf H_p}]\right|_{p=0}
 =-XZ-C_{\rm out}.
\]

The quotient rule gives (6.2). If \(C_G=C\), double counting closed
neighbourhood incidences between \(S\) and the whole graph gives

\[
 A_{\rm in}+A_{\rm out}=\sum_{F\in S}C_F=XC,
 \qquad C_{\rm out}=C(Z-X).
\]

Substitution in the logarithmic derivative obtained from (6.2) proves
(6.3). \(\square\)

### Corollary 6.2 (initial punctured tangent)

In the complete directed punctured-configuration conflict graph, fix a
shallow external target \(T\), \(2\le q\le\sqrt r/4\), and take
\(S=\Omega_q(T):=\mathcal S_0(T)\).  Put
\(D_M=2r\,r!(r+1)!\). Uniformly in this range,

\[
                         {A_{\rm in}\over X}=O(D_q/r).          \tag{6.4}
\]

Consequently the positive part of (6.3) is \(O(D_q/r)\). Since
\(D_q/D_M=O(1)\) in this range, at the initial marking scale
\(p=\gamma/(rD_M)\) the corresponding linearized per-bite protection is

\[
                              O_\gamma(r^{-2}).                 \tag{6.5}
\]

#### Proof

Fix \(F\in\Omega_q(T)\). Every \(G\in\Omega_q(T)\) which conflicts with
\(F\) shares at least one punctured target with it. Hence

\[
 |\{G\in\Omega_q(T):G\cap F\ne\varnothing\}|
 \le\sum_{v\in F}|\{G\in\Omega_q(T):v\in G\}|.      \tag{6.6}
\]

Use the boundary representation with the two endpoints of the external
root \(T\). For a target \(v\in F\) whose boundary edge meets a root
endpoint, the mixed-root codegree estimate gives a normalized contribution
\(O(1/r)\); bounded boundary degree leaves only \(O(1)\) such targets. For
every other \(v\), the root and target have four distinct boundary
vertices, and the normalized contribution is \(O(1/r^2)\); there are
\(O(r)\) such targets. Dividing (6.6) by
\(|\Omega_q(T)|=D_q\) therefore gives \(O(1/r)\), uniformly in \(F\).
Summation over \(F\in\Omega_q(T)\) proves (6.4).

Finally,

\[
 {D_q\over D_M}
 ={b(r-q)!(r+1+q)!\over2r\,r!(r+1)!}=O(1)
\]

uniformly for \(q\le\sqrt r/4\), by taking logarithms of the two short
factorial products. Multiplication by \(p=\gamma/(rD_M)\) gives (6.5).
\(\square\)

Corollary 6.2 is only a tangent statement. It does not control the finite
bite error or exclude a later history-induced buildup of (4.3). It does
show that the needed \(\log(1/x)\) protection is not an immediate
time-zero consequence of external-star clustering.

## 7. Verdict

No positive hole-dependent cover or long-flag-arc tail is proved here.
What is proved is an exact stopped-law reduction sharper than the terminal
degree statistic alone:

* accepted hits have conditional hazard comparable to
  \(p_jX_j(T)/(1+p_jX_j(T))\);
* the currently-unhit hazard has the exact compensator (2.5);
* no-star-mark paths have the exact likelihood martingale (3.2); and
* the desired factor \(1/x\) in the final survivor catalogue is equivalent
  to \(\log(1/x)-O(1)\) cumulative relative blocker avoidance, with the
  explicit first-blocker expansion (5.4);
* the high-protection tail has capacity at most \(KxA\) at the Gate-B
  threshold, so it must be aligned almost perfectly with the
  \(\Omega(xA)\) holes; and
* the time-zero no-hit tangent supplies only \(O(r^{-2})\) linearized
  protection per initial-scale bite.

Accordingly, the smallest remaining statistic for the full-survivor route
is the lower tail in (5.4). Any proposed proof which controls only final
shore sizes, marginal \(X_{q,T}\), or an average hazard after the holes are
revealed does not control that statistic.
