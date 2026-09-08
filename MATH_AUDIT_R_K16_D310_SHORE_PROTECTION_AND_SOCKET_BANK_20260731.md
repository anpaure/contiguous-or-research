# K16 `d310…` shore protection and exact socket bank

Date: 2026-07-31  
Lane: R, fixed-carrier compiler geometry  
Status: proved fixed-schedule reduction; the legal rethread realizing the socket changes remains open

## 1. Frozen input and scope

The target order is

`scratch/k16_seed0_def4_endpoint_transport_upper1_targets_20260731.word`

with SHA-256

`d310b08fddfdd49d019d9a656350377c4d2695ae972e6be8ebac8c7ae99b430f`.

It is obtained from the authenticated def4 order of SHA-256

`0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b`

by three successive strict-suffix reversals after zero-based cuts

\[
6173,\quad 11009,\quad 1004,
\]

in that order.  The deterministic materializer is
`scratch/materialize_r_k16_def4_endpoint_transport_upper1_20260731.py`.

The schedule throughout this note is fixed:

\[
X=\{5288,12871,12872\},\qquad Y=\{0,1,1007\}.
\]

The source audit is
`scratch/k16_seed0_def4_endpoint_transport_upper1_maxpq_hall_20260731.audit.json`,
file SHA-256

`5bfc1eee2e9ab926670a98a546380fb3beac9d3f325f844ec2bcbfbcfaea10e9`,

and embedded payload SHA-256

`7133ee304d07b6ff3bbcaa4304c465fc1dee7ad2852a026035de2dc34c87f81b`.

An independent rebuild of the maximal envelopes, all length-at-most-three
proper-prefix cells, the matching, and the alternating shore reproduced every
displayed array below.  This note proves a criterion and a conditional repair
bank for this carrier and schedule.  It does not assert that a legal Johnson
rethread realizing the required profile changes exists.

## 2. Exact one-cell compatibility criterion

Let the rank-eight targets in order be \(T_0,\ldots,T_{12869}\).  The fixed
schedule assigns row \(i\) a start \(s_i\) and deadline \(d_i\), and its maximal
physical envelope at position \(p\) is

\[
E_p=\bigcap_{i:s_i\le p\le d_i}T_i.
\]

For a physical interval \(I=[a,a+\ell-1]\), \(1\le\ell\le3\), put

\[
A_I=\bigcup_{p\in I}E_p.
\]

For a row bit \(b\in T_i\), let

\[
H_i(b)=\{p\in[s_i,d_i]:b\in E_p\}.
\]

Define the mandatory mask

\[
M_I=\bigcup\{\{b\}: I\cap[s_i,d_i]\ne\varnothing,
                 \ H_i(b)\subseteq I\}.
\]

Here every \(H_i(b)\) is nonempty because the maximal envelopes replay the
middle row.

**Lemma 2.1 (exact one-cell criterion).**  A nonempty lower target \(Q\) can
be installed on \(I\), leaving all positions outside \(I\) maximal, if and
only if

\[
Q\subseteq A_I,\qquad M_I\subseteq Q,\qquad
E_p\cap Q\ne\varnothing\quad(p\in I).                 \tag{2.1}
\]

**Proof.**  Necessity of the first and third conditions follows from a
nonzero letter at every position and union exactly \(Q\).  If a row bit has
all its hosts inside \(I\), deleting it from every letter in \(I\) destroys
that middle row, proving necessity of \(M_I\subseteq Q\).  Conversely set the
letter at \(p\in I\) equal to \(E_p\cap Q\).  The third condition makes every
letter nonzero, the first makes their union \(Q\), and the mandatory condition
leaves every row bit either in the capped interval or at an unchanged host
outside it.  Thus every middle row still replays.  \(\square\)

For several possibly overlapping cells, the exact condition is obtained by
introducing one physical letter \(c_p\subseteq E_p\) at every affected
position and imposing, simultaneously,

\[
c_p\ne0,qquad \bigcup_{p\in I_j}c_p=Q_j,qquad
\bigcup_{p=s_i}^{d_i}c_p=T_i.                         \tag{2.2}
\]

Equation (2.2), not separate uses of (2.1), is the necessary-and-sufficient
test when cells overlap or share middle rows.

## 3. The exact 30-versus-25 shore

The fixed candidate graph has 26,332 lower targets, 30,029 cells, 358,086
incidences, maximum matching size 26,327, and deficiency five.  Its exact
alternating Hall shore has 30 targets and 25 cells.

The four isolated zero-host targets are

\[
Z=\{\mathtt{29cc},\mathtt{38c6},\mathtt{8000},\mathtt{898d}\}.
\]

Removing them leaves the same 26-versus-25 component rooted at
\(\mathtt{0169}\):

\[
\begin{split}
C=\{&0169,016b,017b,01e9,01eb,0369,03e9,0569,056b,0769,
0969,096b,0979,09e9,0b69,0d69,11e9,1969,\\
&8169,816b,8179,81e9,8369,8569,8969,9169\}.
\end{split}
\]

The 25-cell neighborhood is

\[
\begin{split}
N=\{&346,1381,1963,2290,4450,8030,8078,8080,8897,10958,
16346,17494,20132,20630,21582,\\
&26900,26901,26902,28082,28132,28257,28672,29304,29918,29968\}.
\end{split}
\]

Thus the deficiency decomposes exactly as four isolated units plus one unit
from \(C\).

## 4. Exact shore protection

For each of the 25 displayed cells, keep its presently certified mate in
\(C\).  By Lemma 2.1, checking (2.1) for those 25 target-cell pairs after a
rethread is necessary and sufficient for this particular 25-edge matching to
survive.  A convenient stronger, purely positional certificate is to leave
the following 197 target rows unchanged:

\[
\begin{gathered}
[169,175], [686,693], [977,984], [1092,1102], [1812,1822],\\
[3005,3016], [3021,3032], [3294,3305], [3981,3992],\\
[6027,6034], [6601,6608], [7920,7927], [8169,8176],\\
[8645,8652], [11304,11312], [11895,11902], [11920,11927],\\
[11983,11989], [12190,12197], [12506,12513],\\
[12813,12820], [12838,12845].                         \tag{4.1}
\end{gathered}
\]

These are the exact second-order row supports needed to determine the 25
profiles.  Therefore equality of the old and new target order on (4.1)
preserves all 25 edges.  This is sufficient, not necessary; direct profile
testing is less restrictive.

## 5. A five-debt socket bank

All masks below are hexadecimal.  Each row records
\((Q;\text{cell};(a,\ell);A_I;M_I;(E_p)_{p\in I})\).

\[
\begin{array}{c|r|c|c|c|c|c}
Q&\text{cell}&(a,\ell)&A_I&M_I&(E_p)&\text{current defect}\\ \hline
0169&14790&(5265,1)&00e9&0021&(00e9)&\text{missing }0100\\
898d&14834&(5279,3)&098d&0989&(008d,080d,090c)&\text{missing }8000\\
8000&30023&(5288,1)&a071&0001&(a071)&\text{forced }0001\\
29cc&18620&(7169,2)&89cc&0884&(89c8,81cc)&\text{missing }2000\\
38c6&19715&(7717,1)&18c6&00c0&(18c6)&\text{missing }2000.
\end{array}                                                   \tag{5.1}
\]

Cells 14790, 14834, 30023, and 19715 are free in the certified maximum
matching.  Cell 18620 is matched to \(898c\), but \(898c\) has the free exact
host cell 24271 at \((9995,1)\), with profile

\[
A=M\mathbin{\mathop{\rm-free}}=898c,qquad M=0008,qquad E=898c.
\]

More explicitly, after the five new compatibilities in (5.1) are created,
the following five augmenting paths are pairwise vertex- and cell-disjoint:

\[
\begin{array}{rcl}
1969&\to&8030\ [\text{old mate }0969]
       \to346\ [\text{old mate }0169]\to14790,\\
29cc&\to&18620\ [\text{old mate }898c]\to24271,\\
38c6&\to&19715,\\
8000&\to&30023,\\
898d&\to&14834.
\end{array}                                                   \tag{5.2}
\]

The last cell of every line is free.  Hence (5.2) augments the certified
matching five times and saturates all 26,332 lower targets.

**Theorem 5.1 (conditional exact Hall closure).**  Let \(T'\) be any new
rank-eight target order under the same schedule.  Suppose:

1. its maximal envelopes replay every middle target;
2. the old compatible edges used at cells 8030 and 346, and more generally
   the unchanged part of the certified matching, remain compatible;
3. the five new target-cell pairs in (5.1) satisfy (2.1), jointly satisfy
   (2.2) wherever their row supports interact, and cell 24271 remains an
   exact host for \(898c\).

Then the full static lower candidate graph for \(T'\) has a perfect matching.

**Proof.**  Toggle the five pairwise-disjoint augmenting paths (5.2).  All
unchanged matching edges remain valid by hypotheses 1--2; every new edge is
valid by hypothesis 3.  The matching cardinality rises from 26,327 to 26,332.
\(\square\)

The dependency-row supports of the five new sockets are

\[
[5259,5268],\quad[5273,5284],\quad[5282,5289],\quad
[7164,7171],\quad[7712,7718].                              \tag{5.3}
\]

They are disjoint from (4.1).  The first three form one short physical
cluster.  Consequently a local multi-seam braid may alter all three without
touching the old 25-cell shore; the other two sockets occupy two further
local regions.  This leaves, at the level of support counting, a fourth seam
region available to create the sole missing upper mask \(a9fe\).

## 6. Exact remaining construction gate

The carrier is already q1-complete and misses exactly one upper mask,
\(\mathtt{a9fe}\).  Theorem 5.1 does not construct the needed rethread.  A
successful move must simultaneously satisfy:

- Johnson adjacency and one connected target path;
- complete q1 and arbitrary-width upper coverage, including a literal
  interval for \(a9fe\);
- the same P/Q schedule, or another schedule with its Hall graph rebuilt;
- exact middle replay;
- the five profile changes of (5.1), with multi-cell replay (2.2);
- preservation of the matching edges used in (5.2), directly or through an
  independently audited replacement set.

Thus the precise constructive target is a three-cluster-plus-upper
four-cut braid.  The socket bank proves that no further abstract Hall
obstruction remains once those local profile changes are realized, but it
does not prove that the braid exists.

