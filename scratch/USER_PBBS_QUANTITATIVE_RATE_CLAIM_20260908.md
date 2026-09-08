# User-supplied quantitative PBBS claim — review transcription

Status: unverified proposal supplied in the conversation on 2026-09-08. This is a structured transcription for independent internal review, not an accepted theorem or the unavailable linked full proof/verifier package. The user's message is the authoritative original.

## Claim and finite compiler

There are absolute C,gamma>0 with nu(k)/W(k) <= 1+C/(log k)^gamma. More precisely, R=sqrt(r), W_r=binom(2r+1,r), and uniformly 1<=c<=sqrt(log log r), for sufficiently large r:

    nu(2r+1)/W_r <= 1+C(c+2)/R
        +exp(A(c+2)^2)*(log log r)^(3/2)/log r + C exp(-c^2/8).  (3)

Use finite PBBS inputs, not the coefficient-one theorem or its diagonal argument. Compiler with aperture H=t+1:

    nu(2r+1) <= W_r + 2H Cat_r + 2(5H-1) P_t(r) + 2 L_r(r-H),
    Cat_r=W_r/(2r+1),   2 L_r(r-H)/W_r <= C exp(-t^2/(8r)).

## Exact law and sampling representation (sections 2–3)

On the safe exposed environment E_S, for 0=k_0<k_1<...<k_m<=K<=S,

    M_s=sum_a min(k_a-k_(a-1),s+1), P_s=p_s-s-1,
    Pr(Y_(k_1)=...=Y_(k_m)=1 | E_S)
       =product_(s<S) (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s). (4)

Here (x)_j is falling factorial; the Y are actual physically shifted triangle successes. Distinct-slot and no-repeat conditions are explicit in the source.

If (Z_1,...,Z_P) is uniform among weak compositions of ell into P parts, the first K<=P-1 zero indicators have the law of K draws without replacement from N=ell+P-1 objects with P-1 successes. Specified j indicators all zero have probability (P-1)_j/N_j. Inclusion-exclusion determines the full vector. Coupling to draws with replacement gives TV <= K(K-1)/(2N). (5)

For each s<S independently sample a K-long without-replacement vector B_(s,j) with these parameters. Define

    Z*_k=product_(s<S) product_(j=max(1,k-s)..k) B_(s,j). (6)

The union of these blocks at requested indices has size M_s, so the complete success vector has the same conditional law as the actual Y vector. (7) This is distributional equality, not a pointwise static replacement of physical coordinates.

Replace each row by independent Bernoulli variables with p*_s=1-1/(s+2)^2 and include all rows. Then the success intersections are product_a 1/(k_a-k_(a-1)+1), hence a renewal process with renewal masses u_n=1/(n+1). (8)

Regular profile event:

    |r_u-r/(u+1)| <= B_r=sqrt(r)*(4+sqrt(1200 log r)), 0<=u<=2L+2. (9)

Source one-depth concentration gives complement probability <=C(L+2)r^-200. On this event, N_s asymp r/(s+2), and

    |(P_s-1)/N_s-p*_s| <= C*((s+2)B_r/r+(s+2)^2/r). (10)

The numerator perturbation does not need a relative approximation to ell_s. Sampling/Bernoulli couplings and the infinite-row tail K/(S+1) give

    TV <= C*(K^2*S^2/r + K*S^2*B_r/r + K*S^3/r + K/S). (11)

Choose K=floor(r^(1/100)), S=floor(r^(1/50)), L=floor(r^(2/5)). (12)

Renewal gap G has generating function F(z)=1-integral_0^1 (1-z)^t dt and exact tail

    Pr(G>n)=integral_0^1 product_(j=1..n)(1-t/j) dt <=1/log(n+1). (13)

Let R_K count renewals in 0..K including zero. If R_K<=m, the first m gaps sum to >K, so one exceeds K/m. For m<=log K, Pr(R_K<=m)<=2m/log K. Use 1/n=sum_(m>=n)1/[m(m+1)] and split at floor(log K) to conclude

    E(1/R_K)<=C*(1+log log K)/log K. (14)

## Uniform cutoff dependence: section 4

Source full-profile envelope Q=a+sqrt(log(a+2))<=3a, with absolute subGaussian tail for a, plus deterministic clock estimates at legal depth.

First choose geometric depth d_g=floor(kappa_g*R/Q) for fixed small absolute kappa_g. Profile bounds give on every root

    h>=c_h*R/Q. (15)

When d_g<2 use h>=1 after reducing c_h. For cutoff H<=bR use a separate clock depth d=floor(kappa*R/((b+1)Q)). The shorter query depth ensures circumference/composition conditions, but retain the stronger h bound, so H/h<=C bQ rather than the weaker bound from d alone. Source deterministic path estimate yields

    Pr(T<=H | profile) <= C(b+1)Q/R * exp(C(b+1)Q). (16)

Averaging with the subGaussian envelope gives

    mu_H=E[(T+2)1_(T<=H)] <=exp(C(b+1)^2). (17)

The same argument is claimed to yield, with absolute constants,

    Pr(T<=H, h<epsilon R)
       <= exp(C(b+1)^2)/R * exp(-b_0/epsilon^2), (18)
    E[(T+2)1_(T<=H,F_L>0)]
       <= exp(C(b+1)^2)*L^2/r. (19)

F_L is the sum of base triangle entries through L. For (18), low height forces Q>=const/epsilon. For (19), retain early-triangle restriction in finite path majorant. User says the unavailable full proof includes the complementary sector where the legal query depth is shorter than L. Uniform b up to order sqrt(log log r) is essential, fixed-b estimates insufficient.

## Incidence measure, physical eligibility, same-family cutoff (section 5)

Use unnormalized incidence measure

    I_t(f)=E_D[1_(T<=t) sum_(j=0..T+1) f(D,j)], total mass mu_t. (20)

K_t(e) counts traces with lifetime<=t containing edge e; U_t is occupied edge union. Exact identity

    |U_t|/W_r = I_t(1/K_t). (21)

Let q_(r,L) be stationary reference measure obtained by summing all base-zero upper completions and M_L=sum_E q_(r,L)(E)*pk(E). Source finite profile/Abel argument at L=r^(2/5) gives M_L<=C r^(-3/20).

For first K common predecessor boundaries, t_K=C_L^K(0), Delta_K=C_L^K(b_0)-b_0, b_0=2T+1, stationary identities

    sum_E q_(r,L)(E)t_K(E)=2K M_L,
    sum_E q_(r,L)(E)Delta_K(E)=2K M_L.

Claimed exact even for growing finite K. Put q=ceil(R*r^(-1/100)). Markov and offset counting control t_K>=L, 2j<t_K, Delta_K>q. The extra K-slot collar in rows S..L-1 fails with probability

    <= CK sum_(u=S..L-1) ell_u/r_(u+1) <= CK/S. (22)

The latter is the finite Abel bound, not a growing-depth independent approximation. Combine these, (11),(19), and profile regularity: all errors except cutoff boundary strip have raw incidence mass

    <= exp(C(c+2)^2)*r^(-1/200). (23)

Examples before logs: base triangle r^-1/5, initial clock r^-1/25, collar r^-1/100. On remaining incidences every success is distinct native physical birth whose trace contains sampled edge and lifetime<=T+q. Thus successes are in same cutoff family provided t-T>=q. Conditional comparison and (14) give

    |U_t|/W_r <= exp(C(c+2)^2)*[(log log r)/log r+r^-1/200]
         + I_t(0<=t-T<q). (24)

Average t over integer Hset=[ceil(cR),floor((c+1)R)]. A fixed birth lies in the strip for at most q+1 choices, |Hset|>=R/2. Average strip mass <=(q+1)/|Hset| * mu_floor((c+1)R) <=exp(C(c+2)^2)r^-1/100. Therefore some cutoff in this range satisfies

    |U_t|/W_r <=exp(C(c+2)^2)*(log log r)/log r. (25)

## Packing and final rate (section 6)

Split an edge-disjoint packing of short traces at birth height epsilon R. Low height uses (18); every other trace has at least epsilon R distinct edges in U_t. Thus

    R*P_t(r)/W_r <= exp(C(c+2)^2)*exp(-b_0/epsilon^2)
                      + |U_t|/(epsilon W_r). (26)

Take epsilon^2=b_0/(2 log log r), yielding

    R*P_t(r)/W_r <= exp(C(c+2)^2)*(log log r)^(3/2)/log r. (27)

Use the literal compiler at top, H=t+1 and t>=cR, to obtain (3), absorbing a factor c+2 into the exponential constant.

Enlarge A>=1 and choose c=sqrt(log log r/(16A)). Eventually c>=2, exp(A(c+2)^2)<= (log r)^(1/4), exp(-c^2/8)=(log r)^(-1/(128A)). One valid final exponent is gamma=1/(256A). The trimmed one-coordinate lift doubles length, and W(2r+2)=2W_r, so even dimensions inherit the rate. Lower bound B<=nu yields gap estimate.

Claimed algorithm: try every admissible aperture in finite PBBS construction, compile every word and retain shortest. No need algorithm to know gamma/threshold.

User reports checks (not executed/available to us yet):175 composition laws;60 full vector distributions;744 multipoint identities;renewal identities through160;cutoff averaging on1200 finite interval families. These test formulas, not the full asymptotic theorem/inherited PBBS lemmas. User explicitly requests independent review and does not claim nu=B.
