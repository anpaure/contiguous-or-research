# Fixed-`Q` fractional deficiency, the balanced-surplus obstruction, and multicolour locking

Date: 2026-07-31  
Status: exact LP duality and two general obstruction theorems.  These results
do **not** rule out choosing a favourable common basis, a Boolean-geometric
balanced absorber, or a full-colouring cover-down.  They show that physical
dummy slots, the Delcourt--Postle degree-surplus theorem, and three/four
colour splitting do not close the exact side row automatically.

## 1. The unlabelled fixed-`Q` relaxation

Fix one punctured shore.  Let

\[
 \mathcal D\subseteq {[2n]\choose n},\qquad
 \mathcal V={[2n]\choose {n+2}},\qquad
 \mathcal X={[2n]\choose {n+1}},
\]

where `|D|=|V|=P`.  Each physical owner `x in X` has capacity

\[
 c_x\in\{1,2\};
\]

the seam anchors have capacity one and ordinary owners capacity two.  An
unlabelled atom is a pair `e=(D,V)` with `D subset V`.  Its two physical
owners are the two intermediate sets

\[
 p(e)=\{x_e,y_e\},\qquad x_e\cap y_e=D,\quad x_e\cup y_e=V.       \tag{1.1}
\]

For nonnegative artificial capacity `s_x`, consider fractional outer-perfect
weights `w_e` satisfying

\[
\begin{aligned}
 \sum_{e:D(e)=D}w_e&=1 &&(D\in\mathcal D),\\
 \sum_{e:V(e)=V}w_e&=1 &&(V\in\mathcal V),\\
 \sum_{e:x\in p(e)}w_e&\le c_x+s_x &&(x\in\mathcal X).
                                                               \tag{1.2}
\end{aligned}
\]

Define the **fractional physical deficiency**

\[
 \rho(Q)=\min\left\{\sum_xs_x:(w,s)\text{ satisfies (1.2)}\right\}.
                                                               \tag{1.3}
\]

The unlabelled formulation loses nothing fractionally.  Given `w`, split
the mass of an atom equally among its `c_x c_y` occurrence-labelled slot
lifts.  Every slot at `x` then receives `1/c_x` of the total load at `x`.
Conversely, summing occurrence-labelled weights over slot lifts gives `w`.

## 2. Exact dummy-capacity dual

### Theorem 2.1 (weighted host-cut dual)

The deficiency (1.3) is exactly

\[
\boxed{
\begin{aligned}
 \rho(Q)=\max\quad&
   \sum_{D\in\mathcal D}a_D+\sum_{V\in\mathcal V}b_V
       -\sum_{x\in\mathcal X}c_xz_x\\
 \text{subject to}\quad&
   a_D+b_V\le z_{x_e}+z_{y_e}\qquad(e=(D,V)),\\
 &0\le z_x\le1,qquad a_D,b_V\in\mathbb R.
\end{aligned}}                                                   \tag{2.1}
\]

In particular, the original fixed-`Q` slot hypergraph has a fractional
outer-perfect matching if and only if every dual expression in (2.1) is
nonpositive.  Any augmentation which only supplies artificial physical
capacity has total artificial mass at least `rho(Q)`.

#### Proof

Attach free dual variables `a_D,b_V` to the two equality rows of (1.2),
and a nonnegative variable `z_x` to each owner-capacity row.  The coefficient
of `w_e` in the Lagrangian is

\[
 z_{x_e}+z_{y_e}-a_D-b_V,
\]

so boundedness below gives the first dual constraint.  The coefficient of
`s_x` is `1-z_x`, giving `z_x<=1`; nonnegativity of the capacity multiplier
gives `z_x>=0`.  The remaining constant term is the objective in (2.1).
Finite-dimensional LP strong duality proves the equality.  `square`

### Corollary 2.2 (ordinary host cuts are only the Boolean face)

Suppose `W subseteq V` and every candidate for every `V in W` has both
physical owners in `S subseteq X`.  Taking

\[
 b_V=2\mathbf1_{V\in W},\quad a_D=0,\quad z_x=\mathbf1_{x\in S}
\]

in (2.1) gives

\[
                         \rho(Q)\ge 2|W|-\sum_{x\in S}c_x.       \tag{2.2}
\]

The residual `8>7` fixture at parameter three is this inequality after its
two forced outer rows are contracted.  Hence that authenticated common
basis needs at least one unit of artificial physical capacity even in the
fractional relaxation.  More generally, the full weighted dual (2.1), not
only indicator host cuts, is the precise robust-matchability condition.

### Theorem 2.3 (the authenticated bad basis has deficiency exactly one)

For the literal parameter-three fixture in
`MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md`,

\[
 \mathcal D=\{07,0b,0d,0e,13,23\},
\]

all rank-four owners except `0f` are anchors.  Its fractional physical
deficiency is

\[
                              \boxed{\rho(Q)=1}.                 \tag{2.3}
\]

#### Proof

For the lower-bound certificate, use the dual weights

\[
\begin{array}{c|rrrrrr}
D&07&0b&0d&0e&13&23\\ \hline
a_D&1&0&1&1&1&1
\end{array}
\]

and

\[
\begin{array}{c|rrrrrr}
V&1f&2f&37&3b&3d&3e\\ \hline
b_V&0&0&1&0&1&1.
\end{array}
\]

Set `z_x=1` for

\[
             x\in\{17,27,33,1d,2d,1e,2e\}                    \tag{2.4}
\]

and zero elsewhere.  Direct containment replay gives
`a_D+b_V<=z_x+z_y` for every candidate diamond.  Every owner in (2.4) is
an anchor, so the dual value is

\[
                             5+3-7=1.                            \tag{2.5}
\]

For the matching upper bound, take

\[
\begin{array}{c|c|c}
D&V&\{x,y\}\\ \hline
07&2f&\{0f,27\}\\
0b&1f&\{0f,1b\}\\
0d&3d&\{1d,2d\}\\
0e&3e&\{1e,2e\}\\
13&37&\{17,33\}\\
23&3b&\{2b,33\}.
\end{array}                                                   \tag{2.6}
\]

It is outer-perfect.  Every owner respects its original capacity except
`33`, whose load is two instead of its anchor capacity one.  One artificial
unit at `33` therefore makes (2.6) feasible.  Weak duality and (2.5)--(2.6)
give equality in (2.3).  `square`

The certificate is global: unlike the contracted `8>7` explanation, it
does not first assume the two forced rows.  It proves that no fractional
reweighting can hide the missing unit elsewhere.

Thus a theorem asserting exact completion for **every** fixed common basis
cannot follow from dummy regularization: some fixed bases are fractionally
infeasible before graphic acyclicity is imposed.  The bank-flexible target
must choose `Q` so that `rho(Q)=0`, and integral/graphic rounding is an
additional condition even then.

## 3. Bank flexibility is an exact modular-cut problem

The dual becomes especially useful before the common basis is fixed.  Let
`F` be an oriented Catalan path forest.  On the upper side write

\[
 \tau:E(F)\longrightarrow T\subseteq {[2n]\choose n}
\]

for its injective tail map, and

\[
 \upsilon:E(F)\longrightarrow {[2n]\choose {n+1}}
\]

for its upper-colour bijection.  Let `q_e` be the indicator that the child
edge `e` belongs to the deletion bank `Q`.  On the full rank-`n` lower
catalogue, the required fractional row loads and owner capacities are

\[
 r_D(q)=
 \begin{cases}
  1-q_e,&D=\tau(e),\\
  1,&D\notin T,
 \end{cases}
 \qquad
 c_x(q)=2-q_{\upsilon^{-1}(x)}.                       \tag{3.1}
\]

For an integral `q`, the zero rows are precisely the punctured lower
colours and the capacity-one owners precisely the seam anchors.

### Theorem 3.1 (physical common-basis cut system)

For a fixed possibly fractional vector `q`, the upper physical marginal has
a fractional outer-perfect realization if and only if, for every
`a_D,b_V in R` and `z_x>=0` satisfying

\[
                    a_D+b_V\le z_x+z_y                 \tag{3.2}
\]

on every Boolean diamond `(D,V,{x,y})`,

\[
\boxed{
 \sum_Da_D+\sum_Vb_V-2\sum_xz_x
   +\sum_{e\in E(F)}q_e\bigl(z_{\upsilon(e)}-a_{\tau(e)}\bigr)
 \le0.}                                                \tag{3.3}
\]

The lower shore has the complement-dual formula.  Consequently selecting
a bank-flexible fractionally physical common basis is exactly the problem
of finding an incidence vector `q` in the strict common-base family which
satisfies the two families of modular inequalities (3.3).

#### Proof

Use variables `w_(D,V)>=0`, impose lower row sum `r_D(q)`, upper row sum one,
and owner load at most `c_x(q)`.  Farkas duality says feasibility is
equivalent to

\[
       \sum_Dr_D(q)a_D+\sum_Vb_V\le\sum_xc_x(q)z_x    \tag{3.4}
\]

for every dual-feasible `(a,b,z)` in (3.2).  Substitute (3.1) into (3.4)
and collect the coefficient of each `q_e`; this is exactly (3.3).
`square`

### Corollary 3.2 (fractional joint gate has a separation oracle)

Intersect the strict common-base polytope with the upper and lower systems
(3.3).  In the explicit-catalogue model this polytope has a polynomial-time
separation oracle: matroid intersection separates the common-base rows,
and an infeasible physical marginal returns a violated Farkas dual row by
one LP solve.

This is only a fractional algorithm.  The intersection need not have an
integral vertex: the determinant-three/odd-circuit obstructions in the
ordered four-transversal model show why raw polyhedral integrality cannot
be inferred.  Nevertheless (3.3) is the exact bank-flexible target which
dummy regularization had obscured.  It permits choosing `Q` for physical
feasibility rather than demanding the false every-`Q` statement.

## 4. Why the Delcourt--Postle exact degree-surplus theorem cannot be used directly

### Theorem 4.1 (balanced outer-shore surplus obstruction)

Let `G` be any hypergraph with two vertex classes `A,B` of the same finite
size, where every edge contains exactly one member of `A` and exactly one
member of `B` (and may contain further resources).  Then

\[
 \min_{a\in A}d(a)\le {|E(G)|\over|A|}
   ={|E(G)|\over|B|}\le\max_{b\in B}d(b).             \tag{3.1}
\]

Consequently there are no `D>0, epsilon>0` for which every `A`-degree is at
least `(1+epsilon)D` while every `B`-degree is at most `D`.

#### Proof

Each edge contributes one to each of the two degree sums, so both sums equal
`|E(G)|`.  Taking the minimum and maximum relative to their common average
gives (3.1).  `square`

For the capacity-slot host, the two outer classes both have order `P`.
Therefore the bipartite `A`-perfect theorem of Delcourt--Postle cannot be
applied with either real outer shore as `A` while retaining the other shore
as a `B` resource: its strict degree gap is arithmetically impossible.
Splitting or adding physical slots does not change (3.1).  Adding dummy
outer edges can manufacture a degree gap, but an `A`-perfect matching may
then use those dummy edges and need not cover the real opposite shore.
Hence such an augmentation does not imply the desired outer-perfect
matching.

This is independent of the successful use of Corollary 1.17 for the
`P-o(P)` colouring theorem: that corollary needs only maximum degree and
does not claim exact outer coverage.

## 5. Three and four colours can remain globally locked

The two-colour exchange obstruction from the full colouring is not the end
of the generic obstruction.  Even three or four colour classes need not
contain a nontrivial recolouring.

Let `p>=5` be prime, choose four distinct
`a_1,...,a_4 in F_p`, and use four vertex parts

\[
 V_i=\{i\}\times\mathbb F_p.
\]

As in the existing two-colour obstruction, put

\[
 e_{x,c}=\{(i,x+a_ic):1\le i\le4\},\qquad x,c\in\mathbb F_p.   \tag{4.1}
\]

For `2<=t<=4`, retain only `c in C_t={0,1,...,t-1}`.  The resulting
four-partite four-graph is `t`-regular and linear, and the classes

\[
 M_c=\{e_{x,c}:x\in\mathbb F_p\}\qquad(c\in C_t)                \tag{4.2}
\]

are `t` perfect matchings.

### Theorem 5.1 (Fourier locking through four colours)

Every proper `t`-edge-colouring of the retained host with `t` colours is
the colouring (4.2) followed by one global permutation of the colours.
Equivalently, its factorization into `t` perfect matchings is unique up to
permuting the factors.  In particular, no nonempty proper three-colour or
four-colour exchange exists.

#### Proof

At every host vertex the `t` incident atoms must receive all `t` colours.
Fix one output colour and let

\[
 f_c(x)=\mathbf1\{e_{x,c}\text{ receives that output colour}\}.
\]

For every part `i` and every `y in F_p`, properness gives

\[
                 \sum_{c=0}^{t-1}f_c(y-a_ic)=1.                 \tag{4.3}
\]

Let `omega` be a primitive `p`th root of unity.  At every nonzero Fourier
frequency `s`, (4.3) gives

\[
       \sum_{c=0}^{t-1}(\omega^{-sa_i})^c\widehat f_c(s)=0
       \qquad(1\le i\le4).                                     \tag{4.4}
\]

The four numbers `omega^{-sa_i}` are distinct.  Since `t<=4`, a `t`-row
submatrix of (4.4) is a square Vandermonde matrix and is nonsingular.
Thus every `widehat f_c(s)=0` for `s ne0`, so each `f_c` is constant in
`x`.  Being zero-one valued, it is identically zero or identically one.
Equation (4.3) says exactly one input class is assigned to the fixed output
colour.  Repeating this for all output colours gives one global
permutation.  `square`

The host in Theorem 4.1 has codegree at most one, exact regularity, and
perfect colour classes.  Therefore **no theorem using only properness,
small codegree, regularity, and three/four retained colours can supply a
local four-core splitter**.  A positive multicolour theorem must use the
specific Boolean-diamond geometry or a number of colours growing beyond
this locked range.

The threshold four is sharp for this affine family.

### Proposition 5.2 (the first alternative factorization uses five colours)

Take `p=5` and `(a_1,a_2,a_3,a_4)=(0,1,2,3)`.  Besides the vertical
factorization `(M_c:c in F_5)`, the same 25 atoms have the factorization

\[
                 N_b=\{e_{x,c}:c=x+b\}\qquad(b\in\mathbb F_5).  \tag{4.5}
\]

Every `N_b` is a perfect matching, and the five `N_b` partition the host.

#### Proof

At a vertex in part `i`, an atom of `N_b` has coordinate

\[
       y=x+a_i(x+b)=(1+a_i)x+a_ib.                            \tag{4.6}
\]

All four coefficients `1+a_i` are nonzero modulo five, so for fixed `i,y,b`
there is exactly one `x`.  Thus `N_b` is perfect.  The value `b=c-x` is
unique for every atom, proving the partition.  `square`

This is a global 25-atom refactorization, not a bounded ear.  It shows that
five colours are the first point at which the abstract four-partite Fourier
lock can open, while giving no serialization theorem.  For the Catalan
host it motivates a five-or-more-colour core only if its exchanges are
coupled to the Boolean physical/graphic geometry.

## 6. Consequence for the exact recursion

The fixed-`Q` and bank-flexible tasks are now cleanly separated.

1. For fixed `Q`, `rho(Q)` in (2.1) is the exact fractional physical
   obstruction.  `rho(Q)>0` cannot be repaired by merely relabelling or
   regularizing existing slots.
2. Along one recursive chain, the first bank-flexible target is to choose a
   synchronized common basis `Q` with `rho(Q)=0`.  Neither the automatic
   common-basis theorem nor one-point uniform marginals currently imply
   this.
3. Even `rho(Q)=0` leaves a genuinely nonintegral four-resource plus graphic
   rounding problem; the known determinant/odd-circuit examples apply.
4. The exact Delcourt--Postle `A`-perfect reserve theorem is blocked by the
   equal outer-shore degree identity (3.1).
5. Two-, three-, and four-colour local splitting is not guaranteed by the
   full conflict-free colouring.  The first plausible colouring route is a
   **global, many-colour, Boolean-geometric cover-down**, or alternatively a
   balanced edge-aligned absorber constructed together with `Q`.

Thus refined balanced absorption is the more sharply targeted route.  The
full colouring remains useful as its distributed reservoir, but not as an
automatic bounded-colour exchange decomposition.

The exact parameter-three deficiency and the Fourier-locking algebra are
replayed without optimization software by

```text
scratch/audit_catalan_fixed_q_dummy_dual_and_multicolour_locking_20260731.py
```
