# Exact packet-15 ladder audit at Hall 20

Date: 2026-07-28

Status: exact audit of the four specified materialized successors.  The two
original packet moves really do compress one canonical component by 32
targets, but none of the four successors repeats that compression.  Two
successors preserve the already-compressed component exactly; the other two
are the literal inverse moves and return to the frozen H20 base.  Therefore
this four-state ladder contains no `129/128 -> 97/96` double-compressed state.

No new scan was run.

## 1. Evidence

The proof checker and full exact ledger are

```text
scratch/audit_k15_h20_packet15_double_compression.py
scratch/audit_k15_h20_packet15_double_compression.json
```

with SHA-256 values

```text
a551b95111bb3fdf828b4b596cdb82086799c53bba5f7b9dbfaef832238c3c13
1f2b7d5c17e97a098ddf5affef26183a3c6aece0f4a3182245d98feab89d9595
```

The six retained state files have hashes

```text
parent 0161: fdb95c316a3604f23aba75d1360230330743e443306cea5313e866a721d87563
parent 0163: 88c49a713755ba42d3577e2c80ad1c487ff7a9dd0f2f52d25e5af8da02b415c8
0161/0164:   f3ae1daed3294fe937612d4f2967a4960a982ab9ba4921aa503223f094a70194
0161/0165:   685c060189900b45d025bd14151e231a2142621d2f3aeadd44d847f72bed8c32
0163/0162:   957a0be6f6f370094670dd5f4cc9fee47847638139220966e0bde8302970769a
0163/0165:   0d6a27f02aaf73086dc3c6f404f82fdc1f627227e269e9837eff9a634b3c4bc6
```

Every child is materialized exactly from its declared parent.  Every child
is a rank-eight deck permutation, a Johnson path, depth-three resident,
Hall 20 with matching rank 16,363, has six zero candidates, lower-hole vector
`(4,18,11,1,0,0,0)`, and no upper holes through depth seven.

## 2. The two genuine first compressions

Relative to the frozen H20 base, parent `0161` changes only the canonical
component rooted at 960, while parent `0163` changes only the component
rooted at 8217.  In both cases

\[
 (161,160)\longmapsto(129,128),\qquad
 37\text{ targets leave},\quad5\text{ enter},\quad\Delta=-32. \tag{2.1}
\]

For root 960 the removed-target digest is

```text
decdf090ef82127bb5606af3067f217109486b0ab22a674dcafdf0c20786cc22
```

and the added-target digest is

```text
21b9460cd49ec4350520b92ff51ed537bcde95b12fcbb3f8a8f4553413fcb480.
```

For root 8217 the corresponding hashes are

```text
removed: 50dcb5174108427ea751449a1a7cb8904fa785be0c12bf6a4f5ad96cad513e79
added:   d8d5b905b548f52264df595144ee400cc6eeee835eed13155ede34ffb0da8c18.
```

The JSON stores all 37 and all five masks, not merely their digests.  It also
stores the complete occurrence-multiplicity-preserving restricted profile
Counters.  Their nonzero union-profile changes are:

```text
root 960, removed:
  {960,961}, {968,969}, {976}, {984}
root 960, added:
  {960,976}, 2*{961}, {969}, {9153}

root 8217, removed:
  {8217,8219}, {8249}, {24601,24603}, {24633}
root 8217, added:
  {8217,8249}, 2*{8219}, {8223}, {24603}
```

All omitted multiplicities are one.

## 3. The four successors

The exact result is

| parent/child | move | focal size | target change | exact parent-root profile change | provenance |
|---|---|---:|---:|---:|---|
| `0161/0164` | `FF(1783,1798,5169)` | `129/128 -> 129/128` | `0 out, 0 in` | zero | new noncommuting packet |
| `0161/0165` | `FF(1784,5156,5170)` | `129/128 -> 161/160` | `5 out, 37 in` | inverse of first compression | exact inverse |
| `0163/0162` | `FF(1783,1798,3098)` | `129/128 -> 129/128` | `0 out, 0 in` | zero | new noncommuting packet |
| `0163/0165` | `FF(1788,3089,3103)` | `129/128 -> 161/160` | `5 out, 37 in` | inverse of first compression | exact inverse |

For `0161/0164` and `0163/0162`, all twenty canonical DM target components
are identical to their parent's components.  More strongly, the exact
physical restricted-shore Counter on the focal parent-root component is
identical before and after:

```text
root 960:  649670c84c080e08a77196806a617fd603d4c557a03222c1dffc9ff3ae01f3c7
root 8217:  232434f8844a4898e72bf507febf839ef4d4615c245e9f6bd1bb94fb11b22a66
```

Thus these two successors are chronology changes, but they supply neither
the desired `37 out / 5 in` target current nor any hidden parent-root profile
current.  Their canonical DM size stays `645/625`.

For both `0165` successors, the final middle path is byte-for-byte identical
as an integer sequence to the frozen H20 base; its sequence digest is

```text
bd2fa7714020c63bbb280d259be1c61fab095e0e49019e316311c921ab117e6b.
```

Their JSON file hashes differ only because their parent/move metadata differ.

## 4. Ordered and unordered packet provenance

For each adjacent-block swap, the audit identifies the unique length-15
block and hashes both its ordered tuple and its sorted tuple.

| transition | ordered SHA-256 | unordered SHA-256 |
|---|---|---|
| base to `0161` | `d557b9c3a9c5f4b638c6ccc3ea04039299ca5aa2fdca6dea3bf39145b9576f2e` | `4ed3ed8bd97133470fc0b5335726a03dab3e6dcf59395b8821572249cfcad445` |
| `0161` to `0164` | `b71229be6d394cb43e2fe813e2b6eb92013d1aab5028b0a0b7bcddd7f7cdf756` | `3df17d05837ecbaf02b6064c3ac4c3957cf6ac1d7d49ce696f3c31a4af7b543c` |
| `0161` to `0165` | `d557b9c3a9c5f4b638c6ccc3ea04039299ca5aa2fdca6dea3bf39145b9576f2e` | `4ed3ed8bd97133470fc0b5335726a03dab3e6dcf59395b8821572249cfcad445` |
| base to `0163` | `146abff75863d27ca4f37100783cae9cf740e4b28569e6a61768093dcf64fb9d` | `7690a5db2a5215ae91ec2bea30881d1083b641514a28eb3455912ada95725622` |
| `0163` to `0162` | `5ca003103abbe190d6827887d7fc8ab52e8e9d8c1c14e2df99535a38679d8fd3` | `ec8dfe45d4766b6463bd4c6bafbaacdd467c91bb33f698ad7980fbbc99d92b07` |
| `0163` to `0165` | `146abff75863d27ca4f37100783cae9cf740e4b28569e6a61768093dcf64fb9d` | `7690a5db2a5215ae91ec2bea30881d1083b641514a28eb3455912ada95725622` |

The two `0165` moves use exactly the original ordered packet and swap it back
across exactly the original crossed block.  They are literal inverses.

The alternative successor packet is disjoint from the first packet in both
branches, but this does **not** make the moves commute: the complete adjacent
block-swap supports overlap in 3,386 masks on branch `0161` and 1,311 masks
on branch `0163`.  The second named block pair is not even contiguous in the
base state, so the reverse-order named swap is undefined.  Exact replay
therefore classifies these as noncommuting overlapping block moves, not as
independent packet translations.

## 5. Conclusion

The hoped-for iteration

\[
 (161,160)\to(129,128)\to(97,96)
\]

does not occur in the four specified successors.  The first arrow is exact
on both roots.  At the second arrow the two noninverse candidates remain
`129/128` with zero target and profile current, while the two inverse
candidates undo the first arrow.  Hence there is no double-compressed path or
hash to promote from this audited four-state ladder.

