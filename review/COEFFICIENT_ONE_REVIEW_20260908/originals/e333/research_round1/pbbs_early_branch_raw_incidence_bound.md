# Early original-clock branches have negligible raw short incidence

2026-09-08. Pure proof; no computation. This is an actual raw-incidence
bound for one trajectory sector, using the accepted quantitative
original-clock path estimate. It does not bound the complementary
all-zero-prefix low-score sector.

The authoritative input is
`/Users/amir.nuriyev/Documents/problem/scratch/PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md`,
especially its deterministic estimates (6)-(12), full-profile path
bound, and inverse-height integration. Its exact composition-path
input is repeated in task05's
`pbbs_quantitative_clock_polylog_short_mass.md`, Sections 4-6.

## 1. Scales and the branch event

Fix c>0 and H=floor(c sqrt(r)). Use exactly the accepted parameters

    a=16 sqrt(r log(r+1)),   kappa=1/64,
    L=floor(kappa r/a).

For sufficiently large r, L>=2 and L is of order sqrt(r/log r).
GOOD is the original-profile event

    |r_s-r/(s+1)|<=a  for every s>=0.

The source gives Pr(BAD)<=2/(2r+2)^13. Fix an integer 1<=S<=L.
On GOOD, h>=2L, and T<=H, the actual original-clock genealogy through
depth L is valid: every relevant circumference exceeds the entire
short physical horizon, and the queried coordinates in each row are
distinct original slots 0,-1,-2,... . Write W_s for the sum queried
in row s. Define the early-branch event by

    E_S={some W_s>0 for 0<=s<S}.                       (1)

Here “before S” means rows s<S, not row S. Any contribution outside
GOOD or with h<2L will be bounded in full, so it needs no genealogy
extension beyond its domain of validity.

The claimed raw bound is

    E[(T+2)1{T<=H and early branch before S}]
       <=C_c (H+2) S^2/L^3+O_c(r^(-10)),              (2)

where (1) specifies the event on the valid sector. The same bound
holds if every exceptional root is included in the event. This
convention makes (2) insensitive to any definition of the genealogy
on the excluded sector.

## 2. Truncating the deterministic row-weight bound

For 0<=s<L, use the source notation

    ell_s=r_s-2r_(s+1)+r_(s+2)>=0,
    q_s=ell_s/(r_s+r_(s+2)+1),
    A_t=sum_(t<s<L)(s-t)q_s,
    b_t=(t+1)q_t exp(-2A_t),
    B=sum_(t<L)b_t,       B_early=sum_(t<S)b_t.

Uniformly on GOOD, the accepted estimates give

    q_t<=C(t+2)ell_t/r,
    exp(-2A_t)<=C((t+1)/L)^2,
    B<=C.                                             (3)

The quartic summation-by-parts estimate truncates at every S<=L:

    sum_(t<S)(t+2)^4 ell_t<=C(rS^2+aS^3).              (4)

For S>=2, twice summing by parts leaves initial terms O(r), interior
coefficients bounded by C(s+2)^2, and terminal terms

    -[f_(S-1)-f_(S-2)]r_S-f_(S-1)(r_S-r_(S+1))<=0,
    f_t=(t+2)^4.

Insert r_s<=r/(s+1)+a in the interior sum to obtain (4). For S=1,
the direct bound 16ell_0<=16r suffices. The profile estimates needed
here are available through S+1<=L+1.

Combining (3)-(4) yields

    B_early
      <=C/(rL^2) sum_(t<S)(t+2)^4 ell_t
      <=C(S^2/L^2)(1+aS/r)
      <=C S^2/L^2,                                    (5)

because aS/r<=aL/r<=kappa. All constants in (3)-(5) are absolute.

## 3. Keeping the early-branch restriction in the exact path sum

Condition on the FULL original profile, with GOOD and h>=2L. On
T<=H, the exact leaf count implies sum_(s<L)W_s<=H/h. Set

    K=ceil(H/h),       theta=6(K+1).

The source's exact composition comparison is uniform over every
nonnegative path of total at most K:

    Pr(path | profile)
       <=Q0 product_(t<L) (theta b_t)^(W_t)/W_t!,
    Q0<=C/L.                                          (6)

Its hypotheses hold on every such summed path: n_s+W_s is O_c(sqrt(r)),
whereas the available p_s are bounded below by a constant times
sqrt(r log r). This includes paths not realized by a short lifetime;
enlarging to them is an upper bound. The original rows are independent
only after conditioning on the full profile, and the adaptive query
count in a row depends solely on earlier rows. No reached-root law
is substituted.

Retain the condition sum_(t<S)W_t>=1 while enlarging the remaining
sum to all nonnegative paths. Its product exponential sum is exactly

    exp(theta B)-exp(theta(B-B_early))
      =exp(theta B)(1-exp(-theta B_early))
      <=theta B_early exp(theta B).                   (7)

Using (5)-(7), and absorbing K+1 into an exponential with a changed
absolute constant, gives

    Pr(T<=H and E_S | profile)
       <=C S^2/L^3 exp(C'(K+1))                       (8)

on GOOD, h>=2L. This bound is uniform in 1<=S<=L and in all these
profiles. It does not assert independence of branching rows under
the short-lifetime conditioning.

## 4. Original-height integration and the raw rate

The accepted inverse-height estimate is

    X=sqrt(r)/(h+2),       E exp(tX)<=C exp(Ct^2),
    Pr(h<=m)<=C exp[-r/(4(m+2)^2)].                    (9)

On h>=2L, K+1<=H/h+2 and H/h<=2cX. Thus averaging (8) under the
original full-profile law costs only a constant depending on fixed c:

    Pr(T<=H, E_S, GOOD, h>=2L)<=C_c S^2/L^3.          (10)

Height is a function of the conditioned profile; no independence is
needed in this averaging. Multiplying by H+2 bounds the desired raw
length weight on this sector.

The exceptional contributions are smaller than r^(-10). Indeed,

    (H+2)Pr(BAD)=O_c(r^(-25/2)),
    (H+2)Pr(h<2L)
       <=C_c sqrt(r) exp[-r/(36L^2)].                 (11)

Since L<=kappa r/a,

    r/(36L^2)>= [256/(36kappa^2)] log(r+1),

and the fixed displayed coefficient is greater than 13. The second
term of (11) is therefore O_c(r^(-10)) as well. This proves (2).

Because L is of order sqrt(r/log r), (2) also reads

    raw early-branch incidence
       <=C_c S^2(log r)^(3/2)/r+O_c(r^(-10)).          (12)

Take

    S=floor(sqrt(r)/(log r)^(3/2)).

Then 1<=S<=L for all sufficiently large r, and (12) gives

    raw early-branch incidence
       =O_c((log r)^(-3/2))
       =o((log r)^(-1/2)).                            (13)

The raw quantity is normalized by W=(2r+1)Cat_r: the actual total
repair-edge incidence of this sector is W times (13).

## 5. The exact unshifted triangle characterization and scope

On the valid short genealogy, the row-count identity is

    n_s=s+1+2sum_(t<s)(s-t)W_t.

Before the first positive W_t, this gives n_s=s+1. Thus the first
positive row queries exactly original slots 0,-1,...,-s. Consequently

    E_S iff sum_(s=0)^(S-1) sum_(i=0)^s Z_(s,-i)>0.    (14)

One direction uses the first positive actual row. Conversely, the
actual query prefix always contains those s+1 slots, so positivity
of the fixed triangle forces a positive W_s. No shifted or newly
sampled arrays occur in (14).

Any residual low-score incidence also having an early branch is a
subfamily of the all-short early-branch incidences. Its raw mass is
therefore bounded by (13), at the packing-scale rate requested in the
conditional low-score reduction. This does not estimate the remaining
residual low-score incidences with every original triangle entry in
(14) equal to zero. No conclusion on that complementary sector, total
residual packing, or coefficient one is asserted.
