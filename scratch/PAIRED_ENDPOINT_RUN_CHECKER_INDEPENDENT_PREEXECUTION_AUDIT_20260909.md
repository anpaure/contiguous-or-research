# Independent pre-execution audit of the paired-endpoint run checker

Date: 2026-09-09. Full-source review by `exact_equality_structure` of
[verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py](verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py).

**PASS.** No blocking correctness issue was found. This audit did not
run, import, or compile the checker. Its finite checks remain proposed
until a separately reported execution completes.

## 1. Shared-endpoint proof implemented by the small cases

Fix a marked coordinate z and a rank s. Choose one actual interval
witness for each present unmarked rank-s target and each present marked
rank-(s+1) target. Within either family, distinct target witnesses have
different right endpoints, since suffix ORs at an endpoint form a chain.

If the two families use the same endpoint, let their targets be D and E.
They are comparable suffix ORs, `|E|=|D|+1`, z belongs to E and not D,
so `E=D union {z}`. The endpoint is unmarked. Let q be the last marked
position at or before it. The old witness starts strictly after q and
the marked witness starts at or before q. Consequently the entire
unmarked-run prefix from q+1 through the shared endpoint has OR exactly D.

Within any one unmarked run these prefixes are nested and have at most
one distinct rank-s value. The selected old targets are distinct and
each was assigned only one endpoint. Shared endpoints therefore inject
into distinct unmarked runs following an exit. This proves, for partial
as well as universal words,

    d_old,s + d_marked,s+1 <= N + R_exit.

Reversing the word gives the entrance version.

The code implements precisely this argument: it checks target equality,
actual last-mark order, run-prefix equality, the projection of the last
marked letter, and distinct run identifiers. It directly OR-replays both
chosen witness intervals at each shared endpoint.

## 2. Exhaustive small-case scope

The proposed finite loop contains every nonempty word on the seven
nonempty three-coordinate letters at lengths one through six. Each is
checked in both orientations, for each coordinate and both nontrivial
old ranks s=1,2. It uses only target masks present in the word; it does
not assume that these small words are universal.

`suffix_witnesses` is an exact suffix recurrence. For each union at an
endpoint it keeps the latest possible start, taking a maximum when two
predecessor unions merge. It then fixes the first endpoint at which a
target appears. This supplies a valid single witness per present target.
Keeping only the latest start cannot change the union or prevent a later
valid latest-start update. The asserted maximum of three distinct suffix
unions is correct on three coordinates.

The family endpoint counts, pigeonhole intersection bound, injection,
and final partial-word inequality are all checked independently of any
claim that the enumerated word covers a whole cube.

## 3. Hash-pinned literal statistics and run-start coupling

The actual17 and18 inputs are pinned to their previously verified exact
hashes and lengths24,313 and48,623, and every letter is checked nonempty
and within its dimension. The code computes only marked/unmarked runs,
transition counts and literal-rank statistics. It explicitly inherits
universality from the earlier hash-pinned certificates rather than
pretending to recheck it in this run.

For a fixed coordinate and old rank s, let `W=binom(k-1,s)`, M be the
unmarked-position count, R the total unmarked-run count, and H_s the
number of rank-s run-start letters. Every old rank-s target needs a
different unmarked endpoint. A run start of rank different from s cannot
supply one, proving

    R-H_s <= M-W.

Combining with `R>=R_exit>=2W-N` gives the tested new inequality

    H_s >=3W-N-M.

The run-end version follows by reversal. The earlier inequality

    H_s >=(s+1)W-N-(s-1)M

is separately justified by the same-run marked-cut budget in
[the interleaved run-start audit](EXACT_INTERLEAVED_LIFT_RUN_START_BUDGET_AND_FIXED_TRACE_CUT_CORES_20260909.md),
Sections2–3, which was read for this review. It is not being inferred
by an invalid multiplication of independent capacities.

The implementation's exit/entrance identities correctly subtract a
possible initial or final unmarked run. Negative lower bounds are
harmless in assertions and are clipped only for displayed floors.

## 4. Exact finite arithmetic

The proposed arithmetic assertions agree with the proved formulas:

* `2*binom(16,8)-24313=1427`.
* `2*binom(18,9)-92381=4859`.
* `3*binom(18,9)-92381=53479`, and subtracting48,623 gives4,856.
* `10*binom(18,9)-92381-8*48623=4835`.
* `2*binom(18,9)-1=97239`.
* The latter exceeds the earlier fixed-trace bound
  `48623+48620-9=97234` by five.

These are exact integer identities, not floating-point estimates.
The at-most-one-exit conclusion is restricted to that transition
architecture; it is not a lower bound excluding unrestricted B(19)
attainment. The no-rank-nine-run-start consequences retain their stated
literal-inventory hypothesis.

## 5. Execution and claim boundaries

The script enforces the h100 hostname,30 CPU seconds,45 alarm seconds,
and1 GiB address space. It creates a fresh output directory, has no
retry or construction-modification loop, and writes `FINAL_PASS` only
after all checks complete. A hard limit or assertion failure cannot
produce the final success artifact; earlier per-length messages alone
are not a completed diagnostic certificate.

The small exhaustive enumeration is a diagnostic of a general proved
inequality. It is not a universal-word search. The large-word phase
does not alter either exact literal, optimize anything, or broaden
the claimed coverage verification. No execution is authorized or
performed by this code review itself.
