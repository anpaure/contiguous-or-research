# The complete charge-2368 translated-partner family is impossible

2026-09-08. Root's counting obstruction, with a complete pure word
classification and independent audit by cover-selectors. No computation
is used in this proof. The separate saved catalogue agrees with the
classification, but its counts are unnecessary here.

Root independently read the full proof and checked the prefix criteria,
all canonical collision identities, the five-type classification, and
the final capacity ledger: audit PASS. No correction was required.
Ternary-lift independently read the full proof and checked the same
collision identities, prefix table, and final ledger: audit PASS.

## 1. Family and previously proved geometric facts

Coordinates are E=F_2^3. A short rectangle uses a full four-axis
geodesic C on an affine hyperplane H, cropped to ranks1,...,7, and
its translated partner C+v on H+v. Develop under coordinate
translations and value complementation. A self-complementary orbit
contains four physical short rows and has three distinct rank-seven
target orbits. A generic complement bundle contains eight physical
short rows and, to be admissible in an exact critical cover, must
have six distinct rank-seven target orbits.

The family under consideration has164 physical short rows and one
four-row full orbit. The full word is self-complementary and begins
with two equal increments. Its charge is2368. Its critical occurrence
budget is exactly127 target translation orbits, so every critical
orbit must be covered exactly once.

Use the rank-seven classes A,...,F from
Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md, and put

    X=D union E,       Y=A union B.

Their relevant sizes are |C|=28, |Y|=22 and |F|=28. The following
facts have pure proofs in that note and in
Q3_D8_FOURTEEN_GENERIC_BUNDLES_RANK5_OBSTRUCTION_20260908.md:

* Self triples contain no C and meet both Y and F evenly. Their
  only class patterns are FFX, YYX and XXX.
* An allowed full four-edge contains two F vertices and two X
  vertices, and contains no Y or C.
* There are seven rank-five witness orbits W_L, represented by a
  two at zero and ones on a Fano line L.
* A short translation orbit covers W_L exactly when its first
  three increments use two distinct axes and then repeat one of
  them. It covers at most one W_L. The witness plane is
  span(first_axis+second_axis,v).
* A self orbit covering W_L is XXX (DDD or DDE), and an allowed
  full orbit covers no W_L.

It remains to classify ALL admissible generic bundles, including
proving that a generic bundle with no C vertex is inadmissible.

## 2. Generic bundles cannot contain A or E

Let C_r be the rank-r shore member. Its three short critical cells
have ranks (1,6), (2,5), (3,4). If C_4 has four ones, the (3,4)
cell is the unique orbit A. The complement-reversed word also has
four ones at rank four, and repeats A. Such an eight-row bundle
cannot have six distinct critical vertices.

If C_4=2e_a+2e_b, its (3,4) cell is E. After normalizing its unique
one to zero, its twos form the line

    {v,a+b,v+a+b}.

Write c,d for the other shore axes. Their sum c+d equals a+b,
because the xor of the four points of an affine plane is zero.
The reversed complement has rank-four member2e_c+2e_d and repeats
the same E orbit. This is again inadmissible.

Thus in every admissible generic bundle both half-words have the
middle state with one coordinate two, two coordinates one, and one
coordinate zero. Choose distinct shore axes a,b,c,d so that

    C_4=2e_a+e_b+e_c,
    C'_4=2e_d+e_b+e_c,                              (1)

where C' is the complement reversal. The first four increments of
C' are the reverse of the last four of C, up to harmless coordinate
translation.

## 3. Three prefix types and the possible C cell

A half-word with the middle state (1) has one of three prefix types:

* R: the first two increments agree, for example a,a,b,c;
* S: the first two differ and the third repeats one, for example
  (a,b in either order),a,c;
* T: the first three are distinct, followed by the repeated axis a.

Only S can cover a rank-five witness W_L. Denote the prefix types
of C and C' by an unordered pair from {R,S,T}.

Only the (2,5) critical cell can be C. The exact criterion is:

* P: C_2=2e_a and C_5=2e_a+e_b+e_c+e_d;
* Q: C_2=e_a+e_b and C_5=2e_a+e_b+2e_c.

The two-C proof cited above derives these criteria directly from
the canonical xor of the three one-valued coordinates. They also
classify the one-C cases.

For completeness, the other two cells are determined by the prefix
types. The (1,6) cell is F precisely when the mate has type R,
and otherwise D. The (3,4) cell is B precisely for type T,
and otherwise D. For the (2,5) cell, a type-R word gives C if
its mate is T and F otherwise. A type-S or type-T word gives B
if its mate is T, and otherwise C or D according to Q.

Applying these rules gives the following exhaustive table. A
"collision" means an actual repeated critical target orbit, as
proved just below, not merely a repeated class.

| Prefix pair | Admissible class pattern | Maximum W_L orbits |
| --- | --- | ---: |
| R,R | Collision | — |
| R,S | C+3D+2F, or collision | 1 |
| R,T | C+3D+B+F or2C+2D+B+F | 0 |
| S,S | 2C+4D, or collision | 2 |
| S,T | C+3D+2B, or collision | 1 |
| T,T | Collision | — |

Here are the only middle-cell choices needed to obtain the table.
For R,S, write the R prefix a,a,b,c. The mate's S prefix has
repeated axis d and one early single e in {b,c}. Its Q condition
holds exactly when e=b. For S,S, write the first prefix
(a,b),a,c. Both Q conditions hold if the mate's early single is b;
both fail if it is c. For S,T, with the same first S prefix, the
mate satisfies Q exactly when its first two axes include b. R,T
always has P on the R side and has Q or D on the other side.

## 4. Exact collisions exclude every zero-C case

Translation orbits are compared in canonical coordinates: translate
by the xor of the odd set of one-valued positions, so that their
xor becomes zero. For one-one targets this simply moves the one to
zero. Recall a+b+c+d=0 on the affine shore.

For R,R, the two (1,6) cells are the same F vertex. Their canonical
sets of two-valued coordinates are both

    {v,v+a+b,v+a+c}.

For T,T, the two (3,4) cells are the same B vertex. Canonically their
two-valued point is v and their zero-valued points are

    a+d,       a+d+v.

For either the zero-C R,S case or the zero-C S,S case, the first
word has rank-three state2e_a+e_b and its mate has rank-three state
2e_d+e_c. Their rank-four states are those of (1). Their two (3,4)
cells coincide: each has canonical one-set

    {v,b+c,v+b+c}

and canonical two-set

    {a+c,v+a+c}.

Finally consider the zero-C S,T case. The first word begins
(a,b),a,c. Failure of Q on the mate forces its first two axes to
be c,d. Thus the two rank-six states are

    C_6=2e_a+2e_b+e_c+e_d,
    C'_6=e_a+e_b+2e_c+2e_d.

The two (1,6) cells coincide. Put t=a+b, u=a+c, w=a+d. Their
canonical two-set is {v,v+t} and their canonical one-set is

    {t,v+u,v+w}.

These identities are unchanged by the permitted ordering of the
first two axes. They establish every collision marked in the table.
Thus ALL admissible generic bundles have exactly one of the five
listed class patterns and capacities. This conclusion needs no
finite-matrix enumeration.

## 5. Five-type ledger and contradiction

Let the numbers of generic bundles of the five types be:

    p: C+3D+2B,       capacity1;
    q: C+3D+2F,       capacity1;
    r: C+3D+B+F,      capacity0;
    t: 2C+4D,         capacity2;
    z: 2C+2D+B+F,     capacity0.

Here capacity is an upper bound on the number of distinct W_L
covered by that bundle. If s is the number of self short orbits,
the exact C demand and physical short-row budget give

    p+q+r+2t+2z=28,
    s+2(p+q+r+t+z)=41.                              (2)

The generic contribution to B is2p+r+z and to F is2q+r+z. The
full orbit removes two further F vertices and no Y vertices.
Consequently the numbers of YYX and FFX self triples must be

    YYX=(22-2p-r-z)/2,
    FFX=(26-2q-r-z)/2.                              (3)

All remaining self triples are XXX. Subtracting (3) from s and
using (2) yields the exact identity

    XXX=s-24+p+q+r+z=z-11.                          (4)

In particular z>=11. The seven rank-five witness orbits can only
be covered by the p and q types, the t type, and these XXX self
triples. Their total capacity is at most

    p+q+2t+(z-11)
      =17-r-z
      <=6,

where the equality uses the C equation in (2). Seven distinct
witness orbits therefore cannot all be covered. This is a
contradiction.

## 6. Scope

There is no charge-2368 cover consisting of164 short rows from
the complete translated-partner/complement-closed family and four
full rows from one of the allowed self-complementary first-two-equal
orbits. This excludes the full5208-short-candidate family, including
the cases left unresolved by the earlier bounded solver.

The proof does not exclude arbitrary balanced rectangles, different
partner chains on the two shores, other full-row profiles, or a
construction with slack in the critical occurrence budget. It is a
structural obstruction to this precise coupled and complement-closed
charge-2368 design.
