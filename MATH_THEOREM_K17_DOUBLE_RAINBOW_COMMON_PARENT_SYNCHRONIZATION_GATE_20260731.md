# The K17 double-rainbow factor is mode-synchronized but parent-unsynchronized

Date: 2026-07-31  
Status: exact fixed-certificate theorem and exact reformulation; no K17 word
or existence theorem is claimed

## 0. Result

Let `H` be the authenticated 21-component factor

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components
```

on the rank-nine layer of `[15] union {x,y}`.  It uses every rank-eight
lower colour exactly once and covers every rank-ten upper colour.  For each
old rank-seven set `C`, inspect the two lower-colour rows `C+x` and `C+y`.

The two rows already agree on their **mode** for every one of the 6,435
values of `C`:

* 5,005 rows are pure (`XX` together with `YY`);
* 1,430 rows are attached (`AX` together with `AY`);
* there is no mixed-mode row.

But they usually do not come from one common old Johnson edge.  The exact
census is

| mode | common-parent | rows |
|---|---:|---:|
| pure | yes | 189 |
| pure | no | **4,816** |
| attached | yes | 1,382 |
| attached | no | **48** |

Thus exactly

\[
                         4,864                         \tag{0.1}
\]

of the 6,435 paired rows violate the common-parent identity.  This is not a
component-count defect: only 48 bad rows have their x- and y-edges in the
same child component.  The dominant blocks have 3,638 bad pure rows between
child components 1 and 2 and 1,135 between components 0 and 2.

One whole part of the direct construction is already exact.  The 5,005
selected `AA` edges form a cap-two factor supported on exactly the 5,005
pure-mode `C`'s: every such `A(C)` has AA-degree two and every attached-mode
`A(C)` has AA-degree zero.  Thus a synchronization repair which keeps the
current mode set can retain the entire AA shore.  What is missing is the
common old parent chronology and its coupled x/y/old edges, not the
rank-six-to-rank-seven cap factor.

Consequently the current factor cannot be converted into a direct
common-parent four-sector factor by a small splice.  Any such conversion
must first change at least 4,864 selected physical colour-rows.  There is a
second exact obstruction: the 1,382 already-good attached rows are directed
old parent arcs, but their tail--head graph has maximum matching only 1,370.
Thus at least 12 of those good rows must also change.  The final physical
lower bound is therefore

\[
                         4,876.                        \tag{0.2}
\]

In the selected colour-owner incidence vector a target must remove at least
7,538 incidences and add the same number, hence has Hamming distance at least

\[
                         15,076.                       \tag{0.3}
\]

Moreover, at least 2,693 presently unique rank-ten providers must be removed
and their targets re-provided elsewhere.  Therefore lower-rainbow-preserving
alternating cycles are a complete move basis, but unprotected flow alone is
not enough: the synchronization must be solved jointly with upper-q1
provider transport.

## 1. The common-parent row identity

Write the four rank-nine owner sectors as

\[
 U(V)=V,\quad X(T)=T+x,\quad Y(T)=T+y,\quad A(C)=C+x+y,
\]

where `|V|=9`, `|T|=8`, and `|C|=7` on the old 15 coordinates.

The selected edge of lower colour `C+x` is either

\[
 X(T_0)X(T_1)\quad\text{or}\quad A(C)X(T_0),       \tag{1.1}
\]

and the selected edge of lower colour `C+y` is analogously either

\[
 Y(S_0)Y(S_1)\quad\text{or}\quad A(C)Y(S_1).       \tag{1.2}
\]

A direct four-sector construction has one oriented old parent edge

\[
                    T^-_C\longrightarrow T^+_C,
 \qquad T^-_C\cap T^+_C=C.                         \tag{1.3}
\]

It has one of two modes.

* **Pure:** (1.1) and (1.2) are both pure and their unordered old endpoint
  pairs are the same pair `{T^-_C,T^+_C}`.
* **Attached:** (1.1) and (1.2) are both attached, with old endpoints
  `T^-_C` and `T^+_C`, respectively.  In particular they must be distinct.

This criterion is necessary and sufficient row by row.  In the audited
factor all 5,005 pure/attached mode decisions agree.  Among the 4,816 bad
pure rows, the two old endpoint pairs are disjoint 2,662 times and share one
endpoint 2,154 times.  Each of the 48 bad attached rows is a loop: its x and
y attached endpoints are the same old rank-eight set.

## 2. Exact distance lower bounds

Consider one bad pure row, with current old endpoint pairs `P_x` and `P_y`.
Any common target pair `P` obeys

\[
 |P_x\mathbin\triangle P|+|P_y\mathbin\triangle P|
 \ge |P_x\mathbin\triangle P_y|.                  \tag{2.1}
\]

Equality is attained rowwise by retaining either current pair.  A disjoint
pair therefore forces two selected incidences to be removed and two added;
a one-endpoint overlap forces one removal and one addition.  A bad attached
loop likewise forces one endpoint incidence to change.  Hence the rowwise
projection alone gives, relative to `H`, at least

\[
 2(2662)+1(2154)+1(48)=7526                       \tag{2.2}
\]

selected incidences removed.  Independently, every bad row must change at
least one of its two physical edges, proving the first bound 4,864.

The old parent arcs contributed by the 1,382 already-good attached rows must
form a partial directed 2-factor: no two can share a tail or a head.  Their
tail--head bipartite graph has maximum matching 1,370.  The audit freezes
both a matching of that size and a Kőnig vertex cover of that size, so this
is an exact certificate rather than a greedy count.  At least 12 good rows
must therefore change in addition to the 4,864 bad rows.  Each such change
removes at least one more selected incidence.  This upgrades the physical,
removed-incidence, and incidence-Hamming bounds to 4,876, 7,538, and 15,076,
respectively, proving (0.2)--(0.3).

The upper-q1 load audit sharpens the meaning of this distance.  Among the
4,816 bad pure rows, 2,693 have both current physical edges as the unique
provider of their respective upper target.  At least one edge in every such
row changes, so 2,693 distinct currently unique upper targets lose their
provider.  A passing repair must create a new provider for all of them.
This is a lower bound on provider transport, not an upper-q1 impossibility.

## 3. Alternating cycles are complete, but synchronization is not a flow

Let `B` be the bipartite containment graph whose left vertices are
rank-eight lower colours and whose right vertices are rank-nine owners.
A lower-rainbow 2-factor is exactly a Boolean incidence vector `y` satisfying

\[
 \sum_{v\supset c}y_{cv}=2\quad(c\in\tbinom{[17]}8),
 \qquad
 \sum_{c\subset v}y_{cv}=2\quad(v\in\tbinom{[17]}9).             \tag{3.1}
\]

The symmetric difference of any two solutions of (3.1) is Eulerian and
decomposes into alternating cycles.  Thus alternating-cycle switches form a
complete move basis: there is no additional invariant at lower q1.

Upper q1 is the exact quadratic decoration of this flow.  If
`S` is rank ten and `S-c={a,b}`, then `c` supplies `S` precisely when both
incidences to `c+a` and `c+b` are selected.  With witness variables this is

\[
 z_{c,S}\le y_{c,c+a},y_{c,c+b},\qquad
 \sum_{c\subset S}z_{c,S}\ge1.                    \tag{3.2}
\]

A switch is q1-safe exactly when every uniquely supplied target whose
provider is removed by the switch has an added or retained provider in
(3.2).  The 2,693 lower bound shows why independently improving the two
rails is the wrong model.

## 4. The smallest exact missing object

The direct common-parent subclass can be stated without reference to the
current factor.  It asks for:

1. an oriented lower-rainbow 2-factor `P` on `J(15,8)`: every old
   rank-seven colour `C` labels exactly one arc
   `T^-_C -> T^+_C`, and every old rank-eight owner has indegree and
   outdegree one;
2. a mode bit on every arc, with exactly 5,005 pure arcs and 1,430 attached
   arcs;
3. a cap-two incidence factor pairing the 5,005 pure `C`'s over all old
   rank-six colours `Z` (each `Z` selects two containing pure `C`'s and each
   pure `C` is selected twice); and
4. upper-q1 surjectivity (3.2) for the resulting four-sector child factor.

Once the parent arc and its mode are fixed, all x-, y-, and old-colour child
edges are forced by the four-sector formulas; the cap-two factor supplies
the `AA` edges.  This is therefore an exact finite object.

For a repair of the authenticated factor, the mode set and the cap-two
factor may both be frozen to their already valid values.  The smallest
remaining object is then an oriented lower-rainbow parent 2-factor using
those fixed 5,005 pure and 1,430 attached colours, such that its induced
x/y/old child edges satisfy (3.2).  The distance bounds in Section 2 apply
to every solution of this smaller problem.

It is **not** an ordinary single-commodity flow.  Choosing a parent arc
simultaneously consumes its colour, one tail slot, one head slot, the two
rail incidences, and—when pure—two cap-factor incidences.  Equivalently it is
a mode-decorated coloured directed 2-factor (a three-index assignment) with
the quadratic provider rows (3.2).  Proving or constructing this object is
the smallest common-parent rethread theorem missing after the present
audit.  Residence, deeper shadows, opening, and the lower compiler remain
downstream even if it exists.

## 5. Audit

Run

```text
python3 scratch/audit_k17_double_rainbow_parent_synchronization_20260731.py
```

It independently reconstructs all physical edges from the component file,
checks the exact lower and upper q1 palettes, performs the row projection,
and freezes the counts and distance bounds in

```text
scratch/k17_double_rainbow_parent_synchronization_20260731.audit.json
```

The scope is one authenticated factor and the direct common-parent
four-sector subclass.  No statement here rules out a different rethread or
an optimal K17 word outside that subclass.
