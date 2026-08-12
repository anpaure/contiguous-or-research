# Independent implementation audit: `k=11` endpoint alignment

## Verdict

**PASS.**  The guarded implementation in `k11_forest_sat.cpp` at SHA-256

```text
31cb278b5e4e5741d7d9c0ee8eee48f902a177536d44861b1aa408b8626707d7
```

implements exactly the four inequalities proved in
`K11_FOREST_ENDPOINT_ALIGNMENT_CUTS_AUDIT.md`:

```text
sum_p ZL324[p] >= 324
sum_p ZR324[p] >= 324
sum_p ZL24[p]  >= 24
sum_p ZR24[p]  >= 24
```

All sums have exactly 465 ordinary linear-position inputs.  The rank-five
endpoint summaries, all four counted conjunctions, the ripple counters, and
the comparator prefix states are bidirectional/exact.  The implementation
retains all eight required internal carries per increment, cannot overflow
nine bits, and uses the correct comparator polarity `constant <= count`.

The option has the required dependency on the exact rank-six endpoint
summaries supplied by `K11_FOREST_ADJACENT_SHADOWS=1`.  When the new guard is
off, variable allocation and the hard-clause stream are unchanged from the
pre-change source.  Enabling it adds exactly

```text
35,373 variables
126,635 clauses.
```

This audit certifies the encoding only.  It makes no SAT, UNSAT, or
`nu(11)=465` claim.

## 1. Exact pre-change reconstruction and guard behavior

I recovered the two recorded source patches that introduced endpoint
alignment, reversed them in reverse application order, and obtained

```text
scratch/k11_forest_sat_before_endpoint_reconstructed.cpp
SHA-256 8e0c04ae927ecff09b1ffbbeab5f8d719963788151d317cab05b78613e47fd8d
```

This exactly matches the pre-change SHA published in the implementation
note.  A direct diff against the audited source contains only:

1. the `EndpointAlignmentCutPlan` definition;
2. environment parsing and the adjacent-shadow dependency check;
3. guarded plan allocation and guarded clause insertion;
4. diagnostics.

In particular, when the option is false, `next` is not advanced and no plan
clause is passed to the solver.  The additional `endpoint_alignment_cuts=0`
text is diagnostic only.

Both snapshots were independently syntax-compiled at `-O3 -std=c++20`
against the clause-counting no-op CaDiCaL test double.  Three guard-off
profiles gave identical formula inventories:

| profile | old variables/clauses | new variables/clauses |
|---|---:|---:|
| no optional cuts | `4,892,622 / 15,524,818` | `4,892,622 / 15,524,818` |
| adjacent shadows only | `3,148,302 / 14,546,194` | `3,148,302 / 14,546,194` |
| adjacent + band + joint + rank-three | `2,889,324 / 14,390,451` | `2,889,324 / 14,390,451` |

Because the exact source diff has no unguarded hard-formula change, this is
also a source-level identity check rather than only equality of two aggregate
counts.

Requesting endpoint alignment without adjacent shadows exits with status 2
and prints exactly

```text
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS requires K11_FOREST_ADJACENT_SHADOWS
```

The audited source compiles cleanly with
`-Wall -Wextra -Wpedantic` against the test double.

## 2. Rank-five support indexing and boundaries

The implementation enumerates every one of the 462 rank-five schedule slots
and all ten monotone-band states

```text
00 01 02 03 11 12 13 22 23 33.
```

For slot `i` and state `(alpha,beta)`, it uses the physical endpoints

```text
left  = i + alpha
right = i + beta.
```

As `0<=i<=461` and `0<=alpha<=beta<=3`, every support index is in
`0,...,464`.  There is no wraparound, sentinel, or cyclic endpoint.  The
support filters are exactly:

```text
L5pos/R5pos : beta-alpha is 1 or 2
L52/R52     : beta-alpha is 2.
```

Thus width-zero states are excluded, the forbidden rank-five width-three
state `03` is excluded, and all five width-one/two states and both width-two
states are included.

Independent enumeration gives:

| summary family | support occurrences | maximum support at one position |
|---|---:|---:|
| `L5pos` | 2,310 | 5 |
| `R5pos` | 2,310 | 5 |
| `L52` | 924 | 2 |
| `R52` | 924 | 2 |

The asymmetric linear boundaries were checked explicitly.  For example,

```text
L5pos supports at p=0,1,461,462,463,464: 2,4,5,3,1,0
R5pos supports at p=0,1,2,462,463,464:   0,1,3,5,4,2
L52 supports at p=0,1,461,462,463,464:   1,2,2,1,0,0
R52 supports at p=0,1,2,463,464:         0,0,1,2,1.
```

These checks catch both an off-by-one at position 464 and an accidental
cyclic interpretation.

## 3. Exact summaries and conjunctions

For every rank-five summary `V`, the source emits

```text
support literal s -> V                 for every s
V -> OR(all support literals).
```

When the support is empty, the reverse clause is the negative unit `-V`.
Exhaustion over every actually occurring support size `0,...,5` confirms that
the projected CNF is exactly `V <-> OR(support)`.

The reused rank-six arrays are allocated only by the adjacent-shadow block.
That block defines both directions:

```text
selected rank-six state -> B6[p,d] or E6[p,d]
B6[p,d] or E6[p,d] -> OR(all matching selected states).
```

The endpoint plan receives `rank_six_by_left` and `rank_six_by_right` in the
correct order.  Its four predicates use the intended arrays and widths:

```text
ZL324[p] <-> L5pos[p] AND (B6[p,2] OR B6[p,3])
ZR324[p] <-> R5pos[p] AND (E6[p,2] OR E6[p,3])
ZL24[p]  <-> L52[p]   AND B6[p,3]
ZR24[p]  <-> R52[p]   AND E6[p,3].
```

The four-clause and three-clause encodings were exhaustively checked for all
Boolean assignments.  In particular, their reverse implications prevent a
real alignment from being hidden from a lower-bound counter.

## 4. Exact 465-step counters

Each of the four predicate arrays has C++ type `array<int,N>` with `N=465`,
and `exact_count` iterates once over every element.  Each step allocates:

```text
9 exact XOR output bits
8 exact AND carries
```

and emits

```text
9*4 + 8*3 = 60 clauses.
```

The old nine bits begin at the false literal `-one`; hence the initial count
is zero.  Carries out of bits zero through seven are retained and passed to
the next bit.  There is intentionally no variable for carry out of bit eight.
This is exact rather than modular here: every prefix has at most 465 true
inputs and

```text
465 < 512 = 2^9.
```

An independent semantic simulation processed all 465 stages for each
possible final Hamming weight `0,...,465`.  It recovered the exact weight in
all cases and confirmed that the omitted high carry is never one.

## 5. Comparator polarity and thresholds

The source calls

```text
add_leq(constant_bits(324), count)
add_leq(constant_bits(24),  count),
```

so the enforced relations are `324<=count` and `24<=count`, not upper bounds
or equalities.  Both arguments are extended to nine bits.  At every bit the
clause

```text
-equal_above OR -x_bit OR y_bit
```

forbids the first most-significant difference `x=1,y=0`.  The five clauses
for `next_equal` define, in both directions,

```text
next_equal <-> equal_above AND (x_bit == y_bit).
```

The independent checker exhausts all `512*512` pairs and accepts exactly
`x<=y`.  It separately checks both threshold decisions for every attainable
count `0,...,465`.

## 6. Independent inventory

The count was reconstructed from the source loops:

| block | variables | clauses |
|---|---:|---:|
| true constant | 1 | 1 |
| four rank-five OR summaries | 1,860 | `6,468+1,860=8,328` |
| four alignment predicates | 1,860 | `2*465*4+2*465*3=6,510` |
| four counters | `4*465*17=31,620` | `4*465*60=111,600` |
| four comparators | `4*8=32` | `4*(9+8*5)=196` |
| **total** | **35,373** | **126,635** |

With adjacent shadows alone this reproduces

```text
variables=3183675 clauses=14672829
```

from the guard-off baseline

```text
variables=3148302 clauses=14546194.
```

With adjacent, band, joint-band, and rank-three cuts simultaneously enabled,
the independent build gives

```text
guard off: variables=2889324 clauses=14390451
guard on:  variables=2924697 clauses=14517086,
```

again the exact same delta.  This also checks integration and allocation when
all currently deployed structural plans coexist.

## 7. Independent checker

The new checker is

```text
scratch/audit_k11_endpoint_alignment_impl_independent.cpp
SHA-256 f1dacce1042971fbb5cec86cbc9bfd132f35649acaa5199d8fec87975c73db51
```

It was written independently of
`scratch/verify_k11_endpoint_alignment_implementation.cpp`.  It enumerates
the physical support geometry, exhausts every local truth table, executes all
attainable 465-step counter weights, exhausts the complete nine-bit comparator
domain, and derives the inventory from the loop dimensions.  Compiled with
`-O3 -std=c++20 -Wall -Wextra -Wpedantic`, it reports:

```text
support_literals=6468 support_maxima=5,5,2,2
counter_inputs=465 retained_carries_per_step=8 counter_stage_variables=17 counter_stage_clauses=60
endpoint_alignment_delta_variables=35373 endpoint_alignment_delta_clauses=126635
independent_endpoint_alignment_implementation_audit=PASS
```

## 8. Scope

The check used a no-op CaDiCaL test double only for deterministic formula
generation and inventory comparison; it was not used to infer satisfiability.
The mathematical validity and global-WLOG status of the four inequalities
remain supplied by the separate mathematical audit.  A future SAT model must
still be checked by the independent OR verifiers, and a future UNSAT result
still requires a proof-producing solver plus an independently verified proof.
