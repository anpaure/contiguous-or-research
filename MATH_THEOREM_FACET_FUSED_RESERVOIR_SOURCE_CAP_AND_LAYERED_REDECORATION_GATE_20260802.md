# Fused reservoirs: source-cap obstruction and exact layered redecoration gate

Date: 2026-08-02  
Status: unconditional obstruction for complete marked-lower packing on one
fixed support; unconditional q1 capacity bound; and an exact finite-state
reduction of path-preserving q1 avoidance.  No cross-support packing,
deep-upper theorem, or compiler theorem is claimed.

## 0. Outcome

The fixed-support Middle-Levels zipper theorem fuses every core module over
one support into one owner/q1-simple resident component when `k` is even.
The natural next proposal is to pack many such complete fused reservoirs.

There are two different answers depending on what "complete" protects.

* If the literal source rows `P,H` are named resources, at most **two**
  reservoirs over one fixed support can coexist.  Thus an exponential
  same-support packing cannot solve the full marked-lower problem.
* At owner/q1 scope there is no analogous scalar obstruction.  The exact
  upper-q1 capacity is of order `4^h/h^(3/2)`, a factor `sqrt(h)` larger
  than the desired `4^h/h^2` reservoir count.

Path-preserving avoidance at q1 scope is exactly a path problem in a
layered regular socket-state graph of degree `(h-1)!^2`.  This reduction
also exposes a sharp common-anchor obstruction: one forbidden endpoint
owner can delete every successor of a state.  Hence the earlier average
module-pruning estimate cannot simply be lifted to complete paths.

## 1. Fixed-support notation

Use the even-dimensional setup

\[
 k=2r,qquad h=d+1\ge2,qquad s=r-h-1.                    \tag{1.1}
\]

Fix

\[
 D=V\dot\cup\{\beta\},qquad |V|=2h,qquad
 G=[k]-D,qquad |G|=2s+1.                               \tag{1.2}
\]

A complete fixed-support reservoir has one length-`2h` alternating source
cycle for every

\[
                         X\in\binom Gs.                  \tag{1.3}
\]

Each such cycle uses every tag of `V` once, with `h` sources of type

\[
                         P_X(z)=X\cup\{z\}               \tag{1.4}
\]

and `h` sources of type

\[
                         H_X(z)=X\cup\{\beta,z\}.        \tag{1.5}
\]

The core order and tag order may vary between reservoirs.

## 2. Sharp same-support source cap

### Theorem 2.1 (two-reservoir source cap)

Let `R_1,...,R_t` be complete fixed-support reservoirs satisfying
(1.2)--(1.5).  If their named `P` source-target decks are pairwise
disjoint, then

\[
                              t\le2.                     \tag{2.1}
\]

The same conclusion follows from pairwise disjointness of their named `H`
source-target decks.

### Proof

Fix one core `X`.  There are exactly `2h` possible `P` targets over that
core,

\[
                         \{X\cup\{z\}:z\in V\}.          \tag{2.2}
\]

Every reservoir uses `h` distinct members of (2.2).  Pairwise deck
disjointness therefore requires `th<=2h`, proving (2.1).  For `H`, replace
each set in (2.2) by its union with `beta`.  \(\square\)

This is a sharp counting bound at the isolated source row: two reservoirs
could use complementary `P` tag halves.  The theorem does not assert that
all their owner/q1 sockets can simultaneously be made disjoint.

### Consequence

The desired same-support multiplicity is exponentially large,

\[
                         \Theta(4^h/h^2).                \tag{2.3}
\]

Theorem 2.1 rules this out as soon as the rank-`s+1` source targets are
protected literally.  Any same-support exponential packing is necessarily
an owner/q1-only device; its repeated source cells must be supplied by an
occurrence-multiplicity compiler or renamed through different supports.

## 3. Owner/q1 capacity does not rule out the target scale

Let

\[
                         M=\binom{2s+1}{s}.               \tag{3.1}
\]

Each projected Middle-Levels Hamilton path uses all `M` outside cores and
all but one of the `M` outside edge-union colours

\[
                         R\in\binom G{s+1}.              \tag{3.2}
\]

### Proposition 3.1 (upper-q1 capacity bound)

Suppose `t<M` complete fused reservoirs over the same fixed support have
pairwise disjoint upper-q1 decks.  Then

\[
                 \boxed{t\le {1\over2h}\binom{2h}{h}.}   \tag{3.3}
\]

### Proof

Each core path omits at most one colour in (3.2).  Since `t<M`, some `R`
is used by every path.  At the zipper on `R`, one reservoir has two seams
and exactly `h` upper-q1 transitions per seam.  Their private tag parts are
`2h` distinct `h`-subsets of `V`; the full targets are

\[
                         R\cup\{\beta\}\cup J,
                         \qquad J\in\binom Vh.            \tag{3.4}
\]

Pairwise disjointness across `t` reservoirs consumes `2ht` distinct
members of the `binom(2h,h)`-element palette, proving (3.3). \(\square\)

Stirling gives

\[
 {1\over2h}\binom{2h}{h}
      \sim {4^h\over2\sqrt\pi,h^{3/2}}.                \tag{3.5}
\]

This exceeds (2.3) by a factor of order `sqrt(h)`.  Thus q1 scalar capacity
does not block the proposed reservoir count.  The problem is correlated
path construction, not q1 cardinality.

The analogous per-`R` ledgers are:

\[
\begin{array}{c|c|c}
\text{row}&\text{private-tag rank}&\text{uses per reservoir}\ \hline
\text{mixed owner}&h-1&2(h-1)\\
\text{interior lower q1}&h-2&2(h-2)\\
\text{upper q1}&h&2h.
\end{array}                                               \tag{3.6}
\]

The upper row gives the cleanest necessary bound.

## 4. The exact socket-state graph

An oriented tag state is

\[
 \omega=(\mathbf A,\mathbf B,\epsilon),                 \tag{4.1}
\]

where

\[
 \mathbf A=(a_0,\ldots,a_{h-1}),\qquad
 \mathbf B=(b_0,\ldots,b_{h-1})                         \tag{4.2}
\]

are ordered disjoint `h`-tuples partitioning `V`, and `epsilon in Z_2` is
the `P/H` type at `a_0`.  Its incoming wrap socket is

\[
                         b_{h-1}\longrightarrow a_0,     \tag{4.3}
\]

and its outgoing midpoint socket is

\[
                         a_{h-1}\longrightarrow b_0.     \tag{4.4}
\]

Define `omega -> omega'` when

\[
\begin{aligned}
 a_{h-1}&=a'_0,& b_0&=b'_{h-1},\\
 A\cap A'&=\{a_{h-1}\},&B\cap B'&=\{b_0\},\\
 \epsilon'&=\epsilon+h&&\pmod2.                         \tag{4.5}
\end{aligned}
\]

These are exactly the tag and parity conditions of the core-change zipper.

### Lemma 4.1 (exact branching degree)

The directed socket graph is biregular of in- and out-degree

\[
                              D_h=(h-1)!^2.               \tag{4.6}
\]

### Proof

For fixed `omega`, (4.5) forces the unordered successor halves:

\[
\begin{aligned}
 A'&=\{a_{h-1}\}\cup(B-\{b_0\}),\\
 B'&=\{b_0\}\cup(A-\{a_{h-1}\}).                       \tag{4.7}
\end{aligned}
\]

The first element of `A'` and last element of `B'` are fixed.  The other
elements may be ordered in `(h-1)!` ways on each shore, and the phase is
fixed.  This proves the out-degree.  Reversing (4.5) proves the same
in-degree. \(\square\)

## 5. Exact layered avoidance equivalence

Fix one rainbow core path

\[
 X_0,R_0,X_1,\ldots,R_{M-2},X_{M-1}.                   \tag{5.1}
\]

Let `mathcal B` be an arbitrary forbidden bank of named owner/lower-q1/
upper-q1 resources.

Make a layered directed graph with one copy of the state set in every core
layer.  Delete a state in layer `i` if one of its pure block resources at
`X_i` belongs to `mathcal B`.  Retain a compatible edge

\[
                         \omega_i\longrightarrow\omega_{i+1} \tag{5.2}
\]

exactly when every resource generated by the two-seam zipper on `R_i`,
including its endpoint lower colours, avoids `mathcal B`.  Include the two
outer same-core boundary ledgers in the initial and terminal state tests.

### Theorem 5.1 (path-preserving redecoration criterion)

There is a complete fixed-support fused reservoir along (5.1), disjoint
from `mathcal B` at owner/q1 scope, if and only if the layered graph has a
directed path from layer zero to layer `M-1`.

### Proof

A compatible state sequence gives the incoming/outgoing sockets, unique
core-change zippers, and parity phases used in the sequential fusion proof.
Every final owner or q1 colour is either a pure block resource, a zipper
resource on exactly one `R_i`, or one of the two outer boundary resources.
The deletion rules therefore say precisely that the complete deck avoids
`mathcal B`.

Conversely, cut any such sequentially fused reservoir at its core-block
boundaries.  The ordered halves and source phases recover one state per
core; the one-repeated-tag condition recovers (4.5).  Deck disjointness
puts every state and transition in the retained layered graph. \(\square\)

This has an exact backward algorithm.  Let `S_(M-1)` be the terminal-safe
states and recursively put

\[
 S_i=\{\omega:\omega\text{ is pure-safe and }
       \exists\omega'\in S_{i+1}
       \text{ with a safe edge }\omega\to\omega'\}.      \tag{5.3}
\]

The desired reservoir exists exactly when `S_0` is nonempty.

## 6. Common-anchor obstruction

The factorial degree (4.6) does not by itself imply resilience.

Fix a state `omega` and an outside edge colour `R_i`.  At the seam from
`A` to its successor `A'`, the first mixed owner has the fixed value

\[
 R_i\cup\{\beta\}\cup(A-\{a_0\}).                      \tag{6.1}
\]

It is independent of all `(h-1)!^2` choices of successor ordering.  If
(6.1) lies in the forbidden bank, every outgoing transition from this
state is deleted.

Thus even one named target can kill the entire prospective menu of a
state.  An average forbidden-incidence estimate, including the existing
clustered-pruning expectation, cannot prove (5.3) without a statewise
anchor-spread or regeneration theorem.

There is nevertheless no density amplification at this first anchor gate.
Let `F subset binom(V,h-1)` be the forbidden private-tag anchors and call an
unordered half `A in binom(V,h)` dead when every one of its `h` facets lies
in `F`.

### Lemma 6.1 (anchor-shadow nonamplification)

If `mathcal D(F)` is the family of dead halves, then

\[
 { |\mathcal D(F)|\over\binom{2h}{h}}
 \le { |F|\over\binom{2h}{h-1}}.                        \tag{6.2}
\]

### Proof

Count incidences `(A,S)` with `A in mathcal D(F)`, `S in F`, and
`S subset A`.  Every dead `A` contributes `h` incidences.  Every
`(h-1)`-set lies in exactly `h+1` `h`-sets.  Hence

\[
 h|\mathcal D(F)|\le(h+1)|F|.
\]

Since

\[
 \binom{2h}{h}={h+1\over h}\binom{2h}{h-1},
\]

division gives (6.2). \(\square\)

Thus all orientations of one half may be killed, but the fraction of
halves killed is no larger than the forbidden-anchor density.  If `j`
previous q1 reservoirs occupy at most `2(h-1)j` owner anchors on a fixed
outside edge, then for

\[
                         j=O(4^h/h^2)                    \tag{6.3}
\]

only `O(h^(-1/2))` of the tag halves can be completely anchor-dead.
This is the correct local input for a future robust layered-routing
theorem.  It does not itself prevent a different sparse dead family at
each of the exponentially many core layers from cutting every full path.

For comparison, a uniformly random compatible transition on a fixed
`R` has the union-bound estimate

\[
 {2(h-1)|F_O|\over\binom{2h}{h-1}}
 +{2(h-2)|F_I|\over\binom{2h}{h-2}}
 +{2h|F_U|\over\binom{2h}{h}},                           \tag{6.4}
\]

where `F_O,F_I,F_U` are forbidden private-tag sets on the mixed owner,
interior lower, and upper q1 rows.  If (6.2) is below one, some locally safe
zipper exists.  Formula (6.1) explains why such one-edge existence does not
automatically concatenate through all `M` layers.

## 7. Exact finite calibration at `k=10,h=2`

A complete canonical census was run in O3 C++ on the H100.  It used one
fixed projected Hamilton cycle of `ML(5)`, the explicit cyclic-half socket
schedule, all `252` five-coordinate supports in `[10]`, and all five
choices of refreshed point per support: `1260` reservoirs and `793170`
unordered pairs.

The replay found:

```text
owner_disjoint_pairs=1452
fully_q1_disjoint_pairs=0
minimum_total_overlap=4 owner=0 lower=1 upper=3
```

Thus owner overlap is not a universal whole-reservoir obstruction, even at
the first calibration.  For this **specific canonical family**, however,
no pair has disjoint owner/lower/upper q1 decks.  This is a finite audit, not
an all-`h` no-go theorem; other Hamilton cycles and tag decorations were not
enumerated.

Artifacts:

* source:
  `scratch/audit_k10_h2_fused_reservoir_pair_overlap_20260802.cpp`, SHA
  `e3d3b44dc0d3b7cecf7131a83c3ea57638e317895543440344186d1f1869fb5e`;
* H100 root:
  `/home/amodo/or15/work/core_change_zipper_k10_pair_audit_20260802`;
* output:
  `scratch/k10_h2_fused_reservoir_pair_audit_20260802/audit.out`, SHA
  `5e9f33192bc7c3a54ddec21d73b0dfc1a8396b2e36a6fe3ca8d4ee3301faa028`.

## 8. Sharpened remaining theorem

Whole-reservoir packing now separates into two statements.

1. At full marked-lower scope, same-support packing is dead by Theorem 2.1;
   supports or literal occurrence roles must change.
2. At owner/q1 scope, prove that successive forbidden banks leave a path in
   (5.3).  The necessary new input is a hereditary anchor-spread theorem,
   not another aggregate collision expectation.

Even a positive q1 result would remain insufficient for the OR problem
until arbitrary-width upper witnesses and the occurrence-labelled lower
compiler are installed on the same chronology.
