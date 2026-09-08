# A larger fixed partner cutoff suffices for occupied-support decay

2026-09-08. Pure proof; no computation. Independent cover-selectors audit
passed. Root also read the full note and passed the incidence, Cauchy--Schwarz,
conditional-fibre, and scope checks.
This weakens a sufficient dynamical gate; it does not prove abundance.

Fix constants 0<c<=C<infinity and set H_c=floor(c sqrt(r)),
H_C=floor(C sqrt(r)). Use the same profile-measurable GOOD condition
and define the nested physical birth families

    F_c={GOOD, Z_(0,0)=0, T<=H_c},
    F_C={GOOD, Z_(0,0)=0, T<=H_C}.

Write U_c for the occupied edge union of F_c, K_c and K_C for the two
actual physical congestions, and mu_c,mu_C for their normalized raw
incidence masses. The accepted top-zero reduction gives mu_c=Theta_c(1)
and mu_C=O_C(1). All expectations below sample an actual F_c incidence;
partner congestion is always K_C.

## 1. Two deterministic inequalities

For every integer M>=1, split U_c according to K_C<M or K_C>=M. Every
edge in the first set has at least one base incidence. The second set
contains at most the total partner raw incidence divided by M. Hence

    |U_c|/W <= mu_c Pr_inc,c(K_C<M) + mu_C/M.        (1)

There is also the reciprocal bound

    (|U_c|/W)^2 <= mu_C mu_c E_inc,c[1/K_C].        (2)

Indeed, nesting ensures K_C>=K_c>=1 on U_c. Exact incidence counting is

    mu_c E_inc,c[1/K_C]
        = (1/W) sum_(e in U_c) K_c(e)/K_C(e)
        >= (1/W) sum_(e in U_c) 1/K_C(e).

Cauchy--Schwarz and sum_e K_C(e)=mu_C W now give (2). In particular
we do NOT replace the base incidence identity by |U_c|/W equal to
mu_c E_inc,c[1/K_C]; that equality would generally be false.

## 2. The exact top-row fibre still applies

Expose the base environment E=(full profile, all rows s>=1, offset j)
under actual F_c incidence. Its conditional top row is the same exact
uniform composition as in the accepted top-zero reduction: Z_(0,0)=0
and the other N=p-1 entries uniformly compose ell. The environment
keeps its base-c incidence law.

For partner shifts d in {j-H_C-1,...,j}, use that SAME original signed
trajectory and put

    a_d=lambda_1(2d),
    L_d=max(h,j-d-1,1),
    I_d^C=[floor(N_d(L_d-1)/2), floor(N_d(H_C)/2)-1],

with the accepted empty-interval conventions. Let k_(c->C)(E) count
distinct nonzero labels i for which some such d has a_d=i and 0 in I_d^C.
No shifted triangle is imposed.

Let Y be the number of these labels whose actual top gap is zero.
The base birth belongs to F_C. The same-particle virtual endpoint
argument and the exact F_C membership test therefore give

    1+Y <= K_C <= 2+Y.

Conditional on E, Y has precisely the hypergeometric zero-count law of
the accepted top-zero note, with k=k_(c->C). Consequently, on GOOD,

    E_inc,c[1/K_C | E] <= 2/[k_(c->C)(E)+1]          (3)

for sufficiently large r. Enlarging the partner window has not changed
the conditional fibre or its parameter ell/N.

Combining (2)-(3) gives

    |U_c|/W <= sqrt(2 mu_C mu_c
                      E_inc,c[1/(k_(c->C)+1)]).     (4)

## 3. The weaker sufficient gate and its scope

It is sufficient to prove the following statement:

    For every fixed c>0 there exists a finite C(c)>=c such that
    k_(c->C(c)) tends to infinity in actual base-c incidence probability.

Equations (1) or (4), with mu_C bounded for each fixed C, then imply
|U_c|=o(W). The accepted discarded-top-gap estimate transfers this to
ALL births with T<=H_c. The accepted occupied-support-to-packing theorem
then gives their packing o(W/sqrt(r)).

The larger cutoff must remain fixed while r tends to infinity. No
uniform bound in a growing C is asserted. This gate does not require
partner lifetime at most the base cutoff, but it still requires actual
physical lifetime and sampled-edge overlap tests. Its truth, a complete
repair compiler, and the coefficient-one conclusion remain unproved.
