# Protected incidence-C6 moves: exact coupled ledgers and a three-move 7-to-1 criterion

**Date:** 2026-08-01  
**Status:** corrected local-move mathematics for the authenticated protected
k=17 factor
`scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`.
The original version of Theorem 3.1 incorrectly restricted component
changes to even values.  Literal replay gives changes
`-2,-1,0,+1,+2`: after projecting to the owner two-factor and deleting the
three changed projected edges, the retained path matching on the six stubs
need not pair the two endpoint classes of the deleted matching.  The
correct invariant is the arbitrary stub-matching formula below.  The
important special case remains valid: three removed projected edges in
three distinct old components merge those components and give change
`-2`.  The protected-incidence condition, residence-halo locality,
upper-witness multiplicity identity, and serial three-distinct-component
criterion remain valid.  No universal word or compiler is claimed.

## 1. The authenticated starting factor

Let `F` be the spanning degree-two factor of the middle-levels incidence
graph

\[
 ML_9=\left({[17]\choose8},{[17]\choose9};\subset\right)
\]

with retained SHA-256

```text
7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

It contains the 52 protected packet/twin-bank incidences.  Its seven owner
cycles have lengths

\[
 14305,8615,1362,18,4,3,3.                               \tag{1.1}
\]

The rank-ten q1 deck is complete.  Its cyclic short-run census is

\[
 R_1(F)=0,\qquad R_2(F)=3073,\qquad R_3(F)=2710,          \tag{1.2}
\]

and its deeper upper-hole vector is

\[
 (H_{11}(F),H_{12}(F),H_{13}(F))=(1502,295,9).           \tag{1.3}
\]

The problem in this note is to move inside the exact degree-two fibre while
never deleting a protected incidence.

## 2. The Boolean incidence hexagon

Choose a rank-seven core `C` and three distinct coordinates `a,b,c` outside
`C`.  Put

\[
 \ell_a=C+a,\quad\ell_b=C+b,\quad\ell_c=C+c             \tag{2.1}
\]

on the rank-eight shore and

\[
 o_{ab}=C+a+b,\quad o_{bc}=C+b+c,\quad o_{ca}=C+c+a     \tag{2.2}
\]

on the rank-nine shore.  The induced graph is a chordless incidence C6.
Its two alternating matchings are

\[
 E_0=\{\ell_a o_{ab},\ell_b o_{bc},\ell_c o_{ca}\},
\]

\[
 E_1=\{\ell_a o_{ca},\ell_b o_{ab},\ell_c o_{bc}\}.    \tag{2.3}
\]

An oriented toggle `Q=(E^-,E^+)` replaces one of these matchings by the
other.

### Theorem 2.1 (factor and protection criterion)

Let `P` be the fixed set of 52 protected incidences.  The toggle gives
another degree-two factor containing `P` if and only if

\[
 E^-\subseteq F,\qquad E^+\cap F=\varnothing,
 \qquad E^-\cap P=\varnothing.                           \tag{2.4}
\]

#### Proof

Every one of the six C6 vertices is incident with one edge of each
alternating matching.  Replacing `E^-` by `E^+` therefore preserves every
vertex degree.  The first two conditions are exactly the condition that the
symmetric difference is a genuine three-edge replacement.  Since `P` is a
subset of `F`, retaining it is equivalent to deleting no edge of `P`; an
added edge cannot be a protected edge because it is required to lie outside
`F`. \(\square\)

## 3. Projected three-edge reconnection

At each lower vertex `ell_x`, let `p_x` be its other selected rank-nine
neighbour in `F`.  In one orientation the projected Johnson edges change as

\[
 p_a o_{ab},\ p_b o_{bc},\ p_c o_{ca}
 \quad\longmapsto\quad
 p_a o_{ca},\ p_b o_{ab},\ p_c o_{bc}.                  \tag{3.1}
\]

The inverse orientation reverses the three-cycle.  Thus an incidence C6 is
exactly a cyclic reconnection of three projected owner edges.

### Theorem 3.1 (correct stub-matching component delta)

Delete the three projected edges in (3.1), retaining their six labelled
stubs, and contract every retained path between stubs.  Let
`S` be the resulting arbitrary perfect matching on those six stubs.  Let
`M_old` and `M_new` be the old and new three-edge closure matchings.  Then

\[
 \Delta\operatorname{comp}(Q)
 =c(S\cup M_{\rm new})-c(S\cup M_{\rm old}),             \tag{3.2}
\]

where `c` counts alternating cycles in the union of two perfect matchings.
Consequently the possible changes are

\[
                  -2,-1,0,+1,+2.                         \tag{3.3}
\]

If the three removed projected edges lie in three distinct old components,
then each old component becomes one retained path and the cyclic new closure
joins the three paths into one.  In that case, and only this implication is
used by the loose-hypertree criterion,

\[
                  \Delta\operatorname{comp}(Q)=-2.       \tag{3.4}
\]

#### Proof

After deletion, every affected retained component is a path and hence pairs
two of the six stubs.  Those pairs can join any stub types; in particular
they do not in general define an owner-to-lower permutation.  Contracting
the path interiors preserves component count, and closing by `M_old` or
`M_new` gives (3.2).

For completeness, label the old projected edges

\[
 M_{\rm old}=\{x_0y_0,x_1y_1,x_2y_2\},
 \qquad
 M_{\rm new}=\{x_0y_2,x_1y_0,x_2y_1\}.                 \tag{3.5}
\]

Each union of two perfect matchings on six points has between one and three
alternating-cycle components, so (3.2) lies between `-2` and `+2`.  All five
values occur, as witnessed by the following retained-stub matchings:

\[
\begin{array}{c|c}
\Delta\operatorname{comp}&S\\ \hline
-2&M_{\rm old}\\
-1&\{x_0x_1,y_0y_1,x_2y_2\}\\
 0&\{x_0y_0,x_1y_2,x_2y_1\}\\
+1&\{x_0x_1,y_0y_2,x_2y_1\}\\
+2&M_{\rm new}.
\end{array}                                             \tag{3.6}
\]

The `-1` and `+1` rows are exactly the cases excluded by the false
opposite-class assumption: each contains a pair of `x` stubs and a pair of
`y` stubs.  Finally, when the cuts lie in three distinct old cycles, the
three retained paths are joined cyclically by the new matching, proving
(3.4). \(\square\)

In particular, a single C6 cannot change seven components directly to one.
It can pay at most two units of component debt.

## 4. Exact residence locality

For a coordinate `x`, delete the three projected adjacencies in (3.1).
This cuts the affected factor cycles into path segments.  Every old maximal
positive x-run which meets no cut endpoint remains literally unchanged.
After reconnection, every new or modified positive x-run meets one of the
three new seams.

### Theorem 4.1 (junction-age replay)

For every segment endpoint `v`, record the inward x-age

\[
 a_x(v)=\min\{4,\text{number of consecutive x-positive owners from }v
                 \text{ inward}\}.                     \tag{4.1}
\]

Also record whether both endpoints belong to one all-x-positive segment.
Join the positive endpoint germs according to the three new projected
edges.  Each connected component of this weighted endpoint graph is one
new seam-touching x-run; its length is the sum of its segment contributions,
capped at four.  Together with the untouched runs this reconstructs

\[
 (R_1,R_2,R_3)                                           \tag{4.2}
\]

exactly.

#### Proof

Deleting the three edges partitions every affected cyclic trace into
literal path traces.  A positive run in a path is either internal, hence
untouched, or meets one or both endpoints.  New adjacencies can concatenate
only endpoint runs.  The endpoint graph records precisely those
concatenations.  Since only the predicate length below four is required,
ages may be capped at four.  The all-positive flag prevents double-counting
one segment seen from both ends. \(\square\)

For one coordinate, at most three old and three new runs meet the toggle.
Consequently

\[
 |\Delta R_{<4}(Q)|\le3\quad\text{per coordinate},
 \qquad |\Delta R_{<4}(Q)|\le51                         \tag{4.3}
\]

after summing over seventeen coordinates.  This is a locality bound, not a
promise of improvement.

## 5. Exact arbitrary-width upper ledger

Let `m_F(S)` be the number of cyclic owner intervals in `F` whose union is
the target `S`.  For one toggle, let `W_Q^-(S)` be the set of old witnesses
meeting at least one removed projected edge, and let `W_Q^+(S)` be the set
of new witnesses meeting at least one added edge.  Intervals wholly inside
the cut path segments are common to both factors.

### Theorem 5.1 (witness-multiplicity identity)

For every target `S`,

\[
 m_{F\triangle Q}(S)
 =m_F(S)-|W_Q^-(S)|+|W_Q^+(S)|.                          \tag{5.1}
\]

Therefore the exact rank-r hole change is

\[
\begin{aligned}
 \Delta H_r(Q)=
 &\left|\left\{S:|S|=r, m_F(S)>0,
             m_{F\triangle Q}(S)=0\right\}\right|\\
 &-\left|\left\{S:|S|=r, m_F(S)=0,
             m_{F\triangle Q}(S)>0\right\}\right|.
                                                               \tag{5.2}
\end{aligned}
\]

#### Proof

Partition the old intervals into those wholly contained in a surviving
path segment and those crossing a removed edge.  Partition the new intervals
analogously.  The first classes are in value-preserving bijection.  The
second classes are exactly `W^-` and `W^+`, giving (5.1).  Formula (5.2) is
the definition of a change in support. \(\square\)

Unlike residence, the affected witness set need not be bounded in size by
a constant: one new interval may traverse long portions of several former
components.  Exact multiplicities, not only target indicators, must be
retained so that a C6 does not delete the final witness of a rank-11, 12, or
13 target.

The 52 protected incidences keep all three protected owner paths intact.
Hence their twelve internal Ferrers witnesses survive every admissible C6
automatically.

## 6. The weakest exact three-move criterion

Let

\[
 F_0=F,\qquad F_i=F_{i-1}\triangle Q_i\quad(1\le i\le3).
\]

### Theorem 6.1 (serial 7-to-1 criterion)

Three C6 moves reduce the seven-component protected factor to one while
retaining the protected bank if, for `i=1,2,3`,

1. `Q_i` satisfies (2.4) in `F_(i-1)`; and
2. the three removed edges of `Q_i` lie in three distinct components of
   `F_(i-1)`.

This is a sufficient serial criterion.  Any three-move `7`-to-`1` sequence
must have component delta `-2` at every step, because (3.3) bounds the gain
of one move by two.  We do not use here any broader classification of a
toggle from only the number of old components met by its deleted edges.

#### Proof

By Theorem 3.1, every move lowers the component count by exactly two.  The
sequence is therefore

\[
 7\longrightarrow5\longrightarrow3\longrightarrow1.    \tag{6.1}
\]

Theorem 2.1 retains the protected bank.  The final assertion follows because
three moves must pay six units of component debt while one move pays at most
two. \(\square\)

No per-move monotonicity of residence or upper holes is required.  The
weakest coupled acceptance test is the final one:

\[
 R_{<4}(F_3)\le R_{<4}(F_0),                             \tag{6.2}
\]

\[
 H_r(F_3)\le H_r(F_0)\qquad(r=11,12,13),                 \tag{6.3}
\]

or whatever sharper terminal bounds the construction needs.  Intermediate
factors may be worse.  This is important because intervals created by two
or three joins interact and cannot in general be scored as a sum of
single-move gains.

## 7. Static loose-hypertree corollary

For a C6 toggle in the original factor, let

\[
 K(Q)\subseteq\{1,\ldots,7\}                            \tag{7.1}
\]

be the set of original component labels containing its three removed edges.
Let `supp(Q)=E^- union E^+` be its complete six-incidence support.

### Theorem 7.1 (commuting loose-hypertree fusion)

Suppose three protected-safe toggles `Q_1,Q_2,Q_3` satisfy:

1. their complete incidence supports are pairwise edge-disjoint;
2. each `K(Q_i)` has size three; and
3. after reordering the toggles,
   
   \[
   |K(Q_1)|=3,
   \qquad
   \left|K(Q_i)\cap\bigcup_{j<i}K(Q_j)\right|=1
       \quad(i=2,3),                                    \tag{7.2}
   \]

   and their union is all seven component labels.

Then the toggles commute, remain serially valid, and reduce the factor from
seven components to one.

Condition 3 says exactly that the three component triples form a spanning
three-edge loose hypertree: the first hyperedge has three vertices and each
later hyperedge attaches through one old vertex while adding two new ones.

#### Proof

Full support disjointness means that no toggle changes the selected/absent
status of an incidence used by another; symmetric differences commute and
all three moves remain legal.  After `Q_1`, its three original components
form one component.  The next component triple meets that merged block in
exactly one original component and contains two untouched components, so
its removed edges lie in three current components.  It merges them.  The
same argument applies to `Q_3`.  Theorem 6.1 completes the proof. \(\square\)

Edge-disjoint full supports are only a convenient static sufficient
condition.  They may be weakened to the direct serial-validity condition of
Theorem 6.1; shared vertices are harmless whenever all six incidence states
remain correct at the time of each move.

### Exact coupled terminal test

For a proposed loose hypertree, form

\[
 F'=F\triangle Q_1\triangle Q_2\triangle Q_3.            \tag{7.3}
\]

Then:

1. replay all 48,620 factor incidences and the 52 protected flags;
2. replay the component count;
3. use Theorem 4.1 for the final run census; and
4. use Theorem 5.1, with intervals crossing any of the three old/new seam
   sets counted once, for ranks 11--13.

This final replay is weaker and safer than requiring each toggle to be
individually nonworsening.  It automatically credits new intervals crossing
two or three of the loose-hypertree joins.

## 8. Concrete factor-local moves

The H100 O3 enumeration records concrete protected-safe C6 rows using the
schema

```text
core  a b c  orientation
old_incidence[3]  new_incidence[3]
old_component_triple  delta_components
delta_run1 delta_run2 delta_run3
rank11_lost rank11_gained delta_h11
rank12_lost rank12_gained delta_h12
rank13_lost rank13_gained delta_h13
```

The independent literal replay is now frozen in
`MATH_AUDIT_K17_PROTECTED_C6_LOCAL_CALCULUS_AND_THREE_FUSION_OBSTRUCTION_20260801.md`.
It finds the following component-delta distributions:

\[
\begin{array}{c|rrrrr}
\Delta c&-2&-1&0&+1&+2\\ \hline
\text{all protected-safe}&3379&15875&21708&4462&1394\\
\text{q1-hole-free}&405&1967&2642&527&169.
\end{array}                                             \tag{8.1}
\]

Thus the authenticated factor realizes every value in (3.3), not merely
the abstract stub matchings in (3.6).  The same audit proves that no three
initially legal static component triples cover all seven old components, so
the sufficient loose-hypertree face of Theorem 7.1 is empty for this frozen
factor.  This is not a no-go for a dynamic sequence that creates a new C6,
for preparatory neutral/splitting moves, for higher support, or for another
protected factor.

### Theorem 8.1 (complete prefix-q1-safe serial C6 obstruction)

Call a serial C6 step *prefix-q1-safe* when it

1. is legal and avoids all 52 protected incidences;
2. deletes projected edges in three distinct current components; and
3. leaves every rank-ten colour represented after that step.

Starting from the authenticated factor, there is no prefix-q1-safe C6
sequence

\[
                 7\longrightarrow5\longrightarrow3
                   \longrightarrow1.                   \tag{8.2}
\]

More exactly, the complete first generation consists of the 405
rank-ten-safe `7`-to-`5` children in (8.1).  Regenerating the complete
literal C6 catalogue on every child gives only five live children and twelve
ordered safe `5`-to-`3` moves.  These twelve rows represent six unordered
two-move states.  Regenerating the catalogue on every resulting
three-component state gives zero safe `3`-to-`1` moves.

#### Proof

For every current factor, the enumerator loops over every rank-seven core,
every three-subset of its ten outside coordinates, and both alternating
orientations.  It retains exactly the three conditions above, rebuilds the
literal factor after each accepted toggle, and recomputes its components and
rank-ten multiplicities.  Thus the first, second and third catalogues are
complete within the prefix-q1-safe C6 class.  Their exact counts are
`405`, `12`, and `0`; hence (8.2) is impossible in that class.  A separate
deterministic implementation reconstructs all 405 children, the five live
children and twelve ordered grandchildren, and again obtains no third move.
\(\square\)

The authoritative replay artifacts are

```text
scratch/threadA_k17_c6_dynamic2_20260801/sweep.audit.json
  SHA 26c3694f511e9d7ae470c40f54ae643f2fc6f3d66089dbe7b2a90894f9cf8bdf
scratch/threadA_k17_c6_dynamic2_20260801/sweep.independent.audit.json
  SHA 4d308e77eba795856b9748762eb90fd9b236e857d2942b113d8eae9419ffe6b9
scratch/threadA_k17_c6_dynamic2_20260801/sweep.children.tsv
  SHA 922f8e03cea9ade87c681d6fc71c01714cfb5b5c0ba998c4c97fa87e487c7964
scratch/threadA_k17_c6_dynamic2_20260801/sweep.moves.tsv
  SHA cb2bb168c197c95bbcbf4e143cd218e4d4bab72e0132616908b5aafbfd47110d
scratch/threadA_k17_c6_dynamic2_20260801/sweep_k17_c6_dynamic_405.cpp
  SHA 0037fd2a5ca2daa2b4fabc974beef0f053ad907d827ac09631beb7c41f2c73ba
scratch/threadA_k17_c6_loose_hypertree_20260801/verify_k17_c6_dynamic_405.cpp
  SHA 81a6590a43bb1f011c592fb77fe23bee8dedd828fc691aff91277ce548fc725c
```

The theorem does **not** test a compound batch that temporarily loses a
rank-ten colour and restores it only at the final state.  It also does not
exclude a protected q1-safe preparatory move with component delta `-1`, `0`,
`+1` or `+2`, a dynamically created non-fusion C6, or a C8/higher-support
packet (including the open q4/higher-arity topology routes).  Those are the
exact surviving serial routes.

## 9. Scope

The three-move theorem is a conditional topology criterion, not an existence
claim; the current frozen factor fails its static hypothesis by the exact
census above.  Even a one-component result with nonincreasing versions of
(1.2)--(1.3) would still have thousands of short runs and upper holes.  It
would be a better protected host and a precise starting point for a
multiobjective C6/C8 descent, not a k=17 universal word or a common-cap
compiler.
