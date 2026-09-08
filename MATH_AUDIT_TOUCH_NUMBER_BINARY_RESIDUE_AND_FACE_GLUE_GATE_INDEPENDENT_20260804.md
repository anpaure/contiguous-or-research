# Independent audit: touch number, binary residue, and face glue

**Date:** 2026-08-04  
**Verdict:** **PASS after one substantive residence-scope repair and one
connectedness clarification.**  
**Method:** exact binary arithmetic and cube-graph arguments only; no
search, solver, H100, or numerical experiment was used.

## 1. Frozen source and repairs

The submitted theorem

`MATH_THEOREM_TOUCH_NUMBER_BINARY_RESIDUE_AND_FACE_GLUE_GATE_20260804.md`

had SHA-256

`97091539e24cb63e7bd69ea812e3af2174dbb887e4ca0df020c6b2dbf038d82a`.

Two repairs were applied.

1. The exact connectivity condition is simply that the face-glue graph is
   connected.  In a genuine two-touch instance both shores are nonempty,
   so the graph has at least two vertices and “no isolated face” is
   automatic rather than an additional boundary convention.
2. Internal residence of each constituent path plus separate seam tests is
   insufficient when one short constituent allows a window to cross two
   seams.  The sufficient criterion now requires every constituent path to
   have at least `D` vertices, so consecutive seam transitions are at least
   `D` positions apart.  Without that length condition, a direct global
   multi-seam collar audit is explicitly required.

The repaired theorem SHA-256 is

`a0a53ec1846d0bc613eae4a3ce00c3dc296e823ea9f3e06ad888364c90039e18`.

## 2. Trace cardinalities for crossing cells

The companion trace theorem applies to every selected cell with nonempty
intersection with the source cell, whether or not the full selected cell is
contained in the source.  On each alternating component of the two pairing
overlays, a zero/two occupancy fixes the component, while an all-one
component has exactly two complementary solutions.

If `a_i` free components are common pairs and `b_i` are nontrivial free
alternating cycles, the trace is the disjoint union of `2^(b_i)` induced
`a_i`-faces.  Hence

\[
 |K_i\cap C|=2^{a_i+b_i}=2^{e_i}.
\]

No containment assumption enters this cardinality.  Since touching means
the trace is nonempty, every term in the trace partition has this form.

## 3. Modular touch lower bound

Exact coverage gives a disjoint trace partition

\[
 C\setminus U=\dot\bigcup_{i=1}^{t}(K_i\cap C).
\]

As `m>=M`, `|C|=2^m` is zero modulo `2^M`.  Therefore

\[
 (-W_r)\bmod2^M
 \equiv|C|-|U|
 =\sum_{i=1}^{t}2^{e_i}\pmod {2^M}.
\]

Terms with `e_i>=M` vanish modulo `2^M` but still count among the `t`
touches, so discarding them can only strengthen the desired inequality.
When a remaining power `2^e` is added in `M`-bit arithmetic, either one
zero bit becomes one, or a run of ones is cleared and its next zero bit is
set.  The Hamming weight rises by at most one.  A carry past bit `M-1`
only deletes bits.  Starting from zero proves

\[
 \operatorname {wt}_2\left(sum_i2^{e_i}\bmod2^M\right)\le t.
\]

Thus

\[
 t\ge\operatorname {wt}_2((-W_r)\bmod2^M)
\]

is exact and includes all carries and all large-exponent traces.

## 4. Sharp two-touch congruence form

Write

\[
 W_r=2^s u,qquad u\text{ odd},qquad L=M-s.
\]

Because `M>s`, the negative residue has exact valuation `s`.  An `M`-bit
integer of weight at most two and valuation `s` is exactly

\[
 2^s
 \quad\text{or}\quad
 2^s(1+2^d),\qquad1\le d<L.
\]

Dividing by `2^s` and negating modulo `2^L` gives precisely

\[
 u\equiv-1
 \quad\text{or}\quad
 u\equiv-1-2^d\pmod {2^L}.
\]

This is an equivalence with the **binary-weight condition**, and only a
necessary condition for a physical two-touch extension.  The theorem does
not promote it to sufficiency.

## 5. Odd-unit count and complement identity

Negation permutes the `2^(L-1)` odd classes modulo `2^L`.  An odd `L`-bit
integer of weight `j` has its low bit fixed and its remaining `j-1` ones in
arbitrary positions, giving

\[
 \binom{L-1}{j-1}
\]

classes.  Summation over `1<=j<=t` proves the count in (2.9); for `t=2`
it is `1+(L-1)=L`.

If `a=u mod2^L` is odd, then

\[
 (-u)\bmod2^L=2^L-a=(2^L-1)-(a-1).
\]

The right side is exactly the `L`-bit complement of `a-1`.  Therefore

\[
 \operatorname {wt}_2((-u)\bmod2^L)
 =L-\operatorname {wt}_2((u-1)\bmod2^L).
\]

Both the count and identity are exact.  They make no distributional claim
about the odd parts of central binomial coefficients.

## 6. Face-glue connectedness and edge budget

Within one trace family, the companion theorem gives no cube edge between
distinct induced faces.  Contract every face in the induced graph on
`T_1 union T_2`.  Each contracted vertex is connected internally, and the
remaining edges are exactly the bipartite face adjacencies used to define
`H(K_1,K_2;C)`.  Contracting connected pieces preserves connectedness in
both directions.  Hence

\[
 T_1\cup T_2\text{ is connected}
 \quad\Longleftrightarrow\quad H\text{ is connected}.
\]

Since `|F_i|=2^(b_i)`, a connected simple face-glue graph has at least

\[
 2^{b_1}+2^{b_2}-1
\]

distinct face-pair adjacencies.  Each such adjacency is witnessed by at
least one distinct cube edge between disjoint face pairs.  The theorem
claims this face-pair budget, not a count of all parallel cube edges.

## 7. Face-chain and residence sufficiency

An alternating ordering of all faces, Hamilton paths with declared ports,
and one cross edge between each consecutive pair concatenate to a simple
Hamilton path of the complete two-trace union.  A complementary Hamilton
path on `U` plus two distinct boundary edges closes one Hamilton cycle.
Thus the interval criterion is sound.

For residence, suppose every constituent path has at least `D` vertices,
hence at least `D-1` internal transitions.  Consecutive seam transitions
are then at index distance at least `D`.  Every transition interval shorter
than `D` is either internal to one constituent or crosses exactly one seam.
Internal residence and the literal two-sided collar certificate at that
seam therefore imply global `D`-residence.

Without the length hypothesis, a short face can place two seams in one
sub-`D` window; independent single-seam certificates need not compose.  The
repaired theorem correctly requires a global multi-seam check in that case.

## 8. Global `U=C\setminus K` calibration

The companion one-touch note's calibration remains fully global.  With
`P=R`, the complement

\[
 A=V\setminus C
\]

is `P`-measurable.  After the four-coordinate re-pairing, the chosen
`Q`-cell `K` satisfies `K subset C`, so

\[
 B=V\setminus K
\]

is `Q`-measurable, `A subset B`, and

\[
 B\setminus A=C\setminus K.
\]

The source cube has a Hamilton cycle obtained by traversing the four
selector layers in Gray order and alternating the direction of a Hamilton
path in the common `a`-cube.  The `K` layer and its three-layer complement
are both cyclic intervals.  Thus the non-power-of-two nested difference is
not merely a local trace identity; it is a globally measurable calibration.
It does not contradict the touch lower bound, because it is a calibration
of the nested-difference gate rather than a residue-compatible long-resident
target for arbitrary `r,M,D`.

## 9. Exact frontier

The two-touch architecture requires all of the following simultaneously:

1. binary weight at most two;
2. globally consistent zero-zero/one-one-free dicut labels;
3. connected face glue, strengthened to a face-chain or another literal
   interval chronology; and
4. internal and seam residence, including multi-seam interactions when
   constituent traces are short.

Failure of the first row is an unconditional no-go.  Passing it proves no
existence for the other rows.

**Final independent verdict: PASS after the stated repairs.**  No
two-touch selector, macro Hall theorem, palette, compiler, or
`B(k)+O(1)` conclusion is established.
