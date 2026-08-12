# Bank-flexible fractional physicalization: exact min--max, pure saddles, and duplex exchanges

Date: 2026-07-31

Status: exact fixed-fibre and bank-flexible LP duality; exact sufficient
common-basis exchange and purification theorems; exact endpoint-run formula;
exact protected C6/rerouter envelope min--max and scalar obstruction; and a
rounded-SBE generalized-polymatroid criterion with exact ceiling
obstructions; and a literal positive repair of the authenticated
parameter-three bad basis.  No all-parameter existence of a favourable
basis is claimed.

## 0. Verdict

For a fixed oriented child forest, shore, and incidence-admissible common
basis \(Q\), the fractional physical deficiency has the compact form

\[
 \boxed{
 \rho^\sigma_\omega(Q)
 =\max_{0\le z\le1}
   \left(\tau^\sigma_{\omega,Q}(z)
         -c^\sigma_Q\mathbin{\cdot}z\right).
 }                                                       \tag{0.1}
\]

Here \(\tau_Q(z)\) is the minimum physical \(z\)-cost of an outer-perfect
diamond assignment.  Consequently

\[
 \rho(Q)=0
 \quad\Longleftrightarrow\quad
 \forall z\ \exists M_z:
 \operatorname {cost}_z(M_z)\le c_Q\mathbin{\cdot}z.   \tag{0.2}
\]

The matching \(M_z\) may depend on \(z\); the basis \(Q\) may not.

The dependence on \(Q\) can be put on one fixed dual domain.  If
\(\lambda=(a,b,z)\) is a weighted physical cut, then

\[
 L^\sigma_{\omega,Q}(\lambda)
 =\Phi^\sigma(\lambda)
  +\sum_{e\in Q}g^\sigma_{\omega,\lambda}(e),          \tag{0.3}
\]

where

\[
 g^\sigma_{\omega,\lambda}(e)
 =z_{\upsilon^\sigma(e)}-a_{\tau^\sigma_\omega(e)}.    \tag{0.4}
\]

Thus changing \(Q\) is a modular perturbation of every fixed weighted cut.

Let \({\cal B}_\omega\) be the synchronized common bases and
\({\cal P}_\omega=\operatorname {conv}\{\mathbf1_Q:Q\in{\cal B}_\omega\}\).
The exact two-shore fractional bank relaxation is

\[
\boxed{
\begin{aligned}
 \bar\rho_\omega
 &=\min_{x\in{\cal P}_\omega}
   \left(\rho^-_\omega(x)+\rho^+_\omega(x)\right)\\
 &=\max_{\lambda^-,\lambda^+}
 \left[
   \Phi^-(\lambda^-)+\Phi^+(\lambda^+)
   +\min_{Q\in{\cal B}_\omega}
      \sum_{e\in Q}
       \left(g^-_{\omega,\lambda^-}(e)
            +g^+_{\omega,\lambda^+}(e)\right)
 \right].
                                                               \tag{0.5}
\end{aligned}}
\]

A positive value in (0.5) is one exact pair of weighted cuts excluding
every common basis for that orientation.  Value zero is only a fractional
mixed-bank conclusion.

A pure basis follows under either of two proved sufficient conditions.

1. A **pure saddle**: dual optimizers for one integral \(Q\) have combined
   modular weight for which \(Q\) is a minimum-weight common basis.
2. **Joint-fibre purification**: every nonintegral zero-dummy point admits a
   two-sided common-base exchange direction with compatible physical
   circulations.

The first is certified by weighted matroid intersection; the second is an
explicit exchange-direction condition on the joint polytope.

Strict balanced expansion supplies the constant point
\(x_e=C/N\) in the common-base polytope.  It does not supply the owner rows.
Adding all weighted physical-cut inequalities at that constant point gives
the exact stronger condition called diamond-SBE below.  Diamond-SBE proves
\(\bar\rho_\omega=0\), but a pure basis still needs one of the purification
conditions.

The published parameter-three basis with \(\rho=1\) is not a bank-wide
obstruction.  On the same child and orientation, the common basis retaining
\(31\to32\) has integral capacity-safe assignments on both shores, hence

\[
                         \rho^-(Q_*)=\rho^+(Q_*)=0.   \tag{0.6}
\]

Both physical supports are in fact no-empty path forests.  The repair is a
literal synchronized basis exchange plus a nonlocal assignment chain.

Finally, a two-element rank-one example proves that a balanced fractional
point, all weighted cuts, and connected basis exchange do not imply a pure
basis.  It is an abstract purification obstruction, not a Boolean-diamond
counterexample.  There is, however, a literal Boolean obstruction to one
stronger bank quantifier: an arbitrary prescribed \(o(P)\) bank of mutually
private, independently phase-flexible sparse rerouters cannot always be
preserved by one static exterior.  A full C6 has zero scalar
reserve-envelope tax, whereas a live sparse \(2\ell\)-cycle costs \(\ell\)
units of the exact total owner slack \(2P/n\).  Prephasing, serialization,
bank thinning, or correlated overlapping realizations evade the literal
scope of this no-go.  The all-parameter existential Boolean common-basis
theorem remains open.

At the orientation layer, the exact SBE right side

\[
 g(A)=N|\{o:N(o)\subseteq A\}|-R|A|
\]

is supermodular, but \(\lceil g/C\rceil\) need not be.  A four-endpoint
singleton-neighbourhood example and the literal parameter-three Catalan
forest both have a feasible half-endpoint point and no integral
orientation.  A positive generalized-polymatroid theorem does survive when
the rounded shore demands are supermodular and cross-paramodular: then
existence reduces exactly to their incident-path Hall cuts.  Protected
common-basis donors and \(\rho=0\) remain later, correlated rows.

## 1. Fixed data and suppressed indices

Use

\[
 M=\binom{2n}{n},\qquad
 N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},
\]

\[
 K=\operatorname {Cat}_n,\qquad
 C=\operatorname {Cat}_{n+1},\qquad
 R=N-C=P-K.                                           \tag{1.1}
\]

Let \(F\) be an undirected Catalan path forest and let \(\omega\) be one
coherent orientation of each path.  Its edge ground \(E=E(F)\) has order
\(N\).  For the two shores write

\[
 \tau^-_\omega(e)=t_\omega(e),\qquad
 \tau^+_\omega(e)=h_\omega(e),                       \tag{1.2}
\]

for the punctured endpoint labels, and

\[
 \upsilon^-(e)=U_e,\qquad
 \upsilon^+(e)=L_e                                   \tag{1.3}
\]

for the physical anchor labels.  Complementation puts the lower shore in
the same formal rank convention as the upper shore.  Each endpoint map in
(1.2) is injective and each anchor map in (1.3) is a bijection onto the
corresponding \(N\)-element physical-owner shore.

Let \({\cal B}_\omega\) be the family of \(C\)-element sets which are bases
of both pulled-back strict incidence matroids.  Only

\[
                         Q\in{\cal B}_\omega          \tag{1.4}
\]

is considered below.  If \(Q\) is not incidence-admissible, owner dummy
capacity cannot repair the missing outer incidence; the appropriate value
of \(\rho\) is \(+\infty\).

For an integral \(Q\), the punctured lower demand on shore \(\sigma\) is
zero at \(\tau^\sigma_\omega(e)\) for \(e\in Q\), one at every other
endpoint-image member, and one at every terminal endpoint outside the
image.  The physical capacity is

\[
 c^\sigma_Q(x)
 =2-\mathbf1\{x\in\upsilon^\sigma(Q)\}.              \tag{1.5}
\]

Thus \(\rho\) is really

\[
                         \rho^\sigma_{F,\omega}(Q),  \tag{1.6}
\]

not a function of an abstract edge subset alone.  Orientation changes the
punctured endpoints and the common-base family, although the anchor maps
are orientation invariant.

## 2. Elimination of the fixed-\(Q\) dual

Fix one shore and suppress \(\sigma,\omega\).  Let
\({\cal W}_Q\) be the fractional outer-perfect assignment polytope on
candidate diamonds \(e=(D,V)\), \(D\subset V\).  For
\(w\in{\cal W}_Q\), define the physical load

\[
 \ell_x(w)=\sum_{e:x\in p(e)}w_e.                    \tag{2.1}
\]

### Theorem 2.1 (price form of fractional deficiency)

\[
\boxed{
\begin{aligned}
 \rho(Q)
 &=\min_{w\in{\cal W}_Q}
      \sum_x\bigl(\ell_x(w)-c_Q(x)\bigr)_+\\
 &=\max_{0\le z\le1}
      \left(\tau_Q(z)-c_Q\mathbin{\cdot}z\right),
                                                               \tag{2.2}\\
 \tau_Q(z)
 &=\min_{M:D_Q\longrightarrow{\cal V}\ {\rm perfect}}
      \sum_{(D,V)\in M}\left(z_{x_{D,V}}+z_{y_{D,V}}\right).
\end{aligned}}
\]

The minimum defining \(\tau_Q\) may equivalently be taken over fractional
outer-perfect assignments.

#### Proof

For fixed \(w\), the least artificial capacity at owner \(x\) is
\((\ell_x(w)-c_Q(x))_+\), proving the first line.

For the weighted dual in item 2302ROOT, fix \(z\).  Maximizing
\(\sum_Da_D+\sum_Vb_V\) subject to

\[
 a_D+b_V\le z_{x_{D,V}}+z_{y_{D,V}}                 \tag{2.3}
\]

is the dual of the minimum-cost perfect assignment from \(D_Q\) to
\({\cal V}\).  The assignment polytope is integral, so its integral and
fractional optima agree.  Maximizing next over \(0\le z\le1\) gives (2.2)
by finite-dimensional LP duality. \(\square\)

### Corollary 2.2 (weakest exact fixed-fibre criterion)

For an admissible \(Q\), the following are equivalent.

1. \(\rho(Q)=0\).
2. Some \(w\in{\cal W}_Q\) satisfies \(\ell(w)\le c_Q\)
   coordinatewise.
3. For every \(z\in[0,1]^{\cal X}\),
   \[
                 \tau_Q(z)\le c_Q\mathbin{\cdot}z.   \tag{2.4}
   \]
4. Every weighted dual expression in item 2302ROOT is nonpositive.

The quantifiers in item 3 are

\[
                         \forall z\ \exists M_z.     \tag{2.5}
\]

Indicator prices \(z=\mathbf1_S\) recover ordinary host cuts, but do not
in general suffice: the concave piecewise-linear function
\(\tau_Q(z)-c_Q\mathbin{\cdot}z\) may attain its maximum at a fractional
price.

Geometrically, if \(d(M)\) is the physical load vector of an outer-perfect
assignment, then

\[
 \rho(Q)=
 \min_{d\in\operatorname {conv}\{d(M)\}}
          \sum_x(d_x-c_Q(x))_+,                     \tag{2.6}
\]

and

\[
 \rho(Q)=0
 \quad\Longleftrightarrow\quad
 c_Q\in
 \operatorname {conv}\{d(M)\}+\mathbb R_+^{\cal X}. \tag{2.7}
\]

### Corollary 2.3 (the obstruction is spatial)

At \(z=\mathbf1\),

\[
 c_Q\mathbin{\cdot}\mathbf1-\tau_Q(\mathbf1)
 =(2N-C)-2P=C-2K={2P\over n}>0.                     \tag{2.8}
\]

Every outer-perfect assignment uses exactly \(2P\) physical incidences.
Thus positive deficiency can only come from a spatial weighted cut, never
from total owner capacity.

## 3. One fixed dual domain for every basis

Retain all \(M\) central \(D\)-rows, including those deleted by \(Q\), and
give a deleted row demand zero.  Let \(\Lambda^\sigma_\omega\) be the
polyhedron of triples \(\lambda=(a,b,z)\) satisfying

\[
 a_D+b_V\le z_{x_{D,V}}+z_{y_{D,V}}
 \quad\text{for every Boolean diamond},\qquad
 0\le z_x\le1.                                      \tag{3.1}
\]

Put

\[
 \Phi^\sigma(\lambda)
 =\sum_{D\in{\cal X}_n}a_D+\sum_Vb_V-2\sum_xz_x,    \tag{3.2}
\]

\[
 g^\sigma_{\omega,\lambda}(e)
 =z_{\upsilon^\sigma(e)}
  -a_{\tau^\sigma_\omega(e)}.                       \tag{3.3}
\]

### Theorem 3.1 (affine bank dependence)

For every \(Q\in{\cal B}_\omega\),

\[
 \boxed{
 \rho^\sigma_\omega(Q)
 =\max_{\lambda\in\Lambda^\sigma_\omega}
   \left[
     \Phi^\sigma(\lambda)
     +\sum_{e\in Q}g^\sigma_{\omega,\lambda}(e)
   \right].
 }                                                   \tag{3.4}
\]

If \(Q'=Q-q+r\) is another common basis, then for every fixed
\(\lambda\),

\[
\begin{aligned}
 L^\sigma_{\omega,Q'}(\lambda)
 -L^\sigma_{\omega,Q}(\lambda)
 &=
 z_{\upsilon^\sigma(r)}
 -a_{\tau^\sigma_\omega(r)}\\
 &\quad
 -z_{\upsilon^\sigma(q)}
 +a_{\tau^\sigma_\omega(q)}.                        \tag{3.5}
\end{aligned}
\]

#### Proof

The demand coefficient of \(a_{\tau(e)}\) is
\(1-\mathbf1_Q(e)\), while the capacity at
\(\upsilon(e)\) is \(2-\mathbf1_Q(e)\).  Expanding the fixed-domain dual
objective gives exactly (3.2)--(3.4).  A deleted zero-demand row causes no
restriction: its free \(a_D\) may be made sufficiently negative.  Formula
(3.5) is the difference of the two modular sums. \(\square\)

The formula explains why ordinary common-basis connectivity is not by
itself a physical descent theorem.  Replacing one punctured row may force
an assignment alternating path of unbounded length; the modular dual
change is local, while the primal rerouting need not be.

## 4. Exact bank-flexible fractional min--max

For \(x\in{\cal P}_\omega\), replace every bank indicator in the demand and
capacity formulas by \(x_e\).  Let
\(\rho^\sigma_\omega(x)\) be the resulting fractional dummy optimum.

### Theorem 4.1 (two-shore bank min--max)

\[
\boxed{
\begin{aligned}
 \bar\rho_\omega
 &:=
 \min_{x\in{\cal P}_\omega}
       \left(\rho^-_\omega(x)+\rho^+_\omega(x)\right)\\
 &=
 \max_{\lambda^-\in\Lambda^-_\omega,\,
       \lambda^+\in\Lambda^+_\omega}
 \left[
   \Phi^-(\lambda^-)+\Phi^+(\lambda^+)
   +\min_{Q\in{\cal B}_\omega}
      \sum_{e\in Q}
       \left(
        g^-_{\omega,\lambda^-}(e)
        +g^+_{\omega,\lambda^+}(e)
       \right)
 \right].
                                                               \tag{4.1}
\end{aligned}}
\]

#### Proof

Jointly minimize total dummy mass over

\[
 x\in{\cal P}_\omega,\qquad
 w^-,w^+,\qquad s^-,s^+.
\]

All demand, capacity and assignment rows are linear.  Dualizing the two
physical flow systems gives the affine expression

\[
 \Phi^-(\lambda^-)+\Phi^+(\lambda^+)
 +\sum_e x_e\left(g^-_{\lambda^-}(e)+g^+_{\lambda^+}(e)\right).
                                                               \tag{4.2}
\]

LP strong duality permits minimization over \(x\) after the physical duals
are chosen.  Since \({\cal P}_\omega\) is the convex hull of incidence
vectors of synchronized common bases, a linear minimum over it is the
minimum common-basis weight displayed in (4.1). \(\square\)

### Corollary 4.2 (one universal bank cut)

If the right side of (4.1) is positive, one pair of weighted physical cuts,
together with a minimum-weight common-basis certificate, excludes every
\(Q\in{\cal B}_\omega\).

If it is zero, a zero-dummy fractional \(x\in{\cal P}_\omega\) exists.
This does not imply that any integral common basis has zero dummy.

The exact pure target, allowing orientation, is

\[
 \boxed{
 \min_{\omega\ {\rm coherent}}
 \min_{Q\in{\cal B}_\omega}
 \max_{\sigma\in\{-,+\}}
 \max_{0\le z\le1}
 \left[
   \tau^\sigma_{\omega,Q}(z)
   -c^\sigma_Q\mathbin{\cdot}z
 \right]
 =0.
 }                                                     \tag{4.3}
\]

The order in (4.3) is load-bearing: \(\omega,Q\) precede the adversarial
price, while the assignment attaining \(\tau_Q(z)\) may depend on that
price.

## 5. Strict balanced expansion and diamond-SBE

Put

\[
                         \theta={C\over N},\qquad
                         x_0=\theta\mathbf1_E.        \tag{5.1}
\]

Strict balanced expansion on both shores is exactly the assertion

\[
                         x_0\in{\cal P}_\omega.       \tag{5.2}
\]

At this point the endpoint-image demand on either shore is \(1-\theta=R/N\),
every terminal demand is one, and every owner capacity is \(2-\theta\).

### Definition 5.1 (diamond-SBE)

The oriented forest is diamond-SBE on shore \(\sigma\) when

\[
 \Phi^\sigma(\lambda)
 +\theta\sum_{e\in E}g^\sigma_{\omega,\lambda}(e)
 \le0
 \qquad(\lambda\in\Lambda^\sigma_\omega).            \tag{5.3}
\]

Equivalently, the averaged endpoint demands admit one fractional
outer-perfect physical flow whose owner load is at most \(2-\theta\)
everywhere.

### Theorem 5.2 (balanced physical implication)

If an orientation is SBE on both shores and diamond-SBE on both shores,
then

\[
                         \bar\rho_\omega=0.           \tag{5.4}
\]

#### Proof

SBE puts \(x_0\) in the common-base polytope.  Diamond-SBE says that the
two dummy objectives at this feasible point are zero.  Hence the minimum
in (4.1) is at most zero.  Dummy mass is nonnegative, so it equals zero.
\(\square\)

Physical feasibility projects to the strict incidence flow, so
diamond-SBE is stronger than ordinary SBE.  SBE alone supplies a
distribution on common bases with one-point marginals \(\theta\).  It
averages the capacity price exactly:

\[
 \mathbb E[c_Q^\sigma\mathbin{\cdot}z]
 =(2-\theta)\sum_xz_x.                              \tag{5.5}
\]

It does not control the nonlinear assignment term
\(\tau^\sigma_{\omega,Q}(z)\), nor may expectation be interchanged with
\(\max_z\).  Even pointwise average inequalities for every fixed \(z\)
would give only a mixed-bank strategy.

## 6. A sufficient common-basis exchange theorem

For one integral \(Q\), choose dual optimizers
\(\lambda^-_Q,\lambda^+_Q\) in (3.4), and put

\[
 g_Q(e)=
 g^-_{\omega,\lambda^-_Q}(e)
 +g^+_{\omega,\lambda^+_Q}(e).                      \tag{6.1}
\]

### Theorem 6.1 (pure-saddle criterion)

Suppose \(Q\in{\cal B}_\omega\) is a minimum-weight synchronized common
basis for \(g_Q\).  Then

\[
 \boxed{
 \rho^-_\omega(Q)+\rho^+_\omega(Q)=\bar\rho_\omega.
 }                                                   \tag{6.2}
\]

In particular, if diamond-SBE gives \(\bar\rho_\omega=0\), then this
integral \(Q\) satisfies

\[
                         \rho^-_\omega(Q)
                         =\rho^+_\omega(Q)=0.         \tag{6.3}
\]

#### Proof

Let \(\Phi_Q=\Phi^-(\lambda^-_Q)+\Phi^+(\lambda^+_Q)\).
Dual optimality at \(Q\) and the minimum-weight premise give

\[
\begin{aligned}
 \rho^-_\omega(Q)+\rho^+_\omega(Q)
 &=\Phi_Q+g_Q(Q)\\
 &=\Phi_Q+\min_{B\in{\cal B}_\omega}g_Q(B)\\
 &\le\bar\rho_\omega.
                                                               \tag{6.4}
\end{aligned}
\]

Conversely \(Q\) is a feasible point of the minimization defining
\(\bar\rho_\omega\), so
\(\bar\rho_\omega\le\rho^-_\omega(Q)+\rho^+_\omega(Q)\).
This proves equality.  Each shore deficiency is nonnegative, giving
(6.3). \(\square\)

The minimum-weight premise has the standard no-negative-exchange-cycle
certificate from weighted matroid intersection.  The following stronger
condition is elementary and often easier to check.

### Corollary 6.2 (one-constituent fundamental-circuit certificate)

Let \({\cal M}_1,{\cal M}_2\) be the two constituent matroids.  If, for
one \(i\in\{1,2\}\),

\[
 g_Q(e)\le g_Q(f)
 \quad
 \text{for every }f\notin Q,\ 
 e\in C_i(f,Q)\setminus\{f\},                       \tag{6.5}
\]

then \(Q\) is a minimum-weight base of \({\cal M}_i\), hence a
minimum-weight synchronized common basis.  Theorem 6.1 applies.

Thus (6.5), together with an optimal physical cut, is one exact sufficient
common-basis exchange condition.  If
\(\bar\rho_\omega=0\) but an integral \(Q\) is deficient, no combined dual
optimizer at \(Q\) can satisfy the minimum-weight condition.  Weighted
matroid intersection then exposes a negative common-basis exchange packet.
Such a packet breaks the current active cut; it need not decrease the new
maximum after the dual optimizer changes.

## 7. Joint-fibre purification

The pure-saddle theorem is dual.  There is a complementary primal
sufficient condition.

Let \({\cal Z}_\omega\) be the zero-dummy joint polytope of triples

\[
                   (x,w^-,w^+),\qquad x\in{\cal P}_\omega,       \tag{7.1}
\]

with the affine endpoint demands, all outer equalities, and owner loads at
most the affine capacities \(2-x_e\).

### Definition 7.1 (two-sided fibre-exchange property)

The polytope has the two-sided fibre-exchange property when every feasible
point with nonintegral \(x\) admits a nonzero direction

\[
                         (d,h^-,h^+)                \tag{7.2}
\]

and some \(\varepsilon>0\) such that both signs remain feasible.  Explicitly,

\[
 x\pm\varepsilon d\in{\cal P}_\omega,\qquad
 w^\sigma\pm\varepsilon h^\sigma\ge0,                \tag{7.3}
\]

\[
 \sum_Vh^\sigma_{D,V}
 =-\!\!\sum_{\tau^\sigma_\omega(e)=D}d_e,\qquad
 \sum_Dh^\sigma_{D,V}=0,                             \tag{7.4}
\]

and at every tight owner row

\[
 \sum_{D,V:x\in p(D,V)}h^\sigma_{D,V}
 +\!\!\sum_{\upsilon^\sigma(e)=x}d_e=0.              \tag{7.5}
\]

### Theorem 7.2 (purification by fibre exchanges)

If \({\cal Z}_\omega\) is nonempty and has the two-sided fibre-exchange
property, then it contains a point with integral \(x=\mathbf1_Q\).
Consequently some synchronized common basis has

\[
                         \rho^-_\omega(Q)
                         =\rho^+_\omega(Q)=0.         \tag{7.6}
\]

#### Proof

Take a vertex of \({\cal Z}_\omega\).  If its \(x\)-coordinate were
nonintegral, (7.2)--(7.5) would express it as the midpoint of two distinct
feasible points, contradicting extremality.  Thus \(x\) is integral.
Since \({\cal P}_\omega\) is the common-base polytope, it is the incidence
vector of a synchronized common basis.  The two associated flows prove
(7.6). \(\square\)

This is a genuine strengthening of ordinary common-basis exchange.
Equations (7.4)--(7.5) require every bank move to lift simultaneously to
assignment circulations on both shores.  A failure is a locked fractional
vertex supported by active weighted physical cuts.

## 8. Preserving a planted C6 and sparse-cycle bank

The bank has two logically different protection requirements.

* **Puncture protection:** specified child edges are forced into or excluded
  from the common basis.
* **Physical phase protection:** the exterior matching must leave enough
  outer rows and owner slots to install any declared packet phase.

One-point marginals settle neither requirement simultaneously.

### 8.1 The exact protected common-basis face

Fix an orientation.  Let \(I_{\cal A},Z_{\cal A}\subseteq E(F)\) be
disjoint.  Edges in \(I_{\cal A}\) are forced into \(Q\); edges in
\(Z_{\cal A}\) are forbidden.  For a packet whose lower colours must remain
unpunctured, \(Z_{\cal A}\) contains their preimages under the appropriate
injective endpoint map.  Put

\[
 E'=E\setminus(I_{\cal A}\cup Z_{\cal A}),\qquad
 {\cal B}_{\omega,{\cal A}}
 =\{Q\in{\cal B}_\omega:
       I_{\cal A}\subseteq Q\subseteq E\setminus Z_{\cal A}\}.
                                                               \tag{8.1}
\]

### Theorem 8.1 (forced--forbidden common-basis cut)

Let \({\cal M}_1,{\cal M}_2\) be the two strict incidence matroids.  The
family (8.1) is nonempty if and only if \(I_{\cal A}\) is independent in
both matroids and, for every \(S\subseteq E'\),

\[
 \boxed{
 r_{({\cal M}_1/I_{\cal A})|E'}(S)
 +r_{({\cal M}_2/I_{\cal A})|E'}(E'\setminus S)
 \ge C-|I_{\cal A}|.
 }                                                             \tag{8.2}
\]

Thus the two minors are unambiguously
\(({\cal M}_i/I_{\cal A})|E'=({\cal M}_i/I_{\cal A})\setminus
Z_{\cal A}\).

#### Proof

Contract \(I_{\cal A}\) in both matroids and restrict their common ground to
\(E'\).  A protected basis is exactly a common independent set of order
\(C-|I_{\cal A}|\) in these two minors.  Edmonds' common-independent-set
min--max is precisely (8.2). \(\square\)

For the risk-only case \(I_{\cal A}=\varnothing\), put

\[
 \theta={C\over N},\qquad
 \delta_i(S)=r_i(S)-\theta|S|.                                \tag{8.3}
\]

Then (8.2) is equivalent to

\[
 \delta_1(S)+\delta_2(E'\setminus S)
 \ge\theta|Z_{\cal A}|.                                      \tag{8.4}
\]

Ordinary SBE gives only the two nonnegative terms separately; it does not
give the extra margin on the right of (8.4).  Its uniform common-basis
measure gives only

\[
                  {\mathbb E}|Q\cap Z_{\cal A}|
                  =\theta|Z_{\cal A}|.                         \tag{8.5}
\]

If an SBE distribution with these marginals exists and the right side is
below one, the integer random variable \(|Q\cap Z_{\cal A}|\) has expectation
below one, so some basis avoids \(Z_{\cal A}\).  For a general \(o(P)\) bank
the same calculation merely bounds the expected number of punctured packet
incidences and supplies no all-packet cylinder event.

### 8.2 Exact phase envelopes and their dual price

Work on one physical shore.  A phase-flexible block \(b\) consists of
matchings \(S_b^s\), indexed by its allowed phases \(s\), such that every
phase covers the same lower bank \(L_b\) and upper bank \(U_b\) exactly
once.  Write

\[
 |L_b|=|U_b|=m_b,\qquad
 h_b^s(x)=\text{slot load of phase \(s\) at owner \(x\)},       \tag{8.6}
\]

and reserve the literal-slot envelope.  In the occurrence-labelled model,
\(r_b(x)\) is the number of distinct literal slots at owner \(x\) appearing
in the union of all phases:

\[
 r_b(x)=
 \left|\bigcup_s\{\text{literal slots at \(x\) used by }S_b^s\}\right|.
                                                                  \tag{8.7}
\]

In the unlabelled fractional owner model this may be replaced by
\(\max_s h_b^s(x)\).  The two expressions agree for slot-aligned phases.
The suspended C6 uses the same six literal slots in both full phases; the
sparse rerouter is aligned at each common \(H_i\), while its \(P_i,Q_i\)
owners are distinct.

Banks are assumed pairwise disjoint in their outer rows and literal
reserved resources.  Every row in \(L_b\) must have ordinary demand one for
every \(Q\) in the protected face; in particular all endpoint preimages
whose puncture would delete such a demand belong to \(Z_{\cal A}\).

The quantifier in this section is **static robust phase flexibility**: one
exterior solution must support every allowed packet phase without being
reoptimized.  The exterior LP gives demand zero to all rows in
\(L_b\cup U_b\) and capacity \(c_Q-r_b\) at each owner.  Therefore an
exterior solution plus any chosen \(S_b^s\) is outer-perfect and
capacity-safe.  If the exterior may instead be reoptimized after a phase is
chosen, the envelope construction remains sufficient but need not be
necessary.

For the gain-one C6, this statement is applied to the *full*
three-against-three identity:
exterior plus the two-atom off state is the declared one-target leave,
while exterior plus the three-atom on state is full.  Preloading only the
two off atoms and calling the residual LP outer-perfect would be false.

For a dual \(\lambda=(a,b,z)\), define

\[
 \boxed{
 \kappa_b(\lambda)
 =\sum_xr_b(x)z_x
  -\sum_{D\in L_b}a_D
  -\sum_{V\in U_b}b_V.
 }                                                             \tag{8.8}
\]

This price is phase-independent and nonnegative.  Indeed, for every phase,

\[
\begin{aligned}
 \kappa_b(\lambda)
 &=\sum_{e=(D,V)\in S_b^s}
       \bigl(z_{x_e}+z_{y_e}-a_D-b_V\bigr)\\
 &\quad+
   \sum_x\bigl(r_b(x)-h_b^s(x)\bigr)z_x\ge0,                  \tag{8.9}
\end{aligned}
\]

by the diamond dual inequalities and \(z\ge0\).

Let \(\kappa_{\cal A}^\sigma=\sum_{b\in{\cal A}}\kappa_b^\sigma\).
On the unchanged full dual domain, the exact protected mixed optimum is

\[
\boxed{
\begin{aligned}
 \bar\rho_{\omega,{\cal A}}
 =\max_{\lambda^-,\lambda^+}
 \bigg[
 &\Phi^-(\lambda^-)+\kappa^-_{\cal A}(\lambda^-)
  +\Phi^+(\lambda^+)+\kappa^+_{\cal A}(\lambda^+)\\
 &+\min_{Q\in{\cal B}_{\omega,{\cal A}}}
    \sum_{e\in Q}
      \left(g^-_{\lambda^-}(e)+g^+_{\lambda^+}(e)\right)
 \bigg].                                                       \tag{8.10}
\end{aligned}}
\]

#### Proof

Deleting the common outer banks subtracts their \(a\)- and \(b\)-prices
from the dual objective.  Reserving \(r_b\) changes \(-c_Q\cdot z\) by
\(+r_b\cdot z\), giving (8.8).  Summing over disjoint blocks and applying
the minimax proof of Theorem 4.1 on the protected common-base face gives
(8.10). \(\square\)

A positive value in (8.10), together with a minimum-weight common-basis
certificate in the minors of Theorem 8.1, is one exact universal cut
excluding every protected \(Q\) for that orientation.  The existential
orientation quantifier must remain outside: one needs *some* orientation
whose protected value is zero and whose relaxation purifies.  Interchanging
that choice with the adversarial cuts proves only a mixed-orientation
statement.

### 8.3 The exact owner-envelope obstruction

At \(a_D=b_V=z_x=1\), or directly by counting total residual capacity,
(8.10) gives the necessary inequality, separately on each physical shore,

\[
 \boxed{
 \sum_{b\in{\cal A}}
       \bigl(\|r_b\|_1-2m_b\bigr)
 \le (2N-C)-2P={2P\over n}.
 }                                                             \tag{8.11}
\]

A full suspended C6 phase has \(m_b=3\) and the same six literal slots in
both phases, so its **scalar** envelope contribution is \(6-6=0\).
Its spatial cut price \(\kappa_b(\lambda)\) need not vanish.  A
phase-flexible sparse
\(2\ell\)-cycle has \(m_b=\ell\) and envelope
\(\{H_i,P_i,Q_i:i\in\mathbb Z_\ell\}\), hence contributes

\[
                            3\ell-2\ell=\ell.                  \tag{8.12}
\]

Consequently at most \(2P/(n\ell)\) mutually private sparse rerouters can
remain simultaneously independently phase-flexible under one static
exterior.  This is a hard total-capacity cut, not a weakness of rounding.

### Theorem 8.2 (a literal Boolean \(o(P)\)-bank obstruction)

Fix \(\ell\ge5\).  For all sufficiently large \(n\ge2\ell-2\), the Boolean
rank-\(n\)/rank-\(n+2\) host contains a pairwise-resource-disjoint prescribed
bank of

\[
                 T=\left\lceil{3P\over\ell n}\right\rceil=o(P) \tag{8.13}
\]

sparse \(2\ell\)-cycle envelopes, but there is no feasible pair consisting
of a common basis and one static exterior matching which keeps all \(T\)
blocks independently phase-flexible.

#### Proof

Take the full symmetric-group orbit \({\cal O}\) of one sparse-cycle
envelope.  Each member uses \(\ell\) lower rows, \(\ell\) upper rows, and
\(3\ell\) owner slots.  Transitivity gives resource degrees

\[
 {\ell|{\cal O}|\over M},\qquad
 {\ell|{\cal O}|\over P},\qquad
 {3\ell|{\cal O}|\over N}.                                   \tag{8.14}
\]

The envelope-intersection graph therefore has

\[
 \Delta+1
 < {\ell^2|{\cal O}|\over M}
   +{\ell^2|{\cal O}|\over P}
   +{9\ell^2|{\cal O}|\over N}
 \le {11\ell^2|{\cal O}|\over P}.                            \tag{8.15}
\]

A greedy independent set has more than \(P/(11\ell^2)\) envelopes.  For
fixed \(\ell\) and sufficiently large \(n>33\ell\), this exceeds \(T\).
But (8.12)--(8.13) give
\(\ell T\ge3P/n>2P/n\), contradicting (8.11). \(\square\)

Preselecting one sparse-cycle phase reserves only its \(2\ell\) actually
used slots and removes this scalar obstruction.  It also removes the right
to toggle the block later.  Bank thinning, correlated overlapping
realizations, or serializing a reroute by an exterior zero-boundary
circulation are other possible escapes.  Those circulation columns are
useful purification directions, but they are not a simultaneously live
private bank.

### 8.4 Protected purification and exact rerouter span

Suppose the face (8.1) is nonempty and the protected mixed value (8.10) is
zero.  Either of the following independently suffices for a pure protected
basis.

1. For some integral protected \(Q\), take its two optimal protected duals.
   If \(Q\) is a minimum-weight basis of \({\cal B}_{\omega,{\cal A}}\) for
   their combined modular weight, then the proof of Theorem 6.1 gives
   \(\rho^-_{\cal A}(Q)=\rho^+_{\cal A}(Q)=0\).
2. At every feasible point of the protected zero-dummy polytope whose
   common-basis coordinate is nonintegral there is a nonzero direction
   (7.2)--(7.5) with

   \[
             d_e=0\quad(e\in I_{\cal A}\cup Z_{\cal A}),       \tag{8.16}
   \]

   and exterior physical lifts \(h^\sigma\) which vanish on all protected
   outer rows and on every exterior atom column meeting a reserved slot.
   Then the vertex proof of Theorem 7.2 yields an integral protected \(Q\).

The first condition has the ordinary weighted matroid-intersection
no-negative-cycle certificate in the contracted/deleted minors.  The second
can instead be formulated in the enlarged exterior-plus-packet polytope:
there a sparse-cycle phase difference may be added as a
zero-outer-boundary circulation, but only when its owner-slot change is
feasible against the exterior.

Equivalently, at a fractional zero-dummy point let \(T\) be the tangent
space of the minimal protected common-base face.  On one shore a direction
\(d\in T\) has a physical lift exactly when it annihilates every active
equality potential:

\[
 \sum_e\bigl(z_{\upsilon(e)}-a_{\tau(e)}\bigr)d_e=0,            \tag{8.17}
\]

Here the equality potentials are unrestricted real left-null potentials:
\(a_D+b_V=z_x+z_y\) on the positive atom support, \(z_x=0\) on every slack
owner row, and the physical circulation is zero on every forbidden literal
slot column.  This is the Fredholm alternative for (7.4)--(7.5), not a
restriction to nonnegative dual prices.
A nonzero direction in the common kernel for both shores proves that the
point is not extreme.  A full-rank active-gradient system is the exact
fractional locking obstruction.

The two planted packet types play different roles in this derivative
system.  A full suspended-C6 toggle has zero signed boundary on both outer
palettes and on every literal slot.  Its phase difference is consequently
invisible to every weighted \(\rho\)-cut: it can fill its prealigned one-atom
leave or change topology, but it cannot correct a positive fixed-\(Q\)
fractional cut.

For a sparse \(2\ell\)-cycle, the common owners \(H_i\) cancel between its
two phases and the signed owner vector is

\[
             b_j=\sum_{i\in\mathbb Z_\ell}
                    (\mathbf1_{Q_i}-\mathbf1_{P_i}).             \tag{8.18}
\]

Suppose a protected common-base tangent \(d\) is first routed through the
outer assignment equalities by some \(h_0\).  Its residual imbalance on a
tight owner is

\[
 \beta_x=\operatorname {load}_x(h_0)
          +\sum_{\upsilon(e)=x}d_e.                              \tag{8.19}
\]

The available sparse rerouter catalogue lifts this particular tangent if
and only if \(-\beta\) belongs to the guarded signed span of the vectors
\(b_j\), with coefficients respecting phase nonnegativity and resource
privacy, simultaneously on both shores.  Necessity is the tight-owner
derivative equation (7.5); sufficiency follows by adding the corresponding
zero-outer-boundary rerouter circulations to \(h_0\).  This is the exact
finite circulation test behind the phrase “rerouters aid purification.”
It is not implied by the number of catalogue members.

### 8.5 Soft preservation is a configuration polytope

Fix \(\omega\).  If losing a small part of the bank is allowed, a
configuration is a pair \((Q,J)\), where \(J\subseteq{\cal A}\) is the set
of packets kept, all their protected-face conditions hold, and their
envelopes are reserved.  The correct fixed-orientation relaxation is

\[
 {\cal K}_{\omega,{\cal A}}
 =\operatorname {conv}\{(\mathbf1_Q,\mathbf1_J):
                         (Q,J)\text{ is a configuration at }\omega\}.
                                                                  \tag{8.20}
\]

Pairwise inequalities such as \(y_b+x_e\le1\) do not describe this hull;
they miss joint cylinder locks.  With packet weights \(w_b\) and loss budget
\(L\), the exact mixed min--max adds

\[
 \sum_{b\in J}\kappa_b^-(\lambda^-)
 +\sum_{b\in J}\kappa_b^+(\lambda^+)                          \tag{8.21}
\]

to the full modular weight

\[
 \Phi^-(\lambda^-)+\Phi^+(\lambda^+)
 +\sum_{e\in Q}\bigl(g_e^-(\lambda^-)+g_e^+(\lambda^+)\bigr)   \tag{8.22}
\]

and minimizes over configurations satisfying
\(\sum_bw_b(1-\mathbf1_J(b))\le L\).  Purification again requires a pure
saddle or configuration-exchange circulation.  Ordinary one-point
marginals control only the expected number of invalid incidences; they do
not put an averaged pair in (8.20), impose \(\rho=0\), or preserve every
packet.

To choose \(\omega\) as well, either keep the existential orientation
outside this fixed-\(\omega\) min--max, or use a lifted disjunctive
configuration polytope with orientation atoms and correlated physical-flow
variables.  Projecting away \(\omega\) is invalid because endpoint maps,
packet legality, and the weights \(g_{\omega,e}\) depend on it.

Finally, every conclusion in this section is fractional palette/capacity
physicalization.  The local C6 and sparse-cycle phases are physical forests,
but their union with an exterior forest can create a quotient cycle.  Full
acyclicity requires the existing contracted-graphic/Rado ear cuts after the
exterior scaffold is fixed.  The ambient rank bound of item 2302R does not
make those protected graphic cuts automatic.

## 9. Coherent orientation is a run-boundary system

Fix a child path

\[
                         v_0,v_1,\ldots,v_m          \tag{9.1}
\]

and index its edges by \(e_i=v_{i-1}v_i\).  Let
\(I=\{i:e_i\in Q\}\).  For one upper-shore dual, reversing the path changes
the \(Q\)-dependent dual cost by

\[
 \sum_{i\in I}\left(a_{v_{i-1}}-a_{v_i}\right)
 =
 \sum_{\substack{[r,s]\ {\rm maximal}\\Q\text{-run}}}
      \left(a_{v_{r-1}}-a_{v_s}\right).              \tag{9.2}
\]

The anchor-price terms \(z_{U_{e_i}}\) are invariant.

For the two shores jointly, put

\[
                         p(v)=a^-_v-a^+_v.           \tag{9.3}
\]

With forward orientation using upper tail \(v_{i-1}\) and lower head
\(v_i\), reverse minus forward cost is

\[
 \sum_{\substack{[r,s]\ {\rm maximal}\\Q\text{-run}}}
      \left(p(v_{r-1})-p(v_s)\right).                \tag{9.4}
\]

#### Proof

For one selected edge, the upper endpoint term changes from
\(-a^-_{v_{i-1}}\) to \(-a^-_{v_i}\), while the lower term changes from
\(-a^+_{v_i}\) to \(-a^+_{v_{i-1}}\).  Their difference is
\(p(v_{i-1})-p(v_i)\).  Summing over a maximal consecutive selected run
telescopes, proving (9.2)--(9.4). \(\square\)

At the balanced point \(x_0=\theta\mathbf1\), every path is one fractional
run and reverse minus forward becomes

\[
                         \theta\left(p(v_0)-p(v_m)\right).       \tag{9.5}
\]

If \(L_{\rm half}(x_0,\lambda)\) is the average of the two orientations on
each path, then

\[
 \min_{\omega\ {\rm coherent}}
 L_\omega(x_0,\lambda)
 =
 L_{\rm half}(x_0,\lambda)
 -{\theta\over2}
   \sum_{\text{paths }P}
     |p(\operatorname {first}P)-p(\operatorname {last}P)|.       \tag{9.6}
\]

A positive value in (9.6) is one weighted cut excluding every coherent
orientation at the balanced point.  Its absence is not sufficient for one
orientation to satisfy every weighted cut: distinct cuts can require
opposite endpoint choices.  For integral \(Q\), (9.4) shows the sharper
fact that orientation and basis must be coupled through all maximal
\(Q\)-run boundaries, not merely the two endpoints of a child path.

If a planted bank pins some path orientations, the minimum in (9.6) is
taken only over the unpinned paths.  This is the endpoint part of the
protected face in Section 8.

## 9A. Rounded SBE orientation: exact positive face and obstruction

The supermodular occurrence formula gives a useful orientation theorem, but
not an unconditional generalized-polymatroid reduction.

Fix one shore with occurrence graph \(G=({\cal O},X)\), and let \(Z\) be
the terminal endpoint set chosen by orienting the child paths.  For
\(A\subseteq X\), put

\[
 {\cal O}(A)=\{o\in{\cal O}:N(o)\subseteq A\},\qquad
 g(A)=N|{\cal O}(A)|-R|A|.                                  \tag{9A.1}
\]

Then SBE is exactly

\[
                         C|Z\cap A|\ge g(A)
                         \qquad(A\subseteq X).                 \tag{9A.2}
\]

The containment count in (9A.1) is supermodular: a neighbourhood contained
in \(A\cup B\) but in neither \(A\) nor \(B\) contributes one unit of
supermodular slack.  The term \(-R|A|\) is modular.

Let \(E\) be the endpoints of nontrivial paths and \(I_0\) the fixed
isolated terminals.  Eliminating all other coordinates gives the exact
endpoint demand

\[
 \Psi(A)=
 \max_{S:\,S\cap E=A}
       \bigl(g(S)-C|I_0\cap S|\bigr),\qquad
 h(A)=\max\left\{0,\left\lceil{\Psi(A)\over C}\right\rceil\right\}.
                                                               \tag{9A.3}
\]

Partial maximization preserves supermodularity of \(\Psi\).  The ceiling
need not preserve it.

### Proposition 9A.1 (small exact rounding obstruction)

Let \(X=\{1,2,3,4\}\), partitioned into two endpoint pairs.  Give each
\(x\in X\) one outer occurrence with singleton neighbourhood \(\{x\}\), and
take

\[
                         (N,R,C)=(4,3,2).                       \tag{9A.4}
\]

Then \(g(A)=|A|\) is modular, while

\[
                         h(A)=\left\lceil{|A|\over2}\right\rceil \tag{9A.5}
\]

is not supermodular.  For
\(A=\{1,2,3\}\), \(B=\{2,3,4\}\),

\[
                  h(A)+h(B)=4>3=h(A\cap B)+h(A\cup B).         \tag{9A.6}
\]

The half-endpoint vector \(z_x=1/2\) satisfies every unrounded inequality
(9A.2), but the four singleton rows force every Boolean \(z_x=1\), contrary
to choosing one endpoint from each pair.

This is an exact containment-graph counterexample.  There is also a literal
Catalan one: on the authenticated parameter-three child, the upper-shore
sets \(E\setminus\{28\}\) and \(E\setminus\{13\}\) both have rounded demand
three, where \((13,28)\) is one path pair.  The two rows force opposite
orientations of that path.  The lower shore has the analogous obstruction
on \((19,49)\).  Thus no coherent orientation is even one-shore SBE,
although the half-endpoint point satisfies every fractional row.

Consequently neither the supermodularity of \(g\), a min-cut separation
oracle, nor later common-basis donor variables yields an integral
generalized-polymatroid theorem in general.  Donor selection occurs after
orientation and cannot repair a failed SBE row.

### Theorem 9A.2 (rounded joint-orientation polymatroid face)

Let \(\mu:E\to E\) exchange the two endpoints of every nontrivial path.
After subtracting fixed-isolate contributions, let \(h^-\) be the rounded
upper demand and let \(h^+\circ\mu\) be the lower demand pulled to the same
selected-terminal ground.  Define

\[
 H_0(A)=\max\{h^-(A),h^+(\mu A)\},\qquad
 H(A)=\max_{B\subseteq A}H_0(B).                              \tag{9A.7}
\]

Let \({\cal M}_{I,F}\) be a consistent face of the endpoint partition
matroid: \(I\) is a set of forced selected endpoints, \(F\) a set of
forbidden endpoints, and every remaining path contributes one endpoint.
Here consistency means that every fixed path has exactly one endpoint in
\(I\) and its mate in \(F\), while neither endpoint of an unfixed path lies
in \(I\cup F\); arbitrary input sets must first be replaced by this
forced--forbidden closure.
Write \(k\) for the total number of nontrivial paths and
\(r_{I,F}\) for its rank function.  Explicitly,

\[
 r_{I,F}(A)
 =|I\cap A|
  +|\{\text{unfixed path pairs meeting }A\}|.                  \tag{9A.8}
\]

Assume

1. \(H\) is integer, nondecreasing and supermodular;
2. \(H(\varnothing)=0\) and \(H(E)=k\).

Then a coherent endpoint choice satisfying both shores and the fixed bank
face exists if and only if

\[
 \boxed{\qquad H(A)\le r_{I,F}(A)
                   \quad\text{for every }A\subseteq E.\qquad}  \tag{9A.9}
\]

Moreover the feasible endpoint polytope is integral and has a
polymatroid-intersection/submodular-flow algorithm, given value oracles for
\(H\) and \(r_{I,F}\).

#### Proof

Because the selected vector \(z\) is nonnegative and has \(z(E)=k\), all
two-shore rows are equivalent to \(z(A)\ge H(A)\); nonnegativity is what
permits replacement by the monotone closure in (9A.7).  Define

\[
                         b_H(S)=k-H(E\setminus S).              \tag{9A.10}
\]

The hypotheses make \(b_H\) an integer normalized nondecreasing submodular
function.  The lower rows are exactly

\[
                         z\in B(b_H).                           \tag{9A.11}
\]

The bank-compatible endpoint transversals are the integral points of
\(B({\cal M}_{I,F})\).  Edmonds' integral polymatroid-intersection min--max
says that these two base polytopes meet if and only if

\[
 r_{I,F}(A)+b_H(E\setminus A)\ge k
 \qquad(A\subseteq E).                                        \tag{9A.12}
\]

Substituting (9A.10) turns (9A.12) into (9A.9).  Integrality gives a literal
orientation. \(\square\)

Thus a planted bank which merely fixes endpoint choices remains a matroid
face and costs the explicit all-cut margin in (9A.9).  A phase-flexible
multi-path C6 or sparse-cycle menu is instead a synchronized group choice;
it is not automatically such a face.

More explicitly, let \(\kappa_I(A)\) count fixed path pairs for which
\(A\) contains the forbidden mate but not the selected endpoint.  If
\(\gamma(A)\) is the number of path pairs meeting \(A\), then

\[
 r_{I,F}(A)=\gamma(A)-\kappa_I(A),\qquad
 \gamma(A)-H(A)\ge\kappa_I(A).                                \tag{9A.12a}
\]

The second inequality for every \(A\) is exactly (9A.9).  It is the
correlated all-cut price of fixing the bank; expected one-point survival
does not imply it.

### Corollary 9A.3 (exact rounded endpoint deficiency)

Under the hypotheses of Theorem 9A.2,

\[
 \min_{Z\in B({\cal M}_{I,F})}
       \max_{A\subseteq E}\bigl(H(A)-|Z\cap A|\bigr)_+
 =
 \max_{A\subseteq E}\bigl(H(A)-r_{I,F}(A)\bigr)_+.             \tag{9A.12b}
\]

#### Proof

Every protected transversal has \(|Z\cap A|\le r_{I,F}(A)\), proving the
lower bound.  Let the right side be \(d\).  Replace \(H(A)\) by
\(H(A)-d\) on nonempty proper sets, while retaining \(0\) at
\(\varnothing\) and \(k\) at \(E\).  The result remains supermodular:
the shifts cancel on crossing pairs with nonempty intersection and proper
union; disjoint pairs and pairs whose union is \(E\) only gain slack.
It is at most \(r_{I,F}\) on every set.  Its complementary function is an
integer normalized submodular base function, though it need not be
nondecreasing.  The integral generalized-base-polyhedron/matroid-base
intersection theorem, with the same cut calculation as (9A.12), supplies a
protected transversal meeting these weakened lower bounds.  This proves the
reverse inequality. \(\square\)

### Proposition 9A.4 (exact residue test)

For an integer supermodular function \(\Psi\), omit the harmless
nonnegativity truncation on a region where the demands are active and put

\[
 h(A)=\left\lceil{\Psi(A)\over C}\right\rceil,\qquad
 \eta_C(t)=C\left\lceil{t\over C}\right\rceil-t.                \tag{9A.13}
\]

Then \(h\) is supermodular on a pair \(A,B\) if and only if

\[
\begin{aligned}
 \Delta_\Psi(A,B)
 &:=\Psi(A\cap B)+\Psi(A\cup B)-\Psi(A)-\Psi(B)\\
 &\ge
 \eta_C(\Psi(A))+\eta_C(\Psi(B))
 -\eta_C(\Psi(A\cap B))-\eta_C(\Psi(A\cup B)).                 \tag{9A.14}
\end{aligned}
\]

For the containment function (9A.1),

\[
 \Delta_g(A,B)
 =N\,|\{o:N(o)\subseteq A\cup B,\,
             N(o)\nsubseteq A,\,
             N(o)\nsubseteq B\}|.                              \tag{9A.15}
\]

Hence, on active pairs, one crossing occurrence makes (9A.14) automatic
whenever \(N\ge2(C-1)\).  The Catalan parameters satisfy \(N\ge2C\) for
every \(n\ge7\), since

\[
 {C\over N}={2(2n+1)\over n(n+2)}\le{1\over2}.                 \tag{9A.16}
\]

At those parameters only zero-bridge pairs, and pairs touching the
nonnegativity truncation, can violate rounded supermodularity.  This is a
checkable structural target, not a proof that the PBBS/Pascal occurrence
graphs pass it.

### Theorem 9A.5 (exact antipodal cross-paramodular criterion)

The mate-pulled maximum in Theorem 9A.2 is a useful sufficient face.  The
less restrictive natural formulation keeps the two shores as lower and
upper bounds on one head vector.

Let the path pairs form a matching \(H_{\rm path}\) on endpoint ground
\(E\).  Put

\[
\begin{aligned}
 \eta(A)&=\sum_{x\in A}d_{H_{\rm path}}(x)=|A|,\\
 \gamma(A)&=|\{e\in H_{\rm path}:e\cap A\ne\varnothing\}|,\\
 \iota(A)&=|\{e\in H_{\rm path}:e\subseteq A\}|.
                                                               \tag{9A.17}
\end{aligned}
\]

Let \(p^-,p^+\) be the normalized integer rounded demands for the shore
which sees the selected head vector \(z\) and the antipodal shore which sees
\(\eta-z\).  Assume both are supermodular and, for every \(A,B\subseteq E\),

\[
 \boxed{
 p^-(A)+p^+(B)
 \le
 \eta(A\cap B)+p^-(A\setminus B)+p^+(B\setminus A).
 }                                                             \tag{9A.18}
\]

Then a coherent orientation satisfying both shores exists if and only if

\[
                         p^\sigma(A)\le\gamma(A)
 \quad(\sigma\in\{-,+\},\ A\subseteq E).                       \tag{9A.19}
\]

#### Proof

The two-shore system is

\[
                         p^-(A)\le z(A)
                         \le\eta(A)-p^+(A).                    \tag{9A.20}
\]

Condition (9A.18) is precisely the cross inequality saying that
\((p^-,\eta-p^+)\) is an integral paramodular pair.  Hence (9A.20) defines
an integral generalized polymatroid.  Endpoint orientations form the
integral matching-zonotope base

\[
                         \iota(A)\le z(A)\le\gamma(A).          \tag{9A.21}
\]

The generalized-polymatroid intersection theorem reduces nonemptiness to
\(p^-(A)\le\gamma(A)\) and
\(\iota(A)\le\eta(A)-p^+(A)\) for every \(A\).  Since
\(\eta(A)-\iota(A)=\gamma(A)\) for a matching, these are exactly (9A.19).
Integrality supplies a literal orientation. \(\square\)

A fixed-phase packet bank is handled by subtracting its fixed head-count
vectors on the two shores and deleting its already oriented path pairs.
The same theorem then applies to the residual matching.  A live two-phase
packet which locks at least two path choices is not generally a matroid
face: a one-element exchange between its two phase sets gives neither
phase.  It therefore needs the envelope or an extended parity/circulation
state of Section 8, not ordinary endpoint-polymatroid rounding.

### 9A.1 Relation to common-basis donors and common cap

If Theorem 9A.2 supplies an integral both-SBE orientation, ordinary SBE
then puts the constant vector in the two strict matroid base polytopes and
produces some synchronized common basis.  A prescribed donor/absorber bank
requires more:

1. the orientation-dependent forced--forbidden common-basis cuts (8.2);
2. the packet-shifted physical cuts (8.10); and
3. a pure saddle or a two-shore circulation purification.

These systems address different variables and quantifiers.  A rigorous
sequential sufficient theorem is obtained if (9A.9) holds, one resulting
orientation has a nonempty protected common-basis face, and that face
satisfies the protected zero-\(\rho\) and purification hypotheses of
Section 8.

To combine all rows into one generalized-polymatroid/submodular-flow
problem would require an additional **cross-paramodular donor hypothesis**:
the orientation-dependent common-base face and the physical circulation
fibres must admit one integral generalized-polymatroid extension on the
endpoint tokens.  This is not implied by SBE.  The common basis is already
an intersection of two matroid bases; static packet phases add group-locking
blocks; and Section 12 gives a determinant-two physical-cut lock even when
basis exchange is connected.  No such cross-paramodular extension is
proved for the PBBS/Pascal family.

## 10. A primal duplex overload-alignment exchange

The pure-saddle criterion works in the dual.  The following direct
assignment condition is often more transparent.

Let

\[
                         Q'=Q-q+r                 \tag{10.1}
\]

be a synchronized common-basis exchange.  On shore \(\sigma\), the endpoint
row \(\tau^\sigma(r)\) leaves the punctured outer bank and
\(\tau^\sigma(q)\) enters it.  The owner \(\upsilon^\sigma(q)\) changes
from cap one to cap two, while \(\upsilon^\sigma(r)\) changes from cap two
to cap one.

### Theorem 10.1 (duplex overload-alignment lemma)

Suppose that on both shores an assignment alternating chain replaces the
departing row \(\tau^\sigma(r)\) by the arriving row
\(\tau^\sigma(q)\), producing an outer-perfect assignment \(M'^\sigma\).
Assume its loads satisfy

\[
\begin{array}{ll}
 \ell_{\upsilon^\sigma(q)}(M'^\sigma)\le2,&
 \ell_{\upsilon^\sigma(r)}(M'^\sigma)\le1,\\
 \ell_x(M'^\sigma)\le c^\sigma_{Q'}(x)&
 \text{for every unchanged owner }x .
\end{array}                                             \tag{10.2}
\]

Then

\[
                         \rho^-_\omega(Q')
                         =\rho^+_\omega(Q')=0.         \tag{10.3}
\]

#### Proof

The alternating chains preserve every outer equality and replace exactly
the changed puncture row.  Conditions (10.2) are precisely the new owner
capacities, so the two integral assignments are feasible zero-dummy
solutions.

Equivalently, sum any feasible weighted-dual inequalities over the atoms
of \(M'^\sigma\).  Outer perfection gives

\[
 \sum_Da_D+\sum_Vb_V
 \le\sum_x\ell_x(M'^\sigma)z_x
 \le\sum_xc^\sigma_{Q'}(x)z_x.                      \tag{10.4}
\]

Every weighted cut is nonpositive, proving (10.3). \(\square\)

The alternating chain may be long.  Thus (10.1) alone is not enough:
robust assignment exchange and overload alignment are the load-bearing
hypotheses.

## 11. Literal parameter-three repair

Use the oriented child paths

\[
\begin{aligned}
 &34-15-07-0b,\\
 &16-26-2a-29-19-13,\\
 &2c-25-23,\qquad
 38-1c-0d,\qquad
 31-32-1a-0e .
\end{aligned}                                           \tag{11.1}
\]

The published bad basis retains \(07\to0b\) and has upper deficiency one.
Instead retain

\[
 q_*=31\to32,\qquad
 Q_*=E(F)\setminus\{q_*\}.                            \tag{11.2}
\]

Since \(N=15,C=14\), this has the required order.  Its unique cap-two
owners are

\[
                         U_{q_*}=33,\qquad L_{q_*}=30.             \tag{11.3}
\]

### Theorem 11.1 (integral duplex-positive basis)

The following upper assignment is outer-perfect:

\[
\begin{array}{c|c|c}
D&V&\text{physical owners}\\ \hline
23&37&27,33\\
31&3b&33,39\\
13&1f&17,1b\\
0b&2f&0f,2b\\
0d&3d&1d,2d\\
0e&3e&1e,2e .
\end{array}                                            \tag{11.4}
\]

The following complement-normalized lower assignment is outer-perfect:

\[
\begin{array}{c|c|c}
D&V&\text{physical owners}\\ \hline
01&31&11,21\\
02&32&12,22\\
08&2c&0c,28\\
20&34&24,30\\
10&38&18,30\\
04&16&06,14 .
\end{array}                                            \tag{11.5}
\]

Only owner \(33\) repeats in (11.4), exactly twice, and only owner \(30\)
repeats in (11.5), exactly twice.  Every other used owner occurs once.
Consequently

\[
                         \rho^-(Q_*)=\rho^+(Q_*)=0.   \tag{11.6}
\]

Both supports are no-empty linear forests.  On the upper shore the only
two-edge component is

\[
                         27-33-39,                   \tag{11.7}
\]

and on the lower shore it is

\[
                         24-30-18.                   \tag{11.8}
\]

Each shore also has four disjoint anchor--anchor edges and four isolated
anchors.  Therefore

\[
 c_0=0,\qquad c_2=5=\operatorname {Cat}_3,\qquad
 r_{\widehat M/E_\rho}=R=1.                         \tag{11.9}
\]

#### Proof

Every row in (11.4)--(11.5) is a literal containment diamond.  Each table
uses its six lower and six upper outer labels exactly once, proving at the
same time that \(Q_*\) is incidence-admissible on both shores.  The load
statement and (11.3) prove all capacities, so (11.6) follows from Theorem
2.1 or directly from (10.4).

All physical owners are distinct except the one declared repeated owner in
each table.  Hence the component descriptions (11.7)--(11.8) follow.
Counting the remaining anchors gives (11.9). \(\square\)

The exchange from the bad retained edge to \(q_*\) is a concrete instance
of Theorem 10.1.  Upstairs, the four-row assignment rotation replaces

\[
 (07,0b,13,23)\longmapsto(2f,1f,37,3b)
\]

by

\[
 (0b,13,23,31)\longmapsto(2f,1f,37,3b).             \tag{11.10}
\]

The old overloaded owner \(33\) remains load two but becomes the unique
ordinary owner; the replacement row also introduces owner \(39\) outside
the old \(8>7\) cut.  The lower table aligns its repeated load with the new
ordinary owner \(30\).  Thus the repair expands support and aligns both
overloads; it is not merely a relocation of one dummy unit.

This proves that the authenticated \(\rho=1\) basis is a fixed-fibre
obstruction, not an existential obstruction over the same common-basis
bank.

## 12. The smallest purification lock

Let the common-base polytope be the rank-one segment

\[
 {\cal P}=\operatorname {conv}\{(1,0),(0,1)\},       \tag{12.1}
\]

and impose the two modular weighted cuts

\[
                         2x_1-1\le0,\qquad
                         2x_2-1\le0.                 \tag{12.2}
\]

The midpoint \((1/2,1/2)\) satisfies both at equality, while each integral
basis violates one cut by one.  The basis exchange graph is one edge.
Best-response descent simply alternates between its endpoints.

This is the smallest two-cut determinant-two purification obstruction.
It proves:

1. a balanced fractional common-basis point is insufficient;
2. connected common-basis exchange is insufficient;
3. no single universal weighted cut need exclude all pure bases; and
4. active-cut descent need not decrease the new maximum.

The example is an abstract modular-cut system, not a realization of the
Boolean physical host.  No literal Catalan forest is currently known for
which every synchronized common basis has positive \(\rho\).

## 13. Relation to rooted support and exact remaining theorem

Item 2302R proves, for every synchronized \(Q\), that the complete physical
candidate graph on either shore has at most one anchor-free component and
root-contracted graphic rank at least \(R-1\).  This neither implies nor is
implied by \(\rho(Q)=0\):

* \(\rho=0\) is a fractional two-palette load statement with no graphic
  row;
* the rooted support theorem is a graphic statement on the union of all
  candidates with no simultaneous palette selection.

The parameter-three bad basis has near-full ambient rooted rank but
\(\rho=1\).  Conversely a zero-dummy fractional flow need not be integral,
acyclic, or root-independent.  The basis \(Q_*\) in Section 11 happens to
pass all of these stronger rows, but that is a finite calibration.

The exact all-parameter sufficient route is now:

1. choose a coherent both-SBE orientation, using Theorem 9A.2 or 9A.5 when
   its rounded supermodularity hypotheses hold, and a compatible planted
   absorber/rerouter bank;
2. prove the protected common-basis cuts of Theorem 8.1, equivalently
   (8.4) in the risk-only case;
3. prove protected diamond-SBE, equivalently
   \(\bar\rho_{\omega,{\cal A}}=0\);
4. obtain a pure bank-preserving basis from a pure saddle or protected
   fibre purification;
5. round its two fractional physical flows while preserving the ordinary
   and root-contracted graphic rows; and
6. align the residual leave with the planted gain-one packet boundaries.

Steps 2--4 are the exact bank-flexible fractional gate.  Steps 5--6 remain
integral/topological cover-down.  No residence, deep-shadow, compiler, or
contiguous-OR equality conclusion is made.

## 14. Independent audit and scope

The fixed-\(Q\) dual signs and the elimination to \(\tau_Q\), the
two-shore min--max, the pure-saddle inequalities, the orientation
run-boundary signs, the purification direction rows, the literal
parameter-three tables, the forced--forbidden matroid minors, the packet
dual shift, the scalar envelope wall, and the orbit-packing constant were
independently audited in separate proof lanes.  That audit is also the
reason Section 8 explicitly keeps the static-exterior, literal-slot, and
fixed-orientation quantifiers.

The rounded-orientation statements in Section 9A were independently checked
against

\[
\text{MATH\_THEOREM\_CATALAN\_SBE\_ORIENTATION\_AND\_FOUR\_SECTOR\_GATE\_20260731.md}
\]

and

\[
\text{MATH\_THEOREM\_CATALAN\_SBE\_ORIENTATION\_LOGICAL\_AND\_INTEGRALITY\_OBSTRUCTIONS\_20260731.md}.
\]

In particular the report does not replace the ceiling by an unrounded
fractional condition and does not infer integrality from a separation
oracle.

The absorber facts used in Section 8 are exactly those proved in

\[
\text{MATH\_THEOREM\_CATALAN\_SUSPENDED\_TRANSPARENT\_HEX\_ABSORBER\_AND\_BLOCKERS\_20260731.md}
\]

and

\[
\text{MATH\_THEOREM\_CATALAN\_SPARSE\_FIVE\_CYCLE\_PHYSICAL\_SWITCH\_20260731.md}.
\]

Their internal physical forests and resource equalities are used; no
unproved post-hoc packet availability, exterior acyclicity, or common-cap
preservation is imported.

No finite search, SAT computation, or web lookup is used in this report.
