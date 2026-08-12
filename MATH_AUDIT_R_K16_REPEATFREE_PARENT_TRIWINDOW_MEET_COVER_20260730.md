# Audit of the six K15 openings and the exact K16 triwindow collar gate

**Date:** 2026-07-30  
**Lane:** R, K15-to-K16 repeat-free lift  
**Status:** proved source-independent reduction; no K16 construction or
global no-go claimed

## 0. Result and scope

Let \(z\) be the new sixteenth coordinate. The triwindow architecture is

\[
 Q_0\;|\;X[6:6436]\;|\;Q_1\;|\;
 \bigl(z\vee Y[7:6432]\bigr)\;|\;Q_2,                 \tag{0.1}
\]

where \(X,Y\) are chosen from the six authenticated optimal K15 words and

\[
 |Q_0|+|Q_1|+|Q_2|=18.                               \tag{0.2}
\]

Indices in the slices are zero-based and the right endpoint is excluded.
This note proves:

1. only seeds 1 and 5 can be the marked parent \(Y\) in a universal
   length-12873 word of form (0.1);
2. either surviving marked parent forces one fixed jump, leaving exactly
   twenty-one middle deliveries and two waste units for the twenty-three
   boundary starts;
3. the exact physical crop holes are boundary-occurrence transversals, not
   the canonical derivative-row deficits;
4. the two bodies saturate, so every at-risk witness meets exactly one free
   window;
5. an exact integral meet-cover criterion characterizes the eighteen-cell
   completion; and
6. a complete cutoff-free occurrence catalogue has at most

\[
17^2\sum_{j=0}^2\binom{|Q_j|+1}{2}
 \le 17^2\binom{19}{2}=49419                         \tag{0.3}
\]

types.

No live DIMACS or implicit search was rerun. A new lightweight profile audit
proves that, for all six authenticated crops, every boundary OR-chain state
is first attained within 22 cells. Consequently the current distance-40
catalogue is complete for all 36 ordered pairs of the six parents, and hence
for all twelve item-1997d-valid pairs \(X\in\{0,\ldots,5\}\),
\(Y\in\{1,5\}\). This finite completeness statement is stronger than mere
soundness but is scoped to these authenticated crops.

## 1. Six-parent derivative census

The inputs are the six words

    scratch/k15_repeatfree_parents_20260730/k15seed_0.word
    ...
    scratch/k15_repeatfree_parents_20260730/k15seed_5.word.

Their optimality and exact middle rows are authenticated in
scratch/k15_batch_parents_20260730.audit.json. For a parent \(P\), put

\[
 R_i(P)=P_i\vee P_{i+1}\vee P_{i+2},\qquad 0\le i\le6435. \tag{1.1}
\]

A direct one-pass replay of (1.1) gives:

| seed | opening | non-rank-seven trace | repeated rank-seven trace |
|---:|:---|:---|:---|
| 0 | (3713,0,33,1,1) | none | 14792 at starts 45,5223 |
| 1 | (5134,0,5,1,0) | rank 6 at start 6390 | none |
| 2 | (3430,1,17,0,1) | rank 8 at start 0 | 2534 at starts 45,1145 |
| 3 | (22,0,41,1,0) | rank 8 at start 0 | 17017 at starts 5290,6390 |
| 4 | (5560,1,2,0,1) | rank 8 at start 6435 | 15554 at starts 45,1145 |
| 5 | (3856,1,14,0,1) | rank 6 at start 45 | none |

The authoritative word hashes, in seed order, are

    018fa0a98239950ddd1a2a7a23c0666d96da91429dec77330524e0317c92f7ef
    93484c945194c628b761f5b9a67111365d00fc1727d7e19839f07b74fee96d49
    ba9e83cced86e0b3d40890c10e30ad59cb703a50529b7830fa83f4fd28f01c49
    38ef44eaceb7c0ff3edcb694bc260ff020824c73d0fa0d23bd1e6fd5ecd135cf
    57a8370c1df54e2f79eb3af269f57b3b9840546cbb6c4862d6cf2adbcd94b2ae
    4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6

The marked crop retains three-cell starts

\[
K_B=\{7,8,\ldots,6429\}.                               \tag{1.2}
\]

All four repeated pairs lie in \(K_B\). Both repeat-free rank-six starts,
6390 and 45, also lie in \(K_B\). The rank-eight exceptional starts of seeds
2--4 lie outside \(K_B\).

Each crop has 6423 canonical three-cell positions and 6422 distinct
rank-seven labels. Thus its canonical \(D^2\) row omits thirteen rank-seven
labels. This is a statement about (1.1), not about all physical intervals in
the crop. A missing canonical label may have an internal witness of another
length.

## 2. Only the marked parent must be repeat-free

### Theorem 2.1

Suppose \(R_i(Y)=R_j(Y)=R\) has rank seven, both starts lie in \(K_B\), and
the two earliest rank-seven endpoints \(e_i,e_j\) defined below are
distinct. Then every word of form (0.1), independently of its eighteen
free-cell values, has two fixed first-middle deliveries of
\(\{z\}\cup R\) at distinct right deadlines. Hence its first-middle
inventory has \(G\ge1\). The convenient sufficient condition
\(|i-j|\ge3\) guarantees \(e_i\ne e_j\).

### Proof

At start \(i\), let \(e_i\le i+2\) be the earliest endpoint at which the old
OR reaches rank seven. It exists because \(R_i(Y)\) has rank seven. Its OR
is a rank-seven subset of \(R_i(Y)\), hence equals \(R\). After adjoining
\(z\), the child interval first reaches middle rank eight at
\(\{z\}\cup R\). The same argument holds at \(j\). By hypothesis
\(e_i\ne e_j\), so the two copies have distinct right deadlines and form a
ghost wholly inside the fixed marked body, which no collar assignment can
erase. Every repeated pair in Table 1 has start separation at least three,
so the hypothesis applies to all four authenticated non-repeat-free crops.
QED.

Item 1997d proves that every universal length-12873 K16 word has \(G=0\).
Theorem 2.1 therefore excludes seeds 0,2,3,4 as \(Y\).

There is no analogous implication for \(X\). Its transported middle row is
\(D^3X\), which is exact and simple for all six parents. A \(D^2X\) repeat is
a lower-shadow issue, not by itself an unmarked middle ghost. This does not
prove that any particular \(X\) compiles; it proves only that item 1997d does
not exclude it.

### Proposition 2.2

For \(Y=1\) or \(5\), the retained rank-six three-cell trace is followed by a
rank-eight four-cell trace because \(D^3Y\) is the exact parent middle row.
In the child, that left endpoint goes from rank at most seven through three
cells to rank nine after four cells. It is a fixed jump. Thus \(J\ge1\).

The unmarked crop has 6427 fixed canonical middle starts. Any earlier
rank-eight prefix at one of those starts must equal its rank-eight
\(D^3X\) value, so the exact simple \(D^3X\) row makes those deliveries
distinct. In the marked crop, every rank-seven prefix through three cells
equals that start's rank-seven \(D^2Y\) value; the repeat-free row therefore
gives 6422 fixed distinct middle deliveries, while the exceptional start is
the one jump just proved. These account for 12850 of 12873 left endpoints.
Consequently the remaining twenty-three boundary starts of any universal
completion must:

* cover all remaining twenty-one canonical middle labels at least once;
* have exactly two surplus boundary outcomes, each a stall, a jump, or a
  same-deadline flat repetition (so a missing label need not have a unique
  boundary occurrence); and
* create no ghost.

This is an exact necessary middle-schedule ledger, not a sufficient full-mask
criterion.

## 3. Physical crop holes are occurrence transversals

For a word \(P\), define

\[
\mathcal C(P)=
\left\{\bigvee_{t=a}^{b}P_t:0\le a\le b<|P|\right\}.    \tag{3.1}
\]

Put

\[
A=X[6:6436],\qquad B_{\rm old}=Y[7:6432].              \tag{3.2}
\]

Thus the second fixed body in the K16 skeleton is
\(z\vee B_{\rm old}\). The exact targets not covered wholly inside the
fixed bodies are

\[
\begin{split}
\mathcal T_{X,Y}={}&
\bigl((2^{[15]}\setminus\{\varnothing\})\setminus\mathcal C(A)\bigr)\\
&\mathbin{\dot\cup}
\left\{\{z\}\cup R:R\subseteq[15],\
R\notin\mathcal C(B_{\rm old})\right\}.                        \tag{3.3}
\end{split}
\]

In particular, \(\{z\}\) belongs to the second family. Formula (3.3), not
the derivative-row deficit thirteen, is the physical at-risk family.

If \(\mathcal W_P(R)\) is the family of all literal intervals of \(P\) with
OR \(R\), then for any boundary crop

\[
R\notin\mathcal C(P[a:|P|-b])
\Longleftrightarrow
\forall[i,j]\in\mathcal W_P(R),\quad
i<a\ \hbox{or}\ j\ge |P|-b.                            \tag{3.4}
\]

Thus the six openings affect physical holes only through the two
boundary-transversal profiles \(H_{6,2}(X)\), \(H_{7,6}(Y)\) and their
boundary OR chains.

## 4. Body saturation separates the three windows

### Proposition 4.1

For every parent choice,

\[
\bigvee A=[15],\qquad \bigvee B_{\rm old}=[15].        \tag{4.1}
\]

### Proof

The crop \(A\) contains the 6427 \(D^3X\) windows starting at 6 through
6432. They are distinct rank-eight sets. If their union omitted a
coordinate, there could be at most \(\binom{14}{8}=3003\) such sets.

The old crop \(B_{\rm old}\) contains 6422 distinct retained rank-seven
three-cell labels.
If their union omitted a coordinate, there could be at most
\(\binom{14}{7}=3432\). Both contradictions prove (4.1). QED.

An interval meeting \(Q_0\) and \(Q_1\) contains all of \(A\). Its fixed old
OR is \([15]\), so it realizes only \([15]\) or \([16]\), both already
covered internally. An interval meeting \(Q_1\) and \(Q_2\) contains the
marked body and has OR \([16]\). Therefore every witness for a target in
\(\mathcal T_{X,Y}\) meets exactly one free window.

## 5. Exact integral meet-cover theorem

Let \(V=Q_0\cup Q_1\cup Q_2\). For an interval \(I\) meeting one free
window, define

\[
Q(I)=I\cap V,\qquad
F(I)=\bigvee_{p\in I\setminus V}W_p^*,                 \tag{5.1}
\]

where \(W^*\) is the fixed skeleton. For \(T\in\mathcal T_{X,Y}\), let

\[
\mathcal O(T)=
\{(F(I),Q(I)):Q(I)\ne\varnothing,\ F(I)\subseteq T\}.  \tag{5.2}
\]

### Theorem 5.1

There is an assignment of nonempty K16 masks \(C_v\) to all \(v\in V\)
which makes (0.1) universal if and only if one can choose
\((F_T,Q_T)\in\mathcal O(T)\) for every \(T\in\mathcal T_{X,Y}\) such that,
with

\[
U_v=\bigcap_{T:v\in Q_T}T                              \tag{5.3}
\]

and the empty intersection interpreted as \([16]\),

\[
U_v\ne\varnothing\quad(v\in V),                       \tag{5.4}
\]

and

\[
T\setminus F_T\subseteq\bigcup_{v\in Q_T}U_v
\quad(T\in\mathcal T_{X,Y}).                           \tag{5.5}
\]

When these conditions hold, \(C_v=U_v\) is a literal completion.

### Proof

Given a completion, choose one realizing interval for every at-risk target.
If \(v\in Q_T\), its cell \(C_v\) has no bit outside \(T\), so
\(C_v\subseteq U_v\). Nonzero cells imply (5.4), and every bit of
\(T\setminus F_T\) lies in some such \(C_v\), proving (5.5).

Conversely set \(C_v=U_v\). Condition (5.4) makes every cell nonzero. On the
chosen interval for \(T\), every free cell is a subset of \(T\), while
(5.5) supplies every bit not already in \(F_T\). Its literal OR is exactly
\(T\). The fixed bodies cover all remaining targets. QED.

For each coordinate \(b\), define the forbidden collar set

\[
D_b=\bigcup_{T:b\notin T}Q_T.                           \tag{5.6}
\]

Then \(b\in U_v\) iff \(v\notin D_b\). The criterion is equivalently

\[
\forall v\ \exists b:\ v\notin D_b,                   \tag{5.7}
\]

\[
\forall T\ \forall b\in T\setminus F_T:\quad
Q_T\not\subseteq D_b.                                  \tag{5.8}
\]

Every \(Q_T\) is an interval in one of three short windows, so (5.7)--(5.8)
is an exact sixteen-colour interval non-cover system.

It is not an ordinary Hall matching. A minimal abstract residual-support
failure takes

\[
T_1=\{a,b\},\ F_1=\varnothing,\ Q_1=\{u,v\},\qquad
T_2=\{a\},\ F_2=\{a\},\ Q_2=\{u,v\}.                   \tag{5.9}
\]

Both occurrence options are individually feasible, but
\(U_u=U_v=\{a\}\), so \(T_1\)'s required bit \(b\) has no host. Incidence
cardinality alone cannot replace (5.4)--(5.5).

## 6. Cutoff-free catalogue and finite maxext-40 completeness

For a free window of length \(n\), the active set \(Q(I)\) is one of
\(\binom{n+1}{2}\) nonempty subintervals. A left fixed extension contributes
one suffix-OR-chain state and a right extension one prefix-OR-chain state.
Each chain starts at zero and changes at most sixteen times, hence has at
most seventeen states. This proves the bound

\[
17^2\binom{n+1}{2}                                     \tag{6.1}
\]

per window and (0.3) in total.

An exact builder should keep one literal endpoint representative for every
distinct adjacent prefix/suffix OR-chain state and combine these with every
free subinterval, allowing a nonzero left state only when the free
subinterval touches the window's left end and a nonzero right state only
when it touches the right end. This includes a state whose first physical
appearance is far from the window.

The current builders

    scratch/build_k16_triwindow_dimacs_20260730.py
    scratch/trisolve2p_dimacs_20260730.py
    scratch/search_k16_triwindow_implicit_csp_20260730.cpp

use a physical extension cutoff of 40. For arbitrary source words this would
require a separate completeness theorem: a farther fixed-OR state need not
be dominated by a nearer state. For the six authenticated parents, however,
the required theorem is now certified directly.

### Proposition 6.1 (all-six boundary profile)

Each of the four relevant old-coordinate chains

* prefix of \(A=X[6:6436]\);
* suffix of \(A\);
* prefix of \(B_{\rm old}=Y[7:6432]\); and
* suffix of \(B_{\rm old}\)

has exactly eleven nonzero distinct states. Their maximum first-attainment
distances are:

| seed | A prefix | A suffix | B-old prefix | B-old suffix |
|---:|---:|---:|---:|---:|
| 0 | 13 | 22 | 12 | 18 |
| 1 | 20 | 12 | 19 | 11 |
| 2 | 11 | 19 | 13 | 20 |
| 3 | 20 | 12 | 19 | 11 |
| 4 | 11 | 19 | 13 | 20 |
| 5 | 11 | 19 | 13 | 20 |

Thus every state has a literal representative at distance at most 22 from
its window.

### Corollary 6.2 (maxext 40 is complete on the six-parent atlas)

For every ordered pair \(X,Y\) of the six authenticated parents and every
partition \(|Q_0|+|Q_1|+|Q_2|=18\), the occurrence types emitted with
maxext 40 are exactly all occurrence types relevant to
\(\mathcal T_{X,Y}\).

### Proof

By Proposition 4.1, an at-risk witness cannot cross either complete fixed
body, so it meets one free window. Its free intersection \(Q(I)\) is a
contiguous subinterval. A nonzero left fixed extension is possible only when
that subinterval touches the window's left end, and its contribution is a
suffix-chain state of the adjacent body. Proposition 6.1 supplies a
same-state representative within 22 cells. The right side is identical with
a prefix chain. Replacing either extension by its first-attainment
representative preserves both \(F(I)\) and \(Q(I)\), hence preserves the
complete Boolean occurrence type. Since \(22<40\), the builder emits that
type. Conversely every emitted type has a literal representative, so no
spurious type is introduced. QED.

This also explains why omitted intervals crossing a whole body do not create
a gap: their fixed contribution is already \([15]\) or \([16]\), and the
only masks they can realize are in the fixed-body coverage.

## 7. Exact finite physical crop-hole profile

The same lightweight replay enumerated all interval ORs internal to each
crop. The exact nonempty old-mask hole counts are:

| seed | holes in A crop | holes in B-old crop | marked holes including singleton z |
|---:|---:|---:|---:|
| 0 | 27 | 47 | 48 |
| 1 | 26 | 46 | 47 |
| 2 | 27 | 47 | 48 |
| 3 | 26 | 43 | 44 |
| 4 | 25 | 43 | 44 |
| 5 | 26 | 43 | 44 |

These are physical crop holes in the sense of (3.3), not canonical
derivative-row deficits. Therefore the total at-risk counts for the twelve
item-1997d-valid ordered pairs are:

| X seed | Y=1 | Y=5 |
|---:|---:|---:|
| 0 | 74 | 71 |
| 1 | 73 | 70 |
| 2 | 74 | 71 |
| 3 | 73 | 70 |
| 4 | 72 | 69 |
| 5 | 73 | 70 |

The best fixed-body count is thus 69 for \((X,Y)=(4,5)\). This is only a
target count; it does not imply meet-cover feasibility.

The complete hole masks, rank histograms, chain states and first-attainment
distances are frozen in

    scratch/audit_k16_six_parent_triwindow_profiles_20260730.py
    SHA-256 7f24fb58a6d37dcdd773b6777d064de847aa0935ac67f49d02fa9f5415d702cb

    scratch/k16_six_parent_triwindow_profiles_20260730.audit.json
    SHA-256 b4e7b3835b842fb4ab582636dce7183d56c47b2f3aba046599b71a3cbf17d0c2
    payload f455079980b38f62a717ee5580b258801c6c614dc118badb8b58bf6ff208f88c

This audit scans internal intervals only until the full old mask is reached;
monotonicity makes the early stop exact. It is a replay/census, not a search.

## 8. Exact remaining gate

For this architecture the source-independent equality problem is:

1. choose any authenticated \(X\) and \(Y\in\{1,5\}\);
2. use the certified complete maxext-40 catalogue, equivalently the
   cutoff-free option families (5.2);
3. satisfy the integral interval non-cover equations (5.7)--(5.8); and
4. replay all 65535 nonempty K16 masks.

The twenty-three-start ledger is a useful first projection. A matching of
the twenty-one missing canonical labels to twenty-three boundary starts,
with two waste slots, is necessary. It is not sufficient because all chosen
occurrences must share the same eighteen physical cells through Theorem 5.1.

This note does not decide that integral gate and does not change

\[
12873\le\nu(16)\le12874.
\]
