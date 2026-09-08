# Independent implementation audit: `k=11` rank-six boundary entries

## Verdict

**PASS.**  The guarded implementation in `k11_forest_sat.cpp` at SHA-256

```text
1172c55d5ab21f829af8263cb5cc13e65dec0179c5a50159ed3c1b064ba21c81
```

matches the array-level theorem and its two intended modes:

```text
standalone:
    forbid all 462 rank-six masks at positions 1,...,463
    213,906 clauses, 0 variables

with K11_FOREST_CANONICAL_RANK6_ENTRY=1:
    additionally forbid only mask 63 at positions 1,...,464
    464 clauses, 0 variables.
```

The standalone clauses are coordinate-labelled necessary conditions and
leave both word endpoints available.  The smaller canonical interaction is a
satisfiability-preserving normal form that uses the independently valid word
reversal after the rank-six mask has been canonically named.  Neither mode
forces a rank-six occurrence.  The canonical and interaction clause families
are disjoint, so the 464-clause interaction contains no duplicate of a
pre-existing canonical clause.

The guard-off source has the exact pre-edit hard formula.  No SAT, UNSAT, or
`nu(11)=465` claim is made.

## 1. Exact source recovery and guard-off identity

The recorded implementation consisted of an initial patch and one correction
that extended the canonical interaction through position 464.  I reversed
the correction and then the main patch.  The result is

```text
scratch/k11_forest_sat_before_boundary_reconstructed.cpp
SHA-256 8ba2b8203e8dbd699d4e45b87cccd828de5a6cb901d751652b4704f93551dccb
```

which exactly matches the frozen pre-edit SHA in the implementation note.
The source diff contains only:

1. the environment boolean;
2. one diagnostic counter;
3. the guarded mismatch-clause loop;
4. diagnostic output.

There is no new variable allocation and no dependency check.  With the guard
false, the new loop does not call `add_vector`, so all prior hard clauses are
generated in the same order with the same variable numbers.

Both source snapshots compile warning-free at
`-O3 -std=c++20 -Wall -Wextra -Wpedantic` against the deterministic build-only
CaDiCaL test double.  Old/new guard-off comparisons give:

| profile | old variables/clauses | new variables/clauses |
|---|---:|---:|
| no optional guards | `4,892,622 / 15,524,818` | `4,892,622 / 15,524,818` |
| canonical guard | `4,892,622 / 15,739,183` | `4,892,622 / 15,739,183` |
| all previously available structural guards | `2,924,697 / 14,731,914` | `2,924,697 / 14,731,914` |

The only output difference is the new zero-valued diagnostic field.

## 2. Why interior rank-six literals are impossible

Take any literal rank-six occurrence `[p,p]` and deliberately select it as
the witness for its mask.  The unrestricted selected rank-six monotone band
has width profile satisfying

```text
x3>=93,
```

so it contains state `03`.  The only width-zero states comparable with `03`
are `00` and `33`; states `11` and `22` are incomparable.  The independently
proved `x0<=1` makes the selected singleton unique.

If it is state `00`, monotonicity and uniqueness force schedule slot zero,
whose physical interval is `[0,0]`.  If it is `33`, they force slot 461,
whose physical interval is `[464,464]`.  Therefore `p` is zero or 464.

This argument may be rerun after deliberately choosing any literal rank-six
occurrence, so it is an array-level statement, not merely a property of one
preferred witness schedule.  The coordinate-labelled necessary consequence
is exactly

```text
no rank-six entry at positions 1,...,463.
```

No fixed-row or connected-forest assumption enters the proof.

## 3. Why both endpoints cannot occur

If both endpoint entries had rank six, every witness for a mask of rank at
most five would avoid both.  Deleting the two endpoints leaves the contiguous
463-entry word `A[1],...,A[463]`, still covering all masks through rank five.

Choose one witness for each of the 462 rank-five masks in this interior word.
Equal-rank nonnesting gives 462 distinct left and right endpoints in 463
positions.  With slack one, the `i`th interval is contained in `[i,i+1]`.
Hence every physical interval of length at least two contains a selected
rank-five witness and has OR rank at least five.

All masks of ranks one through four would consequently have to occur as
single entries.  Their number is

```text
11+55+165+330=561,
```

but the interior has only 463 singleton positions.  This contradiction shows
that at most one boundary occurrence exists.  It also strengthens “one
distinct mask” to “one literal occurrence.”

The standalone implementation is deliberately weaker: it forbids only the
interior and does not orient or couple the two endpoints.  A weaker necessary
condition remains exact-search safe.

## 4. Independent coordinate and reversal symmetries

If the unique rank-six occurrence has mask `S`, a coordinate permutation
sends `S` to

```text
63={0,1,2,3,4,5}.
```

The pre-existing canonical guard implements this coordinate normal form at
all positions.  Word reversal does not change any entry mask.  If the sole
occurrence of 63 is at position 464, reversal moves it to zero; if it is
already at zero, no reversal is needed; if no rank-six occurrence exists,
neither operation is required.

Thus coordinate naming and physical orientation are independent choices and
may be used sequentially.  The combined normal form is

```text
either no rank-six literal occurs,
or the sole occurrence is A[0]=63.
```

### 4.1 Coordinate equivariance of the other hard clauses

Under a coordinate permutation, rename `A[p,b]` to `A[p,pi(b)]`, map each
complete target-layer block for mask `S` to that for `pi(S)`, and similarly
map all value/occurrence bits and central mask columns.  The remaining
clauses use only ranks, positions, interval widths, and endpoint relations.

In particular, direct targets and every compressed target family enumerate
complete ranks; exact-cardinality clauses enumerate all coordinate subsets;
the central, band, joint-band, adjacent-shadow, rank-three, endpoint-alignment,
forest, singleton-pool, and standalone-boundary constraints name no coordinate.
The input seed affects only solver phases.  Therefore the formula before the
canonical choice is coordinate-equivariant.

### 4.2 Reversal equivariance after the canonical choice

For the two central schedules, reversal maps

```text
physical position p -> 464-p,
schedule slot i      -> 461-i,
state (alpha,beta)   -> (3-beta,3-alpha).
```

The independent checker verifies for all ten states and all 462 slots that
the transformed state represents exactly the reversed physical interval.
The state map is an involution, preserves width, fixes `03`, and exchanges
`00` with `33`.  Hence `x3` and the width-zero indicator `e` are invariant.

The rank-six band chain maps to itself in reverse.  Of the three rank-five
chains in `JointBandCutPlan`, chain A maps to itself and chains B and C are
exchanged.  Thus the band and joint-band restrictions admit the reversed
schedule.  The remaining positional blocks transform as follows:

| block | reversal action |
|---|---|
| direct interval targets | exchange left/right thresholds and reverse occurrence positions |
| central target rows | reverse schedule slots and apply the state involution |
| adjacent rank-four/rank-seven shadows | reverse physical candidate intervals and exchange prefix/suffix roles |
| rank-three shadows | same physical-interval reversal |
| rank-six endpoint summaries | exchange begin/end summaries |
| endpoint alignment | exchange the equal left/right inequalities |
| central forest | exchange left and right edge colours |
| singleton-pool | preserves `e` and `x3` |
| canonical rank-six mask gate | applies at every position, hence is reversal invariant |
| zero-free clauses | positionwise invariant |

Exception slots can be carried to reversed intervals; their identities are
existential.  Every bound depends only on interval length.  Phases again do
not constrain the formula.  Therefore reversal remains available after the
coordinate-canonical guard is enabled.

The canonical-interaction boundary clauses intentionally break reversal by
selecting its left-oriented orbit representative.  That is the WLOG purpose
of this mode.

## 5. Standalone clause audit

With `canonical_rank_six_entry=false`, the source computes

```text
last_position=N-2=463
```

and loops inclusively over positions `1,...,463`.  At each of those 463
positions it loops over `central[1].masks`, previously checked to be the
complete 462-mask rank-six layer.  It skips no mask.

For forbidden mask `S`, the eleven literals are

```text
-A[p,b] if b is in S,
 A[p,b] if b is not in S.
```

All are false exactly when `A[p]=S`; any differing bit satisfies its literal.
The clause is true for every non-rank-six entry.  Position zero and position
464 receive no standalone boundary clause.

The independent checker evaluates the mismatch polarity for every rank-six
mask against every eleven-bit value.  It then checks every `(position,value)`
pair and confirms that standalone mode accepts exactly

```text
popcount(value)!=6 OR position in {0,464}.
```

The exact inventory is

```text
463*462 = 213,906 clauses
213,906*11 = 2,352,966 literal occurrences
0 variables.
```

## 6. Canonical interaction and duplicate audit

When `canonical_rank_six_entry=true`, the source computes

```text
last_position=N-1=464
```

and loops inclusively over positions `1,...,464`.  Inside the rank-six mask
loop it retains only `mask==63`.  Thus it emits exactly one clause at each of
464 positions.

The pre-existing canonical family is

```text
(p,S) with p=0,...,464 and S!=63.
```

The interaction family is

```text
(p,63) with p=1,...,464.
```

These sets are disjoint by mask, proving there are no duplicate clauses.
Their conjunction accepts a rank-six value only when it is 63 at position
zero.  It does not add a positive clause for 63, so the entire no-occurrence
branch remains admitted.

The exact incremental inventory is

```text
464 clauses
464*11 = 5,104 literal occurrences
0 variables.
```

## 7. Formula inventories

Build-only generation independently gives:

| mode | variables | clauses | boundary diagnostic |
|---|---:|---:|---:|
| baseline | 4,892,622 | 15,524,818 | 0 |
| standalone boundary | 4,892,622 | 15,738,724 | 213,906 |
| canonical only | 4,892,622 | 15,739,183 | 0 |
| canonical + boundary | 4,892,622 | 15,739,647 | 464 |
| band + joint + canonical + singleton-pool + boundary | 4,899,664 | 15,778,437 | 464 |
| every current structural guard | 2,924,697 | 14,732,378 | 464 |

The diagnostic is incremented at the actual `add_vector` site.  No new mode
changes the variable inventory.

## 8. Independent checker

The independent checker is

```text
scratch/audit_k11_rank6_boundary_entry_impl_independent.cpp
SHA-256 1f7e0c6c4b44c1ef46c1ea53fa0fc5b7a459b6cd052360b663c022a48d32e7ff
```

It is separate from
`scratch/verify_k11_rank6_boundary_entry_implementation.cpp` and does not
include the production solver.  It:

1. exhausts the mismatch polarity on the full eleven-bit domain;
2. constructs both real clause-key families exactly;
3. checks every `(position,value)` in standalone and combined modes;
4. explicitly verifies the no-rank-six branch;
5. proves the canonical/interaction key sets are disjoint;
6. checks standalone reversal invariance;
7. verifies the ten-state central reversal involution and all three joint
   chain transformations; and
8. derives every displayed inventory.

Compiled with `-O3 -std=c++20 -Wall -Wextra -Wpedantic`, it reports:

```text
standalone_positions=463 masks_per_position=462 clauses=213906 literals=2352966
canonical_interaction_positions=464 masks_per_position=1 clauses=464 literals=5104
canonical_boundary_duplicates=0
central_reversal_involution=PASS
independent_rank6_boundary_entry_implementation_audit=PASS
```

## 9. Scope

The implementation adds only literal-entry restrictions.  It deliberately
does not encode the stronger selected-profile inequality

```text
y2>=x1+82+14*x0.
```

The deterministic test double was used only for clause generation and
inventory comparison, never to infer satisfiability.  Future SAT candidates
still require both independent OR verifiers; future UNSAT claims require an
archived proof-producing CNF/proof pair and independent proof checking.
