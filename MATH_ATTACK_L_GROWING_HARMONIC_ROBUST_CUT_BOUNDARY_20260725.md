# Lane L: growing harmonics and the exact robust-cut boundary

Date: 2026-07-25

## 1. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  At depth \(q\), write

\[
r_q=m-q,\qquad N_q=\binom n{r_q},
\qquad \lambda_q=\frac W{N_q}=c_q+\theta_q.
\]

Unless a narrower range is displayed, depth identities use
\(1\le q\le m-1\); all window sums use \(1\le q\le H\), which lies in
that range for all sufficiently large \(m\).

We retain the full integer-floor energy

\[
Q_q(F)=\sum_{|S|=r_q}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
=\|f_q\|_2^2-\beta_q,
\tag{1.1}
\]

where

\[
f_q=\mu_q-\lambda_q\mathbf1,
\qquad
\beta_q=N_q\theta_q(1-\theta_q).
\]

The window potential is

\[
\mathcal Q_A(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
\tag{1.2}
\]

This report proves four new statements.

1. **All-\(j\), all-\(q\) exact run-cap envelope.**  Literal cyclic
   chronology gives a two-sided interval for every subset run-loss
   \(L_{X,q}\).  Bhatia--Davis and the exact inclusion singular values then
   give an explicit upper bound for every growing Johnson component
   \(P_{E_j}f_q\).  At \((q,j)=(1,2)\), the exact-factor constant improves
   from \(16+o(1)\) to \(8+o(1)\).

2. **Exact three-witness coupling.**  Every set which fails to fit in a
   cyclic interval of length at most \(m\) has a failing subset of size at
   most three.  Applied layer by layer to the run-loss tails, this gives a
   genuine coupled inequality between every high subset and its triples.

3. **A genuine fixed-transposition robust-cut obstruction.**  For every
   transposition fixed in advance and all large \(m\), there is a literal
   integral exact factor \(G_m\) with no improving component cut for that
   transposition and

   \[
   \mathcal Q_A(G_m)
   \ge \frac{t4^H}{1024M_AH^4},
   \qquad
   M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil .
   \tag{1.3}
   \]

   Even after the audited shallow \(E_2\) sector is deleted, the reduced
   energy is super-floor, every correlated reduced cut gains only the
   deleted-sector error, and, in fact, at least a constant multiple of the
   lower bound in (1.3) lies in degrees \(j>J_m^{\rm cell}\), where
   \(J_m^{\rm cell}=\lfloor H/[8\log(108m)]\rfloor\to\infty\).  Thus no
   robust theorem for a prescribed transposition can work.

4. **A growing-harmonic scalar-chronology no-go.**  On infinitely many
   \(m\), there is an integral nonnegative first-shadow pseudohistogram with
   exact total and point margins, loads only \(0,2\), every displayed
   scalar run-cap, nesting and shadow recurrence, and the support-level
   three-witness inequality, but

   \[
   Q_1=(1-o(1))W,
   \qquad
   \sum_{2\le j\le n/(12\log n)}
   \|P_{E_j}f_1\|_2^2=o(t).
   \tag{1.4}
   \]

   Hence essentially all its energy is in genuinely growing Johnson
   degrees.  This object is not an exact factor; it proves that the entire
   displayed scalar run hierarchy is insufficient without simultaneous
   realization by the same cyclic owner rows.

The requested universal higher-harmonic bound and robust reduced-cut gain
are therefore not proved.  The precise surviving candidate is the following
explicitly **unproved** implication: there should be constants
\(K_A,D_A>0\), with \(D_A>\Gamma_A/A\), such that, for the reduced
potential defined in (6.1),

\[
\boxed{
\mathcal Q_A^{\rm red}(F)>K_AHt
\quad\Longrightarrow\quad
\exists\tau,\varepsilon:\ 
\mathcal Q_A^{\rm red}(F)-
\mathcal Q_A^{\rm red}(F_{\tau,\varepsilon})
>D_AHt/n .}
\tag{1.5}
\]

The exact-factor obstruction below refutes every version with \(\tau\)
fixed before \(F\), but it does not refute this adaptive implication,
\(LM_A\), or constant one.  The scale \(Ht/n\) is a sufficient candidate
forced by the shallow-sector oscillation calculation below; it is not proved
to be unique or forced by all growing Johnson coefficients.

## 2. Exact run-cap harmonic envelope

Let \(F\) be an exact factor.  Fix a nonempty coordinate set
\(X\subset[n]\), put \(|X|=j\le r_q\), and let

\[
g_C(X)=\#\{\text{cyclic middle }m\text{-windows of row }C
\text{ containing }X\}.
\]

The verified run-loss identity is

\[
D_Xf_q=\ell_{q,j}-L_{X,q},
\qquad
L_{X,q}=\sum_{C\in F}\min\{q,g_C(X)\},
\tag{2.1}
\]

where

\[
G_j:=\binom{n-j}{m-j},
\qquad
\ell_{q,j}
=G_j-\lambda_q\binom{n-j}{m-q-j}.
\tag{2.2}
\]

Exact middle ownership and cyclic span give

\[
\sum_{C\in F}g_C(X)=G_j,
\qquad
0\le g_C(X)\le d_j:=m-j+1.
\tag{2.3}
\]

### Theorem 2.1 (exact run-cap interval)

For every exact factor, every \(1\le j\le r_q\), and every \(j\)-set
\(X\),

\[
\boxed{
a_{q,j}:=\frac{\min(q,d_j)}{d_j}G_j
\le L_{X,q}\le
b_{q,j}:=\min\{G_j,qt\}.}
\tag{2.4}
\]

#### Proof

For \(0\le x\le d_j\),

\[
\min(q,x)\ge\frac{\min(q,d_j)}{d_j}x.
\]

Sum this inequality over the rows and use (2.3).  The upper bounds follow
from \(\min(q,g)\le g\) and \(\min(q,g)\le q\). \(\square\)

The number \(\ell_{q,j}\) in (2.2) is the mean of \(L_{X,q}\) over all
\(j\)-sets.  Hence Bhatia--Davis gives

\[
\sum_{|X|=j}(L_{X,q}-\ell_{q,j})^2
\le
\binom nj(\ell_{q,j}-a_{q,j})(b_{q,j}-\ell_{q,j}).
\tag{2.5}
\]

The unnormalized squared singular value of the rank-\(r_q\) to rank-\(j\)
inclusion operator on Johnson degree \(j\) is

\[
\alpha_{q,j}=\binom{n-2j}{r_q-j}.
\tag{2.6}
\]

All lower-degree contributions to \(\|D_jf_q\|_2^2\) are nonnegative.
Equations (2.1), (2.5), and (2.6) therefore prove:

### Corollary 2.2 (all-growing-degree envelope)

\[
\boxed{
\|P_{E_j}f_q\|_2^2
\le
\frac{\binom nj
(\ell_{q,j}-a_{q,j})(b_{q,j}-\ell_{q,j})}
{\binom{n-2j}{m-q-j}}.}
\tag{2.7}
\]

This is an unconditional exact-factor theorem with all constants and all
growing \(q,j\) displayed.  It is not summable at the required scale when
used separately.

### Corollary 2.3 (the revised universal first-shadow constant)

At \(q=1,j=2\),

\[
G_2=\frac{m-1}{2}t,
\qquad d_2=m-1.
\]

Thus every pair belongs to a middle window of at least

\[
\left\lceil\frac{G_2}{d_2}\right\rceil
=\left\lceil\frac t2\right\rceil
\]

factor rows.  If \(h_{ab}\) is the number of rows in which \(a,b\) have
maximal cyclic distance \(m\), then

\[
h_{ab}\le\left\lfloor\frac t2\right\rfloor,
\qquad
\frac1{\binom n2}\sum_{a<b}h_{ab}=\frac tm.
\tag{2.8}
\]

Therefore

\[
\sum_{a<b}\left(h_{ab}-\frac tm\right)^2
\le\frac{n(m-2)}{2m}t^2.
\tag{2.9}
\]

Since the pair-inclusion singular value is

\[
\alpha_{1,2}=\binom{2m-3}{m-3},
\]

we obtain the exact improvement

\[
\boxed{
\|P_{E_2}f_1\|_2^2
\le K_m't,
\qquad
K_m'=
\frac{2(2m+1)(2m-1)}{m(m+1)}<8.}
\tag{2.10}
\]

## 3. Exact three-witness coupling

### Lemma 3.1 (cyclic Helly number three)

Let \(1\le\ell\le m\).  If a coordinate set \(X\) is not contained in
any cyclic \(\ell\)-window of a fixed row, then some subset of \(X\) of
size at most three is not contained in any such window.

#### Proof

Take an inclusion-minimal nonfitting subset \(Y\), with \(|Y|=k\), and
write the cyclic gap lengths between its consecutive points as
\(a_1,\ldots,a_k\).  Deleting point \(i\) must produce a fitting set, so

\[
a_{i-1}+a_i\ge n-\ell+1.
\]

After summing in \(i\),

\[
2n\ge k(n-\ell+1).
\]

Here \(n-\ell+1\ge m+2\), while
\(2n=4m+2<4(m+2)\).  Hence \(k<4\), proving \(k\le3\). \(\square\)

### Theorem 3.2 (run-tail three-witness inequality)

For every exact factor, every \(|X|\ge3\), and every \(q\le m-1\),

\[
\boxed{
qt-L_{X,q}
\le
\sum_{\substack{Y\subseteq X\\|Y|=3}}
(qt-L_{Y,q}).}
\tag{3.1}
\]

#### Proof

For one row,

\[
q-\min(q,g_C(X))
=\sum_{s=1}^q\mathbf1_{\{g_C(X)<s\}}.
\]

The condition \(g_C(X)\ge s\) is equivalent to containment in a cyclic
\((m-s+1)\)-window.  If it fails, Lemma 3.1 gives a nonfitting subset of
size at most three; enlarge it inside \(X\), if necessary, to a triple.
Thus, for every \(s\),

\[
\mathbf1_{\{g_C(X)<s\}}
\le
\sum_{\substack{Y\subseteq X\\|Y|=3}}
\mathbf1_{\{g_C(Y)<s\}}.
\]

Sum first over \(s\), then over all factor rows. \(\square\)

Theorems 2.1 and 3.2 are genuinely coupled exact-factor information, but
they contain no ownership-component Gram correlation.

As an identity of row-run statistics, (3.1) has the stated range
\(q\le m-1\).  It couples the actual depth-\(q\) histogram triple stars
\(D_Yf_q\) only in the range \(r_q\ge3\), equivalently \(q\le m-3\).

## 4. A sharper all-depth pair cap

For a coordinate pair \(e\), put

\[
s_C(e)=m-d_C(e)\in\{0,\ldots,m-1\}.
\]

Exact middle ownership gives

\[
\sum_{C\in F}s_C(e)
=\binom{n-2}{m-2}=\frac{m-1}{2}t.
\tag{4.1}
\]

The weighted near-antipodal statistic is

\[
H_e^{(q)}=\sum_C(q-s_C(e))_+.
\]

The chord inequality

\[
(q-s)_+\le q\left(1-\frac{s}{m-1}\right)
\qquad(0\le s\le m-1)
\]

and (4.1) yield, for every \(1\le q\le m-1\),

\[
\boxed{0\le H_e^{(q)}\le\frac{qt}{2}.}
\tag{4.2}
\]

For \(1\le q\le m-2\), so that \(r_q\ge2\),

\[
\sum_eH_e^{(q)}=\frac{ntq(q+1)}2,
\qquad
\overline H_q=\frac{tq(q+1)}{2m},
\]

the exact pair chronology identity gives

\[
\boxed{
\|P_{E_2}f_q\|_2^2
\le
\frac{nt^2q^2(q+1)}{4\alpha_q}
\left(1-\frac{q+1}{m}\right),
\qquad
\alpha_q=\binom{n-4}{m-q-2}.}
\tag{4.3}
\]

At \(q=1\), (4.3) is exactly (2.10).

For later use, consider a transposition \(\tau=(uv)\) and any exact
factor \(G\).  The \(E_2\) displacement between \(G\) and \(\tau G\) is
supported on the two stars at \(u,v\).  With (4.2), the star calculation
improves to

\[
\boxed{
\|P_{E_2}(f_q(G)-\tau f_q(G))\|_2^2
\le\frac{2q^2(q+1)t^2}{\alpha_q}.}
\tag{4.4}
\]

Every correlated transposition-component child is itself an exact factor,
so (4.4) applies uniformly to every signed residual.

## 5. A genuine exact-factor obstruction to fixed-\(\tau\) robust gain

Fix \(\tau=(2\,3)\), and let \(\mathscr X_m\) be the full intrinsic
\(\tau\)-component cell of the canonical MSW exact factor.  We import the
following audited exact lemma, not a signed relaxation:

### Imported Lemma 5.1 (MSW private pair-sum floor)

Every vertex of \(\mathscr X_m\) is an integral squarefree exact factor;
recomputing its \(\tau\)-overlay gives the same cell.  At every depth
\(1\le q\le m-2\), there are

\[
\operatorname{Cat}_{m-q-2}
\]

distinct moved target pairs \(\{S_V,\tau S_V\}\) such that every cell
vertex satisfies

\[
\mu_q(S_V)+\mu_q(\tau S_V)\ge\operatorname{Cat}_q.
\tag{5.1}
\]

This proved exact lemma is Lemmas 5.1--5.2 of
`MATH_ATTACK_AB7_FACTORIAL_DUPLICATE_MIXING_NO_GO_20260725.md`, based on
the independently audited four-arm formula in
`MATH_ATTACK_AB5_AFR_OVERLAY_FRAGMENTATION_20260725.md`.

We now apply it to the full integer-floor potential (1.2).

### Theorem 5.2 (full-floor same-cell obstruction)

For every fixed \(A>0\), all sufficiently large \(m\), and every
transposition fixed in advance, there is an exact factor \(G_m\) such that

\[
\boxed{
\max_\varepsilon
\bigl[\mathcal Q_A(G_m)-
\mathcal Q_A((G_m)_\varepsilon)\bigr]=0,}
\tag{5.2}
\]

where \(\varepsilon\) ranges over every correlated signing of the genuine
ownership components for that transposition, while

\[
\boxed{
\mathcal Q_A(G_m)
\ge\frac{t4^H}{1024M_AH^4}.}
\tag{5.3}
\]

#### Proof

It is enough to use \(\tau=(2\,3)\); conjugation handles every prescribed
transposition.  The exact Gaussian product gives

\[
c_H\le M_A:=\left\lceil e^{2(A+1)(A+2)}\right\rceil
\tag{5.4}
\]

for all sufficiently large \(m\).

Write \(P_c(x)=(x-c)(x-c-1)\).  If \(x+y=z\), then

\[
P_c(x)+P_c(y)
\ge\frac{z^2}{2}-(2c+1)z.
\tag{5.5}
\]

Since \(\operatorname{Cat}_H\to\infty\), eventually
\(\operatorname{Cat}_H\ge4(2M_A+1)\).  Thus (5.1) and (5.5) show that each
private pair at depth \(H\) contributes at least
\(\operatorname{Cat}_H^2/4\) to \(Q_H\).  All individual floor-polynomial
terms are nonnegative, and the private pairs are distinct.  Hence every
cell vertex \(F\) satisfies

\[
\frac{Q_H(F)}{c_H}
\ge
\frac{\operatorname{Cat}_{m-H-2}\operatorname{Cat}_H^2}{4M_A}.
\tag{5.6}
\]

For \(H\ge3\),

\[
\operatorname{Cat}_H\ge\frac{4^H}{4H^2},
\qquad
\operatorname{Cat}_{m-H-2}>\frac{t}{4^{H+2}}.
\tag{5.7}
\]

Equations (5.6)--(5.7) give (5.3).

Choose \(G_m\) minimizing \(\mathcal Q_A\) on the finite cell.  Component
persistence says that every correlated \(\tau\)-component cut stays inside
the same cell, so none decreases the potential.  The empty cut gives gain
zero.  This proves (5.2). \(\square\)

### Corollary 5.3 (the obstruction reaches growing Johnson degrees)

Let

\[
\Gamma_A=81e^{2(A+3)^2}.
\]

Uniformly for \(q\le H\), \(W/\alpha_q\le\Gamma_A\).  Summing (4.3) gives

\[
\sum_{q\le H}\frac{\|P_{E_2}f_q(G_m)\|_2^2}{c_q}
\le\frac{\Gamma_A}{2}H^4t.
\tag{5.8}
\]

More strongly, put

\[
J_m^{\rm cell}
=\left\lfloor\frac{H}{8\log(108m)}\right\rfloor,
\]

where \(\log\) is natural.  Then \(J_m^{\rm cell}\to\infty\), and every
exact factor \(F\) satisfies, for all sufficiently large \(m\),

\[
\boxed{
\sum_{q\le H}\sum_{2\le j\le J_m^{\rm cell}}
\frac{\|P_{E_j}f_q(F)\|_2^2}{c_q}
\le \frac{tH^3}{n}e^{H/8}.}
\tag{5.9}
\]

Indeed, (2.7) and \(0\le a_{q,j}\le\ell_{q,j}\le b_{q,j}\le qt\)
give

\[
\|P_{E_j}f_q\|_2^2
\le\frac{\binom njq^2t^2}{4\alpha_{q,j}}.
\]

Because \(\lambda_q>1\), its integer floor satisfies
\(c_q\ge\lambda_q/2=W/(2N_q)\).  With \((x)_j\) denoting a falling
factorial,

\[
\frac{N_q}{\alpha_{q,j}}
=\frac{(n)_{2j}}{(r_q)_j(n-r_q)_j}.
\]

For \(q\le H\) and \(j\le J_m^{\rm cell}\), eventually
\(H,J_m^{\rm cell}\le m/4\).  Thus every denominator factor is at least
\(m/2\), every numerator factor is at most \(3m\), and, separately,

\[
\binom nj\le(3m)^j,
\qquad
\frac{N_q}{\alpha_{q,j}}\le36^j.
\]

Consequently

\[
\frac1{c_q}\|P_{E_j}f_q\|_2^2
\le \frac{q^2t}{2n}(108m)^j.
\]

Now \(\sum_{q\le H}q^2\le H^3\),
\(\sum_{j=2}^{J}(108m)^j\le2(108m)^J\), and the definition of
\(J_m^{\rm cell}\) gives \((108m)^{J_m^{\rm cell}}\le e^{H/8}\).
This proves (5.9).

The complete weighted harmonic mass equals

\[
\sum_{q\le H}\sum_{j\ge2}\frac{\|P_{E_j}f_q(G_m)\|_2^2}{c_q}
=\mathcal Q_A(G_m)+\sum_{q\le H}\frac{\beta_q}{c_q}.
\]

Since \(4^H\) dominates \(H^7e^{H/8}/n\), (5.3) and (5.9) imply, for
all sufficiently large \(m\),

\[
\boxed{
\sum_{q\le H}\sum_{j>J_m^{\rm cell}}
\frac{\|P_{E_j}f_q(G_m)\|_2^2}{c_q}
\ge\frac{t4^H}{2048M_AH^4}.}
\tag{5.10}
\]

Thus an exact factor with no improving cut for the prescribed
transposition has \(\omega_A(Ht)\) energy in degrees
\(j>J_m^{\rm cell}\to\infty\).  This is a genuine growing-harmonic
obstruction, not a signed or scalar relaxation.

## 6. Deleting shallow \(E_2\) does not unlock the fixed cell

Put

\[
Q_0=\lfloor m^{1/8}\rfloor,
\qquad
\mathcal S_{Q_0}(F)
=\sum_{q\le Q_0}
\frac{\|P_{E_2}f_q(F)\|_2^2}{c_q},
\]

and retain the full floor baseline in

\[
\mathcal Q_A^{\rm red}(F)=\mathcal Q_A(F)-\mathcal S_{Q_0}(F).
\tag{6.1}
\]

Equation (4.3) gives

\[
\mathcal S_{Q_0}(G_m)
\le\frac{\Gamma_A}{2}Q_0^4t
\le\frac{\Gamma_A}{2A}Ht.
\tag{6.2}
\]

Thus

\[
\boxed{
\mathcal Q_A^{\rm red}(G_m)
\ge
\frac{t4^H}{1024M_AH^4}
-\frac{\Gamma_A}{2A}Ht.}
\tag{6.3}
\]

For a transposition component signing \(\varepsilon\), the exact
contribution of one \(E_2\) sector to the full floor-energy change is

\[
\frac14\bigl(R_{\tau,q,2}(\varepsilon)-A_{\tau,q,2}\bigr).
\]

Both residuals are displacements of complete exact factors, so (4.4)
applies to both.  Consequently

\[
\left|
\mathcal S_{Q_0}(G_m)-
\mathcal S_{Q_0}((G_m)_\varepsilon)
\right|
\le
\frac{\Gamma_AQ_0^4}{n}t
\le\frac{\Gamma_A}{A}\frac{Ht}{n}.
\tag{6.4}
\]

Since \(G_m\) minimizes the full potential on its cell,

\[
\boxed{
\max_\varepsilon
\left[
\mathcal Q_A^{\rm red}(G_m)-
\mathcal Q_A^{\rm red}((G_m)_\varepsilon)
\right]
\le\frac{\Gamma_A}{A}\frac{Ht}{n}.}
\tag{6.5}
\]

The reduced energy divided by \(Ht\) tends to infinity, while every
correlated reduced cut has only floor-per-transposition gain.  Therefore
every prescribed-transposition inequality with any inverse-polynomial
multiplicative capture of \(\mathcal Q_A^{\rm red}\), plus an
\(O_A(Ht/n)\) error, is false.

Precisely, for every fixed \(A,B,C>0\), every prescribed transposition,
and all sufficiently large \(m\), the factor \(G_m\) above satisfies

\[
\max_\varepsilon\bigl[
\mathcal Q_A^{\rm red}(G_m)-
\mathcal Q_A^{\rm red}((G_m)_\varepsilon)
\bigr]
\le\frac{\Gamma_A}{A}\frac{Ht}{n}
<m^{-B}\mathcal Q_A^{\rm red}(G_m)-C\frac{Ht}{n}.
\tag{6.6}
\]

The last strict inequality follows from (6.3), because
\(4^H/(m^BH^5)\to\infty\).  Thus (6.6) gives the exact quantifiers behind
the no-go statement.

The exponent \(1/8\) is the cutoff compatible here with the sufficient
candidate scale \(Ht/n\).  Deleting through
\(m^{3/8}\) gives an all-sign oscillation only of order \(Ht\), which is
an \(n\)-fold larger error than the scale-correct sufficient candidate
used here.

## 7. An integral growing-harmonic scalar no-go

This section proves that the displayed scalar capacities, nesting, shadow
recurrence, and support-witness constraints do not control higher
harmonics.  It deliberately does not claim an exact factor.

### Theorem 7.1 (orbit-regular pseudohistogram)

For every sufficiently large \(m\equiv0\pmod6\), there is a function

\[
\mu:\binom{[n]}{m-1}\longrightarrow\{0,2\}
\]

with exact total and point margins

\[
\sum_S\mu(S)=W,
\qquad
\sum_{S\ni v}\mu(S)=(m-1)t
\quad(v\in[n]),
\tag{7.1}
\]

such that the following hold.  Put \(f=\mu-(m+2)\mathbf1/m\), and, for a
\(j\)-set \(X\), define

\[
\rho_j(X)=G_j-D_X\mu.
\tag{7.2}
\]

The definition (7.2) and capacity (7.3) range over \(1\le j\le r=m-1\).
In (7.4), both nonempty set sizes lie in this range; (7.5) has
\(2\le j\le r\); and (7.6) has \(3\le j\le r\).

Then

\[
\boxed{
\left\lceil\frac{G_j}{m-j+1}\right\rceil
\le\rho_j(X)\le\min\{t,G_j\},}
\tag{7.3}
\]

\[
X\subset Y\quad\Longrightarrow\quad
\rho_{|X|}(X)\ge\rho_{|Y|}(Y),
\tag{7.4}
\]

and, for \(|X|=j-1\),

\[
\boxed{
\sum_{\substack{Y\supset X\\|Y|=j}}
\rho_j(Y)
=G_{j-1}+(m-j)\rho_{j-1}(X).}
\tag{7.5}
\]

\[
t-\rho_j(X)
\le
\sum_{\substack{Y\subseteq X\\|Y|=3}}
(t-\rho_3(Y))
\qquad(j\ge3).
\tag{7.6}
\]

Nevertheless, with

\[
J_m=\left\lfloor\frac{n}{12\log n}\right\rfloor,
\]

where \(\log\) denotes the natural logarithm,

\[
\boxed{
\sum_{j=2}^{J_m}\|P_{E_j}f\|_2^2=o(t),
\qquad
\sum_{j>J_m}\|P_{E_j}f\|_2^2=(1-o(1))W,}
\tag{7.7}
\]

and the exact first-shadow floor energy is

\[
\boxed{Q_1(\mu)=\frac{m-2}{m+2}W.}
\tag{7.8}
\]

#### Proof

Let \(r=m-1\) and let the cyclic group \(\mathbb Z_n\) act on the
\(r\)-sets.  Since \(m\equiv0\pmod3\),

\[
\gcd(n,r)=\gcd(2m+1,m-1)=1.
\]

Thus every cyclic orbit has length \(n\).  Let

\[
M=\frac1n\binom nr=\frac{tm}{m+2}
\]

be the number of orbits.  Since \(m\) is even, \(t\) is even: Legendre's
formula gives \(v_2\binom{2m}{m}=s_2(m)\ge1\), while \(m+1\) is odd.
Choose uniformly

\[
k=\frac t2
\]

of the \(M\) cyclic orbits, let \(\mathcal H\) be their union, and set
\(\mu=2\mathbf1_{\mathcal H}\).  Every full orbit contains each coordinate
exactly \(r\) times.  Hence

\[
|\mathcal H|=nk=\frac W2,
\]

and (7.1) follows.

Fix a coordinate set \(X\), \(|X|=j\), and, for an orbit \(O\), put

\[
w_O(X)=\#\{S\in O:X\subseteq S\}.
\]

Then \(0\le w_O(X)\le n\), and

\[
\sum_Ow_O(X)=B_j:=\binom{n-j}{m-1-j}.
\]

If

\[
Y_X=D_X\mu=2\sum_{O\text{ selected}}w_O(X),
\]

then

\[
\mathbb EY_X
=2\frac{k}{M}B_j
=\frac{m+2}{m}B_j.
\tag{7.9}
\]

The elementary Hoeffding inequality for sampling without replacement from
numbers in \([0,n]\) gives

\[
\Pr(|Y_X-\mathbb EY_X|\ge z)
\le2\exp\left(-\frac{z^2}{2kn^2}\right).
\tag{7.10}
\]

Take

\[
D_m=2n\sqrt{kn}.
\]

The failure probability in (7.10) is then at most \(2e^{-2n}\).  There
are fewer than \(2^n\) nonempty coordinate sets, so a union bound gives a
choice of the \(k\) orbits for which

\[
\boxed{|D_Xf|=|Y_X-\mathbb EY_X|\le D_m}
\quad\text{for every }X.
\tag{7.11}
\]

We show that the same choice satisfies (7.3)--(7.6).  The mean of
\(\rho_j\) is

\[
\overline\rho_j=\frac jmG_j.
\tag{7.12}
\]

For \(2\le j\le m/2-1\), the three relevant slacks from this mean are

\[
\overline\rho_j,\qquad
t-\overline\rho_j,\qquad
\overline\rho_j-\frac{G_j}{m-j+1}.
\tag{7.13}
\]

The normalized support density \(p_j:=\overline\rho_j/t\) is
nonincreasing in \(j\).  Indeed,

\[
\frac{p_{j+1}}{p_j}
=\frac{(j+1)(m-j)}{j(2m+1-j)}\le1.
\]

Since

\[
\frac{\overline\rho_2}{t}=1-\frac1m,
\]

the second slack in (7.13) is at least \(t/m\).  The first is at least
\(G_j/m\), and

\[
\overline\rho_j-\frac{G_j}{m-j+1}
=\frac{G_j(j-1)(m-j)}{m(m-j+1)}
\ge\frac{G_j}{2m}.
\tag{7.14}
\]

At \(j=m/2-1\),

\[
G_j=\binom{3m/2+2}{m/2+1}.
\]

The sequence \(G_j\) is decreasing.  The elementary binomial-mode bound

\[
\binom{3s}{s}\ge\frac{(27/4)^s}{3s+1}
\]

and \(W\le2^n\) show uniformly in the present range that
\(G_j/m\gg D_m\).  Also
\(t\ge2^n/[n(n+1)]\), while \(D_m^2=2n^3t\), so
\(t/m\gg D_m\).  Hence (7.11) lies inside all three slacks in (7.13).
The case \(j=1\) is exact:
\(\rho_1=t\).

For \(j\ge m/2\), (7.3) is deterministic.  Indeed,

\[
Y_X\le2B_j=2G_j\frac{m-j}{m+2},
\]

and, writing \(g=m-j\le m/2\),

\[
G_j-2B_j
\ge\frac{G_j}{g+1}.
\]

Also \(G_j\le t\) for all such \(j\) and all sufficiently large \(m\),
by the same binomial estimate.  This proves (7.3).

For nesting in (7.4), if \(X\subset Y\), it is enough to consider one-step
extensions.  For \(|Y|=j\le m/2\),

\[
\overline\rho_{j-1}-\overline\rho_j
=G_j\frac{m(j-2)+2(j-1)}{m(m-j+1)}
\]

for \(j\ge2\), with the value \(t/m\) at \(j=2\).  This is greater than
\(2D_m\) for all sufficiently large \(m\), so (7.11) proves nesting.
For \(j\ge m/2+1\), the pointwise bound \(0\le\mu\le2\) gives

\[
\rho_{j-1}(X)-\rho_j(Y)
\ge
G_{j-1}-G_j-2(B_{j-1}-B_j)
\ge0.
\]

This proves (7.4).

Identity (7.5) is automatic from the zeta transforms in (7.2): each
\(r\)-set containing a \((j-1)\)-set has exactly \(m-j\) extensions of
size \(j\) inside it, and

\[
(n-j+1)G_j=(m-j+1)G_{j-1}.
\]

For (7.6), put \(p_j=\overline\rho_j/t\).  One has

\[
p_3\longrightarrow\frac34,
\qquad
p_4\longrightarrow\frac12,
\]

and \(p_j\) is nonincreasing.  At \(j=4\),
\(\binom43(1-p_3)-(1-p_4)\to1/2\).  For \(j\ge5\), use
\(1-p_j\le1\) and
\(\binom j3(1-p_3)\ge10(1/4-o(1))\).  Hence, uniformly for
\(j\ge4\),

\[
\binom j3(1-p_3)-(1-p_j)
\ge\frac14
\]

for all large \(m\).  Equation (7.11) perturbs the two sides by at most
\((1+\binom j3)D_m\).  Uniformly for \(j\le m-1\), this is
\(O(n^{9/2}\sqrt t)=o(t)\), because \(D_m^2=2n^3t\) and \(t\) is
exponential in \(n\).  This proves (7.6); the case \(j=3\) is equality.

For every fixed \(X\), (7.3) permits positive integers

\[
1\le g_1(X),\ldots,g_{\rho_j(X)}(X)\le m-j+1,
\qquad
\sum_a g_a(X)=G_j.
\tag{7.15}
\]

Thus every scalar run count can be completed to a feasible all-depth tail
\(L_{X,q}=\sum_a\min(q,g_a(X))\).  Nesting also makes every superlevel
family \(\{X:\rho_j(X)\ge c\}\) an integral downset.  The integers
\(g_a(X)\) in (7.15) are chosen separately for each \(X\): they are not
jointly monotone across \(X\) and are not assigned to common cyclic rows.
What is absent is a single common family of \(t\) cyclic rows realizing all
these data at once.

It remains to prove (7.7)--(7.8).  From (7.11),

\[
\|D_jf\|_2^2\le\binom njD_m^2.
\]

The degree-\(j\) inclusion singular value is

\[
s_{j,j}=\binom{n-2j}{m-1-j},
\]

and

\[
\frac W{s_{j,j}}\le n^{2j}.
\]

Since \(D_m^2=2n^2W\),

\[
\|P_{E_j}f\|_2^2
\le2n^{3j+2}.
\tag{7.16}
\]

For \(j\le J_m\), the sum of (7.16) is at most
\(2n^{3J_m+3}=\exp(n/4+O(\log n))\).  On the other hand, because \(W\) is
the largest binomial coefficient at rank \(m\),

\[
t=\frac Wn\ge\frac{2^n}{n(n+1)}.
\]

This proves the first part of (7.7).

Finally, \(|\mathcal H|=W/2\), so exactly \(N_1-W/2\) targets have load
zero and all others have load two.  Since \(c_1=1\),

\[
Q_1=2\left(N_1-\frac W2\right)
=\frac{m-2}{m+2}W.
\]

The exact total and point margins kill \(E_0,E_1\); the low-degree mass is
\(o(t)\), and \(\beta_1<4t\).  The remaining assertions follow. \(\square\)

## 8. Exact proved/conditional boundary

The unconditional advances are:

1. the run-cap envelope (2.7) in every growing degree and depth;
2. the three-witness coupling (3.1);
3. the improved exact-factor \(E_2\) constant \(K_m'<8\);
4. the genuine fixed-transposition full-floor obstruction, including
   energy above \(J_m^{\rm cell}\to\infty\), in (5.2)--(5.10);
5. the quantified reduced-cell obstruction (6.3)--(6.6); and
6. the scalar-chronology no-go (7.3)--(7.8).

What remains unproved is an **adaptive transposition-selection theorem**.
The sufficient candidate scale supplied by the proved shallow oscillation
bound is:

> If \(\mathcal Q_A^{\rm red}(F)>K_AHt\), find a transposition \(\tau\)
> and a genuine common component signing for its freshly recomputed overlay
> with reduced gain greater than \(D_AHt/n\), where
> \(D_A>\Gamma_A/A\).

The proved all-sign estimate permits deletion through \(q\le m^{1/8}\)
at the \(Ht/n\) oscillation scale; the same estimate through
\(m^{3/8}\) is only of order \(Ht\).  A theorem of the displayed form
would, by (6.4), give a positive full-energy cut whenever its high-energy
premise holds and hence prove \(LM_A\).  The exact MSW construction proves
that \(\tau\) must be allowed to depend on \(F\); it cannot be prescribed
in advance.

The scalar obstruction proves that the displayed subset capacities,
nesting, exact shadow recurrence, support-level three-witness inequality,
the induced downset shadow consequences, and growing low-harmonic estimates
still miss one datum: the same \(t\) cyclic owner rows must realize all
subset run tails and the middle-root partition simultaneously.  That
common-owner geometry, together with adaptive transposition choice, is the
precise conditional boundary.  No constant-one conclusion is claimed.
