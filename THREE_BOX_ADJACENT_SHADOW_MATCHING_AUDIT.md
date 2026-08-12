# Audit of the frozen adjacent-shadow theorem

## 1. Verdict

The principal combinatorial theorem in
`THREE_BOX_ADJACENT_SHADOW_MATCHING.md` is correct:

* the graph `Gamma_a` is exactly the lower-color/upper-color graph of
  Johnson edges in the central hexagon;
* its perfect matching is unique for every `a>=0`;
* under the color-edge bijection, that matching is precisely the disjoint
  union of the ordinary edge cycles of the concentric rings
  `R_1,...,R_a`;
* its exact edge-trail cost is `M_a+a`, including the isolated center; and
* Lemma 5 correctly localizes an `s`-defect edge cover to at most `s`
  alternating paths plus at most `2s` discarded edges.

Corollary 6 is also correct after making its architectural hypotheses
explicit: for an exact-rainbow arc row serving as the selected central
occurrences of a monotone band with total physical excess `D=O(a)`, the
number of **extra ring cuts** must be `Omega(a)`.

Four scope/wording corrections are needed.

1. The number `b_s` must mean the number of maximal trail blocks of forced
   `R_s`-edges in the linear row (or separately concatenated arc words).
   An arbitrary formal partition of a ring into `b_s` pieces gives no lower
   bound if adjacent pieces are immediately rejoined with a shared endpoint;
   then they are one trail block.
2. Corollary 6 proves
   `sum_s(b_s-1)=Omega(a)`, a linear number of extra **cuts**.  It does not
   prove that `Omega(a)` distinct radii are split: all those cuts could in
   principle be concentrated on a few rings.  The heading "a positive-order
   number of rings" is too strong.
3. `O(a)` total arcs and the anti-mixing theorem do not by themselves imply
   a bounded number of macroscopic phases.  They imply only average
   `O(1)` arcs per radius and the existence of a quadratic desert in the
   relevant induced order.
4. The nested-subcube result audited separately does not prove that deserts
   at different radii are aligned in the physical word.  Therefore
   "aligned quadratic run deserts at the nested outer scales" remains a
   proposed construction requirement, not a consequence of the two proved
   theorems.

There is also a typo near the end: "Combining Corollary 5" should refer to
Corollary 6 (or simply "Combining this corollary").

With these corrections, the frozen-matching theorem and its quantitative
conditional consequence are certified.

## 2. Adjacent-layer sizes

Write

\[
 \mathcal H_a=\{(x,y,z):x+y+z=0,\ |x|,|y|,|z|\le a\}.
\]

Its size is

\[
                         M_a=3a^2+3a+1.
\]

For the lower layer, translate each coordinate by `a`.  Counting solutions
in `[0,2a]^3` of sum `3a-1` gives

\[
 |L_a|={3a+1\choose2}-3{a\choose2}=3a^2+3a=M_a-1.
\]

Reflection through the origin gives the same count for `U_a`.  The formulas
also hold at `a=0`, where both adjacent layers are empty.

## 3. The graph and the color-edge bijection

The definition

\[
 w\sim u\quad\Longleftrightarrow\quad
 u-w=e_i+e_j\quad(i\ne j)
\]

is the correct one.  Because the nonzero coordinates of `u-w` identify the
unordered pair `{i,j}`, there is no hidden multiplicity.

If `(w,u)` is such an edge, then

\[
                         p=w+e_i,\qquad q=w+e_j
\]

both have coordinate sum zero.  They lie in the box: since `u_i=w_i+1`
and `u_j=w_j+1` are at most `a`, adding the corresponding unit vector to
`w` does not cross a positive wall, while no coordinate is decreased.
Their coordinatewise meet is `w`, their join is `u`, and
`p-q=e_i-e_j`, so they form a Johnson edge of `mathcal H_a`.

Conversely, orient a Johnson edge as

\[
                         q=p-e_i+e_j.
\]

Its meet and join are

\[
                         w=p-e_i,\qquad u=p+e_j.
\]

The fact that both middle endpoints lie in the box guarantees that `w` and
`u` also respect the coordinate bounds.  Their sums are `-1` and `1`, and
`u-w=e_i+e_j`.  The two constructions are inverse.

Pairs with difference `2e_i` are correctly excluded.  The interval from
such a lower point to such an upper point has only one middle point and
cannot encode the meet and join of two distinct adjacent middle targets.

It follows that a collection of `M_a-1` middle Johnson edges is exactly
rainbow on both adjacent layers if and only if the corresponding edges are
a perfect matching of `Gamma_a`.

## 4. Degree-one walls

Suppose `w in L_a` has `w_k=a`.  An edge out of `w` adds one to two distinct
coordinates.  It cannot add to coordinate `k`; hence it must add to the
other two, giving one candidate `u`.  Neither other coordinate can already
equal `a`, since two coordinates equal to `a` would force the third to be
`-1-2a<-a` for `a>=1`.  Thus the candidate remains inside the box and
`deg(w)=1`.

The dual argument proves that `u in U_a` with `u_k=-a` has degree one: its
predecessor must subtract from the other two coordinates, which are both
strictly greater than `-a`.

The six side formulas in (3.2) are correct.  For example, side zero runs
from

\[
 (a,-a+t,-t)\quad\hbox{to}\quad(a,-a+t+1,-t-1),
\]

so its meet and join are

\[
 (a,-a+t,-t-1),\qquad(a,-a+t+1,-t).
\]

The remaining five formulas follow by the displayed cyclic coordinate
symmetries.  Each edge is forced by the positive wall of its meet or the
negative wall of its join, exactly as listed in (3.1).

The lower colors in the six lists are mutually distinct, as are the upper
colors.  This can be read directly from which wall and side parameter they
occupy; the corner cases in one list do not duplicate a color in the next.
There are `6a` colors on each side.

Finally, the colors touching an outer wall are exactly the complement of
the corresponding adjacent layer in the inner cube.  Their number is

\[
 (M_a-1)-(M_{a-1}-1)=M_a-M_{a-1}=6a.
\]

Hence the listed endpoints exhaust, rather than merely lie among, all
boundary colors.

## 5. Peeling and uniqueness for every radius

Every perfect matching must contain all `6a` forced outer-ring color edges.
Their lower endpoints are all distinct, their upper endpoints are all
distinct, and Section 4 shows that they exhaust the boundary vertices.
After deleting them, the surviving vertices are exactly

\[
 L_{a-1},\qquad U_{a-1}
\]

inside `[-a+1,a-1]^3`.  Restricting the same difference rule
`u-w=e_i+e_j` gives exactly `Gamma_(a-1)`, with no extra or missing edge.

At `a=0`, the empty graph has the unique empty perfect matching.  Induction
therefore proves uniqueness for all `a`.  At stage `s` the peeled forced
edges are exactly the `6s` ordinary edges of `R_s`; hence the matching is

\[
                         E(R_1)\sqcup\cdots\sqcup E(R_a).
\]

The rings have disjoint middle vertex sets, and

\[
 \sum_{s=1}^a6s=3a(a+1)=M_a-1,
\]

so this identification also passes the global edge count.

## 6. Trail ledger

For any finite graph, the minimum number of trails partitioning the edges of
a nonempty connected component `C` is

\[
                         \max\{1,o(C)/2\}.
\]

The lower bound follows because each open trail supplies at most two odd
ends, while a nonempty Eulerian component still needs one trail.  Pairing
the odd vertices with dummy edges, taking an Euler tour, and deleting the
dummy edges proves attainability.

If all matched edges are required exactly once, write each trail with its
vertex sequence.  A trail of `e` edges costs `e+1` positions, and every
isolated required middle vertex costs one more position.  Thus any exact
edge traversal has length at least

\[
 |E(G_mu)|+\operatorname{tr}(G_mu)+z(G_mu),
\]

and concatenated trail words attain that numerical length as a row
containing every required edge and vertex.  At a join between two trail
words an accidental graph edge could be traversed a second time; this does
not invalidate the existence statement (which asks only that every edge be
contained) or the stated lower bound for rows using each edge exactly once.
For the concentric matching the components are distinct rings, so even this
minor accidental-join issue does not arise between components.

The frozen graph has `a` nonempty Eulerian components and one isolated
center.  Therefore

\[
 |E|=M_a-1,\qquad\operatorname{tr}=a,\qquad z=1,
\]

and the exact cost is `M_a+a`.

## 7. Arc interpretation and its necessary convention

Cutting a ring cycle into separately written path arcs gives, for radius
`s`, `6s` forced edge occurrences plus one initial vertex per arc.  Across
all rings, after appending the center, the row length is

\[
 (M_a-1)+\sum_sb_s+1=M_a+\sum_sb_s.
\]

This is exact when the `b_s` arcs are the maximal trail blocks in the row,
or when the construction explicitly concatenates `b_s` independent arc
vertex words (including both endpoint occurrences).  That is the convention
needed in (1.1), (4.3), and Corollary 6.

It is not true for a purely formal partition.  If two adjacent arcs of one
ring are immediately placed in cyclic order and their common endpoint is
identified, they have merged into one longer trail block and the effective
value of `b_s` has decreased.  The theorem should define `b_s` after making
all such mergers.

Under that convention the closed ring is `b_s=1`, represented by a closed
trail word of `6s+1` vertices, and summing over radii gives the minimal
`M_a+a` row.  A row of length `M_a+O(a)` can consequently have only `O(a)`
maximal forced-edge arcs in total.

## 8. Near-rainbow defect lemma

Let `F` be an edge cover in a balanced bipartite graph with `n` vertices per
side and unique perfect matching `mu`.  The graph `(V,F)` has no isolated
vertices, so the standard edge-cover identity gives

\[
 \nu(F)\ge2n-|F|\ge n-s.
\]

Choose a maximum matching `P subseteq F`.  In `mu triangle P`, every
component is an alternating path or cycle.  An alternating cycle would let
one toggle `mu` to a second perfect matching of the ambient graph, contrary
to uniqueness.  A path endpoint must be unmatched by `P`, because `mu` is
perfect.  There are exactly

\[
                         2(n-|P|)
\]

such endpoints, hence exactly `n-|P|<=s` nontrivial alternating paths.
Moreover,

\[
 |F setminus P|\le(n+s)-(n-s)=2s.
\]

Every `mu`-edge omitted by `P` belongs to one of those paths.  Lemma 5 is
therefore correct as stated.

The safe interpretation is that, after discarding `O(s)` edges of the
cover, its maximum matching differs from the frozen matching only along
`O(s)` alternating paths.  Those paths may have linear or quadratic length;
the lemma gives no localization bound in the geometry of the hexagon.

## 9. Audit of Corollary 6

Interpret an exact-rainbow arc schedule as follows.  It is a linear middle
occurrence row containing every frozen ring edge, its maximal forced-edge
blocks on `R_s` number `b_s`, and one occurrence of each distinct middle
target is selected in the same order to form the central witness family of
an unrestricted monotone band.  Assume the total physical excess of that
band is `D=O(a)`.

Suppose

\[
                         \sum_s(b_s-1)=o(a).
\]

Then only `o(a)` radii are split.  Delete all target occurrences belonging
to those radii.  Their number is

\[
 R\le6a\,o(a)+O\!\left(\sum_sb_s\right)=o(a^2),
\]

where the second term allows duplicated arc endpoints.  Every surviving
radius is one contiguous complete ring block.

For each surviving block, the cut can destroy at most one of its three
positive extreme sides; choose the other two.  Each chosen side is bounded
inside that block by zero occurrences of its increment, so it remains an
internal maximal run even after the deleted split-ring occurrences are put
back elsewhere in the schedule.  Its length is at most `a+1`.

After the split-ring positions are restored, every surviving index except a
boundary portion can reach a chosen run across at most

\[
                         O(a)+R=o(a^2)
\]

middle indices.  The final boundary portion is charged in the reverse
direction.  Applying the exact run inequality, an adjacent increment of an
endpoint-offset sequence is charged at most `o(a^2)` times.  Since each
offset sequence has total variation at most `D=O(a)`, all difference terms
contribute `o(a^3)`.

The base run-length term is at most `aM_a`; the `R=o(a^2)` deleted indices
each have band width at most `D`, contributing another `o(a^3)`.  The exact
avoidance ledger contributes only `O(D^2)=O(a^2)`.  Hence

\[
                         Q\le3a^3+o(a^3),
\]

contradicting the `4a^3+O(a^2)` distinct nonzero targets below the middle
layer.  Thus

\[
                         \sum_s(b_s-1)=\Omega(a).
\]

The proof is sound under the explicit central-occurrence interpretation.
Its conclusion is a linear number of additional cuts.  Since one ring can
carry `Theta(a)` cuts, it does not imply a linear number of distinct split
rings.

## 10. Conditional consequences and exact scope

The proved synthesis is narrower than the prose in Section 5 suggests:

* exact common adjacent shadows freeze the edge set to the concentric rings;
* a near-width exact traversal has `O(a)` maximal ring arcs;
* universality at `D=O(a)` requires `Omega(a)` extra cuts beyond one per
  ring; and
* any such induced order must also obey the anti-mixing mesh lower bound.

These facts leave a real, nonempty regime: `Theta(a)` total arcs, potentially
concentrated unevenly among the radii, arranged with at least one
macroscopic run desert.  They do not prove a bounded number of phases, a
six-sector form, or alignment of deserts across embedded subcubes.

Finally, the entire frozen theorem concerns consecutive middle Johnson
edges supplying a **common** exact lower/upper adjacent-shadow cover.  An
unrestricted OR word may use extra color edges, different witness lengths,
or a variable endpoint band in which the adjacent ranks are not read from
one central occurrence row.  The source correctly lists these as escape
routes; none is closed by the matching theorem.
