# A dual-rail square-switch reduction for the exact `15 -> 16` lift

## 0. Purpose

The strict shared-tail lift and every cut-only use of the canonical MSW
shore are impossible.  This note isolates the smallest surviving
architecture.  It starts from a rank-eight factor `F` on `[15]` and the
complementary rank-seven factor `bar(F)`, changes both factors jointly, and
uses colour-aware square switches to braid the two Pascal sectors.

The reduction is exact at q1.  It does **not** assert that the needed
dual-resident factor or the final braid exists; those are the two finite
objects now being searched.

## 1. The two Pascal rails

Write `X=[15]` and let `z` be the new coordinate.  The rank-eight layer of
`[16]` splits as

\[
 {cal A}=\binom{X}{8},
 \qquad
 {cal B}=\{\{z\}\cup R:R\in\binom{X}{7}\}.
\tag{1.1}
\]

Let `F_A` be a spanning 2-factor of `J(15,8)`.  Complementing its vertices
and edges gives a spanning 2-factor `F_B` of `J(15,7)`.  Lift the latter to
the `B` sector by adjoining `z` to every vertex.  Initially

\[
 F_A\sqcup(\{z\}+F_B)
\]

is a spanning 2-factor of the child middle layer with no cross-sector
edges.

The four q1 palettes have different roles:

\[
\begin{array}{c|cc}
 &\text{intersection colour}&\text{union colour}\\ \hline
AA&X_0\cap X_1&X_0\cup X_1\\
BB&\{z\}\cup(R_0\cap R_1)&\{z\}\cup(R_0\cup R_1)\\
AB&R&\{z\}\cup X\quad(R\subset X).
\end{array}
\tag{1.2}
\]

In particular only BB edges can cover q1 targets containing `z` on the
lower side.  This is why q1 support must be imposed before ports or the
compiler.

## 2. The colour-aware square switch

Take an AA edge `(X_0,X_1)` and a BB projection edge `(R_0,R_1)` satisfying

\[
 R_0=X_0\cap X_1,
 \qquad
 X_0=R_0\cup R_1.
\tag{2.1}
\]

Then `R_0 subset X_1` and `R_1 subset X_0`, so the two cross edges

\[
 (X_1,\{z\}\cup R_0),
 \qquad
 (X_0,\{z\}\cup R_1)
\tag{2.2}
\]

are legal Johnson edges in the child layer.

### Lemma 2.1 (square palette ledger)

Replacing the two rail edges by (2.2) has the following exact effect:

\[
\begin{array}{c|c|c}
&\text{removed}&\text{added}\\ \hline
\text{lower, no }z&R_0&R_0,R_1\\
\text{lower, with }z&\{z\}+(R_0\cap R_1)&\varnothing\\
\text{upper, no }z&X_0\cup X_1&\varnothing\\
\text{upper, with }z&\{z\}+X_0&\{z\}+X_0,\{z\}+X_1.
\end{array}
\tag{2.3}
\]

Hence the unique AA lower colour `R_0` and the unique BB upper colour
`z+X_0` are restored automatically.  The switch is q1-safe precisely when
the removed BB lower colour and removed AA upper colour have other retained
occurrences (or are charged to the global boundary budget of at most two).

### Proof

The old AA edge has intersection `R_0`; the old BB edge has union
`z+(R_0 union R_1)=z+X_0`.  The new edge incident with `X_1` has intersection
`R_0` and union `z+X_1`; the new edge incident with `X_0` has intersection
`R_1` and union `z+X_0`.  The remaining two removed colours are exactly
those displayed in (2.3).  `square`

Thus a square is the correct primitive braid move: it preserves the two
tight palettes by identity and spends only duplicated occurrences from the
two slack palettes.

## 3. Topology and the singleton channel

Removing one edge from each of two distinct cycles and reconnecting their
four endpoints crosswise by a square switch merges the cycles.  A sequence
of component-transversal squares can therefore reduce the disjoint rail
factor to one child cycle.  Cutting one final edge produces the required
linear middle chronology and costs at most one additional q1 colour.

For depth `d=3`, the new coordinate appears in the source only through
positive `z`-runs of the child chronology.  Every such run must have length
at least four.  A four-state B segment flanked by legal incidence rungs is
a particularly strong trace channel: it creates a unique source position
carrying `z`, and that position may be set to the literal singleton `{z}`.

Indeed, write the collar as

\[
 A_L,B_{R_0},B_{R_1},B_{R_2},B_{R_3},A_R.
\]

The rungs imply `R_0 subset A_L` and `R_3 subset A_R`.  Any old coordinate
in all four B states therefore occurs in both flanks.  Its depth-three
erosion interval has the unique `z` position strictly inside it, so that
position is not mandatory for the old coordinate.  Coordinates outside
the fourfold intersection are absent from its envelope.  Hence the unique
position can be pinned to `{z}` while the other source positions retain
the maximal envelope.  This is the four-ear lemma.

A four-ear is sufficient for the individual singleton channel, but not for
simultaneous coverage of all lower targets; unrestricted `COMP_3` must
still be solved.  Nor is a four-ear logically necessary, since a longer
`z`-run can also admit a literal `{z}` position.

Consequently the macro topology should have:

1. every B segment of length at least four;
2. either a marked internal four-state B segment (which admits `{z}` by the
   four-ear lemma), or more generally a direct feasible compiler selector
   `A_p={z}`;
3. local depth-three residence at every square seam;
4. a connected child factor before its final opening.

## 4. Exact sufficient finite object

The following data suffice for an optimal `k=16` word.

1. A rank-eight 2-factor `F_A` whose lower q1 palette is exact and whose
   upper q1 palette is complete.
2. Its complementary rank-seven factor `F_B`, with complete lower q1
   palette; equivalently the relevant dual palette of `F_A` is complete.
3. Both rail chronologies are depth-three resident.
4. An edge-disjoint family of square switches satisfying the joint
   multiplicity ledger (2.3), merging all components and producing the
   residence conditions in Section 3.
5. After one safe opening, arbitrary-width upper completeness of the child
   chronology and feasibility of unrestricted `COMP_3`.

Items 1--3 are the **dual-resident factor problem**.  Item 4 is a sparse
component-fusion/port problem.  Item 5 is checked exactly by the existing
compiler and exhaustive verifier.

## 5. Why fixed cut-only rails are already excluded

Two independent finite optimizations show that merely cutting either saved
rail cannot meet these conditions.

* For the complement rail derived from `answers/k15.word`, covering its
  `2010` bad run clauses needs at least `1575` cuts, while retaining at
  least `5003/5005` q1 colours permits at most `1432` cuts.
* The completed facet rail's joint hazard/per-colour-capacity model is
  infeasible even with boundary loss two and cut cap `1429`.

Therefore the valid master must **select or rethread BB edges jointly**; a
cut-only segmentation of either fixed answer is impossible.  The centered
PBBS factor is the natural seed because its q1 palettes are already
complete, and its entire protected residence defect is only five
`Z_15`-orbits.

## 6. Solver interface

A sound sparse search should separate the stages:

1. select a q1-complete dual-resident factor (quotient variables);
2. enumerate its q1-safe square catalogue using (2.1)--(2.3);
3. select a component-transversal square packet with local residence
   clauses and either a candidate four-state ear or an unrestricted
   singleton-selector channel;
4. decode the child chronology and reject unless its q1 hole count is at
   most two and every upper target occurs;
5. invoke unrestricted `COMP_3` and exhaustively verify the emitted word.

No solver result before stage 5 is an exact `k=16` certificate.

## 7. Centered-factor scope correction

For a centered Johnson factor coming from an oriented odd-graph 2-factor,
the primitive-square component graph is a perfect matching on the
`f^2`-orbits.  The retained PBBS successor has 73 odd cycles, so its
complementary A/B square graph is literally 73 diagonal pairs.  Its exact
undirected catalogue has 12,870 primitive squares, two per A edge, but no
packet of them can reduce the 146 initial cycles below 73.

This is a centered-factor theorem, not a consequence of complementarity.
An explicit q1-complete pair in `J(5,2)` has a connected `K_(2,2)` square
incidence graph.  Against PBBS B, the unrelated audited A factor of cycle
lengths `6390,45` has 7,485 primitive squares but three component-incidence
blocks, so that fixed catalogue cannot yield one cycle either.

The unrestricted even equivariant `(c,t)` model is broader: every change of
`t` is a general containment rung, with no compulsory pairing into a
primitive square.  It can therefore evade this component invariant, while
retaining the separate orbit, palette, residence, shadow and compiler gates.
The proofs, counts and exact `(c,t)` start/end law are in
`MATH_ATTACK_R_K16_DUAL_RAIL_SQUARE_DIAGONAL_AND_EQUIVARIANT_CT_20260729.md`.
