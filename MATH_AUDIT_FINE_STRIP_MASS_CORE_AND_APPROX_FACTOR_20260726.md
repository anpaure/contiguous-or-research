# Fine strip cover: mass-conservation audit and the exact approximate-factor gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q},\qquad
 1\le H<h<m.
 \tag{0.1}
\]

The mass-conservation claims in Propositions 4.4--4.5 of
MATH_SYNTHESIS_FINE_STRIP_COVER_CONSTANT_ONE_20260726.md are correct.
They admit the following sharper form.

For a whole-strip family \(\mathcal F\), let

* \(E_0=\sum_{|S|=m}(\mu_0(S)-1)_+\);
* \(M_q^\pm\) be the signed depth-\(q\) hole counts;
* \(E_1^\pm=\sum_{|S|=m\pm1}(\mu_1^\pm(S)-1)_+\).

Then

\[
 \boxed{
 \tau-\tau^*=o(W)}
 \tag{0.2}
\]

is equivalent to the existence of \(\mathcal F\) satisfying

\[
 \boxed{
 E_0+\sum_{q=1}^H(M_q^-+M_q^+)=o(W).}
 \tag{0.3}
\]

This equivalence needs only \(H<h\). The stronger hypothesis
\(H/h=o(1)\) is not needed for the mass argument.

Moreover (0.3) automatically implies

\[
\begin{aligned}
 P&=N_1+o(W)=W+o(W),\\
 M_0&=o(W),\\
 E_1^-+E_1^+&=o(W),
\end{aligned}
\tag{0.4}
\]

where

\[
 P=2h|\mathcal F|
\tag{0.5}
\]

is the total strip-occurrence mass at every rank. In particular,

\[
 {H\over2h}(E_1^-+E_1^+)=o(W)
\tag{0.6}
\]

even if \(H/h\) is merely bounded below one. The apparently weak collar
coefficient hides no additional freedom.

Thus the true integral theorem is exactly an approximate-middle-factor
missing-shadow statement: select whole strips whose middle repeat excess is
\(o(W)\) and whose aggregate signed band holes are \(o(W)\).

This note does not prove that such a family exists. It proves three further
facts about the remaining gate.

1. Its natural mixed packing/covering LP has optimum zero. Hence there is
   no fractional cut obstruction left.
2. Independent or exchangeable orbit rounding still has a linear
   depth-one hole count, so the zero LP optimum does not round generically.
3. An approximate-factor family can be pruned to an owner-disjoint family
   with \(o(W)\) additional holes only from the stronger rate

   \[
   E_0=o\!\left({W\over hH}\right).
   \tag{0.7}
   \]

   The proved condition \(E_0=o(W)\) is insufficient for this black-box
   pruning. Owner recycling is therefore a genuine weakening, not disguised
   exact ownership.

The remaining conjecture is stated precisely in Section 8.

## 1. Rankwise mass conservation

Fix an integral strip family \(\mathcal F\). Every selected strip has
exactly \(2h\) occurrences at the middle and at each signed depth. Hence
the total occurrence mass at every such layer is

\[
 P=2h|\mathcal F|.
 \tag{1.1}
\]

Consider any one layer with \(N\) physical targets. Let \(M\) be its hole
count and

\[
 E=\sum_S(\mu(S)-1)_+
 \tag{1.2}
\]

its repeat excess. The covered targets contribute one first occurrence
and then their excess occurrences. Therefore

\[
 P=(N-M)+E,
\tag{1.3}
\]

or equivalently

\[
 \boxed{E-M=P-N.}
\tag{1.4}
\]

This identity has no asymptotic error.

At the middle layer it gives

\[
 E_0-M_0=P-W.
\tag{1.5}
\]

At signed depth one it gives

\[
 E_1^\pm-M_1^\pm=P-N_1.
\tag{1.6}
\]

## 2. Audit of the normal form

Put

\[
 a={H\over2h}.
\tag{2.1}
\]

The exact dual-slack ledger from Proposition 4.2 is

\[
 \mathfrak L(\mathcal F)
 =
 E_0+a(E_1^-+E_1^+)
 +(1-a)(M_1^-+M_1^+)
 +\sum_{q=2}^H(M_q^-+M_q^+).
\tag{2.2}
\]

Substitute (1.5)--(1.6). Since

\[
 E_0=M_0+P-W
\tag{2.3}
\]

and

\[
 E_1^-+E_1^+
 =M_1^-+M_1^++2(P-N_1),
\tag{2.4}
\]

one obtains

\[
\boxed{
\begin{aligned}
 \mathfrak L(\mathcal F)
 ={}&(M_0+P-W)\\
 &+M_1^-+M_1^+
   +{H\over h}(P-N_1)\\
 &+\sum_{q=2}^H(M_q^-+M_q^+).
\end{aligned}}
\tag{2.5}
\]

The first parenthesis is \(E_0\ge0\). The second line need not have
nonnegative summands separately when \(P<N_1\), but their total equals

\[
 a(E_1^-+E_1^+)+(1-a)(M_1^-+M_1^+)\ge0.
\tag{2.6}
\]

Thus no sign error is hidden in (2.5).

If \(P<N_1\), (1.6) and \(E_1^\pm\ge0\) imply

\[
 M_1^\pm\ge N_1-P.
\tag{2.7}
\]

Consequently the second line of (2.5) is at least

\[
 2(N_1-P)-{H\over h}(N_1-P)
 =\left(2-{H\over h}\right)(N_1-P).
\tag{2.8}
\]

This is positive because \(H<h\).

## 3. SCI implies the unweighted core

Assume \(\mathfrak L(\mathcal F)=o(W)\). Every term in the original
nonnegative form (2.2) can be read separately. Since

\[
 1-a>1/2,
\tag{3.1}
\]

we obtain

\[
 E_0=o(W),
\qquad
 M_1^-+M_1^+=o(W),
\qquad
 \sum_{q=2}^H(M_q^-+M_q^+)=o(W).
\tag{3.2}
\]

This proves (0.3).

For later use, (2.7)--(2.8) give

\[
 P\ge N_1-o(W).
\tag{3.3}
\]

Middle conservation and \(E_0=o(W)\) give

\[
 P=W-M_0+E_0\le W+o(W).
\tag{3.4}
\]

Because

\[
 W-N_1={W\over m+1}=o(W),
\tag{3.5}
\]

equations (3.3)--(3.4) imply

\[
 P=N_1+o(W)=W+o(W).
\tag{3.6}
\]

Then (1.5) gives

\[
 M_0=E_0+W-P=o(W).
\tag{3.7}
\]

Finally, (2.4) and (3.2), (3.6) give

\[
 E_1^-+E_1^+=o(W).
\tag{3.8}
\]

This proves every assertion in (0.4).

## 4. The unweighted core implies SCI

Now assume (0.3). Middle conservation gives the exact upper bound

\[
 P=W-M_0+E_0\le W+E_0.
\tag{4.1}
\]

Using (1.6) separately on the two signed depth-one layers,

\[
\begin{aligned}
 E_1^-+E_1^+
 &=M_1^-+M_1^++2(P-N_1)\\
 &\le M_1^-+M_1^+
   +2(W-N_1)+2E_0.
\end{aligned}
\tag{4.2}
\]

Every quantity on the right is \(o(W)\), by (0.3) and (3.5). Hence

\[
 \boxed{E_1^-+E_1^+=o(W).}
\tag{4.3}
\]

In particular,

\[
 a(E_1^-+E_1^+)\le E_1^-+E_1^+=o(W),
\tag{4.4}
\]

so the collar coefficient causes no loss. Substituting (0.3)--(4.4) into
(2.2) proves \(\mathfrak L(\mathcal F)=o(W)\), hence SCI.

The same assumptions also give a lower bound for \(P\):

\[
 P\ge N_1-M_1^-=N_1-o(W).
\tag{4.5}
\]

Together with (4.1), this recovers (3.6), and then (1.5) gives
\(M_0=o(W)\). Thus all statements in (0.4) follow directly from the
unweighted core.

This proves the equivalence with exact inequalities and shows that the
assumption \(H/h=o(1)\) was stronger than necessary.

## 5. Direct approximate-factor packing/covering program

Let

\[
 \mathcal T_{\rm band}
 =\bigcup_{q=1}^H
 \left(\binom{[2m]}{m-q}\cup
       \binom{[2m]}{m+q}\right).
\tag{5.1}
\]

For a cycle \(C\), let

\[
 A_{T,C}=\mathbf1_{\{T\in\mathcal T_H(C)\}},
\qquad
 B_{X,C}=\mathbf1_{\{X\text{ is a middle owner of }C\}}.
\tag{5.2}
\]

The exact integral approximate-factor objective is

\[
\begin{aligned}
 \kappa_{m,H,h}=\min\quad&
 \sum_Xu_X+\sum_Tz_T,\\
 \text{subject to}\quad&
 \sum_CA_{T,C}x_C+z_T\ge1
       &&(T\in\mathcal T_{\rm band}),\\
 &\sum_CB_{X,C}x_C-u_X\le1
       &&(X\in\binom{[2m]}m),\\
 &x_C,z_T\in\{0,1\},\quad u_X\in\mathbb Z_{\ge0}.
\end{aligned}
\tag{5.3}
\]

For fixed \(x\), the minimizing variables are

\[
 z_T=\mathbf1_{\{T\text{ uncovered}\}},
\qquad
 u_X=(\mu_0(X)-1)_+.
\tag{5.4}
\]

Therefore

\[
 \boxed{
 \kappa_{m,H,h}
 =\min_{\mathcal F}
 \left[E_0(\mathcal F)+
       \sum_{q=1}^H(M_q^-+M_q^+)\right].}
\tag{5.5}
\]

The mass audit proves

\[
 \boxed{\mathrm{SCI}\quad\Longleftrightarrow\quad
 \kappa_{m,H,h}=o(W).}
\tag{5.6}
\]

### Proposition 5.1 (zero fractional obstruction)

The linear relaxation of (5.3) has optimum zero.

#### Proof

Let \(D_q\) be the number of catalogue cycles through a fixed signed
depth-\(q\) target. Give every cycle weight

\[
 x_C={1\over D_1}.
\tag{5.7}
\]

Every signed depth-\(q\) target receives load

\[
 {D_q\over D_1}={N_1\over N_q}\ge1.
\tag{5.8}
\]

Every middle owner receives load

\[
 {D_0\over D_1}={N_1\over W}<1.
\tag{5.9}
\]

Thus \(z_T=u_X=0\) is feasible in the fractional relaxation, with objective
zero. Nonnegativity proves optimality. \(\square\)

For reference, the dual of this zero-optimum relaxation is

\[
\begin{aligned}
 \max\quad&\sum_Ty_T-\sum_Xw_X,\\
 \text{subject to}\quad&
 0\le y_T\le1,\qquad0\le w_X\le1,\\
 &\sum_{T\in\mathcal T_H(C)\cap\mathcal T_{\rm band}}y_T
 \le\sum_{X\in C}w_X
 \qquad(C\in\mathscr C_{m,h}).
\end{aligned}
\tag{5.10}
\]

Its optimum is zero. Hence no fractional target-family cut can obstruct
the approximate-factor theorem; the remaining issue is pure integrality
of whole-strip columns.

## 6. Owner-disjoint pruning and its exact rate loss

The unweighted core permits repeated middle owners. It is useful to know
exactly when these repetitions can be removed without solving a new trade
problem.

### Lemma 6.1 (greedy owner-disjoint extraction)

From any strip family \(\mathcal F\), one can delete at most
\(E_0(\mathcal F)\) cycles and obtain a middle-owner-disjoint subfamily.

#### Proof

Process the cycles in an arbitrary order, retaining a cycle if it is
middle-disjoint from those already retained. If a cycle is rejected,
choose one middle owner which already occurred in a retained cycle and
charge the rejected cycle to its incidence at that owner.

At an owner of total multiplicity \(d\), at most \(d-1\) rejected cycles
can be charged there. Charges belonging to different rejected cycles are
distinct. Therefore the number rejected is at most

\[
 \sum_X(d_X-1)_+=E_0(\mathcal F).
\]

\(\square\)

One deleted strip can uncover at most \(2h\) targets in each of the
\(2H\) signed nonmiddle layers, hence at most

\[
 4hH
\tag{6.1}
\]

band targets. Therefore the extracted owner-disjoint family has at most

\[
 \sum_{q=1}^H(M_q^-+M_q^+)+4hH\,E_0
\tag{6.2}
\]

signed band holes.

### Corollary 6.2 (rate needed for black-box factor extraction)

The unweighted core implies an owner-packed missing-shadow theorem by this
generic pruning only under

\[
 E_0=o\!\left({W\over hH}\right).
\tag{6.3}
\]

The actual SCI-equivalent condition is only \(E_0=o(W)\). Thus black-box
pruning loses a factor \(hH\), and cannot close the theorem at the proved
rate.

This does not prove that some more delicate cycle trades cannot repair
repetitions cheaply. It proves that owner-disjointness cannot be recovered
from the mass estimate alone.

## 7. Direct fixed-frame escape theorem

The approximate-factor formulation permits owner recycling, but the
middle repeat budget shows that recycling cannot conceal the fixed-frame
Gaussian deficit.

Fix one coordinate perfect matching \(P\). Call a strip \(P\)-supported if
its \(h\) active replacement pairs are pairs of \(P\). Let

\[
 \mathcal F_P=\{C\in\mathcal F:C\text{ is \(P\)-supported}\},
 \qquad
 P_P=2h|\mathcal F_P|.
\tag{7.1}
\]

At a fixed signed depth \(q\), let \(p_f\) be the occurrence mass supplied
by \(\mathcal F_P\) from middle owners of \(P\)-type \(f\). Let \(V_f\) be
the number of all middle owners of that type and \(T_{f,q}\) the number of
signed depth-\(q\) targets of the corresponding type.

### Theorem 7.1 (positive-density frame escape)

For every strip family and every fixed frame \(P\),

\[
 \boxed{
 M_q^\pm(\mathcal F)
 \ge
 \left[
 D_{m,q}-E_0(\mathcal F)-(P-P_P)
 \right]_+,}
\tag{7.2}
\]

where

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+
\tag{7.3}
\]

is the exact fixed-frame type deficit.

Consequently, if the unweighted core (0.3) holds and
\(q=x\sqrt m+o(\sqrt m)\), \(x>0\), then

\[
 P-P_P\ge(\delta(x)-o(1))W,
\tag{7.4}
\]

where

\[
 \delta(x)
 =e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.
\tag{7.5}
\]

Thus no fixed coordinate pairing can support all but \(o(W)\) of the
selected occurrence mass.

#### Proof

Within the \(P\)-supported subfamily, every depth-\(q\) occurrence preserves
the full-pair type \(f\). If a middle owner occurs \(d\) times in
\(\mathcal F_P\), all but its first incidence contribute to its repeat
excess. Hence there are numbers \(r_f\ge0\) such that

\[
 p_f\le V_f+r_f,
\qquad
 \sum_fr_f\le E_0(\mathcal F_P)\le E_0(\mathcal F).
\tag{7.6}
\]

One occurrence can cover at most one signed target at the fixed depth.
Therefore the number of targets missed by \(\mathcal F_P\) is at least

\[
\begin{aligned}
 \sum_f(T_{f,q}-p_f)_+
 &\ge\sum_f(T_{f,q}-V_f-r_f)_+\\
 &\ge D_{m,q}-\sum_fr_f\\
 &\ge D_{m,q}-E_0(\mathcal F).
\end{aligned}
\tag{7.7}
\]

Every cycle outside \(\mathcal F_P\) supplies \(2h\) occurrences at this
signed depth, so all such cycles together can repair at most
\(P-P_P\) of these missing targets. This proves (7.2).

Under (0.3), \(M_q^\pm=o(W)\), \(E_0=o(W)\), and \(P=W+o(W)\).
The Gaussian fixed-frame census gives
\(D_{m,q}=(\delta(x)+o(1))W\). Substitute these estimates into (7.2) to
obtain (7.4). \(\square\)

The theorem attacks the approximate-factor problem at the whole-strip
level. It does not rely on owner-disjointness: every repeated \(P\)-owner
is paid for explicitly from \(E_0\). It shows that any positive proof must
mix cycle frames at positive occurrence density, not merely repair a
fixed-frame factor with \(o(W)\) outside incidences.

## 8. Direct missing-shadow conjecture and proved boundary

### Proved

1. The mass-conservation normal form (2.5) is exact.
2. SCI is equivalent to the unweighted approximate-factor core (0.3) for
   every \(H<h\).
3. The collar-weighted depth-one repeat term is automatically \(o(W)\);
   inequality (4.2) is the exact reason.
4. The approximate-factor LP (5.3) has fractional optimum zero.
5. Independent whole-cycle rounding has a linear depth-one hole count, so
   zero fractional cost does not round generically.
6. Generic pruning to an owner-disjoint family requires the stronger rate
   (6.3).
7. Every successful family has the positive-density frame-escape property
   (7.4) for every fixed pairing.

### Open

> **Approximate-factor missing-shadow theorem.** For
> \(H=\lceil\sqrt{m\log m}\rceil\) and dyadic
> \(h=m^{3/4+o(1)}\), prove
> \[
>  \kappa_{m,H,h}=o(W).
> \]

Equivalently, find a whole-strip family with middle repeat excess \(o(W)\)
and aggregate signed band holes \(o(W)\).

The dependent Hall theorem proves the analogous statement after replacing
whole strips by independently assignable owner-face incidences. The
SCD-Hoffman theorem proves it after replacing whole strips by owner-rooted
nested paths. Neither replacement lies in the whole-strip column semigroup.
Thus using either theorem here without a new lifting argument would assume
the missing cycle-bundling step.
