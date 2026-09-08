# New user claim: polynomial clock cost and inverse logarithm

Received 2026-09-08. This is a review transcription, not a certification.
The user supplies written arguments but the named downloadable package is
not available locally. All new mathematical execution must run on h100.

Claimed conclusion, on the same finite PBBS inputs:

    nu(k)/W(k) <= 1+C (loglog k)^(3/2)/log k.

## Finite geometric-clock theorem to audit

Let a_0,...,a_(d+1) be positive, decreasing, convex, a_0=r, and

    .99 r/(s+1) <= a_s <= 1.01 r/(s+1).
    ell_s=a_s-2a_(s+1)+a_(s+2),
    pi_s=2a_(s+1)/(a_s+a_(s+2)), q_s=1-pi_s.

Assume every prefix m<=d has

    Z_m=product_(s<m) pi_s^(s+1) <= C_Z/(m+1).

Row s uses independent geometric variables with Pr(Z=j)=pi_s q_s^j.
If W_s is its sum, the number queried is

    n_s=s+1+2 sum_(j<s) (s-j) W_j;
    V_d=sum_(s<d) W_s.

Claim: E z^V_d <= C/[1+d(1-z)] for 0<=z<=1, hence
Pr(V_d<=M)<=C(M+1)/(d+1). Zero ell_s is allowed.

### Exact backward recursion

Two clock types: C becomes C+2Z*T; T becomes C+(2Z+1)*T.
For terminal T weight t, x_d=1,y_d=t and

    x_s=x_(s+1) pi_s/[1-q_s y_(s+1)^2],
    y_s=y_(s+1) x_s.

The terminal T count is1+2V_d, so E z^V_d=y_0/t for z=t^2.
Set y_(d+1)=t and v_s=-log y_s. Then

    v_s-2v_(s+1)+v_(s+2)=g_s(v_(s+1)),
    g_s(v)=log[(1-q_s exp(-2v))/pi_s].

Each g_s is increasing and v_s>=v_(s+1).

### Linear comparison

Set U_d=U_(d+1)=1 and solve backward

    U_s+U_(s+2)=2 U_(s+1)/pi_s.

The actual profile solves this same linear equation. With
Delta_d=a_d-a_(d+1), the exact Wronskian formula is

    U_s/a_s=1/a_d-Delta_d sum_(j=s)^(d-1) 1/(a_j a_(j+1)).

Claim: U_s >= (d+1)/[5(s+1)]. For m=floor(d/2), delta=.01,
convexity gives Delta_d<=(a_m-a_d)/(d-m). Substituting the profile
bounds and sum_(j<d)(j+1)(j+2)=d(d+1)(d+2)/3 yields

    U_s/a_s >= (d+1)/r * [1/(1+delta)
                  -2(1+5delta)/(3(1-delta)^2)] >=(d+1)/(4r).

Let eta=t^-2-1 and w_s=.5 log(1+eta U_s). AM-GM gives

    pi_s sqrt[(1+eta U_s)(1+eta U_(s+2))]
           <= pi_s+eta U_(s+1).

Equivalently, backward second difference of w is at most g_s(w_(s+1)).
The terminal values and backward slopes of w,v agree; induct on both
value and slope, using monotonicity of g_s. Therefore

    y_s^2 <= 1/[1+(t^-2-1)U_s].

### Recovering 1/d

At t^2=1/2, unwind the recursion:

    E 2^-V_d = Z_d product_(s<d)
                        (1-q_s y_(s+1)^2)^(-(s+1)).

The comparison gives y_(s+1)^2<=5(s+2)/(d+1), while
q_s/pi_s=ell_s/(2a_(s+1)). The logarithm of the correction product is
at most

    5/[2(1-delta)r(d+1)]
          *sum_(s<d)(s+1)(s+2)^2 ell_s.

Convexity gives a_s-a_(s+1)<=3r/(s+1)^2; summation by parts gives
sum_(s<d)(s+2)^3 ell_s<=21r(d+1). Thus the correction is<54 and

    E 2^-V_d <= exp(54) C_Z/(d+1).

For z>=1/2, eta=(1-z)/z. If eta(d+1) is large, take
m=floor(eta(d+1)/10). Then y_m^2<=1/2. Restart at this prefix and
apply the preceding fixed-half estimate to get E z^V_d<=C/(m+1).
For bounded eta(d+1), use1; for z<=1/2, use monotonicity.
For M>=1, choose z=M/(M+1), use z^-M<=e. M0 is the zero path.

## Transfer to finite weak-composition rows

For a uniform weak composition of ell into P parts, the sum of n<=P-1
specified entries has exact probability

    binom(n+w-1,w) (ell)_w (P-1)_n /(N)_(n+w), N=ell+P-1,

where the factorials are falling. With pi=(P-1)/N and q=ell/N,
factor (N)_(n+w)=(N)_w (N-w)_n. Because w<=ell,

    (ell)_w/(N)_w<=q^w,
    (P-1)_n/(N-w)_n <=[(P-1)/(N-w)]^n.

So Pr_comp(W=w)<=Pr_geom(W=w)*(1-w/N)^(-n), which for w<=N/2
is at most the geometric probability times exp(2nw/N).
Zero rows cause zero comparison loss.

For a path of mass<=M, n_s<=(2M+1)(s+1),
N_s>=c0 r/(s+2), and the total likelihood ratio is bounded by

    exp[C M(M+1)(d+1)^2/r].

Use height h>=c_h sqrt(r)/Q and query depth
d=floor(kappa sqrt(r)/[(b+1)Q]), with M=ceil(H/h), H<=b sqrt(r).
Then M+1<=C(b+1)Q. Choose kappa small enough for all original-clock
circumference, finite-query and horizon hypotheses. The exponent is
absolute. The actual short event forces this low budget, hence

    Pr(T<=H | Pi)<=C(b+1)^2 Q^2/sqrt(r),
    mu_H(Pi)<=C(b+1)^3 Q^2.

When d<2 the probability bound dominates1 after increasing C. This is
global over profiles and uses no independent profile exception.

## Downstream argument

Keep established polynomial candidate scales and latest-start charging.
At fixed profile, average cutoffs ceil(cR)..floor((c+1)R), R=sqrt(r):

    u_floor(cR)(Pi)<=C mu_floor((c+1)R)(Pi)/log r+bar_e(Pi).

With omega=1+R/(h+2)<=C Q and Gaussian Q moments, both unweighted
and weighted occupied support are at most

    C(c+1)^3/log r + C r^-1/1000,

uniformly for1<=c<=sqrt(loglog r). The existing exponential factor
exp[C(c+2)^2] is only in the inverse-power error and is absorbed at a
sufficiently large absolute threshold.

For packing, use weighted support for T<=R. For dyadic bands
2^(j-1)R<T<=min(2^j R,cR), divide occupied support by2^(j-1)R.
Summation gives

    R P_floor(cR)(r)/W_r <= C(1+c^2)/log r + C r^-1/1000.

Insert into the literal compiler

    nu(2r+1)<=W_r+2H Cat_r+2(5H-1)P_(H-1)(r)+2L_r(r-H),
    H=floor(cR)+1, Cat_r=W_r/(2r+1).

Use the previously audited finite tail32(1+H²/r)exp[-H²/(r+1/2)].
This yields relative excess

    C[c^3/log r+(1+c²)exp(-c²)+r^-1/2000].

Set D=loglog r and c²=D-.5 log D. Both main terms are at most
C D^(3/2)/log r. The trimmed lift doubles length and W in even
dimensions. All finite PBBS dependencies retain their proposed-proof
status. The user did not give certified numerical C or threshold.
