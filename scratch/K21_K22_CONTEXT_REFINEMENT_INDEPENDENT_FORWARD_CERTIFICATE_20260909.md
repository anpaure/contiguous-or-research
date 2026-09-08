# Independent forward certificate for the improved 21/22 literals

Date: 2026-09-09. One approved, fixed-input h100 execution returned
`PASS_FULL_CUBES`. These are verified upper bounds, not optimality results.

| Dimension | Literal length | Distinct nonempty targets | Missing | Exact all-rank endpoint bound | Gap |
|---|---:|---:|---:|---:|---:|
|21|353,094|2,097,151|0|352,719|375|
|22|706,188|4,194,303|0|705,435|753|

Thus the new supplied files independently establish

    352719 <= nu(21) <= 353094,
    705435 <= nu(22) <= 706188.

## Input identity and exact checks

The raw Downloads files were hashed locally as file bookkeeping and
uploaded unchanged. The checker enforced both hashes before any census:

* `k21_upper353094.word`: 2,528,371 bytes, SHA256
  `f404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392`.
* `k22_upper706188.word`: 5,353,123 bytes, SHA256
  `aef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59`.

For every ordinary start, the standalone checker sorted the first
occurrence positions of all coordinates. All bits first appearing at
the same position were added together. These events are exactly all
changing forward interval ORs for that start, without fictitious partial
letters. Every nonempty target was then checked through a target-indexed
witness array. There were 4,943,081 events at k=21 and 10,239,314 at k=22.
All per-rank counts equal the full binomial coefficients, and all letters
are nonempty masks inside the stated cube.

No suffix recurrence, segment tree, cyclic scan, cutoff, search, or previous
verifier import was used. The algorithm is unchanged from the earlier
reviewed forward checker; only the input lengths, hashes, paths, output
names and explicit scope description changed.

For every rank s, the checker recomputed the smallest t>=0 with

    t*binom(k,s)+t(t+1)/2 >= sum_(j=1)^(s-1)binom(k,j),

verified failure at t-1 when t>0, and maximized binom(k,s)+t over ALL
ranks. The unique maximizing rank is 11 in both dimensions, with t=3.
The gaps 375 and 753 are derived from these exact lower bounds and the
checked literal lengths; neither gap was an input assertion.

This run does not reconstruct an optimization procedure, a context
schedule, a compact constructor, or a modification to any prior Hall
instance. No such omitted artifact is a premise of literal coverage.

## Source review, execution and artifacts

Root and induction independently read the entire derivative source before
root authorized exactly one paired run. These are internal reviews, not
an external formal verification claim.

Source:
[verify_k21_k22_context_refinement_forward_first_occurrence_20260909.py](verify_k21_k22_context_refinement_forward_first_occurrence_20260909.py),
SHA256 `13908957a5df1afed72a1af1283eefd15b242252251f9cc04aabde88691acba1`.

The source enforces h100/arboghast, CPU 60 seconds, wall 90 seconds,
address space 2 GiB and individual file size 256 MiB. The command also
used external `timeout 90s`. It exited with code 0 after 7.686822965 CPU
seconds and 7.690287143923342 wall seconds. No retry, changed input or
additional mathematical run occurred.

Full copied bundle:
[k21_k22_context_refinement_forward_20260909/](k21_k22_context_refinement_forward_20260909/).
The principal report is
[k21_k22_context_refinement_forward_complete_certificate.json](k21_k22_context_refinement_forward_20260909/k21_k22_context_refinement_forward_complete_certificate.json).

The bundle includes both raw input copies, the exact executed source,
individual and combined reports, complete log, exact command/provenance,
and all four witness arrays. Arrays are target-indexed signed little-endian
int32; index 0 is unused. A mask T uses the zero-based inclusive ordinary
interval [start[T],end[T]]. Each k=21 array has 2,097,152 entries; each
k=22 array has 4,194,304 entries. All file hashes are retained.

Remote directory:
`/home/amodo/exact-b-k21-k22-context-refinement-forward-20260909/`.

The earlier 353,297/706,594 certificates remain valid historical upper
bounds. These new literals improve the verified finite bounds without
settling either dimension exactly.
