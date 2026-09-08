# K17 Quotient Search f6c2e

Standalone fresh-seed work; no existing source, handoff, answer, or parent job is modified.
Remote isolation: `/home/amodo/or15/work/k17_quotient_search_20260905_f6c2e`.

Sources live in `scripts/k17_quotient_search_20260905_f6c2e*`.
The C++ text input is `K17QF1 17 1430 24310 3` followed by 1430 triples
`canonical_lower_mask M0_added_coordinate P_added_coordinate`. The columns
preserve disjoint perfect-matching colours, not physical chronological order.
Resume with `--resume BODY.txt --output NEW_PREFIX --seed INTEGER --seconds 240`.
JSON exports contain sorted, explicit uncoloured `choices` for pipeline import.

Quotient defect order: `bad2`, `bad3`, `2*bad2+bad3`, missing
`[U1,L2,U2,L3]`, collision counts, wrong-rank starts, and voltage topology.
All these counts are quotient orbit counts except explicit physical cycle sizes.
Each bad run orbit has 17 physical copies. Zero gaps are not forbidden.
Quotient loops are excluded, but parallel incidence IDs and support-one exchanges
are retained. Topology is not constrained to one component.

The entry/deletion residence equalities account for nonconstant positive runs.
A voltage-zero physical triangle additionally has constant positive traces of
length three; their contribution is counted in the topology stage and explicitly
tested. Arbitrary-width physical upper unions stop only at a component's total
union, never at an arbitrary window-width cutoff.

## Result

Four of eight fresh 240-second searches reached zero residence defects and zero
missing U1 orbits. The recommended restart is:

- Body: `batch240/seed17090501.best.txt`
- Explicit choices: `batch240/seed17090501.best.json`
- Independent physical audit: `batch240/seed17090501.best.independent_audit.json`
- Pipeline audit: `batch240/seed17090501.best.pipeline_audit.json`
- Body SHA-256: `3e9027a8ff08709c703438cd8c4722db264226a026d1e7458e582bd75e69b25e`

All paths in this document, unless otherwise stated, are relative to this
artifact directory. This is an exact factor seed, not a compiled word.

Recommended factor's full defect vector:

```text
bad2_orbits = 0
bad3_orbits = 0
constant_bad3_orbits = 0
residence_shortfall_orbits = 0
missing_orbits [U1,L2,U2,L3] = [0,102,51,48]
pair_collisions [U1,L2,U2,L3] = [305,434,1056,1136]
invalid_rank_starts [U1,L2,U2,L3] = [0,0,69,0]
all_width_upper_missing_orbits ranks 10..17 = [0,51,9,0,0,0,0,0]
quotient_cycles = physical_cycles = 5
zero_voltage_cycles = quotient_loops = 0
physical_cycle_lengths = [23307,612,187,136,68]
degree2_rank9_owners = once_only_rank8_facets = 24310
minimum_positive_run = 4
short_zero_gaps_not_forbidden = 6562
```

Its fresh initial factor had residence shortfall 491 and missing decks
`[255,261,129,136]`. The final selected body was found at attempt 39,487,625.
The ASan reload `best_resume_checked.initial.txt` has exactly the same body hash.

## Search Runs

Eight single-thread search processes, each bounded to 240 seconds, ran together
on the SSH alias `h100` (actual hostname `arboghast`). All returned zero and were
waited/reaped by the runner. Total main search counts:

```text
attempts                 704874496
evaluated exact proposals 534159506
accepted                  15535782
support-one proposals     23908022
global/difference proposals  85807
matching recolourings        21508
annealing restarts              48
```

Main weighted-best results, all defects in quotient orbit units:

| Seed | Bad2 | Bad3 | Shortfall | U1 | L2 | U2 | L3 | Physical Cycles | Evaluated Proposals |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17090501 | 0 | 0 | 0 | 0 | 102 | 51 | 48 | 5 | 68944081 |
| 17090502 | 0 | 0 | 0 | 0 | 131 | 70 | 48 | 4 | 68093096 |
| 17090503 | 0 | 9 | 9 | 0 | 91 | 61 | 54 | 7 | 64463409 |
| 17090504 | 0 | 0 | 0 | 3 | 121 | 77 | 49 | 7 | 69735471 |
| 17090505 | 0 | 7 | 7 | 2 | 91 | 54 | 33 | 8 | 64613298 |
| 17090506 | 0 | 0 | 0 | 0 | 190 | 89 | 88 | 7 | 68206258 |
| 17090507 | 0 | 0 | 0 | 0 | 213 | 90 | 74 | 4 | 66869281 |
| 17090508 | 0 | 8 | 8 | 1 | 67 | 55 | 35 | 4 | 63234612 |

Each run also retains lexicographically best residence and U1 bodies. These
names are optimization categories, not assertions that their named defect is
zero. For example, seed 17090503's residence body has
`(bad2,bad3,shortfall; U1,L2,U2,L3; components) = (1,1,3; 0,106,74,45; 5)`.
Seed 17090504's residence body is a two-cycle resident factor with decks
`[2,163,64,48]`. All bodies, including the dirty alternatives, are restartable.

`batch240/commands.json` records all exact executable arguments and PIDs;
`batch240/finished.json` records exit codes and wall times. The PIDs were
2946799 through 2946806. `batch240_runner.log` ends `ALL_FINISHED count=8`.
A final `pgrep -af '[k]17_quotient_search_20260905_f6c2e'` on h100 produced no
matches. No parent CP-SAT process or file was touched.

## Verification

The extended suites passed without sanitizer diagnostics:

| Build | Factors | Delta/Full | Physical | Rollbacks | Support-One | Recolourings | Preferred Differences |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ASan/UBSan | 12 | 4880 | 144 | 2439 | 122 | 72 | 80 |
| Release | 24 | 9773 | 288 | 4712 | 243 | 144 | 173 |
| Total | 36 | 14653 | 432 | 7151 | 365 | 216 | 253 |

Each suite includes a forced physical triangle, random exact factors,
post-move comparisons of every coverage load, rollback checks, phase-only
parallel exchanges, factor recolouring, and preferred matching differences.
Physical audits reconstruct cyclic order from undirected adjacency, verify all
24310 owners and facets, count positive runs literally, and scan arbitrary-width
cyclic union decks. They do not use serialized row order as chronology.

Additional preflight work was a two-factor sanitizer smoke test (814 delta,
24 physical, 389 rollback checks), a 10-second release pilot (2,153,070 evaluated
proposals), and a one-second ASan resume search (14,045 evaluated proposals).
The final recommended body also passed an ASan/UBSan audit-only reload.

The independent Python auditor passed all 32 main exports (eight initial and
24 saved best-category exports), four pilot exports, and a repeated audit of
the selected factor during the pipeline attempt. It checks body/JSON agreement,
both coloured perfect matchings, physical topology and loads, positive and zero
run histograms, arbitrary-width upper decks, and saved C++ metrics. All source
and body hashes are recorded in `SHA256SUMS` and the per-candidate audits.

The independent existing pipeline successfully imported the selected explicit
choices and audited the cycle cover. It reported `carrier_pass=false` and
`connectivity_pending=true`. Compilation was deliberately not invoked across
failed carrier gates.

Remaining gates for the recommended seed:

- L2 rank-seven coverage: 102 missing orbits, or 1734 physical targets.
- L3 rank-six compiler positive degree: 48 missing orbits, or 816 physical targets.
- Upper rank eleven: 51 missing orbits, or 867 physical targets.
- Upper rank twelve: 9 missing orbits, or 153 physical targets.
- Connectivity/unit-voltage strict spiral: five physical components remain.
- Only after those gates: graded core/Hall matching, upper-safe cut, and direct
  compiled-word verification. None of these later gates has been claimed.

## Exact Commands

These are the executed commands, with repeated path prefixes factored into shell
variables for readability. Run from the repository root. The isolation directory
and `batch240` were NEW when created; use a new directory name to repeat the batch
without overwriting these artifacts. Time-based annealing makes a timed rerun
non-bit-identical; the preserved bodies give exact audit/restart inputs.

```bash
R=/home/amodo/or15/work/k17_quotient_search_20260905_f6c2e
S=k17_quotient_search_20260905_f6c2e

ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "ls -ld /home/amodo/or15/work"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "mkdir $R"
scp -o BatchMode=yes -o ClearAllForwardings=yes "scripts/$S.cpp" "scripts/${S}_audit.py" "scripts/${S}_runner.py" "h100:$R/"

ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "g++ -std=c++20 -O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer -Wall -Wextra -Wpedantic $R/$S.cpp -o $R/search_asan"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "g++ -std=c++20 -O3 -march=native -DNDEBUG -Wall -Wextra -Wpedantic $R/$S.cpp -o $R/search"

ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "env ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 $R/search_asan --self-test 2 --seed 17090599"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "$R/search --seed 17090500 --seconds 10 --output $R/pilot10"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "env ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 $R/search_asan --self-test 12 --seed 17090699 > $R/asan_selftest.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "$R/search --self-test 24 --seed 17090799 > $R/release_selftest.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "python3 $R/${S}_audit.py --directory $R --workers 2 > $R/pilot_independent.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "env ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 $R/search_asan --seed 17090899 --resume $R/pilot10.best.txt --seconds 1 --output $R/resume1 > $R/asan_resume.log 2>&1"

ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "python3 $R/${S}_runner.py --binary $R/search --directory $R/batch240 --seconds 240 --seed-base 17090501 --count 8 > $R/batch240_runner.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "python3 $R/${S}_audit.py --directory $R/batch240 --workers 8 > $R/batch240_independent.log 2>&1"

scp -o BatchMode=yes -o ClearAllForwardings=yes scratch/graded_quotient_pipeline.py "h100:$R/"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "python3 $R/${S}_audit.py $R/batch240/seed17090501.best.json --pipeline $R/graded_quotient_pipeline.py > $R/pipeline_attempt.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "env ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 $R/search_asan --seed 17090999 --resume $R/batch240/seed17090501.best.txt --audit-only --seconds 0 --output $R/best_resume_checked > $R/best_resume_asan.log 2>&1"
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "pgrep -af '[k]17_quotient_search_20260905_f6c2e'"

rsync -a --exclude=search --exclude=search_asan --exclude=__pycache__ -e "ssh -o BatchMode=yes -o ClearAllForwardings=yes" "h100:$R/" "scratch/$S/"
shasum -a 256 -c "scratch/$S/SHA256SUMS"
```

Example NEW continuation command (documented for use, not run in this task):

```bash
R=/home/amodo/or15/work/k17_quotient_search_20260905_f6c2e
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 "$R/search --resume $R/batch240/seed17090501.best.txt --seed 17091001 --seconds 240 --output $R/continuation17091001 --res 2.5 --u1 4 --l2 1 --u2 0.4 --l3 0.4 --hot 2 --cold 0.1"
```

The C++ search maintains four coverage-load decks with signed changed-support
deltas and separately counts bad2 and bad3. Its low topology penalty is a
delayed Metropolis filter after the local filter. It rebases every 32768
attempts, proposes preferred matching unions/difference cycles every 65536,
and anneals/restarts on 35-second epochs. Best weighted, residence-first, and
U1-first bodies are checkpointed every five seconds when improved, regardless
of whether they are resident. The full physical expansion is only used at
initialization, final saved-state audits, and explicit self-tests.
