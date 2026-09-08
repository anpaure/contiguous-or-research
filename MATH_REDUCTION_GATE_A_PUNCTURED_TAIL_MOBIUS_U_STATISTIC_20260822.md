# Gate A: the punctured connected correction is a finite tail-tilted U-statistic hierarchy

**Date:** 2026-08-22  
**Status:** exact product-law reduction; the tail-relative stability estimate
for the resulting connected U-statistics remains open

## 0. Outcome

Fix one root target in the complete directed-punctured catalogue and an
ordered carrier of size \(m\).  The connected hazard correction admits an
exact Möbius decomposition

\[
 \boxed{\Xi_\gamma^\circ
   =\sum_{\substack{A\subseteq[m]\\|A|\ge2}}
       K_{|A|}^\circ(\gamma_A).}                         \tag{0.1}
\]

Every summand of \(K_s^\circ(F_1,\ldots,F_s)\) is supported on a further
catalogue row \(G\) which meets **all** \(s\) carrier rows away from the
root.  Thus the previously known off-root two-star is the first member of
an exact hierarchy of off-root \(s\)-stars.

More importantly, the remaining \(m-s\) carrier labels can be summed out
exactly.  In a product target state \(X\), let \(d=d_v(X)\) be the number
of live root rows and let \(\overline K_s(X)\) be the average of
\(K_s^\circ\) over the live ordered \(s\)-carriers.  Put

\[
 f_c(d)=(d-c)_+^m,
 \qquad
 {d\lambda_m\over d\mathbb P}={(d)_m\over\mathbb E(d)_m},
 \qquad
 {d\lambda_c\over d\mathbb P}={f_c(d)\over\mathbb Ef_c(d)}. \tag{0.2}
\]

If \(\pi\) is the survival-weighted law of an ordered \(m\)-carrier and
\(\tau_c\) is its additional tilt by
\(\varphi_c(d)=f_c(d)/(d)_m\), then

\[
 \boxed{
 \mathbb E_\pi\Xi_\gamma^\circ
   =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_m}\overline K_s,\qquad
 \mathbb E_{\tau_c}\Xi_\gamma^\circ
   =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_c}\overline K_s.} \tag{0.3}
\]

Consequently the exact adverse product-reference term at \(m=12\) is

\[
 \boxed{
 q_0\left[
  \sum_{s=2}^{12}{12\choose s}
  \left(\mathbb E_{\lambda_{12}}\overline K_s
       -\mathbb E_{\lambda_c}\overline K_s\right)
 \right]_+.}                                             \tag{0.4}
\]

There is no remaining carrier-extension or between-label normalization in
(0.4).  The live reference theorem is now precisely a tail-relative
equivalence-of-ensembles estimate for the **signed sum** in (0.4).  The
first unresolved cluster is \(s=2\): a further row joined off-root to two
carrier rows, decorated by the all-order root-degree tail tilt.  Bounding
the absolute values of the individual \(s\)-terms would discard the
cancellation in (0.4), so this note does not claim such a bound.

## 1. Product reference and punctured catalogue

Put \(b=2r+1\).  A target is a tagged subset of \([b]\), either a middle
target of size \(r\) or a lower target of size \(r-1\).  For a permutation
\(w=(w_0,\ldots,w_{b-1})\), with indices read cyclically, define

\[
 E(w)=\{(M,\{w_i,\ldots,w_{i+r-1}\}):1\le i<b\}
 \mathbin{\dot\cup}
 \{(L,\{w_i,\ldots,w_{i+r-2}\}):1\le i<b\}.       \tag{1.1}
\]

The complete directed-punctured catalogue \(\mathcal C_r\) consists of
these rows.  Retain targets independently, with probability \(y\) on the
middle shore and \(x\) on the lower shore, where \(0<x\le y\le1\).  Write

\[
 p_u=p_{\operatorname{sh}(u)},\qquad
 q_0=x^{2r}y^{2r},\qquad
 w(A)=\prod_{u\in A}p_u^{-1}.                         \tag{1.2}
\]

Every catalogue row has survival probability \(q_0\).  Fix a target
\(v\) and let \(\mathcal S_v=\{F\in\mathcal C_r:v\in F\}\).  An ordered
\(m\)-carrier is

\[
 \gamma=(F_1,\ldots,F_m)\in\mathcal S_v^{\underline m},    \tag{1.3}
\]

where the underline means that the entries are distinct.  Its survival
probability is

\[
 q_\gamma=\prod_{u\in\cup_iF_i}p_u,                       \tag{1.4}
\]

and its survival-weighted label law is

\[
 \pi_\gamma={q_\gamma\over\sum_{\gamma'}q_{\gamma'}}.     \tag{1.5}
\]

For a target-retention state \(X\), write \(F\preceq X\) when every
target of \(F\) is retained and put

\[
 d=d_v(X)=|\{F\in\mathcal S_v:F\preceq X\}|.              \tag{1.6}
\]

Then, by counting the live ordered carriers statewise,

\[
 \boxed{\sum_\gamma q_\gamma=\mathbb E(d)_m.}             \tag{1.7}
\]

All statements below are for a fixed root.  If Gate A mixes roots within
one shore, sum the numerator and denominator of every displayed root
expectation over the root label.  The identities are rootwise and survive
that averaging without a new term.

## 2. The root-reduced connected correction

For a further catalogue row \(G\), put

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 B_I(G)=\bigcup_{i\in I}B_i(G).                         \tag{2.1}
\]

Define a set function on carrier-index sets by

\[
 g_{G,\gamma}^\circ(I)=
 \begin{cases}
  p_v^{-1}\{w(B_I(G))-1\},&v\in G,\\[3pt]
  \mathbf1_{\{B_I(G)\ne\varnothing\}}w(B_I(G)),&v\notin G.
 \end{cases}                                             \tag{2.2}
\]

In both cases \(g_{G,\gamma}^\circ(\varnothing)=0\).  Define

\[
 \Xi_\gamma^\circ
 =\sum_{G\in\mathcal C_r}
 \left\{g_{G,\gamma}^\circ([m])
            -\sum_{i=1}^m g_{G,\gamma}^\circ(\{i\})\right\}. \tag{2.3}
\]

For \(v\in G\), the summand in (2.3) is

\[
 p_v^{-1}\left\{w(B_{[m]}(G))-\sum_{i=1}^m w(B_i(G))+(m-1)\right\}; \tag{2.4}
\]

for \(v\notin G\), it is

\[
 \mathbf1_{\{B_{[m]}(G)\ne\varnothing\}}w(B_{[m]}(G))
       -\sum_{i:B_i(G)\ne\varnothing}w(B_i(G)).          \tag{2.5}
\]

Thus (2.3) is exactly the connected hazard correction after the constant
root-only term has been removed.

## 3. Carrier-index Möbius expansion

For an ordered \(s\)-tuple
\(\alpha=(F_1,\ldots,F_s)\in\mathcal S_v^{\underline s}\), define

\[
 \widehat g_{G,\alpha}^\circ([s])
 =\sum_{I\subseteq[s]}(-1)^{s-|I|}g_{G,\alpha}^\circ(I),  \tag{3.1}
\]

and

\[
 \boxed{K_s^\circ(\alpha)
   =\sum_{G\in\mathcal C_r}\widehat g_{G,\alpha}^\circ([s]).} \tag{3.2}
\]

The quantity \(K_s^\circ\) is symmetric in its \(s\) arguments, even
though ordered tuples are convenient for Palm counting.

### Theorem 3.1 (exact Möbius hierarchy)

For every ordered \(m\)-carrier,

\[
 \boxed{\Xi_\gamma^\circ
   =\sum_{\substack{A\subseteq[m]\\|A|\ge2}}
       K_{|A|}^\circ(\gamma_A).}                         \tag{3.3}
\]

Moreover, a row \(G\) contributes to
\(\widehat g_{G,\alpha}^\circ([s])\) only if

\[
 \boxed{(G\cap F_i)-\{v\}\ne\varnothing
                 \quad\hbox{for every }1\le i\le s.}     \tag{3.4}
\]

#### Proof

Möbius inversion gives

\[
 g_{G,\gamma}^\circ([m])
 =\sum_{\varnothing\ne A\subseteq[m]}
       \widehat g_{G,\gamma_A}^\circ(A).                  \tag{3.5}
\]

The terms with \(|A|=1\) are precisely
\(g_{G,\gamma}^\circ(\{i\})\).  Subtract them, sum over
\(G\), and obtain (3.3).

If \(B_i(G)=\varnothing\), then for every
\(I\subseteq[s]-\{i\}\),

\[
 g_{G,\alpha}^\circ(I\cup\{i\})=g_{G,\alpha}^\circ(I).  \tag{3.6}
\]

Pair the two terms indexed by \(I\) and \(I\cup\{i\}\) in (3.1).
Their signs are opposite, so the coefficient is zero.  This proves
(3.4).  \(\square\)

### 3.2 Activity form and signs

Put \(a_u=p_u^{-1}-1\) and \(a(T)=\prod_{u\in T}a_u\).  For
\(T\subseteq B_{[s]}(G)\), define the signed cover coefficient

\[
 \eta_\alpha(T;G)=
 \sum_{\substack{I\subseteq[s]\\
        T\subseteq\cup_{i\in I}B_i(G)}}(-1)^{s-|I|}.       \tag{3.7}
\]

If \(v\in G\), then

\[
 \widehat g_{G,\alpha}^\circ([s])
 =p_v^{-1}\sum_{\varnothing\ne T\subseteq B_{[s]}(G)}
                 \eta_\alpha(T;G)a(T).                   \tag{3.8}
\]

If \(v\notin G\) and all \(B_i(G)\) are nonempty, then

\[
 \widehat g_{G,\alpha}^\circ([s])
 =(-1)^{s+1}
  +\sum_{\varnothing\ne T\subseteq B_{[s]}(G)}
                 \eta_\alpha(T;G)a(T).                   \tag{3.9}
\]

If an off-root link is absent, the whole expression is zero by (3.4).
Equations (3.8)--(3.9) exhibit both the signed duplicate constant and the
nonempty conditioning activities inside one \(s\)-star.  In particular,
separating them before the tail tilt is not sign-preserving.

### 3.3 The first kernel explicitly

For \(s=2\), abbreviate

\[
 A=(G\cap F_1)-\{v\},\qquad B=(G\cap F_2)-\{v\}.           \tag{3.10}
\]

If either \(A\) or \(B\) is empty, the coefficient is zero.  Otherwise

\[
 \widehat g_{G,(F_1,F_2)}^\circ([2])=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[3pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{3.11}
\]

Writing \(C=A\cap B\), \(A'=A-C\), and \(B'=B-C\), the root-row line is

\[
 p_v^{-1}\left\{
 w(C)(w(A')-1)(w(B')-1)-(w(C)-1)\right\},                 \tag{3.12}
\]

while the external-row line is

\[
 w(C)(w(A')-1)(w(B')-1)-w(C).                             \tag{3.13}
\]

Thus even the first kernel contains a positive exclusive-link activity
and a negative shared-link/duplicate activity.  Formulae (3.12)--(3.13)
are the smallest signed cluster which a tail-relative boundary estimate
must keep intact.

## 4. Summing out every unused carrier label

For \(2\le s\le m\), define the state statistic

\[
 Y_s(X)=\sum_{\alpha\in\mathcal S_v^{\underline s}}
       \mathbf1_{\{\alpha\preceq X\}}K_s^\circ(\alpha),   \tag{4.1}
\]

and its live-carrier U-statistic

\[
 \overline K_s(X)=
 \begin{cases}
  Y_s(X)/(d)_s,&d\ge s,\\
  0,&d<s.
 \end{cases}                                             \tag{4.2}
\]

Let \(c\ge m-1\), assume \(\mathbb Ef_c(d)>0\), and put

\[
 \varphi_c(d)=
 \begin{cases}
  f_c(d)/(d)_m,&d\ge m,\\
  0,&d<m.
 \end{cases}                                             \tag{4.3}
\]

For a labelled carrier define

\[
 P_\gamma=\mathbb E[\varphi_c(d)\mid\gamma\preceq X],
 \qquad
 {d\tau_c\over d\pi}(\gamma)
 ={P_\gamma\over\mathbb E_\pi P_\gamma}.                \tag{4.4}
\]

### Theorem 4.1 (exact label-to-state collapse)

With \(\lambda_m,\lambda_c\) as in (0.2), equations (0.3) hold.
Equivalently,

\[
 \boxed{
 \mathbb E_\pi\Xi_\gamma^\circ-
 \mathbb E_{\tau_c}\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}
   \left(\mathbb E_{\lambda_m}\overline K_s
       -\mathbb E_{\lambda_c}\overline K_s\right).}      \tag{4.5}
\]

#### Proof

Fix a state with \(d\) live root rows and a set
\(A\subseteq[m]\) of size \(s\).  Once the ordered subcarrier in the
positions \(A\) has been chosen, there are exactly
\((d-s)_{m-s}\) ways to fill the remaining carrier positions.  Therefore
(3.3) gives the statewise identity

\[
 \sum_{\gamma\preceq X}\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}(d-s)_{m-s}Y_s(X)
 =(d)_m\sum_{s=2}^m{m\choose s}\overline K_s(X).          \tag{4.6}
\]

Average (4.6) under the product law and divide by (1.7).  This proves the
first identity in (0.3).

Also

\[
 q_\gamma P_\gamma
 =\mathbb E[\mathbf1_{\{\gamma\preceq X\}}\varphi_c(d)].  \tag{4.7}
\]

Multiplying (4.6) by \(\varphi_c(d)\), averaging, and using
\((d)_m\varphi_c(d)=f_c(d)\), gives

\[
 \sum_\gamma q_\gamma P_\gamma\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}
       \mathbb E[f_c(d)\overline K_s(X)].                  \tag{4.8}
\]

The same count without \(\Xi^\circ\) gives

\[
 \sum_\gamma q_\gamma P_\gamma=\mathbb Ef_c(d).          \tag{4.9}
\]

Divide (4.8) by (4.9).  This proves the second identity in (0.3), and
subtraction proves (4.5).  \(\square\)

An arbitrary constant may be subtracted from each \(\overline K_s\) in
(4.5), because both \(\lambda_m\) and \(\lambda_c\) are probability
measures.  Thus only the nonconstant Hoeffding components matter.

## 5. Exact independent-row benchmark

The reduction identifies why a generic independent-row heuristic looks
tempting and exactly where it fails for target retention.

Suppose, only in this paragraph, that the rows of \(\mathcal S_v\) are
retained independently with a common probability.  Conditional on
\(d\), the live root star is a uniform \(d\)-subset of
\(\mathcal S_v\).  Hence, for every deterministic symmetric kernel
\(K_s\),

\[
 \mathbb E[\overline K_s\mid d]
 ={1\over(|\mathcal S_v|)_s}
   \sum_{\alpha\in\mathcal S_v^{\underline s}}K_s(\alpha), \tag{5.1}
\]

which is independent of \(d\).  It follows that the right side of (4.5)
vanishes for every degree tilt, including the exact cutoff tail.

In the punctured model the *targets*, not the rows, are independent.
Shared-target boundary polymers make the live root star a dependent random
subset.  Thus the remaining theorem is precisely a quantitative,
tail-relative version of (5.1) for the signed connected sum (4.5).

## 6. The exact remaining \(m=12\) theorem

Let \(m=12\), \(x\ge r^{-\alpha}\), and let \(c\) range over the
deterministic terminal thresholds used by the normalized Gate-A potential.
The product-reference Simpson loss is bounded once one proves a uniform
tail-relative estimate on

\[
 \mathcal R_{12,c}
 =q_0\left[
  \sum_{s=2}^{12}{12\choose s}
  \left(\mathbb E_{\lambda_{12}}\overline K_s
       -\mathbb E_{\lambda_c}\overline K_s\right)
 \right]_+.                                             \tag{6.1}
\]

The boundary-polymer input now has an exact shape:

* \(K_s^\circ\) is supported on a further row with \(s\) off-root links;
* \(\lambda_{12}\) is the ordinary factorial root Palm tilt;
* \(\lambda_c\) is the exact normalized high-tail root tilt; and
* all binomial coefficients and all signs must remain inside the sum.

The first live term is the tail-decorated two-star

\[
 q_0{12\choose2}
 \left(\mathbb E_{\lambda_{12}}\overline K_2
             -\mathbb E_{\lambda_c}\overline K_2\right). \tag{6.2}
\]

Ordinary global \(L^2\) control is not tail-relative, and a pointwise
absolute envelope for \(K_2\) discards the activity cancellation in
(3.8)--(3.9).  A closure therefore requires a tail-decorated connected
boundary-polymer or an equivalent microcanonical stability theorem.  This
note proves the exact finite hierarchy and the removal of unused carrier
labels; it does not claim (6.1) is asymptotically small, nor does it perform
the exact-slice, stopped-law, realized-center, or unequal-purge transfers.

## 7. Exact checker

The script

`scratch/verify_gate_a_punctured_tail_mobius_u_statistic_20260822.py`

constructs the complete \(r=2\) punctured catalogue and uses rational
arithmetic.  It verifies the Möbius identity, the all-off-root-link support,
the statewise extension count (4.6), and both tilted identities in (0.3)
on a finite root-star subcatalogue.  The subcatalogue is used only to keep
the exhaustive state/carrier census small; every checked identity is
universal and the kernels themselves use the complete punctured catalogue.
