# Lane K: exact non-row-power multi-parent trades at (k=15)

Date: 2026-07-28

Method: pure mathematics applied to the audited parent artifacts. No new
finite search is claimed in this note.

## 0. Result and exact boundary

Close every middle Hamilton path through one dummy vertex. Relative to the
closed Hall-29 parent (H_{29}), every exact successor factor selected from
the directed union of

\[
 H_{29},\qquad H_{30},\qquad H_{31},\qquad
 H_\tau:=\tau H_{29},\quad \tau=(1\ 12),
\tag{0.1}
\]

has a unique **head-transfer permutation** (p). The nontrivial cycles of
(p) are exactly the base-alternating trade circuits. This gives the
following sharp classification.

1. In a two-parent union, bijectivity forces the shore choice to be constant
   on every assignment component. Thus the Boolean relabel cube is not a
   modelling restriction: it is the complete two-parent exact-factor space.
2. A genuinely non-row-power trade is exactly a **rainbow transfer cycle**:
   no single donor parent supplies its entire replacement shore.
3. If the changed tails have cyclic order (\rho) on closed (H_{29}), and
   (p) is their transfer permutation, then the number of resulting carrier
   components is

   \[
                         c(p\rho).
   \tag{0.2}
   \]

   Hence the child is Hamilton if and only if (p\rho) is one cycle.
4. Every Hamilton transfer permutation is even. A two-tail switch always
   splits the carrier. The support-minimal Hamilton escape from row-power is
   a **forward rainbow (C_6)**: three cuts (x_1,x_2,x_3) in base order
   and the replacement arcs

   \[
   x_1\longrightarrow f_0(x_2),\qquad
   x_2\longrightarrow f_0(x_3),\qquad
   x_3\longrightarrow f_0(x_1).
   \tag{0.3}
   \]

5. There is an exact bounded-window composition theorem for residence,
   every upper trace, and every lower compiler fibre. For separated seams,
   one changed seam requires at most (9) new residence tests and has (28)
   new upper-window slots and (30) new lower-compiler-cell slots; the old
   shore has the same one-sided bounds. A forward (C_6) therefore has
   one-sided collar budgets (27,84,90), respectively.
6. There is an exact **no-relocation matching criterion**. Freeze an actual
   maximum compiler matching of (H_{29}), transport all unaffected matched
   cells, and rematch the targets released in the changed collars together
   with old unmatched targets. If the local residual matching gains (r),
   then the global deficiency drops by (r). This is stronger than crossing
   any fixed list of DM inequalities and cannot hide the defect in a new
   block.

The fourth parent has strong raw capacity: it supplies all seven zero fibres
of (H_{29}), has (92,359,333) cells of slack on the three screened target
families, and contributes (3861) arcs outside the three-parent union.
Nevertheless it has its own conjugate Hall-29 block. Thus the present report
does **not** claim Hall zero. The exact missing certificate is now sharply
identified: a residence-safe, all-upper-preserving rainbow cycle or cycle
deck satisfying the protected matching augmentation criterion.

## 1. Frozen (k=15) data

Let

\[
 V=\binom{[15]}8,\qquad |V|=6435,
\tag{1.1}
\]

and let (\Omega=V\cup\{\partial\}), where (\partial) closes a spanning
path to one (6436)-cycle. The lower compiler has

\[
 16383=\sum_{j=1}^{7}\binom{15}{j}
\tag{1.2}
\]

target vertices and (19311) physical depth-(0,1,2) cells.

The three audited parents are

\[
\begin{array}{c|c|c|c}
\text{parent}&\text{artifact}&\text{matching}&\text{deficiency}\\ \hline
H_{29}&\texttt{scratch/k15\_doubletrans\_05\_213\_hall29.json}
 &16354&29\\
H_{30}&\texttt{scratch/k15\_outer2\_p1\_h30\_bridge.json}
 &16353&30\\
H_{31}&\texttt{scratch/k15\_trans1113\_balanced\_hall31.json}
 &16352&31.
\end{array}
\tag{1.3}
\]

Each is one Hamilton path, has exact depth-three residence, and has every
upper trace complete for (q=1,\ldots,7). The directed three-parent catalogue
contains (15890) distinct physical arcs.

For (H_{29}), the canonical DM target shore (A_{29}) satisfies

\[
 |A_{29}|=1524,\qquad h_{A_{29}}(H_{29})=1495.
\tag{1.4}
\]

Its seven zero-candidate targets are

\[
 \mathcal Z=\{2575,5801,13616,13620,17738,21641,29776\}.
\tag{1.5}
\]

The fourth parent is the literal coordinate conjugate

\[
 H_\tau=(1\ 12)H_{29}.
\tag{1.6}
\]

Its frozen screen and middle path are in
(\texttt{scratch/k15\_transposition\_parent\_winner.json}).

Coordinate conjugation preserves Hamiltonity, residence, all upper ledgers,
and compiler matching number. Its audited screen is

\[
 \bigl(c_{H_\tau}(z):z\in\mathcal Z\bigr)
 =(4,1,4,1,2,1,3),
\tag{1.7}
\]

and

\[
\begin{array}{c|c|c|c}
 A&|A|&h_A(H_\tau)&h_A(H_\tau)-|A|\\ \hline
 A_{29}&1524&1616&92\\
 R_3&1530&1889&359\\
 R_4&1374&1707&333.
\end{array}
\tag{1.8}
\]

It contributes (3861) physical arcs absent from the first three parents,
so the four-parent physical arc union has (19751) distinct arcs. These are
source-capacity statements, not a compatible-selection theorem.

The exact full-boundary Benders certificate
(\texttt{scratch/h29cube\_exact\_benders8.json}) closes the relevant
(691)-bit two-parent relabel cube: it is Hall0-UNSAT even though one DM shore
can be given large slack. The fixed segmentation lane is also closed in the
stated audited families. Nothing below weakens either conclusion.

## 2. Head-transfer normal form

Write

\[
 f_a:\Omega\longrightarrow\Omega
\tag{2.1}
\]

for the successor permutation of closed parent (H_a), and use

\[
                         f_0=f_{29}
\tag{2.2}
\]

as base. Put

\[
 \rho_a=f_0^{-1}\circ f_a,
 \qquad
 R(x)=\{\rho_a(x):a\in\{29,30,31,\tau\}\}.
\tag{2.3}
\]

Here (\rho_{29}=\mathrm{id}). Repeated arcs cause no ambiguity: (R(x))
is a set of possible transferred heads, not a set of colour labels.

### Theorem 2.1 (exact multi-parent factor normal form)

A directed arc selection from the four-parent union has indegree and
outdegree one at every vertex of (\Omega) if and only if it is uniquely of
the form

\[
                         f=f_0\circ p,
\tag{2.4}
\]

where (p\in S_\Omega) is a permutation satisfying

\[
                         p(x)\in R(x)
 \qquad(x\in\Omega).
\tag{2.5}
\]

If

\[
                         C=(x_1\ x_2\ \cdots\ x_s)
\tag{2.6}
\]

is a nontrivial cycle of (p), then its trade deletes

\[
                         x_i\longrightarrow f_0(x_i)
\tag{2.7}
\]

and inserts

\[
                         x_i\longrightarrow f_0(x_{i+1})
 \qquad(i\bmod s).
\tag{2.8}
\]

Thus (C) is exactly an alternating (C_{2s}) in the bipartite
tail--head overlay.

#### Proof

Let (f) be a selected one-factor. Define

\[
                         p=f_0^{-1}\circ f.
\tag{2.9}
\]

Because (f_0) and (f) are bijections, (p) is a permutation. If the arc
out of (x) comes from parent (a), then

\[
 p(x)=f_0^{-1}(f_a(x))=\rho_a(x),
\]

which proves (2.5). Conversely, if (p) is a permutation obeying (2.5),
then every arc (x\to f_0(p(x))) belongs to at least one parent row, and
(f_0\circ p) is a bijection. This is precisely degree one at both shores.
The cycle description follows by substituting (2.6) into (2.4). (\square)

Theorem 2.1 preserves literal middle ownership. Hamilton connectivity,
residence, and upper coverage are additional conditions; degree balance alone
does not imply them.

### Corollary 2.2 (exact forced-arc completion test)

A forced arc family (F) extends to a degree-exact factor in the four-parent
catalogue if and only if (F) is a partial bipartite matching and the
remaining parent-union bipartite graph, after deleting the used tails and
heads, satisfies Hall's inequalities.

#### Proof

After the forced rows and columns are deleted, a completion is exactly a
perfect matching of the residual bipartite graph. Apply Hall's theorem.
(\square)

Hamiltonity is still the one-cycle condition below. This corollary explains
why a collection of attractive compiler motifs may have abundant individual
arcs but fail exact factor consistency.

## 3. Two-parent rigidity and rainbow trades

Fix one nonbase parent (H_1), and write

\[
                         \rho=f_0^{-1}f_1.
\tag{3.1}
\]

A two-parent selection has (p(x)\in\{x,\rho(x)\}). Let (b_x=0) or (1)
record these two choices.

### Theorem 3.1 (two-parent shore rigidity)

The map (p) is a permutation if and only if (b_x) is constant on every
cycle of (\rho). Hence every exact two-parent factor is obtained by choosing
one entire shore on each alternating assignment component.

#### Proof

For a head (y), the two possible preimages are its base row (y) and the
previous row (\rho^{-1}(y)) on the assignment cycle. Its indegree is

\[
                         1-b_y+b_{\rho^{-1}(y)}.
\tag{3.2}
\]

This equals one exactly when

\[
                         b_y=b_{\rho^{-1}(y)}.
\tag{3.3}
\]

Propagation around every (\rho)-cycle proves constancy. Constant choices
obviously give a bijection. (\square)

This proves abstractly that no fractional or partially switched two-parent
component was omitted from the audited Boolean cube.

### Definition 3.2 (parent-pure and rainbow transfer cycles)

A nontrivial cycle (C) of (p) is **parent-pure** if one parent (a)
supplies its whole replacement shore:

\[
                         p|_C=\rho_a|_C.
\tag{3.4}
\]

It is **rainbow** otherwise.

If (3.4) holds, (C) is an invariant cycle of (\rho_a), hence is exactly a
whole two-parent assignment component. Conversely every whole assignment
component is parent-pure. Thus rainbow cycles, rather than the mere use of
several parent names in different components, are the intrinsic
non-row-power objects.

In particular, three source parents are algebraically minimal for a genuine
non-row-power cycle.

## 4. Exact Hamilton monodromy

Let

\[
 S=\operatorname{supp}p=\{x_1,\ldots,x_s\}
\tag{4.1}
\]

be indexed in their cyclic order on the base cycle (f_0), and put

\[
 y_i=f_0(x_i),\qquad \rho=(1\ 2\ \cdots\ s).
\tag{4.2}
\]

Write (\pi\in S_s) for the restriction of (p), so that the new seam out
of (x_i) is

\[
                         x_i\longrightarrow y_{\pi(i)}.
\tag{4.3}
\]

Since (S) is the support, (\pi) has no fixed point.

### Theorem 4.1 (cut-permutation composition formula)

After the seams (4.3) are inserted, the number of directed carrier
components is

\[
                         c(\pi\rho),
\tag{4.4}
\]

the number of cycles of the permutation (\pi\rho). Consequently the child
is one Hamilton cycle if and only if

\[
                         \pi\rho\text{ is one cycle}.
\tag{4.5}
\]

#### Proof

Deleting the base arcs (x_i\to y_i) leaves (s) directed segments. Segment
(i) starts at (y_i), follows the base cycle, and ends at (x_{i+1}).
The new seam out of that endpoint goes to

\[
 x_{i+1}\longrightarrow y_{\pi(i+1)}.
\]

Thus traversal sends segment index (i) to

\[
                         \pi(\rho(i)).
\]

Contracting each unchanged segment proves (4.4) and (4.5). (\square)

This is the exact global composition condition missing from a collection of
independently legal alternating circuits.

### Corollary 4.2 (parity and the minimal atom)

Every Hamilton transfer (p) is even. No nontrivial Hamilton trade has
support one or two. On three support points, exactly the forward 3-cycle

\[
                         \pi=\rho
\tag{4.6}
\]

is Hamilton; the reverse 3-cycle gives three components.

#### Proof

Both (f_0) and (f_0p) are cycles of the same length, so they have the
same sign. Hence (\operatorname{sgn}p=+1). Support one is impossible for a
permutation. Support two forces one transposition; it is odd, and directly
(\pi=\rho=(12)) gives (\pi\rho=\mathrm{id}), namely two components.

For (s=3), the two fixed-point-free even permutations are (\rho) and
(\rho^{-1}). The first gives (\rho^2), one cycle, while the second gives
the identity. (\square)

Therefore (0.3), provided its three alternate arcs are available and no
single donor supplies all of them, is the support-minimal non-row-power
Hamilton trade.

More generally, if the nontrivial cycles of (p) have lengths
(\ell_1,\ldots,\ell_t), then

\[
                         \sum_j(\ell_j-1)\equiv0\pmod2.
\tag{4.7}
\]

Thus a single alternating (C_{2\ell}) can be Hamilton only for odd
(\ell). Even transfer cycles must occur in an even number and be globally
interlaced in a way satisfying (4.5).

### Corollary 4.3 (circulant library)

For (\pi=\rho^a),

\[
                         c(\pi\rho)=\gcd(s,a+1).
\tag{4.8}
\]

Hence this trade is Hamilton exactly when

\[
                         \gcd(s,a+1)=1.
\tag{4.9}
\]

#### Proof

Here (\pi\rho=\rho^{a+1}), whose cycles are the residue classes modulo
(\gcd(s,a+1)). (\square)

The first examples are:

\[
\begin{array}{c|c|c}
s&a&\text{trade}\\ \hline
3&1&\text{one forward rainbow }C_6,\\
4&2&\text{two crossing }C_4\text{ shores whose union is Hamilton},\\
5&1&\text{one forward }C_{10},\\
6&4&\text{two interlaced }C_6\text{ shores}.
\end{array}
\tag{4.10}
\]

### Corollary 4.4 (composition of consecutive odd blocks)

Partition the cut order into consecutive blocks of odd sizes
(\ell_j\ge3). On every block choose its forward cyclic transfer, and let
(\pi) be the product of these disjoint cycles. Then (\pi\rho) is one
cycle.

#### Proof

Label a block (0,1,\ldots,\ell-1). Away from a block boundary,
(\pi\rho) advances by two. Starting at (0) in the first block, traversal
visits its even positions through (\ell-1), then enters position (1) of
the next block. In each later block it visits all odd positions, then (0),
then all positive even positions, and exits to position (1) of the next
block. After the last block it visits the odd positions of the first block
and returns to its (0). Every cut index appears exactly once. (\square)

Corollaries 4.3--4.4 give a deterministic library of globally composable
longer carriers. Availability of their seams in the four-parent catalogue
and the resource conditions below remain substantive requirements.

## 5. The exact external-router toll for a partial relabel shore

The new parent (H_\tau) has useful parent-pure compiler material. Taking
whole (H_{29}/H_\tau) assignment components, however, returns to a
two-parent row-power cube. The following identity quantifies the price of
taking only part of such a component.

Index one alternating component so that

\[
 e_i:x_i\to y_i\quad\text{is an }H_{29}\text{ arc},
 \qquad
 g_i:x_i\to y_{i+1}\quad\text{is an }H_\tau\text{ arc}.
\tag{5.1}
\]

Let (b_i=0) choose (e_i) and (b_i=1) choose (g_i). A **router completion**
of this tentative word may replace some prescribed rows by outside-parent
arcs, but on every nonrouter row it retains the displayed (e_i/g_i) choice.

### Lemma 5.1 (run-boundary defect identity)

The tentative indegree of head (y_i) is

\[
                         d^-(y_i)=1-b_i+b_{i-1}.
\tag{5.2}
\]

Consequently every cyclic transition (0\to1) creates one missing head,
every transition (1\to0) creates one double head, and a binary word with
(r) proper 1-runs has exactly (r) of each.

#### Proof

Head (y_i) receives its base arc precisely when (b_i=0), and receives
the previous relabel arc precisely when (b_{i-1}=1). This gives (5.2).
The transition claims follow immediately. The two types alternate on a
cyclic binary word and hence have equal cardinality. (\square)

### Corollary 5.2 (one outside-parent router per proper run)

Any exact router completion of such a partial shore needs at least (r)
chosen arcs outside the two displayed shores.

#### Proof

On a nonrouter row the tentative base/relabel choice is frozen, so every
missing head in Lemma 5.1 must receive an outside-parent arc. One such arc
has only one head and can repair at most one missing boundary. (\square)

An outside arc may be tight: it can redirect a row formerly contributing to
a double head into the paired hole. A proper relabel run of length (L), plus
one tight router, closes a transfer cycle on (L+1) tails. It is a two-tail
rectangle only for (L=1), and it is a degree-exact (C_6) for (L=2).
Corollary 4.2 says that the rectangle splits the closed carrier; the (C_6)
is Hamilton only when its three tails have the forward physical base order.
Thus the global support-minimal Hamilton repair remains a mixed forward
(C_6), but this is not an automatic repair theorem for an arbitrary run.

This is only a degree/router theorem. Assignment-component order is not
physical chronology. A desired (H_\tau)-pure compiler word may cross several
assignment components, and a run of assignment bits is not automatically a
consecutive (H_\tau) word or residence-safe. Literal motif arcs must be
forced first; Lemma 5.1 then gives the componentwise router toll.

## 6. Exact bounded-window resource composition

The (k=15) predicates have the following audited locality.

- Residence three forbids a coordinate inserted on one edge from being
  removed within the next three edges. Every test uses at most four
  consecutive directed arcs.
- An upper-(q) witness is the OR of (q+1) consecutive middle vertices,
  for (1\le q\le7).
- A lower compiler cell of depth (d\in\{0,1,2\}) is determined by a word of
  exactly (d+10) consecutive middle vertices.

Delete the base arcs at (x_1,\ldots,x_s), producing the unchanged directed
segments used in Theorem 4.1. Assume first that every old and new seam has a
full twelve-vertex collar and no bounded test window meets two seams. This is
the **separated** case.

For an upper target (U) of depth (q), let (I_{q,U}) be the number of
witnesses wholly internal to the unchanged segments, and let

\[
                         u_{q,U}(i,j)
\tag{6.1}
\]

be the number of its witnesses crossing the candidate seam (x_i\to y_j).
Let (\Phi(i,j)) be the multiset of exact compiler-cell fibre signatures
crossing that seam. It retains the complete target adjacency of every
physical cell, not merely a scalar target count.

### Theorem 6.1 (literal separated-seam ledger)

For every available seam permutation (\pi) satisfying (4.5),

\[
 n_{q,U}(f_0p)
 =I_{q,U}+\sum_{i=1}^{s}u_{q,U}(i,\pi(i)),
\tag{6.2}
\]

and the exact lower compiler graph is the disjoint physical-cell union

\[
 G(f_0p)=G_{\rm int}\;\dot\cup\;
          \bigdotcup_{i=1}^{s}\Phi(i,\pi(i)).
\tag{6.3}
\]

The child is residence-safe if and only if every residence window crossing
one of the chosen seams is safe.

#### Proof

Every local window is either wholly within one unchanged segment or crosses
a seam. In the first case its ordered middle word is identical to its base
word and is counted in the internal term. In the separated case a window
cannot cross two seams, so the second class partitions uniquely by its seam.
This proves (6.2) and (6.3). The base segment interiors have zero residence
defects, so any new defect must lie in the second class. (\square)

Subtracting the base ledger gives the exact signed upper identity

\[
 n_{q,U}(f_0p)-n_{q,U}(f_0)
 =\sum_i\bigl(u_{q,U}(i,\pi(i))-u_{q,U}(i,i)\bigr).
\tag{6.4}
\]

Thus all-upper preservation is the family of literal inequalities

\[
                         n_{q,U}(f_0p)\ge1
\tag{6.5}
\]

for every upper target (U), not equality of an aggregate histogram.

For a fixed lower target family (A), define the collar hit count

\[
 a_A(i,j)=
 \bigl|\{C\in\Phi(i,j):N(C)\cap A\ne\varnothing\}\bigr|.
\tag{6.5a}
\]

Because physical cells, rather than target--cell incidences, are being
counted, (6.3) gives the exact compiler-neighbourhood identity

\[
 h_A(f_0p)-h_A(f_0)
 =\sum_i\bigl(a_A(i,\pi(i))-a_A(i,i)\bigr).
\tag{6.5b}
\]

This is the statewise quantity a separated trade must improve. Parent-level
values such as (1.8) cannot be substituted for the right-hand side of
(6.5b).

### Corollary 6.2 (exact collar sizes)

One full interior changed seam has:

\[
 \sum_{q=1}^{7}q=28
\tag{6.6}
\]

upper windows crossing it, and at depth (d) it has (d+9) compiler-cell slots
whose (d+10)-vertex word crosses it. Hence it replaces at most

\[
                         9+10+11=30
\tag{6.7}
\]

compiler cells. Residence needs only the crossing windows of arc lengths
(2,3,4), at most

\[
                         2+3+4=9
\tag{6.8}
\]

window positions. Therefore a separated forward (C_6) has one-sided collar
budgets

\[
                         27,\qquad84,\qquad90
\tag{6.9}
\]

for residence-test windows, upper windows, and compiler cells.

These are one-shore counts. In a before/after comparison, the old shore has
up to (9,28,30) removed occurrence records per seam and the new shore has up
to (9,28,30) added records. Thus the symmetric ledgers can contain as many as
(18,56,60) records per seam. Calling (30), or (90) for a (C_6), a “change”
is valid only after pairing old and new collar slots by their seam offsets;
the raw destroyed and new cell families each have that size separately.

If seams are closer, join all seams at distance at most the dependency radius
into one cluster. The proof of Theorem 6.1 then applies clusterwise: internal
windows plus exact cluster signatures still partition all occurrences.
What fails is only the unjustified sum of one-seam marginals.

Boundary changes are handled by including the exact thirty-six endpoint
compiler indicators in the cluster containing (\partial). Let
(t_0=f_0^{-1}(\partial)) be the base terminal. Fixing (p(\partial)=\partial)
keeps the source, but the new terminal is (p^{-1}(t_0)); therefore both
(\partial) and (t_0) must lie outside the transfer support to preserve the
entire endpoint palette without a fresh boundary audit.

## 7. A no-relocation compiler-matching theorem

For a path (P), let

\[
                         G(P)=(\mathcal T,\mathcal C(P);E(P))
\tag{7.1}
\]

be its exact lower compiler graph. Let (J) be a maximum matching of
(G(H_{29})), so

\[
                         |J|=16354.
\tag{7.2}
\]

For a trade (H_{29}\to P), let (D_0\subseteq\mathcal C(H_{29})) be the
old cells in the affected seam clusters. Every cell outside (D_0) lies
inside an unchanged segment and has a canonical transported occurrence in
(\mathcal C(P)) with exactly the same target neighbourhood. Transport all
edges of (J) whose cell is outside (D_0); call the resulting matching
(J_{\rm keep}).

Put

\[
 X=\mathcal T\setminus V_{\mathcal T}(J_{\rm keep}),
 \qquad
 Y=\mathcal C(P)\setminus V_{\mathcal C}(J_{\rm keep}),
\tag{7.3}
\]

and let (K_P=G(P)[X,Y]).

### Theorem 7.1 (protected exchange-rank criterion)

Among matchings of (G(P)) that retain (J_{\rm keep}), the maximum size is

\[
                         |J_{\rm keep}|+\nu(K_P).
\tag{7.4}
\]

Consequently the protected gain

\[
 g_J(P)=|J_{\rm keep}|+\nu(K_P)-|J|
\tag{7.5}
\]

has the exact implication

\[
                         \operatorname{def}(P)
 \le 29-g_J(P).
\tag{7.6}
\]

In particular, (g_J(P)\ge1) proves Hall (29\to28) or better, and
(g_J(P)=29) proves Hall zero.

#### Proof

After (J_{\rm keep}) is frozen, its target and cell vertices cannot be used
again. Every remaining compatible matching is therefore exactly a matching
of (K_P), and conversely every matching of (K_P) can be adjoined to
(J_{\rm keep}). This proves (7.4). The unrestricted maximum matching of
(G(P)) is at least this large, so

\[
 \operatorname{def}(P)
 \le16383-(|J|+g_J(P))=29-g_J(P).
\]

(\square)

This criterion allows all necessary rematching inside affected collars. A
simpler sufficient form is: rematch every target whose old (J)-cell was
destroyed and also match (r) formerly unmatched targets into distinct new
cells. Then (g_J(P)\ge r).

### Corollary 7.2 (direct-sum augmentation)

Suppose available separated trade blocks have disjoint changed cell sets,
their seam permutation satisfies the global Hamilton condition (4.5), their
endpoint treatment is valid as in Section 6, and their residence and upper
ledgers are legal. For block (i), let (T_i) be the targets whose (J)-cells
it destroys, and choose pairwise disjoint sets (U_i) of formerly unmatched
targets. If the new collar of block (i) has a matching covering
(T_i\cup U_i), then the composed carrier has a compiler matching of size

\[
                         16354+\sum_i|U_i|.
\tag{7.7}
\]

#### Proof

Retain the edges of (J) on every unaffected cell, delete its collar edges,
and insert the assumed local matchings. Their cell sets and target sets are
disjoint, so their union is a matching. Its size is the old size plus the
newly covered targets. (\square)

Equivalently, the new collars must create vertex-disjoint (J)-augmenting
paths in the DM alternating digraph. The protected matching statement is the
correct meaning of “without relocation.” Merely increasing
(h_A(P)=|N_P(A)|) for one frozen shore (A) does not imply (7.6).

For a separated forward (C_6), at most ninety old compiler cells are
destroyed and at most ninety new collar cells are supplied; these are ninety
paired slot updates but up to 180 symmetric occurrence records. Thus a
one-atom Hall-zero repair is not ruled out by its ninety-cell new capacity,
but it must realize protected gain (29). At minimum it must change the
canonical shore by

\[
 h_{A_{29}}(P)-1495\ge29
\tag{7.8}
\]

to reach Hall zero; a gain of one is necessary merely to lower the canonical
Hall lower bound from (29). Neither inequality is sufficient without
Theorem 7.1.

## 8. Audit of the fourth-parent capacity

The compiler is coordinate-equivariant:

\[
                         h_{\gamma A}(\gamma P)=h_A(P)
\tag{8.1}
\]

for every coordinate permutation (\gamma). Put

\[
                         A_\tau=\tau A_{29}.
\tag{8.2}
\]

Because (\tau) is an involution, (1.4), (1.8), and (8.1) give the exact
cross matrix

\[
\begin{array}{c|cc}
 &H_{29}&H_\tau\\ \hline
A_{29}&1495&1616\\
A_\tau&1616&1495.
\end{array}
\tag{8.3}
\]

Both target shores have size (1524). In particular, each parent has (92)
cells of slack on the other parent's private obstruction, but deficiency
(29) on its own. The formal half-mixture has positive margin on both rows;
the integral factor problem is to realize both advantages coherently. The
large (A_{29}) value of (H_\tau) by itself is exactly a relocation, not an
improvement.

Likewise, (1.7) proves only singleton fibre supply. Several targets can be
adjacent to the same physical compiler cell. To certify even the seven-target
subproblem one must verify Hall for every subset of (\mathcal Z), or exhibit
a seven-edge target--cell matching. It still would not settle the remaining
16376 targets.

The diagnostic three-parent tuple in
(\texttt{scratch/k15\_h29\_zero7\_minimal\_tuple.json}) illustrates the
gap sharply. It supplies an individual motif for every target in
(\mathcal Z) with only four non-(H_{29}) arcs, but the combined forced set
activates twenty-three residence-forbidden motifs. Therefore motif abundance
and low arc novelty are not factor-consistency or chronology certificates.

Any serious finite audit of the four-parent family must include at least

\[
 A_{29},\quad A_\tau,
\tag{8.4}
\]

the private DM blocks of the other parents, the observed relocation shores
(R_3,R_4), and an exact global compiler matching. Passing the fixed shores
is only a filter; Theorem 7.1 or a direct larger matching is the certificate.

## 9. What family is minimally capable?

The previous theorems give an exact answer in three increasingly strong
senses.

### 9.1 Algebraic escape

The two-parent exact-factor space consists only of whole shores. To leave it,
one needs a rainbow cycle, so at least three parent colours are necessary.

### 9.2 Literal Hamilton escape

A rectangle on two changed tails is degree-exact but splits the carrier. The
support-minimal literal Hamilton escape is a forward rainbow (C_6) satisfying
all three conditions:

\[
\begin{array}{ll}
\text{availability:}&x_i\to f_0(x_{i+1})
   \text{ belongs to the expanded parent union};\\
\text{rainbow:}&\text{no one donor parent supplies the whole alternate shore};\\
\text{chronology:}&x_1,x_2,x_3\text{ occur in that order on }H_{29}.
\end{array}
\tag{9.1}
\]

Longer positive odd cycles and the interlaced even-cycle decks of Section 4
are the complete next library, with Hamiltonity decided exactly by (4.5).

### 9.3 Deficiency-reducing escape

A sufficient, statewise certificate that an available rainbow cycle makes
genuine progress is that it also satisfies:

1. every crossing residence window is legal;
2. the inequalities (6.5) hold for every upper target at every
   (q=1,\ldots,7); and
3. its protected exchange rank (7.5) is positive.

These conditions produce an actual resident, all-upper Hamilton parent with
strictly larger compiler matching. They cannot merely transfer the canonical
DM label. They are not necessary: a larger matching may require alternating
rematching through some otherwise unaffected edges of (J). The necessary
and sufficient final test is the unrestricted inequality
(\nu(G(P))>|J|). A deck with protected gain (29) completes the Hall part of
the (k=15) construction.

The four-parent data prove that the raw donor and fibre supply needed for such
a deck exists at parent level. They do not yet prove that one forward (C_6),
one longer rainbow cycle, or a composable deck satisfies all three statewise
conditions.

## 10. Relation to the closed segmentation lane

A sparse, separated rainbow (C_6) is the minimal algebraic atom, not a claim
that an already exhausted fixed H30 segmentation has been reopened. A
particular short atom may lie inside one of those closed atlases. Moreover,
the compiler-neighbourhood subadditivity theorem still applies whenever one
only cuts fixed factorable pieces and reconnects them.

The genuinely new candidate is therefore one of the following.

1. A long rainbow transfer cycle using arcs from (H_{31}) or (H_\tau)
   outside the closed two-parent/fixed-segment catalogues.
2. An interlaced cycle deck whose individual rectangles would split but whose
   global monodromy is one cycle, as in (4.10).
3. A dense cluster of partial (H_\tau) shores with the exact external-router
   toll of Lemma 5.1, audited by a cluster compiler graph rather than by
   independent seam marginals.

The head-transfer normal form and the protected matching theorem apply to all
three. Only the convenient (30s)-cell direct sum must be replaced by exact
radius-eleven cluster signatures when supports are dense.

## 11. Proved/conditional boundary

The following statements are proved in this note.

- The head-transfer permutation parametrizes every exact one-factor in the
  four-parent directed union.
- Two-parent shore rigidity is exact.
- Rainbow cycles are precisely the genuinely non-row-power primitive trades.
- The cut-permutation formula (4.4) is necessary and sufficient for Hamilton
  connectivity.
- The forward rainbow (C_6) is support-minimal; odd-block and circulant
  composition give explicit larger Hamilton libraries.
- Partial relabel shores pay one outside-parent router per proper run.
- The bounded-window resource ledgers and collar sizes are exact.
- The protected exchange-rank criterion proves deficiency reduction without
  DM relocation.
- The (H_{29}/H_\tau) cross-DM matrix (8.3) exposes the private obstruction
  omitted by a one-sided parent screen.

The following statement remains open.

> Does the (19751)-arc union of
> (H_{29},H_{30},H_{31},(1\ 12)H_{29}) contain a rainbow transfer cycle or
> cycle deck satisfying residence, all upper targets, and protected exchange
> gain at least one (ideally twenty-nine)?

This is the first precisely formulated candidate enlarged gate aimed outside
both the Hall0-UNSAT two-parent cube and the closed fixed-segmentation lane.
No admissible rainbow trade outside those atlases, and no (k=15) optimum, is
claimed here.

## 12. Independent proof audit

An independent adversarial audit checked the composition order in (2.4),
the monodromy formula (4.4), the parity/minimal-(C_6) conclusion, the
odd-block and circulant calculations, and the conjugacy matrix (8.3); no
correction was required to those statements. The audit did require, and the
present text incorporates, four scope repairs: collar counts are one-sided,
both endpoint-defining tails must be fixed to inherit the old boundary
palette, a router closes an arbitrary length-(L) run on (L+1) tails, and
positive protected exchange rank is sufficient rather than necessary for an
unrestricted matching improvement.
