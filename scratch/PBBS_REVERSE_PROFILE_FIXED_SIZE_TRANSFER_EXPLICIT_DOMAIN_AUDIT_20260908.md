# Explicit fixed-size reverse-profile transfer and probability domain

2026-09-08. Independent pure-proof audit by `exact_b_induction` of root's
finite guards and probability constants. No mathematical program was run.
Verdict: all displayed constants below pass.

To avoid the collision between an event name and the rate scale, write
Gamma for the positive scale and call the final good event mathcal G.

## 1. Domain and elementary scale bounds

Put

    X=log r,       d=log X >= 2^20,
    Gamma=r^(1/5) X^(-3/5),
    T=Gamma X=r^(1/5) X^(2/5),
    L=floor(T).

All logarithms are natural. The exact identity is

    r/T^3=Gamma^2.                                       (1)

On this domain,

    T>=2,       T/2<=L<=T,
    L+2<=2T,   L<=r/2,
    Gamma^2>=2^50 X.                                     (2)

For the last inequality,
`log(Gamma^2/X)=(2X-11d)/5`. Since `X=exp(d)>=d^2/2`, this is at least
`d(d-11)/5`, which exceeds `50log2` already for d>=32.
The present domain is much larger. The comparison T<=r/2 follows from
`log T=X/5+2d/5` and `4X-2d>=5log2`, immediate from X>=2d here.
The remaining floor bounds in (2) follow from T>=2.

In particular L>=20, all tested depths lie before r, and

    sqrt(r)/(L+2) >= Gamma sqrt(T)/2 >= 2^24 sqrt(X)>800. (3)

No estimate below needs a further unspecified sufficiently-large
threshold.

## 2. The relative-profile event A

Under the uniform Dyck_r law define

    A={ |a_j-r/(j+1)|<=.01 r/(j+1), 0<=j<=L+1 }.

The finite concentration inequality in section 2, equation (4), of
`scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md` states

    Pr(|a_j-r/(j+1)|>(4+x)sqrt(r))<=2exp(-x^2/6),

uniformly in every depth j. At the desired threshold its x parameter
is `.01sqrt(r)/(j+1)-4`. By (3) this is at least
`sqrt(r)/[200(L+2)]`. Therefore

    Pr_r(A^c)
       <=2(L+2)exp[-r/(240000(L+2)^2)].                  (4)

Equation (1) and L+2<=2T make the negative exponent in (4) at least
`Gamma^2 T/960000>=Gamma^2/480000>2^-19 Gamma^2`.
Also `log(2(L+2))<=2X<=2^-49 Gamma^2`, by (2).
These inequalities prove the requested weaker clean bound

    boxed: Pr_r(A^c)<=exp(-2^-24 Gamma^2).                (5)

## 3. Dropping restrictions before applying the reverse kernel

Set

    ell_s=a_s-2a_(s+1)+a_(s+2),
    mu_s=(2a_(s+1)+1)/[(s+1)(s+3)],
    B={ mu_s/2<=ell_s<=2mu_s, 0<=s<L }.

Under `P*(D)=4^(-|D|)/2`, conditioning on the ENTIRE deeper profile
makes ell_s a negative-binomial variable with mean mu_s. Its exact law
and the finite two-sided tail are proved in
`scratch/PBBS_REVERSE_PROFILE_NB_TAILS_AND_EXISTENCE_ONLY_SMOOTHING_INDEPENDENT_AUDIT_20260908.md`:

    P*(ell_s outside [mu_s/2,2mu_s] | deeper profile)
       <=2exp(-mu_s/32).                                 (6)

For a given s<L, let C_s impose only the A-range on
`b=a_(s+1)`. On C_s,

    mu_s>=1.98r/[(s+1)(s+2)(s+3)]
          >=r/(L+2)^3>=Gamma^2/8.                        (7)

The event C_s is measurable with respect to the deeper profile, so
integrating (6) over C_s proves a bound `2exp(-Gamma^2/256)` under P*.

This is used at fixed r as follows: the event `{a_0=r} intersect A`
is a subset of C_s. Drop `{a_0=r}` and the other A constraints BEFORE
applying (6), then divide by the fixed-size conditioning probability.
The elementary central-coefficient bound gives

    P*(a_0=r)=Cat_r/(2*4^r)
       >=1/[2(r+1)(2r+1)],

so its inverse is at most `2(r+1)(2r+1)<=12r^2`.
No reverse-kernel assertion is being made after conditioning on a_0=r.
Union over the L indices yields exactly

    Pr_r(A intersect B^c)
       <=24r^2 L exp(-Gamma^2/256).                      (8)

Since L<=r and `log(24r^3)<=4X<=2^-48 Gamma^2`, (8) implies

    boxed: Pr_r(A intersect B^c)<=exp(-Gamma^2/512).       (9)

## 4. Primitive original rows on A intersect B

Now condition on a FULL original profile satisfying A intersect B.
Its incoming-gap row at depth s is the uniform composition of ell_s
into odd `p_s=2a_(s+1)+1` parts. This is the original finite fibre law,
not the auxiliary reverse kernel of the previous section.

By (7) and B,

    ell_s>=mu_s/2>=Gamma^2/16.

Also A gives `p_s>=1.98r/(s+2)>=r/(L+1)`, which is at least
`r/(L+2)^3>=Gamma^2/8`. Hence

    min(p_s,ell_s)>=Gamma^2/16.                           (10)

The exact composition repetition bound in
`scratch/PBBS_SUPERPOLYNOMIAL_PERIOD_REGULARITY_AND_PRIMITIVE_ROWS_INDEPENDENT_AUDIT_20260908.md`
is

    Pr(row nonprimitive | full profile)
       <=2p_s exp[-(2log2/3)min(p_s,ell_s)].

Using `2log2/3>=1/3`, p_s<=2r+1<=3r, and L<=r, the union bound is

    Pr_r(A intersect B intersect {some tested row nonprimitive})
       <=6r^2 exp(-Gamma^2/48).                          (11)

Because `log(6r^2)<=3X` and (2) holds, this gives

    boxed: the probability in (11)<=exp(-Gamma^2/96).     (12)

There are no empty-core or zero-row issues on A intersect B: (10)
forces every relevant mass and row length to be positive and large.
No independence of rows was needed for this union bound.

## 5. The complete good-event estimate

Define mathcal G to be A intersect B together with primitivity of the
first L original rows. Equations (5), (9), and (12) give

    Pr_r(mathcal G^c)
       <=exp(-2^-24 Gamma^2)
          +exp(-Gamma^2/512)+exp(-Gamma^2/96)
       <=3exp(-2^-24 Gamma^2)
       <=exp(-2^-26 Gamma^2).                            (13)

The last inequality follows from
`(2^-24-2^-26)Gamma^2>=log3`, which has substantial room by (2).
Thus the stated probability has no polynomial prefactor left over.

## 6. The full-law smoothing interface at this scale

Choose free indices every third depth in `[ceil(L/2),L-2]`, and expose
all other profile entries. There are at least L/8 such indices, each
at least ten. Let the exposed configuration be one that admits ANY
completion satisfying A intersect B.

The cited existence-only smoothing theorem applies to the independent
FULL conditional laws of the free coordinates. For each chosen s it gives

    max_x Pr(a_s=x | exposed)
       <=min(1,2^20/sqrt(m_s)),
    m_s=r/(s+1)^3.

Since s+1<=L and L<=T,

    m_s>=r/L^3>=r/T^3=Gamma^2.

Consequently the precise common bound is

    boxed: rho<=2^20/Gamma.                              (14)

The estimate uses only the existence of one A intersect B completion.
It does NOT condition the free coordinates on A, B, or mathcal G.
In particular primitivity must not be imposed on these conditional laws.
In a sieve argument it may first be used to deduce necessary divisors
on mathcal G and then dropped when upper-bounding their probability.

This audit verifies the probability domain, all numerical constants,
the fixed-size normalization, and the exact conditioning interface.
It does not itself certify the subsequent number-theoretic sieve or
the final constant in a word-length rate.
