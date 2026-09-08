# Multi-seed exact overlays: Gaussian frozen support, orbit transport, and collision floor

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad t={W\over n}=\operatorname{Cat}_m.
\]

This note treats a genuinely multi-seed physical overlay.  Its owner
components are disjoint, and each component has a finite catalogue of
complete integral resolutions of exactly the same middle-owner set.  One
may choose one resolution independently in every component.  The
resolutions need not be coordinate relabelings of one another, and their
trades are allowed to change every previously considered permutation-orbit
mass.

The following exact obstructions survive that freedom.

1.  Let \(\mathcal A_q\) be the union of the rank-\((m-q)\) target
    coordinates on which at least one component resolution changes its
    load.  The complete floor defect on the complement of
    \(\mathcal A_q\) is frozen at every state of the overlay.  In
    particular,

    \[
    \boxed{
    \mathcal Q_I(F_x)\ge
    \sum_{q\in I}{1\over c_q}
    \sum_{T\notin\mathcal A_q}
    (\bar\mu_q(T)-c_q)(\bar\mu_q(T)-c_q-1).}
    \tag{0.1}
    \]

    This is a statewise statement, not an average-heat statement.

2.  Suppose each component has at most \(R\) equiprobable resolutions.
    If a target is changed nontrivially by two different components, then
    product resampling pays at least \(2/R^2\) expected unweighted
    floor defect at that target.  Therefore

    \[
    \boxed{
    \mathbb E\mathcal Q_I(F_X)
       \ge {2\over R^2}
       \sum_{q\in I}{|\mathcal C_q|\over c_q},}
    \tag{0.2}
    \]

    where \(\mathcal C_q\) is the set of targets changed by at least two
    components.  This is the exact nonlinear restitution missed by a raw
    Gram calculation.

There is also a dense quotient obstruction.  For any partition into
target cells \(O\), put

\[
 D_O=\sum_{T\in O}(\mu(T)-c).
\]

If \(D_O=a|O|+\rho\), \(0\le\rho<|O|\), then the exact minimum cell floor
at that quotient mass is

\[
 G_{|O|}(D_O)=|O|a(a-1)+2a\rho
 \ge2\operatorname{dist}(D_O,[0,|O|]).
\]

The attainable vector \((D_O)_O\) is exactly the Minkowski sum of the
component orbit-mass catalogues.  Therefore a component library whose
total quotient transport capacity is smaller than the initial distance to
the box \(0\le D_O\le|O|\) leaves a positive deterministic floor defect,
even when every literal target is movable.

The complete product identity is

\[
 \mathbb E\mathcal Q_I
 =\|\bar\mu-\lambda\mathbf1\|_I^2-B_I+V_I^{\rm comp}.
\]

On the Gaussian annulus, \(B_I\sim\kappa_{a,b}W\sqrt m\) with an explicit
positive integral \(\kappa_{a,b}\).  Hence even an exactly uniform
barycenter needs the component variance to equal \(B_I\) to additive
accuracy \(o(W)\); an \(O(W\sqrt m)\) estimate is not a
baseline-corrected contraction theorem.

For the physical bounded-collar class the first obstruction is
quantitative.  Suppose the rows have a common rooted indexing and every
one of the at most \(R\) alternatives at a root differs from a reference
row only inside a cyclic block of at most \(k\) positions.  If

\[
 I=\{q:\lceil a\sqrt m\rceil\le q\le\lfloor b\sqrt m\rfloor\},
 \qquad 0\le a<b<\infty,
\]

then

\[
 \boxed{
 \sum_{q\in I}|\mathcal A_q|
 \le 4(R-1)(k-1)t|I|
 =\bigl(2(b-a)+o_{a,b}(1)\bigr)
   {(R-1)(k-1)\over\sqrt m}\,W.}
 \tag{0.3}
\]

Consequently, if \(Rk=o(\sqrt m)\), such a multi-seed overlay can alter
only \(o(W)\) target-depth cells in the whole annulus.  If one seed has
\(\Omega(W)\) cells whose loads are not one of the two floor-optimal
values \(c_q,c_q+1\), every child still has \(\Omega(W)\) aggregate
floor defect.  Thus bounded-collar multi-seed overlays cannot establish
\(o(W)\) by repairing a diffuse Gaussian-annulus defect, even when their
trades change orbit masses.

The theorem does not obstruct a growing carrier with
\(Rk=\Omega(\sqrt m)\), a factor already floor-optimal outside \(o(W)\)
cells, or a strongly correlated global selection which avoids the product
collision cost.  Those are the exact surviving alternatives.

---

## 1. General physical multi-seed overlay

At depth \(q\), put

\[
 r_q=m-q,\qquad \mathcal T_q=\binom{[n]}{r_q},\qquad
 N_q=|\mathcal T_q|,
\]

\[
 \lambda_q={W\over N_q}=c_q+\theta_q,\qquad
 c_q=\lfloor\lambda_q\rfloor,\quad 0\le\theta_q<1.
\tag{1.1}
\]

Let \(\mathscr K\) be a collection of pairwise owner-disjoint physical
components.  Component \(K\) has a finite nonempty resolution catalogue
\(\mathscr R_K\).  Every \(a\in\mathscr R_K\) is a collection of complete
cyclic rows which covers exactly the same middle-owner set \(\Omega_K\),
once each.  Thus choosing one \(a_K\in\mathscr R_K\) for every \(K\)
produces an exact middle wreath factor \(F_x\), where

\[
 x=(a_K)_{K\in\mathscr K}\in
 \prod_{K\in\mathscr K}\mathscr R_K.
\]

This includes an ordinary two-factor ownership overlay, an \(R\)-shore
overlay of \(R\) unrelated factors, and a component with additional
internal exact resolutions.

Let

\[
 u_{K,a,q}\in\mathbb Z_{\ge0}^{\mathcal T_q}
\tag{1.2}
\]

be the full rank-\(r_q\) cyclic-window load supplied by resolution \(a\)
of component \(K\).  Then

\[
 \mu_q^x=\sum_Ku_{K,a_K,q}.
\tag{1.3}
\]

If every resolution of \(K\) has \(s_K\) rows, then for all \(a,b\)

\[
 \sum_T(u_{K,a,q}(T)-u_{K,b,q}(T))=0.
\tag{1.4}
\]

Also, for every coordinate \(i\),

\[
 \sum_{T\ni i}(u_{K,a,q}(T)-u_{K,b,q}(T))=0.
\tag{1.5}
\]

Indeed, one cyclic row has \(n\) rank-\(r_q\) windows and every coordinate
belongs to exactly \(r_q\) of them.  Hence all component effects have zero
total and zero point margins.  No further orbit-mass conservation is
assumed or used below.

For a set of depths \(I\), define the exact floor-corrected energy

\[
 \mathcal Q_I(F_x)=
 \sum_{q\in I}{1\over c_q}
 \left(
  \|\mu_q^x-\lambda_q\mathbf1\|_2^2
  -N_q\theta_q(1-\theta_q)
 \right).
\tag{1.6}
\]

### Lemma 1.1 (exact adjacent-integer identity)

For every exact factor and every depth,

\[
 \boxed{
 \|\mu_q-\lambda_q\mathbf1\|_2^2
 -N_q\theta_q(1-\theta_q)
 =\sum_{T\in\mathcal T_q}
 (\mu_q(T)-c_q)(\mu_q(T)-c_q-1).}
\tag{1.7}
\]

Every summand on the right is a nonnegative even integer.  It vanishes
exactly when \(\mu_q(T)\in\{c_q,c_q+1\}\).

#### Proof

Write \(y_T=\mu_q(T)-c_q\).  Exactness gives

\[
 \sum_Ty_T=W-N_qc_q=N_q\theta_q.
\]

Therefore

\[
\begin{aligned}
 \sum_T(\mu_q(T)-\lambda_q)^2
  -N_q\theta_q(1-\theta_q)
 &=\sum_T(y_T-\theta_q)^2
   -N_q\theta_q(1-\theta_q)\\
 &=\sum_Ty_T^2-N_q\theta_q\\
 &=\sum_Ty_T(y_T-1).
\end{aligned}
\]

For integral \(y_T\), the product of two consecutive integers is
nonnegative and even. \(\square\)

---

## 2. The statewise frozen-support theorem

Choose an arbitrary reference resolution \(a_K^0\in\mathscr R_K\).  Put

\[
 \mathcal A_{K,q}
 =\left\{T:\{u_{K,a,q}(T):a\in\mathscr R_K\}
                 \text{ is not a singleton}\right\},
\]

\[
 \mathcal A_q=\bigcup_K\mathcal A_{K,q}.
\tag{2.1}
\]

For \(T\notin\mathcal A_q\), its common load is denoted
\(\bar\mu_q(T)\); it is independent of every component choice.

### Theorem 2.1 (frozen floor defect)

Every state \(x\) of the complete multi-seed product satisfies (0.1),
namely

\[
 \mathcal Q_I(F_x)\ge
 \sum_{q\in I}{1\over c_q}
 \sum_{T\notin\mathcal A_q}
 (\bar\mu_q(T)-c_q)(\bar\mu_q(T)-c_q-1).
\tag{2.2}
\]

In particular, if \(\mathcal B_q\) is the set of frozen targets whose
common load is not in \(\{c_q,c_q+1\}\), then

\[
 \boxed{
 \mathcal Q_I(F_x)\ge
 2\sum_{q\in I}{|\mathcal B_q|\over c_q}.}
\tag{2.3}
\]

#### Proof

For a frozen target the indicated summand in Lemma 1.1 is the same in
every state.  All omitted summands are nonnegative.  This proves (2.2).
If a summand is nonzero, it is at least two, proving (2.3). \(\square\)

There is an accompanying affine form.  Give

\[
 \mathscr H_I=\bigoplus_{q\in I}\mathbb R^{\mathcal T_q}
\]

the weighted norm \(\|z\|_I^2=\sum_{q\in I}c_q^{-1}\|z_q\|_2^2\), and
let

\[
 D=\operatorname{span}\{u_{K,a}-u_{K,a_K^0}:
                         K\in\mathscr K, a\in\mathscr R_K\}.
\tag{2.4}
\]

If \(f^x=\mu^x-\lambda\mathbf1\), then

\[
 \boxed{P_{D^\perp}f^x=P_{D^\perp}f^0}
 \tag{2.5}
\]

for every state, and consequently

\[
 \boxed{
 \mathcal Q_I(F_x)\ge
 \|P_{D^\perp}f^0\|_I^2-B_I,
 \qquad
 B_I=\sum_{q\in I}{N_q\theta_q(1-\theta_q)\over c_q}.}
\tag{2.6}
\]

Equation (2.5) follows because every state displacement belongs to \(D\);
(2.6) follows by orthogonal Pythagoras.  Unlike (2.2), the right side of
(2.6) can be negative.  Formula (2.2) is the sharper nonlinear statement
when the literal active support is sparse.

Neither theorem requires a component effect to preserve the mass on an
orbit of any coordinate permutation.  An effect may transfer mass between
all such orbits; only the coordinates on which its literal load changes
are charged.

---

## 2A. Exact orbit-cell quotient floor and transport capacity

The literal-support theorem is strongest for sparse edits.  There is a
second deterministic obstruction which remains nontrivial when every
target is active.  Fix a depth \(q\) and let \(\mathscr O_q\) be an
arbitrary partition of \(\mathcal T_q\) into nonempty cells.  The cells may,
but need not, be target orbits of a permutation group.

For \(O\in\mathscr O_q\), write \(r_O=|O|\) and define its excess above
the lower floor by

\[
 D_O(\mu)=\sum_{T\in O}(\mu(T)-c_q).
\tag{2A.1}
\]

For an integer \(D\) and a positive integer \(r\), write uniquely

\[
 D=ar+\rho,\qquad a\in\mathbb Z,\quad0\le\rho<r,
\tag{2A.2}
\]

and put

\[
 \boxed{G_r(D)=ra(a-1)+2a\rho.}
\tag{2A.3}
\]

### Theorem 2A.1 (exact quotient-cell floor)

For every feasible excess \(D\ge-c_qr_O\), among all nonnegative integral
cell loads \((\mu(T))_{T\in O}\) with prescribed excess \(D_O=D\), the
minimum of the cell floor polynomial is

\[
 \boxed{
 \min\sum_{T\in O}
  (\mu(T)-c_q)(\mu(T)-c_q-1)=G_{r_O}(D).}
\tag{2A.4}
\]

Consequently every exact factor satisfies

\[
 \boxed{
 Q_q(F):=\sum_{T\in\mathcal T_q}
 (\mu_q(T)-c_q)(\mu_q(T)-c_q-1)
 \ge\sum_{O\in\mathscr O_q}G_{r_O}(D_O).}
\tag{2A.5}
\]

Moreover,

\[
 \boxed{
 G_r(D)\ge2\operatorname{dist}(D,[0,r]),}
\tag{2A.6}
\]

and therefore

\[
 \boxed{
 Q_q(F)\ge
 2\sum_{O\in\mathscr O_q}
   \operatorname{dist}(D_O,[0,r_O]).}
\tag{2A.7}
\]

Here distance is ordinary absolute distance on \(\mathbb R\).

#### Proof

Put \(y_T=\mu(T)-c_q\), so \(y_T\in\mathbb Z\),
\(y_T\ge-c_q\), and \(\sum_{T\in O}y_T=D\).  If
\(y_S-y_T\ge2\), replacing the pair \((y_S,y_T)\) by
\((y_S-1,y_T+1)\) changes the objective by

\[
 (y_S-1)(y_S-2)+(y_T+1)y_T
 -y_S(y_S-1)-y_T(y_T-1)
 =-2(y_S-y_T-1)<0.
\]

Thus every minimizer has all entries differing by at most one.  They are
therefore \(a\) on \(r-\rho\) coordinates and \(a+1\) on \(\rho\)
coordinates.  Since actual nonnegative loads imply \(D\ge-c_qr\), one
has \(a\ge-c_q\), so this balanced vector respects the lower bound.
Its objective is

\[
 (r-\rho)a(a-1)+\rho(a+1)a
 =ra(a-1)+2a\rho,
\]

proving (2A.4).  Sum over the cells to get (2A.5).

It remains to prove (2A.6).  If \(0\le D\le r\), then the balanced
entries are zeros and ones, so both sides vanish.  If \(D<0\), then

\[
 G_r(D)-2(-D)
 =(a+1)(ra+2\rho)\ge0.
\]

For \(a=-1\) this is zero; for \(a\le-2\), both factors are negative,
because \(ra+2\rho\le-2\).  If \(D>r\), then

\[
 G_r(D)-2(D-r)
 =(a-1)(r(a-2)+2\rho)\ge0.
\]

For \(a=1\) this is zero; for \(a\ge2\), both factors are nonnegative.
This proves (2A.6), and summation proves (2A.7). \(\square\)

The formula is exact for the relaxation in which mass may be redistributed
freely inside every quotient cell.  The physical component restrictions
can only raise the minimum.

### Exact attainable component orbit masses

For a component resolution define its quotient mass vector

\[
 M_{K,a,q}=
 \left(\sum_{T\in O}u_{K,a,q}(T)\right)_{O\in\mathscr O_q}
 \in\mathbb Z_{\ge0}^{\mathscr O_q},
\tag{2A.8}
\]

and let

\[
 \mathfrak M_{K,q}=\{M_{K,a,q}:a\in\mathscr R_K\}.
\]

With \(\mathbf r_q=(r_O)_{O\in\mathscr O_q}\), the exact set of
attainable quotient excess vectors is the Minkowski sum

\[
 \boxed{
 \mathfrak D_{q,\mathscr O}
 =-c_q\mathbf r_q+\sum_{K}^{\rm Mink}\mathfrak M_{K,q}.}
\tag{2A.9}
\]

Indeed, (1.3) and (2A.1) give this identity coordinate by coordinate, and
every independent component choice realizes the corresponding summand.
It follows that

\[
 \boxed{
 \min_x Q_q(F_x)
 \ge
 \min_{D\in\mathfrak D_{q,\mathscr O}}
 \sum_{O\in\mathscr O_q}G_{r_O}(D_O).}
\tag{2A.10}
\]

The same component resolution must be used at every depth.  To retain
that coupling exactly, define

\[
 \mathfrak M_{K,I}
 =\{(M_{K,a,q})_{q\in I}:a\in\mathscr R_K\}
\]

and

\[
 \mathfrak D_{I,\mathscr O}
 =(-c_q\mathbf r_q)_{q\in I}
   +\sum_K^{\rm Mink}\mathfrak M_{K,I}.
\tag{2A.11}
\]

Then the exact joint quotient obstruction is

\[
 \boxed{
 \min_x\mathcal Q_I(F_x)
 \ge
 \min_{D\in\mathfrak D_{I,\mathscr O}}
 \sum_{q\in I}{1\over c_q}
 \sum_{O\in\mathscr O_q}G_{r_O}(D_{q,O}).}
\tag{2A.12}
\]

This is a finite integral optimization statement, not a fractional or
independent-heat bound.  It records all componentwise coupling between
orbit-mass transports and all depths.

There is a simpler coordinate-interval certificate.  Put

\[
 \ell_{K,O}=\min_a M_{K,a,q}(O),\qquad
 u_{K,O}=\max_a M_{K,a,q}(O),
\]

\[
 L_O=-c_qr_O+\sum_K\ell_{K,O},\qquad
 U_O=-c_qr_O+\sum_Ku_{K,O}.
\tag{2A.13}
\]

Every attainable \(D_O\) belongs to \([L_O,U_O]\).  Hence

\[
 \boxed{
 Q_q(F_x)\ge
 2\sum_{O\in\mathscr O_q}
 \operatorname{dist}([L_O,U_O],[0,r_O])}
\tag{2A.14}
\]

for every state.  This interval relaxation discards the coupling between
different cells; (2A.10)--(2A.12) retain it.

### The deterministic transport-capacity obstruction

Fix a reference state \(x^0=(a_K^0)_K\), with quotient excess vector
\(D^0\).  Define

\[
 \Phi_q(D)=\sum_{O\in\mathscr O_q}
             \operatorname{dist}(D_O,[0,r_O])
\tag{2A.15}
\]

and the maximum physical component transport capacity

\[
 \boxed{
 \operatorname{TC}_{q,\mathscr O}(x^0)
 ={1\over2}\sum_K\max_{a\in\mathscr R_K}
 \|M_{K,a,q}-M_{K,a_K^0,q}\|_1.}
\tag{2A.16}
\]

The factor \(1/2\) has a literal meaning: both quotient mass vectors have
the same total, so half their \(L^1\) difference is the number of
occurrence units transported between quotient cells.

### Theorem 2A.2 (dense orbit-transport no-go)

Every deterministic component state satisfies

\[
 \boxed{
 Q_q(F_x)\ge
 2\left(
  \Phi_q(D^0)-2\operatorname{TC}_{q,\mathscr O}(x^0)
 \right)_+.}
\tag{2A.17}
\]

Consequently, through a common depth window,

\[
 \boxed{
 \mathcal Q_I(F_x)\ge
 2\sum_{q\in I}{1\over c_q}
 \left(
  \Phi_q(D^{0,q})-2\operatorname{TC}_{q,\mathscr O_q}(x^0)
 \right)_+.}
\tag{2A.18}
\]

#### Proof

Distance to the box
\(\prod_O[0,r_O]\) in \(L^1\) is exactly \(\Phi_q\), and distance to a
fixed closed set is one-Lipschitz.  Thus

\[
 \Phi_q(D^x)\ge
 \Phi_q(D^0)-\|D^x-D^0\|_1.
\]

The Minkowski representation gives

\[
\begin{aligned}
 \|D^x-D^0\|_1
 &\le\sum_K
 \|M_{K,a_K,q}-M_{K,a_K^0,q}\|_1\\
 &\le2\operatorname{TC}_{q,\mathscr O}(x^0).
\end{aligned}
\]

Apply (2A.7) and take the positive part to prove (2A.17).  Weight and sum
over \(q\) to obtain (2A.18). \(\square\)

Unlike Theorem 2.1, Theorem 2A.2 permits \(\mathcal A_q=\mathcal T_q\):
every literal target may move.  What it forbids is insufficient total
component capacity to transport the quotient excess vector into the
floor-optimal box

\[
 0\le D_O\le|O|\qquad(O\in\mathscr O_q).
\]

On the fixed Gaussian annulus, (5.5) below gives \(c_q\le C_b\).  Hence
for any chosen sequence of partitions, a necessary condition for one
component child to have \(\mathcal Q_I=o(W)\) is

\[
 \boxed{
 \sum_{q\in I}\Phi_q(D^{x,q})=o(W).}
\tag{2A.19}
\]

In particular, if

\[
 \sum_{q\in I}
 \left(
  \Phi_q(D^{0,q})-2\operatorname{TC}_{q,\mathscr O_q}(x^0)
 \right)_+\ge\varepsilon W,
\tag{2A.20}
\]

then every child satisfies

\[
 \boxed{\mathcal Q_I(F_x)\ge {2\varepsilon\over C_b}W.}
\tag{2A.21}
\]

This is the requested dense orbit-changing obstruction.

---

## 3. Exact collision floor for product component heat

Now choose independently and uniformly

\[
 X_K\in\mathscr R_K,
\]

and suppose \(|\mathscr R_K|\le R\).  Define

\[
 d_q(T)=\#\{K:T\in\mathcal A_{K,q}\},\qquad
 \mathcal C_q=\{T:d_q(T)\ge2\}.
\tag{3.1}
\]

For later comparison with a heat/variance proof, put

\[
 \bar u_K={1\over|\mathscr R_K|}
              \sum_{a\in\mathscr R_K}u_{K,a},
 \qquad
 \bar\mu=\sum_K\bar u_K,
\]

and

\[
 V_I^{\rm comp}
 =\sum_K{1\over|\mathscr R_K|}
       \sum_{a\in\mathscr R_K}\|u_{K,a}-\bar u_K\|_I^2.
\tag{3.1a}
\]

### Proposition 3.0 (exact multi-seed baseline identity)

Independent product resampling has

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_X)
 =\|\bar\mu-\lambda\mathbf1\|_I^2-B_I
  +V_I^{\rm comp}.}
\tag{3.1b}
\]

In particular, even if the multi-seed barycenter is exactly uniform,
\(\bar\mu_q=\lambda_q\mathbf1\) at every depth, the output expectation is

\[
 \boxed{\mathbb E\mathcal Q_I(F_X)=V_I^{\rm comp}-B_I\ge0.}
\tag{3.1c}
\]

Thus orbit-mass mixing of the barycenter removes only the first term.  A
baseline-corrected contraction also has to prove
\(V_I^{\rm comp}=B_I+o(W)\), not merely an uncorrected variance upper
bound of order \(B_I\).

#### Proof

The independent centered component variables
\(u_{K,X_K}-\bar u_K\) have mean zero, so all cross-component inner
products vanish after expectation.  The Hilbert-space mean-square identity
gives

\[
 \mathbb E\|\mu^X-\lambda\mathbf1\|_I^2
 =\|\bar\mu-\lambda\mathbf1\|_I^2+V_I^{\rm comp}.
\]

Subtract \(B_I\).  Nonnegativity in (3.1c) also follows independently
from Lemma 1.1. \(\square\)

### Theorem 3.1 (two-component collision restitution)

The product law obeys the exact lower bound (0.2):

\[
 \mathbb E\mathcal Q_I(F_X)
 \ge {2\over R^2}\sum_{q\in I}{|\mathcal C_q|\over c_q}.
\tag{3.2}
\]

#### Proof

Fix \(q\) and \(T\in\mathcal C_q\).  Choose two distinct components
\(K,L\) which are nonconstant at \(T\), and condition on all component
choices except \(X_K,X_L\).  Their two integer contributions have minima
and maxima

\[
 a_-<a_+,\qquad b_-<b_+.
\]

The two endpoint sums differ by at least two:

\[
 (a_++b_+)-(a_-+b_-)\ge2.
\tag{3.3}
\]

After adding the conditioned integral contribution of the other
components, these two possible total loads still differ by at least two.
The zero set of

\[
 \psi_c(y)=(y-c)(y-c-1),\qquad y\in\mathbb Z,
\]

is the two-point set \(\{c,c+1\}\), of diameter one.  Hence at least one
of the two endpoint loads has \(\psi_{c_q}\ge2\).  The corresponding pair
of endpoint choices has conditional probability at least

\[
 {1\over|\mathscr R_K||\mathscr R_L|}\ge {1\over R^2}.
\]

Thus

\[
 \mathbb E\bigl[\psi_{c_q}(\mu_q^X(T))
                  \mid(X_J)_{J\ne K,L}\bigr]\ge {2\over R^2}.
\]

Remove the conditioning, sum over \(T\in\mathcal C_q\), insert the
weights \(1/c_q\), and use Lemma 1.1. \(\square\)

For a fair binary overlay, \(R=2\), so every doubly active target costs at
least \(1/2\) in expected unweighted floor defect.  This conclusion does
not depend on the coherent endpoint separation or on a Johnson-harmonic
decomposition.  It is a literal adjacent-integer collision cost.

The theorem is an averaging obstruction, not a deterministic discrepancy
lower bound.  A correlated global choice may avoid the product law's
cost.  It shows that independent multi-seed component heat can have
\(o(W)\) expected annular floor defect only if

\[
 \sum_{q\in I}{|\mathcal C_q|\over c_q}=o(R^2W).
\tag{3.4}
\]

Thus a successful independent atlas must be essentially collision-free at
the target-depth level when \(R=O(1)\).

---

## 4. Physical bounded-collar overlays

Assume now that every component is rooted: the same root labels occur in
each of its resolutions, one row per root.  Altogether there are
\(t=W/n\) roots.  Fix a reference row at every root.

### Lemma 4.1 (one cyclic collar)

Let two cyclic orders of \([n]\) agree outside a cyclic interval of \(k\)
positions and contain the same coordinates inside that interval.  At any
proper fixed window length, the symmetric difference of their two cyclic
window-set families has size at most

\[
 \boxed{4(k-1).}
\tag{4.1}
\]

#### Proof

A positional window can change only if one of its two boundary cuts lies
strictly inside the edited interval.  There are \(k-1\) internal cuts,
and each is the left boundary of one window and the right boundary of one
window.  Hence at most \(2(k-1)\) old positional windows change.  Cyclic
windows of a proper length in a distinct-label cyclic order are distinct.
The old-only and new-only families have equal size, so their symmetric
difference has size at most \(4(k-1)\). \(\square\)

### Theorem 4.2 (multi-seed collar support bound)

Suppose every component has at most \(R\) rooted resolutions and every
nonreference row differs from its reference row only inside one cyclic
interval of at most \(k\) positions.  Then at every depth

\[
 \boxed{|\mathcal A_q|\le4(R-1)(k-1)t,}
\tag{4.2}
\]

and for every depth set \(I\),

\[
 \boxed{
 \sum_{q\in I}|\mathcal A_q|
 \le4(R-1)(k-1)t|I|.}
\tag{4.3}
\]

#### Proof

For one root and one nonreference alternative, Lemma 4.1 bounds the
support of the row-profile difference by \(4(k-1)\).  Take the union over
at most \(R-1\) nonreference alternatives and then over the \(t\) roots.
Target coincidences only decrease the union size.  This proves (4.2), and
summing proves (4.3). \(\square\)

The same argument gives an adjacent-edit version.  Let \(d(P,a)\) be any
number of adjacent swaps realizing alternative \(a\) from the reference
row at root \(P\), after optimizing cyclic rotation and reversal if
desired.  Put

\[
 D_{\rm edit}=\sum_P\sum_{a\ne a_P^0}d(P,a).
\]

One adjacent swap changes at most two old positional windows and hence at
most four target coordinates.  Therefore

\[
 \boxed{
 \sum_{q\in I}|\mathcal A_q|
 \le4|I|D_{\rm edit}.}
\tag{4.4}
\]

This version makes clear that the relevant notion is the full ambient
cyclic-profile edit, including both collars, rather than the formal size
of an internal seed gadget.

---

## 5. Exact Gaussian-annulus accounting

Fix constants \(0\le a<b<\infty\) and let

\[
 I=I_{a,b}(m)
 =\{q:\lceil a\sqrt m\rceil\le q\le\lfloor b\sqrt m\rfloor\}.
\tag{5.1}
\]

Then

\[
 |I|=(b-a)\sqrt m+O(1).
\tag{5.2}
\]

The exact ratio

\[
 \lambda_q=\prod_{j=0}^{q-1}{m+2+j\over m-j}
\tag{5.3}
\]

satisfies, uniformly for \(q\le b\sqrt m+1\),

\[
 \log\lambda_q={q(q+1)\over m}+O_b(m^{-1/2}).
\tag{5.4}
\]

Consequently, for all sufficiently large \(m=m(b)\),

\[
 1\le c_q\le C_b:=\left\lceil e^{b^2+1}\right\rceil
 \qquad(q\in I).
\tag{5.5}
\]

The floor baseline itself has the exact annular asymptotic

\[
 \boxed{
 {B_I\over W\sqrt m}\longrightarrow
 \kappa_{a,b}:=
 \int_a^b
 {\{e^{x^2}\}(1-\{e^{x^2}\})
  \over e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.}
\tag{5.5a}
\]

Indeed,

\[
 {N_q\theta_q(1-\theta_q)\over c_q}
 =W\,{\{\lambda_q\}(1-\{\lambda_q\})
          \over\lambda_q\lfloor\lambda_q\rfloor}.
\]

The displayed function extends continuously by zero at the positive
integers.  Equations (5.2) and (5.4), followed by the Riemann-sum theorem,
prove (5.5a).  The integrand is positive except at the finitely many points
where \(e^{x^2}\) is an integer, so \(\kappa_{a,b}>0\).

Consequently, in the exactly uniform-barycenter case of Proposition 3.0,
the condition

\[
 \mathbb E\mathcal Q_I=o(W)
\]

is equivalent to the sharply tuned variance equation

\[
 \boxed{
 V_I^{\rm comp}
 =\kappa_{a,b}W\sqrt m+o(W).}
\tag{5.5b}
\]

Thus an \(O(W\sqrt m)\) raw variance estimate has insufficient accuracy
by a factor \(\sqrt m\) for the annular floor-corrected target.

Combining Theorem 4.2 with \(t/W=1/(2m+1)\) gives (0.3):

\[
\begin{aligned}
 {1\over W}\sum_{q\in I}|\mathcal A_q|
 &\le {4(R-1)(k-1)|I|\over2m+1}\\
 &=\bigl(2(b-a)+o_{a,b}(1)\bigr)
   {(R-1)(k-1)\over\sqrt m}.
\end{aligned}
\tag{5.6}
\]

### Corollary 5.1 (diffuse-defect no-go)

Let \(F_0\) be the reference state and put

\[
 \mathcal B(F_0)=
 \{(q,T):q\in I, \mu_q^{F_0}(T)\notin\{c_q,c_q+1\}\}.
\tag{5.7}
\]

Every child \(F_x\) satisfies

\[
 \boxed{
 \mathcal Q_I(F_x)
 \ge {2\over C_b}
 \left(
  |\mathcal B(F_0)|-\sum_{q\in I}|\mathcal A_q|
 \right)_+.}
\tag{5.8}
\]

In particular, if

\[
 |\mathcal B(F_0)|\ge\varepsilon W
\tag{5.9}
\]

for some fixed \(\varepsilon>0\), and

\[
 (R-1)(k-1)=o(\sqrt m),
\tag{5.10}
\]

then uniformly over every component selection,

\[
 \boxed{
 \mathcal Q_I(F_x)\ge
 \left({2\varepsilon\over C_b}-o_{a,b}(1)\right)W.}
\tag{5.11}
\]

#### Proof

At most \(\sum_q|\mathcal A_q|\) bad target-depth cells are active.  All
remaining bad cells are frozen and contribute at least \(2/c_q\ge2/C_b\)
in (2.2).  This proves (5.8).  Insert (5.6), (5.9), and (5.10) to obtain
(5.11). \(\square\)

Equivalently, if a bounded-collar multi-seed overlay satisfying (5.10)
contains any child with \(\mathcal Q_I=o(W)\), then its reference seed
already satisfies

\[
 |\mathcal B(F_0)|=o(W).
\tag{5.12}
\]

Thus such an overlay may polish an already balanced annulus, but it cannot
be the mechanism which removes a diffuse linear defect.

---

## 6. Exact boundary

The proved obstruction covers arbitrary unrelated exact seeds and
arbitrary orbit-mass transport, provided the physical component
resolutions have either sparse literal annular support or insufficient
quotient transport capacity.  It has three independent parts:

* deterministic selection cannot change frozen bad cells;
* for every chosen target partition, the attainable orbit-mass vectors
  form an exact component Minkowski sum and must reach the box
  \(0\le D_O\le|O|\);
* independent component averaging pays a positive adjacent-integer cost
  wherever two component effects overlap.

It does **not** prove that every exact-factor overlay fails.  A successful
annular component theorem must realize at least one of the following exact
escapes.

1.  **Growing literal support:**
    \((R-1)(k-1)=\Omega(\sqrt m)\), or more generally
    \(|I|D_{\rm edit}=\Omega(W)\), so a linear number of target-depth
    cells can actually move.
2.  **Sufficient quotient transport:** for every obstructing target
    partition, the joint component Minkowski sum reaches within \(o(W)\)
    weighted distance of the floor-optimal box at all annular depths.
3.  **Prebalanced seeds:** every seed entering the atlas already has only
    \(o(W)\) non-floor cells outside the movable support.
4.  **Near-disjoint target activity:** independent heat is used, but the
    doubly active sets in (3.4) have total weight \(o(W)\).
5.  **Correlated discrepancy:** component choices are globally correlated
    so that the product collision theorem does not apply; exact ownership
    must then be proved for that correlated selection.

In particular, merely replacing one relabeled seed by two or finitely many
unrelated seeds is not enough.  The quantitative new gate is a physical
annular support theorem at scale \(\Omega(W)\), together with either
collision-free ownership or a correlated integral selection law.
