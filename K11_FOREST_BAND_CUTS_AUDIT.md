# Independent audit of the exact `k=11` forest band cuts

## 1. Verdict

The guarded band-cut addition is mathematically and logically sound.

For the frozen source

```text
0a3db930fc343589fd9840b042a896c2b428459de6c3e3203ed45d676d10b9bc
    k11_forest_sat.cpp
```

setting

```text
K11_FOREST_BAND_CUTS=1
```

adds exactly the four necessary inequalities

```text
x0 <= 3
2*x0+x1 <= 138
sum(width_i) >= 1008
x3 >= 93
```

to the chosen rank-six witness schedule.  It does not impose a fixed-row,
Johnson-path, or Hamilton-path ansatz.  The implication from `x3>0` to the
seven-state chain is valid, all four boundary identities are correct, the
selector and binary encodings are exact, and the adder/comparator circuit is
non-modular and bidirectionally exact.

The implementation adds exactly

```text
3,026 variables
8,361 clauses
```

whether or not `K11_FOREST_ADJACENT_SHADOWS` is enabled.  With the band guard
off, no band variable is allocated and no band clause is emitted.  The two
guard-off inventories reproduce their previously frozen values.

This audit certifies the band-cut delta and its interface with the existing
forest formula.  It does not by itself re-audit every clause of the much
larger base forest encoding, and the build-only runs make no SAT or UNSAT
claim for the full instance.

## 2. Frozen artifacts

The files inspected were

```text
dae6eb0dab4a0e0fe7428fb6f6c9d4a5ad9c53e0dcaa1acee4b11ec7145d4f28
    K11_FOREST_BAND_CUTS.md
0a3db930fc343589fd9840b042a896c2b428459de6c3e3203ed45d676d10b9bc
    k11_forest_sat.cpp
35cabb8c4d498c95b2329cd3c21d82af6775d8d43cc499708a8439251e905982
    scratch/verify_k11_forest_band_cuts.cpp
```

The source was inspected line by line.  The standalone checker was also
compiled against an independent CaDiCaL build and run at `-O3` on the remote
compute host; Section 10 records the output.

## 3. Why all four inequalities are globally valid

Let an arbitrary nonzero universal array on eleven bits have length

```text
N=465.
```

Choose one witnessing interval for each of the

```text
M=binom(11,6)=462
```

rank-six masks.  Since distinct rank-six masks are incomparable, their
selected intervals have distinct left endpoints and distinct right
endpoints.  After sorting by left endpoint, both endpoint sequences strictly
increase.  Writing

```text
I_i=[i+alpha_i,i+beta_i]
```

gives nondecreasing `alpha_i,beta_i` in `[0,3]`.  Put

```text
w_i=beta_i-alpha_i
x_j=#{i:w_i=j}.
```

The excess is `D=N-M=3`.

Every witness for a mask of rank at most five avoids containing every
complete selected rank-six interval: interval containment would imply
containment of the corresponding OR masks, which is impossible across these
ranks.  Therefore the fan-capped avoidance theorem applies to any family of
lower masks.  For a family of chain height `h`, it gives

```text
|F| <= sum_i min(w_i,h) + hD.
```

### 3.1 `x0<=3`

Take all `binom(11,5)=462` rank-five masks.  This is an antichain, so `h=1`,
and

```text
sum_i min(w_i,1)=462-x0.
```

Thus

```text
462 <= 462-x0+3,
```

which is exactly `x0<=3`.

### 3.2 `2*x0+x1<=138`

Take all masks of ranks four and five.  Their number and chain height are

```text
binom(11,4)+binom(11,5)=330+462=792,
h=2.
```

Since

```text
sum_i min(w_i,2)=2*462-(2*x0+x1),
```

the fan cap gives

```text
792 <= 924-(2*x0+x1)+6,
```

or `2*x0+x1<=138`.

### 3.3 `sum(width_i)>=1008`

Take the complete nonempty ideal of ranks one through five.  It contains

```text
11+55+165+330+462=1023
```

masks and has chain height five.  Every `w_i` is at most three, hence

```text
sum_i min(w_i,5)=sum_i w_i.
```

The fan cap yields

```text
1023 <= sum_i w_i + 5*3,
```

so `sum_i w_i>=1008`.

### 3.4 `x3>=93`

This inequality uses a separate physical-interval count.  Every interval of
length at least four contains a selected rank-six witness.  Indeed, if
`J=[a,b]` has length at least four, then `a<=462` and

```text
I_a subseteq [a,a+3] subseteq J.
```

Consequently every rank-one-through-five mask must be witnessed by an
interval of length at most three.  There are exactly

```text
465+464+463=1392
```

such physical intervals.  The 1023 lower masks require 1023 distinct ones.
The selected rank-six witnesses of width at most two require another
`462-x3` distinct short intervals, disjoint from the lower witnesses because
their OR values have different ranks.  Therefore

```text
1023+(462-x3) <= 1392,
```

and `x3>=93`.

These derivations use only an arbitrary selected rank-six antichain schedule
in an unrestricted length-465 solution.  In particular, none assumes that
the witnesses are all four-windows.

## 4. Collapse from ten states to seven

The ten possible endpoint states are

```text
00 01 02 03 11 12 13 22 23 33.
```

The only width-three state is `03`.  Since `x3>=93`, state `03` occurs.  A
coordinatewise nondecreasing schedule containing `03` cannot also contain a
state incomparable with `03`.  The incomparable states are exactly

```text
11 12 22.
```

Every remaining state belongs to the total chain

```text
00 < 01 < 02 < 03 < 13 < 23 < 33.
```

The clauses forbidding state indices `{4,5,7}` therefore follow from a
necessary inequality plus the already-present monotonicity; they are not an
extra structural ansatz.  The source's chain index array

```text
{0,1,2,3,6,8,9}
```

matches the seven displayed states exactly.  The plan is constructed with
`central[1]`, and the initialization `rank=5+layer` confirms that this is the
rank-six schedule, not the independently chosen rank-five schedule.

## 5. Boundary algebra

Let `c0,...,c6` be the multiplicities of the seven chain states and let

```text
b1=c0
b2=c0+c1
b3=c0+c1+c2
b4=c0+c1+c2+c3
b5=c0+c1+c2+c3+c4
b6=c0+c1+c2+c3+c4+c5.
```

Since the total is 462, direct expansion gives

```text
x0 = b1+462-b6
x1 = (b2-b1)+(b6-b5)
x3 = b4-b3
sum(width_i) = b4+b5+b6-b1-b2-b3.
```

Hence

```text
2*x0+x1 = 924+b1+b2-b5-b6.
```

The four original inequalities are therefore exactly equivalent to

```text
b1+459             <= b6
b1+b2+786          <= b5+b6
b1+b2+b3+1008      <= b4+b5+b6
b3+93              <= b4.
```

There is no sign reversal or off-by-one error in these identities.

## 6. Exactness of the boundary selectors

For chain cut `j`, define `b_j` to be the number of schedule slots in chain
states `0,...,j`.  The base formula already enforces exactly one state per
slot and coordinatewise monotonicity.  After the three incomparable states
are forbidden, the chain-state indices are nondecreasing.

For a proposed selector `B[j,t]`, the emitted implications say:

* at `t=0`, slot zero is after the cut;
* at `0<t<462`, slot `t-1` is at or before the cut and slot `t` is after it;
* at `t=462`, the final slot is at or before the cut.

For any fixed monotone schedule, exactly one value of `t` satisfies these
conditions: the actual number of slots at or before the cut.  Every other
selector implies a false state-membership clause.  The one positive clause
over all 463 selectors consequently forces the correct selector true and all
others false.  Pairwise at-most-one clauses are unnecessary, but only because
the base one-state and monotonicity clauses are present.

The boundary implication inventory is also exact.  Per cut it is

```text
1 at t=0 + 2*461 internal + 1 at t=462 = 924,
```

and over six cuts this is `5,544` clauses.

## 7. Exact binary extraction

For each boundary bit `z`, the code emits

```text
!z OR OR(B[j,t] with bit(t)=1)
 z OR OR(B[j,t] with bit(t)=0).
```

With exactly one selected `t`, these clauses force `z=1` when that `t` has a
one bit and force `z=0` otherwise.  Conversely, the forced value satisfies
both clauses.  Nine little-endian bits suffice because every boundary lies
in `[0,462]`.

Thus the unusually small `2*9` clauses per boundary are an exact definition,
not merely a one-way implication.

## 8. Exact arithmetic circuit

### 8.1 Ripple adders

At each bit, the eight parity clauses enumerate every assignment of the
three inputs and force the sum bit to their XOR.  The remaining six clauses
define the carry as the majority of the three inputs: three forward clauses
force it when any input pair is true, and three reverse clauses rule it out
when fewer than two inputs are true.

The fixed variable `one` is constrained by a unit clause.  The literal
`-one` therefore supplies exact zero padding and the initial zero carry.
Each stage retains its outgoing carry, and `add_unsigned` appends the final
carry to the result.  The arithmetic is ordinary unsigned addition, not
addition modulo a power of two.

The eight calls use

```text
9+10+9+10 + 9+10+11+9 = 77
```

full-adder stages.  They introduce `2*77=154` variables and
`14*77=1,078` clauses.

### 8.2 Comparators

`add_leq` scans from the most significant bit.  While `equal_above` is true,
the clause

```text
!equal_above OR !x_bit OR y_bit
```

forbids the only bad first difference, namely `x_bit=1,y_bit=0`.  At every
nonfinal bit, five further clauses define

```text
next_equal <-> equal_above AND (x_bit == y_bit).
```

The two implications from `next_equal` force the previous prefix equality
and current-bit equality; the two reverse four-literal clauses force
`next_equal` in the `00` and `11` equality cases.  Thus a lower bit is ignored
exactly after the first strict difference, and the comparator is equivalent
to unsigned `x<=y`.

After zero extension, the comparison widths are

```text
10, 11, 12, 10.
```

The prefix-equality variables number

```text
9+10+11+9=39,
```

and the clauses number

```text
(6*10-5)+(6*11-5)+(6*12-5)+(6*10-5)=238.
```

The largest possible sums fit in the retained widths, so there is no
overflow truncation.

## 9. Exact inventory

The variable delta is

| category | count |
|---|---:|
| fixed-true variable | 1 |
| six sets of 463 selectors | 2,778 |
| six nine-bit boundary values | 54 |
| 77 full-adder sum/carry pairs | 154 |
| comparator prefix-equality wires | 39 |
| **total** | **3,026** |

The clause delta is

| category | count |
|---|---:|
| fixed-true unit | 1 |
| forbid `11,12,22` in 462 slots | 1,386 |
| six positive selector clauses | 6 |
| selector transition implications | 5,544 |
| binary extraction | 108 |
| full adders | 1,078 |
| comparators | 238 |
| **total** | **8,361** |

Both totals agree with the implementation and independent builds.

## 10. Independent executions

The standalone checker was compiled remotely from the frozen checker source
against `/root/cadical/build/libcadical.a` and run with optimization.  It
reported

```text
added_variables=3026 added_clauses=8361
fixed_schedule_equivalence_cases=1320 expected_sat=66 expected_unsat=1254 PASS
```

Its 1,320 pinned schedules consist of 264 deterministic/random block profiles
on each of the five maximal chains of the ten-state triangular poset.  The
five chains are the complete set of maximal chains.  The test is a useful
independent regression: schedules on the unique chain containing `03` test
both satisfying and failing arithmetic profiles, while the other four chains
must fail `x3>=93`.  It is finite test evidence rather than the proof of all
schedules; Sections 3--8 provide that proof.

A second remote build used the exact frozen main source and the same 465-term
seed in all four guard combinations.  The output was

| adjacent shadows | band cuts | variables | clauses |
|---:|---:|---:|---:|
| 0 | 0 | 4,892,622 | 15,524,818 |
| 0 | 1 | 4,895,648 | 15,533,179 |
| 1 | 0 | 3,148,302 | 14,546,194 |
| 1 | 1 | 3,151,328 | 14,554,555 |

In both adjacent-shadow modes the difference is exactly 3,026 variables and
8,361 clauses.

## 11. Guard-off identity and composition

The source reads the guard as enabled only for a nonempty value other than
`"0"`.  When disabled, `band_cut_plan` remains null.  No call to its
constructor occurs, so `next` is not advanced; the loop adding its clauses is
also skipped.  The class definition has no other side effect.  This proves
source-level identity of the generated base formula with the guard-off path,
and the two reproduced guard-off inventories provide an independent runtime
check.

When adjacent shadows are enabled, all of their variables are allocated
first.  The band plan then allocates fresh identifiers from the resulting
`next` value.  Its only nonfresh inputs are the existing rank-six state
variables.  It neither reads nor aliases any adjacent-shadow auxiliary.
Conversely, the adjacent-shadow clauses do not depend on band auxiliaries.
The two encodings therefore compose by conjunction, and the identical deltas
in the two build modes confirm the allocation boundary.

Since every added clause expresses a globally necessary property of any
length-465 universal array, the guarded formula cannot discard a genuine
optimum.  Since the addition only strengthens the existing formula, it also
cannot introduce a new spurious model.  Therefore it preserves the base
formula's soundness and completeness while pruning its unrestricted rank-six
band schedules.

## 12. Final audit ledger

| item | verdict |
|---|---|
| global hypotheses of all four inequalities | proved |
| application only to rank six | correct |
| `x3>0` forces the seven-state chain | proved |
| boundary telescoping formulas | exact |
| selector uniqueness without pairwise clauses | exact under the base one-hot/monotone clauses |
| two-clause binary extraction | exact |
| full-adder CNF | exact XOR plus majority |
| comparator CNF | exact unsigned `<=` |
| arithmetic overflow handling | exact; final carries retained |
| variable delta | 3,026, independently reproduced |
| clause delta | 8,361, independently reproduced |
| composition with adjacent shadows | safe and independently reproduced |
| guard-off formula path | unchanged, by control flow and inventory |
| full-instance SAT/UNSAT conclusion | none claimed |

