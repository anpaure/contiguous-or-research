# Catalan lifting as a punctured-prism braid

## 1. Purpose

This note replaces the informal “absorb one duplicated cap diamond” picture
by an exact ledger for the entire new middle layer.  The lower-middle
vertices admit an explicit decomposition into outer paths plus a very
specific induced subgraph: two tagged copies of the internal vertices of
every old complementary path.

That lower-vertex decomposition is not yet a middle-level path factor,
because upper edge colours must also be disjoint.  In the minimum-rung
completion scaffold, the upper-colour occurrence failure has the exact
sector imbalance

\[
                         (+D_m,-2D_m,+D_m).
\]

Thus the missing positive operation is precisely a repeated two-for-two
rank transfer in a punctured Johnson prism.  No finite-dimensional search
is involved.

## 2. Old complementary factor

Let `X` have size `2m`, and let

\[
 P=(x_0,y_0,x_1,y_1,\ldots,y_{m-1},x_m)
\tag{2.1}
\]

be a complementary path, where

\[
 |x_i|=m,\qquad |y_i|=m+1,\qquad
 x_i\subset y_i\supset x_{i+1},\qquad x_m=X\setminus x_0.
\tag{2.2}
\]

Let `mathcal P` be an exact complementary path factor.  Its paths partition
both middle levels of `2^X`.  Hence

\[
 |\mathcal P|=\operatorname {Cat}_m=:C_m.
\tag{2.3}
\]

Adjoin two new coordinates `p,q`.  The lower middle layer of
`2^(X union {p,q})`, of rank `m+1`, splits into the three rectangles

\[
\begin{array}{c|c}
\text{number of new coordinates}&\text{old rank}\\ \hline
0&m+1\\
1&m\\
2&m-1.
\end{array}
\tag{2.4}
\]

## 3. Two explicit outer paths

For every `P in mathcal P`, put

\[
\begin{aligned}
 O_0(P)={}&
 x_0p, y_0, y_1,\ldots,y_{m-1}, x_mq,\\
 O_2(P)={}&
 x_0q, (X\setminus y_{m-1})pq,
 (X\setminus y_{m-2})pq,\ldots,
 (X\setminus y_0)pq, x_mp.
\end{aligned}
\tag{3.1}
\]

Here juxtaposition means disjoint union.

### Lemma 1 (outer lower-path lemma)

Each word in (3.1) is a complementary Johnson path with exactly `m+2`
lower vertices.  Over all `P in mathcal P`, these `2C_m` paths are pairwise
disjoint on their lower vertices and cover:

1. every new middle vertex with zero new coordinates;
2. every new middle vertex with two new coordinates; and
3. precisely the four one-new-coordinate vertices
   `x_0p,x_0q,x_mp,x_mq` belonging to the endpoints of each old path.

### Proof

Consecutive `y_i,y_(i+1)` contain the common middle set `x_(i+1)`, so they
are Johnson-adjacent.  The first and final adjacencies of `O_0(P)` follow
from `x_0 subset y_0` and `x_m subset y_(m-1)`.  Its endpoints are
complementary because `x_m=X minus x_0`.

Complementation reverses Johnson adjacency.  Therefore the sequence

\[
 (X\setminus y_{m-1})pq,\ldots,(X\setminus y_0)pq
\]

is a Johnson path.  Since

\[
 X\setminus y_{m-1}\subseteq x_0,
 \qquad X\setminus y_0\subseteq x_m,
\]

its two boundary adjacencies in `O_2(P)` also hold.  The endpoints
`x_0q,x_mp` are complementary.

An exact old factor partitions all `x`-vertices and all `y`-vertices.
Taking complements also partitions the old rank-`m-1` layer.  The three
rank rectangles in (2.4) are disjoint, proving both disjointness and the
coverage statement.  QED.

The qualifier “on their lower vertices” is essential.  Consecutive lower
vertices determine upper edge colours, and the `O_0(P)` paths can repeat
those colours.  Section 5 gives the exact discrepancy.

## 4. Exact leftover graph

After deleting the vertices in Lemma 1, the uncovered new middle vertices
are exactly

\[
 \mathcal V_{\rm int}
 =\{x_ip,x_iq:
       P\in\mathcal P, 1\le i\le m-1\}.
\tag{4.1}
\]

For each old path they come with two prescribed internal segments

\[
 S_p(P)=(x_1p,\ldots,x_{m-1}p),\qquad
 S_q(P)=(x_1q,\ldots,x_{m-1}q).
\tag{4.2}
\]

The induced graph on all one-new-coordinate vertices is the two-sheeted
Johnson prism

\[
 J(2m,m)\square K_2:
\quad xp\sim xq,qquad xp\sim x'p
       \Longleftrightarrow x\sim x'.
\tag{4.3}
\]

Its antipodal involution is

\[
 xp\longleftrightarrow (X\setminus x)q.
\tag{4.4}
\]

Thus `mathcal V_int` is obtained from that prism by deleting the four tagged
endpoint vertices of every path in the old factor.

Put

\[
 D_m=C_{m+1}-2C_m.
\tag{4.5}
\]

The Catalan ratio gives the exact mass identity

\[
 D_m={2(m-1)\over m+2}C_m,
 \qquad
 (m+2)D_m=2(m-1)C_m=|\mathcal V_{\rm int}|.
\tag{4.6}
\]

### Theorem 2 (exact lower-support completion equivalence)

Keeping the lower-vertex paths (3.1), the unused lower middle layer can be
partitioned into the correct number of complementary Johnson paths if and
only if `mathcal V_int` can be partitioned into `D_m` Johnson paths, each
having `m+2` vertices and antipodal endpoints.

This theorem concerns lower support only.  An exact middle-level factor
additionally requires the upper edge colours of all paths to be pairwise
distinct and exhaustive.

### Proof

Every complementary path in dimension `2m+2` has `m+2` lower-middle
vertices.  Lemma 1 has already supplied `2C_m` lower-vertex paths.  A full
factor has `C_(m+1)` paths, so exactly `D_m` remain.  Its unused lower support
is exactly (4.1), and (4.6) gives precisely the required number of vertices.
Therefore a partition into the stated complementary paths is both necessary
and sufficient at the lower-support level.  QED.

## 5. Exact upper-colour imbalance

Every edge of a lower Johnson path is labelled by the union of its two
endpoints, a rank-`m+2` upper vertex.  Split those upper vertices by the
number `t` of new coordinates.

The path `O_2(P)` has upper colours

\[
 x_0pq, (X\setminus x_{m-1})pq,\ldots,
 (X\setminus x_1)pq, x_mpq.
\tag{5.1}
\]

Across the old factor these are every `t=2` upper vertex exactly once.

The two boundary edges of `O_0(P)` have `t=1`.  Its `m-1` internal upper
colours are

\[
                         y_i\cup y_{i+1}
                         \qquad(0\le i<m-1),
\tag{5.2}
\]

and have `t=0`.  Thus the outer paths contribute

\[
\begin{array}{c|ccc}
t&0&1&2\\ \hline
\text{edge occurrences}&(m-1)C_m&2C_m&(m+1)C_m.
\end{array}
\tag{5.3}
\]

Any complementary path contained in the one-tag prism changes its tag an
odd number of times.  Consider first the **minimum-rung scaffold**, in which
each of the `D_m` leftover paths changes tag exactly once.  It then has one
`t=2` rung edge and `m` same-sheet `t=1` edges.  Adding these gives

\[
\begin{array}{c|ccc}
t&0&1&2\\ \hline
\text{provisional occurrences}&
(m-1)C_m&2C_m+mD_m&(m+1)C_m+D_m.
\end{array}
\tag{5.4}

The numbers of available upper vertices are

\[
\begin{array}{c|ccc}
t&0&1&2\\ \hline
\text{targets}&
\binom{2m}{m+2}&2\binom{2m}{m+1}&\binom{2m}{m}.
\end{array}
\tag{5.5}

Using

\[
 \binom{2m}{m+2}=(m-1)C_m-D_m,
 \quad
 \binom{2m}{m+1}=mC_m,
 \quad
 \binom{2m}{m}=(m+1)C_m,
\tag{5.6}
\]

the difference “provisional occurrences minus targets” is exactly

\[
                         \boxed{(+D_m,-2D_m,+D_m).}
\tag{5.7}

In particular, keeping `O_2` unchanged is impossible: it already exhausts
all `t=2` colours, while every leftover antipodal prism path needs at least
one `t=2` rung.  Likewise the `O_0` paths have exactly `D_m` excess `t=0`
**occurrences**.  This is only a count: their multiset (5.2) may also have
holes, in which case it has `D_m` plus the number of holes in repeated
occurrences.  Surjectivity of the `t=0` colour map is a separate gate.

Within the minimum-rung scaffold, an exact Catalan completion must perform
precisely `D_m` net two-for-two transfers

\[
                 (\text{one }t=0\text{ edge})
                 +(\text{one }t=2\text{ edge})
                 \longrightarrow
                 (\text{two }t=1\text{ edges}).
\tag{5.8}

This is the smallest possible global conservation law behind the required
rhombus braid.  If some residual path uses `1+2s` rungs, then two additional
`t=2` occurrences must also be transferred for every such extra pair.

### Canonical indexing of the minimum transfers

Let

\[
 R=\{x_i:P\in\mathcal P, 1\le i\le m-1\}
\tag{5.11}
\]

be the old internal middle vertices.  Every `x_i in R` canonically indexes
both

\[
 e_x=y_{i-1}y_i
 \quad\hbox{and}\quad
 r_x=(x_ip)(x_iq).
\tag{5.12}

Their old intersection is the same set `x_i`, so Lemma 3 pairs `e_x` and
`r_x` without any matching choice.  Define the zero-tag colour map

\[
 g:R\longrightarrow\binom{X}{m+2},qquad
 g(x_i)=y_{i-1}\cup y_i.
\tag{5.13}

Since

\[
 |R|=(m-1)C_m,qquad
 \left|\binom{X}{m+2}\right|=|R|-D_m,
\tag{5.14}

the fixed `O_0` scaffold contains every zero-tag target if and only if `g`
is surjective.  In that case choose a transversal `T subset R` containing
one member of each fibre and put

\[
                         S=R\setminus T.
\tag{5.15}

Then `|S|=D_m`, and the canonical squares indexed by `S` are exactly the
minimum set of removable zero-tag occurrences paired with their prism
rungs.

Consequently the minimum exact gate can be stated without a colour/rung
matching:

> Given a surjective map (5.13) and a fibre transversal `T`, factor the
> punctured prism into antipodal one-rung paths whose rung set is exactly
> `S=R minus T`; after the canonical square switches, require the resulting
> one-tag upper colours to be bijective and the endpoint strands to remain
> complementary.

This couples three conditions—prism path ownership, one-tag colours, and
endpoint topology—but removes the formerly apparent fourth condition of
matching excess edges to rungs.

### Lemma 3 (atomic rank-transfer square)

Let `U_0,U_1` be adjacent old rank-`m+1` sets and put

\[
                         x=U_0\cap U_1.
\]

The four new lower-middle vertices

\[
                         U_0,quad U_1,quad xp,quad xq
\]

span the Johnson four-cycle

\[
                         U_0-U_1-xq-xp-U_0
\tag{5.9}
\]

(with the other cross orientation equally valid).  Replacing the opposite
edges

\[
                         U_0U_1,quad (xp)(xq)
\]

by

\[
                         U_0(xp),quad U_1(xq)
\]

changes their upper-colour sector counts by

\[
                         (-1,+2,-1).
\tag{5.10}

### Proof

The old sets `U_0,U_1` intersect in the `m`-set `x`, so they are
Johnson-adjacent and their union has zero new coordinates.  The tagged
copies `xp,xq` differ only in their tag, so they are Johnson-adjacent and
their union has both new coordinates.  Since `x subset U_i`, each displayed
cross pair is Johnson-adjacent and its union has exactly one new coordinate.
The switch preserves the degree of all four lower vertices and has the
claimed colour change.  QED.

Thus the arithmetic transfer (5.8) has an exact local graph move.  The hard
part is no longer local adjacency; it is **global strand topology**.  A
single switch between two complementary paths generally exchanges their
tails and destroys the antipodal endpoint pairing.  The switches must be
scheduled in alternating circuits (or accompanied by endpoint transfers)
so that every final component again has one complementary endpoint pair and
the prescribed length.  This is the integral braid condition absent from
the scalar ledger.

## 6. The bounded-cut strengthening needed for OR shadows

The bare path factor in Theorem 2 settles middle support only.  For the OR
problem we need a structured version.

### Punctured-prism braid lemma (open)

For a suitable exact old complementary factor `mathcal P`, reroute the
outer paths and the tagged internal segments so that:

1. every lower and upper middle vertex is owned exactly once;
2. the rerouting realizes at least the `D_m` transfers in (5.8), with
   equality in the minimum-rung scaffold;
3. each prescribed tagged segment (4.2) is cut at `O(1)` positions on
   average; and
4. the total number of new seams is `O(C_m)`.

By Lemma 3, the minimum transfer can be realized locally whenever a selected
removable `t=0` occurrence is paired with a selected prism rung having the
same old intersection.  The remaining requirements are:

* first ensure that the map `g` in (5.13) is onto and choose a fibre
  transversal;
* construct one-rung prism paths with the forced complementary rung set;
* make their same-sheet and switched cross edges biject the one-tag upper
  colours; and
* arrange the resulting tail exchanges into circuits whose final endpoint
  pairing is the complement involution.

This is a substantially smaller matching/flow problem than arbitrary path
factor completion.

A uniform worst-case `O(1)` bound per old path would be stronger than
necessary; the total bound is the quantity used by halo compression.

If this lemma holds, every old central-band window away from those cuts is
transported to both fixed tags.  Two tagged copies of an old repair word
cost `2R_(m,H)`, and radius-`O(H)` halos around `O(C_m)` seams cost
`O(HC_m)`.  Consequently

\[
 R_{m+1,H}\le 2R_{m,H}+O(HC_m).
\tag{5.1}
\]

By the contractive-repair theorem in `CONTRACTIVE_DEFECT_LIFT.md`, (5.1)
would imply

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{5.2}
\]

## 7. Why this is a genuine simplification

The formerly proposed pair of coordinate-cut Cartesian sectors overlaps in
one cap diamond per old path and leaves the remaining Catalan sectors
unspecified.  The ledger above accounts for every rank rectangle exactly:

* the outer paths are explicit and disjoint on lower support;
* the leftover vertex set is explicit;
* the required number and length of completion paths follow from the exact
  Catalan identity; and
* upper-edge ownership has one exact imbalance vector, rather than an
  unclassified collision problem.

The only missing positivity statement is the bounded-cut realization of the
`D_m` rank transfers (5.8).  This is an all-dimensional absorber problem,
not a request to improve one finite `k` certificate.
