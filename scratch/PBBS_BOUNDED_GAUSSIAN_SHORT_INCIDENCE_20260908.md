# Bounded Gaussian-short PBBS raw incidence

2026-09-08. Root pure-proof synthesis. Sections1-8 pass complete-file
root/helper/task05 audits, including the corrected Dyck convention and
the probability corollary. Sections9-10 also pass full independent
root-helper and task05 audits, including the actual birth-count packing
bound and the two correctly normalized all-short laws.
No computation. The theorem is about uniform ORIGINAL newborn
roots, not resampled reached states and not the incidence-biased law.

## 1. The theorem and its scope

Let D be a uniform Dyck word of semilength r. Write h for its height,
r_s for its size after s peak-pruning rounds, and T(D) for its PBBS
newborn lifetime INCLUDING the consuming update. A repair trace has
T+2 edges. For every fixed c>0, put H=floor(c sqrt(r)). Then

    mu_H:=E_D[(T+2)1_{T<=H}] = O_c(1).                 (1)

The same proof gives the stronger unweighted statement

    Pr_D(T<=floor(c sqrt(r)))=O_c(r^(-1/2)).           (1a)

The constant may depend on c. No uniform-in-growing-c bound is asserted.
The full raw trace incidence is therefore O_c(W), where
W=(2r+1)Cat_r. It need not be o(W): the already proved zero-budget
contribution has nonvanishing raw mass. Sufficient overlap, residual
packing, target repair and coefficient one are NOT consequences of (1).

The exact pruning census/edit facts and the finite original-clock path
identities used below are already proved in the root notes
PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md and
PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md, and in task05's
pbbs_quantitative_clock_polylog_short_mass.md, Sections4-5. The new
random profile envelope and its complete deterministic use are proved
here. No inverse-height tail theorem is needed for this proof.

## 2. One-depth profile concentration without a conditioning cost

Set R=sqrt(r), n=2r+1. Equality pruning of an odd cyclic binary word w
has size N_s(w) after s rounds. Its accepted finite facts are

    N_s(0D)=2r_s+1;
    one bit flip changes N_s by at most2, uniformly in s;
    0<=E_iid N_s-n/(s+1)<=2sqrt(n), uniformly in s.     (2)

The last inequality follows from the exact cosine census and a Gaussian
sum integral, including all depths. At s=0 the size is constant.

Couple iid fair bits to the uniform slice with r ones by uniformly
flipping the excess or deficit of ones. Permutation symmetry makes the
output uniform on that slice. If K is the iid number of ones, then
2E|K-r|<=sqrt(n+1), so (2) gives

    |E_slice N_s-n/(s+1)|<=2sqrt(n)+sqrt(n+1).          (3)

Expose the bits of a uniform slice word in order. The two possible
completions after the next bit is chosen can be coupled by one swap:
add one uniform unused position to a uniform (k-1)-subset to obtain a
uniform k-subset. Their N_s values differ by at most4. Hence the Doob
increments have conditional range length at most4, and the elementary
bounded-range MGF bound gives

    E_slice exp(lambda[N_s-E_slice N_s])<=exp(2n lambda^2).

A word with r ones and r+1 zeros has exactly one rotation of the form
D0, with D Dyck in the convention1=up: cut after the FIRST minimum of
its one-minus-zero partial sums at times0,...,n-1. Later sums are at
least this minimum, and earlier sums are strictly larger, so every
proper partial sum after this cut is nonnegative, while the full sum
is -1. A later occurrence of the same minimum would fail after wrapping;
any larger cut level would encounter a smaller level, so the cut is
unique. Moving the terminal zero to the front gives the unique rotation
0D. Its n rotations are distinct because a nontrivial repetition would
divide the total excess1. Each Dyck root has exactly n slice preimages.
The entire rotation-invariant pruning profile has exactly the Dyck law
on this slice, with no probability reweighting. Equations (2)-(3) and
the MGF bound therefore imply, for every s>=0 and x>=0,

    Pr_D(|r_s-r/(s+1)|>4R+xR)<=2exp(-x^2/6).          (4)

This is also the complete finite argument in task05's
pbbs_fixed_count_pruning_profile_subgaussian.md, which root has fully
read. Across-depth independence is neither needed nor asserted.

## 3. A profile-measurable subGaussian envelope parameter

Put e_s=r_s-r/(s+1), J=ceil(R), and for each integer1<=j<=J define

    g_j=ceil(R/j)-1.

Index both depths g_j and g_j-1 when nonnegative. Repeated indices
are harmless: the following union bound is over indexed copies.
Define the following function of the FULL ORIGINAL profile:

    a=1+max_{indexed (j,t)}
          [ (|e_t|/R-4)_+/8-sqrt(log(j+2)) ]_+ .     (5)

In particular a>=1. Applying (4) to at most two indices per j gives,
for x>=0 and p=64/6>2,

    Pr(a>1+x)
       <=4sum_{j>=1} exp[-p(x+sqrt(log(j+2)))^2]
       <=C exp(-p x^2).                              (6)

Thus all fixed exponential moments of a are bounded uniformly in r.

We claim, with one absolute constant C0 (for example64), that

    |e_s|<=E_s:=C0 R[a+sqrt(log(2+R/(s+1)))]
                    for EVERY integer s>=0.          (7)

Here is the interpolation, including its rounding. Let v=R/(s+1).
If v>1 is not an integer, put j=floor(v). Then

    u=g_{j+1}<=s<=w=g_j-1.

Both indexed endpoints exist. Monotonicity gives r_u>=r_s>=r_w.
Their deterministic means bracket r/(s+1) within R: the endpoint
means lie between jR and (j+1)R whenever this bin contains s.
Their indexed bounds from (5), with logarithms at j and j+1, prove
(7), absorbing this R interpolation error and the additive constants.
If v is an integer j, then g_j=s and no interpolation is needed.
If v<=1, then g_1<=s, r_s<=r_{g_1}, and both deterministic means
are at most R. This proves (7) on all larger depths as well, including
after extinction. Large one-step drops are why both crossing indices
were included in the grid. C0=64 dominates the displayed constants.

## 4. A legal profile-dependent depth

For t>=1 write

    E(t)=C0 R[a+sqrt(log(2+R/t))],    E_s=E(s+1),
    A=a+sqrt(log(a+2)).

We have 1<=A<=3a. Choose a sufficiently small positive constant
kappa=kappa_c; all requirements on it are stated below. Set

    L=floor(kappa R/A).                               (8)

The FULL profile determines a and L before any inverse-pruning row is
examined. Conditional on that profile, L is a deterministic integer.

For L>=2, flooring gives

    L>=kappa R/(2A),
    L E(L)/r<=delta_kappa,
    delta_kappa:=C0 kappa[1+sqrt(log(8/kappa))].        (9)

Indeed R/L<=2A/kappa and
sqrt(log(2+2A/kappa))<=sqrt(log(a+2))+sqrt(log(8/kappa)).
The function tE(t) is increasing, while E(t) is decreasing. Thus for
t<=2L+2<=3L,

    tE(t)/r<=3L E(L)/r<=3delta_kappa.

Choose kappa so 3delta_kappa<=1/4. Equation (7) now yields

    (3/4)r/(s+1)<=r_s<=(5/4)r/(s+1),  0<=s<=2L+1.   (10)

In particular r_{2L}>0, so h>2L. This automatically deals with the
height condition; we do not discard a constant-probability low-height
set. Cases L<2 will be bounded directly at the end.

A second consequence needed below is

    E(1)<=L E(L),
    sum_{s=0}^{L-1}E_s<=C L E(L).                    (11)

For the sum, use
sqrt(log(2+R/t))<=sqrt(log(2+R/L))+sqrt(log(L/t))
for1<=t<=L, and sum the integrable decreasing function
sqrt(log(1/x)) over right endpoints t/L. No depth independence enters.

## 5. The deterministic clock potentials

For0<=s<L let

    ell_s=r_s-2r_{s+1}+r_{s+2}>=0,
    p_s=2r_{s+1}+1,
    q_s=ell_s/(r_s+r_{s+2}+1).

The convexity ell_s>=0 and monotonicity of r_s are standard exact
pruning-profile properties. Define

    Phi=sum_{s<L}(s+1)q_s,
    A_t=sum_{t<s<L}(s-t)q_s,
    B_L=sum_{t<L}(t+1)q_t exp(-2A_t).

Uniformly for all profiles satisfying (7), with L>=2 as in (8),

    Phi>=log L-C,
    A_t>=log[L/(t+1)]-C,  0<=t<L,
    B_L<=C.                                           (12)

All constants here are absolute once C0 is fixed; they do not depend
on a, r, or the profile. We prove the error accounting in full.

Let

    b_s=r/(s+1)+r/(s+3),
    beta_s=1/b_s=[s+2-1/(s+2)]/(2r).

The actual denominator differs from b_s by at most3E_s. Comparability
(10) consequently gives

    |q_s-beta_s ell_s|<=C(s+2)^2 E_s ell_s/r^2,
    q_s<=C(s+2)ell_s/r.                               (13)

It is essential not to replace the correlated E_s ell_s product by
separate averages. Instead let f_s=(s+2)^3 E_s. This sequence is
increasing, and its interior second differences obey

    |f_s-2f_{s-1}+f_{s-2}|<=C(s+2)E_s,       s>=2.    (14)

For completeness put u=log(2+R/t), alpha=R/(2t+R), g=sqrt(u).
Direct differentiation gives

    g'=-alpha/(2t sqrt(u)),
    g''=[alpha(2-alpha)/(2sqrt(u))
               -alpha^2/(4u^(3/2))]/t^2>=0.

Since u>=log2, |tE'| and t^2 E'' are at most E/(2log2).
Thus f(t)=(t+1)^3E(t) is increasing and |f''(t)|<=C(t+1)E(t).
On the backward interval of length two, the argument ratios are at
most3 and E changes by at most an absolute factor. Integrating f''
proves (14). The initial two summation coefficients are O(E(1)).

For any increasing weights f_s, the last two summation-by-parts terms
against ell_s are

    -[f_{L-1}-f_{L-2}]r_L-f_{L-1}(r_L-r_{L+1})<=0.

Apply this with (14) and the upper bound in (10). It yields

    sum_{s<L}(s+2)^3 E_s ell_s
       <=C r[E(1)+sum_{s<L}E_s].                     (15)

Consequently the total reciprocal-denominator debit in either Phi
or A_t is, by (11), at most

    C r^-2 sum_{s<L}(s+2)^3 E_s ell_s
       <=C L E(L)/r<=C delta_kappa=O(1).              (16)

For the baseline terms, convexity with m=floor(L/2) and (10) gives

    r_L<=Cr/L,
    d_L:=r_L-r_{L+1}<=[r_m-r_L]/(L-m)<=Cr/L^2.

The exact identity

    sum_{s<L}(s+1)^2ell_s
       =r+2sum_{j=1}^{L-1}r_j-(2L-1)r_L-L^2d_L

and (11) bound it below by2r log L-Cr. Since
(s+1)beta_s>=(s+1)^2/(2r), (16) proves the Phi bound.

For A_t use g_s=(s-t)[s+2-1/(s+2)] for s>=t. The first nonzero
summation coefficient is at least2, the interior second differences
are2+2(t+2)/[s(s+1)(s+2)]>=2, and the two final terms are O(r)
uniformly in t. Thus its beta_s baseline is at least

    sum_{j=t+1}^{L-1}r_j/r-C
       >=log[L/(t+1)]-C-r^-1 sum_{j<L}E_j
       >=log[L/(t+1)]-C.

The empty t=L-1 case is immediate. Equation (16) proves the second
part of (12). Finally ordinary polynomial summation by parts and
(10) give sum_{s<L}(s+2)^4ell_s<=CrL^2. With (13),

    B_L<=C/(rL^2) sum_{s<L}(s+2)^4ell_s<=C,

completing (12).

## 6. Exact original-row clock bound at the chosen depth

Conditional on the FULL original profile, the original rows Z_s are
independent uniform weak compositions of ell_s into p_s parts.
They are queried in fixed original order0,-1,-2,... . If W_s is the
sum of the queried entries, the exact clock recurrence is

    n_s=s+1+2sum_{t<s}(s-t)W_t,
    m_L=1+2sum_{s<L}W_s.                               (17)

Thus each query count depends only on earlier original rows. For a
specified path with sum W_s<=K and p_s>=2(n_s+W_s), the exact
composition-prefix probabilities give

    Pr(path | profile)
       <=Q0 product_{t<L}
          [6(K+1)(t+1)q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0<=exp(-Phi).                                    (18)

These finite identities and inequalities are the previously audited
original-clock path bound, not an independent-slot approximation.
Using (12) and the multinomial theorem to sum the nonnegative paths,

    Pr(sum_{s<L}W_s<=K | profile)<=C/L exp[C(K+1)].    (19)

We check every depth/size requirement for the physical use of (17).
On L>=2, (10) implies uniformly s<L

    p_s>=r/L>=RA/kappa.

Every short physical lifetime T<=H has clock length2T+1<=2H+1.
Choose kappa additionally small enough depending only on fixed c so
p_s>2H+1. Then the accepted physical clock partition applies through L.
Since h>2L, its disjoint depth-L leaves each have length at least
2(h-L)+1; on a short lifetime this forces sum W_s<=H/h.
Set K=ceil(H/h). Every path included in (19) has

    n_s+W_s<=3(K+1)(s+1)<=(3/2)H+6L.

Taking, for example, kappa<=1/[100(c+1)] in addition to the earlier
condition makes p_s>=2(n_s+W_s) for all sufficiently large r. Thus
all physical and composition conditions hold for EVERY summed path.
Equations (18)-(19) imply, conditional on this original full profile,

    Pr(T<=H | profile)<=C/L exp[C(1+H/h)].             (20)

There is no new conditioning on a reached profile. The cutoff L is a
function only of the original profile, which was already conditioned on.

## 7. Average the profile bound; no discarded profile sector

For L>=2, use (9) and h>2L in (20). The conditional raw incidence is
at most

    C(H+2)/L exp[C(1+H/h)]<=C_c A exp(C_c A).          (21)

For L<2, the floor in (8) means R<2A/kappa. The trivial conditional
bound H+2 is then at most C_c A, so (21) remains valid without using
any clock argument. Small finite r can also be absorbed into C_c.

Finally A<=3a, and (6) makes E[A exp(C_c A)] finite uniformly in r.
Averaging (21) proves mu_H<=C_c, which is (1).

For (1a), retain the probability form of (20): when L>=2 it is
at most C_c A exp(C_c A)/R. When L<2, R<2A/kappa implies the
trivial bound1<=2A/(kappa R). Averaging over the same envelope
parameter therefore gives Pr(T<=H)<=C_c/R. Multiplying by H+2
is also a direct proof of (1).

## 8. Exact remaining gap

The occupied-edge fraction is mu_H E_inc[1/K_overlap]. Bounded mu_H
reduces this question to overlap control, but supplies none by itself.
The positive-budget residual and the low-score trajectory estimate in
PBBS_SQRTLOG_SCORE_TO_PACKING_REDUCTION_20260907.md remain open.
No low-score hypothesis, fresh-root law, stationary-incidence law or
coefficient-one conclusion was used or established in this proof.

## 9. A handled sector: positive early original triangles

Let S be any deterministic integer1<=S<=sqrt(r). In the cyclic original
row coordinates, define

    B_S={sum_{s=0}^{S-1} sum_{i=0}^s Z_{s,-i}>0}.     (22)

Rows beyond extinction are extended by their unique zero composition.
Indices are interpreted in the original cyclic row; on every safe
clock used below the queried prefixes are shorter than its circumference
and contain distinct slots. There is no shifted-root sampling in (22).

Uniformly in S,

    Pr(T<=H, B_S)<=C_c S^2/r^(3/2),
    E[(T+2)1_{T<=H,B_S}]<=C_c S^2/r.                 (23)

To prove this, condition on the complete original profile as before.
First suppose L>=max(S,2). Put b_t=(t+1)q_t exp(-2A_t). Equation (12),
(13), and polynomial summation by parts truncated at S give

    sum_{t<S}b_t
       <=C/(rL^2) sum_{t<S}(t+2)^4ell_t
       <=C S^2/L^2.                                 (24)

The terminal terms of the truncated summation are nonpositive. Its
interior bound uses r_s<=Cr/(s+1) through S+1; for S=1 use ell_0<=r.
On a safe short clock, (22) is equivalent to W_t>0 for some t<S:
before the first positive row, (17) queries exactly0,-1,...,-t;
conversely every actual query prefix contains these t+1 original slots.

Keep this restriction while summing (18). After applying the path bound
on total W<=K, enlarge only the NONNEGATIVE WEIGHT sum to all paths.
With theta=6(K+1), its restricted exponential sum is

    exp(theta B_L)-exp(theta[B_L-sum_{t<S}b_t])
       <=theta (sum_{t<S}b_t)exp(theta B_L).

Together with Q0<=C/L and (24), this proves

    Pr(T<=H,B_S | profile)
       <=C S^2/L^3 exp[C(K+1)]
       <=C_c (S^2/R^3) A^3 exp(C_c A).               (25)

All probability bounds were applied only to the paths whose size
hypotheses were checked in Section6; adding the other product weights
does not assert that they are possible physical paths.

If L<max(S,2), then A>kappa R/(2S). Therefore

    1_{L<max(S,2)} <=4S^2 A^2/(kappa^2 R^2).

The GLOBAL conditional probability bound proved with (1a), including
L<2, is C_c A exp(C_c A)/R. Multiply it by this indicator bound,
and ignore B_S. This gives the same upper bound as (25) without using
an unsafe genealogy. Averaging (25) over a, whose fixed exponential
moments are uniformly finite, proves the first part of (23). Multiplying
by H+2 proves its raw-incidence part.

In physical coordinates there are at most

    C_c W S^2/r^(3/2)

such short births, so their maximum edge-disjoint repair packing is
bounded by that same number. Consequently for EVERY prescribed
S=S_r=o(sqrt r), all Gaussian-short births with a positive original
triangle before S have packing o(W/sqrt r), and raw incidence o(W).
This conclusion needs no division by the budget cutoff J_r.

The remaining short births have all entries of the growing original
triangle in (22) equal to zero, including Z_{0,0}=0. No abundance of
overlapping SHIFTED short births follows from that unshifted condition.
The packing of this complementary sector and coefficient one remain
open. Estimate (23) strengthens the separately audited earlier
logarithmic-cutoff early-branch bound from task08.

## 10. Sharp orders and the two correctly normalized short laws

The accepted elementary zero-budget Gaussian-band lower bound in
PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md supplies, for
every fixed0<a_0<b_0<min(c,1/2), at least a positive constant times
r^(-1/2) newborn probability with T=h in[a_0 sqrt r,b_0 sqrt r].
Those lifetimes lie below H for all sufficiently large r. Their
T+2 weights are at least a_0 sqrt r. Together with (1) and (1a),
this proves the matching orders

    Pr(T<=floor(c sqrt r))=Theta_c(r^(-1/2)),
    E[(T+2)1_{T<=floor(c sqrt r)}]=Theta_c(1).         (26)

This invokes only the previously accepted elementary positive lower
bound, not a new local-limit or independence assertion.

Consequently (23) can be normalized under either of the following
ACTUAL all-short laws:

    Pr(B_S | T<=H)=O_c(S^2/r),
    Pr_short-inc(B_S)=
       E[(T+2)1_{T<=H,B_S}]/mu_H=O_c(S^2/r).         (27)

Both statements hold uniformly for deterministic1<=S<=sqrt r.
Thus every prescribed S=o(sqrt r) gives an all-zero original
triangle through S with probability1-o(1) under BOTH laws. They
are not statements about a positive-budget-only or other restricted
incidence law whose normalizer might be smaller. Nor do they imply
that nearby shifted newborns remain short or share a repair witness.
