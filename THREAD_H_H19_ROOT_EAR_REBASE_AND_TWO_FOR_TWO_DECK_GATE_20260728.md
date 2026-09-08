# H19 root-ear rebases and the exact two-for-two deck gate

Date: 2026-07-28

Status: fixed-certificate audit.  The current H19 carrier is not improved in
this note.  The note proves (i) that none of its present root sockets already
contains duplicate native capacity, (ii) that every literal socket rebase is
deck-exact but fails protected controller grading, and (iii) that one
rank-preserving local controller rotation realizes the exact desired
Hall-18 critical-shore profile.  That rotation has an explicit two-for-two
middle-deck defect and an explicit two-rank exterior deficit.  No carrier
enumeration was run.

The frozen source is

~~~text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
SHA256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
~~~

The independently reconstructed route audit is

~~~text
scratch/audit_k15_h19_root8216_chain_independent.json
SHA256 71207dcfb6f02d7f5ac5e91bbf28863ca2831edd82b6a7de87ff39001ccd4c5d
~~~

The dedicated reproducibility checker is

~~~text
scratch/audit_k15_h19_root_ear_rotations.py
SHA256 3b4c25c9730226de8591abd90443df6626077e75e740842c5826b141cfedad73
~~~

It derives the socket and facet lists from the frozen carrier, checks the 28
oriented identities, and reconstructs the final compiler graphs.  It does
not import or invoke any carrier-enumeration routine.  Under the canonical
convention (comma-separated decimal masks, no terminal newline), the frozen
middle-path digest is

~~~text
97429bb3f25ccf921e794c1d20ed361684116823d0a14787634dc22af820e441
~~~

## 1. Definitions and the fixed H19 shore

Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad W=\binom{15}{8}=6435,
 \qquad N=\sum_{j=1}^{7}\binom{15}{j}=16383.
\]

Let \(T=(T_0,\ldots,T_{W-1})\) be the frozen rank-eight Johnson
carrier and let

\[
 P_j=\bigcap_{i=\max(0,j-3)}^{\min(W-1,j)}T_i
 \tag{1.1}
\]

be its maximal depth-three controller.  A depth-\(s\) native trace at
start \(p\), \(0\le s\le2\), is

\[
 \tau(p,s)=\bigcup_{j=0}^{s}P_{p+j}.                 \tag{1.2}
\]

The canonical deficient shore is \(X/Y=516/497\).  It consists of one
gap-two component, with set-theoretic intersection 8216 and missing native
targets 8217 and 8218, and seventeen unit-gap components.  The complete
missing-target set is

\[
\begin{split}
\mathcal R=\{&960,1103,2420,2575,2676,4213,5801,7504,8217,8218,\cr
             &9524,13616,13620,17683,17738,18970,19568,21641,29776\}.
\end{split}                                                   \tag{1.3}
\]

The 497 right-shore cells have pairwise distinct native traces equal to
\(X\setminus\mathcal R\).  Their depth census is

\[
\begin{array}{c|ccc}
s&0&1&2\\ \hline
\#&27&129&341.
\end{array}                                                   \tag{1.4}
\]

After reserving those 497 native cells, the targets outside \(X\) have an
exact matching of rank

\[
 15867=N-|X|,
 \qquad 497+15867=16364.                         \tag{1.5}
\]

## 2. There is no present duplicate-child or root occurrence

A **root socket** is a selected right-shore cell whose component-restricted
profile is exactly \(\{R,R+2^a\}\), whose native trace is \(R+2^a\), and
where \(R\in\mathcal R\).

### Theorem 2.1 (native multiplicity obstruction)

The H19 carrier has exactly 45 root sockets.  Every one of their 45 children
has native multiplicity exactly one among all 19,311 physical cells, and
every target in \(\mathcal R\) has native multiplicity zero among those
cells.  In particular, no duplicate-child/root split is already available.

There are 27 depth-zero sockets for the rank-four missing targets
\(960,8217,8218\), nine for each target.  The remaining 18 sockets are the
following depth-two rows; axes are zero based.

\[
\begin{array}{c|c|c|c|c|l}
R&R+2^a&a&p&\text{cell}&(P_p,P_{p+1},P_{p+2})\\ \hline
1103&5199&12&771&13646&(5196,5193,5131)\\
1103&1359&8&5559&18434&(1347,1291,1293)\\
2420&2932&9&3543&16418&(868,2884,2836)\\
2575&2607&5&4929&17804&(2601,2602,2604)\\
2676&10868&13&4458&17333&(10788,8804,8308)\\
4213&4221&3&1262&14137&(4204,4141,4156)\\
4213&5237&10&3172&16047&(5220,5157,5172)\\
4213&12405&13&4298&17173&(12340,8245,8293)\\
4213&4469&8&5239&18114&(357,341,4421)\\
7504&7512&3&1364&14239&(1368,2392,6232)\\
7504&7536&5&3105&15980&(4464,2416,1392)\\
7504&7506&1&3581&16456&(4434,2386,1362)\\
7504&15696&13&4951&17826&(12624,10576,9552)\\
9524&9588&6&4460&17335&(8308,9300,9552)\\
17683&21779&12&4449&17324&(5394,21762,20739)\\
18970&19226&8&5451&18326&(19202,18698,2330)\\
18970&19098&7&5525&18400&(19074,17042,666)\\
19568&27760&13&4944&17819&(10352,11360,25696).
\end{array}                                                   \tag{2.1}
\]

#### Proof

Form all literal unions (1.2), retaining cell labels.  Intersect each cell's
compiler profile with its rooted DM component.  Exactly the 45 cells just
described have two-point profile \(\{R,R+2^a\}\).  Counting the 19,311
literal unions by their masks gives multiplicity one for each displayed
child and multiplicity zero for every mask in (1.3).  This is a direct
finite certificate calculation, independent of the descent search. \(\square\)

Among the six minimal \(2/1\) components the optional axes are

\[
 9,5,13,6,12,13                                      \tag{2.2}
\]

for roots \(2420,2575,2676,9524,17683,19568\), respectively.
Thus axis 13 is the unique repeated minimal axis.  Its two socket starts are
4458 and 4944, separated by 486 positions.

## 3. Exact socket pivots, and why they are not protected root ears

For a socket \((R,R+2^a,p,s)\), define a literal rebase by

\[
 Q_j=P_j\cap R\quad(p\le j\le p+s),
 \qquad Q_j=P_j\quad\text{otherwise}.                 \tag{3.1}
\]

### Theorem 3.1 (all 45 pivots are deck-exact but rank-neutral)

For each of the 45 sockets, (3.1) preserves every four-controller-state
union:

\[
 Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}=T_i
 \quad(0\le i<W).                                    \tag{3.2}
\]

Among the 497 selected native traces it changes exactly the designated
child \(R+2^a\) to \(R\), and changes no other trace.  Consequently the
497 resulting traces remain distinct, but the operation is matching
neutral: the old child, rather than the root, becomes exposed.

For a rank-four root, one interior controller state changes from rank five
to rank four, both collar transitions have Hamming distance three, and the
coordinate-incidence change is \(\Delta p_a=-1\).  For a rank-six root,
three consecutive controller states change from rank five to rank four,
the two internal transitions retain Hamming distance two, both collar
transitions have Hamming distance three, and \(\Delta p_a=-3\).

#### Proof

In every socket all edited states contain \(a\).  The two exterior flanks
also contain \(a\).  Every length-four window meeting the edited interval
contains one of those flanks; deleting \(a\) inside the interval therefore
does not change that window's union.  All other coordinates and all
disjoint windows are untouched, proving (3.2).  Literal evaluation of the
497 selected intervals gives the asserted sole trace change.  The rank,
collar-distance, and incidence assertions follow immediately from deleting
the common coordinate \(a\) from respectively one or three rank-five
states. \(\square\)

For the repeated axis 13 rows, the two rebases are

\[
\begin{aligned}
(10788,8804,8308)&\longmapsto(2596,612,116),\\
(10352,11360,25696)&\longmapsto(2160,3168,17504).
\end{aligned}                                                 \tag{3.3}
\]

They change exactly \(10868\to2676\) and
\(27760\to19568\), respectively.  They compose deck-exactly, but still
only exchange two exposed children for two exposed roots.

### Lemma 3.2 (fixed-deck controller uniqueness)

Let \(Q\) be any controller satisfying the same ordered deck equations

\[
 T_i=Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}.
 \tag{3.4}
\]

Then \(Q_j\subseteq P_j\) for every \(j\).  At every fully interior
position, \(|P_j|=5\); hence if \(|Q_j|=5\), then \(Q_j=P_j\).

#### Proof

Every coordinate of \(Q_j\) belongs to each deck state whose four-window
contains position \(j\).  It therefore belongs to their intersection,
which is exactly (1.1).  Equality follows at equal rank. \(\square\)

Thus no controller-only compensation can turn any pivot in Theorem 3.1
into the **maximal rank-five controller** while keeping the middle carrier
fixed.  If a proposed repair is required to remain a maximal controller,
the incidence congruence

\[
 p_x\equiv\binom{14}{7}=3432\equiv0\pmod3                \tag{3.5}
\]

already rules out an uncompensated depth-zero pivot.  A depth-two pivot
passes (3.5), but fails rank and Johnson chronology.  Equivalently, native
grading requires a rank-six **maximal-controller native** root ear to occur
at depth one, not at the old depth-two child socket.  Such a native ear
therefore requires a rethreaded middle carrier.

This does not invalidate (3.1) as a literal lower-rank common word: all its
letters are nonempty and (3.2) is exact.  If a distinct duplicate child is
first supplied, Theorem 3.1 can be the exceptional common-word splitter.
What fails is only the stronger claim that the rebased word is the new
maximal Johnson controller or that the root pin is native in the graded
sense.

## 4. Rank-preserving one-state facet rotations

Let \(K\) be a positive rank-six unit-component root.  A shortest facet
configuration is

\[
 F=P_i,\quad M=P_{i+1},\quad F'=P_{i+2},
 \qquad F,F'\subset K,\quad F\ne F'.                  \tag{4.1}
\]

Then \(F\cup F'=K\).  The two one-state rotations are

\[
 L:(F,M,F')\mapsto(F,F',M),\qquad
 R:(F,M,F')\mapsto(M,F,F').                            \tag{4.2}
\]

Both preserve the complete controller-state multiset, and therefore all
coordinate incidences and the congruences (3.5).  Each creates a literal
depth-one root trace \(K\).

There are exactly fourteen configurations (4.1):

\[
\begin{array}{c|l}
K&i\\ \hline
2420&3104,3782,5481\\
2575&4310,4775\\
2676&2253,3034,3043\\
9524&2243,5346,6411\\
17683&760\\
18970&1976\\
19568&5391.
\end{array}                                                   \tag{4.3}
\]

### Theorem 4.1 (seven clean near-carriers and a universal deck defect)

Among the 28 oriented rotations in (4.2), exactly the following seven have
all of these properties:

1. the rotated controller retains every interior Johnson transition;
2. its four-window dilation \(T'\) has rank eight at every position and is
   a Johnson walk;
3. \(T'\) remains depth-three resident; and
4. the maximal erosion of \(T'\) is exactly the rotated controller.

\[
\begin{array}{c|c|c|c|c}
K&i&\mathrm{orientation}&\text{omitted middle states}&
       \text{duplicated middle states}\\ \hline
2420&3104&L&11640,12662&10614,13688\\
2420&3782&R&11122,19804&27474,3452\\
2575&4310&R&2983,10957&11173,2767\\
2676&3034&L&11220,18999&11158,19061\\
2676&3034&R&10966,19253&10996,19223\\
2676&3043&R&2791,27196&2806,27181\\
9524&6411&R&8700,11829&8956,11573.
\end{array}                                                   \tag{4.4}
\]

None is an exact middle-layer carrier: in every row, \(T'\) has exactly
6433 distinct states.  The two masks in the fourth column are absent and
the two masks in the fifth column occur twice.

#### Proof

Testing whether an interior controller state is a facet of one of the ten
positive rank-six roots gives exactly (4.3).  For each displayed pair the
two rotations (4.2) are literal three-mask identities.  The controller
Johnson test, the two changed four-window unions, their ranks, their two
adjacent middle transitions, maximal erosion, and residence are therefore
a fixed 28-row bitwise audit.  The seven passing rows give (4.4).
Counting the resulting middle masks in each passing row gives exactly the
two omissions and two repetitions displayed there. \(\square\)

This is not a carrier search: (4.3) fixes all candidates before the 28
constant-size identities are checked.

## 5. The unique upper-safe local ear

Among the seven rows of (4.4), exactly one retains complete upper support at
every depth \(1\le q\le7\): the \(K=2420,i=3782,R\) row.  Its controller
rotation is

\[
 (2416,18768,2388)\longmapsto(18768,2416,2388).        \tag{5.1}
\]

The new consecutive pair at positions 3783,3784 satisfies

\[
 2416\cup2388=2420,                                   \tag{5.2}
\]

so depth-one cell

\[
 c_\star=6438+3783=10221                              \tag{5.3}
\]

is a genuine native root ear.  Only two middle positions change:

\[
\begin{array}{c|c|c}
\text{position}&T& T'\\ \hline
3779&11122&27474\\
3783&19804&3452.
\end{array}                                                   \tag{5.4}
\]

The new masks are duplicate copies of the old masks at positions 537 and
3288, respectively.  Thus

\[
 \text{omitted}=\{11122,19804\},\qquad
 \text{duplicated}=\{27474,3452\}.                    \tag{5.5}
\]

### Theorem 5.1 (exact old-shore gap-18 profile of the near-carrier)

Let \(X/Y\) be the frozen H19 shore.  Under (5.1), all 497 old selected
native traces remain literally unchanged and distinct, and

\[
 N_{G'}(X)=Y\mathbin{\dot\cup}\{c_\star\}.             \tag{5.6}
\]

Consequently the old target shore already has the exact desired profile

\[
 |X|-|N_{G'}(X)|=516-498=18.                          \tag{5.7}
\]

The rotated walk is resident and retains all upper shadows.  Its lower-hole
vector is

\[
 (6,17,11,1,0,0,0).                                  \tag{5.8}
\]

#### Proof

An adjacent swap of controller positions \(j,j+1\) can change only the
four-windows starting at \(j-3\) and \(j+1\); this gives (5.4) directly.
Evaluation of the 497 fixed cell intervals shows that none changes.  The
new cell (5.3) has trace (5.2), and restriction of its profile to \(X\) is
the singleton \(\{2420\}\).  Evaluation of every other cell profile on
\(X\) gives no change, proving (5.6).  Literal shadow evaluation gives
(5.8) and zero upper holes. \(\square\)

This is the sharpest present **maximal-controller local-rotation** profile
target, but it is not H18.  The separate exceptional-common-word route is
to create a second occurrence of one of Theorem 2.1's unique children and
then apply Theorem 3.1.  With
the 498 cells in (5.6) reserved, the targets outside \(X\) have matching
rank only

\[
 15865=15867-2.                                        \tag{5.9}
\]

The two new zero targets are

\[
 10610=11122\setminus\{2^9\},\qquad
 19796=19804\setminus\{2^3\}.                         \tag{5.10}
\]

Accordingly the complete near-carrier graph has rank 16,363, not 16,365.
The two missing exterior ranks align exactly with the two omitted middle
states in (5.5).

## 6. Exact remaining compensation theorem

For this local lane, an H19-to-H18 endpoint will follow from a global
companion circulation satisfying all of the following exact conditions:

1. retain the root ear (5.2) and the other 497 native shore pins;
2. replace the duplicated middle-state supply in (5.5) by the two omitted
   states, producing every rank-eight state exactly once;
3. restore matching rank 15,867 on the targets outside \(X\), in particular
   restore service to 10610 and 19796;
4. retain (5.6), all upper shadows, residence, endpoint data, and the one
   common maximal controller; and
5. restore the required lower support, in particular reduce the first
   entry of (5.8) from six to the protected value four.

Then the 498 critical pins and the disjoint exterior matching give

\[
 498+15867=16365,                                      \tag{6.1}
\]

while (5.7) gives the reverse Hall bound, so the resulting carrier is
exactly H18.

The companion cannot be a direct substitution at the two remote duplicate
positions.  Their middle collars are

\[
\begin{array}{c|c|c}
p&T_{p-1}&T_{p+1}\\ \hline
537&27986&27504\\
3288&3446&9596.
\end{array}                                                   \tag{6.2}
\]

At position 537, substitution by 11122 has boundary distances \((4,2)\)
and substitution by 19804 has \((4,6)\).  At position 3288 the corresponding
distances are \((4,6)\) and \((4,4)\).  Hence neither assignment restores a
Johnson carrier.  A successful compensation must be a genuinely multistate
closed circulation.

This two-for-two circulation, with simultaneous restoration of the two
exterior ranks, is the smallest exact obstruction left by the strongest
local H19 root-ear rebase.
