# K=11 canonical splice attack: corrected tail ledger and a full 32-hole transversal

Date: 2026-07-25

## 1. Status and scope

This note does **not** construct a universal word of length (465), and it
does not prove that no such word exists.  It repairs a second transcription
gap in the canonical-splice ledger and then closes the entire
**backward-tail Hall problem** for the thirty-two currently certified
missing four-colours.

The certified global numerical status therefore remains

\[
465\leq \nu(11)\leq477.
\]

Write `A` for the coordinate (10).  Let

\[
\begin{aligned}
\mathcal H_0={}&\{0147,0169,0237,0247,0256,0257,0258,025A,\\
&0347,0369,0469,0478,0479,047A,0489,0569\},\\
\mathcal H_1={}&\{1269,347A,1369,136A,1459,1469,1478,1479,\\
&158A,2369,247A,257A,2589,258A,259A,267A\},
\end{aligned}
\tag{1.1}
\]

and put (mathcal H=\mathcal H_0\sqcup\mathcal H_1).
This is the corrected family obtained from the old list by replacing
(127A) by (347A).

The A--B symbolic audit, the complete C--D window lists, and the corrected
E window table together prove that **every member of (mathcal H) is
absent** from the canonical cyclic-four support.  In class E the only member
of the old list that occurs is (127A), in row E8; it has been removed from
(1.1).  None of the displayed E windows is (347A).  The independent full
positive certificate
`K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md`
now proves the converse as well: (1.1) is exactly the 32-set complement and
the initial lower and complementary-upper supports are both exactly 298.

For a cyclic five-window

\[
(x_0,x_1,x_2,x_3,x_4),
\]

write

\[
\Delta_j=\{x_0,x_1,x_2,x_3,x_4\}\setminus\{x_j\},
\qquad j=1,2,3.
\tag{1.2}
\]

Since every C in H is genuinely missing, the seven five-sets C+beta,
with beta outside C, lie in seven distinct canonical wreaths and beta is
internal in its owner window.  Hence every C in H has exactly seven
tail-wreath incidences of the form
(1.2).

## 2. Four missing class-E incidences

The class-E deletion table in
`K11_CANONICAL_CYCLIC4_SUPPORT_HAND_AUDIT_20260725.md` omits the following
four entries.  Each is visible in one displayed cyclic order.

\[
\begin{array}{c|c|c|c}
\text{row}&\text{five-window}&\text{deletion}&\text{missing colour}\\ \hline
E9 &(5,2,1,A,8)&\Delta_1&158A\\
E13&(6,4,3,1,A)&\Delta_1&136A\\
E14&(5,3,1,A,8)&\Delta_1&158A\\
E14&(3,1,A,8,6)&\Delta_3&136A
\end{array}
\tag{2.1}
\]

For example,

\[
(5,2,1,A,8)-2=158A,
\qquad
(3,1,A,8,6)-8=136A.
\]

Thus the corrected class-E row degrees are

\[
\boxed{0,6,6,7,7,6,6,7,7,4,10,10,6,4},
\tag{2.2}
\]

whose sum is (86), not (82).  The maximum remains (10), attained by
E11 and E12.

There is a useful independent check.  The reflection

\[
\sigma(0)=0,
\qquad \sigma(x)=11-x\quad(1\leq x\leq10)
\tag{2.3}
\]

preserves the factor and sends (136A\leftrightarrow158A).  The two newly
restored occurrences of each colour are therefore forced in reflected
pairs.

## 3. Complete class-A internal-deletion table

Direct substitution in the fourteen displayed class-A orders gives the
following complete table.  Entries in one cell can occur at different
cyclic starts; the column records the deleted internal position.

\[
\begin{array}{c|l|l|l|r}
\text{row}&\Delta_1\cap\mathcal H&\Delta_2\cap\mathcal H
&\Delta_3\cap\mathcal H&d\\ \hline
A1&--&--&--&0\\
A2&0169&267A,0469&247A&4\\
A3&047A,136A&2369,247A&1369,2589,0478&7\\
A4&0479&259A,047A&247A&4\\
A5&247A,0489,1369&258A,0369&257A,0169&7\\
A6&0347,2369,258A&1479,2589&0147,158A&7\\
A7&259A&1478,257A,0569&267A&5\\
A8&2369,257A&1369,258A&1469,2589&6\\
A9&2589,267A,0147&--&1459,2369,047A&6\\
A10&--&257A&259A&2\\
A11&259A,1478&2369,267A,0169,0478&0147&7\\
A12&2589,0169&0147,247A,259A&347A,258A,0569&8\\
A13&267A,0169,1459&257A&0147,0489&6\\
A14&258A,0147,1469&1479,0469&0479,0169&7
\end{array}
\tag{3.1}
\]

The class-A incidence total is therefore

\[
\boxed{76},
\qquad
\boxed{\Delta_A=8}.
\tag{3.2}
\]

Two entries in (3.1) are particularly useful checks on transcription:

\[
(9,0,1,3,6)-1=0369\quad(A5,\Delta_2),
\]

\[
(9,0,1,4,6)-1=0469\quad(A14,\Delta_2).
\tag{3.3}
\]

These are easy to miss if the tuple is read as a sorted set before the
deleted position is recorded.

The previously audited totals for the other classes are

\[
17\quad(B),
\qquad
15+30=45\quad(C\cup D).
\tag{3.4}
\]

Combining (2.2)--(3.4) gives

\[
76+17+45+86=224=32\cdot7.
\tag{3.5}
\]

Because every listed value is a genuine incidence and the
seven-distinct-tail theorem supplies exactly (32\cdot7) incidences, (3.5)
also proves that the corrected A--E internal-deletion tables are complete.
The global right degree is

\[
\boxed{\Delta_{\rm tail}=10}.
\tag{3.6}
\]

Consequently the elementary vertex-cover estimate already gives a tail
matching of size at least

\[
\left\lceil\frac{224}{10}\right\rceil=23.
\tag{3.7}
\]

The next section proves much more without invoking Hall's theorem.

## 4. An explicit matching saturating all thirty-two holes

The following table assigns every (C\in\mathcal H) to a different tail
wreath containing an internal deletion equal to (C).  The (j) column is
the deleted position in (1.2).

\[
\begin{array}{c|c|c@{\qquad}c|c|c}
C&\text{tail row}&j&C&\text{tail row}&j\\ \hline
136A&E2&1&0147&C1&2\\
259A&E3&2&1478&C2&1\\
1469&E4&1&1369&C3&2\\
0569&E5&3&025A&C4&2\\
247A&E6&3&1269&D1&1\\
0489&E7&3&0256&D2&1\\
257A&E8&3&0347&D3&2\\
258A&E9&2&0237&D4&1\\
0469&E10&2&0257&D5&2\\
2369&E11&1&0258&B2&2\\
347A&E12&3&0169&B5&2\\
158A&E13&3&0369&A5&2\\
0247&E14&1&0478&A3&3\\
047A&A4&2&1459&B1&2\\
1479&A6&2&2589&A8&3\\
267A&A2&2&0479&A14&3
\end{array}
\tag{4.1}
\]

The left column-pair uses thirteen distinct E rows and three distinct A
rows.  The right column-pair uses all four C rows, all five D rows, three B
rows, and four further A rows.  Thus all thirty-two tail rows in (4.1) are
distinct.  The colour column is exactly (1.1), without repetition.

### Theorem 4.1 (full backward-tail transversal)

The bipartite incidence graph between the thirty-two certified holes
(mathcal H) and the forty-two canonical tail wreaths has a matching
saturating (mathcal H).

#### Proof

Table (4.1) is the matching.  Every one of its incidences is present in
(2.1), (3.1), or the previously displayed B/C/D/E tables, its colours are
distinct, and its tail rows are distinct.  \(\square\)

This is stronger than the earlier degree-(11) target and stronger than
the corrected degree-(10) consequence (3.7).  The backward-tail Hall
problem is therefore not the obstruction to the canonical fusion.

## 5. The coupled lower/upper disjointness graph is also unobstructed

At a seam whose new lower and complementary-upper colours are both missing,
the two four-sets must be disjoint.  The abstract disjointness condition by
itself has no Hall defect: the following is a perfect matching from
(mathcal H_0) to (mathcal H_1).

\[
\begin{array}{c|c@{\qquad}c|c}
0147&2369&047A&2589\\
0169&247A&025A&1479\\
0237&1459&0489&267A\\
0247&1369&0479&258A\\
0256&1478&0569&347A\\
0257&136A&0469&158A\\
0258&1469&0369&257A\\
0347&1269&0478&259A
\end{array}
\tag{5.1}
\]

Every pair in (5.1) is disjoint, and every one of the thirty-two colours
occurs once.  Moreover (5.1) is invariant by pairs under the reflection
(2.3).  For instance

\[
(0147,2369)\overset\sigma\longleftrightarrow(047A,2589).
\]

Thus the requirement that at least six seam repairs be simultaneous on the
two ledgers is not blocked by the abstract hole-disjointness graph.  The
missing information is whether such pairs are realised by the **same
physical ports**.

## 6. Tri-letter audit of all sixteen disjoint pairs

For disjoint holes (C,Y), put

\[
K=\Omega\setminus(C\cup Y)=\{\beta,t,\alpha\}.
\tag{6.1}
\]

A seam with lower colour (C) and complementary-upper colour (Y) must
use the five-window

\[
W_\beta=C+\beta
\]

at its tail, the adjacent extension coordinate (t), the head window

\[
W_t=C+t,
\]

and first head insertion (alpha).  Conversely, these data determine the
two new colours.  Thus each ordered pair ((C,Y)) has only the six
permutations of (K) to test.

For a five-window (W_x=(w_0,w_1,w_2,w_3,w_4)), the following local record
is enough:

\[
(\text{owner row};,W_x;,\operatorname{pos}_{W_x}(x);
  \operatorname{pred}(W_x),\operatorname{succ}(W_x)).
\tag{6.2}
\]

If (x) is in position one, only the successor is backward-safe; if it is
in position three, only the predecessor is backward-safe; and in position
two both are backward-safe.  At the head, (alpha) must be respectively
the successor or predecessor of (W_t), and the corresponding two head
deletion tests must pass.

Because reflection (2.3) preserves every item in this test, it is enough to
audit the following eight representative pairs from (5.1).  The
`tail-compatible triples` column lists all permutations surviving the tail
adjacency test.  A triple is written ((\beta,t,\alpha)).

\[
\begin{array}{c|c|c|c}
C\to Y&K&\text{tail-compatible triples}&\text{physical triples}\\ \hline
0147\to2369&\{5,8,A\}&(A,5,8)&--\\
0169\to247A&\{3,5,8\}&(3,8,5)&--\\
0237\to1459&\{6,8,A\}&(8,6,A)&--\\
0247\to1369&\{5,8,A\}&(8,5,A)&--\\
0256\to1478&\{3,9,A\}&(3,9,A),(A,3,9)&(A,3,9)\\
0257\to136A&\{4,8,9\}&(9,8,4)&(9,8,4)\\
0258\to1469&\{3,7,A\}&(3,7,A),(A,3,7)&--\\
0347\to1269&\{5,8,A\}&(A,5,8)&--
\end{array}
\tag{6.3}
\]

For hand verification, the complete local owner data used in (6.3) are:

\[
\begin{array}{c|c|c|c|c}
C&x&\text{owner and ordered }W_x&\operatorname{pos}(x)&
(\operatorname{pred},\operatorname{succ})\\ \hline
0147&5&A13:(0,1,4,5,7)&3&(9,3)\\
&8&A11:(7,0,1,8,4)&3&(6,5)\\
&A&A9:(7,A,0,1,4)&1&(6,5)\\ \hline
0169&3&A5:(9,0,1,3,6)&3&(8,7)\\
&5&A12:(9,5,0,1,6)&1&(8,7)\\
&8&A13:(6,8,9,0,1)&1&(A,4)\\ \hline
0237&6&E7:(0,6,7,2,3)&1&(5,1)\\
&8&E4:(7,0,8,2,3)&2&(6,5)\\
&A&D4:(7,A,0,2,3)&1&(6,5)\\ \hline
0247&5&E8:(0,4,5,7,2)&2&(3,1)\\
&8&E5:(7,0,8,2,4)&2&(5,3)\\
&A&D5:(7,A,0,2,4)&1&(5,3)\\ \hline
0256&3&E11:(0,2,3,6,5)&2&(9,1)\\
&9&E13:(5,9,0,2,6)&1&(7,4)\\
&A&D2:(5,A,0,6,2)&1&(4,3)\\ \hline
0257&4&E8:(0,4,5,7,2)&1&(3,1)\\
&8&E5:(5,7,0,8,2)&3&(6,4)\\
&9&E13:(7,5,9,0,2)&2&(8,6)\\ \hline
0258&3&E4:(0,8,2,3,5)&3&(7,1)\\
&7&E5:(5,7,0,8,2)&1&(6,4)\\
&A&C3:(5,8,A,0,2)&2&(4,3)\\ \hline
0347&5&E8:(3,0,4,5,7)&3&(9,2)\\
&8&E3:(7,3,0,8,4)&3&(6,5)\\
&A&D3:(7,3,A,0,4)&2&(6,5)
\end{array}
\tag{6.4}
\]

For example, in the successful row (0256\to1478), the triple is

\[
(\beta,t,\alpha)=(A,3,9).
\]

The tail is the D2 window

\[
(5,A,0,6,2),
\]

followed by (t=3).  The protected coordinate is (r=2).  The head is
the E11 window

\[
(0,2,3,6,5),
\]

traversed in reverse, whose preceding coordinate is (alpha=9).  Since
(t) is in head position two, the head tests pass automatically.  The
tail complement is ({1,4,7,8,9}), and deleting (alpha=9) gives the
claimed upper colour (1478).

In the failed triple ((A,3,7)) for (0258\to1469), the desired
(alpha=7) is indeed the predecessor of the E4 head window
((0,8,2,3,5)), but the reverse head deletes (t=3) in its second
deletion slot.  This is a genuine head block, not merely a missing-neighbor
failure.

The reverse ordered pairs were audited by the same six-permutation test.
For the eight representatives above their complete tail-compatible and
physical lists are

\[
\begin{array}{c|c|c}
Y\to C&\text{tail-compatible triples}&\text{physical triples}\\ \hline
2369\to0147&(8,5,A),(A,5,8)&--\\
247A\to0169&(3,8,5),(5,8,3)&--\\
1459\to0237&(A,6,8)&--\\
1369\to0247&(A,5,8)&--\\
1478\to0256&(A,9,3)&(A,9,3)\\
136A\to0257&(4,8,9),(9,4,8)&--\\
1469\to0258&(A,7,3)&(A,7,3)\\
1269\to0347&(8,5,A),(A,5,8)&--
\end{array}
\tag{6.5}
\]

Equations (6.3), (6.5), and reflection give exactly the following eight
directed physical double-repair seams supported by the perfect matching
(5.1):

\[
\begin{array}{c|c|c|c|c|c}
B^*&Y^*&(\beta,t,\alpha)&\text{tail row and }W_\beta
&\text{head row and }W_t&\text{head orientation}\\ \hline
0256&1478&(A,3,9)&D2:(5,A,0,6,2)&E11:(0,2,3,6,5)&\text{reverse}\\
1478&0256&(A,9,3)&E11:(1,A,4,8,7)&D2:(1,9,8,7,4)&\text{reverse}\\
0569&347A&(1,8,2)&A12:(9,5,0,1,6)&E12:(6,5,8,9,0)&\text{forward}\\
347A&0569&(1,2,8)&E12:(4,3,7,1,A)&A12:(7,4,3,2,A)&\text{forward}\\
0257&136A&(9,8,4)&E13:(7,5,9,0,2)&E5:(5,7,0,8,2)&\text{forward}\\
0469&158A&(2,3,7)&E13:(9,0,2,6,4)&E9:(9,3,0,4,6)&\text{reverse}\\
1469&0258&(A,7,3)&E4:(1,A,9,4,6)&C3:(1,7,9,6,4)&\text{reverse}\\
257A&0369&(1,4,8)&E8:(5,7,2,1,A)&A5:(7,5,2,4,A)&\text{forward}
\end{array}
\tag{6.6}
\]

Thus six of the sixteen **unordered** pairs in (5.1) are physically
realisable: the pairs containing

\[
0256,\qquad0569,\qquad0257,\qquad0469,\qquad0258,\qquad0369.
\tag{6.7}
\]

There are eight directions because the first two reflected pairs work in
both directions.

This reaches the numerical six-pair overlap target only before the
one-port-per-wreath constraint is imposed.  The unique seam for
(0257\leftrightarrow136A) uses E13 as its tail, and the unique seam for
(0469\leftrightarrow158A) also uses E13 as its tail.  Therefore the six
unordered pairs in (6.7) cannot all be selected simultaneously.

The following five seams, however, have pairwise distinct tail rows,
pairwise distinct head rows, and no directed cycle:

\[
\begin{gathered}
D2\to E11,\qquad A12\to E12,\qquad E13\to E5,\\
E4\to C3,\qquad E8\to A5.
\end{gathered}
\tag{6.8}
\]

They correspond respectively to

\[
0256\to1478,\qquad0569\to347A,\qquad0257\to136A,
\quad1469\to0258,quad257A\to0369.
\]

Hence the symmetric disjoint matching (5.1) is **exactly one
tail-compatible double repair short** of the unavoidable six-seam count in
the zero-cut-loss case.  To reach six one must alter the disjoint pairing,
find a different physical realization of one of its pairs outside this
audit (there is none among the six tri-letter permutations), or exploit a
different global ledger configuration.

The last alternative is in fact available.  The corrected A--B audit gives
the independent physical seam

\[
 B3\longrightarrow D3,
 \qquad B^*=347A,
 \qquad Y^*=1269.
\tag{6.9}
\]

Indeed, its tail window is

\[
(4,3,8,7,A),
\]

with internal deletion \(\beta=8\) in position two and adjacent extension
\(t=0\).  The candidate head is the D3 window

\[
(7,3,A,0,4)
\]

in the forward orientation.  The protected tail coordinate \(A\) is in
head position two and \(t=0\) is in position three, so the head-survival
criterion passes.  The first head insertion is \(\alpha=5\), and deleting
it from the complementary tail five-set

\[
\{1,2,5,6,9\}
\]

gives \(Y^*=1269\).  This proves (6.9) without appealing to the suspended
positive-support converse.

Neither B3 nor D3 occurs among the ten rows used in (6.8).  Moreover,
\(347A\) is distinct from the five lower gains in (6.8), and \(1269\) is
distinct from their five upper gains.  Consequently

\[
\boxed{
 D2\to E11,\quad A12\to E12,\quad E13\to E5,\quad
 E4\to C3,\quad E8\to A5,\quad B3\to D3
}
\tag{6.10}
\]

is a directed matching of six genuine physical double-repair seams.  It
uses twelve different wreaths, hence is automatically acyclic and satisfies
the one-port-per-wreath constraint.  Its six lower gains and six upper gains
are both pairwise distinct.

### Theorem 6.1 (six simultaneous physical double repairs)

The corrected canonical factor admits six pairwise wreath-disjoint,
acyclic physical seams that simultaneously add six certified missing lower
four-colours and six certified missing complementary-upper four-colours.

Thus the unavoidable six-overlap count in the zero-cut-loss ledger is no
longer an obstruction.  What remains is to audit the twelve cut colours of
these six seams and then extend (6.10) to a thirty-six-seam directed forest.

## 6.2 Exact cut-colour audit for the six seams

For an ordered cyclic five-window

\[
W=(w_0,w_1,w_2,w_3,w_4)
\]

with cyclic predecessor and successor, the deleted old lower colour is

\[
\begin{array}{c|cc}
&\text{forward path}&\text{reverse path}\\ \hline
\text{tail port}&W-w_0&W-w_4\\
\text{head port}&W-w_4&W-w_0.
\end{array}
\tag{6.11}
\]

The complementary-upper cut colour depends on whether the selected window
is the last source of a tail path or the first source of a head path:

\[
\begin{array}{c|cc}
&\text{forward path}&\text{reverse path}\\ \hline
\text{tail port}
&\Omega-(W\cup\{\operatorname{succ}(W),\operatorname{succ}^2(W)\})
&\Omega-(W\cup\{\operatorname{pred}(W),\operatorname{pred}^2(W)\})\\
\text{head port}
&\Omega-(W\cup\{\operatorname{pred}(W),\operatorname{succ}(W)\})
&\Omega-(W\cup\{\operatorname{pred}(W),\operatorname{succ}(W)\}).
\end{array}
\tag{6.12}
\]

Indeed, the old lower turn is the intersection of the two rank-five
neighbours of the cut rank-six vertex, while the complementary-upper turn
is the complement of the union of the two rank-six neighbours of the
*old head* of the deleted edge.  At a tail port the displayed window is the
other, last source, which accounts for the two-step shift in the first row
of (6.12).  This proves (6.11)--(6.12) directly from the cyclic order.

Applying these formulas to the twelve ports in (6.10) gives:

\[
\begin{array}{c|c|c|c|c}
\text{arc}&\text{port}&\text{role/orientation}&B_0&Y_0\\ \hline
D2\to E11&D2&\text{tail forward}&026A&4789\\
&E11&\text{head reverse}&2356&478A\\ \hline
A12\to E12&A12&\text{tail reverse}&0159&2347\\
&E12&\text{head forward}&5689&1347\\ \hline
E13\to E5&E13&\text{tail reverse}&0579&1346\\
&E5&\text{head forward}&0578&139A\\ \hline
E4\to C3&E4&\text{tail forward}&469A&2358\\
&C3&\text{head reverse}&4679&028A\\ \hline
E8\to A5&E8&\text{tail reverse}&1257&3689\\
&A5&\text{head forward}&2457&0139\\ \hline
B3\to D3&B3&\text{tail forward}&378A&1569\\
&D3&\text{head forward}&037A&1289
\end{array}
\tag{6.13}
\]

The complete A--B templates and the displayed C--D--E cyclic-four tables
give the following exact occurrence-row audit.  A row listed once contains
the colour in exactly one cyclic position.

\[
\begin{array}{c|l@{\qquad}c|l}
B_0&\text{all owner rows}&Y_0&\text{all owner rows}\\ \hline
026A&D2&4789&D2,E11\\
2356&A14,E11&478A&A3,E11\\
0159&A12&2347&A12,E12\\
5689&D5,E12&1347&A6,E12\\
0579&A10,E13&1346&A8,E13\\
0578&E5&139A&E2,E5\\
469A&A2,E4&2358&E4\\
4679&C3,E4&028A&B1,C3\\
1257&B1,E8&3689&E8\\
2457&A5,E8&0139&A2,A5\\
378A&B3&1569&B3\\
037A&D3&1289&D1,D3
\end{array}
\tag{6.14}
\]

For example, the second occurrences protecting \(0579,469A,2457\) and
\(234A\) are respectively the cyclic windows in A10, A2, E8 and A10.
The singleton entries in (6.14) have no occurrence in any other A--E
template; this is an exact complement check for these twenty-four colours,
not a lower bound on their multiplicities.

It follows that precisely five of the selected lower cut colours are
extinguished,

\[
\boxed{026A,0159,0578,378A,037A},
\tag{6.15}
\]

and precisely three of the selected complementary-upper cut colours are
extinguished,

\[
\boxed{2358,3689,1569}.
\tag{6.16}
\]

None of these colours is a new seam colour, since every colour in
(6.13) is already cyclically supported whereas all twelve seam gains are
certified holes.  Hence the exact local replacement ledger is

\[
\boxed{L_B=5,\quad G_B=6;\qquad L_Y=3,\quad G_Y=6.}
\tag{6.17}
\]

In particular, the six seams already increase lower support by one and
complementary-upper support by three.  Since the initial support is exactly
\(298\), a completion
using all remaining twenty-six certified holes may incur at most six
additional lower extinctions and eight additional upper extinctions.  More
explicitly, the remaining thirty seams must satisfy

\[
G_B^{\rm rem}-L_B^{\rm rem}\ge20,
\qquad
G_Y^{\rm rem}-L_Y^{\rm rem}\ge18.
\tag{6.18}
\]

Thus cut survival does not invalidate the six-seam seed: it leaves positive,
explicit loss budgets on both ledgers.

## 6.3 A strictly better seven-seam seed

Two further physical double repairs improve (6.10) and its cut ledger.

First, use the E2 order

\[
(0,8,6,2,3,1,A,9,7,4,5).
\]

The tail window

\[
(6,2,3,1,A)
\]

has internal deletion \(\beta=2\) in position one and forward extension
\(t=9\).  It therefore creates the lower colour \(136A\).  The head
\(1369A\) is the E5 window

\[
(3,1,A,9,6)
\]

in the forward orientation.  Its successor is \(\alpha=5\), and the
protected pair \((r,t)=(A,9)\) occupies head positions \((2,3)\), so the
five seam tests pass.  Since the complementary tail five-set is \(04578\),
the new upper colour is

\[
04578-5=0478.
\tag{6.19}
\]

Thus

\[
\boxed{E2\longrightarrow E5:\qquad(136A,0478)}
\tag{6.20}
\]

is a genuine physical double repair.

Second, in A3 take the forward tail window

\[
(4,8,7,A,0),
\]

with \((\beta,t)=(8,1)\).  Its new lower colour is \(047A\).  The head is
the forward A9 window

\[
(7,A,0,1,4),
\]

whose successor is \(\alpha=5\).  Here \((r,t)=(0,1)\) occupies head
positions \((2,3)\), so the seam is physical, and

\[
\Omega\setminus(047A\cup\{8,1\})-5=2369.
\]

Therefore

\[
\boxed{A3\longrightarrow A9:\qquad(047A,2369)}
\tag{6.21}
\]

is another physical double repair.

Replace the E13-to-E5 and B3-to-D3 members of (6.10) by the E13-to-E9
seam from (6.6), and then add both (6.20) and (6.21).  This gives the
seven-seam directed matching

\[
\boxed{
\begin{gathered}
D2\to E11,\quad A12\to E12,\quad E13\to E9,\quad
E4\to C3,\\
E8\to A5,\quad E2\to E5,\quad A3\to A9.
\end{gathered}}
\tag{6.22}
\]

All fourteen wreath rows in (6.22) are distinct.  Its lower gains are

\[
0256,0569,0469,1469,257A,136A,047A,
\tag{6.23}
\]

and its upper gains are

\[
1478,347A,158A,0258,0369,0478,2369.
\tag{6.24}
\]

Both lists consist of seven distinct certified holes.

The exact cut ledger is particularly favourable.  A dagger marks an old
colour whose selected occurrence is its only occurrence in the canonical
factor.

\[
\begin{array}{c|cc|cc}
\text{arc}&B_0(\text{tail})&B_0(\text{head})
&Y_0(\text{tail})&Y_0(\text{head})\\ \hline
D2\to E11&026A^\dagger&2356&4789&478A\\
A12\to E12&0159^\dagger&5689&2347&1347\\
E13\to E9&0246&0346^\dagger&578A&128A\\
E4\to C3&469A&4679&2358^\dagger&028A\\
E8\to A5&1257&2457&3689^\dagger&0139\\
E2\to E5&123A&139A&0458&0278\\
A3\to A9&078A&017A&2569&2389
\end{array}
\tag{6.25}
\]

Every undaggered entry has an uncut second occurrence.  For the last two
arcs these protecting occurrences are, respectively,

\[
\begin{array}{c|cccc}
E2\to E5&123A:E7&139A:E2&0458:E3&0278:E4\\
A3\to A9&078A:B3&017A:A3&2569:A6&2389:A8.
\end{array}
\tag{6.26}
\]

The entries in earlier rows are protected by the occurrence pairs already
listed in (6.14), together with

\[
0246:D1,E13,quad578A:A8,E13,quad128A:E6,E9.
\]

Consequently (6.22) has the exact replacement ledger

\[
\boxed{L_B=3,\quad G_B=7;\qquad L_Y=2,\quad G_Y=7.}
\tag{6.27}
\]

The lower and upper supports have therefore already increased by four and
five, respectively.  Conditional on initial support \(298\), the remaining
twenty-nine seams need net gains only

\[
\boxed{
G_B^{\rm rem}-L_B^{\rm rem}\ge17,
\qquad
G_Y^{\rm rem}-L_Y^{\rm rem}\ge16.}
\tag{6.28}
\]

In particular, if the remaining cuts are all redundant, only four further
double-repair seams are forced by the two ledgers: seventeen new lower and
sixteen new upper colours can be placed in twenty-nine seams with overlap
four.  This is strictly weaker than the original six-overlap-at-once gate.

One may reverse the first arc to \(E11\to D2\).  Its gains become
\((1478,0256)\), still new within (6.23)--(6.24); its only extinction moves
from the lower ledger to the upper ledger.  This gives the symmetric
alternative \((L_B,L_Y)=(2,3)\) with the same total net gain.

There is an eighth row-disjoint zero-loss double repair.  In A6 use the
reverse tail window

\[
(1,4,3,7,9),
\]

with \((\beta,t)=(3,0)\).  Its lower colour is \(1479\).  The head is the
forward A14 window

\[
(7,9,0,1,4),
\]

whose successor is \(\alpha=6\).  Since \(t=0\) is in head position two,
the seam is physical, and its complementary-upper colour is \(258A\).
Thus

\[
\boxed{A6\longrightarrow A14:\qquad(1479,258A).}
\tag{6.29}
\]

Its four old cut colours and protecting second occurrences are

\[
\begin{array}{c|c}
1347&E12\\
0179&A4\\
2568&A4\\
235A&A11.
\end{array}
\tag{6.30}
\]

Here A6 itself is the selected occurrence of \(1347\) and \(2568\), while
A14 is the selected occurrence of \(0179\) and \(235A\).  Hence (6.29)
adds no extinction.  Rows A6 and A14 and both gains are new relative to
(6.22).

### Theorem 6.2 (eight simultaneous double repairs at five cut losses)

Adding (6.29) to (6.22) gives eight pairwise wreath-disjoint physical
double-repair seams on sixteen rows.  Their lower and upper gains are each
eight distinct certified holes, while the complete cut ledger remains

\[
\boxed{L_B=3,\quad G_B=8;\qquad L_Y=2,\quad G_Y=8.}
\tag{6.31}
\]

Since the initial support is now independently certified to be \(298\),
the selected sixteen ports already leave supports \(303\) and \(304\).
The remaining twenty-eight seams need only satisfy

\[
\boxed{
G_B^{\rm rem}-L_B^{\rm rem}\ge16,
\qquad
G_Y^{\rm rem}-L_Y^{\rm rem}\ge15.}
\tag{6.32}
\]

The seed consists of eight disjoint directed edges, so together with the
remaining twenty-six unused wreaths it has thirty-four components.  Adding
twenty-eight further arcs without a directed cycle produces exactly six
paths, as required.

There is a further zero-loss improvement if the first seed arc is taken in
the reverse direction \(E11\to D2\).  In A7 use the forward tail window

\[
(2,6,5,A,9)
\]

with \((\beta,t)=(6,0)\).  It creates lower colour \(259A\).  The head
\(0259A\) is the forward C4 window

\[
(5,A,9,0,2),
\]

whose successor is \(\alpha=3\).  The protected pair \((r,t)=(9,0)\)
occupies head positions \((2,3)\), so this is a physical seam, and its
upper colour is \(1478\):

\[
\boxed{A7\longrightarrow C4:\qquad(259A,1478).}
\tag{6.33}
\]

Its cut colours are

\[
B_0(A7)=569A,quad B_0(C4)=059A,qquad
Y_0(A7)=3478,quad Y_0(C4)=1678.
\tag{6.34}
\]

All four cuts are redundant: \(569A\) survives in E5, \(059A\) at a
different A7 turn, \(3478\) has three owners A7, B2 and B3, and \(1678\)
survives in C2.

With \(E11\to D2\), the first seed gains are \((1478,0256)\), so both
gains in (6.33) are new in their respective ledgers.  We obtain:

### Theorem 6.3 (nine-seam seed)

There are nine pairwise wreath-disjoint physical double-repair seams on
eighteen rows with exact ledger

\[
\boxed{L_B=2,\quad G_B=9;\qquad L_Y=3,\quad G_Y=9.}
\tag{6.35}
\]

Thus the lower and upper supports already equal \(305\) and \(304\).
The remaining twenty-seven arcs need net gains only

\[
\boxed{
G_B^{\rm rem}-L_B^{\rm rem}\ge14,
\qquad
G_Y^{\rm rem}-L_Y^{\rm rem}\ge15.}
\tag{6.36}
\]

If their cuts are redundant, only two further double-repair seams are
forced, since fourteen lower and fifteen upper gains can occupy twenty-seven
arcs with overlap two.

## 6.4 Optimized eleven-seam seed

The nine-seam seed can be improved by four coordinated changes.

1. Reverse \(A12\to E12\) to the already-audited seam
   \(E12\to A12\), with gains \((347A,0569)\).
2. Replace \(E13\to E9\) and \(E2\to E5\) by
   \(E13\to E5\) and its reflected zero-loss partner \(E6\to E9\).
3. Add the reflected zero-loss seam \(B3\to B5\).
4. Add the one-new-port seam \(D5\to A8\).

The new seams not already written above have the following exact local
data:

\[
\begin{array}{c|c|c|c|c|c}
\text{arc}&(B^*,Y^*)&(\beta,t,\alpha)&\text{tail }W/\text{orientation}
&\text{head }W/\text{orientation}\\ \hline
E6\to E9&(158A,0347)&(9,2,6)&(1,A,8,9,5)/R&(5,2,1,A,8)/R\\
B3\to B5&(1269,347A)&(5,0,8)&(2,1,6,5,9)/R&(9,0,2,1,6)/R\\
D5\to A8&(1369,257A)&(8,4,0)&(3,1,9,8,6)/R&(1,6,4,3,9)/R
\end{array}
\tag{6.37}
\]

For \(D5\to A8\), for example, the protected pair \((r,t)=(3,4)\)
has head positions \((3,2)\), so the reverse head passes; the complementary
five-set is \(0257A\), and deleting \(\alpha=0\) gives \(257A\).

The complete optimized directed matching is

\[
\boxed{
\begin{gathered}
E11\to D2,quad E12\to A12,quad E13\to E5,quad
E4\to C3,quad E8\to A5,\\
E6\to E9,quad A3\to A9,quad A6\to A14,quad
A7\to C4,quad B3\to B5,quad D5\to A8.
\end{gathered}}
\tag{6.38}
\]

Its twenty-two row names are all distinct, so the selected ports are
automatically common-port compatible and (6.38) is acyclic.

The lower gains are

\[
1478,347A,0257,1469,257A,158A,047A,1479,259A,1269,1369,
\tag{6.39}
\]

and the upper gains are

\[
0256,0569,136A,0258,0369,0347,2369,258A,1478,347A.
\tag{6.40}
\]

Each list contains eleven distinct certified holes.

The simultaneous cut audit has exactly two lower extinctions,

\[
\boxed{1347,0578},
\tag{6.41}
\]

and four upper extinctions,

\[
\boxed{026A,0159,2358,3689}.
\tag{6.42}
\]

The only cross-seam lower collision is \(1347\): its two owners A6 and E12
are both selected at that lower turn.  The colour \(0578\) is unique at E5.
On the upper side the four colours in (6.42) are unique at their selected
turns.  Every other cut colour has an uncut owner.  In particular the
potential \(578A\) collision from \(D5\to A8\) is avoided because E13 now
cuts \(1346\), not \(578A\); and the two selected cuts of \(3478\) at A7
and B3 leave its third occurrence at B2.

### Theorem 6.4 (optimized eleven-seam ledger)

The canonical factor contains an acyclic, common-port-compatible directed
matching of eleven physical double-repair seams with exact ledger

\[
\boxed{L_B=2,\quad G_B=11;\qquad L_Y=4,\quad G_Y=11.}
\tag{6.43}
\]

Thus the two supports after this seed are exactly

\[
\boxed{307\quad\text{and}\quad305.}
\tag{6.44}
\]

There remain twenty factor rows outside the seed and twenty-five arcs to be
added.  The residual exact ledger requirements are only

\[
\boxed{
G_B^{\rm rem}-L_B^{\rm rem}\ge12,
\qquad
G_Y^{\rm rem}-L_Y^{\rm rem}\ge14.}
\tag{6.45}
\]

If all remaining cuts are redundant, only one further double-repair arc is
forced, because twelve lower and fourteen upper gains have total demand
twenty-six across twenty-five arcs.

## 7. The exact surviving finite obstruction

For an oriented physical seam (e=p\to p'), record the four data

\[
\bigl(T(e),H(e),B^*(e),Y^*(e)\bigr),
\tag{7.1}
\]

where (T(e)) and (H(e)) are its tail and head wreath-port groups, and
(B^*,Y^*) are its new lower and complementary-upper four-colours.  The
five local seam inequalities decide membership in this four-way relation
exactly.

Theorem 4.1 proves that the projection

\[
(T,H,B^*,Y^*)\longmapsto(T,B^*)
\]

has a transversal covering every certified hole.  Equation (5.1) proves
that the abstract projection onto ((B^*,Y^*)), after forgetting physical
realizability, also has a perfect disjoint pairing.  Therefore any failure
of the canonical route must occur in the **compatibility of these two
projections** with head survival and one common selected port per wreath.

Concretely, the remaining canonical problem is to choose one oriented port
from each of the forty-two wreaths and thirty-six induced physical seams so
that

1. the seams have indegree and outdegree at most one and contain no directed
   cycle;
2. the exact lower and upper replacement ledgers both retain support at
   least (319);
3. the same seams simultaneously realise the necessary lower and upper
   gains, including the cut-colour losses.

The present note removes neither the head double-block patterns
((4,1)) and ((0,3)), nor the upper-colour restriction, nor the common-port
and acyclicity constraints.  Those form one coupled finite lifting problem;
they cannot be replaced by the two separately solved matchings above.

The positive-support converse is no longer a separate evidentiary gap: it
is supplied by the certificate cited in Section 1.  The remaining problem
is purely the physical port-forest completion and its exact cut ledger.

## 8. Exact advance

Proved here, without a search program:

* four omitted class-E deletion incidences and the corrected E total (86);
* the complete class-A incidence table, total (76), and maximum degree
  eight;
* the complete global (224)-incidence ledger and maximum tail degree ten;
* an explicit matching of all thirty-two certified holes to distinct tail
  wreaths;
* an explicit perfect disjointness matching between the zero-containing and
  zero-avoiding holes;
* the complete six-permutation physical audit of that disjointness matching;
* eight genuine directed double-repair seams on six unordered hole pairs,
  and an exact one-tail collision inside that symmetric pairing;
* one independent B3-to-D3 double repair, which together with five of the
  preceding seams gives six pairwise wreath-disjoint simultaneous physical
  double repairs;
* the exact twenty-four-colour cut ledger for those seams, with five lower
  and three complementary-upper extinctions;
* two further zero-loss double repairs, E2-to-E5 and A3-to-A9, and the
  zero-loss A6-to-A14 repair;
* an eight-seam, sixteen-wreath directed matching with exact ledger
  \((L_B,G_B;L_Y,G_Y)=(3,8;2,8)\);
* the zero-loss A7-to-C4 repair and a nine-seam seed with exact ledger
  \((L_B,G_B;L_Y,G_Y)=(2,9;3,9)\);
* the optimized eleven-seam, twenty-two-row seed with exact supports
  \((307,305)\) and residual net requirements \((12,14)\).

Not proved:

* a lift of the tail transversal through the head tests;
* completion of the eleven-seam seed to thirty-six seams while respecting
  the residual net-gain requirements (6.45);
* a universal nonzero word of length (465).

The corrected mathematical conclusion is therefore

\[
\boxed{
\text{an eleven-seam low-loss physical seed is solved; the remaining gate
is its completion by 25 arcs to a six-path forest.}
}
\]
