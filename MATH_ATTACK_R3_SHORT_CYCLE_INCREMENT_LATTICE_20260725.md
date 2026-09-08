# Short exact odd-graph trades and the balanced first-shadow lattice

## Purpose and scope

Put

\[
n=2m+1,\qquad O_m=KG(n,m),\qquad m\ge 3.
\]

This report studies a single simple alternating \(C_8,C_{10}\), or
\(C_{12}\) between exact \(C_n\)-factors of \(O_m\), computes its first
several shadow increments exactly, and then asks what the resulting signed
increment vectors generate.

All trades here are integral.  No fractional factor, averaged switch, or
formal real tangent direction is used.  There are, however, three different
scopes which must not be conflated.

1. A **single-factor trade** is an alternating cycle in one specified exact
   factor whose toggle is again an exact factor.
2. The **MSW orbit library** consists of coordinate relabelings of one
   explicit MSW local trade.  Every member is an exact factor-to-factor
   \(C_8\), but different members need not be simultaneously present in one
   factor.
3. The **initial PBBS candidate library** is a family of alternating cycles
   in the canonical PBBS 2-factor.  That 2-factor can have long components;
   the PBBS counts alone do not certify exact-wreath preservation.

The decisive positive result is at scope 2.  The decisive negative results
are at scopes 1 and 3.

No web search, finite enumeration, or certificate data is used in the
proofs below.

The only previously proved construction-specific inputs not reproved here
are: the MSW exact factor and its four-letter component
(`MSW_TRANSPOSITION_COMPONENTS.md`), the complete fixed
\((2\ 3)\)-component classification
(`MSW_COMPONENT_HIERARCHY_REDUCTION.md`), its colex-pivot theorem
(`MSW_COLEX_PIVOT.md`), the shifted-atlas first-shadow independence theorem
(`MSW_MULTIRANK_LOCAL_TRADES.md`), and the PBBS six-label
head/local-coordinate lemma
(`MATH_ATTACK_R_PBBS_REBUNDLING_REPORT_RAW_20260724.md`, with its audit).
Every new implication from those inputs is proved below.  No other lemma is
being assumed silently.

## 1. Main conclusions

Let \(B_rF\) be the histogram of cyclic rank-\(r\) intervals over the
wreaths of an exact factor \(F\), and put

\[
\Delta_h(Z)=B_{m-h}(F\triangle Z)-B_{m-h}(F),
\qquad 1\le h\le m-1.
\]

The exact conclusions are as follows.

### Theorem A — short-trade topology

Let \(Z\) be a nontrivial simple \(F\)-alternating \(C_{2k}\), where
\(k\in\{4,5,6\}\), and assume both \(F\) and \(F\triangle Z\) are exact
\(C_n\)-factors.  Then the old and new cut-count profiles are:

\[
\begin{array}{c|c|c}
Z&\text{number of old/new wreaths}&\text{old and new cut counts}\\ \hline
C_8&2&(2,2)\\
C_{10}&2&(2,3)\\
C_{12}&2&(2,4)\text{ or }(3,3),\quad\text{independently on the two sides},\\
      &3&(2,2,2)\text{ on both sides}.
\end{array}
\tag{1.1}
\]

A four-cut wreath requires \(m\ge4\).  These are cut-count partitions, not
residual-path lengths.  The residual incidence multigraphs, their exact
length equations, and their centered balance equations are classified in
Section 2.

Every exact \(C_8\) is much more rigid: its four residual paths have vertex
orders

\[
\boxed{3,n-3,3,n-3.}
\tag{1.2}
\]

### Theorem B — exact first-three-shadow normal form

Let the \(k\) common residual paths have vertex orders \(L_1,\ldots,L_k\).
For \(h=1,2,3\), subject to \(h\le m-1\), define

\[
b_h=\sum_{i=1}^k\min(L_i,2h).
\tag{1.3}
\]

Then \(\Delta_h\) is exactly the new boundary deck minus the old boundary
deck of the residual paths.  Each sign has exactly \(b_h\) raw occurrences,
and consequently

\[
\|\Delta_h^+\|_1=\|\Delta_h^-\|_1\le b_h,
\qquad
\|\Delta_h\|_1,\ |\operatorname{supp}\Delta_h|\le2b_h.
\tag{1.4}
\]

In particular the universal ceilings at depths one, two, and three are

\[
\begin{array}{c|ccc}
Z&\|\Delta_1\|_1&\|\Delta_2\|_1&\|\Delta_3\|_1\\ \hline
C_8&16&32&48\\
C_{10}&20&40&60\\
C_{12}&24&48&72.
\end{array}
\tag{1.5}
\]

These are support/\(\ell_1\) ceilings; cancellations can make the actual
norm smaller.  For an exact \(C_8\), (1.2) sharpens the raw one-sign mass to

\[
b_1=8,\qquad b_h=4h+6\quad(2\le h\le m-1).
\tag{1.6}
\]

### Theorem C — exact MSW \(C_8\) rectangle generation

Put \(r=m-1\), let \(U_r\) be the point-versus-\(r\)-set incidence matrix,
and define the balanced deficit lattice

\[
\mathcal L_r=\ker_{\mathbb Z}U_r.
\tag{1.7}
\]

The coordinate-relabeling orbit of one explicit MSW four-letter
factor-to-factor \(C_8\) has as its first-shadow increments exactly all
elementary rectangles

\[
R_K(a,a';b,b')=
e_{K\cup\{a,b\}}-e_{K\cup\{a,b'\}}
-e_{K\cup\{a',b\}}+e_{K\cup\{a',b'\}},
\tag{1.8}
\]

where \(|K|=m-3\) and the four displayed labels are distinct and avoid
\(K\).  These rectangles generate \(\mathcal L_r\) integrally:

\[
\boxed{
\left\langle B_{m-1}z:z\text{ is an MSW-orbit exact }C_8\right\rangle_{\mathbb Z}
=\mathcal L_{m-1}.}
\tag{1.9}
\]

This is an ambient library theorem.  It does not say that all generators
are simultaneously available in one exact factor.

### Theorem D — a bounded-congestion regime

Fix \(K\in\binom{[n]}{m-3}\), partition \([n]\setminus K=A\mathbin{\dot\cup}B\),
and let

\[
d=\sum_{a\in A,b\in B}d_{ab}e_{K\cup\{a,b\}}\in\mathcal L_{m-1}.
\tag{1.10}
\]

Equivalently, every row and column sum of \((d_{ab})\) is zero.  Put

\[
M=\frac{\|d\|_1}{2},\qquad
\Delta=\max\left\{
\max_a\sum_b|d_{ab}|,
\max_b\sum_a|d_{ab}|
\right\}.
\tag{1.11}
\]

Then \(d\) is a sum of at most \(M\) exact MSW-orbit \(C_8\) increments.
Moreover the decomposition may be chosen so that the number \(c_{ab}\) of
rectangle occurrences whose four-cell support contains \((a,b)\) obeys

\[
\boxed{
c_{ab}\le2\min(p_a,p_b)-|d_{ab}|
\le\Delta-|d_{ab}|\le\Delta,}
\tag{1.12}
\]

where

\[
p_a=\frac12\sum_b|d_{ab}|,\qquad
p_b=\frac12\sum_a|d_{ab}|.
\]

This is bounded first-shadow cell congestion.  It is not a simultaneous
switching theorem and does not bound congestion of the middle-wreath
supports.

### Theorem E — fixed-factor invariant obstructions

No exact common-core \(C_8,C_{10}\), or \(C_{12}\) is first-shadow neutral.
Every \(C_8\) is common-core, hence

\[
\boxed{\Delta_1(Z)\ne0\quad\text{for every exact single }C_8.}
\tag{1.13}
\]

The complete simultaneously switchable \((2\ 3)\)-interaction cube of the
fixed MSW factor has linearly independent first-shadow increments, even over
every field.  Thus it contains no nonempty first-shadow-neutral component
selection and no nonzero signed integer combination invisible at depth one.

For the initial PBBS factor, the common-core candidate counts per core are
at most

\[
12,\quad19,\quad32
\tag{1.14}
\]

for \(C_8,C_{10},C_{12}\), respectively, with factor-edge congestion
\(8m,16m,32m\).  At any fixed PBBS core supporting a short cycle, so that
\(|S_K|\ge4\), their centered-color increment vectors lie in a proper sectorwise-balanced
sublattice of exact codimension \(|S_K|-1\).  These are
candidate and lattice obstructions, not an exact-wreath existence theorem
for the PBBS factor.

## 2. Exact topology and centered residual balance

Write the alternating cycle as

\[
Z=x_0y_0x_1y_1\cdots x_{k-1}y_{k-1}x_0,
\tag{2.1}
\]

where \(x_iy_i\) is an old factor edge and \(y_ix_{i+1}\) is a new factor
edge.  Deleting the \(k\) old seams from the touched old wreaths leaves
\(k\) common residual paths \(P_1,\ldots,P_k\).

Let \(H\) be the bipartite multigraph whose left vertices are touched old
wreaths, whose right vertices are touched new wreaths, and whose edge
corresponding to \(P_i\) joins the two wreaths containing that path.

### Lemma 2.1 — connectedness, equal sides, and no degree one

The graph \(H\) is connected.  It has the same number \(r\) of vertices on
each side, every vertex has degree at least two, and \(r\ge2\).  Therefore

\[
2r\le k.
\tag{2.2}
\]

#### Proof

If \(H\) were disconnected, its residual paths would split into two
nonempty classes invariant under both the old and new seam pairings.  The
symmetric difference of the two factors would then have at least two
components, contrary to the assumption that it is the single cycle \(Z\).

The old touched set has \(rn\) vertices.  If there are \(s\) touched new
wreaths, the same set has \(sn\) vertices, so \(r=s\).

If an old wreath had only one cut, its only residual path would contain all
\(n\) vertices of that wreath.  The exact new wreath containing that path
already has \(n\) vertices and so can contain no other positive residual
path.  It too would have degree one.  Both cycles would then close the same
path.  Because a wreath support induces its unique \(C_n\), the new closing
edge would be the removed old edge, contradicting the disjointness of old
and new seams.  The same argument with the factors reversed excludes a
degree-one new wreath.

If \(r=1\), the old and new wreaths have the same vertex support; inducedness
again forces them to be the same cycle, making the trade trivial.  Finally,
the sum of the degrees on either side is \(k\), so minimum degree two gives
\(2r\le k\).  ∎

The profiles in (1.1) now follow immediately for \(k=4,5,6\).  To obtain
the finer residual equations, give each path its vertex-order \(L_i\).  The
removed factor edges are pairwise vertex-disjoint, so

\[
L_i\ge2.
\tag{2.3}
\]

Every row and every column of \(H\) has total path weight \(n\).

For a residual path \(P\), define its centered incidence vector

\[
\zeta(P)=n\sum_{X\in V(P)}\mathbf1_X-m|V(P)|\mathbf1
\in\mathbb Z^{[n]}.
\tag{2.4}
\]

The paths in one old wreath sum to zero.  For a complete proposed
rebundling into \(r\) nonempty new components, all new components are exact
wreaths if and only if the \(\zeta\)-vectors incident with every new
component sum to zero.

Indeed, if one proposed component has length \(L\) and zero centered vector,
then every coordinate occurs \(mL/n\) times.  Since \(\gcd(m,n)=1\), one has
\(n\mid L\).  If all \(r\) positive new components have zero centered
vector and total length \(rn\), every one must have length \(n\).  Every
length-\(n\) odd-graph cycle is a wreath.  The converse is immediate from
point regularity.  For one component in isolation, \(\zeta=0\) only forces
its length to be a positive multiple of \(n\); the collective hypothesis is
essential.

There is also an omitted-label form.  If \(t_x\) counts retained path edges
omitting \(x\), and \(a_x\) counts new seams omitting \(x\), then for a
component of length \(L\)

\[
2\zeta_x=L-n(t_x+a_x).
\tag{2.5}
\]

At \(L=n\), exactness is therefore equivalent to

\[
t_x+a_x=1\qquad\text{for every }x\in[n].
\tag{2.6}
\]

### Theorem 2.2 — complete residual-incidence tables

Up to row/column permutations and reversing the cycle, the possibilities
are the following.  A braced cell contains several parallel residual paths.

#### (i) \(C_8\)

\[
H=\begin{pmatrix}P_1&P_2\\P_4&P_3\end{pmatrix},
\tag{2.7}
\]

and, for some \(a\),

\[
(L_1,L_2,L_3,L_4)=(a,n-a,a,n-a),
\qquad 2\le a\le n-2,
\tag{2.8}
\]

\[
(\zeta_1,\zeta_2,\zeta_3,\zeta_4)=(z,-z,z,-z).
\tag{2.9}
\]

Odd-graph geometry strengthens (2.8) to \(a=3\), up to replacing \(a\) by
\(n-a\); see Theorem 2.3.

#### (ii) \(C_{10}\)

\[
H=\begin{pmatrix}P_1&P_2\\P_3&\{P_4,P_5\}\end{pmatrix}.
\tag{2.10}
\]

For some \(a\),

\[
L_2=L_3=a,\qquad L_1=n-a,\qquad L_4+L_5=n-a,
\qquad 2\le a\le n-4,
\tag{2.11}
\]

and

\[
\zeta_2=\zeta_3=-\zeta_1,
\qquad \zeta_4+\zeta_5=\zeta_1.
\tag{2.12}
\]

The only other connected integer cell pattern with degree margins
\((2,3)\) would put the two degree-two path sets in disjoint cells.  Each of
those cells would already have total path weight \(n\), leaving positive
weight beyond the available total \(2n\).  Thus (2.10) is forced.

#### (iii) \(C_{12}\) on two old and two new wreaths

For old/new profiles \(42/42\),

\[
H=\begin{pmatrix}P_1&P_2\\P_3&\{P_4,P_5,P_6\}\end{pmatrix},
\tag{2.13}
\]

\[
L_2=L_3=a,\quad L_1=n-a,\quad L_4+L_5+L_6=n-a,
\quad2\le a\le n-6,
\tag{2.14}
\]

\[
\zeta_2=\zeta_3=-\zeta_1,
\qquad \zeta_4+\zeta_5+\zeta_6=\zeta_1.
\tag{2.15}
\]

For old/new profiles \(42/33\),

\[
H=\begin{pmatrix}P_1&P_2\\\{P_3,P_4\}&\{P_5,P_6\}\end{pmatrix},
\tag{2.16}
\]

\[
L_2=L_3+L_4=a,\quad L_1=n-a,\quad L_5+L_6=n-a,
\quad4\le a\le n-4,
\tag{2.17}
\]

\[
\zeta_2=-\zeta_1,\qquad
\zeta_3+\zeta_4=-\zeta_1,\qquad
\zeta_5+\zeta_6=\zeta_1.
\tag{2.18}
\]

For old/new profiles \(33/33\),

\[
H=\begin{pmatrix}P_1&\{P_2,P_3\}\\\{P_4,P_5\}&P_6\end{pmatrix},
\tag{2.19}
\]

\[
L_1=L_6=a,\qquad
L_2+L_3=L_4+L_5=n-a,
\qquad2\le a\le n-4,
\tag{2.20}
\]

\[
\zeta_6=\zeta_1,\qquad
\zeta_2+\zeta_3=\zeta_4+\zeta_5=-\zeta_1.
\tag{2.21}
\]

The transpose of (2.16) covers \(33/42\).  The excluded alternative cell
matrices either disconnect \(H\) or force one row/column of positive paths
to have weight \(n\) while leaving an additional positive path after the
total \(2n\) has already been exhausted.

#### (iv) \(C_{12}\) on three old and three new wreaths

Here \(H\) is a six-cycle.  Ordering its edges cyclically gives

\[
(L_1,\ldots,L_6)=(a,n-a,a,n-a,a,n-a),
\qquad2\le a\le n-2,
\tag{2.22}
\]

and

\[
(\zeta_1,\ldots,\zeta_6)=(z,-z,z,-z,z,-z).
\tag{2.23}
\]

The equations in (2.9), (2.12), (2.15), (2.18), (2.21), and (2.23) are
necessary and sufficient for the proposed new components to be exact once
the displayed residual paths and seam edges actually exist in \(O_m\).
They do not assert geometric existence of every abstract vector solution.

### Theorem 2.3 — universal exact \(C_8\) path profile

Every exact factor-to-factor alternating \(C_8\) has path profile

\[
3,n-3,3,n-3.
\tag{2.24}
\]

#### Proof

The two old and two new wreaths have cut profile \(2+2\).  Any new seam
whose endpoints lay in one old wreath support would be a chord of that
induced wreath, hence would be an old cycle edge.  Thus every new seam joins
the two old supports.

Let \(YY'\) be one removed edge in the second old wreath and let \(X,X'\)
be its two new-seam neighbors in the first.  The disjoint sets \(Y,Y'\)
omit one label \(p\).  Since the old wreath supports are disjoint,

\[
X=(Y'\setminus\{y'\})\cup\{p\},\qquad
X'=(Y\setminus\{y\})\cup\{p\}
\tag{2.25}
\]

for suitable \(y'\in Y'\), \(y\in Y\).  Hence \(X\cap X'=\{p\}\).
In a wreath cycle, two vertices at factor-cycle separation \(2s\) meet in
\(m-s\) points, while two at separation \(2s+1\) meet in \(s\) points.
Thus \(X,X'\) have cyclic distance three.

Index the two removed edges in the first wreath as

\[
C_0C_1,\qquad C_aC_{a+1},\qquad2\le a\le m,
\]

using the shorter cut separation.  The parallel pairing of seam preimages
is one of only two possibilities: the four new seams biject the four
cut endpoints in one old support with those in the other, and the two
preimages of either removed edge cannot be the adjacent endpoints of one
cut because they must have distance three.  Thus each pair uses one endpoint
from each cut.  The parallel pairing means that the two removed edges in
the second wreath pair the first-wreath endpoints as

\[
\{C_0,C_a\},\qquad\{C_1,C_{a+1}\}.
\]

Each pair must have cyclic distance three by (2.25).  Since
\(2\le a\le m\), both displayed distances are \(a\), so \(a=3\).

The only other perfect matching between the two cut-endpoint pairs is the
crossed pairing

\[
\{C_0,C_{a+1}\},\qquad\{C_1,C_a\}.
\]

Its two cyclic distances are
\(\min(a+1,n-a-1)\) and \(a-1\), respectively.  Distance three would
therefore force simultaneously

\[
a-1=3,\qquad \min(a+1,n-a-1)=3.
\]

The first equation gives \(a=4\), while the second becomes
\(\min(5,n-5)=3\), impossible for odd \(n\ge7\).  Therefore the two path
orders are \(3,n-3\) in each old wreath.  Reversing the trade gives the same
new-wreath profile.  ∎

The residual incidence graph is \(K_{2,2}\).  Give each inherited path the
sign recording whether chosen old and new wreath orientations traverse it
in the same direction.  The product of the four signs is negative;
otherwise the changed seams split into two alternating \(C_4\)'s, which do
not exist in an odd graph.  Reversing a wreath orientation switches its two
incident signs, so the orientations may be normalized so that exactly one
path is reversed, and that path may be chosen to be one of the two short
three-vertex paths.  This is an orientation normalization, not an additional
existence assertion.

## 3. Exact first, second, and third shadow increments

### 3.1 A vertex-local first-shadow formula

At a changed middle vertex \(v\), let

- \(a_v\) be the omitted label on its removed factor edge;
- \(b_v\) be the omitted label on its added edge; and
- \(r_v\) be the omitted label on its retained factor edge.

These three labels are distinct.  The neighbor of \(v\) across an edge
omitting \(c\) is \(v^c\setminus\{c\}\).  Put

\[
K_v=v^c\setminus\{a_v,b_v,r_v\},\qquad |K_v|=m-2.
\tag{3.1}
\]

The old centered first-shadow color at \(v\) is
\(K_v\cup\{b_v\}\), and the new color is
\(K_v\cup\{a_v\}\).  Therefore every alternating \(C_{2k}\) has the exact
increment

\[
\boxed{
\Delta_1(Z)=
\sum_{v\in V(Z)}
\left(e_{K_v\cup\{a_v\}}-e_{K_v\cup\{b_v\}}\right).}
\tag{3.2}
\]

Thus \(\Delta_1\) is canonically a sum of \(2k\) directed Johnson edges.
Its raw positive and negative masses are both \(2k\), so

\[
\|\Delta_1\|_1,\ |\operatorname{supp}\Delta_1|\le4k.
\tag{3.3}
\]

It also lies in \(\ker_{\mathbb Z}U_{m-1}\).  One direct proof is worth
recording.  If a fixed coordinate \(c\) is the omitted label of two
successive edges of a simple odd-graph cycle, their cyclic edge-index gap is
odd and at least three.  Indeed, after an edge omitting \(c\), membership of
\(c\) alternates at every edge not omitting \(c\); the next \(c\)-omitting
edge can occur only when two consecutive endpoints again omit \(c\).
Successive occurrences therefore alternate edge parity.  Hence every label
appears equally often among the old and new seams of an even cycle.  Applying
\(U_{m-1}\) to (3.2) gives the old-seam label count minus the new-seam label
count, which is zero.

For the indexing in (2.1), put

\[
A_i=x_i,\qquad C_i=y_i,\qquad
K_i=A_i\cap A_{i+1},
\]

\[
a_i=A_i\setminus A_{i+1},\qquad
b_i=A_{i+1}\setminus A_i.
\tag{3.4}
\]

Then \(C_i=[n]\setminus(A_i\cup A_{i+1})\).  If \(r_i\) and \(s_i\) are
the retained-edge omitted labels at \(A_i\) and \(C_i\), respectively, then
(3.2) becomes

\[
\begin{aligned}
\Delta_1={}&\sum_i\Bigl[
e_{A_i^c\setminus\{r_i,a_{i-1}\}}
-e_{A_i^c\setminus\{r_i,b_i\}}\\
&\hspace{27mm}+
e_{C_i^c\setminus\{s_i,a_i\}}
-e_{C_i^c\setminus\{s_i,b_i\}}
\Bigr].
\end{aligned}
\tag{3.5}
\]

Formula (3.5) is the exact first-shadow classifier once the parity Johnson
walk and retained labels are specified.

### 3.2 The exact boundary-deck formula at every shallow depth

Orient an old wreath in factor-cycle order as

\[
v_0,v_1,\ldots,v_{n-1}.
\]

For \(1\le h\le m-1\), define its stride-two occurrence

\[
D_h(i)=v_i\cap v_{i+2}\cap\cdots\cap v_{i+2h}.
\tag{3.6}
\]

The omitted-edge word shows that \(D_h(i)\) is an \((m-h)\)-set and that
the multiset of all \(D_h(i)\) is exactly the rank-\((m-h)\) shadow of the
wreath.

For an oriented residual path

\[
P=(p_0,\ldots,p_{L-1}),
\]

put

\[
J_h(P)=
\sum_{j=0}^{L-1-2h}
e_{p_j\cap p_{j+2}\cap\cdots\cap p_{j+2h}},
\tag{3.7}
\]

with the sum empty when \(L\le2h\).  Reversing \(P\) merely reverses the
summation order, so \(J_h(P)\) is orientation-invariant.  Every stride-two
block wholly inside a residual path therefore cancels between the old and
new factors.  Only blocks whose spanning \(2h\)-edge arc crosses a seam can
contribute.

For a sewing \(\mathscr S\) of the oriented paths into cycles, let
\(\mathcal B_h(\mathscr S)\) be the sum of the corresponding occurrences
whose spanning arcs cross at least one seam.  Then

\[
\boxed{
\Delta_h=
\mathcal B_h(\mathscr S_{\rm new})
-\mathcal B_h(\mathscr S_{\rm old}).}
\tag{3.8}
\]

This is an identity of integral histograms, not an estimate.

On a cycle partitioned into paths of orders \(L_i\), the number of internal
starts in path \(i\) is \(\max(L_i-2h,0)\).  Subtracting from the total and
summing over all components shows that each boundary deck in (3.8) contains
exactly

\[
b_h=\sum_i\left[L_i-\max(L_i-2h,0)\right]
=\sum_i\min(L_i,2h)
\tag{3.9}
\]

raw occurrences.  Equations (1.3)--(1.6) follow.  If

\[
\nu_j=|\{i:L_i=j\}|,
\]

then the first three raw one-sign counts are

\[
b_1=2k,
\tag{3.10}
\]

\[
b_2=4k-2\nu_2-\nu_3,
\tag{3.11}
\]

\[
b_3=6k-4\nu_2-3\nu_3-2\nu_4-\nu_5.
\tag{3.12}
\]

The last line is in the stated shadow range only for \(m\ge4\).  At the
terminal rank-one shadow \(h=m-1\), the actual increment is always zero,
because every wreath contains every singleton exactly once.  The boundary
count can still be positive; \(b_h\) is a raw occurrence count, not an
asserted histogram distance.

Explicitly, the depth-two boundary cells are

\[
v_i\cap v_{i+2}\cap v_{i+4},
\tag{3.13}
\]

and the depth-three cells are

\[
v_i\cap v_{i+2}\cap v_{i+4}\cap v_{i+6}.
\tag{3.14}
\]

Thus (3.8), together with the residual-incidence tables in Section 2, is a
complete parameterization of the first three signed increment vectors of
every actual exact \(C_8,C_{10},C_{12}\).  It does not replace the geometric
problem of deciding which abstract residual paths and seams exist.

## 4. Johnson active-set classification and neutrality obstructions

The topology of Section 2 does not yet use the small value of \(k\) inside
the Johnson parity walk.  That extra structure sharply restricts
first-shadow neutrality.

Let

\[
K=\bigcap_iA_i,\qquad A_i=K\cup S_i,\qquad
Q=\bigcup_iS_i,
\]

and put

\[
t=|S_i|,\qquad q=|Q|.
\tag{4.1}
\]

Every transition replaces one active label:

\[
S_{i+1}=S_i\setminus\{a_i\}\cup\{b_i\}.
\tag{4.2}
\]

Let

\[
Y=[n]\setminus(K\cup Q).
\]

Then

\[
C_i=Y\cup\left(Q\setminus(S_i\cup S_{i+1})\right),
\tag{4.3}
\]

and the active part on the \(C\)-parity has size

\[
t'=q-t-1.
\tag{4.4}
\]

Every active label has a \(1\to0\) transition in the cyclic membership word
of the \(S_i\)'s.  Since there are only \(k\) exits,

\[
q\le k.
\tag{4.5}
\]

After swapping the two parity classes, assume \(t\le t'\).  Equations
(4.4)--(4.5) give the exhaustive small-cycle alternatives:

\[
\begin{array}{c|c}
k&\text{active-set normal form}\\ \hline
4&t=1;\\
5&t=1,\text{ or }q=5,t=t'=2;\\
6&t=1,\text{ or }t=2\text{ and }q\in\{5,6\},
\text{ with }t'=2\text{ or }3.
\end{array}
\tag{4.6}
\]

The case \(t=1\) is the common-core normal form

\[
A_i=K\cup\{u_i\},\qquad
C_i=B\setminus\{u_i,u_{i+1}\},\qquad B=[n]\setminus K.
\tag{4.7}
\]

Every \(C_8\) is therefore common-core.  A \(C_{10}\) or \(C_{12}\) need
not be.

### Theorem 4.1 — common-core sector obstruction

Assume (4.7) and that both endpoint factors are exact, and let \(r_i,s_i\)
be the retained-edge omitted labels at
\(A_i,C_i\).  Then

\[
r_i\in B\setminus\{u_{i-1},u_i,u_{i+1}\},
\qquad s_i\in K,
\tag{4.8}
\]

and the first-shadow increment splits into disjoint sectors

\[
\Delta_1=\Delta_A+\Delta_C,
\tag{4.9}
\]

\[
\Delta_A=
\sum_i\left(
e_{B\setminus\{u_{i-1},u_i,r_i\}}
-e_{B\setminus\{u_i,u_{i+1},r_i\}}
\right),
\tag{4.10}
\]

\[
\Delta_C=
\sum_i\left(
e_{(K\setminus\{s_i\})\cup\{u_{i+1}\}}
-e_{(K\setminus\{s_i\})\cup\{u_i\}}
\right).
\tag{4.11}
\]

Both sectors are separately point-balanced.  Moreover

\[
\Delta_C=
\sum_j\left(
e_{(K\setminus\{s_{j-1}\})\cup\{u_j\}}
-e_{(K\setminus\{s_j\})\cup\{u_j\}}
\right).
\tag{4.12}
\]

If

\[
t(s)=|\{j:s_{j-1}\ne s_j\}|,
\]

then the unique outside label \(u_j\) prevents cross-column cancellation,
and hence

\[
\boxed{
|\operatorname{supp}\Delta_C|=\|\Delta_C\|_1=2t(s).}
\tag{4.13}
\]

Let \(r\) be the number of touched old wreaths.  An omitted label occurs
exactly once on each exact wreath: if \(d_x\) is the number of cycle vertices
containing \(x\) and \(k_x\) is the number of edges omitting \(x\), then

\[
2d_x=n-k_x.
\]

Every \(k_x\) is positive and odd, and \(\sum_xk_x=n\), so \(k_x=1\) for
every \(x\).  The retained edges at distinct \(C_i\)'s are distinct: two
different \(C_i,C_j\) meet in at least \(m-2>0\) points, so they cannot be
the two endpoints of one odd-graph edge.  Therefore each value among the
\(s_i\)'s occurs at most \(r\) times.  Each cyclic
run has length at most \(r\), so

\[
t(s)\ge\left\lceil\frac{k}{r}\right\rceil,
\qquad
\boxed{\|\Delta_C\|_1\ge2\left\lceil\frac{k}{r}\right\rceil.}
\tag{4.14}
\]

Using the actual profiles from Theorem A gives lower bounds \(4\) for
\(C_8\), \(6\) for \(C_{10}\), and \(6\) or \(4\) for a two- or
three-wreath \(C_{12}\).  In particular no exact common-core short trade is
first-shadow neutral, proving (1.13).

As a matrix with rows \(s\in K\) and columns \(u_j\), (4.12) is a bipartite
circulation.  When \(t(s)=2\), it is exactly one elementary rectangle.  The
universal MSW \(C_8\) in Section 5 attains this sharp case.

### Theorem 4.2 — sharp five-active-label neutrality criterion

Continue to assume that both endpoint factors are exact.  Assume
\(m\ge4\), \(q=5\), and \(t=t'=2\).  This includes every
non-common-core \(C_{10}\) and the five-active-label subclass of
non-common-core \(C_{12}\).

Write

\[
c_i=S_i\cap S_{i+1},\qquad
d_i=Q\setminus(S_{i-1}\cup S_i\cup S_{i+1}).
\tag{4.15}
\]

The set \(d_i\) is a singleton.  Simplicity gives
\(a_{i-1}\ne b_i\): if they were equal, either
\(S_{i-1}=S_{i+1}\) or the consecutive upper unions, and hence the
corresponding \(C\)-vertices, would repeat.

Then

\[
\boxed{
\Delta_1=0
\quad\Longleftrightarrow\quad
s_i=c_i\text{ and }r_i=d_i\text{ for every }i.}
\tag{4.16}
\]

#### Proof

Here \(|K|=|Y|=m-2\).  At an \(A\)-center, the seam label is active, so
only the retained label can remove a member of \(Y\).  Every
\(A\)-centered color therefore contains at least \(m-3\ge1\) labels of
\(Y\) and no label of \(K\).  Symmetrically every \(C\)-centered color
contains at least \(m-3\) labels of \(K\) and no label of \(Y\).  The two
sectors cannot cross-cancel.

At \(C_i\), the retained label is either in \(K\) or is the unique active
nonseam label \(c_i\).  For a fixed \(s\in K\), the contribution from the
indices with \(s_i=s\) is

\[
\sum_{i:s_i=s}
\left(e_{(K\setminus\{s\})\cup S_{i+1}}
-e_{(K\setminus\{s\})\cup S_i}
\right).
\tag{4.17}
\]

The \(S_i\)'s are distinct because the \(A_i=K\cup S_i\) are distinct
vertices of the simple alternating cycle.  The retained edges at distinct
\(C_i\)'s are also distinct: all \(C_i\)'s contain the nonempty common core
\(Y\), so no two of them are disjoint endpoints of one odd-graph edge.
Therefore (4.17) vanishes only when that set of
indices is successor-invariant, hence empty or all indices.  The all-indices
case would give \(k\) distinct same-label retained edges distributed among
only the \(r\) touched old wreaths.
The one-use omitted-label law permits at most one per wreath, contradicting
\(r\le k/2<k\).  Thus \(s_i=c_i\) for every \(i\).
The resulting \(C\)-sector is

\[
\sum_i(e_{K\cup\{b_i\}}-e_{K\cup\{a_i\}})=0,
\]

because exits and entries have the same multiset.

Interchanging the two parity classes gives the identical argument at the
\(A_i\)'s and forces \(r_i=d_i\).  With these retained labels the
\(A\)-sector is

\[
\sum_i(e_{Y\cup\{b_i\}}-e_{Y\cup\{a_{i-1}\}})=0.
\]

This proves necessity and sufficiency.  ∎

Criterion (4.16) is not an existence theorem.  It says that any neutral
exact trade in this regime must realize all the indicated retained factor
edges inside the same original exact factor.

### Theorem 4.3 — the remaining six-active-label \(C_{12}\) invariant

Continue to assume that both endpoint factors are exact.  Assume
\(m\ge4\), \(k=q=6\), and \(t=2,t'=3\).  Sector separation again
holds.  Neutrality forces

\[
s_i=c_i
\tag{4.18}
\]

for every \(i\).  The two seam labels \(a_{i-1},b_i\) are distinct.  If
they were equal, then either \(S_{i-1}=S_{i+1}\), repeating an
\(A\)-vertex, or the two
consecutive upper unions \(S_{i-1}\cup S_i\) and
\(S_i\cup S_{i+1}\) would coincide, repeating a \(C\)-vertex.  Therefore

\[
D_i=Q\setminus(S_i\cup\{a_{i-1},b_i\}),\qquad |D_i|=2.
\tag{4.19}
\]

Every \(r_i\) must belong to \(D_i\).  Let \(e_i\) be the other member of
\(D_i\).  Then full first-shadow neutrality is equivalent to the explicit
six-pair identity

\[
\boxed{
\bigl\{\{b_i,e_i\}:i\in\mathbb Z_6\bigr\}_{\rm multi}
=
\bigl\{\{a_{i-1},e_i\}:i\in\mathbb Z_6\bigr\}_{\rm multi}.}
\tag{4.20}
\]

Indeed the remaining \(A\)-sector is

\[
\sum_i\left(
e_{Y\cup\{b_i,e_i\}}
-e_{Y\cup\{a_{i-1},e_i\}}
\right).
\tag{4.21}
\]

For completeness, every \(C\)-centered color contains at least
\(m-3\ge1\) labels of \(K\), whereas every \(A\)-centered color is disjoint
from \(K\); hence the two center sectors cannot cross-cancel.  The retained
label at \(C_i\) is in \(K\) or equals \(c_i\).  The fixed-\(K\)-label
boundary argument from (4.17) excludes the former and proves (4.18).

At \(A_i\), cleanliness leaves \(r_i\in Y\cup D_i\).  Contributions with
\(r_i\in Y\) omit one member of \(Y\), while those with \(r_i\in D_i\)
contain all of \(Y\), so these subclasses cannot cancel.  For a fixed
\(y\in Y\), the first subclass is the boundary of the distinct active
three-sets

\[
T_i=Q\setminus(S_i\cup S_{i+1}).
\]

Its index set must again be successor-invariant, hence empty or all.  The
all-indices case would use six distinct retained edges with one omitted
label: the distinct \(A_i\)'s share the nonempty core \(K\), so no two can
be opposite endpoints of the same edge.  It therefore contradicts the
one-use omitted-label law and \(r\le3<6\).  Thus \(r_i\in D_i\) for every
\(i\), and direct deletion of
the retained and seam labels gives (4.21).  Equality of its two histograms
is exactly (4.20).

For the standard active walk \(Q=\mathbb Z_6\),
\(S_i=\{i,i+1\}\), identity (4.20) is impossible.  Here
\(D_i=\{i+3,i+4\}\).  If \(A\) is the set of indices with
\(e_i=i+3\), equality of the adjacent-pair terms in (4.20) forces
\(A=A^c+2\).  On each three-element parity orbit of translation by two,
this asks a set to have half of three elements, a contradiction.

No impossibility proof for every six-label Johnson walk is claimed.  Formula
(4.20) is the exact unresolved invariant in that last short-cycle regime.

## 5. A universal MSW trade is literally one alternating \(C_8\)

Use the omitted-edge representation of a wreath.  For a cyclic ordering
(that is, a permutation) of \([n]\),

\[
Q=(q_0,\ldots,q_{n-1}),
\]

put

\[
V_i(Q)=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\},
\qquad i\in\mathbb Z_n.
\tag{5.1}
\]

Then \(V_iV_{i+1}\) is an odd-graph edge omitting \(q_i\), and the
\(V_i\)'s form the wreath belonging to \(Q\).

Fix four distinct labels \(\alpha,\beta,\gamma,\delta\), and let \(T\) be
an arbitrary ordering of the other \(2m-3\) labels.  Define

\[
\begin{aligned}
C&=(\delta,\beta,\gamma,\alpha,T),&
D&=(\beta,\alpha,\delta,\gamma,T),\\
C'&=(\delta,\gamma,\beta,\alpha,T),&
D'&=(\gamma,\alpha,\delta,\beta,T).
\end{aligned}
\tag{5.2}
\]

The two old wreaths \(C,D\) are disjoint, the two new wreaths \(C',D'\)
are disjoint, and their middle supports have equal union.  The next theorem
strengthens this two-for-two incidence identity to an exact edge statement.

### Theorem 5.1 — literal \(C_8\) provenance

The symmetric difference of the old edge union \(E(C)\cup E(D)\) and the
new edge union \(E(C')\cup E(D')\) is one simple alternating \(C_8\).

#### Proof

For \(i=4,5,\ldots,n\), where \(V_n=V_0\), one has

\[
V_i(C)=V_i(D'),\qquad V_i(D)=V_i(C').
\tag{5.3}
\]

At \(i=4\), the selected exceptional positions are \(0,2\).  Their sets
are \(\{\delta,\gamma\}\) in both \(C,D'\), and
\(\{\beta,\delta\}\) in both \(D,C'\).  The two words in each pair have
the same omitted labels from position four onward, so the equality
propagates along the entire long path.

The three-vertex short paths obey

\[
V_1(C)=V_3(C'),\quad V_2(C)=V_2(C'),\quad V_3(C)=V_1(C'),
\tag{5.4}
\]

and

\[
V_i(D)=V_i(D')\qquad(i=1,2,3).
\tag{5.5}
\]

For example, \(V_1(C)\) consists of the even tail positions together with
the label at exceptional position two, namely \(\gamma\); this is
\(V_3(C')\), whose exceptional contribution is the same label at position
one.  The other identities follow identically.

Thus only edges \(0\) and \(3\) of each old and new wreath differ.  Write

\[
c_i=V_i(C),\qquad d_i=V_i(D).
\]

The changed edge union is

\[
\boxed{
c_0-c_1-d_4-d_3-c_4-c_3-d_0-d_1-c_0.}
\tag{5.6}
\]

The edges alternate old and new around (5.6).  Its eight vertices are
distinct because the old wreath supports \(C,D\) are disjoint and the four
listed phase positions within either wreath are distinct.  Hence (5.6) is a
simple alternating \(C_8\).  The inherited paths in each old wreath have
orders \(3,n-3\), independently confirming (2.24).  ∎

### Theorem 5.2 — unconditional exact-factor extension

Every instance (5.2) occurs, after a coordinate relabeling, as a canonical
size-two component of an MSW exact factor.  Replacing \(C,D\) by \(C',D'\)
therefore gives another exact factor.

#### Proof

Fix one canonical MSW four-letter component with tail \(T_0\).  A coordinate
permutation can send its four exceptional labels and the ordered tail
\(T_0\) to the arbitrary labels and ordered tail in (5.2).  The images of
its old wreaths lie in the correspondingly relabeled MSW factor.  The new
wreaths are disjoint and have exactly the same middle support union as the
old pair.  All untouched MSW wreaths are therefore still disjoint from the
new pair.  This produces an exact factor-to-factor switch.  No partial-packing
extension lemma is being assumed.  ∎

### Theorem 5.3 — exact multirank increment of the MSW \(C_8\)

Write

\[
T=(t_0,t_1,\ldots,t_{2m-4}),
\]

and split it into the parity lists

\[
E=(t_0,t_2,\ldots,t_{2m-4}),\qquad
O=(t_1,t_3,\ldots,t_{2m-5}).
\tag{5.7}
\]

For a set \(H\) avoiding \(\beta,\gamma\), put

\[
\partial H=e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.
\tag{5.8}
\]

Let

\[
z=e_{C'}+e_{D'}-e_C-e_D.
\]

For \(2\le r\le m-1\), with \(\ell=r-1\),

\[
\boxed{
B_rz=
\partial\operatorname{suf}_{\ell}(O)
+\partial\operatorname{suf}_{\ell}(E)
-\partial\operatorname{pre}_{\ell}(E)
-\partial\operatorname{pre}_{\ell}(O).}
\tag{5.9}
\]

Also

\[
B_1z=B_mz=0.
\tag{5.10}
\]

To prove (5.9), read a rank-\(r\) interval in the step-two word.  The four
exceptional positions occur in two adjacent pairs.  A window with
\(r<m\) cannot meet both pairs.  Windows meeting neither pair or both
positions of one pair cancel between the four words.  The four windows
meeting exactly one exceptional position have the four prefix/suffix cores
in (5.9), with the displayed signs.  At rank one the four copies cancel;
the middle-rank two-for-two identity gives (5.10).

At first-shadow rank, put

\[
x=t_0,\qquad y=t_{2m-4},\qquad
K=E\setminus\{x,y\}.
\]

The two \(O\)-terms in (5.9) cancel and

\[
\boxed{
B_{m-1}z=
e_{K\cup\{x,\beta\}}-e_{K\cup\{x,\gamma\}}
-e_{K\cup\{y,\beta\}}+e_{K\cup\{y,\gamma\}}.}
\tag{5.11}
\]

This is one elementary rectangle.  At every rank
\(2\le r\le m-2\), (5.9) has exactly eight distinct \(\pm1\) cells.  The
distinctness follows because the four
proper prefix/suffix cores lie in disjoint parity lists or are distinct
proper ends of one list.  Thus first-shadow rectangle generation does not
give independent control of deeper shadows.

## 6. Integral generation of the balanced deficit lattice

The proof of (1.9) has two parts: every rectangle has an exact \(C_8\) lift,
and rectangles generate the entire integer kernel.

### Lemma 6.1 — every rectangle has an exact MSW \(C_8\) lift

Given (1.8), choose the even tail list in (5.7) as

\[
E=(b,K,b'),\qquad \beta=a,\qquad\gamma=a'.
\tag{6.1}
\]

There are exactly \(m\) unused labels.  Choose two of them as
\(\alpha,\delta\), order the remaining \(m-2\) labels as \(O\), and
interleave \(E,O\) to form \(T\).  Equation (5.11) gives
\(R_K(a,a';b,b')\), up to the harmless choice of global sign.  Theorem 5.2
makes this a literal exact factor-to-factor \(C_8\).

### Lemma 6.2 — rectangles integrally generate \(\ker U_r\)

Let \(2\le r\le n-2\).  In the quotient of
\(\mathbb Z^{\binom{[n]}r}\) by the subgroup generated by all rectangles,
take distinct \(a,b\) and an \((r-1)\)-set \(P\) avoiding them, and put

\[
\delta_{ab}(P)=e_{P\cup\{a\}}-e_{P\cup\{b\}}.
\tag{6.2}
\]

If \(P=H\cup\{c\}\) and \(P'=H\cup\{d\}\) are adjacent in
\(J(n-2,r-1)\), then

\[
\delta_{ab}(P)-\delta_{ab}(P')
=R_H(c,d;a,b).
\tag{6.3}
\]

The Johnson graph is connected, so the quotient class of (6.2) is
independent of \(P\); call it \(g_{ab}\).  Choose one common \(P\) avoiding
three distinct labels \(a,b,c\).  Then

\[
g_{ab}+g_{bc}=g_{ac}.
\tag{6.4}
\]

Fix a base label \(p\), put \(h_x=g_{xp}\) and \(h_p=0\), and obtain

\[
g_{ab}=h_a-h_b.
\tag{6.5}
\]

Along a Johnson path from a fixed \(r\)-set \(S_0\) to \(S\), equations
(6.2) and (6.5) give

\[
e_S-e_{S_0}\equiv
\sum_{x\in S}h_x-\sum_{x\in S_0}h_x
\pmod{\langle R\rangle}.
\tag{6.6}
\]

Now let \(d=\sum_Sd_Se_S\in\ker_{\mathbb Z}U_r\).  Summing all point
margins gives

\[
r\sum_Sd_S=0,
\]

so \(\sum_Sd_S=0\) integrally.  Summing (6.6) with coefficients \(d_S\)
then gives

\[
d\equiv
\sum_x(U_rd)_xh_x=0
\pmod{\langle R\rangle}.
\tag{6.7}
\]

Every rectangle visibly lies in \(\ker U_r\), proving equality of the two
integer lattices.  No division, saturation, or rational lifting is used.
∎

Taking \(r=m-1\) and combining Lemmas 6.1--6.2 proves Theorem C.

For reference, \(U_{m-1}\) has row rank \(n\): a linear relation among its
rows would say that the sum of the corresponding point weights is zero on
every \((m-1)\)-set; comparing two sets differing by one point makes all
weights equal, and then they are zero.  Therefore

\[
\operatorname{rank}\mathcal L_{m-1}
=\binom{2m+1}{m-1}-(2m+1).
\tag{6.8}
\]

## 7. Fixed-core bipartite generation with congestion

Under the hypotheses of Theorem D, applying \(U_{m-1}\) to (1.10) shows
that the margins at \(a\in A\) and \(b\in B\) are the row and column sums
of \((d_{ab})\).  Their vanishing also makes the total sum zero, which is
the common margin at every point of \(K\).  Thus row/column balance is
equivalent to membership in \(\mathcal L_{m-1}\) on this support.

Construct a directed bipartite multigraph by taking

- \(d_{ab}\) copies of \(a\to b\) when \(d_{ab}>0\), and
- \(-d_{ab}\) copies of \(b\to a\) when \(d_{ab}<0\).

Every vertex has equal indegree and outdegree.  Decompose this integral
Eulerian multigraph into directed simple cycles.  Write one such cycle's
increment, after cyclic indexing, as

\[
q=\sum_{i=1}^{s}
\left(e_{K\cup\{a_i,b_i\}}-e_{K\cup\{a_i,b_{i-1}\}}\right),
\qquad b_0=b_s.
\tag{7.1}
\]

Anchoring at \(a_1\) gives the exact triangulation

\[
\boxed{
q=\sum_{i=2}^{s}R_K(a_i,a_1;b_i,b_{i-1}).}
\tag{7.2}
\]

The anchor terms telescope.  A cycle containing \(s\) positive units uses
\(s-1\) rectangles.  Since all cycles together contain \(M\) positive
units, the total number of rectangles is

\[
M-\#\{\text{cycles}\}\le M.
\tag{7.3}
\]

For the cell-congestion bound, a simple cycle not anchored at row \(a\)
uses cell \((a,b)\) at most once and only when that cell is an original
cycle edge.  A cycle anchored at \(a\) uses a nonincident chord cell
\((a,b)\) at most twice, and an incident cell once.  The number of
decomposed cycles containing row \(a\) is at most \(p_a\), and the number
containing column \(b\) is at most \(p_b\).  Every one of the
\(|d_{ab}|\) original directed copies saves one incidence from the crude
two-per-common-cycle bound.  Hence

\[
c_{ab}\le2\min(p_a,p_b)-|d_{ab}|.
\tag{7.4}
\]

Since \(p_a,p_b\le\Delta/2\), (1.12) follows.  Lemma 6.1 lifts every term
of (7.2) to an exact MSW-orbit \(C_8\).  This proves Theorem D.

## 8. What one fixed MSW factor does not generate

Continue to assume \(m\ge3\).

The orbit theorem in Section 6 deliberately ranges over coordinate-relabeled
exact factors.  Two exact fixed-factor obstructions show why that scope is
essential.

### 8.1 The complete fixed \((2\ 3)\)-interaction cube

Let \(F_m\) be the canonical MSW factor and \(\tau=(2\ 3)\).  The exact
interaction-component classification between \(F_m\) and \(\tau F_m\) is

\[
K_{j,R},\qquad
0\le j\le m-2,\qquad R\in\mathcal D_{m-j-2},
\tag{8.1}
\]

where \(\mathcal D_t\) is the set of Dyck words of semilength \(t\).  These
are all ownership components, so all of them are simultaneously switchable.
Indeed, one interaction component contains whole old and new wreaths with
the same middle-vertex union.  Replacing the old side by the new side in any
set of pairwise disjoint interaction components leaves a disjoint union of
length-\(n\) wreaths, hence another exact factor.
Their number is

\[
S_m=\sum_{t=0}^{m-2}\operatorname{Cat}_t.
\tag{8.2}
\]

Let \(\Delta_{j,R}\) be the first-shadow effect of component \(K_{j,R}\).
The exact colex-pivot theorem gives its smallest nonzero target, with
coefficient \(+1\), as

\[
P_{j,R}=
\begin{cases}
\{2\}\cup(4+\operatorname{Down}(R)),&j=0,\\[1mm]
\{2\}\cup[4,j+3]\cup
(2j+4+\operatorname{Up}(R)),&1\le j\le m-3,\\[1mm]
\{2,5,7,\ldots,2m-1\},&j=m-2.
\end{cases}
\tag{8.3}
\]

Here \(\operatorname{Up}(R)\) and \(\operatorname{Down}(R)\) are the sets
of up-step and down-step positions of \(R\).

These pivots are pairwise distinct: the case \(j=0\) contains \(2m\), an
interior \(j\) is recovered from its initial consecutive run, the top case
omits \(4\), and then the shifted up/down set recovers \(R\).  Ordering
columns by (8.3) makes their pivot submatrix triangular with diagonal one.
Therefore, over every field and in particular over \(\mathbb Z\),

\[
\boxed{
\sum_{j,R}c_{j,R}\Delta_{j,R}=0
\quad\Longrightarrow\quad c_{j,R}=0\text{ for every }(j,R).}
\tag{8.4}
\]

Consequently:

1. no nonempty \(0/1\) component selection from this complete cube
   preserves the first shadow;
2. no nonzero signed integer combination does so either; and
3. the projection of the cube's full multishadow increment lattice to rank
   \(m-1\) is injective, so this cube cannot create a deeper-only correction.

It is also much too small to generate \(\mathcal L_{m-1}\).  Since
\(W=\binom{2m+1}m=(2m+1)\operatorname{Cat}_m\),

\[
S_m\le2\operatorname{Cat}_{m-2}
\le\frac25\operatorname{Cat}_m,
\tag{8.5}
\]

whereas

\[
\operatorname{rank}\mathcal L_{m-1}
=W\left(\frac{m}{m+2}-\frac1{\operatorname{Cat}_m}\right)
\ge\frac25W
\qquad(m\ge3).
\tag{8.6}
\]

The first inequality follows inductively from
\(\operatorname{Cat}_{t+1}\ge2\operatorname{Cat}_t\) for \(t\ge1\); the
second uses

\[
\frac{\operatorname{Cat}_m}{\operatorname{Cat}_{m-2}}
=\frac{4(2m-1)(2m-3)}{m(m+1)}\ge5.
\]

The lower bound in (8.6) is equality at \(m=3\) and then increases.

This is an invariant obstruction, not merely a dimension heuristic.

### 8.2 The shifted local \(C_8\) atlas

The same four-letter component occurs at every Dyck concatenation boundary.
The number of occurrences in the canonical MSW atlas is

\[
\sum_{p=0}^{m-2}
\operatorname{Cat}_p\operatorname{Cat}_{m-p-2}
=\operatorname{Cat}_{m-1}.
\tag{8.7}
\]

At a fixed boundary \(p\), the
\(\operatorname{Cat}_p\operatorname{Cat}_{m-p-2}\) negative supports are
disjoint and the switches are simultaneous.  Across different boundaries
they can overlap and do not form one flat cube.

The first-shadow rectangles of all occurrences in (8.7) are linearly
independent.  More precisely, index an occurrence by
\((p,P,R)\), let \(\mathsf E_{p,P,R}\) be its even tail list, let
\(E_{p,P,R}\) be the underlying set, let \(x_{p,P,R}\) be the first entry
of \(\mathsf E_{p,P,R}\), and put

\[
\beta_p=2p+2,\qquad
S^*_{p,P,R}=
E_{p,P,R}\setminus\{x_{p,P,R}\}\cup\{\beta_p\}.
\tag{8.8}
\]

The first-negative Dyck position of this target is \(2p+1\).  The target is
absent from every lower-\(p\) column and, at level \(p\), occurs only in its
own column with coefficient \(\pm1\); its suffix recovers \(R\), while its
first \(2p\) coordinates recover \(P\).  Ordering levels from high to low
therefore makes the resulting
\(\operatorname{Cat}_{m-1}\)-square minor triangular with diagonal
entries \(\pm1\).  Their integer span is therefore a primitive rank-
\(\operatorname{Cat}_{m-1}\) sublattice, far below (6.8).

There is also an explicit coordinate invariant.  These rectangles touch at
most \(4\operatorname{Cat}_{m-1}\) first-shadow cells, and

\[
\frac{\binom{2m+1}{m-1}}{\operatorname{Cat}_{m-1}}
=\frac{(2m-1)(2m)(2m+1)}{(m+1)(m+2)}>4
\qquad(m\ge3).
\tag{8.9}
\]

Choose an untouched cell \(S\).  Evaluation at \(S\) annihilates every
known atlas increment but not \(\mathcal L_{m-1}\): choose
\(K\subset S\), \(|K|=m-3\), write \(S=K\cup\{a,b\}\), choose two labels
\(c,d\notin S\), and use the rectangle
\(R_K(a,c;b,d)\), whose coefficient at \(S\) is one.

This proves failure of the known local atlas and of the complete fixed
\((2\ 3)\)-cube.  It does not classify additional clean \(C_8\)'s which
might be present at the canonical MSW factor, and it does not contradict the
coordinate-orbit generation theorem.

## 9. PBBS common-core supply and its invariant obstruction

This section uses one exact structural input from the explicit canonical
PBBS construction: for each core \(K\), all heads in the auxiliary digraph
below lie in a set \(S_K\) of size at most six.  The conclusions derived
from that input are purely finite mathematics.

For a general 2-factor \(F\), write \(Y_F(X),Z_F(X)\) for the two factor
neighbors of a middle vertex \(X\).  Let \(\Gamma(F)\) be the histogram of the
centered colors

\[
X\longmapsto Y_F(X)\cap Z_F(X),
\]

which are defined at every middle vertex, and for an alternating candidate
put

\[
\widehat\Delta_1^F(Z)=\Gamma(F\triangle Z)-\Gamma(F).
\tag{9.0}
\]

The vertex-local proof of (3.2) applies without an exactness hypothesis and
computes \(\widehat\Delta_1^F(Z)\).  It equals the exact-wreath increment
\(\Delta_1=B_{m-1}(F\triangle Z)-B_{m-1}F\) only when both endpoint factors
are exact wreath factors.  Throughout Section 9, “increment” means the
formal centered-color vector \(\widehat\Delta_1\).  Thus the PBBS lattice
calculations are local centered-color obstructions until exact rebundling is
separately certified.

### 9.1 Auxiliary-digraph dictionary

Fix \(K\in\binom{[n]}{m-1}\), put \(B=[n]\setminus K\), and for a 2-factor
\(F\) define the loopless digraph \(D_K^F\) on \(B\) by

\[
u\to v
\quad\Longleftrightarrow\quad
F\text{ contains the edge }
\{K\cup\{u\},\ B\setminus\{u,v\}\}.
\tag{9.1}
\]

Every vertex has outdegree exactly two, corresponding to the two factor
neighbors of \(K\cup\{u\}\).

A directed simple cycle

\[
u_0\to u_1\to\cdots\to u_{k-1}\to u_0
\tag{9.2}
\]

gives the common-core vertices

\[
A_i=K\cup\{u_i\},\qquad
C_i=B\setminus\{u_i,u_{i+1}\}.
\tag{9.3}
\]

It is an \(F\)-alternating \(C_{2k}\) exactly when every reverse arc
\(u_{i+1}\to u_i\) is absent.  Call such a directed cycle clean.  Conversely
every common-core alternating cycle arises this way.  The alternating
edge-label word is

\[
\lambda_{2i}=u_{i+1},\qquad
\lambda_{2i+1}=u_i,
\tag{9.4}
\]

so every active label appears twice, at gaps three and \(2k-3\).

For the canonical PBBS factor, the six-label theorem gives

\[
\text{every arc head lies in }
S_K=U_+(K)\cup U_-(K),\qquad |S_K|\le6.
\tag{9.5}
\]

Every directed cycle is therefore contained in \(S_K\).  Among common-core
alternating cycles of length at least eight, only \(C_8,C_{10},C_{12}\)
can occur.

### 9.2 PBBS candidate-count upper bounds and graph congestion

Rooting a directed \(k\)-cycle gives at most

\[
6\cdot2^{k-1}
\tag{9.6}
\]

choices: choose the root in \(S_K\), then at most two choices at each of
the next \(k-1\) steps, and finally test closure and simplicity.  Every
unrooted directed cycle has \(k\) roots.  Thus

\[
c_4(K)\le12,\qquad c_5(K)\le19,\qquad c_6(K)\le32.
\tag{9.7}
\]

For \(k=5\), the rooted count is a multiple of five and is at most \(96\),
so it is at most \(95\), giving \(19\).

Summing over cores gives

\[
N_8\le12\binom n{m-1},\quad
N_{10}\le19\binom n{m-1},\quad
N_{12}\le32\binom n{m-1},
\tag{9.8}
\]

and their total is less than \(63\binom n m\).

A fixed directed arc lies in at most \(2^{k-2}\) directed \(k\)-cycles.
A factor edge has exactly \(2m\) core-arc representations: choose either
endpoint as the \(A\)-vertex and then choose the distinguished \(u\) in
that endpoint.  Hence the factor-edge congestion is at most

\[
8m,\qquad16m,\qquad32m
\tag{9.9}
\]

for \(C_8,C_{10},C_{12}\), and the corresponding middle-vertex congestion
is

\[
16m,\qquad32m,\qquad64m.
\tag{9.10}
\]

For the mixed union these are \(56m\) per factor edge and \(112m\) per
middle vertex.  Therefore a greedy vertex-disjoint subfamily from \(L\)
candidates has size at least

\[
\frac{L}{1344m}.
\tag{9.11}
\]

This is only a graph-disjoint candidate bound.  It neither proves that an
individual candidate preserves exact \(C_n\)-components nor that a family
of candidates can be switched while retaining exactness.

### 9.3 Fixed-core lattice obstruction for PBBS centered-color candidates

Assume \(m\ge3\) and

\[
4\le s=|S_K|\le\min(6,m+2).
\]

Put \(S=S_K\), \(p=|K|=m-1\), and
define the disjoint target sectors

\[
\mathcal A_K(S)=\{B\setminus R:R\in\tbinom{S}{3}\},
\tag{9.12}
\]

\[
\mathcal C_K(S)=
\{(K\setminus\{a\})\cup\{u\}:a\in K,\ u\in S\}.
\tag{9.13}
\]

The PBBS local-coordinate lemma puts the labels \(u_i,r_i\) in \(S_K\).
Thus the centered-color increment of every PBBS common-core
\(C_8,C_{10},C_{12}\) candidate based at \(K\) is supported on
\(\mathcal A_K(S)\dot\cup\mathcal C_K(S)\).

Let

\[
\mathcal L_K(S)=
\ker_{\mathbb Z}U_{m-1}\cap
\mathbb Z^{\mathcal A_K(S)\cup\mathcal C_K(S)}.
\tag{9.14}
\]

Then

\[
\boxed{
\operatorname{rank}\mathcal L_K(S)
=\left(\binom s3-s\right)+p(s-1).}
\tag{9.15}
\]

To see this, write the \(\mathcal A\)-coefficients as a vector on triples
of \(S\), and the \(\mathcal C\)-coefficients as a \(p\times s\) matrix.
The \(K\)-margins first force the total \(\mathcal C\)-coefficient and
every matrix row sum to be zero: the margin at row label \(a\in K\) is the
matrix total minus row \(a\), and summing these \(p\ge2\) equations gives
\((p-1)\) times the matrix total equal to zero.  Summing all point margins
then forces the
total \(\mathcal A\)-coefficient to be zero (when \(B\setminus S\ne
\varnothing\), any one of those outside labels gives the same equation
directly).  The \(\mathcal A\) point-margin map onto the zero-sum lattice on
\(S\) has rank \(s-1\), and the matrix column margins cancel those
\(\mathcal A\)-margins.  Counting the free kernel and matrix dimensions
gives (9.15).

Every common-core cycle satisfies the stronger condition that its two
sectors are separately point-balanced, by (4.10)--(4.11).  The lattice with
this stronger property has rank

\[
\left(\binom s3-s\right)+(p-1)(s-1),
\tag{9.16}
\]

and hence exact codimension

\[
\boxed{s-1}
\tag{9.17}
\]

inside \(\mathcal L_K(S)\).

The missing quotient is explicit.  For distinct \(u,v\in S\), choose
\(a\in K\) and

\[
P\subseteq S\setminus\{u,v\},\qquad |P|=s-4,
\qquad H=(B\setminus S)\cup P.
\]

Then

\[
\begin{aligned}
x_{u,v}={}&
e_{(K\setminus\{a\})\cup\{v\}}
-e_{(K\setminus\{a\})\cup\{u\}}\\
&+e_{H\cup\{u\}}-e_{H\cup\{v\}}
\end{aligned}
\tag{9.18}
\]

belongs to \(\mathcal L_K(S)\), but its \(\mathcal C\)-sector point margin
is \(e_v-e_u\ne0\).  Thus the map taking a vector in
\(\mathcal L_K(S)\) to its \(\mathcal C\)-sector point margin is integrally
surjective onto the zero-sum lattice on \(S\), because the images of the
\(x_{u,v}\)'s are its root generators.  Its kernel is precisely the
sectorwise-balanced sublattice.  Hence (9.17) is sharp integrally.

There is a further PBBS-specific restriction.  Call an arc \(e=(u,v)\)
clean when its reverse arc is absent.  At
\(C_{uv}=B\setminus\{u,v\}\), let \(s(e)\) be the omitted label of the
factor edge other than the arc edge from \(K\cup\{u\}\).  Cleanliness gives
\(s(e)\in K\): the two seam labels are \(u,v\), and the reverse arc would
be precisely the retained edge omitting \(u\).  Put

\[
g_e=e_{(K\setminus\{s(e)\})\cup\{v\}}
-e_{(K\setminus\{s(e)\})\cup\{u\}}.
\tag{9.19}
\]

The \(\mathcal C\)-sector of a clean directed cycle is \(\sum_{e\in C}g_e\).
Let \(D_K^{[4,6]}\) be the union of the arcs occurring in clean directed
cycles of lengths four, five, or six.  The span under discussion is
contained in the image of the ordinary circulation lattice of this relevant
subgraph.  Let \(t\le s\) be the
number of nonisolated vertices of \(D_K^{[4,6]}\).  The subgraph has
outdegree at most two and at most one
cycle-containing weak component: every such component contains one of the
relevant cycles and hence at least four vertices, so two would require at
least eight.  Every nonisolated component is cycle-containing because every
retained arc lies on a relevant cycle.  Thus the relevant subgraph is empty
or has one nonisolated weak component, and its circulation rank is at most

\[
|E|-t+1\le2t-t+1\le s+1\le7.
\tag{9.20}
\]

Thus the PBBS \(\mathcal C\)-sector ranks are at most \(5,6,7\) for
\(s=4,5,6\), whereas the full sectorwise-balanced matrix lattice has rank

\[
(m-2)(s-1).
\tag{9.21}
\]

For \(m\ge4\), the bound (9.20) is strictly smaller than (9.21) for every
\(s\in\{4,5,6\}\), giving a further fixed-core obstruction independent of
the raw candidate counts.  At \(m=3\), (9.20) remains a valid upper bound,
but this comparison alone does not prove properness.  The earlier
sector-codimension obstruction (9.17) remains valid throughout its stated
domain \(s\ge4\).

### 9.4 Cross-core routing

Every common-core first-shadow increment with core \(K\) is supported on

\[
\Sigma(K)=
\left\{T\in\binom{[n]}{m-1}:
|T\cap K|\in\{0,m-2\}\right\}.
\tag{9.22}
\]

If \(\Sigma(K)\cap\Sigma(K')\ne\varnothing\), then a direct comparison of
the two possible intersection sizes gives

\[
\boxed{|K\cap K'|\le1\quad\text{or}\quad|K\cap K'|\ge m-4.}
\tag{9.23}
\]

Thus cancellation between common-core short trades can propagate only
between near-disjoint or very close cores.  If candidates at several cores
separately pass the exact-factor gate, Theorem 4.1 makes each resulting
increment nonzero.  Therefore any family of such exact common-core trades
whose cores satisfy

\[
2\le|K\cap K'|\le m-5
\]

pairwise has disjoint first-shadow supports and is linearly independent,
because each individual increment has nonzero \(\Delta_C\).

## 10. Audited implication scope and remaining obstruction

The decisive steps were independently rederived after the main proof was
written.

1. The path identities (5.3)--(5.5) give exactly the four removed and four
   added edges in (5.6); one short path reverses, and the other three
   inherited paths keep orientation.
2. Equation (5.11) has the stated signs and every rectangle has enough
   unused labels for the auxiliary \(\alpha,\delta,O\) positions.
3. The quotient proof in Lemma 6.2 is integral for
   \(2\le r\le n-2\).  It does not rely on a modular claim.  In
   characteristic dividing \(r\), the full modular kernel of \(U_r\) has an
   extra nonliftable dimension; this does not affect the integral theorem.
4. The congestion triangulation (7.2) was checked edge by edge.  The sharper
   bound (7.4), rather than the initial \(3\Delta/2\) estimate, is valid.
5. The residual-incidence matrices and the boundary count (3.9) were
   independently reconstructed from row/column length balance.  The
   one-sign *raw* mass is exactly \(b_h\); the positive and negative masses
   of the reduced increment are only bounded above by \(b_h\).

What is proved is therefore:

- a complete cut-count, incidence, length-balance, centered-balance, and
  boundary-deck classification for every actual exact
  \(C_8,C_{10},C_{12}\);
- a complete no-go theorem for first-shadow neutrality of an exact
  common-core \(C_8,C_{10}\), or \(C_{12}\);
- for \(m\ge4\), an exact neutrality criterion for every non-common-core
  \(C_{10}\) and for the five-active-label \(C_{12}\) regime;
- an explicit unresolved six-pair invariant for the remaining six-label
  \(C_{12}\) regime;
- full integral generation of the ambient first-shadow balanced lattice by
  coordinate-relabelled exact MSW \(C_8\)'s;
- a nontrivial fixed-core bipartite generation theorem with maximum cell
  congestion at most \(\Delta\); and
- sharp invariant obstructions for the complete fixed MSW interaction cube,
  the known local MSW atlas, and one PBBS common core.

What is not proved is equally important:

1. The rectangle summands of a general decomposition need not be
   simultaneously available in one exact factor.
2. The bounded cell-congestion theorem does not bound middle-wreath support
   congestion and does not decompose an arbitrary global balanced vector
   into fixed-core bipartite sectors with the same \(\Delta\).
3. The PBBS six-label counts do not certify exact-wreath preservation.
4. No first-shadow-neutral exact non-common-core \(C_{10}\) or \(C_{12}\)
   is constructed here; Theorems 4.2--4.3 give necessary-and-sufficient
   retained-label tests conditional on the rest of the exact trade.
5. First-shadow generation does not isolate deeper shadows.  The exact MSW
   formula (5.9) shows the correlated lower-rank flag dipoles explicitly.
6. The non-common-core neutrality problem at \(m=3\) is not covered by the
   sector-separation proofs in Theorems 4.2--4.3.
7. The ambient signed-lattice generation theorem does not by itself prove
   MWB, construct a literal contiguous-OR word, or supply labelled
   common-owner synchronization.  Such an implication would require one
   integral exact-factor route, not a sum of generators drawn from different
   coordinate-relabelled factors.

The sharp outcome is thus a positive ambient generation theorem and a
negative fixed-chart theorem.  Possible routes to balanced deeper correction
inside one exact factor include adaptive recomputation, additional
fixed-factor trades (local or nonlocal), or cancellation across the sparse
near/antipodal core-overlap graph.  The complete fixed MSW cube cannot
produce a deeper-only correction, and the known local MSW atlas does not
span the balanced first-shadow lattice.  For one PBBS core, what is proved
is only failure to span the full local balanced lattice; whether that
candidate library contains useful first-shadow relations remains unresolved.
