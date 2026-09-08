# Exact screen of the 465 single-deletion plus 12-append branches

## Scope

Start with the fixed 465-entry word in
`k11_upper549_natural_array.txt`.  Delete one of its 465 entries, keep the
remaining entries in their original order, and append exactly 12 new nonzero
11-bit masks.  This note screens all 465 choices of the deleted entry.

This is a complete screen of that repair neighbourhood.  It is **not** a
proof that an arbitrary universal word of length 476 is impossible.

The fixed inputs have hashes

```text
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd  k11_upper549_natural_array.txt
ba44a89403c6b402fb6c9b48cd8a1274dd716cd56885af710db8f091e8ee6989  k11_append_12.txt
```

## Rank-layer screen

After one prefix entry is deleted, every target absent from the remaining
prefix must have a witness ending at one of the 12 appended positions.  At a
fixed right endpoint the suffix OR values form an inclusion chain, so it can
contain at most one target from any fixed rank layer.  Therefore a branch is
impossible if it is missing more than 12 targets of any one rank.

The exhaustive deletion profile gives:

```text
465 total branches
383 structural rank-layer failures
 82 rank-feasible branches
```

All 383 structural failures are caused by rank seven.  Their distribution is

```text
missing rank-seven targets    branches
13                            144
14                            135
15                             73
16                             29
17                              2
```

Among the 82 survivors, 79 have exactly 12 missing rank-seven targets.  The
remaining three have 11:

```text
deleted index    deleted value    missing-by-rank
7                1536             4:2,5:3,6:4,7:11,8:1
89               68               4:1,5:3,6:3,7:11,8:1
196              52               5:3,6:4,7:11,8:1
```

These three branches were the hard shortlist under the rank-layer theorem
alone.

## Exact missing-poset width screen

The rank-layer theorem is a special case of a stronger endpoint fact.  Every
target missing from the fixed prefix must choose a witness ending at one of
the 12 new positions.  All suffix ORs sharing one endpoint form an inclusion
chain.  Consequently the complete missing-mask poset must be coverable by 12
chains, or equivalently

```text
width(missing masks under inclusion) <= 12.
```

Exact maximum matching in the bipartite strict-inclusion graph gives the
complete distribution

```text
missing-poset width    deletion branches
12                       1
13                      24
14                     115
15                     185
16                     138
17                       2
```

Thus 464 of 465 branches are structurally impossible.  In particular, the
old three-branch shortlist has widths

```text
deleted index    missing    matching    width
7                21         8           13
89               19         5           14
196              19         4           15
```

The sole branch surviving the exact width screen is deletion 102, with 17
missing masks, maximum matching five, and width twelve.

## Exact SAT screen of the 79 tight branches

The exact append formula enumerates every appended-only interval and one
representative for every distinct fixed-prefix suffix OR at each new right
endpoint.  The containment caps only delete physically impossible witness
lengths.  Since the 12 missing rank-seven targets saturate the 12 new right
endpoints, the formula also requires each endpoint to carry one selected
rank-seven witness.  This last condition is forced and therefore does not
restrict completeness.

All 79 tight branches returned UNSAT with the current exact formula:

```text
solver-UNSAT branches    79 / 79
sum of solve times       213 seconds
mean solve time          2.70 seconds
median solve time        2 seconds
maximum solve time       11 seconds
SAT candidates           0
timeouts                 0
```

These runs used one low-priority remote core.  The 76 unproved outcomes are
solver conclusions, not certified mathematical refutations.

## Representative proof certification

Three of the easiest/best tight branches were rerun with the corrected proof
hook and independently checked by `drat-trim` in binary mode:

```text
deleted index    missing targets    proof bytes    verification seconds
102              17                 30,314,178     25.724
313              17                  7,104,369     16.292
464              17                  4,969,655     15.541
```

Each verifier log ends in `s VERIFIED`.  The verification command is, for
example,

```sh
/root/drat-trim/drat-trim skip_102.cnf skip_102.drat.bin -i
```

The archived formula/proof generator and deployed binary hashes are

```text
671afc7e431607373db403d742e3acb089849264d1cb94fc8035bcb2f1905e78  append_completion_sat_rankcap.cpp
2d5c196d07d43e4b39fd4d18dc3acf32e595be6f81f5e2301dc906353f238ccd  append_completion_sat_rankcap
```

The three-proof sample totals 42,388,202 bytes.  Linear extrapolation gives
roughly 1.12 GB of proof data and 25 minutes of single-core verifier CPU for
all 79 branches.  This is affordable if full neighbourhood certification is
desired, but it is not needed for the present shortlist.

## Final result

The neighbourhood now has the exact ledger

```text
464 branches    structurally impossible by missing-poset width
  1 branch      deletion 102, independently DRAT-verified UNSAT
```

Thus all 465 single-deletion branches are rigorously eliminated by a theorem
or a checked proof.  No uncertified solver conclusion is needed for the final
claim.  There is no length-476 word in this particular fixed-prefix
delete-one-and-append-12 neighborhood.

This remains a neighborhood theorem, not an unrestricted lower bound on
`nu(11)`.

## Artifacts

The complete row-by-row manifest is
`scratch/k11_length476_deletion_screen_20260723/results.tsv`.  It contains the
deleted index and value, coverage, missing-rank profile, classification,
solver status, run time, and evidence path for every one of the 465 branches.

The same directory contains:

- the raw 465-row deletion profile;
- the 79 tight indices;
- all 79 exact-solver logs;
- the corrected rank-cap source snapshot;
- the three DIMACS files, binary DRAT proofs, independent verifier logs, and
  SHA-256 ledger.

The stronger theorem, complete proof, production implementation, explicit
maximum-antichain certificates, and independently written width checker are
recorded in `APPEND_MISSING_POSET_WIDTH_THEOREM.md` and
`scratch/audit_append_missing_poset_width.cpp`.
