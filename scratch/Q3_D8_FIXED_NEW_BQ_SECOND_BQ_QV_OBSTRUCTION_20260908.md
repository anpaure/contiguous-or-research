# The fixed new BQ also excludes the second-BQ plus Q/V substitution

2026-09-08. Pure hand derivation by ternary_lift; independent audit
pending. No computation, enumeration, or source preparation occurred.
The fixed bank is the original skeleton plus BQ55116677/33220404.
Only the proposed charge2384 multiset

    fixed BQ + second BQ + QV + TT + NN + five NZ

is considered. The literal new BQ remains a valid partial construction.

## 1. A real aggregate-preserving substitution

Let Q=AABBCDCD and V=ABACBCDD, with interior heights respectively

    Q: 1,0,1,0,1,2,1;
    V: 1,2,1,2,1,0,1.

The ordered Q/V pair has critical vector (6,6,0,0) and central
vector (1,5,1,0), exactly the corresponding BU vectors. With
disjoint letters it is AABBCDCD / EFEGFGHH. Its six one-one flags are

    (EFG;A), (AEF;G), (ABE;F),
    (BCD;H), (CDH;B), (CDH;G).

Its only odd rank-four vertices are ABEF and CDGH, automatically
complementary. Thus this is geometrically different from BU: no
AP alignment is needed to make its odd vertices complementary.

Nevertheless the fixed new BQ has odd class223 and the endpoint
has odd class115, so the second BQ and QV must have odd classes
115 and223, one each. The already covered infinity-one classes
are115,223,142, leaving only124 and133 for these two providers.

## 2. Fixed-axis quotas

Use k,g,e for the second BQ's infinity-one flag count, gap, and
endpoint indicator. The BQ table and its one-one zero count5 are
in Q3_D8_FIXED_NEW_BQ_SECOND_BQ_BU_OBSTRUCTION_20260908.md.
Every QV infinity position has one-one zero count3. Its one-one
count j, gap v, endpoint indicator f, and central-four indicator s
are as follows. The indicator s is1 exactly when infinity is one
at the unique central four-one cell (Q rank6,V rank2).

| Infinity axis | j | v | f | s |
| --- | ---: | ---: | ---: | ---: |
| Q-A | 1 | 1 | 1 | 0 |
| Q-B | 1 | 1 | 0 | 0 |
| Q-C | 0 | 2 | 0 | 1 |
| Q-D | 0 | 2 | 1 | 1 |
| V-E | 0 | 2 | 1 | 1 |
| V-F | 1 | 3 | 0 | 1 |
| V-G | 2 | 2 | 0 | 0 |
| V-H | 1 | 1 | 1 | 0 |

The remaining one-one quota requires k+j=2. The TT/NN/NZ five-one
and four-one equations are unchanged except that s replaces the
six-provider central-four indicator: d+a=1+s+i. Here i indicates
an internal NN axis, d indicates the N-D rather than N-B choice
of its distinguished NZ, a counts long Z-A choices, and z counts
all long Z choices. Hence the ten-bundle sums are

    sum gap = 18 + g + v - s + z,
    sum epsilon = 3 + e + f + s.

An infinity0 critical extra would require epsilon sum2 and is
impossible. An infinity1 extra requires e=f=s=0; an infinity2
extra requires e+f+s=1. The table below exhausts both cases.

## 3. Every resulting branch has the wrong odd class

The preceding second-BQ obstruction note proves that a second BQ
at B-B,B-C,Q-F,orQ-G cannot have either required odd class115 or223
while avoiding the endpoint and fixed new BQ one-one flags.

| QV infinity | Necessary second BQ positions | Exclusion |
| --- | --- | --- |
| Q-A or V-H | B-B | e=0,k=1; second-BQ odd-class exclusion |
| Q-B | B-B,B-D,Q-E,orQ-H | QV itself cannot have odd115 or223, as proved below |
| Q-C | B-C,Q-F,orQ-G | e=0,k=2; second-BQ odd-class exclusion |
| Q-D or V-E | none | f+s=2 exceeds the available one unit |
| V-F | B-B | e=0,k=1; second-BQ odd-class exclusion |
| V-G | B-A | QV's odd class is an already excluded infinity-one class, as below |

For QV infinity Q-B, normalize G=0. Its odd class is the cyclic
triple AEF. Both AEF and its complementary triple CDH occur as
infinity-zero flags with unique one G. Avoiding the old endpoint
therefore restricts their necklace pair to the four familiar
possibilities (124,142),(133,124),(142,133),(133,133). In particular
the QV odd class is neither115 nor223, regardless of its partner.

For QV infinity V-G, its odd class is CDH, which is also one of its
two infinity-one flags. Both115 and223 have already been covered.
The exact flag partition therefore forbids either required odd
class. This excludes the final row of the table.

Thus the actual aggregate-preserving Q/V substitution does not
complete this fixed BQ with the unchanged seven higher profiles.
The proof uses finite literal height and flag tables only. It does
not exclude Q/V under other fixed-axis quotas, a different first
provider, different higher profiles, or an additional repair budget.
