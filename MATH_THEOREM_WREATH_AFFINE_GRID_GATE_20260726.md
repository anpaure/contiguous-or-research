# The actual-wreath affine-grid gate

Date: 2026-07-26

Method: pure mathematics only.

Let

\[
                         p=2m+1
\]

be prime, let `F` be an exact middle wreath factor, and let `sigma` be a
coordinate `p`-cycle.  Assume the rows under discussion are transversal
for the `sigma`-necklace partition, so the multiplicity matrix `B_sigma`
is zero-one there.

Theorem 32.3 of the prime-cycle rigidity file shows that a smallest
frequency-zero mixed count has the following form.  There are two row
families

\[
                         P=\{C_i:i\in F_p\},
 \qquad N=\{D_j:j\in F_p\},
\tag{1.1}
\]

such that every pair `(C_i,D_j)` has one common necklace, all these `p^2`
necklaces are distinct, and there are no other incidences from these rows
to these necklaces.  The count vector doubles the rows in `P` and omits
the rows in `N`.

This note records what the actual cyclic-interval geometry adds to that
abstract affine `K_(p,p)` grid.

## 1. Exact phase-array normal form

For every `(i,j)`, let `O_(ij)` be the common necklace.  There are unique
middle sets

\[
 X_{ij}\in C_i\cap O_{ij},
 \qquad
 Y_{ij}\in D_j\cap O_{ij},
\tag{1.2}
\]

and a unique nonzero phase `phi_(ij) in F_p^*` such that

\[
                         Y_{ij}=\sigma^{\phi_{ij}}X_{ij}.
\tag{1.3}
\]

The phase is nonzero because distinct rows of the exact factor have
disjoint physical middle supports.

### Proposition 1.1 (bi-wreath Latin array)

The array `(X_(ij))` has the following exact properties.

1. For fixed `i`, the `p` sets `(X_(ij):j in F_p)` are precisely the
   middle packet of the wreath row `C_i`.
2. For fixed `j`, the `p` sets

   \[
                           (\sigma^{\phi_{ij}}X_{ij}:i\in F_p)
   \tag{1.4}
   \]

   are precisely the middle packet of the wreath row `D_j`.
3. All `2p^2` physical sets in (1.2) are distinct, while the `p^2`
   necklace classes are distinct.

Thus an actual affine grid is a `p by p` Latin array whose rows are
odd-graph `p`-cycles and whose columns become odd-graph `p`-cycles after
entrywise coordinate shifts.

#### Proof

Every row has `p` necklace incidences.  In the equality case each row in
`P` meets each row in `N` once, so its `p` incidences are exactly (1.2).
The same argument applies to each `D_j`.  Exact ownership in `F` gives
physical disjointness. \(\square\)

This is the first necessary normal form not possessed by the abstract
affine-plane counterexample: the two sides of its incidence grid must both
be shortest odd cycles of `KG(p,m)`.

## 2. What harmonic information cannot see

Put

\[
 g_P=\sum_i\mathbf1_{\mathcal W_m(C_i)},
 \qquad
 g_N=\sum_j\mathbf1_{\mathcal W_m(D_j)},
 \qquad z=g_P-g_N.
\tag{2.1}
\]

The affine grid says exactly

\[
                         Q_\sigma z=0,
 \qquad Q_\sigma=I+\sigma+\cdots+\sigma^{p-1}.
\tag{2.2}
\]

Moreover each wreath row contains every coordinate in exactly `m` of its
`p` middle sets.  Therefore

\[
                         \Pi_0z=\Pi_1z=0.
\tag{2.3}
\]

Consequently every `sigma`-invariant statistic of one middle set has the
same total on the two row families.  This includes all necklace orbit
masses and every degree-one Johnson statistic.  Once a phase-isolated
grid is converted into two decompositions of the same physical support
(Section 3), **all** vertex statistics agree identically, in every Johnson
degree.

Thus no vertex-load, collision-energy or Johnson-harmonic argument can
exclude the final orthogonal wreath trade.  The obstruction, if one
exists, must use phase curls, odd-graph edges, endpoint colors, or another
decomposition-sensitive invariant.

## 3. The phase-curl obstruction for a supported mixed move

There is a particularly important local version of the count change.
Start with the exact factor `F`, omit the original rows `D_j`, retain every
other original row (including every `C_i`), and add one further translate

\[
                         \sigma^{a_i}C_i
 \qquad(i\in F_p).
\tag{3.1}
\]

Call this a **supported affine-grid move**.  No row outside `P union N`
changes phase.

### Theorem 3.1 (row-constant phase criterion)

The supported move (3.1) is an exact middle factor if and only if

\[
                         \boxed{\phi_{ij}=a_i
                         \quad\hbox{for every }i,j.}
\tag{3.2}
\]

When (3.2) holds, the two `p`-row families

\[
                         \{\sigma^{a_i}C_i:i\in F_p\}
 \quad\hbox{and}\quad
                         \{D_j:j\in F_p\}
\tag{3.3}

are two wreath factorizations of the same `p^2` physical middle sets, and
their ownership overlay is `K_(p,p)`.

#### Proof

At necklace `O_(ij)`, all unchanged original rows still occupy their old
phases.  The only removed physical set is `Y_(ij)`, and the only new set
available from the changed rows is `sigma^(a_i)X_(ij)`.  Exact ownership
therefore holds precisely when

\[
                         \sigma^{a_i}X_{ij}=Y_{ij},
\]

which is (3.2).  The `p^2` equalities are pairwise on distinct necklaces,
so they identify the two unions in (3.3) without multiplicity. \(\square\)

There is a lossless relative version.  Suppose `e:F->F_p` is any legal
one-translate-per-row phase lift.  Delete the selected copies
`sigma^(e(D_j))D_j` and add one extra copy `sigma^(a_i)C_i` of every
positive row, leaving the baseline copies in place.

### Corollary 3.2 (rank-one phase matrix)

The relative supported move is exact if and only if

\[
                         \boxed{
 \phi_{ij}=a_i-e(D_j).}
\tag{3.4}
\]

Equivalently the additive phase matrix has zero `2 by 2` curl:

\[
 \boxed{
 \phi_{ij}-\phi_{ij'}-\phi_{i'j}+\phi_{i'j'}=0
 \quad(i,i',j,j').}
\tag{3.5}
\]

Equivalently again, the complex matrix `(zeta^(phi_(ij)))` has rank one.
Therefore a single nonzero phase curl excludes every affine-grid move
which is adjacent to a legal row-power factor.

#### Proof

The removed set at `O_(ij)` is
`sigma^(e(D_j)+phi_(ij))X_(ij)`, while the added set is
`sigma^(a_i)X_(ij)`.  Equality gives (3.4).  Additive separability is
equivalent to (3.5), and exponentiation gives the rank-one formulation.
\(\square\)

This is a genuine, checkable phase obstruction.  It does not exclude a
mixed selection which is far from every legal one-copy phase lift, because
then the unchanged rows can participate in long phase-displacement cycles
inside each necklace.

The fact that every `phi_(ij)` is nonzero adds a useful diversity bound.

### Corollary 3.3 (disjoint potential images)

In every zero-curl grid, put

\[
 A=\{a_i:i\in F_p\},
 \qquad E=\{e(D_j):j\in F_p\}.
\]

Then

\[
                         \boxed{A\cap E=\varnothing,
                         \qquad |A|+|E|\le p.}
\tag{3.6}
\]

In particular the grid is impossible if the added positive phases and
the deleted baseline phases together take more than `p` distinct values;
it is impossible if either side already takes all `p` values.

#### Proof

Equation (3.4) and `phi_(ij) ne0` say `a_i ne e(D_j)` for every pair.
Thus the two image sets are disjoint subsets of `F_p`. \(\square\)

## 4. Orthogonal wreath trades as colored medial grids

Assume the curl condition and shift the positive rows as in (3.3).  Label
their common physical support by

\[
                         S_{ij}
 =\sigma^{a_i}X_{ij}=\sigma^{e(D_j)}Y_{ij}.
\tag{4.1}
\]

For each fixed `i`, the cells `(S_(ij))_j` form one wreath; for each fixed
`j`, the cells `(S_(ij))_i` form another.  Thus the support has two
orthogonal wreath resolutions.

Every odd-graph edge `A--B` has a unique color

\[
                         c(A,B)=[p]\setminus(A\cup B).
\tag{4.2}
\]

The colors on every wreath `p`-cycle are all distinct, hence form a
permutation of `[p]`.  The union of the two resolutions is therefore a
four-regular, properly edge-colored graph on the `p^2` cells, decomposed
in two ways into `p` rainbow `p`-cycles.  It is the medial graph of
`K_(p,p)` equipped with cyclic orders at all `2p` vertices.

### Proposition 4.1 (exact alternating-window equations)

For every row `i`, choose its odd-cycle order and write its rainbow edge
colors cyclically as a permutation

\[
                         u_i(0),\ldots,u_i(p-1).
\]

For every column `j`, similarly write the colors as `v_j(0),...,v_j(p-1)`.
If cell `(i,j)` occurs at position `t=t_i(j)` in its row and
`s=s_j(i)` in its column, then

\[
 \boxed{
 S_{ij}
 =\{u_i(t-2),u_i(t-4),\ldots,u_i(t-2m)\}
 =\{v_j(s-2),v_j(s-4),\ldots,v_j(s-2m)\}.}
\tag{4.3}
\]

Conversely, permutations and positions satisfying (4.3), with all cells
distinct, construct two orthogonal wreath resolutions.

#### Proof

The standard reconstruction of a shortest odd cycle from its unique
unused edge colors gives exactly the first alternating expression; apply
the same reconstruction to the column cycle.  Conversely (4.3) makes
consecutive cells disjoint with the displayed unused color, so every row
and column is a shortest odd cycle and hence a wreath. \(\square\)

At each cell the two row-edge colors and the two column-edge colors are
four distinct members of `S_(ij)^c`.  Equality of a row and column edge
would put two cells in the same row and the same column, contradicting the
`K_(p,p)` overlay.  This endpoint condition is automatic in (4.3).

For `m=3`, the four colors exhaust `S_(ij)^c`, so the four-regular union
contains every odd-graph edge incident with its vertices.  Since `O_7` is
connected, the support would have to be all of `O_7`, impossible because
`p^2=49>binom(7,3)=35`.  For `m>=4`, the unused boundary degree is
`m-3`, and this local argument no longer excludes the grid.

The equations (4.3) are the exact coordinate-level successor gate.  The
abstract affine-plane counterexample of Theorem 32.1 supplies only the
incidence grid; it does not supply these simultaneous alternating-window
permutations.

There is a useful linear-algebraic shadow of (4.3).

### Theorem 4.2 (the bi-Smith slice condition)

Let `M(C)` be the `p by p` zero-one incidence matrix between the `p`
middle sets of one wreath `C` and the `p` coordinates.  Then

\[
 \boxed{
 \operatorname{SNF}M(C)=\operatorname{diag}(1,\ldots,1,m),
 \qquad |\det M(C)|=m.}
\tag{4.4}
\]

Consequently, if

\[
                         T(i,j,x)=\mathbf1_{\{x\in S_{ij}\}}
\tag{4.5}
\]

is the binary incidence tensor of an orthogonal wreath trade, then every
one of its `p` horizontal slices `(T(i,j,x))_(j,x)` and every one of its
`p` vertical slices `(T(i,j,x))_(i,x)` has Smith form
`diag(1,...,1,m)`.

#### Proof

Order the coordinates cyclically in the defining order of the wreath and
order its sets by their interval starts.  The incidence matrix is the
circulant matrix with row polynomial

\[
                         f(X)=1+X+\cdots+X^{m-1}.
\tag{4.6}
\]

Its eigenvalue at one is `m`.  At every nontrivial `p`-th root `omega`,

\[
                         f(\omega^k)
 ={1-\omega^{km}\over1-\omega^k}.
\]

Multiplication by `m` permutes the nonzero residues modulo `p`, so the
product of these `p-1` ratios is one.  Hence the determinant has absolute
value `m`.

For the full Smith form, subtract consecutive interval rows.  The
differences are `e_(j+m)-e_j`; because `m` is invertible modulo `p`, these
generate the full sum-zero lattice in `Z^p`.  The only remaining cokernel
is the constant quotient, on which the row sum is `m`.  Thus the cokernel
is `Z/mZ`, proving (4.4).  Row and coordinate reorderings change only
unimodular factors. \(\square\)

In particular, over every field whose characteristic does not divide
`m`, all `2p` slices are invertible; in a characteristic dividing `m`,
each has nullity exactly one.  This bi-Smith condition is a strictly
coordinate-level test for a proposed affine grid.  It is not presently
known whether it alone forbids a `p by p by p` tensor for general `m`.

The degree-two shadow has an equally explicit metric form.  If `pi` is a
cyclic coordinate order and `d_pi(x,y) in {1,...,m}` is the shorter cyclic
distance between two coordinates, then exactly

\[
                         m-d_\pi(x,y)
\tag{4.7}
\]

middle intervals of `pi` contain both `x` and `y`.  Therefore the row
orders `pi_i` and column orders `rho_j` of every orthogonal trade satisfy

\[
 \boxed{
 \sum_i d_{\pi_i}(x,y)=\sum_j d_{\rho_j}(x,y)
 \quad\hbox{for every }x\ne y.}
\tag{4.8}
\]

This equality of aggregate circular-distance matrices is another
checkable harmonic obstruction.  It is necessary rather than sufficient:
it records only the degree-two shadow of the common physical support.

## 5. A voltage-coboundary criterion

The quotient odd graph for `sigma` has at most one disjointness voltage
between two distinct necklace classes.  This turns the column wreaths into
an exact system of additive constraints.

Fix proposed cyclic orders of the row indices in every column.  Whenever
`i` and `i'` are consecutive in column `j`, let

\[
 \delta_j(i,i')\in F_p
\tag{5.1}
\]

be the unique voltage for which

\[
                         X_{ij}\cap
 \sigma^{\delta_j(i,i')}X_{i'j}=\varnothing.
\tag{5.2}
\]

If no such voltage exists, that column order is impossible.

### Theorem 5.1 (simultaneous voltage integrability)

An orthogonal trade obtained by one constant shift `a_i` of each positive
row can use the proposed column orders only if

\[
                         \boxed{
 \delta_j(i,i')=a_{i'}-a_i}
\tag{5.3}
\]

on every oriented column edge.  Equivalently, the voltage sum is zero on
every cycle of the union of the `p` column Hamilton cycles.

Conversely, if all required quotient edges exist and their labels form the
coboundary (5.3), then the shifted cells have every required column
odd-graph edge.  The column orders are therefore wreaths.

#### Proof

After shifting rows, the two cells are disjoint exactly when

\[
 X_{ij}\cap\sigma^{a_{i'}-a_i}X_{i'j}=\varnothing.
\]

Unique-voltage quotient edges identify this difference with (5.1).
A labeling is a vertex-potential difference precisely when all cycle sums
vanish.  The converse follows by reversing the same calculation. \(\square\)

Hence a single nonzero voltage circulation in the union of the proposed
column cycles excludes the trade.  This is stronger than necklace
pair-codegree one and is intrinsic to the coordinate cycle.

## 6. A checkable cross-edge exclusion

For shifted positive rows `A_i=sigma^(a_i)C_i`, let `E_cross` be the set of
odd-graph edges whose endpoints lie in two different packets `A_i,A_i'`.

### Proposition 6.1

Every orthogonal wreath trade satisfies

\[
                         \boxed{|E_{cross}|\ge p^2.}
\tag{6.1}
\]

Indeed its `p` column wreaths consist of `p` edges each, all joining
different row packets.  Consequently a family of shifted positive rows
whose induced odd graph has fewer than `p^2` cross-packet edges cannot be
the positive side of an affine-grid trade.

This gives a direct clean-interaction criterion.  Unlike the one-row
anomaly theorem, it is a condition on a `p`-row family; no current average
bound proves it uniformly over all such families.

## 7. Exact remaining status

The affine `K_(p,p)` count circuit has now been reduced as follows.

1. Any move supported relative to the original factor requires the phase
   differences to be constant along every positive row.
2. Relative to an arbitrary legal phase lift, the phase matrix must be
   additively separable, equivalently have zero `2 by 2` curl.
3. After that reduction, the problem is an orthogonal pair of wreath
   resolutions of `p^2` physical middle sets, satisfying the alternating
   equations (4.3).
4. Its quotient disjointness voltages must form one global coboundary, and
   its induced odd graph must contain at least `p^2` cross-packet edges.

These are rigorous coordinate-specific obstructions absent from the
abstract affine-plane example.  They do not yet prove that every such grid
is impossible for general `m`.  Nor is an actual wreath-compatible model
currently constructed.  The sharp remaining theorem is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{exclude a zero-curl bi-wreath Latin array satisfying (4.3),}\\
 \text{or construct one and determine whether it embeds in an exact factor.}
 \end{gathered}}
\]

Vertex harmonics cannot settle this last gate because the two resolutions
cover the same support.  The live tools are the phase curls, voltage
circulations, rainbow edge colors, and the simultaneous alternating-window
permutation equations.

## 8. Odd-graph girth alone cannot exclude the medial grid

A four-cycle in the medial graph is a rectangle `(i,i';j,j')` for which
`j,j'` are consecutive in both row rotations `i,i'` and `i,i'` are
consecutive in both column rotations `j,j'`.  The odd graph has no
four-cycle, so an actual bi-wreath grid must avoid every such rectangle.
This avoidance is nevertheless compatible with the abstract rotation
system.

### Theorem 8.1 (four-cycle-free medial rotations exist)

For all sufficiently large odd `p`, there are cyclic orders of the `p`
incident cells at every vertex of `K_(p,p)` whose medial graph has no
four-cycle.

#### Proof

Choose the `2p` cyclic orders independently and uniformly.  For each
choice of two row vertices and two column vertices, let `E` be the event
that the corresponding rectangle is consecutive at all four vertices.
Two prescribed incident edges are adjacent in a uniform cyclic order with
probability `2/(p-1)`, so

\[
                         \Pr(E)=\left({2\over p-1}\right)^4.
\tag{8.1}
\]

The event depends only on the four cyclic orders at its rectangle
vertices.  It is independent of every rectangle using neither of its row
vertices and neither of its column vertices.  A crude dependency bound is

\[
                         D\le2p^3.
\tag{8.2}
\]

Thus

\[
 e\Pr(E)(D+1)=O(1/p)<1.
\]

The symmetric Lovasz local lemma gives a choice avoiding every event.
Such a choice has no medial four-cycle. \(\square\)

Therefore the no-four-cycle property used in Proposition 22.2 is a local
constraint, not a universal obstruction to an orthogonal rotation system.
The actual set equations (4.3) remain essential.

There is a topological consequence, but not a contradiction.  Regard the
row and column cyclic orders as an orientable rotation system of
`K_(p,p)`.  A four-face would give precisely a consecutive rectangle and
hence a medial four-cycle.  Thus every face has length at least six.  If
`f` is the number of faces and `g` the genus, then

\[
 6f\le2p^2,
 \qquad
 2-2g=2p-p^2+f,
\]

so every actual grid would satisfy

\[
                         \boxed{g\ge {p^2\over3}-p+1.}
\tag{8.3}
\]

The LLL construction shows that quadratic genus is combinatorially
available; (8.3) is a useful normal form rather than a no-go.

## 9. Slice determinants are compatible; injectivity is the missing part

Let `H` be any cyclic interval of size `m` in `F_p`, and define

\[
                         S_{ij}=H+i+j.
\tag{9.1}
\]

For every fixed `i`, the `p` cells `(S_(ij))_j` are the translate wreath
of `H`; for every fixed `j`, the `p` cells `(S_(ij))_i` are the same kind
of wreath.  Consequently the tensor

\[
                         T(i,j,x)=\mathbf1_{\{x\in H+i+j\}}
\tag{9.2}
\]

satisfies every horizontal and vertical Smith/determinant condition of
Theorem 4.2 and every circular-distance identity of (4.8).

It is not an affine grid because `S_(ij)` depends only on `i+j`: there are
only `p` distinct cells rather than `p^2`.  Hence:

\[
 \boxed{
 \text{the bi-Smith and distance conditions are jointly consistent;}\quad
 \text{global cell injectivity is indispensable}.}
\tag{9.3}
\]

The same degeneration afflicts the most natural two-group construction.

### Proposition 9.1 (double cyclic orbits always repeat a column packet)

Let `g,h` be coordinate `p`-cycles and suppose

\[
                         S_{ij}=g^ih^jS_0.
\tag{9.4}
\]

Assume every column in (9.4) is a wreath packet.  Then every column is a
`g`-invariant wreath.  There are only

\[
                         m={p-1\over2}
\tag{9.5}
\]

such packets: the arithmetic-progression wreaths whose steps are identified
up to sign.  Since there are `p` columns, two columns have the same physical
support.  Thus the `p^2` cells are not distinct, and no injective bi-wreath
grid can arise from a separable double orbit of two coordinate cycles.

#### Proof

The classification of coordinate-cycle-invariant wreaths gives exactly
the `m` AP packets.  Pigeonhole completes the proof. \(\square\)

Accordingly an actual model, if it exists, must use genuinely
row-dependent and column-dependent cyclic orders.  Neither a pair of
global cyclic group actions nor determinant compatibility can construct
it.

## 10. Prime volume excludes fixed-seed phase suspensions

The known balanced-shuffle and one-sided phase-lift constructions have a
simple row-count obstruction at the minimal grid volume.

### Proposition 10.1

Let a cancellation-free seed trade on `q` coordinates contain `t` wreath
rows on each sign.  Developing every seed row through all `q` base phases,
as in a one-sided shuffle lift, produces exactly

\[
                         tq
\tag{10.1}
\]

rows on each sign, independently of the ambient context size.  If the
ambient affine-grid target has prime side size `p`, equality `tq=p` forces

\[
                         (t,q)=(1,p)\quad\hbox{or}\quad(p,1).
\tag{10.2}
\]

Hence no nontrivial proper fixed seed can produce a `p`-row orthogonal
wreath trade by the existing full-phase suspension mechanism.

#### Proof

Every one of the `t` seed rows gives one distinct product row for each of
its `q` cyclic base phases.  Cancellation-free development therefore has
the product count (10.1).  Primality gives (10.2). \(\square\)

For example, the `Q_7` three-row circuit develops to `21` rows per sign;
balanced shuffling changes the ambient dimension but never this row count.
Thus it cannot directly realize the prime-size affine grid.  A construction
would need cancellations, interactions among growing seeds, or an
intrinsically `p`-dimensional design.

## 11. Balanced rainbow gain-graph formulation

On the transversal core, form the **row collision graph**: its vertices
are factor rows, and two rows are joined when they meet one common
`sigma`-necklace.  Pair codegree one makes this graph simple.  Color the
edge by its common necklace.  If

\[
 X\in C\cap O,
 \qquad Y\in D\cap O,
 \qquad Y=\sigma^{\phi(C,D)}X,
\]

orient the edge `C->D` with gain `phi(C,D) in F_p`; reversing orientation
negates the gain.

### Theorem 11.1 (the exact gain-graph gate)

The frequency-zero affine circuit is precisely a bipartite subgraph

\[
                         K_{p,p}=G[P,N]
\tag{11.1}
\]

whose `p^2` edges have distinct necklace colors.  A relative supported
phase move exists precisely when this gain graph is **balanced**, meaning
that the oriented gain sum around every cycle is zero.

For `K_(p,p)`, the following are equivalent:

1. every cycle has zero gain;
2. every four-cycle has zero gain;
3. the gain matrix has zero additive `2 by 2` curl;
4. there are vertex potentials `a_i,b_j` with
   `phi_(ij)=a_i-b_j`;
5. after switching by those vertex potentials, every edge has gain zero.

Under this switching, the two row shores become two physical wreath
factorizations of the same `p^2` middle sets.  They form an actual affine
grid exactly when the switched cells also satisfy the alternating-window
equations (4.3).

#### Proof

The rainbow `K_(p,p)` statement is Theorem 32.3.  The equivalence of
items 1--5 is the standard spanning-tree integration argument for an
abelian gain graph: fix one vertex potential, integrate gains along a
spanning tree, and use cycle sums for path independence.  In a complete
bipartite graph its cycle space is generated by four-cycles, giving item
2.  The physical switching assertion is Corollary 3.2. \(\square\)

Thus the sharp coordinate-specific exclusion theorem can be stated
compactly:

\[
 \boxed{
 \text{the necklace-colored row collision gain graph contains no balanced
 rainbow }K_{p,p}\text{ satisfying (4.3)}.}
\tag{11.2}
\]

The abstract affine-plane matrix from Theorem 32.1 supplies the unlabelled
rainbow `K_(p,p)` but has neither the coordinate gains nor the bi-wreath
alternating-window structure.  This identifies exactly what additional
geometry a maximal-rank proof must exploit.

## 12. The endpoint inverse and the signed-frame normal form

The Smith calculation in Theorem 4.2 has an exact integral refinement.
It is substantially stronger than the statement that the determinant has
absolute value `m`.

Let `C=(A_s:s in F_p)` be a wreath, listed in its odd-cycle order, and let

\[
 e_s=\{c(A_{s-1},A_s),c(A_s,A_{s+1})\}
\tag{12.1}
\]

be the two edge colors incident with `A_s`.  Let `M_C` be the cell by
coordinate incidence matrix and let `E_C` be the cell by coordinate
incidence matrix of the endpoint pairs `(e_s)`.

### Theorem 12.1 (endpoint inverse formula)

One has

\[
 \boxed{|A_t\cap e_s|=1-\mathbf1_{\{s=t\}},}
\tag{12.2}
\]

and consequently

\[
 \boxed{M_CE_C^{\mathsf T}=J-I,
 \qquad
 M_C^{-1}={1\over m}J-E_C^{\mathsf T}.}
\tag{12.3}
\]

In particular `m M_C^{-1}` has the entry `1` except at the two endpoint
positions in each column, where its entry is `1-m=-(m-1)`.  Thus the full
adjugate, not merely its determinant, is determined by the endpoint-color
cycle.

#### Proof

Use the alternating reconstruction (4.3).  The two colors incident with
`A_s` are absent from `A_s`.  Starting from `A_s` and moving to any other
cell of the odd cycle alternately inserts one of those two colors and
deletes the other, so every other cell contains exactly one of them.  This
is (12.2), hence the first identity in (12.3).  Since every row of `M_C`
has sum `m`,

\[
 M_C(J-mE_C^{\mathsf T})
 =mJ-m(J-I)=mI.
\]

Division by `m` proves the inverse formula. \(\square\)

The formula gives integral coordinates for every middle set relative to
every wreath basis.

### Corollary 12.2 (signed endpoint coordinates)

For an arbitrary `m`-set `A`, define

\[
 \kappa_C(A)_s=1-|A\cap e_s|.
\tag{12.4}
\]

Then

\[
 \boxed{
 \kappa_C(A)\in\{-1,0,1\}^p,
 \qquad \sum_s\kappa_C(A)_s=1,
 \qquad
 \mathbf1_A=\sum_s\kappa_C(A)_s\mathbf1_{A_s}.}
\tag{12.5}
\]

Moreover `kappa_C(A)` is a unit vector if and only if `A` is a cell of
`C`.  If `A` is not a cell of `C`, then it has at least one `-1` entry and
at least two `+1` entries; in fact

\[
 \#\{s:\kappa_C(A)_s=1\}
 =\#\{s:\kappa_C(A)_s=-1\}+1.
\tag{12.6}
\]

#### Proof

Multiplying the incidence row of `A` by (12.3) gives exactly (12.4) and
the expansion in (12.5).  The endpoint pairs `(e_s)` are the edges of a
coordinate `p`-cycle.  In the binary cyclic word of `A` on this cycle,
the entries `+1,0,-1` mark respectively `00,01/10,11` edges.  Since the
word has `m+1` zeroes and `m` ones, the number of `00` edges exceeds the
number of `11` edges by one, proving (12.6).  There is no `11` edge
precisely when the ones form a maximum independent set of the odd cycle;
the `p` such independent sets are exactly the cells `(A_s)`. \(\square\)

Now let `C,D` be two wreaths, with arbitrary cyclic orderings of their
cells, and put

\[
                         K(D,C)=M_DM_C^{-1}.
\tag{12.7}
\]

### Corollary 12.3 (bi-unimodular transition matrices)

Every wreath transition matrix satisfies

\[
 \boxed{
 K(D,C)\in\operatorname{GL}_p(\mathbb Z),
 \quad K(D,C),K(D,C)^{-1}\in\{-1,0,1\}^{p\times p},
 \quad K\mathbf1=\mathbf1,
 \quad \mathbf1^{\mathsf T}K=\mathbf1^{\mathsf T}.}
\tag{12.8}
\]

Its rows are the signed endpoint-coordinate vectors
`kappa_C(A)` for `A in D`, its determinant is `+-1`, and its unit rows
are in bijection with the physical cells common to `C` and `D`.

#### Proof

The row description follows from Corollary 12.2.  Reversing `C,D` gives
the same assertion for the inverse.  Both wreath incidence determinants
have absolute value `m`, so the determinant ratio is `+-1`.  Row sums are
(12.5).  Finally

\[
 \mathbf1^{\mathsf T}K M_C
 =\mathbf1^{\mathsf T}M_D
 =m\mathbf1^{\mathsf T}
 =\mathbf1^{\mathsf T}M_C,
\]

and invertibility of `M_C` gives the column sums.  Uniqueness of
coordinates gives the unit-row statement. \(\square\)

There is a useful conceptual reason that every transition is integral.

### Corollary 12.3a (all wreaths are bases of one lattice)

Every wreath incidence basis generates the same index-`m` lattice

\[
 \boxed{
 \mathcal L_m=
 \{z\in\mathbb Z^p:\ \sum_xz_x\equiv0\pmod m\}.}
\tag{12.8a}
\]

#### Proof

Consecutive cell differences of a wreath are coordinate differences
`e_x-e_y`; because the cyclic step is invertible modulo `p`, these
differences generate the full sum-zero lattice.  Adding any one cell,
whose coordinate sum is `m`, gives exactly the lattice in (12.8a).
Its index is `m`, agreeing with Theorem 4.2. \(\square\)

Thus the abstract shadow of an orthogonal wreath grid is a double basis
array of one fixed lattice.  In the equality case, reduction modulo two
in anchor coordinates gives `p` unit vectors on the anchor row and
`p(p-1)` weight-three vectors, with every horizontal and vertical slice
a basis of `F_2^p`.  The row and column XOR identities are consistent;
the nontrivial information is which weight-three vectors arise from
cyclic endpoint patterns and whether their slice bases are wreath bases.

This yields a normalized form of the whole affine-grid gate.  Fix one
horizontal wreath `C_0` as an anchor and order its cells by the column
labels.  For every horizontal wreath and every vertical wreath define

\[
 L_i=M_{C_i}M_{C_0}^{-1},
 \qquad
 K_j=M_{D_j}M_{C_0}^{-1}.
\tag{12.9}
\]

### Theorem 12.4 (signed-frame tensor normal form)

An orthogonal wreath grid gives a tensor

\[
 \kappa(i,j,s)=1-|S_{ij}\cap e_s(C_0)|
 \quad\in\{-1,0,1\}
\tag{12.10}
\]

with all of the following properties.

1. The horizontal slice `(kappa(i,j,s))_(j,s)` is `L_i` and the vertical
   slice `(kappa(i,j,s))_(i,s)` is `K_j`.
2. Every one of these `2p` slices is bi-unimodular as in (12.8).
3. `L_0=I`.  For `i ne0`, `L_i` has no unit row.  Each `K_j` has exactly
   one unit row, namely the row of the common cell `S_(0j)`, and that row
   is the unit vector `e_j`.
4. If `nu_-(A)` denotes the number of negative entries, then

   \[
    \boxed{
    \sum_{i\ne0}\nu_-(L_i)
    =\sum_j\nu_-(K_j)
    \ge p(p-1).}
   \tag{12.11}
   \]

   Equality holds only if every non-anchor cell contains both colors of
   exactly one anchor endpoint pair and avoids both colors of exactly two
   anchor endpoint pairs.

#### Proof

Only the last assertion needs comment.  Every nonunit row in a signed
coordinate matrix has at least one negative entry by Corollary 12.2.
There are exactly `p(p-1)` non-anchor cells.  The two sums count the same
negative entries of the tensor, first by horizontal slices and then by
vertical slices.  Equality and (12.6) give the stated endpoint pattern.
\(\square\)

Theorem 12.4 is stronger than the bi-Smith condition: it retains the
entire adjugate and turns realizability into a simultaneous
`{-1,0,1}`-unimodular-frame problem.  It also cleanly separates the two
possibilities left by the size-`2p` rigidity theorem:

\[
 \boxed{
 \begin{gathered}
 \text{either no tensor (12.10) with the alternating-window origin exists,}\
 \text{or such a tensor is an explicit volume-`p` wreath trade and hence}\
 \text{an actual witness that the minimal modular count circuit is mobile.}
 \end{gathered}}
\tag{12.12}
\]

In particular, determinant or Smith compatibility alone has now been
exhausted: the smallest remaining exact theorem is the realizability (or
nonrealizability) of the endpoint signed-frame tensor in Theorem 12.4,
with the additional global `sigma`-necklace transversality and zero-gain
conditions from Sections 1 and 11.

### Corollary 12.5 (circular metric defect formula)

The endpoint pairs `(e_s(C))` form a coordinate `p`-cycle; call it
`E_C`.  For another wreath `D`, let `d_D(e_s)` be the smaller circular
distance, in the coordinate order of `D`, between the two colors of
`e_s`.  Then

\[
 \boxed{
 \nu_-\bigl(K(D,C)\bigr)
 =\sum_{s\in\mathbb F_p}\bigl(m-d_D(e_s)\bigr)
 =pm-\operatorname{len}_D(E_C),}                            \tag{12.13}
\]

where `len_D(E_C)=sum_s d_D(e_s)` is the length of the anchor endpoint
Hamilton cycle in the circular metric induced by `D`.

In particular, if `D` has no physical cell in common with `C`, then

\[
                         \operatorname{len}_D(E_C)\le p(m-1), \tag{12.14}
\]

and equality holds exactly when every cell of `D` contains both colors of
one and only one anchor endpoint pair.

#### Proof

Two coordinates at circular distance `d<=m` in the order of `D` occur
together in exactly `m-d` of the `m`-windows of `D`.  Corollary 12.2 says
that a negative entry in column `s` of `K(D,C)` is exactly a cell of `D`
containing both colors of `e_s`.  Summing first over cells and then over
endpoint pairs proves (12.13).  If the wreaths have no common cell, every
row of the transition matrix is nonunit and hence has at least one
negative entry, giving `nu_- >= p` and (12.14).  Equality is the equality
case of Corollary 12.2 row by row. \(\square\)

Thus equality in the global tensor bound (12.11) is a simultaneous
second-extremal traveling-salesman problem: relative to the anchor metric,
every non-anchor horizontal packet has tour length exactly `p(m-1)`.
Classifying these equality tours and imposing the vertical wreath
conditions is a concrete possible route to showing that equality forces a
repeated-cell/multiplier degeneration.

### Lemma 12.6 (exact parity of a minimal signed row)

Index the anchor endpoint edges cyclically.  Suppose a nonanchor cell has
exactly one negative coordinate `r` and two positive coordinates `s,t`.
Choose the cyclic order of the two positive coordinates so that the three
successive positive gap lengths are

\[
                         d(r,s),\quad d(s,t),\quad d(t,r).
\]

Then, after possibly interchanging `s,t`,

\[
 \boxed{
 d(r,s)\equiv0,qquad d(s,t)\equiv1,qquad
 d(t,r)\equiv0\pmod2.}                                    \tag{12.15}
\]

Conversely every ordered triple of distinct endpoint edges satisfying
(12.15) is realized by a unique cyclic binary word with `m` ones, whose
unique `11` edge is `r` and whose two `00` edges are `s,t`.

#### Proof

Immediately after the `11` edge `r` the bit is one.  All edges before the
next defect edge `s` are transitions, while the bit at the start of the
`00` edge `s` is zero.  Hence the number `d(r,s)-1` of intervening
transition edges is odd, so `d(r,s)` is even.  From the end of `s` to the
start of the next `00` edge `t`, the bit begins and ends at zero; therefore
`d(s,t)-1` is even and `d(s,t)` is odd.  Finally the bit changes from zero
after `t` to one before `r`, giving `d(t,r)` even.  The three gaps sum to
the odd number `p`, as required.

Conversely assign `11` at `r`, `00` at `s,t`, and alternate on every
other edge.  The parity conditions make the assignments agree when the
three arcs are joined.  The resulting cyclic word has one more `00` than
`11`, hence `m+1` zeroes and `m` ones, and uniqueness is immediate.
\(\square\)

Modulo two, a minimal nonunit signed row is therefore a feasible weight-
three vector subject to (12.15), not an arbitrary weight-three vector.
Equivalently, among its three cyclic gaps exactly one is odd, and the
distinguished negative coordinate is the endpoint-edge index incident
with the two even gaps.  This is the first coordinate restriction beyond
the bare double-basis equations.

## 13. Alternating-window slices do not force additive separability

The degenerate tensor (9.1) can be made genuinely nonseparable.  Thus no
argument using only the assertion that every horizontal and vertical slice
is a wreath can prove the desired cocycle rigidity.

### Proposition 13.1 (nonlinear Latin wreath degeneration)

Let `H` be one cyclic `m`-interval in `F_p`, let `gamma:F_p->F_p` be any
non-affine permutation, and put

\[
                         L(i,j)=\gamma(i+j),
 \qquad
                         S_{ij}=H+L(i,j).
\tag{13.1}
\]

Then every horizontal slice and every vertical slice of `(S_(ij))` is a
genuine wreath packet, with all `p` members occurring once.  Nevertheless
the scalar array `L` has a nonzero additive `2 by 2` curl, so it cannot be
written

\[
                         L(i,j)=f(i)+g(j).
\tag{13.2}
\]

The construction has exactly `p`, rather than `p^2`, distinct physical
cells.

#### Proof

For fixed `i` or fixed `j`, the map in the other variable is a permutation
of `F_p`.  Hence the corresponding sets in (13.1) are precisely all
translates of `H`, which form one wreath packet.

If every additive `2 by 2` curl of `L` vanished, then `L` would have the
form (13.2).  Comparing the row and column through zero would give

\[
 \gamma(i+j)=\gamma(i)+\gamma(j)-\gamma(0)
 \qquad(i,j\in F_p).
\tag{13.3}
\]

Thus `gamma-gamma(0)` would be an additive endomorphism of `F_p`, and
`gamma` would be affine, contrary to hypothesis.  Finally (13.1) depends
only on the `p` possible values of `L`. \(\square\)

For every prime `p>=5`, one may take for `gamma` the transposition of zero
and one fixing every other element; it is non-affine because it has at
least three fixed points but is not the identity.

Therefore the logical boundary is now exact:

\[
 \boxed{
 \begin{gathered}
 \text{wreath slices + alternating-window equations + bi-Smith data}\
 \text{do not imply additive separability;}\\
 \text{the unresolved input is simultaneous }p^2\text{-cell injectivity,}\
 \text{distinct }\sigma\text{-necklace classes, and the balanced gain law.}
 \end{gathered}}
\tag{13.4}
\]

## 14. Equality in the signed-frame bound is not multiplier-rigid

Corollary 12.5 turns equality into a circular traveling-salesman problem.
The equality tours admit an exact interval formulation.

### Proposition 14.1 (one-edge-per-window classification)

Let `C,D` be physically disjoint wreaths.  Regard the endpoint pairs of
`C` as the edges of a Hamilton cycle `Gamma=E_C` on the coordinate set,
and regard the coordinate order of `D` as another cycle `Delta`.  The
following are equivalent.

1. `nu_-(K(D,C))=p`.
2. Every cell of `D` contains exactly one edge of `Gamma`.
3. Every `m`-vertex cyclic interval of `Delta` spans exactly one edge of
   `Gamma`.
4. For every edge `e` of `Gamma`, let `B_e` be the set of starts of the
   `m`-intervals of `Delta` containing both ends of `e`.  Then the
   nonempty cyclic intervals `(B_e)` partition `F_p`.
5. `len_D(Gamma)=p(m-1)`.

#### Proof

The equivalence of 1, 2 and 5 is Corollary 12.5 and the fact that each of
the `p` nonunit rows has at least one negative entry.  Statements 2 and 3
are the same assertion in the two languages.  Finally an edge whose ends
have shorter `Delta`-distance `d` lies in exactly `m-d` consecutive
`m`-windows.  Therefore the number of `Gamma`-edges in a window is the
number of blocks `B_e` covering its start.  It is identically one exactly
when those blocks partition the start cycle. \(\square\)

It is tempting to conjecture that equality forces every edge of `Gamma`
to have `Delta`-distance `m-1`, which would give the constant-multiplier
tour.  That conjecture is false in every relevant prime order.

### Theorem 14.2 (nonconstant second-extremal wreath pairs)

For every prime `p=2m+1>=7`, there are physically disjoint wreaths `C,D`
such that

\[
                         \nu_-(K(D,C))=p,
\tag{14.1}
\]

but the endpoint cycle `E_C` has, in the coordinate order of `D`, edges
of three different lengths `m-2,m-1,m`.  In particular equality in
(12.14) does not force an arithmetic-progression/multiplier relation.

#### Proof

Identify the coordinate order of `D` with `F_p` in its natural cyclic
order and put

\[
                         d=m-1.
\tag{14.2}
\]

The chord graph

\[
                         \Gamma_0=\{\{x,x+d\}:x\in F_p\}
\tag{14.3}
\]

is a Hamilton cycle because `d ne0` and `p` is prime.  Every edge in
(14.3) has distance `m-1` and is contained in one `m`-window, namely the
window starting at `x`.  Hence every `m`-window contains one edge of
`Gamma_0`.

For any `a`, replace the two edges

\[
 \{a,a+d\},\qquad\{a+1,a+1+d\}
\]

by

\[
 \{a,a+1+d\},\qquad\{a+1,a+d\}.
\tag{14.4}
\]

The first new edge has distance `m` and lies in no `m`-window; the second
has distance `m-2` and lies in exactly the two windows starting at `a`
and `a+1`.  Thus (14.4) preserves, pointwise, the assertion that every
window contains one edge.  As a directed successor permutation, the
change replaces `f(x)=x+d` by `f tau_(a,a+1)`.  It splits the Hamilton
cycle into two cycles.

Take `a=0`.  If `r=d^(-1) mod p`, one of the two cycle vertex sets after
the split is

\[
                         B=\{d,2d,\ldots,rd=1\}.
\tag{14.5}
\]

Here

\[
 r={p-2\over3}\quad(p\equiv2\pmod3),
 \qquad
 r={2p-2\over3}\quad(p\equiv1\pmod3),
\tag{14.6}
\]

so `3<=r<=p-3`.  Along the natural coordinate cycle there is therefore a
boundary pair `b,b+1` between `B` and its complement which is disjoint
from `{0,1}`.  Indeed, otherwise membership in `B` could change only on
the three natural edges incident with `{0,1}`, forcing `|B|<=2` or
`|B|>=p-2`.

Apply (14.4) also at this `b`.  The second transposition has one endpoint
in each of the two successor cycles, so multiplication by it joins those
cycles back into one Hamilton cycle `Gamma`.  The two switches have
disjoint supports and each preserves the one-edge-per-window identity.
Consequently every `D`-cell contains exactly one `Gamma`-edge.

There is a unique wreath `C` whose cyclic edge-color order is `Gamma`.
Its cells are the maximum independent sets of `Gamma`, whereas every
`D`-cell contains one `Gamma`-edge.  Thus `C,D` are physically disjoint,
and Proposition 14.1 gives (14.1).  The switched edges exhibit all three
lengths `m-2,m-1,m`. \(\square\)

For `p=7`, a concrete endpoint order is

\[
                         (0,1,3,6,2,4,5),
\tag{14.7}
\]

against the natural `D`-order `(0,1,2,3,4,5,6)`.  Its successive shorter
edge lengths are `1,2,3,3,2,1,2`, and every three-window contains exactly
one displayed edge.

The theorem gives a sharp verdict on the equality lane:

\[
 \boxed{
 \text{minimal endpoint defect is abundant already for a pair of wreaths;}\
 \text{only simultaneous vertical reassembly, necklace transversality,}\
 \text{or gain compatibility can still force repetition/separability.}}
\tag{14.8}
\]

The vertical slices in Theorem 12.4 have one unit row rather than none.
Their corresponding equality case is also realizable for every `m`.

### Theorem 14.3 (one-common-cell equality pairs)

For every `m>=3`, `p=2m+1`, there are two wreaths `C,D` which have exactly
one physical cell in common and satisfy

\[
                         \nu_-(K(D,C))=p-1.
\tag{14.9}
\]

Equivalently, the common cell has endpoint defect zero relative to `C`
and every other cell of `D` has endpoint defect one.

#### Proof

Write the endpoint-color cycle of `C` as

\[
 b_0,a_1,b_1,a_2,b_2,\ldots,a_m,b_m,b_0.
\tag{14.10}
\]

Then

\[
                         A=\{a_1,\ldots,a_m\}
\tag{14.11}
\]

is one cell of `C`: it is a maximum independent set of the endpoint
cycle.  Define `D` by the following cyclic coordinate order:

\[
 \boxed{
 a_1,a_2,\ldots,a_m,
 b_1,b_m,b_2,b_3,\ldots,b_{m-2},b_0,b_{m-1}.}
\tag{14.12}
\]

For `m=3`, the middle string in (14.12) is empty, so the `b`-order is
`b_1,b_3,b_0,b_2`.

The first `m`-window is `A` and spans no endpoint-cycle edge.  We check
the remaining windows.

* While the window loses `a_1,a_2,...` and gains the initial `b`'s, the
  unique edge is first `b_1a_2`, then `b_ma_m`; the subsequently inserted
  `b_2,b_3,...,b_(m-2)` have both `a`-neighbours already deleted.  When
  `b_0` enters and no `a` remains, the unique edge is `b_0b_m`.
* The two all-`b` windows both contain `b_0,b_m`, because the first and
  last entries of the displayed `b`-order are the interior vertices
  `b_1,b_(m-1)`.  Thus their unique edge is again `b_0b_m`.
* On wrapping back into the `a`-block, deletion of `b_1,b_m,b_2,...`
  leaves `b_0a_1` as the unique edge.  At the last step `b_0` is deleted
  and only `b_(m-1)` remains; its unique edge is `b_(m-1)a_(m-1)`.

Hence every `D`-cell other than `A` contains exactly one endpoint edge.
The cells of `C` are precisely the maximum independent sets of that odd
cycle, so none of those other cells belongs to `C`.  The signed-coordinate
description now gives one unit row and `p-1` rows with one negative entry,
which is (14.9). \(\square\)

Thus even the complete equality pattern of an individual vertical slice
in Theorem 12.4 is genuine wreath geometry.  The unresolved equality
question is irreducibly simultaneous:

\[
 \boxed{
 \text{can }p\text{ one-common-cell equality wreaths, one through each}\
 \text{anchor cell, be made mutually disjoint and have their remaining}\
 \text{cells repartition into }p-1\text{ disjoint equality wreaths?}}
\tag{14.13}
\]

This is the smallest exact equality-case realizability theorem left by
the size-`2p` packet rigidity and the signed-frame reduction.

There is, however, a clean obstruction to the most natural way of turning
one equality pair into all `p` columns.

### Theorem 14.4 (cyclic development of an equality column degenerates)

Let `tau` rotate the anchor endpoint cycle `E_C`.  Let `D` be a
one-common-cell equality wreath as in Theorem 14.3 and attempt to form the
vertical packets

\[
                         D_j=\tau^jD
 \qquad(j\in F_p).
\tag{14.14}
\]

If two cells of `D` lie in the same `tau`-necklace, then the developed
array repeats a physical cell.  If `D` is transversal, the `p` phase
orbits of its cells are distinct; but at most one of the non-anchor phase
orbits can be a wreath packet.  Consequently no injective orthogonal
equality grid can be obtained by cyclically developing one column and
using its cell phase-orbits as the horizontal packets.

#### Proof

The first assertion is immediate.  For the second, classify the
`tau`-invariant wreath packets.  They are the arithmetic-progression
packets with a step `c`, identified up to sign.  In the cyclic coordinate
order with step `c`, an edge of the anchor endpoint cycle has shorter
distance

\[
                         d(c)=\min(c^{-1},-c^{-1})\in\{1,\ldots,m\}.
\tag{14.15}
\]

Every cell of that invariant packet therefore contains exactly

\[
                         m-d(c)
\tag{14.16}
\]

anchor endpoint edges.  Endpoint defect one forces `d(c)=m-1`, which has
only the single solution

\[
                         c=\mathord\pm(m-1)^{-1}
\tag{14.17}
\]

up to the sign identification.  Thus there is exactly one
`tau`-invariant defect-one wreath packet.

In a transversal development (14.14), the orbit of the common cell is
the anchor packet and each of the other `p-1` cell orbits has endpoint
defect one.  If those orbits were the horizontal wreath packets, all
`p-1` would have to be the unique packet (14.17), so they would repeat
rather than partition the physical cells. \(\square\)

This closes the equality analogue of the double-global-orbit model in
Proposition 9.1.  It does not exclude a genuine grid with independently
chosen columns: such a grid must break cyclic development on both shores.

## 15. The feasible signed-triple hypergraph

The equality tensor has a completely explicit cell alphabet.  Index the
edges of the anchor endpoint cycle by `F_p` in cyclic order.  A non-anchor
cell has one negative coordinate and two positive coordinates:

\[
                         \kappa(A)=e_a+e_b-e_c.
\tag{15.1}
\]

Here `c` is the unique anchor edge contained in `A`, while `a,b` are the
two anchor edges having both endpoints outside `A`.

### Theorem 15.1 (exact feasible-triple criterion)

Order the two positive edges so that, starting from `c` and moving
clockwise, one encounters `a` and then `b`.  Put

\[
 r=a-c,qquad s=b-a,qquad t=p+c-b
\tag{15.2}
\]

as positive integer cyclic gaps, so `r+s+t=p`.  Then (15.1) is the signed
coordinate vector of an `m`-set if and only if

\[
                         \boxed{r,t\text{ are even and }s\text{ is odd}.}
\tag{15.3}
\]

For every feasible signed triple the corresponding `m`-set is unique.
Consequently the number of endpoint-defect-one `m`-sets is

\[
                         \boxed{p\binom m2={p,m(m-1)\over2}.}
\tag{15.4}
\]

#### Proof

Away from the three exceptional edges, (12.4) says that the membership
bits alternate.  At the negative edge both endpoint bits are one; at a
positive edge both are zero.  Starting with the terminal one of the
negative edge, reaching the first positive edge requires an odd number
of flips, so `r-1` is odd and `r` is even.  Between the positive edges one
must return from zero to zero, so `s-1` is even and `s` is odd.  Returning
from the second positive edge to the initial one at the negative edge
similarly makes `t` even.  These parity conditions also reconstruct the
binary word uniquely, proving sufficiency and uniqueness.

Write `r=2R`, `t=2T`, `s=2S+1`.  Then `R,T>=1`, `S>=0`, and
`R+T+S=m`.  There are `binom(m,2)` such triples for each choice of `c`,
which proves (15.4). \(\square\)

Thus the equality cells form a signed `3`-uniform cyclic hypergraph
`H_Gamma` on the `p` anchor edges.  Its negative degree is
`binom(m,2)` at every vertex, and its positive degree is `m(m-1)` at every
vertex.

The wreath condition orders selected hyperedges into much more than a
linear basis.

### Theorem 15.2 (consecutive-block law)

Let `D` be a wreath and, for an anchor edge `e_s`, put

\[
                         \delta_s=m-d_D(e_s).
\tag{15.5}
\]

In the cyclic order of the cells of `D`:

1. the cells whose signed triple has negative coordinate `s` form one
   consecutive block of length `delta_s`;
2. the cells whose signed triple has positive coordinate `s` form one
   consecutive block of length `delta_s+1`;
3. if `D` is disjoint from the anchor and is equality-extremal, the
   negative blocks partition all `p` cells and

   \[
                            \sum_s\delta_s=p;
   \tag{15.6}
   \]

4. if `D` shares one anchor cell `A_j` and is equality-extremal, the
   negative blocks partition the other `p-1` cells and

   \[
                            \sum_s\delta_s=p-1.
   \tag{15.7}
   \]

   After removal of the unit row `e_j`, the positive multiplicity of `s`
   is `delta_s+1-1_(s=j)`.

#### Proof

If the endpoints of `e_s` have shorter `D`-distance `d`, the `D`-windows
containing both form `m-d=delta_s` consecutive starts.  The windows
containing neither form `m+1-d=delta_s+1` consecutive starts.  These are
the negative and positive entries of (12.4).  Propositions 14.1 and 14.3
give the two partition statements and their total lengths.  The last
formula subtracts the single positive entry supplied by the common unit
row. \(\square\)

More precisely, up to a cyclic rotation, the entire `s`-th signed column
of the transition matrix has the four-block form

\[
 \boxed{
 +^{\,\delta_s+1}\;
 0^{\,d_D(e_s)}\;
 -^{\,\delta_s}\;
 0^{\,d_D(e_s)}.}
\tag{15.7a}
\]

The lengths add to
`(delta_s+1)+2d_D(e_s)+delta_s=2m+1=p`.  Thus the positive and negative
blocks are not independent interval data: their two separating zero
blocks have equal length.

Accordingly, in a simultaneous equality grid, writing

\[
 \kappa(i,j)=e_{a_{ij}}+e_{b_{ij}}-e_{c_{ij}}
 \qquad(i\ne0),
\tag{15.8}
\]

the following must hold at once.

* Every signed triple satisfies the even--odd--even cyclic gap rule
  (15.3), and all `p(p-1)` triples are distinct.
* In each non-anchor horizontal wreath, every negative color occurs in
  one consecutive block and the block lengths sum to `p`.
* In vertical column `j`, every negative color occurs in one consecutive
  block, the blocks sum to `p-1`, and the one uncovered cell is the unit
  `e_j`.
* Every horizontal and vertical signed incidence matrix is unimodular,
  and its inverse is again a feasible signed endpoint-coordinate matrix.

This is strictly stronger than a degree-balanced 3-uniform design or a
mod-two double-basis array: it is a pair of orthogonal consecutive-block
resolutions of a simple subhypergraph of `H_Gamma`.  The remaining global
equality theorem can therefore be stated without reference to sets:

\[
 \boxed{
 \text{exclude, or construct, a }(p-1)\times p\text{ array of distinct}\
 \text{feasible signed triples satisfying both consecutive-block}\
 \text{resolutions and the bi-unimodular inverse condition.}}
\tag{15.9}
\]

Recovering the actual MWB circuit additionally requires the necklace
transversality and balanced-gain conditions of Sections 1 and 11.

## 16. Exact product-support conservation

The simultaneous grid supplies many more transition matrices than the
`2p` anchor transitions in Theorem 12.4.  For every horizontal packet
`C_i` and vertical packet `D_j`,

\[
                         K_jL_i^{-1}=M_{D_j}M_{C_i}^{-1}
\tag{16.1}
\]

is again a bi-unimodular `{-1,0,1}` wreath transition.  It has exactly
one unit row, corresponding to the common cell `S_(ij)`.

For a wreath transition `T`, let `nu_-(T)` be its total number of negative
entries.  Every row has one more positive entry than negative entries, so

\[
                         \boxed{
 \|T\|_F^2=|\operatorname{supp}T|=p+2\nu_-(T).}
\tag{16.2}
\]

### Theorem 16.1 (row/column product-support identity)

For every fixed horizontal packet `C_i`,

\[
 \boxed{
 \sum_j\|K_jL_i^{-1}\|_F^2
 =\sum_\ell\|L_\ell L_i^{-1}\|_F^2,}
\tag{16.3}
\]

and hence

\[
 \boxed{
 \sum_j\nu_-(K_jL_i^{-1})
 =\sum_\ell\nu_-(L_\ell L_i^{-1}).}
\tag{16.4}
\]

Equivalently, after subtracting the unavoidable one-common-cell and
disjoint-packet baselines,

\[
 \boxed{
 \sum_j\bigl(\nu_-(D_j,C_i)-(p-1)\bigr)
 =\sum_{\ell\ne i}\bigl(\nu_-(C_\ell,C_i)-p\bigr).}
\tag{16.5}
\]

There is a symmetric reverse identity: for every fixed vertical packet
`D_j`,

\[
 \boxed{
 \sum_i\bigl(\nu_-(C_i,D_j)-(p-1)\bigr)
 =\sum_{k\ne j}\bigl(\nu_-(D_k,D_j)-p\bigr).}
\tag{16.6}
\]

#### Proof

The `p^2` cell rows have two partitions into bases, so their common Gram
matrix is

\[
                         G=\sum_\ell L_\ell^{\mathsf T}L_\ell
                          =\sum_j K_j^{\mathsf T}K_j.
\tag{16.7}
\]

Therefore

\[
 \begin{aligned}
 \sum_j\|K_jL_i^{-1}\|_F^2
 &=\operatorname{tr}(L_i^{-\mathsf T}GL_i^{-1})\\
 &=\sum_\ell\|L_\ell L_i^{-1}\|_F^2,
 \end{aligned}
\]

which is (16.3).  Formula (16.2) gives (16.4).  Every `D_j` meets `C_i`
in one cell, so its defect baseline is `p-1`; `C_i` itself has defect zero
and every other horizontal packet is disjoint from it, with baseline `p`.
The two baseline totals are both `p(p-1)`, giving (16.5).  Interchanging
the two resolutions proves (16.6). \(\square\)

### Corollary 16.2 (all-cross equality classification)

For a fixed `i`, every one of the `p` cross transitions
`K_jL_i^{-1}` has minimum support `3p-2` if and only if every one of the
`p-1` same-shore transitions `L_ell L_i^{-1}`, `ell ne i`, has minimum
support `3p`.  Consequently all `p^2` row--column transitions are
endpoint-equality transitions if and only if every ordered pair of
distinct horizontal packets is a disjoint endpoint-equality pair.  By
(16.6), this is also equivalent to the analogous statement for every
ordered pair of distinct vertical packets.

#### Proof

Every summand after baseline subtraction in (16.5) is a nonnegative
integer.  The sum vanishes precisely when every summand on either side
vanishes.  Apply this for every `i`, and then use (16.6). \(\square\)

Thus a product-support argument by itself cannot create a strict global
gap: the cross excess is exactly the same-shore excess viewed through the
other basis partition.  The genuinely stronger remaining object in the
minimum-support case is a family of `p` wreath bases which are pairwise
second-extremal in both directed endpoint metrics, together with an
orthogonal reassembly of their cells.  Excluding that family requires
interaction between the endpoint Hamilton cycles, not another norm or
support inequality.

The cyclic/group-developed version of that minimum-support family can be
excluded completely.

### Theorem 16.3 (no mutually sparse circulant transition)

Let `p>=7` be prime.  There do not exist two circulant integer matrices
`A,B` such that

\[
                         AB=I
\tag{16.8}
\]

and every row of each matrix has exactly two entries `+1`, one entry
`-1`, and all other entries zero.  Consequently a translation-circulant
development in the anchor cell index cannot have every nontrivial
transition endpoint-equality sparse in both directions.

#### Proof

Reduce modulo two.  Let `X,Y subset F_p` be the three-element supports of
the first rows of `A,B`.  Circulant multiplication says that the parity
convolution satisfies

\[
                         \mathbf1_X*\mathbf1_Y=\delta_0
 \quad\text{in }\mathbb F_2[\mathbb F_p].
\tag{16.9}
\]

There are nine ordered representations in the ordinary sum multiset
`X+Y`.  Equation (16.9) requires one sum value to have odd multiplicity
and every other represented value to have positive even multiplicity.
Hence

\[
                         |X+Y|\le1+{8\over2}=5.
\tag{16.10}
\]

Cauchy--Davenport gives `|X+Y|>=3+3-1=5`, so equality holds.  The equality
case of Cauchy--Davenport for `p>=7` makes `X,Y` arithmetic progressions
with a common nonzero difference.  After an affine normalization they are
both `{0,1,2}` up to translation.  Their representation multiplicities
are

\[
                         1,2,3,2,1,
\tag{16.11}
\]

so the parity convolution has three, rather than one, nonzero
coefficients.  This contradicts (16.9). \(\square\)

This theorem is the product-support analogue of Theorem 14.4.  It rules
out a common *circulant* cyclic generator even before imposing actual
endpoint-cycle feasibility.  It does not rule out an arbitrary order-`p`
matrix conjugate over `GL_p(Z)` to a cyclic action.  A putative all-cross
equality grid must at least escape the translation-circulant model; the
remaining bases may have to be genuinely noncommuting and independently
chosen.

## 17. Cyclic-composition classification of an equality transition

The consecutive-block law can be inverted completely. This gives a
statewise description of every endpoint-equality transition, without a
circulant or group-development hypothesis.

Fix a wreath `D` and label its cyclic coordinate order by `F_p`, with
coordinate successor `a(x)=x+1`. Its endpoint-color Hamilton cycle has
successor

\[
                         h=a^m;
\tag{17.1}
\]

indeed, in the notation `pi_t=e_(-2t)`, one has `a=h^(-2)` and hence
`h=a^m`. Let `C` be physically disjoint from `D`, let `Gamma=E_C`, and
assume

\[
                         \nu_-(K(D,C))=p.
\tag{17.2}
\]

Equivalently every cyclic `m`-window in the displayed coordinate order of
`D` spans exactly one edge of `Gamma`.

### Theorem 17.1 (cyclic-composition normal form)

There is a cyclic partition of `F_p` into nonempty consecutive blocks

\[
 B_r=[s_r,s_{r+1}-1],\qquad
 \ell_r=s_{r+1}-s_r,\qquad
1\le\ell_r\le m-1,\qquad \sum_r\ell_r=p,
\tag{17.3}
\]

such that the edges of `Gamma` belonging to block `B_r` are exactly

\[
 \boxed{
 \{s_{r+1}-1,s_r+m-1\},\qquad
 \{s_r+t,s_r+t+m\}\quad(0\le t\le\ell_r-2).}
\tag{17.4}
\]

The first edge in (17.4) is the unique edge assigned to the block; the
remaining `ell_r-1` edges are endpoint edges of `D`. Conversely, for any
cyclic composition satisfying the displayed upper bound, the edges
(17.4) form the unique two-factor
whose every `D`-window spans exactly one edge. It is the endpoint cycle
of an equality wreath precisely when this two-factor is connected.

Equivalently, orient the constant-step Hamilton cycle

\[
                         f=a^{m-1}=h^3,
\tag{17.5}
\]

and let `tau` be the permutation which cyclically rotates every block
`B_r` by one step. Then the oriented successor of `Gamma` is

\[
                         \boxed{g=f\tau=h^3\tau.}
\tag{17.6}
\]

#### Proof

For an edge `e={x,x+d}` with `1<=d<=m-1`, the starts of the cyclic
`m`-windows containing `e` form the interval

\[
                         B_e=[x+d-m+1,x]
\tag{17.7}
\]

of length `m-d`. An edge of distance `m` belongs to no `m`-window.
Condition (17.2) therefore says that the nonempty intervals `(B_e)`
partition `F_p`. Writing one such block as in (17.3), its terminal point
is `x=s_{r+1}-1`, and the equation `ell_r=m-d` forces its edge to be

\[
                         \{s_{r+1}-1,s_r+m-1\}.
\]

These are the first edges in (17.4).

It remains to determine the invisible distance-`m` edges. Index such an
edge by `z_x=1` when `{x,x+m}` is present. The visible-edge degree at a
vertex `y` is

\[
 1_{\{y+1\in\{s_r\}\}}+1_{\{y-m+1\in\{s_r\}\}}.
\]

The choice

\[
                         z_x=1-1_{\{x+1\in\{s_r\}\}}
\tag{17.8}
\]

makes the total degree equal to two at every vertex and gives precisely
the second family in (17.4). It is unique: the difference `w` of two
solutions satisfies `w_y+w_{y-m}=0`; iteration around the odd `p`-cycle
generated by the step `m` gives `w_y=-w_y`, hence `w=0` over the
integers.

Finally, on a block `B_r` the old successor `f(x)=x+m-1` is replaced by
`f(tau(x))`: the last point is sent to the old image of the first, while
every preceding point is sent to the old image of its successor. This is
(17.6). A two-regular graph is one wreath endpoint cycle exactly when it
is connected. \(\square\)

The composition has an immediate parity consequence. Its excess length

\[
 z(C,D):=\sum_r(\ell_r-1)
          =|E_C\cap E_D|
\tag{17.9}
\]

counts the shared endpoint edges.

Since `p` is odd, Corollary 17.2 also says that

\[
                         |B|=p-z\text{ is odd}.
\tag{17.9a}
\]

The gap bound `ell_r<=m-1` forces `|B|>=3`: one or two such gaps cannot
sum to `p=2m+1`.

In fact the three-boundary case cannot be Hamiltonian.

### Lemma 17.2a (no three-boundary equality wreath)

In Theorem 17.1, if the two-factor `g` is a Hamilton cycle, then

\[
                         \boxed{|B|\ge5.}
\tag{17.9b}
\]

#### Proof

Suppose `|B|=3`.  Rotate the natural coordinate order and write

\[
                         B=\{0,a,a+b\},
\]

with positive cyclic gaps `a,b,c<=m-1` and `a+b+c=p`.  The endpoint
successor is `h(x)=x+m`, whose inverse is multiplication by the additive
step `-2` in the natural coordinate parameter.  For `g=h pi_B` to be one
cycle, cutting the three `h`-arcs at `B` and reconnecting them by the
predecessor cycle `pi_B` requires the order of `B` along the `h`-cycle to
be the reverse of its natural order.

Now `a<=m-1`, while `c<=m-1` gives `a+b=p-c>=m+2`.  The positions of
`a` and `a+b` in the oriented `h`-cycle starting at zero are therefore

\[
                         p-2a,qquad 2c,
\]

respectively.  Reverse order would require

\[
                         2c<p-2a,
\]

or `2(a+c)<p`.  Since `a+b+c=p`, this says `2b>p`, hence
`b>=m+1`, contradicting `b<=m-1`. \(\square\)

### Corollary 17.2 (shared-edge parity)

For endpoint-equality wreaths `C,D`,

\[
                         \boxed{|E_C\cap E_D|\text{ is even}.}
\tag{17.10}
\]

#### Proof

Both `f` and `g` in (17.6) are `p`-cycles and therefore have positive
permutation sign. The sign of `tau` is
`(-1)^(sum_r(ell_r-1))`. Equation (17.6) makes that sign positive.
\(\square\)

There is now a genuinely noncommutative obstruction to mutual equality.

### Theorem 17.3 (a mutually extremal pair shares at least two endpoint edges)

Let `p=2m+1>=7` be prime. If two physically disjoint wreaths satisfy

\[
 \nu_-(K(D,C))=\nu_-(K(C,D))=p,
\tag{17.11}
\]

then

\[
                         \boxed{|E_C\cap E_D|\ge2.}
\tag{17.12}
\]

#### Proof

By Corollary 17.2 the intersection size is even. Suppose it is zero.
Then (17.9) makes every block in (17.3) a singleton, so `tau=1` and

\[
                         g=h^3.
\tag{17.13}
\]

Apply the same argument in the reverse direction. The coordinate
successor of `C` is `g^(-2)`, so the constant-step equality endpoint
successor is `(g^(-2))^(m-1)=g^3`. Since the endpoint cycles are still
edge-disjoint, the reverse composition also has only singleton blocks.
There is no shared edge fixing the orientation of the physical endpoint
cycle of `D`, so for one sign `epsilon in {1,-1}` we obtain

\[
                         h^\epsilon=g^3=h^9.
\tag{17.14}
\]

The permutation `h` has prime order `p`.  Equation (17.14) forces `p` to
divide `8` when `epsilon=1`, or `10` when `epsilon=-1`, both impossible
for prime `p>=7`. \(\square\)

Thus the minimum-support case of Corollary 16.2 is much more rigid than a
clique of abstract sparse bases. On either shore of a putative equality
grid, the `p` endpoint Hamilton cycles form a two-intersecting family:

\[
 \boxed{
 |E_{C_i}\cap E_{C_\ell}|\ge2\quad(i\ne\ell),\qquad
 |E_{D_j}\cap E_{D_k}|\ge2\quad(j\ne k).}
\tag{17.15}
\]

This conclusion uses the feasible endpoint geometry and the
consecutive-block law, but no commutativity. The remaining equality-grid
gate is now narrower: combine the two-intersection condition (17.15) with
the fact that the corresponding maximum-independent-set packets are
pairwise physically disjoint and admit the orthogonal reassembly.

One must not convert (17.12) into a metric-defect charge.  A shared
endpoint edge of `C` and `D` has distance exactly `m` in the cyclic
coordinate order of either wreath.  It is therefore an *invisible* edge:
its contribution to `m-d` in (12.13) is zero.  Equivalently, shared
endpoint edges are exactly the second family in (17.4).  Their force is
permutational, not metric.

That permutational force gives a much stronger intersection bound.  For
a permutation `rho`, write

\[
                         \ell_T(\rho)=p-c(\rho)
\tag{17.16}
\]

for its Cayley length with respect to all transpositions, where `c(rho)`
is the number of cycles including fixed points.  This length is invariant
under conjugation and subadditive.

### Theorem 17.4 (linear endpoint intersection for mutual equality)

Under the hypotheses of Theorem 17.3,

\[
             \boxed{|E_C\cap E_D|\ge {p-1\over4}.}
\tag{17.17}
\]

#### Proof

Let `h` be the oriented endpoint successor of `D`, and orient the endpoint
cycle of `C` as `g` in the forward cyclic-composition normal form.  Then

\[
                         g=h^3\tau,
 \qquad \ell_T(\tau)=z:=|E_C\cap E_D|.
\tag{17.18}
\]

In the reverse normal form the physical endpoint cycle of `D` may acquire
either of its two orientations.  Thus, for one sign `epsilon in {1,-1}`,

\[
                         h^\epsilon=g^3\upsilon,
 \qquad \ell_T(\upsilon)=z.
\tag{17.19}
\]

Expand the cube in (17.19).  There are three conjugates
`tau_0,tau_1,tau_2` of `tau` such that

\[
                         (h^3\tau)^3
                         =h^9\tau_2\tau_1\tau_0.
\tag{17.20}
\]

Combining (17.19)--(17.20), and conjugating factors if necessary when
moving `h^9` across the equality, expresses

\[
                         h^{\epsilon-9}
\tag{17.21}
\]

as a product of three conjugates of `tau` and one conjugate of `upsilon`.
The exponent in (17.21) is `-8` or `-10`.  Since `p>=7` is prime, neither
is zero modulo `p`; hence (17.21) is a `p`-cycle and has Cayley length
`p-1`.  Subadditivity and conjugacy invariance give

\[
                         p-1\le3\ell_T(\tau)
                                  +\ell_T(\upsilon)=4z.
\]

This proves (17.17). \(\square\)

Consequently, on either shore of an all-cross minimum-support affine
grid, the endpoint cycles satisfy the linear intersection condition

\[
 |E_{C_i}\cap E_{C_\ell}|\ge{p-1\over4},\qquad
 |E_{D_j}\cap E_{D_k}|\ge{p-1\over4}.
\tag{17.22}
\]

If `r_e` is the number of horizontal endpoint cycles containing a
coordinate edge `e`, then

\[
 \sum_e r_e=p^2,
 \qquad
 \sum_e\binom{r_e}{2}
 =\sum_{i<\ell}|E_{C_i}\cap E_{C_\ell}|
 \ge {p(p-1)^2\over8}.
\tag{17.23}
\]

In particular some coordinate edge belongs to at least

\[
                         1+{(p-1)^2\over4p}
\tag{17.24}
\]

horizontal endpoint cycles, and the analogous statement holds on the
vertical shore.  Indeed
`binom(r,2)<=((r_max-1)/2)r`, and (17.23) together with
`sum r=p^2` gives (17.24).

This is not yet a contradiction: high endpoint-edge multiplicity is
compatible with the raw number of available middle sets.  It is,
however, the first noncommutative concentration theorem for a putative
equality grid.  Any completion of the no-grid proof must now use the
orthogonal cell reassembly to rule out (or exploit) an endpoint edge
carried by a linear fraction of every shore.

The normal form has a second expression which makes mutuality exact.
Let `B` be the set of terminal points of the blocks (17.3), and put
`S=F_p\B`.  Thus `S` is the set of sources of the shared, coherently
oriented endpoint edges and

\[
                         |S|=z,\qquad |B|=p-z.
\tag{17.25}
\]

Order `B` by its occurrence in the cyclic coordinate order `h^(-2)`.
Let `pi_B` fix `S` pointwise and send every member of `B` to its
predecessor in this induced cyclic order.

### Theorem 17.5 (boundary-order reversal criterion)

In the forward equality normal form,

\[
                         \boxed{g=h\pi_B.}
\tag{17.26}
\]

Suppose equality also holds in the reverse direction.  Then the
orientations of `g,h` agree on every shared edge, and the order induced on
`B` by the second cyclic coordinate order `g^(-2)` is the reverse of the
order induced by `h^(-2)`.  Conversely, this reverse-order condition,
together with the requirement that every first-return gap to `B` in the
`g^(-2)` order is at most `m-1`, is exactly the additional
cyclic-composition condition for reverse equality.

#### Proof

Consider a block from the successor of a boundary point `b_-` through the
next boundary point `b_+`, in the `h^(-2)` coordinate order.  Formula
(17.4) says that `g(x)=h(x)` at every nonterminal point of the block,
whereas at its terminal point

\[
                         g(b_+)=h(b_-).
\tag{17.27}
\]

Thus `h^(-1)g` fixes `S` and sends `b_+` to its predecessor `b_-` on
`B`, proving (17.26).

Theorem 17.4 gives `z>0`.  Therefore the reverse normal form cannot orient
the endpoint cycle of `D` as `h^(-1)`: on a shared edge the forward form
orients `g` in the same direction as `h`, while the reverse form would
then require the same directed edge to agree with `h^(-1)`.  Hence the
reverse endpoint successor is `h` itself.

Apply (17.26) in reverse.  There is a permutation `pi'_B`, fixing the
same shared-source set `S` and sending each boundary point to its
predecessor in the `g^(-2)` coordinate order, such that

\[
                         h=g\pi'_B.
\tag{17.28}
\]

Equations (17.26) and (17.28) give

\[
                         \pi'_B=g^{-1}h=\pi_B^{-1}.
\]

Thus predecessor in the `g^(-2)` order is successor in the `h^(-2)`
order, which is precisely reversal of the induced cyclic order on `B`.
The upper bound on first-return gaps is the reverse copy of the bound
`ell_r<=m-1` in (17.3).  With it included, every step is reversible,
proving the converse. \(\square\)

After identifying the first coordinate order with the natural cycle,
Theorem 17.5 gives the following purely finite gate.  Choose a nonempty
proper boundary set `B`, let `pi_B` be its predecessor cycle, put

\[
                         h(x)=x+m,qquad g=h\pi_B,
\tag{17.29}
\]

and require that `g` is a `p`-cycle, that the first-return order of
`g^(-2)` on `B` is the reverse of the natural order on `B`, and that all
first-return gaps in both coordinate orders are at most `m-1`. A mutually
endpoint-equality pair exists exactly when this permutation-order system
has a solution. Moreover Theorem 17.4 restricts every solution to

\[
                         |B|\le {3p+1\over4}.
\tag{17.30}
\]

This criterion is noncommutative, contains no metric relaxation, and is
strictly smaller than the original signed-frame system.  A proof that
(17.29) has no solution for prime `p>=7` would close the entire
minimum-support affine-grid case already at the level of one same-shore
pair; a solution would be an explicit new equality pair beyond all
currently known one-sided examples.

There is a useful genus/noncrossing restatement.  The permutation `pi_B`
has one nontrivial cycle on `B` and fixes `S`, so

\[
                         \ell_T(\pi_B)=|B|-1=p-z-1.
\tag{17.31}
\]

Comparing the two forward expressions `g=h pi_B=h^3 tau` gives

\[
                         \boxed{h^2=\pi_B\tau^{-1}.}
\tag{17.32}
\]

Together with `ell_T(tau)=z`, this is a geodesic factorization:

\[
 \ell_T(\pi_B)+\ell_T(\tau)=p-1=\ell_T(h^2).
\tag{17.33}
\]

Thus `pi_B` and `tau^(-1)` are complementary noncrossing permutations
relative to the long cycle `h^2`.  In the mutual case the reverse form
gives simultaneously

\[
                         \boxed{g^2=\pi_B^{-1}\upsilon^{-1},}
\tag{17.34}
\]

again with equality of Cayley lengths.  On the other hand the pair of
long cycles `h,g` has

\[
 c(h)=c(g)=1,\qquad c(h^{-1}g)=c(\pi_B)=z+1,
\]

so its orientable permutation-map genus is exactly

\[
                         \boxed{\mathfrak g(h,g)={|B|-1\over2}.}
\tag{17.35}
\]

Consequently the first-return reversal problem is a simultaneous
noncrossing-complement, or meandric, constraint rather than an arbitrary
Hamilton-cycle comparison.  This explains why parity alone is exhausted:
the oddness of `|B|` is exactly the integrality of (17.35).  The exact
first-return dynamics below, rather than a crossing count, closes this
pairwise constraint completely.

In fact the first-return condition itself is inconsistent.  The useful
point is that the inverse coordinate successor can be followed exactly,
without estimating a permutation length.

### Theorem 17.6 (mutual endpoint equality is impossible)

Let `p=2m+1>=7` be prime.  There are no two physically disjoint wreaths
`C,D` for which

\[
 \nu_-\bigl(K(D,C)\bigr)=\nu_-\bigl(K(C,D)\bigr)=p.
\tag{17.36}
\]

Equivalently, the boundary-order system (17.29) has no solution.

#### Proof

Use the normalization of Theorem 17.5.  Thus

\[
 h(x)=x+m,\qquad h^{-2}(x)=x+1,
\tag{17.37}
\]

and write the boundary points in the natural cyclic order as

\[
 B=\{b_i:i\in\mathbb Z_k\},\qquad
 b_i<b_{i+1},\qquad k=|B|.
\tag{17.38}
\]

Here and below the inequalities use compatible cyclic integer lifts of
successive boundary points.

Let `P=pi_B` be predecessor on `B`, fixing its complement, and let
`Q=P^{-1}` be successor on `B`.  Formula (17.26) gives `g=hP`, hence
the second coordinate successor is

\[
 T:=g^{-2}=Qh^{-1}Qh^{-1}.
\tag{17.39}
\]

Theorem 17.5 says that the first-return map of `T` on `B` must be

\[
                         b_i\longmapsto b_{i-1}.
\tag{17.40}
\]

Partition the natural coordinate cycle into the half-open gaps

\[
                         G_i=[b_i,b_{i+1}).
\tag{17.41}
\]

Away from `h(B)` and from the points immediately preceding `B`, the map
`T` is ordinary successor `x\mapsto x+1`.  More explicitly, if
`x\notin h(B)` and `x+1\notin B`, then the two copies of `Q` in
(17.39) both act trivially and

\[
                         T(x)=h^{-2}(x)=x+1.
\tag{17.42}
\]

Suppose first that a gap `G_i` contains no point of `h(B)`.  Starting at
`b_i`, equation (17.42) advances one step at a time up to
`b_{i+1}-1`.  At that last point the outer `Q` sends `b_{i+1}` to
`b_{i+2}`.  Thus the first return is `b_{i+2}`, contrary to (17.40),
because `k>=5` by Lemma 17.2a.

It follows that every gap contains a point of `h(B)`.  There are `k`
gaps and `|h(B)|=k`, so every gap contains exactly one.  Translation by
`m` preserves cyclic order; consequently, after one common cyclic shift
of the indices, there are points

\[
 x_i=h(b_{i-r})\in G_i
\tag{17.43}
\]

for one fixed `r\in\mathbb Z_k`, and these are the unique points of
`h(B)` in their respective gaps.

Now follow `T` from `b_i`.  It advances by (17.42) until it reaches
`x_i`.  At this exceptional point, (17.39) gives

\[
 \begin{aligned}
 T(x_i)
 &=Qh^{-1}Qh^{-1}\bigl(h(b_{i-r})\bigr)\\
 &=Qh^{-1}(b_{i-r+1})\\
 &=Q\bigl(h(b_{i-r+1})+1\bigr)\\
 &=Q(x_{i+1}+1).
 \end{aligned}
\tag{17.44}
\]

Here we used `h^{-1}(y)=h(y)+1`, which follows from `2m+1=p`.
If `x_{i+1}+1=b_{i+2}`, the final `Q` in (17.44) sends it directly to
`b_{i+3}`.  Otherwise (17.44) lands immediately after the unique point
of `h(B)` in `G_{i+1}`.  Equation (17.42) then advances to
`b_{i+2}-1`, whose next `T`-image is again `Q(b_{i+2})=b_{i+3}`.
In either case the first-return map is therefore

\[
                         b_i\longmapsto b_{i+3}.
\tag{17.45}
\]

Comparing (17.40) and (17.45) gives `3\equiv-1\pmod k`, so `k` divides
four.  This contradicts `k>=5`.  Hence (17.36) is impossible. \(\square\)

### Corollary 17.7 (the minimum transition-support orthogonal grid is excluded)

The all-cross equality case of Theorem 12.4 cannot occur.  Indeed, any
two distinct packets on either shore would be physically disjoint and
would satisfy mutual endpoint equality, contradicting Theorem 17.6.

Thus the orientation-frustration analysis of Sections 19--20 is no
longer needed for the minimum-support case: the obstruction is already
pairwise.  Those sections remain useful as independent structural
ledgers, but their negative triangle cannot actually arise from mutually
extremal wreath transitions.

This does **not** by itself exclude the abstract necklace-incidence
`K_(p,p)` of Theorem 32.3, nor an orthogonal wreath grid with nonminimal
transition support.  It closes exactly the all-cross endpoint-equality
case isolated by Corollary 16.2.

There is also a quantitative support gap.  For disjoint wreaths put

\[
 e(D,C)=\nu_-\bigl(K(D,C)\bigr)-p\ge0.
\tag{17.46}
\]

### Corollary 17.8 (global half-unit cross gap)

In every orthogonal wreath grid,

\[
 \boxed{
 \sum_{i,j}
 \left(\nu_-\bigl(K(D_j,C_i)\bigr)-(p-1)\right)
 \ge\binom p2.}
\tag{17.47}
\]

Equivalently the average cross-transition excess above the
one-common-cell baseline is at least `(p-1)/(2p)`, and the total Frobenius
support excess above `p^2(3p-2)` is at least `p(p-1)`.

#### Proof

For each unordered pair of distinct horizontal packets, Theorem 17.6
gives

\[
                         e(C_i,C_\ell)+e(C_\ell,C_i)\ge1.
\]

Summing over the `binom(p,2)` pairs and applying the product-support
identity (16.5), summed over all anchors `i`, gives (17.47).  Formula
(16.2) doubles negative-entry excess when converted to Frobenius support.
\(\square\)

The same argument is not special to a `p by p` grid.

### Theorem 17.9 (resolution-size support gap)

Let

\[
 \mathcal C=C_1\sqcup\cdots\sqcup C_r
 =D_1\sqcup\cdots\sqcup D_r=\mathcal D
\tag{17.48}
\]

be two wreath factorizations of the same `rp` distinct middle sets.  Put
`t_(ij)=|C_i\cap D_j|`.  Then

\[
 \boxed{
 \sum_{i,j}
 \left(\nu_-\bigl(K(D_j,C_i)\bigr)-(p-t_{ij})\right)
 \ge\binom r2.}
\tag{17.49}
\]

The corresponding total Frobenius-support excess is at least
`r(r-1)`.

Interchanging the two resolutions gives the independent reverse-directed
inequality

\[
 \sum_{i,j}
 \left(\nu_-\bigl(K(C_i,D_j)\bigr)-(p-t_{ij})\right)
 \ge\binom r2.
\tag{17.49a}
\]

Thus the bidirectional negative-entry excess is at least `r(r-1)`, and
the bidirectional Frobenius-support excess is at least `2r(r-1)`.

#### Proof

The common cell Gram matrix gives, for every fixed `i`,

\[
 \sum_j\|K(D_j,C_i)\|_F^2
 =\sum_\ell\|K(C_\ell,C_i)\|_F^2,
\]

exactly as in Theorem 16.1.  Hence the same identity holds with
Frobenius norms replaced by `nu_-`.  Since `sum_j t_(ij)=p`, the cross
baseline is

\[
 \sum_j(p-t_{ij})=(r-1)p,
\]

which equals the baseline of the `r-1` disjoint same-shore transitions.
After subtracting baselines and summing over `i`, the left side of
(17.49) is exactly

\[
 \sum_{i\ne\ell}
 \left(\nu_-\bigl(K(C_\ell,C_i)\bigr)-p\right).
\tag{17.50}
\]

For each unordered pair `{i,ell}`, Theorem 17.6 says that its two
directed summands in (17.50) cannot both vanish.  They are nonnegative
integers, so their sum is at least one.  Summing over the unordered pairs
proves (17.49); (16.2) gives the Frobenius assertion. \(\square\)

For `r=2`, every genuine two-for-two wreath trade therefore has at least
one negative entry (two Frobenius-support positions) beyond the formal
common-cell baselines.  For `r=p`, this is Corollary 17.8.

## 18. Shared dual coordinates: exact ledger and its limitation

The concentration (17.24) can be read directly in the orthogonal cell
array.  For a coordinate pair `e={x,y}`, define

\[
                         Q_e(i,j)=1-|S_{ij}\cap e|.
\tag{18.1}
\]

### Proposition 18.1 (unit-row/unit-column ledger)

Every row and every column of `Q_e` has sum one.  Moreover

\[
 \boxed{
 e\in E_{C_i}\iff Q_e(i,\cdot)\text{ is a unit row},\qquad
 e\in E_{D_j}\iff Q_e(\cdot,j)\text{ is a unit column}.}
\tag{18.2}
\]

If `r_e` and `s_e` are the two endpoint-cycle multiplicities, then `Q_e`
has exactly `r_e` unit rows and `s_e` unit columns.  If `r_e=p`, then
`Q_e` is a permutation matrix and consequently `s_e=p`; the converse is
also true.

#### Proof

In any wreath each coordinate belongs to exactly `m` cells.  Therefore

\[
 \sum_{A\in C_i}(1-|A\cap e|)=p-2m=1,
\]

and similarly down every vertical packet.  The endpoint inverse formula
(12.2)--(12.4) says that evaluation on a packet is a unit vector exactly
when `e` is one of that packet's endpoint edges.  This proves (18.2).
If every row is unit, the total number of nonzero entries is `p`; column
sums equal one and no negative entry occurs, so every column is unit as
well. \(\square\)

Proposition 18.1 also marks a limitation of pure rank arguments.  A
single dual functional may belong to all `2p` dual wreath bases: its
evaluation matrix is then merely a permutation matrix.  This is
consistent with all coordinate marginals and with `p^2` distinct cells.
Hence the linear multiplicity forced by (17.24) cannot be capped using
row/column sums, dual-space dimension, or bi-unimodularity alone.  The
remaining obstruction must couple several endpoint edges through their
cyclic-composition boundary orders.

## 19. The globally oriented shore is impossible

**Status note.**  Sections 19--20 record a valid conditional analysis of
the orientation-sign system, but Theorem 17.6 now shows that its premise
(a mutually endpoint-equality shore) is unrealizable.  They are retained
because the circuit and signed-graph lemmas may be useful for nonminimal
transition problems; they are no longer an open branch of the all-cross
equality case.

There is a sharp circuit obstruction once the relative endpoint
orientations on one shore are coherent.  We separate that orientation
gate explicitly; it must not be silently assumed.

We use the following elementary graphic-circuit fact.  It is the circuit
analogue of the statement that a large clique of paths differing in one
interval is a pencil.

### Lemma 19.1 (large circuit-difference families are pencils)

Let `G` be a simple graph and let `Z_1,...,Z_t` be distinct simple
circuits such that `Z_i triangle Z_j` is a simple circuit for every
`i ne j`.  If the family is not contained in the cycle space of a
subdivision of `K_4` (which has only seven nonzero circuit vectors), then
there are vertices `u,v` and pairwise internally vertex-disjoint `u-v`
paths

\[
                         P_0,P_1,\ldots,P_t
\tag{19.1}
\]

such that

\[
                         \boxed{Z_i=P_0\cup P_i.}
\tag{19.2}
\]

In particular every such family of at least eight circuits has the form
(19.2).

#### Proof

For two circuits `A,B`, the condition that `A triangle B` is one circuit
says that their common edge set is one path after common initial and
terminal subpaths are amalgamated.  Their union is therefore a theta
subdivision: three internally disjoint paths between the two divergence
vertices.

Add a third compatible circuit and trace it through this theta.  It may
either use the same one of the three paths and introduce one further
internally disjoint return path, or it may enter through a second branch
and leave through a third.  In the latter case the four branch vertices
and the six traced path segments form a subdivision of `K_4`.  Circuit
compatibility forces every later circuit to remain inside that
subdivision: leaving it would make its symmetric difference with one of
the four facial circuits split into two edge-disjoint circuits.  A
subdivision of `K_4` has cycle-space dimension three and its seven
nonzero vectors are its only possible circuit-difference members.

Outside this exceptional case, every added circuit uses the same common
path.  Strip the maximal common initial and terminal portions.  If two
remaining return paths met internally and then separated again, their
symmetric difference would have two circuit components.  Hence the
return paths are pairwise internally disjoint, giving (19.1)--(19.2).
\(\square\)

Now let `H_0,...,H_(r)` be endpoint Hamilton cycles and suppose they can
be oriented with successors `h_0,...,h_r` so that every quotient

\[
                         h_i^{-1}h_j
\tag{19.3}
\]

has exactly one nontrivial cycle, of odd length.  Regard each `h_i` as a
perfect matching `M_i` between two copies of the coordinate set.  Put

\[
                         Z_i=M_i\mathbin\triangle M_0
 qquad(1\le i\le r).
\tag{19.4}
\]

Then `Z_i` and every `Z_i triangle Z_j` are single alternating circuits.
If the nontrivial quotient cycle has odd length, each corresponding
alternating circuit has length `2 modulo 4`.

### Theorem 19.2 (odd circuit-pencil bound)

For `p>=11`, a coherently oriented family as above has at most `p-1`
members in total:

\[
                         \boxed{r+1\le p-1.}
\tag{19.5}
\]

#### Proof

If `r+1>=p`, then `r>=p-1>=10`, so Lemma 19.1 places the circuits
`Z_1,...,Z_r` in a pencil (19.2); the `K_4` exception has at most seven
members.

Write `L_i=|P_i|`.  Since both `Z_i=P_0 union P_i` and
`Z_i triangle Z_j=P_i union P_j` have length `2 modulo 4`, one has

\[
 L_0+L_i\equiv2,qquad L_i+L_j\equiv2\pmod4.
\tag{19.6}
\]

With at least three return paths, (19.6) forces all
`L_0,L_1,...,L_r` to have the same odd residue modulo four.  Thus `u,v`
belong to opposite shores of `K_(p,p)`.

If the common residue is one, at most one path has length one and every
other path has length at least five, consuming at least two internal
vertices on each shore.  Since only `p-1` internal vertices are available
on either shore,

\[
 r+1\le1+\left\lfloor{p-1\over2}\right\rfloor<p.
\]

If the common residue is three, every path has length at least three and
consumes at least one internal vertex on each shore.  Hence

\[
                         r+1\le p-1.
\]

Both cases contradict `r+1>=p`, proving (19.5). \(\square\)

For an endpoint-equality shore, Corollary 17.2 makes every quotient-cycle
support odd.  Therefore Theorem 19.2 has the following exact consequence.

### Corollary 19.3 (orientation frustration is necessary)

For prime `p>=11`, the `p` same-shore endpoint cycles of an all-cross
minimum-support affine grid cannot admit one choice of orientation per
cycle for which all pairwise equality normal forms are simultaneously
orientation-preserving.

Equivalently, their pairwise relative-orientation signs form an
unbalanced signed complete graph.  In particular some triangle of wreaths
has pairwise equality orientations whose product is negative.

#### Proof

Under a coherent choice, Theorem 17.5 makes every quotient (19.3) one
proper odd cycle.  Theorem 19.2 would bound the shore by `p-1`, whereas it
contains `p` packets. \(\square\)

This does not yet exclude the grid.  Pairwise relative orientations are
defined by agreement along their shared endpoint edges, and a negative
triangle can occur only when the three endpoint cycles have no common
edge.  Thus the equality case has been reduced further to a concrete
alternative:

\[
 \boxed{
 \begin{gathered}
 \text{either the shore orientations are coherent, in which case it is}\
 \text{impossible by Theorem 19.2, or every survivor contains a negative}\
 \text{orientation triangle with three disjoint pair-intersection cores.}
 \end{gathered}}
\tag{19.7}
\]

The remaining all-cross equality theorem is therefore an
orientation-frustration exclusion, not a support, determinant, or metric
inequality.

The high-multiplicity edge from (17.24) nevertheless supplies a linear
coherent subsystem, without Ramsey loss.

### Corollary 19.4 (linear bounded-pencil subsystem)

For all sufficiently large `p`, every putative equality shore contains a
coherently oriented subfamily of at least

\[
                         1+{(p-1)^2\over4p}
\tag{19.8}
\]

endpoint cycles whose successor matchings form one circuit pencil as in
Lemma 19.1.  If the pencil paths are `P_0,...,P_(q-1)`, then

\[
                         {1\over q}\sum_t|P_t|
                         \le1+{2(p-1)\over q}<10
\tag{19.9}
\]

for all sufficiently large `p`.  In particular a positive linear
subfamily differs from a common successor matching by alternating
circuits of uniformly bounded average length.

#### Proof

Choose an endpoint edge of multiplicity `q` as in (17.24), and orient all
cycles containing it in the same direction.  Every relative orientation
inside this subfamily is then positive.  For large `p`, `q-1>=8`, so
Lemma 19.1 gives a circuit pencil; the subdivided-`K_4` exception is too
small.

All pencil paths have odd length and are pairwise internally disjoint
between opposite bipartition shores.  A path of length `L` uses
`(L-1)/2` internal vertices on each shore.  There are only `p-1` such
vertices per shore, so

\[
                         \sum_t{|P_t|-1\over2}\le p-1,
\]

which is (19.9) together with the lower bound on `q`. \(\square\)

This is concentration, not yet a no-go.  A bounded change in an endpoint
Hamilton cycle can alter all `p` maximum-independent-set cells, so the
physical wreath packets in this pencil may still be disjoint.  Any final
use of (19.9) must invoke the orthogonal reassembly or a suspension
invariant; endpoint edit distance alone is insufficient.

## 20. Exact normal form of the surviving negative triangle

Let `A,B,C` be a negative orientation triangle supplied by Corollary
19.3.  Choose endpoint successors `a,b,c` so that the `A--B` and `B--C`
shared edges have the same directions, while the `C--A` shared edges have
opposite directions.  Put

\[
 X=E_A\cap E_B,qquad Y=E_B\cap E_C,qquad Z=E_C\cap E_A.
\tag{20.1}
\]

### Proposition 20.1 (disjoint linear cores)

The three sets in (20.1) are pairwise disjoint and

\[
                         |X|,|Y|,|Z|\ge {p-1\over4}.
\tag{20.2}
\]

#### Proof

The lower bounds are Theorem 17.4.  If an endpoint edge belonged to all
three cycles, its three pairwise relative orientation signs would be the
products of three vertex signs and hence would multiply to `+1`.  This
contradicts the negative triangle.  Thus the triple intersection is
empty, which makes the three pairwise intersections in (20.1) disjoint.
\(\square\)

Define the aligned relative permutations

\[
 \alpha=a^{-1}b,qquad
 \beta=b^{-1}c,qquad
 \gamma=a^{-1}c^{-1}.
\tag{20.3}
\]

Each is one proper odd cycle with fixed points, obeys its own
boundary-order reversal criterion, and has Cayley length at most
`(3p-3)/4`.  The three are coupled by one exact factorization.

### Proposition 20.2 (negative-triangle factorization)

One has

\[
                         \boxed{a\gamma a\alpha\beta=1.}
\tag{20.4}
\]

Equivalently, `a^2` is a product of three conjugates of
`alpha^(-1),beta^(-1),gamma^(-1)`.  Consequently

\[
 (p-1)le\ell_T(\alpha)+\ell_T(\beta)+\ell_T(\gamma),
\tag{20.5}
\]

or, in shared-core form,

\[
                         |X|+|Y|+|Z|\le2p-2.
\tag{20.6}
\]

#### Proof

The first two definitions give `c=a alpha beta`.  The third gives
`c^(-1)=a gamma`.  Multiplying these inverse identities yields (20.4).
Moving one copy of `a` across (20.4) expresses the nontrivial `p`-cycle
`a^2` as the stated product; Cayley subadditivity proves (20.5).  Since
`ell_T(alpha)=p-|X|-1`, and similarly for the other two cycles, (20.6)
is the same inequality. \(\square\)

There is also an exact edge-chain form.  For an oriented Hamilton cycle
`a`, write `[a]` for the integral directed one-chain consisting of its
`p` oriented edges.

### Proposition 20.3 (short residual circulation)

The chain

\[
                         \boxed{\Omega=[a]-[b]+[c]}
\tag{20.7}
\]

is a nonzero integral circulation.  All edges in `X union Y union Z`
cancel, and therefore

\[
 \|\Omega\|_1
 =3p-2(|X|+|Y|+|Z|)
 \le {3p+3\over2}.
\tag{20.8}
\]

#### Proof

Each Hamilton one-chain has zero boundary, so (20.7) is a circulation.
On `X`, the terms `[a]-[b]` cancel; on `Y`, the terms `-[b]+[c]`
cancel; and on `Z`, the cycles `a,c` traverse the common edge in opposite
directions, so `[a]+[c]` cancels.  Proposition 20.1 makes these cores
disjoint, giving the equality in (20.8), and (20.2) gives its upper bound.
The chain cannot vanish: three odd edge counts cannot be partitioned
entirely into pairwise cancellations when the triple intersection is
empty. \(\square\)

Thus the last minimum-support obstruction is now a concrete three-cycle
problem:

\[
 \boxed{
 \begin{gathered}
 \text{exclude three Hamilton endpoint successors satisfying (20.1)--(20.8),}\
 \text{with each of the three relative cycles also satisfying the two}\
 \text{simultaneous noncrossing-complement laws (17.32)--(17.34).}
 \end{gathered}}
\tag{20.9}
\]

Neither (20.6) nor the circulation bound alone is contradictory: their
allowed interval is

\[
 {3(p-1)\over4}\le |X|+|Y|+|Z|\le2p-2.
\]

The missing step must therefore use the boundary orders or the
orthogonal cell reassembly, not another first-moment edge count.

There is nevertheless a useful Ramsey consequence of Proposition 20.1.

### Corollary 20.4 (bounded negative cliques)

In the relative-orientation signed graph of a mutually endpoint-equality
family, every all-negative clique has size at most five.  Consequently a
shore of `p` packets contains a coherently oriented all-positive clique of
size `Omega(p^(1/5))`.

#### Proof

In an all-negative clique, no endpoint edge can lie in three cycles:
the three relative orientation signs contributed by one common edge are
products of vertex orientations and therefore have positive triangle
product.  Fix one cycle in a negative clique of size `r`.  Its
intersection cores with the other `r-1` cycles are consequently disjoint.
Theorem 17.4 gives

\[
                         (r-1){p-1\over4}\le p.
\]

For `p>=7` this implies `r<=5`.

Color a pair positive or negative according to its relative orientation.
The negative graph has no `K_6`.  The elementary Ramsey recursion gives
`R(6,t)<=binom(t+4,5)`, so on `p` vertices the positive graph contains a
clique of order at least a constant times `p^(1/5)`. \(\square\)

The exponent `1/5` is not enough by itself: Theorem 19.2 excludes a
coherent clique of order `p`, but permits sublinear coherent pencils.
Corollary 20.4 does show that orientation frustration cannot be spread as
an arbitrary random sign pattern; it coexists with a growing coherent
subsystem on which all of Sections 17 and 19 apply simultaneously.

Endpoint multiplicity gives a complementary dense-triple statement.

### Corollary 20.5 (triple-coherence moment)

Let `r_e` be the endpoint-edge multiplicities on one equality shore.  For
`p>=11`,

\[
 \sum_e\binom{r_e}{3}
 \ge {p^4-8p^3+14p^2-8p+1\over96}.
\tag{20.10}
\]

Thus the average number of literal common endpoint edges in a triple of
shore cycles is at least `(1/16-o(1))p`.  In particular a positive
proportion of all triangles are orientation-balanced for the strongest
possible reason: they share an endpoint edge.

#### Proof

Write `R_k=sum_e r_e^k`.  Equations (17.23) and `R_1=p^2` give

\[
                         R_2\ge {p(p+1)^2\over4}.
\]

Cauchy--Schwarz gives `R_3>=R_2^2/R_1`.  On the displayed range the
function `x^2/p^2-3x+2p^2` is increasing for
`x>=p(p+1)^2/4`.  Therefore

\[
 \begin{aligned}
 6\sum_e\binom{r_e}{3}
 &=R_3-3R_2+2R_1\\
 &\ge {(p+1)^4\over16}-{3p(p+1)^2\over4}+2p^2,
 \end{aligned}
\]

which is (20.10).  Divide by `binom(p,3)` for the average statement.  A
triangle with a common endpoint edge has positive orientation product.
\(\square\)

The moment bound still permits negative triangles: it supplies a dense
coherent reservoir, not a global switching potential.  Closing the gate
requires showing that the simultaneous boundary-order complements cannot
support the remaining frustrated triangles around that reservoir.
