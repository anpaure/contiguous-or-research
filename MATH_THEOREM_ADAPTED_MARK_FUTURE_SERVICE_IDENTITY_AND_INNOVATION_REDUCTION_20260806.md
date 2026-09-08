# Adapted-mark future-service identity and innovation reduction

**Date:** 2026-08-06  
**Method:** exact one-transition expansion and incidence Cauchy estimates;
no computation or search  
**Status:** proof-safe identity and partial injection.  Future service also
works for the actual moving score, but it creates one linear mean-drift
term and one quadratic innovation term.  The quadratic term reduces, with
the small potential-cap coefficient, to a small multiple of the existing
normalized-gradient and root-carre rows.  The linear term reduces to the
one-root hazard-error row.  Since the dynamic transfer of those rows is
still the stated GDIR/HDIR gate, this note does not claim an unconditional
closure by the static ROc/FE3 estimates alone.

## 1. Exact adapted-mark identity

Fix one resource type and write

\[
 g_i=Kf_i
\]

on the current candidate fibre.  For transition \(G\), let
\(\delta_i^G\) be the hypothetical resource-vector increment, before
deleting candidate rows, and put

\[
 r_i^G=K\delta_i^G.
\tag{1.1}
\]

For a current row \(a\), write

\[
 \widehat c_i(a)=c_i(a)R_i(a),
 \qquad
 s_a(G)={\bf1}_{\{G\cap U_a=\varnothing\}}.
\tag{1.2}
\]

The density multiplier \(R_i(a)\) is fixed before \(G\) is sampled.  Define

\[
 \Phi_i=\sum_{a\in A_i}c_i(a)g_i(a)^2.
\tag{1.3}
\]

### Theorem 1.1 (exact one-step expansion)

One has

\[
 \boxed{
 \begin{aligned}
 \mathbb E_i(\Phi_{i+1}-\Phi_i)
 ={}&-(1-\rho_i^2)\Phi_i\\
 &+\sum_a c_i(a)R_i(a)
      (q_i(a)-\kappa_i(a))g_i(a)^2\\
 &+\mathcal I_i^{\rm lin}
  +\mathcal I_i^{\rm quad},
 \end{aligned}}
\tag{1.4}
\]

where

\[
 \mathcal I_i^{\rm lin}
 ={2\over X(i)}\sum_Ga_G(i)
   \sum_a\widehat c_i(a)s_a(G)g_i(a)r_i^G(a),
\tag{1.5}
\]

and

\[
 \mathcal I_i^{\rm quad}
 ={1\over X(i)}\sum_Ga_G(i)
   \sum_a\widehat c_i(a)s_a(G)r_i^G(a)^2.
\tag{1.6}
\]

#### Proof

For a surviving row,

\[
 \widehat c_i(a)\bigl(g_i(a)+r_i^G(a)\bigr)^2
 -c_i(a)g_i(a)^2
\]

is its exact potential increment; a killed row contributes only the
negative old term.  Expand the square and average over \(G\).  The old-mark
coefficient is

\[
 R_i(a)(1-\kappa_i(a))-1
 =-(1-\rho_i^2)+R_i(a)(q_i(a)-\kappa_i(a)),
\]

by the exact future-fugacity identity.  The other two terms are
(1.5)--(1.6).  \(\square\)

This is the precise adapted replacement for Remark 1.2 in the affine
Hardy note.

## 2. Full-hypothetical minus killed-correlation form

Let

\[
 \widehat M_i=\operatorname {diag}(\widehat c_i(a)),
 \qquad
 \widehat B_i=K^*\widehat M_iK,
 \qquad
 \overline\delta_i={1\over X(i)}\sum_Ga_G(i)\delta_i^G.
\tag{2.1}
\]

Define

\[
 \begin{aligned}
 \mathcal K_i^{(1)}
 &={2\over X(i)}\sum_Ga_G(i)
   \sum_{a:s_a(G)=0}\widehat c_i(a)g_i(a)r_i^G(a),\\
 \mathcal K_i^{(2)}
 &={1\over X(i)}\sum_Ga_G(i)
   \sum_{a:s_a(G)=0}\widehat c_i(a)r_i^G(a)^2,
 \end{aligned}
\tag{2.2}
\]

and the full hypothetical quadratic innovation

\[
 \mathcal Q_i
 ={1\over X(i)}\sum_Ga_G(i)
       \langle\delta_i^G,\widehat B_i\delta_i^G\rangle.
\tag{2.3}
\]

Then

\[
 \boxed{
 \mathcal I_i^{\rm lin}+\mathcal I_i^{\rm quad}
 =2\langle f_i,\widehat B_i\overline\delta_i\rangle
   +\mathcal Q_i-\mathcal K_i^{(1)}-\mathcal K_i^{(2)}.}
\tag{2.4}
\]

In particular, \(\mathcal K_i^{(2)}\ge0\) is favorable.  The term
\(\mathcal K_i^{(1)}\) is an exact first-kill correlation: its row, the
selected edge \(G\), and the root-load innovation \(\delta_i^G\) share the
same killing transition.  It must be kept in the first-entry ledger rather
than replaced by an independent product.

## 3. Quadratic innovation has no new \(d^2\) loss

Assume every candidate row contains at most \(C_0d\) occurrences of this
resource type.  Put

\[
 \gamma_x=\sum_{a:x\in U_a}\widehat c_i(a),
 \qquad
 \gamma_x=\beta_T^{\rm inn}Y_x+\zeta_x,
 \qquad
 \mathfrak G_i=\sum_x{\zeta_x^2\over Y_x}.
\tag{3.1}
\]

Let

\[
 \mathcal V_i^{\rm root}
 ={1\over X(i)}\sum_Ga_G(i)\sum_xY_x(\delta_{i,x}^G)^2.
\tag{3.2}
\]

### Lemma 3.0 (the innovation family is the GDIR family)

For the generic pair-potential rows,

\[
 \boxed{
 \gamma_x=g_x^\circ,\qquad
 \beta_T^{\rm inn}=\beta_T,\qquad
 \mathfrak G_i=\mathfrak G_T(i),}
\tag{3.2a}
\]

with the notation (4.4)--(4.5) of the joint-Lyapunov note.
Furthermore, \(\mathcal V_i^{\rm root}\) is exactly the conditional
root-load carre-du-champ summed with the \(Y_x\) weights.

#### Proof

Both \(\gamma_x\) and \(g_x^\circ\) sum the same hypothetical next
coefficient

\[
 c_i(Q,E,F)R_i(E,F;Q)
\]

over the same occurrence-labelled condition
\(x\in U_A^\circ=(E\cup F)-Q\).  Their best \(Y\)-proportional
coefficient and centered square are therefore identical.  Equation (3.2)
is the definition of the conditional root-load square injection after
interchanging the \(G\)- and \(x\)-sums.  \(\square\)

For root- and marked-cluster rows, the same conclusion holds after
retaining their distinguished-root omissions.  That is a finite
occurrence convention, not a new analytic estimate.

On the good-load interval, suppose

\[
 c_0\le Y_x\le C_0,
 \qquad |\delta_{i,x}^G|\le C_1.
\tag{3.3}
\]

### Proposition 3.1 (incidence reduction)

\[
 \boxed{
 \mathcal Q_i
 \le C\left(
       d^2\mathfrak G_i+
       (1+d\beta_T^{\rm inn})\mathcal V_i^{\rm root}
       \right).}
\tag{3.4}
\]

#### Proof

For one row,

\[
 (K\delta_i^G(a))^2
 \le C_0d\sum_{x\in U_a}(\delta_{i,x}^G)^2.
\]

Sum with coefficient \(\widehat c_i(a)\), interchange the two sums, and
average over \(G\).  This gives

\[
 \mathcal Q_i
 \le C d\,{1\over X(i)}\sum_Ga_G(i)
       \sum_x(\beta_iY_x+\zeta_x)(\delta_{i,x}^G)^2.
\tag{3.5}
\]

The \(\beta_T^{\rm inn}Y_x\) part is
\(Cd\beta_T^{\rm inn}\mathcal V_i^{\rm root}\).
For the centered part use, pointwise in \(x\),

\[
 |\zeta_x|\,\mathbb E_i(\delta_{i,x}^G)^2
 \le {d\over2}{\zeta_x^2\over Y_x}
   +{1\over2d}Y_x
       \bigl(\mathbb E_i(\delta_{i,x}^G)^2\bigr)^2.
\tag{3.6}
\]

By (3.3), the last square is at most a fixed constant times the second
moment itself.  Insert (3.6) in (3.5), proving (3.4).  \(\square\)

Under the small cap of the affine Hardy note,

\[
 \beta_T^{\rm inn}\le {C\varepsilon_P\over d^2}.
\]

The occupation argument multiplies innovation by
\(C\varepsilon_P/d^2\).  Hence (3.4) gives

\[
 \boxed{
 {C\varepsilon_P\over d^2}\mathcal Q_i
 \le C\varepsilon_P\mathfrak G_i
   +{C\varepsilon_P\over d^2}
       \mathcal V_i^{\rm root}.}
\tag{3.7}
\]

Thus the quadratic moving-mark term is absorbed by a sufficiently small
multiple of the normalized-gradient row plus the already required
root-carre injection.  There is no residual position factor.
Thus the GDIR/root-carre identification is literal on the generic pair
family, by Lemma 3.0.  The marked/root versions use their already separated
finite occurrence conventions.

## 4. The linear term is the one-root hazard-error row

The first term on the right of (2.4) is

\[
 2\langle Kf_i,\widehat M_iK\overline\delta_i\rangle.
\tag{4.1}
\]

For compensated root loads, the exact one-root analogue of (KH4) writes

\[
 \overline\delta_i=-h_i f_i+\varepsilon_i
\tag{4.2}
\]

after centering and adding the separately recorded owner-mixture term.
Here \(h_i=1-\rho_i+O((1-\rho_i)^2)\), while
\(\varepsilon_i\) is the signed one-root hazard defect: its coordinates are
weighted sums of

\[
 q_i(E)-{\Lambda_i(E)\over X(i)}.
\tag{4.3}
\]

Substitution gives the exact division

\[
 2\langle f_i,\widehat B_i\overline\delta_i\rangle
 =-2h_i\langle f_i,\widehat B_if_i\rangle
   +2\langle f_i,\widehat B_i\varepsilon_i\rangle.
\tag{4.4}
\]

The first term is favorable.  The second is not a new stochastic object:
after expanding \(\widehat B_i=K^*\widehat M_iK\), it is the bilinear
pair-future-weight times one-root hazard-error form whose square is HDIR.

There is also an exact scale split for the killed correlation.  Put

\[
 \mathcal D_i^{\rm kill}
 ={1\over X(i)}\sum_Ga_G(i)
   \sum_{a:s_a(G)=0}\widehat c_i(a)g_i(a)^2,
 \qquad
 \mathcal Q_i^{\rm kill}\le\mathcal Q_i
\tag{4.5}
\]

for the corresponding killed quadratic innovation.  Ordinary Young's
inequality gives

\[
 -\mathcal K_i^{(1)}
 \le \mathcal D_i^{\rm kill}
       +\mathcal Q_i^{\rm kill}.
\tag{4.6}
\]

On the good-load/total-rate interval, a row with \(O(d)\) resources has
kill probability at most \(Cd(1-\rho_i)\).  Hence the first term in
(4.6) is at most \(Cd\) times the service mass, plus the same hazard
defect as in (2.2).  This looks too large before the Hardy coefficient is
inserted, but the entire adapted-mark error is multiplied by
\(C\varepsilon_P/d^2\).  Its contribution is therefore only
\(C\varepsilon_P/d\) times the service mass and is absorbed.  The second
term is bounded by \(\mathcal Q_i\); after the same multiplier, Proposition
3.1 gives exactly the small GDIR/root-carre bound (3.7).  No separate
four-edge or FE3 assertion is needed for \(\mathcal K_i^{(1)}\).

The proof-safe implication is therefore conditional:

\[
 \boxed{
 \text{GDIR + HDIR + the root-carre injection}
 \Longrightarrow
 \text{the adapted affine mark innovation is absorbed}.}
\tag{4.7}
\]

Indeed, use Cauchy--Young on the last term of (4.4), with a small fraction
of the favorable first term, and use (3.7) for the quadratic term.
The killed correlation is assigned at its unique first kill; its one-entry
and two-entry expansions must implement (4.6).

This does **not** prove (4.7) solely from the already static ROc/FE3 bounds.
The dynamic transfer from those static injections to GDIR/HDIR is exactly
the remaining local analytic theorem in the parent notes.  Claiming a
direct static injection would hide the same adapted-vector issue that
invalidated the earlier scalar-resolvent argument.

## 5. Consequence for the programme

The affine position obstruction itself is no longer a source of a
\(d^2\) loss:

* future service pays its occupied covariance mass;
* a small potential cap makes the feedback into the hazard gradient
  absorbable;
* the moving-mark quadratic term is only a small GDIR/root-carre term; and
* the moving-mark linear term is precisely the existing one-root
  hazard-error transfer.

What remains is not a one-dimensional path inequality.  It is the already
named dynamic GDIR/HDIR transfer (plus closure of the scalar potential
cap).  Static ROc/FE3 alone do not establish it.
