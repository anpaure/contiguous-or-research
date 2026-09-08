# Exact optimum in dimension 18

The supplied literal word proves

\[
\boxed{\nu(18)=B(18)=48,623.}
\]

This closes the previous three-position gap. Together with the retained
finite certificates, equality is established through dimension 18. The
first unresolved dimension is 19; no all-dimensional equality is asserted.

## Literal certificate

- [Optimal word](answers/k18_optimal48623.word), copied from
  `/Users/amir.nuriyev/Downloads/k18_optimal48623.word`.
- SHA-256: `6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5`.
- Exactly 48,623 nonempty masks in `[1,262143]`.
- All 262,143 nonempty targets have ordinary, nonwrapping interval witnesses.

The [standalone suffix verifier](scripts/verify_k18_optimal48623.py)
enumerates exactly the suffix unions ending at each position, saves one
actual interval for every target, and rechecks every interval with a
separately constructed range-OR segment tree. Its
[report](witnesses/k18_optimal48623/verification.json) records zero missing
targets, all 262,143 successful range queries, and the matching endpoint
lower bound. [All witnesses](witnesses/k18_optimal48623/all_target_witnesses.json.gz)
are retained.

A [separate implementation](scratch/verify_k18_optimal48623_first_occurrence_20260908.py)
enumerates OR-change events from first coordinate occurrences after every
left endpoint. Coordinates with the same first occurrence are added
together, preventing artificial intermediate targets. It checks 607,684
events and independently finds every target, without using the suffix
recurrence or a segment tree. Its
[proof and certificate](scratch/K18_OPTIMAL48623_INDEPENDENT_FIRST_OCCURRENCE_CERTIFICATE_20260908.md)
link the complete second witness collection.

Both deterministic runs executed on `ssh h100` (hostname `arboghast`),
under 30 CPU seconds, 45 wall seconds and 1 GiB limits. The reported
times were approximately 0.29 and 0.55 seconds. The separately reported
296-million-interval scan was not rerun here; it is unnecessary for these
two exhaustive checks.

## Matching lower bound

Set `W=binom(18,9)=48620` and
`Lambda=sum_(j=1)^8 binom(18,j)=106761`. Choose one interval witness for
each nine-set. Distinct witnesses have distinct left and right endpoints,
and neither can contain another. After ordering them by left endpoints,
their right endpoints increase as well. Thus a word of length `N=W+t`
has its i-th chosen interval contained in `[i,i+t]`.

Every `(t+1)`-position window consequently contains a nine-set witness.
Any smaller target must have an interval of length at most `t`, and
there are only `tW+t(t+1)/2` such intervals. At `t<=2`, this is at most
`97243<106761`. Lengths below W are already excluded by the distinct
endpoint count. Therefore every universal word has length at least
`W+3=48623`, attained by the checked literal.

The [independent lower-bound and extension audit](scratch/INITIALIZED_RECENCY_EXTENSION_INTERLEAVING_AND_K18_LOWER_BOUND_AUDIT_20260908.md)
includes the boundary cases and a complete proof. This finite equality
requires no PBBS construction, period, concentration or asymptotic premise.

## General lifting result

For a recency state P, let `lambda_k(P)` be the minimum number of nonempty
updates whose states, including the initial P, cover every nonempty
base target as a prefix. Each state contributes at most one target of a
fixed middle rank, so `lambda_k(P)>=W(k)-1`.

For a universal word A ending at P, the minimum all-marked appended
extension is exactly

\[
\operatorname{Ext}_z(A)=1+\lambda_k(P).
\]

An attaining initialized traversal gives the extension by appending `{z}`
and its marked updates. Conversely, stripping z from any successful
extension and deleting empty projected updates gives an initialized
cover; at least one deleted update was required to realize `{z}`.
The linked audit proves both directions with ordinary interval witnesses.

The [independent structural reconstruction](scratch/K18_OPTIMAL_INITIALIZED_TWO_CYCLE_STRUCTURE_AND_BYTE_REGENERATION_20260908.md)
also passes. The actual word is `A' || {z} || marked(C)`, where A'
adjusts the optimal17 word's final mask from 689 to 8881. The last pair
keeps union25265 and the old singleton689 remains at index87, so A'
is still universal. Its terminal block sizes are `(6,1,1,1,1,1,1,1,1,1,1,1)`.

Recover `Q=A[:85]` and `R=A[86:-2]` from the old17 literal. The supplied
coordinate permutation maps a periodic state of `reverse(R)` to that
terminal state. Starting at zero-based phase1428 of `reverse(R)`, take
24,224 updates, omitting phase1427, and then append `reverse(Q)`.
This gives exactly24,309 initialized updates. The initial state accounts
for the omitted long-cycle endpoint.

Independent scans verify130748cyclic long targets and633linear short
targets. Their union misses exactly the seven reported targets, all
supplied by the specified join. Directly checking every initialized state
then proves full131071-target coverage, with all24310rank-eight and
all24310rank-nine prefixes occurring exactly once. Hence

\[
\boxed{\lambda_{17}(P_{A'})=24,309=W(17)-1.}
\]

All131071marked target witnesses were separately replayed against the
actual18 word. A full-word pass also verifies that every nine-set occurs
at exactly one endpoint; only the first three endpoints lack one.
Regenerating from A, the recovered cycles and the given permutation gives
the supplied18 file byte for byte. The
[complete structure certificate](scratch/k18_optimal_initialized_structure_20260908/optimal18_initialized_structure_certificate.json)
and regenerated body are retained. This third bounded h100run took1.221
seconds under30CPU/45wall/1GiB limits.

This regeneration uses the supplied17 literal. It does not claim to
replay the unprovided compact quotient generator or identify its canonical
long-cycle phase. The literal optimum and initialized lifting mechanism
are both verified without that provenance.

## The next finite frontier

| k | Lower bound | Verified upper bound | Remaining gap |
|---:|---:|---:|---:|
|18|48,623|48,623|0|
|19|92,381|94,161|1,780|
|20|184,759|188,322|3,563|

The [finite comparison](FINITE_BOUNDS_K18_K19_K20_20260908.md) identifies
the actual words for the remaining upper bounds. The gaps are between
proved bounds, not claimed excesses of the true minimum.

An exact19 word must have at least 541 present-to-absent transitions and
541 absent-to-present transitions for every coordinate. This reconfirms
the earlier [entrance/exit capacity result](scratch/EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md),
which already obtained 541 using the lower bound B(18). A single-switch
lift costs at least 97,243 positions and cannot attain B(19)=92,381.
These are architecture constraints, not a proof that B(19) is unattainable.
