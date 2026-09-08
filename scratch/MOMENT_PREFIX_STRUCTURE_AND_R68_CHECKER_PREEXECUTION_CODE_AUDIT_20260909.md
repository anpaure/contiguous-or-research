# Pre-execution audit: exact height structure and one r68 frontier

Date: 2026-09-09. Independent full-source review by
`exact_equality_structure` of
[verify_moment_prefix_structure_and_r68_20260909.py](verify_moment_prefix_structure_and_r68_20260909.py).

**PASS for the reviewed implementation.** No correctness-blocking defect
was found. This is a code audit only: the reviewer did not import, run,
compile, or otherwise execute the checker. No output counts or successful
threshold calculation are certified by this document.

The mathematical comparison is the
[integrated-period/sparse-reserve proof audit](MOMENT_PREFIX_INTEGRATED_PERIOD_SPARSE_RESERVE_AND_THRESHOLD_INDEPENDENT_AUDIT_20260909.md)
and the earlier
[forward-prefix audit](PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md).
The present program uses full children and exact row moments, so it does
not need the sparse-reserve or coarse nonprimitive-count branches.

## 1. Inputs, scope, and structural checks

The program accepts only the prescribed `arboghast` host, creates a fresh
output directory with `exist_ok=False`, and pins the retained exact
rotation-period census to SHA-256

`43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2`.

The local retained reference was read far enough to confirm that its
`rows`, `r`, `catalan`, `overhead`, cycle count, height-histogram and
period-histogram keys match the checker. A changed or incorrectly copied
remote reference fails the pinned hash before use.

The height table through semilength100 is built by the triangular exact
integer recurrence, with exact binomial-ratio divisions, mass identities,
and `K<=H<=(b+1)K` checks. Direct Dyck enumeration through10 checks every
pruning class and height total. Direct bridge enumeration through9 checks
both reflection formulas and the rooted rotation fibres. Geometric-tail
and conditional-height inequalities use exact `Fraction` arithmetic.

Ordered weak-composition rows are directly enumerated at the stated small
sizes and their least periods are compared with divisor inversion.
The small complete-prefix calculation compares its exact period/height
cycle histograms to the pinned existing census. This is a comparison to
that prior physical census, not a new independent physical PBBS traversal.
The implementation and report correctly retain the finite inverse-fibre
theorem as an inherited premise.

## 2. Complete symmetry accounting and exact period arithmetic

`classes(p,ell)` counts rows whose period divides each divisor `d`, then
subtracts the already counted proper-divisor classes. It asserts
nonnegative class counts and the full weak-composition sum. Its checks
for `p=1` and `ell=0` correctly retain exactly one period-one row.

`row_moments(a,b)` includes every allowed `c` and every nonzero
least-period class. It verifies both identities

    sum_d M_d=K(a,b),       sum_d R_d=H(a,b)-K(a,b).

For reduced `beta'=num/den`, the denominator after division by `d` is
`den*d/gcd(num,d)`, exactly as used by `period_after`. `beta_update`
reduces every fraction, and all initial and subsequent divisors are
multiples of the original circumference.

The integrated charge sums the complete correlated weights
`w[(2s+1)M_d+2R_d]/P_d`; it does not replace symmetric periods by the
primitive period. Small-prefix checks separately verify the
primitive-baseline-plus-correction identity and its nonnegative sign.

## 3. Terminal branch and rounding

Both producer `derive` and consumer `replay_derive` explicitly treat
`b=0`. They insert the last one-slot-row denominator before charging
the completed class. No `K(0,c)` expression or empty nonterminal
expansion is used. The original height is then exactly `s+1`.

All ordinary charges are upper charges. Rational moment and integrated
sums are rounded upward once by exact numerator/denominator arithmetic.
The check `integrated_ceil<=moment_ceil<=old_ceil` is valid by monotonicity
of the ceiling function. The program does not assume that the sum of
rounded child charges must decrease: it updates the sum exactly and
records any increases.

There is no predecessor lower-bound calculation in this checker.
Accordingly it cannot accidentally use these upper ceilings to certify
failure at `r=67`.

## 4. Frontier and priority-free replay

The attempted target is hard-coded to `r=68`, `n=137`, denominator
`D=100000`. Initial nodes are exactly the disjoint classes
`(s,a,b,w,P,beta)=(0,68,b,1,137,0)` for `0<=b<68`.

Each split generates every permitted next size and every nonzero ordered
row-period class. The child mass is checked against the parent mass
before the parent is removed. No sparse tail, omitted symmetry class,
or uncharged reserve is present. Final active masses and charges are
freshly summed and written as complete leaf rows.

The replay uses a dictionary of active prefixes, not the priority heap.
It independently computes beta updates with `Fraction`, recomputes row
divisor inversion, and directly sums the `c,d` height weights rather
than calling producer `row_moments` or `derive`. It removes each split
parent exactly once, regenerates every child with deterministic new IDs,
and compares every recorded event mass and charge. It then consumes
every final active leaf exactly once and requires no active row remain.
This checks the actual partition, not merely a final mass total.

The replay intentionally shares the statically generated and separately
checked exact `K,H` table. Its independent scope is the transcript,
period updates, row-class enumeration and charge reconstruction; it is
not a second unrelated derivation of the all-dimensional fibre theorem.

## 5. Normalization and success statuses

The final integer upper sum `U` bounds the root-weight sum. The collar
is at most `n*U`, width is `n*Cat_r`, and the reported length bound is
`n*(Cat_r+U)`. Thus the exact success test is correctly

    100000*U < Cat_68.

The signed margin is `Cat_68-100000*U`. Decimal enclosures are merely
outward displays and are not used in the comparison.

All soft-stop conditions are checked separately from the inequality.
A target success is emitted in the final certificate only after the
completed replay. If a refinement/node/time soft cap is reached without
the strict inequality, the report instead says
`STRUCTURAL_PASS_VALID_SINGLE_FRONTIER_BOUND` and has
`target_certified=False`, with the stop reason and signed margin.
That outcome is not a successful r68 tolerance certificate.

The pre-replay summary and `R68_STOP` line are explicitly intermediate
artifacts. They must not be represented as completion of the independent
replay. The authoritative completed result is the final certificate,
which is written only after `replay_frontier` returns successfully.

## 6. Resource and claim limits

Hard limits are 60 CPU seconds, 90 alarm seconds, 1 GiB address space,
and 512 MiB per output file. Soft build limits reserve time for replay:
30 CPU seconds and40 wall seconds, measured from the start of the entire
job. At most10,000 refinements and1,000,000 generated nodes are allowed.
Child preparation for an individual split is completed before mutation,
and the cumulative generated-node cap is checked beforehand.

If a hard CPU/alarm/file limit or assertion interrupts the process, it
cannot reach the final success write. Such termination may leave partial
artifacts and must be reported as incomplete, regardless of earlier
progress lines. `MemoryError` additionally writes an explicit
`INCONCLUSIVE_MEMORY_LIMIT` marker before re-raising. The checker has
no retry loop.

Even a successful final r68 certificate establishes only the single
odd137 constructor bound and its standard even138 lift, alongside the
stated structural checks. It does not verify the3,356-case band, the
predecessor135/136 failure, the new uniform starting point137, or the
all-dimension exact objective. The final report's explicit scope agrees
with these limits.
