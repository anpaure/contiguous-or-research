# A polylogarithmic raw-incidence bound for Gaussian-short PBBS lifetimes

Date: 2026-09-07. Pure proof; no computation or original-project edits.
The worktree lead and independent recency reader fully audited this note.
The coordinator then completed a full read and a separate independent
full audit; all passed. The fixed-c raw-incidence theorem (1) is accepted.
The worktree lead supplied the adaptive branching improvement; this note
records the quantitative proof. The complete marked-fringe profile proof
is retained as a verified independent route alongside the coordinator's
exact all-depth pruning census. No master document was edited.

Follow-up, 2026-09-08: the coordinator has accepted the stronger
mu_H=O_c(1) and P(T<=H)=O_c(r^(-1/2)) theorem. Its envelope proof is
/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md,
Sections 1-8; the independent coarse-profile proof is
pbbs_bounded_gaussian_short_incidence.md in this directory. The complete
original proof below is retained, particularly its finite adaptive
path comparison. Its stated lack of an O(1) conclusion describes this
older estimate by itself, not the current accepted theorem.

For every fixed c>0, with H=floor(c sqrt(r)),

    mu_H=E_D[(T(D)+2)1{T(D)<=H}] <= C_c(log r)^2          (1)

for sufficiently large r. D is uniform among ORIGINAL Dyck roots of
semilength r. Subscript-c constants may depend on c; other constants
below are absolute and may change between displays.

Extra branches in the clock genealogy increase later query counts and
incur extra zero-slot costs. Keeping these costs removes the larger
exp[O_c((log log r)^2)] bound obtained from the fixed triangle alone.
Equation (1) does not prove bounded raw incidence, a vanishing occupied
union, a target-repair bound, or a packing theorem. No growing-c
uniformity is asserted.

## 1. Uniform marked-fringe generating functions

Let r_s=|partial^s D|_up. An original nonroot tree vertex contributes to
r_s exactly when its fringe subtree has height at least s. Fix s>=1 and
put A_s(x)=C_(s-1)(x), the GF of trees of height at most s-1. Let F_s
mark ALL vertices with fringe height at least s, including the root;
let G_s mark only nonroot such vertices. Ordered root children give

    G_s=1/(1-xF_s),       F_s=uG_s+(1-u)A_s,

so G_s counts r_s exactly and

    xuG_s^2-[1-x(1-u)A_s]G_s+1=0.                     (2)

There are absolute gamma,C_0>0 such that

    A_s(1/4)=2s/(s+1),
    1<=A_s(x)<=3,       0<=A_s'(x)<=C_0(s+1),
    0<=x<=x_+=(1/4)[1+gamma/(s+1)^2].                 (3)

Here is a positive-factor justification of the derivative bound. Write
A_s=sum_(a=0)^(s-1) Z_a, where Z_0=1 and

    Z_a=x^a/[P_a P_(a+1)],
    Z_a(1/4)=2/[(a+1)(a+2)]             for a>=1,
    P_m(x)=product_(k=1)^floor(m/2)
                [1-4x cos^2(pi k/(m+1))].

Here P_m denotes the Fibonacci polynomial, separately from the marked
series F_s in (2).

Put delta=4x_+-1. For m<=s, a normalized inverse factor at x_+ is
[1-delta cot^2(pi k/(m+1))]^(-1). The inequalities

    delta cot^2(pi k/(m+1))<=C gamma/k^2,
    sum_k cot^2(pi k/(m+1))<=C(m+1)^2

follow from sin(pi k/(m+1))>=2k/(m+1). Choose gamma small. The product
of these changes is bounded uniformly, and xZ_a'/Z_a at x_+ is at most
C(a+1)^2. Thus Z_a(x_+)<=C/(a+1)^2 and Z_a'(x_+)<=C. Sum over a;
positivity extends the derivative bound to smaller x. The critical
value and a further reduction of gamma give A_s<=3.

There are absolute C_1,c_1>0 such that, for |theta|<=c_1/(s+1), the
positive combinatorial series is finite at

    u=e^theta,
    x_theta=(1/4)exp[-theta/(s+1)-C_1 theta^2],

and

    G_s(x_theta,e^theta)<=4.                           (4)

We prove this without assuming a radius of convergence. Put
a=1/(s+1), z=4x_theta, A=A_s(x_theta), b=1-x_theta(1-u)A. Its
discriminant is

    Dscr=b^2-4x_theta u
      =1-z+(z/2)(A-2)(u-1)+(z^2/16)A^2(u-1)^2.

For C_1 fixed and c_1 small, x_theta is in (3), b>=1/2, and

    |A-(2-2a)|<=C_0(s+1)|z-1|/4,
    |z-1|<=2[a|theta|+C_1 theta^2].

The logarithm of (1-a)+a e^theta has second derivative at most 1/4.
Consequently

    1-z[1+a(u-1)]>=1-exp[-(C_1-1/8)theta^2].

This is at least a fixed multiple of C_1 theta^2 if C_1 is large and
c_1 small. The remaining possibly negative error in Dscr is at most
C(1+C_1 c_1)theta^2; its final squared term is nonnegative. Choosing
C_1 first large and c_1 afterward small gives Dscr>=0, with equality
allowed at theta=0. The same choices also give

    1-x_theta(1+u)A>=a/2.                              (5)

Indeed its value at theta=0 is a, and its perturbation is bounded by
C(c_1+C_1 c_1^2)a using (3).

The smaller root G_star=2/(b+sqrt(Dscr)) is at most four and is at least
A. For the latter statement, the polynomial in (2), evaluated at A,
is 1-A+x_theta A^2>0 by the bounded-height recurrence, while (5) puts
A to the left of its vertex. Set F_star=uG_star+(1-u)A. Then F_star>=A,
it is a fixed point of u/(1-xF)+(1-u)A, and x_theta F_star<1.

Now truncate trees by total height. Starting with F^(s-1)=A, their
successive evaluations satisfy

    F^(d)=u/[1-x_theta F^(d-1)]+(1-u)A,       d>=s.

They increase as positive combinatorial sums and are bounded by F_star,
because this map is increasing below 1/x_theta. Monotone convergence
therefore proves finiteness and G_s<=G_star, including u<1. This proves
(4) without a radius assumption.

Positive coefficient evaluation and Cat_r>=c4^r r^(-3/2) imply

    E exp(theta[r_s-r/(s+1)])
       <=C r^(3/2)exp(C_1 r theta^2).                 (6)

Chernoff at theta=+/-eps/[2C_1(s+1)] gives, for an absolute eps_0>0
and 0<eps<=eps_0,

    Pr(|r_s-r/(s+1)|>eps r/(s+1))
       <=C r^(3/2)exp[-c eps^2r/(s+1)^2].             (7)

## 2. Growing good profiles

For large r put L=floor(sqrt(r)/(log r)^2), eps=1/log r. A profile is
good when

    (1-eps)r/(s+1)<=r_s<=(1+eps)r/(s+1),
                          0<=s<=L+1.                 (8)

The s=0 condition is automatic. Union bounding (7) gives

    Pr(bad)<=C L r^(3/2)exp[-c eps^2r/(L+2)^2]
            <=C r^2 exp[-c'(log r)^2].                (9)

Thus (H+2)Pr(bad)=o(1), even uniformly for H<r. This is an absolute
incidence-mass estimate, without normalization by mu_H.

At a good profile set, for 0<=s<L,

    ell_s=r_s-2r_(s+1)+r_(s+2),       p_s=2r_(s+1)+1,
    q_s=ell_s/(p_s+ell_s)=ell_s/[r_s+r_(s+2)+1],
    N_s=s+1.                                          (10)

The ell_s are nonnegative but need not individually approximate their
formal means; near L they are often small integers. We use weighted
sums instead.

## 3. Deterministic weighted profile bounds

Define

    Phi=sum_(s=0)^(L-1) N_s q_s,
    A_t=sum_(s=t+1)^(L-1)(s-t)q_s,
    B_L=sum_(t=0)^(L-1)(t+1)q_t exp(-2A_t).

Uniformly on (8),

    Phi>=log L-C,       B_L<=C.                        (11)

Here are the summation details. Put d_L=r_L-r_(L+1). Convexity and
(8), with m=floor(L/2), give

    d_L<=[r_m-r_L]/(L-m)<=Cr/L^2,       r_L<=Cr/L.     (12)

Put D=1+eps+(L+1)/(2r). Since r_s+r_(s+2)+1<=2rD/(s+1),

    Phi>=(2rD)^(-1)sum_(s=0)^(L-1)(s+1)^2ell_s,

    sum_(s=0)^(L-1)(s+1)^2ell_s
       =r+2sum_(j=1)^(L-1)r_j-(2L-1)r_L-L^2d_L.

The last expression is at least 2(1-eps)r log L-Cr. Since
eps log L=O(1) and (L/r)log L=o(1), the first bound in (11) follows.

For A_t use the sharper upper denominator bound

    r_s+r_(s+2)+1<=2rD(s+2)/[(s+1)(s+3)].

Put g_s=(s-t)[(s+2)-1/(s+2)], s>=t. Then

    A_t>=(2rD)^(-1)sum_(s=t+1)^(L-1)g_s ell_s.

Its first summation coefficient g_(t+1) is at least two, and its
interior second differences are

    g_s-2g_(s-1)+g_(s-2)
       =2+2(t+2)/[s(s+1)(s+2)]>=2.

For t<=L-2 the final boundary terms are exactly

    -[g_(L-1)-g_(L-2)]r_L-g_(L-1)d_L.

They are O(r) uniformly in t, using (12), g_(L-1)=O(L^2), and
g_(L-1)-g_(L-2)=O(L). Therefore

    A_t>=alpha log[L/(t+1)]-C,       alpha=(1-eps)/D.  (13)

The empty case t=L-1 satisfies this too. For large r, a=2alpha is
in [1,2]. Since q_t<=C(t+1)ell_t/r, (13) gives

    B_L<=[C/(rL^a)]sum_(t=0)^(L-1)(t+1)^(a+2)ell_t.

The second differences of (t+1)^(a+2) are at most C(t+1)^a,
uniformly for a in [1,2]. Summation by parts has nonpositive final
boundary terms. Dropping them and using (8) gives

    sum_(t=0)^(L-1)(t+1)^(a+2)ell_t
       <=Cr+Cr sum_(j=1)^(L-1)(j+1)^(a-1)
       <=CrL^a.

This proves B_L<=C.

## 4. The exact cost of an adaptive branching path

Conditional on the FULL original profile, the arrays Z_s are independent
uniform weak compositions of ell_s into p_s parts. Their chronological
queries are original slots 0,-1,-2,... . Let W_s be the sum of the n_s
queried coordinates. The accepted clock recurrence is

    n_s=N_s+2sum_(t<s)(s-t)W_t,
    m_L=1+2sum_(s<L)W_s.                               (14)

Thus n_s depends only on EARLIER original rows. No reached root is
sampled afresh.

For a uniform composition of ell into p parts, the sum of n distinct
specified coordinates has exact law

    P(w;n)=binom(w+n-1,w)
           binom(ell-w+p-n-1,p-n-1)/binom(ell+p-1,p-1).

Put P0(n)=P(0;n), q=ell/(p+ell). If n>=N, then

    P0(n)/P0(N)
      =product_(j=N)^(n-1)(p-1-j)/(ell+p-1-j)
      <=exp[-(n-N)q].                                 (15)

If 0<=w<=ell and p>=2(n+w), the exact relative mass is

    P(w;n)/P0(n)
      =binom(n+w-1,w)(ell)_w/(ell+p-n-1)_w
      <=[2(n+w)q]^w/w!,                               (16)

with falling factorials. Impossible values have probability zero;
zero exponents and empty products have their usual value one.

On any nonnegative path with sum W_s<=K, (14) implies
n_s<= (2K+1)N_s and n_s+W_s<=3(K+1)N_s. Assuming
p_s>=2(n_s+W_s) on every such path, multiply (15)-(16) to obtain

    Pr(path | profile)
      <=Q0 product_(t=0)^(L-1)
        [6(K+1)N_t q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0=product_(s=0)^(L-1)P0_s(N_s).                  (17)

The accumulated exponential penalty follows from the exact identity

    sum_s(n_s-N_s)q_s=2sum_t W_t A_t.

Also Q0<=exp(-Phi)<=C/L. Summing (17) over all paths by the multinomial
theorem and using (11) gives

    Pr(sum_(s<L)W_s<=K | profile)
      <=Q0 sum_(k=0)^K [6(K+1)B_L]^k/k!
      <=(C/L)exp[C(K+1)].                             (18)

This uses exact within-row composition laws, not independence of the
coordinates in a row. The row process can be defined abstractly by
(14); on a short physical clock satisfying the circumference conditions,
it is precisely the actual genealogy.

## 5. Apply the bound to actual short lifetimes

On (8), p_s>=c_0 sqrt(r)(log r)^2 for all s<L, with absolute c_0>0.
For the fixed Gaussian constant c and large r,
all these circumferences exceed G=2H+1. The physical clock construction
therefore applies through depth L on T<=H.

Consider h>=2L. Every depth-L T leaf has physical length at least
2(h-L)+1, so disjointness and (14) imply

    sum_(s<L)W_s
      <={G/[2(h-L)+1]-1}/2
      <=H/[2(h-L)]<=H/h.

Take K=ceil(H/h). On the relevant event h<=H, K>=1, and for h>=2L
it is O_c((log r)^2). Every path of total at most K consequently has
n_s+W_s<=C_c sqrt(r), whereas p_s>=c_0 sqrt(r)(log r)^2. Thus all row
hypotheses in (16)-(18) hold. Uniformly on these FULL profiles,

    Pr(T<=H | profile)
       <=(C/L)exp[C(1+H/h)],
                 for good profiles with h>=2L.         (19)

Height is measurable from the full profile. Dropping the good-profile
indicator after (19) therefore makes no independence assumption.

## 6. Inverse-height integration

The accepted uniform exact-height coefficient bound is

    [x^r]Z_h(x)<=C4^r(h+2)^(-4)
                         exp[-r/(2(h+2)^2)].          (20)

Retaining its prefactor gives a small-height tail without a power of r.
For h<=m, split its exponential into two equal halves. One half is at
most exp[-r/(4(m+2)^2)]. The remaining complete height sum satisfies

    sum_(h>=1)(h+2)^(-4)exp[-r/(4(h+2)^2)]
       <=Cr^(-3/2),

by its integral bound or a dyadic split at sqrt(r). Division by
Cat_r>=c4^r r^(-3/2) gives

    Pr(h<=m)<=Cexp[-r/(4(m+2)^2)].                     (21)

Thus X=sqrt(r)/(h+2) has a uniform sub-Gaussian upper tail, and

    E exp(tX)<=Cexp(Ct^2),       t>=0.                  (22)

This follows directly by integrating
1+t integral_0^infinity exp(tx)Pr(X>x)dx.

Bad profiles contribute o(1) to mu_H by (9). Roots with h<2L contribute
at most

    (H+2)Cexp[-r/(4(2L+2)^2)]=o(1)                    (23)

by (21). On the other profiles, (19) bounds the raw incidence by

    [C(H+2)/L] E exp[C(1+H/h)].

For h>=2L and large r, H/h<=2cX. Extend the expectation to all heights
after this bound, and apply (22) at the fixed parameter 2Cc. The last
display is at most C_c H/L<=C_c(log r)^2. Together with (9) and (23),
this proves (1).

## 7. Scope and inputs

Profile concentration concerns original uniform Dyck roots. The
branching calculation conditions on their full profile and uses
independent ROWS of original arrays, with exact within-row laws.
Reached clocks enter only through the accepted deterministic partition.

The occupied fraction is still mu_H E_inc[1/K_overlap]. Its vanishing
requires another overlap estimate; no such estimate is asserted here.

Source inputs: pbbs_gaussian_clock_genealogy_structural_audit.md,
Sections 1-5, for profile fibres, persistent slot order and clocks;
pbbs_growing_budget_uniform_bound.md, equation (18), for (20). The
marked-fringe Chernoff estimate, weighted profile bounds and adaptive
path summation are proved above.
