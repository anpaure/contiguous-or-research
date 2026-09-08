# A valid two-plane endpoint repair and its impossible charge-2384 gate

2026-09-08. Author: appendix_a. Pure literal construction and ledger;
no mathematical computation. Root and independent direct-route full
analytical audits passed.
The pure-corner necessity in Section 3.1 additionally passed root,
direct-route, and ternary-lift analytical review.
The literal endpoint construction is valid, but its charge-2384
completion by a balanced translation-closed saturated short bank is
IMPOSSIBLE. The pure projection argument in Section 5 of
`Q3_D8_U_STRIPS_PALINDROME_2384_AVAILABILITY_AND_CORNER_OBSTRUCTION_20260908.md`
forces charge at least 2408. Root, direct_route, ternary_lift, and
this author independently audited that proof and passed it. No
corrected model was executed. This is a scoped impossibility for
the stated translation-closed construction, not a global lower bound
for arbitrary chain-pair covers.

## 1. The two prescribed short-row constituents

Coordinates are E=F_2^3, labeled 0,...,7 with xor addition. A shore
word uses each of its four coordinates twice; its short chain retains
prefix ranks 1,...,7. A short paired row has charge fourteen.

First include the sixteen-row translation/complement bundle U from
Section 4 of
`Q3_D8_THREE_DIAMOND_POSITIVE_ELIGIBILITY_EXAMPLES_20260908.md`:

    H=0123, v=4,     N=01023231, M=00132321.          (1)

The eight original rows place N on H and M on H+v, then translate
by every element of E. Include their eight distinct complements.
The exact twelve-critical-orbit no-collision proof is the literal
descriptor table in
`Q3_D8_AFFINE_DIAMOND_COMPLEMENT_INVENTORY_AND_LITERAL_BUNDLE_20260908.md`.

Second include a four-row copied palindromic translation orbit on
a different plane direction K. To make this completely literal, take

    K=0246, w=1,     P=02466420, P+w=13577531.       (2)

The order of the four shore coordinates is 0,2,4,6, so P is the
word 01233210 in that order. Place P on K and its copy on K+w.
Its row translation stabilizer is exactly {0,w}: the first increment
identifies the first axis if shores are preserved, while translation
by w exchanges the two identical factors. Its translation orbit
therefore has four rows. The palindrome makes its short and full
chains invariant under value complementation. These four copied rows
are distinct from the independent-partner rows in (1).

The particular K in (2) differs both from H and from the direction
space V=0145 of the short Fano witness already supplied by U. The
literal endpoint construction only requires K to differ from H;
avoiding V matters for the equality conditions in Section 4.

## 2. Exactly thirty-two endpoint restorations

Make the following actual changes to those twenty prescribed rows.

* In all eight original U rows, restore the zero endpoint on the N
  shore. In all eight complemented U rows, restore the corresponding
  top endpoint on the complemented N shore. This costs sixteen.
* Fully restore both endpoints on both shores of each of the four
  palindromic rows. This costs four per row, hence sixteen.

Do NOT additionally restore an isolated M-zero or complemented
M-top in U. Those two changes in the earlier eighteen-letter repair
are unnecessary here, because the full palindromic rows already
contain the global zero and global top.

Since M starts 00, its first two states are e_0 and 2e_0. The
eight translated zero strips in U therefore cover both positive
bottom axis targets at every coordinate. Their complemented strips
cover both top coaxis targets at every coordinate. The full P rows
supply the global endpoints. Thus all 34 extremal targets are covered.
Every restored factor is still a literal strict chain.

Let R_end be the union of all targets in these added endpoint
strips, relative to their twenty original short rows. This definition
includes endpoint-by-endpoint cells newly introduced by full P
restoration, including the global endpoints. It imposes no unnecessary
requirement that the remaining short bank cover a target already in
these strips.

The critical effect is exact. At rank seven the U zero strips add
the eight translations of

    0000 | M_7 = 0000 | 2122.                       (3)

This is E_H, the class-E orbit with four-point support having direction
H. It has eight distinct targets, because its one-valued coordinate
is unique. At rank seven a full P row gains only the two cells
(0,7) and (7,0). Across its four translated rows these are exactly
the eight translations of zero paired with P_7. Their support has
direction K and P_7 has one one and three twos, so they form E_K.
The two cells correspond to the two translations differing by w;
the unique one makes all eight distinct. Since H differs from K,
E_H and E_K are disjoint. Other new P endpoint cells have rank at
least eight or involve a zero shore at a different rank.

Thus the rank-seven section of R_end consists of exactly sixteen
points, namely E_H union E_K. The complete endpoint addition is
complement invariant, so its rank-nine section is exactly the
reflection of that same sixteen-point set.

The rank-five Fano witnesses added by the strips are also exact.
Only zero-shore strips can have rank five. Here
M_5=2111, while P_5 has three ones and a two on its entire shore.
They supply precisely the witness translation orbits W_H and W_K,
respectively. The P endpoints on opposite shores merely complete
the same eight-point orbit. No top strip can have rank five. Hence
the endpoint addition contributes exactly these two distinct witness
orbits, and their rank-eleven reflections.

## 3. The actual all-rank finite gate

Suppose there is a bank of 168 short physical rows containing the
sixteen U rows and four P rows above, whose union covers every target
outside the literal set R_end. After the thirty-two upgrades it
covers the entire ternary cube. Its charge is exactly

    16*15 + 4*18 + 148*14 = 168*14+32 = 2384.       (4)

This implication has a concrete residual and concrete prescribed
rows. In particular, it does not ask the short rows alone to cover
all nonextremal targets. Its antecedent is now excluded when the
short bank is translation closed, by the pure projection obstruction
summarized in Section 5.

Each short row contributes six occurrences at rank seven and at
rank nine. The 168 short rows supply 1008 occurrences at each rank;
the endpoint additions supply sixteen distinct targets. There are
1016 targets in either full critical layer. Thus any completed bank
has eight excess occurrences at each critical rank. For a bank
developed in whole translation orbits, every odd-rank target orbit
has eight points. Consequently the critical orbit multiset consists
of every one of the 127 required orbits once and exactly one orbit
delta once more. It cannot have any additional critical repetition.

By the proved eight-axis q-ary tube amplification with the ninth
accumulator in
`QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md`,
a completed charge-2384 template would give

    (2384/2187) beta_9 = (76288/76545)c_9 < c_9.      (5)

Here the existing binary-eight template has coefficient
(35/32) beta_9. Thus the strict normalized margin is 257/76545
relative to the current c_9, without a separate active-radius
probability condition. Formula (5) is the correct conditional
amplification calculation, but the required bank cannot exist in the
translation-closed family studied here. It gives no coefficient
improvement.

### 3.1. The short critical deck is forced: exclude E_K, not E_H

For a bank developed in whole translation orbits, the apparent freedom
in the excess orbit delta disappears. This conclusion holds for all
cropped saturated balanced 4+4 rows, without restricting to the copied
and diamond families in Section 4.

Consider the pure corner

    x_H = 2*1_H.

It has rank eight and is not in R_end. The U strips have ranks at
most seven or at least nine. In a P shore, every proper nonempty
prefix has a one-valued coordinate: its first four increments are
distinct, and the last four repeat them in reverse order. Thus its
only pure 0/2 states are zero and the full shore. Across the four
fully restored P rows, the only pure corners are the global zero,
2*1_K, 2*1_(K complement), and the global top. Since K has a
different direction from H, none of these is x_H.

Consequently some short row must cover x_H. If its shores are L and
L complement, their ranks at that cell are twice |H intersect L|
and twice |H intersect (L complement)|. Both lie in 1,...,7, so
they are 2, 4, or 6. Decrease either shore rank by one along its
saturated chain. The predecessor is still retained, since its rank
is at least one. As x_H is a pure corner, the removed increment
lies at some i in H. The resulting target is x_H-e_i: it has one
one at i, three twos at the other points of H, and zeros elsewhere.
It belongs to E_H.

Translation development now forces the entire eight-point E_H orbit
to occur in the short bank. All 125 critical orbits outside E_H and
E_K already have to occur there because the endpoint strips do not
cover them. Together these require 126*8=1008 short occurrences,
exactly the total capacity of 168 short rows. Therefore the short
rank-seven deck covers every target except E_K EXACTLY ONCE. It
contains no point of E_K and has no internal repetition. The only
excess orbit after endpoint restoration is necessarily

    delta = E_H; in particular delta_C=0, delta_X=1.

There is an equally direct rank-nine statement. Increase either
shore rank at x_H by one. The rank was at most six, so the successor
remains in the cropped chain, and it adds a one at some j outside H.
The target x_H+e_j is the reflection of a member of E_H. Translation
and the same capacity argument show that the short rank-nine deck
is the exact complement of reflected E_K. This argument does not
require the short bank to be closed under complementation.

In particular, a bundle with an intrinsic critical repetition cannot
participate in any such bank. The endpoint slack cannot compensate
for that repetition: it is already forced to be the duplication of
E_H between an exact short deck and the endpoint strips.

The first bounded availability screen instead imposed exclusion of
E_H from the short deck. That subcase is universally impossible by
this lemma; its uncovered pure corner x_H has a proof independent
of the screen. No LP or integer solver was run in that screen. A
necessary corrected model would exclude E_K, chosen with the
palindromic plane, and still impose the complete all-rank residual
coverage condition. That correction was recorded but not executed.
The later pure projection obstruction also rules out the corrected
gate, so this model is not an outstanding feasibility task.

## 4. Sharp necessary conditions in the current affine bundle pool

This section restricts the short bank to complete old affine copied
translation/complement bundles and the admissible independent diamond
bundles classified in
`Q3_D8_PURE_DIAMOND_CLASSIFICATION_AND_WITNESS_LEDGER_20260908.md`.
It is not a classification of arbitrary short rows. Section 3.1
already excludes all bundles with intrinsic critical collisions,
so those cannot enlarge the pool in this endpoint construction.

Use the notation of that classification. Old generic types are

    p=C+3D+2B, q=C+3D+2F, r=C+3D+B+F,
    t=2C+4D, z=2C+2D+B+F;

their witness capacities are 1,1,0,2,0. Each contains eight physical
rows. Old self four-row types are YYX, FFX, XXX, with Y=A union B
and X=D union E; only XXX has witness capacity, at most one.
Let their counts be nYY,nFF,nXX, and put s=nYY+nFF+nXX.
New U,V,W counts are u,v,w, with physical sizes sixteen,eight,eight,
critical classes 3C+5D+3B+F, 3D+2F+E, A+3B+2D, and witness
capacities 1,1,0, respectively.

Write delta_C,delta_Y,delta_F,delta_X for the class indicators of
the single excess critical orbit. They sum to one. Removing the
two endpoint E orbits leaves the necessary short occurrence counts

    C:28+delta_C, Y:22+delta_Y,
    F:28+delta_F, X:47+delta_X.

With one unit equal to four physical rows, the exact equations are

    p+q+r+2t+2z+3u = 28+delta_C,
    s+2(p+q+r+t+z)+4u+2v+2w = 42,
    nYY = (22+delta_Y-2p-r-z-3u-4w)/2,
    nFF = (28+delta_F-2q-r-z-u-2v)/2.

Subtracting gives

    nXX = z+u-v-11-delta_C-(delta_Y+delta_F)/2.       (6)

The left side is an integer. Therefore delta cannot belong to Y
or F: it lies in C or X. Integrality of nYY now gives
r+z+u even. Nonnegativity in (6) implies r+z+u is at least eleven,
and parity strengthens that to at least twelve. The total short
witness capacity is consequently at most

    p+q+2t+nXX+u+v = 17-r-z-u <= 5.                 (7)

The two endpoint witness orbits make the total bound seven, so the
earlier six-witness contradiction no longer applies. Covering all
seven now requires equality everywhere: the short capacities must
all be attained without any repeated witness orbit, and must avoid
both W_H and W_K. In particular,

    r+z+u=12,       r+v+delta_C <= 1.                (8)

The latter follows by substituting the former in nXX>=0.

The stronger geometric conclusion in Section 3.1 fixes
delta=E_H, so the actual necessary conditions specialize to

    nXX=z+u-v-11,       r+z+u=12,       r+v<=1.

The delta_C alternative in the general bookkeeping above is therefore
eliminated; the only allowed repeated orbit is the repaired E_H itself.

Two further literal restrictions are useful. The palindromic short
orbit P has critical class multiset A+B+D: its paired splits (1,6),
(2,5),(3,4), modulo shore exchange, have classes D,B,A. Since the
only allowed excess orbit lies outside Y, this P constituent already
uses the unique A orbit. Thus w=0, and no other selected constituent
can contain A. Also U in (1) already supplies the short witness W_V,
where V=span(1,4)=0145; for example the (2,3) split has support V.
The equality requirement therefore excludes K=V as well as K=H.
The concrete K=0246 in (2) satisfies both exclusions.

These are necessary conditions for the stated affine pool. This
witness ledger alone leaves room for a seventh witness orbit, unlike
the single-plane charge-2370 ledger. The independent projection
obstruction nevertheless excludes the entire two-plane construction,
including banks outside this finite copied-plus-diamond pool.

## 5. Closed status: projection charge at least 2408

The thirty-two endpoint changes, all extremal coverage, exact two
critical orbits, exact two added witness orbits, charge, and conditional
amplification are proved above without computation. The exact short-deck
necessity and scoped pool ledger are also valid. They do not suffice
to construct a bank, and the following stronger obstruction now proves
that no stated translation-closed completion exists.

The full pure proof is Section 5 of
`Q3_D8_U_STRIPS_PALINDROME_2384_AVAILABILITY_AND_CORNER_OBSTRUCTION_20260908.md`.
Its projection weight is

    y(x) = (1/4)*#{i : sum_(j!=i) x_j=7}.

The total weight is 2358, and every balanced chain pair has total
weight at most its actual charge. Hence a full cover must pay 2358
plus the weighted excess loads of its repeated targets.

The prescribed U16 bundle forces three distinct central target
orbits. The outer (1,7)/(7,1) orbit has eight targets with two ones,
weight one-half and load at least four, causing excess charge twelve.
The inner (3,5)/(5,3) orbit and its distinct complement each have
eight targets with four ones, weight one and load at least two,
causing excess charge sixteen. Both relative U orientations have the
same odd prefix states, so the total U excess is always at least 28.

The four copied palindromic rows all contain the all-ones target,
of weight two. Its excess contributes six, disjoint from the three
U orbits. Finally, Section 3.1 forces both E_H and its rank-nine
reflection to be short covered. The U endpoint strips cover them
again. Each orbit has eight targets of weight one, so these two
critical repetitions add sixteen more. Their ranks distinguish them
from all the preceding central targets. Therefore

    charge >=2358+28+6+16=2408 >2384.

This proves impossibility of the entire prescribed two-plane gate,
including the corrected exact short deck excluding E_K. It assumes
the full U16 bundle, the copied palindrome P4, the stated endpoint
restorations with K distinct from H, balanced shores, and a
translation-closed saturated short bank. It does not use the finite
catalogue and does not rule out arbitrary endpoint constructions or
arbitrary chain-pair covers. No corrected model was run; no improved
unconditional coefficient follows from this repair.
