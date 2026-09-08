# A fixed-endpoint block palette has an exact fractional perfect matching

**Status (2026-08-21).**  The statements below are proved.  They resolve the
fractional-capacity and endpoint-balancing questions for the localized
tail-MTF palette.  They do **not** round the fractional matching to one
integral path per block.  That rounding problem still contains the full
cross-block, cross-rank covering difficulty.

## 1. Parameters and legal blocks

Let

\[
 n=2m+1,\qquad W=\binom n m=\binom n{m+1},
\]

and put

\[
 H=\left\lceil\sqrt{n\log n}\right\rceil,
 \qquad
 K=\{m-H,\ldots,m+1+H\}.
\]

Use the natural DCC floor and its eligible-pool size:

\[
 f=m+H+2,
 \qquad d=n-f+1=m-H,
 \qquad R=n^3+f^2.                                      \tag{1.1}
\]

For all sufficiently large `n`, every `k in K` satisfies

\[
 d\le k<f.                                               \tag{1.2}
\]

A recency state is a permutation of `[n]`.  At each step one may move any
position in `{f,...,n}` to the front; there are `d` choices.  Write `C_k(pi)`
for the set in the first `k` positions of state `pi`.  Every legal access
word has equal-letter gap at least `f`, so its rank-`k` state observations
are clean word windows for every `k in K`.

We use the exact bridge fact that every ordered pair of states is connected
by a legal word of exactly `R` steps.  Fix arbitrary skeleton states

\[
 \gamma_1,\ldots,\gamma_s,\qquad \gamma_{s+1}=\gamma_1.
\]

A palette option in slot `i` will have the form

\[
 \gamma_i
 \xrightarrow[\text{exactly }R]{\text{entry bridge}}
 \rho
 \xrightarrow[\text{free core}]{a_i\text{ steps}}
 \eta
 \xrightarrow[\text{exactly }R]{\text{exit bridge}}
 \gamma_{i+1}.                                           \tag{1.3}
\]

The seed state `rho` and every choice in the free core are part of the
palette option.  The bridge observations are ignored in the matching
ledger.  Their only role is to make every option have the prescribed
endpoints and common physical length `a_i+2R`.

Take

\[
 A=\lfloor e^{n/5}\rfloor                               \tag{1.4}
\]

and partition `W` as

\[
 W=a_1+\cdots+a_s,
 \qquad 1\le a_i\le A,
 \qquad s=\lceil W/A\rceil,                              \tag{1.5}
\]

with all but possibly the last `a_i` equal to `A`.  Then

\[
 \sum_i(a_i+2R)=W+2sR=(1+o(1))W,                         \tag{1.6}
\]

because `R/A=o(1)`.  Thus the second bridge repairs endpoint balancing at
asymptotically zero cost.  It is not legitimate to average over `rho` in a
one-bridge block whose free core is required to start at the fixed state
`gamma_i`; (1.3) is the explicit repair of that hidden endpoint error.

## 2. Band-simple cores exist

A core of length `b` is **band-simple** if, for every `k in K`, its `b`
post-move sets `C_k` are pairwise distinct.

### Lemma 2.1 (history-free return bound)

Run the free core by choosing uniformly among its `d` eligible positions.
Fix `1<=k<f` (in particular, any `k in K`).  For any history through time
`u`, any history-measurable `k`-set `S`, and any `g>=1`,

\[
 \Pr(C_k(\pi_{u+g})=S\mid\mathcal F_u)
 \le
 \prod_{r=1}^{\min(g,k)}\frac{\min(r,d)}d.                \tag{2.1}
\]

If `C_k(pi_u)=S`, `k<f`, and `g<f`, the return probability is zero.

#### Proof

For `g<=k`, no letter initially in positions `1,...,k-g` can be selected:
before move `t` its position is at most `k-g+t-1<=k-1<f`.  The `g` selected
letters are distinct because `g<f`.  Thus the endpoint target fixes their
`g`-set.  Exposing the successive picks, the unused part of that set has
sizes `g,g-1,...,1`; at each pick the eligible pool has size `d`, so
multiplication gives (2.1).  If `g>k`, condition on the history through time
`u+g-k`.  The last `k` picks are distinct because `k<f`, and their set is
exactly `C_k(pi_(u+g))`; the same argument supplies the `k` factors in
(2.1).

For the return assertion, extend the legal history backward if necessary
(or use the preceding exact entry bridge).  Since `k<f`, `C_k(pi_t)` is the
set of the last `k` access occurrences, so the two equal sets are occurrence
intervals.  If `g>=k`, the intervals are disjoint.  Matching equal letters
between them, the sum of the `k` forward recurrence distances is `kg`; as
every such distance is at least `f`, this forces `g>=f`.  If `g<k`, cancel
the `k-g` overlapping occurrences.  The `g` exiting occurrences must match
the `g` entering occurrences; the sum of their forward recurrence distances
is `gk`, which is at least `gf`, forcing `k>=f`.  Both contradict `g<f` and
`k<f`.  \(\square\)

### Lemma 2.2 (nonempty symmetric simple-core palette)

Choose the seed `rho` uniformly from `S_n`, and choose the free-core
generators independently and uniformly from `{f,...,n}`.  For every
`1<=b<=A`, the probability that the core is band-simple is `1-o(1)`,
uniformly in `b`.  In particular, the band-simple palette is nonempty.

Conditional on band-simplicity, its law is invariant under every relabeling
of `[n]`.  Consequently, for every `k in K` and every `S in binom([n],k)`,

\[
 \Pr\{S\text{ occurs in the core}\mid\text{band-simple}\}
 =\frac b{\binom nk}.                                    \tag{2.2}
\]

#### Proof

Put `B_d=d!/d^d`.  If two rank-`k` observations coincide at a gap below
`f`, Lemma 2.1 gives probability zero.  At a gap at least `f`, (1.2) and
(2.1) give the bound `B_d`.  Hence a union bound gives

\[
 \Pr\{\text{some collision in the band}\}
 \le |K|\binom b2 B_d.                                   \tag{2.3}
\]

Stirling's upper bound gives

\[
 B_d\le 3\sqrt d\,e^{-d}.
\]

Here `d=(n-1)/2-H`, `|K|=O(sqrt(n log n))`, and
`b<=exp(n/5)`.  Therefore the right side of (2.3) is

\[
 \exp\{-n/10+o(n)\}=o(1).                               \tag{2.4}
\]

Relabeling the seed and every state along a core preserves its generator
positions and band-simplicity.  The conditional law is therefore
`S_n`-invariant.  On the conditioning event there are exactly `b` distinct
rank-`k` targets.  Transitivity on `binom([n],k)` and summing their equal
appearance probabilities gives (2.2).  \(\square\)

## 3. The augmented palette hypergraph

For each `k in K`, put `M_k=binom(n,k)` and introduce a dummy set
`D_k` of size

\[
 |D_k|=W-M_k.                                            \tag{3.1}
\]

This is nonnegative because the two middle layers are largest.  The
rank-`k` part is

\[
 V_k=\binom{[n]}k\ \dot\cup\ D_k,
 \qquad |V_k|=W.                                         \tag{3.2}
\]

There is also one vertex `z_i` for each block slot.  We regard path-labelled
parallel edges as distinct (equivalently, use the simple quotient and add
their weights).  An augmented palette edge in slot `i` consists of:

1. `z_i`;
2. one legal sandwich path (1.3) whose `a_i`-step core is band-simple; and
3. exactly `a_i` vertices from every `V_k`, obtained by claiming some of
   the actually observed core targets and filling the remaining positions
   with distinct dummy vertices.

An unclaimed observation is simply ignored.  Thus an integral perfect
matching would select one legal path per slot and would claim every real
band target exactly once; hence every real target would occur in the
concatenated legal trajectory.  The bridge observations, totaling `o(W)`,
are outside this incidence ledger and can only add coverage.

### Theorem 3.1 (exact fractional perfect matching)

For all sufficiently large odd `n`, the augmented fixed-endpoint palette
hypergraph above has a fractional perfect matching: there are nonnegative
edge weights for which every slot vertex, every real target vertex, and
every dummy vertex has total incident weight exactly one.

#### Proof

It is enough to give, independently for each slot, a probability law on its
augmented palette edges and verify that the sum of the resulting vertex
marginals over all slots is one.

In slot `i`, choose the seed and free core according to Lemma 2.2,
conditioned on band-simplicity.  For a fixed rank `k`, write

\[
 D=W-M_k,
 \qquad \theta_i=\frac{a_iD}{W}.
\]

Choose an integer `h_{i,k}` supported on
`{floor(theta_i),ceil(theta_i)}` with mean `theta_i`.  (When `theta_i` is
an integer, take it deterministically.)  Since `a_i<=W`, one has

\[
 0\le h_{i,k}\le\min(a_i,D).                             \tag{3.3}
\]

Uniformly choose `h_{i,k}` of the `D` dummy vertices, and uniformly choose
`a_i-h_{i,k}` of the `a_i` distinct observed rank-`k` core targets.  Make
these augmentation choices independently across ranks, conditional on the
core.  This defines a distribution on genuine palette edges, each meeting
`V_k` in exactly `a_i` vertices.

Every edge in the slot contains `z_i`, so its marginal is one.  Fix a real
target `S in binom([n],k)`.  By (2.2), followed by the uniform claiming
choice,

\[
\begin{aligned}
 \Pr_i(S\text{ is claimed})
 &=\frac{a_i}{M_k}
   \mathbb E\!\left[\frac{a_i-h_{i,k}}{a_i}\right]\\
 &=\frac{a_i}{M_k}\left(1-\frac{W-M_k}{W}\right)
 =\frac{a_i}{W}.                                        \tag{3.4}
\end{aligned}
\]

If `y in D_k`, then

\[
 \Pr_i(y\text{ is used})
 =\frac{\mathbb E h_{i,k}}D
 =\frac{a_i}{W},                                        \tag{3.5}
\]

with the assertion vacuous when `D=0`.  Summing (3.4) and (3.5) over
slots and using `sum_i a_i=W` gives marginal one for every vertex of every
rank part.  The slotwise edge probabilities are therefore the desired
fractional-perfect-matching weights.  \(\square\)

## 4. A budget-normalized fractional near-factor

The preceding exact fractional perfect matching uses physical length
`W+o(W)`.  There is a second normalization in which the entire physical
trajectory, including both bridges in every block, has length at most `W`.
It gives an asymptotically perfect fractional matching without a remainder
block.

Set

\[
 a=\lfloor e^{n/5}\rfloor,
 \qquad
 s=\left\lfloor\frac{W}{a+2R}\right\rfloor,
 \qquad
 N=sa,
 \qquad q=|K|=2H+2.                                    \tag{4.1}
\]

Use `s` copies of the anchor-to-seed, free-core, core-terminal-to-anchor sandwich
(1.3), now with one common anchor and core length `a`.  Their total physical
length is

\[
 L=s(a+2R)\le W.                                        \tag{4.2}
\]

### Lemma 4.1 (the lost core volume is negligible)

One has

\[
 W-N=o(W),\qquad q(W-N)=o(W).                            \tag{4.3}
\]

Moreover, for all sufficiently large `n`,

\[
 \binom nk<N\quad(k\in K\setminus\{m,m+1\}),
 \qquad
 \binom nm=\binom n{m+1}=W>N.                           \tag{4.4}
\]

#### Proof

The floor in (4.1) gives `0<=W-L<a+2R`, and hence

\[
 0<W-N=(W-L)+2sR
 <a+2R+\frac{2RW}{a+2R}.                                \tag{4.5}
\]

Now `R=O(n^3)`, `a=exp(n/5+o(1))`, and
`W=exp((log 2)n+o(n))`.  Dividing (4.5) by `W`, even after multiplication
by `q=exp(o(n))`, tends to zero.  This proves (4.3).

By unimodality and symmetry of the binomial coefficients, the largest
nonmiddle layer is rank `m-1` or `m+2`, and

\[
 \frac{\binom n{m-1}}W=\frac{\binom n{m+2}}W
 =\frac{m}{m+2}=1-\frac2{m+2}.                          \tag{4.6}
\]

Equation (4.5) in fact gives `1-N/W=o(1/n)`, so (4.6) is below `N/W`
for all sufficiently large `n`.  The middle equality is the definition of
`W`, and `N<L<=W` because `R>0`.  \(\square\)

For an outer rank `k`, put

\[
 M_k=\binom nk,\qquad D_k=N-M_k>0,                       \tag{4.7}
\]

and augment its real targets by `D_k` dummies, making a part of size `N`.
Choose integers `h_{i,k}` such that

\[
 0\le h_{i,k}\le\min(a,D_k),
 \qquad \sum_{i=1}^s h_{i,k}=D_k.                       \tag{4.8}
\]

Such quotas always exist: distribute `D_k` as evenly as possible among `s`
bins of capacity `a`.  Put `r_{i,k}=a-h_{i,k}`.  Thus

\[
 \sum_i r_{i,k}=sa-D_k=M_k.                             \tag{4.9}
\]

In an edge from slot `i`, uniformly claim `r_{i,k}` of its `a` distinct
observed rank-`k` targets and uniformly use `h_{i,k}` of the dummy labels.
At each middle rank there are no dummies in this normalization and the edge
claims all `a` distinct observed targets.

### Theorem 4.2 (exact outer factor and uniform middle deficit)

Give every slot the uniform-seed, uniform-generator core law conditioned on
band-simplicity, together with the decorations just described.  The
resulting edge weights form a fractional matching with the following exact
degrees:

\[
 \deg(z_i)=1,                                            \tag{4.10}
\]

\[
 \deg(S)=1\quad\text{for every outer real target and every outer dummy},
                                                               \tag{4.11}
\]

and

\[
 \deg(S)=\frac NW=1-o(1)
 \quad\text{for every rank-`m` or rank-`m+1` target}.    \tag{4.12}
\]

Thus the total fractional real-target deficit over the entire band is
exactly

\[
 2(W-N)=o(W).                                            \tag{4.13}
\]

#### Proof

The slot assertion is immediate.  At an outer rank, (2.2) and the uniform
quota choice give, for a real target `S` and dummy `y`,

\[
 \sum_i\Pr_i(S\text{ is claimed})
 =\sum_i\frac a{M_k}\frac{r_{i,k}}a
 =\frac{\sum_i r_{i,k}}{M_k}=1,                         \tag{4.14}
\]

\[
 \sum_i\Pr_i(y\text{ is used})
 =\sum_i\frac{h_{i,k}}{D_k}=1.                          \tag{4.15}
\]

At a middle rank, a given target appears with probability `a/W` in each
slot and is always claimed when it appears, so its degree is `sa/W=N/W`.
Only the two middle ranks are unsaturated by Lemma 4.1, proving (4.13).
Every displayed degree is at most one, so these weights are indeed a
fractional matching.  \(\square\)

Theorem 4.2 is a fractional **near-factor**, not an integral DCC.  An
integral matching with the same saturated outer parts and with only `o(W)`
additional losses would select one path per slot and would yield the desired
DCC (the word is already a closed legal trajectory of length at most `W`).
Theorem 4.2 does not supply that rounding.

## 5. The hidden central-capacity obstruction

The conditioning in Theorem 3.1 is essential rather than cosmetic.

### Proposition 5.1 (zero central dummy capacity forces simple support)

Consider any fractional perfect matching in a block-palette model with
core lengths `a_i` satisfying `sum_i a_i=W`, where an edge in slot `i`
may claim only targets actually observed in that core and meets a rank part
in at most `a_i` distinct vertices.  At rank `m` (and likewise at rank
`m+1`), every positive-weight edge in slot `i` must claim exactly `a_i`
distinct real targets.  In particular, its core trace at that rank must be
collision-free, and no observation there can be ignored.

#### Proof

There are exactly `W` real vertices and no dummies at either middle rank.
The sum of their required degrees is `W`.  On the other hand, the slot
constraints and the per-edge bound give total middle-rank incidence at most

\[
 \sum_i a_i=W.
\]

Equality of all vertex degrees forces equality in every nonnegative
slotwise deficiency.  Thus every edge of positive weight has middle-rank
incidence `a_i`, which is possible only when all `a_i` observations are
distinct and all are claimed.  \(\square\)

For example, the unconditioned uniform-core distribution is not a
fractional perfect matching when `a_i>=f+1`: the positive-probability core
word `T_f^{f+1}` has the same state, and hence the same middle-rank target,
at core times `1` and `f+1`.  Proposition 5.1 rules out assigning positive
weight to it.  Dummies cannot absorb this repeat because
`W-M_m=W-M_{m+1}=0`.

There is also a raw cardinality constraint.  With equal core length `a`,
rank parts of size exactly `W` can have a perfect matching selecting one
edge from each of `s` slots only if `sa=W`.  If divisibility fails, the
remainder block in (1.5) gives an exact model.  Merely taking
`s=floor(W/a)` leaves `W-sa` central vertices uncovered; taking `sa>W`
requires either a rank part of size `sa` with `sa-W` additional central
dummies or an explicit declaration of which observations are outside the
matching ledger.

## 6. Consequence and remaining gate

The exact bridge theorem therefore yields more than a large palette: after
the two-sided endpoint repair, the natural augmented palette has **no
fractional Hall/capacity obstruction at all**.  The fractional solution is
exact, is simultaneous over the entire growing DCC band, respects one unit
of mass per block slot, and balances all skeleton endpoints exactly.

This does not imply an integral or almost-integral matching.  Independent
sampling from the fractional solution gives each target mean load one and
therefore has the usual constant coupon-vacancy scale.  The hyperedges have
growing size `1+a_i|K|`, their rank traces are nested and dynamically
correlated, and no bounded-uniformity matching theorem applies merely from
the existence of the fractional solution.  The remaining theorem is a
rounding theorem exploiting the particular tail-MTF palette well enough to
select one edge per slot while losing only `o(W)` real vertices.  Proving
that would give the required coefficient-one DCC, because the physical
connector overhead is already `o(W)` by (1.6).
