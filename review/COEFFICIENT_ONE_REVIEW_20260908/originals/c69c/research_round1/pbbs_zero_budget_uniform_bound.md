# A uniform semilength bound for the full zero-interruption PBBS class

Date: 2026-09-07. Pure proof; no computation or enumeration.

Using the independently audited terminal-cap lemma in
pbbs_uninterrupted_critical_weight.md, this note proves

    #{D in Dyck_r:T(D)=ht(D)} = O(4^r/r^2)
                              = O(Cat_r/sqrt(r)).        (1)

This sums the complete zero-interruption class over all heights. It is
not a bound on all short lifetimes: classes with positive budget
T-ht(D)=2rho+sigma remain outside (1). No physical packing conclusion
is asserted. The terminal-cap argument and the positive geometric
coefficient transfer were independently checked by the recency-gate agent.

## 1. Positive coefficientwise input

Let F_0=F_1=1 and F_m=F_(m-1)-x F_(m-2). For exact height h, put

    a=floor((h+1)/2),       b=ceil((h+1)/2).

The complete T=h class is bounded coefficientwise by

    G_(h,h)(x) <= U_h(x):=x^h/[F_h(x)F_a(x)F_b(x)].      (2)

The underlying proof uses the unique inverse record-peeling encoding,
all necessary inverse checks, and the terminal-forest caps
ht(V_j)<=ceil(j/2). It does not identify the full class with a protected
fixed-spine family.

At the critical point x=1/4,

    U_h(1/4)=2/[(h+1)(a+1)(b+1)] <= 8/(h+1)^3.         (3)

We retain this amplitude when extracting coefficients.

## 2. The positive geometric representation

The path-matrix factorization is

    F_m(x)=product_(k=1)^floor(m/2) [1-4q_(m,k)x],
    q_(m,k)=cos^2(pi*k/(m+1)).                           (4)

Thus

    F_m(1/4)/F_m(z/4)
      = product_k (1-q_(m,k))/(1-q_(m,k)z)              (5)

is the probability generating function of a sum of independent
geometric random variables, each on {0,1,...} with probability mass
(1-q)q^n. This independence describes the positive coefficient bound
U_h; it is not an independence claim for PBBS transport histories.

Let N_h be the sum of the geometric variables from the three factors
m=h,a,b. Equations (2)-(5) give exactly

    4^(-r)[x^r]U_h(x)
      = U_h(1/4) P(N_h=r-h),                            (6)

for r>=h; the coefficient vanishes for r<h.

For h>=2, the factor m=h contains the mode

    q_*=cos^2(pi/(h+1)).

Convolution cannot increase the maximal point mass of one component.
Therefore P(N_h=n)<=1-q_*<=pi^2/(h+1)^2. To get a simultaneous tail
bound, we apply the same observation after a small positive tilt.

## 3. A uniform tilt and local bound

Set

    delta=1/(h+1)^2,       z=1+delta.

For every mode of every m<=h, the angle is at most pi/2 and

    1-q_(m,k) >= 4k^2/(m+1)^2.

In particular delta*q/(1-q)<=1/4, so zq<1. The exact geometric mean
identity is

    sum_k q_(m,k)/(1-q_(m,k)) = m(m-1)/6.               (7)

One direct proof uses 1/F_m=product_(j=0)^(m-1) C_j, together with
C_j(1/4)=2(j+1)/(j+2) and
(1/4)C_j'(1/4)/C_j(1/4)=j/3. Taking logarithmic derivatives gives (7).

For 0<=v<=1/4, -log(1-v)<=4v/3. Consequently

    log E[z^N_h]
      <= (4/3)delta [h(h-1)+a(a-1)+b(b-1)]/6
      <= 4/9 < 1.                                      (8)

The last bound uses a+b=h+1 and
h(h-1)+a(a-1)+b(b-1)<=2(h+1)^2.

Under this tilt, all geometric parameters become zq. The h-mode's
maximal point mass is 1-zq_*<=1-q_*. Hence

    P(N_h=n)
      = E[z^N_h] z^(-n) P_z(N_h=n)
      <= e*pi^2/(h+1)^2 * exp[-n/(2(h+1)^2)],           (9)

because log(1+delta)>=delta/2. Combining (3), (6), and (9) gives the
explicit uniform estimate, for h>=2 and r>=h,

    [x^r]G_(h,h)(x)
      <= 8e*pi^2 * 4^r/(h+1)^5
           * exp[-(r-h)/(2(h+1)^2)].                   (10)

The h=1 class is just D=10, so contributes nothing for r>1.

## 4. Summing every height

For 2<=h<=r/2, the summand in (10), after removing its absolute
constant and 4^r, is bounded by

    (h+1)^(-5) exp[-r/(4(h+1)^2)].                      (11)

The sum of (11) is O(r^(-2)). For example the corresponding function
f(x)=x^(-5)exp[-r/(4x^2)] is unimodal, its maximum is O(r^(-5/2)), and

    integral_0^infinity f(x) dx = 8/r^2.

A sum of a nonnegative unimodal function is bounded by its integral
plus twice its maximum. For h>r/2, dropping the exponential gives
sum(h+1)^(-5)=O(r^(-4)). This proves

    sum_(h=1)^r [x^r]G_(h,h)(x) = O(4^r/r^2).

The standard Catalan asymptotic yields the second equality in (1).

## 5. What this does and does not resolve

The estimate sums all positive weights in the zero-budget class; it is
not a bound on a single canonical scheme. It also supplies a uniform
joint (r,h) inequality, with both amplitude and exponential factor retained.
Thus zero-interruption histories alone have vanishing Catalan density,
even if all heights are permitted.

The pending task is to bound positive-budget histories, especially
2rho+sigma up to a Gaussian cutoff minus the height. No comparison
between those histories and the independent geometric bound in (5) is
proved here. Neither (1) nor (10) controls that missing sum, and a
quotient root count alone must not be silently promoted to a physical
edge-disjoint packing estimate.
