# Portal-first SCD forests and the canonical upper-exact pull-tree no-go

**Date:** 2026-08-01  
**Lane:** H3, protected upper-exact host  
**Status:** exact positive theorem for the raw graphic row, exact conditional
pull-extension and rooted-port cuts, and an unconditional construction-specific
upper-colour no-go for every \(m\ge12\).  The unrestricted marked all-high
chain selector is also audited as solved by an SCD.  No compiler, lower-turn,
Euler, common-cap, or additive-constant theorem is claimed.

## 0. Verdict

Choosing a bounded ordered-shift or monotone-pivot bank **before** any SCD
components are merged does remove the scattering obstruction, but only at the
uncoloured graphic level.

1. On raw SCD chains, every common-order portal transversal with distinct
   tails is a forest.  With the robust linear lists one may, more strongly,
   choose distinct heads outside all task tails, so a bounded bank can be made
   a matching of raw chain components.
2. Once a literal allowed connector graph has been fixed, a protected forest
   \(A\) extends to a spanning merge tree exactly when the allowed graph
   remains connected after \(A\) is contracted.  This is the precise sense in
   which portal-first selection eliminates scattering.
3. A Johnson portal is not automatically a canonical Mütze/GMN pull label.
   A pull is an occurrence-labelled alternating \(C_6\) with forced companion
   edges and external turn stubs.  Literal provenance and preservation of the
   complete packet interface are additional hypotheses.
4. Even after a literal lift, a graphic spanning tree is not a Hamilton
   chronology.  Tail, head, upper-colour, and graphic independence must be
   chosen jointly, followed by a rooted free-port Hall matching.
5. Most decisively, the canonical lexical GMN pull-tree family cannot be
   upper-exact for \(m\ge12\).  It misses at least

   \[
      M_r-3(\operatorname {Cat}_r-1)>0,
      \qquad r=m-1,                                           \tag{0.1}
   \]

   immediate-upper colours; the first residual is \(1941\) at \(m=12\).
   This holds even with no protected bank.  Prescribing portals or opening the
   final cycle cannot improve the bound.

Thus portal-first selection closes the former graphic-scattering row, but the
requested protected upper-exact host does **not** follow from the canonical
Mütze pull-tree theorem.  The live route must jointly construct a nonlexical
upper-exact rooted Catalan forest, a free-port connector reservoir, and a
hereditarily transparent occurrence interface.

## 1. Raw ordered portals form a protected forest

Fix one total coordinate order (\prec).  For a rank-(m) set (X), put

\[
             \phi(X)=\sum_{x\in X}\operatorname {pos}_\prec(x). \tag{1.1}
\]

Every ordered-shift portal has the form

\[
       p\longrightarrow q=p-\{a\}+\{b\},\qquad a\prec b,       \tag{1.2}
\]

and the prepared pivot geodesic has the same form at every selected step.
Hence every portal strictly increases (\phi).

### Theorem 1.1 (portal-first raw-SCD forest)

Let (A) be a collection of such portals, with every rank-(m) root used as
a tail at most once.  Then the underlying undirected graph of (A) is a
forest.  Contracting the chains of any SCD before any other merger changes
neither its vertices nor its edges.

#### Proof

If an undirected cycle existed, choose on it a vertex of minimum (\phi).
Both incident cycle edges point away from that vertex, giving two selected
outgoing edges from one tail, a contradiction.

A symmetric chain contains at most one set of each rank.  Distinct rank-(m)
sets therefore lie in distinct SCD chains, so raw SCD contraction identifies
no portal endpoints.  \(\square\)

The theorem permits repeated heads.  For a Hamilton chronology those must be
removed.

### Corollary 1.2 (bounded raw-chain portal matching)

Suppose there are \(h\) task tails, every literal menu has size at least
\(L\), and the heads in one menu are distinct.  If \(L\ge2h\), one may choose
one portal per task so that all chosen heads are distinct and no chosen head
is a task tail.  In particular, the chosen raw-chain edges form a matching.

#### Proof

Deleting the at most (h) task-tail vertices leaves at least (L-h\ge h)
head choices in every menu.  Hence every nonempty subfamily of at most (h)
tasks has at least (h), and therefore at least its own size, available head
vertices in its union.  Hall's theorem gives distinct outside heads.  \(\square\)

For the robust ordered flags,

\[
                   L\ge m+1-(h-1)d-b,                         \tag{1.3}
\]

so Corollary 1.2 is automatic for fixed (h), (d=O(\sqrt m)), and
(b=O(hd)) in sufficiently large dimension.

## 2. Exact augmentation after portals are selected

Let (G) be a labelled graph of **literal allowed** component mergers on the
raw SCD chains, and let (A\subseteq E(G)) be the selected portal forest.
Labels forbidden by a protected interface are deleted before forming (G).

### Theorem 2.1 (sharp portal-first augmentation cut)

There is a spanning labelled tree (T\subseteq G) containing (A) if and
only if

\[
       A\text{ is a labelled graphic forest}
       \quad\text{and}\quad G/A\text{ is connected}.           \tag{2.1}
\]

Equivalently, every nontrivial partition of the components of (A) is
crossed by an allowed label.

#### Proof

Necessity is inherited from a spanning tree.  Conversely, take a spanning
tree of the connected contraction (G/A) and uncontract (A).  The result
has (|V(G)|-1) edges and no cycle, hence is the required tree.  \(\square\)

This theorem explains the quantifier gain.  If menus are contracted first,
an entire linear menu can become loops and violate a graphic-flat cut.  If a
literal edge (A) is selected first and every later merger must extend the
same forest, no selected edge can later become redundant: an alternate path
between its endpoints would create a cycle in the final tree.

The word *literal* is load-bearing.  A portal in the Johnson graph of middle
roots and an edge of a canonical pull auxiliary graph are different objects.

## 3. The exact SCD selector collapse is sound

The all-high selector LP chooses one local flag

\[
 q=T_0\supset T_1\supset\cdots\supset T_{d-1},
 \qquad |T_j|=m-j,                                           \tag{3.1}
\]

at every rank-(m) root of (B_{2m+1}).  A suffix may be marked or left
unmarked; every target at every displayed rank must receive marked load one.

### Theorem 3.1 (SCD gives an exact integral marked selector)

Every symmetric-chain decomposition of (B_{2m+1}) gives a zero-one solution
of the exact all-high flag/mark LP for every (d\le m+1).

#### Proof

A symmetric chain runs from rank (a\le m) to rank (2m+1-a), so it has a
unique rank-(m) member (q_C).  The chains partition the middle layer;
therefore (C\mapsto q_C) is a bijection onto all roots.

Read the saturated chain downward from (q_C).  If its successive deleted
elements are (z_1,\ldots,z_\ell), then

\[
          C_{m-j}=q_C-\{z_1,\ldots,z_j\}\qquad(j\le\ell).      \tag{3.2}
\]

Continue the deletion word arbitrarily inside the chain minimum until it has
length (d-1), and leave this arbitrary continuation unmarked.  Mark exactly
the suffixes in (3.2).

There are enough continuation elements: if the chain minimum has rank \(a\)
and the genuine downward segment has length \(\ell=m-a\), then
\(d-1-\ell\le a\) follows from \(d-1\le m\).

Every target (S) of rank (m-j) belongs to one SCD chain.  That chain
reaches rank (m), and its marked (j)-suffix is exactly (S).  No other
chain marks (S).  Root equations and every target equation therefore have
load one.  \(\square\)

There is no hidden nesting requirement in the stated LP: the (y)-variables
may leave a suffix unmarked.  The construction is therefore valid even when
a short SCD chain needs an arbitrary deeper continuation.

Two scope qualifications remain.

* The construction uses the complete adaptive local-order atlas.  Every local
  deletion word is induced by some total order, but the proof does not place
  all chosen flags in one fixed or support-optimal small global-order menu.
* It is selector-level only.  It does not make two successive roots satisfy
  the legal ordered-turn inclusions, balance turn indegrees/outdegrees, or
  produce an Euler or upper-resident chronology.

Arbitrary prescribed root flags can be retained while their suffixes are
quarantined unmarked: for (h\le m+1), strict upper-shadow surplus routes
every high target through unprotected roots.  If occurrence-labelled marks
on those flags are forced, the exact selector condition in the same range is
only that no two forced occurrences name the same target; one transfers each
mark from its flexible provider to the prescribed variable.  For fully
marked prefixes from distinct roots, this reduces exactly to pairwise
vertex-disjointness.  The descending-linear-forest condition belongs to the
stronger unlabelled edge-set factor problem, where arbitrary fragments may
concatenate after root ownership and occurrence multiplicity are forgotten.
Thus unprotected chain correlation, and even the occurrence-labelled marked-
selector version of bounded protection, are not the remaining H3 obstruction.

### Corollary 3.2 (portal-first endpoint freezing is selector-compatible)

Choose (h) ordered-shift portals as in Corollary 1.2, so their (2h)
endpoints are distinct.  Give every tail and head the flag induced by the
same prepared total order.  If

\[
                              2h\le m+1,                       \tag{3.3}
\]

then these endpoint flags coexist with an exact marked all-high selector,
and every selected portal remains a legal ordered-shift turn.

#### Proof

The ordered-shift theorem uses the same total order at its tail and head, so
each selected portal is legal after both endpoint flags are frozen.  The
protected SCD selector accepts any at most (m+1) prescribed root flags: it
quarantines their suffixes unmarked and routes every named high target through
unprotected roots.  Apply it to the (2h) endpoint flags.  \(\square\)

Thus the SCD observation repairs an important quantifier: one should select
the bounded heads first and only then freeze their compatible flags.  It does
not show that all flexible-root flags admit legal successor turns, or that the
selected turns extend to a balanced global turn factor.

## 4. Why an SCD portal is not yet a Mütze pull

Use the canonical GMN lexical factor and let (H_r) be its labelled pull
auxiliary multigraph.  A label (g) represents an alternating incidence
hexagon (C_g), with three old and three new factor incidences.  Canonical
hexagons are edge-disjoint, but they may share vertices.

A protected Johnson portal has a **literal pull lift** only after specifying:

1. a canonical label (g) and the phase in which its claimed portal edge
   occurs;
2. all six old/new incidence occurrences and all six untouched factor stubs;
3. the induced tail, head, and immediate lower/upper turn roles;
4. the packet interior, ordered boundary ports, residence run ages, and every
   prefix/suffix/interval witness claimed to survive; and
5. consistency of all forced and forbidden factor incidences across the
   protected bank.

Call the union of these data the complete protected interface
(\mathcal I(A)).  A completion-label bank is **hereditarily transparent**
when every graphic subset of it can be toggled jointly while leaving
(\mathcal I(A)) unchanged, including the selected occurrence token for
every protected OR value.

### Theorem 4.1 (conditional protected pull extension)

Suppose the portal bank has literal lifts whose canonical labels form a
forest \(A_H\) in \(H_r\).  Delete every label that is not in the declared
hereditarily transparent bank for (\mathcal I(A)), obtaining
(H_r^{\rm adm}).  Then the portal bank extends, using only labels of this
bank, by canonical pulls while preserving the entire declared interface if
and only if

\[
                         H_r^{\rm adm}/A_H
                         \quad\text{is connected}.              \tag{4.1}
\]

Here the equivalence is inside the declared Cartesian, hereditarily
transparent label bank.

#### Proof

Theorem 2.1 gives the labelled spanning tree.  Hereditary transparency lets
all its labels be toggled simultaneously without changing the protected
interface.  Conversely every preserving canonical pull tree consists of
allowed labels, contains a forest, and remains connected after that forest
is contracted.  \(\square\)

Raw-SCD forestness proves none of the lift hypotheses.  Selecting one edge of
a pull also forces its two companion new edges and deletes three old edges.
An arbitrary ordered shift may occur in no canonical pull at all.

## 5. Graphic augmentation is not coloured chronology

There are two independent gaps after Theorem 4.1.

First, a forest may fail the port constraints.  The two forward edges

\[
                         p_1\longrightarrow q
                 \longleftarrow p_2                           \tag{5.1}
\]

form a tree, but no directed Hamilton chronology can contain both because
the head port of (q) is used twice.  Corollary 1.2 removes this local defect
for a bounded raw bank, but a global completion must retain it.

Second, edge-disjoint pull labels do not carry context-free upper colours.
If two pulls touch the two old incidences at the same lower turn, their four
states have the mixed difference

\[
 [L+c+d]-[L+b+c]-[L+a+d]+[L+a+b],                             \tag{5.2}
\]

which is nonzero when the four displayed colours are distinct.  Thus no
additive colour vector on uncoloured pull labels follows from edge
disjointness.  Exact upper preservation needs local pair-state variables or
joint occurrence-token transparency.

For the owner-layer problem on ranks (m-1,m) of ([2m-1]), fix a perfect
incidence matching (M_0).  A rooted Catalan forest (Q_0) has one
occurrence of each rank-((m+1)) upper colour and

\[
             C=\binom{2m-1}{m}-\binom{2m-1}{m+1}
              =\operatorname {Cat}_m                           \tag{5.3}
\]

directed path components.  Contract any already chosen protected component-
connector paths, and let \(\mathcal C'\) be the resulting component set with
\(C'=|\mathcal C'|\).  Every member of \(\mathcal C'\) has at most one free
outgoing and one free incoming port.

### Theorem 5.1 (exact rooted free-port finish)

Let \(K_*\) be the component of \(\mathcal C'\) required to contain the
initial protected portal path.  Suppose the remaining literal component-arc
reservoir is acyclic.  Delete the incoming copy of \(K_*\) from its port
bipartite graph.  There is a set of \(C'-1\) connectors forming one directed
spanning path from \(K_*\) if and only if

\[
 |N^-(Y)|\ge |Y|
 \quad\text{for every family }Y\text{ of components not containing }K_*.
                                                                    \tag{5.4}
\]

#### Proof

Equation (5.4) is Hall's theorem for a matching saturating every incoming
component except \(K_*\).  The matching has \(C'-1\) arcs and component
indegree/outdegree at most one.  Acyclicity excludes a disjoint directed
cycle.  Hence \(K_*\) is the unique source and every component lies on one
directed spanning path.  Necessity is immediate.  \(\square\)

This theorem preserves upper exactness only because (Q_0) was selected
before the connectors and its representative occurrences remain literal.
It does not construct (Q_0).  The latter is a common tail/head/graphic/
upper-colour selection, not a consequence of raw graphic augmentation.

## 6. Canonical lexical pull trees are not upper-exact

Put (r=m-1) and

\[
 W_r=\binom{2r+1}{r},\qquad
 C_r=\operatorname {Cat}_r=\frac{W_r}{2r+1}.                  \tag{6.1}
\]

The immediate-upper turn map of the canonical (0/1)-lexical base factor
omits exactly

\[
 M_r=W_r\frac{(r-2)(r-3)}{2(r+2)(2r-1)}.                     \tag{6.2}
\]

One alternating incidence (C_6) changes the selected incident pair at only
three lower turns, and hence can add at most three formerly missing turn
values.  A canonical pull spanning tree uses at most (C_r-1) pulls.

### Theorem 6.1 (sharp canonical upper-exact no-go)

For every (r\ge11), equivalently (m\ge12), every Hamilton cycle obtained
from the canonical lexical factor by a canonical pull spanning tree omits at
least

\[
              M_r-3(C_r-1)>0                                 \tag{6.3}
\]

rank-((r+2)=m+1) immediate-upper colours.  At (r=11) the residual is
exactly (1941).

The conclusion remains true after prescribing any portal forest inside the
pull tree and after opening the cycle into a Hamilton path.

#### Proof

Telescoping the three-turn bound over at most (C_r-1) pulls gives (6.3).
Moreover

\[
 M_r-3C_r=
 \frac{W_r(2r^3-21r^2-11r+18)}
      {2(r+2)(2r-1)(2r+1)}.                                  \tag{6.4}
\]

The cubic numerator is (18) at (r=11) and has positive derivative for
all (r\ge11).  Adding the final (3) in (6.3) proves positivity, and
direct substitution gives (1941).  A prescribed forest only restricts
the available pull trees.  Deleting an edge to open a cycle creates no new
turn value.  \(\square\)

The requested protected host requires this immediate-upper turn row in
addition to its complete interval-OR deck.  Hence the canonical lexical
pull-tree route already fails one necessary row before residence, wider
intervals, or any compiler condition is imposed.

A separate contiguous-OR word could in principle realize one of these masks
at a longer crossing interval.  Such an occurrence is outside the projected
turn map and must be explicitly address-labelled and protected.  It is not
supplied by the canonical pull-tree theorem and cannot be inferred from
portal-first forestness.

## 7. Exact surviving H3 target

The proof-safe prospective target is the following jointly quantified
object.

1. Choose the protected predecessor shore and (M_0) together, so the
   successor pivot shore is a directed path with distinct tails and heads.
2. Choose a nonlexical upper-surjective directed linear-forest support
   containing that path, and retain one literal representative of every
   upper colour to obtain (Q_0).
3. Choose an acyclic free-port reservoir satisfying the rooted Hall cuts
   (5.4), and connect the (\operatorname {Cat}_m) components.
4. Require every connector operation to be jointly transparent for the
   protected immediate palettes, literal resident return collars, clipped
   boundary ages, and every occurrence-labelled upper OR witness.

The SCD selector theorem closes unrestricted marked lower-chain correlation,
and Theorems 1.1--2.1 close prospective uncoloured scattering.  The missing
theorem is the common upper-exact support plus transparent port reservoir.

The following rows remain explicitly outside the present result:

* legal balanced owner/turn circulation beyond the protected phase;
* exterior residence and regeneration of clipped collar endpoints;
* arbitrary-width upper witness construction when not already included as
  protected tokens;
* the lower compiler, common cap, and terminal damage matching; and
* any implication (\nu(k)\le B(k)+O(1)).
