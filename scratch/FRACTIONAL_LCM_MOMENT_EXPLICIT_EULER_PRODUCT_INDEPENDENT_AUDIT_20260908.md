# Fractional LCM moment: explicit Euler-product audit

2026-09-08. Independent pure-arithmetic audit by `exact_b_induction`.
No mathematical program was run. Verdict: the stated finite bound, with
the constant 96, passes. The application to profile probabilities is
separate from this lemma.

## 1. Finite statement and weighted reduction

Let L be an integer with `L>=2^16`, let

    1/3<=beta<=1/2,    0<eta<=1/6,
    alpha=1+eta-beta,
    Y=(2L/log L)^(1/beta),

and let M>=1. All logarithms are natural, and all u_i in the sum below
are POSITIVE integers. Then

    boxed:
    sum_(1<=u_1,...,u_L<=M) lcm(u_1,...,u_L)^(-alpha)
      <=M^(beta L)(1+eta^(-1))^L exp(96Y).                (1)

For each bounded tuple, `product_i u_i^beta<=M^(beta L)`. Thus the left
side is at most M^(beta L) times

    sum_(u_1,...,u_L>=1) lcm(u)^(-alpha) product_i u_i^(-beta).

By unique factorization and nonnegative summation this last series has
Euler factors

    F_p=sum_(e_1,...,e_L>=0)
           p^[-alpha max_i e_i-beta sum_i e_i].           (2)

The estimates below also prove convergence. One may first form finite
prime products and then take monotone limits, so no unproved interchange
of a conditionally convergent series is used.

## 2. Elementary prime-counting estimates

We use the finite bound

    pi(y)<=8y/log y,     y>=2.                            (3)

Here is an elementary derivation. Every prime between m and 2m divides
`binom(2m,m)`, so `theta(2m)-theta(m)<=2m log2`. Summing at dyadic m
gives `theta(y)<=4y log2`. Split primes at sqrt(y); the larger primes
each have logarithm at least half log y. Hence

    pi(y)<=sqrt(y)+8log2 * y/log y.

Since `log y/sqrt(y)<=2/e<1` and `log2<=3/4`, this is at most
`7y/log y`, and in particular proves (3).

For Y>=4 and beta in the stated range, partial summation gives

    sum_(p<=Y) p^(-beta)<=48Y^(1-beta)/log Y.              (4)

For explicit margin, put a=1-beta and split at sqrt(Y). The small part
is at most `2Y^(a/2)`. The large part, by (3), is at most

    [8+16beta/(1-beta)]Y^a/log Y<=24Y^a/log Y.

Moreover `2log Y/Y^(a/2)<=2log Y/Y^(1/4)<=8/e<4`.
Thus the constant 28 would already suffice in (4); 48 is safe.

For every exponent a>=4/3, another partial summation gives

    sum_(p>Y) p^(-a)
       <=8a integral_Y^infinity t^(-a)/log t dt
       <=[8a/(a-1)]Y^(1-a)/log Y
       <=32Y^(1-a)/log Y.                               (5)

Dropping the negative boundary term here is an upper bound. The
integral converges because a>1.

## 3. Uniform finite guards for Y

Write lambda=log L. On L>=2^16,

    Y>=L^(5/3),   log Y>=(3/2)log L,   Y>=4.             (6)

To check the stronger first inequality, beta<=1/2 gives
`Y>=(2L/log L)^2`. It suffices that `lambda<=2exp(lambda/6)`.
The ratio `2exp(lambda/6)/lambda` increases for lambda>6.
At `lambda_0=16log2`, we have `6<lambda_0<=12`, while
`2exp(lambda_0/6)=2^(11/3)>12`. This proves the comparison for all
the required L, and hence (6).

Also `log L<=L/2` for L>=2. Thus, when p>Y and z=p^(-beta),

    z<=log L/(2L)<=1/4,
    Lz/(1-z)<= (2/3)log L.                              (7)

Strict inequalities at p>Y are unnecessary for the upper bounds.

## 4. Small primes

Since alpha>0, dropping the factor involving the maximum in (2) gives

    F_p<=(1-p^(-beta))^(-L).

For every prime p, `p^(-beta)<=2^(-1/3)<4/5`, so
`-log(1-p^(-beta))<=5p^(-beta)`. Equations (4) and (6), with
`Y^beta=2L/log L`, imply

    sum_(p<=Y) log F_p
       <=240L Y^(1-beta)/log Y
       =120Y log L/log Y
       <=80Y.                                           (8)

No small-prime convergence estimate is needed because this product is
finite.

## 5. Large primes: separate the one-coordinate support exactly

For p>Y write

    z=p^(-beta),    w=p^(-alpha),    u=z/(1-z),
    a_p=p^(-(1+eta)).

Tuples of exponents with exactly one positive coordinate contribute
exactly

    L sum_(k>=1) p^[-(alpha+beta)k]
       =L a_p/(1-a_p).                                 (9)

For support size at least two, the factor `w^(max e_i)` is at most w.
Summing the remaining positive exponents independently yields the bound

    w sum_(j=2)^L binom(L,j)u^j
       <=(w/2)(Lu)^2 exp(Lu).                            (10)

Indeed `binom(L,j)<=L^j/j!`, and the exponential tail starting at degree
two is at most `(Lu)^2 exp(Lu)/2`.

By (7), `u<=4z/3` and `exp(Lu)<=L^(2/3)`. Therefore (10) is at most

    L^(8/3) w z^2
       =L^(8/3)p^(-(1+eta+beta)).                        (11)

The numerical coefficient is valid because `(1/2)(4/3)^2=8/9<1`.

Since `(1-a_p)^(-L)=(1+a_p/(1-a_p))^L>=1+L a_p/(1-a_p)`,
equations (9)-(11) imply

    F_p <=(1-a_p)^(-L)
             [1+L^(8/3)p^(-(1+eta+beta))].               (12)

Thus the single-support contribution is retained inside the exact
zeta factor rather than being charged a divergent coarse beta-power.

## 6. Sum the large-prime correction and finish

Use (5) with `a=1+eta+beta>=4/3`. Taking logarithms of the bracket
in (12) and using eta>0 gives

    sum_(p>Y) log[1+L^(8/3)p^(-(1+eta+beta))]
       <=32 L^(8/3)Y^(-eta-beta)/log Y
       <=16 L^(5/3) log L/log Y
       <=(32/3)L^(5/3)
       <=(32/3)Y.                                       (13)

Together with (8), (12), and the full-prime zeta product,

    product_p F_p
       <=zeta(1+eta)^L exp[(80+32/3)Y]
       <=zeta(1+eta)^L exp(96Y).                         (14)

Enlarging the large-prime zeta product to all primes only increases
the bound. Its convergence follows from eta>0; the correction product
converges by (5). Finally the integral bound for the decreasing series
gives

    zeta(1+eta)<=1+integral_1^infinity t^(-1-eta)dt
                =1+eta^(-1).

Substitution into the weighted reduction in section 1 proves (1).

## 7. Scope and the profile-application constant

The finite parameter domain, positivity, support split, Euler-product
convergence, prime estimates, and constant 96 have all been checked.
The actual exponent debit obtained is at most `(272/3)Y<96Y`.

For reference, the separately audited joint-profile bound is in
`scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`.
Its weaker convenient form is
`16(L+1)((L+1)!)^2 r^(-L/2)`. With n=2r+1 and r>=n/3, a valid
coefficient of n^(-L/2) is

    A_L=16(L+1)3^(L/2)((L+1)!)^2.

The larger root choice with 3^L is therefore safe as well. Conditioning,
period implications, and asymptotic optimization of this application
are not premises of the fractional-LCM lemma and require their separate
audit.
