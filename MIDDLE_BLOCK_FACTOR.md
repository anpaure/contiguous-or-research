# Partial pair-flip blocks: exact geometry, codegrees, and a rate-free packing

This note addresses Stage A of `RANK_BALANCED_BLOCKS.md`.  It contains no
claim about the simultaneous shadow assignment of Stage B.

Put

\[
        W=\binom{2m}{m}.
\]

The main conclusions are:

* a pair-flip block is exactly a fixed core plus the half-intervals of a
  cyclically ordered active set;
* for every `2 <= ell < m`, the **geometric** block hypergraph is regular and
  has the exact relative codegree
  \[
       \frac{\Delta _2}{D}=\frac{2}{m^2};
  \]
* fixed-uniformity matching plus a diagonal argument gives disjoint partial
  blocks covering all but `o(W/h)` middle sets for some
  \[
       h\longrightarrow\infty,\qquad h=o(\ell),\qquad \ell=o(m);
  \]
* cyclic linearization and seam padding then cost only `o(W)`.

There is also a more structural proof of the Stage-A packing.  After fixing
one perfect matching of the coordinate set, the middle layer splits into
disjoint orientation cubes.  A theorem of Gruslys on vertex decompositions
of high-dimensional cubes tiles every sufficiently large orientation cube
exactly by partial pair-flip cycles whenever `ell` is a power of two.  Only
an exponentially small collection of low-dimensional strata is left.  This
removes the growing-uniformity matching issue from Stage A itself.

This is a genuine rate-free growing-depth Stage-A theorem.  It is not a
packing at the prescribed depth `Theta(sqrt(m log m))`, and it does not solve
the cross-block shadow collisions of Stage B.

## 1. Geometric form of a partial pair-flip block

Fix `2 <= ell <= m`.  Choose

\[
 X\in\binom{[2m]}m,
 \quad (a_0,\ldots,a_{\ell-1})\in X^{\underline\ell},
 \quad (b_0,\ldots,b_{\ell-1})\in (X^c)^{\underline\ell},
 \tag{1.1}
\]

where the underline denotes an ordered tuple of distinct elements.  Starting
at `X`, perform

\[
 a_0\mapsto b_0,\ldots,a_{\ell-1}\mapsto b_{\ell-1},
 b_0\mapsto a_0,\ldots,b_{\ell-1}\mapsto a_{\ell-1}.
 \tag{1.2}
\]

This produces a cyclic sequence of `R=2 ell` middle sets.

Let

\[
 C=X\setminus\{a_0,\ldots,a_{\ell-1}\},\qquad
 P=(a_0,a_1,\ldots,a_{\ell-1},b_0,b_1,\ldots,b_{\ell-1}).
 \tag{1.3}
\]

Reading subscripts of `P` modulo `2 ell`, the block is exactly

\[
 \boxed{
 B(C,P)=
 \left\{
 C\cup\{P_i,P_{i+1},\ldots,P_{i+\ell-1}\}:
 i\in\mathbb Z/(2\ell)\mathbb Z
 \right\}.}
 \tag{1.4}
\]

Thus it is a fixed `(m-ell)`-set core plus all cyclic half-intervals of a
`2 ell`-element active set.  Conversely, every family (1.4) is produced by
(1.1)--(1.2).

The middle sets in (1.4) induce a chordless `2 ell`-cycle in the Johnson
graph.  Indeed two starts at cyclic separation `s` have Johnson distance

\[
       \min\{s,2\ell-s\}.
 \tag{1.5}
\]

Consequently, for `ell >= 2`, the unordered family (1.4) recovers its cyclic
order up to rotation and reversal.  Every geometric block therefore has
exactly

\[
                         4\ell                         \tag{1.6}
\]

parameterizations of the form (1.1): `2 ell` choices of the distinguished
start and two directions.

When `ell=m`, (1.4) is precisely the family of the `2m` consecutive
`m`-intervals in a cyclic ordering of `[2m]`, hence a tight Hamilton cycle of
the complete `m`-uniform hypergraph on `[2m]`.  It is not a Baranyai--Katona
wreath in the non-coprime convention: for `(n,k)=(2m,m)` such a wreath has
only `n/gcd(n,k)=2` members.

## 2. Exact degree

Let `H_(m,ell)` be the simple hypergraph whose vertices are the `W` middle
sets and whose edges are the distinct geometric blocks (1.4).  The number of
parameter triples (1.1) is

\[
                 W(m)_\ell^2.                              \tag{2.1}
\]

By (1.6),

\[
 |E(H_{m,\ell})|=\frac{W(m)_\ell^2}{4\ell}.                 \tag{2.2}
\]

The symmetric group on `[2m]` acts transitively on the middle layer and on
the parameter family.  Since every block has `2 ell` vertices, double
counting incidences gives the exact common degree

\[
 \boxed{D_{m,\ell}=\frac{(m)_\ell^2}{2}.}                   \tag{2.3}
\]

## 3. Exact pair codegrees

Let `X,Y` be distinct middle sets and put

\[
                   q=d_J(X,Y)=|X\setminus Y|.               \tag{3.1}
\]

If `q>ell`, no partial block contains both sets.  Suppose first that
`1 <= q < ell`.  In the unique direction in which `Y` is reached from `X`
after `q` transitions, the first `q` removal coordinates are exactly
`X-Y`, and the first `q` insertion coordinates are exactly `Y-X`.  Their
orders may be chosen in `q!` ways each.  The remaining `ell-q` removal
coordinates are an ordered selection from `X cap Y`, and the remaining
insertion coordinates are an ordered selection from `(X union Y)^c`.
Both of those sets have size `m-q`.  Hence

\[
 d(X,Y)=\left[q!(m-q)_{\ell-q}\right]^2,
                    \qquad 1\le q<\ell.                    \tag{3.2}
\]

If `q=ell`, the two sets are opposite vertices of the active cycle.  Both
orientations starting at `X` reach `Y` after `ell` steps, so division by two
is necessary:

\[
 d(X,Y)=\frac{(\ell!)^2}{2},
                    \qquad q=\ell.                         \tag{3.3}
\]

Dividing (3.2)--(3.3) by (2.3) yields

\[
 \frac{d(X,Y)}{D_{m,\ell}}
 =
 \begin{cases}
 \displaystyle\frac{2}{\binom mq^2},&1\le q<\ell,\\[6pt]
 \displaystyle\frac{1}{\binom m\ell^2},&q=\ell,\\[6pt]
 0,&q>\ell.
 \end{cases}                                                \tag{3.4}
\]

Therefore, whenever `2 <= ell < m`,

\[
 \boxed{\Delta _2(H_{m,\ell})
       =\frac{2}{m^2}D_{m,\ell}.}                           \tag{3.5}
\]

The maximum is attained by Johnson-adjacent middle sets.  In particular,
the earlier slot bound `O(D/m)` loses a full factor of `m`.

For `ell=m`, the exceptional pair `Y=X^c` has codegree `D`: every full
cycle containing `X` also contains `X^c`.  Collapsing each complementary
pair to one vertex removes exactly this obstruction.  The quotient block
hypergraph is `m`-uniform, has degree `(m!)^2/2`, and for two distinct
quotient vertices at folded Johnson distance `q` has codegree

\[
             [q!(m-q)!]^2,
 \qquad
 \frac{d(P,Q)}D=\frac{2}{\binom mq^2}.                       \tag{3.6}
\]

Thus its relative maximum codegree is again exactly `2/m^2`.

## 4. What the standard matching theorem proves

For every **fixed** `ell >= 2`, the uniformity `2 ell` is fixed,
`H_(m,ell)` is exactly regular, and (3.5) tends to zero.  The
Pippenger--Frankl--Rodl almost-perfect-matching theorem therefore gives a
matching of partial blocks covering

\[
                          W-o_\ell(W)                       \tag{4.1}
\]

middle sets.

This statement can be diagonalized without pretending that the theorem is
uniform in a growing edge size.

### Theorem 1 (rate-free growing partial-block factor)

There are integer functions `h=h(m)` and `ell=ell(m)` and a matching
`M_m` in `H_(m,ell)` such that

\[
 h\to\infty,\qquad \frac h\ell\to0,\qquad \frac\ell m\to0, 
 \tag{4.2}
\]

and the number `u_m` of uncovered middle sets satisfies

\[
                         h u_m=o(W).                        \tag{4.3}
\]

#### Proof

For stage `s`, set

\[
                  h_s=s,\qquad \ell_s=s^2.                 \tag{4.4}
\]

Apply the fixed-`ell_s` matching theorem with error at most `s^{-3}`.
Choose a threshold `M_s`, increasing in `s`, beyond which such a matching
exists, and enlarge it if necessary so that `M_s >= s^3`.  For
`M_s <= m < M_(s+1)`, use the stage-`s` matching.  Then

\[
 \frac{h_s}{\ell_s}=\frac1s,
 \qquad
 \frac{\ell_s}{m}\le\frac1s,
 \qquad
 \frac{h_su_m}{W}\le\frac1{s^2}.                            \tag{4.5}
\]

As `m` tends to infinity, so does the active stage `s`, proving
(4.2)--(4.3).  QED.

The theorem is existential and rate-free.  In particular, it supplies no
claim that `h` can be as large as `Theta(sqrt(m log m))`.

## 5. Linearizing and concatenating the packed cycles

Fix a packed cyclic block

\[
                 B=(X_0,X_1,\ldots,X_{R-1}),
                 \qquad R=2\ell.                            \tag{5.1}
\]

Assume `h<ell`.  Write the following linear gadget:

\[
 \underbrace{X_0,\ldots,X_0}_{h\text{ extra copies}},
 X_0,X_1,\ldots,X_{R-1},X_0,X_1,\ldots,X_{h-1},
 \underbrace{X_{h-1},\ldots,X_{h-1}}_{h\text{ extra copies}}.
 \tag{5.2}
\]

Its length is `R+3h`.  The repeated cyclic prefix ensures that every cyclic
window of at most `h+1` original block states occurs as an ordinary linear
window in (5.2).

Every active coordinate has cyclic positive runs of length exactly `ell`,
and every core coordinate is present throughout the original block.  Hence
every positive run internal to the continuously unrolled part of (5.2) has
length at least `ell>h`.  The two constant pads make every positive run
truncated by an end have length at least `h+1`.  Consequently arbitrary
concatenation of the gadgets (5.2) has no internal positive coordinate run
of length at most `h`.

If the matching has `t` blocks, then `tR <= W`, and their total gadget
length is

\[
 t(R+3h)
 \le W+\frac{3h}{2\ell}W.                                  \tag{5.3}
\]

For every uncovered middle set `S`, append a constant gadget consisting of
`h+1` copies of `S`.  By (4.3), all such repairs cost `o(W)`.  Combining
(4.2), (4.3), and (5.3) proves the following.

### Corollary 2 (padded middle row)

There is a middle-set sequence of length

\[
                              W+o(W)                         \tag{5.4}
\]

which contains every middle set, has no internal coordinate `1`-run shorter
than `h+1` for some `h->infinity`, and contains every cyclic window through
depth `h` of each selected partial block.

The seam pads deliberately create repeated-state windows, so it is false
that **every** short window of the concatenated row is geodesic.  What is
true, and what the derivative construction uses, is that all designated
block windows survive, while the total seam halo has size

\[
                  O\!\left(\frac h\ell W\right)=o(W).       \tag{5.5}
\]

## 6. Relation to Stage B

A partial block supplies `R=2 ell` cyclic starts at every depth `q<h`.
Repeating the first `h` states, rather than discarding the wrapping starts,
is important here.  For a short block the inequality

\[
                     R\rho_q\le R-q                       \tag{6.1}
\]

need not hold: already at `q=1`, it would require `ell` to be of order `m`.
The repeated prefix restores all `R` physical starts at an asymptotic cost
`h/R=o(1)` per covered middle vertex.

However, the Stage-A matching controls only collisions among the middle
vertices.  Lower and upper colours from different selected blocks may still
coincide.  As proved in `SHADOW_SLOT_HALL.md`, the physical OR problem does
not require prescribed per-block quotas or capacitated assignments: it needs
only union coverage of each shadow layer, with the total number of omissions
small enough to repair in `o(W)` positions.  Nothing in Theorem 1 proves that
simultaneous two-sided multiscale coverage.  In particular an unstructured
random block factor misses a positive fraction of the first few shadows.

## 7. Status and the sharp next target

Proved here:

* the exact cyclic-interval model (1.4);
* the exact geometric degree (2.3);
* all pair codegrees (3.2)--(3.4), in particular (3.5);
* a rigorous rate-free partial-block near-factor with `h->infinity`; and
* `W+o(W)` linearization with run padding.

Not proved here:

* a full `2m`-cycle near-decomposition;
* a partial-block factor at any prescribed growing depth;
* global lower/upper shadow coverage with summed omission `o(W)`; or
* a universal OR array of length `W+o(W)`.

The exact numerical regime suggests the following specialized matching
target.  The partial-block hypergraph has rank `r=2 ell` and

\[
                 \frac{r\Delta_2}{D}=\frac{4\ell}{m^2}.     \tag{7.1}
\]

This tends to zero uniformly for every `ell<=m`, except that full cycles
must first be quotiented by complementation.  A growing-rank nibble theorem
tailored to these cyclic-interval blocks, strong enough when (7.1) tends to
zero, would upgrade the rate-free diagonal theorem to prescribed
`ell=ell(m)`.  Existing fixed-uniformity Pippenger theorems do not provide
that upgrade by themselves.

## 8. A Boolean-specific factor through one fixed coordinate matching

The preceding matching proof is not needed for Stage A.  There is an exact
cube-tiling reduction which exploits the special Boolean geometry.

Fix once and for all a perfect matching of the coordinate ground set,

\[
        \mathcal P=\{P_1,\ldots,P_m\},\qquad |P_i|=2.        \tag{8.1}
\]

For a middle set `X`, classify every coordinate pair as

\[
\begin{aligned}
 F(X)&=\{i:P_i\subseteq X\},\\
 E(X)&=\{i:P_i\cap X=\varnothing\},\\
 S(X)&=\{i:|P_i\cap X|=1\}.
\end{aligned}                                                 \tag{8.2}
\]

Since `|X|=m`, necessarily

\[
                  |F(X)|=|E(X)|.                              \tag{8.3}
\]

Fix disjoint pair-index sets `F,E,S` partitioning `[m]`, with
`|F|=|E|` and `|S|=s`.  The middle sets having this fixed type are obtained
by choosing one of the two coordinates in each pair indexed by `S`.
Consequently the stratum is canonically an `s`-dimensional cube

\[
                         Q_s=\{0,1\}^s.                       \tag{8.4}
\]

Different strata are disjoint and together partition the entire middle
layer.

Now let `ell` be a power of two.  In `Q_ell`, take the standard pair-flip
cycle

\[
 0^\ell,
 10^{\ell-1},
 110^{\ell-2},\ldots,
 1^\ell,
 01^{\ell-1},\ldots,001,0^\ell.                              \tag{8.5}
\]

Its vertex set `C_ell` has `2 ell`, a power of two, elements.  It is an
induced cycle: two of its vertices are adjacent in the cube exactly when
they are consecutive in (8.5).

We use the following proved cube-decomposition theorem.

> **Gruslys' isometric tiling theorem.**  If
> `Y subseteq {0,1}^d` and `|Y|` is a power of two, then for all sufficiently
> large `s`, the cube `{0,1}^s` can be partitioned into isometric copies of
> `Y`.

Apply it with `Y=C_ell`.  There is a threshold `n_0(ell)` such that every
orientation cube `Q_s` with `s>=n_0(ell)` partitions exactly into isometric
copies of `C_ell`.  An isometry from `Q_ell` into `Q_s` fixes `s-ell`
coordinates, permutes the active coordinates, and may complement them.
Under the identification (8.4), its image is therefore exactly a partial
pair-flip block: the fixed full coordinate pairs and the fixed orientations
of inactive split pairs form the core, while the `ell` varying split pairs
are active.

We have proved the following exact statement.

### Theorem 3 (stratified partial-block factor)

Let `ell` be a fixed power of two.  Relative to any fixed perfect matching
of `[2m]`, every middle-layer stratum with at least `n_0(ell)` split pairs
admits an exact partition into partial pair-flip blocks of length `2 ell`.

Only low-split strata remain.  Their size can be bounded without probability.
The number of middle sets with exactly `s` split pairs is

\[
 A_s=
 \binom ms
 \binom{m-s}{(m-s)/2}
 2^s,                                                        \tag{8.6}
\]

when `m-s` is even, and is zero otherwise.  Hence, for every integer `t`,

\[
 \sum_{s<t}A_s
 \le
 2^m\sum_{s<t}\binom ms.                                    \tag{8.7}
\]

For fixed `t`, the right side is `2^m m^{O(t)}`, whereas

\[
 W=\binom{2m}m=\Theta(4^m/\sqrt m).                          \tag{8.8}
\]

Thus Theorem 3 leaves an exponentially small proportion of the middle layer
uncovered for every fixed power-of-two `ell`.

Finally, diagonalize.  At stage `j`, take any power of two

\[
              \ell_j\ge j^2,
 \qquad       h_j=j.                                        \tag{8.9}
\]

Choose the stage threshold large enough that

\[
 n_0(\ell_j)<m,\qquad
 \ell_j/m\le1/j,
 \qquad
 h_j\sum_{s<n_0(\ell_j)}A_s\le W/j^2.                       \tag{8.10}
\]

Use Theorem 3 on every good stratum.  As in Section 4, hold stage `j` until
the next threshold.  This gives functions

\[
 h\to\infty,\qquad h/\ell\to0,
 \qquad \ell/m\to0                                         \tag{8.11}
\]

and a partial-block factor leaving `u_m` vertices with `h u_m=o(W)`.
Therefore Theorem 3 gives a second, Boolean-specific proof of Theorem 1 and
feeds directly into the `W+o(W)` linearization in Section 5.

This construction is structural but not a short closed-form factor: the
outer decomposition into orientation cubes is explicit, while the inner
cube tiling invokes Gruslys' existence theorem.  Its important mathematical
consequence is that Stage A does **not** require a new growing-uniformity
nibble.  The unresolved global step is simultaneous two-sided shadow
coverage, together with obtaining a useful prescribed rate for the depth if
one insists on the literal-tail strategy.

The cube tiling used above is Theorem 5 of V. Gruslys,
*Decomposing the vertex set of a hypercube into isomorphic subgraphs*,
arXiv:1611.02021.

## 9. Exact pair-type criterion for individual shadow representability

The fixed coordinate matching also isolates the remaining Stage-B problem.
For any set `Y subseteq [2m]`, let `f(Y),e(Y),s(Y)` be the numbers of
coordinate pairs which are respectively full, empty, and split in `Y`.

### Proposition 4 (individual shadow criterion)

Fix `0<=q<=ell`.  A rank-`m-q` set `L` is the intersection of `q+1`
consecutive states of **some** partial `ell`-block if and only if

\[
                         s(L)\ge\ell-q.                    \tag{9.1}
\]

Dually, a rank-`m+q` set `U` is the union of `q+1` consecutive states of
some partial `ell`-block if and only if

\[
                         s(U)\ge\ell-q.                    \tag{9.2}
\]

#### Proof

In a geodesic `q`-window, exactly `q` active coordinate pairs are flipped.
Its intersection contains neither coordinate from those pairs.  Every one
of the other `ell-q` active pairs contributes exactly one coordinate, so the
intersection has at least `ell-q` split pairs.  This proves necessity in
(9.1).

Conversely, choose `ell-q` split pairs of `L` and `q` empty pairs of `L`.
The latter exist because, from

\[
 2f(L)+s(L)=m-q,\qquad f(L)+e(L)+s(L)=m,
\]

one gets `e(L)-f(L)=q`.  Use these `ell` pairs as the active pairs.  Keep the
chosen split-pair orientations fixed during the window, and flip the chosen
empty pairs once each.  Add to the starting middle set one of the two
coordinates in every chosen empty pair.  The intersection of the resulting
window is exactly `L`, and the fixed part has size `m-ell`, so this extends
to a valid partial block.  This proves sufficiency.  Complementation proves
(9.2).  QED.

The criterion has only a sparse exceptional family when `ell` is small
relative to `m`.  For the lower layer, the number with exactly `s` split
pairs is

\[
 \binom ms
 \binom{m-s}{(m-q-s)/2}2^s,                                 \tag{9.3}
\]

when the second lower argument is an integer, and zero otherwise.  The same
bound holds in the upper layer by complementation.  Hence the number failing
(9.1), or failing (9.2), is at most

\[
                  2^m\sum_{s<\ell-q}\binom ms.              \tag{9.4}
\]

In particular this is `o(W)` whenever

\[
                         \ell\log m=o(m).                    \tag{9.5}
\]

The diagonal thresholds in Section 8 may be enlarged to enforce (9.5) and
to make the sum of (9.4) over every `q<=h` equal to `o(W/h)`.

Proposition 4 proves that almost every central-band target is compatible
with the local pair geometry.  It does **not** say that the particular cube
factor from Theorem 3 contains a witnessing window for every such target.
The remaining problem is now local and exact:

> tile the high-dimensional orientation cubes by the `2 ell`-cycles so that
> their consecutive `q`-face projections cover almost every admissible
> partial word, simultaneously for `q<=h` and on both sides.

Gruslys' theorem controls the vertex tiling only.  The additional face-shadow
condition is the genuine Stage-B obstruction.

## 10. Exact two-sided pairing of the first shadow inside pair strata

Although the cycle-factor compatibility is unresolved, the fixed coordinate
matching makes the lower/upper **colour pairing** at depth one elementary.

Fix a set `S` of split coordinate-pair indices and fix one orientation on
every pair in `S`.  Put `T=[m]-S`.  If a rank-`m-1` target has this split
data, then

\[
             |T|=2f+1,                                      \tag{10.1}
\]

where its full-pair indices form an `f`-subset `F` of `T`; all other indices
of `T` are empty.  Rank-`m+1` targets with the same split data correspond to
the `(f+1)`-subsets of `T`.

The inclusion graph

\[
       \binom Tf \longleftrightarrow \binom T{f+1}           \tag{10.2}
\]

is `(f+1)`-regular on both sides.  It therefore has a perfect matching.  For
every matched pair `F subset F union {i}`, the associated lower and upper
targets differ by filling the fixed coordinate pair `P_i`.  The two middle
sets obtained by adding either one of the two members of `P_i` form a Johnson
edge whose intersection is the lower target and whose union is the upper
target.

Doing this independently for every split set and every split orientation
proves:

### Proposition 5 (exact fixed-pair colour matching)

There is a family of Johnson edges, every one swapping the two coordinates
of one fixed pair `P_i`, whose intersection colours are exactly all
rank-`m-1` sets once and whose union colours are exactly all rank-`m+1` sets
once.

The proposition selects

\[
       N_1=\binom{2m}{m-1}=\frac{m}{m+1}W                  \tag{10.3}
\]

Johnson edges, so their average degree on the middle layer is

\[
                         \frac{2m}{m+1}<2.                  \tag{10.4}
\]

What (10.4) does not control is the maximum degree.  A middle set with many
split coordinate pairs can be an endpoint of many independently selected
edges.  Thus Proposition 5 solves the exact two-colour pairing but not the
coherent degree-two path/cycle factor required by the OR row.  The remaining
depth-one problem is to choose the regular-bipartite perfect matchings in
(10.2) coherently so that the projected middle graph is a near-spanning
linear forest, preferably one compatible with the partial-cycle tiling of
Section 8.

## 11. Explicit linear-code tiling at prescribed depth

The Gruslys theorem in Section 8 is no longer needed for Stage A.  If
`ell=2^t`, write the standard cycle in `F_2^ell` as

\[
 P_\ell=\{p_i,1+p_i:0\le i<\ell\},
 \qquad p_i=e_1+\cdots+e_i.
\]

There is an explicit surjective linear map

\[
 \phi:\mathbb F_2^\ell\to\mathbb F_2^{t+1}
\]

whose restriction to `P_ell` is bijective.  Namely, enumerate the
codimension-one subspace `U=F_2^t x {0}` as
`u_0=0,u_1,...,u_(ell-1)`, take `v notin U`, and set

\[
 \phi(e_i)=u_i+u_{i-1}\ (i<\ell),
 \qquad \phi(e_\ell)=v+u_{\ell-1}.
\]

Then `phi(p_i)=u_i` and `phi(1+p_i)=v+u_i`.  Consequently
`P_ell` is a complete set of representatives for `ker(phi)`, and

\[
 \{P_\ell+k:k\in\ker\phi\}
\]

partitions `Q_ell`.  Taking Cartesian fibers partitions every `Q_s`,
`s>=ell`, into the same partial cycles.

Choose a power of two `ell` with

\[
 m^{3/4}\le\ell<2m^{3/4}
\]

and `H=(1+epsilon)sqrt(m log m)`.  Every orientation-cube stratum with at
least `ell` split pairs is tiled exactly.  The remaining strata contain at
most

\[
 2^m\sum_{s<\ell}\binom ms=2^{-m+o(m)}W=o(W/H)
\]

middle masks.  Prefixing and padding the selected cycles costs
`O(HW/ell)=o(W)`.  Hence Stage A is now explicit and proved at the full
literal-tail depth `H`; no growing-rank nibble, diagonalization, or unknown
tiling threshold remains.  The complete proof and the structured freedom in
the syndrome enumeration are in `LINEAR_CYCLE_TILING.md`.
