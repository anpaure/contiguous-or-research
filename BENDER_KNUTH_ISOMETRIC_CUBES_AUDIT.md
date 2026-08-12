# Independent audit of the Bender--Knuth isometric-cube theorem

## A. Audited claim and quantifiers

The claim audited here is exactly this:

> For every two-row tableau `Q`, the complement of any vertex cover of its
> odd-generator twist graph spans a fixed-support, disjoint-coordinate,
> radius-pure cube through `Q`.  Moreover, outside an `o(W)` family of
> tableaux, there exists such a cube through `Q` of dimension
> `(1/8-o(1))m`.

The quantifier is **a cube through each good vertex**.  It is not asserted
that the chosen cubes are equal on intersections, vertex-disjoint, or a
partition of the middle layer.  Thus the result is an overlapping host-cube
theorem only.

The audit independently re-derives the local dynamics and both exceptional
counts from `BENDER_KNUTH_ISOMETRIC_CUBES.md`.

## B. Direct RSK check

A two-row standard tableau is equivalent to its row-membership word
`q_1...q_(2m)`, with `U` for the top row and `D` for the bottom.  Standardness
is exactly nonnegativity of every prefix height.

Stack-match every `D` to the most recent unmatched `U`.  If the terminal
height is `2d`, there are `2d` persistent `U` steps.  Assign binary one to
all matched `U` steps and to the last `d` persistent `U` steps; assign zero
to all `D` steps and the first `d` persistent `U` steps.

This has weight

\[
 (m-d)+d=m.
\]

Running ordinary binary row insertion on the result recreates `q`: a `D`
label is created exactly when a zero bumps a previously unmatched one to
the second row, which is exactly a stack closure.  Persistent first-row
cells are read in the forced semistandard order, yielding the half-and-half
assignment.  This checks that the carrier calculation below is about the
actual inverse-RSK middle word, not an auxiliary path labeling.

## C. Independent carrier truth table

Group labels into blocks `(2j-1,2j)`.  At a positive block-boundary level a
mixed block is active and `tau_(2j-1)` toggles

\[
 UD\longleftrightarrow DU.
\]

Fix the stack slot at the block's starting height, and call its current
ground coordinate `e`.  The two orientations have the following effects.

| orientation | odd coordinate | even coordinate | carrier after block |
|---|---|---|---|
| `UD` | matched `U` | its matching `D` | `e` |
| `DU` | `D` matched to `e` | new `U` | `2j` |

There are three exhaustive fates for the two possible post-block carriers.

1. A later down-crossing consumes the stack slot.  Both candidates are
   matched.  Only `2j-1,2j` differ.
2. The slot persists, but its rank among the `2d` persistent steps exceeds
   `d`.  Both candidates receive the same high-half bit.  Again only
   `2j-1,2j` differ.
3. The slot persists and its rank is at most `d`.  The old carrier changes
   from persistent-low to matched while the odd coordinate changes in the
   opposite direction.  The support is `{2j-1,e}`.

At block level `h`, the slot rank is `2h`.  Fate 3 therefore occurs exactly
after the last block boundary below `h` and only when `2h<=d`.  These are
precisely the critical sequences of the main note.

Inside one critical sequence, write `x_r=1` for `DU` and `x_r=0` for `UD`.
A `DU` overwrites the carrier; a `UD` leaves it unchanged.  For direction
`r`:

* a later `1` guarantees fate 1 at the next overwrite and gives native
  support `{p_r,p_r+1}`;
* with no later `1`, the support is `{p_r,e_(r-1)}`, where `e_(r-1)` is the
  initial even carrier or the even coordinate of the last earlier `1`.

This re-derives the exact support formula without using commuting-square
data.

## D. Twist criterion audit

Take `r<s` in one critical sequence.  Toggling `s` can change the answer to
“is there a later overwrite after `r`?” only when every later orientation
other than possibly `s` is zero.  Under the same condition, toggling `r`
changes the last earlier carrier seen at `s`.  If any other later `1` exists,
both effects are erased at that overwrite.

Thus both opposite-edge comparisons agree, and the square is twisted iff

\[
 x_t=0\qquad(t>r,\ t\ne s).                           \tag{D.1}
\]

Outside a critical sequence the support is native regardless of all odd
toggles, so cross-sequence twists are impossible.

This criterion also exposes why a static collision test is insufficient:
two supports can be disjoint at the base vertex while an opposite edge
changes after removal of the last carrier overwrite.

## E. Arbitrary vertex-cover audit

Let `K` be independent in the graph (D.1); equivalently its complement is a
vertex cover.  In a fixed critical sequence, locate the last base-state `1`
whose direction is not retained.  It remains fixed throughout the
`K`-subcube.

Every retained direction before this fixed `1` always has a later overwrite,
so it keeps its native pair.  In the tail after it, there can be at most one
retained direction:

* with no retained `1`, every two retained zeros satisfy (D.1);
* with exactly one retained `1`, it satisfies (D.1) with every other
  retained tail vertex;
* with at least two retained `1` vertices, the final two satisfy (D.1).

The possible one tail direction uses the even coordinate of the fixed last
overwrite, or the initial carrier.  Neither can occur in a retained native
pair: the former belongs to a deleted block and the latter to an inactive
`UU` block.  Stack slots at different heights use distinct carrier
coordinates.  Hence the retained supports are fixed and pairwise disjoint.

Because the odd involutions commute and activity depends only on the block
type and boundary height, all `2^|K|` toggles exist.  Fixed disjoint supports
make their middle words distinct and identify the orbit with an isometric
coordinate-pair cube.  Shape is invariant under Bender--Knuth swaps, so the
cube is radius-pure.

No minimality of the vertex cover was used.  The result holds for **any**
vertex cover.

## F. Audit of the false `3^m` count

For `m>=4`, use the block family

\[
 UU,UD,UD,E,UU,
\]

where `E` is a two-coloured Motzkin excursion of length `m-4`.  It remains
above absolute block level one, returns there, and the final `UU` makes
radius `d=2`.  Level one is therefore critical.  It has at least two mixed
blocks, and the final two mixed blocks form a twist by (D.1).

There are `Cat_(m-3)` choices of `E`.  Hence even the number of tableaux
having one twist is at least

\[
 \operatorname {Cat}_{m-3}
 =\Theta(4^m/m^{3/2})=\Theta(W/m).
\]

Its logarithmic growth rate is `log 4`, so an
`exp((log 3+o(1))m)` bound on total twist-pair occurrences is impossible.

## G. Independent large-dimension count

Let `D(Q)` count `DU` blocks.  Retain all such directions except the final
`DU` in each critical sequence.  The omitted final direction is a permanent
carrier overwrite, so every retained support is its native block pair.  At
most `floor(d/2)` directions are omitted:

\[
 \dim K(Q)\ge D(Q)-\lfloor d/2\rfloor.                \tag{G.1}
\]

Take `a=ceil(m^(2/3))`.

First, the two-row hook counts telescope exactly:

\[
 \#\{Q:d>a\}=\binom{2m}{m-a-1}.
\]

The ratio to `W` is at most

\[
 \exp(-(a+1)^2/(m+a+1))=o(1).                         \tag{G.2}
\]

Second, discarding ballot legality only enlarges the family with fewer than
`m/8` `DU` blocks.  Mark the `DU` locations and give every other block one
of three types:

\[
 \#\{Q:D(Q)<m/8\}
 \le\sum_{t<m/8}\binom mt3^{m-t}.                    \tag{G.3}
\]

The exponent in (G.3) is at most

\[
 H(1/8)+(7/8)\log3=1.3380559138\ldots<\log4.
\]

Thus (G.3) is also `o(W)`.  Combining (G.1)--(G.3), outside `o(W)` vertices,

\[
 \dim K(Q)\ge m/8-\tfrac12\lceil m^{2/3}\rceil
             =(1/8-o(1))m.
\]

This suffices for every requested `ell=o(m)`.

## H. Machine audit and residual boundary

`scratch/verify_bk_isometric_cubes.py` independently reconstructs the RSK
recording path by row insertion, enumerates all actual commuting squares,
checks (D.1), and checks every state of the canonical retained cube.  It
passes through `m=8`, including all 12,870 tableaux there.

What remains unresolved is global.  The theorem gives many overlapping
linear-dimensional local charts.  It does not:

* select a vertex-disjoint near-partition into those charts;
* align their fixed pairs across different base tableaux;
* round typed lower/upper shadows with total defect `o(W)`;
* construct the shift-compatible symmetric-chain decomposition.

Accordingly this audit accepts the local isometric-host theorem and rejects
both the `3^m` twist-incidence claim and any inference from local host cubes
to global shadow completion.
