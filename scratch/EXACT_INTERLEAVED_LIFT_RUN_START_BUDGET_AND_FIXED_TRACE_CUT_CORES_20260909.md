# Interleaved dimension lifts: joint run budget and fixed-trace cut cores

Date: 2026-09-09. Pure-proof audit by `exact_b_induction`.

Status: the general inequalities and the conditional fixed-trace theorem
below are proved. No mathematical execution was performed here. Root is
preparing a separate bounded literal/arithmetic check of the exact18 data.
The numerical dimension19 implications use the already proved endpoint
lower bound B(18)=48623; its newly attained equality is not necessary for
the inequalities. No attaining19 word or all-dimensional construction is
claimed.

## 1. What is inherited and what is added

The earlier
`scratch/EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md`,
Sections 2–5, proves the rank-sensitive cut charge and already records
the necessary 541 entrances and 541 exits per coordinate at B(19).
`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Sections 7–8, already
counts old targets inside unmarked runs. The initialized extension and
run version of the exit inequality are independently proved in
`scratch/INITIALIZED_RECENCY_EXTENSION_INTERLEAVING_AND_K18_LOWER_BOUND_AUDIT_20260908.md`.

The additional statements here couple the lost old-target endpoint at
each run start with that same run's possible contribution to marked
targets. They also give the exact cut condition when a target has a
unique endpoint in a fixed unmarked trace. These sharpen the obstruction
to a specific naive insertion construction; they do not introduce a new
unrestricted lower bound beyond the established capacity framework.

Prior-result clarification: the older
`MATH_THEOREM_K17_SATURATED_COORDINATE_ENDPOINT_SPLIT_CEGAR_20260731.md`,
Sections 2–3, already proves a general occupied-cut obstruction and
certifies that a particular optimal16 trace has no internal universal
cut. The present unique-endpoint proof is a convenient special case,
and the checked18 trace is a new finite application, not the first
general fixed-trace cut criterion.

## 2. Run-start endpoint loss

Let V be a universal word on X union {z}, |X|=k. It has total length N
and exactly M letters avoiding z. Let R be its total number of nonempty
maximal unmarked runs, including a possible initial one. Fix 1<=s<=k
and put W_s=binomial(k,s). Let H be the number of these runs whose FIRST
literal letter has cardinality exactly s.

Every old rank-s target has a witness inside one unmarked run. At each
unmarked endpoint its available old suffix unions form a chain, so the
endpoint can supply at most one distinct rank-s target. At the first
position of a run, the only unmarked suffix is the literal letter itself.
Unless that letter has rank s, this endpoint supplies no old rank-s target.
Therefore

    W_s <= M-(R-H),
    R-H <= M-W_s.                                      (2.1)

This counts distinct target capacity; it does not assume distinct active
endpoints actually expose different targets. Repetitions only make the
capacity estimate weaker. Both letters of rank less than s and letters
of rank greater than s are bad starts for (2.1).

In particular, if no unmarked letter has rank s, then R<=M-W_s. Keeping
an optimal18 unmarked trace of length48623 with no rank-nine letters would
allow at most three unmarked runs by this bound alone. That is already
incompatible with the previously required 541 exits at an optimal19 word.

## 3. Coupling old endpoint loss and marked seam capacity

At an exit cut, let C be the union of the OLD projections of its two
adjacent letters. The earlier fixed-cut lemma bounds the distinct marked
targets with old rank s crossing that cut by

    [s-|C|+1]_+.

The right-hand letter is the first letter of the following unmarked run.
If its rank is s, this cut contributes at most one. If its rank is less
than s, it contributes at most s because the letter is nonempty. If its
rank is greater than s, the contribution is zero.

Marked rank-(s+1) targets with a marked right endpoint contribute at most
N-M in total. All others cross an exit cut. The number of bad starts
among exit runs is at most the total bad starts R-H, and the number of
good exit starts is at most H. Combining the cut charge with (2.1) gives

    W_s <= (N-M)+s*(R-H)+H
         <= (N-M)+s*(M-W_s)+H.                          (3.1)

Consequently

    H >= (s+1)*W_s-N-(s-1)*M.                           (3.2)

Negative right sides may be replaced by zero. This is a joint inequality
on the SAME runs and endpoints. It does not multiply independent trial
probabilities or assume independence of two covers.

The reflected theorem holds for unmarked-run END letters, by reversing
V and applying the entrance inequality. When the right side of (3.2) is
positive, that many rank-s start letters and that many rank-s end letters
are each required; these are separate counts and may overlap at a
singleton run.

For s>=2, if H=0, rearrangement gives

    M >= ceil(((s+1)*W_s-N)/(s-1)).                     (3.3)

For s=1 one must use (3.1) directly rather than divide by s-1.

## 4. Exact dimension19 consequences

Take k=18, s=9, W_s=48620, and N=B(19)=92381. If the unmarked
subsequence has the optimal18 length M=48623, then (3.2) gives

    H >= 10*48620-92381-8*48623 = 4835.                  (4.1)

Thus retaining an optimal-length unmarked trace requires at least 4835
unmarked-run starts whose literal letters have rank nine, and by reversal
at least 4835 such run ends. The earlier 541 transition bound remains
valid but does not contain this additional rank requirement by itself.

If instead the unmarked trace contains NO rank-nine letters, then

    M >= ceil((10*48620-92381)/8)
      = ceil(393819/8)=49228.                           (4.2)

This exceeds 48623 by605. It is not a universal605-letter lower bound on
the new coordinate construction: it applies to the no-rank-nine-literal
restriction on the unmarked subsequence. Changing that literal inventory
is an allowed escape. The exact arithmetic identities in (4.1)–(4.2)
are displayed so a separate numerical certificate can check them directly.

## 5. Exact preservation by inserting marked letters into a fixed trace

Fix an old word A=(A_0,...,A_(M-1)) of nonempty subsets of X. Form a new
word by inserting letters containing z, while requiring that its entire
unmarked subsequence is EXACTLY A in this order. There are no additional
unmarked letters or changes to its literals.

Let J be the set of internal gaps c, 0<=c<M-1, at which at least one
marked letter is inserted between A_c and A_(c+1). Insertions before
A_0 or after A_(M-1) are not in J. An old target D remains covered if and
only if at least one of its original literal witness intervals [a,b]
has

    J intersect {a,...,b-1}=empty.                      (5.1)

Indeed any old witness in the new word must avoid every marked letter,
and so it is exactly an original interval not broken by a cut. Conversely
an unbroken original interval remains an ordinary interval in the new word.
The old projections of the inserted marked letters cannot repair an old
target, because their z coordinate is present.

Suppose D has a UNIQUE old right endpoint e, though it may have several
witness intervals ending there. These intervals are nested. Let a_D be
their largest start, so [a_D,e] is its shortest witness. Then every old
witness contains this one and

    D survives iff J avoids {a_D,...,e-1}.              (5.2)

This is the exact cut core for a unique-endpoint target. For a collection
of such targets, preserving them all is equivalent to avoiding the union
of their cut cores. For arbitrary witness families without the nested
property, intersecting all witnesses gives only individually fatal cuts;
several cuts can collectively destroy coverage even if none lies in that
intersection. Equation (5.2) is not asserted in that broader setting.

## 6. A rigid-endpoint trace forbids every internal insertion

Here is a general sufficient condition for complete internal cut rigidity.
Suppose for some s and d>=1:

1. every rank-s target of A has a unique right endpoint;
2. exactly the endpoints d,d+1,...,M-1 expose those targets, one distinct
   target at each endpoint;
3. every literal A_i has rank different from s;
4. the first target ending at d has shortest witness [0,d].

For an endpoint e>=d, its shortest rank-s witness has length at least
two by condition3, so its cut core contains e-1. Thus all cuts
d-1,...,M-2 are forbidden. The first target's cut core contains all
cuts0,...,d-1. Their union is every internal gap. By (5.2), no nonempty
set of internal marked insertions preserves the old rank-s layer.

For the supplied optimal18 trace, root proposes to certify these premises
with s=9 and d=3: all letters have rank below nine, the only endpoints
without a rank-nine suffix are the first three, all later endpoints give
different rank-nine targets, and the first such target requires the first
four letters. The latter follows if the trailing triple A_1,A_2,A_3 has
rank below nine and A_0,A_1,A_2,A_3 has rank nine: every proper suffix of
those four letters is contained in that trailing triple. An explicit
literal check is appropriate. This note has not run
that check and does not replace it with an assumption about arbitrary
optimal words.

Once these finite premises are verified, EVERY word retaining that exact
unmarked subsequence A has one unmarked block if it preserves the old
cube. All marked letters must lie before or after it. The older exit
inequality then gives

    N >= M+W_9-9 = 48623+48620-9 = 97234.                (6.1)

If there is no preceding marked block, the exit count is zero and the
bound is stronger. Equation (6.1) is therefore valid for the whole
endpoint-only insertion family and excludes B(19)=92381. It is a lower
bound for this fixed-trace architecture, not for unrestricted nu(19).

## 7. The surviving constructive requirement

Many tag transitions alone do not solve an exact dimension lift: they
must coexist with unmarked-run witnesses for every old target. The
fixed rigid trace cannot provide those witnesses after internal cuts.
At the optimal19 budget, a successful construction must change the
unmarked trace itself, its relevant rank-nine literal inventory, or both;
simply marking letters inserted into the checked18 trace is excluded once
the stated finite endpoint premises are verified.

This narrows the task to a genuinely new, extensively interleaved source
or an exact trajectory-splicing theorem that preserves the required old
witnesses across its actual unmarked runs. It does not propose another
one- or two-seam19 search.

## 8. Pre-execution source review of the bounded literal check

This author read all of
`scratch/verify_k18_uncuttable_trace_and_k19_run_budget_20260909.py`
before execution and reported PASS, with no correction required. Its
suffix recurrence stores the greatest possible left endpoint for each
OR, taking the maximum over all predecessor unions that merge to the
same new union. Discarding smaller starts for an identical predecessor
OR cannot lose a larger future start, so this computes the shortest
witness at every endpoint exactly.

The checker separately counts each rank-nine target's endpoint
multiplicity, identifies the first three absent endpoints, and requires
the first present target's greatest start to be zero. For every internal
cut it records a uniquely ended target, verifies that even its greatest
start is at or before the cut, and directly replays that shortest
interval's OR. These conditions are precisely the proof premises in
Sections 5–6. The numerical ceiling and all displayed integer differences
are checked exactly in the same fixed run.

It hash-pins the literal input, permits only nonempty18-bit masks, and
uses hard limits of 30 CPU seconds, 45 wall seconds and 1 GiB address
space on the designated h100 host. It is a finite certificate check,
not a construction search. This paragraph records source review only;
execution results must be attributed separately when the run completes.
