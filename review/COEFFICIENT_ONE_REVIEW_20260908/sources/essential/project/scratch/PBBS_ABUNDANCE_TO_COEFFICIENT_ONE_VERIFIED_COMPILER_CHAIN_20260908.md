# Exposed feasibility abundance suffices for coefficient one

2026-09-08. Cover-selectors independent goal-chain audit. Pure proof;
no computation. The deterministic compiler, its all-target support,
the physical packing interface, exact tail boundaries, and diagonal
quantifiers have been checked against the sources listed below.
Root integration audit passed, including the residence cutoff, exterior
tail boundary, slow diagonal, and even-dimensional lift. The abundance
hypothesis remains open.

## 1. Exact sufficient hypothesis and conclusion

Put R=sqrt(r), W_r=binom(2r+1,r)=(2r+1)Cat_r. For fixed c>0,
let G_c be ALL physical births with lifetime T<=floor(cR). A trace
has T+2 consecutive projected transition edges. Let P_c(r) be the
largest number of edge-disjoint traces in G_c.

The following implication is complete:

    For every fixed c>0, P_c(r)=o_c(W_r/R)
      ==> nu(k)=(1+o(1)) binom(k,floor(k/2)).          (1)

In particular, the sufficient exposed-environment hypothesis is:

    For every fixed c>0, there is a FIXED finite C(c)>=c
    such that J_(c->C(c))(E_2) tends to infinity in probability
    under the ACTUAL base-c incidence-environment law.             (2)

Here J is exactly the feasible-phase count in
PBBS_EXPOSED_PHASE_FEASIBILITY_RECIPROCAL_REDUCTION_20260908.md,
including the physical lifetime and sampled-edge overlap thresholds.
It is not a count of arbitrary recurrent labels or unweighted Dyck roots.
The special choice C(c)=c suffices. Only positive integer c is needed
for the final diagonal.

The current J-reduction and (1) leave no additional all-target,
simultaneous-depth, owner, frame, tail-interface, or parity compatibility
theorem to prove. They do NOT prove (2).

## 2. From J to the full physical packing hypothesis

For fixed c<=C, retain F_c={GOOD,Z_(0,0)=0,T<=floor(cR)} and its
occupied union U_c. Write K_C for the actual partner congestion from F_C,
and mu_c,mu_C for normalized raw incidence masses. The accepted results give

    mu_c=Theta_c(1),   mu_C=O_C(1),
    (|U_c|/W_r)^2 <= mu_C mu_c E_inc,c[1/K_C].       (3)

Under the same actual E_2 marginal, J-divergence is equivalent to
divergence of the virtual-phase count N and the eligible DISTINCT
original-label count k. This follows from the exact finite composition
mean/variance bound at every fixed positive height truncation, followed
by removal of the small-height sector. The limit order is r->infinity
first, then the height cutoff epsilon->0. No fresh law for E_2 is used.
The top-row fibre gives E[1/K_C|profile,rows>=1,j]<=2/(k+1).
Thus (2) implies that the expectation in (3) tends to zero.

Discarded top-gap/BAD traces have normalized raw incidence O_c(1/r),
so their occupied union has that same upper bound. Consequently

    |U_(G_c)|/W_r = o_c(1).                          (4)

For ANY retained short family F, the accepted small-height theorem and
the deterministic edge-capacity split give, for fixed 0<epsilon<=1,

    R P(F)/W_r <= C_c exp(-b_c/epsilon^2)
                    + |U_F|/(epsilon W_r).          (5)

Indeed low-height packed traces are bounded by their number of births,
whose normalized count is at most C_c exp(-b_c/epsilon^2)/R; every other
trace has at least epsilon R distinct edges. Physical cycle lengths
are at least 2r+1, so the short traces do not wrap. Apply (5) to ALL G_c,
send r to infinity and then epsilon to zero, to obtain (1)'s hypothesis.
There is no quantitative logarithmic convergence rate to establish.

This is a full physical-factor statement. No quotient-to-deck estimate,
separate winding case, clean-triangle partner condition, or low-budget
recombination is needed for this version of the chain.

## 3. All targets supplied by the unmodified PBBS owner cycles

Let A_i be the oriented rank-r PBBS states and X_i=[2r+1]\A_i.
The X_i, traversed by step two, are rank-(r+1) Johnson owner cycles;
their lengths sum to W_r and their number is at most Cat_r.

The global-maximum unmatched-mark corridor theorem, Section 21.2 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, says that for every
q>=0 and every rank-(r-q) target S, some oriented q-edge step-two
PBBS path satisfies S=intersection_(t=0)^q A_(i+2t). The q=0 case is
the complete PBBS vertex factor. This is support for EVERY target;
no lower multiplicity estimate beyond one is needed.

The lower/upper conversion for the actual X owner cycles is exact:

    X_i intersect X_(i+2) = A_(i+1),
    intersection_(t=0)^q X_(i+2t)
       = intersection_(t=0)^(q-1) A_(i+2t+1)  (q>=1),
    union_(t=0)^q X_(i+2t)
       = complement(intersection_(t=0)^q A_(i+2t)).   (6)

The first identity follows because A_(i+1) is disjoint from both
adjacent PBBS states and has their complement-intersection's rank r.
The others follow by associativity and complementation.
Therefore intended windows of at most H+1 owners include every target
of every rank in

    [r+1-H, r+1+H].                                 (7)

Correct lower windows have their Johnson floor rank. Oversized lower
intersections are unnecessary, so the staircase's floor-correctness
restriction loses no required target. All needed occurrences can be
selected before the cuts; the compiler restores any selected crossing
occurrence, simultaneously over all depths through H.

## 4. Literal main word and exact physical cut ledger

The indexing guard is

    positive residence length = T+1,
    residence trace edge count = T+2,
    nu_H(P_r) = P({T<=H-1}).                         (8)

Assume 2H<=r+1. On an active owner cycle choose a transversal of all
positive residences of length at most H. Circular interval packing gives
at most 2 nu_H cuts on active cycles. Once cut, each internal positive
coordinate run has at least H+1 owners. Endpoint-capped erosion then
uses v+H letters on a path of v owners, retaining every intended
intersection/union whose owner window stays inside that path.

At each cut the extent-point Pareto staircase has 2H-1 letters and
represents every floor-correct crossing lower intersection. Its proof
uses the first-departure injection to exclude a strictly southwest
extent point, and then the east-before-south rectangle-interception
identity. The literal 2H-owner collar represents every crossing upper
union. Thus the exact appended chart length is 4H-1, and including
endpoint erosion the charge is 5H-1 per cut. Charts use ORIGINAL cyclic
owners, so nearby cuts and windows crossing several cuts are harmless.
Every staircase letter has at least r+2-2H>=1 coordinates.

An inactive cycle uses its cyclic erosion word with a 2H collar.
All chosen target witnesses stay inside a path word or a cut chart;
concatenation cannot destroy them. Hence

    L_central(r,H)
       <= W_r + 2H Cat_r + 2(5H-1) nu_H(P_r).       (9)

The W_r term counts every original owner exactly once in the baseline.
The second term covers ALL inactive-cycle collars, and the third covers
ALL active-path initialization plus crossing-target repair. There is no
unrecorded multiplicity, component, or concatenation charge.

Equation (9) is the unconditional complete compiler of Sections 22 and
24. The older sufficient O_c(Cat_r) estimate is stronger than required:
the actual critical gate is nu_H=o_c(Cat_r sqrt(r)), equivalently
o_c(W_r/sqrt(r)). This is precisely Theorem 24.4, not merely the older
Catalan-order Theorem 24.3.

## 5. Exact all-rank exterior and zero interface charge

For s>=0 let

    A_r(a)=binom(r,a)-binom(r,a-1),
    w_r(0)=r,   w_r(a)=r-2a+1 (a>0),
    C_r(t)=0 (t<0),
           binom(r,min(t,floor(r/2))) (t>=0),
    L_r(s)=2 sum_(a=0)^floor(r/2) A_r(a)w_r(a)C_r(s-a).

The factor-blind product-SCD theorem constructs a word of exact length
L_r(s) on 2r coordinates covering both tails |S|<=s and |S|>=2r-s.
Its trimmed one-coordinate lift has length 2L_r(s) and covers every
odd-dimensional rank outside [r-h,r+h+1] when s=r-h-1.

Use h=H-1, NOT h=H, to match (7). The odd tail costs 2L_r(r-H)
and covers ranks <=r-H and >=r+H+1. Together with (7) this covers
every nonempty target; there is overlap at rank r+H+1. In particular
there is no uncharged missing rank r-H.

The uniform proved estimate is

    2L_r(r-H)/W_r
       <= 2(r+1)/(2r+1) C_0 exp(-(H-1)^2/(8r)).      (10)

Each product-SCD witness remains internal to its own chain-pair gadget.
Appending the tail to the central word costs exactly its length and
ZERO extra seam letters. Neither a shared frame nor a common PBBS
endpoint is required. Thus the explicit finite all-target ledger is

    nu(2r+1) <= W_r + 2H Cat_r
                   + 2(5H-1)P_(H-1)(r)
                   + 2L_r(r-H),                    (11)

where P_t means the packing of all births with integer lifetime T<=t.

## 6. Slow diagonal and opposite parity

For each positive integer j set H_j(r)=floor(j sqrt(r))+1 and

    epsilon_j(r)=sqrt(r) P_j(r)/W_r ->0,

where here P_j is the fixed-Gaussian family of Section 1. By (8),
nu_(H_j)(P_r)=P_j(r). Choose strictly increasing finite thresholds M_j
such that for EVERY r>=M_j,

    epsilon_j(r) <= 1/[10j(j+1)],
    2H_j(r)/(2r+1) <= 1/j,
    2H_j(r)<=r+1,   r>=j^6.

This is possible independently for each fixed j. Let j(r)=j on
[M_j,M_(j+1)), and H=H_(j(r))(r). Then j(r)->infinity, H=o(r), and
the two excesses in (9), divided by W_r, are each at most 1/j(r):
the packing coefficient is at most 10(j+1)epsilon_j. The tail in
(10) tends to zero since (H-1)/sqrt(r)=j(r)+O(1/sqrt(r))->infinity.
This proves nu(2r+1)<=W_r(1+o(1)). Fixed-c hypotheses are used only
beyond their individual thresholds; no uniform growing-c theorem is used.

For any complete nonzero word Q_1,...,Q_N on 2r+1 coordinates, the
trimmed lift

    Q_1,...,Q_N, {z}, Q_1 union {z},...,Q_(N-1) union {z}

has 2N letters and covers the complete (2r+2)-cube. Witnesses ending
at Q_N use their old suffix followed by {z}; other witnesses use the
last block. Since binom(2r+2,r+1)=2W_r exactly, the leading coefficient
is unchanged. The antichain lower bound supplies the matching 1-o(1)
lower estimate in both parities.

## 7. Sources and precise remaining boundary

The compiler audit reads Sections 21-27 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md; the full standalone
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md; the corrected
critical-scale argument in
MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md; and Sections
1-2 and 11-12 of
MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md.
The later sub-Gaussian/tail caveat in
MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md is
respected: a fixed-j tail is NOT o(W_r); only the slow j->infinity
diagonal makes it negligible.

The current probability interface uses the exact J-reciprocal note,
PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md,
PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md, and
PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md in this scratch directory.

There is no remaining compiler compatibility gap conditional on (2).
There remains the substantive, unproved assertion that J diverges under
the ACTUAL incidence-biased depth-two environment at every fixed base
cutoff, or for a fixed larger partner cutoff. This is a sufficient
route to coefficient one, not a necessary condition for arbitrary
literal words and not an unconditional construction.
