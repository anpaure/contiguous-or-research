# Lane L: residence-safe compiler motifs and the two-level Hall condition at \(k=15\)

Date: 2026-07-28

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  Thus `[1,12]_0=(2,13)_1` and
`[5,7]_0=(6,8)_1`.

Method: exact finite mathematics on the directed parent catalogue. The
computational artifacts cited below are used only as frozen finite witnesses;
all implication statements are proved here.

## 0. Outcome

Let

\[
 V=\binom{[15]}8,\qquad |V|=6435,
\tag{0.1}
\]

and let \(D=(V,E)\) be a directed parent catalogue: every arc of \(E\)
is a directed consecutive pair from one of the selected parent Hamilton
paths. Fix a deficient lower-target family \(A\). The two cases of
current interest are

\[
 Z_7=\{2575,5801,13616,13620,17738,21641,29776\}
\tag{0.2}
\]

and the canonical Hall-29 DM family \(A_{29}\), for which

\[
 |A_{29}|=1524,\qquad |N_{P_{29}}(A_{29})|=1495.
\tag{0.3}
\]

Thus its exact deficiency is \(29\).

The conclusions are as follows.

1. A local compiler motif is not merely a target label and an arc tuple.
   It consists of one physical compiler cell (or one complete boundary
   palette), the directed local parent word realizing it, its required
   arcs, its adjacent targets in \(A\), and a possible global endpoint
   flag. Interior depth \(r\in\{0,1,2\}\) uses \(r+10\) consecutive
   middle vertices. A boundary motif uses an oriented 12-vertex prefix
   or suffix.

2. Interactions between motifs have four exact layers: directed degree
   conflicts, directed cycles, depth-three residence conflicts,
   and competition for distinct physical compiler cells. The residence
   layer is a hypergraph of rank at most four. Individual residence
   safety of every motif is not enough.

3. Let \(\mathcal M\) be selected motifs and \(\mathcal C(\mathcal M)\)
   their exposed physical cells. The exact compiler-installation
   condition is

   \[
   \boxed{
   |N_{\mathcal C(\mathcal M)}(B)|\ge |B|
   \qquad(B\subseteq A).}
   \tag{0.4}
   \]

   This is Hall on physical cells, not motif records. For \(Z_7\) it
   has \(127\) nonempty inequalities; for \(A_{29}\) it is equivalently
   a matching of size \(1524\).

4. Condition (0.4) is only the compiler Hall layer. A simultaneous
   residence-safe chronology exists exactly when the forced arcs form a
   residence-safe path forest and the contracted fragments have a port
   perfect matching whose fragment graph is connected and whose complete
   arc union remains residence-safe.

5. There is a genuine Hall-style sufficient form. If the residual seam
   graph can be restricted to a subgraph which increases one fixed
   fragment potential, can never complete a forbidden residence word,
   and satisfies port Hall, then a residence-safe spanning chronology
   exists automatically. Together with (0.4), this installs all targets.

6. The frozen seven-target 60-arc tuple is decisively rejected. It has

   \[
   \begin{array}{c|c}
   \text{target records}&7\\
   \text{distinct required-arc patterns}&6\\
   \text{unique selected arcs}&60\\
   \text{arcs outside the Hall-29 parent}&4\\
   \text{selected forbidden residence motifs}&23.
   \end{array}
   \tag{0.5}
   \]

   It covers every label in \(Z_7\) and is degree/cycle compatible, but
   it cannot lie in any residence-safe chronology. In fact the motifs
   for \(13616,13620,17738,29776\) already contain respectively
   \(7,4,6,6\) selected forbidden clauses; the other three target
   records contain none. Removing clause supersets leaves six minimal
   residence cores, distributed \(2,2,1,1\). All are forced.

7. Installing the seven zero targets is necessary but not sufficient
   for repairing \(A_{29}\). The correct full condition is

   \[
   \boxed{
   |N_0(B)\cup N_{\mathcal C(\mathcal M)}(B)|
      \ge |B|
   \qquad(B\subseteq A_{29}),}
   \tag{0.6}
   \]

   where \(N_0\) is the current Hall-29 compiler neighbourhood. A repair
   may give all seven zero targets neighbours and move the DM deficiency
   to another subset.

8. For the concrete directed catalogue

   \[
   D_4=H_{29}\cup H_{30}\cup H_{31}\cup\tau_{(1,12)}H_{29},
   \tag{0.7}
   \]

   the seven-target gate is closed. There is an explicit transversal of
   seven pairwise arc-disjoint, residence-safe interior motifs on
   \(\tau_{(1,12)}H_{29}\). Their seven physical cells are distinct and
   give a diagonal Hall matching. The unused arcs of that same parent
   give an ordered residence-closed port perfect matching.

9. The analogous twelve-target gate is closed in

   \[
   D_5=D_4\cup\tau_{(5,7)}H_{29}.
   \tag{0.8}
   \]

   An explicit transversal of twelve pairwise arc-disjoint interior
   motifs lies on \(\tau_{(5,7)}H_{29}\), and its unused parent arcs again
   give the port matching. The forced-arc counts are respectively
   \(74\) and \(128\), leaving \(6361\) and \(6307\) contracted
   fragments.

Thus the frozen four/five-parent catalogues settle the local
seven/twelve-zero residence/physical-cell/port gate. They do **not** settle
the full \(A_{29}\) matching gate: a coordinate-transposed Hall-29 parent
is isomorphic to Hall 29 and still has a (transposed) deficiency-29 block.
Covering the named zero targets can move, rather than remove, the global
deficiency.

## 1. Directed residence as a rank-four forbidden system

For a directed path

\[
                         v_0\to v_1\to\cdots\to v_s
\tag{1.1}
\]

and coordinate \(x\), say that \(x\) is inserted on the first arc if

\[
                         x\in v_1\setminus v_0.
\tag{1.2}
\]

It violates depth-three residence if, for some \(1\le j\le3\),

\[
                         x\in v_j\setminus v_{j+1}.
\tag{1.3}
\]

The witnessing selected-arc set is

\[
 \{v_0v_1,v_1v_2,\ldots,v_jv_{j+1}\},
\tag{1.4}
\]

of size \(j+1\in\{2,3,4\}\). Let
\(\mathcal F_{\rm res}(D)\) be the family of all minimal arc sets of
this form in the directed catalogue.

### Lemma 1.1 (exact residence closure)

For any selected arc set \(R\subseteq E\) whose indegrees and outdegrees
are at most one, the induced directed path components are depth-three
residence-safe if and only if

\[
                         F\nsubseteq R
 \qquad(F\in\mathcal F_{\rm res}(D)).
\tag{1.5}
\]

#### Proof

If \(F\subseteq R\), the degree bounds force its arcs to occur
consecutively in one component, giving (1.2)--(1.3). Conversely every
violation has a first inserted coordinate and a first removal at delay
at most three; its consecutive arc set contains a minimal member of
\(\mathcal F_{\rm res}(D)\). \(\square\)

Residence is therefore exactly a rank-four forbidden hypergraph on
selected arcs, not a scalar score or merely a pairwise conflict graph.

## 2. Physical compiler motifs

Fix \(A\). A physical compiler cell \(c\) is one of the actual
depth-three cells determined by a local middle word. Write

\[
                         \Gamma_A(c)\subseteq A
\tag{2.1}
\]

for its exact adjacent targets under the envelope, erosion-mask, and
mandatory-carrier rules.

### Definition 2.1 (directed local motif)

A directed local compiler motif is

\[
                         M=(W_M,R_M,C_M,\epsilon_M),
\tag{2.2}
\]

where \(W_M\) is a simple directed local word in \(D\), \(R_M\) its
consecutive arcs, \(C_M\) the physical cells it exposes, and
\(\epsilon_M\in\{\varnothing,L,R\}\) a possible global endpoint flag.
Every cell retains its exact incidence \(\Gamma_A(c)\).

For interior depth \(r=0,1,2\), \(W_M\) has \(r+10\) vertices and one
designated internal cell. For a boundary motif it has 12 vertices and
\(C_M\) is the complete oriented boundary palette. The motif is locally
residence-safe when \(R_M\) contains no member of
\(\mathcal F_{\rm res}(D)\).

The distinction between \(R_M\) and \(C_M\) is essential. Two target
records may require the same arc word but use different cells in one
boundary palette; different arc words may also expose the same cell.
Hall counts cells, while residence counts arcs.

## 3. Exact interaction across motifs

For a motif family \(\mathcal M\), put

\[
 R(\mathcal M)=\bigcup_{M\in\mathcal M}R_M,
 \qquad
 C(\mathcal M)=\bigcup_{M\in\mathcal M}C_M.
\tag{3.1}
\]

Call \(\mathcal M\) internally compatible if:

1. no vertex has two different forced outgoing arcs or two different
   forced incoming arcs;
2. \(R(\mathcal M)\) contains no directed cycle;
3. at most one motif is flagged \(L\), at most one is flagged \(R\);
   an \(L\)-flagged word begins its forced fragment and an \(R\)-flagged
   word ends its forced fragment; and overlapping flags agree; and
4. \(F\nsubseteq R(\mathcal M)\) for every
   \(F\in\mathcal F_{\rm res}(D)\).

### Proposition 3.1 (complete local interaction list)

The forced union of \(\mathcal M\) is a residence-safe directed path
forest with consistent boundary flags if and only if \(\mathcal M\) is
internally compatible.

#### Proof

Items 1--2 characterize a directed path forest, item 3 is boundary
consistency, and Lemma 1.1 makes item 4 equivalent to residence safety.
\(\square\)

At motif level, every residence obstruction has a minimal cover by at
most four motifs: choose one motif supplying each of its at most four
arcs and remove redundant choices. Thus cross-motif residence interaction
has rank at most four, although proper-cycle conflicts may be longer.

For every \(F\in\mathcal F_{\rm res}(D)\), add the clause

\[
              \bigvee_{M\in J_F}\neg z_M
\tag{3.2}
\]

for every minimal motif cover \(J_F\) of \(F\). No larger residence
clause is needed at depth three.

## 4. The compiler Hall layer

Build a bipartite graph \(H_A(\mathcal M)\) with left side \(A\), right
side the distinct cells \(C(\mathcal M)\), and edge \(Xc\) when
\(X\in\Gamma_A(c)\).

### Theorem 4.1 (physical-cell Hall)

The selected motifs supply pairwise distinct compiler cells to every
target in \(A\) if and only if

\[
 |N_{H_A(\mathcal M)}(B)|\ge |B|
 \qquad(B\subseteq A).
\tag{4.1}
\]

#### Proof

This is Hall's marriage theorem on the target--physical-cell graph.
\(\square\)

For \(A=Z_7\), this is stronger than one motif record per target: two
records may refer to one cell. It is weaker than seven arc-disjoint
motifs because one boundary word may expose several distinct cells.

For \(A_{29}\), let \(C_0\) be the current cells. Full repair is Hall on
\(C_0\cup C(\mathcal M)\), exactly (0.6). At least 29 genuinely new
cells are necessary by (0.3), but total neighbourhood size 1524 alone
does not imply the subset inequalities.

## 5. Exact chronology extension after motifs are fixed

Let \(\mathcal M\) be internally compatible. Include every isolated
vertex as a length-zero fragment and let \(\mathcal P(\mathcal M)\) be
the resulting partition of \(V\) into directed fragments. Each fragment
has one entry and one exit port.

Fix proposed global start and end fragments \(s,t\), respecting motif
flags. Form the bipartite port graph \(B_{\mathcal M}(s,t)\): its left
side is the exits of all fragments except \(t\), its right side the
entries of all fragments except \(s\), and an edge between two distinct
fragments is present when the catalogue contains the corresponding
directed seam.

### Theorem 5.1 (exact motif-extension criterion)

There is a residence-safe Hamilton path in \(D\) containing every forced
arc and respecting all flags if and only if there are \(s,t\) and a
perfect matching

\[
                         J\subseteq B_{\mathcal M}(s,t)
\tag{5.1}
\]

such that:

1. the selected directed fragment graph is connected; and
2. \(R(\mathcal M)\cup J\) contains no member of
   \(\mathcal F_{\rm res}(D)\).

#### Proof

A Hamilton path uses one outgoing seam from every fragment except its
last and one incoming seam to every fragment except its first, yielding
the perfect matching. Its contraction is connected, and Lemma 1.1 gives
item 2.

Conversely the matching gives every non-start fragment indegree one and
every non-end fragment outdegree one. Each component is a directed path
or cycle. Connectedness leaves one spanning path; item 2 and Lemma 1.1
make it residence-safe. \(\square\)

The ordinary port Hall inequalities

\[
 |N_{B_{\mathcal M}(s,t)}(X)|\ge |X|
 \qquad
 (X\subseteq \mathcal P(\mathcal M)\setminus\{t\})
\tag{5.2}
\]

characterize some perfect matching, but do not alone ensure connectedness
or residence.

## 6. A Hall-style sufficient compiler theorem

### Definition 6.1 (ordered residence-closed seam graph)

A subgraph \(B^*\subseteq B_{\mathcal M}(s,t)\) is ordered
residence-closed if:

1. there is an injective potential
   \(\phi:\mathcal P(\mathcal M)\to\mathbb Z\) with
   \(\phi(P)<\phi(Q)\) on every seam \(P^+Q^-\in B^*\); and
2. for every \(F\in\mathcal F_{\rm res}(D)\),

\[
                         F\nsubseteq
               R(\mathcal M)\cup E(B^*).
\tag{6.1}
\]

The second condition is universal: no choice of seams from \(B^*\) can
complete a forbidden residence word.

### Theorem 6.2 (two-level Hall compiler)

Let \(\mathcal M\) be internally compatible. Suppose:

1. physical-cell Hall (4.1) holds for \(A\);
2. there are \(s,t\) and an ordered residence-closed
   \(B^*\subseteq B_{\mathcal M}(s,t)\); and
3. port Hall holds:

\[
                         |N_{B^*}(X)|\ge |X|
\tag{6.2}
\]

for every subset of its left side.

Then one residence-safe Hamilton chronology simultaneously installs
every target in \(A\).

#### Proof

Hall gives a perfect matching \(J\subseteq B^*\). The potential excludes
fragment cycles. Since exactly one entry and one exit are unsaturated,
an acyclic functional fragment graph can have only one component, so it
is a spanning path. Condition (6.1) and Lemma 1.1 make it residence-safe.
Theorem 4.1 assigns its occurring cells injectively to all targets.
\(\square\)

For \(A=Z_7\), Theorem 6.2 is the requested simultaneous-installation
certificate. For \(A=A_{29}\), use the old-plus-new Hall condition
(0.6). The ordered residence-closed hypothesis is sufficient, not
necessary; without it, Theorem 5.1 remains exact.

## 7. The rejected 60-arc tuple

The frozen artifact

scratch/k15_h29_zero7_minimal_tuple.json

has SHA-256

1fc903c362ef846f4ecdc96fc335a45f81c77dbea7be4e907a2ac37a02612e23.

It uses the Hall-29, Hall-30, and balanced Hall-31 parent paths. Its
seven records cover \(Z_7\). The right boundary word is shared by
targets \(5801\) and \(21641\), so there are six distinct arc patterns.
Their union has 60 arcs, of which only four are absent from Hall 29.

The tuple was selected from a census with 15,130 degree/cycle-compatible
minimal tuples. It fixes start mask \(2479\), end mask \(22185\), and
passes the directed degree equations. Exact residence enumeration finds

\[
                         23
\tag{7.1}
\]

selected CP-SAT residence clauses contained in its forced union. These
23 clauses include extensions of shorter bad words. Removing every
nonminimal superset leaves six members of
\(\mathcal F_{\rm res}(D)\). They are already internal to four motif
records:

\[
\begin{array}{c|rrrrrrr}
\text{target}&2575&5801&21641&13616&13620&17738&29776\\ \hline
\text{selected clauses}&0&0&0&7&4&6&6\\
\text{minimal cores}&0&0&0&2&2&1&1.
\end{array}
\tag{7.2}
\]

Thus the tuple fails even the individual residence-safe motif filter.
The union-level rank-four clauses of Section 3 remain necessary for
tuples whose individual motifs all pass.

An independent reconstruction from the three parents and their reverses
gives the exact clause-length census

\[
\begin{array}{c|ccc|c}
\text{selected arc count in clause}&2&3&4&\text{total}\\ \hline
\text{all selected clauses}&3&7&13&23\\
\text{minimal cores}&3&1&2&6.
\end{array}
\tag{7.3}
\]

Thus the stored value 23 and the rank-four minimal-core formulation are
consistent: the former is the SAT clause census, the latter is the
irredundant mathematical obstruction.

### Proposition 7.1 (irreparable residence rejection)

No residence-safe Hamilton path in the parent catalogue can contain all
motifs of the 60-arc tuple.

#### Proof

Let \(R\) be its forced arcs. In particular, each of the six audited
minimal cores \(F\in\mathcal F_{\rm res}(D)\) satisfies
\(F\subseteq R\). Any completion still contains \(F\), so Lemma 1.1
makes it residence-unsafe. Adding seams cannot remove a forced forbidden
subword. \(\square\)

This rejection precedes upper-shadow constraints, DM inequalities, and
connectivity. It is not a timeout or bad completion choice. It also
shows why targetwise Hall on motif records is unsound: residence conflicts
arise across records, and the shared boundary word must be expanded into
actual cells before distinct-cell Hall is assessed.

## 8. Practical exact test

For a fixed parent catalogue:

1. Enumerate every individually residence-safe interior and boundary
   motif, retaining cell identity, target incidence, arcs, and flags.
2. Add degree, directed-cycle, endpoint, and all minimal residence-cover
   clauses (3.2). Residence clauses have rank at most four.
3. Run target--cell matching: size 7 for \(Z_7\), or size 1524 in the
   old-plus-new graph for \(A_{29}\).
4. Contract the forced path forest and run port Hall.
5. Either certify an ordered residence-closed seam graph and apply
   Theorem 6.2, or enforce connectedness and exact residence directly
   as in Theorem 5.1.
6. Materialize the 6435-vertex chronology and independently recompute
   residence and the full compiler Hall graph.

The two Hall tests are polynomial. The remaining hard layer is choosing
a connected residence-safe port matching.

## 9. Exact boundary for lane L

### Proved

1. Residence on selected arcs is exactly a rank-four forbidden
   hypergraph.
2. Motif interaction is exactly directed degree, directed-cycle, endpoint,
   and residence-cover compatibility.
3. Simultaneous target installation is exactly physical-cell Hall.
4. Chronology completion is exactly a connected residence-safe port
   perfect matching.
5. The ordered residence-closed two-level Hall theorem is sufficient for
   all seven zero targets or all of \(A_{29}\).
6. The 60-arc tuple is irreparably residence-invalid because its forced
   union contains 23 forbidden motifs.
7. The concrete four-parent \(Z_7\) and five-parent \(Z_{12}\) gates
   have explicit interior-motif transversals and canonical port matchings.

### Still open

1. The old-plus-new Hall inequalities for every subset of \(A_{29}\).
2. A final chronology whose independently recomputed compiler matching
   has deficiency zero.

The previously open zero-target transversal and port-completion items are
now proved for both the concrete \(Z_7\) and \(Z_{12}\) catalogues by
Theorem 10.1 below. They remain nontrivial for any motif family not
contained in one residence-safe parent chronology.

The finite gate is therefore

\[
\boxed{
\begin{array}{c}
\text{residence-safe motif transversal}\\
\quad+\quad\text{physical-cell Hall}\\
\quad+\quad\text{connected residence-safe port Hall}.
\end{array}}
\tag{9.1}
\]

All three layers are necessary; under the ordered residence-closed
hypothesis they are jointly sufficient.

## 10. Concrete four/five-parent application

Put

\[
\begin{aligned}
P_1&=H_{29},&P_2&=H_{30},&P_3&=H_{31},\\
P_4&=\tau_{(1,12)}H_{29},&
P_5&=\tau_{(5,7)}H_{29}.
\end{aligned}
\tag{10.1}
\]

The frozen path certificates are, in this order,

```text
scratch/k15_doubletrans_05_213_hall29.json
scratch/k15_outer2_p1_h30_bridge.json
scratch/k15_trans1113_balanced_hall31.json
scratch/k15_transposition_parent_winner.json
scratch/k15_accumulated_zero_parent_winner.json
```

Let \(D_i\) contain every directed arc of \(P_1,\ldots,P_i\). Direct
deduplication gives

\[
|E(D_3)|=15890,\qquad |E(D_4)|=19751,\qquad |E(D_5)|=23628.
\tag{10.2}
\]

In particular \(P_i\) itself is a spanning directed path in \(D_i\).
Both \(P_4\) and \(P_5\) have 6435 distinct rank-eight vertices and zero
depth-three residence violations.

For a parent path \(P=(p_0,\ldots,p_{6434})\), define

\[
 M_P(t;a,r):=(p_a,p_{a+1},\ldots,p_{a+r+9}),
 \qquad c_P(a,r):=(a+6,r).
\tag{10.3}
\]

Here \(a\) is zero-based, \(r\in\{0,1,2\}\) is the cell depth, and
\(c_P(a,r)\) is the actual compiler cell starting at erosion position
\(a+6\). Thus \(M_P(t;a,r)\) has \(r+9\) arcs. The pair \((a,r)\),
together with the named frozen parent, identifies the literal motif word;
this is not an abstract lattice direction.

The four-parent zero set is

\[
 Z_7=\{2575,5801,13616,13620,17738,21641,29776\},
\tag{10.4}
\]

and the accumulated five-parent zero set is

\[
\begin{split}
 Z_{12}=\{&1707,6669,8855,9494,9495,9522,9526,\\
           &17547,21832,25682,29332,29972\}.
\end{split}
\tag{10.5}
\]

### Theorem 10.1 (explicit zero-target transversal and canonical port matching)

In \(D_4\), the seven rows of Table 10.1 are an internally compatible
physical-cell transversal for \(Z_7\). In \(D_5\), the twelve rows of
Table 10.2 are an internally compatible physical-cell transversal for
\(Z_{12}\). In both cases the remaining port instance has an ordered
residence-closed perfect matching. Consequently the two-level Hall
compiler theorem applies, and all named zero targets occur simultaneously
in a residence-safe Hamilton chronology.

**Table 10.1: transversal on \(P_4=\tau_{(1,12)}H_{29}\).**

\[
\begin{array}{r|r|r|r|r|r}
t&a&r&a+6&\text{arcs}&(p_a,p_{a+r+9})\\ \hline
2575  &1114&2&1120&11&(30145,19629)\\
5801  &1883&2&1889&11&(10399,11147)\\
13616 & 306&2& 312&11&(1758,18750)\\
13620 & 933&2& 939&11&(26988,25722)\\
17738 &5824&1&5830&10&(5531,30354)\\
21641 &5216&1&5222&10&(25942,19245)\\
29776 &1668&1&1674&10&(27474,19038)
\end{array}
\tag{10.6}
\]

**Table 10.2: transversal on \(P_5=\tau_{(5,7)}H_{29}\).**

\[
\begin{array}{r|r|r|r|r|r}
t&a&r&a+6&\text{arcs}&(p_a,p_{a+r+9})\\ \hline
1707  &1883&2&1889&11&(14397,15145)\\
6669  &1114&2&1120&11&(25955,19629)\\
8855  &3343&2&3349&11&(28324,3064)\\
9494  &2428&2&2434&11&(18388,13737)\\
9495  & 932&2& 938&11&(27096,13560)\\
9522  & 307&1& 313&10&(22132,22940)\\
9526  &3634&2&3640&11&(15060,26189)\\
17547 &2119&1&2125&10&(17726,5996)\\
21832 &5213&1&5219&10&(11988,18735)\\
25682 &1668&1&1674&10&(31568,23132)\\
29332 &5664&2&5670&11&(11121,14052)\\
29972 &1312&2&1318&11&(9459,12240)
\end{array}
\tag{10.7}
\]

#### Proof

The four-parent frozen artifact

```text
scratch/t1_12_h29zero7.interior.tsv
```

contains respectively \(4,1,4,1,2,1,3\) residence-safe interior
records for the targets in the displayed order (10.4). Every row of
Table 10.1 is one of those literal records. Independently recomputing
the erosion masks, complete coordinate carrier sets, envelope, and
mandatory mask shows

\[
                         t\in\Gamma_{Z_7}(c_{P_4}(a,r))
\tag{10.8}
\]

for every row. Their seven cells \((a+6,r)\) are distinct. Their parent
arc intervals are pairwise disjoint, hence their union \(R_4\) contains
exactly

\[
                         |R_4|=74
\tag{10.9}
\]

arcs. Assigning target \(t\) to its tabulated cell is a matching of
size seven. It directly proves every physical-cell Hall inequality for
\(Z_7\).

The five-parent artifact

```text
scratch/k15_accumulated_zero12_tau5_7.per_target.tsv
```

contains 26 residence-safe interior records. Its per-target interior
counts in the order (10.5) are

\[
                    (1,4,1,3,1,4,1,4,2,3,1,1).
\tag{10.10}
\]

The same independent reconstruction verifies every row of Table 10.2,
including its target incidence. Again all twelve physical cells and all
twelve parent arc intervals are distinct. The forced union has

\[
                         |R_5|=128,
\tag{10.11}
\]

and the tabulated target-to-cell assignment is a size-twelve matching,
so physical-cell Hall holds for \(Z_{12}\).

It remains to check interaction and ports. For \(i=4,5\), every forced
arc lies in the single path \(P_i\). Therefore indegree and outdegree are
at most one and no directed cycle occurs. More decisively, the complete
arc set \(E(P_i)\) contains no residence-forbidden member of
\(\mathcal F_{\rm res}\). Since this condition is downward closed,
neither \(R_i\) nor any \(R_i\cup J'\) with
\(J'\subseteq E(P_i)\setminus R_i\) contains one.

Contract the forced forest \(R_i\). It has

\[
 h_i=6435-|R_i|
\tag{10.12}
\]

fragments. List them in their order along \(P_i\), as
\(F_1,\ldots,F_{h_i}\), and restrict the port graph to

\[
 B_i^*=\{\operatorname{exit}(F_j)\to
              \operatorname{entry}(F_{j+1}):1\le j<h_i\}.
\tag{10.13}
\]

Equivalently, \(B_i^*=E(P_i)\setminus R_i\). This restricted graph has
one possible successor for each nonterminal fragment and distinct heads,
so its edge set itself is a port perfect matching. In particular its
Hall inequalities hold, in fact with equality for the image of every
left subset. Fragment index is a strictly increasing potential, and the
downward-closure observation proves ordered residence closure. Hence
Theorem 6.2 applies. The exact residual data are

\[
\begin{array}{c|r|r|r|r|r}
&|R_i|&h_i&|B_i^*|&\text{start}&\text{end}\\ \hline
D_4&74 &6361&6360&9901&7779\\
D_5&128&6307&6306&9901&7875.
\end{array}
\tag{10.14}
\]

Thus the remaining port matching is not merely existential: it is the
literal set of omitted arcs of the corresponding transposed parent.
Adding it reconstructs \(P_i\). \(\square\)

### Independent audit and exact scope

The audit

```text
scratch/audit_k15_zero_motif_transversals.py
```

does not import the motif enumerator or the Hall implementation. It
parses the frozen arc words, recomputes the depth-three erosion and
carrier predicate from the definition, verifies all target-to-cell
incidences, checks cell and arc distinctness, scans the complete parents
for residence violations, and reconstructs the forced/seam partition.
It returns `PASS` for both cases. The decisive frozen SHA-256 values are

\[
\begin{array}{c|l}
P_4&\texttt{8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd}\\
Z_7\text{ motifs}&\texttt{7c472a1a98f8d43f114e6b973ffe3b7b0f8e1aa8cee8f7e3d3f590b03b65b9db}\\
P_5&\texttt{2b25279185b50a9485c65cbc727a08d95b71a1d310332cbdcb23dd6b0b3d2cb7}\\
Z_{12}\text{ motifs}&\texttt{5b619b37a99b163c9db3735ae80a2be705e32a70c0b84dfbd37f2e158affd25e}
\end{array}
\tag{10.15}
\]

No Hamilton or CP-SAT search was run for this step. The proof uses a
frozen parent path as an explicit port-matching witness. What remains
open is the full compiler matching over all targets (equivalently the
all-subsets form of (0.6)), not residence-safe installation of the named
seven or twelve zero targets.
