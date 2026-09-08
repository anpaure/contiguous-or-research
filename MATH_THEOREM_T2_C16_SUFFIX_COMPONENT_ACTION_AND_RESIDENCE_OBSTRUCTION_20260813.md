# The tensorable `T2` `C16` is an eight-component suffix matching, not a resident spanning hypertree

**Date:** 2026-08-13
**Status:** unconditional component-action theorem, exact compatible-selection
theorem, and exact residence/spanning obstruction.  One of the two `C16`s
over each aligned suffix edge is a conflict-free eight-way component merge.
The resulting bank is only a matching of the Dyck suffix graph, and every
nonempty local choice fails the undilated `2`-residence collar test.  A
common-history lift remains possible only after a residence-dilated,
cut-separated occurrence planting; that planting is not supplied here.

## 0. Outcome

Let the even prefix ground have size `2m`, let

\[
                         k=2m+1,
\]

and apply the exact two-hex `T2` packet at every Dyck suffix of
semilength `m-6`.  Close the resulting open incidence forest with the
fixed complemented return and endpoint verticals in `ML(2m+1)`.

For each `W in D_(m-8)`, the two certified `C16`s over

```text
                         1100W  <->  1010W
```

have the following exact action.

1. Either `C16` meets eight distinct post-`T2` components and merges them
   into one component of `16k` vertices on either middle-level shore.
2. The `b=4` and `b=6` trades over the same `W` share exactly the two
   post-`T2` components belonging to `1100W` and `1010W`.  Their other
   twelve component vertices are distinct.  Thus their component--trade
   incidence graph contains a literal four-cycle.  Toggling both produces
   two components, of shore lengths `9k` and `13k`, rather than one.
3. Blocks belonging to distinct words `W` are component-disjoint.  Hence
   choosing at most one of `b=4,6` for each `W` is conflict-free and is the
   maximal hypertree-compatible selection from this bank.
4. On either projected owner chronology the eight new seams of one switch
   have cyclic gap multiset

   \[
                           \{k^6,(5k)^2\}.                 \tag{0.1}
   \]

   Separation is therefore abundant.  Nevertheless a literal new seam
   already fails the `q=2` transition-collar test.  On the rank-`m+1`
   (`q1`-colour) projection the failure is a zero-run singleton; on the
   rank-`m` (`T2`-owner) projection it is a positive-run singleton.  Thus
   neither `C16`, nor their simultaneous toggle, is directly
   `q`-biresident for any `q>=2`.
5. The available suffix edges form the matching

   \[
        \mathcal M_s=\{\{1100W,1010W\}:W\in\mathcal D_{s-2}\}          \tag{0.2}
   \]

   in the Johnson graph induced by `D_s`.  It spans `D_2`, but for every
   `s>=3` it covers only `2 Cat_(s-2)<Cat_s` suffix vertices.  It cannot
   contain a spanning tree, and the associated component trades cannot
   form a spanning flip hypertree.

The sharp remaining gate is therefore not a choice between the two local
`C16`s.  One needs additional suffix-edge templates connecting the
uncovered Dyck roots, together with a residence dilation or a
cut-separated common-history planting that removes the singleton collars.
For the original-owner source hierarchy that planting must also be
turn-faithful for the selected `q2` current and repair the nonneutral
rank-`m-1` intersection palette.

## 1. Full lifted factor and canonical component labels

Let `E_0` be the canonical semilength-`m` MSW incidence forest between
rank `m` and rank `m+1` subsets of `[2m]`.  For any incidence forest `E`
with the same rank-`m` endpoints, let `H(E)` contain:

* the z-free incidences of `E`;
* the fixed `z`-present complemented copy of `E_0`; and
* the fixed endpoint verticals.

This is the construction in `(1.2)` of
`MATH_THEOREM_COMPLETE_ML13_T2_CYCLIC_SUPPORT_AND_RESIDENT_LIFT_GATES_20260813.md`.
The canonical graph `H(E_0)` has `Cat_m` components.  Each is indexed by a
Dyck root `X in D_m`, has `k` vertices on either shore, and will be denoted
`Gamma(X)`.

Put

\[
\begin{split}
\mathcal R={}&\{110101110000,111100110000,111110010000,\\
             &\hspace{25mm}111110100000,111111000000\}.       \tag{1.1}
\end{split}
\]

The `T2` packet at a suffix `V in D_(m-6)` replaces the five components

\[
                         \{\Gamma(XV):X\in\mathcal R\}         \tag{1.2}
\]

by one component of shore length `5k`.  Different `V` give disjoint
five-sets.  Consequently the post-`T2` component count and histogram are

\[
 \boxed{C_0=\operatorname {Cat}_m-4\operatorname {Cat}_{m-6}}, \tag{1.3}
\]

\[
 \{k^{\operatorname {Cat}_m-5\operatorname {Cat}_{m-6}},
       (5k)^{\operatorname {Cat}_{m-6}}\}                   \tag{1.4}
\]

on either shore.

## 2. Exact component support of one `C16`

For `W in D_(m-8)`, write `T(1100W)` and `T(1010W)` for the two
five-wreath components from `(1.2)`.  Define the following six-root sets:

```text
S4 = {
  1101101010100010, 1101001010101010,
  1101101010001010, 1101101010001100,
  1101001010111000, 1101001010101100
}

S6 = {
  1101101100100010, 1101100100101010,
  1101101100001010, 1101101100001100,
  1101100100111000, 1101100100101100
}.
```

### Theorem 2.1 (eight-way component action)

The eight old incidences of `Q_b(W)`, for `b in {4,6}`, lie one each in
the distinct components

\[
 \boxed{T(1100W),\ T(1010W),\
        \{\Gamma(XW):X\in S_b\}.}                          \tag{2.1}
\]

Toggling `Q_b(W)` merges precisely these eight components.  The resulting
component has shore length

\[
                         5k+5k+6k=16k.                     \tag{2.2}
\]

#### Proof

At `m=8`, direct endpoint traversal gives exactly the eight blocks in
`(2.1)`.  Every old incidence is in a different block.  Cutting those
eight incidences opens eight paths, and the eight new incidences occur in
the cyclic order of the alternating `C16`; they concatenate the paths into
one cycle.

For a Dyck tail `W`, the MSW insertion and deletion orders concatenate:

\[
 I(XW)=I(X)\Vert(16+I(W)),\qquad
 D(XW)=D(X)\Vert(16+D(W)).                              \tag{2.3}
\]

All changed incidences occur before the common tail.  Contracting the
unchanged tail therefore gives the same endpoint permutation as the
`m=8` calculation, and appending the tail sends every root `X` in the
base certificate to `XW`.  This proves `(2.1)--(2.2)` for every `m>=8`.
\(\square\)

### Theorem 2.2 (the two local choices form a hypercycle)

For fixed `W`, the supports of `Q_4(W)` and `Q_6(W)` meet exactly in

\[
                         \{T(1100W),T(1010W)\}.              \tag{2.4}
\]

The sets `S_4,S_6` are disjoint.  Hence the component--trade incidence
graph on the two trades contains the cycle

\[
 T(1100W)-Q_4(W)-T(1010W)-Q_6(W)-T(1100W).             \tag{2.5}
\]

The simultaneous toggle has two output components, with `9k` and `13k`
vertices on each shore.  In particular its component reduction is `12`,
not the tree weight `7+7=14`.

If `W != W'`, every root in `(2.1)` has a different terminal Dyck factor,
so the corresponding component supports are disjoint.  Therefore, if
`N_1` tails receive exactly one local trade and `N_2` tails receive both,
the exact component count is

\[
 \boxed{C_0-7N_1-12N_2.}                                  \tag{2.6}
\]

In particular, one choice per tail gives

\[
 \operatorname {Cat}_m-4\operatorname {Cat}_{m-6}
                    -7\operatorname {Cat}_{m-8}.             \tag{2.7}
\]

#### Proof

The two root lists make `(2.4)` literal.  A bipartite hypertree on two
trade vertices would have only one common component neighbour; two common
neighbours give `(2.5)`.  Exact traversal of the finite base endpoint
matching gives shore lengths `9k,13k` after both toggles.  Equation `(2.3)`
tensors those lengths and separates distinct tails.  Additivity across
the disjoint tail blocks proves `(2.6)--(2.7)`. \(\square\)

This does not contradict incidence-level conflict-freeness: the two
`C16`s have disjoint owner and colour vertices and commute.  What fails is
the stronger component-hypertree condition.

## 3. The realized suffix graph is only a matching

Let `G_s` be the graph whose vertices are `D_s`, with an edge between two
Dyck words when their up-step sets are Johnson adjacent.  The two words in
`(0.2)` differ by exchanging coordinates `1` and `2`, so every member of
`M_s` is an edge of `G_s`.

### Theorem 3.1 (exact suffix-graph obstruction)

`M_s` is a matching of size `Cat_(s-2)`.  It covers all of `D_s` only for
`s=2`; for every `s>=3` it leaves an uncovered vertex.

#### Proof

Deleting the first four letters recovers `W` uniquely from either endpoint,
and the two four-letter prefixes are different.  Thus no two edges share
an endpoint.  The endpoint count is `2 Cat_(s-2)`.  Moreover

\[
 {\operatorname {Cat}_s\over\operatorname {Cat}_{s-2}}
   ={4(2s-1)(2s-3)\over s(s+1)},                         \tag{3.1}
\]

which is greater than `2` for `s>=3`. \(\square\)

Consequently no selection from the present `C16` bank is a spanning tree
of `G_s`.  At component level, selecting one trade per edge gives a
disjoint union of eight-way stars, not a connected hypertree.  Selecting
both trades per edge inserts the local cycle `(2.5)` and still leaves two
local outputs.  Thus the spanning-hypertree target of
`MATH_THEOREM_CROSS_WREATH_QSAFE_ALTERNATING_FLIP_HYPERTREE_AND_C4_MINIMALITY_20260813.md`
cannot be met by this bank alone.

## 4. Exact seam spacing and the residence obstruction

Suppress one shore of `H(E)` and, for consecutive retained owners `A,B`,
write

\[
                              e(A,B)=A\triangle B.            \tag{4.1}
\]

A `q`-transition window is resident exactly when its supports are pairwise
coordinate-disjoint.  The rank-`m+1` projection uses the q1 colours as
owners and the rank-`m` sets as immediate-lower labels.  The rank-`m`
projection uses the original `T2` owners.

### Theorem 4.1 (separation is sufficient, collars are not)

For either single switch the eight new seams lie on the `16k` output cycle
with gap multiset `(0.1)`.  Nevertheless:

| switch | bad upper `2`-collars | upper minimum `(positive,zero)` at `m=8` | bad lower `2`-collars | lower minimum `(positive,zero)` at `m=8` |
|---|---:|---:|---:|---:|
| `b=4` | `4` | `(2,1)` | `2` | `(1,2)` |
| `b=6` | `6` | `(2,1)` | `5` | `(1,2)` |

Here “bad collar” counts seams; one seam may contain a collision on both
sides.  The numbers of collision events are respectively `4,7` on the
upper shore and `2,6` on the lower shore.

The finite endpoint traversal orders the eight seam gaps as six one-wreath
arcs and two five-wreath arcs.  Every canonical wreath has exactly `k`
transitions on either projected shore.  The concatenation contraction in
`(2.3)` preserves this wreath word, proving the gap multiset `(0.1)` at
every tensor level.

For example, on the upper shore of `Q_4` the consecutive supports

\[
                         \{8,11\},\quad\{8,13\}               \tag{4.2}
\]

meet at coordinate `8`.  The intervening upper owner is

```text
                         0010110101111100,
```

where coordinate `8` is zero.  It is therefore a literal zero run of
length one.  On the lower shore of the same switch, consecutive supports

\[
                         \{2,10\},\quad\{1,10\}               \tag{4.3}
\]

meet at coordinate `10`; their intervening owner

```text
                         1000010101111010
```

contains coordinate `10`, giving a positive run of length one.

For `Q_6`, stable witnesses are the upper supports

\[
                         \{6,15\},\quad\{12,15\}              \tag{4.4}
\]

around the zero singleton `0010011011011110`, and the lower supports

\[
                         \{0,10\},\quad\{0,2\}                \tag{4.5}
\]

around the positive singleton `1000011011011100`.

Adjoining `U(W)` to every displayed owner leaves all four repeated prefix
coordinates unchanged.  Thus the singleton witnesses tensor for every
`W`.  Toggling both switches does not repair them: the two output cycles
retain ten bad upper collars and seven bad lower collars.  Hence every
nonempty selection from this local pair fails `q`-biresidence for every
`q>=2`. \(\square\)

The obstruction is stronger than a failure of seam separation.  Even for
every `q<=k`, where `(0.1)` makes each `q`-window meet at most one changed
seam, the seam itself is illegal.

## 5. Exact common-history boundary

There are two different common-intersection statements, and conflating
them hides the obstruction.

### 5.1 Upper/q1 projection

The eight switched rank-`m` labels share

\[
             H_b\cup U(W),\qquad |H_b\cup U(W)|=m-2.          \tag{5.1}
\]

Every old and new upper transition at such a label contains this set.
The rank-`m` lower-label ledger is exact, and the earlier `q2` verifier
proves aggregate first-upper support monotonicity.  Thus `(5.1)` supplies
the algebraic core needed by the common-intersection support-monotone
packet theorem at any depth `d<=m-2`.

This is only a **prospective** lift.  The theorem requires an ambient
source with occurrence-disjoint, cut-separated fragments.  The frozen
undilated upper cycle has a positive run of length `2` and a zero run of
length `1`; it cannot itself be a depth-`d` positive-resident antecedent
for `d>=2`, and it is not biresident even at `d=1`.  A phase clock or other
residence dilation must therefore precede the planting.

### 5.2 Original-owner projection

Projecting through the q1 colours changes the actual Johnson edges
`O_iB_i` to `O_iB_(i+1)`, where `B_i` is the other selected owner at the
removed q1 colour.  Their complete common intersections at `m=8` are

\[
 K_4=\{7,9\},\qquad K_6=\{5,8,9\}.                         \tag{5.2}
\]

After tensoring they become `K_b union U(W)`, of ranks `m-6` and `m-5`.
More seriously, the rank-`m-1` intersection-colour multiset is not exact:

| switch | lost occurrences | born occurrences |
|---|---:|---:|
| `b=4` | `7` | `7` |
| `b=6` | `5` | `5` |

The lower-shore positive singleton in Theorem 4.1 also rules out any
undilated positive-depth source antecedent of this exact projected
chronology.  Therefore the exact-palette common-intersection theorem does
not directly lift the original-owner projection.

Finally, at the original source depth the selected `q2` value is the
union of two q1 colours, hence a three-owner turn at source width `d+3`.
The factor-level support calculation remains valid only for a source lift
that carries the unchanged mate on both sides of every hinge, as required
by
`MATH_REDUCTION_TURN_FAITHFUL_COMMON_HISTORY_WIDTH_DPLUS3_CURRENT_AND_CUT_SEPARATION_GATE_20260813.md`.
The finite `C16` ledger already proves the desired aggregate current once
those turn-faithful fragments are planted; what is missing is their
occurrence-disjoint planting in a residence-dilated host, plus a repair of
the displayed rank-`m-1` palette current if that row is required.

## 6. Verifier

The standard-library verifier is

```text
scratch/verify_t2_c16_suffix_component_residence_20260813.py
```

with SHA-256

```text
f125c3b776e014856112e34fb8f07e5c7ed0d7e388c960b39e132e8bcdf58813
```

Its exact output is

```text
scratch/verify_t2_c16_suffix_component_residence_20260813.out
```

with SHA-256

```text
7a77f9bcf694f0721d784e80018cb5e7b750b3979e5bcc6454ab70101a182ac0
```

It performs the following independent checks.

1. It rebuilds the exact canonical factors at `m=8,9,10`, applies every
   tensor `T2` packet, and verifies `(1.3)--(1.4)`.
2. It labels canonical paths by Dyck roots and checks all component sets
   in `(2.1)`, their same-tail and different-tail intersections, and all
   three selections: `b=4`, `b=6`, and both.
3. It verifies reductions `7,7,12`, the simultaneous `9k/13k` split, and
   the Catalan formulas through the first three tensor levels.
4. It traverses both projected shores, checks `(0.1)`, enumerates every
   bad `2`-collar, identifies the singleton value, and recomputes the q2
   support current and the original-owner lower-palette current.
5. It enumerates `D_s` for `2<=s<=10` and verifies that `(0.2)` is a
   matching with the stated coverage.

The tensor replays are implementation checks.  The all-`m` proof is the
concatenation argument `(2.3)` together with the finite root/action
certificate.

## 7. Sharp remaining gate

The present `C16` bank can be used safely only as a disjoint collection of
local eight-way merges, one choice per aligned suffix edge.  It does not
solve either global requirement:

\[
 \boxed{\begin{array}{c}
 \text{add suffix trades whose incidence hypergraph connects all Dyck roots,}\\
 \text{and plant them in a residence-dilated, turn-faithful common-history host.}
 \end{array}}                                             \tag{7.1}
\]

The first line is forced by the matching obstruction of Section 3.  The
second is forced by the literal singleton collars of Section 4.  Any route
using the original-owner source hierarchy must additionally cancel the
`7`- or `5`-ticket rank-`m-1` palette current from Section 5.2.
