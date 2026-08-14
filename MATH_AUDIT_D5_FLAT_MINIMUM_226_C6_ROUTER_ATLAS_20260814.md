# Hostile audit of the flat minimum D5 C6-router atlas

**Date:** 2026-08-14  
**Verdict:** **PASS as an algebraic factorization theorem.**  No cut-open
Johnson compiler is inferred.

Audited source:

`MATH_THEOREM_D5_FLAT_MINIMUM_226_C6_ROUTER_ATLAS_20260814.md`

H100 SHA-256:

```text
a3548ec6ce677866a642a0217399be3d20758da0fc4674bc80756215f318d2a8
```

## 1. Product convention

With rightmost factors acting first,

```text
(v1 v2 v3)(v3 v4 v5)...(v_(2r-1) v_(2r) v_(2r+1))
```

sends each `v_i` to `v_(i+1)` and the last point to `v_1`.  Thus the odd
adjacent-chain formula has the displayed orientation, not its inverse.

For two even cycles, the identities

```text
A = A0(a b),
B = B0(c d),
(a b)(c d) = (a c b)(a c d)
```

hold in the same convention.  Since the two source cycles are disjoint,
the two prefix chains commute past the other cycle's residual
transposition, and the concatenated factor list has action `AB`.

The physical scheduling sentence has been made literal: a traveller must
encounter factors in decreasing certificate index to implement a listed
product whose rightmost factor acts first.

## 2. Minimum and exposure

On the 477-point support, the target has 25 odd cycles and the identity has
477.  Starting at the target and multiplying by inverse three-cycles, one
factor can increase the odd-cycle count by at most two.  Hence at least

```text
(477-25)/2 = 226
```

factors are necessary.  The construction has exactly 226, so it is
globally minimum.

Odd-cycle chain junctions occur twice and all other odd-cycle tokens once.
For each of the eight even-cycle pairs, exactly the two penultimate prefix
endpoints occur once in a chain and twice in the residual two-factor
packet.  Therefore exactly 16 tokens have exposure three and no token has
larger exposure.  Since all 477 tokens occur and total port incidence is
`3*226=678`, the other two histogram entries are forced:

```text
x1+x2 = 461,
x1+2*x2 = 678-3*16 = 630,
(x1,x2) = (292,169).
```

This proves the exact histogram `1:292, 2:169, 3:16` symbolically.

## 3. Strengthened independent replay

The constructor was rerun unchanged on H100:

```text
scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.py
SHA-256 d7639744e5d8ce497a5b7d9cf71c99e769bb62e96326c7fc28014797b9441013

certificate SHA-256
2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc
```

The independent replay was strengthened to verify that source-cycle
indices partition the literal selection, every provenance factor range is
the canonical local chain/pair formula for its cited cycles, every local
product is correct, and the exact appearance histogram holds:

```text
scratch/audit_t2_suffix_d5_flat_minimum_c6_atlas_independent_20260814.py
SHA-256 67bbc59ade5abc2bf869f4daf888fe72809ddd72e35e49a8d05ddb00af89a40c

independent output SHA-256
a5f21662d08da89dddbf6e3d14225557d078e28aff8a3f9224aa9ab5056b4ff0
```

The replay returns `PASS`, including
`canonical_local_factors_verified=true`,
`source_cycles_partition_selection=true`, target equality on all 477
tokens, factor count 226, maximum exposure three, and the exact histogram.

## 4. Scope boundary

The theorem supplies 226 abstract three-cycle actions and a serial-site
upper bound of three.  It does not supply any of the 678 phase-common
context cuts, Johnson cross pairs, q1 refill, crossing q2 equality,
resource simplicity, residence collars, or the final `372 -> 1` traversal.
Those remain independent physical compilation obligations.
