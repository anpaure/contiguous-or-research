**Result**
An independent six-minute, four-CPU-worker run on `h100` produced two literal
17-bit OR-universal words of length **25745**, improving the authenticated
25746 upper bound by one position. Both cover **131071/131071** nonempty masks
using nonempty contiguous, nonwrapping intervals. Every letter is nonempty
and at most 131071.

The resulting interval is `24313 <= nu(17) <= 25745`, leaving a gap of 1432.
This is not a length-24313 construction, an optimality claim, or a result about
the parent quotient/carrier search.

No `answers/` file, `MASTER_HANDOFF.md`, existing script, or parent search file
was edited. The baseline still has SHA-256
`f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b`.

**Retained Witnesses**
Local artifact directory: `scratch/k17_literal_compress_20260905_a19f7/`.
Isolated remote directory: `/tmp/k17_literal_compress_20260905_a19f7/` on `h100`.

Preferred witness, with the simpler replay:

```text
scratch/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.k17_upper25745.worker3.word
length: 25745
covered: 131071
missing: 0
SHA-256: ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38
```

Independent alternate search result:

```text
scratch/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.k17_upper25745.worker1.word
length: 25745
covered: 131071
missing: 0
SHA-256: 4baf8eed9a3fea96563bc45029bba888d87e2969fabc5299cbe739cbf520dc21
```

The `.best.word` files are byte-identical copies of these named witnesses.
The `.near.word` files are explicitly deficient search diagnostics, **not**
upper-bound certificates.

**Deterministic Replay**
Let `X` be the first 12873 letters of the authenticated baseline, and set
`z = 65536`. The preferred witness has the following exact recipe:

```python
Y = X[1:][::-1] + [65536, 50122, 33642] + [x | 65536 for x in X[3:]]
```

Its length is `12872 + 3 + 12870 = 25745`. Relative to the reversed-parent,
reversed-marked-copy lift (variant 3), this is the following zero-based edit
recipe: delete original position 12872 (mask 50120), then replace candidate
positions 12873 and 12874 by 50122 and 33642. Their old values were 115530 and
99146. This is one deletion plus two substitutions, not a safe deletion alone.

The replay mode needs only the authenticated baseline in its input directory;
it does not read a search candidate. It rebuilds the word, performs full
literal verification, and requires the exact preferred-witness hash above:

```bash
python3 scripts/k17_literal_compress_20260905_a19f7_audit.py scratch/k17_literal_compress_20260905_a19f7 --replay
```

The alternate witness has a one-deletion, twelve-substitution replay in
`k17_literal_compress_20260905_a19f7.audit.json`. Neither recipe is asserted to
generalize to arbitrary parent words.

**Implementation**
New files are confined to this unique prefix under `scripts/`:

- `k17_literal_compress_20260905_a19f7.cpp`: exact multiplicity engine, census, repair search, and brute-force self-tests.
- `k17_literal_compress_20260905_a19f7.py`: authenticated lift variants, bounded worker controller, independent suffix-set verifier, and verifier tests.
- `k17_literal_compress_20260905_a19f7_audit.py`: independent sampled census checks, exact edit reconstruction, and baseline-only replay.
- `k17_literal_compress_20260905_a19f7_RUN.md`: this record.

The C++ engine counts all literal intervals with 64-bit multiplicities.
Compressed suffix-OR initialization costs `O(kW + 2^k)`. An OR/count segment
tree supplies the left-suffix and right-prefix profiles around an edit.
Each profile has at most `k+1` entries including the empty boundary choice.
An edit partitions affected intervals into internal, left-prefix,
suffix-right, and fully crossing classes. Exact deltas cost
`O(k log W + k^2)` for the one/two-letter edits used here. If an adjacent
rewrite preserves the pair's OR, the fully crossing contribution cancels.
There is no full-word or quadratic `W^2` recomputation per attempted edit.
Full suffix-count audits occur at checkpoints and before saving a witness.

Tombstones are internal tree bookkeeping only; output never contains zero.
Search episodes delete or OR-merge one marked-side position, then try
targeted missing-mask rewrites, bit changes, adjacent swaps, and bit transfers.
Non-universal intermediate states are allowed, with exact missing-mask counts
and bounded annealing. Only fully checked universal improvements are saved as
`.best.word`. Initial deletions avoid the bare new-bit singleton and favor the
marked side; repairs can subsequently change the shore of a letter.

The four starting variants independently reverse the unmarked parent and/or
its truncated marked copy. Each starting word was independently verified.

**Run Counts**
All four search workers returned zero. The driver took 360.826198 seconds;
each worker stopped at approximately 360.005 seconds including its census.
The controller's per-child fallback timeout was 420 seconds. No unrelated
process was killed, and no search worker remains running.

| Worker | Seed | Logged proposals | Accepted repair proposals | Episodes | Best length |
|---|---:|---:|---:|---:|---:|
| 0 | 202609050 | 75989461 | 14675636 | 30128 | 25746 |
| 1 | 202609051 | 75166565 | 14670800 | 29730 | 25745 |
| 2 | 202609052 | 74998189 | 14214317 | 29826 | 25746 |
| 3 | 202609053 | 75187732 | 14227621 | 29738 | 25745 |

Total: **301341947 logged proposals**, **57788374 accepted repair proposals**.
These counts include revisits, neutral moves, and no-ops; they are not counts
of distinct candidate words. Worker 1 first succeeded at 0.473068 seconds,
worker 3 at 9.189400 seconds. No shorter verified word was found thereafter.
The log field `best_missing_at_shorter=0` is a minimum over the worker's whole
history and refers to its successful 25745 word, not to a 25744 construction.

The main-run starting-word censuses contain **205964** checks: 25746 deletions
and 25745 adjacent OR-merges on each of four variants. The original baseline
admits no safe single move; every deletion and merge loses at least two masks.
The reversed-copy variants have a one-hole bare-bridge removal, whose sole
missing target is the mandatory singleton 65536.

The final two witness censuses add **102978** checks: 25745 deletions and 25744
adjacent OR-merges per word. Every such move loses at least two masks. This is
only a fixed-word one-move limitation, not a no-go for further combined edits.
A preliminary census-only run repeated the four starting-word censuses before
the timed search; it is not included in the logged proposal count above.

**Verification**
- C++ ASan/UBSan self-test: 68750 local-delta comparisons against explicit quadratic enumeration on small random words, including deletions, merges, substitutions, swaps, commits, and tombstones.
- A 100000-letter repeated-mask test counted 5000050000 intervals, checking 64-bit multiplicities.
- Python verifier: three passing tests, including malformed/empty/out-of-range masks, exhaustive small suffix-versus-brute coverage checks, and a nonwrapping counterexample.
- Independent audit: all 205964 starting-census rows checked for bookkeeping; 124 endpoint/low-damage/random moves checked by a separate full-word suffix-set computation.
- Both witnesses passed the independent suffix-set verifier locally and remotely, covering all 131071 masks with maximum suffix frontier 12.
- Both also passed the unmodified repository `verify_exact_or_word.py` on `h100`, with `--k 17 --allow-longer`.

The repository verifier enumerated 103719368 intervals up to full OR for
worker 1, and 103719560 for worker 3. Both reported
`VERIFIED_UNIVERSAL_UPPER_BOUND`, `missing_masks=0`, and `middle_row_exact=false`.
The actual number of all literal intervals in either word is 331415385;
the C++ multiplicity checks account for all of them.

Important artifact files inside the local directory are
`k17_literal_compress_20260905_a19f7.commands.json`,
`k17_literal_compress_20260905_a19f7.summary.json`,
`k17_literal_compress_20260905_a19f7.audit.json`,
`worker1.standard.verify.json`, `worker3.standard.verify.json`,
`self_test_sanitize.log`, `python_tests.log`, and all `.census.tsv`/worker logs.

**Exact Commands**
Commands below were issued from `/Users/amir.nuriyev/Documents/problem`.
Remote commands use absolute paths; the Python controller explicitly sets its
working directory. The retained run directory must not be recreated over an
unrelated run. For a fresh search, choose a fresh directory name.

Parent verification, isolated deployment:

```bash
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'ls -ld /tmp'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'mkdir /tmp/k17_literal_compress_20260905_a19f7'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'ls -ld /tmp/k17_literal_compress_20260905_a19f7'
scp -o BatchMode=yes -o ClearAllForwardings=yes scripts/k17_literal_compress_20260905_a19f7.cpp scripts/k17_literal_compress_20260905_a19f7.py answers/k17_upper25746.word h100:/tmp/k17_literal_compress_20260905_a19f7/
```

Retained optimized build and tests:

```bash
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'g++ -std=c++17 -O2 -march=native -Wall -Wextra -Wpedantic /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.cpp -o /tmp/k17_literal_compress_20260905_a19f7/compressor && /tmp/k17_literal_compress_20260905_a19f7/compressor --self-test'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'g++ -std=c++17 -O1 -g -Wall -Wextra -Wpedantic -fsanitize=address,undefined -fno-omit-frame-pointer /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.cpp -o /tmp/k17_literal_compress_20260905_a19f7/compressor_sanitize && /tmp/k17_literal_compress_20260905_a19f7/compressor_sanitize --self-test > /tmp/k17_literal_compress_20260905_a19f7/self_test_sanitize.log && python3 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.py test > /tmp/k17_literal_compress_20260905_a19f7/python_tests.log 2>&1'
```

The preliminary census invocation and the timed launch:

```bash
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'python3 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.py run --directory /tmp/k17_literal_compress_20260905_a19f7 --seconds 0 --workers 4'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'nohup python3 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.py run --directory /tmp/k17_literal_compress_20260905_a19f7 --seconds 360 --workers 4 > /tmp/k17_literal_compress_20260905_a19f7/driver.log 2>&1 < /dev/null &'
```

The exact four child command lines, cwd, budgets, driver PID, and timed-source
hashes are in `k17_literal_compress_20260905_a19f7.commands.json`. Driver PID
was 2940185. The following check observed exactly four single-threaded children
at 100% CPU, then no children after the bounded run:

```bash
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'ps -o pid,ppid,etime,pcpu,stat,comm --ppid 2940185'
```

Post-run independent verification and audit (run only after the four workers
exited; the two verifiers, audit, and sequential final-census task used at most
four CPUs in parallel):

```bash
scp -C -o BatchMode=yes -o ClearAllForwardings=yes scripts/k17_literal_compress_20260905_a19f7_audit.py scratch/verify_exact_or_word.py h100:/tmp/k17_literal_compress_20260905_a19f7/
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'python3 /tmp/k17_literal_compress_20260905_a19f7/verify_exact_or_word.py /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker1.best.word --k 17 --allow-longer --output /tmp/k17_literal_compress_20260905_a19f7/worker1.standard.verify.json'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'python3 /tmp/k17_literal_compress_20260905_a19f7/verify_exact_or_word.py /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker3.best.word --k 17 --allow-longer --output /tmp/k17_literal_compress_20260905_a19f7/worker3.standard.verify.json'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'python3 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7_audit.py /tmp/k17_literal_compress_20260905_a19f7 > /tmp/k17_literal_compress_20260905_a19f7/independent_audit.log'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 '/tmp/k17_literal_compress_20260905_a19f7/compressor 17 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker1.best.word /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker1.final 0 202609051 census > /tmp/k17_literal_compress_20260905_a19f7/worker1.final.census.log && /tmp/k17_literal_compress_20260905_a19f7/compressor 17 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker3.best.word /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.worker3.final 0 202609053 census > /tmp/k17_literal_compress_20260905_a19f7/worker3.final.census.log'
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'python3 /tmp/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7_audit.py /tmp/k17_literal_compress_20260905_a19f7 --replay'
```

Local artifact directory setup and final compressed retrieval:

```bash
ls -ld scripts scratch /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode
mkdir scratch/k17_literal_compress_20260905_a19f7
ssh -o BatchMode=yes -o ClearAllForwardings=yes h100 'tar -czf - --exclude=./artifacts.tar.gz --exclude=./compressor --exclude=./compressor_sanitize --exclude=./__pycache__ -C /tmp/k17_literal_compress_20260905_a19f7 .' > scratch/k17_literal_compress_20260905_a19f7/artifacts.tar.gz && tar -xzf scratch/k17_literal_compress_20260905_a19f7/artifacts.tar.gz -C scratch/k17_literal_compress_20260905_a19f7
```

An initial uncompressed census transfer timed out after 30 seconds; the final
compressed retrieval replaced its partial files. An initial attempt to create
the archive inside the directory being archived reported a directory-change
warning; streaming tar through SSH avoided that issue. Neither affected the
search or verified words. An early diagnostic `-O3` build emitted GCC optimizer
warnings; the timed run used the clean `-O2` build above and passed sanitizers.

Quick local literal verification of the named preferred witness:

```bash
python3 scripts/k17_literal_compress_20260905_a19f7.py verify scratch/k17_literal_compress_20260905_a19f7/k17_literal_compress_20260905_a19f7.k17_upper25745.worker3.word
```

**Source Hashes**
```text
92d4ff546f311dbc75f79e21c3ee43d92b16010c6537eb4c47d8559ac6c79aba  k17_literal_compress_20260905_a19f7.cpp
fd994b11a586c0bf66ed2e9840af3672e816cddbc110bd742f5e4520498a40d7  k17_literal_compress_20260905_a19f7.py
81fe2b617f36367ca26c656baaa61d163cc4a2d2df0d819db03c1fd82d5da493  k17_literal_compress_20260905_a19f7_audit.py
9d3498964c5b2eb83dcf6e36727e9b0e30cc2e17bac2db7ef057138cef1dd26d  verify_exact_or_word.py (unmodified repository verifier)
```
