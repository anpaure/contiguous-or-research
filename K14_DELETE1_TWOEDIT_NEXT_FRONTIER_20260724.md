# `k=14` next frontier: full delete-one/two-edit neighborhood

Date: 2026-07-24

## Recommendation

The next bounded exact search should cover every word obtained from the
certified 242-entry suffix by:

1. deleting any one of its 242 entries; and
2. replacing any unordered pair of the remaining 241 entries by two arbitrary
   nonzero 14-bit masks.

This is the smallest natural completion of the now-closed common-anchor
portfolio.  It is much broader, still has only 28 shared value bits, and its
exact provider formulas remain small.

There are

```text
242 * C(241,2) = 6,998,640 architectures
6,998,640 * 16,383^2 = 1,878,453,795,342,960 value tuples.
```

The certified common-anchor family contained 49,920 architectures, so the new
family is 140.20 times larger.  A SAT member gives a 3,675-entry universal
word.  Checked UNSAT for all 242 deletion-root formulas would certify that no
delete-one/two-replacement contraction of the known suffix works.  It would
not refute the unrestricted 241-entry append problem.

## Audit of the closed family

The bundle-wide manifest

```text
scratch/k14_onehole_twoedit_shard00_certified_20260724/SHA256SUMS
```

was rechecked from the workspace root.  All 305 entries pass.  All 26 proof
checker logs contain `s VERIFIED`, and all 26 immutable shards are therefore
certified UNSAT within their stated common-anchor scope.

## Exact deletion-root inventory

Recomputing the 260-target complement after every deletion gives

```text
208 roots with one hole
 31 roots with two holes
  3 roots with three holes
```

The old portfolio used only the 208 one-hole roots and only pairs containing
root position 3.  The 34 two/three-hole roots have not been searched by that
certificate.

An exact read-only profile over all 6,998,640 unordered pairs gives the number
of endangered old-prefix targets per architecture:

```text
3: 4,434,768
4: 2,011,470
5:   477,720
6:    69,372
7:     5,136
8:       174
```

Thus the mean is 3.4567 and the maximum is eight.  Exact provider profiles on
representative roots found no dead architecture and measured:

```text
root holes  provider mean  provider maximum
         1          6.641                18
         2          8.616                18
         3         10.608                21
```

These are profiling results, not UNSAT certificates.

## New separately named prototype

The frozen certified source was not edited.  The generalized per-root source
is

```text
scratch/k14_delete1_twoedit_cnf.cpp
```

with SHA-256

```text
7873d6744db1ed3d101eafaa1efc9eee1f00b06dc62025a4a7a4bffe30f3fbc6.
```

For one selected deletion it enumerates all 28,920 unordered position pairs.
Logical `x` is the lower physical replacement and logical `y` the upper.  Both
are arbitrary nonzero values.  Every old target with a witness avoiding both
positions is omitted safely.  Every endangered target is encoded by the same
three exact provider classes as the certified generator:

```text
base OR x,  base OR y,  base OR x OR y.
```

One exactly-selected pair shares the 28 value bits.  The source validates the
exact prefix complement, the certified suffix, and the deletion root's full
one-to-three-hole set before writing a formula.

The independent small-word provider regression is

```text
scratch/audit_delete1_twoedit_provider_identity_small.py
```

with SHA-256

```text
5c185f7c804471619095a468698d44035ae72f6b13ae31aa92b8cd925dea52cf.
```

It exhausts every unordered edit pair, every nonzero replacement pair, and
every nonzero target.  Its default run reports

```text
PASS words=40 architectures=400
exhaustive_target_checks=137200 seed=14242026
```

The generalized model decoder is

```text
scratch/decode_verify_k14_delete1_twoedit.py
```

with SHA-256

```text
d35915437cfa40dedc3449374a6f4b397ff2c7b671c7a24d153ba8bc59190902.
```

It validates the complete lexicographic 28,920-pair map, requires exactly one
selected architecture, a complete contradiction-free assignment of every
declared variable, and two nonzero values.  It performs direct quadratic
interval-OR enumeration and publishes a candidate only after both external
verifiers succeed.  Its map parser passes on the measured deletion-241 map.

The independent decoder/publisher audit is

```text
scratch/audit_decode_verify_k14_delete1_twoedit.py
```

with SHA-256

```text
40040a1ab98f1918459a388242ea4fc73a3e793226b63e136c23d3300e25f00c.
```

It first runs the real quadratic enumerator on the certified 3,676-entry
word.  Because no 3,675-entry witness is known, its accepted-path test then
uses a complete synthetic assignment and replaces only the final universality
predicate with an assertion on the independently reconstructed candidate.
The real publisher, temporary-file discipline, and two real mock verifier
subprocesses remain active.  The synthetic path publishes exactly once and
only after both mock verifiers succeed.

The audit also confirms fail-closed behavior for:

```text
wrong complete-pair inventory
two selected case variables
a zero replacement value
one missing declared-variable literal
a malformed model literal
a duplicate model literal
an external verifier returning exit 9
```

Every negative case exited nonzero and emitted no candidate.  The verifier
failure also left no temporary `.verifying` file.  The complete audit took
3.5 seconds.

The independent production-scale semantic auditor is

```text
scratch/audit_k14_delete1_twoedit_cnf.py
```

with SHA-256

```text
b8a61062dc9dae628960217194daa3275e17e3ddc616044ce92b778ff7da45c2.
```

It imports no generator code or provider table.  Starting from the frozen
prefix, missing family, suffix, and deletion index, it independently derives
the root holes, complete lexicographic pair inventory, avoiding witnesses,
minimal provider needs, provider ownership, sequential exactly-one encoding,
stats ledger, map events, and every DIMACS clause.  The CNF is consumed as a
stream in exact clause order, so the largest measured formula does not require
a multi-million-clause in-memory multiset.

A warning-clean C++20 build succeeded.  Two temporary production-scale
generations measured:

```text
deletion 241 (one hole):
  cases=28,920 variables=249,922 clauses=2,979,495
  unsafe=95,621 providers=192,055 dead=0
  CNF 38 MiB, map 12 MiB

deletion 0 (three holes):
  cases=28,920 variables=364,637 clauses=4,766,269
  unsafe=152,742 providers=306,770 dead=0
  CNF 61 MiB, map 19 MiB
```

An independent Clang ASan/UBSan build regenerated deletion 241.  Formula,
map, and stats were byte-identical to the optimized GCC outputs:

```text
c462b33f27d54b234c057ecf5842154c9d0ce14a8a18828d574ac0494a464828  CNF
8f486c5880f1a7dc31cf09a4f2215bfdb62b22358cb7a2e18d8827fef85e716d  map
2285539be38c8b9ecbe9d28bc4196ece9672658e74c3f8bebb670f656a991e82  stats
```

No SAT solver was launched, and these temporary generations are not
certificates.

The new auditor passed both production-scale examples:

```text
PASS deleted=241 root_missing=1 cases=28920
unsafe=95621 providers=192055 types={'both': 813, 'x': 95621, 'y': 95621}
max_unsafe=7 max_providers=18 variables=249922 clauses=2979495
semantic_cases=37 target_checks=153920 seed=14242027

PASS deleted=0 root_missing=3 cases=28920
unsafe=152742 providers=306770 types={'both': 1286, 'x': 152742, 'y': 152742}
max_unsafe=8 max_providers=21 variables=364637 clauses=4766269
semantic_cases=37 target_checks=153920 seed=14242027
```

Wall times were 5.4 and 7.0 seconds respectively.  Two negative tests also
passed: changing the first sequential clause was rejected at that exact
clause, and changing pair-map case 0 from `(0,1)` to `(0,2)` was rejected as
an inventory mismatch.  Both corrupted inputs exited nonzero.

## Authoritative root ledger and audited production runner

The complete deletion-root order is frozen in

```text
scratch/k14_delete1_root_manifest.tsv
```

with SHA-256

```text
c1bace750348f57022be094c90969f908171472173a72120ff8a1db748a878db.
```

It has one header plus all 242 deletion roots, records each root's exact
missing-target count and sorted target list, and has the independently checked
histogram `1:208, 2:31, 3:3`.  Priorities 0--4 are deletions
`241,204,0,1,13`; priorities 5--35 are exactly all 31 two-hole roots; the
remaining one-hole roots follow.  The reproducing program is

```text
scratch/build_k14_delete1_root_manifest.py
238afa2e862d8b8f91cfb155484202ca3e802ca4e5ce4ea4e578f272ffe4dad1
```

and reconstructs the checked-in manifest byte for byte from the three frozen
word inputs.

The production per-root driver is

```text
scratch/run_k14_delete1_twoedit_root.sh
bf134d5d0e6f4648c9be2cee5f6c6d8a770b4a2164181b980995a31d0b253949
```

Its two explicit modes are

```text
scratch/run_k14_delete1_twoedit_root.sh prepare DELETED WORK
scratch/run_k14_delete1_twoedit_root.sh search \
  DELETED WORK ATTEMPT CPU SEED SOLVE_SECONDS CHECK_SECONDS
```

`prepare` checks hard-coded hashes of all three inputs, generator, independent
CNF auditor, hardened decoder, root manifest, and manifest builder.  It freezes
them into a temporary root bundle, compiles the generator warning-clean,
generates CNF/map/stats, independently audits every clause, reconstructs the
complete 242-root manifest, and cross-checks the selected root's generated
missing count and targets against its authoritative row.  It hashes every
artifact into `PREPARED.sha256`, writes `PREPARED`, and installs the bundle by
an atomic same-filesystem rename protected by a per-root prepare lock.  The
atomic marker is checked against separately hashed `BUNDLE.metadata`.  A
completed prepare is idempotently reused; an incomplete, conflicting, or
hash-drifted bundle fails closed.

`search` rechecks the prepared hash manifest and root identity before creating
an immutable attempt directory.  Kissat is invoked with an explicit DRAT proof
path and bounded time/resource settings.  The decoder and both SAT verifiers
are separately timeout- and address-space-bounded; SAT output is accepted only
after complete-assignment checks, direct quadratic OR enumeration, and fresh
runs of both independent verifiers.  The DRAT checker has the same bounds.
UNSAT is accepted only when a nonempty proof is checked by `drat-trim` and its
exactly one `s VERIFIED` line and no contradictory `s ...` verdict are present
after treating carriage returns as line
boundaries.  Checker-output bytes remain unchanged in the raw log (followed only by the
runner's exit-code record); the normalized stream is stored separately.
Tool paths/hashes, affinity mode, resource
limit, seed, and time limits are frozen in `START.manifest`.
`CLASSIFICATION` is written last and must agree with separately hashed
`RESULT.metadata` and a second SHA-256 manifest over the result artifacts.
Classified retries first require the identical start parameters and current
prepared-bundle hash, then replay the old status without requiring the external
tools still to exist.  An unclassified partial attempt is retained and never
overwritten.

The synthetic lifecycle audit is

```text
scratch/audit_run_k14_delete1_twoedit_root.sh
ba03733ca0cfed1670debb53f6d8ba7c15c61664aeec35c496f7d1f22567fbc4
```

using the checked-in fake-tool multiplexer

```text
scratch/fake_k14_delete1_twoedit_runner_tool.sh
6730936533eba3d5174c5b52d5043152573d86d39778d47fa24a844472611c0e
```

It passed prepare/reuse, independent manifest reconstruction, two frozen-input
hash guards, deletion-root identity binding, synthetic `UNSAT_VERIFIED`, and
an independently exercised CR-prefixed `\rs VERIFIED` verdict whose raw and
normalized logs were both checked, plus a verified verdict without a terminal
line feed.  A mixed `s VERIFIED`/`s NOT VERIFIED` output is rejected.  Its
negative classifications include
`SAT_REJECTED`, `UNSAT_PROOF_REJECTED`,
an exit-zero false checker verdict containing only `s NOT VERIFIED`,
`UNSAT_CHECK_TIMEOUT`, `UNSAT_CHECK_KILLED_137`, `TIMEOUT`, `KILLED_137`, and
`SOLVER_ERROR`.  It also passed immutable classified restart without external
tools, changed-parameter replay rejection, prepare locking, malformed-resource
rejection, prepared/result marker integrity, and incomplete-attempt guards.
A separate prepare of the largest measured three-hole class, deletion 0,
produced and audited the exact
metadata

```text
priority=2
root_missing=3
root_missing_targets=8015,13423,13439
```

with a valid full bundle manifest.  These were prepare/control-flow tests;
no real SAT search was launched and Purple was not contacted or modified.

An independent final read-only review found no remaining
certificate-acceptance correctness defect.  Residual operational caveats are:
the production search path is Linux-specific (`timeout`, `taskset`, optional
`prlimit`, and `/proc`); the prepare lock protects cooperating runners rather
than an out-of-band writer; and the target host should receive one tiny
real-Kissat/real-`drat-trim` compatibility smoke test before launching the
portfolio.  Kissat's binary-DRAT default is compatible with `drat-trim`'s
automatic format detection.

The frozen inputs and all runner/generator/auditor sources above are bound by

```text
scratch/k14_delete1_twoedit_runner_SHA256SUMS
a8877341087d46687b5b98d3546d69224faf662746d16a52e366c87939b76499
```

and `sha256sum -c` passes for all 13 entries.

## Production implementation and certification plan

1. Require optimized and ASan/UBSan generators to produce byte-identical
   formula, map, and stats files on deletion roots 241, 204, 0, 1, and 13.
2. Run checked-proof calibration formulas in this order:
   deletion 241, deletion 204, then the three-hole deletions 0, 1, and 13.
   The first two are the deletion phases underlying the live construction-led
   append branches 5 and 36.  The three-hole roots are entirely outside the
   closed common-anchor portfolio.
3. If calibration is healthy, finish all 31 two-hole roots, then the remaining
   one-hole roots.  Use one immutable formula and proof obligation per
   deletion root.
4. A SAT result is accepted only after direct enumeration and both independent
   verifiers.  An UNSAT result is accepted only after an independently checked
   DRAT/LRAT proof and a hash manifest binding inputs, source, formula, map,
   stats, proof, and checker log.

## Resource estimate

Scaling from the 26 checked anchor-star shards and the measured new formulas:

```text
per deletion root:       0.25--0.37 M variables
                         3.0--4.8 M clauses
                         50--80 MiB formula+map
all 242 roots retained:  roughly 10--15 GiB formula/map artifacts
solver CPU:              roughly 1.5--2 core-hours if lucky preprocessing
full audited pipeline:   roughly 6--8 core-hours plus storage I/O
proof-only storage:      order 0.3 GiB if proof density scales linearly
```

The time estimates are extrapolations, not guarantees.  Any calibration root
that exceeds a five-minute solve quantum should be inspected before launching
the full portfolio.  On 16--32 free cores, the expected compute wall time is
tens of minutes, with artifact I/O likely dominant.

The Purple overlay currently has only about 1.1 GiB free.  It can hold one
transient root formula after the live append searches exit, but it cannot hold
the full certificate portfolio.  Full proof production needs external or
streamed storage.  Do not interrupt the live branch-5 or branch-36 jobs.

## Live unrestricted append searches

At `2026-07-24T12:35:35Z`, the no-proof Purple searches were still healthy:

```text
branch 5  PID 191197  elapsed 5:03:04  CPU 5:03:01  RSS 1.11 GiB
branch 36 PID 191200  elapsed 5:03:04  CPU 5:03:02  RSS 1.02 GiB
```

Neither had emitted a candidate or terminal status.  They retain their
existing bounded timeout near `13:32Z`; no process was interrupted or added.
The local provider portfolio is logically separate and should be run only on
newly idle resources.

## Three-edit fallback

If the full two-edit neighborhood is UNSAT, the next discovery family should
fix root position 3 and choose two further positions.  Across all deletions it
has

```text
242 * C(240,2) = 6,940,560 architectures
```

and three arbitrary nonzero values.  A preliminary exact incidence profile
has mean 4.458 and maximum nine endangered targets.  Because three physical
positions admit six contiguous provider roles, this formula family should be
several times larger than the two-edit family but remains plausible on a
selected-root tranche.  Start only with deletions 241, 204, 0, 1, and 13;
do not launch the all-root three-edit family before measuring those formulas.
