# MSW trade-cube routing is a ganged four-arm program, not a network flow

Date: 2026-07-26

## 0. Verdict

The proposed convex-cost-flow reduction is exact only for a fictitious
model in which every selectable move is one independently usable arc.  A
literal recursive MSW rectangle is not one arc.  At every interior lower
rank its signed target vector has four negative and four positive entries,
and the four resulting Johnson arcs have to be activated together.

Equivalently, if `B` is the node--arc incidence matrix of all individual
arms and `R` repeats one switch variable on its four arms, then the physical
matrix is

\[
                            A=BR.                       \tag{0.1}
\]

`B` is a network matrix; the equality coupling encoded by `R` is the
whole difficulty.  The physical epigraph matrix is not automatically
totally unimodular.  A three-column four-arm instance has a determinant-two
minor and an integrality gap.  Therefore the advertised set-cut formula is
not the exact MSW routing theorem.

What remains true is:

1. the ordinary max-flow/min-cut deficiency formula for genuinely
   independent one-arm moves;
2. an exact **fractional weighted-potential dual** for an additive MSW
   subcube;
3. a stacked weighted-potential dual, with one common switch vector, for
   a subcube additive simultaneously at all protected depths;
4. a statewise marginal-drain identity for the full, nonadditive recursive
   cube.

In particular, indicator sets are not enough even for the fractional
four-arm problem, and separate per-depth Hall conditions do not imply a
common integral choice.

---

## 1. Exact fixed-depth column of one legal rectangle

At depth `q`, put `k=m-q` and `ell=k-1`.  In the notation of
`MSW_MULTIRANK_LOCAL_TRADES.md`, one literal rectangle has signed load
change

\[
\begin{aligned}
 a_{q,e}={}&
   \partial_e\operatorname{suf}_{\ell}(\mathsf O_e)
  +\partial_e\operatorname{suf}_{\ell}(\mathsf E_e)\\
 &-\partial_e\operatorname{pre}_{\ell}(\mathsf E_e)
  -\partial_e\operatorname{pre}_{\ell}(\mathsf O_e),       \tag{1.1}
\end{aligned}
\]

where

\[
                 \partial_eK
                 =\mathbf e_{K\cup\{\gamma_e\}}
                  -\mathbf e_{K\cup\{\beta_e\}}.          \tag{1.2}
\]

For `2<=k<=m-2`, the eight endpoints are distinct.  Thus

\[
                  a_{q,e}=\mathbf1_{P_{q,e}}
                           -\mathbf1_{N_{q,e}},
 \qquad |P_{q,e}|=|N_{q,e}|=4.                            \tag{1.3}
\]

More explicitly, the four arms are

\[
\begin{array}{c|c}
 \text{removed target}&\text{inserted target}\\ \hline
 \operatorname{suf}_{\ell}(\mathsf O_e)\cup\{\beta_e\}
  &\operatorname{suf}_{\ell}(\mathsf O_e)\cup\{\gamma_e\}\\
 \operatorname{suf}_{\ell}(\mathsf E_e)\cup\{\beta_e\}
  &\operatorname{suf}_{\ell}(\mathsf E_e)\cup\{\gamma_e\}\\
 \operatorname{pre}_{\ell}(\mathsf E_e)\cup\{\gamma_e\}
  &\operatorname{pre}_{\ell}(\mathsf E_e)\cup\{\beta_e\}\\
 \operatorname{pre}_{\ell}(\mathsf O_e)\cup\{\gamma_e\}
  &\operatorname{pre}_{\ell}(\mathsf O_e)\cup\{\beta_e\}.
\end{array}                                               \tag{1.4}
\]

At `k=m-1` two cores cancel and one obtains a two-arm square, not a
one-arm move.  At `k=1,m` the column is zero.

Let `D_q` be the directed multigraph containing the four arcs in (1.4)
for every switch.  Its incidence matrix `B_q` is totally unimodular.  But
physical selection requires

\[
       f_{e,1}=f_{e,2}=f_{e,3}=f_{e,4}=x_e\in\{0,1\}.     \tag{1.5}
\]

Writing `R_(e,i),e=1`, this gives `A_q=B_qR`.  Dropping (1.5) is the
independent-arm relaxation; it is not an exact-factor operation.

There is a second qualification.  Formula (1.1) is the isolated change.
It adds linearly for a depth-`q` conflict-independent subfamily (and for
the whole fixed-scale family at its matched depth).  In the full recursive
cube, a window can have two switched boundary phases, so its final target
is not generally the sum of the isolated columns.

---

## 2. The one-arm deficiency formula (the valid benchmark)

Let a directed graph have integral capacities `u_e`, initial integral load
`mu_v`, and cap `b`.  If independent integral flow `f` may be sent along
its arcs, put

\[
 y_v=\mu_v-\sum_{e\in\delta^+(v)}f_e
             +\sum_{e\in\delta^-(v)}f_e,
 \qquad K_b(y)=\sum_v(y_v-b)_+.                          \tag{2.1}
\]

Define `e_v=(mu_v-b)_+` and `d_v=(b-mu_v)_+`.  Then

\[
 \boxed{
 \min_fK_b(y)
 =\max_{X\subseteq V}
   \bigl[e(X)-d(X)-u(\delta^+(X))\bigr].}                \tag{2.2}
\]

The right side is nonnegative because `X=emptyset` is allowed.  Since

\[
             e(X)-d(X)=\sum_{v\in X}(\mu_v-b),           \tag{2.3}
\]

(2.2) is exactly the proposed set-deficiency expression when every
capacity is one.

**Proof.** Attach a source to `v` with capacity `e_v`, attach `v` to a
sink with capacity `d_v`, and retain the routing arcs.  One routed unit
lowers `K_b` by one, and every improvement decomposes into excess-to-deficit
paths after cycles and useless paths are deleted.  Hence the minimum is
`e(V)` minus the maximum flow.  A cut with vertex part `X` has capacity

\[
             e(V\setminus X)+u(\delta^+(X))+d(X).
\]

Subtracting the minimum cut from `e(V)` proves (2.2).  \(\square\)

This theorem solves the independent-arm relaxation.  It does not survive
the equal-flow constraints (1.5).

---

## 3. Exact fixed-depth formulation and fractional dual

Assume a switch family is additive at depth `q`.  With columns (1.3), its
integer optimum is

\[
\boxed{
 \begin{aligned}
 K_{q,b}^{\mathbb Z}=
 \min\ &\sum_{S}z_S\\
 \text{s.t. }&z_S\ge \mu_q(S)-b+(A_qx)_S,\quad z_S\ge0,\\
             &x_e\in\{0,1\}.
 \end{aligned}}                                         \tag{3.1}
\]

Relaxing `x_e` to `[0,1]` and dualizing gives

\[
\boxed{
 K_{q,b}^{\rm LP}
 =\max_{0\le\alpha\le1}
 \left\{
  \langle\alpha,\mu_q-b\mathbf1\rangle
  -\sum_e
    \bigl(\alpha(N_{q,e})-\alpha(P_{q,e})\bigr)_+
 \right\}.}                                             \tag{3.2}
\]

Indeed, the multiplier on the first inequality in (3.1) lies in
`[0,1]`; minimizing one relaxed switch variable gives

\[
 \min_{0\le x_e\le1}x_e
   \bigl(\alpha(P_{q,e})-\alpha(N_{q,e})\bigr)
 =-\bigl(\alpha(N_{q,e})-\alpha(P_{q,e})\bigr)_+.        \tag{3.3}
\]

Thus the correct fractional Hall tests are all fractional potentials
`alpha`, not only indicators.  For `alpha=1_X`, the necessary cut is

\[
 \sum_{S\in X}(\mu_q(S)-b)
 \le\sum_e
       \bigl(|N_{q,e}\cap X|-|P_{q,e}\cap X|\bigr)_+.    \tag{3.4}
\]

A switch can contribute between zero and four units to this cut; counting
it as one escape arc is not the physical cut capacity.

The integer answer is

\[
        K_{q,b}^{\mathbb Z}=K_{q,b}^{\rm LP}
                            +\operatorname{IG}_{q,b},
 \qquad \operatorname{IG}_{q,b}\ge0,                    \tag{3.5}
\]

and no network theorem makes `IG_(q,b)` vanish.

---

## 4. A determinant-two and integrality-gap counterexample

The failure already occurs with three four-arm columns.  Let the resource
targets be `a,b,c`, initially of load zero, and use cap one.  For each
edge `uv` of the triangle, make a switch column whose positive endpoints
are `u,v` and two private zero-load targets.  Its negative endpoints are
one private load-two target `s_uv` and three private load-one targets.
All eight endpoints within one column are distinct.

For an integral choice of `k=0,1,2,3` columns, the residual cap tails are

\[
                              3,\ 2,\ 2,\ 3.             \tag{4.1}
\]

Hence `K_1^Z=2`.  At

\[
                     x_{ab}=x_{bc}=x_{ca}=\tfrac12,      \tag{4.2}
\]

every resource has load one and the three load-two sources contribute
one half each, so `K_1^LP=3/2`.

For completeness, the dual witness is

\[
 \alpha(s_{ab})=\alpha(s_{bc})=\alpha(s_{ca})=1,
 \qquad \alpha(a)=\alpha(b)=\alpha(c)=\tfrac12,          \tag{4.3}
\]

with all private weights zero.  Every column has equal positive and
negative alpha-mass, so (3.2) has value `3-3/2=3/2`.

Indicator cuts are strictly weaker here.  Private negative vertices can
be omitted without loss (they have zero base weight and only increase the
penalty), and a private positive vertex costs one while decreasing a
penalty by at most one.  Thus an optimal indicator uses only some triangle
resources and some load-two sources.  No resource gives value zero; one
resource can support the two adjacent sources and gives value one; two
resources support all three sources and again give value one.  Therefore

\[
 \max_{X\subseteq V}
 \left\{
  \langle\mathbf1_X,\mu-\mathbf1\rangle
  -\sum_e\bigl(|N_e\cap X|-|P_e\cap X|\bigr)_+
 \right\}=1<\frac32<2.                                  \tag{4.4}
\]

There is also an immediate total-unimodularity certificate.  Restricting
the three columns to the resource rows gives

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},                                         \tag{4.5}
\]

whose determinant is two.  Hence the four-arm class is not a network/TU
class.  This example does not assert that every specially selected MSW
submatrix has an integrality gap.  It proves that such integrality would
be an additional MSW theorem, not a consequence of convex-cost flow,
four-arm support, or commuting switches.

---

## 5. What survives jointly across depths

Suppose first that one subcube is additive simultaneously for all
`q<=H`, and let `w_q>0`.  One common physical switch vector must be used.
For the raw weighted cap tail, the fractional relaxation has the exact
dual

\[
\boxed{
\begin{aligned}
 &\min_{0\le x\le1}
   \sum_{q\le H}w_qK_{q,b_q}(\mu_q+A_qx)\\
 &\quad=\max_{0\le\alpha_q\le w_q}
 \left\{
   \sum_{q\le H}\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
  -\sum_e\left(
     \sum_{q\le H}
       [\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
             \right)_+
 \right\}.
                                                               \tag{5.1}
\end{aligned}}
\]

The positive part is outside the sum over depths.  This is the exact
mathematical expression of synchronization: a switch is chosen once, so
favourable action at one depth can be cancelled by collateral action at
another.  Optimizing separately at each depth replaces the last term by a
different, larger relaxation and is invalid.

For the row-power phase-capacity functional

\[
 \operatorname{PCap}_H
 =\sum_{q\le H}
       \bigl(K_{q,p}-(W-N_q)\bigr)_+,                    \tag{5.2}
\]

the corresponding exact fractional dual is

\[
\boxed{
\begin{aligned}
 \max_{0\le\gamma_q\le1}\Bigg\{
 &\sum_{q\le H}
   \left[
    \langle\gamma_q,\mu_q-p\mathbf1\rangle
    -(W-N_q)\|\gamma_q\|_\infty
   \right]\\
 &-\sum_e\left(
    \sum_{q\le H}
      [\gamma_q(N_{q,e})-\gamma_q(P_{q,e})]
            \right)_+
 \Bigg\}.                                               \tag{5.3}
\end{aligned}}
\]

Formula (5.3) follows from

\[
 (K_p(y)-c)_+
 =\max_{0\le\gamma\le1}
   \bigl[\langle\gamma,y-p\mathbf1\rangle
         -c\|\gamma\|_\infty\bigr]                    \tag{5.4}
\]

and minimax.  It is only a fractional theorem.  A constant-one argument
still needs an `o(W)` integer-rounding loss for the stacked matrix.

For the **full** recursive cube, even (5.1)--(5.3) need not describe the
final histogram because simultaneous effects are not additive.  Toggling
the chosen switches in order gives the exact replacement.  If at one
toggle the current old and new target multisets at depth `q` are `N_jq`
and `P_jq`, then in the unit-distinct case

\[
\boxed{
 K_{q,b}(\mu^{(j)})-K_{q,b}(\mu^{(j+1)})
 =|N_{jq}\cap\{S:\mu^{(j)}_q(S)>b\}|
  -|P_{jq}\cap\{S:\mu^{(j)}_q(S)\ge b\}|.}             \tag{5.5}
\]

With repeated endpoints, each removed multiplicity is truncated by the
current excess and each inserted multiplicity is charged after current
slack.  Summing (5.5) over depths and toggles is the surviving dynamic
drain ledger.  It supplies no static max-flow/min-cut theorem.

One may force simultaneous additivity by taking an independent set in the
union of the depth-conflict graphs.  Since each individual conflict graph
has maximum degree at most four, the naive guarantee loses a factor
`4H+1`; that loss is not known to be affordable.  Alternatively, one must
prove a genuinely state-dependent multidepth drain theorem.

---

## 6. Consequence for the constant-one route

The flow/Hall proposal therefore does not close the trade lane.  The exact
remaining fixed-depth requirements are

\[
 \boxed{
 K_{q,b}^{\rm LP}=o(W),\qquad
 \operatorname{IG}_{q,b}=o(W),}                         \tag{6.1}
\]

uniformly in the required range, with the **same** switch choices across
depths.  In dual language the first requirement must hold for all
fractional target potentials, not only overloaded sets.  The second is a
new structured-rounding theorem for the physical MSW columns.

For the nonadditive full cube, these are replaced by the stronger dynamic
condition that almost all used toggles have negative arms in current
excess and positive arms in current strict slack, simultaneously in the
weighted multidepth ledger.  No present rectangle count proves either
condition.

