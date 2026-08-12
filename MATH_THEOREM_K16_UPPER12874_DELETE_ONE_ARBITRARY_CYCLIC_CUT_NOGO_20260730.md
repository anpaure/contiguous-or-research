# Exact no-go for every delete-one and arbitrary cyclic cut of the K16 upper word

Date: 2026-07-30  
Status: exact scoped theorem; solver-free native census with an independently
brute-audited recurrence.  This is **not** an unrestricted K16 no-go.

## 1. Statement

Let `A` be the verified length-12,874 universal word

```text
answers/k16_upper12874.word
SHA256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

Delete any one of its 12,874 cells, regard the remaining 12,873 cells as a
circle in their inherited order, and cut that circle at any one of its
12,873 edges.  None of the resulting

\[
  12{,}874\cdot12{,}873=165{,}727{,}002
\]

linear words is universal.

The minimum number of holes in this complete family is one.  The unique
reported lexicographic minimizer is deletion index 1, cut 0 in the reduced
word, namely the already known raw delete-p1 basin.  Thus allowing the cut to
move does not improve the best deletion.

Consequently no optimal K16 word is obtained from this particular upper word
by one deletion followed only by a cyclic re-cut.  The global bracket remains

\[
  12873\le \nu(16)\le12874.
\]

## 2. Exact cut recurrence

Fix one deleted position and write the remaining circular word as

\[
  w=(w_0,\ldots,w_{m-1}),\qquad m=12873.
\]

For cut `c`, let `C_c(T)` be the number of ordinary linear intervals of the
rotation

\[
  w_c,w_{c+1},\ldots,w_{c+m-1}
\]

whose OR is `T` (indices modulo `m`).  Moving the cut from `c` to `c+1`
removes exactly the `m` prefixes beginning at `c`, one of each length, and
adds exactly the `m` suffixes ending at `c`, again one of each length.  Hence

\[
 C_{c+1}=C_c-P_c+S_c.                                  \tag{2.1}
\]

Along either prefix or suffix scan the OR can change at most 16 times.
Equal consecutive ORs are therefore aggregated into exact multiplicity
plateaux.  Equation (2.1) updates the complete 65,536-entry count vector in
`O(16)` time per cut.  After all `m` cuts the vector must equal its initial
value; the executable checks this closure separately for every deletion.

Initial interval multiplicities are likewise built by retaining the strict
OR chain of intervals ending at each position, of width at most 17.  Thus the
complete census costs `O(n^2 k)`, not cubic time, and does not sample or prune
any cut.

## 3. Run and result

The exact native executable is

```text
scratch/search_k16_all_delete_all_cyclic_cuts_20260730.cpp
SHA256 0afa11a5d3770dcfb048ed89674fe1e430c64b2479ddbec27bc38f7d0cf4a26a
```

It ran on four pinned H100-host CPU cores under an 8-GiB address-space cap and
a 7,200-second timeout.  No limit fired.  Resource summary:

```text
wall time     4:39.52
CPU           391%
maximum RSS   7,680 KiB
swap          0
exit status   1 (the documented NO_PASS status)
```

The final exact line is

```text
NO_PASS deletions=12874 cuts_each=12873 best_holes=1 best_deleted=1 best_cut_reduced=0
```

Retained logs:

```text
scratch/k16_all_delete_allcuts_20260730.run.log
SHA256 1b63b785c725011e45bafbb5848fe65431237161d8c554d42397cc4e25b6b272

scratch/k16_all_delete_allcuts_20260730.run.err
SHA256 2073edb612494910df4ce1fa011278be2ca84940c885d32011e06761f13347b8
```

## 4. Independent recurrence audit

The separately written Python audit compares the entire multiplicity vector
after every incremental cut with direct brute-force enumeration.  It checks
all words of lengths 2 through 6 over `{1,2,3,4}`, plus 40 seeded random
16-bit words at every length 2 through 14.  In total it compares 183,248
delete/cut count vectors over 5,976 source words and obtains

```text
PASS_EXACT_INCREMENTAL_EQUALS_BRUTE
```

Artifacts:

```text
scratch/audit_k16_all_delete_all_cyclic_cuts_update_20260730.py
SHA256 6cfc87e8636012877818ff071b2f19f0f391c1f053f42db172472910e629c332

scratch/k16_all_delete_all_cyclic_cuts_update_20260730.audit.json
SHA256 c1855acd08ca42e740ea297f02cdc07cb3f26ccc7593be74ead245b8d002610f
```

The production executable additionally checks the exact full-cycle closure
`C_m=C_0` for every one of the 12,874 deletion sweeps.  The brute audit and
the production closure invariant test distinct failure modes: the former
checks the recurrence against a direct definition; the latter checks every
large-instance sweep for lost or double-counted plateaux.

## 5. Scope

Closed exactly:

1. one deletion from the fixed verified 12,874-word;
2. every inherited cyclic cut after that deletion;
3. no substitutions, insertions, transpositions, or rethreading.

Still open:

1. deletion plus substitutions (apart from the separately closed
   delete-plus-one-substitution family);
2. arbitrary permutations/rethreads of the surviving cells;
3. other length-12,874 parent words; and
4. unrestricted length-12,873 words.

