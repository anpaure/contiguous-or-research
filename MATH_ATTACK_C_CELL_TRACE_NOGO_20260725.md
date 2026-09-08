# Exact cell trace zero and the corrected local-minimum gate

Date: 2026-07-25

## 1. Statement of the result

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad t=\frac Wn=\operatorname{Cat}_m,
\qquad H=\lceil L\sqrt m\rceil,
\]

where \(L>0\) is fixed.  At depth \(q\), write

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor\lambda_q\rfloor,
\]

and

\[
\beta_q=N_q\theta_q(1-\theta_q),\qquad
B_H=\sum_{q\le H}\frac{\beta_q}{c_q}.
\]

For an exact wreath factor \(F\), let

\[
f_q(F)=\mu_q(F)-\lambda_q\mathbf 1,
\qquad
\mathcal Q_H(F)
=\sum_{q\le H}\frac{\|f_q(F)\|_2^2-\beta_q}{c_q}.
\tag{1.1}
\]

For integer loads this is exactly

\[
\|f_q\|_2^2-\beta_q
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)\ge0.
\tag{1.1a}
\]

The conclusions are as follows.

1.  On every genuine fixed-transposition switching cell \(\mathcal C\),
    if \(\overline{\mathcal Q}_{\mathcal C}\) is the uniform corner mean,
    then at every corner \(F_\sigma\)

    \[
    \boxed{
    A_{\tau,H}(F_\sigma)-V_{\tau,H}(F_\sigma)
    =4\bigl(\mathcal Q_H(F_\sigma)
             -\overline{\mathcal Q}_{\mathcal C}\bigr).}
    \tag{1.2}
    \]

    The same trace-zero identity holds separately at every depth and every
    Johnson degree.  Thus the heat gap is exactly centered cell energy; it
    is not a positive component-curvature quantity.

2.  The slow Johnson degree is \(E_2\) (equivalently the first nontrivial
    zero-margin module; in the zero-margin reindexing it is \(U_1\)).  For
    a uniform unordered transposition,

    \[
    \boxed{
    \mathbb E_\tau\frac{A_{\tau,H}}4
    =\frac2n(B_H+\mathcal Q_H)+\mathsf S_H,}
    \tag{1.3}
    \]

    where

    \[
    \mathsf S_H
    =\sum_{q\le H}\sum_{j\ge3}
      \frac{(j-2)(n-j-1)}{n(n-1)c_q}\,
      \|f_{q,j}\|_2^2\ge0.
    \tag{1.4}
    \]

    The exact slow-mode integer-floor baseline is therefore \(2B_H/n\).

3.  This baseline has the exact Gaussian-window asymptotic

    \[
    \boxed{
    \frac{B_H}{W\sqrt m}\longrightarrow
    \kappa_L:=\int_0^L
    \frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
         {e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0,}
    \tag{1.5}
    \]

    and hence

    \[
    \boxed{
    \frac{2B_H}{n}
    \sim\kappa_L\frac W{\sqrt m}
    =\left(\frac{2\kappa_L}{L}+o(1)\right)Ht.}
    \tag{1.6}
    \]

4.  Let \(F\) be uniform on the finite set of exact factors and let
    \(\tau\) be a uniform unordered transposition.  The fixed-\(\tau\)
    cells partition that set, so

    \[
    \boxed{
    \mathbb E_{F,\tau}(A_{\tau,H}-V_{\tau,H})=0,
    \qquad
    \mathbb E_{F,\tau}\frac{A_{\tau,H}}4
    \ge\frac{2B_H}{n}.}
    \tag{1.7}
    \]

    Consequently, a factorwise relative-gap assertion, with \(a_m\ge0\),

    \[
    \mathbb E_\tau\frac{A_{\tau,H}-V_{\tau,H}}4
    \ge a_m\mathbb E_\tau\frac{A_{\tau,H}}4-r_m
    \tag{1.8}
    \]

    necessarily has

    \[
    \boxed{
    r_m\ge\frac{2a_mB_H}{n}
    =\left(\frac{2\kappa_L}{L}+o(1)\right)a_mHt.}
    \tag{1.9}
    \]

    Thus no such theorem can have \(r_m=o(a_mHt)\).  In particular,
    constant relative contraction cannot have an \(O_L(Ht/n)\) error;
    and if \(a_m=\eta_L/n\), an error \(o(Ht/n)\) is impossible.  More
    precisely, \(r_m=C_LHt/n\) then requires
    \(C_L\ge2\eta_L\kappa_L/L\).  The full slow floor baseline must be
    removed before a relative contraction can even be true.

5.  There is also a single physical exact MSW switching cell with
    multirank component variance

    \[
    \boxed{
    V_{\tau,H}\ge\gamma_LH\operatorname{Cat}_{m-2}
    =\left(\frac{\gamma_L}{16}+o(1)\right)Ht,}
    \tag{1.10}
    \]

    for an explicit \(\gamma_L>0\).  Therefore, if
    \(a_m,b_m\ge0\), \(a_m+b_m\ge\eta_L/n\), no inequality

    \[
    A_{\tau,H}(F)-V_{\tau,H}(F)
    \ge a_mA_{\tau,H}(F)+b_mV_{\tau,H}(F)-r_m
    \tag{1.11}
    \]

    can hold for every exact factor and transposition when
    \(r_m=o(Ht/n)\).  If \(r_m=C_LHt/n\), the necessary constant condition
    is

    \[
    \boxed{C_L\ge\eta_L\gamma_L/16.}
    \tag{1.12}
    \]

    Fixed positive \(a_m+b_m\) are even more strongly impossible with any
    \(O_L(Ht/n)\) remainder.

6.  Identity (1.2) does **not** refute the actual energy-dependent
    fair-heat gate

    \[
    \mathbb E_\tau(A_{\tau,H}-V_{\tau,H})
    \ge \frac{4\eta_L}{n}\mathcal Q_H
       -\frac{4C_L}{n}Ht.
    \tag{1.13}
    \]

    A fixed-\(\tau\) cell average does not control the gaps belonging to
    the other transpositions.  Even the stronger pointwise-in-\(\tau\)
    version

    \[
    A_{\tau,H}-V_{\tau,H}
    \ge \frac{4\eta_L}{n}\mathcal Q_H
       -\frac{4C_L}{n}Ht
    \tag{1.14}
    \]

    is not presently contradicted: averaging (1.14) over one \(\tau\)-cell
    merely forces

    \[
    \overline{\mathcal Q}_{\mathcal C}
    \le\frac{C_L}{\eta_L}Ht.
    \tag{1.15}
    \]

    No exact cell with mean \(\omega(Ht)\) is presently proved.  Thus
    (1.13)--(1.14) are not contradicted; the fixed-cell version already
    contains a low-energy theorem.

The corrected exact target is consequently the direct local-minimum
statement: every component-switch local minimum of \(\mathcal Q_H\) has
\(\mathcal Q_H=O_L(Ht)\).  This avoids attributing a false positive trace
to fair component variance.

## 2. Exact cell-centering identity

Fix a transposition \(\tau\) and one intrinsic interaction cell.  Let
\(K\) range over its ownership components.  Orient the two sides as
\(L_K,R_K\), with \(R_K=\tau L_K\), and put

\[
d_{K,q}=\mu_q(L_K)-\mu_q(R_K).
\tag{2.1}
\]

Write

\[
\|g\|_H^2=\sum_{q\le H}\frac{\|g_q\|_2^2}{c_q}.
\]

Every corner is indexed by signs \(\sigma_K\in\{\pm1\}\).  If \(p\) is
the common midpoint histogram, then

\[
f(F_\sigma)=p+\frac12\sum_K\sigma_Kd_K.
\tag{2.2}
\]

Here \(\tau p=p\) and \(\tau d_K=-d_K\), so the two terms in (2.2) are
orthogonal.  Therefore

\[
\mathcal Q_H(F_\sigma)
=\|p\|_H^2-B_H
+\frac14\left\|\sum_K\sigma_Kd_K\right\|_H^2.
\tag{2.3}
\]

At this corner,

\[
A_{\tau,H}(F_\sigma)
=\left\|\sum_K\sigma_Kd_K\right\|_H^2,
\qquad
V_{\tau,H}=\sum_K\|d_K\|_H^2.
\tag{2.4}
\]

Independent sign averaging kills every cross-component inner product, so

\[
\overline{\mathcal Q}_{\mathcal C}
=\|p\|_H^2-B_H+\frac14V_{\tau,H}.
\tag{2.5}
\]

Subtracting (2.5) from (2.3) proves (1.2).  In particular,

\[
\mathbb E_{\sigma\in\mathcal C}
\bigl(A_{\tau,H}(F_\sigma)-V_{\tau,H}\bigr)=0.
\tag{2.6}
\]

This proof includes the exact integer floor: it cancels because \(B_H\)
is constant throughout the cell.

## 3. Harmonic decomposition and the slow baseline

Each wreath contributes \(n\) rank-\((m-q)\) intervals, and each point
belongs to exactly \(m-q\) of them.  The two sides of a component contain
the same number of wreaths.  Hence every \(d_{K,q}\) has zero total and
zero point margins.  In the Johnson decomposition

\[
\mathbb R^{\binom{[n]}{m-q}}
=E_{q,0}\oplus E_{q,1}\oplus\cdots,
\]

its degrees zero and one vanish.  Also \(\tau d_{K,q}=-d_{K,q}\).
Projection of (2.2)--(2.6) therefore proves the trace-zero identity
separately on every \(E_{q,j}\), \(j\ge2\).

For \(g\in E_{q,j}\), the Johnson Laplacian gives

\[
\mathbb E_\tau\|g-\tau g\|_2^2
=4\kappa_j\|g\|_2^2,
\qquad
\kappa_j=\frac{j(n-j+1)}{n(n-1)}.
\tag{3.1}
\]

Indeed,

\[
\sum_\tau(I-\tau)=L_{J(n,m-q)},
\]

whose eigenvalue on \(E_{q,j}\) is \(j(n-j+1)\); using
\(\|g-\tau g\|^2=2\langle g,(I-\tau)g\rangle\) and dividing by
\(\binom n2\) proves (3.1).

The slow coefficient is

\[
\kappa_2=\frac2n,
\qquad
\kappa_j-\frac2n
=\frac{(j-2)(n-j-1)}{n(n-1)}\quad(j\ge3).
\tag{3.2}
\]

Since \(\|f\|_H^2=B_H+\mathcal Q_H\), summing (3.1)--(3.2) proves
(1.3)--(1.4).  Combining this with one fair component switch gives the
exact floor-corrected recurrence

\[
\boxed{
\mathbb E\mathcal Q_H(F')
=\left(1-\frac2n\right)\mathcal Q_H(F)
+\left[\mathbb E_\tau\frac{V_{\tau,H}}4-\frac{2B_H}{n}\right]
-\mathsf S_H.}
\tag{3.3}
\]

Thus \(2B_H/n\), not zero and not \(B_H\), is the exact slow-mode floor
restitution.

## 4. Proof of the Gaussian floor asymptotic

The exact ratio is

\[
\lambda_q
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\tag{4.1}
\]

Uniformly for \(q\le L\sqrt m\), Taylor expansion gives

\[
\log\lambda_q
=\frac{q(q+1)}m+O_L(m^{-1/2}).
\tag{4.2}
\]

To verify the error, write the \(i\)-th ratio as
\(1+(2+2i)/(m-i)\).  The sum of the linear terms is
\(q(q+1)/m+O(q^3/m^2)\), and the sum of their squares is
\(O(q^3/m^2)\); both errors are \(O_L(m^{-1/2})\).

Put

\[
g(y)=\frac{\{y\}(1-\{y\})}{y\lfloor y\rfloor},\qquad y\ge1.
\tag{4.3}
\]

The numerator tends to zero on both sides of every integer, so \(g\) is
continuous when defined to be zero at integers.  Since

\[
\frac{\beta_q}{c_q}=Wg(\lambda_q),
\tag{4.4}
\]

equation (4.2) and the Riemann-sum theorem give

\[
\frac{B_H}{W\sqrt m}
=\frac1{\sqrt m}\sum_{q\le L\sqrt m}g(\lambda_q)
\longrightarrow\int_0^Lg(e^{x^2})\,dx.
\]

This is (1.5).  The integrand is positive except at the finitely many
points where \(e^{x^2}\) is an integer, so \(\kappa_L>0\).  Finally,
\(n=2m+1\) and

\[
Ht=\left(\frac L2+o(1)\right)\frac W{\sqrt m},
\]

which proves (1.6).

## 5. Uniform-factor trace obstruction

Fix \(\tau\).  Its intrinsic switching cells partition the finite exact-
factor state space, and every cell consists of all of its sign corners.
Equation (2.6), summed over the cells, therefore gives

\[
\mathbb E_F(A_{\tau,H}-V_{\tau,H})=0
\]

for uniform \(F\).  Averaging the last identity over uniform \(\tau\)
proves the first part of (1.7).

On the other hand, (1.3), (1.1a), and \(\mathsf S_H\ge0\) give, for every
individual exact factor,

\[
\mathbb E_\tau\frac{A_{\tau,H}}4
=\frac2n(B_H+\mathcal Q_H)+\mathsf S_H
\ge\frac{2B_H}{n}.
\tag{5.1}
\]

This proves the second part of (1.7).  If (1.8) held for every \(F\),
average it over uniform \(F\).  Its left side becomes zero and (5.1)
gives

\[
0\ge a_m\frac{2B_H}{n}-r_m.
\]

Equation (1.6) now proves (1.9), including its constant.  Notice that this
argument uses a genuine finite-state partition, not a formal random-vector
model.

## 6. A genuine exact cell with mesoscopic component variance

Use the canonical MSW exact factor, indexed by Dyck words of semilength
\(m\), and take \(\tau=(2\ 3)\).  For every Dyck word \(R\) of
semilength \(m-2\), there is a sealed two-wreath component whose old and
new omitted-label orders have the four prefixes

\[
(4,2,3,1),\quad(2,1,4,3),\quad
(4,3,2,1),\quad(3,1,4,2),
\tag{6.0}
\]

followed by one common tail.  The first two are the old side and the last
two are their \(\tau\)-transposes.

For completeness, equality of the two middle-wreath unions follows by
checking the selected prefix positions.  Away from the two exceptional
cuts, the old/new pairs are respectively

\[
\{\{1,2\},\{1,3\}\},\qquad
\{\{1,4\},\{2,3\}\},\qquad
\{\{3,4\},\{2,4\}\},
\]

with the first and third pair merely interchanged.  Across the two
exceptional cuts, the selected prefix singletons are, on both sides, the
multiset \(\{1,2,3,4\}\): in cut order they are

\[
3,4,2,1\quad\text{on the old side},\qquad
2,4,3,1\quad\text{on the new side}.
\]

The common tail is unchanged.  Thus each two-for-two trade is a sealed
interaction block: none of its ownership edges leaves its two old and two
new rows.  It is in fact one component.  If it split, a singleton old/new
pair would have the same full family of middle masks.  Such a family
determines its unoriented odd cyclic order up to the dihedral group.  The
same-row pairing would make that order fixed by \(\tau\), impossible
because no coordinate transposition is a nonidentity odd dihedral
permutation; the two cross pairings are ruled out directly by the four
distinct prefixes in (6.0) and their common ordered tail.  Distinct
\(R\)'s use disjoint old rows and, after applying \(\tau\), disjoint new
rows.

The same four-letter block has an exact action at every lower rank.  Write
the common tail as \(T=(t_0,\ldots,t_{2m-4})\), split it into parity lists

\[
\mathsf E=(t_0,t_2,\ldots,t_{2m-4}),\qquad
\mathsf O=(t_1,t_3,\ldots,t_{2m-5}),
\]

and put

\[
\partial K=e_{K\cup\{3\}}-e_{K\cup\{2\}}.
\]

For a list \(X\), let \(\operatorname{pre}_\ell X\) and
\(\operatorname{suf}_\ell X\) be its first and last \(\ell\) entries.
If \(z_R\) is new side minus old side, then for \(2\le r\le m-1\),
\(\ell=r-1\),

\[
\boxed{
B_rz_R={}
 \partial\operatorname{suf}_\ell\mathsf O
+\partial\operatorname{suf}_\ell\mathsf E
-\partial\operatorname{pre}_\ell\mathsf E
-\partial\operatorname{pre}_\ell\mathsf O.}
\tag{6.1}
\]

Here \(B_r\) sends an omitted-label order to its rank-\(r\) step-two
cyclic-interval histogram.  To prove (6.1), read a step-two window through
the two adjacent exceptional pairs in (6.0).  Since \(r\le m-1\), it cannot
meet both pairs.  A window meeting neither pair cancels among the four
orders, and a window containing both positions of one pair also cancels
because the old and new prefix sets agree as multisets.  Exactly four
windows contain one exceptional position.  Their common tail cores are,
in order,

\[
\operatorname{suf}_\ell\mathsf O,\quad
\operatorname{pre}_\ell\mathsf E,\quad
\operatorname{suf}_\ell\mathsf E,\quad
\operatorname{pre}_\ell\mathsf O,
\]

and their singleton changes have signs \(+,-,+,-\).  This is (6.1).

For \(2\le r\le m-2\), the four cores in (6.1) are distinct: the parity
lists are disjoint, and a proper prefix of a list of distinct entries is
not its suffix.  Hence (6.1) has eight distinct coordinates, all with
coefficient \(\pm1\), and

\[
\boxed{\|B_rz_R\|_2^2=8\qquad(2\le r\le m-2).}
\tag{6.2}
\]

At \(r=m-1\), the two \(\mathsf O\)-terms cancel.  The two
\(\mathsf E\)-terms form one four-coordinate square, so

\[
\boxed{\|B_{m-1}z_R\|_2^2=4.}
\tag{6.3}
\]

Since the sealed block is one actual component, (6.2)--(6.3) show that it
contributes exactly four to \(V_{\tau,1}\), and exactly eight to
\(V_{\tau,q}\) for every \(2\le q\le H\); here \(r=m-q\), and for fixed
\(L\) one has \(2\le r\le m-2\) for all large \(m\).

By (4.2), for all sufficiently large \(m\),

\[
c_q\le M_L:=\lceil e^{L^2+1}\rceil\qquad(q\le H).
\]

Since the \(\operatorname{Cat}_{m-2}\) sealed blocks are disjoint,

\[
\begin{aligned}
V_{\tau,H}
&\ge\operatorname{Cat}_{m-2}
 \left(4+\sum_{q=2}^H\frac8{c_q}\right)\\
&\ge\frac{4}{M_L}H\operatorname{Cat}_{m-2}.
\end{aligned}
\tag{6.4}
\]

Thus (1.10) holds with the explicit choice

\[
\gamma_L=\frac4{\lceil e^{L^2+1}\rceil},
\]

using

\[
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
=\frac{m(m+1)}{4(2m-1)(2m-3)}
\longrightarrow\frac1{16}.
\tag{6.5}
\]

Finally suppose (1.11) held at every corner of this cell.  Cell variance
is invariant and independent-sign averaging gives
\(\mathbb E_\sigma A=V\).  Hence

\[
r_m\ge(a_m+b_m)V.
\tag{6.6}
\]

If \(a_m+b_m\ge\eta_L/n\), (6.4)--(6.5) give

\[
r_m\ge
\left(\frac{\eta_L\gamma_L}{16}+o(1)\right)\frac{Ht}{n}.
\tag{6.7}
\]

This proves the no-go and the necessary constant (1.12).

## 7. What is refuted and what remains open

The theorem refutes every fixed positive multiple of \(A\), of \(V\), or
of a nonnegative combination \(aA+bV\), if the entire correction is only
\(O_L(Ht/n)\).  At the natural coefficient scale \(a_m+b_m=\Omega_L(1/n)\),
it refutes a correction \(o(Ht/n)\); an \(O(Ht/n)\) correction must satisfy
the explicit necessary constant bound (1.12).

More generally, if a cell-invariant proposed baseline \(b_{\mathcal C}\)
is inserted, cell averaging forces

\[
b_{\mathcal C}+\varepsilon_m\ge(a+b)V_{\mathcal C}.
\tag{7.1}
\]

Thus a baseline \(o(Ht)\) cannot repair a fixed-coefficient theorem on the
MSW cell, and a baseline \(o(Ht/n)\) cannot repair a coefficient bounded
below by \(\eta_L/n\).
The true slow integer-floor baseline, however, is of order
\(Ht=\Theta(W/\sqrt m)=\Theta(\sqrt m\,t)\), by (1.6).  The MSW cell above
does not refute a formulation which subtracts that full baseline.

The following two statements are also not refuted.

* The ceiling \(V\le A+C_LHt\) has zero-compatible trace and is not a
  contraction theorem.
* The stronger pointwise energy-dependent inequality (1.14), averaged over
  its fixed \(\tau\)-cell, becomes exactly the low-cell-mean requirement
  (1.15).  The lower bound (1.10) on raw component variance does not
  lower-bound the corrected cell mean, because

  \[
  \overline{\mathcal Q}_{\mathcal C}
  =\|p\|_H^2-B_H+\frac14V_{\mathcal C}
  \]

  and the subtracted floor is \(\Theta(W\sqrt m)\).

The actual fair-heat condition is usually asserted only after averaging
over \(\tau\).  A fixed-\(\tau\) cell average does not preserve the gaps
belonging to the other transpositions, so the trace-zero theorem gives no
contradiction to that weaker quantifier either.

## 8. Corrected local-minimum lemma

For a fixed \(\tau\)-cell, (2.3) gives for any two corners

\[
\mathcal Q_H(F_\sigma)-\mathcal Q_H(F_{\sigma_0})
=\frac14\bigl(A_{\tau,H}(F_\sigma)
              -A_{\tau,H}(F_{\sigma_0})\bigr).
\tag{8.1}
\]

Define

\[
\beta_\tau^{\rm sgn}(F)
=\min_\sigma A_{\tau,H}(F_\sigma).
\]

An exact factor is component-switch local precisely when

\[
\boxed{
A_{\tau,H}(F)=\beta_\tau^{\rm sgn}(F)
\quad\text{for every }\tau.}
\tag{8.2}
\]

At such a factor, cell averaging gives

\[
\boxed{
A_{\tau,H}(F)\le V_{\tau,H}(F),\qquad
V_{\tau,H}(F)-A_{\tau,H}(F)
=4\bigl(\overline{\mathcal Q}_{\mathcal C_\tau(F)}
         -\mathcal Q_H(F)\bigr)\ge0.}
\tag{8.3}
\]

Therefore a positive fair heat gap cannot be the conclusion at a local
minimum.  The exact remaining structural statement is

> **Local-minimum lemma \(\mathrm{LM}_L\).**  Every exact factor satisfying
> (8.2) obeys
> \[
> \mathcal Q_H(F)=O_L(Ht).
> \]

This lemma is sufficient.  The exact-factor state space is finite, so
strict component-switch descent terminates at a factor satisfying (8.2),
or one may simply take a global minimizer.  Since

\[
Ht=\left(\frac L2+o(1)\right)\frac W{\sqrt m}=o(W)
\]

and, pointwise for every integer load \(x\),

\[
(x-c_q)(x-c_q-1)
\ge 2\bigl((c_q-x)_+ +(x-c_q-1)_+\bigr),
\]

the floor excess dominates twice the sum of lower and upper quota
deficits, hence twice the balanced overload.  Therefore
\(\mathrm{LM}_L\) gives \(o(W)\) weighted overload on every fixed
Gaussian window.  The usual fixed-\(L\) diagonalization would then give
MWB.

At a local minimum, any proposed energy-dependent lower bound such as
(1.13) already implies \(\mathrm{LM}_L\), because its left side is
nonpositive by (8.3).  Thus the honest next theorem is the direct
local-minimum bound, or equivalently a positive signed Max-Cut gain away
from the \(O_L(Ht)\) sublevel.  Raw fair component variance has no
universal positive trace to exploit.
