# Independent implementation audit: Type-I global pair profile

## Verdict

**PASS.**  The opt-in implementation behind

```text
K11_FOREST_TYPE1_GLOBAL_PAIR_PROFILE=1
```

in `k11_forest_sat.cpp` is an exact CNF encoding of

```text
n1 + 2*n2 >= 110,
```

where `ns` is the number of physical entries of literal rank `s`.  The
implementation reuses the exact shared rank flags, retains every arithmetic
carry, emits the advertised incremental inventory

```text
1,864 variables / 13,053 clauses,
```

has the correct Type-I dependency and portal incompatibility, and allocates
and emits nothing when its guard is absent or zero.

This audit freezes the production source at

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
  k11_forest_sat.cpp
```

It is an implementation audit of a necessary propagation row.  It is not a
SAT/UNSAT result and does not change the proved bound on `nu(11)`.

## 1. Mathematical row

In the exact Type-I architecture, the one literal rank-six entry and all
literal rank-five entries lie in the boundary blocks.  Every rank-one or
rank-two entry is therefore in the central rank-at-most-four core.

If the core has `q` nonliteral rank-five targets, it has length `q+2`.
Ordering one selected witness for each of those `q` incomparable targets
shows that every core interval of physical length three contains a selected
rank-five witness.  Hence every rank-two target has one of two forms:

* it occurs as a literal rank-two entry; or
* it is represented by an adjacent pair of its two singleton atoms.

Adjacent atom-pair witnesses for distinct targets cannot overlap.  Two
overlapping pairs would form three consecutive singleton entries, whose
three-cell union has rank at most three, contradicting the rank-five witness
contained in every three-cell core interval.

There are `C(11,2)=55` rank-two targets.  At most `n2` of them can be literal,
and at most `floor(n1/2)` can use disjoint atom pairs.  Therefore

```text
n2 + floor(n1/2) >= 55.
```

For integral `n1,n2`, this is exactly equivalent to

```text
n1 + 2*n2 >= 110.
```

The independent checker exhausts all `0<=n1,n2<=465` and confirms this
integer reformulation.  The theorem itself was previously audited in
`K11_TYPE1_FACE_HIERARCHY_NEXT_AUDIT.md`; the argument above was also checked
directly for this implementation audit.

## 2. Exact rank inputs

`TypeIGlobalPairProfilePlan::build()` takes precisely

```cpp
local.rank[position][1]
local.rank[position][2]
```

for each of the 465 positions.  There are no other rank references in the
module.

The shared `LocalDensityPBPlan` obtains its final `rank[position][s]` bank
from an exact prefix-popcount network.  The first input bit is encoded by the
signed pair `(!A[p][0],A[p][0])`; every subsequent count state is an exact
four-clause mux.  Consequently the final flags are an exact one-hot encoding
of the literal entry rank, not one-way indicators.

The module also reuses `local.one`, which is fixed true by a unit clause.  Its
signed negation is therefore a genuine constant-false input to the counter
and ripple circuits.

## 3. Counter and addition semantics

For each of the two 465-literal rows, `exact_count` first uses a Wallace-style
three-to-two compression and then adds the two surviving bit rows with an
unsigned ripple adder.

Independent bucket simulation gives

```text
453 compressor full adders,
  8 final-ripple full adders,
461 full adders per counter.
```

The result has nine bits, enough for every value from zero through 465.  Each
full adder has eight parity clauses and six majority clauses.  Exhausting all
32 assignments to its three inputs and two outputs confirms that these
fourteen clauses accept exactly

```text
sum   = a XOR b XOR carry,
carry = majority(a,b,carry).
```

Both `add_unsigned` implementations append the final carry.  No counter or
outer sum is taken modulo a power of two.

The code constructs `2*n2` in little-endian form as

```cpp
vector<int> doubled_n2{-one};
doubled_n2.insert(doubled_n2.end(), n2.begin(), n2.end());
```

and adds it to `n1`.  Since both counters are nine bits, the shifted operand
is ten bits and the outer retained-carry ripple uses ten full adders.  Its
eleven-bit result exactly represents `n1+2*n2`, whose maximum is 1395.

Finally, `add_geq_constant(profile,110)` uses the direct first-difference
encoding.  The set bits of

```text
110 = 00001101110_2
```

are `1,2,3,5,6`, so five clauses are emitted.  Exhaustion of all 2048
eleven-bit values confirms that their conjunction is true exactly for values
at least 110.

## 4. Independent inventory

The two counters contribute

```text
2 * 461 * 2  =  1,844 variables,
2 * 461 * 14 = 12,908 clauses.
```

The ten-stage outer ripple contributes

```text
10 * 2  =  20 variables,
10 * 14 = 140 clauses.
```

The comparison contributes five clauses and no variable.  Thus the exact
increment is

```text
1,844 + 20        =  1,864 variables,
12,908 + 140 + 5  = 13,053 clauses.
```

An independent literal-call calculation gives 59,691 extra calls to
`solver.add`, including one terminating zero per clause.  The full
build-only fingerprint reproduces this delta exactly.

## 5. Guard integration

The source audit confirms all of the following.

* The environment variable is parsed with the common absent/empty/`0`
  convention.
* Enabling it without `K11_FOREST_RANK_FILTRATION_TYPE1` returns status 2 and
  prints the exact dependency diagnostic.
* The Type-I filtration already requires the shared local-density plan, both
  band plans, the Type-I rank-six branch, and its boundary normalizations, so
  dereferencing `local_density_pb_plan` is safe.
* The module is included in the portal-mode incompatibility list.
* The plan is constructed before `variable_total` is frozen.
* Every stored clause is emitted through `add_vector`.
* The main diagnostic prints the guard bit and the variables, clauses,
  counter, arithmetic, and comparator subtotals.
* When the guard is absent or exactly `0`, the plan is not constructed, so it
  allocates no auxiliary variable and emits no clause.

## 6. Independent build-only evidence

The audit compiles the frozen source with

```text
g++ -O2 -std=c++20 -Wall -Wextra -Wpedantic
```

against the separate `scratch/cadical_hash_stub/cadical.hpp`.  That stub
records the exact complete `solver.add` stream but is deliberately not a SAT
solver.

With the minimal exact Type-I dependency stack, the guard-off build is

```text
variables=4961434 clauses=16078323
CLAUSE_STREAM_FNV64=af21dd24ae24b672 ADD_CALLS=59352346
```

Setting the guard explicitly to zero produces byte-for-byte identical stderr
and the identical clause-stream fingerprint.  This proves guard-off identity
for the audited build.

With the global pair profile enabled, the build is

```text
variables=4963298 clauses=16091376
CLAUSE_STREAM_FNV64=dca75e59b3e26372 ADD_CALLS=59412037
```

The exact differences are

```text
variables: 1,864
clauses:   13,053
add calls: 59,691.
```

The enabled diagnostic independently reports

```text
type1_global_pair_profile_variables=1864
type1_global_pair_profile_clauses=13053
type1_global_pair_profile_counter_variables=1844
type1_global_pair_profile_counter_clauses=12908
type1_global_pair_profile_arithmetic_variables=20
type1_global_pair_profile_arithmetic_clauses=140
type1_global_pair_profile_comparator_clauses=5
```

## 7. Reproducible checker

The independent checker is

```text
6c5ed30688da41b701771e39899a5b49e33b698c3dbc7cdae799f42192844aa0
  scratch/audit_k11_type1_global_pair_profile_source_independent.py
```

Run it from the project root with

```bash
python3 scratch/audit_k11_type1_global_pair_profile_source_independent.py
```

It checks the frozen source hash, source integration anchors, exact rank
references, full-adder truth table, Wallace profile, comparator truth table,
integer theorem reformulation, all component inventories, dependency error,
guard-off identity, full clause-stream fingerprints, and enabled diagnostic
subtotals.

## Final conclusion

The theorem-to-CNF mapping, exact rank flags, counter/addition/comparator
semantics, dependency and incompatibility guards, allocation, emission,
logging, `1,864/13,053` inventory, and guard-off identity all survive
independent audit.  No implementation defect was found.
