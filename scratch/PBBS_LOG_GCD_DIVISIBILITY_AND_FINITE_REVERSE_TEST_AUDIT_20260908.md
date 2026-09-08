# Logarithmic-gcd divisibility: exact residue lemma and finite reverse test

2026-09-08. Independent pure-proof audit by exact_equality_structure.
No mathematical computation was run. The general divisibility estimate,
constant C_0=20, and uniform one-half reverse-test bound all pass.

## 1. A divisibility bound allowing infinite support

Let U be an integer-valued random variable with a unimodal mass function
and maximal atom at most rho. Assume

    Y=2U+1>=Y_0>1

on its entire support, which may be infinite. For every positive integer v,
define

    S(v)=sum_(p^j divides v, j>=1) (log p)/p^j.

Then

    Pr(Y divides v)
       <=[S(v)+2rho log v]/log Y_0
       <=[log(2+log v)+20+2rho log v]/log Y_0.            (1.1)

There is no upper bound assumption on Y. The estimate is trivial but
valid when its right side exceeds one. When v=1 the event is empty;
the first displayed bound is exactly zero.

For completeness, every residue class modulo m of a unimodal integer
law differs from 1/m in probability by at most 2rho. Extend the mass by
zero outside its support and divide the integers into consecutive blocks
of m. The discrepancy between the chosen residue's mass in a block and
that block's average is bounded by its maximum minus minimum. Summing
is bounded by the total variation of the unimodal sequence, at most
2rho. Limits cover infinite supports.

For every odd prime power p^j, the condition p^j divides 2U+1 is one
residue class of U. Thus its probability is at most p^(-j)+2rho.
For powers of two the probability is zero, which satisfies the same
upper bound. On each outcome,

    log gcd(Y,v)
       =sum_(p^j divides v) (log p)1_{p^j divides Y}.

The sum is finite. Taking expectations and using
sum_(p^j divides v)log p=log v gives

    E log gcd(Y,v)<=S(v)+2rho log v.                     (1.2)

On the event Y divides v, the logarithm in (1.2) equals log Y>=log Y_0;
elsewhere it is nonnegative. This proves the first inequality in (1.1),
without a tail approximation, second moment, or finite-support truncation.

## 2. Explicit logarithmic bound for S(v)

The elementary estimate

    |sum_(p<=y)(log p)/p-log y|<=16,      y>=2,           (2.1)

and the absolutely convergent bound

    sum_p sum_(j>=2) (log p)/p^j<3                       (2.2)

were proved with finite constants in Section 4 of
PBBS_PROFILE_PRIME_SIEVE_AND_EXPLICIT_ONE_SEVENTH_RATE_INDEPENDENT_AUDIT_20260908.md.
They do not require the prime number theorem.

Here is their elementary source chain. Central binomial coefficients give
theta(y)<=4y; summing powers yields psi(N)<=8N. Prime factorization of N!
therefore gives

    log N-1<=sum_(p^j<=N)(log p)/p^j<=log N+8.

Subtracting the higher powers and replacing integer N by floor(y) gives
(2.1), with ample room in 16. To check (2.2) directly, bound its sum by
sum_(m>=2)(log m)/[m(m-1)], then by twice
sum_(m>=2)(log m)/m^2. The decreasing-function integral from 2 to infinity
bounds this by less than three.

Put M=2+log v>=2. The contribution to S(v) from primes p<=M is at most

    sum_(p<=M)(log p)/p + sum_p sum_(j>=2)(log p)/p^j
       <=log M+19.

For every p>M and j>=1, p^j>M. Counting only the powers that divide v,
their contribution is at most

    (1/M)sum_(p^j divides v, p>M)log p
       <=(log v)/M<1.

Consequently

    S(v)<=log(2+log v)+20,                              (2.3)

which proves the second inequality in (1.1). Repeated prime powers
are fully counted through log v. No squarefreeness assumption is used.

## 3. The exact auxiliary reverse kernel and its maximal atom

Under the auxiliary law P*(D)=4^(-|D|)/2 on all finite Dyck words,
condition on the ENTIRE deeper profile at level s. For
b=a_(s+1), c=a_(s+2), the original parent size is

    a_s=2b-c+Z,
    Z~NB(N=2b+1,q=(s+2)^(-2)).                          (3.1)

Its mass is binom(N+t-1,N-1)(1-q)^N q^t on every t>=0.
The exact kernel, including its normalization and empty-child case,
is proved in
PBBS_REVERSE_PROFILE_NB_TAILS_AND_EXISTENCE_ONLY_SMOOTHING_INDEPENDENT_AUDIT_20260908.md,
Section 1. This law is not claimed after conditioning on a_0=r.

The negative-binomial mass is unimodal: its consecutive ratio is
q(N+t)/(t+1), which is decreasing for N>1 and constant below one for
N=1. Its maximal atom is bounded by

    max_t Pr(Z=t)<=1/sqrt(Nq),       0<q<=1/4.            (3.2)

The proof in Section 3 of
PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md
was read for this audit. Its Fourier modulus is
[1+4q(1-q)^(-2)sin^2(theta/2)]^(-N/2); the Gaussian-integral bound is
sqrt(pi)(1+q)/(2sqrt(2Nq))<=1/sqrt(Nq). It covers N=1 as well,
and it is harmless if the bound exceeds one. Integer translation in
(3.1) preserves unimodality and the maximal atom.

## 4. Uniform local bounds from only the two child sizes

Fix a target size r and a cutoff L. At a depth 0<=s<L suppose only that
the two deeper values b,c satisfy the one-percent harmonic bounds

    .99r/(s+2)<=b<=1.01r/(s+2),
    .99r/(s+3)<=c<=1.01r/(s+3).                          (4.1)

No restriction is imposed on the free parent a_s. On the ENTIRE infinite
support of (3.1),

    2a_s+1>=4b-2c+1
       >=1.94r/(s+2)>=r/(L+2)=:Y_0.                    (4.2)

Here c<=1.01r/(s+2) was used only as a weakening. Also

    Nq=(2b+1)/(s+2)^2
       >=1.98r/(s+2)^3>=r/(L+2)^3.

Equation (3.2) therefore gives the common maximal-atom bound

    rho<=sqrt((L+2)^3/r).                               (4.3)

The general gcd lemma applies despite the unbounded parent support.
This is exactly why the present proof does not need the earlier
finite-support bound on the number of selected prime factors.

## 5. The explicit scale and one-half pass probability

Write

    X=log r,     D=log X>=2^20,
    J=(r X^2)^(1/5),     L=floor J.

Then X=exp(D)>=D^2/2>=128D. In particular J>=100 and L+2<=2J, so

    log Y_0=log(r/(L+2))
       >=(4/5)X-(2/5)D-log2>0.                          (5.1)

For any positive integer candidate v with log v<=L/16, equations
(1.1) and (4.3) give the explicit bound

    Pr_*(2a_s+1 divides v | entire deeper profile)
      <=[log(2+L/16)+20
              +(L/8)sqrt((L+2)^3/r)]/log(r/(L+2)).      (5.2)

The numerical simplification is uniform. First 2+L/16<=J because
J>=100, whence

    log(2+L/16)<=log J=X/5+(2/5)D.

Next J^5=rX^2 gives

    L sqrt((L+2)^3/r)
      <=X(1+2/J)^(3/2)<=(11/10)X.                       (5.3)

For the last inequality J>=100 implies
(1+2/J)^(3/2)<=(51/50)^2=2601/2500<11/10.
Thus the numerator in (5.2) is at most

    (27/80)X+(2/5)D+20,                                 (5.4)

and its denominator has the positive lower bound (5.1). Their ratio
is at most one half because

    X/16 >= (3/5)D+20+(log2)/2.                         (5.5)

Indeed X>=128D makes the left side at least 8D, and (5.5) follows
throughout D>=2^20. We have proved the finite uniform rejection input

    boxed: Pr_*(2a_s+1 divides v | entire deeper profile)
                <=1/2                                 (5.6)

at EVERY depth 0<=s<L whose two child values meet (4.1). It requires
neither a finite upper support nor conditioning the parent to be regular.

## 6. Exact conditioning scope and downstream boundary

Equation (5.6) is an auxiliary-law reverse conditional estimate. To use
it at fixed r, a reverse product may impose the remaining child-size
ranges, drop restrictions on each parent before applying its kernel,
and then pay the original-size normalizer only once at the end. It must
not assert that the reverse kernel itself holds under a_0=r.

Similarly, primitive rows are used to imply that actual small periods
must pass the divisibility tests, not to recondition (3.1). A union over
candidate integers is legitimate because (5.6) is uniform in each fixed
v up to exp(L/16). The no-prefactor bad-profile and nonprimitive-row
bound from the earlier reverse-profile proof remains a separate finite
input on this same L scale.

This note certifies the complete logarithmic-gcd lemma, the prime-power
constant20, the exact negative-binomial local interface, and every
numerical guard for (5.6). The reverse product, fixed-size probability
transfer and final collar/parity estimate are independently recorded by
root and the finite-frontier audit, rather than silently incorporated
as new independence assumptions here.
