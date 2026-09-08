# A four-block octagon relation is a genuine (4g_8) OR-language move

Date: 2026-08-01  
Status: exact width-graded source theorem, exact circuit/action theorem, and
exact zero-length owner-residence repair.  The resulting owner bank is not
flat or simple, so this is not yet a Catalan-factor/CBC lift.

## 0. Outcome

Let (Q^0,Q^1) be the **unexpanded sharp depth-(d) inverses** of the
resident quaternary octagon, of length (9d+23).  Write

\[
 L=\{a_0,a_1\},\qquad R=\{a_1,a_2\},
\]

and let

\[
 \alpha=(a_0\ a_2),\qquad \beta=(a_1\ a_3),\qquad
 V=\{1,\beta,\alpha,\alpha\beta\}.
\]

For (pi\in V) and (e\in\{0,1\}), put

\[
 G_{\pi,e}=\pi(L)\mid \pi(Q^e)\mid \pi(R).                 \tag{0.1}
\]

Define the two four-block words

\[
\begin{aligned}
 {cal W}^-&=G_{1,0}G_{\beta,1}G_{\alpha,1}G_{\alpha\beta,0},\\
 {cal W}^+&=G_{1,1}G_{\beta,0}G_{\alpha,0}G_{\alpha\beta,1}.
                                                               \tag{0.2}
\end{aligned}
\]

For every (d\ge2):

1. ({\cal W}^-) and ({\cal W}^+) have the same interval-OR multiset
   **at every width**, and remain equal in every fixed exterior context;
2. their octagon-incidence action is (4g_8\ne0), not a stabilized null
   move;
3. four blocks are minimum in the relabelled sharp-block class; among all
   (24) active-label relabellings, there are twelve oriented minimum
   support-four relations having nonzero octagon action;
4. the depth-(d) owner rows (D^d({\cal W}^pm)) are internally resident,
   but their clipped boundary runs are too short;
5. two phase-common **satellite augmentations per block**, at distance (d)
   from the two guards, repair the entire clipped residence signature with
   **zero added positions**, while preserving the width-graded relation;
6. neither the raw nor the satellite word is a flat simple owner bank.  The
   raw central owner bank has (32d+92) occurrences but only (8d+24)
   distinct values, and private uniform block tags cannot separate them.

Thus this is the first authenticated source-level move which is both fully
OR-transparent and nonzero on the indispensable quartic state.  Its remaining
obstruction is physical owner simplicity/rank, not OR transparency or
residence.

## 1. The character identity behind the four blocks

For a set (X), let ([X]) denote its basis vector in the free abelian
module on subsets, and define the (V)-character projection

\[
 \chi[X]=(1-\alpha)(1-\beta)[X]
          =[X]-[\alpha X]-[\beta X]+[\alpha\beta X].       \tag{1.1}
\]

Fix one relative interval address (I=[s,t]) in the guarded base block and
write (X_e(I)=\bigvee_{j\in I}(G_{1,e})_j).  Expanding (0.2), equality of
the four occurrence multisets at this one address is exactly

\[
                  \chi[X_0(I)]=\chi[X_1(I)].              \tag{1.2}
\]

The labels fixed by (V) agree addresswise in the two phases.  On the four
active (a)-labels, (chi[X]) vanishes unless (X) contains exactly one
label from each opposite pair

\[
                       \{a_0,a_2\},\qquad\{a_1,a_3\}.      \tag{1.3}
\]

Directly from the eight-owner path and the sharp inverse formula, whenever
one phase has a nonzero projection, the two active interval unions are
literally equal.  The complete nonzero list is

\[
 \{a_i,a_j\},\quad \{z,a_i,a_j\},
 \qquad i\in\{0,2\},\ j\in\{1,3\}.                       \tag{1.4}
\]

This proves (1.2), uniformly in (d), and hence exact addresswise balance
of all intervals lying inside one block.

There are three seams.  The explicit prefix/suffix formulas give, for all
positive (u,v),

\[
\begin{aligned}
 \operatorname{Suf}_u(G_{1,0})\vee
 \operatorname{Pre}_v(G_{\beta,1})
 &=\operatorname{Suf}_u(G_{1,1})\vee
   \operatorname{Pre}_v(G_{\beta,0}),\\
 \operatorname{Suf}_u(G_{\beta,1})\vee
 \operatorname{Pre}_v(G_{\alpha,1})
 &=\operatorname{Suf}_u(G_{\beta,0})\vee
   \operatorname{Pre}_v(G_{\alpha,0}),\\
 \operatorname{Suf}_u(G_{\alpha,1})\vee
 \operatorname{Pre}_v(G_{\alpha\beta,0})
 &=\operatorname{Suf}_u(G_{\alpha,0})\vee
   \operatorname{Pre}_v(G_{\alpha\beta,1}).             \tag{1.5}
\end{aligned}
\]

Thus the crossing intervals are equal **pointwise**, not only after summing
over seams.  Every interval spanning a complete block sees the common total
union of all active/filler labels.  Equations (1.2) and (1.5) therefore give
a width-preserving occurrence bijection for every interval.

Finally the complete macro prefixes and suffixes agree pointwise.  Any
interval entering from a fixed left context or leaving into a fixed right
context consequently transports with the same width and value.  We have
proved

\[
 \boxed{\operatorname{Deck}_q(X{\cal W}^-Z)
       =\operatorname{Deck}_q(X{\cal W}^+Z)
       \quad\text{for every }q\text{ and all fixed }X,Z.} \tag{1.6}
\]

## 2. The action is (4g_8), not zero

Let

\[
 O=\{A_iB_i:0\le i<4\},\qquad
 N=\{A_iB_{i-1}:0\le i<4\},\qquad g_8=N-O.              \tag{2.1}
\]

Both (alpha) and (eta) interchange (O) and (N), while
(alphaeta) preserves them.  Therefore

\[
       \alpha g_8=\beta g_8=-g_8,
       \qquad \alpha\beta g_8=g_8.                       \tag{2.2}
\]

The four phase changes in (0.2) have signs (+,-,-,+).  Hence

\[
 g_8-\beta g_8-\alpha g_8+\alpha\beta g_8=4g_8.          \tag{2.3}
\]

This is exactly why the construction escapes the guarded-doublet no-go: a
doublet carries one phase and its inverse and has zero net action, whereas
the character signs in (0.2) turn all four relabelled actions in the same
direction.

## 3. Four is minimum in the relabelled-block fibre

For (pi\in S_4), let (v_\pi) be the full **addressed** graded-signature
difference

\[
 v_\pi=\Sigma(G_{\pi,1})-\Sigma(G_{\pi,0}),              \tag{3.1}
\]

where the row key records relative start, relative end, and literal OR
value.  Exact enumeration of the (24) columns gives

\[
\begin{array}{c|rrrr}
\text{signed support}&1&2&3&4\\ \hline
\text{relations up to global sign}&0&0&0&18.
\end{array}                                               \tag{3.2}
\]

Of the (18) support-four circuits, (12) are null on the octagon edge
state and (6) are nonzero.  Counting both orientations gives exactly

\[
                         12                                \tag{3.3}
\]

oriented support-four nonzero relations.  The relation (0.2) is the member
whose action is (+4g_8).  The same census remains true after the satellite
repair of Section 5.

This is an exact finite active-quotient classification, not a random-search
observation.  The replay forms the integer Gram matrix of all addressed
columns; a signed combination is zero exactly when its Gram norm is zero.

## 4. Occurrence pairing and tag rigidity

For each addressed key (k=(s,t,X)), record the four signed block
contributions to (0.2).  There are ten possible nonzero patterns.  This
corrects a tempting but false simplification: not every row is
(pm(1,-1,-1,1)).  Both four-entry rows and sparse two-entry rows occur.

The sparse rows force precisely the four undirected block pairs

\[
              0-1,\qquad0-2,\qquad3-1,\qquad3-2,          \tag{4.1}
\]

which form the connected graph (K_{2,2}) with shores
({0,3}mid{1,2}).  A uniform private tag attached to every letter of
one block must agree across every forced pair.  Connectivity of (4.1) then
forces all four tags equal.  Hence block-private tags cannot turn the four
repeated owner copies into distinct owners without destroying (1.6).

There is nevertheless an exact occurrence pairing.  On a sparse row, pair
its unique positive occurrence to its unique negative occurrence.  On a
four-entry row, use (0\leftrightarrow1) and (3\leftrightarrow2), reversing
arrows when the signs reverse.  Every pair has the same address, width, and
literal value.

Two further facts are load-bearing:

* sparse rows force edges from **both** perfect matchings of (K_{2,2}), so
  no one perfect matching pairs the entire residue;
* the largest paired width is

\[
                           6d+15,                          \tag{4.2}
\]

  and many pairs have width (>d).  This is a global shared-tag rail, not a
  lower-collar-only relation.

## 5. Residence: zero-length satellite repair

For every source word (A), every internal positive run of a coordinate in
(D^dA) has length at least (d+1): one source occurrence at position (p)
contributes the owner interval ([p-d,p]), and a connected union of such
length-((d+1)) intervals cannot have a shorter internal component.

Thus (D^d({\cal W}^{\pm})) are internally resident automatically.  The
problem is clipped boundary safety.  Several active/filler coordinates have
positive leading or trailing runs of lengths (1,2,\ldots,d).  An ambient
neighbour omitting such a coordinate would turn that clipped run into an
illegal internal run.

Literal repetition of every (L_\pi,R_\pi) guard (d+1) times preserves
the OR relation, but costs (8d) new positions and still does not make the
owner row flat.  A sharper repair costs zero length.

Let (Phi=\{f_0,\ldots,f_{d+1}\}) be the filler set and let
(n=|G_{1,e}|=9d+25).  In every block, augment the two existing source
letters at zero-based addresses (d) and (n-1-d) by

\[
                L\cup\Phi,qquad R\cup\Phi,              \tag{5.1}
\]

respectively, and then apply the block relabelling (pi).  Call the
resulting blocks (widehat G_{\pi,e}).

The modification is phase common and (V)-equivariant.  The character and
seam calculations of Section 1 remain valid addresswise, so the two
four-block words (widehat{\cal W}^{\pm}) still satisfy (1.6).  It changes
two existing cells per block and inserts none.  The original pointwise
common cap is enlarged at precisely those addresses by the same
(L\cup\Phi) or (R\cup\Phi), so cap commonality is retained (although cap
rank may increase).

At the owner level, the left satellite at source distance (d) contributes
every left-screen/filler coordinate to owner starts (0,\ldots,d); the
right satellite is dual.  Therefore every positive boundary run is either
zero or at least (d+1).  The clipped signatures of the two phases agree,
so the result remains safe after arbitrary ambient clipping:

\[
 \boxed{\text{full clipped depth-}d\text{ residence at zero added length}.}
                                                               \tag{5.2}
\]

If an incumbent prescribed cap forbids enlarging those eight letters, insert
the satellites instead.  The same proof gives exact graded transparency and
clipped residence using two new cells per block, hence **eight new cells in
total**, independently of (d).  Its owner ranks are

\[
              r^{,24d+100}(r+2)^6(r+3)^{,11d+2}.        \tag{5.3}
\]

Thus the screen-residence problem has both a zero-length mutable-cap solution
and a constant-length insertion-only solution.  Neither is rank-flat.

## 6. Exact physical obstruction

Let (r=d+3) after suppressing the common core.  The raw concatenated
source macro has (35d+100) width-((d+1)) owner windows, with rank
histogram

\[
\begin{array}{c|ccc}
\text{rank}&r&r+2&r+3\\ \hline
\text{occurrences}&32d+92&14&3d-6.
\end{array}                                                \tag{6.1}
\]

The central rank-(r) bank has only (8d+24) distinct values:

\[
             2^2\,4^{,8d+22}.                            \tag{6.2}
\]

The original four owner paths have the same defect, and their lower-(q1)
bank is also fourfold repeated.  The deduplicated physical graph has maximum
degree four, not two.

The zero-length satellite repair improves residence but worsens the rank
ledger:

\[
\begin{array}{c|ccc}
\text{rank}&r&r+2&r+3\\ \hline
\text{occurrences}&24d+92&6&11d+2.
\end{array}                                                \tag{6.3}
\]

Consequently the satellite theorem is a real residence result, but not a
flat-carrier result.  A physical CBC lift must now do one of the following:

1. weave/identify the four owner copies in a quotient chronology while
   retaining the (K_{2,2}) occurrence pairing;
2. plant rank-correct resident satellites whose owner windows replace, rather
   than elevate, the affected rank-(r) windows; or
3. use a nonflat common-cap theorem able to absorb the (O(d)) off-rank
   staircase.

The exact positive conclusion is therefore

\[
 \boxed{\text{context-transparent }4g_8
        +\text{ zero-length residence repair}},           \tag{6.4}
\]

while the exact remaining gate is

\[
 \boxed{\text{simple rank-correct owner/palette physicalization}}. \tag{6.5}
\]

## 7. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_c8_fourblock_graded_relation_and_residence_20260801.py --write
```

The replay checks (2\le d\le12), both raw and satellite words, every
addressed internal interval, all three seams, the full width-graded deck in
tagged contexts, the (4g_8) action, exact rank/multiplicity formulas,
internal and clipped residence, the complete support-(le4) circuit census,
the (K_{2,2}) occurrence pairing, and the (6d+15) width bound.

The independent physical owner/palette audit is

```text
scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py
```

and checks the original owner, lower-(q1), upper-(q1), edge and degree
multisets separately.
