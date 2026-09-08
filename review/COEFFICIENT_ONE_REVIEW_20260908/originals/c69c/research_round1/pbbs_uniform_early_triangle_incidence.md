# Uniform early original-triangle birth and incidence bounds

2026-09-08. Pure proof; no computation or original-project edits.
This is the next derived corollary of the complete root-envelope proof,
fully read and passed by the worktree lead and independent Gaussian
reader. The coordinator has accepted Sections 1-8
of the root envelope theorem. The early-triangle corollary itself is
under separate coordinator review.

The precursor is task08's read-only note
`/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_early_branch_raw_incidence_bound.md`.
Its restricted exact path sum is retained here. The stronger depth and
averaging input is the root's read-only synthesis
`/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`.
All laws below concern ORIGINAL roots and original pruning arrays.

## 1. Statement and a global original-triangle definition

Let r>=1, R=sqrt(r), and let D be uniform among Dyck roots of semilength
r. Fix c>0 and put H=floor(cR). Let T include the consuming update, so
a repair trace has T+2 edges. Fix a deterministic integer 1<=S<=R.

Write h for the height and r_s for the original pruning profile. Put

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).

For 0<=s<h-1, use the actual original incoming-gap array Z_s, with its
fixed original particle indexing. At the last height-one row extend
this convention by

    p_(h-1)=1,       Z_(h-1,0)=ell_(h-1)=r_(h-1).

For s>=h set p_s=1 and Z_(s,0)=0. These are the natural one-part
composition conventions; at the height-one row the sole incoming
particle gap has length 2r_(h-1)+1. Interpret every index cyclically
modulo p_s, and define on every root

    F_S(D)=sum_(s=0)^(S-1) sum_(i=0)^s Z_(s,-i).       (1)

This global definition can repeat a slot in very short rows. The
physical interpretation below is used only where all relevant slots
are distinct; outside that sector the whole short event is bounded.

There is a constant C_c, independent of r and S, such that

    P(T<=H, F_S>0) <= C_c S^2/r^(3/2),                (2)

    E[(T+2)1{T<=H,F_S>0}] <= C_c S^2/r.              (3)

For W=(2r+1)Cat_r, the exact original-birth dictionary therefore gives

    number of physical births in this sector
        <= C_c (W/sqrt(r))(S^2/r).                   (4)

Every pairwise disjoint subfamily of their intervals or full repair
traces has cardinality at most the same bound. This is a count bound
for this specified sector, not a packing estimate for its complement.

## 2. The envelope supplies global conditional probability bounds

The root envelope is a function of the FULL original pruning profile.
It supplies a random a>=1 with uniform subGaussian upper tail and

    A=a+sqrt(log(a+2)),       1<=A<=3a.

For every fixed m>=0 and t>=0,

    E[A^m exp(tA)]<=C_(m,t),                          (5)

uniformly in r. Choose the root proof's fixed sufficiently small
kappa=kappa_c and put

    L=floor(kappa R/A).                               (6)

When L>=2, the profile has coarse bounds through 2L+1, h>2L, and all
physical-circumference and composition-prefix conditions hold at L.
Conditional on this FULL profile, the original-clock bound is

    P(T<=H | profile)<=C/L exp[C(1+H/h)].              (7)

The floor gives L>=kappa R/(2A), so H/h<=H/(2L)<=cA/kappa. Thus on
L>=2, (7) implies

    P(T<=H | profile)<=C_c A exp(C_c A)/R.            (8)

If L<2, (6) gives kappa R/A<2. The trivial probability bound one is
then at most 2A/(kappa R), so (8) holds on this sector too, after
increasing C_c. Hence (8) is GLOBAL, not restricted to typical
profiles. Multiplication by H+2 also gives

    E[(T+2)1{T<=H} | profile]<=C_c A exp(C_c A).       (9)

The constants may depend on fixed c through kappa. No growing-c
uniformity is asserted. Both (8) and (9) are conditional on the same
original profile that determines A and L.

## 3. The restricted path sum when L>=max(S,2)

On this sector, all rows s<S are above the height-one row, and their
query prefixes are distinct original slots. Define the usual exact
path weights at depth L:

    q_s=ell_s/(r_s+r_(s+2)+1),
    A_t^clock=sum_(t<s<L)(s-t)q_s,
    b_t=(t+1)q_t exp(-2A_t^clock),
    B=sum_(t<L)b_t,       B_early=sum_(t<S)b_t.

The superscript distinguishes the clock potential A_t^clock from the
profile-envelope parameter A. The accepted deterministic bounds are

    q_t<=C(t+2)ell_t/r,
    exp(-2A_t^clock)<=C((t+1)/L)^2,
    B<=C.                                             (10)

The coarse convex bounds truncate at every S<=L to give

    sum_(t<S)(t+2)^4ell_t<=CrS^2.                    (11)

For example put d_t=r_t-r_(t+1). Convexity and coarse bounds give
d_t<=Cr/(t+1)^2. One summation by parts with f_t=(t+2)^4 has final
term -f_(S-1)d_S<=0 and initial term 16d_0. Its interior terms are
at most C(t+1)^3d_t, whose sum is O(rS^2). This also covers S=1
directly by 16ell_0<=16r. Equations (10)-(11) imply

    B_early<=C S^2/L^2.                              (12)

On a valid short clock, let W_s be the actual mass queried in row s.
The exact row-count identity is

    n_s=s+1+2sum_(t<s)(s-t)W_t.

Before the first positive W_s, it gives n_s=s+1. Hence a first
positive actual row before S has a positive entry in (1). Conversely,
every actual query prefix contains the first s+1 original entries,
so positivity in (1) forces a positive actual row before S. Thus,
on this valid sector and T<=H,

    F_S>0 iff sum_(s<S)W_s>=1.                       (13)

Let K=ceil(H/h), theta=6(K+1), and Q0<=C/L be the exact path
comparison constants. The physical leaf bound gives sum_(s<L)W_s<=K.
For every such nonnegative path, the exact composition-prefix formula
gives the majorant

    Q0 product_(t<L)(theta b_t)^(W_t)/W_t!.

Retain (13) while summing this majorant. Extending the algebraic sum
to all nonnegative paths only increases it, and yields exactly

    Q0[exp(theta B)-exp(theta(B-B_early))]
       <=Q0 theta B_early exp(theta B).

No probability comparison is asserted for the newly added paths;
only their nonnegative algebraic majorants are added. By (10)-(12),
absorbing K+1 into an exponential gives

    P(T<=H,F_S>0 | profile)
       <=C S^2/L^3 exp[C(1+H/h)]
       <=C_c S^2 A^3 exp(C_c A)/R^3.                 (14)

Every row-law comparison was made conditional on the complete
original profile. The original rows are independent under that
conditioning, while entries within a row need not be independent.
No reached-root or same-orbit fresh-law statement has been used.

## 4. The complementary depth sector is also small

Put M=max(S,2). Since M is an integer, L<M implies

    kappa R/A<M<=2S,
    A>kappa R/(2S).

Therefore, deterministically,

    1{L<M}<=(2SA/(kappa R))^2.                       (15)

On this sector it is unnecessary to identify (1) with any physical
genealogy. Drop the F_S event entirely and use the GLOBAL conditional
probability bound (8). As L<M is profile-measurable, (15) gives

    E[1{L<M} P(T<=H,F_S>0 | profile)]
       <=C_c S^2/R^3 E[A^3 exp(C_c A)]
       <=C_c S^2/R^3.                               (16)

On L>=M, average (14) and use the same moment (5). Adding the two
sectors proves (2). Multiplying by H+2<=(c+2)R proves (3).
The exact physical birth normalization and the elementary fact that
a packing has no more members than its ambient family prove (4).

## 5. Scope

The estimates are uniform over deterministic integers 1<=S<=sqrt(r).
In particular, if S=o(sqrt(r)), this sector has o(W) raw trace
incidence and o(W/sqrt(r)) births, hence at most that many pairwise
disjoint members. Any further subfamily, including a residual
low-score subfamily with F_S>0, inherits these upper bounds.

Nothing here bounds the complementary all-zero original triangle
F_S=0, which remains the relevant unresolved trajectory sector.
The result neither estimates correlations at shifted birth times nor
asserts a fresh distribution after an orbit shift. It does not prove
packing for all positive-budget runs, sufficient shared repair, or a
coefficient-one construction.

## 6. Conditional concentration and tight normalizers

The accepted zero-budget Gaussian-band theorem in
pbbs_zero_budget_gaussian_band_weighted_lower_bound.md, Sections 1-4,
provides positive lower normalizers. Indeed choose any fixed
0<u<v<c. For the zero-budget roots with uR<=h=T<=vR, their birth
probability is asymptotic to a positive constant divided by R, and
their raw length-weighted mass converges to a positive constant.
They are all H-short for sufficiently large r. Combined with the
root envelope upper bounds, this gives

    P(T<=H)=Theta_c(1/R),
    mu_H=E[(T+2)1{T<=H}]=Theta_c(1).                 (17)

Thus division by these particular normalizers is justified. Let the
short-incidence marginal on original births be the law with density
(T+2)1{T<=H}/mu_H relative to the uniform original-root law. Equations
(2)-(3) and (17) imply, for every deterministic 1<=S<=R,

    P(F_S>0 | T<=H)<=C_c S^2/r,
    P_short-incidence(F_S>0)<=C_c S^2/r.             (18)

In particular the original triangle through every prescribed
S=o(sqrt(r)) is entirely zero with probability tending to one under
both laws. These are statements about the sampled ORIGINAL birth.
They assert no stationarity or fresh law at a shifted birth, and do
not estimate the overlap of different repair traces.
