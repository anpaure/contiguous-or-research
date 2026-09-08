# Historical verified upper bounds at21 and22

**Historical pair, now superseded by equality:** the newest supplied words
prove `nu(21)=352719` and `nu(22)=705435`, with zero gaps. See the
[current exact record](K21_K22_OPTIMAL_AND_CYCLIC21_VERIFIED_20260909.md).
The earlier literals, skeleton and fixed Hall obstruction below remain
valid and are retained with their original provenance.

Date: 2026-09-09. Independent verification of the user's supplied words gives

    352719 <= nu(21) <= 353297,
    705435 <= nu(22) <= 706594.

The gaps are578 and1159. Equality remains established through20. The later
357442-letter21 report and its714884 lift are weaker and do not replace
these incumbents; that additional literal was not attached here.

## Complete literal verification

|k|Length|Targets covered|Missing|Separate range-OR rechecks|
|---:|---:|---:|---:|---:|
|21|353297|2097151|0|2097151|
|22|706594|4194303|0|4194303|

- [21 word](answers/k21_upper353297.word), SHA256
  `0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7`.
- [22 word](answers/k22_upper706594.word), SHA256
  `84e7448934c539fcc6c3453ffdb988cef219c263974ba49d876354fd24878b45`.

The forward checker groups coordinates by their first subsequent occurrence
at every ordinary start, with no witness-length cutoff. A separately
authored checker enumerates complete suffix families. A third algorithm,
a segment tree built from the literal word, rechecks every saved witness.

|k|Forward events|Suffix events|Maximum saved suffix-witness length|
|---:|---:|---:|---:|
|21|4943869|4943248|24|
|22|10241093|9886544|24|

Every rank count is exact; all letters are nonzero masks in the stated
cube, and all witnesses are nonwrapping. The maximum length24 is an
observed result of complete enumeration, not an imposed cutoff.

[Forward source](scratch/verify_k21_k22_upper_forward_first_occurrence_20260909.py)
and [report](scratch/k21_k22_upper_forward_20260909/k21_k22_forward_complete_certificate.json)
are independent of the
[suffix/range/lift source](scripts/verify_k21_k22_upper_suffix_and_lift.py)
and [report](witnesses/k21_k22_upper/complete_suffix_range_lift_certificate.json).
Every witness is retained beside those reports.

Both sources were fully reviewed before their single h100/arboghast runs.
Forward verification took7.787 seconds with60CPU/90wall/2GiB limits;
suffix/range/lift verification took13.164 seconds with120CPU/150wall/3GiB
limits. Both terminated successfully. No search or unavailable generator
replay ran. Internal review is not external or formal certification.

## Analytic lower bounds and the literal22 lift

The endpoint theorem gives Lambda_s<=t M_s+t(t+1)/2 for a universal word
of length M_s+t, where M_s=binom(k,s) and Lambda_s counts smaller nonempty
targets. Both checkers independently compute minimal t at every rank and
maximize the bound. Rank11 maximizes it in both dimensions:

|k|M_11|Lambda_11|Capacity at t=2|Lower bound|
|---:|---:|---:|---:|---:|
|21|352716|1048575|705435|352719|
|22|705432|1744435|1410867|705435|

For any universal word A of lengthN and new coordinatez, the ordinary lift
is `A, {z}, (A_i union {z}) for i=0,...,N-2`, of length2N. An old target
persists. A marked target whose old witness ends before the last position
uses the marked copy; one ending at the last position uses that old suffix
followed by{z}. The bridge supplies the singleton{z}.

At z=2097152 this lift regenerates the supplied22 file byte for byte.
Its own complete coverage checks also pass. The extra three positions in
the22 gap beyond twice the21 gap come from doubling a three-position
endpoint excess while B(22)-W(22) remains three.

These finite bounds use no PBBS support, concentration or asymptotic premise.

## The submitted general laws and their scope

[Independent theorem audit](scratch/SHORT_CELL_WEIGHTED_ORBIT_HALL_AND_PARITY_EXCESS_INDEPENDENT_AUDIT_20260909.md)
passes the exact individual-cell deficit-core criterion, weighted orbit
Hall deficiency for arbitrary finite side-preserving groups, and the
odd/even endpoint-excess law with its exact slack criterion. The first two
mechanisms already have proofs in the repository; the audit gives their
attribution. A quotient flow computes the physical matching NUMBER, not
an equivariant assignment or a common cap for overlapping cells.

The numerical462 deficiency now passes a separate complete graph and
primal/dual certificate check, reconstructed directly from the supplied
literal. The [fixed-graph proof and artifacts](scratch/K21_FIXED_THREE_CYCLE_PHYSICAL_CANDIDATE_HALL_DEFICIENCY_462_VERIFIED_20260909.md)
record1,997,177 orbit edges, maximum physical candidate matching695,397
against695,859 targets, and an explicit31,185-target Hall family whose
COMPLETE neighborhood contains only30,723 cells. All2,011,584 local
candidate masks were checked against the actual protected triples and
regenerated for the neighborhood replay. The saved feasible flow and
Hall deficit agree, independently of the flow solver's optimality report.

One reviewed h100 build and one fixed-graph run completed; the latter
took2.879 seconds under120CPU/150wall/2GiB bounds. No alternate skeleton,
word search or cap reassignment ran. The result concerns the cyclic bank's
individual-cell candidate graph. It neither constructs simultaneous caps
nor gives a lower bound of B(21)+462 for unrestricted words or repairs.

The [separate literal structure audit](scratch/K21_SUPPLIED_THREE_CYCLE_CARRIER_LOWER_HOLES_AND_572_REPAIR_CERTIFICATE_20260909.md)
also passed one reviewed h100 run. It reconstructs the three actual
periods352548,105,63, all canonical middle owners and envelope identities,
and verifies the569 cyclic holes:172 of rank7,302 of rank8,95 of rank9.
Opening adds ten higher holes. The actual572-letter tail repairs all579
ordinary holes, with every repair witness independently range-rechecked.
The carrier, envelopes and deficit pins are rotation-equivariant; the
actual literal caps are not (6520 one-step failures). This does not claim
to replay the unavailable original generator, search or repair forest.

[The capacity audit](scratch/WINDOW_RANK_DEFICIT_CAPACITY_AND_NEAR_DEADLINE_PROTECTION_AUDIT_20260909.md)
also passes the general window-rank deficit inequality. At each start,
the longer interval unions form a nested chain; hence at most one target
can occur at each remaining rank. For the explicit protected-window rank
floor in the flat ladder, the resulting slack bound gives

    q >= d(k)+1-(3k/2)^(1/3)(1+o(1)),    q/d(k) -> 1.

At the last odd dimensions before a padding increase, the protection gap
is O(k^(1/6)). These claims concern the protected native window length.
The shorter-window rank floor must be an explicit hypothesis; it does
not follow just from the middle-window rank. The reported finite table
is not a premise and was not independently checked in this audit.

At21 the arbitrary-word inequality is

    sum_i (9-|A_i union A_(i+1)|)_+ >= 401929-N.

Thus49210 is the requirement for hypothetical exactN=352719, not for
either longer reported construction. These necessary laws do not exclude
an arbitrary optimal word outside the flat protected-window hypothesis.

## Current boundary

The historical353297/706594 words are retained. Their literal coverage,
three-cycle carrier, actual repair tail and fixed462 Hall obstruction have
now all been checked, with their separate scopes and provenance above.
The all-dimensional exact goal remains ACTIVE. The disjoint canonical
path bank and subsequent gluing constraints remain in
[the construction-progress record](EXACT_PHI_INDUCTION_AND_UPPER_SUPPORT_GATE_20260909.md).
No necessary condition or finite approximation substitutes for an all-k
proof of nu(k)=B(k).
