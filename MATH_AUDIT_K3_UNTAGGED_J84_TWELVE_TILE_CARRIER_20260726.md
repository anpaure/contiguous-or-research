# Audit of the untagged (J(8,4)	imes Q_R) twelve-tile (k=3) carrier

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 \mathcal U=\binom{[8]}4\times
       \{uw,vw,vx,ux\},                              \tag{0.1}
\]

and measure pair type in

\[
            12\mid34\mid56\mid78\mid uv\mid wx.      \tag{0.2}
\]

The proposed twelve special tiles have the following status.

* Every displayed tile is a physical Q2 after the cyclic reorderings in
  Section 1.
* Their (48) special vertices are pairwise distinct.
* Replacing the four vertical reservoir cells over a tile by its four
  fixed-reservoir horizontal cells is an exact 16-owner trade.
* Dividing the tiles into three groups, each containing two (d=3) and
  two (d=2) tiles, gives eight literal exact factor corners on the same
  (280) owners.
* The lower mean displacement is (40) per bit and (120/280=3/7) in
  the all-new corner.
* One common phase colouring exists for all eight corners.

The first exact failure is the upper ledger.  Every proposed (d=3) tile
has lower signed vector

\[
                         2e_0-e_1-e_2,                \tag{0.3}
\]

but upper signed vector

\[
                         e_2-e_3.                     \tag{0.4}
\]

Thus its lower mean decrease is (3), while its upper mean decrease is
only (1).  A (d=2) tile has the matched vectors

\[
                         2e_0-2e_1,qquad
                         2e_1-2e_2.                   \tag{0.5}
\]

Consequently one proposed bit, containing two tiles of each kind and
repeated over four reservoir orientations, has

\[
 \Delta^-_{m bit}=32e_0-24e_1-8e_2,                \tag{0.6}
\]

\[
 \Delta^+_{m bit}=16e_1-8e_2-8e_3.                 \tag{0.7}
\]

Its lower mean decrease is (40), but its upper mean decrease is (24).
The all-new upper decrease is therefore (72/280=9/35), not (3/7).

The discrepancy is orientation-independent and cannot be repaired by a
different cyclic order of the same twelve squares.  A valid repair needs
additional upper-heavy tiles, naturally complements of the (d=3)
tiles, or a new complement-balanced retile.  The displayed 48-vertex
family is not complement-closed, so simply invoking complementation does
not prove the missing upper formula.

## 1. Physical cyclic orders

The six (d=3) tiles are already in cyclic order:

\[
\begin{aligned}
A_1&=(1234,1346,1356,1235),&&(2\leftrightarrow6, 4\leftrightarrow5),\\
A_2&=(1245,2345,2356,1256),&&(1\leftrightarrow3, 4\leftrightarrow6),\\
A_3&=(1238,2348,2478,1278),&&(1\leftrightarrow4, 3\leftrightarrow7),\\
A_4&=(3456,3567,3578,3458),&&(4\leftrightarrow7, 6\leftrightarrow8),\\
A_5&=(3467,4567,4578,3478),&&(3\leftrightarrow5, 6\leftrightarrow8),\\
A_6&=(1258,2568,5678,1578),&&(1\leftrightarrow6, 2\leftrightarrow7).
\end{aligned}                                        \tag{1.1}
\]

The pairs on the right are the two disjoint Johnson swaps.

The six (d=2) braces become physical Q2 cycles in the following orders:

\[
\begin{aligned}
B_1&=(1257,1357,3457,2457),&&(2\leftrightarrow3, 1\leftrightarrow4),\\
B_2&=(1236,1368,3678,2367),&&(2\leftrightarrow8, 1\leftrightarrow7),\\
B_3&=(1248,1458,4568,2468),&&(2\leftrightarrow5, 1\leftrightarrow6),\\
B_4&=(1348,1358,1568,1468),&&(4\leftrightarrow5, 3\leftrightarrow6),\\
B_5&=(1347,1367,1567,1457),&&(4\leftrightarrow6, 3\leftrightarrow5),\\
B_6&=(2347,2357,2567,2467),&&(4\leftrightarrow5, 3\leftrightarrow6).
\end{aligned}                                        \tag{1.2}
\]

Every adjacent pair in (1.1)--(1.2) differs by one displayed swap, and
opposite edges repeat the same direction.  Hence all twelve cells are
literal physical Q2s.

The displayed 48 four-sets are pairwise distinct.  This can be checked
without an incidence search: within a row the Q2 vertices are distinct;
between rows, comparison of the common two-coordinate cores and the two
fixed-absent coordinates separates every possible coincidence, and direct
comparison of the few rows sharing the same absent pair leaves disjoint
listed four-sets.  Thus the twelve tile supports are disjoint.

## 2. Exact lower discrepancies

For a special four-set (X), let (f(X)) be its number of full pairs
among (12,34,56,78).  In the all-vertical base factor, the reservoir
square over (X) has four lower edges, all of type (f(X)).

For every (A_i), the four vertex types are

\[
                         f_2+3f_1,                   \tag{2.1}
\]

while its four horizontal edge intersections have types

\[
                         2f_1+2f_0.                  \tag{2.2}
\]

For example, (A_1) has vertex types

\[
 f(1234),f(1346),f(1356),f(1235)=2,1,1,1,            \tag{2.3}
\]

and intersection triples

\[
                         134, 136, 135, 123        \tag{2.4}
\]

of types (1,0,0,1).  The other five (A_i) have the identical pattern.
Thus one fixed-reservoir horizontal square has new-minus-old vector (0.3)
and mean decrease (3).

For every (B_i), two vertices have type one and two have type zero,
while all four horizontal intersections have type zero.  Hence its
new-minus-old vector is the lower vector in (0.5), of mean decrease (2).

The actual 16-owner trade repeats the horizontal square at four reservoir
orientations.  Therefore all signed vectors above acquire a factor four.
Two (A)- and two (B)-tiles in one bit give (0.6), with mean decrease

\[
                         4(2\cdot3+2\cdot2)=40.       \tag{2.5}
\]

Three disjoint groups give all-new lower decrease (120), namely (3/7)
of the (280) occurrences.

For reference, the base all-vertical lower ledger on all 70 special
four-sets is

\[
                         64f_0+192f_1+24f_2.          \tag{2.6}
\]

Indeed the numbers of special four-sets with zero, one, and two full pairs
are (16,48,6), and every vertical cell contributes four edges.  After
all three bits, the lower ledger becomes

\[
                         160f_0+120f_1.               \tag{2.7}
\]

This independently confirms the mass (280) and mean decrease (120).

## 3. Exact factor cube

For one special tile (Q), the base factor has four vertical cells

\[
                         \{X\times Q_R:X\in Q\}.      \tag{3.1}
\]

They partition (Q\times\mathcal Y).  The switched shore has four
horizontal cells

\[
                         \{Q\times\{Y\}:Y\in\mathcal Y\},          \tag{3.2}
\]

which partition the identical sixteen owners.  Thus the replacement is
an exact four-for-four completed Q2 trade.

Because the twelve special tile supports are disjoint, their switches are
independent.  Put, for example,

\[
\begin{aligned}
\mathcal G_1&=\{A_1,A_2,B_1,B_2\},\\
\mathcal G_2&=\{A_3,A_4,B_3,B_4\},\\
\mathcal G_3&=\{A_5,A_6,B_5,B_6\}.
\end{aligned}                                        \tag{3.3}
\]

Each group has lower discrepancy (10) before the reservoir factor four.
Switching the four tiles in a group defines one bit.  At every corner,
the twelve tile supports contribute (12\cdot4=48) Q2 cells, while the
remaining (70-48=22) special states contribute vertical reservoir
squares.  Hence every corner contains

\[
                         48+22=70                    \tag{3.4}
\]

physical Q2s and covers all (70\cdot4=280) owners exactly once.

## 4. The upper-ledger failure

For an (A_i), the old vertical upper types are the vertex types shifted
by one reservoir full pair:

\[
                         3f_2+f_3.                   \tag{4.1}
\]

All four horizontal special unions have exactly two full special pairs,
so the new upper ledger is

\[
                         4f_2.                       \tag{4.2}
\]

The upper new-minus-old vector is therefore (0.4), whose mean decrease is
one.

For a (B_i), the old upper ledger is

\[
                         2f_1+2f_2,                  \tag{4.3}
\]

and every horizontal union has one full special pair, giving (4f_1).
This is the upper vector in (0.5), with mean decrease two.

Thus two tiles of each kind give, before the reservoir repetition,

\[
 2(e_2-e_3)+2(2e_1-2e_2)
 =4e_1-2e_2-2e_3.                                    \tag{4.4}
\]

Multiplication by four proves (0.7).  Its weighted mean is (-24), not
(-40).

This failure cannot be altered by rotating or reversing a Q2 cycle:
intersections and unions are the same four undirected edges.  The only
standard route to matched two-sided action is complement balance.  The
complement of an original upper edge is a lower edge in the complementary
tile, so pairing every tile with a disjoint complementary tile would pair
lower-heavy and upper-heavy discrepancies.  The proposed 48-state support
is not complement-closed; for example

\[
                         1234^c=5678\in A_6,
 \qquad                   1346^c=2578\notin\bigcup_i(A_i\cup B_i).  \tag{4.5}
\]

Hence no complement argument applies to the displayed cube.  Constructing
a disjoint complement-balanced retile is additional work.

## 5. Common phase

Despite the upper failure, common phase presents no obstruction.  Since
the twelve special tile supports are disjoint, define

\[
                         g: \binom{[8]}4\to\mathbb Z_4               \tag{5.1}
\]

by assigning (0,1,2,3) around each cyclic order in
(1.1)--(1.2), and assign arbitrary values on the 22 unused special states.
Let the reservoir orientations be

\[
                         y_0=uw, y_1=vw, y_2=vx, y_3=ux,          \tag{5.2}
\]

and colour

\[
                         c(X\cup y_j)=g(X)+j\pmod4.  \tag{5.3}
\]

Every vertical reservoir cell is cyclically coloured.  Every switched
horizontal cell at fixed (y_j) inherits the cyclic order of its tile,
shifted by (j).  Thus the same owner colouring is phase-compatible with
all cells in all eight factor corners.

The coloured-square suspension therefore produces common-support
all-length factors.  It does not repair the unequal lower and upper signed
ledgers.

## 6. Exact boundary

Proved for the proposed (J(8,4)) carrier:

1. all twelve special tiles are physical and vertex-disjoint;
2. the eight factor corners have literal one-copy ownership;
3. the lower ledger is affine with (3/7) all-new mean death;
4. one common phase exists and suspends every corner.

Refuted:

* the same (3/7) action in the upper ledger;
* matched lower/upper affine seed vectors for the displayed groups; and
* any complement proof based on the displayed 48-state support.

The first exact repair gate is a complement-balanced disjoint tile family,
or an alternative grouping containing upper-heavy tiles which contributes
an additional (16) units of upper mean decrease per bit without changing
the lower target.
