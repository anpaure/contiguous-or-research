# Recursive MSW rectangle trades as synchronized target flow

## 0. Outcome

Fix one lower layer

\[
                    \mathcal V=\binom{[n]}{m-q}
\]

and an integer cap `b`.  If a selectable move were a single directed
target arc, then elimination of the cap tail would be an ordinary integral
max-flow problem.  The exact residual is a directed cut deficiency.

The recursive MSW rectangle switch is not such an arc.  At every rank
`2<=m-q<=m-2` it is a synchronized bundle of four arcs: two coordinate
swaps in each direction.  Its exact one-depth optimization is therefore a
0--1 four-arm transshipment problem.  Its fractional relaxation has an
exact weighted-cut dual, but indicator cuts and ordinary max-flow are not
exact in general; a three-column four-arm example already has an
integrality gap.

There is one further distinction.  The isolated four-arm columns add
linearly only on a conflict-independent subfamily.  For the full recursive
cube, a depth-`q` window may have two switched boundary phases, so its
target change is nonlinear in the switch indicators.  Lemma 15.3 of the
plateau audit still implies that toggling one switch in any current state
changes at most four old targets into four new targets.  Thus the LP dual
below is exact for an additive colour class, while the full cube obeys a
dynamic four-arm drain inequality.

For the bulk parent-context family of Section 15 of
`MATH_AUDIT_PLATEAU_TRUNCATION_20260726.md`, the weighted cut given by the
canonical overloaded set yields a sharp capacity audit.  If

\[
 d=\operatorname {Cat}_r,\qquad
 M=H_{m,r+1}\operatorname {Cat}_{r-1},
\]

then all `M` switches together can reduce the cap tail by at most `4M`,
whereas the certified size-`r` plateau contributes at least

\[
                  H_{m,r}(d/2-b).
\]

At the fatal choice `d>=4b`, these two quantities are asymptotically
critical: `4M~H_(m,r)d/4`.  Thus bounded congestion of the one marked
source--destination arc is not the missing lemma.  Near the threshold,
almost every entire four-arm bundle would have to put all four negative
endpoints above the cap and all four positive endpoints strictly below it.
The current parent-context theorem certifies only one of those four
negative arms.

The sharp remaining quantity is the **four-arm drain across the current
overloaded set**, defined in static and dynamic forms below, together with
an integer-rounding theorem for an additive subfamily.

---

## 1. The exact one-arm benchmark

Let `D=(V,E)` be a directed graph with integral arc capacities `u_e`.
An initial integral load is `mu in Z_{>=0}^V`.  Sending an integral flow
along the arcs changes the terminal load by

\[
 y_v=\mu_v-\sum_{e\in\delta^+(v)}f_e
             +\sum_{e\in\delta^-(v)}f_e .                 \tag{1.1}
\]

Put

\[
 K_b(y)=\sum_v(y_v-b)_+,
 \qquad e_v=(\mu_v-b)_+,
 \qquad d_v=(b-\mu_v)_+.                                  \tag{1.2}
\]

### Theorem 1.1 (one-arm max-flow/min-cut formula)

Among all integral flows satisfying `0<=f_e<=u_e` and `y>=0`, the least
possible cap tail is

\[
 \boxed{
 K_b^{\rm arc}
 =\max_{X\subseteq V}
       \bigl[e(X)-d(X)-u(\delta^+(X))\bigr].}              \tag{1.3}
\]

In particular `K_b` can be eliminated if and only if

\[
 \boxed{
 e(X)\le d(X)+u(\delta^+(X))
 \quad\hbox{for every }X\subseteq V.}                     \tag{1.4}
\]

#### Proof

Adjoin a source `s`, arcs `s->v` of capacity `e_v`, a sink `t`, and arcs
`v->t` of capacity `d_v`.  Keep every arc of `D` with capacity `u_e`.
One unit routed from an initially excessive slot to an initially empty
cap slot lowers `K_b` by exactly one.  Conversely, decompose any improving
transshipment into paths and cycles.  Delete cycles and paths which do not
start at an initial excess slot and end at an initial deficit slot.  The
remaining paths have value exactly the improvement in `K_b`.  Hence

\[
 K_b^{\rm arc}=e(V)-\operatorname {maxflow}(s,t).          \tag{1.5}
\]

For a cut whose `V`-part on the source side is `X`, its capacity is

\[
 e(V\setminus X)+u(\delta^+(X))+d(X).
\]

Max-flow/min-cut and subtraction from `e(V)` give (1.3).  Taking the
maximum over a family containing `X=emptyset` also shows that the right
side is nonnegative.  Formula (1.4) is immediate.  \(\square\)

There is an exact hole version for free.  If the total load is `L` and
`N=|V|`, then

\[
 K_1(y)=L-N+H(y),\qquad H(y)=\#\{v:y_v=0\}.               \tag{1.6}
\]

Thus Theorem 1.1 gives

\[
 \boxed{
 H^{\rm arc}
 =\max_{Y\subseteq V}
 \left[
   h(Y)-s(Y)-u(\delta^-(Y))
 \right],}                                                \tag{1.7}
\]

where `h_v=1_(mu_v=0)` and `s_v=(mu_v-1)_+`.  All holes can be filled
without creating others precisely when every set of holes and relays `Y`
has at least `h(Y)` units of internal surplus plus incoming arc capacity.

---

## 2. The actual four-arm problem

Let `mathcal E` be a family of exact factor switches which is **additive
at the chosen depth**: every simultaneous choice has histogram equal to
the initial histogram plus the sum of the isolated changes.  At the chosen
layer write the signed column of switch `e` as

\[
 a_e={\bf1}_{P_e}-{\bf1}_{N_e},
 \qquad |P_e|=|N_e|=4,                                   \tag{2.1}
\]

with all eight endpoints distinct.  Every vector
`x in {0,1}^mathcal E` is physically legal, and

\[
                         \mu^x=\mu+Ax.                    \tag{2.2}
\]

The exact best residual on this additive family is the integer program

\[
 \boxed{
 K_b^{\mathbb Z}(\mu,A)
 =\min\left\{
   \sum_v z_v:
   z_v\ge\mu_v-b+(Ax)_v,\ z_v\ge0,\
   x_e\in\{0,1\}
 \right\}.}                                               \tag{2.3}
\]

This is the precise capacitated target-flow formulation.  The four arms
of one column are **ganged**: they cannot be routed separately.

Relax `x_e` to `[0,1]`.  Linear-programming duality gives an exact
weighted-cut formula for the relaxation.

### Theorem 2.1 (four-arm fractional cut dual)

\[
 \boxed{
 K_b^{\rm LP}(\mu,A)
 =\max_{0\le\alpha\le1}
 \left\{
   \langle\alpha,\mu-b\mathbf1\rangle
   -\sum_{e\in\mathcal E}
      \bigl(
       \alpha(N_e)-\alpha(P_e)
      \bigr)_+
 \right\}.}                                               \tag{2.4}
\]

Consequently fractional elimination is equivalent to

\[
 \boxed{
 \langle\alpha,\mu-b\mathbf1\rangle
 \le
 \sum_e\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
 \quad(0\le\alpha\le1).}                                \tag{2.5}
\]

For an indicator `alpha=1_X`, this becomes the necessary cut condition

\[
 \sum_{v\in X}(\mu_v-b)
 \le
 \sum_e
 \bigl(|N_e\cap X|-|P_e\cap X|\bigr)_+.                 \tag{2.6}
\]

#### Proof

Dualize the inequalities

\[
 z_v\ge\mu_v-b+(Ax)_v
\]

with multipliers `alpha_v>=0`.  Minimization over `z_v>=0` forces
`alpha_v<=1`.  For a fixed column,

\[
 \min_{0\le x_e\le1}
 x_e\langle\alpha,a_e\rangle
 =-\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+.
\]

This proves (2.4), and the other assertions follow.  \(\square\)

The integer residual decomposes canonically as

\[
 \boxed{
 K_b^{\mathbb Z}
 =K_b^{\rm LP}+\operatorname {IG}_b(\mu,A),
 \qquad \operatorname {IG}_b(\mu,A)\ge0.}                \tag{2.7}
\]

Thus two genuinely separate statements are required:

1. weighted four-arm cut expansion, making (2.4) small;
2. an integer rounding theorem, making the integrality loss in (2.7)
   small.

Neither is supplied by congestion of a single distinguished arm.

### Proposition 2.2 (four arms do not have automatic max-flow integrality)

There is a three-column instance with four positive and four negative
endpoints in every column for which

\[
                         K_1^{\mathbb Z}=2,
 \qquad                   K_1^{\rm LP}=3/2.               \tag{2.8}
\]

#### Proof

Use three resource vertices `a,b,c` and one column for each edge of the
triangle.  Column `uv` has two positive arms at `u,v`, two further private
positive arms, one private negative source of initial load two, and three
further private negative arms of initial load one.  Every resource and
private positive target starts at load zero.  The cap is one.

For a selection vector `(x_ab,x_bc,x_ca)`, only the three load-two sources
and the resource triangle can contribute to `K_1`.  If `k` columns are
chosen integrally, the residuals for `k=0,1,2,3` are respectively

\[
                         3,\ 2,\ 2,\ 3.
\]

Hence the integer optimum is two.  The fractional point
`x_ab=x_bc=x_ca=1/2` leaves source overload `3/2` and gives load exactly
one at every resource, proving `K_1^LP<=3/2`.

Conversely, if `s=x_ab+x_bc+x_ca`, the sum of resource overflow is at
least `(2s-3)_+`, while source overflow is `3-s`.  Therefore every
fractional point has value at least

\[
                         3-s+(2s-3)_+\ge3/2.
\]

This proves (2.8).  \(\square\)

The example does not assert an integrality gap for the special MSW
matrix.  It proves that support size `4+4`, commuting physical switches,
and ordinary endpoint congestion cannot by themselves imply an exact
max-flow theorem.

For holes, no new optimization is needed: by (1.6), for every exact
four-arm cube

\[
 \boxed{
 \min_x H(\mu+Ax)
 =K_1^{\mathbb Z}(\mu,A)-(L-N).}                           \tag{2.9}
\]

Thus (2.3)--(2.7), with `b=1`, are also the exact hole-balancing
formulation.

---

## 3. Exact geometry of one MSW column

Use the notation of (2.7) in `MSW_MULTIRANK_LOCAL_TRADES.md`.  At a lower
rank `k=m-q`, one column is

\[
 \begin{aligned}
 \tau_e={}&
  \partial K_{O,s}+\partial K_{E,s}
  -\partial K_{E,p}-\partial K_{O,p},\\
 \partial K={}&e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}.
 \end{aligned}                                             \tag{3.1}
\]

Consequently its four directed arms are

\[
 \begin{array}{c|c}
 \text{negative endpoint}&\text{positive endpoint}\\ \hline
 K_{O,s}\cup\{\beta\}&K_{O,s}\cup\{\gamma\}\\
 K_{E,s}\cup\{\beta\}&K_{E,s}\cup\{\gamma\}\\
 K_{E,p}\cup\{\gamma\}&K_{E,p}\cup\{\beta\}\\
 K_{O,p}\cup\{\gamma\}&K_{O,p}\cup\{\beta\}.
 \end{array}                                               \tag{3.2}
\]

Thus every arm is a directed Johnson edge, but the first two point from
`beta` to `gamma` and the last two point back from `gamma` to `beta`.
They must be activated together.

### Lemma 3.1 (point-margin null cuts)

For every coordinate `i`,

\[
 \sum_{S\ni i}\tau_e(S)=0.                                \tag{3.3}
\]

More generally, every coordinate-additive potential

\[
                     \phi(S)=c+\sum_{i\in S}w_i
\]

satisfies `langle phi,tau_e rangle=0`.

#### Proof

Within each `partial K`, every coordinate of `K` cancels.  The two forward
and two reverse `beta,gamma` swaps cancel the remaining point margins.
Total mass also vanishes.  Linearity proves the second assertion.
\(\square\)

In particular, the one marked arc `S_C->T_C` from Section 15 is only one
quarter of (3.2).  Across a coordinate-star cut it can point outward while
another arm points inward, with exactly zero net signed transport.  Hence
expansion of the marked context graph is not expansion of the legal trade
system.

---

## 4. The overloaded-set cut and the critical-capacity audit

Let the initial load be the canonical MSW load at depth `q`, and put

\[
 \Omega_q=\{S:\mu_q(S)>b\},\qquad
 K_q=\sum_S(\mu_q(S)-b)_+.                                \tag{4.1}
\]

For an additive switch family, the indicator cut
`alpha=1_(Omega_q)` in (2.4) gives the exact universal lower bound

\[
 \boxed{
 K_b^{\mathbb Z}
 \ge K_q-\mathsf {Drain}_{q}(\mathcal E),}                \tag{4.2}
\]

where

\[
 \boxed{
 \mathsf {Drain}_{q}(\mathcal E)
 :=\sum_{e\in\mathcal E}
   \bigl(
    |N_e\cap\Omega_q|-|P_e\cap\Omega_q|
   \bigr)_+.}                                             \tag{4.3}
\]

Every summand is at most four.  It equals four if and only if

\[
                         N_e\subseteq\Omega_q,
 \qquad                   P_e\cap\Omega_q=\varnothing.    \tag{4.4}
\]

This characterizes the indicator-cut surrogate (4.3), not the exact
one-toggle cap gain.  A positive endpoint of load exactly \(b\) lies
outside \(\Omega_q\) but creates one unit of overload when incremented.
The exact four-unit gain additionally requires every positive endpoint to
have load strictly below \(b\).

For the full recursive cube, (4.2) with the **initial** endpoint sets is
not valid: two switches can occur at the two boundaries of one window, so
the combined target is not the sum of their isolated target changes.
There is, however, an exact dynamic substitute.  Toggle the selected
switches in any order.  Let `mu^(j)` be the load just before toggle `j`,
let `Omega^(j)={S:mu^(j)(S)>b}`, and let `N_j,P_j` be the multisets of at
most four old and new targets changed by that toggle in the current state.
All intersections below count multiplicity.  Boundary
locality gives

\[
 \boxed{
 K_b(\mu^{\rm final})
 \ge K_b(\mu^{\rm initial})
 -\sum_j
   \bigl(
    |N_j\cap\Omega^{(j)}|-|P_j\cap\Omega^{(j)}|
   \bigr)_+.}                                             \tag{4.4a}
\]

Each dynamic summand is at most four.  Equality four again requires all
four currently removed targets to be overloaded and all four currently
inserted targets not to be strictly overloaded.  This is again a statement
about the upper-bound surrogate in (4.4a), not the exact marginal.

Indeed, at one target with current load `y`, `a` removed copies, and `c`
inserted copies,

\[
 (y-b)_+-(y-a+c-b)_+
 \le (a-c)\mathbf1_{\{y>b\}}.
\]

Sum this inequality over targets and retain the positive part of the total
marginal gain to obtain (4.4a).

After cancelling targets common to the old and new multisets, let
\(n_{j,S},p_{j,S}\) be the remaining old and new multiplicities at
target \(S\).  Thus \(n_{j,S}p_{j,S}=0\).  The exact statewise identity is

\[
\begin{aligned}
 K_b(\mu^{\rm initial})-K_b(\mu^{\rm final})
 =\sum_{j,S}\biggl(&
 \min\{n_{j,S},(\mu^{(j)}(S)-b)_+\}\\
 &-p_{j,S}
 +\min\{p_{j,S},(b-\mu^{(j)}(S))_+\}
 \biggr).
\end{aligned}                                             \tag{4.4b}
\]

When all current endpoints are unit-distinct, this reduces to

\[
 \sum_j\left[
 |N_j\cap\{S:\mu^{(j)}(S)>b\}|
 -
 |P_j\cap\{S:\mu^{(j)}(S)\ge b\}|
 \right].                                                \tag{4.4c}
\]

Thus an actual four-unit marginal decrease requires four units of current
negative excess and four units of current positive slack.  In the
unit-distinct case, all four negative endpoints must lie above \(b\) and
all four positive endpoints strictly below \(b\).

Now take the fixed-scale recursive parent family of Section 15.  Put

\[
 d=\operatorname {Cat}_r,
 \quad H_r=H_{m,r},
 \quad M=H_{m,r+1}\operatorname {Cat}_{r-1}.              \tag{4.5}
\]

Here, as in Theorem 2.3 of the plateau audit, `r` is chosen minimally so
that `d>=4b`.  In particular `d<16b`.

Theorem 2.3 of the plateau audit gives, uniformly for `r<=q<=m/2`,

\[
                         K_q\ge H_r(d/2-b).                \tag{4.6}
\]

There are exactly `M` selectable switches.  Toggling one of them in any
current state changes at most the two boundary windows in each of its two
rows, hence can lower `K_b` by at most four.  Therefore (4.4a) yields:

### Theorem 4.1 (critical raw-capacity bound)

For every simultaneous choice of the fixed-scale parent switches,

\[
 \boxed{
 K_b(\mu_q^x)
 \ge
 H_{m,r}(d/2-b)-4H_{m,r+1}\operatorname {Cat}_{r-1}.}     \tag{4.7}
\]

The exact capacity ratio is

\[
 \boxed{
 \rho_{m,r}:={M\over H_rd}
 ={(m-r)(r+1)
   \over4(2(m-r)-1)(2r-1)}
 ={1\over16}+O(r^{-1}+r/m).}                              \tag{4.8}
\]

Hence the right side of (4.7) is

\[
 H_r\left[
 d\left({1\over2}-4\rho_{m,r}\right)-b
 \right]
 =H_r\left[
 d\left({1\over4}+O(r^{-1}+r/m)\right)-b
 \right].                                                 \tag{4.9}
\]

#### Proof

Formula (4.7) is (4.4a), (4.6), and the bound four per toggle.  For
(4.8), use

\[
 {H_{m,r+1}\over H_{m,r}}
 ={m-r\over2(2(m-r)-1)},
 \qquad
 {\operatorname {Cat}_{r-1}\over\operatorname {Cat}_r}
 ={r+1\over2(2r-1)}.
\]

Multiplication gives the exact expression.  \(\square\)

### Corollary 4.2 (overshoot obstruction)

If `r^2/m=o(1)` and, along a subsequence,

\[
                         \operatorname {Cat}_r
 \ge(4+\varepsilon)b                                     \tag{4.10}
\]

for some fixed `epsilon>0`, then all fixed-scale parent switches leave

\[
                         K_b(\mu_q^x)
 \ge c_\varepsilon {W\over r^{3/2}}                      \tag{4.11}
\]

at every depth covered by (4.6), for all sufficiently large `m`.

If instead `d/b=4+o(1)`, the capacity is merely asymptotically critical.
Eliminating the certified tail with the full, possibly nonadditive cube
requires, along the chosen toggle order,

\[
 \sum_j
   \bigl(
    |N_j\cap\Omega^{(j)}|-|P_j\cap\Omega^{(j)}|
   \bigr)_+
 =4M-o(M).                                                \tag{4.12}
\]

Since each drain summand is an integer at most four, (4.12) forces the
surrogate dynamic version of (4.4) for all but `o(M)` toggles.  Actual
elimination at the same critical scale, by (4.4b), forces the stronger
four-unit positive-slack condition for all but \(o(M)\) toggles; in the
unit-distinct case this is exactly the strict-below-cap condition on all
four positive endpoints.

#### Proof

Under (4.10), (4.9) is at least a positive constant times `H_r d`.
The Catalan and central-binomial estimates give

\[
                         H_rd=\Theta(W/r^{3/2}).
\]

This proves (4.11).  In the critical case (4.6), (4.8), and (4.4a) give
(4.12); the final assertion follows from the characterization of a
four-unit marginal decrease.  \(\square\)

This audit is deliberately one-depth and seed-specific.  It does not rule
out additional parent types, other subtree scales, noncommuting larger
trades, or a different exact seed.  It does prove that the present one
parent family has no constant-factor slack: a theorem saying merely that
its marked destinations have bounded congestion cannot close the cap-tail
problem.

There is an even simpler decisive audit of the marked-arc projection.

### Corollary 4.3 (the marked intrinsic flow has zero cap-tail gain)

Inside one parent context, put

\[
 d=\operatorname {Cat}_r,
 \qquad e=\operatorname {Cat}_{r-1}.
\]

The exact boundary-profile computation in Lemma 15.2A of the plateau
audit gives marked loads

\[
                    (d,e,e)\longmapsto(d-e,2e,e)          \tag{4.13}
\]

on the three local targets labelled `2,3,4`.  At the fatal cutoff
`d>=4b`, one has `e>b` and `d-e>b`.  Therefore

\[
 \boxed{
 (d-b)+(e-b)+(e-b)
 =(d-e-b)+(2e-b)+(e-b).}                                  \tag{4.14}
\]

The marked intrinsic packet preserves cap tail exactly, even before any
destination-congestion question is asked.

The cruder one-arm projection is also capacity-insufficient: it has only
`M` arcs, whereas the certified plateau is asymptotic to `4M` at
`d/b=4+o(1)`.  But (4.14) is stronger.  It identifies the reason: the
marked tokens are transported between targets which all remain above the
cap.  Any gain must come from the other three cyclic arms of (3.2), not
from the marked context map.

#### Proof

The Catalan quotient is

\[
 {e\over d}={r+1\over2(2r-1)}>{1\over4},
\]

so `e>b` when `d>=4b`; also `d-e>b`.  All six positive-part arguments in
(4.14) are consequently positive, and the equality is literal mass
conservation.  \(\square\)

There is also a rigorous audit of what the presently guaranteed additive
subfamily supplies.  Corollary 15.4 of the plateau file gives an additive
independent set of size at least `M/5`; take exactly `floor(M/5)` of its
members.  For this guaranteed subfamily the static LP of Section 2 is
exact as a formulation, but its total raw cap-tail improvement is at most
`4M/5+O(1)`.  Thus, at `d/b=4+o(1)`, even perfect weighted-cut expansion
and perfect integrality on the guaranteed `M/5` switches leave

\[
 \boxed{
 H_r(d/2-b)-{4M\over5}
 =\left({1\over5}+o(1)\right)H_rd.}                       \tag{4.15}
\]

This does not upper-bound the maximum independent set: a larger additive
subfamily might exist.  What it proves is that the current degree-four
conflict argument alone supplies only one fifth of the critical switch
capacity.  Alternatively, using all five colour classes sequentially
returns the problem to the dynamic marginal condition (4.12).

At the packet's own depth one can improve the universal factor four to
two.

### Theorem 4.4 (self-scale two-arm capacity obstruction)

At depth `q=r`, for every partial or complete choice of the fixed-scale
parent switches,

\[
 \boxed{
 K_b(\mu_r^x)
 \ge H_r(d/2-b)-2M.}                                    \tag{4.16}
\]

In particular, when `d/b=4+o(1)`,

\[
 K_b(\mu_r^x)
 \ge\left({1\over8}+o(1)\right)H_rd
 =\Theta(W/r^{3/2}).                                     \tag{4.17}
\]

#### Proof

Within one parent context, selecting any `k<=e` of its elementary
switches changes the three intrinsic marked loads by

\[
                         (d,e,e)\longmapsto(d-k,e,e+k).
\]

Here `e=Cat_(r-1)>b` and `d-e>b`.  Thus all three targets remain strictly
above the cap throughout every ordering of the selected toggles, and the
two marked boundary arms of each toggle have total cap-tail change zero.
Additional load from other contexts only preserves this conclusion.

Only the two opposite cyclic boundary arms can lower the cap tail.  Their
total marginal decrease is at most two per toggle, even when their target
changes are nonadditive.  Apply the plateau lower bound (4.6) and sum over
at most `M` toggles to obtain (4.16).  Finally
`2M=(1/8+o(1))H_rd`, while at `d=4b(1+o(1))` the initial certified tail is
`(1/4+o(1))H_rd`, proving (4.17).  \(\square\)

This is a self-scale statement.  The phase-capacity failure repeats one
logarithmic-size invisible block through much larger depths `q>>r`; the
two marked arms at those larger depths have not been classified.  Thus
(4.16) neither closes nor kills a multiscale repair.  It does show that
the local packet cannot be treated as four freely useful units even at
the depth where its geometry is best understood.

---

## 5. The exact remaining combinatorial quantities

For any conflict-independent (hence additive) subfamily, a complete
one-depth theorem must prove both

\[
 \boxed{
 \begin{aligned}
 &\textbf{weighted cut expansion:}&
 K_b^{\rm LP}(\mu_q,A)&=o(W),\\
 &\textbf{integer rounding:}&
 \operatorname {IG}_b(\mu_q,A)&=o(W).
 \end{aligned}}                                           \tag{5.1}
\]

At the canonical overloaded-set cut, the first line entails a static
four-arm separation statement.  For the full cube, the corresponding
condition is dynamic.  In concrete MSW language the two quantities are

\[
 \boxed{
 \#\left\{e\text{ in an additive class}:
   N_e\subseteq\Omega_q,
   \ P_e\cap\Omega_q=\varnothing
 \right\}                                                 \tag{5.2}
\]

and the number of toggles in a full sequential use for which

\[
 N_j\subseteq\Omega^{(j)},
 \qquad P_j\cap\Omega^{(j)}=\varnothing.                 \tag{5.3}
\]

Section 15 currently proves that one distinguished negative endpoint of
each switch belongs to the nested fibre being retargeted **at depth
`r`**.  It gives no corresponding theorem for the other three negative
endpoints or for the four positive endpoints.  For a larger protected
depth `q>r`, even the identification of the distinguished negative arm
with the boundary-served plateau occurrence must still be checked.
Formula (3.2) shows exactly which four prefix/suffix flags must be counted.

Thus the sharp next MSW lemma is not ordinary endpoint expansion.  It is
one of the following genuinely stronger statements.

1. Prove the dynamic condition (5.3) for `1-o(1)` of the recursive
   toggles, uniformly through the protected depth window.  A static proof
   may instead work colour class by colour class, but (4.15) shows that no
   single class has enough capacity.
2. Construct enough additional parent orientations/scales that the
   four-arm drain has noncritical slack on every weighted cut in (2.5).
3. Replace the seed so that its overloaded set is transverse to all four
   positive flags and contains all four negative flags for a large legal
   trade cube.

Without one of these, the marked target-flow projection forgets three
quarters of every legal column and cannot certify a descent of either cap
tail or holes.
