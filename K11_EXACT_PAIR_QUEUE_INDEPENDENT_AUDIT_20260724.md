# Independent audit of the exact `k=11` pair-replacement queue

Date: 2026-07-24

## Verdict

`scratch/search_two_replacements_by_pair.cpp` is sound and complete for the
production invocation

```text
K=11, length=476, MAX_MISSING=64, DROP_LAST=0,
replacement values 1,...,2047.
```

If its terminal line is

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450
```

then it has screened every unordered position pair and every ordered pair of
nonzero replacement values, because

```text
113050 = binom(476,2)
473703127450 = 113050 * 2047^2.
```

The solver returns `10` only after independently materializing and exhaustively
verifying a universal candidate.  It returns `20` only after exhausting all
selected pairs.  The queue wrapper additionally requires the full pair/value
counts before accepting status `20`, and checks a status-`10` candidate with
both independent interval-OR verifiers before writing `SAT_VERIFIED`.

I found one resume-safety bug in the original queue wrapper.  Its old test

```bash
grep -Fq "$expected_sha"$'\t' "$ledger"
```

treated every prior ledger row as completed, including `ERROR_143`, other
`ERROR_*` rows, and `INCOMPLETE_UNSAT_SCREEN`.  Restarting after an interrupted
or incomplete seed could therefore skip that seed and eventually create a
worker `.COMPLETE` marker.  The local wrapper now parses the status column and
skips only `UNSAT_EXHAUSTIVE` or `SAT_VERIFIED` rows.  Its patched SHA-256 is

```text
65feda181de414af3bd67e01ce576af9f21390a5aecfdbf06e086cd993355030
```

The two live workers were deliberately left untouched.  At the time of this
audit both worker ledgers were empty and both first solver processes were still
running without interruption, so the resume bug had not affected any live
result.  If either old-wrapper worker is interrupted, the patched wrapper must
be installed before it is restarted.

## Exactness of the direct screen

For positions `p<q`, a target needs repair exactly when every old witness
interval contains `p` or `q`.  For fixed `p`, every witness avoiding `p`
requires `q` to lie in that witness interval.  The intersection of those
ordinary integer intervals is exactly the solver's `low/high` range.  Empty
old witness families require every pair; if every witness contains `p`, every
`q>p` is permitted.  Hence the pair repair mask is exact.

Every changed interval belongs to exactly one category:

1. `p` only, with new OR `base | a`;
2. `q` only, with new OR `base | b`;
3. both, with new OR `base | a | b`.

The `base` is the OR of every unchanged entry in that interval.  The source
enumerates all touched intervals, deduplicates only equal bases, and its three
coverage tables therefore give an exact existential witness test.  Targets
outside the repair mask retain an untouched old witness.  The bitmask equality
is consequently necessary and sufficient, not a heuristic pruning rule.

The value loops include all `2047^2` ordered pairs in `1,...,2047`.  A value is
allowed to equal the old entry, so the enumeration also contains every
zero-change and one-change case.  All fourteen frozen production snapshots
were independently inspected on the remote host: each has 476 entries, a
matching filename SHA-256, and values in the nonzero 11-bit range (minimum 1,
maximum at most 1990).

## Queue and snapshot audit

The complete manifest is copied before solving.  Each source is hashed before
copying, copied to a PID-specific temporary path, hashed again, and atomically
installed with `mv -n`; concurrent preflight workers cannot expose a partial
snapshot.  The installed snapshot is hashed both after preflight and before
each solver run.  This protects against the intended race with live
`best.word` replacement.  The files are hash-frozen by the wrapper, although
they are not made operating-system immutable; an adversarial external writer
between the final hash and solver open is outside the stated trusted-host
model.

Before solving, the queue requires verifier exit status `1`, the exact line

```text
length=476 covered=2046 required=2047
```

and exactly one listed missing mask.  On SAT it requires a 476-token candidate,
then both `verify_or_array` and `verify_or_suffix` must exit zero under
`set -e`.  On UNSAT it requires both exact exhaustive counters.  The two
workers use separate ledgers, so their appends do not race.

## Boundaries of the conclusion

The solver uses a 64-bit repair mask.  A global UNSAT conclusion is justified
only when the terminal selected-pair count is all `113050`; the queue enforces
this.  Replacement value zero is intentionally excluded because the project
uses nonzero word entries.  Generic parser limitations for invalid `K`, an
empty drop-last input, out-of-range seed entries, or words longer than 65,535
do not occur in this production invocation.

## Audited hashes

```text
69b6669501785d9fc8c15c226c109610cdd645029149dcd077eec19aff709f9d  scratch/search_two_replacements_by_pair.cpp
65feda181de414af3bd67e01ce576af9f21390a5aecfdbf06e086cd993355030  scratch/run_k11_exact_pair_seed_queue.sh
489c880219a92382608db7dcfa44bb62f012242b419dbbe030e604afbd423db4  scratch/k11_exact_pair_seed_queue_20260724.tsv
```

