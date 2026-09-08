# K16 two-source-slot filler enumerator

Date: 2026-07-30  
Lane: AD  
Status: **source frozen and independently audited; complete H100 census; one
exact/all-upper output, Hall deficiency 33**

Source:

`scratch/search_ad_k16_two_source_slot_fillers_20260730.cpp`

SHA-256:

`a3d14467d5b78a23970b676e883c321ec8356bcf3db0f31174f950e99260332b`.

Manifest:

`scratch/ad_k16_two_source_slot_fillers_20260730.INPUTS.sha256`

SHA-256:

`04a2a77f548f996f9da15f2038978296f4500a9d33c54ccedb30a8a68adee33f`.

The exact normal form uses original bad2 coordinates:

```text
A=[2186,2217) forward
B=[1266,1295) reverse
F=[6253,6263), inserted reverse at A's old slot
G=an oriented interval of length at most 64, inserted at F's old slot
A+B inserted before old row 3846.
```

The source rows of (A,B,F,G) are each deleted once.  An exact origin
permutation audit proves every old row is emitted once.  The complete
successful one-filler parent is reconstructed and compared row-for-row with
the authenticated SHA-256 `0c19e3c7...` input before the (G) census starts.

The structural catalogue has 766,858 oriented (G) packets.  A safe old-gap
prefilter leaves 19,503: it is applied only when the (G) source gap lies at
least six rows from the fixed destination.  Near the destination, the old
test is deliberately bypassed.  Every candidate then receives literal tests
on the actual materialized:

1. (G)-source gap;
2. (B)-source gap;
3. (G) interval at the old (F) slot;
4. reverse-(F) interval at the old (A) slot;
5. (A+B) destination interval.

Final replay independently enforces terminal depth zero, nonnegative dynamic
depths, nonzero maximal envelopes, and every middle row equation, followed by
unrestricted upper interval-OR replay.

For each unique upper-complete word, the summary records exact
`(allowed,mandatory)` profiles for the five standard (A)-slot cells and the
five analogous (F)-slot cells, as well as which of the targets
`091d,291d,291c,2e28,2f28` occur at the (A) slot.

The output directory and summary must be fresh.  Full-vector deduplication is
exact; exceeding 4096 unique words aborts as UNKNOWN.

Completeness is limited to strict pairwise source-halo separation, one
additional (G) of length at most 64, the two fixed fill slots, and fixed
destination 3846.  Touching halos, longer packets, moved slots/cuts, and
changed row values remain outside scope.

## Independent source audit

An independent static audit checked every relative placement of (G): before
(B), between (B) and (A), between (A) and the destination, between the
destination and (F), and after (F).  The origin-permutation check and the
five literal interval checks are complete for the stated strict-halo normal
form.  In particular, the near-destination old-gap prefilter is bypassed and
cannot create a false negative.  The source does not SHA-pin its inputs
internally, so the external manifest check below is part of the run
certificate.  The profile fields are diagnostics, not a Hall conclusion.

## Authenticated H100 census

The source and manifest above were copied to

```text
/home/amodo/or15/work/ad_exact229_twofill_a3d14467_20260730
```

and compiled and run on one H100 CPU core, at nice level 15, under a 600
second timeout and 2 GiB address-space cap.  No local enumeration was run.
The remote pre-run hashes were

```text
65abf0532b0bbfced9041cbc3d22b48a66ffc7044525e412c37890a62c36d655  search_ad_k16_bad2_splitbuffer_pair_20260730.cpp
a3d14467d5b78a23970b676e883c321ec8356bcf3db0f31174f950e99260332b  search_ad_k16_two_source_slot_fillers_20260730.cpp
dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d  best_upper_complete_bad2.targets
0c19e3c73616a4d771f29f8031aebd946131f4eeb20a571f59852458ec0f0760  f6253_l10_reverse.targets
32c1af82f793a2001fe9ab16323f133f70b339580e081e4ddfcb332f08d61d12  twofill
```

The exhaustive scoped census returned

```text
structural_oriented=766858
prefilter_oriented=19503
materialized_g_gap_pass=18266
literal_component_pass=3
full_exact=3
upper_complete_rows=1
unique_upper=1
```

The sole output has

```text
G = [1522,1547), reverse
word SHA-256 = 37a711b51046e32cd3c529f70c5a71fb4b079c5bc1f0cd384ec755473d733a17
A-slot ears = 2e28,2f28
```

Its independent full generalized-compiler Hall replay gives

```text
targets       26332
cells         32063
incidences    347670
matching      26299
deficiency    33
Hall shore    231/198
```

The Hall witness file has SHA-256
`73d1284a8a6a2f3a600ee01cd91922d46305d13aaf776daef584c59620458943`.
Therefore this exact two-return face transports the open source defect to a
worse collar: it preserves the two desired (2e28,2f28) ears but changes the
deficiency from 27 for its one-filler parent to 33, and from 25 for exact229
to 33.  This closes only the stated one-additional-(G), strict-halo,
length-at-most-64 face as a Hall descent.  It does not obstruct a longer
return chain, interacting halos, a moved fill slot, or a simultaneous
multi-packet closure.

Frozen local copies of the output, summary, hashes, and Hall witness are in
`scratch/ad_k16_exact229_two_source_slot_fillers_20260730/`.
