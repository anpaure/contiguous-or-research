# Open incidence-hexagon pair transport and fixed-size ring planting

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical local transport theorem and
fixed-size common-history-ring two-factor construction.  For every fixed
ring size `c`, both ring phases occur in spanning Middle-Levels two-factors
for all sufficiently large `m`, related by the zero-cost cyclic head
rethread.  The theorem does not make either factor Hamiltonian and does not
plant the full `c=m` ring or its complete witness reservoir.

No computation or search is used.

## 0. Boolean pair coordinates

Work in

\[
 \mathrm {ML}_m=
 \binom{[2m-1]}{m-1}\longleftrightarrow
 \binom{[2m-1]}m.
\tag{0.1}
\]

Let `B` have size `m-2`.  For an external pair

\[
 p\in\binom{[2m-1]\setminus B}{2}
\]

write

\[
 Y(p)=B\cup p.
\tag{0.2}
\]

For `d in B`, put

\[
 Z_d(p)=(B-d)\cup p.
\tag{0.3}
\]

If distinct pairs `p,q` share one label, then `p union q` has size three;
define

\[
 W_d(p,q)=(B-d)\cup(p\cup q).
\tag{0.4}
\]

All displayed sets have the appropriate middle ranks:

\[
 |Z_d(p)|=m-1,
 \qquad |Y(p)|=|W_d(p,q)|=m.
\]

## 1. The open half-hex

### Lemma 1.1 (one-step external-pair transport)

Let `|p cap q|=1`.  The three-edge path

\[
 \boxed{
 Z_d(p)-W_d(p,q)-Z_d(q)-Y(q)
 }
\tag{1.1}
\]

is a literal alternating augmenting path from the lower endpoint `Z_d(p)`
to the upper endpoint `Y(q)` when its middle edge

\[
 W_d(p,q)Z_d(q)
\tag{1.2}
\]

is old and the other two edges are new.

It lies on one incidence hexagon.  More precisely, if

\[
 p=\{r,s\},\qquad q=\{r,t\},
\]

then the hexagon has rank-`(m-2)` core

\[
 H=(B-d)+r
\]

and active labels `d,s,t`.

#### Proof

Every consecutive containment in (1.1) is literal.  Adding the first and
last edges and deleting (1.2) raises the degrees of the two endpoints by
one and preserves the degrees of the two internal vertices.

The six vertices of the containing hexagon are

\[
 \begin{array}{lll}
 H+s=Z_d(p),&H+d=B+r,&H+t=Z_d(q),\\
 H+d+s=Y(p),&H+d+t=Y(q),&H+s+t=W_d(p,q).
 \end{array}
\]

They are exactly the three lower and three upper vertices of the Boolean
incidence hexagon on active labels `d,s,t`.  Path (1.1) is one open half of
that hexagon. \(\square\)

The adjective **open** is load-bearing.  A closed hexagon toggle preserves
all six degrees and merely reverses an isolated three-cycle assignment.  The
open half-hex instead transports one unit of endpoint deficiency.

### Corollary 1.2 (diameter-two pair transport)

For any two distinct external pairs `p,q`, one lower unit at `Z_d(p)` can
be transported to the upper endpoint `Y(q)` by an alternating path with at
most two old edges and at most three new edges.

#### Proof

The graph on two-subsets in which two pairs are adjacent when they intersect
is the line graph of a complete graph and has diameter two.  If `p,q`
intersect, use Lemma 1.1.  If they are disjoint, choose

\[
 h=\{x,y\},\qquad x\in p,\quad y\in q.
\]

Then `p,h,q` is a length-two path.  Concatenating the two open half-hexes,
with the same missing core label `d`, gives

\[
 Z_d(p)-W_d(p,h)-Z_d(h)-W_d(h,q)-Z_d(q)-Y(q),
\tag{1.3}
\]

whose first, third, and fifth edges are new and whose second and fourth
edges are old. \(\square\)

### Corollary 1.3 (private bounded transport bank)

Fix `h` ordered source--target pair demands `(p_i,q_i)` with distinct source
pairs and distinct target pairs.  If `|B|>=h`, assign distinct missing core
labels `d_i in B`.  Then the transports in Corollary 1.2 can be chosen with
pairwise disjoint internal vertices.  They use at most `2h` old edges.

#### Proof

For a disjoint pair demand choose any cross-pair `h_i` as in Corollary 1.2.
Inside one route all pair states are distinct.  Between two routes, the
missing core labels `d_i` differ.  A set missing `d_i` and containing every
other element of `B` cannot equal one missing `d_j`.  The terminal uppers
`Y(q_i)` are distinct by hypothesis.  Thus all internal physical vertices
are private. \(\square\)

## 2. A one-half-hex-per-owner fixed ring

Now fix a ring size `c>=3`, independent of `m`.  Choose disjoint labels

\[
 b,a_0,\ldots,a_{c-1},z_0,z_1\notin B,
\tag{2.1}
\]

and retain any remaining coordinates as unused spares.  Put

\[
 I_i=B+a_i,
 \qquad
 L_i=B+b+a_i,
 \qquad
 R_i=B+a_{i-1}+a_i.
\tag{2.2}
\]

Take the old ring phase

\[
 P^- =\{I_iL_i,I_iR_i:i\in\mathbb Z_c\}.
\tag{2.3}
\]

There are two owner roles at root `I_i`.  Index them by

\[
 Y_{i,0}=L_i,
 \qquad
 Y_{i,1}=R_i,
\tag{2.4}
\]

and write their external pairs as

\[
 p_{i,0}=\{b,a_i\},
 \qquad
 p_{i,1}=\{a_{i-1},a_i\}.
\tag{2.5}
\]

Give them target pairs

\[
 q_{i,0}=\{a_i,z_0\},
 \qquad
 q_{i,1}=\{a_i,z_1\},
\tag{2.6}
\]

and target owners

\[
 U_{i,e}=Y(q_{i,e}).
\tag{2.7}
\]

Every source pair and every target pair is distinct, the two banks are
disjoint, and

\[
 |p_{i,e}\cap q_{i,e}|=1.
\tag{2.8}
\]

Choose `2c` distinct labels

\[
 d_{i,e}\in B.
\tag{2.9}
\]

For every role define

\[
 A_{i,e}=Z_{d_{i,e}}(p_{i,e}),
 \qquad
 C_{i,e}=Z_{d_{i,e}}(q_{i,e}),
\tag{2.10}
\]

and

\[
 W_{i,e}=W_{d_{i,e}}(p_{i,e},q_{i,e}).
\tag{2.11}
\]

### Theorem 2.1 (fixed-size ring two-factor planting)

If

\[
 \boxed{m\ge6c+2,}
\tag{2.12}
\]

then `ML_m` has a spanning two-factor `F^-` containing the entire ring
phase `P^-`.

Moreover

\[
 F^+=(F^-\setminus P^-)
       \cup\{I_iL_i,I_iR_{i+1}:i\in\mathbb Z_c\}
\tag{2.13}
\]

is simultaneously a spanning two-factor containing the cyclically
rethreaded ring phase.  No physical position is added by (2.13).

#### Proof

Form the following old protected incidence bank `D`:

\[
 \begin{aligned}
 D={}&\{I_iU_{i,e}:i\in\mathbb Z_c, e\in\{0,1\}\}\\
 &\cup\{Y_{i,e}A_{i,e}:i\in\mathbb Z_c, e\in\{0,1\}\}\\
 &\cup\{W_{i,e}C_{i,e}:i\in\mathbb Z_c, e\in\{0,1\}\}.
 \end{aligned}
\tag{2.14}
\]

It has exactly `6c` edges.  Every root `I_i` has degree two; all other
vertices in `D` have degree one.  Distinctness follows from the distinct
source pairs, target pairs, and missing core labels.  Hence

\[
 \Delta(D)\le2,
 \qquad |E(D)|=6c\le m-2.
\tag{2.15}
\]

The small protected-factor theorem extends `D` to a spanning two-factor
`F_0`.

Delete all edges of `D`.  Add the `2c` ring edges of `P^-`, and for every
role add the two new half-hex edges

\[
 A_{i,e}W_{i,e},
 \qquad
 C_{i,e}U_{i,e}.
\tag{2.16}
\]

Call the result `F^-`.  The degree check is local:

* `I_i` loses its two target-owner edges and gains its two ring edges;
* `Y_(i,e)` loses `Y_(i,e)A_(i,e)` and gains its ring edge;
* `A_(i,e)` loses the same edge and gains `A_(i,e)W_(i,e)`;
* `W_(i,e)` loses `W_(i,e)C_(i,e)` and gains
  `W_(i,e)A_(i,e)`;
* `C_(i,e)` loses `C_(i,e)W_(i,e)` and gains
  `C_(i,e)U_(i,e)`; and
* `U_(i,e)` loses `U_(i,e)I_i` and gains
  `U_(i,e)C_(i,e)`.

Every other vertex is unchanged.  Thus `F^-` is again a spanning
two-factor and contains `P^-`.

Finally `P^-` and the phase in (2.13) have the same degree at every ring
root and owner.  Replacing one by the other therefore preserves degree two
at every vertex, proving that `F^+` is a spanning two-factor. \(\square\)

### Corollary 2.2 (the three-ring bound)

For `c=3`, both phases of a common-history three-ring are plantable in
spanning two-factors for every

\[
 m\ge20.
\tag{2.17}
\]

The complete switch uses eighteen old and eighteen new incidence edges.
It is supported on six edge-disjoint incidence hexagons.  The two hexagons
assigned to one ring root share that root and no edge; all other physical
vertices are private.

### Corollary 2.3 (zero local word-length charge)

At the owner/factor level, the construction changes incidences only.  Once
the common ordered history is attached to the `c` hinges, the cyclic phase
change (2.13) has the exact short-deck and strict-lower-deck invariance of
the common-history ring theorem.  Hence this local topology preparation
adds no source position.

This corollary does not assert that the eighteen-edge preparation is
residence-, upper-, or cap-transparent.

## 3. Exact component effect of the transport hexagons

For every role `(i,e)`, its three old edges in (2.14) and its three new
edges in (2.16), together with the ring edge `I_iY_(i,e)`, are exactly the
two alternating phases of one incidence hexagon.  Indeed its three lower
vertices are

\[
 I_i,\quad A_{i,e},\quad C_{i,e},
\tag{3.1}
\]

and its three upper vertices are

\[
 U_{i,e},\quad Y_{i,e},\quad W_{i,e}.
\tag{3.2}
\]

The common rank-`(m-2)` core is

\[
 (B-d_{i,e})+a_i,
\tag{3.3}
\]

and the active labels are `d_(i,e)`, the non-`a_i` label of `p_(i,e)`, and
`z_e`.

Thus the construction gives an exact finite topology criterion.

### Theorem 3.1 (transport-hypertree Hamilton criterion)

Let `F_0` be a two-factor containing `D`.  Make a bipartite incidence graph
whose left vertices are the components of `F_0`, whose right vertices are
the `2c` transport hexagons, and where a component is incident with a
hexagon when it contains one of that hexagon's three old edges.

Suppose:

1. the three old edges of every selected hexagon lie on distinct current
   components whenever that hexagon is toggled; and
2. the component--hexagon incidence graph is a tree.

Then toggling all `2c` transport hexagons produces one Hamilton cycle
containing `P^-`.

More generally, if a forest of these hexagons is toggled, its component
effect is contraction of that forest.

#### Proof

The hexagons are edge-disjoint.  Two hexagons at the same ring root share a
vertex but use its two different old edges and its two different new edges;
their degree changes therefore commute.

Under condition 1, toggling a ternary incidence hexagon removes one edge
from each of three distinct cycles and reconnects the resulting paths into
one cycle, lowering the component count by two.  Process the right vertices
of the incidence tree in a leaf order.  The tree property ensures that the
three blocks met by the next hexagon are still distinct; otherwise the
already processed incidence edges would give a path between two of them and
the new hexagon node would close a cycle in the incidence graph.  Hence each
toggle contracts exactly its incident component blocks and splits none.
Induction identifies current physical components with the connected
components of the processed incidence forest.  At the end the incidence
tree is connected, so the physical factor is one cycle.  The forest form is
the same induction componentwise. \(\square\)

### Corollary 3.2 (sharp component capacity)

The `2c` transport hexagons can lower the component count by at most `4c`.
Consequently a Hamilton endpoint obtained using only these toggles requires

\[
 \boxed{|\operatorname {Comp}(F_0)|\le4c+1.}
\tag{3.4}
\]

For a three-ring, the bounded old factor must therefore have at most
thirteen components.  Condition (3.4) is only necessary; the exact positive
condition is the strict component-hypertree incidence in Theorem 3.1.

#### Proof

One incidence hexagon meets at most three old components, so one toggle
reduces their number by at most two.  Sum over `2c` toggles. \(\square\)

This is the rooted-spanning-forest boundary of the fixed-ring construction:
the pair transport itself is explicit, while a completion with the required
bounded, correctly distributed component state is not yet supplied by the
small protected-factor theorem.

## 4. What is and is not solved

Theorem 2.1 removes a real local obstruction:

\[
 \boxed{
 \text{for every fixed }c,
 \text{ a full }c\text{-ring has a bounded, literal, factor-plantable
 external-pair transport macro.}
 }
\tag{4.1}
\]

It also explains why the full-size ring remains different.  The old bank
has `6c` edges, so the present unconditional factor theorem applies only
when `6c<=m-2`; it cannot plant `c=m`.

The construction chooses its starting factor `F_0`.  It does **not** prove
that the old bank (2.14) lies in an arbitrarily prescribed Hamilton cycle.
For a frozen Hamilton cycle, a one-step route additionally requires the
middle old edge

\[
 W_d(p,q)Z_d(q)
\tag{4.2}
\]

to be an actual cycle occurrence for every demand.  Those occurrence
conditions are not consequences of ambient Boolean adjacency.  The
minimal one-layer surgery without (3.2) is exactly the rigidity/no-go in
`MATH_THEOREM_MINIMAL_HAMILTON_RING_SURGERY_RIGIDITY_20260804.md`.

Nor does an arbitrary two-factor extension control topology.  To finish a
joint phase cover, one still needs either

1. a completion `F_0` for which the switched `F^-` has a ring-rooted
   transparent pull host;
2. a completion for which `F^+` itself is Hamiltonian; or
3. a longer protected transport forest whose contracted component quotient
   is connected.

Thus the former local-wedge gate has been separated from the true remaining
gate:

\[
 \boxed{
 \text{bounded pair transport is available for fixed }c;
 \quad
 \text{rooted/Hamilton quotient control is still open.}
 }
\tag{4.3}

## 5. Self-audit

1. The source pairs in (2.5) are distinct for `c>=3`; the target pairs in
   (2.6) are distinct and contain a spare label absent from every source.
2. Condition `m>=6c+2` implies both `|B|=m-2>=2c` and the existence of the
   two spare external labels.
3. Distinct missing core labels make the six physical vertices belonging
   to different hexagon roles disjoint, apart from the deliberately shared
   ring roots, which have old and new degree two.
4. The old bank has exactly three edges per role and `2c` roles, hence
   `6c` edges.  Its maximum degree is two.
5. The displayed local degree ledger checks every vertex touched by the
   switch.  Old and new edge counts both equal `6c`.
6. Replacing `P^-` by `P^+` is degree-neutral because both phases use every
   root twice and every ring owner once.
7. A ternary hexagon decreases component count by at most two, giving the
   exact `4c+1` capacity bound.

No Hamiltonicity, component bound, upper-witness preservation, global
residence, or common-cap statement is hidden in the construction.

## 6. Dependencies

| role | file |
|---|---|
| small protected-factor theorem | `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md` |
| common-history phase rethread | `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md` |
| minimal frozen-Hamilton surgery obstruction | `MATH_THEOREM_MINIMAL_HAMILTON_RING_SURGERY_RIGIDITY_20260804.md` |
