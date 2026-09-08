# Relative PBBS grafting of the common-history `C8`: the exact alternating-linkage gate

**Date:** 2026-08-05  
**Method:** Middle-Levels matching exchange, rooted return permutations, and
target stabilizers; no computation or search  
**Status:** unconditional exact reduction and pointwise upper-backup theorem.
The `C8` toggle itself is an exact owner/q1 exchange in `ML_m`, and every
isolated-collar upper casualty has a disjoint stabilizer copy for all
sufficiently large central ranks.  What is not proved is an `O(d)`
alternating graft relative to the fixed PBBS factor, the simultaneous
packing of all backups, or protection of grafted exterior intervals.

## 1. The incidence form of the active `C8`

Let `B` have rank `r-2`, and choose distinct

\[
                         b,a_0,a_1,a_2,a_3\notin B.
\tag{1.1}
\]

For `i in Z_4`, put

\[
 L_i=B\cup\{b,a_i\},\qquad
 I_i=B\cup\{a_i\},\qquad
 R_i=B\cup\{a_{i-1},a_i\}.
\tag{1.2}
\]

The old and new hinge paths in the Middle-Levels incidence graph are

\[
 L_i-I_i-R_i,
 \qquad
 L_i-I_i-R_{i+1},                                      \tag{1.3}
\]

respectively.  Hence the left incidences `L_iI_i` are fixed, while

\[
 N^-:=\{I_iR_i:i\in Z_4\},\qquad
 N^+:=\{I_iR_{i+1}:i\in Z_4\}                         \tag{1.4}
\]

are complementary perfect matchings of an alternating `C8`.

### Proposition 1.1 (exact active resource exchange)

If a spanning Middle-Levels two-factor contains the old collar, replacing
`N^-` by `N^+` preserves degree two at every owner and facet, preserves the
complete owner and lower-q1 vertex sets, and cyclically permutes the four
immediate-upper hinge colours.

#### Proof

Both banks in (1.4) match the same four facets to the same four right
owners.  The fixed left incidences therefore leave degree two in either
phase.  Moreover

\[
\begin{aligned}
 L_i\cap R_i&=L_i\cap R_{i+1}=I_i,\\
 L_i\cup R_i&=B\cup\{b,a_{i-1},a_i\},\\
 L_i\cup R_{i+1}&=B\cup\{b,a_i,a_{i+1}\},
\end{aligned}                                             \tag{1.5}
\]

so the lower colours agree pointwise and the upper colours are shifted by
one.  \(\square\)

This is an alternating cycle in `ML_m`.  It is not the cyclic
adjacent-token receiver square: realizing all old screen edges there would
require the one cut `b` to be adjacent to the four distinct cuts `a_i`.

## 2. Exact relative-matching normal form

Let `G=(cal L,cal O;E)` be any balanced bipartite graph and let

\[
                         F=M_0\mathbin{\dot\cup}M_1          \tag{2.1}
\]

be a spanning simple two-factor, properly edge-coloured into perfect
matchings.  For a perfect matching `M`, form its directed exchange graph
`D_M` as follows.  Contract every edge of `M` to one vertex.  A nonmatching
edge `xy`, with `x in cal L` and `y in cal O`, becomes the arc

\[
                    [x,M(x)]\longrightarrow[M^{-1}(y),y].  \tag{2.2}
\]

Let `P=P_0 dotunion P_1` be a properly two-edge-coloured protected bank;
for the old compound collar, `P` includes all common excursions and the
old hinges.  We ask for a relative graft

\[
 F'=M'_0\mathbin{\dot\cup}M'_1,qquad P_j\subseteq M'_j,   \tag{2.3}
\]

which agrees with `F` away from a prescribed vertex set.

### Lemma 2.1 (one-matching alternating-return criterion)

Fix `j`.  A perfect matching `M'_j` containing `P_j` and equal to `M_j`
off a set of contracted vertices `X_j` exists if and only if the arcs of
`P_j-M_j` extend to a directed cycle cover of `D_(M_j)[X_j]`, while every
vertex incident with an edge of `P_j cap M_j` is omitted from `X_j`.

#### Proof

For two perfect matchings, the symmetric difference is a disjoint union of
even alternating cycles.  Contracting the old matching edges sends each
such cycle to a directed cycle in `D_(M_j)`.  Every prescribed new edge
gives its forced arc (2.2), and every prescribed retained old edge must lie
outside the switched vertices.  This proves necessity.

Conversely, expand a directed cycle cover of `D_(M_j)[X_j]`.  Its arcs are
nonmatching edges and its contracted vertices are the intervening old
matching edges, so expansion gives disjoint alternating cycles.  Toggling
them produces `M'_j`, contains every forced arc, retains the prescribed old
edges, and changes nothing off `X_j`.  \(\square\)

### Theorem 2.2 (exact colour-compatible local-graft equivalence)

There is a relative old-collar graft `F'` whose two-colouring agrees with
the displayed colouring of `F` off the graft and which changes at most `s`
contracted matching-pair units if and only if there are sets `X_0,X_1` and
directed cycle covers as in Lemma 2.1 such that

\[
 |X_0\cup X_1|\le s                                    \tag{2.4}
\]

and the reconstructed perfect matchings are edge-disjoint.

Every such graft is owner-once and lower-q1 exact.  Conversely, every
colour-compatible owner-once/lower-q1-exact graft relative to `F` has this
form.  Counting original incidence vertices instead changes the bound by
at most the constant factor two.

#### Proof

Apply Lemma 2.1 to the two colour classes.  Edge-disjointness is exactly
the condition that their union is a simple two-factor.  A spanning
two-factor of the Middle-Levels incidence graph has degree two at every
owner and every lower facet, so its Johnson projection uses every owner
once and every lower-q1 facet once.  Conversely, properly two-colour the
even cycles of any relative graft and apply the symmetric-difference
decomposition separately in the two colours.  \(\square\)

Thus the exact `O(d)` PBBS neighbourhood-replacement lemma is a
**two-colour short alternating-return theorem**.  Ordinary unrooted factor
extension proves existence of some completion but gives no bound (2.4)
relative to the PBBS matchings.

For one colour, the optimum return support is an ordinary integral flow,
not a new hypergraph problem.

### Proposition 2.3 (one-colour minimum-support assignment)

Give every vertex of `D_M` a left and a right copy.  Add the diagonal edge
`v_Lv_R` of cost zero, representing retention of the old matching edge,
and for every exchange arc `u->v` add `u_Lv_R` of cost one.  Force the
edges corresponding to the prescribed new collar incidences and force the
diagonals corresponding to prescribed retained old incidences.

Then the minimum number of switched matching-pair units in a perfect
matching containing the prescribed colour class is exactly the minimum
cost of a perfect matching in this assignment graph.  Feasibility is
exactly Hall, and the optimum is integral by total unimodularity.

#### Proof

A perfect assignment selects one outgoing and one incoming arc at every
exchange vertex.  Its nonloop arcs are therefore a vertex-disjoint union
of directed cycles, while every diagonal is a fixed point.  The cost is
the number of vertices on the nontrivial cycles.  Lemma 2.1 gives the
claimed correspondence.  The assignment graph is bipartite, so Hall and
the ordinary bipartite matching polytope are exact.  \(\square\)

The two colour classes are coupled only by the requirement that their
reconstructed physical incidence edges be disjoint.  Separate optimal
assignments need not satisfy that common capacity row; no total-
unimodularity claim is made for their coupled product.

For the natural PBBS matching, the proved no-`C8` theorem says that its
exchange digraph has no directed four-cycle.  Consequently the active
screen toggle cannot be installed by keeping the other PBBS matching fixed
and changing exactly the four screen slots.  A successful relative graft
must first change the host matching on a larger return system (or change
both colour classes).  The explicit PBBS parity bridge has linear, not
`O(d)`, support, so it does not by itself prove the required local bound.

There is also a simple use of PBBS cyclic symmetry once one bounded-span
template has been found.

### Lemma 2.4 (cyclic translate packing)

Suppose a free `Z_n` phase action preserves the base factor and a complete
relative graft template is supported on vertices whose phases lie in one
cyclic interval of length `s<n/2`.  Then translates whose phase intervals
are disjoint have disjoint physical supports.  In particular at least

\[
                         \left\lfloor {n\over s}\right\rfloor          \tag{2.5}
\]

pairwise support-disjoint translates exist.

#### Proof

Translate the phase interval itself.  The cyclic phase intervals starting
at `0,s,2s,...` before wrap are disjoint.  A vertex cannot belong to two
templates whose phase sets are disjoint.  \(\square\)

For `s=O(d)=O(sqrt(n))`, one phase-convex template would therefore supply
many disjoint placements.  The lemma does not construct the first template
and does not show that its translates land on any prescribed pair of PBBS
components.

## 3. Rooted topology and the phase-choice collapse

Delete the four old hinges and follow each complete right continuation to
the next selected role.  Let `sigma in S_4` be this return permutation and
put

\[
                         \tau=(0\ 1\ 2\ 3).                  \tag{3.1}
\]

The toggled factor has cut permutation `tau sigma`.

### Proposition 3.1 (exact rooted face)

The old collar lies on two components, with roles `0,2` on one and `1,3`
on the other, and the toggle fuses exactly those two components if

\[
                         \sigma=(0\ 2)(1\ 3).                 \tag{3.2}
\]

On this face

\[
                         \tau\sigma=(0\ 3\ 2\ 1)             \tag{3.3}
\]

is one cycle.

Conversely, for the declared cyclic order of the two old collar paths,
(3.2) is the required rooted return minor.

#### Proof

The first statement is the definition of the next-selected-role map on
the two declared components.  Direct multiplication gives (3.3).  The
general cut-and-rethread law identifies final components with cycles of
`tau sigma`.  \(\square\)

The rooted condition is not implied by the directed cycle covers in
Theorem 2.2.  It is a constant-terminal graphic/linkage condition on their
union.  Therefore the complete owner/q1 PBBS graft is exactly:

\[
\boxed{
 \text{two short alternating return systems}
 +\text{ edge-disjointness}
 +\text{ rooted minor }(3.2).}
\tag{3.4}
\]

No ordinary Hall test on unrooted receiver jobs contains the last row.

There is, however, a strictly weaker condition which removes the rooted
selector altogether.

### Theorem 3.2 (two protected paths suffice with adaptive phase)

Suppose the old factor contains two vertex-disjoint protected open collar
paths, one containing roles `0,2` and the other containing roles `1,3`,
and no other selected role.  Then one of the following holds.

1. The two paths lie on one factor component.  The old phase already has
   one component containing all four roles.
2. The paths lie on two distinct factor components.  After labelling the
   roles in their displayed opposite pairs, the old return is (3.2), and
   the `C8` toggle fuses the two components.

Thus, after the factor completion is known, choosing the old or new phase
always gives one component containing both protected paths.

#### Proof

Each protected path forces its two marked roles to lie on the same factor
component.  Hence either both paths lie on one component or they lie on
two distinct components.  The first case needs no switch.  In the second,
each component contains exactly its displayed pair of selected roles, so
the next-role permutation is `(0 2)(1 3)`.  Proposition 3.1 applies.
\(\square\)

For a proof which insists that the toggle itself merge two predesignated
PBBS components, those components must still be kept distinct before the
toggle.  For an existence proof whose objective is only that their collar
paths end in one component, Theorem 3.2 replaces the exact rooted minor by
the much simpler pair-connectivity of two protected paths.

## 4. What the protected-factor theorem does prove

The old biresident collar is a 2-bounded incidence bank with

\[
                         32(d+1)                              \tag{4.1}
\]

edges.  Hence, whenever `32(d+1)<=m-2`, the small protected-factor theorem
extends it to a spanning Middle-Levels two-factor.  Proposition 1.1 then
toggles that extension without losing owner or q1 resources.

This completion leaves the two collar cycles saturated and isolated.  It
does not attach them to two named PBBS bodies, does not keep the PBBS factor
outside `O(d)` vertices, and does not force (3.2).  Therefore it is the
unrooted resource theorem, not the relative graft theorem requested in
Theorem 2.2.

There is a stronger unrooted topology consequence.  Delete one incidence
edge from each old collar cycle, away from the four active hinges.  The
result is a pair of vertex-disjoint open paths with

\[
                         32(d+1)-2                         \tag{4.2}
\]

protected incidences, containing opposite role pairs.  If

\[
                         32(d+1)-2\le m-2,                 \tag{4.3}
\]

the small protected-factor theorem extends these paths.  Theorem 3.2 then
chooses an old or toggled phase having one component through the complete
protected collar bank.  Therefore **owner/q1 planting plus local collar
component fusion is unconditional** at the unrooted host level.

This still does not preserve two named PBBS bodies outside `O(d)` support;
that relative assertion is exactly the alternating-return gate of Section
2.

## 5. Pointwise stabilizer backups for isolated upper casualties

The isolated cyclic collar has length `O(d)` and at most `128(d+1)^2`
upper casualties; every casualty has rank at least `r+2`.  There is a
useful exact pointwise backup statement.

### Lemma 5.1 (one-target stabilizer avoidance)

Let `Z` have rank `z`, and let `Q_r,Q_(r-1)` be forbidden collections of
rank-`r` owners and rank-`(r-1)` facets.  Let `W_Z` be an incidence path
whose `p_r` owners and `p_(r-1)` facets are all contained in `Z` and whose
owner union is `Z`.  If

\[
 {p_r|Q_r|\over {z\choose r}}
 +{p_{r-1}|Q_{r-1}|\over {z\choose r-1}}<1,                 \tag{5.1}
\]

then some coordinate permutation fixing `Z` setwise sends `W_Z` to a
valid incidence path disjoint from `Q_r union Q_(r-1)` and still witnessing
the upper value `Z`.

#### Proof

Choose a uniform random permutation of `Z` and fix its complement.  Each
rank-`s` vertex contained in `Z` is sent uniformly to one of the
`binom(z,s)` rank-`s` subsets of `Z`.  The union bound makes the probability
of meeting the forbidden bank at most the left side of (5.1), so some
permutation avoids it.  Incidence and path order are preserved by a
coordinate permutation, and the owner union remains `Z`.  \(\square\)

### Corollary 5.2 (every isolated casualty has an alternative path)

Fix the active collar as the forbidden bank.  For `d=Theta(sqrt(r))` and
all sufficiently large `r`, every isolated-collar casualty has an
owner/q1-vertex-disjoint alternative witness obtained from its old witness
by a stabilizer permutation.

#### Proof

An old interval witnessing `Z` uses `O(d)` owners and facets, all contained
in `Z`; the active collar also has `O(d)` vertices of each rank.  Since
`z>=r+2`,

\[
 {z\choose r}\ge {r+2\choose2}=\Omega(r^2),\qquad
 {z\choose r-1}\ge {r+2\choose3}=\Omega(r^3).               \tag{5.2}
\]

The left side of (5.1) is `O(d^2/r^2)=O(1/r)`.  Apply Lemma 5.1.  \(\square\)

This is only pointwise.  Choosing and extending up to `O(d^2)` such paths
simultaneously is another protected path-packing problem; the worst-case
small protected-factor bound does not cover their possible `O(d^3)` total
incidence length.  Stabilizer abundance alone is not a simultaneous
matching theorem.

## 6. Why grafted exterior intervals remain different

For the isolated two-cycle collar, the old interval address space itself
has size `O(d^2)`, which gives the casualty bound used in Section 5.
After grafting into PBBS bodies, an interval may start arbitrarily far in
an exterior continuation, cross a changed hinge, and end arbitrarily far
in another continuation.  The common-history theorem localizes every
possibly lost value above one of four rank-`(r+1)` hinge unions, but the
resulting cone can be exponential and the physical interval can have
unbounded exterior length.

Consequently Corollary 5.2 does not protect grafted exterior intervals:
even its pointwise copy would duplicate an exterior path, and there is no
`O(d^2)` list to pack.  A valid global proof still needs one of:

1. an exterior permutation which transports all crossing intervals;
2. a PBBS backup bank fixed before the graft; or
3. a monotone whole-component/opening theorem showing that no named upper
   target loses its last witness.

## 7. Exact remaining lemma

The owner/q1 grafting problem is now sharply separated from the receiver
parity flow.

> **Protected PBBS `C8` alternating-graft lemma.**  For two named large
> PBBS components, choose the two open screen-lattice collar paths and two
> colourings so that the forced arcs in both exchange digraphs extend to
> edge-compatible directed cycle covers on `O(d)` vertices, with each path
> attached to its named PBBS body.  If the bodies must remain distinct
> until the toggle, also forbid a pre-toggle cross-link between the two
> supports.

This lemma would put the two old collar paths on the named PBBS components.
Theorem 3.2 would then either find them already joined or use Proposition
1.1 to fuse them at zero positional charge, while retaining owner-once and
lower-q1 exactness.  The lemma is not proved here.
Even after it is proved, Section 6 and the typed common cap remain separate
global gates.

## 8. Dependencies

The literal collar is
`MATH_THEOREM_BIRESIDENT_COMPOUND_C8_SCREEN_LATTICE_20260805.md`.

The unrooted extension is
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.

The corrected Johnson-versus-receiver distinction is recorded in
`MATH_REDUCTION_C8_SCREEN_CYCLE_TO_AUGMENTED_RECEIVER_GRAFT_20260805.md`.

The natural-host support-four obstruction is
`MATH_THEOREM_PBBS_NO_C8_AND_LONG_PARITY_BRIDGE_20260726.md`.
