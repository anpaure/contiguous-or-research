# Pivot-rich protected paths and the exact Catalan port-path connector

Date: 2026-08-01  
Lane: Thread D, global upper-decorated completion of fixed protected packets  
Status: unconditional graph/topology equivalence and damage ledger;
conditional `O(H)` completion lemma; exact finite and abstract obstructions to
dropping its port hypotheses.  No all-dimensional connector existence theorem
is claimed.

## 0. Outcome

The authoritative local input is
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`.
One packet supplies a simple collared Johnson path with `3h` transitions,
both immediate palettes injective, internal residence runs of length `h+1`,
and zero local strict-lower compiler damage.  The incidence lift of `H`
resource-disjoint packets is a protected 2-bounded bank of `6Hh` edges, so
it embeds in some q1 two-factor when `6Hh<=m-2`.

The missing global theorem is not another local pivot statement.  After an
upper-exact rooted Catalan forest is selected, every component has exactly
one unused directed tail port and one unused directed head port.  Legal
connector incidences form a digraph on the `Cat_m` components.  Selecting
connector edges without resource collisions and without a graphic cycle is
**exactly selecting a directed spanning path cover** in this port digraph.

This gives the following sharp conditional conclusion.

> If the protected rooted Catalan forest has an admissible port path cover
> with `s=O(H)` paths, and the `s` residual physical ports satisfy Hall, then
> the protected pivot paths extend to an upper-surjective q1 factor with at
> most `s` components.  Connector edges cause **zero** immediate-upper holes.
> Because the protected bank is a path forest, every factor cycle has an
> unprotected incidence edge.  Opening there causes at most one
> immediate-upper hole per component, hence at most `s=O(H)` holes.

The path-cover hypothesis is load-bearing.  Ordinary connectivity of the
port graph is insufficient, ordinary q1 factor extension is insufficient,
and even an upper-exact rooted Catalan forest may have deficient residual
ports.  Thus the theorem isolates an exact, useful global gate but does not
prove it for all dimensions.

## 1. Local protected input

Let `ML_m` be the incidence graph between

\[
 {cal L}={[2m-1]\choose m-1},\qquad
 {cal M}={[2m-1]\choose m},                            \tag{1.1}
\]

and put

\[
 W=|{cal L}|=|{cal M}|,qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname{Cat}_m.                            \tag{1.2}
\]

Let `H>=1`, and let `J_1,...,J_H` be pairwise resource-disjoint collared paths supplied by
the sharp pivot packet.  Their incidence lifts form a graph `P` with

\[
                 \Delta(P)\le2,qquad |E(P)|=6Hh.        \tag{1.3}
\]

Assume `6Hh<=m-2`.  The small protected-factor theorem then places `P` in a
spanning q1 two-factor.  This fact is used only to confirm that the owner and
lower-palette requests are consistent.  The arbitrary completion may have
`Theta(W)` components and may miss immediate-upper colours.

Properly two-edge-colour the protected bank as

\[
                         P=P_0\mathbin{\dot\cup}P_1.     \tag{1.4}
\]

For the global theorem below, the colour choice is part of the certificate:
we require a perfect matching `M_0` containing `P_0`, while every edge of
`P_1` is assigned to one of the later selected banks.  The local pivot theorem
does not automatically choose such an `M_0` together with the upper
decoration.

## 2. Rooted Catalan coordinates

Fix a perfect incidence matching `M_0`.  For an edge `e=LU` outside `M_0`
define

\[
 \operatorname{up}(e)=M_0(L)\cup U,\qquad
 \lambda(e):L\longrightarrow M_0^{-1}(U).               \tag{2.1}
\]

A **protected rooted Catalan forest** is a matching
`Q_0 subseteq ML_m-M_0` such that:

1. `|Q_0|=U=W-C`;
2. `up:Q_0 -> {[2m-1]\choose m+1}` is a bijection;
3. the labelled links `lambda(Q_0)` form an undirected forest; and
4. the designated part of `P_1` lies in `Q_0`, with all protected owner,
   lower-colour, upper-colour and guard occurrences retained literally.

Because `Q_0` is a matching, its directed links have indegree and outdegree
at most one.  Every forest component is therefore a directed path, including
an isolated vertex as a path of length zero.  There are exactly

\[
                         W-|Q_0|=C                       \tag{2.2}
\]

such components.

For a component `K`, let `t(K)` be its unique vertex unused as a link tail
and let `h(K)` be its unique vertex unused as a link head.  A physical
incidence `e=t(K)U`, with `M_0^{-1}(U)=h(K')`, is an admissible connector
arc

\[
                              K\longrightarrow K'       \tag{2.3}
\]

when it avoids every frozen/protected resource and passes all declared
edge-local guards.  Let `D(Q_0)` be the resulting directed multigraph on the
`C` components.  Parallel physical incidences remain separately labelled,
although in the simple middle-level host the endpoints determine the edge.

## 3. The port-path-cover equivalence

### Theorem 3.1 (connector forest iff directed path cover)

Let `Q_1` be a set of admissible connector incidences.  The following are
equivalent.

1. `Q_0 union Q_1` is an incidence matching and
   `lambda(Q_0 union Q_1)` is a forest with exactly `s` components.
2. The arcs of `Q_1` form a spanning directed path cover of `D(Q_0)` with
   exactly `s` paths.

In either case

\[
                           |Q_1|=C-s.                    \tag{3.1}
\]

#### Proof

Each component of `Q_0` has only the one unused tail `t(K)` and the one
unused head `h(K)`.  Hence incidence-matching compatibility of `Q_1` is
equivalent to choosing at most one outgoing and at most one incoming arc at
every contracted component.  Such a directed graph is a disjoint union of
directed paths and directed cycles.  Adding a directed cycle creates exactly
one undirected cycle in the link graph; conversely every new undirected cycle
contracts to a directed cycle because all indegrees and outdegrees are at
most one.  Graphic independence is therefore equivalent to absence of
directed cycles.  The selected arcs are consequently a spanning path cover.

A path cover on `C` vertices with `s` paths has `C-s` arcs.  Conversely a
cycle-free partial permutation with `C-s` arcs has `s` path components.
This proves all assertions. \(\square\)

This equivalence is the precise topology hidden in the phrase “Catalan
connector forest.”  It is stronger than connectedness of the undirected
port graph and stronger than existence of an arbitrary residual matching.

## 4. Protected upper-decorated completion

After selecting `Q_0,Q_1`, exactly `s` lower-tail ports and `s` owner/head
ports remain for the second matching.  Let

\[
       G_R=(ML_m-M_0)-V(Q_0\cup Q_1)                    \tag{4.0}
\]

be the induced residual incidence graph on those ports, with all additional
forbidden resources deleted.  Here `M_0`'s **edges**, not its vertices, are
removed: both perfect matchings necessarily use every incidence shore.

### Theorem 4.1 (global protected connector lemma)

Assume:

1. `P` is the union of the `H` fixed pivot-rich protected paths;
2. `M_0,Q_0` satisfy Sections 1--2 and contain their designated protected
   colour classes;
3. `D(Q_0)` has an admissible spanning path cover `Q_1` with `s` paths,
   containing every protected connector assigned to its bank;
4. `s<=aH+b` for fixed constants `a,b`;
5. the remaining graph `G_R` has a perfect matching `R` containing every
   protected residual incidence; and
6. all selected incidences belong to one declared owner/guard state.

Then

\[
                         M_1=Q_0\mathbin{\dot\cup}Q_1
                                  \mathbin{\dot\cup}R    \tag{4.1}
\]

is a perfect matching, and `F=M_0 union M_1` is a q1-rainbow,
immediate-upper-surjective spanning two-factor containing all protected
paths, with

\[
                           c(F)\le s=O(H).               \tag{4.2}
\]

Every protected witness wholly internal to a path `J_i` survives literally.

#### Proof

The three pieces of `M_1` use disjoint incidence shores and `R` covers the
two residual shores, so `M_1` is perfect and disjoint from `M_0`.  Thus their
union is a spanning q1 two-factor containing the designated protected edges.

The bank `Q_0` already contains one occurrence of every immediate-upper
colour.  Neither adding `Q_1` nor adding `R` deletes an edge of `Q_0`, so
upper surjectivity survives.

By Theorem 3.1, the link forest of `Q_0 union Q_1` has `s` components and
graphic rank `W-s`.  Adding the links of `R` cannot lower rank.  The cycles
of the permutation `M_0^{-1}M_1` are the factor components, whence

\[
 c(F)=W-r_{\rm gr}(\lambda(M_1))\le W-(W-s)=s.          \tag{4.3}
\]

No selected connector changes an internal edge or ordering of a protected
path, proving the final statement. \(\square\)

Condition 5 is exactly ordinary Hall on the `s`-by-`s` residual shores.
Conditions 2--3 are the correlated Catalan-scale rows; they cannot be
recovered from the small protected-factor theorem after an arbitrary
completion has been chosen.

### Proposition 4.2 (transparent-cut converse)

Let `F=M_0 union M_1` be an immediate-upper-surjective q1 factor containing
the protected bank and having `c` components.  Suppose one may choose an
unprotected `M_1` edge from each component so that every immediate-upper
colour remains witnessed after the `c` deletions.  If one remaining
occurrence of each upper colour can be selected compatibly with the
designated protected `Q_0` edges, then the remaining matching decomposes as
`Q_0 union Q_1` satisfying Theorems 3.1--4.1 with `s=c`; the deleted edges
are the residual matching `R`.

#### Proof

Deleting one permutation edge from each cycle makes the link graph a
spanning forest with `c` directed path components.  Choose one retained edge
for every upper colour as `Q_0`; it is a rooted Catalan forest because it is
a subset of that link forest.  Put all other retained edges in `Q_1`.
Contracting `Q_0`, Theorem 3.1 gives a `c`-path cover.  The deleted edges use
exactly the residual ports and restore `M_1`. \(\square\)

Without upper transparency, the same operation loses at most `c` named
immediate-upper colours.  Thus the certificate is exact for transparent
openings and coefficient-sharp up to the bounded damage already quantified
below.

## 5. Exact upper-hole ledger

### Proposition 5.1 (zero cost per connector)

Every connector edge in `Q_1` has immediate-upper hole cost zero.

#### Proof

The complete immediate-upper palette is already witnessed injectively by
`Q_0`.  A connector adds an incidence and deletes no member of `Q_0`.
Therefore it cannot remove a witness. \(\square\)

The same is true of the residual edges `R`.  This zero-cost conclusion uses
unused ports.  It would be false for a cut-and-reconnect operation which
first deletes existing decorated edges.

### Proposition 5.2 (one hole per final opening)

Delete one unprotected incidence edge per component to open `F` into a path
forest.  Such an edge always exists here because the protected bank `P` is a
forest and therefore cannot contain every edge of a factor cycle.  Then:

1. every protected path remains intact;
2. at most one immediate-upper occurrence is deleted per component; and
3. the number of missing immediate-upper colours is at most

\[
                             c(F)\le s.                  \tag{5.1}
\]

If each chosen occurrence has another surviving occurrence of its upper
colour, the loss is zero.

#### Proof

At a lower endpoint `L`, the one paired-upper occurrence is
`M_0(L) union M_1(L)`.  Deleting either of its two incidence edges affects
that occurrence and no other lower vertex.  Thus at most one colour loses
an occurrence.  The cuts avoid the protected bank, and there is one per
component. \(\square\)

More generally, fix one selected occurrence witness for every protected
higher-depth upper target, and let `b(e)` be the number of selected witness
intervals using the prospective cut `e`.  A cut set `D` loses at most

\[
                              \sum_{e\in D}b(e)           \tag{5.2}
\]

of these selected witnesses.  Hence a uniform exposure bound `b(e)<=B`
gives at most `Bs` potentially lost higher-depth targets.  Without such an
occurrence-locality hypothesis a single cut can meet arbitrarily many nested
interval witnesses, so the immediate-upper bound (5.1) does not extend
automatically to the full upper tower.

## 6. Two useful sufficient forms

### 6.1 Ordered/DAG connector form

Let `D_f` be a chosen subdigraph of admissible connector arcs which is
acyclic.  Split its vertices into a tail copy and a head copy and let `B_f`
be the resulting bipartite graph.  If

\[
              \nu(B_f)\ge C-s,                           \tag{6.1}
\]

then any matching of size `C-s` gives an `s`-path connector forest: the
matching enforces in/out capacity, while acyclicity of `D_f` excludes link
cycles.  Equivalently, by Hall deficiency,

\[
 \max_{X\subseteq V_{\rm tail}(D_f)}\bigl(|X|-|N^+_{D_f}(X)|\bigr)
                              \le s.                     \tag{6.2}
\]

The residual `s` ports must still be matched in the full physical graph
`G_R`; they need not use the forward/DAG arc set.

This is a genuine flow-checkable sufficient condition.  It is not asserted
for the current Catalan host.

### 6.2 Cycle-cover plus transparent absorber form

Let `A` be an admissible connector matching of size `C-s`.  Its contracted
graph has exactly `s` path components and, possibly, `z` directed cycles.
Assume that whenever `z>0` there is an occurrence-disjoint packet exchange
which:

1. preserves matching size, both protected incidence shores, and every
   immediate-upper colour;
2. avoids all protected paths and reserved residual ports; and
3. reduces `z` by one without changing the number `s` of path components.

Then `z` serial exchanges produce the path-cover hypothesis of Theorem 4.1.
All exchanges and connectors have zero immediate-upper hole cost.  The
prepared pentagonal four-path absorber is the special case `s=4`; its
serial accessibility is an additional hypothesis, not a consequence of the
pivot-rich geodesic packet.

## 7. Sharp obstructions to weaker statements

### 7.1 Connectivity does not control path-cover number

Let a port digraph consist of a centre `v` and `n-1` leaves, with both arcs
between `v` and every leaf.  It is strongly connected.  In a directed path
cover, `v` has at most one selected incoming and one selected outgoing arc,
so at most two leaves can share its path.  At least `n-3` leaves remain
singleton, and every path cover has at least `n-2` paths.

Thus even strong connectivity does not imply `O(H)` components.  A high-rank
matching/path-cover row such as (6.1), or a certified absorber, is essential.
This is a graph-theoretic obstruction; it is not asserted to be an actual
middle-level port fixture.

### 7.2 An actual rooted Catalan residual-Hall obstruction

The authenticated `m=4` upper-exact rooted Catalan forest has `C=14` port
components but residual matching rank only `11/14`; its port-gap vector is

\[
                         (4,2,2,3,3,1,-1).               \tag{7.1}
\]

The negative coordinate is invariant under every aligned pentagonal pivot
available in that fibre.  Therefore upper exactness and a Catalan forest do
not imply even residual matching, much less an `O(H)` path cover.

### 7.3 Protected typed-head collision

At the smallest authenticated protected rooted fixture (`m=4`), a
palette-transparent root-aligned pentagonal packet forces

\[
                         52\longrightarrow54,            \tag{7.2}
\]

while the protected collar already forces

\[
                         50\longrightarrow54.            \tag{7.3}
\]

The two lower rows demand the same head, so no second matching contains both.
This is an exact counterexample to replacing the protected port conditions
by lower-row disjointness plus palette transparency.  Connector packets must
be selected correlatively with the global head matching.

## 8. Exact remaining theorem

For the sharp pivot-rich packets, the local rank, q1, residence-interior and
strict-lower compiler rows are proved.  A dimension-uniform global result now
needs precisely:

1. a protected rooted Catalan forest `Q_0` compatible with the chosen
   packet colour classes;
2. either an `O(H)` port path cover or a cycle cover with a serial
   upper-transparent absorber;
3. Hall on the remaining `O(H)` physical ports; and
4. safe openings with bounded exposure to the higher upper tower.

Under these hypotheses Theorem 4.1 gives the desired `O(H)`-component
upper-decorated connector, with zero upper-hole loss per connector and at
most one immediate-upper hole per final opened component.  None of the
current local pivot-rich, q1 planting, or ordinary connectivity theorems
proves hypotheses 1--3 uniformly.
