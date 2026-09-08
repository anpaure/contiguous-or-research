# Square-root-logarithmic Gaussian-short PBBS incidence

2026-09-07. Root pure proof, independently derived by a root helper.
The complete written proof passes an independent root audit. No computation.
This strengthens the accepted
O_c((log r)^2) short-clock bound; it does not prove shared repair or
coefficient one.

## 1. Statement and precise inputs

Let D be uniform among Dyck words of semilength r. Let T(D) be the
accepted PBBS newborn lifetime INCLUDING its consuming update. Write h
for the Dyck height, n=2r+1 and W=n Cat_r. For fixed c>0 set
H=floor(c sqrt(r)) and

    mu_H=E_D[(T+2) 1_{T<=H}].

Then

    mu_H=O_c(sqrt(log(r+1))).                         (1)

Thus the RAW total length of these repair traces is at most
O_c(W sqrt(log r)). This is not a bound of o(W) on that raw total.

Inputs are the exact all-depth pruning census in
PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md and the original-clock
identities, exact composition path bound and inverse-height tail in
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_quantitative_clock_polylog_short_mass.md,
Sections4-6. The deterministic estimates that change the cutoff are
proved here; the probabilistic inputs are repeated explicitly below.

## 2. An absolute-error profile event

Let r_s be the size after s rounds of peak pruning. The exact census,
with iid cyclic fair bits before conditioning to0D, gives

    E_iid N_s=n/(s+1) sum_{j=0}^s cos^(n-1)(pi j/(s+1)),
    N_s(0D)=2r_s+1.

Its Gaussian upper bound and a decreasing-function integral give,
UNIFORMLY in every s>=0,

    0<=E_iid N_s-n/(s+1)
       <=[2n/(s+1)] sum_{j>=1} exp(-a_s j^2)
       <=sqrt(2/pi) n/sqrt(n-1)<=2sqrt(n),
    a_s=(n-1)pi^2/[2(s+1)^2].                         (2)

The s=0 case is immediate. The depth-uniform two-edit concentration,
union bound through r+1 depths, and Dyck conditioning in that note give

    Pr_D(exists1<=s<=r+1:
         |N_s-E_iid N_s|>sqrt(32n log(n+1)))
       <=2/(n+1)^13.                                 (3)

For all sufficiently large r put

    a=16sqrt(r log(r+1)),   kappa=1/64,
    L=floor(kappa r/a).

Equations (2)-(3), and |[n/(s+1)-1]/2-r/(s+1)|<=1/2,
show that outside the event in (3),

    |r_s-r/(s+1)|<=a       for EVERY s>=0.             (4)

For s>r the Dyck core is empty, so that part is automatic.
Call (4) GOOD. BAD contributes at most

    (H+2)Pr(BAD)<=2(H+2)/(n+1)^13=o(1)                (5)

to mu_H. There is no division by an unknown incidence normalizer.

## 3. Deterministic summation with absolute errors

The following estimates hold whenever a>=1, L>=2,
aL/r<=kappa, and the nonnegative decreasing convex sequence r_s
satisfies (4) through L+1, with r_0=r. All constants below are absolute.
Put

    ell_s=r_s-2r_{s+1}+r_{s+2}>=0,
    p_s=2r_{s+1}+1,
    q_s=ell_s/(p_s+ell_s)=ell_s/(r_s+r_{s+2}+1),
    N_s=s+1,                       0<=s<L.

For large r, a(L+2)/r<=1/8; hence throughout this range
r_s is comparable to r/(s+1). Set

    b_s=r/(s+1)+r/(s+3),
    beta_s=1/b_s=[s+2-1/(s+2)]/(2r).

The actual denominator differs from b_s by at most3a. Since
b_s>=2r/(s+2), both denominators are comparable, and

    |q_s-beta_s ell_s|
       <=C a(s+2)^2 ell_s/r^2,
    q_s<=C(s+2)ell_s/r.                               (6)

Let d_L=r_L-r_{L+1}. Convexity with m=floor(L/2) gives

    r_L<=r/(L+1)+a,
    0<=d_L<=[r_m-r_L]/(L-m)
             <=C(r/L^2+a/L).                         (7)

For j=3,4, twice summing by parts gives

    sum_{s<L}(s+2)^3 ell_s<=C(rL+aL^2),
    sum_{s<L}(s+2)^4 ell_s<=C(rL^2+aL^3).             (8)

Here the initial coefficients contribute O(r), interior coefficients
are nonnegative and at most C(s+2)^(j-2), and the two terminal terms
are nonpositive: -[f_{L-1}-f_{L-2}]r_L-f_{L-1}d_L for increasing
f_s=(s+2)^j. Use r_s<=r/(s+1)+a in the interior sum. This proves
(8) without approximating the individual integer ell_s.

Define

    Phi=sum_{s<L}(s+1)q_s,
    A_t=sum_{t<s<L}(s-t)q_s,
    B_L=sum_{t<L}(t+1)q_t exp(-2A_t).

We claim

    Phi>=log L-C,
    A_t>=log[L/(t+1)]-C,        0<=t<L,
    B_L<=C.                                           (9)

For Phi, the beta_s baseline dominates (s+1)^2/(2r), and

    sum_{s<L}(s+1)^2ell_s
       =r+2sum_{j=1}^{L-1}r_j-(2L-1)r_L-L^2d_L
       >=2r log L-C(r+aL).

Its reciprocal-denominator correction, by (6) and the cubic moment
in (8), is at most

    C(a/r^2)(rL+aL^2)
       =C[aL/r+(aL/r)^2]=O(1).                       (10)

This proves the first part of (9). In particular no fixed relative
error is multiplied by log L.

For A_t let

    g_s=(s-t)[s+2-1/(s+2)],     s>=t.

Its first nonzero summation coefficient g_{t+1} is at least2, and its
interior second differences are

    g_s-2g_{s-1}+g_{s-2}
       =2+2(t+2)/[s(s+1)(s+2)]>=2.

For t<=L-2, summation by parts therefore bounds its baseline below by

    [1/(2r)] sum_{s=t+1}^{L-1}g_s ell_s
       >=sum_{j=t+1}^{L-1}1/(j+1)-C(1+aL/r)
       >=log[L/(t+1)]-C.

The two terminal terms are
-[g_{L-1}-g_{L-2}]r_L-g_{L-1}d_L= -O(r+aL),
using (7). The accumulated absolute profile errors cost at most O(aL),
and the reciprocal-denominator correction is again bounded by (10).
The empty case t=L-1 is immediate. This proves the second part of (9).
Finally (6), the second part of (9), and the quartic moment give

    B_L<=C/(rL^2) sum_{t<L}(t+2)^4ell_t
         <=C(1+aL/r)<=C,

proving the last part.

## 4. Transfer through the exact original clock

Conditional on the FULL pruning profile, the original arrays Z_s are
independent uniform weak compositions of ell_s into p_s parts. The
clock queries original slots0,-1,-2,... in each row. If W_s is their
sum, the exact original-row recurrence is

    n_s=s+1+2sum_{t<s}(s-t)W_t,
    m_L=1+2sum_{s<L}W_s.                              (11)

The row query count depends only on EARLIER rows. For a specified
nonnegative path with sum W_s<=K, the exact weak-composition formula
and p_s>=2(n_s+W_s) imply

    Pr(path | profile)
       <=Q0 product_{t<L}
          [6(K+1)(t+1)q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0<=exp(-Phi).                                    (12)

These are the finite inequalities (15)-(17) in the accepted clock
note; they include the future zero-query penalty. Summing all paths,
using the multinomial theorem and (9), gives

    Pr(sum_{s<L}W_s<=K | profile)
       <=C/L exp[C(K+1)].                            (13)

On GOOD, p_s>=c_0 r/L=Theta(sqrt(r log r)) uniformly for s<L.
For a short physical lifetime T<=H these circumferences exceed
2H+1 for sufficiently large r, with c fixed, so (11) applies to the
actual physical genealogy through depth L.

When h>=2L, disjoint physical depth-L leaves each have length at
least2(h-L)+1. Their count in (11) consequently implies

    sum_{s<L}W_s<=H/h.

Take K=ceil(H/h). On paths with total at most K,

    n_s+W_s<=3(K+1)(s+1)
             <=(3/2)H+6L=O_c(sqrt r).

Thus p_s>=2(n_s+W_s) holds uniformly, validating (12) for every
summed path. Equations (12)-(13) prove

    Pr(T<=H | profile)
       <=C/L exp[C(1+H/h)]            on GOOD,h>=2L.  (14)

No adaptively reached profile is resampled.

## 5. Height integration and conclusion

The accepted exact-height coefficient estimate supplies

    Pr(h<=m)<=C exp[-r/(4(m+2)^2)],
    E exp(tX)<=C exp(Ct^2),
    X=sqrt r/(h+2),                 t>=0.             (15)

The coefficient estimate retains its h^(-4) prefactor before summing;
there is no missing polynomial-in-r loss in (15).
For L>=2,

    r/[4(2L+2)^2]>=r/(36L^2)
       >=16^2 log(r+1)/(36 kappa^2).

Therefore (H+2)Pr(h<2L)=o(1). On GOOD,h>=2L, multiply (14) by
H+2 and average over the full original profile. Since
H/h<=2cX, (15) at a fixed parameter depending only on c gives

    mu_H<=o(1)+C_c(H+2)/L
          =O_c(sqrt(log(r+1))),

as asserted. Height is profile-measurable, so this averaging makes
no false independence assumption.

## 6. What is still missing

The occupied-edge fraction is mu_H E_inc[1/K_overlap]. Estimate (1)
controls its first factor but does not prove sufficient overlap. In
particular O_c(1), o(1), and a vanishing occupied fraction are NOT
consequences of this note. Positive-budget residual packing and the
full-cube coefficient-one construction remain open.
