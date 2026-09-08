# Lane L: exact chronology and shallow heat absorption

Date: 2026-07-25

## 1. Result

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
t=\operatorname{Cat}_m=\frac Wn,
\]

and let \(F\) be an exact factor consisting of \(t\) cyclic wreath rows.
For \(1\leq q\leq m-1\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q},\qquad
f_q=\mu_q-\lambda_q\mathbf 1.
\]

The all-subset statements below use \(1\leq q\leq m-1\).  Every statement
involving the pair module \(E_2\), \(\alpha_q\), or component \(E_2\) heat
assumes \(1\leq q\leq m-2\).

The following statements are proved below.

1. **All-subset literal chronology.**  For every nonempty coordinate set
   \(A\) with \(|A|\leq r_q\), there is an integer
   \(L_{A,q}\in[0,qt]\), defined directly from the actual cyclic rows of
   \(F\), such that

   \[
   D_Af_q=\overline L_{|A|,q}-L_{A,q}.
   \tag{1.1}
   \]

   Consequently

   \[
   |D_Af_q|\leq qt.
   \tag{1.2}
   \]

   Every fixed trace cylinder therefore has centered discrepancy at most
   \(2^{|U|}qt\).  This is an exact integral constraint on every literal
   factor; it rules out all bounded-coordinate versions of the previously
   proposed high-energy signed obstructions.

2. **Exact pair chronology.**  If \(d_C(e)\in\{1,\ldots,m\}\) is the
   shorter cyclic distance of a coordinate pair \(e\) in row \(C\), and

   \[
   H_e^{(q)}=\sum_{C\in F}(q-m+d_C(e))_+,
   \tag{1.3}
   \]

   then

   \[
   D_2f_q(e)=H_e^{(q)}-\frac{tq(q+1)}{2m}.
   \tag{1.4}
   \]

   This gives an exact formula and an explicit upper bound for the full
   Johnson \(E_2\) component of \(f_q\).

3. **First-shadow constant.**  At \(q=1\), let \(h_{ab}\) count the rows
   in which \(a,b\) have maximal distance \(m\).  Then

   \[
   D_2f_1(ab)=h_{ab}-\frac tm
   \tag{1.5}
   \]

   and, for \(m\geq3\),

   \[
   \boxed{
   \|P_{E_2}f_1\|_2^2
   \leq K_mt,
   \qquad
   K_m=
   \frac{4(2m+1)(2m-1)(m-1)}
        {m(m+1)(m-2)}
   =16+\frac{4(7m+1)}{m(m+1)(m-2)}.}
   \tag{1.6}
   \]

4. **Exact component heat.**  For every coordinate permutation \(\sigma\),
   every genuine ownership component between \(F\) and \(\sigma F\), and
   the raw squared-displacement conventions

   \[
   A_{q,2}=\left\|P_{E_2}\sum_K\Delta_{K,q}\right\|_2^2,
   \qquad
   V_{q,2}=\sum_K\|P_{E_2}\Delta_{K,q}\|_2^2,
   \]

   one has, with

   \[
   \alpha_q=\binom{n-4}{m-q-2},
   \]

   \[
   \boxed{
   |A_{q,2}-V_{q,2}|
   \leq \frac{nt^2q^2(q+1)}{\alpha_q}.}
   \tag{1.7}
   \]

   At \(q=1\), this is the exact Catalan-scale bound

   \[
   \boxed{
   |A_{1,2}-V_{1,2}|
   \leq
   \frac{8(2m+1)(2m-1)}{(m+1)(m-2)}t
   =(32+o(1))t.}
   \tag{1.8}
   \]

5. **Quantitative composition into the constant-one route.**  For fixed
   \(A>0\), set \(H=\lceil A\sqrt m\rceil\).  Uniformly over all exact
   factors and all coordinate permutations, the entire \(E_2\) sector
   with \(q\leq m^{1/8}\) contributes only

   \[
   O_A(Ht)
   \tag{1.9}
   \]

   both to centered squared mass and to \(|A_H-V_H|\).  For a transposition,
   the sharper star geometry shows that the potentially adverse restitution
   \((V-A)_+\) from all \(E_2\) depths \(q\leq m^{3/8}\) is also
   \(O_A(Ht)\).  More strongly, for every correlated
   transposition-component signing, the full floor-energy change
   contributed by this sector is
   \(O_A(Ht)\).

Every underlying factor used in these statements is genuine, nonnegative,
squarefree, integral, and exact; every emitted child selects complete
ownership-component sides.  The differences and harmonic projections are
signed analytic vectors, but no signed or fractional wreath factor is
emitted or treated as a realization.

This is a proved lemma which plugs directly into \(HG_A\).  For the
positive-cut route it gives a uniform \(O_A(H\operatorname{Cat}_m)\) bound
for every correlated signing of the displayed shallow \(E_2\) sector, so
it plugs into any robust reduced local-minimum theorem whose guaranteed gain
exceeds that error.  An additive bound does not by itself preserve a merely
qualitative positive cut, and the lemma does not finish \(LM_A\).  The
remaining possible obstruction is in Johnson degrees at least three, or in
degree two at the mesoscopic depths left after the displayed cutoffs.

## 2. The integer-floor baseline is retained

Write

\[
\lambda_q=c_q+\theta_q,
\qquad c_q=\lfloor\lambda_q\rfloor,
\qquad 0\leq\theta_q<1,
\]

and define the full floor energy

\[
Q_q(F)=\sum_{|S|=r_q}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{2.1}
\]

Since \(\sum_S\mu_q(S)=W=N_q\lambda_q\), direct expansion gives the exact
identity

\[
\boxed{
Q_q(F)=\|f_q\|_2^2-\beta_q,
\qquad
\beta_q=N_q\theta_q(1-\theta_q).}
\tag{2.2}
\]

Thus the collision excess is \(\Phi_q=Q_q/2\).  The term \(\beta_q\) is
factor-independent, but it is not discarded: it remains explicitly in
(2.2), and it cancels exactly only when two legal exact factors are
compared.

Every row has exactly \(n\) cyclic \(r_q\)-intervals and exactly \(r_q\)
of them contain any prescribed coordinate.  Hence

\[
\sum_Sf_q(S)=0,
\qquad
\sum_{S\ni a}f_q(S)=0\quad(a\in[n]).
\tag{2.3}
\]

Therefore \(f_q\perp E_0\oplus E_1\) on the \(r_q\)-slice.

At \(q=1\),

\[
\lambda_1=\frac{m+2}{m},\qquad c_1=1,
\qquad
\beta_1=\frac{2W(m-2)}{m(m+2)}<4t.
\tag{2.4}
\]

## 3. The cyclic run-loss lemma

For a cyclic row \(C\), a nonempty coordinate set \(A\), and an integer
\(s\leq m\), let

\[
g_s^C(A)=\#\{\text{cyclic }s\text{-intervals of }C\text{ containing }A\}.
\]

### Lemma 3.1 (one run of starts)

For every nonempty \(A\), the starts of the cyclic middle intervals
containing \(A\) are either empty or form one linear run around the cycle.
For every \(0\leq q\leq m-1\),

\[
\boxed{
g_{m-q}^C(A)=(g_m^C(A)-q)_+.}
\tag{3.1}
\]

#### Proof

If an \(m\)-window contains \(A\), its complementary \((m+1)\)-window is
contained in a maximal cyclic run of \(C\setminus A\) of some length
\(L\geq m+1\).  There is at most one such run, because two of them would
have total length at least \(2(m+1)>2m+1=n\).  The complementary
\((m+1)\)-windows inside this run form one run of starts and number
\(L-m\).  Thus \(g_m^C(A)=L-m\).

An \((m-q)\)-window contains \(A\) exactly when its complementary
\((m+q+1)\)-window lies in the same run.  Their number is

\[
(L-m-q)_+=(g_m^C(A)-q)_+.
\]

This proves (3.1).  If no middle interval contains \(A\), neither can a
shorter interval. \(\square\)

Nonemptiness is essential; no use of (3.1) is made for \(A=\varnothing\).

### Theorem 3.2 (all-subset exact chronology)

For \(1\leq |A|\leq r_q\), define

\[
L_{A,q}=\sum_{C\in F}\min\{q,g_m^C(A)\}.
\tag{3.2}
\]

Then

\[
\boxed{
D_A\mu_q
:=\sum_{\substack{S\supseteq A\\|S|=r_q}}\mu_q(S)
=\binom{n-|A|}{m-|A|}-L_{A,q}.}
\tag{3.3}
\]

If \(j=|A|\), put

\[
\overline L_{j,q}
=\binom{n-j}{m-j}
-\lambda_q\binom{n-j}{m-q-j}.
\tag{3.4}
\]

Then \(\overline L_{j,q}\) is the average of \(L_{A,q}\) over all
\(j\)-sets, and

\[
\boxed{D_Af_q=\overline L_{j,q}-L_{A,q}.}
\tag{3.5}
\]

In particular,

\[
\boxed{|D_Af_q|\leq qt.}
\tag{3.6}
\]

#### Proof

Lemma 3.1 gives

\[
g_{m-q}^C(A)=g_m^C(A)-\min\{q,g_m^C(A)\}.
\]

The middle intervals owned by all rows of an exact factor partition
\(\binom{[n]}m\).  Therefore

\[
\sum_{C\in F}g_m^C(A)=\binom{n-j}{m-j}.
\]

Summing the preceding run-loss identity proves (3.3), and subtracting the
constant load proves (3.5).  Alternatively, summing \(D_Af_q\) over all
\(j\)-sets gives

\[
\sum_{|A|=j}D_Af_q(A)
=\binom{r_q}{j}\sum_{|S|=r_q}f_q(S)=0,
\]

so the constant in (3.5) is exactly the mean of \(L_{A,q}\).  Finally,
both \(L_{A,q}\) and its mean lie in \([0,qt]\), proving (3.6). \(\square\)

### Corollary 3.3 (fixed trace cylinders)

Let \(U\subset[n]\), let \(B\subseteq U\), and suppose the trace cell is
feasible at rank \(r_q\).  Put

\[
T_{U,B}(f_q)=
\sum_{\substack{|S|=r_q\\S\cap U=B}}f_q(S).
\tag{3.7}
\]

For this corollary adopt the natural convention

\[
D_Af_q=0\qquad (|A|>r_q).
\]

Then

\[
\boxed{
|T_{U,B}(f_q)|\leq
\begin{cases}
(2^{|U|}-1)qt,&B=\varnothing,\\[2mm]
2^{|U|-|B|}qt,&B\ne\varnothing.
\end{cases}}
\tag{3.8}
\]

#### Proof

For \(A\subseteq U\),

\[
D_Af_q=\sum_{B'\supseteq A}T_{U,B'}(f_q).
\]

Boolean-lattice inversion gives

\[
T_{U,B}(f_q)=
\sum_{A:\,B\subseteq A\subseteq U}
(-1)^{|A|-|B|}D_Af_q.
\]

Use (3.6).  When \(B=\varnothing\), the \(A=\varnothing\) term is zero
because \(D_\varnothing f_q=0\). \(\square\)

For fixed \(A>0\), fixed \(U\), and \(q\leq A\sqrt m\), the right side
of (3.8) is \(O_{A,U}(W/\sqrt m)=o(W)\).  On the other hand, every fixed
feasible trace cell contains \(\Theta_{A,U}(W)\) targets.  Consequently,
if

\[
f_q(S)=\phi(S\cap U)+e(S)
\]

and \(|\phi(B)|\geq\eta>0\) in one feasible cell, then

\[
\|e\|_1
\geq
\binom{n-|U|}{r_q-|B|}\eta
-2^{|U|}qt
=\Omega_{A,U,\eta}(W).
\tag{3.9}
\]

Thus no bounded-coordinate cylinder of constant amplitude can be corrected
into a literal exact-factor histogram by \(o(W)\), and in particular not by
\(O_A(Ht)\), mass.  This excludes the eight-coordinate rectangle and every
fixed-coordinate orthogonal-array variant as genuine exact-factor
obstructions.

## 4. Pair-distance identity and exact \(E_2\) norm

Throughout Sections 4--7, assume \(1\leq q\leq m-2\), so that
\(r_q\geq2\).

Fix a pair \(e=\{a,b\}\).  In one cyclic row \(C\), let
\(d_C(e)\in\{1,\ldots,m\}\) be its shorter cyclic distance.  The number of
cyclic \(s\)-intervals containing both points is

\[
(s-d_C(e))_+.
\tag{4.1}
\]

Define \(H_e^{(q)}\) by (1.3).  Since

\[
(m-q-d)_+=(m-d)_+-q+(q-m+d)_+,
\tag{4.2}
\]

exact middle coverage gives

\[
D_2\mu_q(e)
=\binom{n-2}{m-2}-qt+H_e^{(q)}.
\tag{4.3}
\]

Every odd cyclic order has exactly \(n\) unordered pairs at each distance
\(d\in\{1,\ldots,m\}\).  Hence

\[
\sum_eH_e^{(q)}
=nt\sum_{\ell=1}^q\ell
=\frac{ntq(q+1)}2.
\tag{4.4}
\]

There are \(\binom n2=nm\) pairs.  Since the total of \(D_2f_q\) is zero,
(4.3)--(4.4) prove the exact centered identity

\[
\boxed{
D_2f_q(e)=H_e^{(q)}-\frac{tq(q+1)}{2m}.}
\tag{4.5}
\]

The inclusion operator from the \(r_q\)-slice down to pairs annihilates
Johnson degrees greater than two.  Its squared singular value on \(E_2\)
is

\[
\alpha_q
=\binom{n-2}{r_q-2}
-2\binom{n-3}{r_q-3}
+\binom{n-4}{r_q-4}
=\binom{n-4}{r_q-2}.
\tag{4.6}
\]

Together with (2.3), this yields

\[
\boxed{
\|P_{E_2}f_q\|_2^2
=\frac1{\alpha_q}
\sum_e\left(H_e^{(q)}-\frac{tq(q+1)}{2m}\right)^2.}
\tag{4.7}
\]

Pointwise \(0\leq H_e^{(q)}\leq qt\).  Using \(x^2\leq(qt)x\) and
(4.4),

\[
\begin{aligned}
\sum_e(H_e^{(q)}-\overline H_q)^2
&=\sum_e(H_e^{(q)})^2-nm\overline H_q^2\\
&\leq
\frac{nt^2q^2(q+1)}2
\left(1-\frac{q+1}{2m}\right),
\end{aligned}
\tag{4.8}
\]

where \(\overline H_q=tq(q+1)/(2m)\).  Therefore

\[
\boxed{
\|P_{E_2}f_q\|_2^2
\leq
\frac{nt^2q^2(q+1)}{2\alpha_q}
\left(1-\frac{q+1}{2m}\right).}
\tag{4.9}
\]

### The first shadow

For \(q=1\), \(H_{ab}^{(1)}=h_{ab}\), the number of rows in which the
pair has distance \(m\).  Thus

\[
D_2f_1(ab)=h_{ab}-\frac tm.
\tag{4.10}
\]

Each row contributes the Hamilton cycle of its distance-\(m\) pairs, so

\[
\sum_{a<b}h_{ab}=nt,
\qquad
\sum_{b\ne a}h_{ab}=2t,
\qquad
0\leq h_{ab}\leq t.
\tag{4.11}
\]

Consequently

\[
\sum_{a<b}\left(h_{ab}-\frac tm\right)^2
\leq\frac{n(m-1)}m t^2.
\tag{4.12}
\]

Now

\[
\alpha_1=\binom{2m-3}{m-3},
\qquad
\frac W{\alpha_1}
=\frac{4(2m+1)(2m-1)}{(m+1)(m-2)}.
\tag{4.13}
\]

Equations (4.7), (4.12), and \(nt=W\) give exactly (1.6).

In particular, if a first-shadow defect were supported entirely in
\(E_2\), then (2.2), (2.4), and (1.6) would give

\[
Q_1\leq K_mt-\beta_1=O(t).
\tag{4.14}
\]

Thus a macroscopic pure-\(E_2\) local-minimum obstruction is impossible in
an exact factor.

## 5. Genuine ownership components

Fix a coordinate permutation \(\sigma\) and form the bipartite ownership
overlay between \(F\) and \(\sigma F\).  Every row vertex has degree \(n\),
so every connected component \(K\) has the same number \(s_K\) of rows on
its two sides.  The two sides own precisely the same set of middle roots.

Let \(\Delta_{K,q}\) be the lower-rank load on the plus side minus that on
the minus side.  For a pair \(e\), define

\[
H_{K,e}^{\pm,(q)}
=\sum_{C\in K^\pm}(q-m+d_C(e))_+.
\tag{5.1}
\]

The partial-family version of (4.3) has three terms: the common middle-root
incidence, the constant \(-qs_K\), and \(H_{K,e}^{\pm,(q)}\).  The first two
cancel between the sides.  Hence

\[
\boxed{
D_2\Delta_{K,q}=H_K^{+,(q)}-H_K^{-,(q)}.}
\tag{5.2}
\]

The vector \(\Delta_{K,q}\) has zero total and point margins.  Therefore

\[
\|P_{E_2}\Delta_{K,q}\|_2^2
=\frac1{\alpha_q}
\sum_e(H_{K,e}^{+,(q)}-H_{K,e}^{-,(q)})^2.
\tag{5.3}
\]

On each side,

\[
0\leq H_{K,e}^{\pm,(q)}\leq qs_K,
\qquad
\sum_eH_{K,e}^{\pm,(q)}
=\frac{ns_Kq(q+1)}2.
\tag{5.4}
\]

For \(0\leq x,y\leq qs_K\),

\[
(x-y)^2\leq qs_K(x+y).
\]

Thus

\[
\boxed{
\|P_{E_2}\Delta_{K,q}\|_2^2
\leq\frac{ns_K^2q^2(q+1)}{\alpha_q}.}
\tag{5.5}
\]

Summing (5.5), and using \(\sum_Ks_K=t\), gives

\[
V_{q,2}\leq
\frac{nq^2(q+1)}{\alpha_q}\sum_Ks_K^2
\leq\frac{nt^2q^2(q+1)}{\alpha_q}.
\tag{5.6}
\]

Applying the same two-side calculation to the full overlay, with \(s=t\),
gives the identical upper bound for \(A_{q,2}\).  Since both nonnegative
numbers lie in the same interval \([0,B]\), their difference has absolute
value at most \(B\).  This proves (1.7), and (1.8) follows from (4.13).

All component sign choices here select complete ownership-component sides.
They are therefore genuine integral exact factors.  Equations (5.2)--(5.6)
are not statements about a signed relaxation.

## 6. The sharper transposition bound

Suppose \(\sigma=\tau=(uv)\) is a transposition.  On one component side,
write

\[
a_x=H_K^{+,(q)}(ux),\qquad
b_x=H_K^{+,(q)}(vx)
\qquad(x\notin\{u,v\}).
\]

Orient the shores by

\[
K^+=K\cap F,
\qquad
K^-=K\cap\tau F.
\]

For completeness, each transposition component is invariant under the
involution which swaps its shores and applies \(\tau\).  Indeed, if the
cyclic distance between \(u,v\) in a row \(C\) is \(d\), exactly \(2d\)
of its \(n\) middle intervals contain exactly one of \(u,v\).  Since
\(n-2d\geq1\), the row owns a \(\tau\)-fixed middle interval.  The
corresponding ownership edge places the left copy of \(C\) and the right
copy of \(\tau C\) in the same component.  Thus
\(\tau K^+\subseteq K^-\); the equal shore cardinalities proved in Section
5 give

\[
K^-=\tau K^+.
\tag{6.1}
\]

Thus (5.2) is supported on the two stars at \(u,v\), and

\[
\|D_2\Delta_{K,q}\|_2^2
=2\sum_{x\ne u,v}(a_x-b_x)^2.
\tag{6.2}
\]

Moreover

\[
a_x,b_x\leq qs_K,
\qquad
\sum_{x\notin\{u,v\}}a_x,
\sum_{x\notin\{u,v\}}b_x\leq q(q+1)s_K.
\tag{6.3}
\]

Therefore

\[
2\sum_x(a_x-b_x)^2
\leq2\sum_x(a_x^2+b_x^2)
\leq4q^2(q+1)s_K^2.
\]

Using (4.6) and summing components gives

\[
\boxed{
V_{\tau,q,2}
\leq\frac{4q^2(q+1)t^2}{\alpha_q}.}
\tag{6.4}
\]

In particular,

\[
(V_{\tau,q,2}-A_{\tau,q,2})_+
\leq V_{\tau,q,2}.
\tag{6.5}
\]

This is the form relevant to adverse restitution at a transposition-cut
local minimum.

The same geometry gives a stronger all-sign statement.  For a component
signing \(\varepsilon=(\varepsilon_K)_K\in\{\pm1\}^{\mathcal K}\), let
\(G=F_\varepsilon\) be the resulting exact factor, with \(F\) designated
as the all-\(+\) signing, and put

\[
R_{\tau,q,2}(\varepsilon)
=\left\|P_{E_2}\sum_K\varepsilon_K\Delta_{K,q}\right\|_2^2.
\tag{6.6}
\]

The shore-swapping involution gives

\[
\mu_q(G)-\mu_q(\tau G)
=\sum_K\varepsilon_K\Delta_{K,q}.
\tag{6.7}
\]

Apply the two-star calculation above directly to the full exact factor
\(G\), taking \(s=t\).  Uniformly in \(\varepsilon\),

\[
\boxed{
R_{\tau,q,2}(\varepsilon),\ A_{\tau,q,2}
\leq B_q:=\frac{4q^2(q+1)t^2}{\alpha_q}.}
\tag{6.8}
\]

Because the transposition midpoint is \(\tau\)-invariant and every
\(\Delta_{K,q}\) is \(\tau\)-anti-invariant, these two subspaces are
orthogonal.  Consequently the exact contribution of this harmonic sector
to the full floor-energy change is

\[
\bigl[Q_q(G)-Q_q(F)\bigr]_{E_2}
:=\|P_{E_2}f_q^G\|_2^2-\|P_{E_2}f_q^F\|_2^2,
\]

and it satisfies

\[
\boxed{
\bigl[Q_q(G)-Q_q(F)\bigr]_{E_2}
=\frac14\left(R_{\tau,q,2}(\varepsilon)-A_{\tau,q,2}\right).}
\tag{6.9}
\]

The floor baseline cancels here only because both endpoints are complete
exact factors at the same rank.

## 7. Gaussian-window constants and the shallow cutoffs

Set

\[
R_{m,q}=\frac W{\alpha_q}.
\tag{7.1}
\]

For \(q=1\), (4.13) is exact.  For \(q\geq2\), factorial cancellation
gives

\[
R_{m,q}=
\frac{
(2m+1)(2m)(2m-1)(2m-2)
\prod_{i=2}^{q-1}(m+i)}
{\prod_{i=0}^{q+1}(m-i)}.
\tag{7.2}
\]

Empty products have their usual value one.  Fix \(A>0\).  For all
sufficiently large \(m\), every \(q\leq H=\lceil A\sqrt m\rceil\) satisfies
\(q+1\leq m/2\).  Using

\[
\log(1+x)\leq x,
\qquad
-\log(1-x)\leq2x\quad(0\leq x\leq1/2)
\]

in (7.2) yields the explicit uniform bound

\[
\boxed{
R_{m,q}\leq C_A:=81\exp(2(A+3)^2)
\qquad(1\leq q\leq H).}
\tag{7.3}
\]

Indeed, the four leading factors contribute at most \(81m^4\), and the
logarithm of the remaining normalized product is at most

\[
\frac{3(q+1)(q+2)}{2m}\leq2(A+3)^2.
\]

Also

\[
\sum_{q=1}^Qq^2(q+1)\leq2Q^4.
\tag{7.4}
\]

Since \(c_q\geq1\), (4.9), (7.3), and (7.4) give

\[
\boxed{
\sum_{q\leq Q}\frac{\|P_{E_2}f_q\|_2^2}{c_q}
\leq C_AQ^4t.}
\tag{7.5}
\]

Similarly, (1.7) gives

\[
\boxed{
\sum_{q\leq Q}\frac{|A_{q,2}-V_{q,2}|}{c_q}
\leq2C_AQ^4t.}
\tag{7.6}
\]

Take \(Q=\lfloor m^{1/8}\rfloor\).  Since \(Q^4\leq\sqrt m\leq H/A\),
both (7.5) and (7.6) are \(O_A(Ht)\).  Thus the complete arbitrary-overlay
\(E_2\) sector through depth \(m^{1/8}\) is an allowed floor-scale error in
\(HG_A\).

For a transposition, (6.4), (7.3), and (7.4) give

\[
\sum_{q\leq Q}
\frac{(V_{\tau,q,2}-A_{\tau,q,2})_+}{c_q}
\leq
\frac{8C_AQ^4}{n}t.
\tag{7.7}
\]

Taking \(Q=\lfloor m^{3/8}\rfloor\) and using \(n=2m+1\) gives

\[
\boxed{
\sum_{q\leq m^{3/8}}
\frac{(V_{\tau,q,2}-A_{\tau,q,2})_+}{c_q}
\leq\frac{4C_A}{A}Ht.}
\tag{7.8}
\]

This is uniform in the exact factor and in the transposition.

More strongly, (6.8)--(6.9) give, for every common component signing,

\[
\sup_\varepsilon
\left|
\sum_{q\leq Q}
\frac{[Q_q(F_\varepsilon)-Q_q(F)]_{E_2}}{c_q}
\right|
\leq\frac{2C_AQ^4}{n}t.
\tag{7.9}
\]

Hence, for all sufficiently large \(m\) depending on \(A\),

\[
\boxed{
\sup_\varepsilon
\left|
\sum_{q\leq m^{3/8}}
\frac{[Q_q(F_\varepsilon)-Q_q(F)]_{E_2}}{c_q}
\right|
\leq\frac{C_A}{A}Ht.}
\tag{7.10}
\]

The half-energy \(\Psi\) change has one further factor \(1/2\).

## 8. Why the same argument stops at degree three

The run identity has a useful exact harmonic form at \(q=1\).  For a
\(j\)-set \(T\), define

\[
\rho_j(T)=\#\{C\in F:g_m^C(T)>0\},
\qquad
A_j=\binom{n-j}{m-j}.
\tag{8.1}
\]

Theorem 3.2 says

\[
D_T\mu_1=A_j-\rho_j(T).
\tag{8.2}
\]

The mean of \(\rho_j\) is

\[
\boxed{
\overline\rho_j
=A_j-\frac{m+2}{m}\binom{n-j}{m-1-j}
=\frac jm A_j.}
\tag{8.3}
\]

Thus

\[
D_Tf_1=\overline\rho_j-\rho_j(T),
\qquad 0\leq\rho_j(T)\leq t.
\tag{8.4}
\]

Let \(f_1^{(i)}=P_{E_i}f_1\) and \(e_i=\|f_1^{(i)}\|_2^2\).  The exact
singular values of the inclusion map from rank \(m-1\) to rank \(j\) give

\[
\boxed{
\sum_{|T|=j}(\rho_j(T)-\overline\rho_j)^2
=\sum_{i=2}^j
\binom{m-1-i}{j-i}
\binom{n-j-i}{m-1-j}e_i.}
\tag{8.5}
\]

The elementary range bound is

\[
\sum_{|T|=j}(\rho_j(T)-\overline\rho_j)^2
\leq\binom nj\overline\rho_j(t-\overline\rho_j).
\tag{8.6}
\]

At \(j=2\), one has

\[
\frac{\overline\rho_2}{t}=1-\frac1m,
\]

so the support statistic is nearly saturated.  This is exactly the extra
factor \(1/m\) which produces the Catalan bound (1.6).

There is no analogous automatic gain at degree three.  For fixed \(j\),

\[
\frac{\overline\rho_j}{t}\longrightarrow\frac{j}{2^{j-1}}.
\tag{8.7}
\]

Already at \(j=3\), (8.5)--(8.6) permit

\[
e_3\leq(2+o(1))nW,
\tag{8.8}
\]

which is vastly above \(Ht\).  Thus the scalar range
\(0\leq\rho_j\leq t\) does not iterate the \(E_2\) miracle.

The harmonic energies can be recovered exactly from the owner-support
variances.  If

\[
V_j=\sum_{|T|=j}(\rho_j(T)-\overline\rho_j)^2,
\quad
s_{j,i}=\binom{m-1-i}{j-i}
\binom{n-j-i}{m-1-j},
\]

then

\[
e_2=\frac{V_2}{s_{2,2}},
\qquad
e_j=\frac{V_j-\sum_{i<j}s_{j,i}e_i}{s_{j,j}}
\quad(j\geq3).
\tag{8.9}
\]

Every numerator is nonnegative by orthogonality.  Combining this with the
integer floor gives

\[
\boxed{
Q_1=e_2+\sum_{j\geq3}e_j-\beta_1.}
\tag{8.10}
\]

Since \(e_2=O(t)\) and \(\beta_1=O(t)\), the exact remaining first-shadow
energy statement is

\[
\sum_{j\geq3}e_j=O_A(Ht).
\tag{8.11}
\]

No inequality proved here supplies (8.11).  In particular, the all-subset
chronology identities rule out bounded-coordinate structured defects but
do not rule out a growing-coordinate, high-harmonic, pseudorandom defect.

## 9. Implication for \(HG_A\), \(LM_A\), and constant one

For a genuine ownership overlay, the exact heat identity is

\[
\mathbb E_\varepsilon\Psi_H(F_\varepsilon)
=\Psi_H(F)-\frac18(A_H-V_H),
\tag{9.1}
\]

where every \(F_\varepsilon\) is an integral exact factor and

\[
\Psi_H=\sum_{q\leq H}\frac{Q_q}{2c_q}.
\]

Let \(\mathscr S=\{(q,E_2):q\leq m^{1/8}\}\), and define

\[
M_{\mathscr S}(F)
=\sum_{q\leq m^{1/8}}
\frac{\|P_{E_2}f_q\|_2^2}{c_q},
\qquad
\Psi_H^{\rm rem}=\Psi_H-\frac12M_{\mathscr S}(F).
\tag{9.2}
\]

The entire integer-floor baseline remains in \(\Psi_H^{\rm rem}\); it is
not allocated among harmonic sectors.  Equation (7.5) says

\[
|\Psi_H-\Psi_H^{\rm rem}|=O_A(Ht),
\tag{9.3}
\]

while (7.6) says that deleting \(\mathscr S\) changes \(A_H-V_H\) by
\(O_A(Ht)\).  Therefore any quantitative \(HG_A\) inequality for the
remaining gap against \(\Psi_H^{\rm rem}\) transfers to the original
\(HG_A\), with only a change in its additive constant.  Equivalently, one
may use the one-sided fact

\[
Q_q=\|f_q\|_2^2-\beta_q\leq\|f_q\|_2^2
\]

when moving the bounded shallow centered mass to the error.  This is the
precise floor-retaining sense in which the sector composes into the
constant-one heat route.

For transposition-cut local minima, every component signing is
nonimproving, so in particular the fair expected child is nonimproving and
the adverse fair sign is \(V-A\).
Equation (7.10) is stronger: every correlated component cut changes the
full floor potential through this \(E_2\) sector by at most \(O_A(Ht)\).
Thus this sector also composes with any **robust** reduced local-minimum
theorem asserting a cut gain larger than the displayed error.  It does not
compose with a merely qualitative assertion that some reduced cut has an
arbitrarily small positive gain: the shallow sector could cancel such a
gain.  The sectors in which a quantitative positive-cut theorem is still
needed are

\[
\boxed{
\begin{array}{ll}
\text{(i)}&\text{Johnson degree }j\geq3,\\
\text{(ii)}&E_2\text{ at a depth }q>m^{3/8},\\
\text{(iii)}&\text{cross-rank component restitution coupling these sectors.}
\end{array}}
\tag{9.4}
\]

This is a strict quantitative reduction of \(HG_A\), and of a robust
version of \(LM_A\).  The former composes directly with the audited
implication

\[
HG_A\Longrightarrow
\Psi_H=O_A(H\operatorname{Cat}_m)
\Longrightarrow
\nu(k)\leq(1+o(1))W(k).
\]

It is not a complete proof of \(HG_A\) or \(LM_A\).  No genuine exact
factor with a high-energy growing-harmonic local minimum was constructed,
so there is also no counterexample to either statement.

## 10. Decisive-step audit

The decisive identities were independently re-derived.  The checks are:

1. The cyclic start set is one run only for nonempty \(A\); the empty-set
   case is excluded explicitly.
2. The middle-to-lower loss is \(\min(q,g_m^C(A))\), not a fractional or
   averaged loss.
3. At \(q=1,j=2\), the owner-support mean is

   \[
   \overline\rho_2=\frac{m-1}{m}t,
   \]

   while the antipodal count has mean \(t/m\).  Since
   \(\rho_2(ab)=t-h_{ab}\), these are consistent and give (4.10).  Confusing
   the two means creates an off-by-\((1-2/m)t\) error.
4. The singular value in (4.6) is
   \(\binom{n-4}{r_q-2}\); no normalized-measure factor is present because
   all norms here are unnormalized counting norms.
5. Each ownership component has equal side sizes because the overlay is
   \(n\)-regular.  This is what cancels the \(-qs_K\) term in (5.2).
6. The arbitrary-permutation bound (5.5) uses only nonnegative actual row
   counts.  The transposition improvement (6.4) additionally uses the two
   relabelled stars and is not asserted for general permutations.
7. The heat convention in this report is the raw
   \(A=\|\sum_K\Delta_K\|^2\), \(V=\sum_K\|\Delta_K\|^2\) convention.  Under
   the fair-child variance convention, both appear divided by four; the
   heat identity (9.1) retains the audited factor \(1/8\).
8. The bound (8.8) is only a demonstration that the elementary
   owner-support range estimate is too weak.  It is not an exact-factor
   construction.
9. Equation (7.10) is uniform over every correlated component signing, but
   it supplies only an additive \(O_A(Ht)\) bound.  Deleting the sector from
   qualitative \(LM_A\) would require an additional robust gain margin.
10. In (9.2), the complete floor baseline stays in
    \(\Psi_H^{\rm rem}\).  No sectorwise portion of \(\beta_q\) is removed.

The proved endpoint of this lane is therefore the exact all-depth
chronology theorem and the shallow-\(E_2\) heat-absorption theorem.  The
unproved endpoint is a growing-harmonic owner-support/component-restitution
inequality strong enough to establish (8.11) simultaneously across the
Gaussian window.
