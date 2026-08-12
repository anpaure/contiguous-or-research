# The symmetric vortex halo has a simple spanning 2-factor

## Status

The symmetric product halo from the balanced-coordinate vortex theorem has
two edge-disjoint owner/root perfect matchings for every fixed halo radius
and all sufficiently large middle ranks.  The proof is explicit at the
fractional level: a normalized product flow has every edge weight
`O_p(1/r)`.  Doubling it and using bipartite `b`-matching integrality gives
a simple spanning 2-factor.

This closes the uncoloured owner/root factor inside the halo.  It does **not**
bound the number of cycles, and it does not automatically give distinct or
complete immediate-upper colours.  The natural upper-decorated constraint
matrix already contains a determinant-two minor inside the core slice.
Thus the coloured lift remains a real integral gate, not a consequence of
the two perfect matchings.

The exact core slice is better: it is a smaller middle-levels problem and
inherits the full `D+2` fractional packet factor, including upper colours
and all central chain tickets.

## 1. Product model of the symmetric halo

Fix disjoint sets `A,B subset [2r-1]` of common size `a`, and let

\[
 \mathcal H_s^{p,p}(A,B)=
 \{X\in\tbinom{[2r-1]}s:|A-X|\le p,\ |B\cap X|\le p\},    \tag{1.1}
\]

where `0<=p<=a`.  Put

\[
 g=r-a,\qquad N=2g-1,\qquad
 P=\mathcal B_a^{\le p},\qquad R=P^{\rm op}\times P.       \tag{1.2}
\]

As in the coordinate-vortex theorem, the entire halo poset is

\[
                              R\times\mathcal B_N.          \tag{1.3}
\]

The poset `R` has rank `2p`.  It is rank-symmetric and normal: each factor
has the normalized matching property and a log-concave rank sequence, and
the standard product theorem preserves these properties.  Write

\[
                         h_j=|R_j|,\qquad0\le j\le2p.       \tag{1.4}
\]

Then

\[
 h_j=h_{2p-j},\qquad
 h_0\le h_1\le\cdots\le h_p.                              \tag{1.5}
\]

For every `j<2p`, normality gives a normalized flow

\[
 \phi_j:E(R_j,R_{j+1})\longrightarrow\mathbb R_{\ge0}     \tag{1.6}
\]

with

\[
 \sum_{z':zz'\in E}\phi_j(zz')={1\over h_j},\qquad
 \sum_{z:zz'\in E}\phi_j(zz')={1\over h_{j+1}}.           \tag{1.7}
\]

The two central total ranks of (1.3) are

\[
                         m=g+p-1,\qquad m+1=g+p.            \tag{1.8}
\]

They correspond exactly to set-ranks `r-1` and `r` in (1.1).

## 2. An explicit small-edge fractional perfect matching

For boundary rank `j`, a lower central vertex has neutral rank

\[
                         k_j=m-j=g+p-1-j.                  \tag{2.1}
\]

Let

\[
 L_j=h_j\binom N{k_j},\qquad
 U_j=h_j\binom N{k_j+1}.                                  \tag{2.2}
\]

These are the numbers of lower and upper central vertices having boundary
rank `j`.  Define the cumulative imbalance

\[
                         F_j=\sum_{i=0}^j(L_i-U_i).         \tag{2.3}
\]

Rank symmetry gives

\[
 F_j\ge0,\qquad F_{2p}=0,\qquad
 F_j=F_{2p-j-1}\quad(0\le j<2p).                          \tag{2.4}
\]

Set

\[
 a_j={F_j\over L_j}\quad(0\le j<2p),\qquad a_{2p}=0,      \tag{2.5}
\]

and

\[
 b_0=0,\qquad b_{j+1}={F_j\over U_{j+1}}.                 \tag{2.6}
\]

The letters `a_j,b_j` here are flow fractions and are unrelated to the
anchor-bank size `a`.

### Lemma 2.1 (uniform small boundary current)

For fixed `p` and all `g` large enough,

\[
 0\le a_j,b_j\le \varepsilon,
 \qquad
 \varepsilon={2p(p+1)\over g}.                            \tag{2.7}
\]

#### Proof

For `i<=p`, direct cancellation gives

\[
 {U_i\over L_i}={g-p+i\over g+p-i},\qquad
 L_i-U_i=L_i{2(p-i)\over g+p-i}.                          \tag{2.8}
\]

Both `h_i` and the relevant neutral binomial coefficient are nondecreasing
for `i<=p`; hence `L_i<=L_j` whenever `i<=j<=p`.  Therefore

\[
 F_j\le {2p\over g}\sum_{i=0}^jL_i
      \le {2p(p+1)\over g}L_j.                            \tag{2.9}
\]

Also `U_{j+1}/L_j=h_{j+1}/h_j>=1`, so the same estimate holds for
`b_(j+1)`.  For `j>=p`, use (2.4) and

\[
 L_j=U_{2p-j},                                             \tag{2.10}
\]

reducing the assertion to the preceding half. \(\square\)

### Theorem 2.2 (small-edge central flow)

The central incidence graph of the symmetric halo has a fractional perfect
matching in which every edge has weight at most

\[
 \boxed{
 \gamma=\max\!\left\{{1\over g-p},{2p(p+1)\over g}\right\}.} \tag{2.11}
\]

#### Proof

There are two kinds of central incidence edge.

* A **neutral edge** fixes `z in R_j` and adds one neutral coordinate.
  Give every such edge weight

  \[
                 w_j={1-a_j\over N-k_j}.                  \tag{2.12}
  \]

* A **boundary edge** fixes the neutral set `Y` and uses
  `zz' in E(R_j,R_(j+1))`.  Give it weight

  \[
                         a_jh_j\phi_j(zz').                \tag{2.13}
  \]

The boundary row sum at every lower vertex of boundary rank `j` is `a_j`;
the boundary column sum at every upper vertex of boundary rank `j+1` is

\[
                       a_j{h_j\over h_{j+1}}=b_{j+1}.      \tag{2.14}
\]

Thus every lower vertex has total weight

\[
                 a_j+(N-k_j)w_j=1.                        \tag{2.15}
\]

The recurrence `F_j=F_(j-1)+L_j-U_j` is equivalent to

\[
 1-a_j={U_j\over L_j}(1-b_j)
       ={N-k_j\over k_j+1}(1-b_j).                        \tag{2.16}
\]

Hence every upper vertex also has total weight

\[
                 b_j+(k_j+1)w_j=1.                        \tag{2.17}
\]

This proves fractional perfection.  A neutral edge has weight at most
`1/(g-p)`.  From (1.7), every boundary edge has weight at most `a_j`, and
Lemma 2.1 gives the other term in (2.11). \(\square\)

## 3. Two edge-disjoint perfect matchings

### Theorem 3.1 (simple spanning 2-factor in the halo)

If

\[
                        g\ge4p(p+1),\qquad g-p\ge2,        \tag{3.1}
\]

then the owner/root incidence graph between

\[
 \mathcal H_{r-1}^{p,p}(A,B)
 \quad\text{and}\quad
 \mathcal H_r^{p,p}(A,B)                                  \tag{3.2}
\]

contains a simple spanning `2`-factor.  Equivalently, it contains two
edge-disjoint perfect matchings.

#### Proof

Under (3.1), `2gamma<=1`.  Double every weight from Theorem 2.2.  The
resulting point satisfies

\[
 0\le x_e\le1,
 \qquad
 \sum_{e\ni v}x_e=2\quad\text{for every vertex }v.        \tag{3.3}
\]

The vertex-edge incidence matrix of a bipartite graph is totally
unimodular.  Therefore the capacitated bipartite `b`-matching polytope
defined by (3.3) has an integral extreme point.  At such a point every
edge variable is zero or one and every vertex has degree two.  This is a
simple spanning `2`-factor.  Alternately colouring every even cycle gives
two edge-disjoint perfect matchings. \(\square\)

For the vortex radius `p=3`, this applies once `r-a>=48`.  Thus the entire
`O(W polylog(r)/sqrt(r))` reserve has an exact uncoloured incidence
factor; no asymptotic or divisibility defect remains at this level.

## 4. What the theorem does and does not control

The integral extreme-point argument has no topological objective.  Its
`2`-factor can have many cycles.  Deleting one edge from every cycle gives
a spanning linear forest, but the number of components is exactly the
uncontrolled cycle count.  Neither normality nor total unimodularity bounds
that number.

This is not a known obstruction to a Hamilton halo factor.  At `p=0` the
graph is the ordinary middle-levels graph and is Hamiltonian.  What remains
open is a product-middle-levels connector theorem saying that the factor in
Theorem 3.1 can be chosen with `O(1)` components, or that its cycles admit
enough alternating product squares to merge to `O(1)`.

There is nevertheless a useful locality statement.  If a root `Q` and its
two selected owners belong to the symmetric `p`-halo, their upper colour
`U` satisfies

\[
                         \alpha(U)\le p,
                    \qquad\beta(U)\le p+1.                 \tag{4.1}
\]

Indeed, taking a union cannot lose another `A`-coordinate.  If
`beta(Q)=p`, neither selected owner may add a `B`-coordinate; otherwise the
two additions increase `beta` by at most two, whose maximum is `p+1`.
Thus arbitrary upper damage stays in one slightly enlarged product halo.

There is no scalar shortage for the upper targets which remain in the
symmetric halo.  Rank unimodality of (1.3) gives

\[
 |\mathcal H_{r+1}^{p,p}(A,B)|
 \le |\mathcal H_r^{p,p}(A,B)|.                           \tag{4.2}
\]

The right side is exactly the number of upper occurrences produced by a
spanning `2`-factor (one at each root).  In particular the genuinely
packet-affected upper bank `mathcal H_(r+1)^(1,2)` lies inside the scalar
budget when `p=3`.  The obstruction below is correlation, not count.

## 5. Upper decoration is not supplied by b-matching integrality

At a root `Q`, selecting two distinct owner neighbours `Q+x,Q+y` chooses
the upper colour

\[
                              U=Q+\{x,y\}.                  \tag{5.1}
\]

Introduce a diamond variable `z_(Q,U)`.  The root and owner degree equations
are exactly the bipartite `2`-factor equations, but upper coverage adds
rows indexed by `U`.

### Proposition 5.1 (the coloured halo matrix is not TU)

Already inside the core slice `p=0`, the root/owner/upper diamond matrix
contains a minor of determinant `2`.

#### Proof

Choose a core-slice root `Q` and three neutral labels `x,y,z` outside it.
Use the three columns

\[
 z_{Q,Q+\{x,y\}},\qquad z_{Q,Q+\{x,z\}},\qquad
 z_{Q,Q+\{y,z\}}
\]

and the three owner rows `Q+x,Q+y,Q+z`.  The resulting matrix is

\[
 \begin{pmatrix}
 1&1&0\\1&0&1\\0&1&1
 \end{pmatrix},                                           \tag{5.2}
\]

whose determinant is `-2`.  All six sets contain `A` and avoid `B`, so the
minor is internal to the core slice. \(\square\)

Thus the proof of Theorem 3.1 cannot simply append upper rows and invoke
the same integrality theorem.  An arbitrary pair of disjoint perfect
matchings need not be upper-surjective.  Chain tickets are still more
structured: they require grouping incidence edges into literal `D+2`
source rings.  Neither property is encoded in the uncoloured product graph.

## 6. Exact self-similarity of the core slice

Although the full product halo has only the uncoloured theorem above, its
core has the complete fractional packet structure.

### Theorem 6.1 (core-slice packet recursion)

Let `C=[2r-1]-(A union B)`, so `|C|=2g-1`.  Identify

\[
 \mathcal S_r(A,B)=
 \{A\cup Y:Y\in\tbinom Cg\},\qquad
 \mathcal S_{r-1}(A,B)=
 \{A\cup Y:Y\in\tbinom C{g-1}\}.                          \tag{6.1}
\]

Apply the all-parity `D+2` packet construction on `C` with owner rank `g`
and adjoin `A` to its common core.  Provided `g>=D+2`, this gives a literal
packet family entirely inside the coordinate slice with:

1. an exact fractional owner/root factor;
2. immediate-upper raw load `(g+1)/(g-1)` and exact symmetric marking;
3. all proper central interval tickets, with the same source width `D`;
4. no occurrence containing a coordinate of `B`.

#### Proof

For a neutral packet choose

\[
 K_0\subset H_0\subset C,
 \qquad |K_0|=g-D,\quad |H_0|=g+2.                        \tag{6.2}
\]

Then `K=A union K_0` has size `r-D`, and `H=A union H_0` has size
`r+2`, exactly the original packet parameters.  Every owner, root, upper
colour, and proper interval union contains `A` and avoids `B`.  Removing
the fixed `A` recovers verbatim the two-hole packet theorem with `r`
replaced by `g`. \(\square\)

Theorem 6.1 means that the vortex core is not merely a small exceptional
bank: it is a recursively self-similar instance carrying the full
fractional upper/chain ledger.  The remaining bridge is integral and
correlated:

> choose the product-halo `2`-factor so that its diamonds cover the required
> upper bank, lift its edges into compatible `D+2` packet rings, and merge
> the resulting cycles while retaining the core-slice recursion.

Theorem 3.1 removes owner/root existence from that bridge.  Proposition
5.1 shows why upper marking and chain-ring grouping remain separate.
