# Third-wave Y: adaptive exact transposition-component switching

## 1. Verdict

The adaptive route has an exact calculus and an exact stopping-time
classification, but it does not presently prove fixed-window balancing.
The decisive object is no longer the uniform stationary mean of a fair heat
class.  It is the minimum floor energy inside the communicating class of the
initial exact factor.

More precisely:

1. For every transposition cell, the change of the full weighted floor energy
   under an arbitrary component signing is exactly a weighted Gram cut.  The
   best state-dependent one-step drift is therefore an exact Max-Cut quantity.

2. Recomputing ownership components after every switch gives an exact pathwise
   telescope.  This permits a useful conditional epoch theorem in which
   intermediate switches may increase the energy.  Such a theorem is fully
   compatible with the Boolean-
   \(E_2\) no-go.

3. Every adaptive exact policy remains in one universal switch class.  A
   target can be hit from a prescribed start if and only if that target meets
   the start's class.  The corresponding Bellman hitting-time function is an
   exact Lyapunov function.  Conversely, an unrestricted auxiliary Lyapunov
   theorem is merely a reformulation of this class-intersection condition.

4. State-dependent stationarity has no intrinsic energy content.  A
   Metropolis modification of the symmetric exact proposal realizes any
   strictly positive stationary law on a fixed class.  Gibbs tilting
   concentrates arbitrarily close to the class minimum.

5. The corrected coherent-displacement baseline is
   \(4(n-1)\), but the Boolean-\(E_2\) theorem shows that a genuinely
   low-floor-energy terminal factor must retain a large Johnson-degree-
   \(\ge3\) surplus.  Thus a successful adaptive theorem must control
   component correlations while allowing this surplus; it cannot require
   absolute near-equality with the \(4(n-1)\) baseline.

6. There are rigorous restricted-support barriers.  A disconnected set of
   used coordinate transpositions preserves exact orbit-profile totals and
   their integral quadratic floors.  A transposition-rigid high-energy exact
   factor would be an unconditional pathwise obstruction for its starting
   class, but the existence of such a high-energy family is **unproved**.

No unconditional high-energy full switch class, and no nonlinear invariant
separating such a class, is produced here.  Conversely, no theorem showing
that every class, or even one specified class, has Catalan-scale minimum is
proved.  The exact unresolved gates are stated in Sections 6 and 12.

All states and all switches below are genuine integral exact middle factors.
No signed relaxation is used as a substitute for an exact factor, and no
literal contiguous-OR word is claimed.

---

## 2. Setup and normalization

Let

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\operatorname{Cat}_m=\frac{W}{n}.
\]

Let \(\mathfrak F_m\) be the finite set of exact middle wreath factors.  An
element \(F\in\mathfrak F_m\) consists of \(B\) unoriented cyclic orders and
covers every middle \(m\)-set exactly once.

At depth \(q\), put

\[
r_q=m-q,\qquad
N_q=\binom{n}{r_q},\qquad
\lambda_q=\frac{W}{N_q}=c_q+\theta_q,
\]

where

\[
c_q=\lfloor\lambda_q\rfloor,qquad 0\le\theta_q<1.
\]

For \(S\in\binom{[n]}{r_q}\), let \(\mu_q^F(S)\) be the number of wreaths of
\(F\) in which \(S\) is a cyclic interval.  Then

\[
\sum_S\mu_q^F(S)=W.
\]

Define

\[
f_q^F=\mu_q^F-\lambda_q\mathbf 1,
\qquad
\beta_q=N_q\theta_q(1-\theta_q),
\]

and the full floor-corrected energy

\[
Q_q(F)
=\sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
=\|f_q^F\|_2^2-\beta_q.
\tag{Y3.1}
\]

The summands in the first expression are nonnegative integers.  Hence
\(Q_q(F)\ge0\).

Fix \(A>0\) and, for all sufficiently large \(m\), put

\[
H=H_A=\lceil A\sqrt m\rceil.
\]

The weighted Hilbert structure and the two aggregate quantities are

\[
\langle x,y\rangle_H
=\sum_{q=1}^{H}\frac{\langle x_q,y_q\rangle_2}{c_q},
\qquad
\|x\|_H^2=\langle x,x\rangle_H,
\tag{Y3.2}
\]

\[
\mathcal Q_H(F)=\sum_{q=1}^{H}\frac{Q_q(F)}{c_q},
\qquad
\mathfrak B_H=\sum_{q=1}^{H}\frac{\beta_q}{c_q}.
\tag{Y3.3}
\]

Thus

\[
\mathcal Q_H(F)=\|f^F\|_H^2-\mathfrak B_H.
\tag{Y3.4}
\]

The desired fixed-window scale is

\[
\mathsf T_A:=H_A B=H_A\operatorname{Cat}_m
=\Theta_A\!\left(\frac{W}{\sqrt m}\right).
\tag{Y3.5}
\]

For later crude bounds, every load satisfies \(\mu_q^F(S)\le B\), because
\(F\) has only \(B\) wreaths.  Therefore

\[
\sum_S\mu_q^F(S)^2
\le B\sum_S\mu_q^F(S)=BW=\frac{W^2}{n},
\]

and consequently

\[
0\le \mathcal Q_H(F)\le \frac{HW^2}{n}.
\tag{Y3.6}
\]

Constants carrying a subscript \(A\) may depend on the fixed \(A\), but not
on \(m\) or on the starting exact factor.

---

## 3. Intrinsic transposition cells and the three control models

Assume \(m\ge2\), as is automatic in the asymptotic regime, and fix a
coordinate transposition \(\tau\).  Overlay the middle ownership of
\(F\) and \(\tau F\).  Let the old sides of the connected ownership
components be

\[
K_1,\ldots,K_k.
\]

The corresponding new sides are \(\tau K_1,\ldots,\tau K_k\).  Choosing,
independently for each component, either its old or new side produces
\(2^k\) exact factors.  The resulting set is the intrinsic \(\tau\)-cell

\[
\mathscr D_\tau(F).
\]

The cell is intrinsic: if \(G\in\mathscr D_\tau(F)\), then

\[
\mathscr D_\tau(G)=\mathscr D_\tau(F).
\tag{Y3.7}
\]

Indeed, changing a component side merely reads that same bipartite ownership
component with its two sides reversed; it neither splits nor joins the
component.  This is the exact fact that permits repeated fair resampling of a
cell and sequential switching of its components.

It is helpful to distinguish three scopes of adaptive control.

* **Signed-child control.**  At state \(F\), the controller chooses \(\tau\)
  and then chooses an arbitrary member of \(\mathscr D_\tau(F)\).  Equivalently,
  it chooses all component signs.

* **Fair-cell feedback.**  At state \(F\), the controller chooses \(\tau\),
  possibly from a state- or history-dependent law, and the next state is
  sampled uniformly from \(\mathscr D_\tau(F)\).  Write this projector kernel
  as \(K_\tau\).

* **Supported proposal control.**  Any Markov kernel supported on legal cell
  moves is allowed, including proposal followed by state-dependent acceptance
  or rejection.  The Metropolis theorem in Section 9 has this scope.

Every assertion below states which scope it uses.  A theorem for signed-child
control need not be a one-step theorem for fair-cell feedback, although the
two models have the same eventual target reachability by Theorem 7.2.

---

## 4. Exact component-signing and Max-Cut identities

For an ownership component \(K\), let \(a_{K,q}\) be the depth-\(q\)
histogram contributed by its old-side wreaths, and define

\[
d_{K,q}=a_{K,q}-\tau a_{K,q},
\qquad
d_K=(d_{K,q})_{q\le H}.
\tag{Y3.8}
\]

Then

\[
d:=\sum_Kd_K=f^F-\tau f^F.
\tag{Y3.9}
\]

For signs \(\varepsilon_K\in\{+1,-1\}\), let \(F_{\tau,\varepsilon}\)
be the exact factor choosing the old side when \(\varepsilon_K=+1\) and the
new side when \(\varepsilon_K=-1\).  Put

\[
A_\tau(F)=\left\|\sum_Kd_K\right\|_H^2,
\qquad
R_\tau(F;\varepsilon)
=\left\|\sum_K\varepsilon_Kd_K\right\|_H^2,
\tag{Y3.10}
\]

\[
V_\tau(F)=\sum_K\|d_K\|_H^2,
\qquad
\beta_\tau^{\rm sgn}(F)=\min_\varepsilon R_\tau(F;\varepsilon).
\tag{Y3.11}
\]

The superscript on \(\beta_\tau^{\rm sgn}\) distinguishes the signing
minimum from the integer-variance floor \(\beta_q\) in (Y3.1).

### Theorem 4.1: exact signed-cell energy identity

For every exact factor \(F\), transposition \(\tau\), and component signing
\(\varepsilon\),

\[
\boxed{
\mathcal Q_H(F_{\tau,\varepsilon})-\mathcal Q_H(F)
=\frac{R_\tau(F;\varepsilon)-A_\tau(F)}4.}
\tag{Y3.12}
\]

#### Proof

The centered profile of the signed child is

\[
f^{F_{\tau,\varepsilon}}
=\frac{f^F+\tau f^F}{2}
+\frac12\sum_K\varepsilon_Kd_K.
\tag{Y3.13}
\]

The first summand is \(\tau\)-invariant.  Every \(d_K\) is
\(\tau\)-anti-invariant, because

\[
\tau d_K=\tau a_K-a_K=-d_K.
\]

The invariant and anti-invariant subspaces are orthogonal for the weighted
inner product (Y3.2).  The all-old factor has anti-invariant part \(d/2\).
Subtracting the two squared norms in (Y3.4) therefore gives (Y3.12).  The
floor constant \(\mathfrak B_H\) cancels. \(\square\)

Let

\[
I=\{K:\varepsilon_K=-1\},\qquad
d_I=\sum_{K\in I}d_K,
\qquad
d_{I^c}=\sum_{K\notin I}d_K.
\]

Since \(\sum_K\varepsilon_Kd_K=d_{I^c}-d_I\), (Y3.12) becomes

\[
\boxed{
\mathcal Q_H(F_{\tau,I})-\mathcal Q_H(F)
=-\langle d_I,d_{I^c}\rangle_H.}
\tag{Y3.14}
\]

Thus the one-cell optimization is precisely a weighted Max-Cut problem on
the component Gram graph.

Define

\[
G_\tau(F)
=\max_{I\subseteq\{K_1,\ldots,K_k\}}
\langle d_I,d_{I^c}\rangle_H,
\qquad
G(F)=\max_\tau G_\tau(F).
\tag{Y3.15}
\]

Then

\[
\boxed{
G_\tau(F)=\frac{A_\tau(F)-\beta_\tau^{\rm sgn}(F)}4\ge0.}
\tag{Y3.16}
\]

The inequality follows also from the empty cut, which has value zero.

### Corollary 4.2: exact adaptive one-step drift

For arbitrary state-dependent transposition probabilities \(p_F(\tau)\)
and arbitrary conditional signing laws \(\nu_{F,\tau}\),

\[
\mathbb E[\mathcal Q_H(F_{t+1})-\mathcal Q_H(F_t)\mid F_t=F]
=-
\sum_\tau p_F(\tau)
\mathbb E_{I\sim\nu_{F,\tau}}
\langle d_I,d_{I^c}\rangle_H.
\tag{Y3.17}
\]

Consequently randomization does not improve the best signed-child one-step
drift:

\[
\boxed{
\inf_{\text{signed-child policies}}
\mathbb E[\Delta\mathcal Q_H\mid F]=-G(F).}
\tag{Y3.18}
\]

For independent fair component signs,

\[
\mathbb E_\varepsilon R_\tau(F;\varepsilon)=V_\tau(F),
\]

and hence

\[
\boxed{
K_\tau\mathcal Q_H(F)-\mathcal Q_H(F)
=\frac{V_\tau(F)-A_\tau(F)}4.}
\tag{Y3.19}
\]

In particular,

\[
\beta_\tau^{\rm sgn}\le\min\{A_\tau,V_\tau\},
\qquad
G_\tau(F)\ge\frac{(A_\tau-V_\tau)_+}{4}.
\tag{Y3.20}
\]

The converse implication is false at the level of abstract Gram vectors:
a favorable correlated signing may exist even when fair independent signs
have nonnegative drift.  This is the central reason to distinguish adaptive
Max-Cut from fixed fair heat.

---

## 5. Recomputed-component paths and the exact telescope

Consider any adaptive exact path

\[
F_0,F_1,\ldots,
\]

where at time \(t\), after observing \(F_t\), one chooses \(\tau_t\),
recomputes the ownership components of \(F_t\) versus \(\tau_tF_t\), and
switches a component subset \(I_t\).  Put

\[
g_t=\langle d_{t,I_t},d_{t,I_t^c}\rangle_H.
\tag{Y3.21}
\]

No compatibility between the component partitions at different times is
assumed.

### Theorem 5.1: exact adaptive path telescope

For every deterministic time \(s\),

\[
\boxed{
\mathcal Q_H(F_s)
=\mathcal Q_H(F_0)-\sum_{t=0}^{s-1}g_t.}
\tag{Y3.22}
\]

For every bounded stopping time \(T\),

\[
\boxed{
\mathbb E\mathcal Q_H(F_T)
=\mathcal Q_H(F_0)-
\mathbb E\sum_{t<T}g_t.}
\tag{Y3.23}
\]

The same identity holds for an unbounded \(T\) whenever \(T<\infty\) almost
surely and passage from \(T\wedge s\) to \(T\) is justified, for example by
\(\mathbb E\sum_{t<T}|g_t|<\infty\).  If \(T\) may be infinite, a separate
limiting-state convention and convergence argument are required.

#### Proof

Apply (Y3.14) at the current exact factor at each time and telescope.  This
proof is unaffected by changes in the ownership partition. \(\square\)

The terms \(g_t\) may be negative.  Therefore (Y3.22) is compatible with
uphill preparatory moves.  This is the main flexibility absent from a
pointwise \(\mathcal Q_H\)-Lyapunov inequality.

### Finite strict descent and cut-local terminal states

Let

\[
L_H=\operatorname{lcm}(c_1,\ldots,c_H).
\]

Because each \(Q_q(F)\) is an integer, every strict change in
\(\mathcal Q_H\) has magnitude at least \(L_H^{-1}\).  Repeatedly taking a
maximizing positive cut therefore terminates after at most

\[
L_H\mathcal Q_H(F_0)
\tag{Y3.24}
\]

strict decreases.  Its terminal condition is

\[
\boxed{
G(F)=0
\quad\Longleftrightarrow\quad
\beta_\tau^{\rm sgn}(F)=A_\tau(F)
\text{ for every }\tau.}
\tag{Y3.25}
\]

This is exact but quantitatively useless: \(L_H\) can be enormous, and the
terminal energy is not presently bounded.

Every minimum of \(\mathcal Q_H\) within a universal switch class is
cut-local.  Indeed, every signed child remains in that class, so at a class
minimum

\[
R_\tau(F;\varepsilon)\ge A_\tau(F)
\quad\text{for every }\tau,\varepsilon.
\]

The identity signing has equality.  Hence

\[
\boxed{
\beta_\tau^{\rm sgn}=A_\tau,
\qquad
V_\tau\ge A_\tau
\quad\text{at every class minimum}.}
\tag{Y3.26}
\]

Thus no one-step floor-energy Foster theorem can avoid proving that all of
the relevant class minima are already low.

---

## 6. Quantitative conditional Lyapunov and epoch theorems

This section separates exact implications from their unproved structural
inputs.

### Unproved gate \(\mathrm{APC}_A\): adaptive positive-cut inequality

There exist constants \(\eta_A>0\) and \(C_A>0\) such that, for all
sufficiently large \(m\) and every exact factor \(F\),

\[
\boxed{
G(F)
\ge \frac{\eta_A}{n}\mathcal Q_H(F)
-\frac{C_A}{n}\mathsf T_A.}
\tag{APC_A}
\]

This gate is **unproved**.

### Theorem 6.1: deterministic stopping under \(\mathrm{APC}_A\)

Assume \(\mathrm{APC}_A\), and let the signed-child controller take a
maximizing cut at each step.  Put

\[
L_A=\frac{2C_A}{\eta_A}\mathsf T_A.
\tag{Y3.27}
\]

Then the hitting time

\[
T=\inf\{t:\mathcal Q_H(F_t)\le L_A\}
\]

satisfies

\[
\boxed{
T\le
1+\left\lceil
\frac{2n}{\eta_A}
\log^+\frac{\mathcal Q_H(F_0)}{L_A}
\right\rceil.}
\tag{Y3.28}
\]

In particular, (Y3.6), \(B=W/n\), and \(W\le2^n\) give

\[
T=O_A(n^2)
\tag{Y3.29}
\]

uniformly over the starting exact factor.

#### Proof

Above \(L_A\),

\[
G(F)\ge\frac{\eta_A}{2n}\mathcal Q_H(F).
\]

Equations (Y3.14) and (Y3.18) therefore give

\[
\mathcal Q_H(F_{t+1})
\le\left(1-\frac{\eta_A}{2n}\right)\mathcal Q_H(F_t)
\]

until the target is reached.  Since
\(-\log(1-x)\ge x\), (Y3.28) follows.  Moreover,

\[
\frac{\mathcal Q_H(F_0)}{L_A}
\le \frac{\eta_A}{2C_A}W,
\]

so its logarithm is \(O_A(n)\). \(\square\)

### Theorem 6.2: randomized Foster stopping with a tail bound

Let an arbitrary legal adaptive policy satisfy the filtration-level bound

\[
\mathbb E[\mathcal Q_H(F_{t+1})\mid\mathcal F_t]
\le
\left(1-\frac{\eta}{n}\right)\mathcal Q_H(F_t)
+\frac{b}{n}
\tag{Y3.30}
\]

for fixed \(\eta,b>0\), at least on every event \(\{t<T\}\) below.  (A
Markov state-feedback inequality holding at every state is sufficient.)  Put
\(L=2b/\eta\),
\(T=\inf\{t:\mathcal Q_H(F_t)\le L\}\), and

\[
\rho=1-\frac{\eta}{2n}.
\]

For all sufficiently large \(n\),

\[
\boxed{
\Pr(T>t)
\le
\frac{\mathcal Q_H(F_0)}{L}\rho^t,}
\tag{Y3.31}
\]

and

\[
\boxed{
\mathbb ET
\le
1+\frac{2n}{\eta}
\left(1+\log^+\frac{\mathcal Q_H(F_0)}L\right).}
\tag{Y3.32}
\]

#### Proof

Let

\[
Y_t=\mathcal Q_H(F_t)\mathbf1_{\{T>t\}}.
\]

Stop, or equivalently kill, the process on its first entrance into the
target.

Outside the target, \(b\le\eta\mathcal Q_H(F_t)/2\), so

\[
\mathbb EY_{t+1}\le\rho\mathbb EY_t.
\]

Thus \(\mathbb EY_t\le\rho^t\mathcal Q_H(F_0)\).  Since
\(Y_t>L\) on \(\{T>t\}\), Markov's inequality proves (Y3.31).  Summing
\(\Pr(T>t)\), first with the trivial bound one and then with (Y3.31), proves
(Y3.32). \(\square\)

### Unproved gate \(\mathrm{AFRAG}_A\): adaptive recomputed fragment

There are constants \(0<\eta_A\le1\), \(C_A>0\), and \(L_A^{\rm mov}>0\)
such that, from every exact factor \(F_0\), there is an adaptive exact path

\[
F_0,F_1,\ldots,F_\ell,
\qquad \ell\le L_A^{\rm mov}n,
\]

with components recomputed after every step and

\[
\boxed{
\sum_{t<\ell}g_t
\ge \eta_A\mathcal Q_H(F_0)-C_A\mathsf T_A.}
\tag{AFRAG_A}
\]

This gate is **unproved**.  It is strictly more flexible than
\(\mathrm{APC}_A\), because individual \(g_t\) may be negative.

By (Y3.22), \(\mathrm{AFRAG}_A\) gives

\[
\mathcal Q_H(F_\ell)
\le(1-\eta_A)\mathcal Q_H(F_0)+C_A\mathsf T_A.
\tag{Y3.33}
\]

Above \(2C_A\mathsf T_A/\eta_A\), an epoch contracts energy by at least
\(1-\eta_A/2\).  Iterating at most

\[
1+\left\lceil
\frac{2}{\eta_A}
\log^+\frac{\mathcal Q_H(F_0)}{2C_A\mathsf T_A/\eta_A}
\right\rceil
=O_A(n)
\tag{Y3.34}
\]

epochs gives a target factor after \(O_A(n^2)\) exact switches.

The significance of \(\mathrm{AFRAG}_A\) is not its presently unproved
estimate; it is the exact form of a stopping theorem that can cross local
energy barriers and is not forced into a near-\(E_2\) spectral state.

---

## 7. Universal communicating classes and exact target reachability

Define the undirected legal graph \(\Gamma_m\) on \(\mathfrak F_m\) by

\[
F\sim G
\quad\Longleftrightarrow\quad
G\in\mathscr D_\tau(F)
\text{ for some transposition }\tau.
\tag{Y3.35}
\]

The relation is symmetric by intrinsicness (Y3.7).  Switching one component
at a time or switching an arbitrary subset gives the same connected
components, because all intermediate signings remain in the same intrinsic
cell.  Write \(\mathscr C(F)\) for the connected component of \(F\).

These components are exactly the communicating classes of the original fair
kernel

\[
K=\binom n2^{-1}\sum_\tau K_\tau.
\tag{Y3.36}
\]

### Theorem 7.1: policy-independent class barrier

For every nonanticipating state- or history-dependent adaptive policy,

\[
\boxed{F_t\in\mathscr C(F_0)\quad\text{for every }t}
\tag{Y3.37}
\]

pathwise under signed-child control and almost surely under fair-cell
feedback or supported proposal control.

An adaptive policy can suppress legal moves and split a universal class into
smaller recurrent sets, but it cannot merge two universal classes.

#### Proof

Every permitted transition is an edge of \(\Gamma_m\).  Induction on time
proves (Y3.37). \(\square\)

### Theorem 7.2: exact controlled hitting equivalence

Let \(\mathcal A\subseteq\mathfrak F_m\) be any target set.  For a prescribed
start \(F\), the following are equivalent:

1. \(\mathcal A\cap\mathscr C(F)\ne\varnothing\).

2. A deterministic signed-child controller reaches \(\mathcal A\) in
   finitely many moves.

3. A controlled fair-cell policy reaches \(\mathcal A\) almost surely with
   finite expected time.

Moreover, in case 1 there is a fair-cell policy satisfying

\[
\boxed{
\mathbb E_F T_{\mathcal A}
\le |\mathscr C(F)|\bigl(|\mathscr C(F)|-1\bigr).}
\tag{Y3.38}
\]

#### Proof

Necessity is Theorem 7.1.  For signed-child sufficiency, follow any simple
legal path

\[
x_0=F,x_1,\ldots,x_\ell\in\mathcal A,
\qquad \ell\le|\mathscr C(F)|-1.
\]

For fair-cell sufficiency, choose \(\tau_i\) with
\(x_{i+1}\in\mathscr D_{\tau_i}(x_i)\).  At stage \(i\), repeat
\(K_{\tau_i}\) until the sample equals \(x_{i+1}\).  Every failed sample
remains in the same intrinsic cell, so all trials are uniform on that same
cell.  The stage time is geometric with mean

\[
|\mathscr D_{\tau_i}(x_i)|\le|\mathscr C(F)|.
\]

Summing over at most \(|\mathscr C(F)|-1\) stages proves (Y3.38). \(\square\)

The bound is finite but asymptotically useless.  Even the original fixed
kernel \(K\) eventually hits every nonempty target in its finite irreducible
class; adaptation is needed for a directed or quantitative theorem, not for
bare recurrence.

### Theorem 7.3: Bellman hitting-time Lyapunov function

On a class meeting \(\mathcal A\), define

\[
h(F)=\inf_{\text{fair-cell feedback policies}}
\mathbb E_F T_{\mathcal A}.
\tag{Y3.39}
\]

Then \(h<\infty\), and it is the minimal nonnegative solution of

\[
h(F)=0\quad(F\in\mathcal A),
\tag{Y3.40}
\]

\[
\boxed{
h(F)=1+\min_\tau(K_\tau h)(F)
\quad(F\notin\mathcal A).}
\tag{Y3.41}
\]

A minimizing stationary feedback selector exists.  Under such a selector,

\[
h(F_{t\wedge T_{\mathcal A}})+t\wedge T_{\mathcal A}
\tag{Y3.42}
\]

is a martingale, and optional stopping recovers
\(h(F)=\mathbb E_F T_{\mathcal A}\).

Conversely, if \(\mathcal A\cap\mathscr C(F)=\varnothing\), no
bounded-below potential \(V\) can satisfy a uniform negative-drift bound

\[
\mathbb E[V(F_{t+1})-V(F_t)\mid\mathcal F_t]\le-\epsilon
\tag{Y3.43}
\]

before \(T_{\mathcal A}\), for any \(\epsilon>0\).  The target is never hit,
and iteration of (Y3.43) would force \(\mathbb EV(F_t)\) below the lower
bound of \(V\).

The Bellman theorem is exact and fully compatible with Boolean-\(E_2\), but
it is class-dependent and nonquantitative: defining \(h\) presupposes the
very target reachability that must be proved.

### Theorem 7.4: exact strong-control Foster dual

Let \(g:\mathfrak F_m\to\mathbb R\).  Under signed-child control, the
following are equivalent:

1. There are a legal deterministic state-feedback kernel \(P\) and a
   potential \(V\) such that

   \[
   (I-P)V(F)\ge g(F)
   \quad\text{for every }F.
   \tag{Y3.44}
   \]

2. Every universal class \(\mathscr C\) contains a state \(F_{\mathscr C}\)
   with

   \[
   g(F_{\mathscr C})\le0.
   \tag{Y3.45}
   \]

#### Proof

For necessity, every finite Markov kernel has a stationary law on a recurrent
subclass of each universal class it enters.  Averaging (Y3.44) under that law
gives \(0\ge\mathbb E g\), so some state in the universal class satisfies
(Y3.45).

For sufficiency, choose such a root in each class and direct a spanning tree
toward it.  Let \(P\) move every nonroot state to its parent and hold each
root fixed.  Define \(V\) recursively by

\[
V(F)-V(PF)=g(F)
\]

at nonroots and choose any root values.  At a root,
\((I-P)V=0\ge g\).  A classwise additive constant makes \(V\ge0\) if
desired. \(\square\)

Taking

\[
g(F)=\frac{\eta_A}{n}\mathcal Q_H(F)
-\frac{C_A}{n}\mathsf T_A
\tag{Y3.46}
\]

shows that an unrestricted adaptive Foster potential exists exactly when

\[
\boxed{
\min_{F\in\mathscr C}\mathcal Q_H(F)
\le\frac{C_A}{\eta_A}\mathsf T_A
\quad\text{for every relevant class }\mathscr C.}
\tag{Y3.47}
\]

Thus allowing an arbitrary auxiliary Lyapunov function does not soften the
class-minimum problem.

### Corollary 7.5: direct energy Foster inequalities contain the class gate

Suppose a fair-cell selector obeys

\[
K_{\tau(F)}\mathcal Q_H(F)
\le
\left(1-\frac\eta n\right)\mathcal Q_H(F)+\frac bn
\tag{Y3.48}
\]

for every state.  If

\[
e_{\mathscr C}=\min_{F\in\mathscr C}\mathcal Q_H(F),
\]

then

\[
\boxed{e_{\mathscr C}\le b/\eta\quad\text{for every class }\mathscr C.}
\tag{Y3.49}
\]

Indeed, at a class minimizer every member of every \(\tau\)-cell has energy
at least \(e_{\mathscr C}\), so
\(K_\tau\mathcal Q_H\ge e_{\mathscr C}\) for every \(\tau\).  Substitution in
(Y3.48) gives (Y3.49).

If \(L>b/\eta\), the same drift bound gives the explicit additive estimate

\[
\boxed{
\mathbb E_FT_{\{\mathcal Q_H\le L\}}
\le
\frac{n\mathcal Q_H(F)}{\eta L-b}.}
\tag{Y3.50}
\]

This follows from the stopped supermartingale with outside-target drift at
most \(-(\eta L-b)/n\).

---

## 8. Exact separation of quantifiers

For a threshold \(L\), put

\[
e_{\mathscr C}=\min_{F\in\mathscr C}\mathcal Q_H(F),
\qquad
\bar e_{\mathscr C}
=\mathbb E_{F\sim\pi_{\mathscr C}}\mathcal Q_H(F),
\tag{Y3.51}
\]

where \(\pi_{\mathscr C}\) is the uniform stationary law of the original fair
kernel on \(\mathscr C\).

The exact logical scopes are:

\[
\begin{array}{c|c}
\text{claim} & \text{necessary and sufficient condition}\\ \hline
\text{adaptive success from prescribed }F
& e_{\mathscr C(F)}\le L\\
\text{adaptive success from every start}
& \max_{\mathscr C} e_{\mathscr C}\le L\\
\text{success from some selectable start}
& \min_{\mathscr C} e_{\mathscr C}=\min_F\mathcal Q_H(F)\le L\\
\text{uniform stationary-class selection}
& \min_{\mathscr C}\bar e_{\mathscr C}\le L.
\end{array}
\tag{Y3.52}
\]

The stationary-class statement implies that its selected class contains a
low vertex, and hence adaptive hitting from every state of that class.  The
converse is not a consequence of finite-state geometry: abstractly, a finite
class can have a small minimum and a large uniform mean.  No such separated
true exact-factor class is constructed here; rigorously, only
\(e_{\mathscr C}\le\bar e_{\mathscr C}\) is automatic and no converse
estimate is proved.

The positive-cut local-minimum statement

\[
\boxed{
G(F)=0\Longrightarrow
\mathcal Q_H(F)\le C_A\mathsf T_A}
\tag{LM_A}
\]

is **unproved**.  If true, it would imply the every-start class-minimum bound,
because every class minimum is cut-local.  It remains distinct from the
stationary covariance-selection statement, which concerns
\(\bar e_{\mathscr C}\), not \(e_{\mathscr C}\).

For every fixed \(A\), a bound
\(\min_F\mathcal Q_{H_A}(F)=O_A(\mathsf T_A)=o(W)\) yields the required
small unlabelled overload in that window, since the floor energy dominates
twice the overload.  Repeating this for every fixed \(A\) has the frozen
diagonal implication to MWB.  None of the adaptive statements here yields
labelled common-owner synchronization.

---

## 9. Adaptive stationarity is non-rigid

### 9.1 Occupation ledger for fair-cell feedback

Let

\[
P_\alpha(F,G)=\sum_\tau\alpha_\tau(F)K_\tau(F,G)
\tag{Y3.53}
\]

be a stationary state-feedback fair-cell policy, and let \(\pi\) be an
invariant law.  Define the occupation measure

\[
\eta(F,\tau)=\pi(F)\alpha_\tau(F).
\tag{Y3.54}
\]

It satisfies

\[
\sum_\tau\eta(G,\tau)
=\sum_{F,\tau}\eta(F,\tau)K_\tau(F,G),
\qquad
\sum_{F,\tau}\eta(F,\tau)=1.
\tag{Y3.55}
\]

Stationarity and (Y3.19) give the exact energy ledger

\[
\boxed{
0=\frac14\sum_{F,\tau}\eta(F,\tau)
\bigl[V_\tau(F)-A_\tau(F)\bigr].}
\tag{Y3.56}
\]

The weights \(\eta(F,\tau)\) correlate the chosen transposition with the
current state.  Therefore the coherent term in (Y3.56) cannot be replaced by
the unweighted transposition sum in Section 10.  This is exactly where the
fixed-heat stationary two-slack identity ceases to apply.

For a universal class \(\mathscr C\), the minimum stationary average under
fair-cell feedback is the finite linear program

\[
\lambda_{\mathscr C}^{\rm fair}
=\min_\eta\sum_{F\in\mathscr C,\tau}
\eta(F,\tau)\mathcal Q_H(F),
\tag{Y3.57}
\]

subject to (Y3.55) and \(\eta\ge0\).  Finite linear-programming duality gives

\[
\boxed{
\lambda_{\mathscr C}^{\rm fair}
=\sup_h\min_{F\in\mathscr C,\tau}
\left[
\mathcal Q_H(F)+(I-K_\tau)h(F)
\right].}
\tag{Y3.58}
\]

The sharp elementary sandwich is

\[
\boxed{
e_{\mathscr C}
\le\lambda_{\mathscr C}^{\rm fair}
\le\bar e_{\mathscr C}.}
\tag{Y3.59}
\]

The lower bound is pointwise.  For the upper bound, use the original uniform
transposition policy and the uniform class law.  If stopping, an explicit
no-op, or deterministic signing control is allowed, a point mass at a class
minimizer is stationary and the controlled stationary minimum equals
\(e_{\mathscr C}\).

If every \(\alpha_\tau\) is constant on each intrinsic \(\tau\)-cell, then
the corresponding summand is symmetric.  With full action support the
universal classes and their uniform laws return.  If actions are suppressed,
a symmetric policy may split a universal class, and its smaller recurrent
sets need not be invariant under inactive \(K_\tau\)'s.

### 9.2 Metropolis realization of arbitrary class laws

The previous occupation problem still restricts the controller to fair
resampling after the action is selected.  For the broader supported-proposal
model, stationarity is completely non-rigid.

Let \(K\) be the symmetric kernel (Y3.36) restricted to a universal class
\(\mathscr C\), and let \(\nu\) be any strictly positive probability law on
\(\mathscr C\).  For \(F\ne G\), define

\[
P_\nu(F,G)
=K(F,G)\min\left\{1,\frac{\nu(G)}{\nu(F)}\right\},
\tag{Y3.60}
\]

and place rejected mass on the diagonal.

### Theorem 9.1: arbitrary-law exact Metropolis chain

The kernel \(P_\nu\) is supported on legal exact component switches, is
irreducible and aperiodic on \(\mathscr C\), and is reversible with stationary
law \(\nu\).

#### Proof

Symmetry of \(K\) gives, for \(F\ne G\),

\[
\nu(F)P_\nu(F,G)
=K(F,G)\min\{\nu(F),\nu(G)\}
=\nu(G)P_\nu(G,F).
\]

Strict positivity of \(\nu\) preserves every positive legal edge of \(K\).
The all-old signing gives \(K(F,F)>0\), so the Metropolis kernel has holding
even when every nontrivial proposal is accepted; rejection can add further
holding. \(\square\)

For the Gibbs choice

\[
\nu_{\beta,\mathscr C}(F)
=\frac{e^{-\beta\mathcal Q_H(F)}}
{\sum_{G\in\mathscr C}e^{-\beta\mathcal Q_H(G)}},
\qquad \beta>0,
\tag{Y3.61}
\]

let \(e_{\mathscr C}=\min_{\mathscr C}\mathcal Q_H\).  The Gibbs entropy identity
and \(H(\nu_{\beta,\mathscr C})\le\log|\mathscr C|\) give

\[
\boxed{
0\le
\mathbb E_{\nu_{\beta,\mathscr C}}\mathcal Q_H-e_{\mathscr C}
\le\frac{\log|\mathscr C|}{\beta}.}
\tag{Y3.62}
\]

Thus adaptive stationary measures can concentrate arbitrarily close to the
class minimum, but cannot improve it or cross to another class.  No mixing-
or hitting-time bound useful at the Catalan scale follows from this finite
argument.

There is also a simple caution against any assertion about *every* adaptive
policy: choosing all ownership components produces \(\tau F\).  Uniformly
choosing \(\tau\) gives the coordinate-orbit walk on \(S_nF\), along which
every coordinate-invariant energy, including \(\mathcal Q_H\), is exactly
constant.  The problem is to exhibit one favorable policy, not to prove that
all policies descend.

---

## 10. Corrected \(4(n-1)\) ledger and adaptive drift

Every exact centered profile has zero total and zero point margins.  Hence
its Johnson decomposition begins at degree two:

\[
f_q=\sum_{j\ge2}f_{q,j}.
\tag{Y3.63}
\]

On degree \(j\), the sum over unordered coordinate transpositions satisfies

\[
\sum_\tau\|f_{q,j}-\tau f_{q,j}\|_2^2
=2j(n-j+1)\|f_{q,j}\|_2^2.
\tag{Y3.64}
\]

Define

\[
D_H(F)=\sum_\tau A_\tau(F),
\qquad
R_H(F)=\sum_\tau V_\tau(F),
\tag{Y3.65}
\]

and

\[
\Xi_H(F)
=2\sum_{q=1}^{H}\frac1{c_q}
\sum_{j=3}^{m-q}
(j-2)(n-j-1)\|f_{q,j}\|_2^2.
\tag{Y3.66}
\]

Since

\[
j(n-j+1)-2(n-1)=(j-2)(n-j-1),
\]

one obtains the corrected exact pointwise identity

\[
\boxed{
D_H(F)
=4(n-1)\bigl(\mathfrak B_H+\mathcal Q_H(F)\bigr)
+\Xi_H(F),
\qquad \Xi_H(F)\ge0.}
\tag{Y3.67}
\]

The coefficient is \(4(n-1)\), not \(2n\).

Let \(M=\binom n2=n(n-1)/2\).  Uniformly choosing \(\tau\) and then using
fair component signs gives

\[
\boxed{
K\mathcal Q_H(F)-\mathcal Q_H(F)
=\frac{R_H(F)-D_H(F)}{4M}.}
\tag{Y3.68}
\]

Uniformly choosing \(\tau\) and then choosing an optimal component signing
gives instead

\[
\boxed{
\mathbb E[\Delta\mathcal Q_H\mid F]
=-\frac1{4M}\sum_\tau
\bigl(A_\tau(F)-\beta_\tau^{\rm sgn}(F)\bigr).}
\tag{Y3.69}
\]

Substitution of (Y3.67) rewrites (Y3.69) as

\[
\boxed{
\mathbb E[\Delta\mathcal Q_H\mid F]
=-\frac{2}{n}\bigl(\mathfrak B_H+\mathcal Q_H(F)\bigr)
-\frac{\Xi_H(F)}{2n(n-1)}
+\frac{\sum_\tau\beta_\tau^{\rm sgn}(F)}{2n(n-1)}.}
\tag{Y3.70}
\]

This formula exposes the obstruction exactly.  The spectral theorem controls
the coherent displacement \(D_H\), but it does not control the signing
residual \(\sum_\tau\beta_\tau^{\rm sgn}\).  At a class minimum, the two are
equal transposition by transposition by (Y3.26), so the apparent spectral
gain cancels completely.

A one-component overlay illustrates the issue sharply:

\[
V_\tau=A_\tau=\beta_\tau^{\rm sgn},
\tag{Y3.71}
\]

regardless of how large the coherent displacement is.

---

## 11. Compatibility with the Boolean-\(E_2\) no-go

Let

\[
\theta_*=\frac{3-\sqrt6}{6}.
\tag{Y3.72}
\]

The audited Boolean-\(E_2\) stability theorem states that, for every fixed
central-window width \(C_0\), on ranks
\(|r-m|\le C_0\sqrt m\), and for Boolean densities in any fixed compact
interval \(I\subset(0,\theta_*)\), there is
\(\epsilon_{I,C_0}>0\) such that

\[
\left\|P_{E_1\oplus E_{\ge3}}
(\mathbf1_{\mathcal B}-\theta\mathbf1)\right\|_2^2
\ge\epsilon_{I,C_0}N.
\tag{Y3.73}
\]

After fixing \(C_0\), abbreviate
\(\epsilon_I=\min\{1,\epsilon_{I,C_0}\}\).  Shrinking the constant preserves
(Y3.73) and is the normalization used in the dichotomy below.  In the
depth-\(H_A\) application one may take \(C_0=A+1\).

The audited rounding argument transfers this to every integral exact-factor
load.  Put

\[
\mathcal H_q=\sum_{j\ge3}\|f_{q,j}\|_2^2.
\tag{Y3.74}
\]

On the selected depths it gives the rankwise dichotomy

\[
\boxed{
\mathcal H_q\ge\frac{\epsilon_I}{4}N_q
\quad\text{or}\quad
Q_q(F)\ge\frac{\epsilon_I^2}{256}N_q.}
\tag{Y3.75}
\]

For every fixed \(A>0\), the existing Gaussian-window selection supplies a
set \(J_A(m)\subseteq\{1,\ldots,H_A\}\) and constants
\(\rho_A,a_A,b_A,C_A'>0\) such that, for all sufficiently large \(m\),

\[
|J_A(m)|\ge\rho_A\sqrt m,
\qquad
a_AW\le N_q\le b_AW,
\qquad
1\le c_q\le C_A'
\tag{Y3.76}
\]

for every \(q\in J_A(m)\), and all corresponding \(\theta_q\)'s lie in one
compact \(I_A\subset(0,\theta_*)\).

### Theorem 11.1: low floor energy forces large high-degree surplus

Fix \(A>0\) and \(C>0\).  If

\[
\mathcal Q_{H_A}(F)\le C\mathsf T_A,
\tag{Y3.77}
\]

then, for all sufficiently large \(m\) depending on \(A,C\),

\[
\boxed{
\sum_{q\in J_A(m)}\mathcal H_q=\Omega_A(W\sqrt m),}
\tag{Y3.78}
\]

and

\[
\boxed{
\Xi_{H_A}(F)=\Omega_A(nW\sqrt m).}
\tag{Y3.79}
\]

#### Proof

For \(q\in J_A(m)\), nonnegativity and (Y3.77) give

\[
Q_q(F)\le c_q\mathcal Q_H(F)
=O_{A,C}(W/\sqrt m)=o_A(N_q).
\]

Thus the second alternative in (Y3.75) fails for every selected depth once
\(m\) is large, and

\[
\mathcal H_q\ge\epsilon_{I_A}N_q/4=\Omega_A(W).
\]

Summing over (Y3.76) proves (Y3.78).  For \(j\ge3\) and
\(j\le m-q\),

\[
(j-2)(n-j-1)\ge n-4.
\]

Equations (Y3.66), (Y3.76), and (Y3.78) prove (Y3.79). \(\square\)

This theorem is the exact compatibility statement for the adaptive lane.  A
successful terminal factor with
\(\mathcal Q_H=O_A(\mathsf T_A)\) is not close to Johnson degree two.  It is
forced to have a large degree-\(\ge3\) surplus.

Consequently, any Lyapunov architecture requiring both

\[
\mathcal Q_H=O_A(\mathsf T_A)
\quad\text{and}\quad
\Xi_H=o_A(nW\sqrt m)
\tag{Y3.80}
\]

is impossible.  In particular, at any cut-local state, (Y3.26) gives
\(R_H\ge D_H\), and the Boolean dichotomy plus (Y3.67) yields

\[
R_H-4(n-1)\mathfrak B_H
=\Omega_A(nW\sqrt m).
\tag{Y3.81}
\]

This includes the previously audited global-minimizer no-go.  At arbitrary
nonlocal states the same stability argument controls
\(D_H-4(n-1)\mathfrak B_H\), but it does not control \(R_H\), because
\(R_H\ge D_H\) is then unavailable.  Thus, specifically at cut-local states
(including class and global minima), it kills the absolute near-baseline
criterion

\[
R_H\le4(n-1)\mathfrak B_H+o(nW),
\tag{Y3.82}
\]

not adaptive balancing itself.

The Max-Cut gain depends on

\[
A_\tau-\beta_\tau^{\rm sgn},
\]

not on the absolute size of \(A_\tau\), \(V_\tau\), or \(\Xi_H\).  The
Boolean theorem supplies no sign for this difference.  Large
degree-\(\ge3\) mass is therefore allowed by \(\mathrm{APC}_A\),
\(\mathrm{AFRAG}_A\), and the Bellman theorem.

### An \(E_2\)-safe relative fair-drift gate

The following pointwise statement would also suffice, but is **unproved**:

\[
\boxed{
R_H(F)-D_H(F)
\le-\delta_A n\mathcal Q_H(F)
+C_A n\mathsf T_A.}
\tag{REL_A}
\]

Using (Y3.67), this is equivalent to

\[
R_H(F)
\le
4(n-1)\mathfrak B_H+\Xi_H(F)
+\bigl(4(n-1)-\delta_A n\bigr)\mathcal Q_H(F)
+C_A n\mathsf T_A.
\tag{Y3.83}
\]

Unlike (Y3.82), this retains the entire high-degree surplus \(\Xi_H\).
Together with (Y3.68), \(\mathrm{REL}_A\) gives a Foster contraction on the
\(O(n)\)-step scale.  Averaging it in any uniform fair communicating class,
where \(\mathbb E(R_H-D_H)=0\), would even imply

\[
\mathbb E_{\mathscr C}\mathcal Q_H
\le(C_A/\delta_A)\mathsf T_A
\tag{Y3.84}
\]

for every class.  This strength explains why \(\mathrm{REL}_A\) remains a
major unproved exact-ownership theorem.

Another scale-correct adaptive gate is

\[
\boxed{
\sum_\tau
\bigl(A_\tau-\beta_\tau^{\rm sgn}\bigr)
\ge\delta_A n
\bigl(\mathcal Q_H-C_A\mathsf T_A\bigr)_+.}
\tag{SAPC_A}
\]

By (Y3.69), it would give multiplicative contraction under uniform
transpositions and optimal signings.  It too leaves \(\Xi_H\) unrestricted
and is **unproved**.

---

## 12. Exact class barriers

### 12.1 Restricted coordinate support

Let an adaptive trajectory use transpositions from a set \(T\), and let

\[
G=\langle T\rangle\le S_n.
\]

For a \(G\)-orbit \(\mathcal O\subseteq\binom{[n]}{r_q}\), define

\[
T_{q,\mathcal O}(F)=\sum_{S\in\mathcal O}\mu_q^F(S).
\tag{Y3.85}
\]

### Theorem 12.1: orbit-total invariance

Every total in (Y3.85) is pathwise invariant along the trajectory:

\[
\boxed{
T_{q,\mathcal O}(F_t)=T_{q,\mathcal O}(F_0).}
\tag{Y3.86}
\]

#### Proof

A component switch for \(\tau\in G\) changes the profile by
\((\tau-I)a\).  Since \(\tau\) permutes each \(G\)-orbit,

\[
\sum_{S\in\mathcal O}[(\tau-I)a](S)=0.
\]

Sum over the switches. \(\square\)

Write

\[
M_{\mathcal O}=|\mathcal O|,
\qquad
T_{q,\mathcal O}=a_{\mathcal O}M_{\mathcal O}+\rho_{\mathcal O},
\qquad
0\le\rho_{\mathcal O}<M_{\mathcal O}.
\tag{Y3.87}
\]

Convexity of the integer function
\((x-c_q)(x-c_q-1)\) shows that its minimum at fixed orbit total is attained
by \(M_{\mathcal O}-\rho_{\mathcal O}\) entries equal to \(a_{\mathcal O}\) and
\(\rho_{\mathcal O}\) entries equal to \(a_{\mathcal O}+1\).  Hence every
reachable factor obeys the exact floor

\[
\boxed{
Q_q(F_t)\ge
\sum_{\mathcal O}
\left[
(M_{\mathcal O}-\rho_{\mathcal O})
(a_{\mathcal O}-c_q)(a_{\mathcal O}-c_q-1)
+\rho_{\mathcal O}
(a_{\mathcal O}+1-c_q)(a_{\mathcal O}-c_q)
\right].}
\tag{Y3.88}
\]

After weighting and summing over \(q\le H\), a right side larger than a
proposed target is a rigorous stopping obstruction for every policy confined
to \(G\).

If the graph on coordinates whose edges are the transpositions in \(T\) has
components \(V_1,\ldots,V_s\), then the \(G\)-orbits of rank-\(r\) sets are
their profiles

\[
(|S\cap V_1|,\ldots,|S\cap V_s|).
\]

If this coordinate graph is connected, then \(G=S_n\), there is one orbit
at every rank, and the floor (Y3.88) is zero because the globally prescribed
total is already balanced at the ordinary integer floor.  Thus this
invariant obstructs disconnected-support policies, not unrestricted adaptive
switching.

Along a spanning tree of coordinate transpositions, the relaxed profile
floors telescope from the initial defect to zero.  Consequently some bridge
releases at least a \(1/(n-1)\) share of the relaxed weighted defect.  This
does **not** prove that the corresponding exact ownership components realize
that release; component noise can restore it completely.

### 12.2 Fixed aggregation versus sequential recomputation

The audited multitransposition theorem identifies the join of the fixed
owner-component partitions generated by a subgroup \(G\) with the
row/orbit-incidence quotient of the \(G\)-Schreier action on middle sets.
Connected coordinate support makes this common partition one block.  Hence a
fixed connected-support transposition word or commutator, when aggregated
before the signs are chosen, offers only whole endpoint relabellings and has
zero drift for every coordinate-invariant energy.

This is not a no-go for \(\mathrm{AFRAG}_A\): that gate explicitly recomputes
components after each signed switch.  It does show that one may not replace
the adaptive path by one fixed common-owner cube.

### 12.3 Transposition-rigid orbit barrier

Call \(F\) **transposition-rigid** if its ownership overlay with \(\tau F\)
is connected for every coordinate transposition \(\tau\).

### Theorem 12.2: pathwise rigid-orbit obstruction

If \(F\) is transposition-rigid, then

\[
\boxed{\mathscr C(F)=S_nF.}
\tag{Y3.89}
\]

Every signed-child, fair-cell, or supported-proposal adaptive trajectory
starting at \(F\) remains a coordinate relabelling of \(F\).  Therefore, for
every almost surely finite stopping time \(T\),

\[
\boxed{
\mathcal Q_H(F_T)=\mathcal Q_H(F_0)
\quad\text{pathwise}.}
\tag{Y3.90}
\]

#### Proof

Rigidity is preserved by relabelling, because the overlay of \(\sigma F\)
with \(\tau\sigma F\) is the relabelled overlay of \(F\) with
\(\sigma^{-1}\tau\sigma F\).  A connected overlay has one component, so its
intrinsic cell consists only of

\[
\{\sigma F,\tau\sigma F\}.
\]

Thus the coordinate orbit is closed under every legal switch.  Conversely,
the all-new choice realizes every transposition, and transpositions connect
the coordinate orbit.  This proves (Y3.89).  Coordinate invariance of
\(\mathcal Q_H\) proves (Y3.90). \(\square\)

A family of transposition-rigid exact factors satisfying

\[
\mathcal Q_{H_A}(F_m)\gg\mathsf T_A
\tag{Y3.91}
\]

would be an absolute obstruction to every-start adaptive stopping.  The
existence of such a high-energy family is **unproved**.  Even if it existed,
it would not refute the weaker assertion that another class contains a low
factor.

The actual obstruction hierarchy is therefore:

1. A high state obstructs claims about *all* policies, because the
   coordinate-orbit policy keeps its energy constant.

2. A high cut-local state obstructs monotone one-step
   \(\mathcal Q_H\)-descent, but an uphill path may escape it.

3. A class with \(e_{\mathscr C}>L\) obstructs every adaptive stopped policy
   from that class.

4. A high transposition-rigid factor is a sufficient exact certificate for
   item 3.

Only items 1 and 2 are unconditional for arbitrary high states.  No
unconditional exact example of item 3 at the Catalan target scale is known.

---

## 13. Independent audit of the decisive steps

The following checks were carried out independently of the main derivation.

1. **Full-energy factor.**  The report uses the full floor energy
   \(Q_q=\sum(\mu-c)(\mu-c-1)\).  Therefore the signing identity has factor
   \(1/4\) in (Y3.12), and the cut identity has no extra factor in (Y3.14).
   Reports using \(\Psi=\mathcal Q/2\) instead have the corresponding
   \(1/2\) factors.

2. **Antipodal sign check.**  With \(I\) switched,
   \(d_\varepsilon=d_{I^c}-d_I\), so

   \[
   \|d_\varepsilon\|^2-\|d_I+d_{I^c}\|^2
   =-4\langle d_I,d_{I^c}\rangle.
   \]

   This verifies both the sign and constant in (Y3.14).

3. **Transposition normalization.**  Unordered transpositions are counted
   once.  Hence \(M=\binom n2\), the degree-two spectral contribution is
   \(4(n-1)\|f_{q,2}\|^2\), and the fair drift denominator is
   \(4M=2n(n-1)\).  Equations (Y3.67)--(Y3.70) use this normalization.

4. **Class hitting step.**  Repeating \(K_\tau\) after a failed sample is
   valid only because the entire \(\tau\)-cell is intrinsic.  The next trial
   is uniform on exactly the same cell, so its success probability is
   \(|\mathscr D_\tau|^{-1}\).  This proves the geometric mean in (Y3.38)
   without a mixing assumption.

5. **Lyapunov scope.**  The forest proof in Theorem 7.4 uses signed-child
   control.  The fair-cell analogue used for actual stochastic hitting is
   the Bellman equation (Y3.41).  These two scopes are not conflated.

6. **Metropolis scope.**  Theorem 9.1 changes the transition kernel by
   proposal acceptance.  It does not assert that the original fair heat has
   Gibbs stationarity.  Its purpose is to show that stationarity of an
   arbitrary state-dependent legal chain forces no energy bound.

7. **Boolean implication.**  The proved stability theorem is used only on
   a positive-density set of central depths whose fractional load densities
   remain in a compact subset of \((0,\theta_*)\).  Low floor energy rules
   out the large-\(Q_q\) side of the audited dichotomy, forcing large
   \(E_{\ge3}\) mass.  It does not rule out low floor energy itself.

8. **Barrier scope.**  Orbit-profile floors disappear when the used
   transposition support becomes connected.  The rigid-orbit obstruction is
   conditional on a high-energy rigid exact factor, whose existence is not
   claimed.

9. **Integrality.**  Every child in the calculus is obtained by switching
   complete sides of actual ownership components.  The relaxed profile
   floors and spectral decompositions are used only as bounds on exact
   factors, never as replacement states.

---

## 14. Final theorem-level status

The third-wave adaptive analysis proves the following exact statements:

* the signed-cell energy and Max-Cut identities (Y3.12)--(Y3.20);
* the recomputed-component path and stopped telescopes (Y3.22)--(Y3.23);
* quantitative stopping consequences of explicit drift or epoch hypotheses;
* the universal communicating-class barrier and exact hitting equivalence;
* the Bellman Lyapunov theorem and the strong-control Foster dual;
* the controlled stationary occupation dual and its class-minimum/class-mean
  sandwich;
* arbitrary positive class stationarity by exact Metropolis acceptance;
* the corrected \(4(n-1)\) adaptive drift ledger;
* the fact that Catalan-scale floor energy forces
  \(\Xi_H=\Omega_A(nW\sqrt m)\), so the adaptive route must remain far from
  the forbidden near-\(E_2\) baseline;
* exact restricted-support profile floors; and
* the conditional pathwise transposition-rigid obstruction.

The remaining mathematical alternatives are now sharp.

*Within the analyzed positive schemes*, any one of
\(LM_A\), \(\mathrm{APC}_A\), \(\mathrm{AFRAG}_A\),
\(\mathrm{REL}_A\), or \(\mathrm{SAPC}_A\), with the exact quantifiers stated
above, would suffice.  This list is not logically exhaustive; a direct
class-minimum construction or a different Lyapunov theorem could also work.
Among the displayed gates, the epoch form is the most permissive because it
allows temporary energy increases and recomputes ownership components.

*A negative route* must exhibit an actual exact switch class whose minimum
is \(\gg_A H_A\operatorname{Cat}_m\), or a genuine full-class invariant
forcing such a minimum.  Disconnected-support profile totals are insufficient
once bridges are allowed, and high uniform stationary mean alone is not a
stopping obstruction.  A high transposition-rigid family would suffice, but
none is known.

Therefore adaptive state dependence removes the fixed stationary-mean
barrier but does not solve the balancing problem.  It reduces the lane
exactly to class minima and accumulated positive component correlation.  The
Boolean-\(E_2\) theorem dictates the form of any viable proof: it must lower
the integer floor energy while allowing, and in fact eventually retaining,
a large high-degree spectral surplus.
