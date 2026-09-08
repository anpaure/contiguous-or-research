# Vanishing occupied support now suffices for Gaussian-short packing

2026-09-08. Root pure-proof synthesis. Complete root-helper and task05
full-file audits PASS; the quantitative modulus below also passes
independent audits. No computation. The small-height estimate is the new input
that removes the earlier quantitative logarithmic rate requirement.

## 1. Uniform small-height tightness at the short-birth scale

Let r>=1, R=sqrt r, W=(2r+1)Cat_r, and H=floor(cR), with c>0 fixed.
Use the profile-measurable a>=1, A=a+sqrt(log(a+2))<=3a, and
L=floor(kappa_c R/A) of the accepted theorem
PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md. Its proved inputs are

    Pr(a>1+x)<=C exp(-b x^2),
    Pr(T<=H | full profile)<=C_c A exp(C_c A)/R.       (1)

The second estimate holds on EVERY profile, including L<2.
There is also the following global height bound:

    R/(h+1)<=A/kappa_c.                              (2)

If L>=2, the accepted proof gives h>2L and
2L>=kappa_c R/A, proving (2). If L<2, then A>kappa_c R/2;
since every nonempty Dyck root has h>=1, (2) follows again.

Fix0<epsilon<=1 and take r large enough that R>=1/epsilon. Then
h<epsilon R implies h+1<=2epsilon R. By (2) and A<=3a,

    a>=kappa_c/(6epsilon).

The height event and a are measurable from the ORIGINAL full profile.
Multiplying the global conditional bound in (1) by this indicator,
then using Cauchy-Schwarz and the uniform subGaussian tail, gives

    Pr(T<=H, h<epsilon R)
       <=C_c exp(-b_c/epsilon^2)/R.                   (3)

Here C_c,b_c>0 are independent of r and epsilon. Explicitly,
E[A exp(C_c A)1_{a>=t}] is at most its uniformly bounded L2 norm
times Pr(a>=t)^(1/2), hence at most C_c exp(-b' t^2), after
absorbing the shift by one into the constant. Substitute
t=kappa_c/(6epsilon). This is at the SHORT-BIRTH scale1/R;
a bound only on unconditional low height would not suffice.

## 2. A deterministic packing split

Let F_r be ANY retained family of physical repair traces with T<=H.
It need not be invariant under the dynamics or coordinate rotations.
Let U_F be its occupied-edge union and P(F) its maximum size of an
edge-disjoint subfamily. Every trace has T+2 edges and T>=h.
The accepted full physical factor has W edges in total and each
physical period has length at least2r+1. A trace has consecutive edge
indices d,...,d+T+1. For fixed c and sufficiently large r,
T+2<=H+2<2r+1, so all its T+2 edges are distinct.

Split any packing into births with h<epsilon R and the others.
The first part has at most the number of ALL physical short births
of that height, at most W times (3). Every trace in the second part
has at least epsilon R distinct edges, and these edges are disjoint
and contained in U_F. Therefore

    R P(F)/W
       <=C_c exp(-b_c/epsilon^2)+|U_F|/(epsilon W).    (4)

This bound is uniform over every retained F_r. If |U_F|=o(W), first
let r tend to infinity at fixed epsilon, then let epsilon decrease
to zero. Equation (4) proves

    |U_F|=o(W)  ==>  P(F)=o(W/sqrt r).                (5)

No o(1/sqrt(log r)) rate on occupied support is required. The earlier
budget-floor division remains valid but is no longer needed for this
implication. Conversely, no statement that occupied support actually
vanishes is proved by (4) or (5).

### 2.1. A quantitative modulus

Write u=|U_F|/W, so0<=u<=1. There is a constant depending only on c
such that

    P(F)<=C_c (W/R) u sqrt(log(e/u)),                 (5a)

with value zero at u=0. For0<u<=1 put b=min(b_c,1/2) and
epsilon=sqrt(b/[2log(e/u)]). If epsilon>=1/R and r is sufficiently
large, (4) applies uniformly: its exponential term is at most
C_c(u/e)^2 and its other term is sqrt(2/b)u sqrt(log(e/u)).
The first is absorbed into the second. If epsilon<1/R, use the
elementary P(F)<=|U_F| instead, obtaining

    R P(F)/W<=Ru<u/epsilon=sqrt(2/b)u sqrt(log(e/u)).

If u=0 the packing is empty. Finitely many smaller r are absorbed
into C_c using P(F)<=|U_F| and sqrt(log(e/u))>=1. Thus (5a) holds
uniformly over retained families, not only invariant ones.

## 3. Consequence for the clean-triangle overlap problem

Task08's fully audited
pbbs_clean_triangle_hypergeometric_reciprocal.md defines a clean
retained family F_clean of residual short births. Its omitted sector
already has packing o(W/sqrt r). The accepted low-budget theorem
also handles all B<=J_r births, independently of the lifetime cutoff.

For the clean family let mu_clean=E[(T+2)1_clean]. Its actual incidence
environment E determines the number k(E) of eligible DISTINCT nonzero
original labels, including the shifted deeper-triangle gate and BOTH
lifetime/edge-overlap threshold tests. The exact top-row composition law
and same-particle multiplicity give

    (mu_clean/2) E_inc,clean[1/(k+1)]
       <=|U_clean|/W
       <=2mu_clean E_inc,clean[1/(k+1)].              (6)

If mu_clean=0, interpret all these quantities as zero. Its upper bound
is at most the now proved total short-incidence bound C_c.
Combining (5)-(6), a sufficient remaining condition is simply

    mu_clean E_inc,clean[1/(k+1)] ->0.                (K_c)

There is no prescribed logarithmic convergence rate in (K_c).
Equivalently, using bounded mu_clean, it is enough and necessary that

    mu_clean Pr_inc,clean(k<=M) ->0
                       for EVERY fixed integer M>=0. (7)

Necessity follows because 1/(k+1)>=1/(M+1) on k<=M.
For sufficiency split at M; the reciprocal mass is at most the
left side of (7) plus C_c/(M+1), then take limits in that order.
If the incidence law is defined and k tends to infinity in its
probability, this is sufficient, but a lower bound on mu_clean is
not needed for the raw formulation (7).

Condition (K_c) or (7) is still UNPROVED. If supplied for every fixed c,
(5) would give clean packing o(W/sqrt r); add the already handled
removed and low-budget sectors to get the whole fixed-Gaussian packing
step. The earlier conditional slow-diagonal argument can then be used
with its exact scope. No complete repair compiler, all-target word,
coefficient-one theorem, or exact equality is being claimed here.
