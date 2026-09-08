# Profile prime sieve: residue bounds, elementary prime sums, and an explicit rate

2026-09-08. Independent pure-proof audit by exact_equality_structure.
No mathematical computation was run. The residue sieve, both proposed
scales, and the conservative numerical one-seventh bound pass.

Write

    F(t)=t^(1/7)(loglog t/log t)^(6/7).

The audited construction and inputs imply

    nu(k)/W(k)<=1+exp[-2^-50 F(k)]                         (1)

for every integer k>=ceil(exp(exp(2^21))). The smaller constants in
the proof leave explicit room in this final statement. This is an upper
bound from the existing height-adaptive finite word, not exact equality.

## 1. Exact inherited probability space and what is not conditioned

Let a_s be the original pruning profile of a uniform Dyck word of
semilength r. Its exact weight is

    product_j binom(a_j+a_(j+2),2a_(j+1)).

For 20<=L<=r choose depths

    I={ceil(L/2),ceil(L/2)+3,...} intersect [ceil(L/2),L-2].

Then |I|>=L/8. Expose every profile entry outside I. The full remaining
integer variables a_s, s in I, are independent. Their conditional law is
unimodal on an integer interval, and when the four exposed neighbors of
s lie within Delta=r/[10000(L+3)^3] of their harmonic centers, its maximal
atom is at most

    rho=1024 sqrt((L+1)^3/r).                             (1.1)

The proof, including the full support and its normalization, is
PBBS_EVERY_THIRD_PROFILE_CONDITIONAL_LAW_AND_MAXIMAL_ATOM_INDEPENDENT_AUDIT_20260908.md.
It was read in full for this audit. Its exact free-coordinate weight is

    binom(A+x,2b)binom(b+c,2x)binom(x+D,2c).

The law here is the FULL conditional law. We do not condition a free
coordinate on its own regularity, on primitivity of any gap row, or on
dividing a proposed period. Those events will only be used as subsets
of a divisibility event tested under this full product law.

On regular profiles with the first L original gap rows primitive, the
already proved synchronous period divisibility implies

    2a_s+1 divides v,  every s in I.                       (1.2)

The original-law integration and the subsequent word charge are separately
audited in PBBS_PROFILE_SIEVE_ORIGINAL_LAW_AND_CHARGE_BOOKKEEPING_AUDIT_20260908.md.
Sections 6-7 below provide the full numerical interfaces used there.

## 2. Residues of a unimodal integer law

Let p_j be any unimodal probability mass function on the integers, extended
by zero outside its support, and suppose max p_j<=rho. Its total variation
along the integers is at most 2rho. For a modulus m and a residue b, divide
the integers into disjoint consecutive blocks of m positions, each containing
one representative of b. In each block the difference between that entry
and the block average is bounded in absolute value by the block's maximum
minus minimum. Summing these ranges is at most the full variation. Therefore

    |Pr(X=b mod m)-1/m|<=2rho.                            (2.1)

The argument is valid for finite, one-sided, and two-sided supports by
limits. An interval support containing zeros at its endpoints causes no
normalization loss.

For an odd prime p, the condition 2X+1=0 mod p is one residue class of X.
For two distinct odd primes p,q, their simultaneous condition is one
class modulo pq by the Chinese remainder theorem. Thus both the first
and second moments below use (2.1) with precisely the same error 2rho.

## 3. Missing-prime first and second moments

Fix an integer candidate v. Let P_v be a finite set of odd primes absent
from v, write J=|P_v| and lambda=sum_(p in P_v)1/p, and let

    Z=sum_(p in P_v) 1_{p divides 2X+1}.

Then (2.1) gives

    E Z>=lambda-2Jrho,
    E Z^2<=lambda+lambda^2+2J^2rho.                       (3.1)

For the second inequality the diagonal error is 2Jrho and the pair error
is 4 binom(J,2)rho, totaling exactly 2J^2rho. The main pair sum is
lambda^2-sum_p p^(-2), so dropping its negative last term is legitimate.

By Cauchy-Schwarz applied to Z 1_{Z>0},

    Pr(Z>0)>= [lambda-2Jrho]_+^2
                   /(lambda+lambda^2+2J^2rho).           (3.2)

If Z>0 then 2X+1 cannot divide v. Thus (3.2) is a rejection probability
for each free depth. It is uniform once the displayed lambda and rho
bounds are uniform over candidates and exposed profiles.

## 4. An elementary reciprocal-prime estimate with actual constants

The elementary central-binomial argument proves theta(y)<=4y for y>=2,
and splitting primes at sqrt(y) gives pi(y)<=16y/log y. A complete proof
with these constants is also in
PBBS_BOUNDED_SMALL_DIVISORS_AND_LONG_PERIOD_RATE_ARITHMETIC_AUDIT_20260908.md,
Section 2. No prime number theorem is required here.

For integer N>=2 put

    A_N=sum_(p^j<=N) (log p)/p^j,
    psi(N)=sum_(p^j<=N) log p.

The factorial identity gives

    log(N!)=N A_N-E_N,   0<=E_N<=psi(N).

Also psi(N)<=8N. For N>=16 this follows from
theta(N)<=4N and
sum_(j>=2,j<=log_2 N) theta(N^(1/j))<=4sqrt(N)log_2 N<=4N.
For 2<=N<16, the crude psi(N)<=log(N!)<=Nlog N<3N suffices.

Integral bounds on log(N!) give

    log N-1<=log(N!)/N<=log N.

The higher-power contribution satisfies

    0<=A_N-sum_(p<=N)(log p)/p
      <=sum_(m>=2) (log m)/[m(m-1)]<3.

For example bound it by twice sum_(m>=2)(log m)/m^2, then use the
decreasing-function integral from 2 to infinity. Consequently, for real
y>=2, allowing for N=floor(y), the deliberately loose bound

    |sum_(p<=y)(log p)/p-log y|<=16                       (4.1)

is valid. Partial summation on [Y,Z] now proves

    |sum_(Y<p<=Z)1/p-log(log Z/log Y)|<=32/log Y,
    2<=Y<Z.                                             (4.2)

Indeed the two boundary errors are at most 16/log Y+16/log Z, and
the integrated error is at most 16(1/log Y-1/log Z). This supplies
the required Mertens estimate and its error directly from Chebyshev
and the factorial identity.

## 5. The optimized scales and their symbolic exponents

Put

    X=log r, D=log X,
    T=(rX/D)^(1/7), L=floor(T),
    F=r^(1/7)(D/X)^(6/7)=r/T^6=T D/X.

Choose the prime band

    Y=r^(1/7)X^(-4/5),
    Z=r^(1/7)X^(-7/10).

Its reciprocal mass from (4.2) is

    sum_(Y<p<=Z)1/p=(7/10+o(1))D/X.                    (5.1)

In fact log Z-log Y=D/10, and log Y=X/7-4D/5, which proves the
coefficient 7/10. The error O(1/log Y)=O(1/X) is smaller by a factor D.

If log v<=aF, the band primes dividing v have reciprocal mass at most

    (log v)/(Y log Y)
       =O(a D^(6/7) X^(-37/35))=o(D/X).                 (5.2)

This uses only that each such prime is larger than Y. The exponent is
minus 6/7 plus 4/5 minus 1, namely -37/35. The bound is uniform in v.

Since L+1<=2T eventually, (1.1) gives

    rho<=2^12 r^(-2/7)(X/D)^(3/14).

The crude bound J<=Z is enough to give

    J^2rho<=2^12 X^(-83/70)D^(-3/14)=o(D/X).             (5.3)

Here 3/14-7/5=-83/70. After division by D/X the remaining powers are
X^(-13/70)D^(-17/14), which tend to zero. Equations (3.2) and
(5.1)-(5.3) prove the proposed uniform rejection bound D/(100X)
for all sufficiently large r. No extra logarithmic factor is missing.

## 6. A fully numerical rejection domain

All the preceding estimates can be made simultaneous on the simple domain

    D=loglog r>=2^20,
    log v<=F/6400.                                      (6.1)

First X=exp(D)>=D^2/2>=128D, and T>=3. Hence log Y>=X/8,
L+1<=2T, and the prime band lies above two. Put S=D/X. The elementary
inequalities for log(b/a), with a=log Y and b=log Z, give

    (7/10)S<=log(log Z/log Y)<=(4/5)S.

Together with (4.2), whose error is at most 256/X, and D>=1280,
this yields

    S/2<=sum_(Y<p<=Z)1/p<=S.                             (6.2)

The removed reciprocal mass for a candidate in (6.1) is at most

    (F/6400)/(Y log Y)
      <=(1/800)D^(6/7)X^(-37/35)
      <=S/800.                                         (6.3)

The last ratio to S is D^(-1/7)X^(-2/35)<=1. Thus the absent-prime
mass satisfies

    S/3<=lambda<=S<=1/4.                                (6.4)

Furthermore (5.3) is a literal finite inequality here, and

    2J^2rho/S<=2^13 X^(-13/70)D^(-17/14)
                 <=2^13 D^(-17/14)<1/12.                (6.5)

Indeed D>=2^20 implies D^(17/14)>=2^(170/7)>2^24.
Since lambda>0, J>=1 and also 2Jrho<=2J^2rho. Thus each error in
(3.1) is at most lambda/4. Substituting into (3.2), its numerator is
at least (3lambda/4)^2 and its denominator is at most 3lambda/2.
The rejection probability is therefore at least

    (3/8)lambda>=D/(8X)>=D/(100X).                       (6.6)

This establishes the requested weaker numerical constant 100 on (6.1),
uniformly over all candidates and every admissible regular exposed
configuration. In particular it is not merely an asymptotic claim about
a typical candidate or a typical free-coordinate value.

## 7. Product, union, exceptional profiles, and the explicit word bound

For clarity retain only the weaker D/(100X) from (6.6). Conditional
independence of the full laws at the selected depths gives, for each
fixed candidate v in (6.1),

    Pr(all selected 2a_s+1 divide v | exposed)
      <=exp[-LD/(800X)]<=exp(-F/1600),                   (7.1)

because L=floor T>=T/2. This is then integrated over regular exposed
configurations; no conditioning on the free values is introduced.
There are at most exp(F/6400) positive integer candidates, so the union
is at most

    exp(-3F/6400).                                      (7.2)

A good actual period belongs to that union if it is at most exp(F/6400),
by the deterministic primitive-row divisibility. It is unnecessary to
condition the law in (7.1) on the good event in order to use this inclusion.

Here are explicit bounds for its complement. The inherited finite
one-depth concentration is

    Pr(|a_s-r/(s+1)|>(4+x)sqrt r)<=2exp(-x^2/6).

Use Delta=r/[10000(L+3)^3]. From X>=128D one gets

    log F=(X-6D+6log D)/7>=X/8>=D+50,
    F>=2^50 X.                                         (7.3)

The harmless improvement from 50 to 50log2 uses log2<1. These inequalities
also ensure 20<=L<=r, T>=3, and L+3<=2T. Consequently

    Delta/sqrt r>=sqrt F/80000>=8.

Set x=Delta/sqrt r-4>=sqrt F/160000. The concentration union through
L+1 is at most

    2(L+2)exp[-F/153600000000]
      <=2(L+2)exp(-2^-38 F)
      <=exp(-2^-39 F),                                  (7.4)

using 153600000000<2^38, log(2(L+2))<=2X, and (7.3).

On every regular full profile, let B=r/(L+3)^3. The exact second
differences give ell_s>=B for all first L rows, and their lengths also
satisfy p_s>=B. The conditional composition repetition estimate gives

    Pr(any first-L row nonprimitive | profile)
      <=2Ln exp(-B/3),   n=2r+1.

Since B>=r/(8T^3)=FT^3/8>=F, this is at most exp(-F/4), by
log(2Ln)<=3X and (7.3). Thus irregularity or nonprimitivity has probability
at most exp(-2^-40F). Combining with (7.2), the probability of an actual
period at most exp(F/6400) is at most exp(-2^-41F).

The exact height-adaptive collar charge is E[(2h-1)/v]. On the short-period
exception it is at most its probability, since v>=n and 2h-1<n. Elsewhere
it is at most n exp(-F/6400)<=exp(-F/12800), again by (7.3). Adding
and absorbing the factor two gives

    nu(2r+1)/W(2r+1)<=1+exp(-2^-42F(r)),
    loglog r>=2^20.                                     (7.5)

The bookkeeping bounds (7.1)-(7.5) have also passed an independent
finite-frontier review in
PBBS_PROFILE_SIEVE_ORIGINAL_LAW_AND_CHARGE_BOOKKEEPING_AUDIT_20260908.md.

For k>=ceil(exp(exp(2^21))), use n=k or k-1 according to parity, with
r=(n-1)/2. Then r>=k/4>=sqrt k, so loglog r>=loglog k-log2>2^20.
Also

    F(r)>=2^(-8/7)F(k)>=F(k)/4.

This follows from r>=k/4, log r<=log k and
loglog r>=0.5loglog k. The exact one-coordinate lift doubles both
length and width, introducing no multiplicative error. Equation (7.5)
therefore even proves coefficient 2^-44 in (1); the advertised smaller
2^-50 is safely valid at the same threshold.

## 8. Independent check of the simpler r^(1/8) scale

The simpler choice L=floor(r^(1/8)) also works. Then

    rho<=C r^(-5/16).

Take the fixed-power prime band

    r^(17/128)<p<=r^(9/64).

Equation (4.2) gives reciprocal mass tending to log(18/17)>0.
For log v<=aL, the primes dividing v remove at most

    (log v)/[r^(17/128)log(r^(17/128))]
       =O(a r^(-1/128)/log r)=o(1).

Also J<=r^(9/64), so

    J^2rho<=C r^(9/32-5/16)=C r^(-1/32)=o(1).

The first/second-moment rejection (3.2) consequently tends uniformly
to a positive number. For example, for all sufficiently large r it is
at least 1/100: one may take lambda>=1/24 and lambda<=1/8, with both
errors at most lambda/4, which makes the ratio at least 9/(22*24)>1/100.
Here log(18/17)>1/18 and log(18/17)<1/17 justify those eventual bounds.

The |I|>=L/8 product gives exp(-L/800). Taking any fixed a<=1/6400,
the union over v<=exp(aL) is exponentially small in L. Profile irregularity
has bound exp[-c r/L^6]=exp[-Omega(r^(1/4))], and nonprimitive rows are
even smaller, from their mass Omega(r/L^3). They are negligible on the
L scale. The good collar numerator n is absorbed because log n=o(L).
Thus this simpler sieve rigorously gives

    nu(k)/W(k)<=1+exp[-c k^(1/8)]

for some absolute c>0 and all sufficiently large k, including both
parities. This last display is existential in c and its starting dimension;
the fully specified result is (1)-(2), not an unproved numerical threshold
for the simpler scale.

## 9. Scope

The exact conditional factorization and maximal-atom proof are explicitly
inherited and were read; the residue estimate and missing-prime moments
are proved here for that full law. The elementary prime-sum estimate has
an absolute finite error adequate for the narrowing optimized band.
Every rejection estimate used in the product and candidate union is
uniform over the exposed configurations and candidate periods. No
conditional independence is assumed after imposing primitivity or free
regularity. These points are essential for the stated rate.
