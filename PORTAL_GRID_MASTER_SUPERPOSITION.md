# Portal-grid master superposition and the monotone-fork obstruction

## 1. Status

Write

\[
 \mathcal T_R=\{P_0=(0,0)\}\cup
 \{E_{s,y}=(s,y):1\le s\le R,\ 0\le y<s\},
 \qquad P_s=E_{s,0}.
\]

The target indexed by `(u,r,x)` is the rectangle

\[
                 [u,r]\times[0,x],
 \qquad 0\le u<r\le R,\quad 0\le x<r.       \tag{1.1}
\]

The explicit portal gadget in `NONCANONICAL_TRIANGULAR_BRAID.md` uses, to
the right of `P_u`, the word

\[
 Q_u=E_{u,2},\ldots,E_{u,u-1},D_u,D_{u+1},\ldots,D_{R-1},
 \qquad D_t=E_{t+1,t}.                         \tag{1.2}
\]

Taken literally, the diagonal suffix in (1.2) is copied for every `u` and
therefore has quadratic multiplicity.  The first theorem below proves that
none of these copies is necessary: **all right arms superpose in one word,
with every triangular letter used at most once.**  The intermediate row
blocks are harmless fillers, rather than contaminants.

There is a dual one-copy master for all height-one left arms.  However, the
two masters order their distinguished peak portals oppositely.  Theorems 3
and 4 prove a sharp obstruction to the naive cure: if one fixes the portal
occurrences in either monotone order and asks the other side of every grid
to attach at those same occurrences, then the required low-layer provider
occurrences are quadratic.  Thus a subquadratic construction cannot be a
serial gluing of the two master braids.  It must assign different targets
to different portals in a genuinely nonmonotone or recursively interleaved
fashion.

This note does **not** construct the still-missing subquadratic braid.  It
removes the apparent diagonal-copying obstruction completely and identifies
the next obstruction precisely.

The finite audit `scratch/verify_portal_master_superposition.py` independently
checks Theorems 1 and 2 for every `2<=R<=100`, including all boundary cases
and the exact once-only inventory of `Q_R`.

## 2. One master word contains every right arm

For `0<=v<=R`, define

\[
 B_v=P_v,E_{v,2},E_{v,3},\ldots,E_{v,v-1},       \tag{2.1}
\]

where the positive part is empty for `v<=2`.  Put

\[
                    \mathcal Q_R=B_0B_1\cdots B_R.  \tag{2.2}
\]

The column-one cells `E_(v,1)` are deliberately absent.  Apart from those
cells, (2.2) uses every peak once and every cell of height at least two
once.

### Theorem 1 (right-arm master)

Fix `0<=u<R` and `2<=x<R`.  In `Q_R`, the interval beginning at the
distinguished occurrence of `P_u` and ending at

\[
 H_{u,x}=\begin{cases}
 E_{u,x},&x<u,\\
 D_x=E_{x+1,x},&x\ge u
 \end{cases}                                      \tag{2.3}
\]

has bounding box

\[
 [u,\max\{u,x+1\}]\times[0,x].                    \tag{2.4}
\]

Consequently, if a clean interval ending at that `P_u` has box

\[
                         [u,r]\times[0,1]           \tag{2.5}
\]

for some `r>x`, then adjoining the interval (2.3) gives exactly the target
`[u,r]x[0,x]`.

#### Proof

If `x<u`, the relevant interval stays inside `B_u`:

\[
                     P_u,E_{u,2},\ldots,E_{u,x}.
\]

Its first coordinate is constantly `u`, while its heights have minimum zero
and maximum `x`.  This gives (2.4).

Suppose `x>=u`.  The interval is

\[
 P_u,E_{u,2},\ldots,E_{u,u-1},
 B_{u+1},B_{u+2},\ldots,B_x,
 P_{x+1},E_{x+1,2},\ldots,E_{x+1,x}.               \tag{2.6}
\]

Every letter in a block `B_v` has first coordinate `v` and height at most
`v-1`.  Throughout (2.6),

\[
 u\le v\le x+1,
 \qquad 0\le y\le v-1\le x.                       \tag{2.7}
\]

The first letter supplies first-coordinate minimum `u` and height minimum
zero; the last letter supplies first-coordinate maximum `x+1` and height
maximum `x`.  This proves (2.4).  Since validity gives `x+1<=r`, the join of
(2.4) and (2.5) is `[u,r]x[0,x]`.  QED.

### Interpretation

For fixed `u`, the original `Q_u` is one especially sparse path.  The master
word replaces its diagonal step from `D_t` to `D_(t+1)` by the entire block

\[
                         B_{t+1}.                    \tag{2.8}
\]

Every inserted letter lies in every target that uses that step.  The
quadratically repeated diagonal suffixes in the literal `G_u` concatenation
were therefore an artefact of insisting on an induced path rather than a
contamination-free path.

## 3. One master word contains every left height-one arm

Put `C_s=E_(s,1)` for `2<=s<=R`, and define

\[
 \mathcal L_R=
 C_R,P_{R-1},C_{R-1},P_{R-2},\ldots,C_2,P_1,P_0.   \tag{3.1}
\]

### Theorem 2 (left-arm master)

For every `0<=u<r<=R` with `r>=2`, the interval of `L_R` beginning at
`C_r` and ending at `P_u` has box

\[
                         [u,r]\times[0,1].           \tag{3.2}
\]

#### Proof

The interval is

\[
 C_r,P_{r-1},C_{r-1},P_{r-2},\ldots,C_{u+1},P_u,   \tag{3.3}
\]

with the evident final `P_1,P_0` convention at `u=0`.  Every first
coordinate lies between `u` and `r`; `P_u` and `C_r` attain the two extrema.
All heights are zero or one and at least one `C` occurs.  QED.

Thus the left arms and right arms separately admit zero-waste master
superpositions.  Their distinguished peak orders are opposite:

\[
 \mathcal L_R:\quad P_{R-1},P_{R-2},\ldots,P_0,
 \qquad
 \mathcal Q_R:\quad P_0,P_1,\ldots,P_R.            \tag{3.4}
\]

The issue is not coverage on either side.  It is placing both clean sides
around sufficiently many common physical portals.

## 4. Increasing right portals force quadratic left providers

The following theorem is deliberately stated at the exact level needed to
rule out serial attachment to (2.2).

### Theorem 3 (increasing-portal fork obstruction)

Let `W` be a word over `T_R`.  Suppose it has distinguished occurrences
`p_0<p_1<...<p_(R-1)`, with the letter at `p_u` equal to `P_u`.  Suppose
also that, for every `u<r<=R` with `r>=2`, the target

\[
                         [u,r]\times[0,1]            \tag{4.1}
\]

has a witnessing interval **ending at `p_u`**.

Then the pairwise disjoint gaps

\[
                         (p_{u-1},p_u]
 \qquad(1\le u\le R-1)                              \tag{4.2}
\]

contain at least

\[
                  \sum_{u=1}^{R-1}(R-u)
                  ={R(R-1)\over2}                   \tag{4.3}
\]

occurrences of height-zero or height-one letters.  More precisely, gap `u`
contains a letter of first coordinate `r` for every `r=u+1,...,R`.

Since the triangular alphabet has only `2R` height-at-most-one labels, this
architecture has `Omega(R^2)` repeated low-layer occurrences.

#### Proof

Fix `u>=1`.  The occurrence `p_(u-1)` has first coordinate `u-1`.  Hence an
interval ending at `p_u` whose first-coordinate minimum is `u` must begin
strictly after `p_(u-1)` (indeed, after the last earlier letter of first
coordinate below `u`).

For each `r>u`, a witness for (4.1) must contain some letter whose first
coordinate is `r`.  Its maximum height is one, so that provider has height
zero or one.  It lies in `(p_(u-1),p_u]`.  Distinct values of `r` require
distinct physical occurrences.  Thus gap `u` contains at least `R-u` such
letters.  The gaps are disjoint, so summation proves (4.3).

There are `R+1` peak labels and `R-1` column-one labels, hence `2R`
height-at-most-one labels in `T_R`.  All occurrences beyond the first copy
of these labels are repetitions.  QED.

The exact right-arm master (2.2) has its distinguished `P_u` occurrences in
the increasing order assumed here.  Therefore attaching every left grid at
those same portal roots cannot have subquadratic excess.

## 5. Decreasing left portals force quadratic right providers

There is a symmetric obstruction when one first commits to the order in
the left-arm master.

### Theorem 4 (decreasing-portal fork obstruction)

Let `W` contain distinguished peak occurrences in the order

\[
             p_{R-1}<p_{R-2}<\cdots<p_1<p_0,
 \qquad W[p_u]=P_u.                                 \tag{5.1}
\]

Suppose that for every `1<=u<=R-1` and every `2<=x<=R-1`, the target

\[
                         [u,R]\times[0,x]            \tag{5.2}
\]

has a witnessing interval **beginning at `p_u`**.

Then every gap `[p_u,p_(u-1))` contains a letter of height `x` for each
`x=2,...,R-1`.  Consequently these disjoint gaps contain at least

\[
                         (R-1)(R-2)                  \tag{5.3}
\]

positive-height occurrences.  Moreover, if the attached arm uses the
literal providers from (1.2), then the subfamily `u<=x` alone forces
quadratic multiplicity among the `R-1` diagonal labels `D_x`.

#### Proof

The next distinguished peak after `p_u` is `P_(u-1)`, whose first coordinate
is below `u`.  Hence every witness beginning at `p_u` and having minimum
first coordinate `u` must end before `p_(u-1)`.

For each `x`, a witness for (5.2) must contain a letter of height exactly
`x`; otherwise its maximum height is not `x`.  These providers are distinct
for distinct `x` and lie in `[p_u,p_(u-1))`.  Summing over the `R-1`
disjoint gaps proves (5.3).

For the literal arm (1.2), restrict to `x>=max(2,u)`.  Its prescribed
height provider is `D_x`.  The disjoint gap for `u` must therefore contain
one occurrence of every such `D_x`.  The number of required occurrences is

\[
 \sum_{u=1}^{R-1}\bigl(R-\max\{2,u\}\bigr)
                       =\Theta(R^2),                 \tag{5.4}
\]

drawn from only `R-2` diagonal labels.  Hence all but `O(R)` of them are
repetitions.  QED.

The broad occurrence count (5.3) alone need not be excess, because the full
triangle has `Theta(R^2)` positive-height labels.  The conclusion relevant
to the explicit `G_u` packing is the last sentence: retaining its common
diagonal providers in serial decreasing portal gaps forces quadratic
repetition of a linear label family.

## 6. Consequence for the recursive search

Theorems 1 and 2 solve both one-sided packing problems exactly.  Theorems 3
and 4 show why their obvious identification fails:

\[
 \boxed{
 \begin{array}{c}
 \text{increasing portals make all }Q_u\text{ shareable, but}\\
 \text{force quadratic left-provider multiplicity;}\\[2mm]
 \text{decreasing portals make all }L_u\text{ shareable, but}\\
 \text{force quadratic literal diagonal multiplicity.}
 \end{array}}
                                                               \tag{6.1}
\]

Therefore a successful `|T_R|+O(R log R)` or more generally subquadratic-
excess construction must abandon at least one of the following two rules:

1. one distinguished portal occurrence `P_u` handles every target with
   lower endpoint `u`;
2. the distinguished portals occur in one global monotone order.

Equivalently, targets must be distributed among a nonmonotone hierarchy of
portals, so that a portal's two nested chains vary both lower/upper endpoint
data and height data.  This is the precise point at which a balanced fold or
divide-and-conquer construction must enter.  Merely concatenating or
overlapping the explicit `G_u` strings cannot achieve the required bound.

## 7. Exact audit of the cross-paired Euler splice

There is a tempting way to try to evade (6.1).  Regard the two master words
as paths meeting at the peak labels and take an Euler traversal of their
union.  The local geometry of that traversal can be described exactly.

For `1<=u<R`, put

\[
 A_u=(E_{u,2},E_{u,3},\ldots,E_{u,u-1})              \tag{7.1}
\]

and form the elementary circuit

\[
 K_u=P_u,A_u,P_{u+1},C_{u+1},P_u.                   \tag{7.2}
\]

The empty-arm convention is used at `u=1,2`.  Its first half is the step
from `B_u` to `B_(u+1)` in the right master, and its second half is the
corresponding return step in the left master.  The circuits `K_u` form a
chain cactus: `K_(u-1)` and `K_u` meet only at `P_u`.

### Lemma 5 (a good fork is the isolating Euler pairing)

At an internal articulation `P_u`, the local Euler transition

\[
             C_{u+1}\longrightarrow P_u
             \longrightarrow A_u                 \tag{7.3}
\]

is precisely the transition that puts the clean left arm immediately before
the right arm for lower endpoint `u`.  If (7.3) is one of the two transition
pairs at `P_u`, the other pair also stays within `K_(u-1)`.  Hence the local
transition system does not join the two cactus circuits at `P_u`.

Conversely, every Euler transition system that joins `K_(u-1)` and `K_u`
at `P_u` cross-pairs both visits and destroys (7.3).

#### Proof

There are four incident half-edges at `P_u`: two belonging to `K_(u-1)` and
two belonging to `K_u`.  Transition (7.3) pairs the two half-edges of
`K_u`.  The only two remaining half-edges both belong to `K_(u-1)`, so they
are paired together.  Thus neither transition crosses between circuits.

If the circuits are joined, at least one pair is cross-circuit.  With four
half-edges and a perfect pairing, the remaining pair is then cross-circuit
as well, so the within-`K_u` pair (7.3) is absent.  QED.

### Corollary 6 (one-copy Euler traversal cannot retain the portal forks)

An Euler circuit using every edge of the chain cactus once must cross-pair
at every internal articulation.  It therefore retains none of the internal
forks (7.3).  Pairing every fork correctly instead decomposes the transition
system into the separate elementary circuits `K_u`.

Thus ordinary Hierholzer splicing is not the missing construction: its exact
connectivity operation is the operation that breaks the desired local
portal.

One can preserve the within-circuit pairings by adding a second occurrence
of `P_u` and concatenating two circuits through a new `P_uP_u` connector.
That uses only `O(R)` repeated peaks, so there is no *topological* obstacle.
There is, however, an exact contamination obstacle.

### Lemma 7 (box of an atomic Euler detour)

For `u>=3`, traversing the whole circuit `K_u` forces the bounding box

\[
                         [u,u+1]\times[0,u-1].       \tag{7.4}
\]

Consequently a target interval `[a,r]x[0,x]` may contain `K_u` as an
intermediate atomic detour only if

\[
                         a\le u,
 \qquad u+1\le r,
 \qquad u-1\le x.                                  \tag{7.5}
\]

There is also an intra-arm version: after an interval has reached
`E_(u,x)` with `x<u-1`, it cannot continue through the remainder of `A_u`
without increasing its height maximum above `x`.

#### Proof

Circuit `K_u` contains the two peaks `P_u,P_(u+1)`, the column cell
`C_(u+1)`, and every `E_(u,y)` for `2<=y<u`.  These letters attain first
coordinates `u,u+1`, height minimum zero, and height maximum `u-1`, proving
(7.4).  Containment in a target box gives (7.5).  The final assertion follows
because the next arm letter is `E_(u,x+1)`.  QED.

This identifies the failure seen in the fully nested Euler word.  Nesting
`K_(u+1),K_(u+2),...` inside `K_u` produces exactly the harmless right-arm
fillers only until the requested height is attained.  Returning later to a
farther left provider necessarily crosses either the unused high tail of
`A_u` or a complete circuit `K_v` with `v-1>x`; that detour contaminates the
target.

### Proposition 8 (assigned atomic-circuit serializations fail at height two)

Suppose the circuits `K_4,...,K_(R-1)` and a block containing a row-`R`
provider are serialized as atomic blocks, without interleaving their
interiors.  Assume additionally that the proposed witness for
`[u,R]x[0,2]` takes its distinguished lower-endpoint occurrence from its
assigned circuit `K_(u-1)` or `K_u`, rather than from a separately inserted
peak corridor.  Delete the low circuits `K_1,K_2,K_3` from this block order.
A height-two target can cross no remaining complete circuit by Lemma 7.
Hence its assigned lower-endpoint block and the row-`R` provider block must
be consecutive in the induced high-block order.

In particular, the row-`R` block has at most two high-block neighbours, so
such an atomic serialization cannot cover `[u,R]x[0,2]` from distinct
lower-endpoint blocks for more than two values of `u>=4`.

#### Proof

Every intermediate high block is some complete `K_v` with `v>=4`, whose
height maximum is `v-1>=3`; it cannot lie inside a height-two witness.  Low
blocks may lie between the endpoints without violating the height bound, so
deleting them gives the stated necessary adjacency.  A vertex in a linear
block order has at most two neighbours.  QED.

Proposition 8 is intentionally scoped.  A separate ascending peak corridor
followed by `E_(R,2)` evades it for the height-two layer, so the proposition
is not an unrestricted lower bound against all `O(R)` peak duplication.
It does rule out the most literal cross-paired repair, in which each atomic
cycle is expected to supply its own portal.  A successful balanced splice
must either split the interiors of the `K_u` across recursion levels or add
separate provider corridors and prove that those corridors are shared across
unboundedly many height layers.

## 8. Cartesian-tree form of the balanced-splice problem

The obstruction is not limited to monotone portal orders.  There is an exact
laminar description for an arbitrary order of one distinguished occurrence
of each `P_u`.

Read the distinguished peak labels in physical order as a permutation
`pi`.  For the occurrence of `P_u`, let `lambda_u` and `rho_u` be the nearest
distinguished peak occurrences on its left and right, respectively, whose
labels are smaller than `u`; use word boundaries when one does not exist.
Put

\[
                         N_u=(\lambda_u,\rho_u).      \tag{8.1}
\]

### Lemma 9 (nearest-smaller barrier)

Every interval containing the distinguished `P_u` and having first-
coordinate minimum `u` is contained in `N_u`.  The family of portal spans
`N_u` is laminar; it is exactly the family of subtree intervals of the
min-Cartesian tree of `pi`.

#### Proof

Crossing either endpoint in (8.1) includes a distinguished peak with label
below `u`, contradicting the required minimum.  The standard recursive
description of a min-Cartesian tree takes the minimum permutation label as
root and recurses on the portions to its left and right.  Its node-subtree
interval is precisely the interval between the nearest smaller labels on
the two sides.  Subtree intervals are laminar.  QED.

Consequently, if one physical provider occurrence is used by several
distinguished portals, all their spans contain that occurrence and hence
the corresponding Cartesian-tree nodes lie on one ancestor chain.  This
gives a clean quantitative bound under the direct single-portal rules.

### Proposition 10 (bounded-depth balanced forks remain expensive)

Assume the Cartesian tree has depth at most `h`.  Assume, for every `u`
with `1<=u<R`, that the distinguished `P_u` is required to support, for
every `r>u`, a left-ending height-one witness using a provider of first
coordinate `r`.

Then the word contains at least

\[
 {1\over h}\sum_{u=1}^{R-1}(R-u)
 ={R(R-1)\over2h}                                   \tag{8.2}
\]

height-at-most-one provider occurrences, counted with multiplicity.  Since
there are only `2R` such alphabet labels, at least

\[
                         {R(R-1)\over2h}-2R          \tag{8.3}
\]

are repetitions.  In particular, a balanced portal order of depth
`O(log R)` still costs `Omega(R^2/log R)` excess under the direct `G_u`
assignment; it cannot give `|T_R|+O(R log R)` merely by reordering the
portal roots.

#### Proof

Count requirement--provider incidences.  The displayed family gives the
numerator in (8.2).  A single physical provider occurrence can serve a
portal only if it lies in that portal's span `N_u`.  By Lemma 9, all nodes
whose spans contain one fixed position form an ancestor chain, of size at
most `h`.  One provider has one first-coordinate value, so for each node it
discharges at most one counted requirement.  Thus one occurrence discharges
at most `h` requirements.  Division proves (8.2), and subtracting the `2R`
distinct low-layer labels gives (8.3).  QED.

This proposition is again architectural, not an unrestricted repetition
lower bound: nonliteral height providers and multiple portals for one lower
endpoint can evade its hypotheses.  Its conclusion is nevertheless sharp
for the proposed balanced superposition of the explicit grids.  A genuine
subquadratic construction must use the full two-chain-grid freedom: the
same portal must serve many lower endpoints, or one lower endpoint's targets
must be split among portals, rather than retaining one root `P_u` per `G_u`.
