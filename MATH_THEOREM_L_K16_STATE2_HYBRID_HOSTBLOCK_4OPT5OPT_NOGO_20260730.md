# K16 state2 hybrid host-block 4-opt/5-opt census

**Date:** 2026-07-30  
**Status:** exact finite-portfolio no-go; solver-free

## 1. Verdict

Let `Q` be the authenticated length-12,873 state2 target chronology

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464
```

and let the common cut set be

```text
U = {3278,5725,6388,12826}.
```

The exact census covers all 48 order/orientation states at `U` and all 384
states in each of the three single-host-block refinements

```text
U union {3280},   U union {3281},   U union {5727}.
```

It therefore quantifies exactly 1,200 representations, or 1,056 exact-distinct
target chronologies.  Every row is checked in the literal order

```text
G0
-> nonzero maximal-envelope reconstruction and exact middle replay
-> scalar lower capacity at least 26,332
-> exact ranks-9-through-16 interval coverage
-> complete ranks-1-through-7 individual-host atlas.
```

There is no endpoint/join prefilter.  The final result is

```text
representations:             1200
G0 pass:                     1200
maximal-envelope pass:         12
capacity pass:                 12
upper-complete pass:            8
complete lower-atlas audits:    8
zero-host-free:                 0.
```

The 12 carrier rows collapse to only three distinct chronologies: unchanged
`Q`, `u0`, and `u1`.  The unchanged row retains upper holes `0x4e79,0xc679`.
The eight upper-complete representations are only four embeddings each of
the two parents:

```text
u0: zero-host atlas {0x4c71};
u1: zero-host atlas {0x4879,0x4c39}.
```

Thus none of the three host-block refinements creates a new upper-complete
exact chronology, and no zero-host-free candidate exists in this portfolio.

## 2. Why these are the exact hybrid fibres

The cuts in `U` split the movable body into

```text
X = Q[3279..5725],
Y = Q[5726..6388],
Z = Q[6389..12826],
```

with the outer prefix and suffix fixed.  In this notation the two authenticated
upper-complete parents are

```text
u0 = A Z X Y D,   target SHA 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b;
u1 = A X Z Y D,   target SHA 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0.
```

Hence both lie in the complete common-cut fibre

```text
S_3 x {forward,reverse}^3,
```

of size `3! 2^3 = 48`.

Independent literal replay of the parent envelopes gives exactly one
complementary host for each facet missing from the other parent:

```text
u1 host of 0x4c71: chronology [3279..3281], base origins [3279,3280,3281];
u0 host of 0x4879: chronology [9717..9718], base origins [3279,3280];
u0 host of 0x4c39: chronology [12164..12165], base origins [5726,5727].
```

Their left boundaries are already cuts 3278 or 5725.  Isolating each whole
host block therefore adds exactly the right-boundary cut 3281, 3280, or 5727.
Each refinement has four movable blocks, so its complete fibre is

```text
S_4 x {forward,reverse}^4
```

of size `4! 2^4 = 384`.  This proves the portfolio cardinality
`48 + 3(384) = 1,200` without sampling or heuristic pruning.

## 3. Exact gates

For a G0 chronology `T`, its three flat rows force deadlines `d_i`.  Define

```text
E_p = intersection { T_i : i <= p <= i+d_i }.
```

Every realizing nonzero physical cell at `p` is a submask of `E_p`.
Consequently nonempty `E_p` and

```text
OR_{p=i}^{i+d_i} E_p = T_i
```

for every row are necessary.  They are also sufficient for the middle deck,
by assigning the maximal word `E`.  The scalar sum `sum_i d_i` is the exact
number of proper-prefix cells and must be at least

```text
sum_{r=1}^7 binom(16,r) = 26,332.
```

Upper completeness is replayed directly on every contiguous interval of the
target chronology.  No rank-nine endpoint shortcut is used.

For a proper-prefix cell `J`, put

```text
U_J = OR_{p in J} E_p
```

and let `M_J` contain a bit whenever the complete carrier of some required
middle incidence lies inside `J`.  A lower target `S` has an individual host
on `J` exactly when

```text
S subset U_J,
M_J subset S,
S intersect E_p is nonempty for every p in J.
```

Necessity is immediate.  Sufficiency assigns `E_p intersect S` on `J` and
the maximal values elsewhere.  Exhausting this criterion for all 26,332
lower masks is therefore an exact zero-host atlas, not a marginal proxy.

## 4. Independent replay and provenance

The C++ engine and a structurally separate Python checker both reconstruct
all 1,200 rows literally.  They agree on every global, exact-distinct, and
per-fibre gate counter, and on all eight atlas keys, capacities, flat starts,
and zero-host lists.  The independent comparison has zero mismatches.

The final H100 CPU run used only

```text
/home/amodo/or15/work/root_l_k16_state2_hybrid_4opt5opt_20260730_77dd098d
```

and was preceded by fail-closed SHA-256 manifests.  The production census
used 2.53 seconds wall time and 62,048 KiB maximum RSS; the independent
literal replay used 46.88 seconds and 94,864 KiB.  Both exited zero with no
swap.

Canonical artifacts are

```text
scratch/search_k16_resident_state2_hybrid_4opt5opt_20260730.cpp
  SHA-256 501fc355aa8f9d838e6aefabeec198ac6b9c6f82db061025abec9717ac18877a

scratch/search_k16_resident_state2_exact_2opt3opt_20260730.cpp
  SHA-256 8032758bd195657b1690e266b807af8b0518afcdda0b7caadf78f8c8fbcdd161

scratch/audit_k16_resident_state2_hybrid_4opt5opt_20260730.py
  SHA-256 407ba9c0f3a66880a2aad9768d9e7ace92a8ae13f3941cc2b28d990889fbaea2

scratch/k16_resident_state2_hybrid_4opt5opt_20260730/result.final.json
  SHA-256 9c5dc73b5ef9e8432ebfa80804620bc2f4bb3e9ecd471de95671b1b16249448c

scratch/k16_resident_state2_hybrid_4opt5opt_20260730/independent.final.audit.json
  SHA-256 3590a88eda53ea56d2eeef880494ae51bc0adb8451880ae79330bbb27b386814
  payload  e322065955bcf96e775e334914a4452f7652bbbdab2f00b77aca0b3a3ed85910
```

The independent 1,200-row ledger has SHA
`132327d142e4f00e6a45135057953ad789dd58268b2dd70c421b2eab126c3b4b`;
the exact eight-row atlas has SHA
`ed3855391677b711b1f80dfaeaa1241a918b869e801b7eb3901faac520b87868`.

## 5. Scope

This is exact only for the fixed outer prefix/suffix, the common-cut 4-opt
fibre, and the three single-host-block 5-opt refinements above, with whole
blocks freely permuted and reversed and the rank-eight multiset unchanged.
It does not cover an arbitrary fifth cut, multiple simultaneous extra cuts,
fragmented/interleaved blocks, target substitutions, moved terminal flats,
or a different state2 chronology.

A zero-host-free row would still be only ready for a simultaneous lower
compiler; it would not itself be a physical universal word.  Here there is
no such row.  The global K16 bracket remains unchanged:

```text
12873 <= nu(16) <= 12874.
```
