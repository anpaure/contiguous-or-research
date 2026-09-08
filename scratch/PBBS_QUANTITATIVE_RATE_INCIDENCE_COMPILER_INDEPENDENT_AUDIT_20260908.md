# Quantitative PBBS rate: independent incidence and compiler audit

2026-09-08. Pure proof and source reads; no mathematical computation.
This audits sections 5–6 of
USER_PBBS_QUANTITATIVE_RATE_CLAIM_20260908.md, including the transition
from the conditional vector law to the actual incidence measure. It also
supplies explicit collar, exterior, and compiler constants.

**Verdict:** these transitions pass. There is no missing incidence
normalizer and no need to identify a reached root with a fresh root.
The uniform short-incidence estimates and quantitative vector/flux
estimates are upstream inputs, proved with explicit constants in
PBBS_QUANTITATIVE_CUTOFF_UNIFORMITY_AND_EXPLICIT_CONSTANTS_INDEPENDENT_AUDIT_20260908.md
and PBBS_QUANTITATIVE_VECTOR_RENEWAL_AND_FLUX_EXPLICIT_CONSTANTS_20260908.md.
Their separate proof records supply the numerical constants used below.
The later stronger terminal-charging rate is independently audited in
PBBS_TERMINAL_CHARGING_COMPILER_AND_DYADIC_RATE_INDEPENDENT_AUDIT_20260908.md.

## 1. Exact conditional fibre, with the actual incidence weight retained

Let t be an integer lifetime cutoff, R=sqrt(r), and

    I_t(f)=E_D[1{T<=t} sum_{j=0}^{T+1} f(D,j)],
    mu_t=I_t(1).

The exact physical birth dictionary and double counting give

    |U_t|/W_r=I_t(1/K_t).

Here K_t is congestion in the SAME all-birth cutoff family. On an atom
of this incidence measure, K_t>=1. Thus discarding a set of raw
incidence mass e costs at most e in the displayed identity.

The relevant original source is
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md,
especially sections 3–4, equations (8) and (12).
On the safe profile domain and the zero base triangle F_L=0, that source
proves the exact identity

    T=a_L(E_L),   E_L=(full profile, all rows >=L).

The lifetime and permitted-offset tests therefore inspect E_L and j only.
Conditional on them, every row s<L is still an independent uniform
composition in its free slots, with the s+1 prescribed base slots zero.
The apparent lifetime weight T+2 cancels against uniform offset selection;
each allowed pair (D,j) has the same original-root mass.

The extra collar in rows S,...,L-1 is consequently tested in this
unchanged composition fibre. After those rows are exposed or restricted,
the rows below S retain exactly their base-zero composition law.
The actual marginal law of E_S is retained throughout.

The clock/no-repeat restrictions are also E_S-measurable. On F_L=0,
the first K common boundaries agree at levels S and L. Their clock
times and the extra endpoint time can be read at level L. The profile
condition h>=2L and t_K<L prevent a repeated selected label in the
entire time interval, at every level through L, for EVERY upper-row
completion. This avoids conditioning on a realized lower-row success.
The collar and the base lifetime margin t-T>=q likewise inspect E_S.

It follows that a pointwise conditional total-variation bound eta for
the lower-row success vector integrates to at most mu_t*eta in raw
incidence. No division by mu_t, nor a lower bound on mu_t, is needed.
The renewal reciprocal expectation integrates in the same way.

## 2. An explicit raw error ledger

Let M_L be the stationary unnormalized weighted peak mass and retain
the exact finite clock identities

    sum_E q(E)t_K(E)=2K M_L,
    sum_E q(E)Delta_K(E)=2K M_L.

They hold for each finite integer K: the clock endpoint maps are
bijections, and composing them K times preserves the same stationary
reference measure. There is no fixed-K limit in these identities.
The precise stationary measure and endpoint transport are in
PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md and
PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md.

For t<=H_*, the following are raw incidence bounds:

    I_t(t_K>=L)       <=2(H_*+2)K M_L/L,
    I_t(2j<t_K)      <=K M_L,
    I_t(Delta_K>q)   <=2(H_*+2)K M_L/q.                 (1)

In the middle line t_K is even, so there are at most t_K/2 admissible
integer offsets with 2j<t_K. In the other lines the count of all allowed
offsets is at most H_*+2.

These bounds use the full stationary reference measure FIRST.
One must not condition that measure on an additional nonstationary
profile event before invoking its clock identities. Restricting to
regular profiles afterward only reduces the bad-atom sums.

Write e_base for the raw mass removed by F_L>0, BAD, and profile
irregularity; eta for the conditional vector TV error; rho_K for the
reference renewal reciprocal expectation. Then the exact proof gives

    |U_t|/W_r
      <= mu_t(rho_K+eta+192K/S)
          +e_base
          +2(H_*+2)K M_L/L +K M_L+2(H_*+2)K M_L/q
          +I_t(0<=t-T<q),                              (2)

under the profile margins stated in the next section. The constant
192 can be replaced by any larger constant. Successful phases on the
remaining atoms are distinct native physical births, contain the sampled
edge, and have lifetime at most T+q. Thus the last margin really places
them in the SAME cutoff family counted by K_t. No cross-cutoff reciprocal
identity is being substituted for the first identity in section 1.

## 3. Explicit collar constant

Write a_u=r_u, d_u=a_u-a_(u+1), and ell_u=d_u-d_(u+1).
Assume the regular-profile inequalities

    3r/[4(u+1)] <= a_u <=5r/[4(u+1)]   (0<=u<=2L+2),

and r>=(4/3)L(L+1), with 1<=K<=S<L.
Convexity and comparison to a_floor(u/2) give

    d_u<=8r/(u+1)^2   (u>=1).

For u=1 this follows from d_1<=r. For u>=2, use
d_u<=a_floor(u/2)/(u-floor(u/2)) and distinguish the two parities.

The exact Abel identity gives

    sum_{u=S}^{L-1} ell_u/a_(u+1)
      =d_S/a_(S+1)-d_L/a_L
         +sum_{u=S+1}^{L-1} d_u^2/[a_u a_(u+1)].

The first positive term is at most16/(S+1). Each interior term is at
most (512/3)/(u+1)^2, and the sum of 1/(u+1)^2 over u>=S+1 is at
most1/(S+1). Consequently

    sum_{u=S}^{L-1} ell_u/a_(u+1)
         <=560/[3(S+1)] <=192/S.                       (3)

The free composition has P_u=2a_(u+1)-u slots, so
P_u-1>=a_(u+1) under the displayed size condition. A specified free
slot is nonzero with probability
ell_u/(ell_u+P_u-1)<=ell_u/a_(u+1). All K extra slots are distinct:
P_u-1>=a_(u+1)>=u+1>=K+1. The union bound and (3) prove conditional
collar failure at most192K/S. Section 1 therefore proves its raw
incidence cost at most192(K/S)mu_t.

## 4. Cutoff averaging is in the correct measure

Let Hset be all integers from ceil(cR) through floor((c+1)R).
For R>=2 its size is at least R/2. Fix an original birth with lifetime T.
It contributes its weight T+2 to the strip for at most q+1 choices
of t in this set. Summing first over t and then over births yields

    average_t I_t(0<=t-T<q)
       <=2(q+1)mu_floor((c+1)R)/R.                     (4)

This is an unnormalized finite counting identity. It does not average
different normalized Palm probabilities as though their laws agreed.
For q=ceil(R*r^(-1/100)), the bound in (4) is at most
6r^(-1/100)mu_floor((c+1)R). Since every other term in (2) has a
uniform upper bound on this aperture interval, at least one t satisfies
their common upper bound plus (4). This is the required same-family
occupied-support estimate.

## 5. Explicit exterior constant: 1024

The finite exterior construction is
MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md,
Theorem 1.3. Its proof can be made numerical without changing the
construction. Let m>=1, 0<=h<=m-1, and use the source's variable x.
Elementary central-binomial bounds imply

    2^m W(m)/W(2m)<=2,
    W(m)^2/W(2m)<=2/sqrt(m).

For completeness the width bounds used here are
2^n/sqrt(2(n+1))<=W(n)<=2^n/sqrt(n+1).
Put p_j=binom(2j,j)/4^j. Its adjacent ratio is
(2j+1)/(2j+2). Induction gives p_j>=1/(2sqrt(j)) for j>=1 and
p_j<=1/sqrt(2j+1) for j>=0: after squaring, the two required ratio
comparisons differ by exactly1 in their integer numerators.
The normalized widths in dimensions2j-1 and2j both equal p_j,
which proves the displayed width bounds.

The source's split at floor((h+1-epsilon)/2) has a first part at most
4exp(-h^2/(8m)) after normalization. For the ordinary second-part
terms, its bound (1.18) gives

    32/[m sqrt(m)] *exp(-h^2/(8m))
        *sum_{x>=0}(x+1)^2 exp(-x^2/(2m)).

For m>=1 the sum is at most13m^(3/2). Indeed its x=0 term is1, and
the remaining sum is bounded by

    integral_0^infinity (u+2)^2 exp(-u^2/(2m)) du
      =sqrt(pi/2)m^(3/2)+4m+4sqrt(pi m/2).

Using pi<4 bounds the sum by
1+(3/2)m^(3/2)+4m+6sqrt(m)<=13m^(3/2).
Thus these ordinary terms cost at most416 times the exponential.

The exceptional x=floor(m/2) term is at most4m/2^m before extracting
the exponential. Since h<=m, the resulting prefactor is at most
4m(e^(1/8)/2)^m. The elementary e^(1/8)<=8/7 bounds this by
4sum_{m>=1}m(4/7)^m=112/9<13.
The total even normalized constant is therefore at most433<512.

The one-coordinate lift and
W_r=(2r+1)/(r+1)*binom(2r,r) now give the fully finite bound

    2L_r(r-H)/W_r
          <=1024 exp(-(H-1)^2/(8r)),                  (5)

for r>=1 and 1<=H<=r. This has no large-r threshold.
The exterior family is empty beyond its specified range.

## 6. Packing, exact compiler constants, and parity

Suppose the uniform low-height birth estimate is

    Pr(T<=floor((c+1)R),h<epsilon R)
      <=L0 exp(A0(c+2)^2) R^(-1) exp(-b0/epsilon^2).

Every other packed trace contains at least epsilon R distinct edges.
For the selected cutoff, if u_t=|U_t|/W_r, then

    R P_t/W_r
      <=L0 exp(A0(c+2)^2)exp(-b0/epsilon^2)+u_t/epsilon. (6)

Distinctness requires only t+2<2r+1, which follows for the stated
apertures once 2(t+1)<=r+1. The source's compiler, including its tail
rank boundary and all collars, is precisely
PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md,
sections 3–5. With H=t+1 it gives

    nu(2r+1)/W_r
      <=1+(c+2)/R+10(c+2)R P_t/W_r+1024exp(-c^2/8),  (7)

provided 2H<=r+1. The last estimate uses t>=cR.
No extra seam charge occurs when appending the exterior word.

For example, suppose (2)–(4) have given

    u_t<=U exp(A0(c+2)^2)(loglog r)/log r.

Put y=loglog r and epsilon^2=b0/(2y), in its allowed range.
All packing and compiler prefactors are absorbed by

    A=A0+1+(1/9)log_+[10(L0+U sqrt(2/b0))],             (8)

giving the middle term exp(A(c+2)^2)y^(3/2)/log r.
Here c>=1 implies c+2>=3, and x<=exp(x^2) for x=c+2.
This quantifies how an upstream raw/flux constant enters the final
exponent. A larger A is always allowed.

The trimmed one-coordinate lift has exactly twice the old length and
W(2r+2)=2W_r. It preserves this normalized inequality exactly.
This step has no dimension-dependent loss or extra o(1) term.

## 7. Numerical assembly from the separately supplied upstream bounds

The coordinator supplied the following separately proved numerical inputs,
all for r>=2^1000000:

    A0=2^80 exp(2^20),   b0=2^-53,
    E=exp(A0(c+2)^2),
    M_L<=11000000 r^(-3/20),
    eta<=8r^(-1/100),
    rho_K<=600(1+loglog r)/log r.

The other inputs are mu_t<=E, early-triangle raw mass<=E r^(-1/5),
the stated E-weighted low-height estimate with b0, and negligible BAD
and profile-irregular raw mass. This paragraph is a numerical-input
interface, not an independent proof of those upstream bounds.

With K=floor(r^.01), S=floor(r^.02), L=floor(r^.4), and
q=ceil(r^.49), section 2 gives the three clock losses at most

    44000000(c+3)r^(-.04),
    11000000r^(-.14),
    22000000(c+3)r^(-.13).

The collar loss is at most384E r^(-.01). Since c+3<=E, their sum
together with TV, early triangle, and the negligible terms is bounded
by2^28 E r^(-.01). Section 4 adds at most8E r^(-.01).
Putting y=loglog r, the renewal term is at most1200E y/log r.
At the stated threshold r^(-.01)<=y/log r, so the conservative bound

    u_t<=2^40 E y/log r                               (9)

follows. Indeed, with x=log r>600000, e^(x/100)>=x follows from its
quadratic Taylor term, and y>=1.

For epsilon^2=b0/(2y), one has epsilon^-1=2^27 sqrt(y) exactly.
Thus (6) is at most2^68 E y^(3/2)/log r. The compiler factor satisfies

    10(c+2)2^68 <= exp(128(c+2)^2).

For instance its logarithm is at most71+(c+2), using log2<1,
log10<3 and log(c+2)<=c+2; this is below128(c+2)^2 for c>=1.
Consequently A_req=A0+128 suffices in the proposed displayed bound.

The profile/domain guards do not introduce a growing-cutoff loss here.
Writing x=log r, the profile relative error is at most
5exp(-x/10)(4+sqrt(1200x)), which is <=1/4 already for x>=1024.
Also r>=(4/3)L(L+1), r_L>(c+3)R, K<=S<L,
epsilon<=1<=epsilon R, and2(t+1)<=r+1 hold at the stated threshold.
The r_L inequality even permits the full horizon T+q before using the
cutoff-margin restriction.

## 8. Algebra audit of the proposed completely numerical threshold

Suppose the independently supplied upstream constants permit

    A=2^(2^21)=2^2097152.

This A indeed dominates the previous section's A_req.
Since log2>=2/3 and log2<=1,

    log A >=(2/3)2^21 >2^20+81 >=log(2A0).

Also A0>=128, so A>=2A0>=A0+128.

Set

    gamma=1/(256A)=2^(-2097160),
    k0=ceil(exp(exp(8192A)))
      =ceil(exp(exp(2^2097165))).

For k>=k0 and the corresponding odd source dimension 2r+1, one has
r>=sqrt(k) and
y=loglog r>=8192A-log2>=4096A.
Choose c=sqrt(y/(16A)). Then c>=2 and
exp(A(c+2)^2)<=exp(y/4). The three excess terms in (7), after the
packing substitution, are each at most one quarter of exp(-gamma y):

* 1024exp(-c^2/8)=1024exp(-2gamma y), since
  gamma y>=16>log4096;
* y^(3/2)exp(-3y/4), since gamma<=1/256 and y>=16;
* (c+2)/R, since c+2<=2sqrt(y) and R=exp(exp(y)/2).

For the middle comparison, log y<=y/4 when y>=16, so its ratio to
exp(-gamma y) is at most exp(-95y/256)<1/4.
For the cycle comparison, exp(y)>=4y gives R>=exp(2y);
then 2sqrt(y)exp(-(2-gamma)y)<1/4 for y>=16.

Finally log r>= (log k)/2 and 2^gamma<=5/4. Hence the sum is at most
(15/16)(log k)^(-gamma), and in particular the final multiplier C=1
is valid. This verifies the threshold algebra, not the separate task
of proving that the proposed A dominates every upstream numerical
constant and that their finite validity thresholds lie below k0.

## 9. Claim boundary

The exact conditional law, raw incidence transfer, same-family aperture
selection, packing conversion, literal compiler, and parity passage do
not add a qualitative gap to the proposed rate. The uniform growing-cutoff
raw bounds and quantitative flux/vector estimates have the separate
proof records linked at the beginning. The displayed proof-package checks
reported by the user were not available or rerun in this audit.
No statement here proves nu(k)=B(k), even when the quantitative rate is
accepted.
