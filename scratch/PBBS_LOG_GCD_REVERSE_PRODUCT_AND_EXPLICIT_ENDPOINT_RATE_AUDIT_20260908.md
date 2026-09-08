# Log-gcd reverse product: explicit probability, word charge, and endpoint rate

Date: 2026-09-08. Independent probability and constant audit by
exact_b_finite_frontier. Pure proof and source reads only; no mathematical
program or word search was run.

Verdict: all proposed domain and constant guards pass without an additional
asymptotic qualification. On the linked finite PBBS inputs, the actual
height-adaptive construction satisfies

    nu(k)/W(k) <= 1+exp[-(k(log k)^2)^(1/5)/128]
               <= 1+exp(-k^(1/5))                         (1)

for every integer k>=ceil(exp(exp(2^21))). All logarithms are natural.
This is an upper construction bound, not exact equality nu(k)=B(k).
The finite word record is unchanged by this audit.

## 1. The explicit domain and elementary scale guards

Write

    X=log r,  D=log X>=2^20,
    Gamma=r^(1/5)X^(-3/5),
    J=Gamma X=(rX^2)^(1/5),
    L=floor J,  n=2r+1.

All the following estimates hold on this entire domain. The exponential
series gives X=e^D>=D^2/2>=128D. Consequently

    log Gamma=(X-3D)/5>=D+400,
    Gamma>=2^400 X.                                      (2)

Indeed X>=128D>=8D+2000 on D>=2^20, and e^400>2^400.
In particular J>=2, and

    J/2<=L<=J,  L+2<=2J,
    L>=2^399 X^2,
    Gamma^2>=2^400 J>=2^400 L,
    r/J^3=Gamma^2.                                       (3)

Also log J=(X+2D)/5<X/4. These estimates imply every elementary
lower bound on L used below, including

    L>=128X,  L>=64log2,  L>=6log2,  X>=6.               (4)

They also put all tested depths before extinction on the coarse good
event: L+2<=2J<r in this domain. There is no hidden sufficiently-large
condition beyond D>=2^20.

## 2. Probability spaces and the coarse profile event

Let P_r be the uniform Dyck-root law at fixed semilength r. Let

    P*(D)=4^(-|D|)/2

be the normalized auxiliary law on all finite Dyck words. Conditioning
P* on a_0=r gives precisely P_r. The exact normalizing cost satisfies

    Q_r=1/P*(a_0=r)<=2(r+1)(2r+1)<=12r^2.                (5)

Define the coarse event

    A={|a_j-r/(j+1)|<=.01r/(j+1), 0<=j<=L+1}.

Only Sections 1-2 of the preceding finite audit
`PBBS_REVERSE_PROFILE_FIXED_SIZE_TRANSFER_EXPLICIT_DOMAIN_AUDIT_20260908.md`
are needed for its probability bound:

    P_r(A^c)<=exp(-2^-24 Gamma^2).                        (6)

This is already a fixed-size estimate. No new factor Q_r is placed on
it. The event used in the present argument is

    G=A AND all first-L original incoming-gap rows primitive.

There is no separate second-difference truncation in this G.

## 3. Whole-row primitive failure and its explicit absorption

The exact auxiliary whole-row law, proved in
`PBBS_LOG_GCD_WHOLE_ROW_LAW_AND_SUCCESSIVE_CONDITIONING_AUDIT_20260908.md`,
is an iid geometric vector conditional on the entire child word. At
depth s its length is p=2a_(s+1)+1, with
Pr(Z_i=t)=(1-q)q^t and q=(s+2)^(-2)<=1/4.
This is not asserted after imposing a_0=r or restricting the parent size.

For a j-fold repeated row, j|p and j>=3, its exact auxiliary probability is

    [(1-q)^j/(1-q^j)]^(p/j).

Taking logarithms and using
q^(j-1)/[j(1-q^j)]<=4/189<1/3 bounds this by exp(-2pq/3).
A union bound over possible repeat factors gives at most
p exp(-2pq/3). The p=1 row is primitive and has failure probability zero.
In particular the bound includes zero-total rows rather than silently
omitting them.

On the relevant coarse child-size ranges, p<=3r+1 and
pq>=r/(L+2)^3. Drop the fixed-size and irrelevant parent restrictions
before applying the auxiliary conditional row law, then pay (5) once.
The exact interface from the cited whole-row audit is

    P_r(A AND some first-L row nonprimitive)
       <=Q_r L(3r+1)exp[-2r/(3(L+2)^3)]
       <=48r^3L exp(-Gamma^2/12).                        (7)

The last line uses L+2<=2J and r/J^3=Gamma^2. To absorb its prefactor,

    log(48r^3L)<=6+3X+log J<=5X<=L.

At the same time (3) gives Gamma^2/12>=3L. Therefore (7) is at most
exp(-2L). Equation (6) is also at most exp(-2L), because
2^-24Gamma^2>=2^376L>=2L. Adding the two errors gives

    P_r(G^c)<=2exp(-2L)<=exp(-L).                        (8)

The last inequality holds by L>=log2. No auxiliary-law normalizer or
primitive-conditioned distribution has been omitted in (7)-(8).

## 4. Successive conditioning gives a full reverse product

Fix a positive integer u<=exp(L/16), and test

    2a_s+1 divides u,  s=0,...,L-1.

The complete local arithmetic and negative-binomial interface are proved
in `PBBS_LOG_GCD_DIVISIBILITY_AND_FINITE_REVERSE_TEST_AUDIT_20260908.md`.
Under P*, conditional on the entire deeper profile, if the two child
sizes obey their A ranges, the ENTIRE parent-size law satisfies

    P*(2a_s+1 divides u | deeper profile)<=1/2.           (9)

Its support is infinite. The log-gcd proof needs only the lower support
bound and maximal atom; no artificial parent-size upper bound is imposed.
Its explicit numerator/denominator comparison uses X>=128D and is valid
uniformly in the fixed candidate u and every allowed deeper profile.

For clarity, define E_s to impose the A ranges at depths s through L+1
and all divisibility tests at depths s through L-1. The event E_(s+1)
is measurable in the deeper-profile sigma-field and supplies the two
child ranges needed in (9). Conditional on that sigma-field, drop the
parent's own A range before applying (9). The tower property gives

    P*(E_s)<=P*(E_(s+1))/2.

After L steps, E_L imposes only the two tail ranges, so P*(E_L)<=1.
Consequently

    P*(A AND all L tests)<=2^-L.                        (10)

This is successive conditioning, not independence of adjacent profile
coordinates. The formal proof, including exact tested depths and the
tail ranges, is in the whole-row/successive-conditioning audit cited in
Section 3.

Now impose fixed size only at the end:

    P_r(A AND all tests)
       =Q_r P*(a_0=r AND A AND all tests)
       <=Q_r2^-L.                                      (11)

There is no claim that the reverse kernel (9) remains valid under a_0=r.
Primitivity was not included in either reverse conditioning step.

## 5. Uniform union over actual short periods

On G, synchronous descent through its first L primitive original rows
forces all the tested circumferences to divide the actual g=f^2 period v.
Therefore the event G AND v=u is contained in the event in (11).
Using (11) separately for each deterministic positive integer u, then
union-bounding over u<=exp(L/16), proves

    P_r(v<=exp(L/16))
       <=exp(-L)+Q_r exp(L/16)2^-L.                     (12)

The parameter u in the local proof is never the random actual period
under an additional conditioning. The integer union is what permits its
use for the random v.

For the numerical simplification, (5) gives

    log Q_r<=log12+2X<=3X<=L/16.

Since log2>=2/3,

    Q_r exp(L/16)2^-L
       <=exp[-(log2-1/8)L]<=exp(-L/2).

Equations (4) and (12) then give the clean bound

    P_r(v<=exp(L/16))<=exp(-L)+exp(-L/2)
                      <=exp(-L/3).                     (13)

Indeed 2exp(-L/2)<=exp(-L/3) whenever L>=6log2.

## 6. Exact collar charge with room for the final sum

The physical state and original-Dyck laws agree for the rotation-invariant
height and period. The height-adaptive word has exact normalized overhead

    E[(2h-1)/v].                                        (14)

The invariant-particle period theorem gives n|v globally, even without
primitive rows. Thus the integrand in (14) is at most one everywhere.
When v>exp(L/16), it is at most n exp(-L/16). Splitting at this threshold
and using (13) yields

    overhead<=exp(-L/3)+n exp(-L/16).                   (15)

There must be margin before adding these two terms; merely bounding the
second by exp(-L/32) would not by itself justify that same final bound.
Here (3)-(4) provide the stronger estimate

    log n<=log(3r)<=2X<=L/64,
    n exp(-L/16)<=exp(-3L/64).

Both terms in (15) are at most exp(-3L/64). Since L>=64log2,

    overhead<=2exp(-3L/64)<=exp(-L/32).                 (16)

This verifies the proposed final constant with an explicit strict margin,
and uses a deterministic constructed word through the exact cycle-sum
identity (14).

## 7. Every dimension and the endpoint exponent at the same threshold

Let k>=ceil(exp(exp(2^21))). Use the odd source n=k when k is odd and
n=k-1 when k is even, with r=(n-1)/2. On this range k>=6, so

    r>=k/3,  log r>=.5log k,
    loglog r>=loglog k-log2>=2^20.

All previous finite inequalities apply. The usual trimmed lift doubles
both word length and width in the even case, preserving the normalized
overhead. Moreover

    J=(r(log r)^2)^(1/5)
       >=12^(-1/5)(k(log k)^2)^(1/5)
       >=.5(k(log k)^2)^(1/5),
    L>=J/2>=.25(k(log k)^2)^(1/5).

The inequality 12^(-1/5)>=1/2 follows from 12<=2^5. Substitution in
(16) proves the first bound in (1), with coefficient exactly 1/128.

The endpoint corollary holds at the SAME explicit threshold. Indeed

    (k(log k)^2)^(1/5)/128>=k^(1/5)

is equivalent to

    loglog k>=(35/2)log2.

This is immediate from loglog k>=2^21. Therefore the second inequality
in (1) also holds for every k at the stated threshold; no unspecified
eventual enlargement is required.

## 8. Scope

The old coarse A bound is used only under the fixed-size original law.
The whole-row and local divisibility kernels are used only under P*,
before paying its normalizer. Primitive rows imply necessary period tests
but are never imposed on those kernels. All polynomial prefactors, floors,
candidate counts, and the final two-term sum are absorbed explicitly on
the stated domain.

This completes the bounded probability and word-constant audit. No new
finite k=17 word was claimed or searched for; the missing 24,660-letter
file remains outside this proof. Exact equality is not a consequence of
the rate in (1).
