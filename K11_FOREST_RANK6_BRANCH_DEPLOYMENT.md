# Exact rank-six branch deployment for unrestricted `k=11`

## Status

The independently audited source

```text
c1eff19c73fa6610bd603194a43c89ffb5a54092cb35947fda64c6ed61876f0b
```

was copied to the remote production host as
`/root/k11_forest_exact/k11_forest_sat_branch.cpp` and compiled there with
`g++ -O3 -std=c++2a` against the existing CaDiCaL static library.  The remote
binary SHA-256 is

```text
81b5c18a07c74be816edac882b7865eb5757ee6085078a462e701de0dcec5467.
```

No compilation or SAT search was run on the local Mac.

## Reproduced formula inventories

Both build-only runs enabled

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_SINGLETON_POOL_CUT=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1.
```

They reproduced the audited inventories exactly:

| branch | meaning | variables | clauses |
|---:|---|---:|---:|
| 0 | no literal rank-six entry | 2,924,697 | 14,732,380 |
| 1 | sole literal rank-six entry is `A[0]=63` | 2,924,938 | 14,734,039 |

The branch-one delta is exactly 241 variables and 1,659 profile clauses.
Each member also contains the common anchor clause and its branch unit.

## Live runs

The two weaker seeds 51 and 52 were terminated after the successful
build-only checks.  Their logs were retained.  They were replaced on the same
cores by the exhaustive branches:

```text
branch 0: seed 61, core 36, wrapper PID 164664, solver PID 164667
branch 1: seed 62, core 38, wrapper PID 164665, solver PID 164668.
```

The output files are respectively
`candidate_branch_61.txt` and `candidate_branch_62.txt`; logs are
`branch_61.log` and `branch_62.log`.  The direct, rank-three, joint-only, and
fixed-row portfolios remain live for formulation diversity.

This deployment is not a SAT or UNSAT result.  A candidate still requires the
full independent OR-certificate workflow, and branchwise UNSAT requires
checked proof traces plus an explicit certificate-level case split.
