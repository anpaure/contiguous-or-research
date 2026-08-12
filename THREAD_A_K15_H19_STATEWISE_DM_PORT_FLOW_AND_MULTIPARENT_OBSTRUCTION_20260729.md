# Thread A: the Hall-19 statewise DM port-flow theorem and the nineteen-cell obstruction

Date: 2026-07-29

Status: proved full-graph Dulmage--Mendelsohn cut identity, proved exact
alternating-flow completion theorem, and proved a sharp statewise obstruction
for the authoritative Hall-19 carrier.  No Hall-zero compound exchange is
constructed.  The obstruction identifies the minimum service signature of
the next move family.

## 0. Outcome

Let

\[
 {\cal T}=\{S\subseteq[15]:1\le |S|\le7\},
 \qquad |{\cal T}|=16383,
\tag{0.1}
\]

and let \(G_0=({\cal T},{\cal C};E_0)\) be the **full** lower-compiler graph
of the frozen carrier

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

with all \(19311\) depth-zero, depth-one, and depth-two physical cells.
Its SHA-256 is

```text
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

The audited matching number is \(16364\).  Its canonical positive
Dulmage--Mendelsohn shore has sizes

\[
 |X|/|Y|=516/497,
\tag{0.2}
\]

and decomposes into seventeen gap-one components and one gap-two component.
Six gap-one components are isolated zero-target components.  The other
twelve components carry thirteen deficit units.  In this note the phrase
**thirteen congestion units** always means these thirteen nonzero-component
deficit units.  It does not mean the coincidental thirteen changed compiler
cell shores of the earlier neutral H20 braid.

This note proves the following.

1. There is a maximum matching \(M_*\) which exposes exactly the nineteen
   native roots in the audited component table.
2. For every union \(X_J\) of old DM components and every proposed final
   graph \(G_1\), the remaining Hall gap on \(X_J\) is exactly

   \[
      g(J)-\Phi_{G_1}(J),
   \tag{0.3}
   \]

   where \(g(J)\) is the old component gap and \(\Phi\) is net new boundary
   capacity, with lost old neighbours subtracted.
3. Consequently, merely creating candidates for the six zeros cannot close
   Hall.  The twelve nontrivial components retain the \(510/497\) cut unless
   they receive net boundary gain at least thirteen.  Any Hall-zero final
   state has at least nineteen distinct new \(X\)-neighbour compiler-cell
   addresses.  This does not yet make them free or independently usable.
4. A compound multi-parent exchange is sufficient if its final physical
   state is Johnson, depth-three resident, and upper-complete, and its exact
   full compiler graph contains a protected value-nineteen alternating flow
   relative to \(M_*\).  This is a literal \(16383\)-target theorem, not a
   partial-shore audit.

Thus, for a **one-shot Hall-perfect** search, a proof-safe proposed
architecture is a service-first compound exchange whose final graph
simultaneously has a rank-six zero SDR, \(\Phi_{G_1}(J_+)\ge13\),
\(\Phi_{G_1}([18])\ge19\), and one value-nineteen vertex-capacitated
alternating-flow certificate.  The zero and positive service cells need not
be disjoint, and the cut counts do not by themselves make a cell usable.
An iterative Hall-\(19\to18\) step needs only one genuine augmenting unit,
but it must be certified in the full graph.

Here \([18]\) indexes all old DM components and \(J_+\) indexes the twelve
nontrivial ones; the notation is defined formally in Sections 3 and 6.

## 1. The frozen physical and compiler state

Write the frozen rank-eight path as

\[
 T^0=(T^0_0,\ldots,T^0_{W-1}),
 \qquad W=\binom{15}{8}=6435.
\tag{1.1}
\]

It is a permutation of all rank-eight sets, every consecutive pair differs
by one Johnson swap, every interior coordinate run has length at least four,
and every upper consecutive-union layer \(q=1,\ldots,7\) has complete
support.

For any candidate path \(T\), its depth-three maximal erosion is

\[
 P_p(T)=
 \bigcap_{i=\max(0,p-3)}^{\min(W-1,p)}T_i,
 \qquad 0\le p<W+3.
\tag{1.2}
\]

A compiler cell is \(c=(s,h)\), where \(h\in\{0,1,2\}\) and

\[
 I_c=\{s,s+1,\ldots,s+h\}.
\tag{1.3}
\]

There are

\[
 (W+3)+(W+2)+(W+1)=19311
\tag{1.4}
\]

such cells.  Put

\[
 E_c(T)=\bigcup_{p\in I_c}P_p(T).
\tag{1.5}
\]

For a coordinate occurrence \(x\in T_i\), its erosion carrier is

\[
 K_T(i,x)=
 \{p\in\{i,i+1,i+2,i+3\}:x\in P_p(T)\}.
\tag{1.6}
\]

Let \(Q_c(T)\) be the union of the coordinates \(x\) for which some
occurrence has

\[
 \varnothing\ne K_T(i,x)\subseteq I_c.
\tag{1.7}
\]

The exact target--cell incidence is

\[
 S\sim_T c
 \iff
 Q_c(T)\subseteq S\subseteq E_c(T)
 \quad\hbox{and}\quad
 S\cap P_p(T)\ne\varnothing\ \ (p\in I_c).
\tag{1.8}
\]

Thus every graph below is built from the same complete physical catalogue
and (1.8), including clipped endpoint cells.  No pair-face catalogue,
partial target list, or endpoint scalar bound is used.

The authoritative full audit gives

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
|{\cal T}|&16383\\
|{\cal C}|&19311\\
\nu(G_0)&16364\\
|X|/|Y|&516/497\\
\text{component gaps}&1^{17},2^1.
\end{array}
\tag{1.9}
\]

The six isolated zero targets are

\[
 Z=\{5801,13616,13620,17738,21641,29776\}.
\tag{1.10}
\]

Their ranks are respectively

\[
 7,6,7,6,6,6.
\tag{1.11}
\]

In particular, they are not six rank-six targets.

The thirteen exposed units in nontrivial components are

\[
\begin{split}
 \Omega_+=\{&
 960,1103,2420,2575,2676,4213,7504,\\
 &8217,8218,9524,17683,18970,19568\}.
\end{split}
\tag{1.12}
\]

The pair \(8217,8218\) belongs to the single \(321/319\) component whose
Boolean intersection is \(8216\); \(8216\) is not itself a target of that
component.  The remaining component types are

\[
161/160,\quad 2(5/4),\quad2(3/2),\quad6(2/1).
\tag{1.13}
\]

Put

\[
 \Omega=Z\sqcup\Omega_+,
 \qquad |\Omega|=19.
\tag{1.14}
\]

The set \(\Omega\) is the exposed-root set of the audited native component
bases.  It need not equal the unmatched target list returned by an arbitrary
deterministic maximum-matching implementation.

## 2. A maximum matching exposing the physical roots

For every DM component \(C_i=(X_i,Y_i)\), the frozen maximal controller
gives distinct physical native pins whose target set is

\[
 X_i\setminus\Omega_i,
 \qquad |\Omega_i|=|X_i|-|Y_i|.
\tag{2.1}
\]

Across the eighteen components these pins use all \(497\) cells of \(Y\)
once and have \(497\) distinct targets.

### Lemma 2.1 (root-exposing maximum matching)

There is a maximum matching \(M_*\) of \(G_0\) such that

\[
 V_{\cal T}(M_*)={\cal T}\setminus\Omega.
\tag{2.2}
\]

It consists of the \(497\) audited native component pins and a matching of
all \(15867\) targets outside \(X\) to cells outside \(Y\).

#### Proof

Take a maximum matching used to form the canonical alternating DM shore.
Every reached right vertex is matched, its mate is reached, and no edge
leaves \(X\) for a cell outside \(Y=N_{G_0}(X)\).  Hence the restriction of
that matching outside \(X\cup Y\) saturates all

\[
 |{\cal T}\setminus X|=16383-516=15867
\]

outside targets using cells outside \(Y\).

Inside every component replace the old matching by its audited native
matching (2.1).  This uses exactly the same right shore \(Y_i\), matches
every target except \(\Omega_i\), and is disjoint from the exterior
restriction.  Their union has size

\[
 15867+497=16364
\]

and exposes exactly \(\Omega\).  Since \(\nu(G_0)=16364\), it is maximum.
\(\square\)

Lemma 2.1 is an incidence statement.  The existing audits do not give one
common source word realizing the \(15867\)-edge exterior matching together
with all \(497\) native pins.

## 3. Exact DM component-union port algebra

Let the eighteen old components be \(C_i=(X_i,Y_i)\), with

\[
 g_i=|X_i|-|Y_i|.
\tag{3.1}
\]

For \(J\subseteq[18]\), write

\[
 X_J=\bigcup_{i\in J}X_i,\qquad
 Y_J=\bigcup_{i\in J}Y_i,\qquad
 g(J)=\sum_{i\in J}g_i.
\tag{3.2}
\]

Different components have no cross edge in \(G_0[X\cup Y]\), and no edge
from \(X\) leaves \(Y\).  Therefore

\[
 N_{G_0}(X_J)=Y_J.
\tag{3.3}
\]

For an arbitrary proposed final graph \(G_1\) on the same target and
physical-cell address sets, define its external gain, old-neighbour loss,
and net port gain by

\[
\begin{split}
 a_{G_1}(J)&=
 |N_{G_1}(X_J)\setminus Y_J|,\\
 \ell_{G_1}(J)&=
 |Y_J\setminus N_{G_1}(X_J)|,\\
 \Phi_{G_1}(J)&=a_{G_1}(J)-\ell_{G_1}(J).
\end{split}
\tag{3.4}
\]

### Theorem 3.1 (exact component-union gap identity)

For every \(J\subseteq[18]\),

\[
 \boxed{
 |X_J|-|N_{G_1}(X_J)|
 =
 g(J)-\Phi_{G_1}(J).}
\tag{3.5}
\]

Consequently

\[
 \operatorname{def}(G_1)
 \ge
 \max_{J\subseteq[18]}
 \bigl(g(J)-\Phi_{G_1}(J)\bigr),
\tag{3.6}
\]

where \(\operatorname{def}(G_1)=|{\cal T}|-\nu(G_1)\).  In particular, a
Hall-perfect \(G_1\) must satisfy

\[
 \Phi_{G_1}(J)\ge g(J)
 \qquad(J\subseteq[18]).
\tag{3.7}
\]

#### Proof

The two parts of \(N_{G_1}(X_J)\), inside and outside \(Y_J\), are disjoint.
Thus

\[
 |N_{G_1}(X_J)|
 =
 |Y_J|-\ell_{G_1}(J)+a_{G_1}(J).
\]

Since \(|X_J|=|Y_J|+g(J)\), subtraction gives (3.5).  Hall's deficiency
formula

\[
 |{\cal T}|-\nu(G_1)
 =
 \max_{A\subseteq{\cal T}}(|A|-|N_{G_1}(A)|)
\]

then gives (3.6), and a perfect matching forces every displayed gap to be
nonpositive.  \(\square\)

Theorem 3.1 is exact even when an exchange deletes old incidences, migrates
components, or joins several old components.  Joining two components only
through cells of their old union does not increase \(\Phi\) for that union.

### Corollary 3.2 (the six-zero and thirteen-congestion cuts)

Let \(X_Z=Z\), and let

\[
 X_+=X\setminus Z.
\tag{3.8}
\]

Then

\[
 |X_Z|/|N_{G_0}(X_Z)|=6/0,
 \qquad
 |X_+|/|N_{G_0}(X_+)|=510/497.
\tag{3.9}
\]

Every Hall-perfect \(G_1\) therefore satisfies, for every \(Z'\subseteq Z\),

\[
 \boxed{
 |N_{G_1}(Z')|\ge|Z'|
 \quad\text{for every }Z'\subseteq Z,}
\tag{3.10}
\]

and

\[
 |N_{G_1}(X_+)\setminus Y|
 -
 |Y\setminus N_{G_1}(X_+)|
 \ge13.
\tag{3.11}
\]

For the whole old DM shore it satisfies

\[
 |N_{G_1}(X)\setminus Y|
 -
 |Y\setminus N_{G_1}(X)|
 \ge19.
\tag{3.12}
\]

#### Proof

Apply Theorem 3.1 to every subunion of the six isolated components to obtain
(3.10).  Apply it separately to the union of the twelve nontrivial
components and to the union of all eighteen components.  The latter two gaps
are \(13\) and \(19\).  \(\square\)

The quantified family (3.10) is precisely Hall's condition
for the six zero candidate lists and therefore gives matching rank six.
The single inequality \(|N(Z)|\ge6\), or positive degree of each zero, would
not suffice.  Equation (3.11) is the exact thirteen-congestion condition.
It survives arbitrary internal compression or fusion of the twelve
components.

### Corollary 3.3 (nineteen changed-cell tax)

If \(G_1\) is Hall-perfect, at least nineteen distinct physical cell
addresses acquire a neighbour in \(X\) which they did not have in \(G_0\).
At least thirteen distinct addresses outside the old right shore \(Y\)
are adjacent to \(X_+\), before adding compensation for any lost member of
\(Y\).

#### Proof

By (3.3), every member of \(N_{G_1}(X)\setminus Y\) is a cell whose
incidence with \(X\) is new.  Equation (3.12) gives

\[
 |N_{G_1}(X)\setminus Y|
 \ge19+|Y\setminus N_{G_1}(X)|
 \ge19.
\]

The same argument with (3.11) gives the second assertion.  \(\square\)

This is a lower bound on changed **compiler-cell incidences**, not on the
number of changed successor arcs or middle positions.  Several service
cells can have overlapping dependency windows.

### Theorem 3.4 (contracted port-rank form of the thirteen units)

Assume that \(G_1\) retains the audited native matching of \(Y\) onto
\(X\setminus\Omega\).  On the right-cell subsets of \(G_1[X,{\cal C}]\), let

\[
 \rho(S)=\nu\bigl(G_1[X,S]\bigr).
\tag{3.13}
\]

For \(P\subseteq{\cal C}\setminus Y\), put

\[
 r(P)=\rho(Y\cup P)-497.
\tag{3.14}
\]

Then \(r\) is the rank function of the transversal matroid contracted by
the independent set \(Y\).  In particular it is normalized, monotone, and
submodular, and

\[
 0\le r(P)\le\min\{|P|,19\}.
\tag{3.15}
\]

The old shore \(X\) is saturable using cells in \(Y\cup P\) if and only if

\[
 r(P)=19.
\tag{3.16}
\]

If six distinct external cells \(P_Z\) directly serve the six distinct
targets in \(Z\), while the native matching on \(Y\) is retained, then

\[
 r(P_Z)=6.
\tag{3.17}
\]

For any further port set \(P_+\), the exact remaining condition is

\[
 \boxed{
 r(P_Z\cup P_+)-r(P_Z)=13.}
\tag{3.18}
\]

#### Proof

The matchable right-cell sets of a bipartite graph form a transversal
matroid, with rank \(\rho\).  The native matching proves
\(\rho(Y)=|Y|=497\), so (3.14) is exactly the contraction rank by \(Y\).
The standard rank axioms give (3.15).  Since \(|X|=516\), saturation is
equivalent to

\[
 \rho(Y\cup P)=516=497+19,
\]

which is (3.16).  The native matching together with the six distinct zero
ears has size \(503\), so \(r(P_Z)\ge6\); the bound
\(r(P_Z)\le|P_Z|=6\) gives equality.  Finally (3.16)--(3.17) give (3.18).
\(\square\)

Thus thirteen marginal target hits are not enough.  The additional ports
must have contracted transversal rank thirteen after the six zero ears have
already consumed their cells.

## 4. Exact alternating-component completion

Fix the root-exposing maximum matching \(M_*\) from Lemma 2.1 and let

\[
 F={\cal C}\setminus V_{\cal C}(M_*)
\tag{4.1}
\]

be its free physical cells.  Thus

\[
 |F|=19311-16364=2947.
\tag{4.2}
\]

For a proposed final graph \(G_1\), orient every nonmatching edge
\(t c\in E(G_1)\setminus M_*\) from \(t\in{\cal T}\) to \(c\in{\cal C}\),
and every matching edge \(tc\in M_*\) from \(c\) to \(t\).  Vertex capacities
are one.

### Theorem 4.1 (protected nineteen-flow completion)

Assume \(M_*\subseteq E(G_1)\).  Let \(\lambda(G_1;M_*)\) be the maximum
number of pairwise vertex-disjoint directed paths in the above alternating
network, starting at distinct vertices of \(\Omega\) and ending in distinct
vertices of \(F\).  Then

\[
 \boxed{\nu(G_1)=16364+\lambda(G_1;M_*).}
\tag{4.3}
\]

In particular,

\[
 G_1\text{ is Hall-perfect}
 \iff
 \lambda(G_1;M_*)=19.
\tag{4.4}
\]

#### Proof

Flipping \(M_*\) along any vertex-disjoint family of \(\lambda\) alternating
paths gives a matching of size \(16364+\lambda\).

Conversely, let \(M_1\) be any matching in \(G_1\).  The symmetric difference
\(M_*\triangle M_1\) is a disjoint union of alternating cycles and paths.
Every component on which \(M_1\) has one more edge than \(M_*\) is an
\(M_*\)-augmenting path from an \(M_*\)-unmatched target in \(\Omega\) to an
\(M_*\)-free cell in \(F\).  These components are vertex-disjoint, and their
number is at least \(|M_1|-|M_*|\); components favouring \(M_*\) can only
increase the number needed to achieve that net difference.  Hence

\[
 |M_1|-16364\le\lambda(G_1;M_*).
\]

Maximizing over \(M_1\) proves (4.3).  Since \(|\Omega|=19\), (4.4) follows.
\(\square\)

The value \(\lambda\) is one ordinary integral vertex-capacitated max flow
after splitting every vertex.  It is not a relaxation.

For an incremental protected descent, (4.3) also gives the exact identity

\[
 \operatorname{def}(G_1)=19-\lambda(G_1;M_*).
\tag{4.4a}
\]

Thus one augmenting path proves Hall at most eighteen; an arbitrary thirteen
disjoint paths prove total deficiency at most six; and nineteen prove Hall
zero.  The thirteen nontrivial units are discharged specifically by paths
starting at every vertex of \(\Omega_+\).  Requiring all six old zero targets
merely to acquire candidates is a separate positive-degree condition.
Requiring them to be simultaneously serviceable is the stronger SDR
condition (3.10).

### Corollary 4.2 (direct nineteen-port macro)

Assume \(M_*\subseteq E(G_1)\).  If the bipartite graph induced by
\(\Omega\) and \(F\) contains a matching of size nineteen, then \(G_1\) is
Hall-perfect.

#### Proof

The nineteen matched edges are length-one paths in Theorem 4.1.
\(\square\)

No root in \(\Omega\) is adjacent in \(G_0\) to an \(M_*\)-free cell:
otherwise \(M_*\) would have an augmenting edge.  Hence all nineteen direct
ports in Corollary 4.2 would be genuinely new incidences.

### Theorem 4.3 (general statewise alternating-circuit certificate)

The preservation hypothesis \(M_*\subseteq E(G_1)\) can be removed as
follows.  There is a perfect matching of \(G_1\) if and only if there exists
a vertex-disjoint family \({\cal K}\) of \(M_*\)-alternating components in
the union \(M_*\cup E(G_1)\) such that:

1. exactly nineteen members are augmenting paths, one starting at each
   \(\rho\in\Omega\) and ending at a distinct cell of \(F\);
2. every non-\(M_*\) edge of every member belongs to \(E(G_1)\);
3. every edge of \(M_*\setminus E(G_1)\) belongs to a member of
   \({\cal K}\); and
4. every other member is an alternating cycle or an alternating path whose
   two endpoints lie on the right shore and which contains equally many
   \(M_*\)-edges and non-\(M_*\)-edges.

Flipping \(M_*\) on all members of \({\cal K}\) gives the perfect matching.

#### Proof

Under conditions 1--4, every vertex has matching degree at most one after
the flip, all retained or inserted edges belong to \(G_1\), and the nineteen
augmenting paths raise the size from \(16364\) to \(16383\).

Conversely, for a perfect matching \(M_1\subseteq E(G_1)\), take the complete
symmetric-difference decomposition \(M_*\triangle M_1\).  Because \(M_1\)
saturates every target and \(M_*\) exposes exactly \(\Omega\), precisely one
augmenting component begins at each member of \(\Omega\).  All deleted
\(M_*\)-edges occur in the decomposition, and the remaining components are
alternating cycles or right-to-right size-neutral paths.  This is the
required family.
\(\square\)

Theorem 4.3 is the exact alternating-component algebra for a compound
exchange which also reroutes the old matching.  The protected version,
Theorem 4.1, is the useful positive-search specialization.

### Corollary 4.4 (new-edge tax on augmenting components)

If \(G_1\) is Hall-perfect, each of the nineteen augmenting components in
Theorem 4.3 contains an edge of

\[
 E(G_1)\setminus E(G_0).
\tag{4.5}
\]

The six paths starting in \(Z\) begin with such an edge; the other thirteen
paths start in the nontrivial DM components.

#### Proof

If one augmenting component used only edges of \(G_0\) besides its
\(M_*\)-edges, it would be an augmenting path for \(M_*\) in \(G_0\),
contradicting maximality of \(M_*\).  A zero target has no old incident edge,
so its first edge is new.  \(\square\)

### Corollary 4.5 (one path removes one unit)

An \(M_*\)-augmenting path contains exactly one member of \(\Omega\), namely
its initial vertex, and flipping it raises the matching size by exactly one.
Therefore discharging the thirteen congestion units requires one path
starting at each vertex of \(\Omega_+\), either as thirteen disjoint paths in
one simultaneous certificate or as thirteen sequential augmentations with
the matching recomputed after each step.  They cannot be discharged by one
path which passes serially through all thirteen roots.

#### Proof

Every member of \(\Omega\) is unmatched by \(M_*\), so it has no incoming
matched edge and cannot be an internal vertex of an \(M_*\)-alternating
path.  An augmenting path has one more nonmatching edge than matching edge,
and flipping it increases cardinality by one.  \(\square\)

## 5. The statewise compound multi-parent theorem

Close a rank-eight Hamilton path through a dummy endpoint solely to encode
successor indegree and outdegree.  A **parent-assembled successor state**
chooses directed successor arcs from one or more labelled parent paths and
is accepted only when its final successor permutation is one dummy-rooted
cycle.  The dummy is then deleted; it participates in no Johnson, residence,
shadow, erosion, or compiler test.  We call any such final state a
statewise compound multi-parent exchange.  No independent legality is
assumed for the individual circuit factors used to assemble it.  The
following theorem depends only on this final state, not on a face-local
producer catalogue.

### Theorem 5.1 (statewise Shadow--DM macro)

Let \(T^1\) be the final state of a compound multi-parent exchange from
\(T^0\).  Suppose:

1. **deck and Johnson:** \(T^1\) is a permutation of all \(6435\) rank-eight
   sets and

   \[
      |T^1_i\triangle T^1_{i+1}|=2
      \qquad(0\le i<W-1);
   \tag{5.1}
   \]
2. **depth-three residence:** every coordinate run strictly between the two
   path endpoints has length at least four;
3. **upper support:** for every \(1\le q\le7\),

   \[
   \left\{
      \bigcup_{j=0}^{q}T^1_{i+j}:
      0\le i<W-q,\quad
      \left|\bigcup_{j=0}^{q}T^1_{i+j}\right|=8+q
   \right\}
   =
   \binom{[15]}{8+q};
   \tag{5.2}
   \]
4. **full physical catalogue:** \(G_1=G(T^1)\) is built from all \(19311\)
   cells by (1.2)--(1.8), including both endpoint collars; and
5. **alternating completion:** either the protected value-nineteen condition
   of Theorem 4.1 holds, or a general certificate from Theorem 4.3 is
   supplied.

Then \(T^1\) is a deck-exact, Johnson, depth-three-resident,
all-upper-complete carrier whose **full \(16383\)-target compiler graph** has
a matching of size \(16383\).

#### Proof

Conditions 1--3 are exactly the stated physical carrier properties.
Condition 4 identifies the graph being certified with the actual full
compiler graph of that same state.  Theorem 4.1 or 4.3 supplies a perfect
matching in that graph.  No conclusion is imported from a partial shore or
from another parent catalogue.  \(\square\)

Theorem 5.1 is deliberately a carrier theorem.  A perfect incidence matching
does not by itself prove that all \(16383\) selected pins are realized by
one common nonempty source word; that simultaneous common-\(Q\) lift remains
a separate gate.

## 6. The rigorous obstruction and the next move family

### Theorem 6.1 (zero-only repair cannot close H19)

Let \(J_+\) denote the index set of the twelve nontrivial components, so
\(X_{J_+}=X_+\) and \(Y_{J_+}=Y\).  Suppose a proposed exchange changes the
six zero neighbourhoods but leaves

\[
 N_{G_1}(X_+)=Y.
\tag{6.1}
\]

Then

\[
 \operatorname{def}(G_1)\ge13,
\tag{6.2}
\]

regardless of how the six zero targets are repaired.

More generally,

\[
 \operatorname{def}(G_1)
 \ge
 13-\Phi_{G_1}(J_+).
\tag{6.3}
\]

#### Proof

Equation (6.1) gives \(\Phi_{G_1}(J_+)=0\).  Apply (3.6) to the union of the
twelve nontrivial components.  The general form is the same application
without setting \(\Phi\) to zero.  \(\square\)

Thus the six zeros and the thirteen positive units are not sequentially
independent chores.  A zero port may enter an old positive-component cell
and displace its matched target, but then the alternating flow must carry
that displacement through the positive congestion and out to genuinely
free capacity.

### Proposition 6.2 (the audited root-2420 ear is only a partial-shore gain)

The previously audited controller rotation

\[
 (2416,18768,2388)\longmapsto(18768,2416,2388)
\tag{6.4}
\]

creates the depth-one root-\(2420\) cell

\[
 c_*=10221
\tag{6.5}
\]

and has

\[
 N(X)=Y\mathbin{\dot\cup}\{c_*\}.
\tag{6.6}
\]

It is resident and retains complete upper support.  Hence the restricted old
shore has gap \(516-498=18\).  Nevertheless this near-state omits middle
states

\[
 \{11122,19804\},
\tag{6.7}
\]

duplicates

\[
 \{27474,3452\},
\tag{6.8}
\]

and leaves exterior matching rank only \(15865\), two below \(15867\).
Its complete compiler matching rank is \(16363\), not \(16365\).

#### Proof

These are the exact fixed-certificate conclusions of
`THREAD_H_H19_ROOT_EAR_REBASE_AND_TWO_FOR_TWO_DECK_GATE_20260728.md`,
Theorem 5.1 and equations (5.4)--(5.10).  Equation (6.6) certifies only the
old \(516\)-target shore.  The omitted/duplicated deck states change the
exterior physical cell system, whose independently computed rank loses two.
\(\square\)

Proposition 6.2 is the concrete warning behind condition 4 of Theorem 5.1:
even an exact \(+1\) net DM portal, Johnson chronology, residence, and
upper-support preservation do not imply a gain in the full target graph.
Any surviving version of that ear must at minimum repair the two omitted
deck states, remove the two duplicate supplies, and restore both exterior
rank losses before it can be used as one of the thirteen positive service
units.  A literal two-for-two companion is one local-lane normal form, not a
global necessity.

### Proof-safe candidate-generation rule

A future compound exchange should be generated and filtered in this order.

1. Select six zero service incidences whose six target lists already have
   matching rank six.
2. Supply at least thirteen net external units for \(X_+\), plus one
   additional address for every lost old neighbour.  The gap-two component
   needs net gain two and every other nontrivial component needs net gain one;
   a port may enter a different old component, but it must then be carried by
   the eventual alternating flow and all component-union cuts still apply.
3. Enforce the complete component-union inequalities

   \[
      \Phi_{G_1}(J)\ge g(J)
      \qquad(J\subseteq[18])
   \tag{6.9}
   \]

   as safe early cuts.  These are necessary, not claimed sufficient.
4. Compute the exact value-nineteen alternating flow or the general
   alternating-component certificate of Section 4.
5. Only on that same final state, audit (5.1), residence, (5.2), and the full
   endpoint-conditioned \(19311\)-cell graph.

The cells counted in steps 1 and 2 may overlap.  The simultaneous full-shore
condition \(\Phi_{G_1}([18])\ge19\) and the alternating flow, rather than
addition of the two list sizes, enforce the total usable capacity.

The service incidences in steps 1--2 must satisfy the literal eligibility
test (1.8).  Their local dependency windows may be compiled into successor
constraints and then closed by alternating circuits from several parents.
What cannot work is a move family whose only guaranteed effect is:

* one non-distinct candidate per zero;
* an internal fusion or compression inside \(X_+\cup Y\); or
* for a one-shot Hall-perfect endpoint, fewer than nineteen new
  \(X\)-incident physical cell addresses.

The known direct one-braid census contains no H18 successor of the frozen
H19 state.  The audited Hall-19 neutral one-braid/native-rebase beam also has
no fixed-shore native-retaining ready port for the exposed
\(\{8217,8218\}\) forest; its minimum readiness defect is one.  Those are
finite restrictions on their stated catalogues, not a no-go for an
intrinsic root-migrated socket.  Theorem 3.1 is the catalogue-independent
reason the next family must expose external service capacity, while Theorems
4.1--5.1 give the exact positive certificate a compound multi-parent family
must seek.

## 7. Audit and exact remaining boundary

The conclusions proved here are:

1. the numerical split is six isolated units plus thirteen nontrivial
   congestion units;
2. the old component unions obey the exact net-port identity (3.5) against
   every final state;
3. Hall zero requires six jointly distinct zero candidates, net thirteen
   positive-component ports, and net nineteen ports on the full old DM
   shore;
4. at least nineteen distinct compiler-cell addresses acquire new incidence
   with that shore;
5. a value-nineteen alternating flow, together with the physical conditions
   of Theorem 5.1, is a sufficient full-\(16383\)-target carrier
   certificate.

The following are not proved:

1. existence of a physically legal final state with the required
   nineteen-neighbour and value-nineteen-flow signatures;
2. preservation of the particular matching \(M_*\) by such an exchange;
3. a value-nineteen alternating flow in any current multi-parent atlas;
4. one common source word for a resulting full matching; or
5. the exact \(k=15\) contiguous-OR formula.

For a one-shot Hall-perfect endpoint, the following are compact unavoidable
aggregate requirements:

\[
\boxed{
\begin{aligned}
 \nu\bigl(G_1[Z,{\cal C}]\bigr)&=6,\\
 \Phi_{G_1}(J_+)&\ge13,
\end{aligned}}
\tag{7.1}
\]

together with the global value-nineteen alternating linkage.  Every next
one-shot candidate family must be capable of this final signature.  The
strictly stronger necessary cut family is (3.7), and the exact completion
criterion is Theorem 4.3.  A service-first, interacting, multi-parent
construction is the proposed proof-safe architecture; the theorem does not
exclude an iterative descent or a larger single-parent/global circuit which
produces the same signature incidentally.

No SAT call, exhaustive enumeration, or heavy local computation was used in
this note.  The frozen counts were read from the existing deterministic
full-graph audits.
