# The two-sided diamond 2-factor problem

## Status

This note isolates the exact all-dimensional depth-one problem.  It does not
prove the desired construction for every `m`, and it does not produce an
obstruction.  It does prove four useful facts.

1. The problem is exactly an orthogonal pair of extension matchings between
   ranks `m-1` and `m`.
2. If the upper-shadow condition is deleted, the remaining problem is an
   ordinary bipartite `b`-matching and is always solvable.
3. Restoring the upper-shadow condition takes the problem outside the direct
   scope of ordinary `b`-matching and two-matroid intersection.  This is not
   just a matter of presentation: the natural matrix is not totally
   unimodular and the middle-degree independence system is not a matroid.
4. There is a smallest exact signed trade, a four-diamond rectangle, which
   preserves every lower and upper colour while moving load among four
   middle vertices.

The smallest exact missing lemma is stated in Section 8.

Throughout, the ground set is `[2m]`.  Put

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1},
\]

and

\[
 W=|\mathcal M|=\binom{2m}m,\qquad
 N=|\mathcal L|=|\mathcal U|=\binom{2m}{m-1}
   =\frac m{m+1}W,
\]

\[
 C_m=W-N=\frac{W}{m+1}=\operatorname{Cat}_m.
\tag{0.1}
\]

The near-perfect hypergraph theorem in `ASYMPTOTIC_MATCHING.md` and the exact
branching Greene--Kleitman forest in `GK_TWO_SIDED_RAINBOW_FOREST.md` are
assumed.  Nothing below repeats either argument.

## 1. Diamonds and the exact integer system

For every incidence

\[
 S\in\mathcal L,\qquad U\in\mathcal U,\qquad S\subset U,
\]

write `U\setminus S={a,b}`.  The interval `[S,U]` contains exactly two
middle sets

\[
 X=S\cup\{a\},\qquad Y=S\cup\{b\}.
\]

Call `(S,U)` a diamond.  It is also the Johnson edge `XY`, with its two
colours recorded exactly:

\[
 X\cap Y=S,\qquad X\cup Y=U.
\tag{1.1}
\]

Let `x_{S,U}` be the indicator that the diamond is selected.  The exact
depth-one problem is

\[
 \sum_{U\supset S}x_{S,U}=1 \quad(S\in\mathcal L),
\tag{1.2}
\]

\[
 \sum_{S\subset U}x_{S,U}=1 \quad(U\in\mathcal U),
\tag{1.3}
\]

\[
 \sum_{S\subset X\subset U}x_{S,U}\le 2
       \quad(X\in\mathcal M),
\tag{1.4}
\]

\[
 x_{S,U}\in\{0,1\}.
\tag{1.5}
\]

Equations (1.2)--(1.3) say that the selected diamonds form a perfect
matching in the regular bipartite inclusion graph between `mathcal L` and
`mathcal U`.  Inequality (1.4) says that the projected Johnson graph has
maximum degree two.

The bipartite inclusion graph has degree

\[
 D=\binom{m+1}{2}.
\tag{1.6}
\]

A fixed middle set lies in exactly `m^2` diamonds: choose the deleted
coordinate in the set and the inserted coordinate outside it.

### Fractional sanity check

The uniform point

\[
 x_{S,U}=\frac1D
\tag{1.7}
\]

satisfies (1.2)--(1.3), and its load at every middle set is

\[
 \frac{m^2}{D}=\frac{2m}{m+1}=2-\frac2{m+1}<2.
\tag{1.8}
\]

Thus the linear relaxation has exactly the right average slack.  Any
obstruction must be integral, ordered, or cyclic; it cannot be a first-order
capacity obstruction.

## 2. Exact reduction to two orthogonal extension matchings

Let `H_m` be the bipartite inclusion graph between `mathcal L` and
`mathcal M`.  Its degrees are

\[
 \deg(S)=m+1\quad(S\in\mathcal L),\qquad
 \deg(X)=m\quad(X\in\mathcal M).
\tag{2.1}
\]

### Theorem 2.1 (orthogonal two-extension equivalence)

The diamond system (1.2)--(1.5) is feasible if and only if there are maps

\[
 f_0,f_1:\mathcal L\longrightarrow\mathcal M
\]

such that

1. `S subset f_i(S)` for `i=0,1`;
2. `f_0(S) ne f_1(S)` for every `S`;
3. both `f_0` and `f_1` are injective; and
4. the map

   \[
    u(S)=f_0(S)\cup f_1(S)
    \tag{2.2}
   \]

   is injective, hence is a bijection from `mathcal L` to `mathcal U`.

Under this equivalence the selected middle graph has the directed edges

\[
 f_0(S)\longrightarrow f_1(S).
\tag{2.3}
\]

It is a linear forest exactly when these directed edges contain no directed
cycle.

#### Proof

Suppose first that (1.2)--(1.5) is feasible.  Its projected middle graph has
maximum degree two, so each path and cycle component can be oriented
consistently.  For the edge with lower colour `S`, let `f_0(S)` be its tail
and `f_1(S)` its head.  Consistent orientation gives indegree and outdegree
at most one, so both maps are injective.  The union in (2.2) is the selected
upper colour.  Equation (1.3) says that these upper colours are all distinct.

Conversely, the pair `f_0(S),f_1(S)` consists of the two middle sets in the
diamond `[S,u(S)]`.  Select that diamond.  Injectivity of `u` gives every
upper colour once.  Injectivity of the two `f_i` gives indegree and outdegree
at most one, hence undirected degree at most two.  A directed cycle is the
same thing as a cycle in the underlying degree-two graph.  QED.

This is the cleanest exact formulation found in this pass.  The two maps are
ordinary extension matchings; their **orthogonality** is the requirement
that their pairwise unions are all different.

### Complementary Kneser quotient

There is an equally exact self-dual formulation.  Replace an upper colour
`U` by the lower set `T=U^c`.  Then

\[
 S\subset U\quad\Longleftrightarrow\quad S\cap T=\varnothing.
\tag{2.4}
\]

Thus the lower--upper inclusion graph is the bipartite double cover of the
Kneser graph `KG(2m,m-1)`.  A colour-perfect diamond selection is the same as
a permutation

\[
 \pi:\mathcal L\longrightarrow\mathcal L,
 \qquad S\cap\pi(S)=\varnothing.
\tag{2.5}
\]

For one transition `(S,pi(S))`, exactly two coordinates lie outside
`S cup pi(S)`; adjoining either one to `S` gives the two projected middle
vertices.  The degree-two condition says that each middle set separates at
most two of these directed disjointness transitions.

This quotient makes complementation explicit but does not by itself solve
the degree problem.  If `pi` is an involution, selected Johnson edges occur
in complementary pairs and `d(X)=d(X^c)`.  That is a natural way to realize
the balanced defect law in Section 5, but an involution is unavailable when
`N` is odd and is not known to enforce degree two when it exists.

## 3. Exactly what ordinary b-matching solves

Delete condition 4 of Theorem 2.1.  Then one only asks for two injective
extensions of every lower set, with combined middle capacity two.

This reduced problem is an ordinary bipartite `b`-matching in `H_m`:

\[
 \deg_F(S)=2\quad(S\in\mathcal L),\qquad
 \deg_F(X)\le2\quad(X\in\mathcal M).
\tag{3.1}
\]

It is always feasible.  Indeed, by Konig's line-colouring theorem, the
bipartite graph `H_m` has a proper edge-colouring with `m+1` colours.  Every
lower vertex sees all `m+1` colours, and a middle vertex sees each colour at
most once.  The union of any two colour classes satisfies (3.1).  Its path
and cycle components can be alternately coloured, producing the maps
`f_0,f_1`.

Therefore:

> Lower-colour completeness plus middle degree at most two is easy.  The
> entire depth-one difficulty is making the `N` unions in (2.2) distinct
> (and, for the forest version, removing bichromatic cycles).

Fixing one injection `f_0` makes the remaining obstruction especially
transparent.  For each `S`, a candidate second extension `Y` determines

\[
 U=f_0(S)\cup Y.
\]

One must choose one triple `(S,Y,U)` for each `S`, without repeating `Y` or
`U`.  This is a three-partite matching problem, not a bipartite matching
problem.

## 4. Why the standard matroid shortcut does not apply

There are two separate issues.

### 4.1 The degree-two system is not a matroid

On the Johnson-edge ground set, let

\[
 \mathcal I_2=\{F:\Delta(F)\le2\}.
\]

For every `m>=2`, this independence system fails the matroid exchange axiom.
Fix an `(m-2)`-set `C` and four further coordinates `a,b,c,d`.  Put

\[
 v_0=C+ab,\quad v_1=C+ac,\quad v_2=C+ad,
 \quad v_3=C+bc,\quad v_4=C+bd.
\]

All edges below are Johnson edges.  Let

\[
 A=\{v_0v_1,v_0v_2,v_1v_2\}
\]

and

\[
 B=\{v_0v_1,v_0v_2,v_1v_3,v_2v_4\}.
\]

Both have maximum degree two and `|A|=3<4=|B|`.  But every edge of
`B\setminus A` meets a vertex already of degree two in `A`, so neither can be
adjoined to `A`.  Thus `mathcal I_2` is not a matroid.

The lower- and upper-rainbow conditions are two partition matroids.  The
degree system cannot simply be installed as a third matroid and then handled
by ordinary two-matroid intersection.  Requiring acyclicity adds the graphic
matroid as yet another independent condition.

### 4.2 The natural constraint matrix is not totally unimodular

Take three middle sets forming a Johnson triangle.  Restrict the
middle-load rows and the three corresponding diamond columns to this
triangle.  The resulting submatrix is

\[
 \begin{pmatrix}
  1&1&0\\
  1&0&1\\
  0&1&1
 \end{pmatrix},
\]

whose determinant is `-2`.  Hence the natural matrix for
(1.2)--(1.4) is not totally unimodular, already for `m=2`.

This does not prove computational hardness for the highly symmetric Boolean
instance.  It proves only the relevant point: neither the standard
bipartite-matching polytope nor a direct partition-matroid intersection gives
integrality for free.

## 5. The exact degree-defect design forced by both colour systems

Let `G` be any lower- and upper-colour-perfect diamond selection, and let
`d(X)` be its projected middle degree.  Whether or not `d(X)<=2`, one has

\[
 \sum_{X\in\mathcal M}d(X)=2N.
\tag{5.1}
\]

There is also an exact coordinatewise law.

### Theorem 5.1 (balanced defect law)

For every coordinate `i in [2m]`,

\[
 \sum_{X\ni i}d(X)=N.
\tag{5.2}
\]

Consequently, if `d(X)<=2` and

\[
 \delta(X)=2-d(X),
\]

then

\[
 \sum_X\delta(X)=2C_m,
\tag{5.3}
\]

and, for every coordinate `i`,

\[
 \sum_{X\ni i}\delta(X)=C_m.
\tag{5.4}
\]

#### Proof

For one selected diamond `(S,U)` with middle endpoints `X,Y`, the coordinate
incidence vectors satisfy

\[
 \mathbf1_X+\mathbf1_Y=\mathbf1_S+\mathbf1_U.
\tag{5.5}
\]

Sum (5.5) over all selected diamonds.  Every lower and upper set occurs once.
For a fixed coordinate, the number of lower occurrences is
`binom(2m-1,m-2)` and the number of upper occurrences is
`binom(2m-1,m)`.  Their sum is `N`, proving (5.2).  Equations (5.3)--(5.4)
follow from `W-N=C_m` and the fact that exactly half of the middle sets
contain a fixed coordinate.  QED.

Thus the missing degree is not arbitrary.  The endpoint/isolated-vertex
tokens form a weighted `1`-design on `[2m]`.

If `G` is acyclic, it has

\[
 W-N=C_m
\]

path components.  A degree-one endpoint contributes one defect token and an
isolated vertex contributes two.  Equation (5.4) says that every coordinate
occurs in exactly `C_m` of the `2C_m` endpoint tokens, counted with
multiplicity.  Complement-paired endpoints are therefore a natural, though
not forced, exact design.

If cycles are allowed and `z` is the number of cycle components, then the
number of components is

\[
 C_m+z.
\tag{5.6}
\]

## 6. A stronger symmetric factorization target

The ordinary edge-colouring of `H_m` gives a useful sufficient formulation.
Let

\[
 \kappa:E(H_m)\longrightarrow\{0,1,\ldots,m\}
\]

be a proper `(m+1)`-edge-colouring.  Fix two colours `alpha,beta`.  Every
`S in mathcal L` has a unique `alpha`-extension `f_alpha(S)` and a unique
`beta`-extension `f_beta(S)`.

For `U in mathcal U`, define

\[
 h_{\alpha\beta}(U)=
 \#\{S\subset U:
   f_\alpha(S)\cup f_\beta(S)=U\}.
\tag{6.1}
\]

Always

\[
 \sum_{U\in\mathcal U}h_{\alpha\beta}(U)=N=|\mathcal U|.
\tag{6.2}
\]

Hence collisions and holes balance exactly.

### Corollary 6.1 (orthogonal acyclic colour-pair criterion)

The depth-one linear forest exists if there is a proper edge-colouring
`kappa` and a pair `alpha,beta` such that

\[
 h_{\alpha\beta}(U)=1\quad(U\in\mathcal U)
\tag{6.3}
\]

and the `alpha,beta` bichromatic subgraph of `H_m` is acyclic.

Indeed, suppressing every lower vertex in that bichromatic graph gives the
required middle-layer linear forest.

This criterion is stronger than Theorem 2.1, because a successful pair of
partial extension matchings need not extend to a full `(m+1)`-edge-colouring.
It is nevertheless the most concrete symmetric-factorization target found
here.

One should not strengthen (6.3) to demand that **every** colour pair work.
For example, that stronger statement is impossible already at `m=3`.
If every pair worked, then inside each `U` the colour pairs on its
`binom(m+1,2)` diamonds would be all pairs exactly once.  It would follow
that the unique colour missing at each middle vertex properly colours the
Johnson graph `J(2m,m)` with `m+1` colours.  But `J(6,3)` is not 4-colourable:
one colour class is a family of triples with pairwise intersections at most
one, so has size at most four.  Size five would be a Steiner triple system on
six points, impossible because a point would have replication number
`5/2`.  Four classes therefore cover at most sixteen of the twenty triples.

Thus a viable factorization must distinguish one colour pair; universal
pairwise orthogonality is too strong.

## 7. Exact colour-preserving trades

The natural move space lives in the bipartite graph between `mathcal L` and
`mathcal U`.  Any two perfect matchings in that graph differ by alternating
even cycles.  The smallest move is a four-cycle.

Fix `X in mathcal M`, distinct `a,b in X`, and distinct `c,d notin X`.  Put

\[
 S_a=X\setminus\{a\},\quad S_b=X\setminus\{b\},\qquad
 U_c=X\cup\{c\},\quad U_d=X\cup\{d\}.
\]

Suppose the current colour-perfect matching contains

\[
 (S_a,U_c),\qquad(S_b,U_d).
\]

Replace them by

\[
 (S_a,U_d),\qquad(S_b,U_c).
\tag{7.1}
\]

This preserves both lower colours and both upper colours exactly.  Every one
of the four diamonds contains the pivot `X`.  If

\[
 X_{p,q}=X\setminus\{p\}\cup\{q\},
\]

then the change in the projected middle-degree vector is

\[
 -\mathbf1_{X_{a,c}}-\mathbf1_{X_{b,d}}
 +\mathbf1_{X_{a,d}}+\mathbf1_{X_{b,c}},
\tag{7.2}
\]

while the contribution at `X` remains two.

Equation (7.2) is the basic signed load-transfer relation.  It is an exact
two-edge absorber whenever the two old secondary vertices are overloaded
and the two new secondary vertices have spare capacity.  It may create or
destroy a middle cycle, so acyclicity must be checked separately.

More generally, if

\[
 S_1,U_1,S_2,U_2,\ldots,S_t,U_t,S_1
\]

is an alternating cycle in the lower--upper inclusion graph, replacing
`(S_i,U_i)` by `(S_i,U_{i+1})` (cyclic indices) preserves every lower and
upper colour.  These alternating-cycle switches are the complete global
move language between colour-perfect matchings.  What is missing is an
augmenting theorem showing that their signed load vectors can always remove
all degree-three vertices without creating new ones.

## 8. The smallest exact missing lemma

The general depth-one problem is now the following.

### Orthogonal two-SDR lemma

For every `m>=1`, there exist two injective maps

\[
 f_0,f_1:\binom{[2m]}{m-1}\longrightarrow\binom{[2m]}m
\]

such that

\[
 S\subset f_i(S),\qquad f_0(S)\ne f_1(S),
\]

and the unions

\[
 \{f_0(S)\cup f_1(S):S\in\binom{[2m]}{m-1}\}
\]

are all distinct.

The acyclic refinement asks in addition that the directed graph

\[
 f_0(S)\longrightarrow f_1(S)
\]

have no directed cycle.

By Theorem 2.1, the first statement is **equivalent** to a two-sided rainbow
middle graph of maximum degree two.  The refinement is equivalent to the
desired `C_m`-component linear forest.

No ordinary Hall condition remains to be checked separately: each one-sided
and each degree-capacity relaxation is already feasible.  The only missing
condition is orthogonality of the two systems of distinct representatives.

There are three credible next attacks.

1. **Orthogonal edge-colouring.**  Construct `kappa` and one distinguished
   pair satisfying (6.3), then use Kempe changes to eliminate bichromatic
   cycles.
2. **Convex load minimization plus rectangle trades.**  Choose a perfect
   lower--upper matching minimizing a strictly convex function of the middle
   loads.  Prove that every load at least three admits an alternating-cycle
   trade, beginning with (7.1), that lowers the potential.
3. **Exact absorption in the cloned hypergraph.**  Strengthen the near-perfect
   matching from `ASYMPTOTIC_MATCHING.md` so that all lower and upper colour
   vertices are covered while exactly `2C_m` middle clones are left unused,
   with those unused clones forming the balanced design (5.4).  Fixed-girth
   conflicts can then enforce the forest condition.

## 9. Symmetry warning and final ledger

A fully `Sym(2m)`-equivariant construction is impossible for `m>=2`.  If an
equivariant map sent `S in mathcal L` to an upper set `U supset S`, then the
two-set `U\setminus S` would have to be invariant under the full symmetric
group on the `m+1` coordinates outside `S`.  No such two-set exists when
`m+1>=3`.  Any explicit construction must therefore choose additional
structure: an order, a cyclic action, an SCD, or a seed.

The exact ledger is:

* **proved:** lower and upper colour perfection alone is an ordinary perfect
  matching;
* **proved:** lower perfection plus middle degree two is always an ordinary
  `b`-matching;
* **proved:** the full problem is exactly the orthogonal two-SDR lemma;
* **proved:** every solution has the balanced endpoint-defect design
  (5.3)--(5.4);
* **proved:** four-diamond rectangles are exact two-sided colour-preserving
  load trades;
* **not proved:** an orthogonal two-SDR for every `m`;
* **not proved:** cycle elimination while preserving both colour systems;
* **not available for free:** total unimodularity, an ordinary `b`-matching
  reduction, or direct two-matroid intersection.

So the depth-one problem has not been solved, but it has been reduced to one
precise orthogonality lemma.  This is substantially smaller than the full
universal-OR construction and is the right target before attempting longer
shadows or pinning.
