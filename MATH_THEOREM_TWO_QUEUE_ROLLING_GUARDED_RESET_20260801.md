# A two-queue rolling guarded reset

Date: 2026-08-01

Status: unconditional local construction.  It gives a nonconstant rolling
age reset with distinct rank-`r` owners, exact depth-`d` cyclic residence, exact rail
balance, regeneration of the departure queue, and simple immediate lower
and upper palettes.  It does not embed the reset in a spanning
upper-complete owner factor or solve the terminal compiler.

## 1. Construction

Put

\[
                         n=d+1.
\]

Choose pairwise disjoint sets

\[
 K,\qquad L=\{\lambda_1,\ldots,\lambda_n\},qquad
 R=\{\rho_1,\ldots,\rho_n\},                         \tag{1.1}
\]

with

\[
                         |K|=r-n.                     \tag{1.2}
\]

Thus the construction needs

\[
                         |K\cup L\cup R|=r+n=r+d+1   \tag{1.3}
\]

ground coordinates.  Read the following `2n` letters cyclically:

\[
 K\cup\{\lambda_1\},\ldots,K\cup\{\lambda_n\},
 K\cup\{\rho_1\},\ldots,K\cup\{\rho_n\}.           \tag{1.4}
\]

Every letter is nonempty, even when `K` is empty.

### Theorem 1.1 (rolling reset ring)

Assume `d>=1`, `r>=d+1`, and `k>=r+d+1`.  The cyclic word (1.4) has the
following properties.  For the central parameters `r=ceil(k/2)` and
`d=d(k)`, the first rank inequality is automatic (`d<=r-1`); the last is
the eventual spare-coordinate condition.

1. Its `2n` cyclic length-`n` unions are distinct rank-`r` owners and form a
   simple Johnson cycle.
2. The `2n` consecutive owner intersections are pairwise distinct rank-
   `(r-1)` sets, and the `2n` consecutive owner unions are pairwise distinct
   rank-`(r+1)` sets.
3. Every coordinate in `L union R` has one owner run of length exactly
   `n=d+1`; every coordinate in `K` is permanently present.
4. At the owner `K union L`, the input departure queue is

   \[
   C_d=\{\lambda_1\},\ C_{d-1}=\{\lambda_2\},\ldots,
   C_1=\{\lambda_d\},\quad
   C_0=K\cup\{\lambda_n\}.                            \tag{1.5}
   \]

   After the `R` half of (1.4), the literal state at `K union R` is

   \[
   C'_d=\{\rho_1\},\ C'_{d-1}=\{\rho_2\},\ldots,
   C'_1=\{\rho_d\},\quad
   C'_0=K\cup\{\rho_n\}.                              \tag{1.6}
   \]

   Thus the collar consumes `C_d,...,C_0` in order and exports the identical
   interface with `L` replaced by `R`.  The second half regenerates `L`.
5. If the incoming ages of the core coordinates in `K` are left unfixed,
   the first `R`-letter refreshes all of them.  The terminal state (1.6) is
   nevertheless fixed.  Hence the half-ring is a genuine reset of the
   unfixed core fibre, not only a transport of a state already known in
   full.

The construction has no repeated owner and no intrinsic extra owner slot.
Its protected-state size is `Theta(d)`, attaining the departure-queue lower
bound of
`MATH_THEOREM_PARTIAL_AGE_FIBRE_RESET_AND_GUARD_RAIL_LOWER_BOUND_20260801.md`.

## 2. Owner chronology

Let `X_1,...,X_(2n)` be the private coordinates in the cyclic order

\[
 \lambda_1,\ldots,\lambda_n,\rho_1,\ldots,\rho_n.
\]

The owner beginning at phase `a` is

\[
                         T_a=K\cup\{X_a,X_{a+1},\ldots,X_{a+n-1}\}, \tag{2.1}
\]

with indices modulo `2n`.  It has rank `|K|+n=r`.  Since all `X_i` are
distinct and `n<2n`, different cyclic intervals in (2.1) are different.
Moreover

\[
                         T_{a+1}=T_a-\{X_a\}+\{X_{a+n}\},            \tag{2.2}
\]

so the owner chronology is a simple Johnson cycle.

There are exactly `2n` owners for `2n` cyclic source positions.  Thus the
reset is nonconstant but its central derivative remains flat of rank `r`; it
creates no central-owner multiplicity and needs no stutter.  A later global embedding
must replace an equally sized protected owner segment, rather than append
the ring as an independent word.

## 3. Immediate palettes

For the edge `T_a T_(a+1)`,

\[
\begin{aligned}
 I_a&=T_a\cap T_{a+1}
     =K\cup\{X_{a+1},\ldots,X_{a+n-1}\},\\
 U_a&=T_a\cup T_{a+1}
     =K\cup\{X_a,\ldots,X_{a+n}\}.                   \tag{3.1}
\end{aligned}
\]

Thus `I_a-K` is a cyclic interval of length `n-1` in a `2n`-cycle, while
`U_a-K` is one of length `n+1`.  Both lengths lie strictly between zero and
`2n`, so the start phase is recovered from the set.  Consequently both
palettes in (3.1) are simple.

This also proves the local owner/lower-q1/upper-q1 resource disjointness
needed to plant the reset as one protected macro.

## 4. Residence, synchronization and regeneration

A private coordinate `X_i` belongs to exactly those owner windows whose
cyclic interval of length `n` contains phase `i`.  These are exactly `n`
consecutive owners.  Hence every nonconstant coordinate run has length
`n=d+1`, the exact residence threshold.

At the boundary after the `L` letters, the last occurrence of
`lambda_i` is `n-i` positions old, giving (1.5).  During the next half-ring,
transition `i` deletes `lambda_i` and inserts `rho_i`.  Every core coordinate
appears in every new letter and is immediately refreshed.  After the last
`R` letter, the last occurrence of `rho_i` is `n-i` positions old, giving
(1.6).  This is exactly the departure-queue schedule forced by the guard-
rail lower bound.

The second half performs the same operation from `R` back to `L`.  Therefore
the literal order-`d` state sequence is cyclic.  Every rail prefix count
equals its rail suffix count automatically, and the unique successor arcs
give a perfect statewise matching on this protected component.  No separate
phase repair is required.

## 5. Relation to the pivot-rich normal form

The first half of the owner cycle is

\[
 K\cup L,
 K\cup\{\rho_1\}\cup L[2,n],
 \ldots,
 K\cup R.                                             \tag{5.1}
\]

Put

\[
 Q=K\cup\{\lambda_n\},\qquad
 L^-=\{\lambda_1,\ldots,\lambda_d\},\qquad
 R^-=\{\rho_1,\ldots,\rho_d\}.                       \tag{5.2}
\]

For `0<=j<=d`, the first `d+1` owners in (5.1) are exactly

\[
 Q\cup R^-[1,j]\cup L^-[j+1,d],                      \tag{5.3}
\]

the equality-case depth-`d` Johnson geodesic from the sharp
pivot-aperture theorem.  That geodesic stops at

\[
 K\cup\{\lambda_n,\rho_1,\ldots,\rho_d\}.
\]

The rolling reset adds one further Johnson step

\[
 \lambda_n\longmapsto\rho_n.                         \tag{5.4}
\]

Thus it is not literally the same depth-`d` pivot source: it is its
queue-complete one-step extension.  Step (5.4) consumes the age-zero member
`C_0`, and after `d+1` changes `rho_1` has reached age `d`.  The common core
shrinks from `Q` to `K=Q-{lambda_n}` precisely to make this extra exchange
possible without changing owner rank.

The second geodesic closes the rail state cyclically without reversing the
first path.  Because it follows the same cyclic private order, its internal
owners and both q1 palettes are new rather than repeats.

Thus the rolling reset is the queue-complete cyclic extension of the
pivot-rich geodesic normal form.

## 6. Exact surviving global gate

At the local owner/q1/residence level, the nonflat synchronizer requested by
the partial-age theorem exists with optimal `Theta(d)` state and zero
duplicate-owner cost.

What remains is a protected-host theorem which embeds this `2(d+1)`-owner
cycle (opened at one declared rail boundary) in a spanning owner factor while
simultaneously preserving:

1. the unused immediate lower and upper palettes;
2. arbitrary-width upper witnesses outside the macro;
3. the occurrence-labelled lower/common-cap matching; and
4. regeneration across the same-parity Pascal lift.

None of those global rows follows merely from the local ring.

## 7. Independent exact replay

The standalone C++20 audit

`scratch/audit_two_queue_rolling_guarded_reset_20260801.cpp`

constructs the literal source word and verifies, without calling a solver:

1. the cyclic `D^d` identity;
2. owner rank, distinctness and Johnson adjacency;
3. distinct lower- and upper-`q1` palettes;
4. one private-coordinate run of length exactly `d+1` and permanent core
   coordinates;
5. the full `L -> R -> L` age evolution from deliberately nonconstant
   incoming core ages; and
6. the pivot-geodesic identity (5.2).

Compiled with `-O3` and run on H100 for every `1<=d<=20` and
`0<=|K|<=7`, it reports

`PASS_TWO_QUEUE_ROLLING_GUARDED_RESET cases=160 maxd=20 maxcore=7`.

This replay checks the displayed identities; the proof above is uniform in
`d` and `|K|`.
