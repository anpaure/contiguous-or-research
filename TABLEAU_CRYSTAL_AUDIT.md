# Tableau/crystal audit for a shift-compatible symmetric-chain decomposition

This note tests a natural representation-theoretic idea for the
shift-compatible SCD problem in `PARTIAL_BLOCK_MULTISCALE.md`: encode middle
binary words by two-row standard Young tableaux and try promotion,
evacuation, Bender--Knuth moves, crystal commutors, or affine type-A1
dynamics as the required middle permutation.  Throughout,
`W=binom(2m,m)`.

The outcome is mixed but sharp.

* RSK explains **exactly** why the certification probabilities are the SCD
  radius law.
* The canonical `sl_2` crystal SCD is decisively incompatible with the
  required radius-preserving projection.  No action that merely permutes its
  tableaux of a fixed shape can repair that fact.
* Promotion, evacuation, and the standard affine promotion are not Johnson
  moves on the middle layer.
* A nontrivial elementary Bender--Knuth move *is* exactly a
  radius-preserving Johnson move.  These moves give a connected host graph in
  every radius class.  However each generator is an involution, so it cannot
  satisfy the depth-two shift rule.
* Commuting Bender--Knuth generators nevertheless partition all but `o(W)`
  middle words into high-dimensional **abstract** cubes lying inside single
  radius classes.  The corresponding Johnson swap coordinates depend on the
  current tableau, so these cubes are not known to be isometric pair-flip
  cubes.  Local geodesicity remains unproved.

Thus the usual named dynamics do not construct the desired SCD.  The useful
representation-theoretic residue is the abstract Bender--Knuth cube
decomposition in Section 5; it provides radius-pure connectivity but not the
required coordinate-disjoint middle skeleton.

## 1. RSK gives the radius decomposition exactly

Regard a middle set as a binary word of length `2m` and weight `m`.  Binary
RSK has at most two rows.  If its shape is

\[
 \lambda_d=(m+d,m-d),\qquad 0\le d\le m,              \tag{1.1}
\]

then there is exactly one semistandard insertion tableau of shape
`lambda_d` and content `(m,m)`.

Indeed, the `m-d` columns of height two are forced to be

\[
 \begin{matrix}1\\2\end{matrix}.
\]

After those columns have used `m-d` copies of each letter, the remaining
`2d` cells of the first row are forced to contain `d` ones followed by `d`
twos.  Denote this unique tableau by `P_d`.  Therefore RSK restricts to a
bijection

\[
 \binom{[2m]}m
 \longleftrightarrow
 \bigsqcup_{d=0}^{m}\operatorname {SYT}(m+d,m-d),      \tag{1.2}
\]

where a middle word is identified with the recording tableau `Q` in the pair
`(P_d,Q)`.

The two-row hook formula gives

\[
 f^{(m+d,m-d)}
 =\binom{2m}{m-d}-\binom{2m}{m-d-1}.                  \tag{1.3}
\]

This is exactly the number of radius-`d` chains in every SCD of the
`2m`-cube.  In Schur--Weyl language, the standard tableaux index the
multiplicity copies of the `sl_2` irreducible of highest weight `2d`, and its
unique zero-weight vector is the middle word `(P_d,Q)`.

Consequently the telescoping certification law from Section 9 of
`PARTIAL_BLOCK_MULTISCALE.md` is not merely analogous to a representation
decomposition: it is the two-row Schur--Weyl multiplicity decomposition.

The same dictionary exists off the middle layer.  For `0<=q<=d`, there is
again a unique semistandard tableau `P_(d,q)` of shape `lambda_d` and binary
content `(m-q,m+q)` (with the two entries interchanged under the opposite bit
convention).  The forced height-two columns use `m-d` copies of each symbol,
and the remaining first-row cells contain `d-q` copies of one symbol followed
by `d+q` of the other.  Hence

\[
 \binom{[2m]}{m-q}
 \longleftrightarrow
 \bigsqcup_{d=q}^{m}\operatorname {SYT}(\lambda_d),   \tag{1.4}
\]

and similarly at rank `m+q`.  Numerically this is the telescoping identity

\[
 \binom{2m}{m-q}=\sum_{d=q}^{m}f^{\lambda_d}.         \tag{1.5}
\]

Thus RSK supplies canonical lower and upper weight vectors for every
tableau.  The unresolved issue is to re-pair those vectors into Boolean
chains whose middle projections shift, because the canonical crystal
pairing of the same `Q` has the radius-drop defect proved next.

## 2. A no-go theorem for the canonical crystal chains

Fix the standard tensor-product `sl_2` crystal on binary words.  Holding `Q`
fixed and varying the semistandard tableau `P` traverses one saturated
symmetric chain.  Its radius is `d` when `Q` has shape `lambda_d`.

Let `X_Q` be its middle word, and let `r_0(Q)` and `u_0(Q)` be the first
downward and upward labels at the middle.  The projected Johnson neighbour
of this canonical chain would be

\[
 g(X_Q)=X_Q\setminus\{r_0(Q)\}\cup\{u_0(Q)\}.         \tag{2.1}
\]

### Theorem 1 (canonical radius drop)

For every `d>0`, the word `g(X_Q)` has RSK shape

\[
 \lambda_{d-1}=(m+d-1,m-d+1).                         \tag{2.2}
\]

In particular the canonical crystal projection is never
radius-preserving.

### Proof

Use the usual reduced `sl_2` signature of a binary word.  At the zero-weight
member of a component of highest weight `2d`, the unmatched signature has
`d` symbols of one sign followed by `d` symbols of the other sign.  The two
crystal covers adjacent to the middle act at the two inner boundary symbols;
these are precisely the positions `r_0(Q)` and `u_0(Q)`.

Changing both positions as in (2.1) creates one new matched pair.  All
previously matched pairs remain matched, so the reduced signature now has
`d-1` symbols of each sign.  Its component has highest weight `2d-2`, hence
RSK shape (2.2).  This is also the parenthesis calculation in
`GK_PROJECTION_COUNTS.md`, equation (1.3).  QED.

### Corollary 2

No shape-preserving permutation of the recording tableaux can be the
required projection of the canonical crystal SCD on even one positive-radius
class.

This applies immediately to promotion, evacuation, Bender--Knuth actions on
`Q`, and cactus/crystal-commutor actions that permute the multiplicity copies
of a fixed `sl_2` irreducible.  They preserve `lambda_d`; (2.1) always lands
in `lambda_(d-1)`.

Moreover the failure is macroscopic.  There are only

\[
 f^{(m,m)}=\operatorname {Cat}_m=o\!\left(\binom{2m}m\right)
\]

radius-zero chains.  Thus the canonical projection has the wrong radius on
`(1-o(1))W` middle words.  Conjugating or reordering the same crystal
components cannot yield an `o(W)` repair.

The corollary does **not** rule out a different SCD.  It says that a positive
construction must re-pair the Boolean levels on almost every chain, rather
than apply a familiar action to the standard crystal chains.

## 3. Promotion is a macro move, not a Johnson move

Schuetzenberger promotion preserves the shape of `Q`, but under the inverse
RSK bijection (1.2) it need not change only one selected coordinate and one
unselected coordinate.

There is an explicit obstruction already in rectangular shape `lambda_0`.
Let

\[
 Q_m=
 \begin{array}{cccccc}
 1&2&4&6&\cdots&2m-2\\
 3&5&7&9&\cdots&2m
 \end{array}.                                         \tag{3.1}
\]

For a rectangular two-row tableau the associated radius-zero binary word is
the row-membership word.  Thus the one-set of `X_(Q_m)` is

\[
 \{1,2,4,6,\ldots,2m-2\}.                             \tag{3.2}
\]

The promotion slide in (3.1) runs along the first row and then through the
last cell of the second row.  After decrementing the labels, the first row is

\[
 1,3,5,\ldots,2m-1.                                   \tag{3.3}
\]

Hence promotion changes

\[
 \left|X_{Q_m}\mathbin\triangle X_{\operatorname {pro}Q_m}\right|
 =2m-2.                                                \tag{3.4}
\]

For `m>=3` this is not a Johnson edge.  Therefore promotion cannot be the
one-step middle permutation.  Its expression as a product of elementary
Bender--Knuth moves is useful only as a *walk* of many Johnson edges; using
all those microsteps would introduce a factor of order `m` in the row length.

## 4. Evacuation and commutors are even more rigidly excluded

Let `w=w_1...w_(2m)` be a middle binary word and put

\[
 w_i^*=1-w_{2m+1-i}.                                  \tag{4.1}
\]

The Schuetzenberger involution on words is reverse-complement.  RSK sends it
to evacuation on both tableaux.  Since `P_d` is the unique tableau of its
shape and content, it is fixed by this involution.  Therefore evacuation of
the recording tableau induces exactly `w -> w^*` under (1.2).

Pair positions `i` and `2m+1-i`.  The two words differ at both positions of
a pair exactly when the original pair is `00` or `11`.  If `a` and `b` are
the respective numbers of `00` and `11` pairs, balance gives `a=b`.  It
follows that

\[
 d_H(w,w^*)=2(a+b)=4a.                                \tag{4.2}
\]

Thus evacuation is either the identity at a word or changes at least four
coordinates.  It is never a nontrivial Johnson move.

There is also a dynamics-independent depth obstruction.

### Lemma 3 (involution obstruction)

No involution can satisfy the shift recurrence at a vertex of radius at
least two.

### Proof

Shift compatibility gives

\[
 f^2(X)=X\setminus\{r_0(X),r_1(X)\}
          \cup\{u_0(X),u_1(X)\}.                      \tag{4.3}
\]

The two removal labels are distinct and the two addition labels are
distinct, so `f^2(X) != X`.  QED.

Every elementary crystal commutor and every cactus-group interval-reversal
generator is an involution.  Even in a case where such a generator happened
to be a Johnson edge, Lemma 3 rules it out beyond depth one.  Products of
commutors can have longer order, but the standard product called promotion
already fails the one-edge test in Section 3.

## 5. The useful positive residue: Bender--Knuth edges

Let `tau_i` be the elementary Bender--Knuth involution on a standard tableau:
it swaps the labels `i` and `i+1` when their boxes are incomparable (equivalently,
when the swap remains standard), and otherwise fixes the tableau.

### Theorem 4 (local Johnson dictionary)

Let `w_Q` be the middle word corresponding to `(P_d,Q)`.  If
`tau_i(Q) != Q`, then

\[
 |w_{\tau_iQ}\mathbin\triangle w_Q|=2.                       \tag{5.1}
\]

Consequently (5.1) is one radius-preserving Johnson edge.  The two changed
word coordinates need **not** be `i,i+1`.

### Proof

Run inverse row insertion for `(P_d,Q)` and `(P_d,tau_iQ)` in parallel.  The
deletion orders differ only by interchanging two consecutive incomparable
corners.  In a two-letter tableau, the two reverse bump paths agree outside
the strip between their first meeting points.  Their output words are equal
except at the two endpoints of this strip, where one output is `1,2` and the
other is `2,1`.  Thus the two binary words have equal weight and differ in
exactly two coordinates.  (This is the two-letter specialization of the
local inverse-RSK growth rule.)  Their recording tableaux have the same
shape, so the Johnson edge is radius-preserving.  QED.

It is important not to strengthen this statement to an adjacent-coordinate
swap.  The recording labels `i,i+1` specify the order of two reverse
insertions; their bump paths can terminate at nonadjacent word positions.

For fixed shape `lambda_d`, standard tableaux are the linear extensions of
the Ferrers poset of that shape.  The graph of linear extensions under swaps
of consecutive incomparable elements is connected: repeatedly bubble the
first disagreement of one extension toward its position in another.  Via
Theorem 4 this proves:

### Corollary 5

For every radius `d`, the middle words of RSK shape `lambda_d` form a
connected subgraph of `J(2m,m)` using only nontrivial Bender--Knuth edges.

This is a genuine first-order positive result.  Radius preservation and
Johnson connectivity are available without search.

It does not yet give the required permutation.  A fixed `tau_i` has fixed
points and all its nontrivial orbits have length two; Lemma 3 excludes depth
two.  One would have to choose the generator **state by state** and form long
cycles.

There is an obvious parity condition on such cycles, but it is only a
lower-order obstruction.  Give every tableau the parity of its row-reading
permutation.  Every Bender--Knuth edge reverses this parity, so each shape
graph is bipartite.  Pair tableaux of a fixed shape by swapping the first
pair of labels

\[
 (1,2),(3,4),\ldots,(2m-1,2m)                         \tag{5.2}
\]

that occupy incomparable boxes.  This is a sign-reversing involution.  Its
fixed tableaux have every displayed pair in two adjacent comparable boxes;
equivalently they are standard domino tableaux.

Across **all** two-row shapes of size `2m`, there are at most `3^m` such
fixed tableaux.  To see this, construct one by adding the dominoes in label
order.  A two-row partition has at most three addable dominoes: horizontal
in the first row, horizontal in the second row, or vertical.  Consequently,

\[
 \sum_{d=0}^{m}
 \left|\#\operatorname {SYT}(\lambda_d)_{\rm even}
       -\#\operatorname {SYT}(\lambda_d)_{\rm odd}\right|
 \le 3^m=o\!\left(\binom{2m}m\right).                 \tag{5.3}
\]

Thus bipartite imbalance may force deletions, but only `o(W)` in total.  It
does not rule out the near-spanning cycle-cover program.

The host graph also contains enough exact cubes to cover all but `o(W)`
vertices.

### Theorem 6 (radius-pure abstract cube decomposition)

Retain the commuting generators

\[
 \tau_1,\tau_3,\ldots,\tau_{2m-1},                    \tag{5.4}
\]

corresponding to the disjoint label pairs `(1,2),(3,4),...`.  For a tableau
`Q`, let `s(Q)` be the number of these generators that move `Q`.

1. The orbit of `Q` is an abstract `s(Q)`-cube whose edges are middle-layer
   Johnson edges, entirely inside the one RSK radius class containing `Q`.
2. For every `ell=o(m)`,

\[
 \#\{Q:\ Q\text{ has at most two rows and }s(Q)<\ell\}
 \le
 \sum_{s<\ell}\binom ms\,2^s3^{m-s}
 =\exp((\log3+o(1))m)=o(W).                           \tag{5.5}
\]

### Proof

Generators in (5.4) act on disjoint labels.  They commute, and applying one
does not alter the boxes occupied by any other label pair.  Hence the set of
available generators is constant throughout the orbit, and the orbit graph
is a Boolean cube.  Theorem 4 says that every abstract cube edge is a Johnson
edge.  Every move preserves tableau shape, so the cube is radius-pure.

For the count, construct a two-row tableau in the order of its label pairs.
After labels `1,...,2j-2` have been inserted, their boxes form a two-row
partition.  If boxes `2j-1,2j` are comparable, they are adjacent and can be
added in at most three ways: horizontal in the first row, horizontal in the
second row, or vertical.  If they are incomparable, there are at most two
orders in which the two distinct addable corners can be used.  After choosing
the `s` incomparable pairs, this gives at most `2^s3^(m-s)` tableaux.  Summing
over `s<ell` proves the inequality.  Since `ell=o(m)`, the binomial lower tail
contributes only `exp(o(m))`, while `W=exp((log4+o(1))m)`.  QED.

Choose `ell=m^(3/4+o(1))`.  By Theorem 6, all but `o(W)` middle words lie in
radius-pure abstract cubes of dimension at least `ell`.  This does **not**
permit a direct application of `LINEAR_CYCLE_TILING.md`: that theorem needs
fixed disjoint coordinate-pair directions, whereas the two word coordinates
changed by `tau_i` depend on the current tableau.  Abstract commuting
generators can therefore reuse a word coordinate on consecutive cube edges.

The proved positive conclusion is only a high-dimensional, radius-pure
Johnson host graph on `W-o(W)` vertices.  Obtaining locally geodesic cycles,
let alone a shadow-partitioning SCD, remains a separate colored-edge problem.

There is a precise colored version of the surviving problem.  Label the edge
`Q -- tau_iQ` by its actual two-coordinate support

\[
 S(Q,i)=w_Q\mathbin\triangle w_{\tau_iQ}.
\]

If a cycle is geodesic through depth `d`, then every `d` consecutive actual
supports must be pairwise disjoint:

\[
 S(Q_s,i_s)\cap S(Q_t,i_t)=\varnothing
 \qquad(0\le s<t<d).                                  \tag{5.6}
\]

In addition, the consecutive intersections and unions from all radius
classes must biject onto the corresponding Boolean layers.  Thus the
representation-theoretic remainder is:

> Find almost-spanning colored cycle covers in the Bender--Knuth/linear-
> extension graphs, with the state-dependent support constraint (5.6), and
> couple the covers across radii so that every lower and upper shadow occurs
> once.

This is substantially more structured than an arbitrary SCD search, but it
is not supplied by promotion or evacuation.  Promotion is a long prescribed
word in the generators `1,2,...,2m-1`; generator labels alone do not control
the actual supports in (5.6).

## 6. Affine type-A1 dynamics

The standard affine Dynkin promotion on the one-letter type-A1 crystal swaps
the two letters.  On a tensor word the evident promotion is therefore
letter-complementation (up to tensor rotation conventions).  On a balanced
word it changes all `2m` positions, and it need not preserve the classical
RSK radius.  A cyclic tensor rotation also fails globally: on an alternating
balanced word it changes every position.

Carrier/combinatorial-R dynamics such as the box--ball time evolutions do
preserve representation-theoretic conserved data, but they are parallel
many-particle moves.  For example, the basic periodic evolution translates
the alternating state and again changes all `2m` bits.  Hence the standard
affine dynamics are macro moves, not universal Johnson edges.

This does not prove that no specially engineered affine action can help.  It
does show that the usual affine promotion, tensor rotation, and carrier time
evolutions do not meet the first equation

\[
 f(X)=X-r_0(X)+u_0(X).                                \tag{6.1}
\]

## 7. Recommendation

The tableau route should not spend further effort trying standard promotion,
evacuation, or a single commutor.  They are ruled out before the higher-shadow
problem begins.

If this route is pursued, the correct object is the colored Bender--Knuth
graph from Section 5.  The next purely mathematical questions are:

1. Determine whether the state-dependent Johnson supports in a typical
   high-dimensional Bender--Knuth cube admit long paths whose sliding support
   windows are pairwise disjoint.
2. Couple any such paths across the radius distribution (1.3) so that the
   induced `q`-fold lower and upper shadow maps are bijective, or miss only
   `o(W)` masks in total.
3. Relate those shadows to the inverse-RSK weight vectors `(P_(d,q),Q)`, so
   that the remaining coupling becomes a matching or absorption theorem
   rather than an unconstrained SCD search.

A positive answer would amount to a genuinely new, state-dependent tableau
dynamics.  It would not be one of the standard named operators audited here.

## References

* Henriques and Kamnitzer, crystal commutors and cactus actions:
  [Crystals and coboundary categories](https://arxiv.org/abs/math/0406478).
* Pfannerer, Rubey, and Westbury, promotion through cactus groups:
  [Promotion on oscillating and alternating tableaux](https://arxiv.org/abs/1804.06736).
* Bandlow, Schilling, and Thiery, affine promotion operators:
  [On the uniqueness of promotion operators on tensor products of type A crystals](https://arxiv.org/abs/0806.3131).
* Fukuda, box--ball dynamics and RSK:
  [Box-ball systems and Robinson--Schensted--Knuth correspondence](https://arxiv.org/abs/math/0105226).
