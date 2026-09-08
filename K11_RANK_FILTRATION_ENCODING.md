# Exact `k=11` Type-II rank-filtration encoding

> **Historical/superseded circuit.**  The A-only singleton-width equation in
> this version is not complete for rank-five chains B/C.  Use the corrected
> formulas and frozen source described in
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

> **Update.**  The 2,374-variable / 17,557-clause inventory below is the
> foundational rank/component subcircuit.  The same guard now also encodes
> the audited two-component coordinate separator and slack-one pair row.
> The current complete inventory is 9,814 variables / 47,310 clauses; see
> `K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING.md` and its audit.

## Status

`k11_forest_sat.cpp` now contains an opt-in exact encoding of the Type-II
rank-filtration branch behind

```text
K11_FOREST_RANK_FILTRATION_TYPE2=1.
```

It requires

```text
K11_FOREST_LOCAL_DENSITY_PB=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1.
```

The first prerequisite supplies exact one-hot literals for every physical
entry rank.  The latter two supply the exact selected rank-five width
boundaries.  The option is rejected with `K11_FOREST_RANK6_BRANCH=1`; it is
compatible with an absent rank-six branch or with branch zero.

The source before this edit had SHA-256

```text
3f2cb0564f0bada5b14c9c1746668401e5cccdc5f52f330ae7f8498ec8e68544.
```

The implementation adds exactly 2,374 variables and 17,557 clauses when
enabled.  It allocates and emits nothing when disabled.

## 1. Mathematical branch

At `k=11,n=465`, exact rank-six filtration has two cases.  Type II has no
literal six-set.  Applying rank-five stability with excess

```text
465-beta_5(11)=465-464=1
```

gives, with `delta_5` the duplicate excess of literal five-sets and `s` the
number of rank-at-most-four components,

```text
delta_5+s-1 <= 1.                              (1.1)
```

Rank-six equality also gives `|A[p]|<=6`, so absence of a literal six-set
sharpens this to `|A[p]|<=5` for every position.  Rank-four truncation gives
at least `beta_4(11)=331` positions of rank at most four, hence at most

```text
465-331=134
```

rank-five entries.  Thus Type II satisfies all of the following:

```text
all entry ranks are at most five;
n5 <= 134;
the rank-at-most-four positions have at most two components;
delta_5 <= 1;
delta_5+s <= 2.                                (1.2)
```

The implementation includes the sharp coupled row, not merely its two
separate consequences.

## 2. Reused exact rank layer

`LocalDensityPBPlan::rank[p][t]` is already an exact one-hot encoding of

```text
|A[p]|=t,  0<=t<=11.
```

The Type-II plan emits the 2,790 units

```text
-rank[p][t],  p=0,...,464, t=6,...,11.          (2.1)
```

The inherited nonzero array clause rules out rank zero.  Hence rank at most
four is exactly the negation of `rank[p][5]`.

An exact Wallace count of the 465 rank-five flags gives the binary integer
`n5`; the direct first-difference comparator enforces `n5<=134`.

## 3. Exact component count

Define the component-start literals

```text
c_0 = !rank[0][5],
c_p = rank[p-1][5] AND !rank[p][5],  1<=p<=464. (3.1)
```

The 464 nontrivial starts use exact three-clause AND-NOT definitions.  Since
all entries have rank at most five, the sum of (3.1) is exactly the number
`s` of physical rank-at-most-four components.  A second exact Wallace count
and direct comparator enforce

```text
s<=2.                                           (3.2)
```

This is the original physical word, not a selected-witness or compressed-word
surrogate.

## 4. Exact duplicate/component coupling

For completeness we choose rank-five witnesses canonically: every distinct
literal five-set is assigned one of its singleton occurrences, and every
nonliteral five-set uses any old witness.  Equal-rank incomparability still
puts these 462 chosen intervals into the existing monotone central schedule.
All previously proved band and cross-layer inequalities remain valid for
this choice.

Let `y0` be the number of selected rank-five singleton witnesses.  Under this
choice,

```text
y0 = number of distinct literal five-set values,
delta_5 = n5-y0.                                (4.1)
```

The three possible rank-five state chains all start at state `00` and end at
state `33`.  If `h1` counts the first state and `h6` counts the first six of
the seven chain states, the existing exact boundary bits give

```text
y0 = h1+(462-h6).                               (4.2)
```

Substituting (4.1)--(4.2) into (1.1) gives the single exact integer row

```text
n5+h6+s <= h1+464.                              (4.3)
```

Both sides of (4.3) are formed by bidirectional ripple adders and compared by
an exact bidirectional prefix comparator.  Conversely, any Type-II array has
the canonical witness choice above, so (4.3) loses no Type-II solution.

## 5. Circuit inventory

The independent gate accounting is:

| module | variables | clauses |
|---|---:|---:|
| forbid ranks 6--11 | 0 | 2,790 |
| two 465-input Wallace counts | 1,844 | 12,908 |
| 464 component-start definitions | 464 | 1,392 |
| constant comparisons `n5<=134`, `s<=2` | 0 | 14 |
| three additions in (4.3) | 56 | 392 |
| final width-11 comparison | 10 | 61 |
| **total** | **2,374** | **17,557** |

The two Wallace circuits each use 461 exact full adders.  Every full adder
uses two variables and fourteen clauses.

## 6. Build-only regression

The source compiles cleanly against the local CaDiCaL API stub with

```text
g++ -O2 -std=c++20 -Wall -Wextra -Wpedantic \
  -Iscratch/cadical_stub k11_forest_sat.cpp -o /tmp/k11_rank_filtration_test
```

With all optional guards absent it reproduces the established baseline:

```text
variables=4892622 clauses=15524818
rank_filtration_type2=0.
```

With exactly the three prerequisites, before enabling Type II:

```text
variables=4958700 clauses=15843371.
```

With Type II enabled:

```text
variables=4961074 clauses=15860928
rank_filtration_type2_variables=2374
rank_filtration_type2_clauses=17557
rank_filtration_type2_rank_cap_clauses=2790
rank_filtration_type2_component_definition_clauses=1392.
```

The delta is exactly the audited plan inventory.  With the existing
canonical/boundary gates and `K11_FOREST_RANK6_BRANCH=0`, the compatible build
reports

```text
variables=4961074 clauses=16075759.
```

Guard-alone and branch-one combinations are rejected before allocation with
exit status 2 and explicit diagnostics.

## 7. Type-I reuse

The existing rank-six modules already encode the first Type-I shell exactly:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_RANK6_BRANCH=1.
```

Together they fix the sole literal six-set, up to coordinate and reversal
symmetry, to `A[0]=63`.  Therefore no second rank-six boundary gate is needed.

They do **not** by themselves encode the lower Type-I onion: after deleting
`A[0]`, literal rank-five entries must be distinct, rank-at-most-four entries
must form one component, every remaining entry must have rank at most five,
and `n5<=133`.  The current `e1c2` minimal-component module concerns the
selected rank-five/rank-six witness forest and is not a replacement for those
literal array-rank conditions.  A future Type-I array plan can reuse the same
one-hot and boundary counters with the specializations

```text
s=1, delta_5=0, n5<=133,
```

while reusing the already exact `A[0]=63` branch anchor.

## 8. Scope

This option is an exact satisfiability-preserving encoding of the complete
Type-II array-rank architecture.  SAT still needs independent interval-OR
verification.  UNSAT with this guard excludes Type II only; a global
`n=465` refutation also requires the Type-I branch and checked proof traces.
