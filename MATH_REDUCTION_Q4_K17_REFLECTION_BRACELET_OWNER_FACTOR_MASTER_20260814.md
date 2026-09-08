# Reflection reduces the q4 k17 owner factor to a 750-row bracelet master

**Date:** 2026-08-14
**Status:** exact finite reduction and explicit self-column completion.  A
reflection-invariant owner factor **within the specified strong-self and
frozen paired-column family** exists if and only if the reduced master
below is feasible.  Feasibility is reported separately from this symbolic
reduction.

## 1. The owner quotient has 70 fixed bracelets

Put the ground on `Z_17` and first quotient rank-nine owners by translation.
There are

\[
                  {1\over17}{17\choose9}=1430                 \tag{1.1}
\]

owner necklaces.  Let reflection act by `r(x)=-x` on these necklaces.
Exactly 70 necklaces are fixed.

Indeed, a fixed necklace has a representative invariant under one affine
reflection

\[
                         r_t(x)=t-x.                            \tag{1.2}
\]

For fixed `t`, the involution `r_t` has one fixed point and eight
two-cycles.  An invariant nine-set must contain the fixed point and four of
the pairs, giving

\[
                            {8\choose4}=70.                     \tag{1.3}
\]

No proper nonempty subset of `Z_17` is invariant under a nonzero
translation.  Thus a nine-set cannot be invariant under two distinct
affine reflections, whose product would be such a translation.  Translating
a pair `(A,r_t)` gives all 17 representatives of one fixed necklace, so
the count in `(1.3)` is already the necklace count.

Consequently reflection has

\[
              70\text{ fixed vertices},\qquad
              {1430-70\over2}=680\text{ paired vertices},       \tag{1.4}
\]

and the owner bracelet quotient has exactly 750 rows.

## 2. An explicit complete family of strong self columns

Translation normalizes any affine reflection centre to zero.  Choose an
invariant five-core

\[
                         C=\{0,\pm a,\pm b\},                    \tag{2.1}
\]

choose five further reflection pairs, and choose one representative
`x_i` from each.  Put the ten support labels in cyclic order

\[
       \sigma=(x_1,x_2,x_3,x_4,x_5,
                  -x_5,-x_4,-x_3,-x_2,-x_1).                  \tag{2.2}
\]

Reflection reverses `(2.2)`, so it preserves the collection of cyclic
four-windows.  Since it also preserves `C`, every quotient-simple rail of
this form is a self-reflecting period-ten quotient column.

Write the labels of `(2.2)` as `s_0,...,s_9`.  Then

\[
                         -s_i=s_{9-i}.                           \tag{2.3}
\]

Reflection sends the four-window starting at `i` to the one starting at

\[
                         i\longmapsto6-i\pmod {10}.              \tag{2.4}
\]

The fixed starts satisfy `2i=6 mod 10`, hence are exactly `i=3,8`.
Quotient simplicity makes the ten owner necklaces distinct, so no other
paired starts can become accidentally equal in the translation quotient.
Thus every strong self column has exactly

\[
               2\text{ fixed owner rows}+8\text{ nonfixed rows}.\tag{2.5}
\]

The construction is centre-independent: conjugating `(2.1)--(2.2)` by a
translation gives the identical quotient column for any affine reflection
centre.

### Proposition 2.1 (fixed-row projection is the distance-two graph)

Identify a fixed rank-nine bracelet with the four reflection pairs which,
together with the fixed ground label, form its owner.  The two fixed starts
of `(2.2)` project to

\[
             A=\{a,b,x_1,x_2\},\qquad
             B=\{a,b,x_4,x_5\}.                                \tag{2.6}
\]

Thus \(|A\cap B|=2\).  Conversely, two four-subsets \(A,B\) with
intersection two determine the two core pairs \(A\cap B\) and the
four support pairs in \(A\mathbin\triangle B\).  Of the two remaining
reflection pairs, choose one for `x_3` and leave the other outside the
core and support; orientations and the two within-side orders give the
palindromic lifts.  The literal H100 catalogue confirms that every such
fixed edge has quotient-simple lifts.

Therefore the fixed-row projection of the strong-self catalogue is the
36-regular distance-two graph on the 70 four-subsets of an eight-set.  It
has

\[
              {70\cdot36\over2}=1260                            \tag{2.7}
\]

edges.  Selecting the 35 strong self columns of `(3.1)` projects to a
perfect matching in this graph.  After fixing such a matching, the only
self variables left are the alternative lifts above its 35 edges; their
four nonfixed bracelet rows remain coupled to the paired-column cover.

## 3. The exact 35-self plus 54-pair face

Start with any reflection-closed family of quotient-simple period-ten
columns.  A nonself column is paired with its reflected column.  Such a
pair is usable in a reflection-invariant exact cover only when the two
ten-sets are disjoint; otherwise selecting the pair repeats an owner row.
A usable pair covers ten paired bracelet rows.

Adjoin all distinct strong self columns from Section 2.  A self column
covers its two fixed rows and four paired bracelet rows, hence six reduced
rows.  Since nonself pairs cannot cover a fixed row, all 70 fixed rows
force

\[
                         70/2=35                                \tag{3.1}
\]

strong self columns.  They cover 280 of the 1,360 nonfixed physical owner
rows.  The remaining 1,080 rows force

\[
                         1080/20=54                             \tag{3.2}
\]

usable reflected pairs.  Equivalently,

\[
                         35+2\cdot54=143                        \tag{3.3}
\]

physical quotient columns, as required by `10*143=1430`.

### Theorem 3.1 (specified bracelet-master equivalence)

Construct one reduced column for every strong self column and every usable
reflected pair.  A self reduced column contains its two fixed bracelet rows
and its four nonfixed bracelet rows.  A paired reduced column contains its
ten nonfixed bracelet rows.  Then the following are equivalent:

1. these reduced columns exactly cover all 750 bracelet rows;
2. the corresponding 35 self columns and 54 reflected pairs exactly cover
   all 1,430 owner necklaces; and
3. developing those 143 quotient columns by all translations partitions
   all 24,310 rank-nine physical owners into 2,431 q4 period-ten rails.

#### Proof

On a paired owner orbit the two physical quotient rows have equal load by
reflection.  On a fixed row the load is the reduced load itself.  Hence
reduced exactness is equivalent row by row to exactness on all 1,430
necklaces.  Equations `(3.1)--(3.3)` give the forced column counts.  The
translation action on every rank-nine set is free, so the final equivalence
is the exact quotient-development theorem.  \(\square\)

## 4. A sharp typed boundary: global lifts cannot cover fixed lower tickets

The owner-only bracelet master cannot be strengthened to exact lower-`q1`
coverage while retaining a **globally lifted** reflection.

Rank-eight lower tickets also have exactly 70 fixed bracelets.  For an
affine reflection `r_t`, an invariant eight-set omits the unique fixed
ground label and chooses four of the eight transposition pairs, again
giving `{8\choose4}=70`.

Now consider any globally lifted self-reflecting period-ten rail.  Its
invariant odd five-core contains the unique fixed ground label.  Its
disjoint invariant ten-label support therefore contains no fixed label,
so reflection acts without fixed points on the ten support positions.  Its
induced order-two dihedral action is consequently one of:

1. an edge-axis reflection `j -> a-j` with `a` odd; or
2. the half-turn `j -> j+5`.

The forbidden third dihedral class, a vertex-axis reflection on support
positions, would fix two support labels.

For q4, the edge-axis action sends an owner-window start by

\[
                         i\longmapsto a-3-i.                    \tag{4.1}
\]

Since `a-3` is even, it fixes two owner starts but no edges of the owner
cycle.  The half-turn fixes neither owner starts nor owner-cycle edges.
Immediate-lower tickets are exactly those owner-cycle edges.  Thus every
globally lifted self column contains zero fixed rank-eight lower bracelets.

A nonself reflected pair cannot supply one either: if one member contains
a fixed lower bracelet, its reflected mate contains the same bracelet, so
selecting the pair gives load two.  Hence:

### Theorem 4.1 (global-reflection lower-ticket obstruction)

No globally lifted reflection-invariant q4 period-ten owner factor can
cover every rank-eight lower-`q1` bracelet exactly once.

This does not obstruct the positive owner-only master of Theorem 3.1.
It says that exact lower alignment must break the global reflection, use
quotient-twisted self columns with owner-dependent translating lifts, or be
repaired afterward by a lower-token transport.

## 5. Frozen finite interface

For the frozen 100,000-column multiplier-closed pool, reflection gives

```text
50,000 paired column orbits
22,992 overlapping pairs, unusable
27,008 disjoint usable pairs
0 self-reflecting columns already in the random pool
```

Thus the unaugmented pool has a sharp reflection-face obstruction: its 70
fixed bracelet rows have degree zero.  Section 2 supplies the missing
column type explicitly.  The resulting master has only 750 exact rows,
with the redundant but useful cardinalities `35` and `54` pinned.

The complete strong catalogue contains

```text
645,120 raw palindromic orders
545,824 quotient-simple orders
136,456 distinct quotient columns
1,260 fixed distance-two edges, all liftable
76..128 distinct quotient-simple lifts per fixed edge
```

Together with the 27,008 usable paired configurations this gives 163,464
variables in the monolithic 750-row master.  H100 CP-SAT returned UNKNOWN
after 614.53 seconds.  Five independently sampled fixed perfect matchings
reduced the self block to between 3,749 and 3,859 lift variables; five
further 120-second runs also returned UNKNOWN.  These are capped search
outcomes, neither infeasibility evidence nor a factor certificate.

This reduction asserts neither feasibility of that finite master nor any
lower/upper typed alignment.  If it is feasible, lower-`q1`, lower-`q2`,
and age-state rows can be added only after breaking the global reflection,
adjoining quotient-twisted self columns, or applying a lower-token
transport; Theorem 4.1 rules out the naive globally lifted strengthening.

It also does not classify every quotient-self rail.  Equality of quotient
owner sets allows the translating lift to depend on the owner, so it does
not by itself imply one global affine reflection of the physical rail.
The palindromic catalogue is complete for globally lifted self-reflections;
a constant-lift or unique-cycle lemma would be needed to identify it with
the full quotient-self family.

## 6. H100 scope

The structural census and master search use

```text
scratch/audit_q4_k17_z17_group100k_reflection_quotient_20260814.py
SHA-256 8d4abbe5de1e0705ac71ace48a60539a670c3fd056649736a140c87490cf8731

scratch/audit_q4_k17_z17_group100k_reflection_quotient_20260814.h100.out
SHA-256 21ddfc1c36dfa161cf700ab46c6c58a7e703948b06c76bb6ee0693eff09a636e

scratch/search_q4_k17_z17_reflection_invariant_owner_cover_20260814.py
SHA-256 afe93c934b8cb3bd3899df4370b265ae03073d6dfa06df175ab997053f15515b

scratch/search_q4_k17_z17_reflection_invariant_owner_cover_20260814.h100.out
SHA-256 1d500d1744a13ddaff1ebded5d12b7e41193382dc4b1180e70fb34aeb28f7c46

scratch/search_q4_k17_z17_reflection_matching_faces_20260814.py
SHA-256 207af9d7f303b86cf37e9371c990df09ecec20dbf2d2fb8a6993351d4e387acb

scratch/search_q4_k17_z17_reflection_matching_faces_20260814.h100.out
SHA-256 2b6200f109f0686039d3b8aaad41d0b958baa8d0fb7c8567a4a33a02035336ca
```

All enumeration, solving, verification, and hashing run through SSH on
H100.  The local Mac is used only for reading, editing, transfer, and Git.
