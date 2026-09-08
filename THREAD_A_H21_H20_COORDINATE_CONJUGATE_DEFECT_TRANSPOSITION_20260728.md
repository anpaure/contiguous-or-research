# Thread A: Hall-21 to Hall-20 by a coordinate-conjugate defect transposition

Date: 2026-07-28

Status: exact audited Hall descent, exact comparison with the preceding
\(449\to458\) router, and a reusable sufficient search criterion. This is
not yet a Hall-zero carrier or a full exterior common-word certificate.

## 1. Exact route

Starting from the canonical Hall-21/six-zero carrier,

\[
 H21\xrightarrow{RF(1510,5017,6136)}H21^{\mathrm{port}}
 \xrightarrow{RF(885,1393,3668)}H20.                    \tag{1.1}
\]

The states are

    scratch/k15_segment_braid_hall21_zero6.json
    scratch/k15_segment_braid_hall21_compressed_dm702.json
    scratch/k15_segment_braid_hall20_zero6.json

with SHA-256 values

    8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
    ea5259c4bb8a15444da135f7c6369e11fbc059f322c570fd3db2e6b8509af337
    9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1.

The independent route audit is

    scratch/audit_k15_h21_h20_compression_descent.json

with SHA-256

    0c09b3051ecb3cc2b2e75e40b51a46cf3593e097e8e65a983913a9ff1723a9b5.

The exact state ledger is

\[
\begin{array}{c|ccc}
&H21&H21^{\rm port}&H20\\ \hline
\nu&16362&16362&16363\\
h&21&21&20\\
z&6&6&6\\
|S|/|T|&846/825&702/681&677/657.
\end{array}                                             \tag{1.2}
\]

Every state is a permutation of all 6,435 rank-eight masks, a Johnson path,
depth-three resident, and complete in every upper support layer. The
lower-hole vectors are

\[
(4,18,9,1,0,0,0),\quad
(4,18,11,1,0,0,0),\quad
(4,18,11,1,0,0,0).                                    \tag{1.3}
\]

Thus the route preserves the four immediate-lower holes and all upper
supports, but not the depth-three lower support.

The cross-shore gap matrix is

\[
\begin{pmatrix}
21&20&20\\
20&21&20\\
20&20&20
\end{pmatrix}.                                          \tag{1.4}
\]

Both the portal and final canonical DM-right shores are native-injective:
the maximal erosion controller gives respectively 681 and 657 distinct
valid native traces. Hence their shore-local common-\(Q\) gaps are exactly
21 and 20.

## 2. What the neutral router does

In \(H21\), the large component rooted at \(1920\) has size

\[
169/168,\qquad (n_4,n_5,n_6,n_7)=(1,9,44,115).          \tag{2.1}
\]

The first braid saturates this component and transfers the unique missing
matching unit to a new \(25/24\) component rooted at \(1801\). Its targets
are

\[
\begin{aligned}
\{&1801,1803,1805,1807,1833,1835,1837,1865,1867,1869,1897,1933,1993,\\
  &5897,5899,5961,9993,9997,10025,14089,18185,18187,18249,22281,26377\}.
\end{aligned}                                             \tag{2.2}
\]

The target \(1933\) is the sole overlap between the old \(1920\)-component
and the new component; the other 24 targets are new to the canonical DM
shore.

The first transition changes 29 full cell-shore occurrences. After
multiset cancellation, the common full bank has matching rank 16,338, and
the contracted ranks are

\[
24\longrightarrow24.                                    \tag{2.3}
\]

Thus this is a neutral rank-one defect transposition, not a hidden Hall
gain.

## 3. Exact recurrence of the old \(449\to458\) router

Compare (1.1) with the preceding neutral router

\[
 H22\xrightarrow{FF(1320,5339,6194)}H22^{\rm port},      \tag{3.1}
\]

which saturated the \(160/159\) component rooted at \(449\) and created a
\(24/23\) component rooted at \(458\).

Define the coordinate permutation

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
x&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
\phi(x)&7&3&4&0&6&13&8&9&10&5&12&2&14&11&1.
\end{array}                                               \tag{3.2}
\]

It has the following exact properties.

1. It maps the three old seam edges of (3.1), as an unordered edge
   multiset, to the three old seam edges of the first braid in (1.1).
   It likewise maps the three new seam edges to the three new seam edges.
   Their different physical order and orientation explain \(FF\) versus
   \(RF\).
2. It maps the complete multiset of 29 deleted full cell shores in (3.1)
   to the complete multiset of 29 deleted shores in (1.1).
3. It maps the complete multiset of 29 inserted full cell shores in (3.1)
   to the complete multiset of 29 inserted shores in (1.1).

There are six coordinate permutations with these complete full-bank
properties. Thus the successful Hall-21 router is not merely analogous to
the old router: its entire exact compiler collar is a coordinate conjugate.

Both routers have the identical full-shore size histograms

\[
\begin{array}{c|rrrr}
&2&4&8&16\\ \hline
\text{deleted}&3&16&10&0\\
\text{inserted}&3&11&14&1.
\end{array}                                                \tag{3.3}
\]

The new route's sorted full-bank digests are

    deleted e587af41c8f9c753995a9ca273e3b80734c93111aefcb7b847a5b0fec3a39763
    inserted aa964bf1f57ed87ecb7b1f3ea130477f293ffc8ea509eb98e3b00e9b8d3501af.

## 4. The two coupled restricted-bank moves

The full collar conjugacy decomposes into one positive and one negative
restricted rank move.

### 4.1 Large-component promotion

For the old \(449\)-component, the restricted bank changes as

\[
\begin{array}{c|ccc}
&\text{common}&\text{deleted}&\text{inserted}\\ \hline
\#\text{ columns}&153&6&7\\
\text{rank}&153&6&7.
\end{array}                                                \tag{4.1}
\]

Hence its total rank rises \(159\to160\). The exact deleted shores are

\[
\begin{gathered}
\{449,451,459\},\quad \{449,451,1473,1475\},\\
\{465,467,1489,1491\},\quad \{483,491\},\\
\{1473,1475,1481,1483\},\quad \{2497,2499,3521,3523\},
\end{gathered}                                             \tag{4.2}
\]

and the inserted shores are

\[
\begin{gathered}
\{449,451\},\{459\},\{491\},\{1473,1475\},\\
\{1473,1475,1489,1491\},\{1481,1483\},\{3521,3523\}.
\end{gathered}                                             \tag{4.3}
\]

For the \(1920\)-component, the corresponding ledger is

\[
\begin{array}{c|ccc}
&\text{common}&\text{deleted}&\text{inserted}\\ \hline
\#\text{ columns}&162&6&7\\
\text{rank}&162&6&7,
\end{array}                                                \tag{4.4}
\]

so its total rank rises \(168\to169\). The deleted shores are

\[
\begin{gathered}
\{1920,1928,1929\},\quad\{1920,1928,6016,6024\},\\
\{1924,1932,6020,6028\},\quad\{1984,1992,6080,6088\},\\
\{6016,6017,6024,6025\},\quad\{10120,10121\},
\end{gathered}                                             \tag{4.5}
\]

and the inserted shores are

\[
\begin{gathered}
\{1920,1928\},\{1929\},\{6016,6024\},\\
\{6016,6024,6080,6088\},\{6017,6025\},\\
\{6020,6028\},\{10121\}.
\end{gathered}                                             \tag{4.6}
\]

Permutation \(\phi\) maps (4.2)--(4.3) exactly to
(4.5)--(4.6).

### 4.2 Compensation-component demotion

For the new \(458\)-component the old graph supplies three independent
singleton columns, while the routed graph supplies two independent edge
columns:

\[
\begin{array}{c|ccc}
&\text{common}&\text{deleted}&\text{inserted}\\ \hline
\#\text{ columns}&21&3&2\\
\text{rank}&21&3&2,
\end{array}                                                \tag{4.7}
\]

with

\[
\{\{458\},\{1482\},\{1498\}\}
\longrightarrow
\{\{458,1482\},\{474,1498\}\}.                             \tag{4.8}
\]

For the new \(1801\)-component the exact ledger is

\[
\begin{array}{c|ccc}
&\text{common}&\text{deleted}&\text{inserted}\\ \hline
\#\text{ columns}&22&3&2\\
\text{rank}&22&3&2,
\end{array}                                                \tag{4.9}
\]

with

\[
\{\{1801\},\{5897\},\{5961\}\}
\longrightarrow
\{\{1801,5897\},\{1865,5961\}\}.                          \tag{4.10}
\]

Again \(\phi\) maps (4.8) exactly to (4.10). The unchanged background
expands the two compensation seeds differently, giving component sizes
\(24/23\) and \(25/24\); component size itself is therefore not the
portable invariant.

Equations (4.1)--(4.10) exhibit the mechanism:

\[
\boxed{\text{large component }(+1)\quad+\quad
       \text{compensation component }(-1).}               \tag{4.11}
\]

The global boundary rank is neutral, while the unique missing matching
unit is moved to a small component.

## 5. The local splitter

The second braid in (1.1) removes exactly the complete \(25/24\) component
(2.2), adds no DM target, and raises the global matching rank by one. Its
common full bank has rank 16,345 and its contracted boundary rank changes

\[
17\longrightarrow18.                                     \tag{5.1}
\]

Restricted to the \(1801\)-component, 23 common columns retain rank 23 and
the only changed incidence is

\[
\{1801,1803,1833,1835\}
\longrightarrow
\{1801,1833\},\ \{1803,1835\}.                            \tag{5.2}
\]

Thus the component rank changes \(24\to25\).

The preceding splitter of the \(458\)-component had the identical rank
profile: 22 common columns, followed by

\[
\{462,16846\}
\longrightarrow
\{458,462\},\ \{16842,16846\},                            \tag{5.3}
\]

and rank \(23\to24\). The full 32-cell splitter collars are not coordinate
conjugate, but their exact component-local and contracted-rank ledgers are
the same:

\[
\boxed{\text{one restricted column of rank 1}
\longrightarrow\text{two columns of rank 2},\qquad
17\longrightarrow18.}                                    \tag{5.4}
\]

## 6. Defect-transposition theorem

Let \(G_0,G_1\) be two exact compiler graphs related by a legal segment
braid. Let \(C\) be a unit-gap DM component of \(G_0\), and let \(B\) be a
target set which becomes a unit-gap DM component of \(G_1\). Suppose there
is one matching \(M\) in the common cell-shore bank which extends to a
maximum matching in each graph. Delete the targets and cells used by \(M\).
Assume that the two residual boundary graphs decompose block-diagonally
into a \(C\)-block, a \(B\)-block, and an unchanged remainder, and that:

1. the \(C\)-block ranks are \(6\) before and \(7\) after;
2. the \(B\)-block ranks are \(3\) before and \(2\) after;
3. the unchanged residual block has the same rank in both states;
4. the resulting \(C\)-bank is saturated, while the resulting \(B\)-bank
   has gap one.

Then \(\nu(G_1)=\nu(G_0)\): the braid saturates \(C\) and creates exactly
one replacement deficit on \(B\). If a second legal braid preserves the
common complement matching, replaces one rank-one \(B\)-column by two
rank-two-independent columns, and creates no new deficient component, then
the second braid raises the global matching rank by one.

### Proof

The block decomposition makes matching rank additive after \(M\) is
contracted. The \(C\)-block contributes one more edge, the \(B\)-block one
fewer, and the remainder is unchanged. Thus total rank is unchanged and
the local deficit moves from \(C\) to \(B\). In the second braid the common
matching and unchanged block remain, while the stipulated \(1\to2\)
replacement adds exactly one independent \(B\)-edge. No new deficient
component exists, so the global matching rank rises by one. \(\square\)

For both audited routers, \(b=24\). For both audited splitters, the
contracted boundary rank is \(17\to18\).

## 7. Predictive finite criterion

The successful recurrence gives a substantially sharper search rule than
generic neutral-neighbour scoring.

1. Use the first router's complete radius-six cut/seam collar as a labelled
   template. Search for coordinate images whose three old boundary edges
   occur as physical path edges, in any order and orientation.
2. Require a legal segment rearrangement whose three new seams realize the
   alternate \(C_6\) matching and whose complete 29 deleted and inserted
   full-shore multisets equal the corresponding coordinate images. Endpoint
   colours alone are insufficient.
3. Check the \(6\to7\) promotion and \(3\to2\) compensation ledgers
   (4.1) and (4.7), with the full contracted boundary rank \(24\to24\).
   Compute the actual alternating closure of the compensation seed; do not
   prescribe its component size.
4. Search only splitter collars meeting that closure. Accept a splitter
   when its restricted ledger is \(1\to2\), its contracted rank is
   \(17\to18\), and the final canonical DM shore is nested with no added
   target.
5. Finally verify the exact Johnson path, residence, every upper support
   layer, the desired lower-hole budget, the full matching, and native or
   exact common-\(Q\) pins.

This criterion predicted the actual first move after the fact because the
entire 29-cell router bank, not just a marginal histogram, is a coordinate
conjugate of the previous successful router. It is a sufficient
construction rule. A failure to find another coordinate image would not
exclude unrelated compound routers.

## 8. Exact scope

The Hall descent \(21\to20\), six-zero preservation, all-upper support,
four immediate-lower holes, native-injective portal/final DM shores, and
the recurrent defect-transposition mechanism are proved. The depth-three
lower-hole count is eleven, and no claim is made that the remaining
15,706 exterior matching edges are simultaneously compiled by the same
literal word. Hall-zero and the exact contiguous-OR formula therefore
remain open.
