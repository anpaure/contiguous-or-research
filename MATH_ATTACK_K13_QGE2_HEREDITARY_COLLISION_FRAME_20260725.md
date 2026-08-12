# Lane K13: the \(q\ge2\) collision frame, owner-fixed spikes, and a literal hereditary obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, web search,
SAT, or solver is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 T=\binom{2m+1}{m-1},
\]

\[
 C_m=\operatorname {Cat}_m=\frac{W}{2m+1},\qquad
 A_m=\binom{2m-1}{m-1},\qquad
 R_m=\operatorname {Cat}_{m-1}=\frac{A_m}{2m-1}.
\tag{0.1}
\]

Assume

\[
 2\le H=o(m/\log ^2m).
\tag{0.2}
\]

This contains every fixed Gaussian window \(H=\lceil A\sqrt m\rceil\).
In particular,

\[
 H C_m=\frac{HW}{2m+1}=o(W).
\tag{0.3}
\]

The audited adjacent conjugate atlas has two exact properties.

* Its first-upper within-block charge is pointwise zero.
* For \(q\ge2\), its full adjacent-visible census is exactly the complete
  upper collision census minus the invariant collision census, with the
  arithmetic factorial floor retained.

The new owner-fixed spike chart supplies a genuine repair for one
concentrated upper collision. After the corrections in
PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_AUDIT_20260725.md, a common
phase-\(A\), common-\(U_q\) spike of multiplicity \(t\) has

\[
 \Gamma_{\rm sp}\ge w_q^+t(t-1),
\qquad
 \Delta J\le2t,
\qquad
 t\le R_m.
\tag{0.4}
\]

Thus one spike has \(O(HC_m)\) literal context cost and \(o(W/H)\) run
cost. The chart is nevertheless not a hereditary current-state charge:
its exact expected change from the all-old endpoint is

\[
 \frac{Q(M_1)-Q(M_0)}2-\frac{\Gamma_{\rm sp}}4.
\tag{0.5}
\]

The coherent endpoint drift in (0.5) can have either sign. Moreover one
fixed leaf pair occupies at most \(q-1\) consecutive carrier starts in a
row, so diffuse \(q\)-collisions require \(\Omega(W/q)\) leaf-row blocks.

The main result of this report is a stronger, literal obstruction to the
requested **complete signed** \(q\ge2\) frame.

Choose the phase-one local factor to be the canonical MSW factor on
\([2m-1]\), and transport it along the audited adjacent factor path. The
resulting actual first-avoided, low-run token matching \(M_0\) has

\[
 \boxed{
 Z_2^-(M_0)\ge(1/64-o(1))W}
\tag{0.6}
\]

zero lower-depth-two targets. Consequently its doubled lower factorial
floor excess satisfies

\[
 \boxed{
 Q_2^-(M_0)\ge(1/32-o(1))W.}
\tag{0.7}
\]

Every adjacent conjugate switch and every owner-fixed spike fixes every
lower flag pointwise. Hence (0.6)--(0.7) persist through every sequence of
these switches, regardless of packet dependence, fresh star leaves, or
run budget. An arbitrary completion by the missing \(W-T=O(W/m)\)
tokens cannot erase more than \(o(W)\) of the holes.

It follows that no descent-valid hereditary inequality of the form

\[
 \boxed{
 \mathfrak D_{\rm adj}(M)+\mathfrak D_{\rm sp}(M)
 \ge
 \eta\bigl(\mathcal Q_{\ge2}(M)-C H C_m\bigr)}
\tag{0.8}
\]

can hold for this adjacent-plus-owner-fixed-spike architecture with fixed
\(\eta>0\) and \(C<\infty\). Here “descent-valid” means that the left
side is certified by a legal corner below the current state, not merely
by a positive raw Gram relative to the average of two endpoints.

If the proposed frame is required uniformly for arbitrary nonnegative
signed-depth weights, the refutation is immediate: put all weight on the
lower \(q=2\) summand. Every proposed charge is zero and the right side is
\(\Omega(W)\). For a fixed all-depth weighting, a raw upper Gram sum
could numerically cross-pay the invariant lower defect, but it cannot
compose into descent; a minimum-energy reachable corner still retains
(0.7).

Thus the complete signed frame is rigorously refuted for this architecture.
A genuinely lower-moving, same-word chart is necessary. The upper-only
frame remains open after replacing every spike Gram by its drift-corrected
net charge; the exact surviving upper gate is stated in Section 7.

No coefficient-one conclusion is claimed.

## 1. Exact adjacent-visible census with owner categories and collars

Partition \(2m\) coordinates into ordered disjoint pairs

\[
 P_1,\ldots ,P_m
\]

and leave one coordinate unpaired. In the coherent first-avoided base,
every loaded upper target \(U\) has one category

\[
 \kappa(U)=\min\{j:U\cap P_j=\varnothing\}.
\tag{1.1}
\]

Indeed, if an occurrence is carried by phase \(j\), then its lower root
meets every \(P_h\), \(h<j\), while the whole local row, and hence \(U\),
avoids \(P_j\).

Fix an upper depth \(q\) and a loaded target \(U\) of category \(j\).
For an occurrence over root \(S\), put

\[
 D(U,S)=U\setminus S,\qquad |D(U,S)|=q+1.
\tag{1.2}
\]

Let

\[
 C_j(U)=U\cap P_{j+1}.
\tag{1.3}
\]

The occurrence belongs to the adjacent \(j\)-carrier and moves
nontrivially if and only if

\[
 j<m,\qquad
 \varnothing\ne C_j(U)\subseteq D(U,S).
\tag{1.4}
\]

Write \(a_{j,q,U}\) for the number of occurrences satisfying (1.4), and
put \(a_{j,q,U}=0\) when \(\kappa(U)\ne j\). The complete adjacent-visible
charge at depth \(q\) is

\[
 \mathcal C_{{\rm all},q}
 =\sum_U\binom{a_{\kappa(U),q,U}}2.
\tag{1.5}
\]

Here and below \(a_{m,q,U}=0\); the final owner category has no adjacent
successor.

Let \(x_{q,U}\) be the full upper load, and write

\[
 T=c_qK_q+\delta_q,\qquad
 K_q=\binom{2m+1}{m+q},\qquad
 0\le\delta_q<K_q,
\tag{1.6}
\]

\[
 p_q^{\min}
 =(K_q-\delta_q)\binom{c_q}{2}
 +\delta_q\binom{c_q+1}{2},
\tag{1.7}
\]

\[
 \Phi_q^+
 =\sum_U\binom{x_{q,U}}2-p_q^{\min}.
\tag{1.8}
\]

Define the invariant collision census

\[
 \mathcal I_{{\rm all},q}
 =\sum_U\left[
 \binom{x_{q,U}}2-
 \binom{a_{\kappa(U),q,U}}2
 \right].
\tag{1.9}
\]

The collision pairs at one target split into the two movable occurrences
and all pairs with at least one immovable occurrence. Therefore

\[
 \boxed{
 \mathcal C_{{\rm all},q}
 =\Phi_q^+-
 \bigl(\mathcal I_{{\rm all},q}-p_q^{\min}\bigr).}
\tag{1.10}
\]

The odd and even disjoint layers partition (1.5), so one legal parity
layer captures at least \(\mathcal C_{{\rm all},q}/2\). Its complete
packet catalog obeys

\[
 r_{\rm parity}
 =O(W\log ^2m/m),
\qquad
 \Delta J\le2r_{\rm parity},
\qquad
 \partial_{\rm new}\le4r_{\rm parity}.
\tag{1.11}
\]

Under (0.2), this is \(o(W/H)\).

At \(q=1\), two distinct occurrences of one \(U\) have disjoint two-point
collars. If both satisfied (1.4), the nonempty set \(C_j(U)\) would lie in
both collars, a contradiction. Hence

\[
 \boxed{\mathcal C_{{\rm all},1}=0.}
\tag{1.12}
\]

This is why all subsequent collision comparisons begin at \(q=2\).

## 2. What the owner-fixed spike really adds

For a phase-\(A\) token write

\[
 S=I_\pi(i,m-1),\qquad
 Y=I_\pi(i-1,m),
\]

\[
 U_p=I_\pi(i-1,m+p),\qquad
 D_p^Y:=U_p\setminus Y.
\tag{2.1}
\]

Thus \(|D_p^Y|=p\). For \(q\ge2\), choose a two-set

\[
 B\subset D_q^Y.
\tag{2.2}
\]

Fix one bijection \(B\to A\) globally, let \(\theta_B\) exchange the two
pairs, and require

\[
 F_B=\theta_BF_A.
\tag{2.3}
\]

Because \(B\cap Y=\varnothing\) and \(S\subset Y\),

\[
 \theta_BS=S,\qquad
 \theta_BY=Y.
\tag{2.4}
\]

Thus the old and conjugate tokens have the same lower endpoint and middle
owner, and every lower flag is fixed. Arbitrary choices at distinct
central edges remain a literal unlabelled matching.

For a common target \(U_q=U\), choose one \(B_i\subset U\setminus Y_i\)
per occurrence. At depth \(p\), the exact corrected cross-Gram identity
is

\[
 \langle d_{i,p},d_{k,p}\rangle
 =
 \mathbf1_{\{d_{i,p}\ne0,\ d_{k,p}\ne0\}}
 \left(
  \mathbf1_{\{U_p^{(i)}=U_p^{(k)}\}}
  +\mathbf1_{\{\theta_{B_i}U_p^{(i)}
                   =\theta_{B_k}U_p^{(k)}\}}
 \right)\ge0.
\tag{2.5}
\]

At the distinguished depth all old targets equal \(U\), every column is
nonzero, and

\[
 \theta_{B_i}U=(U\setminus B_i)\cup A.
\tag{2.6}
\]

Hence

\[
 \Gamma_{\rm sp}
 =2\sum_{i<k}\langle d_i,d_k\rangle_w
 \ge w_q^+t(t-1).
\tag{2.7}
\]

For doubled factorial-floor energy,

\[
 \boxed{
 \mathbb E Q(M_\varepsilon)-Q(M_0)
 =\frac{Q(M_1)-Q(M_0)}2-\frac{\Gamma_{\rm sp}}4.}
\tag{2.8}
\]

This proves positive curvature, but the only current-state net charge is

\[
 \boxed{
 \mathfrak D_{\rm sp}^{\,0}
 :=
 \frac{\Gamma_{\rm sp}}4-\frac{Q(M_1)-Q(M_0)}2.}
\tag{2.9}
\]

Other depths and a common completion are included in \(Q(M_1)-Q(M_0)\).
A corner-dependent completion or choice-dependent literal row collars are
not common affine terms and need a separate estimate.

At \(q=2\) there is no leaf choice:

\[
 B_i=U_2\setminus Y_i,\qquad
 U_2=Y_i\cup B_i,\qquad
 V_i:=\theta_{B_i}U_2=Y_i\cup A.
\tag{2.10}
\]

Distinct owners give distinct \(B_i\)'s and distinct \(V_i\)'s within one
common-\(U\) spike. The spike therefore routes mass only to the prescribed
owner-labelled images \(Y_i\cup A\), not to arbitrary floor holes. If
\(x_U=b+t\), \(t_B\) occurrences use \(B\), and \(y_B=x_{(U\setminus
B)\cup A}\), then the distinguished-rank doubled endpoint drift is

\[
 Q_2(M_1)-Q_2(M_0)
 =
 w_2^+\left[
 -2bt-t(t-1)
 +\sum_B\bigl(2y_Bt_B+t_B(t_B-1)\bigr)
 \right].
\tag{2.11}
\]

Thus a Hall/augmenting-path or occupied-image theorem is indispensable.
Raw curvature cannot replace it.

## 3. Catalan reservoir and the diffuse carrier ceiling

In the proper-window range \(q\le m-2\), one fixed \(U_q\) occurs at most
once in a row of \(F_A\). Therefore

\[
 t\le R_m=\operatorname {Cat}_{m-1},
\tag{3.1}
\]

and one spike has

\[
 \Delta J\le2t
 \le2R_m
 =\frac{m+1}{2m-1}C_m<C_m,
\tag{3.2}
\]

\[
 \partial_{\rm new}\le4t<2C_m,
\qquad
 \text{standard context length}=O(HC_m).
\tag{3.3}
\]

This is the exact Catalan reservoir promised by a single concentrated
spike.

It cannot be summed over a diffuse collision sector. In a row

\[
 D_q^Y(i)
 =\{x_{i+m-1},\ldots,x_{i+m+q-2}\}.
\tag{3.4}
\]

For fixed \(B\), the starts satisfying \(B\subset D_q^Y(i)\) form either
the empty set or one cyclic interval of length at most \(q-1\). Distinct
old rows give distinct conjugate rows. Hence switching \(M\) spike
occurrences requires at least

\[
 \boxed{M/(q-1)}
\tag{3.5}
\]

leaf-row blocks. In particular, every \(q=2\) carrier is a singleton.
Covering a positive-density bounded-multiplicity collision sector costs

\[
 \Omega(W/q)\ge\Omega(W/H)
\tag{3.6}
\]

blocks, not \(o(W/H)\). Concentrated multiplicity gives quadratic charge
for linear run cost; diffuse doubletons do not.

The factor ledger has a second restriction. A one-hub star is consistent
after one \(F_B=\theta_BF_A\) is fixed per leaf, even when leaf pairs
overlap. It need not coexist with the protected adjacent path. For three
priority pairs, the path prescriptions

\[
 F_2=\theta_{12}F_1,\qquad
 F_3=\theta_{23}\theta_{12}F_1
\]

and the hub prescription \(F_3=\theta_{13}F_1\) force

\[
 \theta_{13}^{-1}\theta_{23}\theta_{12}
 =\theta_{23}\in\operatorname {Aut}(F_1),
\tag{3.7}
\]

the forbidden two-block triangle holonomy. New coverage therefore needs
fresh nonpriority leaves, or a new factor-symmetry theorem. With only the
existing adjacent edge \(A=P_j\), \(B=P_{j+1}\), every owner-fixed spike
eligible for that edge is already counted by (1.5).

## 4. A literal canonical lower-depth-two defect

Choose \(F_1\) to be the canonical MSW exact factor on

\[
 Q_1=[n]\setminus P_1,\qquad |Q_1|=2m-1.
\]

Define the priority factors recursively by the audited path conjugacies

\[
 F_{j+1}=\tau_jF_j,\qquad 1\le j<m,
\tag{4.1}
\]

and let \(M_0\) be the coherent first-avoided matching.

Let \(Z_2^-(M_0)\) be the number of rank-\((m-2)\) targets with zero
lower-depth-two load. We now prove (0.6) with an explicit finite-\(m\)
lower bound.

### Theorem 4.1 (canonical phase-one holes survive globally)

Let

\[
 t_0=\lceil20\log m\rceil.
\tag{4.2}
\]

Let \(C_0\) be the absolute constant in the audited category-tail estimate

\[
 N_h\le C_0\sqrt m\,A_m(3/4)^{h-1},
\tag{4.3}
\]

where \(N_h\) is the number of roots of first-avoided category \(h\).
Then

\[
 \boxed{
\begin{aligned}
 Z_2^-(M_0)\ge\;&
 A_m\left[
 \frac{m(m-1)}
 {4(2m-3)(2m-1)}
 -\frac2{m+1}
 \right]\\
 &-2R_m(t_0-1)
 -4C_0\sqrt m\,A_m(3/4)^{t_0}.
\end{aligned}}
\tag{4.4}
\]

Consequently

\[
 Z_2^-(M_0)\ge(1/64-o(1))W.
\tag{4.5}
\]

#### Proof

Phase one selects every start of \(F_1\). Apply the independently audited
marked-gap theorem with local central parameter \(m-1\). The number
\(M_{\rm loc}\) of missing rank-\((m-2)\) cyclic targets in this phase
satisfies

\[
 M_{\rm loc}\ge
 A_m\left[
 \frac{m(m-1)}
 {4(2m-3)(2m-1)}
 -\frac2{m+1}
 \right].
\tag{4.6}
\]

Every target counted in (4.6) avoids \(P_1\), and hence has owner category
one. A later phase-\(h\) token can fill such a lower target only if its
lower-depth-two flag has category one. Since this flag is obtained from
the root by deleting one coordinate, that deleted coordinate must be one
of the two points of \(P_1\). Each coordinate departs at one start in a
cyclic row, so there are at most two relevant starts per row, independently
of \(h\). Since every \(F_h\) has \(R_m\) rows, phases
\(2\le h\le t_0\) contribute at most

\[
 2R_m(t_0-1)
\tag{4.7}
\]

possible fills.

For \(h>t_0\), sum (4.3):

\[
 \sum_{h>t_0}N_h
 \le4C_0\sqrt m\,A_m(3/4)^{t_0}.
\tag{4.8}
\]

Subtracting (4.7)--(4.8) from (4.6) proves (4.4).

Finally,

\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)}
 \longrightarrow\frac14,
\qquad
 \frac{R_mt_0}{W}=O(\log m/m),
\tag{4.9}
\]

and the last term in (4.4) is \(O(A_mm^{-2})\). The bracket in (4.6)
tends to \(1/16\). This proves (4.5). \(\square\)

The same coherent matching has

\[
 J(M_0)=O(W\log ^2m/m)=o(W/H)
\tag{4.10}
\]

under (0.2). Thus (4.5) is an actual low-run fixed-factor state, not an
ambient load-vector witness.

## 5. Exact factorial-floor constant and persistence

Put

\[
 N_2^-=\binom{2m+1}{m-2}.
\tag{5.1}
\]

For the autonomous token mass,

\[
 \frac{T}{N_2^-}=\frac{m+3}{m-1}=1+\frac4{m-1}.
\tag{5.2}
\]

For all sufficiently large \(m\), the exact lower-depth-two floor uses
loads one and two. Its doubled floor polynomial is

\[
 Q_2^-(x)
 =\sum_{|R|=m-2}(x_R-1)(x_R-2)
 =2\Phi_2^-(x),
\tag{5.3}
\]

where \(\Phi_2^-\) is the half-floor collision excess. Every zero target
contributes two to \(Q_2^-\), and every integral summand in (5.3) is
nonnegative. Hence Theorem 4.1 gives

\[
 Q_2^-(M_0)\ge2Z_2^-(M_0)
 \ge(1/32-o(1))W.
\tag{5.4}
\]

An arbitrary completion to mass \(W\) adds

\[
 W-T=\frac{2W}{m+2}=o(W)
\tag{5.5}
\]

lower occurrences and therefore fills at most that many holes. Moreover

\[
 \frac{W}{N_2^-}
 =\frac{(m+3)(m+2)}{m(m-1)}<2
\tag{5.6}
\]

for \(m\ge8\), so the completed floor still uses levels one and two.
Thus (5.4) survives with the same asymptotic constant after every
completion:

\[
 Q_{2,{\rm full}}^-\ge
 2\left(Z_2^-(M_0)-\frac{2W}{m+2}\right)
 =(1/32-o(1))W.
\tag{5.7}
\]

The same conclusion covers literal row contexts. If the completed word
adds \(E_m=o(W)\) further positions, those positions can fill at most
\(E_m\) of the holes, while

\[
 \frac{W+E_m}{N_2^-}=1+o(1)<2
\tag{5.7a}
\]

eventually. Hence its doubled lower floor energy is at least

\[
 2\left(
 Z_2^-(M_0)-\frac{2W}{m+2}-E_m
 \right)
 =(1/32-o(1))W.
\tag{5.7b}
\]

In particular, an \(o(W/H)\)-run realization contributes
\(O(HJ)=o(W)\) standard collars, and the permitted
\(O(HC_m)=o(W)\) Catalan reservoir does not affect the constant.

### Theorem 5.1 (pointwise hereditary invariance)

Let \(\mathscr R(M_0)\) be the closure of \(M_0\) under arbitrary
sequences of:

1. legal adjacent conjugate interval switches from the path (4.1);
2. legal owner-fixed spike switches satisfying (2.2)--(2.4), including
   switches using compatible fresh leaf factors.

Then every \(M\in\mathscr R(M_0)\) has exactly the same lower flag at every
central root as \(M_0\). In particular,

\[
 Z_2^-(M)=Z_2^-(M_0),
\qquad
 Q_2^-(M)=Q_2^-(M_0).
\tag{5.8}
\]

#### Proof

For an adjacent switch, the root \(S\) avoids both exchanged priority
pairs. The coordinate exchange fixes \(S\) pointwise, and every lower
flag is a subset of \(S\).

For an owner-fixed spike, (2.4) fixes \(S\) pointwise, and again every
lower flag is a subset of \(S\). Thus each generator of the reachability
closure preserves every lower flag occurrence, not merely its aggregate
histogram. Composition proves (5.8). \(\square\)

This theorem is independent of the number of fresh leaves, the selected
packet correlations, and the run ledger.

## 6. No hereditary complete signed frame

We now formalize the obstruction.

Call a charge \(\mathfrak D(M)\) **descent-valid** if there is a literal
legal corner \(M'\in\mathscr R(M)\) for which

\[
 \mathcal Q_{\ge2}(M')
 \le\mathcal Q_{\ge2}(M)-\mathfrak D(M).
\tag{6.1}
\]

For definiteness, in Theorem 6.1 let

\[
 \mathcal Q_{\ge2}
 =Q_2^-+
 \sum_{\substack{2\le q\le H,\ \sigma\in\{-,+\}\\
                  (q,\sigma)\ne(2,-)}}
 w_q^\sigma Q_q^\sigma,
 \qquad w_q^\sigma\ge0,
\tag{6.1a}
\]

be the doubled autonomous token-core floor energy. The coefficient of
\(Q_2^-\) is one because its exact floor parameter is \(c_2^-=1\).
The same theorem holds for a completed \(W\)-mass ledger, using (5.7)
instead of (5.4).

The adjacent charge is descent-valid because its two coherent endpoints
are rankwise floor-equivalent. The owner-fixed raw quantity
\(\Gamma_{\rm sp}/4\) is not descent-valid; only the drift-corrected
quantity in (2.9), after all ranks and common completion terms are
included, can be used in (6.1).

### Theorem 6.1 (hereditary frame obstruction)

Fix \(\eta>0\) and \(C<\infty\). There is no rule on
\(\mathscr R(M_0)\) which, at every state \(M\), supplies a jointly legal
adjacent-plus-owner-fixed-spike corner of total new-run cost \(o(W/H)\)
and a descent-valid charge satisfying

\[
 \mathfrak D(M)
 \ge
 \eta\left(\mathcal Q_{\ge2}(M)-C H C_m\right).
\tag{6.2}
\]

The conclusion remains true if the run restriction is deleted.

#### Proof

Every state in \(\mathscr R(M_0)\) has, by (5.4) and Theorem 5.1,

\[
 \mathcal Q_{\ge2}(M)
 \ge Q_2^-(M)
 \ge(1/32-o(1))W.
\tag{6.3}
\]

By (0.3), \(C H C_m=o(W)\). Hence the right side of (6.2) is positive
and of order \(W\) for every reachable state.

The fixed factor system and its finite collection of token alternatives
give a finite reachability set. Choose \(M_\ast\in\mathscr R(M_0)\)
minimizing \(\mathcal Q_{\ge2}\). No reachable legal corner can have
positive descent from \(M_\ast\), so every descent-valid charge there is
zero. This contradicts (6.2) and (6.3). \(\square\)

If the desired inequality is asserted for every choice of nonnegative
signed-depth weights, an even shorter proof is available. Set

\[
 w_2^-=1,\qquad
 w_q^\pm=0\quad\text{for every other signed depth}.
\tag{6.4}
\]

Every adjacent and owner-fixed innovation has zero projection on this
space, so the entire proposed left side is zero. Equations (0.3) and
(5.4) make the right side \((1/32-o(1))\eta W>0\).

This refutes a complete signed frame, not merely a particular rounding
law. It also explains why a raw positive upper Gram cannot be counted as
cross-payment: at \(M_\ast\), such a Gram can remain positive only because
its coherent endpoint drift cancels it.

## 7. Positive last-category theorem and the exact remaining upper gate

The owner-fixed chart does give one genuinely one-sided upper repair.
This records the part which survives the audit.

### Theorem 7.1 (complete phase-\(m\), \(q=2\) spike repair)

At the coherent first-avoided base, simultaneously consider every
phase-\(m\) upper-depth-two target of multiplicity \(x_U\ge2\). Retain
one occurrence and owner-fix-switch the other \(x_U-1\) occurrences using
their forced leaves

\[
 B=U\setminus Y.
\tag{7.1}
\]

Then:

1. every required \(B\) is a nonpriority pair, so its hub-\(P_m\) factor
   is a fresh leaf and does not overwrite the protected path factors;
2. all new \(q=1\) and \(q=2\) upper targets are distinct and were empty
   in the coherent base;
3. the autonomous token-core \(q=2\) upper half-floor energy drops by
   exactly

   \[
   \sum_U\binom{x_U}{2};
   \tag{7.2}
   \]

4. the \(q=1\) upper collision energy does not increase;
5. the number of added selected runs is at most

   \[
   2N_m=2^m=o(W/H),
   \qquad N_m=2^{m-1}.
   \tag{7.3}
   \]

Thus, for the autonomous two-upper-depth ledger \(H=2\), this is a literal
one-sided repair of the complete final owner category. It still fixes the
lower defect from Section 5. An arbitrary completion can occupy the image
targets and needs a separate common-completion check, and for \(H>2\) the
deeper endpoint drift is not controlled.

#### Proof

A phase-\(m\) root \(S\) meets every \(P_h\), \(h<m\), and avoids \(P_m\).
Its owner \(Y\supset S\) has the same property. At \(q=2\),
\(B=U\setminus Y\) is disjoint from \(Y\). It cannot equal any
\(P_h\), \(h<m\), because \(Y\) meets that pair, and it cannot equal
\(P_m\), because the whole old row avoids \(P_m\). Hence \(B\) is
nonpriority.

The new targets have the forms

\[
 V_1=Y\cup\{a\},
\qquad
 V_2=Y\cup P_m
\tag{7.4}
\]

for one \(a\in P_m\). Both meet every priority pair. Every coherent-base
upper target avoids the omitted pair of its phase, so no target meeting
all priority pairs is loaded. Distinct middle owners give distinct
targets in (7.4); their intersections with \(P_m\) first identify the
displayed \(P_m\)-part and then identify \(Y\).

Old phase-\(m\) \(q=2\) targets avoid \(P_m\), while the new targets meet
it, so old and new supports are disjoint. Moreover an old phase-\(m\)
target contains its root, which meets every earlier priority pair; its
owner category is therefore exactly \(m\), and no earlier phase can also
load it. Since \(K_2^+=T\), the autonomous upper \(q=2\) floor is the
all-one floor. Moving all but one occurrence from each old target leaves
every old and new target at load one. This proves (7.2) and the \(q=1\)
nonincrease.

Finally a phase-\(m\) root chooses exactly one coordinate from each of
\(P_1,\ldots,P_{m-1}\), so \(N_m=2^{m-1}\). The owner-fixed run ledger
gives (7.3). \(\square\)

For the complete **upper-only** \(q\ge2\) problem, the surviving statement
is now precise. At every current state one would need compatible
owner-category stars and a jointly executable packet family satisfying

\[
 \mathcal C_{\rm adj}^{\rm net}(M)
 +\mathcal C_{\rm sp}^{\rm net}(M)
 \ge
 \eta\left(\Phi_{\ge2}^+(M)-C H C_m\right),
\tag{7.5}
\]

where:

* \(\mathcal C_{\rm adj}^{\rm net}\) is governed exactly by (1.10);
* every spike term uses the full drift correction (2.9), not raw
  \(\Gamma_{\rm sp}/4\);
* repeated leaf factors obey one fixed conjugacy assignment;
* the selected leaf-row blocks total \(o(W/H)\);
* \(q=2\) first-rank leakage and all choice-dependent literal collars are
  charged;
* the same quantifiers survive after a mixed corner.

Concentrated spikes satisfy the Catalan ledger (3.1)--(3.3), and Theorem
7.1 settles one terminal owner category. Diffuse bounded multiplicity,
occupied prescribed images, multi-hub holonomy, and hereditary renewal
remain unproved. None of these upper refinements can repair the complete
signed frame without a lower-moving chart because of Theorem 6.1.

## 8. Certified boundary

The following statements are proved.

1. The exact adjacent-visible collar census is (1.5), its floor-residual
   identity is (1.10), and its \(q=1\) part vanishes pointwise.
2. Owner-fixed spikes are literal central switches when one factor
   conjugacy is fixed per leaf. Their corrected Gram is nonnegative and
   their common-target curvature is (2.7).
3. The only below-current spike charge is the drift-corrected quantity
   (2.9); raw Haar curvature is insufficient.
4. One concentrated spike uses at most \(R_m\) occurrences and has
   \(O(HC_m)\) context cost, while diffuse coverage obeys the sharp carrier
   ceiling (3.5).
5. The canonical path-factor first-avoided matching has the actual
   low-run lower-depth-two defect (4.4)--(5.4).
6. Every adjacent and owner-fixed switch preserves that defect pointwise.
7. Therefore the requested complete signed, descent-valid hereditary
   frame with \(O(HC_m)\) reservoir is false.
8. The final owner category has the positive one-sided \(q=2\) repair in
   Theorem 7.1.

The following remain open.

* an upper-only drift-corrected inequality (7.5);
* a low-run packing theorem for diffuse bounded-multiplicity upper
  collisions;
* compatible fresh stars at all owner categories;
* a literal lower-moving chart with the same fixed-factor and word
  quantifiers.

The last item is logically mandatory for a complete constant-one route.
