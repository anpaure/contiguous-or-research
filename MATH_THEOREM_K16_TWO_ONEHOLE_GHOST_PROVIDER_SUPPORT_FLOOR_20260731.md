# K16 two one-hole basins: ghost/provider support floor

Date: 2026-07-31  
Status: exact solver-free support theorem composed with frozen radius-two no-gos  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Scope

The two authenticated length-12873 words are

```text
scratch/k16_upper12874_best_delete.word
  SHA a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649

scratch/k16_vv_th495_deletep1_onehole_20260731.word
  SHA e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676.
```

Both cover every nonzero K16 mask except

```text
H = 0x2c6d,
```

and both first-deliver

```text
G = 0xc279
```

twice.  Every universal K16 word of length 12873 is ghost-free by the
architecture-free first-delivery inequality.  Hence a completion by cell
substitutions must both install `H` and destroy at least one inherited `G`
deadline group.

This note classifies the smallest physical supports for those two tasks.  It
does not launch a new SAT model; the final support floor is composed from the
already frozen exact radius-two results.

## 2. The two ghost cores

Apply the target-block automaton to `G`.  In both words there are exactly two
full `G`-compatible blocks:

```text
B_0 = [11726,11728],
B_1 = [12826,12828].                                  (2.1)
```

For each block, the exact witness core

```text
[ min_{a in G} last_B(a), max_{a in G} first_B(a) ]
```

is the whole three-cell block.  Therefore a one-cell substitution destroys
one inherited `G` group only if it edits one of exactly six sites

```text
C_G = {11726,11727,11728,12826,12827,12828}.          (2.2)
```

Conversely every site in (2.2) can destroy its block by receiving a value
not contained in `G`.  Thus (2.2) is an equality, not a heuristic candidate
list.

This recovers the six-position surgery theorem directly from compatible
blocks.  The unique-bit masks in the two basins differ at one cell, but the
physical cores coincide.

## 3. Route A: direct exchange

A direct exchange is one edit which both destroys one old `G` block and
supplies `H`.  At site `p`, the exact `H` provider interval is

```text
[H minus C_H(p), H],                                  (3.1)
```

where `C_H(p)` is the maximal two-sided `H`-compatible context.  Intersecting
(3.1) with the exact block-kill condition gives all direct exchanges.

For the collar594 basin there are 13 literal rows:

| site | provider low | exact values | debts after exchange |
|---:|---:|---:|---:|
| 11726 | `2c6d` | 1 | 16 |
| 11727 | `2c6d` | 1 | 15 |
| 11728 | `2c6d` | 1 | 15 |
| 12826 | `240d` | 8 | **11** |
| 12827 | `2c6d` | 1 | **11** |
| 12828 | `2c6d` | 1 | 13 |

The eight values at `p=12826` are exactly

```text
2c6d 2c4d 2c2d 2c0d 246d 244d 242d 240d.
```

For the V/V TH495 basin, `C_H(p)=0` at all six sites, so the only direct
value is `H` itself.  The six debt counts are

```text
16, 15, 15, 11, 11, 12.
```

Hence the exact singleton direct-support set is (2.2), but no direct row is
even close to universal: the sharp debt is eleven in either basin.  This is a
solver-free enumeration of 19 Boolean-interval rows, not a neighborhood SAT
claim.

## 4. Route B: ghost kill plus a separate provider

Suppose the edit that destroys `G` does not itself install `H`.  Then the
support must contain

```text
g in C_G
```

and a distinct provider site `p`.  Structurally every physical site is an
`H` provider, because assigning the literal value `H` creates the singleton
interval `[p,p]`.  Requiring the provider to lie outside the ghost core gives
exactly

```text
6 * (12873-6) = 77,202                              (4.1)
```

designated two-site structural supports.

The target-block context ranking gives a much smaller exact low-bit frontier.
In both words the minimum possible rank of the provider lower bound in (3.1)
is one, attained at the same 24 sites:

```text
0,2,4,556,2180,2685,2689,3528,3530,3532,3957,3959,
3961,4171,4485,4489,4497,4501,5464,5921,5923,5925,
6437,6440.                                           (4.2)
```

Thus the rank-minimum separate frontier has exactly `6*24=144` supports.
This 144-row set is an exact minimum-provider-bit subfamily, not an exhaustive
replacement for the 77,202 structural pairs.

The earlier six-position literal theorem sharpens the clean ghost side.  Only

```text
11726,11728,12826,12828                              (4.3)
```

admit a one-cell ghost kill which preserves every other middle label.
Position 12826 is uniquely strongest.  Sixteen normalized values there leave
exactly

```text
{0x2c6d,0xc679}.
```

The exact common-provider continuation then has only eight assignments, all
at site 6437, and every one replaces that pair by the same six debts

```text
2879,287d,a879,a87d,c879,e879.                       (4.4)
```

Equations (4.3)--(4.4) are the previously frozen H2/PAIR-EXPOSED result; they
are cited here, not recomputed by SAT.

## 5. Minimal-support theorem

> **Theorem.** In either fixed one-hole basin, any universal word obtained by
> arbitrary genuine nonzero cell substitutions must edit at least three
> physical cells and must meet `C_G` in (2.2).

**Proof.** Ghost-free equality forces destruction of at least one inherited
`G` deadline group, and the exact block core forces a support hit in `C_G`.
A support of size one is one of the direct rows in Section 3 or fails one of
the two required tasks; all direct rows retain at least eleven holes.  For a
support of size two, the final `H` witness either contains exactly one edited
site, giving a provider-first ordering, or contains both sites, giving the
all-joint branch.  Both branches are exhaustively closed for the collar594
word.  The independently composed V/V radius-two theorem closes the same
dichotomy there.  Therefore support size at least three is necessary.  QED.

The first still-live support shapes are consequently:

1. a direct exchange at one of the six sites, plus at least two repair sites;
2. a ghost kill at one of the six sites, a distinct `H` provider, and at
   least one repair site; or
3. a genuinely multi-site joint `H` witness, outside the two named provider
   forms.

This is a local theorem around two fixed words.  It does not prove a global
K16 lower bound and does not exclude three-edit completion.

## 6. Authentication

New target-block/direct atlas:

```text
scratch/audit_k16_two_onehole_ghost_provider_supports_20260731.cpp
  SHA-256 e613791e70a2cc639aa9869697df4d282950b8c226a1e99ecaa9c36147b2c068

scratch/k16_two_onehole_ghost_provider_supports_20260731.audit.json
  SHA-256 90878905fa44ef05ab3269ebfe594870b148cb70fa0dbbf12a02f27c5f87b43a

scratch/audit_k16_two_onehole_ghost_provider_supports_composed_20260731.py
  SHA-256 b461cf6718e111e120ce21bfd21990dccd46e62af2913efc40f1ce4f33d1ab76

scratch/k16_two_onehole_ghost_provider_supports_composed_20260731.audit.json
  SHA-256 a170b18f17847722bd56077a9a9c9cf50fe67ed14762c76a267b185f7e5f7666
  payload 21ecaae27ead61039d87c638b5e0ae1a28ed8a8c2a4a73c8e6ed0fe92d96787e.
```

Frozen radius-two inputs are authenticated inside the composed audit.  No
solver was launched for this theorem.

