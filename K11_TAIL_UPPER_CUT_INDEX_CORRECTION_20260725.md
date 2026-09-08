# Correction of the complementary-upper cut index at a tail port

Date: 2026-07-25

## 1. Verdict

The tail entries in (6.13)--(6.16) of
`K11_CORRECTED_TAIL_TRANSVERSAL_AND_COUPLED_GATE_20260725.md` use the
complementary-upper colour immediately *before* the selected tail source.
The edge actually deleted by a tail cut lies immediately *after* its
rank-six tail vertex.  The two colours differ by one cyclic shift.

The six head entries in that table are correctly indexed.  After correcting
only the six tail entries, the six-seam seed extinguishes exactly three,
not four, complementary-upper colours:

\[
 \boxed{2358,\quad3689,\quad1569.}
\]

Thus its exact seed ledger is

\[
 \boxed{L_B=5,\ G_B=6;\qquad L_Y=3,\ G_Y=6.}
\]

Conditional on initial cyclic-four support (298), the remaining thirty
seams need satisfy

\[
 \boxed{G_B^{\rm rem}-L_B^{\rm rem}\ge20,
 \qquad G_Y^{\rm rem}-L_Y^{\rm rem}\ge18.}
\]

No computation or search is used below.

## 2. Exact edge indexing

Fix an oriented cyclic coordinate order

\[
 (z_0,z_1,\ldots,z_{10})
\]

and use the standard canonical states

\[
 S_i=\{z_{i-5},\ldots,z_{i-1}\},\qquad
 D_i=\{z_{i+1},\ldots,z_{i+5}\}.
\]

The alternating cycle locally reads

\[
 S_i,D_i,S_{i+1},D_{i+1}.
\]

The lower and complementary-upper colours on this turn are

\[
 B_i=S_i\cap S_{i+1}
     =\{z_{i-4},z_{i-3},z_{i-2},z_{i-1}\},
\]

\[
 Y_i=D_i\cap D_{i+1}
     =\{z_{i+2},z_{i+3},z_{i+4},z_{i+5}\}.
\tag{2.1}
\]

At a **tail** port, write

\[
 W=S_i=(z_{i-5},\ldots,z_{i-1}),\qquad t=z_i.
\]

The splice deletes the old transition (D_i\to S_{i+1}).  Hence the old
upper colour lost there is (Y_i), not (Y_{i-1}).  If (u=z_{i+1}) is
the first coordinate after (t) in the selected orientation, then

\[
 \boxed{Y_{\rm tail}=D_i-u
 =\Omega\setminus(W\cup\{t,u\}).}
\tag{2.2}
\]

By contrast,

\[
 \Omega\setminus
 \bigl(W\cup\{\operatorname{pred}(W),\operatorname{succ}(W)\}\bigr)
 =Y_{i-1}.
\tag{2.3}
\]

Formula (2.3) is correct at a **head** port (W=S_i), because the removed
incoming transition is (D_{i-1}\to S_i).  It is shifted by one when
applied to a tail port.  The same proof works after reversing the cyclic
orientation: in (2.2), (u) is simply the first coordinate after (t) in
the reversed order.

As a concrete check, the B3 tail is

\[
 W=(4,3,8,7,A),\qquad t=0,qquad
 D_i=\{2,1,6,5,9\}.
\]

The first coordinate after (t) is (2), so the deleted outgoing colour is

\[
 Y_i=D_i-2=1569.
\]

The former value (1256) is (Y_{i-1}); its edge remains in the opened
B3 path.

## 3. Corrected twelve-port table

The lower colours (B_0) are unchanged.  The corrected upper entries are:

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
\tag{3.1}
\]

For instance, at the reverse A12 tail the selected oriented six-window is

\[
 (6,1,0,5,9,8).
\]

The next coordinate in that reversed orientation is (A), so (2.2) gives

\[
 \Omega\setminus\{6,1,0,5,9,8,A\}=2347.
\]

The other five tail entries follow identically.

## 4. Exact occurrence audit for the corrected tail colours

The complete owner rows of the six corrected tail colours are

\[
\begin{array}{c|l}
Y_0&\text{all owner rows}\\ \hline
4789&D2,E11\\
2347&A12,E12\\
1346&A8,E13\\
2358&E4\\
3689&E8\\
1569&B3
\end{array}
\tag{4.1}
\]

The witnesses are literal cyclic windows:

\[
\begin{array}{c|c|c}
Y_0&\text{selected occurrence}&\text{second occurrence, if any}\\ \hline
4789&D2:(9,8,7,4)&E11:(4,8,7,9)\\
2347&A12:(7,4,3,2)&E12:(4,3,7,1)\\
1346&E13:(6,4,3,1)&A8:(1,6,4,3)\\
2358&E4:(8,2,3,5)&--\\
3689&E8:(6,8,9,3)&--\\
1569&B3:(1,6,5,9)&--
\end{array}
\tag{4.2}
\]

For completeness, exactness of (4.1) follows directly from the A--E
templates.  In class A, a nonzero window containing (1) but not (2)
has type (N_1); this gives (1346) only from the first-three-(R_4)
set (421), namely A8, and gives no (1569).  A nonzero window containing
neither (1) nor (2) has type (N_2) or (N_7); none of the displayed
(T_4) rows gives (4789,2358,) or (3689).  A window containing (2)
but not (1) has one of types (N_3,ldots,N_6); the required projections
give (2347) only in A12 and (2358) nowhere.  Class B gives (1569)
only from its (N_2) row (215\mid436), namely B3.  The explicit C--D
lists give only D2 for (4789), and none of the other five colours.
Finally, direct substitution in the fourteen class-E orders gives exactly
the E-row occurrences displayed in (4.1).

This audit also exposes a harmless but relevant transcription error in the
old class-E positive table: E13 has the cyclic window (1346), not the
printed (1236).  Its actual order is

\[
 (0,2,6,4,3,1,A,8,7,5,9).
\]

The six head colours retain the previously audited owner pairs

\[
\begin{array}{c|c}
478A&A3,E11\\
1347&A6,E12\\
139A&E2,E5\\
028A&B1,C3\\
0139&A2,A5\\
1289&D1,D3.
\end{array}
\]

None of the second owners in either table is cut at that same colour.
Therefore precisely (2358,3689,1569) are extinguished in the upper
ledger, proving the verdict.

## 5. Scope

There is a useful alternative choice of the third seed arc.  Replace

\[
 E13\longrightarrow E5,qquad (B^*,Y^*)=(0257,136A),
\]

by the independently certified physical seam

\[
 \boxed{E13\longrightarrow E9,qquad (B^*,Y^*)=(0469,158A).}
\tag{5.1}
\]

Its selected ports are

\[
 E13:(9,0,2,6,4)\quad\hbox{as a forward tail},
\]

\[
 E9:(9,3,0,4,6)\quad\hbox{as a reverse head}.
\]

The four removed old colours are

\[
\begin{array}{c|cc}
&B_0&Y_0\\ \hline
E13\text{ tail}&0246&578A\\
E9\text{ head}&0346&128A.
\end{array}
\tag{5.2}
\]

Three survive elsewhere:

\[
 0246\text{ in D1},\qquad578A\text{ in A8},\qquad
 128A\text{ in E6}.
\tag{5.3}
\]

The colour (0346) is unique to E9: it appears in no A--D template and in
no other E row.  Thus (5.1) has exactly one lower cut extinction.  The
alternative six-seam family

\[
\boxed{
D2\to E11,\quad A12\to E12,\quad E13\to E9,
\quad E4\to C3,\quad E8\to A5,\quad B3\to D3
}
\tag{5.4}
\]

has

\[
 \boxed{G_B=G_Y=6,\qquad L_B=5,\qquad L_Y=3.}
\tag{5.5}
\]

Its gains are

\[
\begin{aligned}
B^*:&\quad0256,0569,0469,1469,257A,347A,\\
Y^*:&\quad1478,347A,158A,0258,0369,1269.
\end{aligned}
\tag{5.6}
\]

They are pairwise distinct within each ledger, and the twelve row groups
are distinct.

At the level of **source-tail incidences**, the alternative seed is compatible
with the already proved full thirty-two-hole tail transversal.  In table (4.1) of
`K11_CORRECTED_TAIL_TRANSVERSAL_AND_COUPLED_GATE_20260725.md`, replace

\[
 E5-0569,quad E10-0469,quad E13-158A,quad E12-347A
\]

by

\[
 \boxed{A12-0569,quad E13-0469,quad E12-158A,quad B3-347A.}
\tag{5.7}
\]

The new tail rows A12 and B3 replace E5 and E10; all other rows and holes
remain unchanged.  Hence (5.7) still matches every one of the thirty-two
certified holes to a different tail row, while containing the six
**source** tail incidences of (5.4).

This is not yet a common-port completion.  A row used as the head of a seed
arc has its opposite tail endpoint fixed by that same oriented cut.  One
may not independently assign (for example) the E12 head port in (5.4) and a
different E12 tail incidence from (5.7).  Thus (5.7) proves only that there
is no row-level tail-matching obstruction after the six forced source
incidences.  Auditing the six fixed opposite tails, and then completing all
forty-two common ports, remains part of the global gate.

For comparison, reversing the first seed direction to (E11\to D2)
moves one unavoidable extinction from the lower ledger to the upper ledger.
With the original (E13\to E5) choice this gives

\[
 L_B=L_Y=4.
\]

With the alternative choice (5.1), it gives

\[
 (L_B,L_Y)=(4,4).
\]

Finally, reflection supplies a seventh row-disjoint double seam
(A7\to A11), with gains (1478,259A).  Its old cut colours are

\[
\begin{array}{c|cc}
A7\text{ reverse tail}&1348&256A\\
A11\text{ reverse head}&0148&239A.
\end{array}
\]

The first three are unique, while (239A) survives in A10.  Thus this
seventh seam adds two lower losses and one upper loss along with one gain in
each ledger.  It is physically valid but does not improve either net support
threshold.

This correction strengthens the local seed ledger but does not complete the
thirty-six-seam forest.  It also does not settle the separate positive
support audit proving that the corrected thirty-two certified holes are the
entire missing family.
