# Shrinking-window PBBS rate with the sharp exterior: complete independent audit

2026-09-08. Pure proof and local source reads. No mathematical computation
was performed by this audit.

This independently verifies the user's stronger rate argument: remove the
cutoff shift from the conditional clock exponential, average over a window
of width R/c, retain profilewise clipping, and use the user's sharper
finite exterior estimate. The resulting explicit conclusions are

    nu(k)/W(k)
       <=1+2^76 (loglog k)^(3/2+2^-1048577)
                         (log k)^(-2^-1048577),                  (1)

and

    nu(k)/W(k)<=1+(log k)^(-2^-1048578),                         (2)

both for

    k>=k*=ceil(exp(exp(2^1048616))).

All logarithms are natural. These are construction bounds with internally
audited proofs, not exact equality nu(k)=B(k) or external certification.

## 1. Exact retained inputs and numerical constants

Use the actual all-birth PBBS trace family, with lifetime T, trace length
T+2, R=sqrt(r), and W_r=binom(2r+1,r). The full original profile Pi
and its height h and envelope Q are invariant on each physical component.
The numerical constants already proved are

    kappa=2^-24,   c_h=2^-25,
    D_*=2^12 exp(2^19),
    J=2^38 exp(2^19),
    A0=2^80 exp(2^20),
    A=2^2097152,
    r0=2^1000000.

In particular h>=c_h R/Q, Q>=1, and

    E[Q^v exp(uQ)]<=2^26(1+u)^3 exp(u^2),
                       1<=v<=2, u>=0.                          (3)

The complete proofs are in
PBBS_QUANTITATIVE_CUTOFF_UNIFORMITY_AND_EXPLICIT_CONSTANTS_INDEPENDENT_AUDIT_20260908.md
and PBBS_TERMINAL_PROFILE_CAPPING_AND_SHARP_MGF_INDEPENDENT_AUDIT_20260908.md.
The latter's terminal charging and profilewise clipping were independently
checked in PBBS_TERMINAL_CHARGING_COMPILER_AND_DYADIC_RATE_INDEPENDENT_AUDIT_20260908.md.

The full sharp exterior proof, read and checked for this audit, is
SHARP_PRODUCT_SCD_EXTERIOR_BOUND_INDEPENDENT_AUDIT_20260908.md.
That improvement is the user's estimate of the existing literal
product-SCD construction, not a newly substituted tail word.

## 2. Remove the cutoff shift before averaging the profile

For H<=bR, b>=1, choose the existing legal depth

    d=floor(kappa R/((b+1)Q)).

On d>=2 the exact finite conditional clock estimate is

    Pr(T<=H | Pi)<=d^-1 exp[D_*(1+H/h)].

The floor and geometric height bound imply

    d^-1<=2^25(b+1)Q/R<=2^26 bQ/R,
    H/h<=bQ/c_h.

Consequently, with

    beta=D_*/c_h=2^37 exp(2^19)=J/2,

one has the global inequality

    Pr(T<=H | Pi)
       <=2^26 exp(D_*) bQ/R *exp(beta bQ).                      (4)

Indeed, if d<2, then
kappa R<2(b+1)Q<=4bQ, so the prefactor2^26 bQ/R already exceeds one.
The trivial probability bound therefore proves (4) on that sector too.

Multiplication by H+2<=(b+2)R<=3bR gives

    mu_H(Pi):=E[(T+2)1{T<=H} | Pi]
       <=2^28 exp(D_*) b^2 Q exp(beta bQ).                      (5)

The factor exp(D_*) has remained outside the Q-dependent exponential.
Replacing it by a shift b+1 inside that exponential would discard
the improvement being used here.

## 3. The shrinking cutoff interval, including all floors

For1<=c<=sqrt(loglog r), put

    b=c+1/c,
    t0=floor(cR),   H_*=floor(bR),
    Tset={t0,t0+1,...,H_*}.

The exact number of integers is

    |Tset|=floor(bR)-floor(cR)+1>=R/c.                           (6)

At each fixed profile, occupied sets are nested, so
u_t0(Pi)<=average_{t in Tset}u_t(Pi). No profile-dependent cutoff
is selected.

For a fixed birth of lifetime T, the strip0<=t-T<q occurs for at most
q+1 choices, where q=ceil(r^(49/100)). Hence

    average_t I_t^Pi(0<=t-T<q)
       <= c(q+1)mu_H*(Pi)/R
       <=3c r^(-1/100)mu_H*(Pi).                              (7)

At r>=r0 this is at most3mu_H*(Pi)/log r, uniformly in the stated c.
To see this without numerical evaluation, write x=log r. Then
c<=sqrt(log x)<=sqrt(x), and e^(x/100)>=x^(3/2) for x>=2^16:
its cubic Taylor term suffices since x^(3/2)>=2^24>6000000.
Here x>=1000000 log2>2^16.

The first-gap terminal bound is100/log r, including its K floor.
Thus after (7),128/log r is a valid profilewise main coefficient.
The previous finite clock/flux/collar argument needs only t<=H_* and
the explicitly charged strip, so including floor(cR) instead of
starting at ceil(cR) is valid. No positive lower bound on mu_t is used.

The new largest cutoff bR is no larger than (c+1)R. All old raw physical
error estimates therefore still apply, with the same safe horizons.
The strip may be removed from the error and charged through (7).
The unchanged weighted-error proof then gives

    E[omega ebar]<=exp((A0+64)(c+2)^2)r^(-1/400),               (8)

where omega=1+R/(h+2)<=2^26Q. Here ebar is the actual conditional
bad-incidence mass plus a bounded coupling defect, not an unbounded
profilewise Markov majorant.

## 4. Clip before averaging and keep the exact p-dependence

Terminal charging and edge-disjointness give

    R P_t0/W_r<=E_Pi[omega u_t0(Pi)].

Use u<=1 at each profile and min(1,z)<=z^p for0<p<=1.
With (3), (5), and the coefficient128 from section3, the main packing
term is at most

    2^52 (2^35 exp(D_*))^p b^(2p)(1+beta p b)^3
                 exp(beta^2 p^2 b^2)/(log r)^p.                (9)

Together with (8), this is an explicit finite bound uniform in p,c,r
on the stated domain. Since b^2<=c^2+3 and b<=2c, it implies the
claimed form

    C c^(2p+3) exp(Ap^2 c^2)/(log r)^p
             +exp((A0+64)(c+2)^2)r^(-1/400).

For the uniform-in-p statement, C is an absolute finite constant.
There is no need to incur its potentially very large crude value in
the fixed-p numerical corollary below: retain (9) until p is chosen.

## 5. Fixed p=1/sqrt(A): a modest explicit main prefactor

Now set

    p=1/sqrt(A)=2^-1048576.

The previously proved comparison A>=2A0, together with beta=J/2 and
A0=16J^2, implies beta p<=1 and D_*p<=1. Also35p<=1.
Therefore

    (2^35 exp(D_*))^p<=2e<8,
    (1+beta p b)^3<=8b^3,
    b^(2p+3)<=32c^(2p+3),
    exp(3beta^2p^2)<=e^3<32.

Using b^2<=c^2+3 in (9) gives the packing main bound

    2^68 c^(2p+3)exp(Ap^2 c^2)/(log r)^p.                     (10)

This does not contain exp(3A), and the original exp(D_*) has been
raised to p before it is bounded. Since Ap^2=1, the remaining
quadratic exponent in (10) is just c^2.

## 6. Exact compiler and the user's sharp exterior

For H=floor(cR)+1 the literal compiler is

    nu(2r+1)
      <=W_r+2H Cat_r+2(5H-1)P_(H-1)+2L_r(r-H).

The cycle term is at most(c+1)/R. Its packing multiplier is at most
10(c+2)<=32c, for c>=1. The main term in (10) consequently becomes

    2^73 c^(2p+4)exp(c^2-p loglog r).                          (11)

The error multiplier is absorbed by10(c+2)<=exp((c+2)^2), so its
exponent is at most A0+65<A.

The sharper finite exterior theorem proves

    2L_r(r-H)/W_r
      <=32(1+H^2/r)exp[-H^2/(r+1/2)],   1<=H<=r.

At the ACTUAL aperture H=floor(cR)+1 it proves, uniformly for
r>=16 and c^2<=loglog r,

    2L_r(r-H)/W_r<=48(1+c^2)exp(-c^2).                         (12)

In particular there is no lost rank or changed tail aperture.
Its proof accounts for the positive floor-plus-one shift directly:
the polynomial loss is at most21/16 and the exponential loss at most8/7.
Their product is3/2, taking32 to48.

Combining these estimates yields the explicit finite inequality

    nu(2r+1)/W_r
      <=1+(c+1)/R
           +2^73 c^(2p+4)exp(c^2-p y)
           +exp(A(c+2)^2)r^(-1/400)
           +48(1+c^2)exp(-c^2),         y=loglog r.              (13)

This is the same complete all-rank compiler. Concatenating its tail
requires no further seam letters.

## 7. The logarithmic balance

For a general p, balancing the leading repair and sharp-tail exponents
gives p/(1+Ap^2), maximized at p=1/sqrt(A). Keep this p and set

    c^2=(p/2)y-((p+1)/2)log y,
    alpha=(p+3)/2.

Whenever this choice is admissible, the main term in (13) is bounded by

    2^73 y^alpha exp(-py/2).                                  (14)

Indeed c^2<=py/2 and
c^(2p+4)=(c^2)^(p+2)<=y^(p+2), while
exp(c^2-py)=exp(-py/2)y^(-(p+1)/2).

The exterior satisfies the same power balance. When py>=2,
1+c^2<=1+py/2<=py<=y, so (12) gives

    48 y^alpha exp(-py/2).                                    (15)

Thus the logarithmic correction is precisely the one that balances
the two polynomial factors. The exponent is p/2=1/(2sqrt(A)), and
the log-log power is alpha=3/2+p/2.

## 8. Explicit domain and error absorption at the stated threshold

Let

    k*=ceil(exp(exp(2^1048616))).

For k>=k*, put 2r+1=k when k is odd and 2r+1=k-1 otherwise.
Then r>=sqrt(k) and

    y=loglog r>=2^1048616-log2>=y0=2^39 sqrt(A),
    py>=2^39.

At y0, log y0=(1048576+39)log2<2^21.
The function(log y)/y is decreasing here. It follows for all y>=y0 that

    (p+1)log y<=py/2.

Consequently py/4<=c^2<=py/2, so c>=1 and c<=sqrt(y).
All of (13)'s finite domain and compiler inequalities are satisfied.

Also c+2<=3c, giving

    A(c+2)^2<= (9/2)sqrt(A)y<=y^2.

For y>=4000, the cubic exponential term gives
y^2<=(3/2000)exp(y). Therefore the weighted error in (13) is at most

    exp(-exp(y)/1000)=r^(-1/1000).                             (16)

This absorption is deliberately made at the new A-dependent threshold,
not at r0.

Both (16) and the cycle term are at most
y^alpha exp(-py/2) here. For (16), use exp(y)/1000>=y>=py/2.
For the cycle term, use R=exp(exp(y)/2)>=exp(2y) and
c+1<=2sqrt(y). The remaining elementary exponential comparison holds
already for y>=16.

Adding (14), (15), and these two errors gives

    nu(2r+1)/W_r
       <=1+2^74 y^alpha exp(-py/2).                            (17)

The conservative replacement of48 by256 would give the same2^74.

## 9. Both parities and the two stated corollaries

The trimmed lift from2r+1 to2r+2 doubles length and middle width exactly.
Writing Y=loglog k, one has y<=Y and
y>=Y-log2. Hence (17) implies

    nu(k)/W(k)
      <=1+2^75 Y^alpha exp(-pY/2)
      <=1+2^76 Y^alpha exp(-pY/2).                            (18)

Since p/2=2^-1048577 and alpha=3/2+2^-1048577, this proves (1).

For the pure-power consequence use the last, deliberately larger,
constant in (18). At

    Y*=2^40 sqrt(A)=2^1048616

one has pY*=2^40 and log Y*<2^21. Thus

    log(2^76)+alpha log Y*
       <=76+2log Y*<2^23<pY*/4.

The ratio (76+2log Y)/Y decreases throughout Y>=Y*. The same comparison
therefore holds for every larger k. Applying it in (18) proves

    2^76 Y^alpha exp(-pY/2)<=exp(-pY/4).

As p/4=2^-1048578, this is exactly the C=1 statement (2), at the
same threshold. No further parity factor is being suppressed: it was
already included in (18).

## 10. Scope and credit

The shift-free clock estimate, shrinking aperture, and logarithmic
balance audit the user's new argument. The sharp exterior bound and
its constant48 are the user's stronger estimate, with the separate
full finite proof linked above. No unavailable package or numerical
simulation is a premise.

The actual finite PBBS and product-SCD word construction is retained.
One may still enumerate its finite admissible apertures and retain
the shortest word; the theoretical rate does not require an algorithm
to evaluate these enormous constants or thresholds first.

The new theorem improves the quantitative asymptotic construction
bound. It supplies no new exact value for nu(17), no automatic embedding
of the recency gadget into the current finite bank, and no proof that
the gap above B(k) vanishes identically.
