# Correlated selection of standard tube pairs need not realize a fractional cover

2026-09-08. Pure analysis; no mathematical computation or search.
Author: appendix_a. Root full analytical audit and direct-route
full independent audit passed.

This is a concrete fractional-gap cover of the complete binary three-cube.
It proves that selecting whole rectangles from the standard tube families
cannot in general realize fractional weights, even with arbitrary
correlations. It also gives a deterministic half-selection-plus-repair
barrier. It does not rule out nonstandard chain repartitions or establish
an obstruction for the particular charge-1248 quaternary certificate.

## 1. A genuine finite fractional gap

Use coordinates x,y,z in {0,1}. Define three actual chain-pair rectangles

    R_1 = {x>=y},    R_2 = {y>=z},    R_3 = {z>=x}.        (1)

For example, R_1 is the three-point chain
(x,y)=(0,0),(1,0),(1,1), paired with the full two-point z chain.
Each row has charge five and six targets. Each nonconstant binary
triple satisfies exactly two inequalities in (1), while 000 and 111
satisfy all three. Weight one-half on each row is therefore a
fractional cover of charge 15/2.

This is the unrestricted fractional optimum for binary three-axis
chain-pair covers. As in the q-ary compiler, first use nonempty
complementary coordinate supports. Put weight 5/4 on each of the six
nonconstant targets and zero on 000 and 111. Every proper split is one-by-two.
The possible shore lengths (a,b), with a<=2 and b<=3, and the
maximum number of nonconstant targets are

    (a,b):       (1,1) (1,2) (1,3) (2,1) (2,2) (2,3)
    maximum:       1     2     2     2     3     4.       (2)

Multiplying the second line by 5/4 never exceeds a+b. The only
entries needing an endpoint observation are b=3, whose binary
two-axis chain contains both 00 and 11, and (a,b)=(2,2), whose
two-axis chain contains at least one of those endpoints. Thus (2)
is a valid all-chain dual of total 15/2.

If empty coordinate shores are also allowed, the additional case is
a singleton on the empty support times a chain of length b<=4 in
the binary three-cube. Such a chain contains at most min(b,2)
nonconstant targets, since only ranks one and two are nonconstant.
Its dual weight is at most (5/4)min(b,2)<=1+b. Thus allowing empty
shores leaves this fractional optimum and all conclusions unchanged.
It also leaves the following integral volume bound unchanged: these
additional rows have at most four targets and charge at most five.

The integral optimum is eight. One row covers at most six points
and costs at most five. A total charge of at most seven can have
at most three nonempty rows; the two-row possibilities have volume
at most 6+1=7 or 4+2=6, while three rows of total charge at most
seven have volume at most 2+1+1=4. Hence they cannot cover eight
targets. Conversely keep R_1, of charge five, and repair its two
missing points 010,011 by the singleton (x,y)=(0,1) times the
two-point z chain, of charge three.

The accepted tube amplification therefore gives an explicit
integral cover of [2m]^3 of charge exactly 8m² for every m.

## 2. The standard inflated families force two entire templates

Apply the exact standard tube construction to (1). For R_1 its
two-axis staircase is partitioned into the m hooks

    H_j = {(x,j): 0<=x<=2m-1-j}
          union {(2m-1-j,y): j<y<=2m-1},
                                          0<=j<m.       (3)

The fine rectangles are H_j(x,y)×[2m]_z. On the staircase the
hook label of a point is

    j_1=min(y,2m-1-x).                                  (4)

The other two families are cyclic copies, with labels

    j_2=min(z,2m-1-y),    j_3=min(x,2m-1-z).             (5)

Let A_i be an ARBITRARY set of selected labels from template i.
There is no independence or common-color assumption. Consider the
macrocell with binary index 100: x is in [m,2m), while y,z are in
[0,m). Its only owners are R_1 and R_2. For any j,k in [m], the
fine point

    (x,y,z)=(2m-1-j,j,k)                                (6)

has labels j_1=j and j_2=k. Thus the two owner labels range over
the complete Cartesian product [m]×[m]. If both A_1 and A_2 are
proper subsets, choose j and k outside them; (6) is uncovered.
The cells 010 and 001 prove the same statement for the pairs
(A_2,A_3) and (A_3,A_1).

Consequently any complete cover formed solely by selecting these
standard fine rectangles must retain every lane of at least two
templates. Each hook has length 4m-1-2j, so one whole template has
charge

    sum_(j=0)^(m-1) (6m-1-2j)=5m².                     (7)

The selected-family optimum is therefore at least 10m². It equals
10m²: any two macro rectangles in (1) already cover the binary cube,
since two of the cyclic inequalities cannot both fail on binary
values. Their full tube supports consequently cover [2m]^3.

In particular the charge (15/2)m² suggested by the fractional
template cannot be approached by correlated whole-pair selection
from these tube families. Increasing m does not remove the gap.

## 3. Half selection followed by arbitrary additive repair still loses

Let m=2n and suppose exactly n labels are selected from each family.
The choices may be arbitrary and correlated, and their actual
principal charges need not equal half the full charge. Let

    B_i=[m] minus A_i,       |B_i|=n,

and let Q_i be the retained charge of family i.

Inside macrocell 100, the intersection of H_j with its (x,y)
square is a standard square-SCD hook of length 2m-1-2j.
The other owner label j_2 equals z throughout this cell. Hence
the uncovered points there include exactly the product of the
hooks indexed by B_1 and the ordered free-axis values B_2.
They contain an antichain of size

    W_1=sum_(j in B_1) min(n,2m-1-2j).                  (8)

For a direct proof, write x'=x-m. The retained square hooks have
rank intervals [j,2m-2-j], all centered at m-1. Replace the n
ordered values in B_2 by their indices 0,...,n-1. The common
middle level of x'+y+index(z) meets the j-th hook product in
min(n,2m-1-2j) points. The union of these level sets is an
antichain, because that rank function strictly increases under
every strict coordinatewise comparison.

Cyclically the cells 010 and 001 give W_2 and W_3 of the same
form. Every point of any one of these three macrocells is
incomparable with every point of another, because their high
coordinate positions differ. Their three hole antichains unite
to an antichain of size W_1+W_2+W_3.

Any new chain-pair rectangle of shore lengths a,b covers at most
min(a,b) points of an antichain and costs a+b>=2min(a,b).
Therefore ANY additive repair, allowing arbitrary new support
splits, strict chains, and overlaps, costs at least
2(W_1+W_2+W_3). The original selected rectangles are retained
and charged in this statement.

The actual retained charge satisfies

    Q_i=5m²-sum_(j in B_i)(6m-1-2j)
       =8n²+n+2 sum_(j in B_i)j.                       (9)

Thus

    Q_i+2W_i=8n²+n+sum_(j in B_i) g(j),
    g(j)=2j+2min(n,4n-1-2j).                           (10)

For 0<=j<n, g(j)=2j+2n<=4n-2. For n<=j<2n, either
g(j)=2j+2n>=4n or g(j)=8n-2-2j>=4n. Its n smallest values
are consequently at j=0,...,n-1. Equations (9)-(10) give the
exact finite bound

    Q_i+2W_i >= 8n²+n+n(n-1)+2n²=11n².

Summing over the three families proves

    retained charge + additive repair charge
                  >=33n²=(33/4)m² > 8m².              (11)

This conclusion requires neither random selection nor an assumed
charge of (15/2)m² before repair. Even the cheapest deterministic
half-lane choices followed by arbitrary additive repair cannot
match the known integral charge-8m² construction.

## 4. What this settles and what it leaves open

The failure is a concrete compatibility constraint in doubly
covered macro cells: the two relevant lane labels are independent
coordinates in the sense of the surjectivity (6). Marginal lane
fractions do not enforce coverage, and no correlation between the
three selected label sets changes that Cartesian-product obstacle.

This disproves a general assertion that rational fractional chain-
pair templates can be realized, or realized with lower-order
additive repair, merely by selecting their standard inflated pairs
at the prescribed proportions. It is separate from the archived
independent-rounding calculation in
INDEPENDENT_FRACTIONAL_TUBE_ROUNDING_20260907.md.

It does not prove that the denominator-15 quaternary certificate
has the same obstruction. Nor does it exclude changing the actual
chain partitions, reconnecting retained and discarded pieces,
introducing different templates while replacing the selected ones,
or using useful slack in a particular larger fractional cover.
No general fractional-to-integral realization theorem and no new
full-cube coefficient are established here.
