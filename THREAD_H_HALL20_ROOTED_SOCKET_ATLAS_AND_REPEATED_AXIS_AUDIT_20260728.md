# Hall-20 rooted socket atlas and repeated-axis audit

Date: 2026-07-28

Status: exact audit of the frozen provisional H20/zero6 carrier. The
outer-Hall descent, the final rooted DM atlas, all current root sockets, and
the repeated-axis neutral rebase are proved. This note does **not** claim a
global common-controller lift, H19, or a complete \(k=15\) word.

## 1. Conventions

Put \(k=15\), \(r=8\), \(d=3\), and

\[
W=\binom{15}{8}=6435,\qquad
N=\sum_{j=1}^{7}\binom{15}{j}=16383.
\]

For an ordered rank-eight Johnson carrier
\(T=(T_0,\ldots,T_{W-1})\), let \(P=(P_0,\ldots,P_{W+2})\) be its maximal
depth-three erosion:

\[
P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i.                 \tag{1.1}
\]

A depth-\(s\) physical cell at start \(p\), \(0\le s\le2\), uses
\(P_p,\ldots,P_{p+s}\). Its native trace is

\[
n(p,s)=P_p\cup\cdots\cup P_{p+s}.                             \tag{1.2}
\]

The compiler graph has the \(N\) lower targets on the left and all

\[
(W+3)+(W+2)+(W+1)=19311                                      \tag{1.3}
\]

cells on the right. The edge rule is the exact mandatory/envelope rule of
the trace-two compiler. All bit axes below are zero based; thus axis \(13\)
means mask \(2^{13}=8192\), or coordinate \(14\) in one-based notation.

## 2. The certified H21-to-H20 descent

### Theorem 2.1 (outer-Hall descent)

The frozen carriers

    scratch/k15_segment_braid_hall21_zero6.json
    scratch/k15_segment_braid_hall21_compressed_dm702.json
    scratch/k15_segment_braid_hall20_zero6.json

form the exact route

\[
H21/z6\xrightarrow{\operatorname{RF}(1510,5017,6136)}
H21/z6\xrightarrow{\operatorname{RF}(885,1393,3668)}H20/z6.  \tag{2.1}
\]

The intermediate \(702/681\) carrier is the state labelled \(c0575\) in the
authoritative neutral-carrier census. This note takes that completed census
as fixed input and does not rerun or reprove its uniqueness claim.

Every state is a permutation of the rank-eight layer, is Johnson,
depth-three resident, has ordered endpoints \(9901,7779\), and has complete
upper support for every \(1\le q\le7\). The matching ranks are

\[
16362,\ 16362,\ 16363,                                        \tag{2.2}
\]

and the cross-state DM gap matrix is

\[
\begin{pmatrix}
21&20&20\\
20&21&20\\
20&20&20
\end{pmatrix}.                                                 \tag{2.3}
\]

The first move replaces the root-\(1920\) component of size \(169/168\)
by a root-\(1801\) component of size \(25/24\), leaving all other components
identical. The second move removes the whole \(25/24\) component. Its
restricted right-profile change is

\[
\mathcal C\sqcup\{\{1801,1803,1833,1835\}\}
\longrightarrow
\mathcal C\sqcup\{\{1801,1833\},\{1803,1835\}\},              \tag{2.4}
\]

where \(|\mathcal C|=23\) and \(\mathcal C\) matches all but the two
distinguished targets \(1801,1835\). Hence the contracted boundary ranks
are \(24\to24\) and then \(17\to18\).

#### Proof

Exact reconstruction of the three listed carrier arrays gives the carrier,
residence, endpoint, and upper-support assertions. After cancelling
identical complete cell shores with multiplicity, the first move has a
common profile graph of matching rank \(16338\), and the second has one of
rank \(16345\). Adding the certified contracted boundary matchings gives
respectively

\[
16338+24=16362,\qquad 16345+17=16362,\qquad
16345+18=16363.                                                \tag{2.5}
\]

The diagonal entries of (2.3) give the reverse bounds
\(N-21,N-21,N-20\) by Hall's theorem. Thus all three ranks in (2.2) are
exact. Direct alternating-component decomposition gives the two component
replacements. Finally, the common 23 profiles in (2.4) match the other 23
targets; the old four-target profile matches \(1835\), while the two new
profiles match \(1801\) and \(1835\), proving the unit rank gain. \(\square\)

The decisive edge to \(1801\) is nonnative. Among the 25 final cells for
that transient component there are only 24 distinct native traces: \(1801\)
is missing and \(1833\) is repeated. Thus Theorem 2.1 is an exact graph
matching theorem, not a global common-\(P\) theorem. The lower-hole vectors
are

\[
(4,18,9,1,0,0,0),\quad(4,18,11,1,0,0,0),\quad
(4,18,11,1,0,0,0).                                            \tag{2.6}
\]

In particular the route does not preserve lower depth-three support.

## 3. Exact H20 rooted-component theorem

### Theorem 3.1 (native rooted atlas)

For the H20 carrier of Theorem 2.1, the canonical DM shore has size
\(677/657\) and is the disjoint union of the following 20 unit-gap
components:

\[
\begin{array}{c|l|c}
\text{size}&\text{roots}&\text{root rank}\\ \hline
161/160&960,8217,24610&4\\
160/159&8218&4\\
5/4&4213,7504&6\\
3/2&1103,18970&6\\
2/1&2420,2575,2676,9524,17683,19568&6\\
1/0&13616,17738,21641,29776&6\\
1/0&5801,13620&7.
\end{array}                                                    \tag{3.1}
\]

For every component \(C=(X_C,Y_C)\), its root is

\[
R_C=\bigcap_{x\in X_C}x,                                      \tag{3.2}
\]

and the cells in \(Y_C\) have pairwise distinct native traces equal exactly
to \(X_C\setminus\{R_C\}\). Globally the 657 native cells have depth census

\[
\begin{array}{c|ccc}
s&0&1&2\\ \hline
\#&36&172&449\\
|n(p,s)|&5&6&7.
\end{array}                                                    \tag{3.3}
\]

None of the 20 roots is the native trace of any of the 19311 cells.

#### Proof

Starting with an exact maximum matching of rank \(16363\), alternate from
the 20 unmatched targets. The resulting connected components have the
sizes and intersections in (3.1); each has one more left than right vertex.
For each right cell, form the literal union (1.2). Component by component,
these unions are distinct and give every target except (3.2). Counting by
depth gives (3.3). Independently forming all 19311 unions (1.2) and testing
the 20 displayed masks gives no occurrence of a root. These checks use the
carrier itself, not a search log or an assumed transport from H21. \(\square\)

Set-theoretically, (3.1) is precisely the H21 atlas with the root-\(1920\)
component removed. The physical cells, however, are rethreaded; this is why
the next section audits them anew.

## 4. Complete current socket-child atlas

A root socket is a current cell whose restricted component shore is

\[
\{R,R^+\},\qquad R^+=R\mathbin{\mathrm{OR}}2^a.               \tag{4.1}
\]

Write an entry as

\[
a:R^+@c/p,                                                     \tag{4.2}
\]

where \(c\) is the global cell index and \(p\) its start. The exact atlas is
as follows.

For the rank-four components, every displayed cell has depth zero:

~~~text
R=960:
  0:961@1802/1802, 1:962@109/109, 2:964@6328/6328,
  3:968@5217/5217, 5:992@3103/3103, 11:3008@622/622,
  12:5056@2771/2771, 13:9152@6053/6053, 14:17344@6040/6040.
R=8217:
  1:8219@1806/1806, 2:8221@6324/6324, 7:8345@4729/4729,
  8:8473@4309/4309, 9:8729@4144/4144, 10:9241@361/361,
  11:10265@618/618, 12:12313@2775/2775, 14:24601@6044/6044.
R=8218:
  2:8222@6323/6323, 5:8250@1792/1792, 6:8282@1777/1777,
  7:8346@4728/4728, 8:8474@4310/4310, 9:8730@4145/4145,
  10:9242@362/362, 11:10266@617/617, 12:12314@2776/2776.
R=24610:
  0:24611@5869/5869, 2:24614@1794/1794, 4:24626@5166/5166,
  6:24674@1779/1779, 7:24738@4726/4726, 8:24866@4312/4312,
  9:25122@4147/4147, 10:25634@364/364, 11:26658@615/615.
~~~

For the positive rank-six components, every displayed cell has depth two:

~~~text
R=1103:  8:1359@18434/5559, 12:5199@15896/3021.
R=2420:  9:2932@15570/2695.
R=2575:  5:2607@17804/4929.
R=2676: 13:10868@16890/4015.
R=4213:  3:4221@13289/414, 8:4469@18114/5239,
          10:5237@15199/2324, 13:12405@16730/3855.
R=7504:  1:7506@15608/2733, 3:7512@13391/516,
           5:7536@15132/2257, 13:15696@17826/4951.
R=9524:  6:9588@16892/4017.
R=17683: 12:21779@16881/4006.
R=18970: 7:19098@18400/5525, 8:19226@18326/5451.
R=19568: 13:27760@17819/4944.
~~~

The six loop roots have no current socket. Every listed cell has envelope
and native trace \(R^+\), and its mandatory mask is contained in \(R\), so
its restricted shore is exactly (4.1). Conversely, inspection of every
cell adjacent to \(R\) shows that those whose component-restricted shore is
exactly \(\{R,R\mathbin{\mathrm{OR}}2^a\}\) are precisely the displayed
cells. There are \(54\) such sockets in total. Thus (4.2) is a complete
current-socket theorem, not a list of every root-adjacent cell.

For later use, the six minimal \(2/1\) rows, including their literal
controller data, are

\[
\begin{array}{c|c|c|c|c|c}
R&R^+&c&p&\text{mandatory}&(P_p,P_{p+1},P_{p+2})\\ \hline
2420&2932&15570&2695&2416&(868,2884,2836)\\
2575&2607&17804&4929&519&(2601,2602,2604)\\
2676&10868&16890&4015&2672&(10788,8804,8308)\\
9524&9588&16892&4017&1332&(8308,9300,9552)\\
17683&21779&16881&4006&17683&(5394,21762,20739)\\
19568&27760&17819&4944&19536&(10352,11360,25696).
\end{array}                                                    \tag{4.3}
\]

## 5. The repeated-axis motif survives physically

### Theorem 5.1 (axis-13 persistence and neutral rebase)

Among the six minimal rows (4.3), the only repeated optional axis is
\(a=13\):

\[
10868=2676\mathbin{\mathrm{OR}}8192,\qquad
27760=19568\mathbin{\mathrm{OR}}8192.                         \tag{5.1}
\]

Both socket payloads are literally the H21 payloads transported by \(1120\)
positions. Their start separation remains \(929\). The complete local
controller collars are

\[
\begin{aligned}
p=4015:&\quad(2693,10757,10788,8804,8308,9300,9552),\\
p=4944:&\quad(12464,10416,10352,11360,25696,25184,24928),
\end{aligned}                                                  \tag{5.2}
\]

where the edited triples are the third through fifth entries. Delete
\(8192\) from all six central letters:

\[
\begin{aligned}
(10788,8804,8308)&\longmapsto(2596,612,116),\\
(10352,11360,25696)&\longmapsto(2160,3168,17504).
\end{aligned}                                                  \tag{5.3}
\]

Then every four-letter OR, hence the ordered rank-eight middle deck, is
unchanged. Among the 657 selected native critical-shore cells, precisely the
two traces in (5.1) change:

\[
10868\longmapsto2676,\qquad27760\longmapsto19568.              \tag{5.4}
\]

The resulting 657 target traces are still distinct. Thus (5.3) is an exact
common-word neutral rebase of the H20 critical shore.

#### Proof

The two triples and the collars in (5.2) are literal entries of the H20
maximal erosion word. In each collar, the unedited letters immediately
before and after the triple still contain \(8192\): these are respectively

\[
10757,9300\qquad\text{and}\qquad10416,25184.                  \tag{5.5}
\]

For a triple \([p,p+2]\), the affected four-letter dilation windows start
at \(p-3,\ldots,p+2\). Each contains at least one of the two flanks
\(p-1,p+3\), and the corresponding flank values in (5.5) contain \(8192\).
Hence every affected window retains \(8192\); every other bit and every
disjoint window is untouched. Therefore the ordered middle deck is
unchanged.

There are exactly three selected native cells whose intervals meet either
edited triple:

\[
\begin{array}{c|c|c|c}
c&(s,p)&\text{controller positions}&\text{trace change}\\ \hline
16890&(2,4015)&[4015,4017]&10868\to2676\\
16892&(2,4017)&[4017,4019]&9588\to9588\\
17819&(2,4944)&[4944,4946]&27760\to19568.
\end{array}                                                    \tag{5.6}
\]

The middle row survives because its two unedited letters are
\(P_{4018}=9300\) and \(P_{4019}=9552\). Thus (5.6) is a complete local
certificate that (5.4) lists all selected-trace changes. Neither root
occurred among the old 657 traces, while each replaced child ceases to occur
at its selected cell, so distinctness is preserved. The collars are
disjoint, hence the two changes compose. \(\square\)

This is a physical persistence theorem but not a descent theorem. It gains
no matching rank: it exchanges the two missing roots for the two formerly
present children. The physical-word coordinate-13 incidence changes by
\[
p_{13}:2145\longmapsto2139,                                   \tag{5.7}
\]
while every other coordinate incidence is unchanged. Thus the mod-\(3\)
residue is numerically preserved by this paired physical-word edit.
This is not an application of the maximal-controller congruence and gives
no rank-five rethreading certificate. Indeed every new letter in (5.3) has
rank four, and the four exterior controller boundaries fail Johnson
adjacency. Thus
(5.3) is not a rank-five Johnson/maximal-controller rethreading. It creates
two root traces, but creates no additional selected occurrence or capacity:
each new root trace replaces one selected child trace, so the selected bank
still has size \(657\).

## 6. Exact next ledger and obstruction

The final H20 shore splits its current exact matching as

\[
657+15706=16363,                                               \tag{6.1}
\]

where 657 is the one-controller native shore atlas and 15706 is an exact
matching on the complement of the 677-target shore whose right cells are
disjoint from the reserved 657-cell atlas. A fixed-shore H19 descent would
require

\[
658+15706=16364                                                \tag{6.2}
\]

and a surviving gap-19 Hall shore. More generally, if a router exposes a
\(c/(c-1)\) component while retaining its existing
component-exterior matching service, the required component-exterior rank is

\[
16363-(c-1)=16364-c.                                          \tag{6.3}
\]

This is the exterior service needed to retain the current H20 rank before
adding a new root occurrence; perfecting the component would then add the
one unit needed for H19.

Within the fixed-shore, all-native common-word architecture, the precise
remaining obstruction is therefore not component topology and not the
availability of same-axis native sockets. It is a protected rethreading
which creates one **additional** native root occurrence while simultaneously
retaining:

1. the other 657 critical-shore occurrences or an equally large distinct
   replacement bank;
2. the 15706 exterior matching;
3. a gap-19 Hall shore;
4. the rank-five Johnson controller, exact middle deck, depth-three
   residence, and all upper supports; and
5. the required lower supports and one common controller for every claimed
   literal cell.

Only the 657 critical pins in (6.1) currently have a common-controller
certificate. The exterior matching is graph-theoretic; it has not been
lifted jointly to that controller. Consequently neither (6.1) nor the
provisional H20 carrier proves the finite \(k=15\) formula. Outside the
fixed-shore architecture, a changed DM shore, component compression, or a
nonnative common-word repair could in principle gain rank without creating
one of the current roots; this note proves no no-go for those routes.

## 7. Audit provenance

No segment-braid enumeration was run for this note. The fixed H20 carrier
was reconstructed once and its finite certificate was parsed independently.
The principal SHA-256 values are

~~~text
9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
  scratch/k15_segment_braid_hall20_zero6.json
0c09b3051ecb3cc2b2e75e40b51a46cf3593e097e8e65a983913a9ff1723a9b5
  scratch/audit_k15_h21_h20_compression_descent.json
a1d0b664c4628517d45c1717a554fae7274257a0e41b943144f1165dea79a5f1
  scratch/audit_k15_h21_h20_compression_theorem.json
84e0ba2786e493259dc8da16c1516b06036ccd48490494c3e97b473294fb2ca5
  scratch/audit_k15_h21_h20_root1801_structure.json
7e0d4b28fdd53befd9480ee6cc4a38c5d1603fdb4c678ac5e0e28b8646d941d1
  scratch/audit_k15_h20_root1801_chain_independent.json
6aacaa197fa130bd94fda2812784f742e1257558751d029238f9237cb4795481
  scratch/audit_k15_h21_component_ports.py
~~~

The route was also cross-checked by the independent audits with hashes

~~~text
b730c31f963d60fbfa09b63e1f8caaa02be0762574304d9be2e9308f7def6d03
99c3f515f7d1f536b8fa88232895876e7c80081b788380a580097cfbebfed0e5
~~~

for scratch/audit_k15_h21_to_h20_root1801_chain.json and
scratch/audit_k15_h21_router1801_to_h20.json, respectively.
