# All Gaussian-short overlap reduces to zero top gaps, with no shifted triangle

2026-09-08. Root pure-proof synthesis. Complete independent root-helper
and task05 full-file audits PASS through Section5; Section6 also passes
an independent full root-helper audit. No computation. This is a
reduction, NOT a proof of the eligible-label abundance condition.

The new observation is to use the accepted early-triangle estimate at
depth S=1, instead of imposing a growing clean triangle and a residual
budget floor. This retains almost all ALL-short raw incidence, so its
normalizer is bounded above and below. Partners need no deeper-triangle
test. The remaining condition is ordinary divergence in probability of
one exactly defined number of distinct labels.

## 1. Inputs and physical normalization

Fix c>0. Let r tend to infinity, R=sqrt(r), n=2r+1,
H=floor(cR), and W=n Cat_r. A uniform original Dyck root D has
pruning profile (r_s), height h, and lifetime T including consumption.
Its physical repair trace has T+2 consecutive edges; T>=h. The full
physical PBBS factor has W edges, and each cycle has period at least n.
For sufficiently large r, H<r and H+2<n, so every short repair has
distinct edges. Physical births, not quotient-root shapes, are counted.

The accepted root theorem
PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md, Sections9-10, gives

    mu_H=E[(T+2)1_{T<=H}]=Theta_c(1),
    E[(T+2)1_{T<=H,Z_(0,0)>0}]=O_c(1/r).             (1)

The second statement is exactly its S=1 case: the triangle contains
only the nonnegative original entry Z_(0,0). No deeper row is tested.

Use GOOD from PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md. It is
invariant under the PBBS dynamics, depends only on the original profile,
and, with p=2r_1+1 and ell=r-2r_1+r_2, gives uniformly

    p/n=1/2+o(1),  ell/p=1/3+o(1),
    E[(T+2)1_{T<=H,BAD}]<=2/(n+1)^9.                 (2)

Let G be all births with T<=H and retain just

    F0={GOOD, T<=H, Z_(0,0)=0}.                      (3)

There is NO positive-budget restriction, small-height removal, or
deeper-triangle predicate in (3). Height one has T=r and is automatically
absent because H<r. Thus each positive-mass retained profile has h>=2.
Writing mu0=E[(T+2)1_F0], (1)-(2) imply

    delta:=mu_H-mu0=O_c(1/r),   mu0=Theta_c(1).       (4)

If U_G and U0 are the occupied-edge unions, every edge of U_G minus U0
is covered by at least one discarded trace. Counting discarded raw
incidences therefore proves

    0<=|U_G|/W-|U0|/W<=delta.                        (5)

This does not identify the two families' congestions; each congestion
below is consistently that of F0.

## 2. Exact base-incidence environment

The exact original-coordinate kernel and same-particle bound are in
task08's pbbs_original_incidence_window_kernel.md and the root note
PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md. Their physical
phase convention is retained here: tau=phi^2, birth shift d begins
at edge e_d and ends at e_(d+T(tau^d D)+1).

Sample a uniform F0 repair-edge incidence. Its environment is

    E=(profile, y, j),

where y comprises ALL original arrays at levels s>=1 and j is the
sampled edge offset. These data determine the entire signed-time reduced
omitted-site trajectory lambda_1(t), independently of row zero. In
particular lambda_1(0)=0. For every integer d define

    a_d=lambda_1(2d) mod p,
    N_d(t)=#{1<=v<=2t+1:lambda_1(2d+v)=a_d-1 mod p}.

For d in {j-H-1,...,j}, put

    L_d=max(h,j-d-1,1),
    I_d=[floor(N_d(L_d-1)/2),floor(N_d(H)/2)-1].       (6)

The interval is empty if L_d>H or its endpoints are reversed.
The exact kernel states that a short birth d covers e_j precisely
when Z_(0,a_d) belongs to I_d. The h floor uses only the universal
T>=h fact; no extra residual lifetime floor is present.

Every feasible base environment has GOOD profile and 0 in I_0. Set
N=p-1. Conditional on E, the base gap is Z_(0,0)=0 and

    (Z_(0,1),...,Z_(0,p-1))
       is uniform over weak compositions of ell into N parts. (7)

Indeed recording the offset j cancels the lifetime incidence weight.
All feasible original arrays at that fixed offset have the same atom
weight; after fixing Z_(0,0)=0, the only base lifetime/overlap test is
0 in I_0, already measurable from E. No remaining row-zero coordinate
is filtered. More explicitly the environment has mass

    binom(ell+N-1,N-1)/(Cat_r mu0)

when these conditions hold, and mass zero otherwise, with the physical
deck phase marginalized out. This is the ACTUAL incidence law, not the
unweighted deeper-array distribution or a newly sampled reached root.

## 3. Eligible distinct labels and an exact hypergeometric law

Define

    V_i(E)={d in {j-H-1,...,j}:a_d=i and 0 in I_d},
    k0(E)=#{i in {1,...,p-1}:V_i(E) is nonempty}.      (8)

The eligibility tests are exclusively the original signed trajectory
and the two count thresholds in (6). Equivalently 0 in I_d means

    L_d<=H, N_d(L_d-1)<=1, N_d(H)>=2.                (9)

No shifted-triangle test is included. The candidate labels are selected
before examining any remaining top-row gap. Let Y count those k0
eligible nonzero labels whose top-row gap equals zero.

An F0 birth d covers the sampled edge exactly when 0 in I_d and
Z_(0,a_d)=0: GOOD is invariant and no other membership condition exists.
The base contributes one. Every label counted in Y contributes at least
one. The same-particle theorem gives at most one such contribution per
zero-gap label, except that the single current label a_j may contribute
two. Consequently the ACTUAL F0 congestion satisfies pointwise

    1+Y<=K0<=2+Y.                                   (10)

The proof counts distinct labels rather than independently counting
repeated visits to one label. It includes both trace boundary edges.

For ell>=1, stars and bars applied to (7) gives probability
(N-1)_q/(ell+N-1)_q that any q specified slots all vanish. Thus

    Y | E ~ Hypergeom(ell+N-1,N-1,k0).               (11)

These all-subset probabilities determine the indicator-vector law.
For ell=0, Y=k0 deterministically instead. The identity
binom(Q,y)/(y+1)=binom(Q+1,y+1)/(Q+1), followed by Vandermonde, yields

    E[1/(Y+1)|E]
      =(ell+N)/(N(k0+1))
         *[1-binom(ell,k0+1)/binom(ell+N,k0+1)]
      <=(1+ell/N)/(k0+1).                            (12)

The deterministic ell=0 case satisfies the same upper bound. On GOOD,
ell/N->1/3 uniformly, so (10)-(12) imply, for large r,

    1/[2(k0+1)]<=E[1/K0|E]<=2/(k0+1).               (13)

## 4. The exact remaining qualitative condition

Incidence counting within F0 is exact:

    |U0|/W=mu0 E_inc,F0[1/K0].

Together with (5) and (13), this gives the two-sided bounds

    (mu0/2) E_inc,F0[1/(k0+1)]
      <=|U_G|/W
      <=delta+2mu0 E_inc,F0[1/(k0+1)].               (14)

Because delta->0 and mu0 is bounded above AND away from zero, these
statements are equivalent as r tends to infinity at fixed c:

    (i)   |U_G|=o(W);
    (ii)  E_inc,F0[1/(k0+1)]->0;
    (iii) for EVERY FIXED M, Pr_inc,F0(k0<=M)->0.      (15)

For (ii)=>(iii), bound the reciprocal below by1/(M+1) on k0<=M.
For the converse, split its expectation at M, bound by
Pr(k0<=M)+1/(M+1), take r to infinity, then M to infinity.
Thus (iii) is precisely k0 tending to infinity in probability under
the specified actual incidence-environment law, with no quantitative
rate, growing threshold, or unknown vanishing normalizer.

If (15) is proved, the accepted occupied-support-to-packing theorem
PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md gives packing(G)=o(W/R).
In fact, writing v=|U_G|/W, its finite modulus gives

    packing(G)<=C_c (W/R) v sqrt(log(e/v)).

This directly handles all fixed-Gaussian short births, not only the
positive-budget residual. The already proved low-budget and early-
triangle results remain valid and may still help establish (iii), but
they need not be imposed as extra membership tests on partners in (8).

Condition (iii) is STILL UNPROVED. Nothing here supplies enough eligible
labels, establishes a growing-c bound, or completes the remaining word
compiler. The equivalence is to the occupied-support property (i), not
to the full conjecture or to a necessary condition for arbitrary words.

## 5. A useful admissible restriction: all gaps through the safe depth

This additional lemma passes independent root-helper and task05 audits. It removes very large
original gaps from the actual incidence problem, but supplies no bound
on the amplification of small gaps by shifted dynamics.

Use the accepted profile envelope parameter a>=1, A<=3a, and
L=floor(kappa_c R/A). On L>=2 its proved profile bounds are

    (3/4)r/(s+1)<=r_s<=(5/4)r/(s+1), 0<=s<=2L+1,
    h>2L,  L<=R,  Pr(a>1+x)<=C exp(-b x^2).

For each row s<L, monotonicity gives ell_s<=r_s. With p_s=2r_(s+1)+1,

    ell_s/(ell_s+p_s-1)
      <=5(s+2)/[5(s+2)+6(s+1)]<=5/8.                (16)

For a uniform weak composition of ell_s into p_s parts, any specified
slot satisfies

    Pr(Z_(s,i)>=m | profile)
      =(ell_s)_m/(ell_s+p_s-1)_m <=(5/8)^m,          (17)

with value zero if m>ell_s. The ratios decrease at successive factors,
so the inequality holds for every integer m>=1. There are at most
L(2r+1)<=3r^(3/2) slots in the first L rows. Conditional on the profile,
a union bound therefore bounds ANY gap at least m in these rows by
3r^(3/2)(5/8)^m. No across-row independence is needed for this step.

To transfer this bound to F0 incidence, use its actual density
(T+2)1_F0/mu0, bounded by C_c R in view of (4). Also L<2 implies
a>kappa_c R/6, so its newborn probability is at most C_c exp(-b_c r),
and multiplying by C_c R preserves such an exponential bound. Hence

    Pr_inc,F0(L<2 OR some Z_(s,i)>=m with s<L)
      <=C_c r^2(5/8)^m+C_c exp(-b_c r).              (18)

For any fixed D>0, taking

    m=ceil((D+3)log(r+1)/log(8/5))

makes (18) O_(c,D)(r^(-D)). This controls ALL original slots through
the random safe depth, including adaptively selected labels there,
under the actual incidence law. In particular a counterexample
requiring a macroscopic level-one gap lies in a negligible exceptional
set. A [later audited construction] (historical local link not bundled)
uses only logarithmic gaps while making an adjacent virtual lifetime
of order sqrt(r)log(r), with a base lifetime of order sqrt(r), on the
same GOOD profile class. Thus these gap bounds do not imply uniform
one-step Gaussian-scale endpoint stability. That exceptional family's
frequency and k0 divergence remain separate questions.

## 6. The profile envelope remains tight under actual short incidence

This further lemma passes independent full proof audit. Unlike the whole-root
density bound used for the gap union in Section5, conditioning only on
the PROFILE lets us retain the sharp short-birth normalization.
The accepted global clock estimate, valid on every profile, is

    Pr(T<=H | profile)<=C_c A exp(C_c A)/R.           (19)

For any profile event E, the F0-incidence probability is at most

    (H+2)/mu0 * E[1_E Pr(T<=H | profile)]
      <=C_c E[A exp(C_c A)1_E].                      (20)

This is an inequality, not a claim that the original profile law is
unchanged. Since A<=3a and the newborn a has a uniform subGaussian
tail, Cauchy-Schwarz and its finite exponential moments imply

    Pr_inc,F0(a>1+x)<=C_c exp(-b_c x^2), x>=0.       (21)

The constants may be enlarged for bounded x. There is no extra factor
R in (21): the factor R from the maximal incidence weight is cancelled
by the conditional1/R in (19).

For every deterministic integer1<=S<=R, the event
L<max(S,2) forces A>kappa_c R/(2S) and hence a>kappa_c R/(6S).
Applying (21), and absorbing bounded R/S into its constant, proves

    Pr_inc,F0(L<max(S,2))<=C_c exp(-b_c r/S^2).      (22)

The raw early-triangle bound and mu0=Theta_c(1) also give

    Pr_inc,F0(Triangle_S>0)<=C_c S^2/r.              (23)

Thus for EVERY prescribed S=o(sqrt r), with S>=1, the sampled base
simultaneously has a zero original triangle through S and a valid safe
clock depth at least max(S,2), with probability tending to one. Neither
condition is imposed on its candidate partner births. This supplies
a legitimate high-probability base restriction for conditional finite-
layer arguments. It does not prove their claimed fibre law, any shifted
lifetime comparison, or eligible-label divergence.
