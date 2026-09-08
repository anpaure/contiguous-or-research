# A tight 3+5 primitive: literal flags and fixed-axis quotas

2026-09-08. Pure proof, with no mathematical execution. Root proposed the
primitive and the final quotient-loop lemma. Direct-route independently
derived or audited the arguments below. Root completed a full-file audit:
PASS. Direct-route corrected two copied actual-rank9 table entries for
roles A and B to agree with the literal flags; the G table and subsequent
arguments were unchanged. Ternary_lift independently found and checked the
same corrections and then passed the full-file audit. Root subsequently
rederived every actual-rank and central table entry from the literal
flags and states, including these corrections: PASS.

All counts follow from displayed states and flags. The final provider
restrictions concern the original29-row Singer skeleton and an exact
one-one deck. They are not a completed covering construction.

## 1. Actual row, states, and projection charge

Use disjoint coordinate names A,B,C and D,E,F,G,H. Take

    C=AABBCC,       retain ranks0,...,6;
    D=DEDEFFGHGH,   retain ranks2,...,8.

The retained states, in their own coordinate orders, are

    C: 000,100,200,210,220,221,222;
    D: 11000,21000,22000,22100,22200,22210,22211.

Both are saturated strict chains with seven states. The actual row has
49 targets and charge14. Rank7 uses local cells(i,7-i), i=0,...,5;
rank9 uses(i,9-i), i=1,...,6; rank8 uses(i,8-i), i=0,...,6. They give

    rank7: five one-one targets and one three-one target;
    rank9: five one-one targets and one three-one target;
    rank8: two pure targets and five two-one targets.

A k-one target has exactly k coordinates equal to1. The universal ternary
projection price gives total

    2*(5+3/4)+5/2=14,

equal to the actual charge. Other target ranks have price zero. Thus
this3+5 row is tight for the proved all-support projection dual.

## 2. Literal flags and odd vertices

Write(T;o) for a rank7 one-one target with twos on the three-set T and
its unique one at o. The lower flags are

    (DEF;G), (DEF;A), (ADE;F), (ADE;B), (ABD;E).    (1)

The rank9 flags, reflected to rank7 notation, are

    (BCH;G), (CGH;B), (CGH;F), (FGH;C), (FGH;E).  (2)

Reflection is notation; a C7-only row does not acquire a complementary
row unless that row is explicitly added.

In the one-one flag graph, edge(T;o) has upper vertex T union{o}.
Equation(1) has odd upper degree only at DEFG; equation(2) only at EFGH.
They intersect in EFG and have Johnson distance1. By contrast, BU has
odd vertices ABCE and CDGH, intersecting only in C, so its Johnson
distance is3. An earlier informal comparison incorrectly said2; none
of the arguments here uses that value.

The three-one targets are

    lower:           zero-set FGH, two-set AB, ones CDE;
    reflected upper: zero-set DEF, two-set BC, ones AGH.         (3)

The central two-one cells have C ranks{0,1,3,5,6}; the pure cells have
C ranks{2,4}. The corresponding D ranks are{8,7,5,3,2} and{6,4}.
This lists every positive target of the row.

## 3. Exact separate-rank and G-closed infinity tables

Let infinity be the fixed coordinate of C7. A triple below lists counts
at infinity values0,1,2. Rank9 is ACTUAL rank9. The two scalar columns
give the infinity values of the unique three-one targets.

| Role | Rank7 one-one | Rank9 one-one | Rank7 three-one | Rank9 three-one | Central two-one |
| --- | --- | --- | --- | --- | --- |
| A | (1,1,3) | (0,0,5) | 2 | 1 | (1,1,3) |
| B | (3,1,1) | (1,1,3) | 2 | 0 | (2,1,2) |
| C | (5,0,0) | (3,1,1) | 1 | 0 | (3,1,1) |
| D | (0,0,5) | (0,0,5) | 1 | 2 | (0,1,4) |
| E | (0,1,4) | (0,1,4) | 1 | 2 | (0,2,3) |
| F | (2,1,2) | (2,1,2) | 0 | 2 | (2,1,2) |
| G | (4,1,0) | (4,1,0) | 0 | 1 | (3,2,0) |
| H | (5,0,0) | (5,0,0) | 0 | 1 | (4,1,0) |

For instance, the critical local ranks on C are0..5 and1..6, whereas
on D they are2..7 and3..8. Reading the states on those intervals proves
the table. The4+4 gap formula based on intervals1..6 and2..7 does not
apply to this primitive.

Now explicitly close the row under G=C7 times global complementation.
The next table counts C7 orbit-OCCURRENCE units in a fourteen-row bundle;
distinctness of targets still requires checking the coordinate embedding.
The critical table applies at rank7 and at reflected rank9.

| Role | All critical | One-one | Three-one | Central two-one |
| --- | --- | --- | --- | --- |
| A or C | (6,2,4) | (6,1,3) | (0,1,1) | (4,2,4) |
| B | (6,2,4) | (6,2,2) | (0,0,2) | (4,2,4) |
| D or H | (6,1,5) | (5,0,5) | (1,1,0) | (4,2,4) |
| E or G | (5,3,4) | (4,2,4) | (1,1,0) | (3,4,3) |
| F | (6,2,4) | (4,2,4) | (2,0,0) | (4,2,4) |

The pure central table is always(2,0,2). The one-one, three-one, and
central two-one totals are10,2,10. If central occurrences are counted
modulo G rather than C7, this is two pure units and five two-one units,
the BQ aggregate.

The fourteen physical rows are distinct. A nonzero Singer translate
cannot preserve the three-coordinate shore support. A complemented
translate fixing the rectangle would likewise preserve that support,
so have translation zero; but complementation changes AABBCC into
CCBBAA, a different chain. The unequal support sizes distinguish the
three-coordinate factor. All coordinates vary, so the two supports
are also recoverable from the physical rectangle's coordinate-conflict
graph K3,5. This argument does not assert disjoint target coverage.

The number of infinity-containing odd upper vertices before quotient
cancellations is zero for roles A,B,C; one for D,H; and two for E,F,G.

## 4. Two G primitives plus BU: complete one-one class reduction

The original29-row skeleton has residual one-one table(13,4,9). Suppose
two G-closed3+5 primitives and one G-closed BU supply these26 target
orbits exactly, while the other profiles supply no one-one targets.
The BU tables are

| BU infinity role | One-one counts |
| --- | --- |
| A,B,E,or H | (3,1,2) |
| C | (2,0,4) |
| D | (3,0,3) |
| F | (4,0,2) |
| G | (3,2,1) |

There are exactly two possible role-class patterns:

1. Primitive infinity=A/C, primitive infinity=E/F/G, and BU
   infinity=A/B/E/H. Their sum is
   (6,1,3)+(4,2,4)+(3,1,2)=(13,4,9).
2. Primitive infinity=B, primitive infinity=E/F/G, and BU infinity=D.
   Their sum is(6,2,2)+(4,2,4)+(3,0,3)=(13,4,9).

Completeness follows by the BU infinity-one count. If it is1, the two
primitive counts must be1+2; only A/C with E/F/G leaves an available
BU table. If it is0, both primitive counts must be2; only B with E/F/G
leaves the D table. If it is2, neither primitive pairing1+1 nor0+2
leaves(3,2,1). This is direct arithmetic on the displayed tables.

It is not a restriction on a single C7 primitive or on a ledger allowing
one-one repeats.

## 5. Which primitive roles could supply infinity-one223?

Under the exact one-one premise, every infinity-zero flag must avoid
the endpoint triple deck, at either critical rank after reflection and
normalization of its unique cyclic one to0:

    F={123,126,135,146,234,245,456}.

Two complementary triples in the six remaining cyclic coordinates
can both avoid F only as

    124/356, 125/346, 134/256, 145/236.              (4)

None has necklace115 or223. The literal flags give the following tests:

* Infinity=A: its infinity-one triple DEF is paired through the zero
  flags(DEF;G) and(BCH;G), forcing DEF/BCH into(4).
* Infinity=C: its infinity-one triple FGH is paired through the zero
  flags(ABD;E) and(FGH;E).
* Infinity=B: its infinity-one triples ADE and CGH occur through the
  zero flags(ADE;F) and(CGH;F).
* Infinity=F: the same two triples occur through zero flags(ADE;B)
  and(CGH;B).
* Infinity=D or H supplies no infinity-one flag.

Consequently a primitive supplying the missing infinity-one223 orbit
must use E or G on its five-axis shore. E supplies the infinity-one
triples ABD/FGH; G supplies DEF/BCH. These roles have central two-one
infinity1 count4 in a G bundle, rather than2 for all other roles.
This is a necessary test, not a proof of eligibility for every embedding.

## 6. Typed odd-vertex parity and the possible quotient loop

In either role-class pattern of Section4, one primitive has two
infinity-containing odd upper vertices, the other has two infinity-free
odd upper vertices. Every permitted BU role has exactly one of each.
The required residual odd vertices are the endpoint pair

    H=infinity+012 (necklace115), and Hc={3,4,5,6}.

If X,Y are the infinity-containing primitive vertices and V the BU
infinity vertex, their quotient parity must satisfy

    {X} XOR {Y} XOR {V}={H}.                       (5)

If X and Y are distinct Singer orbits, one must be H and the other V.
If they coincide, they cancel and V must be H. The analogous statement
holds on the infinity-free side with Hc. A quotient loop must therefore
be retained unless separately excluded.

For example the literal proposed supplier C=114477,
D=5353220606, with cyclic roles
(A,B,C,D,E,F,G,H)=(0,2,5,6,3,1,infinity,4), has odd vertices
infinity+136 and infinity+134, necklaces223 and142. They are distinct
and neither is H. Thus this specific primitive cannot participate in
the exact Section4 provider ledger, irrespective of the eligibility of
its other targets.

## 7. A 223-supplying primitive cannot use the loop escape

It is enough to take infinity=G. Global reversal exchanges E and G,
D and H, and A and C, and is already in a G-closed primitive bank.
The two odd vertices then have cyclic triples DEF and EFH. Suppose
they are Singer equivalent. Normalize D=0. A three-subset which meets
a nonzero translate in two points is a length-three run in that shift's
seven-cycle: it has two internal adjacent edges and hence one run.
Since D is the removed point, necessarily

    {E,F}={d,2d},       H=3d,       d=1,...,6.     (6)

All arithmetic here is modulo7. The primitive's infinity-one triples
are DEF and BCH.

* If d=1 or6, DEF has necklace115, already covered by the endpoint,
  contradicting exact one-one coverage.
* If d=3, DEF has necklace133 and the remaining A,B,C labels are145.
  Since H=2, BCH has one of the triples124,125,245. None has223.
  If d=4, the remaining labels are236 and H=5, giving235,256,356;
  again the only necklaces are124,133,142.
* If d=2, H=6. With E=4,F=2, the infinity-two flag(FGH;E) has normalized
  two-pair FH-E=25, forbidden by the endpoint. With E=2,F=4, the remaining
  A,B,C labels are135. The flag(FGH;C) forces C=3: C=1 gives35 and C=5
  gives16, both forbidden. Then(CGH;F) gives CH-F=26, also forbidden.
* If d=5, H=1. The order E=5,F=3 gives FH-E=35, while E=3,F=5 gives25.
  Both are forbidden.

The endpoint infinity-two forbidden pair deck used here is
{16,35,25,26,45,56}; all cited flags are in(2). Thus no loop case can
both supply223 and satisfy the exact endpoint restrictions.

Combining Sections5-7, a223-supplying primitive in the exact two-primitive
plus BU ledger must use E/G and have a DISTINCT odd vertex of necklace115.
The existence of such an embedding is not asserted here. Nor does this
note exclude a ledger in which the sole223 orbit is supplied by BU
instead of a primitive; that is a separate question.
