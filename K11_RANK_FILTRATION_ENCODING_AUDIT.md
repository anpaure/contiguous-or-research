# Audit of the `k=11` Type-II rank-filtration encoding

> **Superseded/retracted implementation verdict (2026-07-23).**  This audit
> incorrectly asserted that all three allowed rank-five chains have
> width-zero states only at `00` and `33`.  Chains B and C also contain `22`
> and `11`.  The audited A-only equation was therefore not
> satisfiability-complete.  The mathematical stability theorem survives;
> the corrected chainwise implementation and its independent audit are in
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR.md` and
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

> **Update.**  This audit covers the original foundational subcircuit.  The
> production guard has since gained an exact two-component pin/slack
> extension, independently audited in
> `K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING_AUDIT.md`.  The complete
> current plan is 9,814 variables / 47,310 clauses.

## Verdict

**PASS.**  The guarded production module

```text
K11_FOREST_RANK_FILTRATION_TYPE2=1
```

is sound and satisfiability-complete for the Type-II array-rank branch proved
in `RANK_FILTRATION_STABILITY_AUDIT.md`.  It encodes the stronger coupled
inequality

```text
duplicate_excess(rank five)+components(rank<=4) <= 2,
```

as well as the entry-rank cap and the 134-entry rank-five cap.  The module
adds exactly 2,374 variables and 17,557 clauses.  With the guard absent it
allocates no variable and emits no clause.

Audited files:

```text
3a51bcf5f181d0a31f5cceac1e94f19079355b02aad60516be9bc626c1b5dec8
  k11_forest_sat.cpp
c889d95a9644c209a058e3be84cfb70845b6f9cf52200f9c8f5b394170f96419
  scratch/verify_k11_rank_filtration_type2.cpp
```

## 1. Guard and prerequisites

The parser treats an absent or `0` value as disabled and every other nonempty
value as enabled, consistently with the surrounding Boolean guards.  The
enabled mode requires the exact rank one-hot and both rank-five/rank-six band
plans.  A missing prerequisite exits with status 2 before any formula is
built.  The incompatible literal-six-set branch is also rejected explicitly.

The option is included in the portal-branch exclusion test, so the portal
formula cannot accidentally inherit its variables or clauses.

Allocation occurs only after all three prerequisites have been constructed
and before `variable_total` is frozen.  Clause transfer occurs only when the
plan exists.  Diagnostic counts are read directly from the constructed plan.

## 2. Exact rank semantics

The reused `LocalDensityPBPlan::rank[p][t]` literals are defined by a complete
prefix-popcount mux bank.  They are exact, not one-way threshold flags.  The
2,790 added units therefore exclude precisely entry ranks 6 through 11.
The base formula independently forces every entry nonzero, leaving ranks
1 through 5 exactly.

The 465 flags `rank[p][5]` are summed by an exact Wallace compressor and exact
final ripple addition.  Its full width is retained, so the comparison to 134
cannot wrap modulo a smaller power of two.

## 3. Components

For `p>0`, the production truth table is

```text
start[p] <-> rank5[p-1] AND !rank5[p].
```

Together with `start[0]=!rank5[0]`, this counts exactly the starts of maximal
rank-at-most-four runs.  The independent checker exhausts all 1,024 binary
rank patterns of a ten-position analogue and matches the direct component
count in every case.

The 465 starts are passed through another exact Wallace/ripple circuit and
compared directly to two.  There is no boundary omission: a low component at
position zero is counted by the signed literal used as the first input.

## 4. Duplicate alignment and completeness

Every selected rank-five singleton is a literal rank-five array value, and
selected target values are distinct.  Hence for every witness assignment

```text
y0 <= number of distinct literal rank-five values.
```

For a Type-II array, reselect one singleton witness for each distinct literal
rank-five value.  Every nonliteral target keeps an arbitrary old witness.
Equal-rank incomparability still yields a valid monotone rank-five schedule,
and the universal band/cross-layer inequalities remain valid.  For this WLOG
choice,

```text
y0 = distinct literal count,
delta_5 = n5-y0.
```

All three allowed rank-five state chains have width-zero states only at their
first and last vertices.  The exact transition counts therefore give

```text
y0=h1+462-h6.
```

The encoded integer row

```text
n5+h6+s<=h1+464
```

is algebraically identical to `delta_5+s<=2`.  Thus it is sound.  Conversely,
the canonical witness choice satisfies it for every Type-II array, so it does
not discard a valid Type-II solution merely because the original central
witness assignment selected a non-singleton witness for a literal target.

The checker exhausts all multiplicity profiles in `{0,1,2,3}^4` and verifies
`delta=n5-distinct` and the coupled-row equivalence for component counts one
through four.

## 5. Arithmetic circuit audit

The checker reconstructs the inventory independently from gate sizes:

```text
two 465-input exact counts: 2*(461 full adders)
three coupled-row additions: 28 full adders
component-start variables: 464
final prefix-equality variables: 10.
```

With two variables and fourteen clauses per full adder, it obtains

```text
variables=2374 clauses=17557
rank_cap_clauses=2790
component_definition_clauses=1392.
```

This exactly matches production diagnostics.  The checker compiles with

```text
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  scratch/verify_k11_rank_filtration_type2.cpp \
  -o /tmp/verify_k11_rank_filtration_type2
```

and prints

```text
component_start_identity=PASS
duplicate_alignment_identity=PASS
type2_variables=2374 clauses=17557
rank_cap_clauses=2790 component_definition_clauses=1392
k11_beta_4_5_6=331,464,465 PASS
```

## 6. Production build regression

The production source compiles cleanly against the local CaDiCaL API stub
with `-Wall -Wextra -Wpedantic`.  Build-only inventories are:

| configuration | variables | clauses |
|---|---:|---:|
| every optional guard absent | 4,892,622 | 15,524,818 |
| the three prerequisites only | 4,958,700 | 15,843,371 |
| prerequisites plus Type II | 4,961,074 | 15,860,928 |

The last-minus-middle delta is exactly `2,374 / 17,557`.  The established
all-off baseline is unchanged.  Inspection also confirms that no existing
allocation or clause call was moved: the new plan has a conditional
constructor and conditional emission block.

With the existing canonical/oriented boundary modules and rank-six branch
zero added, the build succeeds with

```text
variables=4961074 clauses=16075759.
```

Thus the new array-rank architecture composes with the current exact
no-literal-six-set portfolio.

An integrated build with adjacent/rank-three shadows, both band modules,
endpoint alignment, canonical/singleton/boundary cuts, containment caps,
local density, the independent subcube-deficiency circuit, branch zero, and
Type II also succeeds:

```text
variables=3632888 clauses=19446941
rank_filtration_type2_variables=2374
rank_filtration_type2_clauses=17557.
```

## 7. Type-I assessment

The current canonical, oriented-boundary, and rank-six branch-one modules
already give the exact first Type-I statement `A[0]=63`, with no other
literal six-set.  Reusing them is correct and avoids hundreds of thousands
of duplicate mask-mismatch clauses.

However, the next rank-five peel is not yet present at array level.  In
particular, selected-witness mode `e1c2` does not by itself assert that all
literal rank-five values are distinct or that the actual rank-at-most-four
positions form one component.  Those should be a separate Type-I plan rather
than being claimed as consequences of the existing witness-forest mode.

## 8. Scope

This is a branch cut, not a proof result from a solver run.  SAT requires the
usual independent exhaustive interval-OR verification.  UNSAT plus a checked
proof trace eliminates Type II; it does not eliminate the separately encoded
Type-I branch.
