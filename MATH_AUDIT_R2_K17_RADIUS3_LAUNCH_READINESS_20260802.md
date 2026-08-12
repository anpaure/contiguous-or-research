# `k=17` R2 audit: radius-three catalogue launch readiness

**Date:** 2026-08-02  
**Status:** count and chronology preflight `PASS`; full launch `NOT READY`
(fail-closed).  No radius-three packet enumeration or SAT run was launched.

## 1. Authenticated preflight

The audit used the frozen round-02 cut catalogue, bank, 21-anchor seed, and
the independently frozen exact-3664 proof package.  An independent C++20
program rebuilt the primitive table and its base histogram, checked every
anchor as a literal primitive, and evaluated the elementary-symmetric
polynomials over distinct bases.  It obtained:

| quantity | exact value |
|---|---:|
| candidate cuts / candidate bases | `20,477 / 3,806` |
| selected bases | `3,805` |
| unused candidate bases / cuts | `1 / 5` |
| primitive one-for-one recuts | `16,667` |
| visible / central / total anchors | `12 / 9 / 21` |
| all distinct-base triples | `770,667,109,363` |
| no-anchor triples | `767,757,643,652` |
| anchored triples | `2,909,465,711` |
| exactly one / two / three anchors | `2,906,453,982 / 3,010,838 / 891` |
| raw anchored proposals / secondary duplicates | `2,912,478,331 / 3,012,620` |

It hash-bound the cases, proof manifest, final audit, post-audit, certificate
hash replay, independent core replay, structural audit, and proof/post-audit
join.  It then joined every proof row to the frozen cases table, required
3,664 ordered unique bank keys and 3,664 `UNSATISFIABLE` results, and found
no case/job/key mismatch.
Therefore the chronological label "first new independent-recut shell" is
available relative to that frozen manifest.

The program was compiled only on H100 with
`g++ 13.3.0 -O3 -std=c++20 -DNDEBUG -Wall -Wextra -Wpedantic -Werror`
and run at the unique root

```text
/home/amodo/or15/work/r2_k17_radius3_launch_spec_audit_20260802
```

Hashes:

* verifier source: `5eeab93cdd286c10eab5995331011f2201710a50782d812fbc5e1b7f199f089a`;
* H100 executable: `84bf1fe3c2a0a8b516e40c8f08a1f7869a44d341024230db968fed1363e9cd27`;
* audit JSON: `28527b6a19accbf8ef71fe190e26d1339a9ed671a2b30bddda2d131367400dd2`;
* exact-3664 proof manifest: `0706fee2c9dba89c6339ca2088c9edc021f0d5107f0c1ddf1e344129fa3f92d3`.

The JSON deliberately records `launch_ready:false`; its pass status is only
`PASS_R2_K17_RADIUS3_COUNT_AND_CLOSURE_PREFLIGHT_ONLY`.
As fail-closed negative tests, substituting the cases ledger for the proof
manifest stopped before parsing with the exact SHA-drift diagnostic, while
using an authenticated input as the output path stopped before opening it.
Neither test produced an output or temporary JSON, and the proof manifest
remained byte-identical.  The verifier hashes and parses the same in-memory
byte snapshots, bounds every proof-row lookup, checks clean stream endings,
and publishes a flush/close-checked fresh temporary output by atomic rename.

## 2. Fail-closed launch-readiness audit

The launch root is not a proof-producing catalogue root.  The following
mandatory inputs or implementations from Sections 5--8 of the launch
specification are absent:

1. a complete `inputs.sha256`, serialized `primitive_recuts.tsv`, and an
   `anchors.tsv` with both `rid` and the authenticated root-fan dependency
   record (the present anchor file has neither field and has five descents
   in primitive-`rid` order, so it cannot directly define canonical masks);
2. frozen `L0` and `Lsucc` libraries with complete occurrence-labelled
   embedding/derivation manifests and replayable close/nonclosure data;
3. materialized causal/library anchor intersections, including subset truth
   tables and complete physical resource footprints;
4. frozen occurrence/atom reconstruction and zero-265 replay sources and
   ledgers;
5. the direct eight-subbank generator, canonical shards, immutable worker
   sources, and the full `generation`, truth, footprint, core-scan,
   rejection, survivor, and unknown streams; and
6. an independently implemented full verifier, exact stream merge comparison,
   final partition audit, and authoritative output `SHA256SUMS`.

In particular, the correction theorem says the causal/library intersections
must be materialized before a broad launch; the raw 2.909-billion anchored
stream is not itself a sensible launch plan.  No such intersections were
found locally or under `/home/amodo/or15/work`.  No radius-three launch
process was active.

Any future launcher must additionally pin worker and library epochs before
starting, publish each shard atomically, make resume idempotent, cover
disjoint canonical half-open key ranges, and merge-compare the ordered key
stream.  It must rebuild all eight subset banks directly, retain every
`UNKNOWN`, and must not stop at the first library-open packet if it later
claims a complete catalogue.  These requirements prevent a live-patch or
partial-shard result from being promoted as a proof manifest.

Thus the exact current verdict is:

```text
COUNT_AND_CHRONOLOGY_PREFLIGHT = PASS
RADIUS3_CATALOGUE_LAUNCH      = UNKNOWN / NOT READY
```

## 3. Scope

This audit proves only the input identities, primitive/anchor census,
distinct-base support counts, and availability of the exact-3664
chronological prerequisite.  It does not reconstruct even one radius-three
packet and makes no q1 feasibility claim.

The declared face remains exactly three compatible one-for-one recuts on
three distinct bases.  Same-base compositions, segment rethreads, four or
more recuts, correlated circuits, `C8+recut`, and the separate atomic
aligned `3+1`-`C8` face are outside this audit.  It makes no claim about
rank 11 or deeper, residence, topology, opening, common cap, compiler, or
the full contiguous-OR construction.

## 4. Marker-reservoir rebase

The 96-orbit marker packet in
`MATH_THEOREM_K17_MARKER_RESERVOIR_Z17_ORBIT_PACKING_20260802.md` is now the
authoritative reservoir candidate for future host work; R2 will not repeat
that packing search.  Its independent authentication and exact bridge
requirements are frozen in
`MATH_AUDIT_R2_K17_MARKER_RESERVOIR_REBASE_20260802.md`.

It does not yet replace the round-02 bank used above.  Its exact current
interface is an implicit `(x_mask,shift)` module bank with 6,528 unbound
occurrence-labelled buffer slots.  Until a protected host-position manifest
binds those occurrences and the resulting bank/factor hashes, the
radius-three primitive table, anchors, and launch-readiness verdict are
unchanged.
