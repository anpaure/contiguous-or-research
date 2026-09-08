# Verified k18 upper word of length 48,626 from the optimal k17 word

2026-09-08. One deterministic construction and complete verification by
`exact_equality_structure`, executed only on h100.

The standard trimmed one-coordinate lift of the verified 24,313-letter
k17 word gives an explicit nonzero k18 word of length 48,626. Every one
of its 262,143 nonempty target masks has an ordinary contiguous interval
witness, independently replayed by a segment-tree OR query. The exact
endpoint lower bound is 48,623. Thus

    48,623 <= nu(18) <= 48,626.

The remaining upper-minus-lower gap is three. This is not a proof of
optimality at k18, and no deletion or optimization was attempted.

## 1. Exact literal construction

Let A=(A_1,...,A_m) be
[answers/k17_optimal24313.word](../answers/k17_optimal24313.word),
with m=24,313. Use the new coordinate z=18, represented in the
zero-based bitmask convention by 2^17=131,072. Emit

    A_1,...,A_m,{z},
    A_1 union {z},...,A_(m-1) union {z}.                (1.1)

The resulting word has m+1+(m-1)=2m=48,626 nonempty letters. It is
saved as
[answers/k18_upper48626.word](../answers/k18_upper48626.word).

Every old target remains in the first copy of A. For a target T union
{z}, choose an old witness A_i,...,A_j for nonempty T. If j<m, its
lifted copy in the final part of (1.1) is a witness. If j=m, the
old suffix A_i,...,A_m followed by the bridge {z} is a witness.
The bridge alone supplies {z}. This proves full coverage from the
already verified base word without needing any special endpoint
property of A.

The base file SHA-256 used in the run is

    7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9.

The output word SHA-256 is

    52a68ff6bb2757c00b4be03edbb53eaf821d5dca0985d0a680941502d0c2315b.

## 2. Complete direct target and witness verification

The standalone program
[construct_and_verify_k18_trimmed_lift_48626_20260908.py](construct_and_verify_k18_trimmed_lift_48626_20260908.py)
builds exactly (1.1), then processes every endpoint of the resulting
literal word. Its ending-OR recurrence retains a latest start for
each distinct suffix OR. Equal old suffix ORs have equal extensions,
so retaining one latest start cannot omit any target. No interval
sampling or rank restriction is used.

It finds all 262,143 nonempty target masks. For every target it saves
an actual pair of inclusive, zero-based interval endpoints. A separate
segment tree built from the emitted literal word then independently
recomputes the OR of every saved interval and checks exact equality
to the target mask.

The target counts by ranks 1 through 18 are exactly

    18, 153, 816, 3060, 8568, 18564, 31824, 43758, 48620,
    43758, 31824, 18564, 8568, 3060, 816, 153, 18, 1.

These are all the binomial layer sizes. All letters are also checked
to be nonempty masks on the 18-coordinate ground set.

## 3. Exact lower bound and the remaining gap

The endpoint lower bound in the master handoff is

    B(k)=max_s (binom(k,s)+tau_s),

where tau_s is the least nonnegative integer t satisfying

    sum_(j=1)^(s-1) binom(k,j)
        <=t binom(k,s)+binom(t+1,2).

For k18 the central layer has

    W(18)=binom(18,9)=48,620,
    Lambda_9=sum_(j=1)^8 binom(18,j)=106,761.

The exact comparisons are

    2*48,620+3=97,243 <106,761,
    3*48,620+6=145,866 >=106,761.

Thus the central delay is three. The retained central-maximization
theorem yields B(18)=48,623; the verifier additionally calculates
the bound at all 18 ranks and confirms this maximum directly.
The construction is therefore three letters above the exact known
lower bound.

## 4. Artifacts and execution

* [Literal upper word](../answers/k18_upper48626.word).
* [Complete certificate](k18_trimmed_lift_48626_20260908/k18_upper48626_certificate.json).
* [Every target's checked interval witness](k18_trimmed_lift_48626_20260908/k18_upper48626.all_target_witnesses.jsonl).
* [Reproducible construction and verifier](construct_and_verify_k18_trimmed_lift_48626_20260908.py).

Each witness line is

    [target_mask, inclusive_zero_based_start, inclusive_zero_based_end].

The witness file SHA-256 is

    6b1995bce7166c21f4ad8381cd8c8c06873ff0e21b396c3d66862ad5fbb9ee75.

The single run used h100 (`arboghast`) with hard limits of 30 CPU
seconds, 45 wall seconds, and 1 GiB address space. It returned PASS
in approximately 0.832 seconds. No mathematical code ran locally.
Remote inputs, program, word, and witnesses remain under

    h100:/home/amodo/exact-b-k18-trimmed-lift-48626-20260908/

No deletions, candidate variants, other-coordinate lifts, or searches
were performed. The result is the direct verified consequence of the
new optimal k17 construction.
