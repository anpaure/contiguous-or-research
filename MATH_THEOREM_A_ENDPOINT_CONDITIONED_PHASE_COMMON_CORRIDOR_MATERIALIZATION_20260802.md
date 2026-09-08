# Endpoint-conditioned phase-common corridor materialization

**Date:** 2026-08-02  
**Lane:** A, ambient corridor for the opened fixed-`z` seven-ear packet  
**Status:** exact conditional construction and exact resource-row audit.  The
theorem materializes a spanning co-oriented host from one endpoint-conditioned
ordered Hall certificate.  It does not prove that the required certificate
exists in every Boolean host.

## 0. Purpose and scope

Open the same connector `Q_j` in the two fixed-`z` terminal cycles of
`MATH_THEOREM_A_FIXED_Z_FAR_SOCKET_APERTURE_CYCLE_AND_CORRIDOR_FIBRE_GATE_20260802.md`.
This leaves two internally different protected paths

\[
                    P^0:s\longrightarrow r,
                    \qquad P^1:s\longrightarrow r,                 \tag{0.1}
\]

with the same literal entrance and exit sockets.  Their internal packet rows
differ, but their endpoint owners, endpoint canonical frames, exported
two-polarity history relations, and exposed resource banks agree.  The local
theorem already proves

\[
                  \sigma(P^1)-\sigma(P^0)=0.                       \tag{0.2}
\]

The result below gives the strongest literal implication presently justified:
one *capacity-faithful endpoint-conditioned corridor certificate* embeds
either `P^epsilon` in one co-oriented spanning cycle, using exactly the same
ambient corridor in the two phases.  Consequently the corridor contributes
zero **relative** sidecar displacement.  Absolute quotient voltage, existence
of the certificate, deeper upper shadows, source binding, and the terminal
compiler remain separate.

## 1. Literal fragment table and joins

Fix a finite table `F` of pairwise resource-disjoint, internally accepting,
co-oriented directed fragments which partitions the ambient physical owner
bank.  One distinguished fragment `p` is the contracted protected path
`P^epsilon`; every other fragment is literally identical in the two phases.
The entrance of `p` is `s` and its exit is `r`: an incoming join to `p`
lands at `s`, while an outgoing join from `p` leaves at `r`.
For every fragment fix one entrance state and one exit state.  A state contains

1. the physical endpoint owner and canonical frame;
2. the exact positive and negative boundary-history state;
3. every occurrence-labelled owner, facet, cap, private, and history resource
   already consumed by the fragment; and
4. its additive sidecar label.

An admissible directed join `e:u->v` is a literal Johnson seam between the exit
of `u` and the entrance of `v`.  It is retained only if:

* the two owners are Johnson-adjacent;
* both boundary-history automata accept the concatenation;
* its lower facet `I(e)` and immediate upper cap `U(e)` have the prescribed
  unused types;
* it avoids the protected collision bank; and
* its complete occurrence-labelled resource set `R(e)` and sidecar increment
  `sigma(e)` are recorded.

Thus a join is not an unlabelled endpoint pair.  In the Boolean middle-levels
specialization, for endpoint owners `A,B`,

\[
                        I(e)=A\cap B,\qquad U(e)=A\cup B.           \tag{1.1}
\]

The fixed table quantifier is harmless but important: if a physical fragment
has several orientations or boundary states, one must either enumerate those
fixed tables or use an exact exclusive-state gadget.  Treating different state
copies as independent vertices is not capacity-faithful.  In particular, a
partial endpoint history relation is handled by fixing one accepted endpoint
state in the table and then quantifying over all such choices; it is not
silently promoted to a full reset state.

Let `b_q in {0,1}` be the required residual multiplicity of every physical
resource.  Some resources have only an upper bound; write their requirement as
`<=b_q`.  The fixed internal fragments and the chosen joins must together meet
these rows.  In particular, exact lower- and cap-palette preservation means
equality for every residual lower facet and cap.

## 2. Capacity-faithful ordered split graph

Fix a candidate closing join

\[
                              e_*:z\longrightarrow p                 \tag{2.1}
\]

and a total order `prec` on `F` with `p` first and `z` last.  Keep only
nonclosing joins `u->v` with `u prec v`.  Split the fragments into tail and
head shores, remove `z_tail` and `p_head`, and put an edge
`u_tail v_head` for every retained join.  Denote the balanced bipartite graph
by `B^0`.

Literally, the nonclosing path leaves `r`, traverses the ambient fragments,
ends at the exit of `z`, and `e_*` returns to `s`.  Thus the two exposed
far sockets, rather than merely their owner labels, are conditioned in the
construction.

Call this fixed state table **capacity-faithful** when projection gives a
bijection between perfect matchings of `B^0` and join selections satisfying
all of the following:

\[
\begin{aligned}
 &\text{one outgoing join from every }u\ne z,\quad
   \text{one incoming join to every }v\ne p,\tag{2.2}\\
 &\sum_{e:q\in R(e)}x_e\le b_q
       \quad\text{for every capacity row},                         \tag{2.3}\\
 &\sum_{e:q\in R(e)}x_e=b_q
       \quad\text{for every exact residual row}.                   \tag{2.4}
\end{aligned}
\]

The contribution of `e_*` is subtracted from `b` before (2.3)--(2.4).  This
definition includes exclusive boundary-state choices.  It is stronger than
per-join legality.

### Theorem 2.1 (literal endpoint-conditioned corridor theorem)

Under the fixed-state and capacity-faithful hypotheses, the following are
equivalent.

1. The path `P^epsilon` extends, using the fixed order and closing join, to a
   co-oriented spanning physical cycle which realizes every prescribed
   lower/cap/history resource exactly.
2. `B^0` has a perfect matching.
3. For every subset `A` of the left shore,

\[
                              |N(A)|\ge |A|.                         \tag{2.5}
\]

The one perfect matching materializes both phases `epsilon=0,1`.  If the same
ambient fragments and joins are used in the same orientations, then

\[
            \sigma(C^1)-\sigma(C^0)
               =\sigma(P^1)-\sigma(P^0)=0.                          \tag{2.6}
\]

#### Proof

Let `M` be a perfect matching.  It selects one outgoing join from every
fragment other than `z`, one incoming join to every fragment other than `p`,
no incoming join to `p`, and no outgoing join from `z`.  Every selected join
is forward in `prec`; hence the selected digraph is acyclic.  Each of its
components is a directed path.  Only `p` can have indegree zero, so there is
only one component.  It is the spanning path from `p` to `z`.  Adding `e_*`
gives one directed spanning cycle.

Expand the contracted vertex `p` to `P^epsilon` and every other vertex to its
fixed literal fragment.  Join acceptance proves both history polarities at
every new seam; internal acceptance handles every other run.  Capacity
faithfulness gives (2.3)--(2.4), so no owner, facet, cap, history occurrence,
or private resource is duplicated and every exact residual palette row is
filled.  This proves (1).

Conversely, contract the fixed fragments in any cycle satisfying (1) and
delete `e_*`.  Its `|F|-1` forward joins give the required perfect matching.
Hall's theorem proves (2) iff (3).

The endpoint states of `P^0` and `P^1` are identical, so the same selected
joins accept after either expansion.  All ambient fragments and joins cancel
from the old/new directed ledger.  Equation (0.2) gives (2.6).  Notice that
this is a relative statement: the common ambient corridor may have nonzero
absolute quotient voltage. \(\square\)

### Corollary 2.2 (materialization algorithm)

For a fixed `e_*`, order, and capacity-faithful table, one may construct the
host by:

1. finding a perfect matching `M` of `B^0`;
2. reading its unique successor of each fragment other than `z`;
3. listing the resulting chain from `p` to `z`;
4. expanding each fragment and join literally; and
5. appending `e_*`.

No topology search remains after the matching.  A failure returns an exact
Hall shore `A` with `|N(A)|<|A|`.  Minimizing over the finite choices of
`e_*`, fixed boundary-state table, and total order is therefore an exact
endpoint-conditioned criterion, not an asymptotic surrogate.

### Theorem 2.3 (exact master without capacity faithfulness)

If the expansion is not capacity-faithful, introduce one binary variable
`x_e` for every forward literal join and impose

\[
\begin{aligned}
 \sum_{e:\operatorname{tail}(e)=u}x_e&=1 &&(u\ne z),\\
 \sum_{e:\operatorname{head}(e)=v}x_e&=1 &&(v\ne p),\\
 \sum_{e:q\in R(e)}x_e&\le b_q &&(q\text{ a capacity row}),\\
 \sum_{e:q\in R(e)}x_e&=b_q &&(q\text{ an exact row}).              \tag{2.7}
\end{aligned}
\]

Together with the fixed closing join, (2.7) is necessary and sufficient for
the same literal spanning construction.  If an absolute sidecar residue
`rho` is required, add

\[
                  \sigma(e_*)+\sum_e x_e\sigma(e)=\rho.             \tag{2.8}
\]

#### Proof

The first two lines give the same indegree/outdegree pattern as a perfect
matching.  Forwardness again makes it one `p`-to-`z` spanning path.  The last
two lines are exactly the physical resource ledger, and (2.8) is exactly the
additive sidecar ledger.  Conversely, read these variables from a literal
host. \(\square\)

Thus Hall is an exact theorem only on the capacity-faithful face.  In the
general face, (2.7) is the exact finite object; dropping its resource rows is
only a projection.

## 3. Order-free graphic formulation

For a fixed closing join `e_*:z->p`, let `M_out` and `M_in` be the outgoing
and incoming partition matroids on the candidate joins, with the endpoint
parts deleted as above.  Let `M_gr` be the graphic matroid after forgetting
directions and viewing each fragment as one vertex.

### Theorem 3.1 (rooted common-base form)

A set `Q` of `|F|-1` joins gives one directed spanning `p`-to-`z` corridor iff
it is a common base of `M_out`, `M_in`, and `M_gr`.  With the capacity/exact
rows (2.3)--(2.4), expanding `Q union {e_*}` gives the same two phase-common
cycles as Theorem 2.1.

#### Proof

The two partition bases give the stated indegree and outdegree pattern.  A
graphic base is a spanning tree.  A directed graph with that degree pattern
whose undirected support is a tree is the unique path from `p` to `z`.
Conversely, a spanning path is a base of all three matroids.  Literal
expansion is exactly the proof of Theorem 2.1. \(\square\)

This is an intersection of three matroids plus possible physical packing
rows.  It is not an ordinary two-matroid-intersection theorem.  In the ordered
form, forwardness makes the graphic row automatic; that is the precise gain
from conditioning on an order.

## 4. Exact audit of capacity faithfulness

The capacity-faithful hypothesis can be checked without trusting a state
compiler.  First delete every candidate edge using a resource whose residual
capacity is zero after fixing `e_*`.  For a resource `q` whose residual
capacity is one, let

\[
                         E_q=\{e\in E(B^0):q\in R(e)\}.              \tag{4.1}
\]

### Theorem 4.1 (pair-deletion test)

The row

\[
                              \sum_{e\in E_q}x_e\le1                \tag{4.2}

\]

is valid for every perfect matching of `B^0` iff, for every two vertex-disjoint
edges `e,f in E_q`, the graph obtained by deleting the four endpoints of
`e,f` has no perfect matching on its remaining balanced shores.

#### Proof

A perfect matching violates (4.2) iff it contains two disjoint members
`e,f` of `E_q`.  After fixing those edges, its remaining edges are precisely
a perfect matching of the four-endpoint deletion.  The converse is obtained
by adjoining `e,f`. \(\square\)

Thus capacity faithfulness has a proof-safe finite audit: apply Theorem 4.1
to every physical owner-copy, facet, cap, history occurrence, and private
resource introduced by the state expansion.  Exact-one rows then follow from
the at-most-one audit plus the appropriate cardinality identity when every
selected join consumes exactly one member of a residual bank of the same
size.

### Corollary 4.2 (star-fibre Boolean sufficient condition)

Suppose that, for every capacity-one physical resource `q`, all edges of
`E_q` share one tail or all share one head.  Then every perfect matching is
capacity-safe.  If, in addition,

* every selected join consumes one residual lower facet and one residual cap;
* the residual lower and cap banks each have `|F|` members including the
  resources of `e_*`; and
* all candidate joins use only those banks,

then every perfect matching realizes both residual palettes exactly.

In the Boolean Johnson host this condition is checked literally on the fibres
of the maps `e |-> A intersect B` and `e |-> A union B`, together with the
history and private-resource fibres.

#### Proof

A matching contains at most one edge of any star, proving all capacity rows.
After adding `e_*`, the cycle contains exactly `|F|` joins.  Their lower labels
are distinct members of a bank of size `|F|`, hence give that bank exactly;
the same counting proves the cap statement. \(\square\)

The star condition is the sharp local condition for making one resource row
automatic from matching constraints: an edge family in a bipartite graph has
matching number at most one iff it is a star.  If `E_q` contains two disjoint
edges, the two-edge matching already duplicates `q`; it extends to a perfect
matching exactly in the case detected by Theorem 4.1.  The smallest warning is
a `2 x 2` graph whose diagonal edges both consume `q`: Hall holds, while the
diagonal perfect matching is physically illegal.

This corollary is deliberately a strong **occurrence-token/local-palette**
subclass.  Exact use of a bank of occurrence-labelled cap tokens implies
global distinct rank-`m+1` cap values only when that bank was itself defined
with exactly one token for each required literal cap value and the token-to-set
projection is injective.  Without that additional hypothesis, the conclusion
is exact token preservation, not global upper-palette surjectivity.

## 5. A protected-factor/fusion-tree sufficient construction

There is a second checkable Boolean route which does not require guessing one
global order at the outset.  Suppose there are phase-indexed spanning incidence
two-factors

\[
                         F_0^\epsilon=P^\epsilon\cup R              \tag{5.1}
\]

with the **same oriented ambient residual edge set** `R` and the same
component table after contracting `P^epsilon` to `p`.  This is a
phase-common residual completion; it does not assert that the internally
different `P^0,P^1` are one undirected path.  Let the common contracted
components be vertices of a tree `T`.
For each edge of `T`, choose a pair of directed factor joins, one in each
incident component, and replace them by the crossed pairing.  Assume:

1. all chosen supports are pairwise disjoint;
2. both crossed joins are literal Johnson joins and pass the exact endpoint
   histories;
3. the old and new join pairs have identical lower-facet and cap multisets;
4. no protected packet edge or protected resource is touched; and
5. the crossed pair is retained identically in the two phases.

### Theorem 5.1 (transparent fusion tree)

Under these hypotheses the same `|T|-1` switches merge each `F_0^epsilon`
into one co-oriented spanning cycle containing `P^epsilon`, preserve the
complete immediate lower and upper palettes and all tested boundary histories,
and contribute zero old/new relative displacement.

#### Proof

A crossed two-edge switch between two distinct directed cycles merges them
into one directed cycle.  Pairwise-disjoint supports allow the switches to be
applied in any leaf order of `T`; each tree edge reduces the component count by
one, so the final factor has one component.  Conditions 2--4 prove literal
legality and resource preservation.  Condition 5 makes every ambient switch
cancel in the relative fragment ledger, leaving (0.2). \(\square\)

This is stronger than the small protected-factor theorem only when such a
transparent fusion tree is supplied.  The small protected-factor theorem by
itself gives a spanning two-factor, not the tree of history- and cap-transparent
switches.

## 6. Exact limitations and the remaining gate

The theorem closes the ambient-corridor row **conditionally and literally**:

* one spanning component, rather than a marginal path cover;
* exact endpoint histories in both polarities;
* exact owner/facet/cap capacities named in the table;
* the same co-oriented ambient corridor in both fixed-`z` phases; and
* zero relative sidecar displacement.

It does not prove any of the following.

1. That some closing join, state table, and order satisfies Hall.
2. That a non-capacity-faithful per-arc catalogue becomes faithful merely by
   state splitting.
3. Absolute zero or coprime quotient voltage.  The common corridor can have a
   fixed nonzero residue; a role-converting pump is needed only if that absolute
   fibre misses the required target.
4. Preservation of rank-`>=r+2` upper interval unions, source/envelope data, or
   the terminal compiler unless those resources are included explicitly in
   `R(e)` and in (2.3)--(2.4).
5. A universal Boolean star-fibre or transparent-fusion-tree supply theorem.

Accordingly the unresolved ambient theorem is now exact: construct one
endpoint-conditioned fixed-state table satisfying either Theorem 2.1 (with
Theorem 4.1 as its resource audit) or Theorem 5.1.  A failure of all ordered
tables must be certified by their Hall shores or by a nonredundant physical
resource row; a failure of absolute voltage alone is not a corridor/topology
obstruction.
