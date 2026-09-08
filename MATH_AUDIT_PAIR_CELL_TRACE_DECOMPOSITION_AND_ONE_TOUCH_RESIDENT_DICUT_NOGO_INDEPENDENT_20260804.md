# Independent audit: pair-cell traces and the one-touch resident-dicut no-go

**Date:** 2026-08-04  
**Verdict:** **PASS without mathematical correction.**  
**Method:** direct Boolean-equation, cube-graph, valuation, and residence
arguments only; no search, solver, H100, or numerical experiment was used.

## 1. Frozen source and exact scope

Audited theorem:

`MATH_THEOREM_PAIR_CELL_TRACE_DECOMPOSITION_AND_ONE_TOUCH_RESIDENT_DICUT_NOGO_20260804.md`

SHA-256:

`0d6c01f6d5a37c1858d99112f5f58d73b59ebc102cf86830650961f40a12f15c`

The theorem proves a **one-touch** no-go: after a resident interval is
preselected in one source cell, an exact whole-cell extension cannot have
only one selected compensation cell meeting that source cell.  It does not
rule out two or more compensation traces, punctured compensation cells, or
the compound two-shore face-chain target stated in Section 4.

## 2. Alternating-component equation audit

The overlay of two perfect pairings is a disjoint union of alternating even
cycles; a common pair is correctly treated as a length-two cycle with two
labelled parallel edges.  On one overlay component, simultaneous membership
in an `R`-cell and a `Q`-cell is exactly the binary system

\[
 x_u+x_v=\rho_{uv}\quad(uv\in R),
 \qquad
 x_u+x_v=\kappa_{uv}\quad(uv\in Q).
\]

If one right side is zero or two, both endpoint bits are fixed.  Alternating
propagation then either fixes the full component uniquely or finds an
inconsistency.  If every right side is one, each bit is the complement of
the previous bit; even cycle length gives exactly two complementary
solutions.  The uniform-layer condition creates no additional coupling:
every `R`-edge already has its prescribed occupancy, so the total selected
rank is fixed by the `R`-record.

Different overlay components have disjoint coordinates, so their solution
choices multiply.  This proves the cardinality `2^(a+b)` whenever the trace
is nonempty.

## 3. Induced faces and edge isolation

On a free common pair, the two complementary solutions differ in exactly
one singleton `R`-pair.  That choice is one genuine cube direction of the
source cell.  The `a` such choices are independent and span an induced
`a`-face.

On a free nontrivial alternating component, the two solutions differ on
every coordinate and hence on every singleton `R`-pair of that component.
A nontrivial overlay cycle contains at least two `R`-pairs, so the two
solutions have source-cube Hamming distance at least two.  No source-cube
edge can switch that component choice.  After fixing all `b` nontrivial
choices, the common-pair choices give one induced face; different choices
give pairwise edge-isolated faces.

Thus

\[
 K\cap C=\dot\bigcup_{1}^{2^b}Q_a
\]

as an induced subgraph, and its trace is connected exactly when `b=0`.
This applies to a cell that crosses the boundary of `C`; containment is not
used.  Corollary 1.2 is therefore strictly stronger than the earlier
contained-cell isolation statement and is valid.

## 4. Global three-quarter calibration

Re-pairing the two singleton source pairs as

\[
 \{\alpha_0,\beta_0\},\qquad
 \{\alpha_1,\beta_1\}
\]

and prescribing occupancies two and zero forces the selector choice
`{alpha_0,beta_0}`.  The other `a` common singleton pairs remain free, so
the resulting `Q`-cell `K` is contained in `C` and has size `2^a`.

With `P=R`,

\[
 A=V\setminus C
\]

is a union of complete `P`-cells.  Likewise

\[
 B=V\setminus K
\]

is a union of complete `Q`-cells.  Since `K subset C`, one has

\[
 A\subset B,
 \qquad B\setminus A=C\setminus K,
 \qquad |B\setminus A|=3\cdot2^a.
\]

The measurability is global on the full uniform layer, not defined only
inside `C`.

The Hamilton-cycle calibration also replays.  For `a>=1`, choose a
Hamilton path `H` of `Q_a` from `x` to `y`, order the four selector layers
as

\[
 00,01,11,10,
\]

and traverse successive copies of `H` in alternating directions.  Equal
endpoints join by the indicated selector edge, and the last copy closes to
the first.  Each selector layer is one cyclic interval.  Taking `K` to be
the `00` layer makes the other three layers the complementary interval.
For `a=0`, the ordinary four-cycle supplies the same conclusion.  Hence the
calibration really is a non-power-of-two nested difference with an honest
Hamilton interval.

The optional distinct-name modification of `P` is correctly conditional:
re-pairing two source pairs which are both fixed zero, or both fixed two,
leaves `C` as one `P`-cell.  It is not needed for Proposition 2.1.

## 5. Exact meaning of one touch

Let `U` be the preselected proper interval.  In an exact extension, all
selected whole compensation cells are mutually disjoint, disjoint from
`U`, and cover `V-U`.  If exactly one such cell `K` meets the source cell
`C`, then exact coverage restricts to

\[
 C\setminus U=K\cap C.
\]

The left side is the complementary cyclic interval, hence is connected by
the source Hamilton-path edges.  The trace theorem therefore forces it to
be one induced `a`-face and to have size `2^a`.  Notice that `K` need not be
contained in `C`; only its trace is used.  This confirms the claimed gain
over the older one-shore contained-cell no-go.

## 6. Valuation step

Since `m>=M`, the source-cell size `2^m` vanishes modulo `2^M`.  The residue
hypothesis and the trace size give

\[
 2^a=|C\setminus U|
 \equiv-|U|
 \equiv-W_r\pmod {2^M}.
\]

Write `W_r=2^s w` with `w` odd and `s<M`.  The right side is nonzero modulo
`2^M` and has exact valuation `s`.  Hence `a<M`; if `a` differed from `s`,
the two terms in `2^a+W_r` would have valuation `min(a,s)<M`, contradicting
the congruence.  Therefore

\[
 a=s<D.
\]

No assumption that the least positive residue itself is a power of two is
being made.

## 7. Residence boundary audit

The complementary interval lists every vertex of the induced `a`-face
consecutively.  Every consecutive source-cycle edge with both endpoints in
that induced face is an internal face edge.  Thus the segment is a Hamilton
path of `Q_a` and inherits internal `D`-residence from the source cycle.

For `a<=1`, the face has at most two vertices, fewer than `D>=3`.  For
`2<=a<D`, write `L=2^a-1` for its number of transitions.

* If `L<D`, any repeated direction would have gap below `D`, so all
  transitions would be distinct; this would force `L<=a`, contrary to
  `2^a-1>a`.
* If `L>=D`, the first `D` transitions must be pairwise distinct, forcing
  `D<=a`, again a contradiction.

This exhausts all possible `a=s<D`.  The hypothesis that both source
intervals have at least `D` vertices is stronger than the contradiction
needs on the `U` side, but is the correct symmetric macro-block interface
and creates no logical gap.

## 8. Corollary and surviving target

The independent-anchor corollary is correctly stated in physical terms:
an algebraic tensor product does not evade the theorem if all exterior
compensation still materializes as one selected pair cell meeting `C`.
The theorem says nothing once at least two distinct selected cells survive.

In that surviving case, exact coverage gives a disjoint union

\[
 C\setminus U=dot\bigcup_i(K_i\cap C),
\]

and each trace is itself a disjoint union of equal-dimensional induced
faces.  Requiring at least two traces whose union is one resident cyclic
interval, while their full cells remain globally disjoint and satisfy the
zero-zero/one-one-free dicut, is therefore the precise next construction
problem.

**Final independent verdict: PASS.**  No two-touch existence theorem,
owner selector, macro Hall, collar holonomy, palette, compiler, or
`B(k)+O(1)` conclusion follows.
