# Bounded small divisors and the explicit long-period rate

2026-09-08. Independent arithmetic audit by exact_equality_structure.
All logarithms are natural. No mathematical computation was run.

The finite small-divisor lemma below passes with a=2^-24. Together with
the independently proved regular-profile/primitive-row estimate, it gives

    nu(k)/W(k) <= 1+exp[-2^-32 (log k)^(6/5)]              (1)

for every integer

    k >= ceil(exp(exp(256))).                             (2)

The construction is the already proved height-adaptive PBBS word and its
exact one-coordinate lift. The argument does not assert a product lower
bound for its period factors and does not prove nu(k)=B(k).

## 1. A completely finite small-divisor statement

Let x and v be real/integer parameters with v a positive integer,

    log log x>=12,     v>=x.

Write D_x(v) for the number of positive integer divisors of v at most x.
If

    D_x(v) >= (1/2)x^(1/6)/log x,                         (1.1)

then

    log v >= 2^(-102/5)(log x)^(6/5)
           >=2^-24(log x)^(6/5).                         (1.2)

No squarefreeness assumption is made about v. Nor must the divisors
counted in (1.1) be consecutive integers or coprime.

## 2. Elementary prime estimates with explicit constants

Let theta(y)=sum_(p<=y) log p and pi(y)=#{p<=y}. The standard central
binomial argument gives, for integer m>=1,

    theta(2m)-theta(m)<=log binom(2m,m)<=2m log2.

Every prime m<p<=2m divides the binomial numerator and not its denominator.
Summing this bound at powers of two, then rounding y upward to the next
power of two, gives

    theta(y)<=4y,          y>=2.                         (2.1)

More explicitly, if 2^j<=y<2^(j+1), the sum is less than
2^(j+2)log2<=4y log2<4y. The coarser displayed constant includes every
small case as well.

Splitting the primes at sqrt(y),

    pi(y)<=sqrt(y)+2theta(y)/log y
          <=sqrt(y)+8y/log y<=16y/log y,    y>=2.          (2.2)

The final inequality can even use 9 in place of 16: log y<=sqrt(y),
as follows by maximizing log y/sqrt(y), whose maximum is 2/e<1.

Put M=log v. On the domain of Section 1, M>=log x>=exp(12). For
1/12<=sigma<=1/6, split the distinct prime divisors of v at sqrt(M)
and M. The small primes contribute at most

    pi(sqrt M)<=32sqrt(M)/log M
                <=32M^(1-sigma)/log M.                  (2.3)

For the middle range, partial summation and (2.2) give

    sum_(sqrt M<p<=M) p^(-sigma)
      <=pi(M)M^(-sigma)
         +sigma integral_(sqrt M)^M pi(t)t^(-sigma-1)dt
      <=[16+32sigma/(1-sigma)]M^(1-sigma)/log M
      <=(112/5)M^(1-sigma)/log M.                        (2.4)

Dropping the nonpositive lower boundary term in partial summation is
legitimate. Also log t>=0.5log M throughout its integral.

The product of distinct prime divisors of v is at most v, so their
logarithms sum to at most M. Hence there are at most M/log M prime
divisors larger than M, and their contribution is at most

    M^(1-sigma)/log M.                                   (2.5)

Combining (2.3)-(2.5) gives the stronger constant 277/5<56. In particular
the proposed deliberately loose bound is valid:

    sum_(p|v) p^(-sigma)
      <=512 M^(1-sigma)/log M,
      1/12<=sigma<=1/6.                                 (2.6)

## 3. Rankin's finite divisor bound

For sigma>0, each divisor d<=x has (x/d)^sigma>=1. Therefore

    D_x(v)<=x^sigma sum_(d|v)d^(-sigma)
            <=x^sigma product_(p|v)(1-p^(-sigma))^(-1).

This bounds the finite prime-power sums by infinite geometric sums;
it does not erase or assume anything about v's exponents. For sigma
in the range above,

    1-2^(-sigma)>=1-2^(-1/12)>1/32.

For an elementary check of the strict numerical inequality,
(31/32)^12>=1-12/32=5/8>1/2, by Bernoulli's inequality. Taking twelfth
roots gives 31/32>2^(-1/12).

Using -log(1-z)<=z/(1-z) and (2.6), we obtain

    log D_x(v)
      <=sigma log x + 2^14 M^(1-sigma)/log M.             (3.1)

The factor is exactly bounded by 32 times 512; there is no implicit
constant or uncounted small-prime term.

## 4. Optimize within the stated finite domain

Put X=log x and z=log X>=12. If M>=X^(6/5), (1.2) already holds.
Otherwise assume

    X<=M<X^(6/5),
    sigma=1/6-1/log X.

Then 1/12<=sigma<1/6, so (3.1) applies. The logarithm of (1.1) is

    log D_x(v)>=X/6-log X-log2.

Subtracting sigma X from this and comparing with (3.1) yields

    2^14 M^(1-sigma)/log M
      >= X/log X-log X-log2
      >= X/(2log X).                                    (4.1)

The last inequality is uniformly valid for z>=12. It is enough that
exp(z)>=2z(z+1); at z=12, exp(12)>2^12>2*12*13, and the ratio
exp(z)/[2z(z+1)] increases for z>=12. Also log2<1.

Since log M<(6/5)log X,

    M^(1-sigma)=M^(5/6)exp(log M/log X)
                 <=exp(6/5)M^(5/6)<4M^(5/6).            (4.2)

For the final numerical comparison, log4=2log2>=4/3>6/5.
Combining (4.1)-(4.2) and using log M>=log X gives

    2^16 M^(5/6)/log X >= X/(2log X),
    M^(5/6)>=2^-17 X,
    M>=2^(-102/5)X^(6/5)>=2^-24X^(6/5).

This proves the finite lemma, including the equality endpoint z=12.
The use of the deliberately larger constant 512 in (2.6) is fully
accounted for in the final exponent 102/5.

## 5. Certified PBBS input and the floor-free divisor count

The independent full proof in
PBBS_SUPERPOLYNOMIAL_PERIOD_REGULARITY_AND_PRIMITIVE_ROWS_INDEPENDENT_AUDIT_20260908.md
has been read for this audit. Its exact conclusion is as follows. Put

    u=log r>=2^20,
    L=floor(r^(1/6)/u),
    Delta=r/[100(L+3)^3].

For a uniform original Dyck root, with probability at least

    1-exp[-2^-26 u^6],                                  (5.1)

all r_s, 0<=s<=L+1, lie within Delta of r/(s+1), and every first-L
original incoming-gap row is primitive. On this event all these ranks
are positive and strictly decreasing. The proof uses the finite,
all-depth original-profile concentration

    Pr(|r_s-r/(s+1)|>(4+x)sqrt r)<=2exp(-x^2/6),

not a fixed-depth asymptotic or a dynamically resampled distribution.
The concentration proof in Section 2 of
PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md was also read.

The arithmetic in the probability proof checks: Delta/sqrt r>=u^3/800;
the profile union is at most exp(-2^-25u^6); regular rows have both
mass and length at least B=r/(L+3)^3>=exp(u/2)u^3/8>=u^6;
the conditional primitive-row union is at most exp(-u^6/4).
Their sum is (5.1), without a polynomial prefactor. Uniform physical
middle states have exactly the same law on these rotation-invariant
events. In what follows we may safely weaken 2^-26 to

    b=2^-28.                                             (5.2)

On this good event, the invariant-row period theorem gives

    lcm_(0<=s<L)(n_s n_(s+1)) divides v,
    n_s=2r_s+1.

Consequently n_0,...,n_L are L+1 distinct divisors of v, each at most
n=n_0=2r+1, and v>=n. The count is L+1, not merely L. Thus

    D_n(v)>=L+1>r^(1/6)/log r
               >(1/2)n^(1/6)/log n.                     (5.3)

Here r=(n-1)/2>=n/3, 3^(1/6)<2, and log r<log n. The plus one before
the floor removes any need for a separate asymptotic rounding loss.
No product of the distinct divisors is claimed to divide v.

Whenever log log n>=12, applying Section 1 with x=n proves, on this
same good event,

    v>=exp[a(log n)^(6/5)],      a=2^-24.                 (5.4)

## 6. A finite bound before the final threshold simplification

The already proved height-adaptive compiler gives relative collar charge
E[(2h-1)/v] under uniform physical middle states. Everywhere v>=n and
2h-1<n; on the good event use (5.4). Therefore, provided

    log r>=2^20,     log log n>=12,

the deterministic construction satisfies the explicit finite bound

    nu(n)/W(n)
      <=1+n exp[-a(log n)^(6/5)]
           +exp[-b(log r)^6],
    n=2r+1, a=2^-24, b=2^-28.                            (6.1)

The sharper exceptional coefficient 2^-26 from (5.1) is also available.
The bound (6.1) charges bad states at most by their probability, rather
than multiplying that probability by n or by a cycle-count factor.
If an integer length bound is wanted, floor W(n) times the whole
displayed excess. The existing exact one-coordinate lift preserves
the normalized bound when passing from n to n+1.

## 7. Final constants and both parities

Let k satisfy (2), choose the odd source dimension n=k for odd k and
n=k-1 for even k, and put

    Z=log k,     X=log n,     u=log((n-1)/2).

At this threshold k>=16, and r=(n-1)/2>=k/4>=sqrt k.
Thus u>=Z/2 and X>=Z/2. Since log Z>=256,

    log X>=256-log2>255,
    u>=exp(256)/2>exp(255)>2^20.

These verify all the finite domains of Sections 1 and 6. In addition
X^(1/5)>exp(51)>2^25=2/a. Hence

    n exp[-aX^(6/5)]
      <=exp[-(a/2)X^(6/5)]
      <=exp[-2^-27 Z^(6/5)],                             (7.1)

because 2^(6/5)<4. For the exceptional part, u>=1 permits a deliberately
large weakening from u^6 to u^(6/5), giving

    exp[-b u^6]
      <=exp[-b u^(6/5)]
      <=exp[-2^-30 Z^(6/5)].                             (7.2)

The good contribution in (7.1) is smaller than (7.2). Their sum is at most
2exp[-2^-30 Z^(6/5)]. Finally

    (2^-30-2^-32)Z^(6/5)
      =3*2^-32 Z^(6/5)>log2

throughout the stated domain; for example Z>=exp(256)>2^256 and
Z^(6/5)>=Z make this immediate. It follows that

    2exp[-2^-30 Z^(6/5)]<=exp[-2^-32 Z^(6/5)].

Applying the exact even lift when needed proves (1) for every k in (2).
There is no extra multiplicative two from that lift: its word length
and the central width both double exactly.

## 8. Scope of certification

The new arithmetic step is fully finite, using only elementary prime
counts and the stated divisor-count hypothesis. The growing-profile
probability and deterministic primitive-row divisibility are explicitly
linked and were independently read; all their finite guards needed here
are met at (2). The construction's complete target coverage remains the
previously proved height-adaptive coverage theorem, so this argument is
an improvement in its rigorous size bound rather than a new unverified
compiler. The result is superpolynomial relative convergence to one.
It is not a certificate that the additive difference from B(k) is zero.
