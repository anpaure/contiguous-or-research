# The initial P-run diverges under Gaussian-short incidence

2026-09-08. Pure proof; no computation or original-project edits.
Complete-file reviews by the worktree lead and independent Gaussian
reader pass. The coordinator has accepted the theorem after its own
full read and independent helper audit. This is a one-root incidence
statement, not an eligible-label abundance theorem.

Let D be uniform among Dyck roots of semilength r>=1. Let p_0 be the
number of initial surviving P updates of its newborn before its first
interruption or consumption. Thus for a zero-budget root p_0=h-1.
There is an absolute constant C such that, for every integer m>=0,

    P_D(p_0<=m)<=min{1,C(m+1)^2/r}.                    (1)

In particular this estimate does not first condition on a short
lifetime. For fixed c>0 and H=floor(c sqrt(r)), it implies

    P_D(T<=H,p_0<=m)<=C(m+1)^2/r,                     (2)

    E[(T+2)1{T<=H,p_0<=m}]
       <=C_c(m+1)^2/sqrt(r).                         (3)

For every fixed m, (2) is o(r^(-1/2)) and (3) tends to zero. The
constants in (1)-(3) are uniform in m; the bounds may of course be
uninformative for large m.

## 1. A small initial P-run forces an original near-cap forest

Use the exact original forest decomposition from
`pbbs_original_forest_product.md`. Its suffix forests U_i, 0<=i<h,
have caps

    M_i=h-ceil(i/2).

For B>0, the exact first-interruption identity proved in
`pbbs_original_maximum_excess_coupling.md` gives

    max_i(ht(U_i)-i)=h-p_0.                            (4)

Moreover, the attaining index can be chosen among i<=p_0: the first
interruption occurs while the prefix is made from these original
forests, and the height-h witness lies in one of them. Consequently,

    p_0<=m and B>0
      implies some i<=m with ht(U_i)>=h-m+i>=h-m.      (5)

For h>2m and h>=2, a zero-budget root cannot satisfy p_0<=m, since
then p_0=h-1>m. Thus (5) covers the whole event under study at these
heights. Height one is treated separately below.

## 2. A positive generating-function certificate

Let C_j(x) count Dyck forests of height at most j, and write

    F_0=F_1=1,   F_j=F_(j-1)-xF_(j-2),
    C_j=F_j/F_(j+1),
    Z_h=C_h-C_(h-1)=x^h/[F_hF_(h+1)].

The original forest factors, with their additional h up-steps, form
exactly the positive product Z_h. Their cap multiset is cap 0 once,
cap h once, and caps 1,...,h-1 twice.

Fix h>2m, h>=2, and put q=h-m>h/2. For 0<=i<=2m define

    E_(h,m,i)(x)
      =Z_h(x)[C_(M_i)(x)-C_(q-1)(x)]/C_(M_i)(x).      (6)

This notation means replacing the single original U_i factor by its
height-at-least-q subfamily; it is a nonnegative generating function.
All these indices satisfy i<h and M_i>=q. Equation (5) gives the
coefficientwise union bound

    GF{height h, p_0<=m} <=sum_(i=0)^(2m)E_(h,m,i).    (7)

No independence after conditioning on semilength or lifetime is asserted.

At x=1/4,

    C_j=2(j+1)/(j+2),
    Z_h=2/[(h+1)(h+2)],
    [C_(M_i)-C_(q-1)]/C_(M_i)
       =[m+1-ceil(i/2)]/[(M_i+1)(q+1)].

The sum of the numerators over 0<=i<=2m is exactly (m+1)^2.
Therefore

    sum_i E_(h,m,i)(1/4)
      <=2(m+1)^2/[(h+1)(h+2)(h-m+1)^2]
      <=C(m+1)^2/(h+2)^4.                            (8)

This is the same positive near-cap event used in
`pbbs_growing_budget_uniform_bound.md`, equations (6), (8), and
Sections 2-3. Its analytic transfer works for any nonnegative integer
strip width m; the dynamical budget condition was used there only to
produce a witness, and is not needed once (7) is established.

## 3. Uniform fixed-size transfer, with its local-density factor

For clarity, the accepted transfer can be applied directly here.
Take z=1+(h+2)^(-2) and x_+=z/4. The positive bounded-height factors
satisfy, uniformly for 1<=d<=h,

    Z_d(x_+)/Z_d(1/4)<=e.

Since C_(M_i)-C_(q-1)=sum_(d=q)^(M_i)Z_d, its corresponding ratio is
at most e. Since C_(M_i)(x_+)>=C_(M_i)(1/4), (6) gives

    E_(h,m,i)(x_+)/E_(h,m,i)(1/4)<=e^2.               (9)

The replaced cap is at least q. At least one unchanged factor C_j
remains for every 0<=j<q, and their product is 1/F_q. Thus

    E_(h,m,i)(x)=[1/F_q(x)]H_(h,m,i)(x),              (10)

with H_(h,m,i) having nonnegative coefficients. Because q>h/2 and
q>=2, the tilted factor 1/F_q has a geometric mode whose maximal
point mass is at most C/(h+2)^2. Convolution with the other positive
factor cannot increase this maximum. This is an enumerative product
statement, not a reached-state independence hypothesis.

For the size variable normalized from E at 1/4,

    4^(-r)[x^r]E=E(1/4)E[z^N]z^(-r)P_z(N=r).

Combining (8)-(10) and log z>=1/[2(h+2)^2] proves

    #{D in Dyck_r: ht(D)=h,p_0<=m}
      <=C(m+1)^2 4^r(h+2)^(-6)
                      exp[-r/(2(h+2)^2)].            (11)

The uniform integral-plus-maximum estimate

    sum_(h>=2)(h+2)^(-6)exp[-r/(2(h+2)^2)]
        <=Cr^(-5/2)

therefore bounds the contribution of h>2m, h>=2, by

    C(m+1)^2 4^r/r^(5/2).                            (12)

## 4. Low heights and height one

The accepted exact-height estimate, with its amplitude retained, is

    [x^r]Z_h<=C4^r(h+2)^(-4)
                         exp[-r/(2(h+2)^2)].

As in Section 4 of `pbbs_growing_budget_uniform_bound.md`, summing over
h<=2m gives

    #{D in Dyck_r:ht(D)<=2m}
       <=C4^r r^(-3/2)exp[-r/(16(m+1)^2)]
       <=C(m+1)^2 4^r/r^(5/2).                       (13)

The first sum is empty when m=0. Height one has exactly one root at
each semilength. Its count is absorbed by the right side of (12) for
all r after increasing C; it covers the remaining m=0 endpoint.
Combining (12)-(13) and dividing by
Cat_r>=c4^r/r^(3/2) proves (1). Restricting to T<=H proves (2), and
multiplication by H+2 proves (3).

## 5. The actual F0 incidence consequence and its limit

The top-zero all-short reduction retains

    F0={GOOD,T<=H,Z_(0,0)=0},
    mu0=E[(T+2)1_F0]=Theta_c(1).

Its ACTUAL incidence law consequently satisfies

    P_inc,F0(p_0<=m)
      =E[(T+2)1_F0 1{p_0<=m}]/mu0
      <=C_c(m+1)^2/sqrt(r).                          (14)

In particular p_0 tends to infinity in probability under this law.
The uniform estimate also permits m=o(r^(1/4)), if useful. No
conditioning on F0 was substituted inside a forest-product law;
the numerator was bounded first under the original Dyck law.

This does not show that a long initial P-run supplies eligible
distinct shifted labels. Their actual lifted lifetimes and their
coverage of the sampled edge still require proof. No fresh law at a
shifted root, renewal process for original births, or k0-abundance
conclusion is asserted.
