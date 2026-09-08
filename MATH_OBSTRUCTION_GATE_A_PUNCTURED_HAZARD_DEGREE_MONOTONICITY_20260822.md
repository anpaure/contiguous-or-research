# Gate A no-go: punctured Palm hazard is not monotone in the root degree

**Date:** 2026-08-22  
**Status:** exact finite obstruction to the all-test monotone-regression
shortcut; it is not an obstruction to the specific twelfth-order tail
covariance or to an asymptotic tail-decorated estimate

## 0. Outcome

On the genuine directed-punctured configuration at $r=3$, delete one
uniform middle target and one uniform lower target.  Let

\[
 \zeta_\sigma(d)=\mathbb E\left[\frac{h_\gamma}{Z}
          \mathrel{\Big|}\operatorname{sh}(v)=\sigma, d_v=d\right]
                                                               \tag{0.1}
\]

under the state--root--ordered-twelve-carrier Palm law.  Then

\[
 \boxed{\zeta_M(360)<\zeta_M(336)},\qquad
 \boxed{\zeta_L(912)<\zeta_L(904)}.                          \tag{0.2}
\]

In both cases the displayed degree levels are adjacent in the support of
the corresponding Palm degree law.  Thus the proposed shortcut

\[
                 d\longmapsto\zeta_\sigma(d)
                 \quad\hbox{is nondecreasing}                \tag{0.3}
\]

is false even on a genuine punctured two-shore slice.

This conclusion is deliberately narrow.  Monotonicity of (0.3) would make
the hazard covariance favorable for *every* increasing degree test.  Its
failure does not determine the sign for any particular test.  In fact, for
the normalized $m=12$ test at threshold $11/10$, the aggregate hazard
covariance on this same slice is favorable by the exact signed calculation
in `MATH_CORRECTION_GATE_A_SIGNED_REFERENCE_TAIL_CLUSTER_20260822.md`.
Nor does (0.2) refute an asymptotic tail-mass-relative polymer bound.

## 1. The finite punctured slice and its Palm law

Put $b=7$.  The middle targets are the triples and the lower targets are
the pairs of $[7]$.  For a permutation
$w=(w_0,\ldots,w_6)$, define cyclic windows

\[
 I_k^w(s)=\{w_s,\ldots,w_{s+k-1}\}
\]

and the directed-punctured row

\[
 E(w)=\{(M,I_3^w(s)):1\le s\le6\}
       \mathbin{\dot\cup}
       \{(L,I_2^w(s)):1\le s\le6\}.                         \tag{1.1}
\]

The lower--middle containment graph of (1.1) is the canonically oriented
path $L_1,M_1,\ldots,L_6,M_6$.  Each same-start difference
$M_i\setminus L_i$ recovers one word label; these recover six positions,
and the unique unused label recovers the seventh.  Thus the path
reconstructs $w$, so the catalogue consists of the $7!=5040$ distinct
rows (1.1).  Delete a triple $A$ and a pair $B$,
independently and uniformly, and retain precisely the catalogue rows
avoiding both.  The $735=35\cdot21$ states have the three relabelling
orbits

\[
\begin{array}{c|ccc}
j=|A\cap B|&0&1&2\\ \hline
\#\text{ states}&210&420&105\\
\text{representative }(A,B)&(012,34)&(012,03)&(012,01).
\end{array}                                                  \tag{1.2}
\]

For a residual state $H$, write $Z=|E(H)|$, $d_v$ for a root degree,
and

\[
 \Gamma(F)=\{G\in E(H):F\cap G\ne\varnothing\}.
\]

An ordered twelve-carrier at $v$ is
$\gamma=(v;F_1,\ldots,F_{12})$, where the distinct $F_i$ contain $v$,
and its union hazard is

\[
 h_\gamma=\left|\bigcup_{i=1}^{12}\Gamma(F_i)\right|.       \tag{1.3}
\]

The Palm measure assigns equal mass to every triple
$(H,v,\gamma)$, with $H$ uniform on the 735 states.  Consequently a
state--root pair of degree $d$ has weight $(d)_{12}$.  Definition (0.1)
therefore means

\[
 \zeta_\sigma(d)=
 \frac{
  \sum_H\sum_{\substack{v\in V_\sigma(H)\\d_v=d}}
       (d)_{12}\,\overline h_{12}(H,v)/Z(H)}
 {\sum_H\sum_{\substack{v\in V_\sigma(H)\\d_v=d}}(d)_{12}},
 \qquad
 \overline h_{12}(H,v)=\mathbb E[h_\gamma\mid H,v].        \tag{1.4}
\]

## 2. Exact evaluation formula

For an alive row $F$, put

\[
 C_F=|\Gamma(F)|,\qquad
 \mathfrak E(F)=\sum_{G\in E(H)}(|F\cap G|-1)_+.
\]

For an external alive row $G\not\ni v$, let

\[
 a_G(v)=|\{F\in E(H):v\in F,\ F\cap G\ne\varnothing\}|.
\]

Double counting incidences gives

\[
 E_v=\frac1{d_v}\sum_{F\ni v}(C_F-d_v)
 =\frac1{d_v}\sum_{F\ni v}
   \left(\sum_{u\in F-\{v\}}d_u-\mathfrak E(F)\right).      \tag{2.1}
\]

For a uniform ordered twelve-carrier, the expected repeated external-row
count is exactly

\[
 \overline D_{12}(v)=\sum_{G\not\ni v}
 \left\{\frac{12a_G(v)}{d_v}-1
       +\frac{(d_v-a_G(v))_{12}}{(d_v)_{12}}\right\}.        \tag{2.2}
\]

Indeed the number of sampled carrier rows meeting $G$ is
hypergeometric, and the summand is
$\mathbb E(X_G-1)_+$.  Inclusion--exclusion at multiplicity one now gives

\[
 \boxed{\overline h_{12}(H,v)=d_v+12E_v-\overline D_{12}(v).} \tag{2.3}
\]

Equations (1.1)--(2.3) are an exact finite integer/rational enumeration;
there is no floating-point premise.

## 3. Rational sign certificates

Collecting (1.4) over the three orbits in (1.2) gives, on the middle shore,

\[
 \zeta_M(336)=
 \frac{13024872042392062116997}{13024872409786236344800},    \tag{3.1}
\]

\[
 \zeta_M(360)=
 \frac{2235525687519522070871431}
      {2235525879076321557398400},                           \tag{3.2}
\]

and hence

\[
 \boxed{
 \zeta_M(360)-\zeta_M(336)=
 -\frac{38638925298524583531313366083931}
 {672209791849300553006766641478067259520}<0.}              \tag{3.3}
\]

The middle degree support around these values is
$328,336,360$, so the inversion is adjacent.

On the lower shore,

\[
 \zeta_L(904)=
 \frac{37273593396730211644099971989}
      {37273593401732694120225886320},                      \tag{3.4}
\]

\[
 \zeta_L(912)=
 \frac{10926671071114905752116222985}
      {10926671079616552405470566332},                      \tag{3.5}
\]

and therefore

\[
 \boxed{
 \zeta_L(912)-\zeta_L(904)=
 -\frac{30176433336994070403791779508755991}
 {46868446855715370703686778399001856387448080}<0.}         \tag{3.6}
\]

The lower support around these values is $872,904,912$, so this inversion
is adjacent as well.  All denominators in (3.1)--(3.6) are positive.

For an additional direct integer certificate, if $W_d$ is the Palm mass
at degree $d$ and $S_d=W_d\zeta(d)$, the signs are the signs of
$S_{d_2}W_{d_1}-S_{d_1}W_{d_2}$.  Exact collection gives

\[
\begin{array}{c|r}
(\sigma,d_1,d_2)&
\operatorname{num}(S_{d_2}W_{d_1}-S_{d_1}W_{d_2})\\ \hline
(M,336,360)&
-1151830901063780635855141761027459967840634481696768000000000\\
(L,904,912)&
-14518829694116247471009902730923170977194708769871887961423872000000.
\end{array}                                                  \tag{3.7}
\]

The corresponding positive Palm masses are

\[
\begin{array}{c|r}
(M,336)&712890041266595683494959155200000\\
(M,360)&1653472789066048199284914278400000\\
(L,904)&348777979926295319417557795425730560000\\
(L,912)&64653971485888926919287794438009856000.
\end{array}                                                  \tag{3.8}
\]

This proves (0.2).

## 4. What remains open

The obstruction rules out replacing Gate A by a theorem asserting that
the entire degree-conditioned normalized-hazard profile is nondecreasing.
It does not rule out any of the following narrower possibilities:

1. the covariance with the one specific normalized $m=12$ tail test is
   favorable or sufficiently small;
2. the signed (U/Q) cancellation controls that covariance even though
   individual adjacent degree increments have the wrong sign;
3. adverse local increments have asymptotically negligible
   tail-mass-relative boundary-polymer weight for
   $x\ge r^{-\alpha}$.

Thus the exact remaining reference theorem is still a tail-decorated
signed covariance estimate, not an all-test stochastic-order theorem.
