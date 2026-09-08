# Exact lower-ledger closure from the eight-seam seed

Date: 2026-07-25

## 1. Result

Assume the corrected canonical cyclic-four support is (298).  Use the
eight pairwise row-disjoint physical double repairs

\[
\begin{gathered}
D2\to E11,\quad A12\to E12,\quad E13\to E9,\quad
E4\to C3,\\
E8\to A5,\quad E2\to E5,\quad A3\to A9,
\quad A6\to A14.
\end{gathered}
\tag{1.1}
\]

Their eight distinct lower gains are

\[
0256,0569,0469,1469,257A,136A,047A,1479,
\tag{1.2}
\]

and their exact lower cut loss is three.  The following sixteen further
holes can be assigned to sixteen distinct nonseed tail rows so that **none**
of the sixteen old lower cut colours is extinguished:

\[
\begin{array}{c|c|c|c|c}
\text{tail row}&B^*&\text{orientation}&B_0&\text{protecting row}\\ \hline
E3&259A&F&129A&E1\\
E6&0347&F&0467&E4\\
A13&0489&R&0189&A5\\
E14&0247&F&0249&E12\\
A2&247A&R&2467&E6\\
D3&2589&F&1289&D1\\
C1&0147&R&0124&C2\\
A7&1478&F&3478&\text{multiplicity three}\\
C4&025A&R&059A&A7\\
B3&1269&R&1256&E9\\
D4&267A&R&067A&A9\\
E10&0237&R&0235&D4\\
D5&0257&R&057A&A8\\
B2&0258&R&0125&B1\\
B5&0169&F&0126&B3\\
B1&1459&F&4579&E2
\end{array}
\tag{1.3}
\]

Here (F,R) refer to the displayed forward cyclic order and its reverse.
The protector in the last column is not cut at that same lower colour by
either (1.1) or (1.3).

Consequently the selected lower gains in (1.2)--(1.3) number exactly

\[
8+16=24,
\]

while the only lower extinctions are the three already present in (1.1).
Thus

\[
 \boxed{G_B-L_B=24-3=21.}
\tag{1.4}
\]

The lower support reaches

\[
 \boxed{298+21=319.}
\]

This is a tail-projection theorem.  It does not yet assert that the sixteen
candidate heads are distinct or physically admissible, nor that all
forty-two selected cuts form six paths.  In fact the first orientation
shown for E6 targets the already occupied seed head E12; Section 4 records
this named lifting obstruction.

## 2. Literal tail witnesses

The exact tail data behind (1.3) are as follows.  The deleted entry is
(eta), (t) is the adjacent extension in the selected orientation, and
(H=B^*+t) is the candidate cross head.

\[
\begin{array}{c|c|c|c|c|c}
\text{row}&B^*&W&\beta&t&H\\ \hline
E3&259A&(5,2,1,A,9)&1&6&2569A\\
E6&0347&(3,0,6,7,4)&6&2&02347\\
A13&0489&(8,9,0,1,4)&1&6&04689\\
E14&0247&(7,9,0,2,4)&9&5&02457\\
A2&247A&(7,2,4,6,A)&6&8&2478A\\
D3&2589&(5,2,1,9,8)&1&6&25689\\
C1&0147&(0,4,2,1,7)&2&A&0147A\\
A7&1478&(1,4,3,8,7)&3&2&12478\\
C4&025A&(5,A,9,0,2)&9&4&0245A\\
B3&1269&(2,1,6,5,9)&5&0&01269\\
D4&267A&(6,7,A,0,2)&0&4&2467A\\
E10&0237&(0,2,3,5,7)&5&9&02379\\
D5&0257&(5,7,A,0,2)&A&6&02567\\
B2&0258&(0,2,1,5,8)&1&9&02589\\
B5&0169&(9,0,2,1,6)&2&7&01679\\
B1&1459&(1,5,7,9,4)&7&3&13459
\end{array}
\tag{2.1}
\]

For D5 the middle deletion permits both orientations.  The forward choice
would give (H=02457), colliding already at the raw set level with the E14
head.  The reverse choice displayed in (2.1) gives (H=02567) and changes
the old lower cut from (027A) to (057A); the latter survives in A8.

## 3. Hand audit of the sixteen lower cuts

For a forward tail (W=(w_0,\ldots,w_4)), the deleted old lower colour is
(W-w_0).  For a reverse tail it is (W-w_4).  Applying this to (2.1)
gives precisely the fourth column of (1.3).

Each protector is a literal cyclic window:

\[
\begin{array}{c|c}
129A&E1:(2,1,A,9)\\
0467&E4:(4,6,7,0)\\
0189&A5\text{ at its cyclic }(8,9,0,1)\text{ turn}\\
0249&E12\text{ at its }0249\text{ turn}\\
2467&E6\text{ at its }2467\text{ turn}\\
1289&D1\text{ at its }1289\text{ turn}\\
0124&C2:(0,4,2,1)\\
059A&A7\text{ at its }059A\text{ turn}\\
1256&E9:(6,5,2,1)\\
067A&A9\text{ at its }067A\text{ turn}\\
0235&D4:(0,2,3,5)\\
057A&A8\text{ at its }057A\text{ turn}\\
0125&B1:(0,2,1,5)\\
0126&B3:(0,2,1,6)\\
4579&E2:(9,7,4,5).
\end{array}
\tag{3.1}
\]

The (3478) cut in A7 has multiplicity three in the corrected canonical
cyclic-four ledger.  Its other owners are B2 and B3.  Those rows are
selected in (1.3), but at the different lower cuts (0125) and (1256), so
both protecting occurrences survive.

Some protector rows themselves occur in (1.1) or (1.3), but always at a
different selected lower turn.  For example E4 protects (0467) while its
seed cut removes (469A); E6 protects (2467) while its selected cut
removes (0467); D4 protects (0235) while its selected cut removes (067A);
A8 protects (057A); and B3 protects (0126) while its selected cut removes
(1256).  Hence no alleged second occurrence is simultaneously deleted.

## 4. Exact surviving lifting gate

The sixteen head sets in (2.1) are distinct as sets.  Distinct sets do not
yet imply distinct owner rows, because one wreath contains eleven middle
sets.  Moreover a seed head row already has indegree one.

A direct scan of the forty-two displayed cyclic orders gives the unique
owner rows

\[
\begin{array}{c|c@{\qquad}c|c}
2569A&A7&02347&E12\\
04689&E10&02457&E8\\
2478A&A3&25689&A6\\
0147A&A9&12478&C2\\
0245A&D3&01269&B5\\
2467A&A2&02379&E11\\
02567&E7&02589&E12\\
01679&A11&13459&A9.
\end{array}
\tag{4.1}
\]

The first raw transition is physically blocked in both head orientations.
Indeed, (2569A) occurs in A7 as ((2,6,5,A,9)).  The E3 forward tail has
protected pair ((r,t)=(9,6)), occupying head positions ((4,1)), one of
the four exact double-block patterns.  So even its owner row A7 cannot be
used.

There is an immediate collision in the displayed choices:

\[
 E6\to H=02347,
\]

and (02347) is the E12 window ((0,2,4,3,7)), while E12 is already the
head of the seed arc (A12\to E12).  Thus the forward E6 choice cannot be
used in a directed linear forest containing (1.1).

The same E6 middle-deletion incidence has a reverse alternative

\[
 t=5,\qquad H=03457,\qquad B_0=0367.
\]

Whether this alternative, together with suitable choices at the other
middle deletions, yields sixteen distinct legal head rows is the next exact
finite question.  Once the head orientations are fixed, their new upper
colours and upper cut losses must also meet the residual upper net-gain
requirement (15).

There is a further common-port condition beyond (4.1).  Every selected tail
state fixes the head endpoint at the other end of its own opened wreath.  If
the tail is forward this endpoint is (W-w_0+t); if it is reverse it is
(W-w_4+t).  For the sixteen states in (2.1), these fixed own-heads are

\[
\begin{gathered}
1269A,02467,01689,02459,24678,12689,0124A,23478,\\
0459A,01256,0467A,02359,0567A,01259,01267,34579.
\end{gathered}
\tag{4.2}
\]

Thus an outgoing candidate whose middle set belongs to, say, a residual
row is compatible only if it equals that row's particular member in (4.2).
Row ownership alone is not enough.  Equations (4.1)--(4.2) show explicitly
why the closed tail projection is still far from a path cover in the
selected-port digraph.

Finally, ten row groups remain outside (1.1)--(1.3).  Their cut ports must
be chosen so as not to extinguish one of the protecting lower occurrences
listed above, and all thirty-six cross arcs must be acyclic.  These are
common-port constraints, not defects in the closed lower tail ledger.
