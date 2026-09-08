# Gate C: fixed-split crossing, maximal shallow factors, and integrality barriers

**Status (2026-08-22).**  The crossing theorem, the maximality implication,
the prime-modulus obstruction, and the linear-algebra calculation below are
proved.  They do not decide whether the all-split atom hypergraph has a
matching of density `1-o(1)`.  They do prove that three tempting shortcuts
cannot decide that question:

1. if a complete fixed-split central factor is available, it cannot be
   followed by a complete factor for another split, because it is already
   maximal;
2. perfect atom factors are impossible for every prime `b`, although this
   leaves open a factor with two or `o(W)` holes; and
3. the constant-vector/Gram-matrix use of the exact pair profile gives only
   the trivial packing bound, with equality at the fractional scale.

The sharper experimentally observed crossing bound `4(b-1)` is recorded at
the end as an open strengthening.  The proof here gives the unconditional
bound `2b`, which is already enough for maximality.

## 1. Product atoms and a fixed central band

Let

\[
 b=2h+1\ge5,
 \qquad |\Omega|=2b,
 \qquad \mathcal V={\Omega\choose b}.
\]

Choose a split `A disjoint union B=Omega` with `|A|=|B|=b`, and
oriented cyclic orders `alpha,beta` on the two blocks.  The associated
product atom is

\[
 E(A,\alpha,\beta)=
 \left\{I_\alpha(i,h)\cup I_\beta(j,h+1):
                 i,j\in\mathbb Z_b\right\}.            \tag{1.1}
\]

All `b^2` cells in (1.1) are distinct.  Fix a reference `b`-set
`P subset Omega` and define its two-slice central band

\[
 \mathcal C(P)=
 \{S\in\mathcal V:|S\cap P|\in\{h,h+1\}\}.            \tag{1.2}
\]

### Theorem 1.1 (every all-split atom crosses every fixed central band)

For every product atom `E` and every reference split `P`,

\[
                    |E\cap\mathcal C(P)|\ge 2b.         \tag{1.3}
\]

#### Proof

The band is unchanged when `P` is replaced by `Omega-P`, because every
`S in mathcal V` has

\[
 |S\cap(\Omega-P)|=b-|S\cap P|.
\]

We may consequently assume

\[
                   p:=|P\cap A|\le h.                  \tag{1.4}
\]

Write the membership indicators of `P cap A` in the order `alpha` as a
cyclic binary word with `p` ones, and let

\[
                   x_i=|I_\alpha(i,h)\cap P|.           \tag{1.5}
\]

The set `B-P` also has `p` elements.  The complement in `B` of a cyclic
`(h+1)`-interval of `beta` is a cyclic `h`-interval.  After an immaterial
cyclic reindexing, put

\[
 t_j=|(B-I_\beta(j,h+1))\cap(B-P)|.                    \tag{1.6}
\]

Thus `(t_j)` is also the sequence of length-`h` window counts of a cyclic
binary word with `p` ones.  Since `|B-P|=p`,

\[
 |I_\beta(j,h+1)\cap P|=h+1-p+t_j.                    \tag{1.7}
\]

It follows that the cell indexed by `(i,j)` belongs to `mathcal C(P)` if
and only if

\[
                       x_i+t_j\in\{p-1,p\}.             \tag{1.8}
\]

If `p=0`, all `b^2` pairs satisfy (1.8), so suppose `1<=p<=h`.  For each
`c in Z_b`, consider the diagonal `j=i+c` and the cyclic integer sequence

\[
                         y_i=x_i+t_{i+c}.                \tag{1.9}
\]

Every marked point lies in exactly `h` of the `b` cyclic `h`-intervals.
Therefore

\[
 \sum_{i\in\mathbb Z_b}y_i=2hp=p(b-1)=bp-p,            \tag{1.10}
\]

so the mean of `(y_i)` lies strictly between `p-1` and `p`.  Moving a
cyclic window one place deletes at most one marked point and inserts at
most one marked point.  Hence

\[
                         |y_{i+1}-y_i|\le2.              \tag{1.11}
\]

We claim that at least two terms of `(y_i)` lie in `{p-1,p}`.  If none
did, every term would lie either in

\[
 L=(-\infty,p-2]\cap\mathbb Z
 \quad\hbox{or}\quad
 H=[p+1,\infty)\cap\mathbb Z.
\]

No adjacent terms could lie on opposite sides by (1.11), so cyclic
connectedness would put every term on one side, contradicting the mean.
If there were exactly one central term, deleting its index would leave a
connected path; all remaining terms would again have to lie on one side.
If they all lay in `L`, then

\[
 \sum_i y_i\le p+(b-1)(p-2)=bp-2b+2<bp-p,              \tag{1.12}
\]

where the last inequality uses `p<=h`.  If they all lay in `H`, then

\[
 \sum_i y_i\ge (p-1)+(b-1)(p+1)=bp+b-2>bp-p.           \tag{1.13}
\]

Both conclusions contradict (1.10).  Thus every one of the `b` disjoint
diagonals contains at least two pairs satisfying (1.8), proving (1.3).
\(\square\)

### Corollary 1.2 (a complete fixed-band packing is already maximal)

Let `mathcal M` be any atom matching whose covered vertex set is exactly
`mathcal C(P)`.  Then `mathcal M` is inclusion-maximal in the full all-split
atom hypergraph.  More strongly, every further product atom meets its
covered set in at least `2b` vertices.

#### Proof

Apply Theorem 1.1 to the prospective new atom.  Since every vertex of
`mathcal C(P)` is already covered, the new atom is not disjoint from
`mathcal M`.  \(\square\)

Corollary 1.2 is conditional on the existence of the displayed exact band
packing.  In the current project ledger the required exact middle-wreath
factor is still a conditional/open input; it is **not** supplied by this
note.  The maximality implication itself uses only Theorem 1.1 and does not
import that input.

The size and density of the band are

\[
 |\mathcal C(P)|=2{b\choose h}^2,
 \qquad
 { |\mathcal C(P)|\over |\mathcal V|}
 = {2{b\choose h}^2\over {2b\choose b}}
 = {4+o(1)\over\sqrt{\pi b}}.                         \tag{1.14}
\]

Thus, conditional on one exact fixed-band factor, it would be a maximal
matching whose covered proportion tends to zero.  This does **not** bound
the maximum matching.  Unconditionally, Theorem 1.1 proves that the
strategy of sequentially installing complete central factors cannot get
past its first completed band; it does not prove that the first exact
factor exists.

## 2. A prime-modulus obstruction to a perfect atom factor

### Theorem 2.1 (coordinate congruence)

Let `b>=5` be prime.  No matching of product atoms covers all of
`mathcal V`.  If a matching leaves exactly two middle vertices uncovered,
then those two vertices are complements.

#### Proof

Fix a coordinate `z in Omega`.  In an atom (1.1), if `z in A`, exactly
`h` of the `b` cyclic `h`-intervals contain it and the other factor has
`b` choices.  Hence `z` occurs in `bh` cells of the atom.  If `z in B`, it
occurs in `b(h+1)` cells.  In either case its contribution is divisible by
`b`.  Consequently the number `c_z` of covered vertices containing `z` is
divisible by `b` for every atom matching.

The full middle-layer coordinate degree is

\[
 R={2b-1\choose b-1}
   =\prod_{i=1}^{b-1}{b+i\over i}\equiv1\pmod b,       \tag{2.1}
\]

because every `i=1,...,b-1` is invertible modulo the prime `b`.  If `u_z`
is the number of uncovered vertices containing `z`, then

\[
                         u_z=R-c_z\equiv1\pmod b.       \tag{2.2}
\]

A perfect factor would have `u_z=0`, contradicting (2.2).  If exactly two
vertices are uncovered, then `0<=u_z<=2<b`, so (2.2) forces `u_z=1` for
every coordinate.  The two uncovered `b`-sets therefore partition the
`2b` coordinates and are complements.  \(\square\)

More generally, if `m` vertices are uncovered, summing (2.2) only as a
lower bound gives

\[
                  bm=\sum_{z\in\Omega}u_z\ge2b,
\]

and hence `m>=2`.  This is a genuine integrality obstruction, but it is
compatible with matching density tending to one.

## 3. What the exact pair spectrum does and does not prove

Let `Q` be the `W by |mathcal E|` vertex/labelled-atom incidence matrix,
where

\[
 W={2b\choose b},\qquad k=b^2.
\]

Every column of `Q` has sum `k`, and every row has the common degree
`D=(b!)^2`.  Thus `Q Q^T` is determined by the exact distance-indexed pair
codegrees, and the all-ones vector is an eigenvector with eigenvalue `kD`.

### Proposition 3.1 (the constant eigenspace gives exactly the fractional
packing bound)

If `z` is the indicator of a matching of `t` labelled atoms, then

\[
                         t\le {W\over k}.              \tag{3.1}
\]

The same inequality is attained by the total weight of the uniform
fractional perfect matching, so this calculation gives no integral gap.

#### Proof

Since the selected columns have disjoint supports, `Qz` is a zero-one
vector with exactly `kt` ones.  Hence

\[
 \|Qz\|_2^2=kt,
 \qquad
 \langle\mathbf1,Qz\rangle=kt.
\]

Cauchy--Schwarz against the `W`-dimensional all-ones vector gives

\[
                    kt\ge{(kt)^2\over W},
\]

which is (3.1).  Uniform atom weight `1/D` has total weight `W/k`, by
double-counting incidences.  \(\square\)

Proposition 3.1 does not say that every spectral or representation-theoretic
argument must fail.  It says precisely that regularity, the constant
eigenspace, positive semidefiniteness of the Gram matrix, and the already
known pair profile do not by themselves separate integral from fractional
packing.  A useful spectral attack must exploit a nonconstant module together
with a nonlinear property of disjoint columns, or add higher-order incidence
information.

## 4. Generic local statistics cannot replace coordination

For completeness, the following construction records why regularity and
small normalized pair codegree, even with arbitrarily large absolute degree,
do not imply a near-factor in growing uniformity.

### Proposition 4.1 (regular small-codegree hypergraphs with tiny matchings)

Fix integers `k,D` with `D>=2` and

\[
                       k\ge64\log(2eDk).               \tag{4.1}
\]

For arbitrarily large `L` there is a `D`-regular `k`-uniform hypergraph on
`kL` vertices, with pair codegrees at most two, in which every matching
covers at most

\[
                        {16\log(2eDk)\over k}           \tag{4.2}
\]

of the vertices.

#### Proof

Let `X` have size `LD`, and choose `k` independent uniform equipartitions
of `X` into `L` blocks of size `D`.  Blocks from different partitions have
intersection at most two with probability `1-o(1)`: for a fixed block pair,
the probability of an intersection of size at least three is at most

\[
                       {{D\choose3}^2\over {LD\choose3}},
\]

and a union bound over `O(k^2L^2)` pairs tends to zero.

Put `Q_0=log(2eDk)`, `c=16Q_0/k`, and `s=ceil(cL)`.  For a fixed `s`-set
`Y subset X`, the probability that one partition puts its points in
distinct blocks is

\[
 p_s={(L)_sD^s\over(LD)_s}
     \le \exp\{-s(s-1)/(4L)\}.                        \tag{4.3}
\]

Indeed, the logarithm of the factor indexed by `i` is

\[
 f_D(i/L)=\log(1-i/L)-\log(1-i/(LD)),
\]

and for `0<=x<1`,

\[
 f_D'(x)=-{D-1\over(1-x)(D-x)}\le-\tfrac12.
\]

Summing from `i=0` to `s-1` proves (4.3).  Independence of the partitions
and `binom(LD,s)<=(eLD/s)^s` show that the expected number of `s`-sets
which meet every block in at most one point is at most

\[
 {LD\choose s}p_s^k
 \le\left({eLD\over s}\right)^s
       \exp\{-ks(s-1)/(4L)\}=o(1).                    \tag{4.4}
\]

For all sufficiently large `L`, (4.1) gives `c<=1/4`,
`k(s-1)/(4L)>=2Q_0`, and
`log(eLD/s)<=log(eD/c)<=Q_0`, which justifies the last equality.  Hence
deterministic partitions exist with both required properties.

Make one hypergraph vertex for every block, one vertex part for every
partition, and for each `x in X` make the `k`-edge consisting of the `k`
blocks containing `x`.  Every block contains `D` points, so the hypergraph
is `D`-regular.  Two block vertices from different parts lie together in
at most two edges, while same-part pairs have codegree zero.  A matching of
edges labels a set of points of `X` meeting every partition block at most
once, so it has fewer than `cL` edges.  Since the hypergraph has `kL`
vertices, its covered proportion is less than `c`, proving (4.2).
\(\square\)

Taking `D=k` (for all sufficiently large `k`, condition (4.1) then holds)
makes the normalized pair-codegree at most `2/k`.  At the Gate-C scale
`k=b^2`, Proposition 4.1 therefore shows that an argument using only
regularity and an `O(1/k)` normalized pair-codegree bound cannot prove a
near-factor.  It does not apply as an upper bound to the product atoms,
whose torus structure and symmetric-group orbit are much stronger.

## 5. Consequences for the next Gate-C attack

The proved facts leave the actual maximum matching density open.  They
narrow a viable positive proof to a coordinated construction with at least
one of the following genuinely global ingredients:

- simultaneous selection across many splits, rather than completing one
  split before touching the next;
- bounded-size or multiscale exchanges which, if an exact fixed-band factor
  is used as a starting point, deliberately dismantle the resulting shallow
  maximal matching from Corollary 1.2;
- an absorber that is sensitive to the coordinate residues in Theorem 2.1;
  or
- higher-order orbit/representation information not contained in the pair
  Gram matrix.

In particular, fragmenting atoms and then independently thinning the
residual cannot address Corollary 1.2: the obstruction is an integral
maximality phenomenon, not a failure of initial degree or codegree balance.

## 6. Open sharp crossing multiplicity

Exhaustive enumeration of the two cyclic binary window histograms for every
odd `b<=17` gives

\[
 \min_{P,E}|E\cap\mathcal C(P)|=4(b-1),               \tag{6.1}
\]

with equality for contiguous membership patterns.  After the reduction in
the proof of Theorem 1.1, (6.1) is exactly the following one-dimensional
occupation-convolution assertion.

> Let `x_i,t_j` be the length-`h` cyclic window counts of two binary words
> of length `b=2h+1`, each having `p<=h` ones.  Then the number of pairs
> `(i,j)` for which `x_i+t_j in {p-1,p}` is at least `4(b-1)`.

The elementary diagonal argument proves `2b`, not (6.1).  Therefore (6.1)
is not used anywhere above and must not yet be entered into the proved
Gate-C ledger.
