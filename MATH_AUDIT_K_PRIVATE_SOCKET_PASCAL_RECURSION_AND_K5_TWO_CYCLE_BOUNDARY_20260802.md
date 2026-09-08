# Private-socket Pascal recursion and the first all-high topology boundary

**Date:** 2026-08-02  
**Status:** unconditional recursive closure theorem for private
singleton-tail skeletons, exact block-port criterion for a
block-respecting Hamilton lift, an independent proof of the all-odd
depth-one Hamilton family, and a solver-free first-boundary audit.  Every
balanced owner-exact all-high depth-two table at `k=5` has exactly two
directed 5-cycles.  No upper, residence, exterior, or compiler assertion is
made.

## 0. Verdict

The cut-charge theorem has a clean constructive recursive face.  Suppose a
child role--tail system is feasible and its state bank is partitioned into
Pascal sectors.  If every sector contains a spanning tree made from roles
whose legal tail lists are singletons, and further singleton-tail roles
connect the sectors along a quotient spanning tree, then their union has
identically zero Hall charge.  It therefore extends to one connected
balanced selector.  This gives an exact same-parity induction interface:

1. inherit a private spanning skeleton inside every child sector;
2. supply one private connector socket for every edge of a quotient tree;
3. preserve the literal singleton-tail property after all owner, target,
   and protected rows are imposed; and
4. prove feasibility of the complete child role--tail system.

There is a parallel exact Hamilton interface.  A block-respecting child
Hamilton cycle is equivalent to choosing a spanning directed path through
each sector and compatible entry/exit ports whose quotient transitions form
one directed cycle.  Thus a scalar parent Hamilton certificate is not the
right Pascal state: the recursion must export a two-ended path relation.

The Hamilton alternative does have a genuine infinite family.  Any Middle
Levels Hamilton cycle in `B_(2r-1)` yields a depth-one literal Hamilton rail
using every rank-`r` owner and rank-`(r-1)` target exactly once.  Either
parity matching extends to an SCD, so the same roles also carry a static
partition of every lower Boolean rank.  Only the rank-`(r-1)` row is
serialized by the depth-one source word.

The smallest attempt to raise depth identifies the first exact boundary.
At `k=3,d=1` the three singleton states form a private directed Hamilton
cycle.  At `k=5,d=2`, every feasible all-high flag table is a regular
tournament.  Owner exactness then forces one transition permutation, and it
is the disjoint union of the step-one and step-two directed 5-cycles.  Hence
there is neither a Hamilton predecessor rail nor a spanning bank of
private singleton-tail sockets on this face.

The boundary is structural, not a degree failure: all local state blocks
are `K_(2,2)`.  Any successful same-parity recursion must therefore export
an open port, a non-all-high role, or a compound matching-closed absorber
already at `3 -> 5`.  The ordinary SCD continuation fails later and more
visibly at `k=7,d=3`, where a root has no legal successor.

## 1. Role--tail notation

Let `I` be a fixed owner/target-exact role set and `V` its realized state
bank.  Role `i` has fixed head `h_i in V` and nonempty legal tail list
`N(i) subseteq V`.  Put

\[
 a(v)=|\{i:h_i=v\}|.
\]

Assume the system has a balanced selector.  Thus one can choose one tail in
every list so that state `v` is used as a tail exactly `a(v)` times.  For a
reserved assignment bank `R`, recall the cut charge

\[
 \chi_R(Y)=
 |\{i\in R:t_i\in Y,\ N(i)\not\subseteq Y\}|.             \tag{1.1}
\]

The exact cut-charge theorem says that `R` is Hall-safe precisely when its
vertex capacities are respected and `chi_R(Y)` does not exceed the original
Hall slack on any shore `Y`.

## 2. Private-socket recursive closure

Partition the state bank into nonempty sectors

\[
                         V=\dot\bigcup_{x\in X}V_x.           \tag{2.1}
\]

A reserved role assignment is **private** when

\[
                         N(i)=\{t_i\}.                        \tag{2.2}
\]

Let `R_x` be a bank of distinct private roles whose projected undirected
edges `t_i h_i` contain a spanning tree of `V_x`.  Let `C` be a further
bank of distinct private roles, disjoint from all `R_x`.  Contract every
`V_x` in the projections of `C`, discard loops, and call the resulting
multigraph `Q_C`.

### Theorem 2.1 (private-socket Pascal closure)

If the complete role--tail system is feasible, all roles in

\[
                         R=C\mathbin{\dot\cup}
                           \dot\bigcup_{x\in X}R_x             \tag{2.3}
\]

are private, and `Q_C` contains a spanning tree of `X`, then `R` is a
Hall-safe spanning-tree skeleton.  Consequently the table has one connected
balanced selector and hence one Euler chronology.

#### Proof

Singleton lists give

\[
 t_i\in Y\quad\Longrightarrow\quad N(i)\subseteq Y
\]

for every shore `Y`, so `chi_R(Y)=0` identically.  Feasibility of the full
system implies nonnegative Hall slack.  It also implies the tail-capacity
inequalities for `R`, because every private role is forced in every balanced
selector.

The union of the internal trees spans each `V_x`.  The quotient tree
supplied by `C` joins those sector trees, so the projected edges of `R`
contain a spanning tree of all `V`.  The cut-charge theorem now extends `R`
to a balanced selector.  Its support is connected and balanced, hence
Eulerian.  \(\square\)

### Corollary 2.2 (two-sector induction step)

Suppose a Pascal child consists of two embedded parent sectors, each
retaining a private spanning skeleton.  If the child role--tail system is
feasible and one additional private role has its tail in one sector and
head in the other, then the child has a connected balanced selector.

The conclusion is literal only when the embeddings preserve the complete
owner and named-target payloads and the cross role remains singleton after
all protected option deletions.  An SCD owner lift or an unordered
containment edge does not imply this last condition.

This is a genuine recursive closure theorem: once the private certificate
is present, no new Hall inequality is needed at later levels.  The hard
Boolean construction row is exactly the supply of the private cross socket.

## 3. The exact block-port Hamilton interface

The Hamilton route has a different, equally exact recursive state.  Let a
directed predecessor graph `D` have a vertex partition (2.1).  For each
sector `x`, define the port relation

\[
 {\cal P}_x\subseteq V_x\times V_x                       \tag{3.1}
\]

by `(s,t) in P_x` when `D[V_x]` has a directed Hamilton path from `s` to
`t`.  Retain payload labels in this relation when a path is required to use
prescribed roles or edges.

### Theorem 3.1 (ported block-Hamilton criterion)

There is a Hamilton cycle of `D` which visits every sector contiguously if
and only if one can choose `(s_x,t_x) in P_x` for every `x` and cyclically
order the sectors

\[
                         x_0,x_1,\ldots,x_{|X|-1}              \tag{3.2}
\]

so that

\[
                         t_{x_j}\longrightarrow s_{x_{j+1}}
                         \quad\hbox{lies in }D                 \tag{3.3}
\]

for every `j` modulo `|X|`.

#### Proof

Concatenate the paths certified by (3.1) using the arcs (3.3).  They are
vertex-disjoint and cover all vertices, so the result is a Hamilton cycle.
Conversely, cut a block-contiguous Hamilton cycle at every sector boundary.
Its restriction to sector `x` is a spanning directed path with endpoints
`s_x,t_x`, and its cross edges are exactly (3.3).  \(\square\)

For a two-sector Pascal split, the exported state is therefore not merely
"the parent has a Hamilton cycle."  It is a nonempty relation of admissible
Hamilton path endpoints, together with the two cross-port predicates.  This
is the same deletion--contraction reachability state forced by the Pascal
determinant calculation.

### Lemma 3.2 (atomic singleton--rectangle incompatibility)

A nontrivial `2 x 2` tail-exchange rectangle cannot consist of private
singleton-tail roles.

#### Proof

A rectangle on distinct tails `u,v` and roles `i,j` requires

\[
                         u,v\in N(i)\cap N(j).                 \tag{3.4}
\]

Hence both lists have size at least two.  This contradicts (2.2).
\(\square\)

Accordingly a "private rectangle absorber" must mean a compound macro:
after its internal matching phase is fixed and contracted, its exposed
tail socket is private.  At the atomic role--tail level one must choose
between the zero-charge singleton mechanism of Theorem 2.1 and the
matching-closed transparent rectangle mechanism.  Conflating them hides a
real recursive state.

## 4. An all-odd depth-one Hamilton family

Put

\[
                         k=2r-1,\qquad r\ge2,                 \tag{4.1}
\]

and take a Middle Levels Hamilton cycle

\[
 q_0,T_0,q_1,T_1,\ldots,q_{W-1},T_{W-1},q_0,             \tag{4.2}
\]

where every `q_i` has rank `r-1`, every `T_i` has rank `r`, and

\[
                         q_i\subset T_i\supset q_{i+1}.       \tag{4.3}
\]

### Theorem 4.1 (all-odd depth-one Hamilton rail)

Give role `i` owner `T_i`, one-letter head `q_(i+1)`, and selected tail
`q_i`.  These roles form a literal directed Hamilton cycle which uses every
rank-`r` owner and every rank-`(r-1)` head target exactly once.

#### Proof

The two distinct rank-`(r-1)` facets of `T_i` satisfy

\[
                         q_i\cup q_{i+1}=T_i.                  \tag{4.4}
\]

Thus the two-letter trace `(q_i,q_(i+1))` has the declared owner.  Its tail
and head are consecutive vertices of the cyclic list of all lower Middle
Levels vertices.  Since (4.2) visits every lower and upper vertex once, the
selected traces form one directed Hamilton cycle and have the two claimed
exact palettes.  \(\square\)

### Corollary 4.2 (simultaneous static SCD payload)

The central perfect matching

\[
                         \{q_{i+1}T_i:i\in\mathbb Z_W\}       \tag{4.5}
\]

extends to a full SCD of `B_(2r-1)`.  Assign its downward chain through
`q_(i+1)` to role `i`.  The roles then carry every nonempty target below the
middle rank exactly once as a static nested payload, without changing the
depth-one Hamilton cycle.

Only `q_(i+1)` is a literal one-letter suffix of the selected trace.  The
deeper SCD members are not thereby serialized source windows.  This is the
precise quantifier boundary of the SCD extension.

The construction and this scope agree with
`MATH_THEOREM_K_MOVING_CORE_PULL_CLOCK_DEPTH_ONE_HAMILTON_RAIL_AND_DEPTH_TWO_BOUNDARY_20260802.md`;
the proof above is an independent replay.

### Corollary 4.3 (private base at `k=3`)

Let the ground set be `Z_3`, let the three depth-one head states be the
singletons, and for `i in Z_3` take the literal trace

\[
                         (\{i\},\{i+1\}).                     \tag{4.6}
\]

Its owner is the two-set `{i,i+1}`.  Thus (4.1) uses every rank-one target
once and every rank-two owner once, and its state support is the directed
3-cycle.

After the owner and head are fixed, the only positive-demand tail state
which completes owner `{i,i+1}` is `{i}`.  Hence all three tail lists are
singletons.  The whole cycle is a private Hall-safe spanning skeleton.

This is the smallest nontrivial canonical ordered-rail realization.

## 5. Exact first same-parity boundary at `k=5`

Now take `k=5`, the all-high depth-two face.  A flag on a rank-two root
`{a,b}` deletes one endpoint and retains the other.  Orient the edge from
the deleted endpoint to the retained endpoint.  Therefore a complete flag
table is exactly a tournament on five coordinates.

A literal transition is a directed two-edge path

\[
                         a\longrightarrow b\longrightarrow c,            \tag{5.1}
\]

with owner `{a,b,c}`.  At centre `b`, predecessor balance is a matching
between the incoming and outgoing tournament edges.

### Lemma 5.1 (balance forces the regular tournament)

If the table has even a fractional balanced transition selector, then every
vertex has indegree and outdegree two.  Thus, up to relabelling, the
tournament is

\[
                         i\longrightarrow i+1, i+2
                         \qquad(i\in\mathbb Z_5).              \tag{5.2}
\]

#### Proof

The state block at `b` is complete bipartite between the incoming and
outgoing edges.  Equal total incoming and outgoing mass is necessary for a
perfect fractional transport.  Their sizes sum to four, so both equal two.
The regular tournament on five vertices is unique up to relabelling.
\(\square\)

At `b`, order its incoming edges by the starts `b-1,b-2` and its outgoing
edges by the ends `b+1,b+2`.  A fractional local matching has matrix

\[
                         \begin{pmatrix}
                         x_b&1-x_b\\
                         1-x_b&x_b
                         \end{pmatrix}.                       \tag{5.3}
\]

The owner `{b-1,b,b+1}` is supplied by only the upper-left turn in (5.3).
Owner exactness therefore forces `x_b=1` for every `b`.  This gives the two
transitions

\[
 \begin{aligned}
 (b-1\to b)&\longmapsto(b\to b+1),\\
 (b-2\to b)&\longmapsto(b\to b+2).
 \end{aligned}                                             \tag{5.4}
\]

### Theorem 5.2 (the unique owner-exact cover is `C_5 dot-union C_5`)

Every balanced owner-exact all-high depth-two table at `k=5` has exactly
two directed components.  They are

\[
 \begin{aligned}
 &(0\to1),(1\to2),(2\to3),(3\to4),(4\to0),\\
 &(0\to2),(2\to4),(4\to1),(1\to3),(3\to0).
 \end{aligned}                                             \tag{5.5}
\]

Consequently this face has no Hamilton predecessor rail and no
Hall-safe spanning-tree skeleton.

#### Proof

Lemma 5.1 and the owner equation force (5.4).  The first transition family
preserves step `+1` and the second preserves step `+2`.  Since both steps
have order five in `Z_5`, they give precisely the two cycles (5.5).

For a fixed head and its forced owner, the third coordinate in (5.1) is
unique.  Hence the realized role has a singleton predecessor list.  All ten
private projected edges are exactly the two components in (5.5); no subset
of them spans the state bank.  The Hamilton equivalence and the private
socket theorem therefore rule out both requested constructions.  \(\square\)

The proof is analytic and covers all labelled tables, because every regular
tournament is a relabelling of (5.2).  No enumeration is used.

### Corollary 5.3 (sharp recursive interpretation)

The private Hamilton certificate at `k=3` does not propagate to
`k=5` inside the strict all-high static face.  Any same-parity construction
starting from this face must export at least one of:

1. an open two-ended path state rather than a closed parent cycle;
2. a non-all-high or boundary-deficient role;
3. a compound matching-closed rectangle whose contracted external socket
   is private; or
4. a rethread which changes the static owner/target association.

This is a scoped obstruction, not a no-go for nonflat triangular tables or
for the verified finite optimal word at `k=5`.

## 6. Reconciliation with SCD and Pascal recursion

The protected SCD selector proves the static named-target rows and can
quarantine a bounded bank of prescribed flags.  It does not make their
predecessor lists singleton and does not supply the path relation (3.1).
The antichain-top owner lift similarly gives a Middle Levels Hamilton cycle
in the two-endpoint projection, but its independently filled age cells need
not satisfy the literal shift law.

The standard recursive SCD reaches an even earlier local failure at the next
depth: at `(k,m,d)=(7,3,3)` the target-exact flag

\[
                         (\{0,1,6\};1,0)                     \tag{6.1}
\]

has no legal successor.  Thus neither the `k=5` two-cycle cover nor the
standard `k=7` SCD table supplies the recursive ports required by
Theorems 2.1 or 3.1.

The exact proof-safe Pascal interface is consequently the tuple

\[
 (\text{payload partition},\ \text{base feasible selector},\
   \text{sector path-port relations},\
   \text{private connector sockets}).                       \tag{6.2}
\]

For rectangle-based fusion one must additionally export the literal four
cross options, payload transparency of all four, and retained connectivity
after the designated old arcs are removed.  A scalar parent existence
statement, unordered Boolean degrees, or SCD containment matchings do not
determine (6.2).

## 7. Scope

The note proves only the lower owner/target-exact balance and topology row.
It does not assert:

* upper interval-union coverage at any width;
* residence or exterior-window preservation;
* a common-cap/compiler matching;
* physical Pascal embeddings of the private sockets; or
* an all-`k` bound for `nu(k)`.

The `k=5` theorem is an obstruction only to the strict all-high static
owner/target-exact face.  Nonflat roles, changed target associations, and
larger alternating packets remain outside its scope.
