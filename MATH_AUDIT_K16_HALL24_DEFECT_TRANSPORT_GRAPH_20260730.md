# K16 Hall-24 defect-transport graph

## Scope

This note audits local occurrence transport around the exact carrier

```
scratch/s4_exact229_swap6608_12714_l3_20260730.targets
```

It has length 12,873, exact maximal-envelope middle replay, generalized Hall
deficiency 24, and the sole arbitrary-upper hole `4e79`.  Nothing below is a
global K16 no-go.  The enumerations cover only the explicitly stated token,
block, and forward-rethread move classes.

## Separated defect-transport lemma

Fix the three-flat depth schedule and let `d=3`.  Changing the row at position
`p` can change only envelope positions `p..p+d`, middle equations in the
radius-`d` collar of those positions, and proper-prefix compiler cells meeting
that collar.  Consequently, if changed occurrence positions have pairwise
distance at least eight, their middle effects are disjoint.

Let an occurrence token at source `u` be *compatible* with destination `v` if
putting that token at `v`, with every other row frozen, preserves the flat
schedule and every middle equation in `v`'s dependency collar.  For
pairwise-separated positions `v_0,...,v_(t-1)`, the occurrence cycle

```
q'[v_(i+1)] = q[v_i]  (indices modulo t)
```

is globally middle-exact iff every directed edge `v_i -> v_(i+1)` is locally
compatible.  The forward implication is immediate by restriction to each
collar; the reverse implication follows because the affected collars are
disjoint and every unchanged equation retains its old inputs.

The same factorisation holds for one fixed compiler matching: if each changed
collar retains every matched incidence meeting it, the closed cycle retains
the entire matching.  This is stronger than retaining matching cardinality;
it is used only as a fail-closed Hall-preservation filter.

## Sparse all-upper bad2 census

The carrier

```
scratch/k16_exact229_l3_restore4e79_direct_swaps_20260730/
  uppercomplete_bad2_swap4507_4348.targets
```

is arbitrary-upper complete and has exactly two middle defects: row 4349
misses `0040`, and row 4507 misses `0044`.

The exact separated-cycle census through both defect collars, up to eight
vertices, found

```
expanded     48,912,619
closures          2,099
middle exact       2,099
all upper              0
```

Nine exact cycles have one upper hole.  One nontrivial branch transports the
hole from `4e79` to `2f4b`; a second exact facet-return cycle then gives two
middle-exact/all-upper carriers.  Their full generalized Hall deficiencies
are 53 and 56, so neither preserves the Hall-24 gain.

Adding the fixed-reference-matching filter collapses every separated cycle of
at most ten vertices to the trivial swap-back, which is exact but again misses
`4e79`.  This is a no-go only for preservation of that fixed matching by
separated token cycles; a different maximum matching or interacting collars
are outside its scope.

Two further bounded interacting faces are closed:

* equal-length cross-collar block exchanges of length at most 64:
  366,080 tested, four middle-exact, zero all-upper;
* equal-length interacting local blocks of length 3..16 and gap 0..6:
  5,037,984 formal moves, 585 middle-exact, zero all-upper.

The corresponding raw summaries are in
`scratch/defect_transport_sparse_bad2_20260730/logs/`.

## Exact upper-return cycles from S4

Unprotected occurrence-block cycles from S4, using blocks of length at most
eight and at most six cycle vertices, produce only three exact/all-upper
returns.  They are the forward exchanges at the same two shores
`6608 <-> 12714`, of lengths 3, 6, and 8.  Their full Hall deficiencies are
25, 25, and 26.  No incoming occurrence block of length at most 12 can create
the missing `4e79` seam while locally retaining the fixed Hall-24 matching.

The complete single forward-block rethread census independently gives the
same qualitative result: 565,369 facet-forced moves, 256 middle-exact, three
all-upper, with Hall deficiencies 51, 58, and 61.  See
`MATH_THEOREM_K16_HALL24_FORWARD_BLOCK_RETHREAD_NOGO_20260730.md`.

## A Hall-preserving upper-debt migration

There is a second authenticated Hall-24 state:

```
scratch/defect_transport_sparse_bad2_20260730/pass1_hallswap16/
  hit_14.targets
```

with SHA-256

```
9f78f5ac6bd0348d9309985884ec55c5825dfe1921a71b8f2d47494809910536
```

It is middle-exact, has full Hall deficiency 24, and its sole upper hole is
the rank-ten mask `4e7e`.  Thus the block exchanges transport the upper debt
without changing its size.

The literal lower-zero/upper-hole accounting is sharper.  Relative to the
ten persistent lower zero-providers common to this face:

| carrier | extra lower provider | lower zeros | upper holes |
|---|---:|---:|---:|
| exact229/all-upper | neither | 12 | 0 |
| S4 | `4e70` | 11 | 1 (`4e79`) |
| `hit_14` | `8000` | 11 | 1 (`4e7e`) |
| every audited all-upper return | neither | 12 | 0 |

Hence the best local states obey

```
(number of zero-provider lower targets) + (number of upper holes) = 12.
```

The common shared-component contribution is 13 in the sharp cases, giving
Hall 24 when there are 11 zero-providers and Hall 25 when there are 12.  The
single-move classes seen here transport one defect quantum between upper
coverage and the extra lower provider; they do not annihilate it.

For `hit_14`, the endpoint-complete global two-block return census through
length 32 tested 495,790 exchanges.  Fifty-six are exact at both collars and
ten are all-upper.  Their full Hall deficiencies are 25 or 26.  The complete
forward-block census tested 9,197,855 endpoint-signature triples, found 1,019
middle-exact and 17 all-upper carriers, with best Hall deficiency 28.  See
`MATH_AUDIT_K16_HALL24_4E7E_FORWARD_RETHREAD_NOGO_20260730.md`.

## Two overlapping rethreads break the one-move plateau

The bounded two-shore BFS subsequently found four exact, arbitrary-upper-
complete states with generalized Hall deficiency 24.  Each is the composition
of two **forward** equal-block swaps from exact229:

```text
first  [6611,6611+L) <-> [12718,12718+L)
second [6613,6613+l) <-> [12721,12721+l)
```

| file | `(L,l)` | target SHA-256 | Hall JSON SHA-256 | incidences | shore |
|---|---:|---|---|---:|---:|
| `pass_33` | `(16,9)` | `2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec` | `73a8538d97fe38a94cba661f8d67e7d20282302c6f97c87df61eda48cc584e8f` | 347649 | 211/187 |
| `pass_35` | `(18,9)` | `42420e0eea7102a07227b25e49663a127f89219b8c41cb18ee7de699385d9b04` | `b6ba25add99a7d49913f4c5914696970a19574b266a9d2ca9c8ba13542e9ca42` | 347649 | 198/174 |
| `pass_46` | `(16,13)` | `bf3ee02110f70c168dc9863e1c8258cc54debfa408dd4c97fe5b57c6a4116754` | `fce8c051d7e7d0f3ce7aaf035d6d0d3c0207614c25b1f8b902d5502669a127a8` | 347809 | 211/187 |
| `pass_55` | `(18,15)` | `e1166c6ae5f6c671c779bfb9f692fa8332aa7b9978cfcd93671b64244c5f1f69` | `a60e4d99a31f6ec73b7e3a973e7ff7e83c831f133a05085f092aa072b99fa65e` | 347737 | 198/174 |

All four have capacity 32063, fixed flats `6320,12869,12871`, no upper
hole, and the same eleven zero-provider lower masks

```text
2665 28e9 291d 29a9 2f28 4879 48e9 4e70 6989 6a29 6c70.
```

Thus `8000` remains provided while `4e70` is not; the shared-component term
is still 13.  In particular the composition attains `(Z,H)=(11,0)`, breaking
the single-move relation `Z+H=12`.  This is a genuine defect annihilation,
not another transport of the upper hole.

The full fixed-start parameter family was then enumerated without a length
cutoff: `1<=L<=155`, `1<=l<=152`.  Of 23,560 pairs, 5,469 are exact and 505
are exact plus arbitrary-upper complete.  Fresh full Hall replay on every one
gives

```text
deficiency 24:  63
deficiency 25: 239
deficiency 26: 203.
```

For all 505 carriers, `deficiency = Z + 13`; no member creates a second
provider or lowers the shared term.  The 63 Hall-24 members are exactly the
`Z=11` rows.  This closes the complete two-fixed-start forward family below
24 while exposing 63 authenticated bases for a third compensating overlap.

### Complete length-64 third-overlap shell

From each of those 63 Hall-24 bases, enumerate every forward equal-block
third swap of length at most 64 such that each of its two blocks intersects
the corresponding support of the first two swaps.  Starts and length vary
independently; no three-row collar restriction is imposed.  Fixed-flat and
changed-flat cases are separated only for speed, and their union is the
complete stated family.

The fixed-flat census gives

```text
tested forward swaps                       50,221,716
middle exact                                  306,886
middle exact + arbitrary-upper complete        26,501
distinct exact + upper carriers                21,414

full Hall deficiency 24                         1,290
full Hall deficiency 25                         7,603
full Hall deficiency 26                        12,521
```

Every distinct exact/upper row receives a fresh full maximum matching.  Zero
provider counts are `11:1290, 12:7623, 13:12501`.  The shared term is 13 in
21,394 rows and worsens to 14 in 20 rows; it never drops below 13, and no row
has ten zero providers.  Hence none improves Hall 24.

The complementary changed-flat census has 393 dynamically middle-exact
rows and **zero** arbitrary-upper-complete rows.  Therefore the complete
stated third-overlap shell contains no Hall-below-24 admissible carrier.

Reproducer and compact outputs:

```text
scratch/search_k16_exact229_overlapping_forward_swaps_hall_20260730.cpp
  SHA c0a7655045679a874e626003d4a6bbc855e70486f70715757d5e56ef1198c115
scratch/defect_transport_sparse_bad2_20260730/overlap_exact_census_20260730/
  two_v4.tsv             SHA 06112c8b5e69ee2fc9844917a4d5cc43b97ce893e91a026739bf59342a81e5fb
  third63.tsv             SHA 11f11700689ff37bb6a15574a94200080dc13265118b442ace8702dce4e7e4a5
  third63_dynamic.tsv     SHA d381ae062f3a835b96d46a8d69cd6c38845c7617d4148263431c9caa47c5610c
scratch/audit_k16_exact229_overlapping_forward_swaps_hall_20260731.py
  SHA 4a9ba2548dd85b3e4a391a5c0d65000f79975ee1a57a47473573e4f964c95d4d
scratch/k16_exact229_overlapping_forward_swaps_hall_20260731.audit.json
  SHA 9e8170fd87db87b7f8bd5e6b3f148a9e01bc6c5de9b1ff238772fa701321ab73
  payload 1008412cb52dbe8ce19bee28e6995546d9b1d73e048124f5fd8df48beb8d77e1
```

## Hall 23 exists before upper closure

There is nevertheless a real lower improvement immediately adjacent to this
family.  On any of the four short Hall-24 carriers, append the forward swap

```text
[6608,6611) <-> [12714,12717).
```

The result is middle-exact, retains the `8000` provider, creates a `4e70`
provider, and has full Hall deficiency

```text
23 = 10 zero-provider targets + 13 shared-component units.
```

It is not admissible: its unique upper hole is `4e79`.  Protected facet
returns by one equal-block move, arbitrary protected 3-cycles, a protected
relief-collar 4-cycle family, direct halo exchanges, and the natural
three-block circulation have all been exhausted without an exact return.
Thus Hall 23 is physically real, but the next operation must restore `4e79`
while preserving both occurrence-labelled lower augmentations.  See
`MATH_AUDIT_K16_NESTED_COMMUTATOR_HALL23_THIRD_SWAP_20260731.md` and
`MATH_AUDIT_K16_HALL23_PROTECTED_FACET_4CYCLE_NOGO_20260731.md`.

## Consequence

Single rethreads in the completed move classes consume the one extra lower
provider when they close the upper debt.  Two overlapping rethreads can avoid
that loss, and the complete fixed-start family contains 63 Hall-24/all-upper
states.  A third adjacent swap reaches Hall 23 but owes upper mask `4e79`;
the complete length-64 all-upper third-overlap shell stays at 24 or worse.
Further progress therefore needs at least one of:

1. a third compensating overlap that creates a second independent lower
   augmentation;
2. a move that lowers the shared-component term 13;
3. a move that changes the maximum matching rather than retaining the frozen
   one locally; or
4. another parent carrier.

No length-12,873 universal word is claimed here.
