# Independent audit of the Type-II component/pin extension

> **Prerequisite correction (2026-07-23).**  The component automaton and pin
> consequences audited here remain sound, but the former upstream Type-II
> stability circuit used an A-only singleton-width formula.  Exhaustive
> branch claims for the old combined formula are retracted.  The corrected
> chainwise prerequisite is independently audited in
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## Verdict

**PASS.**  The extension under
`K11_FOREST_RANK_FILTRATION_TYPE2=1` is sound and satisfiability-complete for
the audited two-component consequences in
`BOUNDARY_CORE_PIN_COUPLING.md`.  It adds exactly 7,440 variables and 29,753
clauses, bringing the whole Type-II plan to 9,814 variables and 47,310
clauses.  It allocates and emits nothing when the Type-II guard is absent.

## 1. Consequences already present

The old circuit counts actual rank-at-most-four components, not selected
witness components.  Its coupled row is exactly `delta_5+s<=2` under the
canonical WLOG singleton selection.  Since `delta_5>=0`, `s=2` forces
`delta_5=0`.  Thus the proposed additional duplicate-zero unit would be
redundant.

With no duplicate literal five-set, the selected non-singleton five-set
witnesses lie wholly in the two low components.  Their total slack is three,
and positivity of each component slack forces `{1,2}`.  This is a theorem
about every satisfying array and canonical witness choice; no free integer
assignment is missing from the CNF.

## 2. Prefix automaton

The four clauses used for

```text
z <-> x OR (y AND w)
```

are the two forward implications and the two prime reverse clauses
`z->x OR y`, `z->x OR w`.  Exhausting all eight input triples confirms exact
truth-table equivalence.

The recurrence counts whether at least one and at least two component starts
have appeared.  The old exact `components<=2` comparison then makes the final
`seen_two` literal equivalent to `components=2`.  Exhaustive enumeration of
all binary words through length ten confirms that `first_low` and
`second_low` are precisely the two maximal low runs, including runs touching
either physical endpoint.

## 3. Coordinate selector

The selector clauses are exact-one conditional on `components=2` and force
both selector bits false otherwise.  The exact `chosen_low` definition is the
membership indicator of the selected component.  For every coordinate, an
exact prefix recurrence ORs the array-bit occurrences over those positions.
Requiring its final value makes all eleven coordinates occur in one common
component; the choice cannot vary by coordinate.

Conversely, if one component has OR `[11]`, choose that selector.  The exact
prefix recurrences then end true for all coordinates.  The deterministic
construction has no symmetric existential occurrence choices.

## 4. Slack-one pair support

For every adjacent physical pair `[p,p+1]`, the production support enumerates
all central rank-five states with those exact endpoints.  Independent
enumeration confirms that each of the 464 supports is nonempty, contains at
most three literals, and contains no state for another interval.

When the pair lies in the selected slack-one component, its guarded clause
forces one support literal.  The base central encoding makes the associated
physical interval's OR equal the slot value and gives that value exact rank
five.  Coverage of all 462 target masks by 462 exact-rank slots makes the slot
values a permutation, so different forced pairs have different values.

For completeness, in any genuine two-component Type-II word choose all
literal five-set singleton witnesses.  The coupled theorem makes these
values distinct.  In the slack-one component, its `m-1` assigned five-set
witnesses are exactly its `m-1` adjacent pairs.  Retaining those witnesses
and arbitrary witnesses for all remaining five-sets, then sorting by left
endpoint, gives a legal monotone central schedule containing every forced
pair.  The band and joint cuts are universal for independently selected
rank-five/rank-six schedules, so this re-selection preserves every
prerequisite.

The forced pair row itself proves slack one: no other selected rank-five
interval can properly contain a forced rank-five pair without duplicating an
equal-rank value.  Total slack three then makes the other component's slack
two.  It also makes every length-at-least-two interval in the chosen
component rank at least five, proving the literal-only lower-target
consequence.

## 5. Inventory

The independently recomputed extension is:

```text
automaton variables  = 4*464 = 1856
automaton clauses    = 464*(3+4+3+3) = 6032
selector variables   = 4
chosen-component flags = 465
coordinate prefixes    = 11*465 = 5115
coordinate clauses     = 4 + 5*465 + 11*(3+4*464+1) = 22789
pair clauses         = 4 + 2*464 = 932
```

Hence

```text
new variables = 1856+4+465+5115 = 7440
new clauses   = 6032+22789+932 = 29753
total variables = 2374+7440 = 9814
total clauses   = 17557+29753 = 47310.
```

Production diagnostics match each subtotal exactly.  The checker

```text
python3 scratch/verify_k11_rank_filtration_type2_components.py
```

prints

```text
type2_component_automaton=PASS
type2_coordinate_selector=PASS
type2_adjacent_pair_support=PASS
type2_variables=9814 clauses=47310 PASS
```

The source compiles cleanly with `-Wall -Wextra -Wpedantic`.  The enabled
three-prerequisite build reports 4,968,514 variables and 15,890,681 clauses;
the all-off baseline remains 4,892,622 variables and 15,524,818 clauses.

## 6. Scope

This audit establishes exactness of a formula reduction, not satisfiability
or unsatisfiability of the branch.  The coordinate-complete component need
not cover every mask, and no claim is made about a canonical order inside the
slack-two component.
