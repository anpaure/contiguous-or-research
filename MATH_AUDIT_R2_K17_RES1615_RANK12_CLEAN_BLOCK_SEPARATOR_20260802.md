# R2 audit: exact rank-12 clean-block separator for the residence1615 carrier

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_res1615_cleanblock_rows_20260802`

## Authenticated inputs

- quotient option map: SHA-256 `7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3`;
- independently replayed factor: SHA-256 `a3e5d3eaab97bdac908afb884ec479168446fe81b91f5ebe72cd8dacbe687072`;
- physical deep-hole ledger: SHA-256 `13a90d52920ad1bc67ad48cb3b7d414a55bdcf0e08a227906e3af70a98217f7e`;
- missing-orbit ledger: SHA-256 `07c76ddae4ea9194b3a98fb5dc6e52a69643e2874cd4af153eb03b3d857d6596`.

The factor has 24,310 edges, one copy of each rank-8 facet and rank-9 owner, all 19,448 rank-10 caps, 3,944 protected edges, and 1,198 selected optional quotient orbits.  This audit does not reauthenticate its chronology or residence claim.

## Separator statement

For a missing rank-12 target `Z`, let `C_Z` be the 220 rank-9 owners contained in `Z`.  Restrict the incumbent factor to `C_Z`.  Every resulting component has owner union strictly smaller than `Z`; the certificate records one coordinate in `Z` absent from that union as its persistent hole.

Let `S_Z` be the selected optional quotient orbits incident, in any of all 17 physical phases, with a clean owner in the corresponding copy of `C_Z`.  In the exact degree-two factor master, retaining every orbit in `S_Z` saturates every affected clean owner with its incumbent incidences.  The clean components and their persistent holes therefore remain unchanged, so `Z` remains uncovered.  Consequently the following negative-primary no-good is valid:

```text
OR_{e in S_Z} (not x_e).
```

This proof uses every physical phase.  It does not infer phasewise validity from a quotient representative.  Fixed protected incidences are reconstructed literally and are not exposed as selector literals.

## Exact result

The physical ledger contains 255 rank-12 holes, exactly 15 complete `Z_17` orbits.  The producer and a separately written semantic replay agree on:

- 15 distinct, nonempty negative-primary clauses;
- support widths 217 through 307, total 4,224 literals;
- 220 clean owners in every one of 17 phases of every orbit;
- 36,210 component rows, each with an explicit persistent-hole coordinate;
- 56,100 literal incidence rows;
- identical optional support and clean-component size profile across all 17 phases of each orbit.

Principal artifact hashes:

- rows: `d857081d277b4ec5ff2c610a9fb2b06cf28d615c5cf6c3914138712ae7f7f537`;
- targets: `ff1d08b0e19862612972984a7c87c8cc396cac71beeecf12df84e68778b2050a`;
- components/persistent holes: `fab31694af8347240faa4a2add9bcdcf93b375f5e853b67dd4b79f8963fcde9c`;
- incidences: `7fdc6d6d85b27daafa9e2c237db35fc9c45a41b40d2200ac7c28a0f10f2c00a0`;
- producer audit: `11365a41f18d193dd923b48b4907b3013f2fab282d715bc93ad35f9e70545440`;
- independent replay: `4fed3d4c0851dbe8184a6d0e1e461545ada5e269c06dab1ae6dd66f017000de7`;
- finite-package manifest: `d5b7c969b4d1b4bc05f93561f7744410bf9aefd78bedfad63ef3d2b513a32701`.

## Scope

This is a carrier-specific rank-12 lazy-cut package.  The carrier remains nonresident (1,615 short positive runs), and no SAT, source, compiler, opening, exterior-window, regeneration, or word claim is made.  No solver was launched.
