# The two-copy quotient of a middle-level Hamilton cycle

This note analyzes Hamilton cycles in the middle-level graph on ranks `m` and
`m+1` of a `(2m+1)`-set.  The main result is an exact two-copy path-forest
normal form.  It explains both why the middle-level theorem is highly relevant
to the Catalan linearization program and why ordinary Hamiltonicity, symmetry,
or a prescribed set of vertical edges does not by itself prove that lemma.

Throughout, let

\[
 Y=[2m],\qquad z\notin Y,
\]

and put

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=W-N=\operatorname{Cat}_m. \tag{0.1}
\]

Let \(M_m\) be the bipartite graph induced by ranks \(m,m+1\) of
\(2^{Y\cup\{z\}}\).

## 1. The exact two-copy decomposition

The four vertex classes are

\[
\begin{array}{c|c|c}
 &z\notin X&z\in X\\ \hline
|X|=m&A\in\binom Ym&\{z\}\cup S,\quad S\in\binom Y{m-1}\\
|X|=m+1&U\in\binom Y{m+1}&\{z\}\cup A,\quad A\in\binom Ym.
\end{array} \tag{1.1}
\]

There are three edge types:

1. \(A-U\) when \(A\subset U\); this is the upper copy
   \(Q_{2m}(m,m+1)\).
2. \(\{z\}\cup S-\{z\}\cup A\) when \(S\subset A\); this is the lower copy
   \(Q_{2m}(m-1,m)\).
3. The vertical perfect matching

   \[
   A\longleftrightarrow \{z\}\cup A,qquad A\in\binom Ym. \tag{1.2}
   \]

There are no edges from a `z`-containing rank-`m` vertex to a no-`z`
rank-`m+1` vertex.

## 2. Contracting a Hamilton cycle

Let \(H\) be any Hamilton cycle of \(M_m\).  Let \(V_z\) be the set of middle
labels \(A\in\binom Ym\) whose vertical edge (1.2) belongs to \(H\).

Delete the vertical edges of `H`.  What remains in each copy spans that copy.
Every outer vertex \(U\) or \(\{z\}\cup S\) still has degree two, while a middle
vertex has degree one precisely when its vertical edge was deleted and degree
two otherwise.

Suppress every degree-two outer vertex:

* a path \(A-U-B\) becomes the Johnson edge \(AB\) with union colour
  \(U=A\cup B\);
* a path \(\{z\}\cup A-\{z\}\cup S-\{z\}\cup B\) becomes the Johnson edge
  \(AB\) with intersection colour \(S=A\cap B\).

Call the resulting graphs on \(\binom Ym\) respectively \(F_+(H)\) and
\(F_-(H)\).

### Theorem 1 (two-copy Catalan quotient)

For every Hamilton cycle `H` of `M_m`:

1. exactly `2K` vertical edges occur:

   \[
   |V_z|=2K; \tag{2.1}
   \]

2. `F_+(H)` is a spanning linear forest with no isolated vertices, exactly
   `N` edges, and `K` path components;
3. `F_-(H)` is another such forest with exactly `N` edges and `K` path
   components;
4. the endpoint set of both forests is exactly `V_z`;
5. every rank-`m+1` union colour occurs exactly once in `F_+(H)`;
6. every rank-`m-1` intersection colour occurs exactly once in `F_-(H)`.

#### Proof

In the upper copy every one of the `N` outer vertices has degree two, so the
number of internal Hamilton-cycle edges is `2N`.  The sum of the internal
degrees at its `W` middle vertices is also `2N`.  A middle vertex not in
`V_z` has internal degree two; a vertex in `V_z` has internal degree one.
Therefore

\[
 2W-|V_z|=2N,
\]

which gives (2.1).

After deleting the vertical matching, no copy can contain a cycle component:
such a component would have no vertical edge and would already be a separate
cycle of `H`.  Each copy is therefore a spanning union of paths.  It has
`2K` degree-one vertices, hence exactly `K` paths.  Suppressing each outer
vertex gives `N` Johnson edges and changes neither components nor middle
degrees.  This proves statements 2--4.

Every no-\(z\) upper vertex \(U\) is suppressed once and produces an edge whose
union is \(U\), proving statement 5.  Every \(z\)-containing lower outer vertex
\(\{z\}\cup S\) is suppressed once and produces an edge whose intersection is
\(S\), proving statement 6.  \(\square\)

The count (2.1) is not special to `z`: applying the same decomposition at any
coordinate shows that every Hamilton cycle in `M_m` flips every coordinate
exactly `2K` times.

This exact structural observation appears explicitly in Mütze's proof of the
middle-level theorem; the contribution here is to retain both Johnson colour
projections in the quotient.

## 3. Endpoint pairing is the whole connectivity quotient

Every path component of `F_+(H)` pairs its two endpoints in `V_z`.  Let

\[
 \pi_+:V_z\longrightarrow V_z
\]

be the resulting fixed-point-free involution.  Define \(\pi_-\) analogously
from \(F_-(H)\).

### Theorem 2 (endpoint-pairing criterion)

Conversely, suppose \(F_+,F_-\) are spanning linear forests of Johnson edges
on \(\binom Ym\), with every vertex of degree one or two, such that:

* `F_+` has `N` edges, uses every upper union colour once, and has endpoint
  set `V`;
* `F_-` has `N` edges, uses every lower intersection colour once, and has the
  same endpoint set `V`.

Lift their edges through their corresponding outer vertices in the two copies
of (1.1), and add the vertical edges labelled by `V`.  The resulting spanning
2-factor is a Hamilton cycle if and only if

\[
 \pi_+\cup\pi_- \tag{3.1}
\]

is one alternating cycle on `V`.

#### Proof

Every nonendpoint has degree two inside its own forest.  Every endpoint has
one forest edge and one vertical edge, so the lift is a spanning 2-factor.
Contract each lifted path and identify the two copies of every endpoint via
the vertical edge.  The resulting quotient has at each endpoint one
\(\pi_+\)-edge and one \(\pi_-\)-edge.  It is therefore the union of the two perfect
matchings.  Components of this quotient are in bijection with cycles of the
lifted 2-factor.  Hence the lift is Hamiltonian exactly when (3.1) is one
cycle.  \(\square\)

This proves an exact answer to the prescribed-vertical-edge question:

> A set `V` of vertical edges is feasible precisely when `|V|=2K` and there
> are upper- and lower-colour-perfect path factors with common endpoint set
> `V` whose endpoint involutions form one alternating cycle.

The set `V` alone is far from sufficient; it contains no endpoint-pairing or
internal colour information.

## 4. Relation to Catalan linearization

Call a graph `F` on the middle `m`-sets a **two-sided Catalan forest** if:

* it is a spanning linear forest with no isolated vertices and with `N`
  edges, hence `K` nontrivial paths;
* its edge intersections are all rank-`m-1` sets exactly once; and
* its edge unions are all rank-`m+1` sets exactly once.

This is the nondegenerate colour-perfect core of the Catalan linearization
lemma in `GLOBAL_RECURSION.md`.  That lemma additionally asks that the `K`
path components be joinable at their endpoints by `K-1` Johnson edges into
one Hamilton path.  If that formulation permits singleton path components,
the quotient route here imposes the extra no-isolate condition: one vertical
edge cannot make the two copies of an isolated middle vertex have degree two.

### Theorem 3 (diagonal cycle-factor equivalence)

Two-sided Catalan forests `F` are in bijection with spanning 2-factors of
`M_m` having the following diagonal quotient:

\[
 F_+=F_-=F, \tag{4.1}
\]

with vertical edges at all path endpoints.  The lifted 2-factor has exactly
`K` cycles, one for each path component of `F`.

#### Proof

For every edge \(AB\) of \(F\), lift one copy through its unique upper vertex
\(A\cup B\) and one copy through its unique lower vertex
\(\{z\}\cup(A\cap B)\).  Two-sided colour perfection says that every
outer vertex in both copies is used exactly once.  Add vertical edges at the
`2K` path endpoints.  One path of `F`, traversed in the upper copy and back in
the lower copy, becomes one cycle.  Distinct paths give disjoint cycles.

Conversely, suppressing the two outer classes of any diagonal factor gives
the common forest `F`; coverage of all outer vertices gives both exact colour
conditions.  \(\square\)

### Corollary 4 (diagonal-symmetry obstruction)

For \(m\ge2\), so \(K>1\), a quotient condition forcing \(F_+=F_-\) can never itself
produce a Hamilton cycle.  It produces \(K\) separate cycles.  At least \(K-1\)
component-changing switches are necessary.

Therefore the Catalan linearization lemma is **not** equivalent to ordinary
middle-level Hamiltonicity, nor to a symmetry that simply identifies the two
contracted forests.

There are useful one-way implications:

* If a Hamilton cycle has `F_+` two-sided colour-perfect, then `F_+` is a
  two-sided Catalan forest.
* A two-sided Catalan forest gives the diagonal `K`-cycle factor of Theorem 3,
  but not automatically a Hamilton cycle.
* A Hamilton cycle does not automatically make either one of its two forests
  two-sided: Theorem 1 puts all upper colours in `F_+` and all lower colours
  in `F_-`, in different copies.

Moreover, the endpoint-connectability clause in the stated Catalan
linearization lemma is not implied by a Hamilton cycle whose one forest is
two-sided.  The other forest connects its endpoints by whole paths, not by
single Johnson bridge edges.

## 5. Complement symmetry is duality, not diagonal equality

Let `c` be complementation in the full `(2m+1)`-set.  It is an automorphism of
`M_m` that swaps its two ranks and its two copies.  On middle labels it sends

\[
 A\longmapsto A^c=Y\setminus A. \tag{5.1}
\]

### Proposition 5 (quotient of a complement-invariant cycle)

If a Hamilton cycle `H` is invariant under `c`, then

\[
 V_z=c(V_z),\qquad F_-(H)=c(F_+(H)), \tag{5.2}
\]

and the endpoint involutions satisfy

\[
 \pi_-=c\,\pi_+\,c. \tag{5.3}
\]

#### Proof

Complementation maps the vertical edge labelled `A` to the one labelled
`A^c`, proving the first identity.  It maps an upper path

\[
 A\subset U\supset B
\]

to the lower path

\[
 A^c\supset U^c\subset B^c,
\]

which proves the forest identity and hence the endpoint identity.  \(\square\)

This symmetry does not say that the intersection colours of `F_+` are
distinct.  It merely turns the already-distinct upper colours `U` of `F_+`
into the already-distinct lower colours `U^c` of the *other* forest.  Thus a
complement-symmetric Hamilton theorem would still stop short of Catalan
linearization.

## 6. Coordinate balance

For a Johnson graph edge `AB`, write

\[
 \partial_x(AB)=1_{\{x\in A\triangle B\}}.
\]

For a forest \(F\), put

\[
 \partial_x(F)=\sum_{e\in E(F)}\partial_x(e).
\]

### Proposition 6 (Hamilton quotient balance)

For every Hamilton cycle \(H\) and every old coordinate \(x\in Y\),

\[
 \partial_x(F_+(H))+\partial_x(F_-(H))=2K. \tag{6.1}
\]

#### Proof

Every contracted Johnson edge represents two consecutive cube edges, which
flip exactly the two coordinates in the symmetric difference of its middle
endpoints.  Thus the left side counts precisely the edges of `H` that flip
coordinate \(x\).  Applying Theorem 1 with \(x\) in place of \(z\) shows that this
number is \(2K\).  \(\square\)

There is no extra balance obstruction for a two-sided colour-perfect forest.

### Proposition 7 (automatic balance of a colour-perfect matching)

Every two-sided Catalan forest `F` satisfies

\[
 \partial_x(F)=K\qquad(x\in Y). \tag{6.2}
\]

In fact, (6.2) holds for any perfect matching between the rank-`m-1` and
rank-`m+1` colour layers, whether or not its induced Johnson graph is a
forest.

#### Proof

Write a matched incidence as \(S\subset U\).  Its Johnson edge exchanges the
two elements of \(U\setminus S\), so it contributes at coordinate \(x\) exactly
when \(x\in U\setminus S\).  Since every upper and lower colour is used once,

\[
\begin{aligned}
 \partial_x(F)
 &=|\{U:x\in U\}|-|\{S:x\in S\}|\\
 &=\binom{2m-1}{m}-\binom{2m-1}{m-2}\\
 &=\frac1{m+1}\binom{2m}{m}=K.
\end{aligned} \tag{6.3}
\]

\(\square\)

Thus the Catalan number is simultaneously:

* the number of paths in each contracted forest;
* half the number of vertical edges; and
* the exact number of exchanges of each coordinate in every two-sided
  colour-perfect matching.

### Exact matching reformulation

The bipartite incidence graph between \(\binom Y{m-1}\) and
\(\binom Y{m+1}\), with \(S\) adjacent to \(U\) when \(S\subset U\), is
\(\binom{m+1}{2}\)-regular on both sides.  It therefore has a perfect
matching.  Each matched pair \(S\subset U\) determines the unique Johnson
edge joining the two intermediate \(m\)-sets in the interval \([S,U]\).
Consequently:

> Two-sided colour perfection alone is easy: it is exactly a perfect matching
> in this regular incidence graph.  The hard condition is that the \(N\)
> induced Johnson edges form an acyclic graph in which every middle vertex has
> degree one or two.

Under that degree-and-acyclicity condition the induced graph automatically has
\(W-N=K\) path components, so it is precisely a two-sided Catalan forest.

## 7. Colour-preserving switches

Theorem 3 converts Catalan linearization into a cycle-gluing problem.  The
correct switches live in the colour-incidence graph

\[
 \mathcal I_m=
 \left(\binom Y{m-1},\binom Y{m+1};\subset\right). \tag{7.1}
\]

A perfect matching edge `S--U` induces the Johnson edge between the two
middle sets in the interval `[S,U]`.

Suppose

\[
 S\subset U,\quad T\subset U,\quad
 S\subset V,\quad T\subset V \tag{7.2}
\]

form an alternating four-cycle of \(\mathcal I_m\).  Replacing matching pairs

\[
 (S,U),(T,V)
 \quad\hbox{by}\quad
 (S,V),(T,U) \tag{7.3}
\]

preserves perfect coverage of both colour layers while changing the two
induced Johnson edges.

### Lemma 8 (restricted flippable-pair principle)

Start from the diagonal factor of a two-sided Catalan forest.  If a sequence
of switches (7.3), performed in one copy, has the following properties:

1. after every switch the contracted graph in that copy remains a spanning
   linear forest with the original endpoint set (so the vertical matching
   still completes it to a 2-factor);
2. each switch merges two cycles of the current lifted 2-factor; and
3. after \(K-1\) switches all original path components are connected,

then the resulting lift is a Hamilton cycle of \(M_m\), and the switched copy
remains two-sided colour-perfect.

#### Proof

The matching switch preserves every lower and upper colour exactly once.
Condition 1 preserves the path-factor degree requirements.  A standard
2-factor switch that reconnects two edges in opposite pairing merges the two
cycles specified in condition 2.  Starting with \(K\) cycles, \(K-1\) such merges
leave one Hamilton cycle.  \(\square\)

This is the precise analogue of the flippable-pair method used in known proofs
of the middle-level theorem.  The additional restriction is severe: the
switches must be alternating switches of \(\mathcal I_m\), so they preserve both
Johnson colour projections, and they must retain linearity.

## 8. What known middle-level constructions do and do not give

Mütze's construction starts with exactly the quotient structure of Theorems
1 and 2: a family `P` of `K` paths spanning `Q_(2m)(m,m+1)`, an isomorphic
family `f(P)` spanning `Q_(2m)(m-1,m)`, a common endpoint set, and vertical
matching edges.  It then uses flippable pairs of paths and a connected
auxiliary graph to merge the cycles of the resulting 2-factor.

This proves unrestricted Hamiltonicity and supplies the right *shape* of a
potential proof.  It does not, as presently stated, prove either of the
following extra assertions:

* that the intersection colours of the contracted upper forest `P` are all
  distinct; or
* that its flippable pairs preserve the complete intersection-colour layer.

The ordinary switches preserve vertices of the two-level graph, and hence
preserve upper outer-vertex coverage.  Catalan linearization asks for the
additional matching invariant (7.3).  Therefore the known Hamilton theorem
cannot be cited as a proof of the Catalan linearization lemma without a new
colour-preservation analysis.

Relevant primary sources are:

* Torsten Mütze, [Proof of the middle levels
  conjecture](https://arxiv.org/abs/1404.4442), especially its two-copy path
  decomposition and flippable-pair reduction;
* Petr Gregor, Torsten Mütze, and Jerri Nummenpalo,
  [A short proof of the middle levels
  theorem](https://arxiv.org/abs/1710.08249).

## 9. Exact remaining theorem

The middle-level quotient suggests a sharper target than an unspecified
symmetry.

> Construct a two-sided Catalan forest and prove that its diagonal `K`-cycle
> factor has a connected auxiliary graph of **colour-preserving** switches of
> the form (7.3), while all switched path factors remain linear.

This would simultaneously prove the colour-perfect forest statement and
Hamiltonize its two-copy lift.  The endpoint-connectability by `K-1` direct
Johnson bridges requested in `GLOBAL_RECURSION.md` is a different, stronger
local gluing condition; it is not a formal consequence of middle-level
Hamiltonicity.

The most important proved takeaway is the exact quotient:

\[
\boxed{
\text{middle-level Hamilton cycle}
\Longleftrightarrow
\text{two Catalan path forests with common endpoints and one alternating
endpoint cycle}.}
\]

What remains missing is not path linearity--Hamiltonicity supplies that in
both copies--but simultaneous two-sided colour perfection in one copy.
