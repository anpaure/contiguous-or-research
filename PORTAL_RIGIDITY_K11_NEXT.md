# Portal rigidity at `k=11`: the one-defect theorem and the viable thirteen-portal target

## Verdict

The saturated short-band clauses force substantially more than the previous
“at most one rank-eight internal portal” observation.

For `k=11`, exactly one cell among

\[
 \{R_2(1),\ldots,R_2(369)\}
 \mathbin{\dot\cup}
 \{R_3(370),\ldots,R_3(463)\}
\]

has rank at most four; every other cell in this 463-cell set has rank five.
Consequently the 368 internal portals `R_4(1),...,R_4(368)` are all rank
seven except possibly one.  The seam portal `R_4(369)` has rank between six
and nine.  Hence among all 369 proposed portals, at most two can have rank at
least eight.

This disproves the proposed row-four grading with 330 rank-seven and 39
rank-eight portals.  It does **not** disprove the broad Single-Switch
Saturated Braid Conjecture, and it does not even disprove the clean lower-row
grading by itself.  Rank-eight and higher masks may be delegated to longer
windows.

The actual thirteen omissions of the current fixed-delay `k=11` factor have
exactly the profile allowed by the rigidity theorem: twelve have rank seven
and one (`958`) has rank eight.  Two locally consistent repairs are described
below.  Neither is yet a global construction.

## 1. Hypotheses and strict containment

Let `A_1,...,A_465` be nonempty masks and write

\[
 R_q(i)=A_i\cup\cdots\cup A_{i+q-1}.
\]

Assume only the short-band part of the proposed single-switch conjecture:

1. all windows of lengths one, two, and three have pairwise distinct ORs;
2. `R_3(1),...,R_3(369)` are rank-six masks; and
3. every other short-window OR is a different member of
   `\{S:1\le |S|\le5\}`, and these other 1,023 ORs exhaust that lower ideal.

Put

\[
 B_i=R_2(i),\qquad T_i=R_3(i),\qquad P_i=T_i\quad(1\le i\le369).
\]

Distinctness turns every physical containment between short windows into
strict set containment.  In particular,

\[
 A_i,A_{i+1}\subsetneq B_i,
 \qquad
 B_i,B_{i+1}\subsetneq T_i.                 \tag{1.1}
\]

It follows that every pair has rank at least two and every triple has rank at
least three.

## 2. Exact rank-five location theorem

### Theorem 2.1 (one-defect theorem)

Under the three hypotheses above:

1. every singleton `A_i` has rank at most four;
2. every pair `B_i` with `370<=i<=464` has rank at most four;
3. exactly one cell in

   \[
    \mathcal F=
    \{B_1,\ldots,B_{369}\}
    \mathbin{\dot\cup}
    \{T_{370},\ldots,T_{463}\}
   \]

   has rank at most four, and the other 462 cells have rank five.

Thus precisely one of the following two alternatives holds.

| alternative | early pairs `B_1,...,B_369` | late triples `T_370,...,T_463` |
|---|---:|---:|
| pair defect | 368 rank-five, one rank `2..4` | all 94 rank-five |
| triple defect | all 369 rank-five | 93 rank-five, one rank `3..4` |

The exceptional position is not located more precisely by short-band
saturation alone.

### Proof

No singleton can have rank five.  If `|A_i|=5`, an adjacent pair containing
it strictly contains it by (1.1), and hence has rank at least six.  But every
pair belongs to the lower ideal by hypothesis 3.

For `370<=i<=463`, the pair `B_i` is a proper subset of the lower triple
`T_i`, so `|B_i|<=4`.  The last pair `B_464` is a proper subset of
`T_463`, so it too has rank at most four.

The 465 singleton cells and these 95 late-pair cells give 560 distinct masks
of ranks at most four.  There are exactly

\[
 \binom{11}{1}+\binom{11}{2}+\binom{11}{3}+\binom{11}{4}
 =11+55+165+330=561                         \tag{2.1}
\]

such masks.  All 462 rank-five masks must therefore occupy 462 of the 463
cells in `\mathcal F`, leaving exactly one lower-rank defect there.  The
minimum ranks in the table follow from (1.1).  This also proves that the two
alternatives are exhaustive.  ∎

The proposed clean grading—368 rank-five values in rows one and two and all
94 residual triples rank five—is exactly the pair-defect alternative.  What
was false was not this lower grading, but the attempted placement of 38
rank-eight internal transitions on top of it.

## 3. Exact internal-portal rigidity

For `1<=i<=368`, define the internal portal

\[
 U_i=R_4(i)=P_i\cup P_{i+1}.
\]

The shared physical pair satisfies

\[
 B_{i+1}\subseteq P_i\cap P_{i+1}.           \tag{3.1}
\]

The two rank-six masks `P_i` and `P_{i+1}` are distinct, so their intersection
has rank at most five.  If `b_i=|B_{i+1}|`, then

\[
 7\le |U_i|
 =12-|P_i\cap P_{i+1}|
 \le12-b_i.                                  \tag{3.2}
\]

In particular, whenever `|B_{i+1}|=5`, one has the exact identities

\[
 P_i\cap P_{i+1}=B_{i+1},\qquad |U_i|=7.     \tag{3.3}
\]

The one-defect theorem now gives the complete internal profile.

### Corollary 3.1

At least 367 of `U_1,...,U_368` have rank exactly seven, and at most one has
rank greater than seven.

More precisely:

- in the triple-defect alternative, all 368 internal portals have rank
  seven;
- in the pair-defect alternative with exceptional pair `B_h`, every internal
  portal has rank seven except possibly `U_{h-1}` when `2<=h<=369`;
- if `h=1`, all 368 internal portals again have rank seven; and
- if `b=|B_h|` and `2<=h<=369`, the sole exceptional candidate obeys

  \[
   7\le |U_{h-1}|\le12-b,
   \qquad b\in\{2,3,4\}.                     \tag{3.4}
  \]

Thus its maximum possible rank is respectively 10, 9, or 8 when the defect
has rank 2, 3, or 4.  A lower-rank defect need not make the portal high: the
actual intersection may still have rank five.

This says that the upper-facing path is a Johnson path at every transition
except possibly one.  At every ordinary transition its physical pair is
exactly the rank-five Johnson intersection.

## 4. The seam has different, but still sharp, bounds

Set

\[
 V=R_4(369)=P_{369}\cup T_{370},
 \quad t=|T_{370}|,
 \quad b=|B_{370}|.
\]

Here `3<=t<=5`, `2<=b<=t-1`, and

\[
 B_{370}\subseteq P_{369}\cap T_{370}.
\]

Writing `c=|P_{369}\cap T_{370}|` gives the exact formula

\[
 |V|=6+t-c,qquad b\le c\le t.                \tag{4.1}
\]

Consequently

\[
 6\le |V|\le6+t-b\le9.                       \tag{4.2}
\]

If the seam is required to be a strict upper portal, its rank is therefore
7, 8, or 9.  More explicitly:

- `|V|=8` iff `c=t-2`; hence either `t=5` and `b<=3`, or `t=4` and `b=2`;
- `|V|=9` iff `t=5` and `c=b=2`;
- `|V|=6` iff `T_370` is contained in `P_369`.

Combining Sections 3 and 4, at most one internal portal and the seam can have
rank at least eight.  Thus at most two of all 369 portals can do so.

## 5. What exactly is refuted

The proposed row-four equation required the 369 portals
`R_4(1),...,R_4(369)` to consist of 330 rank-seven and 39 rank-eight values.
That is impossible: the 368 internal cells alone contain at least 367
rank-seven values and at most one value above rank seven, while the seam
contributes at most one further value of rank at least eight.

Therefore all of the following are refuted:

- 38 rank-eight distance-two bridges inside the 369-vertex `P` block;
- the `330 rank-seven + 38 rank-eight + one rank-eight seam` ledger; and
- the claim that the 39 components of a 330-edge rank-seven forest can be
  joined by 38 rank-eight internal portals without changing the saturated
  lower rows.

The following are **not** refuted:

- the broad single-switch short-band clauses;
- the pair-defect clean lower grading on its own;
- a single exceptional internal rank-eight portal;
- a rank-eight seam portal; or
- upper coverage in which nearly all rank-eight masks first occur in windows
  of length at least five.

The broad conjecture does not prescribe 39 rank-eight values in row four.
Its upper-ideal clause could still be met by mostly rank-seven portals plus
longer windows.

If one also imposes the fourth single-switch clause that
`R_4(370),...,R_4(462)` are the remaining 93 distinct rank-six masks, the same
argument applies on the lower-facing side.  In the pair-defect alternative
these 93 masks form a Johnson path whose 92 internal intersections are
exactly `T_371,...,T_462`; its two endpoint facets are `T_370,T_463`.  In the
triple-defect alternative this lower-facing path has at most one
non-Johnson transition.  This conditional statement recovers the valid part
of the proposed `92+2=94` count.

## 6. A corrected thirteen-portal target

The current fixed-delay length-465 factor misses exactly

\[
\begin{array}{ll}
\text{rank 7:}&251,493,607,941,956,1267,1468,1694,1763,1884,1946,1990,\\
\text{rank 8:}&958.
\end{array}                                      \tag{6.1}
\]

This `12+1` profile fits the theorem exactly.  It does not require 38
rank-eight bridges.

### 6.1 A literal central-edge ledger for the twelve rank-seven targets

The following table is a set-theoretic certificate that each rank-seven
omission can be an ordinary Johnson portal.  In every row, `X` and `Y` are
distinct rank-six masks, `X union Y` is the target, and `X intersection Y` is
a rank-five overlap.  All 24 endpoints are distinct, and the 12 overlaps are
also distinct.

| target | `X` | `Y` | `X intersection Y` |
|---:|---:|---:|---:|
| 251 | 250 | 249 | 248 |
| 493 | 492 | 489 | 488 |
| 607 | 606 | 605 | 604 |
| 941 | 940 | 937 | 936 |
| 956 | 952 | 948 | 944 |
| 1267 | 1266 | 1265 | 1264 |
| 1468 | 1464 | 1460 | 1456 |
| 1694 | 1692 | 1690 | 1688 |
| 1763 | 1762 | 1761 | 1760 |
| 1884 | 1880 | 1876 | 1872 |
| 1946 | 1944 | 1938 | 1936 |
| 1990 | 1988 | 1986 | 1984 |

This proves only local rank and overlap compatibility.  It does not embed
these twelve edges into one 369-vertex rainbow, factorable path.

### 6.2 Preferred route: put `958` at the seam

Choose the triple-defect alternative, with its unique late-triple defect away
from position 370.  Then all 368 internal portals are forced rank seven, so
twelve selected internal transitions may be assigned the twelve targets in
(6.1).  Require the seam to equal `958`.

There is no local OR obstruction.  For example, the six-entry fragment at
positions 368 through 373

\[
 (64,178,4,10,768,1)                           \tag{6.2}
\]

has the following consecutive OR rows:

\[
\begin{array}{c|c|c}
\text{length}&\text{OR values}&\text{ranks}\\ \hline
1&64,178,4,10,768,1&1,4,1,2,2,1\\
2&242,182,14,778,769&5,5,3,4,3\\
3&246,190,782,779&6,6,5,5\\
4&254,958,783&7,8,6.
\end{array}
\]

All short values displayed in (6.2) are distinct.  In particular,

\[
 R_3(369)=190,quad R_3(370)=782,quad
 R_2(370)=14,quad R_4(369)=190\cup782=958,     \tag{6.3}
\]

and the next selected lower-facing witness `R_4(370)=783` has rank six.
Thus a rank-eight seam is compatible with a rank-five `T_370`, a rank-three
shared pair, the all-rank-five early-pair regime, and the beginning of the
lower-facing rank-six block.

### 6.3 Alternative route: put `958` at the unique internal defect

The clean pair-defect grading can instead use its one exceptional early pair
for `958`.  The exact local edge is

\[
 190\cup798=958,qquad190\cap798=30,             \tag{6.4}
\]

where both endpoints have rank six and `30` has rank four.  Assigning the
unique defect pair the value `30` makes (6.4) the sole rank-eight internal
portal.  The twelve rank-seven targets can use ordinary transitions from the
table above.  This is also locally consistent and shows that the clean lower
grading itself survived the no-go theorem.

## 7. The unproved gates

The ledgers in Section 6 are not a deformation theorem.  A valid length-465
word still has to pass all of the following simultaneous gates.

1. **Single path embedding.**  The twelve Johnson edges and the optional
   exceptional edge must lie in one ordered 369-vertex path of distinct
   rank-six masks, with every other internal transition obeying the one-defect
   theorem.
2. **Rainbow lower overlaps.**  All 369 early pair values, all late pairs,
   all singletons, and all late triples must be globally distinct and must
   exhaust every rank-one through rank-five mask exactly once.  The local
   tables reserve compatible labels but do not complete this allocation.
3. **Common-factor realization and pins.**  The proposed rows must arise from
   one word `A`, satisfy every coordinate run/factorability constraint and
   coordinatewise pin survival, and have no empty entry.
4. **Lower-facing completion.**  The 93 windows
   `R_4(370),...,R_4(462)` must be the complementary rank-six masks in the
   required order, including the unique late defect in the seam-preferred
   route.
5. **Preservation or recertification of upper coverage.**  The thirteen masks
   in (6.1) are the omissions of a different fixed-delay factor.  After a
   single-switch deformation, previously covered masks need not remain
   covered.  One must either prove witness preservation or exhaustively
   re-establish every upper mask.

Accordingly the corrected claim is only this:

> The exact short-row rigidity permits a `12 rank-seven + 1 rank-eight`
> portal repair, and explicit local ledgers realize all thirteen target ORs
> with the required overlap ranks.  The global braid, factor, pins, and full
> coverage remain open.

That target matches the observed obstruction without contradicting the
forced derivative geometry.  The earlier `330+38+1` target did not.
