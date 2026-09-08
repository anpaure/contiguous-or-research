# Implementation of the cheapest coordinate-omission occurrence cuts

## Status

The audited occurrence-only projection is implemented in a new opt-in source:

```text
scratch/k11_core_incidence/k11_forest_sat_omissioncuts.cpp
SHA-256 f851f651e7d61e7126e25d097ab7bdb9e8f5b7a253c012a3fb26f03be197c350
```

The cloned source is enabled by

```text
K11_FOREST_COORDINATE_OMISSION_OCCURRENCE=1.
```

It requires exactly one of the corrected Type-I or Type-II rank-filtration
branches.  Frozen sources were not edited.  No compilation, CNF generation,
or SAT solving was performed on the user's workstation.

## 1. Encoded theorem

For coordinate `b`, let

```text
Z_b = #{low physical positions whose literal entry omits b}.
```

The new module imposes

```text
Type I:                         Z_b >= 193,
Type II duplicate/two-core:    Z_b >= 193,
Type II no-duplicate one-core: Z_b >= 130.          (1.1)
```

These are the cheapest projections of the stronger exact occurrence/run
rows

```text
2 Z_b-R_b >= 385,
3 Z_b-3 R_b+I_b >= 385,
Z_1b+2 Z_2b-R_2b >= 385.                            (1.2)
```

The present source intentionally does not materialize run or component-local
counters.  It implements only (1.1), as requested.

The Type-II guard is exact:

```text
tight <-> duplicate OR two_components.              (1.3)
```

The corrected filtration alternatives are precisely

```text
(duplicate,two_components)=(0,0),(1,0),(0,1),
```

so `tight` selects exactly the two physical-length-two modes.

## 2. Exact physical flags

`LocalDensityPBPlan` supplies exact entry ranks.  In Type II every position
has rank at most five, so

```text
low[p] <-> !rank[p][5].
```

In Type I, position zero is the canonical rank-six endpoint and every suffix
position has rank at most five.  The module therefore uses positions
`1,...,464` and the same signed low literal.

For every retained position and coordinate, it defines bidirectionally

```text
omit_low[p,b] <-> !rank[p][5] AND !A[p,b].          (2.1)
```

The three clauses are

```text
omit_low -> !rank5,
omit_low -> !A[p,b],
!rank5 AND !A[p,b] -> omit_low.
```

Thus every counted literal is exact; a high position or a position containing
`b` cannot be counted.

## 3. Exact counters and thresholds

The existing Wallace-plus-final-ripple pattern is copied verbatim.  It uses

```text
460 full adders to count 464 Type-I inputs,
461 full adders to count 465 Type-II inputs.
```

Every full adder has two variables and fourteen clauses.  The final carry is
retained, so each output is the ordinary nine-bit integer count.

The fixed comparisons use the source's exact first-difference clauses.  A
threshold `c<=x` needs one clause for every set bit of `c` and no auxiliary
variable.  Hence

```text
popcount(193)=3,
popcount(130)=2.                                    (3.1)
```

The Type-I threshold is unguarded.  In Type II, `193<=Z_b` is guarded by
`tight`, while `130<=Z_b` is guarded by `!tight`.  Signed guards are negated
when inserted as escape literals, so the latter comparison is active exactly
when `tight` is false.

## 4. Exact module inventory

The plan-local increments are:

| category | Type I variables | Type I clauses | Type II variables | Type II clauses |
|---|---:|---:|---:|---:|
| omission gates | 5,104 | 15,312 | 5,115 | 15,345 |
| exact counters | 10,120 | 70,840 | 10,142 | 70,994 |
| exact `tight` gate | 0 | 0 | 1 | 3 |
| constant thresholds | 0 | 33 | 0 | 55 |
| **module total** | **15,224** | **86,185** | **15,258** | **86,397** |

The current full rank-vector formulas already expose the Type-II duplicate
flag through their core-incidence prerequisite.  Relative to those audited
formulas, the predicted complete inventories are therefore

```text
Type I:  3,757,755 variables / 20,738,107 clauses,
Type II: 3,777,488 variables / 20,840,854 clauses.  (4.1)
```

If the occurrence module is enabled on a bare Type-II filtration without
the named-cell/core modules, the clone requests duplicate-flag exposure.
Static width accounting gives an additional upstream

```text
40 variables / 187 clauses                            (4.2)
```

for the three corrected chain-equality flags, selected tightness flag, and
duplicate flag.  This upstream cost is absent from (4.1).

## 5. Integration audit

The new gate is present in all required places:

1. environment parsing;
2. exact-one-filtration prerequisite check;
3. portal-branch incompatibility list;
4. Type-II duplicate exposure request;
5. plan construction before the final variable total;
6. clause emission;
7. build summary and exact category ledger.

With the new gate absent, no new plan is constructed and the Type-II
duplicate exposure predicate is unchanged.  Hence the guard-off variable and
clause streams are structurally unchanged.

The static checker is

```text
scratch/check_k11_coordinate_omission_implementation.py
SHA-256 8dac21828b36003db20af8de2de3987b2834ee555b87fb6de8b96a25e5e684f6
```

It independently verifies:

* the exact Wallace full-adder counts;
* the direct constant-comparison truth table for every nine-bit value;
* the three Type-II mode assignments;
* every inventory category; and
* all source-integration markers and guards.

Its output is

```text
PASS
Type I module increment: 15224 variables / 86185 clauses
  gates=5104/15312 counters=10120/70840 thresholds=0/33
Type II module increment: 15258 variables / 86397 clauses
  gates=5115/15345 counters=10142/70994 branch=1/3 thresholds=0/55
No local compilation or CNF generation was performed.
```

## 6. RunPod compilation and build-only confirmation

The frozen source and both audit artifacts were copied byte-for-byte to the
Rose RunPod.  Their remote hashes matched the audited values.  The static
checker passed under Python 3.11.  Compiling there with
`-O3 -std=c++2a -Wall -Wextra -Wpedantic` and the DIMACS streaming shim
produced zero warning bytes.  The streaming binary has SHA-256

```text
91bac1a91a0cf90181e5bcd8bac2a4cbf5992e2ac02aca8aeb36ae461fabf98f
```

Build-only streams to `/dev/null` exactly matched every prediction:

```text
Type I full:  3,757,755 variables / 20,738,107 clauses
  module:        15,224 variables /     86,185 clauses

Type II full: 3,777,488 variables / 20,840,854 clauses
  module:        15,258 variables /     86,397 clauses
```

No raw CNF was retained and no solver was launched or replaced.

## Scope

This is a static source implementation and audit, not a SAT/UNSAT result.
The inventories are now build-confirmed.  No live solver was stopped or
added.
