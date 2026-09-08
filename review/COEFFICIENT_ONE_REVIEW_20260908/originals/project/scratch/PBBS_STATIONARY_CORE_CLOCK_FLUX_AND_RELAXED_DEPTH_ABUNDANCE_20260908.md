# Stationary core-clock flux and relaxed depth abundance

2026-09-08. Pure proof; no mathematical execution. Appendix_a deduction.
Independent direct-route full-file audit: PASS, including stationary
transport, label sums, clock indices, and the relaxed-abundance scope.
Root full-file audit, including the original structural clock and native
repair-congestion sources: PASS. The fixed original size and actual short-clock
Palm law are retained throughout.

The new conclusions are an exact backward-age formula for the depth-two
distinct-label count, an exact unrestricted clock congestion, and a growing
RELAXED depth-S phase count. The last count does not yet pull back to many
actual depth-two zero-feasible phases.

## 1. Sources and exact stationary reference measure

Use the fully audited notes

* `PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`;
* `PBBS_ZERO_OR_ONE_FEASIBILITY_AND_DISTINCT_LABEL_RECIPROCAL_20260908.md`;
* `PBBS_BAD_PARTNER_UNION_TRANSFER_AND_ZERO_ONLY_FEASIBILITY_20260908.md`;
* `PBBS_HEIGHT_FREE_INTERVAL_STABBING_AND_RECIPROCAL_EQUIVALENCE_20260908.md`.

The physical edge/clock conventions also follow the exact structural
source `pbbs_gaussian_clock_genealogy_structural_audit.md` and stationary
source `pbbs_stationary_lifetime_identities.md` in worktree c69c. Original
label transport is equation (3) of `pbbs_original_array_shift_cocycles.md`
in worktree e333.

Fix original size r, constants 0<c<=C, H_c=floor(c sqrt(r)),
H_C=floor(C sqrt(r)), and a fixed integer S>=2. For a nonempty core E
write t=|E| and k=pk(E). Retain the domain

    t>H_C,                    height(E)>=S.                 (1)

This is invariant under the rooted physical shift tau=phi^2. Its stronger
partner-cutoff circumference requirement changes the actual safe base
event by o(1), for fixed S,c,C as r tends to infinity.

Let W_(r,S)^GOOD(t,k) be the EXACT upper-completion count from the
Narayana-core note, including GOOD and the base zero triangle. Define a
finite, generally subprobability measure on cores by

    q_(r,S)(E)=W_(r,S)^GOOD(t,k)/Cat_r *1_(domain (1)),
    z_(r,S)=sum_E q_(r,S)(E).                              (2)

Every size/peak/height class is tau invariant. Since (2) is constant on
each such class, q_(r,S) is stationary under tau. This stationarity is
obtained AFTER summing the upper fibres. The original event that its
canonical triangle is zero need not itself be invariant under tau.

For the chronological core word Q_S=C_S^S T_S define

    a_S(E)=(endpoint(Q_S at physical time 0)-1)/2.

The exact fibre identifies the restricted actual base-incidence law with

    P(E,j)=q_(r,S)(E)/mu_(r,S,c)
             *1{a_S(E)<=H_c, 0<=j<=a_S(E)+1},             (3)

where

    mu_(r,S,c)=sum_E q_(r,S)(E)
                          (a_S(E)+2)1{a_S(E)<=H_c}.       (4)

This is the original fixed-r law, conditioned on its safe zero-triangle
event. In particular mu_(r,S,c)/mu_c tends to one for each fixed S. No
Boltzmann or independently refreshed core law is used.

## 2. Move the sampled edge to time zero

For a core F and H>=0 put

    K_(S,H)(F)=sum_(u=0)^(H+1)
       1{u-1<=a_S(tau^(-u)F)<=H}.                         (5)

These are actual even core birth phases whose Q_S clock has duration at
most 2H+1 and whose inclusive edge interval contains the current edge.
The phase at age u was born at physical time -2u. Set

    J_(S,C)(E,j)=K_(S,H_C)(tau^j E).

For S>2 this is a RELAXED core phase count: it has not tested the actual
intermediate original rows 2,...,S-1. For S=2 it is exactly J_0 on the
safe depth-two fibre, since sum zero is composition-admissible there.

For every function f of the shifted core, stationarity in (2) gives the
exact finite identity

    E_(3)[f(tau^j E)]
       = [sum_F q_(r,S)(F) K_(S,H_c)(F) f(F)]
                                                    /mu_(r,S,c). (6)

Indeed substitute F=tau^j E into each summand of (3). Its survival test
becomes j-1<=a_S(tau^(-j)F)<=H_c, and j runs from 0 to H_c+1.

Since K_(S,H_C)>=K_(S,H_c), equation (6) implies

    E_(3)[1/J_(S,C)] <= z_(r,S)/mu_(r,S,c).                (7)

The summand with zero base congestion is interpreted as zero. When C=c,
there is the exact identity

    E_(3)[1/J_(S,c)]
      = [sum_F q_(r,S)(F)1{K_(S,H_c)(F)>0}]
                                                    /mu_(r,S,c). (8)

Thus (7) uses the stationary reference mass, not an asserted uniform
distribution at a moving original root.

## 3. An exact formula for the distinct depth-two labels

Specialize to S=2 and fix a shifted core F. Set n=2|F|+1 and, for
0<=u<=H_C+1, define

    e_u=1{u-1<=a_2(tau^(-u)F)<=H_C},
    b_0=0,
    b_u=sum_(v=1)^u omega(tau^(-v)F) modulo n.             (9)

Here omega(G)=|R|+1 if G=P1Q0R is its first-maximum, first-return
factorization; lengths are numbers of letters. The exact signed shift
cocycle says b_u is the ORIGINAL core label selected at physical time
-2u, measured relative to the current selected label zero. There is no
replacement of b_u by -u and no deletion of its possible spatial wraps.

Consequently the distinct zero-feasible label count is exactly

    L_0(F)=|{b_u:e_u=1}|.                                 (10)

The audited strict interval bound gives at most two eligible ages for
each label. Hence there is also the exact two-time expression

    L_0(F)=sum_u e_u
              -sum_(u<v) e_u e_v 1{b_u=b_v}.              (11)

Combining (6) with (10) or (11) gives its exact fixed-r Narayana-class
Palm distribution. For example its lower tail is

    P_(3)(L_0<=M)
      = [sum_F q_(r,2)(F)K_(2,H_c)(F)1{L_0(F)<=M}]
                                                    /mu_(r,2,c). (12)

This reduces distinct-label counting to a backward itinerary and explicit
modular sums in one stationary core. It does not make the summands or
their modular coincidences independent.

## 4. Exact clock flux and a finite congestion recursion

On one signed physical core trajectory, write C and T for the predecessor
and same-label endpoint maps. Strict adjacent-selection alternation makes
C bijective: each selection of label i-1 has exactly one preceding
selection of i paired to it. T is bijective by successive same-label
returns. C preserves time parity; T reverses it. They commute.

Thus, in edge time,

    c(d)=C(2d)/2,
    R_S(d)=(C^S T(2d)+1)/2                              (13)

are bijections of the signed integers. They commute with translation by a
physical period. In particular the full Q_S interval family has one birth
and one inclusive right endpoint at each edge.

The even-started C intervals have exact congestion k=pk(E). To see this,
consider the cyclic edge between labels i-1 and i. Selection at i changes
its incoming bits 00 to 10; until the next selection at i-1 both endpoint
bits are complemented together at each update. Selection at i-1 ends the
unequal interval. At an even observation time, this edge has pattern 01
precisely when that active C interval began at an even time. There are
exactly k cyclic 01 edges. This proves congestion k for intervals
(d,c(d)]. Bijection of c makes the congestion of [d,c(d)) the same.

The accepted native T repair intervals have exact congestion t+2. Split
the Q_S interval into its S half-open C stages and its final inclusive
native T interval. Endpoint bijectivity reindexes the starts of each
stage over every edge once. Therefore

    sum_d 1{d<=j<=R_S(d)}=t+Sk+2                       (14)

at every edge j. Long intervals here may have wrap multiplicities; they
are not asserted to be legal short partners. Averaging (14) over any
nonempty tau-invariant core class gives the additional exact identity

    E[a_S(E)]=t+Sk.                                      (15)

For a cutoff H, let B_H(d)=1{R_S(d)-d-1<=H}. With d_*(j) the unique birth
whose endpoint R_S(d_*(j))=j, the short congestion obeys

    K_H(j+1)-K_H(j)=B_H(j+1)-B_H(d_*(j)).                 (16)

This is an exact finite flux recursion, including the inclusive endpoint
convention. It does not supply a mixing or short-tail estimate.

## 5. The relaxed phase count really grows with depth

The reference mass in (2) is exactly the original uniform-root probability
of GOOD, domain (1), and F_S=0. For each FIXED S, original-depth profile
concentration gives

    p_s/r -> 2/(s+2),
    ell_s/r -> 2/[(s+1)(s+2)(s+3)]   for s<S.

Conditional on the full original profile, the rows are independent uniform
weak compositions. The probability that their s+1 distinct triangle slots
are zero is

    (p_s-1)_(s+1)/(ell_s+p_s-1)_(s+1),                    (17)

where the factorials fall. The fixed-S domain and GOOD have unweighted
probability tending to one. For example r_(2S) is positive with probability
tending to one, which supplies the height requirement. Bounded convergence
in (17) therefore gives

    z_(r,S) -> rho_S
       =product_(s=0)^(S-1)(1-1/(s+2)^2)^(s+1)
       =(S+2)^S/(S+1)^(S+1).                             (18)

The last identity follows by cancellation of the powers of each integer
in the product; rho_S is asymptotic to e/(S+1).

Put m_c=liminf_(r->infinity) mu_c>0, using the accepted retained-incidence
normalizer. Equations (7) and (18), and restoration of the o(1) safe
exception for each fixed S, imply for every fixed positive integer M

    limsup_(r->infinity) P_inc,c(J_(S,C)<=M)
                                     <= M rho_S/m_c.     (19)

Define J_(S,C)=1 on that exception if an everywhere-defined variable is
needed. In particular,

    lim_(S->infinity) limsup_(r->infinity)
                         P_inc,c(J_(S,C)<=M)=0.           (20)

This is a positive abundance statement for the RELAXED physical core
phases, proved under the actual original incidence law. The limits are
fixed S first, then r to infinity, then S to infinity. No uniform growing-S
estimate or interchange of these limits has been used.

## 6. The exact remaining pullback issue

For S=2, the relaxed count is the actual exposed J_0, and (10)-(12) give
L_0. For S>2, a phase counted in (5) need not have zero translated triangle
in its ACTUAL original rows 2,...,S-1. The accepted short forward/reverse
clock theorem pulls it back to a depth-two C_2^2 T_2 phase when those
coordinates are zero. The new zero-only theorem proves that all genuinely
depth-two feasible phases have these zeros with high probability; its
implication runs from actual feasibility to the deep test, not conversely.

The missing converse cannot be inserted into (20). In particular a large
number of relaxed core phases may still be lost upon exposing the actual
intermediate rows. Those rows must be sampled in their exact base-zero
fibre, with their moving original indices and shared coordinates retained.
Their individual zero probabilities decrease with the depth: the product
for disjoint newly tested triangle slots has the same order 1/S appearing
in (18). Thus the core abundance scale alone does not overcome the
pullback loss by an elementary independent-thinning argument.

No L_0 divergence, occupied-support decay, or improved compiler coefficient
is claimed. Equations (11), (16), and the actual relaxed abundance theorem
(20) are the new finite-count and mass-transport inputs.
