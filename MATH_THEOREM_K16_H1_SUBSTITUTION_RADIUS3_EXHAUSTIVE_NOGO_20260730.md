# K16 H1: exhaustive substitution-radius-three no-go

Date: 2026-07-30

## Theorem

Let

```text
F = scratch/k16_h2_to_h1_p0.h1.word
```

be the 12,873-cell word of SHA-256

```text
ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a.
```

Its only uncovered nonzero 16-bit mask is

```text
B = 11373 = 0x2c6d.
```

There is no universal word obtained from `F` by replacing at most three
distinct cells by arbitrary nonzero 16-bit masks.  Equivalently, the complete
fixed-length substitution ball of radius three around `F` contains no
length-12,873 solution.

This is a local theorem about one authenticated word.  It does **not** rule
out an unrelated length-12,873 word, insertion/deletion, a cyclic cut or
rotation of a different source, four or more replacements, or any global
rethreading.

## 1. Exhaustive witness-support partition

In any completion, choose a final interval witnessing the source hole `B`
and minimize how many changed cells it contains.  That number is 1, 2, or 3.

### Three changed cells

All fixed cells between the three sites are `B`-submasks.  The exact source
census has 13,779 possible supports.  A private-target relaxation excludes
13,772; an exact shared-value OR-state DP empties the remaining seven.  Hence
no final `B` witness uses all three edits.

### Two changed cells

The two witness cells form an exact `B` packet and the third replacement is
arbitrary.  The exhaustive census checks

```text
13,310 positional packets,
105,510,990 ordered replacement pairs,
2,308,914 feasible third positions, and
9,667,813 feasible third values,
```

with an exact three-site multiplicity delta.  None completes the word.

### One changed cell

Changing the one witness cell alone must already supply `B`; otherwise the
chosen final witness would contain another changed cell.  The exact portal
atlas contains 28,805 such substitutions, every one with a nonempty debt set
of size 2 through 20.

Fix a portal and call the two remaining repair sites `P,Q`.  Because every
portal debt is uncovered before those repairs, each debt's final witnesses
use `P` only, `Q` only, or both sites (`J`).  Thus each debt has one of the
seven nonempty supplier states

```text
P, Q, J, PQ, PJ, QJ, PQJ.
```

If every debt has a `J` witness, the all-joint census applies.  It exhausts

```text
372,365,874 positional supports,
49,390 structurally feasible supports, and
144,191,783 exact value pairs
```

with no completion.

Otherwise some debt has no `J` witness.  Its nonempty state contains `P` or
`Q`, so orient one individual supplier first.  This is precisely the mixed
provider-first branch.  The finite identity

```text
7^d = 4^d + (7^d - 4^d),       2 <= d <= 20,
```

is an exact partition: `4^d` is the all-joint class, and every complementary
pattern has an orientable individual supplier.  The independent partition
audit explicitly enumerates all patterns through `d=7` and checks the closed
form through `d=20`.

These cases are mutually covering even when a completion has several `B`
witnesses: choosing one of minimum changed support places it in at least one
branch above.  Solutions using fewer than three genuine substitutions are
included automatically.

## 2. Exact mixed provider-first census

For each of the 28,805 portals, for each remaining position, the search takes
the union of the exact one-cell provider intervals over the portal debts.
After applying a provider value it computes the exact intermediate hole set
by multiplicity delta.  A last site `s` can supply every current hole `T` only
with a value in the Boolean interval

```text
L_s = OR_T (T \ c_s(T))  subseteq  z  subseteq  AND_T T = U_s,
```

where `c_s(T)` is the maximal fixed `T`-compatible context through `s` in
the actual two-edit word.  If the incumbent singleton target at `s` is its
sole remaining occurrence, the same exact interval condition is added for
that target.  Every surviving triple is decided by the full three-site
multiplicity delta.

The complete H100 run covered the unsharded portal interval `[0,28805)` and
returned

```text
status                                      PASS_EXHAUSTED_NO_COMPLETION
provider values                             16,205,107,090
partition survivors                         15,662,724,196
exact pair deltas                            15,662,724,196
nonempty-intersection intermediates          15,365,881,034
candidate final positions                         1,618,340
candidate final values / exact triples            4,062,667
deduplicated <=8-hole catalogue rows                466,228
authenticated completions                                  0.
```

It used 16 threads, 9,207.64 seconds wall time, and 2,434,364 KiB maximum
resident memory.  Exit status one is the program's intentional
exhausted-with-no-solution return.

## 3. Independent replay and union audit

The independent audit does not include the mixed-search source.  On a
deterministically permuted sample from all 466,228 retained small-hole rows it

* literally recomputed 64 pair hole sets from all contiguous intervals;
* compared 64 optimized seed-plus-affected-component position sets with a
  brute scan of every physical cell, covering 25,874 brute positions;
* literally replayed 128 admitted final values; and
* literally replayed 128 values rejected by the unique-old-occurrence filter,
  confirming that the old target is indeed lost.

All checks passed.  The final Python union audit independently replays the
source word, authenticates every branch artifact and counter, checks the
supplier-pattern partition, and emits

```text
PASS_EXHAUSTED_NO_COMPLETION_WITHIN_THREE_SUBSTITUTIONS.
```

This proves the theorem.

## 4. Frozen artifacts

```text
scratch/k16_h2_to_h1_p0.h1.word
  ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a

scratch/k16_ejection_h1_one_cell_portal_atlas_20260730.audit.json
  87107b1bc77159058be6f1bafebfed9006da800b54052158acfcf41a1c6777ba
scratch/k16_ejection_h1_allthree_solverfree_20260730.audit.json
  1208e544bf386d3b8e39f85721499d0694c6eb860f34262a9d6eb6a1c6f6e209
scratch/k16_ejection_h1_two_site_plus_one_complete_20260730.audit.json
  7973b6041da36d718e1febae6d183b5181ba41015af8391f865a7b86c21d2e8c
scratch/k16_ejection_h1_one_site_plus_joint_pair_complete_20260730.audit.json
  14aebcd50344894cbd423306299ac0d997571cac66a8b4dfe9ff96aa429244e4
scratch/k16_h1_radius3_supplier_partition_20260730.audit.json
  38e415593f0f777d9d8329d529ce553f75dd0cc573a5785e871737ccb595ad5b

scratch/search_k16_ejection_h1_mixed_provider_first_complete_20260730.cpp
  feacfd79d7f99aa1c475ebb8e7e569e76f274db6b0819e23aca601e41b33b94e
scratch/k16_ejection_h1_mixed_provider_first_complete_20260730.audit.json
  277dbccaf30fdb2077bebac23969b7b981173d0a4b7ae776d73d7e57116bd191
scratch/k16_ejection_h1_mixed_provider_first_complete_20260730.resource.txt
  507613f50e196f8bb11c808c42b8d6b5ba2f5e841a2d7711ee61321e6ce25123

scratch/audit_k16_ejection_h1_mixed_cap8_independent_20260730.cpp
  c4cb558f81db44cb8af97eb6ce8517d84315990d6fe51fbbb0cf97d7093d5ba3
scratch/k16_ejection_h1_mixed_cap8_independent_20260730.audit.json
  cea3b87be8794246bc62cbba1d70a3bb733a9ddba65b24e31725997bc67f1114
scratch/k16_ejection_h1_mixed_cap8_independent_20260730.resource.txt
  ee23b04069d7eab6ca6c2db3121953aac6e587c2959a3a933c86f8f32a10713c

scratch/audit_k16_h1_radius3_exhaustive_union_20260730.py
  d87e1fbc72592f85ff6e121a1c0f31492fa4d085d17f8f5d7babf7982c87dc93
scratch/k16_h1_radius3_exhaustive_union_20260730.audit.json
  6bfbe947923533980bb126f6e84237b7360bbcb597200134faad956ee293e749
  payload 6370036de60b8aba19c3071809c6b8df8ec252a92d0ad8c8147f14ad0cbe671a.
```

The exact global bracket remains

```text
12873 <= nu(16) <= 12874.
```

