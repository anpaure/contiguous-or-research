# Every delete/cut base with at most five holes is one-substitution-incomplete

Date: 2026-07-30  
Status: exact scoped theorem, independently audited. This is not an
unrestricted length-12,873 or K16 no-go.

## Statement

Start with the authenticated universal K16 word

```text
answers/k16_upper12874.word
SHA 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

Delete any one of its 12,874 cells and cut the inherited length-12,873
cycle at any one of its 12,873 positions.  Among the resulting

\[
  12{,}874\cdot12{,}873=165{,}727{,}002
\]

linear words, exactly 1,698 have at most five missing masks. Their complete
hole histogram is

```text
1:1, 2:5, 3:10, 4:196, 5:1486.
```

No arbitrary one-cell substitution completes any of these 1,698 words.
Consequently, any length-12,873 universal word obtained from this parent by
one deletion, one cyclic rethreading cut, and at most one arbitrary nonzero
replacement must pass through a base with at least six holes.

This theorem combines three disjoint exact banks:

1. all 1,122 cut-zero rows with at most five holes are contained in the
   previously audited all-deletion/all-one-substitution theorem;
2. the 21 genuinely nonzero-cut rows with at most four holes are closed by
   `MATH_THEOREM_K16_UPPER12874_NOVEL_CUT_LOW4_ONE_SUB_NOGO_20260730.md`;
3. the remaining 555 genuinely nonzero-cut rows have exactly five holes and
   are closed by the new census below.

The global bracket remains

\[
  12873\le \nu(16)\le12874.
\]

## Exact five-hole profile

The independently audited all-delete/all-cut multiplicity recurrence was run
to threshold five without changing its transition.  It reports the complete
histogram above and retains exactly 1,698 rows. Of the 1,486 five-hole rows,
931 have cut zero and 555 have nonzero cut.

Artifacts:

```text
scratch/k16_all_delete_allcuts_low5_20260730.tsv
  SHA 71abe73c1997468092bb94430f6acd3118f272266b69086ec99142ad08d8cc4a
scratch/k16_all_delete_allcuts_profile5_20260730.run.log
  SHA 1c3bad72c2159b9caea385f59a5d9a599e3679fee2b4f98f8ce60c606ac5c6ef
scratch/k16_all_delete_allcuts_profile5_20260730.run.err
  SHA 54bcde872b18a8be6bb3f5d9c87abe3d2aa79533300fe9a494669e5376be1c92
```

The four-thread H100 run finished in 343.52 wall seconds with 10,240 KiB
maximum RSS and no swap.

## Exact one-cell decision on the 555 novel rows

Let `H` be the five holes of a fixed base. Any new interval witnessing every
member of `H` must contain the changed cell, so its replacement value is a
nonzero submask of

\[
  U=\bigcap_{h\in H}h.
\]

The already independently audited native completer exhausts every physical
position and every nonzero submask of `U`, removes the exact old interval
multiplicity column through that position, inserts the exact new column, and
accepts exactly when every target has positive multiplicity.

Across all 555 rows it evaluates 59,769,339 position/value assignments and
finds no completion.  The common-mask popcount histogram is

```text
0:2, 1:48, 2:151, 3:228, 4:101, 5:21, 6:2, 7:2.
```

For 553 rows no assignment even installs all five original holes. Exactly two
rows have 64 installing assignments:

```text
deleted=12872, cut=12872;
deleted=12873, cut=12872.
```

Both have the same best replacement `(position,value)=(6435,52321)` and still
leave eight masks missing. No candidate word was emitted.

Production artifacts:

```text
scratch/k16_novel_cut_delete_sub1_h5_20260730.audit.json
  SHA e3eb29e904cd64afa9a517134e578b2c9df6f0c0d3c0d999639a65c44f11ff53
  payload e7e570e275c32b20288203821371a965817fb61b945afdd18829c49a6c1c4eba
scratch/k16_novel_cut_delete_sub1_h5_20260730.run.log
  SHA 2a98a5b68a53275c6b9c0444092a23b5ee4c44b7aee380e85ad6494fd23f49ce
scratch/k16_novel_cut_delete_sub1_h5_20260730.run.err
  SHA 2aed98217c6dedd38ff6b9a30679def2365fc8e001f07e6f6cfba4ddd885a4cf
```

## Independent audit

A separate Python audit:

* reconstructs the exact 555-row scope from the retained profile;
* rematerializes every deletion and rotation from the authenticated parent;
* checks every materialized word and transcript hash;
* verifies the common-mask replacement count
  `12873*(2^popcount(U)-1)` independently for every row;
* checks the 555 exit dispositions and the absence of candidate files;
* authenticates the batch payload and exact one-record-per-row run log.

It reports `GO` with the same 59,769,339 assignments and installer histogram
`{0:553,64:2}`.

```text
scratch/audit_k16_novel_cut_delete_sub1_h5_20260730.py
  SHA 5a2f49a59ae4b49d1418a80a7fac5fa69c3f4fc22fb155e84387621b9b84f656
scratch/k16_novel_cut_delete_sub1_h5_20260730.independent.audit.json
  SHA f89f85b5a642eded12edae79e6cbc4b125df408b5e2f62d12217a5db5ea001d3
  payload d4cdb83ead62344d3e64995bc5d28c7847a2d27d2c5f0991a9c8b3d0a80af8bd
```

## Scope boundary

The result is exact only for this fixed parent, one deletion, one cyclic cut,
and one arbitrary replacement, restricted to bases with at most five holes.
It does not exclude six-or-more-hole bases that improve after one replacement,
two or more replacements, non-cyclic rethreads, other parents, or globally
different length-12,873 constructions. It therefore supplies no global lower
bound beyond 12,873.
