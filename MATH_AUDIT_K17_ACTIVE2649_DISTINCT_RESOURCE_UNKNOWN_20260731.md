# K17 active-2649 distinct-colour run: resource UNKNOWN

Date: 2026-07-31  
Scope: one exact seam-bank solve before residual b-flow, topology, D3, or
common-cap compilation

The H100 run at

```text
/home/amodo/or15/work/root_k17_fragment_exactactive2649_full_20260731
```

used the 2,649-target active bank, the relaxed 319-hole hint, exact distinct
seam colours, and disjointness from every selected protected source colour.
The launched script had SHA-256

```text
49005704b91f1446ce07fa62a16af411eaafef5fbafd7fc7a36c109744da0d3a
```

and the inputs were:

| artifact | SHA-256 |
|---|---|
| active bank | `cdd99832bfeafc505c78924ba73b10c3a443c31b460786c9e7b63a9cb3b26aea` |
| relaxed hint | `802f92048ed93e9955472ea92a959fb829e6fafd8c8be3bc68ae8cc2babf08cb` |
| source components | `3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e` |

The initial model had 1,325,100 Boolean variables, 7,094,064 enforced
Boolean conjunctions, and 5,296,166 general linear rows.  Default CP-SAT
presolve expanded it to 4,496,192 at-most-one rows containing 98,124,216
literals.  Search began only after 631.78 solver seconds.  The process was
terminated by this lane when observed RSS reached 225,705,076 KiB and the
shared machine had only about 37 GiB available.  It had reported no feasible
solution, no infeasibility result, and no `CpSolverResponse`.

Therefore the exact status is

```text
UNKNOWN_RESOURCE_STOP
```

and no mathematical conclusion follows.  The retained log is

```text
scratch/k17_fragment_exactactive2649_full_default_resource_unknown_20260731.log
SHA-256 85da1ecd645bca8c7f0d50225f42a12ce32a507f6123207764bd6cf1acda91dd
```

The replacement run uses a deterministic 528-target casualty-independent
bank, the same exact lower-colour gates, eight workers, and bounded presolve.
Any positive candidate must still pass q1 augmentation, exact residual
b-flow, protected-edge replay, full-width upper replay, and topology audit.

