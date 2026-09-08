# Gate A: exact connected-cluster form of the punctured product Simpson term

**Date:** 2026-08-22  
**Status:** unconditional product-law reduction; the tail-mass-relative
boundary-polymer estimate for the connected correction remains open

## 0. Outcome

For the complete directed-punctured catalogue under independent target
retention, the one-carrier conditional mean hazard is exactly constant.
Consequently every between-carrier Simpson contribution comes from a
genuinely connected correction involving at least two carrier rows and one
further catalogue row.

For an ordered $m$-carrier $\gamma=(v;F_1,\ldots,F_m)$, define the
signed connected statistic $\Xi_\gamma$ in (3.3) below.  If

\[
 H_\gamma=\mathbb E[h_\gamma\mid\gamma\text{ retained}],
 \qquad
 P_\gamma=\mathbb E[\psi(d_v/c)\mid\gamma\text{ retained}], \tag{0.1}
\]

where $c>0$ is deterministic and $\psi$ is increasing, then

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi(d_v/c))
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi(d_v/c)
                    \mid\gamma)
  +q_0\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma).}       \tag{0.2}
\]

The first term is nonnegative by Harris/FKG.  Thus, if
$d\tau/d\pi=P_\gamma/\mathbb E_\pi P_\gamma$,

\[
 \boxed{
 \frac{[-\operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)]_+}
      {\mathbb E_{\rm Palm}\psi}
 \le q_0[\mathbb E_\pi\Xi_\gamma
             -\mathbb E_\tau\Xi_\gamma]_+.}                \tag{0.3}
\]

This is the exact product-reference object.  A deterministic normalization
of the hazard divides both sides by that deterministic row-count scale.
The realized random row count is a separate shadow-denominator transfer.

The statistic $\Xi_\gamma$ retains the cancellation lost by separate
absolute bounds on companion exposure and carrier duplicates.  Its activity
expansion has only three kinds of terms:

1. a negative empty-set duplicate term;
2. positive target sets spanning more than one carrier row; and
3. negative target sets shared by at least two carrier rows.

The remaining theorem is a tail-mass-relative estimate for this signed
connected statistic at $m=12$, not a pointwise bound on
$|\Xi_\gamma|$.

## 1. Product reference and carrier Palm law

Let $\mathcal C_r$ be the complete directed-punctured catalogue.  Every
row has $2r$ middle and $2r$ lower targets.  Retain a target $u$
independently with probability

\[
 p_u=p_{\operatorname{sh}(u)},\qquad p_M=y,\quad p_L=x,
 \qquad 0<x\le y\le1,                                    \tag{1.1}
\]

and put

\[
                         q_0=x^{2r}y^{2r}.                  \tag{1.2}
\]

Thus every catalogue row has unconditional survival probability $q_0$.
Fix a root $v$ in one chosen shore, and let
$\gamma=(v;F_1,\ldots,F_m)$ be an ordered tuple of distinct catalogue
rows through $v$.  Write

\[
 S_\gamma=\bigcup_{i=1}^mF_i,\qquad
 m_\gamma(u)=|\{i:u\in F_i\}|.                             \tag{1.3}
\]

The carrier survival probability is

\[
 q_\gamma=\prod_{u\in S_\gamma}p_u
 =q_0^m\prod_{u\in S_\gamma}p_u^{-(m_\gamma(u)-1)}.         \tag{1.4}
\]

Hence the carrier-label Palm law is

\[
                         \pi_\gamma
 =\frac{q_\gamma}{\sum_{\gamma'}q_{\gamma'}}.              \tag{1.5}
\]

Equation (1.4) shows that its departure from the uniform label law is itself
an intersection polymer supported only on targets repeated among carrier
rows.

The formulas may instead mix all root labels in the chosen shore: regard
$(v;F_1,\ldots,F_m)$ as the carrier label and use the same survival weight
$q_\gamma$.  Every identity below is labelwise.  More importantly, the
one-body constant in (2.2) depends on the row but not on the designated
root, and is in fact the same for every row.  It therefore remains a
constant after this shore/root Palm averaging.  Gate A applies the argument
one shore at a time, so no cross-shore mixture is required.

## 2. The one-body profile is constant

For one catalogue row $F$, define

\[
 L(F)=\mathbb E[|\Gamma(F)\cap E(H)|\mid F\text{ retained}]
 =q_0\sum_{G:G\cap F\ne\varnothing}
       \prod_{u\in G\cap F}p_u^{-1}.                       \tag{2.1}
\]

The symmetric group on the $2r+1$ ground labels acts transitively on the
catalogue rows: if $F=E(w)$ and $F'=E(w')$, the coordinate permutation
sending $w_i$ to $w'_i$ maps $F$ to $F'$, preserves the two shores,
and permutes the complete catalogue.  The product probabilities in (1.1)
depend only on the shore.  Therefore

\[
                         \boxed{L(F)=L_r(x,y)}              \tag{2.2}
\]

for every catalogue row $F$.

This is exactly the one-body cancellation absent from a generic
hypergraph.  A root target may occupy different positions in the oriented
punctured path, so its conditional degree-tail profile $P_\gamma$ need
not be one-body constant.  That causes no Simpson term because the hazard
profile paired with it in (2.2) is constant.

## 3. Exact connected correction

For a further catalogue row $G$, put

\[
 A_i(G)=G\cap F_i,qquad
 J_G(\gamma)=\{i:A_i(G)\ne\varnothing\},\qquad
 U_G(\gamma)=G\cap S_\gamma=\bigcup_iA_i(G),               \tag{3.1}
\]

and write

\[
                         w(A)=\prod_{u\in A}p_u^{-1}.       \tag{3.2}
\]

Define

\[
 \boxed{
 \Xi_\gamma=\sum_{G\in\mathcal C_r}
 \left\{
  \mathbf1_{\{J_G\ne\varnothing\}}w(U_G)
  -\sum_{i\in J_G}w(A_i(G))
 \right\}.}                                                \tag{3.3}
\]

### Theorem 3.1 (exact hazard decomposition)

For every labelled carrier,

\[
                         \boxed{H_\gamma=mL_r(x,y)+q_0\Xi_\gamma.} \tag{3.4}
\]

#### Proof

Conditioning the carrier to survive fixes every target in $S_\gamma$.
Thus a further row $G$ survives conditionally with probability

\[
             q_0w(G\cap S_\gamma)=q_0w(U_G).               \tag{3.5}
\]

It belongs to the carrier hazard exactly when $J_G\ne\varnothing$.
Summing (3.5) proves

\[
 H_\gamma=q_0\sum_G
       \mathbf1_{\{J_G\ne\varnothing\}}w(U_G).             \tag{3.6}
\]

On the other hand, summing the one-carrier formula (2.1) over the $m$
carrier rows gives

\[
 mL_r(x,y)=q_0\sum_G\sum_{i\in J_G}w(A_i(G)).              \tag{3.7}
\]

Subtract (3.7) from (3.6).  This is (3.4).  $\square$

If $G$ meets zero or one carrier row, its summand in (3.3) is zero.
Consequently

\[
 \boxed{\Xi_\gamma\text{ is supported on }G
                 \text{ meeting at least two carrier rows}.} \tag{3.8}
\]

This is a literal carrier--carrier--row connectedness condition.

### 3.2 Removing the constant root-only cluster

There is a sharper form adapted to the rooted boundary polymer.  Put
$p_v=p_{\operatorname{sh}(v)}$, let $D_v$ be the complete-catalogue degree
of $v$, and define the off-root intersections

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 K_G=\{i:B_i(G)\ne\varnothing\},\qquad
 B_G=\bigcup_iB_i(G).                                     \tag{3.9}
\]

For a catalogue row $G$, set

\[
 \chi_\gamma^\circ(G)=
 \begin{cases}
 p_v^{-1}\left\{w(B_G)-\displaystyle\sum_{i=1}^mw(B_i(G))
                         +(m-1)\right\},&v\in G,\\[6pt]
 \mathbf1_{\{K_G\ne\varnothing\}}w(B_G)
       -\displaystyle\sum_{i\in K_G}w(B_i(G)),&v\notin G,
 \end{cases}                                               \tag{3.10}
\]

and

\[
                         \Xi_\gamma^\circ
 =\sum_{G\in\mathcal C_r}\chi_\gamma^\circ(G).             \tag{3.11}
\]

If $v\in G$, then every $A_i(G)=\{v\}\cup B_i(G)$ and
$U_G=\{v\}\cup B_G$.  Its summand in (3.3) is therefore

\[
 p_v^{-1}\left\{w(B_G)-\sum_{i=1}^mw(B_i(G))\right\}
 =(1-m)p_v^{-1}+\chi_\gamma^\circ(G).                       \tag{3.12}
\]

There are exactly $D_v$ such rows.  The external-row summands in (3.3)
already equal the second line of (3.10).  Hence

\[
 \boxed{\Xi_\gamma=(1-m)p_v^{-1}D_v+\Xi_\gamma^\circ.}      \tag{3.13}
\]

The first term is independent of the carrier label and disappears from
every covariance.  Moreover,

\[
 \boxed{\chi_\gamma^\circ(G)=0\quad\text{whenever }|K_G|\le1.} \tag{3.14}
\]

For $v\notin G$, this is the one-carrier cancellation already noted after
(3.7).  For $v\in G$, if no $B_i$ is nonempty then the braces in (3.10)
are $1-m+(m-1)=0$; if exactly one is nonempty, its weight cancels and the
same constants cancel.  Thus every nonconstant term has an off-root
two-star

\[
                         F_i\;-\;G\;-\;F_j,\qquad i\ne j,   \tag{3.15}
\]

whose two links are witnessed by off-root shared targets.  This is the
precise connected support to be classified by the punctured boundary
polymer.

## 4. Signed activity expansion

Put

\[
                         a_u=p_u^{-1}-1\ge0,qquad
 a(T)=\prod_{u\in T}a_u.                                  \tag{4.1}
\]

For $J_G\ne\varnothing$ and $T\subseteq U_G$, define

\[
 c_\gamma(T;G)=|\{i\in J_G:T\subseteq A_i(G)\}|.          \tag{4.2}
\]

For $T=\varnothing$, this is $|J_G|$.  Expanding
$w(A)=\prod_{u\in A}(1+a_u)=\sum_{T\subseteq A}a(T)$ in
(3.3) gives the exact identity

\[
 \boxed{
 w(U_G)-\sum_{i\in J_G}w(A_i(G))
 =\sum_{T\subseteq U_G}
          (1-c_\gamma(T;G))a(T).}                           \tag{4.3}
\]

The sign structure is now explicit.

* $T=\varnothing$ contributes $1-|J_G|<0$ when the cluster is
  nontrivial.  This is the multiplicity-one duplicate correction.
* If $T\ne\varnothing$ lies in exactly one carrier row, then
  $c_\gamma(T;G)=1$ and it cancels exactly.
* If no one carrier row contains all of $T$, then
  $c_\gamma(T;G)=0$, necessarily $|T|\ge2$, and the term is positive.
  These are cross-carrier conditioning clusters.
* If at least two carrier rows contain $T$, then the term is negative.
  These are shared-target carrier clusters.

In particular, the positive and negative pieces that appear separately as
companion exposure and duplicate load are coefficients of one connected
activity polynomial.  They should not be bounded independently.

For a root row $G\ni v$, the constant subtraction in (3.10) removes the
empty activity exactly.  With

\[
 c_\gamma^\circ(T;G)
   =|\{i:T\subseteq B_i(G)\}|\qquad
       (\varnothing\ne T\subseteq B_G),
\]

one has

\[
 \boxed{\chi_\gamma^\circ(G)
 =p_v^{-1}\sum_{\varnothing\ne T\subseteq B_G}
       (1-c_\gamma^\circ(T;G))a(T).}                        \tag{4.4}
\]

Every nonzero term in (4.4) therefore contains an off-root target
activity.  Together with (3.14), it is supported on the two-link connected
shape (3.15).

For orientation only, the cancellation-free envelope

\[
 |\Xi_\gamma|
 \le (m+1)\sum_{1\le i<j\le m}
 \sum_{\substack{G:G\cap F_i\ne\varnothing\\
                    G\cap F_j\ne\varnothing}}
          w(G\cap S_\gamma)                                \tag{4.5}
\]

follows from $w(A_i)\le w(U_G)$.  It is generally too lossy for the
coefficient-one ledger; (4.3)--(4.4), not (4.5), are the intended polymer
input.

## 5. Exact covariance reduction

Conditioned on a fixed labelled carrier, the remaining target indicators
are independent.  Both $h_\gamma$ and $\psi(d_v/c)$ are increasing, so
Harris's inequality gives

\[
 \operatorname {Cov}(h_\gamma,\psi(d_v/c)
             \mid\gamma\text{ retained})\ge0.              \tag{5.1}
\]

The law of total covariance under the Palm mixture is

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi\mid\gamma)
  +\operatorname {Cov}_\pi(H_\gamma,P_\gamma).             \tag{5.2}
\]

Substitute (3.4); the constant $mL_r(x,y)$ disappears.  This proves
(0.2).  Dividing the second covariance by
$\mathbb E_\pi P_\gamma=\mathbb E_{\rm Palm}\psi$ gives

\[
 \frac{\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma)}
      {\mathbb E_\pi P_\gamma}
 =\mathbb E_\tau\Xi_\gamma-\mathbb E_\pi\Xi_\gamma,       \tag{5.3}
\]

which proves (0.3).

By (3.13), both covariances and both expectation differences are unchanged
when $\Xi_\gamma$ is replaced by $\Xi_\gamma^\circ$.  Thus the exact
adverse term is already supported on the off-root connected shapes in
(3.14)--(3.15).

## 6. The exact remaining product-reference theorem

For $m=12$, $x\ge r^{-\alpha}$, and the relevant deterministic-center
normalized tail tests, it is enough to prove a tail-mass-relative bound on

\[
                 q_0[\mathbb E_\pi\Xi_\gamma^\circ
                         -\mathbb E_\tau\Xi_\gamma^\circ]_+.
                                                                    \tag{6.1}
\]

The complete one-row boundary polymer already controls every fixed
one-body sum in (2.1).  It does not by itself control (6.1): the carrier
law (1.4), the signed multi-carrier activity (4.3), and the tail tilt
$P_\gamma$ must be expanded together.  The all-order Newton obstruction
for the normalized tail test prevents replacement of that expansion by a
fixed list of carrier moments.

Thus (6.1) is a precise tail-decorated connected-polymer target.  This note
does not claim its asymptotic bound, its exact-slice transfer, or the later
stopped-law/realized-center/purge transfer.
