# Even-depth all-high ring blocks: exact degrees, codegrees, and the absorption gate

## Status

For even trace depth `d`, the shortest state-balanced all-high ring has
`L=d+2` owners.  This note encodes those rings as a uniform hypergraph on
the complete rank-`r` owner shore of `[2r-1]` and computes its degree and
every higher codegree exactly.

The block hypergraph is regular, has an exact uniform fractional perfect
matching, and has pair-codegree ratio

\[
                         {d+1\over r(r-1)}.                    \tag{0.1}
\]

Thus there is no fractional owner separator and the local overlaps are
very small at triangular depth.  The note does not claim a perfect block
matching: exact or subexponential-leave absorption, divisibility repair,
integer pull histograms, and the cross-block named-target palette remain
open.

## 1. Ring blocks

Put

\[
                         n=2r-1,qquad L=d+2,qquad
                         c=r-d-1=r+1-L.                       \tag{1.1}
\]

Let

\[
                         \mathcal V=\binom{[n]}r,qquad
                         W=|\mathcal V|.                       \tag{1.2}
\]

For a pair

\[
                         K\subset H\subset[n],qquad
                         |K|=c,quad |H|=r+1,                  \tag{1.3}
\]

put `F=H-K`, so `|F|=L`, and define the owner block

\[
                         E(H,K)=\{H-\{f\}:f\in F\}.            \tag{1.4}
\]

This is exactly the owner set of the even-depth minimal all-high ring: put
the elements of `F` in any cyclic order and use common core `K`.  Every
length-`d+1=L-1` window omits one element of `F`.

Let `mathcal B_(r,d)` be the `L`-uniform hypergraph with vertex set
`mathcal V` and hyperedges (1.4).

There is a useful complementary description.  Put `G=[n]-H`, so
`|G|=r-2`.  Complementing every owner in (1.4) gives

\[
                         \{G\cup\{f\}:f\in F\}.                \tag{1.5}
\]

Thus the problem is equivalently to partition the rank-`r-1` layer into
`L`-edge stars with a common rank-`r-2` core.

## 2. Exact degree and edge count

### Theorem 2.1 (regularity)

Every owner vertex has degree

\[
 \boxed{
 D_1=(r-1)\binom r{d+1}.}                                   \tag{2.1}
\]

The total number of blocks is

\[
 |E(\mathcal B_{r,d})|
   =\binom{2r-1}{r+1}\binom{r+1}{d+2}
   ={W D_1\over L}.                                         \tag{2.2}
\]

#### Proof

Fix `T in binom([n],r)`.  If `T in E(H,K)`, then

\[
                         H=T\cup\{x\}                         \tag{2.3}
\]

for a unique `x notin T`, and the missing label `x` must lie in `F=H-K`.
Equivalently `K subset T`.  There are `r-1` choices of `x` and
`binom(r,c)=binom(r,d+1)` choices of `K`, proving (2.1).

Counting (1.3) first by `H` gives the first expression in (2.2).  The
second follows either from the identities

\[
 \binom{2r-1}{r+1}={r-1\over r+1}W,qquad
 \binom{r+1}{d+2}={r+1\over d+2}\binom r{d+1},                \tag{2.4}
\]

or by counting vertex--block incidences.  `square`

### Corollary 2.2 (exact fractional perfect matching)

Giving every block weight `1/D_1` is a fractional perfect matching of
`mathcal B_(r,d)`.

This is the exact owner-side fractional ring decomposition; no asymptotic
or random argument is involved.

## 3. Complete codegree sequence

### Theorem 3.1 (higher codegrees)

Let `T_1,...,T_s` be distinct owner vertices, with `s>=2`.  Their common
block codegree is zero unless they are distinct facets of one common
`(r+1)`-set `H`.  In the latter case it is

\[
 \boxed{
 d(T_1,\ldots,T_s)
   =\binom{r+1-s}{c}
   =\binom{r+1-s}{d+2-s}.}                                   \tag{3.1}
\]

In particular,

\[
 \Delta_2=\binom{r-1}d,qquad
 {\Delta_2\over D_1}={d+1\over r(r-1)}.                       \tag{3.2}
\]

For `s>d+2`, every `s`-codegree is zero.

#### Proof

Two distinct rank-`r` sets lie in one rank-`r+1` set exactly when their
intersection has rank `r-1`; in that case the common `H` is their union and
is unique.  If `s` distinct facets of `H` are used, let `f_i` be the label
missing from `T_i`.  A block `E(H,K)` contains them all exactly when

\[
                         K\subset H-\{f_1,\ldots,f_s\}.        \tag{3.3}
\]

The right side has size `r+1-s`, giving (3.1).  The second formula is its
complementary-binomial form.  At `s=2`, divide by (2.1) and use

\[
                         \binom r{d+1}
                          ={r\over d+1}\binom{r-1}d           \tag{3.4}
\]

to obtain (3.2).  If `s>L=d+2`, no `L`-edge block can contain the chosen
vertices.  `square`

At triangular depth `d=Theta(sqrt(r))`, (3.2) is `Theta(r^(-3/2))`.
More generally each additional prescribed facet costs another factor on
the order of `d/r` in (3.1), apart from the initial factor `1/r` coming
from the choice of the common upper set.

## 4. Exact orientation formulation

The star description (1.5) gives an equivalent modular orientation
problem.

### Proposition 4.1 (core-load formulation)

A perfect block matching in `mathcal B_(r,d)` is equivalent to choosing,
for every rank-`r-1` set `C`, one distinguished element `f(C) in C`, such
that for every rank-`r-2` core `G`, the set

\[
 \{f:C=G\cup\{f\},\ f(C)=f\}                                 \tag{4.1}
\]

has cardinality divisible by `L`; its elements are then partitioned into
`L`-sets.

#### Proof

Orient `C` toward the facet `G=C-{f(C)}`.  All vertices oriented to one
core have the form `G+f` with distinct extension labels `f`.  Grouping
these labels into `L`-sets gives precisely the complementary stars (1.5).
Conversely every selected star orients each of its vertices to its common
core.  Owner-disjointness says every `C` is oriented exactly once.  `square`

This formulation isolates the exact integrality issue: ordinary incidence
flow permits arbitrary integer core loads, whereas ring decomposition
requires every load to lie in `L Z`.

## 5. Divisibility and the remaining matching theorem

Every block has `L` vertices.  Therefore any matching leaves a number of
owners congruent to `W` modulo `L`; in particular a perfect block matching
requires

\[
                              L\mid W.                         \tag{5.1}
\]

This necessary condition fails in some dimensions, so a universal exact
construction must either mix ring lengths/types or retain a small residual
bank.  The block hypergraph itself gives no scalar obstruction beyond
(5.1): Corollary 2.2 is fractionally perfect.

The degree/codegree ledger is exceptionally favourable, but it is not by
itself an absorption theorem.  The precise next owner-side statement is:

> **Even ring-block absorption lemma.**  The hypergraph
> `mathcal B_(r,d)` has a matching leaving `2^{o(r)}` vertices (preferably
> `O(d)` vertices with the forced residue), and every bounded protected
> block bank can be retained.

A fixed-uniformity nibble theorem cannot be quoted without checking its
dependence on `L=d+2 -> infinity`.  Equations (2.1) and (3.1) are the exact
inputs for such a growing-uniformity theorem or for a direct absorber.

## 6. Pull decoration and named targets after owner matching

Once a block matching is selected, each `(H,K)` may be cyclically ordered
on `F=H-K`.  The literal pull-overlay theorem then allows core-coordinate
omission runs of length at most `d` without changing any owner in the
block.  Within one ordered block:

* every immediate-lower root is distinct;
* every fixed-width proper target is distinct; and
* integral omission runs realize the exact pull-clock staircase tiles.

The still-open rows are correlated across blocks:

1. choose integer pull histograms whose sum is the exact triangular rank
   demand;
2. choose cyclic orders so named targets do not collide between blocks and
   cover the prescribed palette rather than merely a same-size subset; and
3. join the block state cycles while preserving owners and marked targets.

Thus Theorems 2.1 and 3.1 remove owner-side scarcity and fractional Hall as
possible obstructions.  The first unresolved owner theorem is exact/near-
exact block absorption; after it, the surviving difficulty is the same
named-target/state correlation already isolated by the pull-clock work.

## 7. A large explicit block-free family

There is a useful warning against trying to obtain the required leave merely
from maximality.  The elementary independent-set bound has the correct order
of magnitude, up to a factor smaller than two.

Identify the ground set with `Z_n`, and colour every owner by

\[
                  \kappa(T)=\sum_{x\in T}x\pmod n.          \tag{7.1}
\]

### Theorem 7.1 (cyclic colour obstruction)

Every colour class in (7.1) has cardinality `W/n`.  The union of any
`L-1` colour classes is independent in `mathcal B_(r,d)`.  Consequently

\[
 \boxed{
   \alpha(\mathcal B_{r,d})\ge {L-1\over 2r-1}W.}           \tag{7.2}
\]

On the other hand every independent family `U` satisfies

\[
 \boxed{
   |U|\le {L-1\over r+1}W.}                                \tag{7.3}
\]

Thus, at triangular depth, the largest block-free families have size
`Theta(W/sqrt(r))` up to an absolute factor.

#### Proof

Translation by `t in Z_n` sends the colour of an owner to

\[
                         \kappa(T)+rt.                      \tag{7.4}
\]

Because `gcd(r,2r-1)=1`, translations act transitively on the `n`
colours.  Hence all colour classes have the same cardinality `W/n`.

Fix an `(r+1)`-set `H`.  Its `r+1` facets have colours

\[
                         \kappa(H)-f,\qquad f\in H,          \tag{7.5}
\]

and these colours are pairwise distinct.  A union of `L-1` colour classes
therefore contains at most `L-1` facets of every `H`, whereas a block is
made of `L` facets of one `H`.  This proves (7.2).

Conversely, if `U` is block-free, every `(r+1)`-set contains at most
`L-1` members of `U`.  Count containments `T subset H` with `T in U`:

\[
 |U|(r-1)
   \le (L-1)\binom{2r-1}{r+1}
   =(L-1){r-1\over r+1}W.                                  \tag{7.6}
\]

Cancel `r-1` to obtain (7.3). `square`

In particular, a maximal block matching only guarantees that its leave is
independent, and this fact alone cannot force a leave smaller than the
`W/sqrt(r)` scale.  Any subexponential or bounded leave theorem must use
augmenting structure or an exact design mechanism, not just maximality plus
the local degree ledger.

## 8. Relation to known delta-system decomposition theorems

A block is the partial simplex `F_(r,L)`: `L` rank-`r` facets of an
`(r+1)`-set.  Equivalently, after complementation, it is a delta-system
with core size `r-2` and `L` petals of size one.  Classical delta-system
decomposition theorems state sufficiency of the divisibility conditions
when the pattern parameters are fixed and the host order tends to infinity.
They do not cover the present diagonal regime

\[
             n=2r-1,\qquad L=d+2=\Theta(\sqrt r),           \tag{8.1}
\]

because the uniformity, core, and number of petals all grow with the host.
Thus those theorems corroborate that (5.1) is the right scalar condition,
but cannot be used as the missing absorption lemma without a new uniform
parameter estimate.

## 9. Exact complete-bipartite trades

Although the global matching theorem remains open, every individual block
has a completely explicit absorber of only `L(L-1)` owner vertices.  The
same construction gives an exact exchange between consecutive block sizes.

Work in the complemented rank-`(r-1)` layer.  Fix an `(r-3)`-set `S`, and
let `A,B` be disjoint subsets of `[n]-S`.  The owner family

\[
             \mathcal X(S;A,B)
                =\{S\cup\{a,b\}:a\in A,\ b\in B\}           \tag{9.1}
\]

is the edge set of the complete bipartite graph between `A` and `B`, with
the fixed core `S` adjoined.  It has the two star decompositions

\[
 \begin{aligned}
 \mathcal D_A
   &=\bigl\{\{S+a+b:b\in B\}:a\in A\bigr\},\\
 \mathcal D_B
   &=\bigl\{\{S+a+b:a\in A\}:b\in B\bigr\}.
 \end{aligned}                                             \tag{9.2}
\]

### Theorem 9.1 (absorber for every `L`-block)

Assume `2L<=r+2`.  Let

\[
                    e=\{G+b:b\in B\},\qquad |B|=L,          \tag{9.3}
\]

be any block in the complemented model, where `|G|=r-2` and
`B subset [n]-G`.  There is an owner set `A_e`, disjoint from `e`, such
that both `A_e` and `A_e union e` decompose into `L`-blocks.  Explicitly,

\[
                         |A_e|=L(L-1).                       \tag{9.4}
\]

For every choice of `a in G`, there are

\[
                  \binom{r+1-L}{L-1}                        \tag{9.5}
\]

such labelled absorbers obtained from that anchor.

#### Proof

Put `S=G-{a}`.  Choose an `(L-1)`-set

\[
             A'\subset[n]-(G\cup B),                        \tag{9.6}
\]

and put `A={a} union A'`.  The complement in (9.6) has size

\[
        (2r-1)-(r-2)-L=r+1-L,                               \tag{9.7}
\]

so the choice is possible precisely under the displayed numerical
hypothesis, and (9.5) counts it.

Apply (9.2) to `mathcal X(S;A,B)`.  The member of `mathcal D_A` centred at
`a` is exactly `e`.  Hence

\[
 A_e=\mathcal X(S;A,B)-e                                    \tag{9.8}
\]

is tiled by the other `L-1` members of `mathcal D_A`, whereas
`A_e union e=mathcal X(S;A,B)` is tiled by all `L` members of
`mathcal D_B`.  The size in (9.4) is immediate. `square`

Thus the missing absorption theorem is not blocked by the absence of local
switches: every prospective block has many exact private absorbers.  The
unproved part is to reserve a globally disjoint absorber bank and then
cover the eventual owner leave by absorbable blocks.

### Theorem 9.2 (consecutive-size conversion)

Assume `2L<=r+1`.  Taking `|A|=L` and `|B|=L+1` in (9.1) gives the exact
trade

\[
 \boxed{
   (L+1)\text{ blocks of size }L
       \quad\longleftrightarrow\quad
   L\text{ blocks of size }L+1.}                            \tag{9.9}
\]

Both sides cover exactly the same `L(L+1)` owners.

#### Proof

The `B`-centred decomposition in (9.2) has `L+1` stars, each with `L`
leaves.  The `A`-centred decomposition has `L` stars, each with `L+1`
leaves.  The ground-set condition is

\[
                     |S|+|A|+|B|=r-3+2L+1\le2r-1.          \tag{9.10}
\]

This is equivalent to `2L<=r+1`. `square`

Equation (9.9) is the local integral version of the consecutive-size coin
repair: it changes the number of size-`L` blocks by `L+1` and the number of
size-`(L+1)` blocks by `-L` without changing a single owner.  It is an
owner-side theorem.  To use it in the OR construction one must additionally
choose the two source-state realizations so that their marked lower targets
and boundary states agree; that decorated lift is not asserted here.

### Theorem 9.3 (the bare absorber is maximally lower-visible)

Take `|A|=|B|=L` and put

\[
                       R=[n]-S,\qquad C=R-(A\cup B).         \tag{9.11}
\]

Give `A` and `B` arbitrary cyclic orders.  Realize every star in the two
decompositions (9.2) as its all-high source ring.  At every proper source
width `1<=q<=L-2`, the `A`-centred decomposition emits the target family

\[
 \mathcal P_A(q)=
  \{C\cup(A-\{a\})\cup I:
       a\in A,\ I\text{ a cyclic }q\text{-interval of }B\}, \tag{9.12}
\]

whereas the `B`-centred decomposition emits

\[
 \mathcal P_B(q)=
  \{C\cup(B-\{b\})\cup J:
       b\in B,\ J\text{ a cyclic }q\text{-interval of }A\}. \tag{9.13}
\]

Both families have `L^2` distinct members, and they are disjoint.  Hence
the switch has strict-lower symmetric difference exactly

\[
                         2L^2                              \tag{9.14}
\]

at every one of those widths.  At owner width `q=L-1`, the two families
coincide and equal

\[
                         \{R-\{a,b\}:a\in A,b\in B\}.       \tag{9.15}
\]

#### Proof

For the star centred at `S+a`, the original (uncomplemented) ring has
private set `B` and common source core

\[
                         C\cup(A-\{a\}),                    \tag{9.16}
\]

which gives (9.12).  The other orientation gives (9.13).

Within (9.12), the intersection with `A` recovers the unique missing
element `a`, and the intersection with `B` recovers `I`; hence all `L^2`
targets are distinct.  The same holds on the other shore.

The complement in `R` of a member of (9.12) contains exactly one element
of `A` and `L-q` elements of `B`.  For (9.13) the two numbers are
`L-q` and one.  They can agree only when `L-q=1`, which is excluded for
`q<=L-2`.  This proves disjointness and (9.14).  At `q=L-1`, write the
intervals as `B-{b}` and `A-{a}`; both formulas become `R-{a,b}`, proving
(9.15). `square`

Thus the complete-bipartite absorber is perfect on owners but not a free
literal absorber.  Any successful decorated use must price or cancel
`Theta(L^2)` named targets at each lower width.  This is precisely why the
global pull histogram and target assignment must be chosen together with
the owner cover-down.

## 10. A state-balanced diagonal decoration of the trade

The negative conclusion of Theorem 9.3 concerns the bare all-high source.
There is a different pull decoration which preserves an exact linear bank
of named targets at every depth.

Write

\[
 A=\{a_0,\ldots,a_{L-1}\},\qquad
 B=\{b_0,\ldots,b_{L-1}\},                                \tag{10.1}
\]

with cyclic subscripts.  For the `A`-centred star indexed by `i`, use the
source word

\[
 X^{A,i}_t
   =C\cup\bigl(\{a_t,a_{t+1}\}-\{a_i\}\bigr)\cup\{b_t\},
             \qquad t\in\mathbb Z_L.                       \tag{10.2}
\]

For the `B`-centred star indexed by `i`, use the transposed word

\[
 X^{B,i}_t
   =C\cup\bigl(\{b_t,b_{t+1}\}-\{b_i\}\bigr)\cup\{a_t\}.
                                                                    \tag{10.3}
\]

These are pull overlays of the all-high rings.  In (10.2), a core
coordinate `a_j != a_i` is present only at phases `j-1,j`; its omission
set is the complementary cyclic interval of length `L-2=d`.  Thus every
omission component has the maximal legal length `d`.  The description of
(10.3) is symmetric.

### Theorem 10.1 (diagonal protected bank)

The `L` words (10.2), and separately the `L` words (10.3), have the
following properties.

1. Every word is a literal state-balanced depth-`d` cycle.
2. Across the `L` words, the owner windows are exactly once each the
   `L^2` sets

   \[
                         R-\{a_i,b_j\},qquad i,j\in Z_L.    \tag{10.4}
   \]

   Hence the two shores have the same owner inventory.
3. For every proper width `1<=q<=d` and every `t in Z_L`, both shores
   contain the same named target

   \[
     \boxed{
       P_{q,t}=C\cup\{a_t,\ldots,a_{t+q-1}\}
                  \cup\{b_t,\ldots,b_{t+q-1}\}.}           \tag{10.5}
   \]

   On the `A` shore it occurs in ring `i=t+q`, and on the `B` shore it
   occurs in ring `i=t+q`.
4. The `Ld` targets in (10.5) are pairwise distinct.  Their ranks are

   \[
                         |P_{q,t}|=|C|+2q.                  \tag{10.6}
   \]

Thus the complete-bipartite owner switch has a literal, state-balanced
lift preserving a protected bank of `L` occurrence-labelled lower targets
at every depth.

#### Proof

Consider (10.2).  Any length-`L-1=d+1` owner window omits only one source
phase.  The two supporting phases `j-1,j` of a core coordinate `a_j` cannot
both be omitted, so every `a_j != a_i` occurs in the owner.  Exactly one
private `b` label is absent.  The owner is therefore

\[
             C\cup(A-\{a_i\})\cup(B-\{b_j\})
                =R-\{a_i,b_j\},                            \tag{10.7}
\]

and the `L` windows give all `j`.  Varying `i` proves (10.4); the transpose
proves the same statement for (10.3).  The omission runs have length at
most `d`, so Theorem 6.1 gives literal owner validity and state balance.

A width-`q` interval beginning at `t` in (10.2) contains the private
`B`-interval `b_t,...,b_(t+q-1)`.  Its surviving `A`-core contribution is

\[
                   \{a_t,\ldots,a_{t+q}\}-\{a_i\}.         \tag{10.8}
\]

Choosing `i=t+q` turns (10.8) into the `A`-interval in (10.5).  The
transposed calculation for (10.3) is identical.  This proves the common
occurrences.

For fixed `q<L`, either cyclic interval in (10.5) recovers `t`.  Different
values of `q` have different ranks by (10.6).  Hence all marked targets are
distinct. `square`

### Remaining visibility

Theorem 10.1 does not make the whole switch transparent.  It protects only
one diagonal occurrence per ring and width; the other proper windows still
change.  Moreover, consecutive owners in an `A`-centred ring have the
common upper set `R-{a_i}`, whereas the transposed rings use `R-{b_i}`.
Thus the two q1-upper inventories are oppositely polarized.  A global use
of this actuator still needs either a paired polarization cancellation or
an upper palette with those occurrences left uncommitted.

What has improved is the literal interface: the owner absorber no longer
has zero protected lower supply.  It carries an exact all-depth diagonal
bank of size `Ld=Theta(d^2)` while preserving owner one-copy and state
balance.
