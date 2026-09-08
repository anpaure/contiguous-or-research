# The frozen K16 H1 joint-13 fibre is empty

## Theorem

Let `w` be the authenticated length-12,873 delete-p1 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

and let

```text
S = {0,1,4486,4487,4488,4489,6438,6439,6440,
     12869,12870,12871,12872}.
```

Keep every cell outside `S` fixed and replace every cell in `S` by an
arbitrary nonzero 16-bit mask.  No resulting word covers all 65,535 nonempty
subsets of `[16]` as contiguous ORs.

This is an exact theorem about the whole unbounded-value 13-cell fibre.  It is
not an edit-radius statement.

## 1. Exact localization

The support consists of four disjoint blocks of widths `2,4,3,4`:

```text
[0,2), [4486,4490), [6438,6441), [12869,12873).
```

Fixed-only intervals retain witnesses for 65,480 targets.  Exactly 55 targets
can lose all of their old witnesses.  Safe-gap localization proves that any
new witness for one of those 55 targets lies wholly inside one support block.
The four blocks have respectively `3,10,6,10` internal interval charts, hence
29 charts in total.

The source has the unique hole

```text
H = 11373 = 0x2c6d.
```

Any completion must therefore choose one of the 29 charts as an `H` witness.
The exact five-bit code split into those 29 choices is pairwise disjoint and
exhaustive; codes 29--31 are invalid.

## 2. Canonical normalization

For a proposed completion, choose one witness chart for each residual target.
At a support cell, replace its mask by the intersection of all targets whose
chosen charts cross that cell, or by `0xffff` if no chosen chart crosses it.
This replacement only adds bits to the original cell, remains a submask of
every crossing target, and therefore preserves every chosen witness.

All 55 residual targets contain coordinate 6.  Consequently every normalized
cell is nonzero, and the complete normalized alphabet is the 216-state meet
closure of the residual targets.  Thus an arbitrary-value completion exists
if and only if a completion exists in this finite canonical closure.

## 3. Twenty-two Hall-capacity exclusions

For a block state `s`, let `Gamma_b(s)` be the residual targets that admit at
least one valid chart in block `b`.  If chart `j` in block `b` is selected for
`H`, exact enumeration of all `216^width` block states gives

```text
K(j) + sum_(c != b) M(c,-H),
```

an upper bound on the number of distinct targets assignable to the four
blocks.  The generic H-excluded capacities are exactly

```text
7, 23, 14, 12.
```

For 22 charts the sharp total is below the demand 55.  They are

```text
{0,1,2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,22,23,25,26}.
```

This leaves exactly

```text
{6,15,20,21,24,27,28}.
```

The all-chart capacity calculation was independently replayed from the raw
55-by-29 need ledger, including every maximizing tuple.

## 4. Exact exclusion of charts 6 and 15

The audited 469-variable projection is equisatisfiable with the arbitrary
nonzero-value fibre.  Conditioning its exact 29-way split on chart 6 and chart
15 yields two CNFs of 469 variables and 28,238 clauses.  Both are UNSAT, with
fresh local `drat-trim` verification:

```text
chart 6:
  CNF   a3a7c8110d82053b65369aa034c3d6018c9d06caf6c0140e45bc03ce71411b72
  proof 6c7222b8783defac3055ae8a3bbe954ccfbe1fbccdb3a051750e2d2582f3c0ce

chart 15:
  CNF   c37c0a4c5c79c56f3f7f868cfe6bd5f9786b9e12539e6909f6384e618c2ab54e
  proof 4bc648df2c8b4051ac3bfa2ca652f9e1560885cc7954e98c2b652e545b20dde3
```

## 5. Exact join for the final five charts

For charts `20,21,24,27,28`, scalar capacity is inconclusive.  Two separately
written exhaustive enumerators instead retain the complete family of
near-capacity 55-bit coverage masks for each collar.  They independently
exhaust

```text
216^2, 216^4, 216^3, 216^4
```

tuples and emit identical families.  The four generic family sizes are

```text
17, 4, 4, 114.
```

The final-collar families conditioned on charts `20,21,24,27,28` have sizes

```text
27, 2, 11, 4, 3.
```

An independent Cartesian replay checks every combination that can still meet
the scalar capacity budget.  Its combination counts and best residual holes
are

| H chart | combinations | full covers | minimum holes |
|---:|---:|---:|---:|
| 20 | 81 | 0 | 11 |
| 21 | 4 | 0 | 10 |
| 24 | 22 | 0 | 8 |
| 27 | 8 | 0 | 8 |
| 28 | 6 | 0 | 4 |

Hence none of the final five charts can occur in a completion.

The 22 Hall exclusions, two DRAT exclusions, and five exact joins partition
all 29 possible `H` witnesses.  The frozen 13-cell fibre is therefore empty.

## Scope

This theorem closes the entire specified support with arbitrary nonzero
replacement values.  It does **not** normalize an unrestricted length-12,873
word into this support and does not exclude edits outside `S`.  Therefore it
does not prove `nu(16)>12873`; the exact bracket remains

```text
12873 <= nu(16) <= 12874.
```

## Authoritative artifacts

```text
scratch/k16_h1_joint13_final_unsat_independent_20260730.audit.json
  SHA256 f53a1363230f5892e6ddf0d26d9298c7534d6f61edbbe6b3a1bbe6450aceba3c
  payload ff9317d81903d0c1afaa0565200024caec616a9f0059b70d9d2ff136fa9d9107

scratch/audit_k16_h1_joint13_final_unsat_independent_20260730.py
  SHA256 c352d0a48bb60bdc606bf3d56ac654bc49914130ff12a9b1e26832877537ad3c

scratch/k16_h1_joint13_survivor_exact_coverage_join_20260730.result.json
  SHA256 4b881f6399fcbb0be0374a77cc7d0318982b2b156e7fe66cb32b85d3fabae60a

scratch/k16_h1_joint13_survivor_exact_coverage_join_generic_20260730.result.json
  SHA256 58faffe6b7d2bc4946632220498f13028fa974770020f1237b4b99d60ad92534

scratch/k16_h1_joint13_survivor_join_independent_20260730.audit.json
  SHA256 8e182b21698707f98e975e52b54e73449c090bf7492cf4d407f27337b7b24891

scratch/audit_k16_h1_joint13_survivor_exact_coverage_join_20260730.cpp
  SHA256 2ce315811b6839e0629ae3356ab397a46438dc13a8ab9202b3a5cb1becd870e4

scratch/replay_k16_h1_joint13_survivor_exact_coverage_join_generic_20260730.cpp
  SHA256 be24527c9531d2a883f719d239ca1f1e498ec51b944e8c8943b783460f4f3214

scratch/audit_k16_h1_joint13_survivor_join_independent_20260730.py
  SHA256 d6aec01fbbf2898a484b75dd393a97c25cfed8ffffb00a34c00104c92c8c1914
```
