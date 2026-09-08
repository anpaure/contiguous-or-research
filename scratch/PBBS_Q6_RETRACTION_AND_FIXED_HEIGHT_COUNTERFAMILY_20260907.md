# PBBS Q6 retraction: fixed height, unbounded planted-letter lifetime

Date: 2026-09-07. Pure symbolic proof; no computation. Independently
checked by the coordinator and the cyclic-construction task.

## Verdict and scope

Theorem Q6 of `MATH_THEOREM_PBBS_QUEUE_FLUSH_DYNAMICS_AND_RUN_CONSERVATION_20260820.md`
is false. Its condition `S(D)=empty` does not imply that the newly planted
letter exits in `ht(D)+O(1)` updates, or even in `O(ht(D))` uniformly.
Consequently its Q6.1 fast-run count and Q6.2 Gaussian-scale packing
obstruction, and route-closure statements depending on them, are not
established by that argument. They are not asserted false here: a different
positive-density argument could still prove them.

The independent full-cube upper bound 1.180703803847... and the current
master handoff are unaffected. Rare short runs can disprove an every-run
floor without proving the missing positive-density packing obstruction.

## Exact counterfamily

For a Dyck word, split at its first maximum-attaining up-step and the first
subsequent return to zero:

    D=P 1 R 0 S,          tau(D)=S 1_new P 0 R.

The old displayed 1 is consumed; the new 1 is planted; letters of P,R,S
retain their identities. This is the exact map used by Q1. For q>=1 put

    A=111000, B=1100,
    D_q=1 B^q 0, E_q=A B^(q-1), F_q=B^(q-1) A.

The word D_q has semilength 2q+1, height three, and only one arch, hence
S(D_q)=empty. Its factorizations and images are

    D_q=(11) 1 (00 B^(q-1)) 0       -> E_q,
    E_q=(11) 1 (00) 0 B^(q-1)      -> F_q,
    F_q=(B^(q-1) 11) 1 (00) 0      -> D_q.

For q=1 the three unmarked words coincide, but the letter identities still
evolve. For q>=2, E_q already has q arches, directly refuting the induction
that a primitive input stays a single arch.

Mark the letter planted on D_q -> E_q. It is at position 1 in E_q, then
position 4q-2 in F_q, then position 4q-1 in D_q. These first two subsequent
updates put it in P, increasing its height from one to three. It is now the
peak of the last B copy inside D_q.

If the mark is the peak of B_j for j>=2, the next three updates place it
in R,S,P, respectively, and move it to the peak of B_(j-1). Its positions
are 4j-1, 4j, 4j-6, 4j-5 in D_q,E_q,F_q,D_q. When it reaches B_1 it is
the first maximum and the next update consumes it. Thus the number T of
subsequent updates after planting, including consumption, is exactly

    T(D_q)=2+3(q-1)+1=3q.

Height is fixed at three while T is unbounded. This is a tracked-letter
proof, not an inference from the period of an unmarked word.

## Endpoint convention and surviving identities

Let p,r,s count nonconsuming updates at which the marked letter lies in
P,R,S. The exact height changes are +1,-1,0. Therefore

    p-r=h-1,     T-1=p+r+s,     T=h+2r+s.

Q4's old formula with h-1 instead of h counts only the nonconsuming
updates, and is inconsistent with its own T=3 example for 111000 unless
that endpoint convention is changed. This one-step correction is separate
from Q6's unbounded error. Q1-Q3 do not rely on Q6; a comparison of two
uninterrupted climbers cannot exclude the explicit R,S interruptions above.
The informal cone discussion is not a quantified replacement theorem.

## Dependencies and prior record

The corrected greedy packing inference `a W` intervals of length at most H
with distinct starts => Omega(W/H) disjoint intervals remains valid, but
Q6 does not supply its assumed family of short intervals. Proposition4.1's
empty-front/positive-density claim and Sections4-6 of the queue-flush file
must not be used as proofs of route closure. The companion run-length
file's status updates in Sections8,9.3,10 have the same failed dependency.

The q=2 word 1110011000 and its quotient cycle already occur in
`PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md` and Section23 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, retracting a related
primitive height-time mechanism. The present contribution is the explicit
unbounded fixed-height family and marked lifetime, not discovery of that
individual word. Those earlier retractions must not be overwritten by a
later unsupported status claim.
