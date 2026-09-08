# Every-third profile conditioning and a uniform full-law atom bound

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No mathematical program was run. Verdict: the exact factorization and
the proposed entire-conditional-law anti-concentration estimate pass.
An explicit constant 1024 is valid below. Subsequent prime-sieve and
scale estimates are separate audits.

## 1. Exact weight of the full original pruning profile

Let a_j be the semilength of a Dyck word after j peak-deletions, with
`a_0=r`. Pad the sequence by zero after extinction, in particular
`a_r=a_(r+1)=0`. The feasible profiles are precisely the nonnegative
integer sequences with these endpoints and

    a_j-2a_(j+1)+a_(j+2)>=0.

Indeed these inequalities say that the nonnegative successive losses
are nonincreasing. Working backward from the two terminal zeros shows
that every loss is nonnegative and hence that a_j is nonincreasing.
If a_j is positive, its loss must be positive, since otherwise all
later losses would vanish and extinction would be impossible.
Thus a feasible padded sequence has one ordinary terminal height,
at most r. There is no independent variable-height constraint to impose.

The inverse-pruning fibre at level j has

    ell_j=a_j-2a_(j+1)+a_(j+2),
    p_j=2a_(j+1)+1,
    binom(ell_j+p_j-1,p_j-1)
       =binom(a_j+a_(j+2),2a_(j+1))

possibilities. This exact fibre count and the bottom-up reconstruction
are proved in sections 1 and 2 of
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`.
The encoding records persistent equality-particle gap coordinates and
reconstructs the specified root, so it is not a count modulo rotations.
When the next core is empty, p_j=1 and the last nonempty height-one
word is unique; the displayed binomial is one, as required.

It follows that the exact number of uniform-Dyck words with profile a is

    W(a)=product_(j=0)^(r-1) binom(a_j+a_(j+2),2a_(j+1)).    (1)

Factors past extinction equal one, so this is also the user's product
through the last nonempty level. Its total normalization is Cat_r.
Uniform physical middle states give the same law, since every Dyck root
has exactly n=2r+1 distinct labelled rotations and n is fixed.

## 2. Leaving every third coordinate unexposed gives a product law

Take `20<=L<=r`, and set

    J={ceil(L/2), ceil(L/2)+3, ...} intersect [ceil(L/2),L-2].

The interval contains `floor(L/2)-1` integers. Thus

    |J|=ceil((floor(L/2)-1)/3)>=L/8,

and every s in J satisfies s>=10. Expose EVERY a_j with j not in J,
including the terminal padded entries. Consider a feasible exposed
configuration of positive probability.

The free coordinate x=a_s occurs in exactly the three factors with
indices s-2,s-1,s. Write

    A=a_(s-2), b=a_(s-1), c=a_(s+1), D=a_(s+2).

Its unnormalized conditional weight is exactly

    w_s(x)=binom(A+x,2b) binom(b+c,2x) binom(x+D,2c).      (2)

Its integer support is the whole interval

    a:=max(2b-A,2c-D) <= x <= u:=floor((b+c)/2).           (3)

There is no additional truncation in (3). The exposed data came from
a feasible profile, so `A>=b>=c>=D>=0`. In particular the lower endpoint
is at least c>=0, while the upper endpoint is at most b. Hence (3)
already implies positivity where needed and both monotonicity constraints.
Its three inequalities are exactly the affected convexity constraints.

For consecutive chosen indices s and s+3, their affected factor sets
`{s-2,s-1,s}` and `{s+1,s+2,s+3}` are disjoint. Every convexity constraint
also contains at most one free coordinate. Thus both the feasible set
and the weight factor as products. After normalization, the free a_s
are independent and each has its FULL law proportional to (2) on (3).
No requirement that the free values themselves be regular has been made.

## 3. A finite local regularity hypothesis

For a fixed s>=10 put

    x0=r/(s+1),     m=r/(s+1)^3.

Assume only that its four EXPOSED neighbors satisfy

    |a_j-r/(j+1)|<=delta,   j=s-2,s-1,s+1,s+2,
    delta<=m/10000.                                       (4)

The application uses `delta=Delta=r/[10000(L+3)^3]`, which satisfies
(4) for every chosen s. Define the three central slacks

    alpha=A+x0-2b,
    beta =x0+D-2c,
    gamma=b+c-2x0.

Their values at the harmonic centers are, respectively,

    2m(s+1)^2/[s(s-1)],
    2m(s+1)^2/[(s+2)(s+3)],
    2m(s+1)^2/[s(s+2)].

For s>=10 these lie between m and 3m with ample margin: the first
lies in (2m,121m/45], the second in [121m/78,2m), and the third in
(2m,121m/60]. Their errors are at most 3delta, 3delta, and 2delta.
Consequently

    m<=alpha,beta,gamma<=3m.                              (5)

Also `x0=(s+1)^2m>=121m` and

    x0/2 <= A,D <= 2x0.                                  (6)

Writing U=(b+c)/2 for the real upper endpoint, (3) and (5) give

    a=x0-min(alpha,beta),   U=x0+gamma/2,
    3m/2<=U-a<=9m/2,
    [a,U] subset [x0-3m,x0+3m/2].                         (7)

In particular (7) concerns the ENTIRE conditional support, which is
much wider than the original regularity tolerance delta.

## 4. Exact log-concavity and a mode separated from the endpoints

For integers a<=x<u, the exact consecutive-weight ratio is

    R(x)=w_s(x+1)/w_s(x)
        =[(A+x+1)(D+x+1)(b+c-2x)(b+c-2x-1)]
          /[(A+x+1-2b)(D+x+1-2c)(2x+1)(2x+2)].           (8)

Each of the ratios `(A+x+1)/(A+x+1-2b)` and
`(D+x+1)/(D+x+1-2c)` decreases with x, since b,c are positive under
(4). The other positive factors decrease as well. Equivalently,
differentiating log R gives a strictly negative derivative. Hence the
whole integer weight sequence is log-concave and unimodal.

We now prove the claimed interior-mode bound for m>=400. Put

    K(x)=(A+x+1)(D+x+1)/[(2x+1)(2x+2)].

Equations (6)-(7), with x0>=121m, imply throughout [a,U]

    1/25<=K(x)<=25.                                     (9)

If a<=x<=a+m/100, one of the two lower slack factors in (8) is at
most `m/100+1<=m/50`, and the other is at most 3m. The two numerator
slack factors are both at least 2m, by `U-a>=3m/2`. Thus

    R(x)>= (1/25) * (4m^2)/[(m/50)(3m)] = 8/3 > 1.       (10)

For an integer x with `U-m/100<=x<u`, each numerator slack is at most
m/50, whereas both lower slacks are at least m. Therefore

    R(x)<=25(m/50)^2/m^2=1/100<1.                        (11)

If M is any integer mode, (10) rules out `M<=a+m/100`.
Equation (11), applied to M-1, gives `M<U-m/100+1`. Since
`u>=U-1/2`, m>=400 yields the explicit bounds

    M-a>=m/200,     u-M>=m/200.                           (12)

Small m need not satisfy this mode-separation statement; it is not
assumed in the final uniform atom bound's trivial small-m branch.

## 5. Quantitative flatness near the mode

Suppose m>=2^20. Then `sqrt(m)<=m/1024`, so (12) shows that every real
x within sqrt(m) of M is at least m/400 from both integer support
endpoints. Each of

    A+x+1-2b, D+x+1-2c, b+c-2x, b+c-2x-1

is at least m/400 there. Also x>=m. The negative derivative of log R
is the sum of the corresponding reciprocal terms, after subtracting
the two harmless positive numerator derivatives. In detail it is at
most

    1/(A+x+1-2b)+1/(D+x+1-2c)
    +2/(b+c-2x)+2/(b+c-2x-1)
    +2/(2x+1)+2/(2x+2)
      <=2402/m <4096/m.

Hence throughout this neighborhood,

    |(log R)'|<=4096/m.                                  (13)

The mode inequalities `R(M-1)>=1>=R(M)` and continuity put a zero of
log R between M-1 and M. Summing (13) over consecutive integer ratios
therefore gives, for integer `|t|<=rho:=sqrt(m)/128`,

    log[w_s(M+t)/w_s(M)]
       >=-4096 |t|(|t|+1)/(2m)>=-1/4.                    (14)

Here rho>=8 and `rho(rho+1)<=2rho^2`; all these positions remain in
the support by (12). There are at least rho such integer positions.
Normalizing the WHOLE conditional law thus proves

    max_x Pr(a_s=x | all exposed coordinates)
       <=128 exp(1/4)/sqrt(m)<256/sqrt(m).                (15)

For 0<m<2^20 the trivial bound one is at most `1024/sqrt(m)`.
Combining it with (15) yields the uniform finite statement

    boxed: max_x Pr(a_s=x | exposed)
       <=min(1,1024/sqrt(m))
       <=min(1,1024 sqrt((L+1)^3/r)).                    (16)

The second inequality uses s<=L-2. The slightly larger L+1 is retained
to match the requested interface.

## 6. Conditioning scope and applicability

The regularity event used for (16) concerns only exposed neighbors.
The law in (16) includes every free x in (3), whether or not x is near
r/(s+1). Conditioning those free coordinates on their own regularity
windows would be a different law and is unnecessary here.

The result is a finite lemma independent of the later choice of L.
It therefore applies to both proposed scales

    L=floor((r log r/loglog r)^(1/7)),
    L=floor(r^(1/8)),

as soon as 20<=L<=r. Small m is explicitly covered by the trivial
branch of (16); there is no unquantified interior-mode assumption in
the stated uniform atom bound.

This audit certifies the exact full profile weight, the independent
conditional coordinates, the entire support including terminal
constraints, log-concavity, the finite mode bound, and constant 1024.
The modular-residue discrepancy, prime sieve, union over proposed
short periods, exceptional-profile probability, and final rate require
their separate estimates. No full-cube rate is inferred from the local
atom bound alone.
