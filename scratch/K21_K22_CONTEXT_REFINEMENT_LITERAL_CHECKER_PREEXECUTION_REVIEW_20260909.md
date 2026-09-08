# Independent pre-execution review of the refined21/22 literal checkers

Date: 2026-09-09. Reviewer: exact_b_induction. Verdict: full-source PASS
for both files. No mathematical execution or build by this reviewer.

Reviewed completely:

- `scripts/verify_k21_k22_context_refinement_suffix_and_lift.py`;
- `scratch/verify_k21_k22_context_refinement_forward_first_occurrence_20260909.py`.

The fixed inputs are lengths353094 and706188, with raw SHA-256 values
`f404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392`
and `aef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59`.
Both source files use these exact pins and the corresponding paths.

The root checker enumerates every distinct ordinary suffix union, keeping
a valid latest-start witness under deduplication. It verifies every target
again by an independently built range-OR tree, checks the endpoint lower
bound over every rank, and compares the ordinary doubled22 lift by both
mask sequence and exact bytes. The extra23/24 calculation from the older
source was removed. Its limits remain120 CPU seconds,150 wall seconds,
3GiB address space and512MiB per file.

The frontier checker independently enumerates all ordinary starts through
grouped first-coordinate arrivals. Adding every coordinate with the same
arrival position simultaneously avoids nonexistent partial-letter unions.
It checks every target and all target-rank counts, exports ordinary
witness endpoints, and independently computes each rank's minimal endpoint
slack. Its limits remain60 CPU seconds,90 wall seconds,2GiB address space
and256MiB per file.

Both report upper bounds without assuming equality to B. Neither claims
to replay the user's context optimization, a context schedule, or a Hall
certificate. These are source-review findings only; actual run outcomes
and coverage counts must come from the executing agents' certificates.

