# K16 V/V TH495 one-hole basin and exact radius-one no-go

Date: 2026-07-31  
Status: **authenticated one-hole basin; exact unrestricted two-substitution
no-go; full 18-cell fibre now solver-free UNSAT by immutable ghost**

## 1. Source and deletion

The independently authenticated V/V `5/9/5` 19-cell SAT control is

```text
scratch/k16_raw_splice_19cell_sat_control_20260730/candidate.word
SHA-256 d08b7a96dbe5ccf97a59e4557971b582f91230eded4204f0da8ca050392a6d9b
```

and is a literal universal K16 word of length 12,874.  Both fixed bodies are
cut from the authenticated parent

```text
answers/k15.word
SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b.
```

Deleting zero-based physical position `1` gives

```text
scratch/k16_vv_th495_deletep1_onehole_20260731.word
SHA-256 e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676
```

of length 12,873.  Complete literal replay gives exactly one hole:

```text
0x2c6d = 11373.
```

The eighteen free positions and three windows are exactly

```text
[0,4) union [6434,6443) union [12868,12873),
sizes 4/9/5.
```

The two frozen bodies are literally

```text
word[4:6434]       = X[6:6436],
word[6443:12868]   = z union X[7:6432].
```

Thus this is a genuine one-hole incumbent in the V/V TH495 fibre of the raw
splice ledger, not merely a near-word with a similar score.

The complete deletion census over the nineteen control cells has hole counts

```text
2,1,4,2,8, 8,8,7,5,5,4,3,8,11, 7,6,3,4,2,
```

in physical free-position order.  Position `1` is the unique one-hole
deletion.

## 2. Distinctness from the active collar594 basin

The prior one-hole word is

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

with window sizes `5/9/4`.  The new and old words are not related by any
coordinate permutation, reversal, or cyclic reindexing.  Indeed, coordinate
permutations preserve the complete sequence of cell cardinalities, while
reversal/cyclic reindexing only reverses/rotates that sequence.  The audit
checks every forward and reversed cyclic offset and finds none.  Relabelling
the three window names does not change the physical word, so it cannot alter
this conclusion.

This is therefore independent finite evidence, not another presentation of
the old delete-p1 basin.

## 3. Exact target-closure domain

The fixed bodies cover 65,475 masks and leave a residual family `R` of size
60.  For a nonzero editable value `v`, normalize it to

```text
intersection {t in R : v subset t},
```

and send a value contained in no residual target to the live sentinel `1`.
Exactly as in the collar594 target-closure theorem, this preserves every
chosen residual witness and hence preserves fibre feasibility.

The exhaustive 16-bit census gives

```text
live nonzero masks                 9,647
dead nonzero masks                55,888
live value-target containments    30,582
nonzero closure-fixed values         320.
```

The domain is therefore **larger**, not smaller, than the 245-value domain of
the old collar594 basin.  The smaller residual target count (60 versus 61)
does not imply a smaller closure lattice.

## 4. Exact one-substitution theorem

### Theorem 4.1

No word obtained from the authenticated V/V TH495 one-hole word by replacing
at most one physical cell with an arbitrary nonzero 16-bit mask is universal.

### Proof by complete finite census

Any successful replacement must belong to a new interval whose union is the
old hole `0x2c6d`; therefore the replacement is a nonzero submask of that
hole.  There are `2^8-1=255` possible values.  The independent C++ census
checks all

\[
                    12,873\cdot255=3,282,615
\]

position/value pairs.  At each position it computes exact multiplicities of
all intervals destroyed by removing the old cell and exact side-OR joins of
all intervals created by the new cell.  It finds

```text
hole-installing rows    26,438
universal rows               0.
```

The sharp best row is

```text
position 6440: 0x806d -> 0x046d,
```

which installs `0x2c6d` but leaves exactly the new hole

```text
0xa86d = 43117.
```

An independent Python event-ledger implementation restricts immediately to
values contained in every target whose old witnesses all use the edited
position.  It checks 76,420 feasibility-relevant position/value rows and
also returns zero completions.  Its narrower diagnostic debt statistic is
not used for sharpness; the full literal C++ census supplies the sharp
one-debt row above.  This proves the theorem.  QED.

## 5. Exact radius-two theorem

### Theorem 5.1

No word obtained from the authenticated V/V TH495 one-hole word by changing
at most two distinct physical cells to arbitrary nonzero 16-bit masks is
universal.

### Proof

For the sole input hole, any final witness either contains exactly one of the
two changed sites or contains both.

* In the first case, that site's edit alone already supplies the input hole.
  The patched provider-first engine enumerates all 26,438 such first values.
  For every intermediate word and second site it computes the **true target
  core**: the intersection of the intermediate holes and all represented
  targets whose every witness passes through the second site.  The maximal-
  value theorem reduces each site to that core (plus incumbent-core coatoms).
  The complete run visits 247,044 second sites, computes 242,513 nonzero
  target cores, performs 228,596 maximal tests and 61,396 coatom tests, and
  finds no completion.
* In the second case, every witness of the input hole contains both edits.
  The exact all-joint engine enumerates 13,177 possible position pairs and
  100,771,016 ordered value pairs.  It computes every target whose complete
  old witness family meets the changed sites and checks the exact new
  interval labels.  It also finds no completion.  The sharp rows still owe
  one mask, again `0xa86d`.

These cases are exhaustive.  An independent composer reconstructs the
13,177 all-joint supports, materializes every retained sharp diagnostic row,
and replays its complete hole set.  Therefore the two branch results prove
the theorem.  QED.

## 6. Scope and superseding fixed-fibre theorem

The radius-two result alone proves only that a completion would have to
change at least three incumbent cells.  A later, independent deadline
argument closes the complete V/V TH495 18-cell fibre.  The two immutable
fixed-body triples `[11726,11728]` and `[12826,12828]` first-deliver the same
rank-eight target `0xc279` at distinct deadlines.  Every assignment to the
eighteen free cells therefore has a ghost `G>=1`, whereas every universal
K16 word of length `12873` has `G=0` by

\[
 26332\le(3-G)(12873+G).
\]

Thus the full fixed fibre is solver-free UNSAT.  The one-hole word and its
radius-two no-go remain valid calibrations.  A successful equality collar
retaining these bodies must enlarge its editable support to meet at least one
of the six positions in the two triples.  This does not prove an unrestricted
K16 lower bound.

The global bracket remains

\[
                         12873\le\nu(16)\le12874.
\]

## 7. Frozen artifacts

```text
scratch/audit_k16_vv_th495_deletep1_onehole_20260731.py
  SHA-256 5fade619ca2adb31cee26b188df8d9f078cc23588e25645b19e60d1c9b769955
scratch/k16_vv_th495_deletep1_onehole_20260731.audit.json
  SHA-256 582d66801ed16884a77fa06a61680839c4eaa59248675f37dbde567ee0e42788
  payload 77ae626864cd5cdbf92c79a04f8a316ba4c7daa3c883be279160bfad104b1e12

scratch/audit_k16_vv_th495_onehole_one_substitution_exact_20260731.py
  SHA-256 0d1ef4587e04ff79294d4f86453e9ad429a8c3f002dea2be95e0bbaa7a7dc576
scratch/k16_vv_th495_onehole_radius1_20260731/radius1.audit.json
  SHA-256 e052350b75dec9d3aeb8d6abf753a23415fcd1effd00af33a02f499ba88c1412
  payload 12b0530571b94931fdd277d43febfb7695fbe7802eff1924e8f82fafd7953fff

scratch/search_k16_one_substitution_completion_20260730.cpp
  SHA-256 1b50ccc2491c1985cbff118949eedf0e83fd669585f304a09872acb81ad91c4d
scratch/k16_vv_th495_onehole_radius1_20260731/independent.stderr
  SHA-256 5398f07a163b80f771714142e8f0c156c4b72c9ad8f2d516866b35188ab26b40

scratch/threadD_search_k16_upper12874_d3_provider_core_20260731.cpp
  SHA-256 7b1c17bbd1276a8cd4184e47f56dc4e6c66f84cc084bd155a4896ec308acd9aa
scratch/k16_vv_th495_radius2_20260731/provider.audit.json
  SHA-256 ab50f2c88afe1e1edc71a8568cae6ef9383ec4ab2aa7348bc64dd8a13b3fc62c

scratch/search_k16_exact_joint_two_edit_multihole_20260730.cpp
  SHA-256 aded0eecdc8e62dec044c4c05752a23c2c64c1fb1e93711fe776b2ec2f4bbff3
scratch/k16_vv_th495_radius2_20260731/alljoint.audit.json
  SHA-256 ad80007fb458e3e9c5c0ce771af93608d12b6d7ae57a0bdceecce5bfea2b1eeb

scratch/audit_k16_vv_th495_radius2_composed_20260731.py
  SHA-256 a12a4e97db7923f00c3c865c04b500719ac7736294a3e5e9bf46c3050f0d0d52
scratch/k16_vv_th495_radius2_20260731/composed.audit.json
  SHA-256 3797147349b32c5ba1adc90e4ac1c3cb9ce0b596190b6fcbfa2210ca14c10bbb
  payload f643fecd26e3bb73d88d4db0be69ff60f6796b970a21726a252a0836cf258017
```
