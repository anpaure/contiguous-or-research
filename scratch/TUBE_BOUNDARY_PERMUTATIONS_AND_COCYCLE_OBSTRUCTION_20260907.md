# Tube boundary permutations and the product-cocycle obstruction

Date: 2026-09-07.  This note analyzes one proposed way to round a rational
fractional q-ary macro cover: permute fine-chain lane labels between macro
cells and use thin buffers to change which lane pairs are selected.  A
structured version is genuinely lower order, but arbitrary cell-dependent
selection is not available.  The remaining compatibility condition is
global and finite.  No claim about unrestricted OR words is made.

Throughout, `q,d` and every rational denominator are fixed while the blow-up
parameter `m` tends to infinity.

## 1. Exact cost of a prescribed shore-label permutation

Consider two consecutive macro cells of an `s`-coordinate tube, where the
macro step changes one coordinate.  A partition of each cell into ascending
path pieces has `N=m^(s-1)` outgoing and incoming face labels.  Identify
both label sets with the product poset

\[
                           X=[m]^{s-1}.
\]

Prescribe a bijection `pi:X->X`: the fixed whole-cell piece leaving with transverse label
`x` is to continue into the piece entering with label `pi(x)`.  The changed
macro coordinate automatically increases by one fine-grid unit.  The join
is ascending precisely when

\[
                              x\le\pi(x)              \tag{1}
\]

coordinatewise in the unchanged coordinates.

Put

\[
                 B(\pi)=|\{x\in X:x\not\le\pi(x)\}|. \tag{2}
\]

**Boundary lemma.**  In the cut-only interface which retains these fixed
whole-cell pieces, and relative to the prescribed actual endpoint
bijection, exactly `B(pi)` extra shore-chain components are necessary and
sufficient.

Indeed, join every comparable prescribed pair and cut every incomparable
one.  Starting from `2N` pieces, the `N-B(pi)` joins leave `N+B(pi)`
components.  No incomparable prescribed pair can lie in one ascending
chain, so no further prescribed join is possible. `square`

The word "exactly" is scoped to this interface.  A larger buffer allowed to
reroute or subdivide pieces internally is a different construction and is
not covered by (2).

In particular `B(pi)=0` forces `pi=id`.  One proof is to sum the coordinate
ranks: `x<=pi(x)` for all `x`, while bijectivity makes the two rank sums
equal, so equality holds termwise.

There are nevertheless nontrivial asymptotically cheap permutations.  For
`0<=z<m`, cyclically shift one transverse coordinate by `z`.  Exactly the
last `z` values wrap downward, so

\[
                         B(\pi_z)=z m^{s-2}.          \tag{3}
\]

If `D|m` and the lane phase is that coordinate modulo `D`, this implements
the uniform phase translation `a->a+z (mod D)`.  A bounded number of
bounded translations through a fixed macro tube therefore creates only
`O_D(m^(s-2))` extra shore chains.

For a product row with shore dimensions `r+s=d`, cutting
`O(m^(r-2))` left lanes increases the full-pair principal charge by at most

\[
 O(m^{r-2})\times O(m^s)=O(m^{d-2}),                 \tag{4}
\]

because the total membership of the right tube is `O(m^s)`.  The symmetric
statement holds on the right.  Hence bounded cyclic phase translations are
indeed negligible beside the `Theta(m^(d-1))` principal term.  This is a
positive routing fact, not merely a dimensional heuristic.

## 2. What an uncut selected-pair mask can do

Fix one macro rectangle `C times D`.  Let `L,R` be its left and right lane
sets at reference cells, and let `S subseteq L times R` be the globally
selected fine-chain pairs.  If no pair-specific cuts are made, transport to
the cell `(u,v) in C times D` gives permutations `sigma_u` of `L` and
`tau_v` of `R`.  Its local selected mask is necessarily

\[
                    \boxed{S_{u,v}=(\sigma_u\times\tau_v)S.}       \tag{5}
\]

The left permutation depends only on `u`, and the right permutation only
on `v`.  Thus cell masks cannot be prescribed independently.  Row and
column degree multisets, for example, are invariant throughout the macro
rectangle.

For the natural cyclic phase mask

\[
 S_A=\{(x,y):\phi_L(x)+\phi_R(y)\in A\},
 \qquad A\subseteq\mathbb Z_D,                       \tag{6}
\]

and phase translations from Section 1, the local offset has the separable
form

\[
                           \theta_{u,v}=\alpha_u+\beta_v.          \tag{7}
\]

Consequently every `2 by 2` macro subrectangle obeys the cocycle identity

\[
 \boxed{\theta_{u_0,v_0}+\theta_{u_1,v_1}
       =\theta_{u_0,v_1}+\theta_{u_1,v_0}\pmod D.}    \tag{8}
\]

Conversely, every offset array satisfying (8) has the form (7), after a
base row and column are fixed, and the bounded translations of Section 1
implement it with `O(m^(d-2))` extra principal charge.  Thus (8) is the
exact finite compatibility law for this translation mechanism.

If only `o(|L|)` left lanes and `o(|R|)` right lanes are cut, (5) and (8)
continue to hold away from

\[
                o(|L|)|R|+|L|o(|R|)=o(|L||R|)        \tag{9}
\]

lane pairs.  Thin buffers cannot conceal a positive-density cocycle
violation.

## 3. A principal-scale four-cell obstruction

The obstruction already occurs in the simplest equal-length tubes.  Let
both macro shore chains have two cells along a single coordinate, with
shore dimensions `r,s>=2`.  Their blow-ups partition into

\[
 |L|=m^{r-1},\qquad |R|=m^{s-1}
\]

parallel lanes, every left and right lane having length `2m`.  Assume `m`
is even, color each lane by one transverse coordinate modulo two, and put

\[
 S_0=\{(x,y):\phi_L(x)+\phi_R(y)=0\pmod2\},
 \qquad S_1=(L\times R)\setminus S_0.                 \tag{10}
\]

Prescribe the four local masks

\[
 S_{00}=S_{01}=S_{10}=S_0,\qquad S_{11}=S_1.         \tag{11}
\]

Their offset matrix is

\[
 \begin{pmatrix}0&0\\0&1\end{pmatrix},
\]

which violates (8).  Hence no uncut left/right lane transport realizes
(11).  This conclusion does not depend on restricting the transports to
literal coordinate shifts: any product permutation taking `S_0` to either
`S_0` or `S_1` must send each of the two left parity classes wholesale to a
left parity class, and likewise on the right.  It therefore induces one
left and one right swap bit, whose cell offsets again have the additive
form (7).  Cutting only `o(m^(r-1))` left lanes and `o(m^(s-1))` right lanes
still fails, because `S_0` and `S_1` differ on every one of the
`m^(d-2)` lane pairs, whereas (9) changes only `o(m^(d-2))` pairs.

The cocycle violation by itself should not be converted into a charge lower
bound: for a general mask, automorphisms or changes supported on a few rows
or columns can make a dense-looking phase discrepancy cheap.  For the exact
mask (11), however, there is a direct fiber argument in the global
shore-partition model.

Suppose the left tube is partitioned into chain components, the right tube
is partitioned into chain components, and the selected objects are products
of one complete left component and one complete right component.  Every
point of one left component then has the same selected right-neighbor set.
A left point in macro cell `u_0` of local parity `a` requires right parity
signature `(a,a)` across `v_0,v_1`, by the first row of (11).  A left point
in `u_1`, of whatever transported parity `a'`, requires signature
`(a',1-a')`.  Equality of the actual right-neighbor sets would force both
`a=a'` and `a=1-a'`, impossible.  Hence no left component can cross the
left macro boundary.  The symmetric argument shows that no right component
can cross the right macro boundary.

In the cut-only line-tube model, both shores must therefore split completely
into their length-`m` cell lanes.  The exact selected set in (11) has volume
`2m^d`.  Products of one left and one right cell lane have volume `m^2`, are
mutually disjoint, and each has principal charge `2m`.  Its exact minimum
charge is consequently

\[
                    \boxed{4m^{d-1}.}                \tag{12}
\]

The prescribed density is one half, whereas one half of the uncut full-row
charge is only `2m^(d-1)`.  Thus this nonseparable four-cell resolution loses
a factor two, at principal order.

This proof is scoped to exact realization of (11) by products of two global
shore partitions retaining the displayed line-cell pieces.  It is not a
lower bound against overlapping products, internal buffer rerouting, or an
unrelated chain-rectangle replacement.  It does prove that the word
"thin" cannot justify independently chosen cell offsets in the proposed
partition-and-repair mechanism.

## 4. A positive degree-controlled refinement compiler

The boundary analysis does give a complete positive theorem once global
point coverage and balanced lane-pair degrees are supplied.

Fix one macro row `C times D` with shore dimensions `r,s>=2`, `r+s=d`.
After a bounded number of cyclic boundary translations, Section 1 gives
shore-chain partitions with

\[
\begin{aligned}
 N_L&=m^{r-1}+O(m^{r-2}),&\quad \sum_{F\in L}|F|&=|C|m^r,\\
 N_R&=m^{s-1}+O(m^{s-2}),&\quad \sum_{G\in R}|G|&=|D|m^s.
\end{aligned}                                                   \tag{13}
\]

Every chain has length `O(m)`, with constants depending only on the fixed
macro template.  Let `mathcal G subseteq L times R` be the selected global
lane-pair graph.  Suppose, for a fixed `p>0`, uniformly over its vertices,

\[
\begin{aligned}
 d_{\mathcal G}(F)&=p m^{s-1}+O(m^{s-2}) &&(F\in L),\\
 d_{\mathcal G}(G)&=p m^{r-1}+O(m^{r-2}) &&(G\in R).
\end{aligned}                                                   \tag{14}
\]

Then the principal charge is

\[
\begin{aligned}
 \sum_{FG\in\mathcal G}(|F|+|G|)
 &=\sum_Fd(F)|F|+\sum_Gd(G)|G|\\
 &=\boxed{p(|C|+|D|)m^{d-1}+O(m^{d-2}).}             \tag{15}
\end{aligned}
\]

This uses only (13)--(14); unequal individual chain lengths cause no
problem.

The number of selected edges is `O(m^(d-2))`.  Moreover (14) gives positive
minimum degree of order `p m^(s-1)` on the left and
`p m^(r-1)` on the right.  Every nonisolated connected component therefore
contains `Omega(p m^(r-1))` left vertices and
`Omega(p m^(s-1))` right vertices.  Comparing with (13), the number of
nonisolated components is `O(1/p)`.

Apply the ordinary two-arc bridge/Euler compiler separately in each
component.  Arc-end overhead is `O(|E(mathcal G)|)=O(m^(d-2))`; every
closing bridge has length `O(m)`, and there are `O(1/p)` of them.  Since
`r,s>=2` implies `d>=4`, the resulting literal word has length

\[
 \boxed{p(|C|+|D|)m^{d-1}+O(m^{d-2}).}               \tag{16}
\]

It realizes every selected product and its full complement.  For a fixed
finite collection of macro rows, if the selected global products cover all
fine points, concatenating (16) over the rows gives a genuine chain-pair
cover and word at the sum of the fractional macro costs, up to lower order.

Condition (14) is essential to this accounting.  Without it the selected
graph can have `Theta(m^(d-2))` small components; closing each with an
`O(m)` bridge can cost `Theta(m^(d-1))`.  For the balanced cyclic phase mask
(6), tag every chain component created by a cut with its inherited
reference-lane phase, and select component pairs by the same fixed mask.
Before cuts every degree is exactly the prescribed phase fraction of the
opposite lane count; the `O(m^(r-2))` and `O(m^(s-2))` new tagged components
perturb degrees only by the error allowed in (14).  With this explicit
inherited-phase rule, bounded separable routing satisfies the charge and
closing hypotheses.  Arbitrary reassignment after a cut need not preserve
degrees.  The remaining issue is global point-cover compatibility.

The indexed quaternary six-axis fractional certificate uses only shore
splits `2+4` and `3+3`, so the hypothesis `r,s>=2` does not discard any of
its positive-weight rows.

## 5. Consequence for fractional macro covers

Let a rational macro column have numerator `n_j` and common denominator
`D`; take `m` divisible by `D` (other values can be reached by bounded
padding).  A phase mask with `|A_j|=n_j` selects exactly the desired fraction of
lane pairs; when both shores have at least two coordinates, balanced phase
classes make its leading principal charge exactly `n_j/D` of the full
column charge.  Bounded separable translations preserve that charge up to
`O(m^(d-2))` by (4).

However, the scalar fractional inequalities

\[
             \sum_{j:v\in R_j}n_j\ge D              \tag{17}
\]

do not provide offsets satisfying (8), nor do they align the different
chain-pair partitions induced by rows with different coordinate splits.
At a macro point where (17) is tight, if every incident column retains its
prescribed local density `n_j/D`, then full coverage forces those selected
parts to partition the fine microcell up to a lower-order set: the sum of
their sizes already equals the size of the cell.  This is a simultaneous
colored-refinement condition, strictly stronger than (17).

Therefore the buffering proposal has the following exact status.

* Bounded **separable** cyclic phase transport is constructive and costs
  only lower order.
* Arbitrary cellwise phase choices are false; they must obey the product
  cocycle (8), up to a vanishing set of lane pairs.
* A general fractional q-ary template can be rounded by this mechanism only
  after supplying a finite compatible phase resolution across all its
  macro rectangles and coordinate splits.  Fractional weights alone do not
  supply that object.

This neither proves nor disproves that the specific quaternary certificate
has such a resolution.  It isolates a finite, checkable compatibility
problem and shows precisely which boundary operations would be
asymptotically free if one were found.
