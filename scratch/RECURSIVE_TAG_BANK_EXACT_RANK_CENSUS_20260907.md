# Exact rank census of the recursive all-forward tag bank

2026-09-07. Pure proof; no computation.
Root synthesis of the accepted antipodal-tag permutation and higher-tag
phase trade, with an independently derived census. This is a finite
packet theorem. No global placement or full-cube covering is asserted.

## 1. Data and the one imported finite lemma

Let d>=2 be a power of two and L>=2 an integer. Put

    t=2^d, h=(d+1)L, K=L+1, ell=h+d+1=(d+1)K.

Use the explicit permutation F_d of binary d-tags from
[the root tag-cycle proof](ANTIPODAL_TAG_CYCLES_INJECTIVE_SHADOWS_20260907.md).
That note proves: F changes one bit at each step, F^d(v)=bar(v), and
for every 0<=s<=d/2 the ternary pattern of (v,F^s(v)) determines v.
The ternary pattern records equal bits as0/1 and changed bits as*.
The case s=0 is the identity. Only this finite lemma is imported.

Partition a 2b-coordinate universe into disjoint C,G, ordered lists
D=(d_1,...,d_h), E=(e_1,...,e_h), and d tag pairs, with

    |C|=|G|=b-h-d=b-ell+1>=1.

For a binary tag v, T_v selects one coordinate from each pair. Define

    B_z=C union {d_(z+1),...,d_h} union {e_1,...,e_z}.

For every initial v, traverse the common body in increasing z, inserting
the j-th forward F tag event at body gap jL, j=1,...,d. The resulting
row has ell vertices and ell-1 singleton-exchange edges. Its endpoints
are B_0 union T_v and B_h union T_bar(v).

At global row position a=0,...,ell-1 its phase and body indices are

    i(a)=floor(a/K),    z(a)=a-i(a).

The row state is B_(z(a)) union T_(F^(i(a))(v)).
The j-th event has before/after indices jK-1,jK, both at body level jL.

## 2. The exact census

Count all intersections and unions of row endpoint pairs, together
with their coordinate complements. Let f_q be the number of distinct
targets at either signed rank b-q or b+q. Then

    f_0=R=2t(h+1),

and for every integer 1<=q<=dK/2,

    f_q=2t[ell-q-(d-q/K) 1_{K divides q}].             (1)

Proof. A q-edge endpoint pair begins at a, with 0<=a<ell-q. The
number of tag events it crosses is

    s=i(a+q)-i(a)<=ceil(q/K)<=d/2.

Each body coordinate and each tag bit changes at most once along a
row. Thus intersection/union ranks are b-q,b+q. As v varies, the
finite injectivity lemma supplies exactly t distinct tag results
at this fixed endpoint pair. Complementation gives a further t at
each signed rank: positive targets contain all of C and omit G,
while their complementary orientation contains G and omits C.

The body part recovers both endpoint indices z,z':

    B_z intersect B_z'=C union D_(>z') union E_(<=z),
    B_z union B_z'=C union D_(>z) union E_(<=z').

Therefore different starts can collide only when BOTH of their body
endpoints agree. A body level has two temporal representatives only
at an event, namely jK-1,jK. A repeated fixed-q body pair must
therefore be the before/before pair and the after/after pair at two
distinct events j<k. This occurs precisely when

    q=(k-j)K=sK.

For q=sK there are exactly d-s such pairs. Their complete t-element
tag-result families coincide: increasing both phases by one simply
reindexes the starting tag. Each alias has multiplicity two; there
is no third temporal representative of a body level. All other
endpoint pairs have distinct body parts. Subtracting these aliases
from ell-q gives (1).

For q=0, all t tags occur at each of the h+1 body levels. Event
positions repeat those same states but add no new ones; complements
remain disjoint. Hence f_0=2t(h+1). This separate q=0 argument is
necessary; the positive-q alias count was for two distinct events.
Square.

Mixed body/tag offsets introduce no omitted alias: once q and the
body endpoint pair are fixed, s=q-(z'-z) is fixed as well.

## 3. Uniform normalization

For 1<=q<=H<=dK/2, formula (1) implies

    1-q/(h+1) <= f_q/R <= 1+(d-q)/(h+1).              (2)

It also gives

    f_q/[2t(ell-q)] >= 1-d/(ell-H) >= 1-2/K.          (3)

Thus L->infinity yields asymptotically maximal distinct support
relative to the raw endpoint-pair census throughout this half-depth
range. Uniform f_q/R->1 follows if H+d=o(h). It does NOT follow for
a horizon proportional to h: the finite-row endpoint loss remains.

## 4. Literal actual-support statement and exact charge

Let H be a nonnegative integer with H<ell and H<=b-ell. For a row,
write its canonical cyclic source as

    (C, deleted coordinates in reverse chronological order,
     G, inserted coordinates in reverse chronological order).

It has period2ell and partitions the universe. Form the derivative
letters of source-window length ell-H at starts0,...,2ell+2H-1.
Every endpoint-pair target at depth q<=H occurs at a cyclic source
start with source-window length ell-q or ell+q. The corresponding
derivative interval has H-q+1 or H+q+1 letters and fits in this
finite block even at the last canonical start.

Conversely every source arc containing exactly one cap is one of
these endpoint intersections/unions or their complements. A cap-free
arc has rank at mostell-1, and an arc containing both caps has rank
at least2b-ell+1. By H<=b-ell, both ranges are outside the counted
band b-H,...,b+H. An arc spanning a whole period is the full universe.
Thus the census above counts ALL actual targets at the indicated
band ranks, not only designated witnesses.

Separate the t derivative blocks by t-1 full-universe letters.
Cross-block intervals are the full universe and add no band target.
The total literal word length is exactly

    2t ell+2Ht+(t-1).                                 (4)

For q<=min(H,dK/2), (1) and f_0=R are its exact rank-support counts.
No exterior or insurance word is included. If H+d=o(h), (4)/R->1;
R is THIS PACKET'S middle support, not the whole middle-layer width.

## 5. Relation to global selection

Suppose, separately, that a suitable centrally disjoint, near-complete
relabelled placement of these packets is constructed, with the uniform
one-packet inclusion marginal. Its candidate-supply intensity at rank
b-q would then be asymptotically

    [W(2b)/binom(2b,b-q)] [f_q/R].

When q is on the Gaussian scale and H+d=o(h), the second factor
tends to one. This reproduces the ordinary terminal-bank intensity;
it is not a larger supply benchmark. An intensity computation does
not establish a Poisson law, independent holes, or full coverage
for this new packet family.

The separate accepted higher-tag phase trade gives a lossless
old-to-new transformation into this all-forward family, preserving
EVERY actual interval union at the same compiled length without
insurance. The census here quantifies its terminal local support.
Global fresh gains, feasible placement and universal completion
remain unresolved.

