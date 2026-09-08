# Seven rank-five witnesses exclude fourteen generic bundles

2026-09-08. Root's obstruction, completed and independently audited by
cover-selectors. Pure mathematics; no computation. This excludes the
entire fourteen-generic-bundle case of the relaxed translated-partner
family, without a Singer-orbit assumption.

Ternary-lift independently read and checked the complete proof: audit
PASS, including the DDE correction, generic word classification, full-row
witness exclusion, and exact capacity ledger. The stronger complete-family
obstruction is now proved in
Q3_D8_COMPLETE_TRANSLATION_COMPLEMENT_FAMILY_OBSTRUCTION_20260908.md.

The notation A,...,F for rank-seven translation orbits is that of
Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md. Write

    X=D union E,       Y=A union B.

These auxiliary X,Y sets are not the names of the rank-five witnesses
below. A self short orbit has three critical vertices; a generic
complement bundle has six; the allowed full orbit has four. The
allowed full words are self-complementary and begin with two equal
increments. A charge-2368 bank has one full orbit and164 short rows.

## 1. Seven target orbits and the first three increments

For every Fano line L in E=F_2^3, let W_L denote the translation orbit
of the rank-five target

    x_0=2,       x_p=1 for p in L,       x_p=0 otherwise.

Its support is the plane V={0} union L. The unique two-valued point
canonically fixes the origin, so these are seven distinct translation
orbits.

Consider a short rectangle C^circ x (C^circ+v). Orient its shores
so the shore H containing the two-valued point is the linear
hyperplane containing zero. If H=V, the other restriction is zero,
which is excluded by cropping. Otherwise H intersects V in {0,t}.
The restriction to H is2e_0+e_t, of rank three. The translated-back
restriction from H+v has two one-valued coordinates, of rank two.
Comparability forces its support to be {0,t}; equivalently,

    v in V minus H,
    C_2=e_0+e_t,       C_3=2e_0+e_t.                (1)

Thus a short word covers W_L exactly when its first two increments
use distinct axes and its third repeats one of them. For such a word,
with first axes a,b, the witness support plane is uniquely

    V=span(a+b,v).                                  (2)

Translation or exchanging the two shores does not change (2).
Consequently each translation orbit of a short row covers at most
one W_L, and a generic complement bundle covers at most two.

## 2. Which self rows and full rows can cover these witnesses?

Suppose a self-complementary short word satisfies (1), with symmetry
parameter h. Its rank-five member is the complement of C_3+h.
The comparison C_3<=C_5 forces h outside {0,t}: otherwise C_5 has
value zero or one at the coordinate where C_3 has value two. In the
coordinate order 0,t,h,t+h,

    C_3=(2,1,0,0),       C_5=(2,2,0,1).

The fourth increment may be t OR t+h. This distinction matters:
the corresponding critical classes are D,D,E or D,D,D, respectively.
In either case the self triple lies wholly in X=D union E. Indeed,
the (1,6) target is D; the (2,5) target is D because the single one
of C_5 is outside the two-point support of C_2; and the (3,4) target
is E when C_4 closes t, or D when it opens t+h.

Thus only XXX self triples can cover W_L, at most one witness orbit
per self orbit. The stronger assertion that every such triple is
DDD would be false: H=0123, h=2 and word01013232 give DDE.

An allowed full row covers none of the W_L. When H differs from V,
(1) forces two distinct first increments, contrary to the full-row
condition. When H=V, coverage would require

    C_5=2e_0+sum_(p in L)e_p.

The first two equal increments give C_2=2e_a, and C_2<=C_5 forces
a=0. Self-complementarity then makes C_6 the top vector minus2e_h.
It has a zero coordinate, contradicting C_5<=C_6 because C_5 is
positive in every coordinate.

## 3. Pure classification of generic bundles with two C vertices

For any shore word w, its three short critical representatives have
shore ranks (1,6), (2,5), (3,4). Only the middle representative can
belong to class C.

For (1,6), whenever the total number of ones is three, their xor
lies in H, whereas both two-valued coordinates lie in H+v. It is
therefore D. For (3,4), the only three-one case has shore members
2e_a+e_b and2e_a+e_b+e_c. The xor of its ones is c, where the target
has value zero; this is also D.

The (2,5) representative is C in exactly two situations, with
a,b,c,d denoting the four distinct shore axes:

* P: the first two increments are a,a, and C_5 has values
  2 at a and1 at b,c,d.
* Q: C_2=e_a+e_b and C_5=2e_a+e_b+2e_c, with d still absent.

For Q the order of the first two increments is unrestricted. To
verify completeness, when C_2 has two ones and C_5 has a single one,
the canonical origin is two-valued exactly when that single-one
axis occurs in C_2. When C_2 has a two, the only possible C case
has three ones in C_5, giving P.

An admissible generic bundle with two C vertices must have its
(2,5) representative in C for both w and its complement reversal.
There are exactly two resulting structural types.

If either word has type P, write it

    a a b c d e f g,

where b,c,d and e,f,g are permutations of the other three axes.
The reversal has type Q exactly when b occurs among f,g, or
equivalently e differs from b. The original word has critical
classes D,C,D. Its reversal starts with three distinct increments
and has critical classes F,C,B. The resulting generic type is

    G_BF: 2C+B+2D+F.                                (3)

Neither constituent word has the first-three-increment pattern in
(1): one begins aa, and the other begins with three distinct axes.
Thus G_BF covers no W_L.

In the other case both words have type Q. Up to the two indicated
orders, the word must be

    (a,b in either order), a,c,c,d,(b,d in either order).  (4)

To see this, Q fixes the first-five multiset to a,a,b,c,c and the
last-three multiset to b,d,d. Distinct final two increments force
step six to be d. The reversal can have type Q only if step three
is a, leaving steps four and five equal to c. Each constituent
then has critical classes D,C,D, giving

    G_D: 2C+4D.                                     (5)

This type covers at most two W_L, by (2). Equations (3) and (5)
classify all two-C generic bundles analytically; no catalogue count
is needed for the obstruction.

## 4. The exact-count contradiction

Suppose a charge-2368 cover uses fourteen generic bundles. Since
the28 C vertices occur in neither self triples nor allowed full
edges, and each generic bundle contains at most two C vertices,
all fourteen must contain exactly two. The short-row budget then
leaves thirteen self short orbits.

Let t of the fourteen generic bundles have type G_D; the other
14-t have type G_BF. Exact critical coverage is forced by the
occurrence budget. After the generic bundles, the remaining demands
are

    Y:8+t,       F:14+t,       D:14-2t,       E:7.

The full edge consumes two F vertices and two X vertices. This uses
its verified critical class multiset F,F,E,E or F,F,D,E. It consumes
no Y vertex. Thus the demands for the thirteen self triples are

    Y:8+t,       F:12+t,       X:19-2t.              (6)

Every self triple meets Y evenly and F evenly, by the structural
parities in the critical-geometry note. Therefore its only possible
types are FFX, YYX and XXX. Equation (6) forces their counts to be

    FFX = 6+t/2,
    YYX = 4+t/2,
    XXX = 3-t.                                     (7)

Integrality and nonnegativity give t even and0<=t<=3; hence

    t in {0,2}.                                    (8)

Now count the seven rank-five witness orbits W_L. The full edge
and all G_BF bundles cover none. The t bundles of type G_D cover
at most2t witnesses. Only the3-t XXX self triples can cover a
witness, and each covers at most one. The total available capacity
is therefore

    2t+(3-t)=3+t<=5<7,

a contradiction.

## 5. Exact scope and updated necessary counts

There is no charge-2368 cover in the relaxed translated-partner
family using fourteen generic complement bundles and thirteen self
short orbits. This includes every two-Singer-orbit source of that
form, without assuming its particular remaining class profile.

In the notation u for one-C generic bundles and w for two-C bundles,
the previously derived identities were

    u=28-2w,       s=2w-15,       8<=w<=14.

The present theorem excludes w=14. Consequently a cover in this
family would require8<=w<=13, between15 and20 generic bundles, and
between1 and11 self short orbits. This is an obstruction to one
family subcase, not a proof against arbitrary ternary rectangle banks
or against every charge-2368 translated-partner cover.
