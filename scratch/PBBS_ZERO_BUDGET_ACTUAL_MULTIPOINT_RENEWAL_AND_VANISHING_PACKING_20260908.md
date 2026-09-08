# Actual zero-budget time-shift renewal and vanishing packing

PRIOR-RESULT CORRECTION: this complete zero-budget theorem, including
the multipoint renewal and all-height packing conclusion, was already
proved in `PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md`.
Appendix located that file and root read it in full. This note is an
independent rederivation/consolidation, not a new theorem. The separate
new full-short result is in
`PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md`.

2026-09-08. Root pure-proof deduction; no mathematical execution.
Appendix_a independent full-file audit against all three original sources:
PASS. This concerns actual PBBS time
shifts, rather than original-index cones. It proves vanishing packing
for the complete zero-budget subfamily. Positive-budget short runs
remain outside the conclusion, so no new full-cube coefficient follows.

## 1. Accepted exact inputs and the additional conclusion

Write chi_h(D)=1{height(D)=T(D)=h}, where T includes the consuming
update and a repair trace has T+2 edges. Put R=sqrt(r) and
W=(2r+1)Cat_r. Use the original finite PBBS process tau=phi^2.

The exact sources are

* `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_zero_budget_pair_product_and_overlap_divergence.md`;
* `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_zero_budget_gaussian_band_weighted_lower_bound.md`;
* `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_zero_budget_uniform_bound.md`.

The pair-product source already proves the following actual time-shift
criterion. Conditional on chi_h(D)=1, for 0<=3d<=h,

    chi_h(tau^d D)=1
      iff height(U_i)<=i-d for all d<=i<h.             (1)

Here U_i are the ORIGINAL forest coordinates of the canonical peeling,
whose base caps are height(U_i)<=min(i,M_i),
M_i=h-ceil(i/2). The terminal first-descent forests V_j have caps
ceil(j/2). This is a graded bijection at fixed semilength; no probability
independence at a reached root is used.

The rederived step is to conjoin (1) for several shifts. Its exact product
shows that their limiting indicators form a recurrent renewal process.
This is stronger than the earlier divergent second-moment conclusion.

## 2. Exact multipoint product

Let 0=d_0<d_1<...<d_m, put g_j=d_j-d_(j-1), and assume 3d_m<=h.
Define J_(h;d_1,...,d_m)(x) to count roots satisfying chi_h at all these
actual time shifts. Let F_0=F_1=1 and F_n=F_(n-1)-xF_(n-2).
Then

    J_(h;d_1,...,d_m)(x)
      = x^h / [(product_(j=1)^m F_(g_j)(x))
                                  F_a(x)F_b(x)F_c(x)],           (2)

where a,b,c are the balanced nonnegative integers with
a+b+c=2h+1-d_m. For m=0 this is the full zero-budget series G_h.

Indeed, in d_j<=i<d_(j+1), the strongest applicable test in (1) is
height(U_i)<=i-d_j. All these i<d_m satisfy i<M_i, so no universal
cap modifies that interval. For i>=d_m the cap is min(i-d_m,M_i).
Writing C_l=F_l/F_(l+1), each completed interval contributes

    product_(l=0)^(g_(j+1)-1) C_l = 1/F_(g_(j+1)).

The terminal V factors and the final U tail are precisely the same
ones as in the pair proof at lag d_m. Their product is
1/(F_a F_b F_c), by that proof's exact cap census. Multiplying gives
(2). This argument includes adjacent shifts and gaps equal to one.

At critical weight F_n(1/4)=(n+1)/2^n. Since the sum of all denominator
indices in (2) is 2h+1, it follows exactly that

    J_(h;d_1,...,d_m)(1/4)
      = 2 / [(product_j(g_j+1))(a+1)(b+1)(c+1)].       (3)

## 3. Fixed-size conditioning preserves every fixed multipoint limit

Fix the shifts and a positive Gaussian band 0<a_0<b_0<infinity.
Uniformly for a_0<=h/R<=b_0,

    [x^r]J_(h;d_1,...,d_m) / [x^r]G_h
          -> product_(j=1)^m 1/(g_j+1).              (4)

For clarity, the local-limit justification in the pair source works
unchanged here. Under critical normalization, (2) has size h plus
independent geometric variables from its F factors. The fixed factors
F_(g_j) add a fixed finite sum with finite mean. Each of the three large
indices divided by h tends to 2/3, exactly as for G_h. The scaled size
therefore has the same limiting density g. Keeping one geometric mode
from each of two large factors bounds its characteristic function by
C/(1+t^2) on |t|<=pi h^2. Each additional fixed factor has modulus at
most one. Dominated lattice Fourier inversion gives

    P(N=r)=h^(-2)[g(r/h^2)+o(1)]

uniformly on the band, with g positive on its compact argument interval.
The ratio of the critical amplitudes in (3) tends to the right side
of (4). This proves (4) without any growing-lag approximation.

Consequently, conditional on chi_h(D)=1, the finite indicator vector

    (chi_h(tau^d D):0<=d<=D_*)

converges in law, uniformly on that height band, to a binary process
whose all-one joint probabilities at 0=d_0<...<d_m are
product_j 1/(g_j+1). Finite inclusion-exclusion determines the whole
vector law from those probabilities. Multiplication by h+2 and mixing
over the band preserves this uniform convergence; thus it applies to
the actual zero-budget birth-incidence law as well.

## 4. The limiting process is recurrent, not independent

Put u_n=1/(n+1). Its generating function and renewal-increment series
are

    U(z)=-log(1-z)/z,
    F(z)=1-1/U(z)=1-integral_0^1 (1-z)^t dt.           (5)

For n>=1 the coefficient f_n of F is
-integral_0^1 (-1)^n binom(t,n)dt, which is nonnegative since
binom(t,n) has sign (-1)^(n-1) for 0<t<1. Moreover f_0=0 and
F(1-)=1. Thus these coefficients are a probability law on positive
finite integers. The renewal process with independent increments of
this law has mass sequence u and all-one joint probabilities
product_j u_(g_j). It is therefore exactly the limiting indicator law
in Section3. Its indicators are generally dependent.

Let N_D count its renewals in {0,...,D}. Then N_D tends to infinity
almost surely: each fixed number of finite increments has a finite
sum. Hence for every fixed integer M,

    P(N_D<=M) -> 0 as D->infinity.                   (6)

The same renewal law appeared for original-index cones in the earlier
cone note. Here it follows separately from the ACTUAL time-shift forest
bijection (1), and is not transferred through a common-C-boundary map.

## 5. Actual overlap diverges under zero-budget band incidence

Let B_(r;a_0,b_0) contain all physical zero-budget births with
a_0 R<=h=T<=b_0 R. Sample one of its repair-trace incidences uniformly:
the birth root has density (h+2)1_B/mu_B relative to the uniform Dyck
root, and its edge offset j is uniform in {0,...,h+1}. The accepted
band theorem gives mu_B->I_B with 0<I_B<infinity.

Fix D first. Uniformly throughout the band,

    P(j<D)<=D/(a_0 R+2) -> 0.

On j>=D, every zero-budget shifted birth at time d in {0,...,D}
has its inclusive edge interval [d,d+h+1] covering j. Its height is
unchanged by tau, so it belongs to the same band. Distinct d are
distinct physical birth occurrences. Therefore, if K_B is the actual
number of band traces containing the sampled edge,

    K_B >= sum_(d=0)^D chi_h(tau^dD)  on j>=D.       (7)

Equations (4), (6), and (7), first fixing D and sending r to infinity,
then sending D to infinity, prove

    K_B -> infinity in actual band-incidence probability.      (8)

Since K_B>=1 on that law, bounded convergence also gives
E_inc,B[1/K_B]->0. The exact stationary counting identity is

    fraction of all physical edges covered by B
          = mu_B E_inc,B[1/K_B] = o(1).             (9)

This statement averages over the full physical factor, as required by
the original Dyck/physical dictionary; it asserts no uniform statement
on an individually chosen component.

Every band trace has at least a_0 R edges. A pairwise edge-disjoint
subfamily consequently has cardinality at most the size of their
occupied edge union divided by a_0 R. Equation (9) yields

    packing(B_(r;a_0,b_0)) = o(W/R).                 (10)

## 6. The complete zero-budget family also has vanishing packing

The accepted uniform zero-budget coefficient estimate supplies, for
h>=2,

    # {D in Dyck_r:chi_h(D)=1}
      <= C 4^r (h+1)^(-5)
                     exp[-(r-h)/(2(h+1)^2)].         (11)

For r>1 the height-one class is empty. For h<=aR and fixed small a,
eventually h<=r/2, so the exponential in (11) is at most
exp[-r/(4(h+1)^2)]. Comparing the unimodal positive summand with its
integral and maximum gives

    lim_(a down to0) limsup_(r->infinity)
      R P_D(height=T<aR) = 0.                       (12)

Explicitly, after x=(h+1)/R the limiting integral is bounded by a
constant times integral_0^(2a) x^(-5) exp[-1/(4x^2)]dx, which tends
to zero. The maximal-summand remainder, after normalization, is o(1).
For h>bR, dropping the exponential in (11) and summing (h+1)^(-5)
gives, by Cat_r asymptotics,

    limsup_(r->infinity) R P_D(height=T>bR) <= C/b^4. (13)

The number of physical births in either tail is W times its uniform
Dyck probability, and any packing has at most that many members.
For the middle band use (10). First let r tend to infinity with a,b
fixed, then a decrease to zero and b increase to infinity. This proves

    packing({all physical births with T=height}) = o(W/sqrt(r)). (14)

In particular (14) holds for every Gaussian-cutoff subfamily T<=cR.
This removes the full zero-budget family as a packing obstruction even
though its Gaussian-band raw trace incidence has a nonzero limit and
its stationary second moment diverges.

## 7. Remaining scope

The compiler requires the analogous packing estimate for ALL short
births, including T>height. Neither (1) nor (2) is presently established
for that larger class. Thus (14) is an independently audited subfamily
result, not coefficient one or an improved c9 bound.
No assertion about actual intermediate-row shifted-zero recurrence is
needed for this proof, and none is supplied by it.
