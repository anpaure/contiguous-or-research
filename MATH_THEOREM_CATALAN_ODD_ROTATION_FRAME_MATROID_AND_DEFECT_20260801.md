# Odd rotation factors: an exact signed-frame topology quotient

Date: 2026-08-01  
Status: exact topology compression for odd `m`.  Literal forestness and its
minimum deletion defect become signed-graphic frame-matroid independence and
nullity on the necklace quotient.  Outer margins and middle capacity remain
separate correlated constraints.

## 0. Outcome

Let `m=2h+1` and let `F` be a `C_(2m)`-invariant exact outer factor with
literal middle degree at most two.  After quotienting the physical middle
support by rotation:

* every selected full/full outer orbit becomes an ordinary edge between
  free middle necklaces, possibly an ordinary loop;
* every selected half/half antipodal outer orbit becomes a distinguished
  negative half-loop at one free middle necklace.

Let `G_F` be this signed quotient graph.  Then

\[
 \boxed{
 F\text{ is a literal linear forest}
 \iff
 G_F\text{ is independent in the signed-frame matroid}.}
                                                               \tag{0.1}
\]

Concretely, delete the negative half-loops and call the remaining ordinary
multigraph `G_0`.  Condition (0.1) says exactly:

1. `G_0` is a forest (so an ordinary loop and an ordinary parallel cycle
   are forbidden); and
2. each tree component of `G_0` carries at most one negative half-loop.

The exact topological defect is the frame nullity

\[
 \delta_{\rm fr}(F)=|E(G_F)|-r_{\rm fr}(E(G_F)).       \tag{0.2}
\]

It is the minimum number of complete quotient edge-orbits which must be
deleted to make the literal lift a forest.  Thus `delta_fr=O(1)` is the
right bounded central connector target when a bounded number of exact
rotation-closed operations may be exported.

This is a genuine matroid reduction of the topology row.  It does not make
the two outer partition bases or the literal cap rows into matroids, so the
entire selector is still not ordinary matroid intersection.

## 1. Only free middle necklaces occur in the full sector

Let `alpha` be a full/full outer-simple diamond orbit.  It contains `2m`
diamonds.  If one physical endpoint has middle-necklace stabilizer order
`s`, then every literal vertex of that necklace receives load `s` from
`alpha` when only one endpoint role lies in that necklace, and load `2s`
when both endpoint roles lie in it.

Indeed the orbit has respectively `2m` or `4m` endpoint incidences, spread
uniformly over a necklace of size `(2m)/s`.

For odd `m`, every middle stabilizer order divides `m`; hence a nontrivial
one is at least three.  The literal cap-two condition therefore excludes it.
Every selected full/full orbit has free middle endpoints.  If the two
endpoint necklaces are equal its quotient edge is an ordinary loop and its
literal load is two; otherwise it contributes one at each quotient end.

For a half/half orbit, Section 2 of
`MATH_THEOREM_CATALAN_ROTATION_PARITY_SECTOR_AND_SLACK_DESIGN_20260801.md`
shows that its two endpoints lie in one free middle necklace and differ by
the half-turn `rho^m`.  The diamond orbit has only `m` distinct unoriented
edges, so it gives a perfect matching on that necklace and literal load one.
This is the negative half-loop.

## 2. Lift criterion

### Theorem 2.1 (frame-independence equivalence)

The literal physical lift of a quotient edge set is a forest if and only if
its ordinary quotient edges form a forest and no ordinary tree component
contains two negative half-loops.

#### Proof

Choose one representative in every free middle necklace and put the usual
`Z_(2m)` voltage on every ordinary quotient edge.  The lift of an ordinary
quotient tree is a disjoint union of trees.

One negative half-loop joins sheet `i` to sheet `i+m`.  On a lifted ordinary
tree it pairs two previously disjoint tree copies by one edge in each pair;
the result is still a forest.

Two negative half-loops in the same ordinary tree component create a lifted
cycle: traverse the first half-loop, the unique lifted tree path to the
second, the second half-loop, and the reverse lifted tree path.  Its net
voltage is `m+m=0 mod 2m`, and no edge is repeated.

An ordinary quotient cycle also creates a literal cycle.  If its total
voltage is `v`, repeat the lifted circuit `ord(v)` times; because the group
is finite this closes, and a shortest closing repetition is a simple lifted
cycle.  Ordinary loops and parallel two-cycles are included.

These are the only possibilities.  If the ordinary quotient is a forest
with at most one negative half-loop per component, the preceding component-
by-component construction explicitly gives a literal forest.  \(\square\)

The independence system in Theorem 2.1 is precisely the frame matroid of
the signed graph in which ordinary edges are positive and the distinguished
half-loops are negative.

## 3. Exact rank and defect formula

Let `G_0` contain all ordinary edges, including ordinary loops.  Delete the
ordinary loops temporarily when counting connected components.  Let

* `V_0` be the quotient vertices incident with at least one selected edge;
* `c_0` be the number of connected components of the non-loop ordinary
  graph on `V_0`;
* `u_0` be the number of those components which contain at least one
  negative half-loop;
* `e_0` be the number of ordinary edges, with loops counted; and
* `q_0` be the number of negative half-loops.

Then

\[
 r_{\rm fr}=|V_0|-c_0+u_0,                            \tag{3.1}
\]

\[
 \boxed{
 \delta_{\rm fr}=e_0+q_0-|V_0|+c_0-u_0.}             \tag{3.2}
\]

#### Proof

Inside each ordinary connected component, a spanning tree contributes
`|V|-1` independent edges.  If the component has a negative half-loop,
exactly one such loop may be added independently.  Every further ordinary
edge or negative half-loop closes one of the circuits from Theorem 2.1.
Summing gives (3.1)--(3.2).  \(\square\)

Formula (3.2) remains correct when a component consists of one vertex and
only half-loops or ordinary loops.  An ordinary loop adds defect one; the
first negative half-loop adds rank one and each further one adds defect one.

## 4. Relation to pentagonal orbit banks

A clean rotation-closed pentagonal bank is an alternating quotient `C6` in
the outer matching.  Its old/new replacement preserves both partition-base
margins.  On odd `m`, after the literal cap check, its topology effect is
measured exactly by

\[
 \delta_{\rm fr}(F^{p})-\delta_{\rm fr}(F).           \tag{4.1}
\]

Thus the forest-or-bank programme may be weakened without ambiguity:

> Find an exact selector with bounded frame nullity, or prove that every
> selector of unbounded frame nullity has a clean cap-feasible pentagonal
> bank which strictly lowers (3.2).

The first alternative is already sufficient for any architecture which can
export a bounded number of rotation-closed connector tasks.  Exact zero
nullity is stronger than necessary there.

The finite factors through `m=8` have at most one orbit of literal cycle
components.  In odd dimensions the replay below verifies that their frame
nullities are respectively one, zero, and zero for `m=3,5,7`.

## 5. Mechanical replay

Run

```text
python3 scratch/audit_catalan_odd_rotation_frame_matroid_20260801.py
```

It reconstructs the frozen odd factors, builds the signed quotient, checks
the rank formula, and independently compares frame independence with literal
forestness and the orbit count of literal cycle components.

