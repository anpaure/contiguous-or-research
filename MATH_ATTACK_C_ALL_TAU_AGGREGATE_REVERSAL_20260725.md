# All-transposition locality reverses the aggregate duplicate--mixing gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer algebra, or numerical experiment is used.

---

## 0. Verdict

Let

\[
n=2m+1,\qquad W=\binom nm,
\qquad H=\lceil L\sqrt m\rceil,
\]

where \(L>0\) is fixed.  At depth \(q\), put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor\lambda_q\rfloor,
\]

\[
\beta_q=N_q\theta_q(1-\theta_q).
\]

All exact identities below are stated for \(H\le m-2\), which holds for
all sufficiently large \(m\) at fixed \(L\).

For an exact wreath factor \(F\), write

\[
Q_q(F)
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
=2\Phi_q(F).
\tag{0.1}
\]

This note proves an exact all-transposition **reversal theorem** for every
positive choice of depth weights.  Its two relevant specializations are

\[
a_q=\frac1{c_q},
\qquad
\mathcal Q_H(F)=\sum_{q\le H}a_qQ_q(F),
\tag{0.2}
\]

and

\[
a_q=\frac1{c_q(c_q+1)},
\qquad
\mathfrak F_L(F)=\sum_{q\le H}a_qQ_q(F)
=\sum_{q\le H}\frac{\Phi_q(F)}{\binom{c_q+1}{2}}.
\tag{0.3}
\]

For the corresponding aggregate AB7 shielding variable \(X_a\), one has
for every exact factor the identity

\[
\boxed{
X_a-2(n-1)\mathcal E_a(F)
=\frac12\sum_\tau
\bigl(V_{\tau,a}(F)-A_{\tau,a}(F)\bigr),
}
\tag{0.4}
\]

where \(\mathcal E_a=\sum_qa_qQ_q\), \(A_{\tau,a}\) is total
transposition heat, and \(V_{\tau,a}\) is total ownership-component
variance.

If \(F\) minimizes \(\mathcal E_a\) on every intrinsic
\(\tau\)-component cube, then each summand on the right of (0.4) is
nonnegative.  Consequently

\[
\boxed{X_a\ge2(n-1)\mathcal E_a(F).}
\tag{0.5}
\]

This is the exact reverse of the strict coefficient gap needed in the
aggregate duplicate--mixing route.  It includes the integer balancing
floor and the higher Johnson harmonics; neither has been discarded.

There is also a quantitative rigidity remainder.  If

\[
w_{KL}^{\tau,a}=\langle d_K,d_L\rangle_a
\]

is the off-diagonal Gram weight between two genuine ownership components,
then every all-transposition local minimum satisfies

\[
\boxed{
X_a-2(n-1)\mathcal E_a(F)
\ge
\frac1{18}\sum_\tau
\left(\sum_{K<L}(w_{KL}^{\tau,a})^2\right)^{1/2}.
}
\tag{0.6}
\]

Equality in (0.5) holds if and only if, for every transposition,

\[
\boxed{w_{KL}^{\tau,a}=0\quad(K\ne L).}
\tag{0.7}
\]

Equivalently, every corner of every intrinsic transposition cell has the
same \(\mathcal E_a\)-value.  A connected overlay is the vacuous
one-component special case of (0.7), but disconnected pairwise-orthogonal
cells are also allowed.

Thus the AB7 aggregate ledger does not supply an additional coercive
inequality at an all-transposition local minimum.  More precisely, an
upper bound of the form

\[
X_a\le(2-\eta)(n-1)\mathcal E_a+C(n-1)H\operatorname{Cat}_m
\tag{0.8}
\]

at such minima is already the missing local-minimum theorem, since
(0.5) and (0.8) give

\[
\mathcal E_a(F)\le \frac C\eta H\operatorname{Cat}_m.
\tag{0.9}
\]

At the exact coefficient \(2\), an aggregate upper bound controls only the
Gram shielding remainder in (0.4), and gives no bound at all on
\(\mathcal E_a\).  Coefficients larger than \(2\) give even less.

This closes the proposed route of deriving the local-minimum bound from
the aggregate duplicate--mixing identity plus locality alone.  It does
**not** refute the local-minimum theorem: no high-energy exact factor local
for every transposition is constructed here.  A proof of that theorem must
add a cross-transposition ownership statement which rules out high-energy
cut-dual shielding; a prescribed/fixed-overlay estimate cannot do so by
AB7.

---

## 1. Exact weighted setup

Fix arbitrary positive real weights

\[
a_q>0\qquad(1\le q\le H)
\tag{1.1}
\]

and define

\[
\mathcal E_a(F)=\sum_{q\le H}a_qQ_q(F).
\tag{1.2}
\]

Put

\[
f_q=\mu_q-\lambda_q\mathbf1.
\]

Since \(\sum_S\mu_q(S)=W\), direct expansion gives the exact integer
floor identity

\[
\boxed{\|f_q\|_2^2=Q_q+\beta_q.}
\tag{1.3}
\]

Indeed, if \(b(S)=\mu_q(S)-c_q\), then

\[
Q_q=\sum_Sb(S)(b(S)-1)
=\sum_Sb(S)^2-N_q\theta_q,
\]

whereas

\[
\|f_q\|_2^2
=\sum_S(b(S)-\theta_q)^2
=\sum_Sb(S)^2-N_q\theta_q^2.
\]

Their difference is \(N_q\theta_q(1-\theta_q)=\beta_q\), proving
(1.3).

Every wreath contributes \(n\) rank-\((m-q)\) intervals and contributes
exactly \(m-q\) such intervals through each coordinate.  Hence exactness
gives zero total and zero point-star margins for \(f_q\).  In the ordinary
Johnson decomposition,

\[
f_q=\sum_{j\ge2}f_{q,j}.
\tag{1.4}
\]

Define the nonnegative higher-harmonic surplus

\[
\mathsf S_q
=\sum_{j\ge3}(j-2)(n-j-1)\|f_{q,j}\|_2^2.
\tag{1.5}
\]

Fix an unordered coordinate transposition \(\tau\).  Let \(K\) range over
the genuine connected components of the ownership overlay between \(F\)
and \(\tau F\).  Orient the old and new shores of \(K\), and let

\[
d_{K,q}=\mu_q(K_{\rm old})-\mu_q(K_{\rm new}).
\tag{1.6}
\]

Then

\[
\sum_Kd_{K,q}=\mu_q-\tau\mu_q.
\tag{1.7}
\]

Use the weighted inner product

\[
\langle g,h\rangle_a
=\sum_{q\le H}a_q\langle g_q,h_q\rangle_2.
\tag{1.8}
\]

Set

\[
A_{\tau,a}
=\left\|\sum_Kd_K\right\|_a^2
=\sum_{q\le H}a_q\|\mu_q-\tau\mu_q\|_2^2,
\tag{1.9}
\]

\[
V_{\tau,a}=\sum_K\|d_K\|_a^2.
\tag{1.10}
\]

For a moved unordered target pair \(p=\{S,\tau S\}\), orient \(p\) and
write

\[
d_{\tau,p,K}=x_K(S)-x_K(\tau S).
\tag{1.11}
\]

Define

\[
\mathbf V_q=\sum_{\tau,p,K}d_{\tau,p,K}^2.
\tag{1.12}
\]

Because a component difference has the two coordinates \((d,-d)\) on a
moved pair,

\[
\boxed{\sum_\tau V_{\tau,a}=2\sum_{q\le H}a_q\mathbf V_q.}
\tag{1.13}
\]

Finally define the exact aggregate shielding coordinate

\[
\boxed{
X_q=\mathbf V_q-2(n-1)\beta_q-\mathsf S_q,
\qquad
X_a=\sum_{q\le H}a_qX_q.
}
\tag{1.14}
\]

For the factorial weights in (0.3), this is exactly AB7's
\(X_L^{\rm fac}\).  For the energy weights in (0.2), it is the identical
ledger with the floor-corrected \(\mathcal Q_H\)-normalization.

---

## 2. Exact aggregate reversal identity

### Theorem 2.1 (weighted all-transposition identity)

For every exact wreath factor and every positive weight sequence (1.1),

\[
\boxed{
X_a-2(n-1)\mathcal E_a(F)
=\frac12\sum_\tau(V_{\tau,a}-A_{\tau,a}).
}
\tag{2.1}
\]

#### Proof

At one depth, each pair \((\tau,p)\) is exactly one edge of the Johnson
graph \(J(n,m-q)\).  Its unnormalized Laplacian has eigenvalue

\[
j(n-j+1)
\]

on Johnson degree \(j\).  By (1.4)--(1.5),

\[
\begin{aligned}
\sum_{\tau,p}
(\mu_q(S)-\mu_q(\tau S))^2
&=\langle f_q,L_Jf_q\rangle\\
&=2(n-1)\|f_q\|_2^2+\mathsf S_q\\
&=2(n-1)(Q_q+\beta_q)+\mathsf S_q.
\end{aligned}
\tag{2.2}
\]

The first equality counts every unordered Johnson edge once.  The second
uses

\[
j(n-j+1)-2(n-1)=(j-2)(n-j-1),
\]

and the third is the exact floor identity (1.3).

The counting norm \(\|\mu_q-\tau\mu_q\|_2^2\) contains the two equal
squared coordinates on every moved unordered pair.  Therefore (2.2)
implies

\[
\sum_\tau A_{\tau,a}
=2\sum_{q\le H}a_q
\bigl(2(n-1)(Q_q+\beta_q)+\mathsf S_q\bigr).
\tag{2.3}
\]

Combine (1.13) and (2.3):

\[
\begin{aligned}
\frac12\sum_\tau(V_{\tau,a}-A_{\tau,a})
&=\sum_qa_q
\left[
\mathbf V_q-2(n-1)(Q_q+\beta_q)-\mathsf S_q
\right]\\
&=\sum_qa_qX_q-2(n-1)\sum_qa_qQ_q\\
&=X_a-2(n-1)\mathcal E_a(F).
\end{aligned}
\]

This proves (2.1).  Every \(\beta_q\) and every higher harmonic is retained
with its exact coefficient. \(\square\)

---

## 3. What all-cut locality forces

For a fixed transposition cell, orient the current factor as the all-plus
corner.  Put

\[
w_{KL}^{\tau,a}=\langle d_K,d_L\rangle_a
\qquad(K<L).
\tag{3.1}
\]

If \(I\) is a component subset, switching \(I\) changes the anti-invariant
profile from

\[
D=\sum_Kd_K
\quad\hbox{to}\quad
D-2d_I,
\qquad d_I=\sum_{K\in I}d_K.
\]

The invariant midpoint and every integer floor term are unchanged.
Consequently

\[
\boxed{
\mathcal E_a(F^I)-\mathcal E_a(F)
=-\langle d_I,d_{I^c}\rangle_a
=-\sum_{\substack{K\in I\\L\notin I}}w_{KL}^{\tau,a}.
}
\tag{3.2}
\]

Thus \(F\) is minimal on this whole cell exactly when

\[
\boxed{
\sum_{\delta I}w_{KL}^{\tau,a}\le0
\quad\hbox{for every component cut }I.
}
\tag{3.3}
\]

Uniform independent signs give

\[
\mathbb E\left\|\sum_K\varepsilon_Kd_K\right\|_a^2
=V_{\tau,a}.
\]

Since the current corner minimizes the same norm over every signing,

\[
\boxed{A_{\tau,a}\le V_{\tau,a}.}
\tag{3.4}
\]

Combining (3.4) for every transposition with Theorem 2.1 proves (0.5).

### Theorem 3.1 (equality classification)

Suppose \(F\) is minimal on every intrinsic transposition cell.  Equality
holds in (0.5) if and only if (0.7) holds for every transposition.

#### Proof

By (3.4), every summand on the right side of (2.1) is nonnegative.  Hence
equality in (0.5) holds exactly when

\[
A_{\tau,a}=V_{\tau,a}
\tag{3.5}
\]

for every \(\tau\).

For one fixed cell, let

\[
C(I)=\sum_{\delta I}w_{KL}^{\tau,a}.
\]

Locality gives \(C(I)\le0\) for every cut.  A uniform random cut separates
each component pair with probability \(1/2\), and therefore

\[
\mathbb EC(I)
=\frac12\sum_{K<L}w_{KL}^{\tau,a}
=\frac14(A_{\tau,a}-V_{\tau,a}).
\tag{3.6}
\]

Under (3.5), the expectation in (3.6) is zero.  Since every value is
nonpositive, every cut value is zero.

Let

\[
r_K=\sum_{L\ne K}w_{KL}^{\tau,a}.
\]

The singleton cut gives \(r_K=0\).  The cut \(\{K,L\}\) then gives

\[
0=r_K+r_L-2w_{KL}^{\tau,a}=-2w_{KL}^{\tau,a}.
\]

Thus every off-diagonal Gram entry vanishes.  Conversely, if all those
entries vanish, every signing has squared norm \(V_{\tau,a}\), so the cell
is energy-flat and (3.5) holds. \(\square\)

---

## 4. Quantitative Gram rigidity

### Lemma 4.1 (quadratic-chaos cut bound)

For one weighted component Gram graph, put

\[
s=\sum_{K<L}w_{KL},
\qquad
\sigma=\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\]

Then some component cut has weight at least

\[
\boxed{\frac s2+\frac\sigma{36}.}
\tag{4.1}
\]

#### Proof

For independent Rademacher signs define

\[
Z=\sum_{K<L}w_{KL}\varepsilon_K\varepsilon_L.
\]

Orthogonality of the degree-two characters gives

\[
\mathbb EZ=0,
\qquad
\|Z\|_2=\sigma.
\]

We first prove the needed degree-two Bonami inequality.  More generally, if
\(P\) is a multilinear Rademacher polynomial of degree at most \(d\), then

\[
\|P\|_4\le3^{d/2}\|P\|_2.
\tag{4.2a}
\]

Induct on the number of variables, writing \(P=A+\varepsilon B\), where
\(A\) has degree at most \(d\) and \(B\) has degree at most \(d-1\).
The elementary two-point calculation

\[
\frac{(A+B)^4+(A-B)^4}{2}
=A^4+6A^2B^2+B^4
\le(A^2+3B^2)^2
\]

and the triangle inequality in \(L^2\) give

\[
\|P\|_4^2
\le\|A\|_4^2+3\|B\|_4^2.
\]

The induction hypothesis bounds the last expression by

\[
3^d\|A\|_2^2+3\,3^{d-1}\|B\|_2^2
=3^d\|P\|_2^2,
\]

proving (4.2a).  Applying it with \(d=2\) to \(Z\) gives

\[
\|Z\|_4\le3\|Z\|_2=3\sigma.
\tag{4.2}
\]

Interpolation between \(L^1,L^2,L^4\) yields

\[
\|Z\|_2\le\|Z\|_1^{1/3}\|Z\|_4^{2/3}.
\]

Using (4.2),

\[
\mathbb E|Z|=\|Z\|_1\ge\frac\sigma9.
\tag{4.3}
\]

Since \(\mathbb EZ=0\), the expected negative part is
\(\mathbb E Z_-=\mathbb E|Z|/2\ge\sigma/18\).  Hence some signing has

\[
Z\le-\frac\sigma{18}.
\]

The cut defined by that signing has weight

\[
\frac12(s-Z)\ge\frac s2+\frac\sigma{36},
\]

which is (4.1). \(\square\)

### Theorem 4.2 (quantitative local shielding)

At a cell minimum,

\[
\boxed{
V_{\tau,a}-A_{\tau,a}
\ge
\frac19
\left(\sum_{K<L}(w_{KL}^{\tau,a})^2\right)^{1/2}.
}
\tag{4.4}
\]

Consequently every all-transposition local minimum obeys (0.6).

#### Proof

At a cell minimum every cut has weight at most zero.  Apply Lemma 4.1:

\[
0\ge\frac s2+\frac\sigma{36}.
\]

Since

\[
A_{\tau,a}-V_{\tau,a}=2s,
\]

this is precisely (4.4).  Sum (4.4) over \(\tau\), divide by two, and use
(2.1) to obtain (0.6). \(\square\)

Notice the direction: nonorthogonal component interactions make
\(X_a-2(n-1)\mathcal E_a\) **larger** at a local minimum.  They do not
create a coercive deficit below coefficient \(2\).

---

## 5. The coefficient-two wall with exact mesoscopic accounting

Take \(a_q=1/c_q\).  Then

\[
\mathcal E_a=\mathcal Q_H,
\qquad
X_a=:X_H^{Q},
\]

and every all-transposition \(\mathcal Q_H\)-local minimum satisfies

\[
\boxed{X_H^{Q}\ge2(n-1)\mathcal Q_H.}
\tag{5.1}
\]

Suppose an independent exact-factor theorem supplied, at all such minima,

\[
X_H^{Q}
\le(2-\eta_L)(n-1)\mathcal Q_H
+C_L(n-1)H\operatorname{Cat}_m,
\tag{5.2}
\]

where \(\eta_L>0\).  Equations (5.1)--(5.2) give exactly

\[
\boxed{
\mathcal Q_H
\le\frac{C_L}{\eta_L}H\operatorname{Cat}_m.
}
\tag{5.3}
\]

Thus (5.2), restricted to local minima, is not an easier consequence of
the aggregate ledger: it is already the missing local-minimum theorem in
shielding coordinates.

At coefficient two, the strongest analogous estimate

\[
X_H^Q\le2(n-1)\mathcal Q_H+C_L(n-1)H\operatorname{Cat}_m
\tag{5.4}
\]

only bounds

\[
\frac12\sum_\tau(V_{\tau,H}-A_{\tau,H})
\le C_L(n-1)H\operatorname{Cat}_m.
\]

It leaves \(\mathcal Q_H\) unrestricted.  This remains true even if the
right side of (5.4) is zero: Theorem 3.1 then says only that every
transposition cell is energy-flat.

The exact mesoscopic target is

\[
H\operatorname{Cat}_m
=\frac{HW}{n}
=\left(\frac L2+o_L(1)\right)\frac W{\sqrt m}
=o(W).
\tag{5.5}
\]

The integer floor retained in (2.1) has size

\[
B_H:=\sum_{q\le H}\frac{\beta_q}{c_q}
\sim\kappa_LW\sqrt m,
\tag{5.6}
\]

where

\[
\kappa_L
=\int_0^L
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.
\]

Its slow \(U_2\) transposition rate is \(2/n\), so

\[
\frac{2B_H}{n}
=\left(\frac{2\kappa_L}{L}+o_L(1)\right)
H\operatorname{Cat}_m.
\tag{5.7}
\]

Equations (5.6)--(5.7) show that no floor term has been hidden in the
reversal theorem: the entire floor appears in \(X_q\), cancels in (2.1)
with its exact Johnson coefficient, and remains on precisely the terminal
mesoscopic scale after applying the slow rate.

For the factorial weights \(a_q=1/[c_q(c_q+1)]\), the same proof gives

\[
\boxed{
X_L^{\rm fac}
-2(n-1)\mathfrak F_L
=\frac12\sum_\tau
(V_{\tau,\rm fac}-A_{\tau,\rm fac}).
}
\tag{5.8}
\]

Hence every all-transposition local minimum of the factorial objective
satisfies

\[
X_L^{\rm fac}\ge2(n-1)\mathfrak F_L.
\tag{5.9}
\]

This is exactly the coefficient appearing on the opposite side of AB7's
strict sufficient gate.  The two objectives are uniformly equivalent on a
fixed Gaussian window, but locality for one weight sequence need not imply
locality for the other; (5.1) and (5.9) are therefore stated separately
with their correct quantifiers.

---

## 6. Exact proved/conditional boundary

### Proved

1. Identity (2.1) is exact for every positive depth weighting, every exact
   factor, and the freshly recomputed genuine ownership components of every
   coordinate transposition.
2. The balancing floor \(\beta_q\), ordinary Johnson \(U_2\) baseline,
   and every higher harmonic occur with their exact coefficients.
3. All-transposition cell minimality forces the reverse inequality (0.5).
4. Equality is exactly pairwise orthogonality of the component innovations
   in every transposition cell, not merely connectedness.
5. Nonorthogonality strengthens the reverse inequality quantitatively by
   (0.6).
6. A strict aggregate upper coefficient below \(2\) at local minima is
   already the desired local-minimum estimate; coefficient \(2\) cannot
   bound the energy.

### Not proved

1. No all-transposition high-energy local exact factor is constructed.
   Thus \(\mathrm{LM}_L\) itself is not refuted.
2. No strict upper estimate such as (5.2) is proved.  Such an estimate
   would prove \(\mathrm{LM}_L\), not follow from the aggregate ledger.
3. The AB7 fixed-cell high-energy factors cannot be inserted here: their
   prescribed \((2\ 3)\)-locality does not imply locality for the other
   transpositions.
4. Connected-overlay or pairwise-orthogonal obstructions are exact
   sufficient mechanisms for a flat cell, but simultaneous realization at
   high energy for every transposition remains open.

The next statement must therefore use information absent from the
aggregate variables \((Q_q,\beta_q,\mathsf S_q,\mathbf V_q)\): a
cross-transposition theorem saying that high floor-corrected energy forces
one genuine component Gram graph to leave the negative cut dual.  In exact
form, it must produce

\[
\exists\tau\ \exists I:
\qquad
\sum_{\substack{K\in I\\L\notin I}}
\langle d_K,d_L\rangle_a>0
\tag{6.1}
\]

whenever \(\mathcal E_a>C_LH\operatorname{Cat}_m\).  This is precisely
the all-transposition structural content still missing.  AB7 rules out
replacing it by any fixed or prescribed-overlay version.
