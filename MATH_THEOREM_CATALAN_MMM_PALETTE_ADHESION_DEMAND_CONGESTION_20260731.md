# MMM decoration adhesion is exactly owner-hull congestion

Date: 2026-07-31  
Status: exact all-dimension boundary identity and DP compression theorem;
exact finite audit for one canonical MMM gluing tree through paper parameter
`n=9`; no all-dimension decorated-factor existence or bounded-width theorem

## 0. Verdict

The correlated feasible-decoration relation has a much smaller exact palette
interface than the raw augmented graph suggests.  Give each candidate turn
occurrence to one component block of a tree `T`.  A named turn colour is live
at an edge of `T` exactly when that edge separates two of its occurrence
owners.  Equivalently, the colour is live on its entire owner hull.

When every colour has at most two owners, palette adhesion is therefore
**tree-path congestion** of a labelled demand multigraph.  This is an exact
normal form, not a heuristic:

\[
 |A_s(e)|=
 \#\{d\in E(D_s):e\text{ lies on the }T\text{-path of }d\}.
\tag{0.1}
\]

For the lexicographically first potential-decreasing heavy-root MMM gluing
tree, a literal physical audit through `n=9` finds a striking asymmetric
law.

* Every candidate colour has at most two original plane-tree owners.
* The lower demand multigraph is exactly the selected gluing tree, one named
  lower colour per tree edge.  Thus every lower palette interface has width
  exactly one.
* The upper demand multigraph contains the tree but also has parallel demands
  and, from `n=7`, genuine chord demands.  Its maximum audited congestion is
  `7` at `n=9`.
* Every audited tree cut has exactly two physical chronology edges.

Thus the lower palette coordinate really is one-dimensional.  The upper
coordinate is not: at `n=9` one tree edge carries seven upper colours and one
lower colour.  In particular, any proposed interface of total palette width
at most seven is already false for this canonical tree.

The recent reduction from a decorated Hamilton cycle to a decorated
componentwise Middle Levels 2-factor removes terminal connectivity and
voltage from the existential target.  It does **not** delete shared colour
vertices.  On a fixed terminal 2-factor, chronology closes independently on
each component, while candidate colours occurring in several components
remain globally coupled.  The strongest clean successor target is therefore
a palette-private decorated 2-factor; the weaker exact target is a factor
decomposition whose owner-hull congestion is controlled.

The old `ML(7)` triple-intersection example also survives logically: its
three Hamilton cycles are special 2-factors, so it still refutes a frozen
one-bit notion of edge transparency.  But it is no longer an existential
obstruction.  The terminal factor in that example is itself decorable; a
post-glue relation may choose a fresh decoration there.

## 1. Palette owners and hulls

Let `T` be a tree whose vertices are component blocks.  Fix a Middle Levels
factor, partial factor, or candidate graph, and assign every candidate turn
occurrence `p` to its unique block

\[
                         \kappa(p)\in V(T).
\]

Assign the augmented turn edge `pc` to the same block as `p`.  Treat lower
and upper turn colours as distinct typed vertices even when their underlying
set labels happen to coincide.

For shore `s` and colour `c`, define the owner support

\[
 O_s(c)=\{\kappa(p):pc\text{ is a candidate turn edge}\}.
\tag{1.1}
\]

For `e in E(T)`, let `S_e` and `\bar S_e` be the two components of `T-e`.
The shore-`s` palette boundary is

\[
 A_s(e)=\{c:O_s(c)\cap S_e\ne\varnothing
                 \ne O_s(c)\cap\bar S_e\}.
\tag{1.2}
\]

Here the chained inequality means that both intersections are nonempty.

### Theorem 1.1 (owner-hull identity)

For every tree edge `e`,

\[
 \boxed{
 |A_s(e)|
   =\sum_c {\bf 1}\!\left[e\in\operatorname{Hull}_T(O_s(c))\right],
 }
\tag{1.3}
\]

where `Hull_T(O)` is the minimal subtree of `T` spanning `O`.

#### Proof

A colour vertex is incident with candidate turn edges owned on both sides of
the cut exactly when its owner support meets both sides.  In a tree, deleting
`e` separates two vertices of `O` exactly when `e` belongs to the minimal
subtree spanning `O`.  This is (1.3). `square`

This statement needs no bound on `|O_s(c)|`.  Large supports simply give
demand subtrees instead of demand edges.

## 2. Two-owner colours give a demand multigraph

Assume now that every owner support has size at most two.  Form a labelled
loopless multigraph `D_s` on `V(T)` as follows.  For every colour satisfying

\[
                        O_s(c)=\{u,v\},
\]

add one edge `uv` labelled by `c`.  Retain parallel edges: two distinct
colours are two distinct matching constraints.  Omit singleton-owner
colours.

### Corollary 2.1 (demand-congestion form)

For every `e in E(T)`,

\[
 \boxed{
 |A_s(e)|
  =\#\{d\in E(D_s):e\in P_T(d)\},
 }
\tag{2.1}
\]

where `P_T(d)` is the unique tree path joining the endpoints of the demand
edge `d`.

In particular, if `D_-=T` with one labelled lower demand per tree edge,
then every lower palette boundary has size one.  If

\[
                        D_+=T\uplus D_{\rm extra},
\]

then

\[
 |A_+(e)|=1+\operatorname{load}_T(D_{\rm extra},e).
\tag{2.2}
\]

This also gives the canonical colour-elimination order: a colour is live
precisely on its owner hull and may be forgotten immediately after that hull
has been completely processed.

## 3. Exact feasible-decoration DP interface

Orient a tree edge toward a processed side `S`, and let `M_S` be a partial
matching in the augmented occurrence graph.  For every crossing colour keep
the named bit

\[
                    x_e(c)=\deg_{M_S}(c)\in\{0,1\}.
\tag{3.1}
\]

These bits are the complete colour-vertex boundary datum.

1. A colour owned wholly in `S` must already have matching degree one.
2. A colour owned wholly outside `S` is absent from the state.
3. At a join, bits for the same named colour add; a sum exceeding one is
   rejected.
4. When the last owner is absorbed, the total must equal one before the
   colour is forgotten.

Necessity is immediate from matching degree one.  Sufficiency follows
because candidate turn edges partition by their occurrence owner.  Thus the
palette part contributes at most

\[
                       2^{|A_-(e)|+|A_+(e)|}
\tag{3.2}
\]

syntactic states.

The colours must remain **named**.  A count of used crossing colours is
unsound because different colours have different exterior candidates.  The
two shores must also remain in one correlated relation rather than two
independent projections.

This is only the palette coordinate.  A complete state additionally keeps:

* for every exposed occurrence, whether it is open, turn-matched, or
  residual-matched;
* the oriented order and exact finite run summary of every exposed trace
  fragment; and
* while a physical Hamilton object is still being constructed, port degrees,
  a connectivity partition, and voltage when relevant.

Repeated candidates inside one owner block do not increase palette adhesion,
but they can change local matching feasibility.  Therefore (2.1) is a width
theorem, not a root-nonemptiness theorem.

## 4. Rebase to the decorated 2-factor target

The terminal Hamilton requirement is now known to be stronger than Catalan
Linear Matching needs.  Let a terminal spanning 2-factor have components

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0.
\]

Selected upper and lower turn occurrences must be globally colour-bijective,
and their shore types must alternate separately on every marked component.
An unmarked component chooses either residual matching phase.  Each marked
component has its own binary trace, which must avoid the cycle face.

This changes the boundary relation in three precise ways.

1. **Terminal connectivity disappears.**  Different factor components need
   not be merged, and no global Hamilton partition or voltage is retained.
2. **Trace closure is componentwise.**  As soon as a factor component is
   finished, its cyclic trace is tested and forgotten independently.  An
   unmarked component is accepted automatically on the trace row.
3. **Palette coupling remains global.**  If one turn colour has candidates in
   two unfinished components, its named matching bit remains live.  The
   owner-hull formula is unchanged.

Hence, for a fixed terminal 2-factor whose components are used as the bags,
the only intercomponent matching interaction is the typed palette-demand
hypergraph.  This motivates the following strong sufficient target.

> **Palette-private decorated-factor target.**  Construct a spanning Middle
> Levels 2-factor such that every typed turn colour has all of its candidate
> occurrences in one factor component, and each component admits compatible
> local alternating selections whose union is globally colour-bijective and
> whose marked traces are linear.

Palette privacy makes (1.2) empty after the factor components are formed, so
the decoration problem factorizes completely.  It is stronger than needed
and is not proved in all dimensions.

The weaker recursive target is an MMM-like component forest for which the
owner supports have controlled hull congestion and the correlated root
relation is nonempty.  Connectivity of that forest is not required.

### Proposition 4.1 (what happens to the `ML(7)` scalar counterexample)

Allowing terminal 2-factors does not make scalar frozen-decoration
transparency compose.  The previously frozen sequence

\[
 C_0\mathbin\triangle Z_1=C_1,
 \qquad C_1\mathbin\triangle Z_2=C_2
\]

uses Hamilton cycles, hence valid 2-factors, and satisfies

\[
 |{\cal D}(C_0)\cap{\cal D}(C_1)|=576,
 \quad
 |{\cal D}(C_1)\cap{\cal D}(C_2)|=1620,
 \quad
 {\cal D}(C_0)\cap{\cal D}(C_1)\cap{\cal D}(C_2)=\varnothing.
\]

So one Boolean “some decoration survives this edge” remains unsound.
However, every terminal decoration of `C_2` is on the linear side.  Thus the
example is not an obstruction to terminal 2-factor existence or to a
relation which redecorates after the toggles.  It only forbids freezing a
single decoration through the whole path.

## 5. Canonical MMM finite audit

Use paper parameter `n`, so the Middle Levels graph has ground size
`2n+1` and shores `n,n+1`.  Start with the canonical MMM base factor.  Map
every physical occurrence to its original plane-tree component.  At each
non-star component choose the lexicographically first potential-decreasing
heavy-root gluing label, and toggle all selected physical hexagons.  The
result is one Hamilton factor in every audited case.

The exact cut data are:

| `n` | base blocks | base missing colours / shore | max upper adhesion | max lower adhesion | max total palette adhesion |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 | 0 | 0 |
| 3 | 2 | 0 | 1 | 1 | 2 |
| 4 | 3 | 3 | 1 | 1 | 2 |
| 5 | 6 | 22 | 2 | 1 | 3 |
| 6 | 14 | 117 | 2 | 1 | 3 |
| 7 | 34 | 550 | 3 | 1 | 4 |
| 8 | 95 | 2431 | 3 | 1 | 4 |
| 9 | 280 | 10374 | 7 | 1 | 8 |

The distribution across all selected tree edges is:

| `n` | `(upper,lower,chronology): number of cuts` |
|---:|:---|
| 3 | `(1,1,2):1` |
| 4 | `(1,1,2):2` |
| 5 | `(1,1,2):4`, `(2,1,2):1` |
| 6 | `(1,1,2):11`, `(2,1,2):2` |
| 7 | `(1,1,2):23`, `(2,1,2):8`, `(3,1,2):2` |
| 8 | `(1,1,2):72`, `(2,1,2):19`, `(3,1,2):3` |
| 9 | `(1,1,2):187`, `(2,1,2):56`, `(3,1,2):21`, `(4,1,2):8`, `(5,1,2):5`, `(6,1,2):1`, `(7,1,2):1` |

The number of upper demand colours beyond one copy per tree edge is

\[
                  0,0,0,1,2,6,15,45
\tag{5.1}
\]

for `n=2,...,9`.  Most early extras are parallel demands on a selected tree
edge.  Genuine non-tree owner pairs first occur at `n=7`; their colour counts
for `n=7,8,9` are `1,2,12`.

The canonical base factor itself is palette-private relative to its
plane-tree components throughout the audit: every attained typed turn colour
has owner support one.  But from `n=4` it lacks required colours, by the third
column of the table, so privacy alone does not supply a decoration.  The
canonical full gluing output attains the same number of distinct colours in
this audit.  This is the already-known `81/84` standard-family obstruction at
`n=4`, now placed in the owner-demand picture.

### The exact `n=9` obstruction cut

The maximum-congestion tree edge joins

```text
101010101010111000  ->  101010101010110100
```

and separates `124` original blocks from `156`.  Its seven upper colours are

\[
 67579,68603,77051,83707,84859,87419,305847,
\]

its one lower colour is `43700`, and exactly two physical chronology edges
cross the cut.

Consequently a DP which omits any of these eight named palette coordinates
identifies partial matchings with different exterior completion behaviour.
This proves a lower bound of eight on the total palette width of this exact
tree decomposition.  It does not prove unbounded width, and it does not rule
out a better gluing tree.

## 6. The weakest honest induction theorem left

The finite data support the following hierarchy.

1. **Best target:** directly construct a palette-private decorated 2-factor.
   Then componentwise trace tests and local matchings finish the central
   theorem with no global topology.
2. **Next-best target:** construct a decorated component forest whose typed
   owner hyperedges have a laminar elimination order of controlled hull
   congestion.  The exact DP state is then the named palette bit-vector,
   occurrence statuses, and componentwise run summaries.
3. **Canonical-tree target:** prove all-dimension analogues of owner
   multiplicity at most two and `D_-=T`, then bound the upper demand-path
   congestion.  The finite audit proves neither claim beyond `n=9` and shows
   that a proposed tiny bound cannot be right.

Even a constant congestion theorem would only bound the interface.  One must
still prove that the correlated feasible-decoration relation at the root is
nonempty.  Conversely, a nonconstructive direct decorated-2-factor theorem
would make any width bound unnecessary.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_mmm_palette_adhesion_20260731.py
```

The script reconstructs the base factor, plane-tree ownership, canonical
gluing labels, physical Hamilton factor, all typed turn candidates, every
tree cut, and both demand multigraphs for `n=2,...,9`.  It freezes the exact
histograms and the `n=9` cut above in

```text
scratch/catalan_mmm_palette_adhesion_20260731.audit.json
```

The audit is finite and choice-specific.  It makes no claim that this tree is
congestion-minimizing or that the displayed pattern continues for all `n`.
