# Claimed optimal21/22 literals: independent forward review plan

Date: 2026-09-09. Original pre-execution review plan. The single reviewed
run subsequently passed; see the
[independent optimality certificate](K21_K22_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md).
The remainder preserves its approved fixed scope.

The actual raw files are now present. Their locally checked byte hashes are:

| k | Expected length | Supplied local file | SHA-256 |
|---:|---:|---|---|
| 21 | 352,719 | `/Users/amir.nuriyev/Downloads/k21_optimal352719.word` | `eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2` |
| 22 | 705,435 | `/Users/amir.nuriyev/Downloads/k22_optimal705435.word` | `a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd` |

File names do not establish optimality. The proposed checker is
[verify_k21_k22_optimal_forward_first_occurrence_20260909.py](verify_k21_k22_optimal_forward_first_occurrence_20260909.py).
It retains the previously reviewed forward first-occurrence enumeration
and exact all-rank lower-bound arithmetic. Changes are limited to the
fixed lengths, input hashes and paths, output names, and the final success
condition: both supplied words must cover their complete cubes AND attain
their independently computed maximum endpoint lower bounds.

For each ordinary start, first appearances of coordinates are sorted by
endpoint. Coordinates sharing that endpoint are added simultaneously.
The resulting ORs are exactly the distinct ORs at that start. The checker
explicitly checks every target, its saved ordinary witness bounds, and
every binomial rank census. No cyclic wrap or suffix recurrence is used.

For every rank, the checker derives the least integer auxiliary parameter
using an integer-square-root seed and upward correction. It checks the
defining inequality at that integer and failure at its predecessor, then
takes the maximum resulting lower bound. Neither proposed optimal length
is supplied as a lower-bound premise.

The run saves both raw files, the source, complete per-word and paired
reports, and all four target-indexed signed-int32 start/end witness arrays.
Whole-run status `PASS_OPTIMAL_FULL_CUBES` requires coverage and lower-bound
equality for both words. An interrupted or incomplete run is not PASS.

Before any mathematical execution, root and an independent agent must
read the complete source. The proposed scope is exactly one paired h100
run on hostname `arboghast`, with hard limits 60 CPU seconds, 90 wall
seconds, 2 GiB address space and 256 MiB per file, plus external
`timeout 90s`. The output directory is fresh; no retry or alternate input
is authorized by this preparation.

The prepared 352,862/705,724 upper-pair forward checker remains preserved
and unexecuted. Root's independent suffix/range checks and cyclic-opening
or periodic-lift reconstruction, if run, are separate evidence. This
forward task does not certify those mechanisms or an all-k exact theorem.
