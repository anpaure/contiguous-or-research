# Audit: complete F208 target union and definitive root5 owner gate

Date: 2026-08-15
Status: PASS; exact owner-only atlas and conditional exact-solve gate

## 0. Audited claim and scope

This audit binds
`MATH_REDUCTION_Q4_K17_ROOT5_FULL_F208_TARGET_UNION_AND_DEFINITIVE_FACTOR_GATE_20260815.md`
at SHA-256

```
c01f3f7a5d3e15922fc946248b6f230944a081ecf547ddd51eac07b044c8bf9f
```

The theorem is exact for the reduced owner ledger: a column is keyed by
its full sorted ten-row mask, and one literal core/order witness is
retained.  It does not assert that distinct physical rails with the same
owner mask are interchangeable after lower-ticket, phase, or resource
decoration, nor that the retained witnesses can already be coinstantiated.

## 1. Symbolic hostile audit

The union identity is exact.  Every target catalogue `G_r(F)` is a subset
of the allowed atlas by its literal simplicity, reflection-disjointness,
and containment filters.  Conversely every allowed ten-row mask contains
ten rows of the common set `F`, and anchored completeness puts it in the
catalogue of each of those ten rows.  Deduplication by the entire row mask
therefore loses no owner-level action.

The common-`F` condition is essential and is stated correctly.  Earlier
F180, F186, and F202 catalogues cannot be substituted into this union.
The theorem now distinguishes independent replay from independent
re-enumeration of the 60,963,840 raw parameters, and the proof terminator,
status, and hash punctuation have been normalized.

## 2. Full-atlas certificate

The H100 manifest binds one completed catalogue for each of the 208
allowed rows.  The exact census is

```
10,006 total masks = 7,919 frozen + 2,087 new.
```

There are 100,060 per-target records.  Independent reconstruction finds
every union mask at exactly the ten target rows contained in that mask.
It replays 112,153 literal witnesses in total, including every one of the
2,087 new retained witnesses.  The fixed-F, base-instance, manifest,
all-mask, new-mask, and independent-audit hashes in Section 4 of the
theorem all match their literal H100 bytes.

The targeted generator source and binary, atlas builder, and independent
audit source hashes also match.  Per-target report/catalogue hashes and
their frozen/new/raw counters are checked inside the manifest audit.

## 3. Append replay

The original append report records

```
277,960 base pairs + 2,087 new pairs = 280,047 full pairs.
```

A clean independent ordered replay verifies that the 3,749 self options
are unchanged, the complete base pair list is an identical prefix, the
full list is unique, every appended mask lies in F208, and the appended
suffix equals the new-mask catalogue in literal order.  Its source and
PASS-output hashes are respectively

```
3f70cd5587189edfac13a9467e4773585b7df4f11318220784a862cf1ee941de
2a73e42bee4e3593f40dbdaf8d1481b6e6fec7a92ddece588512e523dc251ae7
```

This supersedes the earlier replay file whose final bytes contained a
literal escaped newline despite its `.json` suffix.

## 4. Exact ten-branch gate

The branch manifest has exactly the ten stated self-menu pairs.  Each
deletes eight rows, leaves 200 residual rows, and leaves row 661 outside
the self menus.  The complete row-661 target bank has 144 masks, all
frozen and none new.

The pivot report gives branch counts

```
105, 97, 101, 104, 106, 102, 104, 94, 100, 101,
```

which sum to 1,014.  Each pivot leaves one connected 190-row incidence
component and no immediate component-size cut.  Because every exact cover
uses exactly one row-661 column, proving all 1,014 K19 subproblems UNSAT
would be an exact owner-only obstruction; any SAT pivot witness would
close the owner patch after literal load replay.

No such terminal verdict is claimed.  The complete-atlas seeded campaign
returned 1,014 `UNKNOWN` results and no SAT certificate, and its literal
result replay passes.  The monolithic 601.56-second CP-SAT run also
returned `UNKNOWN`.  These are bounded search outcomes, not UNSAT proofs.

## 5. Binding replay

The light hostile verifier
`scratch/audit_q4_k17_root5_f208_full_union_freeze_20260815.py` has
SHA-256

```
4efb2bbeeaa0f9084fbc4396faa69ff39959ed6208f761f501e1075a6b6437da
```

It independently hashes 21 load-bearing artifacts, checks the theorem
contains every binding, replays the census and tenfold counters, verifies
the ordered append, checks the ten self branches and 1,014-pivot
partition, and audits both bounded `UNKNOWN` outcomes.  Its H100 PASS
output has SHA-256

```
c2748ecd16fac646b3ec73f999bef0d9c4d4b228119d67a5c492973b04bdd6cc
```

Verdict: PASS at the theorem's declared owner-only scope.
