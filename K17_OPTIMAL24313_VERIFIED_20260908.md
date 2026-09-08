# Exact finite result: nu(17)=B(17)=24,313

2026-09-08. **[I]+[W].** The supplied literal word has been independently
verified to attain the analytic endpoint lower bound:

\[
\boxed{\nu(17)=B(17)=24,313.}
\]

This closes the entire previous 345-position gap and extends the established
finite equality range through dimension 17. It is independent of the PBBS
asymptotic manuscript, matching-corridor and pruning premises. It does not
settle equality in every dimension.

## The actual finite certificate

- [Optimal word](answers/k17_optimal24313.word).
- [Standalone verifier](scripts/verify_k17_optimal24313.py).
- [Executed verification report](witnesses/k17_optimal24313/verification.json).
- [All 131,071 target witnesses](witnesses/k17_optimal24313/all_target_witnesses.json.gz).
- [Independent lower-bound and optimality audit](scratch/K17_STANDALONE_ENDPOINT_LOWER_BOUND_AND_LITERAL_OPTIMALITY_AUDIT_20260908.md).
- [Independent forward-scan and opening certificate](scratch/K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md).
- [User's supplied construction explanation](scratch/K17_OPTIMAL24313_USER_PROOF_20260908.md).

The source was `/Users/amir.nuriyev/Downloads/k17_optimal24313.word`.
The archived word has SHA-256

```text
7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9
```

The root checker ran only on h100, with limits of 30 CPU seconds,
45 wall seconds and 1 GiB. It completed in about 0.139 seconds:

| Check | Result |
|---|---:|
| Letters | 24,313 |
| Nonempty 17-bit masks | all |
| Distinct nonempty interval targets | 131,071 |
| Missing targets | 0 |
| Nonwrapping witnesses independently rechecked by a range-OR tree | 131,071 |
| Endpoint lower bound | 24,313 |
| Gap | 0 |

At each endpoint the checker computes exactly the distinct suffix unions
using `R_new={letter} union {old_OR | letter: old_OR in R_old}`. Induction
identifies these with all nonempty intervals ending at that endpoint.
Keeping one actual start for each union cannot lose a target. The union
over all endpoints is therefore the exact full interval coverage.

The checker then builds a separate segment tree directly from the word
and rechecks every saved interval. Every interval has ordinary inclusive
endpoints in the file; none wraps. Each rank contains exactly binom(17,r)
targets. No construction generator, solver result or earlier verifier is
imported by this program.

A separately implemented direct forward scan also passed. It starts at
every left endpoint and extends rightwards until the full set appears or
the word ends. Further extensions after the full set cannot add a new
union, so this is exhaustive. It examined exactly 552,396 intervals and
found all 131,071 targets independently of the suffix and tree methods.
Its h100 run took about 0.406 seconds under the same resource caps.

## Self-contained matching lower bound

Put W=binom(17,9)=24,310 and
Lambda=sum_(j=1)^8 binom(17,j)=65,535. Choose one interval witness for
each nine-set. Two distinct equal-rank witnesses cannot contain one
another, since interval containment implies containment of their unions.
Their left endpoints are consequently distinct, so a universal length N
must first satisfy N>=W.

Write N=W+t, t>=0. Order the nine-set witnesses I_i=[ell_i,r_i] by their
left endpoints. Their right endpoints are also strictly increasing.
The two ordered endpoint sequences satisfy

    i<=ell_i<=r_i<=i+t,  1<=i<=W.

Every valid interval [a,a+t] therefore contains I_a: its possible starts
are exactly a=1,...,W. Every longer interval also contains such a window.
Thus targets of rank below nine must use intervals of length at most t.
There are only

    sum_(j=1)^t (N-j+1)=tW+t(t+1)/2

such intervals, with the empty sum interpreted as zero when t=0. For
t<=2 this is at most 2W+3=48,623<65,535. A universal word must have
t>=3, hence N>=24,313.

The verified literal word attains that bound. This proves optimality
without assuming how the word was found.

## Construction explanation and scope

The user describes a changed middle-layer chronology with two cycles,
of lengths 24,225 and 85, and a joint opening using three copied letters.
That would be a change of the state inventory, so the previous fixed-native
PBBS routing obstructions do not contradict it. Those obstructions never
excluded unrestricted words or changed chronologies.

The independent forward checker verified the opening and cyclic families
directly. Extract Q as the first 85 letters and R as zero-based positions
86 through 24,310. Their lengths are 85 and 24,225, and the final word is
exactly Q || Q_0 || R || R_0 || R_1. Their cyclic families contain 664
and 130,748 targets and together cover all 131,071. Across the two cycles,
every eight-set occurs exactly once as a three-letter union and every
nine-set exactly once as a four-letter union.

The two separately opened blocks cover 639 and 130,747 targets. Their
union misses exactly 27,299, 27,303, 27,315, 27,319 and 29,363. The actual
six-letter boundary is

    (19076, 19106, 8834 | 25249, 689, 12849).

Its local one-based intervals [2,4], [1,4], [2,5], [1,5] and [3,6]
realize those five targets, respectively. All five cross the join.
All other internal witnesses survive concatenation. Thus the two-block
explanation is itself independently checked from the supplied file.

The whole linear word also has the exact reported short-window table:

| Length | Ranks of all unions | Distinct targets |
|---:|---|---:|
| 1 | 1–6 | 21,777 |
| 2 | 7 | 19,448 |
| 3 | 8 | 24,310 |
| 4 | 9 | 24,310 |
| 5 | 10 | 19,448 |

In particular, its 24,310 four-letter windows are all distinct. Full
higher-rank coverage was checked by the exhaustive scans, not inferred
from this table.

The separate 1,430-row quotient certificate, search
history and generator were not supplied here; their claimed regeneration
is not needed for the literal optimality proof and is not asserted to have
been independently replayed.

The all-dimensional objective remains open. The standard exact lift now
gives nu(18)<=48,626, only three above B(18)=48,623. Its
[literal word and all 262,143 witnesses passed independently](scratch/K18_VERIFIED_48626_TRIMMED_LIFT_FROM_OPTIMAL_K17_20260908.md).
No improvement at 19 or 20 is
inferred solely from the new 17-dimensional optimum.
