# Lane S7: exact spacetime fusion and the triangular tube obstruction for CRHL

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Result and exact boundary

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\). This report proves two facts about the surviving
nonstandard constrained recursive Hall lift.

First, recursive compatibility has an exact static form. Every integral
height-\(H\) recursive lift is equivalent to one pair of deletion-symbol
tableaux \((\alpha_q,\beta_q)\). Across a retained identity edge
\(v\to w\), the tableaux obey the transport laws

\[
 \alpha_{q+1}(v)=\alpha_q(w),\qquad
 \beta_{q+1}(w)=\beta_q(v).
 \tag{0.1}
\]

The depth-zero rule is the corresponding base condition. Rankwise
bijectivity makes the two remaining rotor inequalities automatic. Thus
successive forced-target boundary matchings really do fuse into one
integral band SCD; there is no additional permutation holonomy or merger
condition hidden after the matchings have been chosen.

Second, the choices at different layers are not independent. A lower
depth-\(q\) endpoint transports information through a triangular tube of
earlier edges. If \(k_s\) inherited edges are first cut at layer \(s\),
and \(\Delta_q^-\), \(\Delta_q^+\) are the exact lower and upper canonical
tube defects defined below, then every recursive lift satisfies

\[
 \boxed{
 \Delta_q^\pm\le
 \sum_{s=0}^{q-1}(q-s)k_s
 }
 \qquad(1\le q\le H).
 \tag{0.2}
\]

This gives the global dual lower bound

\[
 \boxed{
 K_H:=\sum_{s=0}^{H-1}k_s
 \ge
 \max_{\theta^\pm\in\mathcal P_H}
 \sum_{q=1}^H
 \bigl(\theta_q^-\Delta_q^-+
       \theta_q^+\Delta_q^+\bigr),
 }
 \tag{0.3}
\]

where

\[
 \mathcal P_H=
 \left\{\theta_q^\pm\ge0:
 \sum_{q=s+1}^H(q-s)
       (\theta_q^-+\theta_q^+)\le1
 \text{ for every }0\le s<H\right\}.
 \tag{0.4}
\]

For the exact odd-cut forest, with its
\(B=W/(m+1)\) paths and globally contiguous radius blocks, the lower and
upper baseline tube families at depth \(q\) both have the floor-exact
integer baseline

\[
 \boxed{
 |\mathcal B_q^-|\ge N_q-qB,
 \qquad
 |\mathcal B_q^+|\ge N_q-qB.
 }
 \tag{0.5}
\]

The floor terms in (0.5) are literal integer counts: \(qB\) comes from the
last or first \(q\) vertices of the active suffix run on each of the \(B\)
open paths.  More exactly, if those run lengths are \(\ell_i\), the common
certified subfamily for either sign has size
\(N_q-\sum_i\min\{q,\ell_i\}\).

Consequently the target estimate

\[
 K_H=o(W/H)
 \tag{0.6}
\]

forces

\[
 \Delta_q^\pm=o(qW/H)
 \quad\text{uniformly for }1\le q\le H,
 \tag{0.7}
\]

and

\[
 \sum_{q=1}^H(\Delta_q^-+\Delta_q^+)=o(WH).
 \tag{0.8}
\]

Thus a successful recursive Hall construction must be simultaneously
near-rainbow on \(N_q-o(W)\) genuine length-\(q\) path tubes at every
Gaussian depth, not merely optimal in each independently re-created
one-layer forced-target instance.

This is a proved global dynamic obstruction and a proved fusion theorem.
It does **not** prove (0.6). The remaining assertion is existence of a
sequence of boundary SDRs whose outputs continue to satisfy the tube
defects (0.7), together with the boundary Hall conditions, through all
\(H\) layers. No constant-one conclusion is claimed.

## 1. Recursive data and notation

Let \(\mathcal V_0\) be a set of \(W\) chain identities. Give each
\(v\in\mathcal V_0\) a distinct middle mask

\[
 X_v\in\binom{[n]}m.
\]

Let \(F_0\) be a directed path forest on these identities. Every edge
\(e=v\to w\) is a Johnson edge, so there are unique coordinates
\(x_e\in X_v\), \(y_e\notin X_v\) with

\[
 X_w=X_v-\{x_e\}+\{y_e\}.
 \tag{1.1}
\]

Choose nested active identity sets

\[
 \mathcal V_0\supset\mathcal V_1\supset\cdots
 \supset\mathcal V_H,
 \qquad |\mathcal V_q|=N_q.
 \tag{1.2}
\]

The identity \(v\) is continued through depth \(q\) exactly when
\(v\in\mathcal V_q\).

Write \(E_{-1}=E(F_0)\). At stage \(q\), first restrict the already
retained radius-\(q\) forest to \(\mathcal V_{q+1}\), then delete
\(k_q\) further identity edges. Let \(E_q\) be the retained edge set
which is to lift from radius \(q\) to radius \(q+1\). Thus

\[
 E_q\subseteq E_{q-1},
 \qquad
 E_q\subseteq\mathcal V_{q+1}\times\mathcal V_{q+1},
 \tag{1.3}
\]

and every \((\mathcal V_{q+1},E_q)\) is a directed path forest. An edge,
once deleted, is never reintroduced. This is exactly the no-merger
recursive architecture.

For bookkeeping, define the structural edge set which would be available
at layer \(q\) in the absence of extra deletions by

\[
 G_q=E(F_0)[\mathcal V_{q+1}].
 \tag{1.4}
\]

Let \(D_s\subseteq G_s\) be the identity edges first deleted at layer
\(s\). The sets \(D_s\) are disjoint and

\[
 |D_s|=k_s,
 \qquad
 E_q=G_q\setminus\bigcup_{s=0}^qD_s.
 \tag{1.5}
\]

In (1.5), an edge in \(D_s\) which no longer has both endpoints active at
depth \(q+1\) is absent from both sides; equivalently one may intersect the
union with \(G_q\). Nothing below counts such an edge twice.

## 2. The exact spacetime-tableau theorem

For \(v\in\mathcal V_q\), let \(L_q(v)\) be its lower endpoint and let
\(R_q(v)\) be the complement of its upper endpoint. Both have size
\(m-q\). At depth zero put

\[
 L_0(v)=X_v,
 \qquad
 R_0(v)=[n]\setminus X_v.
 \tag{2.1}
\]

An extension through the next layer removes symbols

\[
 \alpha_{q+1}(v)\in L_q(v),
 \qquad
 \beta_{q+1}(v)\in R_q(v)
 \tag{2.2}
\]

and sets

\[
 L_{q+1}(v)=L_q(v)-\{\alpha_{q+1}(v)\},
 \qquad
 R_{q+1}(v)=R_q(v)-\{\beta_{q+1}(v)\}.
 \tag{2.3}
\]

### Theorem 2.1 (global spacetime fusion)

Fix the recursive data (1.1)--(1.3). There is one integral symmetric-chain
decomposition of the depth-\(H\) central band, on the chain identities
\(\mathcal V_0\), which retains every identity edge in \(E_q\) as a
radius-\(q\) directed rotor edge for every \(0\le q<H\), if and only if
there are symbols \(\alpha_q(v),\beta_q(v)\) satisfying all of the
following conditions.

1. **Membership and endpoint recursion.** Equations (2.2)--(2.3) hold.

2. **Exact rank ownership.** For every \(0\le q\le H\), both maps

   \[
   v\longmapsto L_q(v),
   \qquad
   v\longmapsto R_q(v)
   \tag{2.4}
   \]

   are bijections from \(\mathcal V_q\) onto
   \(\binom{[n]}{m-q}\).

3. **Depth-zero transport.** If \(e=v\to w\in E_0\), then

   \[
   \alpha_1(v)=x_e,
   \qquad
   \beta_1(w)=x_e.
   \tag{2.5}
   \]

4. **Positive-depth transport.** If \(1\le q<H\) and
   \(v\to w\in E_q\), then

   \[
   \boxed{
   \alpha_{q+1}(v)=\alpha_q(w),
   \qquad
   \beta_{q+1}(w)=\beta_q(v).
   }
   \tag{2.6}
   \]

For such a tableau, the radius-\(q\) state of identity \(v\) is exactly

\[
 \omega_q(v)=
 \bigl(
 L_q(v);
 \alpha_q(v),\ldots,\alpha_1(v),
 \beta_1(v),\ldots,\beta_q(v);
 R_q(v)
 \bigr).
 \tag{2.7}
\]

In particular, independently selected lower and upper boundary matchings
at successive layers fuse into one integral band SCD whenever their output
endpoints are used as the input endpoints at the next layer. There is no
further cross-layer compatibility equation beyond (2.5)--(2.6).

#### Proof

Assume first that the tableaux exist. Membership in (2.2) shows that all
entries in (2.7) are disjoint and partition \([n]\). Indeed one starts
from the partition \(X_v\sqcup X_v^c\), and at each extension removes one
symbol from the lower block and one from the residual block and places the
two removed symbols at the two ends of the singleton queue.

The state (2.7) is the central state of the symmetric chain on identity
\(v\). Extending from depth \(q-1\) to depth \(q\) adds only the two new
boundary masks

\[
 L_q(v),
 \qquad
 [n]\setminus R_q(v).
\]

By (2.4), these masks cover ranks \(m-q\) and \(m+q\), respectively,
exactly once. Induction on \(q\) proves that all chains together form one
integral saturated SCD of the entire depth-\(H\) band.

It remains to check the rotor edges. At depth zero, let
\(e=v\to w\in E_0\). The exact radius-zero lift criterion requires

\[
 \alpha_1(v)=x_e,
 \qquad
 \beta_1(w)=x_e,
 \qquad
 \alpha_1(w)\ne y_e,
 \qquad
 \beta_1(v)\ne y_e.
 \tag{2.8}
\]

The first two conditions are (2.5). If
\(\alpha_1(w)=y_e\), then (1.1) gives

\[
 L_1(w)=X_w-y_e=X_v-x_e=L_1(v),
\]

contrary to injectivity in (2.4). If \(\beta_1(v)=y_e\), then

\[
 R_1(v)=X_v^c-y_e
 =X_w^c-x_e=R_1(w),
\]

again contrary to injectivity. Thus the radius-zero edge lifts.

Now let \(q\ge1\), assume inductively that \(v\to w\in E_{q-1}\)
is a radius-\(q\) rotor edge, and suppose it also lies in \(E_q\). In the
state (2.7), the coordinate removed from the lower block by that rotor edge
is the first singleton of the target, namely \(\alpha_q(w)\); the last
singleton of the source is \(\beta_q(v)\). The exact one-edge lift theorem
therefore requires

\[
 \alpha_{q+1}(v)=\alpha_q(w),
 \qquad
 \beta_{q+1}(w)=\beta_q(v),
 \tag{2.9}
\]

together with two non-equalities. Equations (2.9) are exactly (2.6), and
the two non-equalities are automatic from injectivity of the two maps at
depth \(q+1\), by the same duplicate-endpoint argument as at depth zero.
Thus every selected edge lifts.

Conversely, start with one recursive integral band SCD retaining the
specified edges. Define \(L_q,R_q\) from its endpoints and define
\(\alpha_q,\beta_q\) as the unique symbols removed at each extension.
Exact rank coverage gives (2.4). The one-edge lift criterion gives (2.5)
at depth zero and (2.6) at every positive depth. Hence the tableau
conditions are necessary. \(\square\)

## 3. Boundary SDRs and why sequential choices really compose

Theorem 2.1 has an equivalent boundary-matching form which isolates the
only choices left after the retained edge set is fixed.

Suppose the tableaux have been constructed through depth \(q\), choose
\(\mathcal V_{q+1}\), and prescribe \(E_q\). Let

\[
 T_q^-={v\in\mathcal V_{q+1}:\operatorname{outdeg}_{E_q}(v)=0\},
\]

\[
 T_q^+={v\in\mathcal V_{q+1}:\operatorname{indeg}_{E_q}(v)=0\}.
 \tag{3.1}
\]

These are the terminal and initial vertices of the retained active paths.
For \(v\notin T_q^-\), let \(v\to w\) be its outgoing edge and define the
forced lower target

\[
 \Lambda_q(v)=
 \begin{cases}
 X_v-\{x_{vw}\},&q=0,\\
 L_q(v)-\{\alpha_q(w)\},&q\ge1.
 \end{cases}
 \tag{3.2}
\]

For \(w\notin T_q^+\), let \(v\to w\) be its incoming edge and define

\[
 P_q(w)=
 \begin{cases}
 R_0(w)-\{x_{vw}\},&q=0,\\
 R_q(w)-\{\beta_q(v)\},&q\ge1.
 \end{cases}
 \tag{3.3}
\]

### Theorem 3.1 (exact boundary-completion criterion)

The tableaux through depth \(q\) extend through depth \(q+1\), preserving
every edge of \(E_q\), if and only if all four conditions below hold.

1. The forced lower targets \(\Lambda_q(v)\), \(v\notin T_q^-\), are
   pairwise distinct.
2. The forced upper-complement targets \(P_q(w)\), \(w\notin T_q^+\),
   are pairwise distinct.
3. Put

   \[
   \mathcal M_q^-=
   \binom{[n]}{m-q-1}
   \setminus\{\Lambda_q(v):v\notin T_q^-\}.
   \tag{3.4}
   \]

   The bipartite graph

   \[
   v\sim S
   \quad\Longleftrightarrow\quad
   v\in T_q^-,\ S\in\mathcal M_q^-,\ S\subset L_q(v)
   \tag{3.5}
   \]

   has a perfect matching.
4. With

   \[
   \mathcal M_q^+=
   \binom{[n]}{m-q-1}
   \setminus\{P_q(w):w\notin T_q^+\},
   \tag{3.6}
   \]

   the graph

   \[
   w\sim S
   \quad\Longleftrightarrow\quad
   w\in T_q^+,\ S\in\mathcal M_q^+,\ S\subset R_q(w)
   \tag{3.7}
   \]

   has a perfect matching.

When these conditions hold, the two matchings in (3.5) and (3.7) may be
chosen independently. Their outputs define \(\alpha_{q+1}\) and
\(\beta_{q+1}\), and these outputs may immediately be used as the input to
the next layer. Repeating this operation gives exactly the global tableau
of Theorem 2.1.

#### Proof

Every nonterminal lower choice is forced by (2.5) or (2.6), and its new
lower endpoint is (3.2). Every terminal is unconstrained by an outgoing
retained edge. Since \((\mathcal V_{q+1},E_q)\) is a path forest,

\[
 |T_q^-|=|\mathcal V_{q+1}|-|E_q|.
\]

If the forced targets are distinct, the same number of rank-
\((m-q-1)\) targets is missing in (3.4). Matching a terminal \(v\) to
\(S\subset L_q(v)\) uniquely defines

\[
 \alpha_{q+1}(v)=L_q(v)\setminus S.
\]

Thus (3.5) is necessary and sufficient for the lower endpoint map to be a
bijection. The upper argument is identical. The lower and upper variables
occur in disjoint matching systems, and endpoint injectivity supplies the
remaining rotor inequalities by Theorem 2.1. Hence the two matchings are
independent and the resulting layer is a valid input for the next one.
\(\square\)

The theorem proves actual fusion, but it does not assert that the two
boundary graphs remain matchable after arbitrary earlier choices. That is
the genuinely dynamic existence issue.

## 4. Canonical tubes and transported targets

The transport equations have a useful closed form.

### Definition 4.1 (baseline lower and upper tubes)

Fix \(1\le q\le H\).

A **baseline lower \(q\)-tube** is a directed path

\[
 \tau=(v_0\to v_1\to\cdots\to v_q)
 \tag{4.1}
\]

in \(F_0\) such that, writing \(e_t=v_t\to v_{t+1}\),

\[
 e_t\in G_{q-1-t}
 \qquad(0\le t<q).
 \tag{4.2}
\]

Its canonical lower target is

\[
 I(\tau)=\bigcap_{t=0}^qX_{v_t}.
 \tag{4.3}
\]

A **baseline upper \(q\)-tube** is a directed path

\[
 \tau=(v_{-q}\to\cdots\to v_{-1}\to v_0)
 \tag{4.4}
\]

such that, for \(e_t=v_{-t-1}\to v_{-t}\),

\[
 e_t\in G_{q-1-t}
 \qquad(0\le t<q).
 \tag{4.5}
\]

Its canonical upper-complement target is

\[
 J(\tau)=[n]\setminus\bigcup_{t=0}^qX_{v_{-t}}.
 \tag{4.6}
\]

The reversed level indices in (4.2) and (4.5) are essential. The edge
nearest the endpoint must survive through layer \(q-1\); the farthest edge
need only survive the depth-zero lift.

Call a lower tube rank-good when \(|I(\tau)|=m-q\), and an upper tube
rank-good when \(|J(\tau)|=m-q\), equivalently when the union in (4.6)
has size \(m+q\).

### Lemma 4.2 (tube transport)

If no identity edge of a baseline lower tube \(\tau\) is cut before the
last layer at which (4.2) requires it, then

\[
 L_q(v_0)=I(\tau).
 \tag{4.7}
\]

If the analogous condition holds for an upper tube, then

\[
 R_q(v_0)=J(\tau).
 \tag{4.8}
\]

In particular every surviving baseline tube is rank-good, and the
canonical targets of all surviving lower tubes are pairwise distinct; the
same is true of all surviving upper tubes.

#### Proof

For the lower tube, write \(x_t=x_{e_t}\). Since \(e_{q-1}\in E_0\),
(2.5) gives

\[
 \alpha_1(v_{q-1})=x_{q-1}.
\]

Since \(e_{q-2}\in E_1\), transport gives

\[
 \alpha_2(v_{q-2})=\alpha_1(v_{q-1})=x_{q-1}.
\]

Continuing diagonally, and repeating the same argument for every shorter
suffix, gives

\[
 \alpha_j(v_0)=x_{j-1}
 \qquad(1\le j\le q).
 \tag{4.9}
\]

Therefore

\[
 L_q(v_0)=X_{v_0}\setminus\{x_0,\ldots,x_{q-1}\}.
 \tag{4.10}
\]

Membership in (2.2) makes these \(q\) symbols distinct elements of
\(X_{v_0}\). Along the Johnson path, an original coordinate belongs to
every \(X_{v_t}\) exactly when it is never one of the removed coordinates
\(x_0,\ldots,x_{q-1}\). A coordinate inserted later is absent from
\(X_{v_0}\) and hence cannot lie in the intersection. Thus (4.10) is
exactly (4.3), proving (4.7).

For the upper tube, transport runs in the opposite direction and gives

\[
 \beta_j(v_0)=x_{-j}
 \qquad(1\le j\le q),
\]

where \(x_{-j}\) is removed on
\(v_{-j}\to v_{-j+1}\). Hence

\[
 R_q(v_0)
 =X_{v_0}^c\setminus\{x_{-1},\ldots,x_{-q}\}
 =[n]\setminus\bigcup_{t=0}^qX_{v_{-t}},
\]

which is (4.8). Finally, (2.4) makes the actual endpoints at depth \(q\)
pairwise distinct. \(\square\)

## 5. The triangular dynamic obstruction

Let \(\mathcal B_q^-\) and \(\mathcal B_q^+\) be the baseline lower and
upper tube families. For a lower rank-good target
\(S\in\binom{[n]}{m-q}\), put

\[
 \mu_q^-(S)=
 |\{\tau\in\mathcal B_q^-:I(\tau)=S\}|,
\]

and define \(\mu_q^+\) analogously using \(J\). Define the exact tube
defects

\[
 \Delta_q^-=
 |\{\tau\in\mathcal B_q^-:|I(\tau)|\ne m-q\}|
 +\sum_{S\in\binom{[n]}{m-q}}
      (\mu_q^-(S)-1)_+,
 \tag{5.1}
\]

\[
 \Delta_q^+=
 |\{\tau\in\mathcal B_q^+:|J(\tau)|\ne m-q\}|
 +\sum_{S\in\binom{[n]}{m-q}}
      (\mu_q^+(S)-1)_+.
 \tag{5.2}
\]

Thus \(\Delta_q^\pm\) is exactly the minimum number of baseline tubes of
that sign which must be discarded before all remaining tubes are rank-good
and have distinct canonical targets.

### Theorem 5.1 (triangular cut inequality)

Every integral recursive lift satisfying Theorem 2.1 obeys

\[
 \boxed{
 \Delta_q^-\le\sum_{s=0}^{q-1}(q-s)k_s,
 \qquad
 \Delta_q^+\le\sum_{s=0}^{q-1}(q-s)k_s
 }
 \tag{5.3}
\]

for every \(1\le q\le H\).

#### Proof

Fix a first-cut edge \(e\in D_s\). Consider lower baseline \(q\)-tubes
which cease to survive because of this cut. If \(e\) occurs at offset
\(t\) in (4.1), the tube requires \(e\) through layer \(q-1-t\). The cut
at layer \(s\) can matter only when

\[
 s\le q-1-t,
 \qquad\text{or equivalently}\qquad
 0\le t\le q-1-s.
 \tag{5.4}
\]

For each fixed offset \(t\), an edge of a directed path forest belongs to
at most one directed length-\(q\) path with that edge at offset \(t\).
Thus \(e\) can spoil at most \(q-s\) baseline lower \(q\)-tubes. Summing
over the \(k_s\) first cuts at layer \(s\) and then over
\(0\le s<q\), at most the right side of (5.3) lower tubes fail to
survive.

By Lemma 4.2, all surviving lower tubes are rank-good and their canonical
targets are pairwise distinct. From a multiset with defect \(\Delta_q^-\),
one must delete at least \(\Delta_q^-\) elements to obtain a rank-good
simple set. This proves the lower inequality. The upper tubes use the same
offset count in the reverse direction and give the upper inequality.
\(\square\)

The factor \(q-s\) is not a heuristic Lipschitz constant. It is the exact
number of possible offsets (5.4) in the triangular transport cone.

### Corollary 5.2 (global endpoint-potential dual)

Let \(\mathcal P_H\) be (0.4). Then every integral recursive lift obeys
(0.3).

#### Proof

Multiply the two inequalities in (5.3) by
\(\theta_q^-\) and \(\theta_q^+\), sum over \(q\), and interchange the
order of summation. The coefficient of \(k_s\) is

\[
 \sum_{q=s+1}^H(q-s)(\theta_q^-+\theta_q^+)\le1.
\]

Hence the weighted defect sum is at most \(K_H\). Maximizing over
\(\mathcal P_H\) proves (0.3). \(\square\)

Equivalently, (0.3) is the dual of the fractional covering problem

\[
 \min\left\{\sum_{s=0}^{H-1}z_s:
 z_s\ge0,
 \ \sum_{s<q}(q-s)z_s\ge\Delta_q^-,
 \ \sum_{s<q}(q-s)z_s\ge\Delta_q^+
 \right\}.
 \tag{5.5}
\]

The actual integer vector \((k_s)\) is feasible in (5.5). Thus (0.3) is
the sharp lower bound obtainable from all triangular defect constraints
simultaneously. It is not asserted that every feasible vector in (5.5) is
realizable by a recursive SCD.

Useful exact consequences are

\[
 K_H\ge
 \left\lceil\frac{\Delta_q^\pm}{q}\right\rceil
 \qquad(1\le q\le H),
 \tag{5.6}
\]

and

\[
 K_H\ge
 \frac1{H(H+1)}
 \sum_{q=1}^H(\Delta_q^-+\Delta_q^+).
 \tag{5.7}
\]

For (5.7), take
\(\theta_q^-=\theta_q^+=1/[H(H+1)]\); at \(s=0\) the capacity sum is
one, and at every later \(s\) it is smaller.

## 6. Exact odd-cut baseline size

We now specialize only the counting of baseline tubes. Let \(F_0\) have
\(P\) directed path components. For \(0\le s<H\), let

\[
 c_s=
 |\{v\to w\in E(F_0):
   |\{v,w\}\cap\mathcal V_{s+1}|=1\}|
 \tag{6.1}
\]

be the number of initial-forest edges crossing the active/inactive cut at
stage \(s\).

### Lemma 6.1 (floor-exact baseline count)

For every \(1\le q\le H\),

\[
 |\mathcal B_q^-|\ge
 N_q-qP-\sum_{s=0}^{q-1}c_s,
 \qquad
 |\mathcal B_q^+|\ge
 N_q-qP-\sum_{s=0}^{q-1}c_s.
 \tag{6.2}
\]

#### Proof

There are \(N_q\) possible lower tube starts \(v_0\in\mathcal V_q\).
At most \(qP\) of them lie among the last \(q\) vertices of their initial
path and therefore have no directed length-\(q\) continuation.

Take a remaining start for which (4.2) fails, and let \(t\) be the least
failed offset. For every \(j<t\), the edge
\(v_j\to v_{j+1}\) lies in \(G_{q-1-j}\), so in particular

\[
 v_t\in\mathcal V_{q-t+1}\subseteq\mathcal V_{q-t}.
\]

The failure at offset \(t\) therefore means

\[
 v_t\in\mathcal V_{q-t},
 \qquad
 v_{t+1}\notin\mathcal V_{q-t}.
\]

Thus \(v_t\to v_{t+1}\) is counted by
\(c_{q-t-1}\). For a fixed crossing edge and its forced offset
\(t=q-s-1\), there is at most one path start. Hence the failed starts
inject into the disjoint list of crossing-edge occurrences over
\(0\le s<q\), proving the lower bound. The upper bound follows by
reversing initial and terminal directions. \(\square\)

For the exact odd-cut input,

\[
 P=B=\operatorname{Cat}_m=\frac{W}{m+1}.
 \tag{6.3}
\]

List the vertices of each path in its directed order, concatenate those
\(B\) directed lists, and assign the
radius labels in globally contiguous blocks of exact sizes

\[
 N_0-N_1,\ N_1-N_2,\ldots,\ N_{H-1}-N_H,\ N_H.
 \tag{6.4}
\]

Then \(\mathcal V_{s+1}\) is one suffix of that concatenated order. It
crosses at most one genuine initial-forest edge, so

\[
 c_s\le1.
 \tag{6.5}
\]

There is a sharper specialization than (6.2), simultaneously for both
orientations.  Put

\[
 \ell_i=|\mathcal V_q\cap V(P_i)|
 \qquad(1\le i\le B),
\]

where \(P_i\) is the \(i\)-th directed path.  The intersection with each
path is a suffix run of length \(\ell_i\).  Every directed \(q\)-window
wholly inside such a run is a baseline lower tube; read backward from its
last vertex, the same internal window is a baseline upper tube.  Indeed
all its vertices lie in \(\mathcal V_q\subseteq\mathcal V_{q-t}\) at
every required earlier level.  There are exactly

\[
 \sum_{i=1}^B(\ell_i-q)_+
 =N_q-\sum_{i=1}^B\min\{q,\ell_i\}
 \ge N_q-qB
 \tag{6.6}
\]

such internal windows.  Consequently the floor-exact integer bounds are

\[
 \boxed{
 |\mathcal B_q^-|\ge N_q-qB,
 \qquad
 |\mathcal B_q^+|\ge N_q-qB.
 }
 \tag{6.7}
\]

For \(q\le H=\lceil A\sqrt m\rceil\),

\[
 qB
 \le
 \frac{(A\sqrt m+1)W}{m+1}
 =O_A(W/\sqrt m)
 =o(W).
 \tag{6.8}
\]

Thus every canonical defect \(\Delta_q^\pm\) in (5.1)--(5.2) is measured
on \(N_q-o(W)\) genuine tube occurrences uniformly across the clipped
Gaussian band.

For an odd-cut wreath path, the coordinates removed on its middle edges
are distinct. Hence every baseline tube of length \(q\le H<m\) is
rank-good. In this case (5.1)--(5.2) reduce exactly to duplicate excesses
of the lower intersections and complementary upper unions; no rank-bad
term is present.

## 7. Quantitative implication for CRHL

Assume the desired recursive deletion estimate

\[
 K_H=o(W/H).
 \tag{7.1}
\]

Equation (5.6) gives, uniformly for \(1\le q\le H\),

\[
 \Delta_q^\pm
 \le qK_H
 =o(qW/H).
 \tag{7.2}
\]

At \(q=1\), this is the previously necessary vanishing meet/join defect
at scale \(o(W/H)\). At a Gaussian depth \(q\asymp H\), it requires
\(o(W)\) duplicate excess on a baseline family of size
\(N_q-o(W)=\Theta_A(W)\).

Equation (5.7) yields

\[
 \sum_{q=1}^H(\Delta_q^-+\Delta_q^+)
 \le H(H+1)K_H=o(WH).
 \tag{7.3}
\]

Therefore small defect at a few selected layers is insufficient. The
average lower-plus-upper duplicate excess over the whole Gaussian window
must be \(o(W)\).

For the odd-cut paths all tubes are rank-good.  If \(S_q^-\) and
\(S_q^+\) denote the numbers of distinct canonical targets represented by
the two baseline families, then exactly

\[
 S_q^\pm=|\mathcal B_q^\pm|-\Delta_q^\pm.
 \tag{7.4}
\]

Combining (5.3), (6.7), and (7.4) gives the finite support bounds

\[
 \boxed{
 S_q^\pm\ge
 N_q-qB-\sum_{s=0}^{q-1}(q-s)k_s.
 }
 \tag{7.5}
\]

Thus (7.1) forces

\[
 S_q^\pm=N_q-o(W)
 \tag{7.6}
\]

uniformly for \(q\le H\).  This is stronger than saying that the current
one-layer forced targets have a large matching: the represented targets in
(7.6) are the literal intersections and complementary unions transported
from one common middle path history through all preceding layers.

Conversely, (7.2)--(7.3) are only necessary. Even zero canonical duplicate
excess does not guarantee the terminal and initial boundary matchings
(3.5) and (3.7). A missing target can avoid every legal terminal cap. The
boundary SDRs are exactly where Boolean extendability loss remains.

## 8. The exact residual theorem

Theorem 2.1 proves that there is no unspecified global gluing operation
left after a compatible sequence of boundary SDRs is chosen. Theorems 5.1
and 6.1 show what every such sequence must preserve in its future light
cones. The remaining positive statement can now be stated without
independent-layer ambiguity.

> **Dynamic boundary-SDR theorem \(\mathrm{DBSDR}_A\) -- UNPROVED.**
> For every fixed \(A>0\), for all sufficiently large \(m\), the exact
> odd-cut forest with the contiguous active sets (6.4) admits nested
> retained edge sets \(E_q\) and, at every layer, perfect matchings in the
> two boundary graphs (3.5) and (3.7), such that
> \[
> \sum_{q=0}^{H-1}k_q=o(W/H),
> \qquad H=\lceil A\sqrt m\rceil.
> \tag{8.1}
> \]

This statement is equivalent to CRHL for the present no-merger,
globally-contiguous odd-cut architecture: Theorem 3.1 composes the SDRs
into the spacetime tableau, and Theorem 2.1 composes the tableau into one
integral band SCD. Conversely every CRHL lift supplies exactly these
boundary SDRs.

The new obstruction says that any proof of \(\mathrm{DBSDR}_A\) must
control the entire triangular defect vector, not only the one-layer
quantities optimized on separately chosen parent states. In particular it
must establish (at least)

\[
 \Delta_q^\pm=o(qW/H)
 \quad(1\le q\le H),
 \qquad
 \sum_q(\Delta_q^-+\Delta_q^+)=o(WH),
 \tag{8.2}
\]

for the single evolving history on which it performs the boundary
matchings.

If \(\mathrm{DBSDR}_A\) is proved, the already audited recursive toll
ledger gives

\[
 \widehat\Phi_H
 \le H(H-1)+2H(B+1)+2HK_H=o(W),
\]

and the band-extension theorem gives a full integral SCD. This is only a
conditional implication. Neither \(\mathrm{DBSDR}_A\), RSCD, nor the
constant-one contiguous-OR theorem is proved here.

## 9. Audit checklist

1. **No fractional object.** Every endpoint, tube, matching, edge cut, and
   SCD in the proved statements is integral.
2. **Correct transport direction.** Lower symbols move one edge backward
   at each new layer; upper symbols move one edge forward. This is why the
   near endpoint edge carries level \(q-1\) in (4.2) and (4.5).
3. **Depth-zero exception included.** Equation (2.5), not (2.6), is used
   at the first lift.
4. **Rotor inequalities.** They are not discarded; exact endpoint
   injectivity proves them automatically.
5. **First-cut convention.** A deleted identity edge is charged once, at
   its first deleted layer. Its influence at later depths is the factor
   \(q-s\) in (5.3).
6. **Path-boundary floor.** The baseline loss is exactly bounded by
   \(qP+\sum_{s<q}c_s\).  For the contiguous directed odd-cut order, the
   stronger internal-window count is exactly
   \(N_q-\sum_i\min\{q,\ell_i\}\ge N_q-qB\) for either sign. No
   asymptotic term is hidden in this baseline.
7. **Rank defects retained.** For a general Johnson path, a malformed tube
   is counted explicitly in (5.1)--(5.2). Odd-cut wreath paths make this
   term zero, but the general theorem does not assume that.
8. **Implication scope.** The report proves global fusion conditional on
   the boundary SDR sequence and proves a new necessary dynamic dual. It
   does not construct that sequence and does not claim coefficient one.
