# Fresh-prime reverse process: complete independent audit

2026-09-08. `exact_b_induction` read all ten sections of
`/Users/amir.nuriyev/Downloads/FRESH_PRIME_ADVANCE.md` end to end.
This is an independent pure-proof audit; no mathematical program was run
and no claimed external verifier output was assumed.

Verdict: PASS. The finite error theorem, the killed reverse process, the
selected-prime argument, the eventual constants `c<9/512`, and the explicit
onset `k>=2^2048+1` for `c=1/128` are valid on the stated inherited finite
PBBS inputs. This is internal mathematical review, not external or formal
certification.

## 1. Retained finite interfaces and the probability space

The unchanged height-adaptive word has relative collar cost

    epsilon_n=E_r[(2h-1)/v],     n=2r+1,

where v is the physical g=f^2 period, v>=n, and 0<2h-1<n. Its all-rank
literal support and opening charges are already proved in
`HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md` and its linked proof audits.

The invariant-row theorem in
`scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`
gives `lcm_{s<L}(n_s n_(s+1)) | v` when the first L original incoming
rows are primitive. Consequently every n_1,...,n_L divides v.

Under `P_0(D)=4^(-|D|)/2`, the exact reverse parent of a complete child
word E at depth s+1, of semilength t and peak count b, has

    r_s=t+b+ell_s,
    ell_s~NB(p=2t+1,q_s=(s+2)^(-2)).

The entire original row consists of p independent Geom(q_s) entries
under this REVERSE conditional law. This follows by cancellation of the
negative-binomial composition count against the uniform fixed-sum fibre.
Its normalization, persistence convention, and summation of all shallower
levels were proved in
`scratch/PBBS_LOG_GCD_WHOLE_ROW_LAW_AND_SUCCESSIVE_CONDITIONING_AUDIT_20260908.md`
and
`scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`.
All still deeper cores are deterministic functions of the child E, so
revealing them or previously chosen primes does not change this kernel.

At fixed r, uniform Dyck roots and uniform physical middle states give
the same rotation-invariant statistics. The auxiliary-to-fixed-r
normalizer is

    p_r=Cat_r/(2*4^r)>=1/[n(n+1)].                       (1)

This same number is the probability that n independent fair bits are
exactly 0D for a Dyck-r word. Thus the two conditioning uses below have
the same valid factor n(n+1); neither inserts a geometric law into the
fixed-size probability space.

## 2. Residues and the finite logarithmic prime budget

For any unimodal integer law with maximal atom m, extension by zero
has total variation 2m. Dividing the integers into residue-aligned
d-point blocks bounds each block discrepancy by its oscillation.
Summing gives

    Pr(Z=a mod d)<=1/d+2m.                               (2)

This proof covers infinite supports by limits. The negative-binomial
ratio `q(p+j)/(j+1)` is decreasing, and the retained Fourier proof gives
maximal atom `(s+2)/sqrt(2t+1)`. Multiplication by two preserves each
odd-modulus residue test for the parent size n_s. Even prime powers have
zero divisibility probability because n_s is odd.

The claimed elementary prime estimate

    sum_(p<=Y) log(p)/(p-1)<=log Y+16,    Y>=2            (3)

also passes. Dyadic central-binomial divisibility gives theta(x)<3x.
For integer m>=2 this implies

    psi(m)<=3m+3sqrt(m)log_2(m)<8m.

Indeed `log m/sqrt m<=2/e`, `log2>1/2`, and `e>8/3` bound the last
coefficient strictly below eight. Factorizing m! gives

    sum_(p^a<=m) log(p)/p^a<=log m+8.

For each p<=m, its tail after the first power exceeding m has sum at
most 2/m. Summing the weighted tails adds at most `2theta(m)/m<6`.
Thus the full sum is at most log m+14. Taking m=floor Y proves (3)
with two units of additional room. No prime number theorem or smooth-
number asymptotic is used.

## 3. One active step: selecting one genuinely new prime

Fix the finite parameters from the submission:

    B=n/[2(L+1)]>1,    mu=(L+1)/sqrt(B),
    Kappa=[log Y+16+2mu Y log n]/log B + L(1/Y+2mu),
    L>=2, Y>=2.

At a reverse step s<=L-1, an admissible child has physical size
`p=2t+1` in [B,n]. Its conditional atom bound is at most mu. The parent
size N is at least the child size, hence N>=B throughout its full support.

Let Gamma be any history-measurable set of at most L previously selected
primes, all greater than Y. A success means `N<=n` and a prime factor
greater than Y outside Gamma; `N>n` kills the trajectory.

For the largest Y-smooth divisor Q_Y(N), expand its logarithm into
prime-power indicators, retaining N<=n. Only powers p^a<=n occur.
Equation (2) bounds their main terms by (3). For each prime the total
error weight is at most `2mu log n`; there are at most Y primes. Therefore

    E[log Q_Y(N);N<=n | history]
       <=log Y+16+2mu Y log n.                            (4)

On a surviving Y-smooth outcome this logarithm is at least log B.
Markov bounds that case by the first term of Kappa. If a surviving
outcome is not Y-smooth but has no new prime, at least one member of
Gamma divides N. Equation (2) and a union bound cost at most
`L(1/Y+2mu)`. Consequently

    Pr(survive AND fail to add a prime | history)<=Kappa. (5)

The selected set need not contain every earlier large prime factor.
This causes no gap: failure means ALL current large factors belong
to the selected set, which is precisely the case covered above.

## 4. The killed process and its probability bound

Start with the actual P_0 depth-L marginal, retaining only B<=n_L<=n.
Reconstruct D_(L-1),...,D_1 using the exact reverse kernels, for
`m=L-1` steps. On each success select, for example, the smallest new
prime and add it to Gamma. All choices are measurable in the revealed
history. The inverse map never decreases physical size, so an unkilled
trajectory keeps every current child in [B,n].

Assume Kappa<=5/8. If f and s denote the conditional probabilities of
surviving failure and surviving success at an active history, then
f<=5/8 and f+s<=1. Thus

    E[2^(-increment)1_survive | history]
       =f+s/2<=1/2+f/2<=13/16.                           (6)

Multiplying by the accumulated nonnegative weight and applying the
tower property proves

    E_0[2^(-S)1_all_admissible]<=(13/16)^m.

The initial restriction was not renormalized; its mass is at most one.
No independence of successes, core sizes, or survival events is assumed.
Markov now yields

    P_0(all admissible, S<=m/16)
       <=2^(m/16)(13/16)^m<=exp(-9m/64),                  (7)

using `log(13/16)<=-3/16` and `log2<3/4`.

Each selected prime is distinct and divides some n_j with 1<=j<L.
On first-L row primitivity every such n_j divides v. Distinctness of
the PRIMES, not coprimality of the SIZES, therefore gives

    S>=m/16  =>  v>=Y^(m/16).                             (8)

A prime seen but not selected earlier is permitted at a later success;
it is then selected for the first time and does not invalidate (8).

## 5. All fixed-size transfers and nonprimitive exceptions

After imposing |D|=r, every pruning size is at most n. If n_L>=B,
all sizes of the preceding killed exploration are therefore admissible.
Drop |D|=r before using (7), then divide by (1). This proves

    Pr_r(n_L>=B, too few successes)
       <=n(n+1)exp[-9(L-1)/64].                           (9)

For the depth-L exception, the inherited iid census gives
`E N_L>=n/(L+1)` and the one-bit change bound two gives the lower tail
`2exp(-a^2/(2n))`. Since the gap to B is at least n/[2(L+1)], conditioning
the iid bits to be 0D gives exactly

    Pr_r(n_L<B)<=2n(n+1)exp[-n/(8(L+1)^2)].              (10)

For an odd length-p iid geometric row, an e-fold repetition has exact
probability `[(1-q)^e/(1-q^e)]^(p/e)`. Since e>=3 and
`1-q^e>=1-q`, this is at most `exp(-2pq/3)`. Union over at most p
possible factors. On B<=p<=n and s<L, q_s>=(L+1)^(-2), so

    Pr_0(row s nonprimitive | child)
       <=n exp[-n/(3(L+1)^3)].

When dropping fixed size here, retain the deeper-measurable restriction
B<=p<=n; fixed size and n_L>=B imply it. Apply the conditional bound
on that restricted child domain, union over s=0,...,L-1, then divide
by (1). The result is

    Pr_r(n_L>=B, some tested row nonprimitive)
       <=L n^2(n+1)exp[-n/(3(L+1)^3)].                    (11)

Rows of length one are primitive. Any empty reduced core relevant to
this argument lies in (10), since B>1. No second-difference regularity
condition or new independence is needed.

## 6. The exact finite error theorem

Combining (9)-(11) and charging all exceptional states by at most one,
while using n/v on the remaining states, gives exactly

    epsilon_n <= 2n(n+1)exp[-n/(8(L+1)^2)]
               +L n^2(n+1)exp[-n/(3(L+1)^3)]
               +n(n+1)exp[-9(L-1)/64]
               +nY^(-(L-1)/16).                         (12)

This holds for every odd n with L>=2, Y>=2, B>1, and Kappa<=5/8.
It is a bound for the unchanged all-rank word. Multiplying by W(n)
and flooring the resulting collar upper bound is valid because the
actual collar sum is an integer.

## 7. Eventual constant 9/512

Set w=n^(1/5), L=floor(w/8), Y=w. Direct limits give

    log B/log n ->4/5,    mu Y->1/16,
    L/Y->1/8,            2Lmu->1/64,

and therefore Kappa tends to `13/32+9/64=35/64<5/8`.
The logarithms of the four terms in (12) have orders, respectively,

    -Omega(n^(3/5)),
    -Omega(n^(2/5)),
    -(9/512+o(1))n^(1/5),
    -(1/640+o(1))n^(1/5)log n.

Thus every fixed c<9/512 is valid eventually in odd dimension. To
transfer the SAME c to both parities, first choose c' strictly between
c and 9/512; since (k-1)^(1/5)/k^(1/5) tends to one, the exact even
doubling lift eventually supplies the claimed c. The strict inequality
c<9/512 is appropriate; no assertion at the limiting endpoint constant
is inferred from the displayed asymptotics.

The accompanying period statement also follows: off an exceptional set
of probability `exp[-(9/512+o(1))n^(1/5)]`, equation (8) gives
`log v >=(1/640+o(1))n^(1/5)log n`.

## 8. Complete explicit onset arithmetic

Suppose x=log n>=1024 and w=exp(x/5). The fourth term of the exponential
series gives `w>=x^4/15000>=16x^2`, since x^2>=240000. In particular
w>=56, and

    L+1<=w/7,
    mu Y<=sqrt(2/343)<1/12,
    log B>=4x/5,
    L/Y<=1/8.

Inserting these bounds in Kappa gives

    Kappa<=3/8+(11/4)(1/12)+20/x
          <=29/48+5/256=479/768<5/8.                    (13)

Thus every finite hypothesis of (12) is satisfied on this domain.

The first negative exponent in (12) is at least `(49/8)w^3`, and its
logarithmic prefactor is at most 1+2x. The second negative exponent is
at least `(343/3)w^2`, with prefactor logarithm at most 1+4x. Since
`1+4x<=w/2` and both negative exponents exceed w, each term is at most
exp(-w/2).

For the third term, `L-1>=w/8-2` yields

    log(term_3)<=1+2x+9/32-9w/512.

Now `w/512>=x^2/32>=32x`, which exceeds
`1+2x+9/32+log4`. Hence this term is at most
`(1/4)exp(-w/64)`.

Finally `L-1>=w/16` and log Y=x/5 give

    log(term_4)<=x-wx/1280<=x-(4/5)w<=-w/2.

The last step uses w>=16x^2, hence x<=w/4. Each of the three
exp(-w/2) terms is at most `(1/4)exp(-w/64)` because w>=56.
Summing proves the full explicit odd-dimensional bound

    boxed: epsilon_n<=exp[-n^(1/5)/64],
           n odd, log n>=1024.                           (14)

For every integer `k>=2^2048+1`, its largest odd source dimension n is
at least `2^2048+1`; therefore log n>1024 since log2>1/2. Also
`n^(1/5)>=(k-1)^(1/5)>=k^(1/5)/2`. The exact even lift doubles length
and width together, giving in both parities

    boxed: nu(k)<=W(k)[1+exp(-k^(1/5)/128)],
           k>=2^2048+1.                                 (15)

The onset is conservative but fully supported by the supplied numerical
inequalities. No finite tests or floating-point values are premises.

## 9. Comparison with the currently retained result

The retained log-gcd theorem in `HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md`
already gives error `exp[-(k(log k)^2)^(1/5)/128]` on its recorded much
larger explicit domain. That error is asymptotically smaller than the
fresh-prime `exp(-c k^(1/5))` error for every fixed c. The fresh-prime
note therefore does not improve that asymptotic scale.

Its new numerical benefit is the proved explicit onset `2^2048+1`, far
below the previously recorded `ceil(exp(exp(2^21)))` onset. This comparison
concerns proved onsets, not an assertion that the old route could not be
re-estimated with a better threshold.

The argument improves an upper bound for the same finite construction;
it neither gives a new dimension-17 word nor proves exact equality with
B(k). The absolute excess may remain large because W(k) is exponential.
No missing user verifier or reported experiment has been represented as
executed in this audit.
