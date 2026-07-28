# k=15 native-search port audit (2026-07-28)

## Rule

Port measured hot kernels, not Python syntax indiscriminately.  The live exact
search has three layers:

1. combinatorial instance construction and local compiler scoring;
2. SAT orchestration / proof-auditable JSON;
3. SAT solving.

Layer 3 is Kissat and is already optimized native code.  Layer 2 is negligible
unless profiling proves otherwise.  Layer 1 is the C++ target.

Native builds use C++20, `-O3 -march=native -DNDEBUG` (and LTO where the host
toolchain supports it).  Every replacement must reproduce Python outputs on
frozen certificates before it is used for search.

## Measurements

### Exact Hall audit

On `scratch/k15_outer2_p1_h30_bridge.json`:

```text
Python wall/user: 0.48 / 0.46 seconds per audit
hall_score cumulative: 0.420 seconds
Hopcroft--Karp itself: 0.025 seconds
```

Most time is candidate-graph construction (about 1.5 million dictionary
lookups), not matching.  This is a material bottleneck in any beam that audits
thousands of candidates and is being ported to a batch C++ Hall/DM core.

### Upper-exact segmentation builder

Three trials of `build_k15_h30_segmentation.py` under `cProfile`:

```text
38,445,221 Python calls; 5.50 seconds
endpoint compiler labels: 3.29 seconds / 10,616 calls
remaining randomized cut trial loop: approximately 2 seconds for 3 trials
```

The production 1,000-trial runs take minutes.  The complete builder hot path
(upper-loss accounting, exact action compatibility, compiler endpoint labels,
and randomized greedy trials) is being ported to C++.

### Iterative Hall-cut/Benders search

On the 96-component exact instance:

```text
Python dm_block: 0.181 seconds
all 836 seam weights: 1.097 seconds
compact PB encoding: 0.065 seconds
total Python per new Hall cut: about 1.34 seconds
Kissat after the first cut: already >100 seconds (hard cases)
```

Python is under two percent of the live hard-round wall time.  Porting the
orchestrator cannot materially accelerate the current gate; the native SAT
solver is the bottleneck.  A C++ batch seam-weight kernel remains useful only
if later instances produce many easy cuts.

## Process cleanup

Forty-two old pure-Python Hall/p3 beam processes and three superseded free
component enumerators were terminated on the H100 CPU host.  They had consumed
roughly forty cores for 25--50 minutes without beating Hall 30 and are now
strictly dominated by exact Hall-witness separation.  Active Benders/Kissat
and genuinely new seed-union searches were retained.

## Native deliverables

- exact Hall/DM batch CLI: **complete and regressed**;
- upper-exact/action segmentation builder: **complete and regressed**;
- optional batch fixed-target seam-weight kernel: conditional on new profiles;
- Python JSON/SAT orchestration: intentionally retained;
- Kissat: already native, retained.

### Completed exact-zero segmentation engine

```text
scratch/build_k15_h30_exactzero_fast.cpp
scratch/build_k15_fast_tools.sh
scratch/regress_k15_exactzero_fast.py
```

The C++ engine unifies upper crossing ledgers, compiler seam/endpoint labels,
joint seven-target action selection, and randomized safe filler cuts.  It
reproduces the Python action counts

```text
5397:52, 5801:19, 10794:42, 13589:7,
17738:61, 21588:45, 21672:46
```

and passes independent Python residence/upper audits.  H100 timing is about
0.01 seconds / 8.7 MB.  The comparable unified Python builder is 0.73 seconds
(about 73x slower); the older natural-root builder took about five minutes,
so the native engine is over 30,000x faster than the lane it supersedes.

### Completed Hall/DM engine

```text
scratch/fast_k15_hall_dm.cpp
scratch/fast_k15_hall_dm_cli.py
```

It supports batch certificates, arbitrary `--k/--depth`, exact Hall matching,
zero/unmatched targets, the full DM witness, fixed-target neighbourhoods, and
distance-signature histograms.  It agrees bit-for-bit with Python on Hall 30,
clean Hall 31, and the solved k=13 certificate.  Measured speedups are about
20x for Hall+DM and 31x for fixed-target distance batches.  The general-union
solver can select it via `FAST_K15_HALL_DM_BIN`.

### Completed union-motif engine

```text
scratch/fast_k15_union_motifs.cpp
scratch/regress_k15_fast_union_motifs.py
```

This enumerates every simple local path in a carrier-edge union that realizes
specified exact compiler targets.  On the Hall-30 plus dense `p1_2opt_smoke`
union its frozen undirected motif counts are

```text
10794:1850, 17738:254, 21588:143
```

(twice those counts in oriented form).  The native result is deterministic
and the counts were independently parsed and checked.  Because this exhaustive
regression is intentionally long on a laptop, `regress_k15_fast_tools.sh`
runs it only when `K15_LONG_REGRESSION=1`; production runs belong on the H100
CPU host.

Forty native-generated portfolio instances were produced in under one second;
all forty cut/action hashes were distinct and all exposed seven exact zero
actions with residence zero and complete upper shadows.  A larger 256-instance
portfolio is active on the H100 CPU host.

### General-union loop audit

After native Hall integration, a 12-round profile split each union round into
roughly

```text
Kissat/subprocess 0.215s; DIMACS write 0.089s;
path reconstruction 0.070s; chronology audit 0.056s;
native Hall process 0.018s.
```

No remaining Python function dominates the live loop; replacing any one gives
less than about a 25% total gain.  A separate end-of-run quadratic bug did
recompute source edge sets 13,026 times (84 million edge calls, 23.7 seconds);
it was fixed by precomputing the source edge sets once.  This affects exact
exhaustion finalization, not the per-round search.

### H100 scratch cleanup

The audit found 17,943 stale `.cnf/.out` files occupying 54.26 GiB in the
specific `/dev/shm/k15_rotation` directory.  Completed temporary solver files
were removed while every basename referenced by a live process was preserved.
Certificates, JSON results, source inputs, and logs were untouched.  Available
shared memory increased from zero to about 55 GiB.  The removed DIMACS/output
files are regenerable but were not otherwise recoverable.

No native result is authoritative until it agrees with the Python reference
on Hall 30, clean Hall 31, and the solved k=11/k=13 certificates.

## Port/resource completion filter

The exact-zero generator now keeps its original fast mode by default.  An
optional completion mode and a standalone native auditor build the graph of
remaining oriented component ports after forced compiler actions, contract
the forced seams, and compute:

- connectedness of the fragment graph;
- maximum-cardinality port matching;
- resource-labelled reachability and port-disjoint lower-shadow matchings;
- a max-weight blossom upper bound for the fixed Hall-30 DM neighbourhood.

The blossom implementation was checked against brute force on 4,400 random
small graphs.  This filter rejects the richest historical 64-component source
without SAT: the full completion matching is `56/58`, and its optimistic fixed
DM value is at most 1,511 against the required 1,528.  The native tools are

```text
scratch/analyze_k15_action_compat.cpp
scratch/analyze_k15_port_resources.py
```

Compatibility conditioning is intentionally opt-in (`completion_attempts>0`)
in `build_k15_h30_exactzero_fast`; otherwise the generator retains its
subsecond deterministic regression.  Three conditioned 64/96-component
outputs pass topology but are still rejected by the weighted DM bound
(optimistic values 1,505--1,513).  The next generator objective must therefore
couple port completion and DM seam loss rather than filter them sequentially.

## Exact batch DM/compiler scorer

The remaining repeated Python compiler-signature loop has been replaced by

```text
scratch/k15_dm_batch_score.cpp
scratch/regress_k15_dm_batch_score.py
```

The tool has two exact modes: all cut gains for one or more DM witnesses, and
all intrinsic/directed-seam weights for a segmented carrier.  Regression on
the frozen Hall-30 and Hall-29 certificates checks every one of 6,434 cut
entries.  A second regression checks 2,204 directed arc/witness seam weights
against complete Python concatenation scoring.  Both are exact.  The latter
test also caught and removed an earlier local-collar approximation: native
seam weights now score the full component concatenation.

Measured locally, two-witness segment scoring falls from 2.60 seconds in
Python to 0.39 seconds natively (6.6x); individual complete cut arrays take
about 0.28 seconds.  This output is now the input to the multi-witness H29
portfolio, while Python remains responsible only for JSON orchestration and
the native CP-SAT/Kissat invocation.

## Reproducible optimized build

`scratch/build_k15_fast_tools.sh` now builds every completed native hot-path
tool with C++20, `-O3 -march=native -DNDEBUG`.  The regression driver includes
the exact-zero generator, Hall/DM engine, and batch DM scorer; the deliberately
long union-motif test remains opt-in through `K15_LONG_REGRESSION=1`.

## Native relabel pattern bundle

The two remaining repeated prefix enumerators in the relabel-trade lane,
`mixed_upper_patterns()` and `enumerate_bad_residence_patterns()`, are now
implemented by the `--bundle` mode of
`scratch/fast_k15_relabel_fixed_patterns.cpp`.  One native traversal emits
signed residence clauses, all rank-q upper target patterns for q=1..7, and
optionally the full-boundary multi-DM pricing payload.  The Python driver
accepts the result through `--native-pattern-bundle-bin` or a cached
`--native-pattern-bundle`; CP-SAT model construction remains in Python while
the actual solve runs in OR-Tools' native core.

`scratch/regress_k15_relabel_pattern_bundle.py` compares the complete signed
sets—not samples—on three structurally different cubes: a transposition, the
Hall-29 winning double transposition, and a 3-cycle.  H100 regression passes
with 336,737 / 909,912 / 161,430 enumerated prefixes respectively.  On the
largest case, end-to-end model build falls from 5.11 to 2.69 seconds; the
remaining roughly two seconds instantiate native CP-SAT objects rather than
perform combinatorial enumeration in Python.
