# Second-wave Y: stationary transposition-component switch chain

Date: 2026-07-24

## Verdict

The stationary measures and communicating classes of the fair
transposition-component heat chain can be described exactly.  For every
fixed transposition, the heat kernel is an orthogonal projection onto
intrinsic component-signing cells.  Every communicating class is a union of
whole cells, its unique stationary law is uniform, and that law is invariant
under every fixed-transposition projection separately.

The corrected Johnson baseline is

\[
4(n-1),
\]

not \(2n\).  With the unscaled component-noise convention, every stationary
class satisfies the exact two-slack identity

\[
\boxed{
 \mathbb E_{\mathscr C}R_H-4(n-1)\mathfrak B_H
 =
 4(n-1)\mathbb E_{\mathscr C}\mathcal Q_H
 +\mathbb E_{\mathscr C}\Xi_H .}
\tag{Y2.1}
\]

Here \(\mathfrak B_H\) is the unavoidable integer floor,
\(\mathcal Q_H\) is the floor-corrected energy, and
\(\Xi_H\ge0\) is the exact Johnson-degree-\(\ge3\) spectral surplus.
Stationarity proves

\[
\mathbb E_{\mathscr C}R_H=\mathbb E_{\mathscr C}D_H,
\]

but gives no upper bound on this common value.  Thus (Y2.1) is an identity,
not a Lyapunov estimate.  It does not force

\[
\mathbb E_{\mathscr C}\mathcal Q_{H_A}
=O_A\!\left(H_A\operatorname{Cat}_m\right).
\]

A rigorous projected one-class countermodel is given below.  It has
nonnegative integer loads in \(\{0,1,2\}\), the exact total and point
margins of a first-shadow exact factor, formal reversible pair-cell projections,
uniform stationarity, and the corrected \(4(n-1)\) spectrum, yet has
\(Q_1\ge W/2\).  It even has a signed integral exact-middle lift.  It is not a
nonnegative Boolean exact wreath factor.  Therefore it is a rigorous
obstruction to any proof using only stationarity, integer slice margins,
pair-cell covariance, and the corrected spectrum; it is not a counterexample
inside the true exact-factor state space.

For the true chain, the existence of a class with mean
\(O_A(H_A\operatorname{Cat}_m)\) remains unproved.  No unconditional
high-energy exact communicating class or full-class invariant is produced.
The strongest actual obstruction is conditional: a high-energy
transposition-rigid exact factor would have its coordinate orbit as a closed
high-energy class.

## 1. Setup and normalization

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,
\]

\[
N_q=\binom n{m-q},\qquad
a_q=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor a_q\rfloor,\quad 0\le\theta_q<1.
\]

The structural cell statements assume \(m\ge2\).  The floor-energy and
Gaussian-window sections assume \(m\ge3\) and
\(1\le H\le m-2\).

For an exact middle wreath factor \(F\), let
\(\mu_q(F,S)\) be the number of pointed cyclic intervals equal to the
\((m-q)\)-set \(S\).  Define

\[
f_q(F)=\mu_q(F)-a_q\mathbf1,
\]

\[
\beta_q=N_q\theta_q(1-\theta_q),
\]

\[
Q_q(F)=\|f_q(F)\|_2^2-\beta_q
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{Y2.2}
\]

For an admissible window \(1\le q\le H\le m-2\), set

\[
\mathcal Q_H(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q},
\qquad
\mathfrak B_H=\sum_{q\le H}\frac{\beta_q}{c_q},
\tag{Y2.3}
\]

so that

\[
\sum_{q\le H}\frac{\|f_q(F)\|_2^2}{c_q}
=\mathfrak B_H+\mathcal Q_H(F).
\tag{Y2.4}
\]

All norms are unnormalized counting norms.  Every transposition sum below
is over the \(\binom n2\) unordered coordinate transpositions, each counted
once.

The principal kernel in this report is the fair heat kernel.  For fixed
\(\tau\), it chooses independently and uniformly one complete side of every
ownership component.  Its kernel is denoted \(K_\tau\), and

\[
K=\binom n2^{-1}\sum_\tau K_\tau.
\tag{Y2.5}
\]

The elementary chain which first chooses \(\tau\) uniformly and then flips
one uniformly chosen component has the same communicating classes.  It is
also symmetric because the component count is constant throughout one
intrinsic \(\tau\)-cell, so its class-stationary laws are the same uniform
laws.  The projection and conditional-variance formulas below use the fair
kernel \(K_\tau\).

If instead one chooses uniformly from all available
\((\tau,\text{component})\) pairs with a state-dependent global
denominator, the stationary law is generally degree-biased.  Uniform-class
claims require the fair or per-\(\tau\) normalization just specified.

For the Gaussian window,

\[
H=H_A=\lceil A\sqrt m\rceil
\]

with fixed \(A>0\).  All finite identities hold whenever \(H\le m-2\), and
the Gaussian statements hold for all sufficiently large \(m\).

## 2. Intrinsic fixed-transposition cells

Fix a coordinate transposition \(\tau=(ab)\).

### Theorem 2.1: fixed middle interval

Every unoriented cyclic order \(P\) has a \(\tau\)-fixed middle interval.

### Proof

Among the \(n\) cyclic \(m\)-intervals of \(P\), the total number of
incidences with the two labels \(a,b\) is

\[
2m=n-1.
\]

If every middle interval contained exactly one of \(a,b\), that incidence
total would be \(n\).  Hence some middle interval contains both or neither,
and is fixed by \(\tau\).  \(\square\)

No coordinate transposition stabilizes an unoriented cyclic order when
\(m\ge2\).  The stabilizer of such an order is a conjugate of the dihedral
group \(D_n\).  A nonidentity rotation is not a transposition, while every
reflection of an odd \(n=2m+1\) cycle has cycle type

\[
1\,2^m,
\]

which is not the cycle type \(1^{n-2}2\) of a single transposition.

### Corollary 2.2: disjoint sides

For every exact factor \(F\) and every transposition \(\tau\),

\[
\boxed{F\cap\tau F=\varnothing\qquad(m\ge2).}
\tag{Y2.6}
\]

Indeed, if \(P=\tau Q\in F\cap\tau F\), then \(Q,\tau Q\in F\) share the
\(\tau\)-fixed middle interval supplied by Theorem 2.1.  Exactness forces
\(Q=\tau Q\), contradicting the stabilizer statement.

Form the edge-labelled bipartite ownership overlay of \(F\) and \(\tau F\).
The left vertices are the wreaths of \(F\), the right vertices are the
wreaths of \(\tau F\), and each middle \(m\)-set gives the edge joining its
unique owners.

Every vertex has degree \(n\).  The fixed interval in Theorem 2.1 gives, for
every left row \(P\), an edge from \(P\) to the right row \(\tau P\).
Consequently \(\tau\) preserves each connected overlay component and
exchanges its two sides.  Write the sides as

\[
L_1,\tau L_1;\quad\ldots\quad;L_k,\tau L_k.
\]

The two sides of each component have equal cardinality by regularity.

### Theorem 2.3: intrinsic cell theorem

For every sign vector \(\varepsilon\in\{\pm1\}^k\), independently select
\(L_i\) or \(\tau L_i\).  The selected wreaths form an exact factor.
The resulting \(2^k\) factors are distinct, and their set is independent of
the chosen base factor in it.

### Proof

Each ownership edge has one endpoint on each complete component side, so a
complete-side choice covers every middle set exactly once.  Corollary 2.2
makes the \(2^k\) choices distinct.

If the overlay is rebased at one of these children, every component whose
side was changed is simply read with its two sides reversed.  The same
edge-labelled components and the same \(2^k\) factors reappear.  \(\square\)

Call this set the intrinsic \(\tau\)-cell of \(F\).  On each cell,
\(K_\tau\) is the all-ones averaging matrix divided by the cell size.
Therefore, in the counting inner product,

\[
\boxed{
K_\tau^2=K_\tau=K_\tau^*.}
\tag{Y2.7}
\]

Thus \(K_\tau\) is exactly conditional expectation onto the partition by
intrinsic \(\tau\)-cells.

## 3. Communicating classes and all stationary measures

### Theorem 3.1: class structure

Every communicating class \(\mathscr C\) of \(K\) is a union of complete
\(\tau\)-cells for every fixed transposition \(\tau\).

### Proof

If \(F\in\mathscr C\), every member of its \(\tau\)-cell has positive
one-step transition probability from \(F\).  Hence every such member lies in
the same communicating class.  \(\square\)

It follows immediately that the uniform law
\(\pi_{\mathscr C}\) is invariant under every \(K_\tau\) separately.  If
\(\mathscr D\subseteq\mathscr C\) is a \(\tau\)-cell and
\(G\in\mathscr D\), then

\[
(\pi_{\mathscr C}K_\tau)(G)
=\sum_{F\in\mathscr D}
\frac1{|\mathscr C|}\frac1{|\mathscr D|}
=\frac1{|\mathscr C|}.
\]

Conditional on the cell, its component signs are independent fair bits.
The stationary law weights different \(\tau\)-cells in proportion to their
sizes \(2^k\); it is not uniform over cells.

The full kernel \(K\) is symmetric.  Therefore:

1. \(\pi_{\mathscr C}\) is the unique stationary law on the irreducible
   class \(\mathscr C\);
2. every global stationary law is a mixture of the class-uniform laws;
3. every global stationary law is invariant under each \(K_\tau\).

The last point also follows directly.  If \(g\) is a stationary density,
then

\[
0=\langle g,(I-K)g\rangle
=\binom n2^{-1}\sum_\tau
\|(I-K_\tau)g\|_2^2.
\]

Hence \(K_\tau g=g\) for every \(\tau\).  The invariant algebra is

\[
\boxed{
\ker(I-K)=\bigcap_\tau\operatorname{Ran}K_\tau.}
\tag{Y2.8}
\]

Its atoms are the communicating classes.  This is an exact algebraic
classification, but no more explicit nonlinear combinatorial description
of these atoms is currently proved.

Choosing the opposite side in every component gives \(\tau F\).
Transpositions generate \(S_n\), so

\[
\boxed{S_nF\subseteq\mathscr C(F).}
\tag{Y2.9}
\]

Every class is \(S_n\)-stable.  A class need not be a single coordinate
orbit.

Because \(K\) is an average of orthogonal projections, its spectrum lies in
\([0,1]\), and

\[
K^t\longrightarrow\Pi,
\]

where

\[
(\Pi h)(F)
=\frac1{|\mathscr C(F)|}
\sum_{G\in\mathscr C(F)}h(G).
\tag{Y2.10}
\]

Thus the long-time heat limit is exactly class averaging, with no
quantitative information yet about the value of that average.

## 4. First moments, class divisibility, and the variance gate

Let

\[
M=\frac{(n-1)!}{2}
\]

be the number of unoriented cyclic orders.

Since every class is \(S_n\)-stable and \(S_n\) is transitive on wreaths,
every wreath belongs to the same number of factors in \(\mathscr C\).
Double-counting pairs \((F,P)\) with \(P\in F\) gives

\[
\frac{|\mathscr C|B}{M}\in\mathbb Z.
\]

Since

\[
\frac MB=\frac{m!(m+1)!}{2},
\]

one obtains the exact class-size divisibility

\[
\boxed{
\frac{m!(m+1)!}{2}\mid|\mathscr C|.}
\tag{Y2.11}
\]

At depth \(q\), class invariance and transitivity on the
\(N_q\) targets give, for every fixed \(S\),

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\mu_q(F,S)
=\frac W{N_q}=a_q.}
\tag{Y2.12}
\]

Indeed, the expected load is independent of \(S\), and every factor has
exactly \(W\) pointed rank-\((m-q)\) occurrences.  The integral class total
also gives

\[
\boxed{
\frac{N_q}{\gcd(N_q,W)}\mid|\mathscr C|.}
\tag{Y2.13}
\]

This divisibility exactly clears the reduced denominator of
\(\theta_q\).  Class cardinality alone therefore creates no extra
denominator obstruction to the ordinary two-point integer floor; it does
not prove joint realizability of that floor.

Let

\[
Z_q=\mu_q(F,S),\qquad F\sim\pi_{\mathscr C}.
\]

For an integer-valued variable of mean \(c_q+\theta_q\),

\[
\mathbb E[(Z_q-c_q)(Z_q-c_q-1)]
=\operatorname{Var}Z_q-\theta_q(1-\theta_q).
\]

Summing over the \(N_q\) identically distributed targets gives

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}Q_q
=N_q\left(
\operatorname{Var}_{\pi_{\mathscr C}}Z_q
-\theta_q(1-\theta_q)
\right).}
\tag{Y2.14}
\]

Thus the desired stationary theorem is exactly a near-minimal
integer-variance statement.  Stationarity fixes the mean (Y2.12), but does
not yet control the excess variance in (Y2.14).

## 5. Exact class covariance and fixed-transposition projector identity

Let \(x_F\in\{0,1\}^M\) be the wreath-indicator vector.  Put

\[
p=\frac BM,\qquad
y_F=x_F-p\mathbf1,
\qquad
\Sigma_{\mathscr C}
=\mathbb E_{\pi_{\mathscr C}}y_Fy_F^{\mathsf T}.
\]

Coordinate invariance gives

\[
\mathbb E_{\pi_{\mathscr C}}x_F=p\mathbf1.
\]

Pointwise,

\[
\|y_F\|_2^2=B(1-p),
\]

and exact middle ownership gives

\[
A_my_F=0.
\]

Indeed, \(A_mx_F=\mathbf1\), while incidence counting gives
\(A_m\mathbf1=(M/B)\mathbf1\), so
\(A_m(p\mathbf1)=\mathbf1\).

Therefore

\[
\boxed{
\operatorname{Tr}\Sigma_{\mathscr C}=B(1-p),
\qquad
A_m\Sigma_{\mathscr C}=0,
\qquad
\Sigma_{\mathscr C}A_m^{\mathsf T}=0.}
\tag{Y2.15}
\]

For a fixed \(\tau\), let

\[
P_\tau=\frac{I+\tau}{2},
\qquad
z_i=\mathbf1_{\tau L_i}-\mathbf1_{L_i}.
\]

Here \(z_i=z_i(F,\tau)\) depends on the current factor and transposition.

For a uniform child in the intrinsic cell,

\[
y'=P_\tau y_F+\frac12\sum_i\varepsilon_i z_i,
\]

where the \(\varepsilon_i\) are independent fair signs.  Hence

\[
\mathbb E[y'y'^{\mathsf T}\mid F]
=P_\tau y_Fy_F^{\mathsf T}P_\tau
+\frac14\sum_i z_iz_i^{\mathsf T}.
\]

Separate \(K_\tau\)-stationarity gives

\[
\boxed{
\Sigma_{\mathscr C}
=P_\tau\Sigma_{\mathscr C}P_\tau
+\mathbb E_{\pi_{\mathscr C}}
\frac14\sum_i z_iz_i^{\mathsf T}.}
\tag{Y2.16}
\]

The covariance \(\Sigma_{\mathscr C}\) is \(S_n\)-equivariant, so it
commutes with \(P_\tau\).  Therefore

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}
\frac14\sum_i z_iz_i^{\mathsf T}
=(I-P_\tau)\Sigma_{\mathscr C}.}
\tag{Y2.17}
\]

There is also a fixed pointwise trace:

\[
\boxed{
\operatorname{Tr}\left(\frac14\sum_i z_iz_i^{\mathsf T}\right)
=\frac B2.}
\tag{Y2.18}
\]

Indeed, the two component sides are disjoint,
\(\|z_i\|_2^2=2|L_i|\), and \(\sum_i|L_i|=B\).

Let \(A_r\) be the wreath-to-rank-\(r\) cyclic-interval incidence map.
Then

\[
f_q=A_{m-q}y_F
\]

and

\[
\Gamma_{q,\mathscr C}
:=\mathbb E_{\pi_{\mathscr C}}f_qf_q^{\mathsf T}
=A_{m-q}\Sigma_{\mathscr C}A_{m-q}^{\mathsf T}.
\tag{Y2.19}
\]

The target Johnson module is multiplicity-free, so

\[
\Gamma_{q,\mathscr C}
=\sum_{j=2}^{m-q}a_{q,j}^{\mathscr C}E_{q,j},
\qquad a_{q,j}^{\mathscr C}\ge0,
\tag{Y2.20}
\]

where \(E_{q,j}\) is the degree-\(j\) Johnson projector.

Equations (Y2.15)--(Y2.20) are exact constraints on a class covariance.
The displayed constraints alone yield no bound here on the amplitudes
\(a_{q,j}^{\mathscr C}\) at the scale needed below; further exact-factor
feasibility could impose additional restrictions.

## 6. Exact heat identity

For component side \(L_i\), define its two depth-\(q\) side histograms

\[
u_{i,q}=A_{m-q}\mathbf1_{L_i},
\qquad
w_{i,q}=A_{m-q}\mathbf1_{\tau L_i}
=\tau u_{i,q},
\]

and put

\[
\Delta_{i,q}=u_{i,q}-w_{i,q}.
\]

For fixed \(\tau\), define

\[
A_{\tau,H}(F)
=\sum_{q\le H}\frac{\|f_q-\tau f_q\|_2^2}{c_q},
\tag{Y2.21}
\]

\[
N_{\tau,H}(F)
=\sum_i\sum_{q\le H}
\frac{\|\Delta_{i,q}\|_2^2}{c_q}.
\tag{Y2.22}
\]

The quantity \(N_{\tau,H}/4\) is the total fair conditional component
variance; \(N_{\tau,H}\) is the unscaled convention.

The fair child has midpoint

\[
\frac{f_q+\tau f_q}{2}
\]

and independent component fluctuations
\(\frac12\varepsilon_i\Delta_{i,q}\).  Orthogonality of the
\(\tau\)-invariant midpoint and the \(\tau\)-anti-invariant difference gives

\[
\boxed{
(K_\tau\mathcal Q_H)(F)-\mathcal Q_H(F)
=\frac14\left(N_{\tau,H}(F)-A_{\tau,H}(F)\right).}
\tag{Y2.23}
\]

For a stationary class, separate \(K_\tau\)-invariance yields

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}N_{\tau,H}
=\mathbb E_{\pi_{\mathscr C}}A_{\tau,H}
\quad\text{for every fixed }\tau.}
\tag{Y2.24}
\]

Now put

\[
D_H(F)=\sum_\tau A_{\tau,H}(F),
\qquad
R_H(F)=\sum_\tau N_{\tau,H}(F).
\tag{Y2.25}
\]

Then

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}R_H
=\mathbb E_{\pi_{\mathscr C}}D_H.}
\tag{Y2.26}
\]

This equality is the entire direct contribution of stationarity to the
aggregate energy ledger.

## 7. Corrected \(4(n-1)\) baseline

Fix \(r=m-q\).  In one wreath, exactly \(r\) cyclic \(r\)-intervals contain
a fixed coordinate \(x\).  Since \(F\) has \(B\) wreaths,

\[
\sum_{S\ni x}\mu_q(F,S)=rB=\frac{rW}{n}.
\tag{Y2.27}
\]

The constant profile has the same point margin:

\[
a_q\binom{n-1}{r-1}
=\frac W{N_q}\frac{rN_q}{n}
=\frac{rW}{n}.
\tag{Y2.28}
\]

Thus \(f_q\) has zero total and zero point margins.  Equivalently,

\[
f_q\in\bigoplus_{j\ge2}E_{q,j}.
\tag{Y2.29}
\]

For functions on the rank-\(r\) slice, the Johnson Laplacian has eigenvalue

\[
\lambda_j=j(n-j+1)
\]

on degree \(j\).  Since unordered transpositions are counted once,

\[
\sum_\tau\|f-\tau f\|_2^2
=2\langle f,L_{J(n,r)}f\rangle.
\]

Consequently

\[
\boxed{
\sum_\tau\|f_q-\tau f_q\|_2^2
=2\sum_{j\ge2}j(n-j+1)\|f_{q,j}\|_2^2
\ge4(n-1)\|f_q\|_2^2.}
\tag{Y2.30}
\]

The coefficient \(4(n-1)\) is sharp on the ambient degree-two
zero-point-margin module.  This does not assert exact-factor attainment.

Define the exact spectral surplus

\[
\Xi_H(F)
=2\sum_{q\le H}\frac1{c_q}
\sum_{j=3}^{m-q}(j-2)(n-j-1)\|f_{q,j}\|_2^2.
\tag{Y2.31}
\]

The factorization

\[
j(n-j+1)-2(n-1)=(j-2)(n-j-1)
\]

shows that \(\Xi_H(F)\ge0\) in the controlled ranks.  Equations
(Y2.4), (Y2.25), and (Y2.30) give the pointwise identity

\[
\boxed{
D_H(F)
=4(n-1)\bigl(\mathfrak B_H+\mathcal Q_H(F)\bigr)
+\Xi_H(F).}
\tag{Y2.32}
\]

Combining (Y2.26) and (Y2.32) proves the decisive stationary theorem.

### Theorem 7.1: stationary two-slack identity

For every communicating class \(\mathscr C\),

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}R_H-4(n-1)\mathfrak B_H
=4(n-1)\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
+\mathbb E_{\pi_{\mathscr C}}\Xi_H.}
\tag{Y2.33}
\]

Both terms on the right are nonnegative.

Put

\[
\Delta_{i,q,j}:=E_{q,j}\Delta_{i,q}.
\]

For one fixed transposition and \(2\le j\le m-q\), tracing
(Y2.17) on the multiplicity-one Johnson module gives

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}
\frac14\sum_i\|\Delta_{i,q,j}\|_2^2
=\kappa_j
\mathbb E_{\pi_{\mathscr C}}\|f_{q,j}\|_2^2,
\qquad
\kappa_j=\frac{j(n-j+1)}{n(n-1)}.}
\tag{Y2.34}
\]

In particular,

\[
\kappa_2=\frac2n.
\]

Summing (Y2.34) over the \(\binom n2\) transpositions and restoring the
factor four in the unscaled component noise gives exactly the coefficient
\(4(n-1)\) in (Y2.33).

The meaning of (Y2.34) is negative for the present route: stationary
component noise tracks the harmonic energy already selected by the class.
It does not bound that harmonic energy.

## 8. Why the stationary identity gives no Catalan-scale upper bound

The desired conclusion is

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_{H_A}
\le C_AH_A B.
\tag{Y2.35}
\]

A sufficient new estimate, by (Y2.33), would be

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}R_{H_A}
\le
4(n-1)\mathfrak B_{H_A}
+C_A'(n-1)H_AB.}
\tag{Y2.36}
\]

Since \(nB=W\), the allowed excess in (Y2.36) is

\[
O_A(H_AW)=O_A(W\sqrt m).
\tag{Y2.37}
\]

This estimate is not a consequence of stationarity.  Stationarity supplies
only the equality \( \mathbb ER_H=\mathbb ED_H\), and substituting
(Y2.32) gives (Y2.33) back.

Conversely, low floor energy alone does not imply (Y2.36), because the
degree-\(\ge3\) surplus \(\Xi_H\) can be large.

For scale, uniformly for \(q\le A\sqrt m\),

\[
a_q
=\exp\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right).
\]

Writing \(t=e^{x^2}\), the ordinary Riemann-sum argument gives

\[
\boxed{
\frac{\mathfrak B_{H_A}}{W\sqrt m}
\longrightarrow
\kappa_A
:=\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{\lfloor e^{x^2}\rfloor e^{x^2}}\,dx>0.}
\tag{Y2.38}
\]

Hence

\[
4(n-1)\mathfrak B_{H_A}
=\Theta_A(nW\sqrt m).
\tag{Y2.39}
\]

The excess allowed by (Y2.36) is only \(O_A(W\sqrt m)\), a relative
\(O(1/n)\) correction to the baseline.  The corrected
global-minimizer gate with an \(o(nW)\) excess gives only
\(\mathcal Q_H=o(W)\); it does not supply the sharper
\(O_A(H_AB)=O_A(W/\sqrt m)\) class mean requested here.

### Exact equality is impossible but gives no quantitative gap

For \(m\ge18\) and \(H\ge1\), equality

\[
\mathbb E_{\mathscr C}R_H=4(n-1)\mathfrak B_H
\]

cannot hold.  Equality in (Y2.33) would force
\(\mathcal Q_H=0\) and \(\Xi_H=0\) at every state in the class.  At
\(q=1\), the profile would be floor/ceiling balanced and its centered bonus
indicator would lie entirely in Johnson degree two.  The audited
first-shadow Boolean-\(E_2\) theorem excludes such a family for \(m\ge18\).

This is only strict inequality.  No uniform lower bound on the excess at
the \(O_A(W\sqrt m)\) scale follows from the Boolean theorem.

## 9. Scalar pair-covariance gate

Fix \(\tau\) and a moved target pair

\[
\{S,T\},\qquad T=\tau S\ne S.
\]

Inside one intrinsic \(\tau\)-cell, put

\[
\ell=\mu_q(S)+\mu_q(T).
\]

This pair sum is cell-invariant.  If \(d_i\) is the difference between the
two component-side contributions to \(S\) and \(T\), then conditional on the
cell,

\[
\mu_q(S)=\frac12\left(\ell+\sum_i\varepsilon_i d_i\right),
\qquad
\mu_q(T)=\frac12\left(\ell-\sum_i\varepsilon_i d_i\right).
\tag{Y2.40}
\]

The component signs are independent fair bits.  Taking the class law,
which weights cells by their sizes, gives the exact formulas

\[
\boxed{
\operatorname{Var}_{\mathscr C}\mu_q(S)
=\frac14\operatorname{Var}_{\mathscr C}\ell
+\frac14\mathbb E_{\mathscr C}\sum_i d_i^2,}
\tag{Y2.41}
\]

\[
\boxed{
\operatorname{Cov}_{\mathscr C}
\bigl(\mu_q(S),\mu_q(T)\bigr)
=\frac14\operatorname{Var}_{\mathscr C}\ell
-\frac14\mathbb E_{\mathscr C}\sum_i d_i^2.}
\tag{Y2.42}
\]

The two free quantities are:

1. variation of the pair-sum invariant between different \(\tau\)-cells;
2. component-bundling variance inside each cell.

The stationary identities above provide no upper bound on either quantity.
Equations (Y2.41)--(Y2.42) are the scalar form of the class-covariance
gate; additional exact-factor structure could still constrain them.

For one fixed \(\tau\), all pair sums and the corresponding component-square
data are genuine cell invariants.  They are not known to survive a switch
for another transposition.  Coordinate relabelling merely conjugates the
data from \(\tau\) to \(\sigma\tau\sigma^{-1}\).

## 10. A bounded-load projected stationary obstruction

This section constructs a rigorous obstruction to a stationarity-only
argument.  It is explicitly not an exact-factor construction.

Take infinitely many \(m\) for which

\[
n=2m+1
\]

is prime.  Put

\[
r=m-1,\qquad
N=N_1=\binom nr=\frac{m}{m+2}W,
\qquad
B=\frac Wn.
\]

For \(m\ge3\),

\[
c_1=1.
\]

Fix an \(n\)-cycle \(\rho\) on the coordinates.  Since \(n\) is prime,
every \(\rho\)-orbit on the proper nonempty \(r\)-subsets has size \(n\).
Every such orbit is point-regular: it contains each coordinate in exactly
\(r\) of its members.

The number of these orbits is

\[
\frac Nn=B\frac{m}{m+2}.
\]

For all sufficiently large \(m\), this is at least
\(\lceil B/2\rceil\).  Choose \(\lfloor B/2\rfloor\) distinct orbits and
give every set in them load \(2\).  If \(B\) is odd, choose one additional
orbit and give every set in it load \(1\).  Give all remaining sets load
\(0\).  Call the resulting load vector \(z\).

Then

\[
z(S)\in\{0,1,2\},
\]

\[
\sum_Sz(S)=nB=W,
\tag{Y2.43}
\]

and, for every coordinate \(x\),

\[
\sum_{S\ni x}z(S)=rB=\frac{rW}{n}.
\tag{Y2.44}
\]

Thus \(z\) has exactly the total and point margins forced on an
exact-factor first-shadow profile.  It also satisfies the elementary
extension-capacity condition: an \((m-1)\)-target has \(m+2\) middle
extensions and one wreath occurrence consumes two, while

\[
z(S)\le2\le\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

Only the zero cells contribute to the full floor energy, and each
contributes \(2\).  Therefore

\[
\begin{aligned}
Q_1(z)
&=2\left(N-n\left\lceil\frac B2\right\rceil\right)\\
&\ge W\frac{m-2}{m+2}-n.
\end{aligned}
\tag{Y2.45}
\]

Consequently

\[
\boxed{Q_1(z)\ge\frac W2}
\tag{Y2.46}
\]

for all sufficiently large members of this prime subsequence.

Now take the coordinate orbit

\[
\mathscr Z=S_nz
\]

as a formal state space, and define

\[
\widetilde K_\tau(v,\cdot)
=\frac12\delta_v+\frac12\delta_{\tau v}.
\tag{Y2.47}
\]

Let \(\widetilde K=\binom n2^{-1}\sum_\tau\widetilde K_\tau\).

No transposition fixes \(z\).  Indeed, \(z\) is \(\rho\)-invariant.  If it
were also fixed by a transposition \(\tau=(i,j)\), it would be fixed by the
group generated by \(\rho\) and \(\tau\).  The conjugates of \(\tau\) by
powers of \(\rho\) are the edge transpositions of the step-\((j-i)\)
circulant on \(\mathbb Z_n\).  Since \(n\) is prime, that graph is connected,
and its edge transpositions generate \(S_n\).  Hence \(z\) would be
\(S_n\)-invariant and therefore constant on the rank-\(r\) slice,
contradicting its construction.

Thus every \(\widetilde K_\tau\)-cell has exactly two states.  The orbit
\(\mathscr Z\) is one communicating class because transpositions generate
\(S_n\).  Its unique stationary law is uniform, every coordinate-invariant
energy (in particular \(Q_1\)) is constant on the class, and

\[
\mathbb E_{\mathscr Z}Q_1=Q_1(z)\ge\frac W2.
\]

Since

\[
H_AB=\frac{H_AW}{n},
\]

\[
\boxed{
\frac{\mathbb E_{\mathscr Z}Q_1}{H_AB}
\ge\frac n{2H_A}\longrightarrow\infty.}
\tag{Y2.48}
\]

Declare the pair \(\{v,\tau v\}\) to have one component, with side loads
\(v,\tau v\).  Then component noise equals coherent displacement
pointwise.  The model has:

- reversible pair-cell projections;
- one uniform stationary communicating class;
- \(S_n\)-invariance;
- nonnegative bounded integer loads;
- exact total and point margins;
- fixed-\(\tau\) pair-sum invariance;
- zero Johnson degrees \(0\) and \(1\);
- the corrected \(4(n-1)\) spectral ledger.

Moreover, choose any genuine exact factor \(F_0\) with first-shadow
histogram \(\mu_1(F_0)\).  Since

\[
z-\mu_1(F_0)\in\ker_{\mathbb Z}U_r,
\]

the audited rank-isolated integral selector theorem supplies a signed
\(\zeta\in\ker_{\mathbb Z}A_m\) whose first-shadow image is
\(z-\mu_1(F_0)\).  Hence \(x_{F_0}+\zeta\) is a signed exact-middle solution
with first-shadow \(z\).

What is missing is decisive: the signed solution is not known to be
nonnegative or Boolean, the load \(z\) is not known to decompose into one
exact family of cyclic owners, and the formal pair cells are not ownership
components of exact factors.

Therefore (Y2.48) is a rigorous projected obstruction, not an exact-factor
counterexample.  It proves that stationarity, bounded integer loads, exact
slice margins, signed exact-middle solvability, pair-cell covariance, and
the corrected spectrum still do not imply the target.

## 11. A complementary cyclic-owner obstruction

The preceding model has excellent slice properties but no cyclic-owner
realization.  A complementary model preserves cyclic chronology at every
depth but fails exact middle ownership.

Fix one unoriented cyclic order \(P\), and let

\[
h_{P,r}(S)=
\mathbf1_{\{S\text{ is a cyclic }r\text{-interval of }P\}}.
\]

Define, simultaneously at every lower rank,

\[
\widetilde\mu_q^P=B\,h_{P,m-q}.
\tag{Y2.49}
\]

This is the profile of \(B\) repeated copies of the same wreath.  It is
nonnegative and integral, has total \(nB=W\), has point margin
\((m-q)B\), and the lower shadows come from one genuine nested cyclic
deletion chronology.  Let the state space be the coordinate orbit of \(P\)
and use the two-state kernels

\[
\widetilde K_\tau(P,\cdot)
=\frac12\delta_P+\frac12\delta_{\tau P}.
\]

No transposition stabilizes \(P\), so this is again one reversible
communicating class with one formal component per transposition.  Its energy
is coordinate-invariant.  Directly,

\[
\left\|
\widetilde\mu_q^P-\frac W{N_q}\mathbf1
\right\|_2^2
=\frac{W^2}{n}-\frac{W^2}{N_q}.
\tag{Y2.50}
\]

At \(q=1\), the floor term is only \(O(W)\), while \(W^2/n\) is larger by
the Catalan factor.  Thus

\[
\widetilde Q_1
=\left(1+o(1)\right)\frac{W^2}{n}.
\tag{Y2.51}
\]

This model satisfies the cyclic-row and cross-depth nesting identities but
uses one wreath with multiplicity \(B\) and fails exact middle coverage.
Together with Section 10, it proves two complementary facts:

1. cyclic nesting without exact middle ownership is insufficient;
2. bounded integer slice loads and signed exact-middle solvability without
   nonnegative common owners are insufficient.

Any stationary proof must use the full Boolean exact-cover geometry, not
only either projection.

## 12. Actual exact-factor obstruction: the rigid-orbit theorem

Call an exact factor \(F\) transposition-rigid if the ownership overlay of
\(F\) with \(\tau F\) is connected for every coordinate transposition
\(\tau\).

### Theorem 12.1

If \(F\) is transposition-rigid, then its coordinate orbit \(S_nF\) is
exactly one communicating class of the true chain.

### Proof

For every \(\sigma\in S_n\), the overlay of \(\sigma F\) with
\(\tau\sigma F\) is the \(\sigma\)-image of the overlay of \(F\) with

\[
\sigma^{-1}\tau\sigma F.
\]

The conjugate is a transposition, so the overlay is connected.  Hence the
\(\tau\)-cell at \(\sigma F\) is exactly

\[
\{\sigma F,\tau\sigma F\}.
\]

Every heat move from the coordinate orbit stays in it.  Conversely,
transposition words reach every coordinate image, so the orbit is one
class.  \(\square\)

Since \(\mathcal Q_H\) is coordinate-invariant,

\[
\boxed{
\mathbb E_{\pi_{S_nF}}\mathcal Q_H
=\mathcal Q_H(F).}
\tag{Y2.52}
\]

Thus a sequence of transposition-rigid exact factors with

\[
\mathcal Q_{H_A}(F_m)
\gg H_A\operatorname{Cat}_m
\]

would be a genuine high-energy stationary class and would refute every-class
stationary contraction.  Its existence is unproved.

Even such a high class would not refute the weaker selection statement that
some other class has low mean.  To refute that statement one must prove that
every class is high, or prove irreducibility and a high global-uniform mean.
Neither is known.

## 13. Invariant audit

The exact full invariant algebra is (Y2.8), but no useful explicit
high-energy atom is currently known.

The natural candidates do not close the problem.

1. Fixed-\(\tau\) pair sums and component numbers are proved invariant only
   inside one \(\tau\)-cell; they are not proved full-chain invariants.
2. Coordinate relabelling conjugates fixed-\(\tau\) data rather than fixing
   it.
3. Every additive or modular lower-shadow invariant which annihilates the
   unrestricted signed middle-preserving lattice factors through the fixed
   point margins.  This removes signed index obstructions, not nonlinear or
   support-feasible class invariants.
4. The class divisibilities (Y2.11)--(Y2.13) exactly accommodate the ordinary
   floor proportions and create no extra variance.
5. The known cyclic-order parity candidate is not invariant under all legal
   component switches.

Thus no unconditional exact class invariant forces
\(\mathbb E_{\mathscr C}\mathcal Q_H\) above the target scale.

## 14. Poisson dual and the exact remaining stationary lemma

Put

\[
\Theta_H
=\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H.
\]

Since the stationary laws are exactly mixtures of class-uniform laws,

\[
\Theta_H
=\inf_{\pi K=\pi}\mathbb E_\pi\mathcal Q_H.
\]

For every real function \(h\) on the finite exact-factor state space,
stationarity gives

\[
\min_F\left[\mathcal Q_H(F)+(I-K)h(F)\right]
\le\Theta_H.
\]

Conversely, on each class solve the finite Poisson equation

\[
(I-K)h
=\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H-\mathcal Q_H.
\]

The right side has class mean zero and therefore lies in the range of
\(I-K\).  Solving separately on all classes gives equality.  Hence

\[
\boxed{
\Theta_H
=\sup_h\min_F
\left[\mathcal Q_H(F)+(I-K)h(F)\right].}
\tag{Y2.53}
\]

Adding an unrestricted coboundary therefore does not soften the stationary
problem; it is exactly the same class-selection problem.

The remaining statement for this lane is:

> **Stationary covariance selection \(\mathrm{SCOV}_A\) — UNPROVED.**
> For every fixed \(A>0\), there is a communicating class
> \(\mathscr C_m\) of exact middle wreath factors and a constant \(C_A\)
> such that
> \[
> \mathbb E_{\pi_{\mathscr C_m}}\mathcal Q_{H_A}
> \le C_AH_A\operatorname{Cat}_m
> \]
> for all sufficiently large \(m\).

Equivalently, by (Y2.14), one needs

\[
\sum_{q\le H_A}\frac{N_q}{c_q}
\left[
\operatorname{Var}_{\pi_{\mathscr C_m}}Z_q
-\theta_q(1-\theta_q)
\right]
\le C_AH_AB.
\]

Equivalently, in wreath covariance notation,

\[
\operatorname{Tr}(T_A\Sigma_{\mathscr C_m})
-\mathfrak B_{H_A}
\le C_AH_AB,
\]

where

\[
T_A
=\sum_{q\le H_A}
\frac{A_{m-q}^{\mathsf T}A_{m-q}}{c_q}.
\]

This statement is sufficient for fixed-window unlabelled overload and hence
for MWB after diagonalization.  It is not known necessary for MWB, and it
does not imply the stronger labelled common-owner synchronization theorem.

## 15. Final theorem ledger

### Proved

1. Intrinsic \(\tau\)-cells contain exactly \(2^k\) distinct exact factors.
2. \(K_\tau\) is an orthogonal projection.
3. Communicating classes are unions of full cells.
4. Every class has a unique uniform stationary law, invariant under every
   \(K_\tau\) separately.
5. Every stationary law is a mixture of class-uniform laws.
6. Every class is \(S_n\)-stable and satisfies the exact first-moment and
   divisibility formulas.
7. Class mean floor energy is exactly excess integer variance.
8. The wreath covariance/projector identities and fixed indicator-noise
   trace are exact.
9. The correct all-transposition spectral coefficient is \(4(n-1)\).
10. Every class obeys the stationary two-slack identity (Y2.33).
11. Stationarity supplies noise equals Dirichlet energy, not an upper bound.
12. The bounded-load and repeated-wreath orbit models rigorously obstruct
    deductions using only their respective explicitly listed relaxations.
13. The rigid-orbit theorem is exact under its stated hypothesis.
14. The Poisson dual (Y2.53) is exact.

### Unproved

1. \(\mathrm{SCOV}_A\): existence of one low-mean exact communicating class.
2. Any unconditional high-energy exact communicating class.
3. Any useful nonlinear full-class invariant.
4. Existence of a high-energy transposition-rigid exact factor.
5. Any \(O_A(H_AW)\)-accurate upper bound above the corrected
   \(4(n-1)\mathfrak B_{H_A}\) component-noise baseline.
6. Any implication from stationarity to labelled common-owner
   synchronization.

## Final conclusion

The corrected \(4(n-1)\) baseline does not rescue the stationary route.  It
turns the classwise calculation into the exact identity (Y2.33):
stationarity cancels the heat drift and leaves the class covariance
amplitude free.  The rigorous projected countermodels show that
bounded integer slice margins with signed solvability, and cyclic chronology
without middle exactness, are separately insufficient.  Neither model
combines all of these properties, and neither has the full nonnegative
exact-middle ownership constraint.

No theorem presently proves that some exact communicating class has mean
\(O_A(H_A\operatorname{Cat}_m)\), and no unconditional exact-factor class
obstruction is known.  The lane ends at \(\mathrm{SCOV}_A\), an exact
class-covariance/pair-correlation selection theorem.
