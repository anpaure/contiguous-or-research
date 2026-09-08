# Pair-cell trace decomposition and the one-touch resident-dicut no-go

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  The note classifies
the intersection of two perfect-pairing cells inside one source cube and
proves that a residue-carrying resident nested difference needs at least two
distinct selected compensation cells meeting the source cell.  It also gives
an exact globally measurable non-power-of-two nested-difference calibration.
It does **not** construct the required two-touch object, an owner selector,
macro Hall, collar holonomy, a palette, or a compiler.

## 1. Pair cells and their overlay cycles

Let `R` and `Q` be perfect pairings of a finite coordinate set.  An
`R`-cell is specified by prescribing, for every pair `e in R`, an occupancy

\[
                         \rho_e\in\{0,1,2\}.                 \tag{1.1}
\]

On a fixed uniform layer, the occupancies sum to the layer rank.  The pairs
with occupancy one are the cube directions of the cell.  Thus a cell with
`m` singleton pairs is an induced copy of `Q_m`.

The multigraph `R union Q` is a disjoint union of even alternating cycles.
A common pair is regarded as an alternating cycle of length two, with its
`R`-edge and `Q`-edge retained as two labelled copies.

### Theorem 1.1 (exact trace decomposition)

Let `C` be an `R`-cell and `K` a `Q`-cell on the same uniform layer.  Then
`K cap C` is either empty or has the following form in the cube graph of
`C`:

\[
 \boxed{K\cap C\text{ is the disjoint union of }2^b
        \text{ induced }a\text{-faces, with no cube edge between them}.}
                                                                    \tag{1.2}
\]

Here

* `a` is the number of common `R,Q` pairs on which both cell records have
  occupancy one; and
* `b` is the number of nontrivial alternating components of `R union Q`
  on which every `R`- and `Q`-occupancy is one.

In particular,

\[
                  |K\cap C|=2^{a+b},                         \tag{1.3}
\]

and `K cap C` is connected in the cube graph of `C` if and only if `b=0`.
In that case it is one induced `a`-face.

#### Proof

Write `x_v in {0,1}` for membership of coordinate `v` in an owner.  On an
alternating component of `R union Q`, the two cell records impose equations

\[
       x_u+x_v=\rho_{uv}\quad(uv\in R),\qquad
       x_u+x_v=\kappa_{uv}\quad(uv\in Q),                    \tag{1.4}
\]

with right sides in `{0,1,2}`.

If any equation has right side zero or two, both of its endpoint variables
are fixed.  Propagation around the alternating cycle then fixes every
variable uniquely, or detects inconsistency.  If every right side is one,
each successive variable is the complement of the preceding one.  The
component is even, so there are exactly two complementary solutions.

Different alternating components use disjoint coordinates, hence their
choices are independent.  This already proves (1.3).  It remains to identify
the induced cube graph.

On a common pair, the two complementary solutions differ by flipping the
one corresponding singleton `R`-pair.  This is one edge direction of `C`.
Each free common pair therefore contributes one independent face direction.
On a nontrivial alternating component, the two complementary solutions
differ on every coordinate of a cycle of length at least four, and hence on
at least two singleton `R`-pairs.  They are not adjacent in `C`.  No cube
edge can change the choice on such a component.  Fixing the choices on all
`b` nontrivial free components leaves precisely the `a` common-pair choices,
which form an induced `a`-face.  The `2^b` resulting faces are pairwise
edge-isolated.  This proves (1.2) and the connectedness assertion. \(\square\)

### Corollary 1.2 (connected traces are powers of two)

If a single cell of any second perfect-pairing frame has nonempty connected
trace in `C`, that trace is one face of `C`, and its size is a power of two.

This applies whether or not the second cell is contained in `C`.  The
contained-cell isolation theorem is the special case in which the entire
second cell equals its trace.

## 2. An exact globally measurable calibration

The next construction shows that genuine nested differences of non-power
size do exist.  It is deliberately small and makes no residence claim.

Choose two source pairs

\[
 e_1=\{\alpha_0,\alpha_1\},\qquad
 e_2=\{\beta_0,\beta_1\}                                  \tag{2.1}
\]

of a perfect pairing `R`.  Let `C` be an `R`-cell in which `e_1,e_2` and
`a` further pairs are singleton; all remaining pairs have any fixed zero or
two occupancies compatible with the uniform layer.  Thus `C` is an
`(a+2)`-cube.

Take `P=R`.  Let `Q` agree with `R` away from (2.1), and replace those two
pairs by

\[
 \{\alpha_0,\beta_0\},\qquad \{\alpha_1,\beta_1\}.          \tag{2.2}
\]

Let `K` be the `Q`-cell which has occupancies two and zero, respectively,
on the pairs in (2.2), and has the same record as `C` on every other pair.
Then

\[
                K\subset C,qquad |K|=2^a.                  \tag{2.3}
\]

Indeed, (2.2) forces the selector choice
`{alpha_0,beta_0}`, while the `a` common singleton pairs remain free.

### Proposition 2.1 (the three-quarter nested difference)

On the complete uniform owner layer `V`, put

\[
             A=V\setminus C,qquad B=V\setminus K.           \tag{2.4}
\]

Then `A` is `P`-measurable, `B` is `Q`-measurable,

\[
             A\subset B,qquad B\setminus A=C\setminus K,   \tag{2.5}
\]

and

\[
                       |B\setminus A|=3\cdot2^a.             \tag{2.6}
\]

Moreover, `C` has a Hamilton cycle in which both `K` and `C-K` are cyclic
intervals.

#### Proof

The complements of cells are measurable in their respective cell
partitions.  Equation (2.3) gives (2.5), and (2.6) follows from
`|C|=2^(a+2)`.

For `a=1`, let `H` be the unique edge of `Q_1`.  For `a>=2`, delete one
edge `xy` from a Hamilton cycle of `Q_a` and call the resulting Hamilton
path `H`, directed from `x` to `y`.  Order the four
selector layers by the Gray cycle

\[
                         00,01,11,10.                         \tag{2.7}
\]

Traverse copies of `H` in alternating directions and join equal endpoints
by the selector edges of (2.7).  This is a Hamilton cycle of `Q_(a+2)` in
which every selector layer is consecutive.  Choose `K` as the `00` layer.
The other three consecutive layers form its complementary cyclic interval.
For `a=0`, the ordinary four-cycle of `Q_2` gives the same conclusion.
\(\square\)

This construction is globally honest: (2.4) are measurable subsets of the
entire uniform layer, not functions defined only after restriction to `C`.
It shows that the nested-difference gate itself does not force power-of-two
punctures.  Its failure at the target scale is exposed by the next theorem.

If three distinct pairing names are desired, `P` may be changed from `R`
on two source pairs which are both fixed zero in `C`, or both fixed two in
`C`, by the same four-coordinate re-pairing.  This leaves `C` as one
`P`-cell and leaves (2.4)--(2.6) unchanged.

## 3. The one-touch obstruction

Let

\[
       W_r=\binom{2r}{r},\qquad s=\nu_2(W_r),
       \qquad q_M=2^M,                                      \tag{3.1}
\]

with `M>s`.  Let `C` be a source `R`-cell of dimension `m>=M`, so
`|C|=2^m` is divisible by `q_M`.

Suppose `U` is a nonempty proper cyclic interval of a Hamilton cycle of
`C`.  An exact extension of `U` by whole cells from two other frames means
that selected whole cells are pairwise disjoint, disjoint from `U`, and
cover `V-U`.  Equivalently, by the exact dicut theorem, `U=B-A` for nested
measurable sets and the selected extension cells are the `P`-blocks in `A`
and the `Q`-blocks in `V-B`.

Call such an extension **one-touch at C** when exactly one selected whole
cell has nonempty intersection with `C`.

### Lemma 3.1 (small cubes have no long-resident Hamilton path)

If `D>=3` and `0<=a<D`, no Hamilton path of `Q_a` is simultaneously

1. internally `D`-resident, and
2. supported on at least `D` vertices.

Here internal residence means that equal transition directions in the
linear path word have index distance at least `D`.

#### Proof

For `a<=1`, the path has at most two vertices, fewer than `D`.  Assume
`2<=a<D` and write `L=2^a-1` for the number of transitions.  If `L<D`, all
transitions would have to use distinct directions, giving `L<=a`, contrary
to `2^a-1>a`.  If `L>=D`, the first `D` transitions would have to use
distinct directions, giving `D<=a`, again a contradiction. \(\square\)

### Theorem 3.2 (one-touch resident-dicut no-go)

Assume

\[
             D>=3,qquad s<D,qquad M>s.                      \tag{3.2}
\]

Let the source Hamilton cycle be `D`-resident, and require both `U` and its
complementary cyclic interval `C-U` to have at least `D` vertices.  If

\[
                         |U|\equiv W_r\pmod {2^M},            \tag{3.3}
\]

then no exact extension of `U` is one-touch at `C`.

Equivalently, every residue-carrying resident nested difference at this
scale needs at least two distinct selected compensation cells with nonempty
trace in the source cell.

#### Proof

Suppose `K` is the unique selected extension cell meeting `C`.  Exact
coverage gives

\[
                            C\setminus U=K\cap C.             \tag{3.4}
\]

The left side is the complementary cyclic interval of a Hamilton cycle and
is therefore connected in the cube graph of `C`.  Corollary 1.2 says that
it is one induced `a`-face, for some `a`, and

\[
                            |C\setminus U|=2^a.               \tag{3.5}
\]

Since `m>=M`, equations (3.3) and (3.5) imply

\[
                       2^a\equiv-W_r\pmod {2^M}.              \tag{3.6}
\]

The right side is nonzero modulo `2^M` and has exact two-adic valuation
`s`.  Hence `a<M` and comparison of valuations in (3.6) gives

\[
                                  a=s<D.                      \tag{3.7}
\]

Because all vertices of the face (3.4) occur consecutively on the source
Hamilton cycle, that segment is a Hamilton path of `Q_a`.  It inherits
internal `D`-residence from the source cycle and, by hypothesis, has at
least `D` vertices.  This contradicts Lemma 3.1. \(\square\)

### Corollary 3.3 (independent-anchor products cannot close the target)

Any construction in which the exterior compensation of one source interval
collapses, after all fixed zero/two anchors are imposed, to one physical
pair-cell trace is impossible under (3.2)--(3.3).  Tensoring independent
anchor gadgets does not change this conclusion unless at least two distinct
selected physical cells survive and meet `C`.

This is stronger than the former one-shore contained-cell obstruction.  The
unique compensating cell may cross the boundary of `C`; Theorem 1.1 still
forces its connected trace to be a face, and the valuation plus residence
argument still rules it out.

## 4. The sharpened positive target

The surviving problem is not merely to find `A subseteq B` with
`B-A subset C`.  It must use a genuinely compound trace:

\[
 \boxed{
 C\setminus U=(K_1\cap C)\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}(K_t\cap C),\qquad t\ge2,
 }                                                             \tag{4.1}
\]

where the `K_i` are selected cells from the two compensation shores, their
full cells are globally disjoint, and the union of their traces is one
`D`-resident cyclic interval.  Each individual trace is a disjoint union of
equal-dimensional faces by Theorem 1.1.  Therefore the next constructive
step is a **face-chain coupling theorem**: arrange at least two such traces
so that their union and complement are both connected intervals, while the
full cells still form one global zero--zero/one--one-free dicut.

No conclusion about existence or nonexistence of that compound object is
made here.
