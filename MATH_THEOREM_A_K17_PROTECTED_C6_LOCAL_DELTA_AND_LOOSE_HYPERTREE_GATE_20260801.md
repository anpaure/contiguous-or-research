# Exact local deltas for protected incidence \(C_6\) switches on the seven-component k17 twin-bank factor

**Date:** 2026-08-01  
**Lane:** A, k17 protected twin-bank factor / residence and deep-shadow
rethread  
**Status:** exact local-delta theorem, exact residence-cut lower bound, and
proof-safe three-move search reduction.  A decreasing loose-hypertree
triple is not asserted unless accompanied by a literal final-factor replay.

## 0. Frozen input and objective

The input is

\[
\text{scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv},
\]

with SHA-256

\[
\texttt{7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df}.
\]

Its owner two-factor has seven cycles of sizes

\[
14305,\ 8615,\ 1362,\ 18,\ 4,\ 3,\ 3.                  \tag{0.1}
\]

All 29 protected owners and all 52 protected incidence edges survive.  Both
q1 shores are complete.  The exact remaining cyclic defects are

\[
b_2=3073,\qquad b_3=2710,                               \tag{0.2}
\]

and

\[
h_{11}=1502,\qquad h_{12}=295,\qquad h_{13}=9.           \tag{0.3}
\]

Ranks 14 and above are complete.  Define the non-topological defect

\[
\Phi(F)=b_2(F)+b_3(F)+h_{11}(F)+h_{12}(F)+h_{13}(F).
                                                                    \tag{0.4}
\]

For the frozen factor,

\[
                              \Phi(F)=7589.              \tag{0.5}
\]

The immediate finite target is three protected q1-safe \(C_6\) moves whose
component hyperedges form a loose hypertree on the seven old cycles, whose
literal replay has one component, and for which \(\Phi\) is strictly below
7589.

## 1. Incidence \(C_6\) as a three-edge owner switch

Let \(S\) have rank seven and let \(x_0,x_1,x_2\) be distinct coordinates
outside \(S\), with subscripts modulo three.  Put

\[
 \ell_i=S+x_i,\qquad q_i=S+x_i+x_{i+1}.                  \tag{1.1}
\]

The six incidences \(\ell_iq_i,\ell_iq_{i-1}\) form one Boolean incidence
hexagon.  Suppose the current factor selects \(\ell_iq_i\), and let \(p_i\)
be the other owner selected at \(\ell_i\).  The alternating \(C_6\) switch
is

\[
 \ell_iq_i\longmapsto\ell_iq_{i-1}\qquad(i\in{\mathbb Z}_3). \tag{1.2}
\]

On the owner two-factor this deletes exactly

\[
                         e_i=p_iq_i                     \tag{1.3}
\]

and adds exactly

\[
                         f_i=p_iq_{i-1}.                \tag{1.4}
\]

Every owner degree and every lower-colour degree remains two.  The switch is
physically admissible precisely when the three removed incidences are
selected and unprotected, the three added incidences are absent, and the
six resulting incidences are simple.  In particular, all 52 flagged
incidences remain literal.

### Lemma 1.1 (exact q1 delta)

Let \(u_i^-=p_i\cup q_i\) and \(u_i^+=p_i\cup q_{i-1}\).  For every
rank-ten colour \(R\),

\[
 m'_R=m_R-\#\{i:u_i^-=R\}+\#\{i:u_i^+=R\}.              \tag{1.5}
\]

Hence lower-q1 is preserved identically.  Upper-q1 support is preserved if
and only if \(m'_R\ge1\) for every \(R\).  Exact multiset neutrality is the
stronger coordinatewise equality

\[
            \sum_i {\bf e}_{u_i^+}=\sum_i{\bf e}_{u_i^-}. \tag{1.6}
\]

For a batch of switches, sum (1.5) over all changed adjacencies and then
test the final multiplicities.  Individual safety is sufficient but is not
necessary for a net-safe batch.

#### Proof

The lower vertex \(\ell_i\) is unchanged, so its lower colour is unchanged.
Only the three owner adjacencies (1.3) are replaced, and their upper colours
are respectively the displayed unions.  Counting occurrences gives
(1.5)--(1.6). \(\square\)

## 2. Component delta from the six stubs

Delete \(e_0,e_1,e_2\), retaining their six labelled stubs
\(p_i,q_i\).  Contract every connected path segment of the old factor after
these deletions.  The old closure pairs \(p_i\) with \(q_i\); the new
closure pairs \(p_i\) with \(q_{i-1}\).

### Theorem 2.1 (stub-matching component calculus)

The change in the number of affected owner cycles is exactly

\[
 \Delta c
 =c\bigl({\cal S}\cup\{p_iq_{i-1}:i\in{\mathbb Z}_3\}\bigr)
  -c\bigl({\cal S}\cup\{p_iq_i:i\in{\mathbb Z}_3\}\bigr), \tag{2.1}
\]

where \({\cal S}\) is the contracted segment matching and \(c\) denotes
the number of connected 2-regular components.  After the connectivity
pairing \({\cal S}\) of the six stubs has been computed, no interior vertex
labels are needed for the component delta.  Computing \({\cal S}\) itself
requires tracing which two stubs are joined by each retained path segment.

In particular, if the three removed adjacencies lie in three distinct old
cycles, then the new cyclic stub matching joins those three cycles into one,
so

\[
                              \Delta c=-2.               \tag{2.2}
\]

#### Proof

After deletion, every affected vertex has degree two except the six stubs,
which have degree one.  Contracting degree-two path interiors preserves
component count under either closure.  The two possible closures are
exactly the two matchings in (2.1).  If the cuts lie in three distinct
cycles, \({\cal S}\) consists of three disjoint paths and the nontrivial
three-cycle reconnection makes one cycle. \(\square\)

## 3. Every run delta is contained in six capped junction words

For a positive run of length \(\ell=2\) or \(3\), include its two boundary
edges and its \(\ell-1\) internal edges; call this the run's closure arc.
It has \(\ell+1\) owner adjacencies.

### Theorem 3.1 (six-neighbourhood run calculus)

Under (1.2), every old positive run not meeting one of the three removed
edges survives unchanged, and every new positive run not meeting one of
the three added edges is an unchanged old run.  Therefore the exact change
in \(b_2+b_3\) is obtained by:

1. retaining at each of the six cut stubs the first up to three inward
   owners which could belong to a short run and the next (fourth) inward
   owner as its sentinel; if the segment ends earlier, retaining the whole
   segment and identifying it with the record from its other stub;
2. gluing those six capped half-words by the old and new stub matchings;
3. counting length-two and length-three positive runs which meet a glued
   junction; and
4. deduplicating a run when a segment is so short that two capped
   neighbourhoods overlap.

The replay uses the physical union of all six records.  In particular, a
coordinate-constant short segment can traverse two joins.

No other owner trace can contribute to the delta.

#### Proof

The switch changes only three adjacencies.  A run whose closure arc avoids
them sees the same predecessor and successor at every owner, hence is
unchanged.  Conversely, a new run not meeting a new adjacency lies wholly
inside a retained segment and was already present.  A run of length at most
three is determined by its at most three one-bits and the two bounding
zero-bits, so three owner bits plus the sentinel on each incident half-path
are sufficient.  Taking the union before counting handles overlapping
neighbourhoods exactly. \(\square\)

### Corollary 3.2 (exact old-edge hitting lower bound)

Every resident rethread which retains a set of old adjacencies must delete
at least one adjacency from the closure arc of every old short run.  Here
the 26 forbidden owner adjacencies are exactly the protected path edges for
which both incidence edges are among the 52 flags: altering one of these
owner adjacencies deletes at least one flagged incidence.  On the frozen
factor, forbidding those adjacencies, exact circular-interval stabbing gives

\[
\begin{array}{c|rrrrrrr}
\text{cycle size}&14305&8615&1362&18&4&3&3\\ \hline
\tau&2244&1349&208&2&2&1&1.
\end{array}                                               \tag{3.1}
\]

Thus

\[
                              \boxed{\tau=3807}.          \tag{3.2}
\]

Protection does not increase this optimum.  This is the exact transversal
number of the old run-closure hypergraph, hence a necessary lower bound on
changed old adjacencies, not the minimum support of a fully resident
rethread.  Consequently a completely resident simple Hamilton path on the
same \(W\) owners obtained by retaining old segments must delete at least
3807 old owner adjacencies and add at least 3806 new seams: the old cycles
have \(W\) edges and the final path has \(W-1\).  Three
\(C_6\) moves change only nine old adjacencies, so their role can only be a
first strict descent/topology actuator, not a complete residence repair.

The stabbing computation is exact: condition on one allowed point of one
reference circular arc, cut the circle there, and apply rightmost-allowed
greedy to the remaining line intervals; minimize over the conditioned
point.

## 4. Rank 11--13 deck delta is cut-local

Give every old interval occurrence its component, start and width labels
(and hence its end label).
After deleting the three old edges, every interval lying inside one retained
segment survives with the same OR.  The same statement holds for the new
factor.

### Theorem 4.1 (monotone crossing-interval calculus)

For each target \(R\) of rank 11, 12 or 13, let \(C_R^-\) be the number of
old occurrence-labelled intervals crossing at least one removed edge, and
let \(C_R^+\) be the number of new occurrence-labelled intervals crossing
at least one added edge, using widths from one through the component length.
Then

\[
                         w'_R=w_R-C_R^-+C_R^+.           \tag{4.1}
\]

Both crossing catalogues are obtained from the three complete segment
prefix/full/suffix tables.  Starting at a cut or new join, extend a suffix
through any complete intervening contracted segments and then a prefix.  For
a fixed start/suffix, stop increasing its endpoint as soon as its OR has rank
above 13.  This loses nothing, because OR rank is monotone under that
extension; moving the start is a separate branch and can shrink the union.
An interval which meets two or more changed joins is represented once by
its component, start and width (equivalently it may be assigned to the first
changed join after its start).

Consequently

\[
 h'_r=\#\{R:|R|=r,\ w_R-C_R^-+C_R^+=0\},
 \qquad r=11,12,13.                                      \tag{4.2}
\]

#### Proof

Partition old interval occurrences into those wholly contained in one
retained segment and those crossing a removed edge.  Partition new
occurrences analogously.  The first classes are canonically identical and
cancel occurrencewise.  This proves (4.1).  Monotonicity proves the stopping
rule, and endpoint labels prevent double counting in short or wrapping
segments.  Equation (4.2) is the definition of the support holes. \(\square\)

## 5. Three \(C_6\) moves and the loose-hypertree criterion

For a switch whose removed edges lie in three distinct original cycles,
record the three-cycle set as a 3-uniform hyperedge on \([7]\).

### Theorem 5.1 (three-move \(7\to1\) criterion)

Let three switches be serially compatible, meaning that each remains an
alternating incidence \(C_6\) when it is applied in the stated order and
deletes no protected incidence.  A static sufficient condition is that
their full six-edge symmetric-difference supports are pairwise disjoint.
Suppose each switch meets three distinct original cycles.  Applied in an
order in which each later
hyperedge meets the union of its predecessors in exactly one current
component and introduces two new original components, the three switches
merge all seven cycles into one.

Equivalently, their component hyperedges form a connected Berge-acyclic
3-uniform hypergraph with

\[
                         |V|=2|E|+1=7.                   \tag{5.1}
\]

Thus a connected Berge-acyclic triple system admits the required rooted
edge order.  This includes both a three-edge loose path and a three-edge
star.

#### Proof

The first switch merges three cycles to one by Theorem 2.1.  Because the
circuits are physically compatible, every later removed incidence remains
selected.  The second switch then meets the merged cycle and two new cycles,
and again reduces the component count by two.  The third does the same.
Thus \(7\to5\to3\to1\).  Condition (5.1) plus connected Berge acyclicity is
the standard incidence-tree characterization of precisely this ordering.
\(\square\)

For a proposed triple, residence and deep deltas are additive only when its
eighteen capped stub neighbourhoods around the nine removed edges and its
crossing-interval catalogues are
occurrence-disjoint.  In every other case the exact rule is to replay the
union of the nine cuts (and at most nine retained segments) on the final
segment quotient and apply Theorems 3.1 and 4.1 once.  The final acceptance
test is:

\[
\begin{gathered}
\text{all 52 protected incidences retained};\\
\text{one owner component and degree two at every owner/lower vertex};\\
\text{every rank-ten multiplicity positive};\\
\Phi(F')<7589.
\end{gathered}                                            \tag{5.2}
\]

Only after a later rethread reaches full residence is maximal erosion
defined and a terminal COMP3 Hall audit meaningful.  A compiler claim
before that step would be circular.

Ranks 14 and above are not included in \(\Phi\).  A candidate intended as
an all-upper carrier must replay those ranks too; (5.2) certifies only a
strict scoped descent.

## 6. Proof-safe finite search

An exhaustive O3 implementation needs only the following stages.

1. Enumerate every rank-seven core and unordered outside triple, in both
   hex orientations.
2. Retain physically legal switches avoiding flagged incidences.
3. Compute (1.5), (2.1), and the exact local ledgers of Theorems 3.1--4.1.
4. Group ternary merges by their 3-subset of the seven old components.
5. Enumerate compatible hyperedge triples satisfying (5.1), using local
   scores only for ordering, never for final acceptance.
6. Replay every promising nine-edge batch literally and verify (5.2).

Heavy enumeration belongs on H100 CPU.  Resource termination is UNKNOWN,
not a no-go.  Any positive output must freeze the three cores/orientations,
the nine deleted and nine added incidences, the final factor, and an
independent full replay of degrees, protected edges, q1 support, components,
runs and ranks 11--13.
