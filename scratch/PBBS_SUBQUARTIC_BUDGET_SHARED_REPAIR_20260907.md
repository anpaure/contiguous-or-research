# PBBS repair through every subquartic interruption budget

2026-09-07. Root synthesis; pure proof, no computation.
Status: complete written proof independently audited PASS. Full coefficient
one remains open. The zero-budget and uniform positive-census inputs were
also independently audited and reread by root.

A stronger later cutoff of order sqrt(r/log r), using a new full-history
linear height gap, is proved in PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md.
The uniform weighted estimate here remains a separate valid result.

Let r be the Dyck semilength, W=(2r+1)Cat_r the number of edges in the
full physical PBBS factor, and B=T-h the interruption budget of a birth.
Here h is its invariant height, T includes the consuming update, its
positive residence has T+1 owners, and its full repair trace has T+2
edges. All statements below concern that same full physical factor.

For every prescribed integer sequence J_r>=1 with J_r=o(r^(1/4)), there
is a finite procedure, given r and J_r, choosing an integer H_r such that

    H_r/sqrt(r) -> infinity,       H_r=o(r),

and the family of ALL repair traces with

    B<=J_r

has all of the following properties:

1. Its occupied edge union has size o(W).
2. The maximum edge-disjoint packing of ALL traces with B<=J_r has size
   o(W/sqrt(r)), even without the lifetime cutoff.
3. ALL traces with B<=J_r have a constructed physical transversal whose
   O(H_r)-per-cut charge is o(W), including the original cycle openings.
4. The number of distinct owners belonging to these runs is o(W).

No lifetime or height cutoff is needed for these four conclusions.
Thus the remaining packing problem can be restricted to budgets B>J_r,
with J_r allowed to diverge almost as r^(1/4). This does
NOT control those remaining runs. It also does not bound their actual
target losses or prove a full-cube word theorem.

## 1. The two proof inputs and their exact scopes

The all-height zero-budget theorem in
`PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md` gives

    nu_0(r)=o(W/sqrt(r)),        |E_0(r)|=o(W),         (1)

where nu_0 is the maximum edge-disjoint packing of ALL B=0 traces,
without a lifetime cutoff, and E_0 is their occupied edge union. Its
proof uses the original-forest multipoint product, a proper Palm renewal
law, the reciprocal incidence identity, and uniform low/high tails.

The uniform positive-budget census, proved in task05's
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_growing_budget_uniform_bound.md`,
states, with an absolute constant C, that for every r,J>=1,

    #{D in Dyck_r : 0<B(D)<=J}
       <= C(J+1)^2 4^r/r^(5/2).                       (2)

Its first-packet witness and coefficient transfer are about original
roots, not independent reached states. Catalan normalization and the
exact physical deck multiplicity 2r+1 give

    N_+(r,J):=#{physical births : 0<B<=J}
       <= C'(J+1)^2 W/r.                              (3)

The constant C' is absolute after adjusting finitely many small r.
All later interruption histories are included in (2)-(3); these are not
estimates only for one RS packet or a fixed number of interruptions.
No new probabilistic independence assumption is used below.

There are at most Cat_r=W/(2r+1) physical cycles. Circular interval
transversals for the zero-budget traces can be chosen using at most
nu_0(r)+Cat_r cuts: open each cycle and use the usual interval packing/
transversal equality on intervals not already met by its opening.

## 2. The positive census also gives a uniform LENGTH-weighted bound

The height-resolved proof of (2) supplies more than the summed count.
Set s=2 floor((J-1)/2), so s+1<=J and J<=s+2. For h>2s, h>=2,
equation (16) of the cited uniform-bound source, after Catalan
normalization, states

    Pr(h(D)=h, 0<B(D)<=J)
       <=C(J+1)^2 r^(3/2)(h+2)^(-6)
                    exp[-r/(2(h+2)^2)].              (W1)

Here T+2=h+B+2<=h+J+2<=2(h+2). The nonnegative unimodal kernel
x^(-5)exp[-r/(2x^2)] has integral O(r^(-2)) and maximum O(r^(-5/2)).
Bounding its sum by its integral plus twice its maximum therefore gives

    E[(T+2)1_{0<B<=J, h>2s, h>=2}]
       <=C(J+1)^2/sqrt(r).                            (W2)

For h<=2s, equation (19) of the same source gives, after normalization,

    Pr(h<=2s)<=C exp[-r/(16(s+1)^2)].

The sum is empty if s=0. Within the positive-budget event here,
T+2<=2s+J+2<=3(J+1). Write u=r/(16(s+1)^2). Since sqrt(u)exp(-u) is
bounded, this part of the expectation is at most
C(J+1)(s+1)/sqrt(r)<=C(J+1)^2/sqrt(r).

Height one can be handled separately without any asymptotic exception:
there is one root (10)^r, with T=r, and
(r+2)/Cat_r<=C/sqrt(r) for an absolute C (Catalan growth dominates
every fixed polynomial). This also covers any overlap with the above
upper bounds harmlessly. We have proved, uniformly for EVERY r,J>=1,

    E_Dyck_r[(T+2)1_{0<B<=J}]
       <=C(J+1)^2/sqrt(r).                            (W3)

The exact physical deck dictionary converts this expectation into total
trace incidence divided by W. Thus when J_r=o(r^(1/4)), the total
incidence of ALL positive B<=J_r traces is o(W), without bounding T.
Their occupied edge union is at most that incidence. This new weighted
deduction is separately audited; it uses no lifetime-tail independence.

For avoidance of doubt, (W3) concerns POSITIVE budgets only. Adding the
zero-budget class does not make raw summed incidence o(W): that class
still has its established order-W raw incidence, shared on o(W) edges.

## 3. A finite common cutoff

Enumerate the finite physical factor and its zero-budget traces and
compute nu_0(r), by any finite interval-packing algorithm. Given J=J_r,
take c_r to be the largest positive integer c satisfying

    c^4 r nu_0(r)^2 <= W^2,
    c^4 (J+1)^4 <= r,
    c^8 <= r.                                         (4)

Set c_r=1 if the set is empty, and define

    H_r=isqrt(c_r^2 r)=floor(c_r sqrt(r)).              (5)

This is a finite procedure on integer data. No efficient running time
is asserted. For a noncomputable prescribed sequence J_r, the claim is
only that this same finite procedure works when its value J_r is supplied.

Put delta_r=sqrt(r)nu_0(r)/W. Equation (1) gives delta_r->0, and
J_r=o(r^(1/4)) gives (J_r+1)^2/sqrt(r)->0. Every fixed positive integer
c therefore eventually satisfies all three inequalities (4). Hence
c_r->infinity, and the fallback occurs only finitely often.

For sufficiently large r the first two inequalities respectively give

    c_r^2 delta_r<=1,
    c_r^2 (J_r+1)^2/sqrt(r)<=1.

Consequently

    H_r nu_0(r)/W <=1/c_r ->0,
    H_r (J_r+1)^2/r <=1/c_r ->0,                       (6)

while the third gives H_r<=r^(5/8)=o(r). Also
H_r/sqrt(r)>=c_r-1/sqrt(r)->infinity. The exponent 5/8 is a bound on
the chosen cutoff, not a claim that setting H_r=r^(5/8) always works.

## 4. Occupied edges, packing, and an actual transversal

Equation (W3) gives directly

    |union of ALL positive-budget traces with B<=J_r|
       <=C(J_r+1)^2 W/sqrt(r)=o(W).                    (7)

Adding the entire zero-budget support from (1) proves the occupied-edge
claim. There is no inference from rarity alone: (W3) pays the full
length of every positive trace, including long ones.

Partition any edge-disjoint family with B<=J_r into zero- and positive-
budget runs, without imposing any lifetime cutoff.
Its size is at most

    nu_0(r)+N_+(r,J_r)
       <=nu_0(r)+C'(J_r+1)^2 W/r
       =o(W/sqrt(r)).                                 (8)

For a constructive transversal, take a zero-budget transversal as above
and add the birth edge of EACH positive-budget run with B<=J_r, whether
or not it is short. A birth edge
belongs to its own repair trace, so this is a literal hitting set. Its
size is at most

    nu_0(r)+Cat_r+N_+(r,J_r).                          (9)

Multiplying (9) by H_r, the first term is o(W) by (6), the second is
o(W) because H_r Cat_r/W=H_r/(2r+1)->0, and the third is o(W) by
(3) and (6). Thus any fixed-constant O(H_r)-per-cut compiler charge for
this supplied transversal is o(W).

If a run is born at edge e_s, its owners are
X_(s+1),...,X_(s+T+1), and its trace contains e_s,...,e_(s+T+1).
Sending an affected owner X_i to its preceding edge e_(i-1) is globally
injective into the occupied edge union. This proves the distinct-owner
claim; it is not a bound on owner-coordinate or failed-target incidences.

## 5. What the residual problem now is

Examples of admissible cutoffs are J_r=floor(r^(1/8)) and, eventually,
J_r=floor(r^(1/4)/log r). The construction (4)-(5), rather than an
unproved rate for zero-budget clustering, chooses the compatible H_r.

The remaining unhandled sector is B>J_r. For the SAME H_r, its short
runs relevant to the band compiler satisfy

    T+1<=H_r,       B>J_r.                             (10)

In particular these residual runs have h<=H_r-J_r-2 and at least
ceil((J_r+1)/2) interruption events, since B=2rho+sigma. These are only
deterministic necessary conditions, not distributional estimates.

Their height, birth density, physical overlap, and actual target costs
remain to be controlled. The input census only gives O(J^2/r), which
does not make an O(H)-per-birth charge negligible at budgets of order
sqrt(r) and H/sqrt(r)->infinity. The proof above therefore narrows the
unresolved sector but does not close the PBBS compiler or the conjecture.

The newly proved bounded-height exclusion for 0<B<=3 supplies an even
stronger exponential estimate on those few budgets. It is compatible
with this synthesis, but is not needed for (1)-(10).
