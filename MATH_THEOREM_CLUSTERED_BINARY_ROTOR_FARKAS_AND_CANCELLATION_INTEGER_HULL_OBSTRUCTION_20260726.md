# Clustered binary rotors: exact signed-cancellation Farkas dual and an integer-hull obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(H\le m-1\).  This note treats in one linear system

1. one unit from every middle-owner cluster;
2. exact binary-rotor state flow;
3. all lower-prefix covers through depth \(H\); and
4. exact, or budgeted, cancellation of the signed upper--lower
   divergence.

For exact cancellation, the Farkas dual has three kinds of potentials:
an owner price, a state-flow potential, and a free signed Johnson
potential.  After eliminating the owner prices, fractional feasibility is
equivalent to

\[
 \boxed{
 \sum_{q=0}^{H}\sum_S u_{q,S}
 \le
 \sum_{X\in\binom{[n]}m}
 \max_{\substack{e:\kappa(e)=X\\g\in\{A,B\}}}
 \left(
  \phi_e-\phi_{S_g e}+\Lambda_u(e)
  +\mathbf1_{\{g=A\}}\Gamma_\theta(e)
 \right)}
 \tag{0.1}
\]

for every \(u\ge0\) and every free \(\phi,\theta\).  All notation is
defined below.

If

\[
 \mathfrak D_H(z)=\frac12\sum_{q=0}^{H}\|D_q(z)\|_1\le\Delta
\]

is allowed instead, the exact dual condition is

\[
 \boxed{
 \sum_{q,S}u_{q,S}-2\Delta\eta
 \le \sum_X M_X(\phi,\theta,u),
 \qquad |\theta_{q,T}|\le\eta,\quad \eta\ge0.}
 \tag{0.2}
\]

The uniform rotor segment

\[
 z^t_{e,A}=\frac tD,\qquad
 z^t_{e,B}=\frac{1-t}{D},\qquad 0\le t\le1,
 \tag{0.3}
\]

where \(D=m!(m+1)!\), has *zero signed divergence at every rank* and
proves the stronger domination

\[
 \sum_XM_X(\phi,\theta,u)
 \ge
 \sum_{q=0}^{H}\lambda_q\sum_Su_{q,S},
 \qquad
 \lambda_q=\frac{W}{\binom n{m-q}}.
 \tag{0.4}
\]

In particular, no fractional Farkas obstruction exists.  At Gaussian
depth,

\[
 \lambda_H=e^{A^2}\bigl(1+O_A(m^{-1/2})\bigr).
 \tag{0.5}
\]

There is nevertheless an exact integer-hull obstruction.  The endpoint
\(t=1\) of (0.3) is an \(A\)-only fractional point satisfying owner
balance, flow, every lower-prefix cover, and exact signed cancellation.
Every integral point on that face is a union of \(A\)-orbits of length
\(2m\).  More sharply, if \(t_c\) is the number of selected orbits whose
fixed missing coordinate is \(c\), either any one exact signed-divergence
layer or the owner-incidence equations force

\[
 t_c=\frac{\operatorname{Cat}_m}{2m}
 \quad(c\in[n]),
 \qquad
 \operatorname{Cat}_m=\frac{W}{2m+1}.
 \tag{0.6}
\]

Thus \(2m\mid\operatorname{Cat}_m\) is necessary, not merely
\(2m\mid W\).

For every prime \(m=p>2\),

\[
                         \operatorname{Cat}_p\equiv2\pmod p,
 \tag{0.7}
\]

so the face is integer-empty.  Equivalently,

\[
                         \boxed{\sum_e z_{e,B}\ge1}
 \tag{0.8}
\]

is a valid inequality for the unrestricted integer hull and is violated
by the feasible fractional point.  Thus adding exact signed cancellation
does not repair the integrality gap.

The obstruction does not prove that the unrestricted mixed \(A/B\)
system is integer-infeasible.  It proves that LP, total-unimodularity,
or support-preserving rounding cannot establish it.  The exact remaining
object is an owner-simple cycle cover whose \(A\)-edges form a zero-sum
nested Johnson circulation while its state set covers every protected
lower prefix.  No coefficient-one conclusion is claimed.

## 1. The exact clustered state-transition system

Let \({\cal E}\) be the injective ordered \((n-1)\)-words on \([n]\).
For

\[
 e=(x_1,\ldots,x_{n-1})\in{\cal E},
\]

write \(x_n\) for its unique missing coordinate and set

\[
 S_Ae=(x_2,\ldots,x_{n-1},x_1),\qquad
 S_Be=(x_2,\ldots,x_{n-1},x_n).
 \tag{1.1}
\]

These are the two binary-rotor successors of the permutation state
\((x_1,\ldots,x_n)\).  Its middle-owner cluster is

\[
                         \kappa(e)=\{x_1,\ldots,x_m\}.
 \tag{1.2}
\]

Use variables \(z_{e,A},z_{e,B}\ge0\), and abbreviate

\[
                         y_e=z_{e,A}+z_{e,B}.
 \tag{1.3}
\]

The owner equations are

\[
 \sum_{e:\kappa(e)=X}y_e=1
 \qquad\left(X\in\binom{[n]}m\right).
 \tag{1.4}
\]

Exact state flow is

\[
 y_f=
 \sum_{\substack{e\in{\cal E},\ g\in\{A,B\}\\S_ge=f}}z_{e,g}
 \qquad(f\in{\cal E}).
 \tag{1.5}
\]

For \(0\le q\le H\), put \(r_q=m-q\) and define

\[
 p_q(e)=\{x_1,\ldots,x_{r_q}\}.
 \tag{1.6}
\]

The protected lower-prefix equations are the inequalities

\[
 \sum_{e:p_q(e)=S}y_e\ge1
 \qquad\left(S\in\binom{[n]}{r_q}\right).
 \tag{1.7}
\]

For a general rank \(r\le m\), write

\[
 L_r(T)=\sum_e y_e
 \mathbf1_{\{\{x_1,\ldots,x_r\}=T\}},
 \tag{1.8}
\]

and let the complementary upper-prefix load be

\[
 R_r(T)=\sum_e y_e
 \mathbf1_{\{\{x_{n-r+1},\ldots,x_{n-1},x_n\}=T\}}.
 \tag{1.9}
\]

To encode signed cancellation, put

\[
 K_q(e)=\{x_{n-r_q+1},\ldots,x_{n-1}\},
 \tag{1.10}
\]

which has size \(r_q-1\), and define

\[
 d_{q,T}(e)=
 \mathbf1_{\{T=K_q(e)\cup\{x_n\}\}}
 -\mathbf1_{\{T=K_q(e)\cup\{x_1\}\}}.
 \tag{1.11}
\]

The signed divergence vector is

\[
 D_{q,T}(z)=\sum_e z_{e,A}d_{q,T}(e).
 \tag{1.12}
\]

The exact-cancellation polyhedron \({\cal P}_H^0\) consists of
(1.4), (1.5), (1.7), nonnegativity, and

\[
 D_{q,T}(z)=0
 \qquad\left(0\le q\le H,
              T\in\binom{[n]}{r_q}\right).
 \tag{1.13}
\]

The definition is physical, not a formal auxiliary condition.

### Lemma 1.1 (fractional signed-divergence identity)

For fractional as well as integral \(z\) satisfying state flow,

\[
                         R_{r_q}-L_{r_q}=D_q(z).
 \tag{1.14}
\]

#### Proof

For any consecutive internal block of positions, summing its set-valued
load against the outgoing masses \(y_e\) gives the same result after
shifting the block one position to the right.  Indeed, the shifted block
of \(e\) is the unshifted block of each successor \(S_ge\), and (1.5)
says that the total incoming transition mass at every successor equals
its outgoing mass.  Iterating identifies the lower-prefix load with the
load of the last internal \(r_q\)-block of the successor states.

For a transition out of \(e\), that last block is

\[
 \begin{cases}
 K_q(e)\cup\{x_1\},&g=A,\\
 K_q(e)\cup\{x_n\},&g=B.
 \end{cases}
 \tag{1.15}
\]

On the other hand, the complementary upper load \(R_{r_q}\) counts
\(K_q(e)\cup\{x_n\}\) against the full root mass
\(y_e=z_{e,A}+z_{e,B}\).  The \(B\)-terms cancel on subtraction, and
the remaining \(A\)-terms are exactly (1.12). \(\square\)

Thus (1.13) says that complementary upper load equals lower load target
by target.  In particular, (1.7) and (1.13) imply the corresponding
upper-prefix covers exactly.

For later use, \({\cal P}_H(\Delta)\) replaces (1.13) by

\[
 \frac12\sum_{q,T}|D_{q,T}(z)|\le\Delta.
 \tag{1.16}
\]

## 2. Exact Farkas dual for zero cancellation

Let \(u_{q,S}\ge0\) be lower-target weights, let
\(\phi=(\phi_e)_{e\in{\cal E}}\) be a free state potential, and let
\(\theta=(\theta_{q,T})\) be a free signed-divergence potential.  Define

\[
 \Lambda_u(e)=\sum_{q=0}^{H}u_{q,p_q(e)},
 \tag{2.1}
\]

\[
 \Gamma_\theta(e)=
 \sum_{q=0}^{H}
 \left(
  \theta_{q,K_q(e)\cup\{x_n\}}
  -\theta_{q,K_q(e)\cup\{x_1\}}
 \right),
 \tag{2.2}
\]

and

\[
 M_X(\phi,\theta,u)=
 \max_{\substack{e:\kappa(e)=X\\g\in\{A,B\}}}
 \left(
  \phi_e-\phi_{S_ge}+\Lambda_u(e)
  +\mathbf1_{\{g=A\}}\Gamma_\theta(e)
 \right).
 \tag{2.3}
\]

### Theorem 2.1 (arc-potential Farkas criterion)

The exact signed-cancellation system \({\cal P}_H^0\) is fractionally
feasible if and only if (0.1) holds for every
\(u\ge0\) and every free \(\phi,\theta\).

#### Proof

Give (1.4) free multipliers \(\alpha_X\), write (1.5) with outgoing
minus incoming orientation and give it free multipliers \(\phi_e\),
give (1.13) free multipliers \(\theta_{q,T}\), and give (1.7)
nonnegative multipliers \(u_{q,S}\).  The coefficient of \(z_{e,g}\)
is

\[
 \alpha_{\kappa(e)}+\phi_e-\phi_{S_ge}+\Lambda_u(e)
 +\mathbf1_{\{g=A\}}\Gamma_\theta(e).
 \tag{2.4}
\]

By Farkas' lemma, infeasibility is equivalent to the existence of these
multipliers for which every expression (2.4) is nonpositive while

\[
                         \sum_X\alpha_X+\sum_{q,S}u_{q,S}>0.
 \tag{2.5}
\]

For fixed \((\phi,\theta,u)\), the largest allowed owner multiplier is

\[
                         \alpha_X=-M_X(\phi,\theta,u).
 \tag{2.6}
\]

Substitution in (2.5) says exactly that (0.1) fails.  This proves both
directions. \(\square\)

The free \(\theta\) is essential.  It prices the *signed* vector before
an absolute value is taken; replacing it by nonnegative target prices
would describe two cover systems rather than cancellation.

## 3. Exact Farkas dual with an \(\ell^1\) cancellation budget

Introduce \(s_{q,T}^+,s_{q,T}^-\ge0\) and write

\[
 D_{q,T}(z)-s_{q,T}^++s_{q,T}^-=0,
 \tag{3.1}
\]

\[
 \sum_{q,T}(s_{q,T}^++s_{q,T}^-)\le2\Delta.
 \tag{3.2}
\]

These constraints are equivalent to (1.16): for fixed \(D\), their
minimum left side is \(\sum|D_{q,T}|\).

### Theorem 3.1 (budgeted Farkas criterion)

The system \({\cal P}_H(\Delta)\) is fractionally feasible if and only
if (0.2) holds for every \(u\ge0\), \(\eta\ge0\), every free \(\phi\),
and every \(\theta\) satisfying

\[
                         |\theta_{q,T}|\le\eta.
 \tag{3.3}
\]

#### Proof

Use the multipliers from Theorem 2.1 for the owner, flow, cover, and
(3.1) rows.  Write (3.2) as

\[
                  -\sum_{q,T}(s_{q,T}^++s_{q,T}^-)\ge-2\Delta
\]

and give it multiplier \(\eta\ge0\).  The coefficients of
\(s_{q,T}^+\) and \(s_{q,T}^-\) in a Farkas certificate are respectively

\[
                         -\theta_{q,T}-\eta,
 \qquad
                          \theta_{q,T}-\eta.
\]

Their required nonpositivity is precisely (3.3).  The certificate's
right-hand side is now

\[
                    \sum_X\alpha_X+\sum_{q,S}u_{q,S}-2\Delta\eta.
\]

Eliminate \(\alpha_X\) by (2.6).  A positive certificate exists exactly
when (0.2) fails. \(\square\)

At \(\Delta=0\), any free \(\theta\) is admitted by choosing
\(\eta\ge\|\theta\|_\infty\), and Theorem 3.1 reduces to Theorem 2.1.

There is a gauge-free form of the same criterion.  For every fixed
\(q\), adding a constant to all \(\theta_{q,T}\) leaves
\(\Gamma_\theta\) unchanged, because each Johnson edge in (1.11) has one
positive and one negative endpoint.  Define

\[
 \operatorname{osc}(\theta_q)
 =\max_T\theta_{q,T}-\min_T\theta_{q,T}.
 \tag{3.4}
\]

The least \(\eta\) for which constants can be added separately at every
depth so that (3.3) holds is

\[
                         \frac12\max_{0\le q\le H}
                         \operatorname{osc}(\theta_q).
\]

Consequently (0.2) is equivalently

\[
 \boxed{
 \sum_{q,S}u_{q,S}
 -\Delta\max_{0\le q\le H}\operatorname{osc}(\theta_q)
 \le\sum_XM_X(\phi,\theta,u)}
 \tag{3.5}
\]

for every \(u\ge0\) and free \(\phi,\theta\).  This is the sharp dual
penalty for one aggregate \(\ell^1\) cancellation budget; replacing the
maximum oscillation by a sum would describe separate per-depth budgets.

## 4. Uniform fractional domination and Gaussian accounting

There are

\[
                         D=m!(m+1)!
 \tag{4.1}
\]

states in every owner cluster.  For any \(t\in[0,1]\), define (0.3).

### Lemma 4.1 (the full uniform segment cancels exactly)

For every \(0\le t\le1\), the point \(z^t\) satisfies (1.4), (1.5),
(1.7), and (1.13).  Every lower target at depth \(q\) has load

\[
                         \lambda_q={W\over\binom n{m-q}}.
 \tag{4.2}
\]

#### Proof

Every state has total outgoing mass \(1/D\).  Since both \(S_A\) and
\(S_B\) permute \({\cal E}\), its total incoming mass is also \(1/D\).
This proves flow, while the cluster size proves (1.4).

For a fixed \(r\)-set \(S\), exactly \(r!(n-r)!\) states have prefix
set \(S\).  Hence its load is

\[
 \frac{r!(n-r)!}{D}=\frac{W}{\binom nr},
\]

which is (4.2) for \(r=m-q\) and is at least one.

For signed cancellation, define

\[
 \iota(x_1,x_2,\ldots,x_{n-1})
 =(x_n,x_2,\ldots,x_{n-1}).
 \tag{4.3}
\]

This fixed-point-free involution preserves every \(K_q\), exchanges the
first and missing coordinates, and therefore satisfies

\[
                         d_{q,T}(\iota(e))=-d_{q,T}(e)
 \tag{4.4}
\]

for every \(q,T\).  Since \(z^t_{e,A}=t/D\) is constant on each
\(\iota\)-pair, all signed divergences vanish. \(\square\)

### Theorem 4.2 (uniform domination of the Farkas dual)

For every \(\phi,\theta,u\), inequality (0.4) holds.

#### Proof

For each owner, the maximum (2.3) is at least its average with respect
to the unit owner mass \(z^t\).  Summing these averages gives

\[
\begin{aligned}
 \sum_XM_X(\phi,\theta,u)
 &\ge
 \sum_{e,g}z^t_{e,g}
 \left(
  \phi_e-\phi_{S_ge}+\Lambda_u(e)
  +\mathbf1_{\{g=A\}}\Gamma_\theta(e)
 \right)\\
 &=\sum_{q=0}^{H}\lambda_q\sum_Su_{q,S}.
\end{aligned}
 \tag{4.5}
\]

The flow term vanishes by (1.5), the signed term by (1.13), and the
prefix term is (4.2).  This proves (0.4). \(\square\)

Since \(\lambda_q\ge1\), (4.5) proves (0.1), and it also proves (0.2)
because \(-2\Delta\eta\le0\).  Thus neither the exact nor budgeted
fractional system has a separating Farkas functional.

Factorial cancellation gives

\[
 \lambda_q=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.
 \tag{4.6}
\]

Uniformly for \(q\le H\),

\[
 \log\lambda_q
 =\frac{q(q+1)}m+O_A\left(\frac{(q+1)^3}{m^2}\right).
 \tag{4.7}
\]

Therefore (0.5) follows, including the ceiling error.  The exact first
positive margin is

\[
                         \lambda_1=1+{2\over m}.
 \tag{4.8}
\]

For the unweighted lower functional \(u_{q,S}=1\), take
\(\phi=\theta=0\).  Every state collects exactly \(H+1\), so the exact
dual surplus over the required lower-target weight is

\[
 \sum_{q=0}^{H}\left(W-\binom n{m-q}\right).
 \tag{4.9}
\]

Equation (4.7) gives, uniformly on the Gaussian window,

\[
 {1\over W}\binom n{m-q}
 =e^{-q^2/m}\bigl(1+O_A(m^{-1/2})\bigr).
\]

A Riemann sum therefore turns (4.9) into

\[
 W\sqrt m\left(
 A-\int_0^Ae^{-x^2}\,dx
 \right)+O_A(W).
 \tag{4.10}
\]

This is strictly positive for every fixed \(A>0\).  Depth zero is the
only fractionally tight lower layer.

## 5. Exact integer-hull obstruction surviving cancellation

Impose the support-face equations

\[
                         z_{e,B}=0\qquad(e\in{\cal E}).
 \tag{5.1}
\]

### Theorem 5.1 (prime \(A\)-orbit obstruction)

The face (5.1) of \({\cal P}_H^0\) is fractionally nonempty for every
\(H\le m-1\).  If it has an integral point, and \(t_c\) denotes the
number of its selected \(A\)-orbits with fixed missing coordinate \(c\),
then

\[
                         t_c=\frac{\operatorname{Cat}_m}{2m}
 \qquad(c\in[n]).
 \tag{5.2}
\]

Consequently \(2m\mid\operatorname{Cat}_m\) is necessary, and the face
is integer-empty for every prime \(m>2\).

#### Proof

The endpoint \(t=1\) in Lemma 4.1 is a fractional point on (5.1), and
that lemma includes exact signed cancellation.

Let \(z\) be integral on this face.  State flow says that whenever the
\(A\)-transition out of \(e\) is selected, the \(A\)-transition out of
\(S_Ae\) is selected.  Thus the selected states are a union of complete
\(S_A\)-orbits.  The position rotor \(A\) is a \((2m)\)-cycle on the
first \(2m\) positions and fixes the last position, so every such orbit
has exact length \(2m\).

Summing the owner equations gives exactly \(W\) selected states.  If
\(T=\sum_ct_c\) is the total number of selected \(A\)-orbits, then

\[
                         T=\frac{W}{2m}
 =\frac{(2m+1)\operatorname{Cat}_m}{2m}.
 \tag{5.3}
\]

First use the signed-cancellation equations themselves.  Fix any
protected depth \(q\) and coordinate \(c\).  Sum (1.12) over all
\(r_q\)-sets containing \(c\).  In each switch flag, membership of
\(c\) in the common set \(K_q(e)\) cancels, giving

\[
 0=\sum_{T\ni c}D_{q,T}(z)
 =\sum_e z_{e,A}
 \left(\mathbf1_{\{x_n=c\}}-\mathbf1_{\{x_1=c\}}\right).
 \tag{5.4}
\]

In the selected \(A\)-orbits, the first count is \(2m t_c\).  Every
orbit whose missing coordinate is not \(c\) has exactly one rotated
state with first coordinate \(c\), whereas an orbit missing \(c\) has
none.  The second count is therefore \(T-t_c\).  Equation (5.4) yields

\[
                         2m t_c=T-t_c,
 \qquad t_c=\frac{T}{2m+1}
 =\frac{\operatorname{Cat}_m}{2m},
 \tag{5.5}
\]

which proves (5.2) directly from any one signed layer.

For completeness, the owner clusters force the same identity even
without (5.4).  Fix a coordinate \(c\) and sum the owner equations over
the \(m\)-sets which avoid \(c\).  There are
\(\binom{2m}{m}\) such owners.  An \(A\)-orbit whose missing coordinate
is \(c\) contributes all its \(2m\) states to this sum.  An orbit whose
missing coordinate is \(d\ne c\) cyclically rotates all coordinates
except \(d\); exactly \(m\) of its \(2m\) length-\(m\) cyclic intervals
avoid \(c\).  Therefore

\[
 \binom{2m}{m}
 =2m t_c+m\sum_{d\ne c}t_d
 =m(T+t_c).
 \tag{5.6}
\]

Since

\[
 \binom{2m}{m}=(m+1)\operatorname{Cat}_m,
\]

substitution of (5.3) into (5.6) gives (5.2).  In particular the
integer \(t_c\) forces \(2m\mid\operatorname{Cat}_m\).

If \(m=p>2\) is prime, then modulo \(p\),

\[
 (1+x)^{2p}=((1+x)^p)^2\equiv(1+x^p)^2.
 \tag{5.7}
\]

The coefficient of \(x^p\) gives \(\binom{2p}{p}\equiv2\pmod p\).
Because

\[
 \operatorname{Cat}_p=\frac1{p+1}\binom{2p}{p}
\]

and \(p+1\equiv1\pmod p\), this proves (0.7).  Hence
\(p\nmid\operatorname{Cat}_p\), contradicting the necessary divisibility
\(2p\mid\operatorname{Cat}_p\). \(\square\)

### Corollary 5.2 (valid inequality for the unrestricted integer hull)

For every prime \(m>2\), every integral feasible point of the full
mixed system obeys (0.8), while the feasible fractional endpoint
\(z^1\) violates it.

#### Proof

An integral point violating (0.8) has nonnegative integral \(B\)-mass
zero and hence lies on (5.1), contrary to Theorem 5.1.  The fractional
endpoint has zero \(B\)-mass by definition. \(\square\)

This proves that \({\cal P}_H^0\) is not the convex hull of its integral
points.  Indeed, a convex combination of nonnegative integral points
with zero average \(B\)-mass could use only integral points on the empty
face (5.1).  The same obstruction applies to every budget
\(\Delta\ge0\), since the separating fractional point already has
\(\Delta=0\).

## 6. Exact cycle master, a literal non-TU minor, and the residual gate

Let \(\mathscr C\) be the directed simple cycles of the binary-rotor
state graph.  For \(C\in\mathscr C\), define

\[
 a_X(C)=\#\{(e,g)\in C:\kappa(e)=X\},
 \tag{6.1}
\]

\[
 b_{q,S}(C)=\#\{(e,g)\in C:p_q(e)=S\},
 \qquad
 d_{q,T}(C)=\sum_{(e,A)\in C}d_{q,T}(e).
 \tag{6.2}
\]

Ordinary circulation decomposition shows that the exact fractional
cycle master is

\[
 \begin{aligned}
  &\sum_Ca_X(C)\xi_C=1 &&(X\in\tbinom{[n]}m),\\
  &\sum_Cb_{q,S}(C)\xi_C\ge1 &&(q,S),\\
  &\sum_Cd_{q,T}(C)\xi_C=0 &&(q,T),\\
  &\xi_C\ge0.
 \end{aligned}
 \tag{6.3}
\]

Its exact cycle-form Farkas alternative is: whenever free
\(\alpha_X,\theta_{q,T}\) and nonnegative \(u_{q,S}\) satisfy

\[
 \sum_Xa_X(C)\alpha_X+
 \sum_{q,T}d_{q,T}(C)\theta_{q,T}
 \ge\sum_{q,S}b_{q,S}(C)u_{q,S}
 \qquad(C\in\mathscr C),
 \tag{6.4}
\]

they must satisfy

\[
                         \sum_X\alpha_X\ge\sum_{q,S}u_{q,S}.
 \tag{6.5}
\]

This is equivalent to Theorem 2.1: summing an arc inequality around a
cycle removes the state potential, while circulation decomposition gives
the converse.

Requiring \(\xi_C\in\mathbb Z_{\ge0}\) makes (6.3) exactly the Boolean
clustered problem.  The owner right sides equal one, so every used cycle
is owner-simple and two used cycles have disjoint owner sets; they are
therefore also state-disjoint.  This is the precise integer semigroup in
which rounding remains open.

The integrality failure is also visible locally in the actual rotor
matrix.  Let

\[
 \pi^0=(1,2,\ldots,2m,2m+1),\qquad T=BA^{-1}.
\]

As a position permutation, \(T\) swaps the final two positions and
fixes the others.  Hence

\[
 \pi^0,A\pi^0,\ldots,A^{2m-1}\pi^0,
 T\pi^0,AT\pi^0,\ldots,A^{2m-1}T\pi^0
 \tag{6.6}
\]

is a simple directed rotor cycle of length \(4m\): the internal edges
are \(A\)-edges and the two joins are \(B\)-edges.  The middle owner
\([m]\) occurs exactly twice, once in each \(A\)-string.

Take the \(4m\) arc columns of this cycle, any \(4m-1\) of its state
incidence rows, and the owner row for \([m]\).  The state rows form a
directed cycle incidence matrix with one row deleted.  Its signed
cofactor vector is the all-ones vector, so expansion along the owner row
gives determinant \(\pm2\).  Thus the owner-flow matrix is not totally
unimodular.  Adding lower-prefix and signed-divergence rows cannot remove
this row-and-column minor.

There is nevertheless no integral obstruction on the lower-prefix side
alone.  Fix any symmetric-chain decomposition of \(2^{[n]}\).  Every
chain crosses ranks \(m\) and \(m+1\).  Order one permutation state per
chain by listing its bottom set first, then the successive chain
increments, and finally its unused coordinates.  The resulting \(W\)
states contain exactly one state over every middle owner and realize
every set in every rank as a prefix of the state belonging to its chain.
Hence owner transversality and all lower-prefix inequalities have a
common Boolean solution at every depth.

For a fixed such owner transversal \(P\), form the bipartite successor
graph with left and right copies of \(P\), joining \(e_L\) to
\((S_ge)_R\) whenever \(S_ge\in P\).  Rotor flow exists exactly when

\[
 |P\cap\{S_Ae,S_Be:e\in Q\}|\ge|Q|
 \qquad(Q\subseteq P).
 \tag{6.7}
\]

This is ordinary Hall.  Exact signed cancellation adds to the perfect
matching the zero-weight condition

\[
 \sum_{(e,S_ge)\text{ matched}}
 \mathbf1_{\{g=A\}}(d_{q,T}(e))_{q,T}=0.
 \tag{6.8}
\]

Thus the residual integral problem is a *zero-weight perfect matching
chosen simultaneously with the all-prefix owner transversal*.  The
uniform fractional point proves that its global relaxation has no dual
cut; Theorem 5.1 proves that its integer hull has rotor-orbit cuts not
generated by that relaxation.

## 7. Proved and unproved boundary

Proved here:

1. (1.4), (1.5), (1.7), and (1.13) are the exact clustered binary-rotor
   LP with targetwise signed-divergence cancellation.
2. Equation (0.1) is its exact Farkas dual.
3. Equation (0.2) is the exact extension for an aggregate
   \(\ell^1\)-cancellation budget.
4. The full uniform segment has exact cancellation and proves the
   quantitative domination (0.4), with Gaussian margin (0.5).
5. For infinitely many Gaussian-scale instances, the \(A\)-only face is
   fractionally feasible and integer-empty, yielding the integer-hull
   cut (0.8).
6. The actual matrix is non-TU, while owner plus lower-prefix coverage
   alone has an exact Boolean solution.

Not proved here:

1. infeasibility of the unrestricted mixed integral system;
2. a mixed integral solution with exact or \(o(W)\) signed divergence;
3. a solution with \(o(W/m)\) support components; or
4. the coefficient-one theorem.

The LP/Farkas rounding lane is therefore exhausted at its natural
boundary.  A positive theorem must round in the owner-simple,
zero-weight cycle semigroup, rather than in the ambient circulation
polytope.
