# A pure classification of admissible diamond bundles and their witness capacities

2026-09-08. Author: direct_route. Pure proofs; no computation. This
replaces the saved diamond catalogue as a premise of the new-family
classification in `Q3_D8_COPY_PLUS_DIAMOND_2368_WITNESS_LEDGER_OBSTRUCTION_20260908.md`.
The old copied-family classification is still the theorem proved in
`Q3_D8_COMPLETE_TRANSLATION_COMPLEMENT_FAMILY_OBSTRUCTION_20260908.md`.
Root and appendix_a completed full pure-proof audits: PASS.
Ternary_lift independently audited Sections 1--4: PASS.

## 1. Physical rows and a collision test

Let E=F_2^3. Let H be an affine plane with direction space H0, and
let v be outside H0. A pair of shore words has the form

    C=a,p1,q1,p2,q2,p3,q3,b,
    D=a,q1,p1,q2,p2,q3,p3,b,                         (1)

where each coordinate of H appears twice and p_i differs from q_i.
Place D on H+v and crop both chains to ranks 1,...,7. Write C_i,D_i
for their rank-i states, and put E_i={p_i,q_i}, h=a+b. A generic
bundle means the eight translated rows together with their distinct
eight complemented rows. It is admissible here if its critical
rank-seven and rank-nine targets have no repeated translation orbit.

Every eight-row translation orbit has six distinct critical target
orbits at each critical rank. For completeness, its rank-seven
cells have splits (i,7-i), i=1,...,6. A translation preserving the
shores preserves this split. A translation exchanging shores can
only compare opposite splits; equality of the common odd-rank shore
state forces its within-H translation to be zero, because that state
has odd coordinate sum. The unequal even states then preclude the
collision. Rank nine is identical. An odd-rank target has no nonzero
translation stabilizer, since a translation-invariant vector has
even coordinate sum.

The following test detects a collision BETWEEN the original and
complemented orbits:

    E3 intersects E1+h  ==>  a rank-seven collision. (2)

Indeed, the original outer cells, written on H and H+v, are

    (e_a, 2-e_b-e_p3),   (2-e_b-e_q3, e_a).

Two rank-seven cells of the complemented row are

    (e_b, 2-e_a-e_q1),   (2-e_a-e_p1, e_b).

Translating the latter cells by h or by v+h supplies every comparison
between one of p3,q3 and one of p1+h,q1+h. Any equality of those
coordinates makes one of the displayed original cells equal to a
translated complemented cell. This proves (2), including h=0.

The diamond multigraph has degrees 2-1_{j=a}-1_{j=b}. If a=b, it is
a triangle on the other three coordinates. If a differs from b, its
edges are either a Hamilton path a-c-d-b or ab together with a doubled
edge cd. Here a+b=c+d=h.

Every triangle satisfies (2), since its first and third edges meet.
Every Hamilton order also satisfies (2): translation by h exchanges
the two outer path edges ac,db and fixes cd, so the last edge meets
the translated first edge in all six orders. The double-edge order
cd,ab,cd satisfies (2) as well. Thus a genuinely nonself bundle of
any of these types is inadmissible.

## 2. The only admissible generic case, and the self cases

The remaining graph orders are ab,cd,cd and cd,cd,ab. They are all
admissible generic bundles. To prove this, start with ab first. The
shared odd states of C,D at ranks three and five have histograms

    rank3: 2100,       rank5: 2111.

The corresponding shared states of the reversed words have histograms
0111 and 0122. Consequently none of the inner critical splits
(2,5),(3,4),(4,3),(5,2) can collide with a complemented split: the
odd shore must have the same rank in such a comparison, but the two
histograms differ. For the two outer splits, equality of the unit
state forces translation h or v+h, and the condition is exactly the
coordinate intersection in (2). Here E1+h=ab is disjoint from E3=cd,
so those collisions are impossible too. Reversal handles ab last.
This proves absence of all cross-orbit collisions, hence also that
the two physical translation orbits are distinct. Complementation
gives the identical no-collision statement at rank nine.

For the self cases, the complete elementary complement test is

    (p3,q3)=(q1+h,p1+h),       q2=p2+h.             (3)

There is no additional shore-exchanging solution: for h nonzero its
middle-coordinate equation would fix a coordinate under translation
by h; for h=0 the triangle would require identical first and third
edges. Equation (3) gives precisely the forward Hamilton order,
the reverse Hamilton order, and the middle-ab double-edge order,
with their indicated orientations. This is also proved directly in
`Q3_D8_SELF_DIAMOND_COMMON_DIRECTION_OBSTRUCTION_20260908.md`.

Thus every admissible bundle is one of: the self forward Hamilton
type V; the self reverse-Hamilton or middle-ab double-edge type W;
or the generic outer-ab double-edge type U. No catalogue is needed
for completeness.

## 3. Their exact critical classes and physical counts

Here is a short rule for checking the critical classes. For a rank-seven
target let O be its one-valued coordinates and xi be their xor.
Seven ones give class A; five ones give B. With three ones the class
is C if x(xi)=2 and D if x(xi)=0. With one one at o, class E means
the three two-valued positions, translated by o, form a Fano line;
otherwise the class is F. These are the six classes in
`Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md`.

The following normalized prefix check is complete under permutations
of the four shore coordinates and exchange of the two shores. Use
H=0123, v=4, a=0,b=1. For each displayed C word, D is obtained by
the three swaps in (1). The entries list the classes at rank-seven
splits i=1,...,6. Braces indicate the two choices in the same column.

| Case | Normalized C words | Original class sequence | Complement sequence when distinct |
| --- | --- | --- | --- |
| Forward self Hamilton | 00223311, 00232311 | D,F,{D/E},{E/D},D,F | same orbit |
| Reverse self Hamilton | 03123021, 03132021 | D,B,{B/A},{A/B},B,D | same orbit |
| Middle-ab self double edge | 02301231, 02310231 | D,B,{A/B},{B/A},B,D | same orbit |
| Generic ab first | 00123231, 00123321 | D,C,D,D,B,D | D,C,B,B,C,F |

These entries follow by taking the indicated prefixes and applying
the preceding xor rule. For example, the two generic words share
C3=D3=2100 and C5=D5=2111. Their rank-seven split (2,5) is
2000|2111, whose one-coordinate xor is 4, a two-valued position:
it is C. The complemented split (6,1) is 0222|0100, whose one is
at 5 and whose translated twos {4,6,7} are not a line: it is F.
The last diamond orientation only changes which zero or two is the
one-coordinate xor in the other entries, without changing its class.
Ab-last cases exchange the original and complemented sequences.

It follows that the class multisets are exactly

    V: 3D+2F+E,       W: A+3B+2D,
    U: 3C+5D+3B+F.                                 (4)

The physical counts can also be obtained without an inventory. There
are fourteen affine planes H, four possible v outside H0, and twelve
ordered pairs a,b of distinct axes. For fixed H,v,a,b, there are eight
oriented forward-Hamilton words, eight reverse-Hamilton words, four
self middle-ab words, and sixteen generic outer-ab words.

The row determines its two shore factors up to exchange. Indeed, all
coordinates vary for a!=b. The graph joining two coordinates when
their two-coordinate projection is NOT the Cartesian product of the
individual projections has exactly the two four-coordinate shore
cliques: a chain cannot contain the incomparable corners required
for a nontrivial product. The rank-one and rank-seven states then
recover the omitted first and last increments, so the full words
and v are recovered as well. All translation orbits have size eight.
Therefore divide by two for the choice of left shore, by eight for
translations, and by two more only for a distinct complemented pair.
This gives

    #V = 14*4*12*8/(2*8) = 336,
    #W = 14*4*12*12/(2*8) = 504,
    #U = 14*4*12*16/(2*8*2) = 336.                 (5)

The counts are supplementary; the obstruction below only uses the
complete type classification and capacities.

## 4. Exact rank-five witness capacities

Let W_L be the target translation orbit with one two at zero and
three ones on a Fano line L. Its four-point support is a linear plane.
A translate of that support meets H in zero, two, or four points.
Thus a short-row occurrence must split its support two-and-two;
the only possible rank splits are (2,3) and (3,2). The rank-two state
must consist of two ones, and the rank-three state of a two and a
one. The two support pairs must have the same difference in H0.

In forward Hamilton order, the first diamond is {a,c}. One word
starts aa, the other ac, and their common rank-three support is
{a,c}. Exactly one of the two rank splits is productive, with the
same pair difference a+c on both shores. It supplies exactly one
W_L orbit. In reverse Hamilton and middle-ab double-edge order the
first edge misses a, so the common rank-three state has three ones;
neither split can be productive. For an ab-first generic constituent,
the same productive argument applies with pair {a,b}; its ab-last
complement has a three-point rank-three support and supplies none.
Consequently the exact capacities are

    V: 1,       W: 0,       U: 1.                  (6)

This proves both the upper bounds and attainment, independently of
stored whole-row target lists.

## 5. The charge-2368 and charge-2370 witness contradictions

Use the old copied generic types and capacities

    p=C+3D+2B (1), q=C+3D+2F (1),
    r=C+3D+B+F (0), t=2C+4D (2),
    z=2C+2D+B+F (0).

Old self short types are YYX, FFX, or XXX, where Y=A union B and
X=D union E; only XXX can supply a witness, at most one. These facts
are the old copied-family theorem cited at the start. Let u,v,w count
the new U,V,W bundles and let s count old four-row self short orbits.

First take the old four-row full repair, of charge 72 and critical
contribution 2F+2X, together with 164 short rows. There is no critical
slack. With nYY,nFF,nXX denoting the numbers of old self types,

    p+q+r+2t+2z+3u=28,
    s+2(p+q+r+t+z+v+w)+4u=41,
    nYY=(22-2p-r-z-3u-4w)/2,
    nFF=(26-2q-r-z-u-2v)/2.

Subtracting nYY+nFF from s gives exactly

    nXX=z+u-v-11,       r+z+u is even.              (7)

The parity follows already from integrality of nYY. Total witness
capacity of the short rows is at most

    p+q+2t+nXX+v+u = 17-r-z-u <= 5.                (8)

Indeed nXX>=0 implies z+u>=11+v; hence r+z+u>=11,
and its parity makes it at least twelve. The full repair supplies
none of the seven required witnesses. This proves the charge-2368
impossibility for this prescribed copied-plus-diamond bundle pool.

Next consider the eighteen-letter endpoint addition in Section 5 of
`Q3_D8_THREE_DIAMOND_POSITIVE_ELIGIBILITY_EXAMPLES_20260908.md`.
Its literal repair proof has passed this author's independent audit.
It adds one class-E target orbit at each critical rank and covers all
34 extreme targets. Its residual critical demands are therefore

    C:28,       Y:22,       F:28,       X:48.

Its rank-five endpoint strips supply exactly one W_L orbit: in the
displayed N,M words, N5=M5=2111, supported on the entire affine shore,
so every such witness has the fixed direction space H0. The extra
matched endpoint restoration gives that same witness orbit. The top
strips have no rank-five targets.

For a 168-short-row bank the unit budget is 42 and the numerator 26
in nFF becomes 28. These two changes cancel in the subtraction, so
(7) and (8) remain identical. The short rows can supply at most five
witnesses and the endpoint addition at most one more. Six is less
than the required seven. Thus the particular charge-2370 strategy
also fails within this same complete bundle pool.

This last statement uses the correct residual: the short bank need
only cover the complement of the complete added endpoint-strip union.
At each critical rank that residual has 1008 points, exactly the
number of short-row critical occurrences. Hence repeated short
critical orbits, including any use of an inadmissible generic diamond
bundle, cannot evade the ledger.

These results do not exclude arbitrary independent endpoint modes,
non-affine copied bundles, banks that are not unions of the specified
translation/complement bundles, or a different endpoint construction.
