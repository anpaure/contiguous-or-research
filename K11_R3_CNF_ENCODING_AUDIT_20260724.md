# Independent audit of the exact `R3` CNF refinement

## Verdict

The opt-in implementation in

```text
scratch/k11_core_incidence/k11_forest_sat_r3cuts.cpp
SHA-256 f4b21d6c7b4ad8ba1a326b621980cda7dee2c491c491b9764ca8f52c061906fa
```

is sound as written.  This audit found no wrong contribution gate, sign,
constant, branch guard, or truncated arithmetic word.  The only discrepancy
found was in an external/static inventory estimate, not in the source: the
correct Type-II arithmetic increment is `1436` variables and `10052`
clauses.  Consequently the exact predicted Type-II total increment is
`33658` variables and `223745` clauses.

No production source was changed during this audit and no local SAT build or
solver was run.

## 1. Physical-cell semantics

Let `low[p]` mean that physical position `p` belongs to a rank-at-most-four
component.

* Type I: `low[0]=false`, because `A[0]` is the canonical rank-six entry;
  for `p>=1`, `low[p]=!rank5[p]`, because the suffix rank cap is five.
* Type II: `low[p]=!rank5[p]` for all positions, because every entry has rank
  at most five.

All entries are constrained nonzero by the base formula, so these signed
literals are exact, not merely necessary conditions.

For each coordinate, the pair contribution is defined by

```text
c <-> low[p] & low[p+1] & (A[p,b] | A[p+1,b]).
```

The five source clauses are exactly the prime directional implications:

```text
c -> low[p]
c -> low[p+1]
c -> (A[p,b] | A[p+1,b])
low[p] & low[p+1] & A[p,b]   -> c
low[p] & low[p+1] & A[p+1,b] -> c.
```

Likewise, the seven triple clauses define exactly

```text
c <-> low[p] & low[p+1] & low[p+2]
       & (A[p,b] | A[p+1,b] | A[p+2,b]).
```

Negating a signed `low` literal in the reverse clauses is correct CNF
literal negation.  There is no polarity error.

The allocated banks are:

| branch | pair starts | triple starts | contribution variables | definition clauses |
|---|---:|---:|---:|---:|
| Type I | `463` | `462` | `11*(463+462)=10175` | `5*5093+7*5082=61039` |
| Type II | `464` | `463` | `11*(464+463)=10197` | `5*5104+7*5093=61171` |

Omitting the cells starting at zero in Type I is exact: every such cell
contains the rank-six endpoint and therefore is not wholly inside the low
suffix.

The existing exact vector

```text
S=n1+2*n2+3*n3+4*n4
```

is precisely the singleton part of `R3`.  Exact Wallace/ripple counters sum
the pair and triple contribution bits, and two ordinary additions form

```text
R3 = S + pair_rank_sum + triple_rank_sum.
```

Every ripple addition retains its final carry.  The relevant exact widths
are

```text
pair_rank_sum       13 bits,
triple_rank_sum     13 bits,
short_non_singleton 14 bits,
S                   13 bits,
R3                  15 bits.
```

Thus none of the inequalities is interpreted modulo a power of two.

## 2. Exact Type-II `t1`

For Type II, an endpoint is a length-one low component exactly when it is
low and its sole neighbour is rank five.  An interior position is such a
component exactly when it is low and both neighbours are rank five.  The
source materializes all 465 indicators with bidirectional conjunctions:

```text
2 endpoint indicators * 3 clauses
+ 463 interior indicators * 4 clauses
= 1858 clauses.
```

An exact Wallace/ripple count, rather than a one-way OR, produces `t1`.
The structural filtration permits at most two low components and at least
`465-134` low positions, so this count is necessarily zero or one, as used
by the theorem.  Encoding the full count is nevertheless safer than relying
on that derived Boolean fact.

## 3. Exact `J` rows

Rank one has coefficient zero in

```text
J = sum_(r=1)^4 (r-1)*(nr-C(11,r))_+.
```

It is therefore enough to use the eight subsets of ranks two, three, and
four.  For a subset `R`, the source uses

```text
G_R = sum_(r in R) (r-1)*nr,
C_R = sum_(r in R) (r-1)*C(11,r),
```

with exact terms and constants

```text
(n2, 2*n3, 3*n4),
(55, 330, 990).
```

The identity

```text
J=max_R(G_R-C_R)
```

shows that imposing all eight comparisons is exactly equivalent to charging
`J`.  No positive-part subtraction gadget is required.

## 4. Signs, constants, and branch flags

Write

```text
y1=even-odd,
duplicate=delta,
two=1[s=2].
```

The implementation's comparisons are most transparently read in the
following orientations.

### Type I

For every subset `R`, it imposes

```text
4612 + 4*even + G_R
    <= R3 + 7*n5 + 4*odd + C_R.
```

Taking the maximum over `R` gives exactly

```text
R3 + 7*n5 - J - 4*y1 >= 4612.
```

Here `n5=z` in Type I.

### Type II: unified contaminated row

For every subset `R`, it imposes unconditionally

```text
4615 + 4*even + 4*duplicate + 5*t1 + G_R
    <= R3 + 7*n5 + 7*two + 4*odd + C_R.
```

This is exactly

```text
R3+7*n5+7*two >= 4615+J+4*y1+4*delta+5*t1.
```

The `duplicate_flag` is exact here.  Enabling `SHORT_CELL_R3` requires the
histogram module, which requires the core-incidence module.  That dependency
constructs `RankFiltrationTypeIIPlan` with duplicate exposure enabled, and
the plan defines

```text
duplicate <-> stability_tight & !two.
```

On the exhaustive corrected alternatives this is precisely the
`(delta,s)=(1,1)` case.

### Type II: two-component baseline

Under the exact `two` guard, the source also imposes

```text
4612 + t1 + G_R <= R3 + 7*n5 + C_R,
```

or

```text
R3+7*n5-J >= 4612+t1.
```

This second family is necessary for the corner `two=1,t1=0,y1=0`, where
the max-free contaminated row intentionally gives away four units.  The
conjunction of the baseline and contaminated rows equals

```text
R3+7*n5-J
 >= 4612+t1+4*max(y1-1+t1,0)
```

in the two-component branch.  In both one-component branches the unified
row dominates the corresponding baseline, so no additional guard is
needed.

All prefix-equality clauses in a guarded comparator contain `-guard`.
Consequently an inactive two-component comparison imposes no accidental
restriction through its auxiliary equality variables.

## 5. Exact predicted increments

The Wallace compressor and final ripple counts were mirrored operation by
operation.  The predicted **R3-only** increments are:

| category | Type-I variables | Type-I clauses | Type-II variables | Type-II clauses |
|---|---:|---:|---:|---:|
| physical contribution gates | 10175 | 61039 | 10197 | 61171 |
| `t1` indicator gates | 0 | 0 | 465 | 1858 |
| exact counters | 20320 | 142240 | 21288 | 149016 |
| unsigned arithmetic | 760 | 5320 | **1436** | **10052** |
| exact comparators | 136 | 824 | 272 | 1648 |
| **total increment** | **31391** | **209423** | **33658** | **223745** |

The Type-II counter category includes the exact 465-literal `t1` count.
The previously circulated `1440/10080` Type-II arithmetic estimate treated
`shift_left({two},1)` as a three-bit rather than a two-bit vector.  The
source is correct; the corrected arithmetic cost is four variables and 28
clauses smaller.

Added to the current histogram CNFs, the expected total DIMACS inventories
are:

```text
Type I:  3,711,394 variables / 20,442,802 clauses,
Type II: 3,730,852 variables / 20,543,701 clauses.
```

These totals should be checked against the RunPod build report and an
independent DIMACS token audit before any solver replacement.

## 6. Implementation checklist

1. Keep `K11_FOREST_SHORT_CELL_R3` opt-in and require
   `K11_FOREST_HISTOGRAM_SURPLUS`.
2. Expose `n1..n4`, `S`, `odd`, and `even` from the existing core plan by
   reference only; guard-off inventories must remain unchanged.
3. Use `low[0]=false` only in Type I, and `low[p]=!rank5[p]` everywhere
   else.
4. In Type I allocate only suffix pair/triple starts; in Type II allocate
   every physical start.
5. Keep all five/seven contribution clauses bidirectional, including with
   signed `low` literals.
6. Count pair and triple contributions exactly and retain every final carry.
7. Define every Type-II singleton-component flag bidirectionally and count
   the 465 flags exactly.
8. Use the eight `J` subset rows with terms `(n2,2*n3,3*n4)` and constants
   `(55,330,990)`.
9. Encode the Type-I row unguarded, the Type-II max-free row unguarded, and
   the Type-II baseline row under the exact `two` flag.
10. Ensure every guarded comparator clause, including equality-wire
    definitions, contains `-guard`.
11. Report category counters and compare them with the exact table above.
12. On RunPod, verify both the expected full inventories and that the largest
    DIMACS literal does not exceed the declared variable count.
13. Before replacing a live solver, retain the old branch coverage and check
    that the new CNF is generated from the frozen audited source hash.

## 7. RunPod build-only confirmation

The source was copied byte-for-byte to RunPod Rose and compiled there against
the already audited DIMACS streaming shim.  No compilation or SAT generation
was run on the user's workstation.

```text
source SHA-256:
f4b21d6c7b4ad8ba1a326b621980cda7dee2c491c491b9764ca8f52c061906fa

streaming shim SHA-256:
19391c64c7e2709eda4d6c984b6612134002a123af0a15c6f162c63bf989f4a0

RunPod streaming binary SHA-256:
90a263544bc01eac523323da6eb6ea4ddf47eaa8f787b31d1784290cb4087f24
```

Compilation with `-O3 -std=c++2a -Wall -Wextra -Wpedantic` emitted zero
warning bytes.  Both exhaustive branches were then streamed to `/dev/null`
under `K11_FOREST_BUILD_ONLY=1`; this exercised the complete clause stream
without allocating disk for a raw CNF.  The generator reported exactly:

```text
Type I:  3,711,394 variables / 20,442,802 clauses,
Type II: 3,730,852 variables / 20,543,701 clauses.
```

The internal category ledgers also matched the table in Section 5 exactly,
including the corrected Type-II arithmetic count `1436/10052`.  The cgroup
OOM-kill counter remained 35.  No live solver was stopped or added.  Raw CNF
generation was deliberately deferred because the stronger length-resolved
rank-vector package in `K11_SHORT_CELL_RANK_VECTOR_CUTS_20260724.md` can reuse
the same physical contribution wires at comparable cost.
