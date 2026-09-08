# Joint graphic--gammoid Catalan gluing: the maximal integral face

Date: 2026-07-31  
Status: exact catalogue product, polynomial two-coordinate theorem,
dimension-uniform private-route sufficient theorem, and sharp abstract
counterexamples; the unmodified standard private-triple catalogue is known
not to exist already at `m=5`

## 0. Verdict

There are three independent combinatorial coordinates in a prepared
Catalan gluing choice:

1. the selected polygons must form a forest, ultimately a spanning tree, on
   the factor components;
2. their gained gap attachments must remain acyclic after the retained gap
   forest is contracted; and
3. the exposed common-core matching defects must admit a vertex-disjoint
   directed linkage.

On the strongest face on which each toggle has one component edge, one
effective gap edge and one selectable source in one fixed directed network
with a fixed **unpaired** sink bank, these are exactly two graphic matroids
and one gammoid on the toggle labels.  Thus the literal family is

\[
 \boxed{{\cal F}=I(M_C)\cap I(M_G)\cap I(M_L).}       \tag{0.1}
\]

This is not ordinary matroid intersection.  On three copied grounds it is
matroid matching with three-element blocks, or matroid `3`-parity.  The
general class already contains three-dimensional matching.

The maximal generic polynomial face justified by these three oracle
structures has at most two nonredundant coordinates.  In particular,
private gap sockets or an aligned component--gap image remove one graphic
row, leaving ordinary graphic--gammoid matroid intersection.  Its exact
rank criterion is

\[
 r_C(X)+r_L(T\setminus X)\ge q-1
 \qquad\hbox{for every }X\subseteq T,                \tag{0.2}
\]

where `q` is the number of factor components.

Three labels already give the sharp failure beyond this face: each pair of
rows has a rank-two common basis, but all three rows have common rank one.
The half vector has value `3/2`, the integer optimum is `1`, and the three
active rows have determinant `2`.

There is nevertheless a positive dimension-uniform theorem.  A connected,
prepared catalogue whose gap pieces are aligned one-edge images with only
private tree appendages and whose linkage sources have globally disjoint
private routes to distinct sinks is solved by **any** component spanning
tree.  This is an all-`m` theorem under a concrete catalogue hypothesis.  It
does not construct those catalogues and does not close physical socket
pairing, voltage, deeper shadows, residence or the compiler.

The word **prepared** includes global palette completeness.  Item 2172
proves that the unmodified standard MMM family fails before (0.1) at `m=5`:
both of its Hamilton outputs have only `81/84` turn colours on each shore and
miss the lower orbit `{73,146,292}`.  One output is locally all-six
transparent at both private glues, so local private attachments do not imply
entry to the product theorem.

## 1. The exact product

Let `T` be a prepared family of palette-, boundary- and trace-admissible
gluing toggles.  Preparation is global: a complete joint turn-occurrence
witness is supplied on the starting factor, and every label set under
consideration preserves it or repairs it through the declared linkage
network.  Local equality of the six port palettes is not enough.

Preparation also means that old private sockets have been deleted or
contracted independently of the choice, the retained cores are fixed, and
selecting compatible labels has the advertised component and attachment
effects.

### 1.1 Component coordinate

Let `K_C` be the auxiliary graph whose vertices are the current factor
components.  A label `t` has one edge

\[
                         c_t\in E(K_C).              \tag{1.1}
\]

The label sets which do not make a factor-component circuit are the
independent sets of the pullback graphic matroid

\[
 M_C=\{S\subseteq T:\{c_t:t\in S\}\text{ is a forest}\}.       \tag{1.2}
\]

If `K_C` has `q` vertices, a size-`q-1` independent set is a spanning tree.

### 1.2 Gap coordinate

Delete the lost local support edges from the old simple-support gap forest
and contract every retained tree component.  A label `t` contributes a
bundle `B_t` of gained attachment edges.  The exact gap-safe families are

\[
 {\cal I}_G=\left\{S\subseteq T:
       \bigcup_{t\in S}B_t\text{ is graphic-independent}\right\}.
                                                               \tag{1.3}
\]

For arbitrary bundles, (1.3) is a grouped pullback and need not be a
matroid.  On the **one-effective-edge face**, private leaf trees and series
paths are suppressed and every bundle has one remaining nonloop edge

\[
                         g_t\in E(K_G).              \tag{1.4}
\]

Then (1.3) is the graphic matroid

\[
 M_G=\{S\subseteq T:\{g_t:t\in S\}\text{ is a forest}\}.       \tag{1.5}
\]

Distinct support edges which become parallel after contraction remain
parallel; they form a genuine two-cycle.

### 1.3 Linkage coordinate

Freeze one directed alternating network `D`, one fixed sink bank `Z`, and a
distinct source vertex `s_t` for every selectable label.  No label changes
`D`, `Z` or the orientation.  Define

\[
 M_L=\{S\subseteq T:\{s_t:t\in S\}
       \text{ links vertex-disjointly to distinct vertices of }Z\}.
                                                               \tag{1.6}
\]

This is a gammoid on `T`: under the standard terminology it is a
restriction of the strict gammoid on the vertex-split network.  Its rank
oracle is one vertex-capacitated max flow.  The sinks are unpaired; the
linkage may choose its source--sink bijection.

Under (1.1), (1.4) and (1.6), a label set passes all three independence
coordinates if and only if it belongs to (0.1).  This is an exact equality,
not a relaxation.

### Theorem 1.1 (three-copy normal form)

Take three disjoint copies `T_C,T_G,T_L` of `T` and put

\[
                         N=M_C\oplus M_G\oplus M_L.  \tag{1.7}
\]

For every label set

\[
                  P_t=\{t_C,t_G,t_L\}.              \tag{1.8}
\]

Then `S` belongs to (0.1) if and only if

\[
                         \bigcup_{t\in S}P_t
             \quad\hbox{is independent in }N.       \tag{1.9}
\]

Thus the exact one-atom product is matroid `3`-parity.

#### Proof

Independence in a direct sum is coordinatewise.  The three copies of the
union in (1.9) are respectively the images of `S` in `M_C,M_G,M_L`, so
(1.9) is exactly (0.1). \(\square\)

## 2. The exact gammoid boundary

Item 2169's matching-gain theorem is correct.  If `M` is a matching in a
bipartite graph, orient unmatched edges left-to-right and matched edges
right-to-left.  After vertex splitting, a subset of exposed left vertices
is independent exactly when it can link to distinct exposed right vertices.
This is the gammoid used in (1.6), and full matching repair asks that its
rank equal the number of exposed left vertices.

Two qualifications are load-bearing.

1. This is a gammoid restriction, not necessarily a transversal matroid and
   not, on the exposed-source ground under the standard terminology,
   literally the whole strict gammoid.
2. It does not prescribe which source reaches which sink.

The complete boundary state of item 2169 is richer.  It records oriented
endpoint pairings of partial paths.  One gammoid oracle tests an unpaired
source set against a fixed sink bank; it does not test an arbitrary named
multicommodity pairing.

### Proposition 2.1 (smallest pairing separator)

Let the sources be `a,b`, the sinks be `c,d`, and let the only directed
paths be

\[
                          a\longrightarrow d,
             \qquad      b\longrightarrow c.        \tag{2.1}
\]

The unpaired source set `{a,b}` has gammoid rank two, but the named pairing
`(a,c),(b,d)` is impossible.

#### Proof

The two displayed paths are vertex-disjoint and use the two distinct sinks,
so the unpaired rank is two.  Neither requested named path exists.  With one
source there is no nontrivial pairing choice, so two sources and two sinks
are minimal. \(\square\)

Consequently the full pairing-resolved boundary signature must remain a
finite relation unless the catalogue supplies forced/direct pairings.  For
adhesion size `b` and `r` exposed sources on each shore, the relevant named
terminal parameter is at least

\[
                             p=b+2r,                 \tag{2.2}
\]

before endpoints of unassigned new edges are added.  A safe crude number of
oriented pairing patterns is `4^p p! = 2^{O(p log p)}`.  The tree-composition
theorem remains exact; the overreach would be to claim that its entire
pairing table comes from one max-flow call.

## 3. The maximal generic polynomial face

The phrase **generic face** below means a theorem which uses only the three
matroid oracles, with no additional algebraic correlation among their
representations.

### Theorem 3.1 (two-coordinate integral face)

Assume the prepared one-effective-edge/fixed-network hypotheses of Section
1.  If one of `M_C,M_G,M_L` is free on `T`, or its independent sets contain
the intersection of the other active rows, then the joint problem reduces
to ordinary intersection of at most two matroids and is polynomial and
integral.

In particular, suppose either

* the gap bundles lie on the private-socket face, so `M_G` is free; or
* component independence implies gap independence,
  \(I(M_C)\subseteq I(M_G)\).

Then a jointly safe Hamiltonizing set exists if and only if

\[
 \alpha:=\max\{|S|:S\in I(M_C)\cap I(M_L)\}=q-1.    \tag{3.1}
\]

Equivalently,

\[
 \boxed{r_C(X)+r_L(T\setminus X)\ge q-1
        \quad\text{for every }X\subseteq T.}         \tag{3.2}
\]

The set, or a violated rank partition, is computable in polynomial time
using a graphic oracle and vertex-capacitated flow.

#### Proof

Under either displayed hypothesis the gap row is redundant.  Edmonds'
matroid-intersection min--max theorem gives

\[
 \alpha=\min_{X\subseteq T}
             \bigl(r_C(X)+r_L(T\setminus X)\bigr).  \tag{3.3}
\]

The component rank is at most `q-1`, so (3.1) and (3.2) are equivalent.  A
size-`q-1` component forest is a spanning tree.  The gammoid oracle supplies
the required unpaired linkage, and the private or implied gap row supplies
gap acyclicity. \(\square\)

A concrete aligned sufficient condition for the second bullet is an
injective vertex map `iota:V(K_C)->V(K_G)` with

\[
 c_t=uv\quad\Longrightarrow\quad
 g_t=\iota(u)\iota(v).                               \tag{3.4}
\]

Then the two graphic matroids coincide on the label ground.

The symmetric faces are also polynomial:

* private/dedicated linkage makes `M_L` free, leaving ordinary
  graphic--graphic matroid intersection;
* an automatic component row leaves gap-graphic--gammoid intersection; and
* if all other rows are automatic while each label contributes a pair of
  effective edges to one graphic matroid, the remaining grouped choice is
  graphic matroid parity.

Two one-edge graphic rows may equivalently be written as matroid parity on
the pairs \(\{t_C,t_G\}\) in \(M_C\oplus M_G\), although ordinary matroid
intersection on `T` is the simpler algorithm.

### Theorem 3.2 (generic maximality)

Allowing all three rows in (0.1) to vary independently already contains
three-dimensional matching.  Hence, unless `P=NP`, no polynomial integral
theorem based only on the three unrestricted oracles extends Theorem 3.1 to
the full three-coordinate face.

#### Proof

Given a three-dimensional-matching instance
\(H\subseteq X\times Y\times Z\) with
\(|X|=|Y|=|Z|=n\), use `H` as the label ground.  Order
\(X=(x_1,\ldots,x_n)\) and make `K_C` the path
\(v_0v_1\cdots v_n\), with one parallel copy of edge
\(v_{i-1}v_i\) labelled by every triple containing \(x_i\).  Its graphic
matroid permits at most one label with first coordinate \(x_i\), and a
size-`n` independent set is a component spanning tree.  Use the analogous
parallel-edge path for the `Y` coordinate in `K_G`.

For every label `h=(x,y,z)`, create a source `s_h` with a direct arc to the
fixed sink `z`.  Vertex-disjoint linkage permits at most one chosen source
with third coordinate `z`.  Thus a joint component-spanning set of target
size \(q-1=n\) is exactly a perfect three-dimensional matching. \(\square\)

This is maximality of a generic oracle theorem, not a claim that every
special Catalan catalogue with three active rows is hard.

## 4. The smallest three-row obstruction

Take `T={a,b,c}` and target size two.  In the component graph let `b,c` be
parallel; in the one-effective-edge gap graph let `a,c` be parallel; and in
the fixed-sink gammoid let `a,b` compete for one sink while `c` reaches a
second sink.  All singletons are admissible.

### Theorem 4.1 (three-label Borromean obstruction)

The row bases are

\[
\begin{array}{c|c}
 M_C&ab,ac\\
 M_G&ab,bc\\
 M_L&ac,bc.
\end{array}                                           \tag{4.1}
\]

Every pair of rows therefore has one common rank-two basis, but no pair of
labels is independent in all three rows.  The joint rank is one.

#### Proof

The forbidden pairs are respectively `bc,ac,ab`, which exhaust the three
two-subsets of `T`.  Deleting any one row leaves the unique two-subset not
forbidden by the other two. \(\square\)

The natural rank relaxation contains

\[
 x_b+x_c\le1,qquad x_a+x_c\le1,qquad x_a+x_b\le1. \tag{4.2}
\]

Its coefficient matrix has determinant `2`; `x_a=x_b=x_c=1/2` has value
`3/2`, while the integer optimum is one.

This obstruction is minimum under local admissibility.  On fewer than three
loopless labels, target one has a common singleton, while target two on two
labels has only the full ground as a candidate; if every row has rank two,
that candidate is common.  The exhaustive audit over every labelled matroid
on at most three elements confirms that the first failure is
`(|T|,target)=(3,2)`.

The frozen independent note
`MATH_AUDIT_CATALAN_JOINT_THREE_MATROID_MINIMAL_COUNTEREXAMPLE_20260731.md`
gives the literal two graphic graphs, direct linkage network and exhaustive
minimality census.  It is an abstract catalogue counterexample, not a claim
that one physical Catalan collar realizes these three labels.

### Proposition 4.2 (first three-blocker exchange)

On `T={e,a,b,c}`, make `e,a` parallel in `M_C`, `e,b` parallel in `M_G`,
and make `e,c` compete for one linkage sink in `M_L`; leave every other pair
free.  Then `{a,b,c}` and `{e}` are joint-independent, but inserting `e`
into `{a,b,c}` requires deleting all three of `a,b,c`.

Consequently the joint family is not `2`-extendible and cannot be the
intersection of two matroids on the label ground.

#### Proof

After `e` is inserted, `a` violates the component row, `b` violates the gap
row and `c` violates the linkage row.  The blockers are distinct, so all
three must be removed.  Intersections of two matroids are `2`-extendible.
Four labels are minimum for one inserted element to have three distinct
blockers. \(\square\)

## 5. A positive all-dimension catalogue theorem

### Definition 5.1 (private aligned one-edge route catalogue)

For a fixed semilength `m`, such a catalogue consists of prepared compatible
labels `T_m` satisfying:

1. the advertised effects superpose for every subset: in particular every
   component spanning-tree set can be applied in some order while preserving
   one globally complete joint turn-occurrence witness and all frozen
   boundary and protected-trace guards; each label's component effect is one
   edge of a connected graph `K_C(m)`;
2. after the retained gap forest is contracted, its nonprivate attachment
   suppresses to the aligned edge (3.4); the remaining private trees have
   pairwise disjoint off-core interiors and each meets the full aligned
   effective-edge core in at most one vertex; and
3. in one fixed alternating network, every label `t` owns a directed path
   `P_t` from `s_t` to a distinct sink `z_t`, and the paths `{P_t:t in T_m}`
   are pairwise vertex-disjoint.

The last condition is stronger than gammoid feasibility: it gives a fixed
private linkage for every subset of labels.

### Theorem 5.2 (private catalogue gluing)

Every spanning tree `S` of `K_C(m)` in a private aligned one-edge route
catalogue simultaneously satisfies component graphic independence, gap
graphic independence and boundary linkage feasibility.

#### Proof

The component edges of `S` are a tree.  By (3.4), their effective gap images
are an isomorphic tree.  Adding pairwise private tree appendages, each
meeting the old union in at most one vertex, cannot create a gap cycle.  The
paths `{P_t:t in S}` are a subfamily of a vertex-disjoint family and end at
distinct sinks, so they give the required linkage. \(\square\)

### Corollary 5.3 (conditional all-`m` theorem)

If a private aligned one-edge route catalogue exists for every `m`, then a
jointly valid Hamiltonizing gluing choice exists for every `m` and is found
by an arbitrary spanning-tree algorithm.

The weaker private-socket/fixed-gammoid catalogue does not need globally
private routes: Theorem 3.1 decides it exactly by matroid intersection and
criterion (3.2).

### Proposition 5.4 (the standard `m=5` family is outside the face)

The canonical `m=5` MMM factor has three plane-tree components and three
standard nonexceptional labels.  Exactly two labelled spanning trees are
Hamiltonian.  Both final cycles attain only `81` of the required `84` turn
colours on each shore and both miss the lower period-three orbit

\[
          \{73,146,292\}
          =\{001001001,010010010,100100100\}.         \tag{5.1}
\]

Therefore neither standard output supplies the global preparation required
in Section 1.  This remains true although one tree is locally all-six
palette-transparent at both glues and has the disjoint lower triples

\[
                  \{82,84,88\},\qquad\{50,52,56\}.  \tag{5.2}
\]

#### Proof

The complete standard label census has exactly the two Hamilton trees.  The
literal turn maps of both have multiplicity histogram `1^36 2^45` on each
shore, hence `81` distinct colours, with the missing sets recorded in item
2172.  A missing turn colour has no representative, so no Catalan
decoration—and therefore no prepared catalogue state—exists.  The local
owner-palette and disjointness replay gives (5.2), locating the failure at
global palette surjectivity rather than at the private gap row. \(\square\)

The corrected search order is consequently

\[
 \boxed{\text{palette repair/nonstandard switch/different base factor}
 \longrightarrow\text{global occurrence witness}
 \longrightarrow\text{prepared graphic--gammoid catalogue}.} \tag{5.3}
\]

This is a positive theorem for the **joint central gluing product**.  It does
not assert existence of the catalogues, nor does it supply the final physical
path involution, connector capacities, primitive voltage, deeper-shadow
witnesses, residence or the common compiler cap.  Therefore it is not an
all-`k` contiguous-OR theorem by itself.

## 6. Reproducible audit

Run

```text
python3 scratch/audit_catalan_joint_graphic_gammoid_gluing_face_20260731.py
python3 scratch/audit_catalan_joint_three_matroid_minimal_counterexample_20260731.py
python3 scratch/audit_catalan_private_triple_standard_m5_refutation_20260731.py
```

The first replay checks the pairing separator, the three-label product, the
four-label blocker, the private-route implication on finite catalogues and
the matroid-intersection rank formula on an exhaustive small direct-linkage
family and imports the frozen `m=5` palette verdict.  The second independently
enumerates all labelled matroids on at most three elements and proves the
claimed minimality within the audited finite universe.  The third is the
complete standard-family census behind Proposition 5.4.

## 7. Source relation

This theorem uses and sharpens:

* `MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md` for
  matching gain and bounded boundary composition;
* `MATH_THEOREM_CATALAN_LEAF_PEELABLE_TRANSPARENT_GLUING_STATE_20260731.md`
  for the two graphic coordinates and the private/one-effective-edge faces;
* `MATH_THEOREM_CATALAN_JOINT_TRANSPARENT_GLUING_AND_M4_SOCKET_CLOSURE_20260731.md`
  for the separation of occurrence, linkage and physical socket states; and
* `MATH_THEOREM_R_CAP_TWO_CYCLE_SHIFT_LOCK_AND_GAP_HALL_20260731.md` for the
  full pairing-pattern parameter and its safe `4^p p!` bound; and
* `MATH_THEOREM_CATALAN_PRIVATE_TRIPLE_STANDARD_M5_REFUTATION_20260731.md`
  for the exact global-palette failure of the unmodified standard family.
