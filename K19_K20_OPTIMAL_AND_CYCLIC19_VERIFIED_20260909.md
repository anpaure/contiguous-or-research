# Exact optima at 19 and 20, independently verified

Date: 2026-09-09. The user supplied the two already constructed literal
words. This record verifies those words and reconstructs their stated
periodic lift; it does not claim their discovery or replay an unavailable
construction search. Every mathematical program below ran on `h100`
(`arboghast`), after complete source review and with fixed resource limits.

\[
\boxed{\mu(19)=92378,\qquad \nu(19)=B(19)=92381,\qquad
\nu(20)=B(20)=184759.}
\]

Together with the previous certificates, equality is established through
dimension 20. The first unsettled finite case is now 21. The objective
of proving equality in every dimension remains open.

## Literal words and complete verification

| Dimension | Length | Nonempty targets covered | Missing | Separately rechecked witnesses |
| ---: | ---: | ---: | ---: | ---: |
| 19 | 92,381 | 524,287 | 0 | 524,287 |
| 20 | 184,759 | 1,048,575 | 0 | 1,048,575 |

- [Optimal 19 word](answers/k19_optimal92381.word), SHA-256
  `1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
- [Optimal 20 word](answers/k20_optimal184759.word), SHA-256
  `047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02`.
- [Universal 19 cycle](answers/k19_cyclic92378.word), SHA-256
  `ff7e753ecd579283e519c14df10d3123bde562ca682c667af04543a5576192dc`.

All letters are nonempty masks on the stated alphabet. All witnesses for
the ordinary words are nonwrapping. Three complete checks passed:

1. For each left endpoint, an independent implementation groups the first
   future occurrence of each coordinate. Adding all coordinates with the
   same first-occurrence position enumerates exactly every distinct
   forward interval union. It found 1,200,848 events at 19 and 2,494,149 at 20.
2. A separate suffix implementation uses
   `R_j={A_j} union {A_j OR S:S in R_(j-1)}`. It found 1,200,846 events
   at 19 and 2,401,761 at 20 and recorded a witness for every target.
3. A separate segment tree recomputed the literal interval OR for every
   recorded witness. Every query equalled its target.

Both words have exactly three endpoints without a rank 10 suffix target:
zero-based positions 0, 1, 2. Each later endpoint supplies a distinct rank 10
target. Maximum length among the saved witnesses is 29 in both words.

[Forward checker](scratch/verify_k19_k20_optimal_forward_first_occurrence_20260909.py)
and [its complete report](scratch/k19_k20_optimal_forward_20260909/k19_k20_forward_complete_certificate.json)
are separate from the
[suffix, range, cycle and lift checker](scripts/verify_k19_k20_optimal_suffix_and_lift.py)
and [its complete report](witnesses/k19_k20_optimal/complete_suffix_range_cyclic_lift_certificate.json).
Complete target-indexed forward witnesses and gzipped suffix witnesses
are retained beside the respective reports.

The two reviewed runs took about 1.805 and 3.226 seconds respectively. Their
limits were 60 CPU seconds and 90 wall seconds; no word search was run.
Internal code reviews are not formal or external mathematical certification.

## Matching analytic lower bounds

Fix rank s and choose one ordinary witness for each of its M=binom(k,s)
targets. Distinct equal-rank witnesses cannot contain one another or
share an endpoint. Ordered by their left endpoints, their right endpoints
therefore also increase. In a word of length M+t the i-th witness lies
inside `[i,i+t]`. Hence every interval of length t+1 contains a rank-s
witness, and every smaller target requires at most t positions.

There are exactly `t M+t(t+1)/2` intervals of length at most t. Thus

\[
\sum_{j=1}^{s-1}\binom{k}{j}\le tM+\frac{t(t+1)}2.
\]

At rank 10:

| k | M | Smaller targets | Capacity at t=2 | Required minimum length |
| ---: | ---: | ---: | ---: | ---: |
| 19 | 92,378 | 262,143 | 184,759 | 92,381 |
| 20 | 184,756 | 431,909 | 369,515 | 184,759 |

The literal words attain these lower bounds. Both implementations also
maximize the exact endpoint bound over every rank, with the same answer.
These finite equalities require no PBBS, corridor, concentration, or
asymptotic premise.

## Exact cycle, safe opening, and byte-identical lift

Let M=92378 and C be the first M masks of the supplied 19 word A. The
checker establishes `A=C+C[:3]`, with first three masks
`364614,376898,104514`. The M cyclic triple windows enumerate all nine-sets
once; the M cyclic four-letter windows enumerate all ten-sets once.

Middle-layer identities alone would not prove upper-target coverage.
Here every target already has a checked ordinary witness in A of length
at most 29, hence at most M. Reducing its start modulo M gives the same
letters in C and a valid cyclic witness. Thus C is cyclic universal.
One cyclic endpoint supplies at most one ten-set, so no universal cycle
can have fewer than M positions. This proves mu(19)=M.

A general periodic-core lift is valid whenever `0<=d<M` and `C+C[:d]`
is itself ordinary universal. After that word, the actual recency state is the
periodic state at phase d-1. That state plus the next M-1 periodic updates
visits every phase and supplies every old target as a suffix union.
Appending `{z}` and marking those M-1 updates therefore supplies every
target containing z; the old word retains all unmarked targets. This gives

    B = A + [z] + [C[(d+j) mod M] OR z for j=0,...,M-2],
    length(B)=2M+d.

For the supplied words, d=3 and z=524288. The checker regenerated every
mask of B and compared its serialized bytes with the supplied 20 file:
the files are identical. The regenerated word is retained with the report.
Its universality also passed the independent complete literal checks above.

For M=W(k), every periodic state has initialized optimum lambda=M-1:
the cycle supplies the upper bound, and each state supplies at most one
middle-rank target. The lift is also the retained border-sensitive splice
specialized to this periodic opening. Neither proof asserts existence of
the required cycles and safe openings in every odd dimension.

[Independent proof audit of the endpoint and periodic-lift laws](scratch/K19_K20_ENDPOINT_PERIODIC_LIFT_AND_TURNOVER_AUDIT_20260909.md).

## Structural consequence for further work

A separate literal reconstruction checks the actual carrier and cap
assignment against the fixed canonical 19 PBBS data. It finds that the
outgoing canonical matching is retained on all 92,378 lower labels, while
70,452 incoming incidences change. The native 360 cycles become one literal
cycle. This is a second exact finite instance, after 17, of retaining the
outgoing matching while changing the chronology.

The seven-set envelopes contain the literal letters and have the stated
triple/four unions. Actual caps change 12,654 adjacent-pair unions while
preserving every triple. Literal masks and adjacent pairs together cover
all 169,765 targets of ranks 1 through 8, checked as actual sets. Of the
rank-at-most-seven targets, 11,324 occur as pairs but not as letters.
All 4,862 rotation-quotient records, including coordinate phases and literal
caps, can be recovered from the supplied word; this is a reconstruction,
not a replay of the unprovided compact certificate or search.

[Full structural proof and census](scratch/K19_OPTIMAL_LITERAL_PHI_CARRIER_PAIR_CHANGING_COMPILER_AND_QUOTIENT_CERTIFICATE_20260909.md)
and [complete structural report](scratch/k19_literal_structure_20260909/literal19_structural_reconstruction_certificate.json)
retain every named row, low-target witness, changed pair and incoming
alternating circuit. That third reviewed run took about 2.659 seconds.
The report SHA-256 is
`68c2187cd9ec3d7ccf14c35588265e32fb96daacafe48e63d1325b3f2e02c566`.

The general cap-feasibility principle is monotonic: assigned short witness
intervals force each letter into the intersection of its envelope and all
targets assigned through that position. Such assignments are feasible
exactly when these maximal caps are nonempty and meet every required
short-target and preserved-window union. Proving a simultaneous assignment
and a suitable carrier in every dimension is still necessary.

A [capacity and opening audit](scratch/UNIFORM_CYCLIC_MIDDLE_WINDOW_CAPACITY_AND_OPENING_OBSTRUCTION_20260909.md)
also makes the needed generalization precise. In a cyclic universal core
of width M=binom(2r+1,r), if every q-window has rank r, then

\[
q\ge\left\lceil\frac{4^r-1}{M}\right\rceil,
\qquad d\ge q
\]

for any universal opening consisting of that period and d further
periodic letters. The required q grows at least as
\(\sqrt{\pi r}/2\). Thus the fixed triple architecture cannot persist in
all dimensions. This is a necessary condition for that architecture,
derived from the existing endpoint capacity principle; it is not a new
lower bound excluding unrestricted exact words.

## Next exact target and scope

The same exact arithmetic gives B(21)=352719 and B(22)=705435. These are
lower bounds, not newly attained values. The first open finite target is

\[
\boxed{\nu(21)\stackrel{?}{=}352719.}
\]

The user's turnover bound gives 5,599 present-to-absent transitions per
coordinate at that target. The already proved paired-endpoint inequality
is stronger: it requires 16,793 exits and 16,793 entrances for every
coordinate. These are necessary conditions, not impossibility results.

The old native construction's exponential additive-overhead barrier is
unaffected: it constrains that specific unmodified word, not the optimum.
No all-dimensional exactness, new 21 search, unavailable 19 generator replay,
or new proof of the inherited PBBS support lemmas is claimed here.
