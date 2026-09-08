# Lane A at the corrected linear-seam scale: logarithmic zero-overlap control and the positive diffuse-cell dichotomy

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict and corrected target

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed.  The audited linear dominance seam requires only

\[
 \boxed{\overline\nu_H=o_A(B/H)=o_A(B/\sqrt r).}
 \tag{QST_A}
\]

Equivalently, its physical form is

\[
 \nu_H(P_r)=o_A(B\sqrt r).
\]

The stronger former target \(O_A(B/N)\) is not needed here.  This report
does **not** prove \((QST_A)\), and therefore does not prove coefficient
one.  It proves two vanishing improvements at exactly the corrected scale.

The audited voltage-itinerary bound puts only \(\exp(o_A(r))\) quotient
roots on cycles of length at most \(H+1\).  This is
\(o_A(B/\sqrt r)\).  Such cycles are discarded below, so every packed
trace under discussion is nonwrapping.

1.  For genuine zero-winding returns, write

    \[
      \Lambda=\delta(D_0)+\delta(D_s)-2r.
    \]

    All positive endpoint-overlap sectors

    \[
      0<\Lambda\le2L
    \]

    have total start count \(o_A(B/\sqrt r)\), provided

    \[
      4^L(L+2)^2(\log r)^{5/2}=o(\sqrt r).
      \tag{0.1}
    \]

    In particular every fixed positive \(\Lambda\) is harmless, uniformly
    as far as

    \[
      \Lambda\le(1/2-\varepsilon)\log _2r
    \]

    for any fixed \(\varepsilon>0\).  Together with the already audited
    \(\Lambda=0\) estimate, this removes the complete logarithmic-overlap
    zero-winding sector.

2.  For positive winding, small PBBS carrier deficits have a genuinely
    vanishing aggregate mass.  Uniformly for \(T\le r/2\),

    \[
      \sum_{D:\,d(D)\le T}d(D)=O(B\sqrt T).
      \tag{0.2}
    \]

    Hence every positive-winding packed subfamily whose overlap range has
    a fixed fraction carried by deficits \(T=o(r)\) is

    \[
      o(B/\sqrt r).
    \]

    After this diffuse part, all diverging winding, and near-total
    deficits are removed, the only residual consists of bounded winding,
    especially winding one, with one genuine chronological even--odd cell
    of length \(\Omega_A(\sqrt r)\) whose two carrier deficits are both
    interior-macroscopic.

Thus critical height-stratum saturation can no longer be supported by
bounded zero overlap or by the former \(d=\Theta(\sqrt r)\) positive
pseudoprofile.  The exact surviving mechanisms are stated in Section 5.

## 1. Zero winding: carrier overlap and shifted height caps

Let a genuine first zero-winding return have step-two duration \(s\le H\).
Write its canonical factorizations as

\[
 D_j=P_j1R_j0S_j,\qquad0\le j\le s,
\]

and let \(T_0,\ldots,T_{s-1}\) be the audited dual staircase words.  Put

\[
 e_j=\delta(D_j)=|P_j|+1.
\]

The exact forward and dual ledgers are

\[
 e_s=\sum_{j<s}(|S_j|+1),
 \qquad
 e_0=\sum_{j<s}(|T_j|+1),
 \tag{1.1}
\]

and the original height caps are

\[
 \operatorname {ht}(S_j)\le j,
 \qquad
 \operatorname {ht}(T_j)\le s-1-j.
 \tag{1.2}
\]

The two endpoint certificates are

\[
 \mathcal A=(\overline T_{s-1}0)\cdots(\overline T_00),
 \qquad
 \mathcal C=(0S_s)(0S_{s-1})\cdots(0S_1).
 \tag{1.3}
\]

They are a prefix and suffix of one carrier, with

\[
 \mathcal A=R_sO,
 \qquad
 \mathcal C=OR_0.
 \tag{1.4}
\]

The overlap dictionary is

\[
 |O|=|S_s|+1+\Lambda,
 \qquad
 \Lambda=e_0+e_s-2r,
 \tag{1.5}
\]

and the mandatory-overlap theorem gives

\[
 \operatorname {net}(O)=-1.
 \tag{1.6}
\]

Since \(\Lambda\) is even, write \(\Lambda=2\ell\).  The overlap begins
with the complete first block of \(\mathcal C\), so

\[
 O=(0S_s)E,
 \qquad |E|=2\ell.
 \tag{1.7}
\]

Equations (1.6)--(1.7) show that \(E\) is balanced.  Literal cancellation
in (1.3)--(1.4) gives

\[
 \begin{aligned}
 U &:=(0S_{s-1})\cdots(0S_1)=ER_0,\\
 V &:=(\overline T_{s-1}0)\cdots(\overline T_00)
      =R_s(0S_s)E.
 \end{aligned}
 \tag{1.8}
\]

### Lemma 1.1 (positive-overlap shifted caps)

Every genuine return with \(\Lambda=2\ell\) satisfies

\[
 \boxed{
 \begin{aligned}
  \operatorname {ht}(S_j)
   &\le\alpha_j:=\min\{j,s-j+\ell\},
       &&1\le j<s,\\
  \operatorname {ht}(T_j)
   &\le\beta_j:=\min\{s-1-j,j+1+\ell\},
       &&0\le j<s.
 \end{aligned}}
 \tag{1.9}
\]

#### Proof

Read the first identity of (1.8) from height \(s\).  The word \(R_0\)
stays between heights one and \(s\).  A balanced word of length \(2\ell\)
has vertical deviation at most \(\ell\), so all of \(U=ER_0\) stays
below height \(s+\ell\).  Within \(U\), the Dyck block \(S_j\) is based
at height \(j\).  Hence

\[
 \operatorname {ht}(S_j)\le s-j+\ell.
\]

Combine this with the first cap in (1.2).

For the second identity of (1.8), read from height \(s\).  The word
\(R_s\) stays between one and \(s\); the following block \(0S_s\) stays
between zero and \(s\); and the balanced word \(E\) can descend by at
most \(\ell\).  In the left side \(V\), the complemented Dyck block
\(\overline T_j\) is based at height \(j+1\).  It therefore cannot
descend by more than \(j+1+\ell\), so

\[
 \operatorname {ht}(T_j)\le j+1+\ell.
\]

Combine this with the second cap in (1.2). \(\square\)

## 2. The logarithmic positive-overlap theorem

Let \(C_j(z)\) be the generating function for Dyck paths of height at
most \(j\), and put

\[
 Q_0=Q_1=1,
 \qquad Q_{j+1}=Q_j-zQ_{j-1},
 \qquad C_j=\frac{Q_j}{Q_{j+1}}.
 \tag{2.1}
\]

Define

\[
 F_{s,\ell}(z)
 =\prod_{j=1}^{s-1}C_{\min\{j,s-j+\ell\}}(z).
 \tag{2.2}
\]

### Lemma 2.1 (injective array bound)

If \(z_{r,s,2\ell}\) is the number of normalized roots starting a
genuine zero-winding return of duration \(s\) and endpoint excess
\(2\ell\), then

\[
 \boxed{
 z_{r,s,2\ell}
 \le[z^r],z^{s-\ell}F_{s,\ell}(z)^2.}
 \tag{2.3}
\]

#### Proof

The root injects into

\[
 (S_1,\ldots,S_{s-1},T_0,\ldots,T_{s-1}).
 \tag{2.4}
\]

Indeed the first tuple determines \(U\).  Equation (1.8) makes \(E\) its
first \(2\ell\) bits and determines the remaining suffix \(R_0\).  The
dual tuple gives

\[
 P_01=(\overline T_{s-1}1)\cdots(\overline T_01).
\]

Since \(S_0=\varnothing\), this reconstructs

\[
 D_0=P_01R_00.
\]

No converse construction is used.

Writing \(|X|_e=|X|/2\), equations (1.1) and
\(e_0+e_s=2r+2\ell\) give the exact rank identity

\[
 r=s+\sum_{j=1}^{s-1}|S_j|_e
       +\sum_{j=0}^{s-1}|T_j|_e-\ell.
 \tag{2.5}
\]

The multiset of \(T\)-caps in (1.9) equals the multiset of \(S\)-caps
under \(j\mapsto s-1-j\); the extra cap zero contributes
\(C_0=1\).  Counting all capped arrays, and ignoring the additional
literal compatibility in (1.8), proves (2.3). \(\square\)

In the range \(\ell<s-1\), which is the only range used below, the
product (2.2) telescopes exactly.  For \(s=2q\) or \(2q+1\) and
\(\ell=2a\) or \(2a+1\), one obtains

\[
\begin{array}{c|c|c}
 &\ell=2a&\ell=2a+1\\ \hline
 s=2q&
 \displaystyle\frac{Q_{2a+1}}{Q_{q+a}Q_{q+a+1}}&
 \displaystyle\frac{Q_{2a+2}}{Q_{q+a+1}^2}\\[9pt]
 s=2q+1&
 \displaystyle\frac{Q_{2a+1}}{Q_{q+a+1}^2}&
 \displaystyle\frac{Q_{2a+2}}{Q_{q+a+1}Q_{q+a+2}}.
\end{array}
 \tag{2.6}
\]

At \(z=1/4\),

\[
 Q_j(1/4)=\frac{j+1}{2^j}.
 \tag{2.7}
\]

In every entry of (2.6), write the two denominator indices as \(U,V\).
Then

\[
 |U-V|\le1,
 \qquad U+V=s+\ell+1,
\]

and the numerator is \(Q_{\ell+1}\).  Consequently

\[
 \boxed{
 4^{-(s-\ell)}F_{s,\ell}(1/4)^2
 =\frac{4^\ell(\ell+2)^2}{(U+1)^2(V+1)^2}
 \le C\frac{4^\ell(\ell+2)^2}{s^4}}
 \tag{2.8}
\]

whenever \(\ell=o(s)\).

### Lemma 2.2 (uniform coefficient anti-concentration)

Uniformly once \(\ell\le\varepsilon_0s\), for one sufficiently small
absolute \(\varepsilon_0>0\), if \(X\) has probability generating
function

\[
 \mathbb Ez^X=\frac{F_{s,\ell}(z/4)}{F_{s,\ell}(1/4)},
\]

then

\[
 \boxed{
  \sup_n\Pr(X+X'=n)\le\frac C{s^2},}
 \tag{2.9}
\]

where \(X'\) is an independent copy.

#### Proof

By (2.6),

\[
 F_{s,\ell}=\frac{Q_{\ell+1}}{Q_UQ_V}.
 \tag{2.10}
\]

If \(V=U+1\), then

\[
 \frac{z^U}{Q_UQ_{U+1}}=H_U:=C_U-C_{U-1};
\]

if \(V=U\), then

\[
 \frac{z^{U-1}}{Q_U^2}=C_{U-1}H_{U-1}.
\]

Powers of \(z\) do not affect characteristic-function modulus, and the
normalized \(C_{U-1}\) factor has modulus at most one.

For \(z=e^{it}/4\), choose

\[
 x=\sqrt{1-e^{it}},\qquad\Re x\ge0.
\]

The exact identity

\[
 Q_n(z)=
 \frac{(1+x)^{n+1}-(1-x)^{n+1}}{2^{n+1}x}
 \tag{2.11}
\]

gives

\[
 \frac{|Q_{\ell+1}(z)|}{Q_{\ell+1}(1/4)}
 \le e^{(\ell+1)|x|}.
 \tag{2.12}
\]

The exact \(H_U\) formula gives absolute \(c,C>0\) such that its
normalized characteristic function obeys

\[
 |\varphi_{H_U}(t)|\le
 \begin{cases}
  1,&U|x|\le1,\\
  C(U|x|)^2e^{-cU|x|},&U|x|\ge1.
 \end{cases}
 \tag{2.13}
\]

For \(U|x|\le1\), positivity of the full product \(F_{s,\ell}\) gives
the trivial bound one.  For \(U|x|\ge1\), equation (2.12) is absorbed in
the exponential of (2.13), because \(\ell\le\varepsilon_0s=O(\varepsilon_0U)\).
Since
\(|x|\asymp\sqrt{|t|}\) near zero, integration after the substitution
\(y=U|x|\) gives

\[
 \int_{-\pi}^{\pi}|\varphi_X(t)|^2dt\le\frac C{U^2}\le\frac C{s^2}.
 \tag{2.14}
\]

Fourier inversion of the convolution law of \(X+X'\) proves (2.9).
The possibly signed coefficients of the analytic numerator
\(Q_{\ell+1}\) are never treated as probabilities. \(\square\)

Combining (2.3), (2.8), and (2.9) yields

\[
 \boxed{
 z_{r,s,2\ell}
 \le C\,4^r\frac{4^\ell(\ell+2)^2}{s^6}.}
 \tag{2.15}
\]

### Theorem 2.3 (logarithmic positive-overlap sector)

Let \(Z_r(A,L)\) be the number of normalized roots which start genuine
zero-winding returns with

\[
 s\le A\sqrt r,
 \qquad0<\Lambda\le2L.
\]

If (0.1) holds, then

\[
 \boxed{Z_r(A,L)=o_A(B/\sqrt r).}
 \tag{2.16}
\]

#### Proof

Choose

\[
 s_0=\left\lfloor\sqrt{\frac r{K\log r}}\right\rfloor
\]

with a fixed sufficiently large \(K\).  Since zero-winding duration
equals Dyck height, the path-graph spectral estimate makes all roots with
\(s\le s_0\) contribute

\[
 o(4^r/r^2)=o(B/\sqrt r).
 \tag{2.17}
\]

Condition (0.1) implies \(L=O(\log r)\), and hence \(L=o(s_0)\); in
particular \(L\le\varepsilon_0s\) throughout the retained range.  Apply
(2.15) above \(s_0\).  Then

\[
\begin{aligned}
 \sum_{\ell\le L}\sum_{s_0\le s\le A\sqrt r}
 z_{r,s,2\ell}
 &\le C4^r
 \left(\sum_{\ell\le L}4^\ell(\ell+2)^2\right)
 \left(\sum_{s\ge s_0}s^{-6}\right)\\
 &\le C4^r
 \frac{4^L(L+2)^2(\log r)^{5/2}}{r^{5/2}}.
\end{aligned}
 \tag{2.18}
\]

Since \(B/\sqrt r\asymp4^r/r^2\), (0.1) turns (2.18) into little-oh.
Together with (2.17), this proves (2.16). \(\square\)

Taking

\[
 2L\le(1/2-\varepsilon)\log _2r
\]

makes (0.1) immediate.  A packing has no more members than distinct
starts, so Theorem 2.3 proves the zero-winding part of \((QST_A)\) on
this complete overlap range.

## 3. The exact truncated-deficit estimate

For a Dyck root \(D\), let

\[
 d(D)=|S|+1
\]

in its first-highest-component factorization.  Write

\[
 b_{r,j}=\#\{D\in\mathcal D_r:d(D)=2j+1\}.
\]

### Lemma 3.1 (first-deficit convolution bound)

For every \(0\le j<r\),

\[
 \boxed{b_{r,j}\le\operatorname {Cat}_j\operatorname {Cat}_{r-j}.}
 \tag{3.1}
\]

#### Proof

The exact first-highest-component formula is

\[
 b_{r,j}
 =\sum_{h\ge1}A_{r-j,h}[z^j]C_h(z),
 \tag{3.2}
\]

where

\[
 A_{n,h}
 =[z^n],zC_{h-1}(z)igl(C_{h-1}(z)-C_{h-2}(z)\bigr).
\]

All coefficients are nonnegative,

\[
 [z^j]C_h(z)\le\operatorname {Cat}_j,
\]

and, by the same formula at \(j=0\),

\[
 \sum_hA_{n,h}=b_{n,0}\le\operatorname {Cat}_n.
\]

Substitution proves (3.1). \(\square\)

### Corollary 3.2 (truncated deficit mass)

Uniformly for \(1\le T\le r/2\),

\[
 \boxed{
 \mathscr D_{\le T}:=
 \sum_{D:\,d(D)\le T}d(D)
 \le C B\sqrt{T+1}.}
 \tag{3.3}
\]

#### Proof

Put \(J=\lfloor(T-1)/2\rfloor\).  Uniform Catalan bounds give, for
\(j\le r/2\),

\[
 \frac{\operatorname {Cat}_j\operatorname {Cat}_{r-j}}B
 \le\frac C{(j+1)^{3/2}}.
\]

Therefore

\[
 \mathscr D_{\le T}
 \le CB\sum_{j\le J}\frac{2j+1}{(j+1)^{3/2}}
 \le C'B\sqrt{T+1}.
 \qquad\square
\]

In particular, if \(T=T(r)=o(r)\), then

\[
 \frac{\mathscr D_{\le T}}N=o(B/\sqrt r).
 \tag{3.4}
\]

This is an actual vanishing improvement over the critical first-moment
ledger.

## 4. Positive winding: diffuse mass or an interior macroscopic cell

For a genuine positive-winding return put

\[
 D_j=\tau^jD_0,
 \qquad c_j=d(D_j),
 \qquad\widehat c_j=d(\phi D_j).
\]

Let

\[
 C_j=\sum_{i<j}c_i,
 \qquad Y_j=\delta(D_j)-C_j.
\]

For winding \(w\ge1\), the exact endpoint ledgers are

\[
 C_s=\delta(D_s)+wN,
 \qquad
 \sum_{j<s}\widehat c_j=\delta(D_0)+wN.
 \tag{4.1}
\]

Define the two chronological partitions

\[
 E_j=(-C_{j+1},-C_j],
 \qquad
 O_j=(Y_{j+1},Y_j].
 \tag{4.2}
\]

Their common range is exactly

\[
 J_I=(-wN,0],
 \tag{4.3}
\]

and their common refinement has at most \(2s-1\) nonempty cells.

We first remove the other extreme of the deficit distribution.  Use the
audited early-first-maximum estimate

\[
 M_{r,t}\le Cr^2 4^r
 \exp\!\left(-c\sqrt{r/t}\right).
 \tag{4.4}
\]

Choose an absolute \(\kappa_0\) so that \(c\sqrt{\kappa_0}>6\), and put

\[
 U_r=\left\lfloor\frac r{\kappa_0(\log r)^2}\right\rfloor,
 \qquad
 \mathcal X_r=\{D:d(D)>N-U_r\}.
 \tag{4.5}
\]

The exact identity

\[
 d(D)=N-\delta(D)-\delta(\phi D)
\]

implies \(D\in\mathcal X_r\Rightarrow\delta(D)<U_r\).  Consequently

\[
 \boxed{|\mathcal X_r|=o(B/\sqrt r).}
 \tag{4.6}
\]

Indeed, sum (4.4) over \(t<U_r\).  If a packed interval contains one
member of \(\mathcal X_r\) on either parity, choosing one such carrier is
injective across the family; on the odd parity this uses the bijectivity
of \(\phi\).  Hence all intervals containing a near-total carrier are
also \(o(B/\sqrt r)\).

### Theorem 4.1 (diffuse-or-macroscopic-cell dichotomy)

Fix \(0<\varepsilon<1/16\) and an integer \(K\ge2\).  Let
\(\mathcal P^+\) be a quotient-edge-disjoint family of positive-winding
returns with \(s(I)\le H\).  Put \(T=\lfloor\varepsilon N\rfloor\).

For one interval define

\[
 \begin{aligned}
 L_E(I)&=\sum_{j:\,c_j\le T}|E_j\cap J_I|,\\
 L_O(I)&=\sum_{j:\,\widehat c_j\le T}|O_j\cap J_I|.
 \end{aligned}
 \tag{4.7}
\]

There is a residual quantity \(\rho_{A,K,\varepsilon}(r)\), defined
below, for which

\[
 \boxed{
 |\mathcal P^+|
 \le C_A\left(\frac1K+\sqrt\varepsilon\right)
       \frac B{\sqrt r}
      +o(B/\sqrt r)
      +\rho_{A,K,\varepsilon}(r).}
 \tag{4.8}
\]

The residual \(\rho_{A,K,\varepsilon}(r)\) is the maximum size, after the
short-cycle and near-total-carrier deletions above, of a trace-compatible
family of genuine returns with

\[
 s\le H,qquad1\le w<K,
 \tag{4.9}
\]

each equipped with one actual cell \(E_j\cap O_k\), where
\(0\le j,k<s\), such that

\[
 \boxed{
 \begin{aligned}
 |E_j\cap O_k|&\ge\frac N{4H},\\
 \varepsilon N<d(D_j),d(\phi D_k)&\le N-U_r.
 \end{aligned}}
 \tag{4.10}
\]

The selected even carriers are pairwise distinct and the selected odd
carriers are pairwise distinct.

#### Proof

If \(L_E(I)\ge wN/4\), then \(L_E(I)\ge N/4\).  The even trace
supports of distinct intervals are disjoint.  Thus Corollary 3.2 gives

\[
 \#\{I:L_E(I)\ge wN/4\}
 \le\frac{4\mathscr D_{\le T}}N
 =O\!\left(\sqrt\varepsilon\frac B{\sqrt r}\right).
 \tag{4.11}
\]

The same bound holds for \(L_O\), because \(\phi\) maps all disjoint
even supports bijectively to disjoint odd supports.

If neither diffuse inequality holds, more than \(wN/2\) of \(J_I\)
lies in cells whose two carrier deficits both exceed \(T\).  There are at
most \(2s-1\) cells, so one has length at least

\[
 \frac{wN}{2(2s-1)}\ge\frac N{4H}.
 \tag{4.12}
\]

Delete the \(o(B/\sqrt r)\) intervals from (4.6); the two selected
carriers then satisfy (4.10).  Selecting one cell per interval makes a
bipartite matching: equality of two left roots contradicts disjoint even
supports, while equality \(\phi D_k=\phi D'_{k'}\) on the right implies
\(D_k=D'_{k'}\).

Finally the exact two-endpoint winding budget is

\[
 \sum_{I\in\mathcal P^+}w(I)=O(B/\sqrt r).
\]

Thus \(w\ge K\) contributes \(O(B/(K\sqrt r))\).  The remaining
intervals are precisely those counted by \(\rho_{A,K,\varepsilon}\),
which proves (4.8). \(\square\)

For winding one alone there is no \(K^{-1}\) term:

\[
 \boxed{
 |\mathcal P^{(w=1)}|
 \le C_A\sqrt\varepsilon\frac B{\sqrt r}
     +o(B/\sqrt r)+\rho^{(1)}_{A,\varepsilon}(r).}
 \tag{4.13}
\]

More generally, if \(T=o(r)\), equations (3.3) and (4.11) show directly
that every diffuse subfamily is \(o(B/\sqrt r)\).  This is the promised
strict improvement over critical height-stratum saturation.

## 5. Exact remaining gates

### 5.1 Zero winding

The already audited \(\Lambda=0\) theorem gives

\[
 \overline\nu_H^{0,\Lambda=0}=O(B/r)=o(B/\sqrt r).
\]

Theorem 2.3 adds every

\[
 0<\Lambda\le(1/2-\varepsilon)\log _2r.
\]

The precise unresolved zero-winding branch is therefore the growing
positive-overlap sector beyond this logarithmic range.  Its smallest
packing statement is

\[
 \boxed{
 \overline\nu_H^{0,\,
  \Lambda>(1/2-\varepsilon)\log _2r}
 =o_A(B/\sqrt r).}
 \tag{Z_{\rm grow}}
\]

for any one fixed \(\varepsilon\in(0,1/2)\).  The proof above
does not delete the overlap word or assert that deletion preserves PBBS
chronology; it counts the original genuine returns injectively.

### 5.2 Positive winding

The exact residual is

\[
 \boxed{
 \rho_{A,K,\varepsilon}(r)
 =o_{A,K,\varepsilon}(B/\sqrt r)
 \quad\text{for every fixed }A,K,\varepsilon.}
 \tag{P_{\rm cell}}
\]

If \((P_{\rm cell})\) holds, divide (4.8) by \(B/\sqrt r\), let
\(r\to\infty\), then \(\varepsilon\downarrow0\), and finally
\(K\to\infty\).  This proves the positive-winding part of \((QST_A)\).

The word “genuine” and the common chronological cell are indispensable.
The earlier constant-profile winding pseudoorbit has
\(d=\Theta(\sqrt r)\); Corollary 3.2 now shows that such diffuse mass is
only an \(o(1)\) fraction at the corrected critical scale.  A surviving
saturation must instead match two rare, interior-macroscopic carrier
spikes inside one actual low-winding PBBS return.

Together, \((Z_{\rm grow})\) and \((P_{\rm cell})\), plus the already
proved zero and short-cycle sectors, imply \((QST_A)\), and the audited
linear seam then implies coefficient one.

## 6. Adversarial audit

1.  **Correct scale.**  Every little-oh statement is normalized by
    \(B/H\asymp_A B/\sqrt r\), not by the unnecessarily strong \(B/N\).

2.  **Actual returns only.**  The zero-winding enumeration begins with a
    genuine first return and its literal carrier identities.  No use is
    made of the false implication \(d(D)=1\Rightarrow\) minimal return.

3.  **No overlap deletion.**  The balanced word \(E\) is used only to
    derive height caps.  It is not removed from the root, so there is no
    hidden assertion that deletion preserves first maxima or
    \(\tau\)-chronology.

4.  **Injection, not converse.**  Lemma 2.1 reconstructs \(D_0\) from
    its actual arrays.  The larger class of all capped arrays is used only
    as an upper bound.

5.  **Rank sign.**  The exact shift in (2.5) is \(-\ell\), forced by
    \(e_0+e_s=2r+2\ell\).

6.  **Signed \(Q\)-numerator.**  The product \(F_{s,\ell}\) has
    nonnegative coefficients.  The numerator \(Q_{\ell+1}\) in its
    analytic telescoping formula is controlled only by modulus; it is
    never assigned a probability law.

7.  **Odd support.**  In Theorem 4.1, disjointness on the odd carrier side
    follows from applying the bijection \(\phi\) to the complete disjoint
    even supports.  It is not an independent matching assumption.

8.  **Near-total carriers.**  Equation (4.6) counts roots, and choosing
    one such root per interval is injective.  No rarity-by-trace-length
    multiplication is used.

9.  **Residual scope.**  Neither \((Z_{\rm grow})\) nor
    \((P_{\rm cell})\) is proved here.  Consequently neither
    \((QST_A)\), coefficient one, nor the contiguous-OR conjecture is
    claimed.

10. **Independent check.**  A separate proof audit verified the carrier
    cancellation, shifted cap indices, array injection, all four parity
    formulas in (2.6), the \(Q\)-ratio Fourier bound, the truncated
    Catalan convolution, odd-support disjointness, cell constants, and
    the order of limits in (4.8).  Its only requested changes were the
    explicit \(\ell<s-1\) domain and the fixed
    \(\ell\le\varepsilon_0s\) Fourier range, both now stated above.
