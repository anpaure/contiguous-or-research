# Fixed-depth two-sided shadows at asymptotic width

This note strengthens the adjacent-shadow theorem in
`ASYMPTOTIC_MATCHING.md`.  It is purely asymptotic and uses no finite search.

Write

\[
 W=\binom{2m}{m}.
\]

The main result is the following.

> **Fixed-depth theorem.**  For every fixed integer `J>=1`, there is a
> sequence `T` of middle `m`-sets of `[2m]`, of length `W+o_J(W)`, such that
> every middle set occurs and, for every `1<=q<=J`,
> \[
> \left\{\bigcap_{s=0}^{q}T_{i+s}\right\}_i
>     \supseteq \binom{[2m]}{m-q},
> \qquad
> \left\{\bigcup_{s=0}^{q}T_{i+s}\right\}_i
>     \supseteq \binom{[2m]}{m+q}.
> \tag{0.1}
> \]
> Moreover `T` may be chosen so that every internal coordinate `1`-run has
> length at least `J+1`.

The last assertion is the fixed-delay run condition needed for a factorization
`T=D^J A`.  The theorem is only for fixed `J`; the proof is not uniform when
`J` grows with `m`.  In particular, it does not yet give the depth
`Theta(sqrt(m log m))` needed to discard all but `o(W)` literal tails.

There is nevertheless a rate-free diagonal consequence: some function
`J(m)->infinity` can be chosen so slowly that all conclusions above hold
simultaneously through depth `J(m)` with length `W+o(W)`.  Nothing in the
argument gives a useful lower bound on that function.

There are two parts to the argument.  First, the most direct attempt to add
deeper-shadow conflicts to the directed version of the cloned 4-graph is
audited and shown to fail a Delcourt--Postle codegree hypothesis.  Second, a
different fixed-uniformity hypergraph, whose edges are long cyclic Johnson
blocks, avoids that obstruction and yields the theorem by an ordinary
almost-perfect-matching theorem.

## 1. The directed-edge formulation

Let

\[
 \mathcal L_1=\binom{[2m]}{m-1},\qquad
 \mathcal U_1=\binom{[2m]}{m+1},
\]

and let `mathcal M^out,mathcal M^in` be two role clones of the middle layer.
For every directed Johnson edge `X->Y`, put one 4-edge

\[
 e(X,Y)=\{X^{\rm out},Y^{\rm in},X\cap Y,X\cup Y\}.              \tag{1.1}
\]

A matching projects to a directed graph with indegree and outdegree at most
one.  It is rainbow in both adjacent colour systems.  The exact degrees are

\[
 d(S)=d(U)=m(m+1),\qquad
 d(X^{\rm out})=d(X^{\rm in})=m^2,                                \tag{1.2}
\]

and the maximum pair codegree is `m`.  Thus this directed 4-graph has the same
asymptotic regularity and small-codegree properties as the undirected cloned
4-graph.

A directed path

\[
 X_0\to X_1\to\cdots\to X_q                                   \tag{1.3}
\]

is called **geodesic** when `d_J(X_0,X_q)=q`.  Equivalently, no coordinate is
changed twice along the path.  In that case

\[
 \left|\bigcap_{i=0}^q X_i\right|=m-q,qquad
 \left|\bigcup_{i=0}^q X_i\right|=m+q.                             \tag{1.4}
\]

The converse holds if both equalities in (1.4) hold.

Two consecutive selected arcs are automatically geodesic.  Indeed, a
two-step non-geodesic walk either removes the element just inserted, thereby
repeating its lower `(m-1)` colour, or reinserts the element just removed,
thereby repeating its upper `(m+1)` colour.  In either case the two lifted
4-edges are not disjoint.  Consequently the first non-geodesic-path conflicts
have size three, not size two.

For fixed `J`, the natural configuration hypergraph on the directed 4-edges
would contain:

1. every inclusion-minimal non-geodesic directed `q`-path, `3<=q<=J`;
2. the union of two distinct geodesic `q`-paths having the same lower or
   upper `q`-shadow, `2<=q<=J`; and
3. short directed cycles, in order to leave only few components after cycle
   breaking.

Path ordering and orientation cause no ambiguity: the in/out clones make a
selected component a directed path or a directed cycle.  All the listed
configurations are included only when their lifted-edge union is a
submatching of the directed 4-graph, as required in the definition of a
configuration hypergraph.  Two colliding `q`-windows that overlap in `q-s`
arcs give a conflict of size `q+s`; two disjoint windows give one of size
`2q`.  Thus these conflicts have sizes from `q+1` through `2q`.  There is no
size-two collision conflict: depth one is already enforced by the colour
vertices, while at depth at least two two distinct windows use at least three
arcs.  A directed 2-cycle repeats both adjacent colours and is not a
submatching, so the cycle conflicts also start at size three.  Hence the
maximum common 2-degree of the configuration hypergraph and its maximum
2-codegree with the base 4-graph are both zero.

## 2. Exact obstruction to the direct conflict route

The short-cycle conflicts have the same bounds as in
`ASYMPTOTIC_MATCHING.md`.  Minimal non-geodesic path conflicts also have the
right scale.  If a non-geodesic path is inclusion-minimal, every coordinate
reversal responsible for non-geodesicity joins its first and last transition.
After any proper fixed subpath is prescribed, completing a minimal bad path
either joins prescribed endpoints or forces one transition coordinate.  Thus,
with `D=Theta(m^2)`, their fixed-subconfiguration counts have the power saving

\[
 O_J(D^{q-\ell-1/2})                                                \tag{2.1}
\]

for `2<=ell<q`; their ordinary conflict degree is
`O_J(D^{q-1})`.  Since there are no size-two conflicts, the two extra
2-degree conditions in the Delcourt--Postle theorem vanish.

The projection-collision conflicts do **not** satisfy the required
codegree bound.  This is a genuine obstruction, not a loose count.

### Proposition 1 (collision-codegree obstruction)

Fix `q>=2` and one geodesic directed `q`-path `P`, with lower shadow

\[
 S=\bigcap_{X\in P}X\in\binom{[2m]}{m-q}.
\]

There are

\[
 \Theta_q(m^{2q})=\Theta_q(D^q)                                   \tag{2.2}
\]

geodesic directed `q`-paths `P'` with lower shadow `S` such that the lifted
edges of `P union P'` form a matching.  Therefore the configuration family
of equal-lower-shadow pairs satisfies

\[
 \Delta_{2q,q}\ge c_qD^q,                                         \tag{2.3}
\]

whereas the Delcourt--Postle small-codegree theorem requires, for some fixed
`beta>0`,

\[
 \Delta_{2q,q}\le D^{q-\beta}.                                    \tag{2.4}
\]

The same obstruction holds for upper shadows.

#### Proof

A geodesic path with lower shadow `S` is specified, up to a constant depending
only on `q`, by choosing `q` old elements and `q` new elements outside `S`,
and ordering the removals and insertions.  After avoiding the `O_q(1)` extra
coordinates used by `P`, there remain `Theta(m)` choices at every one of the
`2q` coordinate selections.  This gives (2.2).

Choose the two `2q`-element supports disjoint outside `S`.  Then the middle
vertices are different, all adjacent lower and upper colours are different,
and the in/out clones are different.  Hence the union is a matching in the
directed 4-graph.  Fixing all `q` lifted edges of `P` leaves the
`Theta(D^q)` choices for `P'`, proving (2.3).  QED.

The obstruction survives passage to inclusion-minimal collision conflicts:
the second support can be chosen generically so that no smaller-depth shadow
collision occurs.  Thus the direct instruction

\[
 \text{“add all deeper-shadow collisions as conflicts”}
\]

cannot be justified by the Delcourt--Postle theorem used for the adjacent
case.  The ordinary degree estimates are large but admissible; it is exactly
the `(2q,q)` codegree that fails.

## 3. A locally geodesic cyclic block

Fix integers

\[
 \ell>J,\qquad R=2\ell.                                            \tag{3.1}
\]

Choose a middle set `X`, an ordered tuple of distinct elements

\[
 a_0,\ldots,a_{\ell-1}\in X,
\]

and an ordered tuple of distinct elements

\[
 b_0,\ldots,b_{\ell-1}\notin X.
\]

Starting at `X`, first perform the swaps

\[
 a_0\mapsto b_0,\ a_1\mapsto b_1,\ldots,
 a_{\ell-1}\mapsto b_{\ell-1},                                    \tag{3.2}
\]

and then perform the reverse-direction swaps in the same pair order

\[
 b_0\mapsto a_0,\ b_1\mapsto a_1,\ldots,
 b_{\ell-1}\mapsto a_{\ell-1}.                                    \tag{3.3}
\]

This gives a cyclic sequence

\[
 X_0,X_1,\ldots,X_{R-1},X_R=X_0.                                  \tag{3.4}
\]

Let

\[
 C=X\setminus\{a_0,\ldots,a_{\ell-1}\}.
\]

At every time the current set is `C` together with exactly one member of each
pair `{a_i,b_i}`.  Pair `i` is flipped at transition `i` and again at
transition `ell+i`.

### Lemma 2 (all fixed-depth block shadows are exact and distinct)

For every `1<=q<=J` and every cyclic starting position `t`, put

\[
 L^q_t=\bigcap_{s=0}^qX_{t+s},\qquad
 U^q_t=\bigcup_{s=0}^qX_{t+s}.                                    \tag{3.5}
\]

Then

\[
 |L^q_t|=m-q,qquad |U^q_t|=m+q.                                  \tag{3.6}
\]

For fixed `q`, the `R` sets `L^q_t` are pairwise distinct, and the `R` sets
`U^q_t` are pairwise distinct.  The `R` middle sets `X_t` are also pairwise
distinct.

#### Proof

Any `q<ell` consecutive transitions flip `q` different pairs.  The lower
shadow contains neither member of each flipped pair and one member of each
unflipped pair; the upper shadow contains both members of each flipped pair
and one member of each unflipped pair.  This proves (3.6).

The set of pair labels flipped in a window is a cyclic interval of length `q`
in `Z/ell Z`; since `q<ell`, it determines `t mod ell`.  Positions `t` and
`t+ell` have opposite choices on every unflipped pair.  At least one pair is
unflipped, so their lower shadows differ and their upper shadows differ.
Thus `t mod 2ell` is determined.  The same orientation-vector description
shows that the middle states are distinct.  QED.

Every active coordinate has a cyclic `1`-run of length exactly `ell`; every
coordinate in `C` is present throughout the block.  Thus the cyclic block
already has coordinate runs longer than `J`.

## 4. The block hypergraph

For fixed `J,ell`, define a multihypergraph `B_{m,ell,J}`.  Its vertex classes
are

\[
 \mathcal M=\binom{[2m]}m,
 \qquad
 \mathcal L_q=\binom{[2m]}{m-q},
 \qquad
 \mathcal U_q=\binom{[2m]}{m+q}quad(1\le q\le J).                 \tag{4.1}
\]

For every parameter choice `(X,(a_i),(b_i))` above, insert the hyperedge

\[
 \{X_t:0\le t<R\}
 \cup
 \bigcup_{q=1}^J\{L^q_t:0\le t<R\}
 \cup
 \bigcup_{q=1}^J\{U^q_t:0\le t<R\}.                              \tag{4.2}
\]

Different parameter choices are retained as parallel edges.  Lemma 2 shows
that every edge has exactly

\[
 r=R(1+2J)                                                         \tag{4.3}
\]

vertices.  Here `r` is fixed while `m` tends to infinity.

For completeness, parallelism is inessential.  The middle vertices of one
parameter edge induce the cycle `C_(2ell)` in the `ell`-cube of pair
orientations: they are precisely the cyclic-interval binary words.  Hence the
unordered middle-vertex set recovers the cyclic order up to a dihedral choice,
and then recovers the transition coordinate pairs.  The multiplicity of one
underlying hyperedge is therefore `O_ell(1)`.  One may either use the standard
multihypergraph form of the nibble or discard parallel copies; all degree and
codegree estimates change by bounded factors only.

Let `(m)_ell=m(m-1)...(m-ell+1)`.  The number of parameter edges is

\[
 e(\mathcal B)=W(m)_\ell^2.                                       \tag{4.4}
\]

The symmetric group on `[2m]` acts transitively on every class and preserves
the parameter family.  Since each block contains exactly `R` vertices from
each class, double counting gives

\[
 d_{\mathcal M}=R(m)_\ell^2,                                      \tag{4.5}
\]

and, writing `N_q=binom(2m,m-q)=binom(2m,m+q)`,

\[
 d_{\mathcal L_q}=d_{\mathcal U_q}
     =R(m)_\ell^2\frac{W}{N_q}.                                   \tag{4.6}
\]

For fixed `J`,

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
 =1+O_J(m^{-1}).                                                   \tag{4.7}
\]

Consequently `B_{m,ell,J}` is `(1+O_J(1/m))D`-regular, where

\[
 D=\max_vd(v)=\Theta_{\ell,J}(m^{2\ell}).                          \tag{4.8}
\]

### Lemma 3 (small pair codegree)

For fixed `J,ell`,

\[
 \Delta_2(\mathcal B_{m,\ell,J})
     =O_{\ell,J}(m^{2\ell-1})=O_{\ell,J}(D/m)=o(D).               \tag{4.9}
\]

#### Proof

Label the `R(1+2J)` positions in (4.2).  Fix two positions and two distinct
target vertices `V,W` of the corresponding ranks.  Once the first position
is fixed to `V`, a compatible block is specified by `2ell` active coordinate
choices, up to a constant depending only on `ell,J`; all other coordinates
form the unchanged core.  There are `O_{ell,J}(m^{2ell})` such choices.

If the second position is `W`, then every coordinate on which the two slot
values differ belongs to the active support.  Compatibility implies that this
difference has size `O_{ell,J}(1)`, and it is nonempty because the two
vertices are distinct (or the two ranks differ).  Hence at least one of the
`2ell` active choices is forced to lie in a fixed `O_{ell,J}(1)`-set instead
of a set of size `Theta(m)`.  This leaves

\[
 O_{ell,J}(m^{2ell-1})
\]

parameters.  Summing over the bounded number of ordered slot pairs proves
(4.9).  QED.

This slot argument also covers pairs in different rank classes.  If their
set difference is too large to fit in the `2ell`-coordinate active support,
their codegree is zero.

## 5. Almost-perfect block packing

The fixed-uniformity Pippenger--Frankl--Rodl almost-perfect matching theorem
applies to `B_{m,ell,J}` by (4.7)--(4.9).  Hence, for fixed `J,ell`, there is
a matching of cyclic blocks covering all but

\[
 o_{J,ell}(W)                                                       \tag{5.1}
\]

vertices of the whole block hypergraph.  In particular, it leaves
`o_{J,ell}(W)` uncovered vertices in each one of the finitely many classes.

If the matching has `t` blocks, its middle-class coverage gives

\[
 tR=W-o_{J,ell}(W).                                                 \tag{5.2}
\]

Because the selected hyperedges are disjoint, their depth-`q` lower shadows
are all distinct globally, and so are their depth-`q` upper shadows, for every
`q<=J`.

Notice what changed relative to Section 2.  A whole cyclic block, rather than
one Johnson edge, is now one matching edge.  Equality of a deeper colour is
enforced by literal intersection in the corresponding rank class, so the
bad `Delta_{2q,q}` collision family never arises.

## 6. Linearization and exact repair

For every selected cyclic block, output

\[
 X_0,X_1,\ldots,X_{R-1},X_0,X_1,\ldots,X_{J-1}.                   \tag{6.1}
\]

The repeated prefix linearizes every cyclic window of at most `J+1` middle
sets.  The total length of these words is

\[
 t(R+J)=W+\frac JRW+o_{J,ell}(W).                                  \tag{6.2}
\]

Append every uncovered middle set literally.

For an uncovered lower target `S` of rank `m-q`, choose disjoint ordered
`q`-tuples

\[
 a_1,\ldots,a_q, b_1,\ldots,b_q\notin S
\]

and append the geodesic path

\[
 Y_t=S\cup\{a_{t+1},\ldots,a_q\}\cup\{b_1,\ldots,b_t\},
 \qquad 0\le t\le q.                                               \tag{6.3}
\]

Its intersection is `S`.  For an uncovered upper target `U` of rank `m+q`,
choose an `(m-q)`-subset `S` of `U`, partition `U-S` into two ordered
`q`-tuples, and use (6.3); its union is `U`.

There are only `o_{J,ell}(W)` uncovered vertices in all classes, and every
repair costs at most `J+1` entries.  Hence the repair cost is
`o_{J,ell}(W)`.

We have proved, for every fixed `J` and every fixed `ell>J`, a sequence of
length

\[
 \left(1+\frac{J}{2\ell}\right)W+o_{J,ell}(W)                     \tag{6.4}
\]

with all the shadow properties in (0.1).

Now first choose `ell` arbitrarily large and then let `m` tend to infinity.
A standard diagonal choice `ell=ell(m)->infinity` sufficiently slowly makes
both `J/(2ell)` and the fixed-`ell` matching error tend to zero.  This proves
the length assertion `W+o_J(W)`.

One may diagonalize once more over `J`.  For stage `s`, take `J=s` and, for
example, `ell=s^2`, and then choose a threshold beyond which the relative
uncovered fraction is at most `1/s^3`.  Since every repair together with its
run padding costs `O(s)`, its total relative cost is then `O(1/s^2)`, while
the block-cut padding costs `O(J/ell)=O(1/s)`.  Using stage `s` until the next
threshold defines a rate-free function `J(m)->infinity` and still has total
length `W+o(W)`.  This does not make the result quantitative at a prescribed
growing depth.

No global cycle-breaking theorem is needed: every selected cycle is cut and
linearized separately.  The number of cuts is

\[
 t=\frac{W}{2\ell}+o(W),                                          \tag{6.5}
\]

and therefore their total fixed-depth cost is `o(W)` under the same diagonal
choice.

## 7. Enforcing the coordinate-run condition

Inside a raw cyclic block, every nonconstant coordinate `1`-run has length
`ell>J`.  A short run can be created only by cutting a block or joining two
output words.

Before concatenation, prepend `J` extra copies of the first middle set of
every block word and append `J` extra copies of its last middle set.  Then any
run meeting a seam has length at least `J+1`; internal runs retain length at
least `ell`.  This costs at most

\[
 2Jt=O(JW/ell)=o(W).                                                \tag{7.1}
\]

Do the same at the two ends of every repair gadget.  Along (6.3), every
coordinate is present on a prefix, on a suffix, throughout, or nowhere, so
the endpoint padding makes every internal positive run have length at least
`J+1`.  Literal uncovered-middle repairs are treated as constant one-vertex
gadgets.  Since there are `o(W)` repairs, their padding also costs `o(W)`.

Padding does not destroy any already existing witness window.  This proves
the run-strengthened form of the fixed-depth theorem.

## 8. Consequence for a fixed central band

Let the padded row have length `L=W+o_J(W)` and satisfy the run condition.
Take its maximal delay-`J` factor of length `L+J`, namely

\[
 A_j=\bigcap_{i=\max(1,j-J)}^{\min(L,j)}T_i,
 \qquad 1\le j\le L+J.                                            \tag{8.1}
\]

The run condition is exactly the factorability criterion, so `D^J A=T`.
Every shadow witness constructed above lies inside a padded gadget and may be
chosen away from the two global boundaries.  There the erosion identity gives

\[
 \bigvee_{s=0}^{J-q}A_{i+s}
   =\bigcap_{t=i-q}^{i}T_t                                         \tag{8.2}
\]

for `0<=q<=J`, while

\[
 D^{J+q}A=D^qT.                                                     \tag{8.3}
\]

After retaining the explicit witness locations supplied above, this yields a
length `W+o_J(W)` OR sequence covering every rank in the fixed band

\[
 m-J,m-J+1,\ldots,m+J.                                             \tag{8.4}
\]

If a maximal-factor entry is empty, delete it after all witnesses have been
formed.  Deleting zero entries preserves the OR of every nonzero witnessing
interval, so the zero-free length only decreases.

This is a genuine fixed-band construction theorem.  It is not yet a universal
OR array of asymptotic width: for fixed `J`, the masks outside (8.4) have
total size much larger than `W`.  To obtain a full `W+o(W)` construction by
literal tails, one needs `J` of order at least `sqrt(m log m)`.  The matching
theorem used above has fixed uniformity

\[
 r=2ell(1+2J),
\]

and gives no quantitative threshold uniform in such a growing `J`.

There is a second, structural loss of uniformity at that scale.  Formula
(4.7) is asymptotic to one only for fixed `q`; in general

\[
 \frac{N_q}{W}=\exp\!\left(-\Theta(q^2/m)\right).
\]

At `q=Theta(sqrt(m log m))`, the outer shadow classes are polynomially smaller
than the middle class.  A block using the same `R` slots from every rank then
has polynomially different vertex degrees, so even a growing-uniformity
version of the same nibble would not apply directly.  Reaching the tail scale
requires rank-dependent block occupancies or a genuinely multiscale packing,
not merely a quantitative sharpening of the fixed-`J` theorem.

## 9. Final audit

The following statements are proved here.

1. The direct directed-edge conflict formulation is well defined and has no
   size-two non-geodesicity conflicts.
2. Its deeper projection-collision conflicts violate the precise
   Delcourt--Postle `(2q,q)` codegree hypothesis by a factor `D^beta` for
   every `beta>0`.
3. Packaging a long cyclic swap block as one hyperedge produces a fixed-
   uniformity, asymptotically regular hypergraph with pair codegree `o(D)`.
4. An almost-perfect matching of those blocks gives simultaneous complete
   intersection and union shadows through every fixed depth `J`, after
   `o(W)` repairs.
5. Cutting, repair, and coordinate-run padding all cost `o(W)` after a slow
   diagonal choice of the block length.
6. A second diagonal gives an unspecified depth `J(m)->infinity`, but not the
   `Theta(sqrt(m log m))` depth needed for the full problem.

What remains open is a rank-balanced multiscale version at growing depth, and
beyond that the full pin-surviving/global-growth-diagram problem.  The
fixed-depth shadow obstruction itself is now removed.

## 10. The precise multiscale successor

The degree calculation identifies the right next hypergraph.  If a cyclic
block has `R` middle slots, then a packing of about `W/R` blocks should expose
not `R`, but approximately

\[
 c_q=R\frac{N_q}{W}                                                \tag{10.1}
\]

designated depth-`q` lower slots and the same number of upper slots.  Indeed,

\[
 \frac WRc_q=N_q,                                                  \tag{10.2}
\]

and the corresponding vertex degree becomes

\[
 \frac{e(\mathcal B)c_q}{N_q}
   =\frac{e(\mathcal B)R}{W},                                     \tag{10.3}
\]

exactly matching the middle-class degree.  Floors and ceilings in (10.1)
can be handled by finitely many block types or slot clones.

For the full paired-swap cycle `R=2m` and
`q=Theta(sqrt(m log m))`, the smallest relevant `c_q` can still be a positive
power of `m` if the band constant is chosen below one, while the omitted
binomial tail is already `o(W)`.  The total number of designated slots over
all central depths is

\[
 R\left(1+2\sum_q\frac{N_q}{W}\right)=\Theta(m^{3/2}).             \tag{10.4}
\]

Thus a rank-balanced growing-uniformity matching/design theorem for these
blocks would be an asymptotically optimal route.  The obstacle is now exact:
prove an almost-perfect packing for this `Theta(m^{3/2})`-uniform structured
hypergraph (or construct a resolvable analogue explicitly) while controlling
cross-rank codegrees.  Equal occupancy at every depth cannot solve the
growing-band problem; the capacities (10.1) are forced by counting.
