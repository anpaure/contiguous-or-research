# Audit of the user's selective staircase truncation

2026-09-08. Direct-route independent pure-proof audit. No mathematical
execution. The construction and proposed numerical coefficient are the
USER'S contribution, recorded in
`USER_SELECTIVE_TRUNCATION_PROPOSED_1_177987_20260908.md`.

Verdict: the finite staircase geometry, ninth-coordinate coverage,
padding-stable saving, literal compiler overhead, and continuum
normalization PASS. Root separately verified the simultaneous 256-mask
certificate and rational numerical enclosure on h100. This note does not
claim to have rerun those checks or audit the Brownian moment argument.

## 1. Exact eligible-child geometry

Use the actual A.7 hook partition of a four-axis staircase on [2s]^4.
Its chain indexed by j_2,j_3,j_4 in {0,...,s-1} has length

    ell=8s-3-2(j_2+j_3+j_4)>=2s+3.

For the last hook, the previous three-axis chain has exactly s terminal
members with all three coordinates high. Its horizontal portion at
x_4=j_4 retains s-j_4 of those members. Its subsequent vertical portion
at x_4=j_4+1,...,s-1 adds s-j_4-1 three-high members, followed by s
four-high members. Thus the terminal segment with at least three highs
has EXACT length

    T(j_4)=3s-1-2j_4.                                  (1)

All preceding members have at most two highs.

For a ninth chain of length 1<=r<=2s, ell>=r. The rectangle SCD child
q=0,...,r-1 used by the user has four-axis projection
E_0,...,E_(ell-1-q), followed by repetitions of its final projection
while the ninth coordinate increases. It stays at at most two high
coordinates precisely when q>=T(j_4). Hence the exact eligible count is

    R_elig=s^2 sum_(j=0)^(s-1)[r-3s+1+2j]_+
           =s^2 floor([r-s]_+^2/4).                      (2)

For the last equality set h=s-1-j and x=r-s. The sum becomes
sum_(h>=0)[x-1-2h]_+; because x<=s the existing range contains every
positive term. Separating even and odd integer x gives floor(x^2/4).

Every four-axis hook chain begins with exactly s all-low members.
Inductively these are its first-coordinate values 0,...,s-1 with all
other initial hook indices below s; the horizontal part always retains
them. After the first high coordinate appears, it never disappears.
Thus truncating the all-low prefix from the opposite indexed chain
family removes exactly s^3*s=s^4 memberships. Every truncated chain
remains nonempty, since its endpoint has all four coordinates high.

## 2. Simultaneous coverage includes the ninth coordinate

In each of the twelve selected rows, absorb the ninth factor into the
SELECTED shore, swapping the shore names when necessary. Pair eligible
absorbed children with the opposite family after its all-low prefix is
removed; pair all other children with the full opposite family.

A removed point has at most two highs in the selected ordered shore,
and none in the opposite shore. Its COMPLETE eight-bit mask is therefore
one of empty, {e_1}, {e_1,e_2}. This does not remove every product point
whose selected-shore prefix has length at most two; it removes only
points also all-low on the opposite shore.

The verified simultaneous mask certificate leaves a retained occurrence
of every eight-bit mask. For such a retained occurrence, this row's
modification removes NO point having that mask, whatever the ninth
coordinate. Before modification its complete absorption SCD covers
every ninth-coordinate value. Therefore that retained occurrence still
covers the original full nine-dimensional point. This proves coverage
directly, without assigning the ninth coordinate to a second row or
assuming compatibility of different absorption-child labels.

## 3. Principal charge and literal overhead

Let the absorbed left family have memberships V and R chains, and let
the full opposite family have memberships Z and S=s^3 chains. Write
V=V_e+V_i and R=R_e+R_i for eligible and ineligible subfamilies. The
truncated opposite family still has S chains and memberships Z-s^4.
The sum of their two principal rectangle charges is exactly

    SV_i+R_i Z + SV_e+R_e(Z-s^4)
                            =SV+RZ-R_e s^4.             (3)

Before truncation the fourteen-row principal bound is 140rs^7.
Equations (2)-(3), for the twelve selected rows, give

    P_new<=140rs^7-12s^6 floor([r-s]_+^2/4).              (4)

The local A.24 compiler applies to indexed families of arbitrary strict
set chains on disjoint supports; it does not require their first members
to be empty or their increments to be singletons. Its charge is

    SV+RZ+2RS+Z+S.

Use it separately for the two groups above, omitting an empty group.
There are only constantly many groups. After absorption R=O(B^4),
S=O(B^3), Z=O(B^4), where B is one plus the sum of the nine input
lengths. Thus all endpoint and closing charges remain O(B^7), while
the principal charge has degree eight. Truncation and swapping shores
preserve strictness and disjoint physical supports. No seam, endpoint,
or ninth-coordinate charge of principal order is omitted.

## 4. Padding loses at most D eligible-child positions

Take actual lengths r<=a_1<=...<=a_8, A=2ceil(a_8/2)=2s, and
D=sum_i(A-a_i). If r-s-D<=0, retain the old construction and claim
zero correction. Suppose r-s-D>0. Then each deficit A-a_i is at most
D<r-s<=s, so every a_i>s.

Padding therefore preserves the threshold bit of every formal point:
min(x_i,a_i-1)>=s exactly when x_i>=s. All-low formal positions map
injectively to actual positions.

A formal hook chain is saturated in coordinate indices. An image step
can collapse only when an axis has already reached its last actual
position. Axis i causes at most A-a_i such collapsed steps, so removing
consecutive repetitions loses at most D members from any chain. Write
ell' for its strict image length and T' for the length of its terminal
segment with at least three high coordinates. Then

    ell'>=ell-D>=r-D,                 T'<=T(j_4).         (5)

For the actual rectangle E' x [r], use q=0,...,min(r,ell')-1.
This minimum is important when padding makes ell'<r. The same hook
formula partitions that rectangle for either relative length. At least

    [min(r,ell')-T']_+ >= [r-D-T(j_4)]_+                 (6)

children remain eligible. Summing (6) over the indexed formal chains
gives at least s^2 floor([r-s-D]_+^2/4) eligible children per selected
row. Different image chains remain an indexed family, as in A.7;
coincidence does not invalidate either counting or coverage.

Each opposite image chain still has its s distinct all-low initial
members and a nonempty nonlow remainder. Consequently its family's
removable membership remains EXACTLY s^4. Applying (3) gives the valid
padding-stable bound

    P_new<=r alpha A^7
             -12s^6 floor([r-s-D]_+^2/4),
    alpha=35/32.                                        (7)

Possible additional image contractions only lower the baseline charge.
The proof never normalizes by the padded volume.

## 5. Continuum formula and domination

For positive larger lengths a_1<=...<=a_8 set
D(a)=sum_i(a_8-a_i). After scaling away the integer rounding, the
staircase upper charge divided by the ACTUAL volume r product_i a_i is

    alpha a_8^7/product_i a_i
      -[3a_8^6/(64r product_i a_i)]
                        [r-a_8/2-D(a)]_+^2.              (8)

Choose its minimum with the old complete line alternative
1/a_8+1/a_7. The resulting Psi satisfies

    0<=Psi<=Phi<=2/a_1.

The correction in (8) is supported on r>a_8/2+D(a), so it vanishes
on a neighborhood of r=0. Defining it to be zero at r=0 gives a
continuous function on 0<=r<=a_1 with all a_i positive. It is homogeneous
of degree minus one.

When all eight larger lengths equal a, (8) reduces to

    [alpha-f(r/a)]/a,
    f(t)=3[2t-1]_+^2/(256t),     f(0)=0.                 (9)

The line alternative is 2/a and is strictly larger. On compact sets
with a bounded away from zero, the coalescing-larger-length limit is
uniform over the possibly nonconvergent 0<=r<=a_1. In particular the
claimed passage from the padded finite improvement to the continuum
improvement does not require a limiting law for the smallest factor.
Expectation convergence still uses A.7's previously established
reciprocal uniform integrability, as stated in the user's argument.

The finite and continuum geometry therefore support the user's analytic
saving calculation. Its numerical and Brownian evaluations are separate
audits; this note records the literal construction and padding proof.
