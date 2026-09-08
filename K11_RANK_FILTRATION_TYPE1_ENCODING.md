# Exact `k=11` Type-I rank-filtration encoding

> **Historical/superseded circuit.**  The A-only singleton-width equality in
> this version omits states `22`/`11` on chains B/C.  The corrected chainwise
> implementation is audited in
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## Status

The complementary literal-six-set branch is now encoded behind

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1.
```

It requires

```text
K11_FOREST_LOCAL_DENSITY_PB=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
K11_FOREST_RANK6_BRANCH=1.
```

The last prerequisite already requires the canonical rank-six mask gate and
the oriented rank-six boundary gate.  Together those existing modules fix

```text
A[0]=63
```

as the unique literal rank-six entry.  The new module therefore begins with
the exact 464-position suffix left after deleting that endpoint.

The edit started from source SHA-256

```text
3a51bcf5f181d0a31f5cceac1e94f19079355b02aad60516be9bc626c1b5dec8
```

and produced

```text
ab9a3e1cce0325469adbb57d8c39c9a5b660f194c20b9ff6b099497f0ba9c4ea.
```

The guard adds exactly 2,341 variables and 17,354 clauses.  With the guard
absent it allocates and emits nothing; the existing Type-II plan is unchanged.

## 1. Exact Type-I structure

At `k=11,n=465`, Type I has one literal six-set at an endpoint.  Deleting it
leaves a word of length

```text
464=beta_5(11)
```

covering every mask through rank five.  Exact rank-five filtration gives:

```text
every suffix entry has rank at most five;
all literal rank-five values are distinct;
the rank-at-most-four suffix positions form one nonempty component.
```

That low core itself covers ranks one through four, so it has length at least
`beta_4(11)=331`.  Consequently the number `n5` of literal rank-five entries
satisfies

```text
n5<=464-331=133.                                (1.1)
```

These are actual array-entry and physical-component statements, not merely
selected-witness profile constraints.

## 2. Reused rank and branch layers

The existing branch-one anchor already gives `A[0]=63` and forbids any other
literal six-set.  `LocalDensityPBPlan::rank[p][t]` is an exact one-hot encoding
of `|A[p]|=t`.  The Type-I module emits

```text
-rank[p][t],  p=1,...,464, t=6,...,11,           (2.1)
```

for exactly 2,784 rank-cap clauses.  Position zero is deliberately omitted:
its exact rank-six value is supplied by the branch-one anchor.

An exact 465-input Wallace/ripple count of `rank[p][5]` gives `n5`.  Position
zero contributes zero automatically.  A direct first-difference comparison
enforces (1.1).

## 3. One exact suffix component

Because (2.1) and the base nonzero clauses restrict suffix ranks to 1--5,
rank at most four is exactly `!rank[p][5]`.  Its suffix component starts are

```text
c_1 = !rank[1][5],
c_p = rank[p-1][5] AND !rank[p][5], 2<=p<=464.   (3.1)
```

The 463 nontrivial starts are exact three-clause AND-NOT gates.  A second
exact Wallace/ripple count materializes

```text
s=sum_(p=1)^464 c_p.
```

The nine output bits are fixed to binary one.  Hence the rank-at-most-four
positions in the suffix form exactly one nonempty physical component.  Both
suffix boundaries are handled: a component beginning at position one is
counted by `c_1`, and a component ending at position 464 needs no artificial
closing marker.

## 4. Duplicate-free literal five-sets

Choose, WLOG, one singleton selected witness for every distinct literal
rank-five value.  Retain arbitrary witnesses for nonliteral rank-five targets.
The selected intervals remain incomparable and therefore fit the existing
monotone central schedule.  Under this choice,

```text
y0 = number of distinct literal rank-five values.
```

The three allowed rank-five state chains all have width-zero states only at
their first and last vertices.  With the existing exact chain boundaries,

```text
y0=h1+(462-h6).                                 (4.1)
```

Literal rank-five values are duplicate-free exactly when `n5=y0`.
Substituting (4.1) gives

```text
n5+h6=h1+462.                                   (4.2)
```

Both sides of (4.2) are exact, nonmodular ten-bit ripple sums.  Twenty binary
equivalence clauses impose equality bit by bit.  Conversely, every valid
Type-I array admits the aligned singleton witness choice, so this WLOG
encoding loses no Type-I solution.

## 5. Exact circuit inventory

| module | variables | clauses |
|---|---:|---:|
| suffix rank cap | 0 | 2,784 |
| 465-input `n5` count | 922 | 6,454 |
| 464-input component count | 920 | 6,440 |
| 463 component-start definitions | 463 | 1,389 |
| `n5<=133` | 0 | 6 |
| exact component value one | 0 | 9 |
| two additions in (4.2) | 36 | 252 |
| bitwise equality in (4.2) | 0 | 20 |
| **total** | **2,341** | **17,354** |

Every full adder has two variables and fourteen clauses.  Both final carries
are retained; none of the counters or boundary sums is modular.

## 6. Guard validation and build regression

The Type-I option is rejected before formula construction unless all four
prerequisites are present.  In particular it cannot be enabled in branch zero
or without an anchored literal six-set.  Both Type-I and Type-II options are
excluded from the incompatible portal formulation.

The source and checker compile cleanly with `-Wall -Wextra -Wpedantic` against
the local CaDiCaL API stub.  With the required modules but Type I disabled:

```text
variables=4958941 clauses=16059861.
```

With Type I enabled:

```text
variables=4961282 clauses=16077215
rank_filtration_type1_variables=2341
rank_filtration_type1_clauses=17354
rank_filtration_type1_rank_cap_clauses=2784
rank_filtration_type1_component_definition_clauses=1389.
```

The exact delta is `2,341 / 17,354`.  The all-optional-guards-off build remains

```text
variables=4892622 clauses=15524818.
```

A fully integrated build with adjacent/rank-three shadows, containment caps,
endpoint alignment, singleton pool, local density, subcube deficiency, and
all branch-one prerequisites also succeeds:

```text
variables=3633096 clauses=19448397.
```

## 7. Scope

This is an exact, satisfiability-preserving encoding of the complete Type-I
array-rank onion.  It complements, rather than replaces, the existing
branch-one selected-witness profile circuit and optional `e1c2` minimal
component portfolio.  SAT still needs independent exhaustive interval-OR
verification.  UNSAT with a checked proof eliminates Type I; eliminating
`n=465` globally additionally requires the Type-II branch.
