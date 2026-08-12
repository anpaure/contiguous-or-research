# Conditioned survivor coarea and the second-incidence codegree gate

**Date:** 2026-08-06  
**Method:** conditional centering at a live output resource, covariance
cancellation, and a two-anchor coarea expansion; no computation or search  
**Status:** unconditional positive reduction for the raw survivor part of
the literal adjoint carré.  Independent one-sided row kills cancel after
the correct conditioning.  The residual is an explicit positive
second-incidence codegree form.  Its conjugate subface is compatible with
complete-row blocker conjugation, but the nonconjugate codegree form is not
bounded by the present `ROc`/`FE3` statements.

## 1. Raw survivor multipliers

Fix a stopped state and one resource type.  Retain

\[
 z_A(x)={\bf1}_{\{x\in U_A^\circ\cap T\}},
 \qquad
 g_x=\sum_A\mu_Az_A(x),
 \qquad
 c_x=\beta Y_x.
\tag{1.1}
\]

Write \(S_A\) for the full literal physical support whose consumption
kills row \(A\), and put

\[
                         \chi_A(y)={\bf1}_{\{y\in S_A\}}.
\tag{1.1a}
\]

Thus \(z_A\) records the chosen output incidence type, while \(\chi_A\)
records all non-slot, owner, root, and slot resources relevant to row
survival.  Conflating these two incidence maps would omit cross-type
blockers.

Let the next accepted edge be \(G\), chosen with probabilities

\[
                         p_G={a_G\over X}.
\tag{1.2}
\]

On the raw process, the composite-row multiplier has the form

\[
                         \theta_A^G=t_A
             {\bf1}_{\{G\cap S_A=\varnothing\}},
\tag{1.3}
\]

where \(t_A\) is the deterministic density/future-fugacity multiplier
for this step.  On the common stopped interval,

\[
                         0<t_A\le C_t.
\tag{1.4}
\]

Analytical bad killing is an additional nonpositive survivor deletion and
must remain in its separately named injection; it is not included in this
raw identity.

For a live resource \(x\), let

\[
 L_x=\{G:x\notin G\},
 \qquad p_x=\Pr_i(L_x)>0.
\tag{1.5}
\]

Every row counted by \(z_A(x)\) contains the physical resource \(x\) in
its kill support.
On \(L_x\), such a row is killed precisely when \(G\) meets
\(S_A-\{x\}\).

Define the multiplier centered under the correct live-output law:

\[
 \bar\theta_A^x=\mathbb E_i(\theta_A^G\mid L_x),
 \qquad
 \widetilde\theta_A^{G,x}=\theta_A^G-\bar\theta_A^x.
\tag{1.6}
\]

## 2. Three-part decomposition of the literal mismatch

Recall from the literal diagonal theorem that

\[
                         h_x^G=\sum_A\mu_Az_A(x)
                                      (\theta_A^G-r_x^G),
\tag{2.1}
\]

where \(c_x'=r_x^Gc_x\).  Put

\[
 \bar r_x=\mathbb E_i(r_x^G\mid L_x).
\tag{2.2}
\]

For \(G\in L_x\), split

\[
 \theta_A^G-r_x^G
 =\widetilde\theta_A^{G,x}
  +(\bar\theta_A^x-\bar r_x)
  +(\bar r_x-r_x^G).
\tag{2.3}
\]

Define

\[
 \begin{aligned}
 \mathcal C_i
 &=\mathbb E_i\sum_{x:G\in L_x}{1\over c_x'}
   \left(\sum_A\mu_Az_A(x)\widetilde\theta_A^{G,x}\right)^2,\\
 \mathcal M_i
 &=\mathbb E_i\sum_{x:G\in L_x}{1\over c_x'}
   \left(\sum_A\mu_Az_A(x)(\bar\theta_A^x-\bar r_x)\right)^2,\\
 \mathcal R_i
 &=\mathbb E_i\sum_{x:G\in L_x}{g_x^2\over c_x'}
                 (r_x^G-\bar r_x)^2.
 \end{aligned}
\tag{2.4}
\]

The literal mismatch carré satisfies

\[
 \boxed{K_i\le3(\mathcal C_i+\mathcal M_i+\mathcal R_i).}
\tag{2.5}
\]

The last two terms are, respectively, the conditional mean
incidence-hazard defect and the reference/root carré.  The new positive
content is \(\mathcal C_i\).

The centered term has a stronger property which must be used before
Young's inequality.

### Lemma 2.1 (the centered linear cross vanishes)

Let

\[
 h_{x}^{\rm cen}(G)=
 {\bf1}_{L_x}\sum_A\mu_Az_A(x)
                       \widetilde\theta_A^{G,x}.
\tag{2.6}
\]

Then

\[
 \boxed{
 \mathbb E_i\sum_x f_xh_x^{\rm cen}(G)=0.}
\tag{2.7}
\]

#### Proof

The current \(f_x\) is predictable.  By (1.6),

\[
 \mathbb E_i[{\bf1}_{L_x}\widetilde\theta_A^{G,x}]
 =p_x\mathbb E_i[\theta_A^G-\bar\theta_A^x\mid L_x]=0.
\]

Multiply by \(f_x\mu_Az_A(x)\) and sum. \(\square\)

This removes a factor \(h_i^{-1}\) from the survivor fluctuation.  It is
the main advantage of conditional live-output centering.

### Theorem 2.2 (refined direct chi-square drift)

Put \(h_i=1-a_i\), and let \(D_i\) be the diagonal-service defect from
(4.1) of the literal diagonal theorem.  Define

\[
 \mathcal Q_i=\mathbb E_i\sum_{x:G\in L_x}{1\over c_x'}
 \left[
   \sum_A\mu_Az_A(x)(\bar\theta_A^x-\bar r_x)
   +g_x(\bar r_x-r_x^G)
 \right]^2.
\tag{2.8}
\]

Then

\[
 \boxed{
 \mathbb E_i\Psi_{i+1}
 \le\left(1-{h_i\over2}\right)\Psi_i
   +{3\over2}(D_i)_+ +2\mathcal C_i+{4\over h_i}\mathcal Q_i.}
\tag{2.9}
\]

Moreover,

\[
                         \mathcal Q_i\le2(\mathcal M_i+\mathcal R_i).
\tag{2.10}
\]

#### Proof

Write the exact residual as \(h^{\rm cen}+q\), where \(q\) is the sum of
the last two terms in (2.3).  The exact diagonal identity gives

\[
 \Psi'=\mathcal S_G+2\sum_xf_x(h_x^{\rm cen}+q_x)
             +\|h^{\rm cen}+q\|_{c'^{-1}}^2.
\]

After conditional expectation, Lemma 2.1 deletes the first cross term.
Use

\[
 \|h^{\rm cen}+q\|^2\le2\|h^{\rm cen}\|^2+2\|q\|^2
\]

and, for \(t>0\),

\[
 2\left|\sum_xf_xq_x\right|
 \le t\sum_xc_x'f_x^2+t^{-1}\sum_x{q_x^2\over c_x'}.
\]

Take \(t=h_i/2\).  As in the literal diagonal theorem,

\[
 (1+h_i/2)a_i\le1-h_i/2,
 \quad 1+h_i/2\le3/2,
 \quad 2+2/h_i\le4/h_i.
\]

This proves (2.9).  Equation (2.10) is
\((u+v)^2\le2u^2+2v^2\). \(\square\)

After summing to a stopped time,

\[
 \boxed{
 \mathbb E\sum_{i<\tau}h_i\Psi_i
 \le2\Psi_0+3\mathbb E\sum_i(D_i)_+
    +4\mathbb E\sum_i\mathcal C_i
    +8\mathbb E\sum_i{\mathcal Q_i\over h_i}.}
\tag{2.11}
\]

Thus only the conditional mean/reference part pays the service denominator.
The centered survivor carré \(\mathcal C_i\) is a one-step action term.

## 3. Conditional covariance cancellation

For rows \(A,B\) containing \(x\), put

\[
 H_A^x=\{G\in L_x:G\cap(S_A-\{x\})\ne\varnothing\}.
\tag{3.1}
\]

### Lemma 3.1 (only simultaneous off-root hits survive)

One has

\[
 \boxed{
 \mathbb E_i\!\left[
  {\bf1}_{L_x}\widetilde\theta_A^{G,x}
                   \widetilde\theta_B^{G,x}\right]
 \le C_t^2\Pr_i(L_x\cap H_A^x\cap H_B^x).}
\tag{3.2}
\]

#### Proof

Conditional on \(L_x\),

\[
 \theta_A^G=t_A(1-{\bf1}_{H_A^x}),
 \qquad
 \theta_B^G=t_B(1-{\bf1}_{H_B^x}).
\]

Therefore

\[
 \begin{aligned}
 &\mathbb E_i[{\bf1}_{L_x}\widetilde\theta_A^{G,x}
                  \widetilde\theta_B^{G,x}]\\
 &\qquad=p_xt_At_B
   \operatorname {Cov}_i({\bf1}_{H_A^x},{\bf1}_{H_B^x}\mid L_x)\\
 &\qquad=t_At_B\left(
   \Pr_i(L_x\cap H_A^x\cap H_B^x)
   -{\Pr_i(L_x\cap H_A^x)\Pr_i(L_x\cap H_B^x)\over p_x}
                 \right).
 \end{aligned}
\]

Discard the nonpositive product and use (1.4). \(\square\)

The conditioning on \(L_x\) is load-bearing.  Centering under the
unconditional law leaves a spurious product involving the event that
\(G\) itself consumes \(x\), although that coordinate is absent from the
next chi-square sum.

## 4. Two-anchor coarea

Define the second-incidence weight

\[
                         g_{x,y}^{(2)}
 =\sum_A\mu_Az_A(x)\chi_A(y).
\tag{4.1}
\]

For physical resources \(y,z\), put

\[
 Y_y=\sum_{G:y\in G}a_G,
 \qquad
 Y_{y,z}=\sum_{G:\{y,z\}\subseteq G}a_G.
\tag{4.2}
\]

Assume the live-reference lower bound

\[
                         c_x'\ge c_r c_x
 \quad\text{whenever }G\in L_x,
\tag{4.3}
\]

for an absolute \(c_r>0\).  This is the ordinary next-load/scalar stop;
if it is not part of the common stopping time, (4.3) must remain an
explicit premise.

### Theorem 4.1 (positive coarea bound)

Under (1.4) and (4.3),

\[
 \boxed{
 \begin{aligned}
 \mathcal C_i\le {C\over X}\sum_x{1\over c_x}
 \Bigg[{}
 &\sum_{y\ne x}Y_y\bigl(g_{x,y}^{(2)}\bigr)^2\\
 &+\sum_{\substack{y,z\ne x\\y\ne z}}
      Y_{y,z}g_{x,y}^{(2)}g_{x,z}^{(2)}
 \Bigg].
 \end{aligned}}
\tag{4.4}
\]

#### Proof

Expand \(\mathcal C_i\) in the pair of rows \(A,B\).  By (4.3) and
Lemma 3.1, its \((A,B,x)\) coefficient is at most

\[
 {C\mu_A\mu_Bz_A(x)z_B(x)\over c_x}
 \Pr_i(L_x\cap H_A^x\cap H_B^x).
\tag{4.5}
\]

On the event in (4.5), choose

\[
 y\in G\cap(S_A-\{x\}),
 \qquad
 z\in G\cap(S_B-\{x\}).
\]

If \(y=z\), the total transition probability of edges containing \(y\)
is \(Y_y/X\).  Summing \(A,B\) gives
\((g_{x,y}^{(2)})^2\).

If \(y\ne z\), the total transition probability of edges containing both
is \(Y_{y,z}/X\).  Summing \(A\) gives \(g_{x,y}^{(2)}\), and summing
\(B\) gives \(g_{x,z}^{(2)}\).  Union-bounding over the choices of
anchors gives (4.4). \(\square\)

No inverse Johnson gap and no arbitrary switch conductance appears.  The
two lines in (4.4) are literal:

1. a shared secondary resource \(y\) in both composite rows; or
2. two distinct resources \(y,z\) hit by the same accepted edge.

## 5. Conjugate and nonconjugate faces

In the expansion before (4.4), split pairs \((A,B)\) into:

* \(B=\tau A\) for a declared complete coordinate conjugation;
* named rooted/marked one- and two-entry faces; and
* all remaining nonconjugate pairs.

The first family has the exact first-kill coefficient used by complete-row
blocker conjugation after the corresponding polarization is retained.  The
second family is the declared `ROc`/`FE3`/root/slot input.  Applying the
coarea proof only to the third family defines restricted codegrees
\(g_{x,y}^{\rm nc}\) at the pair-tensor level.  They need not factor as the
square of one marginal, so (4.4) with the unrestricted
\(g_{x,y}^{(2)}\) is a transparent sufficient upper bound.

The exact new positive gate is therefore

\[
 \boxed{
 \begin{aligned}
 \operatorname {PINC4}:={}&
 \mathbb E\sum_{i<\tau}{1\over X_i}
 \sum_x{1\over c_x}
 \Bigg[
 \sum_{y\ne x}Y_y(g_{x,y}^{(2)})^2\\
 &\hspace{30mm}+
 \sum_{\substack{y,z\ne x\\y\ne z}}
 Y_{y,z}g_{x,y}^{(2)}g_{x,z}^{(2)}
 \Bigg]
 \le C\mathsf A,
 \end{aligned}}
\tag{5.1}
\]

or the same inequality after deleting the already priced conjugate and
named faces.

The factor \(1/X_i\) is the literal accepted-transition probability in
the coarea theorem.  There is **no** additional \(h_i^{-1}\).  The older
unconditioned Young bound would have produced \(1/(h_iX_i)\), but Lemma
2.1 proves that loss spurious.

## 6. Relation to existing ledgers

The current `ROc` and `FE3` statements sum one composite coefficient
\(\mu_A\) against one accepted edge.  The same-anchor term in (4.4)
contains

\[
                         (g_{x,y}^{(2)})^2,
\]

which is two composite coefficients sharing **two** named resources.
The distinct-anchor term contains

\[
                         g_{x,y}^{(2)}g_{x,z}^{(2)}Y_{y,z},
\]

which is two composite coefficients sharing \(x\), followed by a selected
edge carrying \(y,z\).  Neither is a summand of the currently stated
degree-two `ROc` or degree-three `FE3` ledger.

Aggregate bounds

\[
 \sum_yg_{x,y}^{(2)}\le Cd,g_x,
 \qquad
 Y_y=O(1),
 \qquad
 Y_{y,z}=O(1/d)
\tag{6.1}
\]

do not close (5.1): they allow all second-incidence mass to concentrate on
one \(y\).  A genuine spread or fourth-moment estimate for
\(g_{x,y}^{(2)}\) is required.

## 7. Full direct-chi-square consequence

Combine the literal diagonal theorem with (2.5) and Theorem 4.1.  The
full direct `GDIR` row follows if:

1. the conditional mean term \(\sum_i\mathcal M_i/h_i\) is placed in the
   signed incidence-hazard/`HDIR` ledger;
2. the reference term \(\sum_i\mathcal R_i/h_i\) is placed in the
   root-carre ledger;
3. `(PINC4)` holds for the unpriced nonconjugate face; and
4. the diagonal service defect \(\sum_i(D_i)_+\) has its already named
   signed bound.

Under those four rows,

\[
 \mathbb E\sum_{i<\tau}{\mathfrak G_T(i)\over\beta_T(i)X_i}
                         =O(\mathsf A).
\tag{7.1}
\]

## 8. Proof boundary

Conditional centering removes the false product-hazard obstruction and
shows that only simultaneous off-root hits create positive survivor
covariance.  The entire raw fourth-order survivor carré is reduced to the
two explicit positive codegree sums in (4.4), plus the already separated
mean and reference terms.

The remaining nonconjugate theorem is `(PINC4)`.  It is the sharpest
currently visible combinatorial analytic gate: a cumulative
second-incidence spread estimate with the actual one-/two-root loads and
no auxiliary normalization.  Its normalization is \(1/X_i\), matching a
literal first-entry action rather than a service-resolvent occupation.
