# Profile sieve: original law, regularity, conditioning, and explicit word charge

Date: 2026-09-08. Independent audit by exact_b_finite_frontier.
Method: symbolic proof and local source reads only; no mathematical program
or construction search was run. The finite-word records are not modified by
this note.

Verdict: the probability bookkeeping passes. Given the separately audited
full conditional profile law and prime-rejection lemma reproduced below,
the height-adaptive word has normalized excess at most

    exp[-2^-50 k^(1/7)(loglog k/log k)^(6/7)]

for every k>=ceil(exp(exp(2^21))). All logarithms are natural. In particular
for each fixed 0<theta<1/7 its excess is at most exp(-k^theta) in all
sufficiently large dimensions. This conclusion concerns the linked internally
audited PBBS construction, not exact equality nu(k)=B(k).

## 1. The original probability space and the collar identity

Put n=2r+1. A labelled rank-r binary state has a unique unmatched zero
and therefore a unique normalized Dyck root D of semilength r. Conversely
each D has exactly n distinct labelled rotations. A nontrivial rotational
repetition would divide the word's zero-minus-one excess, which is one.
Thus uniform physical middle states correspond exactly to uniform Dyck D
and an independent uniform root location, and W_r=n Cat_r.

The entire pruning profile, primitive status of each cyclic incoming-gap
row, Dyck height h, and physical g=f^2 period v are invariant under physical
rotation. They therefore have the same law in the two descriptions. There
is no change to a uniform-cycle law and no inverse cycle-length reweighting
in any of the probabilities below.

For the height-adaptive construction the total collar charge is one term
2h_C-1 per physical owner cycle C. Sampling a uniform physical state instead
gives the exact identity

    (constructed length-W_r)/W_r = E[(2h-1)/v].             (1)

The invariant-particle theorem establishes n|v without any primitivity
assumption, so v>=n and (2h-1)/v<=1 everywhere. The exact sources are
`PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`,
Sections 2-4 and 6, and
`PBBS_SUPERPOLYNOMIAL_PERIOD_REGULARITY_AND_PRIMITIVE_ROWS_INDEPENDENT_AUDIT_20260908.md`,
Section 6. The probabilities used in (1) are state probabilities, not
probabilities after conditioning on a short period or a sampled incidence.

## 2. Scales and explicit domain

Use

    X=log r,  D=log X>=2^20,
    T=(rX/D)^(1/7),  L=floor(T),
    F=r^(1/7)(D/X)^(6/7)=r/T^6=T D/X,
    B=r/(L+3)^3,  Delta=B/10000.

The following elementary guards hold throughout this domain. Since
X=e^D>=D^2/2 and D>=2^20, X>=128D. Hence

    log F=(X-6D+6log D)/7 >= X/8 >= D+50,
    F>=e^50 X>=2^50 X.                                    (2)

Here X/8>=16D>=D+50. Also T>=3, L+3<=2T, and

    Delta/sqrt(r)>=sqrt(F)/80000,
    B>=F T^3/8>=F.                                        (3)

For use in union bounds, log(2(L+2))<=X. For example
log T=(X+D-log D)/7<X/4, and T>=2 gives
log(2(L+2))<=log4+log T<=X on the stated domain.

## 3. Uniform all-depth concentration gives the regularity error

Write a_j for the original pruning semilength at depth j. The exact finite
one-depth input is

    Pr(|a_j-r/(j+1)|>(4+x)sqrt(r))<=2exp(-x^2/6),          (4)

for every depth j and every x>=0. It comes from the all-depth finite
pruning census, slice bounded differences, and unique-root argument in
`PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`, Section 2.
It is not a fixed-depth approximation and requires no independence
between profile coordinates.

Let Regular require |a_j-r/(j+1)|<=Delta for 0<=j<=L+1. By (2)-(3),
Delta/sqrt(r)>=8. Set x=Delta/sqrt(r)-4, which is at least
Delta/(2sqrt(r)). Then

    x^2/6 >= Delta^2/(24r)
           >= F/(1536*10^8) >= 2^-38 F.

The last comparison is the exact inequality 1536*10^8<2^38.
A union bound over the L+2 depths, followed by (2), gives

    Pr(not Regular)
       <=2(L+2) exp(-2^-38 F)
       <=exp(-2^-39 F).                                  (5)

Indeed the logarithmic prefactor is at most X<=2^-50 F. All floor
and endpoint allowances are included in L+3 and the displayed depth set.

## 4. Regular profiles: large rows and negligible primitive failures

For 0<=s<L define ell_s=a_s-2a_(s+1)+a_(s+2) and p_s=2a_(s+1)+1.
The exact second difference of the center r/(s+1) is

    2r/[(s+1)(s+2)(s+3)].

On Regular the error in this difference is at most 4Delta. Consequently

    ell_s>=2B-4Delta>=B,
    p_s>=2r/(L+3)-2Delta+1>=r/(L+3).                     (6)

Thus min(p_s,ell_s)>=B, the relevant cores are nonempty, and the rows
are not zero rows. The first L+1 decreases are strict as well:

    a_s-a_(s+1)>=r/(L+3)^2-2Delta>0,  0<=s<=L.

Conditional on the FULL original profile, row s is a uniform weak
composition of ell_s into the odd number p_s of parts. The exact
composition repetition count in the preceding primitive-row audit gives

    Pr(row s nonprimitive | full profile)
       <=2p_s exp[-(2log2/3)min(p_s,ell_s)].               (7)

This follows by bounding a j-fold repetition, j>=3, by a fraction
D_s^(-2/3), where D_s=binom(ell_s+p_s-1,p_s-1), and using
D_s>=2^(min(ell_s,p_s)-1). No row is sampled from a reached-state or
Palm law. Independence of rows is not needed for the following union bound.

Since p_s<=n<=3r and L<=r, (6)-(7) imply, on every regular full profile,

    Pr(some first-L row nonprimitive | profile)
       <=exp(3X-B/3)<=exp(-F/4).                         (8)

For the last inequality use B>=F and 3X<=F/12, both from (2)-(3).
Integrating (8) over regular profiles and adding (5), the event

    G=Regular AND all first-L original rows primitive

satisfies

    Pr(G^c)<=exp(-2^-40 F).                              (9)

Every regular-profile and composition probability here is taken before
any conditioning on primitive status.

## 5. The full conditional profile law after exposing every third coordinate

Let

    J={ceil(L/2),ceil(L/2)+3,...} intersect [ceil(L/2),L-2].

Then |J|>=L/8 on the present domain. Expose EVERY profile coordinate
a_j with j not in J, including the terminal padded zeros. Call this
exposed sigma-field E. Let Regular_E require the exposed coordinates among
0,...,L+1 to obey their Delta bounds.

The exact profile weight is

    product_j binom(a_j+a_(j+2),2a_(j+1)).

Each free a_s affects only the three consecutive factors with indices
s-2,s-1,s. The factor sets of different chosen coordinates are disjoint;
each convexity constraint also contains at most one free coordinate.
Thus, conditional on feasible E, the free coordinates are independent
under their FULL feasible laws. The precise theorem, including support
endpoints and maximal atoms, is
`PBBS_EVERY_THIRD_PROFILE_CONDITIONAL_LAW_AND_MAXIMAL_ATOM_INDEPENDENT_AUDIT_20260908.md`.

On Regular_E all four exposed neighbors of a_s are within Delta of their
centers. Since Delta<=r/[10000(s+1)^3], that theorem gives a unimodal law
with maximal atom at most

    rho=1024 sqrt((L+1)^3/r).                             (10)

Crucially, this statement is about the entire conditional support, not
the law further restricted to the free coordinate's own regularity window.
The latter restriction is neither imposed nor used in the sieve.

## 6. Uniform fixed-integer sieve input

The complete separately audited prime-sieve proof is
`PBBS_PROFILE_PRIME_SIEVE_AND_EXPLICIT_ONE_SEVENTH_RATE_INDEPENDENT_AUDIT_20260908.md`,
particularly Sections 6-7 for the exact finite interface below. It uses the band

    Y=r^(1/7) X^(-4/5),  Z=r^(1/7) X^(-7/10).

For each FIXED positive integer u with log u<=F/6400, take the odd primes
Y<p<=Z which do not divide u. On every feasible exposed configuration
satisfying Regular_E, (10) and that lemma imply

    Pr(2a_s+1 does not divide u | E)>=D/(100X), s in J.   (11)

The prime audit actually obtains the stronger D/(8X) on D>=2^20;
retaining 1/100 leaves its full advertised margin. The estimate is uniform
over both u and the exposed regular configuration. Its local arithmetic
uses the full-law residue discrepancy bound at most 2rho, followed by a
second-moment bound for primes not dividing u. This section records its
exact probability interface; the prime-counting proof is a separate audit.

## 7. Integrate first; use primitivity only for a deterministic inclusion

For each fixed u define A_u={2a_s+1 divides u for every s in J}. Then

    Pr(Regular AND A_u | E)
       <=1_Regular_E Pr(A_u | E)
       <=1_Regular_E (1-D/(100X))^|J|
       <=1_Regular_E exp(-F/1600).                       (12)

The first inequality DROPS the regularity restrictions on the free
coordinates. The second uses their independence under the full conditional
law, and the last uses |J|>=L/8 and
L D/X>=T D/(2X)=F/2. Integrating (12) gives

    Pr(Regular AND A_u)<=exp(-F/1600).                  (13)

There is no division by Pr(Regular_E), no conditioning on G, and no claim
that independence survives conditioning on primitivity.

If the first L original rows are primitive, the actual physical period v
is divisible by each 2a_s+1 for 0<=s<=L, by the invariant-row period
theorem. Therefore

    {G AND v<=exp(F/6400)}
       subset union_(1<=u<=floor(exp(F/6400))) {Regular AND A_u}.

Here primitivity is used only for this pointwise inclusion. Applying (13)
separately to each deterministic u, and then a union bound, gives

    Pr(G AND v<=exp(F/6400))<=exp(-3F/6400).              (14)

Combining (9) and (14), and absorbing the factor two using (2), proves

    Pr(v<=exp(F/6400))<=exp(-2^-41 F).                   (15)

The argument never conditions the sieve on the actual period. Its
fixed-u bounds are applied before the union over possible periods.

## 8. Word charge, both parities, and every exponent below 1/7

Split (1) at v=exp(F/6400). On the small-period event its integrand is
at most one; on the complement it is less than n exp(-F/6400). Since
log n<=2X and F>=2^50X, (15) yields

    E[(2h-1)/v]
       <=exp(-2^-41 F)+n exp(-F/6400)
       <=exp(-2^-41 F)+exp(-F/12800)
       <=exp(-2^-42 F).                                 (16)

This controls the actual deterministic collar sum of the height-adaptive
word, not an average construction selected at random.

For an arbitrary target dimension k, use n=k when k is odd and n=k-1
when k is even, with r=(n-1)/2. The established trimmed one-coordinate
lift doubles both length and width in the even case, so it preserves
the normalized overhead. For k>=ceil(exp(exp(2^21))), r>=k/4 and

    loglog r>=loglog k-1>=2^20.

Also loglog r>=(loglog k)/2 and log r<=log k. Hence, writing
F_k=k^(1/7)(loglog k/log k)^(6/7),

    F>=4^(-1/7)2^(-6/7)F_k>=F_k/4.

Equation (16) therefore even gives coefficient 2^-44 in front of F_k;
the proposed smaller coefficient 2^-50 is safe throughout the stated
all-dimension range.

Finally F_k/k^theta tends to infinity for every fixed 0<theta<1/7.
Thus 2^-50F_k>=k^theta eventually, yielding the stated
exp(-k^theta) normalized excess in every sufficiently large dimension.
No numerical computation, uniform-cycle resampling, primitive-conditioned
sieve, or growing-parameter limit substitution is hidden in these steps.
