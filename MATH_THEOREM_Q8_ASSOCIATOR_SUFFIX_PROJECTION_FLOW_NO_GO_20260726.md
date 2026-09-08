# The `Q_8` associator does not cross the first-eligible suffix Hall cut

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The phase-synchronized crossed `Q_8` associator in
`MATH_THEOREM_PHASE_SYNCHRONIZED_CROSSED_Q8_ASSOCIATOR_20260726.md`
genuinely changes the direction frame and gives a fixed-point-free
same-owner opposite.  If it is installed only inside the active coordinates
of a fixed first-eligible packet, however, it cannot improve the frozen
suffix Hall ledger at all.

The reason is stronger than an option-count bound.  The complete outer
incidence graph is block diagonal under the exact suffix projection

\[
                         X\longmapsto X\cap R.
\]

Frame changes may increase degrees and alter codegrees inside one block,
but they create no edge between two projection blocks.  The optimal
fractional flow, the optimal integral selection, and every multiple-choice
packet selection therefore obey the same explicit projection deficiency.

For a suffix `R` of size `s`, at lower depth `q` that deficiency is

\[
 \boxed{
 \sum_{k=0}^{s}\binom sk
 \left[
   \binom{2m-s}{m-q-k}-\binom{2m-s}{m-k}
 \right]_+ .}                                            \tag{0.1}
\]

The analogous upper deficiency replaces `m-q-k` by `m+q-k`.
Exceptional owners capable of entering `R` can reduce either bound by at
most their number.

Thus the fixed-point-free frame change closes a local ownership gate but
does **not** enlarge the outer option catalogue in the direction needed by
first-eligible Hall.  To exploit it globally, one must embed an associator
whose physical support crosses the first-eligible boundary, or use a moving
ambient atlas with no common positive-density suffix.

## 1. Projection-flow lemma

Let `U` be a finite owner set, `T` a target set, and let

\[
                         \pi_U:U\to Z,\qquad \pi_T:T\to Z
\]

be projections to a common finite set.  Partition `U` into packets.  Every
packet option gives each of its owners at most one target occurrence.  The
options may be arbitrarily numerous and may be selected integrally,
fractionally, independently, or with arbitrary dependence between packets.

Assume only the statewise conservation law

\[
       X\longmapsto t\quad\Longrightarrow\quad
                         \pi_T(t)=\pi_U(X).                 \tag{1.1}
\]

Put

\[
                         S_z=|\pi_U^{-1}(z)|,
 \qquad                  D_z=|\pi_T^{-1}(z)|.              \tag{1.2}
\]

### Theorem 1.1 (exact projection deficiency)

Every integral option selection misses at least

\[
                         \sum_{z\in Z}(D_z-S_z)_+           \tag{1.3}
\]

targets.  The same lower bound holds for uncovered mass in every fractional
packet LP normalized to total owner mass one.  If a set `E` of exceptional
owners is exempt from (1.1), the right side decreases by at most `|E|`.

#### Proof

By (1.1), all occurrences reaching the target fibre `pi_T^{-1}(z)` come
from the `S_z` owners in `pi_U^{-1}(z)`.  Each owner supplies total integral
or fractional mass at most one.  Therefore covered target mass in that
fibre is at most `min(D_z,S_z)`, and its uncovered mass is at least
`(D_z-S_z)_+`.  Sum over the disjoint fibres.

An exceptional owner contributes at most one occurrence and hence can
decrease total deficiency by at most one. \(\square\)

This is simultaneously a Hall dual and a flow decomposition.  In the
bipartite occurrence graph, (1.1) says that the adjacency matrix is a
direct sum over `z`.  No within-block degree or codegree estimate can move
capacity between its summands.

## 2. Exact binomial ledger for a frozen coordinate set

Take

\[
 U=\binom{[2m]}m,qquad
 T_q^-=\binom{[2m]}{m-q},qquad
 T_q^+=\binom{[2m]}{m+q},                              \tag{2.1}
\]

and let `R subset [2m]` have size `s`.  Use the exact-set projection

\[
                         \pi(X)=X\cap R.                   \tag{2.2}
\]

For a fixed `Z subset R`, `|Z|=k`, the fibre sizes are

\[
 \begin{aligned}
 S_Z&=\binom{2m-s}{m-k},\\
 D^-_Z&=\binom{2m-s}{m-q-k},\\
 D^+_Z&=\binom{2m-s}{m+q-k}.
 \end{aligned}                                           \tag{2.3}
\]

Applying Theorem 1.1 and grouping the `binom(s,k)` subsets of size `k`
gives exactly (0.1) and

\[
 \boxed{
 \sum_{k=0}^{s}\binom sk
 \left[
   \binom{2m-s}{m+q-k}-\binom{2m-s}{m-k}
 \right]_+ .}                                            \tag{2.4}
\]

These exact-set deficiencies imply the earlier one-sided suffix-count
cuts, but do not require choosing a threshold `k<=a` in advance.

## 3. Application to the phase-synchronized associator

Fix the ordered first-eligible atlas and a packet `P`.  Let `A(P)` be its
active physical coordinate support.  For every normal packet in the
frozen-suffix theorem,

\[
                         A(P)\cap R=\varnothing.             \tag{3.1}
\]

The corrected `Q_8` associator has the following operations only:

1. it alternates between two active child blocks;
2. it applies parent neighbour moves in those child blocks; and
3. its relative involution exchanges `Li` with `R(Si)` inside the same
   eight-coordinate support.

Hence every vertex of every resulting component agrees on `R`.  For every
phase start `X`, every lower intersection and upper union consequently
satisfies

\[
 \tau^-_{q}(X)\cap R=X\cap R,
 \qquad
 \tau^+_{q}(X)\cap R=X\cap R.                         \tag{3.2}
\]

Equation (3.2) is (1.1) for both signs.  It survives:

* arbitrary choices among the corrected shores;
* the affine parity-complete lift built from the associator;
* arbitrary compositions of associators on active coordinates;
* arbitrary relabellings which preserve `A(P)`; and
* arbitrary integral or fractional mixing of whole packet components.

Therefore every such enlarged option catalogue has the same lower bounds
(0.1) and (2.4), up to the exponentially small nonnormal/leave owner set.
At `q=A sqrt(m)` and a suffix of positive limiting density, the standard
hypergeometric central limit comparison makes these deficiencies
`Omega_A(W)`, exactly as in the frozen-suffix theorem.

## 4. Escape boundary

The local associator can affect outer Hall only if its embedding violates
(3.1).  Concretely, at least one child block must contain a suffix
coordinate, so a component transports actual owner mass between distinct
values of `X cap R`.  Merely mapping an active left direction to an active
right direction is not enough, even when the relative permutation has no
fixed coordinate.

This leaves two honest global uses of the `Q_8` primitive:

1. a **cross-boundary associator atlas**, whose active supports overlap a
   moving family of suffixes and whose owner components remain exactly
   packable; or
2. a **moving first-eligible chronology**, in which no fixed `R` is frozen
   on `1-o(1)` of the owners.

Either redesign must prove exact owner compatibility.  Catalogue size,
fixed-point-freeness, and intrapacket trace injectivity alone cannot alter
the projection-flow dual.

There is also a quantitative minimum on any cross-boundary redesign.

### Proposition 4.1 (cross-direction occurrence budget)

Let a packet factor consist of isometric `C_(2h)`'s on `h` active physical
directions.  Suppose only `t` of those directions belong to `R`.  At depth
`q<h`, at most

\[
                              {tq\over h}                     \tag{4.1}
\]

of its directed phase starts can have a trace whose suffix projection
differs from the starting owner's projection.  Consequently a collection
of such packets can alter at most `(tq/h)W` occurrences relative to the
suffix-preserving ledger.  Clearing a Hall deficit `delta W` requires

\[
                              t\ge \delta {h\over q}.          \tag{4.2}
\]

#### Proof

In a doubled-permutation direction word every one of the `h` directions
occurs twice.  One fixed occurrence belongs to exactly `q` cyclic
`q`-windows.  Hence the number of directed starts whose window contains
one of the `t` suffix directions is at most `2tq`, out of `2h` starts on
the cycle.  A trace can change `X cap R` only if its direction window
contains a suffix direction.  This proves (4.1), and summing phase starts
over the exact owner partition proves (4.2). \(\square\)

Thus a bounded number of boundary-crossing `Q_8` cells per macropacket is
still insufficient when `q/h -> 0`.  At a Gaussian depth
`q=Theta(sqrt(m))` with `h=Theta(m)`, a successful atlas needs
`Omega(sqrt(m))` genuinely cross-boundary active directions per packet (or
an equivalent moving-support mechanism).  A single local associator cannot
carry the outer transport by itself.

## 5. The full moving atlas removes the dual only fractionally

The obstruction is genuinely caused by the fixed atlas, not by a global
capacity imbalance.  Let `F` be any exact middle factor and let

\[
                         \{\sigma F:\sigma\in S_{2m}\}          \tag{5.1}
\]

be its complete coordinate-conjugacy atlas.

### Proposition 5.1 (uniform conjugacy marginal)

The uniform fractional average of (5.1) has owner load exactly one and,
at every depth `q`, target load exactly

\[
                              {W\over N_q}                     \tag{5.2}
\]

on every lower target and on every upper target.

#### Proof

Every `sigma F` is an exact middle factor, so averaging gives owner load one
pointwise.  The symmetric group is transitive on each target rank, hence
the averaged target load is constant.  Its total mass is `W` (one directed
trace occurrence per middle owner), and division by the `N_q` targets gives
(5.2).  Complementation gives the identical upper statement. \(\square\)

Thus a moving atlas clears every suffix-projection Hall dual at the
fractional level.  The unresolved outer theorem is precisely an integral
decomposition/rounding theorem which mixes conjugate frames while retaining
whole exact owner components.  The local `Q_8` associator supplies one
legal frame-changing primitive, but Proposition 4.1 shows that a bounded
number of such primitives per packet cannot approximate the conjugacy
marginal at Gaussian depth.
