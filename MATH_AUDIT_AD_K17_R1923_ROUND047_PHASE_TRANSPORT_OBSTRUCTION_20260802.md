# Audit: scoped K17 round047 owner-phase transport on R1923/H1702

**Date:** 2026-08-02  
**Status:** superseded calibration; static transport passes and complete source
projection fails in both phases.

The copied checkpoint manifest SHA
`097ec68ba65380d442dcfe4018b673db3854729213847e12f4482707d99fc2ba`
verifies every entry.  Its model SHA is
`7a80fe02517039df87bcf7f88860b1bbf201482952c1317bfbcd6aeb9d435a2c`.
Independent replay gives exact q1 coverage `19412/19412`, one component,
48,620 selected edges, best linear residence 1,923, and deeper holes
`(1463,237,2)`, totaling 1,702.  Its manifest-authenticated containment table
has `(loss,gain)=(0,10)` in each alignment.

The positive round047 gate is authenticated by table SHA
`95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`
and independent projection-audit SHA
`2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a`.
The adapter reconstructs a connected-unicyclic carrier with 17,640 cycle
vertices, 8,820 cycle roots, 15,490 forced off-cycle phase edges, and exactly
two perfect owner phases.  It emits both tables and a complete incidence diff.

A separately compiled static verifier accepts each table with 24,310 selected
owners and all 65,535 lower targets exactly once.  A separately compiled
complete short-reset projection verifier then returns:

```text
phase 0: matching 16835/16898, deficiency 63, zero 48,
         Hall 88/25, graph FNV64 59afec0d73cb812a
phase 1: matching 16823/16898, deficiency 75, zero 56,
         Hall 107/32, graph FNV64 4e21a69aeae6f8af
```

This is an owner-dependent supplier-incidence obstruction.  It proves only
that the fixed res1972 round047 payload does not transport to R1923; R1923 is
now superseded.  No state balance, residence, upper, DM, common cap, compiler,
or word is claimed.

Frozen bundle:

```text
scratch/ad_k17_res1923_round047_phase_transport_obstruction_20260802/
```
