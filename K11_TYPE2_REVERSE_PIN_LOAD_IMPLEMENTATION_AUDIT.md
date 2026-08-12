# Production implementation audit for the Type-II reverse pin-load cut

## 1. Status

The audited theorem in `K11_TYPE2_REVERSE_PIN_LOAD.md` is now implemented in
`k11_forest_sat.cpp` behind

```text
K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1.
```

The guard requires

```text
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1,
```

which supplies the exact oriented slack-one/slack-two component memberships
and transitively supplies the repaired Type-II filtration, local-density, and
joint rank-five boundary circuits.  An invalid standalone invocation exits
with status 2 and the expected prerequisite diagnostic.

This is a formula implementation and build audit.  It is not a SAT result,
an UNSAT result, or a proof that `nu(11)>465`.

## 2. Zero-cost occurrence reuse

`TypeIITwoComponentPinPlan` already allocated the exact conjunctions

```text
slack_two_membership[p] AND A[p,b]
```

for all 465 positions and eleven coordinates.  The implementation retains
those existing literals in

```text
array<vector<int>,K> slack_two_occurrence;
```

without changing their allocation or clause order.  The reverse module uses
the retained 5,115 literals as its counter inputs and does not rebuild them.

The strongest repaired Type-II formula, with rank-seven width enabled, has
the following guard-off result:

```text
variables=3660446 clauses=20079690
CLAUSE_STREAM_FNV64=97fd4ee01d10aa7a
```

This exactly reproduces the independently frozen pre-module inventory and
clause-stream fingerprint.  The same output is obtained when the new guard is
absent and when it is explicitly zero.  Thus the retention refactor is
byte-for-byte dormant when the module is disabled.

## 3. Exact production circuit

For each coordinate `b`, the module defines the exact union flag for the
slack-one component and reuses the retained slack-two occurrences to count

```text
o_b = #{p in C2 : b in A[p]}.
```

When the exact two-component flag is true and the slack-one union omits `b`,
it enforces

```text
o_b >= 59.
```

The repaired A/B/C rank-five profiles all satisfy the invariant

```text
y0+y2 = 462+h1+h3+h5-h2-h4-h6.
```

Because `z=y0` in the exact two-component branch, the second reverse theorem
row is encoded in the chain-independent unsigned form

```text
h2+h4+h6 <= 3*o_b+h1+h3+h5+76.
```

All full adders retain their final carry.  The prefix-equality chains in the
coupled comparisons are bidirectional on the active branch, and every
comparison and equality-definition clause carries the same two escape
literals.  Therefore inactive comparison auxiliaries impose no accidental
restriction.

## 4. Frozen incremental inventory

Build-only generation reproduces the design exactly:

| component | variables | clauses |
|---|---:|---:|
| exact slack-one coordinate unions | 5,126 | 20,471 |
| eleven reused-input occurrence counters | 10,142 | 70,994 |
| shared and coordinate arithmetic | 677 | 4,629 |
| eleven conditional `o_b>=59` comparisons | 0 | 55 |
| **total** | **15,945** | **96,149** |

With the strongest repaired Type-II portfolio and rank-seven module enabled,
turning on the reverse guard changes the exact full inventory to

```text
variables=3676391 clauses=20175839
CLAUSE_STREAM_FNV64=fe81112af74df36a
```

The differences from the guard-off formula are exactly the frozen module
inventory above.

## 5. Checkers and build evidence

The production source is frozen at

```text
3500113db42662e783cb8a4e9d3e247372cad1488f346b8f90b9eb36b55d3e38
  k11_forest_sat.cpp
```

The mathematical, design, and source-aware checkers have hashes

```text
d66b3e8884d0d0140505ab95a86985e32e71de3379a900654146dd2edd406cc8
  scratch/check_k11_type2_reverse_pin_load.py
8166b1ba3f48677cdf9688154ff3dbdf36437ab82823c9f545c94edb9cd571b4
  scratch/check_k11_type2_reverse_pin_load_implementation.py
5fc28b5cc1d704444cafd6f2b222e9773b00bcda22272d1ec61e00174ba7ffa1
  scratch/check_k11_type2_reverse_pin_load_source.py
```

Together they verify the touched-cell theorem, the four-row envelope, the
chain-independent boundary identity, all gate/comparator truth tables, the
465-input Wallace profile, retained final carries, integration anchors, and
the exact preferred/fallback inventories.

The source compiles cleanly with

```text
g++ -std=c++20 -Wall -Wextra -Wpedantic
```

against the independent build-only CaDiCaL stub.  No remote solver process
was launched as part of this implementation audit.
