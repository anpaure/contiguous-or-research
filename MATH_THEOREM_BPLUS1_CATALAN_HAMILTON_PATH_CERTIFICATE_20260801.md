# The `B+1` owner gate is a Catalan Hamilton path, with no residual closure

Date: 2026-08-01  
Status: unconditional owner-layer equivalence and exact Catalan
decomposition.  Source-factorization, residence, arbitrary-width upper
coverage, and the common lower compiler remain separate.

## 0. Outcome

Let `ML_m` be the incidence graph between

\[
 {cal L}={[2m-1]\choose m-1},\qquad
 {cal M}={[2m-1]\choose m},
\]

with common shore size

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname{Cat}_m.                            \tag{0.1}
\]

Fix a perfect matching `M_0` of `ML_m`.  For an edge `e=LV` outside
`M_0`, put

\[
 \operatorname{up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).              \tag{0.2}
\]

Then the exact owner-layer certificate for an upper-surjective alternating
Hamilton **path** is one matching `Q subset ML_m-M_0` such that

\[
 |Q|=W-1,\qquad
 \operatorname{up}(Q)={[2m-1]\choose m+1},\qquad
 \lambda(Q)\text{ is graphic-independent}.             \tag{0.3}
\]

Unlike the two-factor/cycle formulation, (0.3) needs no residual perfect
matching and no final closure edge.  Selecting one occurrence of every
upper colour decomposes it exactly as

\[
 \boxed{Q=Q_0\mathbin{\dot\cup}Q_1,quad
        |Q_0|=U,quad |Q_1|=C-1,}                       \tag{0.4}
\]

where `Q_0` is a rooted Catalan forest and `Q_1` is a tree on its `C`
contracted components.  More precisely, endpoint matching forces this tree
to be a directed Hamilton path through the `C` components, using the unique
free outgoing and incoming ports of each `Q_0` path component.

This is the correct weaker owner target for a prospective `B(k)+1`
construction.  It does not by itself show that the path has a depth-`d`
source antecedent with the pivot block.

## 1. Hamilton-path equivalence

### Theorem 1.1

For a matching `Q subset ML_m-M_0`, the following are equivalent.

1. `Q` satisfies (0.3).
2. `M_0 union Q` is a spanning alternating Hamilton path of `ML_m`, and
   the turns at its internal lower-shore vertices cover every rank-`m+1`
   upper colour.

#### Proof

Because `M_0` is perfect and `Q` is a matching of size `W-1`, the union
`M_0 union Q` spans all `2W` vertices, has `2W-1` edges, maximum degree two,
and exactly two degree-one endpoints.  Contract every `M_0` edge.  The
result is precisely the labelled graph `lambda(Q)` on `W` contracted
vertices.

If (0.3) holds, `lambda(Q)` has `W-1` edges and is a forest, hence it is a
spanning tree.  Since the uncontracted graph has maximum degree two, that
tree is a path.  Undoing the contractions gives one alternating Hamilton
path.  At a lower vertex `L` incident with both matchings, its two owner
neighbours are `M_0(L)` and the endpoint `V` of its `Q` edge, so their union
is exactly `up(LV)`.  Surjectivity in (0.3) is therefore the stated turn-
colour condition.

Conversely, in statement 2 the path is already given as `M_0 union Q`.
Contracting its prescribed perfect-matching class `M_0` gives a spanning
path, so `lambda(Q)` is graphic-independent and `|Q|=W-1`.  The turn-colour
hypothesis is exactly surjectivity of `up(Q)`.  Globally, an arbitrary
Hamilton path determines its own size-`W` parity class; that class need not
equal a perfect matching `M_0` fixed in advance.  \(\square\)

The two endpoints lie on opposite shores.  The unique lower-shore endpoint
has no two-owner turn and is the one missing immediate-lower colour in the
owner projection; a full OR construction must route that boundary target
through its short-cell bank.

## 2. Exact Catalan decomposition

### Theorem 2.1

Condition (0.3) is equivalent to the existence of disjoint matchings
`Q_0,Q_1 subset ML_m-M_0` whose union is a matching and such that

1. `up:Q_0 -> binom([2m-1],m+1)` is a bijection;
2. `lambda(Q_0)` is a forest;
3. after contracting the `C` components of `lambda(Q_0)`, the `C-1` links
   of `Q_1` form a directed Hamilton path, each link using the free outgoing
   port of one component and the free incoming port of the next.

#### Proof

Assume (0.3).  For every upper colour select one carrying edge of `Q` and
call the selected set `Q_0`.  It has size `U`; it is a matching, and its
links are a subset of the forest `lambda(Q)`.  Thus `Q_0` is a rooted
Catalan forest.  It spans `W` link vertices with `U=W-C` edges and therefore
has exactly `C` components.  Put `Q_1=Q-Q_0`.  Its size is

\[
                  (W-1)-U=C-1.                         \tag{2.1}
\]

Since the full link graph is a spanning tree, the contracted links of
`Q_1` form a spanning tree on the `C` old components.  Each component of
`lambda(Q_0)` is itself a directed path: the matching property gives
indegree and outdegree at most one.  It therefore has one free incoming and
one free outgoing port.  Compatibility of `Q_0 union Q_1` as a matching
keeps the contracted indegree and outdegree at most one.  A connected
acyclic graph on `C` vertices with these directed port bounds is a directed
Hamilton path.

Conversely, a forest together with a directed free-port path on its
contracted components is a spanning tree.  The union is a matching by
hypothesis, has size
`U+C-1=W-1`, and `Q_0` supplies every upper colour.  Hence (0.3) holds.
\(\square\)

### Protected version

Let a fixed 2-bounded incidence path bank be properly two-edge-coloured
`P=P_0 dotunion P_1`.  The Hamilton path contains `P` whenever one can
choose the certificate above with

\[
                         P_0\subseteq M_0,qquad
                         P_1\subseteq Q_0\cup Q_1.       \tag{2.2}
\]

Thus a protected pivot collar changes the theorem only by forced edges; it
does not restore a residual matching stage.

Proper two-edge colouring alone is not an existence certificate.  The
perfect matching `M_0` must be chosen to contain `P_0`, and the forced
`P_1` edges must be compatible with the upper representatives and with the
free-port component path.  The small protected-factor theorem can supply an
undirected two-factor containing `P`, but it does not supply these correlated
upper/graphic/port conditions.

## 3. Relation to the monotone pivot

The explicit pivot-rich block has a subtle temporal direction.  Before
inserting `X`, its `h` crossing source windows of length `h+1` are

\[
                         U_j=M_j\cup M_{j+1},            \tag{3.1}
\]

of rank `r+1`.  After insertion they are replaced by `h+1` rank-`r`
windows `M_0,...,M_h`.  Therefore the packet cannot be inserted into an
already-flat depth-`h` source while retaining that old flat row.

Specialize now to the target depth `h=d` and write `B=W+h`.  At total source
length `B+1`, the depth-`h` row has

\[
                         (B+1)-h=W+1                   \tag{3.2}
\]

cells.  A direct simple-carrier architecture uses `W` consecutive,
pairwise-distinct rank-`r` cells for the owner Hamilton path and puts the
one surplus cell at a boundary.  If the entire row is value-simple, that
surplus is necessarily a nonowner; without value-simplicity, counting alone
also permits a duplicate owner.  Thus “one controlled boundary nonowner” is
the clean sufficient design state, not an unqualified consequence of
(3.2).

The temporal ledger is exact.  Before insertion the `W` depth cells consist
of the `h` rank-`r+1` cells (3.1), together with `W-h` unchanged cells.  In
the direct boundary-nonowner design those unchanged cells are `W-h-1`
owners plus the same controlled nonowner.  Insertion replaces the `h`
upper-rank cells by `h+1` owners, yielding all `W` owners plus that one
nonowner.  Constructing this nonflat scaffold and proving one common
erosion/cap state is an additional theorem; Theorems 1.1--2.1 solve only
the owner/q1/topology projection.

This corrects the overly strong prescription “start from a flat length-`B`
factor and insert `X`.”  The valid sufficient object is a jointly designed
`B+1` source whose final depth row has the protected Hamilton path plus its
one priced nonowner cell.

## 4. Exact remaining owner theorem

The `B+1` owner-layer problem is now:

> Find a rooted upper-exact Catalan forest `Q_0` and a compatible
> `C-1`-edge connector matching `Q_1`, distribute the protected non-`M_0`
> edges between them, and require the contracted `Q_1` arcs to be a directed
> free-port Hamilton path on the `Q_0` components.

This is strictly weaker than the earlier upper-surjective two-factor with a
one-cycle residual perfect matching.  It remains a correlated matching,
upper-palette, and graphic-tree problem; ordinary Hall for either marginal
does not prove it.

Downstream one still needs the nonflat pre-insertion scaffold, the final
one-nonowner depth row, global residence, arbitrary-width upper witnesses,
and one literal lower common cap.  Accordingly this theorem is a reduction,
not an all-`k` upper bound.
