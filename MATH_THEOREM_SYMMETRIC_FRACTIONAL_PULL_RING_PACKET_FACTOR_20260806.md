# A symmetric fractional factor of owner-once pull rings

## Status

The corrected triangular pull-clock coefficients can be realized without
repeating an owner inside a packet.  More precisely, they are a convex
combination of literal, state-balanced, owner-once Johnson rings, each ring
carrying either no pull or one **pure repeated pull-block type**.  After
symmetrization, every middle owner and every immediate-lower root has load
one, while every named residual lower target has exactly its prescribed
fractional load.

This closes the full marked fractional packet-factor version of the
macroscopic complementary-profile problem, including both immediate
palettes.  It is not an integral decomposition: the
same owner occurs fractionally in many alternative packets, and the theorem
does not select one packet occurrence per owner or fuse the selected packet
cycles.

## 1. Triangular data

Work on a ground set of size `k=2r-1`, and put

\[
 D=d+1,\qquad c=r-D.                                      \tag{1.1}
\]

Let `b_s` be the left-filled triangular boundary multiplicities and

\[
 q_s={\binom{k}{s}-b_s\over W},\qquad
 W=\binom{k}{r},\qquad 1\le s<r.                           \tag{1.2}
\]

Use the nonnegative pull-clock coefficients

\[
                         x_{\delta,j}\ge0,
 \qquad1\le\delta\le c,\quad1\le j\le d,                \tag{1.3}
\]

from the corrected triangular pull-clock theorem.  Their staircase tiles
have the following literal meaning.  A block of type `(delta,j)` consists
of `j` consecutive phases in which the same `delta` core coordinates are
omitted, followed by one full-core separator.  Relative to the all-high
profile, it moves exactly `j-q+1` width-`q` occurrences from rank `c+q`
to rank `c+q-delta`, for every `q<=j`.

The coefficients satisfy

\[
             C:=\sum_{\delta=1}^c\sum_{j=1}^d
                         (j+1)x_{\delta,j}\le1,             \tag{1.4}
\]

and the resulting marked rank profile dominates `q=(q_s)`.  Rankwise
thinning gives equality.

For odd `k=2r-1`, `q_(r-1)=1`, so the terminal high deficit is zero and

\[
                         x_{\delta,d}=0                     \tag{1.5}
\]

for every `delta`.  Thus no positive-weight packet has a low run of length
`d`; every width-`d` source interval is the intended rank-`r-1` immediate
lower root.

## 2. Pure integral packet types

### Proposition 2.1 (the shortest facet ring collapses upstairs)

Take `L=D+1`, a core `K` of size `r-D`, and `L` private labels forming
`F`.  The cyclic source word

\[
                         A_t=K\cup\{f_t\}                    \tag{2.1}
\]

has owner set

\[
                         \{H-\{f\}:f\in F\},
                 \qquad H=K\cup F.                          \tag{2.2}
\]

Every cyclic order of `F` gives a literal owner-once Johnson ring, for
both parities of `L`.  Its immediate-lower roots are

\[
                         H-\{f_t,f_{t+1}\}.                  \tag{2.3}
\]

All of its immediate-upper colours, however, are the same set `H`.

#### Proof

A length-`D=L-1` source window omits exactly one private phase.  Consecutive
windows exchange the two consecutive omitted labels, giving (2.2)--(2.3).
The union of two consecutive owners is all of `H`.
The source word itself is cyclically balanced under one-step translation;
no shift-two macro packaging is needed.  \(\square\)

Thus `L=D+1` is unusable for an upper-rich factor.  The packets below keep
one additional private phase.

For every `j`, put `ell_j=j+1` and choose the multiple

\[
 L_j=\ell_j
       \left\lceil{D+2\over\ell_j}\right\rceil.            \tag{2.4}
\]

Then

\[
 D+2\le L_j\le D+\ell_j+1\le2D+1.                         \tag{2.5}
\]

Assume henceforth that

\[
                            r\ge D+2,                        \tag{2.6}
\]

so `L_j<=r+D-1`, and the required private phase labels fit on `[2r-1]`.

Choose a core `K` of size `c`, `L_j` distinct private labels
`f_0,...,f_(L_j-1)`, and a `delta`-set `H\subseteq K`.  On the cyclic phase
set `Z_(L_j)`, repeat the word

\[
 \underbrace{\text{low},\ldots,\text{low}}_{j\text{ phases}},
 \text{high}.                                             \tag{2.7}
\]

At a low phase `t` use

\[
                       A_t=(K-H)\cup\{f_t\},                \tag{2.8}
\]

and at a high phase use

\[
                       A_t=K\cup\{f_t\}.                    \tag{2.9}
\]

Call this a pure packet of type `(delta,j)`.  An all-high packet is the
same construction with (2.9) at every phase; take `L=D+2`.

### Lemma 2.2 (literal pure packet)

Every pure packet is one state-balanced owner-once component.  Its owner
windows are `L_j` distinct rank-`r` sets forming a Johnson cycle; its
immediate-lower roots and immediate-upper colours are also separately
`L_j` distinct.  All of its proper source
interval unions, across every width `1<=q<D`, are pairwise distinct.
Per source phase, its net proper-window profile relative to the all-high
packet is

\[
                    {1\over j+1}\,S_{\delta,j},             \tag{2.10}
\]

where `S_(delta,j)` is the signed pull-clock staircase tile.

#### Proof

Since `j<=d=D-1`, every length-`D` source window contains a high separator.
It therefore contains all of `K` and has union

\[
                     K\cup\{f_t,\ldots,f_{t+D-1}\}.        \tag{2.11}
\]

The private interval gives distinct owners, and shifting once deletes one
private label and inserts one, so the owners form a Johnson cycle.  Their
intersections are `K` plus distinct cyclic `(D-1)`-intervals.
Their unions are `K` plus distinct cyclic `(D+1)`-intervals, because
`D+1<L_j`.

Every proper source interval has as its intersection with the private-label
set exactly the corresponding cyclic interval of the `f` labels.  At fixed
width these recover the start phase, while different widths have different
private cardinalities.  Hence no two proper intervals in one packet have
the same union.

The cyclic source word itself is one state-balanced component under the
one-source shift and uses every owner start exactly once.  There are exactly
`L_j/(j+1)` pull blocks.  Within each block, a width-`q` interval loses the
`delta` coordinates precisely when it is wholly contained in the `j` low
phases, which occurs `j-q+1` times for `q<=j`.  Divide by `L_j` to obtain
(2.10).  \(\square\)

## 3. The convex packet mixture

Give the all-high packet type weight

\[
                              p_0=1-C,                       \tag{3.1}
\]

and the pure type `(delta,j)` weight

\[
                       p_{\delta,j}=(j+1)x_{\delta,j}.       \tag{3.2}
\]

These weights are nonnegative and sum to one.  Within each type, average
uniformly over:

* all ground-set images of the core and private labels;
* all cyclic orders of the private labels;
* all choices of the omitted `delta`-set;
* all cyclic translations of the low/high pattern.

Normalize each type-orbit so that every rank-`r` owner has total load one.
Equivalently, because every packet of that type has `L_j` owners, its total
packet mass is `W/L_j`.

### Theorem 3.1 (symmetric fractional pull-ring packet factor)

For every sufficiently large odd `k=2r-1`, the mixture above is a weighted
family of literal packets with all of the following properties.

1. Every packet is individually state-balanced under the one-source shift
   and is one owner-once Johnson component.
2. Every rank-`r` owner has aggregate load exactly one.
3. Every rank-`r-1` immediate-lower root has aggregate load exactly one.
4. Every rank-`r+1` immediate-upper target has aggregate raw load
   `(r+1)/(r-1)` and admits a symmetric marking of load exactly one.
5. Before thinning, the aggregate proper-window rank profile is exactly the
   pull-clock profile `v=(v_s)`.
6. There is a symmetric rankwise marking of proper-window occurrences for
   which every fixed rank-`s` target has aggregate load

   \[
                  1-{b_s\over\binom{k}{s}}
                  \qquad(1\le s<r).                        \tag{3.3}
   \]

   The triangular boundary bank supplies the complementary load.

#### Proof

Lemma 2.2 proves the literal packet assertions.  The symmetric group on the
ground set acts transitively on the owner shore, so a uniformly averaged
type-orbit has constant owner load; normalize it to one.  Each packet has
the same number of owner incidences and immediate-lower-root incidences.
The two shores both have cardinality `W`, and ground-set symmetry is
transitive on the root shore.  Hence root load is also one.  Convex mixing
preserves both identities.

Every packet has one upper occurrence per owner.  The upper shore has size
`binom(2r-1,r+1)`, so symmetry gives each upper target raw load

\[
 {W\over\binom{2r-1}{r+1}}={r+1\over r-1}.                \tag{3.4}
\]

Mark the fraction `(r-1)/(r+1)` of every upper occurrence.  This gives
exact upper load one; the unmarked physical duplicates are harmless.

The all-high baseline has total mixture weight one.  By Lemma 2.2, pure
type `(delta,j)` contributes its staircase correction divided by `j+1`.
Multiplication by (3.2) therefore contributes exactly
`x_(delta,j)S_(delta,j)`.  Summing over all types reproduces the corrected
pull-clock telescoping decomposition, proving item 5.

The pull-clock theorem gives `v_s>=q_s`.  Mark each rank-`s` proper-window
occurrence with the symmetric fraction `q_s/v_s` (and mark none when both
are zero).  To make the occurrence convention explicit, map a cyclic
width-`q` source window to the unique length-`D` owner window having the
same right endpoint.  As `q=1,...,D-1`, these are exactly the nested proper
suffixes of that owner.  This is a bijection at every `q`, and the private
labels make the inclusions strict.  Therefore deleting any fraction of the
marks preserves legality of the marked chain.

After full ground-set symmetrization, a fixed owner carries total marked
rank-`s` mass `q_s`, uniformly over its `binom(r,s)` rank-`s` subsets.  A
fixed rank-`s` target belongs to `binom(k-s,r-s)` owners.  Its load is

\[
 {\binom{k-s}{r-s}\over\binom{r}{s}}q_s
   ={Wq_s\over\binom{k}{s}}
   =1-{b_s\over\binom{k}{s}},                              \tag{3.5}
\]

which proves (3.3).  \(\square\)

## 4. Why the pure-type trick matters

The stationary pull-clock proof clears all denominators on one long
timeline.  That timeline repeats owners.  Trying instead to round all
`x_(delta,j)` simultaneously inside one short owner-once ring creates a
knapsack divisibility problem, especially because the packing cost (1.4)
can be close to one.

The convex construction avoids that obstruction exactly.  A pure
`(delta,j)` ring has length divisible by `j+1`, so it is tiled integrally by
that block type.  Its mixture weight `(j+1)x_(delta,j)` then recovers the
desired block density.  No common denominator and no within-ring rounding
are required.

No parity condition on `L_j` is needed.  Evenness appeared in the separate
bookkeeping which partitions a source ring into disjoint shift-two
two-owner macros.  A whole cyclic source ring is already a balanced literal
chronology under the one-source shift.  If a later interface insists on
two-owner macro packets, odd rings need a different packaging; that is not
part of this fractional whole-ring theorem.

## 5. Exact remaining gate

This theorem proves a symmetric **fractional** packet master containing,
in the same packet coordinates:

* full literal state balance;
* one-copy owners within each packet;
* exact aggregate owner and immediate-lower-root factors; and
* an exact marked immediate-upper factor; and
* the complete fractional residual named-target load.

It does not prove an integral rainbow packet matching.  The remaining
lower-side theorem is to choose an integral, nearly spanning collection of
these decorated packets so that each owner and named target is used at most
once (and all but `O(1)` required targets are used), then fuse its packet
cycles without destroying the markings.  Fractional feasibility and
macroscopic profile balance are no longer obstructions to that theorem.

## 6. Exact pair spread and the laminar exception

The packet list is simple, but its target codegrees are not uniformly
small: nested suffixes are intentionally correlated.  The precise boundary
is elementary.

Fix one ground-set orbit `O` of one pure packet type, with an integral
choice of marked targets.  Let `a_s` be the number of marked rank-`s`
targets in one packet, and let `a_(s,t,u)` be the number of ordered marked
pairs `(S,T)` in one packet satisfying

\[
                 |S|=s,\qquad |T|=t,\qquad |S\cap T|=u.    \tag{6.1}
\]

Uniform orbit averaging gives the exact formulas

\[
 d(S)={|O|a_s\over\binom{k}{s}},                           \tag{6.2}
\]

and, for distinct `S,T`,

\[
 d(S,T)=
 {|O|a_{s,t,u}\over
   \binom{k}{u}\binom{k-u}{s-u}\binom{k-s}{t-u}}.          \tag{6.3}
\]

Consequently

\[
 {d(S,T)\over d(S)}=
 {a_{s,t,u}/a_s\over
   \binom{s}{u}\binom{k-s}{t-u}}.                          \tag{6.4}
\]

In a pure `(delta,j)` packet, a fixed target rank can occur at no more than
two source widths: the high width `q=t-c` and the low width
`q=t-c+delta`.  There are `L_j` starts at each width, so

\[
                         {a_{s,t,u}\over a_s}\le2L_j\le6D. \tag{6.5}
\]

If `T` is not contained in `S`, then `u<t`, and

\[
 \binom{s}{u}\binom{k-s}{t-u}\ge k-s\ge r.                \tag{6.6}
\]

Thus every noncontainment pair has relative codegree

\[
                         O(D/r)=O(r^{-1/2}).                 \tag{6.7}
\]

For containment pairs `T\subsetneq S`, however, (6.4) has denominator only
`\binom{s}{t}`, which may be constant at the bottom ranks.  This is a real,
sharp exception: targets on one owner suffix chain are meant to occur
together.  Therefore a generic low-codegree matching theorem cannot be
applied to the individual target vertices.  Integral rounding must either
contract whole nested owner chains, use a laminar matching theorem, or
treat containment pairs as prescribed positive correlations.  Away from
that laminar family, the packet system has the desired vanishing pair
spread.

#### Proof of (6.2)--(6.4)

The symmetric group is transitive on rank-`s` targets and on ordered pairs
with fixed `(s,t,u)`.  Count packet-target and packet-pair incidences.  The
number of possible second targets `T` of rank `t` and intersection `u` with
a fixed `S` is

\[
                       \binom{s}{u}\binom{k-s}{t-u}.         \tag{6.8}
\]

Dividing the two incidence identities gives (6.4).  The remaining bounds
were proved above.  \(\square\)
