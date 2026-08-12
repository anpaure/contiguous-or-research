# Exact monotone-band cuts in the unrestricted `k=11` forest solver

## Status

`k11_forest_sat.cpp` now has the optional environment guard

```text
K11_FOREST_BAND_CUTS=1
```

which adds all four globally valid rank-six band inequalities from
`K11_INTEGRATED_SEARCH.md`, Section 8.2:

```text
x0 <= 3
2*x0+x1 <= 138
sum(width_i) >= 1008
x3 >= 93
```

Here `xj` counts the chosen **rank-six** central witnesses of width
`beta-alpha=j`.  These cuts do not apply to the independently chosen rank-five
schedule.  The implementation remains unrestricted: it assumes neither a
fixed derivative row nor a Hamilton/Johnson path.

The guard adds exactly

```text
3,026 variables
8,361 clauses
```

to either the original forest formula or the adjacent-shadow-compressed
formula.  Guard-off inventories are unchanged.

## 1. Why the ten states collapse to one chain

The rank-six schedule has states

\[
 (\alpha_i,\beta_i),\qquad
 0\leq\alpha_i\leq\beta_i\leq3,
\]

with both coordinates nondecreasing.  Width three is possible only in state
`03`.  The proved inequality `x3>=93` therefore forces state `03` to occur.

The states `11`, `12`, and `22` are incomparable with `03` in the coordinate
order.  A coordinatewise monotone sequence cannot contain an incomparable
pair in either order.  Hence every schedule satisfying the four necessary
inequalities lies on the single total chain

```text
00, 01, 02, 03, 13, 23, 33.
```

Forbidding `11`, `12`, and `22` is consequently not an additional ansatz; it
is a logical consequence of the necessary `x3` inequality and schedule
monotonicity.

Let `c0,...,c6` be the block lengths along this chain, and define the six
cumulative transition positions

\[
\begin{aligned}
b_1&=c_0,\\
b_2&=c_0+c_1,\\
b_3&=c_0+c_1+c_2,\\
b_4&=c_0+c_1+c_2+c_3,\\
b_5&=c_0+\cdots+c_4,\\
b_6&=c_0+\cdots+c_5.
\end{aligned}
\]

The schedule length is `M=462`, so `c6=M-b6`.  The width classes are

\[
x_0=c_0+c_6,\quad x_1=c_1+c_5,\quad
x_2=c_2+c_4,\quad x_3=c_3.
\]

Straight telescoping turns the four pseudo-Boolean inequalities into

\[
\begin{array}{rcl}
b_1+459&\leq&b_6,\\
b_1+b_2+786&\leq&b_5+b_6,\\
b_1+b_2+b_3+1008&\leq&b_4+b_5+b_6,\\
b_3+93&\leq&b_4.
\end{array}                                      \tag{1}
\]

Indeed,

\[
\begin{aligned}
x_0&=b_1+462-b_6,\\
2x_0+x_1&=924+b_1+b_2-b_5-b_6,\\
\sum_i(\beta_i-\alpha_i)
 &=b_4+b_5+b_6-b_1-b_2-b_3,\\
x_3&=b_4-b_3.
\end{aligned}
\]

This is the reason a generic cardinality network is unnecessary.

## 2. Exact CNF encoding

For each of the six boundaries and every `t in {0,...,462}`, introduce
`B[j,t]`.  It means `bj=t`.  For an internal `t`, its two implications are

```text
B[j,t] -> slot[t-1] is at or before chain state j
B[j,t] -> slot[t]   is after chain state j.
```

There are analogous one-sided implications at `t=0` and `t=462`, plus one
positive clause over all 463 selectors.

No pairwise at-most-one clauses are needed.  The pre-existing monotone
schedule has a unique transition across each chain cut, so two different
selectors cannot both satisfy their implications.  The positive clause
therefore forces exactly the correct selector.

Each boundary is converted to nine little-endian binary bits.  Given the
unique selector, a bit is defined by only two long clauses:

```text
bit  -> OR(B[j,t] : bit_r(t)=1)
!bit -> OR(B[j,t] : bit_r(t)=0).
```

Eight small ripple additions construct the four sides of (1).  Every adder
stage has an exact three-input parity output and exact majority carry; the
final carry is retained, so no arithmetic is modular.  Four lexicographic
comparators forbid `left>right` by maintaining equality of the more
significant prefix.

Thus every auxiliary variable is functionally tied to the selected monotone
schedule.  Conversely, every schedule satisfying the four numerical cuts
extends to the unique boundary values and ordinary binary arithmetic wires.
The encoding is exact in both directions.

## 3. Independent inventory

The added variables are

| category | count |
|---|---:|
| one-hot boundary selectors, `6*463` | 2,778 |
| binary boundary bits, `6*9` | 54 |
| fixed-true constant | 1 |
| eight ripple adders, 77 stages at two wires each | 154 |
| comparator prefix-equality wires | 39 |
| **total** | **3,026** |

The added clauses are

| category | count |
|---|---:|
| fixed-true unit | 1 |
| forbid `11,12,22` in 462 slots | 1,386 |
| boundary positive clauses | 6 |
| boundary transition implications | 5,544 |
| binary extraction, `6*9*2` | 108 |
| ripple adders, `77*14` | 1,078 |
| four comparators of widths `10,11,12,10` | 238 |
| **total** | **8,361** |

The comparator count uses `6w-5` clauses at width `w`.

## 4. Scope and exactness

The mathematical source of the cuts is the fan-capped lower-slab theorem and
the independent short-interval-pool count:

* `x0<=3` uses the rank-five antichain;
* `2*x0+x1<=138` uses ranks four and five, of chain height two;
* `sum(width)>=1008` uses the complete nonzero ideal of ranks one through
  five, of chain height five;
* `x3>=93` is the independent count forcing at least 93 length-four selected
  rank-six witnesses.

They concern the witnesses chosen for the rank-six antichain.  Applying them
to rank five would be an unjustified strengthening, so the implementation
uses only `central[1]`.

Every universal nonzero array of length 465 has a rank-six monotone schedule
and satisfies these four inequalities.  Therefore enabling the guard cannot
remove a genuine optimum.  The original forest formula's soundness is also
unchanged, since only necessary clauses are added.  Consequently the guarded
formula is still SAT if and only if `nu(11)=465`.

The guard composes independently with
`K11_FOREST_ADJACENT_SHADOWS=1`; neither encoding relies on the other's
auxiliary variables.

## 5. Reproduction evidence

The standalone C++ checker is

```text
scratch/verify_k11_forest_band_cuts.cpp
```

It independently rebuilt the circuit and compared it with direct arithmetic
on 1,320 fixed monotone schedules: 264 deterministic threshold/random block
profiles on each of all five maximal chains of the original ten-state poset.
The remote `-O3` run reported

```text
added_variables=3026 added_clauses=8361
fixed_schedule_equivalence_cases=1320 expected_sat=66 expected_unsat=1254 PASS
```

A remote `-O3` CaDiCaL build-only smoke test then reproduced all four complete
formula inventories:

| adjacent shadows | band cuts | variables | clauses |
|---:|---:|---:|---:|
| 0 | 0 | 4,892,622 | 15,524,818 |
| 0 | 1 | 4,895,648 | 15,533,179 |
| 1 | 0 | 3,148,302 | 14,546,194 |
| 1 | 1 | 3,151,328 | 14,554,555 |

The two guard-off rows exactly match their previously frozen inventories; the
two guard-on rows differ by precisely 3,026 variables and 8,361 clauses.

Typical build-only invocation:

```bash
K11_FOREST_BUILD_ONLY=1 \
K11_FOREST_ADJACENT_SHADOWS=1 \
K11_FOREST_BAND_CUTS=1 \
./k11_forest_sat seed465.txt ignored_output.txt 1
```

Any future SAT model still requires both independent OR verifiers.  Any UNSAT
claim still requires an archived CNF/proof pair and independent proof check;
the band-cut smoke tests make no SAT/UNSAT claim for the full instance.
