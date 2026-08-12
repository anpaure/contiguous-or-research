# Implementation of the k=11 rank-six boundary-entry cut

## 1. Verdict

**PASS.**  The independently audited array-level boundary theorem was added to
`k11_forest_sat.cpp` behind

```text
K11_FOREST_RANK6_BOUNDARY_ENTRY=1.
```

The edit started from source SHA-256

```text
8ba2b8203e8dbd699d4e45b87cccd828de5a6cb901d751652b4704f93551dccb
```

and produced

```text
1172c55d5ab21f829af8263cb5cc13e65dec0179c5a50159ed3c1b064ba21c81.
```

The guard adds no variables and has no dependency.  Its exact clause family
depends deliberately on whether the pre-existing coordinate-canonical guard
is enabled:

* standalone: 213,906 necessary clauses forbid every rank-six mask at each
  interior position `1,...,463`;
* together with the canonical gate: 464 additional clauses forbid canonical
  mask 63 at positions `1,...,464`, using reversal symmetry to choose the
  left endpoint.

No clause forces a rank-six entry to occur.  The stronger selected-profile
row `y2>=x1+82+14*x0` was not implemented.

## 2. Mathematical scope

### 2.1 Necessary localization

Any literal rank-six entry may be deliberately selected as that mask's
singleton witness.  The audited rank-six monotone band contains state `03`
because `x3>=93`.  A width-zero state comparable with `03` is only `00` or
`33`; uniqueness of the selected singleton forces it to schedule index zero
or 461, hence physical position zero or 464.

Therefore every valid length-465 array satisfies the coordinate-labelled
necessary condition

```text
no rank-six entry occurs at positions 1,...,463.       (2.1)
```

This is the standalone guard's exact scope.

### 2.2 Two boundary entries are impossible

Suppose both endpoint entries had rank six.  Every witness of rank at most
five avoids both endpoints, so deleting them leaves a contiguous word of
length 463 still covering all masks through rank five.

The 462 selected rank-five witnesses now have endpoint slack one.  Thus every
reduced-word interval of length at least two contains a selected rank-five
witness.  Every target of ranks one through four must consequently be
represented by a singleton interval.  But there are

```text
C(11,1)+C(11,2)+C(11,3)+C(11,4)=561
```

distinct such targets and only 463 singleton positions.  This is impossible.
Hence at most one literal rank-six entry exists in the whole array.

### 2.3 Reversal WLOG in the canonical interaction

The problem and all current hard constraints are invariant under physical
word reversal.  If the sole possible rank-six entry is at position 464,
reverse the array; it moves to position zero.  If no rank-six entry occurs,
reversal is unnecessary.

When `K11_FOREST_CANONICAL_RANK6_ENTRY=1` is also active, coordinate symmetry
has already fixed the possible mask to 63.  Combining the two independent
symmetries gives the existence-preserving normal form

```text
the only possible literal rank-six entry is A[0]=63.   (2.2)
```

This is a symmetry-WLOG interaction, not a necessary condition on every fixed
physical orientation.  The standalone boundary mode deliberately does not
silently use reversal and leaves both physical endpoints available.

## 3. Standalone clause family

With the canonical guard off, for every

```text
p in {1,...,463}
```

and every one of the 462 rank-six masks `S`, the implementation adds

```text
(OR_(b in S)     -A[p,b])
 OR (OR_(b not in S)  A[p,b]).
```

The 11-literal mismatch clause is false exactly when `A[p]=S`.  It is true
for every non-rank-six value.  The exact inventory is

```text
variables: 0,
clauses: 463*462=213906,
literal occurrences: 213906*11=2352966.
```

Positions zero and 464 receive no clause in this standalone mode.

## 4. Interaction with the canonical-mask gate

The existing canonical gate already forbids all 461 noncanonical rank-six
masks at all 465 positions.  Re-emitting those clauses internally would be a
duplicate.  Therefore, when both guards are active, the boundary loop keeps
only mask 63 and uses positions

```text
1,...,464.
```

The last position is included because the combined mode also uses the
reversal-WLOG orientation from (2.2).  Its incremental inventory is

```text
variables: 0,
clauses: 464,
literal occurrences: 464*11=5104.
```

The two clause families are disjoint in `(position,mask)` space:

```text
canonical gate: S!=63 at positions 0,...,464,
boundary interaction: S=63 at positions 1,...,464.
```

Thus there are exactly zero duplicate clauses between them.  Mask 63 at
position zero remains allowed but is not required.

## 5. Guard-off identity and exact inventories

The no-op CaDiCaL build of the pre-edit source reported, with all optional
guards off,

```text
variables=4892622 clauses=15524818.
```

The post-edit source with the new guard off reports exactly the same values
and additionally prints

```text
rank6_boundary_entry=0
rank6_boundary_entry_clauses=0.
```

With only the standalone boundary guard:

```text
variables=4892622 clauses=15738724
delta variables=0 clauses=213906.
```

With only the canonical guard:

```text
variables=4892622 clauses=15739183.
```

With canonical and boundary guards together:

```text
variables=4892622 clauses=15739647
boundary incremental variables=0 clauses=464.
```

With band, joint-band, canonical, singleton-pool, and boundary guards:

```text
variables=4899664 clauses=15778437
canonical clauses=214365
singleton-pool clauses=463
boundary clauses=464.
```

With every currently available structural guard and all three recent guards:

```text
variables=2924697 clauses=14732378.
```

The diagnostic counter at the actual clause-addition site reports exactly
213,906 in standalone mode and 464 in canonical-interaction mode.

## 6. Independent checker

The independent checker is

```text
scratch/verify_k11_rank6_boundary_entry_implementation.cpp
SHA-256 7d7f63f5deaaae29d933897ae71748c75ff24a6b46b2d74c51d388d4709e35cc.
```

It does not include the production source.  It:

1. exhausts every value at every position in a small rank-two analogue and
   proves that standalone mode excludes exactly middle-layer values at
   interior positions;
2. combines the small canonical and boundary gates and proves that the only
   admitted middle-layer value is the canonical mask at position zero;
3. independently enumerates all real rank-six masks and checks the exact
   clause and literal inventories for both modes; and
4. verifies that the canonical and interaction families have disjoint mask
   conditions, hence no duplicate clauses.

It compiles cleanly with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic \
    scratch/verify_k11_rank6_boundary_entry_implementation.cpp \
    -o verify_k11_rank6_boundary_entry_implementation
```

and prints

```text
small_boundary_gate=PASS
small_canonical_interaction=PASS
k11_boundary_plain_variables=0 clauses=213906 literals=2352966
k11_boundary_with_canonical_variables=0 clauses=464 literals=5104
duplicate_interaction_clauses=0
```

## 7. Compilation evidence

The production source compiles cleanly against the real remote CaDiCaL
library without generating or solving a formula.  The resulting executable
has SHA-256

```text
0b7b83caa56429caaf46444172b6edf5f42bf09b8bb9203261e1b107fcc72fa5.
```

No live search was started, and no SAT or UNSAT conclusion is claimed.

