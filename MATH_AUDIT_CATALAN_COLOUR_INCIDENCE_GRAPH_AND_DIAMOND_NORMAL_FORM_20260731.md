# Colour-incidence graph and the rigid Catalan diamond normal form

Date: 2026-07-31  
Status: exact graph, determinant, orientation, and cap-two diamond theorems;
no all-dimensional existence claim

## 0. Scope and the necessary terminology correction

This note isolates the graph-theoretic content behind the directed repair
gate in
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`.
All matchings below are matchings of **physical edge occurrences**.  This is
important if the input is a walk or multiset rather than a simple cycle.

There are two different notions which must not be conflated.

1. A **common transversal** is one edge set which is simultaneously a
   transversal of all lower colours and all upper colours.
2. A three-level tight enumeration uses a lower transversal and an upper
   transversal whose union covers the middle cycle.  These are generally two
   different edge sets.

A common transversal yields the required pair only in the cap-two block
normal form, by taking its blockwise opposite upper transversal.  Using the
same common transversal on both sides is not tight.  Likewise, a generic
covering pair of transversals need not give a common transversal unless the
cap-two block rule is imposed.

## 1. The occurrence colour-incidence multigraph

Let (P) be any occurrence family of Johnson edges between rank-(m) sets
of (Q_{2m}).  For a physical occurrence (e=AB), put

\[
 \ell(e)=A\cap B\in { [2m]\choose m-1},\qquad
 u(e)=A\cup B\in { [2m]\choose m+1}.
\]

Define the bipartite multigraph

\[
 G(P)=({\cal L},{\cal U};E_P),\qquad
 {\cal L}={ [2m]\choose m-1},\quad
 {\cal U}={ [2m]\choose m+1},
\]

by putting one occurrence edge from (ell(e)) to (u(e)) for every
occurrence (e\in P).  Let

\[
 a_{L,U}=|\{e\in P:\ell(e)=L, u(e)=U\}|
\]

and let (A_P=(a_{L,U})) be its (N\times N) biadjacency matrix, where
(N={2m\choose m-1}={2m\choose m+1}).

For a simple physical middle-edge set, (G(P)) is actually simple.  Indeed,
if (L\subset U), (|L|=m-1), and (|U|=m+1), writing
(U\setminus L=\{a,b\}) shows that the unique middle edge with colours
((L,U)) is

\[
                         (L+a)(L+b).                 \tag{1.1}
\]

The multigraph language is nevertheless the correct one for repeated edge
occurrences and for counting physical transversals.

### Theorem 1.1 (common-transversal equivalence)

An edge-occurrence set (T\subseteq E_P) contains every lower colour once
and every upper colour once if and only if (T) is a perfect matching of
(G(P)).  Moreover,

\[
              \#\{\text{physical common transversals}\}
                    =\operatorname {per} A_P.          \tag{1.2}
\]

#### Proof

The lower-colour condition says that exactly one selected occurrence is
incident with every vertex of ({\cal L}); the upper-colour condition says
the same on ({\cal U}).  These are precisely the two perfect-matching
degree conditions.  In the permanent expansion, a permutation chooses a
lower-to-upper colour pairing and the factor (a_{L,U}) chooses one of its
physical parallel occurrences.  This is exactly the occurrence-level
matching count. (square)

There is also an exact determinant form without cancellation.  Give every
occurrence (e) an independent indeterminate (x_e) and put

\[
             \mathsf E(P)_{L,U}
                 =\sum_{e:\ell(e)=L,,u(e)=U}x_e.      \tag{1.3}
\]

Then (det\mathsf E(P)) is a nonzero polynomial if and only if a common
transversal exists: every perfect matching contributes its own squarefree
edge-occurrence monomial with coefficient (+1) or (-1).  By contrast,
the ordinary integer determinant (det A_P) can cancel and is only a
sufficient certificate when nonzero.  Over (mathbb F_2), it records the
parity of the permanent.

## 2. Exact maximum-degree-two theorem

All degrees in this section count edge multiplicity.  A bound on the number
of distinct neighbours is not enough.

### Theorem 2.1 (balanced-component criterion and count)

Suppose every vertex of (G(P)) has occurrence degree at most two.  Every
connected component is an isolated vertex, a path, or an even cycle; a pair
of parallel edges is the allowed two-cycle.  Then:

1. (G(P)) has a perfect matching if and only if every component is
   balanced between the two shores.  Equivalently, there is no isolated
   vertex and every path component has its two endpoints on opposite
   shores.
2. Every balanced path has exactly one physical perfect matching.
3. Every cycle, including a parallel two-cycle, has exactly two physical
   perfect matchings.
4. Consequently, if the criterion holds and (c) is the number of cycle
   components, then

   \[
                         \operatorname {per}A_P=2^c.   \tag{2.1}
   \]

   The common transversal is unique exactly when (G(P)) is a spanning
   forest of balanced paths.

#### Proof

The component classification is the standard degree-two classification,
with multiplicity making two parallel edges a cycle.  An unbalanced
component cannot be matched internally and components have no external
edges.  In a balanced path an endpoint edge is forced; deleting its two
ends and iterating gives a unique matching.  An unbalanced path ends with an
unmatched endpoint.  On a cycle the two alternating edge classes are the
only matchings.  Multiplying the independent component counts proves
(2.1). (square)

### Corollary 2.2 (ordinary determinant and an exact signing)

Under the hypotheses of Theorem 2.1, suppose a perfect matching exists.  A
balanced path block has determinant of absolute value one.  A cycle of
length (2k), with the parallel two-cycle interpreted as (k=1), has

\[
 |\det A_C|=
 \begin{cases}
  2,&k\text{ odd},\\
  0,&k\text{ even}.
 \end{cases}                                             \tag{2.2}
\]

Thus the unsigned integer determinant is nonzero exactly when no component
cycle has length divisible by four, and then
(|\det A_P|=2^c=\operatorname {per}A_P).

For every feasible degree-two graph there is an explicit signing of the
occurrence incidences for which the signed biadjacency determinant has
absolute value (2^c): leave an odd-(k) cycle unchanged, flip one
incidence on every even-(k) cycle, and give the two parallel incidences of
a two-cycle the same sign.

#### Proof

After ordering a (2k)-cycle alternately, its block is (I+S), where
(S) is a cyclic permutation matrix.  Hence
(det(I+S)=1-(-1)^k).  Flipping one incidence reverses the relative sign
of the two alternating matching terms.  Path blocks have one determinant
term.  Multiply over components. (square)

In particular, a four-cycle has two common transversals but unsigned
determinant zero.  Any theorem using the ordinary determinant without a
signing or independent variables would therefore be false.

## 3. Cap-two orientation and literal cut seams

Now specialize to the Catalan cap-two cycle.  Write the saturating cycle as

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,
\]

with the (C_i) distinct.  Let (H\subsetneq\mathbb Z_N) be the hosted
blocks.  In block (i\notin H), the middle cycle (P) has the sole edge

\[
                         s_i=C_iC_{i+1}.
\]

In block (i\in H), with inserted omitted facet (X_i\subset U_i), it has

\[
 e_i^-=C_iX_i\quad\text{(incoming)},\qquad
 e_i^+=X_iC_{i+1}\quad\text{(outgoing)}.                \tag{3.1}
\]

The upper-colour degrees of (G(P)) are therefore one off (H) and two on
(H).  Every common transversal selects (s_i) off (H) and exactly one
of (e_i^-,e_i^+) on (H).

### Theorem 3.1 (uniform outgoing criterion)

Define the canonical outgoing set

\[
        T_{\to}=\{s_i:i\notin H\}\sqcup\{e_i^+:i\in H\}. \tag{3.2}
\]

The following are equivalent.

1. (G(P)) has a uniformly outgoing common transversal.
2. (T_{\to}) is a perfect matching of (G(P)).
3. Every lower colour occurs exactly once among the distinguished edges in
   (3.2).
4. The literal directed-repair identity holds:

   \[
   \{C_i\cap C_{i+1}:i\notin H\}
     \sqcup
   \{X_i\cap C_{i+1}:i\in H\}
     ={[2m]\choose m-1}.                                \tag{3.3}
   \]

When it exists, the uniformly outgoing matching is unique among uniformly
outgoing choices, although (G(P)) may have additional mixed matchings on
cycle components.

#### Proof

The upper endpoint of every edge in block (i) is (U_i), so (3.2)
already meets every upper colour exactly once.  It is a perfect matching
exactly when its lower intersections are all distinct and exhaustive.
Those intersections are precisely the two families displayed in (3.3).
(square)

Uniform outgoing orientation is sufficient for distinct cut seams, but it
is not necessary.  The exact statement is the following.

### Theorem 3.2 (cut-seam threshold criterion)

For a common transversal, put (epsilon_i=0) if it selects (e_i^+) and
(epsilon_i=1) if it selects (e_i^-).  The opposite cut seam is

\[
 J_i=\begin{cases}C_i,&\epsilon_i=0,\\
                   C_{i+1},&\epsilon_i=1.
      \end{cases}                                       \tag{3.4}
\]

The seams (J_i), (i\in H), are pairwise distinct if and only if no two
cyclically consecutive hosted blocks have the pattern

\[
                         \epsilon_i\epsilon_{i+1}=10.   \tag{3.5}
\]

Because (H\ne\mathbb Z_N), this is equivalent to saying that the word on
every maximal cyclic hosted run is (0^*1^*).  Uniform outgoing and uniform
incoming are the two constant special cases.

#### Proof

Distinctness of the (C_i) implies that two cut seams can agree only when
their blocks share a boundary.  At the shared boundary (C_{i+1}), block
(i) chooses it exactly for bit one and block (i+1) chooses it exactly
for bit zero.  This is precisely (3.5).  A binary word has no descent (10)
exactly when it is (0^*1^*). (square)

Thus “cut seams are distinct if and only if the matching is uniformly
outgoing” is false; uniformity is a clean sufficient subcase of the exact
threshold theorem.

## 4. Exact relation to a three-level diamond-tight enumeration

Let (P=(A_0,A_1,\ldots,A_{M-1})) be a cyclic Hamilton ordering of all
rank-(m) sets.  A **(P)-respecting three-level enumeration** keeps this
middle projection and, between (A_i,A_{i+1}), may insert its unique lower
colour (ell_i), its unique upper colour (u_i), or both.  When both are
inserted, either

\[
 A_i,\ell_i,u_i,A_{i+1}
 \quad\text{or}\quad
 A_i,u_i,\ell_i,A_{i+1}                                \tag{4.1}
\]

is a Boolean diamond segment of total Hamming distance four.

Let (T^-) be the edges carrying the lower insertions and (T^+) the edges
carrying the upper insertions.  Enumerating each boundary layer once means
that (T^-) is a lower transversal and (T^+) an upper transversal, so
(|T^-|=|T^+|=N).  If (n_j) is the number of middle edges carrying exactly
(j) boundary insertions, then

\[
 n_0+n_1+n_2=M,\qquad n_1+2n_2=2N,
\]

and the cyclic Hamming distance is

\[
 2M+2n_2=4N+2n_0.                                      \tag{4.2}
\]

Hence the enumeration is tight, of distance (4N), if and only if

\[
               T^-\cup T^+=E(P),\qquad
               |T^-\cap T^+|=N-K,                     \tag{4.3}
\]

where (K=M-N).

Equation (4.3) is a **covering pair** of transversals, not a single common
transversal.  If one incorrectly uses a common transversal (T) for both,
then (n_2=N), (n_0=K), and the distance is (4N+2K), not tight.

The cap-two block structure supplies the missing complement canonically.
Call the enumeration **rigid cap-two diamond respecting** when

* every sole edge (s_i) carries both its lower and upper vertices; and
* in every split block, one of (e_i^-,e_i^+) carries the lower vertex and
  the other carries the upper vertex.

### Theorem 4.1 (rigid diamond equivalence)

For a cap-two cycle (P), common transversals of (G(P)) are in bijection
with rigid cap-two (P)-respecting diamond-tight enumerations of ranks
(m-1,m,m+1), up to the two local orders in each diamond segment.

Given a common transversal (T), use (T) for the lower insertions and use

\[
       T^{\mathrm{opp}}
        =\{s_i:i\notin H\}\sqcup(E(P)\setminus T)       \tag{4.4}
\]

for the upper insertions.  Conversely, the lower-marked edges of every rigid
cap-two diamond enumeration form a common transversal.

#### Proof

A common transversal contains the forced sole edge in every singleton upper
block and one of the two edges in every split upper block.  The set
(T^{\mathrm{opp}}) therefore also contains exactly one edge of every upper
block.  The two sets cover every physical edge and meet exactly in the
(N-K) sole edges.  The set (T) enumerates all lower colours and
(T^{\mathrm{opp}}) enumerates all upper colours, so (4.3) and the rigid
block rules hold.

Conversely, the lower-marked set in a rigid enumeration meets every lower
colour once by definition.  It also contains the sole edge of every
singleton upper block and one edge of every split upper block, hence meets
every upper colour once.  It is a common transversal. (square)

The rigid block qualifier is load-bearing.  A generic tight covering pair
can put both lower marks in one split upper block and none in another; its
lower transversal then need not be an upper transversal and therefore need
not be a matching of (G(P)).

For a uniformly outgoing common transversal, (4.4) is exactly the incoming
upper transversal.  This recovers the directed Catalan diamond normal form:
outgoing lower marks, incoming upper marks, and diamonds on the unmatched
sole blocks.

## 5. Independent finite replay

The dependency-free audit

```text
python3 scratch/audit_catalan_colour_incidence_graph_20260731.py
```

checks the following.

* On the authenticated positive (m=3) cycle, the complete graph has ten
  balanced path components and no cycles: seven one-edge paths, one
  three-edge path, and two five-edge paths.  Its permanent is one and its
  determinant is (-1).  Direct enumeration of all (2^5) block choices
  finds the same unique matching, uniformly outgoing.  The rigid diamond
  replay lists all ranks (2,3,4) exactly once and has cyclic Hamming
  distance (60=4{6\choose2}).
* On the frozen (m=4) SatCycle-derived cap-two fixture, the two shore
  degree histograms are

  \[
     {\cal L}:0^8 1^{26}2^{22},\qquad
     {\cal U}:1^{42}2^{14}.
  \]

  Eight isolated lower colours make the permanent and determinant zero.
  Direct enumeration of all (2^{14}) block choices finds no common
  transversal.  This is a negative calibration for that one host injection,
  not an (m=4) no-go.
* Exhausting every orientation word gives exact agreement between literal
  cut-seam distinctness and the no-(10) criterion: 24 of 32 words at
  (m=3), and 2592 of 16384 words in the frozen (m=4) fixture.
* Synthetic balanced/unbalanced paths, a parallel two-cycle, (C_4), and
  (C_6) verify the permanent and unsigned-determinant formulas.  In
  particular, (C_4) has permanent two and determinant zero.

The audit proves no recursive existence theorem.  It reduces that theorem
to constructing, for every (m), one cap-two (P) whose occurrence graph
has a perfect matching with the desired threshold orientation; uniform
outgoing is the canonical directed-repair subcase.
