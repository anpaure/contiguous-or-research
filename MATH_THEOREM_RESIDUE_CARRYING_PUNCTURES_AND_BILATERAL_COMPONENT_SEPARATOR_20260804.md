# Residue-carrying pair-cell punctures and the bilateral component separator

**Date:** 2026-08-04  
**Status:** unconditional arithmetic and owner-incidence theorems.  The note
proves that one proper cyclic interval has enough local length freedom to
carry the complete two-adic defect, and gives an exact component criterion
for extending any such puncture by whole blocks from two other frames.  It
does **not** prove that a residue-compatible cyclic interval satisfies that
component criterion, macro Hall, collar holonomy, an upper palette, or a
compiler.

## 1. A neutral cut does not evade the two-adic obstruction

Put

\[
             V=\binom{[2r]}r,\qquad W_r=|V|=\binom{2r}r,
             \qquad s=s_2(r)=\nu _2(W_r).                 \tag{1.1}
\]

Fix a good-cell dimension threshold `M>s` and write

\[
                         q_M=2^M.                            \tag{1.2}
\]

Every whole good pair cell has cardinality divisible by `q_M`.

Call a collection of path blocks cut from one source cell **support-neutral**
when their vertex sets partition that entire cell.  This definition does not
require the paths to have equal lengths or to be consecutive pieces of one
particular cycle.

### Proposition 1.1 (neutral-cut obstruction)

No partition of `V` can be made from whole good cells and support-neutral
collections cut from whole good cells.

Consequently, merely opening selected cell cycles into paths for a macro
splice does not bypass the whole-cell obstruction.  At least one source cell
must be selected non-neutrally: the selected paths cover a proper subset of
that cell and the omitted owners are covered from other frames.

#### Proof

Group the selected path blocks by source cell.  Every support-neutral group
has total cardinality equal to the size of its source cell, hence is divisible
by `q_M`.  The same is true of every selected whole cell.  Their disjoint union
would therefore have cardinality divisible by `q_M`, whereas
`nu_2(W_r)=s<M`.  \(\square\)

This is stronger than the observation that a degree-preserving switch tree
cannot repair owner support.  Arbitrarily many cuts and arbitrary path
lengths remain useless if each cut source is selected in its entirety.

## 2. One puncture has exactly the required arithmetic freedom

Let

\[
             \omega=W_r\bmod q_M,\qquad 1\le\omega<q_M.          \tag{2.1}
\]

Since `nu_2(W_r)=s<M`, reduction modulo `2^M` preserves the exact
valuation:

\[
                         \nu _2(\omega)=s.                    \tag{2.2}
\]

Suppose an owner partition uses exactly one proper block `B` and every
other selected block is a whole pair cell of dimension at least `M`.  Then

\[
             |B|\equiv\omega\pmod {q_M},
             \qquad \nu _2(|B|)=s.                            \tag{2.3}
\]

Thus a one-puncture selector would pay the two-adic defect sharply, not just
with valuation at most `s`.

The next lemma shows that (2.3) creates no local path-length obstruction.

### Lemma 2.1 (two-sided resident residue interval)

Let `D>=1`.  Assume

\[
                         q_M\ge2D                              \tag{2.4}
\]

and let a source good cell have dimension `m>=M+1`.  Put `N=2^m`.
There is an integer

\[
              b\equiv\omega\pmod {q_M},qquad
              D\le b\le N-D.                                \tag{2.5}
\]

In fact one may take

\[
 b=
 \begin{cases}
   \omega,&\omega\ge D,\\
   \omega+q_M,&\omega<D.
 \end{cases}                                                 \tag{2.6}
\]

If the cell carries a cyclic `D`-resident Hamilton ordering, any `b`
consecutive vertices form an internally `D`-resident proper path block, and
the complementary `N-b` consecutive vertices form another internally
`D`-resident proper path block.  Both blocks have at least `D` vertices,
and hence at least `D-1` internal edges.

#### Proof

When `omega>=D`, take `b=omega`.  Since `N>=2q_M`,

\[
                     N-b\ge2q_M-(q_M-1)=q_M+1\ge D.
\]

When `omega<D`, take `b=omega+q_M`.  Then `b>=D`, and

\[
             N-b\ge2q_M-q_M-(D-1)=q_M-D+1\ge D+1
\]

by (2.4).  This proves (2.5).  A contiguous subword of a resident transition
word is resident.  Cutting a cycle at the two boundary edges of the chosen
interval gives the two claimed paths. \(\square\)

In the intended local-cube regime, `M` is itself at least a constant multiple
of the residence deadline, so (2.4) is extremely loose.  The lemma says that the
two-adic obstruction has been completely localized: arithmetic permits one
long puncture and one long complement.  It says nothing about reallocating
the complement to other cells.

## 3. Exact extension theorem for arbitrary punctures

The reallocation problem has a clean component formulation which is valid
for arbitrary partitions, not just pair cells.

Let `P,Q,R` be three partitions of a finite universe `V`.  Mark some blocks
of `P` and `Q` as available.  In distinct `R`-blocks choose pairwise disjoint
preselected pieces

\[
                         U_1,\ldots,U_t,                       \tag{3.1}
\]

where a piece may be the whole `R`-block or a proper subset, and put

\[
                         U=U_1\mathbin{\dot\cup}\cdots
                           \mathbin{\dot\cup}U_t.              \tag{3.2}
\]

For every `P`-block `A` with `A-U` nonempty, create a left vertex `A`, and
for every `Q`-block `B` with `B-U` nonempty, create a right vertex `B`.
Join them when

\[
                         (A\cap B)-U\ne\varnothing.            \tag{3.3}
\]

Call such a residual vertex **forbidden** when its original block was
unavailable or met `U`.  Meeting `U` forbids the entire original block,
because the extension is allowed to select only whole `P`- and `Q`-blocks.

### Theorem 3.1 (punctured two-frame component criterion)

The pieces (3.1) extend to an exact cover of `V` by adding available whole
blocks from `P` and `Q` if and only if no connected component of the
residual graph (3.3) contains

* a forbidden `P`-vertex, and
* a forbidden `Q`-vertex.

#### Proof

For every residual owner in `(A cap B)-U`, exact coverage is the equation

\[
                         x_A+y_B=1.                            \tag{3.4}
\]

An unavailable block or a block meeting `U` cannot be selected, so its
variable is fixed to zero.  Along a connected component of (3.3), equations
(3.4) force all left variables to one common value `c` and all right
variables to `1-c`.  A forbidden left vertex forces `c=0`; a forbidden
right vertex forces `c=1`.  These requirements are compatible exactly under
the stated component condition.  If neither shore is forced, choose either
`c=0` or `c=1`.  Every variable is then binary, the selected original
blocks are disjoint from `U`, and (3.4) covers every residual owner once.
Adding the preselected pieces covers all of `V` exactly.

Conversely, any exact extension supplies a binary solution of (3.4).
One component cannot contain zero variables on both shores, proving the
necessity. \(\square\)

The theorem permits any number of whole selected `R`-blocks and any number
of proper punctures.  It is an exact generalization of the whole-third-frame
deletion criterion: a proper piece is treated literally, rather than as if
its whole source block had been selected.

## 4. The owner-edge form and the multicut obstruction

There is a useful equivalent picture.  Form the bipartite multigraph
`Gamma(P,Q)` whose vertices are the blocks of `P` and `Q`, and whose edge
labelled by `v in V` joins the two blocks containing `v`.  Preselecting `U`
deletes exactly the owner edges labelled by `U`.  A surviving vertex is
forbidden precisely when it was initially unavailable or is incident with a
deleted owner edge.

Thus Theorem 3.1 says:

\[
 \boxed{\text{after deleting the preselected owner edges, no residual
 component may contain forbidden vertices on both shores.}}   \tag{4.1}
\]

This gives a sharp obstruction even when every `P`- and `Q`-block is
initially available.

### Corollary 4.1 (every genuine puncture is a bilateral multicut)

Assume all `P`- and `Q`-blocks are initially available, and assume every
block meeting `U` also contains at least one owner outside `U`.  If `U`
extends by whole `P`- and `Q`-blocks, then for every deleted owner edge
`e in U`, the two endpoints of `e` lie in different connected components
of `Gamma(P,Q)-U`.

More strongly, every residual component is of one of three types:

1. it contains touched `P`-blocks but no touched `Q`-block;
2. it contains touched `Q`-blocks but no touched `P`-block; or
3. it contains no touched block.

Every deleted owner edge joins components of the first two opposite types.

#### Proof

Both endpoints of a deleted edge are touched and, by hypothesis, survive in
the residual graph.  If they belonged to one residual component, that
component would contain a forbidden vertex on each shore, contradicting
Theorem 3.1.  The same theorem gives the three component types.  Each
deleted edge has a touched left and a touched right endpoint, hence joins
opposite types. \(\square\)

### Corollary 4.2 (edge-connectivity lower bound)

Under the hypotheses of Corollary 4.1, if `Gamma(P,Q)` is
`lambda`-edge-connected, then every nonempty extendible puncture obeys

\[
                              |U|\ge\lambda.                   \tag{4.2}
\]

In particular, if `Gamma(P,Q)-U` remains connected, no nonempty puncture is
extendible.

#### Proof

Corollary 4.1 says that deletion of `U` disconnects the endpoints of every
edge of `U`; in particular it disconnects the graph.  The definition of
edge connectivity gives (4.2). \(\square\)

This is the incidence price hidden by the scalar congruence.  Under the
survival hypothesis of Corollary 4.1, a cyclic interval is not useful merely
because its length is correct: the full preselected owner-edge set `U` must
be a globally saturated bilateral separator.  Without that hypothesis,
touched blocks wholly contained in `U` disappear from the residual graph,
and the exact statement is the component criterion of Theorem 3.1 rather
than the stronger endpoint-separation conclusion.

## 5. Exact one-puncture reduction for pair-cell frames

Fix `D>=1`.  Take three perfect-pairing frames on `[2r]`, and declare a pair cell
available when its dimension is at least `M`.  Fix in the third frame

* a dimension-`m` available cell `C`, with `m>=M+1`;
* a cyclic `D`-resident Hamilton ordering
  `z_0,z_1,...,z_(2^m-1)` of `C`; and
* any family `S` of other whole available cells from that frame.

Assume for this section that `q_M>=2D`.  This guarantees both that the
admissible interval family below is nonempty and that every available whole
cell has at least `D` vertices.

For a start `a` and a length `b`, write

\[
 I(a,b)=\{z_a,z_{a+1},\ldots,z_{a+b-1}\},                    \tag{5.1}
\]

with cyclic indices.  Let `omega` be (2.1), and restrict to

\[
 b\equiv\omega\pmod {q_M},qquad D\le b\le2^m-D.                 \tag{5.2}
\]

Lemma 2.1 proves that admissible lengths exist.

### Theorem 5.1 (one-puncture selector equivalence)

There is an owner partition consisting of

* one proper resident interval `I(a,b)` satisfying (5.2);
* all whole cells in `S`; and
* whole available cells from the first two frames

if and only if, for some admissible `(a,b)`, the preselected set

\[
                  U=I(a,b)\ \mathbin{\dot\cup}
                    \bigcup_{C'\in S}C'                       \tag{5.3}
\]

satisfies the bilateral component condition of Theorem 3.1.

#### Proof

Necessity of the congruence in (5.2) follows by reducing the cardinality of
the owner partition modulo `q_M`; every selected block other than `I(a,b)`
has size divisible by `q_M`.  The two length bounds are part of the stated
class of allowed intervals, and internal residence follows by restriction
of the cyclic resident ordering, as in Lemma 2.1.  For a fixed
choice of `(a,b)`, Theorem 3.1 is exactly the necessary and sufficient
condition for the remaining owners to be partitioned by whole available
blocks of the first two frames.  Taking the existential quantifier over all
admissible intervals proves the equivalence. \(\square\)

The theorem answers the scalar part of the one-puncture question
positively and isolates its exact incidence part.  It does not assert that
such an interval separator always exists.  When `S` is empty and every
block touched by the interval survives deletion, Corollary 4.1 says that
the interval itself must be an edge multicut, not a generic sample of the
correct size.  With nonempty `S`, that corollary applies to the full set
`U` in (5.3); without the survival hypothesis, Theorem 3.1 is the exact
criterion and no stronger multicut claim is made.

## 6. What remains after the owner partition

Suppose Theorem 5.1 supplies an owner partition, and in addition equip every
selected whole cell with a cyclic `D`-resident Hamilton ordering.  (The
owner-partition theorem does not construct these orderings; they must come
from the separate local good-cell theorem.)  Open each such cycle at one
edge, and keep the interval `I(a,b)` as a path.  The interval has at least
`D` vertices by (5.2), and every whole-cell block has at least
`q_M>=2D` vertices.  Thus every resulting path has at least `D` vertices,
equivalently at least `D-1` internal edges, and is internally `D`-resident.
This is exactly the block-length convention `ell_i>=D-1` in the macro
theorem.  That theorem may then be applied at its sharp threshold:

1. build the literal seam-safe connector digraph on these blocks;
2. prove its bipartite Hall inequalities; and
3. for balanced or relabelled collars, prove the selected cycle-cover
   holonomy has a fixed point, or prove a flat transport gauge.

A perfect macro matching then gives a spanning resident cycle factor; a
loopless directed Hamilton cycle in the seam graph gives one component.

These rows do not follow from Theorem 5.1.  In particular, the two boundary
collars of the residue interval are arbitrary histories of the source cube
cycle.  Large local dimension may make each seam feasible prospectively,
but simultaneous physical labels and cycle holonomy remain global data.

The selector frontier is therefore the following exact three-stage object:

\[
 \boxed{
 \begin{array}{c}
 \text{one low-valuation resident interval}\\
 +\ \text{bilateral component separator in the other two frames}\\
 +\ \text{macro Hall and collar holonomy for the selected blocks}.
 \end{array}}                                                \tag{6.1}
\]

The first row is unconditional under the stated size bound and assumed local
cyclic ordering.  The second row is characterized exactly but not proved to
have a solution.  The third row remains the resident splice theorem already
isolated at macro scale.
