# Cycle-first reset hypergraphs: exact packing/cover marginals, a linear hard-target obstruction, and the support-three topology gate

Date: 2026-08-01

Status: unconditional degree, codegree, fractional, and divisibility
calculations for the bidirectional reset-ring block family, together with a
sharp obstruction to treating high targets as ordinary matching vertices.
The note identifies the correct mixed packing--cover object and the separate
support-at-least-three connector problem.  It does not prove an integral
almost-perfect packing or construct a decorated Boolean hex splice.

## 0. Outcome

Let

\[
 k=2m+1,qquad N=2(d+1),qquad 2\le d\le m,
\]

and use the unoriented bidirectional reset rings from
`MATH_THEOREM_BIDIRECTIONAL_ROLLING_RESET_ORBIT_SCD_AND_G0_GATE_20260801.md`.
One ring contains:

* `N` distinct rank-`m` roots;
* `N` distinct rank-`m+1` owners;
* for every `1<=j<d`, `N` distinct offered rank-`m-j` targets;
* two legal orientations with identical resource inventories.

On roots and owners alone, the block family is regular.  Its dominant
root--owner codegree ratio is

\[
                         {2\over m+1},                         \tag{0.1}
\]

and nested root/target and target/target ratios are also `O(1/m)` for
`d=o(m)`.  The uniform block weight gives exact root/owner load one and
target load at least one.  Thus the cycle family has the correct fractional
packing--cover point.

However, a standard hypergraph matching which makes every offered target a
capacity-one vertex is impossible as an almost-perfect root packing.  Every
ring uses `N` vertices from every rank shore, so the smallest target shore
caps the number of roots covered.  The root deficiency is at least

\[
 \boxed{
   \binom{2m+1}{m}-\binom{2m+1}{m-d+1}.}
                                                                  \tag{0.2}
\]

At the conjectural depth `d=Theta(sqrt(m))`, (0.2) is a positive fraction
of the middle layer.  At `k=17,d=3`, it leaves at least

\[
                         24310-12376=11934                       \tag{0.3}

physical roots, or `1430-728=702` root necklaces.

Consequently high targets must be **coverage resources with optional marked
occurrences**, not packing vertices carried by every cycle atom.

Even after that correction, a disjoint reset-ring packing is a union of
closed components.  The owner-preserving two-edge splice theorem rules out
ordinary graph edges as topology connectors.  Any connector must change at
least three occurrence edges and must simultaneously close the reset's one
owner endpoint pair and two predecessor parity endpoint pairs.  The correct
global object is therefore:

\[
 \boxed{\text{root/owner cycle packing}
 +\text{target marking SDR}
 +\text{support-}\ge3\text{ connector hypertree}.}             \tag{0.4}
\]

No standard exact matching theorem supplies all three rows.

## 1. The reset-ring block family

Let `X` be a cyclically ordered set of size `N=2(d+1)`, let `K` have size
`m-d`, and keep the remaining `m-d-1` coordinates unused.  The ring roots,
owners, and depth-`j` target banks are

\[
\begin{aligned}
 Q_a&=K\cup X[a,a+d-1],\\
 O_a&=K\cup X[a,a+d],\\
 T_{a,j}&=K\cup X[a,a+d-j-1]
                  \qquad(1\le j<d),                         \tag{1.1}
\end{aligned}
\]

with `a in Z_N`.  The forward and reverse reset phases pair the same
resource sets in opposite cyclic orders, so orientation is not part of the
unoriented block.

Let `B` be the set of all labelled unoriented blocks.  Direct selection of
`K`, cyclic `X`, and the unused set gives

\[
 |B|={k!\over2N(m-d)!(m-d-1)!}.                    \tag{1.2}
\]

The factor `2N` quotients reversal and cyclic shift of the private order.

## 2. Exact degrees

Put

\[
 W_j=\binom{2m+1}{m-j},
 \qquad W_0=W=\binom{2m+1}m.                       \tag{2.1}
\]

### Theorem 2.1 (all-shore degree ledger)

Every root and every owner has common block degree

\[
 D={1\over2}
   {m!\over(m-d)!}
   {(m+1)!\over(m-d-1)!}.                           \tag{2.2}
\]

Every depth-`j` target has degree

\[
                         D_j={|B|N\over W_j}
                             =D{W\over W_j}.          \tag{2.3}

#### Proof

Every block contains `N` roots and `N` owners.  Transitivity on both central
layers gives degree `|B|N/W`, which simplifies to (2.2).

At depth `j`, every block contains `N` target sets.  Transitivity on rank
`m-j` gives `|B|N/W_j`, proving (2.3). \(\square\)

Since `W_j<=W`, every target load under the uniform root-normalized block
weight is at least one.

### Corollary 2.2 (exact fractional packing--cover point)

Assign every block weight `1/D`.  Then

\[
 \sum_{B\ni Q}{1\over D}=1,
 \qquad
 \sum_{B\ni O}{1\over D}=1,                         \tag{2.4}

and every depth-`j` target has load

\[
                         \rho_j={D_j\over D}={W\over W_j}\ge1. \tag{2.5}

Marking each target occurrence fractionally with the additional factor
`1/rho_j` gives exact marked load one while retaining exact root and owner
loads.

Thus no fractional separator exists at the simultaneous cycle-packing and
high-target-cover rows.  The issue is integral correlation and topology.

## 3. Exact nested codegrees

The previously proved central codegrees are

\[
 {\lambda_{QO}\over D}={2\over m+1},
 \qquad
 {\lambda_{QQ}^{\rm Johnson}\over D}
 ={2\over m(m+1)},                                  \tag{3.1}

with the complementary owner--owner formula equal to the second ratio.

There is an analogous exact target calculation.

### Theorem 3.1 (nested root/target codegree)

Fix a root `Q` and a depth-`j` target `T subset Q`.  Then

\[
             \lambda(Q,T)
             =D\,{j+1\over\binom mj}.                \tag{3.2}

#### Proof

Inside a common block, the private interval of `T` has length `d-j` and
must be contained in the private interval of `Q`, of length `d`.  There are
`j+1` possible offsets.

Fix one offset.  Choose the core `K subset T` in

\[
                         \binom{m-j}{d-j}
\]

ways.  Order `T-K` in `(d-j)!` ways and the `j` elements of `Q-T` in `j!`
ways around the chosen offset.  Choose and order the remaining `d+2`
private coordinates outside `Q` in

\[
                         {(m+1)!\over(m-d-1)!}
\]

ways, and divide by two for reversal.  Comparing with (2.2), one offset
has ratio

\[
 {\binom{m-j}{d-j}(d-j)!j!\over m!/(m-d)!}
 ={j!(m-j)!\over m!}={1\over\binom mj}.              \tag{3.3}
\]

Sum the `j+1` offsets. \(\square\)

### Theorem 3.2 (nested target/target codegree)

Let `0<=i<j<d`, interpret depth zero as the root layer, and fix nested
targets

\[
                         T_j\subset T_i.
\]

Then

\[
 {\lambda(T_i,T_j)\over D_i}
 ={j-i+1\over\binom{m-i}{j-i}}.                    \tag{3.4}

The proof is Theorem 3.1 after replacing `m,d` by `m-i,d-i`.

In particular adjacent nested layers have ratio

\[
                         {2\over m-i},                         \tag{3.5}

which is `O(1/m)` uniformly for `i<d=o(m)`.  These exact rows support an
approximate-packing heuristic, but they do not overcome the hard-target or
topology obstructions below.  No claim is made here that every nonnested
mixed-layer pair has smaller codegree; such a global maximum is unnecessary
for the no-go in Section 4.

## 4. Why target vertices cannot be matching resources

Form the naive cycle hypergraph whose vertex shores are

\[
 \mathcal R,\mathcal O,
 \mathcal T_1,\ldots,\mathcal T_{d-1},              \tag{4.1}

and whose edge for a reset block contains all `N` resources from every
shore in (1.1).

### Theorem 4.1 (equal-consumption obstruction)

Every matching of `b` block edges covers exactly `bN` vertices in every
shore.  Hence it covers at most

\[
                         W_{d-1}                              \tag{4.2}

roots, and its root deficiency is at least (0.2).

#### Proof

Disjointness on the deepest target shore gives `bN<=W_(d-1)`.  The root
shore contribution is the same `bN`. \(\square\)

The relative maximum root coverage is

\[
 {W_{d-1}\over W}
 =\prod_{s=0}^{d-2}{m-s\over m+2+s}.                \tag{4.3}

If `d^2/m` is bounded away from zero, (4.3) is bounded away from one.  At
the conjectural depth `d=Theta(sqrt(m))`, the deficiency is therefore
`Theta(W)`.

This obstruction applies equally to hypothetical three-root hex-cycle
atoms if every offered high target is made a capacity-one vertex: each such
atom still consumes the same number of resources in every suffix layer.

### Corollary 4.2 (correct marked-target interface)

Cycle selection must impose

\[
 \sum_{B\ni Q}x_B\le1,
 \qquad
 \sum_{B\ni O}x_B\le1,                              \tag{4.4}

but target rows must use separate occurrence marks

\[
 0\le y_{B,T}\le x_B,
 \qquad
 \sum_{B\ni T}y_{B,T}=1.                            \tag{4.5}

Unmarked duplicate target offerings are allowed.  Equations (4.4)--(4.5)
are a mixed packing--cover/SDR system, not a hypergraph matching.

## 5. Arithmetic of reset and hypothetical hex atoms

A pure reset-ring packing uses roots and owners in multiples of

\[
                         N=2(d+1).                            \tag{5.1}

Thus an exact decomposition requires

\[
                         N\mid W.                              \tag{5.2}

At `k=17,d=3`, `W=24310=6 mod 8`, giving the known six-root and six-owner
physical residue.  If whole free rotation orbits of blocks are required,
the quotient residue is six blocks and the literal residue is

\[
                         6\cdot17=102.                         \tag{5.3}

Suppose, conditionally, that a fully decorated root-simple Boolean hex atom
exists and uses three roots and three owners while exporting the same marked-
target interface.  Root/owner counts would then lie in the semigroup

\[
                         \langle N,3\rangle.                   \tag{5.4}

If `3` does not divide `N`, the gcd is one and the scalar root/owner residue
can eventually be removed exactly.  If `3` divides `N`, at most two roots
remain for scalar reasons.  Thus a genuine decorated hex family would
remove the growing pure-reset divisibility residue.

This is only arithmetic.  The support-three splice theorem says a ternary
central exchange is the first possible owner-preserving move; it does not
construct a root-simple hex cycle preserving the complete ordered rail,
all suffix marks, and exterior OR currents.

## 6. Topology is a connector-hypergraph problem

A matching in (4.4) is a collection of closed reset components.  Reversing
one bidirectional ring preserves all internal resources, but after opening
it exports exactly

\[
 \boxed{\text{one head--owner endpoint pair}
       +\text{two predecessor parity endpoint pairs}.}       \tag{6.1}

The bidirectional functional-attachment theorem proves that external
alternating returns must close all three pairs.

The owner-preserving splice lemma proves that two distinct cycle edges
cannot be cross-reconnected by a nondegenerate support-two exchange.
Therefore an ordinary graph on reset components, with one edge representing
a two-cut splice, has no literal realization.

Define instead the **connector hypergraph** of a selected packing:

* its vertices are selected cycle blocks together with their occurrence-
  labelled boundary ports;
* a hyperedge is a support-`s`, `s>=3`, Boolean trade whose old occurrences
  lie in those cycles, whose new occurrences preserve every root/owner and
  marked-target resource, and whose rail/exterior currents vanish;
* a successful connector family must join all cycle components while
  respecting port capacities and the three endpoint-pair equations (6.1).

This is a hypertree/ear-system problem sharing the already selected cycle
vertices.  It is not a matching disjoint from the cycle packing.

### Theorem 6.1 (two-stage necessity)

Any cycle-first proof using bidirectional reset rings must establish both:

1. an integral solution of the mixed packing--cover system
   (4.4)--(4.5); and
2. a connected port-respecting spanning structure in the support-`>=3`
   connector hypergraph.

Neither conclusion follows from the degree/codegree ledger of Sections
2--3.

#### Proof

The first statement is exact root/owner capacity plus exact target marking.
The second is necessary because the selected rings are closed components,
and every topology-changing literal replacement has support at least three.
The endpoint ledger (6.1) is preserved by any valid global factor, so every
opened ring's three boundary pairs must be closed through the chosen
connectors. \(\square\)

## 7. Consequence for an absorbing theorem

The root/owner block hypergraph has an exact fractional perfect matching and
several favourable `O(1/m)` codegree rows.  This makes an almost-perfect
root/owner packing plausible.  It is not yet an `O(1)` theorem because:

1. pure reset rings have the residue (5.2);
2. treating targets as matching vertices causes the linear obstruction
   (0.2);
3. optional target marking requires a correlated SDR after cycles are
   selected;
4. support-two topology absorption is impossible; and
5. no positive-density family of fully guarded support-three connector
   atoms has been proved.

Accordingly, the shortest credible positive statement is:

> **Cycle packing--marking--connector theorem.**  Select root/owner-disjoint
> reset and decorated-hex cycles covering all but `O(1)` roots and owners;
> mark every high target exactly once among their offered occurrences; then
> select a port-compatible support-`>=3` connector hypertree which merges
> all cycles without changing those marks or the complete rail/OR boundary.

The present theory supplies the reset atoms and their exact fractional
ledger.  It supplies neither the decorated hex atoms nor the connector
hypertree.  Those are the next actual construction objects; a standard
cycle-hypergraph matching theorem alone cannot finish the proof.
