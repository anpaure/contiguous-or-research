# Odd root links: exact upper fibres, shortest excursions, and the fractional Hamilton gate

**Date:** 2026-08-02  
**Status:** unconditional structural theorems and an exact fractional
reduction.  These results do not construct an upper-surjective Hamilton
path, do not impose the fixed lollipop endpoints integrally, and do not
prove `nu(17)=24313`.

## 0. Outcome

Let

\[
 r\ge2,\qquad k=2r-1,\qquad
 \mathcal Q={{[k]}\choose {r-1}},\qquad
 \mathcal T={{[k]}\choose r},\qquad
 W=|\mathcal Q|=|\mathcal T|,
\]

and fix an arbitrary perfect containment matching

\[
 \mu:\mathcal Q\longrightarrow\mathcal T,
 \qquad L\subset\mu(L).
\]

The omitted case `r=1` (`k=1`) is the one-owner triviality and has no
root-link arc.

The root-link digraph from
`MATH_THEOREM_ODD_H1_ROOTED_EXCURSION_AND_GUARDED_REVERSAL_LIFT_20260802.md`
has a particularly rigid owner-coordinate form.

1. Every owner `T` has one matched deletion `rho(T) in T`, and every arc is
   exactly
   \[
          T\longrightarrow T-\{\rho(T)\}+\{x\},\qquad x\notin T.
   \]
2. Every rank-`(r+1)` upper colour has exactly `r+1` arcs.  Its arcs form a
   loopless functional digraph on its `r+1` facets and contain a directed
   cycle of length at least three.
3. For every rank-`(r+q)` upper target `U`, every starting facet `T subset U`
   and every ordering of `U-T` give a simple `q`-edge root-link excursion
   whose owner union is `U`.  Thus `U` has exactly
   \[
                  {r+q\choose r}q!={(r+q)!\over r!}
   \]
   canonical shortest excursions.  No upper target has a local root-link
   supply obstruction, for any choice of `mu`.
4. For every fixed `mu`, there is an **integral graphic forest** selecting
   exactly one arc of every rank-`(r+1)` colour.  It has exactly
   `Cat_r` components.  This statement does not control its tail or head
   degrees.
5. The full upper-surjective Hamilton-path system has a universal strict
   fractional point.  The same constant arc weight lies simultaneously in
   the spanning-tree polytope, both directed port-capacity polytopes, and
   every immediate-upper covering inequality.

Consequently the immediate-upper gate after fixing `mu` has no scalar,
ordinary Hall, graphic-cut, or fractional port obstruction.  Its exact
remaining difficulty is integral correlation between

\[
 \boxed{\text{graphic tree}\ \cap\ \text{tail capacity}\ \cap\
        \ \text{head capacity}\ \cap\ \text{upper cover},}
\]

together with the prescribed lollipop endpoints.  Higher ranks add a
global chronology synchronization problem, not a local excursion-existence
problem.

## 1. Owner-coordinate normal form

For `T in mathcal T`, define

\[
 L(T)=\mu^{-1}(T),\qquad
 \rho(T)=T\setminus L(T).
\tag{1.1}
\]

The second set is a singleton, which we identify with its element.

### Theorem 1.1 (root-link owner form)

Under the vertex identification `L -> mu(L)`, the root-link digraph is

\[
 \boxed{
 T\longrightarrow T^{x}:=T-\{\rho(T)\}+\{x\}
 \quad (x\in[k]\setminus T).}
\tag{1.2}
\]

The immediate-upper colour of this arc is

\[
                         c(T,x)=T\cup\{x\}.
\tag{1.3}
\]

In particular the digraph has indegree and outdegree `r-1`.

#### Proof

Put `L=L(T)=T-rho(T)`.  A root-link arc leaving `L` ends at a root `L'`
whose owner contains `L`.  Every rank-`r` owner different from `T` and
containing `L` has the unique form `L+x` with `x notin T`.  This is (1.2),
and its union with `T` is (1.3).  Conversely every such owner supplies the
required root-link arc.  There are `k-r=r-1` choices.

The indegree statement is also immediate from the original root form:
an owner has `r` coatoms, one used by `mu` and `r-1` others.  \(\square\)

The underlying undirected root-link graph is simple.  Parallel arcs with
one tail are excluded by (1.2).  Opposite arcs between two adjacent owners
would require their unique common coatom to be matched by `mu` to both
owners, which is impossible.

## 2. Exact immediate-upper fibres

Fix `R in binom([k],r+1)`.  Its `r+1` facets are the owners

\[
                         T_x=R-\{x\},\qquad x\in R.
\]

### Theorem 2.1 (functional colour fibre)

The arcs of upper colour `R` are exactly

\[
 T_x\longrightarrow R-\{\rho(T_x)\},\qquad x\in R.
\tag{2.1}
\]

Consequently:

1. every immediate-upper colour has exactly `r+1` arcs;
2. its colour fibre is a functional digraph of outdegree one on the
   `r+1` facets of `R`;
3. it has no loop or directed two-cycle; and
4. it contains a directed cycle of length at least three.

#### Proof

For the tail `T_x`, the only outgoing arc whose union colour is `R` is the
arc obtained by inserting `x`.  Formula (1.2) gives exactly (2.1).  This
proves items 1--2.  A loop is excluded because `x notin T_x` whereas
`rho(T_x) in T_x`.  Opposite arcs would match the common coatom of their
two owners to both owners, as observed after Theorem 1.1.  Every finite
functional digraph contains a directed cycle, proving items 3--4.
\(\square\)

### Corollary 2.2 (every potential has a complete forward support)

Let `phi` be any injective real-valued potential on the owner set.  The
forward support

\[
 E_\phi=\{T\to T':\phi(T)<\phi(T')\}
\tag{2.2}
\]

contains at least one arc of every immediate-upper colour.

#### Proof

On the directed cycle in any colour fibre, not every edge can decrease an
injective potential.  \(\square\)

This gives an acyclic directed support of every upper colour.  It does not
by itself give an undirected forest: a directed acyclic graph may have
undirected cycles.  Once both tail and head capacities are imposed,
however, any undirected cycle is coherently directed, so a common potential
then makes graphic acyclicity automatic.  This is precisely the remaining
three-resource selector, rather than an upper-colour existence issue.

## 3. Every higher target has factorially many shortest excursions

Let `U` have rank `r+q`, where `1<=q<=r-1`, and let `T_0 subset U` have
rank `r`.  Order the missing coordinates as

\[
                         U\setminus T_0=(x_1,\ldots,x_q).
\]

Recursively define

\[
             T_j=T_{j-1}-\{\rho(T_{j-1})\}+\{x_j\},
             \qquad 1\le j\le q.
\tag{3.1}
\]

### Theorem 3.1 (shortest-excursion abundance)

The sequence

\[
                         T_0\to T_1\to\cdots\to T_q
\tag{3.2}
\]

is a simple directed root-link path, every owner lies in `binom(U,r)`, and

\[
                         \bigcup_{j=0}^qT_j=U.
\tag{3.3}
\]

Different ordered pairs consisting of a starting facet and an ordering of
its missing coordinates give different directed paths.  Hence `U` has
exactly

\[
             {r+q\choose r}q!={(r+q)!\over r!}
\tag{3.4}

canonical shortest excursions.

#### Proof

Before step `j`, every coordinate ever seen belongs to

\[
                         T_0\cup\{x_1,\ldots,x_{j-1}\}.
\]

Thus the new coordinate `x_j` is not in `T_(j-1)`, so (3.1) is a legal
root-link arc.  Deletion and insertion both occur inside `U`, proving
`T_j subset U`.

The owner `T_j` contains `x_j`, while no earlier owner contains `x_j`.
Therefore the owners in (3.2) are distinct.  Every member of `T_0` occurs
at time zero, and every missing coordinate occurs at its insertion time,
proving (3.3).

Finally a directed path recovers its start and, at every step, the unique
inserted coordinate `T_j-T_(j-1)`.  The parametrization is therefore
injective.  Conversely, one Johnson arc introduces at most one coordinate
which was absent from the accumulated union.  A witness for a rank-`r+q`
target therefore needs at least `q` arcs.  At equality every arc introduces
one distinct member of `U-T_0`, so its insertion labels are an ordering of
that set and the path is exactly (3.1).  Counting starts and permutations
proves (3.4).  \(\square\)

A witness for `U` can be longer than `q` arcs, so Theorem 3.1 is a complete
description of the **shortest** witnesses and a sufficient bank for the
all-upper gate, not a claim that every witness is shortest.  In a global
Hamilton path, requiring one path from (3.2) for every `U` is stronger than
ordinary upper completeness.  The theorem proves that this stronger gate
has abundant local atoms for every `mu`; selecting them compatibly in one
owner-once chronology remains open.

## 4. Every fixed matching has an upper-exact graphic forest

Let `G_mu` be the underlying simple root-link graph, with one ground edge
for every directed arc.  Put

\[
 d=r-1,\qquad
 U_1={2r-1\choose r+1}=W{r-1\over r+1}.
\tag{4.1}
\]

Give every arc the weight

\[
                              x_e={1\over r+1}.
\tag{4.2}

### Lemma 4.1 (uniform graphic-colour point)

The vector `x` belongs simultaneously to

1. the graphic independent-set polytope of `G_mu`; and
2. the base polytope of the partition matroid whose parts are the
   immediate-upper colour fibres.

Its total mass is `U_1`.

#### Proof

Theorem 2.1 gives exactly `r+1` arcs of every colour, so every colour part
has load one.  The total mass is

\[
 {W(r-1)\over r+1}=U_1.
\]

For a vertex set `S` of order `s`, simplicity and outdegree `d` give

\[
 |E(S)|\le\min\left\{{s\choose2},\,ds\right\}.
\tag{4.3}

If `s<=2(r+1)`, the first bound gives

\[
 x(E(S))\le {s(s-1)\over2(r+1)}\le s-1.
\]

If `s>2(r+1)`, the second gives

\[
 x(E(S))\le{(r-1)s\over r+1}<s-1.
\]

These are exactly the graphic rank inequalities.  \(\square\)

### Theorem 4.2 (fixed-`mu` upper-exact forest)

For every perfect containment matching `mu`, there is an integral arc set
`Q_0` which

* contains exactly one arc of every rank-`(r+1)` upper colour; and
* is graphic-independent in `G_mu`.

It is a spanning forest with exactly

\[
                         W-U_1={2W\over r+1}=\operatorname{Cat}_r
\tag{4.4}

components, including isolated vertices.

#### Proof

Lemma 4.1 gives a common fractional independent set of size `U_1` in the
graphic matroid and the upper-colour partition matroid.  The common
independent-set polytope of two matroids is integral.  Hence it contains an
integral common independent set of the same size.  Since the colour
partition has rank `U_1`, every colour is used exactly once.  The component
count is vertices minus forest edges.  \(\square\)

This is stronger than separate colour Hall and graphic rank feasibility:
the two rows have a common integral solution for every fixed first
matching.  It is weaker than a rooted Catalan forest in the OR construction,
because several selected arcs may share a tail or a head.

### Corollary 4.3 (upper-surjective spanning tree, without port caps)

For every `mu`, the forest `Q_0` extends to a spanning tree of `G_mu`
which still covers every immediate-upper colour.

#### Proof

The middle-levels incidence graph is connected, and contracting every edge
of `mu` preserves connectedness.  Hence `G_mu` is connected.  Every forest
in a connected graph extends to a spanning tree; adding edges cannot remove
the upper colours already represented by `Q_0`.  \(\square\)

Thus immediate-upper coverage and undirected spanning topology are jointly
integral for every fixed matching.  The obstruction in a Hamilton path is
specifically **linearization** of this tree: every rooted vertex must have
at most one selected outgoing and at most one selected incoming arc.

## 5. The complete immediate-upper Hamilton system is fractionally feasible

The middle-levels incidence graph is connected, vertex-transitive,
`r`-regular and has girth six.  Wang's super-restricted-connectivity theorem
therefore says that, for `r>=3`, every edge cut which leaves no isolated
vertex has size at least `2r-2`; equality is the cut around one incidence
edge.  The case `r=2`, where the middle-levels graph is `C_6`, is checked
directly.

Contract the matching edges of `mu`.  A vertex subset `S` of the contracted
graph corresponds to the union of `|S|` matching edges in the original
graph.  Every component on either side of its cut contains a matching edge,
so no component is isolated.  Matching edges do not cross the cut.
Therefore

\[
                         |\delta_{G_\mu}(S)|\ge2r-2=2d
\tag{5.1}
\]

for every nonempty proper `S`.  A singleton has cut `2d`, so `G_mu` is
`2d`-edge-connected as well as `2d`-regular.

Give every arc the weight

\[
                         y_e={W-1\over W(r-1)}={W-1\over Wd}.
\tag{5.2}

### Theorem 5.1 (universal fractional upper Hamilton point)

For every `mu`, the vector `y` satisfies all of the following.

1. `y(E)=W-1` and `y` lies in the spanning-tree polytope of `G_mu`.
2. Every directed tail and every directed head has load `(W-1)/W<1`.
3. Every immediate-upper colour has load strictly greater than one.

#### Proof

For a proper vertex set `S` of order `s`, regularity and (5.1) give

\[
 |E(S)|=ds-{1\over2}|\delta(S)|\le d(s-1).
\]

Consequently

\[
 y(E(S))\le{W-1\over W}(s-1)<s-1,
\]

while `y(E)=W-1`.  These are the spanning-tree inequalities.

Every vertex has `d` outgoing and `d` incoming arcs, proving item 2.
By Theorem 2.1, an upper-colour fibre has `r+1` arcs, and hence load

\[
 { (r+1)(W-1)\over W(r-1)}>1,
\tag{5.3}
\]

because the difference between the two cross-multiplied sides is
`2W-(r+1)>0`.  \(\square\)

Thus even the full tree mass, both physical port capacities, and every
upper-cover lower bound have one common fractional solution.  This does
not imply an integral solution: it is an intersection of a graphic
base, two crossing partition capacities, and covering inequalities.

## 6. Exact integral gate and fixed-boundary scope

Let `z_e in {0,1}`.  Ignoring protected arcs for display, an
immediate-upper-surjective rooted Hamilton path is exactly a solution of

\[
\begin{aligned}
 z(E)&=W-1,\\
 z(E(S))&\le |S|-1 &&(\varnothing\ne S\subsetneq V),\\
 z(\delta^+(v))&\le1 &&(v\in V),\\
 z(\delta^-(v))&\le1 &&(v\in V),\\
 z(E_R)&\ge1 &&\left(R\in{{[k]}\choose{r+1}}\right).
\end{aligned}
\tag{6.1}

Indeed, the first two rows make a spanning tree.  The next two give
undirected degree at most two, so the tree is one directed Hamilton path.
The final row is exactly immediate-upper surjectivity.

For fixed initial root `s` and terminal root `t`, add

\[
 z(\delta^-(s))=0,\qquad z(\delta^+(t))=0,
\tag{6.2}

with equality one at the corresponding ports of every other vertex.  The
fixed-boundary lollipop also prescribes the matching `mu` and the literal
endpoint owners described in the rooted-excursion note.

Theorem 5.1 proves feasibility of the unpinned linear relaxation (6.1).
It does not prove the pinned relaxation (6.1)--(6.2), and neither theorem
in this note rounds (6.1) integrally.

The Catalan interpretation is now sharp:

* Theorem 4.2 always supplies the one-per-colour graphic forest `Q_0` with
  `Cat_r` components.
* Exactly `Cat_r-1` further edges are needed to reach tree size `W-1`.
* The only immediate-upper obstruction is selecting `Q_0` and those
  connectors while keeping every tail and head capacity one and retaining
  the fixed endpoints.

Thus the root-link formulation removes upper-colour existence and graphic
rank from the list of possible obstructions.  What remains is a genuinely
integral linearization problem.

## 7. Relation to arbitrary-width upper coverage

For a Hamilton owner path `H`, the complete upper condition is still the
component/excursion condition of the rooted-excursion theorem.  Theorem 3.1
shows that every target has factorially many shortest legal excursions in
the ambient root-link digraph.  It does **not** show that one Hamilton path
contains one excursion for every target.

Accordingly the clean next theorem is:

> **Root-link excursion packing theorem.**  Choose an integral solution of
> (6.1)--(6.2) which, for every `1<=q<=r-1` and every rank-`(r+q)` target
> `U`, contains either one canonical shortest excursion from Theorem 3.1 or
> another path component below `U` whose owner union is `U`.

The local atom bank in this statement is now unconditional for every
matching `mu`.  The unresolved content is simultaneous packing into one
owner-once path, followed by residence and the lower compiler.

## 8. Exact `K5` calibration: upper is automatic, endpoints are not

The independent exhaustive audit
`MATH_AUDIT_K5_ROOT_LINK_UPPER_CENSUS_AND_FIXED_BOUNDARY_NOGO_20260802.md`
enumerates all perfect matchings at `r=3`.

There are `60` matchings.  Every one has a directed root-link Hamilton
path, and every one of the `2,280` directed Hamilton paths covers all five
rank-four upper colours.  This last fact also has a short proof from binary
run counts, independent of the enumeration.

The fixed-boundary strengthening is false.  Only `600` of the `1,200`
relevant `(M,D,B,C)` endpoint requests admit a Hamilton path at all.  In the
Petersen permutation classification, the matching types have the following
boundary behaviour:

\[
\begin{array}{c|c|c}
\text{type}&\text{number of matchings}&
 \text{feasible relevant boundaries per matching}\\ \hline
2+2+2+2+2&6&0/20\\
2+8&30&4/20\\
5+5&24&20/20.
\end{array}
\tag{8.1}
\]

Thus the smallest case supports the positive upper theory but gives a
literal warning for (6.2): the matching and the protected lollipop boundary
must be selected jointly.  The `5+5` class shows that the joint target is
robustly feasible there; the failure is not an intrinsic endpoint count.

## References for the cut input

The restricted-cut input used in Section 5 is Y. Q. Wang, *Super restricted
edge-connectivity of vertex-transitive graphs*, Discrete Math. **289**
(2004), 199--205, DOI `10.1016/j.disc.2004.08.011`.  It proves that every
connected vertex-transitive graph of degree greater than two and girth
greater than four is super restricted edge-connected.  The middle-levels
graph is the bipartite Kneser graph `H(2r-1,r-1)`, so its degree and girth
are `r` and six.
