# Independent audit of `VIRTUAL_SEAM_TRACE_STITCHING.md`

## Verdict

The two principal results are correct.

1. For every fixed `q`, the forced-arm spine plus the stated path library
   gives a word of length

   \[
        |L_{2m}|+O_q(m^2)
   \]

   covering ranks `2m-1,...,2m+q`.  More precisely, the displayed repair
   count is uniform in `m,q` and is `O(m^2(q+1)^5)`.  Hence the conclusion
   for `q=o(m^(1/5))` is valid; there is no hidden fixed-`q` constant being
   used in that deduction.
2. In an edge-once signed ordering of refinements of the forced arms, an
   `Omega(m^2)` family of seams must be active already for rank `2m+1`.
   The stated congestion bound `45` is valid.  It is not sharp: the same
   proof gives `36`, because every target in the chosen hard family has
   exactly three positive coordinates.

The supplied finite checker passed unchanged.  It substantively verifies
the graph/arm counts, the hard-family obstruction inside individual arms,
and bounded-depth repair paths in the sampled boxes.  It does not check the
constant-congestion charging theorem; that part is justified by the
independent argument in Section 4 below.

I found no overclaim in the fixed-`q` theorem or in its stated growing-`q`
corollary.  Two possible improvements are noted below, but neither is needed
for correctness.

## 1. Forced-arm accounting

For `m>=2`, the previously proved degree inventory gives

\[
 |K_m|=2m^2+2.
\]

The sum of degrees at the degree-one and degree-three kernel vertices is

\[
 m(m-1)+3\bigl(m(m+1)+2\bigr)=4m^2+2m+6.
\]

Thus there are `2m^2+m+3` arms with kernel endpoints.  The unique component
containing only degree-two vertices contributes one more arm after it is
cut, so

\[
                  |\mathcal A_m|=2m^2+m+4.          \tag{1}
\]

Writing every arm with `h` edges as its `h+1` vertices gives total length

\[
                  |E(G_m)|+|\mathcal A_m|
                = |L_{2m}|+2m^2+m+4.               \tag{2}
\]

Every selected edge is internal to exactly one arm word, so its two endpoint
letters give its rank-`2m` colour.  Every rank-`(2m-1)` vertex is incident to
an arm for `m>=2`; equivalently, the exact degree inventory has no isolated
vertex.  Thus the base word covers precisely the two claimed central ranks,
with arbitrary arm orientations and arbitrary joins.

The artificial cut in the unique all-degree-two component must be included
in the exceptional set.  The source does this: adjoining its cut vertex to
`K_m` gives

\[
                       |K_m^*|\le 2m^2+3.            \tag{3}
\]

If a path avoids `K_m^*`, all of its edges lie in one uncut arm segment.
Reversing that arm does not matter, because coordinatewise maximum is
unchanged by reversal.

## 2. Audit of the bounded-depth construction

Fix an upper target `y` and put `D=|y|-2m`.  Every lower-central vertex
below `y` has the form

\[
                         v=y-\delta,
             \qquad |\delta|=D+1.                  \tag{4}
\]

The reverse-greedy construction supplies a directed facet-spanning path
`P_y`.  Along each selected directed edge, one unit moves from a later
coordinate to an earlier coordinate, so

\[
                         \Phi(v)=\sum_{i=1}^4 i v_i
\]

strictly decreases.  For vertices satisfying (4),

\[
 \Phi(v)=\Phi(y)-\sum_i i\delta_i.
\]

Among nonnegative deficit vectors of fixed mass `D+1`, the weighted sum has
range at most `3(D+1)`.  Therefore

\[
                    |E(P_y)|\le3(D+1),
       \qquad |V(P_y)|\le3D+4\le3q+4.              \tag{5}
\]

All letters of `P_y` have rank `2m-1`, lie coordinatewise below `y`, and
their coordinatewise maximum is exactly `y`.  Appending its vertex word
therefore gives a literal contiguous witness for `y`; it is not merely a
connected-subgraph certificate.  Concatenating this gadget with other
gadgets cannot destroy the interval consisting of the gadget itself.

If `P_y` avoids `K_m^*`, Section 1 shows that it already occurs inside one
base arm.  Otherwise choose one vertex `v in P_y cap K_m^*` to charge the
repair.  For fixed `v`, the target is `y=v+delta`, where

\[
                         |\delta|\le q+1.
\]

The number of nonnegative four-coordinate vectors of total mass at most
`q+1` is exactly

\[
                \sum_{s=0}^{q+1}{s+3\choose3}
                ={q+5\choose4}.                    \tag{6}
\]

Box ceilings only decrease this number.  Choosing one charge for each
exceptional target prevents multiple kernel hits from being counted more
than once.  Equations (3), (5), and (6) give the explicit repair bound

\[
       (2m^2+3){q+5\choose4}(3q+4).                 \tag{7}
\]

Together with (2), this proves Theorem 2.  It also checks all exact rank
statements:

* base letters have rank `2m-1`;
* adjacent letters along a selected edge have maximum of rank `2m`;
* an appended `P_y` has maximum exactly `y`, of rank at most `2m+q`.

No cross-gadget or cross-arm interval is needed by the proof.

## 3. Fixed `q` versus growing `q`

For `q>=1`,

\[
 {q+5\choose4}(3q+4)=O((q+1)^5)
\]

with an absolute constant.  Hence (7) is genuinely uniform:

\[
 |W|-|L_{2m}|=O\bigl(m^2(q+1)^5\bigr).             \tag{8}
\]

It follows directly that `q=o(m^(1/5))` makes the excess `o(m^3)`.  This
use of growing `q` does not rely on the notation `O_q(m^2)`; it relies on
the explicit formula (7).  The restriction `q<=2m` is exactly the range in
which `2m+q` remains inside the four-box rank range.

There is a simple optional improvement if one does **not** insist that all
new letters remain in rank `2m-1`: append each exceptional target `y`
itself rather than its path `P_y`.  Equation (6) then gives excess
`O(m^2(q+1)^4)`, and consequently `q=o(m^(1/4))` would suffice.  The source's
path-library version is still useful because it preserves the stronger
rank-pure alphabet property needed by factor constructions.  Its `q^5`
bound is correct as stated, merely nonoptimal for unrestricted words.

## 4. Audit of the quadratic active-seam bound

For

\[
 y=(0,a,b,c),\qquad 2\le a,b,c\le m-1,
       \qquad a+b+c=2m+1,
\]

the allowed selected colours are exactly `y-e_2,y-e_3,y-e_4`.  The first
two meet at

\[
                         p=(0,a-1,b-1,c),
\]

and the third edge is vertex-disjoint from this two-edge path.  The point
`p` has first two positive coordinates `2,3`, both nonfull, and therefore
degree three.  Cutting at every non-degree-two vertex places the two useful
edges in different forced arms.  Since any interval with maximum `y` uses
only letters below `y`, it cannot leave the induced graph and return by an
outside colour.  Hence no interval internal to one forced arm represents
`y`.  Refining an arm only removes possible internal intervals, so the same
is true for every refinement.  The coordinate-swapped family has the same
property.

Writing `alpha=m-a`, `beta=m-b`, `gamma=m-c` converts the count to positive
compositions of `m-1` into three parts.  Thus each family has
`C(m-2,2)` members, the two families are disjoint, and their union has

\[
                         (m-2)(m-3)                 \tag{9}
\]

members.

Now fix an edge-once signed block ordering and a witness of rank `2m+1`.
Every within-block adjacency used by that witness is a selected edge whose
rank-`2m` colour lies below the target.  There are at most four such colours
for an arbitrary target, and every selected edge occurs in only one block.
If the witness meets `b` blocks, each of its `b-2` strict interior blocks
contains at least one within-block edge.  Therefore `b<=6`.

Charge every chosen hard-target witness to its leftmost crossed seam.  Its
initial block is then fixed: it is the block immediately before that seam.
With `b<=6`, there are at most five possible terminal blocks.  For one
fixed terminal block, the relevant suffix maxima in the initial block form
an inclusion chain.  Every one is nonempty and has rank between `2m-1` and
`2m+1`; after duplicates are removed, strict inclusion permits at most one
value at each of those three ranks.  Hence there are at most three suffix
values.  The terminal prefixes give another chain of size at most three.
All complete intervening blocks are fixed, so the full target is determined
by one suffix-prefix pair.  This gives at most

\[
                         5\cdot3\cdot3=45            \tag{10}
\]

charged targets per seam and proves the displayed lower bound in the
source.

For the particular hard family, one coordinate is zero, so there are only
three rank-`2m` colours below a target.  Replacing `b<=6` by `b<=5` leaves
only four possible terminal blocks.  Thus (10) improves to `36`, and the
same proof actually yields

\[
       \#\{\text{active seams}\}
          \ge {(m-2)(m-3)\over36}.                 \tag{11}
\]

The source's denominator `45` remains fully valid.  The theorem is properly
scoped: it is an obstruction only to edge-once signed forced-arm orderings,
not to arbitrary coordinatewise-maximum words and not to bounded-copy
trace libraries.

## 5. Checker scope and independent tests

I ran

```text
python3 scratch/check_virtual_seam_trace_stitching.py
python3 scratch/search_virtual_seam_order.py 2 --verify-known
python3 scratch/search_virtual_seam_order.py 3 --verify-known
python3 scratch/search_virtual_seam_order.py 4 --verify-known
```

All tests passed.  The first script checks `4<=m<=8`, `1<=q<=4`; the three
stored full-upper signed orders have the claimed lengths `33,69,125`.

I also independently implemented the reverse-greedy path rather than the
checker's augmented-state BFS and exhaustively checked every upper target
for `2<=m<=13`.  For every target the path:

* used only selected edges;
* stayed below the target;
* had coordinatewise maximum equal to the target;
* obeyed `|E(P_y)|<=3(D+1)`.

For `2<=m<=9`, every such path avoiding `K_m^*` used edges from exactly one
forced arm, confirming the artificial-cut case in the constructive proof.

The supplied checker does not enumerate arbitrary signed arm orders and
does not test the `45`-charging assertion.  Its `facet_path` routine is a
BFS in `(vertex,visited-facets)` states and may return a walk rather than
the canonical simple reverse-greedy path.  This is harmless for its finite
coverage test, but the all-`m` path-length theorem comes from the potential
argument in Section 2, not from that code.  Likewise, the active-seam lower
bound comes from the chain-and-charging proof in Section 4, not from the
finite checker.

## 6. Final status

The proof-grade conclusions are therefore:

* bounded upper depth is solved by a rank-pure word at
  `|L_(2m)|+O_q(m^2)` length;
* the explicit formula supports the stated slowly growing depth
  `q=o(m^(1/5))`;
* any edge-once pure arm ordering that covers the upper half must use
  `Omega(m^2)` seams, with denominator `45` as written and `36` available
  by the same argument;
* the all-upper trace-packing lemma remains open.

None of these statements proves a full four-box word of
`|L_(2m)|+o(m^3)` length, but both the positive construction and the
architecture lower bound are mathematically sound.
