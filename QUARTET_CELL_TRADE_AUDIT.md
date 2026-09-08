# Independent audit of the quartet cell trade

## 1. Verdict

The local four-cycle trade and its disjoint-quartet wreath extension are
valid.

Accepted conclusions:

* the fixed-matching full/empty/split cells partition the middle layer;
* every overlap component of one four-cycle switch has the stated
  `1-versus-1`, `2-versus-2`, or `3-versus-3` form;
* the outside balance equation is necessary and sufficient;
* choosing either complete side independently in every component gives a
  physical isometric cube partition;
* arbitrary rank-vector product resolutions on disjoint quartets give an
  exact wreath partition, including the odd-`m` leftover-pair case;
* switching preserves the full vertex-weighted cell-dimension histogram;
* almost every vertex lies in a cell of dimension at least
  `m/2-m^(2/3)`;
* a typical vertex has `(1/8+o(1))m` dimension-changing local quartet
  opportunities.

Rejected inference:

* linear-density local switches do not by themselves prove type diffusion,
  shadow injectivity, radius resolution, or an OR construction.

One proof detail was repaired during audit: after arbitrary component
choices, the dimension assigned to a vertex need not be Lipschitz under a
slice transposition.  The concentration theorem is applied to the canonical
split count, and then transferred by exact histogram equality.

## 2. Canonical cell and balance audit

For a fixed matching, an `m`-set has `f` full, `e` empty, and `s` split
edges.  The equations

\[
 f+e+s=m,qquad2f+s=m
\]

give `f=e`.  Thus full and empty edge families uniquely index one physical
cube and all such cubes partition the middle layer.

After isolating the switched quartet, an outside status with `f_0,e_0,h`
has

\[
 f_0+e_0+h=m-2,qquad
 |S_{\rm out}|=2f_0+h=m-2+f_0-e_0.
\]

If the quartet rank is `t`, middle rank requires

\[
                         f_0-e_0=2-t.
\]

This equation is independent of which of the two local matchings is used.
It also shows that one fixed outside status belongs to exactly one `t`
layer; components at different local ranks cannot accidentally merge.

## 3. Local table audit

For `P=(ab,cd)` and `Q=(ac,bd)`, direct classification gives:

* `t=0,4`: one fixed state on either side;
* `t=1`: `P` groups singleton states as `ab|cd`, while `Q` groups them as
  `ac|bd`; this is `K_(2,2)`;
* `t=3`: the complementary `K_(2,2)`;
* `t=2`: `P` has singleton states `ab,cd` and the four-state cell
  `ac,ad,bc,bd`; `Q` has singleton states `ac,bd` and the four-state cell
  `ab,ad,bc,cd`.

At `t=2`, the two four-state cells intersect in `ad,bc`; each singleton is
contained only in the opposite four-state cell.  Hence the overlap graph is
connected with five edges and normalized intersection sizes

\[
                              2,1,1,1,1.
\]

Multiplication by the common outside `h`-cube multiplies every intersection
size by `2^h` without changing connectivity.

The local dimension multisets are exactly

\[
 (0),\quad(1,1),\quad(0,0,2),\quad(1,1),\quad(0).
\]

In particular, “four-state cube” means a two-dimensional cube, not a
four-dimensional cube.

## 4. Independent-component quantifier

The two sides of one connected overlap component are distinct partitions
of the same set

\[
 \mathcal C_{P_0}(F_0,E_0)\times
 \binom{\{a,b,c,d\}}t.
\]

Different connected components have disjoint unions: otherwise a cell on
one side of the first and a cell on the other side of the second would
intersect and create an overlap edge.  Consequently one may choose the
entire `P` side or entire `Q` side independently in every component.

It would generally be invalid to choose arbitrary individual cells from
both sides of one component.  The theorem does not claim that stronger
operation.

Each chosen cell inherits one fixed set of disjoint pair supports from its
side, so abstract partition validity and physical isometry are both proved.

The number of nontrivial components is the sum of the three central
coefficients of `(1+z+z^(-1))^(m-2)`.  The local central-limit estimate gives
`Theta(3^m/sqrt(m))`, so the stated number of independent binary choices is
correct.

## 5. Wreath balance and partition audit

For `g=floor(m/2)` disjoint quartets, a local rank-`t_j` cell has

\[
 \#\text{full pairs}-\#\text{empty pairs}=t_j-2
\]

under either local resolution.  If `m` is odd, the leftover pair has
imbalance `u-1`.  Hence the global rank condition

\[
 \sum_jt_j+u=m
\]

is exactly equivalent to zero total full/empty imbalance.

For each fixed rank vector, either local resolution partitions every local
slice.  Cartesian products therefore partition that vector sector, and the
rank-vector sectors themselves are disjoint.  Pair supports from distinct
quartets are disjoint.  This proves the product theorem for arbitrary frame
choices depending on the complete rank vector.

The theorem does not assert that the resolution may depend independently on
the individual vertex after cells are formed.  Its allowed dependence is on
the rank-vector sector, or on complete overlap components as in the
single-quartet theorem.

There are exponentially many visibly different sectors.  For example,
vectors using local ranks one and three in balanced numbers already number
`exp(Theta(g))`, and every such quartet has a visible free local pair.
Thus exponentially many frames can occur in one partition, although their
statistical distribution is unconstrained.

## 6. Togglable-quartet calculation

For a fixed quartet, each specified two-subset occurs in
`binom(2m-4,m-2)` middle sets.  Four of the six two-subsets change between a
singleton and a two-cube under the switch.  Therefore

\[
 p_{\rm tog}
 =4{\binom{2m-4}{m-2}\over\binom{2m}m}
 ={m(m-1)\over(2m-1)(2m-3)}
 ={1\over4}+O(1/m).
\]

Multiplication by `floor(m/2)` gives `m/8+O(1)` expected togglable
quartets.

Under a selected/unselected transposition on the uniform `m`-slice, at most
two quartets change state, so the toggle count changes by at most two.  The
standard slice bounded-difference inequality yields

\[
 \Pr(|T-\mathbb ET|\ge x)\le2e^{-c x^2/m}.
\]

At `x=m^(2/3)`, the exceptional fraction is
`exp(-Omega(m^(1/3)))=o(1)`.  This proves a linear number of opportunities,
not an actual random walk or mixing theorem.

## 7. Dimension distribution audit

For a fixed matching, if exactly `d` edges are split, choose those edges,
orient them, and choose half of the remaining edges to be full:

\[
 \#\{S:D=d\}
 =\binom md2^d\binom{m-d}{(m-d)/2},
\]

with the usual parity restriction.  Indicator counting gives

\[
 \Pr(e\text{ split})={m\over2m-1},
\]

and for distinct matching edges

\[
 \Pr(e,e'\text{ split})
 ={m(m-1)\over(2m-1)(2m-3)}.
\]

These yield

\[
 \mathbb ED={m^2\over2m-1},
 \qquad
 \operatorname{Var}D
 ={2m^2(m-1)^2\over(2m-1)^2(2m-3)}.
\]

The local dimension multiset is identical on the two sides of every trade.
For a wreath product, this identity holds in every local rank slice and is
preserved under products.  Therefore every permitted hybrid partition has
exactly the canonical vertex-weighted dimension histogram.

The canonical split count is two-Lipschitz on the uniform slice, giving an
`exp(-Omega(x^2/m))` tail.  Histogram equality transfers this tail to every
hybrid partition.  The transfer is necessary: an arbitrary componentwise
dimension assignment need not itself remain two-Lipschitz.

Taking `x=m^(2/3)` proves the claimed `m/2-m^(2/3)` lower dimension outside
`o(W)` vertices.

## 8. Machine audit

`scratch/check_quartet_cell_trade.py` exhaustively checks both one-switch
partitions, every overlap component, arbitrary component choices, dimension
histograms, and even/odd wreath products through `m=7`.  All checks pass.

The computation verifies the finite classification; none of the shadow or
asymptotic conclusions is inferred from it.
