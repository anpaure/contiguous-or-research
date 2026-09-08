# Implementation of the k=11 canonical-literal and singleton-pool cuts

## 1. Verdict

**PASS.**  Two isolated zero-variable guards were added to
`k11_forest_sat.cpp`, starting from the frozen source

```text
31cb278b5e4e5741d7d9c0ee8eee48f902a177536d44861b1aa408b8626707d7
```

and producing

```text
8ba2b8203e8dbd699d4e45b87cccd828de5a6cb901d751652b4704f93551dccb.
```

The guards are:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_SINGLETON_POOL_CUT=1
```

The first adds exactly 214,365 clauses and zero variables.  The second adds
exactly 463 clauses and zero variables, and validates that both the existing
band and joint-band plans are enabled.  With both guards off, the formula's
variable and clause inventories are byte-for-byte numerically unchanged from
the frozen pre-edit builds.

No SAT or UNSAT claim is made by this implementation audit.  All builds below
used the clause-counting no-op CaDiCaL test double and `BUILD_ONLY`.

The frozen source was additionally compiled, but not executed, against the
real CaDiCaL library on the remote Linux host.  That production-header build
used the host compiler's spelling `-std=c++2a` and produced executable
SHA-256

```text
60f676f17f0835e43305f0a41fff41b42cc1656b6483052695738793c1a5edd5.
```

## 2. Canonical rank-six literal gate

The audited odd-width theorem proves that a length-465 solution contains at
most one distinct literal rank-six mask.  Coordinate permutations act
transitively on the 462 six-sets, so the possible mask may WLOG be fixed to

```text
C=63={0,1,2,3,4,5}.
```

For every physical position `p` and every rank-six mask `S!=63`, the guarded
implementation adds

```text
(OR_(b in S)     -A[p,b])
 OR (OR_(b not in S)  A[p,b]).
```

This 11-literal clause is false exactly when `A[p]=S`.  It does not force
`A[p]=63`, does not force any rank-six entry to occur, and is automatically
true for every entry whose rank is not six.

The implementation iterates over `central[1].masks`, which was independently
constructed as the complete rank-six layer before clauses are emitted.  It
skips only decimal mask 63.  Hence its exact inventory is

```text
465*(462-1)=214365 clauses,
0 variables,
214365*11=2358015 literal occurrences.
```

The gate has no dependency on the optional selected-witness encodings.  It is
a symmetry-WLOG existence cut, rather than a necessary restriction on every
fixed coordinate labelling.  The current hard formula is coordinate
equivariant; the seed affects phases only.

## 3. Singleton-pool gate

The proved short-pool theorem gives for k=11

```text
x3>=93+2*x0.
```

`BandCutPlan` already enforces `x3>=93`.  `JointBandCutPlan` strengthens
`x0<=1` and defines its public variable `e` exactly as the Boolean value
`x0`.  In the rank-six chain

```text
00,01,02,03,13,23,33,
```

the exact one-hot boundary

```text
g3=boundary[2]
```

counts the slots through state `02`, while

```text
g4=boundary[3]
```

counts the slots through state `03`.  Therefore

```text
x3=g4-g3.
```

For every `t=0,...,462`, the new guard emits

```text
-e OR -g3[t] OR g4[t+95] OR ... OR g4[462].
```

An empty suffix is allowed near the upper boundary.  Since both boundary
arrays are exact one-hot, these 463 clauses are equivalent to

```text
e -> g4-g3>=95.
```

Together with the old unconditional `x3>=93`, this is exactly
`x3>=93+2*x0`.  The inventory is

```text
463 clauses,
0 variables.
```

The guard is rejected unless both

```text
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
```

are set.  An invalid invocation exits with status 2 and the exact diagnostic

```text
K11_FOREST_SINGLETON_POOL_CUT requires both K11_FOREST_BAND_CUTS and K11_FOREST_JOINT_BAND_CUTS
```

## 4. Diagnostics

The build summary now prints

```text
canonical_rank6_entry=<0|1>
singleton_pool_cut=<0|1>
canonical_rank6_entry_clauses=<count>
singleton_pool_clauses=<count>
```

These counters are incremented at the actual `add_vector` sites.  The two
cuts allocate nothing before `variable_total` is frozen, so the variable
inventory cannot change.

## 5. Guard-off identity and exact inventories

Using the same seed and the no-op CaDiCaL header, the all-guard-off source
before the edit reported

```text
variables=4892622 clauses=15524818.
```

The post-edit source with both new guards off reports exactly

```text
variables=4892622 clauses=15524818
canonical_rank6_entry=0 singleton_pool_cut=0
canonical_rank6_entry_clauses=0 singleton_pool_clauses=0.
```

With only the canonical gate enabled:

```text
variables=4892622 clauses=15739183
delta variables=0 clauses=214365.
```

The band+joint baseline before the edit was

```text
variables=4899664 clauses=15563145.
```

With the singleton-pool gate added:

```text
variables=4899664 clauses=15563608
delta variables=0 clauses=463.
```

With band+joint and both new gates:

```text
variables=4899664 clauses=15777973
combined delta variables=0 clauses=214828.
```

Finally, with every existing optional structural guard plus both new cuts:

```text
variables=2924697 clauses=14731914
canonical_rank6_entry_clauses=214365
singleton_pool_clauses=463.
```

The corresponding pre-edit fully guarded inventory was

```text
variables=2924697 clauses=14517086,
```

again giving the exact combined delta 214,828.

## 6. Independent checker

The independent checker

```text
scratch/verify_k11_literal_pool_implementation.cpp
SHA-256 845b76a0ee7311d20f7be44a4515003e89c81f63003c5de43197df33e08ce3e1
```

does not include or call the production solver.  It performs four checks.

1. Exhausts every exact-one pair `(g3,g4)` and both values of `e` in a small
   analogue, verifying that the suffix clauses are equivalent to
   `e -> g4-g3>=threshold`.
2. Constructs and inspects all 463 real k=11 pool clauses, including every
   suffix literal and every empty boundary suffix.
3. Independently enumerates all 462 rank-six masks, checks that exactly 461
   are forbidden at every one of 465 positions, and verifies the mismatch
   polarity and the exact 2,358,015 literal count.
4. Explicitly constructs a coordinate permutation taking each of the 462
   rank-six masks to decimal 63.

It compiles cleanly with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic \
    scratch/verify_k11_literal_pool_implementation.cpp \
    -o verify_k11_literal_pool_implementation
```

and prints

```text
small_pool_truth_table=PASS
k11_pool_clauses=463 variables=0 threshold=95
k11_canonical_clauses=214365 variables=0 literals=2358015
k11_rank6_transitivity=PASS
```

## 7. Explicit non-implementation

The additional schedule-anchoring implication

```text
A[p]=63 -> e
```

has been mathematically justified in
`K11_FOREST_UPPER_LITERAL_MASK_CUT.md`, but was deliberately not added here,
as requested.  Neither new guarded family contains this implication.
