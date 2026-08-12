# Order-free partition-Hamilton contraction and the protected pull-tree gate

**Date:** 2026-08-02  
**Lane:** A, independent audit and continuation of the two-corridor reduction  
**Status:** exact contraction and integer formulation; sharp state-fibre
obstruction; exact protected pull-tree sufficient theorem.  No all-dimension
safe-pull supply theorem is claimed.

## 1. Audited physical state model

Let \({\cal P}\) be the residual physical-fragment bank after every internal
fragment of the fixed pump path \(P_3\) has been deleted.  Each physical
fragment \(p\) has an admissible literal-state fibre \(\Sigma_p\), and

\[
             V=\mathop{\dot\bigcup}_{p\in{\cal P}}\Sigma_p.       \tag{1.1}
\]

The accepted digraph \(G_{\rm acc}\) has vertex set \(V\).  Its arcs encode
literal transition compatibility, including the endpoint histories which
are local to one transition.  Shared occurrence capacities and cumulative
charge rows remain global unless they have genuinely been compiled into the
state.

Put

\[
 r_1=D_c,\quad s_1=C_{bc},\qquad
 r_2=B_{bc},\quad s_2=A_b.                            \tag{1.2}
\]

The prescribed new phase adds

\[
             g_1:s_1\longrightarrow r_2,\qquad
             g_2:s_2\longrightarrow r_1.              \tag{1.3}
\]

The first arc is the fixed new-phase Boolean-hex edge \(n_2\).  The second
represents the whole protected pump composite

\[
        A_b\longrightarrow F\xrightarrow{P_3}E\longrightarrow D_c.
                                                               \tag{1.4}
\]

It carries the complete cumulative history, resource, capacity and charge
ledger of (1.4), with every contribution counted once.  Thus no internal
fragment or token of \(P_3\) remains available in (1.1).

If either protected arc has several compatible state realizations, it is a
marked arc fibre and exactly one literal realization must be chosen.  Treating
it as one untyped arc is not sound.

## 2. Exact contraction equivalence

### Theorem 2.1 (two corridors are one partition-Hamilton cycle)

The following pure graph statements are equivalent.

1. There are two vertex-disjoint directed paths

   \[
        Q_1:r_1\leadsto s_1,\qquad Q_2:r_2\leadsto s_2,            \tag{2.1}
   \]

   whose union contains exactly one state from every fibre \(\Sigma_p\).
2. The augmented accepted graph has a directed cycle containing \(g_1,g_2\)
   and exactly one state from every fibre \(\Sigma_p\).

The equivalence remains true after imposing global ledger rows, provided the
same rows are required of the selected object on both sides.

#### Proof

From (2.1), concatenate

\[
 s_2\xrightarrow{g_2}r_1\xrightarrow{Q_1}s_1
 \xrightarrow{g_1}r_2\xrightarrow{Q_2}s_2.
\]

Conversely, deleting \(g_1,g_2\) from the cycle gives the two displayed
paths.  Their cyclic placement forces the uncrossed endpoint pairing, and
the exact-one fibre property is unchanged.  The cumulative ledger is
unchanged because \(g_2\) is precisely the ledger of the deleted composite.
\(\square\)

This proves the prescribed-arc equivalence in
MATH_THEOREM_ROOT_ORDER_FREE_TWO_CORRIDOR_HAMILTON_CONTRACTION_20260802.md,
at audited SHA
\[
 \texttt{7231f74bf433c75d81e117d21861e9763862ccba62ca3ee6accbd6c13c6ea9e6}.
\]

### Proposition 2.2 (forced-arc contraction)

For a forced literal arc \(g:u\to v\), replace the compatible triple
\((u,v,g)\) by one marked state.  Retain only external arcs entering \(u\)
and external arcs leaving \(v\).  Discard arcs entering \(v\), arcs leaving
\(u\), and the reverse internal arc \(v\to u\).  Attach the union ledger with
\(g\) counted once.

Expansion and contraction are mutually inverse on partition-Hamilton cycles
which contain \(g\).  When several compatible triples exist, they are the
states of one marked contracted fibre; they must not be identified.

#### Proof

In every cycle containing \(u\to v\), the unique incoming role of \(v\) and
the unique outgoing role of \(u\) have already been consumed.  Hence only an
arc entering \(u\) and an arc leaving \(v\) can be exterior neighbours of
the contracted state.  Conversely those two exterior arcs uniquely expand
through \(u\to v\).  The ledger convention makes the expansion resource
preserving. \(\square\)

## 3. Exact partition-Hamilton master

Let \(y_\sigma\) select a state and \(x_e\) select an accepted or protected
arc.  For \({\cal A}\subseteq{\cal P}\), put

\[
                 \Sigma({\cal A})=\bigcup_{p\in{\cal A}}\Sigma_p.
\]

### Theorem 3.1 (fibre-union subtour formulation)

In the single-realization protected-arc case, the exact binary master is

\[
\begin{aligned}
 \sum_{\sigma\in\Sigma_p}y_\sigma&=1
                           &&(p\in{\cal P}),\\
 x(\delta^+(\sigma))=x(\delta^-(\sigma))&=y_\sigma
                           &&(\sigma\in V),\\
 x_{g_1}=x_{g_2}&=1,\\
 x\!\left(\delta^+\!\left(\Sigma({\cal A})\right)\right)&\ge1
                           &&(\varnothing\ne{\cal A}\subsetneq{\cal P}),
                                                               \tag{3.1}
\end{aligned}
\]

together with every exact global ledger row.  Before contraction, if
\(\Gamma_i\) is the set of compatible literal state/path realizations of the
\(i\)-th protected composite, replace its forced scalar row by

\[
                         \sum_{e\in\Gamma_i}x_e=1,     \tag{3.2}
\]

and impose the corresponding endpoint-state consistency equations.  After
contraction, use one marked fibre
\(\{\widehat\sigma_e:e\in\Gamma_i\}\) with its ordinary exact-one fibre row.
Each \(\widehat\sigma_e\) indexes the complete path realization and cumulative
ledger, not only its two endpoint states.

No subtour inequalities on arbitrary subsets of state copies are needed:
the fibre-union inequalities in (3.1) are sufficient.

#### Proof

The first two rows make the selected arcs a directed cycle cover on exactly
one state from every physical fibre.  If the cover has more than one cycle,
the physical fibres represented on one cycle form a nonempty proper
\({\cal A}\) with no selected outgoing arc from \(\Sigma({\cal A})\).
Conversely a single cycle crosses every nontrivial union of fibres.  The
forced rows and Theorem 2.1 complete the proof. \(\square\)

## 4. The state-fibre obstruction

Ordinary Hamiltonicity of the expanded state graph and Hamiltonicity of its
physical-fibre quotient are both insufficient.

### Proposition 4.1 (minimal holonomy obstruction)

Let

\[
 \Sigma_A=\{a_0,a_1\},\qquad \Sigma_B=\{b_0,b_1\},
\]

and let the only arcs be

\[
                 a_0\to b_0\to a_1\to b_1\to a_0.    \tag{4.1}
\]

The full state graph is Hamiltonian, and its fibre quotient has both
\(A\to B\) and \(B\to A\).  Nevertheless there is no directed cycle selecting
one state from each fibre.

#### Proof

Every one-state-per-fibre cycle would be a directed two-cycle.  The four-cycle
(4.1) contains none.  Equivalently the state bit changes after one quotient
lap. \(\square\)

Thus quotient Hall, quotient expansion, or an ordinary Hamilton cycle through
all state copies cannot replace the common state section in (3.1).

There is an exact dense calibration after that section is chosen.  Suppose a
globally ledger-feasible transversal is fixed and the two protected arcs are
directionally contracted.  If the underlying simple loopless digraph on
\(N\) selected units satisfies

\[
                         \delta^+,\delta^-\ge N/2,     \tag{4.2}
\]

then the directed Ghouila--Houri theorem gives a Hamilton cycle.  Parallel
literal arcs do not increase the degrees in (4.2), and (4.2) certifies only
topology unless the global ledger was compiled into the selected state/arc
expansion so that every resulting Hamilton cycle is ledger-feasible.

A selector-free but deliberately strong corollary is available.  Call a
physical fibre \(q\) a universal out-neighbour of state \(\sigma\) if every
state in \(\Sigma_q\) receives an accepted arc from \(\sigma\); define
universal in-neighbours dually.  If every state has at least \(N/2\) universal
in- and out-neighbour fibres after the marked contractions, then every
ledger-feasible transversal satisfies (4.2).

This condition is not expected in the history graph: one transition fixes a
specific next history state, not merely a next physical fragment.

## 5. Exact cut obstruction

For every nonempty proper \({\cal A}\subset{\cal P}\), a selected cycle must
use at least one arc leaving and one arc entering \(\Sigma({\cal A})\).
Consequently a fibre set with no accepted crossing is fatal unless the
protected arcs supply crossings in both directions.  One protected crossing
is not enough.

In the unaugmented two-path form, a sealed physical class \(W\) must obey

\[
 |W\cap\{r_1,r_2\}|=|W\cap\{s_1,s_2\}|.              \tag{5.1}
\]

This is a post-transversal obstruction.  It must not be combined with the
pre-transversal degree
\[
                         q_d=(m-d)(m-d-1)
\]
of the complete coherent-history state graph: selecting one state per
physical fragment need not preserve degree \(q_d\).

## 6. An internal state-path calibration and its boundary

At \(m=3,d=1\), let

\[
 \Omega=\{s,b,a,z,c\},\qquad
 D=sbc,\ C=szc,\ B=sac,\ A=saz.
\]

The two paths

\[
\begin{aligned}
 Q_1:\;&sbc\to sba\to baz\to azc\to szc,\\
 Q_2:\;&sac\to bac\to bzc\to sbz\to saz              \tag{6.1}
\end{aligned}
\]

contain every rank-three owner once.  Their transition labels are

\[
       ca,sz,bc,as\qquad\hbox{and}\qquad sb,az,cs,ba,
\]

and successive labels are disjoint, which is exactly depth-one history
compatibility.  A literal state lift is

\[
\begin{aligned}
 &(sbc;b,z),(sba;a,c),(baz;z,s),(azc;c,b),(szc;s,a),\\
 &(sac;a,z),(bac;b,s),(bzc;z,a),(sbz;s,c),(saz;a,b).
                                                               \tag{6.2}
\end{aligned}
\]

This is only an **internal** two-path state certificate.  It does not assert
the protected boundary arcs, palettes, upper tickets, or charge rows.  In
fact it is not compatible with the prescribed \(g_1:C\to B\) boundary:
the last \(Q_1\) label is \(\{a,s\}\), while the \(g_1\) label is
\(\{z,a\}\), so the two labels collide at \(a\).  Exact enumeration gives
zero covers for these four endpoints when that boundary history is imposed.

The endpoint dependence is real even before protected boundary histories are
imposed.  Of the \(10P4=5040\) ordered quadruples of distinct owner endpoints,
exactly \(2520\) admit an internal depth-one two-path cover and \(2520\) do
not.  One failure is

\[
                  012\leadsto013,\qquad014\leadsto023.           \tag{6.3}
\]

Therefore vertex transitivity and regular local degree do not imply
arbitrary two-linkedness.

There is also a conditional design-theoretic source of resident cycle
factors.  If

\[
 R_i=\{v_i,v_{i+1},\ldots,v_{i+m-2}\}
       \qquad(i\in{\mathbb Z}_{2m-1}),
\]

is a tight Hamilton cycle in the complete \((m-1)\)-uniform hypergraph on
\(2m-1\) coordinates, with
\((v_0,\ldots,v_{2m-2})\) a permutation of \(\Omega\), then the complementary
owners
\(T_i=\Omega\setminus R_i\) have transition labels
\(\{v_i,v_{i+m-1}\}\).  Labels at cyclic distance at most \(m-2\) are
disjoint.  Hence the \(T_i\) form a depth-\((m-2)\) coherent owner cycle.
A tight-cycle decomposition would give a resident owner-cycle factor, but
for \(m>3\) it still has many components and needs safe merging.

## 7. Boolean pull-tree contraction

The preceding observation motivates a Boolean-specific route which is weaker
than generic robust expansion.

Let \({\cal C}\) be a globally ledger-feasible, state-labelled cycle factor
which selects one state from every physical fibre and contains the two marked
contractions.  Let its components be \(C_1,\ldots,C_t\).

A candidate Boolean pull is called safe when:

1. its old phase consists of factor edges and its new phase consists of
   accepted literal arcs;
2. the selected state transversal is fixed and every new arc is accepted
   between those fixed states; if a pull changes states instead, it includes
   a complete jointly compatible relabelling of every incident selected arc;
3. every new transition passes the literal history relation, and its complete
   signed additive resource, palette, capacity, deep-ticket and charge
   increment is zero;
4. it avoids both marked contractions and their cumulative ledgers; and
5. if its old phase meets two distinct cycles at the certified execution
   prefix, its new phase merges those cycles and creates no third component.

The pull auxiliary multigraph \({\cal A}\) has vertices
\(C_1,\ldots,C_t\) and one edge for each safe binary merger, joining the two
factor components which it merges.

A pull-labelled spanning tree is **rooted tree-coherent** if it has a root
and a parent-before-child execution order with the following property.  When
the pull to a fresh child is executed, its retained ports still occur in the
current parent aggregate and the untouched child, its exact local port test
gives a two-to-one merger, every new transition is accepted, and all later
pulls remain available.  For a \(2+1\) Boolean \(C_6\), a proof-safe
certificate cuts once in the current parent aggregate and twice in the fresh
child and verifies the exact alpha/beta port pairing.  Guarded mutable
supports are disjoint, and no edge added by an earlier pull is removed by a
later pull, unless an explicit higher-order commutation identity certifies
the interaction.

### Theorem 7.1 (compatible spanning pull tree)

If the pull auxiliary multigraph contains a rooted tree-coherent spanning
tree, then applying its \(t-1\) pulls in the certified parent-before-child
order produces one partition-Hamilton cycle.  It preserves the complete
ledger and both marked contractions.

#### Proof

Use the certified order.  Before each pull, its fresh child has not been
touched and its parent belongs to the already merged ancestor aggregate.
The local port test therefore reduces the component count by one.
Tree coherence preserves every later pull.  After \(t-1\) steps there is one
cycle, while state exactness, transition histories and every zero-increment
additive row have been preserved. \(\square\)

### Corollary 7.2 (protected deletion criterion)

Let \({\cal B}\) be the protected bank.  For a nontrivial component set
\(S\subset[t]\), let \(\ell_\rho(S)\) be the number of auxiliary cut edges
killed by protected resource \(\rho\).  If

\[
 |\delta_{\cal A}(S)|
   >\sum_{\rho\in{\cal B}}\ell_\rho(S)
       \qquad(\varnothing\ne S\subsetneq[t]),          \tag{7.1}
\]

then the surviving pull auxiliary graph is connected.  If, in addition, its
surviving edges admit a rooted tree-coherent spanning tree, Theorem 7.1
closes the topology row.

In particular, if the unfiltered auxiliary graph is \(\lambda\)-edge
connected, \(|{\cal B}|\le b\), and every protected resource kills at most
\(L\) auxiliary edges, then

\[
                             \lambda>bL               \tag{7.2}
\]

guarantees connectivity after the bank is imposed.

#### Proof

For each cut, the right side of (7.1) is an upper bound on all deleted
crossing edges.  Hence every nontrivial cut retains an edge.  This is
equivalent to connectivity.  Inequality (7.2) implies (7.1) uniformly.
\(\square\)

For the rooted parent-before-child formulation, orient an auxiliary candidate
from its intended parent component to its fresh child.  A surviving
\(C_1\)-out-arborescence exists exactly when

\[
 \delta^-_{\cal A}(S)\ne\varnothing
       \qquad(\varnothing\ne S\subseteq[t]\setminus\{1\}).       \tag{7.3}
\]

Indeed, (7.3) is equivalent to reachability of every component from \(C_1\),
and a search tree is then an out-arborescence.  If every rooted in-cut has
size at least \(\lambda_1\), a bank of at most \(b\) resources of per-resource
cut load at most \(L\) preserves (7.3) whenever
\(\lambda_1>bL\).  The arc labels must still be rooted tree-coherent; the
cut condition proves only the component-level arborescence.

The scalar bound is sharp from \((\lambda,b,L)\) alone.  Take two internally
dense component blobs joined by exactly \(bL\) pull candidates, partitioned
into \(b\) protected resource classes of \(L\) candidates.  Protecting those
classes deletes the whole cut.  Total pull abundance inside the two blobs is
irrelevant.  Moreover, even a connected three-vertex auxiliary path can fail
execution if its two pull labels use the same old port, or both consume one
common slack-one token.  In the first example each pull can be exact-safe
individually but no joint spanning tree is executable; in the second each is
only individually feasible before the common capacity is charged.

Connectivity alone does not imply support compatibility: arbitrary
multi-resource conflicts are not a matroid.  A proof using (7.1) must
therefore supply either a private-support pull atlas, a compatible spanning
tree directly, or a separate common-base theorem.  This is the exact missing
Boolean supply row.

There is an exact min--max statement when the compatibility system is
matroidal.  Let \(M_{\rm gr}\) be the graphic matroid of the auxiliary
component multigraph and let \(M_{\rm safe}\) be a matroid on the same pull
catalogue whose independent sets are simultaneously executable pulls.  The
latter hypothesis holds, for example, for a private-ticket atlas in which
the only conflicts are partition classes and at most one pull may be chosen
from each class, provided the atlas also has the rooted tree-coherence closure:
every common independent forest admits the certified parent-before-child
execution above.

### Theorem 7.3 (graphic/safe common-base criterion)

After deleting every pull forbidden by the protected bank, a compatible
spanning pull tree exists if and only if

\[
 r_{\rm gr}(X)+r_{\rm safe}(E'\setminus X)\ge t-1
                         \qquad(X\subseteq E'),       \tag{7.4}
\]

where \(E'\) is the surviving catalogue.  Under (7.4) and the stated
tree-coherence closure, Theorem 7.1 produces
the required partition-Hamilton cycle.

#### Proof

The matroid-intersection min--max theorem says that the maximum size of a set
independent in both matroids is

\[
 \min_{X\subseteq E'}
       \bigl(r_{\rm gr}(X)+r_{\rm safe}(E'\setminus X)\bigr).
\]

It reaches \(t-1\) exactly under (7.4).  A graphic-independent set of
\(t-1\) edges on \(t\) component vertices is a spanning tree, while
\(M_{\rm safe}\)-independence is simultaneous executability. \(\square\)

The matroid and execution hypotheses are load-bearing.  Here
\(M_{\rm safe}\) is permitted only when every common independent forest is
rooted tree-coherent in the sense above; abstract pairwise compatibility is
not enough for a \(2+1\) pull.  A pull can use several independent
capacity-one resources, and the resulting multi-resource conflict system
need not be a matroid.  In that generality (7.4) is not available without an
extended private-ticket representation or a stronger packing theorem.

The canonical gluing tree alone is not protected-bank robust.  If the
auxiliary catalogue is itself a tree, every edge is a one-edge cut; forbidding
one resource unique to one pull disconnects it.  Hence survival of
\(O(d)\) protected deletions requires genuine alternate pulls across every
relevant component cut, quantitatively as in (7.1), rather than only the
existence of one unfiltered Mütze gluing tree.

## 8. Conclusion

The root contraction theorem is correct at SHA \(7231f74b\ldots\), with the
state-fibre and cumulative-ledger interpretation made explicit above.  The
exact target is not an ordinary Hamilton cycle on all accepted state copies.
It is the partition-Hamilton master (3.1).

There are now two rigorous positive interfaces:

1. a state transversal whose contracted simple digraph meets (4.2); or
2. a globally compatible cycle factor with a protected compatible spanning
   pull tree as in Section 7.

The first is too dense for the raw history graph.  The second is the natural
Mütze-style Boolean route, but its all-dimensional safe-pull supply is open.
The decisive theorem still needed is a state/resource-safe pull atlas whose
auxiliary cut size dominates the \(O(d)\) protected deletion load and whose
surviving edges contain a support-compatible spanning tree.  Deeper
upper/source/compiler/regeneration rows remain separate unless included in
the pull ledger.
