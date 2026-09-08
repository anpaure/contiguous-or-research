# Every fixed incidence matching has an explicit invariant core

This is a finite construction lemma, not a 42-row full-cube cover. It extends
the lower-owner orientation observation in
`binary10_involution_scd_core_20260907.py` by eliminating both the SCD and the
sign-search requirements for the ten invariant rows.

Partition ten coordinates into five labelled pairs, exchanged by an involution.
Let `A -> B(A)` be any perfect matching between the two- and three-subsets of
the five pair labels, with `A` contained in `B(A)`.

**Claim.** There are ten invariant full `5+5` prefix rectangles, one per matched
incidence, whose 160 rank-4, rank-5, and rank-6 targets are all distinct. They
cover all twenty involution-fixed targets at these ranks.

## Construction

For each owner `A`, select a last pair label `j(A)` outside `B(A)`, as below.
Order the pair labels by the two members of `A` (either order), the member of
`B(A) \ A`, the other label outside `B(A)`, then `j(A)`. Orient each pair by
membership in `A`: one shore chooses its second coordinate on labels in `A`
and its first coordinate elsewhere; the other shore chooses the mates. Give
both shores the displayed pair order. This row is invariant under the
coordinate involution and has its prescribed fixed targets `A` and `B(A)`.

Here are the requirements on the last labels. Join two disjoint owners `A,A'`
by an edge labelled `j` if their union is all labels except `j` and `j` is an
allowed last label for both. We must not have both endpoints choose that edge's
label. Each owner has two allowed labels; each allowed label has at most one
conflicting partner. The conflict graph therefore has maximum degree two.

In a cycle component, let each vertex choose the label on its next edge in a
cyclic orientation. In a path component, choose at one endpoint an allowed
label not belonging to its incident edge, and let every other vertex choose
the label on the edge toward that endpoint. For an isolated vertex choose
either label. No edge has its label chosen at both endpoints. This constructs
all the `j(A)` without search.

## Complete collision check

A row target has a uniquely determined set `F` of doubly occupied pairs and
set `E` of nonempty pairs. If the prefix lengths are `i <= j`, then `F` is
the first `i` pair labels, `E` the first `j`, and the singleton choices on
`E \ F` are encoded by `A \ F`, up to complementing all singleton choices.
Its coordinate rank is `i+j`. Distinct `(F,E)` cannot yield the same target.

At rank 4 the possibilities `(i,j)` are `(0,4),(1,3),(2,2)`.

- For `(1,3)`, `E=B(A)` identifies the row, since the upper owners are distinct.
- For `(2,2)`, `F=E=A` identifies the row.
- For `(0,4)`, `E` omits the last label. Distinct owners cannot have equal
  singleton choices. They have complementary choices exactly when their
  disjoint union is `E`. This is precisely the collision excluded by the
  last-label selection.

At rank 5 the possibilities are `(0,5),(1,4),(2,3)`.

- For `(0,5)`, the encoding `A` has size two in a five-set; distinct owners
  are neither equal nor complementary.
- For `(1,4)`, the encoding `A \ F` has size one in a three-set. Complementarity
  is impossible; equality, with the same `F`, identifies `A`.
- For `(2,3)`, `F=A` identifies the row.

At rank 6 the possibilities are `(1,5),(2,4),(3,3)`.

- For `(1,5)`, the encoding has size one in a four-set; the same reasoning
  excludes collisions between distinct owners.
- For `(2,4)`, `F=A` identifies the row.
- For `(3,3)`, `F=E=B(A)` identifies the row.

Each row has respectively 5, 6, and 5 targets at these ranks. The twenty fixed
targets are the doubled pair sets `A` and `B(A)`, all distinct by hypothesis.
This proves the claim.

## Executable form and scope

`binary10_involution_matching_core_20260907.py` implements this construction.
Its `--verify-all` mode enumerates every fixed matching and checks the literal
rectangle targets, rather than merely the last-label constraints. Under the
compute policy, run verification only via explicit `ssh h100`.

Verification was run on h100 on 2026-09-07 and passed for all 60 matchings:
each constructed core had ten literal rows, 160 distinct tight targets, and
all twenty fixed tight targets. The proof above does not depend on this check.

The lemma removes the need to search for a tight-disjoint invariant core and
permits choosing any of the three matching-isomorphism types. It does not
establish that any core extends by sixteen nonfixed row orbits to a full
42-row cover. The full all-rank residual constraints remain necessary.

## A necessary local ordering condition for extension

There is a reason not to choose the first two owner labels in increasing order.
Orient the edge `{i,j}` of the complete graph on pair labels from the label put
first to the one put second. For each label `j`, consider the transversal
middle target with exactly one exceptional singleton sign, at `j`. Its orbit
is not covered by this lower-owner-oriented core. For each edge `i -> j`,
the core row owned by `{i,j}` already covers its rank-6 neighbor obtained by
doubling pair `i`. These blocked neighbors are distinct.

Such a transversal middle target cannot be an endpoint of an admissible
nonfixed row: that would give a transversal shore split and repeat its
involution orbit. As an interior middle target, it needs two distinct upper
neighbors in that row. Hence a completable core must have at least two of its
five upper neighbors free; in particular, the first-pair tournament cannot
have a vertex of indegree four.

Increasing order has just such a sink. An exhaustive catalogue check on h100
confirmed that the first constructed class-6 core had two missing residual
orbits, masks 373 and 496; the latter is the exceptional-sign target at the
sink, up to involution. The exact omission excludes that particular core.

The executable now uses the regular tournament `i -> j` when
`j-i mod 5` is 1 or 2. Each indegree is two. This preserves the construction
lemma and removes the sink obstruction; it does not itself prove completion.

## All last-label choices, not just the canonical one

Let `f(A)` be the complement of `B(A)`, a two-subset disjoint from `A`.
The graph of disjoint two-subsets of a five-set is the Petersen graph. For an
edge `A,A'`, let `j` be the missing fifth label. The choice `j` is forbidden
at `A` exactly when `f(A)=A'`. Consequently, the last-label conflict graph is
the Petersen graph with every edge used by `f` in either direction deleted.
A vertex in a 2-cycle of `f` has remaining degree two; a vertex in any longer
cycle has remaining degree one.

All feasible last-label choices can be parametrized independently on the
components. On a path of `m` edges, list the `m+1` vertices from left to right.
Their two choices are left or right, with the endpoint's outward choice free.
The only forbidden consecutive choice pattern is right-then-left. Therefore
the valid assignments are exactly `L*R*`, numbering `m+2`. On a cycle only
the two consistently oriented assignments are valid.

For the three incidence-permutation types in the sixty-matching census, this
gives the following complete counts per matching:

| Cycle type of `f` | Conflict components | Last-label choices |
| --- | --- | ---: |
| five 2-cycles | two 5-cycles | 4 |
| two 5-cycles | five separate edges | 243 |
| one 2-cycle and one 8-cycle | two length-2 paths and two edges | 144 |

For the last case the two degree-two vertices cannot be adjacent, since their
common 2-cycle edge was deleted. Thus they lie internally in two distinct
length-2 paths. The executable exposes all assignments through
`BINARY10_LAST_VARIANT`, default zero. Its variant zero was checked on h100 to
preserve every one of the sixty previously screened literal cores exactly.
Changing a last-label variant changes the literal core; it is not merely a
solver seed change. None of these counts imply full-cube extendability.

### Exact residual neighborhood counts

Write the coordinate pair with label `i` as `{v_i^0,v_i^1}` and put
`T_Z={v_i^1:i in Z} union {v_i^0:i not in Z}`. Thus the coordinate
involution takes `T_Z` to `T_(Z^c)`. Let `K` be the union of the ten core
rectangles, let `j(A)` be the last label in the row owned by `A`, and let
`d^-(i),d^+(i)` be the indegree and outdegree of the first-pair tournament.
The following statements hold for every matching and every permitted
last-label selection in the construction above.

The core's transversal middle targets are exactly the `T_Z` with
`|Z| in {2,3}`. Hence the six missing transversal orbits have representatives
`T_empty` and `T_{i}`, `0<=i<5`.

1. All five lower and all five upper neighbors of `T_empty` are outside `K`.
2. All five lower neighbors of `T_{i}` are outside `K`. Exactly `d^-(i)`
   of its five upper neighbors are in `K`.

To check the lower statements, a lower neighbor of a transversal has no
doubled pair and exactly four nonempty pairs. A core target of this form
has precisely two exceptional signs on those four pairs, in either shore
orientation. The stated lower neighbors have zero or one. An upper neighbor
has one doubled pair `a` and all five pairs nonempty. The core can produce
such a target only from prefix lengths `(1,5)` or `(5,1)`. Its owner is
`{a,c}`, its first pair is `a`, and its exceptional signs on the other four
pairs are either `{c}` or its complement. Consequently the upper neighbor
of `T_{i}` obtained by doubling `a` lies in the core exactly when `a -> i`.
The neighbor doubling `i` has no exceptional sign outside its doubled pair
and is not in the core. This proves the exact counts, not merely bounds.

There is a second useful family. Fix a label `i` and a two-subset
`Z` of the other four labels, and let `U(i,Z)` contain both coordinates
of pair `i` and the coordinate `v_a^1` or `v_a^0` according as `a in Z`
or `a not in Z`, for every `a != i`. This is a rank-six target outside
`K`: it has two exceptional signs on its four singly occupied pairs,
whereas a core target with the same doubled/nonempty pattern has one or
three. Of its six rank-five predecessors:

* the two obtained by undoubling pair `i` are in `K`, since they are
  transversal targets with two or three exceptional signs;
* for each `a != i`, the predecessor obtained by deleting the coordinate
  at pair `a` lies in `K` exactly when

  `i -> c(a)` and `j({i,c(a)})=a`,

  where `c(a)` is the other member of the part containing `a` in the
  partition `{Z, [5] \\ (Z union {i})}` of the other four labels.

Indeed this predecessor has doubled-pair set `{i}` and nonempty-pair set
`[5] \\ {a}`. Its only possible core prefix lengths are `(1,4)` and `(4,1)`.
If `a in Z`, its remaining exceptional sign is `{c(a)}`; if `a not in Z`,
its exceptional signs are the complement of `{c(a)}` inside the three
singly occupied pairs. Thus its unique possible owner is `{i,c(a)}`, with
first pair `i` and last pair `a`. The four values `c(a)` are distinct, so
at most `d^+(i)` of these four predecessors are core-covered. Therefore

\[
 \#\{V\subset U(i,Z):|V|=5,\ V\notin K\}
       \ge 4-d^+(i).                                      \tag{1}
\]

In a regular tournament, every residual one-sign transversal has exactly
three free upper neighbors, and every `U(i,Z)` has at least two free middle
predecessors. This addresses both local defect types above. It remains a
necessary-neighborhood improvement, not an integral completion theorem.

For context, the threshold two in (1) is necessary: every rank-six target
of a full `5+5` prefix rectangle has two different rank-five predecessors
in that rectangle, obtained by shortening either nonempty prefix. A new
row cannot use a core-covered middle target, because ranks four through
six must be exact partitions in a 42-row solution. The analogous fact for
an internal middle target gives the two-upper-neighbor condition used
earlier.

Independent literal verification on h100 on 2026-09-07, using
`../scripts/check_binary10_core_neighborhoods_20260907.py`, passed all 60
matchings under both increasing and regular first orders: 120 cores, 720
transversal-neighborhood cases, and 3,600 rank-six-neighborhood cases. The
checker tests the exact membership equivalences above, not just degree
inequalities. The analytic proof does not use these checks as a premise.
