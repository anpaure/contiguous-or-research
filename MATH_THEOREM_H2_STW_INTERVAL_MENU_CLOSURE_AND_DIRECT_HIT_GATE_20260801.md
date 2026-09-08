# STW interval menus: terminal-tail routing, dynamic cuts, and the pivot-ray gate

Date: 2026-08-01  
Status: unconditional Boolean closure bounds, an exact conditional
`O(d^2)` direct-hit theorem, a deterministic STW terminal-tail routing
reserve, a simultaneous STW block-discrepancy refinement, and an exact
scope theorem for the pivot-rich two-ray packet.  No `O(d^2)` or `O(1)`
triangular factor is claimed.

## 0. Verdict

Let

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad
 d=\min\left\{q:qW+\binom{q+1}{2}\ge|\mathcal L|\right\},
\]

where `mathcal L` is the nonempty strict lower Boolean half.  Start from a
complete chain partition with the triangular address capacities, as in
`MATH_THEOREM_TRIANGULAR_CHAIN_SINGLE_HOLE_ROUTING_AND_INTERVAL_CUT_20260801.md`.

The new single-hole actuator and the component-ceiling obstruction fit
together exactly as follows.

1. A nonaccepting coloured route closure containing a gap of dimension `g`
   must expose at least `binom(g,floor(g/2))` distinct nonoverloaded
   addresses: use one middle layer of the interval, since a chain contains
   at most one target of a fixed rank.  Hence the Boolean interval theorem
   excludes every bounded blossom: a closure reachable from the large gap
   of an underloaded owner has at least

   \[
               \binom{\lceil r/d\rceil}
                     {\lfloor\lceil r/d\rceil/2\rfloor}
               =2^{\Theta(\sqrt{k})}
   \]

   addresses.
2. The actual STW geometry supplies more than randomness.  Every initially
   underloaded STW address has a direct target in an overloaded terminal
   tail.  A source-indexed Boolean reserve and Erdos's chain theorem keep
   this true for

   \[
      \Delta_N=2^N-1-S_{d-1}(N)
       =2^{k/2-O(\sqrt{k\log k})}
   \]

   consecutive direct rotations.  This is an unconditional regeneration
   theorem, but the published STW overload is exponentially larger than
   `Delta_N`, so it does not give a polynomial leave.
3. The STW random chunks can simultaneously be chosen to meet every
   sufficiently dense Boolean interval slice in the expected order of
   magnitude.  Equal-rank injection turns this into many distinct final
   addresses.  The later arbitrary Dilworth and attachment choices still
   give no overload-colour mixing for those addresses beyond the terminal
   reserve above.
4. The pivot-rich geodesic packet closes local owner, lower-`q1`, residence,
   OR-transport, and two-ray compiler rows.  It does not close the coloured
   routing row: each nested ray is compatible with a single address colour,
   and every internal ray deletion exposes a Boolean sibling absent from the
   packet.  Four parity sibling chains are the exact constant-address return
   augmentation, conditional on physical cells and overloaded displaced
   targets.
5. There is an exact weakest one-step theorem.  Greedy direct
   hits stop exactly when the targets in overloaded addresses avoid every
   insertion menu of every underloaded address.  If the remaining
   overload-side interval-avoidance core always has size at most
   `R`, then the final overload is at most `R`.  Taking
   `R=binom(d+1,2)` yields a static `O(d^2)` leave.

Thus the live theorem is not another Ferrers or fractional Hall row.  Past
the explicit terminal reserve it is a robust union-expansion/hitting
statement for the **final address map**, or a square-complete physical
return bank which regenerates the packet's missing Boolean siblings.

## 1. Dynamic component-ceiling cut

Let `C=(C_a)` be a complete chain system.  Write `alpha(X)=a` when target
`X` belongs to `C_a`, and let

\[
                         \mathcal O=\{a:|C_a|>c(a)\}
\]

be the overloaded addresses.  Every address outside `mathcal O` has load
at most `d`, including all boundary addresses.

For a gap `g=(P,Q)`, put

\[
                         I(g)=\{X\in\mathcal L:P\subsetneq X\subsetneq Q\}.
                                                               \tag{1.1}
\]

Consider a reachable, nonaccepting coloured state `(g,F)` in the exact state
graph of the single-hole theorem.  Thus every address in `F` is
nonoverloaded: the start is underloaded, and reaching an overloaded address
would have accepted rather than adding it to `F`.

Define the new-address frontier

\[
 N(g,F)=\{\alpha(X):X\in I(g),\ \alpha(X)\notin F\}.             \tag{1.2}
\]

### Theorem 1.1 (address expansion of a nonaccepting state)

If `(g,F)` has no accepting transition, then every address in `N(g,F)` is
nonoverloaded and

\[
 |N(g,F)|
 \ge
 \left\lceil\frac{(|I(g)|-d|F|)_+}{d}\right\rceil.              \tag{1.3}
\]

For an initial state, the owner of `g` contributes no target strictly
inside its own ordinary gap, so the sharper bound is

\[
                         |N(g,\{a_0\})|
                         \ge\left\lceil\frac{|I(g)|}{d}\right\rceil.
                                                               \tag{1.4}
\]

#### Proof

An address outside `F` containing a fitting target would be an accepting
transition if it were overloaded.  Hence all addresses in (1.2) are
nonoverloaded and contain at most `d` targets each.  The used addresses in
`F` contain at most `d|F|` targets in total.  Counting the remaining targets
of `I(g)` proves (1.3).

For an ordinary gap, its endpoints are consecutive in `C_(a_0)`, so no
member of that chain fits strictly between them.  This removes the
`d|F|` term at an initial state and proves (1.4).  \(\square\)

### Theorem 1.2 (middle-layer address injection)

If `g=|Q-P|>=2`, the middle layer

\[
 L(g)=\{P\cup Z: Z\subseteq Q-P,\ |Z|=\lfloor g/2\rfloor\}     \tag{1.5}
\]

contains

\[
                         \binom g{\lfloor g/2\rfloor}          \tag{1.6}
\]

targets in pairwise-distinct chain addresses.  For an initial gap these
addresses are all external to its owner.  At a general nonaccepting state,
at most `|F|` of them lie in used addresses, so there are at least

\[
             \binom g{\lfloor g/2\rfloor}-|F|         \tag{1.7a}
\]

distinct nonoverloaded successor addresses outside `F`.

#### Proof

All members of (1.5) have the same rank, while an inclusion chain contains
at most one member of any rank.  Hence their current addresses are distinct.
No target of the chain owning an ordinary gap lies strictly in that gap.
At most one middle-layer target can lie in each address of `F`.  Finally,
an overloaded external address would be an accepting transition.
\(\square\)

### Corollary 1.3 (no bounded Boolean blossom)

Every nonaccepting closure reachable from an underloaded anchored address
contains at least

\[
 \binom{g_0}{\lfloor g_0/2\rfloor},
 \qquad g_0=\left\lceil\frac rd\right\rceil                    \tag{1.7}
\]

distinct nonoverloaded successor addresses.

Indeed, choose the gap supplied by the exponential interval-menu theorem
and apply Theorem 1.2.

This is the exact dynamic counterpart of the component-ceiling cut in
`MATH_THEOREM_H2_TRIANGULAR_CHAIN_RANK_ROUNDING_ABSORBER_AND_GENERIC_GK_NOGO_20260801.md`.
In the generic obstruction, a comparability component cannot send a chain
atom outside itself.  Here a route closure can be proper only if all its
interval targets remain assigned to its own nonoverloaded address colours.
Equations (1.3) and (1.7) are the corresponding capacity ceilings.  Boolean
intervals force this dynamic component to be exponentially large, but `W` is
exponential in `k`, so size alone does not make the closure global.

There is a literal Hall shadow of this state closure.  Form a bipartite
graph with underloaded addresses on the left and overloaded addresses on
the right, joining `a` to `b` when some target of `C_b` fits some ordinary
gap of `C_a`.  A matching in this graph gives commuting address-disjoint
length-one rotations.  Its exact one-unit obstruction is

\[
             \max_{X\subseteq U}\bigl(|X|-|N_{\mathcal O}(X)|\bigr).     \tag{1.8}
\]

This is the typed Hall form of the component ceiling: only overloaded
neighbours pay debt.  Cloning an address for all of its slack or excess
units is only a relaxation, because successive insertions split its gaps
and successive deletions must keep a common chain order.  Those
configuration constraints are precisely what the used-address coordinate
`F` records; the full coloured state closure is the sequential
rainbow/blossom refinement of (1.8).

## 2. Exact one-step reduction to `O(d^2)`

Put

\[
 \mathcal G_U(C)=
   \bigcup_{a:\,|C_a|<c(a)}\ \bigcup_{g\text{ gap of }C_a}I(g),
 \qquad
 \mathcal H(C)=\bigcup_{b\in\mathcal O}C_b.                    \tag{2.1}
\]

### Lemma 2.1 (exact direct-hit cut)

If

\[
                         \mathcal G_U(C)\cap\mathcal H(C)\ne\varnothing,
                                                               \tag{2.2}
\]

then `C` has a balancing route of length one; conversely every length-one
balancing route gives such an intersection.

#### Proof

Take `X` in the intersection.  It fits a gap of an underloaded
address and is held by an overloaded address.  Those addresses are
different.  Moving `X` directly into the gap is Theorem 3.1 of the
single-hole note with `t=1`.  The converse reads the moved target from a
length-one route.  \(\square\)

### Theorem 2.2 (interval-avoidance-core criterion)

Run greedy length-one rotations until none remains.  At any terminal state,

\[
 \mathcal H(C)\cap\mathcal G_U(C)=\varnothing,
 \qquad
 \Phi(C)\le |\mathcal H(C)|
             =|\mathcal H(C)-\mathcal G_U(C)|.                  \tag{2.3}
\]

Consequently, if every direct-hit-terminal state reachable from the initial
system satisfies

\[
                         |\mathcal H(C)-\mathcal G_U(C)|\le R,  \tag{2.4}
\]

then deleting only the remaining overload gives a triangular static packing
with deficiency at most `R`.

In particular, (2.4) with

\[
                         R=B_\triangle:=\binom{d+1}{2}=O(d^2)  \tag{2.5}
\]

is sufficient for the requested one-step `O(d^2)` cover-down.

#### Proof

Greedy descent terminates because every direct hit lowers `Phi` by one.
At a terminal state Lemma 2.1 gives the first equality in (2.3).  For each
overloaded chain, its excess is at most its total load, so
`Phi<=|mathcal H|`; disjointness gives the second equality.  Apply (2.4),
then truncate the remaining overloaded chains.  \(\square\)

The interval-avoidance core in (2.4), rather than raw menu size, is the exact
Boolean object to bound.  The quantifier over reachable terminal states is
load-bearing: insertions split gaps and terminal deletions change overload
colours.

### Lemma 2.3 (an anchored large gap exists above triangular slack)

Let `sigma=sum_a c(a)-|mathcal L|>=0`.  Total underload equals
`Phi+sigma`.  Boundary addresses contribute at most `B_triangle` underload
units.  Hence every state with `Phi>B_triangle` has an underloaded anchored
address, and that address has a gap of dimension at least
`g_0=ceil(r/d)`.

#### Proof

The identity follows by summing `c(a)-|C_a|` over all addresses and
separating positive and negative parts.  If all anchored addresses were
full, total underload would be at most the sum of boundary capacities,
namely `B_triangle`, contradicting `Phi+sigma>=Phi>B_triangle`.  The gap
bound is Theorem 5.2 of the single-hole note.  \(\square\)

There is also a proof-safe resilience formulation for the direct-hit
schedule.  Let `rho_0` be the minimum, over all Boolean intervals of
dimension at least `g_0`, of the number of middle-layer targets whose
**initial** addresses are overloaded.  After `h` length-one balancing
rotations, every such interval retains at least

\[
                         \rho_0-h                              \tag{2.6}
\]

active overloaded middle-layer targets.  In a direct-hit schedule an
overloaded address only loses targets and never receives one; the
underloaded recipient never becomes overloaded.  One rotation changes one
currently overloaded address, and a fixed-rank interval layer has at most
one target in that chain.  Thus it destroys at most one active hit in the
layer.  Therefore

\[
 \rho_0\ge\Phi_0-B_\triangle                                  \tag{2.7}
\]

guarantees direct-hit descent to `Phi<=B_triangle`: after fewer than
`Phi_0-B_triangle` rotations, the large interval from Lemma 2.3 still has
an active overloaded middle-layer target.  This is a rigorous preservation
law for length-one routes, but (2.7) is far stronger than a one-hit initial
margin.  For routes of length at most `L`, the safe loss bound is
`rho_0-h(L+1)`: moved intermediate targets and terminal-address deactivation
must both be charged.

## 3. What ideal random address mixing would give

The following benchmark separates the desired probability statement from
what STW actually prove.  Fix an address map and a family of gap menus.  Let
`mathcal O` be a uniformly random `q`-subset of the `W` anchored address
colours, independent of the menu-address incidence.  If a fixed menu meets
`L` distinct address colours, then

\[
 \Pr(\mathcal O\text{ misses the menu})
 =\frac{\binom{W-L}{q}}{\binom Wq}
 \le \exp(-qL/W).                                  \tag{3.1}
\]

Consequently a fixed family of `G` menus is hit everywhere with positive
probability whenever

\[
                         qL/W>\log G.               \tag{3.2}
\]

For the initial largest gaps, Theorem 1.2 gives the deterministic benchmark

\[
                         L\ge w_0:=
                         \binom{g_0}{\lfloor g_0/2\rfloor}.     \tag{3.3}
\]

Even under the artificial independent-colour model, a union bound over at
most `W` selected menus therefore needs roughly

\[
 q\gtrsim
 \frac{W\log W}{w_0}
 =W\,2^{-\Theta(\sqrt{k})}\operatorname{poly}(k).              \tag{3.4}
\]

This is still exponentially larger than `O(d^2)`.  Thus an "every menu is
hit" theorem is much stronger than necessary and, by itself, cannot explain
the final polynomial leave.

For one direct hit, let `R_U` be the union of all address colours met by
`mathcal G_U(C)`.  The same ideal model gives

\[
                   \Pr(\mathcal O\cap R_U=\varnothing)
                   \le e^{-q|R_U|/W}.                          \tag{3.5}
\]

This identifies the potentially useful statement: prove large **union**
expansion of all underloaded menus, rather than hitting every menu
separately.  Neither (3.3) nor the STW length theorem controls `|R_U|`,
because the large menus may overlap in their address colours.

Equations (3.1)--(3.5) are a benchmark only.  In a real chain partition an
address is overloaded precisely because of its selected chain length, so
the overload colours are not independent of the address map.

## 4. A deterministic STW terminal-tail reserve

This section uses the notation of the STW construction, with ambient
dimension `n` (equal to `k` elsewhere in this note).  Put

\[
 m=\left\lceil\frac n2\right\rceil,
 \qquad M=\binom nm,
 \qquad K=\left\lceil\frac{2^{n-1}}M\right\rceil,
 \qquad
 C_0=\left\lceil\sqrt{n\log n/3}\right\rceil.       \tag{4.1}
\]

STW first construct a core upper-half partition `D`, then put every set of
rank at least `m+C_0` into the leftover set `L`.  Their final partition
`D*` attaches every leftover chain only to a core chain whose maximum is in
the terminal level `A_K`.  A terminal core has `K+1` members.

After complementation and the parity-specific owner deletion, a terminal
core contributes `K+1` strict-lower targets in odd dimension and `K` in
even dimension.  In both parities the triangular depth satisfies `d<=K`.
Consequently a terminal address containing even one still-unmoved nonempty
strict-lower leftover target is overloaded.

Put

\[
 N=n-m-C_0-1,
 \qquad
 S_j(N)=\text{the sum of the }j\text{ largest coefficients of }(1+x)^N,
                                                               \tag{4.2}
\]

and

\[
             \Delta_N=2^N-1-S_{d-1}(N).              \tag{4.3}
\]

### Theorem 4.1 (terminal-tail direct routing)

For all sufficiently large `n`, the complemented STW chain system, with
the triangular boundary addresses initially empty, admits at least

\[
                         \min\{\Phi_0,\Delta_N\}       \tag{4.4}
\]

consecutive length-one balancing rotations.  Hence the resulting static
overload obeys

\[
                         \Phi_{\rm out}
             \le (\Phi_0-\Delta_N)_+.                 \tag{4.5}
\]

This schedule fills one underloaded source in a consecutive batch before
moving to the next source.

#### Proof

First consider an untouched underloaded anchored source.  In the original
upper-half orientation let `Y` be the maximum of its STW core.  An
underloaded source cannot be terminal, and the construction gives
`|Y|<=m+C_0`.  Choose

\[
 B_Y\subseteq[n]-Y,
 \qquad |B_Y|=m+C_0+1-|Y|,
 \qquad V_Y=[n]-(Y\cup B_Y),                          \tag{4.6}
\]

so `|V_Y|=N`.  For every proper subset `R` of `V_Y`, put

\[
 Z_R=Y\cup B_Y\cup R,
 \qquad X_R=Z_R^c=V_Y-R.                              \tag{4.7}
\]

The set `Z_R` has rank at least `m+C_0+1`, so STW put it in `L`.
The target `X_R` is nonempty, is a strict-lower target, and lies strictly
below `Y^c`, the minimum of the complemented source chain.  It therefore
fits the bottom gap of that source.  In `D*`, `Z_R` belongs to a leftover
tail attached to a terminal core.  While `X_R` is unmoved, its terminal
address has its full base load plus this target and is overloaded.

After `t` earlier direct rotations, at most `t` members of the
`2^N-1`-element bank (4.7) are unavailable.  If the present source has
remaining deficit `u<=d`, put `v=min(u,Phi_t)`.  Erdos's theorem on
families with no `v`-chain shows that a `v`-chain remains whenever

\[
 t<2^N-1-S_{v-1}(N)\ge\Delta_N.                      \tag{4.8}
\]

An increasing chain of `Z_R` gives a decreasing chain of complements
`X_R`.  Insert those complements successively into the source's bottom gap,
largest first.  Before each deletion, the donor terminal address is still
overloaded: the target being deleted itself supplies a surplus unit, even
if earlier targets on the same tail were removed.  This fills `v` source
slots by `v` length-one balancing rotations, except that when `v<u` the
overload has reached zero and the proof stops.

For a boundary address, use the same construction with `Y=emptyset` and
fill the empty boundary chain by a decreasing complement chain.  Boundary
addresses can be processed first.  A terminal donor never becomes
underloaded, while every nonfinal nonterminal source is processed in one
batch and then is full.  Thus at every later step with positive overload an
untouched underloaded source of one of these two kinds is available.  Induction up to
(4.4) proves the theorem. \(\square\)

### Corollary 4.2 (size and limitation of the reserve)

More sharply,

\[
 d=(\sqrt{\pi/8}+o(1))\sqrt n,
 \qquad N=(1/2+o(1))n.                                \tag{4.9a}
\]

Thus `d/sqrt(N)` tends to `sqrt(pi)/2`.  The local central limit theorem
gives

\[
       \Delta_N=\Theta(2^N)
          =2^{n/2-O(\sqrt{n\log n})}.                \tag{4.9}
\]

Writing `Phi_N` for the standard normal cdf, the `d-1` largest levels have
limiting Gaussian mass `2 Phi_N(sqrt(pi)/2)-1<1`, so they occupy a fixed fraction strictly below one
of `2^N`; this proves the first equality.  This is an exponential
shortest-rotation horizon, but it is not enough for `O(d^2)`: the STW core
has length at most `K+1`, while all extra overload is charged to the
leftover mass, giving only

\[
       \Phi_0\le O(M)+|\mathscr L_{\rm tail}|
          \le O(M)+2^n n^{-3/16+o(1)}
          =2^{n-o(n)},                               \tag{4.10}
\]

and the published leftover estimate is exponentially larger than (4.9).
The theorem is therefore a genuine improvement of the actuator, not a
coefficient-changing bound on the known leave.

The banks (4.7) are source-indexed but need not be disjoint.  The proof
uses only the global fact that `t` rotations make at most `t` targets
unavailable; it makes no independence assertion.

## 5. What the STW chunk randomness does prove

Although it does not randomize final overload colours, the within-level
randomness has a useful simultaneous interval consequence.

### Theorem 5.1 (whole-block Boolean discrepancy)

There is a realization satisfying all STW good events with the following
additional property.  Let `B=X_(a,b)` be a whole, unshattered STW block
contained in one level `A_t`, and let

\[
                     F=[P,Q]^\circ\cap A_t,
 \qquad
                     \mu={|B||F|\over |A_t|}.          \tag{5.1}
\]

If

\[
                     \mu\ge16(n\log3+2\log n),        \tag{5.2}
\]

then simultaneously for every such pair

\[
                     |B\cap F|\ge\mu/2.               \tag{5.3}
\]

#### Proof

The marginal law of a fixed whole block inside `A_t` is a uniformly chosen
fixed-size subset.  The hypergeometric lower-tail inequality gives

\[
             \Pr(|B\cap F|<\mu/2)\le e^{-\mu/8}.      \tag{5.4}
\]

There are at most `n^2` blocks and at most `3^n` Boolean intervals.  Under
(5.2), the union of the bad events in (5.4) has probability strictly below
one, even after adding the failure probabilities in STW Lemmas 2 and 3.
Hence one common realization has all the stated properties. \(\square\)

All members of `B cap F` have the same rank.  No inclusion chain can contain
two of them, so after **any** later choice of the Dilworth chains and tail
attachments they occupy `|B cap F|` distinct final addresses.  Thus there
is an exact dichotomy: either one is already on an overloaded address, or
(5.3) supplies that many distinct nonoverloaded address colours.  This is
address breadth, not overload mixing.

The high-order missing row can be stated using Greene--Kleitman notation.
If a block poset `K_a` has height `r_a`, and a chain partition attains the
`(r_a-1)`-norm `alpha_(r_a-1)(K_a)`, then its number of full `r_a`-chains is

\[
                     |K_a|-\alpha_{r_a-1}(K_a).       \tag{5.5}
\]

STW control the width `alpha_1(K_a)`, not the interval-local quantity in
(5.5), nor do they choose their Dilworth partition to optimize it.  An
interval-local high-order saturation theorem is one exact way to continue
after the reserve (4.3) is exhausted.

## 6. Source audit of the remaining STW probability space

The published construction of Sudakov--Tomon--Wagner has the following
exact order of quantifiers.

1. The sets above the first `K+1` upper-half levels are ordered by rank; only
   sets of the same rank receive a random order.  Fixed-size consecutive
   chunks `X_(a,b)` are then cut from these orders.
2. For fixed `a`, whole chunks lying in distinct ranks are uniform
   fixed-size subsets and are independent.  This is the independence used
   by the container and Chernoff arguments.
3. After Lemmas 2 and 3, the proof says that **there is a choice** of all
   chunks with the required antichain and defect-matching bounds and fixes
   it.
4. For each resulting `K_a`, an arbitrary Dilworth chain decomposition
   `C_a` is selected.  Existence matchings `M_a` are selected to build the
   central partition `D_0` and attach compatible tail chains.
5. The leftover high sets are partitioned by another family of complete
   matchings, and those tail chains are attached to obtain `D*`.

Only the chunk membership is randomized.  The source proves aggregate
maximum-antichain, matching-defect, leftover-mass, and final chain-length
bounds.  It neither samples nor counts the admissible Dilworth
decompositions/matchings, and it states no marginal, negative-association,
codegree, or interval-hitting law for the final map

\[
                         X\longmapsto\text{the chain/address of }X.       \tag{6.1}
\]

In particular, overload is determined only after those existential choices
and the final tail attachment.  It is not a uniform random address colour
independent of (6.1).  Therefore the ideal-colour estimates (3.1)--(3.5),
or a robust interval-local overload law beyond Theorem 4.1, cannot be
imported from the STW theorem as a black box.

This is a scope no-go, not a proof that a suitably randomized STW
refinement cannot work.  Such a refinement must specify distributions on
the Dilworth decompositions, defect matchings and leftover-chain
attachments, then prove interval/address mixing conditional on all earlier
choices.

Primary source: B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain
decompositions and applications*, Random Structures & Algorithms 60
(2022), 261--286, especially Sections 2.3, 2.6 and 2.7.

## 7. Shortest rotations do not retain local expansion automatically

### Proposition 7.1 (Boolean-diamond collapse)

Let `X` be an internal member of a chain whose predecessor has rank
`|X|-1` and whose successor has rank `|X|+1`.  Write

\[
 P=X-\{x\},\qquad Q=X\cup\{y\}.
\]

Then the deletion interval `(P,Q)` contains exactly two targets:

\[
                         X,
                         \qquad X'=(X-\{x\})\cup\{y\}.          \tag{7.1}
\]

After `X` is moved into the preceding hole, `X'` is the only possible new
target which can fill its deletion gap.  Thus this branch has at most one
new continuation before the address-colour test.

#### Proof

The difference `Q-P` is the two-element set `{x,y}`.  Its nonempty proper
subsets give precisely the two intermediate sets in (7.1).  One is the
target just moved; only the other can come from a new address.  \(\square\)

The STW central partition `D_0` is built by matchings between consecutive
levels `A_(i-1)` and `A_i`.  Hence every internal central target satisfies
Proposition 7.1.  A first gap can expose
`2^{Theta(sqrt(k))}` targets and addresses, but every branch entering such
a central target can immediately become a forced sibling walk.  The STW
paper gives no noncoalescence or overload-hitting theorem for this family of
walks.  Theorem 4.1 bypasses this local collapse by jumping directly from a
terminal leftover tail into the source bottom gap.  After that reserve is
exhausted, local expansion is still not preserved by shortest rotations as
a formal consequence of `D*`.

## 8. The pivot-rich packet and the coloured-hole automaton

Use the notation of
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`.
For packet depth `h`, put

\[
\begin{aligned}
 P_0&=S_0=Q,\\
 P_i&=Q\cup\{\lambda_{h-i+1},\ldots,\lambda_h\},\\
 S_i&=Q\cup\{\rho_1,\ldots,\rho_i\},
                         &&1\le i<h,\\
 P_h&=Q\cup L,\qquad S_h=Q\cup R.                    \tag{8.1}
\end{aligned}
\]

The frozen packet proves that these two rays, the singleton `X`, and the
collared rank-`r` geodesic have literal OR transport, local lower-compiler
closure, residence on the nonclipped coordinates, distinct immediate
palettes, and fixed-`H` lower-`q1` planting.  None of those statements
assigns the targets in (8.1) to colours in the **current lower-chain
partition**.

### Proposition 8.1 (two-ray address collapse)

The packet hypotheses imply no address expansion beyond two colours for
the non-singleton side bank.  Each family `(P_i)` and `(S_i)` is itself an
inclusion chain and is therefore compatible with one chain address.  The
two families are cross-incomparable, so two addresses are both sufficient
and, when both rays are nonempty, necessary for this local target set.

Consequently the `2h-2` physical ray cells are not `2h-2` certified donor
colours in the hole automaton.  Old-OR transport controls witness cells;
the geodesic collar and protected-factor theorem control rank-`r` owners
and lower-`q1` edge colours.  None controls the map `alpha(P_i),alpha(S_i)`
or makes either colour overloaded. \(\square\)

There is an exact constant-address augmentation.  Define the square
siblings

\[
\begin{aligned}
 \widehat P_i
   &=Q\cup\{\lambda_{h-i}\}
        \cup\{\lambda_{h-i+2},\ldots,\lambda_h\},\\
 \widehat S_i
   &=Q\cup\{\rho_1,\ldots,\rho_{i-1},\rho_{i+1}\},
                         &&1\le i<h.                  \tag{8.2}
\end{aligned}
\]

For `2<=i<h`, the natural ray deletion gap has dimension two and contains
exactly the displaced target and its sibling:

\[
 (P_{i-1},P_{i+1})\cap\mathcal L=\{P_i,\widehat P_i\},
 \qquad
 (S_{i-1},S_{i+1})\cap\mathcal L=\{S_i,\widehat S_i\}.          \tag{8.3}
\]

For `i=1`, the displayed sibling fits when `P_1` (respectively `S_1`) is
bottom-anchored, or more generally when its actual predecessor is contained
in the sibling.  An arbitrary exterior predecessor need not have this
property.  No sibling in (8.2) is a singleton or a member of either packet
ray.  Thus every internal ray branch reaches an uncertified target
immediately; the packet is a first-step fan, not a closed absorber.

### Theorem 8.2 (four-chain square-complete return bank)

Within each shore,

\[
 \widehat P_i\subset\widehat P_j,
 \quad
 \widehat S_i\subset\widehat S_j
                         \qquad(j\ge i+2),             \tag{8.4}
\]

while consecutive indices are incomparable.  Cross-shore siblings are
incomparable.  Hence for `h>=3` the sibling poset has chain-cover number
exactly four: odd and even indices on each shore.  (For `h=2` it has two.)

Suppose these four parity chains are realized in four addresses whose
formal endpoint gaps are chosen so that

\[
 P_i\text{ fits }g(\widehat P_i),
 \qquad
 S_i\text{ fits }g(\widehat S_i).                     \tag{8.5}
\]

Four distinct unused boundary addresses with formal bottom `emptyset`,
formal top `[k]`, and adequate capacities give an order-theoretic
realization of (8.5), with capacity demands

\[
 \left\lceil{h-1\over2}\right\rceil,
 \left\lceil{h-1\over2}\right\rceil,
 \left\lfloor{h-1\over2}\right\rfloor,
 \left\lfloor{h-1\over2}\right\rfloor.               \tag{8.6}
\]

For `h<=d`, the capacities `1,...,d` contain such four slots once `d>=4`,
but their use displaces any triangular chains already assigned there.  If a
ray-slot hole `P_i` is at an underloaded address `a`, its
sibling is at a distinct return address `b`, and the displaced `P_i` is at
an overloaded third address `c`, then

\[
             a\xleftarrow{\widehat P_i}b
              \xleftarrow{P_i}c                       \tag{8.7}
\]

is an address-distinct balancing route of length two.  The same holds on
the `S` shore.

#### Proof

Formula (8.4) is a direct comparison of the suffix/prefix sets; consecutive
siblings exchange rather than contain one another.  This proves the chain
cover statement.  In (8.7), the first fit is (8.3), with formal-bottom
anchoring at the first slot, and the second fit is (8.5).  The three
addresses are distinct and the terminal is overloaded, so Theorem 3.1 of the single-hole
note applies. \(\square\)

The condition (8.5) is not part of the frozen packet.  It consumes four
literal chain addresses, cells and common-cap rows, and its boundary use
must be reconciled with the triangular boundary bank.  More importantly,
it closes canonical **ray-slot** holes only; it does not normalize an
arbitrary STW bottom gap into that form.

At the sharp triangular depth `h=d`, the mismatch with Theorem 4.1 is
quantitative.  Packet ray targets have ranks

\[
                         r-d+1,\ldots,r-1,             \tag{8.8}
\]

whereas every terminal-reserve target (4.7) has rank at most

\[
                         N=n-m-C_0-1<r-d               \tag{8.9}
\]

for all sufficiently large `n`.  Such a target can be the packet singleton
after choosing `Q superseteq X` of size `r-d` (the required collar room is
eventually available), but cannot be one of its two rays.  Therefore the
packet creates at most one new side cell for a direct terminal-tail transfer
supplied by Theorem 4.1.  Transported background cells may already witness
other low targets, but are not packet-created transfer cells.  The fixed-`H`
planting theorem handles a bounded selected bank, not the exponential STW
leave, and does not contract task birth by itself.

## 9. Proof-safe frontier

The component/blossom analysis has therefore improved to

\[
\boxed{
\begin{array}{c}
\text{bounded nonaccepting closures: excluded;}\\
\text{initial address frontier }2^{\Theta(\sqrt{k})}:\text{ proved;}\\
\text{STW terminal-tail direct horizon }\Delta_N:\text{ proved;}\\
\text{STW block-to-address discrepancy: proved;}\\
\text{shortest-route expansion after the reserve: open;}\\
\text{pivot packet plus four return chains: ray-slot closure only;}\\
\text{robust union direct hit down to }O(d^2):\text{ sufficient, open.}
\end{array}}
\]

The smallest positive next theorem is one of the following.

* A union-expansion bound for the selected largest gaps of all underloaded
  chains, together with a distributional overload-hitting theorem for a
  newly randomized `D*` selection.
* An interval-local high-order saturation theorem for the whole STW blocks,
  converting Theorem 5.1's address breadth into overload-colour supply.
* A noncoalescence/endpoint theorem for the forced Boolean-sibling walks,
  or a matching-closed physical realization of the four-chain return bank
  in Theorem 8.2 for a normal form broad enough to include STW bottom gaps.
* An address-regenerating rechoice of the STW matchings after each bounded
  batch of rotations.

Any one must be stable under the state changes in (2.3).  Static interval
size, the finite pivot rays, and the existing STW length concentration alone
do not prove it.
