# Mathematical attack I: nonlocal exact-factor circuits

## Verdict

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor,
\]

and fix \(H=H_A=\lceil A\sqrt m\rceil\), where \(A>0\) is fixed.
Every move below has exact factors at all of its vertices.  There is no
fractional factor, no independently chosen factor at each depth, and no
unextendible almost-matching.

This route does **not** prove the contiguous-OR width conjecture.  It gives
the following unconditional advances.

1. Every finite coordinate group has an exact group-component product of
   factor moves.  Its multidepth energy has an exact group-Haar
   vector-discrepancy identity.
2. Every support-feasible static two-transposition rectangle is already a
   partial-support one-transposition trade.  Whenever it is applicable
   inside the exact-factor fibre, it decomposes into ordinary
   one-transposition ownership components.  A rectangle based on a whole
   factor is never support-feasible.
3. A multistep circuit has no higher-order energy term: its change is the
   quadratic energy of its net endpoint effect.  Closed circuits and global
   coordinate commutators have zero descent.
4. Fixing shallow shadows is a hard integral constraint on one common set
   of component choices.  The known bounded selector and MSW move systems
   have no such nonzero shallow kernel.
5. The exact one-transposition spectral baseline is \(4(n-1)B_H\), not
   \(2nB_H\).  The earlier \(2nB_H\) gate is impossible on every fixed
   Gaussian window.

The smallest quantitative missing statement is the correlated Haar frame
\((\mathrm{CHF}_A)\) in Section 9.  It is explicitly marked **UNPROVED**.
It would give fixed-window weighted overload \(o(W)\) and therefore the
final OR bound after diagonalization.

No finite or computational search is used here.

---

## 1. Floor-subtracted energy and overload

For a wreath family \(U\), let \(\mathcal A_r\mathbf1_U(S)\) count its
cyclic orders having \(S\) as a cyclic \(r\)-interval.  For an exact middle
factor \(F\), define

\[
\mu_q=\mathcal A_{m-q}\mathbf1_F,\qquad
\lambda_q=\frac{W}{N_q},\qquad
f_q=\mu_q-\lambda_q\mathbf1.
\]

Write

\[
W=c_qN_q+r_q,\qquad 0\le r_q<N_q,\qquad
\beta_q=\frac{r_q(N_q-r_q)}{N_q}.
\]

The minimum of \(\|x-\lambda_q\mathbf1\|_2^2\) over integral vectors of
total \(W\) is \(\beta_q\).  Put

\[
\begin{aligned}
E_H(F)&=\sum_{q=1}^H
 \frac{\|f_q\|_2^2-\beta_q}{c_q},\\
\Psi_H(F)&=\frac12E_H(F),\\
B_H&=\sum_{q=1}^H\frac{\beta_q}{c_q},\\
\langle u,v\rangle_H&=
 \sum_{q=1}^H\frac{\langle u_q,v_q\rangle_2}{c_q}.
\end{aligned}
\tag{1.1}
\]

Thus

\[
\Psi_H(F)=\frac12\|f(F)\|_H^2-\frac12B_H,\qquad
\|f(F)\|_H^2=B_H+2\Psi_H(F).
\tag{1.2}
\]

The convention matters: \(E_H\) is the corrected heat-audit convention,
whereas \(\Psi_H\) is the half-energy in which the curvature of a move
\(\delta\) is \(\|\delta\|_H^2/2\).

### Lemma 1.1 (exact overload ledger)

Let \(\mu\in\mathbb Z_{\ge0}^N\) have total \(W=cN+r\).  Let \(O(\mu)\)
be its least overload above a quota vector having \(r\) entries \(c+1\)
and \(N-r\) entries \(c\).  Define

\[
D^-=\sum_i(c-\mu_i)_+,\qquad
D^+=\sum_i(\mu_i-c-1)_+.
\]

Then

\[
O(\mu)=\max(D^-,D^+)
\tag{1.3}
\]

and

\[
\left\|\mu-\left(c+\frac rN\right)\mathbf1\right\|_2^2
-\frac{r(N-r)}N
\ge2(D^-+D^+)\ge2O(\mu).
\tag{1.4}
\]

#### Proof

Set \(y_i=\mu_i-c\), so \(\sum_i y_i=r\).  If
\(p=\#\{i:y_i\ge1\}\), then

\[
r=p+D^+-D^-.
\tag{1.5}
\]

If \(p\ge r\), assign the \(r\) high quotas to positive coordinates.
The overload is \(D^++p-r=D^-\), which is also forced by the total
deficit below \(c\).  If \(p\le r\), assign a high quota to every positive
coordinate and then to \(r-p\) other coordinates.  The overload is
\(D^+\), which is forced by entries above \(c+1\).  This proves (1.3).

Moreover,

\[
\left\|\mu-\left(c+\frac rN\right)\mathbf1\right\|_2^2
-\frac{r(N-r)}N
=\sum_i y_i(y_i-1).
\]

For integral \(y\),

\[
y(y-1)\ge
\begin{cases}
2(-y),&y\le-1,\\
0,&y=0,1,\\
2(y-1),&y\ge2.
\end{cases}
\]

Summation gives (1.4). \(\square\)

Therefore, if

\[
P_H(F)=\sum_{q=1}^H\frac{O_q(F)}{c_q},
\]

then

\[
\boxed{P_H(F)\le\frac12E_H(F)=\Psi_H(F).}
\tag{1.6}
\]

This is an unlabelled histogram statement.  It does not produce a common
balanced nested owner flow, so it proves the fixed-window MWB lane, not the
stronger labelled statement \((\mathrm{CA}_A)\).

---

## 2. The corrected \(4(n-1)\) baseline

The point margins of every centered exact-wreath histogram vanish.  If
\(r=m-q\) and \(x\in[n]\), every cyclic order has exactly \(r\) cyclic
\(r\)-intervals containing \(x\).  Since \(|F|=W/n\),

\[
\sum_{S\ni x}\mu_q(S)=\frac{rW}{n}.
\]

Also

\[
\lambda_q\binom{n-1}{r-1}
=\frac{W}{\binom nr}\binom{n-1}{r-1}
=\frac{rW}{n}.
\]

Hence \(f_q\) has neither Johnson degree \(0\) nor degree \(1\).
For all unordered coordinate transpositions \(\tau\), the Johnson identity
is

\[
\sum_\tau\|g-\tau g\|_2^2
=2\sum_j j(n-j+1)\|g^{(j)}\|_2^2.
\tag{2.1}
\]

Applying this to \(f_q\), whose nonzero degrees have \(j\ge2\), gives

\[
\boxed{\sum_\tau\|f_q-\tau f_q\|_2^2
\ge4(n-1)\|f_q\|_2^2.}
\tag{2.2}
\]

The coefficient \(4(n-1)\) is sharp on the ambient degree-two subspace.

Fix \(\tau\).  Overlay \(F\) and \(\tau F\) by joining the two owners of
each middle mask.  For every ownership component \(K\), let \(d_K\) be
the simultaneous depth-\(1,\ldots,H\) histogram difference between its
two sides, and put

\[
A_{\tau,H}=\left\|\sum_Kd_K\right\|_H^2,\qquad
N_{\tau,H}=\sum_K\|d_K\|_H^2.
\tag{2.3}
\]

Independent fair side choices give

\[
\mathbb E[\Psi_H(F')-\Psi_H(F)]
=\frac18(N_{\tau,H}-A_{\tau,H}).
\tag{2.4}
\]

If \(F_*\) globally minimizes this same \(H\)-window energy, every child is
exact, so

\[
A_{\tau,H}\le N_{\tau,H}.
\tag{2.5}
\]

Let

\[
D_H=\sum_\tau A_{\tau,H},\qquad
R_H=\sum_\tau N_{\tau,H}.
\]

Equations (1.2), (2.2), and (2.5) give

\[
\boxed{R_H\ge D_H
\ge4(n-1)\bigl(B_H+2\Psi_H(F_*)\bigr).}
\tag{2.6}
\]

Combining this with (1.6) yields the exact gate

\[
\boxed{P_H(F_*)\le\Psi_H(F_*)
\le\frac{R_H-4(n-1)B_H}{8(n-1)}.}
\tag{2.7}
\]

The floor baseline is not negligible.  Uniformly for \(q\le A\sqrt m\),

\[
\lambda_q
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}
=\exp\left(\frac{q^2}{m}+O_A(m^{-1/2})\right).
\tag{2.8}
\]

If \(\theta_q=\{\lambda_q\}\), then

\[
\frac{\beta_q}{c_qW}
=\frac{\theta_q(1-\theta_q)}
{\lambda_q\lfloor\lambda_q\rfloor}.
\]

A Riemann sum gives

\[
\boxed{\frac{B_H}{W\sqrt m}\longrightarrow
\kappa_A:=
\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.}
\tag{2.9}
\]

There are only finitely many staircase discontinuities on a fixed
interval, and the integrand is positive off a finite set, proving the
claimed convergence and positivity.

Thus the earlier proposed upper bound

\[
R_H\le2nB_H+o(nW)
\]

is impossible: together with (2.6) it would imply

\[
(2n-4)B_H+8(n-1)\Psi_H=o(nW),
\]

while the first term is \(\Theta_A(nW\sqrt m)\).  The viable target is

\[
\boxed{R_H\le4(n-1)B_H+o(nW),}
\tag{2.10}
\]

which implies \(\Psi_H=o(W)\) and \(P_H=o(W)\).  All later noise estimates
are stated in the floor-subtracted energy \(\Psi_H\); raw contraction of
\(\|f\|_H^2\) would incorrectly try to erase \(B_H\).

---

## 3. Exact moves from a finite coordinate group

Let \(\Gamma\le S_n\) be finite.  For an exact factor \(F\), form an
undirected graph \(\mathcal G_\Gamma(F)\) on the wreaths of \(F\): join the
owner of a middle mask \(M\) to the owner of \(gM\) for every
\(g\in\Gamma\).  Loops are harmless.  If \(K\) is a connected component,
put

\[
\mathcal M(K)=\bigcup_{C\in K}\mathcal W_m(C).
\]

### Theorem 3.1 (exact group-component product)

For every component \(K\):

1. \(\mathcal M(K)\) is \(\Gamma\)-invariant;
2. for every \(h\in\Gamma\), \(hK\) is a partial factor covering
   \(\mathcal M(K)\) once;
3. independently choosing \(h_K\in\Gamma\) for every component gives

   \[
   F_{\mathbf h}=\bigcup_Kh_KK,
   \tag{3.1}
   \]

   which is an exact middle factor.

#### Proof

If \(M\in\mathcal M(K)\), its unique owner \(C\in F\) lies in \(K\).
The owner of \(gM\) is adjacent to \(C\), so it also lies in \(K\).
Thus \(\mathcal M(K)\) is \(\Gamma\)-invariant.

The middle masks of \(hK\) are
\(h\mathcal M(K)=\mathcal M(K)\), each once.  Different components have
disjoint middle supports, so (3.1) covers every middle mask once.  Two
chosen translates from distinct components cannot be the same wreath:
that wreath would carry a middle mask in two disjoint component supports.
Hence (3.1) is an exact factor. \(\square\)

If \(\Gamma_1\le\Gamma_2\), every \(\Gamma_2\)-component is a union of
\(\Gamma_1\)-components.  Adding generators therefore increases coherent
mixing but can only reduce integral choice freedom.  If \(\Gamma\) is
transitive on middle masks, the graph is connected: for wreaths \(C,D\),
choose \(M\in C\), \(M'\in D\), and \(gM=M'\).  Then \(C,D\) are adjacent.
Such a group gives only global relabelings \(hF\), all energy-isometric.

This is the exact mixing-versus-fragmentation obstruction.

---

## 4. Exact group-Haar energy

For a component \(K\), let

\[
a_K=(\mathcal A_{m-q}\mathbf1_K)_{q\le H}
\]

be its multidepth load.  Let

\[
P_\Gamma=\frac1{|\Gamma|}\sum_{g\in\Gamma}g
\]

be the orthogonal projection onto the \(\Gamma\)-invariant subspace, and
define

\[
A_\Gamma(F)=\|(I-P_\Gamma)f(F)\|_H^2.
\]

### Theorem 4.1 (group-Haar identity)

For every group-component choice \(\mathbf h=(h_K)_K\),

\[
f(F_{\mathbf h})
=P_\Gamma f(F)+
\sum_K(h_Ka_K-P_\Gamma a_K),
\tag{4.1}
\]

and the two terms on the right are orthogonal.  Consequently

\[
\boxed{
\Psi_H(F_{\mathbf h})+\frac12B_H
=\frac12\|P_\Gamma f(F)\|_H^2
+\frac12\left\|
\sum_K(h_Ka_K-P_\Gamma a_K)
\right\|_H^2.}
\tag{4.2}
\]

Put

\[
R_\Gamma(F)=
\min_{(h_K)\in\Gamma^{\mathcal K}}
\left\|\sum_K(h_Ka_K-P_\Gamma a_K)\right\|_H^2.
\tag{4.3}
\]

Then

\[
\boxed{\Psi_H(F)-\min_{\mathbf h}\Psi_H(F_{\mathbf h})
=\frac12\bigl(A_\Gamma(F)-R_\Gamma(F)\bigr).}
\tag{4.4}
\]

#### Proof

Since \(f(F)=\sum_Ka_K-\lambda\mathbf1\) and the constant vector is
\(\Gamma\)-invariant,

\[
P_\Gamma f=\sum_KP_\Gamma a_K-\lambda\mathbf1.
\]

Subtract this from
\(f(F_{\mathbf h})=\sum_Kh_Ka_K-\lambda\mathbf1\) to get (4.1).
Every residual is in \(\ker P_\Gamma\), while \(P_\Gamma f\) is invariant.
This gives (4.2).  The identity choice has residual sum
\((I-P_\Gamma)f\), whose squared norm is \(A_\Gamma\); minimizing (4.2)
proves (4.4). \(\square\)

At a global minimizer of the same window,

\[
\boxed{R_\Gamma(F_*)=A_\Gamma(F_*)}
\tag{4.5}
\]

for every \(\Gamma\), because \(R_\Gamma\le A_\Gamma\) and every choice in
Theorem 3.1 is exact.

If the \(h_K\)'s are uniform and independent, define

\[
V_\Gamma=
\sum_K\frac1{|\Gamma|}\sum_{g\in\Gamma}
\|ga_K-P_\Gamma a_K\|_H^2.
\]

The residuals are independent and mean zero, hence

\[
\boxed{\mathbb E[\Psi_H(F_{\mathbf h})-\Psi_H(F)]
=\frac12(V_\Gamma-A_\Gamma).}
\tag{4.6}
\]

For \(\Gamma=\{1,\tau\}\), both \(A_\Gamma\) and \(V_\Gamma\) are one
quarter of the corresponding quantities in (2.3), so (4.6) is exactly
\((N_{\tau,H}-A_{\tau,H})/8\).

### The \(V_4\) Haar cube

Let \(\tau,\sigma\) be disjoint transpositions and
\(\Gamma=\langle\tau,\sigma\rangle\cong C_2^2\).  Put

\[
P_{\varepsilon\eta}
=\frac14(I+\varepsilon\tau)(I+\eta\sigma),\qquad
a_K^{\varepsilon\eta}=P_{\varepsilon\eta}a_K.
\]

The four character sectors are orthogonal.  Equation (4.2) becomes

\[
\boxed{
\Psi_H(F_{\mathbf h})+\frac12B_H
=\frac12\|P_{++}f\|_H^2
+\frac12\sum_{\chi\ne++}
\left\|\sum_K\chi(h_K)a_K^\chi\right\|_H^2.}
\tag{4.7}
\]

Each \(h_K\) supplies two signs; the third nontrivial character sign is
their product.  This is an exact simultaneous Haar Max-\(4\)-cut problem.
It permits correlated choices unseen by fair independent one-transposition
resampling, but it does not permit arbitrary Fourier signs.

---

## 5. Static two-transposition rectangles collapse

A signed wreath vector \(z=z^+-z^-\) is a support-feasible middle trade
exactly when

\[
z_C\in\{-1,0,1\},\qquad
\mathcal A_mz=0,\qquad
\mathcal A_mz^+\le\mathbf1.
\tag{5.1}
\]

Then its two signs are partial factors covering the same middle masks.

### Lemma 5.1

If \(U\) is a partial factor and \(\pi\) is a coordinate transposition,
then

\[
U\cap\pi U=\varnothing.
\tag{5.2}
\]

#### Proof

Let \(\pi=(u\,v)\).  In a cyclic order, the total number of incidences of
\(u,v\) among the \(n\) middle intervals is \(2m=n-1\).  Therefore some
middle interval contains both or neither of \(u,v\), and is fixed by
\(\pi\).  Thus \(C\) and \(\pi C\) share a middle mask.

They are distinct for \(n\ge5\).  If a single label transposition
stabilized an unoriented odd cyclic order, it would induce a nonidentity
dihedral automorphism of an odd \(n\)-cycle.  Such an automorphism is a
nontrivial rotation or a reflection with one fixed vertex and \(m\)
transposed pairs, never one transposition when \(m\ge2\).  A partial factor
therefore cannot contain both \(C\) and \(\pi C\). \(\square\)

### Theorem 5.2 (static rectangle reduction)

Let \(U\) be a partial factor and let \(\tau,\sigma\) be distinct coordinate
transpositions, not necessarily commuting.  Set

\[
z=(I-\tau)(I-\sigma)\mathbf1_U
=\mathbf1_U-\mathbf1_{\tau U}-\mathbf1_{\sigma U}
+\mathbf1_{\tau\sigma U}.
\tag{5.3}
\]

Then \(z\) is support-feasible if and only if

\[
P=U\mathbin{\dot\cup}\tau\sigma U
\tag{5.4}
\]

is a partial factor and

\[
\mathcal A_m\mathbf1_P=\tau\mathcal A_m\mathbf1_P.
\tag{5.5}
\]

In that event

\[
\boxed{z=\mathbf1_P-\mathbf1_{\tau P},\qquad
\tau P=\tau U\mathbin{\dot\cup}\sigma U,}
\tag{5.6}
\]

and \(z\) decomposes into the connected components of the partial-support
ownership graph between \(P\) and \(\tau P\).  If the two sides have a
common exact-factor completion (in particular, if this rectangle occurs as
an applicable move in the exact-factor fibre), these are ordinary
\(\tau\)-ownership-component trades.

#### Proof

Lemma 5.1, applied to \(\tau,\sigma\), and conjugate transpositions, shows
that every positive-negative intersection among

\[
U,\ \tau\sigma U
\quad\text{and}\quad
\tau U,\ \sigma U
\]

is empty.  For example, after applying \((\tau\sigma)^{-1}\), an
intersection of \(\tau\sigma U\) with \(\sigma U\) becomes an intersection
of \(U\) with \(\sigma\tau\sigma U\), and
\(\sigma\tau\sigma\) is a transposition.  No cross-sign cancellation can
hide a coefficient of magnitude two.

Applying \(\tau\) maps
\(U\cap\tau\sigma U\) bijectively to
\(\tau U\cap\sigma U\).  Thus the same-sign families are disjoint
simultaneously.  If not, (5.1) fails.  If so, the positive side is \(P\)
and the negative side is \(\tau P\); conditions (5.1) are then exactly
(5.4)-(5.5).  The ownership graph between \(P\) and \(\tau P\) decomposes
their equal middle support into connected partial-support components.
With a common exact-factor completion, adjoining that common complement
makes these precisely the usual applicable \(\tau\)-components.
\(\square\)

### Corollary 5.3 (whole-factor rectangle no-go)

For an exact factor \(F\),

\[
(I-\tau)(I-\sigma)\mathbf1_F
\tag{5.7}
\]

is never support-feasible.  If a same-sign pair intersects, a coefficient
of magnitude two occurs.  If the two same-sign pairs are disjoint, each
sign is the union of two exact factors and covers every middle mask twice,
so it is not a partial factor.

Thus a formal two-transposition Haar rectangle is a relation among four
factor corners, not a new squarefree exact-factor move.

---

## 6. Nonlocal alternating circuits

Let

\[
F_0\to F_1\to\cdots\to F_t
\]

be any legal path of exact factors.  Put

\[
\delta_i=f(F_i)-f(F_{i-1}),\qquad
D=\sum_{i=1}^t\delta_i=f(F_t)-f(F_0).
\]

The moves may be state-dependent and may use different transpositions or
alternating trades at different steps.

### Theorem 6.1 (exact composition law)

\[
\boxed{\Psi_H(F_t)-\Psi_H(F_0)
=\langle f(F_0),D\rangle_H+\frac12\|D\|_H^2.}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
\Psi_H(F_t)-\Psi_H(F_0)
=\sum_i\left(
\langle f(F_0),\delta_i\rangle_H+\frac12\|\delta_i\|_H^2
\right)
+\sum_{i<j}\langle\delta_i,\delta_j\rangle_H.}
\tag{6.2}
\]

#### Proof

At step \(i\), the factor-independent quantization term cancels and

\[
\Psi_H(F_i)-\Psi_H(F_{i-1})
=\langle f(F_{i-1}),\delta_i\rangle_H
+\frac12\|\delta_i\|_H^2.
\]

Insert
\(f(F_{i-1})=f(F_0)+\sum_{j<i}\delta_j\) and sum.  Expansion of
\(\|\sum_i\delta_i\|_H^2\) gives both forms. \(\square\)

At one protected rank \(q\), \(D_q=0\) if and only if

\[
\boxed{\sum_{i<j}\langle\delta_{i,q},\delta_{j,q}\rangle
=-\frac12\sum_i\|\delta_{i,q}\|_2^2.}
\tag{6.3}
\]

All individual curvature at that rank cancels, but so does the total
linear score there.

Consequences:

1. A closed factor circuit has \(D=0\), hence zero energy change.
2. A global coordinate word has endpoint \(\pi F\).  Since \(\pi\) is
   unitary,

   \[
   \langle f,(\pi-I)f\rangle_H
   =-\frac12\|(\pi-I)f\|_H^2,
   \tag{6.4}
   \]

   so its linear gain and curvature cancel.  This includes global group
   commutators.
3. Independent sequential heat noises are martingale differences; their
   propagated variances add.  They cannot create negative cross-time
   covariance.

For four factor corners, write

\[
f_{10}=f_{00}+a,\qquad f_{01}=f_{00}+b,\qquad
h=f_{11}-f_{10}-f_{01}+f_{00}.
\]

Expansion gives

\[
\boxed{
\begin{aligned}
\Psi_{11}-\Psi_{10}-\Psi_{01}+\Psi_{00}
={}&\langle f_{00},h\rangle_H+\langle a,b\rangle_H\\
&+\langle a+b,h\rangle_H+\frac12\|h\|_H^2.
\end{aligned}}
\tag{6.5}
\]

If \(h=0\), the mixed energy is \(\langle a,b\rangle_H\).  If all four
corners are coordinate relabelings, all four energies agree and the
right-hand side is zero.  A useful Haar circuit requires a state-dependent
defect and a nonzero endpoint residual.

---

## 7. Fixing shallow shadows

For a group-component choice, the net rank-\(q\) effect is

\[
D_q(\mathbf h)=\sum_K(h_K-I)a_{K,q}.
\tag{7.1}
\]

### Proposition 7.1 (exact shallow-kernel criterion)

The move fixes all shadows through depth \(s\) if and only if the **same**
component choices satisfy

\[
\boxed{\sum_K(h_K-I)a_{K,q}=0\qquad(1\le q\le s).}
\tag{7.2}
\]

It changes depth \(r>s\) exactly when the analogous sum is nonzero there.
For a state-dependent path, replace (7.1) by its telescoping step sum.
Equation (6.3) then cancels all curvature at every protected depth.

The point is not the tautological equality but its integrality: (7.2) is a
common vector-discrepancy constraint across all depths, not an independent
sign choice at each rank.

Two audited exact obstructions eliminate the known bounded local systems.

* A coefficient-one Petr--Turek selector square is rank-isolated as a
  signed incidence vector, but neither sign is a middle packing.  Every
  connected support-feasible composite of adjacent-swap selector cells
  uses at least \(\lceil(m+1)/2\rceil\) cells.
* The complete local MSW four-letter \(2\)-for-\(2\) family has linearly
  independent first-shadow effects.  No nonzero combination of those
  trades fixes depth one while changing a deeper depth.  The family also
  touches only an \(O(1/m)\) fraction of the first-shadow layer.

Together with Theorem 5.2, this rules out bounded static
selector/MSW/Haar cubes.  It does not rule out a mesoscopic,
state-dependent preparation that creates a new ownership component.
Preparation can change which endpoint effects are legal, but Theorem 6.1
still governs their energy.

The minimal geometric precursor is open:

> **Prepared shallow component \((\mathrm{PSC})\) — UNPROVED.**
> For every sufficiently large \(m\), there is a legal exact-factor path
> to \(F'\), a coordinate transposition \(\tau\), and a nontrivial
> \(F'\)-versus-\(\tau F'\) component trade \(z_K\) such that
> \[
> \mathcal A_{m-1}z_K=0,\qquad
> \mathcal A_{m-r}z_K\ne0
> \quad\text{for some }r\ge2.
> \tag{7.3}
> \]

\((\mathrm{PSC})\) would show that dynamic recomputation escapes the local
first-shadow injection, but is not quantitatively sufficient for MWB.

---

## 8. Fixed-window curvature and packet descent

From (2.8), \(1\le c_q\le C_A\) on the fixed window, and Riemann sums give

\[
\sum_{q\le H}\frac1{c_q}
=(I_A+o(1))\sqrt m,\qquad
I_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{8.1}
\]

and

\[
\sum_{q\le H}\frac q{c_q}
=(J_A+o(1))m,\qquad
J_A=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\tag{8.2}
\]

For a bounded MSW four-letter trade,

\[
\|\delta_1\|_2^2=4,\qquad
\|\delta_q\|_2^2=8\quad(2\le q\le m-2).
\]

Its half-curvature on the fixed window is

\[
\frac12\|\delta\|_H^2=(4I_A+o(1))\sqrt m.
\tag{8.3}
\]

Thus the following would suffice:

> **Bounded-trade frame \((\mathrm{BTF}_A)\) — UNPROVED.**
> At every exact factor \(F\), there is a distribution on legal bounded
> trades such that
> \[
> \mathbb E\langle f,\delta\rangle_H
> \le-\eta_A\frac mW\Psi_H(F),\qquad \eta_A>0.
> \tag{8.4}
> \]

At a local minimum, (8.3)-(8.4) would imply

\[
\Psi_H(F)\le
\left(\frac{4I_A}{\eta_A}+o(1)\right)\frac W{\sqrt m}
=o(W).
\tag{8.5}
\]

The known bounded atlas has no proved bulk frame.

For a generic balanced alternating \(C_8\), the exact seam estimate is

\[
\|\delta_q\|_2^2\le32q.
\tag{8.6}
\]

Its half-curvature is at most

\[
16\sum_{q\le H}\frac q{c_q}
=(16J_A+o(1))m.
\tag{8.7}
\]

At drift scale \(m/W\), this gives only \(O(W)\).  Merely applying the
additive estimate
\(\mathbb E\|Z\|_H^2\le t(32\sum q/c_q)\) to a packet of \(t\) moves does
not improve the bound, because that certified drift and curvature both
scale by \(t\).  This is not a claim that the true net curvature must be
additive: negative cross terms are precisely the possible packet gain.

### Theorem 8.1 (conditional residual-packet descent)

Suppose that at every exact factor \(F\) (or at least at every global
minimizer) there is a distribution on legal state-dependent batches of
\(t=t(F)\ge1\) balanced \(C_8\) moves, with net effect \(Z\), such that

\[
\mathbb E\langle f,Z\rangle_H
\le-\alpha_A\frac{tm}{W}\Psi_H(F),
\tag{8.8}
\]

while

\[
\mathbb E\|Z\|_H^2
\le\varepsilon_m tB_{A,m},\qquad
B_{A,m}=32\sum_{q\le H}\frac q{c_q}=O_A(m).
\tag{8.9}
\]

Then a global minimum satisfies

\[
\boxed{\Psi_H(F_*)
\le\frac{\varepsilon_mB_{A,m}}{2\alpha_A m}W
=O_A(\varepsilon_mW).}
\tag{8.10}
\]

#### Proof

Every endpoint is an exact factor.  At a global minimum, Theorem 6.1 and
(8.8)-(8.9) give

\[
0\le\mathbb E\Delta\Psi_H
\le-\alpha_A\frac{tm}{W}\Psi_H(F_*)
+\frac12\varepsilon_mtB_{A,m}.
\]

Cancel \(t\) and rearrange. \(\square\)

Thus \(\varepsilon_m=o(1)\) proves \(\Psi_H=o(W)\);
\(\varepsilon_m=\Theta(1)\) recovers only the \(O(W)\) barrier.  Perfect
cancellation gives \(Z=0\), but then (8.8) has zero drift.  A successful
packet needs simultaneously:

1. legal exact intermediate factors;
2. near-total negative cross-correlation of its step effects;
3. a nonzero residual aligned against \(f\).

---

## 9. Smallest quantitative replacement lemma

Let \(\mathfrak G_m\) be the concrete family of elementary abelian
coordinate groups

\[
\mathfrak G_m=
\left\{
\left\langle (u_1\,v_1),\ldots,(u_t\,v_t)\right\rangle:
1\le t\le m,\ \{u_i,v_i\}_{i=1}^t\text{ pairwise disjoint}
\right\}.
\tag{9.0}
\]

These nontransitive groups are the natural first candidates: increasing
\(t\) makes their common fixed-target set small, while their middle-set
action still has many orbits.

> **Correlated Haar frame \((\mathrm{CHF}_A)\) — UNPROVED.**
> There are constants \(\eta_A,C_A>0\), independent of \(m\) and \(F\),
> such that for all sufficiently large \(m\), every exact factor \(F\)
> satisfies
> \[
> \boxed{
> \max_{\Gamma\in\mathfrak G_m}
> \bigl(A_\Gamma(F)-R_\Gamma(F)\bigr)
> \ge\eta_A\Psi_H(F)-C_AH\operatorname{Cat}_m.}
> \tag{9.1}
> \]

Here \(A_\Gamma,R_\Gamma\) are the exact quantities in
(4.3)-(4.4), with one common group-component choice across all depths.

### Theorem 9.1 (implication of \((\mathrm{CHF}_A)\))

If \((\mathrm{CHF}_A)\) holds for fixed \(A\), then some exact factor
satisfies

\[
\Psi_H(F_*)=O_A(H\operatorname{Cat}_m)
=O_A(W/\sqrt m)=o(W)
\tag{9.2}
\]

and \(P_H(F_*)=o(W)\).

#### Proof

Choose a global minimizer \(F_*\) of \(\Psi_H\) on the finite exact-factor
fibre.  By (4.5),
\(A_\Gamma(F_*)-R_\Gamma(F_*)=0\) for every \(\Gamma\).  Equation (9.1)
therefore gives

\[
\Psi_H(F_*)\le\frac{C_A}{\eta_A}H\operatorname{Cat}_m.
\]

Since

\[
\operatorname{Cat}_m
=\frac1{m+1}\binom{2m}{m}
=\frac{W}{2m+1}=\frac Wn
\]

and \(H=O_A(\sqrt m)\), (9.2) follows.  Equation (1.6) gives
\(P_H=o(W)\). \(\square\)

The additive term in (9.1) is the natural factor-size seam scale.
\(R_\Gamma\) optimizes correlated exact component choices, so this is
strictly more flexible than fair group resampling.  It also automatically
pays integral floor restitution and never asks a fractional projection to
reduce the raw norm below \(B_H\).

The spectral part alone is adequate.  Let
\(P_\tau=(I+\tau)/2\).  The zero point-margin subspace is invariant, and
(2.2) gives, for independent uniform transpositions,

\[
\mathbb E\|P_{\tau_T}\cdots P_{\tau_1}f\|_H^2
\le\left(1-\frac2n\right)^T\|f\|_H^2.
\tag{9.3}
\]

Indeed, conditioned on the current vector \(g\),

\[
\mathbb E_\tau\|P_\tau g\|_H^2
=\|g\|_H^2-\frac14\mathbb E_\tau\|g-\tau g\|_H^2
\le\left(1-\frac2n\right)\|g\|_H^2,
\]

because division of (2.2) by
\(\binom n2\) gives
\(\mathbb E_\tau\|g-\tau g\|_H^2\ge8\|g\|_H^2/n\).
Iterating proves (9.3).  Thus \(T=\Theta(n)\) yields constant coherent
contraction.

What is unproved is the integral implementation.  Rounding every
projection by common ownership components must restore the floor baseline,
and no theorem controls its harmful excess.  Enlarging the coordinate
group also coarsens the component partition; a middle-mask-transitive group
has one component and no descent.  No current theorem balances coherent
mixing against component fragmentation.

For a dynamic implementation, Theorem 8.1 is an alternative sufficient
target with the same \(o(W)\) scale: construct a recomputed legal packet
with \(\varepsilon_m=o(1)\) while retaining (8.8).  It is not logically
equivalent to the static group statement \((\mathrm{CHF}_A)\).  Static
rectangles cannot supply it by Theorem 5.2, and independent heat cannot
supply it because its martingale variances add.

---

## 10. Conditional implication to the OR bound

For every fixed \(A\), any one of \((\mathrm{CHF}_A)\),
\((\mathrm{BTF}_A)\), or Theorem 8.1 with \(\varepsilon_m=o(1)\) produces
one exact factor with

\[
\sum_{q\le A\sqrt m}\frac{O_q(F)}{c_q}=o(W).
\tag{10.1}
\]

This is the fixed-window overload statement \((\mathrm{GW})\).
Here is an explicit diagonalization.  For every positive integer \(j\),
choose increasing thresholds \(M_j\) such that the fixed-\(j\) overload is
at most \(W/j\) once \(m\ge M_j\).  Set

\[
A(m)=\max\{j\le m^{1/4}:M_j\le m\}.
\]

Then \(A(m)\to\infty\),
\(H=\lceil A(m)\sqrt m\rceil\le m^{3/4}+1=o(m)\), and
\(P_H=o(W)\).

Use the audited SCD-product outer-tail word beginning directly at this
diagonal \(H\).  Its exact bound is

\[
\nu(2m+1)
\le W+\frac{2H+1}{n}W+2P_H(F)+2L_m(m-H-1),
\tag{10.2}
\]

where the proved SCD-product estimate gives

\[
L_m(m-H-1)=o(W)
\tag{10.3}
\]

whenever \(H/\sqrt m\to\infty\) and \(H=o(m)\).  The other two error terms
satisfy

\[
\frac{2H+1}{n}W=o(W),\qquad 2P_H(F)=o(W).
\tag{10.4}
\]

Therefore (10.2) gives

\[
\nu(2m+1)\le W+o(W),
\]

and the standard trimmed one-bit lift gives the same leading constant in
even dimension.

This implication never weakens exact ownership.  It does not assert that
small overload produces the stronger labelled common nested resolution
\((\mathrm{CA}_A)\); that requires a separate stability theorem.

---

## 11. Adversarial audit

### Exactness

The group construction was checked against stabilizers and repeated
wreaths.  Each component support is \(\Gamma\)-invariant, each chosen
translate covers it once, and chosen translates from different components
cannot coincide because their middle supports are disjoint.  Thus (3.1)
is an actual factor, not an orbit average.

All component choices are common across depths.  Every circuit theorem
assumes exact intermediate factors and uses only the endpoint net effect.

### Factors of two and the floor baseline

The conventions are

\[
E_H=2\Psi_H,\qquad
\|f\|_H^2=B_H+E_H=B_H+2\Psi_H.
\]

Fair one-transposition resampling changes \(\Psi_H\) by
\((N_\tau-A_\tau)/8\), the aggregate spectral coefficient is
\(4(n-1)\), and

\[
P_H\le\Psi_H
\le\frac{R_H-4(n-1)B_H}{8(n-1)}.
\]

Replacing \(4(n-1)\) by \(2n\), or omitting \(B_H\), would be wrong.

### Quantifiers

The conclusions \(A_{\tau,H}\le N_{\tau,H}\) and
\(A_\Gamma=R_\Gamma\) hold only at a global minimizer of the same fixed
\(H\)-window objective.  They are not asserted for an arbitrary factor or
for a minimizer of another window.

The proof first fixes \(A\).  Only after proving every fixed-\(A\)
statement may one diagonalize to \(A(m)\to\infty\), slowly enough that
\(H=o(m)\).  The separate factor-independent overload tail beginning at
\(Q\asymp\sqrt{m\log m}\) is not used here: by itself it would leave the
annulus \(H<q<Q\) uncontrolled.  The SCD-product tail in (10.3) is what
starts directly at the diagonal \(H\).

### Static rectangles

Theorem 5.2 does not assume \(\tau,\sigma\) commute.  Cross-sign
intersections reduce to a partial factor meeting a transposition of itself;
same-sign intersections create coefficients \(\pm2\).  In the remaining
case the vector is exactly \(\mathbf1_P-\mathbf1_{\tau P}\), so no hidden
four-corner move remains.

### Circuits

Because \(\Psi_H\) is quadratic plus a factor-independent constant, there
are no higher-order terms in a long circuit.  Every apparent commutator
gain is a pairwise cross term already contained in \(\|D\|_H^2/2\).  A
closed circuit has \(D=0\), so a useful packet must retain a nonzero
residual as well as cancel curvature.

### Unproved statements

Neither \((\mathrm{PSC})\), \((\mathrm{BTF}_A)\), nor
\((\mathrm{CHF}_A)\) is proved.  In particular:

* no high-energy exact factor is proved to have a suitably fragmented
  multitransposition group graph;
* no Fourier or deterministic certificate controls \(R_\Gamma\) at the
  required scale;
* no state-dependent exact packet with \(o(1)\) relative net curvature is
  constructed;
* no counterexample exact factor with all relevant overlays connected is
  constructed.

This is therefore a move-system obstruction and an exact reduction, not a
proof or disproof of the conjecture.

---

## 12. Final theorem-level summary

**Unconditional new theorem.**  Finite coordinate groups admit the exact
group-component product (Theorem 3.1), whose optimal correlated descent is
exactly \((A_\Gamma-R_\Gamma)/2\) (Theorem 4.1).

**Unconditional no-go theorem.**  Every support-feasible static
two-transposition rectangle is a partial-support one-transposition trade;
with a common exact-factor completion it is a union of ordinary
one-transposition components.  The whole-factor rectangle is never
support-feasible (Theorem 5.2 and Corollary 5.3).

**Unconditional circuit identity.**  Every nonlocal alternating circuit
obeys (6.1)-(6.3); closed circuits and global coordinate commutators cannot
descend.

**Strongest conditional theorem.**  The correlated Haar frame
\((\mathrm{CHF}_A)\) implies
\(\Psi_H=O_A(W/\sqrt m)\), fixed-window overload \(o(W)\), and the final
OR bound after diagonalization.

**Smallest obstruction.**  Coherent mixing is available on the
transposition spectral scale, but adding generators coarsens ownership
components and can leave only global relabelings.  Static Haar rectangles
collapse, while independent dynamic heat adds nonnegative noise.  The
remaining task is one exact correlated-residual theorem above the
unavoidable \(4(n-1)B_H\) floor baseline.
