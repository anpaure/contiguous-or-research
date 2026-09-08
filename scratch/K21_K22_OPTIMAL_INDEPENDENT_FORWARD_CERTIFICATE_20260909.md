# Independent forward verification proves the supplied 21/22 words optimal

Date: 2026-09-09. Status: **both complete cubes and both exact lower-bound equalities passed**.

The supplied literal words establish

    nu(21) = B(21) = 352719,
    nu(22) = B(22) = 705435.

One independently reviewed forward-first-occurrence checker verified every
nonempty target as an ordinary interval OR, and independently computed
the all-rank endpoint lower bounds. The literal lengths attain those
bounds. This is a finite optimality result at 21 and 22, not an all-k
equality theorem.

## 1. Fixed supplied inputs and exact result

| k | Literal length | Nonempty targets verified | Missing | Derived B(k) | Gap |
|---:|---:|---:|---:|---:|---:|
| 21 | 352,719 | 2,097,151 | 0 | 352,719 | 0 |
| 22 | 705,435 | 4,194,303 | 0 | 705,435 | 0 |

All letters were nonzero valid masks in their respective cubes. Every
rank's distinct target count equaled the full binomial layer. The numbers
of forward OR-change events examined were 4,937,973 and 10,228,713.

The raw inputs were supplied by the user, without modification:

- `k21_optimal352719.word`, 2,526,061 bytes, SHA-256
  `eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2`.
- `k22_optimal705435.word`, 5,347,789 bytes, SHA-256
  `a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd`.

Their file names and the user's claims were not correctness premises:
each byte hash, length, mask range and complete cube was checked.

## 2. Independent coverage method

The source is
[verify_k21_k22_optimal_forward_first_occurrence_20260909.py](verify_k21_k22_optimal_forward_first_occurrence_20260909.py),
SHA-256 `ce205cef9f5f2208bcaccd1bb2f1d25ecd29f19f01782c17040ab89874080312`.
It imports no previous verifier and uses neither a suffix-OR recurrence,
a segment tree, nor a cyclic extension.

For each ordinary start l, let p_x be the first occurrence at or after l
of coordinate x, or infinity if absent. For any ordinary endpoint r,
the OR of letters l through r consists precisely of the coordinates
with p_x<=r. Sorting the finite p_x therefore enumerates every distinct
OR at that start. When several coordinates have the same p_x, the checker
adds them together; it never invents a target inside a single letter.

The starts are swept backwards only to maintain these first-occurrence
positions efficiently. The OR enumeration from each start is forward
in endpoint order. All starts and every nonempty target are checked.
Each recorded witness has 0<=l<=r<N, with zero-based inclusive ordinary
endpoints. No circular interval is used.

Complete target-indexed start and end arrays are retained for both words.
They contain one witness for every target, with index 0 unused. The arrays
are signed 32-bit little-endian integers: each k21 array has 2,097,152 entries,
and each k22 array has 4,194,304 entries. The forward construction certifies
their OR values; it does not claim a separate range-OR replay in this run.
Root's separate suffix/range and cyclic/lift checks are independent work.

## 3. Exact all-rank lower-bound comparison

For each rank s, let m=binom(k,s) and let L be the total number of nonempty
targets of smaller rank. The established endpoint bound gives

    nu(k) >= m+tau,
    tau = min{t>=0 : L <= t*m + t*(t+1)/2}.

The checker evaluates every rank with exact integers, verifies that tau
satisfies the inequality and that tau-1 fails when tau>0, and then takes
the maximum. The unique maximizing rank is 11 for both inputs, with
tau=3 in each case.

At k=21 the rank size is 352,716 and L=1,048,575. The capacities at t=2
and t=3 are 705,435 and 1,058,154. Thus the rank-11 bound is 352,719.
At k=22 the rank size is 705,432 and L=1,744,435. The corresponding
capacities are 1,410,867 and 2,116,302, giving 705,435. Every other rank's
bound is recorded and is smaller.

Since the complete literal words have exactly these lengths, the upper
and lower bounds coincide. The final whole-run status required both
full-cube coverage and both equalities; coverage alone could not produce
`PASS_OPTIMAL_FULL_CUBES`.

## 4. Review, single bounded run and retained evidence

Root and the induction agent read the complete source and
[review plan](K21_K22_OPTIMAL_FORWARD_REVIEW_PLAN_20260909.md)
before the one authorized run. The finite-frontier agent also reread
the full derivative and its exact diff. The source and both raw hashes
were checked again remotely before execution. No source edits, retries,
alternative inputs or searches occurred after the source was frozen.

Execution was on h100, hostname `arboghast`, with 60 CPU seconds, 90 wall
seconds, 2 GiB address space and 256 MiB per output file, plus external
`timeout 90s`. It exited 0. Actual total CPU time was **7.738175413 seconds**;
actual wall time was **7.739107304718345 seconds**. The final status was
`PASS_OPTIMAL_FULL_CUBES`.

The complete artifact directory is
`scratch/k21_k22_optimal_forward_20260909/`:

- [Paired complete certificate](k21_k22_optimal_forward_20260909/k21_k22_optimal_forward_complete_certificate.json).
- [k21 complete report](k21_k22_optimal_forward_20260909/k21_forward_certificate.json)
  and [k22 complete report](k21_k22_optimal_forward_20260909/k22_forward_certificate.json).
- [k21 supplied raw copy](k21_k22_optimal_forward_20260909/k21_optimal352719.word)
  and [k22 supplied raw copy](k21_k22_optimal_forward_20260909/k22_optimal705435.word).
- All four `.int32` witness arrays, with their exact hashes in the reports.
- [Source snapshot](k21_k22_optimal_forward_20260909/checker.py),
  [run log](k21_k22_optimal_forward_20260909/run.log),
  [exact command](k21_k22_optimal_forward_20260909/exact_command.txt),
  [provenance](k21_k22_optimal_forward_20260909/PROVENANCE.md), and
  [remote hash manifest](k21_k22_optimal_forward_20260909/SHA256SUMS).

The paired report has SHA-256
`137029022789f1af18e949c870945a8b1d0bfb874b9e306f792b82770bdeb4fb`.
All 12 copied remote artifacts, including every witness array, passed
their stored SHA-256 manifest locally.

The earlier 352,862/705,724 forward checker was prepared and reviewed but
never executed; its files and every earlier result remain preserved.
This certificate does not reconstruct the user's search, cyclic core,
opening, or periodic lift, and it does not claim equality at higher k.
