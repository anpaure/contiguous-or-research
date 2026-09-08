# ECO private hypertrees: construction order, owner alignment, and weighted router rank

Date: 2026-07-31  
Status: exact prepared-factor selection and composition theorem, with sharp
counterexamples; no all-\(m\) prepared private ECO hypertree construction

## 0. Verdict

The coherent-ECO supply theorem settles only the first, static row.  At a
fixed coordinate rotation its component hypergraph has connected
two-section in every dimension, and its physical-port and two displayed
forced-colour-face collision graphs are one and the same path forest.  Hence
one independent set removes all three local collision systems at once.

Three further implications are false without extra hypotheses.

1. Connected two-section does not imply a simultaneously usable ECO
   hypertree.
2. A collision-free clean hypertree does not imply one common owner
   decoration.  The complete minimal two-atom topology-safe raw canonical
   \(m=5\) catalogue is an exact counterexample.
3. For the deletion-stable router-resilience row, one node-private
   occurrence route per atom proves only the ordinary binary-tree charge.
   (It can still prove fixed simultaneous route feasibility.)  An ECO atom
   which merges three components has topological rank two, and losing it
   must cost at least two router deletions.

The valid recursive order is therefore

\[
 \boxed{
 \begin{array}{c}
 \text{controlled repair/rethread with an exported ECO bank}\ 
 \longrightarrow\text{ collision-free, clean ECO hypertree}\ 
 \longrightarrow\text{ owner-aligned residual Hall on that same tree}\ 
 \longrightarrow\text{ rank-weighted private/laminar occurrence routing}.
 \end{array}}
                                                               \tag{0.1}
\]

Under the literal hypotheses below, these four stages compose.  The result
is a fixed-decoration Hamilton endpoint with the prepared forced-port Hall
and router rows closed.  Residence, deeper shadows, terminal sockets and
voltage, Pascal reachability, and the common-\(Q\) compiler remain separate.

## 1. Prepared ECO atoms and the common collision forest

Use the paper parameter \(n\): the middle-levels ground set has size
\(2n+1\).  Let \(F\) be a prepared two-factor with initial component set
\(Q\).  A **literal ECO atom** \(t\) is an \(F\)-alternating incidence
hexagon with old matching \(O_t\), new matching \(N_t\), six named ports,
and common external labels \((d_t,e_t)\).  Its component support is

\[
 S_t=\{C\in Q: C\text{ contains an edge of }O_t\}.               \tag{1.1}
\]

Atoms in a simultaneous bank must have disjoint physical port sets, unless
an explicit product-cube capacity certificate is supplied.  Throughout the
clean private theorem we use the disjoint case.

For the canonical fixed-rotation family, atoms are indexed by
\(D=1u0v\in{\cal D}_{n-1}\).  The exact collision theorem says that the
physical-port collision graph and the forced-colour collision graph on
each shore are the same path forest, with directed edges

\[
            1p100v\longrightarrow1p010v.                         \tag{1.2}
\]

It has

\[
 |V|=\operatorname {Cat}_{n-1},\qquad
 |E|=\operatorname {Cat}_{n-2}.                                  \tag{1.3}
\]

### Corollary 1.1 (one collision-free bank clears all local systems)

For \(n\ge3\), there is a fixed-rotation ECO subbank of size at least

\[
       \operatorname {Cat}_{n-1}-\operatorname {Cat}_{n-2}       \tag{1.4}
\]

whose physical ports and both displayed forced-colour faces are pairwise
disjoint.

#### Proof

In any graph, choosing one endpoint from every edge gives a vertex cover of
size at most the number of edges.  Its complement is independent.  Apply
this to the common path forest and use (1.3).  Independence clears all
three collision systems because their edge sets are literally identical.
\(\square\)

For \(n\le2\) the collision system is empty or trivial and is handled
directly; formula (1.4) is not asserted there.

This is only a positive-density local bank.  It does not imply that the
component hyperedges of an independent subbank still span \(Q\), that its
atoms have the right topological phase, or that any forced occurrence is
owned by a global decoration.

## 2. The exact clean-hypertree topology row

For a selected atom family \(T\), let \(B(Q,T)\) be the simple bipartite
incidence graph with vertex classes \(Q,T\) and edge \(Ct\) when
\(C\in S_t\).  Discard component-neutral atoms here, so
\(|S_t|\in\{2,3\}\), and put

\[
                         w_t=|S_t|-1.                            \tag{2.1}
\]

Call \(B(Q,T)\) a **Berge tree** when it is a tree.  An ordering
\(t_1,\ldots,t_s\) is **clean** when, just before toggling \(t_i\),

* every edge of \(O_{t_i}\) is still present;
* the \(|S_{t_i}|\) incidence branches of
  \(B(Q,T)-t_i\) represented at its ports lie in distinct current factor
  components; and
* replacing \(O_{t_i}\) by \(N_{t_i}\) joins those components into one,
  without a simultaneous split.

This is an occurrence-level condition.  It is not inferred from the set
\(S_t\) alone.

### Theorem 2.1 (clean ECO hypertree execution)

Suppose that

1. the atoms in \(T\) are pairwise port-disjoint and are literal
   all-or-none degree-preserving toggles;
2. \(B(Q,T)\) is a Berge tree; and
3. \(T\) has a clean ordering.

Then the ordered toggles end in one factor component.  Since the atoms are
port-disjoint, all toggles commute as symmetric differences, so their
simultaneous endpoint is the same Hamilton factor.

Moreover,

\[
                  \sum_{t\in T}w_t=|Q|-1.                         \tag{2.2}
\]

Conversely, suppose the initial supports \(S_t\) are frozen, no toggle
creates a connection between two initial-component blocks except through
an atom incident with both blocks, and every selected atom has exact
decrement \(|S_t|-1\) relative to those supports.  If such a
component-faithful support family admits a monotone execution ending in one
component, then its incidence graph is a Berge tree.

#### Proof

Because \(B(Q,T)\) is a tree,

\[
 \sum_{t\in T}|S_t|=|E(B)|=|Q|+|T|-1,
\]

which is equivalent to (2.2).  Every clean toggle lowers the component
count by \(w_t\).  Starting from \(|Q|\), the final count is therefore

\[
 |Q|-\sum_t w_t=1.
\]

Disjoint ports make the symmetric differences commute.  For the converse,
the final connectivity makes the incidence graph connected, while the
sum of exact decrements is \(|Q|-1\); hence
\(|E(B)|=|V(B)|-1\), so the connected incidence graph is a tree.
\(\square\)

A rooted postorder is a useful sufficient clean ordering: after every child
subtree has been contracted, toggle the parent atom, provided its literal
port pairing joins the incident branches.

### Lemma 2.2 (three-touch atoms are clean; two-touch atoms need a phase)

If the three old ECO edges lie in three distinct current factor cycles,
the toggle is automatically clean and has \(w_t=2\).  If they lie in only
two current cycles, clean merging is not automatic.

#### Proof

Removing one old edge from each of three cycles leaves three paths paired
by the old matching.  Replacing that matching by the opposite matching of
the incidence hexagon joins the three paths into its one alternating
six-cycle.

For two touched cycles, label the old and new port matchings

\[
 O=\{01,23,45\},\qquad N=\{05,21,43\},                            \tag{2.3}
\]

and suppose \(45\) is the singleton old edge.  The doubled cycle can induce
either pairing

\[
 P_{\rm good}=\{02,13,45\},\qquad
 P_{\rm bad}=\{03,12,45\}.                                      \tag{2.4}
\]

Then \(P_{\rm good}\cup N\) is one six-cycle, whereas
\(P_{\rm bad}\cup N\) is a four-cycle plus a two-cycle.  Thus the first
phase merges and the second is component-neutral.  Earlier toggles can
change this doubled-side pairing, so a prefix-invariant phase bit or the
literal test \(c(P_t^U\cup N_t)=1\) is necessary.  \(\square\)

Connected two-section is strictly weaker than Theorem 2.1.  On
\(Q=\{1,2,3,4\}\), the hyperedges

\[
                \{1,2,3\},\qquad\{2,3,4\}                       \tag{2.5}
\]

have connected two-section, but both are needed to span and their incidence
graph contains the four-cycle through component nodes \(2,3\).  No
subfamily is a spanning Berge tree.  Even the common path-collision theorem
does not remove this issue: on three components, two spanning links may be
the two endpoints of one collision edge, so every collision-independent
subbank is disconnected.

## 3. Exact occurrence-level owner mask

Fix one joint decoration \(D\) by its selected occurrence sets \((I,J)\).
Let \(I\) be its selected rank-\(n\) upper-turn occurrences.  On the
prepared pre-toggle factor, assume the occurrence-labelled
gap--lower-colour graph \(\Gamma_I\) is a forest with unique perfect
matching \(M\), the initial gap representation of \(J\).

Write one ECO atom as

\[
 L_a=H+a, L_b=H+b, L_c=H+c,\qquad
 U_{ab}=H+a+b, U_{bc}=H+b+c, U_{ca}=H+c+a,          \tag{3.1}
\]

with old matching

\[
                 L_aU_{ca},\quad L_bU_{ab},\quad L_cU_{bc}.       \tag{3.2}
\]

Its exact **pre-toggle** owner test is

\[
                    L_a,L_b,L_c\in I                              \tag{3.3}
\]

and membership in \(M\) of the three **named occurrence edges**

\[
\begin{split}
 &(g(U_{ab}),(H-e)+b;U_{ab}),\\
 &(g(U_{bc}),(H-e)+c;U_{bc}),\\
 &(g(U_{ca}),(H-e)+a;U_{ca}).                    \tag{3.4}
\end{split}
\]

The occurrence coordinate in (3.4) cannot be dropped when one lower colour
appears more than once in a gap.

After toggling, the same selected occurrence sets \((I,J)\) persist under
fixed-decoration transparency, but their gap representation can be a
transported matching \(M_U\), not the literal initial edge set \(M\).

### Theorem 3.1 (owner-aligned residual Hall)

Let \(T\) be a port-disjoint coherent ECO family.  If (3.3)--(3.4) hold for
every \(t\in T\), then all its forced ports extend through the one fixed
decoration \(D\).  Equivalently, after consuming the forced gap and colour
vertices, the restriction of \(M\) is a perfect residual matching.

Off the forest face the exact replacement is one vertex-disjoint
\(M\)-alternating-cycle packing which inserts every forced edge outside
\(M\) and deletes none of the already forced edges of \(M\).  Pairwise
disjoint zero-flux blocks are a sufficient specialization, not an
equivalent reformulation.

#### Proof

Equations (3.3) select the upper ports.  Equations (3.4) say literally that
every forced lower edge belongs to the unique perfect matching.  Hence the
named edges already have distinct gap and colour endpoints; port
disjointness also excludes a duplicated physical occurrence edge.  Their
union is a submatching of \(M\), whose restriction after deleting its
endpoints matches every residual vertex.
The nonforest statement is the standard symmetric-difference
characterization of two perfect matchings.  \(\square\)

The common path forest (1.2) ensures only that the prescribed forced
colours and physical ports are distinct.  It does not imply (3.3), does not
place an occurrence into an \(I\)-gap, and does not imply (3.4).

## 4. The raw \(m=5\) owner obstruction fixes the construction order

For the canonical project parameter \(m=5\), the raw factor has three
components and 45 physical ECO atoms.  The complete minimal topology-safe
catalogue has

\[
       648\text{ legal ordered two-atom sequences},\qquad
       324\text{ Hamilton endpoints}.                              \tag{4.1}
\]

Every accepted pair is port-disjoint and its displayed forced-colour faces are
disjoint on both shores.  Nevertheless every endpoint realizes only
\(81/84\) turn colours on each shore and misses

\[
 \mathcal R^+=\{219,365,438\},\qquad
 \mathcal R^-=\{73,146,292\}.                                   \tag{4.2}
\]

Therefore no upper transversal \(I\) exists at all.  In particular neither
Theorem 3.1 nor any nonforest owner exchange can begin.  This proves

\[
 \text{raw collision-free clean ECO hypertree}
 \centernot\Longrightarrow
 \text{owner-aligned decoration}.                                \tag{4.3}
\]

The obstruction is exactly scoped to the unrepaired canonical factor and
minimal raw ECO Hamiltonizations.  It does not apply after a transparent
repair/rethread which restores the missing palettes and either preserves a
named ECO bank or transports it by an occurrence-labelled isomorphism.
Thus the minimal raw two-atom architecture has no owner test.  Any surviving
raw route must first use a neutral or palette-changing packet, or leave that
architecture.  Such preparation must export the literal atom ports, their
clean phase, and their common decoration/router signatures, or the ECO
catalogue must be rebuilt on the prepared factor.

### Theorem 4.1 (the ordered route is positive at the first obstruction)

For project \(m=5\), the synchronized three-\(C_{10}\) repair produces a
pre-glue factor with two components of lengths \(120,132\), selected
occurrence sets \((I,J)\), and a forest gap graph with one perfect matching.
All five fixed-rotation ECO atoms survive disjointly from the repair support
and each Hamiltonizes the two components.  Exactly four,

\[
                110100,\quad110010,\quad101100,\quad101010,       \tag{4.4}
\]

have all six ports selected and pass the literal owner test (3.3)--(3.4).
Their endpoints preserve the same selected palettes, a forest gap graph
with unique matching, and the trace forest.  The atom \(110100\) gives a
nonstandard endpoint outside the four-state standard-glue cube.

Thus (0.1) is unconditionally realized through the owner row at \(m=5\).
For the selected isolated atom \(101100\), the compiled postrepair router
also contains the literal rank-one channel \(s_{g_1}\to z_{g_1}\), and the
separate socket audit closes the Hamilton endpoint.  Thus no cross-atom
packing is needed and the complete finite router row passes.  This compiled
arc is not a uniform physical all-\(m\) channel construction.  The theorem
is a finite base, not an induction.

## 5. Weighted router rank for atomic ECO hypertrees

Fix a clean Berge tree \(B(Q,T)\).  In a prepared occurrence router, call
atom \(t\) **live after deletion \(Y\)** when at least one of its declared
source-to-terminal occurrence routes survives in \(N-Y\), and let
\(R(Y)\) be the dead atoms.  Let \(K_Y\) be the component hypergraph formed
by the live atoms.

### Theorem 5.1 (exact weighted damage identity)

For every router deletion set \(Y\),

\[
             c(K_Y)=1+\sum_{t\in R(Y)}w_t.                         \tag{5.1}
\]

Consequently the fixed ECO hypertree is router-resilient exactly when

\[
       \boxed{\displaystyle
       \sum_{t\in R(Y)}w_t\le |Y|\quad\text{for every }Y.}         \tag{5.2}
\]

#### Proof

Delete the dead atom nodes from the incidence tree.  The remaining graph is
a forest with

\[
 |Q|+|T|-|R(Y)|
\]

vertices and

\[
 |E(B)|-\sum_{t\in R(Y)}|S_t|
\]

edges.  Using \(|E(B)|=|Q|+|T|-1\), its number of components is the
right side of (5.1).  Every forest component contains a component node, so
this is also the component count of the live hypergraph.  Inequality (5.2)
is precisely \(c(K_Y)\le |Y|+1\).  \(\square\)

### Corollary 5.2 (rank-compensated node-private bundles)

For each atom \(t\), suppose there are \(w_t\) alternative occurrence
routes to its terminal bank such that

1. the atom remains live if any one route survives;
2. their vulnerable internal vertex sets are pairwise disjoint;
3. vulnerable sets are disjoint between different atom bundles; and
4. common endpoints are undeletable, or are cloned/capacitated so that one
   deletion cannot kill the whole bundle; distinct atoms have distinct
   capacity-one terminal copies when simultaneous linkage is required.

Then (5.2) holds.

#### Proof

If \(t\) dies, \(Y\) meets all \(w_t\) routes at \(w_t\) distinct
vulnerable vertices.  Cross-atom privacy makes all these charges distinct,
so \(\sum_{t\in R(Y)}w_t\le|Y|\).  \(\square\)

The endpoint clause is essential.  Internally disjoint routes sharing one
deletable source can all die after one deletion.  Cross-bundle privacy is
also essential: two atoms can share the same minimum cut.

A single private path suffices for a two-component atom \((w_t=1)\), but
not for a three-component atom \((w_t=2)\).  With three components, one
ternary ECO atom, and one route through a deletable vertex \(v\), deletion
of \(v\) leaves three pieces, while

\[
                         3>|\{v\}|+1=2.                         \tag{5.3}
\]

This is the smallest weighted-router counterexample.  A ternary atom is one
all-or-none degree-preserving move; its two virtual connectivity units are
not separately executable binary switches.  Corollary 5.2 supplies route
redundancy for that one atomic move, not a binary compilation.

The exact laminar alternative to Corollary 5.2 is a charging certificate
which, for every \(Y\), injects \(w_t\) copies of each dead atom into
distinct vertices of \(Y\).  Calling routes merely “laminar” without this
weighted dead-atom inequality is insufficient.

## 6. Prepared private-ECO composition theorem

### Theorem 6.1 (joint private coherent ECO hypertree)

Assume a controlled repair/rethread produces a prepared factor \(F'\) and
exports:

1. one literal joint decoration \(D=(I,J)\), whose pre-toggle
   occurrence-labelled leaf-forest gap graph has unique matching \(M\);
2. a collision-independent, pairwise-port-disjoint ECO family \(T\) whose
   incidence graph is a Berge tree and which has a clean ordering;
3. the occurrence-level owner memberships (3.3)--(3.4) for every atom;
4. simultaneous fixed-\(D\) transparency and all physical H0--H5/product-
   cube compatibility for every prefix of the clean ordering and every
   router-relevant incidence-subforest; and
5. either the exact weighted router row (5.2) or the rank-compensated
   private-bundle certificate of Corollary 5.2, computed in the actual
   vertex-split capacity-faithful router with one source per atom and
   distinct capacity-one terminal copies.

Then the ordered ECO packet has a literal degree-two Hamilton endpoint,
preserves the one decoration \(D\), has a perfect residual forced-port
matching, and satisfies router resilience

\[
                         c(K_Y)\le |Y|+1
                         \qquad(Y\subseteq V(N)).                  \tag{6.1}
\]

#### Proof

Theorem 2.1 gives the Hamilton endpoint.  Coherence plus item 4 preserves
the selected occurrence sets \((I,J)\) and supplies their transported
gap matching \(M_U\) at every prefix; the initial matching \(M\) is not
asserted to remain literally unchanged.  Theorem 3.1 supplies the initial
simultaneous owner extension and residual perfect matching.  Theorem 5.1
and item 5 give the generalized atomic-hypergraph inequality (6.1).  They also
supply the ordinary simultaneous occurrence linkage: because every
\(w_t\ge1\), (5.2) implies
\(|R(Y)|\le\sum_{t\in R(Y)}w_t\le|Y|\) for every cut \(Y\), and the
prepared gammoid/Menger cut formula links all atom sources to distinct
terminals.  Port
disjointness and the full correlated prefix state ensure these conclusions
refer to the same literal atom choices, not to three marginal selections.
\(\square\)

Equation (6.1) is the grouped atomic-hypergraph damage row.  If a downstream
theorem instead requires the original unit-expanded graphic--gammoid
interface, add a stronger certificate: atom \(t\) must export \(w_t\) named
sources linked simultaneously to \(w_t\) distinct sinks, with one equality
constraint tying all \(w_t\) virtual rank units to the same all-or-none
physical atom.  Corollary 5.2 gives redundant alternatives for atomic
availability; by itself it does not create \(w_t\) simultaneous sources.

On a genuinely slot-private grammar, Theorem 6.1 becomes local after a
clean incidence-tree template is fixed: every atom slot must contain one
candidate carrying **all** of the collision, clean-phase, owner and
rank-compensated route signatures, and the slot annuli must be mutually
private.  Without slot privacy the selection is a grouped hypergraphic
correlation problem.  Separate owner-feasible and route-feasible
hypertrees do not recombine.

## 7. Sharp remaining all-\(m\) lemma

The all-\(m\) coherent supply row is solved, and the common collision forest
gives a large simultaneously collision-free subbank.  The exact remaining
prepared-factor lemma is:

> Construct a controlled palette/matching repair which exports a
> fixed-rotation ECO bank containing a collision-independent clean Berge
> hypertree; find one common leaf-peelable decoration owning every named
> forced occurrence of that hypertree; and give every rank-\(w_t\) atom a
> weighted-private or weighted-laminar occurrence route certificate.

The minimal clean two-atom raw canonical Hamiltonization is closed by
(4.1)--(4.3).  The repaired route is live and exact at the first obstruction
by Theorem 4.1, but that finite base does not prove the displayed lemma for
all \(m\).

Even this lemma stops before residence, all-depth shadow support, terminal
Johnson sockets and primitive voltage, Pascal reachability, and the
common-\(Q\) compiler.  No all-\(m\) equality theorem is claimed.

## 8. Authoritative inputs and audit boundary

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`;
* `MATH_THEOREM_CATALAN_ECO_LOCAL_CHANNEL_EXPORTED_STATE_AND_FIRST_OBSTRUCTIONS_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`;
* `MATH_THEOREM_R_PRIVATE_COHERENT_COLLAR_CHART_AND_PRESERVATION_20260731.md`.

The topology and weighted-router proofs above were independently audited in
this lane.  The finite numbers (4.1)--(4.2) and Theorem 4.1 are imported only
from their frozen literal audits.  No finite search was run for this report.
