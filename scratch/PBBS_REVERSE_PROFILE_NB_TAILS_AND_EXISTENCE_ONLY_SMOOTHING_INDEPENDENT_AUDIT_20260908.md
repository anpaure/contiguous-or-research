# Reverse profile kernels, exponential tails, and existence-only smoothing

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No mathematical program was run. Verdict: the exact reverse kernel,
the stated Chernoff estimate, and the full conditional smoothing
interface pass. An explicit smoothing constant `C_rho=2^20` is valid.
The transfer back to fixed size and the resulting sieve rate are separate
root and arithmetic audits.

## 1. Exact auxiliary tail-profile law

Use the probability measure `P*(D)=4^(-|D|)/2` on all finite Dyck words,
including the empty word. Its depth-s word law is proved in
`scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`:

    P_s(E)=K_s X_s^|E| Y_s^pk(E),
    K_s=(s+1)/(s+2),
    X_s=(s+1)^2/(s+2)^2,
    Y_s=1/(s+1)^2.

Since a depth-s word with subsequent profile a has `pk(E)=a_s-a_(s+1)`,
its exact TAIL PROFILE probability is

    K_s x_s^(a_s) y_s^(a_(s+1))
      product_(j>=s) binom(a_j+a_(j+2),2a_(j+1)),           (1)

where

    x_s=1/(s+2)^2,    y_s=(s+1)^2.

The product is finite after padding by terminal zeros; all later factors
are one. The profile count is the exact original inverse-pruning fibre
count, not a product of independently distributed profile sizes.

Condition on the ENTIRE deeper profile, and write
`b=a_(s+1), d=a_(s+2)`. Its feasible parent values are precisely

    a_s=2b-d+t,    t>=0.

Indeed this is the remaining convexity constraint, and b>=d>=0 makes
it imply a_s>=b>=0. In (1) the dependence on t is exactly

    binom(2b+t,2b) x_s^t.

Normalizing gives the exact reverse conditional kernel

    ell_s=a_s-2b+d ~ NB(N=2b+1,q=x_s),
    Pr(ell_s=t | deeper profile)
       =binom(N+t-1,N-1)(1-q)^N q^t,                      (2)

with mean

    mu_s=Nq/(1-q)=(2b+1)/[(s+1)(s+3)].                   (3)

The empty deeper core, b=d=0, is included: N=1 and the kernel is
geometric. This law holds under P*, before imposing a fixed value of
a_0 or a regularity event. Dropping such restrictions before applying
the kernel is therefore essential in a fixed-size transfer.

## 2. A uniform two-sided Chernoff estimate

Let Z have (2), with `0<q<=1/4` and mean mu. Take
`theta=log(4/3)`. Its exact transform gives

    log E exp(theta Z)
      =N log[(1-q)/(1-4q/3)]
      <=N q/[3(1-4q/3)]
      =mu(1-q)/(3-4q)
      <=3mu/8<=mu/2.                                    (4)

The middle inequality is `log(1+x)<=x`; the rational factor increases
to 3/8 at q=1/4. Convexity of 1/x on [1,4/3] gives
`log(4/3)>=2/7`. Chernoff therefore yields

    Pr(Z>2mu)<=exp[-(2log(4/3)-1/2)mu]
                <=exp(-mu/14)<=exp(-mu/32).               (5)

For the lower tail,

    log E 2^(-Z)
      =-N log[1+q/(2(1-q))]
      <=-Nq/(2-q)
      =-mu(1-q)/(2-q)
      <=-3mu/7.                                         (6)

Here `log(1+x)>=x/(1+x)`, and the last rational factor decreases
to 3/7. The trapezoid bound on the integral of 1/x from 1 to 2 gives
`log2<=3/4`. Thus

    Pr(Z<mu/2)<=exp[(log2/2-3/7)mu]
                <=exp(-3mu/56)<=exp(-mu/32).              (7)

Combining (5)-(7) proves the requested finite bound

    boxed: Pr(Z<mu/2 or Z>2mu)<=2 exp(-mu/32).             (8)

All thresholds may be nonintegers. The exponential Markov inequalities
remain valid for the stated strict events, with no rounding adjustment.

## 3. The fixed-size conditional law remains the same full product

For a uniform Dyck word of fixed semilength r, expose every profile
coordinate except a set J of indices at mutual distances at least three.
Take J inside `[ceil(L/2),L-2]`, with s>=10. The exact law and all terminal
constraints were proved in
`scratch/PBBS_EVERY_THIRD_PROFILE_CONDITIONAL_LAW_AND_MAXIMAL_ATOM_INDEPENDENT_AUDIT_20260908.md`.

For a free x=a_s, write its fixed neighbors as

    A=a_(s-2), b=a_(s-1), c=a_(s+1), D=a_(s+2).

Its FULL conditional weight and integer support are

    w(x)=binom(A+x,2b) binom(b+c,2x) binom(x+D,2c),
    a=max(2b-A,2c-D) <= x <= u=floor((b+c)/2).            (9)

Every free variable affects only the convex constraints and factors at
indices s-2,s-1,s. They are disjoint for the chosen J, so after exposing
the others these conditional laws are independent. The support (9)
already implies all nonnegativity, monotonicity, and extinction constraints;
there is no extra restriction by the location of the terminal height.

The new assumption is ONLY that the exposed data admit at least one
feasible completion satisfying:

    A_good: |a_j-r/(j+1)|<=.01 r/(j+1),   0<=j<=L+1;
    B_good: mu_j/2<=ell_j<=2mu_j,         0<=j<L.          (10)

The rest of this proof uses one such completion merely to choose a
reference value x*. It does NOT condition the free variable x, or any
other free variable, on belonging to that completion or satisfying (10).

## 4. What one good completion guarantees locally

Fix s in J and put

    m=r/(s+1)^3,
    alpha=A+x*-2b,
    gamma=b+c-2x*,
    beta=x*+D-2c.

These are exactly ell_(s-2), ell_(s-1), ell_s in the chosen completion;
all their B_good indices are between zero and L-1.

For m>=1, the three means in (3) obey the crude bounds

    m/2<=mu_j<=4m,       j=s-2,s-1,s.

To verify them explicitly, the main term divided by m is between

    1.98 (s+1)^3/[(j+1)(j+2)(j+3)]

and the same expression with 1.98 replaced by 2.02. For s>=10 the
displayed cubic ratio is between 3/4 and 3/2. The additive +1 in
the numerator contributes at most `1/[(s-1)(s+1)]<=m/99`.
Thus the asserted loose bounds hold. Using B_good yields

    m/4<=alpha,beta,gamma<=8m.                            (11)

The size condition A_good also gives

    x*>=.99(s+1)^2m>=100m,
    x*/2<=A,D<=2x*.                                     (12)

For example the extreme neighbor-to-x* ratios are bounded by
`(99/101)(11/13)>1/2` and `(101/99)(11/9)<2`.

With U=(b+c)/2, equations (9)-(11) become

    a=x*-min(alpha,beta),   U=x*+gamma/2,
    3m/8<=U-a<=12m,
    [a,U] subset [x*-8m,x*+4m].                          (13)

These facts concern the entire conditional support. In particular they
do not restrict it to the set of free values making (10) true.

## 5. Unimodality and explicit mode separation

The exact ratio remains

    R(x)=w(x+1)/w(x)
      =[(A+x+1)(D+x+1)(b+c-2x)(b+c-2x-1)]
        /[(A+x+1-2b)(D+x+1-2c)(2x+1)(2x+2)].            (14)

It is decreasing on its positive interior: the two large-factor ratios
decrease because b,c>0, and the remaining numerator factors decrease
while the denominator factors increase. Therefore w is log-concave.

Assume first m>=2^20 and set `eta=2^-16`. From (12)-(13), throughout
the support the factor

    K(x)=(A+x+1)(D+x+1)/[(2x+1)(2x+2)]

satisfies `1/25<=K(x)<=25`, by exactly the numerator/denominator
comparison using x*/2<=x<=2x*.

For a<=x<=a+eta m, one lower slack is at most `eta m+1<=2eta m`.
The other is at most 9m. Both numerator slack factors are at least m/2,
since U-a>=3m/8. Thus

    R(x)>=1/(1800 eta)>1.                               (15)

For `U-eta m<=x<u`, the numerator slacks are at most 2eta m, whereas
both lower slacks are at least m/4. Thus

    R(x)<=1600 eta^2<1.                                 (16)

Every integer mode M consequently satisfies

    M-a>=eta m/2=2^-17 m,
    u-M>=eta m/2=2^-17 m.                               (17)

The upper endpoint rounding costs at most 3/2: (16) gives
`M<U-eta m+1` and u>=U-1/2. Since m>=2^20, this is comfortably
absorbed in eta m/2. The lower endpoint is already an integer.

## 6. Full-law maximal atom, with the constant 2^20

Suppose m>=2^40. Then `sqrt(m)<=2^-20 m`. Throughout the real
interval `[M-sqrt(m),M+sqrt(m)]`, (17) leaves distance at least
`2^-18 m` from both integer support endpoints. Thus each lower slack
in (14), and each of its two numerator slack factors, is at least
`2^-18 m`; the latter follows from `b+c-2x=2(U-x)` and the harmless
subtraction of one. Also x>=m.

Dropping the two positive large-numerator derivatives gives

    |(log R)'|
       <=6*2^18/m+2/m <2^21/m                            (18)

throughout that interval. A zero of log R lies between M-1 and M.
Set `rho=sqrt(m)/2^11`, which is at least one. For every integer
`|t|<=rho`, summing the log-ratio derivative estimate gives

    log[w(M+t)/w(M)]
       >=-2^21 |t|(|t|+1)/(2m)>=-1/2.                   (19)

At least rho integer positions satisfy this bound. Normalizing the
ENTIRE law therefore gives

    max_x Pr(x | exposed)
       <=2^11 exp(1/2)/sqrt(m)<2^12/sqrt(m).             (20)

For 0<m<2^40, the trivial probability bound one is at most
`2^20/sqrt(m)`. Consequently, with no restriction on m>0,

    boxed: max_x Pr(a_s=x | exposed)
       <=min(1,2^20/sqrt(m))
       <=min(1,2^20 sqrt((L+1)^3/r)).                    (21)

For m<1 no local slack claim was needed: it belongs to this same trivial
branch. Thus (21) has no hidden lower-bound hypothesis on m.

## 7. Exact scope of the existence hypothesis

An exposed configuration may have many completions, some regular and
some very irregular. If at least one completion satisfies (10), its
reference x* proves (11)-(13), which constrain the fixed weight (9).
The mode and normalization estimates then apply to ALL x in that
weight's support. They do not condition on x=x*, nor do they discard
the irregular completions from the normalizing denominator.

Accordingly one may first bound a sieve event under these independent
full laws and only afterward integrate over the set of exposed data
admitting a good completion. This is the precise conditional interface
required by the proposed first-moment argument.

The note certifies this interface and the auxiliary reverse-kernel tails.
It does not itself prove the fixed-size exceptional-probability transfer,
the prime-divisor sieve, or the final `exp(-c G_r)` word-length bound.
Those remain the explicitly separate downstream estimates.
