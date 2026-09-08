# K16 exact-229 shifted-eight seam-token lemma and one-donor no-go

## 1. Setup

Start with the authenticated exact and arbitrary-upper-complete chronology
`exact_229.targets`.  The natural shifted-eight circulation uses positions

```text
3846 2328 3933 3522 2063 817 238 4653
```

whose original values are

```text
6b29 6939 293d 297c 293e 693a 69aa 69a9.
```

Cyclically assigning each position the next value installs `6b29` at 4653
and realizes the desired late Hall cells, but row 3845 misses bit `0200`.
This note asks which rank-eight value (V) at position (j=3846), with the
depth-three neighbours fixed, restores every affected middle row.

## 2. Exact seam-token lemma

Put

\[
 C={\tt 2b20},\qquad F={\tt 4099}.
\]

Here (C) has five bits and (F) has five disjoint bits.

> **Seam-token lemma.**  Under the fixed depth-three schedule, replacing only
> row 3846 by a rank-eight mask (V) preserves every middle replay equation
> if and only if
> \[
> V=C\mathbin\cup S,qquad S\subseteq F,qquad |S|=3.       \tag{2.1}
> \]

Consequently there are exactly (inom53=10) masks:

```text
2b39 2ba9 2bb1 2bb8 6b29
6b31 6b38 6ba1 6ba8 6bb0
```

In particular every feasible seam token contains `0200`.

### Proof

For a fixed coordinate (b), let (t_i(b)) be its target trace and put

\[
 e_p(b)=\bigwedge_{h=0}^{3}t_{p-h}(b),\qquad
 r_i(b)=\bigvee_{h=0}^{3}e_{i+h}(b).       \tag{2.2}
\]

Only (e_j,ldots,e_{j+3}), and hence only replay rows
(j-3,ldots,j+3), depend on (t_j(b)).  The exact coordinate table is:

| bit | trace (t_{j-6},\ldots,t_{j+6}) | allowed (t_j) |
|---:|:---:|:---:|
| 0 | `000000*111111` | 0 or 1 |
| 1 | `100000*000000` | 0 |
| 2 | `111110*000001` | 0 |
| 3 | `111111*000011` | 0 or 1 |
| 4 | `000000*111111` | 0 or 1 |
| 5 | `000111*110000` | 1 |
| 6 | `110000*000111` | 0 |
| 7 | `111111*001111` | 0 or 1 |
| 8 | `000011*111100` | 1 |
| 9 | `111001*111111` | 1 |
| 10 | `111100*000000` | 0 |
| 11 | `001111*100000` | 1 |
| 12 | `000000*011111` | 0 |
| 13 | `111111*111000` | 1 |
| 14 | `011111*111110` | 0 or 1 |
| 15 | `000000*000000` | 0 |

Thus the forced-one, forced-zero, and free masks are respectively

\[
 {	t 2b20},qquad {	t 9446},qquad {	t 4099}.           \tag{2.3}
\]

The five forced-one bits leave exactly three free bits to reach rank eight,
which proves (2.1).  Conversely (2.2) is coordinatewise, so every such choice
passes all seven affected replay rows.  Direct fixed-depth replay of all ten
masks confirms zero empty envelopes and capacity 32063.  This proves necessity
and sufficiency. (square)

### Literal-flat caveat

The lemma fixes the depth-three schedule.  If only row 3846 is changed,
`6ba8` equals row 3845 and `6b31` equals row 3847, creating an extra flat.
The other eight masks are literal-schedule-compatible as one-row changes.
A circulation that simultaneously moves the neighbouring donor can remove
that equality, so both masks must still be retained in the donor analysis.

## 3. Unique one-donor nine-token circulation

Every one of the ten feasible masks occurs exactly once in the authenticated
source deck, at

```text
2b39@437   2ba9@6263  2bb1@468   2bb8@2206
6b29@3846  6b31@3847  6b38@795   6ba1@4652
6ba8@3845  6bb0@681.
```

Fix all seven non-3846 assignments of the shifted-eight circulation.  For a
candidate (V\ne{	t 6b29}), the unique one-donor extension inserts its
unique occurrence immediately after 3846 in the position cycle.  Position
3846 receives (V), the donor position receives the displaced `6939`, and
position 4653 still receives `6b29`.  Deck multiplicity leaves no other
one-donor assignment under this convention.  The mask `6b29` has no distinct
donor occurrence.

Exact replay gives:

| donor | position | missing middle bits by row | upper holes |
|---|---:|---|---|
| `2b39` | 437 | `436:0200,437:4000,438:0200,439:0200` | `2b3d` |
| `2ba9` | 6263 | `6263:4010,6264:0200` | `2bad,6b39` |
| `2bb1` | 468 | `465:0200,466:0200,467:0280,468:4000,469:0080,470:0080,471:0080` | `2fb1,6b39` |
| `2bb8` | 2206 | `2203:0080,2204:0080,2205:0080,2206:4001` | `2bbc,2bf8,2bfc,6b39` |
| `6b29` | 3846 | no distinct donor | — |
| `6b31` | 3847 | `3845:0200,3846:0200,3847:0008` | none |
| `6b38` | 795 | `795:0001` | `6b78` |
| `6ba1` | 4652 | `4649:0200,4650:0200,4651:0200` | none |
| `6ba8` | 3845 | `3845:0011,3846:0080` | `6b39` |
| `6bb0` | 681 | `680:0080,681:0001` | `6b39` |

> **One-donor no-go.**  No one-donor nine-token extension of the fixed
> shifted-eight transport preserves exact middle replay.

All nine candidates retain capacity 32063 and have no zero envelope.  The
two upper-complete near misses are `6b31` and `6ba1`; both fail only by the
listed middle carriers.  Hall is therefore not reached.

This theorem does not close a reordered nine-token permutation, a second
donor, or a ten-token circulation.  It does show exactly what the next atom
must accomplish: retain a token from the ten-mask hypersimplex while repairing
the donor seam as well as the original `0200` seam.

## 4. Exact artifacts

```text
scratch/audit_k16_exact229_shifted8_seam_token_20260730.py
scratch/ad_k16_bad2_splitpair_exact_20260730/
  exact229_shifted8_seam_token.k.audit.json
```

The reproducer performs only coordinatewise enumeration of the 12,870
rank-eight masks and nine literal whole-word replays; it invokes no solver.
