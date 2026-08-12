# K16 upper 12874 and the exact one-cell compression gate

Date: 2026-07-30  
Lane: R  
Status: authenticated upper bound; exact deletion, fusion, radius-one, and
radius-two theorems, plus one closed radius-three branch.  The bounded 4/9/4
collar attempt ended `UNKNOWN` and is not a theorem.

## 0. Headline

The literal word

```text
answers/k16_upper12874.word
SHA256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
length 12874
```

covers all `65535` nonzero masks.  Together with the established counting
lower bound this gives

```text
12873 <= nu(16) <= 12874.
```

The exact best deletion is position `1` (zero based).  It gives

```text
scratch/k16_upper12874_best_delete.word
SHA256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
length 12873
sole hole 11373 = 0x2c6d.
```

No single substitution completes that word.  Exhaustive arbitrary
two-substitution scans also find no completion, but their joint-witness class
reaches a new one-hole state with sole hole `43117=0xa86d`.  The complete
one-cell continuation of that closest state returns to `11373=0x2c6d` and
does not close.  The all-three-site radius-three class is also excluded
below.  Thus the live finite target is specifically a one-site-plus-two-
repair or two-site-plus-one-repair branch, or a wider exact collar—not
another deletion or one-cell portal.

## 1. Independent authentication of the upper bound

An ending-OR recurrence starts with the singleton at each position and merges
the distinct OR states from the preceding position.  It finds all `65535`
nonzero labels; at most eleven suffix states occur at any endpoint.  A
separate start-by-start replay agrees.  The full independent audit is

```text
scratch/ad_k16_upper12874_phase_collar_independent_20260730.audit.json
SHA256 dc800a738a0c771a50c01dd9b8cfb39df6e3b4e25769f713814d0926b5b458ea

scratch/audit_ad_k16_upper12874_phase_collar_independent_20260730.py
SHA256 daa12d77fe5ca736136fd06d70635b77aa91c56eed195ddd337a7b0cf0d2122e
```

The answer was decoded from the exact 5/9/4 collar model.  That model lists
eighteen editable positions.  Exactly twelve values differ from the source
and six retain their incumbent values.  The four positions added beyond the
older 4/7/3 list are editable positions, not four additional actual changes.
The twelve changed zero-based positions are

```text
0, 1, 3, 4, 6436, 6438, 6439, 6440, 6442, 12871, 12872, 12873.
```

## 2. Exact deletion theorem

### Theorem 2.1

No single deletion of the authenticated 12,874-cell word is universal.
Exactly one deletion has only one hole: deleting position `1`, whose value is
`0x2800`, leaves the sole hole `0x2c6d`.

### Proof

Fix a deleted position `p`, its cell `d`, a nonempty suffix OR `l` of the
left part, and a nonempty prefix OR `r` of the right part.  The old intervals
meeting `p` have labels

```text
l OR d OR r,
```

where either side may be empty.  The new crossing intervals have labels
`l OR r`, with both sides nonempty.  All other intervals are unchanged.
The audit stores the suffix and prefix OR chains with their physical
multiplicities, applies this exact subtraction/addition ledger for every one
of the 12,874 positions, and directly replays the unique optimum.

Its hole-count histogram is

```text
1^1, 2^3, 3^3, 4^184, 5^931, 6^1638, 7^1889, 8^1995,
9^1655, 10^1132, 11^774, 12^639, 13^738, 14^499,
15^366, 16^190, 17^176, 18^3, 19^58.
```

Therefore the stated optimum is exhaustive.  QED.

The frozen artifacts are

```text
scratch/k16_upper12874_deletion_census.audit.json
SHA256 c2990f25c9ef15d7c3a4ddc5eda5f5ca4ce60e75dabe93dfc8c4988b349cd619

scratch/audit_ad_k16_upper12874_deletion_census_20260730.py
SHA256 fc8ce6aec17be6ad7a0bb072fd04332361394896e7dbe4312d55178656baf348
```

## 3. Exact adjacent-fusion theorem

There are two natural meanings of fusing adjacent cells.

### Theorem 3.1 (OR fusion)

Replacing any adjacent pair `(x,y)` by the one cell `x OR y` never produces
a universal word.  The minimum residual is two holes and is attained at two
positions.

Indeed, intervals containing both old cells correspond bijectively, with the
same OR, to intervals containing the fused cell.  Only old intervals ending
at the left cell or beginning at the right cell disappear.  The exact census
over all 12,873 pairs has minimum rows

```text
p=0: holes {11373,18553};
p=2: holes {5229,21613}.
```

### Theorem 3.2 (arbitrary one-cell fusion)

Even if the fused cell is an arbitrary nonzero mask, no adjacent two-to-one
fusion is universal.  Exactly nine fusion operations have only one hole, and
all nine leave `11373=0x2c6d`.  They produce eight distinct words: the
position-zero operation below coincides with the position-one operation with
replacement `0x2069`.

```text
p=0: z=0x4879;
p=1: z in {0x2008,0x2009,0x2028,0x2029,
           0x2048,0x2049,0x2068,0x2069}.
```

### Proof of Theorem 3.2

Write the old word as `A x y B`.  For a fixed adjacent pair, let `R` be the
targets which have no occurrence wholly inside `A` or wholly inside `B`.
These are exactly the targets which the new fused cell must resupply.  A
candidate `z` is universal precisely when, for every `T` in `R`, some suffix
OR `a` of `A` and prefix OR `b` of `B` (empty sides allowed) satisfy

```text
a OR z OR b = T.
```

Any feasible replacement `z` is a submask of every member of `R`, hence

```text
z subseteq U := intersection(R).
```

If some `z` works, replacing it by `U` preserves each of its witnessing
contexts: `U` has no bit outside the target and only adds target bits.
Thus it is enough, and is exact, to test the single maximal value `U` for
each adjacent position when deciding universality.

More generally, if `z` leaves at most one hole `S`, then it works on
`R minus S` and is a submask of

```text
U_S := intersection(R minus S).
```

The same monotonicity proves that `U_S` works on every target on which `z`
works; the intersection of an empty family is understood as `0xffff`.
Testing `U` and every leave-one-out `U_S`, followed by direct replay
of every nonzero submask of each successful maximal value, therefore lists
every zero- or one-hole fusion value.  The audit finds no zero and exactly
the nine operations displayed above.  QED.

Artifacts:

```text
scratch/k16_upper12874_adjacent_fusion_census_20260730.audit.json
SHA256 8f8441844dff8470723566f38818d0e17da2af81fe66dbbd007e9040cdb6195e
payload 2b35f6e62cdf264f39425b07d55e47b522e16d0094951326d863a553a100516e

scratch/audit_k16_upper12874_adjacent_fusion_census_20260730.py
SHA256 6a4089b4599fc174d4ebc1a126a6210db19ed36577f0562bbe3a14d45cbc20e6

scratch/k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.audit.json
SHA256 9c9451aa69f80778ec0843dbb4471757ce779d9678a43ed6f97161a99bf7597a
payload 02ecfdcdd561fd7bd727154ade27eb3bb561f60404da9ae94409e92390ba9861

scratch/audit_k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.py
SHA256 deade2971c563312153b47ff6d6b2b6202daa8c38331507d621fc33bdf9ad279
```

An implementation-independent replay of the extremal rows, including the
only repeated extremal target multiplicity, is recorded in

```text
MATH_AUDIT_R_K16_UPPER12874_ADJACENT_FUSION_CENSUS_20260730.md
SHA256 e3484a2cb9180060e20a1341049ac647bf0db8ba391ed696f9615f0635fe91b3.
```

These theorems freeze every other cell.  They do not exclude deleting or
fusing one cell while simultaneously rethreading additional cells.

## 4. Exact radius-one theorem at length 12873

### Theorem 4.1

No word obtained from the best deletion basin by at most one arbitrary
nonzero substitution is universal.

### Proof

For each target, intersect all its old occurrence intervals.  At position
`p`, only the targets whose every old occurrence contains `p`, together with
the old hole, need a new witness through `p`; every other target retains an
untouched occurrence.  If the replacement is `z`, then `z` is a submask of
every target in this active set.  Every affected new interval has the form

```text
left_suffix_OR OR z OR right_prefix_OR.
```

The audit enumerates all distinct left/right bases and every nonzero submask
of the active-target intersection.  This is necessary and sufficient.  It
tests 77,153 assignments and finds no universal word.  QED.

The independent artifacts are

```text
scratch/k16_12873_phase_delete_radius1.audit.json
SHA256 475f35023004eb7402bfb7da42135b26f277a8bf3ccf3eb904b89af4d31196f2

scratch/audit_ad_k16_12873_phase_delete_one_substitution_exact_20260730.py
SHA256 cbfcce2d1d52904364b260b0507875fe59df96ded8ee46b138b7a01591cf6ec6
```

The complete common-provider ledger has 27,064 assignments.  Its minimum
debt is one, attained by exactly sixteen values at position 6440; every one
transfers the hole to `43117=0xa86d`.

### Theorem 4.2 (all low-hole deletion basins plus one edit)

The complete deletion census has exactly seven positions whose deletion
leaves at most three holes:

```text
p=0:     {18553,26745}
p=1:     {11373}
p=3:     {5229,21613}
p=6389:  {18041,27233,27489}
p=6441:  {37997,43117,54381}
p=12871: {35943,36071,48367}
p=12873: {52833,52835}.
```

For each basin, earliest-end/latest-start occurrence extrema give the exact
necessary replacement domain at every position.  Exact suffix/prefix joins
then test sufficiency.  Across the seven basins, 475,756 necessary-domain
assignments were evaluated and none is universal.  Values outside those
domains are excluded by a missing-target forbidden bit, so this exhausts all
`5,905,424,385` position/value pairs for these seven basins.

This is an authenticated exact-enumerator theorem.  The independent light
replay checks the source and basin hashes, all seven zero-candidate statuses,
payload, and exhaustive-domain accounting; it does not independently repeat
all 475,756 replacement outcomes.  The frozen artifacts are

```text
THREAD_D_K16_UPPER12874_GAP_ONE_SHORTENING_FRONTIER_20260730.md
SHA256 1eb70fedfd56758fef772f6a5d7f4a0c559f2d6d1d7f648aefbdbbe702a63d6b

scratch/ad_k16_upper12874_lowhole_delete_sub1_20260730/audit.json
SHA256 5a4f47b1a431241e26b9dfbe8e19af69a6e52d136892c670d131fb45d94740e5
payload f715897ea360dd45d28f05980bf47b9b68d881d4aa150b707df3e0428d6ffa16

scratch/threadD_k16_upper12874_lowhole_delete_sub1_replay_20260730.audit.json
SHA256 7bfe2050e9acae22eed1e4dc18a93fd172e1b02d043c2ec3b4376a125ce8de57
payload 11a3772c2b1f80b584b3c1c1604280e61a6f485979d4bbe02eb5758ab32c6c8d.
```

Deletions leaving four or more holes plus one edit remain outside this
theorem.

## 5. Complete arbitrary-two-substitution normal form

Let `B=11373` be the sole hole of the deletion basin, and suppose a final
word differs at two distinct positions.

### Lemma 5.1 (sequential-or-joint dichotomy)

Every such universal word lies in the union of two classes.

1. **Sequential class.**  Some final `B` witness contains exactly one edited
   site.  That site's final value already installs `B` before the other edit;
   the second edit must repair every collateral debt.
2. **Joint class.**  A final `B` witness contains both edited sites.  Every
   unchanged cell between them is a submask of `B`, both final edited values
   are nonzero submasks of `B`, and their maximal compatible extension has OR
   exactly `B`.

### Proof

Every new `B` witness contains at least one edited site because `B` was absent
before the edits.  Choose one.  If it contains one edit, the other edit lies
outside and deleting it from the chronology does not alter this witness,
giving class 1.  If it contains both, every cell in the witness must be a
submask of `B`; extending through adjacent unchanged submasks preserves OR
`B`, giving class 2.  The classes may overlap, but their union is exhaustive.
QED.

The two exact finite evaluators implement these classes.  In the sequential
class they enumerate every first `B` service, calculate its exact
multiplicity ledger, and enumerate every second value which supplies every
debt.  In the joint class they enumerate every compatible position pair and
every pair of nonzero `B` submasks, retaining a target exactly when a new
affected interval supplies it.

The retained runs report:

```text
sequential:
  27,064 first services;
  646,720 second-stage pairs;
  no zero; minimum two holes.

joint:
  13,235 position pairs;
  102,404,745 replacement pairs;
  1,761,984,913 target checks;
  no zero; minimum one hole.
```

The best joint rows are

```text
(p,q,u,v)=(6439,6440,8300,1133), residual {43117};
(p,q,u,v)=(6438,6440,10344,1133), residual {43117}.
```

Direct ending-OR replay of both displayed children gives exactly that sole
hole.  An independent source audit proves the support/value loops complete,
checks the closed-form support counts, replays the extremal rows, and
materializes the first child.  The primary scalar ledgers are

```text
scratch/k16_12873_deletebest_twoedit_full.audit.json
SHA256 dc46acdd4cfb6eb77ea6bf32324b67197bec919a06ef2b7f1b853162facfad69

scratch/k16_12873_deletebest_joint2.audit.json
SHA256 aa2fbf3fe87069f75c4acb33cfcfcb61c4531b991a0054733a83f1f8abf99348
```

The independent audit is

```text
MATH_AUDIT_R_K16_12873_DELETE_RADIUS2_NORMAL_FORM_20260730.md
SHA256 25807a86dd0ca3fe52d03854fbfebdd6a2b9521d5cfa1aaadca4450e1caabbf2

scratch/r_k16_upper12874_delete_radius2_normal_form_20260730.audit.json
SHA256 6ac56bab32034e179c26a0c3f3b82607c5d33abe94b402ad5e528feeefa8e6d0.
```

Consequently no set of at most two arbitrary nonzero substitutions completes
this exact deletion basin.

### Corollary 5.2 (closest-branch latch)

The materialized closest state is

```text
scratch/k16_upper12874_delete_radius2_best1_43117.word
SHA256 09a60d48584a737f452a5d53c8fadec9b26cdad354f36926fbc5b1b1ceb4d166.
```

Its complete one-substitution census has 27,902 provider assignments and no
completion.  The exact floor is one at eight values at position 6440,

```text
{0x8041 OR s : s subseteq 0x002c},
```

and every one loses exactly `11373`.  Hence this branch forms the latch

```text
0x2c6d -> 0xa86d -> 0x2c6d.
```

The independent return audit is

```text
scratch/r_k16_upper12874_delete_radius2_best1_return_20260730.audit.json
SHA256 f5540f050a565f6bba5dd5cc3570a0156f176834496ea71587fad8987409b85b.
```

This closes one named radius-three branch, not every radius-three word from
the deletion basin.

### Theorem 5.3 (all-three-site radius-three branch is empty)

Suppose three distinct sites are edited and some final literal witness for
the old hole `B=0x2c6d` contains all three sites.  No such edited word is
universal.

Indeed, the `B`-submask runs give exactly 13,627 potential positional
supports, with span histogram

```text
2:12871, 3:629, 4:110, 5:17.
```

For each support, call a target private when every old witness meets the
three sites.  A deliberately relaxed test lets each affected interval choose
an independent, possibly zero, `B`-submask contribution.  It already
excludes 13,620 supports.  The seven survivors are consecutive triples; an
exact dynamic program over the 255 nonzero submasks of `B` enforces one
shared triple of edited values, the all-three `B` witness, and every private
target.  Every state set becomes empty.  The DP even permits an edited value
to equal its source value, so the no-go is stronger than exact Hamming
distance three.

The proof and adversarial audit are

```text
MATH_THEOREM_R_K16_RADIUS3_PROVIDER_PARTITION_AND_FROZEN_GAP_COLLARS_20260730.md
SHA256 874a4361f46e9c466ccbf5ec9960c471c1780d844dc9f84d492bae1e1f8614af

MATH_AUDIT_R_K16_RADIUS3_PROVIDER_AND_COLLAR_THEOREM_20260730.md
SHA256 6f05719c5cc70db3553ea46f281dd8c802b31b249f88fc9950ccc1053e10776b

scratch/r_k16_radius3_allthree_solverfree_obstruction_20260730.audit.json
SHA256 51dad15c6e7bbee6b2771906588d4af79130aa0d9bfacb7456b6c8ca3f4121f8.
```

Consequently the exact unresolved radius-three classes are now only:

1. a `B` witness using one edited site, with two cooperating repairs outside
   that protected witness; and
2. a `B` witness using two edited sites, with one repair outside it.

This is not a global radius-three no-go.

## 6. First excluded synergistic family: adjacent OR braids

For an adjacent replacement

```text
(x,y) -> (x',y'),    x OR y = x' OR y',
```

all intervals containing both cells and all intervals containing neither are
unchanged.  Only left-exposed intervals ending at the first cell and
right-exposed intervals beginning at the second can change.  This proves the
exact adjacent OR-braid delta lemma and algebraic exposed-provider catalogue.

The completed append and five-phase scans are valid only with their explicit
debt bounds (`<=4` and `<=5`) and forbidden-position conditions.  They are
not global braid no-gos.  The one-layer scans are complete for strict
one-braid improvement from their named inputs; the saved multistep chain is
greedy, not a complete two-braid search.  The independently audited scope is
recorded in

```text
MATH_AUDIT_R_K16_ADJACENT_OR_BRAID_SCOPES_20260730.md
SHA256 af59cfd2956f5d7ba8809a64c9c6c3a08b44789fe43eaaf6ae8d4941a3bfc5a0.
```

This remains useful structurally: one OR braid is the first family in which
two cell edits can jointly create a blocker although neither cell edit is an
individual provider.  Any complete two-braid search must therefore use a
joint affected-interval model, not an independent-provider filter.

## 7. Frozen catalogue-relative radius-four theorem

The earlier support-40 theorem remains proof-certified with exactly this
scope: starting from the five-phase source, fix

```text
p12873: 0x287d -> 0x4e63,
p6439:  0xa069 -> 0x206d,
```

then permit exactly two further arbitrary nonzero substitutions inside the
specified 40-position Hamming-neighbour provider catalogue, fixing every
other coordinate.  The exact CNF is UNSAT and its DRAT proof has literal
`s VERIFIED`.  Therefore no word in that source-relative radius-four
catalogue is universal.

This is not a global radius-four theorem: completeness is proved for the
sixteen Hamming-neighbour provider rows, not for synergistic pairs outside
their union.  The frozen manifest is

```text
scratch/r_k16_fivephase_blocker40_b2_20260730.manifest.json
SHA256 f6be395c0536b7e873a81eac167236df5562a298bb5aeaa13aa065ed46c96dd2,
```

and the checked-proof ledger is

```text
scratch/r_k16_fivephase_blocker40_b2_certified_unsat_20260730.audit.json
SHA256 d58fb6c9693dddb33067d102ebaa99fa131bb7524d2206c48d92a8d207c2982b.
```

## 8. Exact fixed-gap collar reductions

After deleting position 1, the old 5/9/4 editable collar contracts to

```text
P = [0,4) union [6435,6444) union [12869,12873),  |P|=17.
```

Allow every cell in `P` to be an arbitrary nonzero 16-bit mask and freeze the
complement.  Deleting `P` leaves fixed runs; every interval meeting `P`
contains a nonempty consecutive block of editable sites and a uniquely
determined fixed suffix/full-gap/prefix OR.  Enumerating those bases and
requiring one exact witness for every target is therefore an iff CNF, not a
window proxy.

The authenticated instance has

```text
461 interval patterns,
57 residual targets,
4,739 variables = 272 value bits + 4,467 witnesses,
145,704 clauses,
CNF SHA256 206581940afea13d9be331cf4d44f028dda9f79c7ffc705dea3dd2a1c928cf80.
```

A bounded H100 CaDiCaL run ended at its 1,260-second cap with exit `124`,
empty stdout/stderr, and no model or completed proof.  Its partial DRAT stream
is not a certificate.  The exact verdict is therefore `UNKNOWN`: no SAT
claim is valid without decoded literal replay, and no UNSAT claim is valid
without a checked proof.  The clause-by-clause independent audit is

```text
MATH_AUDIT_R_K16_12873_PHASE_FUSION_COLLAR_20260730.md
SHA256 922b6b2f2c2e94dbae98a2d87acda521da3a304020fb17b2e9e895027c5fcff7.
```

The related pre-existing direct and closure-normalized 5/9/4 jobs also
ended `UNKNOWN`; the latter hit its 1,800-second cap with exit `124` and no
SAT/UNSAT certificate.  No partial proof stream is promoted.

Within the architecture retaining the two authenticated fixed gaps, there
are exactly three ways to shorten one of the original collar widths
`(5,9,4)` by one cell:

```text
(4,9,4), (5,8,4), (5,9,3).
```

The location of the removed incumbent *inside a chosen collar* is immaterial
after every surviving collar cell is again allowed every nonzero mask: it
defines the same full variable fibre.  A solver-free reconstruction finds the
same 57 repair targets for all three profiles.  Their exact target-
intersection closure has 245 nonzero values, and maximal fixed-context
dominance gives the deterministic strengthened dimensions

```text
profile   variables   clauses
4/9/4       3,977     124,558
5/8/4       3,749     109,268
5/9/3       4,034     127,201.
```

These are equisatisfiable reductions, not SAT/UNSAT verdicts.  The audit is

```text
MATH_THEOREM_R_K16_RADIUS3_PROVIDER_PARTITION_AND_FROZEN_GAP_COLLARS_20260730.md
SHA256 874a4361f46e9c466ccbf5ec9960c471c1780d844dc9f84d492bae1e1f8614af

scratch/audit_k16_12873_three_profile_closure_model_20260730.py
SHA256 29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2

scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
payload d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47.
```

This trichotomy is complete only while both fixed gaps and their boundaries
are retained.  Deleting a gap cell, moving a boundary, or nonlocally
reordering cells lies outside it.  A mere independent-provider union is
already excluded by Lemma 5.1 and the OR-braid audit.

## 9. Precise boundary

Proved or independently replayed:

* the literal upper bound 12,874 and gap-one bracket;
* failure of every single deletion;
* failure of every adjacent OR fusion and every arbitrary adjacent one-cell
  fusion with the complement frozen;
* failure of every one-substitution continuation of the unique best deletion;
* failure of every one-substitution continuation of all seven deletions
  leaving at most three holes (authenticated exact enumeration);
* failure of every at-most-two-substitution continuation of that deletion,
  by the complete sequential-or-joint normal form;
* failure of every one-substitution continuation of the displayed closest
  radius-two child, closing that one named radius-three branch;
* solver-free failure of all 13,627 all-three-site radius-three supports;
* the adjacent OR-braid lemma and corrected finite scan scopes; and
* the DRAT-certified support-40 catalogue-relative radius-four exclusion.

Still open:

* a universal length-12,873 word;
* deletion-plus-one-edit basins whose initial deletion leaves at least four
  holes;
* the one-site-plus-two-repair and two-site-plus-one-repair radius-three
  classes from the deletion basin;
* a decisive solver verdict for any of the three exact fixed-gap profiles;
  the completed 4/9/4 attempt is only `UNKNOWN`; and
* all gap-moving or larger/nonlocal rethreads.
