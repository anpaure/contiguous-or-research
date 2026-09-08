# K16 Hall-24 forward-block rethread census

Date: 2026-07-30  
Status: **solver-free scoped no-go; no global K16 claim**

## 1. Frozen source and move class

The authenticated source is

```text
scratch/s4_exact229_swap6608_12714_l3_20260730.targets
SHA256 955dc2fb350cd399f050e4dafb481925633e0024eaa438ee3cf4f984e0acb995
```

It has length 12,873, exact literal middle replay, compiler capacity 32,063,
generalized Hall deficiency 24, and sole arbitrary-upper hole `0x4e79`.

Write the occurrence-labelled chronology as

\[
    Q=P\,X\,Y\,Z,
    \qquad |X|\ge13,quad |Y|\ge1,
\]

and replace it by

\[
    Q'=P\,Y\,X\,Z.                                      \tag{1}
\]

No block interior is reversed.  Thus (1) is a single forward block
cut-and-rejoin and changes only three seam neighbourhoods.  The lower bound
`|X|>=13` deliberately excludes the already-closed one-token and protected
block faces through length 12.

## 2. Endpoint completeness

Every row has rank eight.  An interval with OR `0x4e79` consists only of
rank-eight facets of `0x4e79`.  Since the source has no such interval, any
new witness in (1) crosses a new seam.  At that seam the two adjacent facet
runs have union `0x4e79`.  Therefore it is complete to enumerate boundary
triples `(a,b,c)` for which one of the three new seams has this property.

The exact C++ census is

```text
scratch/k16_h24_forward_block_rethread_complete_20260730/search.production.cpp
SHA256 bd61b7eb40e889ededee6e2e9c9502222e59fee9410a057d223f330a3f95367f
```

For every boundary triple it reconstructs the full occurrence-labelled
chronology, rebuilds its variable-depth maximal envelopes, checks literal
middle equality at every row, and then enumerates all unrestricted interval
ORs.  The endpoint-inclusive production run visited

```text
565369 endpoint-forced forward rethreads
   256 exact-middle rethreads
     3 exact-middle and arbitrary-upper-complete rethreads.
```

The frozen production transcript is

```text
scratch/k16_h24_forward_block_rethread_complete_20260730/run_all.stderr
SHA256 6dd0350bd6c4fc22c7deefba3c92c561e2700652b5b6a166e1676f216656f438
scratch/k16_h24_forward_block_rethread_complete_20260730/summary_all.tsv
SHA256 956772f128835949ba9823b9175e1ffec937a726b76d3a70477b958ea501f7c5
```

As an independent subface check, keeping the entire move inside one
constant-depth phase gives

```text
82389 formal rethreads, 114 exact-middle, 0 upper-complete.
```

Hence every simultaneous middle/upper pass crosses the first depth boundary.

## 3. The three simultaneous passes

The complete pass list is:

| candidate | `(a,b,c)` | `(|X|,|Y|)` | flats | cells | Hall deficiency |
|---|---:|---:|---:|---:|---:|
| 0 | `(3105,4148,12714)` | `(1043,8566)` | `5277,12869,12871` | 31020 | 58 |
| 1 | `(3105,4475,12714)` | `(1370,8239)` | `4950,12869,12871` | 30693 | 61 |
| 2 | `(4507,5491,12714)` | `(984,7223)` | `5336,12869,12871` | 31079 | 51 |

Their authenticated words and independent complete generalized-Hall audits
are:

```text
candidate_0.targets  05be5723307094a064255283d00cb6a4bed2ecff9bf844504843de833743f7af
candidate_0.hall     c0567655b05a1408d762d75ebc3cd9a18823431e48d551f0b4599079de6cc09f
candidate_1.targets  60adfd5725e421e8f6611c862735d16aeede7902d1d5b999ac507ef56ca52967
candidate_1.hall     12d8b0e465967a55f0d8af90022f03f0d6864debfdbb5f8008f97fae93cd186e
candidate_2.targets  53ccee88a1c3aee0dde3a63225180dd77734c024bfd302d91b947405895a3285
candidate_2.hall     d090e07193a7ef12e79a4049bd0778d191823a6a02683c5732627ea2f5d33c0b
```

under

```text
scratch/k16_h24_forward_block_rethread_20260730/all/
```

The independent auditor is

```text
scratch/audit_k16_generalized_hall_20260730.py
```

and rebuilds all 26,332 lower targets, every compiler cell and incidence,
the maximum matching, and the canonical alternating Hall witness.

Each pass moves the first flat earlier by exactly `|X|`; its compiler-cell
loss is also exactly `|X|`.  Thus repairing the upper hole in this family
does not merely fail to preserve the Hall-24 gain: the best pass has Hall
deficiency 51.

## 4. Scoped conclusion

> **Theorem.** No occurrence-labelled forward-block rethread (1) of the
> authenticated S4 Hall-24 source with `|X|>=13` simultaneously has exact
> middle replay, complete arbitrary-upper coverage, and generalized Hall
> deficiency at most 24.

This closes one forward block only.  It does not close a composition of two
rethreads, a reversed block, an arbitrary permutation, a different Hall-24
parent, or an unrelated length-12,873 chronology.  In particular it is not a
global no-go for `nu(16)=12873`.
