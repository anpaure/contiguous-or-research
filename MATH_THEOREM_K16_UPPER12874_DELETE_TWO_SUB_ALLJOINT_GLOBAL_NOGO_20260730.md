# K16 upper-12874: global all-joint delete-plus-two-substitution no-go

Date: 2026-07-30  
Status: exact scoped theorem; independently replayed  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Result and exact scope

Fix the verified universal word

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Delete any one cell.  Then change two distinct remaining cells to arbitrary
nonzero 16-bit masks.  There is no completion in the following exact class:

> every hole created by the deletion has a new final witness containing both
> changed cells.

The search covers all `12,874` deletions, all physical supports, all ordered
nonzero replacement values, and exact collateral multiplicities.  A putative
zero-collateral row is replayed against all `65,535` targets before acceptance.

This is **not** a global delete-plus-two-substitution no-go.  The complementary
provider-first branch remains: at least one edit, applied alone to the deletion
word, supplies at least one original deletion hole.  Partial providers are
essential; the previously retained `131,482` rows install *all* original holes
and therefore do not exhaust this complement.

## 2. Complete dichotomy

Let `H_d` be the exact holes after deletion `d`, and let the two changed cells
be `p,q`.  Every final witness of `h in H_d` contains at least one changed cell.
Consequently every two-substitution completion belongs to the union of:

1. **all-joint:** every `h` has a witness containing both `p,q`;
2. **provider-first:** some `h` has a witness containing exactly one of
   `p,q`; orient that edited cell first, and it supplies `h` in the one-edit
   intermediate word.

The classes can overlap, which is harmless.  The first class is closed here.
The second must enumerate partial as well as full first providers.  Deletion
`2` is the standing completeness test: the exact two-edit circuit recorded in
the multiroot audit reaches the one-hole `0x2c6d` state although neither edit
is full-provider-first.

## 3. Exact support reduction

Put

```text
I_d = intersection(H_d).
```

If every original hole has a both-cell witness, then both new values `u,v` are
nonzero submasks of `I_d`, and every unchanged cell strictly between `p,q` is
a submask of `I_d`.

For `h in H_d`, let `L_h(p)` be the OR of the maximal `h`-compatible suffix
ending at `p-1`, and let `R_h(q+1)` be the OR of the maximal `h`-compatible
prefix starting at `q+1`.  With `J(p,q)` the unchanged interior OR, some
combined value `z=u OR v` can provide `h` exactly iff

```text
L_h(p) OR J(p,q) OR z OR R_h(q+1) = h.
```

Hence a support survives for all holes iff it survives at the maximal value
`z=I_d`.  Its mandatory combined bits are

```text
M(p,q) = union over h in H_d of
         (h minus (L_h(p) OR J(p,q) OR R_h(q+1))).
```

Every admissible combined value is exactly

```text
M(p,q) subseteq z subseteq I_d,  z != 0,
```

and every ordered nonempty split `u OR v=z` is enumerated, excluding unchanged
endpoint values.  This is an equality, not a relaxation.

The independent support census gives:

```text
deletions                              12,874
physical position pairs considered    166,320,953
surviving supports                     17,294
combined values                        61,974
ordered genuine-change value pairs     112,462,474
```

The concentration is extreme.  Deletion `1`, already frozen independently,
accounts for `13,235` supports and `102,404,745` value pairs.  Every deletion
with at least eleven initial holes has zero all-joint support.

## 4. Exact collateral criterion

For a fixed support, only intervals meeting `p` or `q` change.  Their three
disjoint classes are:

1. intervals containing `p` but not `q`;
2. intervals containing `q` but not `p`;
3. intervals containing both.

Left/right OR chains enumerate each class with exact multiplicity.  A covered
target is private precisely when its full baseline multiplicity is contained
in those classes.  For every private target the search tabulates, as functions
of `u`, `v`, and `u OR v`, whether it is restored by a p-only, q-only, or
both-cell interval.  Requiring each private target in their union is necessary
and sufficient: every nonprivate target retains an unchanged witness.

The newly run residual search re-derived and exhausted exactly

```text
active deletions                       2,029
supports                               4,059
ordered replacement pairs              10,057,729
collateral bitset checks                10,057,729
minimum remaining private targets       2
```

No candidate survives.  Composing this with the previously frozen global
deletion-1 audit exhausts all `17,294` supports and all `112,462,474`
all-joint assignments.

## 5. Independent authentication

The residual result was produced three ways:

1. local Clang, four threads;
2. local Clang, one thread;
3. H100 GCC 13, one low-priority CPU core.

The two local result/audit pairs are byte-identical.  The H100 result TSV is
also byte-identical:

```text
a2ea7b1e3bf23d20d19aafb81fa258e453882d3954773c6a8125b482e534d243.
```

The H100 run used `19.36 s`, `11,132 KiB` maximum RSS, no swap, a 300-second
timeout, and the unique directory

```text
/home/amodo/or15/work/root_k16_global_alljoint_delete2_20260730.
```

The fail-closed Python audit authenticates the source and both independent
support/search implementations, checks all `2,029` rowwise expected/actual
equalities, recomputes both aggregate totals, confirms the frozen deletion-1
word is literally source deletion `1`, and composes the two scopes.

## 6. Provider-first complexity and next exact target

The complete complementary branch is larger than the old full-provider table.
There are `116,073` deletion-hole incidences.  At every remaining position,
setting a changed cell equal to a hole supplies that hole as a singleton.
Thus, before optional values are counted, the partial-provider atlas already
has approximately

```text
12,873 * 116,073 = 1,494,207,729
```

position/hole provider incidences (with only the trivial unchanged-value
duplicates removable).  Scanning every second position naively is therefore
not viable.

The smallest faithful sequential partition is:

1. choose the canonical first edited cell among those that supplies at least
   one original hole;
2. compute the exact intermediate holes: residual original holes plus all
   first-edit ejection debts;
3. for a second position, add the targets whose every intermediate witness
   crosses that position;
4. intersect these required targets and use the maximal-intersection value;
   if any second value succeeds, this maximal value succeeds too;
5. impose the exact second-position private-target table and literal replay.

Both value domains have a closed Boolean-interval form.  For an original hole
`h` and first position `p`, let `C_h(p)` be the OR of the maximal
`h`-compatible suffix before `p` and prefix after `p`.  Then `u` supplies `h`
alone exactly when

```text
h minus C_h(p) subseteq u subseteq h,  u != 0.
```

Thus the complete partial/full first bank is a union of at most `|H_d|`
Boolean intervals per position.  After the first edit, let `R_q` consist of
all intermediate holes and every covered target whose witnesses all cross the
prospective second position `q`.  With `C_t(q)` defined in the intermediate
word, put

```text
L_q = union over t in R_q of (t minus C_t(q)),
U_q = intersection over t in R_q of t.
```

A completing second value exists exactly when `L_q subseteq U_q`; the maximal
value `U_q` itself services every required target.  Since intermediate holes
remain, it cannot merely be an unchanged cell that was already servicing all
of them.  This collapses the second mask loop to one exact value per position.

The Boolean-interval lemma removes the `65,535`-value loop for the second edit,
but a new shared provider-position index is still required to avoid a
quadratic scan over roughly 1.5 billion first incidences.  The already retained
`131,482` full-provider rows form a tractable strict subbranch; they are not the
whole complement.

## 7. Artifacts

```text
scratch/census_k16_upper12874_delete_two_sub_alljoint_supports_20260730.cpp
  SHA-256 455eeb97b844d110f72a97e66b621e5d1377974ba891a372c92c6bfea57ef731

scratch/k16_upper12874_delete_two_sub_alljoint_global_20260730.tsv
  SHA-256 426bd3201b5ea5906bd0bab6e52ac41fc9acab59f7ceef8dd39fe9426aabaafa

scratch/k16_upper12874_delete_two_sub_alljoint_global_20260730.audit.json
  SHA-256 e4cff194fab654af3078e3b4f41eca4a3a7c6697442518ac41d866d17ff04ff0

scratch/search_k16_upper12874_delete_two_sub_alljoint_global_20260730.cpp
  SHA-256 a43a530b39db54166a23584c0622667d0ba7623a0938ef1da46595f2c98aa63a

scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730/results.tsv
  SHA-256 a2ea7b1e3bf23d20d19aafb81fa258e453882d3954773c6a8125b482e534d243

scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730/audit.json
  SHA-256 6980f27defe7f2cd6dc9a0a33e4447093ea6519955aa6c5d28a7ef4a363170de

scratch/audit_k16_upper12874_delete_two_sub_alljoint_global_20260730.py
  SHA-256 6efdb87b23c440782d4c1f707a91fdbefc27214396bb3dc9bbbe649e508360b2

scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730.independent.audit.json
  SHA-256 e0303b3bef80d14e9bde85863347b6c78947b212eb159bac77cac005bb29bcd0
  payload c0d0004f3307a4e2918d6a67cf4fe71fa8200d87a0eb67395af3aa2aaccc86f1

scratch/k16_12873_deletebest_joint2.audit.json
  SHA-256 aa2fbf3fe87069f75c4acb33cfcfcb61c4531b991a0054733a83f1f8abf99348
```

The theorem removes one complete half of the exact global radius-two
partition around the fixed upper word.  It does not change the K16 bound.
