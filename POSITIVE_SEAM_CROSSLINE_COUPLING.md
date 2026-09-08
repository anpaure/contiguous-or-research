# Positive seam must live in a cross-line desert

## 1. Outcome

This note couples the first-dangerous seam functional to the mixed
cross-line variational gate.  The coupling is finite and elementary.

Fix a family of long directed peak plateaux.  Let `V` be the union of their
plateau vertices and let `Lambda` be the union of their complete coordinate
lines.  The cross-line slack is

\[
                    \Delta_a={|\Lambda|-|V|\over a^2}\ge0.       \tag{1.1}
\]

For every plateau except the first in word order, choose the clipped part
of its predecessor gap which occurs in the first-dangerous seam sum.  Let
`C` be the union of these clipped gap cores and put

\[
              \Gamma_a={|C|\over a^2},\qquad
              \Gamma_{0,a}={|C\setminus\Lambda|\over a^2}.       \tag{1.2}
\]

Then

\[
             \boxed{\Gamma_a\le\Gamma_{0,a}+\Delta_a.}           \tag{1.3}
\]

Thus a large seam has only two possible geometric sources:

1. unused capacity inside the union of the selected long-plateau lines;
2. predecessor-gap positions lying on none of those lines.

The second source is called the **cross-line desert**.  Equation (1.3) is
strictly more informative than the scalar seam upper bound because it
retains where the seam positions lie.

For a one-atom profile

\[
                         \mu_a\Longrightarrow2\delta_x,
             \qquad {4\over3}\le x\le{3\over2},                 \tag{1.4}
\]

the coupling becomes quantitative.  The seam linearity and cross-line
envelope below require only the atom hypothesis.  The reservoir conclusions
(1.6) and (1.8) additionally assume the inherited selected-middle-order
hypothesis `D=o(a^2)`.  Along a further subsequence there is
one threshold-independent clipped-gap density `Gamma` such that, for every
fixed `c<x`,

\[
                         H(c)=(x-c)\Gamma.                       \tag{1.5}
\]

This linearity is a genuine multiscale restriction.  In particular, the
threshold-by-threshold scalar choice of `H(c)` in
`GENERAL_BOUNDARY_RESERVOIR.md`, Section 7, is not the seam profile of an
actual pure atom unless its quotient `H(c)/(x-c)` is constant.

The exact gap-loss formula and the quadratic reservoir law force

\[
             \boxed{\Gamma\ge {4-x\over4}(3-2x).}                \tag{1.6}
\]

The mixed cross-line gate gives a closed upper bound on `Delta`.  Put

\[
 u=x-1,
 \qquad
 u_*={8-2\sqrt3\over13}=0.348\ldots .                           \tag{1.7}
\]

Then no atom (1.4) is geometrically possible when `u>u_*`, independently
of its seam mass.  When `1/3<=u<=u_*`, every possible atom must satisfy

\[
 \boxed{
 \liminf\Gamma_0
 \ge { -5+25u-24u^2\over4}>0.}                                  \tag{1.8}
\]

Here `Gamma_0` is the limiting density of clipped predecessor-gap positions
which lie on none of the selected long-plateau lines.  Consequently (1.8)
excludes a nontrivial positive-seam class: a surviving atom cannot have its
macroscopic seam carried inside the selected line union.  It must maintain
a positive-density, three-direction level desert in the correct locations
of the word.

The remaining endpoint is real at the level of all current variational
ledgers.  The data

\[
 \mu=2\delta_{4/3},\qquad
 \nu_x=\nu_y=\nu_z={\bf1}_{[-1/3,1/3]},du,
 \qquad \Gamma=\Gamma_0={2\over9}                               \tag{1.9}
\]

satisfy the strongest mixed cross-line gate with equality, satisfy (1.3)
and (1.6), and give the linear seam

\[
                         H(c)=\left({4\over3}-c\right){2\over9}.
                                                                         \tag{1.10}
\]

This is an abstract joint profile, not a word construction.  It is a
precise no-go result for the present method: after (1.8), the missing
theorem must control the ordering of the cross-line-desert points, not just
the plateau lengths, line levels, additive triples, and total seam mass.

## 2. The finite seam--line-union coupling

Let `P_1,...,P_m` be selected directed peak plateaux in word order, with
edge lengths `lambda_j`, and suppose their complete coordinate lines are
distinct.  The latter is automatic when `lambda_j>ba` for one fixed
`b>1`, apart from a negligible exceptional family in the atomic
application.

For `j>=2`, let `g_(j-1)` be the number of complement positions between
`P_(j-1)` and `P_j` in the plateau vertex-union convention, and put

\[
                         h_j=\min\{g_{j-1},L-\lambda_j\},
             \qquad L=4a+2.                                   \tag{2.1}
\]

Choose any `h_j` positions from that predecessor gap and call the chosen
set `C_j`.  The sets `C_j` are pairwise disjoint and avoid every selected
plateau vertex.  Put

\[
 C=\bigcup_{j=2}^m C_j,
 \qquad
 V=\bigcup_{j=1}^m V(P_j),
 \qquad
 \Lambda=\bigcup_{j=1}^m \ell(P_j).                            \tag{2.2}
\]

Every plateau vertex lies on its complete line, so `V subseteq Lambda`.
Moreover

\[
                      C\cap\Lambda\subseteq\Lambda\setminus V. \tag{2.3}
\]

Therefore

\[
 |C|=|C\setminus\Lambda|+|C\cap\Lambda|
     \le |C\setminus\Lambda|+|\Lambda\setminus V|.             \tag{2.4}
\]

Division by `a^2` proves (1.3).  Notice that no run-spectrum, atomicity, or
limit argument enters this proof.

There is also a weighted version.  For a first-dangerous threshold `c`, set

\[
 w_j={\lambda_j-ca\over a},
 \qquad
 H_{0,a}(c)={1\over a^2}
       \sum_{j=2}^m w_j|C_j\setminus\Lambda|.                   \tag{2.5}
\]

Since `0<w_j<=2-c`,

\[
 H_a(c)\le H_{0,a}(c)+(2-c)\Delta_a.                            \tag{2.6}
\]

For a mixed profile supported above a fixed `b>1`, the contribution of the
`o(a)` exceptional plateaux below `ba` is `o(1)` in (2.6).  Thus (2.6)
already gives a general positive-seam dichotomy.  The atomic case is
stronger because all regular weights are asymptotically equal and (1.3),
rather than (2.6), can be used.

## 3. Cross-line slack is exactly the variational slack

Let `n_x,n_y,n_z` be the selected line counts, let

\[
 m=n_x+n_y+n_z,
 \qquad T=\sum_P|t(P)|,                                      \tag{3.1}
\]

and let `I` be the number of genuinely intersecting pairs of selected lines
in different directions.  Let `J` be the number of points incident with
selected lines in all three directions.

The sum of the selected complete-line cardinalities is

\[
                         2am-T+m.                              \tag{3.2}
\]

Inclusion--exclusion is exact because at most three coordinate lines pass
through one point:

\[
                         |\Lambda|=2am-T+m-I+J.                \tag{3.3}
\]

The selected plateau vertex intervals are pairwise disjoint except for
shared word endpoints.  If `omega=O(m)` counts those endpoint overlaps,
then

\[
                         |V|=\sum_P\lambda(P)+m-\omega.        \tag{3.4}
\]

Consequently

\[
 a^2\Delta_a
 =2am-T-\sum_P\lambda(P)-I+J+\omega.                         \tag{3.5}
\]

At a continuity threshold `b>1`, use the notation of
`MIXED_PROFILE_CROSSLINE.md`:

\[
 f=\sum_i\alpha_i,
 \quad s_2=\sum_i\alpha_i^2,
 \quad \tau=\sum_i\int|t|\,d\nu_i(t),
 \quad \eta=\hbox{nonintersection density},
 \quad \theta=\hbox{triple density}.                          \tag{3.6}
\]

Passing to a common subsequence in (3.5) gives

\[
 \boxed{
 \Delta=
 2f-\tau-\ell-{f^2-s_2\over2}+\eta+\theta.}                  \tag{3.7}
\]

Thus `Delta>=0` is exactly the strongest mixed cross-line inequality.  The
new information in (1.3) is that its slack has a physical meaning: it is
the number of line-union points not consumed by the long plateau blocks.

## 4. Atomic seam linearity

Assume (1.4).  Fix a small `epsilon>0` and call a plateau regular when

\[
                    |\lambda(P)/a-x|<\varepsilon.              \tag{4.1}
\]

Weak convergence on the compact interval `[0,2]` gives

\[
 \#\{P:P\hbox{ is not regular}\}=o(a),
 \qquad
 {1\over a}\sum_P|\lambda(P)/a-x|=o(1)                         \tag{4.2}
\]

after sending `a` to infinity and then `epsilon` to zero.  In particular,

\[
                         \sum_P|\lambda(P)-xa|=o(a^2).         \tag{4.3}
\]

Choose two fixed thresholds `c_1,c_2<x`.  Apart from `o(a)` exceptional
plateaux, their dangerous lists are the same regular family.  Inserting or
deleting one exceptional plateau changes the sum of clipped predecessor-gap
lengths by only `O(a)`.  Changing a regular cap from
`L-lambda(P)` to `(4-x)a` changes it by at most
`|lambda(P)-xa|+O(1)`.  Equations (4.2)--(4.3) therefore give a common
quantity

\[
 \Gamma_a={1\over a^2}\sum_{P\ {\mathrm{regular}}}
       \min\{g_{\rm pred}(P),(4-x)a\}+o(1),                    \tag{4.4}
\]

independent of the fixed threshold.  Take a further subsequence on which
`Gamma_a -> Gamma`.

For every fixed `c<x`, the exceptional seam contribution is `o(1)`, while

\[
 \begin{aligned}
 H_a(c)
 &= {1\over a^3}\sum_{P\ {\mathrm{regular}}}
       (\lambda(P)-ca)
       \min\{g_{\rm pred}(P),L-\lambda(P)\}+o(1)\\
 &= (x-c)\Gamma_a+o(1).                                       \tag{4.5}
 \end{aligned}
\]

The error estimate uses (4.3) and the uniform `O(a)` bound on every clipped
gap.  Passing to the limit proves (1.5).

## 5. A sharper atomic boundary bound

The total complement of the regular plateau vertex union has size

\[
                         (3-2x+o(1))a^2.                       \tag{5.1}
\]

For one internal complement gap of length `g`, the exact number of positions
which have neither a forward nor a backward gap-contained length-`L` window
is at most

\[
 I_L(g)\le\min\{g,L\}.                                        \tag{5.2}
\]

Put `B=(4-x)a`.  Uniformly over regular successors,

\[
 \min\{g,L\}
 \le\left({4\over4-x}+o(1)\right)\min\{g,B\}.                 \tag{5.3}
\]

The two outside word gaps cost only `O(a)`, and the `o(a)` exceptional
successors cost `o(a^2)`.  Every other complement position belongs to the
dangerous-free one-sided reservoir `R_c`.  Hence

\[
 3-2x
 \le \limsup {|R_c|\over a^2}+{4\over4-x}\Gamma.              \tag{5.4}
\]

Under `D=o(a^2)`, the audited quadratic reservoir law gives

\[
                         \limsup {|R_c|\over a^2}
                         \le {9\over4}c^2                       \tag{5.5}
\]

for every fixed `0<c<2/3`.  First take the large-`a` limit and only then
send `c` to zero.  Equations (5.4)--(5.5) prove (1.6).

This improves the coefficient `1/2` obtained by using the worst possible
long-plateau cap `L-2a`.  The improvement is available because an atom fixes
the asymptotic cap at `(4-x)a`.

## 6. A closed atomic cross-line envelope

Put `u=x-1`, so `1/3<=u<=1/2`.  At a tail threshold tending upward to `x`,
the selected direction masses satisfy

\[
 0\le\alpha_i\le2(1-u),
 \qquad \alpha_x+\alpha_y+\alpha_z=2.                          \tag{6.1}
\]

The strongest cross-line union capacity is

\[
 2+{1\over2}\sum_i\alpha_i^2-\tau+\eta+\theta.                \tag{6.2}
\]

For a level `v`, the total nonintersecting level mass in either one other
direction is at most `(|v|-u)_+`.  Counting every nonintersecting pair at
both endpoints gives the inherited estimate

\[
                 \eta\le\sum_i\int(|v|-u)_+\,d\nu_i(v).        \tag{6.3}
\]

Therefore

\[
 \tau-\eta\ge\sum_i h_u(\alpha_i),                              \tag{6.4}
\]

where centered interval compression gives

\[
 h_u(\alpha)=
 \begin{cases}
  \alpha^2/4,&0\le\alpha\le2u,\\
  u\alpha-u^2,&2u\le\alpha\le2(1-u).
 \end{cases}                                                   \tag{6.5}
\]

The discrete one-dimensional Riesz rearrangement inequality, followed by
the limit, gives for direction masses sorted as
`alpha>=beta>=gamma`

\[
 \theta\le
 \Theta(\alpha,\beta,\gamma)
 =\beta\gamma-{1\over4}(\beta+\gamma-\alpha)_+^2.             \tag{6.6}
\]

Define

\[
 A_u(t)={t^2\over2}-h_u(t).                                    \tag{6.7}
\]

Then the part of (6.2) above the constant `2` is at most

\[
                  \sum_i A_u(\alpha_i)+\Theta(\alpha_x,
                                                   \alpha_y,
                                                   \alpha_z). \tag{6.8}
\]

### Lemma 6.1

For `1/3<=u<=1/2`, the maximum in (6.8), subject to (6.1), is

\[
 M(u)=\max\left\{{2\over3},
                  2-6u+{13\over2}u^2\right\}.                 \tag{6.9}
\]

#### Proof

Sort the masses as `a>=y>=z`, and put `r=y+z=2-a`.  At fixed `a`, the
function

\[
                         A_u(y)+A_u(z)+yz                         \tag{6.10}
\]

is maximized at `y=z=r/2`.  Indeed, as a function of `y` with
`z=r-y`, its second derivative is

\[
                         A_u''(y)+A_u''(z)-2\le0,                \tag{6.11}
\]

piecewise, and the first derivative is continuous across the sole break
at `2u`.  Symmetry then puts the maximum at `y=z`.  The subtraction in
the second term of (6.6), when present, depends only on `a` and `r`, so it
does not change this conclusion.

Now `2/3<=a<=2(1-u)` and `y=z=1-a/2<=2u`.  Substitution gives three
elementary ranges.  On `a<=2u`, with necessarily `a<=1`, the expression is

\[
                         {1\over2}+{a\over2}-{3a^2\over8},       \tag{6.12}
\]

which is nonincreasing for `a>=2/3`.  On `2u<=a<=1` it is

\[
                         u^2+{1\over2}
                         +\left({1\over2}-u\right)a-{a^2\over8}, \tag{6.13}
\]

whose derivative is also nonpositive on the stated domain.  On
`1<=a<=2(1-u)` it is

\[
                         u^2+{3\over2}
                         -\left({3\over2}+u\right)a+{7a^2\over8}, \tag{6.14}
\]

which is convex.  Hence the global maximum is attained either at

\[
 (a,y,z)=\left({2\over3},{2\over3},{2\over3}\right)             \tag{6.15}
\]

or at

\[
 (a,y,z)=\bigl(2(1-u),u,u\bigr).                                \tag{6.16}
\]

The corresponding values are `2/3` and
`2-6u+(13/2)u^2`, proving (6.9).  \(\square\)

The required plateau edge mass is `2x=2+2u`.  Equations (6.2) and
(6.9) imply

\[
                         2u\le M(u).                             \tag{6.17}
\]

The second branch of (6.9) meets `2u` at

\[
                         u_*={8-2\sqrt3\over13}.                 \tag{6.18}
\]

For every larger `u`, both branches of `M(u)` are strictly below `2u`.
This proves the unconditional atomic exclusion claimed after (1.7).

For `1/3<=u<=u_*`, the second branch is the active one and the cross-line
slack obeys

\[
                         \Delta\le
              2-8u+{13\over2}u^2.                              \tag{6.19}
\]

## 7. Forced cross-line desert in every remaining atom

Use the same regular plateau family in Sections 4--6 and choose the clipped
gap cores from Section 4.  Define

\[
                         \Gamma_0=\liminf
                         {|C\setminus\Lambda|\over a^2}.        \tag{7.1}
\]

Equations (1.3), (1.6), and (6.19) give

\[
 \begin{aligned}
 \Gamma_0
 &\ge {4-x\over4}(3-2x)-\Delta\\
 &\ge {4-x\over4}(3-2x)
       -\left(2-8u+{13\over2}u^2\right)\\
 &= {-5+25u-24u^2\over4}.                         \tag{7.2}
 \end{aligned}
\]

The quadratic in the last line is positive throughout
`1/3<=u<=u_*`; its smaller zero is `(25-sqrt(145))/48<1/3`.
This proves (1.8).

At the two ends of the surviving interval, (7.2) gives

\[
 \Gamma_0\ge{1\over6}\quad(x=4/3),
 \qquad
 \Gamma_0\ge {4-x\over4}(3-2x)>0\quad(x=1+u_*).                \tag{7.3}
\]

Thus a positive seam cannot merely be inserted among already selected
long lines.  A macroscopic portion of its clipped predecessor gaps must be
made from points whose `x`, `y`, and `z` levels are all absent from the
corresponding long-plateau level sets.

## 8. The exact abstract survivor at `x=4/3`

Take

\[
                         \mu=2\delta_{4/3}.                      \tag{8.1}
\]

For each of the three directions take normalized level measure

\[
                         \nu_i={\bf1}_{[-1/3,1/3]},du.          \tag{8.2}
\]

Then

\[
 \alpha_i={2\over3},\qquad
 s_2={4\over3},\qquad
 \tau={1\over3},\qquad
 \eta=0.                                                       \tag{8.3}
\]

The centered additive-triple density is

\[
 \theta=\left({2\over3}\right)^2
       -{1\over4}\left({2\over3}\right)^2={1\over3}.          \tag{8.4}
\]

Substitution in the strongest mixed cross-line expression gives

\[
 2f-\tau-{f^2-s_2\over2}+\eta+\theta
 =4-{1\over3}-{4/3}+{1\over3}
 ={8\over3}=\ell.                                               \tag{8.5}
\]

Hence `Delta=0`.  The selected line union has normalized area `8/3`, so
its complement—the cross-line desert—has normalized area `1/3`.

Choose abstract clipped-gap density

\[
                         \Gamma=\Gamma_0={2\over9},              \tag{8.6}
\]

which fits inside that desert.  Then

\[
 H(c)=\left({4\over3}-c\right){2\over9}                         \tag{8.7}
\]

for every fixed `c<4/3`.  The sharpened boundary inequality is met exactly
as `c` decreases to zero:

\[
 {4\over4-4/3}\Gamma={3\over2}{2\over9}={1\over3}=3-2x.        \tag{8.8}
\]

The ordinary seam upper bounds, mass law, weighted-supply law, line
capacity, and general boundary inequalities all hold as well.

Equations (8.1)--(8.8) do **not** construct a permutation word.  They show
that the following data are mutually consistent:

* the plateau length measure;
* the exact threshold dependence of the seam;
* all three direction and level marginals;
* pair intersections and additive triples;
* zero cross-line slack; and
* enough cross-line-desert area to hold every required clipped gap core.

Therefore a further scalar or static level-set optimization cannot exclude
this endpoint.  The missing statement must use how the desert points are
ordered between successive directed plateaux—for example, prove that
placing at least `2a^2/9` such positions in clipped predecessor gaps creates
enough cheap threshold runs, forces additional long plateaux, or violates a
transition-sign resource.

## 9. Theorem ledger

### Proved here

* The finite seam--line-union coupling (1.3) and its weighted form (2.6).
* The identity (3.7): cross-line variational slack is precisely unused
  selected-line-union capacity.
* Atomic multiscale seam linearity `H(c)=(x-c)Gamma`.
* The sharpened atomic boundary lower bound (1.6).
* The closed atomic cross-line envelope (6.9).
* Unconditional exclusion of `2 delta_x` for
  `x>1+(8-2 sqrt(3))/13`.
* The positive cross-line-desert lower bound (1.8) for every remaining atom.

### Exact limitation / no-go

* The enriched abstract profile (8.1)--(8.8) passes all the proved scalar,
  seam, line-level, pair-intersection, additive-triple, and new
  seam--line-union constraints.
* It is not asserted to be geometrically realizable by one permutation.

### Still open

* A transition theorem controlling the order of cross-line-desert points.
* Exclusion of the endpoint `2 delta_(4/3)`.
* Extension of the quantitative desert bound from atoms to arbitrary mixed
  profiles without introducing a threshold-dependent desert measure.
* The full three-box obstruction and the Boolean-lattice conjecture.
