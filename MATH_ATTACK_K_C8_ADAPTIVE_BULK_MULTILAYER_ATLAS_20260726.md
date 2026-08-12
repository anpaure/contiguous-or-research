# Adaptive bulk reciprocal-`C_8` layers: a literal bounded cube and its carrier ceiling

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

Fix `u in {4,5,6,7}`.  There is a literal context-adaptive atlas with all
of the following properties.

1. Every layer is a completed reciprocal `C_8` factor trade, not an open
   incidence cycle.
2. The `u` partial factor involutions commute through the complete `X/Y`
   ledger.
3. Every layer contains

   \[
       M_{r,u}=C_{r-2}+O_u(1)
              =\left({1\over16}+o(1)\right)C_r       \tag{0.1}
   \]

   reciprocal packets.
4. The direct old/all-on overlay has `L_(r,u)` nontrivial components, each
   of shore size `2^u<=128`, and all other rows are singleton components.
   In particular

   \[
       \chi_r\longrightarrow1+{2^u-1\over8}.          \tag{0.2}
   \]

The construction uses invariant, pairwise disjoint **adaptive bulk
contexts**, not fixed top-level word gaps.  It therefore evades the
fixed-position ceiling
`C_aC_(r-a-2)` without contradicting it.

The candidate nevertheless fails at the signed carrier gate.  Every
selected packet is suspended once and lies a positive linear distance
from the left word end.  The exact boundary recursion in Section 5 gives

\[
                         \Delta I_{\rm root}
                         =\Delta D_{\rm root}=0.       \tag{0.3}
\]

An arbitrary top-level suspended packet need not satisfy the deletion
equality in (0.3); the bulk/non-prefix placement is essential.  Thus the
atlas's local entrance unit is not a global first-boundary unit.  Its
complete depth-`q` carrier is the reciprocal four-arm vector

\[
 \Delta_q=
   \partial_\beta^\gamma\operatorname{suf}(O)
  +\partial_\beta^\gamma\operatorname{suf}(E)
  -\partial_\beta^\gamma\operatorname{pre}(E)
  -\partial_\beta^\gamma\operatorname{pre}(O),       \tag{0.4}
\]

including both cyclic collars.  It has half-`l_1` action two at depth one
and at most four at every proper depth.  Consequently the entire `u`-layer
atlas has only `O(u)` moved starts per edited row.

After a critical first-fringe lift from local rank
`r=Theta(sqrt(m))` to ambient rank `m`, for
`H=ceil(A sqrt(m))`, every atlas state obeys

\[
 \boxed{
 {1\over2}\sum_{q\le H}{1\over c_q}
       \|\mu_q^{\rm child}-\mu_q^{\rm base}\|_1
 \le \left({u\over4}+o_u(1)\right)C_m
                    \sum_{q\le H}{1\over c_q}
 =O_A\!\left({uW_m\over\sqrt m}\right)=o_A(W_m).}    \tag{0.5}
\]

Hence the construction meets literal completion, commutation, density,
and bounded-component requirements, but it is not a `CRH_A` pair.  In
particular it cannot reduce a weighted balanced-overload functional, or
any other half-`l_1`-Lipschitz carrier functional, by `Omega(W_m)`.
Separation of the local
slots across `Theta(r)` word distance does not help: a cyclic interval has
only two boundaries, and the number of changed boundary positions is
controlled by the number of local swaps, not by their span.

The first exact failure in the proposed implication is therefore

> `C_r/16` reciprocal packets in a bulk layer do **not** provide
> `C_r/16` aligned parent-boundary carrier units.

## 1. The completed reciprocal atom

The canonical rooted rank-two traces are

\[
\begin{array}{c|ccc}
1100&12&14&34\\
1010&13&23&24,
\end{array}                                             \tag{1.1}
\]

and the reciprocal rectangle replaces them by

\[
\begin{array}{c|ccc}
1100&12&23&34\\
1010&13&14&24.
\end{array}                                             \tag{1.2}
\]

Both shores have the same lower-state palette

\[
                    \{12,13,14,23,24,34\}             \tag{1.3}
\]

and the same adjacent-union palette

\[
                    \{123,124,134,234\}.              \tag{1.4}
\]

The row rooted at `1100` still ends at its complement `34`, and the row
rooted at `1010` still ends at `24`.  Thus (1.1)--(1.2) are a sealed
two-row rooted port-factor trade.  Their incidence symmetric difference is
the reciprocal alternating `C_8`.

The rooted one-hole context theorem applies: wrapping both rows in any
common ordered-tree context transports (1.3)--(1.4) injectively, while the
two crossing collars depend only on the unchanged local ports.  Hence
every contextual copy is a literal completed-factor trade.

Each changed rooted cyclic word makes one adjacent transposition in its
deletion half and one in its insertion half.  Therefore its rooted edit
distance is exactly

\[
                              d(P)=2.                 \tag{1.5}
\]

## 2. An invariant supply of genuinely bulk holes

Suspend the two local roots once:

\[
 A=J(1100)=111000,
 \qquad
 B=J(1010)=110100,
 \qquad J(x)=1x0.                                    \tag{2.1}
\]

For a size-`r` ordered binary tree `T`, let `N(T)` count fringe roots whose
complete size-three fringe filling is `A` or `B`.  These fringe roots are
pairwise disjoint.  Replacing `A` by `B`, or conversely, preserves the
entire ordered occurrence list:

* the toggled root remains an `A/B` root of size three;
* its proper descendants have size below three;
* every strict ancestor retains its size; and
* every disjoint fringe subtree is unchanged.

The bivariate generating function is

\[
 \mathcal T(z,y)=1+z\mathcal T(z,y)^2+2(y-1)z^3
 ={1-\sqrt{1-4z+8(1-y)z^4}\over2z}.                 \tag{2.2}
\]

### Lemma 2.1 (linear bulk supply)

There is an absolute `delta>0` such that

\[
       |\{T\in D_r:N(T)<\delta r\}|=o(C_r)            \tag{2.3}
\]

exponentially in `r`.

#### Proof

Fix `0<y<1`.  The discriminant in (2.2) is positive at `z=1/4` and is
strictly decreasing on `[0,1/4]`; by nonnegative coefficients and
Pringsheim, the radius `rho(y)` of `T(z,y)` is strictly larger than
`1/4`.  Choose a real number `R` with

\[
                         {1\over4}<R<\rho(y).         \tag{2.4}
\]

Coefficient positivity gives

\[
 \sum_{T\in D_r}y^{N(T)}=[z^r]\mathcal T(z,y)
       \le \mathcal T(R,y)R^{-r}.                    \tag{2.5}
\]

If `B_r(delta)=|{T:N(T)<delta r}|`, then, because `0<y<1`,

\[
 B_r(\delta)y^{\delta r}
       \le\sum_{T\in D_r}y^{N(T)}.
\]

Choose `delta>0` so small that `4Ry^delta>1`.  Using
`C_r~4^r/(sqrt(pi)r^(3/2))`, (2.5) gives

\[
 {B_r(\delta)\over C_r}
   \le r^{O(1)}(4Ry^\delta)^{-r}=o(1)
\]

exponentially.  This proves (2.3). \(\square\)

On the family in (2.3)'s complement, select the occurrences of ranks

\[
 j_i(T)=\left\lceil{iN(T)\over u+1}\right\rceil,
 \qquad1\le i\le u.                                \tag{2.6}
\]

Changing any selected filling preserves `N(T)` and the whole occurrence
list, so it preserves every selected index.  For fixed `u` and large `r`,
the number of intervening occurrences between consecutive selected ones,
and between a selected occurrence and either end of the occurrence list,
is at least

\[
                 {N(T)\over u+1}-2
                 \ge {\delta r\over2(u+1)}.          \tag{2.7}
\]

The intervening size-three fringe words are disjoint six-bit intervals.
Consequently the selected blocks are separated from one another and from
both word ends by at least

\[
                       {3\delta r\over u+1}-O(1)     \tag{2.8}
\]

word positions.  Thus they are genuinely bulk contexts, not endpoint-
prefix copies.

## 3. The commuting `u`-layer atlas

The selected occurrences generate free Boolean orbits.  A root with the
chosen `u` fillings has orbit

\[
                         \mathcal O\cong\{0,1\}^u,    \tag{3.1}
\]

where bit `i` records `A` or `B` at the `i`-th selected fringe root.
Equation (2.3) gives

\[
                  {C_r-o(C_r)\over2^u}               \tag{3.2}
\]

such orbits.

Choose

\[
 L_{r,u}=\left\lfloor{C_{r-2}\over2^{u-1}}\right\rfloor          \tag{3.3}
\]

of them.  This is possible for all sufficiently large `r`, since the
available number in (3.2) is asymptotically eight times larger.

For each mask `eta in {0,1}^u`, define `F^eta` by using shore `eta_i` of
the reciprocal packet in selected slot `i` of every chosen orbit and
using the canonical paths elsewhere.  Explicitly, on a root with filling
mask `epsilon`, its `i`-th slab is the `A`-row or `B`-row of the old local
table when `eta_i=0`, and the corresponding row of the new local table
when `eta_i=1`.

### Theorem 3.1 (literal commuting factor cube)

Every `F^eta` is an anchored exact factor.  The `u` coordinate switches
commute in the full lower-state, adjacent-union, and root/complement port
ledgers.

#### Proof

Within one row, the selected fringe carriers are disjoint.  The MSW rooted
context recursion processes their local packets in disjoint contiguous
phase slabs, possibly reversing/complementing a slab but never
interleaving two of them.  On either local shore the slab has the same two
boundary states.  Thus choosing either variant independently in each slab
still concatenates to a geodesic with the original global endpoints, and
the row obtained is independent of the order of the choices.

Ledger equality is an aggregate, not a rowwise, statement.  Fix a
coordinate `i` and all choices at the other slots.  Pair the `2^u` roots
of an orbit along its `i`-edges.  In each pair the other fillings and all
other slab variants agree, so they are common exterior material for the
local two-row packet.  Section 1, with the fixed collars included, says
that switching slot `i` preserves the pair's aggregate `X/Y` ledger and
both ports.  The `2^(u-1)` pairs partition the orbit, so the whole orbit
ledger is invariant.  Doing this successively for the chosen coordinates
proves exactness, while disjoint slabs prove commutation.

Different Boolean orbits have disjoint root rows.  Each orbit's aggregate
token ledger is invariant under every coordinate switch, so no ownership
collision occurs between orbits.  Unselected rows are unchanged. \(\square\)

For one coordinate layer, each chosen orbit contains `2^(u-1)` disjoint
reciprocal packets.  Thus

\[
 M_{r,u}=2^{u-1}L_{r,u}
         =C_{r-2}+O_u(1),                             \tag{3.4}
\]

which proves (0.1).  The layer changes

\[
 2^uL_{r,u}=2C_{r-2}+O_u(1)
           =\left({1\over8}+o(1)\right)C_r            \tag{3.5}
\]

root rows.

The fixed-top-level-position formula
`C_aC_(r-a-2)` does not apply to (3.4): the selected hole position depends
on the invariant occurrence list of the current Boolean orbit.  No
coordinate conjugate or quotient ledger is used.

## 4. Full overlay components and edit moment

Compare `F^0` with `F^1`, where `1=(1,...,1)`.  On every chosen orbit,
the common root tokens give the identity shore matching.  Fix the other
`u-1` filling bits.  The contextual image of local state `14` is owned in
`F^0` by the `A`-root and in `F^1` by the `B`-root; the contextual image
of `23` gives the reverse cross-ownership.  Thus, for every coordinate
`i`, these exchanged middle states give every Boolean axis edge

\[
             \epsilon\;--\;\epsilon+e_i.             \tag{4.1}
\]

Phase-disjointness ensures that the all-on edits in the other slots do not
alter these two axis witnesses.  Hence the direct full `X/Y` overlay is
connected on that orbit.  Successive sealed-packet equalities say that
the complete `X/Y` multiset owned by the orbit is identical on the two
shores, so no ownership edge leaves it.  Root/complement ports, and every
lifted exterior port signature, agree rowwise; port closure therefore adds
only diagonal edges and cannot merge two orbits.  The component has
exactly `2^u` rows per shore.  All other rows are diagonal singletons.

Put

\[
                         R_{r,u}=2^uL_{r,u}.           \tag{4.2}
\]

Then

\[
\begin{aligned}
 \chi_r
 &= {C_r-R_{r,u}+L_{r,u}4^u\over C_r}\\
 &=1+(2^u-1){R_{r,u}\over C_r}
 \longrightarrow1+{2^u-1\over8}.                    \tag{4.3}
\end{aligned}
\]

For `u=4,5,6,7`, the limiting values are respectively

\[
                 {23\over8},\quad{39\over8},
                 \quad{71\over8},\quad{135\over8}.   \tag{4.4}
\]

Every active row contains `u` disjoint local edits, so (1.5) adds exactly:

\[
                              d(P)=2u.                \tag{4.5}
\]

For the edit-weighted component moment

\[
             C_r\Xi_r=\sum_K|K|\sum_{P\in K}d(P),    \tag{4.6}
\]

one obtains

\[
 \Xi_r={2uL_{r,u}4^u\over C_r}
       \longrightarrow u2^{u-2}.                     \tag{4.7}
\]

These limits are `16,40,96,224` for `u=4,5,6,7`.  They are bounded in
`r`; neither ownership fragmentation nor sparse-edit rounding is the
failure.

## 5. Exact signed all-depth carrier

For one contextual packet, let `beta,gamma` be its adjacent active
coordinates and put

\[
        \partial_\beta^\gamma H
          =e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.   \tag{5.1}
\]

At every proper cyclic depth, with the prefix/suffix lengths dictated by
that depth, its complete physical carrier is exactly (0.4).  The four
terms include the two entrance arms, the two exit arms, and both crossing
collars.  At depth one it reduces to

\[
                         -e_A+e_B+e_C-e_D,             \tag{5.2}
\]

with four distinct targets and half-`l_1` action two.  At a generic
interior depth the eight displayed targets are distinct and the half-
`l_1` action is four; at exceptional depths collisions are retained in
(0.4), and the half-`l_1` action is at most four.

For the transition `F^eta -> F^(eta+e_i)`, sum (0.4) over the
`M_(r,u)` packets in layer `i`, with their literal context-specific cores.
For `F^0 -> F^1`, telescope through the `u` commuting layers in any order.
This is an exact occurrence-resolved formula.  It also gives the
statewise bounds

\[
 {1\over2}\|\mu_1^{F^1}-\mu_1^{F^0}\|_1
      \le2uM_{r,u}
      =\left({u\over8}+o_u(1)\right)C_r,              \tag{5.3}
\]

and, at every proper depth,

\[
 {1\over2}\|\mu_q^{F^1}-\mu_q^{F^0}\|_1
      \le4uM_{r,u}
      =\left({u\over4}+o_u(1)\right)C_r.              \tag{5.4}
\]

Target collisions and interaction of two switched interval boundaries can
only lower these triangle bounds.  More structurally, context lifting
sends each local reciprocal row edit to two adjacent transpositions of
the rooted cyclic order.  The `2u` swap cuts on an active row are distinct
because the phase slabs are disjoint.  A contiguous interval changes
under one such transposition exactly when one of its two boundary cuts is
that swap cut.  Therefore a fixed row/start target depends on at most two
layer bits, and its one-hot vector has multilinear Boolean degree at most
two.  Summing occurrences preserves this degree: there are no three-layer
carrier interactions.

For completeness, fix two bits `i,j` on one active row.  There are four
choices of one swap cut from bit `i` and one from bit `j`, and two oriented
cyclic intervals having those two cuts as boundaries.  Each resulting
mixed one-hot second difference has half-`l_1` at most two.  Hence

\[
 \sum_q {1\over2}\|\Delta_i\Delta_j\mu_q(P)\|_1\le16. \tag{5.5}
\]

Over all selected rows and the fixed `binom(u,2)` bit pairs, the entire
mixed interaction action is `O_u(C_r)=o(W_r)`; the first-order collar
terms are already included in (0.4).

The signed vector has no background-independent favourable orientation.
For the four-cell vector (5.2), at integer cap `c`, the two shore gains are

\[
\begin{aligned}
G_+={}&1_{\mu(A)>c}+1_{\mu(D)>c}
       -1_{\mu(B)\ge c}-1_{\mu(C)\ge c},\\
G_-={}&1_{\mu(B)>c}+1_{\mu(C)>c}
       -1_{\mu(A)\ge c}-1_{\mu(D)\ge c}.             \tag{5.6}
\end{aligned}
\]

If all four loads equal `c`, both orientations cost two.  The interior
eight-cell analogue costs four in both orientations at a flat cap.  A
coordinate or context conjugation pushes all four arms of (0.4) together;
it cannot reverse only the unwanted exit arms.

Finally, the boundary claim (0.3) needs the bulk hypothesis, not merely
the first `J`-wrapper.  Write the local reciprocal boundary signature in
the order first insertion, first deletion, last insertion, last deletion:

\[
                    (v,v,-v,-v),\qquad v=e_3-e_2.    \tag{5.7}
\]

If `S` shifts local labels through a wrapper, the flip identity
`rho_J=(2r+2,1+rev(rho),1)` sends this signature to

\[
                         (0,-Sv,Sv,0).               \tag{5.8}
\]

Thus one `J` kills the local first insertion but can expose the old last
deletion as a new first deletion.  The three unary context operations act
on a general boundary signature `(FI,FD,LI,LD)` as follows, up to the fixed
injective relabelling:

\[
\begin{array}{c|c}
x\mapsto xB,\ B\ne\varnothing &(FI,FD,0,0),\\
x\mapsto Ax,\ A\ne\varnothing &(0,0,LI,LD),\\
x\mapsto J(x)&(0,LD,FI,0).
\end{array}                                           \tag{5.9}
\]

Starting from (5.8), its nonzero first deletion survives to the global
root only if every remaining outer operation is right concatenation,
that is, only if the entire suspended six-bit block is a prefix of the
global Dyck word.  But (2.8) puts every selected block a positive linear
distance from the left word end.  Hence neither first boundary is visible,
and (0.3) follows.  The canonical prefix-layer transfer `e_3-e_2` is not
present.  Notice that this conclusion would be false for an arbitrary
nonbulk suspended copy: the prefix family `J(core)B` retains the shifted
first-deletion arm.  At rank `r` this exceptional family has exactly
`C_(r-3)` reciprocal packets (one for each suffix in `D_(r-3)`), hence
only `(1/64+o(1))C_r` visible deletion units; none belongs to the selected
quantile atlas.

## 6. Ambient carrier ceiling

Already at local rank `r`, put `H_r=ceil(A sqrt(r))` and
`mathsf S_(H_r)=sum_(q<=H_r)1/c_q`.  The exact floor baseline has
`c_1=1`, so the packet bounds give

\[
 {1\over2}\sum_{q\le H_r}{1\over c_q}
       \|\mu_q^{\rm child}-\mu_q^{\rm base}\|_1
 \le(4\mathsf S_{H_r}-2)uM_{r,u}
 =O_A(uC_r\sqrt r)=o(W_r).                           \tag{6.0}
\]

Thus the ceiling is intrinsic to the atlas, not an artefact of the
following lift.

Let the local rank satisfy `r=Theta(sqrt(m))`, and lift `F^0,F^1` through
the disjoint first size-`r` fringe classes of rank `m`.  If `a_(m,r)` is
the number of leftover roots outside those complete classes, then the
number of classes is

\[
                 {C_m-a_{m,r}\over C_r}\le {C_m\over C_r}.     \tag{6.1}
\]

Let

\[
             \mathsf S_H=\sum_{q=1}^{H}{1\over c_q},
             \qquad H=\lceil A\sqrt m\rceil.          \tag{6.2}
\]

One adjacent transposition in the ambient `(2m+1)`-cycle changes at most
two starts at every proper interval length.  Thus a lifted reciprocal
packet has half-`l_1` action at most four for every ambient `q`, including
`q>r` and both collars, and at most two for `q=1`.  Since the exact floor
baseline has `c_1=1`, equations (5.3)--(5.4) give

\[
\begin{aligned}
 {1\over2}\sum_{q\le H}{1\over c_q}
       \|\mu_q^{\rm child}-\mu_q^{\rm base}\|_1
 &\le {C_m\over C_r}(4\mathsf S_H-2)uM_{r,u}\\
 &\le\left({u\over4}+o_u(1)\right)C_m\mathsf S_H.    \tag{6.3}
\end{aligned}
\]

Since `mathsf S_H<=H` and `W_m=(2m+1)C_m`, (6.3) is

\[
                         O_A\!\left({uW_m\over\sqrt m}\right)
                         =o_A(W_m)                    \tag{6.4}
\]

for fixed `u`.  The same conclusion holds for every component child:
expand its selected orbit-components into their elementary packet
differences and apply the same triangle bound.  Omitting an orbit-component
omits all of its packet terms.

In particular, if a weighted balanced-overload functional has value
`kappa W_m+o(W_m)` on the base factor for some fixed `kappa>0`, its value
on every atlas child is at least `kappa W_m-o(W_m)`, because a fixed-mass
cap hinge can decrease by at most the weighted half-`l_1` carrier action.

Equivalently, every active local row changes only `O(u)` coordinate-word
positions.  The `Theta(r)` separation between the chosen slabs does not
create `Theta(r)` active width.  The multi-block two-boundary lemma charges
the total number of changed positions, so this pair fails the extensive
carrier test required by `CRH_A`.

## 7. Exact implication boundary

Proved positively:

* a literal completed reciprocal atom;
* `u` commuting full-ownership layers in one common factor cube;
* genuinely bulk, invariant, phase-disjoint contexts;
* `(1/16+o(1))C_r` packets per layer;
* exact Boolean components of size `2^u`, (4.3), and (4.7);
* the occurrence-resolved all-depth carrier (0.4).

Proved negatively:

* bulk layers have zero global first-boundary transfer;
* reciprocal entrance and exit signs cannot be separated by conjugation;
* the entire fixed-`u` atlas has only `o(W_m)` ambient weighted action;
* therefore it is not a critical-root hinge pair.

The fixed-position Catalan ceiling and the adaptive atlas answer different
questions.  At one predetermined complete-prefix boundary the count is
`C_aC_(r-a-2)` and only endpoint boundaries have density `1/16`.  The
present atlas chooses an invariant bulk context separately in each Boolean
orbit, so that ceiling does not apply.  What remains closed is the carrier:
a viable successor needs a number of physically active seams growing with
`r`, or one nonlocal packet whose single signed carrier moves
`Theta(r)` starts per row while retaining bounded full-overlay components.
