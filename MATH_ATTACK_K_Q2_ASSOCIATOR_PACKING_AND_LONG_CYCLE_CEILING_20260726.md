# Exact packing of the pair-frame (Q_2) associator and the long-cycle action ceiling

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The exact (24)-owner pair-frame associator has a genuine macroscopic
packing.  For every

\[
 t=o(m),\qquad s=o(m),\qquad h=2t+s=2^a,
\tag{0.1}
\]

all but (e^{-\Omega(m)}W) middle owners can be partitioned canonically
into packets

\[
                         \mathcal V^t\square Q_s .
\tag{0.2}
\]

Every packet has (2^t) exact pair-frame resolutions.  Each resolution
partitions the packet into (Q_h)'s and hence into physical isometric
(C_{2h})'s.  Thus the completed factors have

\[
                  {W-e^{-\Omega(m)}W\over2h}
\tag{0.3}
\]

long-cycle components.  In particular (t=\Theta(\sqrt m)) local
recouplings are simultaneously available to (1-o(1)) of all owners.

There are, however, two exact limitations.

1. Completed associator packets cannot be additively packed on
   overlapping owner supports: the middle multiplicity of the union is
   the number of supports containing the owner and is independent of all
   shore choices.  Nor can coordinate-overlapping (Q_2) atoms be
   Cartesian-tensored: independent Johnson-cube directions must have
   disjoint coordinate supports.  Thus the presently certified Boolean
   tensor is exactly the coordinate-disjoint tensor.  An overlapping
   construction would be a new nonproduct factor, not a recombination of
   the existing completion theorem.

2. Let a (C_{2h}) Hamming row use a pair frame at matching-switch
   distance at most (t) from a fixed base frame.  If (V) is the base
   middle pair-type histogram and \(\nu_q\) is the lower depth-(q)
   histogram, then

   \[
      \boxed{\mathsf W_1(\nu_q,V)\le {2tq\over h}\,W.}
   \tag{0.4}
   \]

   The same estimate holds cycle by cycle when different rows use
   different frames in the radius-(t) matching ball.  It also holds for
   a final row obtained from at most (t) overlapping recouplings,
   provided the row remains a pair-geodesic Hamming row.

At (q=A\sqrt m+o(\sqrt m)), covering all but (o(W)) targets requires

\[
                         \mathsf W_1(\nu_q,V)
                         =\Omega_A(W\sqrt m).
\tag{0.5}
\]

Consequently a necessary condition is

\[
                              {t\over h}=\Omega_A(1).
\tag{0.6}
\]

On the other hand the cycle-collar toll through
(H=\Theta(\sqrt m)) is

\[
                              O\!\left({HW\over h}\right).
\tag{0.7}
\]

If only (t=O(\sqrt m)) recouplings are used, making (0.7) (o(W))
forces (h/\sqrt m\to\infty), hence (t/h\to0), contradicting (0.6).
Thus the proposed \(O(\sqrt m)\)-layer pair-frame/Hamming architecture,
when linearized by the certified collar-deletion implementation, has the
following action--fragmentation ceiling:

\[
\boxed{
 \begin{array}{c}
 h=\Theta(\sqrt m):\text{ the general radius bound permits the needed
                    action order, but the certified collar is }\Theta(W);\\[2mm]
 h\gg\sqrt m:\text{ an }o(W)\text{ collar, but }
                    o(W\sqrt m)\text{ pair-type transport.}
 \end{array}}
\tag{0.8}
\]

Overlapping the \(t\) recouplings cannot improve (0.4) while the final row
still lies in one pair-geodesic frame: overlap can only
decrease the number of changed matching edges.  The first possible escape
is therefore a genuinely non-Hamming, owner-preserving braid whose
direction monodromy is not contained in one radius-(t) pair frame, or a
construction with (t=\Theta(h)\gg\sqrt m) exact recouplings per row.

## 1. The local completed atom

On one labelled eight-coordinate block write

\[
 B=\{a,b,c,d,u,v,w,x\}
\tag{1.1}
\]

and put

\[
 \mathcal X=\binom{\{a,b,c,d\}}2,
 \qquad
 \mathcal Y=\{uw,ux,vw,vx\},
\tag{1.2}
\]

\[
                         \mathcal V
 =\{X\cup Y:X\in\mathcal X,\ Y\in\mathcal Y\}.
\tag{1.3}
\]

Thus \(|\mathcal V|=24\).  Relative to

\[
 P_0=ab\mid cd\mid uv\mid wx,
 \qquad
 P_1=ac\mid bd\mid uv\mid wx,
\tag{1.4}
\]

the two completed resolutions are

\[
 \mathscr R^0=
 \{Q_0\cup Y:Y\in\mathcal Y\}
 \mathbin{\dot\cup}\{ab\cup Q_R,cd\cup Q_R\},
\tag{1.5}
\]

\[
 \mathscr R^1=
 \{Q_1\cup Y:Y\in\mathcal Y\}
 \mathbin{\dot\cup}\{ac\cup Q_R,bd\cup Q_R\}.
\tag{1.6}
\]

Each side is a partition of \(\mathcal V\) into six physical (Q_2)'s.
The lower depth-one pair-type ledgers, measured in (P_0), are

\[
                         16f_0+8f_1
 \quad\hbox{and}\quad 24f_0.
\tag{1.7}
\]

Hence an exposed new-shore block removes one Bernoulli pair-type
contribution of mean (1/3).  This is the exact signed drift which
motivates iteration.

The important completion fact is that a shore is not a selection of six
independent squares.  The old/new ownership overlap is connected, so an
exact cover made only from the twelve displayed cells chooses all six
old cells or all six new cells.

## 2. Why overlapping atoms do not pack or tensor automatically

The following two elementary facts locate the first exact ownership
failure.

### Lemma 2.1 (overlapping completed supports add fixed multiplicity)

Let \((U_i,\mathscr F_i^0,\mathscr F_i^1)\), (i\in I), be completed
exact trades: each shore \(\mathscr F_i^\eta\) covers every owner of
(U_i) exactly once and no owner outside (U_i).  For arbitrary shore
choices \(\eta_i\), the additive union has middle multiplicity

\[
                         d(x)=|\{i:x\in U_i\}|.
\tag{2.1}
\]

In particular it is an exact factor only when the nonempty (U_i)'s
partition their union.

#### Proof

The incidence of either shore of packet (i) is the same vector
\(\mathbf1_{U_i}\).  Summing these vectors gives (2.1), independently of
the shore bits. \(\square\)

Thus two completed pair-frame associators with overlapping occurrence
sets cannot be *packed by union*.  Cancellation is unavailable because
all middle incidences are nonnegative and both shores have the same
support.

### Lemma 2.2 (commuting Johnson directions are coordinate-disjoint)

Suppose two Johnson swaps are independent directions of a literal
isometric (Q_2).  Then their two unordered coordinate supports are
disjoint.

#### Proof

Write the swaps at one corner as (a\mapsto b) and (c\mapsto d), where
(a,c) are present and (b,d) absent.  If (a=c), applying either swap
makes the other unavailable.  If (b=d), the first swap fills the point
which the second must insert.  If (a=d) or (b=c), the common point
would have to be simultaneously present and absent at the initial
corner.  Therefore all four coordinates are distinct. \(\square\)

Pairwise application gives the usual classification of the relevant
Johnson (Q_r): after removing a fixed core, it chooses one point from
each of (r) disjoint coordinate pairs.

Every coordinate of the pair-frame atom is active in some cell of each
complete resolution: the special coordinates are active in the four
local squares and the reservoir coordinates are active in the two
reservoir squares.  Hence if two full atoms share a coordinate, their
formal Cartesian product contains a pair of cells in which two proposed
independent directions share that coordinate.  Lemma 2.2 rules out that
product cell.

Consequently the certified operations are exactly:

* additive packing on owner-disjoint completed supports; and
* Cartesian tensoring on coordinate-disjoint blocks.

Coordinate-overlapping recouplings may still admit a new joint factor,
but neither local exactness nor the overlap lemma constructs it.  In
particular the matching flips themselves do not commute when they share a
current matching edge: after the first flip that edge no longer exists.
They form a sequential matching path, not a Boolean cube.

## 3. A near-spanning exact tensor with long spectator tails

We next show that ownership density is not the obstruction.

Fix the (2m) ordinary coordinates, leaving the distinguished odd
coordinate in the frozen exterior.  Reserve two disjoint regions.

* Region \(A\) contains \(B_A=\lfloor m/8\rfloor\) disjoint labelled
  eight-blocks, each carrying the support \(\mathcal V\).
* Region (S) contains (P_S=\lfloor m/2\rfloor) disjoint labelled
  coordinate pairs.  The (O(1)) unused coordinates are frozen.

Call an \(A\)-block eligible for a middle owner \(X\) when its restriction
lies in \(\mathcal V\), and call an \(S\)-pair split when \(X\) contains
exactly one of its endpoints.  For owners having at least \(t\) eligible
\(A\)-blocks and at least \(s\) split \(S\)-pairs, choose the first \(t\)
and first \(s\), respectively, and freeze everything else.  Vary the
chosen restrictions over

\[
                         \mathcal V^t\square Q_s.
\tag{3.1}
\]

### Lemma 3.1 (selector stability)

The first-(t), first-(s) lists are constant throughout (3.1).
Consequently these sets form pairwise disjoint canonical packets.

#### Proof

Variation inside \(\mathcal V\) keeps the selected (A)-blocks eligible;
every unselected (A)-block is frozen.  Variation of a selected
spectator pair changes only its orientation and keeps it split; every
unselected spectator pair is frozen.  The two regions are
coordinate-disjoint, so neither variation changes the other selector.
Thus both ordered lists and the exterior remain fixed. \(\square\)

Before conditioning on total rank, an (A)-block is eligible with
probability

\[
                         {24\over2^8}={3\over32},
\tag{3.2}
\]

and an (S)-pair is split with probability (1/2).  The corresponding
indicators are independent inside their separate regions.  Chernoff and
conditioning on rank (m) therefore give the following finite form.

### Proposition 3.2 (near-spanning packet mass)

If

\[
                  t\le {3B_A\over64},
                  \qquad s\le {P_S\over4},
\tag{3.3}
\]

and (G) is the number of owners in the canonical packets, then

\[
 {W-G\over W}
 \le 2(m+1)
 \left[
   \exp\!\left(-{3B_A\over256}\right)
   +\exp\!\left(-{P_S\over16}\right)
 \right].
\tag{3.4}
\]

In particular (G=W-e^{-\Omega(m)}W) whenever (t,s=o(m)).

#### Proof

The eligible count has mean (3B_A/32); the first inequality in (3.3)
is half that mean.  The standard half-mean Chernoff bound gives the first
exponential in (3.4).  The split-pair count has mean (P_S/2), and the
second inequality is again the half-mean threshold, giving the second
exponential.  A union bound handles the two failures.

Under independent fair bits, conditioning on total rank (m) gives the
uniform law on \(\binom{[2m+1]}m\).  The conditioning event has probability
at least (1/[2(m+1)]).  Dividing the unconditioned failure bound by this
probability proves (3.4). \(\square\)

For each resolution vector \(\varepsilon\in\{0,1\}^t\), resolve the
\(i\)-th \(\mathcal V\) factor by \(\mathscr R^{\varepsilon_i}\).  Taking
products gives

\[
 \mathcal V^t\square Q_s
 =\mathop{\dot\bigcup}_{6^t\text{ cells}}Q_{2t+s}.
\tag{3.5}
\]

If (h=2t+s) is a power of two, the standard Hamming syndrome factor
partitions every (Q_h) into (C_{2h})'s, in any prescribed common
cyclic order of its directions.  Hence:

### Theorem 3.3 (literal macroscopic associator tensor)

Under (3.3) and (h=2t+s=2^a), the retained middle owners admit (2^t)
exact alternative (C_{2h})-factors, each with exactly

\[
                              {G\over2h}
\tag{3.6}
\]

components.  All resolution choices have identical middle support.

This proves literal ownership, integrality, and long-cycle realizability.
It does not yet prove a useful all-depth target histogram.

## 4. Exact transport per Hamming row

Fix a base coordinate matching (P) and let (f_P(X)) be the number of
full (P)-pairs in (X).  A recoupling

\[
                         ab\mid cd\longleftrightarrow ac\mid bd
\tag{4.1}
\]

has matching-switch cost one.  If (P') is at switch distance at most
(t) from (P), then

\[
                         |P'\setminus P|\le2t.
\tag{4.2}
\]

Consider one pair-geodesic Hamming cycle (C_{2h}) in frame (P').
Its direction word is

\[
                         \pi_1\cdots\pi_h
                         \pi_1\cdots\pi_h,
\tag{4.3}
\]

where the \(\pi_j\)'s are disjoint (P')-pairs.  Every cycle owner
contains one endpoint of every active pair.

For the lower target (L_i^{(q)}) of the (q)-window beginning at owner
(X_i), put

\[
                         d_i=f_P(X_i)-f_P(L_i^{(q)}).
\tag{4.4}
\]

Deleting an endpoint of a direction \(\pi_j\in P\) cannot break a full
(P)-pair, because (X_i) contains exactly one endpoint of \(\pi_j\).
Thus only directions in (P'\setminus P) can contribute to (d_i), and
each contributes at most one.

### Lemma 4.1 (cycle action identity)

If (b=|\{j:\pi_j\notin P\}|\), then for every (q\le h),

\[
                         \sum_{i=0}^{2h-1}d_i\le2qb\le4qt.
\tag{4.5}
\]

#### Proof

Every one of the (b) bad directions occurs twice in (4.3).  Each
occurrence belongs to exactly (q) cyclic (q)-windows.  Summing the
number of bad directions in each window therefore gives (2qb), which
dominates \(\sum_i d_i\).  Equation (4.2) gives the final inequality.
\(\square\)

Now let a factor on \(G\) owners consist of \(C_{2h}\)'s, each in a
possibly different frame \(P_C\) at distance at most \(t\) from \(P\).
Associate each middle owner with its lower target.  This is a coupling of
the retained source pair-type histogram \(V_G\) and the retained output
histogram \(\nu_{q,G}\).  Its cost is \(\sum_i d_i\).  There are
\(G/(2h)\) cycles, so Lemma 4.1 gives:

### Theorem 4.2 (action-density ceiling)

\[
                  \boxed{
                  \mathsf W_1(\nu_{q,G},V_G)
                  \le {2tq\over h}\,G.}
\tag{4.6}
\]

If (E=W-G) exterior owners are completed arbitrarily, their additional
contribution to every bounded (R\sqrt m)-truncated Lipschitz test is at
most (R\sqrt m E).

The theorem is componentwise and survives arbitrary dependence among the
chosen frames.  It also survives overlapping recouplings: after (t)
matching switches the final frame is still in the radius-(t) ball, and
overlap can only reduce \(|P_C\setminus P|\).  No independence or random
choice is used.

Its scope is one final pair-geodesic Hamming frame per row.  A future row
whose directions undergo nontrivial sequential frame monodromy and admit
no single final pairing \(P_C\) is outside the theorem.  Likewise, if a
row actively uses the distinguished odd coordinate, that direction must
be charged separately; the packet construction above freezes it.

For the tensor in Theorem 3.3, a resolution vector of Hamming weight
(r) uses a frame at switch distance exactly (r), so (4.6) applies with
(t=r\).  Appending the (s) spectator directions increases (h) but
does not increase (r).  This is the exact dilution mechanism.

## 5. Comparison with the Gaussian transport demand

At

\[
                              q=A\sqrt m+o(\sqrt m),
\tag{5.1}
\]

the base middle pair-type law and the rank-\((m-q)\) target pair-type law
are separated on the \(\sqrt m\) scale.  The audited weighted-Gaussian
deficit theorem supplies constants (c_A,R_A>0), a threshold (a_m),
and the nonnegative one-Lipschitz test

\[
 \varphi_m(f)=\min\{(a_m-f)_+,R_A\sqrt m\}
\tag{5.2}
\]

such that any output histogram missing (H_q) distinct targets obeys

\[
 \sum_f\varphi_m(f)(\nu_q(f)-V(f))
 \ge c_AW\sqrt m-R_A\sqrt m H_q-o(W\sqrt m).
\tag{5.3}
\]

The quoted theorem is often written on the even core \([2m]\).  It applies
unchanged to the present odd model.  Indeed, split the source and target
laws according to the bounded infinity bit.  In either stratum the
full-pair statistic has variance \(m/16+o(m)\), and the two relevant
saddles and the crossing threshold differ from their even-core values by
only \(O(1)\).  The same truncated one-Lipschitz test therefore has the
same positive Gaussian limit in both strata.  Summing the two strata
gives (5.3); allowing windows to cross the infinity bit changes only the
output histogram, not the validity of the Lipschitz lower bound.

Kantorovich duality and (4.6) give the opposite bound

\[
 \sum_f\varphi_m(f)(\nu_q(f)-V(f))
 \le {2tq\over h}W+R_A\sqrt m E.
\tag{5.4}
\]

If (E=o(W)), combining (5.1)--(5.4) yields

\[
 {H_q\over W}
 \ge {c_A\over R_A}
      -{2A\over R_A}{t\over h}-o(1).
\tag{5.5}
\]

### Corollary 5.1 (positive-density holes when (t/h\to0))

If (t/h\to0), every factor in the radius-(t) pair-frame/Hamming
architecture misses \(\Omega_A(W)\) targets at depth
(q=A\sqrt m+o(\sqrt m)).

In particular, eliminating the Gaussian pair-type deficit requires

\[
                         {t\over h}\ge {c_A\over2A}+o(1)
\tag{5.6}
\]

with the normalization of (5.3).  The displayed constant is not asserted
sharp; the constant-order necessity is sharp for this argument.

This is stronger than merely requiring a positive density of starts to
cross pair type.  A sparse set of changed directions can make a positive
fraction of long (q)-windows nonnative while moving each such window
only (O(1)) or (o(\sqrt m)) type steps.  The Gaussian deficit has
transport cost \(\Theta_A(W\sqrt m)\), so adjacent birth--death motion,
not just support crossing, is the relevant ledger.

## 6. Exact component and collar tradeoff

Theorem 3.3 has \(G/(2h)\) long-cycle components.  Breaking and joining
these cycles in the standard literal word construction changes exactly
\(q-1\) cyclic starts at each cut at depth \(q\).  The usual certified
construction discards the \(H\)-neighbourhood of every cut once for the
whole range \(q\le H\); its collar-deletion cost is therefore

\[
                         O\!\left({HG\over h}\right).
\tag{6.1}
\]

Take (H=A\sqrt m+O(1)) and suppose only

\[
                              t\le C\sqrt m
\tag{6.2}
\]

recouplings are available per row.

* If the certified collar-deletion cost (6.1) is \(o(W)\), then
  \(h/H\to\infty\), and (6.2) gives
  \(t/h\to0\).  Corollary 5.1 leaves \(\Omega_A(W)\) holes.
* If (t/h\) is bounded below as required by (5.6), then
  \(h=O_A(t)=O(\sqrt m)\), and (6.1) is \(\Theta(W)\), not \(o(W)\).

For the unsuspended tensor (s=0), one has (h=2t).  It therefore sits
exactly at the critical point: it has sufficient *order* of pair-type
action, but (G/(4t)=\Theta(W/\sqrt m)) components and a
\(\Theta(W)\) Gaussian collar.  Adding spectator directions repairs the
component count only by diluting action in the identical ratio.

For the fully product-transversal canonical tensor there is a sharper
fact: one touched new-shore block erases a Bernoulli contribution of mean
\(1/3\).  If a shallow window touches \(q\) distinct blocks, its exact
mean death is \(q/3\), whereas the uniform rank-\((m-q)\) law is displaced
from the middle law by \(q/2+O_A(1)\).  Thus this particular unsuspended
tensor already has the wrong drift; “sufficient order” above refers only
to the general radius-\(t\) upper envelope (4.6), not to the canonical
all-new corner.

If (L) sequential radius-one recoupling slabs are used instead of one
radius-(L) endpoint factor, the raw number of state boundaries can be
as small as (O(LW/h)) only after a compatible row identification has
been proved.  Weighting each boundary by its depth-(H) collar gives

\[
                         O\!\left({LHW\over h}\right).
\tag{6.3}
\]

For (L,H=\Theta(\sqrt m)) and (h\le m), this is never (o(W)).
More fundamentally, the sequential identification is not provided by
the local associator when consecutive recouplings overlap: Section 2
shows that those atoms neither pack by union nor tensor as commuting
cube dimensions.

Equations (6.1)--(6.3) are the costs of the collar-deletion and literal
serial-slab architectures, not universal lower bounds against a future
seam-balanced fused braid.  The statewise result within the current
pair-geodesic Hamming architecture, independent of how seams are later
treated, is (4.6).

## 7. Exact boundary

Proved here:

1. a canonical (1-e^{-\Omega(m)}) owner packing of
   \(\mathcal V^t\square Q_s);
2. (2^t) literal exact completed factors on every packet;
3. physical (C_{2h})-realizability and the exact component count
   (G/(2h));
4. the fixed-incidence obstruction to additive overlap;
5. the coordinate-disjointness obstruction to Cartesian overlap;
6. the statewise action ceiling (4.6), valid under arbitrary dependent
   component/frame choices; and
7. the (O(\sqrt m))-recoupling action--collar no-go (0.8).

Not proved, and not ruled out:

* a new nonproduct factor jointly completing coordinate-overlapping
  associators;
* a non-Hamming long cycle with growing pair-frame monodromy, so that one
  row is not contained in a radius-(t) pair frame;
* (t=\Theta(h)\gg\sqrt m) exact recouplings per long row; or
* a fused braid whose internal interfaces do not pay the serial collar
  (6.3).

Therefore the existing (Q_2) associator does have macroscopic exact
owner capacity.  Its first failure is not density or local signed drift.
It is the simultaneous requirement of

\[
 \text{positive matching-action density }t/h
 \quad\hbox{and}\quad
 \text{vanishing component collar }H/h.
\tag{7.1}
\]

With only (t=O(H)=O(\sqrt m)) local recouplings, these two ratios cannot
respectively stay positive and tend to zero.
