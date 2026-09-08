# Sharp residue and negative-binomial bounds, with the exact depth integral

2026-09-08. Independent audit by exact_equality_structure of the local
estimates and rational certificate in DEPTH_PRODUCT_ADVANCE. The pure
proof passes. The specified finite arithmetic was independently executed
on h100 under 30 CPU seconds, 45 wall seconds, and 512 MiB address space;
it returned PASS. No mathematical program ran locally.

The proved inputs are the sharp residue discrepancy, sharpened log-gcd
bound, a finite 1.001/sqrt(2pi pq) negative-binomial atom bound, the
depth-dependent pass envelope, and the exact integral lower certificate
S>1.41158740928968>1.41. The subsequent finite product, probability
transfer, word charge and parity passage are separate audits.

## 1. The sharp residue discrepancy for a unimodal integer law

Let U be integer-valued with unimodal mass p_j and maximum rho. For
0<t<=rho, its superlevel set {j:p_j>=t} is a finite interval of integers
(apart from irrelevant endpoint choices at a level). For an interval
of N consecutive integers, the number in any one residue class modulo
d differs from N/d by at most 1-1/d. Integrating these count discrepancies
over the mass levels proves

    |Pr(U=b mod d)-1/d|<=(1-1/d)rho.                    (1.1)

Infinite support is permitted: the superlevel intervals are finite at
each positive level because the total mass is one, and the layer-cake
identity applies by Tonelli. A point mass shows that the constant
1-1/d is sharp in general.

Suppose Y=2U+1>=Y_0>1. For each odd prime power p^j, (1.1) gives

    Pr(p^j divides Y)<=rho+(1-rho)/p^j.

The probability for powers of two is zero, so the same upper bound is
harmless there. For a positive integer candidate v put

    S(v)=sum_(p^j divides v)(log p)/p^j.

The exact finite prime-power expansion of log gcd(Y,v) yields

    E log gcd(Y,v)<=(1-rho)S(v)+rho log v,

    Pr(Y divides v)
      <=[(1-rho)S(v)+rho log v]/log Y_0.                 (1.2)

If an upper bound for the maximal atom is used in place of rho, the
right side is nondecreasing in that bound, because log v>=S(v).
The application below has its atom bound below one. The previously
proved finite arithmetic bound S(v)<=log(2+log v)+20 therefore applies
directly; see PBBS_LOG_GCD_DIVISIBILITY_AND_FINITE_REVERSE_TEST_AUDIT_20260908.md.

## 2. A finite sharp atom bound for NB(p,q)

Let Z have mass

    Pr(Z=m)=binom(p+m-1,m)(1-q)^p q^m,
    p a positive integer, 0<q<=1/4,
    mu=pq>=1000.

Then

    boxed: max_m Pr(Z=m)
      <=1001/[1000 sqrt(2pi mu)].                       (2.1)

This mu is the product pq, not the NB mean pq/(1-q).

Put N=p-1 and choose the mode m=floor(Nq/(1-q)); if the quotient is
an integer, it is one of the two equal modes. The assumptions ensure
N,m>=1. Write z=N+m. The finite Stirling inequalities are

    sqrt(2pi n)(n/e)^n < n!
       <sqrt(2pi n)(n/e)^n exp(1/(12n)),    n>=1.         (2.2)

The official DLMF states that for positive real arguments the remainder
of the logarithmic gamma expansion has the sign of, and magnitude
bounded by, its first omitted term. Applied at integer n, and using
n!=n Gamma(n), this gives (2.2).
[DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii), together with
[equation 5.11.1](https://dlmf.nist.gov/5.11.E1).
Those official pages were opened and checked during this audit.

Apply the upper factorial estimate to z! and the lower estimates to
m! and N!. The factor

    z^z q^m(1-q)^N/(m^m N^N)

is at most one, since q^m(1-q)^N is maximized at q=m/z. Hence the
modal probability P satisfies

    P<=(1-q)exp(1/(12z))sqrt[z/(2pi mN)].                (2.3)

The floor in m causes no uncharged approximation. It gives

    m>=(Nq-1)/(1-q),
    z/(mN)=1/m+1/N<=1/(Nq-1)<=1/(mu-5/4).              (2.4)

Here Nq=mu-q>=mu-1/4. Also z>=N>=4mu-1>=mu. Squaring (2.3),
using (2.4), and dropping (1-q)^2<=1 gives

    2pi mu P^2
      <=exp(1/(6mu))/(1-5/(4mu))
      <=[6000/5999][800/799]
      <(1001/1000)^2.                                  (2.5)

For the middle step, exp(x)<=1/(1-x) for 0<=x<1, and mu>=1000.
The last comparison was reproduced with exact rational arithmetic:

    [6000/5999][800/799]=4800000/4793201
      <1002001/1000000.

This proves (2.1), uniformly over the entire infinite NB support.

## 3. The depth-dependent pass envelope and its finite domain

Put X=log r>=65536, D=log X, and

    T=(rX^2)^(1/5),     L=floor(2T).

Use the inherited exact auxiliary reverse kernel at depth 0<=s<L:

    a_s=2b-c+NB(p=2b+1,q=(s+2)^(-2)),
    b=a_(s+1), c=a_(s+2).

Assume only the two child values are within one percent of their harmonic
centers r/(s+2) and r/(s+3). All statements below concern the FULL
conditional parent law; no upper support or parent-regularity truncation
is imposed. The already proved lower support and shape estimates give

    2a_s+1>=r/(L+2)=Y_0,
    pq>=1.98r/(s+2)^3.

These products exceed1000 on this finite domain. Indeed L+2<=3T,
so pq>=r/(3T)^3=Gamma^2/27, with Gamma=T/X. Here
log(Gamma/X)=X/5-(8/5)log X>=X/6, using the logarithm bound below.
It follows that Gamma>=2^100 X and T>=4000, more than enough for
pq>=1000. This does not require the older loglog r>=2^20 domain.

Equation (2.1) gives

    rho_s <= (1001/1000)(s+2)^(3/2)
                      /[2sqrt(pi*.99r)].                (3.1)

For candidates log v<=(7/10)T, use (1.2), bound its nonnegative S term
by S(v), and divide by log Y_0. This yields the claimed envelope

    boxed: Pr_*(2a_s+1 divides v | entire deeper profile)
       <= b_s:=251/1000+(1/4)((s+2)/T)^(3/2).            (3.2)

Here are complete finite guards for its two terms. For X>=65536,
the decreasing ratio log X/X gives

    D=log X<=X/4000.

At the left endpoint log65536=16log2<16<65536/4000. Therefore

    log Y_0>=X-log(3T)
       =(4/5)X-(2/5)D-log3 >=(799/1000)X.               (3.3)

Also T>=20/3 implies 2+.7T<=T, and

    log(2+log v)+20<=X/5+(2/5)D+20.

Its ratio to the right side of (3.3) is at most251/1000, because

    (2/5)D+20 <= (549/1000000)X.                         (3.4)

Indeed .4D+20<=X/10000+X/3000, since X>=60000, and
1/10000+1/3000=13/30000<549/1000000. Similarly
.4D+log3<X/10000+X/3000<X/1000, proving (3.3).
Notice that the older coarser guard X>=128D alone would not suffice
for (3.4); the sharper finite logarithm bound is explicitly used here.

For the second term, T^(5/2)=sqrt(r)X. Its coefficient times
((s+2)/T)^(3/2) is bounded by

    C=(1001/1000)(7/10)
          /[(799/1000)2sqrt(pi*.99)].                   (3.5)

Using pi>25/8, the exact rational square comparison is

    C^2 < 8926918/143640225 < 1/16,                     (3.6)

which was independently reproduced. The lower bound for pi was also
certified rationally using Machin's identity and two alternating-series
terms:

    pi >16(1/5-1/(3*5^3))-4/239
        =281476/89625 >25/8.

Thus C<1/4 and (3.2) follows. All tested b_s are below one as well:
T>=100 gives (s+2)/T<=2.01, and
sqrt(2.01)<10/7 yields b_s<.251+201/280<1.

## 4. The rigorous integral lower bound

Let

    f(t)=-log(251/1000+t^(3/2)/4),
    I=integral_0^2 f(t)dt.

The function is decreasing and positive on [0,2]. For positivity,
sqrt2<10/7 gives .251+sqrt2/2<.251+5/7<1.
For i=0,...,280 put t_i=(i/200)^2; then t_280=49/25<2 and

    q_i=251/1000+i^3/(4*200^3),
    t_i-t_(i-1)=(2i-1)/200^2.

Every q_i lies strictly between zero and one. The right-endpoint sum
and the positive logarithmic series give

    I >=sum_(i=1)^280 (2i-1)/200^2 *[-log q_i]
       >sum_(i=1)^280 (2i-1)/200^2
                    *sum_(j=1)^32 (1-q_i)^j/j
       =:S.                                             (4.1)

The unused interval [49/25,2] has nonnegative integrand, so discarding
it does not reverse the bound. The truncated logarithmic series is
a lower bound with positive omitted terms; there is no floating-point
quadrature premise.

The exact rational value was independently enclosed by

    1.41158740928968704395986676100717634170197891388258
       < S <
    1.41158740928968704395986676100717634170197891388259.

In particular S>141/100, and its margin above141/100 exceeds

    0.00158740928968704395986676100717634170197891388258.  (4.2)

Both decimal endpoints are exact rational numbers with denominator10^50.
The complete reduced numerator and denominator of S are retained in the
certificate below, so (4.2) is independently checkable by integer
cross multiplication. No conclusion here asserts that S equals I.

## 5. What was actually executed and retained

The exact verifier is

    scratch/verify_pbbs_depth_product_rational_certificate_20260908.py.

It was copied to and run only in

    h100:/home/amodo/exact-b-depth-product-audit-20260908/.

The program set hard limits of30 CPU seconds and512 MiB address space,
plus a45-second alarm; the shell also used a45-second timeout. It returned
PASS in about0.046 seconds. The server's recorded hostname was arboghast.

It checked the NB square comparison (2.5), the Machin lower bound,
the depth coefficient square (3.6), and S>141/100. It evaluated the
finite expression S twice: once by a common-denominator integer sum,
and once by independent Fraction operations. The results agreed exactly.

The saved report is

    scratch/depth_product_rational_certificate_20260908.json.

It contains all exact fractions, 50-place outward decimal enclosures,
the run limits, and the verifier SHA-256

    ae4eed725616654e0eacc72b73179e23b9b11ffadad8fa5dc5f8f19af1287cdf.

Only elapsed-time metadata uses floating point. All mathematical checks
use integers and exact fractions. No additional NB sample enumeration,
full-cube word verification, or construction search was run or claimed.

## 6. Scope for the subsequent depth product

The result available to the downstream proof is the uniform finite
bound (3.2) at every tested reverse depth and the exact lower integral
certificate (4.1)-(4.2). A product over the shifted sample points
(s+2)/T still needs its own finite shifted-Riemann comparison, followed
by the original-size conditioning debit, candidate-period union,
exceptional-profile bound, and word/parity charge. Those are separate
steps and are not replaced by merely inserting the limiting integral.

The sharp residue proof, finite Stirling/NB estimate, local numerical
coefficient and the requested rational certificate are all verified here.
The asymptotic or exact-equality conclusions require their explicitly
retained additional construction and probability inputs.
