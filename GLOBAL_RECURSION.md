# Catalan compression and dimension recursion

This note pursues a dimension-recursive construction for universal
contiguous-OR words.  It deliberately separates statements about central
Boolean layers from statements about completed OR words.

The main new proved facts are:

1. the pure **Catalan-compressed consecutive-union row** exists in every even
   dimension, by a direct consequence of the saturating-cycle theorem for
   consecutive levels of the cube; and
2. the Greene--Kleitman symmetric-chain decomposition canonically induces a
   two-sided colour-perfect forest on the middle layer with exactly one
   Catalan number of components.

Neither fact, by itself, proves a new all-rank OR upper bound.  The exact
remaining requirements are stated below.

Throughout, put

\[
 W=\binom{2m}{m},\qquad
 K=\operatorname{Cat}_m=\frac{1}{m+1}\binom{2m}{m},\qquad
 N=\binom{2m}{m+1}=W-K.
\]

Here `W` is the even-dimensional Boolean width, `K` is the Catalan defect,
and `N` is the size of either adjacent layer.

## 1. A proved Catalan-compressed union cycle

We use the following published theorem.

> **Saturating-cycle theorem** (Gregor--Mička--Mütze).  The subgraph of
> an `n`-cube induced by any consecutive sequence of levels has a saturating
> cycle: a cycle visiting every vertex in the smaller bipartition class.

This is Corollary 2 of [Gregor, Mička, and Mütze, *On the central levels
problem*](https://arxiv.org/abs/1912.01566).  Apply it to levels `m` and
`m+1` of the `2m`-cube.  Since those levels have sizes `W` and `N`,
respectively, it gives a cyclic alternating sequence

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,                 \tag{1.1}
\]

where the `U_i` are all `(m+1)`-sets, the `C_i` are `N` distinct `m`-sets,
and

\[
 C_i\subset U_i\supset C_{i+1}                              \tag{1.2}
\]

with cyclic indices.

### Theorem 1 (contiguous-colour Hamilton cycle)

There is a Hamilton cycle `P` in `J(2m,m)` such that, for every `(m+1)`-set
`U`, all edges of `P` whose union colour is `U` form one nonempty contiguous
block.  Consequently, compressing equal consecutive union colours of `P`
gives a Hamilton cycle through the complete `(m+1)`-layer, of exact length

\[
 N=W-K.                                                       \tag{1.3}
\]

#### Proof

The cycle (1.1) uses `N` of the `W` middle sets.  For each of the remaining
`K` middle sets `X`, choose arbitrarily one `(m+1)`-set `U_i` containing it,
and assign `X` to `U_i`.  Such a set exists (in fact there are `m` choices).

For every `i`, list between `C_i` and `C_{i+1}` all middle sets assigned to
`U_i`, in an arbitrary order.  Every listed set is an `m`-subset of `U_i`.
Any two distinct `m`-subsets of the same `(m+1)`-set differ by one exchange,
so they are adjacent in `J(2m,m)` and their union is exactly `U_i`.

Concatenating these `N` blocks cyclically visits:

* every seam vertex `C_i` once; and
* every formerly unused middle vertex once, in its assigned block.

It is therefore a Hamilton cycle `P` of the entire middle layer.  The edges
in block `i` all have union colour `U_i`; the block is nonempty because it at
least joins the distinct seam vertices `C_i,C_{i+1}`.  Different blocks have
different colours because (1.1) visits every `U_i` exactly once.  Compressing
the colour blocks yields the order `U_0,...,U_{N-1}`.  Consecutive colours
`U_i,U_{i+1}` meet in the `m`-set `C_{i+1}`, so this compressed order itself
is a Hamilton cycle in `J(2m,m+1)`.  QED.

The case `m=1`, where the conventional saturating cycle is a single edge, is
the direct two-vertex construction and satisfies the same conclusion.

### What this settles

The handoff previously isolated the following as the central combinatorial
part of a possible even-to-odd recursion:

> Find a Hamilton middle-layer order whose adjacent-union colours each occur
> in one interval, so that their compression has length `W-Cat_m`.

Theorem 1 proves exactly that statement for every `m`.  No search and no
unproved Hamiltonicity assertion is needed.

It does **not** prove that the same `P` has complete lower intersection
colours, long coordinate runs, deeper consecutive shadows, or a pinnable
factor.  Those extra properties must not be folded into Theorem 1.

## 2. Exact width-preserving even-to-odd central braid

Theorem 1 gives an exact central-row recursion, again without yet giving a
completed OR word.

Choose the cyclic indexing in (1.1).  Cut `P` at `C_0`.  If necessary, assign
one unused middle set to the block immediately preceding the cut; this
ensures that deleting the cyclic closing edge does not delete the only
occurrence of its union colour.  (For `m=1` this is automatic.)  Let `z` be a
new coordinate and define

\[
 T=(U_{N-1},U_{N-2},\ldots,U_0)
       \;\Vert\;
   (\{z\}\cup P_0,\{z\}\cup P_1,\ldots,\{z\}\cup P_{W-1}),  \tag{2.1}
\]

where `P_0=C_0`.

### Theorem 2 (exact central parity braid)

`T` is a Hamilton path through the rank-`m+1` layer of the `(2m+1)`-cube.
Its length is exactly

\[
 N+W=2W-K=W(2m+1).                                         \tag{2.2}
\]

#### Proof

The first section lists every old `(m+1)`-set once.  The second section lists
every new-bit `(m+1)`-set once because `P` lists every old `m`-set once.  The
two sections are disjoint and exhaust the new middle layer.

Inside the first section, consecutive `U`'s are Johnson-adjacent by (1.1).
Inside the second section, adjacency follows from the Hamilton cycle `P`.
At the unique seam, `C_0\subset U_0`, so `U_0` and `{z}\cup C_0` differ by
one exchange.  Thus every consecutive pair in (2.1) is Johnson-adjacent.
QED.

### Exact first-shadow ledger

The construction gives more precise information than mere Hamiltonicity.

* The `N-1` intersections internal to the reversed `U` section, together
  with the seam intersection, are exactly the `N` distinct sets
  `C_0,...,C_(N-1)`.  Hence exactly

  \[
    W-N=K                                                        \tag{2.3}
  \]

  old rank-`m` sets are absent from this part of the lower shadow.
* The adjacent unions inside the `{z}\cup P` section include every set
  `{z}\cup U_i`; the cut convention above retains at least one edge of every
  union-colour block.
* Completeness of the new-bit lower colours is equivalent to completeness of
  the rank-`m-1` intersection colours of `P`.
* Completeness of the old no-`z` upper colours is equivalent to the required
  longer union shadow of the compressed `U` path.

Thus (2.1) exactly realizes the binomial/Catalan vertex count and one full
new-bit upper colour layer, but leaves two explicitly identified opposite
shadow conditions.  This is the honest boundary between theorem and
conjecture.

The incidence word of `z` in (2.1) is one zero block followed by one boundary
one block, so `z` itself creates no forbidden internal one-run.  No comparable
run assertion for the old coordinates follows from the saturating-cycle
theorem.

## 3. The Greene--Kleitman Catalan forest

There is also a canonical **two-sided** object.  It covers both adjacent
colour layers perfectly, but it is a forest rather than a Hamilton path.

Every Johnson edge on the middle layer has two colours

\[
 c(P,Q)=P\cap Q\in\binom{[2m]}{m-1},\qquad
 u(P,Q)=P\cup Q\in\binom{[2m]}{m+1}.                       \tag{3.1}
\]

Conversely, every incidence pair `S subset U` of ranks `m-1,m+1` determines
the unique Johnson edge between the two intermediate `m`-sets.  Thus Johnson
edges are in bijection with edges of the inclusion graph

\[
 \mathcal I_m=\left(\binom{[2m]}{m-1},
                     \binom{[2m]}{m+1};\subset\right).       \tag{3.2}
\]

### Theorem 3 (Catalan colour-perfect forest)

There is a perfect matching of `\mathcal I_m` whose `N` induced Johnson edges
form a spanning forest on the `W` middle vertices with exactly `K` connected
components.

Every rank-`m-1` intersection colour and every rank-`m+1` union colour occurs
exactly once among these forest edges.

#### Proof

Take the Greene--Kleitman SCD of the `2m`-cube.  Every nonsingleton symmetric
chain contains exactly one set `S` of rank `m-1` and exactly one set `U` of
rank `m+1`, and `S subset U`.  Since the SCD partitions both ranks, pairing
these two members in every nonsingleton chain is a perfect matching of
`\mathcal I_m`.

We now prove acyclicity of the induced Johnson edges.  Write a Greene--Kleitman
chain template as fixed Dyck blocks separated by stars

\[
 w_0 * w_1 *\cdots * w_{2t}.
\]

Its middle member `P` has the first `t` star positions equal to `1` and the
last `t` equal to `0`.  If the star positions are
`e_1<...<e_(2t)`, then the rank-`m-1` predecessor and rank-`m+1` successor
are

\[
 S=P\setminus\{e_t\},\qquad U=P\cup\{e_{t+1}\}.             \tag{3.3}
\]

The other middle vertex in the interval `[S,U]` is

\[
 f(P)=P\setminus\{e_t\}\cup\{e_{t+1}\}.                    \tag{3.4}
\]

Orient the induced Johnson edge from `P` to `f(P)`.  Every middle vertex
belonging to a nonsingleton SCD chain has exactly one outgoing edge.  A middle
vertex in a singleton chain has none.

The potential

\[
 \Phi(P)=\sum_{x\in P}x                                      \tag{3.5}
\]

strictly increases along every oriented edge, by
`e_(t+1)-e_t>0`.  Hence there is no directed cycle.  There is no undirected
cycle either: on an undirected cycle, the number of edges equals the number
of vertices, and outdegree at most one would force every cycle vertex to
orient one cycle edge, producing a directed cycle.

The number of singleton Greene--Kleitman chains is

\[
 \binom{2m}{m}-\binom{2m}{m-1}=K.                           \tag{3.6}

There are therefore `N=W-K` forest edges on `W` vertices, so the forest has
exactly `K` components.  The perfect-matching construction already proves
the exact two-sided colour statement.  QED.

### A necessary correction: the forest is not linear

It is tempting to say that `K-1` additional bridges now turn the forest into
a Hamilton path.  That is false unless every component is already a path.
The Greene--Kleitman forest branches.

For example, in dimension six the singleton-chain root

```text
010101
```

has the three distinct predecessors

```text
100101,  011001,  010110.
```

In each word, the central two unmatched symbols are `10`, and (3.4) changes
them to the corresponding `01`, producing `010101`.  The root therefore has
degree three.  A Hamilton path cannot retain all three incident matched
edges.

So acyclicity is a real theorem, but **acyclicity alone is insufficient**.
Any claim that only `K-1` arbitrary bridges finish the construction has a
degree gap.

### The cyclic-parenthesis variant has the same degree obstruction

Another natural incidence bijection is circular rather than linear.  For an
`(m-1)`-set, repeatedly cancel cyclic adjacent `01` pairs in its binary word.
Exactly two `0` symbols remain; flip both to `1`.  The reverse cancellation
on an `(m+1)`-set shows that this is a bijection to the upper adjacent layer.

This modification does **not** make the induced middle graph linear.  In
dimension six, the balanced middle word

```text
P = 010101
```

is incident with all three matched pairs below:

| lower word `S` | cyclic unmatched zeros | upper word `U` | other middle endpoint |
|---|---|---|---|
| `000101` | positions `1,2` | `110101` | `100101` |
| `010001` | positions `3,4` | `011101` | `011001` |
| `010100` | positions `5,6` | `010111` | `010110` |

In every row, `P` is one of the two intermediate middle sets between `S` and
`U`.  Hence `P` has degree three.  The most obvious rotation-equivariant
replacement for the Greene--Kleitman matching therefore fails the exact same
maximum-degree gate; it does not prove the Catalan linearization lemma.

## 4. Exact matching formulation of the missing central theorem

Theorem 3 suggests the correct next lemma.

### Catalan linearization lemma (open)

Find a perfect matching `M` in `\mathcal I_m` such that its induced Johnson
edges form an endpoint-connectable linear forest: a spanning acyclic graph of
maximum degree at most two whose `K` path components can be oriented and
joined by `K-1` additional Johnson edges into one Hamilton path.

If this lemma holds, the resulting Hamilton path has:

* every rank-`m-1` intersection colour at least once;
* every rank-`m+1` union colour at least once; and
* exactly `K-1` surplus transitions, whose colours may repeat.

The component count is forced: a perfect matching contributes `N=W-K`
edges, so any acyclic induced graph on `W` middle vertices has exactly `K`
components.

An equivalent constructive direction is to begin with the Greene--Kleitman
matching and perform alternating-cycle switches in the incidence graph
`\mathcal I_m`.  Such a switch preserves the perfect coverage of both colour
layers.  The missing theorem is that switches can eliminate every degree at
least three and arrange connectable endpoints without creating cycles.

Even this lemma is only a **central two-sided skeleton theorem**.  A completed
OR recursion must additionally control longer union/intersection shadows and
the coordinatewise pinning/factorization constraints.

## 5. Why the naive SCD product recursion has hidden seam cost

The standard SCD product with a new coordinate `z` splits an old chain into
one long lifted chain and, except at the centre, one short lifted chain.  It
is natural to try to visit those two new chains consecutively in an MTF--SCD
tour.  One half of that move is indeed cheap: from a state

\[
 (B,e_1,\ldots,e_h,z,\ldots)
\]

exposing the long chain, updating `B union {z}` exposes the corresponding
short chain in one step.

The return to the next long-chain state is not one step.  The following
recency observation makes the obstruction exact.

### Lemma 4 (age-depth bound)

Immediately after an update containing `z`, the block containing `z` is the
first block of the last-occurrence ordered partition.  After `q` subsequent
updates that omit `z`, at most `q` blocks can lie before the `z` block.

#### Proof

An update omitting `z` inserts one new front block.  Removing updated
elements from old blocks preserves the relative order of all nonempty
remainders, including the remainder containing `z`.  Hence one update can
increase the number of blocks before `z` by at most one.  Induction proves
the claim.  QED.

To expose the standard long lift of a chain with `h` old singleton increments,
the `z` block must occur after those `h` increment blocks (and after the
nonempty minimum block, when present).  Lemma 4 therefore forces at least
`h` intervening updates after a short-chain state that has just refreshed
`z`.

Typical central Greene--Kleitman chains have `Theta(sqrt(m))` free
coordinates.  Thus a local recursion that physically restores the age of
`z` after every chain pair pays a nonconstant cost per pair.  A valid
near-width recursion must instead globalize the new-coordinate schedule, or
carry virtual endpoint states and resolve them in one global splice.  This is
the MTF analogue of the previously identified recursive seam-padding error.

## 6. Strongest rigorous recursion ledger

The current mathematical status is now:

### Proved

1. A Catalan-compressed consecutive-union Hamilton cycle exists in every
   even middle layer (Theorem 1).
2. It gives an exact width-preserving even-to-odd Hamilton **central row**
   with one legal seam and the first-shadow ledger in Section 2.
3. The Greene--Kleitman SCD gives a two-sided colour-perfect Catalan forest
   (Theorem 3).
4. The forest may branch, and naive local SCD lifting has a quantified recency
   cost (Lemma 4).

### Not proved

1. The Catalan linearization lemma.
2. Simultaneous long coordinate runs and deeper two-sided shadows for either
   Theorem 1 or Theorem 3.
3. A pin-surviving factor/labeling inherited by the parity braid.
4. An all-rank recursion attaining `B(k)`, `W(k)+O(k)`, or
   `(1+o(1))W(k)`.

Accordingly, this note proves a substantially stronger central reduction but
does **not** claim a new general OR-array upper bound.  The sharpest next
purely mathematical target is the incidence-matching linearization theorem,
followed by a shadow-and-pinning inheritance theorem for the exact braid
(2.1).
