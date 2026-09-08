# Positive eligibility examples for independent three-diamond partners

2026-09-08. Pure explicit construction; no mathematical computation.
Author: appendix_a. Root full analytical audit and direct-route full
construction-proof audit passed. The critical-orbit census is also
proved by the separately audited literal descriptor note cited below.
These are
physical rows and individual eligibility statements, not a small
simultaneous cover.

## 1. Four physical rows and their symmetries

Label coordinates by E=F_2^3, with xor addition, and use
H={0,1,2,3}, v=4. A word of length eight on H describes the
successive unit coordinate increments of a full ternary shore
geodesic. All words below use every axis twice. The partner word
is placed on H+4. Retain shore ranks 1,...,7.

Use the following words:

    P = 00113322,       Q = 01031232,
    S = 01233210,
    U = 03213012,       V = 02331102.                    (1)

The rows (P,P) and (S,S) are copied self-complementary rows. Word
P has reversal-plus-translation symmetry h=2, and S is a palindrome
(h=0). The independent rows (P,Q) and (U,V) have the three-diamond
form: their first and last increments agree, and the three pairs
of intermediate increments are swapped between the shores.

For (P,Q), the endpoints are a=0,b=2 and its three ordered pairs
in P are (0,1),(1,3),(3,2). For (U,V), the same endpoints have
pairs (3,2),(1,3),(0,1). These are the forward and reverse
Hamilton-path cases, respectively. Every pair has unequal axes.
Each of P,Q,U,V separately equals its reversal translated by h=2.
These identities can be checked by reversing the displayed words
and xor-adding two to each letter.

Thus the examples belong to the complement-preserving family in
the task, and their translation developments remain in that family.
The independent rows have eight-row translation orbits; copied
rows have four-row translation orbits. This observation does not
assert compatibility between different selected orbits.

## 2. An explicit Fano rank-five witness

For a two-dimensional linear plane W={0} union L, the old witness
has value two at zero, value one at the three points of the Fano
line L, and zero elsewhere. The row (P,Q) at shore ranks (3,2)
contains exactly

    P_3=(2,1,0,0),       Q_2=(1,1,0,0),
    x=(2,1,0,0,1,1,0,0).                              (2)

Its support is W={0,1,4,5}, so it is the witness for L={1,4,5}.
Invertible linear coordinate transformations act transitively on
the seven two-dimensional subspaces of E and preserve the word
construction. Their images of (2), followed by translations if
desired, make EVERY one of the seven old rank-five witness orbits
individually eligible in the independent-partner family.

Thus the forward independent orbit can supply a W_L witness from
the new row family. The earlier fourteen-generic-bundle theorem
was a simultaneous-capacity obstruction; this membership does not
invalidate its scoped conclusion. The separate common-direction
obstruction at rank seven still applies to the self-complementary
three-diamond family.

## 3. Every central geometric type is individually eligible

The rank-eight layer has eight AGL(3,2) orbits. The following
description also proves completeness without a catalogue.

* With no ones, the four two-valued points form either an affine
  plane or an affinely independent four-set. The latter condition
  is equivalent to their xor being nonzero. These are two orbits.
* With two ones at {o,o+w}, the remaining six coordinates are the
  three other w-pairs. The three two-valued coordinates either
  choose one from each pair, or have pair counts (2,1,0).
  These are two orbits.
* With four ones, write T and Z for the two two-valued and two
  zero-valued positions. The differences of the two pairs are
  either equal or different. These are two orbits.
* With six ones, the single two and single zero give one orbit;
  the all-one target gives the last orbit.

Here are brief transitivity checks for the nontrivial assertions.
For two ones, the stabilizer of their pair acts as all permutations
of the other three points of E/<w>. Its kernel can independently
choose the endpoint in each of those three pairs: an affine Boolean
function on the quotient can take arbitrary values at three
distinct points of F_2^2. Thus each of the two listed pair-count
types is one orbit. For four ones, translate one two to zero and
write T={0,u}, Z={a,a+t}. If t=u, the two pairs lie in one affine
plane and all such configurations are equivalent. If t differs
from u, disjointness forces u,a,t to be linearly independent, so
again all such configurations are equivalent. Four distinct
binary-corner positions with nonzero xor are affinely independent;
the standard basis-map argument handles that case too.

The explicit targets below realize every type. A word pair refers
to (1), and i,j specify its retained shore ranks. Targets are
listed in global coordinate order 0,...,7.

| Central type | Word pair | (i,j) | Actual target |
|---|---|---|---|
| Four twos forming a plane | (P,P) | (4,4) | 22002200 |
| Four twos not forming a plane | (P,P) | (2,6) | 20002202 |
| Two ones; twos a w-pair transversal | (P,P) | (3,5) | 21002201 |
| Two ones; twos not a w-pair transversal | (P,Q) | (2,6) | 20002211 |
| Four ones; equal T and Z pair differences | (S,S) | (2,6) | 11001122 |
| Four ones; different T and Z pair differences | (U,V) | (2,6) | 10011212 |
| Six ones | (S,S) | (3,5) | 11101112 |
| Eight ones | (S,S) | (4,4) | 11111111 |

For example, 20002211 has ones at 6,7, so w=1. Its twos
at 0,4,5 have counts (1,0,2) in the other three w-pairs.
For 10011212, the twos are at 5,7, with difference two,
while the zeros at 1,2 have difference three. These are exactly
the two central types absent from the old copied-self family.

The copied and independent word families are invariant under
affine relabelings. The table and transitivity proof therefore
show that their union makes every central target individually
eligible. They do not assert that a bounded number of the row
orbits simultaneously covers these targets.

## 4. A genuinely nonself row reaches the old critical C target

Take instead

    N = 01023231,       M = 00132321.                  (3)

The common endpoints are a=0,b=1; the three pairs in N are
(1,0),(2,3),(2,3), swapped in M. Each pair has distinct axes,
although the unordered edge {2,3} is repeated, as permitted by
the three-diamond construction. The two words are full geodesics.
At retained ranks (5,2),

    N_5=(2,1,1,1),       M_2=(2,0,0,0),
    x=(2,1,1,1,2,0,0,0).                              (4)

This is the explicit rank-seven target excluded by the old copied
self-complementary family and by the common-direction obstruction
for self-complementary three-diamond rows.

The example is genuinely nonself. A complement-translation
symmetry, with or without exchanging the two shores, would force
the within-H translation to be h=a+b=1 by the first/last axes.
But reversal(N)+1 is 02323101, which is neither N nor M.
Thus the row's complement is not in its translation orbit. The
translation orbit itself has eight distinct rows: a translation
preserving shores must fix the first axis and hence be zero;
one exchanging shores would then require N=M, which is false.
A separate complemented translation orbit gives a sixteen-row
candidate bundle.

The explicit canonical descriptor proof in Section 3 of
`Q3_D8_AFFINE_DIAMOND_COMPLEMENT_INVENTORY_AND_LITERAL_BUNDLE_20260908.md`
confirms twelve distinct critical translation orbits in this bundle, with class
multiset 3C+5D+3B+F. The three reported C parameters are
(L=123,t=4), (L=347,t=1), and (L=246,t=1), in the notation of
Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md.
All twelve descriptors in that separately audited note differ;
this is an exact no-collision proof, also checked by the bounded
literal catalogue. It is not merely a numerical count. No-collision
inside this one bundle still does not give a complete critical cover.

All four sections concern explicit row eligibility or a candidate
bundle. No full rank-seven partition, all-rank integral bank, or
improved asymptotic coefficient is claimed.

## 5. An actual eighteen-letter endpoint repair inside the nonself bundle

Start with all eight translates of the cropped row (N,M), together
with their separate complemented rows. Each of these sixteen rows
initially has charge fourteen.

Restore the zero endpoint on the N shore in each of the eight
original translates. This costs eight. Word M starts with 00,
so its first two states are e_0 and 2e_0. Paired with the restored
zero, their coordinate translates cover the two positive bottom
axis targets at every one of the eight coordinates.

In each of the eight complemented rows restore the corresponding
N-complement top endpoint, also costing eight. These upgrades cover
every top coaxis target. Finally restore the M zero endpoint in one
original row, and the M-complement top endpoint in its complemented
partner, costing two more. These give the global minimum and maximum.
The total endpoint addition is exactly eighteen and repairs all
34 extremal targets. All restorations preserve the actual chains.

Its critical-rank effect is exact. The eight original zero-endpoint
upgrades add the translates of

    0000 | M_7 = 0000 | 2122                           (5)

at rank seven. This target has one unique one-valued coordinate,
so its translation orbit has eight distinct points. It is the
plane-support E_H orbit in the existing critical notation. The
complemented upgrades add its reflected rank-nine orbit. The
one extra M-zero endpoint adds N_7|0000 at rank seven, but
N_7=M_7=2122, so this target already occurs among (5)'s translations
(translate by v=4). Its upper counterpart is likewise already
covered. Thus there is exactly one new eight-point orbit available
at each critical rank from the endpoint additions; repetitions
with other preexisting short rows are not excluded.

Let R_end denote the explicit union of the added endpoint strips
above, including the global minimum and maximum. It contains all
34 extremal targets and precisely the eight targets of (5) at rank
seven, and their eight complements at rank nine.

This gives a precise simultaneous-cover implication. Its antecedent
is now excluded for balanced covers by the pure projection obstruction
described below. If a
168-short-row bank contains the sixteen-row bundle above and covers
every target outside R_end, the upgrades produce a full cover of charge

    168·14+18=2370.                                   (6)

For a bank developed in whole translation orbits, the necessary
critical arrangement consists of 126 distinct target translation
orbits supplied by the short rows and the new E_H orbit, totaling
all 127. The
underlying 168 short rows have 1008 occurrences at each critical
rank; the added eight-point orbit supplies the remaining eight.
The extra global-endpoint restoration gives only the already
identified repetition. No such 126-orbit selection is constructed
in this note.

Under the proved q-ary amplification theorem, a completed charge-2370
template would give coefficient

    (2370/2187) beta_9 = (5056/5103)c_9 < c_9.          (7)

The endpoint repair is proved; (6) as a full cube cover and (7)
are conditional implications whose required balanced bank is now
impossible. The unrelated
copied-partner endpoint obstruction does not apply automatically
to this genuinely independent row pair.

For the specific pool of old affine copied bundles plus admissible
affine diamond bundles, the charge-2370 bank is now excluded by the
pure witness ledger in
`Q3_D8_PURE_DIAMOND_CLASSIFICATION_AND_WITNESS_LEDGER_20260908.md`.
Its short rows cover at most five Fano witness orbits, and this
eighteen-letter endpoint repair supplies only one more. That scoped
obstruction does not invalidate the literal repair. The later pure
projection argument in Section 5 of
`Q3_D8_U_STRIPS_PALINDROME_2384_AVAILABILITY_AND_CORNER_OBSTRUCTION_20260908.md`
is stronger: retaining the full U16 bundle forces charge at least
2358+28=2386 in ANY balanced cover. Thus the charge-2370 antecedent
also fails without the finite-family restriction. The literal
eighteen-letter restoration and its conditional charge calculation
remain valid. A different two-orbit endpoint repair, whose stated
translation-closed charge-2384 completion is likewise now excluded,
is recorded in
`Q3_D8_TWO_PLANE_ENDPOINT_REPAIR_2384_GATE_20260908.md`.
