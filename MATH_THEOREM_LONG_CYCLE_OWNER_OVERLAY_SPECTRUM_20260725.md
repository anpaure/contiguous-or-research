# Long-cycle owner overlays: principal angles, conductance, and the exact bridge tension

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let `F` be an exact middle wreath factor on `n=2m+1` coordinates, with

\[
 W=\binom nm,\qquad B={W\over n}
\]

rows.  For a coordinate permutation `sigma`, the normalized owner-overlap
matrix is a compression of the coordinate permutation to the row-packet
subspace.  Its singular values are exactly the cosines of the principal
angles between that subspace and its `sigma`-image.

For the diagonal near-trade `A -> sigma A`, the middle boundary is governed
not merely by those singular values but by the symmetric diagonal
compression

\[
                  S_\sigma={K_\sigma+K_\sigma^{\mathsf T}\over2}.
\]

Vanishing balanced diagonal conductance is equivalent, via ordinary
Cheeger inequalities, to a nonconstant eigenvalue of `S_sigma` tending to
one.  In particular it forces a principal angle tending to zero.

The conjugacy class of coordinate `n`-cycles has the opposite average
behavior.  Exact row-packet one-design symmetry gives

\[
 \mathbb E_{\sigma\text{ an }n\text{-cycle}}K_\sigma={J_B\over B}.
\]

Consequently every fixed balanced row cut has average middle boundary
`Theta(W)`.  Long-cycle averaging supplies shadow opportunity, but it does
not supply the exceptional near-invariant packet cut needed to make that
opportunity cheap.

There is a guaranteed algebraic fragmentation: rotating the coordinates
along any one wreath row is an `n`-cycle and isolates that row in the owner
overlay.  The associated switch is, however, trivial because the row is
itself rotation-invariant.  No guaranteed nontrivial long-cycle component
trade follows.

The exact surviving one-shot gate is therefore the simultaneous existence
of:

1. almost-complete hole-to-covered opportunity;
2. a balanced low-conductance diagonal cut capturing that opportunity;
3. negligible shadow damage on the same cut.

The class-average opportunity theorem and the spectral statements below do
not prove this correlation.

The shadow condition is made exact below by two augmented row graphs.
The positive graph consists of cliques on collision-rich old-only target
supports; the negative graph consists of the owner overlap plus normalized
common-support commodities.  A profitable two-shore near-trade exists
exactly when some row vector has larger `L^1` variation in the positive
graph than in the negative graph.  An explicit regular abstract packet
countermodel shows that owner spectrum, target load sizes, and unsigned
support crossing do not determine this sign.  The minimal missing input is
therefore a signed shadow-assortativity theorem on the same `(sigma,A)`.

## 1. The packet incidence matrix

Let `Omega=binom([n],m)`.  Define the `W x B` incidence matrix

\[
 (A_F)_{X,C}=\mathbf1_{\{X\in{\cal W}_m(C)\}},
 \qquad X\in\Omega,\ C\in F.
\tag{1.1}
\]

Exact ownership says that the column supports partition `Omega`, each with
size `n`.  Therefore

\[
 A_F^{\mathsf T}A_F=nI_B.
\tag{1.2}
\]

Put

\[
 Q_F={A_F\over\sqrt n},\qquad
 V_F=\operatorname {im}Q_F,\qquad
 \Pi_F=Q_FQ_F^{\mathsf T}.
\tag{1.3}
\]

Thus `Q_F` is an isometry from row-coordinate space `R^B` onto the
row-packet subspace `V_F`.

Let `P_sigma` be the orthogonal permutation matrix on middle sets.  Define

\[
 M_\sigma=A_F^{\mathsf T}P_\sigma A_F,
 \qquad
 K_\sigma={M_\sigma\over n}
 =Q_F^{\mathsf T}P_\sigma Q_F.
\tag{1.4}
\]

Its entry is

\[
 M_\sigma(C,D)
 =|{\cal W}_m(C)\cap\sigma{\cal W}_m(D)|.
\tag{1.5}
\]

Every row and column sum of `M_sigma` is `n`, so `K_sigma` is doubly
stochastic.

## 2. Exact principal-angle theorem

### Theorem 2.1

The singular values

\[
 1=s_1(K_\sigma)\ge s_2(K_\sigma)\ge\cdots\ge0
\]

are exactly

\[
                         s_i(K_\sigma)=\cos\theta_i,
\tag{2.1}
\]

where `theta_i` are the principal angles between `V_F` and
`P_sigma V_F`.

Moreover, the multiplicity of singular value one is

\[
 \boxed{
 \dim(V_F\cap P_\sigma V_F)
 =\#\{\text{connected components of the }F/\sigma F
      \text{ owner overlay}\}.}
\tag{2.2}
\]

### Proof

The two matrices `Q_F` and `P_sigma Q_F` are orthonormal frames for the two
subspaces.  Their cross-Gram matrix is exactly (1.4), and the standard
principal-angle theorem gives (2.1).

A function belongs to the intersection precisely when it is constant on
every row packet of `F` and on every row packet of `sigma F`.  Such a
function is constant on each connected component of the bipartite common
refinement graph, and its component constants are arbitrary.  This proves
(2.2). \(\square\)

Equivalently,

\[
 K_\sigma K_\sigma^{\mathsf T}
 =Q_F^{\mathsf T}P_\sigma\Pi_FP_\sigma^{-1}Q_F,
\tag{2.3}
\]

so its eigenvalues are the squared principal cosines.

## 3. Exact diagonal-cut Rayleigh quotient

Let `A subseteq F`, let `x=1_A in R^B`, and put `a=|A|`.  The normalized
packet vector is

\[
                         Q_Fx={\mathbf1_{U(A)}\over\sqrt n}.
\]

The diagonal middle boundary from the near-trade theorem is

\[
\begin{aligned}
 \partial_\sigma(A)
 &=|U(A)\triangle\sigma U(A)|\\
 &=n\|Q_Fx-P_\sigma Q_Fx\|_2^2\\
 &=2n\bigl(a-x^{\mathsf T}K_\sigma x\bigr).
\end{aligned}
\tag{3.1}
\]

Put `p=a/B`, `f=x-p1`, and

\[
                         S_\sigma={K_\sigma+K_\sigma^{\mathsf T}\over2}.
\tag{3.2}
\]

Since `K_sigma` is doubly stochastic,

\[
 \|f\|_2^2=a(1-a/B)
\]

and (3.1) becomes

\[
 \boxed{
 \partial_\sigma(A)
 =2n\left(\|f\|_2^2-f^{\mathsf T}S_\sigma f\right).}
\tag{3.3}
\]

Thus a balanced cut with `partial=o(W)` supplies a centered vector with

\[
 {f^{\mathsf T}S_\sigma f\over\|f\|_2^2}=1-o(1).
\tag{3.4}
\]

In particular the largest singular value of `K_sigma` on `1^perp`
satisfies

\[
 \boxed{
 s_*(K_\sigma)
 \ge1-{\partial_\sigma(A)\over2n\|f\|_2^2}.}
\tag{3.5}
\]

Hence every useful balanced near-trade forces a nonconstant principal angle
`o(1)`.

The converse requires the symmetric diagonal compression.  A large
singular value alone may compare `Q_Fx` with `P_sigma Q_Fy` for different
coefficient vectors `x,y`; the near-trade demands the same Boolean vector
on both shores.

## 4. Cheeger equivalence for diagonal near-trades

Regard `S_sigma` as a reversible Markov matrix with uniform stationary
measure.  For `0<|A|<=B/2`, its ordinary conductance is

\[
 \phi_\sigma(A)
 ={\sum_{C\in A,D\notin A}S_\sigma(C,D)\over|A|}
 ={\partial_\sigma(A)\over2n|A|}.
\tag{4.1}
\]

Let `phi_*` be the minimum over nontrivial cuts and let `lambda_2` be the
second-largest eigenvalue of `S_sigma`.  The standard Cheeger inequalities
give

\[
 \boxed{
 {\phi_*^2\over2}\le1-\lambda_2\le2\phi_*.}
\tag{4.2}
\]

Consequently

\[
 \boxed{
 \exists\text{ a balanced cut with }\partial=o(W)
 \quad\Longrightarrow\quad
 \lambda_2(S_\sigma)=1-o(1)
 \quad\Longrightarrow\quad
 s_*(K_\sigma)=1-o(1).}
\tag{4.3}
\]

Conversely `lambda_2=1-o(1)` produces a cut of vanishing conductance by a
Cheeger sweep, though its volume need not automatically be a fixed positive
fraction of `B`.  A coefficient-one one-shot repair additionally needs the
balance forced by the first-shadow row-Lipschitz argument.

This is the precise spectral form of the long-cycle owner-fragmentation
gate.

## 5. The class average of long-cycle overlap matrices

Every wreath row is a one-design on the middle layer: among its `n` middle
sets, every coordinate occurs exactly `m` times.  Therefore

\[
 V_F=U_0\oplus V_F^0,
 \qquad
 V_F^0\subseteq U_2\oplus U_3\oplus\cdots,
\tag{5.1}
\]

where `U_j` are the Johnson harmonics.  Indeed a centered linear
combination of row packets has zero total mass and zero point margins, so it
has no `U_0` or `U_1` component.

The coordinate-`n`-cycle class average acts as one on `U_0`, as
`-1/(n-1)` on `U_1`, and as zero on every `U_j`, `j>=2`.  Compressing this
identity with `Q_F` and using (5.1) gives:

### Theorem 5.1 (exact mean overlap)

\[
 \boxed{
 \mathbb E_{\sigma\text{ an }n\text{-cycle}}K_\sigma
 ={J_B\over B}.}
\tag{5.2}

For every fixed row cut `A`, equations (3.1) and (5.2) yield

\[
 \boxed{
 \mathbb E_\sigma\partial_\sigma(A)
 =2n|A|\left(1-{|A|\over B}\right).}
\tag{5.3}

For `|A|=pB`, `p in (0,1)` fixed, this is

\[
                         2p(1-p)W.
\tag{5.4}
\]

Thus a fixed positive-density cut has coefficient-scale average middle
cost over long cycles.  A low-cost long-cycle cut must be selected jointly
with the cycle and must have exceptional positive packet correlation

\[
 f^{\mathsf T}K_\sigma f=(1-o(1))\|f\|_2^2.
\tag{5.5}
\]

The class-average shadow opportunity theorem and (5.2) point in opposite
directions: averaging supplies many moved holes, while averaging supplies
no nonconstant packet correlation at all.

## 6. Exact opportunity-versus-conductance necessity

Let `Z_1` be the first-shadow hole family of `F`, `h=|Z_1|`, and define the
oriented global opportunity

\[
\mathcal O_\sigma
 =\#\{S\in Z_1:\mu_{F,1}(\sigma^{-1}S)>0\}.
\tag{6.1}
\]

This is the orientation compatible with replacing `A` by `sigma A`.
The class of `n`-cycles is closed under inversion, so the long-cycle
opportunity theorem applies with this convention unchanged.

For a row cut `A`, let `R_1(A),D_1(A)` be the exact repaired and damaged
counts in the near-trade ledger.  Then

\[
 R_1(A)\le\mathcal O_\sigma,
 \qquad
 R_1(A)\le n|A|,
\tag{6.2}
\]

and

\[
 H_1((F\setminus A)\sqcup\sigma A)
 =h+D_1(A)-R_1(A).
\tag{6.3}
\]

Therefore a one-shot near-factor with `H_1=o(W)` necessarily satisfies

\[
 \boxed{
 \mathcal O_\sigma\ge h-o(W),\qquad
 R_1(A)-D_1(A)=h-o(W).}
\tag{6.4}

If its total OR cost is coefficient one, it also necessarily satisfies

\[
 \boxed{
 \partial_\sigma(A)=o(W),}
\tag{6.5}

and hence the near-one spectral condition (3.4).

For a linear starting defect `h=Theta(W)`, the universal long-cycle
guarantee

\[
 \mathcal O_\sigma\ge {2h\over m}
\tag{6.6}
\]

is consequently a factor `Theta(m)` below the one-shot requirement (6.4).
The sharper class-average value

\[
 {h(N_1-h)\over N_1}
 +{\|P_1\mathbf1_{Z_1}\|_2^2\over n-1}
\tag{6.7}
\]

can be linear when covered and missing targets both have positive density,
but it still does not guarantee the near-total opportunity in (6.4), nor
correlate the opportunity with the exceptional packet cut (5.5).

Combining the first-band length ledger with (3.1), the exact profit
functional is

\[
 \boxed{
 \operatorname {Gain}_1(A,\sigma)
 =2(R_1(A)-D_1(A))-\partial_\sigma(A).}
\tag{6.8}
\]

This is the desired usable inequality: shadow opportunity must dominate
the diagonal owner boundary on the **same** Boolean packet cut.

### 6.1 A two-shore opportunity--conductance inequality

The cut itself does not need to be correlated with the location of the
opportunity.  Consider both orientations `A` and `A^c=F\A`.  Every global
opportunity target has at least one new-side owner row, which lies on at
least one of the two shores.  Therefore

\[
 \boxed{R_1(A)+R_1(A^c)\ge\mathcal O_\sigma.}
\tag{6.9}
\]

Define the separated-covered leakage

\[
 \mathcal D_{\rm sep}(A)=D_1(A)+D_1(A^c).
\tag{6.10}
\]

The two damage families are disjoint.  More explicitly,
`D_sep(A)` counts covered targets whose complete old occurrence support is
contained in one shore while their complete `sigma^{-1}`-occurrence support
is contained in the opposite shore.

The two orientations have the same middle boundary.  Averaging their exact
profit ledgers gives

\[
\boxed{
 \max\{\operatorname {Gain}_1(A,\sigma),
        \operatorname {Gain}_1(A^c,\sigma)\}
 \ge
 \mathcal O_\sigma-\mathcal D_{\rm sep}(A)
 -\partial_\sigma(A).}
\tag{6.11}
\]

Consequently a long cycle with

\[
 \mathcal O_\sigma=\Omega(W),\qquad
 \partial_\sigma(A)=o(W),\qquad
 \mathcal D_{\rm sep}(A)=o(W)
\tag{6.12}
\]

has one shore orientation giving an `Omega(W)` improvement in the literal
first-band ledger.  This is a genuine opportunity--conductance coupling:
opportunity automatically chooses a shore, and the only additional shadow
obstruction is the exact separated-covered leakage (6.10).

Low conductance does not itself bound `D_sep`; this is the remaining
packet-shadow correlation theorem.

### 6.2 Exact weighted multidepth form

For every depth `q>=1`, define

\[
 \mathcal O_{\sigma,q}
 =\#\{S:\mu_q(S)=0,\ \mu_q(\sigma^{-1}S)>0\},
\tag{6.13}
\]

and let

\[
 \mathcal D_{{\rm sep},q}(A)=D_q(A)+D_q(A^c).
\tag{6.14}
\]

As at depth one,

\[
 R_q(A)+R_q(A^c)\ge\mathcal O_{\sigma,q}.
\tag{6.15}
\]

Let `w_q>=0` be arbitrary weights.  Define the weighted designated gain of
one orientation by

\[
 \operatorname {Gain}_{w,H}(A,\sigma)
 =2\sum_{q=1}^Hw_q(R_q(A)-D_q(A))
  -\partial_\sigma(A).
\tag{6.16}
\]

The middle boundary occurs only once, regardless of the number of shadow
ranks.  Adding the two shore orientations and dividing by two proves:

### Theorem 6.2 (weighted two-shore near-trade lemma)

\[
\boxed{
 \max_{E\in\{A,A^c\}}
 \operatorname {Gain}_{w,H}(E,\sigma)
 \ge
 \sum_{q=1}^Hw_q
   \bigl(\mathcal O_{\sigma,q}
         -\mathcal D_{{\rm sep},q}(A)\bigr)
 -\partial_\sigma(A).}
\tag{6.17}
\]

For the literal OR ledger take `w_q=1`.  Therefore the exact one-shot
sufficient inequality is

\[
 \boxed{
 \sum_{q=1}^H
 \bigl(\mathcal O_{\sigma,q}
       -\mathcal D_{{\rm sep},q}(A)\bigr)
 >\partial_\sigma(A).}
\tag{6.18}
\]

It guarantees that one of the two orientations strictly improves the
complete designated central-band length.  An `Omega(W)` margin in (6.18)
gives an `Omega(W)` improvement.  Weighted overload or entropy ledgers may
use other `w_q`, but the physical middle debit remains the single unweighted
term in (6.17).

## 6A. Why a spectral sweep does not control separated leakage

The obstruction can be written exactly.  For a target `S` at depth `q`,
let

\[
 \mathsf O_q(S)=\{C\in F:C\text{ contains an occurrence of }S\},
\]

\[
 \mathsf N_{\sigma,q}(S)
 =\{C\in F:C\text{ contains an occurrence of }\sigma^{-1}S\}.
\tag{6A.1}
\]

Let `v in R^B` and take sweep cuts `A_t={C:v_C<=t}`.  Suppose first that
both support sets in (6A.1) are nonempty, and choose `t` from a distribution
with continuous cumulative distribution function `G`.  The target belongs
to the separated leakage of the cut exactly when the threshold lies between
the two support intervals.  Its probability is

\[
\boxed{
 \begin{aligned}
 p_{q,S}(v)={}&
 \bigl[G(\min\mathsf N_{\sigma,q}(S))
       -G(\max\mathsf O_q(S))\bigr]_+\\
 &+\bigl[G(\min\mathsf O_q(S))
       -G(\max\mathsf N_{\sigma,q}(S))\bigr]_+,
 \end{aligned}}
\tag{6A.2}
\]

where `G(min X)` abbreviates `G(min_{C in X}v_C)`, and similarly for the
other extrema.  Hence

\[
 \mathbb E_t\mathcal D_{{\rm sep},q}(A_t)
 =\sum_{S:\mu_q(S)>0}p_{q,S}(v)
\tag{6A.3}
\]

with the evident one-sided terms when the new support is empty.

By contrast, the sweep's owner boundary is controlled by the Dirichlet
form of `S_sigma`, or in coarea form by sums of
`M_sigma(C,D)|v_C-v_D|`.  Formula (6A.2) involves gaps between **shadow
support extrema**, and those row pairs need not be owner-overlay neighbors.
There is therefore no formal implication from small owner Dirichlet energy
to small (6A.3).

This failure occurs inside the actual wreath system, not merely in an
abstract countermodel.  In the canonical `(2 3)` overlay, take one proved
private size-two component `K_V` and its component-indicator eigenvector.
Its owner boundary and Dirichlet energy are exactly zero.  Switching that
component nevertheless creates one first-shadow hole and repairs none; the
two shore orientations together have positive separated leakage.  Repeating
over the disjoint private family gives additive leakage while every selected
union remains a zero-boundary component cut.

Thus no universal inequality of the form

\[
 \sum_{q<=H}w_q\mathcal D_{{\rm sep},q}(A)
 \le F(\partial_\sigma(A)),\qquad F(0)=0,
\tag{6A.4}
\]

can hold, even for exact MSW owner overlays.

The required positive theorem must augment the owner graph by shadow-support
links.  One precise surviving target is a coarea comparison

\[
 \sum_{q<=H}w_q\sum_S p_{q,S}(v)
 \le o(W)+Lambda
 \sum_{C,D}M_\sigma(C,D)|v_C-v_D|,
\tag{6A.5}
\]

for a specially chosen long cycle and slow vector, with a coefficient
`Lambda` small enough for (6.17).  The private-component example proves that
(6A.5) cannot be derived from owner spectrum alone; it needs genuine
long-cycle shadow-support geometry.

## 6B. The augmented packet graph and an exact signed coarea criterion

The preceding obstruction can be repaired at the level of definitions.
The repair does not prove that a profitable cut exists, but it turns that
question into an exact comparison of two explicit weighted graphs on the
row packets.

Fix `sigma`, a depth `q`, and write

\[
 k_q(S)=\mu_q(S),\qquad
 p_{q,S}(C)={\mathbf 1_{\{C\in\mathsf O_q(S)\}}\over k_q(S)}
 \quad(k_q(S)>0).
\tag{6B.1}
\]

Thus `p_(q,S)` is the uniform probability measure on the old owner support
of `S`.  For a row cut `A`, put

\[
 u_{q,S}(A)=p_{q,S}(A)
 ={|A\cap\mathsf O_q(S)|\over k_q(S)}.
\tag{6B.2}
\]

There are three relevant transition types under the target permutation
`S -> sigma S`:

\[
 \begin{aligned}
 \mathcal E^+_{\sigma,q}
 &=\{S:k_q(S)=0,\ k_q(\sigma^{-1}S)>0\},\\
 \mathcal E^-_{\sigma,q}
 &=\{S:k_q(S)>0,\ k_q(\sigma^{-1}S)=0\},\\
 \mathcal C_{\sigma,q}
 &=\{S:k_q(S)>0,\ k_q(\sigma^{-1}S)>0\}.
 \end{aligned}
\tag{6B.3}
\]

On every cycle of the target permutation, the numbers of `0 -> positive`
and `positive -> 0` transitions agree.  Consequently

\[
 |\mathcal E^+_{\sigma,q}|
 =|\mathcal E^-_{\sigma,q}|
 =\mathcal O_{\sigma,q}.
\tag{6B.4}
\]

For `S in C_(sigma,q)`, set

\[
 c_{q,S}(A)=w_q\bigl[
 u_{q,S}(A)(1-u_{q,\sigma^{-1}S}(A))
 +(1-u_{q,S}(A))u_{q,\sigma^{-1}S}(A)
 \bigr].
\tag{6B.5}
\]

This is the cut weight of the normalized complete bipartite commodity from
`O_q(S)` to `O_q(sigma^{-1}S)`: for every ordered pair in the two supports
give weight

\[
 {w_q\over k_q(S)k_q(\sigma^{-1}S)},
\tag{6B.6}
\]

and combine the two directions between each unordered row pair.  Loops do
not enter a cut.  If the two complete supports lie on opposite shores,
then `c_(q,S)(A)=w_q`; otherwise it is merely nonnegative.  Hence

\[
 w_q\mathcal D^{\rm common}_{{\rm sep},q}(A)
 \le\sum_{S\in\mathcal C_{\sigma,q}}c_{q,S}(A).
\tag{6B.7}
\]

For `S in E^-_(sigma,q)` with `k=k_q(S)`, put a clique on
`O_q(S)`, assigning every unordered row pair weight `4w_q/k^2`.  Its cut
weight is

\[
 r_{q,S}(A)=4w_q u_{q,S}(A)(1-u_{q,S}(A)).
\tag{6B.8}
\]

It is zero when the support is confined to one shore and is at most `w_q`
when the support is split.  Therefore

\[
 r_{q,S}(A)
 \le w_q\mathbf 1_{\{\mathsf O_q(S)\text{ meets both shores}\}}.
\tag{6B.9}
\]

The reason for using the old-only family `E^-`, rather than the hole family
`E^+`, is the following exact cancellation.  An old-only target contributes
one to `D_q(A)+D_q(A^c)` precisely when its old support is confined to one
shore.  A common target contributes precisely when its old and new supports
are confined to opposite shores.  Using (6B.4),

\[
\boxed{
 \mathcal O_{\sigma,q}-\mathcal D_{{\rm sep},q}(A)
 =\sum_{S\in\mathcal E^-_{\sigma,q}}
   \mathbf 1_{\{\mathsf O_q(S)\text{ split}\}}
 -\mathcal D^{\rm common}_{{\rm sep},q}(A).}
\tag{6B.10}
\]

Now form two undirected weighted multigraphs on the row set `F`.

* `G^-_(sigma,w,H)` contains the owner-overlap graph, with edge weight
  `M_sigma(C,D)+M_sigma(D,C)` on `{C,D}`, and all common commodities
  (6B.6) for `q<=H`.
* `G^+_(sigma,w,H)` contains all exclusive-support cliques (6B.8) for
  `q<=H`.

Write `Cut_-(A)` and `Cut_+(A)` for their cut weights.  The owner part has
cut exactly `partial_sigma(A)`.  Equations (6B.7)--(6B.10) give

\[
 \sum_{q=1}^Hw_q
 \bigl(\mathcal O_{\sigma,q}
       -\mathcal D_{{\rm sep},q}(A)\bigr)
 -\partial_\sigma(A)
 \ge \operatorname {Cut}_+(A)-\operatorname {Cut}_-(A).
\tag{6B.11}
\]

Together with Theorem 6.2 this proves:

### Theorem 6B.1 (augmented packet-cut criterion)

If a row cut satisfies

\[
                    \operatorname {Cut}_+(A)
                    >\operatorname {Cut}_-(A),
\tag{6B.12}
\]

then one of `A,A^c` has strictly positive weighted designated gain.  For
`w_q=1`, one of the two near-trades strictly shortens the complete literal
central-band ledger.  A margin `Omega(W)` in (6B.12) gives an `Omega(W)`
ledger improvement.

There is an exact `L^1` spectral/sweep formulation.  For a weighted graph
`G`, define

\[
 \operatorname {TV}_G(v)
 =\sum_{\{C,D\}}w_G(C,D)|v_C-v_D|.
\tag{6B.13}
\]

Then

\[
\boxed{
 \inf_{A:\operatorname {Cut}_+(A)>0}
 {\operatorname {Cut}_-(A)\over\operatorname {Cut}_+(A)}
 =
 \inf_{v:\operatorname {TV}_{G^+}(v)>0}
 {\operatorname {TV}_{G^-}(v)\over
  \operatorname {TV}_{G^+}(v)}.}
\tag{6B.14}
\]

Indeed, indicators give one inequality.  For the other, the layer-cake
identity gives simultaneously

\[
 \operatorname {TV}_{G^\pm}(v)
 =\int_{-\infty}^{\infty}
   \operatorname {Cut}_{G^\pm}(\{C:v_C\le t\})\,dt.
\tag{6B.15}
\]

Thus a ratio lower bound for every cut integrates to the same ratio lower
bound for every vector.  In particular, a profitable augmented cut exists
if and only if some vector has

\[
                 \operatorname {TV}_{G^+}(v)
                 >\operatorname {TV}_{G^-}(v).
\tag{6B.16}
\]

Unlike ordinary quadratic Cheeger inequalities, (6B.14) loses no square
root and no constant.  The price is that the numerator and denominator are
two different graphs.

### 6B.2 Exact size and degree scales

The owner graph has total off-diagonal edge weight at most `W` and maximum
weighted degree at most `2n`.  A common commodity has total edge weight at
most `w_q`.  A row is in exactly `n` old depth-`q` supports and exactly `n`
new depth-`q` supports, so the common part at depth `q` has

\[
 |G^-_{{\rm common},q}|\le w_qN_q,
 \qquad
 \Delta(G^-_{{\rm common},q})\le2nw_q.
\tag{6B.17}
\]

An exclusive clique of support size `k` has total edge weight

\[
 {4w_q\over k^2}{k\choose2}
 =2w_q{k-1\over k}<2w_q,
\tag{6B.18}
\]

and contributes weighted degree at most `w_q` to each incident row.
Therefore

\[
 |G^+_q|\le2w_qN_q,
 \qquad
 \Delta(G^+_q)\le nw_q.
\tag{6B.19}
\]

Summing through depth `H`,

\[
\boxed{
 \begin{aligned}
 |G^-|&\le W+\sum_{q\le H}w_qN_q,&
 \Delta(G^-)&\le2n+2n\sum_{q\le H}w_q,\\
 |G^+|&\le2\sum_{q\le H}w_qN_q,&
 \Delta(G^+)&\le n\sum_{q\le H}w_q.
 \end{aligned}}
\tag{6B.20}
\]

At `q=1,w_1=1`, both graphs have total weight `O(W)` and maximum degree
`O(n)`; more explicitly `|G^-|<=W+N_1`, `|G^+|<=2N_1`,
`Delta(G^-)<=4n`, and `Delta(G^+)<=n`.

For `H=ceil(A sqrt(m))` with fixed `A>0`, the Gaussian estimate

\[
 {N_q\over W}=\exp(-q^2/m+O_A(m^{-1/2}))
\tag{6B.21}
\]

shows, both for literal weights `w_q=1` and for overload weights
`w_q=1/c_q`, that

\[
 \sum_{q\le H}w_qN_q=\Theta_A(W\sqrt m),
 \qquad
 \sum_{q\le H}w_q=\Theta_A(\sqrt m).
\tag{6B.22}
\]

Thus the raw augmented graph over a Gaussian window has total commodity
weight `Theta_A(W sqrt(m))` and degree `Theta_A(n sqrt(m))`.  Any positive
theorem must exploit the signed distinction between `G^+` and `G^-`; a
bound using only their separate total weights loses the fatal factor
`sqrt(m)`.

### 6B.3 What the long-cycle class average does, and does not, control

Let `R_q` be the target-by-row support matrix

\[
 R_q(S,C)=\mathbf1_{\{C\in\mathsf O_q(S)\}},
\tag{6B.23}
\]

let `D_q=diag(k_q(S))`, and put `Z_q=D_q^\dagger R_q`, using zero rows at
holes.  For `x=1_A`, the vector `u=Z_qx` has coordinates (6B.2).  If
`P_sigma` is the target permutation, the unsigned normalized support
crossing is

\[
\begin{aligned}
 X_{\sigma,q}(A)
 &=\sum_S\bigl[u(S)(1-u(\sigma^{-1}S))
 +(1-u(S))u(\sigma^{-1}S)\bigr]\\
 &=2\mathbf1^{\mathsf T}u
   -2\langle u,P_\sigma u\rangle.
\end{aligned}
\tag{6B.24}
\]

For a uniform coordinate `n`-cycle, the class average on rank-`(m-q)`
targets is `Pi_0-(n-1)^{-1}Pi_1`.  Consequently, with
`T=1^T u`,

\[
\boxed{
 \mathbb E_\sigma X_{\sigma,q}(A)
 =2T-{2T^2\over N_q}
   +{2\|\Pi_1u\|_2^2\over n-1}.}
\tag{6B.25}
\]

This is an exact class-average formula for the normalized support geometry
of every **fixed** row cut.  The signed pieces can also be averaged, but
they require more vectors than `u` alone.  Put

\[
 g_q(S)=\mathbf1_{\{k_q(S)>0\}},\qquad
 h_q=\mathbf1-g_q,\qquad
 v_q=g_q-u_q,\qquad a_q=u_qv_q.
\tag{6B.26}
\]

Thus `u_q,v_q` are the fractions of the old support on the two shores, and
`a_q(S)=u_q(S)(1-u_q(S))` on covered targets.  Directly from the graph
definitions,

\[
 \operatorname {Cut}_{+,q}(A)
 =4w_q\langle a_q,P_\sigma h_q\rangle,
\tag{6B.27}
\]

whereas the common part of the negative cut is

\[
 \operatorname {Cut}^{\rm common}_{-,q}(A)
 =w_q\bigl(
   \langle u_q,P_\sigma v_q\rangle
  +\langle v_q,P_\sigma u_q\rangle\bigr).
\tag{6B.28}
\]

Let `T_q=Pi_0-(n-1)^(-1)Pi_1` be the `n`-cycle class-average operator on
rank-`(m-q)` targets.  Since the class is inverse-closed, `T_q` is
self-adjoint.  Combining (5.3), (6B.27), and (6B.28) gives the exact signed
fixed-cut average

\[
\boxed{
 \begin{aligned}
 \mathbb E_\sigma[\operatorname {Cut}_+(A)
                    -\operatorname {Cut}_-(A)]
 ={}&\sum_{q\le H}w_q
 \bigl(4\langle a_q,T_qh_q\rangle
       -2\langle u_q,T_qv_q\rangle\bigr)\\
 &-2n|A|\left(1-{|A|\over B}\right).
 \end{aligned}}
\tag{6B.29}
\]

Equivalently, each depth-`q` summand before the owner debit is

\[
 \begin{aligned}
 4\left({(\mathbf1^Ta_q)(\mathbf1^Th_q)\over N_q}
 -{\langle\Pi_1a_q,\Pi_1h_q\rangle\over n-1}\right)
 -2\left({(\mathbf1^Tu_q)(\mathbf1^Tv_q)\over N_q}
 -{\langle\Pi_1u_q,\Pi_1v_q\rangle\over n-1}\right).
 \end{aligned}
\tag{6B.30}
\]

Thus positivity of the right side of (6B.29) is a rigorous sufficient
condition: the fixed cut `A` has some long cycle for which one shore gives a
profitable near-trade.  This is the strongest conclusion obtainable from
the class average alone.

It still does not control the adaptive augmented ratio (6B.14).  The
quantity in (6B.24) merges common, old-only, and new-only target transitions
with the same positive sign, while (6B.29) shows that the signed margin also
depends on the separate nonlinear vectors `a_q,u_q,v_q,h_q`.  More
importantly, the useful cut may depend on `sigma`, whereas (6B.29) averages
a cut fixed in advance.  Therefore the already proved long-cycle
class-average spectrum does not by itself imply
`TV_(G^+)>TV_(G^-)` for an adaptively chosen cut.

The exact remaining theorem in this lane is now a signed, adaptively
selected comparison between these two explicit augmented graphs.  It is
strictly stronger information than owner-overlay spectrum or unsigned
support crossing alone.

### 6B.4 An abstract packet countermodel and the minimal extra property

The failure of unsigned control is algebraic, not a weakness of the
estimates above.  Here is a finite packet/load countermodel.

Take eight row packets and a balanced cut `A` of four rows.  Take two
disjoint three-cycles of targets under `sigma`.  On each target cycle the
old support sequence is

\[
                         (\varnothing,X,Y),
\tag{6B.31}
\]

where every nonempty support has size four.  Thus each cycle has one
old-only transition, one common transition, and one new-only transition.
Write

\[
 x={|X\cap A|\over4},\qquad y={|Y\cap A|\over4}.
\]

For this cycle, the unsigned crossing (6B.24) and the signed shadow margin
before the owner debit are respectively

\[
 X_{\rm unsigned}=2(x+y-xy),
\qquad
 X_{\rm signed}=4x(1-x)-(x+y-2xy).
\tag{6B.32}
\]

Compare the following two models.

* Model I uses `(x,y)=(0,1/2)` on the first target cycle and
  `(x,y)=(1,1/2)` on the second.
* Model II uses `(x,y)=(1/2,1/2)` on both target cycles.

Both models have the same target-load multiset

\[
                         (0,4,4,0,4,4),
\tag{6B.33}
\]

and the same total unsigned crossing, namely `3`.  The total numbers of
support incidences on the two row shores are also the same: eight on each
shore.  Averaging either construction under all permutations within `A`
and within `A^c` makes every row incidence exactly regular without changing
the equality of the load and unsigned-crossing data or the opposite signs
of the two margins (all extensive quantities are merely multiplied by the
same orbit size).  Give the two models the same owner graph (for example
the zero owner graph).

Padding the initial empty position in each target cycle by any number of
additional consecutive empty supports changes none of the crossing or
signed-margin calculations.  Thus the two target cycles may be given any
prescribed common length `ell>=3`, in particular `ell=n`.  The example
therefore survives the orbit-length constraint of a prime-order coordinate
cycle, although it is still not asserted to arise from actual subset
supports of a wreath factor.

Nevertheless, (6B.32) gives

\[
 X_{\rm signed}({\rm Model\ I})=-1,
 \qquad
 X_{\rm signed}({\rm Model\ II})=+1.
\tag{6B.34}
\]

Thus owner spectrum, cut density, target load sizes, row-incidence
regularity, and even the exact unsigned normalized support crossing do not
determine the sign of `Cut_+-Cut_-`.  This is an abstract packet model, not
a claimed wreath realization; its force is that no formal argument using
only those aggregate inputs can prove the needed signed inequality.

For an actual wreath factor the minimal additional algebraic property can
be stated without graph language.  With the vectors (6B.26), one needs a
long cycle `sigma` and a row cut `A` such that

\[
\boxed{
 4\sum_{q\le H}w_q\langle a_q,P_\sigma h_q\rangle
 >
 \partial_\sigma(A)
 +\sum_{q\le H}w_q
  \bigl(\langle u_q,P_\sigma v_q\rangle
       +\langle v_q,P_\sigma u_q\rangle\bigr).}
\tag{6B.35}
\]

The left side is **exclusive-support dispersion**: old-only supports must
straddle the cut.  The second term on the right is **common-support
misalignment**: old and pulled-back supports of targets covered on both
sides must not lie on opposite shores.  The first right-hand term is the
middle owner debit.  Equation (6B.35) is exactly (6B.12), not a relaxation.

There is also a sharp necessary support condition hidden in its left side.
Define the collision-to-hole transition count

\[
 J_{\sigma,q}
 =\#\{S:k_q(S)\ge2,\ k_q(\sigma^{-1}S)=0\}.
\tag{6B.36}
\]

A singleton old-only support cannot be split, while every other exclusive
clique has cut at most `w_q`.  Hence

\[
 \boxed{\operatorname {Cut}_{+,q}(A)\le w_qJ_{\sigma,q}.}
\tag{6B.37}
\]

Thus a coefficient-scale profit requires collision-rich targets to be sent
next to holes by the **same** coordinate permutation.  At the first shadow,
if `h=M_1` and `r=W-N_1=2W/(m+2)`, then

\[
 \#\{S:k_1(S)\ge2\}\le h+r,
\tag{6B.38}
\]

because the total duplicate excess is exactly
`sum_S(k_1(S)-1)_+=h+r`.  Long-cycle averaging computes only the mean

\[
 \mathbb E_\sigma J_{\sigma,q}
 ={|\{k_q\ge2\}|\,|\{k_q=0\}|\over N_q}
 -{\langle\Pi_1\mathbf1_{\{k_q\ge2\}},
          \Pi_1\mathbf1_{\{k_q=0\}}\rangle\over n-1};
\tag{6B.39}
\]

it does not align these transitions with a low-owner-boundary cut.

Accordingly, the minimal new property is a signed shadow-assortativity
theorem coupling all three features on the same `(sigma,A)`.  Parallel-pair
or long-cycle spectrum controls the owner debit; class averaging controls
fixed-cut bilinear means; neither supplies the required conditional sign
between exclusive dispersion and common alignment.  Any successful
algebraic factor construction must add precisely that conditional
correlation.

### 6B.5 A total-mass sufficient test and its exact class average

There is a stronger but easily testable sufficient condition.  Choose each
row independently for `A` with probability `1/2`.  Every nonloop edge of
either augmented graph crosses with probability `1/2`.  Therefore

\[
\boxed{
 |G^+_{\sigma,w,H}|>|G^-_{\sigma,w,H}|
 \quad\Longrightarrow\quad
 \text{some row cut satisfies (6B.12)}.}
\tag{6B.40}
\]

Here total edge weight has exact support formulas.  Put

\[
 b_q(S)=\mathbf1_{\{k_q(S)>0\}}\left(1-{1\over k_q(S)}\right),
\tag{6B.41}
\]

and retain the normalized support matrix `Z_q` from (6B.23).  Then

\[
\boxed{
 |G^+_{\sigma,w,H}|
 =2\sum_{q\le H}w_q
   \langle b_q,P_\sigma h_q\rangle,}
\tag{6B.42}
\]

because an exclusive clique of support size `k` has total weight
`2w_q(1-1/k)`.  The owner graph has total off-diagonal weight

\[
                         W-\operatorname {tr}M_\sigma,
\tag{6B.43}
\]

and the common commodities have total weight

\[
\boxed{
 \sum_{q\le H}w_q\left(
  \langle g_q,P_\sigma g_q\rangle
  -\sum_{C\in F}\langle Z_q(\cdot,C),
                         P_\sigma Z_q(\cdot,C)\rangle
 \right).}
\tag{6B.44}
\]

Indeed, the first term counts common target transitions.  For such a
transition, the deleted loop mass in its normalized bipartite commodity is
the inner product of its two support-probability vectors; summing over rows
gives the second term.

All terms in (6B.42)--(6B.44) have exact long-cycle class averages.  Since
`E K_sigma=J_B/B`,

\[
 \mathbb E_\sigma\operatorname {tr}M_\sigma=n.
\tag{6B.45}
\]

With `T_q=Pi_0-(n-1)^(-1)Pi_1`, one obtains

\[
\boxed{
 \begin{aligned}
 \mathbb E_\sigma(|G^+|-|G^-|)
 ={}&2\sum_{q\le H}w_q\langle b_q,T_qh_q\rangle-(W-n)\\
 &-\sum_{q\le H}w_q\left(
   \langle g_q,T_qg_q\rangle
   -\sum_{C\in F}\langle Z_q(\cdot,C),
                          T_qZ_q(\cdot,C)\rangle
                         \right).
 \end{aligned}}
\tag{6B.46}
\]

If the right side is positive, one long cycle satisfies the total-mass
test (6B.40), and hence yields a profitable near-trade.  This criterion is
genuinely checkable from the load/support harmonics of `F`.

It is also deliberately strong.  At depth one,

\[
 |G^+_{\sigma,1}|\le2J_{\sigma,1}\le2M_1,
\tag{6B.47}
\]

while a generic long cycle has owner mass close to `W` (its exact class
average is `W-n`) even before the nonnegative common cost is included.
In fact, for the first-depth graph alone,

\[
 \mathbb E_\sigma(|G^+|-|G^-|)
 \le2M_1-(W-n).
\tag{6B.48}
\]

Thus factors with first-shadow hole density below `1/2-o(1)` have negative
mean total-mass margin.  The exact `L^1` criterion
(6B.14) remains substantially more flexible: it asks for a localized cut
on which the positive graph dominates, not domination of total mass.

## 7. Guaranteed algebraic fragmentation, and why it is trivial

Fix one wreath row `C in F`, choose an orientation of its cyclic coordinate
order, and let `sigma_C` be the one-step rotation of its coordinates.  Then
`sigma_C` is an `n`-cycle and

\[
                         \sigma_C{\cal W}_m(C)
                         ={\cal W}_m(C).
\tag{7.1}
\]

Every middle set owned by `C` therefore gives an owner-overlay edge from
the left copy of `C` to the right copy of `sigma_C C=C`; all `n` incident
edges remain inside this pair.  Hence:

\[
 \boxed{
 \text{the }F/\sigma_CF\text{ owner overlay has an isolated one-row
 component}.}
\tag{7.2}
\]

Equivalently `e_C` is a nonconstant singular-value-one vector of
`K_(sigma_C)`, and the principal-angle intersection has dimension at least
two (the isolated packet and its complement).

This is genuine graph fragmentation but not a useful factor trade:
`sigma_C C=C`, so switching the isolated component changes no row and no
shadow.  Switching its complement merely changes `F` to the whole relabel
`sigma_C F`, which has the same hole counts.  Thus an algebraic `n`-cycle
with guaranteed **nontrivial productive** fragmentation is still missing.

## 8. Orbit rounding for a very small boundary

Let `sigma` be any permutation of order at most `n` on the middle layer;
in particular this holds for a coordinate `n`-cycle.  For an arbitrary set
`U subseteq Omega`, put

\[
                         b=|U\triangle\sigma U|.
\]

On every `sigma`-orbit, round the binary membership word of `U` to its
majority constant.  A nonconstant orbit of length `ell<=n` has at least two
membership transitions, and its minority size is at most `ell/2`.  Summing
orbitwise gives a `sigma`-invariant set `U^*` with

\[
 \boxed{
 |U\triangle U^*|\le {n\over4}|U\triangle\sigma U|.}
\tag{8.1}
\]

Consequently boundary `o(W/n)` forces a packet union to be `o(W)`-close to
a union of full coordinate-cycle orbits.  The coefficient-one condition
only gives boundary `o(W)`, so this orbit-rounding statement does not by
itself classify all usable near-trades; it records the stronger regime in
which algebraic orbit structure becomes unavoidable.

## 9. Multiround implication

The scale (6.6) naturally suggests `Omega(m)` adaptive rounds rather than
one round.  But a near-trade destroys unique middle ownership, so its next
regular owner overlay is undefined unless exactness is restored.  Even in a
common-baseline simultaneous model, final middle defect is

\[
 {1\over2}\left\|\sum_td_t\right\|_1,
\]

not the sum of nominal one-step defects.  `Omega(m)` rounds each costing
only `O(W/m)` can still accumulate `Theta(W)` middle error.  A viable
long-cycle schedule therefore needs one of:

1. exact component switches after each bridge;
2. a signed cancellation theorem for the final middle updates;
3. a common low-conductance laminar cut whose total boundary, rather than
   each per-round boundary, is `o(W)`.

The long-cycle class average proves opportunity.  The missing theorem is
the joint opportunity--principal-angle correlation on one legal integral
cut, together with a nonaccumulating multiround realization.
