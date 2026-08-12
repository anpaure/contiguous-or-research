# Independent audit: `k=11` canonical-literal and singleton-pool implementation

## Verdict

**PASS.**  I independently audited `k11_forest_sat.cpp` at SHA-256

```text
8ba2b8203e8dbd699d4e45b87cccd828de5a6cb901d751652b4704f93551dccb
```

against `K11_FOREST_UPPER_LITERAL_MASK_CUT.md`,
`ODD_SHORT_POOL_SINGLETON_REFINEMENT.md`, and the implementation note.

The two guarded clause families are correct:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1 : 214,365 clauses, 0 variables
K11_FOREST_SINGLETON_POOL_CUT=1    :     463 clauses, 0 variables
combined                           : 214,828 clauses, 0 variables.
```

The first is a satisfiability-preserving coordinate-symmetry choice, not a
coordinate-labelled necessary condition.  The rest of the current hard CNF
is coordinate-equivariant.  The second is the exact conditional refinement

```text
x3 >= 93 + 2*x0.
```

The audit covers all 463 boundary clauses, including the 95 clauses with an
empty `g4` suffix.  Both guards off leave the prior hard formula unchanged.
No SAT, UNSAT, or `nu(11)=465` conclusion is asserted.

## 1. Frozen-source recovery and guard-off identity

I extracted the recorded source patch, reversed it, and reconstructed

```text
scratch/k11_forest_sat_before_literal_pool_reconstructed.cpp
SHA-256 31cb278b5e4e5741d7d9c0ee8eee48f902a177536d44861b1aa408b8626707d7
```

which exactly matches the frozen pre-edit SHA in the implementation note.
The direct source diff contains only:

1. two environment booleans;
2. the singleton-pool dependency check;
3. two diagnostic counters;
4. the two guarded clause-generation blocks;
5. diagnostic output.

There is no new variable allocation.  When both guards are false, neither
new block calls `add_vector`; all pre-existing allocations and clauses occur
in the same order as in the frozen source.  Thus the hard-clause stream is
source-level identical, not merely equal in aggregate size.

Both old and new snapshots were independently compiled at
`-O3 -std=c++20 -Wall -Wextra -Wpedantic` against the build-only CaDiCaL test
double; both compiled without a warning.  Three guard-off profiles reproduce
identical inventories:

| profile | old variables/clauses | new variables/clauses |
|---|---:|---:|
| no optional structural cuts | `4,892,622 / 15,524,818` | `4,892,622 / 15,524,818` |
| band + joint-band | `4,899,664 / 15,563,145` | `4,899,664 / 15,563,145` |
| adjacent + band + joint + rank-three + endpoint alignment | `2,924,697 / 14,517,086` | `2,924,697 / 14,517,086` |

The new source only adds diagnostic zeros in these runs.

## 2. Array-level premise for the canonical gate

The audited odd cross-layer theorem gives `x0<=1` for every independently
chosen rank-five/rank-six witness family.  If two distinct rank-six masks
occurred as literal entries, one could deliberately select those two
singletons as their witnesses, contradicting `x0<=1`.  Therefore every
genuine length-465 solution has either:

```text
no literal rank-six entries, or
one distinct literal rank-six mask, possibly repeated.
```

This quantifier is essential.  It turns a selected-schedule theorem into an
array-level statement before any coordinate symmetry is used.

The group `S_11` acts transitively on the 462 six-subsets.  If the sole mask
is `S`, map its six coordinates bijectively to `0,...,5` and its other five
coordinates to `6,...,10`.  The resulting coordinate permutation sends `S`
to

```text
63 = {0,1,2,3,4,5}.
```

All its repetitions are sent to 63.  If no rank-six literal occurs, the
identity permutation already satisfies the canonical restriction.  Hence
the gate preserves existence in both branches.

## 3. Coordinate-equivariance audit of every other hard block

For a coordinate permutation `pi`, use the following variable renaming:

```text
A[p,b]                         -> A[p,pi(b)]
target block for mask S        -> target block for pi(S)
central q-column for mask S    -> central q-column for pi(S)
value/occurrence bit b         -> value/occurrence bit pi(b)
schedule states and positions  -> unchanged.
```

Numeric mask ordering need not be preserved; this is an arbitrary CNF
variable permutation.  Inspection of every hard-clause family gives:

| hard block | reason it is equivariant |
|---|---|
| nonzero array entries | each clause contains all eleven coordinate bits uniformly |
| direct targets | target families are complete by rank; bounds depend only on rank; positive/absent bits map with the target |
| rank-five and rank-six schedules | both full layers are enumerated; state geometry is coordinate-free; OR/value bits map uniformly |
| exact rank cardinality | all coordinate subsets of each required size are enumerated |
| target occurrence columns | complete rank layers are permuted among columns |
| monotone-band constraints | use only endpoint offsets and state indices |
| `BandCutPlan` | uses only state counts and widths |
| `JointBandCutPlan` | uses only both state-count profiles and width-zero presence |
| adjacent rank-four/rank-seven compression | complete target layers, physical intervals, endpoint containment, and bitwise values all map uniformly |
| rank-three compression | the complete rank-three layer and all bit clauses map uniformly |
| endpoint-alignment plan | depends only on positions, endpoint colours, and widths |
| rank-five/rank-six forest | applies the same containment clauses to every coordinate |
| singleton-pool family | refers only to schedule boundaries and `e` |

The input array is used solely to set `solver.phase(...)`; `best_interval`
and `central_phase` affect phases only.  The solver seed is also heuristic.
There is no other hard clause naming a distinguished coordinate or fixed
mask.  Therefore the canonical rank-six gate is compatible with every
currently available guard, including the singleton-pool cut.

This conclusion must be re-audited if a future hard symmetry break fixes
another coordinate-labelled mask: the stabilizer of that mask need not act
transitively on rank-six sets.

## 4. Canonical mismatch clauses

The source constructs `central[1].masks` as the complete rank-six layer and
checks that it has 462 members before any clauses are emitted.  For every
position `p=0,...,464` and each such mask `S` except 63, it adds eleven
literals:

```text
-A[p,b]  when b is in S,
 A[p,b]  when b is not in S.
```

For `A[p]=S`, all eleven literals are false.  If `A[p]` differs from `S`, a
differing coordinate makes its corresponding literal true.  Thus each clause
is exactly `A[p]!=S`, with the required polarity.

The independent checker evaluates each of the 461 clauses on all `2^11`
possible entry values.  Their conjunction accepts exactly

```text
popcount(A[p]) != 6  OR  A[p] == 63.
```

Consequently:

* entries of every non-six rank are admitted;
* 63 is admitted and is not forced;
* an array with no rank-six entry remains admitted;
* every other rank-six value is rejected.

The exact inventory is

```text
465 positions * (462-1) masks = 214,365 clauses
214,365 * 11                    = 2,358,015 literal occurrences
new variables                  = 0.
```

No `A[p]=63 -> e` schedule-anchoring implication is present.

## 5. Singleton-pool dependencies and `e`

The singleton-pool option is rejected unless both `band_cuts` and
`joint_band_cuts` are true.  With neither or with only band enabled, it exits
with status 2 and prints

```text
K11_FOREST_SINGLETON_POOL_CUT requires both K11_FOREST_BAND_CUTS and K11_FOREST_JOINT_BAND_CUTS
```

If joint-band is requested without band, the earlier joint-band dependency
check exits with status 2, so no null plan can be dereferenced.  With both
dependencies satisfied, `band_cut_plan` and `joint_band_cut_plan` are
allocated before their public fields are read.

In the allowed rank-six chain

```text
00,01,02,03,13,23,33
```

the widths are

```text
0,1,2,3,2,1,0.
```

`JointBandCutPlan` defines `e` bidirectionally as the OR of every selected
`00` or `33` state.  Its always-active comparison is

```text
g1 + 461 <= g6.
```

Here `g1=#00` and `g6=462-#33`, so the comparison is exactly

```text
#00 + #33 <= 1.
```

Therefore `e` is false exactly when `x0=0` and true exactly when `x0=1`; it
is not merely a one-way indicator.  Requiring joint-band is what makes this
one-bit use of `e` exact.

## 6. Boundary meaning and all 463 suffix clauses

`BandCutPlan::boundary[j]` has indices `0,...,462`.  Under its exact monotone
chain schedule, the unique true boundary is the number of slots lying in the
first `j+1` chain states.  Hence

```text
g3 = boundary[2] = #(00,01,02)
g4 = boundary[3] = #(00,01,02,03)
g4-g3             = #03 = x3.
```

The implementation uses precisely these two arrays.  For every
`t=0,...,462`, it emits

```text
-e OR -g3[t] OR g4[t+95] OR ... OR g4[462].
```

There are exactly 463 clauses.  Boundary details are:

```text
t=0:   suffix g4[95],...,g4[462]
t=367: suffix g4[462]
t=368: empty suffix
...
t=462: empty suffix.
```

Thus exactly 95 clauses have no `g4` literal and reduce to
`-e OR -g3[t]`.  Every generated subscript lies in `0,...,462`; the loop with
start greater than 462 simply emits no suffix.

Because `g3` and `g4` are exact-one boundaries, all clauses except the one at
the selected `g3=t` are satisfied by `-g3[u]`.  The remaining clause is true
when `e=1` exactly if the selected `g4` boundary is at least `t+95`.
Therefore the full family is equivalent to

```text
e -> g4-g3>=95
e -> x3>=95.
```

The pre-existing band comparison is `x3>=93`.  Since exact `e` is in
`{0,1}`, their conjunction accepts precisely

```text
x3>=93                    when e=0,
x3>=95                    when e=1,
```

which is exactly `x3>=93+2*x0`.

The independent checker exhausts all

```text
2 * 463 * 463
```

exact-one triples `(e,g3,g4)` at the real boundary size and checks every one
of the 463 clause templates.

## 7. Inventories and integration

Deterministic build-only generation gives:

| enabled new guards | variables | clauses | delta from matching old profile |
|---|---:|---:|---:|
| canonical only | 4,892,622 | 15,739,183 | `0 / +214,365` |
| singleton pool with band+joint | 4,899,664 | 15,563,608 | `0 / +463` |
| both with band+joint | 4,899,664 | 15,777,973 | `0 / +214,828` |
| every structural guard and both new guards | 2,924,697 | 14,731,914 | `0 / +214,828` |

The fully guarded old inventory is `2,924,697 / 14,517,086`, so the final
difference is exactly `214,828` clauses and no variables.  The diagnostics
report the independently counted values at the actual clause-addition sites.

## 8. Independent checker

The new independent checker is

```text
scratch/audit_k11_literal_pool_impl_independent.cpp
SHA-256 c0ad6d82419d5bc27cc83649fa64f714c9bc805ee5fdadcfade44ecf8210dbdb
```

It does not include or invoke the production solver.  It independently:

1. enumerates the complete rank-six layer;
2. checks every forbidden mismatch clause on every eleven-bit entry;
3. checks the conjunction, including the no-rank-six case;
4. constructs a coordinate permutation from every rank-six mask to 63;
5. reconstructs and inspects all 463 suffixes and boundary indices;
6. exhausts the real exact-one boundary domain;
7. checks the `e=x0` algebra and `x3=g4-g3` state widths;
8. derives both individual and combined inventories.

Compiled with `-O3 -std=c++20 -Wall -Wextra -Wpedantic`, it reports:

```text
canonical_forbidden_masks=461 clauses=214365 literals=2358015
pool_boundaries=463 empty_suffixes=95 suffix_literals=67896
pool_clauses=463 combined_clauses=214828 added_variables=0
independent_literal_pool_implementation_audit=PASS
```

## 9. Scope

The build-only CaDiCaL test double was used only to execute deterministic
clause generation and compare inventories.  It was not used as a SAT solver.
The source passed warning-clean compilation, but this audit did not launch a
search.  A future SAT candidate still requires both independent OR verifiers;
a future UNSAT claim still requires an archived proof-producing CNF/proof
pair and independent proof checking.
