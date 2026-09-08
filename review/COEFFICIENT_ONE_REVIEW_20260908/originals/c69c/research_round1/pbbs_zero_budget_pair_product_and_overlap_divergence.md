# Exact zero-budget pair product and divergent stationary overlap moment

Date: 2026-09-07. Pure proof; no computation or original-source edits.

Let chi_h(D)=1{ht(D)=T(D)=h}. For 0<=3d<=h, the actual joint event
chi_h(D)chi_h(tau^d D)=1 has the exact generating function

    J_(h,d)(x)=x^h/[F_d(x)F_a(x)F_b(x)F_c(x)],         (1)

where a,b,c are balanced integers with sum 2h+1-d, and
F_0=F_1=1, F_m=F_(m-1)-xF_(m-2). In particular J_(h,0) is the accepted
full zero-budget generating function G_h.

For each fixed lag d, on every positive Gaussian height band,

    [x^r]J_(h,d) / [x^r]G_h -> 1/(d+1),               (2)

uniformly when a_0<=h/sqrt(r)<=b_0, for fixed 0<a_0<b_0.
Consequently, the zero-budget Gaussian-band family has DIVERGENT second
moment of stationary interval overlap, despite a finite positive limiting
first moment. Thus a uniform second-moment bound for this actual full
subfamily is false. The proof does not use a thin-profile example or a
fresh law at a reached state.

## 1. Actual time shifts in the original forest encoding

Use the original formal peeling from pbbs_original_forest_product.md:

    A_i=L_i 1 R_i 0 U_i,
    A_(i+1)=L_i 0 R_i,       A_0=D,                    (3)

where A_i starts at height i and ends at zero. The terminal first-descent
forests V_j have caps ceil(j/2), and the original suffixes have universal
caps M_i=h-ceil(i/2). Zero budget is equivalent to

    ht(U_i)<=i,                 0<=i<h.               (4)

Assume chi_h(D)=1. Set

    Q_d=U_(d-1) 1 U_(d-2) 1 ... U_0 1,
    Q_0=empty.

The actual unmarked evolution satisfies

    tau^d D=Q_d A_d,             0<=d<=h.              (5)

Indeed Q_d has net height d and every vertex before its last up-step has
height at most d-1, by (4). For d<h, the first height-h step is therefore
in A_d, and the next first-maximum block rotation prepends U_d 1 and
replaces A_d by A_(d+1). This proves (5) by induction. U_0 is empty,
as required by (4), so the first step is also covered.

Now formally peel the NEW original root tau^d D. For 0<=j<h-d its
partial core is Q_d A_(d+j), read from height j. The prefix Q_d has
height at most j+d<h, so the canonical selected maximum and following
return remain in A_(d+j). Its first h-d suffix forests are consequently

    U'_j=U_(d+j),                0<=j<h-d.             (6)

The remaining suffixes need not be identified or assumed independent.
Every height-h root has the universal cap

    ht(U'_j)<=h-ceil(j/2).

If 3d<=h and j>=h-d, then h-ceil(j/2)<=j. Thus all the remaining
zero-budget tests on U'_j are automatic. Combining this with (6) gives
the EXACT equivalence, on the event chi_h(D)=1,

    chi_h(tau^dD)=1
      iff ht(U_i)<=i-d for every d<=i<h.              (7)

This is a condition on the original independent forest coordinates at
critical weight. No original-to-reached reset is used. At fixed
semilength, the same statement holds as a graded combinatorial identity,
without claiming independence after size conditioning.

## 2. The exact positive pair partition

Write C_m=F_m/F_(m+1) for height-at-most-m forest generating functions.
The original forest bijection and (7) give

    J_(h,d)=x^h product_(j=0)^(h-1) C_ceil(j/2)
                  product_(i=0)^(d-1) C_i
                  product_(i=d)^(h-1) C_min(i-d,M_i). (8)

Here i<d<=h/3 implies min(i,M_i)=i. All factors are positive counting
series and every original tuple satisfying these caps is admissible.

For ell>=1, the number of caps in (8) which are at least ell is

    max(0,h-2ell+1)+(d-ell)_+
      +max(0,min(h-1,2h-2ell)-ell-d+1)
    =max(0,2h+1-d-3ell)+(d-ell)_+.                     (9)

The equality follows by separating ell<=(h+1)/2 and ell>(h+1)/2;
3d<=h keeps the relevant lower branch positive until the stated cutoff.
The first term is the cap profile of 1/(F_aF_bF_c), with a+b+c=2h+1-d
balanced. The second term is the profile of
product_(i=0)^(d-1) C_i=1/F_d. Telescoping proves (1).

At critical weight, F_m(1/4)=(m+1)/2^m, so

    J_(h,d)(1/4)=2/[(d+1)(a+1)(b+1)(c+1)].            (10)

For fixed d and h->infinity, division by G_h(1/4) therefore tends to
1/(d+1).

## 3. Exact semilength conditioning at fixed lag

The critical-normalized size of (1) is h plus independent geometric
variables from its four F factors. For fixed d, the F_d factor adds only
a fixed finite sum with finite mean. The other three indices divided by
h tend to 2/3. Thus their size divided by h^2 converges to the SAME
positive variable Y as for G_h, with Laplace transform

    E exp(-uY)=[(2sqrt(u)/3)/sinh(2sqrt(u)/3)]^3.       (11)

Keep the first geometric mode from two of the three large factors.
Exactly as in pbbs_zero_budget_gaussian_band_weighted_lower_bound.md,
their characteristic functions at frequency t/h^2 give the integrable
bound C/(1+t^2) on |t|<=pi h^2. The extra fixed F_d factor has modulus
at most one. Dominated Fourier inversion therefore gives the same
uniform lattice local limit with density g:

    P(N_(h,d)=r)=h^(-2)[g(r/h^2)+o(1)].               (12)

Combining (10),(12) with the corresponding formulas for G_h proves (2).
Uniformity on a positive Gaussian band follows because g is continuous
and bounded away from zero on the associated compact size-ratio interval.
There is no assertion of uniformity for d growing with r.

Let p_(r,h)=P_Dyck_r(chi_h=1) and
p_(r,h,d)=P_Dyck_r(chi_h(D)chi_h(tau^dD)=1). If

    kappa(u)=(27sqrt(pi)/4)u^(-5)g(u^(-2)),

then the accepted one-point local limit and (2) give, for every fixed d,

    p_(r,h,d)=r^(-1)[kappa(h/sqrt(r))/(d+1)+o(1)]      (13)

uniformly on the fixed band.

## 4. Exact stationary overlap kernel

Fix a physical complement-projected cycle and height h. At each
transition let Y_i be the indicator that the newly inserted coordinate
starts a zero-budget run of height h. Its full repair interval has
h+2 edges. Thus the number of these intervals covering edge e is

    K_e=sum_(j=0)^(h+1) Y_(e-j).                       (14)

Uniform physical phases correspond to the n-fold deck of uniform Dyck
roots when averaged over the FULL physical factor. Equation (14) defines
K componentwise, but (15) below uses this full-factor average and the
unconditional probabilities p_(r,h),p_(r,h,d); it is not an average on an
arbitrarily fixed component. One step of the projected dynamics induces tau on the root
coordinate. The complement-birth phase may differ by phi, but the full
root set is phi-invariant and phi commutes with tau=phi^2; this common
phase change preserves every two-time count. Hence the exact stationary
second-moment contribution of height h is

    (h+2)p_(r,h)
      +2 sum_(d=1)^(h+1)(h+2-d)p_(r,h,d).             (15)

This is just expansion of (14), with no independence assumption. The
pruning height is invariant along an orbit, so different heights cannot
contribute at the same physical edge. Summing (15) over a band gives its
full second moment. Even without using this last disjointness, the same
sum would be a lower bound, which is enough below.

## 5. Harmonic divergence in every positive Gaussian band

Fix 0<a_0<b_0, and include only zero-budget runs with
a_0 sqrt(r)<=h<=b_0 sqrt(r). Put

    I_1=integral_(a_0)^(b_0) u kappa(u)du>0.

The one-point band theorem gives E K_e->I_1. For every fixed integer
D>=1, (13) and Riemann summation give

    sum_(h in band)(h+2-d)p_(r,h,d) -> I_1/(d+1)
               for every 1<=d<=D.                    (16)

For sufficiently large r, all those pairs lie in the range 3d<=h where
the exact partition was proved. Keeping only these nonnegative terms
of (15),

    liminf_(r->infinity) E K_e^2
      >= I_1 [1+2 sum_(d=1)^D 1/(d+1)].               (17)

First fix D, send r to infinity, and then send D to infinity. It follows
that

    E K_e^2 -> infinity,       Var(K_e)->infinity.      (18)

No growing-lag uniform estimate is needed and no rate of divergence is
claimed. The same proof applies to stationary existing-owner overlap
(each run has h+1 owners) and internal-edge overlap (each run has h
internal edges): replacing h+2 by either h+1 or h changes none of the
limits in (16).

This answers negatively the proposed uniform second-moment bound for
the actual full zero-budget Gaussian-band subfamily. It does not imply
that overlap is uniformly large, that the fraction of affected owners
is bounded below, or that many distinct targets are lost. A profile-
restricted subfamily would require a separate analysis. Shared repairs,
cut packing, and normalized target-fibre damage remain separate questions.

Sources: pbbs_original_forest_product.md Sections 1-5;
pbbs_zero_budget_gaussian_band_weighted_lower_bound.md Sections 1-3;
pbbs_gaussian_clock_genealogy_structural_audit.md Sections 1-5; and
pbbs_gaussian_age_residual_and_cut_charges.md Sections 1-4.
