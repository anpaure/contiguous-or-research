# Independent implementation audit of `K11_FOREST_RANK3_SHADOWS`

## Verdict

The guarded rank-three implementation in the frozen source

```text
k11_forest_sat.cpp
SHA-256 6b0b5621aaed7b525c5a5e4eb082bc643ac72f0a6625caf461a6a3ff6f600663
```

faithfully implements the theorem audited in
`K11_FOREST_RANK3_SHADOW_REDUCTION_AUDIT.md`.  The guard is sound and
complete relative to the already-audited adjacent-shadow forest formula.
With adjacent shadows and band cuts enabled, the independently reproduced
formula inventory is exactly

```text
variables = 2,885,308
clauses   = 14,360,485
direct targets = 298.
```

The implementation neither assumes a fixed derivative row nor changes the
meaning of the existing central schedules.  With the new guard off, the
generated variable and clause sets follow the prior source path unchanged.
The diagnostic line has gained a `rank3_shadows=0` field and prints three
exception-slot counts instead of two; therefore stderr is not byte-identical,
but the SAT formula is.

This audit proves an encoding equivalence, not a SAT or UNSAT result.

## 1. Frozen comparison basis

I compared the new source directly with the previously audited source:

```text
previous source SHA-256
0a3db930fc343589fd9840b042a896c2b428459de6c3e3203ed45d676d10b9bc

new source SHA-256
6b0b5621aaed7b525c5a5e4eb082bc643ac72f0a6625caf461a6a3ff6f600663
```

The complete source diff contains only these semantic additions:

1. two optional fields in the existing short-interval record;
2. reading and validating `K11_FOREST_RANK3_SHADOWS`;
3. omitting direct rank-three targets when the guard is active;
4. guarded rank-three mask, exception-slot, gate, and target-flag allocation;
5. guarded generic-slot, at-most-three, short-target, and coverage clauses;
6. additional diagnostics.

No pre-existing clause body, central schedule, direct-target encoding,
rank-four/rank-seven shadow clause, band circuit, proof hook, DIMACS hook, or
SAT-output path was edited.

## 2. Guard dependency and control flow

The option is true exactly under the same convention as the other forest
guards: its environment value must be nonempty and different from the literal
string `"0"`.  Immediately afterward the source checks

```text
rank_three_shadows && !adjacent_shadows
```

and exits with status 2 and the message

```text
K11_FOREST_RANK3_SHADOWS requires K11_FOREST_ADJACENT_SHADOWS
```

before reading the seed or allocating SAT variables.  I executed this path
with band cuts both off and on; both executions returned 2.  This dependency
is necessary because the rank-three reduction reuses the 929 exact short OR
values allocated by the adjacent-shadow guard.

When the guard is false:

* the direct-target loop does not skip rank three;
* `rank_three_masks` and `exception_three` remain empty;
* no rank-three exception slot, `at_most_three`, or `q_three` variable is
  allocated;
* no rank-three generic, gate, flag, or coverage clause is emitted;
* the added structure fields remain unused and consume no SAT variable; and
* band-cut allocation starts at exactly the same value of `next` as before.

The final diagnostic formatting is the only unguarded observable difference.

## 3. Direct-target removal

In the adjacent-shadow formula without rank-three compression, the retained
direct ranks are

```text
1,2,3,8,9,10,11,
```

containing 463 targets.  The new condition

```text
if (rank_three_shadows && rank == 3) continue;
```

removes exactly the `C(11,3)=165` rank-three targets and no others, leaving

```text
463-165 = 298
```

direct targets.  The observed guard-on build reports 298.

Each removed target owns six arrays of length 465—three endpoint/inside arrays
and three present-bit occurrence arrays—so direct removal subtracts exactly

```text
165*2,790 = 460,350 variables
165*9,301 = 1,534,665 clauses.
```

These are the same source loops audited independently in the theorem report;
the implementation deletes the whole target record before either allocation
or clause generation, so no orphan direct variable remains.

## 4. Variable-allocation audit

Rank-three masks are populated only inside the adjacent-shadow allocation
block and only when the new guard is active.  The source verifies their count
is 165.

### 4.1 Six exact generic slots

The existing `allocate_exception_slots` helper is called once with

```text
rank = 3,
masks = rank_three_masks,
slots = exception_three.
```

It allocates six slots.  Per slot it allocates

```text
3*465 threshold/inside variables
11 exact value bits
11*465 bit-occurrence variables
165 target flags
```

for `6,686` variables.  The six slots therefore add `40,116` variables.

### 4.2 Shared short strip

The adjacent-shadow loop still creates exactly 929 records, one for every
singleton and adjacent-pair interval.  It continues to allocate each record's
eleven exact physical-OR bits and 330 rank-four flags exactly once.  Under the
new guard only, it additionally allocates

```text
one at_most_three gate
165 q_three target flags
```

per record.  Hence the added short-strip variables are

```text
929*(1+165) = 154,214.
```

All allocations use the monotonically increasing `next`; there is no alias
with existing rank-four variables or with the band plan, which is constructed
only afterward from the updated `next`.

The replacement therefore adds `194,330` variables after removing `460,350`,
for the exact net change

```text
-266,020 variables.
```

## 5. Generic-slot clause audit

The implementation invokes the already-audited `encode_exception_slots`
helper on the six new slots.  For rank three, each slot receives:

1. an exact nonempty contiguous interval of safe length at most three;
2. eleven value bits equivalent to the physical interval OR;
3. exact-cardinality-three clauses, namely `C(11,4)` at-most and `C(11,9)`
   at-least clauses;
4. for every target flag, implications to the target's three bits; and
5. one positive clause over all 165 target flags.

Exact cardinality makes two flags for distinct three-sets incompatible, so
the positive clause is exact-one without quadratic pairwise clauses.  A true
flag fixes the exact value to its target.  Thus every generic slot is an
ordinary sound physical witness.

The helper contributes exactly `19,025` clauses per slot and `114,150` over
all six slots.  No rank-four or rank-seven helper behavior changes.

## 6. Short-strip clause audit

The pre-existing short-interval clauses make each `item.value[bit]`
bidirectionally equivalent to the OR of that bit over the interval.  The new
code reuses those exact values rather than rematerializing them.

### 6.1 At-most-three gate

For each of the 929 records, the guarded loop enumerates every four-subset of
the eleven bits and adds

```text
not at_most_three OR not bit_1 OR ... OR not bit_4.
```

When the gate is true these `C(11,4)=330` clauses are exactly
`popcount(value)<=3`.  They add

```text
929*330 = 306,570 clauses.
```

The gate need not be defined in the reverse direction: it is an existential
auxiliary used only under a target flag.  Completeness sets it true for the
chosen rank-three interval.

### 6.2 Target flags

For every short interval and every one of the 165 targets, the code emits
exactly six clauses:

1. `q_three -> at_most_three`;
2. three implications to the target's physical OR bits;
3. one disjunction of selected rank-five states giving a proper same-left
   extension; and
4. one disjunction giving a proper same-right extension.

The first four implications force the physical OR to contain the three-set
target and have size at most three, hence to equal the target.  The two
endpoint disjunctions are built from the existing exact rank-five central
states using the literal tests

```text
central_left == short_left  && central_right > short_right,
central_right == short_right && central_left < short_left.
```

They therefore express strict physical containment exactly.  An empty
extension list becomes a unit `not q_three` clause, as it should at an
impossible boundary.  There are

```text
929*165 = 153,285 flags
153,285*6 = 919,710 clauses.
```

### 6.3 Coverage

For each target column, `cover_three[column]` receives all 929 short flags and
the matching flag from each of the six generic slots.  Exactly one positive
coverage clause is then emitted.  This adds 165 clauses and ensures that no
rank-three direct target was removed without replacement.

The endpoint theorem guarantees that at least 159 targets can use crossed
short intervals and at most six require generic slots.  Conversely, exact
generic slots can cover at most six distinct targets.  Hence the implemented
coverage is complete without inventing solutions.

The entire replacement adds

```text
114,150 + 306,570 + 919,710 + 165 = 1,340,595 clauses,
```

so the net clause change is

```text
1,340,595-1,534,665 = -194,070.
```

## 7. Exact output inventories

I independently executed the new binary in all four guard-off combinations
and reproduced the prior frozen inventories:

| adjacent shadows | band cuts | rank-three shadows | variables | clauses | direct targets |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 4,892,622 | 15,524,818 | 1,123 |
| 0 | 1 | 0 | 4,895,648 | 15,533,179 | 1,123 |
| 1 | 0 | 0 | 3,148,302 | 14,546,194 | 463 |
| 1 | 1 | 0 | 3,151,328 | 14,554,555 | 463 |

This runtime evidence agrees with the direct old/new source diff: guard-off
formula generation is preserved.

With the guard enabled, adjacent shadows are mandatory.  The two legal
inventories are

| adjacent shadows | band cuts | rank-three shadows | variables | clauses | direct targets |
|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 2,882,282 | 14,352,124 | 298 |
| 1 | 1 | 1 | 2,885,308 | 14,360,485 | 298 |

The difference between these rows is exactly the independently audited band
circuit: 3,026 variables and 8,361 clauses.  The combined real build also
reported

```text
rank3_shadows=1
shadow4_candidates=929
exception_slots=6,6,6
band_cut_variables=3026
band_cut_clauses=8361
BUILD_ONLY
```

Every execution returned normally.  These counts corroborate the source
audit; they are not used as its logical proof.

## 8. Independent source-oriented checker

I added

```text
scratch/verify_k11_forest_rank3_implementation.cpp
SHA-256 ac1a10ef9f88ecd5cfb5f2dc1d02e289096b9693e644fefc724155e805099703
```

It checks twelve guard/allocation/clause anchors in the frozen source,
exhausts all `2048*165=337,920` local truth-table cases for both short flags
and generic flags, enumerates all 929 physical short intervals and their
central extension literals, and recomputes the full inventory.  Compiled with
`g++ -O3 -std=c++20`, it reports

```text
source_anchors=12 short_truth_cases=337920 generic_truth_cases=337920
short_intervals=929 left_extension_literals=4158 right_extension_literals=4158
removed=460350,1534665 added=194330,1340595
variables=2885308 clauses=14360485 PASS
```

This checker is deliberately supplementary.  Text anchors can detect a
missing or duplicated source family but cannot prove control-flow dominance;
the latter was established by the direct source diff and manual clause audit
above.

## 9. Guard-off and certificate scope

With `K11_FOREST_RANK3_SHADOWS` absent, empty, or exactly `0`, the SAT formula
is the prior audited forest formula for the chosen adjacent/band settings.
The new diagnostic text is not proof-relevant.

With the guard active, the formula remains satisfiable if and only if a
universal nonzero 11-bit array of length 465 exists, because the theorem gives
completeness and every replacement witness is a sound physical interval OR.

This result does not settle that satisfiability question.  A future SAT model
must still decode to 465 masks and pass both independent interval-OR
verifiers.  A future UNSAT theorem still requires an archived exact CNF,
proof trace, hashes, and independent DRAT/LRAT verification.
