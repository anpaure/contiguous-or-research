# Common deep C boundaries are eligible with an explicit probability

2026-09-08. Pure proof, no mathematical execution. Direct-route deduction.
Root and appendix_a independently read and checked Sections 1-5 in full:
both audits PASS. Root also read and checked the no-repeat/static-position
corollary in Section 6: PASS. Appendix_a's full Section 6 audit, including
the zero-bit and finite-span observations: PASS. Its final deterministic
two-arc guard was proposed by appendix_a and independently checked by
direct-route.

Fix 0<c<C. For every fixed S>=K>=1, under the ACTUAL base-c incidence
law, the first K common depth-S C boundaries all pass the deep partner
cutoff and sampled-edge overlap test with limiting lower probability

    [(S+1)/(S+2)]^K.                                    (1)

Thus, for each fixed K, that probability tends to one as S tends to
infinity after r. This resolves an eligibility issue in the common-
boundary transfer. Survival through the actual intermediate shifted
triangles, and hence divergence of L_0, are not proved here.

## 1. Exact inputs and the sampled-base/all-partner distinction

Use H_c=floor(c sqrt(r)), H_C=floor(C sqrt(r)), and the retained family
F_c={GOOD,T<=H_c,Z_(0,0)=0}, with raw incidence normalizer mu_c=Theta_c(1).
The accepted sources are:

* the exact original composition fibre and uniform depth concentration
  recorded in `PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md`;
* the exact core law in
  `PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`;
* the stationary core measure and C-clock index in
  `PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md`;
* the original uniform early-triangle source
  `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_uniform_early_triangle_incidence.md`,
  Section 6, especially (18).

The last source bounds the SAMPLED BASE triangle failure under short
incidence by O_c(L^2/r), together with the accepted safe-profile tail
O_c,C(exp(-b_c,C r/L^2)). These bounds allow every deterministic
L=o(sqrt(r)). They do not include the additional sqrt(r) loss incurred
when asking that ALL partners simultaneously have zero triangles.
The all-partner statement is not used at the growing depth below.

Set

    L=floor(r^(2/5)).                                    (2)

Let B_L be the event that the sampled base has F_L=0 and the exact
depth-L safe profile domain, strengthened to the partner cutoff C:

    r_L>H_C,                  h>=2L.                    (3)

Then P_inc,c(B_L)=1-o(1). All upper circumferences exceed 2H_C+2, so
the accepted forward and reverse grouping applies whenever the finite
candidate endpoint is at most 2H_C+1. No expansion to the bottom row,
nor endpoint of an infinite oracle, will be used.

## 2. A stationary weighted peak mass tends to zero

Write a_u=r_u, d_u=a_u-a_(u+1)=pk(D_u), and
ell_u=d_u-d_(u+1)>=0. Thus a_u decreases and d_u is nonincreasing.
The original uniform-root concentration input states, for every u and x,

    P_D(|a_u-r/(u+1)|>(4+x)sqrt(r))<=2 exp(-x^2/6).

With B_r=(4+log r)sqrt(r), define A_r by these simultaneous inequalities
with B_r on the right for every u<=2L+2. Its failure probability is at
most (4L+6)exp(-(log r)^2/6), smaller than every fixed inverse power of
r. On A_r, uniformly in this range,

    (1-delta_r)r/(u+1)<=a_u<=(1+delta_r)r/(u+1),
    delta_r=(2L+3)B_r/r=o(1).                            (4)

Convexity gives, for u>=2,

    d_u <= [a_floor(u/2)-a_u]/[u-floor(u/2)]
                                              <= C_0 r/u^2. (5)

In particular d_L<=C_0r/L^2. The same estimates supply (3), positivity
through 2L, and all distinct-slot margins for large r.

Conditional on the original complete profile, on A_r the probability
that the whole canonical depth-L triangle is zero is EXACTLY

    product_(u=0)^(L-1)
             (p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1),
    p_u=2a_(u+1)+1,                                    (6)

with falling factorials. We claim that, for every fixed eta>0, a
constant C_eta bounds this probability by

    C_eta L^(-1+eta).                                   (7)

Here is a uniform proof. A row's negative logarithm in (6) is at least
(u+1)ell_u/(p_u+ell_u), using log(1+x)>=x/(1+x). By (4)-(5), for every
sufficiently large fixed m=m(eta), and then sufficiently large r,

    (u+1)ell_u/(p_u+ell_u)
      >=(1-eta/4)(u+1)(u+2)ell_u/(2r),   m<=u<L,         (8)

after making the fixed tolerance smaller if needed. Indeed ell_u<=d_u
and p_u+ell_u<=2r/(u+2)[1+delta_r+O(1/u)]. No relative approximation
to the individual second differences ell_u is being assumed.

For w_u=(u+1)(u+2), discrete summation by parts gives the exact identity

    sum_(u=m)^(L-1) w_u ell_u
      =w_m d_m-w_(L-1)d_L
        +2(m+2)a_(m+1)-2L a_L
        +2 sum_(u=m+2)^(L-1) a_u.                       (9)

The two negative boundary terms have magnitude O(r) by (4)-(5).
The sum of a_u in the last term, before its factor 2, is at least
(1-delta_r)r log L-O_m(r).
Consequently (8)-(9), with sufficiently small tolerances, give total
negative logarithm at least (1-eta)log L-O_eta(1). This proves (7).

Let q_(r,L) be the EXACT unnormalized stationary core measure from the
core-law and flux notes: each D_L=E of size t and peak count k has
weight W_(r,L)^GOOD(t,k)/Cat_r, restricted to t>H_C and height(E)>=L.
Define its weighted peak mass

    M_L=sum_E q_(r,L)(E) pk(E).

The inverse-array bijection identifies this with the original uniform-
root expectation of d_L on GOOD, the domain, and F_L=0. On A_r use
(5) and (7); on its complement use d_L<=r. Thus

    M_L <= C_eta r/L^(3-eta)+r P_D(A_r^c).               (10)

Taking eta=1/4 and L from (2) proves

    M_L=O(r^(-1/10))+o(1)=o(1).                          (11)

The estimate is for the STATIONARY UNNORMALIZED reference measure,
not for peaks in a freshly sampled short-conditioned endpoint.

## 3. Small initial boundary times and small extra endpoint times

The exact depth-L base-incidence law conditional on B_L is

    q_(r,L)(E)/mu_(r,L,c)
       *1{a_L^*(E)<=H_c, 0<=j<=a_L^*(E)+1},              (12)

where Q_L=C_L^L T_L has physical endpoint b_0=2a_L^*+1. Its normalizer
satisfies mu_(r,L,c)/mu_c=P_inc,c(B_L)->1, by Section 1.

For a fixed K, put t_K=C_L^K(0). The exact C-even index says the
stationary mean of its edge duration t_K/2 is K pk(E) on each invariant
class. Consequently

    sum_E q_(r,L)(E)t_K(E)/2=K M_L.                      (13)

For each E, at most t_K/2 permitted integer offsets satisfy 2j<t_K.
Summing (12) and using (13) gives

    P_inc,c(2j<t_K | B_L)<=K M_L/mu_(r,L,c)=o(1).         (14)

Next let Delta_K=C_L^K(b_0)-b_0. The endpoint map Q_L is a bijection
of physical selection events: C and T are commuting bijections, and
Q_L goes from even starts to odd endpoints. Use the finite physical
lift if necessary; these maps are equivariant under spatial translation
and descend to canonical roots. The measure q_(r,L) is PHI-invariant,
not merely tau-invariant: its weight and domain depend on sizes, peak
counts and height, all invariant under the physical update. Hence the
Q_L endpoint permutation preserves this reference measure even when it
switches tau components. It follows that

    sum_E q_(r,L)(E)Delta_K(E)=2K M_L.                   (15)

This is an unconditioned reference transport. In the actual base Palm
sum keep the short-base weight, bounding it by H_c+2. For every fixed
delta>0, Markov's inequality and (15) then yield

    P_inc,c(Delta_K>delta sqrt(r) | B_L)
       <=2K(H_c+2)M_L/[delta sqrt(r)mu_(r,L,c)]
       =o(1).                                          (16)

Thus the first fixed K deep boundaries occur before the sampled edge,
and the K additional deep C clocks AFTER the odd base endpoint have
duration o(sqrt(r)) in the actual incidence law. Bottom clocks have
not been approximated or expanded. All statements concern the finite
nonempty core D_L.

## 4. Exact extra-slot collar probability, with a uniform tail bound

Fix S>=K>=1 independently of r. On B_L expose

    E_L=(full original profile, all rows u>=L, offset j).

Rows u<L are the independent exact base-zero compositions. Define the
original-coordinate collar event

    A_(S,K,L)={Z_(u,-u-i)=0:
                         S<=u<L, 1<=i<=K}.               (17)

These are the K slots immediately after the u+1 base-forced coordinates
in each row. On the profile domain they are distinct free coordinates.
Writing P_u=p_u-u-1, its exact conditional probability is

    Q_(r,S,K,L)=product_(u=S)^(L-1)
                     (P_u-1)_K/(ell_u+P_u-1)_K.          (18)

For each fixed upper depth m, finite-depth profile concentration gives
the usual fixed-parameter limit for the product S<=u<m. We must also
control the rows between m and L; they cannot be replaced uniformly by
a geometric oracle.

On A_r, P_u>=a_(u+1) and P_u>=2 for u<L, for all large r. Another exact
summation by parts, using ell_u=d_u-d_(u+1), gives

    sum_(u=m)^(L-1) ell_u/a_(u+1)
      =d_m/a_(m+1)-d_L/a_L
        +sum_(u=m+1)^(L-1)d_u^2/[a_u a_(u+1)]
      <= C_1/m.                                        (19)

The last step follows from (4)-(5). For a free coordinate of row u,
its nonzero probability is ell_u/(ell_u+P_u-1)<=2ell_u/P_u. A union
bound over the K collar slots and (19) therefore bounds the conditional
probability of any collar failure at depths m,...,L-1 by C_2 K/m.

First take r to infinity for fixed m,S,K, then m to infinity. The finite
product limit and this uniform tail bound prove that (18) converges in
probability, under the ACTUAL E_L marginal, to

    product_(u=S)^infinity [1-1/(u+2)^2]^K
                        =[(S+1)/(S+2)]^K.                (20)

It also converges in mean, being bounded by one. The probability of
A_r^c under incidence is o(1), since the incidence density over the
original root law is O_c(sqrt(r)). This handles the exceptional profiles
in (19)-(20). No uniform growing-depth approximation of ell_u/P_u was
used; only the exact composition and the deterministic tail estimate.

## 5. The finite reverse grouping proves eligibility

At depth u the chronological zero-gap expansion of a word with u+k C
nodes and one T node queries the prefix 0,-1,...,-(u+k). The base
triangle supplies its first u+1 zeros, and the collar (17) supplies
the remaining k<=K. Thus on A_(S,K,L), the candidate word from depth S
has the formal endpoint expansion

    C_S^(S+k)T_S  ->  C_L^(L+k)T_L.                     (21)

We only use this as a physical identity AFTER its finite depth-L
endpoint passes the cutoff. By commutation that endpoint is

    b_k=C_L^k(b_0),              0<=k<=K.

Equations (14)-(16), with a fixed margin smaller than 2(C-c), imply
with probability 1-o(1) under (12) that

    t_K<=2j,       b_K<=2H_C+1.                          (22)

The latter also bounds every smaller b_k. All groups in (21) then lie
inside the tested safe horizon, so the accepted reverse grouping
identifies them with the actual depth-S words.

The first k C boundaries themselves agree at depths S and L: at every
intervening row their first k incoming coordinates are base-forced zero,
since k<=K<=S. Therefore t_k=C_S^k(0)=C_L^k(0). The candidate word from
the boundary t_k has endpoint b_k by commutation. It is short because
b_k-t_k<=b_K<=2H_C+1; it covers the sampled edge because

    t_k<=t_K<=2j,                 b_k>=b_0>=2j-1.

The event (22) is E_L-measurable and has probability 1-o(1). Combining
it with (18)-(20) shows that its intersection with the collar has
probability tending to [(S+1)/(S+2)]^K. Finally restore B_L's o(1)
exception. This proves the limiting lower bound (1).

Equivalently, if A_S is the actual deep eligibility set in
`PBBS_COMMON_DEEP_BOUNDARY_SHIFTED_ZERO_TRANSFER_20260908.md`, then

    liminf_(r->infinity) P_inc,c({0,...,K} subset A_S)
                                      >=[(S+1)/(S+2)]^K,

and for each fixed K the right side tends to one as S tends to infinity.

This is an actual probability/number-of-eligible-boundaries statement.
It uses a growing but finite retained base fibre to control late times,
not an infinite prefix oracle endowed with a physical endpoint. The
remaining lower-row shifted-zero survival problem is separate. Neither
independence of those survival events nor L_0-divergence follows from
the eligibility statement alone.

## 6. Initial boundary times have no repeated labels or visit corrections

There is a stronger initial-time consequence of the same weighted flux.
For every fixed delta>0, (12)-(13) and Markov give

    P_inc,c(t_K>delta sqrt(r) | B_L)
       <=2K(H_c+2)M_L/[delta sqrt(r)mu_(r,L,c)]=o(1).      (23)

Thus t_K=o(sqrt(r)) in actual incidence probability. In fact a smaller
time scale is available, without any Gaussian-height truncation. Take
eta=1/8 in (10). It yields M_L=O(r^(-3/20))+o(r^(-A)) for every fixed
A in the superpolynomial exceptional term. Hence

    P_inc,c(t_K>=L | B_L)
       <=2K(H_c+2)M_L/[L mu_(r,L,c)]
       =O(r^(-1/20))+o(1).                               (24)

On B_L, h>=2L. At every depth v<=L the reached height is h-v>=L, so
any two selections of one original physical label are separated by at
least 2L+1 physical updates. On t_K<L there are therefore NO repeated
labels in [0,t_K], simultaneously in all the trajectories D_v, v<=L.

To state the consequence without a position-convention ambiguity, define
the ORIGINAL initial particle-position map I_s on integer lifts by

    I_s(0)=0,
    I_s(j)-I_s(j-1)
       =2Z_(s,j)+1+epsilon_(s,j),
    epsilon_(s,j)=1{the original core bits j-1 and j differ}.

Extend periodically by I_s(j+p_s)=I_s(j)+n_s, where n_s=2r_s+1.
This is exactly the map called C_s in Section 2 equations (4)-(6) of
`/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`.
That source's exact formula is

    lambda_s(t)=I_s(lambda_(s+1)(t))
       +M_(s+1,lambda_(s+1)(t))(t) modulo n_s,            (25)

where M counts selections at times 0<=u<t, EXCLUDING the current
update. The physical edge position has a minus one and the omitted-site
formula adds one; these cancel in (25). There is no further +1.

On the no-repeat event, the label selected at t_k has not been selected
previously in [0,t_k). Consequently the M term in (25) is zero for
every k<=K and every s<L. The initial shifts are therefore exactly
nested STATIC original insertion maps:

    lambda_L(t_k)=-k modulo n_L,
    lambda_s(t_k)=I_s(lambda_(s+1)(t_k)) modulo n_s.       (26)

For any fixed S>=K, the same t_k are the first k C_S boundaries, as
explained in Section 5; the equality of these initial C boundaries
requires only the base forced zeros and NO collar event.

The original deep-core bits at sites 0,-1,...,-K are also zero with
probability 1-o(1), for every fixed S>=K. Indeed these sites are selected
at even times t_k, without earlier selections in [0,t_k). Before a
site's first selection, its bit has been complemented exactly t_k
times. Since t_k is even and the selected bit is zero, its original
bit was zero. This is a condition on D_S itself, hence E_S-measurable;
restricting to it does not change the exact conditional upper-row
composition law.

Each I_s is strictly increasing on its integer lift, with increments
at least one. Thus the recursively chosen integer representatives in
(26), starting at -k, satisfy for k<l<=K

    lambda_s(t_k)-lambda_s(t_l)>=l-k                    (27)

when read as those lifts. For a fixed row, sufficiently separated
indices therefore have disjoint extended query intervals on the line.
There is also a DETERMINISTIC cyclic guard, due to appendix_a. Periodicity
and positive increments give the following for the static lifts
j_S(k)=-k and j_s(k)=I_s(j_(s+1)(k)):

    n_s+j_s(k)
      =I_s(n_(s+1)+j_(s+1)(k))
      >=n_(s+1)+j_(s+1)(k)>=n_S-k.                      (28)

This follows inductively from j_S(k)=-k; both complementary arcs expand
under insertion. Consequently, for every row u<S and k<=K,

    j_(u+1)(k)-u
      >=-n_(u+1)+n_S-K-u > -n_(u+1),                  (29)

because the safe domain has n_S>=2S+1 and K<=S. All these query blocks
lie in the same fundamental interval (-n_(u+1),0]. Their integer-lift
union therefore has EXACTLY its cyclic cardinality for every upper-row
realization. No no-wrap conditioning or probabilistic wrap error is
needed for the fixed collection of boundaries.

For completeness, the following stronger tightness observation remains
useful independently of the deterministic cyclic guard.

Fix S,K and define static lifts j_S(k)=-k and
j_s(k)=I_s(j_(s+1)(k)) on ALL original arrays, before restricting to the
no-repeat event. Put B_s=-j_s(K)>=0. Conditional on the deeper rows and
the full profile in the exact base-S fibre, B_(s+1) and the original
epsilon bits are known. Every free row-s coordinate has exact mean
ell_s/P_s, and the forced ones have mean zero. Summing the defining
increments of I_s therefore gives

    E[B_s | deeper rows,profile]
                         <=2(1+ell_s/P_s)B_(s+1).        (30)

This remains valid for a winding input, since linearity counts any
repeated coordinate with its multiplicity. On a fixed-depth typical
profile, all ell_s/P_s are uniformly bounded. Iterating (30) gives
E[B_s|E_S,profile]<=C_S K, uniformly over its allowed deep core, for
the finitely many intermediate rows. Hence the B_s are tight as r tends
to infinity. All row circumferences p_s tend to infinity, so with
probability 1-o(1) none of the extended row-s query intervals for
0<=k<=K crosses the cyclic boundary at -p_s. Their integer-lift unions
then have exactly their cyclic cardinalities.

This estimate is made in the unchanged composition fibre. Only AFTER
proving it do we intersect the high-probability no-repeat event, on
which j_s(k) equals the physical shift. No freshness assertion has
been conditioned on no-repeat. For this fixed collection of depths and
boundaries, (27)-(29) already justify using linear separation to distinguish
the physical query slots deterministically.

This corollary removes the dynamic VISIT COUNTS from the finite common-
boundary shifts with probability 1-o(1). The original bits in I_s still
belong to the original core; no independent bit law has been asserted.
Any renewal or joint shifted-zero law derived from the nested insertion
maps requires its own proof. No such law or L_0-divergence is included
in this corollary.
