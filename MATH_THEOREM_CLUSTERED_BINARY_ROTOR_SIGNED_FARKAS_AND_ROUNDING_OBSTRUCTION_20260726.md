# Clustered binary rotors: the signed Farkas dual and an exact rounding obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad D=m!(m+1)!.
\]

This note treats the exact reduced system consisting of

1. one selected state-arc in every middle-owner fibre;
2. state-flow conservation;
3. all lower-prefix cover inequalities through depth \(H\); and
4. exact cancellation of the signed nested Johnson divergences through
   depth \(H\).

There are four conclusions.

* The complete Farkas alternative is the owner-fibre maximum inequality
  (2.7).  The dual variables for divergence cancellation are arbitrary
  signed Johnson potentials, not nonnegative target prices.
* For the relaxed bound

  \[
     \mathfrak D_H(z)=\frac12\sum_{q=0}^H
       \lVert D_qz\rVert_1\le \Delta,
  \]

  the exact extra dual term is

  \[
        \Delta\max_{0\le q\le H}\operatorname {osc}(\theta_q).
  \]

  This is sharper than the unnormalised
  \(2\Delta\lVert\theta\rVert_\infty\), because every Johnson
  divergence has coordinate sum zero.
* The uniform \(A\)-only circulation satisfies exact signed cancellation
  and has lower-target load

  \[
   \rho_q=\frac{W}{\binom n{m-q}}
   =\exp\!\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right)
  \]

  uniformly for \(q\le A\sqrt m\).  Hence there is no real Farkas
  obstruction, even with \(\Delta=0\).
* Nevertheless, for every odd prime \(m=p\), this feasible fractional
  \(A\)-face contains no Boolean point: its integral circulations are
  unions of free \(2p\)-orbits, while

  \[
       \binom{2p+1}{p}\equiv2\pmod p.
  \]

  Thus the full owner--flow--lower-prefix--signed-cancellation matrix is
  not totally unimodular.  More intrinsically, on this prime subsequence
  its integer hull satisfies

  \[
                      \sum_{\pi\in S_n}z_{\pi,B}\ge1,
  \]

  whereas an exactly divergence-free feasible fractional point has left
  side zero.

This is a rigorous obstruction to LP, network-matrix, or support-preserving
rounding.  It is not an obstruction to a genuinely mixed integral rotor
factor; that remains the precise surviving boundary.

## 1. The exact clustered primal

For a permutation state

\[
                  \pi=(x_1,\ldots,x_n)\in S_n
\]

let

\[
 A\pi=(x_2,\ldots,x_{n-1},x_1,x_n),\qquad
 B\pi=(x_2,\ldots,x_n,x_1),
\tag{1.1}
\]

and let its middle owner be

\[
                  X(\pi)=\{x_1,\ldots,x_m\}.
\tag{1.2}
\]

For \(0\le q\le H\), write

\[
 r_q=m-q,\qquad
 P_q(\pi)=\{x_1,\ldots,x_{r_q}\},
\tag{1.3}
\]

and

\[
 K_q(\pi)=\{x_{n-r_q+1},\ldots,x_{n-1}\}.
\tag{1.4}
\]

Thus \(|K_q(\pi)|=r_q-1\).  For
\(T\in\binom{[n]}{r_q}\), define the signed switch flag

\[
 \partial_{q,T}(\pi)=
 \mathbf 1\bigl[T=K_q(\pi)\cup\{x_n\}\bigr]
 -\mathbf 1\bigl[T=K_q(\pi)\cup\{x_1\}\bigr].
\tag{1.5}
\]

Let \(z_{\pi,g}\ge0\), \(g\in\{A,B\}\), be the mass on the state arc
\(\pi\to g\pi\).  The owner and flow equations are

\[
 \sum_{\pi:X(\pi)=X}\sum_gz_{\pi,g}=1
 \qquad\left(X\in\binom{[n]}m\right),
\tag{1.6}
\]

\[
 \sum_gz_{\pi,g}-\sum_gz_{g^{-1}\pi,g}=0
 \qquad(\pi\in S_n).
\tag{1.7}
\]

The lower-prefix loads are

\[
 L_{q,S}(z)=
 \sum_{\pi:P_q(\pi)=S}\sum_gz_{\pi,g},
 \qquad S\in\binom{[n]}{r_q},
\tag{1.8}
\]

and the signed divergences are

\[
 D_{q,T}(z)=
 \sum_{\pi\in S_n}z_{\pi,A}\partial_{q,T}(\pi).
\tag{1.9}
\]

The exact primal system \({\cal P}_H(0)\) is

\[
 \boxed{
 \begin{aligned}
  &(1.6),\ (1.7),\qquad z\ge0,\\
  &L_{q,S}(z)\ge1 &&(0\le q\le H,\ |S|=r_q),\\
  &D_{q,T}(z)=0 &&(0\le q\le H,\ |T|=r_q).
 \end{aligned}}
\tag{1.10}
\]

For Boolean \(z\), (1.6)--(1.7) are exactly the clustered binary-rotor
cycle-cover equations: the selected state arcs are disjoint directed
cycles and exactly one selected state lies above each owner.

The signed-divergence identity from the binary-rotor construction is

\[
                  R_{q,T}(z)-L_{q,T}(z)=D_{q,T}(z),
\tag{1.11}
\]

where \(R_q\) is the complementary upper-prefix load.  Consequently
exact cancellation in (1.10) makes every lower cover simultaneously an
upper cover.  Thus (1.10) is the exact one-sided-plus-cancellation
replacement for the two-sided prefix system.

## 2. The complete Farkas alternative

Let

\[
 \lambda_{q,S}\ge0
 \qquad(0\le q\le H,\ |S|=r_q)
\tag{2.1}
\]

be lower-target prices.  Let \(\phi_\pi\in\mathbb R\) be state
potentials, \(\alpha_X\in\mathbb R\) owner prices, and
\(\theta_{q,T}\in\mathbb R\) signed Johnson potentials.  Put

\[
 \Lambda_\lambda(\pi)=\sum_{q=0}^H
             \lambda_{q,P_q(\pi)},
\tag{2.2}
\]

\[
 \Theta_\theta(\pi)=\sum_{q=0}^H
 \left(
  \theta_{q,K_q(\pi)\cup\{x_n\}}
 -\theta_{q,K_q(\pi)\cup\{x_1\}}
 \right).
\tag{2.3}
\]

### Theorem 2.1 (arc-form signed Farkas dual)

The system \({\cal P}_H(0)\) is feasible if and only if every tuple
\((\alpha,\phi,\theta,\lambda)\) satisfying

\[
 \boxed{
 \alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}
 +\mathbf1[g=A]\Theta_\theta(\pi)
 \ge \Lambda_\lambda(\pi)
 }
\tag{2.4}
\]

for all \(\pi\in S_n\) and \(g\in\{A,B\}\), also satisfies

\[
                 \boxed{\sum_X\alpha_X\ge
                    \sum_{q,S}\lambda_{q,S}.}
\tag{2.5}
\]

#### Proof

If \(z\) is feasible, multiply (2.4) by \(z_{\pi,g}\) and sum over all
state arcs.  The owner equations turn the owner term into
\(\sum_X\alpha_X\).  Flow conservation cancels the state-potential
terms.  Exact signed cancellation cancels the Johnson-potential terms.
Finally the lower-cover inequalities make the right side at least
\(\sum_{q,S}\lambda_{q,S}\).  This proves (2.5).

Conversely, (2.4)--(2.5) are precisely the Farkas alternative for the
owner, flow, and signed-divergence equalities, the lower-cover
inequalities, and nonnegativity of \(z\).  If (1.10) were infeasible,
the separating halfspace supplied by Farkas would give a tuple violating
(2.5). \(\square\)

The owner prices can be eliminated.  Define

\[
 M_X(\phi,\theta,\lambda)=
 \max_{\substack{\pi:X(\pi)=X\\g\in\{A,B\}}}
 \left(
  \Lambda_\lambda(\pi)-\phi_\pi+\phi_{g\pi}
  -\mathbf1[g=A]\Theta_\theta(\pi)
 \right).
\tag{2.6}
\]

### Corollary 2.2 (owner-fibre maximum form)

The exact signed system is feasible if and only if, for every
\(\phi,\theta\) and every \(\lambda\ge0\),

\[
 \boxed{
       \sum_{X\in\binom{[n]}m}M_X(\phi,\theta,\lambda)
       \ge \sum_{q,S}\lambda_{q,S}.}
\tag{2.7}
\]

#### Proof

For fixed \((\phi,\theta,\lambda)\), (2.4) is equivalent to
\(\alpha_X\ge M_X\) for every owner \(X\).  Its least possible total
owner price is therefore \(\sum_XM_X\).  Substitute this into Theorem
2.1. \(\square\)

The important sign distinction is exact: \(\lambda\) is nonnegative
because lower coverage is an inequality, whereas \(\theta\) is
unrestricted because signed cancellation is an equality.

## 3. The sharp dual for an aggregate cancellation budget

For a vector \(v_q\) on \(\binom{[n]}{r_q}\), put

\[
 N(v)=\frac12\sum_{q=0}^H\lVert v_q\rVert_1.
\tag{3.1}
\]

Every \(D_q(z)\) has coordinate sum zero, because every switch flag in
(1.5) has one positive and one negative entry.  On this zero-sum
subspace, the dual norm of \(N\) is

\[
 N^*(\theta)=\max_{0\le q\le H}\operatorname {osc}(\theta_q),
 \qquad
 \operatorname {osc}(\theta_q)=\max_T\theta_{q,T}-\min_T\theta_{q,T}.
\tag{3.2}
\]

Indeed, for zero-sum \(v_q\),

\[
 \theta_q\mathbin\cdot v_q
 \le \frac12\lVert v_q\rVert_1
       \operatorname {osc}(\theta_q).
\tag{3.3}
\]

Equality is attained by putting equal positive and negative masses at a
maximizer and a minimizer of the depth having largest oscillation.

Let \({\cal P}_H(\Delta)\) be (1.6)--(1.8) together with

\[
                         N(D(z))\le\Delta.
\tag{3.4}
\]

### Theorem 3.1 (budgeted signed Farkas dual)

The system \({\cal P}_H(\Delta)\) is feasible if and only if, for all
\(\phi,\theta\) and \(\lambda\ge0\),

\[
 \boxed{
  \sum_XM_X(\phi,\theta,\lambda)
  +\Delta\max_q\operatorname {osc}(\theta_q)
  \ge \sum_{q,S}\lambda_{q,S}.}
\tag{3.5}
\]

#### Proof

Introduce a vector \(v=D(z)\) in the product of the zero-sum target
spaces and constrain \(N(v)\le\Delta\).  Apply separating-hyperplane
duality to the owner and flow equalities, the lower inequalities, and
the equality \(D(z)-v=0\).  Eliminating \(v\) contributes the support
function of the ball \(N(v)\le\Delta\), which by (3.2) is exactly
\(\Delta\max_q\operatorname {osc}(\theta_q)\).  Eliminating the owner
prices is Corollary 2.2. \(\square\)

For \(\Delta=0\), (3.5) reduces to (2.7).  Constants may be added
independently to each \(\theta_q\), so the oscillation rather than an
absolute \(\ell^\infty\) norm is forced.

## 4. No fractional separator and exact Gaussian accounting

Give every \(A\)-arc mass \(1/D\) and every \(B\)-arc mass zero:

\[
                 z^*_{\pi,A}=\frac1D,\qquad
                 z^*_{\pi,B}=0.
\tag{4.1}
\]

### Proposition 4.1 (exactly cancelled fractional point)

The vector \(z^*\) satisfies owner balance, state flow, exact signed
cancellation at every depth, and

\[
 L_{q,S}(z^*)=\rho_q
 =\frac{(m-q)!(m+1+q)!}{m!(m+1)!}
 =\frac{W}{\binom n{m-q}}
\tag{4.2}
\]

for every lower target \(S\) at depth \(q\).

#### Proof

There are \(D\) states over every owner, proving (1.6).  Since \(A\)
permutes \(S_n\), every state has incoming and outgoing mass \(1/D\),
proving (1.7).

For signed cancellation, pair every state
\(\pi=(x_1,x_2,\ldots,x_{n-1},x_n)\) with

\[
 \iota\pi=(x_n,x_2,\ldots,x_{n-1},x_1).
\tag{4.3}
\]

This involution leaves every \(K_q\) fixed and exchanges \(x_1,x_n\),
so

\[
             \partial_{q,T}(\iota\pi)=-\partial_{q,T}(\pi).
\]

The common weight \(1/D\) therefore gives \(D_{q,T}(z^*)=0\).

A fixed \(r_q\)-set is the prefix set of exactly
\(r_q!(n-r_q)!=(m-q)!(m+1+q)!\) permutation states.  Division by \(D\)
proves (4.2). \(\square\)

From (4.2),

\[
 \rho_q=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.
\tag{4.4}
\]

For fixed \(A<\infty\), uniformly for \(0\le q\le A\sqrt m+1\),

\[
 \begin{aligned}
 \log\rho_q
 &=\sum_{j=0}^{q-1}
   \log\left(1+\frac{2j+2}{m-j}\right)\\
 &=\frac{q(q+1)}m+O\left(\frac{q^3}{m^2}\right)
 =\frac{q(q+1)}m+O_A(m^{-1/2}).
 \end{aligned}
\tag{4.5}
\]

Consequently, for \(H=\lceil A\sqrt m\rceil\),

\[
             \boxed{\rho_H=e^{A^2}
               \bigl(1+O_A(m^{-1/2})\bigr).}
\tag{4.6}
\]

In particular \(\rho_0=1\), and every positive Gaussian depth has a
strict asymptotic margin.

Substitution of \(z^*\) into the dual gives the stronger coefficientwise
inequality

\[
 \boxed{
 \sum_XM_X(\phi,\theta,\lambda)
 \ge\sum_{q=0}^H\rho_q\sum_S\lambda_{q,S}.}
\tag{4.7}
\]

The state potentials telescope because \(A\) is a permutation, and the
Johnson potentials cancel by Proposition 4.1.  Hence no choice of signed
potentials can produce a real obstruction.  The obstruction, if any, is
integral.

## 5. Exact cycle-master form

Let \({\mathscr C}\) be the directed simple cycles of the state rotor
digraph with arcs \((\pi,A)\) and \((\pi,B)\).  For
\(C\in{\mathscr C}\), define

\[
 a_X(C)=\#\{(\pi,g)\in C:X(\pi)=X\},
\tag{5.1}
\]

\[
 \ell_{q,S}(C)=\#\{(\pi,g)\in C:P_q(\pi)=S\},
\tag{5.2}
\]

and

\[
 d_{q,T}(C)=
 \sum_{(\pi,A)\in C}\partial_{q,T}(\pi).
\tag{5.3}
\]

Every nonnegative state circulation decomposes into directed cycles.
Therefore (1.10) is equivalent to

\[
 \boxed{
 \begin{aligned}
  &\sum_Ca_X(C)\xi_C=1 &&\text{for every }X,\\
  &\sum_C\ell_{q,S}(C)\xi_C\ge1
       &&\text{for every }(q,S),\\
  &\sum_Cd_{q,T}(C)\xi_C=0
       &&\text{for every }(q,T),\\
  &\xi_C\ge0.
 \end{aligned}}
\tag{5.4}
\]

Its exact cycle Farkas alternative says that, for all free
\(\alpha,\theta\) and nonnegative \(\lambda\),

\[
 \sum_Xa_X(C)\alpha_X+\sum_{q,T}d_{q,T}(C)\theta_{q,T}
 \ge\sum_{q,S}\ell_{q,S}(C)\lambda_{q,S}
 \quad(C\in{\mathscr C})
\tag{5.5}
\]

must imply

\[
                         \sum_X\alpha_X\ge\sum_{q,S}\lambda_{q,S}.
\tag{5.6}
\]

The state potentials in (2.4) disappear after summing around a cycle.
This displays the exact failure of ordinary network integrality: after
flow is decomposed, the cycles are hyperedges in the owner-partition and
prefix-cover system.

Moreover, requiring \(\xi_C\in\mathbb Z_{\ge0}\) makes (5.4) exactly
the Boolean clustered problem.  Indeed the owner right sides are one,
so every used cycle is owner-simple and distinct used cycles have
disjoint owner sets.  Since each state has one owner, the cycles are
also state-disjoint.

## 6. Prime-divisibility rounding obstruction

Restrict (1.10) to the face

\[
                         z_{\pi,B}=0\qquad(\pi\in S_n).
\tag{6.1}
\]

Proposition 4.1 proves that this face is fractionally feasible for every
\(m\) and every \(H\le m-1\), with exact signed cancellation.

### Theorem 6.1 (integer-empty cancelled \(A\)-face)

If \(m=p>2\) is prime, the face (6.1) contains no Boolean
owner-transversal circulation.  This remains true after imposing every
lower-prefix inequality and exact signed cancellation through any
\(H\le p-1\).

#### Proof

On (6.1), let \(y_\pi=z_{\pi,A}\in\{0,1\}\).  Flow conservation says

\[
                           y_\pi=y_{A^{-1}\pi}.
\tag{6.2}
\]

Hence the selected state set is a union of \(A\)-orbits.  The rotor
\(A\) rotates the first \(2p\) positions and fixes the last.  Its action
on permutation states is free: equality \(A^j\pi=\pi\) forces
\(2p\mid j\), because those \(2p\) positions contain distinct labels.
Every orbit therefore has size \(2p\).

The owner equations select exactly one state over each of the \(W\)
owners, so the selected set has cardinality \(W\).  But in
\(\mathbb F_p[x]\),

\[
 (1+x)^{2p+1}
 \equiv(1+x^p)^2(1+x)\pmod p.
\tag{6.3}
\]

The coefficient of \(x^p\) on the right is two.  Thus

\[
                         W=\binom{2p+1}{p}\equiv2\pmod p,
\tag{6.4}
\]

so \(W\) cannot be the cardinality of a union of \(2p\)-orbits.  This
contradicts (6.2). \(\square\)

For every fixed \(A<\infty\), \(H=\lceil A\sqrt p\rceil\le p-1\) for
all sufficiently large primes.  The obstruction therefore occurs in the
requested Gaussian window, while (4.6) gives the exact fractional
margin there.

### Corollary 6.2 (non-TU and an integer-hull cut)

On every odd-prime instance, every Boolean point of the unrestricted
system satisfies

\[
                          \boxed{\sum_\pi z_{\pi,B}\ge1.}
\tag{6.5}
\]

The feasible fractional point (4.1) violates (6.5).  Consequently the
owner--flow--lower-prefix--signed-divergence matrix is not totally
unimodular, and the fractional feasible region is not the convex hull of
its Boolean points.

#### Proof

If the left side of (6.5) vanished at a Boolean point, nonnegativity
would put it on the forbidden face (6.1), contradicting Theorem 6.1.
The point (4.1) has left side zero.

For total unimodularity, suppose the augmented constraint matrix were
TU.  Delete all \(B\)-columns; total unimodularity is preserved under
column deletion.  Change the lower inequalities to the standard
opposite orientation if desired; row sign changes also preserve TU.
All right sides are integral.  The resulting \(A\)-face polytope is
nonempty by Proposition 4.1 and bounded because summing the owner
equations gives \(\sum_\pi z_{\pi,A}=W\).  A nonempty bounded polytope
with a TU matrix and integral right side has an integral vertex,
contradicting Theorem 6.1. \(\square\)

Thus no theorem based only on total unimodularity, ordinary circulation
decomposition, or support-preserving rounding of the uniform fractional
point can solve the clustered system.

## 7. Exact proved boundary

The following are now rigorous.

1. Equations (2.4)--(2.7) are the complete LP/Farkas dual for owner
   transversality, flow, lower-prefix coverage, and exact signed
   divergence cancellation.
2. Equation (3.5) is the sharp dual when exact cancellation is weakened
   to the aggregate floor-repair budget \(\mathfrak D_H\le\Delta\).
3. The common fractional point has zero divergence at every depth and
   Gaussian lower-prefix multiplicity \(e^{A^2}(1+O_A(m^{-1/2}))\) at
   depth \(A\sqrt m\).  Hence there is no fractional Hall/Farkas cut.
4. The cancelled \(A\)-only face is integer-empty for infinitely many
   Gaussian-scale instances.  Therefore generic LP or TU rounding is
   rigorously obstructed.

What is not proved is infeasibility of the unrestricted mixed face.  A
successful construction may cross the integer-hull cut (6.5) by changing
the rotor support.  It must choose an owner-simple family of cycles in
(5.4) whose lower-prefix loads cover every target and whose signed cycle
vectors cancel exactly, or to total \(o(W)\) in the budgeted form.  That
mixed cycle-semigroup saturation statement is the precise remaining
rounding problem; the present theorem neither proves nor assumes it.
