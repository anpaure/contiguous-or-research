# The exposed phase-feasibility count controls the actual reciprocal

2026-09-08. Pure proof; no computation. Root proof review and independent
direct-route full audit passed, including the exact finite-fibre proof and
the final definition and limit statements.
This eliminates random
row-one marks from a qualitative overlap gate, but does not prove that
the resulting exposed-environment count diverges.

## 1. Actual base law and the commuted two-row kernel

Fix 0<c<=C<infinity, let R=sqrt(r), and set H_c=floor(cR), H_C=floor(CR).
Sample an actual incidence of F_c={GOOD,T<=H_c,Z_(0,0)=0}. Restrict the
BASE to its safe zero triangle through depth two. This removes o(1)
incidence probability. Expose

    E_2=(full original profile, all rows s>=2, sampled offset j).

Conditional on every feasible E_2, the accepted exact fibre makes row one
a uniform composition of ell=ell_1 into P=p_1-2 free slots; its original
slots 0,-1 are forced to zero. Row zero has its independent corresponding
free composition and forced zero slot. E_2 retains its actual incidence
law. No partner is required to have a shifted zero triangle.

Use the independently checked commuted kernel on the one exposed D_2
trajectory. For each physical phase

    d in D_j={j-H_C-1,...,j},

put b_d=lambda_2(2d), let u_d be its first subsequent selection time of
label b_d-1, and define

    N_d(t)=#{u_d<v<=2d+2t+1 : lambda_2(v)=b_d-2},
    L_d=max(h,j-d-1,1),
    I_d=[floor(N_d(L_d-1)/2), floor(N_d(H_C)/2)-1].   (1)

Counts are zero if their upper endpoint precedes u_d. The interval is
empty if L_d>H_C or its endpoints are reversed. All labels are original
cyclic labels. All quantities in (1) are E_2-measurable.

Write w_d=Z_(1,b_d)+Z_(1,b_d-1). The virtual top-zero birth d is short
enough and covers the sampled edge exactly when w_d belongs to I_d.
Indeed its depth-two word is

    C T^(2Z_(1,b_d)) C T^(2Z_(1,b_d-1)+1),

whose endpoint, by adjacent-selection alternation, equals that of
C^2 T^(2w_d+1). Its endpoint is the (2w_d+2)-nd selection of b_d-2
STRICTLY AFTER u_d. Safe forward/reverse clock grouping gives precisely
(1), with both lifetime and sampled-edge overlap thresholds retained.

## 2. The deterministic count J

Call d feasible if some nonnegative values at its FREE marked slots,
together with zero at any forced slots, have sum in I_d and total at most
ell, so that they extend to the full row-one composition. Let

    J(E_2)=#{feasible d},
    X_d=1{w_d in I_d},      N_virt=sum_(d in D_j) X_d. (2)

If both slots are forced, feasibility requires 0 in I_d. Otherwise any
nonnegative integer in I_d is an admissible sum once ell exceeds the
fixed bound below. The base d=0 is feasible and successful for EVERY
completion of the free row, because its two row-one marks are forced
zero and E_2 is feasible. Consequently

    1<=N_virt<=J<=H_C+2.                              (3)

Define J by (1)-(2) on ALL safe feasible E_2, independently of epsilon.
Only on the o(1)-probability safe/profile exceptions may it be assigned
an arbitrary value. In particular its definition is not changed on a
fixed-epsilon low-height sector.

Fix epsilon>0 before sending r to infinity. Work on E_2-measurable
profiles satisfying h>=epsilon R, the safe circumferences p_0,p_1>2H_C+2,
P comparable to r, and ell/P in a fixed positive compact interval.
The latter profile conditions have actual incidence probability 1-o(1)
at fixed c,C; low height is treated in Section 6.

## 3. Bounded allowed sums and bounded phase reuse

Every D_2 same-label return has length at least

    g=2(h-2)+1=2h-3,

at every reached phase, by height invariance. If w>=0 is allowed by I_d,
the word C^2 T^(2w+1) finishes within 2H_C+1 physical steps. Its T clocks
alone therefore give (2w+1)g<=2H_C+1. For sufficiently large r this bounds
every allowed sum by a fixed integer B_*=B_(C,epsilon).

The tested physical starting times span 2(H_C+1) steps. A fixed label b
can occur at no more than

    1+floor(2(H_C+1)/g) <= K_*=K_(C,epsilon)          (4)

of them. The sharper even-time spacing is unnecessary. A free mark i
appears only in phases with b_d=i or b_d=i+1, at most 2K_* phases.
Thus each phase shares a free mark with at most 4K_* other phases.

## 4. Exact conditional mean and covariance bounds

Put q=ell/(ell+P). If t distinct free slots have prescribed nonnegative
values totaling A, stars and bars gives exactly

    Pr(values | E_2)
      =(P-1)_t (ell)_A /(ell+P-1)_(A+t),             (5)

with falling factorials. For t<=4 and A<=4B_*, on the stated compact
profile domain,

    Pr(values | E_2)=(1-q)^t q^A+O_(B_*)(1/P),       (6)

uniformly in labels and allowed values. To check (6), factor P, ell,
and ell+P from the respective bounded numbers of falling-factorial
terms in (5); each remaining factor is 1+O(1/P).

Each feasible phase admits an assignment of its at most two free slots
with total at most B_*. The corresponding independent geometric mass
is bounded below by a positive constant, uniformly for q in its compact
interval. Equation (6) therefore gives

    E[X_d | E_2]>=p_*>0

for all feasible d and sufficiently large r. If both slots are forced,
X_d=1 and the same bound holds. Hence

    E[N_virt | E_2]>=p_* J.                          (7)

For phases with disjoint FREE marked-slot sets, sum (6) over the bounded
possible assignments defining their two events. The independent geometric
reference events are independent, so

    |Cov(X_d,X_e | E_2)|<=K'/P.                      (8)

This is an exact-fibre bound; actual disjoint-slot events have not been
declared independent. For overlapping supports use |Cov|<=1 and (4).
There are at most 4K_*J ordered overlapping pairs. Since J<=H_C+2<=P
for sufficiently large r, summing all covariances gives

    Var(N_virt | E_2)
       <=(1+4K_*)J+K'J^2/P <=D_* J.                 (9)

The constants p_*,D_* depend on fixed c,C,epsilon and the chosen compact
profile bounds, not on r or the particular feasible E_2.

## 5. Uniform reciprocal comparison and distinct original labels

The deterministic upper bound N_virt<=J gives a reciprocal lower bound.
For the upper bound, split at N_virt>=p_*J/2 and apply Chebyshev using
(7)-(9). Since N_virt>=1, this proves

    1/J <= E[1/N_virt | E_2]
       <= [2/p_*+4D_*/p_*^2]/J.                     (10)

The exact same-label virtual endpoint bracket from the two-row theorem
gives

    k_(c->C)+1 <= N_virt <= k_(c->C)+2,              (11)

where k_(c->C) counts distinct eligible nonzero ORIGINAL level-zero
particle labels. The base label contributes at least one phase, and only
the current label at the sampled edge can contribute an additional phase.
Thus no separate reconstruction of those labels is needed to use (10).

Conditional on row one as well, the accepted top-row hypergeometric
argument gives a reciprocal comparable to 1/(k_(c->C)+1) for the actual
partner congestion K_C. Combining it with (10)-(11) yields constants
0<a_*<=b_*<infinity such that

    a_*/J(E_2) <= E_inc,c[1/K_C | E_2]
                          <= b_*/J(E_2).           (12)

All expectations are under the actual base-c incidence fibre. In
particular (10)-(12) have no additive total-variation approximation error.

## 6. Limit order and the remaining exposed-environment gate

For every fixed epsilon, (3), (7), and (9) show that N_virt tends to
infinity in actual incidence probability on h>=epsilon R if and only
if J does. For example, when J is large, Chebyshev gives
Pr(N_virt<p_*J/2 | E_2)<=4D_*/(p_*^2 J); conversely N_virt<=J.
Equations (10)-(12) give the same conclusion through reciprocals and
distinct eligible labels.

For clarity, the needed small-height bound follows directly from Section 6
of `PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md`. Under actual
base-c incidence, its profile variable A has a subGaussian upper tail and
L=floor(kappa_c R/A). On L>=2, h>2L>=kappa_c R/A. Hence h<epsilon R
forces A>kappa_c/epsilon there. On L<2 one has A>kappa_c R/2, which
exceeds kappa_c/(2epsilon) once R>1/epsilon. Consequently

    limsup_(r->infinity) Pr_inc,c(h<epsilon R)
                              <=C_c exp(-b_c/epsilon^2).

All other safe/profile exceptions above are o(1) for fixed epsilon.
Thus take r to infinity FIRST at fixed epsilon, then epsilon to zero.
J still uses (1)-(2) on the low-height sector; epsilon is only a proof
truncation. With any harmless convention on the o(1) safe/profile
exceptions, global
divergence of J, N_virt, and k_(c->C) are equivalent under the actual
base-c incidence law.

When C=c, the accepted top-zero support identity and mu_c=Theta_c(1)
therefore make |U_c|=o(W) equivalent to J(E_2) tending to infinity.
For fixed C>=c, J-divergence suffices by the accepted cross-cutoff support
inequality. Adding the already negligible discarded top-gap sector and
using the occupied-support-to-packing theorem gives the stated Gaussian-
short packing consequence IF this exposed-environment gate is proved.

No statement here shows that J usually grows. Its remaining randomness
is entirely the ACTUAL profile/depth-two trajectory/offset environment,
including both count thresholds in (1). No unweighted deeper law,
physical recurrence, complete repair compiler, or coefficient-one theorem
is inferred.
