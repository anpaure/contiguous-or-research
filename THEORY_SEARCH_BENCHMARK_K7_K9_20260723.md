# Controlled exact-search benchmark at `k=7,8,9` — 2026-07-23

## Purpose

This benchmark measures what the proved structural theory does to one common
unrestricted interval-OR encoding.  It does not compare unrelated fixed-row
or factor ansatzes, and it does not treat conflicts per second as a proof of
eventual solver speed.

All runs used the same local Kissat binary, seed 1, and one CPU.  Equality
runs had a 120-second process-time cap.  The strict-lower-bound runs had a
30-second cap.  Every reported `UNKNOWN` is a timeout, not evidence for SAT
or UNSAT.

`exact_or_sat.cpp` recognizes the benchmark-only environment variable
`OR_BENCH_PROFILE`; when absent it retains production profile 2.

| profile | exact additions |
|---:|---|
|0|raw interval-OR target encoding plus singleton symmetry only|
|1|cumulative rank truncation and simultaneous containment caps|
|2|profile 1 plus equal-rank endpoint injections, low/central cell competition, and complementary middle-layer disjointness|
|3|profile 2 plus the exact equality-case literal-rank onion used at the indicated dimension|

For `k=8`, profile 3 imposes the exact rank-four boundary/core structure:
rank-at-most-three entries form one interval, rank-four literal values are
distinct, and cumulative rank-three truncation caps their boundary mass.  For
`k=9`, zero residual forces every literal entry to have rank at most three.

## 1. Equality instances

### Formula size and terminal result

| instance | profile | variables | clauses | 120-second result |
|---|---:|---:|---:|---|
|`k=7,n=37`|0|183,874|909,271|UNKNOWN|
||1|43,140|200,317|UNKNOWN|
||2|60,261|274,388|UNKNOWN|
|`k=8,n=72`|0|1,362,201|7,439,039|UNKNOWN|
||1|240,516|1,249,045|UNKNOWN|
||2|298,258|1,449,410|UNKNOWN|
||3|298,258|1,688,042|UNKNOWN|
|`k=9,n=128`|0|8,513,729|50,858,700|UNKNOWN|
||1|813,783|4,575,133|UNKNOWN|
||2|1,038,568|5,551,750|UNKNOWN|
||3|1,038,568|5,551,878|UNKNOWN|

The structural theory cuts the raw clause count by factors of approximately
`4.5`, `6.0`, and `11.1` at `k=7,8,9`.  It does not, by itself, make the
unrestricted equality SAT instances easy.

### Solver work completed before timeout

| instance/profile | conflicts | decisions | propagations |
|---|---:|---:|---:|
|`k7/p0`|771,575|2,199,460|1,471,042,384|
|`k7/p1`|1,575,874|5,303,445|1,926,846,054|
|`k7/p2`|1,407,303|5,106,405|1,938,357,533|
|`k8/p0`|117,147|637,507|1,106,314,947|
|`k8/p1`|570,382|3,484,710|2,568,472,528|
|`k8/p2`|576,311|2,861,459|2,385,270,241|
|`k8/p3`|387,772|2,847,928|3,022,185,317|
|`k9/p0`|15,076|193,485|3,998,187,966|
|`k9/p1`|146,571|1,799,295|2,754,899,484|
|`k9/p2`|149,086|1,945,017|2,172,352,173|
|`k9/p3`|102,267|1,795,292|2,343,279,571|

The rank/containment theory materially improves formula size and search
throughput.  The onion units trade conflicts for substantially more unit
propagation, but no equality profile terminated.  Therefore a statement such
as “five times more conflicts” must not be reported as a fivefold solution
speedup.

A second `k=8` test constrained the word to differ from the stored optimum in
at most eight positions.  Profiles 0--3 all remained `UNKNOWN` after 60
seconds.  Thus the current unrestricted selector encoding is itself a major
bottleneck even inside a small certified neighborhood.

For comparison only, the much stronger fixed-factor `factor_k9.cnf` has
65,034 variables and 752,735 clauses and solves SAT in 0.05 seconds.  That is
evidence that the right WLOG structure can transform the search; it is not an
unrestricted benchmark because its factor structure is prescribed.

## 2. Strict lower-bound instances

| impossible instance | raw profile 0 | rank/containment profile 1 |
|---|---|---|
|`k=7,n=36`|UNKNOWN after 30s|UNSAT in 0.01s, 0 conflicts|
|`k=8,n=71`|UNKNOWN after 30s|UNSAT in 0.08s, 0 conflicts|
|`k=9,n=127`|UNKNOWN after 46.5s|UNSAT in 0.26s, 0 conflicts|

The profile-1 formulas contain the direct contradiction supplied by the
rank-count theorem.  This is the correct interpretation of the benchmark:

* the proved theory essentially solves the lower-bound side at these exact
  thresholds;
* it compresses equality search by an order of magnitude;
* it has not yet supplied the constructive/ordered information needed to find
  the known equality words in the unrestricted encoding.

## 3. Reproduction

Compile:

```text
clang++ -O3 -std=c++20 exact_or_sat.cpp -o exact_or_sat_benchmark
```

Generate one equality profile:

```text
OR_BENCH_PROFILE=2 ./exact_or_sat_benchmark generate 8 72 k8-p2.cnf
```

Solve:

```text
kissat --time=120 --seed=1 --statistics k8-p2.cnf
```

The raw DIMACS files used for this benchmark were temporary and are not
certificates.  The source profiles and this ledger are the reproducible
artifacts.

## 4. Scheduling conclusion

Long equality searches should be replaced when a strictly stronger audited
WLOG formula becomes available.  Keeping one weaker seed for formulation
diversity is reasonable; keeping many superseded seeds for tens of core-hours
is not.  Future theory modules should be benchmarked on both:

1. an impossible `B(k)-1` instance, to test lower-bound propagation; and
2. a known equality instance, to test whether the module actually exposes
   constructive geometry rather than merely shrinking the CNF.
