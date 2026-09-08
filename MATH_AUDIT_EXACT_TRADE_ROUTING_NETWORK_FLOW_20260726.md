# Exact audit of the trade-routing network-flow claim

## 0. Verdict

The statement

> the recursive trade-routing problem is a convex-cost directed network
> flow

is false as stated.

At a fixed nondegenerate lower depth, one switch is not one directed arc.
It is one binary coefficient multiplying four directed Johnson arcs, two in
each coordinate direction.  At the first depth the two coincident arms
cancel and the column is an oriented Johnson square with two positive and
two negative entries.  Splitting these arms into independent arc variables
strictly enlarges the feasible set; retaining the equal-use constraints
destroys the node--arc form.

There are three different exact optimization objects, and they must not be
conflated.

1. For a conflict-free family whose isolated target changes add, the exact
   integral problem is a ganged-column integer program.  Its continuous
   relaxation has an exact **weighted** Hall/deficiency dual.
2. If selections are restricted by physical conflicts, the dual penalty is
   the support function of the legal-selection polytope, not a sum of arc
   capacities.
3. If simultaneous switches interact at a window boundary, there is no
   fixed incidence matrix.  The honest relaxation is a configuration LP,
   or one must work with a statewise dynamic drain inequality.

The fixed-depth trade matrix is not a directed node--arc incidence matrix.
Nor is the complete coordinate-relabeling orbit a network matrix in the
more general linear-algebraic sense: already at `m=3`, depth `q=1`, three
exact Johnson-square columns have a determinant-two minor.  This example is
minimal among first-depth Johnson-square columns.  It also supports an
exact cap-tail instance with LP value `3/2` and integer value `2`.

This does **not** prove that a particular restricted compatible subfamily
inside one fixed MSW factor is non-TU.  It proves that network integrality
does not follow from the local trade identity, and that a construction
which mixes coordinate frames must audit the actual stacked selected
matrix or supply a right-hand-side-specific rounding theorem.

The precise surviving routing gate is stated in Section 8.

---

## 1. The exact column of one legal local trade

Let `n=2m+1`.  Use four distinct exceptional labels

\[
                 \alpha,\beta,\gamma,\delta
\]

and order the remaining labels as

\[
                 T=(t_0,t_1,\ldots,t_{2m-4}).
\]

Split the tail into its two parity lists

\[
 \mathsf E=(t_0,t_2,\ldots,t_{2m-4}),\qquad
 \mathsf O=(t_1,t_3,\ldots,t_{2m-5}).                  \tag{1.1}
\]

For a lower target rank `k=m-q` put `ell=k-1` and define

\[
\begin{array}{ll}
 K_{O,s}=\operatorname {suf}_{\ell}(\mathsf O),&
 K_{E,s}=\operatorname {suf}_{\ell}(\mathsf E),\\
 K_{E,p}=\operatorname {pre}_{\ell}(\mathsf E),&
 K_{O,p}=\operatorname {pre}_{\ell}(\mathsf O).
\end{array}                                             \tag{1.2}
\]

Writing

\[
                 \partial K
 =\mathbf e_{K\cup\{\gamma\}}-\mathbf e_{K\cup\{\beta\}},
\]

the exact isolated target change of the switch is

\[
 \boxed{
 a_{q,e}=\partial K_{O,s}+\partial K_{E,s}
          -\partial K_{E,p}-\partial K_{O,p}.}          \tag{1.3}
\]

Thus, when `2<=k<=m-2`, all eight targets are distinct and

\[
                 a_{q,e}=\mathbf1_{P_{q,e}}-
                           \mathbf1_{N_{q,e}},           \tag{1.4}
\]

where

\[
\begin{aligned}
P_{q,e}={}&\{K_{O,s}\gamma,K_{E,s}\gamma,
             K_{E,p}\beta,K_{O,p}\beta\},\\
N_{q,e}={}&\{K_{O,s}\beta,K_{E,s}\beta,
             K_{E,p}\gamma,K_{O,p}\gamma\}.           \tag{1.5}
\end{aligned}
\]

Here `Kx` abbreviates `K union {x}`.  The first two arms point
`beta -> gamma`; the last two point `gamma -> beta`.  All four arms have
one common switch variable.

At the first depth `q=1`, equivalently `k=m-1`, the two odd-list terms
coincide and cancel.  If

\[
 x=t_0,\qquad y=t_{2m-4},\qquad
 K=\mathsf E\setminus\{x,y\},
\]

then the exact column is the Johnson square

\[
 \boxed{
 a_{1,e}=\mathbf e_{K\beta x}-\mathbf e_{K\gamma x}
          -\mathbf e_{K\beta y}+\mathbf e_{K\gamma y}.} \tag{1.6}
\]

The lower actions at ranks `1` and `m` vanish.  The upper-depth column is
the row-permuted complementary copy of the corresponding lower-depth
column.

Two useful invariants follow immediately from (1.3):

\[
 \sum_S a_{q,e}(S)=0,\qquad
 \sum_{S\ni i}a_{q,e}(S)=0\quad(i\in[n]).               \tag{1.7}
\]

Thus every coordinate-additive target potential annihilates a legal
column.  These equations do not imply total unimodularity.

Formula (1.3), including the cancellation in (1.6), is the complete
fixed-depth incidence audit.  Treating one distinguished arm as the
trade, or assigning four independent flow values to (1.5), is not the
same optimization problem.

---

## 2. When a fixed matrix is actually valid

Let `mathcal E` be a proposed switch family at depth `q`, and let
`mathscr I subseteq 2^mathcal E` be the physically legal simultaneous
subfamilies.  There are two independent issues.

* **Physical compatibility:** the cycles removed by the chosen switches
  and the cycles inserted by them must remain disjoint and preserve exact
  middle ownership.
* **Target additivity:** for every legal `I in mathscr I`, the final
  histogram must satisfy

  \[
                \mu_q^I=\mu_q+\sum_{e\in I}a_{q,e}.     \tag{2.1}
  \]

Boundary interactions can make (2.1) false even when each isolated
column (1.3) is correct.

Only if both conditions hold is the fixed-depth matrix

\[
                 A_q=(a_{q,e})_{e\in\mathcal E}         \tag{2.2}
\]

an exact description on the legal selection set.  If, in addition,
`mathscr I=2^mathcal E`, the variables range over the full cube
`{0,1}^mathcal E`.  This last hypothesis is what allows the dual penalty
to separate column by column.

For a merely conflict-constrained additive family, put

\[
 P_{\mathscr I}=\operatorname {conv}
       \{\mathbf1_I:I\in\mathscr I\}.                   \tag{2.3}
\]

Replacing this polytope by the unit cube is another relaxation, not a
network-flow identity.

---

## 3. The exact fixed-depth deficiency dual

Fix an integral initial load `mu`, an integral cap `b`, and an additive
family.  For a conflict-free cube the exact integer cap-tail problem is

\[
 \boxed{
 K_b^{\mathbb Z}(\mu,A)=
 \min_{x\in\{0,1\}^{\mathcal E}}
       \sum_v\bigl(\mu_v-b+(Ax)_v\bigr)_+.}             \tag{3.1}
\]

Its linear relaxation is obtained by taking `0<=x<=1` and introducing
`z_v>=0` with

\[
                 z_v\ge \mu_v-b+(Ax)_v.                 \tag{3.2}
\]

### Theorem 3.1 (weighted four-arm deficiency)

For the full cube,

\[
 \boxed{
 K_b^{\rm LP}(\mu,A)=
 \max_{0\le\alpha\le1}
 \left\{
  \langle\alpha,\mu-b\mathbf1\rangle
  -\sum_{e\in\mathcal E}
     \bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
 \right\}.}                                            \tag{3.3}
\]

Consequently fractional elimination of the cap tail is equivalent to

\[
 \boxed{
 \langle\alpha,\mu-b\mathbf1\rangle
 \le \sum_e\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+
 \quad\text{for every }0\le\alpha\le1.}                \tag{3.4}
\]

For `alpha=1_X`, (3.4) gives the necessary indicator-cut inequality

\[
 \sum_{v\in X}(\mu_v-b)
 \le\sum_e\bigl(|N_e\cap X|-|P_e\cap X|\bigr)_+.       \tag{3.5}
\]

Indicator cuts alone are not the exact dual: all fractional weights
`0<=alpha<=1` are required.

#### Proof

Give (3.2) multipliers `alpha_v>=0`.  Minimization over `z_v>=0` forces
`alpha_v<=1`.  For a fixed column,

\[
 \min_{0\le x_e\le1}x_e\langle\alpha,a_e\rangle
 =\min_{0\le x_e\le1}
   x_e\bigl(\alpha(P_e)-\alpha(N_e)\bigr)
 =-\bigl(\alpha(N_e)-\alpha(P_e)\bigr)_+.
\]

Strong LP duality proves (3.3), and zero primal value is equivalent to
(3.4).  \(\square\)

For a legal-selection polytope (2.3), the same proof gives the exact
convexified formula

\[
 \boxed{
 K_{b,P}^{\rm LP}=
 \max_{0\le\alpha\le1}
 \left\{
  \langle\alpha,\mu-b\mathbf1\rangle
  -h_P(d(\alpha))
 \right\},}                                             \tag{3.6}
\]

where

\[
 d_e(\alpha)=\alpha(N_e)-\alpha(P_e),\qquad
 h_P(d)=\max_{x\in P}\langle d,x\rangle.               \tag{3.7}
\]

For the cube, `h_P(d)=sum_e(d_e)_+`, recovering (3.3).  For a conflict
graph, (3.7) is a maximum-weight independent-set value.  It is not an arc
cut capacity in general.

Theorem 3.1 is a fractional Hall/deficiency theorem.  It is not an exact
formula for (3.1) unless a separate integrality theorem is proved.

---

## 4. Why this is not a directed network matrix

A directed node--arc incidence column has, after deletion of one redundant
node row, at most one `+1` and at most one `-1`.  The legal column (1.5)
has four of each, and (1.6) has two of each.  Therefore `A_q` is not the
node--arc incidence matrix of the target graph.

One can introduce four Johnson-arc variables `y_(e,1),...,y_(e,4)`.
Their target-balance columns are ordinary directed incidence columns, but
physical legality imposes

\[
              y_{e,1}=y_{e,2}=y_{e,3}=y_{e,4}=x_e.      \tag{4.1}
\]

Deleting (4.1) is exactly the false independent-arm relaxation.  Keeping
(4.1) appends ganging rows and does not give an ordinary flow matrix.

There is a broader notion of a network matrix, namely `B_T^{-1}B_N` for a
directed graph incidence matrix `B` and a tree basis `B_T`.  Such a matrix
may have columns with many nonzero entries, but every network matrix is
totally unimodular.  Hence one determinant of absolute value at least two
rules out this broader interpretation as well.

The next section gives such a determinant inside the exact first-depth
coordinate-relabeling orbit.

---

## 5. The smallest exact first-depth counterexample

Take `m=3`, so `n=7`, and work at depth `q=1`; the targets are two-sets.
Formula (1.6) has `K=emptyset`.  Consider the following three exact
Johnson-square columns:

\[
\begin{aligned}
 a_1&=\mathbf e_{13}-\mathbf e_{23}
               -\mathbf e_{14}+\mathbf e_{24},\\
 a_2&=\mathbf e_{13}-\mathbf e_{36}
               -\mathbf e_{15}+\mathbf e_{56},\\
 a_3&=\mathbf e_{24}-\mathbf e_{46}
               -\mathbf e_{25}+\mathbf e_{56}.          \tag{5.1}
\end{aligned}
\]

They are literal instances of (1.6): use respectively

\[
 (\beta,\gamma,x,y)=(1,2,3,4),\quad
 (1,6,3,5),\quad
 (2,6,4,5).                                             \tag{5.2}
\]

For example, complete the universal four-letter data by taking

\[
\begin{array}{c|c|c}
e&(\alpha,\delta)&T\\ \hline
1&(5,6)&(3,7,4)\\
2&(2,4)&(3,7,5)\\
3&(1,3)&(4,7,5).
\end{array}                                             \tag{5.3}
\]

The rows `13,24,56` against these columns form

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det=-2.                                        \tag{5.4}
\]

Therefore the full coordinate-relabeling trade-column matrix is not TU
and cannot be a network matrix.

### Proposition 5.1 (minimality at the first depth)

No one- or two-column matrix of oriented Johnson squares has a minor of
absolute value greater than one.  Hence (5.1) is minimal in the number of
first-depth trade columns.  It also occurs at the smallest nondegenerate
parameter `m`: for `m=2` the rank-one trade action vanishes.

#### Proof

Only a two-by-two minor needs consideration for two columns.  In an
oriented Johnson square, two support vertices have opposite signs exactly
when their Johnson distance is one, and the same sign exactly when their
Johnson distance is two.  Thus, if two square columns contain the same two
target rows `U,V`, the relative sign between `U` and `V` is the same in
both columns, since it is determined by `d_J(U,V)`.  The corresponding
two-by-two determinant is zero.  If one of the four entries is zero, its
absolute determinant is at most one.  This proves the claim.  The
determinant in (5.4) proves sharpness.  \(\square\)

The three columns in (5.1) belong to the universal relabeled local-trade
catalogue.  The assertion here is a matrix assertion.  It does not assert
that all three switches are simultaneously available inside one fixed
MSW factor.  A fixed-factor claim must additionally prove physical
compatibility and must identify the actual selected submatrix.  This
caveat cannot restore the general network-flow reduction; it merely
defines a narrower TU question.

---

## 6. Exact integral gap on the counterexample

The determinant obstruction is visible directly in the cap-tail
objective.  Put cap `b=1`.  Start the shared positive targets

\[
                        13,24,56
\]

at load zero.  In each column choose one negative target as a source of
load two and start its other negative target at load one:

\[
 \mu_{23}=\mu_{36}=\mu_{46}=2,qquad
 \mu_{14}=\mu_{15}=\mu_{25}=1.                         \tag{6.1}
\]

All unlisted targets start at zero.  If `x_i` is the coefficient of
`a_i` and `s=x_1+x_2+x_3`, the exact relaxed cap tail is

\[
\begin{aligned}
F(x)={}&3-s
 +(x_1+x_2-1)_+ +(x_1+x_3-1)_+\\
 &\hspace{35mm} +(x_2+x_3-1)_+.                         \tag{6.2}
\end{aligned}
\]

At `x_1=x_2=x_3=1/2`, one has `F=3/2`.  Conversely, the three positive
arguments in (6.2) have sum `2s-3` before positive parts, so

\[
 F(x)\ge3-s+(2s-3)_+\ge\frac32.                        \tag{6.3}
\]

Thus `K_1^LP=3/2`.  If exactly `k` columns are selected integrally, the
values for `k=0,1,2,3` are

\[
                            3,2,2,3.                    \tag{6.4}
\]

Indeed, selecting one column removes one source excess; selecting two
also overloads their unique common positive target; selecting all three
overloads all three common positive targets.  Hence

\[
 \boxed{K_1^{\mathbb Z}=2>\frac32=K_1^{\rm LP}.}        \tag{6.5}
\]

Therefore the weighted inequalities (3.4), although exact for fractional
feasibility, are not an integral Hall theorem for the trade matrix.
Disjoint union of `L` copies gives additive gap `L/2` in the abstract
compatible-column model.

For comparison, if one forgets the Johnson-square geometry and assumes
only ganged balanced columns, two columns already suffice for a sharper
gap `K^Z=1`, `K^LP=0`: on four shared rows use the core columns

\[
 \begin{pmatrix}1&1\\1&-1\\-1&1\\-1&-1\end{pmatrix}
\]

and pad each column with private arms.  One column can never give a gap,
because with integral data every breakpoint of
`sum_v(c_v+a_vx)_+`, `a_v in {0,+-1}`, on `[0,1]` is integral, so an
endpoint is optimal.  Thus two columns are minimal for the support-only
model, while Proposition 5.1 explains why the exact first-depth rectangle
geometry postpones the first obstruction to three columns.

---

## 7. Shared-trade coupling across depths

Let `mathcal Q` be a set of tagged lower and upper depths.  Assume first
that one switch family is physically compatible and additive at every
serviced depth:

\[
                 \mu_q^x=\mu_q+A_qx
                 \quad(q\in\mathcal Q).                 \tag{7.1}
\]

The same variable `x_e` occurs in every block.  For caps `b_q` and weights
`w_q>=0`, the exact additive relaxation is

\[
 \min_{0\le x\le1}
   \sum_qw_q\sum_v
       \bigl(\mu_q(v)-b_q+(A_qx)_v\bigr)_+.             \tag{7.2}
\]

### Theorem 7.1 (synchronized weighted deficiency)

The exact dual of (7.2) is

\[
\boxed{
 \max_{0\le\alpha_{q,v}\le w_q}
 \left\{
  \sum_q\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
  -\sum_e
   \left(
    \sum_q[\alpha_q(N_{q,e})-\alpha_q(P_{q,e})]
   \right)_+
 \right\}.}                                             \tag{7.3}
\]

#### Proof

The `z_(q,v)` minimizations bound `alpha_(q,v)` by `w_q`.  The coefficient
of the one shared variable `x_e` is

\[
 \sum_q\langle\alpha_q,a_{q,e}\rangle
 =\sum_q[\alpha_q(P_{q,e})-\alpha_q(N_{q,e})].
\]

Minimizing that coefficient times `x_e` over `[0,1]` gives the last term
of (7.3).  \(\square\)

The positive part in (7.3) is outside the depth sum.  In general

\[
 \left(\sum_q d_{q,e}\right)_+
       <\sum_q(d_{q,e})_+                                \tag{7.4}
\]

when a switch drains one depth and refills another.  The right side of
(7.4) is the false relaxation in which different depths choose the same
physical switch independently.

With a legal-selection polytope `P`, replace the final sum in (7.3) by

\[
 h_P\left(
   \left(\sum_q[\alpha_q(N_{q,e})-
                 \alpha_q(P_{q,e})]\right)_e
 \right).                                               \tag{7.5}
\]

Even if every separate `A_q` were TU, this would not prove simultaneous
integrality.  The relevant matrix is the vertical stack

\[
                       A^{\rm all}=egin{bmatrix}A_qend{bmatrix}_{q\in\mathcal Q}.
                                                               \tag{7.6}
\]

Vertical stacking does not preserve TU: the two one-row TU matrices
`[1 1]` and `[1 -1]` stack to a determinant-two matrix.  Thus the exact
universal matrix gate is TU of `A^all` together with an integral
description of the legal-selection polytope.  Equivalently, for the
unconstrained cube, every subset of stacked target rows must admit a
Ghouila--Houri signing whose signed sum in every trade column lies in
`{-1,0,1}`.

If (7.1) fails, there is no honest stacked incidence matrix.  Let
`mathfrak X` be the set of complete physical configurations and let
`mu_q^X` be the exact resulting histograms.  The convexified histogram
relaxation has dual

\[
 \boxed{
 \max_{0\le\alpha_{q,v}\le w_q}
 \left\{
  -\sum_qb_q\alpha_q(V_q)
  +\min_{X\in\mathfrak X}
       \sum_q\langle\alpha_q,\mu_q^X\rangle
 \right\}.}                                             \tag{7.7}
\]

The inner configuration minimum separates into the column penalties of
(7.3) exactly when simultaneous additivity and cube feasibility hold.
An exponential state-DAG can encode the same optimization as a path
problem, but that tautological construction merely enumerates
`mathfrak X`; it supplies no target-flow integrality theorem.

---

## 8. The precise surviving routing gate

The flow claim leaves the following theorem to prove.

### Routing gate

Construct a physical multiframe trade family and prove one of the two
alternatives below.

**Additive alternative.**  Identify a legal-selection polytope `P` and
prove exact simultaneous additivity on every protected tagged depth.
Then prove both

\[
\begin{aligned}
&\max_{0\le\alpha_{q,v}\le w_q}
 \left\{
  \sum_q\langle\alpha_q,\mu_q-b_q\mathbf1\rangle
  -h_P\left(
    \left(\sum_q[\alpha_q(N_{q,e})-
                  \alpha_q(P_{q,e})]\right)_e
          \right)
 \right\}=o(W),                                        \tag{8.1}\\
&K^{\mathbb Z}-K^{\rm LP}=o(W).                        \tag{8.2}
\end{aligned}
\]

Equation (8.1) is the exact synchronized weighted-cut/deficiency gate.
Equation (8.2) requires stacked TU, a proof specialized to the actual
right-hand side, or an integral absorber.  Per-depth Hall expansion and
per-depth rounding are insufficient.

**Nonadditive alternative.**  Work with the exact configurations in
(7.7), prove its obstruction is `o(W)`, and round the convexified
histogram to one physical configuration with only `o(W)` additional cap
tail.  Equivalently, give a dynamic construction in which each toggle is
charged its net gain across all protected depths; gains cannot be charged
separately by depth or separately by arm.

The fixed-factor special question that remains open after the determinant
audit is narrow and explicit:

> Does the actually compatible, simultaneously additive selected MSW
> subfamily have a stacked TU matrix, or at least `o(W)` integrality gap
> on the canonical cap right-hand side?

No existing local identity answers it.  Conversely, because a
coefficient-one proof must change coordinate frames to evade the fixed-pair
capacity deficit, the determinant-two relabeled-square obstruction cannot
be dismissed without showing how the multiframe construction restricts or
rounds those columns.

This is the surviving routing theorem.  Ordinary convex-cost max-flow and
ordinary indicator Hall cuts solve a strictly weaker independent-arm,
independent-depth problem.

