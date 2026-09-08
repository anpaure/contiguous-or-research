# Synchronized four-arm recursive trade optimization

## 0. Outcome

The synchronized problem is not a unit-arc flow problem.  One recursive
switch has four lower arms, four complementary upper arms, and one common
binary coefficient at every serviced depth.  There are also two distinct
regimes.

1. On a switch family which is additive at every serviced depth, the exact
   relaxation is an ordinary linear program.  Its dual is a weighted
   four-arm cut formula.  The decisive coupling is

   \[
   \left(
      \sum_q\bigl[\alpha_q(N_{q,e})-\alpha_q(P_{q,e})\bigr]
   \right)_+,                                             \tag{0.1}
   \]

   not the sum over depths of the positive parts.  Thus one switch gets
   credit only for its net simultaneous-depth gain.

2. For the full recursive cube the histogram is not additive.  The exact
   convexified relaxation is a configuration LP whose dual contains a
   minimization over complete switch configurations.  It reduces to
   (0.1) precisely in the additive case.  A state-by-state four-arm drain
   inequality gives the corresponding dynamic necessary condition.

For an additive family, total unimodularity of the vertically stacked
multidepth matrix is a clean sufficient integral theorem, and the
Ghouila--Houri signing criterion is an exact test.  Neither four-arm
support, first-shadow linear independence, nor total unimodularity of
the separate depth matrices implies this stacked condition.  A scalable
three-column four-arm example has LP value `3/2` and integer value `2`.
That example is an obstruction to any support-only rounding theorem; it
is not yet an MSW-matrix minor.

There is, however, an actual MSW obstruction independent of rounding.  At
the packet's own depth `q=r`, two intrinsic arms have zero cap-tail gain,
so every fixed-scale recursive switch has useful capacity at most two.
Consequently every simultaneous multidepth construction from that one
fixed-scale parent family retains

\[
       K_{b_r}(\mu_r^x)
       \ge H_{m,r}(\operatorname {Cat}_r/2-b_r)-2M,       \tag{0.2}
\]

where

\[
       M=H_{m,r+1}\operatorname {Cat}_{r-1}.
\]

At `Cat_r/b_r=4+o(1)`, the right side is
`(1/8+o(1))H_(m,r)Cat_r=Theta(W/r^(3/2))`.  Total
unimodularity would not remove this capacity residual.

The remaining integral theorem is therefore sharply separated into two
questions:

* does the actual stacked MSW column matrix satisfy the signing criterion,
  or at least have `o(W)` integrality gap on the particular cap right-hand
  side; and
* after adding other scales or parent types, can the synchronized dynamic
  four-arm drain be made critical at every protected depth at once?

---

## 1. The literal synchronized column

Let `mathcal Q` be the set of protected **tagged layers**.  A lower depth
and its complementary upper depth are two separate members of
`mathcal Q`; the upper target rows are the complement images of the lower
rows.  Write the target set of tagged layer `q` as `V_q`.  Thus one column
has four positive and four negative entries in each tagged layer.  If a
lower/upper pair is instead grouped into one block, it has eight of each;
all formulas below are unchanged after expanding that block into its two
tags.

For a recursive switch `e`, the exact lower action at rank `m-q` is

\[
\begin{aligned}
 a_{q,e}
   ={}&\partial_e K^{q}_{O,s}+\partial_e K^{q}_{E,s}
      -\partial_e K^{q}_{E,p}-\partial_e K^{q}_{O,p},\\
 \partial_e K
   ={}&\mathbf e_{K\cup\{\gamma_e\}}
      -\mathbf e_{K\cup\{\beta_e\}} .                  \tag{1.1}
\end{aligned}
\]

Thus, away from the degenerate boundary ranks,

\[
       a_{q,e}=\mathbf1_{P_{q,e}}-\mathbf1_{N_{q,e}},
       \qquad |P_{q,e}|=|N_{q,e}|=4,                    \tag{1.2}
\]

where two arms point `beta_e -> gamma_e` on the suffix flags and two
point `gamma_e -> beta_e` on the prefix flags.  The four cores shorten
simultaneously as `q` grows.  The upper action is obtained by complement.

The same variable `x_e` multiplies every term in (1.1), at every lower
and upper depth.  Splitting (1.1) into independently routable Johnson
arcs changes the feasible set and is invalid.

There is a second audit.  Formula (1.1) is the isolated change.  For two
switches at the two boundaries of one depth-`q` window, the target after
both switches need not be the sum of their isolated changes.  Hence a
static matrix formulation is literal only for a family `mathcal E` which
is additive at every `q in mathcal Q`:

\[
             \mu_q^x=\mu_q+A_qx
       \quad(q\in\mathcal Q,\ x\in\{0,1\}^{\mathcal E}). \tag{1.3}
\]

One sufficient condition is that the family be independent in the union
of the boundary-conflict graphs for all serviced depths.  Independence is
not asserted necessary, since special interactions could cancel.  The one-depth bound
`Delta(G_q)<=4` does not give a constant-density family uniformly in a
growing set `mathcal Q`; the union bound is only
`Delta(\bigcup_qG_q)<=4|mathcal Q|`.  At `q=r` all fixed-scale switches
are additive, but this says nothing by itself about simultaneous
additivity at the other depths.

---

## 2. Exact additive simultaneous-depth LP and dual

Fix integer caps `b_q` and nonnegative depth weights `w_q`.  On a family
satisfying (1.3), the exact integer objective is

\[
 \boxed{
 \mathcal K_w^{\mathbb Z}
 =\min_{x\in\{0,1\}^{\mathcal E}}
   \sum_{q\in\mathcal Q}w_q
   \sum_{v\in V_q}
   \bigl(\mu_q(v)-b_q+(A_qx)_v\bigr)_+.}                \tag{2.1}
\]

The linear relaxation is

\[
\begin{aligned}
 \mathcal K_w^{\rm LP}=\min\quad
   &\sum_qw_q\sum_{v\in V_q}z_{q,v}\\
 \text{subject to}\quad
   &z_{q,v}\ge \mu_q(v)-b_q+(A_qx)_v,\\
   &z_{q,v}\ge0,\qquad 0\le x_e\le1.                  \tag{2.2}
\end{aligned}
\]

### Theorem 2.1 (synchronized four-arm cut dual)

The exact dual of (2.2) is

\[
 \boxed{
 \mathcal K_w^{\rm LP}
 =\max_{0\le\alpha_{q,v}\le w_q}
 \left\{
   \sum_q\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
   -\sum_{e\in\mathcal E}
    \left(
      \sum_q
       [\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
    \right)_+
 \right\}.}                                             \tag{2.3}
\]

Multiset multiplicity is understood at boundary ranks.  In particular,
simultaneous fractional elimination is equivalent to the weighted-cut
inequalities

\[
 \sum_q\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
 \le
 \sum_e\left(
      \sum_q[\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
          \right)_+                                     \tag{2.4}
\]

for every `0<=alpha_q<=w_q`.

#### Proof

Dualize the first line of constraints in (2.2) with multipliers
`alpha_(q,v)>=0`.  Minimization over `z_(q,v)>=0` gives
`alpha_(q,v)<=w_q`.  The coefficient of the single synchronized variable
`x_e` is

\[
 \sum_q\langle\alpha_q,a_{q,e}\rangle
 =\sum_q[\alpha_q(P_{q,e})-\alpha_q(N_{q,e})].           \tag{2.5}
\]

Minimizing `x_e` over `[0,1]` contributes the negative of the positive
part in (2.3).  Strong LP duality proves the formula.  Since the zero dual
vector is feasible, the optimum is zero exactly when (2.4) holds.  \(\square\)

The placement of the positive part is essential:

\[
 \left(\sum_q d_{q,e}\right)_+
 \le \sum_q(d_{q,e})_+,                                 \tag{2.6}
\]

and strict inequality occurs whenever the same switch drains one depth
but refills another.  The right side of (2.6) is the fictitious model in
which the depths may choose the switch independently.

Square brackets inside the depth sum in (2.3)--(2.6) are ordinary
grouping symbols; only the single outer subscript `+` denotes a positive
part.

For overloaded sets

\[
       \Omega_q=\{v:\mu_q(v)>b_q\},                    \tag{2.7}
\]

the legal simultaneous indicator cut is therefore

\[
 \boxed{
 \mathcal K_w^{\mathbb Z}\ge
 \sum_qw_qK_{b_q}(\mu_q)
 -\sum_e\left(
   \sum_qw_q\bigl[
       |N_{q,e}\cap\Omega_q|-|P_{q,e}\cap\Omega_q|
   \bigr]
 \right)_+.}                                            \tag{2.8}
\]

It is never legitimate to replace the last term by the sum of its
one-depth positive parts when claiming an exact synchronized capacity.

---

## 3. Exact minimax form

A sum over depths can conceal a bad row.  Let `s_q>0` be the admissible
residual scale and define the relaxed worst-depth objective

\[
 \Psi^{\rm LP}
 =\min_{0\le x\le1}
    \max_{q\in\mathcal Q}
       {K_{b_q}(\mu_q+A_qx)\over s_q}.                  \tag{3.1}
\]

### Theorem 3.1 (simultaneous-depth min--max dual)

One has

\[
\boxed{
 \begin{aligned}
 \Psi^{\rm LP}=\max\quad
 &\sum_q\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
 -\sum_e\left(
    \sum_q[\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
            \right)_+\\
 \text{subject to}\quad
 &\lambda_q\ge0,qquad
   \sum_q\lambda_qs_q\le1,\\
 &0\le\alpha_{q,v}\le\lambda_q.
 \end{aligned}}                                         \tag{3.2}
\]

#### Proof

Use variables `z_(q,v)>=0` as in (2.2), add a variable `t>=0`, and impose

\[
                 \sum_vz_{q,v}\le s_qt.                \tag{3.3}
\]

Let `lambda_q>=0` be the multiplier for (3.3).  Minimization over `t`
gives `sum_q lambda_qs_q<=1`; minimization over each `z_(q,v)` gives
`alpha_(q,v)<=lambda_q`; and minimization over the common `x_e` gives the
same synchronized penalty as in (2.3).  Strong duality proves (3.2).
\(\square\)

Thus the adversary in the exact fractional min--max theorem chooses both
a distribution of emphasis among depths and a weighted cut inside each
depth.  A proof for each depth with unrelated switch choices does not
imply (3.2).

---

## 4. The precise total-unimodularity gate

Stack the target rows vertically:

\[
                     A^{\rm all}=\begin{bmatrix}
                           A_q
                         \end{bmatrix}_{q\in\mathcal Q}. \tag{4.1}
\]

### Theorem 4.1 (TU sufficient condition)

If `A^all` is totally unimodular, then for every integral collection
`(mu_q,b_q)` and every nonnegative weight vector `w`, (2.2) has an
integral optimum.  Hence

\[
                    \mathcal K_w^{\mathbb Z}
                    =\mathcal K_w^{\rm LP}.             \tag{4.2}
\]

#### Proof

After changing row signs, the nontrivial constraint matrix in (2.2) is

\[
                         [\,A^{\rm all}\mid-I\,].       \tag{4.3}
\]

Adjoining signed identity columns and integral variable bounds preserves
total unimodularity.  The right-hand side is integral, so every vertex is
integral.  Linear optimization therefore has an integral optimum.  \(\square\)

This is also an exact matrix test: the matrix in (4.3) is TU if and only
if `A^all` is TU, because `A^all` is a submatrix and adjoining signed unit
columns preserves TU.  By the Hoffman--Kruskal theorem, it is the exact
criterion for integrality for every integral right-hand side of the
corresponding bounded linear system.  A particular MSW right-hand side
may of course be integral even when the universal matrix test fails.

The Ghouila--Houri form is especially concrete here.

### Corollary 4.2 (exact signing criterion)

`A^all` is TU if and only if, for every set `R` of tagged depth-target
rows, one can choose signs `epsilon_(q,v) in {+1,-1}` such that every
recursive switch satisfies

\[
 \sum_{(q,v)\in R}\epsilon_{q,v}
 \bigl(\mathbf1_{v\in P_{q,e}}-
       \mathbf1_{v\in N_{q,e}}\bigr)
       \in\{-1,0,1\}.                                   \tag{4.4}
\]

This criterion includes the four arms and all depths simultaneously.

Complement symmetry causes no hidden TU difficulty by itself.  An upper
tagged block is, up to row permutation (and harmless row signs), a copy of
the corresponding lower block.  Appending duplicate or signed duplicate
rows preserves TU.  The possible TU failure comes from stacking genuinely
different depths.  Nevertheless the complementary tags remain coupled in
the optimization: their dual contributions are still added before the
single positive part for `x_e` is taken.

Three common shortcuts do not prove (4.4).

1. **Separate-depth TU is insufficient.**  Vertical concatenation can
   destroy TU.  The two one-row matrices `[1\ 1]` and `[1\ {-1}]` are TU,
   whereas their vertical stack has determinant `-2`.

2. **First-shadow pivots are insufficient.**  The recursive local columns
   have a triangular `+-1` pivot minor at rank `m-1`, and hence are
   linearly independent there.  TU requires every square minor to be
   `0,+-1`, not merely one unimodular full-column-rank minor.

3. **Four-arm balance is not a TU certificate.**  Zero total mass and zero
   point margins give linear equations on each column, whereas (4.4)
   quantifies over every subset of target rows.  The latter signing
   condition must still be proved for the actual columns.

The exact unresolved MSW rounding question is therefore (4.4), or a
right-hand-side-specific substitute proving only

\[
        \mathcal K_w^{\mathbb Z}-\mathcal K_w^{\rm LP}=o(W). \tag{4.5}
\]

No determinant-two minor of the certified fixed-factor recursive family
is asserted here.  Establishing one requires three or more switches from
the same physical factor, not three independently relabelled copies of a
universal four-letter identity.

---

## 5. An exact scalable support-level integrality obstruction

The universal four-arm hypotheses cannot yield (4.5).  Consider three
columns indexed by the edges of a triangle on resource rows `a,b,c`.
Column `uv` has positive endpoints at `u,v`, two further private positive
endpoints, one private negative endpoint of initial load two, and three
private negative endpoints of initial load one.  All other initial loads
are zero and the cap is one.

If `k` columns are selected integrally, the residual for
`k=0,1,2,3` is

\[
                              3,2,2,3.                  \tag{5.1}
\]

Thus the integer optimum is two.  At
`x_1=x_2=x_3=1/2`, the three resource loads are exactly one and the
three private sources have total excess `3/2`.  Conversely, if
`s=x_1+x_2+x_3`, source excess is `3-s` and resource excess is at least
`(2s-3)_+`, whose sum is at least `3/2`.  Hence

\[
                      K_1^{\mathbb Z}=2,
             \qquad  K_1^{\rm LP}=3/2.                  \tag{5.2}
\]

The three resource rows against the three columns contain the minor

\[
             \begin{pmatrix}
              1&1&0\\
              1&0&1\\
              0&1&1
             \end{pmatrix},
             \qquad \det=-2.                            \tag{5.3}
\]

Disjoint union of `L` copies gives additive integrality loss `L/2`, so
bounded column width does not even imply a sublinear gap.  Additional
serviced depths may be appended with high enough caps that they never
contribute; hence simultaneous ganging alone does not remove the gap.

This is an exact, linearly scalable obstruction to a theorem based only on
`4+4` support, commutation, or endpoint congestion.  It is not a proof
that the special stacked MSW matrix contains (5.3).  That distinction is
essential.

---

## 6. The full nonadditive recursive cube

Let `mathfrak X` be the set of physically legal complete switch
configurations and let `mu_q^X` be the exact histogram obtained from
configuration `X`.  This notation includes every interaction remainder;
no sum of isolated columns is assumed.  The literal integer problem is

\[
 \boxed{
 \mathcal J_w^{\mathbb Z}
 =\min_{X\in\mathfrak X}
   \sum_qw_qK_{b_q}(\mu_q^X).}                           \tag{6.1}
\]

The useful convexified histogram relaxation chooses a distribution
`theta` on complete configurations:

\[
\begin{aligned}
 \mathcal J_w^{\rm conf} =\min\quad
   &\sum_qw_q\sum_vz_{q,v}\\
 \text{subject to}\quad
   &z_{q,v}\ge\sum_{X\in\mathfrak X}
                  \theta_X\mu_q^X(v)-b_q,\\
   &z_{q,v}\ge0,\quad \theta_X\ge0,\quad
    \sum_X\theta_X=1.                                  \tag{6.2}
\end{aligned}
\]

### Theorem 6.1 (exact dual of the configuration relaxation)

\[
 \boxed{
 \mathcal J_w^{\rm conf}
 =\max_{0\le\alpha_{q,v}\le w_q}
 \left\{
    -\sum_qb_q\alpha_q(V_q)
    +\min_{X\in\mathfrak X}
       \sum_q\langle\alpha_q,\mu_q^X\rangle
 \right\}.}                                             \tag{6.3}
\]

Moreover

\[
                  \mathcal J_w^{\rm conf}
                  \le\mathcal J_w^{\mathbb Z}.          \tag{6.4}
\]

If (1.3) holds, the inner minimum in (6.3) separates by switch and (6.3)
reduces exactly to (2.3).

#### Proof

Dual multipliers `alpha_(q,v)>=0` for the first constraints in (6.2)
are bounded above by `w_q` after minimizing over `z`.  Minimizing the
linear expression over the simplex of `theta` selects the least-weight
complete configuration, giving the inner minimum in (6.3).  Strong
duality proves equality.  Every integral configuration is a feasible
vertex of (6.2), proving (6.4).  Under (1.3),

\[
 \min_{x\in\{0,1\}^{\mathcal E}}
 \sum_q\langle\alpha_q,\mu_q+A_qx\rangle
 =\sum_q\langle\alpha_q,\mu_q\rangle
  -\sum_e\left(
       \sum_q[\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
            \right)_+ .                                 \tag{6.5}
\]

This is (2.3).  \(\square\)

Formula (6.3) is the honest LP/min--max reduction for the nonadditive
recursive cube.  Replacing its inner configuration minimum by independent
unit arcs is an additional, generally false relaxation.

There is a trivial integral state-DAG formulation: use a node for every
partial switch state and put the exact terminal cap-tail value on every
complete state.  Its path matrix is TU, but it merely enumerates the
original exponential optimization and supplies no rounding theorem.  The
fact that this artificial state graph is a network does not make the
target transport a network flow.

---

## 7. Dynamic synchronized drain

The full cube still has an exact local necessary condition.  Toggle a
chosen sequence of switches.  Immediately before toggle `j`, let

\[
          \Omega_q^{(j)}=\{v:\mu_q^{(j)}(v)>b_q\},       \tag{7.1}
\]

and let `N_(q,j),P_(q,j)` be the multisets of at most four old and new
targets changed at depth `q` in the current state.  Define

\[
 d_{q,j}=|N_{q,j}\cap\Omega_q^{(j)}|
          -|P_{q,j}\cap\Omega_q^{(j)}|.                 \tag{7.2}
\]

### Theorem 7.1 (dynamic simultaneous four-arm inequality)

For every toggle order,

\[
 \boxed{
 \sum_qw_qK_{b_q}(\mu_q^{\rm final})
 \ge
 \sum_qw_qK_{b_q}(\mu_q^{\rm initial})
 -\sum_j\left(\sum_qw_qd_{q,j}\right)_+.}              \tag{7.3}
\]

#### Proof

At one target of current load `y`, if the toggle removes `a` copies and
inserts `c` copies, then

\[
 (y-b)_+-(y-a+c-b)_+
 \le(a-c)\mathbf1_{\{y>b\}}.                            \tag{7.4}
\]

Sum over targets at depth `q`; the cap-tail decrease is at most
`d_(q,j)`.  After multiplying by `w_q` and summing in `q`, the weighted
decrease at toggle `j` is at most `sum_qw_qd_(q,j)`, and hence at most its
positive part.  Telescope.  \(\square\)

Again the positive part occurs after summing over depths.  The weaker
quantity

\[
                     \sum_qw_q(d_{q,j})_+               \tag{7.5}
\]

credits mutually incompatible one-depth gains and is not the exact
synchronized marginal.

Put `w_* = sum_qw_q` and suppose there are at most `M` toggles.  Since
`d_(q,j)<=4`, the maximum possible term in (7.3) is `4w_*`.  If a proposed
construction needs weighted drain

\[
                         4Mw_*-\eta,                    \tag{7.6}
\]

then necessarily

\[
 \sum_j\left[4w_*-\left(\sum_qw_qd_{q,j}\right)_+\right]
 \le\eta.                                                \tag{7.7}
\]

Because the `d_(q,j)` are integers, (7.7) also implies

\[
 \boxed{
 \sum_j\sum_{q:\ d_{q,j}\le3}w_q\le\eta.}             \tag{7.8}
\]

Indeed, if the weighted sum in (7.7) is nonnegative, its deficit from
`4w_*` is `sum_qw_q(4-d_(q,j))`; if it is negative, the left side of
(7.7) is `4w_*`, which is still at least the total weight of the bad
depths.  Thus critical simultaneous drain forces almost every
switch-depth pair of nonnegligible weight to have

\[
 N_{q,j}\subseteq\Omega_q^{(j)},\qquad
 P_{q,j}\cap\Omega_q^{(j)}=\varnothing.                 \tag{7.9}
\]

This is substantially stronger than proving four-arm separation at each
depth using a different set or order of switches.

---

## 8. Application to the actual fixed-scale recursive family

For the fixed-scale parent family put

\[
       d=\operatorname {Cat}_r,\qquad
       M=H_{m,r+1}\operatorname {Cat}_{r-1}.             \tag{8.1}
\]

The certified initial tail at every covered depth satisfies

\[
                       K_{b_q}(\mu_q)
                       \ge H_{m,r}(d/2-b_q).             \tag{8.2}
\]

The raw four-arm capacity is at most `4M`, with exact ratio

\[
 {M\over H_{m,r}d}
 ={(m-r)(r+1)\over4(2(m-r)-1)(2r-1)}
 ={1\over16}+O(r^{-1}+r/m).                              \tag{8.3}
\]

At `d/b_q=4+o(1)`, (8.2) and (8.3) already require drain
`4M-o(M)`.  Therefore (7.8)--(7.9) are necessary simultaneously over
the protected depths.

At the matched depth `q=r` there is a sharper literal fact.  In each
parent context, selecting `k` elementary switches changes the three
intrinsic marked loads by

\[
                         (d,e,e)\mapsto(d-k,e,e+k),
             \qquad e=\operatorname {Cat}_{r-1}.        \tag{8.4}
\]

At the critical cutoff all three displayed loads remain above the cap.
The two intrinsic marked arms therefore have total cap-tail gain zero,
in every current state and every order.  Only the two opposite cyclic
arms can help.  Consequently

\[
                         d_{r,j}\le2                    \tag{8.5}
\]

for every toggle, and

\[
 \boxed{
 K_{b_r}(\mu_r^x)
 \ge H_{m,r}(d/2-b_r)-2M.}                               \tag{8.6}
\]

At `d/b_r=4+o(1)`, use `2M=(1/8+o(1))H_(m,r)d` to obtain

\[
 K_{b_r}(\mu_r^x)
 \ge(1/8+o(1))H_{m,r}d
 =\Theta(W/r^{3/2}).                                     \tag{8.7}
\]

For a weighted simultaneous objective, (8.5) lowers the total per-toggle
capacity from `4w_*` to at most

\[
                           4w_*-2w_r.                    \tag{8.8}
\]

Thus a critical four-units-per-switch proof at every depth is impossible
for this family even before rounding.  The residual (8.7) is a genuine
actual-family obstruction.  Its consequence for coefficient one depends
on the chosen scale: it is linear in `W` for bounded `r`, but is `o(W)`
when `r` tends to infinity.  It nevertheless rules out exact elimination
and any claim of four-arm slack at the self scale.

Finally, every column has zero point margins:

\[
              \sum_{S\ni i}a_{q,e}(S)=0.                \tag{8.9}
\]

Hence coordinate-additive dual potentials see zero net switch gain at
every depth.  Any positive obstruction carried by such a bounded dual
potential survives untouched.  This is another reason the distinguished
marked Johnson arc cannot be audited separately from its three collateral
arms.

---

## 9. Exact frontier

The strongest honest theorem presently available is the following
dichotomy.

### Theorem 9.1 (Lane D reduction)

Let `mathcal E` be a physically legal recursive switch family and
`mathcal Q` a protected depth set.

1. If `mathcal E` is additive simultaneously on `mathcal Q`, then
   coefficient-one rounding follows from the stacked Ghouila--Houri
   condition (4.4).  Without it, one must prove the particular bound
   (4.5); `4+4` support alone permits a linear integrality gap.

2. If `mathcal E` is not simultaneously additive, its honest fractional
   obstruction is (6.3), and every integral trajectory obeys (7.3).
   A unit-arc max-flow certificate is not a certificate for this problem.

3. For the present fixed-scale recursive parent family, the self-scale
   lower bound (8.6) holds for every integral configuration, regardless
   of total unimodularity or fractional feasibility.

Accordingly, a successful multiscale proof must do all three of the
following:

* add switch types whose actual four-arm bundles supply the missing
  self-scale capacity;
* verify simultaneous-depth weighted drain, with the positive part outside
  the depth sum as in (2.3) or (7.3); and
* prove stacked TU, an MSW-specific `o(W)` rounding theorem, or an integral
  absorber for the remaining configuration-LP gap.

This is the exact optimization target.  Any formulation which assigns
independent flow to the four Johnson arms, independent choices to the
depths, or additive columns to the interacting full cube solves a strictly
weaker problem.
