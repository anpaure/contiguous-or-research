# Independent audit: Type-I prefix-chain selector compression

## Verdict

**PASS** for source SHA-256

```text
5a88fa91cccaf8e271927ead3509a21d55c6fc5b76fef43c8585569eefbce2aa
  k11_forest_sat.cpp
```

The current implementation is logically equivalent, under its checked
Type-I prerequisites, to the former `0 variables / 2,531 clauses` prefix
encoding.  Its adjacent-shadow inventory is exactly

```text
0 variables / 32 clauses / 74 solver.add calls.
```

The full Type-I plus rank-seven-width build is

```text
3,640,493 variables / 19,986,627 clauses.
```

This audit did not edit the solver and did not deploy it.

## 1. Semantic prerequisites

The guard requires both

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_RESIDUAL_COORD_LEX=1.
```

Type I indirectly requires rank-six branch one, and that branch requires the
canonical-rank-six and boundary-entry gates.  The exact `e=x0` row, branch
unit `e`, coordinate canonicalization, and endpoint localization together
force

```text
A[0]=63={0,1,2,3,4,5}.
```

Residual lex enforces

```text
column(6) <=lex column(7) <=lex ... <=lex column(10).
```

Singleton coverage makes every outside-coordinate first occurrence finite.
The comparator direction therefore gives

```text
f_10 <= f_9 <= f_8 <= f_7 <= f_6.
```

Consequently every prefix OR, including all intervals that contain position
zero, belongs to

```text
63, 1087, 1599, 1855, 1983, 2047.
```

The executable rejects the prefix guard without the two direct prerequisites.
The standard adjacent-shadow module is optional at the guard level because a
sound direct-target fallback exists.

## 2. Clauses made redundant by endpoint containment

For every direct target `S` not containing `63`, choose a low bit `b` absent
from `S`.  The base exact-OR encoding contains

```text
-Inside_S(0) OR -A[0][b].
```

Since `A[0][b]` is forced, the base formula already implies
`-Inside_S(0)`.  For an active crossed rank-seven target the corresponding
base clause is

```text
-active_S OR -Inside_S(0) OR -A[0][b],
```

which already implies the old guarded prefix clause.  Hence the compressed
module only needs to mention endpoint supersets that residual lex, rather
than an absent endpoint bit, excludes.

The exact endpoint-superset counts are

```text
rank 7:  C(5,1)-1 = 4,
rank 8:  C(5,2)-1 = 9,
rank 9:  C(5,3)-1 = 9,
rank 10: C(5,4)-1 = 4.
```

Thus the adjacent formula adds 22 direct units and four active crossed
clauses.  The source locates the canonical rank-seven mask `1087` by value;
its actual sorted column is 120.

## 3. Generic-slot equivalence

Each generic rank-seven slot has an exact rank-seven value.  Its positive
selector clause chooses at least one of 330 distinct seven-sets, and
`q_S -> S subseteq value`.  Two distinct selectors would force at least
eight value bits, contradicting exact rank seven.  Selection is therefore
exactly one.

Let `M=Inside(0)` and let `q_c` select canonical target `1087`.  Under this
exact-one invariant, the former 329 clauses

```text
-q_S OR -M                 (S != 1087)
```

are equivalent to the single clause

```text
-M OR q_c.
```

The source emits this once for each of six slots.  The resulting adjacent
inventory is

| family | clauses |
|---|---:|
| direct ranks 8--10 | 22 |
| active crossed rank 7 | 4 |
| six generic slots | 6 |
| **total** | **32** |

No variable allocation occurs in the block.  Its emitted literal stream is

```text
22*(1+terminator) + 4*(2+terminator) + 6*(2+terminator)
= 74 solver.add calls.
```

The old count reconstructs independently as

```text
(165+55+11-3) + (330-1) + 6*(330-1)
= 228 + 329 + 1974
= 2531 clauses.
```

Therefore the exact saving is 2,499 clauses.

## 4. Independent build-only regression

The source was freshly compiled against the independent CaDiCaL audit double
in `scratch/rank7_independent_hash_stub`, which checks declared-variable
bounds and fingerprints every emitted literal and terminator.

With the complete current Type-I/rank-seven portfolio and the prefix guard
absent:

```text
variables=3640493 clauses=19986595
INDEPENDENT_FNV64=5d3eb39bc836b76f
ADD_CALLS=88268630 DECLARED=3640493 MAXVAR=3640493
```

Setting the guard explicitly to zero produced a byte-identical log.  With
the guard enabled:

```text
variables=3640493 clauses=19986627
type1_prefix_chain_clauses=32
INDEPENDENT_FNV64=337b2301854ddb4b
ADD_CALLS=88268704 DECLARED=3640493 MAXVAR=3640493
```

The observed delta is exactly `0 variables / 32 clauses / 74 add calls`.
With adjacent shadows disabled, the rank-seven family remains direct and a
fresh build emitted exactly 26 prefix clauses, as required by

```text
4 + 9 + 9 + 4 = 26.
```

## 5. Scope

This is an exact propagation-preserving compression, not a SAT result.  It
does not change the represented Type-I solution set.  Any candidate still
requires independent exhaustive interval-OR verification, and an UNSAT
claim still requires a checked proof trace.
