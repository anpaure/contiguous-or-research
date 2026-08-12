# Min-cost owner-area rounding and automatic q1 propagation

**Date:** 2026-08-04  
**Method:** pure mathematics; integral min-cost flow; no computation or
search  
**Status:** unconditional network-flow theorem.  It converts an aggregate
fractional owner-layer current bound into one integral disjoint linkage with
the same owner-area bound, then derives a quadratic q1 projection without
path monotonicity.  The present Pascal/common-cap construction still has to
supply the fractional current in one typed physical state.

## 0. Main result

Let `D` be one finite directed common-cap network after every physical
unit-capacity vertex has been node-split.  Add a super-source with unit arcs
to `q` distinct claim starts and a super-sink with unit arcs from the legal
sink bank.  Let `O` be the set of split capacity arcs corresponding to
rank-`m` owner occurrences.

Assign cost one to every arc in `O` and cost zero to every other arc.

### Theorem 0.1 (fractional owner current rounds without loss)

Suppose `D` has a feasible fractional flow of value `q` whose total load on
the owner-capacity arcs is at most `L`:

\[
                         \sum_{e\in O}x_e\le L.
\tag{0.1}
\]

Then `D` has an integral value-`q` flow, and hence `q` pairwise
vertex-disjoint claim-to-sink paths, whose union uses at most

\[
                         \boxed{\lfloor L\rfloor}
\tag{0.2}
\]

rank-`m` owner occurrences.  Its number of distinct Boolean owner values is
no larger.

This conclusion requires no bound on the number of rank changes, no
monotonicity of the paths, and no prescribed route for any individual
claim.

## 1. Proof by integral min-cost flow

Among all value-`q` fractional flows, minimize the nonnegative integral arc
cost defined above.  Hypothesis (0.1) makes the optimum at most `L`.

The node-split network has integral capacities, supplies and demands.
The min-cost-flow polytope is integral, so it has an integral optimum
`y` of value `q`.  Its cost is an integer and obeys

\[
 \sum_{e\in O}y_e\le L,
\]

hence is at most `floor(L)`.

Delete directed flow cycles.  Costs are nonnegative, so this cannot
increase cost.  The remaining integral flow decomposes into `q` paths from
the `q` unit source arcs to distinct unit sink arcs.  Node splitting makes
the paths vertex-disjoint.  Every used owner occurrence contributes its
unit capacity arc once, so the cost is exactly their number.  Projection
from occurrences to Boolean values can only identify records and therefore
cannot increase the count.  This proves Theorem 0.1.

## 2. Automatic terminal propagation

Let `Z` denote the rank-`m+1` q1 terminal occurrences used by the integral
linkage.  Project the used owner and terminal occurrences to Boolean value
sets `D_U,D_Z`.

Let `E_Z` be the terminal values for which no used occurrence is joined on
its selected path by a Boolean rank-`m` to rank-`m+1` containment edge to a
used owner occurrence.  Put `e=|E_Z|`.

### Theorem 2.1

The integral linkage supplied by Theorem 0.1 satisfies

\[
 \boxed{
 |D_Z|\le(m-1)\lfloor L\rfloor+e.
 }
\tag{2.1}
\]

#### Proof

Every nonexceptional used terminal value contains at least one used owner
value.  A rank-`m` owner on a `2m-1` element ground set has exactly `m-1`
rank-`m+1` supersets.  Take the union of those neighbourhoods over the at
most `floor(L)` used owner values and add the exception bank.  \(\square\)

In particular, if `L=O(m)` and `e=O(m^2)`, the owner and q1 terminal
projections satisfy exactly the linear/quadratic Regenerative Owner Area
rows.  If every used q1 terminal lies on an owner--terminal incidence edge
of its path, then `e=0`.

## 3. Regular fractional bundles give an explicit owner budget

Let `G` be `q` claims and let `B=(G,P;E)` be a left-`h`-regular,
right-at-most-`h` incidence factor.  Suppose every incidence `gp` has one
complete typed path `Q_(gp)` in the same node-split state, and the standard
privacy/congestion hypotheses make the flow which sends `1/h` along every
`Q_(gp)` feasible.

Let `ell_(gp)` be the number of owner-capacity arcs on `Q_(gp)`.  The total
owner cost of that fractional flow is

\[
 L_{\rm frac}
 ={1\over h}\sum_{gp\in E}\ell_{gp}.
\tag{3.1}
\]

### Corollary 3.1 (average-length, not pathwise, control)

There is an integral linkage of all `q` claims using at most

\[
                         \boxed{\lfloor L_{\rm frac}\rfloor}
\tag{3.2}
\]

owner occurrences.

It is enough that the average owner count over the `hq` displayed paths be
at most `ell`; then

\[
                         L_{\rm frac}\le q\ell.
\tag{3.3}
\]

Thus `q=O(sqrt(m))` and average owner count `ell=O(sqrt(m))` imply linear
owner area.  Individual paths may be much longer or nonmonotone, provided
the weighted aggregate (3.1) is linear.

#### Proof

The regular-factor fractional routing sends `1/h` on every complete path.
Summing its load on owner-capacity arcs gives (3.1).  Apply Theorem 0.1.
(\square\)

## 4. Direct interface with active wedge materialization

Suppose the integral linkage is the frozen compensation/background bank
against which the active-wedge atlas is formed.  If

\[
 L\le Am,
 \qquad e+H\le Em^2,
\tag{4.1}
\]

where `H` is the total explicitly priced hidden wedge-hole bank, then
Theorem 2.1 gives

\[
 |D_U|=O(m),
 \qquad |D_Z|+H=O(m^2).
\tag{4.2}
\]

The active cycle-aligned wedge theorem then leaves only an absolute number
of cap casualties for `p=O(sqrt(m))`, while simultaneously aligning each
surviving active edge with its Boolean linkage assignment and literal q1
factor occurrence.

Hence a sufficient replacement for path-monotonicity is the single
aggregate certificate

\[
 \boxed{
 \text{one feasible fractional compensation current of value q
 with owner load O(m).}
 }
\tag{4.3}

The certificate must be computed after fixing the same type/phase/guard
state and every shared capacity.  Fractional currents living in different
states cannot be averaged.

## 5. Regenerative min-cost owner-current invariant

The following is sufficient for the cap row of an additive-constant
same-parity induction.

> **Regenerative MCOC.**  At every transition, in one fixed complete state:
>
> 1. the transported background/compensation demands admit a value-full
>    fractional flow with total rank-`m` owner load at most `Am`;
> 2. terminal-only and hidden wedge exceptions total at most `Em^2`;
> 3. the surviving active menus satisfy the selection-stable typed privacy
>    interface of the active cycle-aligned theorem; and
> 4. after integral rounding and wedge/factor completion, the child exports
>    a fresh certificate with the same constants rather than accumulating
>    all ancestral footprints.

### Theorem 5.1

Regenerative MCOC implies a bounded one-coordinate common-cap sidecar.  If
the other carrier, upper, residence, topology, compiler and two-coordinate
rows also regenerate with bounded defect, then

\[
                         \nu(k)\le B(k)+O(1).
\]

#### Proof

Round the fractional background by Theorem 0.1.  Apply Theorem 2.1 to its
q1 projection, then the layer-energy form of the active cycle-aligned
wedge theorem.  This loses only a constant number of tasks.  Item 4 keeps
that sidecar bounded across transitions rather than summing it.  The final
bounded-defect terminal theorem appends only a constant number of literal
masks.  \(\square\)

## 6. Sharp scope

The theorem closes an **integral rounding** gap, not a fractional existence
gap.  It does not prove that the present Pascal child has the fractional
current (4.3), that terminal-only exceptions are quadratic, or that the
rounded linkage is compatible with the second occurrence coordinate.

Two marginal fractional currents in separate coordinate networks do not
give one common product-cap flow.  Shared capacities must be allocated in
one joint node-split network before Theorem 0.1 is applied.

Likewise, a fractional flow which records only abstract Boolean values but
not physical occurrence capacities is insufficient: its min-cost integral
rounding lives in the same network in which the fractional flow was
certified.

## 7. Dependencies

- integral min-cost-flow theorem;
- `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`;
- `MATH_THEOREM_AUTOMATIC_PROTECTED_TURN_LIFT_AND_REGENERATIVE_OWNER_AREA_20260804.md`;
- `MATH_THEOREM_ACTIVE_CYCLE_ALIGNED_WEDGE_LINKAGE_AND_LAYER_ENERGY_20260804.md`.
