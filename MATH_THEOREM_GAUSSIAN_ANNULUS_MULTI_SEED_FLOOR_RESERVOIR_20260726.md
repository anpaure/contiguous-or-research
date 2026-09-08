# Gaussian-annulus multi-seed overlays: exact floor reservoir, binary collision classification, and orbit-quotient obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
\mathcal T_q=\binom{[n]}{m-q},\qquad N_q=|\mathcal T_q|,
\]

and fix

\[
I=I_{a,b}(m)=
\{q:\lceil a\sqrt m\rceil\le q\le\lfloor b\sqrt m\rfloor\},
\qquad 0\le a<b<\infty.
\]

Write

\[
\lambda_q={W\over N_q}=c_q+\theta_q,\qquad
c_q=\lfloor\lambda_q\rfloor,\qquad 0\le\theta_q<1.
\]

For an exact middle wreath factor \(F\), define

\[
\mathcal Q_I(F)=
\sum_{q\in I}{1\over c_q}
\left(\|\mu_q^F-\lambda_q\mathbf1\|_2^2
-N_q\theta_q(1-\theta_q)\right).
\tag{0.1}
\]

This note proves three exact results.

1. For every physical multi-seed ownership overlay with independent
component choices,

\[
\boxed{\mathbb E\mathcal Q_I=\mathsf T_I+\mathsf R_I,}
\tag{0.2}
\]

where both terms are nonnegative.  Here \(\mathsf T_I\) is the convex
transport cost of the barycentric load to the floor box
\([c_q,c_q+1]^{\mathcal T_q}\), while \(\mathsf R_I\) is variance above
the least variance compatible with integer loads.  Consequently
\(\mathsf T_I+\mathsf R_I=o(W)\) is an exact baseline-corrected
contraction criterion for a genuine physical multi-seed overlay.

2. For fair two-seed component heat, let \(a_{K,q,T}\) be the integer
load change made by component \(K\) at target \(T\).  Then

\[
\boxed{
\mathsf R_I={1\over4}
\sum_{q\in I}{1\over c_q}\sum_{T\in\mathcal T_q}
\left(\sum_Ka_{K,q,T}^2
-\mathbf1_{\{\sum_Ka_{K,q,T}\ {\rm odd}\}}\right).}
\tag{0.3}
\]

The local summand vanishes exactly when no component changes \(T\), or
one component changes it by \(+1\) or \(-1\).  Every other pattern costs
at least \(1/2\).  Thus fair binary heat can have \(o(W)\) annular
defect only if its physical effects are disjoint single-unit moves away
from \(o(W)\) weighted target-depth cells.

3. For any partition into target-orbit cells, attainable orbit masses
give a deterministic lower bound on every component state.  If a cell
has size \(r\), its excess above \(c_qr\) is \(D=ar+\rho\), and
\(0\le\rho<r\), put

\[
G_r(D)=ra(a-1)+2a\rho.
\tag{0.4}
\]

Then every child satisfies

\[
\boxed{
\mathcal Q_I(F)\ge
\sum_{q\in I}{1\over c_q}\sum_OG_{|O|}(D_{q,O}(F))
\ge
2\sum_{q\in I}{1\over c_q}\sum_O
\operatorname {dist}(D_{q,O}(F),[0,|O|]).}
\tag{0.5}
\]

This remains valid when all component trades change orbit masses.  The
statewise gate is whether their integral, common-all-depth orbit-mass
semigroup reaches every floor interval simultaneously.

Finally, the Gaussian floor reservoir is

\[
B_I=\sum_{q\in I}{N_q\theta_q(1-\theta_q)\over c_q}
=(\kappa_{a,b}+o(1))W\sqrt m,\qquad \kappa_{a,b}>0.
\tag{0.6}
\]

Therefore an \(O(W\sqrt m)\) variance estimate is not accurate enough.
For a uniform barycenter one needs

\[
V_I=B_I+o(W),
\tag{0.7}
\]

not merely \(V_I=O(W\sqrt m)\).

---

## 1. Exact adjacent-floor identity

Every exact factor obeys

\[
\sum_{T\in\mathcal T_q}\mu_q^F(T)=W.
\tag{1.1}
\]

Put \(y_T=\mu_q^F(T)-c_q\).  Since
\(\sum_Ty_T=N_q\theta_q\),

\[
\begin{aligned}
\|\mu_q^F-\lambda_q\mathbf1\|_2^2
-N_q\theta_q(1-\theta_q)
&=\sum_T(y_T-\theta_q)^2-N_q\theta_q(1-\theta_q)\\
&=\sum_Ty_T(y_T-1).
\end{aligned}
\tag{1.2}
\]

Hence

\[
\boxed{
\mathcal Q_I(F)=\sum_{q\in I}{1\over c_q}
\sum_{T\in\mathcal T_q}
(\mu_q^F(T)-c_q)(\mu_q^F(T)-c_q-1).}
\tag{1.3}
\]

Every summand is a nonnegative even integer, vanishing exactly at
\(c_q,c_q+1\).  Also, for integral \(y\),

\[
y(y-1)\ge2\big((-y)_++(y-1)_+\big).
\tag{1.4}
\]

Thus \(\mathcal Q_I=o(W)\) implies \(o(W)\) aggregate weighted
floor/ceiling discrepancy.  Since \(c_q=O_{a,b}(1)\) in the annulus,
the corresponding unweighted discrepancy is also \(o(W)\).

---

## 2. Physical multi-seed ownership components

Let \(F_1,\ldots,F_L\) be arbitrary exact middle wreath factors.  Form
their \(L\)-partite ownership hypergraph: vertices are tagged rows and
each middle \(m\)-set gives the \(L\)-edge containing its unique owner
in every seed.  Let \(K\) range over connected components.

The rows of every seed in \(K\) partition the same middle-owner set.  If
one shore has \(b_K\) rows, every shore has \(b_K\) rows.  Choosing one
complete seed shore independently in each component therefore gives
another exact integral factor.

Let \(u_{K,j,q}\in\mathbb Z_{\ge0}^{\mathcal T_q}\) be the depth-\(q\)
load supplied by the \(F_j\)-shore of \(K\), and put

\[
\bar u_{K,q}={1\over L}\sum_{j=1}^Lu_{K,j,q},\qquad
\bar\mu_q=\sum_K\bar u_{K,q}.
\tag{2.1}
\]

Choose \(J_K\) independently and uniformly in \([L]\), and set

\[
X_q(T)=\sum_Ku_{K,J_K,q}(T).
\tag{2.2}
\]

Then \(X\) is the load of an exact integral factor,

\[
\mathbb EX_q=\bar\mu_q,
\quad
\operatorname {Var}X_q(T)
=\sum_K{1\over L}\sum_{j=1}^L
(u_{K,j,q}(T)-\bar u_{K,q}(T))^2.
\tag{2.3}
\]

Give the direct sum the norm

\[
\|z\|_I^2=\sum_{q\in I}{1\over c_q}\|z_q\|_2^2,
\]

and define

\[
V_I=\sum_K{1\over L}\sum_{j=1}^L
\|u_{K,j}-\bar u_K\|_I^2.
\tag{2.4}
\]

The mean-square identity gives

\[
\boxed{
\mathbb E\mathcal Q_I(X)
=\|\bar\mu-\lambda\mathbf1\|_I^2+V_I-B_I.}
\tag{2.5}
\]

There is also an exact joined-owner form.  Put

\[
A_I={1\over L}\sum_{j=1}^L
\|\mu^{F_j}-\bar\mu\|_I^2.
\tag{2.6}
\]

Then

\[
A_I={1\over L^2}\sum_{i<j}\|\mu^{F_i}-\mu^{F_j}\|_I^2,
\qquad
V_I={1\over L^2}\sum_K\sum_{i<j}
\|u_{K,i}-u_{K,j}\|_I^2,
\tag{2.7}
\]

and therefore

\[
\boxed{
\mathbb E\mathcal Q_I(X)
={1\over L}\sum_{j=1}^L\mathcal Q_I(F_j)-(A_I-V_I).}
\tag{2.8}
\]

Thus \(A_I-V_I\) is precisely the cross-component Gram removed by
independent shore choices.  It can have either sign for unrelated seeds;
no relabeling identity has been used.

---

## 3. Exact floor-reservoir decomposition

For real \(x\), write \(r(x)=x-\lfloor x\rfloor\) and define

\[
\ell_\lambda(x)=
(1-r(x))(\lfloor x\rfloor-\lambda)^2
+r(x)(\lfloor x\rfloor+1-\lambda)^2.
\tag{3.1}
\]

Equivalently,

\[
\ell_\lambda(x)=(x-\lambda)^2+r(x)(1-r(x)).
\tag{3.2}
\]

The slope on \([j,j+1]\) is \(2(j-\lambda)+1\), so
\(\ell_\lambda\) is convex.  Also

\[
\ell_{\lambda_q}(\lambda_q)=\theta_q(1-\theta_q).
\tag{3.3}
\]

If an integer-valued random variable \(Z\) has mean \(p=a+r\), where
\(a\in\mathbb Z\) and \(0\le r<1\), then
\((Z-a)(Z-a-1)\ge0\) gives

\[
\operatorname {Var}Z\ge r(1-r).
\tag{3.4}
\]

Equality holds exactly when \(Z\in\{a,a+1\}\) almost surely.

Define

\[
\mathsf T_I=
\sum_{q\in I}{1\over c_q}
\left(\sum_{T\in\mathcal T_q}
\ell_{\lambda_q}(\bar\mu_q(T))
-N_q\ell_{\lambda_q}(\lambda_q)\right),
\tag{3.5}
\]

\[
\mathsf R_I=
\sum_{q\in I}{1\over c_q}\sum_{T\in\mathcal T_q}
\left(\operatorname {Var}X_q(T)
-r(\bar\mu_q(T))(1-r(\bar\mu_q(T)))\right).
\tag{3.6}
\]

### Theorem 3.1 (baseline-corrected contraction)

\[
\boxed{
\mathbb E\mathcal Q_I(X)=\mathsf T_I+\mathsf R_I,
\qquad \mathsf T_I\ge0,\quad\mathsf R_I\ge0.}
\tag{3.7}
\]

Moreover:

* \(\mathsf T_I=0\) exactly when
  \(\bar\mu_q(T)\in[c_q,c_q+1]\) for every \(q,T\);
* \(\mathsf R_I=0\) exactly when every marginal \(X_q(T)\) is supported
  on the two adjacent integers bracketing its mean;
* if \(\mathsf T_I+\mathsf R_I=o(W)\), some exact component child has
  \(\mathcal Q_I=o(W)\);
* product component heat has expected defect \(o(W)\) only if both terms
  are \(o(W)\).

#### Proof

Equation (3.2), summed over all coordinates, rewrites (2.5) as (3.7).
Jensen's inequality applies because

\[
{1\over N_q}\sum_T\bar\mu_q(T)=\lambda_q,
\]

and proves \(\mathsf T_I\ge0\).  Inequality (3.4) proves
\(\mathsf R_I\ge0\).

The maximal affine interval of \(\ell_{\lambda_q}\) containing its mean
\(\lambda_q\) is \([c_q,c_q+1]\).  This gives the first equality
condition; when \(\theta_q=0\), the average constraint forces every
entry in that interval to equal \(c_q\).  Equality in (3.4) gives the
second condition.  Some outcome is no larger than the expectation, and
the last assertion follows from nonnegativity. \(\square\)

If \(\bar\mu_q=\lambda_q\mathbf1\), then \(\mathsf T_I=0\), and

\[
V_I-B_I=\mathsf R_I\ge0.
\tag{3.8}
\]

Thus the floor baseline is the least possible component variance, not a
variance error that may be discarded.

---

## 4. Sharp fair-binary classification

Take \(L=2\), and put

\[
a_{K,q,T}=u_{K,2,q}(T)-u_{K,1,q}(T)\in\mathbb Z.
\tag{4.1}
\]

Let independent fair bits \(B_K\) select the second shores.  At fixed
\((q,T)\),

\[
X_q(T)=x_0+\sum_KB_Ka_{K,q,T},
\qquad
\operatorname {Var}X_q(T)={1\over4}\sum_Ka_{K,q,T}^2.
\tag{4.2}
\]

If \(A=\sum_Ka_{K,q,T}\), the mean is \(x_0+A/2\).  Its fractional
part is zero for even \(A\), and \(1/2\) for odd \(A\).  Substitution in
(3.6) proves (0.3).

Because \(z^2\equiv z\pmod2\), the bracket in (0.3) is a nonnegative
even integer.  It vanishes precisely when

\[
(a_K)_K=0
\quad\hbox{or}\quad
(a_K)_K=(0,\ldots,0,\pm1,0,\ldots,0).
\tag{4.3}
\]

Every other vector gives a bracket at least two.  If
\(\mathcal C_q^*\) is the set of targets violating (4.3), then

\[
\boxed{
\mathsf R_I\ge{1\over2}
\sum_{q\in I}{|\mathcal C_q^*|\over c_q}.}
\tag{4.4}
\]

This detects both two-component overlap and a single component jump of
magnitude at least two.  It permits genuine orbit-mass transfer, but
forces such transfers to be literal disjoint unit moves if fair heat is
to reach \(o(W)\).

---

## 5. Deterministic orbit-mass quotient

At each depth fix any partition \(\mathscr O_q\) of \(\mathcal T_q\).
For an actual integral child set

\[
D_{q,O}=\sum_{T\in O}(\mu_q(T)-c_q),\qquad O\in\mathscr O_q.
\tag{5.1}
\]

### Lemma 5.1 (sharp cell relaxation)

Let \(r\ge1\), \(D\in\mathbb Z\), and write
\(D=ar+\rho\), \(0\le\rho<r\).  Then

\[
\min_{\substack{y_i\in\mathbb Z\\ \sum_{i=1}^ry_i=D}}
\sum_{i=1}^ry_i(y_i-1)
=G_r(D)=ra(a-1)+2a\rho.
\tag{5.2}
\]

Also

\[
G_r(D)\ge2\operatorname {dist}(D,[0,r]).
\tag{5.3}
\]

#### Proof

If \(y_i\ge y_j+2\), replacing \((y_i,y_j)\) by
\((y_i-1,y_j+1)\) decreases the objective by
\(2(y_i-y_j-1)\).  Thus a minimizer has \(\rho\) entries \(a+1\)
and \(r-\rho\) entries \(a\), proving (5.2).

For \(0\le D\le r\), both sides of (5.3) vanish.  If \(D>r\),

\[
G_r(D)-2(D-r)=(a-1)(r(a-2)+2\rho)\ge0.
\]

If \(D<0\),

\[
G_r(D)-2(-D)=(a+1)(ra+2\rho)\ge0.
\]

This proves (5.3). \(\square\)

Applying the lemma cellwise in (1.3) proves (0.5).  In a multi-seed
overlay,

\[
D_{q,O}(j_\bullet)=
\sum_K\sum_{T\in O}u_{K,j_K,q}(T)-c_q|O|.
\tag{5.4}
\]

Consequently

\[
\Delta_{\rm orb}:=
\min_{(j_K)}
\sum_{q\in I}{1\over c_q}
\sum_{O\in\mathscr O_q}G_{|O|}(D_{q,O}(j_\bullet))
\tag{5.5}
\]

is a statewise lower bound for every canonical child.  This is not an
orbit-invariance claim: every vector in (5.4) may depend on \(j_K\).
It is an integral coupled-semigroup obstruction.

For a direct transport bound, fix a reference state \(j_K^0\) and put

\[
L_0=\sum_{q\in I}{1\over c_q}\sum_O
\operatorname {dist}(D_{q,O}(j^0),[0,|O|]),
\tag{5.6}
\]

\[
C=\sum_K\max_j\sum_{q\in I}{1\over c_q}\sum_O
\left|\sum_{T\in O}
(u_{K,j,q}(T)-u_{K,j_K^0,q}(T))\right|.
\tag{5.7}
\]

Distance to an interval is one-Lipschitz, so every child satisfies

\[
\boxed{\mathcal Q_I(F_{j_\bullet})\ge2(L_0-C)_+.}
\tag{5.8}
\]

Thus even dense orbit-changing trades fail statewise if their total
orbit-mass transport capacity is smaller than the reference distance
from the floor box by \(\Omega(W)\).

---

## 6. Gaussian accounting and exact surviving gate

The exact load ratio is

\[
\lambda_q=\prod_{j=0}^{q-1}{m+2+j\over m-j}.
\tag{6.1}
\]

Uniformly for \(q\le b\sqrt m+1\),

\[
\log\lambda_q={q(q+1)\over m}+O_b(m^{-1/2}).
\tag{6.2}
\]

Thus \(c_q=O_b(1)\), and \(q/\sqrt m\to x\) implies
\(\lambda_q\to e^{x^2}\).  Since \(N_q=W/\lambda_q\), Riemann summation
gives

\[
{B_I\over W\sqrt m}\longrightarrow
\kappa_{a,b}:=
\int_a^b
{\{e^{x^2}\}(1-\{e^{x^2}\})
\over e^{x^2}\lfloor e^{x^2}\rfloor}\,dx.
\tag{6.3}
\]

The integrand extends continuously by zero where \(e^{x^2}\) is an
integer and is positive elsewhere, so \(\kappa_{a,b}>0\).

The proved boundary is therefore:

* a physical product overlay closes the annulus if it proves
  \(\mathsf T_I=o(W)\) and \(\mathsf R_I=o(W)\);
* for two seeds, the latter is exactly the disjoint-unit condition
  (0.3), up to \(o(W)\) weighted violations;
* every deterministic or correlated choice still has to pass the
  statewise orbit-semigroup bound (0.5);
* the missing constructive object is an exact atlas with broad enough
  orbit-mass transport to make \(\mathsf T_I=o(W)\), while its physical
  effects are disjoint unit moves, or else an equally strong correlated
  discrepancy theorem.

Uniform orbit averaging plus a raw \(O(W\sqrt m)\) variance estimate does
not suffice.  No constant-one conclusion is claimed.
