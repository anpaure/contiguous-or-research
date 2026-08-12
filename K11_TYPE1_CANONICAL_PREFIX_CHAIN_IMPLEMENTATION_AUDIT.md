# Implementation audit: compressed Type-I canonical prefix-chain cut

## Verdict

**PASS.**  The optional source guard

```text
K11_FOREST_TYPE1_PREFIX_CHAIN=1
```

still implements the exact Type-I canonical-prefix consequence, but its
selector expansion has been reduced from

```text
0 variables / 2,531 clauses
```

to

```text
0 variables / 32 clauses.
```

The full current Type-I v6 build is now

```text
3,640,493 variables / 19,986,627 clauses.
```

The six-loss count/coupling does not require another circuit: after residual
lex, the only possible suffix losses are the six fixed masks

```text
63, 1087, 1599, 1855, 1983, 2047.
```

Thus the existing normalized formula already proves that the suffix covers
at least 2,041 targets.  The prefix guard exposes that semantic consequence
to propagation; it does not change the solution set.

## 1. Guard and prerequisites

The source reads `K11_FOREST_TYPE1_PREFIX_CHAIN` with the same nonempty,
nonzero convention as neighboring guards.  It rejects the cut unless both

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_RESIDUAL_COORD_LEX=1
```

are active.

These prerequisites are sufficient:

* Type I requires the exact branch-one modules, which force `A[0]=63`;
* residual lex sorts outside coordinate columns `6,...,10` and makes every
  prefix OR one of the six displayed chain masks;
* Type II and coordinate-named portal formulas cannot pass the guard.

The standard 32-clause portfolio also has adjacent shadows enabled.  If
adjacent shadows are absent, rank seven stays direct and the same source block
emits 26 unit clauses instead.

No subcube, containment-cap, named-cell, pin-localization, or rank-seven
width module is required for soundness.

## 2. Clauses already supplied by endpoint containment

If a fixed target `S` does not contain `63`, choose a low coordinate `b`
which is in `A[0]` but absent from `S`.

For a direct target, the base exact-OR encoding contains

```text
-Inside_S(0) OR -A[0][b].
```

Since branch one fixes `A[0][b]`, this already gives `-Inside_S(0)` by unit
propagation.

For a crossed rank-seven target, the base encoding contains

```text
-active_S OR -Inside_S(0) OR -A[0][b],
```

which already reduces to `-active_S OR -Inside_S(0)`.

It is therefore redundant to add prefix clauses for the 206 direct and 325
crossed target names which fail to contain `63`.  Only endpoint supersets
excluded specifically by residual lex need new clauses.

## 3. Exact generic-slot compression

Each generic rank-seven slot has an exact rank-seven `slot.value` and one
positive clause over its 330 target selectors `slot.q[column]`.  If two
distinct target selectors were true, `slot.value` would contain the union of
two distinct seven-sets, which has rank at least eight.  This contradicts the
exact rank-seven clauses.  Therefore every slot selects exactly one target.

Let `c` be the column of canonical target `1087`, let `M=slot.Inside(0)`, and
write `q_c=slot.q[c]`.  Under exact-one selection, the old 329 clauses

```text
-q_t OR -M                 (t != c)                    (3.1)
```

are equivalent to the one clause

```text
-M OR q_c.                                               (3.2)
```

If `M` is true, (3.1) kills every noncanonical selector and the positive
target clause forces `q_c`.  Conversely, if a noncanonical `q_t` is true,
exact-one selection makes `q_c` false, and (3.2) forces `M` false.

The source finds the canonical column by mask value and verifies that it
exists.  It does not rely on a hard-coded column number.

## 4. Exact clause inventory

### Direct ranks eight through ten

There are `C(5,r-6)` rank-`r` supersets of `63`.  Removing the one canonical
target in each rank gives

```text
(C(5,2)-1)+(C(5,3)-1)+(C(5,4)-1)
=9+9+4=22
```

unit clauses `-item.Inside(0)`.

### Crossed rank seven

Five rank-seven targets contain `63`; one is canonical.  The other four
receive

```text
-item.active OR -item.Inside(0).
```

### Generic rank-seven slots

Each of the six slots receives the single clause (3.2).

The total is

| component | variables | clauses |
|---|---:|---:|
| direct ranks 8--10 | 0 | 22 |
| crossed rank 7 | 0 | 4 |
| generic rank-7 slots | 0 | 6 |
| **total** | **0** | **32** |

No `next++`, `fresh`, or auxiliary allocation occurs in the emission block.
The solver-add increment is independently

```text
22*(1+terminator)+4*(2+terminator)+6*(2+terminator)=74.
```

## 5. Full build and guard-off identity

The source compiles against the independent build-only CaDiCaL double, which
checks every literal against the declared variable range and fingerprints the
complete clause stream.

With the full current Type-I v6 guards and the prefix option absent:

```text
variables=3640493 clauses=19986595
type1_prefix_chain=0 type1_prefix_chain_clauses=0
INDEPENDENT_FNV64=5d3eb39bc836b76f ADD_CALLS=88268630
```

Setting the option explicitly to zero gives the identical inventory,
fingerprint, and add-call count, proving guard-off identity.

With the prefix option enabled:

```text
variables=3640493 clauses=19986627
type1_prefix_chain=1 type1_prefix_chain_clauses=32
INDEPENDENT_FNV64=337b2301854ddb4b ADD_CALLS=88268704
```

Thus the observed increment is exactly `0 variables / 32 clauses / 74 add
calls`.

The non-adjacent fallback independently builds with

```text
type1_prefix_chain_clauses=26.
```

## 6. Checkers and frozen hashes

The static source checker

```text
python3 scratch/check_k11_type1_prefix_chain_implementation.py
```

verifies the guard, endpoint-superset filters, canonical column lookup,
compressed slot schema, absence of variable allocation, and the `22+4+6`
inventory.

The independent finite checker

```text
python3 scratch/check_k11_type1_prefix_chain_selector_compression.py
```

recomputes the canonical chain and target counts and exhausts all 660
`(Inside(0), exact-one target)` slot cases, proving equivalence of (3.1) and
(3.2).

At this audit revision:

```text
5a88fa91cccaf8e271927ead3509a21d55c6fc5b76fef43c8585569eefbce2aa
  k11_forest_sat.cpp
e6994672a01704138692d45c7bccb8cb90144beffd5e0c458e3d5168c32b6bd7
  scratch/check_k11_type1_prefix_chain_implementation.py
247505d9dcf647508fc03620b351fd5c1c685edce9bffc56d5f5a14bf99f647b
  scratch/check_k11_type1_prefix_chain_selector_compression.py
```

This remains a search reduction.  A SAT candidate requires independent
interval-OR verification; an UNSAT claim requires an archived and
independently checked proof trace.
