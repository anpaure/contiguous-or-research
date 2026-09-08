# Mixed-conjugate resolution of radius-typed Bender--Knuth blocks

## 0. Status and outcome

This note formulates the coordinate-conjugate mixing problem in one
radius-resolved hypergraph and proves its exact fractional laws.

Proved here:

1. The last-`DU` Bender--Knuth partition has an exponentially strong enough
   large-cell tail to discard only `E=o(W/H)` vertices at every intended
   polynomial depth `H`.
2. After tiling its large cells into radius-pure pair-flip blocks, averaging
   **all ordered coordinate conjugates** gives one simultaneous fractional
   matching on the middle layer and every lower/upper depth.  In the ideal
   no-defect case every typed degree is exactly one.
3. The weighted codegrees have an exact orbit formula.  In particular,
   distinct middle vertices at Johnson distance `r` have codegree at most

   \[
      \frac{R-1}{\binom mr^2},                         \tag{0.1}
   \]

   where `R` is the block length.  Under the intended parameters all
   distinct typed codegrees tend to zero.
4. Two partitions admit only componentwise trades: the overlap incidence
   graph permits no finer Birkhoff mixing.  Hence the uniform fractional
   point cannot be rounded by an automatic pairwise switching argument.

Conjectural:

* the low-cost integral resolution/absorption theorem in Section 8.

Crucially, every real hyperedge below contains one middle block together
with **all** of its certified depths.  No inference is made by separately
matching depth `1`, depth `2`, and so on and then assuming those unrelated
matchings stitch.

The word *radius* needs care.  A coordinate permutation does not preserve
the original fixed-order RSK shape of an individual set.  A conjugated block
instead carries the radius label of its source block.  This transported
label is constant on the block, and the global label multiplicities are the
exact Boolean SCD radius multiplicities.  That is the radius preservation
used here.

## 1. Strengthening the large-cell tail

Write

\[
 W=\binom{2m}{m},\qquad
 a_d=\binom{2m}{m-d}-\binom{2m}{m-d-1}.               \tag{1.1}
\]

The orbitwise partition in `BENDER_KNUTH_SHADOW_BRIDGE.md` divides every
odd-BK orbit into native-pair isometric cells.  In a critical orientation
sequence of length `a`, the cell-dimension deficit `delta` has distribution

\[
 \Pr(\delta=t)=2^{-t}\quad(1\le t<a),
 \qquad
 \Pr(\delta=a)=2^{1-a}.                               \tag{1.2}
\]

Indeed, `delta=t<a` means that the last `DU` is exactly `t` positions from
the right; `delta=a` combines a last `DU` in the first position and the
all-`UD` word.

For any fixed `0<theta<log 2`, (1.2) gives the uniform exponential-moment
bound

\[
 \mathbb E e^{\theta\delta}
 \le \sum_{t\ge1}2^{-t}e^{\theta t}
       +2\sup_{t\ge1}(e^\theta/2)^t
 =:C_\theta<\infty.                                   \tag{1.3}
\]

At radius `d` there are at most `d/2` critical sequences.  Their orientation
coordinates are disjoint, hence independent under the uniform measure on
one odd-BK orbit.  If `Delta` is the total cell deficit, then

\[
 \mathbb E e^{\theta\Delta}\le C_\theta^{d/2}.        \tag{1.4}
\]

Take `D_0=ceil(m^(2/3))`.  The radius tail telescopes and satisfies

\[
 \frac1W\sum_{d>D_0}a_d
 =\frac{\binom{2m}{m-D_0-1}}W
 \le \exp(-\Omega(m^{1/3})).                          \tag{1.5}
\]

The number of tableaux with fewer than `m/8` `DU` blocks is at most

\[
 \sum_{t<m/8}\binom mt3^{m-t}
 \le \exp((\log4-c_0+o(1))m),                         \tag{1.6}
\]

where

\[
 c_0=\log4-H(1/8)-(7/8)\log3
     =0.0482384472\ldots>0.                            \tag{1.7}
\]

Every orbit meeting the complement of (1.6) has at least `m/8` active
directions.  Let `ell=o(m)`.  On an orbit with `d<=D_0` and at least `m/8`
active directions, a cell of dimension below `ell` has

\[
 \Delta>m/8-\ell.
\]

For all sufficiently large `m`, the right side is at least `m/9`.
Chernoff's bound from (1.4) gives

\[
 \Pr(\Delta>m/9)
 \le \exp(-\theta m/9+O(m^{2/3}))
 =\exp(-\Omega(m)).                                   \tag{1.8}

Combining (1.5), (1.6), and (1.8) proves:

### Theorem 1 (strong large-cell resolution)

For every `ell=o(m)`, the native BK orbit partition has a family of cells
of dimension at least `ell` covering all but

\[
 E\le W\exp(-\Omega(m^{1/3}))                         \tag{1.9}

middle vertices.  In particular,

\[
 HE=o(W)                                               \tag{1.10}

for every `H=exp(o(m^(1/3)))`, including all parameter scales used in the
central-band program.

This improves the earlier Markov estimate only in its error rate; the cells
remain confined to the one native coordinate matching.

## 2. A base radius-resolved block partition

Choose a power of two `ell` with

\[
 H<\ell=o(m),\qquad R=2\ell.                          \tag{2.1}

By `LINEAR_CYCLE_TILING.md`, every isometric cube of dimension at least
`ell` partitions into pair-flip cycles of length `R`.  Apply this inside
every cell retained by Theorem 1.  We obtain a family `mathcal B` of
vertex-disjoint middle blocks, leaving the exceptional set of size `E`.

Each block `B` inherits one transported radius `d(B)`, has cyclically ordered
middle vertices

\[
 X_0(B),\ldots,X_{R-1}(B),                            \tag{2.2}
\]

and, for every `q<=min(d(B),H)`, has the two sets of cyclic shadows

\[
 \begin{aligned}
 L_q(t;B)&=\bigcap_{j=0}^{q}X_{t+j}(B),\\
 U_q(t;B)&=\bigcup_{j=0}^{q}X_{t+j}(B)
 \end{aligned}\qquad(t\in\mathbb Z/R\mathbb Z).       \tag{2.3}

Because `q<ell` and the cycle flips distinct coordinate pairs locally, the
`R` lower shadows in (2.3) are distinct within `B`, and so are the `R`
upper shadows.

Let

\[
 g_d=\#\{X\in\cup\mathcal B:d(B_X)=d\},
 \qquad e_d=a_d-g_d,                                  \tag{2.4}

where `B_X` is the unique base block containing `X`.  Then

\[
 \sum_de_d=E,
 \qquad
 G_q:=\sum_{d\ge q}g_d=N_q-\sum_{d\ge q}e_d,          \tag{2.5}

with `N_q=binom(2m,m-q)`.

## 3. The full conjugate reservoir

Let `G=S_(2m)` act on every mask by coordinate permutation.  For
`pi in G` and `B in mathcal B`, transport the entire decorated block:

\[
 e(\pi,B)=
 \pi\{X_t(B):t\in\mathbb Z/R\mathbb Z\}
 \ \cup
 \bigcup_{q\le\min(d(B),H)}
 \pi\{L_q(t;B),U_q(t;B):t\in\mathbb Z/R\mathbb Z\}.  \tag{3.1}

The copies of equal-rank masks are regarded as separate typed vertex
classes:

\[
 \Omega_0=\binom{[2m]}m,
 \quad
 \Omega_q^-=\binom{[2m]}{m-q},
 \quad
 \Omega_q^+=\binom{[2m]}{m+q}.                       \tag{3.2}

Thus (3.1) is one hyperedge of size

\[
 R(1+2\min(d(B),H)).                                  \tag{3.3}

It is essential to average the complete ordered pairing frames, equivalently
the full symmetric group.  Averaging bare perfect matchings without their
pair order and within-pair orientations does not make the inherited RSK
radius labels uniform.

Give every occurrence `(pi,B)` weight

\[
 x(\pi,B)=1/|G|.                                      \tag{3.4}

Repeated decorated edges are retained as parallel occurrences; this avoids
irrelevant stabilizer divisions.

### Theorem 2 (simultaneous conjugate degree law)

For every middle vertex `X`,

\[
 \deg_x(X)=\frac{W-E}{W}.                             \tag{3.5}

For every target `S in Omega_q^-` or `S in Omega_q^+`,

\[
 \deg_x(S)=\frac{G_q}{N_q}.                           \tag{3.6}

More finely, the weighted degree at a fixed middle vertex coming from
radius-`d` blocks is exactly

\[
 \deg_{x,d}(X)=g_d/W.                                 \tag{3.7}

In the ideal case `E=0`, equations (1.1) and (2.5) make every degree in
every typed class exactly one.  Hence (3.4) is an exact fractional perfect
matching simultaneously through all depths `1,...,H`.

### Proof

The symmetric group is transitive on each typed class.  Total weighted
middle incidence equals

\[
 \sum_{\pi,B}\frac1{|G|}|B|=\sum_B|B|=W-E.
\]

It is uniform over `W` middle vertices, proving (3.5).  Restricting the same
count to radius `d` gives (3.7).

A block of radius at least `q` contributes exactly `R` targets of either
sign at depth `q`.  The total number of such occurrences in the base system
is therefore `G_q`.  Transitivity on the target layer of size `N_q` proves
(3.6).  When `E=0`, `g_d=a_d=N_d-N_(d+1)`, so the telescoping identity gives
`G_q=N_q`.  QED.

This is the precise fractional escape from the fixed-native-pair capacity
obstruction: after full conjugation, every individual target has the right
degree at every depth.

## 4. Exact singleton completion and its cost

Adjoin a singleton repair edge for every typed vertex.  Give a middle
singleton weight `E/W`, and give every singleton in either depth-`q` target
class weight

\[
 1-G_q/N_q.                                           \tag{4.1}

Together with (3.4), these weights form an exact fractional perfect matching
of the augmented hypergraph.  If real blocks have cost zero and repair
singletons cost one, its total fractional repair cost is

\[
 \begin{aligned}
 C_{\rm frac}
 &=E+2\sum_{q=1}^H(N_q-G_q)\\
 &=E+2\sum_{q=1}^H\sum_{d\ge q}e_d
 \le(2H+1)E=o(W).                                    \tag{4.2}
 \end{aligned}

Thus there is no density, radius-quota, or divisibility obstruction even in
the actual system with small cells removed.  The unresolved issue is the
integrality gap of this exact-cover LP.

## 5. Exact conjugate codegrees

The diagonal action of `G` partitions ordered pairs of typed vertices into
orbits.  Let `mathcal O` be one such orbit, and for a base edge put

\[
 c_{\mathcal O}(B)
 =\#\{(u,v)\in e(B)^2:(u,v)\in\mathcal O\}.           \tag{5.1}

### Theorem 3 (orbit codegree formula)

For any fixed `(u,v) in mathcal O`, its weighted codegree is

\[
 \codeg_x(u,v)=\frac1{|\mathcal O|}
                 \sum_{B\in\mathcal B}c_{\mathcal O}(B). \tag{5.2}

### Proof

For every base ordered pair in `mathcal O`, exactly
`|G|/|mathcal O|` permutations send it to `(u,v)`.  Multiply by the weight
`1/|G|` and sum over all base pairs.  QED.

For two distinct middle vertices at Johnson distance `r`, the orbit has
size

\[
 W\binom mr^2.                                        \tag{5.3}

There are at most `(W-E)/R` base blocks, and one block contains at most
`R(R-1)` ordered distinct middle pairs.  Equations (5.2)--(5.3) give (0.1).

There are similarly useful coarse consequences.  For a fixed middle set,
every orbit of rank-`m-q` or rank-`m+q` sets has at least `binom(m,q)`
members.  Hence a middle--depth-`q` codegree is at most

\[
 \frac{R}{\binom mq}\le\frac Rm.                     \tag{5.4}

For two distinct shallow target types that actually co-occur in a base
edge, the smallest relevant diagonal orbit has at least `Omega(m)`
continuations from a fixed first target.  Here it matters that one block
varies only its chosen `ell=o(m)` coordinate pairs: every one of its typed
vertices contains the same fixed core of size at least `m-ell`.  Thus the
complementary, one-continuation orbits of two near-middle layers have zero
numerator in (5.2).

More explicitly, if the two target ranks are `k,l` and their intersection
has size `a`, then the number of continuations from a fixed first target is

\[
 \binom{k}{a}\binom{2m-k}{l-a}.                     \tag{5.5a}
\]

For `k,l in [m-H,m+H]`, the only ways (5.5a) can equal one are the diagonal
same-set orbit (`k=l=a`) and the complementary orbit (`a=0,k+l=2m`).  The
first is excluded for two distinct vertices of one typed class, and two
different target classes never have the same rank.  The second has zero
base numerator because co-occurring targets share the nonempty fixed core.
Every remaining feasible orbit has at least `m-H=Omega(m)` continuations;
the smallest cases are one-element nested extensions.  Since

\[
 \frac{W}{N_H}=\exp(H^2/m+o(1))                       \tag{5.5}

uniformly for `H=o(m^(2/3))`, the same pair count gives the conservative
bound

\[
 O\!\left(\frac{R\exp(H^2/m+o(1))}{m}\right).         \tag{5.6}

Thus all distinct typed codegrees are `o(1)` whenever

\[
 R\exp(H^2/m)=o(m).                                   \tag{5.7}

For example, `R=m^(3/4+o(1))` and
`H=sqrt(m omega(m))` satisfy (5.7) when `omega(m)->infinity` sufficiently
slowly, such as `omega=o(log m)` with the corresponding quantitative
margin.

The exact formula (5.2), rather than the coarse bound (5.6), is the correct
input to any future nibble theorem.  Small codegree alone does not supply
the additive `o(W)` error required here.

## 6. Why ordinary Birkhoff mixing does not apply

At the middle-only level, (3.4) is literally the average of integral block
partitions.  Once shadows are included, an individual conjugate block
partition is generally **not** a matching: distinct blocks can repeat the
same lower or upper target.  Hence (3.4) is not a convex combination of
integral typed matchings, and the Birkhoff--von Neumann theorem says nothing
about its rounding.

There is also an exact obstruction to mixing two middle partitions by local
whole-cell trades.

### Theorem 4 (two-partition trade rigidity)

Let `mathcal P` and `mathcal Q` be two partitions of a finite vertex set
`V`.  Form their bipartite overlap multigraph `Gamma`: its left vertices are
the cells of `mathcal P`, its right vertices are the cells of `mathcal Q`,
and every `v in V` gives one edge joining its two containing cells.

A selection of whole cells from `mathcal P union mathcal Q` covers every
vertex exactly once if and only if, independently on each connected
component of `Gamma`, it selects all left cells and no right cells, or all
right cells and no left cells.

### Proof

Give a selected left cell variable `x_P in {0,1}` and a selected right cell
variable `y_Q`.  Exact coverage of the vertex represented by edge `PQ` is

\[
 x_P+y_Q=1.                                           \tag{6.1}

Along any path in `Gamma`, equations (6.1) force all left variables to one
common value and all right variables to its complement.  Conversely either
of the two componentwise choices satisfies every edge.  QED.

In particular, if the overlay is connected, the only exact resolutions are
the two original partitions.  Fine mixing therefore needs at least three
systems, a deliberately disconnected overlay, temporary uncovered vertices,
or genuine multi-block absorbers.  Convex averaging by itself creates none
of these trades.

## 7. The bundled radius ledger

Suppose an integral matching chooses real decorated blocks and some repair
singletons.  Let `n_d` be the number of selected middle vertices carried by
radius-`d` real blocks.  Every real radius-`d` middle start supplies exactly
one lower and one upper slot at every `q<=min(d,H)`.  Therefore the cumulative
radius discrepancy at depth `q` is exactly accounted for by the repair
singletons in the two depth-`q` target classes.

A sufficient standalone middle-radius condition is

\[
 \sum_{d=0}^m(\min(d,H)+1)|n_d-a_d|=o(W),             \tag{7.1}

but the augmented hypergraph makes (7.1) unnecessary as a separate
matching: all depths and the middle assignment are already coupled inside
one edge.  This is why the scheme does not commit the invalid operation of
constructing unrelated matchings at successive depths.

## 8. The exact missing absorption theorem

Let `mathscr H_(m,H,ell)` be the augmented decorated multihypergraph of
Sections 3--4, and give real conjugate blocks cost zero and singleton repair
edges cost one.

### Mixed-Conjugate Resolution Conjecture

For some parameters

\[
 H=\sqrt{m\,\omega(m)},\quad \omega(m)\to\infty,
 \qquad H<\ell=o(m),                                  \tag{8.1}

the hypergraph `mathscr H_(m,H,ell)` has an integral perfect matching of
repair cost `o(W)`.

Equivalently, one can choose vertex-disjoint blocks from many coordinate
conjugates so that the middle layer and every certified lower and upper
layer are all covered, apart from `o(W)` total literal repairs.

The fractional optimum has cost `o(W)` by (4.2), and all distinct typed
codegrees may be made `o(1)` by (5.7).  What is not proved is an
`o(W)` additive integrality gap.  The typed universe has
`Theta(W sqrt m)` vertices, so a standard `1-o(1)` near-matching could leave
`o(W sqrt m)`, far too many.  The largest real edge has size

\[
 R(1+2H),                                             \tag{8.2}

which also grows with `m`.

A sufficient theorem would be a cost-sensitive nibble plus absorption
statement of the following form:

> Every `S_(2m)`-averaged block system satisfying the orbit degree law
> (3.5)--(3.7), codegree formula (5.2), and a bounded family of higher-order
> orbit tests admits a perfect matching whose singleton cost is at most the
> fractional singleton cost plus `o(W)`.

No available theorem has been verified with the required growing edge size,
the exponentially many target vertices, and this additive error.

## 9. Concrete next mathematical directions

1. **Three-conjugate absorbers.**  Classify the smallest connected
   configurations of blocks from three ordered pairing frames whose middle
   vertices and every typed shadow have two exact resolutions.  Theorem 4
   shows why two-frame alternating components are insufficient.
2. **Association-scheme sparsification.**  Sample only enough conjugates to
   retain the exact orbit degrees approximately, using (5.2) to control all
   pair orbits rather than all individual targets.  Then reserve a second,
   independent conjugate sample for absorbers.
3. **Costed fractional-to-integral duality.**  Search for a nonnegative dual
   weighting that separates integral matchings from (3.4).  The exact degree
   law rules out every obstruction depending only on one typed vertex or one
   radius class; any counterexample must detect higher-order overlap.
4. **Vary direction catalogs before rounding.**  Each conjugated cube admits
   many choices of its `ell` active directions and linear-code transversal.
   These choices should be included as parallel real edges.  Fixing one
   cyclic order in advance reintroduces the catalog obstruction from
   `BENDER_KNUTH_SHADOW_BRIDGE.md`.
5. **Absorb the radius ledger once.**  Any absorber must exchange complete
   decorated blocks, not just a lower shadow at one depth.  Its two
   resolutions must agree simultaneously on the middle vertices and all
   depth classes outside the absorber.

## 10. Final ledger

| statement | status |
|---|---|
| strong BK large-cell error `E<=W exp(-Omega(m^(1/3)))` | proved |
| conjugated middle and radius-typed degree laws | proved |
| exact diagonal-orbit codegree formula | proved |
| fixed-pair capacity bias disappears fractionally | proved |
| two-partition trades are component-rigid | proved |
| all depths are bundled in every real edge | by construction |
| integral resolution with `o(W)` repair cost | conjectural |
| asymptotic universal OR construction from this scheme | conditional on the conjecture plus the proved tail/linearization steps |

The big-picture gain is a clean separation.  Coordinate conjugation fully
repairs the native-pair bias at the fractional level and preserves the exact
radius ledger.  The remaining obstacle is a single correlated,
cost-sensitive integral resolution problem—not a missing scalar capacity
identity and not a collection of independently solvable depth matchings.
