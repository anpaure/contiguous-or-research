# Edge-only child Doléans normalization: exact moving-shore generator and the boundary-covariance obstruction

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver,
probabilistic black box, or web input is used.

## 0. Outcome

Remove all singleton compensation coins.  Let only selected catalogue
edges ring.  Give every child link its exact predictable Doléans
normalizer, retain the fixed time-zero child-incidence weights, and
center only on the currently live extension shore.

The audit has a sharp positive algebraic conclusion and three
independent obstructions.

### Theorem A (exact edge-only moving-shore generator)

Fix a protected profile \(S\) and its live extension resources \(a\).
Let \(p_{S,a}\) be the fixed time-zero incidence weights.  After the
child-specific Doléans normalization, every child coordinate \(Z_{S,a}\)
has zero predictable drift until its own physical death.

For the live shore \({\cal A}_S(t)\), put

\[
 P_S(t)=\sum_{a\in{\cal A}_S(t)}p_{S,a},
\qquad
 \bar Z_S={1\over P_S}\sum_{a\in{\cal A}_S}p_{S,a}Z_{S,a},
\tag{0.1}
\]

\[
 V_S=\sum_{a\in{\cal A}_S}p_{S,a}(Z_{S,a}-\bar Z_S)^2.
\tag{0.2}
\]

For a selected edge \(g\), let \(D_g\) be the extension coordinates
physically contained in \(g\), let \(B_g\) be the surviving shore, and
put

\[
 d_g=\sum_{a\in D_g}p_{S,a},\qquad P_g=P_S-d_g.
\]

Write \(\bar Z_g\) for the mean on \(B_g\),
\(\delta_g=\bar Z_g-\bar Z_S\), and let
\({\cal D}_S(g)=V_S-V_{S;B_g}\ge0\) be the exact variance lost by
deleting \(D_g\) before changing the surviving coordinates.  On
\(B_g\), let \(h_{g,a}\) be the Doléans-normalized child-link mass
killed by \(g\), put

\[
 H_g=\sum_{a\in B_g}p_{S,a}h_{g,a},
\]

and let \(h_g^\circ=h_g-H_g/P_g\).  Then, stopped at death of \(S\),

\[
 \boxed{
 (\partial_t+{\cal L}_t)V_S
 =\sum_g\lambda_g
 \left[
  -{\cal D}_S(g)+2\delta_gH_g
  +\|h_g^\circ\|_{L^2(p_S;B_g)}^2
 \right].}
\tag{0.3}
\]

There is no coin term and no predictable linear bias on a fixed
shore.  But the mixed term \(2\delta_gH_g\) remains because deletion
changes the center before the surviving coordinates jump.  It is the
exact obstruction missed by a coordinatewise zero-drift calculation.

### Conditional PFS3 theorem

For pair parents \(S\), the edge-only construction closes PFS3 if:

1. the Doléans factors are incidence-weightedly comparable with the
   natural physical pair/triple references;
2. the live-shore mass has its expected lower bound; and
3. the augmented selected-edge diagonal satisfies

\[
 \boxed{
 Q_S^{E,+}(t):=
 \sum_g\lambda_g(t)
 \left[
  \|h_g^\circ\|_{L^2(p_S;B_g)}^2
  +{d_gH_g^2\over P_SP_g}
 \right]
 \le {L^C\over r(r-2)}}
\tag{ASE--CHD}
\]

in marked-pair incidence aggregate.

With a fixed separation between the pair and triple thresholds,
ASE--CHD gives total PFS3-stopped incidence

\[
                         O\left(
 {L^C\log(1/z)\over A_3^2}
 \right)W=o(W).
\tag{0.4}
\]

Thus an edge-only process gives a correct conditional PFS3 proof, but
the sufficient selected-edge estimate is stronger than the centered
square alone.

### Obstruction 1: the centered selected-edge bound alone is not a gate

Even if \(h_g\) is constant on the surviving shore, so that
\(\|h_g^\circ\|=0\), the mixed deletion/decrement term can make the
variance generator positive.  The exact two-child example in Section
3 has

\[
 \sum_g\lambda_g\|h_g^\circ\|^2=0,
 \qquad
 (\partial_t+{\cal L}_t)V_S=h^2/4>0.
\tag{0.5}
\]

Therefore the centered selected-edge square by itself does not close
PFS3.  One must bound the boundary covariance, retain it together with
its negative deletion energy, or change the observable.

### Obstruction 2: a selected-edge first-moment bound is insufficient

The common-resource part of the centered diagonal

\[
 Q_S^{E,\circ}
 :=\sum_g\lambda_g
       \|h_g^\circ\|_{L^2(p;B_g)}^2
\]

is a conditional fourth kernel.
On degree-flat resources its selected-edge clock coefficient is still
\(\Theta(1/r)\).  A block-design residual below satisfies the natural
one-child, pair/triple, and maximum selected-edge influence scales, but
has

\[
                         Q_S^{E,\circ}=\Theta(1/r),
\tag{0.6}
\]

a factor \(\Theta(r)\) above ASE--CHD even before adding the boundary
covariance diagonal.

Hence, even after the boundary covariance is separately controlled,
the **full centered selected-edge square** is still required:
a first-moment, maximum-jump, or one-column selected-edge bound does not
suffice.  Removing coins does not eliminate the fourth conditional
kernel.

### Obstruction 3: degree/shore completion is independent

The Doléans factors cancel drift in their own coordinates; they do not
prove that those coordinates are comparable with the physical PFS
normalization.  That comparison is exactly an integrated edge-load and
multiple-intersection condition.

Moreover, diffuse local selected-edge influence does not imply a large
matching.  A concrete Hall-cut state below has normalized nonterminal
influence \(O(1/N)\) per root but leaves a fixed positive fraction of
roots and owners unmatched.  Thus degree/shore stops need a hereditary
joint-Hall or load-coherence theorem in addition to ASE--CHD.

The edge-only replacement removes the compensation-coin algebra, but
the coefficient-one trajectory remains conditional on

\[
 \boxed{
 \text{augmented selected-edge conditional variance}
 \quad+\quad
 \text{hereditary Hall/load coherence}.}
\tag{0.7}
\]

## 1. Edge-only child coordinates

Let every active selectable edge \(g\) have predictable rate
\(\lambda_g(t)\).  When \(g\) rings it is selected, and every catalogue
row meeting \(g\) is deleted.  Selected edges are therefore disjoint.

Fix a protected \(k\)-set \(S\), and put

\[
                         R=r-k.
\tag{1.1}
\]

For a live extension resource \(a\notin S\), write \(T=Sa\).  Let

\[
                         A_T(t)=d_t(T)
\tag{1.2}
\]

be its current link degree, stopped and removed when \(a\) or \(S\)
dies.  Choose a positive predictable physical reference
\(\mu_T(t)\).  For the ordinary density reference one takes

\[
                         \mu_T(t)=d_0(T)v_t^{R-1},
\tag{1.3}
\]

where \(v_t\) is the owner/resource density used by the edge-only
trajectory.

For a current row \(f\supseteq T\), its nonterminal killing intensity is

\[
 h_{f\mid T}(t)
 =\sum_{\substack{g:g\cap T=\varnothing\\
                    g\cap(f\setminus T)\ne\varnothing}}
 \lambda_g(t).
\tag{1.4}
\]

The normalized coordinate

\[
                         X_T={A_T\over\mu_T}
\tag{1.5}
\]

has an exact predictable logarithmic drift

\[
 (\partial_t+{\cal L}_t)X_T=\beta_T(t)X_T
\tag{1.6}
\]

before terminal death, where

\[
 \beta_T
 =-{\dot\mu_T\over\mu_T}
 -{1\over A_T}
   \sum_{f\in{\cal H}_t(T)}h_{f\mid T},
\tag{1.7}
\]

with value zero when \(A_T=0\).

Define the child-specific Doléans factor and coordinate

\[
 c_T(t)=\exp\left[-\int_0^t\beta_T(s)\,ds\right],
\qquad
                         Z_T=c_TX_T.
\tag{1.8}
\]

### Lemma 1.1 (coordinatewise zero drift)

Until physical death of \(T\),

\[
                         (\partial_t+{\cal L}_t)Z_T=0.
\tag{1.9}
\]

#### Proof

Differentiate \(c_T\) and use (1.6).  Terminal death removes the
coordinate from the live shore and is handled separately. \(\square\)

This is the correct child-specific normalization.  Using one row
Doléans factor simultaneously in the parent and every child would give
an exact parent-child average, but it would include the death hazard of
the extension \(a\).  It would therefore differ from the physical
triple reference by a factor of order \(v_t^{-1}\), producing a large
artificial shore variance.  Live-shore centering avoids that error.

## 2. Fixed time-zero incidence weights and live-shore centering

Every initial row through \(S\) contains exactly \(R\) extension
resources.  Thus

\[
 \sum_a d_0(Sa)=R\,d_0(S).
\tag{2.1}
\]

Use the fixed weights

\[
                         p_{S,a}
 ={d_0(Sa)\over R\,d_0(S)},
\qquad
                         \sum_ap_{S,a}=1.
\tag{2.2}
\]

More generally, the same formulas hold for arbitrary fixed nonnegative
row-incidence weights.

Let \({\cal A}_S(t)\) be the extension resources still physically live.
Define \(P_S,\bar Z_S,V_S\) by (0.1)--(0.2).  If \(P_S=0\), terminate the
observable.

Deleting one live coordinate of weight \(p\) and value \(x\), from a
shore of total weight \(P\) and mean \(\bar x\), changes the centered
variance by

\[
 V_{\rm old}-V_{\rm new}
 ={pP\over P-p}(x-\bar x)^2\ge0.
\tag{2.3}
\]

Simultaneous deletion is obtained by iterating (2.3).  Hence every
physical extension-shore deletion is favorable.

Before applying the Doléans factors, the raw degree identity remains
pathwise exact:

\[
                         \sum_{a\in{\cal A}_S(t)}d_t(Sa)
 =R\,d_t(S).
\tag{2.4}
\]

With the references

\[
 \mu_{Sa}=d_0(Sa)v^{R-1},
\qquad
 \mu_S=d_0(S)v^R,
\tag{2.5}
\]

this gives

\[
 \sum_{a\in{\cal A}_S}p_{S,a}X_{Sa}
 =vX_S.
\tag{2.6}
\]

Equation (2.6) supplies the mean comparison needed at a triple crossing
provided \(c_{Sa}=1+o(1)\) incidence-weightedly and

\[
                         P_S(t)\ge c_0v_t
\tag{Shore}
\]

outside \(o(W)\) marked incidence.  Neither assertion follows merely
from the formal Doléans cancellation.

## 3. Exact centered variance generator

Fix a selected edge \(g\) disjoint from the protected parent \(S\).
First remove

\[
                         D_g={\cal A}_S(t)\cap g
\tag{3.1}
\]

from the extension shore.  Let \(B_g={\cal A}_S(t)\setminus D_g\), and
write

\[
 d_g=\sum_{a\in D_g}p_{S,a},\qquad
 P_g=P_S-d_g.
\tag{3.2}
\]

If \(P_g=0\), put \({\cal D}_S(g)=V_S\) and set all the remaining
event quantities below to zero.  Suppose henceforth that \(P_g>0\).
Let \(\bar Z_g\) be the weighted mean on \(B_g\), and set

\[
 \delta_g=\bar Z_g-\bar Z_S.
\tag{3.3}
\]

If \(0<d_g<P_S\), let \(\bar Z_{D_g}\) and \(V_{D_g}\) be the mean
and centered variance on the deleted shore.  Weighted ANOVA gives the
exact deletion energy

\[
\begin{aligned}
 {\cal D}_S(g)
 &: =V_S-V_{S;B_g}\\
 &=V_{D_g}
   +{P_gd_g\over P_S}
       (\bar Z_g-\bar Z_{D_g})^2\\
 &=V_{D_g}+{P_SP_g\over d_g}\delta_g^2.
\end{aligned}
\tag{3.4}
\]

When \(d_g=0\), put \({\cal D}_S(g)=\delta_g=0\).

For \(a\in B_g\), let

\[
 K_g(Sa)
 =|\{f\in{\cal H}_t(Sa):
           g\cap(f\setminus Sa)\ne\varnothing\}|
\tag{3.5}
\]

and define its Doléans-normalized decrement

\[
                         h_{g,a}
 =c_{Sa}{K_g(Sa)\over\mu_{Sa}}.
\tag{3.6}
\]

Put

\[
 H_g=\sum_{a\in B_g}p_{S,a}h_{g,a},
 \qquad h_g^\circ=h_g-{H_g\over P_g}.
\tag{3.7}
\]

For the centered vector on the post-deletion shore, polarization gives

\[
 \Delta_gV_S
 =-{\cal D}_S(g)
   -2\langle Y,h_g^\circ\rangle_{p;B_g}
   +\|h_g^\circ\|_{L^2(p;B_g)}^2.
\tag{3.8}
\]

Lemma 1.1 says more explicitly that, between jumps,

\[
 \dot Z_{Sa}
 =\sum_{g:a\in B_g}\lambda_gh_{g,a}.
\tag{3.9}
\]

Consequently the continuous contribution to \(\dot V_S\) is

\[
 2\sum_g\lambda_g
   \sum_{a\in B_g}p_{S,a}
      (Z_{Sa}-\bar Z_S)h_{g,a}.
\tag{3.10}
\]

The linear term in (3.8) is instead centered at \(\bar Z_g\).
Their difference is exactly

\[
 2(\bar Z_g-\bar Z_S)
   \sum_{a\in B_g}p_{S,a}h_{g,a}
 =2\delta_gH_g.
\tag{3.11}
\]

This term is not canceled coordinatewise.

### Theorem 3.1 (exact edge-only generator)

\[
 \boxed{
 (\partial_t+{\cal L}_t)V_S
 =\sum_{\substack{g:g\cap S=\varnothing}}
   \lambda_g
   \left[
    -{\cal D}_S(g)+2\delta_gH_g
    +\|h_g^\circ\|_{L^2(p;B_g)}^2
   \right].}
\tag{3.12}
\]

Events meeting \(S\) terminate the marked parent and are omitted.
Formula (3.12) contains only selected-edge events.  It is an equality,
not an upper bound.

Completing the square in (3.4) gives

\[
 -{\cal D}_S(g)+2\delta_gH_g
 =-V_{D_g}
  -{P_SP_g\over d_g}
    \left(\delta_g-{d_gH_g\over P_SP_g}\right)^2
  +{d_gH_g^2\over P_SP_g}.
\tag{3.13}
\]

Therefore the sharp sign-free upper bound is

\[
 (\partial_t+{\cal L}_t)V_S
 \le Q_S^{E,+}:=
 \sum_g\lambda_g
 \left[
  \|h_g^\circ\|_{L^2(p;B_g)}^2
  +{d_gH_g^2\over P_SP_g}
 \right].
\tag{3.14}
\]

The second summand is the **boundary covariance diagonal**.  By
Cauchy--Schwarz,

\[
 {d_gH_g^2\over P_SP_g}
 \le {d_g\over P_S}
      \sum_{a\in B_g}p_{S,a}h_{g,a}^2,
\tag{3.15}
\]

so an uncentered square estimate weighted by the deleted shore mass
would control it.  A centered square estimate does not.

### Proposition 3.2 (minimal boundary-covariance counterexample)

There is a two-child stopped state for which the centered
selected-edge diagonal is zero but the variance generator is positive.

#### Proof

Take two live children of weights \(p_1=p_2=1/2\), one event of rate
one, \(D_g=\{1\}\), \(B_g=\{2\}\), and surviving decrement
\(h_{g,2}=h>0\).  The Doléans finite-variation drift of child 2 is
then \(\dot Z_2=h\), while child 1 is terminal at the event.  Put
\(Z_2-Z_1=h\).  Since the surviving shore has one point,
\(h_g^\circ=0\).  On the other hand,

\[
 V_S={h^2\over4},\qquad
 \delta_g={h\over2},\qquad H_g={h\over2},
\]

and (3.12) yields

\[
 (\partial_t+{\cal L}_t)V_S
 =-{h^2\over4}+2{h\over2}{h\over2}
 ={h^2\over4}>0.
\]

Thus no inequality involving only
\(\sum_g\lambda_g\|h_g^\circ\|^2\) can upper-bound the moving-shore
variance generator. \(\square\)

## 4. Conditional PFS3 closure

Now take \(|S|=2\), so \(R=r-2\).  Use pair threshold \(A_2\) and triple
threshold \(A_3\), with the fixed corridor separation

\[
                         A_3\ge {12A_2\over c_0}.
\tag{4.1}
\]

The exact auxiliary conditions are:

\[
 \boxed{
 \left|\int_0^t\beta_{Sa}(s)\,ds\right|=o(1)}
\tag{NC}
\]

in the marked child incidence being charged,

\[
                         P_S(t)\ge c_0v_t,
\tag{4.2}
\]

and ASE--CHD, up to the stopping time.  Here the edge-clock horizon is
assumed to satisfy

\[
 \int_0^\tau dt\le C r\log(1/z),
\tag{4.3}
\]

as in the underlying edge-only trajectory, and the standard marked
pair ledger satisfies \(\sum_Sq_2(S)\le C W\).

Under NC, \(Z_{Sa}=(1+o(1))X_{Sa}\).  Equations (2.6), (4.2), and the
safe pair threshold imply

\[
                         \bar Z_S\le2A_2/c_0
\tag{4.4}
\]

after harmless corridor constants.  Thus a first triple crossing
satisfies

\[
                         |Z_{Sa}-\bar Z_S|\ge A_3/3.
\tag{4.5}
\]

At a crossing, quarantine the coordinate and charge the variance drop
using (2.3).  Formally adjoin this quarantine as a deletion event with
\(h=0\); its negative deletion energy pays the crossing.  For genuine
selected-edge events, the boundary covariance has already been
included in the upper bound (3.14).
Equivalently, stop each centered coordinate at its first crossing and
apply the stopped square identity.  From ASE--CHD,

\[
 \mathbb E\sum_{a\ {\rm crossing}}p_{S,a}
 \le {CL^C\log(1/z)\over (r-2)A_3^2}.
\tag{4.6}
\]

Finally

\[
                         q_3(Sa)
 =(r-2)q_2(S)p_{S,a}.
\tag{4.7}
\]

Multiplying (4.6) by \((r-2)q_2(S)\), and summing with the existing
marked pair-incidence weights, proves (0.4).

Thus the **augmented** selected-edge square is sufficient, but only
together with NC and the shore lower bound.  Proposition 3.2 shows that
the centered selected-edge square alone is not sufficient.

## 5. The selected-edge common-resource kernel

Expand \(K_g(Sa)^2\) over two rows in the \(Sa\)-link.  If the two rows
share an unprotected resource \(y\), every selected edge containing
\(y\) kills both.  Reversing the row-pair sum leaves the centered kernel

\[
 \boxed{
 \sum_y h_y^E(t)
 \operatorname{Var}_{p_S}
 \left(
 a\longmapsto
 c_{Sa}{d_t(Say)\over\mu_{Sa}}
 \right),}
\tag{5.1}
\]

where

\[
                         h_y^E(t)
 =\sum_{g\ni y}\lambda_g(t).
\tag{5.2}
\]

The complementary row-pair class consists of selected edges meeting
the two exclusive shores.  It is the already isolated whole-arm
selected-edge term.  Formula (5.1) is the surviving common-resource
conditional fourth kernel.

For root-stochastic edge weights \(p_g\), with
\(\lambda_g=p_g/K\),

\[
                         h_y^E={1\over K}\sum_{g\ni y}p_g.
\tag{5.3}
\]

On a balanced or degree-flat owner,

\[
                         h_y^E=(1+o(1))/r.
\tag{5.4}
\]

In the compensated process, the selected-edge and coin coefficients
sum to \(1/r\).  Thus removing the coin does not change the asymptotic
coefficient of (5.1).

### Proposition 5.1 (first-moment selected-edge data do not imply ASE--CHD)

There is an induced \(r\)-uniform stopped link satisfying the natural
one-child, pair/triple, and first selected-edge influence scales for
which

\[
                         Q_S^{E,\circ}=\Theta(1/r).
\tag{5.5}
\]

#### Construction

Put \(b=r-2\).  Take \(b^3\) child resources, partitioned into \(b\)
groups of size \(b^2\).  Inside the \(S\)-link, for each group \(G\)
take all rows

\[
                         S\cup B,
\qquad
                         B\in\binom Gb,
\tag{5.6}
\]

and no cross-group row.  Every child has degree

\[
                         A=\binom{b^2-1}{b-1},
\tag{5.7}
\]

and two distinct children in one group have joint degree

\[
 D=\binom{b^2-2}{b-2}
  =A{b-1\over b^2-1}
  =(1+o(1)){A\over b}.
\tag{5.8}
\]

Use uniform child weights \(p_a=b^{-3}\), and pad the remaining
catalogue so that every active common resource has edge-only hazard
\((1+o(1))/r\).  At the displayed state take \(c_{Sa}=1+o(1)\) and
\(\mu_{Sa}=A\).  For fixed \(y\),

\[
 {d_t(Say)\over\mu_{Sa}}
 =
 \begin{cases}
  (1+o(1))/b,&a\ne y\text{ in the group of }y,\\
  0,&\text{otherwise}.
 \end{cases}
\tag{5.9}
\]

The group has \(p\)-mass \(1/b\), so the variance in (5.1) is
\((1+o(1))b^{-3}\).  Summing over \(b^3\) choices of \(y\) and using
(5.4) gives (5.5).

Yet one-child profile mass is \(O(b^{-2})\), one common-resource
decrement is \(O(b^{-1})\), and the usual marginal and one-event sums
have the desired small scales.  What fails is their centered square
summed over all common resources.

The construction is an abstract induced stopped state, not a proved
reachable residual of the promotion-frame catalogue.  It proves that
the currently available first selected-edge and marginal stops do not
logically imply ASE--CHD.

## 6. Normalizer and shore coherence

The Doléans factors prove zero drift in the \(Z\)-coordinates.  PFS3 is
defined in the physical \(X\)-coordinates.  The comparison is

\[
                         Z_{Sa}
 =X_{Sa}
 \exp\left[-\int_0^t\beta_{Sa}(s)\,ds\right].
\tag{6.1}
\]

Thus NC is precisely an integrated drift-coherence statement.  It is
not a formal consequence of choosing the exact normalizer.

For root-stochastic edge weights, the nonterminal row hazard is governed
by the owner loads

\[
                         \ell_Y=\sum_{g\ni Y}p_g
\tag{6.2}
\]

and by the weighted multiple-intersection correction.  In schematic
exact form,

\[
 h_{f\mid T}
 ={1\over K}
 \left[
 \sum_{v\in f\setminus T}\ell_v
 -J_p^T(f)
 \right].
\tag{6.3}
\]

Comparing (6.3) with
\(-\dot\mu_T/\mu_T\) is exactly NC.

Likewise, the live-shore mass

\[
                         P_S(t)=\sum_{a\ {\rm live}}p_{S,a}
\tag{6.4}
\]

has selected-edge decrement

\[
                         w_S(g)
 =\sum_{a\in g\setminus S}p_{S,a}.
\tag{6.5}
\]

If the owner loads are hereditarily balanced and
\(\max_gw_S(g)\) has the static one-frame scale, then the usual
selected-edge Freedman argument makes (4.2) fail on only \(o(W)\)
marked incidence.  Without balanced loads, \(P_S\) has no common
reference drift and the same argument does not apply.

Thus the coin-free shore stop can be cheap, but only after a separate
load theorem.

## 7. A diffuse Hall cut defeats degree/shore completion

Let \({\cal A}\) contain \(N\) roots.  Let \(B\) contain

\[
                         M=(1-\delta)N
\tag{7.1}
\]

bottleneck owners, with fixed \(0<\delta<1\).  For every root \(R\),
take a private set \(P_R\) of \(r-1\) owners.  Include, for every
\(b\in B\), the edge

\[
                         e_{R,b}
 =\{R\}\cup P_R\cup\{b\}.
\tag{7.2}
\]

Every edge has one root and \(r\) owners.  Every root has degree \(M\).
Give its edges the root-stochastic weights

\[
                         p_{R,b}=1/M.
\tag{7.3}
\]

A nonterminal selected edge using \(b\) deletes exactly one of the
\(M\) options at every other root.  Hence its normalized influence on
each surviving root shore is

\[
                         1/M=o(1).
\tag{7.4}
\]

Nevertheless every matching uses distinct bottleneck owners, so its
size is at most

\[
                         |B|=(1-\delta)N.
\tag{7.5}
\]

At least \(\delta N\) roots remain unmatched.  The owner universe has
size

\[
                         W'=(r-1)N+M.
\tag{7.6}
\]

After a maximum matching the owner leave is

\[
\begin{aligned}
 W'-rM
 &=(r-1)N+M-rM\\
 &=\delta(r-1)N
 =\Theta(W').
\end{aligned}
\tag{7.7}
\]

Thus a diffuse local selected-edge bound does not make the degree/shore
stops cheap.  The obstruction is the signed Hall cut \(B\).  It is
detected by the edge-only joint Hall/Farkas criterion, not by
ASE--CHD.

This state is an abstract hypergraph obstruction.  It is not asserted
to be a reachable promotion-frame residual.  It proves that a proof for
that catalogue must use hereditary structure beyond the selected-edge
bound.

## 8. Exact implication boundary

### Proved

1. Child-specific Doléans factors remove all predictable linear bias.
2. Fixed time-zero incidence weights and live-shore centering make
   physical extension deletion an explicit nonpositive term.
3. The exact edge-only generator is (3.12), including the mixed
   boundary covariance.
4. ASE--CHD, NC, and the live-shore lower bound close PFS3 with
   \(o(W)\) stopped incidence.
5. The centered selected-edge diagonal alone does not control the
   moving-shore generator.
6. Removing coins does not improve the common-resource fourth-kernel
   scale.
7. First-moment or maximum selected-edge influence does not imply
   ASE--CHD.
8. ASE--CHD does not imply hereditary Hall or \(o(W)\) degree/shore
   stops.

### Not proved

1. ASE--CHD along the actual promotion-frame edge-only trajectory.
2. Incidence-weighted NC.
3. The live-shore lower bound under endogenous edge weights.
4. Hereditary diffuse joint Hall.
5. A near-perfect coefficient-one edge-only matching.

The edge-only proposal is therefore algebraically valid but not
complete.  Its exact remaining input is not singleton compensation:
it is a trajectory-specific augmented selected-edge conditional
spectral theorem, including the deletion/decrement boundary diagonal,
together with hereditary edge-load/Hall coherence.
