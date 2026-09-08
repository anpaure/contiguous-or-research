# QRE: the two-step Sinkhorn carrier and its positive overload tail

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

Let \(G_q^-\) be the maximal lower rank-twisted compatibility graph for
independent rank matchings, at

\[
                         q=A\sqrt m+O(1),\qquad A>0,
\tag{0.1}
\]

and put

\[
 d_R(X)=\binom{S(X)}q,\qquad
 B_{TX}={\mathbf1_{\{T\sim X\}}\over d_R(X)}.       \tag{0.2}
\]

Every retained source column of \(B\) sums to one. Define

\[
 \Lambda(T)=\sum_XB_{TX},\qquad
 C(X)=\sum_T{B_{TX}\over\Lambda(T)}
 ={1\over d_R(X)}\sum_{T\sim X}{1\over\Lambda(T)}. \tag{0.3}
\]

Define the lower source look-ahead carrier

\[
 L^-(X)={4\over\sqrt m}\sum_j
 \left(e_{j,k_j+1}(X_j)
       -{(d-|X_j\cap A_j|)(d-|X_j\cap C_j|)\over d}\right),
 \qquad k_j=|X_j|,                                  \tag{0.4}
\]

and define \(L^+(X)\) with the full-edge count in
\(\pi_{j,k_j-1}\). On the Gaussian core,

\[
                         L^\pm\Rightarrow N(0,1).   \tag{0.5}
\]

The exact carrier transition proved below is

\[
 \boxed{
 Z^-(T)=L^-(X)+A+o_B(1),\qquad
 Z^+(U)=L^+(X)+A+o_B(1),}                           \tag{0.6}
\]

when the target is chosen from a source column according to \(B\), which
is the uniform choice of \(q\) intrinsic split axes.

The remaining input is the one-vertex weighted saddle

\[
 \boxed{
 \log\Lambda_q^\pm(T)
 ={A^2\over2}+A Z^\pm(T)+o(1).}                    \tag{WGS}
\]

The multivariate coefficient expansion reducing WGS to a standard
uniform saddle extraction is recorded in Section 3.

Combining (0.6) with WGS gives

\[
 \boxed{
 \log C(X)=-{3A^2\over2}-A L^\pm(X)+o(1).}          \tag{0.7}
\]

Consequently

\[
                         \log C\Rightarrow
 N\!\left(-{3A^2\over2},A^2\right),                \tag{0.8}
\]

and

\[
 \boxed{
 {1\over W}|\{X:C(X)>1\}|
 \longrightarrow\Phi(-3A/2)>0.}                   \tag{0.9}
\]

Thus one row normalization of the source-uniform kernel is not a direct
fractional matching proof. This does not refute QRE: further nonuniform
scaling or a one-sided isoperimetric flow may still succeed.

## 1. Exact one-hit carrier edit

Fix one source block with half-counts

\[
                         \alpha=|X\cap A|,\qquad
                         \gamma=|X\cap C|.           \tag{1.1}
\]

Use its intrinsic matching \(\pi\), and let \(F\) be its number of full
edges. Then

\[
 F\sim\operatorname{Hyp}(d,\gamma,\alpha),\quad
 \mu_F={\alpha\gamma\over d},\quad
 \operatorname{Var}F=
 {\alpha\gamma(d-\alpha)(d-\gamma)\over d^2(d-1)}. \tag{1.2}
\]

The number of split edges occupied on the \(A\)-side is \(\alpha-F\).
Choose one with the size bias induced by a uniform split-axis deletion
and delete its \(A\)-endpoint. The intrinsic empty count increases by one,
while its centered mean increases by

\[
                         {d-\gamma\over d}.          \tag{1.3}
\]

The full-count size bias is exactly

\[
 {\mathbb E[(F-\mu_F)(\alpha-F)]
       \over\mathbb E(\alpha-F)}
 =-{\operatorname{Var}F\over\alpha-\mu_F}
 =-{\gamma(d-\alpha)\over d(d-1)}.                 \tag{1.4}
\]

The adjacent-rank look-ahead matching is independent and centered.
Therefore the mean lower edit score on an \(A\)-occupied split edge is

\[
 \boxed{
 r_A(\alpha,\gamma)
 =1-{d-\gamma\over d}
  -{\gamma(d-\alpha)\over d(d-1)}
 ={\gamma(\alpha-1)\over d(d-1)}.}                 \tag{1.5}
\]

The \(C\)-occupied calculation is symmetric:

\[
 \boxed{
 r_C(\alpha,\gamma)
 ={\alpha(\gamma-1)\over d(d-1)}.}                 \tag{1.6}
\]

Weighting (1.5)--(1.6) by their expected split counts gives

\[
 \bar r(\alpha,\gamma)=
 {\alpha\gamma\bigl((d-\gamma)(\alpha-1)
                  +(d-\alpha)(\gamma-1)\bigr)
  \over
  d(d-1)\bigl(\alpha(d-\gamma)+\gamma(d-\alpha)\bigr)}.
\tag{1.7}
\]

Uniformly on the central half-rank core,

\[
 \bar r(\alpha,\gamma)
 ={1\over4}
 +O\!\left({|\alpha-d/2|+|\gamma-d/2|+1\over d}\right).         \tag{1.8}
\]

Every edit score has variance \(O(d)\). For the upper sign,
complementation gives the same formulas.

## 2. Proof of the carrier transition

Choose a uniform retained middle owner \(X\), then choose uniformly one
of its \(\binom{S(X)}q\) sets of \(q\) intrinsic split axes. Let \(\ell_j\)
be the number chosen in block \(j\). Standard occupancy estimates give

\[
 \#\{j:\ell_j=1\}=q-O_{\mathbb P}(d),\qquad
 \#\{j:\ell_j\ge2\}=O_{\mathbb P}(d).              \tag{2.1}
\]

On an untouched block, the target carrier uses the same adjacent-rank
frame as \(L^-(X)\). On a one-hit block, the target carrier uses the
intrinsic source frame, and the difference is the edit score above.
Consequently

\[
 {4\over\sqrt m}\sum_{j:\ell_j=1}\bar r(\alpha_j,\gamma_j)
 ={4\over\sqrt m}\left({q\over4}+o(\sqrt m)\right)
 =A+o(1).                                           \tag{2.2}
\]

The conditional variance is at most

\[
 {16\over m}O(qd)=O(d/\sqrt m)=o(1).                \tag{2.3}
\]

The \(O_{\mathbb P}(d)\) multi-hit blocks contribute
\(O_{\mathbb P}(d^2/\sqrt m)=o(1)\), using
\(d^2=o(\sqrt m)\). This proves (0.6). The blockwise hypergeometric CLT
also gives (0.5), because the total unnormalized variance is
\(m/16+o(m)\).

## 3. The weighted Gaussian saddle

The exact lower row load is

\[
 \Lambda_q^-(T)=
 \sum_{\substack{\mathbf a\ge0\\\sum a_j=q}}
 {2^q\prod_j\binom{z_j(\mathbf a,T)}{a_j}
  \over\binom{q+\sum_js_j(\mathbf a,T)}q},          \tag{3.1}
\]

apart from the exponentially small low-dimension leave. The upper formula
has full counts in place of empty counts.

Use the exact beta identity

\[
 {1\over\binom Sq}
 =(S+1)\int_0^1x^q(1-x)^{S-q}\,dx                 \tag{3.2}
\]

to mark the source split count in (3.1). After also marking
\(\sum a_j=q\), this is a coefficient/integral of a product of independent
block polynomials. At its saddle:

1. the promotion variable is \(2A/\sqrt m+o(m^{-1/2})\);
2. \(q-O(d)\) blocks are hit once, \(O(d)\) twice, and higher hits have
   \(o(1)\) logarithmic contribution;
3. the only random linear target term is \(A Z^\pm(T)\);
4. the intrinsic source split carrier uses the rank-\(k\) frames and is
   independent, on unhit blocks, of the adjacent-rank target carrier, so
   its Gaussian exponential moment changes only the deterministic
   constant; and
5. the total third-order error is \(O(d^2/\sqrt m)=o(1)\).

Thus the product saddle reduces WGS to

\[
                         \log\Lambda_q^\pm(T)
 =c_A+A Z^\pm(T)+o(1).                              \tag{3.3}
\]

The exact conservation law and Gaussian exponential moments force

\[
 e^{A^2+o(1)}
 ={1\over N_q}\sum_T\Lambda_q^\pm(T)
 =e^{c_A+A^2/2+o(1)},
\]

and therefore

\[
                         c_A={A^2\over2}.            \tag{3.4}
\]

This proves WGS once the stated uniform coefficient extraction is
installed. Pointwise uniformity over all targets is not needed; an
exception negligible for the weighted edge measure suffices.

## 4. Second normalization

For a fixed source, \(B\) chooses each depth-\(q\) trace equally. Hence
WGS and (0.6) give

\[
\begin{aligned}
 C(X)
 &=\mathbb E_B[\Lambda(T)^{-1}\mid X]\\
 &=\exp\left(-{A^2\over2}-A(L^\pm(X)+A)+o(1)\right)\\
 &=\exp\left(-{3A^2\over2}-A L^\pm(X)+o(1)\right).
\end{aligned}                                      \tag{4.1}
\]

This proves (0.7)--(0.9). The mean check is

\[
 \mathbb EC(X)\longrightarrow
 e^{-3A^2/2}\mathbb Ee^{-AZ}
 =e^{-A^2}={N_q\over W},                            \tag{4.2}
\]

as required by \(\sum_XC(X)=N_q\).

### 4.1 An exact change-of-measure reduction

There is a weaker route to a linear aggregate overload which does not
require pointwise WGS. Let \(P\) be the probability measure on incidences
obtained by first choosing a retained source uniformly and then choosing
one of its \(q\)-traces uniformly:

\[
                         P(T,X)={B_{TX}\over G}.      \tag{4.3}
\]

Its target marginal is \(P_T(T)=\Lambda(T)/G\). Put
\(\rho_G=N_q/G\), and define

\[
 \widehat Q(T,X)
 ={P(T,X)\over \rho_G\Lambda(T)}.                   \tag{4.4}
\]

Then \(\widehat Q\) is a probability measure, its target marginal is
uniform, and its source marginal satisfies the exact identity

\[
 \widehat Q_X(X)={C(X)\over N_q}.                   \tag{4.5}
\]

Consequently, for every source family \(\mathcal S\),

\[
 {1\over|\mathcal S|}\sum_{X\in\mathcal S}C(X)
 =\rho_G\,{\widehat Q_X(\mathcal S)\over P_X(\mathcal S)}.
\tag{4.6}
\]

Thus it is enough to prove the **reverse carrier transition**

\[
 Z^\pm(T)=L^\pm(X)+A+o_{\widehat Q}(1).             \tag{RCT}
\]

Indeed, under \(P\), \(L^\pm\Rightarrow N(0,1)\). Under \(\widehat Q\),
the target is uniform, so \(Z^\pm\Rightarrow N(0,1)\); RCT then gives
\(L^\pm\Rightarrow N(-A,1)\). For a short fixed carrier interval \(I\)
around \(\ell\), (4.6) tends to

\[
 e^{-A^2}{\phi(\ell+A)\over\phi(\ell)}
 =\exp\left(-{3A^2\over2}-A\ell\right).             \tag{4.7}
\]

Choose a bounded interval strictly below \(-3A/2\). Its \(P\)-mass is a
positive constant and the right side of (4.7) is uniformly greater than
one. Hence RCT alone implies

\[
                         \sum_X(C(X)-1)_+=\Omega_A(W).           \tag{4.8}
\]

The local reverse edit has the same exact \(1/4\) mean as the forward
edit. For a lower target with half-counts \(a,c\), an empty-edge choice
size-biases its full count \(F\) by
\(z=d-a-c+F\). Therefore

\[
 {\mathbb E[(F-ac/d)z]\over\mathbb Ez}
 ={\operatorname{Var}F\over (d-a)(d-c)/d}
 ={ac\over d(d-1)}
 ={1\over4}+o(1)                                    \tag{4.9}
\]

on the central core. This is exactly (1.5) after writing
\(a=\alpha-1,c=\gamma\). The source inverse-degree weight changes one
block by a tilt \(O(d/\sqrt m)\), which is negligible after summing the
\(q\) edits. Hence RCT has the same local saddle and the same shift as
(0.6).

What remains to make (4.8) unconditional is a uniform reverse
coefficient extraction under (4.4). This is strictly weaker than
pointwise WGS: it asks only for the adjacent-carrier marginal under the
row-reweighted incidence measure.

## 5. Fixed-frame audit

For a legal constant-in-rank pair frame, a middle owner with \(f\) full
and \(s=m-2f\) split pairs satisfies exactly

\[
 \Lambda(T)={2^q\binom{f+q}q\over\binom sq},\qquad
 C(X)={\binom sq\over2^q\binom{f+q}q}.              \tag{5.1}
\]

Writing \(f=m/4+x\sqrt m\), Stirling gives

\[
                         \log\Lambda(T)
 =3A^2+8Ax+o(1).                                    \tag{5.2}
\]

For a uniform middle owner,
\((f-m/4)/\sqrt m\Rightarrow N(0,1/16)\), so a fraction
\(\Phi(-3A/2)+o(1)\) has \(C(X)>1\). This verifies the threshold and
shows that two-step monotonicity is not an abstract inclusion identity.

## 6. Boundary

Unconditional here:

1. the exact one-hit size-biased means (1.5)--(1.8);
2. the carrier transition \(Z=L+A+o_B(1)\), for both signs;
3. the Gaussian adjacent-rank source carrier; and
4. the exact fixed-frame obstruction.

Conditional only on the uniform weighted saddle extraction in Section 3:

1. the independent-frame row-load law WGS;
2. the lognormal second-step law; and
3. the positive overload density.

Conditional only on the weaker reverse carrier transition RCT:

1. a linear aggregate second-step excess (4.8), which already refutes the
   proposed \(o(W)\) excess criterion.

Thus the minimum remaining audit for a completely unconditional
independent-frame no-go is the one-vertex weighted coefficient extraction
from (3.1)--(3.2), not an all-cuts theorem.
