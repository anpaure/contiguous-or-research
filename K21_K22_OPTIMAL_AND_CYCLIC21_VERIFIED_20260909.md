# Exact optima at dimensions 21 and 22

September 9, 2026. The user supplied these constructions. This record
documents independent verification, not a new discovery of the words.

\[
\boxed{\mu(21)=352716,\qquad
\nu(21)=B(21)=352719,\qquad
\nu(22)=B(22)=705435.}
\]

Both ordinary additive gaps are zero. Together with the earlier cases,
equality is established through22. The all-dimension existence problem
remains open. The next independently computed lower-bound targets are
`B(23)=1352082` and `B(24)=2704159`; neither is claimed attained here.

## Supplied solutions and complete checks

| Dimension | Word | Length | Nonempty targets | Missing | Gap to B |
|---:|:---|---:|---:|---:|---:|
| 21 | [Optimal word](answers/k21_optimal352719.word) | 352,719 | 2,097,151 | 0 | 0 |
| 22 | [Optimal word](answers/k22_optimal705435.word) | 705,435 | 4,194,303 | 0 | 0 |

Raw SHA-256 values:

```text
k21 eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2
k22 a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd
```

Two independently organized complete enumerations passed. The suffix
recurrence records every distinct suffix OR at each endpoint. The forward
method instead groups coordinates by first occurrence after each start,
adding all coordinates arriving in the same letter together. Neither uses
a witness-length cutoff. A separate segment tree recomputes the OR of
every saved suffix-method witness directly from the literal input.

| Check | Dimension21 | Dimension22 |
|:---|---:|---:|
| Suffix OR-change events | 4,937,949 | 9,875,974 |
| Forward first-occurrence events | 4,937,973 | 10,228,713 |
| Witnesses independently range-checked | 2,097,151 | 4,194,303 |
| Maximum saved witness length, observed after scanning | 29 | 29 |

All letters are nonempty and all witnesses ordinary and nonwrapping.
Every rank count equals its binomial layer. Only the first three endpoints
lack a rank-eleven suffix union; every later endpoint supplies a different
eleven-set. No PBBS construction or asymptotic result is a premise of
these complete literal checks.

## Matching analytic lower bounds

For rank s, the endpoint theorem gives length at least `M+t`, where
`M=binom(k,s)` and t is the least nonnegative integer satisfying

\[
\sum_{j=1}^{s-1}\binom{k}{j}\le tM+\frac{t(t+1)}2.
\]

At rank11 the decisive values are:

| k | M | Required smaller targets | Capacity at t=2 | Least t | M+t |
|---:|---:|---:|---:|---:|---:|
| 21 | 352,716 | 1,048,575 | 705,435 | 3 | 352,719 |
| 22 | 705,432 | 1,744,435 | 1,410,867 | 3 | 705,435 |

Both implementations evaluate every rank with exact integers and verify
minimality of t on both sides. The unique maximizing rank is11 in each
dimension. The verified words meet these lower bounds. The general proof
is retained in [MASTER Section2](MASTER_HANDOFF.md#2-sharp-lower-bound-finite-theorem-and-unconditional-upper-bounds).

## Cyclic core, safe opening and exact lift

Let M=352716 and C be the first M letters of the21 word. The checker proves
that the supplied word is exactly `C+C[:3]`, with first three masks
`1499680,1372192,1358336`. Every saved ordinary target witness spans at most
one period. Reducing its start modulo M preserves all its letters, proving
that C is cyclically universal. The cyclic endpoint bound gives `mu(21)>=M`,
so this [extracted cyclic word](witnesses/k21_k22_optimal/k21_cyclic352716.word)
is optimal. Its SHA-256 is
`f6121263598c34174d59c38f39096e24170f0ef9108a0acccd963a36f52d9d02`.

All M cyclic triples enumerate the ten-sets exactly once; all M cyclic
four-letter windows enumerate the eleven-sets exactly once. Complete
ordinary coverage verifies the particular safe opening, including higher
targets. No claim is made that every cut is safe.

With z=2097152, the periodic-core lift is

```text
A21, {z}, (C[(3+j) mod M] union {z}) for j=0,...,M-2.
```

The initial state and the next M-1 periodic states together represent
every base target. Appending `{z}` marks the initial suffixes; subsequent
marked letters follow those periodic states. The length is `2M+3=705435`.
The regenerated22 output is byte-identical to the supplied file, whose
full coverage was also checked independently.

## Sources, reports and execution provenance

- [Suffix, every-witness range check, cyclic core and lift source](scripts/verify_k21_k22_optimal_suffix_and_lift.py).
- [Complete paired report](witnesses/k21_k22_optimal/complete_suffix_range_cyclic_lift_certificate.json).
- [Cyclic/opening/lift report](witnesses/k21_k22_optimal/cyclic21_and_periodic_core_lift.json).
- [Every21 target witness](witnesses/k21_k22_optimal/k21_all_target_witnesses.jsonl.gz) and [every22 target witness](witnesses/k21_k22_optimal/k22_all_target_witnesses.jsonl.gz).
- [Independent forward proof and source record](scratch/K21_K22_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md).
- [Independent complete forward report](scratch/k21_k22_optimal_forward_20260909/k21_k22_optimal_forward_complete_certificate.json).

Both complete sources were read by root and a separate agent before one
fixed h100 execution each. The suffix/range/lift run used13.289354858 CPU
seconds and13.289871970 wall seconds, within120 CPU/150 wall seconds,
3 GiB address space and512 MiB per file. The forward run used7.738175413
CPU seconds and7.739107305 wall seconds, within60 CPU/90 wall seconds,
2 GiB and256 MiB per file. No retry, alternative input, construction search
or unprovided generator replay occurred.

```text
Suffix source  cf2701d2e7e3fe95d078d472a03caead671a20a671c34bacc160c73aece9fc1f
Suffix report  d5a6e51f5d5c14cf218b86c7e9ee1d8885f43525c87b1c58619e35d01e375706
Forward source ce205cef9f5f2208bcaccd1bb2f1d25ecd29f19f01782c17040ab89874080312
Forward report 137029022789f1af18e949c870945a8b1d0bfb874b9e306f792b82770bdeb4fb
```

The user's compact successor records, skeleton search, Hall-flow file and
full generator package were not attached. Their numerical claims are not
silently credited as separately replayed here. The raw words suffice for
the finite equalities; the cyclic core and periodic lift above are directly
reconstructed from those raw words.

## Progress history and general compatibility result

| Stage | Upper21 | Upper22 | Gap21 | Gap22 |
|:---|---:|---:|---:|---:|
| Earlier three-cycle construction | 353,297 | 706,594 | 578 | 1,159 |
| Overlapping local refinement | 353,094 | 706,188 | 375 | 753 |
| Later supplied upper words | 352,862 | 705,724 | 143 | 289 |
| Current exact words | **352,719** | **705,435** | **0** | **0** |

The intermediate352862/705724 pair also passed a separate full suffix,
every-witness range check and ordinary doubled-lift run before the optimal
files arrived. Its [complete report](witnesses/k21_k22_local_compatibility/complete_suffix_range_lift_certificate.json)
is retained. Its prepared forward checker was not executed, because the
optimal pair superseded that task.

The accompanying [three-placement compatibility audit](scratch/THREE_PLACEMENT_COMPATIBILITY_AND_THIRTEEN_VERTEX_WITHDRAWAL_AUDIT_20260909.md)
passes the bounded-obstruction theorem: every infeasible triple-preserving
placement matching has an infeasible subfamily of at most three placements.
For protected q-windows the proved bound is `max(q,q(q-1)/2)`. A new placement
has an exact local withdrawal formulation on at most13 old placements,
with occupied cells forced out and cyclic neighborhoods deduplicated.
This gives a finite feasibility description, not all-dimension existence.
The older462 Hall deficiency remains true for its particular old skeleton.
