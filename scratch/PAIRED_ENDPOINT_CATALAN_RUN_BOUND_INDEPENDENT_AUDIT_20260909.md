# Paired endpoints force a Catalan-scale number of coordinate runs

Date: 2026-09-09. Root proposed the paired-endpoint theorem; this is its
independent pure-proof audit by `exact_b_induction`.

Verdict: **PASS**, including partial coverage, both endpoint orientations,
the stronger joint run-start bound, and all boundary cases below. No
mathematical execution was required for this proof. A subsequent single
bounded diagnostic completed successfully and is attributed in Section6.
No new universal word or all-dimensional exact construction is claimed.

## 1. Partial-coverage theorem

Let V=(V_1,...,V_N) be any word of nonempty subsets of X union {z}, where
|X|=k>=1. Fix 1<=s<=k. Let

    a_s = number of distinct represented rank-s targets avoiding z,
    b_s = number of distinct represented rank-(s+1) targets containing z.

Let R_out be the number of transitions from a z-containing letter to a
letter avoiding z. Equivalently, it counts the nonempty unmarked runs
that follow a marked letter, and excludes a possible initial unmarked
run. Define R_in as the opposite transition count.

**Theorem.**

    a_s+b_s <= N+R_out,
    a_s+b_s <= N+R_in.                                  (1.1)

No universality, fixed-rank literals, or specific construction is assumed.

### Proof for right endpoints

Choose one actual ordinary interval witness for each of the a_s old
targets and one for each of the b_s marked targets. Let E_0 and E_1 be
their sets of right endpoints. Within either selected family, endpoints
are distinct: two suffix intervals ending at the same position are
nested, and distinct targets of the same rank cannot be comparable.
Thus |E_0|=a_s and |E_1|=b_s, and

    |E_0 intersect E_1| >= a_s+b_s-N.                    (1.2)

At a shared endpoint t, denote the old target by D and the marked target
by E. Their suffix intervals are nested. Since z belongs to E but not D,
it is impossible that E is contained in D. Hence D is contained in E.
Their ranks differ by one, so necessarily

    E=D union {z}.                                      (1.3)

The endpoint t is unmarked, because the old witness ends there. The marked
witness contains an earlier z, so let q<t be the last marked position
before t. Let B_t be the union of the unmarked run prefix V_(q+1),...,V_t.
The old witness starts after q, giving D subseteq B_t. The marked witness
starts at or before q and contains the whole run prefix, giving
B_t subseteq E minus {z}=D. Therefore

    B_t=D.                                             (1.4)

Inside a fixed unmarked run, B_t increases by inclusion. It can take at
most one DISTINCT value of cardinality s. The selected old targets D at
different shared endpoints are distinct. Consequently no two shared
endpoints belong to the same unmarked run. Each such run follows a marked
letter, so the assignment is an injection into the R_out exit runs:

    |E_0 intersect E_1| <= R_out.                       (1.5)

Combine (1.2) and (1.5) to obtain the first inequality in (1.1). Apply
that proved statement to the reversed word for the second: ordinary
target coverage is unchanged, and exits in the reversed word are
entrances in the original word. QED.

### Boundary and witness checks

An initial unmarked run cannot contain a shared endpoint, since no marked
suffix witness exists there. A marked endpoint cannot supply an old
target. Repeated equal run-prefix unions at several physical endpoints
do not break (1.5): they would represent the same D, selected only once.
If a_s+b_s<=N, the resulting run lower bound is simply zero. Empty target
families cause no problem. The theorem does not use s=0, because the old
empty target is not part of the universal target family. Marked letters
may be the singleton {z}; their old projection being zero does not affect
any step of the proof.

The recency cursor from
`scratch/EXACT_MANY_RUN_RECENCY_CURSOR_AND_PROTECTED_WITNESS_COMPILER_20260909.md`
gives the equivalent description B_t=C_t=D at a shared endpoint. The
direct interval proof above does not require that auxiliary theorem.

## 2. Universal words and the exact odd-dimensional scale

If V is universal then a_s=b_s=W_s=binomial(k,s). Thus EVERY coordinate
z of a universal word satisfies

    R_out,R_in >= max(0,2*binomial(k,s)-N).               (2.1)

There is no division by s. The proof jointly charges the two target
families, rather than bounding all marked targets independently of the
old targets at shared endpoints.

For an odd target dimension 2r+1, put W_old=binomial(2r,r). Its middle
width satisfies

    W(2r+1)=2W_old-Cat_r.

At the exact target length N=B(2r+1)=W(2r+1)+d_(2r+1), (2.1) becomes

    R_out,R_in >= max(0,Cat_r-d_(2r+1)).                 (2.2)

In particular the stated exact arithmetic is

    at17: 2*12870-24313=1427 exits and1427 entrances;
    at19: 2*48620-92381=4859 exits and4859 entrances.     (2.3)

These bounds do not require equality in the preceding dimension. The
number of maximal marked runs is at least the bound in (2.1), and one
more if either endpoint of the full word is marked, by the standard
entrance/exit endpoint correction. The total number of tag transitions
is at least twice the bound. This is a necessary chronology condition,
not a proof that such a word cannot exist.

## 3. Stronger coupling with unmarked-run starts

Let M be the number of unmarked letters, R the total number of unmarked
runs, and H_s the number of those runs whose first literal letter has
rank exactly s. The run-start endpoint-loss argument gives

    R-H_s <= M-W_s.                                    (3.1)

Indeed an unmarked run's first endpoint exposes no old rank-s target
unless its literal has that rank, and every other endpoint can expose
at most one distinct target. This argument is proved in
`scratch/EXACT_INTERLEAVED_LIFT_RUN_START_BUDGET_AND_FIXED_TRACE_CUT_CORES_20260909.md`.

Since R>=R_out and (2.1) gives R_out>=2W_s-N, combination with (3.1)
gives the stronger bound

    H_s >= max(0,3W_s-N-M).                              (3.2)

The identical inequality holds for rank-s unmarked-run END letters by
reversal. At optimal19 length92381, with M=48623 unmarked letters,

    H_9 >=3*48620-92381-48623=4856.                      (3.3)

This improves the earlier joint boundary-charge lower bound4835 in the
cited run-start note. If the unmarked trace has NO rank-nine literal,
then H_9=0 and (3.2) forces

    M>=3*48620-92381=53479,
    M-48623>=4856.                                     (3.4)

Thus the earlier605 extra-unmarked-letter condition remains a valid
weaker estimate but is superseded by4856 in this restricted no-rank-nine
family. These bounds constrain the unmarked trace, not the entire new
word's excess above B(19). Changing its literal inventory is allowed.

## 4. Consequence for the fixed uncuttable18 trace

If a separately certified old trace cannot be split by an internal
marked insertion while preserving its old targets, every resulting
superword has at most one exit and at most one entrance. Equation (2.1)
then forces

    N>=2W_s-1.                                        (4.1)

For the supplied exact18 trace, whose cut-rigidity proof and checker are
recorded in the cited cut-core note, s=9 gives

    N>=2*48620-1=97239.                                 (4.2)

This improves the previously recorded97234 bound for that fixed-trace
insertion architecture by five. It does not claim97239 is attainable,
nor is it a lower bound on unrestricted nu(19). If the permitted
architecture has zero exits or entrances, the appropriate orientation
of (2.1) gives the still stronger N>=2W_s.

## 5. Prior-result and novelty audit

The shared-endpoint overlap step is already present in
`TWO_ANTICHAIN_ENDPOINT_FOREST.md`, Section 2, and independently audited
in its companion audit. Specializing its two antichains to old rank-s
targets and marked rank-(s+1) targets makes their cross-comparability
edges exactly the pairs D,D+z. The additional step used here is the
injection of shared RIGHT endpoints into unmarked runs via (1.4), with
the left-endpoint analogue under reversal.

`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Sections 8–9, already
contains the NUMBERS1427 and4859 as the deficits D=2W-N. That earlier
argument feeds D into s*(binomial(q,2)+3q)>=D, yielding much smaller run
counts; it does not state R_out>=D. The later entrance/exit note gives
the179/541 bounds by a different marked-target-only charge. The paired
bound therefore strengthens these cited retained run estimates; the
deficit numbers themselves are not new computations.

The bounded source search also located the earlier fixed-K16 internal-cut
obstruction in
`MATH_THEOREM_K17_SATURATED_COORDINATE_ENDPOINT_SPLIT_CEGAR_20260731.md`,
Sections 2–3. The new exact18 cut-rigidity instance should be attributed
as another application, not as the first general occupied-cut criterion.
No claim of priority over the external mathematical literature is made.

## 6. Executed diagnostic, provenance, and status

The proof-purpose checker
`scratch/verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py`
was read in full by root and independently by `exact_equality_structure`
before root authorized exactly one h100 execution. The source review is
`scratch/PAIRED_ENDPOINT_RUN_CHECKER_INDEPENDENT_PREEXECUTION_AUDIT_20260909.md`.
The single run completed PASS in3.6019seconds under30CPU45wall1GiB limits.
There was no retry, scope change, construction search or word edit.

It exhausted137256 words on the seven nonempty three-coordinate letters
through length six, in both endpoint orientations. Exact counts:

    1647072 family/orientation checks;
    227130 shared-endpoint events;
    454260 direct literal shared-witness replays.

The actual optimal17 literal has exits and entrances each ranging
2231–2232 over its17 coordinates. In the actual optimal18 literal, old
coordinates0–16 have exits4462–4463 and entrances4462–4464; coordinate17
has zero exits and one entrance. All per-rank necessary inequalities and
the displayed1427/4859/4856/53479/4835/97239 arithmetic passed. This input
phase inspected only run/rank statistics; it did not reverify full-cube
coverage of those previously hash-certified literals.

The code snapshot, exact report, execution log and hashes are preserved in
`scratch/paired_endpoint_run_diagnostic_20260909/`, including
`PROVENANCE.md`. The report SHA-256 is

    2fdc338e54cff94664ffd07058eb7714fc8aa8f2e8bd424b497b7af930da3a67.

All processes have exited. The theorem, its coupling, and its scoped
consequences are established by the pure proofs above; enumeration is
diagnostic rather than a premise. Exact all-dimensional attainment remains
open, with required interleaving quantified at the stronger Catalan scale.
