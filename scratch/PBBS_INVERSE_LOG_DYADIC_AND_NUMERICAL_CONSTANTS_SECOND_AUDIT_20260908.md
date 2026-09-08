# Independent audit of inverse-log dyadic packing and explicit numbers

Date: 2026-09-08. Auditor: exact_b_finite_frontier.

Verdict: the complete downstream derivation in
`PBBS_INVERSE_LOG_DYADIC_COMPILER_AND_EXPLICIT_NUMBERS_20260908.md` passes.
Its previously pending polynomial clock input is now established by the
linked finite-row and physical-clock proof, giving

    mu_H(Pi)<=K_mu(b+1)^3Q^2,
    H<=b sqrt(r), b>=1,
    K_mu=2^100 exp(2^18+64).                              (A)

The complete input proof is
`PBBS_INVERSE_LOG_ORIGINAL_COMPOSITION_TRANSFER_INDEPENDENT_AUDIT_20260908.md`,
using the finite geometric theorem in
`GEOMETRIC_CLOCK_FINITE_PGF_AND_PREFIX_RESTART_INDEPENDENT_AUDIT_20260908.md`.
Its actual stronger coefficient is 2^74 exp(2^18+55), which is smaller than
the deliberately conservative K_mu in (A). The transfer uses kappa=2^-40,
an entire feasible-path likelihood debit below e, verified finite row and
physical-clock guards, and the trivial probability bound on d<2. The root
has independently read and passed that proof; this auditor has also read
its full parameter and constant derivation. Thus no pending numerical
condition remains in the downstream conclusion. All inherited finite PBBS
structural inputs and their internal-review scope remain as linked below.

The original user claim is transcribed in
`USER_PBBS_INVERSE_LOG_CLOCK_CLAIM_20260908.md`. The supplied downloadable
verifier package is not available locally, and none was assumed or replayed.
This audit uses pure symbolic proof and source reads only, with no mathematical
program execution.

## 1. Retained dependencies and conditional occupied support

The preceding independently audited terminal-charging argument supplies
latest-start assignment within each invariant physical profile, cutoff
averaging, and the weight

    omega=1+sqrt(r)/(h+2)<=2^26 Q.

Its profilewise errors are actual conditional bad-incidence masses and a
bounded coupling defect. Their weighted expectation is bounded by

    delta_r(c)=exp((A0+64)(c+2)^2)r^(-1/400),
    A0=2^80 exp(2^20),

on r>=2^1000000 and 1<=c<=sqrt(loglog r). In particular no conditional
Markov majorant is substituted for the actual mass when multiplying by
omega. The preceding source is
`PBBS_TERMINAL_PROFILE_CAPPING_AND_SHARP_MGF_INDEPENDENT_AUDIT_20260908.md`,
Sections 1-5. The finite exterior estimate is in
`SHARP_PRODUCT_SCD_EXTERIOR_BOUND_INDEPENDENT_AUDIT_20260908.md`.

The earlier first-gap constant is 100/log r. Keeping 128/log r, with the
additional boundary strip as in the root note, is conservative. On applying
(A) at b=c+1, the inequalities E Q^2,E Q^3<=exp(32) therefore imply both
ordinary and omega-weighted occupied-support bounds

    D0(c+2)^3/log r+delta_r(c),
    D0=2^33 K_mu exp(32).                                (B)

The power two moment is used unweighted and the power three moment weighted;
128*2^26=2^33. Thus the root note's common D0 indeed dominates both.
This uses the original profile distribution, with its incidence bias still
present in mu_H(Pi), and does not introduce a new random-root assertion.

## 2. Exact dyadic accounting, including the last partial band

Put R=sqrt(r). A packed trace with T<=R has at least R total omega-weight,
since it has T+2>=h+2 distinct edges, each with weight
1+R/(h+2). Its contribution to R P/W_r is therefore at most weighted
occupied support at c=1, namely 27D0/log r+delta_r(c).

For c>1 let J=ceil(log_2 c) and b_j=min(2^j,c). The remaining disjoint
bands are

    2^(j-1)R<T<=b_jR,  1<=j<=J.

Each such trace has more than 2^(j-1)R edges. Its occupied set is contained
in the all-short family at integer cutoff floor(b_jR), so (B) applies.
The last cutoff never exceeds c: this explicitly avoids any unproved
extension of the allowed aperture beyond sqrt(loglog r).

The j-th contribution is at most

    2^(1-j)[D0(b_j+2)^3/log r+delta_r(c)].

Here b_j+2<=3*2^j is valid for every j>=1, giving main coefficient
54D0*4^j. Also 2^J<2c, including when c is a power of two, and hence

    sum_(j=1)^J4^j < 16c^2/3,
    sum_(j=1)^J2^(1-j)<2.

The total main coefficient is at most (27+288c^2)D0, which is bounded
by 2^9D0(1+c^2). The errors sum to at most 3delta_r(c). When c=1 the
upper bands are empty, and the same inequality remains valid. Thus

    R P_floor(cR)/W_r
       <=2^9D0(1+c^2)/log r+3delta_r(c).                 (C)

Only disjoint-edge counting and occupied-set inclusion are used here.
No stationarity, independence, or loss of an uncharged trace is required.

## 3. Literal compilation and all numerical factors

Use the inherited literal compiler at H=floor(cR)+1. Its opening term
satisfies 2H/(2r+1)<=(c+1)/R. Its packing multiplier is

    2(5H-1)/R<=10(c+2)<=30c.

Since 1+c^2<=2c^2 for c>=1, multiplying the main term of (C) gives at
most 30*2^10D0 c^3/log r<2^15D0 c^3/log r. The error is at most
90c delta_r(c). The inequality

    90c<=exp((c+2)^2), c>=1,

holds at c=1 and persists because the logarithmic difference has
derivative 2(c+2)-1/c>0. Consequently this error is bounded by

    exp(B(c+2)^2)r^(-1/400), B=A0+65.

The exact-aperture exterior term is at most 48(1+c^2)exp(-c^2), as
proved in the separately audited finite exterior note. These calculations
establish the root note's complete pre-absorption inequality (5), including
the still-visible large constant B in the exceptional error.

## 4. The proposed enormous threshold is sufficient

Let y=loglog r>=2^22-1. The elementary estimate

    B<exp(2^21)

follows from A0=2^80exp(2^20); its logarithm is less than 2^20+81,
well below 2^21. On 1<=c<=sqrt(y), (c+2)^2<=9y.

At y=2^22-1, log(7200y)<16+22=38<y/4. The difference
y/4-log(7200y) is increasing thereafter. Also 2^21+y/4<y on this
entire range. Therefore

    7200By<=exp(y),
    B(c+2)^2<=log r/800,

and the compiled exceptional term is at most r^(-1/800).
The inequalities exp(y)>=800y and
2sqrt(y)exp(-exp(y)/2)<=exp(-y) hold with enormous room at this
threshold and persist thereafter. They can alternatively be obtained
from the cubic Taylor lower bound for exp(y). Hence both r^(-1/800)
and the opening term (c+1)/R are at most exp(-y).

Now choose c^2=y-(log y)/2. It lies in [1,y], and

    c^3<=y^(3/2),
    (1+c^2)exp(-c^2)<=2y^(3/2)exp(-y).

The exterior contributes at most 96y^(3/2)exp(-y), and the two
remaining terms contribute at most 2y^(3/2)exp(-y). Thus the total
odd-dimensional coefficient is at most 2^15D0+98<=2^16D0, exactly
as claimed in the root note.

## 5. Both parities and the advertised integer-power constant

For k=2r+1 the preceding result applies directly. For k=2r+2 the
established trimmed one-coordinate lift doubles the word length and
the width, preserving the normalized bound. Since k<=4r, for r>=4
one has log k<=2log r and loglog r<=loglog k. Therefore

    (loglog r)^(3/2)/log r
       <=2(loglog k)^(3/2)/log k.

If k>=ceil(exp(exp(2^22))), then r>=k/4 gives
loglog r>=loglog k-1>=2^22-1; all preceding restrictions hold.
The final coefficient becomes

    2^17D0=2^150exp(2^18+96).

Its logarithm is less than 2^18+246. This is less than
400000*(2/3), which is less than 400000log 2. Thus it is strictly
smaller than 2^400000.

With (A) now established by the linked finite proof, the advertised
all-dimension statement follows with no unspecified numerical constants:

    nu(k)<=W(k)[1+2^400000(loglog k)^(3/2)/log k],
    k>=ceil(exp(exp(4194304))).

The same upper expression controls (nu(k)-B(k))/W(k), using the already
established B(k)>=W(k). Nothing here asserts an equality nu(k)=B(k),
an effective small-dimensional improvement, or external formal verification.
No correction to the root downstream note was required.
