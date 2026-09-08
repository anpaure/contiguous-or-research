# Native MSW wreaths do not inherit the published standard-pull collar

## Status

This note audits the proposed shortcut

\[
 \text{MSW minimum wreath factor}
 \;\longrightarrow\;
 \text{published plane-tree pull tree}
 \;\longrightarrow\;
 \text{masked }C_6\text{ joins}.
\]

The first object has the desired exact owner/root partition and an explicit
resident cyclic antecedent.  The second object does **not** act on that
factor.  More precisely:

1. one native Mütze--Standke--Wiechert component is a shortest wreath and is
   completely described by one cyclic coordinate order;
2. the usual label `110u0v <-> 101u0v` is a standard pull in the distinct
   rotational/lexical Middle-Levels factor; its six-cycle has three local
   ports but only two old factor components, with old-edge distribution
   `2+1`;
3. the native MSW factor contains no same-phase directed common-core cycle,
   so in particular it cannot supply the all-six-coherent masked collar
   needed to transfer the published pull to three native wreath histories;
4. the canonical MSW factor is not translation-equivariant.  Consequently
   neither the pull tree nor the factor descends to the necklace quotient by
   a formal voltage argument.

Thus the MSW factor remains a useful exact resident **base factor**, but the
component-spanning buffered-coherent-wreath pull lemma is a genuinely new
theorem, not a corollary of the standard Middle-Levels pull catalogue.

No computation or search is used.

## 1. A native MSW component is one cyclic coordinate order

Put

\[
                     N=2q-1.
\]

For a cyclic permutation

\[
                 w=(w_0,w_1,\ldots,w_{N-1})
\tag{1.1}
\]

of the ground coordinates, define

\[
 O_i=\{w_i,w_{i+1},\ldots,w_{i+q-1}\},\qquad
 Q_i=O_i\cap O_{i+1}
     =\{w_{i+1},\ldots,w_{i+q-1}\}.
\tag{1.2}
\]

The alternating incidence cycle

\[
              O_0,Q_0,O_1,Q_1,\ldots,O_{N-1},Q_{N-1}
\tag{1.3}
\]

is the bipartite lift of a shortest odd-graph wreath.  Conversely, the
omitted-coordinate sequence of a shortest wreath reconstructs (1.1), up to
cyclic shift and reversal.  A canonical MSW component indexed by a Dyck word
`x` has omitted-coordinate word

\[
                 \widehat\rho(x)=(\rho(x),N),
\tag{1.4}
\]

where, for `x=1u0v` and `a=|u|+2`,

\[
 \rho(1u0v)=
 \bigl(a,\ a-\rho(\overline{\operatorname{rev}u}),\ 1,\
       a+\rho(v)\bigr).
\tag{1.5}
\]

This is the precise sense in which the MSW components are Catalan-labelled
minimum wreaths.

For deadline `h-1`, put `s=q-h` and

\[
                         A_i=\{w_i,\ldots,w_{i+s}\}.
\tag{1.6}
\]

Then

\[
                         D^{h-1}A=O.
\tag{1.7}
\]

Every coordinate has an owner run of length `q` and an owner gap of length
`q-1`, hence the native wreath is automatically biresident for every
`h<=q-1`.

At a cut, its cumulative left and right source profiles are

\[
 L_i=K\cup\{\lambda_1,\ldots,\lambda_i\},\qquad
 R_j=K\cup\{\rho_1,\ldots,\rho_j\},
\tag{1.8}
\]

with disjoint ordered exterior banks.  Thus **one** wreath exposes the local
masked tensor.  What is not automatic is coherent alignment of three cuts
belonging to different components.

## 2. What the standard pull actually relates

The standard Middle-Levels pull is labelled

\[
                         x=110u0v,
 \qquad                  p(x)=101u0v.
\tag{2.1}
\]

Writing `y=x0` and `z=p(x)0`, its six vertices are

\[
 y, f(y), f^6(y), f^5(y), z, f(z),
\tag{2.2}
\]

or, literally,

\[
\begin{array}{lll}
 110u0v0,&110u1v0,&100u1v0,\\
 101u1v0,&101u0v0,&111u0v0.
\end{array}
\tag{2.3}
\]

Only three coordinates vary.  If `t=|u|`, they are the coordinates in
positions

\[
                           2,\quad3,\quad t+4.
\tag{2.4}
\]

After deleting the common one-set `K`, the three lower vertices of (2.3)
are the singletons on those active coordinates and the three upper vertices
are their pairwise unions.  Hence (2.3) is exactly the Boolean incidence
hexagon

\[
 Ka-Kab-Kb-Kbc-Kc-Kca-Ka.
\tag{2.5}
\]

### Proposition 2.1 (the standard pull is binary at component level)

In the factor on which (2.1) is a published pull, two of its old selected
hexagon edges belong to `C(y)` and one belongs to `C(z)`.  Therefore the
pull joins exactly two old factor components.  The three lower ports of the
hexagon are not three distinct plane-tree components.

#### Proof

The old selected edges are

\[
       \{y,f(y)\},\qquad
       \{f^6(y),f^5(y)\},\qquad
       \{z,f(z)\}.
\tag{2.6}
\]

The first two are edges of the same factor cycle `C(y)`; the third is an
edge of `C(z)`.  Symmetric difference with (2.3) merges these two cycles.
This is the standard `2+1` pull relation.  \(\square\)

The auxiliary vertices of this pull theory are free plane-tree classes.
They must not be identified with the rooted Dyck labels of the Catalan
family of minimum MSW wreaths.  The rotational/lexical factor cycle may
contain several rotations of a rooted tree and need not have minimum wreath
length.  In particular, a standard pull tree is a theorem about that
factor, not about the native MSW `C_N`-factor.

## 3. Exact collar obstruction on the native MSW factor

A full masked `C_6` collar at three lower ports has the following
unavoidable first-edge form.  Its unchanged exterior incidences all belong
to one phase and insert one common exterior coordinate; the three hexagon
incidences therefore belong to the other phase.  Suppressing the common
exterior produces a directed common-core cycle

\[
 K+a\longmapsto K+a+b,
 \quad K+b\longmapsto K+b+c,
 \quad K+c\longmapsto K+c+a
\tag{3.1}
\]

inside one incidence matching.

### Theorem 3.1 (native same-phase no-go)

Neither of the two canonical MSW incidence matchings contains a directed
common-core cycle.  Consequently the canonical MSW factor contains no
native all-six-coherent full masked `C_6` collar, and no buffered collar
whose protected interface includes the same first exterior incidence at
all three ports.

#### Proof

The two canonical up-maps are the Chung--Feller maps `g` and `g'`.  Both
change a down-step touching height zero into an up-step.  Suppose one of
them maps

\[
                         K+u\mapsto K+u+\sigma(u)
\tag{3.2}
\]

around a directed cycle of active labels.  Let `p` be the least active
coordinate, `r=\sigma(p)`, and let `a` be the predecessor of `p` in the
cycle.  Both `a,r` exceed `p`.  Since the map on `K+a` selects `p`, the
height of the deficient path with up-set `K` immediately before `p` is
zero or one.  Since the map on `K+p` selects the later coordinate `r`, the
extra up-step at `p` raises that same height by two before every later
position.  The required zero-touch at `r` is then impossible.  This is the
least-active-coordinate proof of the canonical same-phase obstruction.

The first-edge form (3.1) would be precisely such a directed cycle, so it
cannot occur.  A buffered collar that retains the common first exterior
stub has the same forced first-edge projection and is excluded as well.
\(\square\)

This theorem does not say that an abstract Boolean `C_6` is absent from the
middle-levels graph.  Such hexagons are abundant.  It says that the three
required old edges cannot all be selected in the same native MSW phase
with the common exterior demanded by the masked collar.

### Corollary 3.2 (the published coherent-pull planting is not an MSW bypass)

The coherent single-pull planting theorem for the rotational canonical
factor remains valid on its stated factor.  It cannot be transferred to
the native MSW minimum-wreath factor by identifying their Dyck or
plane-tree labels.  Its deliberately imported common history is new local
data; it is not the simultaneous native history of three MSW wreath cuts.

## 4. Monodromy and why three formal copies are insufficient

Cutting the three old paths before (2.5) and toggling the hexagon permutes
their tails by

\[
                              \tau=(a\ c\ b).
\tag{4.1}
\]

The opposite orientation gives `tau^{-1}`.  Three formally transported
copies have identity endpoint monodromy exactly when their orientations
all agree.  This does not produce three independent fixed-exterior wreath
slabs: a minimum wreath segment is geodesic, while a nontrivial `tau`
changes its local endpoint set.  With fixed exterior such a slab exists
only when the local endpoint set is `tau`-invariant.  More generally the
number of exterior deletions must equal the number of local labels moved
out by `tau`.

Thus even after abandoning the canonical same-phase gate, a positive
construction would have to be one jointly zero-monodromy packet with all
crossing collars paid, or a genuinely exterior-moving packet.  Three
abstract copies of the Boolean hexagon do not supply that physical
realization.

## 5. Quotient and voltage boundary

For a native shortest wreath with omitted-coordinate order
`c=(c_i)_(i in Z_N)`, normalize a rank-`(q-1)` state `M_i` by its translation
phase `beta_i`.  If `y_i=c_i-beta_i`, then

\[
                   \beta_{i+1}=\beta_i+2y_i,
 \qquad             \sum_i y_i=0.
\tag{5.1}
\]

Hence a nonfixed shortest wreath projects to a closed zero-total-voltage
walk.  A translation-fixed arithmetic-progression wreath instead projects
to repetitions of one quotient loop with nonzero primitive voltage.

This componentwise statement does not make the **canonical factor**
translation-equivariant.  For every nontrivial dimension the translated
omitted-coordinate word of a canonical MSW row need not be another
canonical row; the alternating Dyck row already gives an explicit failure.
For prime `N`, no canonical row is a translation-fixed arithmetic-
progression row.

### Theorem 5.1 (no formal quotient descent)

The canonical MSW factor and the published standard pull tree do not
descend together to a translation-necklace factor.  A quotient construction
must separately choose:

1. the required zero-voltage necklace cycles, together with the exceptional
   arithmetic-progression loops when forced by congruence;
2. a compatible lift of every selected component join; and
3. one global voltage-closing condition after the joins.

#### Proof

The MSW factor is not invariant under the translation action, so its set of
components is not a union of translation orbits.  The standard pull tree is
defined on the distinct rotational/plane-tree factor.  Consequently there
is no common invariant factor on which to project its edges.  Equation
(5.1) only certifies the voltage of an individually chosen native wreath;
it does not identify a quotient pull between two such wreaths.  \(\square\)

## 6. Exact remaining bridge

The MSW route has genuinely solved rows:

* exact owner/root partition;
* minimum cyclic components;
* a literal depth-`(h-1)` antecedent;
* positive and negative residence;
* the complete local masked tensor at every individual cut.

What it has **not** supplied is a component-spanning family of joins whose
three native cyclic orders have a common protected collar.  The exact new
theorem would have to be one of the following.

1. A noncanonical shortest-wreath factor carrying a compatible buffered
   pull hypertree and the required voltage closure.
2. A transfer theorem from the rotational pull factor to shortest wreaths
   that transports the entire ordered collar, not only the six central
   vertices.
3. A new exterior-moving, zero-monodromy multi-pull packet whose crossing
   histories are proved directly.

Absent one of these, the central-wreath observation is a local tensor
simplification, not an all-dimensional `B(k)+O(1)` construction.

