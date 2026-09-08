# Height-adaptive PBBS words: finite construction, period, and range count

2026-09-08. Independent pure-proof audit of the user's height-adaptive
construction. No mathematical program was run for this proof.

For n=2r+1, r>=1, put W_r=binom(2r+1,r). The construction below proves

    nu(2r+1)
      <=W_r+floor((2^(2r+2)-3W_r)/(2r+1)),                    (1)

and the exact trimmed lift gives

    nu(2r+2)
      <=2W_r+2floor((2^(2r+2)-3W_r)/(2r+1)).                  (2)

In particular it gives

    nu(k)/W(k)<=1+sqrt(2pi/k)+O(1/k).                        (3)

This is a finite, deterministic all-rank word construction. It needs no
probabilistic cutoff, short-trace packing estimate, or unspecified
diagonal sequence. The inherited finite PBBS structural theorems are
identified explicitly below. This internal audit is not external or
formal certification and does not establish nu(k)=B(k).

## 1. Definitions and retained structural inputs

On the rank-r binary states of length n=2r+1, let f flip every bit except
the unique unmatched zero in the usual cyclic Dyck matching. Put g=f^2.
These are the actual PBBS maps. The g-cycles partition all W_r states.
For one such cycle write

    A_i=g^i A_0,  i modulo v,
    X_i=[n] minus A_i.

The normalized Dyck height h is invariant under f, f^-1, and g, with
1<=h<=r. The strict-height proof and interleaving are fully recorded in
PBBS_STRICT_HEIGHT_CORRIDOR_AND_INTERLEAVED_HEIGHT_INDEPENDENT_AUDIT_20260908.md,
which this audit read completely and independently checked.

Its precise corridor input is: for every nonempty S of rank r-q,
0<=q<=r-1, there is an actual oriented g-path

    B_0,...,B_q

with intersection S and height h>=q+1. For q=0 this is immediate.
The q>=1 proof refines the global-maximum corridor in
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Theorem21.2, by selecting
a global maximum preceded by a nonempty reverse-Dyck gap.

The other structural input is the height-gap theorem,
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Theorem16.1:
a consecutive same-label selection gap at height h is at least2h+1.
Its proof uses the finite equality-particle renormalization: a short
return contains a strictly shorter odd return in the peak-deleted word,
and peak deletion lowers height by one. A return at least the entire
circumference already satisfies the bound because h<=r.
The same source's section1 gives positive projected residence length
(gap+1)/2.

The all-rank application requires the STRICT corridor height q+1.
The weaker height q would not suffice for the lower interleaved witness
or for the2h-1 collar below.

## 2. Every g-cycle has length divisible by n

Index physical sites by Z/nZ, and index edge i between sites i and i+1.
For a binary state A, define

    J(A)=sum{i : bits at i,i+1 are equal} modulo n.

For r>=1 the unmatched zero u has local neighbors0,1: its normalized
word is0D, with D nonempty, beginning with1 and ending with0.
Thus the local three-bit pattern001 changes under f to100.
The equal edge at u-1 is removed and the equal edge at u is inserted.
Every other edge has both endpoints flipped and retains its equality
indicator. Consequently

    J(fA)=J(A)+1 modulo n,
    J(gA)=J(A)+2 modulo n.

If g^v A=A, then2v=0 modulo n. Since n is odd,

    n divides v; in particular v>=n.                         (4)

This uses labelled physical sites. No quotient by rotations is being
treated as the physical cycle.

The same argument ensures gA!=A when n>=3. Both A and gA are disjoint
from the rank-r state fA. Hence they are distinct r-subsets of the same
(r+1)-set, so they are Johnson neighbors. In particular

    X_i intersect X_(i+1)=fA_i.                              (5)

## 3. The height-dependent erosion is nonempty

Every positive coordinate run in the upper-owner cycle X has length
at least h+1. Indeed its consecutive omitted-label return has odd gap
2T+1 with T>=h, and the projected positive residence is T+1.
This includes the one-step shift between return time and residence.
An identically positive coordinate causes no difficulty.

Define the cyclic literal erosion word

    D_i=intersection_{j=0}^h X_(i+j).                         (6)

Each adjacent owner is a Johnson neighbor, so intersecting h+1 of
them loses at most h coordinates from the first owner. Thus

    |D_i|>=r+1-h>=1.

All emitted letters are nonempty.

The following identities are exact:

    X_i=union_{j=0}^h D_(i-j),                               (7)

    intersection_{j=0}^q X_(i+j)
       =union_{j=0}^{h-q} D_(i-j),       0<=q<=h,             (8)

    union_{j=0}^q X_(i+j)
       =union_{j=-h}^q D_(i+j),         q>=0.                (9)

For (7)–(8), check one coordinate. A finite positive run [a,b] of X
has length at least h+1; its positive D run is [a,b-h].
The right side of (8) is positive exactly for i in[a,b-q], which is
the left-side intersection condition. Identically positive or negative
coordinates satisfy the same identities. Circular runs are handled by
integer lifts. Equation (9) follows immediately by taking the union
of the intervals in (7).

## 4. Literal opening and complete target coverage

For this cycle emit one complete D period followed by its first2h-1
letters. This has exactly

    v+2h-1

letters and realizes every cyclic D interval of length at most2h.
Indeed 2h<=2r<n<=v, so these intervals are shorter than a period,
and the copied collar supplies every possible crossing occurrence.

All nonempty proper upper targets have the form S^c, where S is
nonempty of rank r-q,0<=q<=r-1. Choose its strict-height lower
corridor B_0,...,B_q. Their complementary upper owners have union
S^c. By (9) this target has a D witness of length

    h+q+1<=2h.

Thus it occurs in the emitted word for that component. This includes
the upper middle rank at q=0.

For any nonempty lower target S of rank r-q,0<=q<=r-1, use the same
corridor and define the interleaved lower states

    C_j=f^-1 g^j B_0,   0<=j<=q+1,
    Y_j=C_j^c.

They lie on one actual g-cycle of the SAME height h. By (5),
Y_j intersect Y_(j+1)=B_j, and hence

    intersection_{j=0}^{q+1}Y_j=S.

Since q+1<=h, identity (8) gives a D witness of length

    h-(q+1)+1=h-q,

between1 and h. This supplies every rank1 through r.

Concatenate the emitted words of all g-cycles in any fixed order.
Every selected witness stays inside its own emitted word.
The full target[n] is the union of the entire word, because all
singletons, or already all upper-middle targets, are represented.
The empty target is not required for nu. No extra joining letters
are needed.

The exact finite construction length is therefore

    W_r+sum_over_g_cycles (2h-1).                            (10)

## 5. Convert cycle charges to a pointwise height sum

The height is constant on each cycle, and its charge2h-1 is positive.
By (4),

    sum_cycles(2h-1)
      =sum_cycles sum_{A in cycle}(2h(A)-1)/v
      <=(1/n)sum_{|A|=r}(2h(A)-1).                         (11)

Using positivity here is legitimate because r>=1 and h>=1.
The exceptional r=0 dimension is handled separately by the one-letter
word on one coordinate.

## 6. Dyck height is bounded by the linear bridge range

For a rank-r binary word A, assign increment+1 to a one and-1 to a zero,
and write its linear partial sums S_0=0,...,S_n=-1. Let

    M(A)=max S_j,   m(A)=min S_j,   R(A)=M(A)-m(A).

Cut at the canonical cyclic Dyck start to obtain D0. A partial height
after that cut is either S_b-S_a without wrapping, or S_b-S_a-1
after wrapping. In either case it is at most R(A).
The maximum proper height of D0 is h(A). Consequently

    h(A)<=R(A).                                              (12)

This inequality holds for each labelled word; no averaging over
rotations or assertion of a uniform Dyck root is needed.

## 7. Exact reflection count for the total range

There are W_r=binom(n,r) bridges from0 to-1.
For a>=1, reflection after the first hit of+a gives a bijection to
paths ending at2a+1. Therefore

    #{A:M(A)>=a}=binom(n,r-a).

Similarly reflection after the first hit of-a gives endpoint1-2a,
so

    #{A:-m(A)>=a}=binom(n,r+1-a).

Binomials outside their usual range are zero. Summing these integer
tail counts gives

    sum_A M(A)=sum_{j=0}^{r-1}binom(n,j),
    sum_A[-m(A)]=sum_{j=0}^r binom(n,j).

Since n is odd, sum_{j=0}^r binom(n,j)=2^(n-1). Hence the exact identity is

    sum_{|A|=r}R(A)=2^n-W_r.                                (13)

Combining (11)–(13) proves

    sum_cycles(2h-1)
       <=[2(2^n-W_r)-W_r]/n
       =(2^(n+1)-3W_r)/n.

The left side is an integer, so taking its floor proves (1).
No rounding has been discarded in the finite statement.

## 8. Even dimensions and an all-dimension envelope

The already established trimmed one-coordinate lift maps a complete
nonzero word of length N on2r+1 coordinates to one of length2N on
2r+2 coordinates. Since W(2r+2)=2W_r, it proves (2).

Let n(k) be k for odd k and k-1 for even k. For k>=3, the slightly
weaker but convenient common formula is

    nu(k)<=W(k)+floor((2^(k+1)-3W(k))/n(k)).                    (14)

For even k this follows from2floor(x)<=floor(2x); (2) retains the
sharper original rounding. The small values nu(1)=1 and nu(2)=2 have
their direct one- and two-letter witnesses.

Stirling's central-binomial estimate gives

    2^k/W(k)=sqrt(pi k/2)(1+O(1/k)).

Substitution in (14), with n(k)=k+O(1), gives (3).
More precisely the displayed upper envelope is
1+sqrt(2pi/k)-3/k+O(k^(-3/2)); the floor only lowers it.

## 9. Monotonicity and the finite threshold certificates

For odd n=2r+1 define

    t_r=2^(2r+1)/W_r,
    e_r=(2t_r-3)/(2r+1).

The normalized excess in (1)–(2) is at most e_r in BOTH parities.
The exact width ratio gives

    t_(r+1)=t_r(2r+4)/(2r+3).

Writing n=2r+1, direct subtraction yields

    e_r-e_(r+1)
      =2[t_r(n+4)-3(n+2)]/[n(n+2)^2]>0.

For r=1 this follows from t_1=8/3; for every r>=2,
t_r>=t_2=16/5>3, which makes the numerator positive.
Thus e_r strictly decreases for every r>=1.

The independent exact-integer certificates in
K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md
give

    e_283>1/10,    e_284<1/10,
    e_31115>1/100, e_31116<1/100.

Together with monotonicity and the exact parity lift, this bound certifies

    nu(k)<1.1 W(k)   for every k>=569,
    nu(k)<1.01 W(k)  for every k>=62233.

These thresholds concern this proved envelope, not the first dimensions
at which the true unknown optimum satisfies those inequalities.

## 10. Fixed k17 construction and scope

The separately executed fixed h100 construction, recorded in
K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md,
has146 cycles and height sum519. Formula (10) therefore gives the
literal universal word

    24310+2*519-146=25202.

The same finite record supplies a24829-letter trimmed word with128
explicit holes and a24957-letter complete word obtained by appending
those targets. Its interval witnesses were independently rechecked.
Those finite improvements are additional certificate facts; they are
not premises of the general proof above.

The height-adaptive construction and strict-height improvement are
user-supplied. This note supplies the independent complete period,
erosion, collar, range-count, rounding, and asymptotic audit.
The result improves the quantitative all-rank upper bound and its
finite construction. It does not settle exact equality at k17 or
in all dimensions.
