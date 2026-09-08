# Independent implementation audit: Type-I ridge pin load

## Verdict

**PASS.**  The current `TypeIRidgePinLoadPlan` is a sound, exactly guarded
implementation of the independently audited boundary-ridge theorem.  It
adds exactly

```text
20,760 variables / 124,470 clauses
```

to the current full Type-I facet build.  Construction, emission,
diagnostics, variable declaration, and prerequisite validation are all
correct.  The absent and explicit-zero guards are byte-identical, and the
guard-off clause stream is identical to the frozen pre-ridge v7 source.

No production source was edited during this audit.

## 1. Guard and prerequisite chain

The environment parser treats

```text
K11_FOREST_TYPE1_RIDGE_PIN_LOAD
```

as enabled exactly when it is present, nonempty, and not the string `0`.
Before seed loading or formula allocation, the source rejects

```text
ridge enabled AND facet disabled
```

with status two and the exact diagnostic

```text
K11_FOREST_TYPE1_RIDGE_PIN_LOAD requires K11_FOREST_TYPE1_FACET_PIN_LOAD
```

The facet validation immediately preceding it requires exact Type I and the
subcube module.  Type I in turn requires local-density rank flags, both band
plans, and rank-six branch one.  Thus every pointer dereferenced by the
ridge constructor is guaranteed nonnull:

```text
local_density_pb_plan,
type1_facet_pin_load_plan,
type1_facet_pin_load_plan->facet_support.
```

The portal compatibility test includes both the facet and ridge guards, so
the ridge module cannot leak into a portal formula.  No named-cell,
residual-lex, prefix-chain, or rank-seven-width guard is needed for the
ridge theorem itself.

An independent negative run with the ridge guard alone returned status two
before constructing a `CaDiCaL::Solver` object.

## 2. Reuse of facet literals

`TypeIFacetPinLoadPlan` now retains

```cpp
array<vector<int>, 6> facet_support;
```

and appends one variable for each suffix position in increasing order:

```text
facet_support[b][position-1]
  <-> [position in C_4 and A[position] subseteq 63\{b}],
1<=position<465.
```

The ridge constructor indexes the retained row by exactly `position-1`, so
there is no zero/one-based shift.  Merely moving the already allocated
variables into retained vectors changes neither allocation nor clause
order; Section 7 verifies this against the frozen pre-ridge source.

## 3. Ridge enumeration and exact gate semantics

The nested loops are

```cpp
for (int first=0; first<6; ++first)
  for (int second=first+1; second<6; ++second)
```

and therefore enumerate each of the `C(6,2)=15` endpoint ridges exactly
once.

For every pair and every suffix position `1,...,464`, the implementation
defines one fresh variable by

```text
z <-> facet_support[first][position-1]
     AND !A[position,second]
     AND !rank4[position].
```

The emitted clauses are

```text
!z or in_facet
!z or !coordinate
!z or !rank4
 z or !in_facet or coordinate or rank4.
```

Exhaustion of all sixteen truth assignments confirms the exact
bidirectional equivalence.

Semantically, `in_facet` supplies membership in `C_4` and containment in
`63\{first}`.  The missing second coordinate reduces this to containment in
`63\{first,second}`.  Exact Type-I rank flags make `!rank4` exclude the only
nonproper contained value, namely the four-set ridge itself.  Hence `z` is
true exactly at strict ridge supports.  Using the first facet row rather
than the second is asymmetric only syntactically.

## 4. Counter and comparator

For each ridge the code passes exactly 464 `z` literals to the same exact
Wallace/ripple architecture used by the facet module.

Independent bucket simulation gives

```text
452 Wallace compressor full adders,
  8 ripple full adders,
460 full adders total.
```

Every full adder has two fresh variables.  Its eight parity clauses and six
majority clauses exhaustively define the sum and carry, and the ripple
retains the final carry.  Thus one counter represents the ordinary integer
sum from 0 through 464 without modular wraparound.

The resulting count has nine bits.  `add_geq_constant(count,10)` emits one
first-difference clause for each set bit of `10=000001010_2`, hence two
clauses.  Exhausting all 512 nine-bit inputs confirms exact equivalence to
unsigned `count>=10`.

## 5. Independent inventory

The gate row is

```text
15*464 = 6,960 variables,
6,960*4 = 27,840 clauses.
```

The counters are

```text
15*460*2  = 13,800 variables,
15*460*14 = 96,600 clauses.
```

The comparisons add thirty clauses and no variable.  Therefore

```text
variables = 6,960+13,800      = 20,760,
clauses   = 27,840+96,600+30 = 124,470.
```

The independent literal-stream delta supplies a second reconstruction.
One strict gate contributes ten nonzero literals and fourteen `solver.add`
calls; one full adder contributes fifty nonzero literals and sixty-four add
calls; one ridge comparison contributes fourteen nonzero literals and
sixteen add calls.  Hence the predicted module deltas are

```text
nonzero literals:
  6,960*10 + 6,900*50 + 15*14 = 414,810,

solver.add calls:
  6,960*14 + 6,900*64 + 15*16 = 539,280.
```

Both deltas match the independently observed complete streams exactly.

## 6. Construction, emission, and diagnostics

The facet plan is constructed before the ridge plan.  The ridge plan is
constructed conditionally, before `variable_total` is frozen, so all 20,760
fresh variables are declared.  Its clauses are emitted conditionally and
after the facet clauses; all referenced literals have already been defined.

The diagnostic header always reports the Boolean ridge guard.  The detailed
inventory is printed only when the ridge object exists, and includes total,
gate, counter, and comparator variables/clauses.  The enabled full build
reports

```text
variables=3,669,557
clauses=20,160,885
type1_ridge_pin_load_variables=20760
type1_ridge_pin_load_clauses=124470
type1_ridge_pin_load_gate_variables=6960
type1_ridge_pin_load_counter_variables=13800
type1_ridge_pin_load_gate_clauses=27840
type1_ridge_pin_load_counter_clauses=96600
type1_ridge_pin_load_comparator_clauses=30.
```

The independent solver double also verified

```text
DECLARED=3,669,557
MAXVAR=3,669,557,
```

so there is neither an undeclared reference nor an unused high-water error.

## 7. Independent rebuild and guard-off identity

The current source was compiled independently with Clang C++20 and the
read-only hashing CaDiCaL double.  The only warning was the pre-existing
unused `BITS` constant.  The enabled build reproduced

```text
INDEPENDENT_FNV64=3948591229824f06
ADD_CALLS=89023684
ZEROES=20160885
LITERALS=68862799
DECLARED=3669557
MAXVAR=3669557.
```

Absent and explicit-zero ridge guards produced byte-identical logs and
reproduced

```text
INDEPENDENT_FNV64=b33abee6ccc470f4
ADD_CALLS=88484404
ZEROES=20036415
LITERALS=68447989
DECLARED=3648797
MAXVAR=3648797.
```

For a stronger regression check, the frozen remote v7 source at SHA-256

```text
0d41fbd4cfe3ac075c850b0cfe41cea740608bfa953b53d7ffc40d2a1e3bd6d5
```

was independently compiled against the same hash double.  Its full Type-I
facet stream has the same FNV fingerprint, add-call count, clause count,
literal count, declaration, and maximum variable as the current ridge-off
build.  Therefore retaining `facet_support` and adding the guarded code did
not perturb the pre-ridge formula at all.

## 8. Source-aware checker

Both

```text
python3 scratch/check_k11_type1_boundary_ridge_pin_load.py
python3 scratch/check_k11_type1_ridge_pin_load_source.py
```

pass.  The source-aware checker confirms the principal production anchors,
constructor and emission sites, gate clauses, full-adder truth table,
counter inventory, comparator truth table, and claimed module inventory.

Its textual anchors alone do not prove loop bounds, exact clause-stream
identity, prerequisite transitivity, or diagnostic totals.  The independent
source inspection and full-stream builds above cover those gaps; this is a
checker scope observation, not a production defect.

## 9. Frozen artifacts and scope

The audited files have hashes

```text
bb42caaee3c5adfc511ed8171a80944889020a4b0a3869069baeb90141034cc3  k11_forest_sat.cpp
f0516ba8004b8b16b6d11520162bfb9711dd6c6e512b057c6168b721dc01877f  scratch/check_k11_type1_ridge_pin_load_source.py
2a5f23f1e310ecff7cf9c27596ef047787ab92240e24a2e02f899ea62cdc727c  scratch/rank7_independent_hash_stub/cadical.hpp
```

The ridge module is a satisfiability-preserving propagation reduction inside
Type I.  It proves neither SAT nor UNSAT.  A candidate still requires both
independent interval-OR verifiers, and any UNSAT claim still requires an
archived proof and independent checking.
