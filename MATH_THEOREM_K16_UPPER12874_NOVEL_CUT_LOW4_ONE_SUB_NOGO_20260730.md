# Novel cyclic-cut low-hole bases admit no one-substitution K16 completion

Date: 2026-07-30  
Status: exact scoped theorem, independently audited.  It is not a global
delete/cut/one-substitution no-go.

## Statement

Start with the verified length-12,874 K16 universal word, delete one cell,
and choose any inherited cyclic cut.  Among all

\[
  12{,}874\cdot12{,}873=165{,}727{,}002
\]

resulting length-12,873 words, exactly 212 have at most four holes.  Of these,
191 use cut zero and therefore belong to the previously closed global
delete-plus-one-substitution family.  The remaining 21 use a genuinely new
nonzero cut.

No arbitrary one-cell substitution completes any of those 21 bases.
The exact native census evaluates 11,778,795 position/value assignments.
Twenty bases have no value at any position which even installs all current
holes.  The sole exception is

```text
deleted=12871, cut=12872, holes=4,
```

with 64 installing assignments; its best result still has ten holes.

Therefore every delete/cut base of the fixed parent with at most four holes
is one-substitution-incomplete.  Bases with five or more holes, multiple
substitutions, arbitrary rethreads, other parents and unrestricted K16 remain
open.  The bracket stays

\[
  12873\le\nu(16)\le12874.
\]

## Complete cut profile

The exact `O(n^2k)` cut recurrence proved and independently brute-audited in
`MATH_THEOREM_K16_UPPER12874_DELETE_ONE_ARBITRARY_CYCLIC_CUT_NOGO_20260730.md`
was instrumented without changing its multiplicity transition.  The complete
hole histogram begins

```text
1:1, 2:5, 3:10, 4:196, 5:1486, 6:4657, ... , 33:8612.
```

The low-four bank is therefore exactly `1+5+10+196=212`; no heuristic
thresholding or sampled cuts are involved.  The production profile repeats
the same best row as the independent no-pass run and checks count-vector
closure after every deletion sweep.

Artifacts:

```text
scratch/profile_k16_all_delete_all_cyclic_cuts_20260730.cpp
  SHA 5bae6c26ce96588082df5d5d337ebd86b0e66279f06355a3b52ffbd0da65e300
scratch/k16_all_delete_allcuts_low4_20260730.tsv
  SHA fc496fce30f9a1d98400b4c6ec3eec13cc96cfca18d9fccee0e28708e8664791
scratch/k16_all_delete_allcuts_profile_20260730.log
  SHA a637c3e3497707c5bb2a0dca44ffa87169e501c3fc1829de381b12f1518d2385
scratch/k16_all_delete_allcuts_profile_20260730.err
  SHA f6fd431a37a1bafd316f761dd6e7dcabb5ed08fcd89f8b0fb9946afb39425366
```

## Exact one-cell decision

For a fixed base with hole family `H`, any replacement value occurring in a
witness for every hole is a nonzero submask of

\[
  U=\bigcap_{h\in H}h.
\]

The native completer enumerates every such value at every physical position.
For a position `p`, it removes the exact multiplicity bank of all old
intervals through `p` and adds the exact bank obtained from every left/right
OR-chain pair after replacement.  It accepts only if all original holes are
installed and no uniquely supported old target is lost.  This is necessary
and sufficient for one-cell completion.

The completer source is the same source independently reconstructed in the
earlier all-12,874-deletion theorem:

```text
scratch/k16_upper12874_delete_sub1_all12874_20260730/
  search_k16_one_substitution_completion_nobest_20260730.cpp
  SHA 2eaa69c150720783f565eee42f406619a6896e90d0216a8200984d0b24472847
```

The batch driver materializes each reduced rotation literally and runs the
exact completer:

```text
scratch/run_k16_novel_cut_delete_one_sub_20260730.py
  SHA c394e4a7c28642ffdb87fe7640eca1e0a642f3d1929ee8beb8a549d81029aee2
scratch/k16_novel_cut_delete_sub1_20260730/summary.audit.json
  SHA 40dbefba9a45bec208293595e432871871f8f530e9a87c99a6ab8f85f757bdcf
  payload 2028bd3bf2a196d9c3fe13099f402eaaeef507de9a70c2409d915d9be7d71097
```

## Independent audit

A separate Python audit rematerializes every one of the 21 rotations from
the authenticated parent, recomputes its literal interval-OR hole set, checks
the profile count, reconstructs the common-mask replacement count, verifies
the exact `12873*(2^popcount(U)-1)` evaluated-row total, authenticates every
stderr/candidate disposition, and replays the batch payload hash.  It reports

```text
GO
evaluated_assignments=11778795
installing_histogram={0:20,64:1}
```

Artifacts:

```text
scratch/audit_k16_novel_cut_delete_sub1_20260730.py
  SHA 77c60adf9f3964c275e50e314a21ffc1bf6d942c62c0c3d4945a89784eb3a0d8
scratch/k16_novel_cut_delete_sub1_20260730.independent.audit.json
  SHA b02feabacf475fe2f618c06c8da8bfe464d3430e3ec017233188ee30705a0555
  payload d86a6270d28e40eed7e364b3fb5b2b7c9fb5d76dab4f20a66a1abbca6a3b449a
```

