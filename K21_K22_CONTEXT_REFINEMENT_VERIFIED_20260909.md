# Verified improved upper bounds at21 and22

**Historical result, superseded by exact equality:** the subsequently
supplied optimal words prove `nu(21)=352719` and `nu(22)=705435`, with
zero gaps. See the [current exact record](K21_K22_OPTIMAL_AND_CYCLIC21_VERIFIED_20260909.md).
The checks and inequalities below retain their original historical scope.

Date: 2026-09-09. The supplied raw words independently establish

|Dimension|Endpoint lower bound|Verified upper bound|Gap|
|---:|---:|---:|---:|
|21|352719|353094|375|
|22|705435|706188|753|

These improve the earlier353297/706594 certificates by203/406 positions.
Equality remains established through20. The separate357442/714884 report
is weaker than both pairs and never replaces the better certificates.

## Complete literal checks

|k|Nonempty targets covered|Missing|Forward events|Suffix events|Separate range-OR witness rechecks|
|---:|---:|---:|---:|---:|---:|
|21|2097151|0|4943081|4943001|2097151|
|22|4194303|0|10239314|9886049|4194303|

The independently written forward algorithm enumerates changes at each
coordinate's first occurrence after every start. The suffix algorithm
enumerates every distinct suffix union at every endpoint. Neither uses
a witness-length cutoff. A segment tree built from the raw letters
separately checks a saved ordinary interval for every target. The largest
saved suffix witness has length24 in both cases, an observed statistic.
All per-rank counts match the binomial coefficients; every letter is a
nonzero mask in the stated cube. Both programs recompute the endpoint
lower bound over every rank, rather than assuming the claimed gaps.

The complete words are:

- [21-coordinate word](answers/k21_upper353094.word), SHA256
  `f404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392`.
- [22-coordinate word](answers/k22_upper706188.word), SHA256
  `aef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59`.

The [forward proof and full witnesses](scratch/K21_K22_CONTEXT_REFINEMENT_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md)
and [suffix/range/lift report](witnesses/k21_k22_context_refinement/complete_suffix_range_lift_certificate.json)
retain both standalone sources, actual reports and all target witnesses.
The [source review](scratch/K21_K22_CONTEXT_REFINEMENT_LITERAL_CHECKER_PREEXECUTION_REVIEW_20260909.md)
was completed before execution. The algorithms were retained from the
previous independently authored checks, with new fixed input pins and
separate output directories.

Exactly one paired forward run took7.690 seconds under60CPU/90wall/2GiB
bounds. Exactly one paired suffix/range/lift run took13.291 seconds under
120CPU/150wall/3GiB bounds. Both ran only on h100/arboghast and exited0.
The copied files and principal artifact hashes were checked. No optimizer,
alternative word search, or local mathematical execution occurred.

## The exact22 lift and matching lower bounds

For a complete21 word A and z=2097152, the sequence

    A, {z}, (A_i union {z}) for i=0,...,|A|-2

is a complete22 word of length2|A|. A marked target whose old witness ends
at the last position uses that old suffix followed by{z}; every other
marked target uses its copy. Unmarked targets remain in A. The supplied22
file is byte-identical to this literal lift, and also passes its own
complete coverage checks above.

Rank11 attains the endpoint lower bound in both dimensions. Its widths
are352716/705432 and lower-target counts1048575/1744435. The two-position
capacities705435/1410867 are too small, so three extra positions are
necessary. This yields352719/705435, also the maximum of all rank bounds.
No PBBS support or asymptotic premise is needed for these finite results.

## The submitted overlapping-refinement laws

The [pure proof audit](scratch/ORDERED_OVERLAPPING_REFINEMENT_AND_SIMULTANEOUS_CONTEXT_CERTIFICATES_AUDIT_20260909.md)
passes the general preservation theorem. If each old letter is the union
of a new interval, these intervals have nondecreasing left/right endpoints
and no consecutive gap, then every old interval union is preserved. A
replacement inside a larger word additionally covers both new boundaries.

The nonempty adjacent-pair factorization criterion is the existing
depth-one maximal flat compiler: neighboring old letters must intersect,
and each interior letter must be contained in the union of its neighbors.
The audit retains that attribution.

The simultaneous theorem also passes with its stated guards: replacement
blocks are disjoint in the original word, insertion gaps are distinct,
and neither neighbor of an insertion belongs to a replacement block.
Each operation preserves every interval union in arbitrary exterior
context, and these edits commute. Putting each focal repair first proves
that all its certified targets survive in the same final word. Overlapping
certificate contexts are permitted; conflicting edits of one old position
are not covered by the theorem.

The old462 deficiency remains an exact obstruction to the OLD cyclic
single/pair candidate graph. Refining an old letter into an overlapping
interval changes that graph, so it does not impose a462-position repair
cost. The new literal upper bound and the old obstruction are consistent.

The endpoint budget still matters for an exact construction. Any transported
rank-s witness must have length at most N-binom(k,s)+1. At hypothetical
exact21, every rank11 witness has length at mostfour. An inflation that
leaves a five-position rank11 interval cannot itself yield that exact
length, even if a different shorter witness exists for the same target.

## Provenance and limits

Only the two final raw words and the user's written theorem description
were provided for this continuation. The202-operation schedule,644 accepted
edit trace, claimed402-target local recovery, and original generator were
not independently replayed. The general theorem audit and raw-word checks
do not silently certify those unavailable intermediate artifacts.

The all-dimensional equality goal remains open. These are complete finite
upper certificates with gaps375/753, not optimality certificates, a new
asymptotic result, or a proof of equality beyond20. Internal source and
proof reviews are not external or formal certification.
