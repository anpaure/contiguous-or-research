# The MNW static annulus is one ordered two-SDR, and the marked `z` seam is automatic

**Date:** 2026-08-07  
**Method:** exact bipartite factorization, terminal-permutation calculus,
and suffix-cylinder substitution; no computation or search  
**Status:** unconditional equivalence/reduction theorem.  It removes the
marked-`z` seam as an independent gate and packages phase, turn, chronology,
and topology into one ordered two-perfect-matching host.  Existing protected
factor and MNW Hamiltonization theorems prove proper projections of this
host statement, but do not yet prove its suffix-cylindrical occurrence.

## 0. Outcome

Let `Z_B` be the four-hex B8 circulation and let its one-step context
annulus carry it from `01` to `10`.  Once the already-audited face order,
boundary mates, spare providers, and socket order are fixed, the remaining
literal host question is exactly this:

> Find two edge-disjoint perfect matchings of the appropriate balanced
> Middle-Levels incidence graph whose union contains the selected annulus
> phase and whose successor permutation contains the prescribed ordered
> socket paths, simultaneously in every Dyck-suffix cylinder.

Equivalently, find one oriented spanning two-factor extending a finite
coloured incidence pattern and realizing a prescribed partial successor
permutation.  This is the promised single static incidence/path-factor
statement.  It contains no dynamic CEGAR or intermediate-deck condition.

There is one further simplification.  The fixed lifted `z` closure is not a
new constraint.  The literal socket transport changes only the two context
coordinates and fixes every base endpoint label.  Context transport and
base complementation commute.  Hence the closure-augmented component
permutation before and after the shell is conjugate.  In particular, a
turn-, chronology-, and ordered-socket-faithful host is automatically
marked-`z`-seam faithful.

The finite B8 upper audit now closes every deck gate after such a host is
given:

* q2 has the exact terminal current already recorded for the carried B8
  packet;
* q3 and q4 lose multiplicity but no support;
* q5 has only gains; and
* every base window of width at least six is full.

Thus the remaining B8 relay obstruction is genuinely the one ordered
two-SDR below.

## 1. Coloured two-factors and the successor permutation

Let

\[
 G=(\mathcal L,\mathcal U;E)
\tag{1.1}
\]

be a balanced bipartite graph.  In the intended application, `G` is the
Middle-Levels containment graph and both shores have the same cardinality.

An **ordered two-SDR** is an ordered pair `(M_0,M_1)` of edge-disjoint
perfect matchings of `G`.  Regard each matching as a bijection

\[
 M_i:\mathcal L\longrightarrow\mathcal U.
\]

Its successor permutation on the lower shore is

\[
 \rho=M_1^{-1}M_0.                                  \tag{1.2}
\]

The union

\[
                         F=M_0\cup M_1              \tag{1.3}
\]

is an oriented spanning two-factor.  Conversely, orienting every component
of a spanning bipartite two-factor and colouring its edges alternately
produces an ordered two-SDR.  The cycles of `rho` are exactly the oriented
components of `F`, after suppressing the upper shore.

Therefore every occurrence-level chronology condition is a partial-word
condition on one permutation `rho`.  In particular, an ordered socket path

\[
                         x_0,x_1,\ldots,x_s          \tag{1.4}
\]

means simply

\[
                         \rho(x_i)=x_{i+1}
                         \quad(0\le i<s),            \tag{1.5}
\]

possibly after globally exchanging `M_0,M_1` on that component.  Multiple
paths are compatible precisely when the prescribed partial successor map
is injective and has no vertex with two prescribed predecessors or two
prescribed successors.

This formulation retains occurrence order.  An uncoloured spanning
two-factor, or two separate perfect matchings with no common orientation,
does not by itself certify (1.5).

## 2. The static annulus pattern

Fix the complete one-step B8 annulus data.  It consists of:

1. the `01` and `10` boundary copies of the four base hexagons;
2. one complementary rail bit at every auxiliary owner and colour;
3. the untouched boundary mate at every affected owner;
4. the two named spare-provider occurrences for the negative B8 q2 terms;
5. the interleaved face order, including the already identified leaf
   endpoint-transfer face; and
6. the ordered exposed sockets of the changed base paths.

For every incidence used by this datum, its required initial status is
forced: selected or unselected.  The selected incidences, together with
their required alternating colours along the oriented paths, form a finite
coloured partial matching pair

\[
                         P=P_0\mathbin{\dot\cup}P_1. \tag{2.1}
\]

The incidences required to be initially unselected form a forbidden bank
`N`.  Let `omega` be the prescribed partial successor map on the socket
and chronology vertices.

Call `(P_0,P_1,N,omega)` the **static annulus pattern**.  All four objects
are occurrence labelled.  Equal set values at different physical
occurrences are not identified.

### Theorem 2.1 (static-host equivalence)

For a fixed suffix fibre, the following are equivalent.

1. The B8 source packet and its `01 -> 10` annulus admit the stated literal
   alternating sweep in one oriented spanning factor, with turn-faithful
   boundary mates and the prescribed ordered socket chronology.
2. There is an ordered two-SDR `(M_0,M_1)` such that

   \[
   P_i\subseteq M_i,\qquad
   (M_0\cup M_1)\cap N=\varnothing,\qquad
   \rho=M_1^{-1}M_0\supseteq\omega.                 \tag{2.2}
   \]

The same equivalence holds simultaneously over a suffix bank when one
ordered two-SDR satisfies the direct sum of the occurrence-labelled
patterns.

#### Proof

Assume 1.  Alternately colour and orient every component of the initial
factor.  The selected annulus incidences receive their actual colours,
giving `P_i subset M_i`; every forbidden incidence is absent.  Reading the
oriented exterior paths between the exposed sockets gives exactly `omega`,
so (2.2) holds.

Conversely, assume 2.  The union `F=M_0 union M_1` is a spanning
two-factor.  Its restriction to the annulus has exactly the required
initial incidence statuses.  The alternating-annulus lemma now applies
face by face: first use the source-boundary operation in the prescribed
interleaving, and then the ordered transport faces.  Every face is
alternating when reached; every auxiliary rail is flipped twice and is
restored; the source boundary returns to its old state; and the destination
boundary receives the B8 packet.  The protected mate incidences give turn
faithfulness.  Finally `rho superset omega` says that the exterior attaches
to the exposed sockets in the prescribed order, so the sweep is
chronology- and socket-faithful.  This is 1.

Suffix fibres have disjoint occurrence supports.  The same argument may be
applied componentwise to their direct sum.  The requirement that one
global ordered two-SDR contain that direct sum is load-bearing: separately
constructed completions in different fibres need not coexist. `square`

### Corollary 2.2 (exact uncoloured factor projection)

Forget the successor constraint and the red/blue labels.  Put

\[
 d_P(v)=\deg_{P_0\cup P_1}(v),\qquad
 b(v)=2-d_P(v),                                      \tag{2.3}
\]

and let

\[
 G_0=G-(P_0\cup P_1)-N.                             \tag{2.4}
\]

There is a spanning two-factor containing the selected bank and avoiding
the forbidden bank if and only if, for every `A subseteq mathcal L`,

\[
 \boxed{
 \sum_{x\in A}b(x)
 \le
 \sum_{U\in\mathcal U}
       \min\{b(U),\,d_{G_0}(U,A)\}.}
\tag{2.5}
\]

#### Proof

After fixing `P_0 union P_1`, the remaining edges must form a bipartite
`b`-factor of `G_0`.  The two shore sums of `b` agree because every fixed
edge has one endpoint on each shore.  Formula (2.5) is the exact
Ore--Ryser criterion for that `b`-factor. `square`

Condition (2.5) closes only the uncoloured degree projection of Theorem
2.1.  It does not force an alternating colouring compatible with the
precoloured edges, nor the partial successor map `omega`.  Those are the
correlated rows of the ordered two-SDR.

## 3. Marked closure is a commuting involution

Let `B` be the abstract endpoint labels of the changed base paths.  Let

\[
                         \iota:B\longrightarrow B    \tag{3.1}
\]

be the fixed endpoint-complement involution.  It reverses each canonical
complementary geodesic and satisfies `iota^2=1`.

There are two context copies

\[
                         E=\{01,10\}\times B.        \tag{3.2}

The literal ordered socket transport is

\[
 \tau(01,b)=(10,b),\qquad
 \tau(10,b)=(01,b).                                 \tag{3.3}

The fixed marked-`z` closure is

\[
 \kappa(01,b)=(10,\iota b),\qquad
 \kappa(10,b)=(01,\iota b).                         \tag{3.4}

Both are fixed-point-free involutions.

### Lemma 3.1 (marked-seam commutation)

The context transport commutes with the fixed closure:

\[
                         \boxed{\tau\kappa=\kappa\tau.} \tag{3.5}

Consequently, if the source socket reconnection is `pi` and the transported
destination reconnection is

\[
                         \pi'=\tau\pi\tau^{-1},      \tag{3.6}

then the closure-augmented monodromies are conjugate:

\[
                         \boxed{
 \kappa\pi'=\tau(\kappa\pi)\tau^{-1}.}              \tag{3.7}

They have identical cycle type and component count.

#### Proof

For either context `s` and every `b in B`, one map changes only the context
coordinate and the other additionally applies `iota` only to the base
label.  Thus

\[
 \tau\kappa(s,b)=(s,\iota b)=\kappa\tau(s,b),
\]

proving (3.5).  Using (3.5) and (3.6),

\[
 \kappa\pi'
 =\kappa\tau\pi\tau^{-1}
 =\tau\kappa\pi\tau^{-1},
\]

which is (3.7).  Conjugate permutations have the same cycle type. `square`

### Corollary 3.2 (no separate marked-`z` gate)

Suppose the B8 annulus host is ordered-socket faithful in the literal sense
of Theorem 2.1: `tau` preserves every base endpoint label and only changes
the `01/10` context.  Then the fixed lifted closure survives with exactly
the same component action.  No additional endpoint matching, Hall cut, or
seam absorber is required.

All annulus and B8 operations lie in the bipartite incidence graph, so they
do not toggle a retained complement/closure edge.  They also preserve the
endpoint set.  Lemma 3.1 proves the only remaining issue, namely compatibility
of the new ordered socket pairing with those retained closure edges.

The hypothesis that base labels are retained is essential.  An arbitrary
unlabelled bijection between equal-size socket banks need not commute with
`kappa` and can change the number of lifted components without changing
any local incidence degree.

## 4. Cylindrical substitution

Let `mathcal D` be a Dyck-suffix family.  For each `v in mathcal D`, let
`j_v` append the fixed suffix up-set to every prefix occurrence.  Distinct
images are vertex-disjoint.

### Lemma 4.1 (suffix-cylinder substitution)

Suppose one global oriented factor contains, for every `v`, the old static
annulus pattern `j_v(P_0,P_1,N,omega)`.  Then the interleaved annulus sweeps
may be performed simultaneously in every suffix fibre.  The output is
again one spanning two-factor.  Its q-deck current is the direct sum of the
contextual base currents, and its marked closure/component action is the
direct sum of the conjugate base actions.

#### Proof

Suffix projection separates all owners, colours, incidences, turns, and
endpoints belonging to distinct fibres.  Therefore the symmetric
differences commute and every local degree is preserved.  The all-width
endpoint-coboundary theorem gives the direct-sum deck statement.  Lemma
3.1 gives the closure statement in each summand. `square`

This lemma is a substitution theorem, not an existence theorem.  A finite
prefix host in one fibre does not imply that one global factor contains its
copy in every suffix fibre.

## 5. Relation to the existing host machinery

The current theorems prove the following strict projections of Theorem
2.1.

1. **One fixed fibre, uncoloured q1 factor.**  If the selected static bank
   has maximum degree at most two and at most `m-2` edges, the small
   protected-factor theorem extends it to a spanning two-factor.  When the
   selected incidences saturate every vertex of the finite face bank, the
   required unselected face incidences are automatically excluded.  In the
   general unsaturated case the exact condition is (2.5).
2. **Canonical marked closure.**  MNW endpoint-augmented Hamiltonization
   preserves every chosen complement edge.  Section 3 proves that the
   annulus socket transport is compatible with that matching.
3. **One protected interval.**  The MNW leaf theorem can preserve one
   prescribed half-path interval in the rethreaded half.  It does not
   preserve a Catalan-size family of independently prescribed annulus
   phases.
4. **One already-prepared finite pull forest.**  The canonical
   prescribed-pull theorem extends a graphic forest of literal canonical
   pull labels.  The transport faces in the present annulus are arbitrary
   incidence hexagons until their literal MNW occurrence/provenance and
   admissible completion bank are supplied.
5. **Abstract ports.**  Preselect-then-complete and the common-cap router
   can protect a fixed or deadline-scale matching bank.  They do not impose
   the partial successor permutation `omega`, and their hypotheses do not
   produce the suffix-cylindrical occurrence bank.

None of these results implies the direct-sum ordered two-SDR of Theorem
2.1.  The number of suffix fibres is Catalan, so the small and polynomial
protected-bank theorems cannot be invoked merely by summing their edges.
The unmodified relay hypertree also fails the required destination phase at
one named incidence in every suffix fibre; the leaf-transfer hex repairs
that incidence locally but does not prove a common global completion.

## 6. Finite recursive-module reduction

The Catalan number of suffix copies does not force a Catalan-size
independent choice.  The MNW recursion exposes isomorphic suffix modules,
so one connector-faithful finite module would tensor to all of them.

The required statement is a general tree-substitution fact.

### Lemma 6.1 (marked recursive subtree substitution)

Let `T` be the ordinary incidence tree of a conflict-free MNW hypertree.
Suppose a family of pairwise vertex-disjoint connected subtrees

\[
                         T_v\qquad(v\in\mathcal D)   \tag{6.1}
\]

meets `T-T_v` in the same labelled terminal set `B_v`.  For every `v`,
replace `T_v` by a tree `T'_v` on the same internal Dyck-root vertices and
the same terminal set, satisfying:

1. `T'_v` induces the same partition of `B_v` (in particular a one-terminal
   subtree remains attached at that terminal);
2. its selected marks are distinct from one another and from all exterior
   marks;
3. its factor rethread has the same oriented terminal/socket signature as
   `T_v`; and
4. `T'_v` is the suffix-labelled copy of one fixed finite module `T'_*`.

Then replacing all `T_v` simultaneously gives another ordinary tree and a
conflict-free MNW rethread.  Every occurrence-labelled property internal to
`T'_*`, including the static annulus pattern, tensors to all suffixes.

#### Proof

Contract every `T_v` to its terminal partition.  Hypothesis 1 says the
contracted exterior graph is unchanged.  Re-expanding with a tree cannot
create a cycle or disconnect the graph, so the resulting incidence graph
is again a tree.  Hypothesis 2 is exactly MNW conflict-freeness.  The
terminal-substitution lemma and hypothesis 3 preserve the exterior factor
chronology.  Finally, distinct suffix projections separate all internal
vertices and marks, so the copies in hypothesis 4 coexist. `square`

### Corollary 6.2 (one finite module is sufficient)

It is sufficient to construct one semilength-five, ten-prefix-bit annulus
module with all of the following finite data:

1. the gamma--alpha relay phase inherited from the modified base tree;
2. the complete interleaved B8 source-plus-transport face bank;
3. the two spare-provider incidences and the protected pivot incidences;
4. an ordered two-SDR realizing the required socket paths;
5. the unchanged marked attachment edges used by every higher MNW
   connector; and
6. the same exported terminal partition as the standard semilength-five
   recursion block.

If that module is a conflict-free tree module in the sense of Lemma 6.1,
then its suffix copies prove the suffix-cylindrical ordered two-SDR theorem
in every larger semilength.

This is a sufficient finite reduction, not a claim that the module exists.
The phase calculations presently in the record specify many of its edges,
but do not yet give the complete ordered two-SDR and inherited connector
interface.

## 7. Exact remaining theorem

The one-prefix prepared-prism lemma is equivalent to the following static
statement.

> **Suffix-cylindrical ordered two-SDR theorem.**  For every sufficiently
> large semilength, the modified gamma--alpha relay factor admits two
> edge-disjoint perfect incidence matchings `(M_0,M_1)` which, in every
> suffix fibre, extend the complete B8 annulus pattern and whose successor
> permutation contains the prescribed ordered socket paths, while avoiding
> the pivot/protected-provider bank.

By Theorem 2.1, this statement supplies the literal interleaved sweep.  By
the finite B8 audits it preserves q2 and all wider upper support.  By Lemma
3.1 it also preserves the marked-`z` seam and the audited `-5` base component
action.  There is no further local deck or closure lemma after it.

The statement remains unproved.  By Corollary 6.2 it can be closed by one
finite connector-faithful ten-bit module, so no independent Catalan-size
selection is intrinsically necessary.  Its unresolved content is not
ordinary factor Hall: it is the existence of that module with the ordered
successor correlation and the exact inherited MNW attachment marks.
Proving only (2.5), or constructing one factor independently in each suffix
fibre, is insufficient.

## 8. Self-audit

1. Every spanning bipartite two-factor decomposes into two edge-disjoint
   perfect matchings by alternating its even cycles; conversely their union
   is a spanning two-factor.
2. Formula (1.2) records the actual cyclic order, so topology is not inferred
   from uncoloured degree data.
3. Ore--Ryser (2.5) is applied only to the residual uncoloured factor and is
   explicitly not promoted to the ordered two-SDR conclusion.
4. The closure involution complements base labels and swaps complementary
   contexts; the socket map swaps contexts and fixes base labels, so (3.5)
   is literal.
5. Suffix copies are disjoint by restriction to their suffix-coordinate
   up-sets, but disjointness of requested patterns does not manufacture one
   global matching pair; this quantifier is retained in Section 6.
6. No statement about residence, the lower common cap, or the all-k
   additive conjecture is inferred from this relay theorem.
7. Lemma 6.1 is invoked only for a genuine subtree module with a declared
   attachment partition.  An arbitrary finite factor on ten coordinates
   does not automatically satisfy that recursive-interface hypothesis.
