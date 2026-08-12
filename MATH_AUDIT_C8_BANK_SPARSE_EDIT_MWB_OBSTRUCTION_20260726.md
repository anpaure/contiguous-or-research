# Alternating `C_8` banks versus the sparse-edit moment

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 B=\operatorname {Cat}_s,\qquad n=2s+1,\qquad W=nB,
 \qquad H=\lceil A\sqrt s\rceil,
 \qquad {\mathsf S}_H=\sum_{q=1}^H{1\over c_q}.
\]

There are two different `C_8` objects.

* A reciprocal, or folded, `C_8` cuts two rooted paths twice and exchanges
  their middle segments.  It is already port-preserving.  Its full ownership
  component has two roots.
* A clean `C_8` cuts four distinct rooted paths once and has a four-cycle
  endpoint monodromy.  One clean `C_8` is not an anchored factor and hence has
  no sparse-edit moment.  A zero-monodromy packet, such as a coherent
  four-stage conveyor, is an anchored factor.  Its nontrivial full ownership
  component has four roots.

For a pair of factors `F,G`, define the weighted endpoint carrier motion

\[
 {\mathscr A}_H(F,G)
  ={1\over2}\sum_{q=1}^H{1\over c_q}
       \|\mu_q^G-\mu_q^F\|_1.                         \tag{0.1}
\]

If every nontrivial full component in the bank has exactly `b` roots, then
the sparse-edit theorem gives the following action--moment inequality

\[
 \boxed{
 {\mathscr A}_H(F,G)
       \le {2B{\mathsf S}_H\over b}\,\Xi(F,G),
 \qquad
 {{\mathscr A}_H(F,G)\over W}
       \le {2{\mathsf S}_H\over bn}\,\Xi(F,G).}       \tag{0.2}
\]

It holds for every component child as well, with the sums restricted to the
chosen components.  Since `mathsf S_H<=H`, a bank with

\[
                         \Xi=o_A(\sqrt s)              \tag{0.3}
\]

has `mathscr A_H=o_A(W)`.

This implication has to be normalized correctly.  A presently audited
**positive-density row demand** asks for `Omega(B)` changed roots, not for
`Omega(W)` endpoint motion.  That demand is compatible with bounded `Xi`:
a hypothetical perfect packing of elementary folded rectangles would have
`Xi=4` while changing all its rows.  Therefore there is no unconditional
sparse-edit obstruction to a hypothetical dense bounded-`C_8` atlas.

There are two stronger, conditional conclusions.

1. If an application separately proves that the two endpoints must differ
   by at least `kappa W` in the weighted carrier metric (0.1), then
   
   \[
   \boxed{
   \Xi\ge {\kappa b n\over2{\mathsf S}_H}
         \ge\left({\kappa b\over A}+o_A(1)\right)\sqrt s.} \tag{0.4}
   \]
   
   Such a demand is incompatible with `Xi=o(sqrt(s))`.  It must not be
   silently substituted for the weaker row demand.
2. The audited critical-root construction gate additionally requires a
   positive-density set of roots to change `Theta(s)` positions of the
   active coordinate word.  Under that explicit active-width clause,
   every bounded-component `C_8` bank has `Xi=Omega(s)`, as proved in
   Section 1.2.

## 1. Weighted carrier demand is controlled by rooted edit distance

Let `d(P)` be the rooted adjacent-transposition distance between the two
cyclic coordinate words at root `P`, and put

\[
 D_K=\sum_{P\in K}d(P),\qquad
 D_{\rm tot}=\sum_KD_K.
\]

The two-start lemma for one adjacent transposition gives, at every depth,

\[
 \|\mu_q^G-\mu_q^F\|_1
 \le\sum_P\|h_{G,P,q}-h_{F,P,q}\|_1
 \le4D_{\rm tot}.                                    \tag{1.1}
\]

After multiplication by `1/(2c_q)` and summation,

\[
             {\mathscr A}_H(F,G)\le2{\mathsf S}_HD_{\rm tot}. \tag{1.2}
\]

If all nontrivial components have size `b`, then

\[
                 B\Xi=\sum_KbD_K=bD_{\rm tot},        \tag{1.3}
\]

and (0.2) follows.  More generally (0.2) remains true with `b` replaced
by a lower bound on the sizes of components carrying nonzero edit distance.

This is one useful carrier metric.  It must not be confused with the
weaker audited parent-packet demand.  At depth `q`, balanced overload is

\[
 O_q(\mu)={1\over2}\min_{z\in\mathcal B_q}\|\mu-z\|_1.
\]

Distance to a fixed set is one-Lipschitz, so

\[
 \left|\sum_{q\le H}{O_q(\mu^G)-O_q(\mu^F)\over c_q}\right|
 \le {\mathscr A}_H(F,G).                             \tag{1.4}
\]

Consequently, **if** an endpoint or component child is required to repair a
weighted defect of size `kappa W` by direct endpoint transport, it must
satisfy (0.4).  Target collisions, collars, and opposite signs can only
decrease the left side of (1.1), so they cannot evade that conditional
obstruction.  No assertion that the current local MWB demand is always
`kappa W` is made here.

The exact parent-packet ledger instead has the scalar condition

\[
 \lambda^{\rm act}_{r,s}\gamma_{r,s}
            \ge {\delta_\theta\over2s+1}.             \tag{1.4a}
\]

Equivalently, it asks for `delta_theta B` useful moved occurrences in one
protected depth of one `B`-row root context.  For an unseparated root-scale
bank changing an `alpha` fraction of the roots, if `g` starts per changed
row are genuinely useful, this normalization is

\[
                              \alpha g\gamma
                                  \ge\delta_\theta.   \tag{1.4b}
\]

Thus fixed positive `alpha` and fixed `g` are not excluded.  Summing a
coherently useful construction over several depths multiplies both demand
and supply by the same weighted depth factor; it does not create an extra
factor `n`.

### 1.1 Positive-density rows alone are compatible with sparse edit

Suppose an `alpha` fraction of the `B` roots is changed, all nontrivial
components have size `b`, and the average rooted distance on those roots is
`d_bar`.  Then directly from the definition,

\[
                          \boxed{\Xi=b\alpha\bar d.}   \tag{1.5}
\]

Thus fixed `b`, fixed positive `alpha`, and bounded `d_bar` give
`Xi=O(1)=o(sqrt(s))`.  This passes both the extensive row-count test and
the sparse-edit variance test.  Existence of a dense switch-stable physical
atlas and a favourable signed carrier is a separate question.

In particular, the audited native-packet row-ball obstruction requires

\[
 \alpha\ge\delta_{\rm inv}-o(1),\qquad
 \delta_{\rm inv}={107897\over19784704}.              \tag{1.5a}
\]

A hypothetical disjoint elementary folded bank at exactly this row density
would use

\[
 R=\left({\delta_{\rm inv}\over2}+o(1)\right)B,
 \qquad
 \Xi=4\delta_{\rm inv}+o(1),                          \tag{1.5b}
\]

which is far below `sqrt(s)`.  This computation proves compatibility of
the two necessary scalar tests; it does not construct the bank.

### 1.2 The stronger active-width clause is incompatible

For one row, let `rho(P)` be the number of positions at which the deletion
and insertion halves of the two rooted words differ.  A product of `d`
transpositions fixes every symbol outside the union of the `2d` positions
touched by those transpositions.  Since adjacent transpositions are a
special case,

\[
                              d(P)\ge{\rho(P)\over2}.  \tag{1.6}
\]

Suppose `alpha B` roots obey `rho(P)>=eta s`.  Then

\[
 D_{\rm tot}\ge{\alpha\eta\over2}sB.                 \tag{1.7}
\]

If every edited component has at least `b` roots, then

\[
 \boxed{
 \Xi={1\over B}\sum_Kb_KD_K
       \ge {bD_{\rm tot}\over B}
       \ge {b\alpha\eta\over2}s.}                   \tag{1.8}
\]

For folded and clean banks this gives, respectively,
`Xi>=alpha eta s` and `Xi>=2 alpha eta s`.  Hence the stronger
positive-density, linearly-active carrier clause cannot coexist with
`Xi=o(sqrt(s))` in a bounded-component cycle bank.

## 2. Folded reciprocal `C_8`

Consider a reciprocal two-cut switch.  The old rows have residual pieces

\[
 L_A\mid M_A\mid R_A,
 \qquad L_B\mid M_B\mid R_B,
\]

and the new rows are

\[
 L_A\mid M_B\mid R_A,
 \qquad L_B\mid M_A\mid R_B.                         \tag{2.1}
\]

The complementary endpoints remain paired.  Every other rooted row is
identical and hence is an isolated inert component of the full overlay.
Each new row in (2.1) contains a physical state or colour formerly owned by
the other old row.  Together with the two diagonal port-token edges, these
cross-owner edges connect the four shore vertices.  Thus the unique
nontrivial full component has

\[
                              b_K=2.                  \tag{2.2}
\]

Suppose the exchanged trace blocks contain `k` Johnson exchanges.  At one
fixed root the old and new deletion orders agree outside a consecutive
`k`-position block, and the same holds for the insertion orders.  Equality
of the two boundary states implies equality of the sets of deleted
coordinates and of inserted coordinates inside the block.  Hence, writing
the two induced block permutations as `sigma^-` and `sigma^+`, one has the
exact formula

\[
 d(P)=\operatorname {inv}(\sigma^-)
             +\operatorname {inv}(\sigma^+)
       \le2\binom k2=k(k-1).                          \tag{2.3}
\]

Therefore one reciprocal `C_8` obeys

\[
 \boxed{
 \Xi_K={2\over B}\bigl(d(A)+d(B)\bigr)
          \le {4k(k-1)\over B}.}                     \tag{2.4}
\]

For row-disjoint reciprocal switches of widths `k_1,...,k_R`, the
components are disjoint and

\[
 \boxed{
 \Xi={2\over B}\sum_{j=1}^R
        \bigl(d_j(A)+d_j(B)\bigr)
       \le {4\over B}\sum_{j=1}^Rk_j(k_j-1).}        \tag{2.5}
\]

### 2.1 The elementary octahedral rectangle

In the octahedral normal form, the first affected row performs the two
exchanges

\[
                         b\mapsto c,\qquad a\mapsto d
\]

in the old factor and performs the same two exchanges in reverse order in
the new factor.  Thus its deletion order makes one adjacent transposition,
and its insertion order makes one adjacent transposition.  Its rooted
distance is exactly two.  The same is true on the second row.  Therefore

\[
                 D_K=4,qquad b_KD_K=8,qquad
                 \boxed{\Xi_K={8\over B}.}            \tag{2.6}
\]

For `R` row-disjoint rectangles,

\[
                 \boxed{\Xi={8R\over B}\le4},        \tag{2.7}
\]

because `2R<=B`.  On the other hand, (1.2) gives

\[
 {\mathscr A}_H\le 8R{\mathsf S}_H
        \le4B{\mathsf S}_H
        =O_A(B\sqrt s)=O_A(W/\sqrt s)=o_A(W).         \tag{2.8}
\]

This is the simplest exact example showing that positive changed-row
density and bounded `Xi` do not give `Omega(W)` endpoint motion.  It does
not rule out the correctly normalized parent demand (1.4a)--(1.4b).

### 2.2 The literal rank-three reciprocal `C_8`

For the reciprocal cycle in the rooted pentagon report, suppressing the
anchor gives the following old and new coordinate words:

\[
\begin{array}{c|c|c}
P&\omega_F(P)&\omega_G(P)\\ \hline
123&(2,3,1\mid6,4,5)&(3,2,1\mid6,5,4)\\
124&(4,2,1\mid6,5,3)&(2,4,1\mid6,3,5).
\end{array}                                           \tag{2.9}
\]

Each row again has one deletion inversion and one insertion inversion, so
`d(123)=d(124)=2`.  Hence this folded `C_8` also has (2.6).  A
right-concatenated bank with physically disjoint suffix tags retains these
distances and has `Xi=8R/B` exactly.

### 2.3 The actual canonical first-two-cut bank

The canonical Chung--Feller first two cuts contain exactly one octahedral
rectangle on each disjoint root pair

\[
                         1100R\longleftrightarrow1010R,
               \qquad R\in D_{s-2}.                  \tag{2.10}
\]

Thus this is an actual cube of `C_(s-2)` two-root full components, not a
hypothetical packing.  Equations (2.6)--(2.7) give

\[
\boxed{
 \Xi_{\rm can}=8{C_{s-2}\over C_s}
 = {2s(s+1)\over(2s-1)(2s-3)}
 \longrightarrow {1\over2}.}                         \tag{2.11}
\]

The exact active-root and first-boundary transfer fractions are

\[
 {2C_{s-2}\over C_s}\longrightarrow{1\over8},
 \qquad
 {C_{s-2}\over C_s}\longrightarrow{1\over16}.       \tag{2.12}
\]

Consequently the bank passes `Xi=o(sqrt(s))` and changes more than the
native row-ball constant (1.5a).  This does not make it an MWB repair: the
whole cube is the already audited first-two-cut rectangle family and obeys
its rooted exchange-matching and native-packet invariants.

There is also a sharp scalar supply comparison.  The parent plateau demand
per protected depth is `delta_theta C_s`, where
`1/4<=delta_theta<7/16`.  Even crediting every canonical rectangle with one
perfectly routed unit, one layer supplies only `C_(s-2)`, and hence

\[
 {C_{s-2}\over\delta_\theta C_s}
       ={1\over16\delta_\theta}+o(1).                \tag{2.13}
\]

This ranges from `1/4` at the bottom endpoint to `1/7` at the hard
endpoint.  Thus the known single layer is quantitatively insufficient,
but the failure is signed carrier supply, not sparse-edit rounding.

## 3. Clean four-strand `C_8` packets

A single clean coherent `C_8` cyclically permutes four terminal tails.
Its endpoint monodromy is a four-cycle.  It is therefore not an anchored
`D_s`-port factor, and neither `d(P)` nor `Xi` from the anchored sparse-edit
theorem may be assigned to it.  Formal serial multiplication of open twists
does not cure this issue inside fixed-exterior holes: the audited geodesic
obstruction rules out those holes before the sparse-edit theorem applies.

There is nevertheless a legitimate conditional object: an internal
zero-monodromy packet, for example four switch-stable clean `C_8` toggles on
the same four transported strands, in the same cyclic orientation, at
successively later phases.  Its monodromy is `tau^4=1`, so its final output
is again anchored.

Let `k` be the number of exchange positions in the phase slab from the
first changed incidence to the first state after the last changed
incidence.  Before this slab every final row is its old root prefix.  After
the fourth tail rotation every final row has recovered its old suffix.
Thus each of the four final coordinate words agrees with its old word
outside one consecutive `k`-position deletion block and the corresponding
insertion block.  As in (2.3),

\[
                              d(P)\le k(k-1).          \tag{3.1}
\]

The token segment strictly between the first and second switches is moved
from each old strand to the next new strand in the four-cycle.  The
diagonal port edges and these four cross-owner edges connect all four roots
in the full ownership overlay.  Hence a nondegenerate clean conveyor has

\[
                              b_K=4.                  \tag{3.2}
\]

Its exact moment and universal width bound are

\[
 \boxed{
 \Xi_K={4\over B}\sum_{P\in K}d(P)
          \le {16k(k-1)\over B}.}                    \tag{3.3}
\]

For `R` row-disjoint clean conveyors, with widths `k_j`,

\[
 \boxed{
 \Xi={4\over B}\sum_{j=1}^R\sum_{P\in K_j}d_j(P)
       \le {16\over B}\sum_{j=1}^Rk_j(k_j-1).}       \tag{3.4}
\]

In particular, a constant-width bank may cover a positive fraction of all
rows and still have `Xi=O(1)`.  It therefore passes the row-count and
sparse-variance tests.  Equation (0.2), now with `b=4`, says only that its
endpoint motion in the metric (0.1) is `O_A(B sqrt(s))`; whether that is
enough depends on the correctly normalized physical carrier demand.

## 4. Serial repetition

Suppose one fixed two-root folded bank is used serially `u` times, with
active widths `k_1,...,k_u`.  Adjacent-transposition distance is a metric,
so triangle inequality and (2.3) give

\[
 d(A)+d(B)\le2\sum_{j=1}^u k_j(k_j-1).                \tag{4.1}
\]

If some physical segment remains cross-owned in the final pair, the
nontrivial overlay component still has the same two roots.  If all
cross-owner tokens cancel, the overlay may split; this only lowers `Xi`,
and the following upper bound remains valid because every component is
contained in the same two-root set.
For `R` disjoint root pairs,

\[
 \Xi\le {4\over B}\sum_{i=1}^R\sum_{j=1}^u
                         k_{i,j}(k_{i,j}-1).           \tag{4.2}
\]

If the serial moves are elementary rectangles on disjoint phase pairs,
the affected adjacent inversions have disjoint supports and add exactly.
Then

\[
                         \boxed{\Xi={8uR\over B}.}    \tag{4.3}
\]

At maximal row packing `R=B/2`, this is `Xi=4u`.  Therefore

\[
 u=o(\sqrt s)\quad\Longrightarrow\quad \Xi=o(\sqrt s)
 \quad\Longrightarrow\quad {\mathscr A}_H=o(W),      \tag{4.4}
\]

whereas the additional hypothesis `mathscr A_H>=kappa W` forces

\[
                         u\ge {\kappa n\over4{\mathsf S}_H}
                          =\Omega_A(\sqrt s)           \tag{4.5}
\]

and then (4.3) has `Xi=Omega_A(sqrt(s))`.

For the canonical matching (2.10), a hypothetical `u`-layer serial atlas
which uses the same root pairs at `u` disjoint phase corridors would have

\[
 \boxed{
 \Xi_u=8u{C_{s-2}\over C_s}\longrightarrow {u\over2}.} \tag{4.5a}
\]

Its ideal one-depth scalar supply would be `uC_(s-2)`.  Therefore `u=4`
is the first count which can meet the bottom plateau
`delta_theta=1/4`, while `u=7` is the first count which can meet the hard
limit `delta_theta=7/16`.  Every fixed `4<=u<=7` still has
`Xi=O(1)=o(sqrt(s))`.  What is missing is the existence of these later
switch-stable same-pair layers and a common favourable physical sign.

If different root matchings are used in different layers, their union can
merge the two-root components.  Let `mathcal C` be the connected components
of the union owner graph, and let `u_P` count elementary phase rectangles
incident with root `P`.  For disjoint inversion supports, `d(P)=2u_P`, and
the exact moment is

\[
 \boxed{
 B\Xi=\sum_{C\in\mathcal C}|C|
                  \sum_{P\in C}2u_P.}                \tag{4.5b}
\]

Thus serial repetition is safe only when this edit-weighted component-size
moment is `o(B sqrt(s))`.  A fixed number of matchings may already form a
giant connected component, so layer count alone does not certify sparse
rounding.

For serial exact clean conveyors on one fixed four-root set, the overlay
size remains four and

\[
 \Xi\le {16\over B}\sum_j k_j(k_j-1)                 \tag{4.6}
\]

per root set.  Disjoint active phase slabs make the rowwise inversion
counts additive; overlapping repetitions can cancel, in which case both
the final edit distance and the final carrier action decrease.  Regardless
of cancellation, (0.2) shows that macroscopic action forces

\[
                         \Xi\ge
             {2\kappa n\over{\mathsf S}_H}
             =\left({4\kappa\over A}+o_A(1)\right)\sqrt s. \tag{4.7}
\]

Thus serial repetition never opens a gap between `Xi` and the particular
endpoint-action metric (0.1).  This is a conditional quantitative statement,
not a proof that every MWB carrier requires `kappa W` in that metric.

## 5. Exact boundary

The audit proves the following.

1. An elementary folded octahedral `C_8` has one two-root component and
   exact moment `8/B`; the literal rank-three reciprocal `C_8` has the same
   value.
2. A nondegenerate exact clean four-stage `C_8` conveyor has one four-root
   component and moment (3.3).
3. Disjoint banks add their moments exactly.  Serial banks obey the metric
   bounds (4.2), (4.6), with equality for disjoint elementary inversion
   supports.
4. Positive-density bounded-distance banks can have `Xi=O(1)` and are not
   ruled out by row count plus sparse variance alone.
5. Under either an independently proved `Omega(W)` endpoint-action demand,
   or the stronger positive-density linear-active-width clause, one obtains
   the quantitative obstructions (0.4), respectively (1.8).

What is not ruled out is a dense bounded-cycle atlas with a favourable
physical sign at the actual, weaker carrier normalization; nor is a
construction whose signed carrier effect uses a theorem not captured by
the endpoint metric (0.1).  The precise surviving lemma is therefore a
dense, switch-stable folded-`C_8` or exact clean-conveyor atlas with:

1. enough genuinely useful target moves to satisfy (1.4a) at every
   protected carrier;
2. full owner components satisfying
   
   \[
        \sum_C|C|\sum_{P\in C}d(P)=o(B\sqrt s);
   \]
3. one common favourable physical sign after all collars and target
   collisions.

The same-pair four-to-seven-layer rectangle packet suggested by
(4.5a) is the smallest concrete candidate.  The sparse-edit theorem would
round any such atlas at `o(W)` cost.
