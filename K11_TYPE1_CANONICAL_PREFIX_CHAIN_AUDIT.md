# Independent audit of the Type-I canonical prefix chain

## Verdict

**PASS as a mathematical and encoding design.**  With Type I and residual
coordinate lex both enabled, every interval containing position zero has OR
in

```text
63, 1087, 1599, 1855, 1983, 2047.
```

It is therefore sound to force every noncanonical upper-target witness into
positions `1,...,464`.  After removing endpoint-containment duplicates and
compressing exact-one generic selectors, the cut needs no variables and
exactly `32` clauses with the current direct/compressed target portfolio.

The compressed production implementation and build audit are recorded in
`K11_TYPE1_CANONICAL_PREFIX_CHAIN_IMPLEMENTATION_AUDIT.md`.

## 1. Lex direction

The existing comparator for adjacent columns `x,y` adds, while their earlier
prefix is equal,

```text
!x or y.
```

Thus the forbidden first unequal pair is `(x,y)=(1,0)`, exactly the usual
binary lexicographic condition

```text
column(x) <=lex column(y).
```

In Type I the residual module applies this to

```text
column(6)<=lex column(7)<=lex ... <=lex column(10).
```

All outside columns are zero at position zero because `A[0]=63`.  Let `f_b`
be the first positive position in column `b`.  Singleton coverage guarantees
that every outside coordinate occurs, so every `f_b` exists.  If `a<b` but
`f_a<f_b`, the first unequal pair for columns `a,b` is `(1,0)`, a
contradiction.  Hence

```text
f_10 <= f_9 <= f_8 <= f_7 <= f_6.                 (1.1)
```

This confirms the direction in the design note; reversing (1.1) would be an
error.

## 2. Decimal masks and prefix classification

Any interval containing position zero is a prefix.  It already contains all
low coordinates `0,...,5`, and by (1.1) its outside coordinates form an
upper suffix of `6,7,8,9,10`.  Simultaneous first occurrences may skip a
chain member but create no other mask.  The six possible values are

| rank | decimal | added outside coordinates |
|---:|---:|---|
| 6 | 63 | none |
| 7 | 1087 | 10 |
| 8 | 1599 | 10,9 |
| 9 | 1855 | 10,9,8 |
| 10 | 1983 | 10,9,8,7 |
| 11 | 2047 | 10,9,8,7,6 |

The independent checker recomputes these masks and exhausts finite
first-occurrence schedules including ties.

## 3. WLOG composition

Type I has already used coordinate and reversal symmetry to put the unique
literal six-set at the left endpoint as

```text
A[0]={0,1,2,3,4,5}.
```

The remaining coordinate group is

```text
S_{0,...,5} x S_{6,...,10}.
```

Sorting the five outside occurrence columns uses only its second factor and
fixes `A[0]` setwise.  It does not disturb the endpoint orientation.  The
enabled Type-I structural modules are coordinate-equivariant under this
stabilizer, while the direct target families and compressed rank-seven
columns are complete families and are merely renamed.  Exception slots are
generic and their target-selector columns are renamed with the targets.

Therefore the prefix-chain cut is a consequence of the simultaneous Type-I
and residual-lex quotient.  It is not sound under Type I alone, residual lex
alone, Type II, or a coordinate-named portal branch.  A production guard
must require both exact prerequisites.

## 4. Exact clause schemas

Let `Inside(0)` denote the already allocated membership literal for the
selected witness interval.

If a target does not contain `63`, an existing absent-bit clause together
with `A[0]=63` already forces its witness out of position zero (guarded by
`active` for a crossed target).  Only endpoint supersets excluded
specifically by residual lex need new clauses.

### Direct ranks eight through ten

Every endpoint superset other than the unique canonical target of its rank
receives the unit clause

```text
-Inside(0).
```

The exemptions are exactly

```text
rank 8: 1599
rank 9: 1855
rank 10: 1983.
```

The number of clauses is

```text
(C(5,2)-1)+(C(5,3)-1)+(C(5,4)-1)
=9+9+4=22.                                         (4.1)
```

### Crossed rank-seven witnesses

For each of the four noncanonical rank-seven endpoint supersets, the physical
interval matters only when its `active` alternative is selected.  The exact
clause is

```text
-active or -Inside(0).                              (4.2)
```

The sole exemption is target `1087`, leaving

```text
C(5,1)-1=4                                         (4.3)
```

clauses.

### Generic rank-seven exception slots

Each of the six slots chooses exactly one target through `slot.q[column]`:
two distinct seven-set selectors would force its exact rank-seven value to
have rank at least eight.  If `c` is the column of target `1087`, add once
per slot

```text
-slot.Inside(0) or slot.q[c].                       (4.4)
```

Under exact-one target selection this is equivalent to all old noncanonical
target guards.  It contributes

```text
6 clauses.                                          (4.5)
```

It would be wrong to impose `-slot.Inside(0)` unconditionally: that would
also remove the canonical target from the generic alternative.

The total is

```text
22+4+6=32 clauses, 0 variables.                     (4.6)
```

The rank-eleven target is uniquely `2047`, so it needs no clause.  Rank six
is the anchored `63`.  Existing Type-I lower-core cuts already move the
relevant lower targets into the suffix; they are not part of this upper cut.

## 5. Checker

`scratch/check_k11_type1_canonical_prefix_chain.py` independently checks:

* the lex/first-occurrence direction on all short binary column pairs;
* the six decimal masks and their ranks;
* all bounded ordered first-occurrence schedules, including ties;
* the three clause counts;
* truth tables for the unit and selector-guarded clause schemas.

The cut remains a search reduction, not a SAT or UNSAT result.
