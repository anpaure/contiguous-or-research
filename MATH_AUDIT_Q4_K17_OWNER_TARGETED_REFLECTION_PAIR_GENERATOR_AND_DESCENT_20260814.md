# Hostile audit of the q4 k17 owner-targeted reflection-pair generator and descent

**Date:** 2026-08-14
**Verdict:** **PASS** for the owner-only quotient claims, exact anchored
parameterization, complete target-local counts, bounded top-K theorem, and
literal one-pair-swap certificates stated in the source.  No lower-ticket
or full-factor conclusion is audited here.

**Audited source:**
`MATH_THEOREM_Q4_K17_OWNER_TARGETED_REFLECTION_PAIR_GENERATOR_AND_EXACT_DESCENT_20260814.md`

## 1. Completeness audit

Translation is free on rank-nine subsets of `Z_17`, so a quotient-simple
rail containing a chosen owner necklace has one target occurrence and one
translation taking it to the canonical representative `A`.  Rotating that
occurrence to start zero leaves exactly:

```text
C subset A, |C|=5;
an order of A-C in positions0..3;
an ordered six-subset of Z_17-A in positions4..9.
```

Hence the raw size is
`C(9,5)*4!*P(8,6)=60,963,840`.  The implementation's eight-label
permutation with the two unused labels increasing represents every ordered
six-tuple exactly once.

The generator is for unordered reflected pairs.  If the base member of a
given pair contains `rho(A)` rather than `A`, reflect the whole rail first;
the mate is then in the enumerated orientation.  This closes the only
orientation ambiguity and proves completeness for ten-row reduced masks.

## 2. Filter and deduplication audit

Every raw rail is reconstructed literally.  Canonical owner-orbit IDs are
required to be distinct.  The test `E intersect rho(E)=empty` is exactly
reflection-pair usability: it excludes fixed owners and any collision
between the two columns.  It also implies that the ten reduced row IDs are
distinct.  The optional `F` test is the literal subset condition on those
ten IDs.

Deduplication is by the sorted ten-row mask.  Witness updates retain the
lexicographically least core/order/owner sequence.  The reflected core,
order, and owner IDs in scored TSVs are direct coordinate negations and
were reconstructed independently.

For every complete census, the current instance is parsed independently.
The source asserts that every current pair mask containing the target row
is regenerated.  All reported overlaps pass exactly; this is a strong
end-to-end check of normalization, reflection orientation, and reduced-row
indexing.

## 3. Census audit

The three E86 rows were selected by the stated blocker-menu ordering.  The
independent audit recomputes 43 holes, their menu data, frozen pair degrees,
and the order `595,484,631`.  It reconstructs all 36 sampled physical
witnesses and confirms that the three targets lie in one multiplier orbit.

All three independent complete runs agree on

```text
59,564,920 quotient-simple raw rails,
30,978,490 reflection-disjoint raw rails,
15,486,081 distinct pair masks,
327/327 frozen target masks regenerated,
15,485,754 new masks.
```

The later row516, row395, row399, row459, row605, row348, row664, and
row624 outputs each bind their own raw/simple/disjoint/unique/overlap/new
counters.  These are per-target counts; the theorem correctly does not add
them or claim a deduplicated cross-target atlas.

The counts concern owner decks only.  They do not test lower-q1 or lower-q2
decks, collars, or actuator resources.

## 4. Score audit

For load `ell`, adding one incidence changes `(ell-1)^2` by `-1,+1,+3`
at loads `0,1,2`; removing changes it by `+3,+1,-1`.  Their sum is always
two, so subtracting `2|N intersect P|` exactly cancels rows present in both
incoming and outgoing masks.  The hole-change formula likewise removes
filled old holes and adds singly-loaded outgoing rows absent from the new
mask.  Both formulas are exact.

The per-shard top-K reduction is sound.  A key discarded from one shard has
at least K distinct better keys in that shard and therefore cannot be in
the global K.  Global merging deduplicates keys and retains the least
witness.  The same argument applies independently to each per-hole
reservoir.

## 5. Full-record replay

The independent Python verifier parses every emitted scored record, not
only the best row.  For each record it checks:

* ten distinct reduced rows and absence from the scored-against pool;
* core/support ranks, disjointness, and literal owner reconstruction;
* all owner IDs and all reflected owner IDs;
* reflection disjointness and the reduced-row mask;
* covered incumbent holes, add base, and holes filled;
* all 54 outgoing selected pairs, the exact best pair index, energy delta,
  new energy, and hole change; and
* deterministic score order and score histograms.

For E86 it replays 100,000 top records plus 4,725 reservoir records and
checks the literal E80 load vector.  For later 5,000-record batches it
replays each top file and its reservoir.  An independent hostile pass also
recomputed all E86 top-100,000 swaps and confirmed strict global order.

The direct descent witnesses and the three zero-best target oracles in the
source agree with these replays.  A zero best score proves only complete
one-swap exhaustion for that target at that incumbent.  The source properly
leaves neutral pivots, self moves, and two-swaps open; the row348 neutral
escape demonstrates why this qualification is necessary.

## 6. Descent scope

The target generator supplies new pair columns and exact local scores.  The
separate Benders lane appends/deduplicates those rows, preserves witness
metadata, and certifies the new incumbent and pair/self local optimum.
Accordingly this audit distinguishes:

* literal scored steps, verified directly here; and
* additional pool/self descent moves and local-optimum states, imported
  from their separately verified Benders certificates.

No owner exact cover, lower alignment, or global actuator compilation is
deduced from decreasing energy alone.

## 7. H100 provenance

All substantive compilation, enumeration, scoring, replay, compression,
and hashes ran on H100.  The Mac was used only for reading, editing, file
transfer, and Git.

The E62 freeze replay returned PASS on the independent E86 census and on
all eight later scored batches (nine replay jobs total).  Its H100 binding
is:

```text
theorem                 8c6fd9f281c6ef5f225c82eb705fff3d95aabc6d43d3ea881dae8db4d5e22828
C++ generator           861527ebce2d0f6a3aa7edbb070dd5e57ddb832f5a9786bcd12483d904d4db14
context builder         ca6f5d58241f152f0b99d471e9929e040d024fb890f35b0711176f9d896b572b
census verifier         c0bd20ed567a9e4ed400e33de922238da1a7b74447847b2e37c4edf2f8a02361
full-record verifier    ffc433fdaf7c0944741ce285acb322e8a917d23250ba150a50a6573ebb3bd41c
freeze replay rollup    d60a5ca1aeb2e2de79d86aacdf1e494df6f5e198c00820ad3aa9d23c22713a9e
63-entry manifest       4bb7f82713d0d9080f7f91f1a940ed1f022b9dea165da993d0f12824603585a5
```

The 63-entry manifest is
`scratch/q4_k17_owner_targeted_reflection_pair_freeze_20260814.sha256`.
It binds the exact census/score reports, all nine replay outputs, every
scored top/reservoir TSV, and every instance/incumbent used by the replay.
It deliberately stops at E62; the later E60 descent is outside this audit.
