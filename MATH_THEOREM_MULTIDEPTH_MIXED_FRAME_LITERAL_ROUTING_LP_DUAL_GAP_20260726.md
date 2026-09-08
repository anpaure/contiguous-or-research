# Common-choice multidepth mixed-frame literal routing

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
independent rankwise rounding is used.

## 0. Verdict

The genuinely multidepth problem has one variable for an entire physical
route. A route contains its owner support, coordinate frame, cyclic order,
and all lower and upper literal shadows through the protected depth. The
same variable therefore occurs in every depth row.

For an augmented catalogue with owner-repair and target-hole columns, the
exact fractional primal is

\[
 \begin{aligned}
 \min\quad&
 \sum_R d_Rx_R+\sum_X\kappa_Xe_X+\sum_t w_th_t,\\
 \text{subject to}\quad&
 \sum_{R:X\in M(R)}x_R+e_X=1 &&(X\text{ a middle owner}),\\
 &\sum_Ra_{tR}x_R+h_t\ge1 &&(t\text{ a typed target}),\\
 &x_R,e_X,h_t\ge0.
 \end{aligned}                                             \tag{0.1}
\]

Here a typed target is \(t=(q,\sigma,T)\), with
\(\sigma\in\{-,+\}\), and \(a_{tR}\) is its actual number of physical
occurrences in route \(R\). Its exact dual is

\[
 \begin{aligned}
 \max\quad&\sum_ty_t-\sum_Xz_X,\\
 \text{subject to}\quad&
 0\le y_t\le w_t,\qquad z_X\ge-\kappa_X,\\
 &\sum_ta_{tR}y_t-\sum_{X\in M(R)}z_X\le d_R
                                      &&(R\text{ a route}).
 \end{aligned}                                             \tag{0.2}
\]

Thus a dual witness prices all depths at once and tests each whole route,
not one independently chosen shadow at each depth.

There is a valid conditional integrality theorem. The LP is integral if
the common-route language has a single-commodity network realization with
all owner and physical-target requirements represented by integral arc
bounds. Equivalently, the history carried by a prefix may be forgotten
when two prefixes reach the same physical target only if their legal suffix
languages agree. This is the exact running-state condition needed for a
laminar prefix flow.

Actual mixed pair frames do not have that property. Equal physical shadows
can retain different unused pair frames and different legal cyclic
continuations. Keeping the frame tag restores a prefix forest but ceases to
test literal target equality; forgetting the tag creates nonlaminar
mergers.

There is also an unconditional physical nonintegrality result. For every
power of two \(\ell\) with

\[
 H\le\ell/2,\qquad 3(\ell-1)\le m-2,
\]

three genuine recursive-frame necklaces contain the owner minor

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad\det=2.                                             \tag{0.3}
\]

Each column is a single legal cycle carrying its complete common
multidepth lower and upper flag catalogue. In the restricted augmented
instance, the fractional singleton residual is
\(3(2\ell-2)/2\), while the integral residual is \(4\ell-3\). The
additive gap is \(\ell\) and the ratio tends to \(4/3\).
The gap remains genuinely multidepth with positive target-hole weights:
if owner repair costs \(20H\) and every lower and upper target hole costs
one, the integral optimum exceeds the fractional optimum by at least
\(8H\ell\) on the target rows touched by the gadget.

Taking disjoint coordinate-orbit copies gives at least
\(\Omega(W/\ell^2)\) independent gadgets, hence total additive gap
\(\Omega(W/\ell)\). For \(\ell=\Theta(H)\) this is
\(\Omega(W/H)\). Therefore neither nested prefixes, submodularity of
coverage, nor a hidden total-unimodularity argument can round the genuine
joint LP. This is a restricted-catalogue obstruction, not a global
coefficient-one no-go: routes crossing different gadgets may supply the
missing higher-order inequalities or repairs.

## 1. Atomic physical routes

Let

\[
 \mathcal O=\binom{[2m]}m
\]

be the owner set. Fix a protected depth \(H\), and put

\[
 \mathcal T
 =\{(q,\sigma,T):
       1\le q\le H,\ \sigma\in\{-,+\},\
       |T|=m+\sigma q\}.                                  \tag{1.1}
\]

The notation \(|T|=m+\sigma q\) means \(m-q\) for \(\sigma=-\) and
\(m+q\) for \(\sigma=+\).

An atomic physical route \(R\) consists of:

1. a legal coordinate frame and a legal ordered pair-flip cycle or path;
2. its middle-owner set \(M(R)\subseteq\mathcal O\);
3. for every owner position of \(R\), the actual forward lower and
   backward upper literal flags through depth \(H\);
4. any radius, collar, or tail certificate required by the declared
   compiler.

For \(t=(q,\sigma,T)\), let

\[
 a_{tR}
 =\#\{\text{certified positions of }R
          \text{ whose signed depth-\(q\) target is }T\}.   \tag{1.2}
\]

For a two-sided rainbow route, \(a_{tR}\in\{0,1\}\). No frame tag is
retained in \(t\): two routes in different pair frames which produce the
same physical set \(T\) meet the same target row.

The word “common-choice” means precisely that there is one variable
\(x_R\) for all of (1.2). Replacing it by variables \(x_{R,q,\sigma}\)
changes the problem: it permits the frame, cycle, and owner partition to
depend on the depth.

## 2. The exact augmented primal and dual

Let \(d_R\ge0\) be the interface or component cost of route \(R\).
Let \(\kappa_X\ge0\) be the cost of repairing owner \(X\) outside the route
bank, and let \(w_t\ge0\) be the cost of one missing typed target. Consider
the fractional programme

\[
 \boxed{
 \begin{aligned}
 {\rm(P)}\qquad
 \min\quad&
 \sum_R d_Rx_R+\sum_X\kappa_Xe_X+\sum_t w_th_t,\\
 \text{subject to}\quad&
 \sum_{R:X\in M(R)}x_R+e_X=1 &&(X\in\mathcal O),\\
 &\sum_Ra_{tR}x_R+h_t\ge1 &&(t\in\mathcal T),\\
 &x_R,e_X,h_t\ge0.
 \end{aligned}}                                           \tag{2.1}
\]

The integral programme \({\rm(P)}_{\mathbb Z}\) requires the route
variables to be integral. The owner equations then make every nonempty
route variable \(0\) or \(1\), and make \(e_X\in\{0,1\}\). At an optimum
with \(w_t>0\), one may also take \(h_t\in\{0,1\}\).

Specializations include:

* exact owner partition: omit \(e_X\), equivalently
  \(\kappa_X=+\infty\);
* pure target-hole minimization: \(d_R=0\), \(w_t=1\);
* low-component routing: put the appropriate cut or path cost in \(d_R\);
* radius-thinned exact SCD incidence: the total certified mass in each
  typed layer is its number of targets, so zero holes force exact
  multiplicity one.

### Theorem 2.1 (common multidepth coverage dual)

The dual of (2.1) is

\[
 \boxed{
 \begin{aligned}
 {\rm(D)}\qquad
 \max\quad&\sum_{t\in\mathcal T}y_t-\sum_{X\in\mathcal O}z_X,\\
 \text{subject to}\quad&
 0\le y_t\le w_t &&(t\in\mathcal T),\\
 &z_X\ge-\kappa_X &&(X\in\mathcal O),\\
 &\sum_ta_{tR}y_t-\sum_{X\in M(R)}z_X\le d_R
                                      &&(R\in\mathscr R).
 \end{aligned}}                                           \tag{2.2}
\]

If owner repair is forbidden, the variables \(z_X\) are free.

#### Proof

Give the target inequalities the nonnegative multipliers \(y_t\), in the
form

\[
                         1-\sum_Ra_{tR}x_R-h_t\le0,
\]

and give the owner equalities free multipliers \(z_X\), in the form

\[
                         \sum_{R:X\in M(R)}x_R+e_X-1=0.
\]

The Lagrangian has constant term

\[
                         \sum_ty_t-\sum_Xz_X.
\]

Its coefficients on \(h_t,e_X,x_R\) are respectively

\[
 w_t-y_t,\qquad
 \kappa_X+z_X,\qquad
 d_R-\sum_ta_{tR}y_t+\sum_{X\in M(R)}z_X.
\]

Their nonnegativity is exactly the constraint system (2.2). Conversely,
those inequalities make the infimum of the Lagrangian equal its constant
term. Ordinary finite-dimensional LP duality proves the result.
\(\square\)

The route inequality in (2.2) is indivisible. It tests the sum of all
prices collected by one physical route across all depths and both signs.
There is no valid replacement by separate inequalities for separately
chosen depth-\(q\) routes.

## 3. Exact lower/upper quota version

Sometimes literal routing requires prescribed integral lower and upper
target multiplicities rather than one-sided coverage. Let
\(\ell_t,u_t\in\mathbb Z_{\ge0}\), with \(\ell_t\le u_t\), and consider

\[
 \boxed{
 \begin{aligned}
 {\rm(Q)}\qquad
 \min\quad&\sum_Rd_Rx_R,\\
 \text{subject to}\quad&
 \sum_{R:X\in M(R)}x_R=1 &&(X\in\mathcal O),\\
 &\ell_t\le\sum_Ra_{tR}x_R\le u_t &&(t\in\mathcal T),\\
 &x_R\ge0.
 \end{aligned}}                                           \tag{3.1}
\]

### Theorem 3.1 (common multidepth quota dual)

The exact dual of (3.1) is

\[
 \boxed{
 \begin{aligned}
 {\rm(QD)}\qquad
 \max\quad&
 \sum_t\ell_t\alpha_t-\sum_tu_t\beta_t-\sum_Xz_X,\\
 \text{subject to}\quad&
 \alpha_t,\beta_t\ge0,\qquad z_X\in\mathbb R,\\
 &\sum_ta_{tR}(\alpha_t-\beta_t)
       -\sum_{X\in M(R)}z_X\le d_R
                                      &&(R\in\mathscr R).
 \end{aligned}}                                           \tag{3.2}
\]

#### Proof

Use multipliers \(\alpha_t\ge0\) on
\(\ell_t-\sum_Ra_{tR}x_R\le0\), multipliers \(\beta_t\ge0\) on
\(\sum_Ra_{tR}x_R-u_t\le0\), and free \(z_X\) on the owner equalities
written as in Theorem 2.1. Minimization over \(x_R\ge0\) gives precisely
the route inequalities in (3.2). \(\square\)

Taking \(\ell_t=u_t=1\) gives exact once-only SCD routing. Prescribed
floor/ceiling MWB quotas are another instance. Mobile MWB quotas require
one additional common choice of the upper-quota cells; they must not be
selected independently after the route variables have been rounded.

## 4. Farkas form and the rankwise fallacy

With \(d_R=0\), (3.2) says that the fractional common-route system is
feasible if and only if every \((\alpha,\beta,z)\) satisfying

\[
 \sum_ta_{tR}(\alpha_t-\beta_t)
 \le\sum_{X\in M(R)}z_X
 \qquad(R\in\mathscr R)                                   \tag{4.1}
\]

also satisfies

\[
 \sum_t\ell_t\alpha_t-\sum_tu_t\beta_t
 \le\sum_Xz_X.                                             \tag{4.2}
\]

Both sums over \(t\) range over all depths and both signs.

If a separate variable \(x_R^{q,\sigma}\) is introduced for each typed
layer, then (4.1) is replaced by one family of route inequalities per
layer. Its dual is the direct sum of the rankwise duals. That relaxation
may be feasible even when (4.1)--(4.2) fail, because it uses incompatible
owner partitions or incompatible cyclic orders at different depths.

Thus “Hall at every depth” is not the common-choice theorem. The exact
fractional statement is one Farkas inequality against every simultaneous
price field \((\alpha_t-\beta_t)_{t\in\mathcal T}\).

## 5. When prefix laminarity really gives integrality

There are two valid sufficient structures. Neither is implied merely by
the set inclusions among the shadows of one route.

### 5.1 Laminar row supports

For every owner and typed target define subsets of the route catalogue

\[
 \mathscr R_X=\{R:X\in M(R)\},
 \qquad
 \mathscr R_t=\{R:a_{tR}=1\}.                             \tag{5.1}
\]

### Proposition 5.1 (literal laminar-support criterion)

Assume all routes are target-simple, and assume the family

\[
 \{\mathscr R_X:X\in\mathcal O\}
 \cup\{\mathscr R_t:t\in\mathcal T\}                      \tag{5.2}
\]

is laminar as a family of subsets of the column set \(\mathscr R\).
Then its incidence matrix is totally unimodular. Consequently every
bounded version of (3.1) with integral right-hand sides has integral
vertices.

#### Proof

The incidence matrix of a laminar set family is totally unimodular. One
proof orders the atoms by a depth-first traversal of the laminar inclusion
forest: every row becomes an interval, and the resulting interval matrix
has the consecutive-ones property. Transposition preserves total
unimodularity. Adding identity rows for variable bounds preserves it.
\(\square\)

The shadows

\[
 L_1(R)\supset L_2(R)\supset\cdots\supset L_H(R)
\]

are laminar as subsets of the ground coordinates inside one column. This
is not condition (5.2), which asks whether all columns producing one
physical target form laminar subsets of the route catalogue. Mixed-frame
target collisions concern the latter family.

### 5.2 A common prefix network

Call the catalogue network-realizable if there is one directed network
with integral supplies and integral lower and upper arc bounds such that:

1. every legal atomic owner route is an \(s\)-\(t\) flow path;
2. choosing one route at every owner is exactly the decomposition of one
   feasible single-commodity flow;
3. for each typed physical target \(t\), there is a distinguished arc
   \(e_t\), and a path uses \(e_t\) exactly \(a_{tR}\) times;
4. all route and repair costs are arc-additive.

### Proposition 5.2 (common-network integrality)

For a network-realizable catalogue, both (2.1) and (3.1) have integral
optimal route decompositions whenever their data are integral.

#### Proof

In the extended arc formulation the problems are min-cost
single-commodity flows with integral supplies and integral arc bounds.
The node-arc incidence matrix is totally unimodular, so an integral optimal
arc flow exists. Integral flow decomposition gives integral route
multiplicities. \(\square\)

The nontrivial hypothesis is the permission to merge histories at the
arc \(e_t\). If two route prefixes reach the same target \(t\), merging
them in a single-commodity network permits their suffixes to recombine.
This creates no spurious route if and only if all merged states have the
same legal suffix language, or an equivalent running-intersection state
description exists.

For a fixed tagged pair frame, the deletion-prefix tree retains enough
state and is a genuine network. Across mixed frames, the same physical
target can retain different unused split pairs, different cyclic phases,
and different legal successors. Their suffix languages differ. Keeping
those states separate restores a forest but counts equal physical targets
as different tagged targets. Identifying them restores literal coverage
but destroys the common-network hypothesis.

## 6. Why submodular coverage alone does not close the LP

For a route subfamily \(\mathcal A\), put

\[
 F(\mathcal A)
 =\sum_{t\in\mathcal T}w_t
    \mathbf1_{\{\exists R\in\mathcal A:a_{tR}>0\}}.         \tag{6.1}
\]

This is a monotone submodular set function. That fact is useful for
fractional coverage and greedy estimates, but it is not an integrality
theorem for (2.1).

The obstruction is the owner side. Legal integral route families are
packings in the hypergraph \(\{M(R):R\in\mathscr R\}\), followed by exact
completion. In general this packing system is neither a matroid nor an
integral polymatroid. Intersecting it with the superlevel requirements
implicit in (6.1) does not become a polymatroid intersection.

Equivalently, submodularity describes the value of a fixed selected family;
it does not produce the missing convex-hull inequalities for which
overlapping whole routes may be selected together.

## 7. A genuine common-multidepth determinant-two minor

Let \(R=2\ell\), where \(\ell\) is a power of two, and assume

\[
 H\le\ell/2,
 \qquad
 3(\ell-1)\le m-2.                                         \tag{7.1}
\]

Choose an \((m-1)\)-set \(K\) and distinct coordinates
\(a,b,c\notin K\). Put

\[
 X_a=K\cup\{a\},\qquad
 X_b=K\cup\{b\},\qquad
 X_c=K\cup\{c\}.                                           \tag{7.2}
\]

For each of \(ab,bc,ca\), choose \(\ell-1\) auxiliary members of \(K\)
and \(\ell-1\) auxiliary coordinates outside
\(K\cup\{a,b,c\}\), with the six auxiliary groups disjoint across the
three choices. This is possible by (7.1). For \(ab\), use
\(\{a,b\}\) and its \(\ell-1\) auxiliary pairs as the active pairs of an
orientation cube, and embed one recursive \(F_\ell\)-cycle so that one
edge is

\[
                         X_a\longrightarrow X_b.
\]

Call the resulting necklace \(B_{ab}\), and define \(B_{bc},B_{ca}\)
cyclically. Since \(H\le\ell/2\), every necklace is a genuine common
multidepth route: all its forward lower and backward upper flags through
depth \(H\) are literal geodesic shadows.

### Lemma 7.1 (exact physical intersections)

\[
 B_{ab}\cap B_{bc}=\{X_b\},\qquad
 B_{bc}\cap B_{ca}=\{X_c\},\qquad
 B_{ca}\cap B_{ab}=\{X_a\},                               \tag{7.3}
\]

and the triple intersection is empty.

#### Proof

At \(X_b\), the affine direction space of the \(ab\)-cube is generated by
\(\mathbf e_a+\mathbf e_b\) and its private auxiliary pair toggles. The
direction space of the \(bc\)-cube is generated by
\(\mathbf e_b+\mathbf e_c\) and a disjoint private auxiliary family.
A common nonzero direction could use no private coordinate. It also could
use neither special generator: the first exposes \(a\), and the second
exposes \(c\), with no generator on the other side capable of cancelling
it. Thus the two affine cubes, and hence the two necklaces, meet only at
\(X_b\). The other two identities follow cyclically. The three shared
owners are distinct. \(\square\)

On the three owner rows \(X_a,X_b,X_c\) and the three whole-route columns
\(B_{ab},B_{bc},B_{ca}\), the common multidepth master matrix therefore
contains

\[
 \boxed{
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix}},
 \qquad\det=2.                                             \tag{7.4}
\]

Adding every target row at every depth cannot restore total
unimodularity, because (7.4) remains a submatrix. This also shows exactly
why columnwise nested prefixes do not imply the laminar row-support
condition (5.2).

## 8. The restricted fractional/integral gap and its dual

Let

\[
 \mathcal U=B_{ab}\cup B_{bc}\cup B_{ca}.
\]

By Lemma 7.1,

\[
                         |\mathcal U|=3R-3.                \tag{8.1}
\]

Restrict the augmented master problem to the three necklace columns and
one singleton owner-repair column at every \(X\in\mathcal U\). Retain all
multidepth target rows with their hole variables; set their weights to zero
for this face, and minimize the total singleton owner residual.

### Theorem 8.1 (exact local common-choice gap)

The fractional and integral residual optima are

\[
 E_{\rm frac}={3(R-2)\over2},
 \qquad
 E_{\rm int}=2R-3,                                        \tag{8.2}
\]

so

\[
 \boxed{E_{\rm int}-E_{\rm frac}={R\over2}=\ell,}
 \qquad
 {E_{\rm int}\over E_{\rm frac}}\longrightarrow{4\over3}. \tag{8.3}
\]

If all typed target rows occurring in at least one of the three necklaces
are retained, every target hole has weight one, and every singleton owner
repair has weight \(20H\), then

\[
 \boxed{
 \operatorname {OPT}_{\mathbb Z}
 -\operatorname {OPT}_{\rm LP}\ge8H\ell.}                 \tag{8.4}
\]

#### Proof

Give every necklace weight \(1/2\). Each of the three shared owners has
total route load one. Every necklace has \(R-2\) private owners; give the
singleton column at each private owner weight \(1/2\). This is feasible
and has residual \(3(R-2)/2\).

Let the necklace weights be \(x_1,x_2,x_3\). The three shared-owner rows
give

\[
 x_1+x_2\le1,\qquad
 x_2+x_3\le1,\qquad
 x_3+x_1\le1.                                             \tag{8.5}
\]

After exact singleton completion, the residual objective is

\[
                         (3R-3)-R(x_1+x_2+x_3).            \tag{8.6}
\]

Summing (8.5) gives
\(x_1+x_2+x_3\le3/2\), with equality at
\(x_1=x_2=x_3=1/2\). This proves the fractional value.

Integrally, (8.5) permits at most one necklace. Selecting one is optimal
and leaves

\[
                         |\mathcal U|-R=2R-3
\]

singleton owners. This proves (8.2)--(8.3).

For the weighted assertion, the three necklaces together have at most

\[
                         3R\cdot2H=6RH
\]

distinct typed target rows. The integral objective is at least
\(20H E_{\rm int}\), since target-hole costs are nonnegative. The
fractional half-necklace solution has objective at most
\(20H E_{\rm frac}+6RH\), after its target deficits are put into the hole
variables. Therefore

\[
 \begin{aligned}
 \operatorname {OPT}_{\mathbb Z}
 -\operatorname {OPT}_{\rm LP}
 &\ge20H(E_{\rm int}-E_{\rm frac})-6RH\\
 &=20H(R/2)-6RH\\
 &=4RH=8H\ell,
 \end{aligned}
\]

which proves (8.4). \(\square\)

The reduced fractional maximization and its exact dual are

\[
 \begin{aligned}
 \max\quad&x_1+x_2+x_3,\\
 \text{subject to}\quad&
 x_1+x_2\le1,\quad x_2+x_3\le1,\quad x_3+x_1\le1,\quad
 x_i\ge0,
 \end{aligned}                                             \tag{8.7}
\]

\[
 \begin{aligned}
 \min\quad&y_{12}+y_{23}+y_{31},\\
 \text{subject to}\quad&
 y_{12}+y_{31}\ge1,\\
 &y_{12}+y_{23}\ge1,\\
 &y_{23}+y_{31}\ge1,\qquad y_{ij}\ge0.
 \end{aligned}                                             \tag{8.8}
\]

The primal and dual optima are both \(3/2\), attained by all variables
equal to \(1/2\). The missing integral inequality is the triangle rank cut

\[
                         x_1+x_2+x_3\le1.                  \tag{8.9}
\]

It is a valid local submodular-rank inequality, but it is not generated by
the individual owner rows. Globally, the analogous clique and odd-cycle
cuts of the route-overlap hypergraph are not a laminar family.

Target weights were set to zero only to expose a face of the full joint
polyhedron. Therefore Theorem 8.1 proves that no theorem asserting
integrality of the common multidepth matrix for all integral costs can
follow from prefix laminarity or total unimodularity. It does not assert a
positive gap for the special unit target-hole objective after every route
in the unrestricted catalogue is restored.

## 9. Asymptotic persistence

The local gap is not a fixed small-dimensional accident. Let

\[
                         S=3R-3
\]

be the number of owners in one gadget, and take its full coordinate orbit
under \(S_{2m}\). This is an \(S\)-uniform regular hypergraph on the
\(W=\binom{2m}{m}\) middle owners. Let its owner degree be \(D\). The
number of orbit gadgets is \(WD/S\).

A fixed gadget meets at most \(SD\) orbit gadgets: sum the degree \(D\)
over its \(S\) owners. Hence greedy matching in this orbit hypergraph gives
at least

\[
 {WD/S\over SD}
 ={W\over S^2}                                             \tag{9.1}
\]

pairwise owner-disjoint gadgets.

Restricting the catalogue independently inside those gadgets makes the
master problem a direct sum. By (8.3), its additive gap is at least

\[
 {W\over S^2}\,\ell
 =\Omega\!\left({W\over\ell}\right),                       \tag{9.2}
\]

while the ratio of integral to fractional residual tends to \(4/3\).
If \(\ell=\Theta(H)\), subject to \(2H\le\ell\le(m+1)/3\), the additive
gap is \(\Omega(W/H)\). If the compiler insists on \(H=o(\ell)\), the
proved packed gap is \(\Omega(W/\ell)=o(W/H)\); the ratio obstruction and
the failure of generic integrality nevertheless remain.

Thus the determinant-two obstruction survives in growing dimension and in
many disjoint physical copies. What it does not prove is that the full
mixed-frame catalogue cannot use cross-gadget routes to absorb those
defects at the coefficient-one scale.

## 10. Exact implication boundary

The following statements are proved.

1. (2.1) and (3.1) are the common-choice multidepth primal programmes.
2. (2.2) and (3.2) are their exact duals. Their route inequalities price
   all depths and both signs simultaneously.
3. A true common prefix network, or literal laminarity of the row supports
   over route columns, gives integral rounding.
4. The nesting of shadows inside one route is not that laminarity.
5. Genuine recursive mixed-frame routes contain the determinant-two minor
   (7.4).
6. The restricted augmented problem has exact gap (8.3), with the
   fractional dual (8.8).
7. Disjoint orbit copies amplify the additive gap to
   \(\Omega(W/\ell)\).

The following statements are not proved.

1. A positive gap for the unrestricted catalogue with the specific unit
   target-hole objective.
2. A global coefficient-one obstruction.
3. An \(o(W)\), or where required \(o(W/H)\), rounding theorem after all
   higher-order overlap cuts are included.

The sharp remaining positive route is therefore not ordinary Hall at each
depth. It is a common-cycle rounding theorem showing that the unrestricted
mixed-frame catalogue supplies enough cross-gadget columns to satisfy all
multidepth dual price fields while paying only the permitted additive
integrality loss.
