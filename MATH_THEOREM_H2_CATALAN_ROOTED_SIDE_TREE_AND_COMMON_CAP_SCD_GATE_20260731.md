# Rooted Catalan side trees and the exact common-cap SCD gate

Date: 2026-07-31  
Status: exact reformulation and exact augmentation criterion; explicit
orthogonal-SCD obstruction.  No all-parameter side-realization theorem is
claimed.

## 0. Verdict

Fix the upper punctured shore after a synchronized common basis has been
chosen.  Let

\[
 M={2n\choose n},\qquad N={2n\choose {n-1}},\qquad
 P={2n\choose {n-2}},
\]

\[
 K=M-N=\operatorname {Cat}_n,\qquad
 C=M-P=\operatorname {Cat}_{n+1}.
\tag{0.1}
\]

The observed condition \(c_0=0\) has an exact graphic formulation.  For a
spanning \(P\)-edge side forest \(J\) on the \(N\) side owners and its
\(C\)-set of seam anchors \(B\), adjoin a new root \(\rho\) adjacent to every
anchor.  Then

\[
 c_0(J,B)=0
 \quad\Longleftrightarrow\quad
 J\cup R\text{ is a spanning tree for some }
 R\subseteq\{\rho b:b\in B\},\ |R|=C-K.
\tag{0.2}
\]

The count is forced:

\[
 C-K=N-P,\qquad P+(C-K)=N.
\tag{0.3}
\]

Consequently one punctured shore is exactly a common base of two extended
palette partition matroids and one rooted graphic matroid, together with
the overlapping physical capacity row.  This is a three-matroid-plus-
\(b\)-matching face, not ordinary matroid intersection.

There is also an exact SCD compatibility statement.  Two SCDs provide the
two physical corners of one diamond only when they have a **pointwise common
two-step cap** and use its two opposite intermediate corners.  Edge
disjointness guarantees the latter but not the former.  Ordinary SCD
orthogonality does not guarantee the common cap; in its literal strongest
reading it forbids it, because the two cross-chains would meet at both the
bottom and the cap.  The frozen \(Q_4\) census gives a smaller explicit
failure: of 408 almost-orthogonal SCD pairs, 324 have repeated unions of
their two middle successors.

The remaining positive theorem is therefore Boolean-specific: choose a
common basis and a palette-perfect, capacity-feasible rooted graphic base
on each shore whose induced anchor pairings pass the alternating-cycle
test.  Nothing below proves that choice for every recursively supplied
**structural** forest.  The independent-`c`-rail theorem means that this
structural forest need not also supply the guard chronology: an independent
same-parameter Catalan filler may be chosen for that isolated rail.

## 1. The rooted-tree equivalence

Let \(V\) be a set of \(N\) side owners, \(B\subseteq V\) an anchor bank of
order \(C\), and \(J\) a set of \(P\) physical side edges.  Isolated owners
are included as components of \((V,J)\).  Write \(c_0(J,B)\) for the number
of components disjoint from \(B\).

### Theorem 1.1 (rooted side-tree identity)

The following are equivalent.

1. \((V,J)\) is a forest and \(c_0(J,B)=0\).
2. There is a set

   \[
   R\subseteq E_\rho:=\{\rho b:b\in B\},\qquad |R|=C-K=N-P,
   \tag{1.1}
   \]

   such that \(J\cup R\) is a spanning tree on \(V\cup\{\rho\}\).

For a fixed forest \(J\), the legal root sets are obtained by choosing
exactly one anchor from every component of \(J\).

#### Proof

If \(J\) is a \(P\)-edge forest on \(N\) vertices, it has \(N-P=C-K\)
components.  When every component contains an anchor, choose one such
anchor in every component and join it to \(\rho\).  The resulting graph is
connected and has

\[
 P+(N-P)=N
\]

edges on \(N+1\) vertices, hence is a spanning tree.

Conversely, remove \(R\) from the spanning tree \(J\cup R\).  The remaining
graph is the forest \(J\).  Every one of its components contains the anchor
incident with its former root edge.  Moreover a component cannot receive
two root edges, because their union with the unique path inside the
component would be a cycle.  Thus there is exactly one selected root edge
per component and \(c_0=0\).  The final assertion is the same
correspondence. \(\square\)

The forest hypothesis in statement 1 is essential.  Merely saying
\(c_0=0\) for a cyclic \(P\)-edge graph does not imply (1.1).  Equivalently,
one may use statement 2 itself as a single condition which enforces both
acyclicity and \(c_0=0\).

### Corollary 1.2 (charge and rooted anchor orientation)

Assume in addition that \(J\) has maximum degree two and every anchor has
degree at most one.  If \(c_0=0\), then

\[
 c_2=K,\qquad c_1=C-2K.
\tag{1.2}
\]

Every two-anchor component contains exactly one rooted and one unrooted
anchor.  Its unique root-to-unrooted path recovers the shore's induced
anchor pair.  Hence a legal root set orients, but does not alter, each of
the \(K\) pairing edges.

#### Proof

An anchor-capped linear-forest component has at most two anchors.  Counting
components and anchors gives

\[
 c_0+c_1+c_2=C-K,\qquad c_1+2c_2=C,
\]

so \(c_2-c_0=K\).  Put \(c_0=0\).  Theorem 1.1 chooses one root anchor in
each component.  A double-anchor component therefore leaves exactly its
other anchor unrooted, and the unique path between them is the asserted
pairing path. \(\square\)

## 2. Exact three-base plus capacity formulation

Fix the punctured lower palette

\[
 D\subseteq {[2n]\choose n},\qquad |D|=P,
\]

the full upper extreme palette

\[
 \mathcal U={[2n]\choose {n+2}},\qquad |\mathcal U|=P,
\]

and the inherited upper anchor bank

\[
 B\subseteq {[2n]\choose {n+1}},\qquad |B|=C.
\]

The unrestricted diamond-atom ground is

\[
 \mathcal A(D)=\{(L,U):L\in D,\ U\in\mathcal U,\ L\subset U\}.
\tag{2.1}
\]

For \(U-L=\{x,y\}\), put

\[
 \psi(L,U)=\{L+x,L+y\}.
\tag{2.2}
\]

Let \(M_L,M_U\) be the two partition matroids on \(\mathcal A(D)\),
with capacity-one blocks indexed respectively by \(L\) and by \(U\).  On
the augmented ground

\[
 \widehat{\mathcal A}=\mathcal A(D)\sqcup E_\rho
\]

define the rank-\(N\) partition matroids

\[
 \widehat M_L=M_L\oplus U_{C-K,E_\rho},\qquad
 \widehat M_U=M_U\oplus U_{C-K,E_\rho}.
\tag{2.3}
\]

Let \(M_{\rm gr}\) be the graphic matroid obtained by mapping a diamond
atom to (2.2) and a root atom \(\rho b\) to the corresponding root edge.
Parallel occurrences, if a restricted occurrence catalogue has them, are
kept as parallel graphic elements.  Finally define

\[
 b_v=\begin{cases}1,&v\in B,\\2,&v\notin B,
 \end{cases}
\qquad
 \mathcal I_b=
 \left\{J:\ |J\cap\delta(v)|\le b_v\text{ for every }v\right\}.
\tag{2.4}
\]

### Theorem 2.1 (rooted rainbow graphic face)

A set \(J\subseteq\mathcal A(D)\) is an exact palette-saturating,
anchor-capped linear side forest with \(c_0=0\) if and only if there is
\(R\subseteq E_\rho\) such that, for \(T=J\cup R\),

\[
 T\in\mathcal B(\widehat M_L)
       \cap\mathcal B(\widehat M_U)
       \cap\mathcal I(M_{\rm gr}),
 \qquad J\in\mathcal I_b.
\tag{2.5}
\]

The two partition-base rows force \(|T|=N\).  Hence graphic independence
on the specified \(N+1\) vertices is equivalent to saying that \(T\) is a
spanning tree.  In every feasible instance it is therefore also a basis of
the restricted graphic matroid.

#### Proof

A base of \(\widehat M_L\) contains one atom of every \(L\)-block and
exactly \(C-K\) root atoms.  A base of \(\widehat M_U\) gives the same
root count and one atom of every \(U\)-block.  Their common bases therefore
select a containment perfect matching between the two palettes and
\(C-K\) root edges.  The graphic-base row and Theorem 1.1 are exactly
physical acyclicity plus \(c_0=0\).  The inequalities (2.4) are exactly
maximum degree two away from the inherited seams and maximum degree one at
the anchors.  These are all side conditions. \(\square\)

This is not ordinary two-matroid intersection.  Even before (2.4), (2.5)
intersects two partition bases and a graphic base.  The sets
\(\delta(v)\) in (2.4) overlap whenever an atom touches two capped owners;
the resulting matching/\(b\)-matching system is not a matroid in general.
The rooted graphic row removes the separate nonlinear phrase
``every component has an anchor'', but it does not remove the physical
degree row.

### Quantifier warning 2.2 (unrestricted versus direct-edgewise banks)

The automatic two-coordinate common-basis theorem concerns the full
two-step containment transversal matroids, hence the unrestricted atom
ground (2.1).  It does **not** imply a common basis in the smaller
child-edge occurrence graphs consisting only of atoms \(q\uparrow x\) and
\(q\downarrow x\).  The strict direct-edgewise theorem proves separate
degree and one-sided Hall laws for those graphs and verifies a finite
recursive chain, but its coupled restricted common-basis row remains an
additional hypothesis.

Thus (2.5) is unconditional after an automatic common basis only in the
unrestricted side catalogue.  If ``strict recursion'' means the literal
child-edge-only catalogue, incidence availability must remain in the
state.

### Corollary 2.3 (strict direct-edgewise rooted face)

For a fixed `Q`, replace `\mathcal A(D)` in Theorem 2.1 by the allowed
direct occurrences

\[
 \mathcal E_Q^-=\{(q,x):x\notin U_q,\ L_q+x\in D\}.
\]

Restrict the two palette partition matroids and the physical-edge map to
this ground. Then (2.5) remains an exact characterization of the strict
upper shore. It is conditional on all palette blocks being simultaneously
saturable; Quantifier Warning 2.2 says precisely that this restricted
incidence row is not automatic.

### Theorem 2.4 (the rooted row is a Higgs-lift matroid)

Let `\widehat M` be the labelled graphic matroid of the full augmented
candidate multigraph on the occurrence ground `E` and root-star ground
`R=E_\rho`. Put

\[
 L=\widehat M\backslash R,\qquad Q_0=\widehat M/R.
\]

Then `Q_0` is a quotient of `L`. Assume the augmented candidate graph is
connected and `r(L)\ge P`. Its `K`-th Higgs lift

\[
 \mathcal H=H^K_{Q_0,L},\qquad
 r_{\mathcal H}(X)=
 \min\{r_{Q_0}(X)+K,\ r_L(X)\},                       \tag{2.6}
\]

has rank `P`, and its `P`-element bases are exactly the side-edge sets `J`
which are forests and satisfy `c_0(J,B)=0`.

#### Proof

The root star is independent of rank `C`. Connectivity gives

\[
 r(Q_0)=r(\widehat M)-C=N-C,\qquad
 (N-C)+K=P.
\]

For `|J|=P`, equation (2.6) has value `P` exactly when

\[
 r_L(J)=P,\qquad r_{Q_0}(J)=N-C.
\]

The first equality says that `J` is a forest. By contraction rank,

\[
 r_{Q_0}(J)=r_{\widehat M}(J\cup R)-C.
\]

The second equality therefore says that `J\cup R` has full graphic rank
`N`, equivalently every component of `J` meets the root star at an anchor.
This is `c_0=0`. \(\square\)

Thus the rooted forest row alone is one honest matroid base condition. The
full upper shore remains the intersection of this Higgs base with both
palette partition bases and the overlapping physical `b`-capacity row.
Theorem 3.2 shows that this intersection is not itself a matroid or an
equicardinal delta-matroid.

## 3. An exact rooted graphic augmentation test

Fix a rooted tree \(T=J\cup R\).  Let a palette-preserving packet replace
\(A\subseteq T\) by equally many distinct allowed atoms
\(E\subseteq\widehat{\mathcal A}\setminus T\), and for each
\(e\in E\) let \(C_T(e)\) be its fundamental cycle with respect to \(T\).
Form the binary matrix

\[
 X_{A,E}=\bigl(\mathbf 1[a\in C_T(e)]\bigr)_{a\in A,e\in E}.
\tag{3.1}
\]

### Theorem 3.1 (fundamental-cycle packet criterion)

For \(|A|=|E|\),

\[
 T-A+E\text{ is a spanning tree}
 \quad\Longleftrightarrow\quad
 X_{A,E}\text{ is nonsingular over }\mathbf F_2.
\tag{3.2}
\]

If only side palette atoms are changed, palette exactness is preserved
exactly when the symmetric difference of their old and new
\((L,U)\)-edges is a union of alternating cycles in the bipartite
palette-incidence graph.  Root-star exchanges may
be included as additional columns and rows in (3.1).  The packet is a
legal side augmentation exactly when (3.2), the two palette ledgers and
the capacities (2.4) all hold.

#### Proof

Represent the graphic matroid over \(\mathbf F_2\) and row-reduce the
columns of the basis \(T\) to the identity.  The coordinate column of a
nonbasis edge \(e\) is the incidence vector of its fundamental cycle
\(C_T(e)\).  Replacing the basis columns indexed by \(A\) with the columns
indexed by \(E\) gives a basis exactly when the minor on rows \(A\) and
columns \(E\) is nonsingular.  This is (3.2).  The symmetric difference of
two perfect matchings in a bipartite graph is a disjoint union of
alternating cycles, proving the palette assertion. \(\square\)

The theorem is a complete audit and augmentation test, not an augmenting
**existence** theorem: an alternating palette circuit may have singular
graphic exchange matrix, and a nonsingular packet may violate a physical
capacity.

### Theorem 3.2 (a whole alternating circuit is sometimes minimal)

On the authenticated `n=3` child, retain child edge `1` and let
`Q=E(F)-{1}`. There are two strict upper rooted selections, in occurrence
ids,

\[
 A=\{4,5,11,16,17,18\},\qquad
 B=\{5,6,9,17,18,19\}.                               \tag{3.3}
\]

Both satisfy both palettes, all physical capacities and `c_0=0`. The same
nine root anchors

\[
 \{23,27,30,39,45,53,54,57,60\}
\]

extend each one to a spanning tree. Their symmetric difference is the
single alternating palette `C_6`

\[
                   [4,19,16,9,11,6].                 \tag{3.4}
\]

For `e=16\in A-B`, no `f\in B-A` makes `A-e+f` palette-exact. In fact full
symmetric exchange fails, so the feasible rooted selections are neither
the bases of one matroid nor the equicardinal feasible sets of a
delta-matroid.

Deleting `A-B` from the rooted tree leaves four components, and the three
edges `B-A` contract to a tree on those components. Thus the whole `C_6` is
the exact graphic augmentation unit in this example.

#### Proof

The retained audit reconstructs all occurrences from the literal child,
checks the two palette sets, degrees, anchor components and both rooted
trees, and exhausts every one- and two-toggle symmetric exchange. The last
claim is the component-contraction form of Theorem 3.1. \(\square\)

## 4. Two intermediate injections and common caps

Let \(\pi:D\to\mathcal U\) be a containment bijection.  Every interval
\([L,\pi(L)]\) contains exactly two rank-\((n+1)\) corners.

### Theorem 4.1 (two-intermediate equivalence)

The physical lift of \(\pi\) has maximum degree at most two if and only if
its edges can be ordered as maps

\[
 f_0,f_1:D\longrightarrow {[2n]\choose {n+1}}
\tag{4.1}
\]

such that

\[
 L\subset f_i(L),\qquad f_0(L)\ne f_1(L),
\tag{4.2}
\]

\[
 f_0(L)\cup f_1(L)=\pi(L),qquad
 f_0(L)\cap f_1(L)=L,
\tag{4.3}
\]

and both \(f_0,f_1\) are injective.  The lift is a forest if and only if
the directed graph

\[
 f_0(L)\longrightarrow f_1(L)
\tag{4.4}
\]

has no directed cycle, under a component-consistent orientation (paths
consistently and cycles cyclically).  The anchor
cap is the additional condition that no anchor belongs to the combined
images more than once.

#### Proof

If the lift has maximum degree two, each path or cycle component can be
oriented consistently.  Take its tail and head as \(f_0(L),f_1(L)\).
Indegree and outdegree at most one give the two injections, while the
intersection and union recover the diamond colours.  Conversely, the two
injections give indegree and outdegree at most one, hence undirected degree
at most two.  A directed cycle is then exactly an undirected cycle of the
lift. \(\square\)

### Theorem 4.2 (exact two-SCD common-cap condition)

Let \(\mathcal D_0,\mathcal D_1\) be two saturated chain decompositions
having the same deep rank-\(n\) bank \(D\).  For \(L\in D\), let
\(f_i(L)\) and \(g_i(L)\) be respectively its first and second upward
successors in \(\mathcal D_i\).  The two SCD segments are the two opposite
paths through one diamond matching if and only if

\[
 g_0(L)=g_1(L)=:\pi(L)\qquad(L\in D),
\tag{4.5}
\]

and

\[
 f_0(L)\ne f_1(L)\qquad(L\in D).
\tag{4.6}
\]

The common cap map \(\pi\), and each intermediate map \(f_i\), are
injective automatically.  If the two SCDs are edge-disjoint, (4.6) is
automatic, but (4.5) is not.

#### Proof

A saturated chain contains at most one vertex of any fixed rank.  Thus its
first- and second-successor maps are injective.  Under (4.5), the interval
from \(L\) to \(\pi(L)\) has rank difference two and exactly two
intermediate corners.  Condition (4.6) says the two chains use the two
different corners, proving sufficiency.  Necessity follows by reading the
bottom, two corners and cap of a common diamond.  If the SCDs are
edge-disjoint, equality of the first successors would repeat the first
cover edge, so (4.6) holds.  No edge-disjointness statement constrains the
two distinct second successors, so it does not imply (4.5). \(\square\)

### Corollary 4.3 (ordinary orthogonality is the wrong relation)

Strict SCD orthogonality is incompatible with (4.5) at every non-extreme
two-step interval: the chain of \(\mathcal D_0\) containing \(L\) and the
chain of \(\mathcal D_1\) containing \(L\) would intersect at both
\(L\) and \(\pi(L)\).  Almost orthogonality has the same conclusion away
from its permitted common extreme pair.

If instead one uses orthogonality only to obtain the two first-successor
injections and defines

\[
 \pi(L):=f_0(L)\cup f_1(L),
\tag{4.7}
\]

then the missing condition is injectivity of (4.7).  Ordinary
orthogonality does not imply it.

#### Exact \(Q_4\) witness

The following two almost-orthogonal SCDs are written as comma-separated
chains:

\[
\begin{aligned}
\mathcal D={}&(\varnothing,1,12,123,1234),
 (2,23,234),(3,13,134),(4,14,124),(24),(34),\\
\mathcal E={}&(\varnothing,4,24,234,1234),
 (1,14,134),(2,12,124),(3,23,123),(13),(34).
\end{aligned}
\tag{4.8}
\]

Their rank-one successor maps are

\[
\begin{array}{c|cccc}
L&1&2&3&4\\ \hline
f_{\mathcal D}(L)&12&23&13&14\\
f_{\mathcal E}(L)&14&12&23&24.
\end{array}
\tag{4.9}
\]

Both rows are injective and differ pointwise, but

\[
 \pi(1)=\pi(4)=124,
 \qquad
 \pi(2)=\pi(3)=123.
\tag{4.10}
\]

The exact local enumerator finds all 240 SCDs of \(Q_4\), 408 unordered
almost-orthogonal pairs, and 324 pairs failing union injectivity.  Hence
neither ordinary orthogonality nor the weaker edge-disjointness statement
supplies the required common-cap/union-perfect row.

The complete `Q_4` census also shows that edge-disjointness is a viable
ambient class once the missing equality is imposed: among 1,236
edge-disjoint SCD pairs, exactly 180 satisfy the pointwise common-cap
condition (4.5), and 144 of those have an acyclic opposite-corner physical
graph. This is a finite compatibility fixture, not an all-dimensional
construction and not a rooted-anchor certificate.

## 5. Scope and surviving theorem

The upper-shore target can now be stated without hidden topology:

1. choose an automatic common basis \(Q\) in the unrestricted incidence
   model;
2. choose a common base (2.5), or a stronger opposite-corner common-cap SCD
   pair realizing it;
3. expose the \(K\) rooted double-anchor paths as the upper partial
   involution;
4. choose the lower shore so that the union of its partial involution with
   the upper one has no alternating cycle.

The last row is itself an exact, but different, graphic condition.  Put
\(V=\operatorname{comp}(F-Q)\), let \(\mu_-\) be the upper anchor-pair
matching and \(\mu_+\) the lower one.  Here
\(|\mu_-|=K\) because \(c_0^-=0\), while in general
\(|\mu_+|=K+c_0^+\).  Contract \(\mu_-\) and retain loops and parallel
images of \(\mu_+\).  Then

\[
 \beta(\Gamma_Q)=\beta(\mu_-\cup\mu_+)
 =\beta(\overline{\mu_+}\text{ on }V/\mu_-).
\tag{5.1}
\]

Equivalently, if \(\alpha,\delta\) are the two partial involutions, the
combined physical graph is acyclic exactly when \(\delta\alpha\) has no
periodic orbit on its iterated domain.  A lower exchange is topology-safe
exactly when, after its old quotient links \(\overline X\) are removed, its
new quotient links \(\overline Y\) are graphic-independent over the
residual forest.  Necessarily \(X\) meets every old alternating cycle, so

\[
 |X|\ge \beta(\Gamma_Q).                              \tag{5.2}
\]

This lower quotient test is not the fundamental-cycle test (3.1): (3.1)
preserves the upper rooted tree, whereas (5.1) governs the lower pairing
relative to the already fixed upper matching.  Neither implies the other.
The lower criterion is proved and independently replayed in
`MATH_THEOREM_H2_CATALAN_ROOTED_UPPER_AND_LOWER_QUOTIENT_GRAPHIC_GATE_20260731.md`.
It does not supply the required palette- and cap-preserving physical packet.

For the direct-edgewise recursive subclass, step 1 must additionally be
available inside its restricted occurrence catalogue.  The exact
fundamental-cycle matrix (3.1) is a proof-safe packet test for modifying a
candidate, but no theorem here guarantees a nonsingular, capacity-safe
packet in every dimension.

### Two-parent quantifier

Write `F` for the structural parent that supplies `Q`, the direct side
occurrence banks, the punctured `z`-rail and both seam families.  The
isolated `c`-rail may be `c+G` for any Catalan linear forest `G` at the same
parameter.  Its two palettes and physical components direct-sum with the
three-sector construction based on `F`.  Consequently the rooted
Higgs/palette/cap selection above is a condition on `F` alone, while body
residence on the `c`-rail is a condition on `G` alone.

This is an exact quantifier separation, not a new existence theorem.  A
strict induction may seek

1. a structural `F` admitting the rooted rainbow side selection and the
   lower quotient test; and
2. independently, a same-parameter `G` carrying the required output-depth
   guard.

Any no-go obtained by forcing `G=F` is therefore only a fixed-filler
obstruction.  Motif-safe `z` and side sectors, seam residence, deep shadows
and compiler ownership remain coupled to the structural choice.  The exact
substitution theorem and finite replay are in
`MATH_THEOREM_CATALAN_INDEPENDENT_C_RAIL_FILLER_20260731.md`.

Formally, let `S_n(h)` be the set of structural tuples
`(F,Q,S^-,S^+)` whose complementary three-sector support has all required
palettes, topology and guard-`h` predicates, and let `G_n(h)` be the set of
guard-`h` Catalan fillers.  Because the `c`-rail is a union of whole
components on a disjoint vertex set, the outputs valid for the palette,
topology and component-local guard rows are exactly

\[
                         S_n(h)\times G_n(h).          \tag{5.3}
\]

Thus nonemptiness factors into two independent existence questions.  The
rooted/Higgs theorem attacks the physical-topology row inside `S_n(h)`;
it imposes no additional restriction on `G_n(h)`.  This Cartesian-product
law is the usable gain over the one-parent formulation.

Accordingly, this note proves neither an all-\(n\) side realization nor the
full Catalan linear matching conjecture.  It isolates the missing supply as
a rooted rainbow graphic \(b\)-matching/common-cap construction, followed
by the already exact alternating-permutation topology test.

## 6. Audit and references

The explicit \(Q_4\) counts and witness are independently replayed by

```text
scratch/enumerate_q4_oscd.py
```

with output

```text
scds 240
pairs 408 bad_pairs 324
```

The stronger common-cap/edge-disjoint census is independently replayed by

```text
scratch/audit_h2_catalan_common_cap_scd_compatibility_20260731.py
scratch/h2_catalan_common_cap_scd_compatibility_20260731.audit.json
```

The rooted `n=3` alternating-circuit obstruction is independently replayed
by

```text
scratch/audit_h2_catalan_rooted_side_tree_c6_20260731.py
scratch/h2_catalan_rooted_side_tree_c6_20260731.audit.json
```

The Higgs-lift identification is exhaustively checked on the same strict
`n=3` ground by

```text
scratch/audit_h2_catalan_rooted_side_higgs_n3_20260731.py
scratch/h2_catalan_rooted_side_higgs_n3_20260731.audit.json
```

The lower quotient/alternating-permutation reduction is independently
checked by

```text
scratch/audit_h2_catalan_rooted_upper_alternating_lower_20260731.py
scratch/h2_catalan_rooted_upper_alternating_lower_20260731.audit.json
```

The independent-`c`-rail substitution is replayed by

```text
scratch/audit_catalan_independent_c_rail_filler_20260731.py
scratch/catalan_independent_c_rail_filler_20260731.audit.json
```

The detailed earlier audit is

```text
ORTHOGONAL_SCD_TWO_SDR_AUDIT.md
```

Background on orthogonal SCD terminology only:

* Hunter Spink, [*Orthogonal Symmetric Chain Decompositions of
  Hypercubes*](https://arxiv.org/abs/1706.08545).
* Karl Däubel, Sven Jäger, Torsten Mütze and Manfred Scheucher,
  [*On orthogonal symmetric chain decompositions*](https://arxiv.org/abs/1810.09847).
* Petr Gregor, Sven Jäger, Torsten Mütze, Joe Sawada and Kaja Wille,
  [*Gray codes and symmetric chains*](https://arxiv.org/abs/1802.06021).

The present common-cap obstruction and rooted-tree formulation are proved
above and do not rely on an unquoted claim from either paper.
