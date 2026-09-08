# Lane W: integral Reynolds substeps and matched-component orbit rebalancing

Date: 2026-07-25

## 0. Result and exact boundary

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
t=\frac Wn=\operatorname{Cat}_m.
\]

This report proves two integral statements inside one exact middle-wreath
factor.

1. **Floor-aware conformal substep.**  For every exact factor whose
   floor-corrected weighted collision excess is positive, full coordinate
   orbit averaging produces a nonzero connected ownership-component trade
   \(g_C\).  It is squarefree, conformal to the Reynolds direction, and
   \(F+g_C\) is a literal exact factor.  Its negative floor-supporting signal
   is at least
   \[
   \frac{s_C}{2t}Q(F),
   \]
   where \(s_C\) is the number of old wreaths in the component.

2. **Correlated matched-sign rounding.**  In any overlay of two exact orbit
   factors, ownership components may be paired and their two side choices
   forced to have a chosen relative sign.  Independent fair coins between
   the pairs give genuine exact factors in every outcome.  This proves an
   exact upper bound for the common-sign rounding variance by a minimum
   vector-pairing cost.  Components of the same shadow type cancel in pairs;
   only within-type diameter and one parity residue per odd type are paid.

The first statement gives an actual nonzero exact-factor endpoint, not a
fractional vector.  It escapes the coordinate orbit only when the selected
component is a proper overlay component; the theorem does not guarantee
that fragmentation.  It also does **not** by itself prove collision descent.
The exact remaining toll is a nonnegative integral curvature
\(\kappa_F(C)\).  Actual descent follows if

\[
\frac{\kappa_F(C)}{s_C}<\frac{Q(F)}t.
\]

Likewise, the matched-sign theorem becomes a constant-one proof if, for
some \(\eta_A<1\), its orbit-averaged pairing cost is at most the integer
floor term plus \(2\eta_AQ_A+O_A(H_A\operatorname{Cat}_m)\).  Neither
curvature/type-capacity estimate is proved here.  Thus the report gives a proved integral
rebalancing theorem and a sharp tractable missing lemma, not \(\mathrm{SPC}_A\)
or the constant-one theorem.

## 1. Exact-factor and collision notation

Let \(\mathscr W_m\) be the set of physical unoriented \(n\)-wreaths.  For
\(0\le q\le m-1\), let

\[
A_q:\mathbb Z^{\mathscr W_m}
   \longrightarrow
   \mathbb Z^{\binom{[n]}{m-q}}
\]

be the depth-\(q\) interval-incidence operator.  Thus \(A_0\) is middle
ownership incidence.  An exact factor is a vector

\[
f=\mathbf1_F\in\{0,1\}^{\mathscr W_m},
\qquad A_0f=\mathbf1.
\]

Every exact factor has exactly \(t\) wreaths.  Put

\[
N_q=\binom n{m-q},\qquad
\mu_q^F=A_qf,\qquad
\lambda_q=\frac W{N_q},
\]

and write

\[
c_q=\lfloor\lambda_q\rfloor,
\qquad \theta_q=\lambda_q-c_q\in[0,1).
\]

Fix \(1\le H\le m-1\) and positive weights \(w_q\).  The application to
constant one takes

\[
H=H_A:=\lceil A\sqrt m\rceil,
\qquad w_q=\frac1{c_q}.
\]

For every fixed \(A\), this choice has \(H_A\le m-1\) for all sufficiently
large \(m\).  We abbreviate the resulting quantities by \(Q_A(F)\) and
\(B_A\).

Define the doubled floor-corrected collision excess

\[
\boxed{
Q_w(F)=
\sum_{q=1}^{H}w_q
\sum_{S\in\binom{[n]}{m-q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
}
\tag{1.1}
\]

Every summand is a nonnegative even integer before multiplication by
\(w_q\), so \(Q_w(F)\ge0\).  With

\[
e_q^F=\mu_q^F-\lambda_q\mathbf1,
\qquad
B_w=\sum_{q=1}^{H}w_qN_q\theta_q(1-\theta_q),
\tag{1.2}
\]

We abbreviate

\[
\|e_F\|_w^2:=\sum_{q=1}^{H}w_q\|e_q^F\|_2^2.
\tag{1.2a}
\]

the exact floor identity is

\[
\boxed{
Q_w(F)=\sum_{q=1}^{H}w_q\|e_q^F\|_2^2-B_w.
}
\tag{1.3}
\]

Indeed, if \(k=\mu-c_q\), then \(e=k-\theta_q\), and the term linear in
\(e\) vanishes after summing because every exact factor has total depth load
\(W\).

For the weights \(w_q=1/c_q\), the weighted balanced overload is at most
\(Q_w(F)/2\), since

\[
\frac{k(k-1)}2\ge(k-1)_+
\qquad(k\in\mathbb Z).
\tag{1.4}
\]

Thus

\[
Q_w(F)=O_A(H_At)=O_A(W/\sqrt m)=o(W)
\tag{1.5}
\]

is already at the constant-one fixed-window scale.

## 2. The clipped floor functional

Define \(h:\mathbb Z\to\mathbb Z\) by

\[
h(k)=
\begin{cases}
k,&k\le0,\\
k-1,&k\ge1.
\end{cases}
\tag{2.1}
\]

This is the signed distance from the two balanced values \(\{0,1\}\).

### Lemma 2.1 (exact floor identities)

For every \(k\in\mathbb Z\) and every \(0\le\theta<1\),

\[
\boxed{k(k-1)=h(k)^2+|h(k)|}
\tag{2.2}
\]

and

\[
\boxed{h(k)(k-\theta)\ge\frac12k(k-1).}
\tag{2.3}
\]

#### Proof

If \(k\le0\), then \(h(k)=k\), and

\[
h(k)^2+|h(k)|=k^2-k=k(k-1).
\]

Moreover,

\[
2h(k)(k-\theta)-k(k-1)
=k(k+1-2\theta)\ge0.
\]

For \(k=0\) this is zero.  For \(k\le-1\), both factors in the last
product are nonpositive.

If \(k\ge1\), then \(h(k)=k-1\), and

\[
h(k)^2+|h(k)|=(k-1)^2+(k-1)=k(k-1),
\]

while

\[
2h(k)(k-\theta)-k(k-1)
=(k-1)(k-2\theta)\ge0.
\]

For \(k=1\) the product is zero; for \(k\ge2\), its second factor is
positive.  This proves both statements. \(\square\)

For a fixed factor \(F\), put

\[
k_{q,S}^F=\mu_q^F(S)-c_q,
\qquad h_F(q,S)=h(k_{q,S}^F),
\tag{2.4}
\]

and use the weighted inner product

\[
\langle a,b\rangle_w
=\sum_{q=1}^{H}w_q\sum_Sa_q(S)b_q(S).
\tag{2.5}
\]

Lemma 2.1 gives the exact supporting inequality

\[
\boxed{
\langle h_F,e_F\rangle_w\ge\frac12Q_w(F).
}
\tag{2.6}
\]

## 3. A nonzero integral conformal Reynolds substep

For a coordinate permutation \(\pi\in S_n\), let \(\pi F\) be the
relabelled exact factor.  Form the bipartite middle-owner overlay
\(\Gamma(F,\pi F)\): its left vertices are indexed wreaths of \(F\), its
right vertices are indexed wreaths of \(\pi F\), and every middle set \(K\)
is an edge between its unique two owners.  Every vertex has degree \(n\).

For a connected component \(C\), let \(F_C\) and \((\pi F)_C\) be its two
block sides and define

\[
g_C=\mathbf1_{(\pi F)_C}-\mathbf1_{F_C},
\qquad
s_C=|F_C|=|(\pi F)_C|,
\tag{3.1}
\]

where equality of side sizes follows by counting the \(n\)-regular edges
of the component.  Put

\[
u_{C,q}=A_qg_C.
\tag{3.2}
\]

Switching the complete component gives

\[
F_C^+=(F\setminus F_C)\cup(\pi F)_C,
\tag{3.3}
\]

which is again a physical exact factor: every middle edge has one endpoint
on each chosen side.

Let

\[
D_m=\frac{m!(m+1)!}{2}
\tag{3.4}
\]

be the number of physical wreaths containing a fixed middle set, and define
the Reynolds integer kernel direction

\[
z_F=\mathbf1_{\mathscr W_m}-D_m\mathbf1_F.
\tag{3.5}
\]

### Theorem 3.1 (floor-aware integral Reynolds substep)

Let \(m\ge2\), \(1\le H\le m-1\), and \(w_q>0\).  If an exact factor
\(F\) satisfies \(Q_w(F)>0\), then there are a coordinate permutation
\(\pi\) and a nonzero connected component \(C\) of
\(\Gamma(F,\pi F)\) such that:

1. \(F_C^+=F+g_C\) is a literal exact factor;
2. \(g_C\) is squarefree and conformal to \(z_F\);
3. \(g_C\) is a primitive conformal integer kernel vector of \(A_0\); and
4. its floor-supporting signal obeys
   \[
   \boxed{
   -\frac1{s_C}\langle h_F,u_C\rangle_w
   \ge\frac{Q_w(F)}{2t}.
   }
   \tag{3.6}
   \]

In particular, orbit averaging always produces a nonzero one-factor
integral step with a strictly negative clipped-floor supporting signal.

#### Proof

For uniform \(\pi\in S_n\), transitivity on every target rank and the fixed
total depth load \(W\) give

\[
\mathbb E_\pi e_q^{\pi F}(S)=0
\qquad(q\le H,\ S\in\tbinom{[n]}{m-q}).
\tag{3.7}
\]

Therefore

\[
\mathbb E_\pi\langle h_F,e_{\pi F}\rangle_w=0.
\tag{3.8}
\]

Choose \(\pi\) with

\[
\langle h_F,e_{\pi F}\rangle_w\le0.
\tag{3.9}
\]

Equations (2.6) and (3.9) imply

\[
\left\langle h_F,e_{\pi F}-e_F\right\rangle_w
\le-\frac12Q_w(F).
\tag{3.10}
\]

If one indexed wreath occurs in both factors, its two copies form an
isolated overlay component with \(n\) parallel middle edges; its component
vector is zero.  Delete all such common components.  Every remaining
component has its negative support in \(F\) and its positive support outside
\(F\).  Hence

\[
g_C\sqsubseteq z_F
\tag{3.11}
\]

in the conformal order.  Also

\[
\sum_Cs_C=|F\setminus\pi F|\le t,
\qquad
\sum_Cu_C=e_{\pi F}-e_F.
\tag{3.12}
\]

The strict negativity in (3.10) shows that at least one remaining
component is nonzero.  If every component violated (3.6), summing over
components and using (3.12) would give a value strictly larger than
\(-Q_w(F)/2\), contradicting (3.10).  Thus a component satisfying (3.6)
exists.

It remains only to prove primitivity.  A conformal subvector of \(g_C\)
chooses some of its left coefficients \(-1\) and some of its right
coefficients \(+1\).  In the row belonging to a middle edge, kernel balance
forces its two incident coefficients to be chosen together or omitted
together.  Connectedness of \(C\) therefore forces a nonzero conformal
kernel subvector to contain every vertex of \(C\).  Thus \(g_C\) is
primitive. \(\square\)

## 4. Exact curvature and the quota-safe class

Define

\[
\sigma_F(q,S)=
\begin{cases}
-1,&k_{q,S}^F\le0,\\
+1,&k_{q,S}^F\ge1.
\end{cases}
\tag{4.1}
\]

For a component \(C\), define its floor curvature

\[
\boxed{
\kappa_F(C)=
\sum_{q=1}^{H}w_q
\left(
\|u_{C,q}\|_2^2+
\langle\sigma_F(q,\cdot),u_{C,q}\rangle
\right).
}
\tag{4.2}
\]

### Theorem 4.1 (exact component expansion)

For every ownership component switch,

\[
\boxed{
Q_w(F_C^+)-Q_w(F)
=2\langle h_F,u_C\rangle_w+\kappa_F(C).
}
\tag{4.3}
\]

Moreover,

\[
\boxed{
\kappa_F(C)=
\sum_{q,S}w_q
\begin{cases}
u_{C,q}(S)(u_{C,q}(S)-1),&k_{q,S}^F\le0,\\
u_{C,q}(S)(u_{C,q}(S)+1),&k_{q,S}^F\ge1,
\end{cases}
\ge0.
}
\tag{4.4}
\]

Equality \(\kappa_F(C)=0\) holds exactly when

\[
u_{C,q}(S)\in\{0,1\}
\quad\text{on every currently low cell }k_{q,S}^F\le0,
\tag{4.5}
\]

and

\[
u_{C,q}(S)\in\{-1,0\}
\quad\text{on every currently high cell }k_{q,S}^F\ge1.
\tag{4.6}
\]

#### Proof

At one target cell, with current integer \(k\) and integer change \(u\),

\[
(k+u)(k+u-1)-k(k-1)=(2k-1)u+u^2.
\tag{4.7}
\]

The definition of \(h\) gives the exact identity

\[
2k-1=2h(k)+\sigma(k).
\tag{4.8}
\]

Summing (4.7)--(4.8) proves (4.3).  If \(k\le0\), the curvature term is
\(u^2-u=u(u-1)\); if \(k\ge1\), it is
\(u^2+u=u(u+1)\).  Both are nonnegative for integer \(u\), and vanish
exactly in the two displayed unit-transfer classes. \(\square\)

### Corollary 4.2 (an exact finite-descent gate)

For the component supplied by Theorem 3.1,

\[
Q_w(F_C^+)-Q_w(F)
\le -\frac{s_C}{t}Q_w(F)+\kappa_F(C).
\tag{4.9}
\]

Consequently it is a strict integral collision descent whenever

\[
\boxed{
\frac{\kappa_F(C)}{s_C}<\frac{Q_w(F)}t.
}
\tag{4.10}
\]

In particular, every quota-safe unit-transfer component
\(\kappa_F(C)=0\) selected by Theorem 3.1 strictly improves \(F\).

The following is a scale-correct sufficient theorem for constant one.

> **Unproved joint curvature lemma \(\mathrm{JCL}_A\).**  There are
> constants \(0<\eta_A\le1\) and \(0\le C_A<\infty\) such that every exact factor
> \(F\) with \(Q_A(F)>0\) has one component satisfying both (3.6) and
> \[
> \frac{\kappa_F(C)}{s_C}
> \le(1-\eta_A)\frac{Q_A(F)}t+C_AH_A.
> \tag{4.11}
> \]

If \(F_*\) globally minimizes \(Q_A\), then (4.9)--(4.11) and minimality
give

\[
0\le-\eta_A\frac{Q_A(F_*)}t+C_AH_A,
\]

so

\[
\boxed{
Q_A(F_*)\le\frac{C_A}{\eta_A}H_At=o(W).
}
\tag{4.12}
\]

An aggregate version is also sufficient.  For the orbit comparator chosen
in (3.9), if its nonzero components obey

\[
\sum_C\kappa_F(C)
\le(1-\eta_A)Q_A(F)+C_AH_At,
\tag{4.13}
\]

then summing (4.3) and using (3.10) shows that some single component
strictly descends whenever \(Q_A(F)>C_AH_At/\eta_A\).  Thus (4.13) gives
the same minimizer bound (4.12).

No estimate (4.11) or (4.13) is proved here.

## 5. Exact antipodal orbit rebalancing

We next give a second, genuinely correlated way to round ownership
components.

Fix any \(\pi\), and let \(C_1,\ldots,C_r\) be the nonzero components of
\(\Gamma(F,\pi F)\).  Stack their weighted shadow effects as Hilbert vectors

\[
d_i=\left(\sqrt{w_q}\,u_{C_i,q}\right)_{q\le H}.
\tag{5.1}
\]

Put

\[
D=\sum_{i=1}^rd_i,
\qquad
\mathcal A_\pi=\|D\|^2.
\tag{5.2}
\]

For \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_r)\in\{\pm1\}^r\),
choose the \(\pi F\)-side of component \(i\) when \(\varepsilon_i=+1\)
and the \(F\)-side when \(\varepsilon_i=-1\).  Denote the resulting exact
factor by \(F_\varepsilon\).  Its antipode \(F_{-\varepsilon}\) makes the
opposite choice in every component.  Define

\[
R_\pi(\varepsilon)=\left\|\sum_i\varepsilon_id_i\right\|^2,
\qquad
\beta_\pi=\min_{\varepsilon\in\{\pm1\}^r}R_\pi(\varepsilon).
\tag{5.3}
\]

### Theorem 5.1 (exact antipodal identity)

For every sign vector \(\varepsilon\),

\[
\boxed{
Q_w(F_\varepsilon)+Q_w(F_{-\varepsilon})
=2Q_w(F)+\frac{R_\pi(\varepsilon)-\mathcal A_\pi}{2}.
}
\tag{5.4}
\]

Consequently some literal exact factor \(H\subseteq F\cup\pi F\) satisfies

\[
\boxed{
Q_w(H)\le Q_w(F)-\frac{\mathcal A_\pi-\beta_\pi}{4}.
}
\tag{5.5}
\]

In particular,

\[
\boxed{
\mathcal A_\pi-4Q_w(F)\le\beta_\pi\le\mathcal A_\pi.
}
\tag{5.6}
\]

#### Proof

Let the weighted centered load vector and its midpoint be

\[
\widetilde e_F
=\left(\sqrt{w_q}\,e_q^F\right)_{q\le H},
\qquad
x=\frac{\widetilde e_F+\widetilde e_{\pi F}}2.
\]

The centered load vectors of the two antipodes are

\[
x\pm\frac12\sum_i\varepsilon_id_i.
\tag{5.7}
\]

Their squared norms therefore sum to

\[
2\|x\|^2+\frac12R_\pi(\varepsilon).
\tag{5.8}
\]

Since \(F\) and \(\pi F\) have equal squared centered energy,

\[
\|x\|^2
=\|\widetilde e_F\|^2-\frac14\mathcal A_\pi
=\|e_F\|_w^2-\frac14\mathcal A_\pi.
\tag{5.9}
\]

Subtracting the two fixed floor baselines \(B_w\) proves (5.4).  Taking a
minimizing sign and then the better antipode proves (5.5).  The all-positive
sign gives \(\beta_\pi\le\mathcal A_\pi\).  Both terms on the left of
(5.4) are nonnegative, so a minimizing sign also gives the lower bound in
(5.6). \(\square\)

There is an exact covariance-cut formulation.  If \(S\subseteq[r]\) is
the set of signs flipped from the all-positive vector, then

\[
R_\pi(\varepsilon)-\mathcal A_\pi
=-4\sum_{i\in S,\ j\notin S}\langle d_i,d_j\rangle.
\tag{5.10}
\]

Thus

\[
\frac{\mathcal A_\pi-\beta_\pi}{4}
=\max_{S\subseteq[r]}
\sum_{i\in S,\ j\notin S}\langle d_i,d_j\rangle.
\tag{5.11}
\]

A positive covariance cut gives a nonzero strict exact-factor step.  More
sharply, cancellation of the required \(1-\varepsilon\) fraction follows
from the exact checkable inequality

\[
\boxed{
\mathcal A_\pi-\beta_\pi
\ge4(1-\varepsilon)Q_w(F)
\quad\Longrightarrow\quad
Q_w(H)\le\varepsilon Q_w(F).
}
\tag{5.12}
\]

For a chosen scale parameter \(q_0\), taking
\(\varepsilon=O(1/q_0)\) gives the corresponding
\(1-O(1/q_0)\) contraction of the aggregate objective.  It does not assert
simultaneous depthwise contraction by one signing.  Such a theorem would
require the analogue of (5.12) separately at every depth for one common
component sign vector and remains unproved.  Notice the compulsory floor
correction (5.6): controlling raw signed variance without subtracting the
integer baseline is not enough.

For arbitrary \(\pi\), (5.4) is an antipodal-sum identity.  It is not an
identity for each individual antipode because the midpoint term in (5.7)
need not be orthogonal to the signed component sum.

## 6. Correlated pairing and type capacity

The minimization in \(\beta_\pi\) is integral but still global.  The next
lemma gives a proved target-specific correlated signing.

Add one dummy zero vector if \(r\) is odd.  For a perfect pairing
\(\mathcal P\) of the resulting index set and relative signs
\(\rho_{ij}\in\{\pm1\}\), define

\[
M(\mathcal P,\rho)
=\sum_{\{i,j\}\in\mathcal P}
\|d_i+\rho_{ij}d_j\|^2,
\tag{6.1}
\]

and

\[
M_{\rm pair}=\min_{\mathcal P,\rho}M(\mathcal P,\rho),
\qquad
R_{\rm pair}=\min\{\mathcal A_\pi,M_{\rm pair}\}.
\tag{6.2}
\]

### Theorem 6.1 (matched-component exact rounding)

For every orbit overlay,

\[
\boxed{\beta_\pi\le R_{\rm pair}.}
\tag{6.3}
\]

Consequently some exact factor satisfies

\[
\boxed{
Q_w(H)\le Q_w(F)-\frac{\mathcal A_\pi-R_{\rm pair}}4.
}
\tag{6.4}
\]

#### Proof

Fix a pairing and its relative signs.  For every pair \(\{i,j\}\), choose
an independent fair sign \(\xi_{ij}\).  Put

\[
\varepsilon_i=\xi_{ij},
\qquad
\varepsilon_j=\rho_{ij}\xi_{ij}.
\tag{6.5}
\]

Every outcome is a complete-side choice in every ownership component and
hence is a literal exact factor.  The pair coins are independent and have
mean zero, so all cross-pair inner products vanish in expectation:

\[
\mathbb E\left\|\sum_i\varepsilon_id_i\right\|^2
=\sum_{\{i,j\}\in\mathcal P}
\|d_i+\rho_{ij}d_j\|^2.
\tag{6.6}
\]

Some outcome has squared norm at most this expectation.  Minimize over the
pairing and relative signs, and also allow the all-positive endpoint of
cost \(\mathcal A_\pi\).  This proves (6.3); (6.4) follows from Theorem
5.1. \(\square\)

This proves the required negative-covariance statement rather than assuming
a general negative-dependence property.

### Corollary 6.2 (exact type-capacity bound)

Partition the component indices into types \(I_a\), with
\(r_a=|I_a|\).  Suppose

\[
\|d_i-d_j\|^2\le\Delta_a
\qquad(i,j\in I_a).
\tag{6.7}
\]

For every type with odd \(r_a\), designate one residue
\(i_a\in I_a\) satisfying

\[
\|d_{i_a}\|^2\le R_a^2.
\tag{6.8}
\]

Then

\[
\boxed{
M_{\rm pair}
\le
\sum_a\left\lfloor\frac{r_a}{2}\right\rfloor\Delta_a
+\sum_{a:r_a\ {\rm odd}}R_a^2.
}
\tag{6.9}
\]

#### Proof

Pair all nonresidue indices within their types and impose opposite relative
signs.  Each such pair costs

\[
\|d_i-d_j\|^2\le\Delta_a.
\]

Pair the designated residues arbitrarily, using a dummy zero if their
number is odd.  The number of odd types has the same parity as
\(r=\sum_ar_a\), so this is exactly the one dummy already permitted before
Theorem 6.1.  For two residues \(u,v\), choose the better relative sign:

\[
\min\{\|u+v\|^2,\|u-v\|^2\}
=\|u\|^2+\|v\|^2-2|\langle u,v\rangle|
\le\|u\|^2+\|v\|^2.
\]

The dummy pair costs the squared norm of its one real residue.  Summing
proves (6.9). \(\square\)

Thus exact shadow twins cancel at zero signing cost in pairs.  A type pays
only its within-type diameter and at most one parity residue.  This is the
promised tractable integrality lemma for growing correlated atoms.

## 7. Orbit-average implication at a global minimizer

For uniform \(\pi\), target transitivity gives

\[
\mathbb E_\pi\widetilde e_{\pi F}=0.
\]

Therefore

\[
\boxed{
\mathbb E_\pi\mathcal A_\pi
=\mathbb E_\pi\|\widetilde e_{\pi F}-\widetilde e_F\|^2
=2\|e_F\|_w^2
=2(Q_w(F)+B_w).
}
\tag{7.1}
\]

### Theorem 7.1 (paired orbit-rebalancing criterion)

Suppose \(0\le\eta<1\) and \(R_0\ge0\), and assume that for an exact factor
\(F\),

\[
\mathbb E_\pi R_{\rm pair}(F,\pi F)
\le2B_w+2\eta Q_w(F)+R_0.
\tag{7.2}
\]

Then there is a literal exact factor \(H\) with

\[
\boxed{
Q_w(H)
\le\frac{1+\eta}{2}Q_w(F)+\frac{R_0}{4}.
}
\tag{7.3}
\]

If \(F_*\) is a global minimizer of \(Q_w\) and (7.2) holds for \(F_*\),
then

\[
\boxed{
Q_w(F_*)\le\frac{R_0}{2(1-\eta)}.
}
\tag{7.4}
\]

#### Proof

Equations (7.1)--(7.2) imply

\[
\mathbb E_\pi(\mathcal A_\pi-R_{\rm pair})
\ge2(1-\eta)Q_w(F)-R_0.
\tag{7.5}
\]

For some \(\pi\), the left side is at least its average.  Apply (6.4) to
obtain (7.3).

If \(F_*\) is a global minimizer, every ownership-component signing is an
exact factor with value at least \(Q_w(F_*)\).  The antipodal identity
forces

\[
\beta_\pi=\mathcal A_\pi
\qquad\text{for every }\pi.
\tag{7.6}
\]

Since

\[
\beta_\pi\le R_{\rm pair}\le\mathcal A_\pi,
\]

all three quantities are equal at a minimizer.  Average this equality and
use (7.1)--(7.2):

\[
2(Q_w(F_*)+B_w)
\le2B_w+2\eta Q_w(F_*)+R_0.
\]

Rearranging proves (7.4). \(\square\)

For the Gaussian window, the following theorem would now suffice:

> **Unproved orbit type-capacity theorem \(\mathrm{OTC}_A\).**  For some
> \(0\le\eta_A<1\) and \(0\le C_A<\infty\), every global minimizer satisfies
> \[
> \mathbb E_\pi R_{\rm pair}(F_*,\pi F_*)
> \le2B_A+2\eta_AQ_A(F_*)+C_AH_At.
> \tag{7.7}
> \]

Theorem 7.1 would give

\[
Q_A(F_*)=O_A(H_At)=o(W),
\tag{7.8}
\]

and hence the constant-one theorem through the frozen exact-factor
transfer and diagonalization.

Corollary 6.2 reduces \(\mathrm{OTC}_A\) further to a geometric statement:
find genuine common multidepth component types whose total within-type
diameter and odd-residue cost have the right orbit average.  This is not a
generic negative-dependence assertion; every sign outcome is already an
exact factor.

Absent such an independent physical type construction, (7.7) is not a
weaker relaxation of (7.8).  At a global minimizer, pair-rigidity gives
\(R_{\rm pair}=\mathcal A_\pi\) pointwise, so (7.1) makes (7.7)
algebraically equivalent to the asserted \(O_A(H_At)\) bound.  Its new
content must therefore come from a wreath-specific application of
Corollary 6.2.

## 8. Sharp obstruction inside this circuit family

If \(\Gamma(F,\pi F)\) is connected, there is only one nonzero component.
Then

\[
\beta_\pi=R_{\rm pair}=\mathcal A_\pi,
\tag{8.1}
\]

and the only two component-side factors are \(F\) and \(\pi F\).  Both have
the same collision value.  In the floor-aware theorem, if the selected
overlay is connected, the curvature of its sole component cancels the
negative tangent exactly:

\[
2\langle h_F,u_C\rangle_w+\kappa_F(C)=0.
\tag{8.2}
\]

Thus orbit symmetry and a negative clipped-floor supporting signal do not
imply a finite integral descent.  Fragmentation into several components with a positive
covariance cut, or matched shadow types with small parity residue, is
indispensable for this route.

More generally, every global minimizer is **pair-rigid**:

\[
R_{\rm pair}(F_*,\pi F_*)=\mathcal A_\pi
\qquad\text{for every }\pi.
\tag{8.3}
\]

Therefore a failure of \(\mathrm{OTC}_A\) must exhibit a genuine wreath
factor whose orbit overlays have enough unmatched component-type cost to
absorb the complete Reynolds displacement at every permutation.

No existence theorem for such a pair-rigid wreath factor is claimed.

## 9. Independent audit and final proved/conditional boundary

The decisive formulas were independently rederived.  The audit confirmed:

1. the pointwise factor \(1/2\) in (2.3);
2. the orbit-average and component-size factor \(Q/(2t)\) in (3.6);
3. the exact curvature sign and the absence of any missing factor two in
   (4.3)--(4.10);
4. the doubled-excess antipodal gain \((\mathcal A-\beta)/4\);
5. the floor obstruction \(\beta\ge\mathcal A-4Q\);
6. the matched-pair/type-capacity bound, including the need to designate
   one bounded residue in every odd type; and
7. the global-minimizer constant \(R_0/[2(1-\eta)]\).

The following scope restrictions are essential.

* The component in Theorem 3.1 has a proved negative supporting tangent,
  but its curvature bound is unproved.
* The favorable tangent component and a favorable matched-type overlay are
  not automatically produced by the same permutation.
* \(M_{\rm pair}\) is an upper bound for the optimal signing variance; it
  is not generally equal to it.
* For an arbitrary permutation, Theorem 5.1 controls the better member of
  an antipodal pair; it is not an individual exact-energy formula for both
  antipodes.
* No physical necklace theorem proving (4.11), (4.13), or (7.7) is supplied.

Accordingly, a nonzero one-copy conformal endpoint and an exact correlated
rounding lemma are proved.  A non-orbit collision descent, and hence the
constant-one theorem, remains conditional on a sharp necklace-specific
fragmentation, curvature, or component-type-capacity estimate.
