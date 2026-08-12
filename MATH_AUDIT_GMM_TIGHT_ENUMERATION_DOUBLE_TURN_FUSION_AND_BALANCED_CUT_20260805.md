# GMM tight enumerations do not yet give double-turn Middle Levels cycles

**Date:** 2026-08-05  
**Method:** pure mathematics and primary-source audit; no computation, search,
or solver

## 0. Verdict

Let `r >= 2`, let `Omega` be a `(2r-1)`-set, and put

\[
 \mathcal L={\Omega\choose r-1},\qquad
 \mathcal M={\Omega\choose r},\qquad
 \mathcal U={\Omega\choose r+1},
\]

\[
 W=|\mathcal L|=|\mathcal M|={2r-1\choose r},\qquad
 U=|\mathcal U|={2r-1\choose r+1},
\]

\[
 C=W-U={2W\over r+1}={1\over r+1}{2r\choose r}
   =\operatorname {Cat}_r.                                      \tag{0.1}
\]

The primary Gregor--Mička--Mütze result and the older tight-enumeration
theorem imply two **separate** facts.

1. The Middle Levels Theorem gives a Hamilton cycle of the containment
   graph on `\mathcal L\mathbin{\dot\cup}\mathcal M`.  Suppressing
   `\mathcal L` gives a Hamilton cycle on `\mathcal M` whose rank-`(r-1)` intersection
   colours are bijective.
2. A tight enumeration of levels `r,r+1` gives a generally different
   Hamilton cycle on `\mathcal M` whose rank-`(r+1)` union colours are
   surjective.  Deleting its `C` direct distance-two steps gives an
   unconditional spanning `C`-component upper-exact forest.

Neither cited theorem says that these two Hamilton cycles have the same
order on `\mathcal M`.  A tight enumeration of levels `r,r+1` is not a
Hamilton cycle of `ML(2r-1)`: it uses rank-`(r+1)` vertices and `C`
distance-two steps between rank-`r` vertices.  It lifts to an
`ML(2r-1)` Hamilton cycle exactly when all its rank-`(r-1)` edge
intersections are distinct, and the primary theorem contains no such row.

Consequently the proposed all-`r` statement

\[
 \boxed{\text{an `ML(2r-1)` Hamilton cycle with surjective upper turns}}
                                                               \tag{0.2}
\]

is **not** an unconditional consequence of GMM.  It is precisely the
still-open double-turn fusion theorem.

Conditional on (0.2), however, the claimed Catalan forest and its exact
cut-to-balanced-path-cover interpretation are correct, subject to one
wording correction: one must delete `mu(R)-1` occurrences of each upper
colour `R`, not necessarily one occurrence for each repeated colour.
Surjectivity alone does not imply multiplicity at most two.

The complement-dual lower-turn statement is exactly equivalent to (0.2).

## 1. What the primary theorems actually state

The local primary source

* `tmp/central/gmlc2.tex`, Corollary `cor:sat-tight`,

states that every interval of consecutive Boolean levels has **both** a
saturating cycle and a tight enumeration.  The proof treats these as two
existence statements.  For tight enumerations outside the central balanced
case it invokes the results of Gregor--Mütze, *Trimming and Gluing Gray
Codes*.

In that paper, Theorem 15 states that for every `n >= 3` and
`0 <= k <= n-1` there is a tight enumeration of levels `k,k+1`.  The
definition of tightness says that all steps have Hamming length one or two,
and the length-two steps lie in the larger bipartition class.  Their
construction moreover keeps every length-two step inside one Boolean level.

For `n=2r-1` there are two relevant substitutions.

* `k=r-1`: the two levels have equal size, so tightness is ordinary
  Middle Levels Hamiltonicity.
* `k=r`: rank `r` has size `W`, rank `r+1` has size `U`, and the tight
  enumeration has exactly `W-U=C` direct rank-`r` distance-two steps.

The quantifiers do not identify the cyclic rank-`r` order in these two
applications.  In fact the proof constructs the different values of `k`
inductively as separate cycles.  The word “both” in the GMM corollary does
not assert a common witness.

## 2. Exact projection of the upper tight enumeration

Let `E` be a tight enumeration of levels `r,r+1` of `Q_(2r-1)`.
Suppress every rank-`(r+1)` vertex.  Since the smaller partition has no
distance-two steps, every such vertex `R` is flanked by two distinct
rank-`r` facets `X,Y` and

\[
 X\cup Y=R.                                                     \tag{2.1}
\]

Every other consecutive pair of retained rank-`r` vertices was a direct
length-two step, hence differs by one Johnson exchange.  Thus suppression
gives a Hamilton cycle

\[
 C_+\subset J(2r-1,r).                                         \tag{2.2}
\]

Each `R\in\mathcal U` appears exactly once in `E` and certifies one edge
of `C_+` with union colour `R`.  Therefore the upper-turn map

\[
 u: E(C_+)\longrightarrow\mathcal U,\qquad u(XY)=X\cup Y       \tag{2.3}
\]

is surjective.  Its `U` subdivided edges contain one certified occurrence
of every colour; its remaining `C` direct edges are surplus occurrences.

### Theorem 2.1 (unconditional upper-only Catalan forest)

Delete from `C_+` all `C` direct distance-two steps of the tight
enumeration.  The result is a spanning linear forest `F_+` on `\mathcal M`
with exactly `C=Cat_r` components, and

\[
 XY\longmapsto X\cup Y
\]

is a bijection from `E(F_+)` to `\mathcal U`.

#### Proof

The retained edges are exactly the `U` edges certified by the
rank-`(r+1)` vertices of `E`, so their union colours are bijective.  At
least one edge was deleted and the starting graph was a cycle, hence the
spanning remainder is a forest.  It has `W` vertices and `U=W-C` edges,
so it has `C` components. \(\square\)

This theorem has no lower-colour conclusion.  The intersections of the
retained edges may repeat.

## 3. Why the upper tight enumeration is not automatically Middle Levels

Every Johnson edge `XY` in (2.2) has the unique lower colour

\[
 \ell(XY)=X\cap Y\in\mathcal L.                                \tag{3.1}
\]

Inserting `ell(XY)` on every edge of `C_+` produces a closed alternating
walk in the Middle Levels graph.  It is a Hamilton cycle if and only if

\[
 \ell:E(C_+)\longrightarrow\mathcal L
 \quad\hbox{is bijective}.                                    \tag{3.2}
\]

Necessity is immediate because an `ML(2r-1)` Hamilton cycle visits every
lower vertex once.  Conversely, (3.2) makes the inserted alternating walk
visit every vertex of both equal shores exactly once.

Tightness does not impose (3.2).  Here is a hand-checkable example at
`r=3`.  On `[5]`, take the cyclic Johnson order

\[
 345,145,245,235,135,134,124,125,123,234.                       \tag{3.3}
\]

Its upper colours omit, in cyclic order, the coordinates

\[
 2,3,1,4,2,5,3,4,5,1,                                         \tag{3.4}
\]

so every rank-four colour occurs exactly twice.  Insert the corresponding
rank-four vertex at the first turns labelled `2,3,1,4,5`, and leave the
other five turns direct.  This is a tight enumeration of levels `3,4`:
it uses every rank-three and rank-four vertex once, all inserted steps have
length one, and the five direct steps have length two.

But the first two lower colours of (3.3) are both

\[
 345\cap145=45=145\cap245.                                     \tag{3.5}
\]

Thus even a perfectly upper-surjective tight enumeration need not be
lower-exact.  This example does not disprove existence of a different
double-turn cycle; it proves that the missing row is not a formal
consequence of tightness.

## 4. The exact double-turn fusion statement

Let `H` be a Hamilton cycle of `ML(2r-1)`.  Suppressing its lower shore
gives a Hamilton cycle `C_H` on `\mathcal M`.  Every edge of `C_H` arose
through a different lower vertex, so

\[
 \ell:E(C_H)\longrightarrow\mathcal L
\]

is automatically a bijection.

Therefore (0.2) is equivalent to the following single Johnson-cycle
statement:

> There is a Hamilton cycle `C` of `J(2r-1,r)` for which the intersection
> map is bijective and the union map is surjective.

GMM supplies a cycle satisfying the first condition and, separately, a
cycle satisfying the second.  Finding one cycle satisfying both is the
integral colour/monodromy fusion gate; no cited GMM theorem closes it.

### Proposition 4.1 (exact common-witness formulation)

The following data are equivalent.

1. An upper-turn-surjective Hamilton cycle `H` of `ML(2r-1)`, together
   with one chosen occurrence of every upper colour.
2. A tight enumeration `E` of levels `r,r+1` whose suppressed rank-`r`
   Hamilton cycle has pairwise distinct rank-`(r-1)` intersections.

#### Proof

From item 1, suppress the lower shore to obtain `C_H`.  Subdivide the one
chosen edge of each upper colour by that rank-`(r+1)` set and leave the
other `C` edges direct.  This lists all `W` rank-`r` and all `U`
rank-`(r+1)` vertices once, with `C=W-U` direct length-two steps, hence is
tight.  Its intersections are the distinct lower vertices of `H`.

Conversely, suppress the upper vertices of `E`.  By item 2 its `W`
intersections enumerate the `W` lower sets; inserting all of them gives an
`ML(2r-1)` Hamilton cycle.  The `U` edges originally subdivided in `E`
certify every upper colour, so its upper-turn map is surjective. \(\square\)

Thus “make the two literature witnesses the same” is not informal: it is
exactly the request that the upper tight enumeration lie on the
lower-injective face (3.2).

## 5. Conditional Catalan deletion theorem

Assume now that `H` satisfies (0.2), and let

\[
 \mu(R)=|\{e\in E(C_H):u(e)=R\}|\qquad(R\in\mathcal U).         \tag{5.1}
\]

Choose one retained edge from every nonempty colour class and delete all
other edges.  The number deleted is

\[
 \sum_{R\in\mathcal U}(\mu(R)-1)
 =W-U=C.                                                       \tag{5.2}
\]

### Theorem 5.1 (conditional two-colour Catalan forest)

The retained graph `F` is a spanning `C`-component linear forest on
`\mathcal M`.  Its union map is a bijection onto `\mathcal U`, and its
intersection colours are injective.

#### Proof

Exactly one edge per upper colour remains, proving upper exactness and
giving `U` retained edges.  All intersections were distinct on the full
cycle `C_H`, so they remain distinct.  Deleting the nonempty set of `C`
edges from a cycle gives a spanning forest, and

\[
 c(F)=|V(F)|-|E(F)|=W-U=C.
\]

\(\square\)

The phrase “delete one redundant occurrence per upper colour” is correct
only under the additional cap-two condition `mu(R) <= 2`.  The generally
correct instruction is to delete `mu(R)-1` occurrences from colour `R`.

## 6. Exact cut-to-balanced-path-cover interpretation

Lift every retained edge `XY` of `F` through its lower colour `X\cap Y`.
Because those lower colours are injective, this gives a vertex-disjoint
alternating path cover `\mathcal P` in `ML(2r-1)` with the following exact
properties.

1. It contains all `W` rank-`r` vertices and exactly `U=W-C`
   rank-`(r-1)` vertices.
2. It has exactly `C` components, each beginning and ending on the
   rank-`r` shore.  Hence every component contains one more rank-`r`
   vertex than rank-`(r-1)` vertex; isolated rank-`r` components are
   allowed.
3. At its `U` internal lower vertices, the unions of the two neighbouring
   rank-`r` vertices enumerate `\mathcal U` exactly once.
4. The omitted lower vertices are precisely the `C` intersection colours
   of the deleted edges.

Equivalently, `\mathcal P` is obtained from `H` by cutting out those `C`
lower vertices.  Adding back each omitted lower vertex with its two old
incident edges reconnects the components into the original Hamilton cycle.

This admits an exact converse.  Let `\mathcal P` be any alternating path
cover satisfying items 1--3, and let
`O=\mathcal L\setminus V(\mathcal P)`.
Then `|O|=C`.  It completes to a double-turn Hamilton cycle if and only if
one can assign to every `A\in O` two endpoint **roles** at distinct owner
vertices `X,Y` containing `A`, using every endpoint role exactly once, such
that the resulting
2-regular quotient on the `C` path components is connected.  Equivalently,
that quotient is one cycle (with the evident one-component convention).

Endpoint roles, rather than just endpoint vertices, are required here:
an isolated rank-`r` component has two unused incidence roles at its one
vertex, and the two roles may be used by two different bridges.

Indeed, the assigned two-edge bridges make every vertex degree two.  The
quotient criterion is exactly connectedness.  Every upper colour already
appears once inside `\mathcal P`, so every bridge adds only a repeat; hence
the completed Hamilton cycle remains upper-turn surjective.  Conversely,
cutting a double-turn Hamilton cycle produces exactly this bridge system.

Thus a double-turn cycle with a chosen upper-colour transversal is
equivalent to

\[
 \boxed{
 \begin{gathered}
 \text{an upper-exact, lower-injective balanced Catalan path cover}\\
 {}+\text{ a cyclic completion through all omitted lower vertices.}
 \end{gathered}}                                               \tag{6.1}
\]

## 7. Complement-dual lower-turn theorem

Suppressing the rank-`r` shore of an `ML(2r-1)` Hamilton cycle gives a
Hamilton cycle on `\mathcal L`.  Its edge unions are automatically a
bijection onto `\mathcal M`.  Define its lower-turn colour by

\[
 d(AB)=A\cap B\in{\Omega\choose r-2}.                           \tag{7.1}
\]

The complement map on `Omega` sends

\[
 \mathcal M\leftrightarrow\mathcal L,qquad
 {\Omega\choose r+1}\leftrightarrow{\Omega\choose r-2},
\]

and converts unions into complements of intersections.  Consequently

\[
 \boxed{
 \begin{aligned}
 &\text{upper-turn-surjective `ML(2r-1)` Hamilton cycles exist}\\
 &\quad\Longleftrightarrow
 \text{lower-turn-surjective `ML(2r-1)` Hamilton cycles exist}.
 \end{aligned}}                                                \tag{7.2}
\]

Conditional on the lower-turn version, retaining one edge per rank-`(r-2)`
colour gives a spanning `C`-component forest on `\mathcal L` whose lower
turns are exact and whose rank-`r` union colours are injective.  Its lift is
the dual balanced path cover: all lower-shore vertices, `U` upper-shore
vertices, `C` components with endpoints on the lower shore, and cyclic
completion through the `C` omitted upper vertices.

The tight enumeration of levels `r-2,r-1` supplies a separate
lower-turn-surjective Johnson cycle, dual to Section 2.  Again, it is not
automatically the lower projection of an `ML(2r-1)` Hamilton cycle.

## 8. Proof-safe conclusion

The unconditional consequences of the cited literature are exactly:

\[
 \begin{array}{c|c}
 \text{source}&\text{same-cycle conclusion on rank `r`}\\ \hline
 \text{Middle Levels Hamilton cycle}&
   \text{intersection-exact Hamilton cycle}\\
 \text{tight enumeration of levels `r,r+1`}&
   \text{union-surjective Hamilton cycle}\\
 \text{delete its direct steps}&
   \text{upper-exact `Cat_r`-component forest}
 \end{array}
\]

What is **not** supplied is intersection exactness and union surjectivity
on one Hamilton cycle.  Therefore GMM does not close the proposed
double-turn theorem, the two-colour Catalan forest, or the balanced
Middle-Levels path cover.  Sections 5--7 give the exact conditional
implications and the duality, so this route has been reduced without
overclaiming it.

## Primary references

* P. Gregor, O. Mička, T. Mütze, *On the central levels problem*,
  Corollary 2 and its proof; local primary source `tmp/central/gmlc2.tex`;
  arXiv:1912.01566.
* P. Gregor, T. Mütze, *Trimming and Gluing Gray Codes*, Theorem 15 in
  the arXiv version (adjacent-level tight enumerations); local extracted
  primary text `tmp/pdfs/trimming_gluing_gray_codes_1607.08806.txt`;
  arXiv:1607.08806.
