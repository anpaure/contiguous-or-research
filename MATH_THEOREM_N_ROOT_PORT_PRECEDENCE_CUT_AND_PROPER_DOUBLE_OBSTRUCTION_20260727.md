# Root-port packet chronology: exact trail/cut/DAG equivalence and a forced proper-double two-cycle

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad \kappa=4H-1,\qquad
 d=M-\kappa=m-3H+1,
\]

and let \({\cal U}=\binom{[n]}M\).  This note gives an exact
chronological criterion for a fixed selected family of the literal
three-top packets from
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`.

There are three logically separate gates.

1. At each top, the selected root-port arcs must form one directed trail
   component.  If the component is a directed cycle, one adjacency must
   be cut to make the physical chronology open.
2. Every uncut root adjacency must lift to equality of the complete
   literal retained states, including the exposed long contexts and
   phase endpoints.  Equality of the root label alone is insufficient.
3. The union of all local event orders must be acyclic.  A topological
   ordering is then, and only then, a global packet chronology.

Once the initial endpoint states form a coefficient-one table, there is
no further prefix owner condition: every legal three-top packet preserves
the complete middle-owner incidence vector exactly.

The acyclicity gate is nonvacuous already on two events.  If two distinct
packet events contain the same adjacent tops but have different third
tops, signed root-flag disjointness forces opposite orientations.  Their
two common tops then impose opposite consecutive orders, hence a directed
precedence two-cycle.  It can be removed only by using one of those two
adjacencies as the unique cycle cut at its top.  A family of these
conflicts must therefore have a matching into eligible top cuts.  A Hall
deficiency \(h\) forces at least \(h/3\) packet deletions.

Finally, deleting \(o(N)\) packets, where
\(N=\binom{2m}M\), is an extremely strong requirement.  If \(b_U\) is
the number of arcs outside the largest root component at top \(U\), then
every such deletion scheme obeys

\[
                       3|D|\ge \sum_U b_U.
\]

Thus \(|D|=o(N)\) requires the original selected family already to have
one root component at all but \(o(N)\) tops.  Sparse deletion cannot
coalesce a generic flag matching.

## 1. Complete literal states and packet menus

For a top \(U\in{\cal U}\), let \({\mathscr S}_U\) be the set of
complete physical retained path states on \(U\).  A state records the
literal retained word, its rooted phase endpoints, and every exposed
context needed to evaluate windows through length \(2H\).  Hidden cyclic
completions which do not occur in the literal path are witnesses for
legality, not additional physical state.

For \(s\in{\mathscr S}_U\), let

\[
             \rho(s)\in U,\qquad \Omega(s)\subseteq\binom{[n]}m
\]

be respectively its position-three root label and its set of \(d\)
middle owners.  The retained paths under discussion are squarefree, so
\(|\Omega(s)|=d\).

An oriented root-port event has data

\[
 e=(C;x,y,a),\qquad |C|=M-2,qquad x,y,a\notin C
\]

with \(x,y,a\) distinct.  Its three tops are

\[
 U_{xy}=C+xy,\qquad U_{ya}=C+ya,\qquad U_{ax}=C+ax,
\]

and its projected root action is

\[
 U_{xy}:x\longrightarrow y,\qquad
 U_{ya}:y\longrightarrow a,\qquad
 U_{ax}:a\longrightarrow x.                       \tag{1.1}
\]

The reverse event reverses all three arcs.

Let \(\Lambda_e\) be the menu of all legal physical realizations of
this event: choices of the two positional bases, ordered arms and
fillers, and matched length-\(\kappa\) phase cuts.  The orientation is
already part of \(e\).  A choice
\(\lambda\in\Lambda_e\) specifies, at each incident top \(U\), one
literal state arc

\[
               s^-_{e,U}(\lambda)\longrightarrow
               s^+_{e,U}(\lambda).                 \tag{1.2}
\]

Legality includes the two exact owner facts

\[
 \dot\bigcup_{U\in e}\Omega(s^-_{e,U})
 =
 \dot\bigcup_{U\in e}\Omega(s^+_{e,U}),             \tag{1.3}
\]

and squarefreeness of both shores.  The three state arcs in (1.2) are
coupled: they must come from one common \(\omega/\eta\) packet
realization.  They cannot be selected independently at the three tops.

A coefficient-one table is a choice of at most one state per top whose
owner sets are pairwise disjoint.

## 2. Exact chronological realizability theorem

Let \({\cal E}\) be a finite multiset of distinct event occurrences.
Occurrences, rather than packet types, are the vertices of every order
below.

### Theorem 2.1 (state-trail and precedence-DAG equivalence)

There is a coefficient-one chronology which fires every occurrence of
\({\cal E}\) exactly once if and only if the following objects exist.

1. For every \(e\in{\cal E}\), choose one implementation
   \(\lambda_e\in\Lambda_e\).
2. For every top \(U\), order the incident occurrences as

   \[
                         e_{U,1},\ldots,e_{U,r_U}
   \]

   so that they form one exact state trail:

   \[
    s^+_{e_{U,i},U}(\lambda_{e_{U,i}})
    =s^-_{e_{U,i+1},U}(\lambda_{e_{U,i+1}})
        \qquad(1\le i<r_U).                         \tag{2.1}
   \]

3. The initial states

   \[
             s_U^0=s^-_{e_{U,1},U}
   \]

   on used tops, together with the chosen background states on unused
   tops, form a coefficient-one table.  The final state on a used top is
   \(s_U^1=s^+_{e_{U,r_U},U}\).
4. Form the precedence digraph \(P\) on \({\cal E}\) by adding

   \[
                         e_{U,i}\longrightarrow e_{U,i+1}    \tag{2.2}
   \]

   for every \(U\) and \(i<r_U\).  Then \(P\) is acyclic.

If initial and final tables are prescribed, the endpoint equalities in
Item 3 are imposed with those prescribed states.

#### Proof

In a chronology, the events incident with one top occur in the order in
which its unique current state changes.  Consecutive events must satisfy
(2.1).  All local orders are restrictions of the one global order, so
their union is acyclic.  The initial table is coefficient one by
hypothesis.  This proves necessity.

Conversely, choose a topological ordering of \(P\).  When an event \(e\)
is reached, every predecessor of \(e\) at each of its three tops has
already fired, while every successor is still unfired.  Induction along
the local trail (2.1) therefore says that the current states on all three
tops are exactly the source shore of \(e\).  Hence \(e\) is physically
applicable.

By (1.3), firing \(e\) changes the global owner multiplicity vector by
zero.  Thus the table remains coefficient one after every prefix.  The
induction fires every occurrence and reaches the stated final table.
\(\square\)

### Euler form

For fixed implementations, make a directed multigraph on
\({\mathscr S}_U\) whose edges are the incident state arcs (1.2).  Item 2
is equivalent to the existence of a directed Euler trail using all those
edge occurrences.  Therefore it is equivalent to weak connectivity of
all nonisolated vertices together with the standard degree balances:
all vertices balanced for a circuit, or one source with
\(\deg^+-\deg^-=1\), one sink with
\(\deg^--\deg^+=1\), and all other vertices balanced.

This is an exact state criterion.  Applying the Euler test only after
projecting to \(\rho(s)\) is merely necessary.

There is also a useful endpoint audit.  For every rooted position \(j\)
and ground label \(v\), let \(C_{j,v}\) count the tops whose current
literal state has \(v\) in position \(j\).  Every implemented three-top
packet preserves all \(C_{j,v}\).  Hence the initial and final endpoint
tables in Theorem 2.1 must have identical column histograms.  This is
automatic when the endpoint trails are assembled from the actual state
arcs (1.2), but it need not hold for trails constructed only from the
projected root arcs (1.1).

## 3. Flag-disjoint specialization, trail components, and cuts

Use two signed copies of every root flag \((U,x)\).  Call a selected
family flag-disjoint when its outgoing flags and incoming flags are each
used at most once.  For each top \(U\), let \(R_U\) be the directed graph
on labels in \(U\) obtained from (1.1).  Flag disjointness gives

\[
                         \deg^+_{R_U},\deg^-_{R_U}\le1.       \tag{3.1}
\]

Hence every nontrivial component of \(R_U\) is a directed path or a
directed cycle.

### Proposition 3.1 (one-component and cut criterion)

For a flag-disjoint family, Item 2 of Theorem 2.1 can hold at \(U\) only
if all selected arcs at \(U\) lie in one nontrivial component of
\(R_U\).

If this component is a path, its event order is forced.  If it is a
cycle, choose one cyclic successor adjacency as a cut and use the unique
linear order beginning after that cut.  The root trail lifts physically
if and only if (2.1) holds at every uncut adjacency.  No equality is
required across the cut; its two endpoint states are the final and
initial states at \(U\).

Thus one cycle cut performs two jobs simultaneously:

1. it is the sole permitted local context discontinuity; and
2. it is the sole cyclic successor relation omitted from the precedence
   digraph.

#### Proof

The projection of one state trail is a directed root trail using every
selected root arc.  Under (3.1), such a trail cannot move between two
components.  A path has only one directed edge order.  A cycle has only
its cyclic order, with a choice of where the chronological list begins.
Exact equality of complete states is precisely (2.1) at the uncut
successors. \(\square\)

### Exact transposition holonomy

Every local arc \(x\to y\) of a three-top packet literally swaps the two
labels \(x,y\) in the retained rooted word and fixes all other labels.
Suppose a projected root cycle is

\[
             x_0\to x_1\to\cdots\to x_{\ell-1}\to x_0.      \tag{3.2}
\]

The product of its \(\ell\) literal swaps fixes \(x_0\) and acts on the
other cycle labels as one \((\ell-1)\)-cycle.  In one composition
convention it is

\[
                 (x_1\ x_{\ell-1}\ x_{\ell-2}\ \cdots\ x_2). \tag{3.3}
\]

Indeed, track the label occupying the root position after every swap.
At the final swap \(x_0\) returns to the root, while the labels formerly
away from the root shift once around their \(\ell-1\) positions.

Consequently a simple projected cycle of length \(\ell\ge3\) is not a
closed full-state circuit.  It can still be used, but only as the open
state trail obtained by making a genuine cut as in Proposition 3.1.
The length-two inverse pair is the only simple root cycle with zero
transposition holonomy.

This corrects a tempting but false shortcut: a root-label circulation is
not automatically a literal-state circulation.

## 4. A forced directed two-cycle from a proper double

Let

\[
                    U=S+u,\qquad V=S+v,\qquad |S|=M-1,
\]

be adjacent tops.  For \(z\in S\), the packet triangle containing
\(U,V\) with third top different from them is

\[
                     e_z:\quad U,\ V,\ S-z+u+v.              \tag{4.1}
\]

Call \(e_z,e_w\) a proper double on \(U,V\) when \(z\ne w\).  Thus the
two packet events share exactly the two tops \(U,V\), not all three.

### Theorem 4.1 (proper-double precedence obstruction)

In a flag-disjoint selected family, two events in a proper double have
opposite orientations.  After relabeling the two events, their projected
actions at the shared tops are

\[
\begin{array}{c|cc}
        &U&V\\ \hline
 e_z&z\to u&v\to z\\
 e_w&u\to w&w\to v.
\end{array}                                                   \tag{4.2}
\]

Therefore they are consecutive with orders

\[
                         e_z<e_w\quad\hbox{at }U,
 \qquad                  e_w<e_z\quad\hbox{at }V.             \tag{4.3}
\]

The uncut precedence graph contains a directed two-cycle.  Any chronology
must use at least one of the two adjacencies in (4.3) as the cycle cut at
its top.  In particular, if both shared-top components are paths, no
chronology exists.

#### Proof

Orient \(e_z\) by taking \((x,y,a)=(z,u,v)\) in (1.1).  This gives
\(z\to u\) at \(U\) and \(v\to z\) at \(V\).  The reverse orientation
gives \(u\to z\) and \(z\to v\).

If \(e_z,e_w\) had the same orientation, they would repeat either the
incoming flag \((U,u)^-\) or the outgoing flag \((U,u)^+\).  Hence flag
disjointness forces opposite orientations, yielding (4.2).  The common
port \(u\) makes the two arcs consecutive at \(U\), and the common port
\(v\) makes them consecutive in the reverse order at \(V\).  The two
precedence arcs form a directed two-cycle unless one is the omitted cycle
cut. \(\square\)

The qualifier proper is necessary.  The two opposite orientations of
one fixed packet triangle share all three tops; at every top they can be
ordered as an event followed by its inverse.  They are not the
opposite-order pattern (4.3).  If distinct unoriented direction atoms are
required, that inverse pair is excluded anyway because it repeats the
same unordered direction at every top.

In particular, the family consisting only of \(e_z,e_w\) is already an
explicit root-port scheduling counterexample.  Its graph at \(U\) is the
single path

\[
                              z\to u\to w,
\]

while its graph at \(V\) is the single path

\[
                              w\to v\to z.
\]

The two third tops each carry one isolated event arc.  Thus every used
top has one local trail component, but the two compulsory path orders
are opposite.  No choices of physical contexts can repair the global
precedence two-cycle; contexts can only create an earlier failure of
state gluing.

### The cut-Hall obstruction

Let \({\cal Q}\) be the family of proper doubles.  After the root
components and all permitted context lifts have been fixed, form a
bipartite graph \(B_{\rm cut}\) with left shore \({\cal Q}\) and right
shore the tops.  A conflict \(q\) on \(U,V\) is adjacent to \(U\) exactly
when the component at \(U\) is cyclic and its forced adjacency from
(4.3) is an admissible context cut; define adjacency to \(V\) similarly.

### Corollary 4.2 (cut-Hall necessity)

Every chronology gives a matching of \({\cal Q}\) into eligible top
cuts.  Hence

\[
              |F|\le |N_{B_{\rm cut}}(F)|
                    \qquad(F\subseteq{\cal Q})               \tag{4.4}
\]

is necessary.  If

\[
                         h=|{\cal Q}|-\nu(B_{\rm cut}),        \tag{4.5}
\]

then every repair by packet deletion uses at least

\[
                              \left\lceil {h\over3}\right\rceil \tag{4.6}
\]

deleted packets.

#### Proof

Theorem 4.1 assigns every proper double to one of the two cuts which
breaks it.  One top has only one chronological cut, and for proper
doubles one successor adjacency identifies only one conflict.  This is
the matching in (4.4).

At least \(h\) left vertices must be removed before the remaining cut
graph can have a matching covering its left shore.  One packet belongs
to only three unordered top pairs and, under flag disjointness, to at
most one proper double on each pair.  Deleting one packet therefore
removes at most three proper-double conflicts.  This proves (4.6).
\(\square\)

This Hall condition removes only the forced two-cycles.  Longer mixed-top
precedence cycles may remain, so (4.4) is necessary and not sufficient.

## 5. The full global cut condition

Before choosing chronological cuts, put one colored successor arc
between each pair of consecutive events in every local root path and in
every local root cycle.  Call the resulting event digraph
\(\widehat P\).  Path arcs are compulsory.  At each cyclic top one may
remove exactly one of its colored successor arcs, and that same removal
must be the context cut of Proposition 3.1.

### Proposition 5.1 (global feedback-transversal form)

After the packet implementations and one local root component per top
have been fixed, a chronology exists if and only if there is a choice of
one admissible successor cut at every cyclic top such that

1. every remaining local adjacency satisfies exact state equality
   (2.1); and
2. deleting the chosen colored arcs from \(\widehat P\) leaves an
   acyclic event digraph.

This is just Theorem 2.1 and Proposition 3.1, but it exposes the exact
combinatorial object: a partition-constrained feedback-arc transversal,
coupled to literal context equality.

In particular, a directed cycle made solely of compulsory path
adjacencies is an absolute obstruction.  More generally, if after every
admissible cut choice the remaining precedence graph has \(r\)
vertex-disjoint directed cycles, at least \(r\) event deletions are
necessary.

## 6. What deleting \(o(N)\) events must actually prove

Let \({\cal E}_0\) be a flag-disjoint selected family, and let
\(d_U\) be its number of arcs at top \(U\).  If the nontrivial root
components at \(U\) have edge sizes

\[
                   s_{U,1}\ge s_{U,2}\ge\cdots,
\]

put

\[
                         b_U=d_U-s_{U,1}.                     \tag{6.1}
\]

### Lemma 6.1 (component deletion lower bound)

If deleting \(D\subseteq{\cal E}_0\) leaves one root trail component at
every top, then

\[
                              3|D|\ge\sum_U b_U.              \tag{6.2}
\]

#### Proof

Deletion cannot join two original components.  At top \(U\), every arc
outside one chosen original component must therefore be deleted, costing
at least \(b_U\) incident arcs.  Every deleted packet contributes exactly
three deleted top incidences.  Sum over the tops. \(\square\)

Consequently

\[
 |D|=o(N)\quad\Longrightarrow\quad
 \sum_U b_U=o(N),                                            \tag{6.3}
\]

and hence all selected arcs already lie in one component at all but
\(o(N)\) tops.  This is much stronger than saying that a typical largest
component has size \(M-o(M)\): the integral error outside the largest
component must have total \(o(N)\), or average \(o(1)\) per top.

There are analogous sharp demands at the next two gates.

* All but the one chosen cut per cyclic top must be exact literal-context
  joins.  Since there are \((1-o(1))MN\) local arcs, this asks for exact
  compatibility at all but \(O(N)\) of \(\Theta(MN)\) potential joins,
  followed by the correct global choice of the exceptional cuts.
* After those cuts, the precedence graph must have feedback vertex number
  \(o(N)\).  Every packet event has at most three local predecessors and
  three local successors, so deleting \(o(N)\) event vertices changes only
  \(o(N)\) colored precedence arcs.

Thus an \(o(N)\)-deletion theorem cannot be obtained by first taking an
arbitrary near-perfect flag matching and then cleaning a positive density
of local component or precedence defects.

## 7. Scaling and the absence of a scalar capacity obstruction

Assume the calibrated regime

\[
               \lambda={W\over N}=M+O(H),\qquad H=o(m),
 \quad W=\binom{2m}m.                                       \tag{7.1}
\]

Then \(N=(1+o(1))W/M\), and a near-perfect matching in the signed
root-flag hypergraph contains

\[
                  |{\cal E}_0|=(1-o(1)){MN\over3}
                              =(1-o(1)){W\over3}.             \tag{7.2}
\]

It gives degree \(M-o(M)\) at a typical top.  If those arcs coalesce into
one component, the resulting local trail has the required
\(\Theta(m)\) length, and all top-event incidences together have mass
\((1-o(1))MN=(1-o(1))W\).

There is no elementary top-pair shortage behind Theorem 4.1.  The number
of adjacent unordered top pairs is

\[
                         {1\over2}NM(n-M).                    \tag{7.3}
\]

A packet uses three such pairs, so the family in (7.2) asks for only

\[
                         3|{\cal E}_0|=(1-o(1))MN             \tag{7.4}
\]

pair incidences, a fraction

\[
                         {2+o(1)\over n-M}=O(m^{-1})          \tag{7.5}
\]

of the available adjacent pairs.  Likewise, a top needs only
\(2M+o(M)\) neighboring-top incidences out of its
\(M(n-M)=\Theta(m^2)\) Johnson neighbors.  Thus top-pair simplicity is
counting-feasible; it is a structured matching requirement.

The initial coefficient-one endpoint table would use

\[
                         dN=W-O(HN)=W-o(W)                    \tag{7.6}
\]

middle owners.  Again the scalar census is correct.  The missing fact is
an integral choice of the actual endpoint states whose owner supports are
pairwise disjoint and whose uncut contexts glue.

## 8. Exact proved and unproved boundary

Proved here:

1. a necessary-and-sufficient state-trail/precedence-DAG theorem for a
   fixed packet family with arbitrary legal phase-cut menus;
2. the reduction of a signed-flag matching to one path/cycle component,
   one cut per root cycle, and exact context equality off the cuts;
3. the nontrivial transposition holonomy of every simple root cycle of
   length at least three;
4. a literal proper-double directed two-cycle obstruction;
5. the cut-Hall necessary condition and its \(h/3\) deletion lower bound;
6. the component deletion inequality \(3|D|\ge\sum_Ub_U\); and
7. the exact calibrated counts showing no scalar top, pair, event, or
   owner shortage.

Not proved:

1. a selected flag matching with \(\sum_Ub_U=o(N)\);
2. simultaneous choices of all \(\omega/\eta\) contexts and matched
   physical phase cuts satisfying every uncut state equality;
3. an initial coefficient-one endpoint table for those lifted trails;
4. a cut selection making the global precedence graph acyclic after only
   \(o(N)\) event deletions; or
5. the resulting coefficient-one contiguous-OR construction.

The exact positive target is therefore not merely a near-perfect root-flag
matching.  It is a near-Hamilton root-component packing with a common
literal context lift and a partition-constrained acyclic cut system.
