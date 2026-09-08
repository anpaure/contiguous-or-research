# Actual common-boundary shifted triangles have a recurrent renewal law

2026-09-08. Pure proof, no mathematical execution. Ternary_lift derives
the exact multipoint law from the new physical static-insertion interface.
Root, direct_route, and appendix_a independently checked the key slot-count
and deterministic arc arguments before this file was written. Root's
subsequent full-file audit passed. Independent direct_route and appendix_a
full adversarial audits also passed, including the native-partner and
final compiler implications. No correction was required.

The proof concerns ACTUAL shifted triangles at common deep C boundaries.
It does not identify them pointwise with original-index cones. It uses
all rows0,...,S-1, so a successful eligible phase is a native short
top-gap-zero PBBS partner. No virtual-row thinning is needed.

The dynamical input is the separately proved finite growing-depth flux
and eligibility theorem in
`PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md`.
The joint-law proof below does not assume independent survival indicators,
freshness after a failed test, or a renewal law at a reached root.

## 1. Exact base fibre and its measurable good sector

Fix0<c<C<infinity and put H_c=floor(c sqrt(r)), H_C=floor(C sqrt(r)).
Sample the ACTUAL incidence law of

    F_c={GOOD,Z_(0,0)=0,T<=H_c}.

For fixed integers S>=K>=1, retain the safe base zero triangle

    Z_(s,-u)=0, 0<=s<S, 0<=u<=s,

and expose E_S=(full original profile, all original rows u>=S, offset j).
The finite-layer incidence-fibre theorem proves that this restriction
has probability1-o(1). Conditional on each feasible E_S, rows s<S are
independent uniform weak compositions of ell_s into

    P_s=p_s-s-1, p_s=2r_(s+1)+1=n_(s+1)

free slots; the displayed s+1 base slots are fixed zero. There is no
additional lifetime weight or constraint on the free entries. The law
of E_S itself remains the original actual-incidence law.

Let t_k=C_S^k(0), 0<=k<=K, on the ONE original depth-S trajectory.
These are distinct even physical times, with selected original labels
lambda_S(t_k)=-k. The flux theorem's Section6 proves

    t_K=o(sqrt(r)) in actual incidence probability.

The actual safe-height bound, or its stronger growing-L version, makes
the following E_S-MEASURABLE good condition have probability1-o(1):

    t_K<2(h-S)+1, n_S>=2S+1,                         (1)

together with the fixed-depth safe profile margins. Every upper-level
completion has height h-s at depth s<=S. Its same-label return gap is
at least2(h-s)+1. Thus (1) prevents ANY repeated selected original label
in[0,t_K], simultaneously at all depths s<=S and for EVERY completion
in this fibre. Conditioning on(1) therefore leaves the exact upper-row
composition law unchanged. This is not conditioning on a realized
survival or a hidden upper-row no-repeat event.

At depth S the sites0,-1,...,-K have original bit zero. Each is first
selected at its even time t_k; before its first selection its bit has
been complemented exactly t_k times. This zero spine is part of E_S.

## 2. Actual shifts are initial insertion maps

Let I_s be the initial particle-position map on integer lifts, with

    I_s(0)=0,
    I_s(a)-I_s(a-1)=1+epsilon_(s,a)+2Z_(s,a),
    I_s(a+p_s)=I_s(a)+n_s,

where epsilon_(s,a) is1 if the two adjacent ORIGINAL depth-(s+1)
core bits differ, and0 otherwise. These maps are strictly increasing
and expand integer distances.

The exact physical cocycle is

    lambda_s(t)=I_s(lambda_(s+1)(t))
      +M_(s+1,lambda_(s+1)(t))(t) modulo n_s,

where M counts previous selections, excluding the current update.
On(1) its visit term vanishes at every t_k. Hence the actual shifts
are represented by the nested STATIC images

    xi_S(k)=-k,
    xi_s(k)=I_s(xi_(s+1)(k)), 0<=s<S.                (2)

The original insertion maps, including their epsilon bits, are used.
No independent law for those bits is asserted.

Define the full shifted-triangle indicator Y_k by

    Y_k=1 iff Z_(s,xi_(s+1)(k)-u)=0
                for every0<=s<S and0<=u<=s.         (3)

All indices in(3) are the actual original-array indices at time t_k.
The base gives Y_0=1.

## 3. Deterministic cyclic guard for every fibre completion

The composed insertion map from depth S to depth v sends0 to0 and
-n_S to-n_v. It expands each unit distance by at least one. Therefore

    n_v+xi_v(k)>=n_S-k, 0<=k<=K.                    (4)

For the row-s query interval

    J_s(k)=[xi_(s+1)(k)-s, xi_(s+1)(k)],

(4) and n_S>=2S+1, K<=S imply

    -p_s < xi_(s+1)(k)-s <= xi_(s+1)(k) <=0.         (5)

Thus all query intervals, including the forced base interval[-s,0],
lie in the SAME integer fundamental arc(-p_s,0]. Their unions have
exactly their integer cardinalities after cyclic projection.

This holds for every row configuration. No maximum-gap restriction,
no-wrap conditioning, probabilistic query cutoff, or growing-coordinate
geometric approximation is required.

## 4. Short-gap reset and long-gap separation

Fix i<j<=K and write g=j-i. Before row s is exposed, suppose the
row-u tests for Y_i have passed at every higher row u>s.

If g<=s+1, then

    xi_(s+1)(j)=xi_(s+1)(i)-g.                      (6)

Here is the exact static induction. At depth S the g+1 sites from-i
through-j are consecutive zero bits. At a higher row u>s, the successful
triangle at i forces its first g incoming coordinates to zero: the
required indices have offsets0,...,g-1, and g-1<=u. If the g+1 child
sites are consecutive zeros, their adjacent epsilon values are zero.
The insertion increments across those g gaps are consequently all1.
The inverse-pruning encoding sends each child site's recorded bit to
the same bit at its parent image. Their images are therefore again
consecutive zero sites in the parent. Descend
through rows S-1,...,s+1. This proves(6).

If g>=s+1, no success assumption is needed: distance expansion in(2)
gives

    xi_(s+1)(i)-xi_(s+1)(j)>=g>=s+1.                (7)

The two row-s intervals of length s+1 are then disjoint. Statements
(6)-(7) include the common boundary g=s+1 consistently.

This is the physical replacement for the invalid static-cone map.
Failures may shift later centers farther left, but they cannot shrink
a long separation. A prior success supplies exactly the short alignment
needed when intervals can overlap.

## 5. Exact finite conditional multipoint formula

Choose0=k_0<k_1<...<k_m<=K, and put g_a=k_a-k_(a-1). Define

    M_s=sum_(a=1)^m min(g_a,s+1), 0<=s<S.

Then, on every feasible good environment from Section1,

    P(Y_(k_1)=...=Y_(k_m)=1 | E_S,base triangle)
      =product_(s=0)^(S-1)
          (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s).       (8)

Factorials fall. Since M_s<=sum g_a=k_m<=K and the safe margins give
P_s>K, every ratio in(8) is within its ordinary stars-and-bars range.

Proof: reveal entire rows S-1,S-2,...,0. Conditional on higher rows,
all row-s centers are determined, and row s keeps its independent
base-zero composition law. On the event that all higher tests passed,
add the requested intervals in increasing k order, starting with the
base interval J_s(0). For a gap g_a<=s+1, (6) says the new interval
adds exactly g_a slots to the left of the previous leftmost interval.
For g_a>=s+1, (7) says it adds all s+1 slots. Earlier intervals lie
farther right and cannot change this count. By(5) there are no cyclic
coincidences. Exactly M_s NEW FREE row-s slots must therefore be zero.
Their uniform-composition probability is precisely the row ratio in(8).
It is independent of the locations and of all other higher-row data.
Iterating these conditional probabilities proves(8).

This computes all finite intersections of success events. It does not
claim that testing candidates chronologically leaves a fresh law after
failed tests; no such assertion is needed.

## 6. Fixed-depth limiting law and proper renewal

At every fixed S, the accepted original-profile concentration under
ACTUAL base incidence gives, in probability,

    ell_s/(ell_s+P_s) -> 1/(s+2)^2, 0<=s<S.

The finite safe and good exceptions above are o(1). Hence(8), integrated
over the unchanged E_S law, gives

    lim_(r->infinity) P_inc,c(all Y_(k_a)=1)
       =product_(a=1)^m u_(g_a,S),                 (9)

where

    u_(g,S)=product_(s=0)^(S-1)
                [1-1/(s+2)^2]^min(g,s+1).

For1<=g<=S this telescopes exactly to

    u_(g,S)=1/(g+1)*[(S+2)/(S+1)]^g.               (10)

One may verify it by dividing the g product by the g-1 product; the
tail ratio is g(S+2)/[(g+1)(S+1)]. In particular, with K fixed, sending
S to infinity in(9) gives the multipoint probabilities

    product_(a=1)^m 1/(g_a+1).                     (11)

These specify the renewal process begun at0 with renewal masses
u_n=1/(n+1). For completeness, write

    U(z)=sum_(n>=0)u_n z^n=-log(1-z)/z,
    F(z)=1-1/U(z)=1-integral_0^1 (1-z)^t dt.

The coefficient at n>=1 is

    f_n=-integral_0^1 (-1)^n binom(t,n)dt >=0,

because binom(t,n) has sign(-1)^(n-1) for0<t<1. Also f_0=0 and
F(1-)=1. Thus f is a probability distribution on finite positive
integer gaps, with renewal mass U=1/(1-F). Its regeneration identity
is exactly(11). Finite inclusion-exclusion determines every finite
binary indicator-vector law from its success intersections, so this
identifies the limiting law of the ACTUAL indicators, not only their
individual expectations.

Let R_K be its number of renewals in{0,...,K}. Since all interarrival
times are finite positive integers almost surely, R_K tends to infinity
almost surely. Consequently for every fixed integer M,

    lim_(K->infinity) P(R_K<=M)=0.                 (12)

Equations(9)-(12) use the order r->infinity first at fixed S,K, then
S->infinity at fixed K, then K->infinity. They require no uniform
growing-S approximation to geometric rows and no second-moment shortcut.

## 7. Eligible successes are native physical partners

Let A_S be the deep eligibility set from the transfer and flux notes.
For k in A_S, the depth-S word C_S^S T_S starting at t_k has endpoint
b_k satisfying

    b_k-t_k<=2H_C+1, t_k<=2j, b_k>=2j-1.            (13)

If Y_k=1, all shifted triangles through rows0,...,S-1 vanish.
Starting with this FINITE tested depth-S word, apply the accepted reverse
grouping C->C and T->CT at its actual chronological endpoints. At row
s it queries exactly the s+1 zero coordinates in(3), giving C_s^s T_s.
The profile circumferences exceed the entire horizon in(13), so these
groups are actual clocks, not formal infinite expansions. At depth0
this produces the native T clock of the original birth at t_k/2.

Its lifetime is (b_k-t_k-1)/2<=H_C. The row0 condition in(3) gives
its actual incoming top gap zero. GOOD is profile-measurable and
invariant under PBBS, so the shifted birth belongs to F_C. Its trace
covers the sampled edge j by the two endpoint inequalities in(13).

Different k give distinct even starting times, and on(1) even have
distinct original top labels. Thus, writing K_C for ACTUAL physical
partner congestion under the base-c incidence law,

    K_C >= sum_(k=0)^K Y_k
          whenever {0,...,K} is contained in A_S.   (14)

No row-one virtual feasibility, top-row thinning, or factor-two label
conversion is involved.

## 8. Abundance, occupied support, and the compiler consequence

The independently proved eligibility estimate states, for fixed S>=K,

    liminf_(r->infinity)
      P_inc,c({0,...,K} subset A_S)
          >=[(S+1)/(S+2)]^K.                      (15)

No independence from Y is assumed. By the union bound and(14),

    P_inc,c(K_C<=M)
       <=P_inc,c(sum_(k=0)^K Y_k<=M)
            +P_inc,c({0,...,K} not subset A_S)
            +o(1).                               (16)

For any fixed K, (9)-(11) and(15) make the limsup of(16), first in r
and then in S, at most P(R_K<=M). Send K to infinity and use(12).
Equivalently, given a desired error, choose K finite first, then S
finite, then r sufficiently large. This proves

    K_C -> infinity in ACTUAL base-c incidence probability
                     for every fixed0<c<C.        (17)

The partners remain in one fixed larger cutoff C; C does not grow
with r, S, or K. Taking C=2c suffices for every fixed c>0.

The deterministic cross-cutoff inequality in
`PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md` gives

    |U_c|/W <= mu_c P_inc,c(K_C<M)+mu_C/M,

with mu_c=Theta_c(1), mu_C=O_C(1). First let r tend to infinity using
(17), then M tend to infinity. Thus |U_c|=o_c(W). The accepted negligible
discarded-top-gap/BAD incidence bound extends this to all physical
births with T<=floor(c sqrt(r)). The occupied-support-to-packing theorem
then gives packing o_c(W/sqrt(r)).

Finally the already audited chain
`PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`
has no further compatibility premise: its literal erosion/cut compiler,
correct tail boundary, slow fixed-c diagonal, and opposite-parity lift
turn this physical packing conclusion into coefficient one.

This final deduction is to be accepted only together with the stated
finite core-law/flux/eligibility input and adversarial full-file audits.
The new point of this note is the exact ACTUAL multipoint law(8), with
measurable conditioning, deterministic arc separation, and native
partner realization. None of these conclusions follows from the old
original-index cone theorem alone.
