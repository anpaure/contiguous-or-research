# Antichain-top SCDs over a Middle Levels Hamilton cycle

Date: 2026-08-02  
Status: unconditional odd-dimensional owner/topology theorem, exact
fixed-matching and prescribed-pull refinements, and an exact statement of
the remaining literal age gate.  No literal OFHT cycle, residence theorem,
compiler theorem, or contiguous-OR bound is asserted.

## 0. Outcome

For `r>=2` put

\[
             k=2r-1,\qquad
 \mathcal L={ [k]\choose r-1},\qquad
 \mathcal O={ [k]\choose r},\qquad
 W=|\mathcal L|=|\mathcal O|.
\]

There is no conflict between the following two requirements:

1. the owner matching from rank `r-1` to rank `r` is the middle edge
   matching of a full symmetric-chain decomposition of `B_k`; and
2. a second incidence matching joins it to one alternating Hamilton cycle
   of the Middle Levels graph.

Indeed, take either parity matching of any Middle Levels Hamilton cycle.
Every prescribed perfect matching between the two middle ranks of an odd
Boolean lattice extends to a full SCD.  This observation can then be
combined with the antichain-top theorem: after the SCD has been chosen,
the prescribed target-chain maxima occupy distinct SCD chains, so their
roles receive distinct owners on the Hamilton matching.  Empty roles fill
the remaining chains.

Thus the antichain-top theorem closes the static target/owner resources and
Middle Levels Hamiltonicity closes the **projected central topology**, with
the same owner matching.  This is an unconditional all-`r` statement for
free owner assignment.

The quantifier is important.  The theorem chooses the Hamilton cycle, its
matching parity, the SCD, and the owners.  It does not say that a previously
fixed SCD matching, previously fixed owner map, or previously fixed literal
flag table extends to a Hamilton cycle.  For a fixed central matching `M`,
the exact extra condition is Hamiltonicity of a directed contraction graph
`D_M`; ordinary matching gives only a cycle cover.

Nor does the theorem make the constructed static states consecutive in the
literal age automaton.  In the all-high sector, the remaining condition is
exactly a resident Johnson Hamilton cycle whose prescribed chains occur in
the consecutive-intersection decks.  The adjacent-union owner deck is then
automatically rainbow.  In general types, the unreduced condition remains
the cellwise shift equation

\[
                 X^{i+1}_{j+1}=X^i_j\setminus X^{i+1}_0.
\]

## 1. Every central perfect matching extends to an SCD

We record the band-extension fact in the form needed here.

### Theorem 1.1 (central-matching extension)

Let `n=2h+1`.  Every perfect matching in the inclusion graph

\[
             { [n]\choose h}\longleftrightarrow
             { [n]\choose h+1}
\]

is the central matching of a saturated symmetric-chain decomposition of
`B_n`.

#### Proof

Regard the prescribed matching edges as symmetric chains in the central
two-rank band.  Suppose inductively that the ranks

\[
                    h-t,\ldots,h+1+t
\]

have been decomposed into saturated symmetric chains, retaining every
previous internal adjacency.  Let `Y` be the chains whose lower and upper
endpoints lie on the two boundary ranks `h-t` and `h+1+t`.  Write those
endpoints as `A_y,B_y`.

To add the next two ranks put

\[
 X={ [n]\choose h-t-1},\qquad
 Z={ [n]\choose h+t+2}.
\]

Make a bipartite graph with shores

\[
                         X\mathbin{\dot\cup}Y^-,\qquad
                         Z\mathbin{\dot\cup}Y^+.
\]

Join `x` to `y+` when `x subset A_y`, join `y-` to `z` when
`B_y subset z`, and include the identity edge `y-y+`.  Give each
comparison edge weight

\[
                         {1\over h+t+2}
\]

and each identity edge weight

\[
             1-{h-t\over h+t+2}={2t+2\over h+t+2}.
\]

Every `x` and every `z` has `h+t+2` comparison neighbours.  Every boundary
chain has `h-t` possible extensions on either side.  Hence all row and
column sums are one.  The support is therefore a square bipartite graph
with a fractional perfect matching, and so it has an integral perfect
matching.

If the identity edge of `y` is selected, its old chain stops.  Otherwise
the perfect matching pairs it with one unused `x` and one unused `z`, and
the chain is extended at both ends.  Every new outer vertex is used once,
and symmetry and all old internal adjacencies are preserved.  Iteration to
ranks zero and `n` proves the theorem.  \(\square\)

This theorem says that being an SCD middle matching imposes no restriction
on a perfect matching of the two middle ranks.  Higher-depth age and flag
conditions are not part of the extension.

This is not the same implication as the Gregor--Mička--Mütze theorem that
the particular Greene--Kleitman SCD extends to a Hamilton cycle of the
**full cube**.  A full-cube chain ordering does not by itself give a second
middle-incidence matching.  Here the order of construction is reversed:
first choose a Hamilton cycle of the Middle Levels graph, then extend one
of its parity matchings vertically to an SCD by Theorem 1.1.  Consequently
no identification between the full-cube SCD chain order and the canonical
Middle Levels pull factor is needed for Theorem 3.1.

## 2. The exact fixed-matching topology gate

Fix a perfect incidence matching

\[
                       M:\mathcal L\longrightarrow\mathcal O.
\]

Define a directed graph `D_M` on `mathcal L` by

\[
 q\longrightarrow q'
 \quad\Longleftrightarrow\quad
 q'\subset M(q),\qquad q'\ne q.                       \tag{2.1}
\]

It is `(r-1)`-regular in both directions.  It is also strongly connected.
Indeed, a sink strongly connected component `S` has no outgoing arc.  The
equality of total indegree and outdegree on `S` then gives no incoming arc
either.  Consequently the lower vertices `S` together with their matched
upper vertices `M(S)` form a union of components of the Middle Levels
graph.  That graph is connected, so `S=\mathcal L`.

### Theorem 2.1 (fixed-`M` permutation criterion)

The following objects are in bijection.

1. Perfect matchings `N` of the Middle Levels graph which are disjoint
   from `M`.
2. Permutations `sigma` of `mathcal L` such that
   `q -> sigma(q)` is an arc of `D_M` for every `q`.

Under the bijection,

\[
                  N=\{M(q)\,\sigma(q):q\in\mathcal L\},          \tag{2.2}
\]

and the alternating components of `M union N` are exactly the cycles of
`sigma`.  Consequently

\[
 \boxed{\ M\cup N\text{ is Hamiltonian}
       \quad\Longleftrightarrow\quad
       \sigma\text{ is one }W\text{-cycle in }D_M.\ }          \tag{2.3}
\]

#### Proof

At the upper vertex `M(q)`, a disjoint perfect matching `N` chooses a
unique lower neighbour `q' != q`; set `sigma(q)=q'`.  Saturation of the
lower shore by `N` makes `sigma` a permutation.  Conversely (2.1) and a
permutation `sigma` make (2.2) a disjoint perfect matching.  Alternating
two-step traversal sends

\[
                         q-M(q)-\sigma(q),
\]

so its components are precisely the permutation cycles.  \(\square\)

Regularity gives a perfect matching, hence a cycle cover, and strong
connectivity removes the elementary component obstruction.  Neither fact
settles the one-cycle row.  A forced proper directed cycle is an immediate
sharp obstruction to extending a set of prescribed arcs to one Hamilton
cycle.  More generally the exact fixed-`M` formulation is a directed
Hamilton-cycle problem with the usual nontrivial subtour cuts.

### Corollary 2.2 (fixed-SCD criterion)

For a fixed SCD `D`, let `M_D` be its central matching.  A second incidence
matching has Hamilton union with `M_D` if and only if `D_(M_D)` has a
directed Hamilton cycle.  Thus the fact that `M_D` comes from an SCD does
not by itself prove the positive answer for a preselected decomposition;
the remaining question is exactly the contraction topology in (2.3).

## 3. Antichain-top Hamilton owner lift

For every role `u` prescribe a possibly empty nested chain

\[
                       \mathcal C_u=\{P_{u,j}:j\in J(u)\}
                                                                    \tag{3.1}
\]

with the rank/type consistency from Theorem 6.1 of
`MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md`.
Assume that all named targets are pairwise distinct and that the maxima of
the nonempty chains form an antichain.  There are `W` roles, including the
empty ones.

### Theorem 3.1 (free-owner SCD--Hamilton extension)

Fix **any** Middle Levels Hamilton cycle and either one of its two parity
matchings.  Then there exist

1. a Middle Levels Hamilton cycle
   \[
       q_0,T_0,q_1,T_1,\ldots,q_{W-1},T_{W-1},q_0;       \tag{3.2}
   \]
2. a full SCD `D` whose central matching is
   \[
                         M=\{q_iT_i:i\in\mathbb Z_W\};   \tag{3.3}
   \]
3. a bijection from the roles to the SCD chains; and
4. one literal static state of the prescribed type for every role,

such that every chain (3.1) is realized exactly and the state assigned to
the `i`th SCD chain has owner `T_i`.  The second incidence matching

\[
                         N=\{T_iq_{i+1}:i\in\mathbb Z_W\}           \tag{3.4}
\]

is perfect and `M union N` is the Hamilton cycle (3.2).

#### Proof

Index the fixed cycle as in (3.2), with its chosen parity denoted by `M` as
in (3.3).  Theorem 1.1 extends `M` to a full SCD `D`.  The published Middle
Levels theorem guarantees that at least one such starting cycle exists for
every `r>=2`.

Every nonempty maximum in (3.1) lies on a unique SCD chain.  Two such
maxima cannot lie on the same chain, since an SCD chain is totally ordered
and the maxima form an antichain.  Assign each nonempty role to the chain
containing its maximum, and assign the empty roles arbitrarily to the
remaining SCD chains.  This is a bijection because an SCD of `B_(2r-1)`
has exactly `W` chains.

Let `T_i` be the rank-`r` member of the assigned chain.  Insert the empty
set before (3.1) and `T_i` after it.  Between consecutive prescribed
prefixes, partition the set difference into ordered cells of the required
sizes.  The rank consistency guarantees the sizes, and the resulting
cells are disjoint and have union `T_i`.  Thus they form a literal static
state realizing (3.1), exactly as in the proof of the antichain-top
one-copy theorem.

Finally, (3.3)--(3.4) are the two parity matchings of (3.2), so their union
is one Hamilton cycle.  \(\square\)

The theorem remains true if every target chain is already saturated, but
saturation is unnecessary.  If a maximum has rank `r-1`, its assigned
owner is literally its `M`-mate.  For a lower maximum, the intervening
rank-`(r-1)` member is the central root of its assigned SCD chain.

### Quantifier boundary

Theorem 3.1 proves

\[
 \forall(\mathcal C_u)_u\quad\forall C\in\operatorname{Ham}(ML(k))
 \quad\forall M\in\operatorname{Parity}(C)\quad
 \exists(\mathcal D,(X^u)_u),                               \tag{3.5}
\]

with the other parity `N` already determined by `C`.

It does not prove the same assertion after `M`, `D`, the owner `T_u`, or a
complete flag `X^u` has been fixed in advance.  A fixed `M` invokes
Theorem 2.1.  Fixed target-to-owner pairs additionally require the desired
maxima to be contained in their prescribed owners, with the owner map
injective; membership of the maximum in the corresponding SCD chain is a
device used to construct the free owner map, not a necessary condition once
that map is supplied.  Neither fixed-`M` Hamiltonicity nor this containing
owner assignment follows from the antichain hypothesis alone.

For even `k=2r`, the literal two-perfect-matching statement is impossible:

\[
                   {2r\choose r-1}<{2r\choose r}.
\]

Thus the equal-shore Hamilton-cycle theorem above is intrinsically
odd-dimensional.  An even-dimensional statement needs a saturating-cycle
or Hamilton-path formulation and is separate.

## 4. Exact prescribed-pull refinement

The canonical Gregor--Mütze--Nummenpalo pull construction has a connected
labelled auxiliary multigraph `H_(r-1)` for the Middle Levels graph on
ranks `r-1,r`.  Its labelled pull hexagons are
edge-disjoint and noninterleaving in the sense used by the canonical
construction.

### Corollary 4.1 (graphic prescribed pulls plus antichain tops)

Let `A` be a labelled set of canonical pull occurrences.  If `A` is a
graphic forest in `H_r`--in particular it contains no loop, ordinary
cycle, or two parallel labels forming a two-cycle--then Theorem 3.1 may be
realized with a canonical Hamilton cycle whose pull spanning tree contains
`A`.  Every pull in `A` has its prescribed switched phase, and later pulls
do not change an edge of its hexagon.  The prescribed target chains are
then lifted on one parity matching of that final Hamilton cycle.

Within the canonical labelled spanning-tree construction, the forest
condition is also necessary for containing all labels of `A`.

#### Proof

Contract the components of `A` in the connected auxiliary graph and extend
the contraction to a labelled spanning tree.  Canonical edge-disjointness
and noninterleaving make the corresponding simultaneous switch a Hamilton
join and protect the already selected pull edges.  Now take either parity
matching of the final Hamilton cycle and apply Theorems 1.1 and 3.1.  The
necessity is the ordinary fact that every subset of a spanning tree is a
forest.  \(\square\)

This corollary is deliberately edge-level.  Pulls may share vertices and
may change external pairing, marks, and chronology.  If target states or
packet interfaces are attached to specified occurrences **before** the
pulls, the complete-interface/hereditary-admissibility hypotheses of the
prescribed-packet theorem are still required.  A forest in the pull graph
does not preserve those non-edge resources.  The present theorem avoids
that issue by choosing the SCD and the free owners after the final Hamilton
cycle is fixed.

## 5. What literal age compatibility still requires

The states constructed in Theorem 3.1 are static.  The fact that
`q_i subset T_i supset q_(i+1)` is a legal Middle Levels wedge does not
imply that the state at role `i` can be followed by the state at role
`i+1`.

### 5.1 General age types

For cyclically ordered states

\[
                         X^i=(X^i_0,\ldots,X^i_d),
\]

the unreduced literal condition is

\[
 \boxed{
 X^{i+1}_{j+1}=X^i_j\setminus X^{i+1}_0
 \quad(0\le j<d,\ i\in\mathbb Z_W).}                  \tag{5.1}
\]

If the role template has a prescribed successor relation `E_U`, the same
cyclic role assignment must also satisfy

\[
                              (u_i,u_{i+1})\in E_U.              \tag{5.1a}
\]

The gap partitions in the antichain-top proof are independent from role to
role and need not satisfy (5.1).  Thus Theorem 3.1 supplies a connected
owner/incidence projection, not selected arcs in the literal compatibility
digraph of OFHT.

For a fixed flag table, the equivalent chronology rows remain:

1. balance of every de Bruijn rail prefix/suffix state;
2. Hall's condition in every statewise legal-turn graph;
3. one joint choice of the statewise matchings using every owner once; and
4. one-cycle, rather than cycle-cover, topology.

Theorem 3.1 settles the owner count and an abstract version of the last
row, but not the first two rows or their common integral choice.

### 5.2 Exact all-high serialization

In the all-high depth-`d` sector write (3.2) as

\[
 q_{i+1}=q_i-\{a_i\}+\{b_i\},\qquad
 T_i=q_i\cup q_{i+1}=q_i+\{b_i\}.                    \tag{5.2}
\]

A literal connected flag chronology on this carrier has necessarily

\[
                 f_i=(q_i;a_i,a_{i+1},\ldots,a_{i+d-2}).          \tag{5.3}
\]

Equivalently, the departure word must be resident: every positive
coordinate run in the cyclic incidence word of the `q_i` has length at
least `d`, so the displayed future departures are distinct members of
`q_i`.  For every `1<=j<d`, its marked target is

\[
 \begin{aligned}
 q_i-\{a_i,\ldots,a_{i+j-1}\}
   &=q_i\cap q_{i+1}\cap\cdots\cap q_{i+j}.             \tag{5.4}
 \end{aligned}
\]

Conversely, (5.2)--(5.4) with the residence condition give the literal
shift at every turn.  Hence preserving the prescribed chains in the
literal sense requires a role-to-index assignment for which every named
target is the required member of an intersection deck (5.4), not merely a
subset of the owner `T_i`.

The upper owner condition is already exact:

\[
                         \{q_i\cup q_{i+1}:i\in\mathbb Z_W\}
                          =\mathcal O,                          \tag{5.5}
\]

because (3.2) visits every upper vertex once.  Thus, on a carrier already
known to be the projection of a Middle Levels Hamilton cycle, the exact
residual all-high statement is

\[
 \boxed{
 \text{resident Johnson Hamilton cycle}
 +\text{ prescribed/complete lower intersection decks}.}       \tag{5.6}
\]

If one searches over ordinary Johnson Hamilton cycles without fixing a
Middle Levels lift, then `rainbow adjacent unions` must be retained as a
third condition in (5.6); it is precisely what makes that lift possible.
On the carrier (3.2) it is automatic.  If the first deletion of a
fixed flag is prescribed, it forces the outgoing arc

\[
                         q_i\longrightarrow T_i-\{a_i\}
                                                                    \tag{5.7}
\]

in the contraction graph `D_M`; a proper forced subtour is already fatal.
Deeper prescribed chains constrain consecutive arcs through (5.4).

The recursive SCD flag table at `(k,m,d)=(7,3,3)` recorded in
`MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md`
is an explicit warning: it is target-exact but has nonzero rail divergence
and fifteen roots with no legal successor.  Static SCD exactness therefore
does not imply even a literal cycle cover.

## 6. Exact scope for OFHT and contiguous OR

Theorem 3.1 closes, simultaneously and exactly:

* one copy of every role;
* one copy of every rank-`r` owner;
* every prescribed antichain-top target chain;
* an SCD whose central matching is the owner matching; and
* one connected alternating Middle Levels incidence skeleton.

It does not close:

* the literal compatibility arcs (5.1), or the rail/Hall rounding that
  selects them;
* a prescribed role order or role-successor relation;
* prescribed target-to-owner assignments;
* residence except when imposed through (5.3)--(5.4);
* arbitrary-width upper shadows, protected interfaces, quotient voltage,
  opening, or the common-cap/compiler rows; or
* any all-`k` additive-constant or `O(1)` contiguous-OR conclusion.

Accordingly the topology row is no longer an independent obstacle on the
free-owner antichain face.  The remaining obstruction is alignment: the
same Hamilton order must realize the prescribed chains as literal age
histories.

## 7. Inputs used

* `MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md`, Theorem 6.1;
* `FIXED_PAIR_RESIDUAL_SCD.md`, Theorem 2;
* `MATH_THEOREM_R_CANONICAL_MUTZE_PULL_COATOM_AND_RESIDENT_COLLAR_EMBEDDING_20260801.md`, Theorem 1.1 and its protected-interface qualification; and
* `MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md`, Theorems 2.1 and 7.1.
