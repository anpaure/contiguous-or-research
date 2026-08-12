# Audit and two exact refinements of the `K17` residual-port switch calculus

Date: 2026-07-31  
Status: independent mathematical audit and scoped exact refinements; no
`K17` upper-complete or resident carrier is claimed

## 0. Verdict

The switch calculus in

```text
MATH_THEOREM_R_K17_RESIDUAL_PORT_CIRCUIT_TURN_TRANSPORT_20260731.md
```

is correct in its frozen-macro scope.  In particular:

1. residual integral `b`-flow circuits are directed alternating cycles;
2. lower-`q1` and all owners are preserved automatically;
3. Hamiltonicity is exactly the connectedness of the retained-fragment/new-
   seam transition graph;
4. an incidence hexagon is Hamilton-safe exactly when none of its three new
   seams closes one retained fragment by itself; and
5. the upper rank-ten derivative is the literal occurrence transport
   formula at the touched port colours.

One precision correction is incorporated in the theorem: a provider search
must seed an ordered corner `U+ -> T -> U-`, not merely the unused incidence
`U+ -> T`.  When `T` has two selected pure incidences, the selected first
return arc chooses which owner is evicted and therefore which opposite
endpoint and upper target are fixed.  With that ordered-corner convention,
the directed return-path bijection is exact.

The exact frozen `C6` census also passes source-level audit.  The count and
scope are

\[
 7225=3625+2703+897,
\]

where the three summands give one, two, and three factor components after
the toggle.  Among the `3625` Hamilton-safe rows, the complete
`(filled,lost)` table in the JSON gives `1711` lossless rows and `1121`
strict net improvements.  The lossless rows split as

\[
 793+711+192+15=1711
\]

according as they fill `0,1,2,3` previously missing upper colours.

The rest of this note records two useful consequences not needed for that
audit: an exact run-counting monoid and a conserved upper first moment.

## 1. Setup

Let

\[
 {cal T}=\binom{[15]}8,\qquad {cal U}=\binom{[15]}9.
\]

Contract the `1430` fixed `A/X/Y` paths to macro blocks.  Together with the
`5005` singleton `U` blocks and the `6435` colour vertices in `T`, the frozen
carrier is one bipartite Hamilton cycle.  Macro incidences are fixed.  A
residual flow `x` selects two facets of every `U` and has prescribed colour
degrees

\[
 \deg_x(T)=d_T=2-\deg_{\cal P}(T).
\]

Orient a selected containment `T-U` as `T -> U` and an unselected legal
containment as `U -> T`.  A simple directed cycle deletes its selected arcs
and inserts its unselected arcs.

## 2. Exact fragment theorem

Let a balanced trade delete a set `R` of selected incidences and insert a set
`B` of unselected incidences, with equal deleted and inserted degree at every
`U` and every `T`.  Delete `R` from the old Hamilton cycle and regard the two
ends of every resulting retained path as labelled half-ports.  Let
`K(R,B)` be the multigraph obtained by contracting the retained paths and
inserting the links in `B`.

> **Theorem 2.1 (exact monodromy).**  The toggled residual factor is a
> Hamilton cycle if and only if `K(R,B)` is connected.  Equivalently, every
> nonempty proper union of retained fragments has a new link leaving it.

The proof is literal contraction and expansion.  Degree balance makes
`K(R,B)` two-regular, and expansion preserves its component count.

For a simple alternating hexagon, `R` has three edges and the old cycle is
cut into three retained paths.  A loop of `K(R,B)` is a separate component.
Conversely, a loopless two-regular multigraph on three vertices is the
triangle.  This proves the advertised no-loop criterion in both directions.
For four or more fragments, absence of loops is not sufficient; the full
subtour condition is indispensable.

## 3. Boolean hexagons and their upper derivative

The rank-eight/rank-nine containment graph has no `C4`: two distinct
rank-nine sets have at most one common rank-eight facet.  Every simple `C6`
therefore has a unique rank-seven kernel `K` and three distinct outside
coordinates `a,b,c`.  In one orientation it replaces

\[
\begin{array}{ccl}
K+a+b:&K+a&\longmapsto K+b,\\
K+b+c:&K+b&\longmapsto K+c,\\
K+c+a:&K+c&\longmapsto K+a.
\end{array}
\]

The reverse orientation reverses these three replacements.  This
parameterization is unique, so the source loop counts every applicable
hexagon once.

At a touched colour `T`, let `U^-` be the removed pure owner, `U^+` the
inserted pure owner, and `N_T` the unchanged physical owner on the other
side of the port.  The only changed upper occurrence is

\[
                  U^-\cup N_T\longmapsto U^+\cup N_T.       \tag{3.1}
\]

Both sides have rank ten and are adjacent in `J(17,10)`.  Hence, if `m(Q)`
is the full physical multiplicity and `o(Q),i(Q)` count the old and new
occurrences in a packet, then

\[
                  m'(Q)=m(Q)-o(Q)+i(Q).                     \tag{3.2}
\]

This validates the census implementation: a colour is lost exactly when
the right side of (3.2) is zero, and an initially missing colour is filled
exactly when its `i(Q)` is positive.  Additions which cancel removals and
repeated added labels are therefore handled correctly.

There is no hidden provider choice once the evicted incidence is fixed.
Choose a selected arc `T -> U-` to delete, and let \(N_T\) be the other
physical owner at \(T\).  For a prescribed rank-ten target \(Q\), an
incidence entering \(T\) can create \(Q\) if and only if

\[
 N_T\subset Q,\qquad Q\setminus N_T=\{c\}
 \text{ with }c\in[15]\setminus T,                 \tag{3.3}
\]

and the uniquely determined pure owner \(U^+=T+c\) is not already selected
at \(T\).  Thus the atomic provider datum is the ordered corner

```text
U+ -> T -> U-
```

and not the added incidence alone.  At a colour of residual degree two the
two possible choices of `U-` generally give two different anchors and two
different upper signatures.

The audited artifacts are

```text
scratch/audit_r_k17_residual_flow_c6_decoration_20260731.py
scratch/k17_residual_flow_c6_decoration_20260731.audit.json
```

with SHA-256 values, at audit time,

```text
efeade2d5df9e1d2c4b6f1bffafde927cbf9265dd08d6cac717bd9748eefa033
ac201ac3cf2dee747a6a654a7de696135df093f02d7116174058f4094392523a
```

respectively.

The extended payload also cuts the common `45`-incidence support of the
fifteen maximum hexagons once and enumerates its complete `2^15` option
cube as two matchings on `90` labelled boundary occurrences.  This is the
same exact contraction theorem, not a second topology proxy.  It gives
`10270` Hamilton states, of which `10128` have a Hamilton-safe prefix
ordering.  The best reachable state uses thirteen hexagons and fills `39`
distinct holes without loss, leaving `1852`; the displayed thirteen-step
order is therefore a literal sequence of legal residual circuits.

## 4. A conserved first moment of every residual flow

For a selected pure incidence `U-T`, let its **moving tag** be the unique
coordinate in \(U\setminus T\).  Write \(1_S\) for the
coordinate-incidence vector of a set \(S\).  Then every feasible residual
flow satisfies

\[
\begin{aligned}
 \sum_{(U,T)\in x} e_{U\setminus T}
 &=\sum_{(U,T)\in x}(1_U-1_T)\\
 &=2\sum_{U\in{\cal U}}1_U-\sum_{T\in{\cal T}}d_T1_T.    \tag{4.1}
\end{aligned}
\]

The right side is independent of `x`.

> **Proposition 4.1 (upper first-moment invariant).**  Throughout the whole
> fixed-macro residual `b`-flow fibre, the moving-tag histogram and hence the
> coordinate-degree vector of the complete physical rank-ten upper-turn
> multiset are invariant.

Indeed the base contribution `sum_T 1_T`, the macro endpoint tags, and all
internal macro turns are fixed, while the pure incidence-tag contribution is
(4.1).  Equivalently, on every alternating circuit the multiset of entering
coordinate tags and the multiset of departing tags have equal coordinate
counts.

In fact the coordinate-degree conclusion has a source-independent proof for
every exact lower-rainbow factor on the full owner deck.  In dimension
`2m+1`, fix a coordinate `z`.  There are

\[
 M=\binom{2m}{m}
\]

rank-`m+1` owners containing `z`.  If `E_11` is the number of factor edges
whose two endpoints contain `z`, lower-colour bijectivity gives

\[
 E_{11}=\binom{2m}{m-1}=M-\operatorname{Cat}_m.
\]

The degree sum over the `z`-containing owners gives

\[
 2M=2E_{11}+E_{10},
\]

where `E_10` counts crossing edges.  Therefore the number of upper-turn
occurrences containing `z` is

\[
 E_{11}+E_{10}=M+\operatorname{Cat}_m.              \tag{4.2}
\]

For `m=8`, (4.2) is `14300` in every one of the seventeen coordinates.
A complete rank-ten palette uses
`C(16,9)=M-Cat_8=11440` such occurrences, so the unavoidable surplus is
`2 Cat_8=2860` per coordinate.  Thus this first moment is a useful invariant
and audit identity, but it does **not** obstruct ordinary upper coverage in
the present exact-owner/lower-rainbow setting; any obstruction must occur at
higher correlation or at the circuit/topology level.

## 5. Exact residence/run state

For a cyclic owner word `W` and coordinate `z`, a short positive run is an
occurrence of one of

\[
                        010,\qquad0110,\qquad01110.         \tag{5.1}
\]

For a linear binary fragment `w`, define

\[
 S_4(w)=\bigl(\min(|w|,4),\operatorname{pref}_4(w),
 \operatorname{suff}_4(w),n_1(w),n_2(w),n_3(w)\bigr),       \tag{5.2}
\]

where `n_l(w)` is the number of linear occurrences of `0 1^l 0` wholly
inside `w`.  When two fragments are concatenated,

\[
 n_l(uv)=n_l(u)+n_l(v)+
 \#\{0\,1^l\,0\text{ crossing the }u|v\text{ boundary}\}. \tag{5.3}
\]

The last term is determined by `suff_4(u)` and `pref_4(v)`, and the new
prefix and suffix are determined by the same stored data.  Thus (5.2) is an
exact associative finite monoid.  After all fragments are joined, the
cyclic wrap terms are again determined by the final suffix and prefix.

> **Proposition 5.1 (exact run derivative).**  For any balanced residual
> packet, its exact length-one/two/three positive-run counts are determined
> by the transition pairing of Theorem 2.1 and the seventeen summaries
> (5.2) of every retained fragment in both orientations.  No interior replay
> is needed.

This is stronger than a Boolean residence flag: it gives the exact change
in the defect count.  For a general required minimum run `d+1`, replace four
by `d+1` and store the counts of `0 1^l 0`, `1<=l<=d`.

There is also a structural simplification.

> **Lemma 5.2 (no singleton run in a lower-rainbow cycle).**  A cyclic
> Johnson owner factor whose consecutive rank-eight intersections are all
> distinct has no positive coordinate run of length one.

If `x` occurs only at owner `U` in such a run, both neighbours omit `x`, so
the two incident lower colours are both \(U\setminus\{x\}\), a
contradiction.  Every residual switch preserves the exact lower palette, so this remains true
after every legal packet.

The finite boundary state can change boundary-touching length-two and
length-three runs, but it cannot change a pattern whose closed support lies
strictly inside a frozen macro.  The authenticated family has `605` such
length-three runs.  More strongly, every rank-six occurrence transversal of
this fixed parent retains at least `165` forced internal length-three runs.
Therefore no residual `b`-flow switch, no compound residual packet, and no
mere change of the occurrence transversal can make this fixed parent
flat-depth-three resident.

The separately frozen exact occurrence optimization sharpens `165` to
`180`: a literal transversal attains `180`, and the retained bound-179 DRAT
proof independently checks `UNSAT`.  The extra fifteen are a coupled
integrality effect; the solver-free `165` remains the dimension-uniform
forced-packet certificate.

## 6. Exact constructive and obstructive boundary

The authenticated carrier has `24310` upper-turn occurrences, `17557`
distinct rank-ten colours, and `1891` holes.  Its scalar surplus is

\[
                         24310-17557=6753.
\]

A packet deleting `t` residual incidences changes at most `t` port turns,
so any packet filling all current holes has

\[
                              t\ge1891.                     \tag{6.1}
\]

The fifteen audited fill-three/loss-zero hexagons show that the local ratio
three filled colours per three deleted incidences is attained.  Their
supports are pairwise disjoint and their combined upper signature fills
`44` distinct holes without a loss, but the simultaneous transition graph
has four cycles.  Thus even disjointness, individual Hamilton safety, and
perfect local provider efficiency do not imply compound Hamiltonicity.

The complete `2^15` transition cube is small enough to replay exactly and
also gives a positive compound statement.  Of its `32768` states, `10270`
are Hamiltonian and `10128` are reachable from the empty state by adding one
hexagon at a time while every prefix remains Hamiltonian.  The mask `31735`
uses the thirteen hexagons

```text
0,1,2,4,5,6,7,8,9,11,12,13,14
```

and has a safe application order

```text
14,13,12,9,11,8,7,6,5,4,2,1,0.
```

Its `39` new upper labels are distinct and none of its removed labels is
lost, so it gives a literal sequential lower-rainbow Hamilton descent from
`1891` to `1852` rank-ten holes.  This is a finite positive calibration,
not a scalable completion theorem; the all-fifteen terminal state itself
has four components.

The smallest exact deterministic repair formulation is consequently:

1. a balanced directed circulation in the residual incidence digraph;
2. all fragment subtour cuts from Theorem 2.1;
3. the multiplicity inequalities (3.2); and
4. if one scores boundary residence, the finite monoid state (5.2).

The first three rows are necessary and sufficient for a lower-rainbow
Hamilton switch with the requested upper-q1 gains.  Row four scores exactly
what this fixed fibre can alter, but the immutable-run theorem proves that
no accepting flat-residence state exists in the fibre.  Deeper upper/lower
shadows and the common-cap compiler are not controlled by these statements.

For an augmenting-path implementation, a desired provider is an **ordered
corner**, not merely one unused incidence.  If the closing arc is
`U+ -> T`, the first arc of the complementary path is a selected incidence
`T -> U-`; this choice specifies which old singleton is evicted and hence
which other incidence at `T` remains the anchor in (3.1).  When `d_T=2`, the
same unused arc can have two different turn signatures according to this
first path arc.  Once the ordered corner is fixed, residual circuits through
it are exactly the simple directed paths from `T` back to `U+`, with that
first arc prescribed, subject to the fragment and multiplicity acceptance
states above.
