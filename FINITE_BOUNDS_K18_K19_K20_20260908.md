# Exact finite answers in dimensions 18, 19 and 20

All three dimensions are now exact: verified literal words attain the
endpoint lower bound. These are finite answers, independent of an eventual
asymptotic estimate. Exact attainment is established through dimension 20;
the next unresolved dimension is 21. Updated 2026-09-09.

| Dimension | Endpoint lower bound B(k) | Constructed upper bound | Gap | Upper bound above B(k) |
| ---: | ---: | ---: | ---: | ---: |
| 18 | 48,623 | 48,623 | 0 | 0% — exact |
| 19 | 92,381 | 92,381 | 0 | 0% — exact |
| 20 | 184,759 | 184,759 | 0 | 0% — exact |

The earlier 94,161- and 188,322-letter constructions remain documented below
as historical upper bounds; they are no longer the current answers.

## Lower bounds

With s=ceil(k/2), write W=binom(k,s) and
Lambda=sum_{j=1}^{s-1} binom(k,j). The exact endpoint-count bound is
B(k)=W+d, where d is the least nonnegative integer for which
d W+d(d+1)/2 >= Lambda.

| k | W | Lambda | d |
| ---: | ---: | ---: | ---: |
| 18 | 48,620 | 106,761 | 3 |
| 19 | 92,378 | 262,143 | 3 |
| 20 | 184,756 | 431,909 | 3 |

These integer calculations were executed on h100. Independent maximization
of the endpoint bound over all target ranks gives the same lower bounds.
The new 19/20 forward verifier records every rank and both inequalities
certifying the minimal delay at that rank.

## Matching literal constructions

At dimension 18, the supplied [optimal word](answers/k18_optimal48623.word)
has exactly 48,623 nonempty letters. Complete suffix-union enumeration,
all 262,143 separate range-OR witness queries, and an independent
607,684-event first-occurrence scan establish full ordinary coverage.
The lower bound above matches, proving nu(18)=48623. Its SHA-256 is
`6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5`.
The [optimality record](K18_OPTIMAL48623_VERIFIED_20260908.md) contains
the standalone verifiers, proof and full witness collections.

At dimension 19, the supplied
[92,381-letter word](answers/k19_optimal92381.word) covers all 524,287
nonempty targets. An independent forward first-occurrence enumeration
checked 1,200,848 change events, every target and every rank count. Its
length equals the independently computed all-rank endpoint bound, proving
nu(19)=92381. Its raw SHA-256 is
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.

At dimension 20, the supplied
[184,759-letter word](answers/k20_optimal184759.word) covers all 1,048,575
nonempty targets. The same standalone method checked 2,494,149 change
events and independently obtained B(20)=184759. Its raw SHA-256 is
`047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02`.

Both checks passed in one bounded h100 run. Every letter is nonzero and
every saved witness is an ordinary, nonwrapping interval. The completed
[forward proof and certificate](scratch/K19_K20_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md)
links the standalone source, both unchanged word files and all target
witness arrays. The
[full machine report](scratch/k19_k20_optimal_forward_20260909/k19_k20_forward_complete_certificate.json)
records the complete rank counts and lower-bound calculations. See also
the [consolidated 19/20 record](K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md).
The forward verification alone suffices for the two ordinary optimality
claims; no structural regeneration is a premise of those claims.

A second complete suffix enumeration and independent segment-tree check
of every saved witness also passed for both dimensions. Its
[report](witnesses/k19_k20_optimal/complete_suffix_range_cyclic_lift_certificate.json)
additionally proves mu(19)=92,378 and verifies that the20 word is the
byte-identical periodic-core lift of the19 word.

## Historical height-adaptive and doubled upper bounds

Before exact 19 was supplied, one fixed canonical height-adaptive construction had
360 owner cycles, 92,378 owner positions, and total cycle height 1,384.
The untrimmed theorem word has length
92,378+2(1,384)-360=94,786 and covers the entire cube.

Keeping h copied prefix letters per cycle instead gives 93,762 letters.
Complete interval-OR enumeration finds 399 missing targets: 180 at rank
11, 164 at rank 12, 54 at rank 13, and one at rank 14. Appending those
399 masks as individual letters gives a 94,161-letter universal word.
Every one of its 524,287 nonempty targets has an ordinary nonwrapping
witness, independently rechecked by a segment-tree range-OR calculation.
No cut, cycle-order, or local-rewrite search was used.

That historical word is [k19_upper94161.word](answers/k19_upper94161.word), with SHA-256
`1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224`.
The [construction certificate](scratch/k19_height_adaptive_20260908/height_adaptive_fixed_certificate.json)
records all three word lengths, coverage counts and hashes.

The exact one-coordinate lift in MASTER_HANDOFF.md, equation (3.44), sends
a universal word A_1,...,A_N to

    A_1,...,A_N,{z},A_1 union {z},...,A_(N-1) union {z}.

This has exactly 2N nonempty letters. Old targets persist; targets with z
use the second copy when an old witness ends before N, or the old suffix
followed by the singleton bridge otherwise. The bridge realizes {z}.
The optimal 24,313-letter word in dimension 17 initially gave
48,626 at dimension 18. That literal lift independently passed all
262,143 targets and every range-OR witness query; see
[its complete verification](scratch/K18_VERIFIED_48626_TRIMMED_LIFT_FROM_OPTIMAL_K17_20260908.md)
and [that historical word](answers/k18_upper48626.word). Its SHA-256 is
`52a68ff6bb2757c00b4be03edbb53eaf821d5dca0985d0a680941502d0c2315b`.
The 48,626- and 49,316-letter words remain historical. The 94,161-letter
word also gave the historical 188,322-letter dimension 20 construction.

Those even-dimensional upper words were materialized and checked on
every target, with independent segment-tree verification of all witnesses.
The current [dimension-18 report](witnesses/k18_optimal48623/verification.json)
supersedes the earlier 48,626-, 49,316- and 49,336-letter lifts; the
[historical dimension-20 report](scratch/k20_height_adaptive_20260908/k20_upper188322_verification.json)
and [188,322-letter word](answers/k20_upper188322.word) remain unchanged.
The latter has SHA-256
`0d42106351f630eda5693e91a246ceb738f0704004a38b803eba8456aeec3874`.

The finite word certificates require no asymptotic PBBS estimate. These
older words remain verified constructions, but their lengths are strictly
above the now-proved optima 48,623, 92,381 and 184,759.
