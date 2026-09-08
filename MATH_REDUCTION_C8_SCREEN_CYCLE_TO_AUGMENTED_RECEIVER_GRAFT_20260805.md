# The common-history `C8` is a Middle-Levels matching cycle, not a cyclic receiver-sector cycle

**Date:** 2026-08-05  
**Method:** active-screen projection and symmetric difference of matchings;
no computation or search  
**Status:** corrected fail-closed reduction.  The active
screens do form an alternating Johnson `C8`, but Johnson adjacency is not
the same as the adjacent-token-transfer edge relation in the paired
receiver sector.  In particular, the four old edges would require the
single label `b` to be cyclically adjacent to four distinct `a_i`, which is
impossible in a cycle.  Therefore the claimed direct reduction to the
existing augmented receiver Hall/Tutte graph is false without an additional
embedding/lift theorem.  The correct physical toggle is instead a matching
exchange in the Middle-Levels incidence graph.  Its unrooted protected
factor extension is known; relative PBBS locality and the rooted return
remain open.

## 1. The active screen graph

Fix the rank-`(r-2)` common core `B` and the five active coordinates

\[
                         \Omega=\{b,a_0,a_1,a_2,a_3\}.
\tag{1.1}
\]

For `i in Z_4`, put

\[
 A_i=\{b,a_i\},
 \qquad
 D_i=\{a_{i-1},a_i\}.                              \tag{1.2}
\]

The eight sets in (1.2) are distinct vertices of `J(Omega,2)`.  Define

\[
 M_0=\{A_iD_i:i\in\mathbb Z_4\},
 \qquad
 M_1=\{A_iD_{i+1}:i\in\mathbb Z_4\}.                \tag{1.3}
\]

### Lemma 1.1 (screen `C8`)

The eight-edge graph `M_0 union M_1` is the alternating cycle

\[
 A_0,D_0,A_3,D_3,A_2,D_2,A_1,D_1,A_0.              \tag{1.4}
\]

Both `M_0` and `M_1` are perfect matchings of its eight vertices.  The
statement concerns this selected eight-edge **Johnson** subgraph; the
ambient `J(Omega,2)` has additional chords.  No adjacent-token-sector
claim is included.

#### Proof

The old edge incident with `D_i` is `A_iD_i`; the new edge incident with
`D_i` is `A_(i-1)D_i`.  Hence every displayed vertex has degree two in the
union.  Following alternately old and new edges subtracts one from the
tail index, which has order four.  This gives (1.4), one cycle of length
eight.  `square`

The lift of a screen `S` is the rank-`r` owner `B union S`.  The old and new
hinge edges then have lower and upper q1 colours

\[
\begin{aligned}
 (B+A_i)\cap(B+D_i)&=B+a_i,\\
 (B+A_i)\cap(B+D_{i+1})&=B+a_i,                    \tag{1.5}\\
 (B+A_i)\cup(B+D_i)&=B+b+a_{i-1}+a_i,\\
 (B+A_i)\cup(B+D_{i+1})&=B+b+a_i+a_{i+1}.          \tag{1.6}
\end{aligned}
\]

Thus the lower colours agree pointwise and the upper colours are cyclically
permuted.

## 2. Exact receiver-sector obstruction

In the cyclic capacity-two token graph, a vertex is a two-subset of a
cyclic cut set and an edge moves one token to an adjacent empty cut.  If
the Johnson edge `A_iD_i` from (1.3) were such a receiver edge, the move
would replace `b` by `a_(i-1)`.  Hence `b` and `a_(i-1)` would have to be
adjacent in the cut cycle.

### Proposition 2.1 (no literal cyclic-sector embedding)

For distinct `a_0,a_1,a_2,a_3`, the old matching `M_0` is not a matching
of any cyclic adjacent-token capacity-two sector with the displayed
literal representatives.

#### Proof

The four edges `A_iD_i` would require the single cut `b` to be adjacent to
all four distinct cuts `a_(i-1)`.  A vertex of a simple cycle has degree
two.  `square`

Passing to unpointed necklace orbits does not repair the literal
common-history packet: independently rotating one endpoint also rotates
the common core and ordered history.  A quotient argument would need an
additional pointed screen-order lift supplying one coherent set of
literal representatives.  No such lift is proved here.

## 3. The correct Middle-Levels matching exchange

Put

\[
 I_i=B\cup\{a_i\},\qquad
 L_i=B\cup A_i,\qquad R_i=B\cup D_i.
\tag{3.1}
\]

The old hinge in the Middle-Levels incidence graph is

\[
 L_i-I_i-R_i,
\tag{3.2}
\]

whereas the new hinge is

\[
 L_i-I_i-R_{i+1}.
\tag{3.3}
\]

Thus the four left incidences `L_iI_i` are fixed.  On the bipartite graph
between the four facets `I_i` and the four heads `R_i`, the old right bank

\[
 N_0=\{I_iR_i:i\in\mathbb Z_4\}
\tag{3.4}
\]

and the new right bank

\[
 N_1=\{I_iR_{i+1}:i\in\mathbb Z_4\}
\tag{3.5}
\]

are complementary perfect matchings of one alternating `C8`.

### Theorem 3.1 (exact owner/q1 resource toggle)

Let a spanning Middle-Levels two-factor contain the complete old collar,
and hence the incidences (3.2).  Replacing (3.4) by (3.5):

1. leaves degree two at every owner and facet;
2. preserves the owner vertex set and lower-q1 facet set exactly; and
3. cyclically permutes the four immediate-upper hinge colours.

The conclusion remains true with all common core-excursion edges of the
biresident screen lattice protected.

#### Proof

The fixed incidences `L_iI_i` and either one of (3.4)--(3.5) give degree
two at every hinge facet.  Both right banks are perfect matchings of the
same eight incidence vertices, so the toggle preserves every degree.
Equations (1.5)--(1.6) give the two palette statements.  All excursion
edges are common to the phases and are untouched.  `square`

The small protected-factor theorem embeds the old collar as an unrooted
two-factor whenever its protected incidence size is at most `m-2`.  It
does not keep a prescribed PBBS factor outside an `O(d)` neighbourhood and
does not impose the return permutation below.

## 4. The topology row is separate and exact

Delete the four hinge edges from a directed factor and label the complete
right continuations by their tail roles.  Let `sigma in S_4` send a role
to the next selected role reached along its old continuation.  Toggling
the active `C8` applies the head cycle

\[
                         \tau=(0\ 1\ 2\ 3),                   \tag{4.1}
\]

so the new component permutation is `tau sigma`.

### Proposition 4.1 (rooted return condition)

The declared two-component-to-one crossover occurs exactly on the rooted
face

\[
                         \sigma=(0\ 2)(1\ 3),                 \tag{4.2}
\]

because then

\[
                         \tau\sigma=(0\ 3\ 2\ 1)             \tag{4.3}
\]

is one cycle.

An unrooted protected-factor extension of the old Middle-Levels collar need
not impose (4.2).  The complete PBBS graft therefore needs one rooted
graphic condition: the four protected continuation sockets must be paired
in that order.  Equivalently, after contracting the four protected collar
paths, the selected residual factor must realize the prescribed two-cycle
return minor.

#### Proof

The cut-permutation formula is the standard complete-continuation
rethread law.  Substitution gives (4.3).  Perfect matching controls degrees
and endpoint use but not which remote protected socket lies on the same
factor component, so it does not determine `sigma`.  `square`

## 5. Consequence and remaining scope

The former collar-grafting gate separates into two exact rows:

1. **Middle-Levels local matching exchange:** extend the fixed left
   incidences and old right matching while changing the PBBS factor only
   on an `O(d)` alternating-linkage support; and
2. **rooted graphic return:** enforce (4.2) in that residual factor.

Once the old collar is embedded, no further q1 collision theorem is needed
for its toggle.  What is not automatic is the embedding relative to the
fixed PBBS body.  The terminal permutation switches in the FIFO macro
construction and the Catalan connector graphic-rank formulation remain
possible mechanisms for the rooted row.

This reduction does not prove the relative PBBS matching extension, the
rooted return condition, exterior arbitrary-width upper protection, the
typed common cap, or a quiet opening.  It must not be cited as an
application of the paired-receiver Hall/Tutte theorem.

## 6. Dependencies

The literal lift is

`MATH_THEOREM_BIRESIDENT_COMPOUND_C8_SCREEN_LATTICE_20260805.md`.

The unrooted protected-factor theorem is

`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.

The paired-receiver theorem concerns a different cyclic adjacent-token
graph and is relevant only to delimit the obstruction:

`MATH_THEOREM_PAIRED_RECEIVER_SQUARE_AUGMENTATION_AND_EVEN_LEVEL_TU_20260805.md`.
