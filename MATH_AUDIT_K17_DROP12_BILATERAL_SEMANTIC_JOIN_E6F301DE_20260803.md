# Fresh audit of the K17 drop-12 bilateral semantic join

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_K17_DROP12_IRREDUCIBLE_BILATERAL_SOURCE_TRIPLE_ORACLE_20260803.md`  
**Exact SHA-256:**
`e6f301de250af9f7833e5265415c63d7ac5bb385b2da0caa4bfa272f16a0a1d2`

## Verdict

**PASS for the factorization and candidate-driven schema.**  The current
theorem preserves the previously audited support-zero/support-one proof and
adds proof-safe implementation requirements: the exact 32 source-role cache
classes, complete support-mode/state provenance, both-helper-donor filtering
for every `G1` derivation, literal `common_five_cell` replay after semantic
indexing, and an explicit refusal to claim a subquadratic bound.

This is not a PASS for an implementation or a broad run.  At the time of this
audit no completed bilateral `B/G1/G2` producer source was present to inspect.
Any later producer must be audited against the acceptance contract below and
must bind this exact theorem SHA or an explicitly superseding theorem SHA.

The word “smallest” in the theorem's status paragraph should be read as
operational (the support-two projection isolated by the proved no-go chain),
not as a uniqueness/minimality theorem.  Replacing it with “lossless” would
avoid an unnecessary overstatement.

## Evidence chain

The exact 70-row extension package has manifest SHA

```text
c1daf35909f76d9d60c34c61f41e5f4554fc17a391fea980045139ddc8579441
```

and all 18 entries in that manifest replay locally.  It binds the two complete
exact70 implementations, binaries, outputs, audits, empty supplier handoff,
and projection proof.  The corrected unary manifest cited by the theorem is

```text
94101008273ed54928cd818daab8142bf03b007fba106477c71009b4d0ffcb03.
```

The earlier independent semantic audit remains useful for the unchanged
support theorem, but it is bound to theorem SHA `30c08e08...`; it is not by
itself a SHA-bound audit of the current theorem.  This note supplies that
fresh binding.

## Independent 32-class census

An independent parser bound to the current theorem SHA is

```text
scratch/audit_k17_drop12_support2_role_classes_independent_20260803/
  audit_k17_drop12_support2_role_classes_independent_20260803.cpp
SHA-256 93bc116b627eed19617fe2cb1ad87f7b6355a835426eed7cb452041ef656387c
```

It verifies the catalogue, 468-source bank, both owner phases, current
theorem, and prior audit by exact SHA.  Its output is

```text
sources                         468
two-phase source-role classes    32
class size range                1..99
source postings                 468
```

with role key

```text
(middle, receiver_root, owner_phase0(donor), owner_phase1(donor)).
```

The complete postings ledger has SHA
`2557669a8ef90ed8af0ca5f53ff1114e0b3dc0213e898dbaf212703fd476f50c`.

A second independently written checker also verifies the complete 112,621
helper bank.  It finds 112,621 distinct activated semantic signatures in
each phase and therefore exactly

```text
112621 * 4 flags * 2 phases = 900968
```

activated state postings.  Thus the 32-class quotient saves repeated source
predicate work, but it does **not** merge away helper identities or make the
helper-pair output small.

## Exact schema audit

For each provider posting retain

```text
kind, installing_mode, physical_row, donor_row, phase, flag,
Family, physical_root, phase_owner, predecessor/successor side.
```

The semantic tuple may be a bucket key, but the posting list is part of the
exact relation.  In particular, two modes with the same host/family cannot be
coalesced unless their complete mode, donor, short-payload, and supplier
provenance remains recoverable.

For a fixed source `e`, phase and declared key, construct four disjoint
ticket classes:

* `B`: complete unary-`e` tickets, including `H_e` and admissible incumbent
  LLR hosts, with later survival under both helper donors;
* `G1_f`: exact pair-child tickets using `h_f`, including the legal
  `(H_f,H_f)` self ticket when `alpha=beta`, and surviving both `d_f` and the
  later-selected `d_g`;
* `G1_g`: symmetrically;
* `G2`: exact tickets using distinct mode-labelled states `H_f,H_g`, retaining
  both predecessor/successor orientations.

The crucial implementation point is that a `G1` record cannot be declared
safe when only its named helper donor has been removed.  It must carry its
complete non-created provider footprint as a casualty certificate; after the
second helper is known, reject it if that footprint contains **either** helper
donor.  The source donor is already absent from the unary/pair child.

Join the two source phases on the same source key and a single-valued flag
map.  Require helper-support union exactly two, six distinct transfer
endpoints, and one of the nine exact phase-class pairs.  Emit

```text
(source edge, unordered helper pair, both literal phase tickets,
 class pair, full derivation/provenance set).
```

Only after this stage may records be projected to a physical child.  A child
with multiple designated sources retains the complete viable source-label
set.  The 21 and 645 counts are audit censuses of host-incidence patterns;
they should **not** be implemented as multiplicative outer loops.

Membership in the resulting source-support domain `Q` proves one complete
bilateral source option only.  It does not prove either helper option.  For
each child, regenerate all triple-local options for all three roles.  The
exact final occurrence test is the triangle test on the three option banks:
same-phase footprints pairwise disjoint and the six flag maps globally
single-valued.  Pairwise incompatibility bitsets are exact for this step.

## Required producer assertions

A promoted producer must fail closed unless it reports all of the following.

1. Input hashes for the parent, catalogue, source and partner banks, phase
   reservations, private and incumbent tickets, owner phases, theorem,
   every included source/header, and the final executable all pass before
   the run starts.
2. Reservation counts are 20/20, with intersection 17 and union 23; the
   private bank has 7,213 rows; incumbent LLR hosts remain eligible under the
   phase rule.
3. The source cache census is exactly 32 classes and 468 full postings.
4. Every `G1` record stores both donor-survival decisions and has no selected
   donor in its literal footprint.  The producer separately counts legal
   same-row helper self tickets.
5. Every `G2` record retains two distinct mode IDs and both physical
   orientations.  No tuple-only or host-only deduplication is allowed.
6. The nine class joins, 21 source patterns, and 645 full host matrices are
   reproduced exactly.
7. Output ledgers report semantic-class pair counts, posting-list product
   counts, expanded ticket counts, `|Q|`, source-label multiplicities, and all
   later exact-menu and triangle-test counts.
8. Every occurrence positive is simultaneously materialized, protected rows
   are byte-identical, and a fresh supplier matching reaches rank 16,878.

## H100 workload assessment

The blind source-anchored structural domain has about 2.95 trillion records
and must not be scanned.  The exact semantic precomputation is much smaller:
testing incoming and outgoing predicates for every activated posting, nine
short families, 32 source classes and both phases is at most

```text
32 * 2 * 112621 * 4 * 9 * 2 = 518,957,568
```

small predicate evaluations.  That stage is a reasonable CPU workload on
the H100 host and its resident state bank is well below a gigabyte with
compact records.

The expensive quantity is data-dependent: the number of surviving semantic
left/right class pairs and the sum of their posting-list products.  The
theorem supplies no subquadratic bound, and the 112,621 activated signatures
are all distinct in each phase.  Therefore the safe launch sequence is:

1. build and freeze only the class/posting census;
2. count candidate class pairs and expanded products with 128-bit counters,
   sharded by source class, phase and key;
3. report those counts before materializing `B/G1/G2` ledgers;
4. run one or two representative shards to measure exact
   `common_five_cell` throughput and output bytes;
5. launch the full expansion only after the measured disk/RAM budget is
   explicit.

This is candidate-driven and potentially feasible, but its full H100 runtime
cannot be estimated honestly until the class-pair/product census exists.
Worst-case quadratic output remains possible.

## Scope

This audit validates the current theorem and a proof-safe implementation
contract.  It reports no `Q` census, occurrence positive, supplier replay,
K17 child, chronology, residence, compiler, or word.
