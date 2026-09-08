# The dominant two-scale cube: exact one-parent hinge and the surviving suffix dual

Date: 2026-07-26

Method: hand mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let \(r\) be minimal with

\[
                         d=C_r\ge 4p,
 \qquad                  c=C_{r-1}.
\tag{0.1}
\]

Then

\[
 {c\over d}={r+1\over2(2r-1)}>{1\over4},
 \qquad c>p,
 \qquad d-c>p.                                           \tag{0.2}
\]

For one scale-\(r\) parent \(C\), the complete matched-depth isolated
packet is

\[
 Z_C=c\,\partial_C(A_C+B_C)
       -\sum_{R\in\mathcal D_{r-1}}\partial_C
          (P^E_{C,R}+P^O_{C,R}),                         \tag{0.3}
\]

where

\[
 \partial_CK={\bf e}_{K\cup\{\gamma_C\}}
                 -{\bf e}_{K\cup\{\beta_C\}}.            \tag{0.4}
\]

Write \(\mu=\mu_r^{\rm MSW}\) for the physical canonical load. The exact
one-parent cap gain is

\[
\boxed{
 \begin{aligned}
 \Gamma_C={}&
 \Phi_c(\mu(A_C\beta),\mu(A_C\gamma))
 +\Phi_c(\mu(B_C\beta),\mu(B_C\gamma))\\
 &+\sum_{R\in\mathcal D_{r-1}}
   \left[
    \Phi_1(\mu(P^E_{C,R}\gamma),\mu(P^E_{C,R}\beta))
   +\Phi_1(\mu(P^O_{C,R}\gamma),\mu(P^O_{C,R}\beta))
   \right],
 \end{aligned}}                                         \tag{0.5}
\]

where juxtaposition means union with the displayed exceptional label and

\[
 \boxed{
 \Phi_t(u,v)=
 \min\{t,(u-p)_+\}
 -\bigl(t-(p-v)_+\bigr)_+.}                             \tag{0.6}
\]

Thus \(\Phi_t(u,v)\) is exactly the cap decrease obtained by moving \(t\)
units from a source of load \(u\) to a destination of load \(v\).

The complete endpoint classification forced by the parent packet is

\[
\begin{array}{c|c|c|c}
\text{arm}&\text{source}&\text{destination}&
       \text{physical canonical loads}\\ \hline
A_C& A_C\beta&A_C\gamma&d+\rho_A^-,\ c+\rho_A^+\\
B_C& B_C\beta&B_C\gamma&c+\rho_B^-,\ \rho_B^+\\
P^\epsilon_{C,R}&P^\epsilon_{C,R}\gamma&
 P^\epsilon_{C,R}\beta&1+\rho^\epsilon_{R,-},\
 \rho^\epsilon_{R,+}
\end{array}                                             \tag{0.7}
\]

for uniquely defined nonnegative integers \(\rho\). They count every
other canonical owner of the same physical target. In particular,

\[
 \boxed{\Phi_c(d+\rho_A^-,c+\rho_A^+)=0}                \tag{0.8}
\]

for all residuals, while a prefix term simplifies to

\[
 \boxed{
 \Phi_1(1+\rho_-,\rho_+)
   ={\bf1}_{\{\rho_-\ge p\}}
    -{\bf1}_{\{\rho_+\ge p\}}.}                         \tag{0.9}
\]

Thus packet-private support is not the same as physical load one.
Cross-parent and other-phase owners are precisely the residuals in
(0.7). Neither always-on nor always-off follows from the marked Catalan
profile.

There is, however, a background-independent protected-set witness. Put

\[
 \Omega_r=\{S:\mu(S)>p\},\qquad \alpha_r={\bf1}_{\Omega_r}.
\tag{0.10}
\]

The two marked boundary arms of every elementary scale-\(r\) rectangle
have all endpoints in \(\Omega_r\). Only its two opposite cyclic arms can
cross this cut. Hence

\[
 \boxed{
 \Gamma_C\le-\langle\alpha_r,Z_C\rangle\le2c.}           \tag{0.11}
\]

This is the correct full-four-arm replacement for the neutral marked-arm
calculation.

For every larger depth \(q\ge r\), the distinguished suffix arm survives
under suffix truncation and obeys

\[
 \alpha_q(A_{q,C}\beta_C)=
 \alpha_q(A_{q,C}\gamma_C)=1,
 \qquad \alpha_q={\bf1}_{\{\mu_q^{\rm MSW}>p\}}.         \tag{0.12}
\]

Therefore its cut derivative is exactly zero. At \(q>r\) no second
neutral arm has been proved, and the surviving conclusion is

\[
 \boxed{
 -\langle\alpha_q,Z_{q,C}\rangle\le3c.}                 \tag{0.13}
\]

The improvement \(3c\to2c\) is special to the matched depth. Equation
(0.12), not a nonlinear cap equality after arbitrary previous toggles, is
the identity which persists for \(q>r\).

For the adjacent-scale cube:

* at \(q=r\), a scale-\(r\) bit has protected drain at most \(2\), while
  a retained scale-\((r+1)\) bit has only the universal bound \(4\);
* at every \(q\ge r+1\), both scale-\(r\) and scale-\((r+1)\) bits have
  protected drain at most \(3\).

Thus the scalar four-units-per-rectangle count overstates directed
capacity by one unit at every later depth. Product biasing cannot remove
this loss because the same fixed \(\alpha_q\) witnesses every state and
every probability mixture.

## 1. Exact cap hinge for one transported arm

Suppose \(t\) occurrences are removed from a target of load \(u\) and
inserted at a target of load \(v\). Its cap-tail decrease is

\[
 \begin{aligned}
 &(u-p)_++(v-p)_+\\
 &\quad -(u-t-p)_+-(v+t-p)_+ .                          \tag{1.1}
 \end{aligned}
\]

The source releases at most \(t\) units and at most its original excess
\((u-p)_+\). The destination creates the part of \(t\) which does not fit
in its slack \((p-v)_+\). This proves (0.6).

At a proper rank, the four cores of one rectangle are distinct. Inside
one parent packet, fixed suffix endpoints are disjoint from all prefix
endpoints, while prefix endpoints recover their arm type and \(R\).
Applying (1.1) to the two \(c\)-fold suffix transports and the \(2c\)
unit prefix transports proves (0.5).

## 2. Canonical endpoint ledger

The signs in (0.3) matter. A positive \(\partial_CK\) moves load from
\(K\beta_C\) to \(K\gamma_C\), while \(-\partial_CK\) moves load from
\(K\gamma_C\) to \(K\beta_C\).

The distinguished suffix source \(A_C\beta_C\) contains the complete
first-return class of size \(C_r=d\), and its destination contains the
adjacent boundary class of size \(C_{r-1}=c\). Other canonical windows
can only add owners, so

\[
 \mu(A_C\beta_C)=d+\rho_A^-,\qquad
 \mu(A_C\gamma_C)=c+\rho_A^+ .                          \tag{2.1}
\]

Every one of the \(c\) switched rows supplies the old occurrence at
\(B_C\beta_C\). Thus

\[
 \mu(B_C\beta_C)=c+\rho_B^-,\qquad
 \mu(B_C\gamma_C)=\rho_B^+.                             \tag{2.2}
\]

For each \(R\) and \(\epsilon\in\{E,O\}\), the negative prefix arm has
one old occurrence at \(P^\epsilon_{C,R}\gamma_C\). Hence

\[
 \mu(P^\epsilon_{C,R}\gamma_C)=1+\rho^\epsilon_{R,-},
 \qquad
 \mu(P^\epsilon_{C,R}\beta_C)=\rho^\epsilon_{R,+}.      \tag{2.3}
\]

Equations (2.1)--(2.3) define the nonnegative residuals and prove (0.7).
The packet-private-prefix theorem says the certified occurrences in
(2.3) are distinct as \(R,\epsilon\) vary. It does not say the residuals
vanish: a target may have owners at other phases or in other parents.
Likewise, suffix cores erase \(R\), and literal cross-parent suffix
collisions occur at positive density. Therefore replacing physical loads
by the tagged values

\[
 (d,c),\qquad(c,0),\qquad(1,0)                          \tag{2.4}
\]

is not a valid cap calculation.

By (0.2), after the \(A_C\) source loses all \(c\) selected occurrences,
it still has load at least \(d-c>p\), while its destination began above
\(p\). The source releases \(c\) units of excess and the destination
creates exactly \(c\) units. This proves (0.8).

For a unit prefix arm, integrality and (0.6) give

\[
 \min\{1,(1+\rho_--p)_+\}={\bf1}_{\{\rho_-\ge p\}},
\]

and

\[
 \bigl(1-(p-\rho_+)_+\bigr)_+
       ={\bf1}_{\{\rho_+\ge p\}}.
\]

This proves (0.9). The prefix sign is exactly the difference of two
physical overload indicators. An inverse-owner theorem or a global
collision count is needed to choose it; the one-parent support theorem
alone cannot.

## 3. Optimal on/off bias

There are two notions of bias.

If the whole parent is a Bernoulli on/off packet \(X\in\{0,1\}\) with
\(\Pr(X=1)=\theta\), then

\[
 \mathbb E K_p(\mu+XZ_C)
   =(1-\theta)K_p(\mu)+\theta K_p(\mu+Z_C)
   =K_p(\mu)-\theta\Gamma_C.                             \tag{3.1}
\]

Consequently the exact unconstrained optimum is

\[
 \boxed{
 \theta^*=
 \begin{cases}
 1,&\Gamma_C>0,\\
 0,&\Gamma_C<0,\\
 \text{arbitrary},&\Gamma_C=0.
 \end{cases}}                                           \tag{3.2}
\]

There is no canonical nontrivial product bias without first determining
the residual loads in (0.7).

If instead one minimizes the cap tail of the mean histogram,

\[
 f_C(\theta)=K_p(\mu+\theta Z_C),\qquad0\le\theta\le1,  \tag{3.3}
\]

then \(f_C\) is convex and piecewise linear. Its subgradient is obtained
directly from (0.3):

\[
\begin{aligned}
 \partial f_C(\theta)={}&
 c\sum_{K\in\{A_C,B_C\}}
  \left[
   -\partial(x-p)_+\big|_{x=\mu(K\beta)-c\theta}
   +\partial(x-p)_+\big|_{x=\mu(K\gamma)+c\theta}
  \right]\\
 &+\sum_{R,\epsilon}
  \left[
   -\partial(x-p)_+\big|_{x=\mu(P^\epsilon_R\gamma)-\theta}
   +\partial(x-p)_+\big|_{x=\mu(P^\epsilon_R\beta)+\theta}
  \right].                                              \tag{3.4}
\end{aligned}
\]

The minimizers are exactly the \(\theta\) for which
\(0\in\partial f_C(\theta)\), with the usual endpoint alternatives.
Convexity does not create a universal bias; (3.4) still depends on the
physical residual loads.

## 4. The matched-depth protected-set witness

For any nonnegative histogram \(y\) and any \(0\le\alpha\le1\),

\[
 K_p(y)\ge\langle\alpha,y-p{\bf1}\rangle.               \tag{4.1}
\]

For \(\alpha_r={\bf1}_{\Omega_r}\), equality holds at \(\mu\). Therefore

\[
 \Gamma_C\le-\langle\alpha_r,Z_C\rangle.                \tag{4.2}
\]

Define

\[
 \nabla^\alpha_{\beta\gamma}(K)
  =\alpha(K\gamma)-\alpha(K\beta).                      \tag{4.3}
\]

Substituting (0.3) gives the exact packet cut ledger

\[
\boxed{
 -\langle\alpha,Z_C\rangle
 =\sum_{R,\epsilon}
     \nabla^\alpha_{\beta\gamma}(P^\epsilon_{C,R})
   -c\nabla^\alpha_{\beta\gamma}(A_C)
   -c\nabla^\alpha_{\beta\gamma}(B_C).}                 \tag{4.4}
\]

At \(q=r\), the two boundary Catalan profiles have marked loads

\[
                         (d,c,c),                       \tag{4.5}
\]

all strictly above \(p\). The two marked arms of each elementary
rectangle therefore have equal \(\alpha_r\)-value at source and
destination. Their contributions to (4.4), before packet telescoping,
are zero. Only two opposite arms remain, each draining at most one unit
of \(\alpha_r\)-mass. Summing over the \(c\) rectangles proves

\[
 -\langle\alpha_r,Z_C\rangle\le2c,                      \tag{4.6}
\]

and hence (0.11). Treating the three unmarked summands visible after
(0.3) as independent would lose this exact two-arm neutrality.

For the pruned adjacent-scale cube, let \(M_r\) be the number of retained
scale-\(r\) bits and \(\widetilde M_{r+1}\) the number of retained
scale-\((r+1)\) bits. A scale-\((r+1)\) bit at depth \(r\) has only the
universal four-arm bound. Thus every state and probability mixture
satisfies

\[
 \boxed{
 K_{r,p}\ge
 H_{m,r}(d/2-p)-2M_r-4\widetilde M_{r+1}.}              \tag{4.7}
\]

This is the promised \(\alpha\)-dual answer when the residual owner
counts in (0.7) have not been explicitly inverted.

## 5. The identity which survives above the matched depth

Let \(s\in\{r,r+1\}\) be a switch scale and \(q\ge s\). The isolated
column retains the prefix/suffix form

\[
 a_{q,C,R}=\partial_C(A_{q,C,s}+B_{q,C,s})
 -\partial_C(P^E_{q,C,R,s}+P^O_{q,C,R,s}).              \tag{5.1}
\]

Increasing \(q\) shortens each suffix inside the exterior tail; it does
not inspect \(R\). The distinguished \(A\)-arm remains the projection of
the two boundary Catalan classes with canonical loads at least

\[
                         C_s,\qquad C_{s-1}.             \tag{5.2}
\]

For \(s=r\) or \(r+1\), both exceed \(p\). Hence

\[
 \nabla^{\alpha_q}_{\beta\gamma}(A_{q,C,s})=0,          \tag{5.3}
\]

which is (0.12).

The other three arm derivatives lie in \(\{-1,0,1\}\). Therefore an
elementary column has protected drain at most three:

\[
 \alpha_q(N_{q,C,R})-\alpha_q(P_{q,C,R})\le3.           \tag{5.4}
\]

Summing (5.4) over a complete size-\(s\) parent gives (0.13), with
\(c=C_{s-1}\) at that scale.

Two limitations are essential.

1. Equation (5.3) concerns the fixed canonical overloaded set. After
   other toggles, the actual source can cross the cap, so (5.3) is not a
   statewise nonlinear zero-gain statement.
2. For \(q>s\), the second matched marked arm need not remain within the
   projected overloaded set. The bound three cannot be replaced by two
   without a new endpoint theorem.

If the tuned cube uses \(L_q\) isolated columns at depth \(q\ge r+1\), a
scalar audit credits \(4L_q\) units of drain, while the fixed dual credits
at most \(3L_q\). When scalar tuning spends essentially all four units,
the protected residual is at least

\[
                         (1-o(1))L_q                    \tag{5.5}
\]

before the separately audited boundary-interaction error. This is the
one-unit-per-column obstruction which persists across the growing depth
window and closes the literal adjacent-scale rectangle cube.

## 6. Final audit

1. The distinguished marked suffix transfer has full-parent cap gain
   exactly zero, not merely zero first derivative.
2. All other physical endpoint loads are represented exactly by the
   residual-owner variables in (0.7). Packet-private support does not set
   them to zero.
3. The exact full gain is (0.5). Its sign, and hence the exact optimal
   Bernoulli on/off choice, is not determined by the one-parent Catalan
   ledger alone.
4. The fixed overloaded-set potential supplies the required alternative:
   full scale-\(r\) parent gain is at most \(2c\) at \(q=r\).
5. At every \(q>r\), one saturated suffix derivative remains zero and
   yields the \(3c\) protected-drain ceiling. No stronger persistent sign
   identity is justified.

Thus the dominant two-scale cube has ample scalar four-arm capacity but
not four units of directed capacity per bit. The missing unit is a
literal saturated suffix arm, and neither product bias nor an owner-blind
one-parent calculation can recover it.
