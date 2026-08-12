# Joint fan/endpoint selection is a three-matroid gate

**Date:** 2026-08-05  
**Method:** partition and bicircular matroids, Edmonds intersection, and a
literal growing orientation-cube obstruction; no computation  
**Status:** unconditional exact formulation and linear-loss counterexample
for fixed active-anchor catalogues.  A positive two-matroid theorem is
proved when one endpoint shore is private.  The note does not rule out a
jointly designed parent factor which avoids the bad catalogue.

## 1. Exact selector model

Let `mathcal F` be a family of fan tasks.  For each `f in mathcal F`, let
`E_f` be the catalogue of receiver squares which may discharge that fan,
and suppose exactly one square must be selected from every `E_f`.  Put

\[
                         E=\mathbin{\dot\bigcup}_{f\in\mathcal F}E_f.
\]

Every candidate `e` has two diagonal endpoint lists `A_e,B_e`, each of
size at most two after orbit coalescence and fixed deletions.  Let `M_A`
and `M_B` be the corresponding bicircular/transversal matroids on `E`.
Let `P` be the partition matroid with blocks `E_f` and capacity one.

### Theorem 1.1 (three-matroid formulation)

A complete one-square-per-fan selector whose two endpoint graphs are
pseudoforests is exactly a common independent set

\[
                         I\in P\cap M_A\cap M_B
\]

of cardinality `|mathcal F|`.

#### Proof

Independence in `P` says at most one candidate is used from each fan; at
cardinality `|mathcal F|` this is exactly one from every fan.  By the
two-element endpoint orientation theorem, independence in `M_A` and
`M_B` is exactly endpoint packability on the two shores. \(\square\)

Thus the fan constraint is not absorbed by the common-bicircular
two-matroid intersection.  Equivalently, the direct-sum linear parity
formulation for `(M_A,M_B)` becomes **coloured matroid parity**, with one
pair required from every fan colour.  Ordinary matroid intersection or
ordinary uncoloured matroid parity does not encode this third constraint.

For fans with more than one passive pair, a fixed decomposition into pair
slots gives one partition block per slot.  If the pairing itself is also
variable, the additional requirement is a perfect matching in the petal
clique and is at least as strong as the gate above.

## 2. Exact positive case: one private endpoint shore

There is one important circumstance in which the third constraint
collapses.

Say the `A` shore is **fan-private** when every `P`-independent set is
independent in `M_A`.  A sufficient literal condition is that the
`A`-diagonal endpoint sets of candidates belonging to different fans are
pairwise disjoint and that the candidates inside one fan are individually
nondegenerate.

### Theorem 2.1 (private-shore fan selector)

If the `A` shore is fan-private and `q=|mathcal F|`, then the maximum
number of simultaneously dischargeable fans is

\[
 \boxed{
 \nu=\min_{X\subseteq E}
          \bigl(r_P(X)+r_B(E\setminus X)\bigr).}       \tag{2.1}
\]

In particular a complete selector exists if and only if

\[
 r_P(X)+r_B(E\setminus X)\ge q
 \qquad\hbox{for every }X\subseteq E.                 \tag{2.2}
\]

Here

\[
 r_P(X)=|\{f:X\cap E_f\ne\varnothing\}|              \tag{2.3}
\]

and `r_B` is the explicit bicircular component rank.

#### Proof

Fan-privacy makes the `M_A` condition redundant on every set independent
in `P`.  Feasible sets are therefore precisely the common independent
sets of the two matroids `P` and `M_B`.  Edmonds' matroid-intersection
theorem gives (2.1), and (2.2) is the condition that its value equal `q`.
\(\square\)

The symmetric statement holds with `A,B` exchanged.  This theorem is a
concrete constructive target: make one receiver diagonal globally private,
then only one ordinary partition--bicircular intersection remains.

## 3. Pairwise feasibility is not a three-way theorem

Even for partition matroids, three-way feasibility is not implied by
feasibility of the three pairwise intersections.  The obstruction can be
seen with two fan blocks, each having choices labelled `0,1`.

Let the `A` constraint forbid choosing equal labels from the two fans and
let the `B` constraint forbid choosing unequal labels.  Then `P cap M_A`
has a complete selector (choose unequal labels) and `P cap M_B` has one
(choose equal labels), but no selector satisfies all three constraints.

Capacity-one conflicts of this form are bicircular: preload one ordinary
edge between two endpoint vertices, and represent each conflicting choice
by an additional parallel edge.  One choice together with the preload is
unicyclic, while two conflicting choices create a three-parallel-edge
bicycle.  Thus no abstract exchange argument based only on the three
pairwise rank systems can prove Theorem 1.1.

The next section gives a stronger obstruction using literal receiver
squares, without relying on this abstract preload gadget.

## 4. An actual family with linear unavoidable loss

Fix `h>=1`.  Work in the even labelled capacity-two sector

\[
                 \mathcal T_{16h+2,\,24h+3}.          \tag{4.1}
\]

Partition the coordinates into `8h+1` consecutive pairs.  On every pair
use the two local states

\[
                              12,\quad21.              \tag{4.2}
\]

and fix the final pair.  The first `8h` pair states form an orientation
cube.  Group them into `h` disjoint blocks of eight direction bits, and
inside each block group the bits into four ordered pairs.

In block `c`, use the eight receiver squares whose `B` diagonals form two
four-cycles through the global all-zero group state:

\[
 0000-1000-1100-0100-0000,
\]

\[
 0000-0010-0011-0001-0000.                            \tag{4.3}
\]

All other blocks stay at their zero group state.  Give every square its
own fan task, one fixed private active-anchor petal, and the displayed two
passive petals.  Hence every catalogue block `E_f` is a singleton.

Choose a superincreasing macro background.  As in the one-block
counterexample, local mass three makes every deleted-cut parent critical;
disjoint direction sets make the square boundaries distinct; and private
split blocks provide the active anchors.  The background kills all
rotational stabilizers.  Thus this is one literal actual fan bank, not a
disjoint union of abstract matroids.

The `A`-diagonal endpoint graph is a matching.  On the `B` shore, the
`2h` four-cycles all meet at the one global zero-state vertex and are
otherwise vertex-disjoint.  Therefore

\[
 |E_B|=8h,
 \qquad
 |V_B|=1+3(2h)=6h+1.                                  \tag{4.4}
\]

The whole `B` graph is connected and has bicircular surplus

\[
                         8h-(6h+1)=2h-1.              \tag{4.5}
\]

Its bicircular rank is `6h+1`.  Since the fan catalogues are singletons,
every complete fan selector contains all `8h` jobs, while any endpoint-safe
subselector contains at most `6h+1` jobs.

### Theorem 4.1 (linear-loss fixed-fan obstruction)

For every `h` there is an actual even labelled fixed-active-anchor fan
catalogue with `8h` mandatory one-pair fan tasks for which at least

\[
                              2h-1                    \tag{4.6}
\]

tasks must be dropped before both receiver endpoint shores are packable.

Consequently no `O(1)`-loss endpoint selector follows from the local fan,
joint-admissibility, criticality, or trivial-quotient axioms alone.

#### Proof

The literal realization was checked above.  The `A` graph is independent.
On the `B` shore every independent set has size at most the bicircular rank
`min(8h,6h+1)=6h+1`, proving the lower bound `2h-1`.  Conversely a connected
unicyclic spanning subgraph of the bouquet has `6h+1` edges, so the bound is
sharp. \(\square\)

The theorem is deliberately scoped to fixed active anchors.  A global
parent selector may avoid this catalogue by changing its parent edges or
anchors before the fans are frozen.  What is ruled out is any theorem that
first chooses an arbitrary valid parent/anchor bank and then promises a
bounded-loss receiver repair.

## 5. Correct all-dimensional target

The receiver row must therefore be imposed during parent-factor selection.
A proof-safe sufficient package is:

1. choose one candidate per fan, or one perfect passive pairing per larger
   fan;
2. satisfy the three-matroid condition of Theorem 1.1, preferably through
   the private-shore reduction of Theorem 2.1;
3. satisfy the pseudoforest tree-discount inequalities for every proper
   ordinary Hall cut; and
4. impose the residual augmented perfect-matching condition on the same
   choice.

Theorem 4.1 shows that step 2 cannot be repaired with a bounded terminal
sidecar after an arbitrary parent factor.  To preserve an additive
constant, the parent construction must export either a private endpoint
shore, the full rank inequalities (2.2), or an equivalent joint selector
certificate.

## 6. Quotient and odd-level scope

The obstruction has trivial stabilizer, so it is independent of periodic
quotient difficulties.  Conversely, an invariant occurrence-level
pseudoforest descends to an odd rotational quotient pseudoforest by the
tree/unicycle quotient theorem.

At odd cut length the fan/endpoint selection remains the same three-matroid
gate, but ordinary extension is a Tutte/blossom constraint rather than the
even Hall constraint.  No odd-wrap conclusion is claimed here.
