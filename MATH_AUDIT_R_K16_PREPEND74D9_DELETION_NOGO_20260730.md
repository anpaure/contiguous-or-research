# Exact deletion audit for the 74d9 K16 word and prepend-delete no-go

## Verdict

Let

\[
T=\texttt{scratch/k16\_12874\_twohole\_partial.word}
\]

be the length-12,874 word of SHA-256
`a62cb41fc97127edbac362afa0447cf6a45d795f327ec7f2a3652f7c12873181`,
whose exact missing set is `{0xa879,0xa87d}`.  Let

\[
U=(0xa879)\mathbin\Vert T.
\]

The canonical space-separated serialization of `U` has length 12,875,
SHA-256
`74d9aa13a6b9dae664ccbaa744a16efa724acbafee2ed44afc5462a03c5bc441`,
and is universal.

Two exact negative results hold.

1. Deleting any one cell of `U` leaves at least two holes.  Thus `U` has no
   universal length-12,874 subsequence.
2. For every cell `p` of `T` and every nonzero 16-bit mask `x`, the word
   `x || (T with cell p deleted)` is nonuniversal.  Thus the complete
   same-length prepend-plus-delete family contains no length-12,874 solution.

Both statements are source-relative.  They do not exclude an internal
insertion, two coordinated replacements, or another length-12,874 basin.

## Exact deletion recurrence

For a deleted position `p`, all intervals avoiding `p` survive.  Intervals
containing `p` disappear, while intervals crossing the new seam appear.  If
`L_p` and `R_p` are the multiplicity-bearing suffix and prefix OR states on
the two sides, then the lost and added multiplicities are exactly

\[
\begin{aligned}
L_t&=\sum_{\ell,r:\ \ell\lor w_p\lor r=t}m(\ell)m(r),
  &&\ell,r\text{ optional},\\
A_t&=\sum_{\ell,r:\ \ell\lor r=t}m(\ell)m(r),
  &&\ell,r\text{ nonempty}.
\end{aligned}
\]

Hence the post-deletion multiplicity is `N_t-L_t+A_t`.  The checker applies
this identity to every target and every deletion, and directly replays every
minimum row.

## Deleting from the universal word U

The complete number-of-holes histogram over all 12,875 deletions is

| holes | deletions | holes | deletions |
|---:|---:|---:|---:|
| 2 | 7 | 11 | 774 |
| 3 | 5 | 12 | 636 |
| 4 | 182 | 13 | 741 |
| 5 | 930 | 14 | 499 |
| 6 | 1636 | 15 | 366 |
| 7 | 1895 | 16 | 190 |
| 8 | 1989 | 17 | 176 |
| 9 | 1657 | 18 | 3 |
| 10 | 1131 | 19 | 58 |

The seven minimum rows, with zero-based positions, are exactly:

| deleted position | deleted cell | exact holes |
|---:|---:|---|
| 0 | `0xa879` | `{0xa879,0xa87d}` |
| 1 | `0x882c` | `{0xa86d,0xac6d}` |
| 2 | `0x2829` | `{0x286d,0x2c6d}` |
| 6436 | `0x0600` | `{0x4e61,0x4e63}` |
| 6440 | `0x2879` | `{0x2879,0x287d}` |
| 12871 | `0x0864` | `{0x8ce6,0x9ce6}` |
| 12874 | `0xce41` | `{0xce61,0xce63}` |

The canonical digest of all 12,875 deletion rows, including every exact
missing set, is
`c4637830ef650b8fd12518f5f2856e0c952538133862c91dafb356fde1465ebe`.

## Complete prepend-plus-delete obstruction

Now delete a position `p` from the two-hole seed `T`, producing `D_p`, and
then prepend an arbitrary nonzero mask `x`.  Prepending preserves every old
interval of `D_p`.  Its only new intervals are its prefixes, with labels

\[
x,\quad x\lor d_0,\quad x\lor d_0\lor d_1,\quad\ldots.
\]

These labels form a chain under set inclusion.  Consequently, a necessary
condition for `x || D_p` to be universal is that the exact missing set of
`D_p` itself form an inclusion chain.  This condition is independent of `x`.

The complete deletion census of `T` has histogram

| holes | deletions | holes | deletions |
|---:|---:|---:|---:|
| 4 | 7 | 13 | 773 |
| 5 | 5 | 14 | 636 |
| 6 | 181 | 15 | 741 |
| 7 | 930 | 16 | 499 |
| 8 | 1636 | 17 | 366 |
| 9 | 1895 | 18 | 190 |
| 10 | 1990 | 19 | 176 |
| 11 | 1656 | 20 | 3 |
| 12 | 1132 | 21 | 58 |

**None of the 12,874 residual missing sets is an inclusion chain.**  Therefore
no value of `x` can complete any deletion.  This proves the claimed family
no-go without restricting `x` to an a priori candidate list.

For reference, the seven four-hole minima are:

| deleted `T` position | cell | exact residual holes |
|---:|---:|---|
| 0 | `0x882c` | `{0xa86d,0xa879,0xa87d,0xac6d}` |
| 1 | `0x2829` | `{0x286d,0x2c6d,0xa879,0xa87d}` |
| 6435 | `0x0600` | `{0x4e61,0x4e63,0xa879,0xa87d}` |
| 6438 | `0x4879` | `{0x4879,0x6879,0xc879,0xe879}` |
| 6439 | `0x2879` | `{0x2879,0x287d,0xa879,0xa87d}` |
| 12870 | `0x0864` | `{0x8ce6,0x9ce6,0xa879,0xa87d}` |
| 12873 | `0xce41` | `{0xa879,0xa87d,0xce61,0xce63}` |

The canonical digest of all deletion rows of `T` is
`def41fabd6b13852e9cf8820ee6d33970b708570c72e407bfc5f411d2613ccb4`.

Deleting the newly prepended `x` itself merely returns the original two-hole
word `T`, so it cannot evade the obstruction.

## Reproducer

The independent checker is
`scratch/audit_r_k16_prepend74d9_deletion_20260730.py`.  It uses exact
multiplicities for the complete censuses and a separate direct suffix-OR
replay for `T`, `U`, and every minimum row.
