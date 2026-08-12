# Corrected cube frontier for the `k=11`, length-476 repair neighborhood

## Scope and current verdict

This calculation starts from the fixed 465-entry prefix
`k11_upper549_natural_array.txt`, deletes exactly five original entries, and
appends exactly sixteen nonzero masks.  It concerns precisely that
fixed-prefix neighborhood:

```text
465 - 5 + 16 = 476.
```

It is not the unrestricted length-476 problem and says nothing directly
about the conjectural length 465.

The authoritative exact direct-span formula remains

```text
scratch/k11_length476_five_deletion_span_20260724/
  delete5_append16_span.cnf
```

with SHA-256

```text
42d64edb00f1a8cb0367b3071b2bb6a8d1cdce75e1f09f9df34d509743d6334f.
```

No corrected cube has yet returned SAT or certified UNSAT.  The exact current
status is therefore **UNKNOWN**.

## 1. Invalid first cube generation

The first file `cubes/delete_count_b8.jsonl` is invalid.  It inferred that
successive deletion-counter rows have stride `d+1=6`.  The production CNF
allocates a six-variable state row followed by five sequential-AMO
auxiliaries, so its actual stride is eleven.  At the first boundary, after 58
prefix decisions, v1 used variables `808..813`; the intended row is
`1093..1098`.

Consequently all 792 v1 UNSAT results, including checked DRAT proofs, decide
only malformed branches.  They do not cover the deletion space.  The invalid
batch was stopped and is labelled permanently in
`cubes/INVALID_V1_COUNTER_STRIDE_NOTICE.md`.

## 2. Explicit source-to-map repair

The CNF generator now exports every exact-count row explicitly:

```text
counter_vars POSITION V_0 V_1 ... V_5
```

The corrected cube generator refuses to infer any allocation stride and
reads those rows literally.  A separate streaming audit ties the exported
rows back to the frozen production CNF.  It found every expected forward
transition clause and the final exact-five unit:

```text
PASS positions=465 deletions=5 counter_rows=465
     counter_variables=2790 transition_clauses=5571
     cnf_clauses=2196500
```

The explicit counter map and independent audit hashes are

```text
da94199dc580e268aede15eb2ee674abd3e838c8bbc7927ed39b847f0239722e  counter map
c0c7a2fd6c0cadbc9f14e01d745257c60ca55fec187f800c1183ad59ce004703  CNF/map audit
```

## 3. Correct exhaustive cube decompositions

Divide the 465 prefix positions into consecutive blocks.  A cube specifies
the cumulative exact-deletion count at every block boundary by fixing the
complete one-hot counter row.  For a block-count profile

```text
(c_1,...,c_b),  c_i>=0,  sum c_i=5,
```

the number of deletion sets in the cube is

```text
product_i C(block_size_i,c_i).
```

Every five-set has one such profile.  Cumulative counts uniquely recover the
profile, while two distinct profiles disagree on a complete one-hot row and
therefore contain opposite literals.  The cubes are consequently exhaustive
and pairwise disjoint.

Four independently audited granularities are available:

| blocks | cubes | pairwise-disjoint pairs | cube SHA-256 |
|---:|---:|---:|---|
| 8 | 792 | 313,236 | `02850c1944c2c9907d3f64de5ab601e0862ac20d3a4cccff7f9975413cb1f215` |
| 12 | 4,368 | 9,537,528 | `ffb271b35fc0892f85872fe1b37dd8a23f15d1e2003b81c3f3851e7a7a908404` |
| 16 | 15,504 | 120,179,256 | `dc4b57c78276bde6f9ba61f7fe51c6299336bd5c031617fd7fb322a7646227fc` |
| 24 | 98,280 | 4,829,430,060 | `204f38d850f3aefa8a59eb7f71fbdc76409e3610ac7bf5bdfcf85f0e67582bf0` |

For every granularity the total combinatorial weight is exactly

```text
177,301,977,468 = C(465,5).
```

The independent audit also exhausts 4,293 small deletion assignments.

## 4. Compact propagation strengthening

An exact-equivalent experimental formula adds three early projections of the
append-suffix geometry.

1. At one appended endpoint, at most one selected target of each rank may
   occur.  AMOs are imposed for every rank 1 through 10.
2. A target chooses one witness mode WLOG: a selected prefix span or exactly
   one appended endpoint.  At most sixteen targets of any one rank may choose
   append mode, because a rank layer is an antichain and sixteen endpoints
   supply sixteen suffix-OR chains.
3. Compact selected-label channels enforce that targets of different selected
   ranks at one endpoint are nested coordinatewise.

These clauses are satisfiability preserving: every genuine completion can
choose one witness per target and its suffix ORs at one right endpoint form an
inclusion chain.  Conversely every selected span and append occurrence still
uses the already-audited literal witness implications.

The strengthened inventory is

```text
variables       266,928
clauses       2,782,148
literals      6,651,972
CNF SHA-256   a06b8b0d27c3c1f7a352f7e84921a446f3de58721e0fdc73fcd12c637ed24746
```

An exhaustive/sampled brute-force comparison through dimension three passed
all 1,601 instances.  Regenerating without the optional modules reproduces
the frozen production CNF byte for byte.

## 5. Solver status and next exact action

The two monolithic baseline searches were externally terminated without a
terminal result after approximately 3,841 and 3,322 CPU seconds.  Their exit
status 143 is not SAT, UNSAT, or a certificate.

Corrected cube probes are comparing the baseline and strengthened formulas.
On one corrected eight-block cube, matched 300-CPU-second runs both returned
UNKNOWN.  The baseline processed 1,511,718 conflicts with about 306 MB peak
resident memory; the strengthened formula processed 660,322 conflicts with
about 392 MB.  This does not establish a winner, but it gives no basis for
replacing the lean baseline.

A second nested benchmark used the count profiles containing the known
deletion pattern `0,272,275,276,464`.  After 180 wall seconds under matched
contention, all three runs were UNKNOWN:

| blocks | cube | conflicts | peak memory |
|---:|---:|---:|---:|
| 8 | 493 | 659,817 | 383 MB |
| 12 | 3,068 | 939,594 | 369 MB |
| 16 | 11,831 | 984,630 | 347 MB |

Finer counter cubes improve preprocessing, conflict throughput, and memory on
this profile, although no tested granularity is yet terminal.  A 24-block
probe reached 386,703 conflicts in 56 CPU seconds before external termination
(status 143), again without a solver verdict.  The strengthening is retained only if future
controlled corrected-cube benchmarks beat the baseline; formula size alone
is not evidence of improvement.

The next decisive action is:

1. finish matched probes at 8, 12, and 16 blocks on the same deletion-count
   profiles;
2. choose the granularity/formula minimizing terminal cube time, not raw
   clause count;
3. run every cube with proof output;
4. independently check every proof and hash an aggregate manifest;
5. combine those checked branches only with the audited disjoint/exhaustive
   cube theorem.

Only step 4 on every corrected cube would establish UNSAT for the complete
fixed-prefix delete-five/append-sixteen neighborhood.  A SAT cube instead
must be decoded and checked by direct quadratic interval-OR enumeration.
