# Next sound strengthenings after B2 and PTge5

## Scope

This note compares three optional, logically nonredundant additions to the
`k=11,n=465` formula after the coordinate-pair occurrence (`B2`) and PTge5
modules.  It is a theorem and source-inventory note only.  No local CNF was
built and no solver was run.

The inventories below are **incremental**.  They assume that the exact
one-coordinate omission flags, the 55 B2 joint-omission flags/counters, and
the short-cell rank-vector flags already exist.  Alternative numbers are
given when one-coordinate rank-resolved candidate flags are also retained.

Throughout, `B` denotes a coordinate set, and `free_B[p]` means that physical
low entry `p` omits every coordinate of `B`.

## 1. Exact two-component B2 row

Work in the Type-II two-component branch.  Let `C1` be the selected
slack-one low component and `C2` the selected slack-two component.  For a
coordinate pair `B={b,c}`, let

```text
Z1_B = number of B-free positions in C1,
Z2_B = number of B-free positions in C2,
R2_B = number of nonempty B-free runs in C2.
```

There are

```text
C(9,1)+C(9,2)+C(9,3)+C(9,4)=255
```

nonempty lower masks omitting `B`.  Every such target represented in `C1`
must be literal, because every internal adjacent pair in the slack-one
component has OR-rank five.  Thus `C1` supplies at most `Z1_B` targets.  In
`C2`, a lower witness has length at most two.  The B-free singleton and
adjacent-pair cells number

```text
Z2_B + (Z2_B-R2_B) = 2*Z2_B-R2_B.
```

Choosing one selected witness for each of the 255 distinct targets gives the
exact necessary row

```text
Z1_B+2*Z2_B-R2_B >=255.                         (C2-B2)
```

Since `Z_B=Z1_B+Z2_B`, the source comparison is

```text
255+R2_B <= Z_B+Z2_B.
```

It is guarded by `two_components`.

### Source-style encoding

This tier requires the already existing exact `slack_two_membership[p]`
bank from `K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION`.  Retain the B2
`free_B[p]` bank at zero CNF cost, and define

```text
z2[p] <-> free_B[p] AND slack_two_membership[p]       (465 gates),
r2[0] = z2[0],
r2[p] <-> z2[p] AND !z2[p-1]                         (464 gates).
```

Exactly count `z2` and `r2`, add the two nine-bit sides, and compare the two
ten-bit sums under `two_components`.

Per coordinate pair:

| item | variables | clauses |
|---|---:|---:|
| 465 `z2` AND gates | 465 | 1,395 |
| 464 run-start AND-NOT gates | 464 | 1,392 |
| exact `Z2` and `R2` counters | 1,844 | 12,908 |
| two nine-bit additions + guarded ten-bit comparator | 45 | 307 |
| **total** | **2,818** | **16,002** |

Across all 55 coordinate pairs:

```text
154,990 variables / 880,110 clauses.              (1.1)
```

A cheaper projection drops `R2_B` and imposes

```text
Z_B+Z2_B >=255.
```

It costs, across all pairs,

```text
77,275 variables / 439,065 clauses,
```

using a direct guarded constant comparator.  It is weaker than `(C2-B2)`
but is a useful low-memory probe.

The exact row is not implied by `Z_B>=128`: for example, the occurrence row
does not prevent all 128 free positions from lying in `C1`, where their
capacity is only 128 rather than 255.

## 2. Rank-resolved pair-omission rows

For `r=1,2,3,4`, the number of rank-`r` targets omitting a fixed pair `B` is

```text
r:             1    2    3     4
C(9,r):        9   36   84   126.
```

Let `n_r(B)` count B-free singleton cells of exact rank `r`, `P_r(B)` count
B-free adjacent-pair cells of exact OR-rank `r`, and `T_r(B)` count B-free
length-three cells of exact OR-rank `r`.  Selecting one physical witness for
each target gives

```text
Type I / tight Type II:  n_r(B)+P_r(B) >= C(9,r),
non-tight Type II:       n_r(B)+P_r(B)+T_r(B) >= C(9,r).       (R-B2)
```

For `r=1`, the simpler unconditional consequence `n_1(B)>=9` suffices: a
nonempty OR equal to a singleton contains that singleton as a literal entry.
The base per-target clauses already expose this fact, so rank one should not
be re-encoded merely as a redundant aggregate row.  Its inventory is listed
below only to make the full `r<=4` comparison explicit.

These rows are pointwise stronger than rank-blind B2.  B2 can put all of its
free capacity into cells of the wrong OR-rank, while `(R-B2)` cannot.

### Encoding from only B2 + rank-vector banks

For `r=2,3,4`, define one exact output per candidate cell:

```text
s[p] <-> rank[p]==r AND free_B[p],
p[e] <-> pair_rank_r[e] AND free_B[left(e)] AND free_B[right(e)],
t[e] <-> triple_rank_r[e] AND free_B[p] AND free_B[p+1] AND free_B[p+2].
```

Use a combined `s+p` counter.  Type II also exactly counts `t`, adds it to
`s+p`, and compares the two branch capacities directly with the constant.
Direct first-difference comparisons allocate no equality-prefix variables.

Exact all-pair incremental inventories are:

| branch/rank | variables | clauses |
|---|---:|---:|
| Type I, `r=1` | 76,120 | 430,870 |
| Type I, `r=2` | 152,625 | 890,010 |
| Type I, `r=3` | 152,625 | 890,065 |
| Type I, `r=4` | 152,625 | 890,230 |
| Type II, `r=1` | 76,285 | 431,805 |
| Type II, `r=2` | 230,010 | 1,380,500 |
| Type II, `r=3` | 230,010 | 1,380,610 |
| Type II, `r=4` | 230,010 | 1,380,940 |

All of `r=2,3,4` at once cost

```text
Type I:  457,875 variables / 2,670,305 clauses,
Type II: 690,030 variables / 4,142,050 clauses.       (2.1)
```

Those full tiers are too large for the first 32-GB benchmark.  Rank four is
the natural single-row probe because it has the largest target family.

If the existing one-coordinate rank-resolved candidate banks are retained,
each two-coordinate candidate is only the AND of its `b`-free and `c`-free
versions.  The optimized rank-four costs fall to

```text
Type I:  152,625 variables / 864,765 clauses,
Type II: 230,010 variables / 1,304,490 clauses.       (2.2)
```

The slightly larger previously quoted inventories `153,120/867,460` and
`231,055/1,310,210` use the generic guarded prefix comparator.  `(2.2)` uses
the direct guarded constant comparator already present in the B2 source.

## 3. Three-coordinate aggregate omission row

Fix a coordinate triple `B`.  There are

```text
C(8,1)+C(8,2)+C(8,3)+C(8,4)=162
```

nonempty lower targets omitting `B`.  Let `Z_B` be the number of B-free low
positions.

In a tight branch, B-free singleton/pair cells have capacity at most
`2*Z_B-R_B<=2*Z_B-1`.  Hence

```text
Z_B>=82.                                             (B3-tight)
```

In the non-tight branch, all singleton/pair/triple cells have capacity
`3*Z_B-3*R_B+I_B<=3*Z_B-2`, where `I_B` is the number of singleton free runs.
Hence

```text
Z_B>=55.                                             (B3-01)
```

The rank-five augmentation counts another `C(8,5)=56` targets.  For
`Z_B>=2`, all B-free low cells of lengths one through three number at most
`3*Z_B-3`; at most `n5` literal rank-five positions can help.  Thus

```text
3*Z_B+n5>=221.                                       (B3-r5)
```

The last row is redundant after `Z_B>=82`, so it should be emitted only in
non-tight Type II.

### Source-style encoding

For every coordinate triple, choose a canonical contained pair and define

```text
free3[p,a,b,c] <-> free2[p,a,b] AND free[p,c].
```

Exactly count these flags and apply the branch thresholds.  Across all
`C(11,3)=165` triples:

```text
Type I:  228,360 variables / 1,292,775 clauses,
Type II: 228,855 variables / 1,296,405 clauses.       (3.1)
```

The optional non-tight `(B3-r5)` arithmetic adds

```text
6,270 variables / 44,880 clauses.                    (3.2)
```

B3 is not implied by all B2 occurrence rows.  In a tight abstract incidence
profile, take 27 positions omitting all three coordinates and 101 further
positions for each of the three pair-only omission types.  Every pair then
has count 128, while the triple count is only 27.  In the non-tight branch,
three disjoint pair-only banks of size 86 give all B2 counts with triple
count zero.  Thus `(B3-tight)/(B3-01)` test a genuinely new third-order
intersection.

## 4. Recommendation under the approximately 32-GB RunPod limit

Do not stack all three tiers in the first build.

1. **Type II:** add the exact two-component row `(C2-B2)` first, provided
   `K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION` is already enabled.  Its
   `880,110` clauses are the smallest exact tier among the three, and it
   attacks the known two-core escape directly.  If the RunPod build-only
   audit is too close to the memory ceiling, try its `439,065`-clause
   no-run projection first.
2. **Type I:** `(C2-B2)` is unavailable.  Add only the rank-four instance of
   `(R-B2)`, not all ranks.  Its cost is about `0.89M` clauses from the B2
   banks alone, or `0.865M` when the one-coordinate rank-four flags already
   exist.
3. **B3:** hold the aggregate triple tier for the next independent
   benchmark.  It is genuinely new but costs about `1.30M` clauses and is
   rank-blind; the rank-four B2 row gives more targeted propagation at a
   comparable or smaller cost.
4. Run a RunPod **build-only token/inventory audit** before replacing a
   solver.  These increments are roughly 4--7 percent of the present
   21.3-million-clause Type-II formula; actual resident-memory change must be
   measured rather than inferred from clause count.

The practical order is therefore

```text
Type II: exact C2-B2 -> rank-4 B2 -> B3,
Type I:  rank-4 B2   -> B3.
```

All three are redundant necessary cuts.  None is a SAT/UNSAT result.
