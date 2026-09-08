# Hostile audit: exact q4 k17 two-pair exchange signature oracle

**Date:** 2026-08-14

**Verdict:** **PASS** as an algebraic/pruning theorem.  No current-pool or
streamed-oracle search verdict is part of the source.

## 1. Source

```text
MATH_REDUCTION_Q4_K17_EXACT_TWO_PAIR_EXCHANGE_DIRECTED_SIGNATURE_ORACLE_20260814.md
sha256 296b90db85ae7684464eee115b6242b5058bb74f68282742d1a97adfacdd3e72
```

## 2. Formula audit

For `Phi(ell)=sum(ell_x-1)^2`, adding one occurrence at load `ell` costs
`2ell-1`, and removing one costs `3-2ell`.  If two signed changes `d,e`
are applied together, the only omitted term from the two separate scores is
`2<d,e>`.  Expanding `d=1_N-1_P` and `e=1_M-1_Q` gives the four
intersection terms in source `(1.3)`.  Regrouping them gives exactly

```text
c_{P,Q}+h_{P,Q}(N)+h_{P,Q}(M)+2|N intersect M|.
```

The formula correctly counts row-set overlap with multiplicity while
requiring only the four configuration indices to obey selection
constraints.

## 3. Cut and algorithm audit

Because the final overlap term is nonnegative, `c+2m>=0` is a valid face
no-go.  If a candidate `N` belongs to a negative pair, replacing its mate's
score by `m` gives the strict necessary threshold `h(N)<-c-m`.  Therefore
the two-pass streamed filter is lossless once its first-pass minimum is
complete.  A fixed top-K bank has no such guarantee, and the source says so.

For one ten-row `N`, the subset query removes every bucket member containing
a row of `N-S`.  A surviving member intersects `N` only inside `S`.
Enumerating `S` by increasing cardinality therefore returns the exact
minimum intersection; the 1,024-test bound is correct.

Excluding selected incoming indices loses only states whose symmetric
difference from the incumbent has size zero or two.  At a certified
one-exchange local optimum none is a hidden negative genuine two-exchange.

## 4. Independent replay

```text
scratch/verify_q4_k17_exact_two_pair_exchange_signature_oracle_20260814.py
sha256 6ec8dd1381ecf6f447c6df70b807b27cece5f1b9e7b615ffdd6bb9cefc32eb06

scratch/verify_q4_k17_exact_two_pair_exchange_signature_oracle_20260814.h100.out
sha256 7c6e8bcaa91653e34173d73de034b6ead8ad1ef9dee57111bda6fe6ee66f3360
status PASS
```

The H100 replay verifies all 80 rowwise membership cases, 12,915 direct
synthetic two-exchanges with negative examples, every strict-threshold
retention, 7,182 bucket/subset queries, and fifteen nonvacuous dead faces.
It deliberately performs no q4 owner-pool search, avoiding duplication of
the Benders lane.
