# Critical orbit geometry, exact bundle counts, and complete binary parities

2026-09-08. Pure structural proofs plus two separately authorized h100
matrix reads, taking 0.062503 and 0.047476 seconds. No optimization
or solver restart ran. These structural results alone do not decide
the proposed charge-2368 cover.

Root independently audited the analytic geometry and parity proofs
in this note and reported PASS. Later scoped obstructions are in
the complete copied-family and copied-plus-diamond ledger notes.

## 1. Canonical geometric names for the 127 critical target orbits

Let x have ternary rank seven on E=F_2^3. Its set O of one-valued
coordinates has odd cardinality. Put b=xor(O). Translation by b
uniquely normalizes xor(O) to zero. The resulting representatives
split into the following six GL(3,2) classes:

| Class | Canonical description | Number of translation orbits |
| --- | --- | ---: |
| A | Seven ones; O=E minus {0} | 1 |
| B | Five ones; their complement is a Fano line L; one point of L is two | 21 |
| C | Three ones forming a Fano line L; zero is one of the two-valued coordinates | 28 |
| D | Three ones forming a Fano line L; zero is one of the zero-valued coordinates | 42 |
| E | One one, at zero; the three two-valued coordinates form a Fano line | 7 |
| F | One one, at zero; the three two-valued coordinates are not a Fano line | 28 |

Here a Fano line is a three-element subset {a,b,a+b} of E minus {0}.
The counts are 1; 7*3; 7*4; 7*6; 7; and 35-7, respectively.

For a vertex in F, define its direction d to be the xor of its three
canonical two-valued coordinates. This is nonzero. Let F_d be the
four vertices of F with that direction. The seven F_d partition F.

## 2. Directions in the original self-complementary family

A target has a direction d if its four d-pairs have value sums
2,2,2,1. For a fixed d there are

    4 choices of exceptional pair * 2 orientations * 3^3 = 216

rank-seven targets of this kind, hence 27 translation orbits.

For an original self-complementary row C x (C+v), write its symmetry
parameter as h and put d=h+v. A rank-seven target has restrictions
C_i and C_j+v, with i+j=7. Complement-translation symmetry gives

    C_i(p) + C_j(p+h)
        = 2 - (C_(j+1)(p+h)-C_j(p+h)).                (1)

The difference on the right is one unit vector. Therefore every
critical target of this row has direction d. The three critical
target orbits of the row share that direction, although some triples
also have a second common direction.

The numbers of directions are:

| Class | Directions per target orbit |
| --- | ---: |
| A | 7 |
| B | 2 |
| C | 0 |
| D | 2 |
| E | 4 |
| F | 1 |

The total incidence count is

    7 + 21*2 + 42*2 + 7*4 + 28 = 189 = 7*27.         (2)

For the three-ones case, let P={a,b} be the two-valued coordinates
and Z the three zero-valued coordinates. A direction exists exactly
when

    a+b belongs to {z+z' : z,z' in Z, z != z'}.        (3)

Indeed a valid direction must send P onto two members of Z. A
three-set has three distinct pair differences, so condition (3)
gives one unordered pair of zeros and two possible translations.
For fixed P, the six coordinates outside P form three pairs of
difference a+b. There are 3*4=12 choices of Z containing such a pair,
out of 20 total choices. Thus 28*12/8=42 orbits are eligible and
28*8/8=28 are ineligible. In the canonical labeling these are D and C.

For the one-one case, normalize that one to zero and write T for
the three twos. A direction must avoid T and its three pair
differences. If T is a Fano line, the two sets coincide and four
directions remain. Otherwise the two sets are disjoint, and their
complement in E minus {0} is the single direction xor(T). This proves
the E and F entries of the table.

## 3. Exact structural inventory of the saved candidate matrix

The admissible relaxed catalogue has 2184 size-four self-complementary
short candidates and 3024 size-eight generic complement bundles.
Their critical incidences have the following exact structure:

* The 2184 self candidates give 756 distinct triples on A+B+D+E+F,
  which has 99 vertices.
* The 3024 generic candidates give 3024 distinct six-element edges.
* Each generic edge contains either one or two vertices of C:
  2016 contain one and 1008 contain two.
* There are 112 distinct intersections of generic edges with C.
* For each fixed direction, there are 120 distinct self triples on
  its 27 vertices; their binary incidence rank is 25.
* Of the 2184 self candidates, 1176 have exactly one common direction
  among their critical targets and 1008 have two.

The same critical triple may arise with different physical rows or
directions. Consequently the sum 7*120 is not the number of distinct
global critical triples.

## 4. Necessary exact bundle counts

Suppose a charge-2368 cover in the relaxed family exists. Let

    s = number of size-four self short orbits,
    u = number of generic orbits containing one vertex of C,
    w = number of generic orbits containing two vertices of C.

The full orbit contains no vertex of C. Every critical vertex must
be covered exactly once, so the 28 vertices of C and the short-row
budget give the exact equations

    u + 2w = 28,
    s + 2u + 2w = 41.                                (4)

Therefore

    u = 28-2w,       s=2w-15,       8 <= w <= 14.     (5)

Thus the cover must use between 14 and 20 generic bundles and an
odd number of self short orbits from {1,3,5,7,9,11,13}. These are
necessary integer identities, not existence results.

## 5. Analytic proof of the global parity A+B+F

For a critical target let f(x) indicate membership in A union B union
F. Let C_0,...,C_8 be any full shore geodesic, and put n_r equal to
the number of nonzero coordinates of C_r. A translation orbit of
C x (C+v) has its three critical orbit representatives at shore-rank
pairs

    (1,6), (2,5), (3,4).                             (6)

The two shore supports, after translating the second shore back,
are nested. For a one-one critical target, total support size is
four. It belongs to F exactly when these shore support sizes are
(1,3); shore sizes (2,2) give two equal two-element supports and
therefore an affine plane, so give E.

This observation and the support sizes of A and B give the values of
f on the three representatives in (6), modulo two:

    n_6,       1+n_2+n_5,       n_3.                 (7)

For the first point n_6 is three or four, and only three gives F.
For the second, the productive pairs (n_2,n_5) are (1,3), giving F,
and (2,4), giving B. For the third, n_3=2 gives support size at most
five, while n_3=3 gives B or A. Hence the triple parity is

    P(C) = 1+n_2+n_3+n_5+n_6 mod 2.                 (8)

The complement-reversed chain has nonzero counts

    n'_r = r-4+n_(8-r).                             (9)

Substitution in (8) gives P(C')=P(C). A generic complement bundle
therefore has even intersection with A union B union F. In the
self-complementary case n_6=n_2+2 and n_5=n_3+1, which gives P(C)=0
already for its three-element edge.

The critical-collision filter guarantees that these are actual
edge incidences, with no repeated critical target orbit. Thus every
admissible short edge has even intersection with

    A union B union F, of size 1+21+28=50.           (10)

The binary incidence matrix of all 5208 admissible short edges has
rank 126 on the 127 critical vertices. Its nullspace therefore has
dimension one. The analytic relation (10) is its entire nonzero
binary parity constraint.

Both canonical full orbits pass this constraint. Their critical
class multisets are respectively F,F,E,E and F,F,D,E, so each
contains two members of (10). The all-ones demand vector also has
even intersection with (10), because 50 is even. The complete
binary parity relaxation therefore gives no impossibility proof.

## 6. The eight self-family parity relations

For a self-complementary chain, n_5=n_3+1. Of the three points (6),
the first never belongs to A or B. The second belongs to B exactly
when n_3=3; the third belongs to A or B under that same condition.
Thus every self edge meets A union B evenly.

Combining this with (10), the self edge also meets F evenly. Every
F vertex has a unique direction, and all vertices of the self edge
share the row's direction d. Therefore it meets each F_d evenly.
We have obtained the eight relations

    indicator(A union B),
    indicator(F_d),  d=1,...,7.                     (11)

Their supports are nonempty and pairwise disjoint, so they are
independent. The self incidence matrix has exact binary rank 91 on
99 vertices, hence nullity eight. The relations (11) are therefore
all its binary parity relations. Seven have weight four; one has
weight 22. This replaces the opaque saved bitvectors with canonical
geometric sets.

The generic edges project with full binary rank 28 onto C. The
all-ones vector on C lies in that projection span. Both canonical
full-orbit residual demands lie in the full short-edge span, as
also follows from the single global parity relation above.

## 7. Exact artifacts and scope

The original inventory was a single h100 process under a three-second
outer cap, two-CPU affinity, and a 1 GiB address-space limit. Its
runtime was 0.06250279815867543 seconds. A separately authorized
existing-matrix parity extraction used a one-second outer cap and
the same resource limits; it took 0.04747566021978855 seconds.

Files:

* `q3_d8_translation_orbit_structural_inventory_20260908.py`;
* `Q3_D8_TRANSLATION_ORBIT_STRUCTURAL_INVENTORY_20260908.json`;
* `q3_d8_translation_orbit_parity_extract_20260908.py`;
* `Q3_D8_TRANSLATION_ORBIT_PARITY_EXTRACT_20260908.json`.

The extraction independently assigns the six canonical geometric
classes, checks all eight proposed self relations on the saved
matrix, and verifies that its unique global nullvector is precisely
A union B union F. Gaussian elimination is over exact binary
integers. No numerical tolerances or optimization enter these ranks.

The exact candidate counts and ranks refer to the saved restricted
translation/complement catalogue. The parity proofs establish its
relations structurally; they do not construct a simultaneous cover.
