# Gap--Hall Pascal recursion for Catalan middle-levels decorations

Date: 2026-07-31  
Status: exact Pascal decomposition, exact block-composition theorem, exact
power-of-two specialization, exact bounded-linkage state, and an exact
three-\(C_{10}\) repair of the first standard \(m=5\) palette obstruction;
an exact all-\(m\) residence-surplus identity, a sharp necessary typed
separated-bank ledger, and a controlled-debt streaming theorem are also
proved.  No all-\(m\) repair/rethread-bank existence theorem is claimed.

## 0. Rebased verdict

Three facts are taken as frozen.

1. A Catalan linear diamond matching is exactly an ordered
   four-transversal

   \[
      L\longmapsto
      \bigl(U_L=L+\{a_L,b_L\},
            T_L=L+a_L,
            H_L=L+b_L\bigr)
   \]

   in which the upper, tail, and head maps are injective and the directed
   graph \(T_L\to H_L\) is acyclic.
2. On one Hamilton cycle of \({\rm ML}(2m-1)\), the corresponding
   sufficient subclass is exactly a pair of turn transversals whose
   physical marks alternate, followed by the forced residual matching and
   the one exact binary-trace forest test.
3. For a fixed upper transversal \(I\), alternation is equivalent to a
   perfect matching in its gap--lower-colour graph. Separate surjectivity
   of the two turn maps is not sufficient: the authenticated \(m=4\)
   example has both turn maps surjective but gap matching number \(20<21\).
   This is an obstruction to that cycle, not to \(m=4\): one standard
   incidence-hexagon toggle produces an explicit decorable
   \({\rm ML}(7)\) cycle with a fourteen-path lift.

The recursive state is therefore not “two rainbow turn words.” The exact
state is

\[
 \boxed{(\hbox{upper occurrence transversal }I,
          \hbox{ gap matching for }\Gamma_I,
          \hbox{ trace boundary state}).}
 \tag{0.1}
\]

This note proves the following advances.

* The ordered four-transversal has an exact Pascal decomposition into two
  rectangular path-forest states and a signed residual inclusion matching.
  This is the correct matching-first induction state.
* Gap--Hall has an exact block-composition rule. If recursive blocks solve
  their internal gaps, only a boundary Hall graph remains.
  In the stronger census-supported state, that graph is built by a
  component-distinct matched-ear order and is therefore a balanced forest
  with a unique, leaf-peelable matching.
* When \(m\) is a power of two and the middle-levels cycle is
  complement-antipodal, the complement-coherent subclass reduces the two
  occurrence systems to one odd-gap transversal on a fundamental
  half-cycle.
* The exact incidence-hexagon transfer theorem turns the block criterion
  into a local recursive target: choose the alternating SDR and the
  gluing tree jointly, with every used hexagon transparent for the carried
  decoration.
* For nontransparent bounded switches, matching repair is exactly a
  directed vertex-disjoint linkage problem of common-deficiency width at
  most \(d+3t\). Bounded adhesion makes that linkage an exact finite tree-DP
  coordinate, but it must be carried jointly with the gap-forest,
  trace/socket/voltage, and deeper compiler states.
* The two canonical private-path bundles persist locally at \(m=5\), but
  the complete unmodified standard family has only \(81/84\) turn colours
  on each shore. In the prepared two-matroid ledger the label deficit is
  zero while the missing-colour preparation deficit is exactly three per
  shore (six in the direct-sum ledger).
* Three pairwise vertex-disjoint \(C_{10}\) switches repair that entire
  \(m=5\) preparation deficit.  The packet has exact common-core linkage
  width thirteen, retains all twelve private ports, and outputs a
  leaf-peelable private state.  It is an atomic debt-carrying preparation
  macro: its first three augmented states have deficiencies \(3,2,1\), so
  it is not a sequence of accepting decorated transitions.
* A colour-injective 42-connector closure of that state covers the complete
  lower/upper flag tower, but every intact-path opening retains 31 internal
  length-two one-runs.  An independently replayed interior rethread changes
  119 matching partners and removes all 31 internal residence defects while
  preserving both immediate palettes and the 42-path forest.  Its remaining
  finite debt is 21 deep targets; a subsequent two-dead-socket theorem
  proves that these fixed path bodies cannot be joined residently by
  endpoint seams alone, so one more interior/socket actuator is necessary.
* For every \(m\), each coordinate has exactly \(\operatorname {Cat}_m\)
  runs in a Catalan path forest and every Johnson seam merges exactly
  \(m-1\).  A cyclic joining therefore has average run length exactly
  \(m\), giving aggregate surplus over the
  \(d+1=\Theta(\sqrt m)\) floor; the all-\(m\) issue is redistribution and
  simultaneous deep/connector compatibility.
* Free and stabilizer-three defect banks obey the exact five-vertices-per-
  rail capacity law (10.5).  Such banks cannot supply the full Pascal
  extreme shell, even with minimal \(C_6\) unit atoms for \(m\ge5\).  At
  the clean subgroup scale, private exclusions are measured by occupied
  \(H\)-orbits, not raw vertices; Proposition 10.1B gives an explicit
  candidate-pressure condition for a disjoint translated bank.
  The controlled-debt streaming theorem permits growing packet length when
  the joint palette/topology/linkage/gap/reachability/residence graph has
  bounded width (or exact bounded-interface block signatures); its live
  boundary stays \(O(w)\).

The ordinary one-port GMM splice does not carry this state. More generally,
copied parent cycles miss an explicit \(Q+R\) extreme-shell bank on each
turn side. Within this decorated middle-levels architecture, the precise
remaining induction lemma is a bulk extreme-shell construction followed by
a controlled-debt palette/residence packet and an ordered fixed-decoration
transparent gluing list.  The packet size may grow; only its live
boundary, matching debt and reachability state must stay bounded.  This is
strictly stronger than ordinary Hamiltonicity or two separate turn
surjections.

Nothing below uses the retracted \(W/2\) Greene--Kleitman projection bound,
and nothing asserts that an arbitrary Catalan linear matching is
middle-levels-resolvable.

## 1. The exact matching-first Pascal state

Let \(\Omega\) have size \(2m-1\), add a new element \(z\), and put

\[
 A=\binom{2m-1}{m-1}=\binom{2m-1}{m},\qquad
 B=\binom{2m-1}{m-2}=\binom{2m-1}{m+1},
 \tag{1.1}
\]

\[
 K=A-B=\operatorname {Cat}_m.
 \tag{1.2}
\]

Consider an ordered four-transversal on the \(2m\)-point set
\(\Omega+z\). Its lower colours have rank \(m-1\), its upper colours have
rank \(m+1\), and its physical directed edges join rank-\(m\) sets.

Split lower and upper colours according to \(z\):

\[
 \begin{array}{c|c|c}
 &z\notin&z\in\\ \hline
 \text{lower}&\binom\Omega{m-1}\ (A)&
                z+\binom\Omega{m-2}\ (B)\\
 \text{upper}&\binom\Omega{m+1}\ (B)&
                z+\binom\Omega m\ (A).
 \end{array}
 \tag{1.3}
\]

Containment permits three and only three diamond types:

* an internal \(0\)-diamond, from a \(z\)-free lower colour to a \(z\)-free
  upper colour;
* an internal \(1\)-diamond, from a \(z\)-containing lower colour to a
  \(z\)-containing upper colour;
* a cross diamond

  \[
                  L\subset z+S,\qquad S=L+c,
  \tag{1.4}
  \]

  where \(L\in\binom\Omega{m-1}\) and \(S\in\binom\Omega m\).

There is no reverse cross type because a lower colour containing \(z\)
cannot lie in an upper colour avoiding \(z\).

### Theorem 1.1 (exact rectangular Pascal decomposition)

An ordered four-transversal on \(\Omega+z\) is equivalent to the following
data.

1. A directed acyclic path forest \(F_0\) with \(B\) edges on the \(A\)
   vertices \(\binom\Omega m\). Its edges use every \(z\)-free upper colour
   exactly once, use \(B\) distinct \(z\)-free lower colours, and have
   injective tails and heads.
2. A directed acyclic path forest \(F_1\) with \(B\) edges on the \(A\)
   vertices \(\binom\Omega{m-1}\). It is obtained from the
   \(z\)-containing physical rail by deleting \(z\); its edges use every
   \(z\)-containing lower colour exactly once, use \(B\) distinct
   \(z\)-containing upper colours, and have injective tails and heads.
3. Residual banks

   \[
       \mathcal R_L\subseteq\binom\Omega{m-1},\qquad
       \mathcal R_S\subseteq\binom\Omega m,\qquad
       |\mathcal R_L|=|\mathcal R_S|=K,
   \tag{1.5}
   \]

   consisting respectively of the lower colours unused by \(F_0\) and the
   old-coordinate parts of the upper colours unused by \(F_1\), and a
   perfect matching

   \[
                       L\longmapsto S=L+c
   \tag{1.6}
   \]

   in the one-step inclusion graph between these banks.
4. For every pair \(L\subset S\) in (1.6), one of the two signs

   \[
              S\longrightarrow z+L,\qquad
              z+L\longrightarrow S,                 \tag{1.7}
   \]

   subject to the exact port conditions

   \[
   \begin{array}{ll}
   S\to z+L:& S\text{ is not a tail of }F_0,
               \quad L\text{ is not a head of }F_1,\\
   z+L\to S:& L\text{ is not a tail of }F_1,
               \quad S\text{ is not a head of }F_0.
   \end{array}                                      \tag{1.8}
   \]
5. After contracting every path component of \(F_0\cup F_1\), the \(K\)
   signed cross arcs (1.7) form no directed cycle.

Each \(F_i\) has exactly \(K\) path components, with isolated vertices
allowed. Under the equivalence, the union of the two forests and the cross
arcs is the physical lift of the four-transversal and has exactly \(K\)
path components.

#### Proof

Every \(z\)-free upper colour must be matched from a \(z\)-free lower
colour, so there are exactly \(B\) internal \(0\)-diamonds. Every
\(z\)-containing lower colour must be matched to a \(z\)-containing upper
colour, so there are exactly \(B\) internal \(1\)-diamonds. The remaining
\(A-B=K\) lower and upper colours must be paired by cross diamonds, and
containment forces (1.4). This proves the palette split and (1.5)--(1.6).

The tail and head maps of the global ordered four-transversal restrict to
injective tail and head maps on both internal rails. Its acyclicity
restricts to acyclicity of both internal graphs. Thus each \(F_i\) is a
directed graph with indegree and outdegree at most one and no directed
cycle, hence a path forest. It has \(A-B=K\) components by Euler's
identity.

A cross diamond has the two physical middle states \(S=L+c\) and \(z+L\).
The orientation of that physical edge is exactly one of (1.7). Global
tail/head injectivity is exactly (1.8), because (1.6) already makes all
cross sources and destinations distinct within their own types.

Finally, after adding arcs between two path forests, an undirected cycle
would have indegree and outdegree one at every one of its vertices and
would therefore be a directed cycle. Such a cycle exists exactly when it
survives after contracting the old path components. This proves condition
5 and necessity.

Conversely, data 1--5 use every lower and upper colour once, respect both
middle port capacities, and have no cycle. Expanding each signed cross arc
to its unique diamond recovers an ordered four-transversal. Its edge count
is

\[
                  2B+K=2A-K,
\]

on \(2A\) middle vertices, so the resulting forest has \(K\) components.
\(\square\)

### Consequence 1.2

A balanced \({\rm CLM}(m-1)\) object is not a closed induction state. The
two parents in Theorem 1.1 are rectangular partial four-transversals; one
must carry their residual colour banks, their unused tail and head ports,
and the start--end pairing of every path component. Palette Hall alone is
insufficient: a cross edge can hit a saturated directed port, and
port-compatible cross edges can still close a cycle.

This theorem is matching-first. It does not say that the resulting object
is supported by one middle-levels Hamilton cycle.

## 2. Exact block composition of the gap matching

Now fix a Hamilton cycle

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
 \tag{2.1}
\]

of \({\rm ML}(2m-1)\), and fix an upper-turn transversal \(I\) of size
\(P\). Its marked \(A\)-positions create \(P\) cyclic gaps of \(B\)-turn
positions. Let \(\Gamma_I\) be the authoritative gap--lower-colour graph.

Partition (2.1) cyclically into \(b\) oriented blocks, each containing at
least one mark from \(I\). Blocks with no mark may simply be merged with a
neighbour. There are two kinds of \(I\)-gaps:

* an **internal gap**, whose two endpoint \(A\)-marks lie in the same
  block;
* a **bridge gap**, running from the final \(A\)-mark of one block through
  a seam to the first \(A\)-mark of the next block.

There are exactly \(P-b\) internal gaps and \(b\) bridge gaps.

### Theorem 2.1 (gap--Hall block-composition theorem)

Suppose the recursive block data contain an injective assignment
\(\mu_{\rm int}\) of one occurring lower colour to every internal gap.
Let \(\mathcal D\) be the \(b\) lower colours not used by
\(\mu_{\rm int}\). Form the boundary graph

\[
 H_{\partial}=H_{\partial}(I,\mu_{\rm int})
 \tag{2.2}
\]

whose left shore is the \(b\) bridge gaps, whose right shore is
\(\mathcal D\), and where a bridge gap is adjacent to a colour precisely
when that colour has an occurrence in the gap.

Then \(\mu_{\rm int}\) extends to alternating bijective lower-turn
representatives if and only if \(H_{\partial}\) has a perfect matching.
Equivalently,

\[
       |N_{H_{\partial}}(\mathcal S)|\ge |\mathcal S|
       \quad\text{for every family of bridge gaps }\mathcal S.
 \tag{2.3}
\]

#### Proof

The internal and bridge gaps partition the left shore of \(\Gamma_I\).
The fixed internal assignment consumes \(P-b\) distinct colours, leaving
exactly \(b\). Any extension of it is therefore exactly a perfect matching
between the bridge gaps and the residual colours, using occurrences in
those gaps. This is (2.2), and (2.3) is Hall's theorem. \(\square\)

### Corollary 2.2 (private boundary sockets)

If every bridge gap contains a designated residual lower colour and the
designated colours are pairwise distinct, then the blocks compose. More
generally, the degree-spread or circular-interval criteria from the frozen
gap--Hall theorem may be applied only to the \(b\)-by-\(b\) boundary graph,
after the recursive internal matchings have been fixed.

This is the useful recursive localization. It replaces a global
\(P\)-by-\(P\) occurrence problem by internal child certificates and one
boundary Hall problem. The \(m=4\) counterexample proves that this boundary
state cannot be discarded: its three forced upper marks create two
singleton gaps carrying the same lower colour. The authenticated hexagon
repair proves the complementary positive fact: the gap graph can change
from deficient to feasible under one standard Middle Levels toggle.

### Theorem 2.3 (transparent-hex transfer, recursive form)

Let a standard Boolean-incidence hexagon replace one alternating
three-edge matching by the other in a middle-levels factor. Fix selected
turn occurrences before the toggle. The same selected occurrences remain
a decoration after the toggle if and only if:

1. the selected local turn-colour multisets agree before and after,
   separately on the two shores; and
2. after reconnection, the first and last selected shore types on each of
   the three retained path fragments alternate across all new seams.

If a trace breaker disjoint from the six ports is retained, linearity is
also preserved.

#### Proof

Only the neighbour pairs at the six hexagon vertices change, so the two
global colour bijections survive exactly when the two selected local
multisets survive. Inside each retained fragment the selected shore types
already alternate, and reversal preserves alternation. Thus only the new
fragment boundaries need to be tested, giving condition 2. A protected
trace breaker invokes Lemma 3.1. \(\square\)

The theorem is about a decoration and a toggle jointly. It does not say
that an arbitrary frozen decoration survives an arbitrary gluing tree. In
the complete \(m=4\) census, 16 hexagons preserve Hamiltonicity, 10 outputs
are decorable, but only 6 toggles have a decoration common to both sides.
Those six are the literal transparent local atoms.

### Corollary 2.4 (transparent alternating-polygon transfer)

The same criterion holds for any alternating even cycle \(Z\) whose old
perfect matching lies in the factor and is replaced by the complementary
perfect matching. Use equality of selected local turn-colour multisets on
the two shores, and impose opposite last/first selected shore types across
every new retained-fragment seam.

#### Proof

Exactly as in Theorem 2.3, only neighbour pairs at vertices of \(Z\)
change. Deleting the old matching leaves retained alternating paths;
alternation is already valid inside each path, including after reversal.
Thus palette equality and the new boundary pairs are respectively
necessary and sufficient. \(\square\)

For a flipping square in a larger cube-level factor this is a
two-fragment/four-port rule; for an incidence hexagon it is the
three-fragment/six-port rule above. The strict middle-levels incidence
graph has no \(4\)-cycle, so its first literal local case is the hexagon.
The same decorated transition relation nevertheless applies to every
available alternating switch polygon.

We will use the following elementary equivalence repeatedly. A balanced
bipartite forest with a perfect matching has a unique perfect matching and
is leaf-peelable: a nonempty forest has a leaf, its incident edge is forced,
and deleting the two matched endpoints leaves another forest with a perfect
matching. Conversely, two distinct perfect matchings would have an
alternating cycle in their symmetric difference.

### Lemma 2.5 (matched-ear extension of a gap forest)

Let \(F\) be a balanced bipartite forest with perfect matching \(M\). Add
one new vertex \(v\) on either shore and one new vertex \(w\) on the other
shore. Suppose:

1. \(v\) is adjacent only to \(w\); and
2. apart from \(v\), the neighbours of \(w\) lie in pairwise distinct
   components of \(F\).

Then

\[
                        F'=F+\{v,w\}
 \tag{2.4}
\]

with all declared edges incident to \(w\) is a balanced forest, and its
unique perfect matching is \(M\cup\{vw\}\).

Conversely, if \(F'\) is a forest with a perfect matching, \(v\) is a leaf,
and \(vw\) is its matching edge, then \(F'-\{v,w\}\) is a balanced forest
with a perfect matching and the other neighbours of \(w\) lie in distinct
components of that residual forest.

#### Proof

The leaf \(v\) forces \(vw\) in every perfect matching. Removing \(v,w\)
therefore leaves \(M\), and adding them preserves balance. Joining \(w\) to
at most one vertex in each old tree component connects distinct trees
through a new star and cannot create a cycle. This proves the forward
direction and uniqueness.

Conversely, two neighbours of \(w\) in the same residual tree would be
joined there by a path; together with their two edges to \(w\) this would
make a cycle in \(F'\). The matching restriction covers every remaining
vertex. \(\square\)

Iterating Lemma 2.5 is exactly reverse leaf deletion. It is stronger than
the existence of an arbitrary perfect matching and gives a deterministic
matching certificate.

### Theorem 2.6 (exact leaf-transparent switch test)

Let a decoration have balanced gap--colour forest \(\Gamma\), and let an
alternating polygon toggle satisfy Corollary 2.4 for that decoration. Label
each gap vertex by its preceding physical selected \(A\)-vertex in the
carried orientation; this keeps the gap and colour vertex sets fixed across
the toggle. The orientation is part of the switch state. Let \(\Gamma'\)
be the new **simple support** gap--colour graph: \(gL\) is one edge iff
colour \(L\) has at least one occurrence in gap \(g\), with repeated
occurrences coalesced. Put

\[
 E^- =E(\Gamma)\setminus E(\Gamma'),\qquad
 E^+ =E(\Gamma')\setminus E(\Gamma).                 \tag{2.5}
\]

Delete \(E^-\) from \(\Gamma\), contract each resulting tree component,
and retain one quotient edge for every distinct support edge in \(E^+\).
Then \(\Gamma'\) is a balanced forest with its unique perfect matching if
and only if that quotient multigraph is loopless and acyclic. Two distinct
gained support edges joining the same contracted components are parallel
quotient edges and form a genuine two-cycle.

#### Proof

Decoration transparency supplies a perfect matching of \(\Gamma'\): every
new gap contains exactly one selected lower representative and all its
colours are distinct. The graph \(\Gamma-E^-\) is a forest. Adding \(E^+\)
preserves acyclicity exactly when no new edge lies inside one old component
and the component-level attachment graph has no cycle. This is precisely
the loopless/acyclic contraction test. A forest has at most one perfect
matching, so the transparent matching is then unique and Lemma 2.5 peels
it. The converse is the graphic-matroid contraction criterion. \(\square\)

Transparency alone does not imply Theorem 2.6. The six positive
\(m=4\) transparent hexagons each have at least one common decoration for
which the test passes on both sides, but that finite fact is not an
all-\(m\) preservation theorem.

There is also an exact bounded-width state for a nontransparent switch.
For a supplied middle-levels factor \(C\), let \(\mathcal A_C\) be the
frozen augmented bipartite trace graph whose perfect matchings are exactly
alternating turn decorations. Its three edge types are physical-incidence,
upper-turn, and lower-turn edges.

### Theorem 2.7 (finite-width common-core linkage)

Let \(C'\) be obtained from \(C\) by a factor-safe alternating
\(2t\)-circuit, meaning that the toggle preserves the required physical
degree conditions but need not yet produce one Hamilton component. Put

\[
  N=|\text{one shore of }\mathcal A_C|,\qquad
  d=N-\nu(\mathcal A_C),\qquad
  H=\mathcal A_C\cap\mathcal A_{C'},
  \tag{2.6}
\]

and let

\[
                         r=N-\nu(H).                 \tag{2.7}
\]

Then

\[
                         r\le d+3t.                 \tag{2.8}
\]

For a maximum matching \(M\) of \(H\), the new factor \(C'\) is decorable
if and only if \(\mathcal A_{C'}\) contains \(r\) pairwise vertex-disjoint
\(M\)-augmenting paths which cover all \(2r\) vertices exposed by \(M\).
Thus a switch from a decorated parent has an exact augmenting-linkage
common-deficiency width at most \(3t\), equivalently at most \(3t\)
unpaired terminals on each shore.

#### Proof

The \(2t\)-circuit deletes at most \(t\) old physical-incidence edges, at
most \(t\) old upper-turn edges, and at most \(t\) old lower-turn edges of
the augmented graph. Restrict a maximum matching of \(\mathcal A_C\), of
size \(N-d\), to \(H\). At most \(3t\) of its edges disappear, so

\[
                 \nu(H)\ge N-d-3t,
\]

which is (2.8).

If \(P\) is a perfect matching of \(\mathcal A_{C'}\), the symmetric
difference \(M\triangle P\) contains exactly \(r\) vertex-disjoint
augmenting paths whose endpoints are the vertices exposed by \(M\), plus
alternating cycles. Conversely, toggling any such complete augmenting
linkage increases the matching size by \(r\) and gives a perfect matching.
\(\square\)

The “width” in Theorem 2.7 is the common deficiency \(r\): there are
\(r\) unpaired exposed terminals on each shore, hence \(2r\) terminal
vertices in total. The augmenting paths choose their pairing; the
terminals are not supplied as prepaired pairs. This width is bounded for a
bounded switch, but the
augmenting paths may traverse the entire augmented graph. Consequently
finite width is not a locality theorem. Any recursive use must additionally
verify the output trace breaker, gap-forest state, and physical socket
labels, or constrain both the physical circuit collar and the linkage
symmetric-difference support to avoid their protected occurrences.

Bounded adhesion supplies the exact extra hypothesis under which this
global linkage becomes a finite recursive state. Orient unmatched
bipartite edges left-to-right and matching edges right-to-left.

### Theorem 2.8 (exact bounded-adhesion linkage composition)

Suppose this directed augmentation graph is decomposed into blocks with
disjoint interiors, glued along a tree. After including the exposed
source/sink terminals in the relevant bags, suppose every boundary state
has size at most \(a\). For each block record every realizable collection of
vertex-disjoint directed path fragments whose endpoints are exposed
terminals or boundary vertices, including orientations and the used
boundary vertices.

The linkage signature of the union is obtained exactly by joining child
patterns and rejecting:

1. repeated use of a boundary vertex;
2. an internal directed cycle; or
3. an illegal source/sink orientation.

The number of possible endpoint patterns is \(2^{O(a\log a)}\), so complete
augmenting linkage is decidable by an exact finite-state tree dynamic
program when \(a\) is bounded.

#### Proof

Restrict any global vertex-disjoint linkage to the blocks. Cutting its
paths at adhesion vertices produces one recorded oriented pattern per
block, and disjointness gives conditions 1--3. Conversely, compatible
child fragments join through their identified adhesion vertices. Those
three conditions make their union a collection of vertex-disjoint directed
paths with the required exposed endpoints. Induction over the block tree
proves necessity and sufficiency. The pattern count is the number of
oriented partial pairings/terminal labels on \(O(a)\) boundary vertices.
\(\square\)

Without bounded adhesion, Theorem 2.7 gives bounded exposed-terminal width
but not a local recursion. With bounded adhesion, Theorem 2.8 gives an
exact finite linkage coordinate. It remains only one coordinate: the
gap-forest connectivity partition, trace/socket data, voltage, and deeper
shadow/compiler guards must be carried alongside it.

## 3. A composable topology guard

Once the marks alternate, the residual cross matching is forced. The
physical lift fails to be a forest only on the exact binary face

\[
  \text{every zero-run has length }2,
  \qquad
  \text{every one-run has odd length}.               \tag{3.1}
\]

### Lemma 3.1 (protected four-zero socket)

Suppose one recursive block contains four consecutive physical
middle-levels positions that are unmarked, and every later glue operation
preserves their adjacency and never selects a representative at one of
them. Then the final decorated lift is a spanning \(K\)-path forest.

#### Proof

Those four positions lie in a maximal zero-run of length at least four.
This violates the first condition in (3.1), independently of every other
run. The exact binary-trace theorem then gives a spanning linear forest.
\(\square\)

Thus a recursion may carry one protected \(0^4\) socket rather than the
entire topology. Without such a socket, the exact trace boundary state is
still finite: boundary zero-run lengths need to be retained with cap
\(0,1,2,3,4+\), boundary one-runs need their parity, and one bit records an
already witnessed violation of (3.1). The protected socket is a stronger
but cleaner sufficient invariant.

## 4. The exact Pascal shell that copied parents miss

The usual semilength step \(m\mapsto m+1\) adds two coordinates \(x,y\) to
an old ground set \(\Omega\) of size \(2m-1\). Put

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 R=\binom{2m-1}{m-3},                                \tag{4.1}
\]

with \(R=0\) when the lower index is negative.

The lower turn colours at semilength \(m+1\) have rank \(m-1\). Splitting
by the number \(t\) of new coordinates gives banks of sizes

\[
                 |\mathcal L_0|=Q,\qquad
                 |\mathcal L_1|=2P,\qquad
                 |\mathcal L_2|=R.                  \tag{4.2}
\]

The upper turn colours have rank \(m+2\), and their bank sizes are

\[
                 |\mathcal U_0|=R,\qquad
                 |\mathcal U_1|=2P,\qquad
                 |\mathcal U_2|=Q.                  \tag{4.3}
\]

Complementation pairs \(\mathcal L_t\) with \(\mathcal U_{2-t}\).
Two coordinate-tagged copies of a decorated parent can directly represent
only the mixed banks \(\mathcal L_1,\mathcal U_1\). The extreme banks have
exact size

\[
                       Q+R                           \tag{4.4}
\]

on each turn side.

### Theorem 4.1 (extreme-shell support lower bound)

Consider a recursive architecture whose initial selected occurrences are
only the two tagged copies of parent selected occurrences. Suppose every
additional glue collar \(C_\alpha\) changes at most
\(c^-_\alpha\) lower-turn positions and at most \(c^+_\alpha\) upper-turn
positions. If the final cycle is turn-surjective on both sides, then

\[
        \sum_\alpha c^-_\alpha\ge Q+R,
        \qquad
        \sum_\alpha c^+_\alpha\ge Q+R.               \tag{4.5}
\]

In particular, if each of \(g\) collars changes at most \(c\) positions on
either turn side, then

\[
                       g\ge\left\lceil\frac{Q+R}{c}\right\rceil.
 \tag{4.6}
\]

#### Proof

No copied parent occurrence has an extreme-shell colour: its old turn
colour acquires exactly one of \(x,y\). Every one of the \(Q+R\) colours
in (4.4) therefore needs a selected occurrence at a turn position changed
or newly created by a collar. One turn position can represent at most one
colour. Summing the collar supports proves (4.5), and (4.6) follows.
\(\square\)

This is deliberately scoped. An auxiliary Pascal path system may already
populate extreme-shell colours, in which case it is part of the recursive
input rather than a glue correction. What (4.5) rules out is a recursion
made only from copied decorated parents and boundedly many local repairs.

The leaf-peelable state determines the exact stronger router size in the
**clean copied-mark template**. Write

\[
                         P^+=Q+2P+R                  \tag{4.7}
\]

for the new number of colours on either turn side. Start with two tagged
parent decorations whose gap graphs are balanced forests, retain all
\(2P\) selected mixed-bank upper occurrences with their colours, and cut
them into a total of \(b\) nonempty marked blocks. Require the \(b\) block
boundaries to destroy exactly \(b\) distinct old gaps and no additional
internal parent gap. At every cut delete that old closing gap and its
uniquely matched lower colour. The retained parent core has

\[
                         2P-b                       \tag{4.8}
\]

gap--colour pairs. It is still a balanced forest with its restricted unique
matching.

The child therefore has exactly

\[
                  s=P^+-(2P-b)=Q+R+b               \tag{4.9}
\]

router vertices on each shore. Their shores have forced types:

\[
\begin{array}{c|c}
\text{router gap vertices}&
  Q+R\text{ gaps following extreme-shell upper marks}
  \;+\;b\text{ bridge gaps},\\
\text{router colour vertices}&
  Q+R\text{ extreme-shell lower colours}
  \;+\;b\text{ released mixed lower colours}.
\end{array}                                         \tag{4.10}
\]

Thus \(Q+R\) is the palette deficit, while \(Q+R+b\) is the exact number
of leaf-router vertices per shore after opening \(b\) parent blocks in this
template. Pairing those two shores is an additional exterior-router
condition in Theorem 4.2, not a consequence of the count.

In the minimal two-parent/two-block splice, \(b=2\), so the exact bank is
\(Q+R+2\) vertices per shore, not \(Q+R\): the two extras are the two
bridge gaps on one shore and the two mixed lower colours released from the
parent closing gaps on the other. For \(m=4\to5\), this is
\(35+7+2=44\) router vertices on each shore.

The chronology-free identity is slightly more general. If exactly \(c\)
matched parent gap--colour pairs literally survive in the child core, then

\[
                       s=P^+-c.                      \tag{4.11}
\]

If \(d\) parent pairs are destroyed and all \(2P\) copied mixed upper
colours survive, then \(c=2P-d\) and \(s=Q+R+d\). Therefore
\(Q+R+b\) is the sharp minimal count for \(b\) clean block boundaries, not
a necessity for an arbitrary Pascal braid. A collar which changes another
selected parent turn or splits another retained gap must charge the
additional loss through (4.11).

### Theorem 4.2 (exact exterior leaf-router criterion)

Assume the **core-forest condition**: after the child chronology is formed,
the simple support gap graph induced by the retained parent gap and colour
vertices is a balanced forest covered by the restricted parent matching.
Strict core separation--equality with the disjoint union of the opened
parent cores--is a convenient sufficient special case, but is not
necessary.

Under this condition, the child gap graph is an exterior leaf extension of
the retained core if and only if its \(s=P^+-c\) router gap vertices can be
perfectly paired with its \(s\) router colour vertices by actual occurrence
edges and ordered so that, in reverse construction order:

1. relative to the graph present immediately after that pair is added, one
   endpoint is a leaf, adjacent only to its mate; and
2. the mate's other occurrence edges meet pairwise distinct components of
   the graph already constructed.

All simple support edges whose two endpoints are present at a stage are
included; repeated occurrences do not create parallel graph edges. Edges
to a router pair not yet added are checked when that later pair is
introduced.

Every such router produces a balanced gap forest with a unique perfect
matching. Conversely, every balanced child gap forest whose router pairs
can all be peeled before any core vertex has exactly such an ordering.

#### Proof

The general count is (4.11); in the clean copied-mark template the banks
are exactly (4.9)--(4.10). The retained core is a forest with a perfect
matching by hypothesis, hence that matching is unique. Starting from this
core, apply Lemma 2.5 once for every router pair in the stated reverse
order. Each step preserves a forest and extends its unique perfect matching
by the new leaf edge.

Conversely, reverse an exterior peeling order in the child forest. At each
step the peeled leaf forces its matching edge. Lemma 2.5 says that its mate
has at most one neighbour in each residual component. After all router
pairs are removed, the core-forest condition leaves the declared retained
core. \(\square\)

The theorem exposes two independent failure modes for a proposed Pascal
router:

* a **core collision**, where the induced retained core ceases to be a
  forest or loses the restricted perfect matching; or
* an **ear collision**, where the mate of a forced leaf has two occurrence
  edges into one current tree component.

Either collision can hold even when ordinary Hall succeeds. Therefore the
extreme-shell router needed by the leaf invariant is not merely an
arbitrary pairing of the \(Q+R+b\) vertices on each shore in the clean
template; it is a component-distinct matched-ear ordering on the literal
support graph.

The published one-port adjacent-level splice is therefore not the required
decorated recursion. The separate exact sector audit gives its sharper
\(\operatorname {Cat}_m-1\) distinguished-block deficiency. The global
Middle Levels constructions do use extensive factor modifications, but
their Hamiltonicity and connectivity statements do not assert
(4.2)--(4.3), gap--Hall, or the trace guard. They are possible substrates
for a bulk router, not proofs of one.

## 5. The exact recursive closure target

The preceding results give a concrete sufficient induction statement.
To avoid confusing parent and child palette sizes, write

\[
                  P_r=\binom{2r-1}{r-2}             \tag{5.1}
\]

for the turn-palette size at the target semilength \(r\). In the Pascal
step of Section 4, \(r=m+1\) and \(P_r=P^+=Q+2P+R\).

### Definition 5.1 (bulk Pascal gap router, \({\rm BPGR}(r)\))

A \({\rm BPGR}(r)\) certificate is a cyclic family of oriented
middle-levels blocks which, after the prescribed GMM/Pascal glues, has:

1. one occurrence of every target upper turn colour; in a Pascal step,
   this represents all three banks in (4.3);
2. an internal gap matching in every block, the internal assignments being
   colour-disjoint and together using exactly \(P_r-b\) lower colours, where
   \(b\) is the number of blocks;
3. a perfect matching in the boundary graph (2.2), using the remaining
   target lower colours; in a Pascal step, these include all three banks in
   (4.2);
4. one protected \(0^4\) socket disjoint from all glue collars; and
5. a single Hamilton middle-levels chronology after the glues.

### Theorem 5.2 (bulk-router closure)

For every \(r\), \({\rm BPGR}(r)\) produces a Catalan decoration whose
physical lift is a spanning \(\operatorname {Cat}_r\)-path forest. Hence it
solves the ordered-four-transversal integral-correlation gate inside the
middle-levels-resolvable subclass.

#### Proof

Condition 1 is the upper-turn bijection. Conditions 2 and 3 and Theorem
2.1 give the alternating lower-turn bijection. Once the marks alternate,
the residual matching is forced by the decorated-cycle equivalence.
Condition 4 and Lemma 3.1 give a forest, and its component count is
\(\operatorname {Cat}_r\). Condition 5 supplies the literal common
middle-levels support. \(\square\)

Relative to the published cycle-factor proof, the strengthened auxiliary
problem is now explicit. Ordinary connectivity of the flip graph must be
replaced by a choice of Hamiltonizing flips whose induced block order has a
perfect residual boundary gap graph. This is a coloured spanning-tree/
occurrence-Hall assertion. The \(m=4\) counterexample shows that ordinary
connectivity plus both marginal rainbows cannot imply it.

### Definition 5.3 (leaf-\({\rm BPGR}(m+1)\) from semilength \(m\))

A leaf-\({\rm BPGR}(m+1)\) certificate over the Pascal step of Section 4
is a \({\rm BPGR}(m+1)\) certificate in the clean copied-mark template,
whose two tagged semilength-\(m\) parent gap graphs are balanced forests and whose
\(Q+R+b\) shell/bridge vertices on each shore are paired by an exterior
leaf router satisfying
Theorem 4.2. Equivalently, it carries an explicit matched-leaf deletion
order down to the two opened parent cores.

### Theorem 5.4 (leaf-router closure)

A leaf-\({\rm BPGR}(m+1)\) certificate satisfies the boundary Hall condition
with a unique perfect matching. Its full gap--colour graph is a balanced
forest, and the lower occurrence SDR is recovered deterministically by the
declared leaf order.

#### Proof

Theorem 4.2 builds the full child gap graph from the opened parent forests
by component-distinct matched-ear extensions. Lemma 2.5 preserves a forest
and extends its unique matching at every step. Therefore the resulting
matching is perfect and unique, so it in particular discharges every Hall
cut in Definition 5.1. \(\square\)

Thus leaf-\({\rm BPGR}\) replaces the arbitrary boundary Hall oracle by a
linear-size proof object: the router pairing, its leaf side at every step,
and the component labels hit by the mate's other occurrence edges.

### Corollary 5.5 (exact decorated spanning-tree criterion)

Let a middle-levels cycle factor have \(b\) components. Cut each component
once and include every changed turn position of its eventual flip collars
in the resulting oriented block. Suppose that, after those collar turns
are evaluated literally,

* the block upper representatives form one global upper-colour
  transversal;
* the block-internal gaps have colour-disjoint lower assignments, using
  \(P_r-b\) lower colours; and
* one protected four-zero socket survives.

For any pairwise noninterfering flip set \(T\) which merges the factor to
one Hamilton cycle, let \(H_\partial(T)\) be the boundary graph of the
induced cyclic block order. Then the declared upper representatives and
block-internal lower assignments extend along \(T\) to a Catalan
linear-forest decoration if and only if \(H_\partial(T)\) has a perfect
matching.

#### Proof

The flip set fixes the cyclic order and orientation of the \(b\) blocks,
and hence fixes their \(b\) bridge gaps. All other gaps already have
distinct lower representatives. Theorem 2.1 makes perfect matching of
\(H_\partial(T)\) necessary and sufficient for alternation. The protected
socket then invokes Lemma 3.1. \(\square\)

Thus the published auxiliary-graph step has an exact coloured
strengthening: choose a spanning tree of noninterfering flips not merely
for connectivity, but from the subfamily whose induced boundary graph
passes every Hall cut. This is finite and literal for each factor. What is
not yet proved is that the GMM factor always has such a tree, or that its
recursive shell blocks can be decorated as required.

Corollary 5.5 is a final-cycle criterion. For a fixed internal assignment
its boundary test is exact; existence for a supplied \(T\) quantifies
jointly over the internal assignment and the resulting boundary matching.
A genuinely recursive sufficient state is stronger.

### Definition 5.6 (leaf-transparent \({\rm BPGR}(r)\) state)

A leaf-transparent \({\rm BPGR}(r)\) state consists of

1. an oriented middle-levels factor with one global pair of turn-colour
   transversals, alternating on every factor cycle, whose global
   gap--colour graph is a balanced forest;
2. one protected trace breaker whose adjacency and mark status are
   preserved by every switch;
3. a spanning tree of pairwise noninterfering alternating switch cycles
   available in the factor (in strict middle levels, incidence hexagons
   and possibly longer alternating cycles);
4. an ordering of that tree's toggles such that every toggle satisfies
   Corollary 2.4 for the same carried decoration at the moment it is used
   and joins exactly two distinct current factor components without
   splitting any component, and hence
   \[
             \kappa(F_{\rm after})=\kappa(F_{\rm before})-1;
   \]
5. every toggle passes the contraction-forest test of Theorem 2.6.

The selected occurrences and the gluing tree are part of one certificate.

### Theorem 5.7 (leaf-transparent gluing-tree closure)

Every leaf-transparent \({\rm BPGR}(r)\) state yields a Hamilton middle-levels
cycle with a Catalan decoration and a spanning
\(\operatorname {Cat}_r\)-path lift. Its final gap--colour graph remains a
balanced forest with a unique, leaf-peelable perfect matching.

#### Proof

Induct along the ordered tree toggles. Corollary 2.4 preserves both colour
bijections and alternation at every step. Theorem 2.6 preserves the
gap--colour forest and therefore its unique leaf-peelable matching. The
protected breaker preserves the physical diamond-forest face. Each tree
toggle reduces the number of factor components by one, so the final factor
is a Hamilton cycle. The frozen decorated-cycle equivalence gives the
claimed diamond forest. \(\square\)

This is the exact modification of the published gluing architecture that
is currently supported by a local theorem. The weaker dynamic alternative
would carry the entire feasible-decoration relation and permit a new SDR
after a nontransparent toggle. The \(m=4\) census shows that this relation
is sometimes strictly larger than the diagonal transparent relation, but
no all-\(m\) propagation theorem for it is known.

The finite \(m=2,3,4\) census verifies the initial leaf state in every
positive decoration tested. Every one of the 1,728 decorations of the
repaired \(m=4\) cycle has a balanced forest gap graph, and each of the six
transparent Hamilton hexagons has at least one common decoration passing
the leaf test on both sides. This is evidence for Definition 5.6, not a
proof that Corollary 2.4 automatically implies Theorem 2.6.

For the displayed positive fixtures, the gap-forest component profiles
\((\#\text{gaps},\#\text{colours},\#\text{edges})\) are

\[
\begin{array}{c|c}
m&\text{profiles}\\ \hline
2&(1,1,1),\\
3&(5,5,9),\\
4&6(1,1,1)+(2,2,3)+3(3,3,5)+(4,4,7).
\end{array}                                         \tag{5.2}
\]

Every component is a balanced tree and hence has its forced matching.

The fixed-decoration transparent state is not the only finite-width
possibility. Theorem 2.7 gives the exact dynamic replacement.

### Definition 5.8 (bounded-linkage gluing state)

A bounded-linkage \({\rm BPGR}(r)\) state is a sequence of oriented factors

\[
                        C_0,C_1,\ldots,C_q
 \tag{5.3}
\]

such that every \(C_i\to C_{i+1}\) is an alternating \(2t_i\)-circuit and:

1. a carried perfect augmented matching decorates \(C_i\);
2. writing
   \[
      H_i=\mathcal A_{C_i}\cap\mathcal A_{C_{i+1}},
   \]
   choose a maximum matching \(M_i^H\) of \(H_i\). Its common deficiency
   \(\rho_i=N_i-\nu(H_i)\), where \(N_i\) is the common shore size, is at
   most \(3t_i\), so it exposes \(\rho_i\)
   **unpaired** terminals on each shore. Carry those two terminal sets
   together with a complete vertex-disjoint
   \(M_i^H\)-augmenting linkage in \(\mathcal A_{C_{i+1}}\), or with compatible
   bounded-adhesion linkage signatures whose root composition supplies
   that complete linkage by Theorem 2.8;
3. the perfect matching obtained from that linkage is decoded to the new
   occurrence representatives;
4. the new simple support gap graph comes with either a direct
   balanced-forest/leaf certificate or a valid exterior-ear certificate;
5. the protected trace and every declared endpoint-labelled physical
   socket are either disjoint from both the physical circuit collar and
   the matching symmetric-difference support, or are reverified in the
   output state; and
6. the circuit satisfies the literal component equation
   \[
        \kappa(C_{i+1})=\kappa(C_i)-1,
   \]
   equivalently it joins exactly two current physical factor components
   and splits none.

### Theorem 5.9 (bounded-linkage gluing closure)

If \(C_0\) has the declared initial decoration/leaf/trace/socket state and
a bounded-linkage gluing state uses exactly
\(\kappa(C_0)-1\) component-reducing circuits, then \(C_q\) is a Hamilton
middle-levels cycle with a Catalan decoration, a spanning
\(\operatorname {Cat}_r\)-path physical lift, and the declared final socket
state.

#### Proof

At each step Theorem 2.7 turns the named maximum common matching plus
complete linkage
into a perfect augmented matching, hence a decoration. Item 4 restores the
leaf-peelable gap state; item 5 restores the physical trace/socket state.
Item 6 lowers the component count by one, so after the declared number of
steps the factor is Hamiltonian. The decorated-cycle equivalence and the
trace certificate give the Catalan path lift. \(\square\)

Without a decomposition hypothesis, only the terminal count in Definition
5.8 is bounded and an augmenting path may cross arbitrarily many recursive
blocks. Under bounded adhesion, Theorem 2.8 replaces the global linkage by
an exact finite tree-DP signature. The DP state must be the product of that
linkage signature with the gap-forest component partition,
trace/socket/voltage data, and all deeper-shadow/compiler guards; bounded
linkage alone is not an accepting recursion.
Before the recursive decorated state is entered, Theorem 2.7 separately
allows a deficiency-\(d\) input with width \(d+3t\).

## 6. Complement-antipodal power-of-two reduction

There is a sharp simplification on the power-of-two subsequence. Let
\(m\ge2\) and

\[
 Q=\binom{2m-1}{m-1}=2s+1
 \tag{6.1}
\]

and suppose complementation acts on the Hamilton cycle by

\[
       \overline{A_i}=B_{i+s},\qquad
       \overline{B_i}=A_{i+s+1}.                    \tag{6.2}
\]

Then

\[
                         \overline{u_i}=\ell_{i+s}. \tag{6.3}
\]

Thus any upper occurrence transversal \(I\) canonically supplies the lower
transversal

\[
                              J=I+s.                 \tag{6.4}
\]

This is a distinguished complement-coherent choice, not the only possible
lower transversal.

The physical circular order is not the ordinary order on \(I\). Define

\[
                         S=2I\pmod Q\subseteq\mathbb Z_Q. \tag{6.5}
\]

### Theorem 6.1 (odd-gap antipodal selector theorem)

The complement-paired representatives \((I,I+s)\) alternate by rail around the
physical \(2Q\)-cycle if and only if every cyclic gap between consecutive
elements of \(S\) is odd.

#### Proof

The \(A_i\)-mark is at physical position \(2i\). Its paired \(B\)-mark is
at

\[
                   2(i+s)+1=2i+Q\pmod{2Q}.           \tag{6.6}
\]

Hence the complete mark set is

\[
                         \{p,p+Q:p\in S\}.           \tag{6.7}
\]

In physical order it consists of two copies of the cyclic indicator of
\(S\). Rail type is physical-position parity. Consecutive marks lie on
opposite rails exactly when their distance is odd, and those distances are
precisely the cyclic gaps of \(S\), repeated twice. \(\square\)

The factor \(2\) in (6.5) is essential. Multiplication by two is a
permutation of \(\mathbb Z_Q\), but it changes the cyclic order.

There is an equivalent two-state form. Start at some \(p_0\in S\), lift
the cyclic interval to \([p_0,p_0+Q)\), and put

\[
 D(r)=\sum_{\substack{p\in S\\p_0\le p\le r}}
             (-1)^{p-p_0}.                           \tag{6.8}
\]

Then all gaps are odd exactly when

\[
                  D(r)\in\{0,1\}\quad\text{for all }r,
                  \qquad D(p_0+Q-1)=1.               \tag{6.9}
\]

Selected positions of the starting parity are the \(0\to1\) transitions,
selected positions of the other parity are the \(1\to0\) transitions, and
unselected positions are identity transitions. This is the exact
fundamental-half automaton for a complement-paired recursion.

Lucas' theorem gives

\[
 Q\text{ odd}\quad\Longleftrightarrow\quad m\text{ is a power of two}.
 \tag{6.10}
\]

In that case

\[
 K=\operatorname {Cat}_m=\frac{2Q}{m+1}
 \tag{6.11}
\]

has \(2\)-adic valuation one, and \(P=Q-K\) is odd, exactly as required for
writing the odd number \(Q\) as a sum of \(P\) odd cyclic gaps.

### Theorem 6.2 (exact antipodal trace face)

Let \(z\in\{0,1\}^Q\) be the indicator of \(S\). Under Theorem 6.1, the
physical lift has a cycle exactly when every zero-run of \(z\) has length
two and every one-run of \(z\) has odd length. It is a forest exactly when
some zero-run has length at least four or some one-run has even length.

The bad face is not removed by parity. Indeed

\[
                        z=(1^{m-1}00)^{K/2}           \tag{6.12}
\]

has length \((m+1)K/2=Q\), weight \((m-1)K/2=P\), all gaps odd, and lies on
the bad face. Formula (6.12) is a combinatorial trace example; it does not
assert that its ones form an occurrence transversal on an arbitrary cycle.

Consequently the complete gate inside the complement-coherent subclass is:

> Find one occurrence of every upper turn colour such that the doubled
> positions (6.5) have all cyclic gaps odd and avoid the bad trace
> condition in Theorem 6.2.

The paired lower SDR and its gap matching are then automatic. A protected
\(0^4\) quotient socket gives the cleanest sufficient trace guard.

The unrestricted power-of-two problem is broader. Already at \(m=2\),
with \(Q=3,s=1\), one may take \(I=\{0\}\). The complement-paired choice
\(J=\{1\}\) has trace \(100100\) and lies on the bad cycle face, whereas
the unpaired choice \(J=\{0\}\) has a forest trace. Thus complement symmetry
supplies a sharp sufficient subproblem; it does not prove that every useful
decoration is complement-paired.

For a recursion that keeps both the factor and the carried decoration
complement-paired at every stage, switch polygons must be toggled in
complement-stable batches and the intermediate block system must retain the
antipodal indexing. Under these hypotheses, the lower palette equation in
Theorem 2.3 is the complement of the upper palette equation and the
boundary test is exactly (6.9). Thus this paired power-of-two atom carries
one local upper-colour multiset and one two-state boundary relation, rather
than two independent gap graphs.
Preserving the leaf invariant still requires Theorem 2.6's contraction
test; complement symmetry does not make that graphic condition automatic.

This is a genuine simplification, but not an all-\(m\) induction: powers of
two are not closed under \(m\mapsto m+1\). A standard Pascal recursion must
carry the full two-sided gap state at intermediate semilengths, or else use
a new doubling/final-step construction that preserves complement pairing.

## 7. Exact remaining lemma and scope

The strongest proved recursive conclusion is now the following.

* For the general matching-first architecture, Theorem 1.1 is a
  necessary-and-sufficient Pascal rule. The missing existence theorem is a
  port-compatible, acyclic signed matching of the two residual rectangular
  path systems.
* For the middle-levels sufficient subclass, Theorem 2.1 is the exact
  composition rule. The missing existence theorem is \({\rm BPGR}(m)\):
  populate the \(Q+R\) extreme shell on both sides and choose the GMM/Pascal
  glues so that the residual bridge graph has a perfect matching.
  In the leaf-peelable refinement, opening \(b\) blocks forces exactly
  \(Q+R+b\) router vertices on each shore in the clean template. The
  concrete stronger target is a component-distinct pairing and matched-ear
  order together with a **joint alternating SDR plus leaf-transparent
  gluing tree** as in Definition 5.6.
  Nontransparent factor-safe \(2t\)-switches have the exact alternative
  state of Definition 5.8: common deficiency at most \(3t\), hence at most
  \(3t\) unpaired terminals on each shore, followed by a complete
  augmenting linkage and explicit
  leaf/trace/socket revalidation. In general only the width is bounded;
  under bounded adhesion, Theorem 2.8 gives the exact finite gammoid/
  linkage signature. The remaining task is an accepting **joint** tree
  state with the gap-forest, socket/voltage and deeper guards.
  Sections 9--11 refine “bounded linkage” to controlled debt: a packet may
  have growing length and undecorated prefixes, provided the joint
  interaction graph has bounded width--or exact bounded-interface block
  signatures--and only \(O(w)\) terminals, component endpoints and
  reachability ports remain live.  Scalar
  two-complete-parent Pascal recursion is impossible; contraction must
  preserve residual acyclicity and the no-\(H\leadsto T\) condition.
* For power-of-two \(m\), the complement-coherent subclass reduces to the
  single odd-gap coloured transversal of Theorem 6.1 plus the trace guard.
  Unpaired lower SDRs remain a legitimate broader route.

The authenticated \(m=4\) counterexample is the smallest possible warning
against weakening \({\rm BPGR}\) to two turn surjections. Conversely, the
existing \(m=3\) audit shows every middle-levels Hamilton cycle there is
decorable, and the frozen \(m=4\) hexagon repair supplies an explicit
decorable cycle and transparent local atoms. These are finite bases, not
an inductive proof.

No published Middle Levels or GMM theorem currently states the bulk
extreme-shell occurrence system, its boundary gap--Hall condition, or its
protected trace socket. Their constructions may be modified only by
proving exactly this extra coloured-router assertion. This note neither
rules out such a modification nor derives it from undecorated connectivity.

Section 8 sharpens this for the literal standard family: its private
attachments survive locally at \(m=5\), but a period-three turn orbit is
absent before the two-matroid gluing theorem can be entered. Section 9 then
closes this finite preparation gate by a synchronized three-\(C_{10}\)
packet.  The packet changes the component matroid and has undecorated
intermediate states, so it must be contracted to one debt-carrying
preparation macro before the private accepting recursion.  The all-\(m\)
problem is to construct such a macro uniformly, not to revive the
unmodified standard tree.

The final \(m=5\) closure is now all-depth complete, so its remaining
failure is not a shadow marginal.  Thirty-one immutable internal
length-two runs violate depth-two residence under every whole-path
permutation, reversal and socket choice.  Section 11 proves the exact
capacity law for a separate interior-rethread bank and the bounded-width
streaming theorem which keeps live debt bounded as that bank grows.

Even a proof of leaf-\({\rm BPGR}(r)\) would close only the central
ordered-four-transversal/decorated-cycle gate. The full equality
\(\nu(k)=B(k)\) additionally requires its carrier to be coupled to
residence, deeper shadow towers, protected endpoint sockets, and the exact
compiler. None of those downstream implications is claimed here.

## 8. The private-path face and the exact standard \(m=5\) failure

The first standard glue has more structure than mere leaf safety.  After
its two old singleton sockets are deleted, its gained attachment is a
pendant path on three colour blocks.  The following abstraction is the
closed recursive form of that observation.

### Lemma 8.1 (postorder private-path composition)

Let the factor-component glues be the edges of a rooted tree.  Prepare one
common retained gap forest.  For every tree edge \(e\), suppose its gained
attachment, after suppressing private series subdivisions, is

\[
       [p_e]-g_e^0-[q_e]-g_e^1-[a_e],               \tag{8.1}
\]

where \([p_e]\) and \([q_e]\) are singleton colour components used by no
other attachment, and \([a_e]\) is one component of the already constructed
child-subtree gap forest.  Suppose also that no occurrence of \(p_e\) or
\(q_e\) lies outside the two displayed gap stars after the old sockets are
deleted, that the full unsuppressed off-anchor interiors of different
bundles are pairwise vertex-disjoint, and that the full support of bundle
\(e\) meets the union already constructed before \(e\) exactly in
\([a_e]\).

Then adding the bundles in child-to-parent order preserves a gap forest.
Consequently the gap-graphic row is free on the component-tree labels, and
the simultaneous gluing problem reduces to component-graphic--gammoid
intersection, together with the independent palette, trace/socket/voltage,
and compiler guards.

#### Proof

At the moment bundle \(e\) is added, (8.1) is a tree which meets the old
union only at \([a_e]\).  Adjoining a tree at one old vertex cannot create a
cycle.  The occurrence-closure hypothesis prevents an undeclared second
attachment of either private colour to the old union, while the explicit
one-contact and disjoint-interior hypotheses exclude shared gaps and
undeclared old-core incidences.  Induction in
postorder proves the claim.  This is precisely the private-socket face of
Theorem 4.2. \(\square\)

Laminar physical intervals alone are not enough: the final sentence of the
hypothesis is essential.  A repeated private colour in an uncut old gap
would give a second contact with the retained core and could close a cycle.

### Proposition 8.2 (canonical local triple injection)

Write a canonical MMM gluing pair as

\[
                 x=110u0v,\qquad y=101u0v,          \tag{8.2a}
\]

and put \(x_i=f^i(x0)\), \(y_i=f^i(y0)\).  Its incidence hexagon is

\[
                    (x_0,x_1,x_6,x_5,y_0,y_1).     \tag{8.2b}
\]

Mark the rank-\(m-1\) states
\(x_0,x_2,x_6,y_0,y_4\) and the opposite-shore ports
\(x_1,x_5,y_1\).  Define

\[
 c_0=010u0v0,\qquad c_1=001u0v0,\qquad c_2=000u1v0. \tag{8.2c}
\]

Inside the declared tube, the old simple supports are the three singleton
sockets \(\{c_0\},\{c_1\},\{c_2\}\), while the new supports are

\[
                 \{c_0,c_1\},\quad\{c_1,c_2\},\quad\{c_2\}.           \tag{8.2d}
\]

The selected opposite-shore owners rotate from
\((x_1,y_1,x_5)\) to \((y_1,x_5,x_1)\).  Thus the complete lower-turn
multiset is preserved for every standard label.  For the
potential-decreasing heavy-root labels used in the canonical tree below,
the local upper-owner multiset is preserved as well.  Moreover, distinct
canonical pairs \((u,v)\) have disjoint triples
\(\{c_0,c_1,c_2\}\).

#### Proof

Apply the defining local word map \(f\) successively to \(x0\) and \(y0\).
The three intersections at the marked opposite-shore ports are exactly the
words in (8.2c); replacing the old hex matching by the other matching gives
(8.2d) and the displayed owner rotation.  The corresponding unions give
the same upper multiset in the other cyclic order for the declared
heavy-root labels.  This upper assertion is not made for an arbitrary
non-heavy standard label.

For injectivity, the prefixes `010`, `001`, `000` distinguish the three
roles.  In the first two roles, the first down-step below height zero in
\(u0v\) recovers the cut between the Dyck words \(u,v\).  In the third,
the last primitive component of \(u1v0\) recovers the same cut.  Hence an
equality of two colour words forces both the role and \((u,v)\) to agree.
\(\square\)

Proposition 8.2 is a local lower-tube theorem, with two-sided transparency
only on its stated heavy-root face; it is not privacy in the full factor.
Lemma 8.1 additionally requires occurrence closure and a single retained-
core anchor.  Those extra conditions hold for the following first
nontrivial pair of simultaneous labels.

### Theorem 8.3 (exact local \(m=5\) private paths)

For the potential-decreasing standard \(n=4\) MMM tree, the base factor has
component lengths \(36,72,144\).  Its two canonical glues are

\[
\begin{array}{c|c|c|c}
 &x&y&(A\text{-ports};B\text{-ports})\\ \hline
\tau_0&11001010&10101010&
  (\{83,85,89\};\{87,91,93\}),\\
\tau_1&11001100&10101100&
  (\{51,53,57\};\{55,59,61\}).
\end{array}                                         \tag{8.2}
\]

They successively change the component lengths to \(72,180\) and then
\(252\).  Mark all six ports of each glue and additionally mark the
rank-four endpoint states

\[
       \{340,90\}\quad\hbox{for }\tau_0,
       \qquad
       \{308,58\}\quad\hbox{for }\tau_1.           \tag{8.3}
\]

The local lower triples are disjoint:

\[
       C_0=\{82,84,88\},\qquad C_1=\{50,52,56\}.   \tag{8.4}
\]

Before \(\tau_0\), the relevant simple gap supports are

\[
 N(g_{83,90})=\{82\},\quad
 N(g_{85,340})=\{84\},\quad
 N(g_{90,89})=\{88\};                              \tag{8.5}
\]

after \(\tau_0\), they are

\[
 N(g_{83,340})=\{82,84\},\quad
 N(g_{85,90})=\{84,88\},\quad
 N(g_{90,89})=\{88\}.                              \tag{8.6}
\]

Before \(\tau_1\), the analogous supports are

\[
 N(g_{51,58})=\{50\},\quad
 N(g_{53,308})=\{52\},\quad
 N(g_{58,57})=\{56\};                              \tag{8.7}
\]

after \(\tau_1\), they are

\[
 N(g_{51,308})=\{50,52\},\quad
 N(g_{53,58})=\{52,56\},\quad
 N(g_{58,57})=\{56\}.                              \tag{8.8}
\]

Thus the two complete attachment quotients are the disjoint pendant paths

\[
 [82]-g_{83,340}-[84]-g_{85,90}-[88],
 \qquad
 [50]-g_{51,308}-[52]-g_{53,58}-[56].              \tag{8.9}
\]

The first two colour blocks in each path are private; the last is its one
retained-core anchor.  Hence there is no local private-triple overlap at
\(m=5\).

Each symbolic atom marks five rank-four states
\(x_0,x_2,x_6,y_0,y_4\) but only three opposite-shore states
\(x_1,x_5,y_1\).  Thus \(g\) disjoint atoms leave an exact exterior mark
debt of \(2g\) on the opposite shore.  Here the two atoms consume ten of
the 84 upper-side marks and six of the 84 lower-side marks, leaving
respectively 74 and 78 exterior marks.  In the final cyclic order the four
units lie across the four exterior sectors

\[
  308\to83,\qquad340\to85,\qquad89\to53,\qquad57\to51.          \tag{8.9a}
\]

This signed boundary debt is part of the bulk-router state; the private
path incidence matrix alone does not balance the global alternation.

#### Proof

Literal turn calculation gives the lower owner permutations

\[
\begin{array}{c|ccc|ccc}
 &\multicolumn{3}{c|}{\text{old}}&\multicolumn{3}{c}{\text{new}}\\
\tau_0&87{:}84&91{:}82&93{:}88&87{:}82&91{:}88&93{:}84\\
\tau_1&55{:}52&59{:}50&61{:}56&55{:}50&59{:}56&61{:}52,
\end{array}                                         \tag{8.10}
\]

and the upper owner sets are respectively
\(\{343,347,349\}\) and \(\{311,315,317\}\) on both sides.  The endpoint
marks in (8.3) have upper colours \(350,95,318,63\), all distinct from one
another and from those six local upper colours.  Their intervening rivals
are duplicate occurrences of already selected colours.  The complete
occurrence census of (8.4) is contained in the gaps displayed in
(8.5)--(8.8); there is no outside support edge.  Equations (8.5)--(8.9)
follow, and Lemma 8.1 applies. \(\square\)

This theorem is local.  It does not supply a global alternating occurrence
SDR.  In fact the unmodified standard recursion fails exactly there.

### Theorem 8.4 (period-three palette obstruction at \(m=5\))

The complete standard \(m=5\) MMM gluing family has two Hamilton outputs.
Each has only \(81\) of the required \(84\) lower turn colours and only
\(81\) of the required \(84\) upper turn colours.  Both miss

\[
       \mathcal R^- =\{73,146,292\};                \tag{8.11}
\]

these are the three rotations of the period-three word \(100100100\).
The locally private output \(\{\tau_0,\tau_1\}\) misses

\[
       \mathcal R^+=\{219,365,438\}.                \tag{8.12}
\]

Therefore no unmodified standard \(m=5\) output admits a Catalan
decoration.  The private-path graphic row succeeds locally; palette
surjectivity fails first.

#### Proof

The fourteen semilength-four Dyck words give three plane-tree classes and
three standard labels, two of which are parallel at component level.  The
two resulting labelled spanning trees are the complete standard Hamilton
family.  Exhaustive evaluation of the explicit turn maps gives (8.11) and
the two upper missing triples recorded in the frozen theorem of item 2172;
for the locally private tree it gives (8.12).  Proposition 8.2 shows that
every standard label only permutes its complete lower local triple.
Consequently the base factor's missing lower orbit (8.11) is invariant
under every standard gluing sequence, independently of the chosen tree.
The two canonical heavy-root toggles also preserve their upper triples; the
alternative non-heavy label is not all-six upper-transparent, and its
separate literal output census still has three missing upper colours.  Turn
surjectivity is necessary for a decoration.
\(\square\)

### Proposition 8.5 (exact two-matroid rank ledger)

Lemma 8.1 is exactly what removes the gap-graphic row.  Without its private
one-contact hypothesis, the selectable labels lie in the three-row product
\(I(M_C)\cap I(M_G)\cap I(M_L)\), equivalently matroid three-parity on
three copied grounds; the generic class contains three-dimensional
matching and has no two-matroid Edmonds criterion.  On the private face,
the following ordinary two-matroid ledger is exact.

On the locally private label ground

\[
                         T=\{\tau_0,\tau_1\},       \tag{8.13}
\]

the component graph is a three-vertex path and the gap row is free by
Lemma 8.1.  Conditional on a carried decoration, both labels are locally
transparent, so the label-only component-graphic--gammoid intersection has
rank two.  Its Edmonds deficit is therefore zero:

\[
 \delta_{\rm label}
 =2-\min_{X\subseteq T}
       \bigl(r_C(X)+r_L(T\setminus X)\bigr)=0.       \tag{8.14}
\]

This does not contradict Theorem 8.4: the carried-decoration hypothesis is
false.  To put the failed preparation into the same two-matroid ledger, add
one mandatory repair source for every colour in
\(\mathcal R^-\dot\cup\mathcal R^+\).  On

\[
E=T\dot\cup\mathcal R^-\dot\cup\mathcal R^+,      \tag{8.15}
\]

take the direct sum of the component matroid with \(U_{6,6}\), so the six
repair atoms are coloops in that row, and make the unmodified occurrence
gammoid loop on them: the missing colours have no occurrence, hence no
directed route.  The target rank is \(2+6=8\), while

\[
 \min_{X\subseteq E}
       \bigl(r_C^+(X)+r_L^+(E\setminus X)\bigr)=2,  \tag{8.16}
\]

witnessed by \(X=T\).  Thus the augmented Edmonds rank deficit is exactly

\[
                         \boxed{6},                 \tag{8.17}
\]

or exactly \(3\) on either turn shore separately.  Equivalently the exact
failure vector is

\[
               (\delta_-,\delta_+,\delta_{\rm label})=(3,3,0).        \tag{8.18}
\]

The distinction is load-bearing.  The private/aligned two-matroid theorem
is an accepting-glue theorem after palette preparation; it cannot create
isolated colour rows which are absent before the glues.
The deficit six counts mandatory missing-colour atoms, not physical
switches: one future nonstandard switch may create several required
colours simultaneously.

Finally, at the Pascal step \(m=4\to5\),

\[
             Q=35,\qquad R=7,\qquad Q+R+b=42+b.     \tag{8.19}
\]

Each private path supplies two exterior matched-ear pairs, so the two
standard paths supply four.  In a clean copied-parent template they leave
\(38+b\) router pairs to a genuine bulk construction (forty when \(b=2\)).
Equivalently their six turn ports per shore are far below the
\(Q+R=42\) extreme-shell support lower bound.  The standard MMM interiors
do supply most of that bulk state--their final turn maps reach \(81/84\)--
but a preliminary period-three palette repair, a nonstandard switch, or a
different base factor is still necessary before the private transparent
tree and the two-matroid rank test can be invoked.

The last necessity is discharged at this one finite scale by Section 9.
The obstruction and the rank ledger above remain the exact description of
the *unmodified* standard family; they are not an obstruction after
nonstandard palette preparation.

## 9. The synchronized three-\(C_{10}\) repair closes the \(m=5\) central state

The preparation deficit in Proposition 8.5 is not an obstruction to a
nonstandard packet.  The newly frozen repair gives the exact positive
counterpart.

### Theorem 9.1 (exact repaired private Catalan state at \(m=5\))

Let \(C_0\) be the locally transparent standard Hamilton output using
\(\tau_0,\tau_1\).  There are three pairwise vertex-disjoint alternating
\(C_{10}\) circuits \(Z_1,Z_2,Z_3\) such that every successive toggle is
Hamilton-safe and

\[
 (\delta_-,\delta_+,d_{\rm aug}):
 (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0).            \tag{9.1}
\]

The final augmented occurrence graph has a perfect matching of order
\(210\) even after all twelve standard hexagon ports are forced selected.
For the resulting occurrence decoration:

1. the simple gap--colour graph is a forest with a unique matching;
2. the binary trace is on the linear-forest side;
3. all four states obtained by independently toggling \(\tau_0,\tau_1\)
   retain the same leaf-peelable decoration and trace acceptance; and
4. the two private attachments remain exactly the paths (8.9).

The common augmented graph of \(C_0\) and the repaired Hamilton cycle has
matching order \(197\), hence deficiency \(13\).  Relative to a maximum
common matching and the forced-port final matching, their symmetric
difference has exactly thirteen vertex-disjoint augmenting paths, covering
all twenty-six exposed terminals.  Thus the repair packet satisfies the
literal common-core linkage condition; palette counts alone are not being
used as a proxy.

More strongly, the packet support is disjoint from the complete old/new
private tubes, not merely from their twelve named ports.  It changes none
of the six private lower labels

\[
                   50,52,56,82,84,88
\]

or the six private upper labels

\[
                  311,315,317,343,347,349.          \tag{9.1a}
\]

#### Proof

The three displayed circuits in the frozen repair theorem have disjoint
ten-vertex supports.  Literal symmetric difference gives (9.1) and a
Hamilton cycle after every prefix.  Exact bipartite augmentation gives the
forced matching \(210/210\).  Direct construction of the simple support
graphs for the two-standard-glue Boolean square gives a forest and unique
matching in each of the four states; direct trace replay accepts each
state.  The old/new occurrence closures of the two private triples are the
matrices in (8.5)--(8.8), and direct support comparison gives (9.1a).
Finally, symmetric difference of a maximum \(197\)-edge common matching
with the final perfect matching decomposes into thirteen augmenting paths
and four harmless alternating cycles.
\(\square\)

For the compound packet, \(t=15\) in the notation of Theorem 2.7.  The
generic bound from source deficiency three is \(3+3t=48\); the exact width
is only thirteen.  Consecutive common-core ranks are

\[
                   204,205,205,                       \tag{9.1b}
\]

so their deficiencies are \(6,5,5\); the matching gains from each common
core to its old/new endpoint are respectively

\[
                   (3,4),(3,4),(4,5).                \tag{9.1c}
\]

All twelve private-port matching edges remain available in every stage,
and forcing them does not lower any rank in (9.1b), nor the macro common
rank \(197\).  Nevertheless the intermediate augmented graphs still have
deficiencies two and one.  The three switches are therefore not a sequence
of already accepting decorated states.  They are one synchronized
regeneration macro whose last state enters the private gluing recursion.

### Proposition 9.2 (the repaired component face has rank one)

The three repair circuits are vertex-disjoint from the two standard hexagon
tubes, so their toggles commute with \(\tau_0,\tau_1\).  Remove both
standard hex matchings from the repaired Hamilton cycle.  The resulting
preglue factor has two components, of orders \(120,132\), and the component
counts on the Boolean square are

\[
   \kappa(0,0)=2,\qquad
   \kappa(1,0)=\kappa(0,1)=\kappa(1,1)=1.           \tag{9.2}
\]

Consequently either \(\tau_0\) or \(\tau_1\) alone is a complete
component-tree basis.  On

\[
                         T=\{\tau_0,\tau_1\},       \tag{9.3}
\]

the prepared component matroid is \(U_{1,2}\); the gap row is free by the
private-path theorem, and the fixed forced-port decoration makes the
linkage row free on these transparent labels.  Edmonds' minimum is

\[
   \min_{X\subseteq T}
       \bigl(r_C(X)+r_L(T\setminus X)\bigr)=1=q-1. \tag{9.4}
\]

Thus the repaired private/aligned two-matroid deficit is zero.  If both
hexes are retained, the second is an additional Hamilton-preserving
transparent switch, not a second edge of the necessary component tree.

The old rank-two component tree is therefore not transported through the
packet.  Before the standard glues, the exact component profiles along the
packet are

\[
 (36,72,144)\to(36,216)\to(36,48,168)\to(120,132). \tag{9.4a}
\]

The middle switch splits a component.  Component monotonicity holds only
for the contracted macro output followed by one chosen private glue, not
switch by switch.

#### Proof

Disjoint physical supports give commutation.  The four component counts,
(9.4a), and all four gap/linkage acceptances are the exact Boolean-square
and packet-prefix replay in Theorem 9.1.  A rank-one uniform component
matroid and a free rank-two linkage matroid give (9.4) directly.
\(\square\)

This corrects the pre-repair rank-two picture in Proposition 8.5: the
repair packet changes not only palette ranks but also the component
decomposition against which the standard glues are interpreted.

### Proposition 9.3 (an output trace socket, not a full physical socket state)

For the forced-port repaired decoration, the unmarked four-state run

\[
                         121,105,361,353             \tag{9.5}
\]

occurs consecutively in every point of the two-standard-glue Boolean
square.  A second unmarked run is

\[
                         403,147,155,27,             \tag{9.6}
\]

up to reversal in the double-toggle state.  Both are disjoint from the
standard hexagon ports.  Hence (9.5) is a protected \(0^4\) trace breaker
for the subsequent private gluing stage.

These runs are output sockets: they intersect the support of the preceding
\(C_{10}\) repair and are not claimed to survive through that packet.
Moreover, a trace breaker is not an endpoint-labelled physical connector
schedule.  The repair certificate used in Theorem 9.1 does not itself audit
those downstream rows.  The later all-depth closure audit, recorded below,
now settles final socket topology and the shadow tower at \(m=5\), while
residence fails sharply.

#### Proof

Read the cyclic marked/unmarked word of each of the four factors using the
same forced matching.  The two displayed vertex strings are consecutive
unmarked runs of length four in every state.  Lemma 3.1 gives trace
linearity; the final scope statement follows because none of the listed
downstream coordinates appears in the repair audit. \(\square\)

### Theorem 9.4 (pinned atomic preparation-macro contraction)

Let

\[
                         C_0,C_1,\ldots,C_s          \tag{9.7}
\]

be a sequence of factor-safe alternating switches.  Suppose only the final
augmented graph \(\mathcal A_{C_s}\) is required to have a perfect matching
\(P\).  Put

\[
 H=\mathcal A_{C_0}\cap\mathcal A_{C_s},\qquad
 \rho=N-\nu(H).                                    \tag{9.8}
\]

Let \(M\) be a maximum matching of \(H\), and let \(\Pi\) be a set of
pairwise disjoint matching edges which belongs to both \(M\) and \(P\).
Then \(P\triangle M\) supplies exactly \(\rho\) vertex-disjoint
\(M\)-augmenting paths covering every exposed vertex, plus alternating
cycles, and none of those paths uses an endpoint of an edge in \(\Pi\).

Consequently the whole sequence (9.7) may be contracted to one legal
matching-level preparation transition provided that:

1. the final factor, gap matching/forest, binary trace, component state,
   private occurrence closure, sockets and every claimed shadow/residence
   guard are protected or reverified at \(C_s\);
2. every future private-glue port is **simultaneously** pinned in the one
   common set \(\Pi\); and
3. no recursive assertion is made about decoration or component
   monotonicity at the intermediate \(C_i\).

For the three-\(C_{10}\) packet one may take \(|\Pi|=12\) and
\(\rho=13\).  Its contracted output has two factor components and either
private hex is a legal component-reducing transparent glue.  Thus the
packet followed by one chosen private hex is a complete central
palette/linkage/gap/trace transition at \(m=5\).  This does not by itself
supply residence or the compiler.

#### Proof

The symmetric difference of two matchings consists of alternating paths
and cycles.  Since \(M\) has deficiency \(\rho\) and \(P\) is perfect,
exactly \(\rho\) path components are augmenting and their endpoints are
the \(2\rho\) vertices exposed by \(M\).  Every edge of \(\Pi\) belongs to
both matchings, so it is absent from their symmetric difference; its
endpoints are already matched in both and cannot lie on an alternating
component.  The remaining claims use only the two endpoint states.  The
exact \(m=5\) values and component/glue assertion are Theorem 9.1 and
Proposition 9.2. \(\square\)

Theorem 9.4 is not a relabelling of Definition 5.8.  That definition
requires a perfect decorated state after every switch.  Here the
intermediate deficiencies are deliberately hidden inside one macro.  An
alternative all-\(m\) recursion could expose them, but then its state must
carry partial matchings and deficit terminals.
Common pinned matching edges protect their matching endpoints only; they
do not protect physical tube adjacency, gap occurrence closure or a deeper
witness unless those resources satisfy Item 1 separately.

### Lemma 9.5 (retained-window protection through a switch packet)

Let a cyclic middle-state chronology be cut into retained fragments by a
factor-safe switch; fragments may be permuted and reversed.  For \(q\ge1\)
write

\[
 L_i^{(q)}=\bigcap_{j=0}^{q}V_{i+j},\qquad
 U_i^{(q)}=\bigcup_{j=0}^{q}V_{i+j}.                \tag{9.9}
\]

If the complete \((q+1)\)-state window
\(V_i,\ldots,V_{i+q}\) lies inside one retained fragment, then after the
switch it still occurs, possibly reversed, and supplies the same two
targets \(L_i^{(q)},U_i^{(q)}\).  For a packet of switches, a witness is
preserved if its window lies inside one retained fragment at every stage.
Therefore, if every required lower and upper target at every depth
\(q\le d\) has one such protected occurrence, the packet preserves the
complete depth-\(d\) shadow tower.

#### Proof

A switch changes only the adjacencies at its cut/reconnection seams.  Every
retained fragment occurs verbatim or in reverse order.  Intersection and
union are independent of order, so a window wholly inside that fragment
has the same labels after the switch.  Induct over the packet. \(\square\)

Lemma 9.5 gives one sufficient packet-prefix audit.  The original frozen
repair certificate checks only physical incidence, the two immediate turn
palettes, augmented alternation, gap support, Hamiltonicity, and the binary
trace.  A later independent replay instead closes the final state directly:
the 42-path lift plus a colour-injective 42-connector closure covers the
complete lower-intersection and upper-union tower through depth five.
Exactly 46 of the 252 cycle cuts preserve that all-depth support; 39 are
connector cuts retaining all 42 path blocks intact.

The same replay proves a sharp negative residence theorem.  The fixed path
interiors contain 31 coordinate one-runs of length two, spread over 18
paths with coordinate multiplicities

\[
                 5,5,2,3,3,3,3,3,3,1.              \tag{9.10}
\]

Every such run is bounded by zeroes inside its path.  Path permutation,
reversal and endpoint socket choice preserve it.  Since depth two requires
all one-runs to have length at least three, no intact-path opening is
resident.  An interior rethread is mandatory.

The corrected recursive target is therefore sharper than the end of
Section 8:

> construct, uniformly in \(m\), a controlled-debt packet of bounded-port
> repair and interior-rethread circuits which outputs a private leaf-safe
> gluing state and protected flag/socket interface; its total length may
> grow, but its live boundary, linkage debt and reachability state must stay
> bounded.  Then apply an ordered fixed-decoration transparent gluing list.

At \(m=5\), palette preparation, common linkage, private gap geometry,
component gluing, binary trace, final physical closure and the complete
flag tower are proved for the synchronized source.  A different,
independently replayed interior matching now closes its 31 internal
residence defects while preserving both immediate palettes, but incurs 21
deep-target debts before joining.  The remaining finite gate is therefore
a residence-compatible all-depth connector chronology, followed by the
compiler, together with recursive transport of the private resource state;
no coefficient-one consequence is claimed.

### Authenticated finite source

The exact finite input used in this section is
`MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`,
SHA-256
`78c2079ad71641b96fc1e5002047f012f8f8fd787a73f4ae1d8bc6c916910881`.
Its audit script has SHA-256
`65a52cb19f2ef6e38e437fe251726bec28935509ca05e86b43557bf5ab72e07d`,
and its frozen JSON has SHA-256
`f43e39674c4a027fe46ed2f9918e8c3dcc218865816decad4a8e1f4b8052c7e1`
with canonical payload
`ca3c2ffe5bc7f7a93543f63be93a282f39c12eb08e8fdd9f2fefb4f132b0d1fe`.
The downstream all-depth/residence audit is
THREAD_A_M5_THREE_C10_DOWNSTREAM_COMPATIBILITY_AUDIT_20260731.md,
SHA-256
bd3cc11ac3682c5d7a244099e736f5a707884edac5d1554dde7ada0805f20c60.
Its replay JSON has SHA-256
91201d7281bde581ef01a58778b6e8edbea8dcb7da37d185c76f1771b91b2a5e
and payload
19752a1d1ec5d02ad5ab18479228a85d6128caa8b1bc51cc0226e509c8f31549.

## 10. Orbit-bank capacity for a recursive turn-defect router

The \(m=5\) packet suggests a precise general architecture.  A bounded
switch repairs one missing lower colour and one missing upper colour; all
but the last switch in a cyclic orbit bank are direct filters, while one
mixed relay closes the orbit packet's topology.  Before asking for such a
construction, there is a sharp packing obstruction.

Put

\[
 n=2m-1,\qquad
 N_m=\binom{n}{m-1},\qquad
 P_m=\binom{n}{m-2}.                                \tag{10.1}
\]

The two middle-levels rails have \(N_m\) vertices each, and each turn
palette has \(P_m\) colours.  We take \(m\ge2\); at the degenerate base
\(m=2\), the unique empty/full turn colour has stabilizer three, which is
the whole group \(\mathbb Z_3\), so it still belongs to the stated
order-three class.

### Theorem 10.1 (exact orbit and vertex-capacity obstruction)

Let the missing lower and upper turn colours be unions of translation
orbits.  Write \(f_- ,f_+\) for their numbers of free \(\mathbb Z_n\)
orbits and \(e_- ,e_+\) for their numbers of orbits with stabilizer of
order three.  The latter numbers are zero unless

\[
                         m=3a+2.                    \tag{10.2}
\]

Suppose a type-preserving router pairs free lower orbits with free upper
orbits and order-three lower orbits with order-three upper orbits, and uses
one pair-repairing \(C_{10}\) for every physical colour pair.  Then

\[
                  f_-=f_+=f,\qquad e_-=e_+=e,       \tag{10.3}
\]

and the number of required circuits is exactly

\[
                  D=n f+\frac n3e.                  \tag{10.4}
\]

At the clean-subgroup scale, put

\[
 s=3^{v_3(n)},\qquad h=n/s.
\]

A free full-rotation orbit splits into \(s\) clean
\(\mathbb Z_h\)-tracks and an order-three orbit into \(s/3\) tracks.
Hence the corresponding quotient demand is

\[
                  B=s f+\frac s3e,\qquad D=hB.      \tag{10.4a}
\]

Here \(B\) counts clean quotient tracks and \(D\) counts physical
circuits; they must not be identified.

Let \(r_0,r_1\) middle vertices on the two rails be reserved for private
tubes, fixed ports, or other inherited physical sockets.  If all circuit
supports and the reserve are pairwise vertex-disjoint, then necessarily

\[
             5D+r_0\le N_m,\qquad 5D+r_1\le N_m.   \tag{10.5}
\]

Equivalently,

\[
 f\le
 \min_{\epsilon\in\{0,1\}}
 \left\lfloor
   \frac{N_m-r_\epsilon-5(n/3)e}{5n}
 \right\rfloor.                                    \tag{10.6}
\]

If the router is organized as one cyclic packet per missing orbit, with
one final mixed relay in every packet, then the exact role counts are

\[
    \#\text{relays}=f+e,\qquad
    \#\text{direct filters}=D-(f+e).                \tag{10.7}
\]

Equation (10.7) is the proposed orbit-router architecture, not a palette-
only lower bound; (10.3)--(10.6) are unavoidable for every disjoint
realization of that architecture.

#### Proof

A subset of \(\mathbb Z_n\) of size \(m-2\) can have a stabilizer of order
\(d>1\) only if \(d\mid n\) and \(d\mid m-2\).  But

\[
                  \gcd(2m-1,m-2)=\gcd(3,m-2),       \tag{10.8}
\]

so \(d=3\), and this occurs only in (10.2).  A free orbit has \(n\)
physical colours and an order-three orbit has \(n/3\).  Type-preserving
pair repair therefore gives (10.3)--(10.4).  Without type preservation the
weaker unavoidable equation is

\[
 n f_-+\frac n3e_-=n f_++\frac n3e_+,              \tag{10.9}
\]

but it does not supply orbitwise banks.

An alternating \(C_{10}\) contains five vertices on each middle-levels
rail.  Pairwise disjointness from all other circuits and the reserve gives
(10.5), and solving it for \(f\) gives (10.6).  A cyclic bank of length
\(n\), respectively \(n/3\), has one declared final relay and all its
other members direct, proving (10.7). \(\square\)

### Proposition 10.1A (clean-track balance and orbit-saturated reserve)

Keep \(s=3^{v_3(n)}\), \(h=n/s\), and let \(H=\mathbb Z_h\) be the clean
translation subgroup.  Without type preservation put

\[
 B_-=sf_-+\frac s3e_-,\qquad
 B_+=sf_++\frac s3e_+.                              \tag{10.9a}
\]

An \(H\)-equivariant one-pair-per-circuit router can be complete only if

\[
 B_-=B_+=B,\qquad\text{equivalently}\qquad
 3f_-+e_-=3f_++e_+.                                 \tag{10.9b}
\]

For a fixed private/socket reserve \(S\), let

\[
 \rho_H(S_\epsilon)=
 \#\{H\text{-orbits on }V_\epsilon\text{ which meet }S\}.             \tag{10.9c}
\]

Suppose every \(C_{10}\) seed uses five distinct \(H\)-orbits on each
rail, its \(h\) translates are pairwise disjoint, and different seeds use
disjoint rail orbits.  Then the exact orbit-slot obstruction is

\[
 \boxed{
       5B+\rho_H(S_\epsilon)\le\frac{N_m}{h}
          =s\operatorname {Cat}_{m-1}\qquad(\epsilon=0,1).
 }                                                   \tag{10.9d}
\]

Conversely, once literal seeds with the declared five-orbit supports are
supplied, disjointness of those support-orbit sets and (10.9d) are exactly
the rail-slot condition for taking all their \(H\)-translates.  They do not
by themselves supply the seeds, endpoint topology, or common decoration.

#### Proof

Every rank-\((m-1)\) or rank-\(m\) middle vertex has a free \(H\)-orbit,
because \(\gcd(h,m-1)=\gcd(h,m)=1\).  Thus each rail has \(N_m/h\)
\(H\)-orbits.  A free defect orbit splits into \(s\) \(H\)-tracks and a
stabilizer-three orbit into \(s/3\), giving (10.9a).  Every circuit pairs
one lower with one upper track, proving (10.9b).  Translating one seed uses
exactly its five rail orbits, while every orbit meeting \(S\) is forbidden;
counting the available orbits proves (10.9d). \(\square\)

This exposes a private-tube obstruction invisible in (10.5).  Always

\[
 \rho_H(S_\epsilon)\le
 \min\{|S\cap V_\epsilon|,N_m/h\}.                   \tag{10.9e}
\]

A reserve with \(N_m/h\) vertices, dispersed one per \(H\)-orbit, saturates
the quotient rail.  Since \((N_m/h)/N_m=1/h\), such a reserve is \(o(N_m)\)
along every subsequence with \(h\to\infty\).  Thus physical sublinearity
alone is not a uniform equivariant capacity condition.  An all-\(m\)
equivariant construction needs orbit-compressed
private tubes, for example

\[
                    \rho_H(S_\epsilon)=o(N_m/h),     \tag{10.9f}
\]

or it must break the clean symmetry and reconfigure the reserve.

### Proposition 10.1B (a literal quotient-pressure sufficient condition)

Let \(x_1,\ldots,x_B\) be paired clean defect tracks.  After all private,
palette and protection filters, let \(\mathcal Z_i^H(S)\) be the family of
legal \(C_{10}\) seed supports for \(x_i\), represented by their five
\(H\)-orbit slots on each rail.  Put

\[
 \Delta_{i,\epsilon}=
 \max_{v\in V_\epsilon/H}
 \bigl|\{Z\in\mathcal Z_i^H(S):v\in Z\}\bigr|.       \tag{10.9g}
\]

If the jobs can be ordered so that

\[
 |\mathcal Z_i^H(S)|
 >
 5(i-1)\bigl(\Delta_{i,0}+\Delta_{i,1}\bigr)
 \qquad(1\le i\le B),                               \tag{10.9h}
\]

then they admit a rainbow quotient-support matching.  Lifting every
selected seed through \(H\) gives \(hB\) pairwise vertex-disjoint physical
repair circuits.

#### Proof

After choosing \(i-1\) seeds, at most \(5(i-1)\) quotient vertices are
occupied on either rail.  On rail \(\epsilon\), at most
\(5(i-1)\Delta_{i,\epsilon}\) candidates for job \(i\) meet an occupied
vertex.  The union bound and (10.9h) leave a legal candidate.  Induction
selects the quotient matching, and Proposition 10.1A lifts it. \(\square\)

This condition is deliberately stronger than the exact rainbow-matching
criterion.  Its value is quantitative: a Pascal atlas with candidate
pressure satisfying (10.9h) proves the entire disjoint orbit bank without
a global hypergraph theorem.

The symbolic marked core of one private atom in Section 8 uses five
vertices on one rail and three on the other.  That is not automatically a
complete occurrence-isolation tube.  In the independent literal \(m=5\)
replay, the full old/new isolation supports have seven vertices on one
rail and five on the other.  Conditional on future tubes having that same
proved full-isolation footprint, \(g_+\) tubes in one orientation and
\(g_-\) in the reverse give

\[
\begin{aligned}
 5D+7g_++5g_-&\le N_m,\\
 5D+5g_++7g_-&\le N_m.                              \tag{10.10}
\end{aligned}
\]

The weaker scalar inequality \(10D+12(g_++g_-)\le2N_m\) loses the rail
imbalance and is not sufficient even as a capacity check.
For a different all-\(m\) collar halo one must use its actual
\((r_0,r_1)\) in (10.5), not the \(7/5\) calibration.

### Corollary 10.2 (exceptional banks fit; arbitrary free defects do not)

In (10.2), the complete stabilizer-three bank on either turn shore has

\[
 E_a=\binom{2a+1}{a}=\frac n3\operatorname {Cat}_a \tag{10.11}
\]

physical colours in \(\operatorname {Cat}_a\) shortened orbits.  Repairing
the whole paired exceptional bank therefore requires exactly \(E_a\)
circuits, of which \(\operatorname {Cat}_a\) are declared relays in the
one-relay-per-orbit architecture.  For every \(a\ge1\),

\[
                         5E_a<N_m.                  \tag{10.12}
\]

Thus the exceptional bank alone is not ruled out by middle-vertex
capacity.  After reserving it and the private tubes, the number of
additional free defect orbits is bounded exactly by

\[
 f\le
 \min_{\epsilon\in\{0,1\}}
 \left\lfloor
   \frac{N_m-r_\epsilon-5E_a}{5n}
 \right\rfloor.                                    \tag{10.13}
\]

By contrast, a disjoint one-pair-per-\(C_{10}\) bank cannot repair an
arbitrary turn map.  If all \(P_m\) colours were missing, even with no
private reserve it would require \(5P_m\le N_m\), whereas

\[
                  \frac{5P_m}{N_m}=\frac{5(m-1)}{m+1}>1
                  \qquad(m\ge2).                    \tag{10.14}
\]

Hence a recursive source must first guarantee a sparse free-orbit defect
set satisfying (10.6); the \(C_{10}\) bank cannot replace the bulk Pascal
turn construction.

#### Proof

An order-three invariant \((m-2)=3a\)-set is a union of \(a\) cosets of
the unique order-three subgroup.  This gives (10.11), and division by the
orbit length \(n/3=2a+1\) gives \(\operatorname {Cat}_a\) orbits.  Split
the \(6a+3\) points into blocks of sizes \(2a+1\) and \(4a+2\).  Counting
only the \((3a+1)\)-sets which take \(a\) points from the first block gives

\[
 N_m=\binom{6a+3}{3a+1}
 \ge \binom{2a+1}{a}\binom{4a+2}{2a+1}
 >5E_a,                                             \tag{10.15}
\]

because the second factor is greater than five for \(a\ge1\).  Equations
(10.13)--(10.14) follow from Theorem 10.1 and
\(P_m/N_m=(m-1)/(m+1)\). \(\square\)

At the clean-track scale the same comparison is sharper.  The complete
exceptional bank uses

\[
 B_{\rm exc}=\frac s3\operatorname {Cat}_a
\]

seed tracks, so its fraction of all rail orbits is

\[
 \frac{5B_{\rm exc}}{N_m/h}
   =\frac{5\operatorname {Cat}_a}
          {3\operatorname {Cat}_{m-1}}=o(1).         \tag{10.15a}
\]

A free paired orbit contributes \(s\) seed tracks.  With no reserve, the
exact quotient-slot threshold is therefore

\[
                         f\le\frac15\operatorname {Cat}_{m-1};        \tag{10.15b}
\]

with private tubes it is reduced by the orbit-saturation term in (10.9d).

At \(m=5\), \(n=9,N_m=126,E_1=3\).  The two audited private tubes have
\((r_0,r_1)=(14,10)\), so the actual three-switch packet uses only

\[
       5\cdot3+14=29<126,\qquad
       5\cdot3+10=25<126.                            \tag{10.16}
\]

After reserving that exceptional packet, the raw disjoint-support budget
would still permit at most two complete free-orbit banks.  This is only a
capacity statement; it does not assert that their required alternating
circuits exist.

There is a sharper Pascal-specific obstruction.  In the step
\(m\mapsto m+1\), the copied parents miss the extreme-shell bank

\[
 S_m=\binom{2m-1}{m-1}+\binom{2m-1}{m-3},           \tag{10.16a}
\]

while one rail of the child middle-levels graph has

\[
 N_{m+1}=\binom{2m+1}{m}
\]

vertices.  Direct factorial cancellation gives

\[
 \frac{S_m}{N_{m+1}}
   =\frac{m^2+2}{(2m+1)(m+2)}.                      \tag{10.16b}
\]

Therefore

\[
                         5S_m>N_{m+1}               \tag{10.16c}
\]

for every \(m\): indeed the difference after clearing denominators is
\(3m^2-5m+8>0\).  Thus disjoint one-pair \(C_{10}\) atoms can never
populate the full Pascal extreme shell.  Since the strict middle-levels
incidence graph has no \(C_4\), the smallest alternating atom is a
\(C_6\), costing three vertices per rail; even that hypothetical unit
router would require \(3S_m\le N_{m+1}\), equivalent to

\[
                         m^2-5m+4\le0.              \tag{10.16d}
\]

It fails for every \(m\ge5\) and is tight at \(m=4\), leaving no room for
private tubes there.  Consequently the turn-defect packet is necessarily
a sparse **post-bulk** repair.  It cannot replace the \(Q+R\) extreme-shell
router of Section 4.

The three-primary filter theorem imposes a separate mixed-orbit
obstruction.  Repairing the complete exceptional banks requires at least
\(2\operatorname {Cat}_a\) partial full-rotation edge orbits, and, when
\(3\nmid\operatorname {Cat}_a\), at least one additional partial orbit
whose two turn colours are nonexceptional.  Thus an otherwise orbit-pure
exceptional router must touch an ordinary edge orbit (unless the bulk
source already supplies it).  This is one global extra partial-orbit
obligation, not one extra \(C_{10}\) per exceptional orbit.  The \(m=5\)
coincidence

\[
 E_1=3=2\operatorname {Cat}_1+1
\]

explains its \(2+1\) direct/relay picture; it does not extrapolate
numerically.  Already at \(a=2\), the physical unit demand is \(E_2=10\)
while the partial-orbit floor is \(5\).

The exact next obstruction is a rainbow support-packing problem.  For each
physical paired defect \(x\), let \(\mathcal Z_x\) be the family of
ten-vertex alternating supports which repair exactly that lower/upper pair,
lose no already unique turn colour, and avoid every reserved private tube.
A disjoint bank exists exactly when the ten-uniform families
\((\mathcal Z_x)_x\) have a rainbow matching.  In particular every
subfamily must satisfy the typed union cuts

\[
 \left|\bigcup_{x\in X}\bigcup_{Z\in\mathcal Z_x}(Z\cap V_\epsilon)
 \right|\ge5|X|\qquad(\epsilon=0,1),                \tag{10.17}
\]

but these Hall-looking vertex counts are not sufficient for a
ten-uniform rainbow matching.  This is the first finite local/flow gate
after (10.5), not a generic palette count.

### Lemma 10.2A (exact endpoint-transition topology)

Let \(F\) be the pre-packet 2-factor, let \(R\) be the union of the old
\(F\)-edges removed by a vertex-disjoint switch packet, and let \(A\) be
the union of its new edges.  Cut \(F\) at \(R\).  Pair the two ends of
every retained path fragment by a matching \(S\).

After contracting the retained paths, the components of
\(F-R+A\) are exactly the alternating cycles of \(S\cup A\), together
with every untouched component of \(F\).  In particular, the endpoint is
Hamiltonian if and only if every old component is cut and \(S\cup A\) is
one alternating cycle.

#### Proof

Every exposed path end is incident with one edge of \(S\) and one edge of
\(A\).  Contracting each retained path therefore gives the 2-regular
alternating multigraph \(S\cup A\), without changing component count.
Any old component missed by \(R\) survives separately. \(\square\)

Thus the word “relay” has two independent meanings.  A wrap arc in the
chosen defect permutation is a palette relay.  It is a physical topology
relay only when the endpoint-transition graph in Lemma 10.2A says so.
Disjoint supports and the role count (10.7) do not imply Hamiltonicity.

### Theorem 10.3 (conditional Pascal/private-tube defect-router closure)

Suppose a Pascal state has paired missing orbit banks satisfying
(10.3)--(10.6), and suppose one can choose a rainbow support matching with
the following additional properties.

1. Each chosen circuit has the declared one-lower/one-upper monotone
   palette delta, and their union repairs every missing physical colour.
2. The union of direct filters and mixed relays passes the exact endpoint
   transition test of Lemma 10.2A for the declared component profile;
   prefixes need only be factor-safe, not decorated or component-monotone.
3. Every complete private tube, including the two boundary marks which
   define its gap stars, lies inside a retained fragment throughout the
   packet.  At the endpoint its occurrence closure is reverified.
4. The endpoint augmented graph has a perfect matching containing all
   private port pins, and its common-core linkage, gap forest and binary
   trace pass Theorem 9.4.
5. Either the retained-window test of Lemma 9.5 protects the desired trace
   and deeper tower through both the packet and every subsequent glue, or
   those rows are reverified after every stage at which they can change.
6. On the *new* endpoint component ground there is an ordered list of
   private glues for the same fixed decoration.  At the moment it is used,
   every glue satisfies the two palette-multiset equalities, retained-
   fragment boundary alternation, the contraction-forest test, and
   \(\kappa_{\rm after}=\kappa_{\rm before}-1\); the list has exactly one
   fewer member than the endpoint component count.  The old component-tree
   basis is not assumed to survive.
7. For a finite-state recursion, either the bank splits into uniformly
   bounded atomic macros which each return to an accepting pinned state, or
   the joint support/augmentation/gap graph has a uniformly bounded-width
   decomposition.  Alternatively one may use bounded-adhesion blocks only
   when each block carries a supplied exact bounded-interface transition
   relation.

Then contracting the whole defect router to one atomic preparation macro
and applying that ordered private-glue list produces a decorated Catalan
linear matching with the declared protected deeper state.

#### Proof

Vertex-disjoint switches have disjoint changed incidences, so their turn
deltas add and the endpoint edge set is independent of their algebraic
order.  Items 1--2 give complete turn palettes and the required endpoint
factor.  Item 3 preserves the literal private local geometry, while Item 4
and Theorem 9.4 supply the joint alternating SDR, gap forest and trace
without requiring false perfect intermediate states.  Item 5 supplies the
deeper coordinate throughout the transition.  Finally Item 6 is precisely
the ordered fixed-decoration hypothesis of Theorem 5.7, so it glues the
endpoint components without importing the pre-repair component matroid.
\(\square\)

Theorem 10.3 is the promised extension of the Pascal/private-tube theorem,
but its hypothesis is one **joint** constructive certificate with several
independent coordinates: rainbow support packing, endpoint transition,
pinned common-core linkage, gap/trace/deeper state, and a new private-glue
basis.  The rainbow matching is only the first local gate.  Item 7 is
load-bearing when \(D\) grows: treating the whole bank as one macro gives
only the generic common-deficiency bound \(d+15D\), not a bounded recursive
state.

Theorem 10.1 shows why no theorem of this form can start from an arbitrary
turn-defective factor.  As a scalar prerequisite, the source must already
cover at least

\[
                  P_m-\left\lfloor
                     \frac{\min(N_m-r_0,N_m-r_1)}5
                  \right\rfloor                    \tag{10.18}
\]

turn colours on each shore, with the remaining free and shortened orbits
paired as above.  The child Pascal \(0/1/2\)-new-coordinate banks are not
themselves cyclic orbits, so the \(f/e\) language applies only after a
cyclic or clean-subgroup residual defect set has been produced.  Proving
that a Pascal construction supplies that sparse residual together with all
coordinates of Theorem 10.3 is the exact new all-\(m\) gate.

There are two logically different switch classes in this statement.

* A **fixed-decoration transparent glue** is governed by Theorem 2.3: its
  selected local turn-colour multisets must agree separately on both
  shores, and the last/first selected shore types on the retained fragments
  must alternate after reconnection.  It must additionally pass the
  contraction-forest test of Theorem 2.6.  These are the moves used in
  Item 6 of Theorem 10.3, and the selected SDR and gluing tree must be chosen
  jointly.
* A **debt-carrying repair macro** is not transparent at its prefixes.  It
  is accepted only through the endpoint perfect matching and common-core
  linkage of Theorem 9.4.  Requiring local multiset equality at every
  constituent \(C_{10}\) would exclude the proved \(m=5\) staircase.

The authenticated \(m=4\) census calibrates the first class exactly:
31 alternating incidence hexes, 16 Hamilton outputs, 10 decorable outputs,
and only 6 with a common fixed decoration.  Thus neither an arbitrary
frozen SDR nor an arbitrary published gluing tree is an admissible
substitute for the joint transparent state.  The \(m=5\) three-\(C_{10}\)
packet calibrates the second class.  A recursive proof must use the repair
macro first and transparent private glues only after its final SDR has been
selected.

## 11. Quantitative repair--rethread capacity and bounded live debt

### Proposition 11.0 (exact all-\(m\) residence surplus)

Put

\[
 M_m=\binom{2m}{m},\qquad L_m=\binom{2m}{m-1},\qquad
 K_m=M_m-L_m=\operatorname {Cat}_m.
\]

Let \(F\) be any Catalan linear-matching lift: a spanning
\(L_m\)-edge path forest in \(J(2m,m)\) using every lower and upper
immediate colour once.  Then every coordinate has exactly \(K_m\) positive
runs on the path components.  If \(c\) Johnson seams successively join
different current components, the total number of coordinate runs is

\[
                         2mK_m-(m-1)c.               \tag{11.0}
\]

Consequently a Hamilton path has \((m+1)K_m+m-1\) runs, while a Johnson
cyclic closure has \((m+1)K_m\) cyclic runs and average positive-run
length exactly \(m\).

More precisely, for a cyclic closure and a required run floor \(h\), let

\[
 D_h=\sum_R(h-|R|)_+,qquad S_h=\sum_R(|R|-h)_+,
\]

where the sums range over all positive coordinate runs.  Then

\[
                    S_h-D_h=(m-h)(m+1)K_m.          \tag{11.0a}
\]

For a Hamilton path the corresponding identity is

\[
 S_h-D_h=m(m+1)K_m-h\bigl((m+1)K_m+m-1\bigr).       \tag{11.0b}
\]

Thus for the compiler floor \(h=d+1=\Theta(\sqrt m)\), residence has
positive aggregate surplus \(\Theta(m^2K_m)\).  The missing theorem is
redistribution of this surplus while preserving palettes, deep witnesses
and chronology, not creation of additional run mass.

#### Proof

For a coordinate \(x\), the induced forest has
\(\binom{2m-1}{m-1}\) vertices.  Its edges are exactly the once-used lower
colours containing \(x\), of which there are
\(\binom{2m-1}{m-2}\); their difference is \(K_m\).  A Johnson seam has
\(m-1\) common coordinates and merges exactly one boundary run in each,
which proves (11.0).  The total positive-coordinate mass is
\(mM_m=m(m+1)K_m\).  Subtracting \(h\) times the displayed run counts gives
(11.0a)--(11.0b). \(\square\)

The all-\(m\) packet may have growing length.  What must remain bounded is
the active interface, not the number of completed circuit cells.  First we
separate three quantities which coincide only for a simple rail-balanced
alternating circuit:

* the turn circuit's literal footprint on each Pascal rail;
* the number of old forest edges deleted by a residence rethread; and
* the rethread's complete physical footprint on each rail.

This distinction is essential.  A palette-incidence \(C_{2t}\) need not
use \(t\) vertices of each Pascal rail, and a physical rethread can have
auxiliary collar or port vertices outside its alternating core.

Let \(\mathcal B_{\rm turn}\) be a pairwise resource-disjoint turn-repair
bank.  For \(X\in\mathcal B_{\rm turn}\), put

\[
 a_{X,\epsilon}=|\operatorname {supp}(X)\cap V_\epsilon|
 \qquad(\epsilon=0,1).                              \tag{11.1}
\]

Let \(R\) be the value of the global forbidden-short-run potential which
must be reduced to zero, and let \(\mathcal B_{\rm res}\) be a family of
interior rethread atoms, pairwise resource-disjoint and disjoint from the
turn bank and private reserve.  Write

\[
 E_Z=\{\hbox{old forest edges deleted by }Z\},\quad
 d_Z=|E_Z|,\quad
 s_{Z,\epsilon}=|\operatorname {supp}(Z)\cap V_\epsilon|.
                                                               \tag{11.1a}
\]

Fix the packet order and define \(g_Z\) to be the marginal drop of the
**global** forbidden-run potential when \(Z\) is applied.  Thus
interactions and newly created defects are included and the gains
telescope.  Neither \(d_Z\) nor \(s_{Z,\epsilon}\) is inferred from the
palette-cycle length.

The separated ledger freezes the turn packet first: \(R\), the source
forest, and the closed spans below are measured at that endpoint.  If turn
and residence operations are interleaved, every turn operation which can
change a run or span must instead be included in the same ordered marginal
ledger, with spans recomputed at the relevant stage; the static theorem
below does not apply by projecting the two classes separately.

For every internally bounded bad run, let its **closed span** be the set
of old path edges from the zero immediately before the run through the zero
immediately after it.  Let \(\mathcal I\) be this interval hypergraph and
let

\[
                         \tau=\tau(\mathcal I)        \tag{11.1b}
\]

be its minimum edge-transversal number.
For a forbidden reserve \(S\), let \(\tau_S\) be the minimum transversal
using only old edges whose two endpoints avoid \(S\); put
\(\tau_S=\infty\) if some closed span contains no such edge.

### Theorem 11.1 (sharp necessary separated-bank ledger)

Let \(S\) be the union of the turn-repair and private-reserve vertices.
Under the disjoint-bank architecture, repairing all \(R\) residence
defects requires

\[
\sum_{Z\in\mathcal B_{\rm res}}g_Z=R,\qquad
\sum_{Z\in\mathcal B_{\rm res}}d_Z\ge\tau_S\ge\tau. \tag{11.2}
\]

If the private reserve occupies \(r_\epsilon\) vertices of rail
\(V_\epsilon\), the exact typed packing inequalities are

\[
 \boxed{
  \sum_{X\in\mathcal B_{\rm turn}}a_{X,\epsilon}
  +\sum_{Z\in\mathcal B_{\rm res}}s_{Z,\epsilon}
  +r_\epsilon\le N_m\qquad(\epsilon=0,1).
 }                                                    \tag{11.3}
\]

In the simple \(C_{10}\) orbit-router architecture of Section 10,
repairing \(f\) paired free orbits and \(e\) paired stabilizer-three
orbits uses

\[
                 D=nf+\frac n3e                    \tag{11.3a}
\]

circuits with \(a_{X,0}=a_{X,1}=5\).  Thus (11.3) specializes to

\[
 5D+\sum_Zs_{Z,\epsilon}+r_\epsilon\le N_m
 \qquad(\epsilon=0,1).                              \tag{11.3b}
\]

If, additionally, every residence atom is a simple rail-balanced
alternating \(C_{2t_Z}\) which deletes its \(t_Z\) old matching edges and
has no auxiliary support, then

\[
 \Theta:=\sum_Zt_Z=\sum_Zd_Z=
          \sum_Zs_{Z,0}=\sum_Zs_{Z,1}.              \tag{11.3c}
\]

Writing \(r_*=\max(r_0,r_1)\), every nonempty bank in this restricted
subclass satisfies

\[
 \frac{\sum_Z g_Z}{\sum_Z t_Z}
 \ge
 \frac{R}{N_m-5D-r_*}.                              \tag{11.4}
\]

Within the restricted subclass (11.3c), if every residence atom has
ordered marginal gain \(g_Z=1\) and the same half-length \(t\), then there
are exactly \(R\) atoms and (11.3b) becomes

\[
                         5D+tR+r_\epsilon
       \le N_m.                                      \tag{11.5}
\]

#### Proof

Resource-disjointness gives (11.3), and telescoping gives the first part
of (11.2).
If no old edge in a closed span is deleted, all its vertices remain
consecutive in one retained fragment, possibly reversed; its bounded short
run therefore survives.  The deleted old edges must hit every member of
\(\mathcal I\).  Their union has size at most \(\sum_Zd_Z\).  Strict
disjointness from \(S\) allows only old edges whose two endpoints avoid
\(S\), proving the second part of (11.2).  A simple \(C_{10}\) has five
vertices per rail, which gives (11.3a)--(11.3b).  Under the additional
rail-balanced hypothesis (11.3c),
\(\Theta\le N_m-5D-r_*\), and division gives (11.4).  The unit-gain
specialization is immediate. \(\square\)

This is a resource theorem, not an existence theorem for the atom
families.  Overlapping correlated atoms can beat (11.3), and one atom may
repair several turn or residence defects.  Such a construction must be
charged by its literal union footprint and net gain rather than by the
separated formula.

The two ledgers in Theorem 11.1 are deliberately independent:
\(\sum d_Z\) pays the closed-span transversal, while
\(\sum s_{Z,\epsilon}\) pays physical capacity.  A one-rail palette braid,
a rethread with auxiliary collars, or an overlapping compound macro cannot
be charged by its abstract half-length.  Overlapping banks require the
same theorem with literal unions in place of the displayed sums.

More explicitly, for an ordered overlapping packet \(Z_1,\ldots,Z_q\) and
a genuinely untouchable reserve \(S_{\rm fix}\), put

\[
 \delta_{i,\epsilon}=
 \left|
  (\operatorname {supp}(Z_i)\cap V_\epsilon)
  \setminus\left(S_{\rm fix}\cup
       \bigcup_{j<i}\operatorname {supp}(Z_j)\right)
 \right|.                                           \tag{11.5a}
\]

Then

\[
 |S_{\rm fix}\cap V_\epsilon|+\sum_i\delta_{i,\epsilon}
 =
 \left|
  \left(S_{\rm fix}\cup\bigcup_i\operatorname {supp}(Z_i)\right)
   \cap V_\epsilon
 \right|                                             \tag{11.5b}
\]

is the exact distinct-resource charge.  This identity permits controlled
overlap but does not certify that the sequential local transitions commute,
restore touched private tubes, or realize their advertised marginal gains.

For the authenticated synchronized \(m=5\) source state,

\[
 N_5=126,\qquad D=3,\qquad r_*=14,\qquad R=31,\qquad
 \tau=29.
\]

The value \(\tau=29\) is exact: the 31 closed three-edge spans lie on 18
paths, and interval duality gives both a 29-edge hitting set and 29
pairwise disjoint spans.  In the restricted rail-balanced simple-cycle
subclass the scalar window is therefore

\[
              29\le\Theta\le126-5\cdot3-14=97.       \tag{11.6}
\]

That raw capacity is not realizable with strict reserve disjointness:
\(\tau_S=\infty\) for the combined repair/private reserve \(S\).
An independent literal comparison uses the 30 turn-packet vertices and two
12-vertex private tubes, all distinct.  Exactly 10 of the 31 closed spans
meet this 54-vertex reserve, and the following two have no edge whose two
endpoints both avoid it:

\[
\begin{array}{c|c|c}
\text{path, coordinate, edge interval}&\text{three span edges}
\\ \hline
(3,1,[19,21])&(59,313),(59,62),(62,572)\\
(7,1,[1,3])&(91,345),(91,94),(94,604).
\end{array}                                           \tag{11.6a}
\]

Deleting any one of these old edges places both its endpoints in the
alternating rethread support, so a support disjoint from the reserve cannot
hit the span.  Hence **no** residence bank satisfying Theorem 11.1's strict
separation hypothesis repairs this literal \(m=5\) state.  A successful
rethread must overlap/reconfigure the repair or private reserve, or first
move one of the locked spans.

For comparison, if one ignores this incidence lock and further restricts
to strict middle-levels, rail-balanced simple cycles with one unit of
ordered gain per bad run, then the absence of a \(C_4\) forces
\(t_Z\ge3\).  A uniform bank must have \(t=3\), while a mixed bank obeys
\(\sum_Z(t_Z-3)\le4\).  This is not a conclusion about general physical
rethreads: the authenticated one-rail braid and the palette \(C_4\)
candidates lie outside that subclass.  The 29-edge transversal and the
two reserve-locked spans are the load-bearing obstruction to the **strictly
separated frozen reserve**, not to residence itself.

The closed-span source is
MATH_AUDIT_AD_M5_INTERNAL_RUNSPAN_TRANSVERSAL_20260731.md,
SHA-256
20a632a046d2f8fdeb745ef366e1c93938ab858d1d107e6f35dc80b7be3d74e2.
Its frozen JSON has SHA-256
22fb3d9fc344ba0f1656319f304f26df4961853fd9b31bbb68dc893f98f9789d
and payload
43b39a185d71991d3e40538defd1e325e0f7436f63a41113f0fc0a14ccc2340f.
The independent repair/private support source has SHA-256
e5f15f9775bc65c8e283a16ffc584c3d2c1cc29c73382fca58894ecfe1de3540.

The strict-separation no-go has now been bypassed at this finite base.
An independently replayed perfect diamond matching changes 119 of the 210
partners.  Its matching symmetric difference consists of 30 colour-
disjoint alternating circuits with half-length histogram

\[
              2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1,    \tag{11.6b}
\]

whose half-lengths sum to 119.  The lifted endpoint is again a 210-edge,
42-path Catalan forest with both immediate palettes exact, and every
strictly internal positive coordinate run has length at least three.  It
therefore removes all 31 old internal residence defects by overlapping and
reconfiguring the frozen repair/private geometry, exactly the case excluded
from Theorem 11.1.  The circuit decomposition is on diamond-colour
resources; it is not asserted to be a vertex-disjoint physical Pascal-rail
bank, and no accepted intermediate physical-switch history is claimed.

The remaining finite debt is different: the rethreaded fragments miss 21
deep targets (lower/upper counts \(6/10,2/2,0/1\) at depths \(2,3,4\)) and
their boundary runs still depend on the connector chronology.  Hence the
new all-\(m\) target is residence-compatible **all-depth joining**, not
repair of an intrinsic central residence deficit.

The fixed endpoint-only face has since been closed negatively.  Its
pair-safe port graph has only 69 of 304 formal Johnson pairs and 15 dead
ports; one path component has both ports dead.  The two forced defect
collars are edge-disjoint for every connected choice, except for one choice
which isolates a two-component cycle.  Thus no connector matching and no
single opening edge can make these 42 fixed path bodies resident.  The
next positive bank must contain a further interior/socket actuator which
creates at least one pair-safe port while carrying the 21 deep debts.  This
is a sharp obstruction to that endpoint face, not to a different Catalan
matching or a joint interior--connector rethread.

The imported run, rethread and two-dead-socket facts are the authenticated
packages in handoff items 2187R, 2188 and 2190.  Their source notes are
MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md,
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md and
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_SOCKET_DEAD_COMPONENT_NOGO_20260731.md.
Their current artifact hashes are maintained in those handoff items; the
proof of Theorems 10.1A--11.2 does not depend on a particular prose freeze
of the imported notes.

There is genuine asymptotic room for a sparse residual router.  The exact
identity

\[
                         N_m=n\operatorname {Cat}_{m-1}             \tag{11.7}
\]

shows that \(p_m\le\operatorname {Cat}_{m-1}\) private tubes of at most
\(\sigma\) vertices per rail cost at most \(\sigma N_m/n\).  For
\(m=3a+2\), (10.15) gives

\[
             \frac{E_a}{N_m}
             \le\binom{4a+2}{2a+1}^{-1}.             \tag{11.8}
\]

Hence all stabilizer-three defects and \(O(\operatorname {Cat}_{m-1})\)
bounded tubes consume \(o(N_m)\) vertices.  In particular, for every fixed
\(\eta>0\), if

\[
      nf\le\left(\frac15-\eta\right)N_m,\qquad
      \sum_Zs_{Z,\epsilon}=o(N_m)\quad(\epsilon=0,1),\qquad
      p_m\le\operatorname {Cat}_{m-1},                \tag{11.9}
\]

then (11.3b) has positive linear slack for all sufficiently large \(m\),
even after reserving the complete stabilizer-three bank.  The constant
\(1/5\) is the sharp raw ceiling of this disjoint unit-\(C_{10}\)
architecture.

This conclusion is for symmetry-broken physical packing.  For an
\(H\)-equivariant translated bank, let \(S_{\rm live}\) be the union of
private and residence resources which the turn seeds must avoid.  The
additional sharp requirement is (10.9d); in particular the asymptotic
version needs

\[
                    \rho_H(S_{\rm live}\cap V_\epsilon)
                       =o(N_m/h)\qquad(\epsilon=0,1). \tag{11.9c}
\]

Typed physical \(o(N_m)\) footprint does not imply (11.9c) uniformly.

The slot count does not by itself bound matching debt.  The following is
the exact finite-state condition which does.

### Theorem 11.2 (controlled-debt streaming theorem)

Form one joint interaction graph \(\mathfrak G\) for the ordered repair and
rethread packet.  Its vertices include every candidate cell-choice vertex,
physical support resource, factor- and matching-degree row, augmented-
matching vertex, turn-defect row, gap-support vertex, component endpoint,
private pin, residence guard, and directed head/tail port, including every
adjacency/window resource whose later change could invalidate a stored
witness.  Use the primal co-use graph, joining two vertices whenever one
local choice or constraint uses both; equivalently one may use the
cell--resource incidence graph only with the explicit requirement below
that every complete constraint neighbourhood occurs in one bag.

Suppose \(\mathfrak G\) has a rooted tree decomposition of width at most
\(w\), so every bag has at most \(w+1\) vertices, such that:

1. every circuit, rethread, palette row and witness guard is contained in
   one bag, and the common-core matching used to orient augmentation is
   either fixed globally or its selected edges and exposed terminals are
   represented in the same bags;
2. every resource appears in a connected set of bags;
3. when a bag interior is forgotten, every individual palette and
   residence row incident with it is discharged, every internal augmented
   and gap-matching vertex is covered, and every internal factor fragment
   is either rejected as a premature sealed cycle or represented by its
   endpoints in the adhesion;
4. every live vertex of the residual directed forest is included in the
   stored boundary reachability relation; deletions are performed before
   that relation is frozen, or the relation is recomputed after each
   deletion, and adding \(T\to H\) is rejected whenever
   \(H\leadsto T\); and
5. the root state requires zero palette/matching/residence debt, the desired
   endpoint connectivity/acyclicity condition determined by the carried
   pairings, the fixed private pins, a perfect carried gap matching in an
   acyclic support, residual directed acyclicity, and the declared
   shadow/trace state.  An arbitrary labelled component-size profile is not
   included unless its own finite boundary counter is added.

Then packet feasibility is decided exactly by a tree dynamic program whose
live debt and number of live physical endpoints are \(O(w)\), independently
of the number of circuit cells.  A complete boundary state consists of:

* used-resource, in/out-degree capacity and exposed matching-terminal
  subsets, together with the fixed/selected common-core matching edges
  which orient them;
* oriented partial pairings of factor and augmenting-path endpoints;
* the gap-forest connectivity partition together with the restriction of
  the same decoded gap perfect matching;
* the directed reachability relation among live head/tail ports; and
* either a certificate that the binary trace and quotient voltage/phase are
  immutable, or their exact finite boundary automata: boundary trace bits,
  zero-run lengths capped at \(4+\), one-run parity, all-same-run and
  violation bits, together with the live voltage/phase sum or type; and
* for every live fragment/coordinate collar, its boundary bit, prefix and
  suffix one-run lengths capped at \(d+1\), an all-one/same-boundary-run
  bit, and internal-violation bit,
  together with every named changed-window debt or immutable protected
  shadow witness which can still be invalidated.

Every table entry is one **jointly realizable tuple** arising from the same
local circuit and representative choices; taking Cartesian products of
separately feasible rows is forbidden.  If \(A_m\) bounds the finite local
type/occurrence-label alphabet on one live port, there are at most

\[
             A_m^{O(w)}2^{O(w^2)}(d+2)^{O(w)}        \tag{11.9a}
\]

boundary states.  When all labels are fixed by the decomposition, the
\(A_m^{O(w)}\) factor may be omitted.  In either form the exponent is
independent of the number of already processed packet cells.

#### Proof

Restrict any global solution to a bag subtree.  All interactions with its
complement use adhesion vertices by Items 1--2, so restriction produces
exactly the displayed boundary data.  Conversely, compatible child states
glue if they use no resource twice, match every forgotten vertex, join
oriented path fragments consistently, create no forbidden component or
gap cycle, and discharge every forgotten guard.  Induction over the tree
gives necessity and sufficiency.

Subsets, partial pairings and set partitions on \(O(w)\) points contribute
\(2^{O(w\log w)}\) possibilities.  Directed reachability contributes at
most \(2^{O(w^2)}\).  Capped run collars and their all-one bits contribute
\((d+2)^{O(w)}2^{O(w)}\), and live labels contribute \(A_m^{O(w)}\).
No state coordinate depends on the number of already forgotten cells, so
live debt remains \(O(w)\).
\(\square\)

A bounded-adhesion block decomposition with unbounded bags gives the same
boundary conclusion only when every block is supplied with an exact
bounded-interface transition relation.  Bounded adhesion alone is
insufficient--the one-bag decomposition would otherwise make the theorem
vacuous.

The reachability coordinate is algebraically necessary.  Contracting one
chosen directed atom \(T\to H\) preserves a directed forest exactly when
the residual graph is acyclic and contains no directed path
\(H\leadsto T\).  Thus the Pascal determinant obstruction to two complete
parent copies cannot be repaired by scalar sector counts; boundary-
deficient rails and their live reachability relation must be carried.

An orbitwise defect cycle has abstract width two, but this alone does not
invoke Theorem 11.2.  Its physical circuit supports, common-core augmenting
paths, gap attachments, residence rethreads and private pins must admit one
**aligned bounded-width** decomposition, or bounded-interface blocks with
supplied exact transitions.  A packet of growing length is therefore
legitimate precisely when this joint width remains bounded (or when it
splits into uniformly bounded accepting macros).  This is the
quantitative controlled-debt theorem requested by the synthesis: packet
length may grow, while live boundary and debt do not.

### Corollary 11.3 (serial free/shortened orbit banks)

Suppose every free orbit packet of length \(n\) and every shortened packet
of length \(n/3\) has a cyclic order of cells.  After cutting its declared
wrap relay, suppose the resources of cell \(i\) split as

\[
             I_i\ \dot\cup\ S_{i-1}\ \dot\cup\ S_i,
             \qquad |I_i|\le b,\quad |S_i|\le w,    \tag{11.10}
\]

where:

1. every physical circuit, turn row, augmented edge, component transition,
   gap edge, reachability guard and assigned residence rethread involving
   \(I_i\) uses no resource outside the displayed three sets;
2. a resource shared by two cells belongs to their common \(S_i\);
3. every completed cell discharges all debt except the labelled defect,
   path and reachability terminals in \(S_i\); and
4. private tubes are processed in tree-contiguous order, with at most \(p\)
   private pin resources carried across any cut.

Then a packet containing arbitrarily many free and shortened orbit cells
has live boundary at most \(2w+p\) after each orbit wrap is cut.  Its cell
bags have size at most

\[
                         \omega=b+3w+p,
\]

the third interface being the carried initial wrap interface, and it has
an exact controlled-debt DP with

\[
             A_m^{O(\omega)}2^{O(\omega^2)}
                  (d+2)^{O(\omega)}                 \tag{11.11}
\]

combinatorial states.  Cross-bank relays may concatenate the orbit packets
without increasing this bound if they use only the outgoing interface of
one bank and the incoming interface of the next.

#### Proof

Take one bag for each cell, containing \(I_i,S_{i-1},S_i\), the initial
wrap interface carried until closure, and the live private pins.
Consecutive bags intersect only in the current/carried interfaces and pins;
all resource occurrences are connected by Items 1--2.  A cyclic bank is
opened at its wrap, so at worst its two end interfaces are simultaneously
live.  Items 3--4 give the forgetting condition of Theorem 11.2.  Apply
that theorem with width at most \(\omega-1\).  A cross-bank relay replaces
one outgoing/incoming boundary and does not add a third. \(\square\)

Corollary 11.3 is the weakest literal “long packet, bounded debt” lemma.
It permits \(D\) and the number of residence cells to grow.  What remains
unproved is the physical alignment hypothesis (11.10): a short abstract
defect word does not prevent a common-core augmenting path or a residence
witness from jumping between distant cells.
When \(b,w,p\) are uniform constants, the live boundary and debt are
uniformly bounded independently of packet length; without that uniformity
the displayed formula, rather than the phrase “bounded debt,” is the
quantitative conclusion.

The remaining all-\(m\) construction lemma is now exact:

> after the bulk Pascal shell is supplied, produce a sparse free/shortened
> turn-defect bank and an interior residence rethread satisfying the typed
> capacity ledger (11.3) and, when equivariant, the orbit-saturated reserve
> cut (10.9d); then choose a residence-compatible component chronology which
> includes the required interior/socket actuators and supplies every
> residual deep target.  All palette, endpoint-transition,
> matching, gap, reachability, run, shadow and private-tube resources must
> admit one aligned bounded-width decomposition (or exact bounded-interface
> block signatures).  At the endpoint choose an ordered list of
> fixed-decoration transparent, leaf-peelable glues.

Theorem 11.2 proves that such a certificate has bounded live state.  It
does not prove that the published GMM/Pascal construction supplies the
certificate.

The ordered-gluing theorem of handoff item 2189 discharges the final list
once a zero-debt fixed-decoration private/aligned entrance satisfies its
two-matroid rank and prefix reachability hypotheses.  The present capacity
theorems do not manufacture that entrance; they quantify the growing
repair/rethread packet which must precede it.
