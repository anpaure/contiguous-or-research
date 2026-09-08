# Task8 K17 drop-12 `S`-source bilateral semantic join

**Date:** 2026-08-03  
**Status:** lossless checker/producer contract for the remaining no-`H`,
target-capable, three-mode occurrence face on the canonical drop-12 parent.
This is an audit specification, not a broad-run result.

## 1. Frozen boundary

The contract is bound to the following exact objects.

```text
compressed parent
  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
literal final
  fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
structural catalogue
  790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
fixed-bank-safe U ledger
  f1d9ab4ad29d4806d1b3e6a7518dda17733cd415c24e34a5aa8865f236f067db
all-U Q23 classification
  160fd9c41409ef8bc99977efbeae4a5e45b8da4c492792cdb0ba4d7273d9f58c
S47 host-admitting unary ledger
  8311bb9909d22e8361c50d700909c46ed9e287df1aa2f91842d5328068c6c8c2
global H/S source-cover theorem
  7556ec953b062a88810b81f26163ff8c86616019dbaa44a6ac9ce1216d1b30ca
executed S support-one closure theorem
  a2395a13cd992ab1b14fbb5192cb88ae0083646f28c4099269c2b9c90e36c058
general bilateral factorization theorem
  e6f301de250af9f7833e5265415c63d7ac5bb385b2da0caa4bfa272f16a0a1d2
```

The all-`U` partition is exactly

```text
H  468       singleton full supplier rank 16878, Q23 credit +1
S   47       singleton full supplier rank 16877, Q23 credit +1
Z 112099     literal identity on Q23, credit 0
N    7       deletes supplier row 14851, credit -1
```

All seven `N` modes share host row 14851, so an endpoint-disjoint child
contains at most one `N`.  Task8 owns the no-`H` face.  A target-capable
Task8 triple therefore has one of the following class signatures:

```text
S,(S or Z),(S or Z)
S,S,N
```

Equivalently, after choosing an `S` source `s`, an unordered helper pair is
admissible only when it contains no `H`, contains at most one `N`, and an
`N` is accompanied by another `S`.  `S,Z,N` has inherited-shore credit at
most zero and is rejected before occurrence work.

The executed support-one theorem proves that every occurrence-valid,
target-capable Task8 triple gives each selected `S` role a two-phase option
whose external support is both other installed hosts.  This is a necessary
reduction.  It does not prove that a bilateral option, helper options, or a
rank-16878 child exists.

## 2. Physical identities and source labels

A transfer mode is the complete record

```text
(u_index, edge_index, q23_class,
 host_row, donor_row, lower, host_bottom, middle,
 receiver_root, host_root).
```

Neither `u_index` nor a host row is an edge identity.  Modes that install
the same physical host row can delete different donors and have different
new shorts, supplier effects, and casualty behavior.

A Task8 structural child key is the sorted edge triple

```text
child_key = (edge_lo, edge_mid, edge_hi).
```

The six endpoint rows of the three transfers must be distinct.  This test is
performed on exact host/donor rows, before any occurrence quotient.

Every `S` edge in the child remains a possible source label through the
bilateral source join.  The child projection stores the full set

```text
present_S_labels, bilateral_S_labels, occurrence_compatible_S_labels.
```

The least `S` edge may be attached later as a duplicate-free partition tag,
but it must not erase the other labels or their derivations.  A child
containing an `H` edge is routed to the H lane and is not a Task8 child.

## 3. Exact phase-local provider bank

For a selected triple `T={s,f,g}` and phase `phi`, construct the long bank
from the literal final skeleton and that phase's owner table:

1. delete all three donor rows;
2. insert all four flag states of all three host rows;
3. remove all 7,213 private rows;
4. remove the 20 incumbent rows reserved in phase `phi`;
5. admit a row reserved only in the opposite phase only at its incumbent
   flag; and
6. retain the ten incumbent materialized LLR hosts whenever those exact
   phase rules admit them.

The reservation intersection is 17 and the union is 23.  The global union
must not be banned from both phases.  Phase 0 is native.  Phase 1 remains
transported-owner evidence and is not authenticated as a private/native
phase.

Every provider atom stores

```text
provider_atom_id, phase, side, provider_kind,
installing_edge_or_minus1, row, flag,
exact Family payload, physical root, phase owner,
host/donor/lower/middle/root provenance.
```

`provider_kind` distinguishes base/incumbent providers from selected-host
providers.  The installing mode is mandatory for a selected host even when
another mode produces the same `(row,flag,Family)` tuple elsewhere in the
global catalogue.

## 4. Phase tickets and two-phase options

For each role `x in T`, phase `phi`, and one of the canonical 90 declared
keys `k=(q,alpha,beta)` with `beta<=alpha`, enumerate every physical pair
of provider atoms satisfying the exact incoming, outgoing, and
`common_five_cell` predicates.  If both sides use the same physical row,
require `alpha=beta` and count its footprint once.

A phase ticket retains

```text
role_edge, phase, key,
pred_atom_id, pred_row, pred_flag,
succ_atom_id, succ_row, succ_flag,
physical_footprint, row_to_flag_map,
selected_host_support_edges, donor_survival_bits,
complete_derivation_id.
```

The two phases of one role join only at the same declared key and only when
their row-to-flag maps have a single-valued union.  Different roles need not
use the same key.  Marginal nonemptiness, a first tuple, or a count per key
is not an exact option relation.

For the distinguished source `s`, partition each phase menu relative to
helpers `{f,g}` into the exact disjoint classes

```text
B       uses neither helper host and survives both helper-donor deletions
G1_f    uses h_f but not h_g and survives deletion of d_g
G1_g    uses h_g but not h_f and survives deletion of d_f
G2      uses both mode-labelled helper hosts
```

The legal equal-flag ticket `(H_f,H_f)` has one physical helper-host row and
belongs to `G1_f`, not `G2`.  Both predecessor/successor orientations of a
two-host `G2` ticket remain distinct.

The source option join contains exactly the following nine ordered
phase-class pairs:

```text
(B,G2)       (G2,B)
(G1_f,G1_g)  (G1_g,G1_f)
(G1_f,G2)    (G2,G1_f)
(G1_g,G2)    (G2,G1_g)
(G2,G2)
```

These are the phase patterns whose support union is exactly `{f,g}`.  No
H-specific `G2=empty` result is imported into Task8.

## 5. Complete three-role join

Membership in the bilateral source relation proves only one source option.
For every emitted physical child, independently regenerate the complete
triple-local phase tickets and two-phase options for all three roles.  Do
not freeze a helper tuple from the source-side producer.

Three role options form an occurrence packing exactly when:

* in each phase, the three physical footprints are pairwise disjoint; and
* the union of all six ticket flag maps is single-valued.

Same-phase reuse is forbidden even at an equal flag.  Opposite-phase reuse
is allowed precisely at the same flag.  Pairwise conflict bitsets are exact
for this final triangle test because both kinds of conflict are pairwise.

Every positive is then simultaneously materialized from `fa491`, not by
composing separately written children.  It must preserve all protected rows
byte-for-byte and receive a fresh complete supplier matching of rank 16878.

## 6. Safe quotient keys

Quotients are caches over exact predicate arguments; they are never physical
identities.

The 47 `S` sources have exactly ten two-phase predicate-cache classes keyed
by

```text
(middle, receiver_root, owner_phase0(donor), owner_phase1(donor)).
```

This key may cache source-short transition tables.  Every posting still
retains the exact source edge, endpoints, own installed host state, Q23
class, and supplier provenance.

For a phase/side provider predicate, a safe cache key contains all literal
arguments consumed by that predicate, at least

```text
(phase, source_predicate_class, declared_key, side,
 exact provider flag, exact Family payload,
 physical root, phase owner).
```

For `common_five_cell`, the cache key is the ordered pair of the complete
left/right semantic keys plus the exact source-short arguments.  A bucket
hit is expanded through both provenance posting lists before emitting a
ticket.

The following are unsafe as standalone quotient keys:

```text
host row; q23_class; candidate_id; Family alone;
(row,flag,Family); literal ticket tuple; source cache class;
sorted child key before retaining the source-label set.
```

Ticket deduplication is allowed only on a complete derivation record, or by
storing one literal tuple with the complete set of derivations and donor
casualties.  `G2` orientation and source labels are never deduplicated away.

## 7. Fail-closed ledgers

The accompanying machine schema is
`K17_DROP12_TASK8_S_BILATERAL_LEDGER_SCHEMA_20260803.tsv`.  A promoted Task8
run must freeze at least:

1. exact input hashes and a successful preflight transcript;
2. the `S47` source/class ledger and complete helper postings;
3. provider atoms and semantic-bucket posting lists;
4. all literal `B`, `G1`, and `G2` tickets with donor survival;
5. all bilateral source options and source labels;
6. duplicate-free children with the complete retained label sets;
7. complete triple-local role menus/options and the final triangle result;
8. simultaneous child tables, protected-row audit, and supplier matching for
   every occurrence positive; and
9. exact per-stage row counts, posting-list products, output bytes, and
   hashes.  A complexity claim cannot replace those measured counts.

The lightweight checker in
`scratch/audit_k17_drop12_task8_s_bilateral_schema_20260803/src/`
authenticates the frozen classification, S-source identity, reservation and
private-bank rules, endpoint-bank separation, and ten source cache classes.
It intentionally does not launch or simulate the broad bilateral join.

## 8. Scope

This specification is lossless for endpoint-disjoint three-mode selections
from the authenticated `U112621` catalogue on the fixed `e878/fa491`
parent, after the executed S support-one closure.  It does not cover
overlapping exchanges, another parent/root subset, cardinality four or
higher, chronology, residence, outer matching, compilation, or a K17 word.
It does not report a Task8 bilateral positive or no-go.
