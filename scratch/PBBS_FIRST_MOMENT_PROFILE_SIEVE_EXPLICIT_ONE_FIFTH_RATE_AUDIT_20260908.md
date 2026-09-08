# First-moment profile sieve: a fully explicit one-fifth rate

2026-09-08. Independent arithmetic and conditioning audit by
exact_equality_structure. No mathematical computation was run.

The first-moment improvement and the proposed numerical choices pass.
With natural logarithms, put

    Gamma(t)=t^(1/5)(log t)^(-3/5).

The previously proved height-adaptive finite construction satisfies

    nu(k)/W(k)<=1+exp[-2^-330 Gamma(k)]                    (1)

for every integer

    k>=ceil(exp(exp(2^21))).                             (2)

All probability and arithmetic hypotheses used below have finite domains;
no unspecified sufficiently-large qualification is needed for (1)-(2).
This remains an upper bound, not a proof that nu(k)=B(k).

## 1. Audited full-law and fixed-size inputs

Write

    X=log r, d=log X>=2^20,
    Gamma=r^(1/5)X^(-3/5),
    T=Gamma X,
    L=floor(T).

The two independently proved inputs are recorded in

* PBBS_REVERSE_PROFILE_NB_TAILS_AND_EXISTENCE_ONLY_SMOOTHING_INDEPENDENT_AUDIT_20260908.md;
* PBBS_REVERSE_PROFILE_FIXED_SIZE_TRANSFER_EXPLICIT_DOMAIN_AUDIT_20260908.md.

Both complete files were read for this audit. Their relevant finite
conclusions are as follows. For a uniform Dyck root of semilength r,
let A require one-percent relative accuracy of its original profile a_j
through depth L+1. Let B require every first-L second difference
ell_s=a_s-2a_(s+1)+a_(s+2) to lie between half and twice

    mu_s=(2a_(s+1)+1)/[(s+1)(s+3)].

Let mathcal G be A intersect B together with primitivity of all first-L
original gap rows. Then

    Pr_r(mathcal G^c)<=exp(-2^-26 Gamma^2).               (1.1)

Choose free depths

    I={ceil(L/2),ceil(L/2)+3,...} intersect [ceil(L/2),L-2].

There are at least L/8 of them. Expose every original profile coordinate
outside I. On any exposed configuration admitting even ONE completion
in A intersect B, the free variables have independent FULL conditional
laws, each unimodal, with maximal atom at most

    rho<=2^20/Gamma<=2^22/Gamma.                          (1.2)

Their support is the entire feasible profile interval, including values
that fail A or B. Every such full feasible profile obeys 0<=a_s<=r.
The second constant in (1.2) is the deliberately loose interface used
in the numerical sieve below.

The fixed-size transfer in (1.1) is essential. The reverse negative-binomial
law is first used under the auxiliary all-size law after dropping the
fixed-size and irrelevant profile restrictions; division by the exact
fixed-size probability then costs at most 12r^2, explicitly absorbed
in (1.1). The reverse law is not assumed to persist after conditioning
on a_0=r.

On mathcal G, the inherited invariant-row period theorem implies that
every 2a_s+1, s in I, divides the actual physical g-period v. This is
only a necessary event used below; we do not condition the free laws
on primitivity or on mathcal G before multiplying their probabilities.

## 2. Uniform residue bound and the new first-moment observation

For any unimodal probability mass on the integers with maximal atom rho,

    |Pr(U=b mod m)-1/m|<=2rho.                           (2.1)

One proof extends the mass by zero, divides it into blocks of m entries,
and bounds the discrepancy in each block by its maximum minus minimum.
The sum is at most the full variation of the unimodal sequence, 2rho.
This proof applies to the FULL conditional laws in (1.2).

Fix a proposed period v and a band Y<p<=Z of odd primes absent from v.
Let P_v be these primes, J their number, and lambda their reciprocal sum.
For one full conditional variable U=a_s put

    Q=sum_(p in P_v) 1_{p divides 2U+1}.

Each odd prime specifies exactly one residue class of U, so

    E Q>=lambda-2Jrho.                                  (2.2)

Suppose Y^7>2r+1. Since the ENTIRE conditional support obeys 2U+1<=2r+1,
no value in that support is divisible by seven distinct primes larger
than Y. Consequently 0<=Q<=6 pointwise, and

    Pr(2U+1 does not divide v)
      >=Pr(Q>0)>= [lambda-2Jrho]_+/6.                   (2.3)

This avoids any second-moment or pair-residue error. The bound Q<=6
uses the full physical size restriction; it is not valid merely from
an unbounded comparison distribution for U. The actual finite support
is what makes the improvement legitimate.

## 3. Elementary prime estimates used with actual constants

The finite estimates needed here are

    pi(y)<=16y/log y,          y>=2,

    |sum_(Y<p<=Z)1/p-log(log Z/log Y)|<=32/log Y,
    2<=Y<Z.                                              (3.1)

They are proved from Chebyshev and the factorial identity in Section 4 of
PBBS_PROFILE_PRIME_SIEVE_AND_EXPLICIT_ONE_SEVENTH_RATE_INDEPENDENT_AUDIT_20260908.md.
For clarity, no prime number theorem is an input: theta(y)<=4y follows
from central binomial coefficients; the factorial identity and
psi(N)<=8N give
|sum_(p<=y)(log p)/p-log y|<=16. Partial summation then gives exactly
the second error constant in (3.1).

The choices for this proof are

    B_0=2^256,     delta=2^-40,     a=2^-320,
    H=log Gamma,
    Y=delta Gamma/B_0,       Z=delta Gamma.              (3.2)

The band ratio B_0 is a fixed absolute constant. Although large, it
does not change the limiting one-fifth power of Y or Z.

## 4. All finite scale guards on d>=2^20

Since X=exp(d)>=d^2/2>=128d,

    X/6<=H=(X-3d)/5<=X/5.                              (4.1)

In particular H>=592log2 and log Y=H-296log2>=H/2>0.
Also log Z=H-40log2>=H/2, and Y>2. These inequalities follow with
room from H>=X/6>=128d/6 on the stated domain.

For later numerator and probability absorptions we may use the stronger
elementary guard

    Gamma>=2^400 X.                                     (4.2)

Indeed log Gamma>=X/6>=128d/6>=d+400, and log2<1. This implies
T>=40, 20<=L<=r, T/2<=L<=T, and Gamma is larger than every fixed
power of two that appears below. The inequality T<=r follows directly
from log T=X/5+2d/5<=X, since X>=d/2.

Finally, the product guard for (2.3) is finite, not just asymptotic:

    7log Y-log(2r+1)
      >=7H-2072log2-X-log3
      >=X/6-2072log2-log3>0.                            (4.3)

Thus Y^7>2r+1 everywhere in the stated domain. In particular all selected
primes are odd, and Q<=6 applies to every full conditional value.

## 5. Numeric reciprocal mass, deletion by v, and residue errors

From (3.1), (3.2), and (4.1),

    sum_(Y<p<=Z)1/p
      >=log(log Z/log Y)-32/log Y
      >=(256log2)/H-64/H
      >=1/H.                                           (5.1)

The middle inequality uses log(b/a)>=(b-a)/b, with b=log Z<=H.
The last follows already from log2>=2/3: 256log2-64>=320/3>1.
Thus the large fixed B_0 explicitly absorbs the Mertens error.

Consider any integer v satisfying log v<=a Gamma. The band primes
dividing v have reciprocal mass at most

    (log v)/(Y log Y)
      <=2aB_0/(delta H)=2^-23/H.                        (5.2)

This is uniform over every candidate; it uses only that the logarithms
of distinct prime divisors of v sum to at most log v. Notice that
a=2^-320<=delta/(8B_0)=2^-299, as required by the looser abstract argument.

The number of absent band primes is at most the total number up to Z.
Equations (3.1), (4.1), and (1.2) give

    J<=16Z/log Z<=32delta Gamma/H,
    2Jrho<=64delta 2^22/H=2^-12/H.                       (5.3)

Combining (5.1)-(5.3),

    lambda-2Jrho >=(1-2^-23-2^-12)/H>=1/(2H).            (5.4)

By (2.3), each selected depth therefore rejects the candidate with
probability at least

    1/(12H)>=1/(12X).                                   (5.5)

All these estimates are uniform over the exposed configurations
admitting a good completion. Neither the local-law normalization nor
the physical support has been changed.

## 6. Conditional product and the union over all short candidates

Fix one exposed configuration admitting an A intersect B completion.
Under its independent full conditional laws, (5.5) and |I|>=L/8 give

    Pr(all selected 2a_s+1 divide a fixed v | exposed)
      <=exp[-L/(96X)]<=exp(-Gamma/192),                  (6.1)

because L>=Gamma X/2. This remains an upper bound after intersecting
with mathcal G, so we integrate it over such exposed configurations
without conditioning the free variables further.

On mathcal G, if the actual period is at most exp(a Gamma), it is
one of at most exp(a Gamma) positive integer candidates in (6.1).
Since a=2^-320<=1/768, the union bound gives

    Pr_r(mathcal G AND v<=exp(a Gamma))
       <=exp[-(1/192-a)Gamma]<=exp(-Gamma/256).          (6.2)

Primitivity is used solely to imply these divisibilities on mathcal G.
There is no claim that the profile coordinates stay independent after
conditioning on primitive rows, or after conditioning on a candidate.

Adding the already proved fixed-size exception (1.1), and using (4.2),
gives

    Pr_r(v<=exp(a Gamma))
      <=exp(-Gamma/256)+exp(-2^-26Gamma^2)
      <=exp(-Gamma/512).                                (6.3)

For the last step it suffices that Gamma>=2^18 and Gamma/512>=log2;
both follow from (4.2).

## 7. Actual word charge, integer length, and both parities

For the existing height-adaptive construction at n=2r+1, its normalized
collar charge is exactly E[(2h-1)/v] under uniform physical middle states.
These have exactly the same profile probability space as uniform Dyck
roots for all events above; each root has n labelled rotations.

Everywhere v>=n and 2h-1<n, so the short-period contribution is at most
(6.3). On its complement the contribution is at most

    n exp(-a Gamma)
      <=exp(-2^-321 Gamma),                             (7.1)

because log n<=2X and (4.2) gives 2X<=a Gamma/2. Thus

    E[(2h-1)/v]
      <=exp(-Gamma/512)+exp(-2^-321Gamma)
      <=exp(-2^-322Gamma).                              (7.2)

The factor two is absorbed since 2^-322Gamma>=log2, again by (4.2).
In particular one may give the explicit finite integer bound

    nu(2r+1)<=W(2r+1)
                 +floor[W(2r+1)exp(-2^-322Gamma(r))],
    loglog r>=2^20.                                     (7.3)

The floor is applied to the whole normalized collar estimate, which
is valid because the actual collar sum is an integer.

For k in (2), choose n=k when odd and n=k-1 when even, and set
r=(n-1)/2. Then r>=k/4>=sqrt k, so

    loglog r>=loglog k-log2>2^20,
    Gamma(r)>=2^(-2/5)Gamma(k)>=Gamma(k)/2.               (7.4)

The second inequality uses r>=k/4 and log r<=log k. The exact
one-coordinate lift doubles the length and the central width, hence
preserves the normalized bound. Consequently (7.2) already proves
coefficient 2^-323 at threshold (2). The smaller advertised coefficient
2^-330 in (1) is therefore valid with room to spare.

## 8. Relation to the existential argument and precise scope

For any fixed finite smoothing constant C_rho in rho<=C_rho/Gamma,
the same argument works by first choosing a sufficiently large fixed
band ratio B_0, then choosing delta>0 small enough, and finally a>0
below both delta/(8B_0) and 1/768. The explicit choices (3.2) implement
that order for the certified C_rho<=2^22.

The key improvement is the pointwise bound of six prime factors on
the actual conditional support, which converts the first moment into
a rejection probability. It replaces the pair-counting error from
the earlier second-moment sieve. The full support bound, the existence-only
smoothing hypothesis, and the fixed-size transfer are all necessary
parts of that justification. None is replaced by a typical-value
heuristic or an independent negative-binomial model at fixed size.

The proof certifies the numerical one-fifth relative upper bound for the
already proved all-rank word. It supplies no finite construction of
length B(k) and does not assert that its remaining error is zero.
