# GK orientation graphs are biregular; physical row balance is a max-weight d-factor gate

**Status (2026-08-21).**  The exact biregularity and `d`-factor statements
below are proved.  They refine the alternating Greene--Kleitman integral
retirement theorem at one new level: the selected middle sources can be
made exactly regular in both local Boolean coordinates.  The resulting
maximum-weight `d`-factor is an ordinary integral bipartite-flow problem.

What is not yet proved is that its extra top-weight loss is `o(W_b)` in the
full regime `H=Theta(sqrt(b log b))`.  Exact finite optima show that the
row/column constraint has a genuine positive cost; the globally longest
chains are not already regular.  This note keeps separate:

1. row/column regular selection of GK sources;
2. decomposition of those selected incidences among actual phase diagonals
   inside cyclic wreath decks; and
3. packing whole translated product atoms without source or target
   collisions.

Only the first level is solved here.

## 1. The two orientation graphs

Let `b` be an odd prime, let `A={A_1,...,A_b}` and
`B={B_1,...,B_b}`, and use the alternating coordinate order

\[
                 A_1,B_1,A_2,B_2,\ldots,A_b,B_b.   \tag{1.1}
\]

Fix a proper middle split `1<=r<=b-1`, and put

\[
             N_r={b\choose r}.                     \tag{1.2}
\]

Rows are the `r`-subsets `X` of `A`; columns are the `(b-r)`-subsets `Y`
of `B`.  The pair `(X,Y)` is one rank-`b` Boolean source.  Join it in
`G_r^A` when its Greene--Kleitman chain is `A`-first, equivalently when its
top excess is odd.  Join it in `G_r^B` when its top excess is even; the
top-excess-zero sources are formal `B` edges and carry weight zero.

## 2. A rotation-minimum identity

Encode a fixed row and column by signs

\[
 x_i=2\mathbf1_{A_i\in X}-1,qquad
 y_i=2\mathbf1_{B_i\in Y}-1.                       \tag{2.1}
\]

Then

\[
 \sum_i x_i=2r-b=:a,qquad \sum_i y_i=-a.          \tag{2.2}
\]

Define `X_i=sum_(h=1)^i x_h` and `Y_j=sum_(h=1)^j y_h`, with
`X_0=Y_0=0`, and extend these prefix sums quasiperiodically:

\[
 X_{i+b}=X_i+a,qquad Y_{j+b}=Y_j-a.               \tag{2.3}
\]

For a cyclic rotation `t` of the `B` word, put

\[
                  M_t=\min_{0\le i<b}(X_i+Y_{i+t}).\tag{2.4}
\]

### Lemma 2.1 (orientation is the sign of one minimum increment)

For the `B`-rotation `t`, the even-coordinate prefix minimum of the
interleaved word is

\[
                         M_t-Y_t,                   \tag{2.5}
\]

and its odd-coordinate prefix minimum is

\[
                         M_{t-1}-Y_t.               \tag{2.6}
\]

Moreover

\[
 M_t-M_{t-1}\in\{-1,+1\},                          \tag{2.7}
\]

and the chain is `A`-first exactly when this increment is `+1`.

#### Proof

After `i` complete coordinate pairs, the rotated prefix sum is

\[
 X_i+Y_{i+t}-Y_t;
\]

minimizing gives (2.5).  Immediately after the next `A` coordinate it is
`X_(i+1)+Y_(i+t)-Y_t`, which gives (2.6) after reindexing.

Every summand defining `M_t` differs from the corresponding summand for
`M_(t-1)` by one sign `y_(i+t)`, so the two minima differ by at most one.
Also `X_i` has parity `i`, and `Y_(i+t)` has parity `i+t`; hence
`M_t` has parity `t`.  Equality is impossible and (2.7) follows.

The minimum in (2.5) is even, while the minimum in (2.6) is odd.  The
rightmost unmatched zero, and therefore the first upward GK step, is in an
`A` position exactly when the odd minimum is smaller.  This is precisely
`M_t>M_(t-1)`.  \(\square\)

Finally (2.3) gives

\[
                 M_b-M_0=-a=b-2r.                  \tag{2.8}
\]

Among the `b` increments in (2.7), there are therefore exactly `b-r`
pluses and `r` minuses.

## 3. Exact biregularity

Every proper subset of a prime cyclic group has a full orbit of size `b`.
Partition the `(b-r)`-subsets on the column shore into their cyclic-rotation
orbits.  Lemma 2.1 gives exactly `b-r` `A`-first and `r` `B`-first columns
in every orbit, for every fixed row.  Rotating the `A` word instead gives
the identical statement for every fixed column.  In that calculation the
two candidate minima are `N_t-X_t` and `N_(t+1)-X_t`, where
`N_t=min_i(X_(i+t)+Y_i)`; `A`-first is now the negative increment.  Since
`N_b-N_0=a`, there are again exactly `b-r` such increments.

### Theorem 3.1 (exact orientation degrees)

The two GK orientation graphs are regular bipartite graphs with degrees

\[
 \boxed{
 D_r^A={b-r\over b}N_r={b-1\choose r},
 \qquad
 D_r^B={r\over b}N_r={b-1\choose{r-1}}.}            \tag{3.1}
\]

Their edge counts are respectively

\[
                  {b-r\over b}N_r^2,qquad
                  {r\over b}N_r^2,                 \tag{3.2}
\]

agreeing with the `u=0` orientation masses of the refined GK theorem.
At `r=0,b`, the same displayed algebraic degrees hold, but the unique
empty/full coordinate words have orbit size one.  These boundary splits are
handled separately below and are not covered by the necklace proof.

## 4. The exact max-weight factor reduction

Let

\[
 n_r=\max\left\{0,
 \left\lfloor{b-|2r-b|-H+2\over2}\right\rfloor\right\} \tag{4.1}
\]

be the number of persistent affine phase origins of either orientation.
The desired selected source count is

\[
 K_r={n_rN_r^2\over b}.                            \tag{4.2}
\]

Exact row and column regularity therefore asks for degree

\[
                         d_r={n_rN_r\over b}.        \tag{4.3}
\]

Primality makes `d_r` integral.  Also
`n_r<=min(r,b-r)` for `H>=1`, so `d_r<=D_r^A,D_r^B`.

### Theorem 4.1 (integral row/column phase-cap selection)

Each orientation graph contains a spanning `d_r`-factor.  If an edge has
top excess `k`, give it weight

\[
                         w_H(k)=\min(k,H).           \tag{4.4}
\]

A maximum-weight spanning `d_r`-factor exists and is obtained by an
integral min-cost bipartite flow.

This theorem is stated for `1<=r<=b-1`.  If `r=0` or `r=b` and `H>=1`,
then (4.1) gives `n_r=d_r=0`, so the required selection is empty.

#### Proof

A regular bipartite graph of degree `D` decomposes into `D` perfect
matchings.  The union of any `d_r` of them proves existence.  Equivalently,
the row--edge incidence constraints together with the column--edge
incidence constraints form the standard bipartite `b`-matching matrix,
which is totally unimodular.  Adding the linear objective (4.4) therefore
has an integral optimum.  \(\square\)

Because the selected edges are still chains of one GK decomposition, their
sources and every positive-rank target remain mutually distinct.  Thus
Theorem 4.1 adds exact row and column source balance without sacrificing
nestedness or integral target disjointness.

Top-excess-zero `B` edges are permitted as null bookkeeping assignments in
the factor.  They use no real target and are omitted if the retired-chain
hypergraph is defined only for retirement times at least one.  Thus the
formal source matrix is exactly regular, while its positive-target subgraph
need not remain regular after null assignments are erased.

### Proposition 4.2 (explicit coordinate-necklace diagonal factors)

Partition each shore into its orbits under cyclic relabelling of the fixed
coordinate indices.  Between one row necklace and one column necklace,
label the vertices `X_s,Y_t`, with `s,t in Z_b`.  The orientation of
`(X_s,Y_t)` depends only on `t-s`: simultaneous rotation moves the balanced
interleaved word by an even number of coordinates, which changes its
minimum depth by an even integer and preserves its orientation parity.

Consequently every necklace-pair block is a disjoint union of diagonal
perfect matchings

\[
                    \{(X_s,Y_{s+t}):s\in\mathbb Z_b\}.       \tag{4.5}
\]

Exactly `b-r` of these diagonals are `A`-first and exactly `r` are
`B`-first.  In every block and orientation, choose any `n_r` diagonals.
The union over all necklace pairs is a spanning `d_r`-factor.  Choosing the
`n_r` diagonals of greatest total weight in each block gives a completely
explicit feasible lower bound on the maximum in Theorem 4.1.

As in Theorem 4.1, this proposition assumes `1<=r<=b-1`; the two boundary
splits have the empty factor just described.

This is a coordinate-necklace decomposition, not a cyclic-wreath
decomposition.  A general rank-`r` subset necklace is not the interval deck
of a cyclic order.  Proposition 4.2 therefore remains at level 1 of the
three-level distinction in the status paragraph.

## 5. The extra-loss quantity is real

Let `U_(r,c)` be the sum of the `K_r` largest weights in orientation
`c in {A,B}`, with no row/column constraints, and let `F_(r,c)` be the
maximum `d_r`-factor weight.  Define

\[
                         \Gamma_{r,c}=U_{r,c}-F_{r,c}\ge0. \tag{5.1}
\]

The integral retirement theorem proves that the aggregate loss before the
new regularity requirement is `o(W_b)`.  To retain that conclusion at the
row/column-balanced level, the exact missing estimate is

\[
                         \sum_{r,c}\Gamma_{r,c}=o(W_b).     \tag{5.2}
\]

This does not follow merely from regularity.  The top-threshold subgraphs
are highly nonregular.  For example, at `(b,r)=(7,3)`, the `A`-first
subgraph induced by top excess at least two has row degrees ranging from
zero to nineteen, although the full `A` graph is `20`-regular.

Exact H100 min-cost-flow optima give the following finite diagnostics.
`extra` is `Gamma_(r,c)` and `L_r=N_r^2`.

\[
\begin{array}{c|c|c|c|c|c}
b&r&H&c&\Gamma_{r,c}&\Gamma_{r,c}/L_r\\ \hline
5&2&2&A&2&0.0200\\
5&2&2&B&0&0\\
7&3&2&A&28&0.0229\\
7&3&2&B&0&0\\
7&3&3&A&194&0.1584\\
7&3&3&B&109&0.0890\\
9&4&3&A&2238&0.1410\\
9&4&3&B&1425&0.0898
\end{array}                                           \tag{5.3}
\]

These rows are finite evidence only.  They prove that `Gamma` is not
identically zero, but neither prove nor disprove (5.2).

A uniform fractional `d_r/D_r^c` thinning is feasible, then integral by
the same polytope, but its weight bound uses the average length of all GK
chains and is too coarse in the DCC regime.  A proof of (5.2) must exploit
the abundance and placement of short-top edges, or construct low-cost
`(D_r^c-d_r)`-factors directly.

## 6. Scope beyond the d-factor

Theorem 4.1 is a source-matrix theorem.  Its row and column degrees match
the first necessary local multiplicities for product-wreath grouping.  It
does not partition a selected row into the prescribed affine phase
diagonals of one cyclic deck, and it does not require its selected edges to
come from common local cyclic orders.  Even such a diagonal decomposition
would still not pack the resulting full `b^2` translated product atoms
without collisions.

Accordingly the logical order is

\[
 \boxed{\text{GK }d\text{-factor}}
 \quad\longrightarrow\quad
 \boxed{\text{phase diagonals inside wreath decks}}
 \quad\longrightarrow\quad
 \boxed{\text{whole product-atom packing}}.          \tag{6.1}
\]

Only the first box, without the asymptotic cost estimate (5.2), is solved
here.  In particular, Theorem 4.1 must not be cited as fixed-order
coinstantiation.

## 7. H100 audit

The checker `scratch/audit_gk_orientation_biregularity_dfactor_20260821.py`
enumerates the rotation minima and literal GK orientations, verifies
Lemma 2.1 orbit by orbit, checks the exact row and column degrees through
`b=7`, and solves the finite max-weight `d`-factor instances in (5.3) by
the totally-unimodular linear program, verifying integral optima and the
displayed gaps.
