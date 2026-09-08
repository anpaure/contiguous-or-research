# Shadow projections of the fixed-pair cube tiling

This note audits the Boolean-specific Stage-B route in Section 8 of
`MIDDLE_BLOCK_FACTOR.md`.  Fix a perfect matching of the `2m` ground
coordinates and decompose the middle layer into orientation cubes.  The main
conclusions are as follows.

* Every depth-`q` shadow window in an orientation cube is exactly an
  axis-parallel `q`-face.  Its lower and upper shadows are the two endpoints
  of a regular inclusion graph, and this graph has an exact perfect matching.
  Thus every fixed depth has an exact two-sided fractional and integral
  assignment before the cube-tiling constraint is imposed.
* For `ell=2^t`, the partial-cycle tile has a completely explicit linear
  translate tiling of `Q_ell`; no appeal to the very large threshold in
  Gruslys' theorem is needed.  A finite-field choice makes this tiling
  **face-simple** at every depth `q<=t=log_2 ell`.
* The translate construction cannot be face-simple substantially deeper:
  its quotient has dimension only `t+1`.
* Independently randomizing one cube tiling in every source stratum does not
  solve Stage B.  Even assuming the optimal face-simple property, a typical
  rank-`m-q` target has mean occurrence

  ```text
                     exp(-(1+o(1)) q^2/m),
  ```

  in the fixed-pair model.  In particular a positive proportion is missed
  for `q=o(sqrt(m))`, while for `q/sqrt(m)->infinity` almost every typical
  target is missed.  This is a stronger obstruction than the ordinary
  Poisson calculation for unrestricted random pair-flip blocks.
* More strongly, the same pair-type ledger is a deterministic capacity
  obstruction.  If `q/sqrt(m)->infinity`, **every** block factor confined
  to one fixed coordinate matching misses `1-o(1)` of the corresponding
  target layer, however its source-cube tilings are coupled.  Useful
  literal-tail depth therefore requires mixing coordinate matchings or a
  different global architecture.
* There is a rigorous sparse absorber: one prescribed shadow face in every
  `ell`-dimensional fibre can be forced while retaining an exact cycle
  tiling.  It is useful for a genuinely sparse final defect, but its capacity
  is far too small to replace the required near-rainbow main construction.

The fixed-pair decomposition therefore remains a valid exact Stage-A factor,
but its Stage B must be deliberately coupled across source cubes.  Independent
random automorphisms, even with the best possible local face multiplicity,
move in the wrong direction at growing depth.

## 1. Orientation cubes and shadow faces

Write the fixed coordinate pairs as

\[
             \mathcal P=\{P_1,\ldots,P_m\},\qquad |P_i|=2.
\]

A middle set has `f` full pairs, `f` empty pairs, and `s=m-2f` split
pairs.  After the full, empty, and split index sets have been fixed, its
remaining choices form an orientation cube `Q_s`.

Fix an axis-parallel `q`-face `F` of this cube.  Let `Q` be its `q` free
pair coordinates, and keep the orientations of the other split pairs fixed.
The two Boolean masks associated with the face are

\[
 \partial^-F:\text{ make every pair in }Q\text{ empty},
 \qquad
 \partial^+F:\text{ make every pair in }Q\text{ full}.
 \tag{1.1}
\]

### Proposition 1 (face-shadow dictionary)

If `q<ell`, every `q+1`-term window in a partial `2ell`-cycle is a
geodesic path which flips `q` different orientation coordinates.  The affine
span of the path is a `q`-face `F`, and its intersection and union are
respectively

\[
                         \partial^-F,\qquad\partial^+F.       \tag{1.2}
\]

Conversely, after an ordering and a starting orientation of its free
coordinates have been chosen, every `q`-face is the affine span of a
geodesic `q`-path and can be extended to a partial `ell`-cycle whenever the
ambient orientation cube has dimension at least `ell`.

#### Proof

Each flipped coordinate pair contributes neither of its two ground
coordinates to the intersection and both to the union.  An unflipped split
pair contributes its fixed selected coordinate to both.  Full and empty
pairs outside the orientation cube remain unchanged.  This proves (1.2).

For the converse, order the `q` free directions arbitrarily, add
`ell-q` other cube directions, and use these as consecutive directions in
the standard pair-flip cycle.  A cube translation chooses the desired
starting corner.  QED.

## 2. Exact occurrence counts

Let `L` be a lower target of rank `m-q`.  Suppose it has

\[
 f\text{ full pairs},\qquad e=f+q\text{ empty pairs},
 \qquad r=m-2f-q\text{ split pairs}.                         \tag{2.1}
\]

To obtain a source orientation cube, choose `q` of the empty pairs and make
them free split pairs.  Thus `L` has exactly

\[
                  d_{f,q}=\binom{f+q}{q}                    \tag{2.2}
\]

candidate source faces.  They lie in distinct source strata, all of common
dimension

\[
                         s=r+q=m-2f.                         \tag{2.3}
\]

The same count holds dually for an upper target of rank `m+q`.

The number of lower targets of type `f` is

\[
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.                  \tag{2.4}
\]

Consequently

\[
          \sum_f T_{f,q}=\binom{2m}{m-q}.                   \tag{2.5}
\]

There is an exact type-capacity law.  Let

\[
 V_f=\frac{m!}{f!f!(m-2f)!}\,2^{m-2f}                       \tag{2.6}
\]

be the number of middle vertices in all source strata having `f` full,
`f` empty, and `s=m-2f` split coordinate pairs.  Any cyclic block factor
supplies exactly one depth-`q` starting window per one of these vertices.
Every such window has a lower target of type `f`; dually its upper target
has the paired type coming from the same source `f`.

### Proposition 2A (fixed-pair type capacity)

Every block factor confined to the fixed coordinate matching misses at least

\[
                    \sum_f (T_{f,q}-V_f)_+                  \tag{2.7}
\]

rank-`m-q` targets.  The same bound holds for rank `m+q`.  Moreover,

\[
 \frac{T_{f,q}}{V_f}
 =\frac{(m-2f)_{\underline q}}
        {2^q(f+1)^{\overline q}}
 =\left(
       \frac{2^q\binom{f+q}{q}}
            {\binom{m-2f}{q}}
   \right)^{-1}.                                           \tag{2.8}
\]

#### Proof

There are only `V_f` physical starts of source type `f`, independently of
the chosen tilings.  Distinct targets need distinct window occurrences,
which proves (2.7).  Dividing (2.4) by (2.6) proves (2.8).  QED.

### Proposition 2 (exact two-sided pairing at every depth)

For every fixed `q`, one may select candidate source faces so that every
rank-`m-q` target and every rank-`m+q` target occurs exactly once, paired
by the same selected face.  Restricted to split-data classes whose source
dimension `s` is at least `ell`, the same statement holds using only faces
which can be extended to partial `ell`-cycles.  The classes with `s<ell`
are exactly the individually nonrepresentable exceptional types from
Proposition 4 of `MIDDLE_BLOCK_FACTOR.md`.

#### Proof

Fix the split pair set, its orientations, and write `T` for the remaining
pair indices.  If a lower target has `f` full pairs, then

\[
                         |T|=2f+q.                           \tag{2.9}
\]

Lower targets with this split data are indexed by the `f`-subsets of `T`;
upper targets are indexed by the `(f+q)`-subsets.  A common source `q`-face
exists precisely for an inclusion

\[
                   F\in\binom Tf,\quad G\in\binom T{f+q},
                   \quad F\subset G.                        \tag{2.10}
\]

The bipartite inclusion graph in (2.10) is regular on both sides, of degree
`binom(f+q,q)`, so it has a perfect matching.  A matched inclusion uses the
free pair set `G-F`; (1.1) gives exactly the corresponding lower and upper
targets.  Perform this independently for every split set and orientation.
QED.

Proposition 2 generalizes the depth-one colour pairing in Proposition 5 of
`MIDDLE_BLOCK_FACTOR.md`.  It proves that there is no target-count or Hall
obstruction at one depth after the sparse nonextendable types are removed.
The missing condition is that the selected faces at all depths must be
consecutive windows of one common vertex tiling.

Proposition 2A explains why this realization condition is substantive: the
perfect face assignment can overload the physical windows of a source type
even though the untyped inclusion graph has a perfect matching.

## 3. An explicit translate tiling

Let

\[
                         \ell=2^t.                           \tag{3.1}
\]

Work in `V=F_2^ell`, with standard basis `e_1,...,e_ell`, and put

\[
 p_0=0,\qquad p_i=e_1+\cdots+e_i,
 \qquad
 P=\{p_i,\mathbf1+p_i:0\le i<\ell\}.                       \tag{3.2}
\]

The set `P` is the vertex set of the standard induced `2ell`-cycle.

Let `U=F_2^t x {0}`, choose `v` outside `U`, and enumerate `U` as

\[
                 u_0=0,u_1,\ldots,u_{\ell-1}.                \tag{3.3}
\]

Define the linear map

\[
 \phi:V\longrightarrow U\oplus\langle v\rangle
\]

by

\[
 \phi(e_i)=u_i+u_{i-1}\quad(1\le i<\ell),
 \qquad
 \phi(e_\ell)=v+u_{\ell-1}.                                \tag{3.4}
\]

Then

\[
             \phi(p_i)=u_i,qquad
             \phi(\mathbf1+p_i)=v+u_i.                      \tag{3.5}
\]

Hence `phi` maps `P` bijectively onto its entire codomain.  If

\[
                             K=\ker\phi,                     \tag{3.6}
\]

then addition induces a bijection `K x P -> V`.

### Theorem 3 (explicit exact Stage-A tiling)

The translates

\[
                             \{P+k:k\in K\}                  \tag{3.7}
\]

partition `Q_ell` into isometric copies of the partial pair-flip cycle.
Fibering over the remaining coordinates gives such a partition of `Q_s` for
every `s>=ell`.

This replaces the nonquantitative Gruslys threshold for this particular
tile.  It is an exact algebraic construction.

## 4. Exact face multiplicities of the translate tiling

Let `I` be a cyclic interval of `q<ell` coordinate directions and put

\[
 V_I=\operatorname{span}\{e_i:i\in I\},\qquad
 r_I=\dim(K\cap V_I),
 \qquad
 \delta_I=\mathbf1_{\{v\in\phi(V_I)\}}.                    \tag{4.1}
\]

For one of the two half-cycle occurrences, the faces are

\[
                         p_a+k+V_I\qquad(k\in K).             \tag{4.2}
\]

Two values of `k` give the same face exactly when their difference lies in
`K cap V_I`.  The other half-cycle gives their translates by `1`; the two
families coincide exactly when `1 in K+V_I`, equivalently when
`v in phi(V_I)`.

### Proposition 4 (multiplicity formula)

For the direction interval `I`, the number of distinct `q`-faces is

\[
 \begin{cases}
  2|K|/2^{r_I},&\delta_I=0,\\
  |K|/2^{r_I},&\delta_I=1.
 \end{cases}                                               \tag{4.3}
\]

Their occurrence multiplicity is respectively `2^{r_I}` or
`2^{r_I+1}`.

There is a choice of the enumeration (3.3) which is optimally simple at
logarithmic depth.  Identify `U` with the field `F_(2^t)`, take a primitive
element `alpha`, and set

\[
                   u_0=0,qquad u_i=\alpha^{i-1}
                   \quad(1\le i<\ell).                       \tag{4.4}
\]

The columns of `phi` are then

\[
 c_1=1,qquad
 c_i=(\alpha+1)\alpha^{i-2}\ (2\le i<\ell),
 \qquad
 c_\ell=v+\alpha^{-1}.                                     \tag{4.5}
\]

### Theorem 5 (logarithmic-depth face simplicity)

For (4.4), every cyclic interval `I` of length `q<=t` satisfies

\[
                       r_I=0,\qquad\delta_I=0.               \tag{4.6}
\]

Consequently every depth-`q` window in the translate tiling spans a different
`q`-face, simultaneously for all `q<=log_2 ell`.

#### Proof

An interval not meeting the last column consists either of consecutive
multiples of

\[
                  1,\alpha,\ldots,\alpha^{q-1},              \tag{4.7}
\]

or of `1` followed by consecutive vectors
`(alpha+1)alpha^j`.  A dependence would give a nonzero polynomial in
`alpha` of degree at most `q-1<t`, impossible because the minimal
polynomial of `alpha` has degree `t`.

If the interval contains `c_ell`, its outside-`U` component makes that
column independent of the other `q-1` columns.  Multiplying a hypothetical
dependence among those other columns by a suitable power of `alpha` again
gives a polynomial of degree at most `q-1`; its support has one missing
monomial at the join between the suffix and prefix.  It cannot vanish.

Finally, `v` could lie in the span only if the `U`-component
`alpha^{-1}` of `c_ell` lay in the span of the remaining columns.  After the
same multiplication, this would require

\[
             (x+1)P(x)=x^a(B+Cx)                            \tag{4.8}
\]

with the coefficient of `x^a` forbidden in `P`.  If `B ne C`, the right
side is not divisible by `x+1`; if `B=C=1`, division gives precisely the
forbidden monomial.  Thus no such dependence exists.  This proves (4.6).
QED.

The logarithmic range is intrinsic to this linear-coset construction.  Its
quotient has dimension `t+1`, so an interval space of dimension
`q>t+1` necessarily meets `K` nontrivially.  Changing the enumeration can
optimize the sliding ranks, but cannot remove this rank obstruction.

## 5. Randomly automorphized tilings: the exact ledger

Let `mathcal T_s` be any tiling of `Q_s` by the cycle, and let
`D_{s,q}` be the number of **distinct** `q`-faces spanned by its depth-`q`
windows.  There are `2^s` window occurrences and

\[
                     2^{s-q}\binom sq                         \tag{5.1}
\]

axis-parallel `q`-faces.  Put

\[
                     \gamma_{s,q}=D_{s,q}/2^s.               \tag{5.2}
\]

For notational convenience set `gamma_(s,q)=0` when `s<ell`, since no
partial `ell`-cycle lies in that source cube.

Within one tile the `q`-faces are distinct for `q<ell`.  If several tiles
span the same face, their geodesic paths are vertex-disjoint and each uses
`q+1` vertices.  Therefore

\[
 \frac1{\lfloor2^q/(q+1)\rfloor}
       \le\gamma_{s,q}\le1.                                 \tag{5.3}
\]

The upper bound is attained by the construction of Theorem 5 through depth
`log_2 ell`.  In particular every tiling is face-simple at depths one and
two.

Apply an independent uniform cube automorphism to the tiling in every source
stratum.  A fixed `q`-face in dimension `s` is then covered with probability

\[
              p_{s,q}=\gamma_{s,q}
                 \frac{2^q}{\binom sq}.                      \tag{5.4}
\]

The candidate faces of a fixed target lie in distinct source strata, so the
events are independent.  Combining (2.2)--(2.4) gives the exact expectation

\[
 \boxed{
 \mathbb E M_q^-=
 \sum_f T_{f,q}
 \left(1-\gamma_{m-2f,q}
              \frac{2^q}{\binom{m-2f}{q}}
 \right)^{\binom{f+q}{q}}.}                                 \tag{5.5}
\]

Here the summand is interpreted as `T_(f,q)` when `m-2f<ell`, since those
source cubes do not contain an `ell`-cycle.  The same formula holds for upper
targets.  Even the optimistic choice
`gamma=1` does not make (5.5) small.

## 6. The pair-type bias obstruction

For a uniformly random rank-`m-q` target, let `F` be its number of full
coordinate pairs.  The mass function is (2.4), and its continuous saddle is

\[
              f_* =\frac{(m-q)^2}{4m}.                       \tag{6.1}
\]

The variance of `F` is `O(m)`: write it as a sum of the indicators that a
fixed coordinate pair is fully selected and use the standard negative
dependence of sampling without replacement.  Thus `F=f_*+O_p(sqrt(m))`.

Even for a face-simple tiling, the expected number of occurrences of a type
`f` target is at most

\[
 \lambda_{f,q}=
       \frac{2^q\binom{f+q}{q}}{\binom{m-2f}{q}}.             \tag{6.2}
\]

At the saddle (6.1), direct expansion of the product in (6.2) gives

\[
 \log\lambda_{f_*,q}
 =-\frac{q^2}{m}
   +O\left(\frac qm+\frac{q^3}{m^2}\right).                 \tag{6.3}
\]

Moreover, throughout the central type range,

\[
       \left|\frac{\partial}{\partial f}
                 \log\lambda_{f,q}\right|=O(q/m).           \tag{6.4}
\]

Equations (6.1)--(6.4) imply the following.

### Theorem 6 (deterministic fixed-pair depth barrier)

Let `q=o(ell)`, `ell=o(m)`, with `q/sqrt(m)->infinity` and
`q=O(sqrt(m log m))`.  Every partial-cycle factor constructed entirely
inside the orientation cubes of one fixed coordinate matching misses

\[
                  (1-o(1))\binom{2m}{m-q}                    \tag{6.5}
\]

targets of rank `m-q`, and likewise of rank `m+q`.

#### Proof

Choose a diverging type window of width `a_m sqrt(m)` such that

\[
             a_mq/\sqrt m=o(q^2/m).                          \tag{6.6}
\]

It contains `1-o(1)` of the targets.  Equations (6.3)--(6.4) give

\[
                    \lambda_{f,q}
          =\exp(-(1+o(1))q^2/m)=o(1)                        \tag{6.7}
\]

throughout this window.  By (2.8), source type `f` contains only
`V_f=lambda_(f,q)T_(f,q)` physical starts for its `T_(f,q)` targets.
Proposition 2A therefore forces a missing fraction `1-o(1)` on a family
containing `1-o(1)` of the target layer.  Concatenating the cycles creates
at most `q` new depth-`q` windows per seam.  There are `O(W/ell)` seams, so
these contribute only `O(qW/ell)=o(W)` additional targets and do not change
the conclusion.  QED.

In particular, no coupling, trade, or absorption performed solely among the
source cubes of one fixed coordinate matching can reach the
`Theta(sqrt(m log m))` depth required by literal-tail completion.  Different
coordinate matchings must be mixed at the block level, or the construction
must leave the fixed-pair architecture.

### Theorem 7 (independent-randomization barrier)

Assume `q<ell=o(m)` and every tileable source-stratum tiling is independently
uniformly automorphized.

1. If `q=o(sqrt(m))`, then

   \[
             \mathbb E M_q^\pm
             \ge(e^{-1}-o(1))\binom{2m}{m-q}.                \tag{6.8}
   \]

2. If `q/sqrt(m)->infinity` and
   `q=O(sqrt(m log m))`, then

   \[
             \mathbb E M_q^\pm
             =(1-o(1))\binom{2m}{m-q}.                       \tag{6.9}
   \]

Both statements remain true if the local tilings have repeated shadow faces.

#### Proof

For `q=o(sqrt(m))`, choose a type window of width
`a_m sqrt(m)`, where `a_m->infinity` and
`a_mq/sqrt(m)->0`.  It contains `1-o(1)` of the targets.  Equations
(6.3)--(6.4) give `lambda<=1+o(1)` there.  The one-face probability in
(5.4) is `o(1)`, so the exact miss probability in (5.5) is at least
`e^{-1-o(1)}`.

If `q/sqrt(m)->infinity`, take any diverging type window still satisfying
`a_mq/sqrt(m)=o(q^2/m)`.  On `1-o(1)` of the targets,

\[
                 \lambda_{f,q}
        =\exp(-(1+o(1))q^2/m)=o(1).                          \tag{6.10}
\]

The probability of being covered is at most the expected occurrence count,
so (6.9) follows.  Repeated local faces only decrease (5.4).  QED.

The sign in (6.3) is important.  In the unrestricted symmetric block family,
the average target occurrence is
`binom(2m,m)/binom(2m,m-q)=exp(+q^2/m+o(1))`.
Inside one fixed coordinate-pair decomposition, typical targets instead have
the inverse-scale occurrence (6.3); rare pair types carry the excess average.
Thus averaging over automorphisms of separate source cubes is severely
nonuniform at the exact depth where random outer-shadow coverage was supposed
to help.

## 7. A sparse prescribed-face absorber

The explicit tiling does have one useful extension property.

### Lemma 8 (one face per fibre)

Let `A` be an `ell`-element set of coordinate directions in `Q_s`.  Partition
`Q_s` into its `2^{s-ell}` affine `A`-fibres.  In each fibre prescribe at
most one face, of any dimension `q<=ell`, whose free directions lie in `A`.
Then `Q_s` has a tiling by partial `2ell`-cycles in which every prescribed
face is spanned by a consecutive geodesic window.

#### Proof

In a fibre containing a prescribed face, extend a geodesic path across that
face to a full partial cycle, as in Proposition 1.  Any two copies of the
standard cycle in `Q_ell` are related by a cube isometry.  Apply such an
isometry to the entire translate tiling (3.7), mapping one of its tiles to
the prescribed cycle.  This tiles the fibre and contains the desired window.
Use the unmodified translate tiling in fibres without a prescription.  The
fibres are disjoint, so their tilings combine.  QED.

The lemma can absorb `2^{s-ell}` arbitrary prescribed faces in one source
cube when they share a carrier direction set and occupy different fibres.
This is only a `2^{-ell}`-scale correction relative to the `2^s` main
windows.  It is therefore a legitimate final absorber, but not a substitute
for the near-rainbow main tiling required by shallow shadows.

## 8. Exact remaining target

The fixed-pair program has now separated into three statements.

1. **Solved Stage A.**  Theorem 3 gives an explicit exact cycle factor of
   every sufficiently split orientation cube, with threshold `s>=ell`.
2. **Solved one-depth incidence.**  Proposition 2 chooses a perfect set of
   paired lower/upper faces at every depth separately.
3. **Unsolved simultaneous realization.**  Choose these perfect face
   assignments coherently so that, in every source cube, they are the
   consecutive faces of one common partial-cycle tiling, up to `o(W)` total
   defects; then use Lemma 8 to absorb the sparse remainder.

Theorem 7 rules out obtaining item 3 by independently randomizing arbitrary
Gruslys or translate tilings.  More decisively, Theorem 6 says that item 3 is
itself impossible at useful growing depth while all blocks use the same
coordinate matching.  A successful global proof must mix coordinate
matchings so that a target which is an over-capacity pair type in one matching
can be routed through a balanced type in another.  The exact perfect
matchings of Proposition 2 and the sparse extension in Lemma 8 remain useful
local ingredients for that mixed-matching theorem.

## 9. A polynomial reservoir of coordinate matchings removes the local bias

The deterministic obstruction is attached to one fixed coordinate matching,
not to the target itself.  A small reservoir of different matchings already
removes it at the incidence level.

Fix a target `S` of rank `m-q`, and choose a uniformly random perfect
matching `mathcal P` of the `2m` ground coordinates.  Let `F_P(S)` be the
number of matching edges lying wholly inside `S`.  Its exact distribution is

\[
 \Pr(F_{\mathcal P}(S)=f)=
 \frac{
  \binom{m-q}{2f}(2f-1)!!
  \binom{m+q}{m-q-2f}(m-q-2f)!
  (2f+2q-1)!!
 }{(2m-1)!!}.                                             \tag{9.1}
\]

Its mean differs by `O(1)` from the saddle `f_*` in (6.1), and its
standard deviation is `Theta(sqrt(m))`.  Stirling's formula applied to
(9.1) gives, uniformly for

\[
                  |f-f_*|=O(\sqrt{m\log m}),                 \tag{9.2}
\]

the coarse local lower bound

\[
             \Pr(F_{\mathcal P}(S)=f)
             \ge m^{-C_0}                                  \tag{9.3}
\]

for a constant `C_0` depending only on the constant implicit in (9.2).

Since `lambda_(f,q)` is increasing in `f`, (6.3)--(6.4) show that

\[
                 f\ge f_*+q/3+O(1)
       \quad\Longrightarrow\quad \lambda_{f,q}\ge1          \tag{9.4}
\]

uniformly for `q=O(sqrt(m log m))`; the harmless constant deals with the
bounded values of `q` and integer rounding.

### Proposition 9 (polynomial favourable-matching reservoir)

For every fixed `C`, there is a polynomial-size family

\[
                  \mathcal P_1,\ldots,\mathcal P_J,
                  \qquad J=m^{O_C(1)},                       \tag{9.5}
\]

of perfect coordinate matchings such that, for every mask `S` with

\[
             ||S|-m|\le C\sqrt{m\log m},                    \tag{9.6}
\]

at least one `mathcal P_j` gives `S` a source type satisfying
`lambda_(f,q)>=1`.

#### Proof

For a fixed target, (9.3)--(9.4) give probability at least `m^{-C_1}`
that a random matching is favourable, for a constant `C_1=C_1(C)`.
Choose `J=m^{C_1+2}` independent matchings.  The probability that a fixed
target has no favourable matching is at most `exp(-m^2)`.  There are fewer
than `4^m` masks and fewer than `2m` relevant ranks, so a union bound is less
than one for large `m`.  Hence a deterministic reservoir exists.  QED.

Proposition 9 is not yet a block factor: taking whole factors from all `J`
matchings would repeat every middle set `J` times, while taking arbitrary
blocks can create overlaps and holes.  Its role is to identify a viable next
global theorem:

> select disjoint algebraic blocks from a polynomial reservoir of exact
> fixed-matching factors, covering all but `o(W)` middle sets, while routing
> each shadow target through a matching in which its pair type is favourable.

The explicit translate factors supply a resolvable block reservoir and
Lemma 8 supplies sparse local absorption.  What remains is the mixed-factor
rounding theorem; the single-matching cube-tiling problem should no longer be
treated as capable of reaching the full central band.

## 10. Update: the mixed reservoir is fractionally sufficient

The local statement in Proposition 9 has now been upgraded.  If an
`s`-split stratum is given block weight `2/(s)_ell`, its middle degree is
exactly one and the normalized degree of a depth-`q` target of pair type `f`
is exactly

\[
 \lambda_{f,q}
 =\frac{2^q(f+q)_q}{(m-2f)_q}.
\]

Writing `pi_q(f)` for the random-matching type law of a rank-`m-q` target,
one has the exact size-bias identity

\[
             \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f).
\]

After a balanced-type truncation, a polynomial family of coordinate
matchings therefore supports simultaneously an arbitrarily accurate typed
fractional perfect matching in every required central rank.  Its weighted
pair-codegree is `O(1/m)`.

This closes the fractional mixed-factor problem, but not integral rounding.
The typed edges have average size `Theta(ell sqrt(m))=m omega(1)` in the
application, and projective planes show that degree plus `O(1/m)` relative
pair-codegree alone cannot force a large matching at such growing
uniformity.  The remaining theorem must use the fact that every block is a
necklace of disjoint symmetric-chain segments.  Complete statements and
proofs are in `MIXED_PAIR_ROUNDING.md`.
