# Hall-21 native-socket router/splitter frontier

Date: 2026-07-28

Status: historical H21 input, superseded at the active frontier by
THREAD_H_HALL20_ROOTED_SOCKET_ATLAS_AND_REPEATED_AXIS_AUDIT_20260728.md.
The H21 outer-Hall descent, native-component atlas, common-profile splitter,
and repeated-axis rebase below remain valid. A provisional H20 carrier is
now proved, but no global common-word lift is proved.

## 1. Correct frontier

The authoritative route is

\[
H22/z6\xrightarrow{\operatorname{FF}(1320,5339,6194)}
H22/z6\xrightarrow{\operatorname{FR}(778,2292,6368)}H21/z6.   \tag{1.1}
\]

Its matching ranks are

\[
16361\longrightarrow16361\longrightarrow16362.                \tag{1.2}
\]

The first braid does not transport the old component: it replaces the
root-449 component of size 160/159 by a new root-458 component of size 24/23.
The second braid perfects and removes that new component.  This proves outer
Hall 21.  Its decisive edge to 458 is nonnative, so (1.1) does not lift the
global 16362-edge matching to one word.

The final canonical DM shore has size 846/825, consists of 21 gap-one
components, and its 825 right cells have distinct native traces under one
final controller.  The next literal-positive target is therefore not the
old H22 gate but a new H21 native socket which enlarges this atlas from 825
to 826 while carrying the exterior ledger.

## 2. Audited H22-to-H21 theorem

### Theorem 2.1

Let \(G_0,G_1,G_2\) be the compiler graphs of the three carriers in (1.1).
Then:

1. every middle chronology is an exact permutation of
   \(\binom{[15]}8\), is Johnson, is depth-three resident, has the fixed
   ordered endpoints 9901 and 7779, and has complete upper support at every
   depth \(1\le q\le7\);
2. the matching rank and deficiency sequences are (1.2) and
   \(22,22,21\), while the zero count remains six;
3. for \(G_0\to G_1\), a common matching core of rank 16337 and a contracted
   boundary bank of rank 24 before and after give total rank 16361;
4. for \(G_1\to G_2\), a common matching core of rank 16344 and contracted
   boundary ranks \(17\to18\) give total ranks \(16361\to16362\); and
5. the cross-shore gap matrix is

\[
\begin{pmatrix}
22&21&21\\
21&22&21\\
21&21&21
\end{pmatrix}.                                                   \tag{2.1}
\]

Consequently \(G_2\) has deficiency exactly 21.

#### Proof

The exact carrier reconstruction verifies item 1 and the six unchanged zero
targets.  The two displayed common-core matchings, together with the
contracted boundary matchings, give lower bounds

\[
16337+24=16361,
\qquad
16344+17=16361,
\qquad
16344+18=16362.                                                  \tag{2.2}
\]

The diagonal entries of (2.1) give shores of gaps 22,22,21 in the respective
graphs.  By the deficiency form of Hall's theorem, these cap the matching
ranks at 16361,16361,16362.  Equality follows from (2.2).  \(\square\)

The protected lower-support scope is smaller.  The lower-hole vectors are

\[
(4,18,6,1,0,0,0),\quad
(4,18,8,1,0,0,0),\quad
(4,18,9,1,0,0,0).                                               \tag{2.3}
\]

Thus immediate-lower support and all upper supports survive; lower depth
three does not.

## 3. Common-profile one-ear splitter

### Lemma 3.1

Let \(X\) be a target set in a unit component.  Suppose the old restricted
right-profile multiset is

\[
\mathcal C\sqcup\{A\},                                         \tag{3.1}
\]

and the endpoint bank is

\[
\mathcal C\sqcup\{A_0,A_1\}.                                  \tag{3.2}
\]

Assume distinct \(x_0,x_1\in X\) satisfy:

1. \(\mathcal C\) matches \(X\setminus\{x_0,x_1\}\);
2. \(x_1\in A\cap A_1\); and
3. \(x_0\in A_0\).

Then the old bank has a matching of size \(|X|-1\) exposing \(x_0\), while
the endpoint bank saturates \(X\).

#### Proof

Adjoin the edge \(x_1A\) to the matching of
\(X\setminus\{x_0,x_1\}\) into \(\mathcal C\).  This matches the old bank
and exposes \(x_0\).  At the endpoint, instead adjoin the two disjoint edges
\(x_0A_0\) and \(x_1A_1\).  This saturates \(X\).  \(\square\)

No partition identity \(A=A_0\dot\cup A_1\) is needed.

For (1.1), \(|\mathcal C|=22\) and

\[
\begin{aligned}
x_0&=458,&x_1&=16846,\\
A&=\{462,16846\},&
A_0&=\{458,462\},&
A_1&=\{16842,16846\}.
\end{aligned}                                                    \tag{3.3}
\]

This is the exact local source of the boundary-rank gain \(17\to18\).

## 4. Essential physical caveat

The new edge to 458 is not native.  Endpoint cell 7216 has depth one, start
778, envelope/native trace 462, mandatory mask 448, and restricted shore
\(\{458,462\}\).  Across the 24 final cells incident with the transient
component, the native traces take only 23 values: 458 is absent and 462 is
duplicated.

Therefore Lemma 3.1 proves a graph matching, not a common-Q lift of the
discharged component.  The final 825-pin native theorem concerns only the
residual 846-target canonical shore.  Neither the transient 24-edge component
matching nor the global 16362-edge matching is realized by one audited word.

## 5. Exact H21 component and native atlas

The final H21 shore is the following disjoint union of unit transversal
circuits.

\[
\begin{array}{c|l|c|c}
\text{size}&\text{intersection/native roots}&\text{root rank}
 &\text{native depths per component }(0,1,2)\\ \hline
169/168&1920&4&(9,44,115)\\
161/160&960,8217,24610&4&(9,43,108)\\
160/159&8218&4&(9,43,107)\\
5/4&4213,7504&6&(0,0,4)\\
3/2&1103,18970&6&(0,0,2)\\
2/1&2420,2575,2676,9524,17683,19568&6&(0,0,1)\\
1/0&13616,17738,21641,29776&6&(0,0,0)\\
1/0&5801,13620&7&(0,0,0).
\end{array}                                                     \tag{5.1}
\]

Thus there are five rank-four roots, fourteen rank-six roots, and two
rank-seven roots.  Ten of the rank-six roots are positive-component roots;
the other four rank-six roots and both rank-seven roots are the six zero
components.

All 825 right cells have pairwise distinct native traces and, componentwise,
give exactly every target except the displayed root.  Their depth census is

\[
\begin{array}{c|ccc}
\text{depth}&0&1&2\\ \hline
\text{count}&45&216&564\\
\text{native target rank}&5&6&7.
\end{array}                                                     \tag{5.2}
\]

Every one of these intervals is fully interior: the minimum start is 33 and
the maximum end is 6430.  More strongly, none of the 21 roots is the native
trace of any of the 19311 current compiler cells.  Hence the current H21
controller has no immediate native ear.

## 6. Fixed-endpoint grading at H21

For every fixed-endpoint protected segment braid, the ordered endpoints are
9901 and 7779.  The clipped controller values are

\[
9901,1709,1197,173
\quad\text{and}\quad
1571,1635,3683,7779.                                            \tag{6.1}
\]

None of the 21 roots is contained in either endpoint, so no root can occur
as a clipped-boundary native trace.  In the interior, the grading theorem
gives

\[
\text{native depths }0,1,2\quad\longleftrightarrow
\quad\text{ranks }5,6,7.                                       \tag{6.2}
\]

Consequently:

* a rank-six root requires a new fully interior depth-one native socket;
* a rank-seven root requires a new fully interior depth-two native socket;
* a rank-four root has no all-native socket in this architecture.

Servicing one of the six loop roots would reduce the zero count.  To retain
zero6, the native-socket lane must select one of the ten positive rank-six
roots.

## 7. Fixed-shore native-socket descent theorem

### Theorem 7.1

Let \(S\) be the 846-target H21 shore and let \(\mathcal R\) be its set of 21
intersection roots.  Suppose a protected fixed-endpoint endpoint graph has:

1. 825 target- and cell-distinct native pins realizing
   \(S\setminus\mathcal R\) under one final controller \(P\);
2. a distinct unused native cell whose trace is one positive root
   \(R\in\mathcal R\);
3. a target- and cell-disjoint 15537-edge matching on the complement of
   \(S\); and
4. a Hall shore of gap 20.

Then its matching rank is exactly 16363 and its deficiency is exactly 20.
The 826 shore pins are simultaneously realized by the single word \(P\).

#### Proof

The old native atlas plus the new root cell matches 826 distinct targets of
\(S\).  Together with the disjoint exterior matching this gives

\[
826+15537=16363.                                                \tag{7.1}
\]

The gap-20 shore gives the reverse bound
\(\nu\le16383-20=16363\).  Hence equality holds.  Since every one of the 826
shore pins is native under \(P\), adding the root pin changes no controller
intersection \(K_p\), and the shore pins are one-word feasible.  \(\square\)

This last conclusion is shore-local.  A global literal theorem additionally
requires all 15537 exterior pins, jointly with the 826 shore pins, to satisfy
the final-controller \(K_p\) criterion.  Graph disjointness and edgewise
feasibility do not imply that joint statement.

If a router changes the canonical shore, the invariant ledger is as follows.
For an intermediate \(c/(c-1)\) component, retain an outside matching of

\[
16362-(c-1)=16363-c                                             \tag{7.2}
\]

and perfect the component to size \(c\).  If the final canonical shore has
size \(s/(s-20)\), its native pin count is \(s-20\) and the genuinely exterior
count is \(16383-s\).

## 8. Six minimal nested splitter targets

The six smallest positive components are nested rank-6/rank-7 circuits:

\[
\begin{array}{c|c|c|c}
R&R^+&\text{current native }R^+\text{ cell}&(\text{depth},\text{start})\\ \hline
2420&2932&18663&(2,5788)\\
2575&2607&16684&(2,3809)\\
2676&10868&15770&(2,2895)\\
9524&9588&15772&(2,2897)\\
17683&21779&15761&(2,2886)\\
19568&27760&16699&(2,3824).
\end{array}                                                     \tag{8.1}
\]

For any row, retaining the displayed depth-two native \(R^+\) cell and
creating one distinct unused depth-one native \(R\) cell changes the local
native matching rank from one to two.  By (6.2), these depths are necessary
within the fully interior all-native architecture.  The same depth-one
native-root theorem applies to the four larger positive rank-six components,
but (8.1) is the smallest bank to carry through a router.

## 9. Repeated-axis-13 controller theorem

Write \(z=2^{13}=8192\).  The two repeated-axis circuits are

\[
2676\subset10868=2676\cup\{z\},
\qquad
19568\subset27760=19568\cup\{z\}.                              \tag{9.1}
\]

### Lemma 9.1 (unique cost-one near-ear demand)

Let \(R\) have rank six and let a current depth-one native trace
\(\tau=P_s\cup P_{s+1}\) satisfy

\[
|\tau\mathbin\triangle R|=2.                                  \tag{9.2}
\]

Write \(R\setminus\tau=\{a\}\) and \(\tau\setminus R=\{e\}\).
If \(e\) occurs in exactly one endpoint state \(P_q\), then the unique
one-state rank-preserving change which turns this interval into native trace
\(R\) is

\[
P_q\longmapsto P'_q=P_q-\{e\}+\{a\}.                           \tag{9.3}
\]

#### Proof

The extra coordinate \(e\) must be removed from its unique supporting
endpoint, and the missing coordinate \(a\) must be inserted into at least one
endpoint.  Changing only one rank-five state forces both operations to occur
at \(q\), giving (9.3).  Conversely (9.3) removes the only occurrence of
\(e\), supplies \(a\), and leaves every common coordinate unchanged, so the
new union is exactly \(R\).  \(\square\)

For root 2676 there are exactly 38 such near-ear intervals; 17 of their
forced replacements remain Johnson-adjacent to both unchanged neighbours.
For root 19568 the corresponding counts are 36 and 13.  Even the 30
Johnson-legal replacements are not deck-exact: each has controller incidence
\(+e_a-e_e\), contradicting the coordinatewise mod-3 law until compensated,
and its four affected middle windows still require exact multiset closure.

### Theorem 9.2 (minimal repeated-axis collars do not close)

The axis-13 near-ear candidates are exactly

\[
\begin{array}{c|c|c|c}
R&s&q&\text{forced replacement}\\ \hline
2676&986&986&8756\to628\quad(-13,+6)\\
2676&5281&5282&10772\to2612\quad(-13,+5)\\
19568&2177&2177&26704\to18544\quad(-13,+5).
\end{array}                                                     \tag{9.4}
\]

None is Johnson-legal with both neighbours fixed.  The respectively forced
neighbour-repair candidate sets are

\[
\begin{aligned}
\mathcal N_{986}&=\{372,852,8308,8788\},\\
\mathcal N_{5282}&=\{2836,2852,10772,10788\},\\
\mathcal N_{2177}&=\{6256,10352,22608,26704\}.                 \tag{9.5}
\end{aligned}
\]

No choice from \(\mathcal N_{986}\times\mathcal N_{2177}\), and no choice
from \(\mathcal N_{5282}\times\mathcal N_{2177}\), both satisfies the
coordinatewise mod-3 controller congruences and preserves the exact multiset
of affected four-window middle masks.  Hence two minimally repaired
same-axis collars cannot form an exact controller trade.

#### Proof

Substitution of (9.3) into the two adjacent Johnson equations gives exactly
the three four-element sets (9.5).  For the parallel pair at starts 5281 and
2177, the two demanded states alone have

\[
\Delta p_{13}=-2,qquad \Delta p_5=+2,                         \tag{9.6}
\]

and the alternative 986/2177 pair has

\[
\Delta p_{13}=-2,qquad \Delta p_6=Delta p_5=+1.              \tag{9.7}
\]

For each of the sixteen choices in either Cartesian product in (9.5), direct
coordinate subtraction leaves some \(\Delta p_x\not\equiv0\pmod3\).  Direct
union of each altered controller quadruple likewise gives a nonzero signed
middle-deck multiset.  These are exhaustive because (9.5) is the complete
solution set of the two local Johnson equations.  \(\square\)

The scope is minimal-collar only.  Any realization needs at least one further
incidence companion and a larger interacting deck circulation.

### Theorem 9.3 (exact neutral two-circuit physical rebase)

The current controller triples are

\[
\begin{aligned}
(P_{2895},P_{2896},P_{2897})&=(10788,8804,8308),\\
(P_{3824},P_{3825},P_{3826})&=(10352,11360,25696).
\end{aligned}                                                   \tag{9.8}
\]

Deleting \(z\) from all six physical letters gives

\[
\begin{aligned}
(10788,8804,8308)&\longmapsto(2596,612,116),\\
(10352,11360,25696)&\longmapsto(2160,3168,17504).              \tag{9.9}
\end{aligned}
\]

This preserves every ordered middle target.  Among the 825 selected native
shore pins, it changes exactly

\[
10868\longmapsto2676,
\qquad
27760\longmapsto19568,                                         \tag{9.10}
\]

and leaves the other 823 pins unchanged.  The resulting 825 targets remain
distinct.  Thus (9.9) is an exact common-word neutral rebase, not a matching
gain.

#### Proof

The coordinate \(z\) occurs throughout each five-state collar
\(P_{s-1},\ldots,P_{s+3}\), for \(s=2895,3824\).  No length-four central
window is contained in the three edited positions.  Every such window
meeting the triple therefore contains an unchanged flank carrying \(z\), so
deleting \(z\) from the central triple changes no central OR; all other
coordinates are untouched.  The two collars are 929 positions apart and
compose independently.  The frozen last-witness audit shows that only the
two focal depth-two pins lose their final \(z\)-witness, giving (9.10).
Neither root was previously selected, so target distinctness is retained.
\(\square\)

The new six letters have rank four, not five.  Four boundary controller
transitions cease to be Johnson:

\[
\begin{array}{c|c}
s=2895&\{0,5\}\to\{0,5,13\},\quad
        \{5,10\}\to\{5,10,13\}\\
s=3824&\{6,7\}\to\{6,7,13\},\quad
        \{9,10\}\to\{9,10,13\}.
\end{array}                                                     \tag{9.11}
\]

Hence (9.9) is a physical subword trade, not a new maximal controller.

### Corollary 9.4 (middle rethreading is necessary)

For the fixed ordered middle path \(T\), any rank-five interior controller
\(Q\) satisfying \(D^3Q=T\) equals the maximal erosion controller \(P\).
Consequently no nontrivial rank-five native-root socket can preserve this
ordered \(T\); it must rethread the middle chronology.

#### Proof

Every realizing word satisfies \(Q_j\subseteq P_j\).  Both sets have rank
five at every interior position, hence \(Q_j=P_j\).  \(\square\)

There is also a general congruence obstruction.  A nested socket retaining
one old depth-two child and creating an overlapping depth-one root removes
axis 13 from two controller states.  Two such same-axis sockets contribute
\(\Delta p_{13}=-4\not\equiv0\pmod3\).  Thus the repeated axis cancels
neither controller incidence nor full turn-colour holonomy; an external
companion with \(\Delta p_{13}\equiv1\pmod3\) and the remaining boundary
current is necessary.

## 10. Exact next gate

The current controller supplies none of the needed sockets.  A proof of
H21-to-H20/zero6 must therefore construct a genuine protected router which:

1. creates a new fully interior depth-one native socket for one of the ten
   positive rank-six roots, preferably a row of (8.1);
2. regenerates the other 825 native shore pins under the same final
   controller;
3. retains or reroutes the 15537-edge exterior matching;
4. retains a gap-20 shore and the fixed ordered endpoints;
5. preserves the exact middle deck, Johnson chronology, depth-three
   residence, all seven upper supports, immediate-lower support, and the six
   zero targets; and
6. passes the full joint common-Q ledger if a global literal matching is
   claimed.

The presently audited lower-hole vector is

\[
(4,18,9,1,0,0,0).                                              \tag{10.1}
\]

No claim of deeper-lower preservation should be made unless it is separately
verified.  No H20 endpoint, universal orbit-hitting theorem, or global
16362-edge common-word lift is presently proved.

## 11. Audit artifacts and computational scope

The finite input is

```text
scratch/k15_segment_braid_hall21_zero6.json
scratch/audit_k15_segment_braid_hall22_to21.json
```

with SHA-256 values

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c
```

All local work for this note was lightweight certificate parsing and proof
audit.  Any exhaustive segment-braid search from H21 is run only on the H100
CPU.
