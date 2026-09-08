# Guarded implementation of the `k=11` endpoint-alignment cuts

## Status

The four cuts audited in `K11_FOREST_ENDPOINT_ALIGNMENT_CUTS_AUDIT.md` are
implemented in `k11_forest_sat.cpp` behind

```text
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
```

The option is rejected unless

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

is also set, because the implementation deliberately reuses that option's
exact bidirectional rank-six `B/E` endpoint summaries.  No solver search was
run as part of this implementation check.

The source before this change had SHA-256

```text
8e0c04ae927ecff09b1ffbbeab5f8d719963788151d317cab05b78613e47fd8d
```

The implemented source has SHA-256

```text
31cb278b5e4e5741d7d9c0ee8eee48f902a177536d44861b1aa408b8626707d7
```

## 1. Exact auxiliary definitions

For each physical position `p=0,...,464`, the new plan defines four rank-five
summaries as bidirectional ORs of existing exact schedule states:

```text
L5pos[p] iff a width-1/2 rank-five witness starts at p,
R5pos[p] iff a width-1/2 rank-five witness ends   at p,
L52[p]   iff a width-2   rank-five witness starts at p,
R52[p]   iff a width-2   rank-five witness ends   at p.
```

For every support literal `s`, the implementation emits `s -> summary`, plus
one reverse clause `summary -> OR(all supports)`.  Empty support lists produce
a negative unit clause.  Thus a summary cannot guess an endpoint absent from
the schedule.

It then defines, in both directions,

```text
ZL324[p] iff L5pos[p] AND (B6[p,2] OR B6[p,3]),
ZR324[p] iff R5pos[p] AND (E6[p,2] OR E6[p,3]),
ZL24[p]  iff L52[p]   AND B6[p,3],
ZR24[p]  iff R52[p]   AND E6[p,3].
```

The four counters enforce

```text
sum ZL324 >= 324,
sum ZR324 >= 324,
sum ZL24  >= 24,
sum ZR24  >= 24.
```

## 2. Exact counters

Each counter processes all 465 input literals.  At each step it retains nine
output bits and eight internal ripple carries.  Every output bit is an exact
two-input XOR and every carry is an exact AND.  The high carry after bit eight
is unnecessary because

\[
465<2^9.
\]

The final nine bits are compared against 324 or 24 using the same exact
most-significant-prefix comparator pattern as the audited band plans.  All
prefix-equality auxiliaries are defined in both directions.

## 3. Exact inventory

| block | variables | clauses |
|---|---:|---:|
| true constant | 1 | 1 |
| four rank-five endpoint summaries | 1,860 | 8,328 |
| four alignment predicates | 1,860 | 6,510 |
| four 465-step nine-bit counters | 31,620 | 111,600 |
| four unsigned comparators | 32 | 196 |
| **total delta** | **35,373** | **126,635** |

The summary clause count consists of 6,468 state-to-summary implications and
1,860 reverse disjunctions.  Each counter step uses 17 variables and 60
clauses.

With adjacent shadows enabled and every other optional cut disabled, the
published guard-off baseline is unchanged:

```text
variables=3148302 clauses=14546194
```

Enabling endpoint alignment gives exactly:

```text
variables=3183675 clauses=14672829
endpoint_alignment_cut_variables=35373
endpoint_alignment_cut_clauses=126635
```

The difference is exactly the table above.

## 4. Guard behavior and diagnostics

With endpoint alignment requested without adjacent shadows, the program exits
with status 2 and prints

```text
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS requires K11_FOREST_ADJACENT_SHADOWS
```

The normal diagnostic line now always reports

```text
endpoint_alignment_cuts=0|1
```

and, when enabled, additionally reports the plan's exact variable and clause
counts.  When disabled, no plan object, variables, clauses, or schedule
restriction is created.  The guard-off adjacent-shadow inventory exactly
matches the previously audited inventory above.

## 5. Lightweight checks

The local machine did not have a CaDiCaL development header/library.  The
production source was therefore syntax-compiled at `-O3 -std=c++20` against
the no-op test double

```text
scratch/cadical_stub/cadical.hpp
```

The test double stores no clauses and cannot return SAT or UNSAT.  It was used
only to execute deterministic clause generation in build-only mode, yielding
the exact inventories in Section 3.  No search was launched.

The independent checker

```text
scratch/verify_k11_endpoint_alignment_implementation.cpp
```

exhaustively checks the local CNF truth tables for OR summaries, both
alignment predicates, XOR, AND, prefix equality, and every pair of nine-bit
integers in the comparator.  It also reconstructs the exact inventory and
tests both threshold decisions at all possible counts `0,...,465`.  Its output
is

```text
summary_forward_clauses=6468 summary_reverse_clauses=1860
endpoint_alignment_variables=35373 endpoint_alignment_clauses=126635
adjacent_plus_endpoint_variables=3183675 adjacent_plus_endpoint_clauses=14672829
k11_endpoint_alignment_implementation=PASS
```

SHA-256 values:

```text
f9ff56c2c3837858181b1d10e3f8d7e7f443a1726d44c5b3c7005766d5a69a4c  scratch/verify_k11_endpoint_alignment_implementation.cpp
161fbffb904267432228a97bb35b21e2dd7acb74f35d9c413791b8750b3feb95  scratch/cadical_stub/cadical.hpp
```

## 6. Proof status

The implementation adds only the necessary inequalities proved in the
independent mathematical audit.  It does not prove `SAT`, `UNSAT`, or
`nu(11)=465`.  Any future SAT model still requires both OR verifiers; any
future UNSAT result still requires an archived production CNF/proof pair and
independent proof checking with a real proof-producing solver.
