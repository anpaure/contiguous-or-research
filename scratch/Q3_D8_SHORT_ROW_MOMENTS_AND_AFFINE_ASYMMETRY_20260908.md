# Endpoint moments and asymmetry constraints for ternary short rows

2026-09-08. Cover-selectors. Pure finite mathematics; no computation or
optimization. The affine-repair conclusions concern the167-short-row
proposal only. They do not exclude the separate construction using four
full geodesic repair rows and164 short rows.

## 1. Exact excess measures and a two-step transport

A short row consists of two four-axis saturated chains C_r,D_s, with
one member at each rank1,...,7. Its six rank7 targets and six rank9
targets are canonically paired by

    (C_r,D_(7-r)) -> (C_(r+1),D_(8-r)),  1<=r<=6.     (1)

Each arrow increases one coordinate in each shore by one. The two
increased coordinates are distinct. This is an actual bijection of the
two row decks, not just a comparison of their cardinalities.

Let Q_r be the whole ternary eight-cube rank r, and R_r the affine
repair's DISTINCT rank-r targets. Both R_7 and R_9 have16 members.
If167 short rows cover Q_r minus R_r, their1002 occurrences at each
rank r=7,9 can be written uniquely as a multiset

    M_r = 1_(Q_r minus R_r) + E_r,   |E_r|=2.          (2)

An occurrence on R_r is an excess, as is an additional occurrence of
an unrepaired target. Thus E_r is an actual nonnegative multiset of
two points, not merely two formal rank defects.

## 2. First and last axes are separately determined

Let F_a count the short-row shores whose first increment is on axis a,
and L_a count those whose last increment is on a. Each row has two
first and two last axes, so

    sum_a F_a = sum_a L_a = 334.                      (3)

For any function f of a coordinate on the C shore, telescoping gives

    sum_(row rank9) f(x_a) - sum_(row rank7) f(x_a)
      = f(C_7(a))-f(C_1(a)).                         (4)

The first shore member is e_first and the last is2*1-e_last. For
g_+(u)=1{u>0} and g_2(u)=1{u=2}, (4) is respectively

    1-1{a=first},             1-1{a=last}.             (5)

For the whole cube the corresponding differences are both127. For
g_2 this is the coefficient difference W_3(7,7)-W_3(7,5)=393-266;
g_+ gives the same answer because the other intermediate-rank terms
cancel. The affine repair contributes two to each difference at every
coordinate. Indeed, its shore ranks are0,1,2,6,7,8; subtracting the
rank7 pairs from the rank9 pairs leaves the rank2 and rank8 members
minus ranks0 and6. For either indicator this is the first-axis indicator
plus the last-axis indicator. Every coordinate occurs exactly once in
each role among the four affine repair rows.

Therefore the residual differences are125, and (2)–(5) imply

    F_a = 42 - E_9[g_+(x_a)] + E_7[g_+(x_a)],
    L_a = 42 - E_9[g_2(x_a)] + E_7[g_2(x_a)].           (6)

Both F_a and L_a are integers between40 and44. Adding (6) recovers
the root's identity

    F_a+L_a = 84 - E_9[x_a] + E_7[x_a].               (7)

Subtracting them determines the endpoint imbalance from the excess
ones at EACH coordinate. Summing (6) over coordinates additionally
shows that the two E_9 points have exactly two more twos and two fewer
zeros than the two E_7 points. Their total numbers of ones are equal.
This last aggregate condition is already visible to a complete
histogram census; the separate coordinate degrees in (6) are stronger.

One immediate integrality guard is independent of the repair: a multiset
of N short rows invariant under a coordinate-transitive group must have
equal first-axis degrees, so8 divides2N. Hence N is a multiple of four.
A coordinate-transitive167-row short bank is impossible.

## 3. Pair moments and the affine bias

Put y_a=x_a-1. For a pair a,b on the SAME shore of a short row,
telescoping gives

    Delta_ab = sum_rank9 y_a y_b - sum_rank7 y_a y_b
      = 1{first in {a,b}} - 1{last in {a,b}}.          (8)

For opposite-shore a,b, the pairing (1) gives an exact formula. If
alpha_r is the indicator that C_r to C_(r+1) increments a, and beta_r
the indicator that D_(7-r) to D_(8-r) increments b, then

    Delta_ab = sum_(r=1)^6 [
       alpha_r (D_(7-r)(b)-1)
       + beta_r (C_r(a)-1) + alpha_r beta_r ].         (9)

At most four paired cells are affected, since each coordinate increments
at most twice. If both increments occur in one cell, each pre-increment
centered value is -1 or0, so its whole contribution is -1,0,or1.
Thus |Delta_ab|<=4. Formula (9) records genuine internal-order information
which is not determined by the target histogram alone.

For the affine repair, let S_a be the four-axis shore on which a is a
first axis, and T_a its shore in its last-axis row. Define

    d_ab = 1{b in T_a} - 1{b in S_a}.

The repair's centered pair difference is exactly

    R_ab = 4(d_ab+d_ba).                             (10)

To check this, a repair row contributes4 times the last-axis indicators
of a,b to the uncentered product x_a x_b when they share a shore, and
4 times their first-axis indicators when they are on opposite shores.
Sum over the repair rows, then subtract the two coordinate first-moment
differences, each equal to four. This yields (10).

In the literal affine repair,

    S_0=0246, T_0=0123, S_1=1357, T_1=0145,

so d_01=d_10=1 and R_01=8. The full cube's centered pair difference
is zero by complementation. Any167-row completion must consequently obey

    sum_short Delta_01 = -8 + E_9[y_0y_1]-E_7[y_0y_1]
                       in [-12,-4].                 (11)

It cannot have zero difference on every coordinate pair. More generally,
(10) supplies an exact prescribed pair-moment vector up to the two
excess points at each rank. Every short row has sum_(a<b) Delta_ab=0:
the total centered rank is -1 or1 and the total change in the number
of one-valued coordinates is zero. Thus a proposed design with the
SAME pair difference on every coordinate pair would force all of them
to be zero, contrary to (11).

## 4. The affine adjacent decks are disjoint after reflection

Write bar(x)=2*1-x. Then

    R_9 intersect bar(R_7) = empty.                  (12)

Here is a direct physical-support proof. Each repair point on either
rank has exactly one coordinate equal to one. Fix that coordinate a.
The first-axis shore S=S_a and last-axis shore T=T_a belong to distinct
repair rows, because a row's first and last axes are different. All
cross-row shores in the affine repair intersect in exactly two points,
so |S intersect T|=2 and a lies in their intersection.

Let b be the OTHER shore's last axis in a's first-axis row, and c the
OTHER shore's first axis in a's last-axis row. The two possible supports
of the twos in R_9 with one-coordinate a are

    S^c,                   (T minus {a}) union {c}.

The two possible supports of the twos in bar(R_7) are

    T^c,                   (S minus {a}) union {b}.

The complete shores S^c,T^c differ because S!=T. A complete complement
cannot equal the other expression containing three points of its own
shore. Finally an equality between the two mixed expressions would
give a four-set containing (S union T) minus {a}, which has five points.
All four comparisons fail. Since the one-coordinate identifies a,
this proves (12) for the entire decks.

## 5. Complement-closed designs need at least170 short rows

Suppose a short-row multiset is closed under bar, including reflected
row pairs or self-reflecting rows. Its rank9 occurrence multiset is
the reflection of its rank7 multiset. To cover both affine residual
decks, its rank7 support must therefore contain

    (Q_7 minus R_7) union (Q_7 minus bar(R_9)) = Q_7,

where equality uses (12). Thus its rank7 occurrences must cover all1016
targets. Six targets per short row give

    N >= ceil(1016/6) = 170.                         (13)

This excludes every complement-closed167-row completion, not just a
particular pairing scheme. In particular83 complementary row pairs
plus one self-reflecting row cannot work for the affine repair.

A quantitative version applies to arbitrary167-row completions. Cancel
all available reflected row pairs and self-reflecting rows, leaving d
rows. Each remaining row can contribute at most six units of positive
mass to M_9-bar(M_7). By (2),

    M_9-bar(M_7)
      = 1_bar(R_7) - 1_R_9 + E_9-bar(E_7).

On the16-point set bar(R_7), the first two terms are uniformly +1 by
(12), and bar(E_7) can remove at most two units. Positive mass is at
least14. Hence6d>=14 and d>=3. Any successful167-row design must retain
at least three asymmetric rows after this cancellation.

These are obstructions to specified symmetries, not a proof that an
arbitrary167-row affine-residual cover is impossible.

## 6. Check on the newer four-full-plus164-short proposal

The separate proposal uses four FULL geodesic rows as repair, not the
four nonsaturated affine rows above. Each full row has eight targets
at each of ranks7 and9. Four such rows plus164 short rows have exactly
32+984=1016 occurrences at each critical rank, so any full cover must
be exact on those ranks.

For a full balanced row, the analogues of (5) are both one at every
coordinate: the relevant telescoping endpoints are rank0 and rank8.
The four full rows therefore contribute four to each indicator
difference. Since the whole-cube differences are127, the164 short rows
must satisfy

    F_a = L_a = 164-(127-4)=41  for every a.           (14)

This is consistent with a coordinate-transitive164-row orbit family.
Neither (12) nor the170-row obstruction applies to this different repair.
Equation (14) is a useful exact check on any proposed physical candidate.
