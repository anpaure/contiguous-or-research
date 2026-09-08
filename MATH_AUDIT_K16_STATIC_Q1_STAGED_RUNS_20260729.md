# K=16 static-residence q1 staging: executed runs

This audit records the first live executions of the ladder specified in
`MATH_K16_STATIC_RESIDENCE_Q1_COVERAGE_STAGING_20260729.md`.  Every run was
H100-CPU-only and left the independent full-Johnson hard-both run untouched.

## Combined q1 objective, Q union R, 8 GiB

Configuration: 25,349 physical edges, exact static directed residence,
`q1-mode none`, soft objective `both`, resident-distance lexicographic
tie-break, validated artifact hint, four workers, 1,800 second solver limit,
7,168 MiB OR-Tools memory parameter, and an 8 GiB OS address-space cap.

The process stopped after about 6 minutes 14 seconds with `std::bad_alloc`.
The largest sampled RSS was 4,999,384 KiB (about 4.77 GiB); virtual-address
usage, rather than sampled RSS, reached the 8 GiB guard.  No result JSON or
incumbent was serialized.  This is `RESOURCE_LIMIT`, not infeasibility.

Frozen log:

```text
scratch/k16_static_softboth_q_union_r_artifact_1800s_20260729.log
sha256 416fd4b0b2aabd9fe2754102a99e3a7ac7500a8b8cf2880346a0a7e5b0847e99
```

## Lower-only objective, Q union R, 8 GiB

Configuration was identical except for `soft-q1-objective lower`, seed
20260730, and a 300 second solver limit.  It terminated normally with a
feasible, nonoptimal incumbent.  Independent solver-free replay proved:

```text
lower modeled/replayed coverage = 10,948 / 11,440
upper literal coverage          = 10,742 / 11,440
lower/upper holes               = 492 / 698
residence violations            = 0
components                      = 2 (lengths 4,435 and 8,435)
unclaimed replayed lower colours= 0
resident symmetric difference   = 0
```

Thus the five-minute stage returned the resident exactly and did not close a
palette.  This does not prove that the Q-union-R optimum equals the seed.

Frozen result and independent replay:

```text
scratch/k16_static_softlower_q_union_r_artifact_300s_20260729.json
sha256 82a99d4b2493e8bd6e4b15766597ce4dd6c23779ef180013d45f517afe587dd5

scratch/k16_static_softlower_q_union_r_artifact_300s_20260729.audit.json
sha256 bc3e8b059e36e332c84757430a61ecbb3b46a2bb3a01b76a44b803034c710f96
```

## Combined q1 objective, Q union R, 16 GiB

The resource-distinct rerun used two workers, a 14,336 MiB OR-Tools limit, a
16 GiB OS address-space cap, and a 1,800 second solver limit.  It terminated
normally with a feasible, nonoptimal incumbent, but again returned the
resident exactly:

```text
lower modeled/replayed coverage = 10,948 / 11,440
upper modeled/replayed coverage = 10,742 / 11,440
lower/upper holes               = 492 / 698
residence violations            = 0
components                      = 2 (lengths 4,435 and 8,435)
unclaimed replayed colours      = 0 / 0
resident symmetric difference  = 0
```

The solver bound remained strictly above the incumbent, so this does not prove
that the Q-union-R optimum equals the seed.  It does show that neither the
five-minute focused stage nor the full 30-minute combined stage moved away
from the complete oriented artifact hint.  The next useful ladder step should
therefore enlarge the provider catalogue rather than repeat Q union R.

Frozen result and independent replay:

```text
scratch/k16_static_softboth_q_union_r_artifact_16g_1800s_20260729.json
sha256 fa10f79ffb898b4febdf86d1db3e4fbb0510ca62a4f142247d3e68f800784c09

scratch/k16_static_softboth_q_union_r_artifact_16g_1800s_20260729.audit.json
sha256 2c54c4778bea15c0bde308f3e1e2afffa173e781346474a3e0749b5de38ec53c

scratch/k16_static_softboth_q_union_r_artifact_16g_1800s_20260729.log
sha256 ef55d43b09ea51f81dbfc9dbb6bb07bbc9ae6717fbee551e3816af63fb90955e
```
