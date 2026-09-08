# Finite adaptive gap queries under actual short-incidence conditioning

2026-09-08. Pure proof; no computation. Root read the complete note and
passed the conditional-composition update, uniform maximal coupling,
fixed-S,M quantifiers, recycled-label, and actual-environment-law checks.
The conclusion concerns a legal query transcript in ORIGINAL coordinates.
It is not a fresh law for reached roots or an unproved trajectory oracle.

## 1. Quantifiers and the accepted exact fibre

Fix c>0 and integers S>=1, M>=0 BEFORE letting r tend to infinity.
Use actual F0 incidence and the safe base event B_(r,S) from
`PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md`: the profile domain of
the accepted finite-layer fibre holds and F_S=0. Its probability tends
to one for fixed S. Expose

    E_r=(entire pruning profile, all original rows s>=S, sampled offset j).

The accepted exact fibre is
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`.
Conditional on each feasible E_r and B_(r,S), rows 0<=s<S are independent.
In row s the s+1 base coordinates 0,-1,...,-s are zero, and the

    P_s=p_s-s-1

remaining labelled coordinates are a uniform weak composition of ell_s.
The exposed environment retains its ACTUAL conditioned incidence law.

A legal exploration may depend on r and E_r and on an independent random
seed. Each requested row/index must be a function only of these inputs
and previously requested indices and returned values. It may query a
base coordinate, revisit a previous coordinate, or request a previously
unseen free coordinate. It may make at most M requests of the last kind.
Assume its reported transcript is finite; arbitrary intervening queries
of already known values can be removed without changing its information.

An unexposed trajectory, cumulative gap sum, reached-root description,
or other function of unrevealed coordinates is NOT an additional legal
input. Such information must first be reconstructed from legal queries.

## 2. Exact deferred decisions, including recycling

Fix E_r and the seed. After any feasible query history, let k_s be the
number of revealed free slots in row s and a_s the sum of their values.
The remaining row-s slots are a uniform weak composition of

    ell_s-a_s into P_s-k_s parts.                    (1)

The unqueried parts of different rows remain independent conditional on
that history. This statement includes the information in which indices
were chosen and when the algorithm stopped.

Proof is by induction over requests. It is true initially by the accepted
fibre. A next index is determined by the known history, hence its choice
does not impose any extra condition on unrevealed coordinates. A base
or repeated request returns an already fixed value and changes nothing.
At a new free slot, fixing its value in a uniform composition leaves a
uniform composition of the residual total in the other labelled slots;
the other rows are unchanged. The induction also explains why an
unrevealed aggregate oracle would invalidate the assertion.

In particular, if the residual parameters at a fresh request are ell,P
with P>=2, its exact conditional mass is

    Pr(value=a | history,E_r)
      = binom(ell-a+P-2,P-2)/binom(ell+P-1,P-1),
                  0<=a<=ell.                       (2)

It is zero otherwise. A repeated label returns the SAME previously
revealed value; it is never resampled.

## 3. Uniform finite-transcript geometric limit

Define a comparison oracle on the identical labelled slots. Base slots
are zero. At the first query of a free slot in row s, return an independent
G_s with

    Pr(G_s=a)=(1-q_s)q_s^a,
    q_s=1/(s+2)^2,  a=0,1,2,... .                   (3)

Store and reuse that value at every repeated request. Different first
queries use independent variables, also independent of E_r and the seed.
Run the SAME adaptive exploration against this oracle.

For every fixed S,M, uniformly over all legal explorations described in
Section 1, the two transcript laws satisfy

    E_[E_r | B_(r,S)] TV(
       Law(actual transcript | E_r,B_(r,S)),
       Law(oracle transcript | E_r,B_(r,S))) -> 0.  (4)

Equivalently, the joint laws of the exposed environment and transcript
are close in total variation when the environment has the same actual
marginal on both sides. No limiting or unweighted law for E_r is asserted.

Proof. The accepted actual-incidence profile concentration gives,
simultaneously at the finitely many queried depths,

    P_s -> infinity,
    ell_s/(ell_s+P_s) -> q_s

in incidence probability. Restriction to B_(r,S), whose probability
tends to one, preserves this statement. Choose shrinking deterministic
typical-profile tolerances such that their exceptional mass tends to zero.

Fix a value cutoff B. On a typical profile, any history with at most M
fresh requests and all their values at most B removes at most M slots
and MB mass from each row. Thus its residual parameters in (1) still
have P tending to infinity and ell/(ell+P) tending to q_s, uniformly
over all these histories, labels, and rows.

The ratio (2) then tends to (3) for each a. Its limiting masses sum to
one, so this convergence is in total variation: restrict to a finite set
whose limiting mass is close to one and control the complementary mass
by subtraction. Uniformity follows by the same argument along every
possible parameter sequence; a sequence violating uniformity would
contradict this pointwise-to-total-variation conclusion. Denote the
resulting uniform one-step error by delta_r(B), which tends to zero.

Couple the seeds and environments identically. At each new free request,
maximally couple (2) to a fresh variable (3), continuing only while
previous replies agree and are at most B. Base and repeated requests
then agree automatically. The chance of any mismatch is at most

    M delta_r(B) + M max_(s<S) Pr(G_s>B)
      <= M delta_r(B) + M 4^(-(B+1)),                (5)

plus the atypical-profile probability. Decisions, selected indices,
stopping, and reported transcripts coincide whenever all replies do.
The bound does not depend on the particular adaptive algorithm.
First let r tend to infinity, then B tend to infinity. This proves (4).

One may define any common exceptional output outside B_(r,S); its o(1)
mass yields the corresponding unconditional actual-incidence comparison.

## 4. What is and is not supplied for a physical exploration

Equation (4) permits adaptively selected original labels and fully accounts
for recycled labels. It applies to a stopped physical construction IF that
construction is explicitly computed from E_r and individual queried gaps
using the rule in Section 1. The conditional law changes exactly as in (1),
not by assigning independent arrays to newly reached roots.

A useful extension is immediate: if the number of fresh queries in a
specified finite physical task is tight, uniformly in r under its actual
base-incidence law, stop after M queries and use (4), then let M grow.
To conclude convergence for the unstopped task one also needs termination
and the corresponding tail control in the comparison exploration (or an
argument transferring that tail from a finite stopped transcript).

This note does not prove that any proposed physical task has that tight
query budget. In particular a selection cocycle evaluated from a whole
unrevealed row is not automatically a legal single query. An infinite-
depth extension, conservative arrival process, sufficient short virtual
births, and the cross-cutoff eligible-label gate remain to be proved.
