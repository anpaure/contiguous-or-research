# Coefficient one for complete interval-union words

**Status: proposed proof with AI-agent internal reviews. It has not been
externally reviewed or formally verified. No gap was found in the current
reviews; their PASS labels must not be read as independent human certification.**

2026-09-08. Consolidated proof with supporting finite lemmas linked below.
The two new main lemmas and the passage through the existing literal word
compiler have passed root, direct-route and appendix mathematical audits.
This is a proof manuscript, not a formal proof-assistant certificate.
No mathematical computation was used in this PBBS proof. The manuscript
was recorded in MASTER_HANDOFF.md, Section 9.2, on 2026-09-08 as a proposed
proof [P], retaining the review status above.

## Theorem

Let nu(n) be the minimum length of a word of nonempty subsets of [n]
whose nonempty contiguous interval unions include every nonempty subset
of [n]. With W(n)=binom(n,floor(n/2)),

$$
\boxed{\displaystyle \nu(n)=(1+o(1))\binom{n}{\lfloor n/2\rfloor}.}
\tag{1}
$$

This holds in every sufficiently large dimension and covers every rank.
No explicit convergence rate is asserted.

The new argument proves abundant overlap for ALL Gaussian-short PBBS
repair intervals. It combines growing-depth stationary flux with an
exact renewal law for ACTUAL shifted triangles. The earlier raw-cone
renewal alone did not provide this physical interface.

## 1. The physical reduction and exact base fibre

Work in dimension 2r+1; write R=sqrt(r) and
W_r=binom(2r+1,r)=(2r+1)Cat_r. The full PBBS factor has W_r edges.
A newborn lifetime T includes the consuming update, its native physical
same-label return has length 2T+1, and its repair trace has T+2 edges.

For fixed 0<c<C put H_c=floor(cR), H_C=floor(CR) and

    F_c={GOOD,Z_(0,0)=0,T<=H_c}, F_C={GOOD,Z_(0,0)=0,T<=H_C}.

GOOD is the established invariant profile condition. Actual base
incidence weights a uniform Dyck root by(T+2)1_(F_c)/mu_c, then samples
offset j uniformly in{0,...,T+1}. The accepted bounds are
mu_c=Theta_c(1) and mu_C=O_C(1). Let K_C count the ACTUAL F_C traces
containing the sampled edge. It will suffice to prove K_C tends to
infinity under this law.

Let D_s be the original depth-s pruned core, r_s its semilength,
p_s=2r_(s+1)+1 and ell_s=r_s-2r_(s+1)+r_(s+2). The exact inverse-pruning
rows Z_s are independent uniform weak compositions conditional on the
complete profile. On the safe base zero triangle through depth S, expose

    E_S=(complete original profile, all original rows at depths>=S, j).

Conditional on this environment, row s<S is uniform on P_s=p_s-s-1
free slots, and its slots0,-1,...,-s are fixed zero. The short-base
condition introduces no further weight on these free entries.

The physical clocks C_s and T_s select the next predecessor and next
same label. They commute, C preserves parity, and T reverses parity.
A zero gap gives the exact short-horizon rules C->C and T->CT under
pruning, including reverse grouping. Profiles and height are invariant.

## 2. Growing-depth flux supplies eligible boundaries

Here and below all quoted finite identities are proved in the linked
supporting notes, with their original source dependencies recorded.
Set L=floor(r^(2/5)). The accepted sampled-base triangle and safety
bounds retain depth L with probability1-o(1): triangle failure costs
O_c(L^2/r), and the safe-profile exception is exponentially small in
r/L^2. This does not require simultaneous zero triangles for all partners.

Sum all upper completions to obtain the EXACT unnormalized stationary
core measure q_(r,L), divided by Cat_r, retaining GOOD and safety. Define

    M_L=sum_E q_(r,L)(E) pk(E).

The new profile calculation proves, for every fixed eta>0,

    M_L<=C_eta r/L^(3-eta)+superpolynomially small error.          (2)

Briefly, uniform original-depth concentration through2L gives
r_u=(1+o(1))r/(u+1), and convexity gives
d_u=r_u-r_(u+1)<=O(r/u^2). The exact zero-triangle probability is
product_(u<L)(p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1). Its negative logarithm
is at least sum_(u<L)(u+1)ell_u/(p_u+ell_u). The exact Abel identity for
sum(u+1)(u+2)ell_u supplies2r log L-O(r). Thus the zero probability is
at most C_eta L^(-1+eta). Multiplication by d_L proves(2), including
the negligible exceptional-profile contribution. With eta=1/8,
M_L=O(r^(-3/20)).

On the base core let b_0 be the endpoint of Q_L=C_L^L T_L. For fixed K,
t_K=C_L^K(0) and Delta_K=C_L^K(b_0)-b_0. The exact stationary C index
is the peak count. The Q_L endpoint permutation preserves q_(r,L), even
when switching parity. Consequently

    sum q_(r,L)t_K=2K M_L, sum q_(r,L)Delta_K=2K M_L.     (3)

In the actual Palm sum the base weight is at most H_c+2. Markov and
offset counting give

    P_inc,c(t_K>=L)=O(r^(-1/20))+o(1),
    Delta_K=o(R), P_inc,c(2j<t_K)=o(1).                  (4)

Fix S>=K. Base zeros identify the first K common C boundaries at depths
S and L by reverse grouping inside the already short base endpoint
b_0<=2H_c+1; this supplies a finite safe horizon for that identification.
Require K extra zeros immediately after each base prefix in
rows S,...,L-1. Their exact composition-product probability tends to

    product_(u=S)^infinity(1-1/(u+2)^2)^K
                         =[(S+1)/(S+2)]^K.             (5)

The tail is uniform because the finite Abel bound
sum_(u=m)^(L-1)ell_u/r_(u+1)<=O(1/m) controls all remaining extra slots.
No growing-depth geometric approximation is used.

On this collar, C_S^(S+k)T_S reverse-groups from the FINITE endpoint
C_L^k(b_0). By(4) it passes the fixed larger cutoff C with probability
1-o(1). Grouping is used only after that safe endpoint test. If A_S
is the set of common boundaries passing the deep cutoff and the
sampled-edge overlap test, then

    liminf_r P_inc,c({0,...,K} subset A_S)
                              >=[(S+1)/(S+2)]^K.        (6)

## 3. The exact actual multipoint law

Equation(4), together with h>=2L on the retained safe base, prevents
any repeated selected label before t_K at every upper depth. For fixed
S it is enough to restrict to the E_S-MEASURABLE event

    t_K<2(h-S)+1, n_S=2r_S+1>=2S+1.                    (7)

This has probability1-o(1) and guarantees no repeats for EVERY upper
completion, so the exact row law remains unchanged. The depth-S sites
0,-1,...,-K are original zero bits: they are first selected at even times.

Let I_s be the ORIGINAL initial insertion map, with

    I_s(0)=0, I_s(a)-I_s(a-1)=1+epsilon_(s,a)+2Z_(s,a),
    I_s(a+p_s)=I_s(a)+n_s.

Here epsilon records whether adjacent child bits differ. The physical
position cocycle is I_s plus a previous-visit count. That count vanishes
on(7), so the actual shifted labels are the nested static images

    xi_S(k)=-k, xi_s(k)=I_s(xi_(s+1)(k)).                (8)

Define Y_k by the FULL shifted zero triangle

    Z_(s,xi_(s+1)(k)-u)=0 for0<=s<S, 0<=u<=s.           (9)

Two exact geometric facts determine its joint law. First, insertion
maps expand integer distances and are periodic; thus
n_v+xi_v(k)>=n_S-k. Every query block lies in the same fundamental
arc(-p_s,0], for every fibre configuration. There are no cyclic collisions.
Second, for successive requested successes i<j and g=j-i, their row-s
blocks add exactly min(g,s+1) new positions. If g<=s+1, the earlier
HIGHER-row zero tests preserve a consecutive zero block through each
insertion, so the centers are exactly g apart. If g>=s+1, increasing
maps separate the centers by at least g, making the blocks disjoint.

Therefore, for0=k_0<...<k_m<=K, g_a=k_a-k_(a-1), and
M_s=sum_a min(g_a,s+1), revealing whole rows downward gives EXACTLY

    P(Y_(k_1)=...=Y_(k_m)=1 | E_S)
       =product_(s=0)^(S-1)
            (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s).          (10)

The locations depend on deeper rows, but the probability of M_s new
zeros depends only on the profile. No independence of survival events
or freshness after failed chronological tests is assumed. These events
need not equal original-index cones pointwise.

For fixed S,K, actual-incidence profile concentration gives
ell_s/(ell_s+P_s)->1/(s+2)^2. The limiting multipoint probabilities are

    product_a u_(g_a,S),
    u_(g,S)=1/(g+1)*[(S+2)/(S+1)]^g, 1<=g<=S.           (11)

For fixed K let S tend to infinity. Finite inclusion-exclusion identifies
the full indicator vector with the renewal process of masses u_n=1/(n+1).
It is proper: U(z)=-log(1-z)/z and

    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt

has nonnegative coefficients
-integral_0^1(-1)^n binom(t,n)dt for n>=1, constant coefficient0 and
F(1-)=1. Its gaps are finite positive integers almost surely. Hence its
number R_K of renewals through K tends to infinity almost surely.

## 4. Native partners, occupied support, and packing

If k is deep-eligible and Y_k=1, the tested finite C_S^S T_S word
reverse-groups through all rows to the native T_0 clock. It is H_C-short
and its trace contains the sampled edge. Row zero supplies its actual
top gap0, and invariant GOOD is preserved. Distinct k give distinct
physical births. Therefore K_C>=sum_(k=0)^K Y_k on{0,...,K} subset A_S.

For each fixed M, use this bound and a union bound. First send r to
infinity at fixed S,K, then S to infinity at fixed K, using(6),(11).
The resulting limsup of P_inc,c(K_C<=M) is at most P(R_K<=M).
Sending K to infinity proves

    K_C -> infinity under actual base-c incidence
                         for every fixed0<c<C.         (12)

The cutoff remains fixed; C=2c suffices. Equivalently choose finite K,
then finite S, then all r beyond a threshold. No independence between
eligibility and survival or interchange of growing parameters is needed.

The established deterministic cross-cutoff inequality is

    |U_c|/W_r<=mu_c P_inc,c(K_C<M)+mu_C/M.               (13)

Equations(12),(13) give |U_c|=o_c(W_r). The accepted negligible
top-gap/BAD incidence extends this to ALL births with T<=H_c.
For fixed epsilon>0 the low-height birth count and edge-capacity split
bound their maximum edge-disjoint packing P_c(r) by

    R P_c(r)/W_r<=C_c exp(-b_c/epsilon^2)
                              +|U_all,c|/(epsilon W_r).

Let r tend to infinity and then epsilon decrease to zero. Thus

    P_c(r)=o_c(W_r/sqrt(r)) for every fixed c>0.         (14)

## 5. Literal word, all ranks, and every dimension

The audited PBBS owner-corridor theorem supplies every required central
target. Erosion, actual dominance-staircase cut charts, and the existing
product-SCD exterior word give the finite all-target ledger

    nu(2r+1)<=W_r+2H Cat_r
               +2(5H-1)P({T<=H-1})+2L_r(r-H),           (15)
    2L_r(r-H)/W_r<=C exp(-(H-1)^2/(8r)),

for2H<=r+1. All witnesses are ordinary contiguous interval unions;
the exact exterior boundary and every seam are charged in(15).

For each fixed integer j use H=floor(jR)+1 and(14). Choose successive
finite thresholds after which both normalized central excesses are
at most1/j. A sufficiently slow diagonal j(r)->infinity keeps H=o(r)
and2H<=r+1. Both central excesses and the exterior term then vanish,
giving nu(2r+1)<=(1+o(1))W_r. The exact trimmed one-coordinate lift
doubles the word length, while W(2r+2)=2W_r, proving the even case.
At a fixed right endpoint the interval unions are nested, so at most
one middle-rank target is realized there. Hence nu(n)>=W(n), proving(1).

## Supporting proofs and contribution record

* [Exact stationary core law and flux](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md).
* [Full growing-depth eligibility and insertion-interface proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md).
* [Exact actual multipoint renewal and native-partner proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md).
* [Complete previously audited literal compiler, tail and parity chain](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md).

This consolidated manuscript also passed complete independent reads by
both direct-route and appendix, with no mathematical correction required.
The eligibility and renewal files have root, direct-route and appendix
full-file audits marked PASS. Both independent auditors also reread the
complete cross-cutoff and literal compiler chain. This manuscript
consolidates those checked arguments and retains their exact quantifiers.

The user's separate selective-truncation construction proves the explicit
coefficient 1.177987. Its geometry, padding, literal compilation, energy
identity and moment certification also pass independent checks; the
small exact numerical check ran only on h100. That construction and
the earlier finite-completion refinement are credited to the user.
Neither is used in the PBBS proof above.

The zero-budget renewal/packing theorem rederived during this continuation
already appeared in a September7 note. The new result here concerns the
FULL Gaussian-short family, including positive-budget runs.
