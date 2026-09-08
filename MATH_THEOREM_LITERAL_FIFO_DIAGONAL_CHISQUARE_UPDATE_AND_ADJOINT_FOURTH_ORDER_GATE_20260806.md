# Literal FIFO diagonal chi-square update and the adjoint fourth-order gate

**Date:** 2026-08-06  
**Method:** exact survivor-multiplier expansion of the authenticated
exponential-clock state; no computation or search  
**Status:** unconditional identity and a correction to the proposed
`Rq+r` response picture.  The natural FIFO update is diagonal on resource
labels.  Its residual is an adjoint hazard-discrepancy square involving
two composite rows sharing one resource.  It does not in general factor
through the current complete-row switch scores.  Complete-row blocker
conjugation therefore does not by itself close the direct chi-square gate.

## 1. Authoritative incidence and root measures

At a fixed stopped state let \(\mathfrak A_i\) be the occurrence-labelled
composite rows and let

\[
 z_A(x)={\bf1}_{\{x\in U_A^\circ\cap T\}},
 \qquad
 \mu_A=c_i(A)R_i(A)\ge0.
\tag{1.1}
\]

The normalized-gradient incidence measure is exactly

\[
                         g_x=\sum_A\mu_Az_A(x).
\tag{1.2}
\]

The reference root measure is

\[
                         Y_x=\sum_{E\ni x}a_E(i).
\tag{1.3}
\]

Put

\[
 \beta={\sum_xg_x\over\sum_xY_x},
 \qquad c_x=\beta Y_x,
 \qquad f_x={g_x-c_x\over c_x}.
\tag{1.4}
\]

These are the definitions in the joint-Lyapunov and normalized-incidence
notes.

Fix one accepted transition \(G\).  Define its **literal composite-row
multiplier** by

\[
 \theta_A^G=
 \begin{cases}
 \mu_{i+1}^G(A)/\mu_i(A),&A\text{ survives }G,\\
 0,&A\text{ is killed by }G,
 \end{cases}
\tag{1.5}
\]

with the zero convention when \(\mu_i(A)=0\).  This includes the exact
deterministic density/future-fugacity update.  Equivalently, on a surviving
row the recursion \(c_{i+1}=c_iR_i\) supplies the first factor and the next
future multiplier supplies the rest.  Nothing below needs those factors
separated.

Likewise define the literal atomic-edge multiplier

\[
 \kappa_E^G=
 \begin{cases}
 a_E(i+1)/a_E(i),&E\text{ survives }G,\\
 0,&E\text{ is killed by }G.
 \end{cases}
\tag{1.6}
\]

Then the authenticated survivor updates are exactly

\[
 g_x'=\sum_A\mu_Az_A(x)\theta_A^G,
 \qquad
 Y_x'=\sum_{E\ni x}a_E(i)\kappa_E^G.
\tag{1.7}
\]

This is merely the definition of the next available-row and available-edge
sums.  It introduces no approximation.

## 2. Conditional survival ratios

When \(g_x>0\) and \(Y_x>0\), put

\[
 u_x^G={g_x'\over g_x}
       ={\sum_A\mu_Az_A(x)\theta_A^G
          \over\sum_A\mu_Az_A(x)},
 \qquad
 v_x^G={Y_x'\over Y_x}
       ={\sum_{E\ni x}a_E(i)\kappa_E^G
          \over\sum_{E\ni x}a_E(i)}.
\tag{2.1}
\]

Thus \(u_x^G\) is the conditional mean composite-row multiplier seen
from an incidence at \(x\), while \(v_x^G\) is the conditional mean
atomic-edge multiplier seen from the root \(x\).

Let \(\beta'=(\sum_xg_x')/(\sum_xY_x')\) and define

\[
                         r_x^G={\beta'\over\beta}v_x^G.
\tag{2.2}
\]

Then, literally,

\[
                         g_x'=u_x^Gg_x,
 \qquad                 c_x'=r_x^Gc_x.
\tag{2.3}
\]

Dead coordinates are omitted.  If \(g_x=0\), no positive row in (1.2)
contains \(x\), so \(g_x'=0\); set \(u_x^G=0\).

## 3. Exact diagonal residual identity

The natural reference transport is diagonal:

\[
                         J_{xx}^G=c_x'=r_x^Gc_x.
\tag{3.1}
\]

It transports the old centered likelihood error to \(c_x'f_x\).  Define

\[
                         h_x^G=g_x(u_x^G-r_x^G).
\tag{3.2}
\]

### Theorem 3.1 (literal FIFO chi-square identity)

One has

\[
 \boxed{e_x'=c_x'f_x+h_x^G.}
\tag{3.3}
\]

Consequently, with

\[
 \mathcal S_G=\sum_xr_x^Gc_xf_x^2,
 \qquad
 \mathcal K_G=\sum_x{g_x^2\over c_x'}(u_x^G-r_x^G)^2,
\tag{3.4}
\]

the next chi-square potential satisfies the exact identity

\[
 \boxed{
 \Psi'=\mathcal S_G
 +2\sum_xg_xf_x(u_x^G-r_x^G)
 +\mathcal K_G.}
\tag{3.5}
\]

Equivalently,

\[
 \mathcal K_G
 =\sum_xc_x{(1+f_x)^2\over r_x^G}
                  (u_x^G-r_x^G)^2.
\tag{3.6}
\]

#### Proof

Using (2.3) and \(g_x=c_x(1+f_x)\),

\[
 \begin{aligned}
 e_x'
 &=u_x^Gg_x-r_x^Gc_x\\
 &=r_x^Gc_xf_x+c_x(1+f_x)(u_x^G-r_x^G)\\
 &=c_x'f_x+g_x(u_x^G-r_x^G).
 \end{aligned}
\]

This is (3.3).  Square it, divide by \(c_x'\), and sum.  The first square
is \(\mathcal S_G\), the second is \(\mathcal K_G\), and the cross term
is the middle term in (3.5).  Equation (3.6) is (1.4). \(\square\)

This is the literal version of the Bregman identity.  It has no auxiliary
switch generator and no unspecified response map.

## 4. Direct stopped criterion with exact constants

Let \(a_i=\rho_i^2\), \(h_i=1-a_i\), and put

\[
 D_i=\sum_xc_xf_x^2\bigl(\mathbb E_i r_x^G-a_i\bigr),
 \qquad
 K_i=\mathbb E_i\mathcal K_G.
\tag{4.1}
\]

Thus \(\mathbb E_i\mathcal S_G=a_i\Psi_i+D_i\).

### Theorem 4.1 (diagonal service plus adjoint mismatch)

For every stopped state,

\[
 \boxed{
 \mathbb E_i\Psi_{i+1}
 \le\left(1-{h_i\over2}\right)\Psi_i
       +{3\over2}(D_i)_+ +{3\over h_i}K_i.}
\tag{4.2}
\]

Hence, for every finite stopped time \(\tau\),

\[
 \boxed{
 \mathbb E\sum_{i<\tau}h_i\Psi_i
 \le2\Psi_0+3\mathbb E\sum_{i<\tau}(D_i)_+
       +6\mathbb E\sum_{i<\tau}{K_i\over h_i}.}
\tag{4.3}
\]

#### Proof

For \(t>0\), (3.3) and the two-vector Young inequality give

\[
 \Psi'\le(1+t)\mathcal S_G+(1+t^{-1})\mathcal K_G.
\]

Take conditional expectations and choose \(t=h_i/2\).  Since
\(a_i=1-h_i\) and \(0<h_i\le1\),

\[
 (1+h_i/2)a_i\le1-h_i/2,
 \qquad
 1+h_i/2\le3/2,
 \qquad
 1+2/h_i\le3/h_i.
\]

This proves (4.2).  Sum the drift, discard the nonnegative terminal
potential, and multiply by two to obtain (4.3). \(\square\)

For example, if

\[
 (D_i)_+\le\eta_Dh_i\Psi_i+h_iJ_i^D,
 \qquad
 K_i\le\eta_Kh_i^2\Psi_i+h_iJ_i^K,
\tag{4.4}
\]

and

\[
                         {3\over2}\eta_D+3\eta_K<\frac12,
\tag{4.5}
\]

then the service absorbs both errors.  The concrete choice
\(\eta_D=\eta_K=1/12\) leaves service coefficient \(1/8\).
Together with \(X_ih_i\asymp1\), this proves `GDIR` from the cumulative
\(J^D+J^K\) budget.

## 5. The adjoint fourth-order kernel

The mismatch in (3.2) has the exact row expansion

\[
 \boxed{
 h_x^G=\sum_A\mu_Az_A(x)(\theta_A^G-r_x^G).}
\tag{5.1}
\]

Therefore

\[
 \boxed{
 \mathcal K_G
 =\sum_{A,B}\mu_A\mu_B
   \sum_{x\in U_A^\circ\cap U_B^\circ\cap T}
   { (\theta_A^G-r_x^G)(\theta_B^G-r_x^G)
      \over c_x'}.}
\tag{5.2}
\]

This is an adjoint selected-relation form:

* two composite rows \(A,B\) share the output resource \(x\);
* the same accepted transition \(G\) supplies both survivor multipliers;
* the denominator is the literal next reference mass \(c_x'\); and
* the scalar normalization of \(\beta'\) is already included in \(r_x^G\).

If one composite row stores two host edges, (5.2) is fourth order in the
host-row weights before the selected transition is exposed.  This is the
same algebraic degree diagnosed by the old normalized-gradient kernel,
but (5.2) is now the exact one-step coefficient rather than an abstract
operator surrogate.

## 6. Why complete-row switch scores are not the literal response state

Complete-row blocker conjugation controls the primal quantities

\[
 (Kf)(A)-(Kf)(\tau A)
 =\sum_x(z_A(x)-z_{\tau A}(x))f_x.
\tag{6.1}
\]

The literal mismatch (5.1) is instead the adjoint hazard current

\[
 K^*\bigl(\mu_A\theta_A^G\bigr)
 -D_{r^G}K^*\mu.
\tag{6.2}
\]

There is no algebraic identity turning (6.2) into a matrix applied to the
vector (6.1).  Such an identity would be a new normal equation relating
the survivor multipliers to the present likelihood profile; it is not a
consequence of the survivor update.

### Proposition 6.1 (balanced-state innovation obstruction)

There is a finite incidence update with \(f=0\), hence every current
complete-row score in (6.1) equal to zero, but with \(\mathcal K_G>0\).

#### Proof

Use four resource coordinates and two positive composite rows

\[
 U_A=\{1,2\},\qquad U_B=\{3,4\},\qquad \mu_A=\mu_B=1.
\]

Give \(A,B\) distinct private blocker tags outside this resource type.
Take \(Y=(1,1,1,1)\).  Then

\[
 g=(1,1,1,1),\qquad \beta=1,\qquad c=g,qquad f=0.
\]

Accept a transition containing only the private tag of \(A\).  Let the
reference root edges survive unchanged.  Then

\[
 g'=(0,0,1,1),\qquad Y'=Y,qquad
 \beta'={1\over2},\qquad c'=(1/2,1/2,1/2,1/2).
\]

Thus

\[
 e'=(-1/2,-1/2,1/2,1/2),
 \qquad
 \mathcal K_G=\Psi'=2.
\]

Every quantity in (6.1) is zero because \(f=0\). \(\square\)

The example is an incidence-process obstruction, not a claim that this
two-row toy is a complete balanced-doublet orbit.  It proves the exact
logical point: a factorization

\[
                         h'=Rq
\]

through current complete-row scores is false without a separate
innovation term.  That innovation can be as large as the entire next
chi-square creation even when the reference roots do not move.

## 7. Consequence for the response-aperture programme

The physical-response Schur theorem remains valid as a sufficient theorem
for any part of the mismatch which really has an `Rq` factorization.
The authenticated FIFO update, however, first produces the decomposition

\[
 \boxed{
 \text{diagonal reference service }D_i
 \quad+\quad
 \text{adjoint survivor discrepancy }K_i,}
\tag{7.1}
\]

not a canonical full `Rq` response.

Therefore the weakest literal analytic target is

\[
 \boxed{
 \mathbb E\sum_{i<\tau}(D_i)_+
 +\mathbb E\sum_{i<\tau}{K_i\over1-a_i}
 =O(\mathsf A),}
\tag{7.2}

or the absorbable local form (4.4)--(4.5).

The first term is the inhomogeneous one-root/reference hazard row.  The
second is the exact fourth-order common-incidence survivor carré (5.2).
`ROc` and `FE3` identify its one- and two-entry subfaces, but no current
theorem bounds the whole form with its next-reference denominator.

Complete-row blocker conjugation can still be used after a literal
polarization of a subfamily of (5.2) into conjugate rows.  It cannot replace
(5.2) wholesale, because arbitrary pairs \(A,B\) sharing \(x\) need not
be coordinate conjugates and the balanced-state innovation in Proposition
6.1 has no current row-score signal.

## 8. Proof boundary

The identity-level gate is now closed: the actual normalized-incidence
residual has the explicit formulas (3.2) and (5.1)--(5.2).  Those formulas
also prove a minimal obstruction to the earlier hoped-for full `Rq`
factorization.

The remaining analytic theorem is precisely the cumulative bound (7.2),
with (5.2) split by earliest physical blocker into:

1. conjugate complete-row faces paid by blocker conjugation;
2. one-/two-entry faces paid by `ROc`/`FE3`; and
3. the residual nonconjugate pair-of-composite-rows face.

Only the third face is new.  It is a literal fourth-order
selected-relation estimate, not an auxiliary switch-normalization problem.
