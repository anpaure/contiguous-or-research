# Depth three is one transition system: the exact common-order gate

Date: 2026-07-28

Status: unconditional reduction and switching theorem.  It converts the
remaining mismatch between two separately realizable adjacent Euler trails
into local pairings of coloured half-edges in one **two-sided diamond
multigraph**.  The formerly proposed scalar support condition
`min_S d_S>=2` is now refuted by a complete-support Johnson counterexample;
the required replacement is cut-aware.  This note does not construct the
needed `k=15` multigraph or solve the owner/compiler gate.

## 0. Outcome

Let the depth-one trace row have rank `s`, the depth-two row rank `s-1`,
the middle-owner row rank `s+1`, and the depth-three row rank `s-2`.
Every Johnson edge at depth one has two forced colours,

\[
 R=A\cap B\in\binom{[k]}{s-1},\qquad
 U=A\cup B\in\binom{[k]}{s+1}.
\]

Thus the first object must be a connected **diamond multigraph** `G` with
both the prescribed lower `R`-loads and the prescribed upper `U`-loads.
Once it exists, an ordering of its edges is the desired depth-one
chronology.  The depth-two row is its lower-colour word.  The depth-three
row is determined locally: at every visit to
an `s`-set `A`, pair the incoming and outgoing edge copies; if their facet
colours are `A-x` and `A-y`, that visit contributes the label

\[
                         A-\{x,y\}.
\]

Thus the common-order problem is not a second independent Euler trail.  It
is a transition system on the **same** edge copies.  The local pair counts
obey an explicit integer system, and the transition system spells one
chronology exactly when its edge-copy graph is one path.

There is also a useful switching result.  If two transition components meet
the same owner vertex through actual transition pairs, they can be joined by
a local cross-pairing which preserves the first two row multisets, the end
stubs, depth-three rank, and the complete depth-three point-degree vector.
The only exceptional contact is through one of the two unpaired end stubs.
It can also be joined, but moves that end stub to another colour at the same
owner and changes one boundary depth-three occurrence.  After at most one
such move for each global end stub, further joins through that stub's owner use ordinary
pair--pair switches.  Consequently connectivity itself costs at most two
boundary changes; the substantive conditions are existence of the
two-sided diamond table and support preservation inside one explicit
local-pairing fibre.

For the frozen `k=15` Hall-29 data, the separately constructed depth-three
row has every rank-five target with load two or three.  This supplies a full
unit of pointwise redundancy before the transition components are joined,
but pointwise redundancy alone is not enough.  The sharpened finite gate is
whether the actual component/label incidence has a cut-feasible protected
occurrence transversal.

## 1. Coloured Euler data

Put

\[
 \mathcal A=\binom{[k]}s,qquad
 \mathcal R=\binom{[k]}{s-1},qquad
 \mathcal S=\binom{[k]}{s-2}.
\]

Let `G` be a connected loopless multigraph on vertex types
`A in mathcal A`.  Every edge copy `e=AB` is a Johnson edge and has its
forced lower and upper colours

\[
 c_-(e)=A\cap B\in\mathcal R,
 \qquad c_+(e)=A\cup B\in\binom{[k]}{s+1}.
\tag{1.1}
\]

Let `m_A` be the intended number of occurrences of `A`.  Fix endpoint
stub numbers `epsilon_A in {0,1,2}` with total two and

\[
                         \deg_G(A)=2m_A-\epsilon_A.
\tag{1.2}
\]

The coloured-Euler theorem says precisely that an Euler trail in `G` has
vertex-type multiset `m`, depth-two multiset equal to its lower edge-colour
multiset, and middle-owner interior multiset equal to its upper edge-colour
multiset.  The two boundary middle owners are supplied by the nested end
flags.

Equivalently, before pairing or ordering is considered, let

\[
 z_{R,U}\in\mathbb Z_{\ge0}
 \quad(R\subset U,\ |U\setminus R|=2)
\tag{1.3}
\]

be the multiplicity of the unique Johnson edge whose endpoints are the two
`s`-sets strictly between `R` and `U`.  The exact two-sided diamond table
has the prescribed row sums in `R`, prescribed column sums in `U` after
the two boundary corrections, and endpoint degrees

\[
 \sum_{R\subset A\subset U}z_{R,U}=2m_A-\epsilon_A.
\tag{1.4}
\]

A one-sided half-edge flow which omits the `U` column sums is not a middle
chronology, even if it is connected.

### Proposition 1.1 (PBBS supplies the disconnected diamond table)

Let

\[
 A_0,A_1,\ldots
\]

run around the canonical PBBS odd-graph factor on the rank-`m` sets of
`[2m+1]`, and project by step two.  Every projected edge
`A_i A_(i+2)` has

\[
 A_i\cup A_{i+2}=\overline{A_{i+1}}.
\tag{1.5}
\]

Consequently the projected PBBS two-factor is upper-perfect: its union
colours enumerate every rank-`m+1` set exactly once.  By the PBBS all-depth
flag theorem its intersection colours cover every rank-`m-1` set.  Hence it
is an integral two-sided diamond table with every intermediate rank-`m`
vertex of degree two.

#### Proof

Odd-graph neighbours `A_i,A_(i+1)` are disjoint and together omit one
coordinate.  Both `A_i` and `A_(i+2)` are disjoint from `A_(i+1)`, so their
union is contained in `overline{A_(i+1)}`.  They are distinct adjacent
rank-`m` vertices in the step-two Johnson projection, and their union has
rank `m+1`; equality in (1.5) follows.  Translation of the index `i+1`
permutes all odd-graph vertices, proving upper perfection.  Complete lower
support is the depth-one case of the PBBS flag theorem. \(\square\)

Thus the diamond equations themselves have no integrality obstruction.
What PBBS does not supply is one linear component with the required
residence and boundary/owner behaviour.  Any joining operation must be
audited on both edge colours; preserving only intersections is insufficient.

At a vertex `A`, every incident edge colour is a facet of `A`; write it
uniquely as

\[
                         R=A-\{x\}.
\tag{1.6}
\]

Let `h_(A,x)` be the number of incident edge copies of this colour.

## 2. Exact transition-system criterion

A **safe local transition system** consists, at each `A`, of

* `epsilon_A` unpaired incident edge copies, globally the two end stubs;
* a pairing of all remaining incident edge copies;
* no pair whose two colours are equal.

For each pair with colours `A-x,A-y`, put

\[
                         \ell_A(x,y)=A-\{x,y\}\in\mathcal S.
\tag{2.1}
\]

Construct the transition graph `K_tau` whose vertices are the edge copies
of `G`, with two edge copies adjacent when they are paired at a common
endpoint.  Every vertex of `K_tau` has degree two except the two edge copies
carrying the global end stubs, which have degree one.  Hence `K_tau` is a
disjoint union of cycles and one path.

### Theorem 2.1 (common-order iff transition path)

There is an Euler trail of `G` whose consecutive edge-colour word has
depth-three multiplicities `d_S` if and only if `G` admits a safe local
transition system such that

\[
 \#\{\text{pairs with label }S\}=d_S
 \qquad(S\in\mathcal S),
\tag{2.2}
\]

and `K_tau` is connected.

#### Proof

An Euler trail orders all edge copies of `G`.  At every internal visit to
`A`, pair the entering copy with the leaving copy; leave the first and last
trail copies unpaired at their respective end vertices.  The resulting
transition graph is the path of edge copies in trail order.  If consecutive
edge colours are `A-x` and `A-y`, their intersection is (2.1), proving
(2.2).  Correct depth-three rank is exactly `x ne y`.

Conversely, if `K_tau` is connected, it is one path through all edge copies.
Read those copies in path order.  Consecutive copies are paired at a common
endpoint of `G`, so they form a trail; every edge copy occurs once, and the
two unpaired stubs give its ends.  Equation (2.1) gives the depth-three row
and (2.2) its multiplicities.  \(\square\)

### Corollary 2.2 (local integer formulation)

For `x ne y` in `A`, let `p_(A,{x,y})` be the number of transition pairs
of omitted-coordinate types `x,y`, and let `u_(A,x)` be the number of end
stubs of type `x`.  Every common ordering satisfies

\[
 \sum_{y\in A\setminus\{x\}}p_{A,\{x,y\}}+u_{A,x}=h_{A,x},
\tag{2.3}
\]

\[
 \sum_{A\supset S}p_{A,A\setminus S}=d_S,
\tag{2.4}
\]

\[
 \sum_{A,x}u_{A,x}=2,
\qquad
 \sum_xu_{A,x}=\epsilon_A.
\tag{2.5}
\]

Conversely, every nonnegative integral solution of (2.3)--(2.5) can be
realized by pairing the distinguishable half-edge copies of each type.  It
gives a common ordering precisely when the resulting `K_tau` is connected.

The local feasibility in (2.3) is a loopless multigraph degree-sequence
condition on the omitted-coordinate types at `A`.  In particular, after
the two end stubs are chosen, it is feasible if and only if the largest
remaining `h_(A,x)` is at most half the remaining degree sum.

## 3. Transition-component joining

### Theorem 3.1 (safe cross-pair and endpoint switches)

Let `tau` be a safe transition system on a connected `G`.  If `K_tau` has
`c` components, there is a sequence of `c-1` local switches which makes
`K_tau` one path.  A pair--pair switch preserves

1. `G`, hence the depth-one vertices, depth-two intersections, and
   middle-owner unions;
2. both endpoint stubs;
3. safety (the two members of every transition pair have distinct colours);
4. the total point-degree vector of the depth-three row.

and replaces exactly two depth-three occurrences by two others.

If two components meet only through an unpaired end stub, a stub--pair
switch merges them while preserving the endpoint owner type and safety, but
moves the stub colour and replaces one boundary depth-three occurrence.
At most one stub--pair switch is needed for each of the two global end
stubs (even if their owner types coincide).  Hence at most two switches in
the whole joining sequence can alter
the endpoint flags or the depth-three point-degree vector.

#### Proof

If `K_tau` is disconnected, connectedness of `G` implies that some owner
vertex `A` has incident edge copies in two different transition components.
Within a transition component, all copies incident at `A` are partitioned
into local pairs, except possibly a global end stub.  First suppose both
components supply an actual pair at `A`.  Write their omitted-coordinate
types as

\[
                         (x,y),\qquad(u,v),
\]

with `x ne y` and `u ne v`.

Delete these two pairing edges.  Cross-pair the four half-edges.  Of the two
cross-pairings

\[
 (x,u),(y,v),\qquad (x,v),(y,u),
\]

at least one has unequal types in both pairs: if the first fails, one of
`x=u,y=v` holds, and the second is then safe because the original pairs
were safe (and symmetrically).  Choose a safe cross-pairing.

There is only one path component in `K_tau`; all other components are
cycles.  Removing one pairing edge from a cycle leaves it connected.  Thus
the cross-pairing merges two cycles into one cycle, or merges the unique
path with a cycle into one path.  It decreases the component count by one.
Iteration proves connectivity and preserves the end stubs.

The old depth-three labels were

\[
 A-\{x,y\},\qquad A-\{u,v\},
\]

and the new labels remove one of the two cross-paired coordinate pairs.
The multiset of four omitted coordinates, with multiplicity, is unchanged.
Therefore the sum of the two label incidence vectors is unchanged, proving
point-degree preservation.  Exactly the displayed two occurrences change.

It remains to treat a contact at which one component contributes only an
unpaired end stub of type `x`, while the other contributes a pair `(u,v)`.
Pair the stub copy with one of the two pair copies whose type is different
from `x`, and leave the other copy unpaired.  This joins the path component
to the cycle, preserves safety and leaves the endpoint at the same owner
`A`, but changes its colour.  It replaces the one old pair label by one new
pair label.  Afterwards the enlarged path component has an actual pair at
`A`, so every later join at that owner is a pair--pair switch.  Only the two
global end stubs can require this exceptional operation.  This
proves all assertions. \(\square\)

### Corollary 3.2 (quantitative common-order bound)

If a feasible local transition system initially has `c` transition
components and depth-three hole count `H_3`, some common Euler order has

\[
                         H_3'\le H_3+2(c-1),
\tag{3.1}
\]

with exactly the same first two row multisets.  All but at most two switches
preserve the endpoint flags and depth-three point degrees; the two possible
exceptions are boundary stub moves, one for each global end stub.

This is only a safe upper bound.  A switch creates no hole whenever each
removed label retains another occurrence.

## 4. Frozen `k=15` implication

The deterministic hypersimplex completion now frozen in the coloured-Euler
note has depth-three load histogram

\[
                         2^{2577}3^{426}.
\tag{4.1}
\]

Thus every rank-five target begins with at least two occurrences.  The two
one-sided adjacent half-edge flows are feasible and can be made connected,
but their explicit trails have large upper-union deficits; they do **not**
yet give a two-sided diamond table.  Moreover, load two does not by itself
guarantee support-preserving joining: the explicit `k=12`, rank-four
counterexample in
`MATH_DEPTH3_LOAD_TWO_JOINING_COUNTEREXAMPLE_20260728.md` has complete
rank-two support of minimum load two, yet every connected final transition
system loses three labels.  The remaining carrier question is equivalently:

> choose a connected depth-one diamond multigraph satisfying all three
> projections (lower colours, upper colours, and intermediate degrees), and
> a safe local transition system satisfying (2.3)--(2.5), with complete
> rank-five support, such that the transition graph is one path.

Once the two-sided `G` exists, Theorem 3.1 proves that transition
connectivity can always be imposed with at most two boundary-marginal
changes.  Under the pair-overlap condition (no component
is attached to the trail solely through an end stub), all point marginals
are retained exactly.  What is not yet proved is that this particular table
has a cut-feasible protected-occurrence transversal and a corresponding
switch sequence and, in the exceptional case, that the two boundary changes
match the prescribed nested end flags.  This is a finite
support-preserving transition-switch problem, strictly smaller than the
full `D_3(15,8)` flow, but it is not implied by the histogram (4.1).

Even a positive solution would settle only the carrier synchronization.
The trace-two fixed-skeleton theorem still requires the induced controller
word to display every residual target as an eligible interval union.
