# Inverse logarithm: dyadic packing, compiler, and explicit constants

Date: 2026-09-08. Root audit by symbolic proof and local source reads.
No mathematical program has been executed locally.

This note audits the downstream steps of
`USER_PBBS_INVERSE_LOG_CLOCK_CLAIM_20260908.md`. The upstream polynomial
clock lemma is now independently reviewed in
`GEOMETRIC_CLOCK_FINITE_PGF_AND_PREFIX_RESTART_INDEPENDENT_AUDIT_20260908.md`
and `PBBS_INVERSE_LOG_ORIGINAL_COMPOSITION_TRANSFER_INDEPENDENT_AUDIT_20260908.md`.
Root read both proofs in full and checked their constants. In particular,
the explicit upstream estimate (1) is certified. The complete downstream
argument below also passes the separate full-file audit
`PBBS_INVERSE_LOG_DYADIC_AND_NUMERICAL_CONSTANTS_SECOND_AUDIT_20260908.md`.
These are internal proof reviews, not external or formal certification.

Additional independent structure-agent full-file review on 2026-09-08:
PASS. This review checked profile normalization, both occupied-support
bounds, the dyadic last-band cutoff, summed errors, literal compiler
charges, the sharp-tail aperture, numerical error absorption, parity,
and the comparison with 2^400000. Its separately proved upstream constant
2^74 exp(2^18+55) is smaller than the K_mu used here. The reviewer also
read the complete geometric proof and passed its constants. No additional
mathematical program was executed for this review.

## 1. Precisely retained numerical inputs

Put E=2^18, R=sqrt(r), W_r=binom(2r+1,r). The certified conservative
upstream numerical estimate is

    mu_H(Pi) <= K_mu (b+1)^3 Q^2,
    H<=bR, b>=1, K_mu=2^100 exp(E+64).                  (1)

The already audited inputs are

    E Q^2 <= exp(32), E Q^3 <= exp(32),
    omega=1+R/(h+2)<=2^26 Q,
    A0=2^80 exp(2^20), r0=2^1000000.

At fixed profile, latest-start charging and cutoff averaging over
ceil(cR),...,floor((c+1)R) give the main coefficient128/log r.
The finite first-gap bound is100/log r; the boundary strip costs at
most6mu/log r. All other errors remain actual conditional bad-incidence
mass plus a bounded coupling error, not unbounded Markov majorants.
Their weighted mean is bounded by

    delta_r(c)=exp((A0+64)(c+2)^2) r^(-1/400),             (2)

uniformly for r>=r0, 1<=c<=sqrt(loglog r). These exact constants
are in the preceding terminal-charging compiler audit.

## 2. Occupied support and dyadic packing

Let U_floor(cR) be the occupied edges at the prescribed cutoff. Applying
(1) at b=c+1 and using the fixed moments shows that BOTH ordinary and
omega-weighted relative occupied support are at most

    D0 (c+2)^3/log r + delta_r(c),
    D0=2^33 K_mu exp(32).                               (3)

The larger weighted coefficient is used for both inequalities.

For traces T<=R, their omega-weight is at least R, so their packing
contribution R*count/W_r is at most27D0/log r+delta_r(c).
For 1<=j<=J=ceil(log_2 c), set b_j=min(2^j,c), and count traces

    2^(j-1)R<T<=b_j R.

Each has more than2^(j-1)R edges. These edges lie in U_floor(b_j R),
and b_j<=c stays within the proved cutoff range even for the last band.
Thus its normalized packing contribution is at most

    2^(1-j)[D0(b_j+2)^3/log r+delta_r(c)].

Since b_j+2<=3*2^j, the main contribution is at most54D0*4^j/log r.
For c>1, sum_(j=1)^J4^j<16c^2/3; the errors have total coefficient<2.
For c=1 there are no upper bands. Therefore, for every allowed c,

    R P_floor(cR)/W_r
      <=2^9 D0(1+c^2)/log r+3delta_r(c).                 (4)

No trace is discarded and no independence or stationary resampling is
used in this step. Floors are harmless because the lifetimes are integers.

## 3. Literal compiler, including errors

Set H=floor(cR)+1. The inherited literal compiler gives

    nu(2r+1)<=W_r+2H Cat_r
                   +2(5H-1)P_(H-1)(r)+2L_r(r-H).

The relative cycle-opening charge is at most(c+1)/R. The multiplier
of R P/W_r is at most10(c+2)<=30c. In particular, (4) has principal
compiled charge at most2^15 D0 c^3/log r. Its error is at most
90c delta_r(c), bounded by

    exp((A0+65)(c+2)^2) r^(-1/400),

because90c<=exp((c+2)^2) for c>=1. The previously proved sharp exterior
bound at this exact aperture is48(1+c^2)exp(-c^2). Thus

    nu(2r+1)/W_r <=1+(c+1)/R
       +2^15 D0 c^3/log r
       +exp((A0+65)(c+2)^2)r^(-1/400)
       +48(1+c^2)exp(-c^2).                            (5)

This finite inequality retains the large coefficient in the exceptional
error; it has not yet been hidden in an unspecified asymptotic threshold.

## 4. A numerical threshold that absorbs the old error

Let y=loglog r and require y>=2^22-1. Write B=A0+65. Then

    B<exp(2^21), (c+2)^2<=9y.

For y>=2^22-1 one has log(7200y)<=y/4. At the left endpoint this
follows from log7200<16, log y<22 and38<y/4; afterwards the difference
increases because1/y<1/4. Moreover2^21+y/4<y. Consequently

    7200By<=exp(y),
    exp(B(c+2)^2)r^(-1/400)<=r^(-1/800).                (6)

Both r^(-1/800) and (c+1)/R are at most exp(-y) on this range.
For the former use exp(y)>=800y. For the latter use
2sqrt(y) exp(-exp(y)/2)<=exp(-y). These follow already from the
quadratic or cubic Taylor lower bounds for exp(y) at this threshold.
The condition also implies r>=r0 and every earlier aperture restriction.

## 5. Balance and convert both parities

Choose

    c^2=y-.5log y.

Then1<=c<=sqrt(y), c^3<=y^(3/2), and

    (1+c^2)exp(-c^2)<=2y^(3/2)exp(-y).

Using (5)-(6), the odd-dimensional coefficient is at most

    2^15D0+98 <=2^16D0.

For k=2r+1 or2r+2, the trimmed one-coordinate lift doubles both the
word length and the width in the even case. Also k<=4r for r>=1,
and for r>=4,

    (loglog r)^(3/2)/log r
         <=2(loglog k)^(3/2)/log k.

Take the explicit all-dimension threshold

    k_star=ceil(exp(exp(2^22))).

Then r>=k/4 implies loglog r>=loglog k-1>=2^22-1. The resulting
coefficient in both parities is at most

    2^17D0 =2^150 exp(2^18+96).

Its logarithm is less than2^18+246<400000*(2/3). Using log2>2/3,
we may advertise the simpler numerical coefficient

    C=2^400000.                                         (7)

Accordingly, with the certified upstream estimate (1), the explicit result is

    nu(k)<=W(k)[1+2^400000 (loglog k)^(3/2)/log k]

for every k>=ceil(exp(exp(4194304))). All logarithms are natural.
The same expression bounds (nu(k)-B(k))/W(k) from above because the
established endpoint lower bound is B(k)<=nu(k) and B(k)>=W(k).

These deliberately conservative constants remain useless for k17. This
is an internally audited deduction on the same finite PBBS inputs,
not external/formal verification or a proof of nu(k)=B(k).
