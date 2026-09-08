# Critical full-top promotion rings: fixed-census heat and the floor-energy obstruction

Date: 2026-07-26

Method: pure mathematics only.  The promotion-ring and critical-height
identities are taken from `TOP_FIBRE_PROMOTION_PACKET_REDUCTION_20260725.md`
and the literal tagged ring formula from
`MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md`.
No crossed recursion or computational input is used.

## 0. Verdict

Let

\[
 W=\binom{2m}m,\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.                                  \tag{0.1}
\]

Use the covering-side critical height: \(H\) is the greatest integer for
which

\[
                         \lambda_H\le M:=m+H.                \tag{0.2}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},qquad
 L:=MN_H=W+O(WH/m)=W+o(W).                                  \tag{0.3}
\]

Choose one full promotion ring with \(M\) phase slots over every rank-
\(M\) top.  Give the slots the exact SCD tag census

\[
 g_d=N_d-N_{d+1}\quad(0\le d<H),qquad g_H=N_H,              \tag{0.4}
\]

and \(L-W=o(W)\) vacant tags.  At either signed rank \(m\pm q\), exactly

\[
                         \sum_{d\ge q}g_d=N_q                \tag{0.5}
\]

slots are active.  Thus every rank has total load equal to its number of
targets and its exact floor baseline is one.

Physical legality requires exactly one tag-\(H\) anchor in every ring.
Pin one such anchor slot per ring and put

\[
                         R=L-N_H.                            \tag{0.6a}
\]

There is a completely explicit legal heat operator: exchange the remaining
lower tags and vacancies on a uniformly random pair of these \(R\) slots.
Its stationary law is the uniform anchored fixed-census law, and its exact
nonconstant spectral gap is

\[
                         \boxed{\gamma_{\rm anc}={2\over R-1}},           \tag{0.6}
\]

and every centered *linear* target load contracts by the exact factor

\[
                         1-{2\over R-1}.                       \tag{0.7}
\]

If one temporarily ignores the one-anchor-per-ring law and exchanges all
\(L\) tags, the corresponding relaxation has gap \(2/(L-1)\).

This heat converges to the wrong integral baseline.  For the unrestricted
relaxation, if \(d_{q,T}\) is the number of raw ring slots whose rank-
\((m\pm q)\) mask is \(T\), then at stationarity

\[
 \boxed{
 \mathbb E Z_{q,T}={N_q\over L}d_{q,T},qquad
 \mathbb E Q_q
 ={N_q(N_q-1)\over L(L-1)}
       \sum_Td_{q,T}(d_{q,T}-1),}                           \tag{0.8}
\]

where

\[
 Q_q=\sum_T(Z_{q,T}-1)(Z_{q,T}-2)
     =\sum_T(Z_{q,T}-1)^2                                  \tag{0.9}
\]

uses \(\sum_TZ_{q,T}=N_q\).  Formula (0.8) includes the floor correction
exactly; it is not a raw Gram estimate.

For the legal anchored heat, let \(a_{q,T}\) and \(b_{q,T}\) be the raw
anchor and nonanchor slot degrees, and put \(S_q=N_q-N_H\).  Its exact
stationary energy is

\[
 \boxed{
 \mathbb E Q_q=
 \sum_Ta_{q,T}(a_{q,T}-1)
 +{2S_q\over R}\sum_Ta_{q,T}b_{q,T}
 +{S_q(S_q-1)\over R(R-1)}
       \sum_Tb_{q,T}(b_{q,T}-1).}                       \tag{0.8a}
\]

The last term alone has the same \(\Omega(W)\) mesoscopic lower bound as
(0.11), because \(N_H=o(W)\).

Even an optimally balanced raw slot census has linear stationary energy.
For any fixed

\[
                         0<a<b<\sqrt{\log2},                  \tag{0.10}
\]

uniformly for \(a\sqrt m\le q\le b\sqrt m\),

\[
 \boxed{\inf_{(d_{q,T})}\mathbb E Q_q\ge c_{a,b}W}           \tag{0.11}
\]

for a constant \(c_{a,b}>0\).  Consequently

\[
 \boxed{
 \sum_{a\sqrt m\le q\le b\sqrt m}
       \bigl(\mathbb E Q_q^-+\mathbb E Q_q^+\bigr)
 =\Omega_{a,b}(W\sqrt m).}                                  \tag{0.12}
\]

Thus fixed-census transposition heat cannot yield floor-correct collision
energy \(o(W)\).  Its spectral contraction smooths the fractional mean,
while its equilibrium rounding noise restores a linear amount at each
mesoscopic rank.

The monotone tag placement which supplies the required long-tail ledger does
**not** by itself restrict cyclic-order heat: its one-top kernel depends only
on the number of high tags, not on their order.  Thus it is fully compatible
with the negative equilibrium calculation above.  A stronger restriction
sometimes imposed on a *move catalogue* is that every move preserve one
prescribed nonempty proper physical tail \(F\).  Under that additional
hypothesis the target harmonic

\[
                         T\longmapsto |T\cap F|               \tag{0.13}
\]

is fixed, so the full target operator has gap zero.  If only adjacent
swaps in a reserve path of length \(s=m-H\) are allowed, the conditional
per-ring linear gap is only

\[
 {2-2\cos(\pi/s)\over s-1}=\Theta(s^{-3}),                   \tag{0.14}
\]

and without conditioning the per-ring tag counts the chain is
disconnected.

There is also an exact path-fragmentation warning.  Write \(V=L-W\) for
the vacancy count.  With one pinned occupied anchor in every ring, uniform
anchored fixed-census heat has expected number of nonempty promotion pieces

\[
 \boxed{
 {N_HV\over R}
 +{(L-2N_H)V(R-V)\over R(R-1)}
 +N_H{\binom{R-M+1}{V}\over\binom RV}.}                     \tag{0.15}
\]

The first two terms count vacant-to-occupied ring boundaries; the last
counts completely occupied rings, each of which must be cut once.
Thus unstructured vacancy heat has \(\Theta(V+N_H)\) resets in its natural
range.  Critical tuning proves only \(V=O(WH/m)=o(W)\), whereas the path
ledger needs \(o(W/H)\).  Clustering vacancies into one interval per ring
restores \(O(N_H)=O(W/m)=o(W/H)\) paths.  Complete tag transpositions do not
preserve that clustered state space.  The natural per-ring or fixed-tail
restrictions which do preserve it have the invariant sectors discussed
below; a more global interval-transport heat is not ruled out by this
observation.

This is a heat-method obstruction, not a nonexistence theorem for the
promotion-ring selection.  An exceptional, strongly correlated fixed-
census assignment could still have \(Q=o(W)\); spectral convergence to the
uniform census neither constructs nor rules out such an assignment.

## 1. Exact critical census

The ratio recurrence

\[
 {\lambda_{q+1}\over\lambda_q}={m+q+1\over m-q}              \tag{1.1}
\]

and maximality in (0.2) give

\[
 1\le {M\over\lambda_H}
 <{M\over m-H}=1+O(H/m).                                    \tag{1.2}
\]

Together with

\[
 \log\lambda_q={q(q+1)\over m}
          +O(q^3/m^2+q/m),                                  \tag{1.3}
\]

this proves (0.3).

There are \(N_H\) full tops and \(M\) phase slots in each promotion
ring, hence \(L=MN_H\).  The tag counts (0.4) telescope:

\[
 \sum_{d=0}^Hg_d=N_0=W,
 \qquad
 \sum_{d=q}^Hg_d=N_q.                                      \tag{1.4}
\]

Since \(L\ge W\), the remaining \(L-W\) slots receive a vacancy symbol
\(\varnothing\), which reaches no rank.  This creates an exact finite
fixed-census state space.  Using instead the least \(H\) with
\(\lambda_H\ge M\) gives \(L\le W\) and an unavoidable \(W-L=o(W)\)
chain leave; all formulae below apply after adjoining that many formal
vacant physical slots.  The covering-side convention avoids this
notational defect.

## 2. Raw ring maps and the fixed-census state space

For every top \(U\), fix a cyclic order

\[
                         c^U_0,\ldots,c^U_{M-1}.               \tag{2.1}
\]

Let \(\mathcal S\) be the disjoint union of their \(M\) phase slots, so
\(|\mathcal S|=L\).  The full promotion-ring theorem assigns, to every
slot \(s=(U,i)\) and signed offset \(r\in[-H,H]\), the raw mask

\[
 \phi_r(s)=U\setminus
 \{c^U_{i+H+r},c^U_{i+H+r+1},\ldots,c^U_{i+2H-1}\}.          \tag{2.2}
\]

The omitted cyclic interval has length \(H-r\).  A tag \(d\) activates
this mask exactly when \(d\ge|r|\).

Let \(\Omega_{\mathbf g}\) be the **relaxed** set of all assignments of
the multiset of tags in (0.4), together with the vacancies, to
\(\mathcal S\).  For
\(\eta\in\Omega_{\mathbf g}\), put

\[
 X_s^{(q)}(\eta)={\bf1}_{\{\eta(s)\ge q\}},
 \qquad
 Z_{r,T}(\eta)=
 \sum_{s:\phi_r(s)=T}X_s^{(|r|)}(\eta).                    \tag{2.3}
\]

Equation (1.4) gives

\[
                         \sum_TZ_{r,T}=N_{|r|}.                \tag{2.4}
\]

Define the raw slot degree

\[
 d_{r,T}=|\{s\in\mathcal S:\phi_r(s)=T\}|,
 \qquad
                         \sum_Td_{r,T}=L.                     \tag{2.5}
\]

The geometry of the chosen promotion rings enters the tag heat only
through this degree sequence and its higher collision relations.

For the physical anchored space, choose one distinguished slot in every
ring and place its unique tag \(H\) there.  Let \(\mathcal A\) be this
\(N_H\)-set of anchor slots and \(\mathcal R=\mathcal S\setminus\mathcal A\),
so \(|\mathcal R|=R=L-N_H\).  Assign the lower tags
\(0,\ldots,H-1\) and the vacancies arbitrarily to \(\mathcal R\) with
their fixed counts.  At threshold \(q<H\), exactly

\[
                         S_q=N_q-N_H                            \tag{2.6}
\]

nonanchor slots are active.  Define

\[
 a_{r,T}=|\{s\in\mathcal A:\phi_r(s)=T\}|,
 \qquad
 b_{r,T}=|\{s\in\mathcal R:\phi_r(s)=T\}|.                  \tag{2.7}
\]

Then \(\sum_Ta_{r,T}=N_H\), \(\sum_Tb_{r,T}=R\), and
\(d_{r,T}=a_{r,T}+b_{r,T}\).

## 3. Stationary mean and exact floor energy

At a fixed threshold \(q\), a uniform element of
\(\Omega_{\mathbf g}\) makes the active set

\[
                         \{s:\eta(s)\ge q\}                   \tag{3.1}
\]

a uniform \(N_q\)-subset of the \(L\) slots.  Therefore, for every target,

\[
 \mathbb E_\pi Z_{r,T}={N_q\over L}d_{r,T}.                   \tag{3.2}
\]

This stationary mean is identically one if and only if

\[
                         d_{r,T}={L\over N_q}\quad\text{for all }T.       \tag{3.3}
\]

For a fixed integral ring selection, tag heat does not repair failure of
(3.3); it merely multiplies the raw slot profile by \(N_q/L\).  Averaging
the ring geometry over the full coordinate group makes (3.2) constant by
transitivity, but that is a further fractional average.

Since the total in (2.4) equals the number of targets, the three forms

\[
\begin{aligned}
 Q_r
 &=\sum_T(Z_{r,T}-1)(Z_{r,T}-2)\\
 &=\sum_T(Z_{r,T}-1)^2\\
 &=\sum_TZ_{r,T}(Z_{r,T}-1)
\end{aligned}                                                \tag{3.4}
\]

are equal.  The first is the exact floor/ceiling energy with floor one;
the last counts ordered collisions.

Two distinct slots are simultaneously active with probability

\[
                         {(N_q)_2\over(L)_2}.                  \tag{3.5}
\]

There are \(d_{r,T}(d_{r,T}-1)\) ordered raw slot pairs mapping to one
target \(T\).  Summing (3.5) proves the second formula in (0.8).

Equivalently, the hypergeometric variance identity gives

\[
\begin{aligned}
 \mathbb E_\pi Q_r
 ={}&\sum_T\left({N_q\over L}d_{r,T}-1\right)^2\\
 &+{N_q(L-N_q)\over L^2(L-1)}
       \sum_Td_{r,T}(L-d_{r,T}).                         \tag{3.6}
\end{aligned}
\]

The first line is the stationary-mean bias; the second is the integral
fixed-census variance.  Both are nonnegative.

For the anchored law, the active nonanchor set is a uniform
\(S_q\)-subset of \(\mathcal R\).  Expanding the ordered-collision form in
(3.4) into anchor--anchor, anchor--nonanchor, and nonanchor--nonanchor
pairs gives exactly

\[
\begin{aligned}
 \mathbb E_{\pi_{\rm anc}}Q_r
={}&\sum_Ta_{r,T}(a_{r,T}-1)
 +{2S_q\over R}\sum_Ta_{r,T}b_{r,T}\\
 &+{S_q(S_q-1)\over R(R-1)}
       \sum_Tb_{r,T}(b_{r,T}-1),                         \tag{3.7}
\end{aligned}
\]

which proves (0.8a).  This is the exact legal stationary energy.

## 4. Uniform linear lower bound at mesoscopic ranks

Fix constants as in (0.10), and let \(q=x\sqrt m+O(1)\) with
\(x\in[a,b]\).  Uniformly in that interval,

\[
 {N_q\over W}=e^{-x^2+o(1)},qquad {L\over W}=1+o(1).          \tag{4.1}
\]

Thus, for some \(\delta_{a,b}>0\),

\[
                         1+\delta_{a,b}\le {L\over N_q}
 \le2-\delta_{a,b}.                                          \tag{4.2}
\]

Among nonnegative integer sequences \((d_T)_{T\in\mathcal T_r}\) with
\(\sum_Td_T=L\), the convex sum

\[
                         \sum_Td_T(d_T-1)                     \tag{4.3}
\]

is minimized when every \(d_T\) is one or two.  Exactly \(L-N_q\)
targets then have degree two, and the minimum is

\[
                         2(L-N_q).                             \tag{4.4}
\]

Substitution in (0.8) gives

\[
 \mathbb E_\pi Q_r
 \ge {N_q(N_q-1)\over L(L-1)}\,2(L-N_q)
 =\left[2e^{-2x^2}(1-e^{-x^2})+o(1)\right]W.                 \tag{4.5}
\]

The bracket is uniformly positive on \([a,b]\), proving (0.11).  There
are \((b-a+o(1))\sqrt m\) integer depths in this interval, and the two
signs have the same estimate.  This proves (0.12).

The anchored physical space has the same lower bound.  Indeed
\(N_H=(1+o(1))W/m=o(W)\), so throughout the same interval

\[
 R-N_q=L-N_H-N_q=\Theta_{a,b}(W),qquad
 {S_q\over R}={N_q-N_H\over L-N_H}=\Theta_{a,b}(1).           \tag{4.5a}
\]

Also \(1+\delta'\le R/N_q\le2-\delta'\).  Convexity gives

\[
 \sum_Tb_{r,T}(b_{r,T}-1)\ge2(R-N_q),                         \tag{4.5b}
\]

and the last, nonnegative term of (3.7) is therefore
\(\Omega_{a,b}(W)\).  Pinning one top anchor per ring repairs physical
legality but does not change the mesoscopic equilibrium obstruction.

The conclusion is stronger than failure of independent topwise ring
selection.  It allows an optimally flat raw degree sequence before the tag
heat begins.  The equilibrium collision noise from the fixed census alone
is still linear.

### 4.1 Heat on the cyclic orders with the tags fixed

There is a second natural interpretation of promotion-ring heat: keep the
tag at each phase position fixed and randomize the cyclic order of the
labels in every top.  It has the same obstruction, with an even simpler
formula.

For a top \(U\), let

\[
 k_{U,q}=|\{i:d_{U,i}\ge q\}|                              \tag{4.6}
\]

be its number of positions active at threshold \(q\).  Fix a signed offset
\(r\), put \(q=|r|\), and let

\[
                         \ell=H-r.                            \tag{4.7}
\]

For \(0<\ell<M\), a uniform cyclic order makes the omitted
\(\ell\)-interval at a fixed phase a uniform \(\ell\)-subset of \(U\).
A proper subset occurs at at most one phase in a given order.  Therefore a
target \(T\subset U\) of rank \(m+r=M-\ell\) is hit from top \(U\) with
probability

\[
                         {k_{U,q}\over\binom M\ell}.           \tag{4.8}
\]

Independent uniform order heat over the tops consequently has stationary
mean

\[
 \boxed{
 \overline Z_{r,T}
 ={1\over\binom M\ell}
   \sum_{\substack{U\supset T\\|U|=M}}k_{U,q}.}              \tag{4.9}
\]

Thus even its linear stationary mean is uniform only if the cumulative tag
census is balanced over all tops containing each target.

Contributions from distinct tops are independent Bernoulli variables.
Since one top supplies \(k_{U,q}\) distinct targets, its summed Bernoulli
variance is

\[
                         k_{U,q}\left(1-{k_{U,q}\over\binom M\ell}\right).
                                                                    \tag{4.10}
\]

If the global fixed census gives \(\sum_Uk_{U,q}=N_q\), the exact
stationary floor energy is therefore

\[
 \boxed{
 \mathbb E Q_r
 =\sum_T(\overline Z_{r,T}-1)^2
  +N_q-{1\over\binom M\ell}\sum_Uk_{U,q}^2.}                 \tag{4.11}
\]

For \(q=x\sqrt m\), \(x\in[a,b]\), both signed values
\(\ell=H\mp q\) tend to infinity and

\[
                         \binom M\ell/M^2\longrightarrow\infty.          \tag{4.12}
\]

Since \(k_{U,q}\le M\), (4.11) gives

\[
                         \mathbb E Q_r\ge(1-o(1))N_q=\Theta_{a,b}(W).
                                                                    \tag{4.13}
\]

Thus uniform cyclic-order heat with a fixed tag census also has
\(\Omega(W\sqrt m)\) aggregate stationary energy.  It is not rescued by
choosing the per-top tag counts adversarially.

In fact the diagonal variance has an exact census-independent leading
term.  Summing (4.11) over the physical signed ranks \(-H\le r\le H\),
put

\[
 \mathcal R_Q=
 \sum_{r=-H}^{H}\left[
 N_{|r|}-{1\over\binom M{H-r}}
             \sum_U k_{U,|r|}^{\,2}\right],               \tag{4.14}
\]

with the evident literal interpretation at the two endpoint cells.  Then

\[
                         \boxed{
 \mathcal R_Q=(\sqrt\pi+o(1))W\sqrt m.}                    \tag{4.15}
\]

Indeed, the local central estimate in (4.1), followed by a Riemann sum and
the Gaussian tail bound, gives

\[
 W+2\sum_{q=1}^{H}N_q=(\sqrt\pi+o(1))W\sqrt m.             \tag{4.16}
\]

For the subtracted term, fix \(K>0\).  Uniformly for
\(|r|\le K\sqrt m\), both relevant interval lengths are
\(H+O_K(\sqrt m)\), and
\(\binom M{H-r}/M\to\infty\).  Since
\(\sum_U k_{U,q}=N_q\) and \(k_{U,q}\le M\), its total on this central
window is \(o_K(W\sqrt m)\).  Outside the window it is bounded by the
unsubtracted mass

\[
 2\sum_{q>K\sqrt m}N_q
 \le\left(2\int_K^\infty e^{-x^2}\,dx+o(1)\right)W\sqrt m.
\]

First let \(m\to\infty\), then \(K\to\infty\), proving (4.15).  Thus no
choice of the fixed per-top tag histograms changes the leading product-heat
noise.  The unordered collision normalization is one half of (4.15).

## 5. Dirichlet form and exact spectral contraction

Let

\[
 (Pf)(\eta)={1\over\binom L2}
       \sum_{\{s,t\}\in\binom{\mathcal S}2}f(\eta^{st}),      \tag{5.1}
\]

where \(\eta^{st}\) exchanges the two tags.  Exchanges of equal tags are
self-loops.  The operator is reversible for the uniform law \(\pi\), and
its Dirichlet form is

\[
 \mathcal E(f,f)
 ={1\over2\binom L2}\mathbb E_\pi
       \sum_{s<t}\bigl(f(\eta^{st})-f(\eta)\bigr)^2.          \tag{5.2}
\]

### Theorem 5.1 (relaxed fixed-census spectrum)

If at least two tag symbols occur, then

\[
 \operatorname {Var}_\pi f
 \le {L-1\over2}\mathcal E(f,f),                             \tag{5.3}
\]

and the constant is sharp.  Equivalently, the exact relaxed gap is
\(2/(L-1)\).

#### Proof

The state space is one orbit of the coordinate-permutation action of
\(S_L\).  The transposition average in (5.1) is central.  On an irreducible
Specht module \(S^\lambda\), its eigenvalue is the transposition character
ratio.  Every nontrivial constituent is dominated by the standard module
\(S^{(L-1,1)}\), on which the eigenvalue is

\[
                         1-{L\over\binom L2}=1-{2\over L-1}.  \tag{5.4}
\]

The standard module occurs because two tag symbols occur: the centered
coordinate indicators are nonzero.  This proves both the inequality and
sharpness.  Alternatively, restricting to any threshold set in (3.1)
gives the Johnson eigenvalues

\[
 1-{j(L-j+1)\over\binom L2},
 \qquad0\le j\le\min(N_q,L-N_q),                              \tag{5.5}
\]

whose first nonconstant value is (5.4). \(\square\)

Every \(Z_{r,T}\) is linear in the threshold indicators.  Hence its
centered part lies entirely in the standard module and one has the exact
identity

\[
 P^t\left(Z_{r,T}-{N_q\over L}d_{r,T}\right)
 =\left(1-{2\over L-1}\right)^t
  \left(Z_{r,T}-{N_q\over L}d_{r,T}\right).                  \tag{5.6}
\]

The floor energy is quadratic.  On the threshold slice it has harmonic
degrees at most two, so

\[
 P^tQ_r=\mathbb E_\pi Q_r
       +\lambda_1^tQ_{r,1}+\lambda_2^tQ_{r,2},                \tag{5.7}
\]

where

\[
 \lambda_1=1-{2\over L-1},qquad
 \lambda_2=1-{2(L-1)\over\binom L2}=1-{4\over L}.            \tag{5.8}
\]

If the raw degrees \(d_{r,T}\) are constant, the collision graph on slots
is regular, the degree-one component \(Q_{r,1}\) vanishes, and (5.7)
converges at the faster degree-two rate.  In every case the limit is the
positive quantity (0.8), not zero.

For the legal anchored heat, replace \(\mathcal S,L,N_q\) in
(5.1)--(5.6) by the nonanchor slot set \(\mathcal R\), its size \(R\),
and the active lower-tag count \(S_q=N_q-N_H\).  The identical proof gives

\[
 \operatorname {gap}(P_{\rm anc})={2\over R-1},              \tag{5.8a}
\]

and, with \(Z'_{r,T}=Z_{r,T}-a_{r,T}\),

\[
 P_{\rm anc}^t\left(Z'_{r,T}-{S_q\over R}b_{r,T}\right)
 =\left(1-{2\over R-1}\right)^t
  \left(Z'_{r,T}-{S_q\over R}b_{r,T}\right).                \tag{5.8b}
\]

Its quadratic limit is (3.7), which is already
\(\Omega(W)\) on the mesoscopic window.

### Corollary 5.2 (no floor-energy contraction to zero)

For either the relaxed or anchored reversible heat, there is no uniform
inequality of the form

\[
                         P Q_r\le(1-\kappa_m)Q_r+e_mW         \tag{5.8c}
\]

on a mesoscopic rank with \(e_m=o(\kappa_m)\).  Indeed, average (5.8c)
under stationarity.  Equations (4.5) and (4.5a) give
\(\mathbb E_\pi Q_r\ge cW\), so stationarity would imply

\[
                         \kappa_mcW\le e_mW,                  \tag{5.8d}
\]

a contradiction.  For the sum over the Gaussian window, the unavoidable
stationary additive term is \(\Omega(\kappa_mW\sqrt m)\).

Thus the Dirichlet gap is a contraction toward the positive equilibrium,
not a Lyapunov inequality toward floor balance.

### Corollary 5.3 (sparse swap catalogues do not change the floor)

Let \(G\) be any undirected graph on the \(R\) legal nonanchor slots, and
at each step choose an edge of \(G\) with a positive symmetric weight and
transpose the two endpoint tags.  If \(G\) is connected, its edge
transpositions generate \(S_R\): along a path, conjugating adjacent edge
transpositions produces the transposition of either endpoint with the
initial vertex, and these star transpositions generate every permutation.
Hence the chain is irreducible on the anchored fixed-census orbit.  Its
unique reversible stationary law is the uniform law
\(\pi_{\rm anc}\), independently of the edge weights.

Consequently every connected sparse catalogue has exactly the same
stationary floor (3.7), in particular

\[
 \sum_{a\sqrt m\le |r|\le b\sqrt m}
       \mathbb E_{\pi_{\rm anc}}Q_r=\Omega_{a,b}(W\sqrt m).
                                                               \tag{5.8e}
\]

If \(G\) is disconnected, the count of each tag symbol in every connected
component is invariant, so the full fixed-census chain has spectral gap
zero.  Thus sparsifying the tag-swap catalogue gives a sharp dichotomy:
disconnecting it creates exact conserved modes, while keeping it connected
retains the same fatal floor.  No lower bound on its mixing rate is needed
for this conclusion.

For **rooted, fixed-phase** cyclic-order heat on one top, averaging all
transpositions of its \(M\) positions has the analogous gap
\(2/(M-1)\).  (The fixed phase is already present when the tag pattern is
held at named positions.)  If only adjacent
position swaps around the cyclic order are used, then on the linear label
module

\[
 I-P_{\rm adj}={L_{C_M}\over M},                             \tag{5.9}
\]

so its exact linear gap is

\[
 {2-2\cos(2\pi/M)\over M}=\Theta(M^{-3}).                    \tag{5.10}
\]

If a global step first chooses one of the \(N_H\) tops uniformly, this
gap is divided by \(N_H\).  Parallel topwise updates avoid that additional
factor but still converge to the positive equilibrium (4.11).  Thus the
choice of full versus adjacent order heat affects only mixing time, not the
floor-energy obstruction.

## 6. Forced-tail-compatible restrictions

For a graph \(G\) on the slot set, let

\[
                         P_G={1\over|E(G)|}
             \sum_{st\in E(G)}\tau_{st}.                     \tag{6.1}
\]

On centered linear coordinate functions,

\[
                         I-P_G={L_G\over|E(G)|},               \tag{6.2}
\]

where \(L_G\) is the ordinary graph Laplacian.  Therefore the full heat
gap is at most

\[
                         {\lambda_2(L_G)\over|E(G)|}.          \tag{6.3}
\]

This elementary upper bound settles the variants whose legal move graph
really does fix ring histograms or a prescribed physical tail.  It does not
apply merely because the tag word is monotone.

### 6.1 Per-ring moves

If tags may move only within their own promotion ring, \(G\) is a disjoint
union of \(N_H\) components.  Every per-ring tag histogram is invariant,
so the unconditioned fixed-census chain has gap zero.  After conditioning
all those histograms, adjacent cyclic swaps in one ring have

\[
 \lambda_2(L_{C_M})=2-2\cos(2\pi/M).                         \tag{6.4}
\]

With one ring edge chosen uniformly inside that ring, (6.3) gives gap at
most

\[
 {2-2\cos(2\pi/M)\over M}=\Theta(M^{-3}).                    \tag{6.5}
\]

If one edge is instead chosen uniformly from all \(L=MN_H\) ring edges,
the corresponding bound is

\[
 {2-2\cos(2\pi/M)\over L}=\Theta((M^2L)^{-1}).                \tag{6.6}
\]

### 6.2 A fixed long splice tail

The literal long-splice constructions preserve an ordered common block of
length \(2H\).  Write that forced tail as \(F\) and the remaining reserve
length as

\[
                         s=M-2H=m-H.                           \tag{6.7}
\]

Every compatible label move fixes \(F\) pointwise, or at least setwise.
Consequently, on every nontrivial target rank, the centered function

\[
 T\longmapsto |T\cap F|-
 {|T||F|\over2m}                                             \tag{6.8}
\]

is a nonzero invariant target harmonic.  The full target spectral gap is
therefore exactly zero.  Its stationary mean is only sectorwise constant
on the orbits classified by the forced-tail intersection data.

If adjacent swaps are allowed only along the reserve path, then

\[
 \lambda_2(L_{P_s})=2-2\cos(\pi/s),                           \tag{6.9}
\]

and the conditional per-ring linear gap is at most

\[
 {2-2\cos(\pi/s)\over s-1}=\Theta(s^{-3}),                   \tag{6.10}
\]

which is (0.14).  Full transpositions inside the reserve improve this
conditional mixing rate, but they still fix (6.8) and cannot mix the tail
sectors.

Thus a fixed-coordinate-tail move restriction cannot improve the
unrestricted heat argument: it introduces exact invariant sectors or slows
the already irrelevant convergence to the positive floor-energy
equilibrium.  By contrast, the valid monotone tag construction needs no
fixed coordinate tail and remains subject directly to the unrestricted
product-heat floor (4.11).

### 6.3 Vacancy scattering and the long-piece requirement

Let \(V=L-W\).  Ignore the numerical tag values and mark only whether a
nonanchor slot is vacant.  Under the uniform anchored fixed-census law the
vacancies form a uniform \(V\)-subset of the \(R=L-N_H\) nonanchor
positions.

In a ring containing at least one vacancy, every occupied promotion path
begins at a directed vacant-to-occupied boundary.  There are \(N_H\)
directed nonanchor-to-anchor edges, each contributing expected boundary
\(V/R\).  There are \(L-2N_H\) directed nonanchor-to-nonanchor edges;
each contributes

\[
 {V\over R}{R-V\over R-1}.                                  \tag{6.11}
\]

Thus the expected boundary count is

\[
 {N_HV\over R}+{(L-2N_H)V(R-V)\over R(R-1)}.                \tag{6.12}
\]

A completely occupied ring has no such boundary but is one directed cycle,
which must be cut once.  A prescribed ring is completely occupied with
probability

\[
 {\binom{R-M+1}{V}\over\binom RV},                           \tag{6.13}
\]

because its other \(M-1\) positions are nonanchors.  Adding (6.12) and
\(N_H\) times (6.13) proves (0.15).

Since \(N_H/L=O(1/m)\) and \(V=o(L)\), the boundary expression (6.12) is
\((1-o(1))V\).  Hence, if \(V\gg W/H\), it violates the required
\(o(W/H)\) component scale.  The critical-height estimate
\(V=O(WH/m)\) does not exclude this, because

\[
 {WH/m\over W/H}={H^2\over m}=(1+o(1))\log m.                \tag{6.14}
\]

Putting all vacancies assigned to a ring in one cyclic interval makes the
occupied slots of that ring one interval as well, hence at most one path.
Across all tops this costs at most

\[
 N_H=(1+o(1)){W\over m}=o(W/H)                               \tag{6.15}
\]

paths.  But arbitrary transpositions do not preserve interval-clustered
vacancies.  The elementary cluster-preserving heats obtained by per-ring
swaps or by fixing one physical tail have the invariants described in
Sections 6.1--6.2.  This proves a conflict for those natural catalogues.  It
does not rule out a global moving-block operator which transfers whole
vacancy intervals between rings while preserving exact ownership.

## 7. Exact implication boundary

The following are proved.

1. At the covering-side critical height, all full-top ring slots admit the
   exact fixed tag census with only \(o(W)\) vacancies.
2. Complete tag-transposition heat has the exact stationary mean, floor
   energy, Dirichlet form, and spectral gap in (0.6)--(0.9).
3. Its stationary floor energy is \(\Omega(W)\) at every rank in a fixed
   positive-width Gaussian window and \(\Omega(W\sqrt m)\) in aggregate.
4. This remains true even if the raw ring degree sequence was optimally
   floor-balanced before the heat began.
5. Per-ring heats and heats fixing a prescribed physical tail have
   additional exact invariant sectors and no all-target-harmonic gap.  The
   monotone tag realization itself imposes no such fixed-coordinate sector.
6. Uniform vacancy heat has the exact fragmentation mean (0.15); forcing
   long occupied pieces repairs the path count, while the elementary local
   heats preserving those pieces have invariant sectors.

### 7.1 Cross-audit of the two promotion-ring inputs

The conclusions above have the following exact relation to the two dated
reports used in the current chronology.

1. `MATH_THEOREM_TUNED_PROMOTION_RING_CAPACITY_FRACTIONAL_DESIGN_20260726.md`
   is correct within its stated scope.  Its symmetric point is a
   **full-ring annulus set-cover relaxation**: every top chooses one
   fractional frame, but it does not impose the SCD tag census (0.4).
   Consequently its uniform fractional target load is neither contradicted
   nor integrally rounded by the present theorem.  The present obstruction
   begins only after one asks a uniform reversible heat to round an exact
   fixed census.

2. `MATH_AUDIT_CRITICAL_FULL_TOP_PROMOTION_RING_HEAT_AND_TAIL_20260726.md`
   passes this independent audit.  Its monotone placement gives exactly one
   tag \(H\) per ring, clustered blanks, and
   \(e_q=N_q-N_H\) high--high edges at every threshold.  In particular the
   long forced-tail requirement is positively satisfied; it is not the
   obstruction.  Its product-order heat floor agrees with (4.11).  The only
   normalization difference is that its energy \(\Phi\) counts unordered
   collisions whereas (3.4) counts ordered collisions:

   \[
                              Q=2\Phi.                       \tag{7.1}
   \]

   Thus its
   \(\mathcal R=(\sqrt\pi/2+o(1))W\sqrt m\) is equivalent to
   an ordered-collision contribution
   \((\sqrt\pi+o(1))W\sqrt m\).  The present calculation independently
   refines that audit by giving the exact anchored tag-transposition gap,
   its stationary floor formula, and the exact vacancy-fragmentation mean.

The decisive combined implication is therefore clean: one may simultaneously
realize the exact census and all required monotone long tails, but randomizing
the cyclic frames still converges to a floor-correct energy of order
\(W\sqrt m\).  The tail theorem survives; ordinary product heat does not.

What is not proved is that every fixed-census ring assignment has large
energy.  The exact remaining positive statement is therefore an
exceptional correlated selection theorem:

> Choose the cyclic orders, the tag placement with census (0.4), and the
> long-splice-compatible tails jointly so that the aggregate floor energy
> through all ranks is \(o(W)\), while retaining pairwise mask-disjointness.

Such a state, if it exists, lies exponentially far from what uniform
fixed-census heat describes.  A proof must use deterministic
matching/absorption or monotone state-adaptive moves with a new Lyapunov
inequality; a reversible spectral-gap argument around the uniform census
cannot establish it.
