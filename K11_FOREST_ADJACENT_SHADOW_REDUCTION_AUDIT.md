# Independent-style audit of the guarded adjacent-shadow forest reduction

## Verdict

I audited the guarded branch of `k11_forest_sat.cpp` against the original
length-465 nonzero problem, rather than merely checking that it matches the
design note.  The guarded formula is sound and complete.  I found no hidden
choice of the six exceptional targets, no fixed-row assumption, and no use of
intersection/union masks without a physical interval witness.

The most important audit point is that the two directions are encoded
differently for a reason:

* a crossed rank-four interval is the **inner positional intersection** of two
  rank-five intervals, so the program materializes its physical OR explicitly;
* a crossed rank-seven interval is their dual **outer hull**.  The program
  proves its positive bits using two contained rank-six intervals and proves
  its negative bits position by position.

Merely asserting a set intersection or union of central values would not have
been complete in the presence of positional gaps.  The implementation does
not make that mistake.

## 1. Scope audit

The environment flag is read before variable allocation.  When it is false,
ranks four and seven remain in `direct` and no shadow variable or clause block
is allocated.  A stubbed build-only reconstruction reproduces the frozen
inventory exactly:

```text
variables=4892622 clauses=15524818 direct_targets=1123
```

When the flag is true, only ranks four and seven are removed from `direct`.
All array variables, both central monotone-band schedules, central target
permutations, forest propagation clauses, direct witnesses in the other seven
ranks, proof tracing, DIMACS writing, and model extraction remain unchanged.

## 2. Endpoint theorem audit

For ranks four and five, the selected left endpoint sets have sizes 330 and
462 in a universe of 465, hence at least 327 common endpoints.  The same is
true on the right.  Intersecting the two sets of good rank-four masks leaves
at least 324.  The rank-six/rank-seven calculation is identical.  Therefore
six generic slots per replaced rank are sufficient for every possible array
and every possible choice of its already-selected central witnesses.

At a common endpoint, nesting direction is forced by rank.  At a two-sided
rank-four flag the two rank-five masks are distinct: if their selected masks
were equal, the central permutation would assign one mask two different
selected intervals.  Their physical intervals properly extend the rank-four
interval on opposite sides.  Since rank-five length is at most three, the
inner interval length is at most two.

At a two-sided rank-seven flag, the selected rank-six intervals are proper
prefix and suffix intervals of the rank-seven witness.  Their masks are
distinct six-subsets of the seven-set target and therefore have full union.
No assumption about their overlap is needed.

## 3. Generic exception-slot audit

For every slot, the `L`, `R`, and `Inside` clauses select one nonempty interval
within the safe bound.  For each coordinate, the `H` variables and three
implications per position enforce

\[
 V_b=\bigvee_{p\in J}A_{p,b}.
\]

The two subset-clause families enforce exact rank.  A target flag implies all
bits of a same-rank target, hence fixes `V` exactly.  Two distinct target flags
cannot coexist because their union has larger rank.  The positive target
clause thus makes every generic slot select exactly one target without a
quadratic at-most-one encoding.

Six slots can cover at most six distinct targets.  They may repeat a target,
which is necessary to represent solutions having fewer than six exceptions
without adding enable bits.  Repetition cannot create a false witness.

## 4. Rank-four clause audit

There are exactly 929 one- or two-position intervals.  Their eleven value
bits are equivalent to the corresponding physical OR.  `at_most_four` guards
all 462 five-subset clauses.  A target flag implies this guard and the four
target bits, so the interval OR equals the target; outside-bit clauses are not
needed.

The two endpoint clauses attached to a target flag contain every central
rank-five state whose interval is respectively a proper right extension at
the same left endpoint or a proper left extension at the same right endpoint.
An empty list becomes the unit clause `-q`, as required at impossible boundary
geometries.  Because central endpoints are distinct, satisfying both lists
selects the required two-sided flag.

Each of 330 target coverage clauses contains all 929 physical flags plus the
six corresponding exception flags.  Therefore no target is omitted.

## 5. Rank-seven clause audit

For each endpoint and each length zero through three, the summary variable has
both directions:

```text
central state -> summary,
summary -> OR(all corresponding central states).
```

Thus it cannot invent a prefix or suffix.  The exact-start antecedent is
`L[l] AND NOT L[l-1]`; its CNF negation is implemented with `-L[l]` and
`+L[l-1]`.  The exact-end antecedent is dual.  Boundary cases omit the
nonexistent threshold literal.

For a prefix `[l,l+d]`, the clause requires `R[l+d+1]`, which is exactly
`selected_right >= l+d+1`.  If the index is outside the array the clause
correctly forbids that state.  For a suffix `[r-d,r]`, requiring
`L[r-d-1]` is exactly `selected_left <= r-d-1`.  Hence both selected rank-six
intervals are proper and physically contained in the active rank-seven
interval.

Only absent target bits receive direct array clauses.  This is sufficient:
the two contained central masks have cardinality six and no outside bit; they
are distinct because the central row is a permutation and their endpoint
pairs differ.  Their union is therefore the seven-set target, supplying all
positive bits inside the active interval.

## 6. Inventory and regression audit

`scratch/verify_k11_forest_adjacent.cpp` derives independently:

```text
direct variables                 1,832,565
generic exception clauses          246,246
rank-four shadow clauses          2,601,060
endpoint summary clauses             12,960
rank-seven shadow clauses         3,024,780
full variables                    3,148,302
full clauses                     14,546,194
```

It also exhausts all 6,930 unordered pairs of distinct six-subsets inside the
330 seven-sets and verifies their union identity.  A GCC 15.2 C++20/O3 run
prints:

```text
PASS k11 adjacent-shadow reduction
rank4_candidates=929 rank4_target_flags=306570
rank7_pair_types=6930 rank7_endpoint_comparisons=1227600
variables=3148302 clauses=14546194
```

A separate build-only execution of the actual generator against a no-op
CaDiCaL interface prints the same guarded inventory.  This checks C++ syntax,
variable allocation, and every generator loop without performing a local SAT
search.

## 7. Remaining operational requirement

The option has been syntax- and count-tested locally, but any promoted SAT or
UNSAT result still requires the existing remote real-CaDiCaL workflow.  A SAT
array must pass both independent OR verifiers.  An UNSAT claim requires the
archived DIMACS/proof pair and independent proof checking.  This is unchanged
from the parent forest formula and is not a logical gap in the reduction.
