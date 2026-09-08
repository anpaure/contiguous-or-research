# Independent audit of the stopped logarithmic-LCM bound

2026-09-08. Pure-proof consistency audit by exact_equality_structure.
No mathematical program was run. The complete file
HEIGHT_ADAPTIVE_STOPPED_LCM_RATE_20260908.md was read end to end, together
with the retained finite prime budget and geometric-repetition arguments
in HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md. The root's already
executed rational report stopped_lcm_constants_certificate_20260908.json
was read; its checks were not rerun by this audit.

Verdict: the finite stopped-process inequality, four-term word bound,
asymptotic coefficient range, and odd/even passage pass. There is one
minor wording clarification in the asymptotic comparison, stated in
Section 5 below; its intended upper bound is correct.

## 1. Finite parameter domain and conditional kernel

Take odd n and an INTEGER L>=2. With B=n/[2(L+1)]>1, the parameter
range already gives L<=r-1 for r=(n-1)/2, so there is no hidden demand
for a pruning level beyond the possible fixed-size depth. Empty cores
remain possible but belong to the event n_L<B.

Under the exact auxiliary law, the full parent of a known child with
circumference p has its original independent-geometric gap row and
negative-binomial sum. The deeper history is a function of that child,
so revealing it does not alter the reverse kernel. The Fourier atom
bound gives, when p>=B and s<L,

    maxatom<=sqrt(pi)/(2sqrt2)
                *[(s+2)+(s+2)^(-1)]/sqrt B
            <=(63/100)[(L+1)+(L+1)^(-1)]/sqrt B=:mu.

The increasing factor t+1/t is used only for t>=2. The rational Machin
check in the root report certifies sqrt(pi)/(2sqrt2)<63/100. It is
harmless if mu exceeds one: it is still an upper bound, and the finite
theorem separately requires kappa<1.

No negative-binomial or independent-row claim is made after conditioning
on the original size r. The conditioning cost n(n+1) is explicitly paid
after the auxiliary probability bound.

## 2. The logarithmic-gcd budget is uniform on active histories

For the known odd LCM Q with log Q<H, expansion over its finite prime
powers and the unimodal residue bound give

    E log gcd(Q,N)
       <=sum_(p|Q)log p/(p-1)+2mu log Q.

The retained finite budget for primes up to H is log H+16. Primes
larger than H contribute at most

    (2/H)sum_(p|Q)log p <=2log Q/H<2,

since p-1>=p/2. Hence the budget is at most log H+18+2mu H.
This is an expectation under the ENTIRE parent law, not its truncation
at N<=n. Infinite parent support causes no issue: the gcd has only the
finite prime-power list of the known Q.

Every parent satisfies N>=p>=B. If its LCM increment Delta is less
than alpha log B, its gcd logarithm exceeds (1-alpha)log B. Thus

    Pr(N<=n AND Delta<alpha log B | active history)<=kappa,
    kappa=(log H+18+2mu H)/[(1-alpha)log B].

Dropping N<=n while applying Markov only enlarges the event. The
threshold is positive because B>1 and 0<alpha<1.

## 3. The finite stopped-process inequality

Reveal the depth-L core and retain only B<=n_L<=n, without renormalizing
its distribution. Start Q=1 and reconstruct the L-1 parents at depths
L-1,...,1. Kill a path if N>n; stop it successfully if log Q>=H.
On an active history, call Delta>=alpha log B a counted success.

If a is the mass of surviving failures and b that of surviving successes,
then a<=kappa and a+b<=1. Therefore, for theta>0,

    a+exp(-theta)b<=kappa+(1-kappa)exp(-theta)=:rho.

Removing paths that have hit the threshold only lowers this expectation.
Successive conditional expectations prove

    E_0[exp(-theta S)1_{survives without hit}]<=rho^(L-1).

On a surviving path without a hit, all LCM increments are nonnegative
and each counted success contributes at least alpha log B. Hence

    alpha log B*S<=log Q<H.

It follows directly that

    Pr_0(survives without hit)
       <=exp[theta H/(alpha log B)]rho^(L-1).

This is the claimed finite stopping inequality (5). No independence of
the LCM increments, success indicators, or parent sizes is assumed.
The strict inequality at the stopping boundary is consistent with the
non-strict Markov upper bound; no integer rounding of S is needed.

## 4. All four terms in the word estimate

The exact all-depth equality census under iid bits has mean at least
n/(L+1). A deviation of size n/[2(L+1)], followed by the fixed-size
root conditioning cost, gives

    Pr_r(n_L<B)<=2n(n+1)exp[-n/(8(L+1)^2)].

For the second term, a fixed-size root with n_L>=B has every child
circumference p in [B,n]. Retain ONLY this child-measurable restriction
when applying the auxiliary independent-geometric row law. An odd row
can repeat only with a factor e>=3; its exact repeat probability is

    [(1-q)^e/(1-q^e)]^(p/e)<=exp(-2pq/3).

Here p>=B and q=(s+2)^(-2)>=(L+1)^(-2). Union over at most p<=n
repeat factors, the L rows, and the size-conditioning cost gives exactly

    L n^2(n+1)exp[-n/(3(L+1)^3)].

This argument does not posit geometric independence after fixing r.
The upper restriction p<=n is retained before dropping the root event;
it is what permits the factor n in that union bound.

The third term is the stopped probability in Section 3 multiplied once
by n(n+1). A fixed-size path is never killed by N>n. On a hit with
primitive first-L rows, all sizes included in Q divide v, so v>=exp H.
Their word charge is at most n exp(-H). All remaining exceptional
states cost at most one because (2h-1)/v<1 everywhere.

Thus all four terms of (6) follow on the explicitly stated finite
parameter range. Flooring W(n) times their entire sum is legitimate
because the actual collar count is an integer. There is no fifth
unpaid initialization, survival, or root-normalization cost.

## 5. Constant limit and the one wording clarification

Put x=log n, w=(nx^2)^(1/5), L=floor(w/2), H=w/3,
alpha=1/1024, theta=log x. Then

    log B/x ->4/5,
    mu*w/x ->63/200,

    kappa -> [1/5+2(63/200)/3]/[(1023/1024)(4/5)]
            =2624/5115.

The root's exact report certifies

    5131/10000-2624/5115=1013/10230000>0.

For kappa_star=5131/10000, z=(1-kappa_star)/(1+kappa_star)=4869/15131.
The identity

    log(1/kappa_star)=2sum_(j>=0)z^(2j+1)/(2j+1)

has positive terms. The exact three-term certificate in the report
exceeds 2/3 by

    6029174125738179544/11896779586212353469765>0.

The intended asymptotic comparison is therefore valid. More precisely,
kappa<=kappa_star eventually, so with exp(-theta)=1/x,

    rho<=kappa_star+1/x,
    (L-1)log rho <=(L-1)log(kappa_star+1/x).

This is an UPPER BOUND, not an equality with
(w/2+o(w))log(kappa_star+O(1/x)): the actual kappa tends to the
strictly smaller limit above. Replacing the consolidated note's word
"is" by "is bounded above by" in that sentence makes the presentation
precise. No numerical or theorem change is required. L should likewise
be explicitly described as an integer in the finite parameter statement.

The third term's other logarithms are O(x)+O(w log x/x)=o(w), so its
decay coefficient is strictly greater than1/3. The first two error
exponents have orders n^(3/5)x^(-4/5) and n^(2/5)x^(-6/5), both much
larger than w. The last term has logarithm x-w/3. Hence the sum is at
most exp(-c w) eventually for each fixed c<1/3. Neither c=1/3 nor an
explicit onset for the optimized choice is asserted.

## 6. Both parities and comparison

For an even target dimension k use the exact lift from n=k-1. Its
word length and width double together, so the odd normalized error
is unchanged. Given c<1/3 choose c<c'<1/3. Since

    [(k-1)log^2(k-1)]^(1/5) / [k log^2 k]^(1/5) ->1,

the odd c' estimate yields the even c estimate for all sufficiently
large k. Odd dimensions already have the desired bound. Thus the
eventual all-dimension statement is correct for every fixed c<1/3.

This stopped-LCM route is weaker than the reviewed coefficient3/5
on the SAME (k log^2 k)^(1/5) scale. It has a completely specified
finite four-term inequality, but no newly certified optimized onset
or new literal word. These are upper-bound comparisons only; exact
attainment of B(k) remains open.
