# Independent audit of the joint `k=11` band-cut implementation

## 1. Verdict

**PASS.**  The guarded implementation in

```text
k11_forest_sat.cpp
SHA-256 8e0c04ae927ecff09b1ffbbeab5f8d719963788151d317cab05b78613e47fd8d
```

is a sound and complete encoding of the globally necessary joint
rank-five/rank-six band cuts proved in
`K11_FOREST_JOINT_SHORT_BAND_CUTS.md` and independently audited in
`K11_FOREST_JOINT_SHORT_BAND_CUTS_AUDIT.md`.

I checked all of the following independently:

* the environment guard and its dependency on `K11_FOREST_BAND_CUTS`;
* formula identity when the new guard is off;
* completeness of the three rank-five maximal-chain selectors;
* exact uniqueness and binary extraction of all six rank-five boundaries;
* the strengthened `x0<=1` comparison and the bidirectional definition
  `e=x0`;
* every full-adder and guarded-comparator clause polarity;
* all twelve substituted algebraic rows;
* retention of every final carry and absence of unsigned overflow;
* the exact auxiliary inventory `1,180/8,133`; and
* the complete joint inventory `4,016/29,966`.

No fixed-row, Hamilton-path, Johnson-adjacency, connected-forest, adjacent-
shadow, or rank-three-shadow assumption is introduced.  The joint guard is
valid with only the pre-existing band guard enabled.

One wording point is worth making explicit.  The ripple adders themselves
are **not** guarded.  They are total definitional circuits and hence impose
no restriction on their inputs.  Every comparison clause, including every
prefix-equality definition, is guarded by the relevant chain selector.  This
is exactly the safe implementation; guarding the adders is unnecessary.

The independent implementation checker is

```text
scratch/verify_k11_forest_joint_band_implementation.cpp
SHA-256 2513eb5d491c0390501ce4acb6fd108bae2f0de2d419997547fe4e81a0ad8ec3
```

and reports

```text
full_adder_truth_table=PASS
guarded_comparator_truth_table=PASS
chain_A_aux=357/2460 chain_B_aux=398/2746 chain_C_aux=398/2746
arithmetic_aux=1180/8133
joint_inventory=4016/29966 PASS
```

This remains a search reduction, not a SAT or UNSAT result.

## 2. Frozen sources and comparison basis

The current local source has the claimed hash `8e0c04ae...`.  The previously
audited rank-three source is recorded as

```text
SHA-256 6b0b5621aaed7b525c5a5e4eb082bc643ac72f0a6625caf461a6a3ff6f600663
```

in `K11_FOREST_RANK3_SHADOW_IMPLEMENTATION_AUDIT.md`.

That exact previous source file was no longer present in the local tree.  I
also searched the three available remote hosts by filename and by SHA-256
over their C++ archives; no copy of `6b0b5621...` remained.  Therefore I
could not make a byte-for-byte old/new source diff.

This does not leave formula identity inferentially unsupported.  There are
three independent checks:

1. A complete search of the current source finds the new feature only in
   `JointBandCutPlan`, guard parsing/dependency checking, conditional plan
   allocation, conditional clause insertion, and diagnostics.
2. When the guard is false, `JointBandCutPlan` is never constructed, `next`
   is unchanged, and no clause from its private vector is inserted.
3. A frozen guard-off build of the current source reports exactly the prior
   audited rank-three/band inventory:

   ```text
   variables=2,885,308 clauses=14,360,485
   joint_band_cuts=0
   band_cut_variables=3026 band_cut_clauses=8361
   ```

The prior frozen rank-three build log independently records the same
`2,885,308/14,360,485` formula.  Only the diagnostic field
`joint_band_cuts=0` is new; the SAT variable and clause sets are unchanged.

## 3. Guard dependency and allocation order

The option is true exactly when `K11_FOREST_JOINT_BAND_CUTS` is nonempty and
different from the literal string `"0"`.  Before reading the seed or
allocating any SAT variable, the source checks

```text
joint_band_cuts && !band_cuts
```

and exits with status 2 and

```text
K11_FOREST_JOINT_BAND_CUTS requires K11_FOREST_BAND_CUTS
```

when the dependency is absent.  The frozen remote log reproduces this path.

The dependency is exact.  The plan reuses:

* the six exact binary rank-six boundaries from `BandCutPlan`; and
* its forced-true constant variable `one`.

It does not use any adjacent-shadow or rank-three-shadow variable.  Real
remote build-only runs with those guards disabled succeeded and added the
same joint delta:

| adjacent | rank 3 | band | joint | variables | clauses |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 | 4,899,664 | 15,563,145 |
| 1 | 0 | 1 | 1 | 3,155,344 | 14,584,521 |
| 1 | 1 | 1 | 1 | 2,889,324 | 14,390,451 |

Subtracting the corresponding frozen guard-off inventories gives exactly
`4,016` variables and `29,966` clauses in every case.

The plan is allocated after `BandCutPlan` and before `variable_total` is
frozen.  Its clauses are inserted immediately after the band clauses and
before the base formula.  Thus every fresh variable is declared, and proof
and DIMACS hooks see the complete formula.

## 4. Completeness of the three chain selectors

The ten monotone-band states are

```text
00 01 02 03 11 12 13 22 23 33.
```

The base unrestricted rank-five theorem already forbids state `03`.  A
coordinatewise monotone rank-five schedule therefore extends to one of the
following four maximal chains:

```text
A = 00 01 02 12 13 23 33
B = 00 01 02 12 22 23 33
C = 00 01 11 12 13 23 33
D = 00 01 11 12 22 23 33.
```

These are all paths from `00` to `33` which increment one endpoint at a time
without passing through `03`.  Chain D has no width-two state.  Hence every
schedule whose only maximal-chain extension is D has `y2=0` and violates the
proved inequality

```text
y2 >= y0+87+4*x0.
```

If a schedule is a subchain of D but does not force D uniquely, then it is
also a subchain of at least one of A, B, C and may choose that extension.
Consequently selecting exactly one of A, B, C loses no valid solution.

The source allocates three selector variables, one positive clause, and the
three pairwise negative clauses.  This is exact-one.  For each selected
chain, every one of the three states outside that chain is forbidden at each
of 462 slots.  The inactive-chain membership clauses contain the negated
selector and impose no condition.

A schedule may extend to more than one selected chain.  This causes no
ambiguity: skipped chain states give equal neighboring transition boundaries,
and every chain formula below evaluates to the same physical counts `y0`
and `y2`.

## 5. Exact boundary selectors and binary extraction

For each selected rank-five chain and each `j=0,...,5`, define `h_(j+1)` as
the number of slots lying in the first `j+1` chain states.  The source
allocates 463 candidate literals for boundary values `0,...,462` and one
positive clause over them.

Under the active chain selector, candidate `t` says:

* at `t=0`, slot 0 lies after chain state `j`;
* at `0<t<462`, slot `t-1` lies at or before `j` and slot `t` lies after
  `j`; or
* at `t=462`, the final slot lies at or before `j`.

The base formula gives every slot exactly one state and makes successive
states coordinatewise nondecreasing.  Restricted to a selected maximal
chain, the chain indices are therefore nondecreasing.  Exactly one of the
463 cases above is possible.  The positive boundary clause consequently is
already exact-one; quadratic at-most-one clauses would be redundant.

For each of nine binary bits, the implementation adds

```text
bit -> OR(boundaries whose integer has that bit 1)
not bit -> OR(boundaries whose integer has that bit 0).
```

Exact boundary uniqueness makes these two clauses an exact binary extraction
of the chosen integer.  Nine bits cover the complete range `0,...,462`.

The resulting clause counts are exact:

```text
six positive boundary clauses                          6
six * three chains * (2*461+2) implications      16,632
six * nine bits * two extraction clauses            108
```

## 6. Exact derivation of `e=x0`

The pre-existing rank-six chain is

```text
00 01 02 03 13 23 33.
```

Its exact boundary identities give

```text
x0 = g1+462-g6.
```

The unguarded comparison in the joint plan is

```text
g1+461 <= g6,
```

which is algebraically equivalent to `x0<=1`.

The source then defines `e` by

```text
state(position,00) -> e
state(position,33) -> e
e -> OR(all 924 state(position,00/33) literals).
```

`BandCutPlan` already forbids the other width-zero states `11` and `22`, so
these 924 literals are exactly all rank-six width-zero occurrences.  The
strengthened comparison proves at most one occurs.  Therefore `e` is not
merely an existence bit:

```text
e = x0 in {0,1}.
```

The exact definition uses one variable, 924 forward implications, and one
reverse clause, for `1/925`.

The vector

```text
{-one,-one,e}
```

is little-endian binary `4e`, not a signed expression.

## 7. Ripple adders and guarded comparators

### 7.1 Full adders

For each input-bit triple the implementation adds one clause forcing the
proper parity bit.  The six majority clauses define the next carry in both
directions.  Thus one width-`w` addition uses

```text
2w variables and 14w clauses
```

and returns `w+1` bits, including its final carry.  No addition is modular.

The independent checker exhaustively evaluated all 32 assignments of one
full-adder cell and found that its fourteen clauses accept exactly

```text
sum = a XOR b XOR carry,
next_carry = majority(a,b,carry).
```

The adders are unguarded.  For every input assignment they have one exact
extension to their output and carry variables, so they cannot constrain a
boundary, selector, `e`, or reused rank-six bit.

### 7.2 Comparators

The comparator scans from the most significant bit.  At every active prefix
it forbids the only bad first difference `x=1,y=0`.  Five clauses define the
next prefix-equality bit exactly.  Crucially, the negated chain selector is
present in all six clause types, including all five definition clauses.

For width `w`, a comparator therefore uses

```text
w-1 variables and w+5(w-1) clauses.
```

The independent checker exhaustively evaluated all width-three inputs,
both guard values, and all assignments to the two prefix auxiliaries.  It
found:

```text
guard=1: satisfiable exactly when x<=y
guard=0: satisfiable for every x,y.
```

The unguarded `x0<=1` row uses the already forced literal `one` as its guard,
so it is active exactly.

## 8. Audit of every algebraic row

The selected-chain boundaries give:

| chain | `y0` | `y2` |
|---|---|---|
| A | `462+h1-h6` | `h3+h5-h2-h4` |
| B | `462+h1+h5-h4-h6` | `h3-h2` |
| C | `462+h1+h3-h2-h6` | `h5-h4` |

The rank-six boundaries give:

```text
x0+x1 = g2+462-g5,
x3    = g4-g3.
```

Substitution into the four proved cuts produces exactly the source rows.

### Chain A

```text
y0+x0<=135:
  h1+327+e <= h6

y2>=y0+87+4*x0:
  h2+h4+h1+549+4e <= h3+h5+h6

x0+x1<=y0+3:
  g2+h6 <= h1+g5+3

y2<=x3+3:
  h3+h5+g3 <= h2+h4+g4+3
```

### Chain B

```text
y0+x0<=135:
  h1+h5+327+e <= h4+h6

y2>=y0+87+4*x0:
  h2+h1+h5+549+4e <= h3+h4+h6

x0+x1<=y0+3:
  g2+h4+h6 <= h1+h5+g5+3

y2<=x3+3:
  h3+g3 <= h2+g4+3
```

### Chain C

```text
y0+x0<=135:
  h1+h3+327+e <= h2+h6

y2>=y0+87+4*x0:
  h4+h1+h3+549+4e <= h5+h2+h6

x0+x1<=y0+3:
  g2+h2+h6 <= h1+h3+g5+3

y2<=x3+3:
  h5+g3 <= h4+g4+3
```

Every sign, constant, and operand in lines 488--516 of the frozen source
matches these transformations.

The independently proved short-pool row and total-width-455 row need not be
separate comparators.  They are algebraic consequences of the generating
rows above, as proved in the mathematical audit.  In particular, the two
cumulative nesting rows together with `x0<=1` imply total width 455, while
the fan row and first cumulative nesting row imply the short-pool cut.

## 9. Exact variable and clause inventory

### 9.1 Non-arithmetic variables

| category | variables |
|---|---:|
| exact-one chain selectors | 3 |
| six 463-way boundary selectors | 2,778 |
| six nine-bit boundary values | 54 |
| exact `e=x0` bit | 1 |
| subtotal | 2,836 |

### 9.2 Arithmetic auxiliaries

An independent width-by-width reconstruction gives:

| circuit group | variables | clauses |
|---|---:|---:|
| unguarded `x0<=1` | 27 | 181 |
| four chain-A rows | 357 | 2,460 |
| four chain-B rows | 398 | 2,746 |
| four chain-C rows | 398 | 2,746 |
| **arithmetic total** | **1,180** | **8,133** |

The different A versus B/C counts are correct: the unsigned rearrangements
have different left-associative addition widths.

### 9.3 All clauses

| category | clauses |
|---|---:|
| exact-one chain selector | 4 |
| conditional chain membership, `3*462*3` | 4,158 |
| six positive boundary clauses | 6 |
| boundary transition implications | 16,632 |
| binary boundary extraction | 108 |
| exact `e` definition | 925 |
| adders and thirteen comparisons | 8,133 |
| **total** | **29,966** |

Adding the `1,180` arithmetic variables to the `2,836` non-arithmetic
variables gives exactly

```text
joint_band_cut_variables=4016
joint_band_cut_clauses=29966.
```

The source's `variables()` method measures precisely the advancement of
`next` across this plan, while `clauses.size()` measures precisely its
private clause vector.  The real build output matches both totals.

## 10. No accidental restriction and scope

For completeness, start from any assignment satisfying the pre-existing
formula and the proved joint inequalities.

1. Choose any maximal-chain extension among A, B, C of its monotone rank-five
   schedule.  Section 4 proves that at least one exists.
2. Set each of the six boundary selectors to its unique transition count and
   set its nine bits to that integer.
3. The rank-six boundaries already have their exact values from
   `BandCutPlan`.
4. Set `e` to the unique width-zero occurrence, if one exists.
5. Extend every ripple adder by ordinary unsigned arithmetic.
6. Set each active prefix-equality variable to the equality of the higher
   bits.  Inactive comparators may be extended arbitrarily.

All clauses are then satisfied.  Conversely, every satisfying assignment
selects one compatible chain, exact boundaries, exact arithmetic, and obeys
the twelve active necessary rows plus `x0<=1`.  Hence the encoding is both
sound and complete for the intended cuts.

The implementation does not prove that a length-465 array exists or does not
exist.  A SAT result still needs independent contiguous-OR verification.  An
UNSAT theorem still needs an archived DIMACS/proof pair and independent proof
checking.
