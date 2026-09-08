# Quantitative PBBS vector, renewal, and flux audit with explicit constants

Date: 2026-09-08.

Scope: independent pure audit of Sections 2--3 and the stationary-flux input of the user proposal transcribed in `USER_PBBS_QUANTITATIVE_RATE_CLAIM_20260908.md`. No mathematical computation or claimed inaccessible verifier was run. This note supplies explicit constants for these interfaces; it does not by itself prove the final quantitative OR-word theorem.

The sampling representation, complete-vector coupling, chosen K,S,L scales, and reciprocal renewal estimate pass. Their application to physical births retains the exact safe-fibre and no-repeat hypotheses stated below. Uniform raw physical incidence and early-triangle bounds are a separate input, audited by the induction agent; fixed-cutoff qualitative statements alone do not supply those bounds.

All logarithms in this note are natural. An explicit sufficient threshold throughout is

    r_0 = 2^(1,000,000).

The constants are deliberately loose.

## 1. Exact sampling representation and physical-law scope

For a uniform weak composition of ell into P parts, let B_i indicate that its ith coordinate is zero. For any j specified distinct coordinates, with j<=P-1, stars and bars gives

    Pr(all j indicators equal one)
      = (P-1)_j/(ell+P-1)_j.

These are exactly the joint success probabilities of draws without replacement from a population of N=ell+P-1 objects with P-1 successes. Inclusion-exclusion recovers every binary atom from its success intersections, so the entire first K<=P-1 indicator vector has that sampling law. This includes ell=0.

For each original row s<S use an independent length-K sampling vector with P=P_s=p_s-s-1 and ell=ell_s, and define

    Z*_k = product over s<S and max(1,k-s)<=j<=k of B_(s,j),
    Z*_0=1.

For indices 0=k_0<...<k_m<=K, the union of the corresponding row-s intervals has exactly

    M_s=sum_a min(k_a-k_(a-1),s+1)

coordinates. Therefore every joint success probability of Z* agrees with the exact actual shifted-triangle formula in Section 5 of `PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md`. Inclusion-exclusion gives equality of the complete conditional vectors. This is equality in distribution; actual shifted coordinates are not replaced pointwise by the auxiliary fixed windows.

The source formula is finite and can be used for growing deterministic S,K. It requires the following numerical and measurable hypotheses, rather than merely a fixed-parameter limiting statement:

- the original base triangle through S is zero;
- the complete profile and original rows at depths at least S, together with the sampled offset, are exposed;
- h>=2S and the required profile circumferences exceed the finite clock horizon;
- K<=S, n_S>=2S+1, and P_s>K;
- the first K common-boundary times satisfy the exposed-environment no-repeat test t_K<2(h-S)+1.

These conditions come from the actual shifted-triangle source and from `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`, Sections 1--4. On that finite domain, the conditional free rows are independent uniform compositions with no residual lifetime weighting. The claim is valid without a limiting approximation.

In the proposed growing-depth implementation, the deeper rows S,...,L-1, the collar, and the depth-L clock times are measurable in this exposed environment. Once the whole base triangle through L is zero, base C grouping identifies the first K boundaries at depths S and L. The retained event h>=2L and t_K<L then gives the required no-repeat test for every upper completion. Thus these environment restrictions do not secretly condition on outcomes of the unexposed survival tests.

## 2. An explicit complete-vector coupling bound

Let

    B_r=sqrt(r)*(4+sqrt(1200 log r)),
    |r_u-r/(u+1)|<=B_r, 0<=u<=2L+2.

Write N_s=ell_s+P_s-1. There is the useful exact cancellation

    N_s=r_s+r_(s+2)-s-1.

Let

    N_s^0=r/(s+1)+r/(s+3),
    ell_s^0=2r/((s+1)(s+2)(s+3)).

Then ell_s^0/N_s^0=1/(s+2)^2,

    |ell_s-ell_s^0|<=4B_r,
    |N_s-N_s^0|<=2B_r+s+1.

On the above event, for the scales used below and r>=r_0, N_s>=r/(s+2). Consequently

    |(P_s-1)/N_s - (1-1/(s+2)^2)|
      <= 6(s+2)B_r/r + (s+2)^2/r.                  (2.1)

This follows by writing the difference as ell_s/N_s-ell_s^0/N_s^0 and bounding its numerator by 4B_r+(2B_r+s+1)/(s+2)^2. No relative estimate for the second difference ell_s is needed.

Couple K draws without replacement to K independent draws from the same finite population. A repeated sampled population index is the only obstruction, giving TV at most K(K-1)/(2N_s). Conditional on no repetition, the ordered sample is uniform without replacement. Independent Bernoulli variables of parameters p and p* can be coupled with discrepancy probability |p-p*| per entry. Summing these errors over rows gives

    TV(finite actual vector, finite ideal vector)
      <= K^2 S^2/r +12KS^2 B_r/r+4KS^3/r.           (2.2)

Here sum_(s<S)(s+2)<=2S^2 and sum_(s<S)(s+2)^2<=4S^3 were used.

For the infinite ideal array, the finite-depth success probability at k<=S is

    u_(k,S)=(1/(k+1))*((S+2)/(S+1))^k,

while the infinite-depth probability is 1/(k+1). The finite-depth indicators dominate the infinite ones under the same array. Since e^x-1<=2x for 0<=x<=1, a union bound gives an additional TV cost at most 2K/(S+1)<=2K/S. Thus the explicit complete bound is

    TV <= K^2 S^2/r+12KS^2 B_r/r+4KS^3/r+2K/S.      (2.3)

Take

    K=floor(r^(1/100)),
    S=floor(r^(1/50)),
    L=floor(r^(2/5)).

For every r>=r_0, the numerical consequence is

    TV <= 8 r^(-1/100).                             (2.4)

To check constants, put x=log r. Then x>=500,000 because log 2>1/2, and 4+sqrt(1200x)<=2x. The four terms in (2.3) are at most r^(-94/100), 24x r^(-45/100), 4r^(-93/100), and 4r^(-1/100). The first three are each at most r^(-1/100) on this domain. For the middle assertion, e^(11x/25)>24x follows already from the quadratic term of its exponential series. This even gives 7r^(-1/100); (2.4) leaves room.

For completeness, the denominator estimate and finite profile margins follow from the stronger uniform relation proved in Section 4 below. They are therefore valid on the same explicit threshold.

The bound (2.4) is conditional on a feasible safe environment. It is not the probability that such an environment is retained. That latter mass is supplied by the physical, triangle, collar, and flux estimates.

## 3. An explicit reciprocal renewal bound

The ideal infinite-vector process has renewal masses u_n=1/(n+1), with gap generating function

    F(z)=1-integral_(0,1)(1-z)^t dt.

Its gap tail is exactly

    Pr(G>n)=integral_(0,1) product_(j=1,...,n)(1-t/j) dt.

This is the coefficient identity for (1-F(z))/(1-z); it also follows by summing the nonnegative gap coefficients. For n>=1, log(1-y)<=-y gives

    Pr(G>n)<=integral_(0,1)e^(-t H_n)dt
             <=1/H_n<=1/log(n+1).                  (3.1)

Let R_K count renewals in 0,...,K, including zero. For an integer 1<=m<=log K, the event R_K<=m means that the sum of the first m gaps exceeds K, so some gap exceeds K/m. The union bound and (3.1) give

    Pr(R_K<=m)<=2m/log K.                           (3.2)

Indeed log(floor(K/m)+1)>=log(K/m)>=log K/2, since m<=log K<=sqrt K.

Using the exact identity

    E(1/R_K)=sum_(m>=1)Pr(R_K<=m)/(m(m+1))

and splitting at floor(log K), one obtains, for every integer K>=3,

    E(1/R_K)
      <= [2log(log K+1)+1]/log K
      <= 3(1+loglog K)/log K.                      (3.3)

At the K chosen above and r>=r_0, log K>=log r/200 and loglog K<=loglog r. In particular,

    E(1/R_K)<=600(1+loglog r)/log r.                 (3.4)

These estimates concern the proper renewal process identified by its full multipoint law, not independent success indicators. They use no unproved renewal asymptotic.

## 4. Explicit stationary peak-flux bound

Use the same regular event through depth 2L+2. The explicit one-depth concentration bound gives

    Pr_D(regular event fails)<=(4L+6)r^(-200)
                              <=10r^(-998/5).      (4.1)

The stationary unnormalized measure q_(r,L) in the existing core-law/flux theorem satisfies the exact inverse-array identity

    M_L=sum_E q_(r,L)(E) pk(E)
        =E_D[d_L 1_(retained profile domain) 1_(F_L=0)],
    d_u=r_u-r_(u+1), ell_u=d_u-d_(u+1)>=0.

Dropping any extra GOOD, cutoff, or safety restrictions can only increase this nonnegative expectation. Hence no cutoff-dependent constant is needed in the following bound.

On the regular event, put

    delta=(2L+3)B_r/r.

For r>=r_0,

    delta<=1/1024,
    (1-delta)r/(u+1)<=r_u<=(1+delta)r/(u+1),
    0<=u<=2L+2.                                   (4.2)

To justify the numerical threshold, x=log r>=500,000 gives delta<=10x e^(-x/10). The cubic term e^(x/10)>x^3/6000 proves this is at most 1/1024, since x^2>61,440,000. All inequalities persist for larger x.

Monotonicity of the nonnegative sequence d_u yields, for u>=2,

    d_u <= [r_floor(u/2)-r_u]/[u-floor(u/2)]
         <=5r/u^2.                                (4.3)

The last inequality follows from (4.2), with each denominator factor at least u/2. The factor 4(1+delta) is less than 5.

Conditional on a complete regular profile, the probability of the canonical zero triangle through L is exactly

    Z_L=product_(u=0,...,L-1)
          (p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1).

The slots are distinct: (4.2), L<=r^(2/5), and r>=r_0 give p_u-1>=u+1. Each row's negative logarithm is at least (u+1)ell_u/(p_u+ell_u).

Choose the fixed integer m=1024. For m<=u<L, (4.2)--(4.3) give

    p_u+ell_u
      <= [2r/(u+2)]*(1+delta+(u+2)/(2r)+5(u+2)/(2u^2))
      <= [2r/(u+2)]*(1+1/128).

The last three additions are bounded by 1/1024, 1/1024, and 3/1024. Therefore

    -log Z_L >= (127/128)*(1/(2r))
                    sum_(u=m,...,L-1)(u+1)(u+2)ell_u.    (4.4)

The exact Abel identity is

    sum_(u=m,...,L-1)(u+1)(u+2)ell_u
      =(m+1)(m+2)d_m-L(L+1)d_L
       +2(m+2)r_(m+1)-2Lr_L+2sum_(u=m+2,...,L-1)r_u.

Discard the positive boundary terms. By (4.2)--(4.3), the two negative terms have total magnitude at most 9r. The remaining sum is at least

    (1-delta)r*(log L-log(m+3)).

It follows from (4.4) that

    -log Z_L >= (7/8)log L-log(1027)-5,

because (127/128)(1-delta)>7/8. Consequently

    Z_L<=250,000 L^(-7/8).                         (4.5)

Here e^5*1027<3^5*1027=249,561<250,000. Combining (4.3) and (4.5), the regular contribution to M_L is at most

    1,250,000 r/L^(23/8)
      <=10,000,000 r^(-3/20),                      (4.6)

using L>=r^(2/5)/2 and 2^(23/8)<8. The irregular contribution is at most r times (4.1), bounded by r^(-3/20) on the stated threshold. We obtain the explicit result

    M_L <=11,000,000 r^(-3/20), r>=2^(1,000,000).    (4.7)

The same regular event gives h>2L+2, since r_(2L+2)>0. Also N_s>=r/(s+2) for s<S: its ideal value is at least 2r/(s+2), the relative profile error is at most delta, and (s+1)(s+2)<<r. These inequalities, and P_s>K and n_S>=2S+1, hold at r_0 and above by the stated power separation.

If 1<=c<=sqrt(loglog r), the actual finite clock horizon up to (c+2)sqrt r is also below r_L on this event. Indeed r_L>=r^(3/5)/4, while r^(1/10)/4>=log r>=sqrt(loglog r)+2 on the same threshold. Thus the numerical profile margins used by the growing-scale proposal are valid; the probability of having the zero triangle and good clock endpoints remains a separate raw-incidence estimate.

## 5. Remaining quantitative dependency and bookkeeping

The finite source law and the coupling above are sufficient for the proposed growing-vector step. They do not require exchanging the iterated limits in the qualitative coefficient-one proof. The proposal correctly replaces that limiting argument by a quantitative finite coupling.

However, the final OR-word rate additionally requires explicit uniform versions of the physical short-incidence and early-triangle estimates for b as large as order sqrt(loglog r). Existing sources such as `PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md` explicitly state only fixed-b constants. The separate new derivation of inequalities (16)--(19) must be retained as a proof input, including the sector where its legal query depth is shorter than L; assigning numbers to the old symbols C_b would not suffice.

Discarding non-GOOD profiles is already uniform for every cutoff H<r: `PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md`, Section 5, bounds their raw incidence mass by 2/(n+1)^9. A proved early-triangle bound controls positive top gaps as well, since Z_(0,0)>0 implies F_L>0. Thus the use of an unnormalized incidence measure creates no missing lower-normalizer assumption.

The values in (2.4), (3.4), and (4.7) are genuine explicit numeric constants derived above. Their threshold is an interface threshold; the final assembled theorem must also meet the thresholds in the separate uniform-incidence and compiler proofs. This note does not assign a final gamma, C, or k-threshold before those inputs are assembled.
