# Quartet trades between matching-cell partitions

## 1. Result and scope

Every perfect matching `P` of `[2m]` gives a canonical partition of the
middle layer into physical coordinate cubes: record which matching edges are
full, empty, and split.  A four-cycle switch

\[
                 ab,cd\quad\longleftrightarrow\quad ac,bd              \tag{1.1}
\]

relates the two resulting partitions by exact finite trades.

After fixing the common outside cell, the overlap components are classified
by the number `t` of selected quartet coordinates:

* `t=0,4`: one cell versus the same one cell;
* `t=1,3`: a two-versus-two square;
* `t=2`: a three-versus-three trade, consisting on each side of one
  four-state, two-dimensional local cube and two singleton local cells.

Choosing either entire side independently in every overlap component always
produces another partition of the middle layer into physical isometric
cubes.  The vertex-weighted cell-dimension distribution is unchanged.

On disjoint quartets these trades admit an exact product, or wreath,
construction with locally varying matching frames.  Almost every middle
vertex still lies in a cell of dimension at least

\[
                              {m\over2}-m^{2/3}.       \tag{1.2}
\]

A typical middle vertex has `(1/8+o(1))m` quartets on which switching the
local resolution changes whether it belongs to the large local cube or a
singleton.  This supplies a linear-density local mixing reservoir.  It does
not prove any lower- or upper-shadow coverage.

## 2. The matching-cell partition

Let `P` be a perfect matching.  For disjoint subfamilies `F,E subseteq P`
with

\[
                              |F|=|E|,                \tag{2.1}
\]

define

\[
 \mathcal C_P(F,E)=
 \left\{
   \bigcup_{e\in F}e\ \cup\
   \{\text{one chosen endpoint of every }e\in P\setminus(F\cup E)\}
 \right\}.                                           \tag{2.2}
\]

Every edge in `F` is full, every edge in `E` is empty, and all remaining
edges are split.  If `|F|=|E|=r`, then (2.2) is a physical isometric cube of
dimension

\[
                              m-2r.                  \tag{2.3}
\]

### Proposition 1 (canonical cell partition)

The nonempty cells (2.2) partition `binom([2m],m)`.

#### Proof

Every middle set uniquely classifies every matching edge as full, empty, or
split.  If the numbers are `f,e,s`, then

\[
 f+e+s=m,\qquad 2f+s=m,
\]

so `f=e`.  Conversely (2.1) makes every member of (2.2) an `m`-set.
Different status triples are disjoint.  QED.

## 3. The global balance equation for one quartet

Assume

\[
 P=\{ab,cd\}\cup P_0,\qquad
 Q=\{ac,bd\}\cup P_0,                               \tag{3.1}
\]

where `P_0` is the common matching on the other `2m-4` coordinates.

Fix disjoint outside full and empty families `F_0,E_0 subseteq P_0`; let

\[
 f_0=|F_0|,\quad e_0=|E_0|,\quad
 h=m-2-f_0-e_0.                                     \tag{3.2}
\]

The common outside factor is an `h`-cube on the split edges of `P_0`.
If a middle set uses `t` coordinates of `{a,b,c,d}`, then its outside part
has size `m-t`.  But the outside cell contributes

\[
 2f_0+h=m-2+f_0-e_0.
\]

Therefore a component exists exactly under the balance equation

\[
                         f_0-e_0=2-t.                \tag{3.3}
\]

This equation is the global condition that cannot be dropped.  It is the
same for `P` and `Q`, because the switch changes no outside edge.

Moreover, two `P`- and `Q`-cells can intersect only if their complete
outside full/empty/split statuses agree.  Hence every overlap component is
indexed by one exact pair `(F_0,E_0)` satisfying (3.3).

## 4. Complete local classification

Write a word such as `ab` for the local subset `{a,b}`.  In the table, a
braced list is the collection of local states forming one cell.

\[
\begin{array}{c|c|c|c}
t&f_0-e_0&P\text{-cells}&Q\text{-cells}\\ \hline
0& 2&\{\varnothing\}&\{\varnothing\}\\
1& 1&\{a,b\},\ \{c,d\}&\{a,c\},\ \{b,d\}\\
2& 0&\{ab\},\ \{cd\},\ \{ac,ad,bc,bd\}
    &\{ac\},\ \{bd\},\ \{ab,ad,bc,cd\}\\
3&-1&\{abc,abd\},\ \{acd,bcd\}
    &\{abc,acd\},\ \{abd,bcd\}\\
4&-2&\{abcd\}&\{abcd\}
\end{array}                                          \tag{4.1}
\]

Every displayed cell is multiplied by the common outside `h`-cube.

### Theorem 2 (overlap components)

For fixed `(F_0,E_0)` satisfying (3.3), all cells in the corresponding row
of (4.1) form one connected component of the bipartite overlap graph.
There are no other components.

More precisely:

1. At `t=0,4`, the two cells coincide.
2. At `t=1,3`, every cell on one side meets both cells on the other side in
   one local state, so the overlap graph is `K_(2,2)`.
3. At `t=2`, the overlap graph has three vertices on either side.  The two
   large local cubes meet in the two states `ad,bc`; each of the four
   singleton cells is a leaf attached to the opposite large cube.  Thus the
   five nonempty local intersection sizes are

   \[
                                2,1,1,1,1.           \tag{4.2}
   \]

#### Proof

The table follows by classifying the two local matching edges as full,
empty, or split.  Intersections are obtained by comparing the explicit
state lists.  Agreement of outside statuses is necessary, while the common
outside cube makes every listed local intersection nonempty.  The graphs in
the three cases are connected, and different outside statuses cannot be
joined.  QED.

The local cube dimensions on either side are identical as multisets:

\[
\begin{array}{c|ccccc}
t&0&1&2&3&4\\ \hline
\text{local dimensions}&(0)&(1,1)&(0,0,2)&(1,1)&(0).
\end{array}                                          \tag{4.3}
\]

## 5. Independent component switching

### Theorem 3 (quartet cell trade)

For every connected overlap component, choose either all of its `P`-cells
or all of its `Q`-cells.  The chosen cells, over all components, form an
exact partition of the middle layer into physical isometric cubes.

Every `P`-selected cell uses the local supports `ab,cd`; every `Q`-selected
cell uses `ac,bd`; all outside free supports remain the common matching
edges in `P_0`.  Choices in distinct components are completely independent.

#### Proof

Each side of one component partitions the same set

\[
 \mathcal C_{P_0}(F_0,E_0)
       \times\binom{\{a,b,c,d\}}t.                  \tag{5.1}
\]

Different components have disjoint unions, since any common middle set
would create an overlap edge between them.  Selecting one complete side per
component therefore covers every middle set once.

Every selected cell is one of the canonical cells of a perfect matching,
so its free pair supports are fixed and mutually disjoint.  It is therefore
a physical isometric cube.  QED.

By (4.3), switching one component preserves its complete vertex-weighted
dimension profile.  At `t=2`, for example, either side assigns
`4*2^h` vertices to dimension `h+2` and `2*2^h` vertices to dimension `h`.
Thus **every** independent switching pattern preserves the global
vertex-weighted dimension distribution exactly.

The number of nontrivial independently switchable components is

\[
 N_{\rm mix}
 =\sum_{t=1}^3[z^{\,2-t}](1+z+z^{-1})^{m-2}
 =\Theta(3^m/\sqrt m).                              \tag{5.2}
\]

The coefficient records the full/empty/split status of every outside edge.
Hence the construction produces `2^(N_mix)` hybrid cube partitions, though
this count by itself says nothing about shadows.

## 6. Product or wreath construction on disjoint quartets

Partition the first `4g` coordinates into disjoint quartets, where

\[
                              g=\lfloor m/2\rfloor. \tag{6.1}
\]

On quartet `j`, fix the two resolutions

\[
 P_j=(a_jb_j,c_jd_j),\qquad
 Q_j=(a_jc_j,b_jd_j).                               \tag{6.2}
\]

If `m` is odd, leave the final two coordinates as one additional unchanged
pair.

For a middle set, let `t_j` be its rank inside quartet `j`; in the odd case
let `u in {0,1,2}` be its rank on the final pair.  The admissible rank
vectors satisfy

\[
                    \sum_{j=1}^g t_j+u=m,           \tag{6.3}
\]

with the `u` term omitted when `m` is even.

For every admissible vector, independently choose a frame

\[
                    \epsilon(t_1,\ldots,t_g,u)
                         \in\{P,Q\}^g.              \tag{6.4}
\]

Partition each local `t_j`-slice using the corresponding side of (4.1),
use the trivial empty/free/full partition on the possible final pair, and
take Cartesian products of the local cells.

### Theorem 4 (quartet wreath partition)

For arbitrary choices (6.4), the product cells form an exact partition of
the middle layer into physical isometric cubes.  A product cell's free
support system is the disjoint union of the locally chosen `P_j` or `Q_j`
pairs and the possible final pair.

#### Proof

For a local cell at rank `t_j`, the number of full local pairs minus empty
local pairs is `t_j-2`, on either resolution.  The possible final pair has
imbalance `u-1`.  Equation (6.3) gives

\[
 \sum_j(t_j-2)+(u-1)=0,                              \tag{6.5}
\]

where the last term is omitted when `m` is even.  Thus every product cell
has equally many full and empty edges and lies in the middle layer.

Each chosen local partition covers its local rank slice once.  Their
Cartesian product covers the rank-vector sector once, and distinct vectors
are disjoint.  Local free pairs lie in disjoint quartets, so all physical
supports are fixed and pairwise disjoint.  QED.

There are exponentially many admissible rank-vector sectors (a central
coefficient of `(1+x+x^2+x^3+x^4)^g`, with the evident odd-pair factor).
Consequently one partition may use exponentially many different local
frames by varying (6.4).  This is genuine cellwise matching variation, but
not a theorem that those frames have any desired pseudorandom distribution.

## 7. Linear-density togglability

At local rank two, four of the six states change between a singleton and
the large local two-cube when the resolution is switched:

\[
                         ab,cd,ac,bd.                \tag{7.1}
\]

Call such a quartet togglable for the middle set `S`, and let `T(S)` be the
number of togglable quartets.  For a fixed quartet and uniform
`S in binom([2m],m)`,

\[
 \Pr(\text{togglable})
 =4{\binom{2m-4}{m-2}\over\binom{2m}m}
 ={m(m-1)\over(2m-1)(2m-3)}
 ={1\over4}+O(1/m).                                  \tag{7.2}
\]

Therefore

\[
 \mathbb E T
 =\lfloor m/2\rfloor,{m(m-1)\over(2m-1)(2m-3)}
 ={m\over8}+O(1).                                    \tag{7.3}
\]

The standard bounded-difference inequality on the uniform slice applies:
one selected/unselected transposition changes at most two quartet
indicators.  Hence, for an absolute `c>0`,

\[
 \Pr\{|T-\mathbb ET|\ge x\}
 \le2\exp(-c x^2/m).                                \tag{7.4}
\]

Taking `x=m^(2/3)` shows that all but
`exp(-Omega(m^(1/3)))W=o(W)` middle vertices have

\[
                         T(S)=(1/8+o(1))m.           \tag{7.5}
\]

Thus a typical vertex has linearly many local locations at which a frame
switch changes its cell status.  This is only a mixing opportunity; no
independence, diffusion law, or shadow balance is inferred.

## 8. Exact dimension law and tail

Let `D(S)` be the dimension of the partition cell containing `S`, under any
component-switching pattern of Theorem 3 or any rank-vector wreath choice of
Theorem 4.  The local dimension multiset (4.3) is the same on both sides, so
the complete vertex-weighted law of `D` is independent of every switch.
It equals the split-edge count for one fixed perfect matching:

\[
 \#\{S:D(S)=d\}
 =\binom md2^d
   \binom{m-d}{(m-d)/2},                             \tag{8.1}
\]

when `m-d` is even, and is zero otherwise.

Indicator calculation gives the exact first two moments, for `m>=2`:

\[
 \mathbb ED={m^2\over2m-1},                         \tag{8.2}
\]

and

\[
 \operatorname{Var}D
 ={2m^2(m-1)^2\over(2m-1)^2(2m-3)}
 ={m\over4}+O(1).                                    \tag{8.3}
\]

Indeed, one matching edge is split with probability `m/(2m-1)`, while two
specified edges are both split with probability

\[
                         {m(m-1)\over(2m-1)(2m-3)}.
\]

For the canonical fixed-matching partition, the split-edge count changes by
at most two under a selected/unselected transposition, so the uniform-slice
bounded-difference inequality gives

\[
 \Pr\{|D-\mathbb ED|\ge x\}
 \le2\exp(-c' x^2/m)                                \tag{8.4}
\]

for an absolute `c'>0`.  With `x=m^(2/3)`, all but `o(W)` vertices lie in
cells of dimension at least

\[
                         {m\over2}-m^{2/3}.           \tag{8.5}
\]

Every switched or wreath partition has exactly the same dimension histogram
as the canonical partition, so it inherits this tail even though its
cell-dimension function need not itself be Lipschitz under transpositions.
This proves (1.2).

## 9. Boundary of the result

The quartet trades prove an exact local mechanism for changing pair frames
at linear density while retaining a disjoint middle-layer cube partition.
They do not supply:

* standard binary-RSK radius purity;
* a radius-count ledger;
* lower- or upper-shadow injectivity across cells;
* compatible cyclic direction orders;
* a factor or pinning theorem;
* an asymptotic OR upper bound.

In particular, the linear number of togglable quartets is not itself a
proof that pair types mix uniformly.  That requires a separate global
selection or discrepancy theorem.

## 10. Finite audit

`scratch/check_quartet_cell_trade.py` exhaustively verifies through `m=7`:

1. both canonical matching-cell partitions;
2. every overlap component and all normalized intersection sizes;
3. the global balance equation;
4. arbitrary independent component switching;
5. exact preservation of the dimension histogram;
6. even and odd quartet-wreath products with independently chosen frames.

The checker validates the finite identities; the proofs above establish the
general statements.
