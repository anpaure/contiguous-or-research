# Colored Boolean one-step flow: exact contraction and the rounding gap

**Date:** 2026-08-05  
**Method:** pure mathematics plus a proof-scope audit of standard dependent
rounding theorems; no computation, search, or solver  
**Status:** unconditional exact one-step fractional theorem and an exact
error-contraction calculation.  A positive maximum-entropy perfect-
matching law realizes all these edge marginals exactly, but it cannot be
Strong Rayleigh in edge coordinates: a conditional dummy `K_(2,2)` face
has positive edge correlation.  Conditional on a Boolean-specific full-
marginal Chernoff rounding theorem, the spread-top theorem extends through
all `O(D)` chain levels and the vanishing reserve pays the error.  Standard
bipartite dependent rounding does not supply that statement; the strongest
general arbitrary-linear-statistic theorem loses a multiplicative fraction
of the matching.

## 0. The augmented Boolean interface

Let `n=2r` and `q<r`.  Put

\[
 \mathcal B_q=\binom{[n]}q,
 \qquad
 \mathcal B_{q+1}=\binom{[n]}{q+1},
 \qquad
 h_{q+1}=C_{q+1}-C_q.
\tag{0.1}
\]

Make a square bipartite graph `J_q`.

* Its right shore is `mathcal B_(q+1)`.
* Its left shore contains every `S in mathcal B_q`, adjacent to its
  rank-`q+1` supersets.
* It also contains `h_(q+1)` labelled start dummies, each adjacent to every
  right vertex.

An integral perfect matching in `J_q` is exactly one Boolean inclusion
matching from the complete rank-`q` layer into rank `q+1`, together with
the complementary bank of new chain starts.  Iterating these interfaces is
a complete SCD-style path cover.  Fragmenting the resulting paths later
does not change the underlying inclusion edges.

Give the old vertices and start dummies colours.  A colour records one
**whole canonical-job configuration**: its chain-bottom type, every future
fragment boundary, and the collar-socket rank assigned to every fragment.
It persists along the underlying unfragmented Boolean path.  At a rank
where one of its fragments ends, that colour contributes to the
corresponding chunk-top test.  Thus no arbitrary recolouring of an already
named path is being assumed.  Boundary-deleted or unmarked paths receive a
background colour.  There are only `exp(o(r))` configuration roles in the
depth-`D=Theta(sqrt(r))` application.

## 1. Exact uniform fractional perfect matching

### Theorem 1.1 (uniform coloured one-step flow)

The following weights form a fractional perfect matching of `J_q`:

\[
 x_{S,T}={1\over n-q}
 \quad(S\subset T, |S|=q),
 \qquad
 x_{d,T}={1\over C_{q+1}}
 \quad(d\text{ a start dummy}).
\tag{1.1}
\]

Fix a future test set `U in mathcal B_v`, where `q+1<=v<=r`.  If a colour
`a` occupies `m_a` old rank-`q` vertices and

\[
 Z_{a,q}(U)=
 |\{S\in\mathcal B_q:S\text{ has colour }a, S\subset U\}|,
\tag{1.2}
\]

then the fractional expected number of colour-`a` old images contained in
`U` is exactly

\[
 {v-q\over n-q}Z_{a,q}(U).
\tag{1.3}
\]

If `h_a` start dummies have colour `a`, their expected contribution inside
`U` is

\[
                         h_a{\binom v{q+1}\over C_{q+1}}.
\tag{1.4}
\]

#### Proof

Every old left vertex has `n-q` neighbours, and every dummy has
`C_(q+1)` neighbours, so all left loads are one.  A right vertex receives

\[
 {q+1\over n-q}+{h_{q+1}\over C_{q+1}}
 ={C_q\over C_{q+1}}+1-{C_q\over C_{q+1}}=1.
\]

Thus (1.1) is a fractional perfect matching.

For fixed `S subset U`, exactly `v-q` of the `n-q` one-element extensions
of `S` remain inside `U`, proving (1.3).  Every dummy is uniform on the
right shore, and `U` contains `binom(v,q+1)` right vertices, proving (1.4).
`square`

## 2. Spread errors contract rather than accumulate

The uniform benchmark for the old colour inside `U` is

\[
                         \overline Z_{a,q}(U)
 =m_a{\binom vq\over C_q}.
\tag{2.1}
\]

The binomial identities give

\[
 {v-q\over n-q}\overline Z_{a,q}(U)
 =m_a{\binom v{q+1}\over C_{q+1}}.
\tag{2.2}
\]

Hence an old-colour deviation

\[
                         e_{a,q}(U)
 =Z_{a,q}(U)-\overline Z_{a,q}(U)
\tag{2.3}
\]

is carried fractionally to

\[
                         {v-q\over n-q}e_{a,q}(U).
\tag{2.4}
\]

Since `v<=r` and `n=2r`,

\[
                         0\le {v-q\over n-q}\le {1\over2}.
\tag{2.5}
\]

Thus each Boolean step contracts all future-owner subset-count errors by
at least a factor two before the new rounding error is added.

### Conditional Corollary 2.1 (a Chernoff one-step oracle closes extension)

Assume that every fractional matching (1.1), with any colouring of its
left vertices, admits a random integral perfect matching which

1. preserves every edge marginal in (1.1); and
2. gives the usual Chernoff--Bernstein upper tail for every nonnegative
   linear statistic of the selected edges.

Then a bottom-up coloured path cover through any `L<=D+1` consecutive
Boolean ranks can be chosen so that all eventual chunk-top normalized
codegrees satisfy the spread inequalities of Theorem 1.1 in
`MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`,
provided its reserve constants are enlarged by one absolute factor.

#### Proof

Encode the entire fragmentation configuration, including every eventual
top rank and socket rank, in the persistent colours.  At step `q`, for
every future owner test `U` and every needed aggregate of colours, use
the corresponding edge indicator sum as one linear statistic.  There are
only `exp(O(r))` tests over all steps.

The assumed Chernoff bound gives the same one-step exponent as independent
top sampling:

\[
 \Omega\left({\Delta_u^2d_{\min}(u)\over C_uH_u}\right).
\tag{2.6}
\]

The variable reserve theorem makes this at least a sufficiently large
constant times `r`, so a union bound controls every new rounding error.
By (2.5), errors inherited from earlier interfaces form a geometric series
of ratio at most `1/2`.  Their total is at most twice the largest one-step
allowance.  Enlarging the absolute reserve constant pays this factor.

The integral perfect matchings concatenate to pairwise target-disjoint
inclusion paths.  Cutting them at the prescribed coloured boundaries gives
the requested interval chains and their spread literal tops.  `square`

This calculation is important: `D` interfaces do not require `D` times the
spread reserve.  Boolean containment contracts the relevant error.

## 3. Why standard exact dependent rounding is not the missing oracle

Ordinary bipartite integrality rounds (1.1) to some perfect matching but
does not control any of the exponentially many future-owner statistics.

There does exist a full-support perfect-matching Gibbs distribution having
edge marginals exactly (1.1).  This follows from finite exponential-family
duality: (1.1) is a strictly positive point in the relative interior of the
bipartite perfect-matching polytope, and the mean map of the edge-weighted
perfect-matching exponential family is onto that relative interior.

However, Strong Rayleigh theory cannot provide the missing concentration.
More generally, no nondegenerate law supported on perfect matchings of a
simple graph is edge-Strong-Rayleigh: the support of a homogeneous multi-
affine stable polynomial must be a matroid base family, while two distinct
perfect matchings fail one-edge basis exchange.  For the positive Gibbs
law there is also an elementary witness.  Fix a perfect matching, retain
two universal start dummies and their two matched right endpoints, and
condition on every other matching edge.  The residual law is a positive-
weight perfect matching of `K_(2,2)`.  Its two opposite edges occur
together with probability `p` and each has marginal `p`, so their
covariance is `p(1-p)>0`.

The exact proof and the vertex-variable versus edge-variable matching-
polynomial scope audit are in
`MATH_THEOREM_PERFECT_MATCHING_MAXENT_EXACT_MARGINAL_AND_STRONG_RAYLEIGH_NOGO_20260805.md`.
The local positive correlation does not itself rule out concentration of
the particular aggregate Boolean statistics; it rules out only the generic
Strong Rayleigh shortcut.

The classical Gandhi--Khuller--Parthasarathy--Srinivasan dependent rounding
for bipartite graphs preserves marginals and degree constraints, but its
negative-correlation guarantee is local to edge families incident with a
common vertex.  The statistics in Corollary 2.1 contain edges spread across
many left and right vertices, so that theorem does not imply the required
Chernoff bounds.

This limitation is structural for generic assignment polytopes.  Arbitrary
linear-function concentration with exact expectation is not available for
all such polytopes.  Chekuri--Vondrak--Zenklusen obtain dimension-free
Chernoff bounds for matching and matroid-intersection polytopes by rounding
to expectation

\[
                         (1-\gamma)x
\tag{3.1}
\]

for a positive loss parameter `gamma`, rather than preserving `x`
exactly.

At the critical first collar gap, the smallest relevant fractional test
mean is

\[
                         \alpha_ud_{\min}(u)=\Theta(rD)
                         =\Theta(r^{3/2}).
\tag{3.2}
\]

Their exponent is proportional to `gamma` times this mean.  Beating an
`exp(O(r))` union therefore needs

\[
                         \gamma=\Omega(1/D)=\Omega(r^{-1/2}).
\tag{3.3}
\]

One interface would then leave `Theta(W/sqrt(r))` old continuers
unmatched.  This is the scale of the first adjacent-depth tail margin, but
it is larger than the `O(W/r^(3/4))` spread reserve.  Repeating the loss at
`Theta(sqrt(r))` interfaces can create `Theta(W)` breaks unless a separate
nonaccumulation or absorption theorem is proved.

Thus the general scaled theorem is a plausible ingredient, not a direct
proof of Corollary 2.1.

## 4. Exact surviving one-step theorem

The spread-extension problem is reduced to either of the following.

1. **Boolean exact-coloured rounding.**  Prove the Chernoff oracle of
   Corollary 2.1 for the special augmented inclusion graph `J_q` and its
   uniform fractional perfect matching.
2. **Scaled-loss regeneration.**  Use a concentrated `(1-gamma)` matching,
   route its `Theta(W/sqrt(r))` unmatched continuers through the adjacent-
   depth socket margin, and prove that this debt does not accumulate over
   the remaining interfaces.

The unconditional part of this note proves that the fractional coloured
flow itself is exact and that all inherited spread errors contract
geometrically.  The remaining obstruction is the concentration law of one
integral coloured Boolean matching, not an accumulation of `D` marginal
errors.

## 5. External theorem scope used in Section 3

1. R. Gandhi, S. Khuller, S. Parthasarathy, and A. Srinivasan,
   *Dependent Rounding in Bipartite Graphs*, FOCS 2002 / JACM 2006.
2. C. Chekuri, J. Vondrak, and R. Zenklusen,
   *Multi-budgeted Matchings and Matroid Intersection via Dependent
   Rounding*, SODA 2011, arXiv version:
   <https://theory.stanford.edu/~jvondrak/data/matching-chernoff.pdf>.
