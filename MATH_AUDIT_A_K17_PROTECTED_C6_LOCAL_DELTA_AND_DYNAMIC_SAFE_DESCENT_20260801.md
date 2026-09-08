# K17 Protected Incidence-C6 Local Delta and Dynamic Safe-Descent Audit

Date: 2026-08-01  
Lane: A  
Status: **proved local calculus; exhaustive no-go for three serial individually-q1-safe ternary mergers from the frozen protected factor**

## 1. Frozen input and scope

The input is

`scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`,

SHA-256

`7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`.

It is the authenticated degree-two incidence factor with component sizes

\[
14305,8615,1362,18,4,3,3,
\]

all rank-eight and rank-ten colours present, and exactly 52 protected
lower--owner incidences.  Its defect statistic is

\[
\Phi=R_2+R_3+H_{11}+H_{12}+H_{13}
     =3073+2710+1502+295+9=7589.                 \tag{1.1}
\]

Here \(R_i\) is the number of cyclic positive coordinate runs of length
\(i\), and \(H_j\) is the number of missing rank-\(j\) interval-union
targets.

This note studies only Boolean incidence \(C_6\) switches that preserve all
52 flags and leave the complete rank-ten palette covered after **each**
move.  The last qualification is essential.  Temporary q1 debt repaired by
a later move, a support larger than three, and a preliminary non-merging
switch are not covered by the main no-go below.

## 2. Exact projected switch

Fix a rank-seven core \(S\) and distinct coordinates \(a,b,c\notin S\).
Put

\[
t_a=S+a,\quad t_b=S+b,\quad t_c=S+c
\]

and

\[
u_{ab}=S+a+b,\quad u_{bc}=S+b+c,\quad u_{ca}=S+c+a.
\]

One orientation of the incidence hex replaces

\[
(t_a,u_{ab}),\ (t_b,u_{bc}),\ (t_c,u_{ca})       \tag{2.1}
\]

by

\[
(t_a,u_{ca}),\ (t_b,u_{ab}),\ (t_c,u_{bc});      \tag{2.2}
\]

the other orientation reverses this replacement.  Let \(v_a,v_b,v_c\)
be the unchanged second owner endpoints at \(t_a,t_b,t_c\).  In the owner
projection (2.1)--(2.2) is exactly the three-edge switch

\[
u_{ab}v_a,\ u_{bc}v_b,\ u_{ca}v_c
   \longmapsto
u_{ca}v_a,\ u_{ab}v_b,\ u_{bc}v_c.               \tag{2.3}
\]

All lower and owner degrees remain two.  The implementation rejects a move
if an old incidence is protected, a new incidence is already selected, or
some rank-ten colour loses its last occurrence.

## 3. Local-delta theorem

### Theorem 3.1 (three-edge locality)

For the switch (2.3):

1. If the three removed projected edges lie in three different factor
   cycles, the switch merges those cycles into one and reduces the component
   count by exactly two.
2. A positive coordinate run can change its status as a run of length less
   than four only if it contains an endpoint of an old or new junction.
   Thus its exact delta is obtained by scanning, for each of the six
   junction neighbourhoods and each coordinate, only until a zero boundary
   or four positive owners have been seen.
3. An interval-union occurrence not using a changed adjacency remains the
   same ordered owner interval, except for the full-cycle occurrence of an
   affected component.  Hence the exact rank-eleven through rank-thirteen
   deck delta is obtained by enumerating intervals crossing an old or new
   join, stopping as soon as the union rank exceeds 13, together with the
   affected full-cycle cases.

Consequently \(\Delta\Phi\) is determined by the six junction
neighbourhoods and the crossing-interval lists.

#### Proof

Deleting one edge from each of three cycles produces three paths.  The
cyclic reassignment in (2.3) joins the terminal endpoints of these paths in
one cycle, proving (1).

For a fixed coordinate, all adjacencies away from the six old/new junctions
are unchanged.  A maximal positive run disjoint from those junctions has
the same two boundary edges and the same owner sequence before and after
the switch.  If a changed run has length at most three, walking at most
three positive owners from a junction finds the whole run; a fourth
positive owner certifies that it contributes nothing to \(R_1+R_2+R_3\).
This proves (2).

Likewise, a proper cyclic interval is characterized by its internal factor
adjacencies.  If none is changed, the interval survives literally.  Every
other proper interval crosses a changed join.  Along an extension its union
only grows, so after its rank exceeds 13 it can never contribute again.
The only adjacency-free ambiguity is an interval equal to a complete
affected cycle; listing those full-cycle occurrences separately proves
(3).  Summing the exact occurrence-count changes decides whether each
target count becomes zero or positive and hence gives \(\Delta\Phi\).
\(\square\)

The production catalogue uses a stronger terminal check: it rebuilds the
entire factor and recomputes components, all short runs, and all cyclic
rank-eleven through rank-thirteen interval witnesses.  Therefore acceptance
does not rely on additive single-move estimates or on an omitted
multi-junction interaction.

## 4. Complete first-generation catalogue

There are exactly 405 protected, individually rank-ten-safe incidence
hexes whose three removed projected edges lie in three distinct original
components.  Every one was literally scored.  With components numbered in
the displayed size order, their component-mask histogram and
\(\Delta\Phi\) ranges are

| component mask | components | count | \(\Delta\Phi\) range |
|---:|---|---:|---:|
| 7  | \(\{0,1,2\}\) | 391 | \([-6,8]\) |
| 11 | \(\{0,1,3\}\) | 9 | \([-2,0]\) |
| 13 | \(\{0,2,3\}\) | 1 | \([1,1]\) |
| 14 | \(\{1,2,3\}\) | 1 | \([1,1]\) |
| 35 | \(\{0,1,5\}\) | 1 | \([-1,-1]\) |
| 67 | \(\{0,1,6\}\) | 2 | \([-3,0]\) |

No such move touches component 4, the four-owner component.  Thus the
fixed first-generation component hypergraph has no spanning loose
hypertree.  This is already an exact obstruction to three simultaneous
baseline safe mergers.

The best single move is catalogue row 144 (external user id 17416):

\[
(S;a,b,c;\epsilon)=(36449;1,12,13;0).
\]

It gives five components and

\[
(R_2,R_3,H_{11},H_{12},H_{13};\Phi)
=(3071,2709,1501,293,9;7583).                    \tag{4.1}
\]

The materialized child is

`scratch/threadA_k17_c6_loose_hypertree_20260801/row144.factor.tsv`,

SHA-256

`af235ad2b631e4dd56f686e823571d043c1bfd482cccb924ae86ba9df0be67fa`.

Its component sizes are \(24282,18,4,3,3\).  Complete regeneration on this
child finds no protected individually-q1-safe ternary merger.

## 5. Complete dynamic three-generation sweep

The previous paragraph does not by itself rule out choosing another first
move.  We therefore performed the following exhaustive serial audit.

1. Materialize each of the 405 first-generation moves.
2. On every five-component child, regenerate the complete protected,
   individually-q1-safe ternary-merge catalogue.
3. Materialize every second move.
4. On every resulting three-component state, regenerate the complete safe
   \(3\to1\) catalogue.

Exactly five first rows admit a second move:

\[
171,172,239,248,362.
\]

They admit 12 ordered second moves, representing the six unordered pairs

\[
\{171,239\},\ \{171,248\},\ \{172,239\},\
\{172,248\},\ \{239,362\},\ \{248,362\}.        \tag{5.1}
\]

The best three-component defect is \(7587\).  Complete third-generation
regeneration on all six states returns zero safe \(3\to1\) moves.

### Corollary 5.1 (scoped serial no-go)

Starting from the frozen protected factor, no sequence of three incidence
\(C_6\) moves can join all seven components if every move

- preserves all 52 protected incidences,
- preserves the complete rank-ten palette immediately, and
- is a ternary merge at the state where it is applied.

#### Proof

The first move is one of the complete 405-row catalogue.  The exhaustive
child regeneration leaves only (5.1).  Every corresponding complete final
catalogue is empty. \(\square\)

This corollary does **not** rule out a component-neutral preparatory C6, a
two-component rethread, temporary q1 debt with compound restoration, or a
larger alternating circuit.  Those are the exact next escape classes.

## 6. Complete component-neutral preparation sweep

The first escape left by Corollary 5.1 is a protected q1-safe C6 that keeps
the component count equal to seven, followed by a three-edge fusion
hypertree.  The complete component-neutral preparation catalogue has

\[
2642
\]

rows.  Every row was literally scored; the best has
\(\Delta\Phi=-8\).  Preparation component-mask counts are

\[
1:584,\quad 2:126,\quad 3:1668,\quad 5:190,\quad
6:71,\quad 9:2,\quad 33:1.                      \tag{6.1}
\]

For every prepared state the complete protected individually-q1-safe
ternary-merge catalogue was regenerated.  Every state has at least one such
move, and the total number of regenerated fusion rows is

\[
968086.                                             \tag{6.2}
\]

Nevertheless, on no prepared state do the supported component triples
contain three hyperedges forming a spanning loose hypertree.  Thus no move
compatibility or final \(\Phi\) calculation is reached: the exact
component-mask obstruction occurs first.

An independent endpoint/component/q1-only implementation reproduced all
2642 per-state fusion counts and the zero-pattern verdict without using the
run/deep scorer or the producer's triple selector.  Its aggregated fusion
mask histogram is

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
\text{mask}&7&11&13&14&19&21&22&25&28&35&37&38&67&69&70\\
\hline
\text{rows}&936795&17909&4374&2810&7&9&1&1&1&2381&105&58&3330&269&36.
\end{array}                                          \tag{6.3}
\]

Nine regenerated fusion rows touch component 4, so the obstruction is not
the simpler assertion that this component is always isolated.  The exact
statement is statewise correlation: none of the 2642 individual mask
families contains a spanning three-edge loose tree.

### Corollary 6.1 (scoped neutral-preparation no-go)

No protected, immediately-q1-safe component-neutral C6 from the frozen
factor can be followed by three simultaneously available protected,
immediately-q1-safe ternary C6s whose baseline-component hyperedges form a
spanning loose hypertree.

This does not rule out dynamically regenerating the second and third fusion
after each preceding fusion, nor a batch whose intermediate moves incur q1
debt.  The latter is the separate net-q1 repair face.

## 7. Frozen artefacts

- Search source:
  `scratch/threadA_k17_c6_loose_hypertree_20260801/search_k17_c6_loose_hypertree.cpp`,
  SHA `065416a48b577e11b495dd9e2596e3820fc80409b563433a5d2d7bf11ec32e1c`.
- Complete 405-row catalogue:
  `scratch/threadA_k17_c6_loose_hypertree_20260801/result.catalogue.tsv`,
  SHA `090226cc365861f9247ad1dd65327749b464ea22523e6c7cfef51d249af6dfe9`.
- Independent complete first-generation audit:
  `scratch/threadA_k17_c6_loose_hypertree_20260801/result.independent.audit.json`,
  SHA `cf0febde7cecc8166fb9cfc0cc7296f68226157cca5ff57a5e7e11d4b0f615e5`.
- Dynamic sweep source:
  `scratch/threadA_k17_c6_loose_hypertree_20260801/sweep_k17_c6_dynamic_405.cpp`,
  SHA `0037fd2a5ca2daa2b4fabc974beef0f053ad907d827ac09631beb7c41f2c73ba`.
- Dynamic child and move ledgers:
  `sweep.children.tsv` SHA
  `922f8e03cea9ade87c681d6fc71c01714cfb5b5c0ba998c4c97fa87e487c7964`,
  and `sweep.moves.tsv` SHA
  `cb2bb168c197c95bbcbf4e143cd218e4d4bab72e0132616908b5aafbfd47110d`.
- Primary dynamic audit:
  `sweep.audit.json` SHA
  `26c3694f511e9d7ae470c40f54ae643f2fc6f3d66089dbe7b2a90894f9cf8bdf`.
- Deterministic second replay:
  `sweep.independent.audit.json` SHA
  `4d308e77eba795856b9748762eb90fd9b236e857d2942b113d8eae9419ffe6b9`.
- Neutral-preparation sweep source:
  `scratch/threadA_k17_c6_loose_hypertree_20260801/sweep_k17_c6_prep2642.cpp`,
  SHA `c53b40a53fcacae25f449fae3fafd60cd138aead99c9ffc6edd26418d907445e`.
- Complete preparation catalogue:
  `prep.catalogue.tsv`, SHA
  `ed9898abd4af82388b69ac344eb9cd45c976c3232aa88ccedb23c3dc2acf3251`.
- Per-preparation summary and primary audit:
  `prep.summary.tsv` SHA
  `ec2ffeb563391b1caecc8f9d66c1d96df4ff52c49a109960161bd6fc77387757`,
  and `prep.best.audit.json` SHA
  `01a2d506ececc304edbcb88481cfbd4358a3f6f448bec5bbfda9a9335c0b788e`.
- Independent component-mask audit:
  `prep.independent.audit.json` SHA
  `1d8f51dadad116bfc4a6dfc1c303b4d46d87ccf2506c9026b585e697c3539733`.

All nontrivial runs were compiled with `-O3` and executed on H100 CPU under
`/home/amodo/or15/work`; no `/dev/shm` result is used.
