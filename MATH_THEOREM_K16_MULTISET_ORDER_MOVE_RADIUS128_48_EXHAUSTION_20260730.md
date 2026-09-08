# Exact K16 multiset-order move exhaustion through reversal 128 and rotation 48

## Move family

For a fixed length-12874 word `w`, the audit exhausts:

1. every contiguous reversal `w[l:r] -> reverse(w[l:r])` with
   `2 <= r-l <= 128`; and
2. every adjacent-block transposition
   `XY -> YX` on a contiguous span of length at most 48, for every nontrivial
   split of that span.

These moves preserve the multiset of cells and hence preserve all length-one
witnesses.  The verifier uses an exact local interval ledger.  Intervals wholly
outside the changed span are unchanged; intervals containing the whole span
are unchanged because union is commutative.  It exactly subtracts and re-adds
all internal, left-boundary, and right-boundary interval OR multiplicities.

The driver is

```
scratch/search_k16_order_moves_exact_20260730.cpp
```

Each named input has exactly 16,100,149 nontrivial moves in this family.

## Exhaustive result

| source basin | baseline holes | moves installing at least one source hole | best holes | sole-hole labels reached |
|---|---:|---:|---:|---|
| `k16_append0200_12874_onehole.word` | 1 | 3,644 | 1 | `0x287d` only |
| `k16_append0200_rex_hole10365_e23.word` | 1 | 3,644 | 1 | `0x287d` only |
| `k16_fivephase_portal_v2_hole10365.word` | 1 | 3,647 | 1 | `0x287d` only |
| `k16_fivephase_rex_hole20067.word` | 1 | 3,940 | 1 | `0x4e63` only |
| `k16_delete12875_p0_partial.word` | 2 | 5,613 | 2 | none |
| `k16_delete12875_p1_partial.word` | 2 | 5,952 | 2 | none |
| `k16_delete12875_p6435_partial.word` | 2 | 4,619 | 2 | none |
| `k16_delete12875_p12873_partial.word` | 2 | 4,797 | 2 | none |

In total, 128,801,192 moves were replayed exactly.  Of these, 35,856 install
at least one currently missing mask, but every such gain is offset by enough
last-witness losses to keep the hole count at or above its baseline.  No new
sole-hole phase label is reached.

The machine-readable audits are

```
scratch/k16_*order.audit.json
```

## Scoped theorem

For each of the eight authenticated words above, no contiguous reversal of
length at most 128 and no adjacent-block transposition of total span at most 48
strictly decreases its number of uncovered masks.  In the four one-hole words,
this family also reaches no different one-hole label.

This is not a statement about longer order moves, two disjoint simultaneous
order moves, substitutions, or coordinate-stabilizer crossovers.  It does show
that preserving the cell multiset is not by itself enough: a successful order
lane must be genuinely longer-range or compound.

