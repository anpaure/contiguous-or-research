# Rotating-frame two-port packet heat on exact factors

## Exact conditional stationary theorem, phase-age cut, detailed-balance obstruction, and a high-energy intrinsic packet cube

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computational experiment is used.

## 0. Verdict

Let

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\operatorname{Cat}_m=\frac Wn,
 \qquad H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\). Throughout, \(m\ge m_0(A)\) is sufficiently large that
\(1\le H\le m-2\). There is an exact positive theorem for any completed
rotating-frame packet chain. The particular same-phase entry-neutral
two-port compiler which motivated it is no longer open: the audited
phase-residence invariant refutes that gadget at the requested length.

Suppose a rotating packet gadget completes, after forgetting all auxiliary
labels, to an injective cube of literal squarefree exact middle wreath
factors

\[
 \{F_\varepsilon:\varepsilon\in\{-1,+1\}^s\},
 \qquad
 f^{F_\varepsilon}
 =\bar f+\frac12\sum_{i=1}^s\varepsilon_i z_i,
\tag{0.1}
\]

and suppose every bit is an intrinsic reverse-closed exact-factor switch.
Put

\[
 Z=\sum_i z_i,
 \qquad
 G=\|Z\|_H^2-\sum_i\|z_i\|_H^2.
\tag{0.2}
\]

If \(F^-\) and \(F^+\) are the two coherent endpoints, then fair packet
Haar has the exact stationary floor-energy identity

\[
 \boxed{
 \mathbb E_{\varepsilon}\mathcal Q_H(F_\varepsilon)
 =\frac{\mathcal Q_H(F^-)+\mathcal Q_H(F^+)}2
 -\frac14G.}
\tag{0.3}
\]

There is no omitted floor term. For a rainbow packet family which separates
captured equal-target occurrence pairs of total weighted count \(C_w\),
the audited nonnegative-Gram property gives

\[
 G\ge2C_w,
\tag{0.4}
\]

so the exact Haar gain is at least \(C_w/2\).

This yields a quantitative conditional theorem. Put

\[
 R_A=C_AHB.
\]

Assume every exact factor \(F\) with \(\mathcal Q_H(F)>R_A\) is one
coherent endpoint of such a completed cube, that its selected packets obey
\(G\ge2C_w\), and that constants
\(\rho_A>0\), \(\sigma_A<\rho_A/4\) satisfy

\[
 C_w\ge\frac{\rho_A}{2}
       \bigl(\mathcal Q_H(F)-R_A\bigr),
\tag{0.5}
\]

\[
 \frac{\mathcal Q_H(F^+)-\mathcal Q_H(F)}2
 \le \sigma_A\bigl(\mathcal Q_H(F)-R_A\bigr).
\tag{0.6}
\]

Uniformly resampling the selected cube above level \(R_A\), and holding
below it, gives an exact-factor Markov kernel satisfying

\[
 \boxed{
 K\mathcal Q_H(F)-\mathcal Q_H(F)
 \le-\left(\frac{\rho_A}{4}-\sigma_A\right)
       \bigl(\mathcal Q_H(F)-R_A\bigr).}
\tag{0.7}
\]

Every stationary law of this kernel is supported on
\(\mathcal Q_H\le R_A\). In particular, a literal exact factor with

\[
 \mathcal Q_H=O_A(H\operatorname{Cat}_m)=o(W)
\]

exists. This is sufficient for the frozen constant-one diagonalization.
More precisely, if the hypotheses hold for every fixed \(A\), the usual
slow diagonal in \(A\) gives the constant-one theorem.

The requested same-phase rotating-frame seam does **not** furnish the
hypotheses above, because it does not exist at length
\(|\mathcal P|+O(1)\). If \(p\) switched requests from one source phase and
depth are placed on one path physical through depth \(H\), the exact
phase-age cut gives

\[
 L\ge1+(p-1)(H+q).
\tag{0.6a}
\]

Thus even \(p=2\) needs overhead at least \(H+q-1\), independently of the
two ports. A different cross-phase or age-compatible gadget, if used to
instantiate this factor-chain route, would still need one unlabelled exact
factor at every simultaneous packet corner, an intrinsic reverse
dictionary after rebasing, and the endpoint surcharge estimate (0.6). A
direct literal-OR construction may bypass factor completion, but must prove
its own exact coverage and word-length ledger.

There are two exact detailed-balance obstructions.

1. For a fixed sequence of self-adjoint packet heats
   \(H_0,\ldots,H_{L-1}\), the forward-period skeleton

   \[
   P_\to=H_0H_1\cdots H_{L-1}
   \]

   is doubly stochastic, but

   \[
   P_\to^*=H_{L-1}\cdots H_1H_0.
   \]

   Thus uniform detailed balance is equivalent to equality of the weighted
   forward and reverse-order packet-word counts. Rotation does not imply
   this equality. For two frames it is exactly the commutation condition
   \(H_1H_0=H_0H_1\).

2. Even if every packet word has a weight-preserving reverse, choosing
   uniformly among the packets currently enabled at \(F\) gives stationary
   factor weight proportional to the enabled packet degree \(d(F)\), not
   counting-uniform weight. Uniformity requires constant degree or a global
   padded proposal catalogue. Without reciprocal support and the
   Kolmogorov cycle identities, no positive reversible law exists at all.

Finally, reversibility is not the missing energy theorem. There is a
positive-density intrinsic exact packet cube of dimension

\[
 d_m=\operatorname{Cat}_{m-2}\sim \frac1{16}B
\]

inside the canonical MSW factor. Every subset of its root-disjoint
two-for-two packets is a literal exact factor; the packet flips commute and
are intrinsic involutions. Nevertheless every corner satisfies

\[
 \boxed{
 Q_1\ge
 2\left((2m-7)\operatorname{Cat}_{m-2}
       -\frac{2W}{m+2}\right)
 =\left(\frac18-o(1)\right)W.}
\tag{0.8}
\]

Hence its fair packet heat is symmetric, reverse-closed, and stationary,
but

\[
 \frac{\mathbb E\mathcal Q_H}{HB}
 \ge\left(\frac1{4A}-o(1)\right)\sqrt m\longrightarrow\infty.
\tag{0.9}
\]

These local MSW packets are not asserted to possess the proposed
entry-neutral rotating-frame word geometry. Their role is decisive but
properly scoped: exact packet existence, positive density, intrinsicness,
reverse closure, detailed balance, and stationarity do not imply a
Catalan-scale mean. The same-phase rotating compiler is independently
impossible by (0.6a). Any materially different surviving cross-phase,
age-compatible, or direct-OR gadget must contribute the new quantitative
content in (0.5)--(0.6), or an equivalent stationary
coherent-versus-restitution estimate.

## 1. Exact factors and floor normalization

Let \(\mathfrak F_m\) be the finite set of literal squarefree exact middle
wreath factors on \([n]\). Thus every \(F\in\mathfrak F_m\) consists of
\(B\) unoriented cyclic orders and their middle interval families partition
\(\binom{[n]}m\).

For \(1\le q\le H\), put

\[
 r_q=m-q,\qquad
 N_q=\binom n{r_q},\qquad
 \lambda_q=\frac W{N_q}=c_q+\theta_q,
 \qquad c_q=\lfloor\lambda_q\rfloor,
 \quad0\le\theta_q<1.
\tag{1.1}
\]

For sufficiently large \(m=m(A)\), all \(c_q\ge1\). Let
\(\mu_q^F(S)\) be the number of rows of \(F\) in which \(S\) is a cyclic
rank-\(r_q\) interval, and define

\[
 f_q^F=\mu_q^F-\lambda_q\mathbf1,
 \qquad
 \beta_q=N_q\theta_q(1-\theta_q).
\tag{1.2}
\]

Use

\[
 \langle x,y\rangle_H
 =\sum_{q=1}^H\frac{\langle x_q,y_q\rangle_2}{c_q},
 \qquad
 \|x\|_H^2=\langle x,x\rangle_H,
\tag{1.3}
\]

and

\[
 \mathfrak B_H=\sum_{q=1}^H\frac{\beta_q}{c_q}.
\tag{1.4}
\]

The unhalved factorial-floor energy is

\[
\begin{aligned}
 \mathcal Q_H(F)
 &=\sum_{q=1}^H\frac1{c_q}
   \sum_{S\in\binom{[n]}{r_q}}
   (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)\\
 &=\|f^F\|_H^2-\mathfrak B_H.
\end{aligned}
\tag{1.5}
\]

Every numerator product in the first line is a nonnegative integer; after
division by \(c_q\), \(\mathcal Q_H\) need not be integral. Every exact
factor has total mass \(W\) at every displayed rank, so the floor baseline
\(\mathfrak B_H\) is the same at every exact state.

At depth one,

\[
 \lambda_1
 =\frac{\binom{2m+1}m}{\binom{2m+1}{m-1}}
 =\frac{m+2}{m},
\]

so \(c_1=1\) for \(m\ge3\).

A framed chain may have a finite augmented state space \(\mathcal X_m\)
and a projection

\[
 \operatorname{fac}:\mathcal X_m\longrightarrow\mathfrak F_m.
\]

The energy of \(x\in\mathcal X_m\) means
\(\mathcal Q_H(\operatorname{fac}(x))\). Every claim below which calls a
trajectory an exact-factor trajectory requires every intermediate
projected state, not only the two macro endpoints, to belong to
\(\mathfrak F_m\).

Sections 3--4 use factor-skeleton kernels directly on
\(\mathfrak F_m\): a rotating frame is internal data of one macro
transition. Section 5.2 separately analyzes the genuinely lifted
phase-by-phase chain.

## 2. The exact stationary ledger for an arbitrary macro-step

The first identity is independent of reversibility and of the particular
packet geometry.

### Theorem 2.1 (coherent-versus-restitution identity)

Let \(P\) be any Markov kernel on a finite framed exact-factor state space.
At \(x\), let \(Y\) be the next state and abbreviate

\[
 f_x=f^{\operatorname{fac}(x)},
 \qquad
 \bar f_x=\mathbb E[f^{\operatorname{fac}(Y)}\mid x].
\]

Define

\[
 R_P(x)
 =\mathbb E\bigl[
   \|f^{\operatorname{fac}(Y)}-\bar f_x\|_H^2
   \mid x\bigr],
\tag{2.1}
\]

\[
 A_P(x)=\|f_x\|_H^2-\|\bar f_x\|_H^2.
\tag{2.2}
\]

Then, exactly,

\[
 \boxed{
 (P\mathcal Q_H)(x)-\mathcal Q_H(x)
 =R_P(x)-A_P(x).}
\tag{2.3}
\]

Consequently every stationary law \(\pi\) satisfies

\[
 \boxed{\mathbb E_\pi R_P=\mathbb E_\pi A_P.}
\tag{2.4}
\]

#### Proof

Conditional variance in the Hilbert space gives

\[
 \mathbb E[\|f_Y\|_H^2\mid x]
 =\|\bar f_x\|_H^2+R_P(x).
\]

Subtract \(\|f_x\|_H^2\). The common floor constant
\(\mathfrak B_H\) cancels, proving (2.3). Integrating (2.3) against a
stationary law proves (2.4). \(\square\)

Equation (2.4) is an equality, not an upper bound. It isolates exactly the
extra estimate a packet gadget must provide.

### Theorem 2.2 (class-average conditional stationary bound)

Let \(\pi\) be stationary on one closed framed class. Suppose, for some
\(\kappa>0\), \(\delta>0\), and \(C_0,C_1\ge0\),

\[
 \mathbb E_\pi A_P
 \ge\kappa\,\mathbb E_\pi\mathcal Q_H-C_0HB,
\tag{2.5}
\]

and

\[
 \mathbb E_\pi R_P
 \le(1-\delta)\mathbb E_\pi A_P+C_1HB.
\tag{2.6}
\]

Then

\[
 \boxed{
 \mathbb E_\pi\mathcal Q_H
 \le
 \frac{C_0+C_1/\delta}{\kappa}\,HB.}
\tag{2.7}
\]

#### Proof

By (2.4), (2.6) gives

\[
 \delta\mathbb E_\pi A_P\le C_1HB.
\]

Insert this upper bound in (2.5) and divide by \(\kappa\). \(\square\)

Thus an \(O_A(HB)\) conclusion follows precisely when

\[
 \frac{C_0+C_1/\delta}{\kappa}=O_A(1).
\tag{2.8}
\]

No pointwise Lyapunov inequality is required for Theorem 2.2. On the other
hand, neither double stochasticity nor detailed balance supplies (2.5) or
(2.6).

## 3. Completed rotating two-port cubes

The current physical seam must be strengthened before it defines an
exact-factor heat cell. The needed object is recorded explicitly.

### Definition 3.1 (completed exact rotating packet cube)

A pointed completed packet cube based at an exact factor \(F\) consists of
the following data.

1. There are \(s\) packet bits and an injective map

   \[
   \varepsilon\longmapsto F_\varepsilon
   \quad(\varepsilon\in\{-1,+1\}^s)
   \]

   into \(\mathfrak F_m\). Every corner is one unlabelled squarefree exact
   factor, not a collection of rows borrowed from differently labelled
   auxiliary factor copies.

2. Every individual bit flip and every prescribed rotating-frame
   realization between corners is a finite path all of whose intermediate
   states are exact factors. The two physical ports and the output frame
   are independent of the packet signs.

3. There are stacked load increments \(z_1,\ldots,z_s\) such that (0.1)
   holds. Equivalently, packet effects add without a choice-dependent
   completion term.

4. For every corner and every \(i\), the same persisted packet label
   identifies the inverse flip

   \[
   T_iF_\varepsilon=F_{\varepsilon\oplus e_i}.
   \tag{3.1}
   \]

   Thus every \(T_i\) is an involution on the cube. This is the intrinsic
   rebasing and reverse-dictionary condition.

The port condition alone is item 2. It does not imply items 1, 3, or 4.

### Theorem 3.2 (exact cube floor identity)

For a completed exact packet cube, put

\[
 Z=\sum_i z_i,
 \qquad
 G=\|Z\|_H^2-\sum_i\|z_i\|_H^2.
\tag{3.2}
\]

Let \(F^-\) be the all-minus corner and \(F^+\) the all-plus corner.
Then (0.3) holds:

\[
 \mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
 =\frac{\mathcal Q_H(F^-)+\mathcal Q_H(F^+)}2
 -\frac14G.
\tag{3.3}
\]

#### Proof

Independent fair signs have mean zero and pairwise zero covariance. Hence

\[
 \mathbb E_\varepsilon\|f^{F_\varepsilon}\|_H^2
 =\|\bar f\|_H^2+\frac14\sum_i\|z_i\|_H^2.
\tag{3.4}
\]

The coherent endpoint profiles are

\[
 f^{F^-}=\bar f-\frac12Z,
 \qquad
 f^{F^+}=\bar f+\frac12Z.
\]

Therefore

\[
 \frac{\|f^{F^-}\|_H^2+\|f^{F^+}\|_H^2}{2}
 =\|\bar f\|_H^2+\frac14\|Z\|_H^2.
\tag{3.5}
\]

Subtract (3.4) from (3.5), and subtract the same
\(\mathfrak B_H\) from every energy. This proves (3.3). \(\square\)

The factor \(1/4\) is exact for the unhalved energy (1.5).

### Proposition 3.3 (exact collision/floor conversion)

At depth \(q\), define

\[
 \operatorname{Coll}_q(F)
 =\sum_S\binom{\mu_q^F(S)}2.
\tag{3.6}
\]

The minimum collision count among integral load vectors of total mass
\(W\) on \(N_q\) targets is

\[
 \operatorname{Coll}^{\min}_q
 =c_qW-\frac{N_qc_q(c_q+1)}2.
\tag{3.7}
\]

Moreover,

\[
 \boxed{
 Q_q(F)
 =2\bigl(
 \operatorname{Coll}_q(F)-\operatorname{Coll}^{\min}_q
 \bigr),}
\tag{3.8}
\]

and hence

\[
 \boxed{
 \mathcal Q_H(F)
 =2\sum_{q=1}^H\frac{
 \operatorname{Coll}_q(F)-\operatorname{Coll}^{\min}_q}{c_q}.}
\tag{3.9}
\]

#### Proof

Writing \(W=N_qc_q+r_q'\), the balanced integral profile has
\(N_q-r_q'\) coordinates equal to \(c_q\) and \(r_q'\) equal to
\(c_q+1\). Its collision count is

\[
 N_q\binom{c_q}{2}+r_q'c_q
 =c_qW-\frac{N_qc_q(c_q+1)}2.
\]

Also

\[
\begin{aligned}
 Q_q(F)
 &=\sum_S\bigl[
   \mu_q(S)^2-(2c_q+1)\mu_q(S)+c_q(c_q+1)
   \bigr]\\
 &=2\operatorname{Coll}_q(F)-2c_qW+N_qc_q(c_q+1),
\end{aligned}
\]

which is (3.8). Weighting proves (3.9). \(\square\)

Thus the total weighted excess-collision mass is exactly
\(\mathcal Q_H/2\).

### Proposition 3.4 (rainbow Gram capture)

Suppose the packet increments have the form

\[
 z_P=\sum_{i\in P}d_i
\]

over rainbow occurrence packets. Write \((d_i)_q\) for the depth-\(q\)
component. Assume, whenever \(i,j\) lie in different packets,

\[
 \langle(d_i)_r,(d_j)_r\rangle_2\ge0
 \qquad(1\le r\le H).
\tag{3.10}
\]

Let \(\mathscr C^\sharp\) be a set of captured pair-depth incidences
\((\{i,j\},q)\), where \(i,j\) lie in different packets, their occurrences
have the same depth-\(q\) target, and

\[
 \langle(d_i)_q,(d_j)_q\rangle_2\ge1.
\tag{3.10a}
\]

The same unordered pair may be credited at several depths only through
distinct incidences in \(\mathscr C^\sharp\). Put

\[
 C_w=\sum_{(\{i,j\},q)\in\mathscr C^\sharp}\frac1{c_q}.
\tag{3.10b}
\]

Define \(G\) by (3.2) with the packet increments \(z_P\). Then

\[
 \boxed{G\ge2C_w.}
\tag{3.11}
\]

#### Proof

Expanding packet sums gives

\[
 G=2\sum_{P<Q}\langle z_P,z_Q\rangle_H.
\]

Every term is nonnegative. Each captured pair occurs in one cross-packet
inner product. Its credited rank-\(q\) component contributes at least
\(2/c_q\) after the leading factor two. If the same pair is credited at
several depths, the corresponding orthogonal rank components add; (3.10)
prevents a negative uncredited rank from cancelling them. Summing proves
(3.11). \(\square\)

### Theorem 3.5 (exact current-endpoint biased packet law)

Let a completed exact cube be pointed at one corner \(F\), and use
\(0/1\) coordinates

\[
 f^{F_\xi}=f^F+\sum_{i=1}^s\xi_i d_i,
 \qquad \xi_i\in\{0,1\}.
\tag{3.12}
\]

Put

\[
 G_F=\left\|\sum_i d_i\right\|_H^2-\sum_i\|d_i\|_H^2,
\tag{3.13}
\]

\[
 D_F=-\left\langle f^F,\sum_i d_i\right\rangle_H
     -\frac12\sum_i\|d_i\|_H^2.
\tag{3.14}
\]

If the bits are independent Bernoulli variables of common mean
\(t\in[0,1]\), then

\[
 \boxed{
 \mathbb E_t\mathcal Q_H(F_\xi)-\mathcal Q_H(F)
 =t^2G_F-2tD_F.}
\tag{3.15}
\]

If \(G_F\ge0\), the maximum expected descent over \(t\in[0,1]\) is

\[
 \boxed{
 \Psi(D_F,G_F)=
 \begin{cases}
 0,&D_F\le0,\\[1mm]
 D_F^2/G_F,&0<D_F<G_F,\\[1mm]
 2D_F-G_F,&D_F\ge G_F>0,\\[1mm]
 2D_F,&G_F=0<D_F.
 \end{cases}}
\tag{3.16}
\]

#### Proof

The exact quadratic expansion is

\[
\begin{aligned}
 \mathbb E_t\mathcal Q_H(F_\xi)-\mathcal Q_H(F)
 &=2t\left\langle f^F,\sum_i d_i\right\rangle_H
   +t\sum_i\|d_i\|_H^2\\
 &\qquad
   +2t^2\sum_{i<j}\langle d_i,d_j\rangle_H.
\end{aligned}
\]

The last line's cross term is \(t^2G_F\), and the first two terms are
\(-2tD_F\), proving (3.15). The fixed rank masses make every floor
baseline cancel. Minimizing the convex quadratic
\(t^2G_F-2tD_F\) on \([0,1]\) gives (3.16). \(\square\)

Formula (3.15) is the exact point at which a state-dependent packet
orientation enters. The optimizer uses the current loads through \(D_F\).
It need not assign the same transition weight to the reverse packet at a
child, and therefore does not automatically define a reversible heat.

## 4. Conditional Catalan-scale stationary theorems

### Theorem 4.1 (one completed cube)

On a completed exact packet cube, independently replace every bit by a fair
sign. The resulting kernel is uniform averaging on the cube. It is a
stochastic self-adjoint idempotent, and the uniform cube law is its unique
stationary law. If

\[
 \frac{\mathcal Q_H(F^-)+\mathcal Q_H(F^+)}2
 -\frac14G
 \le C_AHB,
\tag{4.1}
\]

then the stationary mean is at most \(C_AHB\), and some literal exact
corner has energy at most \(C_AHB\).

#### Proof

Intrinsic bit flips identify the corner set independently of the base
corner. Uniform resampling is therefore one partition projection. Formula
(3.3) evaluates its stationary mean. At least one member of a finite set is
no larger than its average. \(\square\)

### Theorem 4.2 (adaptive rotating-packet stationary theorem)

Fix constants \(C_A<\infty\), \(\rho_A>0\), and
\(0\le\sigma_A<\rho_A/4\), and put

\[
 R_A=C_AHB.
\]

Assume that, for every exact factor \(F\) with
\(\mathcal Q_H(F)>R_A\), a completed packet cube is available with
\(F=F^-\), and that (0.5)--(0.6) and

\[
 G(F)\ge2C_w(F)
\tag{4.1a}
\]

hold. Fix one such cube deterministically at every \(F\). Define a kernel
\(K\) by uniformly resampling that cube at such a factor and holding at
every factor with
\(\mathcal Q_H\le R_A\).

Then

\[
 K\mathcal Q_H(F)-\mathcal Q_H(F)
 \le-\gamma_A
 \bigl(\mathcal Q_H(F)-R_A\bigr)
 \quad\text{above }R_A,
\tag{4.2}
\]

where

\[
 \boxed{\gamma_A=\rho_A/4-\sigma_A>0.}
\tag{4.3}
\]

Every stationary law of \(K\) is supported on
\(\mathcal Q_H\le R_A\). Consequently the hypotheses themselves force the
existence of a literal exact factor satisfying

\[
 \mathcal Q_H(F)\le C_AH\operatorname{Cat}_m.
\tag{4.4}
\]

#### Proof

By (3.3), viewed from the coherent endpoint \(F=F^-\),

\[
 K\mathcal Q_H(F)-\mathcal Q_H(F)
 =\frac{\mathcal Q_H(F^+)-\mathcal Q_H(F)}2-\frac14G.
\tag{4.5}
\]

Equations (0.4)--(0.6) imply

\[
 \frac14G\ge\frac12C_w
 \ge\frac{\rho_A}{4}
       \bigl(\mathcal Q_H(F)-R_A\bigr).
\]

Substitution in (4.5) proves (4.2).

Every finite Markov kernel has a stationary law \(\pi\). Since low states
hold, and (4.2) applies at high states,

\[
 0=\mathbb E_\pi(K\mathcal Q_H-\mathcal Q_H)
 \le-\gamma_A
 \mathbb E_\pi(\mathcal Q_H-R_A)_+.
\]

Hence \((\mathcal Q_H-R_A)_+=0\) \(\pi\)-almost surely. This also shows
that the low set cannot be empty. Projecting any state in its support gives
(4.4). \(\square\)

If the opposite coherent endpoint never has larger energy and the packets
capture all weighted excess collisions beyond the reserve, one may take
\(\sigma_A=0\) and \(\rho_A=1\). The exact contraction coefficient in
(4.2) is then \(1/4\).

Theorem 4.2 does not assert reversibility. In fact a current-relative
choice of the better oriented packet is normally incompatible with
uniform detailed balance. The point of the theorem is that reversibility is
not needed once the exact drift is proved.

### Corollary 4.3 (current-gain stationary gate)

Suppose every exact factor \(F\) is assigned a completed cube with
\(G_F\ge0\), and the kernel uses the optimizing bias from Theorem 3.5.
If, for some \(\eta_A>0\), \(C_A<\infty\),

\[
 \Psi(D_F,G_F)
 \ge\frac{\eta_A}{n}\mathcal Q_H(F)
     -\frac{C_A}{n}HB
\tag{4.6}
\]

at every state, then every stationary law \(\pi\) satisfies

\[
 \boxed{
 \mathbb E_\pi\mathcal Q_H
 \le\frac{C_A}{\eta_A}HB.}
\tag{4.7}
\]

#### Proof

The optimized kernel has exact drift

\[
 K\mathcal Q_H-\mathcal Q_H=-\Psi(D_F,G_F)
\]

by (3.15)--(3.16). Stationarity gives
\(\mathbb E_\pi\Psi=0\). Averaging (4.6) proves (4.7).
\(\square\)

This is a sufficient packet-gadget theorem, not an established inequality.
It makes the remaining quantitative gate explicit without invoking
detailed balance.

## 5. The exact detailed-balance obstruction

### 5.1 Fixed labelled packet involutions

Let \(T_{j,a}\) be a packet switch with frame phase \(j\) and persistent
label \(a\). To define a genuine heat cell, require \(T_{j,a}\) to be a
total involution of \(\mathfrak F_m\): it swaps the two exact endpoints on
its intrinsic legal domain and fixes factors where the labelled packet is
unavailable. Endpoint exactness at one base factor does not prove this
rebasing property.

For state-independent weights

\[
 \alpha_{j,a}\ge0,
 \qquad \sum_a\alpha_{j,a}=1,
\]

put

\[
 H_j=\sum_a\alpha_{j,a}\frac{I+U_{T_{j,a}}}{2},
\tag{5.1}
\]

where \(U_T\phi(F)=\phi(TF)\). Every \(H_j\) is stochastic,
self-adjoint, positive semidefinite, and doubly stochastic.

### Theorem 5.1 (forward-period and reverse-period criterion)

Apply the phases in chronological order and observe the chain only after a
full period:

Here kernels act on functions by
\((H\phi)(F)=\sum_GH(F,G)\phi(G)\). Thus chronological application of
\(H_0\), then \(H_1\), and so on has product in the displayed order.

\[
 P_\to=H_0H_1\cdots H_{L-1}.
\tag{5.2}
\]

Its endpoint multiplicities are explicitly

\[
\begin{aligned}
 P_\to(F,G)
 =\sum_{\substack{a_0,\ldots,a_{L-1}\\
                  \varepsilon\in\{0,1\}^L}}
 2^{-L}\left(\prod_{j=0}^{L-1}\alpha_{j,a_j}\right)
 {\bf1}\!\left\{
 G=T_{L-1,a_{L-1}}^{\varepsilon_{L-1}}
   \cdots T_{0,a_0}^{\varepsilon_0}F
 \right\}.
\end{aligned}
\tag{5.2a}
\]

Thus parallel packet histories are counted with their full aggregate
weight; they may not be collapsed to one endpoint edge.

Then:

1. \(P_\to\) is doubly stochastic, so counting measure is stationary;

2. every communicating class is closed and has the uniform law as its
   unique stationary law;

3. the exact adjoint is

   \[
   \boxed{P_\to^*=P_\leftarrow=H_{L-1}\cdots H_1H_0;}
   \tag{5.3}
   \]

4. uniform detailed balance holds exactly when

   \[
   \boxed{P_\to=P_\leftarrow.}
   \tag{5.4}
   \]

Equivalently, for every pair \(F,G\), the total weight of all chronological
rotating packet words from \(F\) to \(G\) equals the total weight of their
reverse-order words from \(F\) to \(G\).

#### Proof

A product of doubly stochastic matrices is doubly stochastic. A finite
chain with a strictly positive stationary measure has no transient state;
hence its communicating classes are closed. Restricting counting measure
to a closed irreducible class gives the unique uniform stationary law.
There is a positive all-hold word, so every class is aperiodic.

Each \(H_j\) is self-adjoint. Taking the adjoint of a product reverses the
order, proving (5.3). A kernel is reversible with respect to counting
measure exactly when it is self-adjoint, proving (5.4). \(\square\)

For two deterministic packet involutions \(T_0,T_1\), with
\(H_i=(I+U_{T_i})/2\),

\[
 H_0H_1-H_1H_0
 =\frac14(U_{T_0}U_{T_1}-U_{T_1}U_{T_0}).
\tag{5.5}
\]

Thus two-frame reversibility is exactly commutation of the two induced
permutations of the exact-factor state space. For \(L>2\), pairwise
commutation is sufficient but not necessary; (5.4), or the weighted
endpoint path-count equality, is the exact criterion.

The canonical reversible factor-skeleton repair is

\[
 P_{\rm rev}=\frac12(P_\to+P_\leftarrow).
\tag{5.6}
\]

It is symmetric and stochastic. If positive semidefiniteness is desired,
use

\[
 \widehat P=\frac12(I+P_{\rm rev}).
\tag{5.7}
\]

Under the total-involution hypotheses of Section 5.1, the reverse sequence
is legal. Before those hypotheses have been proved for an endpoint-only
seam proposal, however, (5.6) is only a formal matrix expression: adjunction
cannot manufacture a missing reverse physical move.

### 5.2 The forward-only phase clock

On the microscopic lift \(\mathfrak F_m\times\mathbb Z_L\), define

\[
 \widetilde P((F,j),(G,j+1))=H_j(F,G).
\tag{5.8}
\]

Uniform measure on the lifted space is stationary, because every \(H_j\)
is doubly stochastic. If \(L\ge3\), however, no strictly positive
reversible law exists. Indeed,

\[
 \widetilde P((F,j),(F,j+1))>0
\]

from the hold term, whereas

\[
 \widetilde P((F,j+1),(F,j))=0;
\]

the forward phase clock moves from \(j+1\) to \(j+2\), not back to \(j\).
For \(L=2\), uniform detailed balance is equivalent to
\(H_0=H_1\).

A microscopic reversible repair allows both phase directions:

\[
\begin{aligned}
 K_{\rm bi}((F,j),(G,j+1))&=\frac12H_j(F,G),\\
 K_{\rm bi}((F,j),(G,j-1))&=\frac12H_{j-1}(F,G).
\end{aligned}
\tag{5.9}
\]

For \(L\ge3\), this is visibly symmetric; the coincident directions for
\(L=2\) are defined as the single entry

\[
 K_{\rm bi}((F,j),(G,j+1))
 =\frac12\bigl(H_j(F,G)+H_{j-1}(F,G)\bigr).
\tag{5.9a}
\]

Its row sum is one. Lazification gives aperiodicity and positive
semidefiniteness if needed.

There is a projection caveat. A uniform stationary law on one lifted class
projects to factor weights proportional to the number of phase states of
that factor which lie in the lifted class. Constant phase-fibre
multiplicity must be proved before calling the projected factor law
uniform. The full-period skeleton avoids this particular ambiguity.

### 5.3 State-dependent packet menus and degree bias

Let \(\mathscr P(F)\) be the finite multiset of oriented exact packet
histories proposed at factor \(F\). Parallel histories with the same
endpoint are retained. Suppose path reversal is an involution

\[
 (F,p)\longleftrightarrow(G,p^\dagger),
 \qquad G=\operatorname{end}(F,p),
\tag{5.10}
\]

and raw conductances obey

\[
 c(F,p)=c(G,p^\dagger)>0.
\tag{5.11}
\]

Put

\[
 C(F,G)=\sum_{p:F\to G}c(F,p),
 \qquad
 D(F)=\sum_GC(F,G).
\tag{5.12}
\]

Assume \(D(F)>0\) on the class under consideration; equivalently, add a
positive labelled hold history at every state. Then
\(C(F,G)=C(G,F)\). The natural normalized-menu chain

\[
 P(F,G)=\frac{C(F,G)}{D(F)}
\tag{5.13}
\]

is reversible with

\[
 \boxed{
 \pi_{\mathscr C}(F)
 =\frac{D(F)}{\sum_{X\in\mathscr C}D(X)}}
\tag{5.14}
\]

on every connected class \(\mathscr C\). It is counting-uniform on that
class if and only if \(D\) is constant along the active edges, hence
constant on \(\mathscr C\).

The stationary factor energy is therefore exactly

\[
 \boxed{
 \mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
 =\frac{\sum_{F\in\mathscr C}D(F)\mathcal Q_H(F)}
        {\sum_{F\in\mathscr C}D(F)}.}
\tag{5.15}
\]

Equivalently, writing

\[
 \mathcal Z_{\mathscr C}=\sum_{F\in\mathscr C}D(F),
\]

\[
 \mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
 =\frac1{2\mathcal Z_{\mathscr C}}
  \sum_{\substack{F\in\mathscr C\\p\in\mathscr P(F)}}c(F,p)
 \bigl[
 \mathcal Q_H(F)+
 \mathcal Q_H(\operatorname{end}(F,p))
 \bigr].
\tag{5.16}
\]

Thus a count of productive packets at their source cannot be turned into a
stationary upper bound unless their endpoint energy and the source degree
bias are also controlled.

Uniformity can be repaired without deleting packets. Choose

\[
 M\ge\max_F\sum_{G\ne F}C(F,G),
\]

put

\[
 P_M(F,G)=C(F,G)/M\quad(F\ne G),
\]

and place the unused mass on the diagonal. Then \(P_M\) is symmetric.
Equivalently, use a state-independent global label catalogue and reject an
unavailable label as a self-loop. This repair regularizes stationarity; it
does not prove an energy estimate.

Without the symmetric reversal hypothesis, write a general kernel as

\[
 P(F,G)=\frac{a(F,G)}{d(F)},
 \qquad
 d(F)=\sum_Ga(F,G).
\tag{5.17}
\]

Kolmogorov's criterion gives the exact obstruction to any positive
reversible law:

\[
 a(F,G)>0\Longleftrightarrow a(G,F)>0,
\tag{5.18}
\]

and, for every factor cycle
\(F_0,F_1,\ldots,F_\ell=F_0\),

\[
 \boxed{
 \prod_{i=0}^{\ell-1}a(F_i,F_{i+1})
 =\prod_{i=0}^{\ell-1}a(F_{i+1},F_i).}
\tag{5.19}
\]

The degree denominators cancel around the cycle. Forward packet closure
supplies neither (5.18) nor (5.19).

### 5.4 The rotating-frame reverse label

Let the physical frame be \(g\), let \(\rho\) be one frame advance, and
let a native packet map be \(S_a\). Its physical action is

\[
 gS_ag^{-1}.
\]

After the frame advances to \(g\rho\), a native label \(b\) represents
the physical reverse exactly when

\[
 (g\rho)S_b(g\rho)^{-1}=gS_a^{-1}g^{-1}.
\]

Equivalently,

\[
 \boxed{S_b=\rho^{-1}S_a^{-1}\rho.}
\tag{5.20}
\]

Closure merely under \(a\mapsto a^{-1}\) is insufficient. The packet
dictionary must be closed under the conjugated inverse (5.20), with paired
proposal weights, and the scheduler must permit the backward phase order.

Freshly recomputed exact ownership packets have an additional groupoid
effect. If a packet with \(\tau\)-invariant middle root \(U\) is switched
by a coordinate transposition \(\tau\), its natural pullback gauge on
middle sets is

\[
 \alpha_U(X)=
 \begin{cases}
  \tau X,&X\in U,\\
  X,&X\notin U.
 \end{cases}
\tag{5.21}
\]

The next coordinate move \(\rho\), pulled back through the switched state,
acts through \(\alpha_U\rho\alpha_U\). In general \(\alpha_U\) is a
piecewise permutation of the middle layer, not one coordinate permutation.
Consequently a catalogue closed under rotating coordinate conjugacies need
not contain the transported reverse port after a freshly recomputed
packet. Reversing the realized exact path in reverse chronological order is
legal; proposing that reverse path under the same forward rotating
schedule is a separate, unproved assertion.

This is the exact rebasing obstruction hidden by a purely endpoint-level
two-port statement.

To verify the pullback formula, let \(K\) be the old packet over \(U\), let
\(F'=(F\setminus K)\cup\tau K\), and identify a new row \(\tau C\) over
\(U\) with its old label \(C\). If \(o_F(X)\) denotes the owner of \(X\),
then under this row identification

\[
 o_{F'}(X)\longmapsto o_F(\alpha_UX).
\tag{5.22}
\]

Indeed, outside \(U\) the owner is unchanged, while for \(X\in U\) the
new owner is \(\tau o_F(\tau X)\), which pulls back to \(o_F(\tau X)\).
A new \(\rho\)-owner edge joins \(o_{F'}(X)\) to
\(o_{F'}(\rho X)\). Setting \(Y=\alpha_UX\) in (5.22) pulls this edge back
to the old relation

\[
 o_F(Y)\sim o_F(\alpha_U\rho\alpha_UY),
\]

as claimed.

## 6. A positive-density high-energy intrinsic packet cube

The next theorem proves that all of the algebraic heat properties above are
still insufficient without an energy-capture estimate.

### Theorem 6.1 (fixed-root MSW local packet stationary no-go)

For all sufficiently large \(m\), let \(F_m^{\rm MSW}\) be the canonical
exact MSW wreath factor. It
contains

\[
 d_m=\operatorname{Cat}_{m-2}
\tag{6.1}
\]

pairwise middle-root-disjoint \(p=0\) universal two-for-two trades. Let
\(T_1,\ldots,T_{d_m}\) be their toggles. Then:

1. every subset of the trades gives a distinct literal squarefree exact
   factor;

2. the \(T_i\)'s are commuting involutions intrinsic relative to the fixed
   root-labelled \(2^{d_m}\)-corner cube;

3. the fair single-bit heats \((I+U_{T_i})/2\), and their full product,
   are symmetric, doubly stochastic, reverse-closed exact-factor kernels
   on that closed cube;

4. every corner \(F\) satisfies

   \[
   \boxed{
   Q_1(F)\ge
   2\left((2m-7)\operatorname{Cat}_{m-2}
          -\frac{2W}{m+2}\right).}
   \tag{6.2}
   \]

In particular, uniformly on this packet cube,

\[
 \mathbb E\mathcal Q_H
 \ge\left(\frac18-o(1)\right)W,
\tag{6.3}
\]

and for fixed \(A\),

\[
 \boxed{
 \frac{\mathbb E\mathcal Q_H}{HB}
 \ge\left(\frac1{4A}-o(1)\right)\sqrt m.}
\tag{6.4}
\]

#### Proof

The exact positive-density local-chart theorem in
MATH_ATTACK_R_SUSPENDED_SHADOW_INVISIBLE_TRADES_20260725.md supplies the
\(d_m\) negative row pairs inside \(F_m^{\rm MSW}\). Their middle root
unions are disjoint, and each positive pair partitions the same root union
as its negative pair. Hence every subset may be replaced simultaneously,
and the unchanged residual completes every corner exactly.

The two sides of each trade are distinct. Restriction to its root union
therefore recovers its bit, proving injectivity of the cube. Since other
trades act on disjoint root unions, flipping one bit does not change the
availability or the inverse of any other bit. Thus the toggles are
commuting fixed-root involutions. The heat assertions follow on the
restricted cube. If a kernel on all of \(\mathfrak F_m\) is desired, each
\(T_i\) may be extended by the identity outside this cube; no claim is made
that a freshly recomputed rotating-frame catalogue canonically rediscovers
the same packet there.

It remains to prove (6.2). The audited MSW marked-gap estimate, in the
form recorded in
MATH_ATTACK_Y10_CYCLIC_CROSS_BUNDLE_HAAR_20260725.md, gives

\[
 M_1(F_m^{\rm MSW})
 \ge(2m-3)d_m-\frac{2W}{m+2}
\tag{6.5}
\]

depth-one holes. Every universal two-for-two trade changes depth-one loads
on at most four target cells. Therefore all cube corners agree with the
MSW depth-one load outside a fixed union \(U_1\) satisfying

\[
 |U_1|\le4d_m.
\tag{6.6}
\]

At least

\[
 (2m-7)d_m-\frac{2W}{m+2}
\]

of the old holes consequently remain holes at every corner. Since
\(c_1=1\), a hole contributes

\[
 (0-1)(0-2)=2
\]

to \(Q_1\). This proves (6.2).

Finally,

\[
 \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 \longrightarrow\frac1{16}.
\tag{6.7}
\]

Since \(c_1=1\), all other rank energies are nonnegative, and therefore
\(\mathcal Q_H\ge Q_1\). With
\(B=\operatorname{Cat}_m=W/n\), (6.2) gives (6.3). Also

\[
 \frac{W}{HB}=\frac nH
 =\left(\frac2A+o_A(1)\right)\sqrt m,
\]

and (6.4) follows. \(\square\)

Theorem 6.1 is stronger than a global-coordinate-orbit warning: it uses a
positive-density family of genuine local exact factor-to-factor packets,
and every inverse persists after every other packet choice. It therefore
rules out each of the following proposed black-box implications:

\[
\begin{gathered}
 \text{every positive-density packet cube has an }O_A(HB)
 \text{ stationary mean},\\
 \text{every intrinsic reversible packet heat has an }O_A(HB)
 \text{ stationary mean},\\
 \text{every large exact packet cube contains a low-energy corner}.
\end{gathered}
\]

Its scope is equally important. The \(p=0\) universal MSW trades are not
claimed to have the same physical geometry as the owner-fixed spike
compiler. The latter same-phase compiler is independently refuted in
Section 7 by a residence invariant, not by Theorem 6.1. The MSW cube
proves that any materially different surviving packet geometry must yield a
new quantitative endpoint or curvature estimate, not merely a larger exact
state graph. It does not exclude a different low class elsewhere in
\(\mathfrak F_m\), a global cross-phase schedule, or an adaptive rule using
a different special-geometry cube.

## 7. The same-phase rotating two-port compiler is impossible

The requested entry-neutral compiler would take an arbitrary rainbow
packet \(\mathcal P\) of at most \(H\) owner-fixed spikes from one source
phase \(A\) and one depth \(q\), and produce old and switched literal
realizations of length \(|\mathcal P|+O(1)\), with common entrance and
exit ports. The audited phase-residence theorem closes this object even
when the two sides are allowed unrelated ports.

The complete independent proofs are in
MATH_ATTACK_S14_ENTRY_NEUTRAL_ROTATING_FRAME_INVARIANT_20260725.md and
MATH_ATTACK_Z12_ROTATING_FRAME_TWO_PORT_FLOW_CUT_20260725.md. The core
argument is reproduced here.

### Theorem 7.1 (phase-age separation)

Let

\[
 X_0,X_1,\ldots,X_{L-1}\in\binom{[n]}m
\]

be one middle-owner path physical through depth \(H\), meaning that for
every valid start \(t\) and \(1\le h\le H\),

\[
 \left|\bigcap_{j=0}^hX_{t+j}\right|=m-h,
 \qquad
 \left|\bigcup_{j=0}^hX_{t+j}\right|=m+h.
\tag{7.1}
\]

Fix one omitted source pair \(A\) and \(1\le q\le H\). If
\(t<t'\) are two switched owner-fixed spike starts from that same
phase/depth stratum, then

\[
 \boxed{t'-t\ge H+q.}
\tag{7.2}
\]

Under the strict recursive Gray convention that every coordinate
residence is greater than \(H\), the bound is \(H+q+1\).

#### Proof

First note the residence lemma. If a coordinate \(a\) first enters at
\(X_{r-1}\to X_r\) and \(X_{r+s}\) is the first later owner omitting it,
then \(s\ge H\). Otherwise \(s<H\), and the path segment

\[
 X_{r-1},X_r,\ldots,X_{r+s}
\]

has \(s+1\le H\) transitions. One departure removes the newly entered
coordinate \(a\), so at most \(s\) of the \(s+1\) departures remove
coordinates of \(X_{r-1}\). The intersection of these owners therefore
has size at least \(m-s>m-(s+1)\), contradicting (7.1).

For the spike at \(t\), every switched upper flag below depth \(q\)
avoids \(A\), while its depth-\(q\) flag contains one coordinate
\(a\in A\). Thus \(a\) first enters at \(X_{t+q}\) and then remains
present for at least \(H\) owner states.

If \(0<t'-t<q\), put \(h=q-(t'-t)\). Then
\(1\le h<q\), and \(X_{t+q}\) lies in the depth-\(h\) upper window
starting at \(t'\). That window contains \(a\), contradicting the fact
that the second spike's flags below depth \(q\) avoid \(A\).

If \(q\le t'-t<q+H\), coordinate \(a\) is still present in the central
owner \(X_{t'}\). But every designated phase-\(A\) central owner avoids
all of \(A\). This is again a contradiction. The two cases exclude every
positive gap below \(H+q\). The strict-residence version retains \(a\)
for one further owner. \(\square\)

### Corollary 7.2 (exact packet length cut)

If one physical module contains \(p\ge1\) switched requests from one
phase/depth stratum, then

\[
 \boxed{L\ge1+(p-1)(H+q).}
\tag{7.3}
\]

Consequently a claimed length bound \(L\le p+C\) forces

\[
 \boxed{C\ge(p-1)(H+q-1).}
\tag{7.4}
\]

#### Proof

Order the starts as \(t_1<\cdots<t_p\). Summing (7.2) over consecutive
starts gives

\[
 t_p-t_1\ge(p-1)(H+q).
\]

Since \(t_p-t_1\le L-1\), this is (7.3). Successive principal owners are
distinct physical update positions, so common external ports cannot
shorten this internal span. Subtracting \(p\) from
\(p+C\ge1+(p-1)(H+q)\) gives (7.4). \(\square\)

The requested \(p+O(1)\) compiler fails already at \(p=2\) as
\(H\to\infty\), and a packet with \(p=H\) needs \(\Omega(H^2)\) principal
owners. These inequalities use only the switched realization and hence
are independent of common ports, unrelated ports, helper choices, frame
names, or occurrence order.

The obstruction is nonvacuous in every fixed Gaussian window. The exact
local phase count in
MATH_ATTACK_Z12_ROTATING_FRAME_TWO_PORT_FLOW_CUT_20260725.md shows that,
for all sufficiently large \(m\), every \(q\le H=O_A(\sqrt m)\) has at
least \(H\) distinct collision fibres. Selecting one occurrence from each
gives a genuine local-row rainbow packet of size \(H\).

Thus the independent same-phase rotating-frame packet lane is closed
before detailed balance is reached. The abstract exact-factor theorems in
Sections 2--5 can apply only to a different surviving gadget, such as:

1. a global schedule interleaving different source phases during their
   forced residence intervals;
2. an age-compatible packetization constructed from the physical
   chronology rather than an arbitrary collision-rainbow bin; or
3. a noncanonical direct contiguous-OR construction which does not realize
   the target as the canonical union of consecutive middle owners.

None of these three objects is proved. If one is constructed and is to
instantiate Theorems 4.1--4.3, the following exact-factor gates still
remain.

1. **One-factor completion.** Every simultaneous packet corner must lie in
   one unlabelled exact factor.

2. **Injectivity after forgetting labels.** Different packet signs must
   give distinct factor states, or their exact multiplicities must be
   retained.

3. **Additive common completion.** Choice-dependent completion rows would
   add extra increments and invalidate (0.1).

4. **Intrinsic rebasing and reverse scheduling.** Every child must expose
   the correct groupoid-conjugated inverse with the correct weight.

5. **Energy capture and endpoint control.** The gadget must prove
   (0.5)--(0.6), or the current-gain inequality (4.6).

6. **Exact intermediate states.** If internal rotating substeps are
   advertised as a multistep exact-factor chain, every intermediate state
   must itself be a literal exact factor.

With these gates and \(\rho_A/4>\sigma_A\), Theorem 4.2 gives an
\(O_A(HB)\) exact factor for that fixed \(A\). Proving this for every fixed
\(A\) would give constant one by the frozen diagonalization.

## 8. Independent audits of the decisive constants

The decisive steps were derived independently in three forms and then
cross-checked.

### 8.1 Haar constant

The fair-sign variance in (3.4) is

\[
 \frac14\sum_i\|z_i\|_H^2,
\]

while the coherent endpoint variance in (3.5) is

\[
 \frac14\left\|\sum_i z_i\right\|_H^2.
\]

Their difference is exactly \(G/4\). No factor \(1/2\) is missing.

### 8.2 Collision constant

Every captured pair-depth incidence in different packets contributes at
least \(1/c_q\) to
\(\sum_{P<Q}\langle z_P,z_Q\rangle_H\). Distinct depths are orthogonal
coordinates, so repeated pairs across depths add rather than overcount.
Since \(G\) has a leading factor two, the incidence contributes
\(2/c_q\), proving \(G\ge2C_w\). Combining with the Haar factor \(1/4\)
gives gain \(C_w/2\).

### 8.3 Floor constant

Expansion of the unhalved polynomial gives

\[
 Q_q=2(\operatorname{Coll}_q-\operatorname{Coll}^{\min}_q).
\]

Thus the full weighted excess-collision mass is \(\mathcal Q_H/2\), not
\(\mathcal Q_H\).

### 8.4 Adaptive contraction

From \(C_w\ge(\rho_A/2)(\mathcal Q_H-R_A)\),

\[
 G/4\ge C_w/2\ge(\rho_A/4)(\mathcal Q_H-R_A).
\]

Subtracting the endpoint surcharge \(\sigma_A(\mathcal Q_H-R_A)\)
gives the exact coefficient \(\rho_A/4-\sigma_A\).

### 8.5 Reverse-period order

For \(P_\to=H_0\cdots H_{L-1}\), self-adjointness of the individual
stages gives

\[
 P_\to^*=H_{L-1}\cdots H_0,
\]

not the original chronological product. For two stages, the discrepancy is
the commutator (5.5).

### 8.6 Degree cancellation in Kolmogorov's test

For \(P(F,G)=a(F,G)/d(F)\), the product of the forward degree denominators
around a cycle is

\[
 \prod_i d(F_i),
\]

which is also the reverse product. Hence (5.19) is the exact residual cycle
condition.

### 8.7 MSW asymptotic

Using (6.7), the leading term in (6.2) is

\[
 2(2m)\frac{B}{16}
 =\frac{mB}{4}
 =\left(\frac18+o(1)\right)W.
\]

The subtraction \(4W/(m+2)\) is \(o(W)\). Since
\(HB=(A/2+o_A(1))W/\sqrt m\), the ratio is
\((1/(4A)-o(1))\sqrt m\), as in (6.4).

## 9. Exact proved/conditional boundary

The following statements are proved.

1. Every exact-factor macro-kernel satisfies the coherent-versus-
   restitution identity (2.3), and every stationary law satisfies (2.4).

2. The class-average inequalities (2.5)--(2.6) imply the exact stationary
   bound (2.7).

3. A completed intrinsic exact packet cube satisfies the floor-exact Haar
   identity (3.3), the collision identity (3.9), and the rainbow gain
   (3.11). Its optimized current-endpoint drift is exactly
   (3.15)--(3.16).

4. The capture and endpoint inequalities (0.5)--(0.6) imply the
   Catalan-scale stationary theorem, with exact contraction coefficient
   \(\rho_A/4-\sigma_A\). The alternative current-gain condition (4.6)
   gives (4.7).

5. A forward rotating period is uniform-stationary but is reversible
   exactly under the reverse-word equality (5.4).

6. A reverse-closed state-normalized packet menu has degree-biased
   stationary law (5.14); general reversibility is characterized by
   reciprocal support and (5.19).

7. The positive-density intrinsic MSW packet cube of Theorem 6.1 has
   stationary energy \(\Omega(W)\), so reversibility and packet density
   alone cannot give the desired scale.

8. Within the canonical phase-fixed owner-spike/Pascal--Gray model,
   switched starts are separated by \(H+q\). Hence \(p\) same-phase
   requests require at least \(1+(p-1)(H+q)\) principal owners, and the
   requested entry-neutral \(p+O(1)\) two-port compiler is impossible.

The following statements are not proved.

1. A global cross-phase age-interleaving scheduler, an age-compatible
   packetization, or a noncanonical direct-OR replacement for the refuted
   same-phase compiler.

2. A one-factor exact completion of the simultaneous corners of any
   surviving gadget intended to instantiate the factor-chain theorems.

3. Intrinsic reverse closure under cumulative rotating and freshly
   recomputed ownership gauges.

4. The collision-capture inequality (0.5), or the current-gain inequality
   (4.6), for all excess above the Catalan reserve.

5. The endpoint-surcharge inequality (0.6).

Accordingly, this lane does not prove constant one. It closes both the
generic stationarity shortcut and the independent same-phase rotating
compiler. A surviving route must first construct a materially different
global cross-phase, age-compatible, or direct-OR gadget. A surviving
factor-chain gadget must then be exact-factor completable, reverse coherent
if reversibility is desired, and quantitatively energy-capturing, with
\(\rho_A/4>\sigma_A\). A direct-OR bypass must instead prove literal
coverage and the coefficient-one word-length ledger on its own. Common
ports and detailed balance by themselves are strictly insufficient.
