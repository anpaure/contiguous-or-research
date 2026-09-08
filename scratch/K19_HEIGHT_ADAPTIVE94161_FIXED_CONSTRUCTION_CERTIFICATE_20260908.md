# A verified universal 94,161-letter word at k=19

Date: 2026-09-08. Status: one fixed deterministic construction and exact
coverage verification passed on h100. No cut, cycle-order, deletion,
or repair optimization was used.

The directly usable word is `answers/k19_upper94161.word`. It has exactly
94,161 nonzero letters and covers every one of the 524,287 nonempty
19-coordinate targets. Its SHA-256 is

    1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224.

This proves nu(19)<=94161. No optimality claim is made.

## 1. Exact construction and counts

Use the same canonical convention as the preceding k17 height-adaptive
certificate: on rank-nine lower states of the 19-cycle, let f complement
every bit except the unique unmatched zero, and let g=f^2. Start each
g-cycle at its smallest lower-state integer mask, keep its forward
orientation, and order cycles by their initial masks.

The exact census gives 92,378 owners in 360 cycles. Their invariant
Dyck heights have total 1,384 and histogram

| Height | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cycles | 1 | 51 | 107 | 96 | 67 | 28 | 8 | 1 | 1 |

Complement each lower cycle to its upper owners X_i. For its height h,
form the cyclic source period

    D_i=intersection_(j=0)^h X_(i+j).

Every source letter is nonempty. The verifier checks height invariance
at every state, that every positive residence exceeds h, and that every
cyclic union of h+1 consecutive source letters equals its shifted owner.

Repeating the first 2h-1 source letters after each period, then concatenating
the blocks, gives the fully verified universal word of length

    92378+2*1384-360=94786.

Instead repeat only the first h source letters in each block. The resulting
prefix has length 92378+1384=93762 and covers 523,888 targets. Its exact
missing-target census is

| Missing rank | 11 | 12 | 13 | 14 | Total |
|---:|---:|---:|---:|---:|---:|
| Number | 180 | 164 | 54 | 1 | 399 |

Append all 399 missing masks as individual letters in ascending mask order.
Every prefix witness survives, and each missing target now has a length-one
witness. This gives the universal word of length 93762+399=94161.

## 2. Exact verification

For each of the three words, all suffix ORs at every endpoint were
enumerated, retaining a start/end witness for every distinct target.
A separate segment tree then re-evaluated every recorded ordinary,
nonwrapping interval OR. The theorem and repaired words each passed
524,287 witness checks; the partial prefix passed 523,888.

The three outputs have these hashes:

| Word | Length | Missing | SHA-256 |
|---|---:|---:|---|
| `k19_height_theorem94786.word` | 94,786 | 0 | `57d460152d07d62de354a1e194ab196e1933b9621df926e91be3d28de193a50b` |
| `k19_height_trimmed93762.word` | 93,762 | 399 | `669c59df0794c8dd152238c8215e5aa15fdfc03952015a78cc61ce05618f9df5` |
| `k19_height_repaired94161.word` | 94,161 | 0 | `1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224` |

## 3. Artifacts and resource record

The exact deterministic generator and verifier is

    scratch/verify_k19_height_adaptive_fixed_construction_20260908.py.

The local directory `scratch/k19_height_adaptive_20260908/` contains all
three words and `height_adaptive_fixed_certificate.json`, including all
399 missing masks, the height census, hashes, and exact coverage counts.
The best word is additionally copied to `answers/k19_upper94161.word`.

The single mathematical process ran only on h100, with outputs at

    /home/amodo/exact-b-k19-height-adaptive-20260908/.

The complete per-target witness maps and canonical cycle/source data are
retained there. Those larger JSON files were not copied locally because
the requested immediate delivery was the compact report and usable word.

The process had limits of 300 CPU seconds, 360 wall seconds, and 4 GiB
address space. Its recorded construction-and-certification time was about
4.27 CPU and wall seconds. Both universal-word checks returned PASS.
No larger resource allowance or additional construction attempt was needed.
