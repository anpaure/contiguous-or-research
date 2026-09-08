# Fixed-pair cube factors in the exact MWB quota norm

Date: 2026-07-26

Method: pure mathematics only. No computation, search, or probabilistic
independence assumption is used.

## 0. Verdict

There are two corrections to the near-rainbow interpretation of a
fixed-pair cube factor.

First, an exact MWB depth has \(W\) physical occurrences but only \(N_q\)
targets. Its desired histogram is not a near-permutation. It is a mobile
floor/ceiling vector with entries

\[
 c_q=\left\lfloor {W\over N_q}\right\rfloor,
 \qquad c_q+1,
\]

and the exact defect is

\[
 O_q=\max\{L_q,U_q\}.
\]

Near-coverage controls neither \(L_q\) nor \(U_q\) in general. In the
first nontrivial case \(c_q=1\), the exact pair-energy identity is

\[
 P_q-P_q^{\min}
 =h_q+\sum_{\mu_q(S)\ge3}\binom{\mu_q(S)-1}{2},
\]

where \(h_q\) is the number of holes. Thus holes are only one part of the
defect; high multiplicities are the other part.

Second, the native fixed-pair architecture has a stronger obstruction.
At every depth

\[
                         q\sim a\sqrt m,\qquad a>0,
\]

the ratio between the available source mass and the number of targets in a
random pair-type class converges to

\[
                         R_a=e^{-a^2+2aZ},
 \qquad Z\sim N(0,1).
\]

Consequently every factor confined to one fixed coordinate matching misses
a positive fraction of the target layer. Moreover, even the optimal
distribution inside every pair-type class has a positive pair-collision
excess

\[
 {P_q-P_q^{\min}\over N_q}
 \ \ge\ \Gamma(a)+o(1),
 \qquad
 \Gamma(a):=\mathbb E p_*(R_a)-p_*(e^{a^2})>0,
\]

where

\[
                         p_*(x)=\lfloor x\rfloor x
                         -{\lfloor x\rfloor(\lfloor x\rfloor+1)\over2}.
\]

Thus one native fixed-pair system fails the Gaussian-window MWB test even
when its individual cube-cycle factors are exactly shadow-rainbow. Mixing
coordinate matchings can remove this type obstruction, but near-coverage
still does not suffice. The correct joint sufficient condition is that the
actual pair overlaps of the completed mixed factor exceed the balanced
pair baseline by only \(o(W)\) after summing with weights \(1/c_q\).

## 1. Exact mobile quotas

Put

\[
 n=2m+1,
 \qquad W=\binom{n}{m},
 \qquad N_q=\binom{n}{m-q},
\]

and write

\[
 W=c_qN_q+\rho_q,
 \qquad c_q=\left\lfloor{W\over N_q}\right\rfloor,
 \qquad 0\le\rho_q<N_q.                                      \tag{1.1}
\]

Let \(\mu_q\) be a nonnegative integral target histogram of total mass
\(W\). Define

\[
 L_q=\sum_S(c_q-\mu_q(S))_+,
 \qquad
 U_q=\sum_S(\mu_q(S)-c_q-1)_+.                              \tag{1.2}
\]

Let \(\mathcal B_q\) be the set of all integral vectors having exactly
\(\rho_q\) entries \(c_q+1\) and all other entries \(c_q\).

### Proposition 1.1 (exact MWB ledger)

For every full-mass histogram \(\mu_q\),

\[
 \boxed{
 O_q(\mu_q):={1\over2}\min_{b\in\mathcal B_q}
                    \|\mu_q-b\|_1
             =\max\{L_q,U_q\}.}                            \tag{1.3}
\]

#### Proof

Put \(d(S)=\mu_q(S)-c_q\), and set

\[
 A=\sum_S d(S)_+,
 \qquad t=|\{S:d(S)\ge1\}|.
\]

Since \(\sum_Sd(S)=\rho_q\), one has

\[
 A-L_q=\rho_q,
 \qquad U_q=A-t,
 \qquad U_q-L_q=\rho_q-t.                                  \tag{1.4}
\]

Starting with the constant floor \(c_q\), a high quota placed at a target
with \(d(S)\ge1\) removes one unit of excess, and a high quota placed
elsewhere removes none. There are \(\rho_q\) high quotas and they must be
placed at distinct targets. The minimum positive excess is therefore

\[
 A-\min\{\rho_q,t\}
 =\max\{A-\rho_q,A-t\}
 =\max\{L_q,U_q\}.
\]

Every \(b\in\mathcal B_q\) has the same total mass as \(\mu_q\), so its
positive and negative discrepancies agree. The positive discrepancy is
therefore one half of the \(\ell^1\) distance. This proves (1.3).
\(\square\)

The full-mass qualification is essential. A partial cube bank of mass
less than \(W\) does not yet have an MWB overload. Its completion and the
targets used by that completion must be included before (1.3) is applied.

## 2. Pair collisions and centered energy

Set

\[
 \lambda_q={W\over N_q}=c_q+\theta_q,
 \qquad \theta_q={\rho_q\over N_q},                         \tag{2.1}
\]

and define

\[
 P_q=\sum_S\binom{\mu_q(S)}2.                               \tag{2.2}
\]

Among all integral histograms of mass \(W\), the minimum of \(P_q\) is

\[
 P_q^{\min}
 =(N_q-\rho_q)\binom{c_q}{2}
   +\rho_q\binom{c_q+1}{2}
 =N_q\binom{c_q}{2}+c_q\rho_q.                             \tag{2.3}
\]

Put

\[
 \Pi_q=P_q-P_q^{\min}.                                     \tag{2.4}
\]

### Proposition 2.1 (three exact forms of the excess)

One has

\[
 \boxed{
 \Pi_q
 =\sum_S {d(S)(d(S)-1)\over2}
 ={1\over2}\left(
   \sum_S(\mu_q(S)-\lambda_q)^2
   -N_q\theta_q(1-\theta_q)
   \right).}                                               \tag{2.5}
\]

Moreover,

\[
 \boxed{\Pi_q\ge L_q+U_q\ge O_q.}                          \tag{2.6}
\]

#### Proof

The identity

\[
 \binom{c+d}{2}=\binom c2+cd+{d(d-1)\over2}
\]

and \(\sum_Sd(S)=\rho_q\) give the first equality in (2.5).
Also

\[
 \sum_S\mu_q(S)^2=W+2P_q,
\]

and the balanced vectors have centered energy

\[
 (N_q-\rho_q)\theta_q^2
 +\rho_q(1-\theta_q)^2
 =N_q\theta_q(1-\theta_q).
\]

Subtracting the balanced identity gives the second equality in (2.5).

Finally, for every integer \(d\),

\[
 {d(d-1)\over2}\ge(-d)_+ +(d-1)_+.
\]

After summing, the right side is \(L_q+U_q\). Proposition 1.1 gives
\(L_q+U_q\ge O_q\). This proves (2.6). \(\square\)

Equivalently, the two tails of (2.5) are

\[
 \Pi_q=
 \sum_{\mu_q(S)\le c_q-1}
       \binom{c_q-\mu_q(S)+1}{2}
 +\sum_{\mu_q(S)\ge c_q+2}
       \binom{\mu_q(S)-c_q}{2}.                             \tag{2.7}
\]

This is the quadratic version of the exact linear quota defect.

## 3. Why near-coverage is not the MWB condition

Let

\[
 h_q=|\{S:\mu_q(S)=0\}|.
\]

Near-coverage means only that \(h_q\) is small. From (1.2),

\[
                         L_q\ge c_qh_q,                     \tag{3.1}
\]

but there is no converse: targets with loads
\(1,\ldots,c_q-1\) also contribute to \(L_q\), and a small number of very
large loads can make \(U_q\) macroscopic.

When \(c_q=1\), the distinction is especially transparent. Since
\(W=N_q+\rho_q\),

\[
 \begin{aligned}
 \Pi_q
 &=P_q-\rho_q\\
 &=h_q+\sum_{\mu_q(S)\ge3}
                   \binom{\mu_q(S)-1}{2}.                  \tag{3.2}
 \end{aligned}
\]

Indeed, if \(D_q=W-|\operatorname{supp}\mu_q|\) is the ordinary duplicate
count, then

\[
 D_q=\rho_q+h_q,
 \qquad
 P_q-D_q=\sum_{\mu_q(S)\ge3}\binom{\mu_q(S)-1}{2}.
\]

Thus near-coverage controls the first term in (3.2), not the second.

For example, give \(N_q-1\) targets load \(1\) and put all remaining mass
on the last target. There are no holes, but \(O_q=\Theta(W)\) whenever
either \(c_q\ge2\), or \(c_q=1\) and \(\rho_q=\Theta(N_q)\). Consequently
no support-only theorem can imply Gaussian-window MWB.

### 3.1 The exact translation of a near-permutation cube census

The SCD shadow census and the MWB census have different total masses. A
near-rainbow SCD bank may furnish approximately \(N_q\) certified starts at
depth \(q\), one per target. An exact MWB histogram has \(W\) starts. Thus
the former is only a partial histogram in the latter problem.

More precisely, write a proposed completed MWB histogram as

\[
                         \mu_q=\eta_q+\gamma_q,
\]

where \(\eta_q\) is the cube-bank histogram and \(\gamma_q\) is its physical
completion. For every fixed balanced quota \(b\in\mathcal B_q\), the
following identity holds target by target and hence after summation:

\[
 \boxed{
 \sum_S(\eta_q(S)+\gamma_q(S)-b(S))_+
 =
 \sum_S(\eta_q(S)-b(S))_+
 +
 \sum_S\left(\gamma_q(S)-(b(S)-\eta_q(S))_+\right)_+.}      \tag{3.3}
\]

The second term is the completion spill beyond the residual quota left by
the cube bank. Near-coverage of \(\eta_q\) gives no bound on it. At
\(q\sim a\sqrt m\),

\[
 W-N_q=(e^{a^2}-1+o(1))N_q=\Theta_a(W),                    \tag{3.4}
\]

so the completion is not a sparse perturbation. It must itself be placed
with floor/ceiling accuracy. This is the exact reason that a
near-permutation theorem for \(N_q\) certified shadows does not translate
automatically to MWB.

## 4. Exact joint formulas for cube-cycle factors

Fix a depth \(q\), and decompose a completed factor into physical
cube-cycle blocks indexed by \(\alpha\in\mathcal A\). Let

\[
 x_{\alpha,q}(S)
 =\text{the number of depth-\(q\) occurrences from block \(\alpha\)
 landing at \(S\)},
\]

and put

\[
 w_{\alpha,q}=\sum_Sx_{\alpha,q}(S),
 \qquad
 \mu_q=\sum_\alpha x_{\alpha,q},
 \qquad
 \sum_\alpha w_{\alpha,q}=W.                               \tag{4.1}
\]

Define the actual joint overlap

\[
 C_{\alpha\beta,q}
 =\sum_Sx_{\alpha,q}(S)x_{\beta,q}(S).                     \tag{4.2}
\]

### Proposition 4.1 (collision decomposition)

The factorial pair count is exactly

\[
 \boxed{
 P_q=
 \sum_\alpha\sum_S\binom{x_{\alpha,q}(S)}2
 +\sum_{\alpha<\beta}C_{\alpha\beta,q}.}                   \tag{4.3}
\]

If every block is depth-\(q\) shadow-simple, so that
\(x_{\alpha,q}(S)\in\{0,1\}\), then

\[
 \boxed{
 \Pi_q=
 \sum_{\alpha<\beta}
 |\mathcal S_{\alpha,q}\cap\mathcal S_{\beta,q}|
 -P_q^{\min},}                                             \tag{4.4}
\]

where \(\mathcal S_{\alpha,q}\) is the target set of block \(\alpha\).

#### Proof

For each target \(S\), expand

\[
 \binom{\sum_\alpha x_{\alpha,q}(S)}2
 =\sum_\alpha\binom{x_{\alpha,q}(S)}2
  +\sum_{\alpha<\beta}x_{\alpha,q}(S)x_{\beta,q}(S),
\]

and sum over \(S\). If the blocks are simple, all internal terms vanish.
Subtract (2.3). \(\square\)

There is an equivalent centered Gram formula. Put

\[
 z_{\alpha,q}=x_{\alpha,q}
        -{w_{\alpha,q}\over N_q}\mathbf1.
\]

Then

\[
 \boxed{
 \sum_S(\mu_q(S)-\lambda_q)^2
 =\left\|\sum_\alpha z_{\alpha,q}\right\|_2^2
 =\sum_\alpha\|z_{\alpha,q}\|_2^2
  +2\sum_{\alpha<\beta}
       \langle z_{\alpha,q},z_{\beta,q}\rangle,}            \tag{4.5}
\]

with

\[
 \langle z_{\alpha,q},z_{\beta,q}\rangle
 =C_{\alpha\beta,q}
   -{w_{\alpha,q}w_{\beta,q}\over N_q}.                    \tag{4.6}
\]

Equations (4.3)--(4.6) use actual joint intersections. Replacing
\(C_{\alpha\beta,q}\) by a product of marginal hit probabilities is valid
only after independence of those two selected blocks has been proved.
Cube choices coupled by vertex-disjointness, common ownership, or exact
factor constraints are not independent by default.

## 5. The native fixed-pair type ledger in odd dimension

Pair the first \(2m\) coordinates and distinguish the last coordinate
\(\infty\). Let \(\varepsilon\in\{0,1\}\) record whether a target contains
\(\infty\). We work below the pair-residence length, so every protected
depth-\(q\) window changes \(q\) distinct pair directions. A rank-\(m-q\)
target of type \((\varepsilon,f)\) has

\[
 f\text{ full pairs},\qquad
 f+q+\varepsilon\text{ empty pairs},\qquad
 m-2f-q-\varepsilon\text{ split pairs}.
\]

The number of such targets is

\[
 T_{f,q}^{\varepsilon}
 ={m!\over
 f!(f+q+\varepsilon)!(m-2f-q-\varepsilon)!}
 2^{m-2f-q-\varepsilon}.                                  \tag{5.1}
\]

Every fixed-pair depth-\(q\) window landing in this class starts in the
middle source class with \(f\) full pairs,
\(f+\varepsilon\) empty pairs, and \(m-2f-\varepsilon\) split pairs.
The total number of available physical starts in that source class is

\[
 V_f^{\varepsilon}
 ={m!\over
 f!(f+\varepsilon)!(m-2f-\varepsilon)!}
 2^{m-2f-\varepsilon}.                                    \tag{5.2}
\]

Both identities include all orientation labels. They imply

\[
 \sum_{\varepsilon,f}T_{f,q}^{\varepsilon}=N_q,
 \qquad
 \sum_{\varepsilon,f}V_f^{\varepsilon}=W.                  \tag{5.3}
\]

Define the exact type ratio

\[
 R_{f,q}^{\varepsilon}
 ={V_f^{\varepsilon}\over T_{f,q}^{\varepsilon}}
 ={2^q(f+\varepsilon+1)^{\overline q}
   \over(m-2f-\varepsilon)_{\underline q}}.                \tag{5.4}
\]

No choice of direction orders or cycle factors changes (5.1)--(5.4),
because a fixed-pair window preserves \(\varepsilon\) and \(f\).

### Proposition 5.1 (exact type lower bounds)

Every completed factor confined to this one coordinate matching satisfies

\[
 h_q\ge
 \sum_{\varepsilon,f}
       (T_{f,q}^{\varepsilon}-V_f^{\varepsilon})_+,         \tag{5.5}
\]

\[
 L_q\ge
 \sum_{\varepsilon,f}
       (c_qT_{f,q}^{\varepsilon}-V_f^{\varepsilon})_+,      \tag{5.6}
\]

and

\[
 P_q\ge
 \sum_{\varepsilon,f}
 T_{f,q}^{\varepsilon}
 p_*\left(R_{f,q}^{\varepsilon}\right),                    \tag{5.7}
\]

where, for \(x\ge0\),

\[
 p_*(x)=\lfloor x\rfloor x
       -{\lfloor x\rfloor(\lfloor x\rfloor+1)\over2}
       =\sum_{j\ge1}(x-j)_+.                               \tag{5.8}
\]

#### Proof

A type class has \(T=T_{f,q}^{\varepsilon}\) targets and receives exactly
\(V=V_f^{\varepsilon}\) starts. It can cover at most \(\min(T,V)\)
targets, proving (5.5). Also

\[
 \sum_{S\text{ in class}}(c_q-\mu_q(S))_+
 \ge(c_qT-V)_+,
\]

which proves (5.6).

Finally, convexity of \(x\mapsto\binom x2\) on the nonnegative integers
shows that its sum is minimized by distributing \(V\) as evenly as
possible among the \(T\) cells. If \(k=\lfloor V/T\rfloor\), the minimum
is

\[
 (T-(V-kT))\binom k2+(V-kT)\binom{k+1}2
 =T p_*(V/T).
\]

Summing over the type classes proves (5.7). \(\square\)

## 6. Gaussian limit of the type ratio

Choose a uniformly random rank-\(m-q\) target. Equivalently, choose
\((\varepsilon,F)\) with probabilities
\(T_{f,q}^{\varepsilon}/N_q\), and set

\[
                         R_m=R_{F,q}^{\varepsilon}.
\]

### Lemma 6.1 (pair-type lognormal limit)

If

\[
                         {q\over\sqrt m}\longrightarrow a>0,
\]

then

\[
 \boxed{R_m\ \Longrightarrow\ R_a:=e^{-a^2+2aZ},
        \qquad Z\sim N(0,1).}                              \tag{6.1}
\]

#### Proof

Condition on \(\varepsilon\). The remaining target chooses

\[
                         k=m-q-\varepsilon
\]

points uniformly from \(2m\) points partitioned into \(m\) pairs. If
\(F\) is the number of full pairs, its exact factorial moments are

\[
 \mathbb E(F)_{j}
 =(m)_j{(k)_{2j}\over(2m)_{2j}}.                            \tag{6.2}
\]

In particular,

\[
 \bar f_{q,\varepsilon}:=\mathbb EF
 =m{(k)_2\over(2m)_2},
 \qquad
 \operatorname {Var}F={m\over16}+O_a(\sqrt m).             \tag{6.3}
\]

For completeness, the required central limit theorem follows directly by
conditioning independent pair variables. Put \(p=k/(2m)\). Let
\((X_i,Y_i)\), \(1\le i\le m\), be independent, where
\(X_i\sim\operatorname {Bin}(2,p)\) and
\(Y_i=\mathbf1_{\{X_i=2\}}\). Conditional on
\(\sum_iX_i=k\), the chosen \(k\)-subset is uniform and
\(F=\sum_iY_i\). The unconditioned covariance data are

\[
 \begin{aligned}
 \operatorname {Var}X_i&=2p(1-p),\\
 \operatorname {Var}Y_i&=p^2(1-p^2),\\
 \operatorname {Cov}(X_i,Y_i)&=2p^2(1-p).
 \end{aligned}                                             \tag{6.4}
\]

Hence the conditional Gaussian variance is

\[
 p^2(1-p^2)-
 {4p^4(1-p)^2\over2p(1-p)}
 =p^2(1-p)^2.                                               \tag{6.5}
\]

Here is a short rigorous conditional-CLT argument. Fourier inversion in
the conditioning variable writes the conditional characteristic function
as a ratio of two integrals over \([-\pi,\pi]\). On
\(|u|\le m^{-2/5}\), Taylor expansion of the joint characteristic function
of \((X_i,Y_i)\) gives the bivariate Gaussian exponent with covariance
(6.4), uniformly because \(p=1/2+O_a(m^{-1/2})\). On the complement, the
modulus is at most
\(\exp(-c m u^2)\) for \(|u|\le\delta\), and at most
\(\exp(-c_\delta m)\) for \(\delta\le|u|\le\pi\); these follow from the
three-point support of \(X_i\) and hold uniformly for \(p\) in a fixed
compact subinterval of \((0,1)\). Dividing the two Gaussian integrals and
using (6.5) yields

\[
 {F-mp^2\over\sqrt m\,p(1-p)}
 \Longrightarrow N(0,1).
\]

Since \(\bar f_{q,\varepsilon}-mp^2=O_a(1)\), this is

\[
 {4(F-\bar f_{q,\varepsilon})\over\sqrt m}
 \Longrightarrow N(0,1).                                  \tag{6.6}
\]

This convergence is uniform in the two values of \(\varepsilon\). The
same calculation can alternatively be read from the exact probability
generating function

\[
 { [x^k](1+2x+ux^2)^m\over\binom{2m}{k}}.                  \tag{6.7}
\]

Taylor expansion of the logarithm of (5.4), first at the saddle
\(\bar f_{q,\varepsilon}\) and then in \(f\), gives, uniformly on every
\(O(\sqrt m\log m)\) central band,

\[
 \log R_{f,q}^{\varepsilon}
 =-{q^2\over m}
  +{8q\over m}(f-\bar f_{q,\varepsilon})+o(1).              \tag{6.8}
\]

Indeed, the first derivative is

\[
 \left.
 \left(
 \sum_{i=1}^q{1\over f+\varepsilon+i}
 +2\sum_{j=0}^{q-1}{1\over m-2f-\varepsilon-j}
 \right)\right|_{f=\bar f_{q,\varepsilon}}
 ={8q\over m}+O_a(m^{-1}),                                 \tag{6.9}
\]

while the second derivative is \(O_a(q/m^2)\); its contribution on an
\(O(\sqrt m\log m)\) band is \(o(1)\). Direct expansion at the saddle
gives the constant term \(-q^2/m+o(1)\). Chebyshev's inequality and
(6.3) put \(F\) in that band with probability \(1-o(1)\). Equations
(6.6), (6.8), and Slutsky's theorem prove (6.1). \(\square\)

The first moment is consistent with the global ledger:

\[
 \mathbb E R_a=e^{a^2}
 =\lim {W\over N_q}.                                       \tag{6.10}
\]

The point is that the mean comes from a broad lognormal type distribution;
the individual type ratio is not concentrated near this global mean.

## 7. Quantitative Gaussian-window obstruction

Let \(\Phi\) denote the standard normal distribution function. Define

\[
 \kappa(a)=\mathbb E(1-R_a)_+
 =\Phi(a/2)-e^{a^2}\Phi(-3a/2)>0.                          \tag{7.1}
\]

For an integer \(k\ge1\), put

\[
 z_k={\log k+a^2\over2a},
 \qquad
 \Lambda_k(a)=\mathbb E(k-R_a)_+
 =k\Phi(z_k)-e^{a^2}\Phi(z_k-2a)>0.                        \tag{7.2}
\]

Finally, put

\[
 \Gamma(a)=\mathbb Ep_*(R_a)-p_*(e^{a^2}).                 \tag{7.3}
\]

Since \(p_*\) is convex and the law of \(R_a\) has a positive density on
all of \((0,\infty)\), strict Jensen inequality gives

\[
                         \Gamma(a)>0.                       \tag{7.4}
\]

An explicit convergent form is

\[
 \Gamma(a)=
 \sum_{j\ge1}
 \left(e^{a^2}\Phi(2a-z_j)-j\Phi(-z_j)\right)
 -p_*(e^{a^2}).                                             \tag{7.5}
\]

### Theorem 7.1 (native fixed-pair Gaussian no-go)

Suppose \(q/\sqrt m\to a>0\). Every completed factor whose depth-\(q\)
windows remain inside one fixed coordinate-pair system satisfies

\[
 {h_q\over N_q}\ge\kappa(a)+o(1),                          \tag{7.6}
\]

\[
 {\Pi_q\over N_q}\ge\Gamma(a)+o(1),                        \tag{7.7}
\]

and, along every subsequence on which \(c_q=k\),

\[
 {L_q\over N_q}\ge\Lambda_k(a)+o(1).                       \tag{7.8}
\]

In particular,

\[
 {O_q\over c_qW}
 \ge {e^{-a^2}\over k}\Lambda_k(a)+o(1)>0.                 \tag{7.9}
\]

#### Proof

Divide (5.5) by \(N_q\). Its right side is

\[
 \mathbb E(1-R_m)_+,
\]

which tends to (7.1) by Lemma 6.1. This proves (7.6).

Since \(P_q^{\min}=N_qp_*(W/N_q)\), (5.7) gives

\[
 {\Pi_q\over N_q}
 \ge\mathbb Ep_*(R_m)-p_*(W/N_q).
\]

The function \(p_*\) is nonnegative and continuous. The Portmanteau
theorem and Lemma 6.1 give

\[
 \liminf_m\mathbb Ep_*(R_m)\ge\mathbb Ep_*(R_a).
\]

Since \(W/N_q\to e^{a^2}\), this proves (7.7).

Similarly, (5.6) divided by \(N_q\) is

\[
 {L_q\over N_q}\ge\mathbb E(c_q-R_m)_+.
\]

On a subsequence with \(c_q=k\), its limit is (7.2), proving (7.8).
Finally \(O_q\ge L_q\), \(N_q/W\to e^{-a^2}\), and \(c_q=k\), which gives
(7.9). \(\square\)

If \(e^{a^2}\) is not an integer, then eventually
\(k=\lfloor e^{a^2}\rfloor\). If \(e^{a^2}\) is an integer, \(c_q\) has
at most the two adjacent subsequential values; (7.2) is positive for both.
Thus (7.9) has a positive liminf without excluding the boundary case.

One depth \(q\sim a\sqrt m\) already contributes \(\Omega_a(W)\) to the
fixed-window MWB sum. Hence, for every fixed \(A>0\), a single native
fixed-pair system fails the window \(q\le A\sqrt m\): choose any
\(0<a<A\). This conclusion is unaffected by perfect local rainbow
properties, direction diversity, or coupling among the cycles inside that
one matching. Complementation gives the identical obstruction for the
upper target histogram.

## 8. The correct mixed-cube sufficient condition

The preceding no-go is specific to one fixed global matching. Suppose now
that coordinate-conjugate cube systems or other legal cube-cycle blocks are
mixed, and let the completed lower and upper histograms be
\(\mu_q^-\) and \(\mu_q^+\). Apply the definitions above to each sign and
write \(\Pi_q^\pm\), \(O_q^\pm\).

For

\[
                         H_A=\lceil A\sqrt m\rceil,
\]

the exact ratio is

\[
 {W\over N_q}
 =\prod_{i=1}^q{m+1+i\over m-q+i},
 \qquad
 \log{W\over N_q}
 ={q(q+1)\over m}+O_A(m^{-1/2}).                            \tag{8.1}
\]

Thus \(1\le c_q\le C_A\) uniformly in this window.

### Theorem 8.1 (joint pair-energy bridge to MWB)

If, for every fixed \(A>0\), completed mixed cube-cycle factors can be
chosen so that

\[
 \boxed{
 \sum_{q=1}^{H_A}{\Pi_q^-+\Pi_q^+\over c_q}=o(W),}          \tag{8.2}
\]

then

\[
 \sum_{q=1}^{H_A}{O_q^-+O_q^+\over c_q}=o(W).              \tag{8.3}
\]

In particular the one-sided version gives the exact fixed-window MWB
condition, and the usual diagonalization yields the coefficient-one
conclusion.

#### Proof

Apply (2.6) at every depth and to each sign, divide by \(c_q\), and sum.
No synchronization or independence statement is used. \(\square\)

Using (2.5), condition (8.2) is equivalently

\[
 \sum_{q=1}^{H_A}{1\over2c_q}
 \sum_{\sigma\in\{-,+\}}
 \left[
 \|\mu_q^\sigma-\lambda_q\mathbf1\|_2^2
 -N_q\theta_q(1-\theta_q)
 \right]=o(W).                                             \tag{8.4}
\]

Using the actual cube-cycle overlaps in (4.3), it is equivalently

\[
 \sum_{q=1}^{H_A}{1\over c_q}
 \sum_{\sigma\in\{-,+\}}
 \left[
 \sum_\alpha\sum_S
       \binom{x_{\alpha,q}^\sigma(S)}2
 +\sum_{\alpha<\beta}C_{\alpha\beta,q}^\sigma
 -P_q^{\min}
 \right]=o(W).                                             \tag{8.5}
\]

If every cube block is shadow-simple throughout the window, the internal
terms vanish. The exact requirement becomes

\[
 \sum_{q=1}^{H_A}{1\over c_q}
 \sum_{\sigma\in\{-,+\}}
 \left[
 \sum_{\alpha<\beta}
 |\mathcal S_{\alpha,q}^\sigma
       \cap\mathcal S_{\beta,q}^\sigma|
 -P_q^{\min}
 \right]=o(W).                                             \tag{8.6}
\]

This is the promised joint criterion. The subtraction of
\(P_q^{\min}\) is essential: at Gaussian depth the balanced histogram
itself has \(\Theta_A(W)\) collision pairs. What must be small is the
excess above that compulsory baseline, not the raw number of collisions.

A convenient stronger, depthwise condition is

\[
 \Pi_q^-+\Pi_q^+
 \le {\epsilon_mW\over\sqrt m}
 \quad(1\le q\le H_A),
 \qquad \epsilon_m\longrightarrow0.                        \tag{8.7}
\]

Indeed, (8.7), \(H_A=O_A(\sqrt m)\), and \(c_q\ge1\) imply (8.2).
Condition (8.7) is not asserted to be necessary; the weighted sum (8.2)
is the sharp sufficient statement supplied by pair energy.

## 9. Exact boundary

The fixed-pair cube results therefore split cleanly.

1. A recursive cube factor may be exactly two-sided shadow-rainbow inside
   every individual cube. This removes its internal term in (4.3).
2. One native global matching nevertheless has the immutable type defect
   (7.6)--(7.9). Local rainbow structure cannot repair it.
3. Mixing conjugate pair systems is necessary to escape that obstruction.
4. After mixing, near-coverage remains only a support statement. The
   remaining theorem is the genuinely joint overlap estimate (8.5), or
   (8.6) for locally simple cube factors. Marginal hit probabilities do
   not imply it.

Thus the fixed-pair cube construction is a valid local factor library, but
its coefficient-one use requires a correlated global selection whose
pair-collision excess is summable through every fixed Gaussian window.
