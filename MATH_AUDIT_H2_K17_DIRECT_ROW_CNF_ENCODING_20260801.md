# K17 direct rooted-row CNF encoding audit

Date: 2026-08-01  
Lane: H2 independent audit  
Status: **GO at source/encoding level; generated three-basin DIMACS superseded without solve**

Audited generator:

```text
scratch/build_h2_k17_rooted_flag_direct_row_cnf_20260801.cpp
SHA256 3b92d8a2b41a040414061d3ec12ec441ba1241c18a4920b7dacd4d4dff5245a4
```

The source passes `clang++ -std=c++20 -Wall -Wextra -Wpedantic
-fsyntax-only`.  The following semantic checks are independent.

## 1. Exact channel equivalences

At a root, let exactly one option variable be true.  For a membership bit `m`,
the generator emits

```text
not m OR (all options containing the bit),
m     OR (all options omitting the bit).
```

If the selected option contains the bit, the second clause becomes the unit
`m`; otherwise the first becomes `not m`.  Thus these two aggregate clauses
are an equivalence, not merely a one-way channel.  The identical argument
proves each per-root type channel, so exactly one of the nine type channels is
true at every root.

## 2. Sinz caps and exact type masses

The sequential variables `s[i][j]` carry the forward assertion that at least
`j+1` inputs among `x[0..i]` are true.  The propagation and overflow clauses
are the standard at-most-`k` implication system.  If at most `k` inputs are
true, the canonical prefix-count assignment satisfies it.  If a `(k+1)`st
input is true, the first `k` inputs force `s[i-1][k-1]`, contradicting its
overflow clause.  Hence the encoding is equisatisfiable exactly when the cap
holds.

There are 1,430 roots and the nine caps sum to 1,430.  Since each root has
exactly one true type channel, the nine upper bounds are simultaneously exact
equalities.  No separate lower-bound clauses are missing.

## 3. Suffix ledgers

Every rank-two-through-seven necklace is emitted as an exactly-one group over
the options carrying that literal suffix.  `C0` and `C0 union C1` always have
different cardinalities because `C1` is nonempty in all nine types, so an
option cannot occur twice in one group.  Rank eight is already exact from one
option at each fixed root.

## 4. Rotation and compressed owner clauses

An owner incidence stores `shift` with

```text
rot_left(root_rep,shift) = owner_rep - {complement}.
```

Therefore physical owner bit `b` is canonical flag bit `b-shift mod 17`, which
is exactly the index used in every owner clause.

For ordered old/next incidences, support implies

```text
next.complement in aligned old C2,
aligned next C2 subset aligned old C1,
aligned next C1 subset aligned old C0.
```

Only the eight bits of the next root are scanned.  The omitted
`next.complement` bit is zero in all three next classes because every option is
validated as a partition of its fixed root.  At `old.complement`, the two old
classes are likewise forced zero, and the specialized binary clauses are the
correct reductions.  Thus the compressed scan is exact.  Same-root pairs are
excluded, and the positive ALO over all remaining ordered-pair atoms is
equivalent to existence of a loop-free incoming pair.  With owner scope
`all`, all 1,430 owner ALOs are present.

## 5. Generated artifact status

The now-superseded all-owner three-basin artifact had
2,430,270 variables and 6,453,771 clauses, CNF SHA
`5f18378586d06ff512b3035f06a2013e901ca3644a9746290bbdde7533578b98`.
Its generator-side raw/channel regression reported dead-owner counts
782/703/708 for baseline/28401/shuffle201, agreeing with the independent
literal decoder.  It was not sent to a solver.

An independent full sequential clause-replay program was prepared:

```text
scratch/audit_h2_k17_rooted_flag_direct_row_cnf_20260801.py
SHA256 9bdb36ccc2a750ce6711be4904a9e41d4089fa92aaee07a667cc75c1a6d3ca1b
```

It was syntax-checked and uploaded, but **not executed** before the three-basin
artifact was superseded.  No clause-level PASS or DIMACS verdict is claimed.
The source-level proof above is reusable for the final union provided its
encoding body remains byte-identical; the final option/provenance changes and
new DIMACS hashes still require fail-closed replay.

## 6. Scope

This is a GO for the audited static-ledger plus owner-support encoding, not for
SAT, a rooted-state transversal, a transition cycle cover, voltage, upper
coverage, source realization, or the compiler.  Neither three-basin CNF is a
live search target.
