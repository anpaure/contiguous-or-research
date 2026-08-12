# Stationary tiling restriction gives literal chains, spread tops, and an affine socket ledger

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional reduction theorem.  A single stationary marked
tiling law, independently restricted to the chains of any symmetric-chain
decomposition, simultaneously gives literal target-once fragmentation and
uniform random top names at every rank.  Its complete expected socket use
depends only on total work and the number of jobs, not on the individual
chain lengths.  Existence of a stationary law satisfying the tight
coefficient-one socket inequalities is not asserted here.

## 1. Canonical suffix chains

Fix a ground-set dimension `k` and a cutoff rank `t<ceil(k/2)`.  Restrict
any symmetric-chain decomposition of the Boolean lattice to the nonempty
lower ideal of ranks `1,...,t`.  Discard empty intersections.

The resulting chains are

\[
 C_a=(S_{a,b_a}\subset S_{a,b_a+1}\subset\cdots\subset S_{a,t}),
 \qquad 1\le a\le h,
\tag{1.1}
\]

where every inclusion raises rank by one.  They partition every nonempty
target of rank at most `t`, and every chain ends at rank `t`.  Put

\[
 L_a=t-b_a+1,
 \qquad
 h={k\choose t},
 \qquad
 \Lambda_t=\sum_{s=1}^t{k\choose s}=\sum_aL_a.
\tag{1.2}
\]

Thus these are literal realizations of the canonical suffix jobs; no
subsequent named-target matching is required.

## 2. Stationary marked tilings

A **stationary marked tiling** of `Z` is a translation-invariant random
partition of `Z` into finite consecutive intervals.  Every tile has a
mark `u` in a finite set `mathcal U` and an integer capacity `c(u)` at
least its length.  Assume all tile lengths are at most `D`.

For `u in mathcal U`, define

\[
 \beta_u=Pr\{0\hbox{ is the last point of a tile marked }u\},
 \qquad
 \theta_u=Pr\{\hbox{the tile containing }0\hbox{ is marked }u\}.
\tag{2.1}
\]

Then

\[
 \sum_u\theta_u=1,
 \qquad
 0\le\sum_u\beta_u\le1.
\tag{2.2}
\]

For a tail threshold `q`, write

\[
 \beta_{\ge q}=\sum_{u:c(u)\ge q}\beta_u,
 \qquad
 \theta_{\ge q}=\sum_{u:c(u)\ge q}\theta_u.
\tag{2.3}
\]

Independently for every Boolean chain `C_a`, sample one copy `Xi_a` of
this tiling on the **absolute rank line** `Z`.  Intersect its tiles with
the rank interval `[b_a,t]`.  Delete empty intersections and inherit the
mark of the parent tile on every surviving piece.

### Theorem 2.1 (literal restriction lift)

The resulting pieces have the following properties.

1. They partition every chain `C_a`, and hence every nonempty Boolean
   target of rank at most `t`, exactly once.
2. Every piece is a consecutive inclusion chain.
3. A piece inheriting mark `u` has length at most `c(u)`.

#### Proof

Intersections of a partition of `Z` with `[b_a,t]` partition that interval.
They are consecutive rank intervals, so (1.1) turns them into consecutive
inclusion chains.  Intersecting can only shorten a tile; its inherited
capacity therefore still dominates its length. `square`

This is the key quantifier change: the Boolean chains are chosen first,
and the complete physical fragment naming is performed afterward without
ever risking repeated lower targets.

## 3. Exact random top laws

For `s<t`, let `Q_(s,u)` be the rank-`s` targets which become the top of a
piece marked `u`.  Let `Q_(t,u)` be the terminal targets whose final piece
has mark `u`.

### Theorem 3.1 (post-hoc uniform top partition)

For every fixed `s<t`, the labelled families

\[
 \bigl(Q_{s,u}:u\in\mathcal U\bigr)
\tag{3.1}
\]

together with the no-top family form an iid categorical partition of the
complete rank-`s` layer, with cell probabilities `(beta_u)` and
`1-sum_u beta_u`.

At the terminal rank `t`, the families `(Q_(t,u))` form an iid categorical
partition with cell probabilities `(theta_u)`.

Conditional on their cell sizes, both are uniform labelled partitions of
the corresponding complete rank layer.

#### Proof

Every rank-`s` target lies on exactly one chain, and distinct targets at
one rank lie on distinct chains.  Their tilings are therefore independent.
For `s<t`, the target is a piece top of type `u` exactly when `s` is the
last integer of a tile of type `u`, an event of probability `beta_u` by
stationarity.  At `s=t`, the forced terminal piece inherits the mark of
the tile containing `t`, whose law is `(theta_u)`.  These laws do not
depend on the chain bottom because the tilings were placed on absolute
ranks.  Exchangeability of iid categorical labels gives the conditional
uniformity. `square`

The partitions at two different ranks need not be independent: their
labels may come from the same chain tiling.  Thus the multi-rank Bernstein
argument must not be imported by conditioning on all rank counts.
Nevertheless the independent objects are the **whole chains**, and the
geometric decay of the normalized containment weights gives the same
vanishing-reserve exponent as independent ranks.

### Theorem 3.2 (whole-chain Bernstein spread)

Let a mark `v` request a collar start of rank `v`, and put

\[
 p_{s,v}=\begin{cases}
 \beta_v,&s<t,\\
 \theta_v,&s=t.
 \end{cases}
 \qquad
 d_{s,v}={k-s\choose v-s}.
\tag{3.2}
\]

Assume `v<=ceil(k/2)` and only ranks `s<=t<v` are assigned to `v`.  Put

\[
 m_v^{\rm exp}=\sum_s p_{s,v}{k\choose s}
 =\beta_v(\Lambda_t-h)+\theta_vh
\tag{3.3}
\]

and let

\[
 \Delta_v=H_v-m_v^{\rm exp},
 \qquad
 d_v=d_{t,v}={k-t\choose v-t}.
\tag{3.4}
\]

For every `T in binom([k],v)`,

\[
 \Pr\left\{
 \sum_s{|Q_{s,v}\cap\binom Ts|\over d_{s,v}}
 >{H_v\over{k\choose v}}
 \right\}
 \le
 \boxed{
 \exp\left(-{\Delta_v^2d_v\over8{k\choose v}H_v}\right)}.
\tag{3.5}
\]

Consequently there is an absolute `A_0` such that all pointwise
top-to-collar Hall inequalities hold simultaneously whenever every
`Delta_v>0` and

\[
 \boxed{
 {\Delta_v^2d_v\over {k\choose v}H_v}\ge A_0k.}
\tag{3.6}
\]

#### Proof

Fix `(v,T)`.  For Boolean chain `a`, let `Y_a` be its complete contribution
to the left side of (3.5): sum `1/d_(s,v)` over its marked-`v` piece tops
which lie in `T`.  The variables `(Y_a)` are independent because the
chain tilings are independent.

Write `w_s=1/d_(s,v)`.  A direct binomial ratio gives

\[
 {w_{s-1}\over w_s}
 ={v-s+1\over k-s+1}
 \le {v\over k}\le {2\over3}
\tag{3.7}
\]

for every relevant `k>=3`; the remaining finite cases are immediate.
Therefore

\[
 0\le Y_a\le\sum_{s\le t}w_s\le {3\over d_v}.
\tag{3.8}
\]

Let `Y=sum_aY_a`.  The flag identity

\[
 {{v\choose s}\over {k-s\choose v-s}}
 ={{k\choose s}\over{k\choose v}}
\tag{3.9}
\]

and Theorem 3.1 give

\[
 \mu:=\mathbb EY={m_v^{\rm exp}\over{k\choose v}}.
\tag{3.10}
\]

Since `0<=Y_a<=3/d_v`,

\[
 \sum_a\operatorname {Var}(Y_a)
 \le\sum_a\mathbb EY_a^2
 \le {3\mu\over d_v}.
\tag{3.11}
\]

Put `g=Delta_v/binom(k,v)`.  Bernstein's inequality yields

\[
 \Pr\{Y-\mu>g\}
 \le
 \exp\left(-{g^2\over6\mu/d_v+2g/d_v}\right).
\tag{3.12}
\]

Both `mu` and `g` are at most `H_v/binom(k,v)`, so the exponent in
(3.12) is at least the exponent in (3.5).  Union-bound over the
`exp(O(k))` pairs `(v,T)` and use (3.6).  The exact pointwise codegree
theorem then gives every collar matching. `square`

Thus the cross-rank dependence costs only an absolute constant.  The
vanishing-reserve criterion is exactly the same, up to constants, as in
the independent-rank spread theorem.

No coloured Boolean matching, persistent-colour oracle, or prescribed-top
extension theorem is needed: target-once extension was built into the
fixed symmetric chains before the random top labels were exposed.

## 4. Exact affine socket ledger

Let `N_(a,u)` be the number of marked-`u` pieces produced on chain `a`.

### Theorem 4.1 (one-chain expectation)

For a chain of length `L`,

\[
 \boxed{\mathbb E N_u(L)=(L-1)\beta_u+\theta_u.}
\tag{4.1}
\]

Consequently the aggregate expected use is

\[
 \boxed{
 \mathbb E\sum_aN_{a,u}
   =(\Lambda_t-h)\beta_u+h\theta_u.}
\tag{4.2}
\]

For capacity tails,

\[
 \boxed{
 \mathbb E\sum_{a,u:c(u)\ge q}N_{a,u}
   =(\Lambda_t-h)\beta_{\ge q}+h\theta_{\ge q}.}
\tag{4.3}
\]

#### Proof

A restricted tiling of an interval of length `L` has one fragment top at
each of its `L-1` internal ranks which is a tile boundary, plus its forced
terminal top.  The corresponding type probabilities are `beta_u` and
`theta_u`.  Linearity gives (4.1).  Sum it and use (1.2) to obtain
(4.2); summing over marks above a threshold gives (4.3). `square`

Thus the entire anonymous fragmentation ledger has forgotten the
individual job lengths.  It depends on the Boolean lower ideal only through
the two scalars `Lambda_t-h` and `h`.

## 5. Tile-intensity form

Let `x_(ell,u)` denote the stationary intensity per integer site of tiles
of length `ell` and mark `u`.  Then

\[
 x_{\ell,u}\ge0,
 \qquad
 \sum_{\ell,u}\ell x_{\ell,u}=1,
 \qquad
 x_{\ell,u}=0\quad(\ell>c(u)),
\tag{5.1}
\]

and

\[
 \beta_u=\sum_\ell x_{\ell,u},
 \qquad
 \theta_u=\sum_\ell\ell x_{\ell,u}.
\tag{5.2}
\]

Conversely, every rational nonnegative array satisfying (5.1) has a
stationary periodic realization: take an integer multiple of each tile
type prescribed by the array, concatenate the resulting tiles in any
order around a cycle, and choose a uniform cyclic shift.  Irrational arrays
are weak limits of rational ones.

Substitution into (4.2) gives the exact type load

\[
 \boxed{
 M_u^{\rm exp}
 =\sum_{\ell\le c(u)}
   \bigl(\Lambda_t-h+h\ell\bigr)x_{\ell,u}.}
\tag{5.3}

Hence a stationary post-hoc construction with expected socket reserves is
equivalent to the finite linear system

\[
 \begin{aligned}
 &x_{\ell,u}\ge0,
 &&x_{\ell,u}=0\quad(\ell>c(u)),\\
 &\sum_{\ell,u}\ell x_{\ell,u}=1,
 &&\sum_{u:c(u)\ge q}\sum_\ell
   (\Lambda_t-h+h\ell)x_{\ell,u}
   \le K_q-\Delta_q
   \quad(1\le q\le D),
 \end{aligned}
\tag{5.4}
\]

where `K_q` is the number of physical sockets of capacity at least `q` and
`Delta_q` is the desired tail reserve.

This is a polynomial-size ordinary linear program with no whole-job
configuration variables.  Its only nontrivial geometry is the distinction
between boundary intensity and coverage intensity in (5.2).

## 6. Concentration and exact integral packing

Assume (5.4) with positive reserves.  For each threshold `q`, the total
number `Z_q` of produced pieces requiring capacity at least `q` is a sum
of independent chain contributions.  Each contribution lies in
`[0,L_a]`.  Hoeffding gives

\[
 \Pr\{Z_q-\mathbb EZ_q\ge\Delta_q\}
 \le
 \exp\left(-{2\Delta_q^2\over\sum_aL_a^2}\right).
\tag{6.1}
\]

Since `L_a<=t=O(k)` and `sum_aL_a=Lambda_t`,

\[
 \sum_aL_a^2\le t\Lambda_t.
\tag{6.2}
\]

In the Gaussian collar regime the available adjacent-depth margins are
exponential in `k` divided by a polynomial, whereas `t` is polynomial.
Whenever the chosen `Delta_q` has that scale, the exponent in (6.1) is
itself exponential in `k`.  Thus a union over all capacity thresholds is
harmless.  Separately, Theorem 3.2 controls all exponentially many owner
tests.  No independence between the two success events is required: the
sum of their failure probabilities is below one.

On a successful outcome, every tail inequality `Z_q<=K_q` holds.  Sorting
pieces and sockets by capacity gives an integral injection.  The literal
Boolean fragments and their top names were already fixed, so no further
target assignment or coloured rounding remains.

### Conditional Corollary 6.1 (stationary-clock lower lift)

If the coefficient-one socket tails admit (5.4), the capacity-tail
reserves make (6.1) summable, and the classwise pointwise gaps satisfy
(3.6), then the complete strict-lower ideal has a literal target-once
interval-chain lift into the collar sockets, with all pointwise
top-to-collar Hall inequalities simultaneously valid.

## 7. Zero-slack obstruction to inherited tile marks

The stationary restriction construction is not a shortcut around the
critical zero-trimming theorem.

### Proposition 7.1 (endpoint clipping is forbidden at zero slack)

Suppose the total capacity of the physical socket multiset equals the
total lower-target work.  In any successful restriction outcome, every
used piece must fill its assigned socket exactly.  Consequently, if a
restricted chain endpoint lies strictly inside its parent tile, the
inherited-mark construction cannot be successful.

In particular, every successful zero-slack outcome of an independently
restricted translation-stationary law must happen to align the sampled
tile boundaries with both endpoints of every job.

#### Proof

The sum of piece lengths is the total target work.  Every assigned socket
has capacity at least its piece length.  If total available capacity equals
work, summing these inequalities forces every available positive socket to
be used and every individual inequality to be equality.

If a chain endpoint clips a parent tile, its intersection is strictly
shorter than that tile, while the inherited capacity is at least the parent
tile length.  This gives strict unused capacity, a contradiction.

This proves the asserted necessary alignment. `square`

Thus the high-probability concentration proof in Section 6 is naturally a
slackful tool.  At zero slack, if the stationary law has boundary
probability less than one, the expected number of clipped job endpoints is
positive and typically exponential; Section 6 cannot certify their total
absence.  This does not rule out an exponentially rare globally aligned
outcome.  It shows only that the present concentration argument cannot use
such a rare event while simultaneously retaining its socket and spread
estimates.  A robust critical-coefficient proof needs an endpoint-aware
renewal or configuration law which assigns a clipped first piece a
genuinely smaller socket.  That is exactly the all-price
fragmentation/coagulation gate; it has not been bypassed.

## 8. Exact remaining boundary

This theorem does not prove that (5.4) is feasible at the coefficient-one
socket vector.  It proves that this is the only anonymous lower-side
question left in the stationary post-hoc route.

It also does not construct the central owner chronology, arbitrary-width
upper deck, or residence carrier.  Those remain the upper/carrier half of
the all-dimensional problem.

The gain is exact:

\[
 \boxed{
 \text{stationary marked tiling with reserve}
 \Longrightarrow
 \text{literal target-once lower chains + spread top names}.}
\]

Thus the previously separate persistent-colour matching and prescribed-top
extension gates collapse to the finite linear system (5.4).

## 9. Dependencies

1. `MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`;
2. `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`;
3. the existence of symmetric-chain decompositions of Boolean lattices.
