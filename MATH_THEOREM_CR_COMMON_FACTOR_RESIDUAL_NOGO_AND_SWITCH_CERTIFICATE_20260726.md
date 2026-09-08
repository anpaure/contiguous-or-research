# Critical Kneser rounding as a common factor: the random-residual no-go and the exact switch certificate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 \Omega=[2m],\quad
 \mathcal L=\binom{\Omega}{m-1},\quad
 \mathcal M=\binom{\Omega}{m},
\]

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1},\qquad
 D=W-N={W\over m+1}.                                         \tag{0.1}
\]

The critical rounding assertion \((\mathrm {CR})\) from the preceding
Kneser near-core note remains open.  This note proves a sharper normal
form and a genuine statewise obstruction to the ordinary nibble/cleanup
route.

There are two graphs on one common edge set:

* \(K=KG(2m,m-1)\), on the \(N\) lower targets;
* the folded Johnson graph

  \[
       J^{\pm}=J(2m,m)/(X\sim X^c),                            \tag{0.2}
  \]

  on the \(W/2\) complementary owner-pairs.

Every Kneser edge is canonically one folded Johnson edge, and this is a
bijection.  Therefore \((\mathrm {CR})\) is exactly the problem of
selecting a common edge set which is

\[
 \boxed{\text{a matching in \(K\), and has degree at most two in
 \(J^{\pm}\).}}                                               \tag{0.3}
\]

This form gives four exact conclusions.

1. If the matching leaves \(u\) Kneser vertices uncovered, and the
   folded degrees are at most two, then, writing \(n_i\) for the number
   of folded vertices of degree \(i\),

   \[
                         2n_0+n_1=D+u.                         \tag{0.4}
   \]

   Thus the owner defect is automatically already at the optimal
   \(O(D+u)\) scale.  Only matching size and lifted cycle count remain.
2. A pseudorandom residual cannot be cleaned up at the critical scale.
   If lower vertices survive independently with density \(\alpha\) and
   owner clones with density \(\beta\), then the expected number of
   surviving auxiliary edges incident with a retained lower vertex is

   \[
                         2m(m+1)\alpha\beta^2.                 \tag{0.5}
   \]

   At \(u=\Theta(D)\), both densities are \(\Theta(1/m)\), so (0.5) is
   \(O(1/m)\).  With probability tending to one, all but \(o(u)\) of the
   residual lower vertices are isolated in the residual clone
   hypergraph.  The same conclusion holds under a four-resource moment
   upper bound, not merely literal independence.
3. For a common matching with a saturated folded owner \(P=[X]\), its
   two selected incidences determine one canonical alternating Kneser
   rectangle.  If their cells are \((x_1,y_1),(x_2,y_2)\), the rectangle
   is capacity-legal exactly when both cross owners

   \[
             [X-x_1+y_2],\qquad [X-x_2+y_1]                   \tag{0.6}
   \]

   currently have degree at most one.  This is an exact statewise switch
   criterion.  A matching for which every saturated owner fails (0.6) is
   frozen under all elementary alternating rectangles.
4. There is no ordinary one-shore odd-set explanation of a failure of
   \((\mathrm {CR})\).  Outside the Mersenne parity case, the uniform
   Kneser fractional point is the orbit-average of genuine Kneser perfect
   matchings.  The degree relaxation of (0.3) also has optimum exactly
   \(N/2\).  Any obstruction must therefore couple the two graph
   structures; it cannot be a Kneser blossom or a folded-owner capacity
   cut alone.

The decisive negative result is item 2.  Repeated nibbling down to a
random-like \(W/m\) residual and then matching inside that residual is
impossible.  The first-moment threshold of that strategy is

\[
                             \rho\asymp m^{-2/3},              \tag{0.7}
\]

which leaves \(Wm^{-2/3}\gg W/m\) resources.  A successful proof must
prebuild absorbers whose alternate states run through already occupied
resources, and it must correlate the final lower holes with the final
owner-clone holes.  No such absorber, and no cross-graph odd-set
obstruction ruling it out, is proved here.  Hence this is a statewise
no-go theorem for the random-residual and elementary-rectangle routes,
not a disproof of \((\mathrm {CR})\).

## 1. The common-edge bijection

Let

\[
                    \mathcal P=\mathcal M/(X\sim X^c).        \tag{1.1}
\]

For a Kneser edge \(e=\{R,S\}\), write

\[
                    \Omega\setminus(R\cup S)=\{a,b\}.        \tag{1.2}
\]

Define

\[
 \phi(e)=\bigl\{[R+a],[R+b]\bigr\}.                          \tag{1.3}
\]

Since \((R+a)^c=S+b\) and \((R+b)^c=S+a\), the two endpoints in
(1.3) are precisely the two complementary owner-pairs in the canonical
Johnson lift of \(e\).

### Theorem 1.1 (Kneser/folded-Johnson edge bijection)

For \(m\ge3\), the map

\[
        \phi:E(KG(2m,m-1))\longrightarrow E(J^{\pm})          \tag{1.4}
\]

is a bijection.

#### Proof

The representatives \(R+a\) and \(R+b\) differ by one Johnson swap, so
(1.3) is an edge of \(J^{\pm}\).

Conversely, let \([X][Y]\) be a folded Johnson edge.  Choose adjacent
representatives \(X,Y\), and put

\[
                  R=X\cap Y,\qquad S=(X\cup Y)^c.             \tag{1.5}
\]

Then \(|R|=|S|=m-1\), \(R\cap S=\varnothing\), and the two points of
\(X\triangle Y\) form the leave of \(\{R,S\}\).  Formula (1.3) recovers
\([X][Y]\).  For \(m\ge3\), \(X\) cannot be Johnson-adjacent to both
\(Y\) and \(Y^c\): the two conditions would give simultaneously
\(|X\cap Y|=m-1\) and \(|X\cap Y|=1\).  Thus the choice of complement
orientation does not produce a second Kneser edge.  This proves
bijectivity. \(\square\)

The degree and edge counts agree:

\[
 d_K=\Delta=\binom{m+1}{2},\qquad d_{J^{\pm}}=m^2,            \tag{1.6}
\]

\[
 |E(K)|={N\Delta\over2}={Wm^2\over4}=|E(J^{\pm})|.           \tag{1.7}
\]

### Corollary 1.2 (common-factor form of the clone hypergraph)

A set \(F\) of Kneser edges lifts to a matching of the complement-pair
clone hypergraph if and only if

\[
                  d_K^F(R)\le1\quad(R\in\mathcal L),
 \qquad           d_{J^{\pm}}^F(P)\le2\quad(P\in\mathcal P).  \tag{1.8}
\]

#### Proof

The first inequalities say exactly that the projected Kneser edges form
a matching.  At a folded owner \(P\), at most two selected edges can be
assigned injectively to its two clones if and only if its folded degree is
at most two.  Clone assignments at distinct folded vertices are
independent, so no further compatibility remains. \(\square\)

Thus the clone labels are only a capacity implementation.  They introduce
no additional integrality condition after (1.8).

## 2. Exact deficiency and component ledgers

Let \(F\) satisfy (1.8), let

\[
                         |F|={N-u\over2},                      \tag{2.1}
\]

and let \(n_i\) count vertices of \(J^{\pm}\) having \(F\)-degree \(i\),
for \(i=0,1,2\).

### Proposition 2.1 (the Catalan deficiency identity)

One has

\[
 n_0+n_1+n_2={W\over2},\qquad
 n_1+2n_2=N-u,                                                \tag{2.2}
\]

and hence

\[
                         \boxed{2n_0+n_1=D+u.}                 \tag{2.3}
\]

In particular,

\[
 n_0+n_1\le D+u,\qquad n_1\le D+u.                           \tag{2.4}
\]

#### Proof

The first equation counts folded owner vertices.  The second is the
degree sum in the folded graph, because it has \(|F|=(N-u)/2\) edges.
Subtracting the second equation from twice the first gives
\(W-(N-u)=D+u\). \(\square\)

Thus, once the maximum folded degree is two, the owner-pair exceptional
set is automatically Catalan-sized.  For a Kneser perfect matching
\((u=0)\), the conditioned histogram is forced by

\[
                            2n_0+n_1=D.                         \tag{2.5}
\]

This makes clear how strongly polarized the conditioning is: all but at
most \(D\) of the \(W/2\) folded owners have degree exactly two.

Let \(c(F)\) be the number of cycle components of the folded graph
\((\mathcal P,F)\).

### Proposition 2.2 (literal lifted component count)

The canonical Johnson lift of \(F\) has at most

\[
                              n_1+2c(F)                         \tag{2.6}
\]

nontrivial components.

#### Proof

The folded graph has maximum degree two.  It has \(n_1/2\) path
components and \(c(F)\) cycle components.  The canonical Johnson lift is
a two-sheeted cover.  A folded path has two lifted path components.  A
folded cycle has either one or two lifted cycles, according to its
complement voltage.  This gives (2.6). \(\square\)

Consequently, a common factor with \(u=O(D)\) and \(c(F)=O(D)\) already
has \(O(D)=o(W/H)\) owner exceptions and lifted components.  Completion
of its \(u\) uncovered Kneser vertices by at most \(u\) further Kneser
edges changes these bounds only by \(O(u)\).

## 3. Fractional feasibility and where an odd-set obstruction must live

The common-factor integer program is

\[
 \max\sum_{e\in E}x_e                                            \tag{3.1}
\]

subject to

\[
 \sum_{e\ni_K R}x_e\le1\quad(R\in\mathcal L),qquad
 \sum_{e\ni_{J^{\pm}}P}x_e\le2\quad(P\in\mathcal P),qquad
 x_e\in\{0,1\}.                                                \tag{3.2}
\]

The constant point

\[
                              x_e={1\over\Delta}               \tag{3.3}
\]

saturates every Kneser constraint and gives folded degree

\[
                         {m^2\over\Delta}={2m\over m+1}<2.     \tag{3.4}
\]

Thus the degree relaxation has value \(N/2\), which is optimal by the
Kneser shore.

When \(N\) is even, the connected vertex-transitive graph \(K\) has a
perfect matching.  Averaging the incidence vector of one such matching
over the coordinate-permutation group gives exactly (3.3), because the
group is edge-transitive.  Hence (3.3) lies in the genuine Kneser
perfect-matching polytope and satisfies every Kneser blossom inequality.

When \(N\) is odd, the same vertex-transitive matching theorem gives a
near-perfect matching after deleting one vertex; orbit-averaging gives
the uniform value

\[
                         {N-1\over N\Delta},                   \tag{3.5}
\]

whose total loss is exactly one half-edge.  This is the Mersenne parity
loss and is \(O(1)\).

Therefore a dual obstruction of order \(D\), if it exists, cannot be an
ordinary odd cut of \(K\) alone.  Nor can it be a folded degree-capacity
cut alone, since (3.4) has total folded slack exactly \(D\).  It must be a
cross inequality involving how the bijection \(\phi\) couples a Kneser
odd set to a folded-owner set.  No such inequality is found here.

## 4. The random-residual no-go theorem

Return temporarily to the cloned four-uniform hypergraph
\(\mathfrak K_m\).  Its two vertex shores are

\[
                         \mathcal L,qquad
                         \mathcal C=\mathcal P\times\{0,1\},  \tag{4.1}
\]

of sizes \(N\) and \(W\).  Every auxiliary edge contains two vertices
from each shore.  Its exact number of edges is

\[
                         |E(\mathfrak K_m)|=2N\Delta,           \tag{4.2}
\]

and every lower vertex has degree \(4\Delta=2m(m+1)\).

Retain each lower vertex independently with probability \(\alpha\), and
each owner clone independently with probability \(\beta\).  Let
\(Z_{\mathcal L}\) be the retained lower set and let \(Y\) be the number
of auxiliary edges all four of whose vertices survive.

### Theorem 4.1 (induced-residual isolation)

If

\[
                        m^2\alpha\beta^2=o(1)                  \tag{4.3}
\]

and \(N\alpha\to\infty\), then with probability tending to one,

\[
 |Z_{\mathcal L}|=(1+o(1))N\alpha,qquad
 Y=o(N\alpha).                                                 \tag{4.4}
\]

Consequently every matching contained entirely in the induced residual
hypergraph covers only \(o(|Z_{\mathcal L}|)\) retained lower vertices.

#### Proof

Binomial concentration gives the first assertion in (4.4).  Every
auxiliary edge survives with probability \(\alpha^2\beta^2\), and hence

\[
 \mathbb EY=2N\Delta\alpha^2\beta^2,qquad
 {\mathbb EY\over N\alpha}=2\Delta\alpha\beta^2=o(1).         \tag{4.5}
\]

Choose any \(\varepsilon_m\downarrow0\) with
\(2\Delta\alpha\beta^2=o(\varepsilon_m)\).  Markov's inequality gives
\(Y\le\varepsilon_mN\alpha\) with probability tending to one.  A
matching with \(Y\) available hyperedges covers at most \(2Y\) lower
vertices. \(\square\)

The proof uses only a four-resource moment bound.  Namely, the conclusion
remains true for any random residual law satisfying

\[
 \Pr(e\subseteq Z)\le C\alpha^2\beta^2
       \quad(e\in E(\mathfrak K_m))                            \tag{4.6}
\]

for a fixed \(C\), together with
\(|Z_{\mathcal L}|=(1+o(1))N\alpha\) with high probability.

### Corollary 4.2 (the critical and random-greedy scales)

Suppose a partial auxiliary matching leaves \(u\) lower vertices and
therefore \(D+u\) owner clones unused.  The corresponding densities are

\[
                  \alpha={u\over N},qquad
                  \beta={D+u\over W}.                          \tag{4.7}
\]

If \(u=\Theta(D)\), then \(\alpha,\beta=\Theta(1/m)\), and Theorem 4.1
applies.  A product-like critical residual has only \(O(W/m^2)\)
surviving auxiliary edges in expectation but \(\Theta(W/m)\) lower
holes.  It cannot internally cover more than an \(o(1)\) fraction of
those holes.

More generally, while \(u\gg D\) and both residual densities have order
\(\rho=u/W\), a retained lower vertex has expected residual degree

\[
                       \Theta(m^2\rho^3).                      \tag{4.8}
\]

Therefore the first-moment threshold for a random-like residual is

\[
                              \rho=m^{-2/3}.                   \tag{4.9}
\]

Below that scale, almost all residual lower vertices are isolated.  Since
\(m^{-2/3}\gg m^{-1}\), an ordinary random-greedy descent cannot reach
the Catalan residual without an absorber which uses previously matched
resources.

This is a statewise assertion about the residual law.  It does not say
that a deliberately correlated residual of size \(O(D)\) is impossible.

## 5. Exact arithmetic of a genuine absorber

Let \(F_0,F_1\) be two matchings of \(\mathfrak K_m\), and define their
signed covered-resource boundary by

\[
                     \partial=\mathbf1_{V(F_1)}-
                                  \mathbf1_{V(F_0)}.           \tag{5.1}
\]

### Proposition 5.1 (two-by-two boundary law)

If \(|F_1|-|F_0|=t\), then

\[
 \sum_{R\in\mathcal L}\partial(R)=2t,qquad
 \sum_{c\in\mathcal C}\partial(c)=2t.                        \tag{5.2}
\]

In particular, a clean absorber which increases matching size by one and
has no negatively exposed resource has boundary consisting of exactly two
new lower vertices and two new owner clones.

#### Proof

Every auxiliary edge contains exactly two vertices of each shore.  A
matching of size \(s\) therefore covers exactly \(2s\) vertices in each
shore.  Subtract the two identities for \(F_0,F_1\). \(\square\)

Absorbing all \(u\) lower holes requires \(u/2\) additional matching
edges and consumes net \(u\) owner clones.  The initial \(D+u\) clone
holes then leave exactly the forced Catalan slack \(D\).  Thus there is no
scalar absorption deficit.  The obstruction in Theorem 4.1 is geometric:
the two lower and two clone boundary resources do not arrive as legal
four-tuples.  They must be joined by alternating structures passing
through the occupied matching.

## 6. Exact elementary switching at a saturated owner

Let \(F\) be a Kneser matching satisfying the folded capacity bound, and
fix \(P=[X]\) with folded degree two.  Every Kneser edge incident with
\(P\) has a unique cell representation

\[
 e_{x,y}=\{X-x,X^c-y\},qquad (x,y)\in X\times X^c.            \tag{6.1}
\]

Let the two selected cells at \(P\) be

\[
                         (x_1,y_1),\qquad(x_2,y_2).            \tag{6.2}
\]

Because \(F\) is a Kneser matching,

\[
                         x_1\ne x_2,qquad y_1\ne y_2.        \tag{6.3}
\]

For a cell define its secondary folded owner

\[
                         Q_{ij}=[X-x_i+y_j].                   \tag{6.4}
\]

### Lemma 6.0 (classification of Kneser 4-cycles)

Every nondegenerate 4-cycle of \(KG(2m,m-1)\) has the grid form used in
(6.1)--(6.3): its two vertices on one side are distinct facets of an
\(m\)-set \(X\), and its two vertices on the other side are distinct
facets of \(X^c\).

#### Proof

Write the cycle as \(A-B-C-E-A\), so \(A,C\) are both disjoint from
\(B,E\).  Since \(B,E\) are two distinct \((m-1)\)-subsets of
\(\Omega\setminus(A\cup C)\), that complement has size at least \(m\).
Thus \(|A\cup C|\le m\).  Distinct \((m-1)\)-sets have union of size at
least \(m\), so equality holds.  Put \(X=A\cup C\).  Then \(A,C\) are
distinct facets of \(X\), while \(B,E\subseteq X^c\).  Their sizes and
distinctness force \(B\cup E=X^c\), so they are distinct facets of
\(X^c\). \(\square\)

### Theorem 6.1 (canonical pivot rectangle)

The replacement

\[
             \{e_{x_1,y_1},e_{x_2,y_2}\}
       \longmapsto
             \{e_{x_1,y_2},e_{x_2,y_1}\}                     \tag{6.5}
\]

is an alternating Kneser 4-cycle switch and remains a Kneser matching.
Its folded-degree signature is

\[
                    -\mathbf e_{Q_{11}}-\mathbf e_{Q_{22}}
                    +\mathbf e_{Q_{12}}+\mathbf e_{Q_{21}},   \tag{6.6}
\]

while the degree of \(P\) remains two.  For \(m\ge3\), it preserves the
folded maximum-degree-two condition if and only if

\[
                         d_F(Q_{12})\le1,qquad
                         d_F(Q_{21})\le1.                      \tag{6.7}
\]

#### Proof

The four Kneser vertices are

\[
 X-x_1,\quad X^c-y_1,\quad X-x_2,\quad X^c-y_2.              \tag{6.8}
\]

Every facet of \(X\) is disjoint from every facet of \(X^c\).  Thus the
old and crossed pairings are the two parity classes of a Kneser 4-cycle;
(6.3) makes all four vertices distinct.  Each cell edge has folded
endpoints \(P,Q_{ij}\), proving (6.6).  For \(m\ge3\), the four secondary
owners in (6.6) are distinct.  Equality of two representatives forces
equality of the corresponding row and column indices; equality with a
complement would make one \(m\)-set contain at least \(m-1\) elements of
\(X\) and at most one element of \(X\), which is impossible for
\(m\ge3\).  The old secondary degrees only decrease.
The two new secondary degrees increase by one, so the capacity condition
is exactly (6.7). \(\square\)

### Corollary 6.2 (a statewise rectangle no-go certificate)

Call \(F\) **rectangle-frozen** if for every folded owner \(P\) of degree
two, the two cross owners determined by its selected cells satisfy

\[
                         \max\{d_F(Q_{12}),d_F(Q_{21})\}=2.    \tag{6.9}
\]

Then no elementary alternating Kneser rectangle can be applied while
remaining inside the folded capacity region.

#### Proof

Lemma 6.0 shows that every nondegenerate Kneser 4-cycle is based at a
folded pivot \(P\).  If its old parity belongs to \(F\), then the pivot
has degree two and its old parity is exactly the two selected cells in
(6.2).  Theorem 6.1 says that the other parity is capacity-legal exactly
when both cross owners have degree at most one.  Condition (6.9) excludes
this at every pivot. \(\square\)

Thus an elementary-switch proof of \((\mathrm {CR})\) needs an additional
theorem excluding rectangle-frozen high-cardinality states.  Degree
counts do not exclude them: by (2.3), a near-perfect feasible state has
only \(D+u\) total units of folded slack, whereas almost every possible
pivot is saturated.  No expansion theorem ruling out (6.9) is presently
available.

Longer alternating cycles can evade this certificate.  Their exact
condition is that their positive folded signature fit inside the current
slack vector.  A component-joining theorem must therefore either construct
such balanced longer cycles or prove that the defect owners in (2.3) can
be routed through successive legal pivot rectangles.

## 7. What remains for \((\mathrm {CR})\)

The owner part of \((\mathrm {CR})\) is now the following sharply isolated
statement.

> **Common-factor theorem.**  The common edge set of \(K\) and
> \(J^{\pm}\) contains a set \(F\) with
> \[
>       d_K^F\le1,qquad d_{J^{\pm}}^F\le2,qquad
>       |F|\ge {N\over2}-O(D),qquad c(F)=O(D).                \tag{7.1}
> \]

Theorem 4.1 rules out proving (7.1) by continuing a product-like nibble
inside its residual.  Proposition 5.1 says exactly what a valid absorber
must exchange.  Theorem 6.1 supplies the smallest alternating move and
Corollary 6.2 gives its exact stopping certificate.  Section 3 rules out
an obstruction confined to either graph separately.

The live alternatives are therefore:

1. construct a correlated absorber reservoir whose alternate matching
   states realize all admissible two-lower/two-clone boundaries from
   Proposition 5.1;
2. prove that the defect set \(2n_0+n_1=D+u\) can always be routed through
   the pivot rectangles (6.5) without reaching a frozen state; or
3. exhibit a genuinely cross-graph blossom/odd-set inequality violated by
   every integral solution of size \(N/2-O(D)\).

None of these three final statements is proved here.  In particular, the
conditioned random-perfect-matching route must not be declared successful
from its one-point mean: conditioning on maximum folded degree two forces
the global histogram (2.5), and no estimate showing that this conditioned
set is nonempty has been established.
