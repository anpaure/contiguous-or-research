# Reduction: exhausting all F208 target rows gives the complete root5 pair atlas

Date: 2026-08-15
Status: exact union theorem and complete H100 F208 atlas; definitive solve pending

## 0. Scope

Fix the current root5 defect-cover leaf, its 208-row free set `F`, and the
owner-only quotient conventions of the exact targeted reflection-pair
generator.  A pair configuration is identified by its sorted ten-row
reduced mask.  This identification is exact for the owner ledger because
equal row masks have identical owner action; one literal core/order witness
is retained for physical realization.  Later lower-ticket, phase, or
resource decorations are outside this statement and would require the
correspondingly augmented key.

Let `A(F)` be the set of all quotient-simple, reflection-disjoint q4
period-ten pair masks contained in `F`.  For each `r in F`, let `G_r(F)`
be the complete emit-all catalogue produced with target row `r` and the
same allowed-row file `F`.

## 1. Complete-union theorem

### Theorem 1.1

If every one of the 208 target runs is complete, then

```
                         A(F) = union_(r in F) G_r(F).          (1.1)
```

Consequently, deduplicating the union by the complete sorted ten-row mask
produces the complete allowed root5 pair atlas.

### Proof

Every mask emitted into `G_r(F)` passes the literal quotient-simplicity,
reflection-disjointness, and `C subseteq F` tests, so the right side of
(1.1) is contained in `A(F)`.

Conversely, take `C in A(F)`.  It has ten distinct rows and hence contains
some `r in F` (canonically, choose its least row).  The anchored generator
is complete for every allowed reflected pair containing `r`; therefore
the target run `G_r(F)` emits `C`.  Thus `A(F)` is contained in the right
side.  Deduplication loses no owner-level option because the key is the
entire row mask.  This proves (1.1).  \(\square\)

The argument needs all target runs to use exactly the same allowed set
`F`.  A catalogue produced for F180, F186, F202, or another leaf is not
transferable merely because its target row agrees.

## 2. Finite completeness certificate

A frozen full-atlas artifact should bind the following data.

1. The sorted 208-row allowed file and its SHA-256.
2. For every `r in F`, a completed emit-all catalogue and replay binding:
   target `r`, raw/final counts, report hash, catalogue hash, and the
   assertion that every previously frozen mask through `r` reappears.
   The generator source and binary are bound globally.
3. A union pass that parses all 208 catalogues, rejects any mask of size
   other than ten or not contained in `F`, retains one literal witness,
   and deduplicates by the complete sorted mask.
4. The union atlas, a target-coverage histogram, and SHA-256.  Every atlas
   mask must occur in exactly the ten per-row catalogues indexed by its
   ten rows; this is an especially strong replay check of (1.1).
5. An independent union, tenfold-membership, and literal-witness replay
   that checks the assembled atlas without trusting the merge
   implementation.  It need not repeat the 60,963,840-parameter anchored
   enumeration for every target.

The status labels `frozen` and `new` are pool-relative metadata.  They do
not affect membership in `G_r(F)` and must not enter the union key.

## 3. Definitive root5 exact-cover gate

Once the full atlas is frozen, rebuild the root5 patch instance using:

* the complete self menus in the two destroyed groups;
* every mask in `A(F)` as a pair column; and
* no sampled or target-local pair pool.

Exactly ten compatible choices of the two four-row self menus remain.  In
each branch, delete their eight rows.  The remaining 200 rows must be
partitioned by twenty atlas ten-sets, equivalently by a K20 in the
disjointness graph.

Row 661 lies outside every one of the ten compatible self pairs.  Its
F208 target catalogue has already been generated completely and inserted,
so no later target run can add a new pair mask through row 661.  In the
ten self-branch order used by the frozen K20 manifest, the resulting
full-atlas pivot counts are

| self menus | row-661 pivots |
|---|---:|
| 3309,3361 | 105 |
| 3309,3425 | 97 |
| 3309,3428 | 101 |
| 3309,3429 | 104 |
| 3309,3438 | 106 |
| 3309,3439 | 102 |
| 3316,3361 | 104 |
| 3316,3425 | 94 |
| 3316,3428 | 100 |
| 3316,3439 | 101 |

The total is 1,014 pivots.  An exact cover uses exactly one column
through row 661, whether or not that row has minimum degree.  Thus every
branch is the disjoint union of its row-661 pivot subproblems, each on 190
rows with target K19.  This supplies three independent complete backends:

1. memoized Algorithm X / bitset K19 search on every pivot;
2. an exact-one CNF with one primary variable per residual atlas mask and
   one exact-one constraint per residual row; and
3. a monolithic branch solve as a cross-check.

A SAT pivot witness is combined with its pivot and two self menus and
must replay with load exactly one on all 208 rows.  If all 1,014 pivots
are proved UNSAT over `A(F)`, then all ten self branches are UNSAT and this
is an exact obstruction for the owner-only root5 patch—not a finite-pool
no-go.  Conversely, a SAT witness closes the root5 owner patch but does
not by itself establish lower-ticket or phase compatibility.

## 4. Frozen complete-atlas census

The fixed F208 file has SHA-256

```
f7966bdb17b3ac79a5d13bffc5fe3f76fc78fd3a29a30da0e01e5a4983dbd30c
```

and the leaf9196 instance used to classify `frozen` versus `new` has
SHA-256

```
78b5eff17642880681e156bbecb52405a3254f985b60e8e61fdb033e1979a7c9
```

All 208 target runs completed.  Their exact union is

```
10,006 complete allowed masks = 7,919 frozen + 2,087 new.       (4.1)
```

The per-target record sum is 100,060, and every union mask occurs in
exactly the ten catalogues indexed by its ten rows.  The complete-atlas
manifest, all-mask catalogue, and new-mask catalogue have respective
SHA-256 values

```
b87e920ca6bbb5fdcc94bae5d05a7ead5e03f6a5e3c23000d3173908e7c327f9
973330a5ec497a8a834b8cac8f11797592fdc5d73503cd9e95fc45b435e45a76
6ed4d58e0dc88ab4c394e189395f9ebae650d20ec52ed5c5b3f6fa0fc1e5145e
```

The independent audit replayed 112,153 literal witnesses, checked the
tenfold identity, and returned PASS.  Its SHA-256 is

```
7b58b3f235c82a4217b617bb7cff97bd2d737fa5835d10e50fc3bc03cdfc5369
```

The targeted-generator source/binary and the atlas-builder/audit sources
have respective SHA-256 values

```
861527ebce2d0f6a3aa7edbb070dd5e57ddb832f5a9786bcd12483d904d4db14
2874480130e9e27a71115f82f00c3f4b234da9a8f94b4b9922d8b9a20b57560c
553900a33d9cc37153f5af210d4ea1cf5349e69d18cfa54c4fc8ec673f142f1f
6dc10771c0bd56659997019978f76b6a78f8845f34e65d3119002fe4301a6f07
```

In particular the row-661 catalogue contains exactly 144 masks, all
already frozen and none new.  Its report/catalogue hashes are

```
0b9b89133ab1953f47848cf852dd2ef1d491ed80b1ed345fc8da25a5e7e73459
dc9aab41f80c418f85aa845a6abd126bc6b4fef66394f3d877a2b1ef45ca3dd8
```

This is the direct finite certificate that the 1,014-pivot decomposition
in Section 3 is already the full-atlas decomposition.

Appending precisely the 2,087 new masks to leaf9196 gives the immutable
full-atlas instance

```
/dev/shm/q4z17_reflect_sample0_root5_f208_fullatlas.dat
```

with SHA-256

```
cc97b4fb16040c965f923e6ce9c847e254a0307693d5c2eaec0b616c601c2f3a
```

An independent ordered replay checked the unchanged base prefix, all
2,087 appended masks, uniqueness, containment in F208, and literal
equality of the appended suffix with the new-mask catalogue.  The append
report and clean replay hashes are respectively

```
596636546cbcf88d7ed7a1208ce9a001804e0f26d5808f5fc5b27f2fe1dd5105
2a73e42bee4e3593f40dbdaf8d1481b6e6fec7a92ddece588512e523dc251ae7
```

The clean append-replay source has SHA-256
`3f70cd5587189edfac13a9467e4773585b7df4f11318220784a862cf1ee941de`.

The exact ten-branch graph manifest has SHA-256
`29c490c1cbcb3bb6ff9068e5d950a05f2c633453026a27e546900c1b42344923`;
the complete 1,014-pivot report has SHA-256
`ce5530bf6eb2271af5a3ede31f4a8eaaa283f85bb2e72f26079a6709dd0010a2`.
Every pivot incidence graph is connected and none has an immediate
component-size cut.

## 5. Present backend boundary

The finite sampled campaigns motivated this reduction but do not decide
the full-atlas problem.  On successively enlarged pools:

* deterministic K20 search gave nine finite-pool branch UNSAT verdicts
  and one UNKNOWN on leaf6254;
* two different 311-pivot Algorithm-X passes on leaf8677 returned only
  UNKNOWN at their per-pivot caps; and
* a backend-diverse 311-pivot Sinz/Kissat pass on leaf8942 also returned
  311 UNKNOWN results.

On the complete atlas, a 64-worker seeded Algorithm-X pass gave 1,014
`UNKNOWN` results at 30 seconds per pivot: no SAT witness and no exact
UNSAT pivot.  The campaign summary and independent all-result literal
replay have respective SHA-256 values

```
4d29d90465fad2b22df6788e36f3dc512c58eb500a71fb7c5e48bca5c19a2281
895e12d9dc9a406ae7fa84383dabc89418e724e1027726600234d56149eca30f
```

A monolithic exact CP-SAT run on the same complete atlas also returned
`UNKNOWN` after 601.56 solver seconds (1,089,205 branches and 82,926
conflicts).  Its scoped report has SHA-256
`accb7c1109d1a2daf0b97ea58435d957254199136f180f96b408b9f436aea164`.

An independent 64-worker monolithic CP-SAT run on the same full-atlas
root5 patch also returned `UNKNOWN` after 601.558 seconds, with no primal
witness.  Its report has SHA-256
`accb7c1109d1a2daf0b97ea58435d957254199136f180f96b408b9f436aea164`.

The first three are honest search boundaries over earlier incomplete
pools.  The complete-atlas all-UNKNOWN pass is also only a bounded search
boundary.  The atlas in Section 4 removes the missing-column ambiguity;
the remaining gate is computational exhaustion or a SAT witness for the
1,014 exact subproblems.
