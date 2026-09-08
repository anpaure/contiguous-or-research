# User-supplied selective-truncation coefficient 1.177987

2026-09-08. This records the substantive proof supplied in the latest
user message for independent audit. The contribution and claimed bound
are the USER'S. Geometry, padding, literal compilation, analytic energy
and all-dimension passage: independent audits PASS. Root independently
reproduced the mask and rational numerical certificate on h100 and read
the complete geometric audit. The displayed labels “Full proof”, “Exact
runnable verifier”, and “Complete proof-and-verifier package” in that
message did not contain a usable path or URL in the received text.
No supplied external verifier has been read or run.

Audited theorem: nu(k)<=(1.177987+o(1))W(k), improving c9=1.180703803847...
at all ranks and every sufficiently large dimension.

## 1. Simultaneous threshold-mask certificate

Keep A.7's fourteen rows on eight axes. In each selected shore
E=(e1,e2,e3,e4), delete that row's masks empty, {e1}, {e1,e2}.

    row I    J    selected
     1 0461 5723 0461
     2 0473 2651 2651
     3 0674 3152 unchanged
     4 0726 1435 1435
     5 1507 4263 unchanged
     6 1605 7432 1605
     7 2104 6375 2104
     8 2150 7463 7463
     9 3206 7154 3206
    10 3210 4567 4567
    11 3617 5204 3617
    12 4302 6157 4302
    13 5034 6721 5034
    14 5426 7301 7301

Every row covers unions of a prefix of I and a prefix of J. The user
reports that all256 masks remain covered after the36 deletions, total
multiplicity314 rather than350, and minimum retained multiplicity1.

## 2. Equal lengths, absorbed children, and selective truncation

Each four-axis staircase on length-2s axes has R=s^3 chains and total
memberships V=5s^4. Its chain indexed by j2,j3,j4 in{0,...,s-1} has
length L=8s-3-2(j2+j3+j4). The terminal segment having at least three
high coordinates has T(j4)=3s-1-2j4 members: s with four highs and
2s-1-2j4 immediately before them with three highs.

Absorb a ninth chain of length1<=r<=2s into the selected shore. For a
staircase chain E0<...<E_(L-1), its rectangle-SCD child q=0,...,r-1 is

    (E0,q),...,(E_(L-1-q),q),
                  (E_(L-1-q),q+1),...,(E_(L-1-q),r-1).

It is eligible when its four-axis projection ends with at most two high
coordinates, hence every projected member has at most two. This is
equivalent to q>=T(j4). Thus

    R_elig=s^2 sum_(j=0)^(s-1)[r-(3s-1-2j)]_+
          =s^2 floor([r-s]_+^2/4).

For eligible children ONLY, truncate the all-low prefix from every
chain on the opposite shore. Every deleted point has at most two highs
on the selected shore and none on the opposite shore, so its mask is
one of that selected row's three deleted masks. The simultaneous mask
certificate supplies another retained row covering the same point,
including its ninth-chain coordinate. Other rows retain all points of
their masks except similarly designated deletable masks.

The opposite staircase has exactly s^4 all-low members. Each eligible
child therefore saves s^4 in rectangle side-length charge. Across the
twelve selected rows the finite principal charge is at most

    P_new<=140 r s^7 -12 s^6 floor([r-s]_+^2/4).          (A)

## 3. Literal compiler and padding

A.7's local compiler for indexed left/right chain families, chain counts
R,S and total memberships V,Z, has nonzero word length at most

    SV+RZ+2RS+Z+S.                                      (B)

It covers the product and its physical full complement, with closing
bridges included. Compile the ineligible children against the full
opposite family, and eligible children against its truncated family.
The principal charge drops by exactly R_elig s^4. Splitting a row into
two only changes the constant in degree-seven overhead; principal
charge is degree eight.

For unequal actual lengths r<=a1<=...<=a8, set

    A=2 ceil(a8/2), s=A/2, D=sum_(i=1)^8(A-ai),
    alpha=35/32.

Pad axes to A and contract consecutive repetitions. At most D members
are lost from any formal staircase chain. If r-s-D>0, all actual axes
extend beyond threshold s, so the opposite staircase still has exactly
s^4 all-low members. The user claims the padding-stable bound

    P_new<=r alpha A^7
                 -12s^6 floor([r-s-D]_+^2/4).            (C)

If the correction is zero, use the old construction. Also retain its
line alternative r(a8+a7) product_(i=1)^6 ai, choosing the cheaper valid
construction. Normalize by ACTUAL volume r product_i ai. New and old
continuum costs obey0<=Psi<=Phi<=2/a1. With all eight larger lengths
equal a, the new cost is

    Psi(r,a,...,a)=[alpha-f(r/a)]/a,
    f(t)=3/256 *[2t-1]_+^2/t, f(0)=0.                    (D)

## 4. Energy identity and expected leading-order saving

Keep all A.7 deterministic product-SCD refinements. In its nine-slot
Gaussian mesh process, r_m is the smallest terminal radius and
Y1_m<=...<=Y8_m are the other eight; a_m=Y8_m. A.7 gives convergence
of the eight charged radii to a common A>0 and

    A^(-2) has law S9=sum of9 independent unit-ball exit times

for standard three-dimensional Brownian motion started at zero. Its
reciprocal uniform integrability is retained. No convergence of r_m is
assumed.

Every Gaussian update has conditional squared-norm increment3/m and
zero expected cross term. After m updates,

    E[r_m^2+sum_(i=1)^8 Yi_m^2]=3.                        (E)

Positive moments are dominated by Brownian path suprema. For
M_p=E S9^(-p), define gamma=3-33M1/4 and X_m=r_m^2-a_m^2/4.
Then

    E X_m -> gamma, E a_m^5 -> M_(5/2).

For0<=t<=1,

    f(t)>=(1/48)[t^2-1/4]_+^2,

since for t>1/2,
(2t-1)^2/t=4(t^2-1/4)^2/[t(t+1/2)^2]
          >=(16/9)(t^2-1/4)^2.

Cauchy--Schwarz therefore yields

    E[f(r_m/a_m)/a_m]
      >=(1/48)E[(X_m)_+^2/a_m^5]
      >=[E X_m]_+^2/[48 E a_m^5].                        (F)

Continuity of the padding-stable cost and the old reciprocal domination
give E[Phi(Y_m)-Psi(r_m,Y_m)]
       =E[f(r_m/a_m)/a_m]+o(1).
On compacts bounded away from zero the comparison is uniform over the
possibly nonconvergent0<=r_m<=a_m. Off those compacts both costs are
bounded using A.7's second-smallest-radius estimates.

The claimed improved coefficient is

    C*=c9-sqrt(pi/8)*(3-33M1/4)^2/[48M_(5/2)].            (G)

## 5. Claimed exact numerical certificate

From E exp(-s tau)=sqrt(2s)/sinh(sqrt(2s)),

    M_p=2^(1-p)/Gamma(p) *integral_0^infinity
                            x^(2p+8)/sinh(x)^9 dx.

Writing J_q=integral x^q/sinh(x)^9 dx gives the positive series

    J_q=512 q! sum_(j=0)^infinity binom(j+8,8)/(2j+9)^(q+1),
    M1=J10, M_(5/2)=2J13/[3sqrt(2pi)].

The AM--GM tail bound from j=N onward is

    2^(8-q) q!/[8!(q-8)] * (N+7/2)^(-(q-8)).             (H)

The user reports1000 terms with upward rational rounding, plus this
tail and Machin-formula rational bounds on pi, certifying

    M1<0.348224, M_(5/2)<0.077681,
    sqrt(pi/8)>0.62665, c9<1.1807038039.

Thus gamma>0.127152 and

    C*<1.1807038039
         -0.62665*(0.127152)^2/[48*0.077681]
       =1.177986642788284...<1.177987.

## 6. All dimensions and reported verification

For each fixed initial-block count m, the finite modified compiler keeps
degree-seven overhead and degree-eight principal charge. All SCD children
remain. Use the same fixed-m then block-size-to-infinity limit, top-bit
splices, and finite candidate selection over m as A.7; no growing-m
uniform estimate is invoked. Claimed conclusion is limsup nu(k)/W(k)
<=C*<1.177987 for all sufficiently large dimensions and all ranks.

The user's reported verifier checks are:

* all256 masks after the twelve deletions;
* staircase and absorption counts for1<=s<=8, every r<=2s;
* padding eligible-child bound on128 unequal-length examples;
* all262144 points of the s=2,r=4 fine grid;
* exact rational coefficient enclosure.

The mask and exact numerical runs have now been independently reproduced
in this task. The stated sample staircase/padding/fine-grid runs were
not replayed; their general geometric claims were checked by proof.

## 7. Independent verification record

The complete geometry and padding audit is
`USER_SELECTIVE_TRUNCATION_GEOMETRY_PADDING_COMPILER_AUDIT_20260908.md`.
Direct-route and root passed its literal point coverage, exact eligible
count, contracted-chain bound, and degree-seven compiler overhead.
Appendix independently passed Sections4–6 above: nonanticipative Gaussian
energy, moment domination, the pointwise f bound, Cauchy--Schwarz,
continuity uniform in the shortest radius, Mellin constants, series tail,
and the fixed-block/all-dimension passage. Root checked the same scalar
identities and continuum normalization.

The independent small verifier executed ONLY on h100 at
`/home/amodo/selective-truncation-audit-20260908.VGqood/verify.py`.
The run completed successfully; its execution session35295 is terminal.
Its source was copied back without local execution as
`USER_SELECTIVE_TRUNCATION_EXACT_AUDIT_20260908.py`.
It checks the256 masks and the1000-term rational moment certificate;
it is not represented as the user's unavailable full verifier.

All arithmetic assertions used Fractions and integer upward rounding.
The output certified M1<0.348224, M_(5/2)<0.077681,
sqrt(pi/8)>0.62665, c9<1.1807038039 and gamma>0.127152. The final EXACT
rational upper bound was

    915071803984367/776810000000000 < 1.177987.

This is a valid independent explicit full-cube improvement credited to
the user. The separate PBBS coefficient-one proof does not use it.
