# Independent audit of quartet wreath diffusion

## 0. Verdict

The three-resolution quartet construction is a valid exact partition
mechanism.  After the repairs listed below, its rigorous content is:

* all three perfect matchings of a quartet give the claimed local cube
  resolutions;
* an arbitrary resolution vector may be chosen separately for every
  admissible local-rank sector, and the resulting product cells partition
  the middle layer;
* for a fixed set and a random sector frame, the full-pair statistic has the
  stated shifted binomial law;
* dually, for a fixed deterministic frame and a uniformly random set inside
  one sector, the same binomial law is exact;
* every deterministic frame function has exactly the canonical
  fixed-matching cell-dimension histogram, so the large-cell tail is
  universal rather than merely existential; and
* one deterministic frame function gives `Omega(m)` genuinely nonreference
  free supports at all but `e^{-Omega(m)}W` middle vertices.

Two corrections were required in `QUARTET_WREATH_DIFFUSION.md`.

1. For odd `m`, the leftover pair is free only in its local rank-one sector,
   and it contributes `1_{\{u=2\}}` to the full-pair statistic.
2. Section 4 previously obtained one good frame by averaging.  The audited
   cell trade gives the stronger exact statement that **every** frame has
   the same dimension histogram.

The construction genuinely lies outside the hypotheses of
`PIVOT_SHADOW_CAPACITY.md`: there is no single native frame controlling all
sectors, and a deterministic choice can have linearly many nonnative free
directions in almost every cell.  This only invalidates that theorem as an
obstruction to the new construction.  It does not prove shadow coverage,
shadow injectivity, suitable cyclic orders, or an OR upper bound.

## 1. Three local resolutions

Let `Q={a,b,c,d}` and

\[
 P_0=ab|cd,\qquad P_1=ac|bd,\qquad P_2=ad|bc.
\]

For any `P_i`, fixing which of its two edges are full, empty, or split
partitions every local rank slice into physical pair-flip cubes.  The
cell-dimension multisets at ranks zero through four are

\[
 (0),\quad(1,1),\quad(0,0,2),\quad(1,1),\quad(0).     \tag{1.1}
\]

For any two distinct resolutions, coordinate relabelling reduces their
comparison to `P_0` versus `P_1`.  The audited overlap graphs are:

* one common cell at ranks zero and four;
* `K_{2,2}` at ranks one and three; and
* one connected three-versus-three graph at rank two, with normalized
  intersection sizes `2,1,1,1,1`.

Thus every pair among the three resolutions is a complete local partition
trade.  The use of three choices in the wreath note is not an extrapolation
from a special asymmetric pair.

## 2. Rank-vector product partition

First let `m=2g` and partition the ground coordinates into `g` quartets.
For

\[
 t=(t_1,\ldots,t_g),\qquad t_j\in\{0,1,2,3,4\},
 \qquad\sum_jt_j=2g,                                 \tag{2.1}
\]

choose any frame vector `eta(t) in {0,1,2}^g`.  Each chosen local
resolution partitions its rank-`t_j` slice, so their Cartesian products
partition the complete sector `Omega_t`.  Different sectors are disjoint.

There is also an exact global matching-cell check.  If a chosen local cell
has `f_j` full and `e_j` empty frame edges, then

\[
 f_j-e_j=t_j-2.                                      \tag{2.2}
\]

Equation (2.1) gives `sum_j(f_j-e_j)=0`.  Hence every product cell has
equal total numbers of full and empty pairs and is a genuine middle-layer
physical cube.

For odd `m`, let `g=(m-1)/2` and reserve one final pair of local rank
`u in {0,1,2}`.  It is empty, free, or full according as `u=0,1,2`.
The admissibility condition

\[
 \sum_jt_j+u=m
\]

is equivalent to

\[
 \sum_j(t_j-2)+(u-1)=0.                              \tag{2.3}
\]

This proves the odd product partition as well.  The original phrase
“inessential fixed final direction” was inaccurate: it is a free direction
only when `u=1`.

The frame may depend on the complete rank vector, but not on an individual
vertex after the cells are formed.  That distinction is essential.

## 3. Exact full-pair law

Fix a sector and a set `S` in it.  Choose the `g` coordinates of its frame
independently and uniformly from the three local resolutions.  Let `n_i(S)`
count its rank-`i` quartets.  Locally:

* ranks zero and one contain no frame edge;
* a rank-three state contains exactly one edge of every frame;
* rank four contains both frame edges; and
* a rank-two state is an edge of exactly one of the three frames.

Therefore

\[
 F_\eta(S)
 ={\bf1}_{\{u=2\}}+n_3(S)+2n_4(S)
    +\operatorname{Bin}(n_2(S),1/3),                 \tag{3.1}
\]

with the first term omitted for even `m`, and

\[
 \operatorname{Var}_\eta F_\eta(S)=\frac29n_2(S).   \tag{3.2}
\]

This is an exact marginal law for each fixed `S`.  Different sets in the
same sector use the same frame vector and are generally correlated.

There is a useful deterministic dual.  Fix `eta(t)` and choose `S` uniformly
from `Omega_t`.  At every rank-two quartet, two of the six local states are
frame edges.  The sector is a Cartesian product, so the Bernoulli variables
are independent and (3.1) again holds exactly.

For a uniform middle set,

\[
 \mathbb E n_2
 =g\,6\frac{\binom{2m-4}{m-2}}{\binom{2m}{m}}
 =\left(\frac3{16}+o(1)\right)m.                    \tag{3.3}
\]

A slice bounded-difference estimate implies concentration on every fixed
linear-width band around this mean.  Letting the relative width tend slowly
to zero gives

\[
 n_2=(3/16+o(1))m
\]

outside `o(W)` vertices, so (3.2) is
`(1/24+o(1))m` there.

This proves square-root-scale marginal variation.  It does not select one
frame that balances every target simultaneously.

## 4. A deterministic linearly re-paired partition

The availability of three frames can be made integral, rather than left as
a fractional slogan.  Fix `P_0` on every quartet as a reference.  For a
middle set `S` and a random frame for its sector, let `Y_j` be the number of
free local supports in quartet `j` which are not reference edges.

At ranks one and three, `Y_j=1` with probability `2/3`.  At rank two it is
zero or two and has expectation at least `2/3` for every local state.  It is
zero at ranks zero and four.

Let `A(S)` count quartets of ranks one, two, or three.  Its mean is
`(7/8+o(1))g`, and slice concentration gives

\[
 A(S)\ge3g/4                                         \tag{4.1}
\]

outside `e^{-Omega(m)}W` sets.  Conditional on (4.1), the independent
bounded variables `Y_j` have total mean at least `g/2`, so

\[
 \Pr_\eta\{\sum_jY_j<g/4\}=e^{-\Omega(m)}.           \tag{4.2}
\]

Averaging (4.2) over `S` and fixing one outcome proves that some
deterministic frame function has at least `g/4=Omega(m)` nonreference free
directions at all but `e^{-Omega(m)}W` vertices.

This statement concerns available directions in the containing cells.  It
does not say a later cycle factor uses a positive fraction of them in every
short window.

## 5. Exact dimension histogram and tail quantifiers

Equation (1.1) is identical for all three resolutions.  It remains
identical under Cartesian products, separately in every rank-vector sector.
Therefore every deterministic frame function has exactly the same
vertex-weighted dimension histogram as one fixed global matching.

For that canonical matching, a cell has dimension `d` exactly when `d`
matching edges are split.  Hence for every wreath frame `eta`,

\[
 \#\{S:D_\eta(S)=d\}
 =\binom md2^d\binom{m-d}{(m-d)/2},                 \tag{5.1}
\]

with zero count when `m-d` is odd.  In particular,

\[
 \mathbb E D_\eta=\frac{m^2}{2m-1}
 =\frac m2+O(1).                                     \tag{5.2}
\]

The canonical split count is two-Lipschitz under a selected/unselected
transposition on the uniform middle slice.  Thus

\[
 \Pr\{D_\eta<m/4\}=e^{-\Omega(m)}                    \tag{5.3}
\]

for every deterministic `eta`, by transferring the canonical tail through
the exact histogram identity.

The original averaging argument was logically sufficient to prove the
existence of one good frame, but unnecessarily weak.  Equations
(5.1)--(5.3) establish the correct universal quantifier.

## 6. Relation to the pivot-capacity theorem

`PIVOT_SHADOW_CAPACITY.md` assumes all of the following:

1. cells belong to the nonlocal-pivot BK partition and carry an RSK radius;
2. one global native matching defines the type statistic `F` for every
   cell;
3. a radius-`d` cell has at most `d/2` nonnative pivot directions; and
4. the retained radii satisfy `D/H to 0`, so almost every depth-`q` window
   uses `o(q)` pivots.

The quartet wreath construction is not a member of this structural class.
It has no established RSK radius label, its locally controlling frame
depends on the rank-vector sector, and Section 4 gives a deterministic
choice with `Omega(m)` nonreference free supports in the cells containing
all but `e^{-Omega(m)}W` middle vertices.
One may of course still define the full-pair statistic of any fixed
reference matching, but the pivot theorem's `o(q)` displacement estimate is
then unavailable: the number of nonreference directions is no longer
`O(d)=o(H)`.

This is a genuine escape from the **hypotheses** and from that particular
capacity proof.  It is not a contradiction to the theorem.  In particular:

* a cell may contain many nonreference directions while a chosen cyclic
  factor uses too few of them;
* the binomial law is relative to sector-dependent frames, not one global
  target statistic;
* no radius quotas, direction orders, or cross-cell shadow collision bounds
  are supplied; and
* a different capacity theorem adapted to sector-dependent frames may still
  exist.

Thus the correct ledger entry is:

\[
 \text{pivot-capacity obstruction not applicable}
 \quad\not\Longrightarrow\quad
 \text{shadow coverage}.                             \tag{6.1}
\]

## 7. Machine and source audit

`scratch/check_quartet_cell_trade.py` was extended to use all three local
resolutions, verify the local full-pair histograms, and test even and odd
rank-vector products.  Exhaustive runs through `m=7` pass.

The source note was patched to:

* include the odd-pair balance and full-pair correction;
* state both forms of the binomial law and its typical variance;
* add the deterministic linear re-pairing corollary;
* replace the existential dimension tail by the exact universal histogram;
  and
* scope the escape from `PIVOT_SHADOW_CAPACITY.md` without claiming any
  shadow theorem.
