# Lane R: constant-one packet schedules and quota-directed nonlocal fusion

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
random experiment, or long-running computation is used.

## 0. Verdict

Conditional on the certified positive-density Lane W negative-mode
hypothesis stated below, the bounded-packet stability theorem cannot be
converted into an `o(W)` additive packet-size schedule on the Gaussian
band.  This is an **actual collision lower bound** under that hypothesis,
not merely a failure of the absolute-value proof.

Let

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m.
\]

If an exact reference factor has a two-block negative mode of the audited
strength at depths in a positive-density subset of

\[
a\sqrt m\le q\le A\sqrt m,
\]

then any exact endpoint factor satisfies the movement--collision
inequality

\[
\boxed{
E_q+2Q_q\ge
\left\lceil\frac{D_q}{M_q}\right\rceil,}
\tag{0.1}
\]

where `E_q` is its depth-`q` histogram distance from the reference,
`D_q` is the negative spectral score, and `M_q` is the test's largest
target weight.  In the mesoscopic two-block regime this is

\[
E_q+2Q_q
\ge
\left\lceil\frac{4\gamma q(q+1)t}{s_q}\right\rceil
\ge
\left\lceil\frac{4\gamma}{C}(q+1)t\right\rceil.
\tag{0.2}
\]

Consequently, `O(t)` packets of mass `o(q)` leave weighted collision
`Omega(W)`.  Packet splitting, geometric sizing, telescoping, and dependent
signs do not change this conclusion.  Linear-in-`q` average packet mass is
necessary in weighted aggregate on a dense Gaussian mode set.  Any
successful exact endpoint must replace `(gamma/2-o(1))t` whole wreath rows;
every exact-factor trajectory to it has `Omega(W)` cumulative row-event
volume and `Omega(W)` weighted shadow-movement mass.

There is, however, an exact nonlocal escape at the histogram level.
For every point-regular integral histogram one can choose a point-regular
floor/ceiling quota and move to it through conformal integral packets,
preserving all point margins and never increasing collision.  The final
collision is exactly zero.  A fan construction implements a nontrivial
alternating-cycle class with four-cell packets and one moving quota buffer.

Moreover, the audited integral shallow-filtration theorem lifts these
rankwise quota corrections to a simultaneous integral **signed** cyclic-row
solution with exact middle ownership and zero collision at every controlled
depth.

The remaining failure is decisive and cannot be repaired universally from
point margins and second moments.  At the genuine Gaussian depth
`q=floor(sqrt(m)/2)`, an explicit cyclic-invariant, point-regular,
zero-collision quota passes every PSD moment test but violates a literal
containment cut and lies outside even the fractional exact-factor cone.
Thus the lifted row vector need not be nonnegative or squarefree and need
not lie in one exact-factor fibre.  The natural synchronized four-`C8`
PBBS connector also fails by a local degree-zero/four obstruction.

No literal exact factor, and hence no constant-one contiguous-OR theorem,
is obtained.  The missing theorem must jointly choose **liftable** quotas
and realize their downhill corrections by endpoint-valid nonlocal circuits;
neither packet sizing nor a universal signed-to-positive lift can do this.

## 1. Exact floors and collision

For `1<=q<=m-2`, put

\[
r_q=m-q,\qquad
\Omega_q=\binom{[n]}{r_q},\qquad
N_q=|\Omega_q|,
\]

\[
d_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad
\rho_q=W-d_qN_q.
\tag{1.1}
\]

For an integral histogram `mu_q` of total `W`, define

\[
Q_q(\mu_q)
=\frac12\sum_{S\in\Omega_q}
(\mu_q(S)-d_q)(\mu_q(S)-d_q-1).
\tag{1.2}
\]

Let

\[
\mathcal B_q
=\left\{
\beta\in\{d_q,d_q+1\}^{\Omega_q}:
\sum_S\beta(S)=W
\right\}
\tag{1.3}
\]

be the exact floor/ceiling quota set.

## 2. Exact distance from the quota slab

### Lemma 2.1 — quota distance formula

Let `mu` be any nonnegative integral vector of total

\[
W=dN+\rho,
\qquad 0\le\rho<N.
\]

Put `z(S)=mu(S)-d` and define

\[
h(\mu)=\sum_S(-z(S))_+,
\qquad
e(\mu)=\sum_S(z(S)-1)_+.
\tag{2.1}
\]

Then

\[
\boxed{
\min_{\beta\in\mathcal B}
\|\mu-\beta\|_1
=2\max\{h(\mu),e(\mu)\}.}
\tag{2.2}
\]

Moreover,

\[
\boxed{
\min_{\beta\in\mathcal B}
\|\mu-\beta\|_1
\le2Q_d(\mu).}
\tag{2.3}
\]

#### Proof

Clip every `z(S)` to `{0,1}`.  The clipping cost is `h+e`, and the sum of
the clipped vector is

\[
\rho-e+h.
\]

If `e>=h`, promote `e-h` clipped zeroes to ones; if `h>e`, demote
`h-e` clipped ones to zeroes.  The final `0/1` vector has sum `rho`, and
the total cost is respectively `2e` or `2h`.

Conversely, every quota vector must absorb all mass below zero and above
one, and its total number of ones forces the same additional imbalance
correction.  Thus (2.2) is exact.

For an integer `z`,

\[
\frac12z(z-1)
\ge
\begin{cases}
-z,&z\le-1,\\
z-1,&z\ge2,\\
0,&z\in\{0,1\}.
\end{cases}
\]

Hence `Q_d(mu)>=h+e>=max{h,e}`, proving (2.3).  ∎

## 3. Spectral movement versus endpoint collision

Let `F_0,F_1` be exact factors.  At depth `q`, the audited cyclic boundary
identity is

\[
K_q(F)=a_qJ+b_qI+H_q(F),
\tag{3.1}
\]

where

\[
K_q(F)
=\sum_{S\in\Omega_q}(\mu_q^F(S)-d_q)
 \mathbf1_S\mathbf1_S^{\mathsf T}.
\]

Fix

\[
Z\succeq0,\qquad Z\mathbf1=0,
\]

and put

\[
D_q
:=-\operatorname{Tr}Z(b_qI+H_q(F_0))>0,
\tag{3.2}
\]

\[
M_q
:=\max_{S\in\Omega_q}
 \mathbf1_S^{\mathsf T}Z\mathbf1_S,
\qquad
E_q:=\|\mu_q^{F_1}-\mu_q^{F_0}\|_1.
\tag{3.3}
\]

The hypothesis `D_q>0` forces `M_q>0`: if every displayed target weight
were zero, then `Tr(ZK_q(F_0))=0`, contradicting (3.1)--(3.2).

### Theorem 3.1 — exact movement--collision inequality

Under the preceding hypotheses,

\[
\boxed{
E_q+2Q_q(F_1)
\ge
\ell_q
:=\left\lceil\frac{D_q}{M_q}\right\rceil.}
\tag{3.4}
\]

#### Proof

Choose `beta in B_q` minimizing

\[
\|\mu_q^{F_1}-\beta\|_1.
\]

Since

\[
\sum_S(\beta(S)-d_q)
 \mathbf1_S\mathbf1_S^{\mathsf T}\succeq0,
\]

testing against `Z` gives

\[
0
\le
-D_q+
\sum_S(\beta(S)-\mu_q^{F_0}(S))
 \mathbf1_S^{\mathsf T}Z\mathbf1_S.
\]

Therefore

\[
D_q
\le M_q\|\beta-\mu_q^{F_0}\|_1
\le M_q\left(
E_q+\|\beta-\mu_q^{F_1}\|_1
\right).
\]

Lemma 2.1 bounds the last norm by `2Q_q(F_1)`.  The left side of (3.4)
is integral, so the ceiling is valid.  ∎

This theorem is quota-position independent and uses the actual endpoint
factor.  It does not assume an additive or independent packet model.

### Corollary 3.2 — mesoscopic two-block form

Let the positive and negative blocks `P_q,N_q` be disjoint, with

\[
|P_q|=|N_q|=s_q/2,
\qquad
s_q\le 2r_q,
\qquad
r_q+s_q/2\le n,
\]

where `r_q=m-q`, and assume the audited aggregate-bias hypothesis for the
Lane W two-block test.  Then

\[
D_q\ge\gamma q(q+1)t s_q,
\qquad
M_q=s_q^2/4.
\]

Hence

\[
\boxed{
E_q+2Q_q(F_1)
\ge
\left\lceil
\frac{4\gamma q(q+1)t}{s_q}
\right\rceil.}
\tag{3.5}
\]

If `s_q<=Cq`, then

\[
\boxed{
E_q+2Q_q(F_1)
\ge
\left\lceil
\frac{4\gamma}{C}(q+1)t
\right\rceil.}
\tag{3.6}
\]

## 4. Exact packet-size schedule obstruction

Allow any packet architecture: atomic packets, fused packets, or a
telescoping sequence of exact factors.  Suppose its available absolute
depth-`q` mass is

\[
\widehat A_q
=\sum_jP_{j,q}R_{j,q},
\tag{4.1}
\]

where every actual endpoint increment is covered by that budget.  Thus

\[
P_q:=\sum_jP_{j,q}
\]

is the total packet count at depth `q`, and

\[
E_q\le\widehat A_q.
\tag{4.2}
\]

### Theorem 4.1 — schedule lower bound with exact floors

For every set of certified mode depths `Q_m`,

\[
\boxed{
\sum_{q\in\mathcal Q_m}\frac{Q_q(F_1)}{d_q}
\ge
\sum_{q\in\mathcal Q_m}\frac1{d_q}
\left\lceil
\frac{(\ell_q-\widehat A_q)_+}{2}
\right\rceil.}
\tag{4.3}
\]

#### Proof

Equation (3.4) and (4.2) give

\[
2Q_q(F_1)\ge\ell_q-\widehat A_q.
\]

Take positive parts, use integrality, divide by the exact `d_q`, and sum.
∎

No rearrangement of the same packets improves (4.3): only their total
actual endpoint leverage matters.

### Theorem 4.2 — dense Gaussian schedule no-go

Fix constants

\[
0<a<A<\infty,\qquad \eta,\gamma,C,C_0>0.
\]

Suppose

\[
\mathcal Q_m
\subseteq
[\lceil a\sqrt m\rceil,\lfloor A\sqrt m\rfloor],
\qquad
|\mathcal Q_m|\ge\eta\sqrt m,
\tag{4.4}
\]

and at every `q in Q_m` the two-block hypotheses of Corollary 3.2 hold.
For all sufficiently large `m`, put

\[
D_A=\left\lfloor e^{2A^2+1}\right\rfloor.
\tag{4.5}
\]

Then

\[
1\le d_q\le D_A
\qquad(q\in\mathcal Q_m).
\tag{4.6}
\]

If at most `C_0t` packets are available at every such depth and their
mass is `o(q)` uniformly, then

\[
\boxed{
\sum_{q\in\mathcal Q_m}
\frac{Q_q(F_1)}{d_q}
=\Omega_{a,A,\eta,\gamma,C,C_0}(W).}
\tag{4.7}
\]

#### Proof

The exact quotient is

\[
\frac W{N_q}
=\prod_{j=1}^q
\left(1+\frac{q+1}{m-q+j}\right).
\]

For `q<=A sqrt(m)`, its logarithm is at most

\[
\frac{q(q+1)}{m-q+1}\le2A^2+1
\]

for all sufficiently large `m`, proving (4.6).

The mass hypothesis gives

\[
\widehat A_q=o(qt)
\]

uniformly.  Equations (3.6) and (4.3) therefore give a fixed positive
multiple of

\[
t\sum_{q\in\mathcal Q_m}\frac{q+1}{d_q}.
\]

Finally,

\[
\sum_{q\in\mathcal Q_m}\frac{q+1}{d_q}
\ge
\frac{\eta a}{D_A}m,
\]

and `mt=(m/n)W=Theta(W)`.  ∎

### Corollary 4.3 — necessary critical schedule

Under all the hypotheses of Theorem 4.2, suppose precisely that the
weighted endpoint collision on the certified modes is small:

\[
\sum_{q\in\mathcal Q_m}\frac{Q_q(F_1)}{d_q}=o(W).
\]

Then

\[
\boxed{
\sum_{q\in\mathcal Q_m}\frac{\widehat A_q}{d_q}
\ge
\frac{4\gamma}{C}t
\sum_{q\in\mathcal Q_m}\frac{q+1}{d_q}
-o(W).}
\tag{4.8}
\]

If `P_q<=C_0t`, the global `d_q^{-1}`-weighted average packet mass on the
certified Gaussian depths is therefore `Omega(sqrt(m))`, the scale of a
typical `q` in the band.  No depth-dependent trade between packet count and
packet size changes the aggregate product required by (4.8); this sentence
does not assert the lower bound separately at every depth.

Indeed (4.3) and an `o(W)` left side imply

\[
\sum_{q\in\mathcal Q_m}
\frac{(\ell_q-\widehat A_q)_+}{d_q}=o(W).
\]

Since
`widehat A_q>=ell_q-(ell_q-widehat A_q)_+`, summation and (3.6) give
(4.8).

### Theorem 4.4 — exact-factor row-volume obstruction

At one depth, let `P_q,N_q` satisfy all the feasibility hypotheses of
Corollary 3.2, put

\[
u=\mathbf1_{P_q}-\mathbf1_{N_q},
\qquad
Z=uu^{\mathsf T},
\qquad
|P_q|=|N_q|=s_q/2,
\]

fix `gamma>0`, and define

\[
T_q(F)=\operatorname{Tr}Z(b_qI+H_q(F)).
\]

Assume

\[
T_q(F_0)\le-\gamma q(q+1)t s_q.
\tag{4.9}
\]

For another exact factor `F_1`, let

\[
k=t-|F_0\cap F_1|
\]

be the number of initial wreath rows absent from the endpoint.  Then

\[
\boxed{
Q_q(F_1)
\ge
\frac{4q(q+1)}{s_q}(\gamma t-2k)_+,}
\tag{4.10}
\]

or equivalently

\[
\boxed{
k\ge
\frac{\gamma t}{2}
-\frac{s_qQ_q(F_1)}{8q(q+1)}.}
\tag{4.11}
\]

Consequently, under the dense-band hypotheses of Theorem 4.2, if

\[
\sum_{q\in\mathcal Q_m}\frac{Q_q(F_1)}{d_q}=o(W),
\]

then

\[
\boxed{k\ge(\gamma/2-o(1))t.}
\tag{4.12}
\]

If `F^(0)=F_0,...,F^(J)=F_1` is any exact-factor trajectory and

\[
c_j=|F^{(j-1)}\setminus F^{(j)}|,
\]

then

\[
n\sum_{j=1}^Jc_j\ge nk
\ge(\gamma/2-o(1))W.
\tag{4.13}
\]

The left side is cumulative row-event volume, counted with multiplicity.
Independently, at least `nk` distinct initial middle vertices are touched,
because the `k` endpoint-deleted initial wreaths are pairwise disjoint.

#### Proof

The one-row tail matrix is symmetric, nonnegative, and
`q(q+1)`-regular.  Its operator norm is at most `q(q+1)`.  Removing `k`
initial rows and inserting `k` endpoint rows therefore gives

\[
T_q(F_1)
\le T_q(F_0)+2kq(q+1)\operatorname{Tr}Z
\le-q(q+1)s_q(\gamma t-2k),
\tag{4.14}
\]

because `Tr Z=s_q` for the two-block rank-one test.  Proposition 5.2
below, applied to `F_1` when its trace is negative and using
`Tr(ZK_q(F_1))=T_q(F_1)` because `Z1=0`, gives

\[
T_q(F_1)\ge-M_qQ_q(F_1);
\]

the same inequality is trivial when the trace is nonnegative.  Since
`M_q=s_q^2/4`, comparison with (4.14) proves (4.10)--(4.11).

On the dense band,

\[
t\sum_{q\in\mathcal Q_m}\frac q{d_q}=\Omega(W).
\]

Thus a restricted collision ledger `o(W)` has some certified depth with
`Q_q(F_1)=o(qt)`.  Since `s_q<=Cq`, (4.11) gives (4.12).  Finally the
symmetric-difference metric on row sets gives `sum_j c_j>=k`, proving
(4.13).  ∎

This theorem allows a packet shared across all depths and arbitrary
refreshed or dependent packets.  It rules out `o(W)` physical row-edit
mass around a certified negative-mode factor.  It does **not** rule out a
global exact-factor replacement of linear mass whose endpoint is
quota-directed.

### Corollary 4.5 — shared-packet multidepth charge

For any exact-factor trajectory `F^(0)=F_0,...,F^(J)` put

\[
V_{j,q}
=\|\mu_q(F^{(j)})-\mu_q(F^{(j-1)})\|_1
\tag{4.15}
\]

and

\[
\mathcal M_{\rm path}
=\sum_{q\in\mathcal Q_m}\frac1{d_q}
  \sum_{j=1}^JV_{j,q}.
\tag{4.16}
\]

Then, with no independence or disjointness assumption,

\[
\boxed{
\mathcal M_{\rm path}
+2\sum_{q\in\mathcal Q_m}\frac{Q_q(F^{(J)})}{d_q}
\ge
\sum_{q\in\mathcal Q_m}\frac{\ell_q}{d_q}.}
\tag{4.17}
\]

Under Theorem 4.2's dense Gaussian hypotheses and final restricted
collision `o(W)`,

\[
\boxed{
\liminf_{m\to\infty}
\frac{\mathcal M_{\rm path}}W
\ge\frac{2\gamma\eta a}{CD_A}.}
\tag{4.18}
\]

#### Proof

The triangle inequality gives

\[
E_q\le\sum_jV_{j,q}.
\]

Insert this into (3.4), divide by `d_q`, and sum to obtain (4.17).
Equations (3.6), (4.4), and (4.6) give

\[
\sum_{q\in\mathcal Q_m}\frac{\ell_q}{d_q}
\ge
\frac{4\gamma}{C}t\frac{\eta a}{D_A}m.
\]

Since `mt/W->1/2`, (4.18) follows.  ∎

A physical packet used at many depths is counted once at each target in
its actual shadow profile.  Thus shared signs and packet fusion do not make
the additive weighted-shadow-mass ledger `o(W)`.  The result does not
identify this ledger with literal word-length cost.

### Sparse-depth boundary

Define

\[
\Sigma_m(\mathcal Q_m)
=\sum_{q\in\mathcal Q_m}\frac{q+1}{d_q}.
\tag{4.19}
\]

A formal matched critical envelope

\[
\widehat A_q=\Theta((q+1)t)
\]

with uniform two-sided constants and bounded target congestion has an
`o(W)` **absolute stability envelope restricted to** `Q_m` exactly when

\[
\Sigma_m(\mathcal Q_m)=o(n).
\tag{4.20}
\]

Inside the fixed band (4.4), this is equivalent to

\[
|\mathcal Q_m|=o(\sqrt m).
\tag{4.21}
\]

Thus finitely many Gaussian modes are affordable at the level of this
restricted formal envelope.  This assertion assumes no uncontrolled
spillover at depths outside `Q_m`; it does not construct an
exact-factor-realizable schedule.  A positive-density Gaussian family is
not affordable within this envelope.

## 5. Why curvature-only fusion cannot finish

### Proposition 5.1 — integral endpoint curvature

For every integral histogram displacement `delta_q`,

\[
\|\delta_q\|_2^2\ge\|\delta_q\|_1.
\tag{5.1}
\]

Consequently, if

\[
\|\delta_q\|_1\ge\kappa qt
\]

through all integer depths

\[
a\sqrt m\le q\le A\sqrt m,
\]

then

\[
\frac12\sum_q\frac{\|\delta_q\|_2^2}{d_q}
\ge
\left(
\frac\kappa4
\int_a^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}
-o(1)
\right)W.
\tag{5.2}
\]

#### Proof

For an integer `z`, `z^2>=|z|`, proving (5.1).  The exact Gaussian floor
Riemann sum is

\[
\frac1m\sum_{q=\lceil a\sqrt m\rceil}^{\lfloor A\sqrt m\rfloor}
\frac q{d_q}
\longrightarrow
\int_a^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\]

Since `mt/W=m/n->1/2`, (5.2) follows.  ∎

Thus, conditional on the displayed `Omega(qt)` endpoint displacement at
every depth of the band, neither packet fusion nor dependence among its
constituent moves can make the diagonal endpoint-curvature ledger `o(W)`.
This is not by itself a collision lower bound, because the linear term may
be negative.  For the
equal-total endpoint displacements considered here,

\[
\sum_S\delta_q(S)=0,
\]

and the exact energy identity is

\[
Q_q(\mu_q+\delta_q)-Q_q(\mu_q)
=\langle\mu_q,\delta_q\rangle
 +\frac12\|\delta_q\|_2^2.
\tag{5.3}
\]

The only possible escape is a negative linear term canceling essentially
all of (5.2).

### Proposition 5.2 — the obstructed mode already carries collision debt

Let

\[
w_S=\mathbf1_S^{\mathsf T}Z\mathbf1_S,
\qquad 0\le w_S\le M,
\]

and suppose

\[
D=-\sum_S(\mu(S)-d)w_S>0.
\]

Then

\[
\boxed{Q_d(\mu)\ge D/M.}
\tag{5.4}
\]

#### Proof

Only cells with `mu(S)<d` contribute positively to `D`; all cells above
the floor have nonnegative coefficient and can only reduce it.  Therefore

\[
D
\le M\sum_{\mu(S)<d}(d-\mu(S)).
\]

Every unit below the floor contributes at least one unit to `Q_d`, proving
(5.4).  ∎

Thus the `Omega(W)` curvature in (5.2) can in principle be paid by removing
collision already present in the negative-mode histogram.  The required
fusion must be quota-directed, not merely covariance-balanced.

### Lemma 5.3 — one downhill transfer

Moving one occurrence from a cell of load `x` to a cell of load `y`
changes collision by exactly

\[
\boxed{y-x+1.}
\tag{5.5}
\]

In particular the move is collision-nonincreasing whenever `x>=y+1`.

#### Proof

Use (5.3) with `delta=-e_X+e_Y`.  Its squared norm is two.  ∎

## 6. Point-regular floor/ceiling quotas always exist

Let `U_r` be the point-versus-`r`-set incidence matrix.

### Theorem 6.1 — regular high-quota family

Fix `1<=r<=n-1`, and let an arbitrary integral rank-`r` vector `mu`
satisfy

\[
\sum_S\mu(S)=W,
\qquad
U_r\mu=rt\mathbf1.
\tag{6.1}
\]

Put

\[
d=\left\lfloor\frac W{\binom nr}\right\rfloor,
\qquad
\rho=W-d\binom nr,
\]

and

\[
k
=rt-d\binom{n-1}{r-1}
=\frac{r\rho}{n}\in\mathbb Z.
\tag{6.2}
\]

There exists a simple `r`-uniform family

\[
\mathcal H\subseteq\binom{[n]}r,
\qquad |\mathcal H|=\rho,
\]

in which every point has degree exactly `k`.  Consequently

\[
\boxed{
\beta=d\mathbf1+\mathbf1_{\mathcal H}}
\tag{6.3}
\]

has total mass `W`, satisfies

\[
U_r\beta=rt\mathbf1,
\tag{6.4}
\]

and has

\[
Q_d(\beta)=0.
\tag{6.5}
\]

#### Proof

The identity in (6.2) follows from

\[
n\binom{n-1}{r-1}=r\binom nr
\]

and `nt=W`.  In particular `k` is integral.

Among all `rho`-edge simple `r`-families, choose one minimizing the sum of
squared point degrees.  If two points `u,v` have

\[
d(u)\ge d(v)+2,
\]

then there is an edge `E` containing `u` and not `v` for which

\[
E-u+v
\]

is absent.  Indeed, otherwise the injective map

\[
E\longmapsto E-u+v
\]

would send all `d(u)-d(u,v)` edges containing `u` but not `v` into the
`d(v)-d(u,v)` edges containing `v` but not `u`, contradicting the degree
inequality.

Replacing `E` by `E-u+v` decreases the degree-square sum.  Therefore all
degrees differ by at most one.  Their average is the integer

\[
\frac{r\rho}{n}=k,
\]

so every degree equals `k`.  Equations (6.3)--(6.5) follow.  ∎

Every such `beta` has a PSD histogram moment Gram matrix and therefore
removes **all** negative modes of that moment matrix at rank `r`, not just
one chosen mode.  This sentence does not assert that `beta` is realized by
an exact cyclic factor.

For any nonnegative target weights `w_S`, a coordinate relabeling by some
permutation in the full symmetric group of one regular high family also
satisfies

\[
\sum_{S\in\mathcal H}w_S
\ge
\frac{\rho}{\binom nr}\sum_Sw_S,
\tag{6.6}
\]

because averaging the symmetric-group orbit includes every target with
probability `rho/binom(n,r)`.

## 7. Exact quota-directed fusion in the point-margin fibre

For integral vectors `g,delta`, write

\[
g\sqsubseteq\delta
\]

when they lie in the same orthant and
`|g(S)|<=|delta(S)|` at every coordinate.

### Theorem 7.1 — conformal nonlocal fusion

Let `mu,beta` be nonnegative integral rank-`r` histograms satisfying

\[
U_r\mu=U_r\beta,
\]

and suppose `beta` is a floor/ceiling quota vector.  Put

\[
\delta=\beta-\mu.
\]

There is a conformal decomposition

\[
\delta=g_1+\cdots+g_s,
\qquad
g_i\in\operatorname{Gr}(U_r),
\tag{7.1}
\]

such that, for every `j`,

\[
\mu^{(j)}
:=\mu+\sum_{i=1}^jg_i
\tag{7.2}
\]

is nonnegative, has the same point margins, lies coordinatewise between
`mu` and `beta`, and satisfies

\[
\boxed{
Q_d(\mu^{(j)})
\le Q_d(\mu^{(j-1)}).}
\tag{7.3}
\]

Moreover,

\[
\sum_i\|g_i\|_1=\|\beta-\mu\|_1,
\qquad
Q_d(\mu^{(s)})=0.
\tag{7.4}
\]

#### Proof

The difference `delta` lies in `ker_Z U_r`.  If it is nonzero, choose a
nonzero conformally indecomposable kernel vector `g_1` with

\[
g_1\sqsubseteq\delta.
\]

If the remainder is nonzero, repeat.  The `l1` norm strictly decreases, so
the process terminates.  The indecomposable vectors are precisely the
Graver elements, and conformality gives the norm identity in (7.4).

Every negative coordinate of a packet decreases a donor monotonically
toward `beta(S)>=d`; every positive coordinate increases a receiver
monotonically toward `beta(S)<=d+1`.  On the donor side, the function

\[
z\longmapsto\frac12z(z-1)
\]

does not increase when an integer `z>=1` moves down toward `0` or `1`.
On the receiver side it does not increase when an integer `z<=0` moves up
toward `0` or `1`.  Thus every coordinate contribution is nonincreasing,
proving (7.3).  Point margins are preserved because every `g_i` is in the
kernel.  The endpoint is `beta`, proving the last assertion.  ∎

This is an exact integral nonlocal packet fusion.  When it is applied to a
mesoscopically obstructed reference histogram, every zero-collision quota
endpoint has the `Omega(qt)` displacement forced by Theorem 3.1, and the
fusion reaches such an endpoint with no absolute-mass overhead.  Its
packets need not have bounded size.

### Proposition 7.2 — nonlocal packet size is genuinely necessary in the
conformal corridor

Assume `r>=2` and `2ell<=n-r+2`.  Let `K` have size `r-2`, and let

\[
v_1,\ldots,v_{2\ell}
\]

be distinct points outside `K`.  With cyclic indices, put

\[
g
=\sum_{i\text{ odd}}e_{K\cup\{v_i,v_{i+1}\}}
 -\sum_{i\text{ even}}e_{K\cup\{v_i,v_{i+1}\}}.
\tag{7.5}
\]

Then

\[
g\in\operatorname{Gr}(U_r),
\qquad
\|g\|_1=2\ell.
\tag{7.6}
\]

Thus Graver packet mass can be `Theta(m)` in the Gaussian regime
`r=m-q`, where the complement of `K` has order `m`.

#### Proof

At every `v_i`, the two incident cycle edges have opposite signs, so
`U_rg=0`; points of `K` see equally many positive and negative terms.

If a nonzero `h\sqsubseteq g` lies in the kernel, balance at `v_i` forces
the two incident coefficients either both to occur with their prescribed
opposite signs or both to vanish.  Connectivity of the cycle forces all
terms to be present.  Since the coefficients of `g` have magnitude one,
`h=g`.  Hence `g` is conformally indecomposable.  ∎

## 8. A constructive bounded-packet buffer regime

Large conformal packets can sometimes be replaced by bounded packets if
temporary quota cells are available.

### Theorem 8.1 — alternating-cycle rectangle fan

Use the notation and domain of Proposition 7.2 and assume `ell>=2`.
Define donor
cells

\[
D_0=K\cup\{v_{2\ell},v_1\},
\qquad
D_j=K\cup\{v_{2j},v_{2j+1}\}
\quad(1\le j\le\ell-1),
\tag{8.1}
\]

target cells

\[
T_j=K\cup\{v_{2j-1},v_{2j}\}
\quad(1\le j\le\ell),
\tag{8.2}
\]

and temporary chords

\[
C_j=K\cup\{v_{2j-1},v_{2\ell}\}
\quad(2\le j\le\ell-1).
\tag{8.3}
\]

Suppose initially:

- every donor has load at least `d+1`;
- every target has load at most `d`;
- every temporary chord has load exactly `d` and is not used elsewhere in
  the fan.

For `1<=j<=ell-1`, interpret `C_1=D_0` and
`C_ell=T_ell`, and apply the four-cell packet

\[
g_j
=-e_{C_j}-e_{D_j}+e_{T_j}+e_{C_{j+1}}.
\tag{8.4}
\]

Then:

1. `U_rg_j=0` and `||g_j||_1=4`;
2. every intermediate histogram is nonnegative and has the same point
   margins;
3. collision never increases;
4. the endpoint decreases every donor by one, increases every target by
   one, and restores every temporary chord to load `d`.

#### Proof

The two negative cells and two positive cells have the same multiset union
of points, proving `U_rg_j=0`.  The first packet consumes `D_0` and creates
`C_2`; every later packet consumes the preceding chord and creates the next
one.  The last created chord is `T_ell`, so all intermediate chords cancel.

Donors move downward toward the slab and targets move upward toward it.
Every temporary chord undergoes

\[
d\longrightarrow d+1\longrightarrow d,
\]

which has zero collision throughout.  Coordinatewise monotonicity of the
other moves proves the result.  ∎

This gives a rigorous constant-size packet schedule for a nontrivial class
of large quota corrections.  It is a histogram theorem; a physical PBBS
factor circuit realizing the refreshed chords is not known.

## 9. Simultaneous signed multidepth fusion

Let `Omega_m` be the set of unoriented cyclic orders, and let `B_r` map an
integral row coefficient vector to its cyclic rank-`r` interval histogram.
For `q>=1`, put

\[
\mathcal K^{(q)}
=\ker_{\mathbb Z}B_m
 \cap\bigcap_{s=m-q+1}^{m-1}\ker_{\mathbb Z}B_s.
\tag{9.1}
\]

The audited integral shallow-filtration theorem states that, for
`1<=q<=m-2`,

\[
\boxed{
B_{m-q}:\mathcal K^{(q)}
\twoheadrightarrow\ker_{\mathbb Z}U_{m-q}.}
\tag{9.2}
\]

### Theorem 9.1 — exact signed Gaussian quota schedule

Let `F` be any exact factor and fix `H<=m-2`.  There is an integral signed
row vector

\[
x^{(H)}\in\mathbb Z^{\Omega_m}
\]

such that

\[
B_mx^{(H)}=\mathbf1
\tag{9.3}
\]

and, simultaneously for every `1<=q<=H`,

\[
B_{m-q}x^{(H)}
\in\{d_q,d_q+1\}^{\Omega_q}.
\tag{9.4}
\]

In particular every controlled collision is zero.

#### Proof

Start from the `0/1` incidence vector `x^(0)=1_F`.  Suppose
`x^(q-1)` has already been made quota-exact at depths below `q`.  Its
rank-`(m-q)` histogram has point margins

\[
U_{m-q}B_{m-q}x^{(q-1)}
=(m-q)t\mathbf1.
\]

Indeed `B_mx^(q-1)=1` implies `sum_C x_C^(q-1)=t`, and every cyclic order
contains each point in exactly `m-q` rank-`(m-q)` intervals.  This argument
remains valid for signed row coefficients.

After the first correction the displayed rank vector may have negative
coordinates.  Theorem 6.1 was stated for an arbitrary integral vector and
its construction uses only these point margins, so it still supplies a
regular quota `beta_q` with the same point margins.  Then

\[
\delta_q
=\beta_q-B_{m-q}x^{(q-1)}
\in\ker_{\mathbb Z}U_{m-q}.
\]

By (9.2), choose `z_q in K^(q)` with

\[
B_{m-q}z_q=\delta_q.
\]

Put

\[
x^{(q)}=x^{(q-1)}+z_q.
\]

The definition of `K^(q)` preserves exact middle ownership and every
previously fixed shallower depth.  It makes depth `q` equal to `beta_q`.
Induction proves (9.3)--(9.4).  ∎

The lifts can be chosen packetwise after a conformal Graver decomposition.
Although Theorem 7.1 states its physical version for nonnegative
histograms, its coordinatewise algebraic argument extends verbatim to an
arbitrary integral vector moving conformally toward a `{d_q,d_q+1}` quota:
the polynomial `z(z-1)/2` is nonincreasing along every such integer
coordinate path.  Thus at the active rank the algebraic collision
polynomial is nonincreasing while all already fixed ranks remain unchanged.
At deeper unfixed ranks, the intermediate histograms and row coefficients
may already be signed; no physical nonnegativity is asserted.

### Exact limitation

The vector `x^(H)` is integral but signed.  Its coordinates need not lie in
`{0,1}` or even be nonnegative.  Therefore (9.3) is an exact middle
relation, not an exact factor.  Frozen integrality forbids using it as a
literal OR construction.

## 10. A Gaussian containment cut blocks universal positive fusion

For a cyclic row `C`, let `W_s(C)` be its `n` cyclic rank-`s` windows.
For `r=m-q` and `U subseteq binom([n],r)`, write

\[
\partial_q^+\mathcal U
=\left\{M\in\binom{[n]}m:
R\subseteq M\text{ for some }R\in\mathcal U\right\}.
\tag{10.1}
\]

### Lemma 10.1 — exact containment cut and negative-mass certificate

For every cyclic row `C`, put

\[
u_C=|W_r(C)\cap\mathcal U|,
\qquad
v_C=|W_m(C)\cap\partial_q^+\mathcal U|.
\tag{10.2}
\]

Then `u_C<=v_C`.  If an integral rank-`r` target vector `b` has

\[
\Delta_{\mathcal U}(b)
:=\sum_{R\in\mathcal U}b(R)-|\partial_q^+\mathcal U|>0,
\tag{10.3}
\]

there is no nonnegative real cyclic-row vector `x` satisfying

\[
B_mx=\mathbf1,
\qquad
B_rx=b.
\tag{10.4}
\]

More sharply, define

\[
\Gamma(\mathcal U)=\max_C(v_C-u_C)\le n.
\tag{10.5}
\]

If a signed real lift `y` satisfying (10.4) exists, then
`Delta_U(b)>0` forces `Gamma(U)>0`, and every such lift obeys

\[
\boxed{
\|y^-\|_1
\ge
\frac{\Delta_{\mathcal U}(b)}{\Gamma(\mathcal U)}
\ge
\frac{\Delta_{\mathcal U}(b)}n.}
\tag{10.6}
\]

Here `y^-_C=max{-y_C,0}` coordinatewise.

#### Proof

Inside one row, join a rank-`r` window to every rank-`m` window containing
it.  This is a `(q+1)`-regular bipartite graph on the `n` window positions
on each side.  The neighbors of the `u_C` selected rank-`r` positions are
all counted by `v_C`.  Regular bipartite edge counting, or Hall's
inequality, gives `u_C<=v_C`.

If (10.4) holds, exact summation gives

\[
\Delta_{\mathcal U}(b)
=\sum_Cy_C(u_C-v_C).
\tag{10.7}
\]

For a signed lift, the positive left side forces some `v_C-u_C>0`, so
`Gamma(U)>0`.
Every coefficient `u_C-v_C` is nonpositive.  Thus a nonnegative `y`
makes the right side nonpositive.  For signed `y`, its positive part still
contributes nonpositively, while its negative part contributes at most
`Gamma(U)||y^-||_1`.  This proves (10.6).  ∎

### Theorem 10.2 — explicit zero-collision Gaussian quota outside the
fractional factor cone

Let `n=2m+1` tend to infinity through odd primes and put

\[
q=\left\lfloor\frac{\sqrt m}{2}\right\rfloor,
\qquad
r=m-q,
\qquad
N=\binom nr,
\qquad
\lambda=\frac WN.
\tag{10.8}
\]

For all sufficiently large such `n`, there is a cyclic-invariant family

\[
\mathcal H\subseteq\binom{[n]}r
\]

for which

\[
\beta=\mathbf1+\mathbf1_{\mathcal H}
\tag{10.9}
\]

has all of the following properties:

1. `beta` has total `W` and exact point margins `rt 1`;
2. `beta` is a floor/ceiling quota and `Q_q(beta)=0`;
3. its centered moment Gram matrix is positive semidefinite;
4. no nonnegative real `x`, and hence no exact factor, satisfies
   `B_mx=1` and `B_rx=beta`;
5. nevertheless the audited integral shallow-filtration theorem supplies
   an integral signed lift, and every signed lift satisfies

   \[
   \boxed{
   \|x^-\|_1
   \ge
   \frac{2-e^{1/4}}{16}\frac W{n^3}.}
   \tag{10.10}
   \]

#### Proof

Fix a cyclic ordering of the coordinates and put

\[
a=\lceil2\log_2n\rceil.
\]

Let `U` be the family of all rank-`r` sets containing at least one cyclic
block of `a` consecutive coordinates.  The union bound and one fixed block
give

\[
\binom{n-a}{r-a}
\le|\mathcal U|
\le n\binom{n-a}{r-a}.
\tag{10.11}
\]

Moreover,

\[
\frac1N\binom{n-a}{r-a}
=\prod_{i=0}^{a-1}\frac{r-i}{n-i}
=2^{-a}\prod_{i=0}^{a-1}
\left(1-\frac{2q+i+1}{n-i}\right).
\tag{10.12}
\]

Here `a q/n+a^2/n=o(1)` and

\[
\frac1{2n^2}<2^{-a}\le\frac1{n^2}.
\]

Therefore, for all sufficiently large `m`,

\[
\boxed{
\frac N{4n^2}\le|\mathcal U|\le\frac Nn.}
\tag{10.13}
\]

Count pairs `(R,M)` with `R in U`, `M in binom([n],m)`, and `R subset M`.
Every `R` has `binom(m+q+1,q)` upper extensions.  Every `M` in the upper
shadow contains a distinguished cyclic `a`-block and therefore at least
`binom(m-a,q)` members of `U`.  Hence

\[
\frac{|\partial_q^+\mathcal U|}{|\mathcal U|}
\le
\theta_{m,q,a}
:=\frac{\binom{m+q+1}q}{\binom{m-a}q}.
\tag{10.14}
\]

The exact product formulas give

\[
\frac{\theta_{m,q,a}}\lambda
=\prod_{j=1}^q
\frac{m-q+j}{m-a-q+j}
\le
\exp\left(\frac{aq}{m-a-q+1}\right)
\longrightarrow1.
\tag{10.15}
\]

Also `lambda->e^(1/4)`.  Thus `d_q=floor(lambda)=1` eventually and

\[
\theta_{m,q,a}\longrightarrow e^{1/4}<2.
\tag{10.16}
\]

Put

\[
\rho=W-N.
\]

Then `rho/N->e^(1/4)-1>0`, whereas (10.13) gives
`|U|/N<=1/n`; hence `rho>=|U|` eventually.  Because `n` is prime, every
nontrivial subset has a full orbit of size `n` under cyclic coordinate
rotation.  Thus `n` divides `|U|`, `N`, `W`, and `rho`.  Extend `U` by
whole unused cyclic orbits to a cyclic-invariant family `H` of exactly
`rho` rank-`r` sets.  This is possible because `rho<N` and
`n` divides `rho-|U|`.

Cyclic invariance makes `H` point-regular, of degree `r rho/n`.  Therefore

\[
U_r\beta
=\left(\binom{n-1}{r-1}+\frac{r\rho}n\right)\mathbf1
=\frac{rW}n\mathbf1
=rt\mathbf1.
\tag{10.17}
\]

Its total is `N+rho=W`; (10.9) is an exact quota and has zero collision.
Also

\[
\sum_R(\beta(R)-1)\mathbf1_R\mathbf1_R^{\mathsf T}
=\sum_{R\in\mathcal H}\mathbf1_R\mathbf1_R^{\mathsf T}
\succeq0.
\tag{10.18}
\]

But `U subseteq H`, so by (10.14)--(10.16),

\[
\Delta_{\mathcal U}(\beta)
=2|\mathcal U|-|\partial_q^+\mathcal U|
\ge\frac{2-e^{1/4}}2|\mathcal U|>0
\tag{10.19}
\]

for all sufficiently large `m`.  Lemma 10.1 excludes every nonnegative
fractional lift.  The shallow-filtration surjectivity supplies an integral
signed lift because `beta` has the required point margins.  Finally
`N>=W/2` eventually, so (10.6), (10.13), and (10.19) give

\[
\|x^-\|_1
\ge\frac{2-e^{1/4}}2\frac1n\frac{N}{4n^2}
\ge\frac{2-e^{1/4}}{16}\frac W{n^3}.
\]

This proves every assertion.  ∎

The obstruction is higher-order than total mass, point margins, and every
PSD boundary-moment test: the quota passes all of them but violates one
literal containment cut.  It definitively rules out a universal
positivization of Theorem 9.1 based only on those data.  It does not rule
out jointly choosing a different, liftable quota and therefore is not a
counterexample to MWB or constant one.

## 11. Existing bounded exact cubes have insufficient leverage

The audited fixed MSW local `C8` packet has

\[
\|\delta_{i,1}\|_1=4,
\qquad
\|\delta_{i,q}\|_1=8
\quad(2\le q\le m-2).
\tag{11.1}
\]

The available simultaneous exact-factor subcube has

\[
L=\operatorname{Cat}_{m-2}
\]

such binary components.  Any two cube vertices therefore satisfy

\[
E_q\le8L
=\frac{2m(m+1)}{(2m-1)(2m-3)}t
=O(t).
\tag{11.2}
\]

This is a factor `Theta(q)` below the `Omega(qt)` leverage demanded by a
Gaussian two-block mode.  While one stays inside this fixed commuting
cube, fusing, reordering, or correlating the same binary bits cannot change
their endpoint symmetric difference: parity reduces every repeated toggle
to one subset of the cube.  This does not exclude refreshed or dynamic
exact packets that become available after leaving the cube.

Thus the known bounded-mass exact cube cannot supply the `Omega(qt)` quota
correction demanded by a certified Gaussian negative mode.  It may still
realize a special quota correction whose required displacement is only
`O(t)`.

## 12. Ambient four-core dipoles and spectral tangent space

For an exact factor define its raw rank-`r_q` moment Gram matrix

\[
G_q(F)=\sum_{S\in\Omega_q}\mu_q^F(S)
\mathbf1_S\mathbf1_S^{\mathsf T}.
\]

Each point lies in exactly `r_q` cyclic rank-`r_q` windows in each of the
`t` wreaths.  Hence

\[
\operatorname{diag}G_q(F)=r_qt\mathbf1,
\qquad
G_q(F)\mathbf1=r_q^2t\mathbf1.
\]

The baseline terms in `K_q` and in the cyclic boundary identity are
factor-independent, so for two exact factors

\[
\Delta H_q=\Delta K_q=\Delta G_q.
\]

Subtracting the raw-moment identities therefore gives

\[
\Delta H_q\mathbf1=0,
\qquad
\operatorname{diag}\Delta H_q=0.
\tag{12.1}
\]

There is no further obstruction inside this ambient formal matrix lattice.
The tangent directions realized by actual exact-factor circuits may form a
strict subset.

### Proposition 12.1 — four-point dipoles generate the spectral tangent
lattice

Assume `n>=4`.  Every integral symmetric matrix `M` satisfying

\[
\operatorname{diag}M=0,
\qquad
M\mathbf1=0
\tag{12.2}
\]

is an integral sum of matrices

\[
\operatorname{sym}
\left[(e_a-e_d)(e_b-e_c)^{\mathsf T}\right]
\tag{12.3}
\]

with four distinct coordinates, where

\[
\operatorname{sym}(uv^{\mathsf T})=uv^{\mathsf T}+vu^{\mathsf T}.
\]

At any rank `r>=2`, these matrices are the second-moment dipoles of
elementary four-core relations

\[
A=I+\{a,b\},\quad
B=I+\{c,d\},\quad
C=I+\{a,c\},\quad
D=I+\{b,d\}.
\tag{12.4}
\]

Here `|I|=r-2` and `I` is disjoint from `{a,b,c,d}`.  For PBBS
first-shadow cores, `r=m-1`, so `|I|=m-3` and this interpretation requires
`m>=3`.

#### Proof

Identify the upper-triangular entries of `M` with an integral edge vector

\[
w\in\mathbb Z^{\binom{[n]}2}.
\]

The row-sum condition is

\[
U_2w=0.
\]

We give an integral elimination proof, avoiding any saturation assumption.
Fix distinct pivots `p,q`.  For every edge `ij` disjoint from `{p,q}`,
subtract an integral multiple of the rectangle

\[
e_{ij}+e_{pq}-e_{ip}-e_{jq}
\]

to eliminate its coefficient.  The remaining vector is supported on the
edges incident with `p` or `q`.  Write its coefficients as `a_i` on `ip`,
`b_i` on `iq`, and `c` on `pq`.  The point equations give

\[
b_i=-a_i,
\qquad
c=-\sum_i a_i=\sum_i a_i.
\]

Over the integers, `2 sum_i a_i=0`, hence `sum_i a_i=0` and `c=0`.
The residual vector is therefore an integral sum of rectangles

\[
(e_{ip}-e_{iq})-(e_{jp}-e_{jq}),
\]

again on four distinct vertices.  This proves that the four-cycle
rectangles integrally generate `ker_Z U_2`, and each rectangle is the
upper-triangular edge vector of (12.3).  Expanding the second moment of
(12.4) gives the same dipole.  ∎

Thus the ambient elementary four-core charge-dipole class spans the formal
zero-diagonal, zero-row-sum matrix lattice.  It is unproved that the
actually available PBBS load-one packet subfamily spans this ambient
lattice.

This does **not** identify a core-charge dipole with the actual
depth-`q` shadow-moment change of a PBBS switch.  Endpoint-compatible seams,
exact-wreath output, and simultaneous realization over all `q` remain
unproved.

### Proposition 12.2 — direct synchronized-connector no-go

Assume `m>=3` and let `F` be a spanning `2`-factor of `KG(2m+1,m)`.
Choose an `(m-2)`-set `H` and distinct labels `b,c,u` outside it.  Put

\[
K_b=H+\{b\},\qquad K_c=H+\{c\},
\]

\[
X_b=H+\{b,u\},\qquad
X_c=H+\{c,u\},\qquad
Z=H+\{b,c\},
\]

and

\[
Y=[n]\setminus(H\cup\{b,c,u\}).
\tag{12.5}
\]

Suppose two `F`-alternating common-core `C8` cycles based at `K_b,K_c`
both use the direct low connector `Y`, with their two incident cycle-edge
pairs at `Y` equal to

\[
\{YX_b,YZ\},
\qquad
\{YX_c,YZ\}.
\tag{12.6}
\]

Here a common-core `C8` is the standard PBBS lift of a residual directed
`C4`: each of its four high vertices contains the core and each of its four
low vertices is disjoint from the core.

Then their simultaneous symmetric-difference toggle is not a `2`-factor.
More generally, let `H_1!=H_2` be two `(m-2)`-sets avoiding `b,c,u`, and
take the four analogous direct-connector cycles based at

\[
H_i+\{b\},\ H_i+\{c\}
\qquad(i=1,2).
\]

Their simultaneous toggle is not a `2`-factor either.

#### Proof

The sets `X_b,X_c` have intersection `H+{u}` of size `m-1`, so their
union has size `m+1`; its complement `Y` is their unique common neighbor
in the odd graph.  In (12.6), each pair contains exactly one factor edge.

If `YZ` is not in `F`, then `YX_b` and `YX_c` are the two old factor edges
at `Y`.  Toggling both cycles removes them, while the duplicated proposed
edge `YZ` cancels modulo two.  The resulting degree at `Y` is zero.

If `YZ` is in `F`, then `YX_b,YX_c` are both proposed new edges.  The
duplicated removal of `YZ` cancels, so both original factor edges at `Y`
remain and both proposed edges are added.  The resulting degree is four.
Thus the two-cycle toggle already fails locally.

For the four-cycle statement, put

\[
Y_i=[n]\setminus(H_i\cup\{b,c,u\}).
\]

The two cycles based at `H_2` cannot contain `Y_1`.  A vertex of a
common-core `C8` is either high and contains its core or low and is
disjoint from it.  Since `Y_1` excludes `b,c`, it cannot be high for an
`H_2` core.  If it were low for `H_2+{b}`, then

\[
H_2+\{b\}
\subseteq[n]\setminus Y_1
=H_1+\{b,c,u\}.
\]

As both `H_i` avoid `c,u` and have the same size, this forces `H_2=H_1`,
a contradiction; the `c` case is identical.  Hence the other two cycles
cannot repair the degree-zero/four defect at `Y_1`.  ∎

This closes the natural one-cell rank-one fusion of the synchronized
four-core PBBS packet before balance or shallow shadows are tested.  It
does not exclude a larger retained-tail circuit containing an additional
alternating component through each defective connector.  The existing
Catalan packet supply is not ruled out by a raw cut-count comparison; the
remaining obstruction is endpoint-compatible, quota-downhill multidepth
alignment, not merely the number of available cores.

## 13. Precise constant-one boundary

### Proved

1. Under a positive-density Gaussian family of certified mesoscopic Lane W
   negative modes, every `O(t)` packet schedule with mass `o(q)` has
   `Omega(W)` actual restricted weighted collision.
2. Under the same hypothesis, every endpoint with restricted weighted
   collision `o(W)` must supply linear-in-`q` packet mass in weighted
   aggregate.  Every exact-factor path to it has `Omega(W)` weighted
   shadow-movement mass, with arbitrary cross-depth packet sharing allowed.
3. Under that hypothesis, every endpoint with restricted weighted
   collision `o(W)` differs from the certified reference in at least
   `(gamma/2-o(1))t` wreath rows, so its cumulative and distinct-initial
   touched-middle volume is `Omega(W)`.
4. If the endpoint displacement is `Omega(qt)` throughout the Gaussian
   band, its diagonal endpoint-curvature ledger is `Omega(W)`.  This does
   not preclude cancellation by the negative linear term.
5. Every point-regular integral rank histogram admits a point-regular
   exact quota, and a conformal integral fusion reaches it with no
   collision increase and zero final collision.
6. Alternating matching deficits admit an explicit mass-four buffered
   rectangle schedule.
7. Every finite Gaussian collection admits a simultaneous integral signed
   cyclic-row solution with exact middle ownership and zero collision.
8. Along prime `n=2m+1`, a concrete point-regular zero-collision Gaussian
   quota lies outside the fractional exact-factor cone and forces signed
   negative row mass at least `(2-e^(1/4))W/(16n^3)`.
9. The ambient four-core dipole class spans every direction in the formal
   integral zero-diagonal, zero-row-sum spectral tangent lattice.
10. The specific paired direct-connector four-`C8` PBBS configuration of
    Proposition 12.2 is not a `2`-factor toggle: at the connector of either
    paired subconfiguration (in particular `Y_1`), the final degree is zero
    or four.

### Not proved

1. No theorem jointly chooses liftable floor/ceiling quotas through a
   Gaussian window and realizes them in one exact factor.  The explicit
   bad quota rules out only a universal lift of arbitrary regular quotas.
2. The buffered four-cell rectangles are histogram trades, not PBBS
   factor-fibre circuits.
3. The four-core charge dipoles are not proved to equal actual PBBS shadow
   moment increments.
4. The direct-connector no-go does not exclude larger retained-tail
   circuits with additional alternating components through the connector.
5. The known exact bounded-mass `C8` cube has only `O(t)` endpoint leverage
   and cannot remove a certified Gaussian mode requiring `Omega(qt)`
   displacement.
6. No current theorem places a PBBS-derived exact reference factor in a
   positive-density family of Lane W modes; the schedule no-go is
   conditional on that explicit spectral hypothesis.

### Exact missing theorem

A constant-one completion of this lane now requires the following literal
statement:

> **Factor-fibre quota transport.**  Starting from one exact factor,
> jointly choose, at every controlled depth, a regular floor/ceiling quota
> satisfying every exact-factor containment cut, and realize its
> Theorem-7.1 correction (or the buffered rectangles of Theorem 8.1) by a
> conformal sequence of squarefree exact-factor circuits, using the same
> physical factor across all depths.  At depth `q`, every physical packet
> must preserve `B_m` and every already fixed rank
> `B_{m-1},...,B_{m-q+1}`, while realizing the prescribed `B_{m-q}`
> correction.

If this theorem held through every fixed Gaussian window, the endpoint
factor would have `Q_q=0` at all controlled depths and would compose
immediately into constant one.  Theorem 9.1 proves the complete integral
signed-lattice version, but exact-factor positivity is precisely the
unresolved gate.

No literal contiguous-OR word or constant-one theorem is claimed.

## 14. Independent audit record

The decisive claims were audited independently after the full statements
were written.

1. The quota-distance constant `2`, the movement--collision ceiling,
   `D_A=floor(e^(2A^2+1))`, the row-edit factors `4` and `1/8`, and the
   multidepth constant `2 gamma eta a/(C D_A)` were checked directly.
2. The signed-filtration induction was checked with signed intermediate
   vectors, and the distinction between the raw Gram matrix `G_q` and the
   Lane W tail matrix `H_q` was enforced.
3. The Gaussian containment construction was separately checked: both
   binomial ratios, the prime-orbit divisibilities, the strict
   `e^(1/4)<2` gap, the exact point margins, the containment cut, and the
   negative-mass constant in (10.10) all survive.
4. The direct PBBS connector proof was checked vertex-locally.  The two
   paired connectors were distinguished explicitly; the proof needs only
   the defect at `Y_1`.

All audit corrections are incorporated in the present text.  The audited
boundary remains exactly the one stated in Section 13.
