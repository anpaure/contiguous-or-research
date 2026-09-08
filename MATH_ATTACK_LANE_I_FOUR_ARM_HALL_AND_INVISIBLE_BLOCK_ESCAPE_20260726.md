# Lane I: four-arm Hall deficiency and invisible-block escape

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 K_b(\mu)=\sum_{v}(\mu_v-b)_+                     \tag{0.1}
\]

be the cap overload at one target layer.  A four-arm trade has signed
column

\[
 a_e=\mathbf1_{P_e}-\mathbf1_{N_e},
 \qquad |P_e|=|N_e|=4.                              \tag{0.2}
\]

There are three distinct conclusions.

1. The exact gain of one statewise trade is

   \[
    \boxed{
    K_b(\mu)-K_b(\mu+a_e)
    =
    |N_e\cap\{\mu>b\}|
    -
    |P_e\cap\{\mu\ge b\}|.}                         \tag{0.3}
   \]

   Thus a four-unit decrease requires every negative endpoint to be
   strictly overloaded and every positive endpoint to be strictly below
   the cap.  A positive endpoint of load exactly \(b\) is not free.

2. For an additive four-arm family, the correct fractional Hall
   deficiency is a **weighted** cut over all
   \(0\le\alpha_v\le1\):

   \[
    \boxed{
    \operatorname{Def}^{\rm frac}_b(\mu,A)
    =
    \max_{0\le\alpha\le1}
    \left[
      \langle\alpha,\mu-b\mathbf1\rangle
      -
      \sum_e
       \bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
    \right].}                                      \tag{0.4}
   \]

   Fractional elimination is equivalent to the nonpositivity of every
   such weighted cut.  Indicator cuts alone are not sufficient, and the
   integral problem has an additional hypergraph-matching integrality
   deficiency.

3. A fixed invisible fibre is closed under substitutions performed wholly
   inside its own hole, but it is not closed under the certified
   one-level-up parent rectangle direction.  The parent trade moves one
   occurrence from

   \[
    O\cup\{2\}\longrightarrow O\cup\{4\}.           \tag{0.5}
   \]

   Hence the fixed-fibre obstruction is not an invariant of the full
   recursive trade system.  Closure failure is nevertheless not an escape
   theorem: at the packet's own depth the displayed destination classes
   remain saturated, so the marked intrinsic transfer has zero cap gain.

The exact remaining positive statement is statewise.  Above the desired
residual level, one must find either an improving legal toggle satisfying
(0.3), or a capacitated matching of many fully draining eight-endpoint
bundles.  Ordinary one-arm Hall expansion does not certify either.

## 1. Exact statewise marginal

Put

\[
 \Omega_>(\mu)=\{v:\mu_v>b\},
 \qquad
 \Omega_\ge(\mu)=\{v:\mu_v\ge b\}.                 \tag{1.1}
\]

Cancel any endpoint occurring with the same multiplicity in \(N_e\) and
\(P_e\).  In the MSW bulk formula the remaining eight endpoints are
distinct.

### Lemma 1.1 (exact four-arm cap derivative)

For one unit four-arm toggle,

\[
 \boxed{
 G_e(\mu):=K_b(\mu)-K_b(\mu+a_e)
 =
 |N_e\cap\Omega_>(\mu)|
 -
 |P_e\cap\Omega_\ge(\mu)|.}                         \tag{1.2}
\]

In particular,

\[
 G_e(\mu)=4
 \quad\Longleftrightarrow\quad
 N_e\subseteq\Omega_>(\mu)
 \ \hbox{and}\
 P_e\cap\Omega_\ge(\mu)=\varnothing.                \tag{1.3}
\]

#### Proof

At a negative endpoint \(v\), replacing \(\mu_v\) by \(\mu_v-1\)
decreases \(K_b\) by one exactly when \(\mu_v>b\).  At a positive
endpoint \(w\), replacing \(\mu_w\) by \(\mu_w+1\) increases \(K_b\) by
one exactly when \(\mu_w\ge b\).  The endpoints are distinct, so the
changes add. \(\square\)

The distinction between \(\Omega_>\) and \(\Omega_\ge\) is essential.
The surrogate

\[
 |N_e\cap\Omega_>|-|P_e\cap\Omega_>|                \tag{1.4}
\]

is an upper bound for \(G_e(\mu)\), but it treats a positive endpoint at
load \(b\) as free.  It is not the exact marginal.

For a legal sequence \(e_1,\ldots,e_s\) whose current old and new targets
remain unit-distinct, let \(\mu^{(j)}\) be the state before the \(j\)-th
toggle.  Exact telescoping gives

\[
 \boxed{
 K_b(\mu^{(0)})-K_b(\mu^{(s)})
 =
 \sum_{j=1}^s
 \left[
 |N_j\cap\Omega_>(\mu^{(j)})|
 -
 |P_j\cap\Omega_\ge(\mu^{(j)})|
 \right].}                                         \tag{1.5}
\]

Consequently a decrease of \(4s-o(s)\) forces (1.3) for all but
\(o(s)\) toggles.  Merely requiring the positive targets not to be
strictly overloaded is insufficient.

For completeness, there is an exact multiset formula.  At one toggle,
cancel common old and new copies, and let \(n_v,p_v\) be the remaining
old and new multiplicities at \(v\); thus \(n_vp_v=0\).  Then

\[
\boxed{
\begin{aligned}
 G_e(\mu)
 &=
 \sum_v\min\{n_v,(\mu_v-b)_+\}\\
 &\quad-
 \sum_v\left[
 p_v-\min\{p_v,(b-\mu_v)_+\}
 \right].
\end{aligned}}                                      \tag{1.6}
\]

Equation (1.2) is the unit-distinct specialization.  Formula (1.6), not
multiset cardinality against a single threshold set, must be used if two
changed windows have the same physical target.

## 2. Correct Hall deficiency for an additive family

Assume that a family \(\mathcal E\) is additive at the chosen depth:
every \(x\in\{0,1\}^{\mathcal E}\) is legal and has load

\[
 \mu^x=\mu+Ax.                                      \tag{2.1}
\]

The exact integer residual is

\[
\boxed{
\begin{aligned}
 \operatorname{Def}^{\mathbb Z}_b(\mu,A)
 =\min\biggl\{&
 \sum_v z_v:
 z_v\ge\mu_v-b+(Ax)_v,\ z_v\ge0,\\
 &x_e\in\{0,1\}\biggr\}.
\end{aligned}}                                      \tag{2.2}
\]

This is the integer cap deficiency; it equals the smallest overload
reachable in the additive cube.

Relaxing \(x_e\in[0,1]\) and dualizing gives:

### Theorem 2.1 (weighted four-arm Hall criterion)

\[
\boxed{
\operatorname{Def}^{\rm frac}_b(\mu,A)
=
\max_{0\le\alpha\le1}
\left[
 \langle\alpha,\mu-b\mathbf1\rangle
 -
 \sum_{e\in\mathcal E}
 \bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
\right].}                                          \tag{2.3}
\]

Thus a fractional cap-feasible selection exists if and only if

\[
\boxed{
\langle\alpha,\mu-b\mathbf1\rangle
\le
\sum_e
\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
\quad\hbox{for every }0\le\alpha\le1.}              \tag{2.4}
\]

#### Proof

Give the constraints

\[
 z_v\ge\mu_v-b+(Ax)_v
\]

dual multipliers \(\alpha_v\ge0\).  Minimizing over \(z_v\ge0\) forces
\(\alpha_v\le1\).  For one column,

\[
 \min_{0\le x_e\le1}
 x_e\langle\alpha,a_e\rangle
 =
 -\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+.
\]

Summing the independent column minima proves (2.3), and zero deficiency
is equivalent to (2.4). \(\square\)

For an indicator \(\alpha=\mathbf1_Z\), (2.3) gives the Hall-type lower
bound

\[
\boxed{
\operatorname{Def}^{\mathbb Z}_b(\mu,A)
\ge
\mu(Z)-b|Z|
-
\sum_e
\bigl(
 |N_e\cap Z|-|P_e\cap Z|
\bigr)_+.}                                          \tag{2.5}
\]

This is useful but not complete: four-arm matrices need not be totally
unimodular, and nonindicator \(\alpha\)'s may be stronger.  In general

\[
 \operatorname{Def}^{\mathbb Z}_b
 =
 \operatorname{Def}^{\rm frac}_b
 +\operatorname{IG}_b,
 \qquad \operatorname{IG}_b\ge0.                    \tag{2.6}
\]

The known three-column triangle gadget has
\(\operatorname{Def}^{\mathbb Z}_1=2\) and
\(\operatorname{Def}^{\rm frac}_1=3/2\).  Therefore there is no exact
ordinary-Hall theorem for arbitrary four-arm columns.  Moreover every
indicator objective in (2.3) is integral, so in that gadget its value is
at most one; the fractional optimum \(3/2\) is attained only by a
nonindicator weight.  Thus indicator Hall cuts are genuinely incomplete
even for the fractional problem.

## 3. The monotone full-drain hypergraph

There is a genuine Hall object for trades which are required to realize
all four units of gain without relays.

At a state \(\mu\), give every overloaded target \(v\) exactly

\[
 e_v=(\mu_v-b)_+                                    \tag{3.1}
\]

excess tokens, and every sub-cap target \(w\) exactly

\[
 d_w=(b-\mu_w)_+                                    \tag{3.2}
\]

slack tokens.  Form a nine-uniform hypergraph \(\mathcal H_\mu\).  In
addition, give every trade one private selector token \(s_e\).
For every applicable trade \(e\) with

\[
 N_e\subseteq\Omega_>(\mu),
 \qquad P_e\cap\Omega_\ge(\mu)=\varnothing,          \tag{3.3}
\]

put in all lifted hyperedges consisting of \(s_e\), one excess token at
each of the four negative endpoints, and one slack token at each of the
four positive endpoints.  The selector prevents one trade from being
chosen twice through different token lifts.

### Theorem 3.1 (exact monotone escape matching)

There is a simultaneous additive selection lowering \(K_b\) by \(4t\)
without any intermediate relay if and only if \(\mathcal H_\mu\) has a
matching of size \(t\).

#### Proof

A matching chooses distinct excess and slack tokens, so no negative target
is used more than its available excess and no positive target more than
its available slack.  Every selected trade therefore contributes exactly
four units of cap decrease, and the contributions add.

Conversely, a relay-free simultaneous selection with total decrease
\(4t\) uses one distinct excess unit at every negative arm and one
distinct slack unit at every positive arm.  Label those units; the
selected bundles become disjoint lifted hyperedges. \(\square\)

Let \(\nu(\mathcal H_\mu)\) be its matching number.  The exact monotone
four-arm deficiency for a desired \(t\) bundles is

\[
 \boxed{
 \Delta_\mu(t)=\bigl(t-\nu(\mathcal H_\mu)\bigr)_+.} \tag{3.4}
\]

Equivalently, its natural fractional \(b\)-matching relaxation is

\[
\begin{aligned}
 \nu^*(\mathcal H_\mu)
 =\max\biggl\{&
 \sum_e x_e:\ 0\le x_e\le1,\\
 &\sum_{e:v\in N_e}x_e\le e_v,\quad
 \sum_{e:w\in P_e}x_e\le d_w
 \biggr\}.
\end{aligned}                                      \tag{3.5}
\]

Its exact LP dual is

\[
\boxed{
\begin{aligned}
 \nu^*(\mathcal H_\mu)
 =\min\biggl\{&
 \sum_v e_v\lambda_v^-+\sum_wd_w\lambda_w^+
 +\sum_e\theta_e:\\
 &\theta_e+\sum_{v\in N_e}\lambda_v^-
 +\sum_{w\in P_e}\lambda_w^+\ge1,\\
 &\lambda^\pm,\theta\ge0
 \biggr\}.
\end{aligned}}                                     \tag{3.6}
\]

This is a nine-uniform lifted hypergraph matching problem, not a bipartite
matching problem.  Ordinary neighborhood Hall conditions, even on every
one-arm projection, are only necessary.  They do not enforce that the
four source arms and four destination arms use one common trade.

## 4. Directional closure and a rigorous obstruction

For a target set \(Z\), define the drain of one direction across \(Z\) by

\[
 D_e(Z)=|N_e\cap Z|-|P_e\cap Z|
       =-\langle\mathbf1_Z,a_e\rangle.              \tag{4.1}
\]

Call \(Z\) **directionally closed** for a family \(\mathcal E\) when

\[
 D_e(Z)\le0\qquad(e\in\mathcal E).                  \tag{4.2}
\]

Thus no allowed direction decreases the total load inside \(Z\).

### Proposition 4.1 (closed-set Hall obstruction)

If \(Z\) is directionally closed, then every additive selection satisfies

\[
 (\mu+Ax)(Z)\ge\mu(Z).                               \tag{4.3}
\]

Consequently

\[
 \boxed{
 K_b(\mu+Ax)
 \ge\bigl(\mu(Z)-b|Z|\bigr)_+.}                     \tag{4.4}
\]

#### Proof

Equation (4.2) says
\(\langle\mathbf1_Z,a_e\rangle\ge0\) for every column.  Sum over the
selected columns to obtain (4.3).  If the total load on \(Z\) exceeds
\(b|Z|\), at least that excess contributes to \(K_b\). \(\square\)

For a nonlinear recursive trade system, the exact statewise version is:
if the current direction at every reachable state \(\nu\) obeys

\[
 D_e^\nu(Z)\le0,                                    \tag{4.5}
\]

then \(\nu(Z)\) is nondecreasing along every legal trade sequence, and
(4.4) remains valid.  This is a genuine global obstruction.  Verifying
(4.5) only at the initial state is not sufficient.

## 5. Are fixed invisible-block targets closed?

There are two different trade scales.

### 5.1 Trades closed inside the same hole: yes

Let \(J\) be the \(2r\) coordinates of a size-\(r\) hole and let \(O\)
be the exterior coordinates fixed throughout its slab.  Every closed
substitution which preserves its two complementary boundary states has

\[
 \bigcap_tX'_t=O.                                   \tag{5.1}
\]

Therefore all Catalan fillings in that hole retain the same invisible
target \(O\).  At the invisible-target layer, every such internal trade
has zero signed coordinate on the target \(O\).  The singleton

\[
 Z_O=\{O\}                                          \tag{5.2}
\]

is directionally closed, in fact invariant, under the same-hole
directions.

This is the exact statewise obstruction behind closed one-hole
substitutions: if \(\mu(O)>b\), no combination of those directions can
remove any of that excess.

### 5.2 One-level-up parent rectangle trades: no

The certified parent rectangle changes one nested filling from

\[
 O\cup\{2\}\longrightarrow O\cup\{4\}.              \tag{5.3}
\]

The two targets are distinct, and the full four-arm column has distinct
endpoints in the bulk.  Hence for

\[
 Z=\{O\cup\{2\}\}
\]

the parent direction has

\[
 D_e(Z)=1.                                         \tag{5.4}
\]

Thus a fixed invisible fibre is not closed under the full recursive trade
directions.  The parent coordinate imported through the boundary is
exactly the escape from the same-hole invariant.

This is a rigorous escape from **support invariance**, but not yet from
cap overload.  At the packet's own depth the canonical local loads on the
marked classes satisfy

\[
 (\operatorname{Cat}_r,\operatorname{Cat}_{r-1},
   \operatorname{Cat}_{r-1})
 \longmapsto
 (\operatorname{Cat}_r-\operatorname{Cat}_{r-1},
  2\operatorname{Cat}_{r-1},
  \operatorname{Cat}_{r-1}).                       \tag{5.5}
\]

At the critical cutoff \(\operatorname{Cat}_r\ge4b\), every displayed
class remains above \(b\).  Therefore the marked intrinsic transfer has
exact cap gain zero.  Any gain must come from the other cyclic arms and
from their statewise cap status.

The argument proves fibrewise nonclosure.  It does not prove that the
union of all size-\(r\) invisible targets over all parent contexts is
nonclosed; a positive endpoint of one parent may be the invisible target
of another.  That global union requires a separate incidence census.

## 6. A statewise escape theorem and its obstruction

Let \(\mathscr G\) be the directed graph of physically legal factor states,
with one directed edge for every currently applicable toggle.  Define

\[
 \Gamma_b(\mu)=
 \max_{e\ {\rm applicable\ at}\ \mu}G_e(\mu),       \tag{6.1}
\]

where \(G_e\) is the exact marginal (1.2).
For a toggle with repeated current endpoints, \(G_e\) means the multiset
marginal (1.6).

### Theorem 6.1 (greedy statewise escape)

Fix \(\kappa\ge0\).  If

\[
 K_b(\mu)>\kappa
 \quad\Longrightarrow\quad
 \Gamma_b(\mu)\ge1                                 \tag{6.2}
\]

at every state reachable from the initial factor, then a legal sequence
reaches a state with \(K_b\le\kappa\) after at most

\[
 K_b(\mu^{(0)})-\kappa                              \tag{6.3}
\]

toggles.

#### Proof

While the overload exceeds \(\kappa\), choose a toggle with positive
integer gain.  Each step lowers \(K_b\) by at least one.  Hence the process
cannot cycle and must terminate after at most (6.3) steps. \(\square\)

Conversely, a state with

\[
 \boxed{
 G_e(\mu)\le0
 \quad\hbox{for every applicable }e}                \tag{6.4}
\]

is a one-toggle cap-local minimum.  For unit-distinct endpoints this is
the exact statewise obstruction:

\[
 |N_e\cap\Omega_>(\mu)|
 \le
 |P_e\cap\Omega_\ge(\mu)|
 \quad(e\ {\rm applicable}).                       \tag{6.5}
\]

A local minimum need not be a global obstruction, because a temporarily
nonimproving toggle may open later draining moves.  A directionally closed
set satisfying (4.5), by contrast, is a genuine obstruction to every
sequence.

## 7. Exact remaining criterion for the MSW parent family

The fixed invisible fibres themselves do not block parent trades.
Therefore a negative theorem must exhibit either:

1. a larger target set \(Z\) satisfying the reachable-state closure
   condition (4.5) and carrying super-cap mass; or
2. a reachable cap-local minimum satisfying (6.5), together with an
   argument that every exit from its basin incurs too much overload.

A positive theorem may take either of two forms.

1. **Statewise escape:** prove (6.2) outside an \(o(W)\) cap tail.
2. **Bulk monotone escape:** prove

   \[
    \nu(\mathcal H_\mu)
    \ge {K_b(\mu)-o(W)\over4}                       \tag{7.1}
   \]

   at a sequence of additive states, with a rounding theorem controlling
   the hypergraph matching gap.

At the asymptotically critical parent scale, an elimination theorem must
use almost every toggle with exact gain four.  By (1.3), this means all
four current negative targets are strictly overloaded and all four
current positive targets are strictly below the cap for all but
\(o(M)\) toggles.  The existing parent-context theorem certifies only one
negative arm.  It neither proves (7.1) nor constructs a closed-set
obstruction.

This is the correct Hall/deficiency frontier.  The problem is a ganged
eight-endpoint hypergraph matching with state-dependent cap thresholds,
not four independent one-arm flows.
