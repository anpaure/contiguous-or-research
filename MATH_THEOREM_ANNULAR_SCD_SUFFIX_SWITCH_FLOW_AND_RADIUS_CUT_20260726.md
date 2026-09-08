# Gaussian-annular SCD switching: exact flow criterion and the radius-layer cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad h=o(\sqrt m),
\tag{0.1}
\]

where \(A>0\) is fixed.  The surviving target from the preceding note was
a noncanonical SCD, or a pair of complementary SCDs, with only \(o(W)\)
directed prefix-contaminant transitions.  This note formulates the exact
flow problem for the largest presently certified class of good
transitions--state-composable suffix switches--and proves a sharp
obstruction.

Every symmetric chain in \(2^{[2m+1]}\) has a radius \(s\ge0\): its
minimum and maximum ranks are

\[
 m-s,\qquad m+1+s.
\tag{0.2}
\]

Let \(V_s\) be the radius-\(s\) chains of an arbitrary SCD and put
\(c_s=|V_s|\).  The layer sizes are independent of the SCD:

\[
 \boxed{
 c_s=\binom{2m+1}{m-s}-\binom{2m+1}{m-s-1}.}
\tag{0.3}
\]

Choose one actual ordered-partition state for every chain.  Between
\(V_s\) and \(V_{s-1}\), retain any certified one-update arcs which map
the chosen source state to the chosen target state.  Let \(\nu_s\) be the
maximum matching size of this bipartite graph and let

\[
 \delta_s=c_s-\nu_s
 =\max_{X\subseteq V_s}\bigl(|X|-|N_s(X)|\bigr).
\tag{0.4}
\]

Then the exact minimum number of paths in a radius-decreasing state cover
is

\[
 \boxed{
 p=c_0+\sum_{s\ge1}\delta_s.}
\tag{0.5}
\]

This is an ordinary integral max-flow/min-cut theorem; no nibble or
fractional rounding is hidden in it.

The decisive obstruction is already present in the complete-graph
relaxation.  Even if every radius-\(s\) state could switch to every
radius-\((s-1)\) state,

\[
 \boxed{
 p\ge\max_s c_s
 =\left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{0.6}
\]

The equality \(p=\max_sc_s\) holds in the complete relaxation.  Thus no
choice of noncanonical SCD can improve the radius-decreasing component
rate below the critical \(W/\sqrt m\) scale.

There is also a sharp escape census.  In an arbitrary state-composable
path cover, let \(b\) be the number of selected arcs which do not decrease
radius.  Then

\[
 \boxed{p+b\ge \max_s c_s.}
\tag{0.6a}
\]

Consequently, a construction with \(p=o(W/H)\) must contain at least

\[
 \left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}
\tag{0.6b}
\]

state-composable horizontal or upward switches.  This is the exact
quantitative burden that a complementary second SCD would have to carry.

This rate is fatal for the standard exact component-reset compiler at a
fixed Gaussian cutoff.  There are constants \(b_A,d_A>0\) such that at
least

\[
 b_A{W\over\sqrt m}
\tag{0.7}
\]

components must start at radius at least \(d_A\sqrt m\).  Their first
annular states each contain \(\Theta_A(\sqrt m)\) forced singleton
increment blocks.  Hence the exact reset ledger pays

\[
 \boxed{\Omega_A(W)}
\tag{0.8}
\]

extra letters, even under complete adjacent-layer compatibility.

Therefore neither a noncanonical SCD nor one member of a complementary
pair can solve the Gaussian annulus using only radius-decreasing suffix
switches plus independent component resets.  A positive construction must
add one of the following genuinely new mechanisms:

1. state-composable same-radius or radius-increasing arcs which cross the
   radius-layer cut;
2. useful nonlocal reset words whose letters simultaneously cover assigned
   annular targets, so their cost is not an independent component charge;
3. a two-SCD chronology which changes decompositions while retaining the
   inherited ordered-partition state.

The theorem is an architecture-level obstruction, not a universal lower
bound for literal OR words.

## 1. Annular state fibers and the exact switching test

For an ordered partition \(\Pi=(B_1,\ldots,B_k)\) and a nonempty mask
\(X\), write

\[
 M_X(\Pi)=(X,B_1\setminus X,\ldots,B_k\setminus X),
\tag{1.0}
\]

with empty blocks deleted.  This is the exact last-occurrence-state update
caused by appending \(X\) to the literal word.

Let \(C\) be a symmetric chain.  Write

\[
 C=(B;z_1,\ldots,z_{2s+1})
\tag{1.1}
\]

when its radius is \(s\).  Let \(\mathcal A_{h,H}(C)\) be the nested
subfamily consisting of the two central members and every chain member in
the lower and upper annuli through the smaller of \(s\) and \(H\).

An ordered partition \(\Pi\) is an annular state for \(C\) if every member
of \(\mathcal A_{h,H}(C)\) is a prefix union of \(\Pi\).  Let
\(F_{h,H}(C)\) be this state fiber.

The following is the fixed-state switching criterion.  It is stated for a
general nested target family because the shallow ranks between the annulus
and the centre need not be prescribed.

### Lemma 1.1 (exact annular anchor test)

Let \(\Pi\) be any ordered partition and let

\[
 \mathcal T=(A=T_0\subset T_1\subset\cdots\subset T_r)
\tag{1.2}
\]

be a nonempty nested target family with \(A\ne\varnothing\).  There is a
nonempty update whose new state exposes \(\mathcal T\) if and only if the
prefix chain of \(\Pi-A\) contains

\[
 \mathcal T-A=(\varnothing,T_1-A,\ldots,T_r-A).
\tag{1.3}
\]

Whenever some update works, the canonical update \(X=A\) works.

#### Proof

Suppose \(M_X(\Pi)\) exposes \(\mathcal T\).  Its first block \(X\) is
contained in every target and hence in \(A\).  Removing that first block
shows that the prefix chain of \(\Pi-X\) contains \(\mathcal T-X\).
Delete the additional common set \(A\setminus X\) from the residual
partition and all target prefixes.  This gives (1.3).

Conversely, if (1.3) holds, then

\[
 M_A(\Pi)=(A,\Pi-A)
\]

exposes every member of \(\mathcal T\). \(\square\)

For a target chain \(D\) whose required annular family has least member
\(A_D\), Lemma 1.1 is an exact switching screen:

\[
 \boxed{
 \Pi_C\longrightarrow D
 \quad\Longleftrightarrow\quad
 \operatorname {Pref}(\Pi_C-A_D)
 \supseteq\mathcal A_{h,H}(D)-A_D.}
\tag{1.4}
\]

The actual inherited successor state is

\[
 \Pi_D=M_{A_D}(\Pi_C).
\tag{1.5}
\]

Consequently a sequence of switches composes exactly only when the state
chosen at each intermediate chain is the state actually produced in
(1.5).  Pairwise existential compatibility without this equality is not
enough.

### Definition 1.2 (certified suffix-switch system)

For every SCD chain \(C\), choose one state
\(\Pi_C\in F_{h,H}(C)\).  A certified arc \(C\to D\) is an equality

\[
 \Pi_D=M_X(\Pi_C)
\tag{1.6}
\]

for some nonempty mask \(X\).  A radius-decreasing suffix-switch system
retains only certified arcs from \(V_s\) to \(V_{s-1}\).

Because states, rather than only chain labels, are fixed in (1.6), every
directed path in this graph is a literal move-to-front state path.

## 2. Exact max-flow/min-cut criterion

For each \(s\ge1\), form the bipartite graph

\[
 G_s=(V_s,V_{s-1};E_s)
\tag{2.1}
\]

of certified arcs.  Matchings in different \(G_s\)'s may be selected
independently: a chain may have one incoming edge from radius \(s+1\) and
one outgoing edge to radius \(s-1\), exactly as an internal path vertex.

### Theorem 2.1 (graded path-cover flow)

Let \(\nu_s\) be the maximum matching size in \(G_s\).  The maximum number
of edges in a vertex-disjoint directed path cover using only the certified
radius-decreasing arcs is

\[
 \sum_{s\ge1}\nu_s,
\tag{2.2}
\]

and the minimum number of paths is

\[
 \boxed{
 p=W-\sum_{s\ge1}\nu_s
   =c_0+\sum_{s\ge1}\delta_s,}
\tag{2.3}
\]

where

\[
 \boxed{
 \delta_s
 =\max_{X\subseteq V_s}\bigl(|X|-|N_s(X)|\bigr).}
\tag{2.4}
\]

#### Proof

Choose a maximum matching independently in every \(G_s\).  At a vertex in
\(V_s\), the matching in \(G_s\) uses at most one outgoing edge and the
matching in \(G_{s+1}\) uses at most one incoming edge.  Since radius
strictly decreases along every selected edge, their union has no directed
cycle.  It is therefore a vertex-disjoint directed path cover with
\(\sum_s\nu_s\) edges.

Conversely, the edges of any such path cover between \(V_s\) and
\(V_{s-1}\) form a matching in \(G_s\), so there are at most \(\nu_s\) of
them.  This proves (2.2).  A path forest on \(W\) vertices with \(E\) edges
has \(W-E\) components, proving the first equality in (2.3).

Finally, Hall's deficiency form of the integral bipartite matching theorem
gives

\[
 \nu_s=c_s-\max_{X\subseteq V_s}(|X|-|N_s(X)|).
\]

Since \(W=c_0+\sum_{s\ge1}c_s\), the second equality follows. \(\square\)

Equivalently, in the unit-capacity network

\[
 \mathbf s\longrightarrow V_s\longrightarrow V_{s-1}
 \longrightarrow\mathbf t.
\]

the minimum cut has value \(\nu_s=c_s-\delta_s\).  Indeed the cut
associated with \(X\subseteq V_s\) has capacity

\[
 c_s-|X|+|N_s(X)|,
\]

whose minimum is \(c_s-\max_X(|X|-|N_s(X)|)\).

Thus (2.3)--(2.4) are a literal min-cut criterion for the proposed
switching architecture.

### Corollary 2.2 (exact low-barrier criterion)

For a sequence of chosen annular states, a radius-decreasing certified
schedule with \(o(W)\) components exists if and only if

\[
 \boxed{
 \sum_{s\ge1}
 \max_{X\subseteq V_s}\bigl(|X|-|N_s(X)|\bigr)=o(W).}
\tag{2.5}
\]

Indeed \(c_0=2W/(m+2)=o(W)\), so this is immediate from (2.3).  Thus
(2.5), rather than vertexwise outdegree or average compatibility, is the
exact all-cuts switching condition that a noncanonical SCD must meet.

## 3. The universal radius-layer cut

Even the complete-graph relaxation cannot make \(p\) smaller than the
largest radius stratum, because one strictly decreasing path contains at
most one chain of each radius.

The exact stratum formula (0.3) can be written

\[
 \boxed{
 c_s=\binom{2m+1}{m-s}{2(s+1)\over m+s+2}.}
\tag{3.1}
\]

Its consecutive ratio is

\[
 \boxed{
 {c_{s+1}\over c_s}
 ={(m-s)(s+2)\over(s+1)(m+s+3)}.}
\tag{3.2}
\]

Hence \((c_s)\) is unimodal, increasing precisely while

\[
 m-2s^2-6s-3\ge0.
\tag{3.3}
\]

Let \(s_*\) be a maximizing index.  Then

\[
 s_*=\sqrt{m/2}+O(1).
\tag{3.4}
\]

### Theorem 3.1 (complete-relaxation obstruction)

For every certified radius-decreasing switch graph,

\[
 \boxed{p\ge c_{s_*}.}
\tag{3.5}
\]

If every graph \(G_s\) is replaced by the complete bipartite graph, equality
holds:

\[
 p_{\rm complete}=c_{s_*}.
\tag{3.6}
\]

Moreover,

\[
 \boxed{
 c_{s_*}
 =\left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.}
\tag{3.7}
\]

#### Proof

Every path contains at most one vertex of \(V_{s_*}\), proving (3.5).
In the complete relaxation,

\[
 \nu_s=\min(c_s,c_{s-1}),
 \qquad
 \delta_s=(c_s-c_{s-1})_+.
\]

Unimodality makes (2.3) telescope to \(p=c_{s_*}\), proving (3.6).

For \(s=x\sqrt m+O(1)\), the exact central-binomial product gives

\[
 {\binom{2m+1}{m-s}\over W}
 =e^{-x^2+o(1)},
\tag{3.8}
\]

while the second factor in (3.1) is

\[
 {2x+o(1)\over\sqrt m}.
\]

The function \(2xe^{-x^2}\) is maximized at \(x=1/\sqrt2\), with value
\(\sqrt{2/e}\).  Equations (3.4) and (3.8) prove (3.7). \(\square\)

The theorem is independent of the chosen SCD and independent of how many
actual suffix-switch arcs survive the prefix fence.  Any missing arc only
increases the Hall deficiencies \(\delta_s\).

### Proposition 3.2 (cross-grading burden)

Let \(\mathcal P\) be any vertex-disjoint directed path cover of the chains
of one SCD by certified state arcs, with no restriction on the radii of
those arcs.  Write \(p=|\mathcal P|\), and let \(b\) be the number of
selected arcs \(C\to D\) satisfying

\[
 \operatorname {rad}(D)\ge \operatorname {rad}(C).
\tag{3.9}
\]

Then

\[
 \boxed{p+b\ge c_{s_*}.}
\tag{3.10}
\]

In particular, because \(H=A\sqrt m+O(1)\), any path cover with
\(p=o(W/H)\) has

\[
 b\ge
 \left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}.
\tag{3.11}
\]

#### Proof

Delete the \(b\) nondecreasing arcs.  Each deletion increases the number
of path components by one, so the remaining cover has \(p+b\) paths.
Every remaining path has strictly decreasing radii and hence contains at
most one vertex of \(V_{s_*}\).  It takes at least \(c_{s_*}\) such paths
to cover that stratum.  This proves (3.10), and (3.11) follows from
(3.7). \(\square\)

Proposition 3.2 is only a census, not an assertion that the required arcs
exist.  It identifies the exact statewise switching theorem a positive
construction must prove.  Notice also that its lower bound is itself
\(o(W)\); it is compatible with the desired number of exceptional
transitions, but only if those cross-grading transitions are legal
one-update state changes rather than independent Gaussian-size resets.

## 4. The Gaussian reset toll is already linear

The flow obstruction is at the critical component scale.  We now insert
it into the exact state-reset ledger.

Fix

\[
 x_A=\min\{A/2,1/4\},
 \qquad s_0=\lfloor x_A\sqrt m\rfloor.
\tag{4.1}
\]

Then \(s_0<H\) and \(s_0< s_*\) for all sufficiently large \(m\).  From
(3.1) and the same product estimate as (3.8), there is a constant
\(b_A>0\) such that

\[
 c_{s_0}\ge b_A{W\over\sqrt m}.
\tag{4.2}
\]

Every radius-decreasing path cover has at least \(c_{s_0}\) components
whose starting radius is at least \(s_0\): each of the \(c_{s_0}\) chains
in \(V_{s_0}\) lies on a different path, and that path can reach it only
from a radius at least \(s_0\).

An annular state for a chain of starting radius at least \(s_0\) exposes
the consecutive lower ranks

\[
 m-s_0,m-s_0+1,\ldots,m-h-1.
\tag{4.3}
\]

Successive sets in (4.3) differ by one coordinate.  Therefore the ordered
partition contains at least

\[
 s_0-h-1
\tag{4.4}
\]

distinct singleton increment blocks.

### Theorem 4.1 (independent-reset obstruction)

Use the exact component compiler which initializes the prescribed first
state of every path by writing its ordered-partition blocks in reverse, and
then uses one mask per internal certified arc.  Every radius-decreasing
path cover has total initialization excess

\[
 \boxed{
 \sum_{P}(|\Pi_P|-1)=\Omega_A(W).}
\tag{4.5}
\]

This remains true in the complete adjacent-layer relaxation.

#### Proof

For each of the at least \(c_{s_0}\) paths identified above, (4.4) gives

\[
 |\Pi_P|-1\ge s_0-h-1.
\]

Since \(h=o(\sqrt m)\), equations (4.1)--(4.2) yield

\[
 \sum_P(|\Pi_P|-1)
 \ge b_A{W\over\sqrt m}
       (x_A\sqrt m-h-2)
 =\Omega_A(W).
\]

\(\square\)

Thus optimizing the actual Hall cuts in (2.4) cannot close the annulus
inside the independent-reset suffix-switch architecture.  The best
possible component count and the cheapest forced Gaussian first states
already multiply to linear cost.

This theorem does not assert that every way of joining two components costs
their full reset size.  A nonlocal joining word may do useful annular work
while changing the state.  Such useful joins lie outside the independent
reset ledger and are one of the surviving mechanisms listed in Section 0.

In particular, the radius census alone does **not** obstruct an unweighted
\(o(W)\) number of prefix-contaminant joins.  In the complete relaxation
there are only

\[
 p-1=\left(\sqrt{2/e}+o(1)\right){W\over\sqrt m}
\tag{4.6}
\]

component joins.  If every such join admitted a literal bridge of bounded
excess, their aggregate excess would be \(O(W/\sqrt m)=o(W)\).  Thus the
precise surviving local question is whether states can be chosen so that
all but \(o(W/H)\) component joins have \(O(1)\)-excess bridges.  Theorem
4.1 proves only that replacing these bridges by independent state
initializations cannot work.

## 5. Consequence for noncanonical and complementary SCD proposals

The exact min-cut criterion separates what changing the SCD can and cannot
do.

* A noncanonical SCD may enlarge every actual neighborhood \(N_s(X)\) and
  reduce the additional deficiencies beyond the radius cut.
* It cannot change the stratum counts \(c_s\), the lower bound
  \(p\ge\max_sc_s\), or the independent Gaussian reset toll.
* Replacing one SCD by its complementary SCD leaves the same radius counts
  and therefore the same obstruction for every schedule whose useful arcs
  remain strictly radius-decreasing.

Using two decompositions can escape only if a cross-decomposition switch
preserves the inherited state while staying at the same radius or moving to
a larger radius, or if it turns a component join into useful target
coverage.  Merely doubling the catalogue of radius-decreasing candidate
arcs cannot cross the layer cut: one decreasing path still meets each
radius at most once.

This statement concerns schedules which cover the chain list of one SCD
(or the full chain list of each decomposition separately).  It does not
rule out a more flexible two-SCD allocation which chooses only some chains
from each decomposition and thereby changes the selected radius profile.
Such an allocation must additionally prove exact ownership of every
annular target; that ownership problem is outside the present flow model.

Accordingly, the next exact graph is not another adjacent-layer matching.
It must contain state-decorated horizontal/upward arcs.  For chosen states,
the local membership of every such arc is already decided by Lemma 1.1;
the new theorem needed is an expansion or switching theorem for those arcs
which proves that the full decorated graph has a path cover with
\(o(W/H)\) reset components or with useful total reset cost \(o(W)\).

## 6. Status

Proved here:

1. the exact fixed-state annular switching criterion;
2. the exact adjacent-layer max-flow/min-cut formula;
3. the universal radius-layer cut and its sharp Gaussian constant;
4. the sharp cross-grading burden for every arbitrary certified path
   cover; and
5. the \(\Omega_A(W)\) independent-reset obstruction, even under complete
   adjacent-layer compatibility.

Not proved here:

1. abundance of state-composable horizontal or radius-increasing arcs;
2. a useful nonlocal reset compiler;
3. a two-SCD stateful chronology or coefficient one.

The constructive target has therefore narrowed again.  Altering the SCD
can repair prefix fences inside a radius layer interface, but no amount of
such repair changes the Gaussian layer-width cut.  Constant one requires
either bounded-excess joins between the \(\Theta(W/\sqrt m)\) monotone
components or stateful transitions that cross the radius grading.  A
better matching between the same adjacent radius strata alone is not
enough.
