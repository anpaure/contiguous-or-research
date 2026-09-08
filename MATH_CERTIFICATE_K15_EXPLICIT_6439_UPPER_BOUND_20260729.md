# The explicit `k=15` upper bound improves to 6,439

Date: 2026-07-29

## Result

There is an explicitly stored contiguous-OR word on `[15]` of length

\[
                              \boxed{6439}.
\]

Together with the proved deadline lower bound `B(15)=6438`, this gives

\[
                         \boxed{6438\le \nu(15)\le6439}.
\]

The word is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/arc7_6439.word
```

with SHA-256

```text
50e1877b1fd336673738c5963aa5571aae6d6417d438aa100ba881c21c826a34
```

The independent literal verifier reports

```text
PASS k=15 length=6439 covered=32767/32767
```

so every nonempty mask is the OR of a contiguous interval of the stored
word.  No solver assertion is used for this final coverage claim.

## Construction

The independently audited equivariant factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  from3_markov_s7_merge.best.json
```

has SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555
```

and consists of two physical cycles of lengths `6390` and `45`.  It has
minimum residence four and complete lower and upper fixed-width shadows at
every depth.

All `1,290` residence-safe Johnson seams that recycle one removed lower-q1
colour were exhausted combinatorially.  None preserves every upper target,
but arc `7` has exactly one upper hole, namely mask `20215`; its sole missing
lower target `3179` has an exact boundary assignment.  The exhaustive ledger
is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  twocycle_exhaustion_arbitrary.audit.json
```

with SHA-256

```text
bcc52a207aa5ec25c11384822b7144526e3dd6c41a2344d944fb7aa0ca6f310c
```

The exact generalized compiler emits a length-`6438` prefix for arc `7`:

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  arc7_6438.prefix.word
```

with SHA-256

```text
dd512cf9f1f71284ebce86654031c7745f0cf6c344103a3a5d8e9c31b334a0d3
```

Direct enumeration verifies that this prefix misses exactly `20215`.
Appending that single mask gives the stored `6439` word.

The proof-safe builder and its retained audit are

```text
scratch/compile_k15_two_cycle_one_hole_20260729.py
scratch/k15_fixed_matching_pbbs_resident_20260729/
  arc7_6439.build.audit.json
```

The independent verifier transcript is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  arc7_6439.independent.verify.txt
```

with SHA-256 values

```text
6e9733f92fdaf4e14653819c0677513ff225f701937f33ea1b0a6f9c12ef88d7  build audit
b762ab817531027e42f76f4ac531207bab0167c41dbc19fc0db941117fe1714f  verifier transcript
```

## Exact scope

This proves only the upper bound `nu(15) <= 6439`.  It does not prove that
`6439` is optimal.  The conjectured equality `nu(15)=B(15)=6438` remains open
by exactly one position.

