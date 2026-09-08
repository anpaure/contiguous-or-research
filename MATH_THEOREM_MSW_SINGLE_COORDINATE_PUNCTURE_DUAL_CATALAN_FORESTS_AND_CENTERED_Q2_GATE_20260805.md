# MSW single-coordinate puncture: dual Catalan forests and the centered-q2 gate

**Date:** 2026-08-05  
**Method:** pure mathematics; exact path slicing and Boolean-layer counting;
no computation, search, solver, or probabilistic input  
**Status:** unconditional puncture theorem and exact completion criteria.  A
single coordinate puncture of the canonical MSW complementary-geodesic
forest produces two different spanning Catalan path forests on the odd
middle layer: one is upper-exact and one is lower-injective.  Their
identification is exactly a centered occurrence-labelled `q=2` problem.
The theorem does not prove that either forest has both properties.

## 0. Setting and outcome

Let `Omega` have order `2r`, fix `z in Omega`, and put

\[
 \Omega_z=\Omega\setminus\{z\},\qquad
 V={2r-1\choose r},\qquad
 C=\operatorname {Cat}_r={1\over r+1}{2r\choose r},
\tag{0.1}
\]

and

\[
 U={2r-1\choose r+1}=V-C=V{r-1\over r+1}.
\tag{0.2}
\]

Take the canonical MSW family of `C` vertex-disjoint complementary
Johnson geodesics partitioning `binom(Omega,r)`.  Write one path as

\[
 M_j=\{\lambda_{j+1},\ldots,\lambda_r\}
       \cup\{\rho_1,\ldots,\rho_j\},\qquad 0\le j\le r,
\tag{0.3}
\]

where the two ordered rails partition `Omega`.  Its intervening rank-
`(r+1)` vertices are

\[
 Y_j=M_j\cup M_{j+1},\qquad 0\le j<r.
\tag{0.4}
\]

The `Y_j`, over all MSW paths, enumerate `binom(Omega,r+1)` exactly once.

The puncture has two exact projections.

1. The owners avoiding `z` form an **upper-exact outward-geodesic
   Catalan forest** `A_z` on `binom(Omega_z,r)`.
2. The part of the alternating MSW paths containing `z`, after deleting
   `z`, forms a spanning `C`-path cover `H_z` of the middle-levels
   incidence graph between `binom(Omega_z,r-1)` and
   `binom(Omega_z,r)`.  Suppressing its internal lower vertices gives a
   **lower-injective outward-geodesic Catalan forest** `B_z` on the same
   owner set.

Both forests have `V` vertices, `U=V-C` edges and `C` components.  The
first controls upper colours and the second controls lower colours.  The
upper colours of `B_z` are exactly the centered-at-`z` punctures of the
MSW `q=2` windows.  Thus the desired correlated lift is literally the
problem of making these two exact marginal structures coincide, or of
rethreading between them without losing either palette.

## 1. Exact A/B sector ledger on one complementary geodesic

There are two cases.

* If `z=lambda_a`, then

  \[
   z\in M_j\iff j<a.
  \tag{1.1}
  \]

  The `B` sector is `M_0,...,M_(a-1)` and the `A` sector is
  `M_a,...,M_r`.

* If `z=rho_b`, then

  \[
   z\in M_j\iff j\ge b.
  \tag{1.2}
  \]

  The `A` sector is `M_0,...,M_(b-1)` and the `B` sector is
  `M_b,...,M_r`.

In either case both sectors are nonempty contiguous geodesics.  If `a_x`
and `b_x` denote their numbers of owner vertices on path `x`, then

\[
 a_x+b_x=r+1.
\tag{1.3}
\]

There is exactly one A/B transition.  Its intervening upper vertex
contains `z`; after deleting `z` it is exactly the boundary owner of the
`A` sector.

### Theorem 1.1 (global sector counts)

Over all `C` paths,

\[
 \sum_x a_x=\sum_x b_x=V,
 \qquad
 \sum_x(a_x-1)=\sum_x(b_x-1)=V-C=U.
\tag{1.4}
\]

#### Proof

The rank-`r` owners avoiding `z` are exactly `binom(Omega_z,r)`, of order
`V`.  The owners containing `z`, after deleting it, are exactly
`binom(Omega_z,r-1)`, also of order `V`.  The MSW paths partition the
whole rank-`r` layer, proving the first two equalities.  There are `C`
nonempty sectors of each type, so subtracting one edge per sector proves
the second pair.  Equation (0.2) gives the last equality.  \(\square\)

This is an exact balance, not an average over the choice of puncture.

## 2. The A-sector upper-exact Catalan forest

Let `A_z` retain, on every path, the owners avoiding `z` and the Johnson
edges between consecutive such owners.

### Theorem 2.1 (upper-exact geodesic projection)

`A_z` is a spanning linear forest on `binom(Omega_z,r)` with exactly `C`
outward-geodesic components and `U` edges.  Moreover

\[
 \boxed{\{X\cup Y:XY\in E(A_z)\}={\Omega_z\choose r+1}}
\tag{2.1}
\]

with every upper colour occurring exactly once.

#### Proof

Each A-sector is a contiguous subpath of a complementary Johnson
geodesic, hence is itself an outward geodesic from either endpoint.  The
sectors partition every rank-`r` owner avoiding `z`, and Theorem 1.1 gives
the edge and component counts.

An MSW edge union avoids `z` if and only if both its endpoints avoid `z`.
The complete MSW upper palette enumerates every rank-`(r+1)` subset of
`Omega` once.  Restricting to the upper sets avoiding `z` therefore gives
exactly (2.1).  \(\square\)

Thus the puncture already gives the entire upper-exact, geodesic Catalan
forest required in the factor-first segmentation theorem.  What it does
**not** give automatically is injectivity of the edge-intersection
colours.  That issue cannot be removed by counting: `A_z` has exactly the
right number `U` of edges, but different edges can in principle have the
same rank-`(r-1)` intersection.

There is, however, an exact pointwise criterion for this row.  For
`q in binom(Omega,r-1)`, let `mu(q)` be the number of original MSW edges
with intersection `q`.  Write such an edge uniquely as

\[
 (q+\{a\})(q+\{b\})
\tag{2.2}
\]

and associate to it the pair `{a,b} subseteq Omega-q`.  Let `S(q)` be the
union of all these pairs.

### Theorem 2.2 (lower fibres are coordinate matchings)

For fixed `q`, the pairs in (2.2) are pairwise disjoint.  Consequently the
multiplicity of `q` among the A-edges is

\[
 \mu_z^A(q)=
 \begin{cases}
 0,&z\in q,\\
 \mu(q)-1,&z\notin q\text{ and }z\in S(q),\\
 \mu(q),&z\notin q\text{ and }z\notin S(q).
 \end{cases}
\tag{2.3}
\]

In particular, `A_z` has injective lower colours if and only if both of
the following hold:

1. every `q` with `mu(q)>=3` contains `z`;
2. whenever `mu(q)=2` and `z notin q`, one has `z in S(q)`.

#### Proof

If two pairs for `q` shared `a`, the corresponding two edges would both
be incident with the unique owner `q+{a}`.  Along one complementary
geodesic, membership of each coordinate changes exactly once: an initial
rail coordinate is deleted once and a final rail coordinate is inserted
once.  Hence at a fixed owner there is at most one incident edge which
changes membership of `a`.  This proves disjointness.

An edge of the fibre survives in `A_z` exactly when `z` belongs neither to
`q` nor to its associated pair.  If `z notin q`, disjointness says that it
lies in zero or one fibre pair, giving (2.3).  The final characterization
is the condition `mu_z^A(q)<=1` for every `q`.  \(\square\)

Thus the first direct-completion gate is a very rigid one-coordinate
transversal condition on the heavy lower fibres.  Aggregate collision
energy alone does not decide whether such a coordinate exists.

## 3. The B-sector incidence cover and its lower-injective suppression

Instead of keeping only owner vertices, retain from each original
alternating path all vertices containing `z`, both the rank-`r` vertices
`M_j` and the rank-`(r+1)` vertices `Y_j`, and then delete `z` from every
retained set.  Call the result `H_z`.

### Theorem 3.1 (punctured middle-levels path cover)

`H_z` is a spanning `C`-component path cover of

\[
 {\Omega_z\choose r-1}\longleftrightarrow
 {\Omega_z\choose r}.
\tag{3.1}
\]

Every component contains equally many vertices on the two shores.  Its
endpoints are:

1. the `A`-boundary owner, obtained from the unique crossing upper vertex;
2. the puncture of the `z`-containing complementary endpoint, on the
   rank-`(r-1)` shore.

#### Proof

On one geodesic the owner membership of `z` is the interval (1.1) or
(1.2).  The upper vertices containing `z` extend that interval through
the unique crossing upper vertex.  The retained alternating vertices
therefore form one path, not several pieces.  It has one upper vertex for
each retained owner vertex, so its shore sizes agree.

Every rank-`(r-1)` subset `q` of `Omega_z` occurs exactly once because
`q+z` is one rank-`r` owner of the partition.  Every rank-`r` subset `R`
of `Omega_z` occurs exactly once because `R+z` is one rank-`(r+1)` upper
vertex of the exact MSW upper palette.  Hence the paths span both shores
of (3.1).  The endpoint description is immediate from the unique crossing
and from complementation of the original geodesic endpoints.  \(\square\)

Suppress every internal rank-`(r-1)` vertex of `H_z`.  This gives a
Johnson forest `B_z` on `binom(Omega_z,r)`.

### Corollary 3.2 (lower-injective geodesic projection)

`B_z` is a spanning outward-geodesic forest with `C` components and `U`
edges.  Its edge intersections are all distinct.  They are exactly the
rank-`(r-1)` vertices of `H_z` except its `C` terminal lower endpoints.

#### Proof

A component with `b_x` vertices on each incidence shore suppresses to a
path with `b_x` owner vertices and `b_x-1` edges.  The suppressed edge at
an internal lower vertex `q` joins its two distinct rank-`r` supersets and
therefore has intersection exactly `q`.  Different edges use different
lower vertices of the path cover, proving injectivity.  The explicit rail
formula (0.3), read from the crossing toward the `z`-containing endpoint,
shows that every step deletes a new rail label and inserts a new rail
label; hence every component is an outward geodesic.  The counts follow
from Theorem 1.1.  \(\square\)

The two puncture forests therefore satisfy complementary exact rows:

\[
\begin{array}{c|c|c}
 &\text{lower edge colours}&\text{upper edge colours}\\ \hline
 A_z&\text{uncontrolled}&\text{all, exactly once}\\
 B_z&\text{all but `C`, injectively}&\text{centered `q=2`, uncontrolled}.
\end{array}
\tag{3.2}
\]

## 4. The centered-q2 identity

Take two consecutive owner vertices of the suppressed B-forest.  Before
puncturing they are consecutive upper vertices

\[
 Y_{j-1}=M_{j-1}\cup M_j,qquad
 Y_j=M_j\cup M_{j+1},
\tag{4.1}
\]

and the suppressed lower vertex is `M_j-z`.  Therefore

\[
 (Y_{j-1}-z)\cup(Y_j-z)
 =\bigl(M_{j-1}\cup M_j\cup M_{j+1}\bigr)-z.
\tag{4.2}
\]

The right side is precisely a punctured MSW `q=2` window whose middle
owner contains `z`.

For a rank-`(r+2)` set `T subseteq Omega`, let `m(T)` be the number of MSW
`q=2` occurrences with union `T`, and define

\[
 c_z(T)=\#\{\text{such occurrences whose middle owner contains }z\}.
\tag{4.3}
\]

### Theorem 4.1 (exact correlated-lift criterion)

The B-forest `B_z` is upper-exact if and only if

\[
 \boxed{c_z(T)=1\quad\text{for every }T\in{\Omega\choose r+2}
                         \text{ with }z\in T.}
\tag{4.4}
\]

For every fixed `T`,

\[
 \boxed{\sum_{z\in T}c_z(T)=r\,m(T).}
\tag{4.5}
\]

Consequently, for `r>=3`, no MSW `q=2` occurrence system can satisfy
(4.4) simultaneously for every puncture coordinate `z`.

#### Proof

Equation (4.2) gives a bijection between edges of `B_z` with upper colour
`T-z` and the occurrences counted by `c_z(T)`.  Both the edge set and the
target layer have order `U`, so upper surjectivity is equivalent to exact
multiplicity one, proving (4.4).

Every occurrence counted by `m(T)` has one middle owner of rank `r`, and
contributes to `c_z(T)` exactly for the `r` coordinates of that owner.
Double-counting gives (4.5).  If (4.4) held for all `z in T`, its left side
would be `r+2`, whereas the right side is divisible by `r`.  This is
impossible for `r>=3`.  \(\square\)

The final sentence is a puncture-uniform obstruction, not a no-go for a
single carefully chosen `z`.  It proves that the desired lift cannot be
obtained by a coordinate-blind assertion that every puncture is exact.

The marginal q2 theorem in
`MATH_THEOREM_Q2_SATURATING_CYCLE_CLIQUE_INSERTION_AND_CATALAN_PATH_FOREST_20260805.md`
correctly constructs a Catalan path forest with the desired intersection
palette, but it deliberately leaves its union labels uncontrolled.  In the
puncture language, that remaining row is exactly (4.4), together with the
requirement that the resulting paths use the MSW occurrence endpoints.

## 5. Exact direct-completion criterion for the A-forest

The puncture also sharpens the cap-two segmentation gate.  Orient every
A-component from its crossing boundary `S_i` toward its `z`-free
complementary endpoint `E_i`.  Suppose it has a first retained edge
`S_iS_i'`, and put

\[
 H_i=S_i\cup S_i'.
\tag{5.1}
\]

Any cap-two predecessor `P` satisfying

\[
 P\cup S_i=H_i
\tag{5.2}
\]

is a third facet

\[
 P=H_i-\{t\},\qquad
 t\in S_i\setminus\{\text{first deleted rail label}\}.
\tag{5.3}
\]

Its connector lower colour is

\[
 P\cap S_i=S_i-\{t\}.
\tag{5.4}

For depth `h`, seam cleanliness is exactly the condition that `t` is not
among the first `h` deleted rail labels.

Let `L(A_z)` be the set of edge intersections used by `A_z`, and fix a
set `I` of nontrivial A-components which are required to be cap-two.  Form
the edge-coloured bipartite **puncture completion graph** with:

* one left vertex for every terminal endpoint `E_j`;
* one right vertex for the entrance `S_i` of every A-component;
* an edge `E_j i` whenever `E_j` and `S_i` are Johnson adjacent and its
  colour `E_j intersection S_i` lies outside `L(A_z)`;
* for `i in I`, retain only those edges which additionally have the
  cap-two form (5.2)--(5.3) and satisfy the desired seam-clean condition.

Colour an edge by the rank-`(r-1)` set `E_j intersection S_i`.  A matching
is **rainbow** when these colours are distinct.

### Theorem 5.1 (no-deletion cap completion)

The forest `A_z` extends, without deleting an A-edge, to a lower-exact,
upper-surjective spanning two-factor in which every component in `I` has
the prescribed cap-two entrance if and only if:

1. the intersections of the A-edges are distinct;
2. the puncture completion graph has a rainbow perfect matching.

The component cycles of the resulting factor are the cycles of the induced
permutation of the A-components.  It is one Hamilton cycle exactly when
that permutation is one cycle.

#### Proof

The forest has `U=V-C` edges.  A spanning two-factor requires exactly `C`
additional edges and every path endpoint must receive one.  Lower
exactness first forces the old A-edge colours to be distinct and then
forces the new edges to use precisely the complementary `C` colours.  The
completion graph restricts every new colour to that complement; since the
matching is rainbow and has `C` edges, it uses the whole complement.
Cap-two on `I` is exactly (5.2)--(5.4).  The old forest already contains
every upper colour once, so arbitrary connector upper colours cannot
destroy upper surjectivity; on `I` they specifically repeat the first
retained colour.  Conversely, any direct completion has these properties
by degree, palette, and cap-two necessity.  The last assertion is the
usual path-component contraction.  \(\square\)

This theorem is an exact construction criterion, but puncturing alone does
not prove either of its first two rows.

## 6. The natural crossing seam already fails in the first nontrivial calibration

There is one tempting but incorrect shortcut: use, for every A-component,
the lower colour of its original A/B crossing edge.  The canonical
semilength-three paths are

\[
\begin{array}{lll}
123,136,146,456;&124,126,156,356;&125,145,345,346;\\
134,234,236,256;&135,235,245,246.&
\end{array}
\tag{6.1}
\]

Puncture `z=1`.  The A-edge intersection colours are

\[
 \{34,23,26,25,24\},
\tag{6.2}
\]

whereas the five natural crossing colours are

\[
 \{46,56,45,34,35\}.
\tag{6.3}
\]

The colour `34` is repeated across (6.2)--(6.3), and `36` is absent from
their union.  Thus even when the A-edge colours happen to be injective,
the literal crossing seams need not be the missing lower palette.  A
rethreading or a genuinely correlated cap matching is necessary.

This calibration is a symbolic application of the MSW flip recursion, not
a computational search.

## 7. Scope and self-audit

The exact positive conclusions are:

1. one puncture gives an upper-exact geodesic Catalan forest `A_z`;
2. the same puncture gives a spanning Catalan incidence path cover `H_z`;
3. suppressing `H_z` gives a lower-injective geodesic Catalan forest `B_z`;
4. its missing upper row is exactly the centered q2 condition (4.4);
5. direct cap-two completion of `A_z` is exactly Theorem 5.1.

The note proves none of the following:

1. A-edge intersection injectivity in general;
2. a puncture `z` satisfying (4.4);
3. the endpoint matching in Theorem 5.1;
4. arbitrary-width upper coverage beyond the displayed q2 row;
5. residence, the lower trace compiler, or a `B(k)+O(1)` construction.

Arithmetic audit:

\[
 {2r\choose r}=2{2r-1\choose r},\qquad
 C={2V\over r+1},\qquad
 V-C=V{r-1\over r+1}={2r-1\choose r+1}.
\tag{7.1}
\]

Local-path audit: if `z=lambda_a`, the B incidence path has `a` vertices
on each shore and the A path has `r-a+1` owner vertices; if `z=rho_b`, the
corresponding counts are `r-b+1` and `b`.  In both cases they sum to
`r+1`, their internal edge counts sum to `r-1`, and their crossing upper
vertex belongs only to the B incidence path.  These facts account for
every vertex and every edge used above exactly once.
