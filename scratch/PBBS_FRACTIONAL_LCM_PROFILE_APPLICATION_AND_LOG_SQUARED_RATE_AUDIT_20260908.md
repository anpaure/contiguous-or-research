# Fractional LCM application: original profile sum and the log-squared rate

Date: 2026-09-08. Independent application audit by exact_b_finite_frontier.
Method: pure symbolic proof and local source reads. No numerical program,
construction search, or word modification was performed.

Verdict: the finite application inequality and the claimed asymptotic
optimization pass. With the rational choice lambda=1/8192, they give the
eventual all-dimension bound

    nu(k)/W(k) <= 1+exp[-(log k)^2/65536].                 (1)

Optimizing this particular estimate gives the leading exponent constant
1/(6144e^2), in the asymptotic sense made precise below. This is an
additional period-moment route, not an improvement to the stronger
one-seventh or one-fifth power rates. No assertion about exact equality
nu(k)=B(k) or a newly supplied finite word is made here.

## 1. Exact finite inputs and their original-law scope

Let n=2r+1 be odd. For a uniform original Dyck root write
n_j=2a_j+1 for the pruning circumferences, h for the height, and v for
the labelled physical period under g=f^2. The height-adaptive construction
has normalized excess

    epsilon=E[(2h-1)/v].                                  (2)

Uniform middle states and uniform Dyck roots give the same law for these
rotation-invariant quantities; this is a state average, not an average
over cycles. The invariant-row theorem gives n|v everywhere, so
(2h-1)/v<=1 without a primitivity condition.

Choose an integer L>=2^16 with n>=4096(L+3)^6. Let G be the event that
the profile is regular through level L+1 and all first L original rows
are primitive, as in
`PBBS_FINITE_MULTILEVEL_REGULARITY_AND_PRIMITIVITY_DELTA_AUDIT_20260908.md`.
That fully finite proof gives

    Pr(G^c)<=delta,
    delta=2(L+1)n(n+1)exp[-n/(2048(L+3)^6)]
             +Ln*2^[-n/(6(L+3)^3)],                    (3)

and a_j>=r/[2(j+1)] for every 0<=j<=L+1 on G.

The auxiliary Boltzmann calculation in
`PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`
proves the following UNCONDITIONAL original-Dyck joint atom bound for
every prescribed tuple satisfying these lower-size bounds:

    Pr(a_1=t_1,...,a_L=t_L)
       <=16(L+1)((L+1)!)^2 r^(-L/2)
       <=A_L n^(-L/2),
    A_L=16(L+1)3^L((L+1)!)^2.                            (4)

The conversion only needs r>=n/3. In fact 3^(L/2) would suffice in
A_L, so the displayed convenient coefficient is conservative. No
independence of the a_j is assumed. The auxiliary-law conditioning
back to fixed r was already paid explicitly in the proof of (4).

## 2. Period divisibility and the pointwise fractional-power inequality

For a prescribed tuple u_j=n_j, define d(u)=lcm(u_1,...,u_L).
On G, synchronous descent through the primitive rows makes each u_j
divide the original period v. Therefore d(u)|v. This consequence is
from `PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`.
The stronger pair-product lcm divisor is available but is not needed here.

Take

    1/3<=beta<=1/2,  0<eta<=1/6,  alpha=1+eta-beta.

These ranges ensure 1/2<alpha<=5/6<1. Since d(u)>=1, pointwise on G,

    (2h-1)/v <= n/d(u) <= n/d(u)^alpha.                  (5)

This is a direct inequality for each state. It is not Jensen's inequality
and makes no assertion about a fractional power of an averaged period.

For each tuple compatible with G,

    Pr((n_1,...,n_L)=u AND G)
       <=Pr((n_1,...,n_L)=u)<=A_L n^(-L/2).              (6)

The passage from a_j to n_j=2a_j+1 is injective and does not change
an atom's mass. Importantly, (6) does not condition the atom law on G
and does not divide by Pr(G). The primitive condition is used only to
justify (5); it is then dropped when bounding the probability in (6).
Regularity ensures that the atom bound applies to every remaining tuple.

## 3. The finite probability sum and the exact LCM input

Sum (5)-(6) over the tuples arising on G and charge G^c by (3).
Enlarging the sum to all positive integer tuples with 1<=u_j<=n only
increases it. Oddness, ordering, and profile feasibility can therefore
be dropped after the probability bound is applied. This gives

    epsilon <=delta+n A_L n^(-L/2)
                       sum_(1<=u_1,...,u_L<=n) d(u)^(-alpha).   (7)

The finite lemma in
`FRACTIONAL_LCM_MOMENT_EXPLICIT_EULER_PRODUCT_INDEPENDENT_AUDIT_20260908.md`
holds uniformly throughout the displayed beta,eta range and L>=2^16:

    sum_(1<=u_1,...,u_L<=M) d(u)^(-alpha)
       <=M^(beta L)(1+eta^(-1))^L
                    exp[96(2L/log L)^(1/beta)].          (8)

Taking M=n in (7)-(8) proves exactly

    epsilon <=delta
       +n A_L n^[-(1/2-beta)L](1+eta^(-1))^L
                    exp[96(2L/log L)^(1/beta)].          (9)

All parameters in (9) are finite. No estimate valid only for a fixed
beta or a fixed L has been promoted to a growing-parameter statement.

## 4. The proposed growing parameters are in the proved finite domain

Put

    x=log n,  y=log x,
    beta=1/2-1/(2y),  eta=1/x,
    L=floor(lambda x y),

where lambda>0 is fixed while n tends to infinity. For y>=3,
beta belongs to [1/3,1/2], and eta<=1/6 once x>=6. Also L>=2^16
eventually. Finally

    4096(L+3)^6=O_lambda(x^6 y^6)=o(e^x)=o(n),

so the finite regularity condition in (3) holds eventually. Thus all
inputs of (9) apply along the entire chosen parameter sequence.

Both terms of delta are negligible on the log-squared scale:

    log delta=-omega(x^2).                              (10)

Indeed their negative exponents contain n divided by a fixed power
of L+3, whereas the positive prefactors have logarithms O_lambda(x).
For L=O_lambda(xy), n/(L+3)^6 dominates every fixed power of x.
This proves (10) without choosing a profile-dependent cutoff or a
nonuniform hidden constant.

## 5. Exact leading-order ledger

Let B_n denote the second term on the right of (9). Its logarithm is

    log B_n=x+log A_L-Lx/(2y)+Llog(1+x)
                         +96(2L/log L)^(1/beta).          (11)

From the explicit A_L,

    log A_L=O(Llog L)=O_lambda(xy^2)=o(x^2),
    Llog(1+x)=O_lambda(xy^2)=o(x^2),
    Lx/(2y)=(lambda/2)x^2+o(x^2).                       (12)

The last expression includes the harmless floor error O(x/y).
For the only remaining leading term, put z=2L/log L. Then

    log L=y+log y+log lambda+o(1),
    z/x -> 2lambda,
    log z/y -> 1,
    1/beta=2+2/(y-1).

Consequently

    z^(1/beta)/x^2
       =(z/x)^2 exp[2log z/(y-1)] -> 4e^2 lambda^2.       (13)

The e^2 factor is essential: replacing the varying exponent 1/beta
by two before raising z would lose it. Equations (11)-(13) prove

    log B_n=-[lambda/2-384e^2lambda^2+o(1)]x^2.           (14)

Together with (10), this is the claimed asymptotic ledger whenever
c(lambda)=lambda/2-384e^2lambda^2 is positive.

## 6. Optimization and the rational parameter choice

The concave quadratic c(lambda) has its maximum at

    lambda_star=1/(1536e^2),
    c_star=1/(6144e^2).                                  (15)

Thus the optimized estimate is

    epsilon<=exp[-(c_star+o(1))(log n)^2].               (16)

Equivalently, for each fixed c<c_star, epsilon<=exp[-c(log n)^2]
for every sufficiently large odd n. The asymptotic calculation alone
does not fix the sign of the o(1) and does not assert the exact eventual
coefficient c_star with no slack.

For the rational choice lambda=1/8192, the elementary inequality e^2<8
gives the strict comparison

    c(lambda)=1/16384-384e^2/8192^2
              >4/65536-3/65536=1/65536.                 (17)

No decimal approximation to e is required. For example the exponential
series gives e<11/4, whose square is less than eight.
The strict margin in (17) absorbs the lower-order terms in (14), the
addition of delta, and the parity conversion below. It therefore proves
the exact advertised eventual coefficient 1/65536.

## 7. Both parities, comparison of rates, and limitations

For target dimension k use the odd source n=k if k is odd, and n=k-1
if k is even. The established trimmed one-coordinate lift doubles both
the word length and the width in the latter case. It therefore preserves
the normalized excess. Moreover log n/log k tends to one, so (16)
holds with log k as well. The strict margin in (17) preserves the same
coefficient 1/65536 after this conversion, proving (1) for every
sufficiently large dimension, with no parity subsequence restriction.

The exponent (log k)^2 grows faster than (log k)^(6/5), log k, and
the exponents corresponding to inverse-log errors. Thus this estimate
improves the earlier logarithmic-scale routes. However both

    k^(1/7)(loglog k/log k)^(6/7)
    and k^(1/5)(log k)^(-3/5)

grow faster than (log k)^2. Their associated negative-exponential error
bounds are stronger than (1). The constant in (15) optimizes only the
present finite-bound calculation; it is not an optimal OR-word constant.

This note establishes an eventual asymptotic rate, not an explicit finite
starting dimension for (1), a smaller literal k=17 word, or exact equality
nu(k)=B(k). Every probability estimate is under the original root law,
and all uses of regularity and primitivity in the finite sum are explicit.
