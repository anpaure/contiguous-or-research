# Forward-prefix integer frontier: independent source-code audit

Date: 2026-09-08. Reviewer: `exact_b_induction`.

Reviewed in full:
`scratch/census_pbbs_forward_prefix_integer_frontier_20260908.py`.
Verdict: **PASS; no correction required before the specified bounded run.**
No execution was performed by this reviewer. This is a source review, not
a claim that the r=163 target has passed or that the user's 713-case band
has been reproduced.

The mathematical reference is
`scratch/PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md`.
The program implements one full small-r validation for r=1,...,8 followed
by one r=163 attempt at 10000*U<Cat_r. It contains no other band sweep,
priority variation, or restart.

## 1. Period and terminal conventions

`next_beta` computes the exact reduced fraction

    beta_(s+1)=(1+(2b+1)*beta_s)/(2a+1).

For reduced num/den, `divided_denominator` returns

    den*d/gcd(num,d)=den((num/den)/d),

which is correct because gcd(num,den)=1. Every child P is the lcm of its
parent P and this denominator. The initial P=n=2r+1 is a valid divisor
even before a row is processed.

At b=0, `make_node` correctly keeps beta_s and P_s in the stored state,
but computes the separate `charge_period` as

    lcm(P_s,den((1+beta_s)/(2a+1))).

This processes the unique final one-slot row of least period one. Its
height s+1 and completion mass w are exact. A terminal node is never put
in the refinement heap, so no K(0,c) or missing terminal row occurs.
The replay computes this same terminal update independently with
`Fraction` and includes it in every terminal charge and exact comparison.

## 2. Complete root partition and rounded charges

`K(a,b)` uses the exact integer Narayana expression and checks division
by a. Initialization includes every b=0,...,r-1 with weight one and
checks their sum is Cat_r.

`child_specifications` includes every

    max(0,2b-a)<=c<b,

and every positive ordered least-period class for row mass a-2b+c and
2b+1 slots. `row_classes` uses divisor subtraction without a necklace
quotient and checks that the class counts sum to the full composition
count. Its special assertions correctly cover zero rows and one-slot rows.

Each split checks the sum of child masses equals the parent mass. It
also checks that every child charge period is a multiple of the parent's
charge period and the child height cap does not grow. The displayed
cross-multiplied inequality verifies per-root unrounded domination;
combined with mass conservation this proves the full unrounded split
inequality without constructing a large common denominator.

Each node's integer charge is exactly

    ceil(mass*(2*height_cap-1)/charge_period).

The program does not assume the sum of these ceilings decreases. It
counts increases, updates U by the actual difference, and freshly sums
both total mass and U from every active leaf at stopping. No unfinished
leaf is discarded. The target test is the exact strict integer comparison
10000*U<Cat_r, and the reported word-length upper bound n*(Cat_r+U)
agrees with the proved rounding convention.

## 3. Priority-free transcript replay

The split log records the chosen parent ID and contiguous child IDs,
not a trusted list of child states. `replay_frontier` reconstructs the
initial partition, removes each recorded active parent once, regenerates
every possible child using the complete c range and a separate row-count
routine, and recomputes beta with `Fraction`.

It checks every logged child count, child mass, child ceiling sum, current
mass, and current U. It does not reconstruct or assume the priority queue.
The final-leaf file is checked by popping each recorded leaf ID from the
reconstructed active dictionary. Duplicate IDs fail, missing IDs leave
nonempty state and fail, and every stored primitive and derived field
must equal the replayed value. Thus the transcript cannot certify a
favorable partial collection while omitting unfinished leaves.

The separate row-count routine shares the proved divisor-subtraction
identity with the builder; it is not an unrelated mathematical formula.
The relevant independence here is from the priority choices and from
trusting generated child records, with separate rational arithmetic for
the period updates. This is accurately described as priority-free replay.

## 4. Small-r comparison

For r=1,...,8 the heap is exhausted, so all final nodes are complete
least-period signatures. The code compares against the hash-pinned prior
partition census:

* exact signature count and the integer n*mass/period cycle count;
* total cycles, total cycle heights, and total collar overhead;
* full period and height histograms;
* exact rational unrounded root charge times n.

It correctly does NOT compare rounded U to the exact native charge,
since the former can be strictly larger. Every small-r run also gets
the complete priority-free transcript replay. A disagreement stops the
program before the r=163 attempt.

## 5. Resource and stopping behavior

Execution is restricted by a hostname assertion to the intended h100
host. Hard process limits are 120 CPU seconds, 150 wall seconds, 2 GiB
address space, and 1 GiB maximum size per output file. There are also
limits of 10000 refinements and 1000000 generated nodes.

The r=163 build checks the absolute elapsed CPU and wall time since
program start at 65 and 85 seconds, reserving the remaining hard budget
for output and replay. These counters include small-r validation and
therefore cannot silently spend a fresh full build budget afterward.

At a generated-node limit, child specifications may have been computed
but the parent has not yet been popped or split: the current active leaf
partition remains complete. All other soft stops likewise serialize the
entire valid frontier. The fixed hard limits also cover each individual
split and the replay, even though the soft checks occur between splits.

The top-level final certificate is written only after all replays pass.
Memory failure is explicitly marked inconclusive. A hard CPU, wall, or
file-size termination before the final replay/report must likewise be
reported as incomplete; an earlier `pre_replay_summary.json` is not a
completed replay certificate. The reserved time is a practical allowance,
not a proof that every possible frontier will finish replay within it.

## 6. Scope

If the single run completes, its final report will certify either the
specified r=163 target or a valid upper bound at the fixed stopping
frontier. Failure of the rounded target is not a lower bound on the
native constructor or on nu(k). Even a successful r=163 certificate does
not reproduce the missing 713-case user band. No numerical outcome is
claimed by this pre-execution review.
