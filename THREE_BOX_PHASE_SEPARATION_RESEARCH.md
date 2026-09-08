# Phase-separated forced-ring arcs: a heterogeneous run obstruction

## 1. Outcome

Write

\[
 \mathcal H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                         |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1.
\]

The frozen adjacent-shadow theorem leaves one particularly natural
width-plus-perimeter architecture.  Split every forced ring into a bounded
number of arcs, place the three positive-wall arcs of the current outer ring
on one side of the recursively ordered inner hexagon, and place the other
three arcs on the other side.  In every induced `\mathcal H_s` order, the
outer extreme runs are then concentrated near the ends and the quadratic
deserts required by the anti-mixing theorem are perfectly aligned.

That canonical construction does **not** work.  The main result below is the
exact bound

\[
 Q\le a^3-a+(3a+3)D+3D^2,                              \tag{1.1}
\]

where `D=N-M_a` and `Q` is the number of physical intervals avoiding every
selected middle witness.  Since the nonzero lower half contains

\[
 V_a=4a^3+\frac92a^2+\frac32a-1,                       \tag{1.2}
\]

the recursively phase-separated order cannot be universal with `D=O(a)`.
In fact it requires

\[
                         D\ge(1-o(1))a^{3/2}.           \tag{1.3}
\]

The new ingredient is a **heterogeneous run-cover lemma**.  The earlier
anti-mixing theorem used internal runs of only the three positive extreme
increments.  Here a different coordinate threshold may be used at every
middle index.  A purported desert for the three outer increments is useless
if it is densely covered by cheap internal runs of other thresholds.

There is a second consequence.  The six-sector schedule, and more generally
any schedule having only `o(a)` side-homogeneous batches, also fails at
surface error.  Thus neither of the two obvious versions of phase separation
survives:

* a bounded number of macroscopic side phases has too many cheap threshold
  runs; and
* the perfectly nested order which aligns all outer-scale deserts has even
  less lower-interval capacity.

This is not a no-go theorem for all `O(a)` forced-ring arc schedules.  It
leaves irregular schedules with `Theta(a)` side changes, as well as long
near-rainbow alternating defect corridors.

## 2. The heterogeneous run-cover lemma

Choose one witnessing interval for every target in `\mathcal H_a` and sort
them by their left endpoints:

\[
 I_i=[\ell_i,r_i],\qquad 1\le i\le M_a.
\]

The targets are an antichain, so both endpoint sequences are strictly
increasing.  With `N=M_a+D`, write

\[
 \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
 \qquad w_i=\beta_i-\alpha_i,                           \tag{2.1}
\]

where

\[
 0\le\alpha_1\le\cdots\le\alpha_{M_a}\le D,
 \quad
 0\le\beta_1\le\cdots\le\beta_{M_a}\le D,
 \quad \alpha_i\le\beta_i.                            \tag{2.2}
\]

For any coordinate threshold, let `[u,v]` be an internal maximal `1`-run in
its incidence word on the selected middle targets, so
`2<=u<=v<=M_a-1`.  Coordinate pinning
forces the audited run inequality

\[
                    \beta_{u-1}-\alpha_{v+1}\le v-u.   \tag{2.3}
\]

The following form permits different runs, and different increments, at
different indices.

### Lemma 1 (heterogeneous run cover)

Let `J` be a set of middle indices.  For every `i\in J`, choose an internal
coordinate-threshold run

\[
                         R_i=[u_i,v_i]
\]

which does not contain `i`.  Put `\lambda_i=v_i-u_i`.  Define the two charge
congestions

\[
\begin{split}
 C_\alpha&=\max_t
 \#\{i\in J:i<u_i,\ i<t\le v_i+1\},\\
 C_\beta&=\max_t
 \#\{i\in J:i>v_i,\ u_i\le t\le i\}.
                                                               \tag{2.4}
\end{split}
\]

Then every factorable monotone band obeys

\[
 \sum_{i=1}^{M_a}w_i
 \le \sum_{i\in J}\lambda_i
       +(C_\alpha+C_\beta)D+(M_a-|J|)D.               \tag{2.5}
\]

Here the one-sided span means `v_i+1-i` when `i<u_i`, and
`i-(u_i-1)` when `i>v_i`.  In particular, if every chosen run has
one-sided span at most `h`, then

\[
 \sum_iw_i
 \le \sum_{i\in J}\lambda_i+2hD+(M_a-|J|)D.          \tag{2.6}
\]

#### Proof

If `i<u_i`, monotonicity and (2.3) give

\[
\begin{split}
 w_i&\le\beta_{u_i-1}-\alpha_i\\
    &\le\lambda_i+\alpha_{v_i+1}-\alpha_i.             \tag{2.7}
\end{split}
\]

If `i>v_i`, the symmetric estimate is

\[
 w_i\le\lambda_i+\beta_i-\beta_{u_i-1}.                \tag{2.8}
\]

Expand every difference in (2.7) into adjacent increments of `\alpha`.
By definition, any one increment is charged at most `C_\alpha` times.  The
total variation of `\alpha` is at most `D`.  The `\beta` terms are bounded
identically by `C_\beta D`.  Every unassigned index has `w_i\le D`, proving
(2.5).

If a forward run has span `v_i+1-i\le h`, a fixed `\alpha` increment can be
charged only by one of the preceding `h` indices.  Hence
`C_\alpha\le h`.  The reverse statement gives `C_\beta\le h`, proving
(2.6). \(\square\)

Combining Lemma 1 with the exact avoidance ledger gives the reusable
obstruction

\[
 V_a\le
 \sum_{i\in J}\lambda_i+(C_\alpha+C_\beta)D
 +(M_a-|J|)D+3D^2+2D.                                  \tag{2.9}
\]

Thus, at `D=O(a)`, any run cover with

\[
 \sum_{i\in J}\lambda_i\le(4-\varepsilon)a^3,
 \qquad M_a-|J|=o(a^2),                                \tag{2.10}
\]

must have `C_\alpha+C_\beta=\Omega(a^2)`.  This is a
heterogeneous version of the quadratic-desert requirement: it is no longer
enough to create a desert only for `x=a`, `y=a`, and `z=a`.

## 3. The perfectly aligned recursive arc order

For `s\ge1`, split the radius-`s` ring into the following six half-open side
blocks, each containing `s` distinct vertices:

\[
\begin{array}{c|c}
k&B_{k,s}=\{b_{k,s}(t):0\le t<s\}\\ \hline
0&(s,-s+t,-t)\\
1&(s-t,t,-s)\\
2&(-t,s,-s+t)\\
3&(-s,s-t,t)\\
4&(-s+t,-t,s)\\
5&(t,-s,s-t).
\end{array}                                                   \tag{3.1}
\]

Appending `b_{k,s}(s)=b_{k+1,s}(0)` turns each block into the usual side
trail and traverses all `s` frozen edges on that side.  Hence separating the
six blocks is compatible with an exact-rainbow row having `6a` forced-edge
trail blocks and only linear occurrence overhead.  For every repeated
corner, select the copy designated by the half-open partition (this copy
may be earlier or later in the trail order), so that the distinct
middle-target order is the half-open order below.

Define

\[
\begin{split}
 \mathcal O_a={}&
  B_{0,a},B_{2,a},B_{4,a},
  B_{0,a-1},B_{2,a-1},B_{4,a-1},\ldots,
  B_{0,1},B_{2,1},B_{4,1},\\
 & (0,0,0),\\
 &B_{1,1},B_{3,1},B_{5,1},
  B_{1,2},B_{3,2},B_{5,2},\ldots,
  B_{1,a},B_{3,a},B_{5,a}.                            \tag{3.2}
\end{split}
\]

This is the strongest elementary attempt to align the multiscale deserts.
After deleting all radii greater than `s`, the induced order is exactly
`\mathcal O_s`.  The length-`s` half-open portions of the three positive-wall
sides of `R_s` precede the entire inner hexagon, while their remaining corner
vertices and the three negative-wall blocks follow it.  Thus all internal
runs of the three outer extreme supports lie in `O(s)`-sized outer clusters,
and every nested quadratic desert occupies the same recursive central
region.

Nevertheless, other coordinate thresholds supply a cheap run cover.

### Lemma 2 (explicit run certificate for `\mathcal O_a`)

Assume `a\ge2`.  Every noncentral index of `\mathcal O_a` can be assigned an
internal coordinate-threshold run not containing that index, with one-sided
span at most `2a`, so that the sum of the assigned `\lambda_i` is exactly

\[
                         a^3-a.                       \tag{3.3}
\]

#### Proof

On the first half of (3.2), the whole block `B_{2,s}` is the internal
maximal run of the increment `y\ge s`, and the whole block `B_{4,s}` is the
internal maximal run of `z\ge s`.  The neighboring half-open sides have
coordinate at most `s-1`, so these runs cannot extend.  Each has `s`
vertices and therefore `\lambda=s-1`.

Assign indices in `B_{0,s}` to the run `B_{2,s}`, indices in `B_{2,s}` to
the run `B_{4,s}`, and indices in `B_{4,s}` back to the run `B_{2,s}`.
The assigned run is always different from the index's own block.  Its
one-sided span is at most `2s`, and the contribution at radius `s` is

\[
                         3s(s-1).                     \tag{3.4}
\]

On the second half, the first vertex of `B_{1,s}` is an internal singleton
run of `x\ge s`; the first vertex of `B_{3,s}` is one of `y\ge s`; and the
first vertex of `B_{5,s}` is one of `z\ge s`.  Assign `B_{1,s}` to the
singleton in `B_{3,s}`, assign `B_{3,s}` to the singleton in `B_{5,s}`, and
assign `B_{5,s}` back to the singleton in `B_{3,s}`.  These spans are at
most `2s+1`, and every assigned `\lambda` is zero.  The center is left
unassigned.  Again every one-sided span is at most `2s`.

Finally,

\[
 \sum_{s=1}^a3s(s-1)
 =a(a+1)(a-1)=a^3-a,                                  \tag{3.5}
\]

Inspecting the charge intervals in each three-block radius group also gives

\[
                         C_\alpha\le2a,
 \qquad                    C_\beta\le a.                \tag{3.6}
\]

Indeed, the two forward assignments overlap any `\alpha` increment at most
`2s` times, while the single backward assignment overlaps any `\beta`
increment at most `s` times.  Charge intervals from different radius groups
are disjoint except at an uncharged group boundary.  This proves the lemma.
\(\square\)

### Theorem 3 (aligned recursive phases need volumetric slack)

If the selected middle-target order is `\mathcal O_a`, every factorable
band satisfies

\[
 \sum_iw_i\le a^3-a+(3a+1)D.                          \tag{3.7}
\]

Consequently its middle-avoiding interval capacity satisfies (1.1), and a
universal word with this order has `D\ge(1-o(1))a^{3/2}`.

#### Proof

Apply Lemma 1 with the congestion bounds (3.6), the run-length sum (3.3),
and only the center unassigned.  This gives

\[
 \sum_iw_i
 \le a^3-a+(2a+a)D+D
 =a^3-a+(3a+1)D.                                      \tag{3.8}
\]

The avoidance ledger `Q\le\sum_iw_i+3D^2+2D` gives (1.1).  Universality
requires `V_a\le Q`; hence

\[
 3D^2+(3a+3)D
 \ge 3a^3+\frac92a^2+\frac52a-1.                     \tag{3.9}
\]

Equation (1.3) follows. \(\square\)

The important point is qualitative.  The order has the largest possible
desert one could ask for with respect to the three outer extreme increments,
but that region is not a desert for the full multiscale coordinate system.
The long `y\ge s` and `z\ge s` runs on the pre-inner positive-wall blocks,
together with singleton runs of the same nested extreme thresholds in the
post-inner blocks, cover the order with only linear congestion.

## 4. Bounded side phases also fail

The opposite arrangement is to group equal side types into a few
macroscopic phases.  The same lemma disposes of this case too.

Call an order **side-batched** if, after deleting the center, the `6a`
blocks `B_{k,s}` occur intact and their block sequence is a concatenation
of `B` **maximal** batches, each batch containing blocks of one fixed side
type `k`.  Radii may be permuted arbitrarily inside a batch, every block may
be reversed, and a side type may occur in several batches.  If the center
splits a batch in the full order, regard its two pieces as separate local
batches; this increases the local count by at most one.  The ordinary
six-sector order has `B=6` before this harmless possible split.

### Proposition 4 (linear side switching is necessary)

For a side-batched order used by a factorable universal band with
`D=O(a)`, one must have

\[
                              B=\Omega(a).              \tag{4.1}
\]

More generally, the proof gives `BD=\Omega(a^2)` whenever `D=O(a)`.

#### Proof

Use the following threshold in a batch of type `k`:

\[
\begin{array}{c|cccccc}
k&0&1&2&3&4&5\\ \hline
\text{increment}&z\ge0&y\ge1&x\ge0&z\ge1&y\ge0&x\ge1.
\end{array}                                                   \tag{4.2}
\]

On every even block the incidence word in (4.2) is one `1` and `s-1`
zeros, in either order.  On every odd block it is one `0` and `s-1` ones,
in either order.  Therefore an internal maximal `1`-run in an even batch
has at most three vertices: two endpoint singletons can meet, and the unique
radius-one block can bridge at most once.  In an odd batch a run meets at
most two consecutive blocks and has at most `2a-2` vertices.

Discard the first and last four blocks of every local batch.  This removes
at most `8a(B+1)` indices, including the possible center split.  Let a
retained index lie in block `W_j`; the nine-block window
`W_{j-4},...,W_{j+4}` is then wholly inside its batch.

For an even side type, each block contributes one endpoint `1`.  If this
nine-block window contained no internal maximal `1`-run avoiding the chosen
index, all nine endpoint symbols would lie in at most three runs: the run
crossing the left edge, the run containing the index, and the run crossing
the right edge.  Each such run meets at most three blocks, and a three-block
run requires the unique radius-one block as its middle block.  At most one
of the three runs can therefore meet three blocks, a contradiction.

For an odd side type, at least eight of the nine blocks have a nonempty
`1`-run (only the radius-one block can be all zero).  The same three
distinguished runs meet at most two blocks each, so they cannot cover those
eight positive blocks.  Again an internal run avoiding the index exists.

In both cases it lies on one side of the index within at most five blocks,
so its one-sided span is at most `5a` (and hence at most the stated `6a`).
Splitting at the center ensures that none of these runs crosses it; the
center and the additional discarded margin contribute only `O(aD)` below.

There are

\[
 S=\sum_{s=1}^as=\frac{a(a+1)}2                         \tag{4.3}
\]

indices of each side type.  The total assigned run-length term is therefore
at most

\[
 3S(2a)+O(a^2)=3a^3+O(a^2).                            \tag{4.4}
\]

Lemma 1 and the avoidance ledger now give

\[
 Q\le3a^3+8aBD+O(aD+D^2+a^2).                         \tag{4.5}
\]

Comparison with (1.2) proves `BD=\Omega(a^2)`.  At `D=O(a)`, this is
(4.1). \(\square\)

Thus a viable exact-rainbow arc order cannot consist of a bounded number of
six-sector phases.  It must switch side type a linear number of times among
its `O(a)` total forced-ring trail blocks.  The perfectly recursive order
does make that many switches, but Theorem 3 shows that its extremely regular
nested switching is still too cheap in the heterogeneous run metric.

## 5. What remains alive

The two existing theorems and the new run-cover obstruction now impose
three simultaneous requirements on an exact- or near-rainbow construction
at surface error:

1. The frozen matching and trail ledger permit only `O(a)` maximal forced
   ring arcs, while the adjacent-shadow cut corollary requires `\Omega(a)`
   extra cuts.
2. The three positive outer supports must have a quadratic internal-run
   desert in every relevant induced near-outer order.
3. That desert must not admit a low-congestion cover by short internal runs
   of **other** coordinate thresholds.  If the assigned run-length budget is
   below `(4-\varepsilon)a^3`, equation (2.9) forces quadratic charge
   congestion.

The first two obvious schedules violate item 3.  Grouping sides into a few
macroscopic sectors gives the `3a^3` certificate of Proposition 4.  Nesting
the six sides radius by radius aligns all extreme deserts, but gives the much
stronger `a^3` certificate of Theorem 3.

The remaining exact-rainbow possibility is consequently quite irregular:
it needs `Theta(a)` side changes, only `Theta(a)` total arcs, outer extreme
supports concentrated enough to leave a quadratic desert, and yet no
linear-congestion assignment of cheap runs from the other `6a+O(1)`
coordinate thresholds.  This is a concrete finite combinatorial scheduling
problem; Lemma 1 supplies a proof-producing obstruction certificate for any
candidate order.

The near-rainbow escape is wider.  The unique-matching defect lemma permits
`O(a)` alternating defect paths, and one such path may contain many frozen
edges.  Nothing above bounds the geometric length of those paths.  The
present results therefore do not rule out:

* an irregular `Theta(a)`-arc permutation with no cheap heterogeneous run
  cover;
* a long alternating defect corridor which replaces substantial portions of
  several forced rings;
* a band whose selected middle-witness order is not the order of the obvious
  forced-ring occurrences; or
* completion of such a survivor to all upper shadows and exact lower target
  assignments.

What has been ruled out is the cleanest proposed resolution of the previous
audit gap: merely aligning the nested quadratic deserts by a recursive
six-side shelling is not sufficient.  It fails before upper-shadow
completion or lower Hall matching is reached.
