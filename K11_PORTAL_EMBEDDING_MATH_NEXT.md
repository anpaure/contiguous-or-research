# Mathematical reduction of the corrected `k=11` portal branch

## 1. Outcome

There are three rigorous conclusions.

1. The proposed `q=13` partial switch cannot put the twelve missing
   rank-seven masks and `958` into its first thirteen portal cells.  The
   obstruction is already visible in `J(11,7)`: the twelve rank-seven masks
   have six connected components, whereas one rank-eight portal can split a
   consecutive rank-seven colour walk into at most two pieces.
2. Mixed triple/quadruple central schedules have an exact coordinate-run
   factorization criterion.  With a fixed three-entry boundary state there is
   a similarly exact extension criterion.  Thus this branch does not require
   a raw factor SAT instance merely to test factorability.
3. The `369/93` two-path problem with all 462 rank-five labels has a standard
   global source: cut a Hamilton cycle of the eleven-dimensional middle
   levels graph into arcs containing 369 and 93 rank-six vertices.  The
   remaining graph-theoretic gate is a **prescribed-path extension problem**
   in the middle levels graph.

The explicit `q=19` prefix in `K11_PARTIAL_SWITCH_PREFIX_NEXT.md` passes an
independent direct OR check.  A compatible 56-vertex beginning of its
rank-six suffix is also given below.  Neither object is yet a full array.

Throughout, write

\[
 R_t(i)=A_i\cup A_{i+1}\cup\cdots\cup A_{i+t-1}.
\]

## 2. Portal colours form a Johnson walk

### Lemma 2.1 (consecutive portal-colour lemma)

Suppose

\[
 P_i=R_3(i),\qquad 1\le i\le q,
\]

are distinct rank-six masks, and put

\[
 U_i=R_4(i),\qquad 1\le i\le q.
\]

If `U_i` and `U_(i+1)` are distinct rank-seven masks, then they are adjacent
in `J(11,7)`, and

\[
 P_{i+1}=U_i\cap U_{i+1}.                    \tag{2.1}
\]

This applies also to `i=q-1`: the last portal `R_4(q)` is the mixed-delay
seam, but it still shares the rank-six triple `P_q` with `R_4(q-1)`.

#### Proof

Both four-windows contain the shared triple:

\[
 P_{i+1}=R_3(i+1)\subseteq U_i\cap U_{i+1}.
\]

The two distinct seven-sets therefore have intersection of size at least six
and at most six.  Equality follows, proving both claims.  ∎

There is a small but important lift condition.  Given three successive
rank-seven colours `U_(i-1),U_i,U_(i+1)`, the two forced facets

\[
 U_{i-1}\cap U_i,\qquad U_i\cap U_{i+1}
\]

must be different.  Otherwise the two central triples on the sides of portal
`U_i` coincide and their union is only rank six.  Thus a simple path in
`J(11,7)` is not quite enough; it must be nonbacktracking at the level of the
removed element.

### Corollary 2.2 (component bound)

Let a portal sequence contain required rank-seven colours whose induced
subgraph in `J(11,7)` has `c` components.  Suppose the sequence also uses `s`
extra rank-seven connector colours and `h` colours of ranks other than seven.
Then necessarily

\[
 c\le s+h+1.                                 \tag{2.2}
\]

Indeed, delete the `s+h` non-required positions from the linear colour
sequence.  At most `s+h+1` blocks remain, and Lemma 2.1 puts every block in a
single component of the required-colour graph.

## 3. The `q=13` plan is impossible

The twelve missing rank-seven masks are

\[
 251,493,607,941,956,1267,1468,1694,1763,1884,1946,1990.
\]

Their induced `J(11,7)` graph has exactly the following six components:

\[
\begin{aligned}
 &251-1267-1763,\\
 &493-941-956-1468,\\
 &1694-1946,\\
 &\{607\},\quad\{1884\},\quad\{1990\}.
\end{aligned}                                  \tag{3.1}
\]

This is checked simply by taking pairwise intersections: adjacency means
intersection rank six.

In the proposed `q=13` schedule, the thirteen portal cells are exactly the
twelve rank-seven omissions and the one rank-eight mask `958`.  Removing the
`958` position leaves at most two consecutive rank-seven blocks.  Equation
(3.1) requires six.  Corollary 2.2 gives the contradiction

\[
 6\le0+1+1=2.
\]

Hence the exact `q=13` proposal is impossible, independently of factorability
or lower-mask pinning.

More generally, even before factorability, one rank-eight portal requires at
least four additional rank-seven connector colours.  If `958` is fixed at the
right seam rather than used internally, it does not split the ordinary-colour
walk, and at least five connectors are necessary.

## 4. Exact factorization of a one-switch central schedule

Let selected central intervals be

\[
 I_i=\begin{cases}
 [i,i+2],&i\le q,\\
 [i,i+3],&i>q,
 \end{cases}                                   \tag{4.1}
\]

with prescribed target masks `C_i`.  No rank or adjacency hypothesis is
needed in the following theorem.

### Theorem 4.1 (mixed-delay run criterion)

There is an array `A` satisfying

\[
 \bigcup_{j\in I_i}A_j=C_i\qquad(1\le i\le M)
\]

if and only if, for every coordinate, each maximal incidence one-run
`[a,b]` that touches neither end of the target row obeys

\[
 b-a+1\ge
 \begin{cases}
 3,&a\le q+1,\\
 4,&a\ge q+2.
 \end{cases}                                   \tag{4.2}
\]

Runs touching either boundary may be shorter.

#### Proof

Work with one coordinate.  Write `r_i` for the right endpoint of `I_i`, so

\[
 r_i=i+2\quad(i\le q),\qquad r_i=i+3\quad(i>q).
\]

For an internal positive run `[a,b]`, the preceding zero interval ends at
`r_(a-1)` and the following zero interval begins at `b+1`.  Therefore the
positions on which the coordinate may be placed are exactly

\[
 [r_{a-1}+1,b].                                \tag{4.3}
\]

Every positive interval in the run meets (4.3), so taking all its positions
realizes the run, exactly when (4.3) is nonempty.  This says

\[
 b-a+1\ge r_{a-1}-a+2,
\]

which is three when `a-1<=q` and four otherwise.  A boundary run has no zero
interval on one side and is always realizable.  Coordinates are independent,
so the conditions are sufficient simultaneously.  ∎

This theorem explains a small amount of extra flexibility at the switch: an
internal run beginning at `q+1` may have length three even though all selected
windows from there onward have length four.

## 5. Exact continuation criterion for the certified prefix

The certified `q=19` prefix fixes

\[
 A_{20}=4,\qquad A_{21}=32,\qquad A_{22}=514.  \tag{5.1}
\]

Let

\[
 D_t=R_4(19+t),\qquad 1\le t\le443,
\]

be the desired remaining rank-six row.  More generally, let `F_1,F_2,F_3`
be fixed first factor entries for a length-four window row
`D_1,...,D_N`.

### Theorem 5.1 (fixed-boundary extension criterion)

An extension by free entries from position four onward exists exactly when
the following hold coordinatewise.

1. Fixed occurrences do not contaminate a negative window:

   \[
   F_1\subseteq D_1,\quad
   F_2\subseteq D_1\cap D_2,\quad
   F_3\subseteq D_1\cap D_2\cap D_3.          \tag{5.2}
   \]

2. Every internal one-run has length at least four.
3. If an initial one-run is finite and has length `ell=1,2,3`, then its
   coordinate belongs to `F_ell`.

#### Proof

Condition (5.2) is immediate from which first windows contain each fixed
position.  For an internal run the legal pin interval is the fixed-delay
version of (4.3), so length four is necessary and sufficient.

Suppose an initial run ends at `ell<N`.  The following zero window starts at
`ell+1`, so every legal pin is at a factor position at most `ell`.  The last
positive window starts at `ell`; hence it can only be hit by position `ell`.
If `ell<=3`, this is the fixed entry `F_ell`.  If `ell>=4`, that position and
enough preceding positions are free.  Right-boundary runs are handled by free
positions after their last start.  Choosing legal pins independently for each
coordinate proves sufficiency.  ∎

For (5.1), condition (5.2) becomes

\[
 550\subseteq D_1,\qquad546\subseteq D_2,
 \qquad514\subseteq D_3,                      \tag{5.3}
\]

and the three short initial-run constraints are equivalently

\[
\begin{aligned}
 D_1\setminus D_2&\subseteq4,\\
 (D_1\cap D_2)\setminus D_3&\subseteq32,\\
 (D_1\cap D_2\cap D_3)\setminus D_4&\subseteq514.
\end{aligned}                                  \tag{5.4}
\]

These formulas are an exact boundary signature, not merely necessary tests.

## 6. Independent check of the `q=19` prefix

The ordinary portal colours are

```text
493 941 956 892 1884 1878 1990 1735 1763
1267 251 127 607 671 1694 1946 1438 1468
```

and the central triples are

```text
489 429 940 828 860 1876 1862 1734 1731 1251
243 123 95 543 670 1690 1434 1436 444
```

The factor entries are

```text
489 425 424 300 780 788 836 1604 1602 1218 195
99 83 27 30 538 154 1176 408 4 32
```

Direct enumeration gives all nineteen displayed triple ORs and all eighteen
displayed quadruple ORs exactly.  They are respectively distinct rank-six and
distinct rank-seven masks.  Appending `514` gives

\[
 R_4(19)=958,qquad A_{20}\cup A_{21}\cup A_{22}=550.
\]

Thus all twelve missing rank-seven masks and the missing rank-eight mask occur
in a factorable 22-entry local prefix.  Six of the eighteen ordinary portal
colours are connectors.  It is one portal cell above the seam-specific
component lower bound and one ordinary edge above the metric-optimal
factorability search reported in `K11_PARTIAL_SWITCH_PREFIX_NEXT.md`.

## 7. A compatible beginning of the 443-vertex suffix

The boundary conditions (5.3)--(5.4) are not an obstruction.  One may start

\[
 D_1,D_2,D_3,D_4=686,683,1675,1929.           \tag{7.1}
\]

These are distinct rank-six masks outside the nineteen-mask prefix, they form
a Johnson path, and they obey (5.3)--(5.4).  Continue after `1929` with
positions 6 through 50 of `k11_lower956_upper549.txt`:

\[
 1937,1944,1820,\ldots,993,739.
\]

The resulting 49-vertex row has no internal coordinate one-run shorter than
four.  Its only trailing runs shorter than four are

\[
 \text{bit }0:\ 2,qquad
 \text{bit }1:\ 1,qquad
 \text{bit }9:\ 3.                            \tag{7.2}
\]

It can therefore be joined, without a run defect, to the existing segment

\[
 723,691,571,1593,1833,1836,1452.             \tag{7.3}
\]

Indeed `739` and `723` intersect in five bits; the first three vertices in
(7.3) continue exactly the short runs in (7.2).  Through (7.3), all 56
vertices remain distinct, all adjacencies are Johnson adjacencies, and no
internal one-run has length below four.

At the new endpoint `1452`, the unresolved short suffix signature is

\[
 \text{bit }2:\ 2,qquad
 \text{bit }7:\ 1,qquad
 \text{bit }8:\ 3.                            \tag{7.4}
\]

Thus the next three vertices must contain respectively

\[
 \{2,7,8\},\qquad\{2,7\},\qquad\{7\}.         \tag{7.5}
\]

This is a concrete, local continuation problem.  It also shows why merely
permuting the old path components is insufficient: path-end adjacency and
the three-step run signature must be satisfied simultaneously.

The partial suffix in this section is not claimed to preserve all rank-five
colours.  In fact it shares the rank-five edge colour `852` with the prefix.
The partial-switch schedule has 350 unused short cells, so this collision is
not itself fatal, but all lower masks must eventually be recertified.

## 8. The `369/93` ledger is a cut middle-levels cycle

Let `ML_11` be the bipartite inclusion graph whose vertices are the rank-five
and rank-six subsets of `[11]`.  A Hamilton cycle can be written cyclically as

\[
 V_1,F_1,V_2,F_2,\ldots,V_{462},F_{462},V_1,
\]

where every `V_i` has rank six, every `F_i` has rank five, and

\[
 F_i=V_i\cap V_{i+1}.                          \tag{8.1}
\]

The middle-levels theorem guarantees that such cycles exist.

### Theorem 8.1 (cut-cycle construction)

Cut a middle-levels Hamilton cycle at two rank-five vertices so that one arc
contains 369 rank-six vertices and the other contains 93.  Projecting onto
the rank-six vertices gives two disjoint Johnson paths `P,Q` with

\[
 |P|=369,\qquad |Q|=93.                        \tag{8.2}
\]

Their internal intersection colours are all distinct and number

\[
 368+92=460.
\]

The two cut rank-five vertices are the two remaining colours and are facets
of the corresponding path endpoints.  Hence the 460 internal colours plus
the two endpoint facets exhaust all 462 rank-five masks exactly once.

Conversely, if two such paths have two unused rank-five endpoint facets that
join their four ends crosswise, inserting those facets reconstructs a
middle-levels Hamilton cycle.

This theorem exactly explains the valid `368+92+2=462` part of the saturated
`369/93` blueprint.  It is stronger than the endpoint requirements of the
blueprint, because each cut colour is incident to an endpoint on both sides.

Under complementation, the same cycle is a Hamilton cycle on the rank-five
layer whose consecutive **union** colours exhaust all rank-six masks.  A
prescribed rank-seven portal on the rank-six side becomes a prescribed
rank-four intersection colour on the complementary side.

## 9. The precise graph-theoretic extension target

The nineteen rank-six masks in Section 6 and their eighteen distinct
rank-five intersections form a simple alternating path of 37 vertices in
`ML_11`.  If this prescribed alternating path extends to a Hamilton cycle of
`ML_11`, then:

1. all twelve desired rank-seven portal edges lie on one rainbow rank-five
   central cycle;
2. one can choose a 93-rank-six cut arc disjoint from the prescribed
   nineteen-vertex rank-six block, leaving that block inside the 369-vertex
   arc; and
3. the complementary 93-vertex block and all 462 rank-five short labels are
   reserved automatically by Theorem 8.1.

There is no bipartite cardinality obstruction.  Removing the prescribed
alternating path leaves 443 rank-six and 444 rank-five vertices, exactly the
parity needed for an alternating path connecting its two free sides.

The missing theorem is therefore sharply stated:

> **Prescribed middle-level path extension problem.** Does the explicit
> 37-vertex alternating path of Section 6 extend to a Hamilton cycle of
> `ML_11`, with the two cut positions chosen outside that path?

Ordinary middle-levels Hamiltonicity does not answer this prescribed-path
question.  Nor does Hamilton-connectedness of the projected Johnson graph:
the rank-five colours must also remain distinct.

## 10. Safe path-splicing operations

Two elementary operations are useful for attacking the extension problem.

### Lemma 10.1 (oriented segment splice)

Delete the prescribed rank-six vertices from a known Johnson path.  Its
remaining vertices form disjoint path segments.  If the segments can be
ordered and independently reversed so that every new pair of endpoints is
Johnson-adjacent, their concatenation is a Hamilton path of the induced
remaining graph.  Every old edge and every longer shadow window wholly inside
a segment is preserved.  Only windows meeting a new join require checking.

For delay three, reversing a segment preserves its internal coordinate-run
lengths.  Therefore a new forbidden run must meet a join and can be detected
from the last three and first three incidence vectors at that join.

### Lemma 10.2 (Johnson-square merge)

Let two path components contain edges `XY` and `X'Y'` that are opposite sides
of a four-cycle in `J(11,6)`.  Replacing those edges by `XX'` and `YY'` (or by
`XY'` and `YX'`, according to orientation) merges or rearranges the two path
components while preserving every vertex.

Such squares arise explicitly as follows.  Write

\[
 X=C\cup\{a\},\qquad Y=C\cup\{b\},\qquad |C|=5.
\]

Choose `c in C` and `z` outside `C union {a,b}` and put

\[
 X'=(C\setminus\{c\})\cup\{a,z\},\qquad
 Y'=(C\setminus\{c\})\cup\{b,z\}.
\]

Then `X,Y,Y',X'` is a Johnson four-cycle.  Colour and run constraints at its
two new joins remain local checks.

In `k11_lower956_upper549.txt`, the nineteen prescribed prefix vertices occur
at one-based positions

```text
86 103 117 152 160 165 178 183 193 216
218 239 268 275 276 296 405 413 454
```

and deleting them leaves nineteen nonempty path segments.  Keeping the old
linear order already fails at fifteen joins.  A finite exhaustive check of
all orders and orientations of these nineteen intact segments also finds no
valid concatenation, even before imposing run signatures.  This diagnostic is
not used in any general theorem above, but it proves that this particular
checkpoint needs at least one additional cut or relocation.  Johnson-square
or three-edge relocation moves, together with the local run signature, are
therefore the appropriate next layer.

## 11. Exact remaining gates

The corrected branch has passed more than a local colour count, but it has not
yet solved `k=11`.  The remaining requirements are:

1. **Central completion.** Extend the nineteen-mask prefix through the other
   443 rank-six masks, either by the prescribed middle-level cycle theorem or
   by an explicit mixed-delay suffix.
2. **Boundary factorability.** Satisfy Theorem 5.1 at the fixed tail `550` and
   the length-four run condition at every later splice.  Equations
   (7.1)--(7.5) give one certified beginning.
3. **Lower coverage and pins.** The sparse prefix deliberately duplicates some
   short OR values.  All masks of ranks one through five must be reassigned to
   physical windows and pass the exact coordinate pin-survival test.
4. **Upper preservation.** The thirteen repaired masks were omissions of a
   different fixed-delay factor.  All formerly present upper witnesses must be
   preserved or independently rebuilt after the path surgery.
5. **Nonempty entries.** A coordinatewise factor may leave empty physical
   positions; the final pin choice must cover every position.

The main mathematical simplification is now clear:

\[
\boxed{
\text{portal embedding + rank-five ledger}
\quad\Longrightarrow\quad
\text{prescribed-path extension in }ML_{11}.
}
\]

The `q=13` shortcut is impossible, while the certified `q=19` prefix is a
valid prescribed path.  What remains is a global extension and pinning
theorem, not another local portal-count argument.
