# Exact Type-II component/pin encoding

> **Prerequisite note.**  The component extension remains valid, but it must
> be paired with the corrected chainwise Type-II stability circuit audited in
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## Verdict

The guarded `K11_FOREST_RANK_FILTRATION_TYPE2=1` module now includes every
cheap array-level consequence of the audited two-component escape in
`BOUNDARY_CORE_PIN_COUPLING.md`:

* when there are two physical rank-at-most-four components, the existing
  coupled stability row already forces rank-five duplicate excess zero;
* the two component slacks are `{1,2}`;
* at least one component has coordinate union `[11]`;
* every internal adjacent pair of the slack-one component is one of the
  already selected 462 rank-five witnesses.

The last clause forces those adjacent-pair ORs to be distinct five-sets.  It
also implies that every lower target represented in that component is a
literal entry.  No target/component assignment variables are required.

The extension adds 7,440 variables and 29,753 clauses to the previous Type-II
plan.  The complete Type-II module is now

```text
9,814 variables / 47,310 clauses.
```

With the guard absent it still allocates no variable and emits no clause.

## 1. What was already automatic

Write `n5` for the number of literal rank-five entries, `y0` for the number
of selected singleton rank-five witnesses, `delta=n5-y0`, and `s` for the
number of physical rank-at-most-four components.  The pre-existing exact row

```text
n5+h6+s <= h1+464
```

is `delta+s<=2`, since `y0=h1+462-h6`.  If `s=2`, it gives `delta=0` because
`y0<=n5`.  Thus every literal five-set is distinct and all of them are chosen
as singleton witnesses in this subcase.

After deleting the literal five-set positions, all remaining selected
five-set witnesses lie in the two low components.  Their total interval slack
is

```text
d+c-delta = 2+1-0 = 3.
```

Every nonempty low component has positive slack, so the two slacks are
exactly `{1,2}`.  These facts follow logically from the existing CNF and need
no second scalar counter.

## 2. Exact component automaton

Let `low[p]=!rank5[p]`, and let `start[p]` be the already exact component-start
literal.  The new prefix state is

```text
seen_one[p] <-> OR_(q<=p) start[q],
seen_two[p] <-> at least two starts occur by p.
```

It is implemented recursively by

```text
seen_one[p] <-> seen_one[p-1] OR start[p],
seen_two[p] <-> seen_two[p-1]
                 OR (seen_one[p-1] AND start[p]).
```

All gates are bidirectional.  Since the old circuit enforces `s<=2`,
`seen_two[464]` is exactly the branch literal `s=2`.  Exact membership flags
are

```text
first_low[p]  <-> low[p] AND !seen_two[p],
second_low[p] <-> low[p] AND  seen_two[p].
```

This uses 1,856 variables and 6,032 clauses.

## 3. Coordinate-complete component

Conditional on `s=2`, an exact-one selector chooses the first or second low
component.  Exact `chosen_low[p]` flags materialize that component.  For each
coordinate `b`, a deterministic prefix OR records whether `b` has occurred
at a chosen position; its final flag is required.

Therefore the selected component has total OR `[11]`.  Conversely, if either
component is coordinate-complete, selecting it makes every final prefix flag
true.  This is an exact deterministic encoding of the coordinate-transversal
consequence, not a relaxation, and avoids symmetric occurrence witnesses.

It uses 5,582 variables (465 selected-component flags, 5,115 prefix flags,
and two selector bits) and 22,789 clauses.

## 4. Slack-one adjacent-pair row

A second exact-one selector chooses the slack-one component.  For each
physical adjacent pair `[p,p+1]` internal to that component, one clause forces
the pair to occur in the existing selected rank-five schedule.

For a fixed pair, the support is the at-most-three central state literals

```text
rank_five.state[i][alpha,beta]
```

whose physical endpoints satisfy

```text
i+alpha=p, i+beta=p+1.
```

Every selected central value has exact rank five.  The 462 slots cover all
462 rank-five targets, so their values are a permutation of that layer.
Consequently forcing every internal pair into this row gives both exact rank
five and pairwise distinctness.

This loses no Type-II array.  In the two-component branch, choose singleton
witnesses for the distinct literal five-sets and choose every adjacent pair
in the slack-one component for its five-set value.  Complete the remaining
targets with arbitrary old witnesses and sort by endpoints.  Equal-rank
incomparability gives a valid monotone central schedule, and all universal
band/joint inequalities remain valid for this witness choice.

The two selector variables and 928 guarded pair clauses cost 2 variables and
932 clauses.

## 5. Why the other component has slack two

If the selected slack-one component has length `m`, all `m-1` internal pairs
are selected witnesses.  No longer selected five-set interval can lie in
that component: it would contain one of those pairs, and equal rank would
force a duplicate target.  Hence its slack is exactly one.  Since the total
slack is three, the other component has slack exactly two.

Every interval of length at least two inside the slack-one component contains
a selected rank-five pair.  Its OR therefore has rank at least five, so any
rank-at-most-four value represented there must be a singleton entry.

## 6. Inventory and checks

| extension | variables | clauses |
|---|---:|---:|
| component prefix automaton and labels | 1,856 | 6,032 |
| coordinate-complete selector, membership, and prefix ORs | 5,582 | 22,789 |
| slack-one selectors and pair supports | 2 | 932 |
| **new extension** | **7,440** | **29,753** |
| previous Type-II plan | 2,374 | 17,557 |
| **complete Type-II plan** | **9,814** | **47,310** |

The independent checker

```text
python3 scratch/verify_k11_rank_filtration_type2_components.py
```

exhausts every binary pattern through length ten having at most two low
components, checks all component labels and the exact two-component branch
literal, checks the nontrivial prefix-gate truth table, verifies every one of
the 464 physical pair-support lists, and recomputes the complete inventory.

A build with the three original prerequisites reports

```text
variables=4968514 clauses=15890681
rank_filtration_type2_variables=9814
rank_filtration_type2_clauses=47310
rank_filtration_type2_component_automaton_clauses=6032
rank_filtration_type2_coordinate_separator_clauses=22789
rank_filtration_type2_slack_one_pair_clauses=932.
```

The all-guards-off build remains

```text
variables=4892622 clauses=15524818.
```

## 7. Scope

These are necessary branch cuts, not a SAT or UNSAT result.  Coordinate
completeness means only that a component's total OR is `[11]`; it does not
make the component universal.  The slack-two component remains structurally
flexible.  A satisfying model still requires both independent interval-OR
verifiers, and an unsatisfiable run requires an archived proof certificate.
