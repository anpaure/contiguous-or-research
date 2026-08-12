# Quartet wreath partitions and exact pairing diffusion

## 0. Status

This note gives an exact middle-layer construction.  It does **not** prove
shadow coverage or an OR upper bound.

The point is to escape the sparse-pivot obstruction in
`PIVOT_SHADOW_CAPACITY.md`.  Instead of perturbing one global coordinate
matching in only `o(sqrt(m))` places, the construction below partitions the
middle layer into physical pair-flip cubes whose matching frames may differ
independently on a linear number of four-coordinate packets.

For each fixed middle set under a random sector frame, the rank-two packet
contributions are exactly binomial; dually, the same law holds for a uniform
set in one fixed deterministic sector frame.  For typical central sets the
marginal variance is `Theta(m)`, matching the scale of the shadow imbalance
at depth `Theta(sqrt(m))`.  No simultaneous shadow statement is inferred.

## 1. The three local resolutions of a quartet

Let

\[
 Q=\{a,b,c,d\}
\]

and let

\[
 P_0=ab|cd,\qquad P_1=ac|bd,\qquad P_2=ad|bc                 \tag{1.1}
\]

be its three perfect matchings.  For one matching `P`, declare two subsets
of `Q` equivalent when they have the same full and empty `P`-edges.  The
split `P`-edges are free, one endpoint being chosen from each.

This partitions `2^Q` rank by rank into physical pair-flip cubes:

* rank zero and rank four each give one singleton;
* rank one and rank three each give two one-dimensional cubes;
* rank two gives one two-dimensional cube and two singletons.

For example, at rank two the `P_0` resolution is

\[
 \{ac,ad,bc,bd\}\ \dot\cup\ \{ab\}\ \dot\cup\ \{cd\}.   \tag{1.2}
\]

The other two resolutions are obtained by permuting the three matchings.

### Lemma 1 (local overlap components)

Compare the `P_0` and `P_1` cell partitions on a fixed local rank `t`.

* For `t=0,4` the common partition is trivial.
* For `t=1,3` the overlap incidence graph is one four-cycle: two
  `P_0` edges versus two `P_1` edges.
* For `t=2` the overlap incidence graph is connected and has three cells
  on either side: one square and two singletons.

Consequently either complete side is an exact resolution of the same local
vertex set.  This is a genuine partition trade; no middle vertex is added,
deleted, or repeated.

### Proof

At rank one the two resolutions are

\[
 \{a,b\},\{c,d\}\qquad\hbox{and}\qquad
 \{a,c\},\{b,d\},                                     \tag{1.3}
\]

whose incidence graph is a four-cycle.  Rank three is complementary.

At rank two the `P_0` cells are

\[
 \{ac,ad,bc,bd\},\{ab\},\{cd\},                     \tag{1.4}
\]

whereas the `P_1` cells are

\[
 \{ab,ad,bc,cd\},\{ac\},\{bd\}.                     \tag{1.5}
\]

The two square cells meet at `ad,bc`; each singleton on one side belongs
to the square on the other.  Hence the overlap graph is connected.  The
rank-zero and rank-four assertions are immediate.  QED.

The same statement holds for every pair among `P_0,P_1,P_2`.

## 2. Product and wreath partitions of the middle layer

Assume first that `m=2g`, so that the coordinate set `[2m]` is the disjoint
union of quartets

\[
                    Q_1\dot\cup\cdots\dot\cup Q_g.   \tag{2.1}
\]

For a middle set `X`, put

\[
 t(X)=(|X\cap Q_1|,\ldots,|X\cap Q_g|).              \tag{2.2}
\]

Its coordinates lie in `{0,1,2,3,4}` and sum to `m=2g`.  Let

\[
 \Omega_t=\{X\in\tbinom{[2m]}m:t(X)=t\}.             \tag{2.3}
\]

For every admissible vector `t`, choose an arbitrary frame

\[
 \eta(t)=(\eta_1(t),\ldots,\eta_g(t))\in\{0,1,2\}^g. \tag{2.4}
\]

On `Omega_t`, take the Cartesian product of the local rank-`t_j` cell
partitions belonging to `P_(eta_j(t))`.

### Theorem 2 (quartet wreath partition)

For every choice of the frame function `eta`, these product cells form a
partition of the complete middle layer.  Every cell is a genuine isometric
Boolean cube in the Johnson graph.  Its free directions are disjoint
coordinate pairs, but its pairing frame may depend on the whole local-rank
vector `t`.

### Proof

For fixed `t`, each local matching resolution partitions the local
rank-`t_j` subsets of `Q_j`.  Their Cartesian products therefore partition
`Omega_t`.  Distinct rank vectors give disjoint strata, and the admissible
strata partition the middle layer.

In one product cell every local full or empty pair is fixed, and every
local split pair contributes exactly one freely chosen endpoint.  Supports
from distinct quartets are disjoint.  If `f_j,e_j` are the local numbers
of full and empty frame pairs, then

\[
 f_j-e_j=t_j-2.
\]

Thus `sum_j(f_j-e_j)=sum_jt_j-2g=0`.  The product is therefore a
canonical middle-layer matching cell, hence a physical pair-flip cube, and
flipping one direction is a Johnson edge.  QED.

This is already qualitatively different from a single matching frame.
There are exponentially many admissible rank vectors, and their frame
choices are completely independent without creating a seam or losing a
middle vertex.

For odd `m`, reserve one coordinate pair `E` and apply the construction to
the remaining `g=floor(m/2)` quartets.  Refine the rank vector by
`u=|X intersect E| in {0,1,2}` and allow the frame to depend on `(t,u)`.
The final pair is empty for `u=0`, free for `u=1`, and full for `u=2`.
The balance identity is

\[
 \sum_j(t_j-2)+(u-1)=0.
\]

Thus the odd case is also an exact product partition.  The final direction
is present only in the rank-one sector; it is not globally fixed as a free
direction.

## 3. Exact local type law

For a frame `eta` and a set `S`, let

\[
 F_\eta(S)=\#\{\hbox{chosen frame pairs contained in }S\}. \tag{3.1}
\]

In the odd case include the reserved final pair in the physical frame.

Fix a local-rank stratum `t` (or `(t,u)` in the odd case) and choose the
coordinates of its frame independently and uniformly from `{0,1,2}`.

Let

\[
 n_i(S)=\#\{j:|S\cap Q_j|=i\}.                       \tag{3.2}
\]

### Theorem 3 (binomial pairing diffusion)

For every fixed set `S` in the stratum,

\[
 F_\eta(S)
   ={\bf1}_{\{u=2\}}+
     n_3(S)+2n_4(S)+\operatorname{Bin}(n_2(S),1/3)  \tag{3.3}
\]

in distribution.  The Bernoulli variables contributed by the rank-two
quartets are independent.  The first term is omitted when `m` is even.  In
particular,

\[
 \operatorname{Var}F_\eta(S)=\frac{2}{9}n_2(S).     \tag{3.4}
\]

### Proof

A local zero- or one-set contains no matching edge.  A local three-set
contains exactly one edge of every perfect matching of the quartet, and a
local four-set contains both edges.  A local two-set is itself an edge of
exactly one of the three perfect matchings.  The frame choices on distinct
quartets are independent, proving (3.3)--(3.4).  QED.

There is an exact dual form.  Fix any deterministic `eta(t)` and choose
`S` uniformly from `Omega_t`.  At a rank-two quartet, exactly two of the six
local states are edges of the chosen frame.  Since `Omega_t` is a Cartesian
product, (3.3) is again the exact distribution, now over `S` rather than
over `eta`.

For a uniformly random middle set `S`,

\[
 \mathbb E n_2(S)
 =g\,6\frac{\binom{2m-4}{m-2}}{\binom{2m}{m}}
 =\left(\frac3{16}+o(1)\right)m.                    \tag{3.5}
\]

For every fixed `epsilon>0`, the uniform-slice bounded-difference
inequality gives

\[
 \Pr\left\{\left|n_2(S)-3m/16\right|>\epsilon m\right\}
 \le e^{-c_\epsilon m}.                              \tag{3.6}
\]

Letting `epsilon` tend to zero sufficiently slowly shows that
`n_2(S)=(3/16+o(1))m` outside `o(W)` sets.  Consequently the conditional
variance in (3.4) is `(1/24+o(1))m` for almost every middle set.

This is genuine `Theta(sqrt(m))` marginal fluctuation in full-pair type.
It is not independence between different sets in one stratum: those sets
share the same frame vector.

### Corollary 4 (deterministic linear re-pairing)

Fix the reference matching `P_0` obtained by using `P_0` on every quartet.
There is a deterministic frame function `eta` for which, outside
`e^{-Omega(m)}W` middle vertices, the cell containing `S` has
`Omega(m)` free supports that are not edges of this reference matching.

### Proof

For fixed `S` and random `eta(t(S))`, let `Y_j` count nonreference free
supports in quartet `j`.  If the local rank is one or three then
`Y_j=1` with probability `2/3`.  At rank two, `Y_j` is either zero or two
and has expectation at least `2/3`, regardless of which two-set occurs.
It is zero at ranks zero and four.

Let `A(S)` count quartets of ranks one, two, or three.  A slice
transposition changes at most two indicators, and
`mathbb E A=(7/8+o(1))g`.  Hence `A(S)>=3g/4` outside
`e^{-Omega(m)}W` sets.  Conditional on such an `S`, the variables `Y_j`
are independent, bounded by two, and have total mean at least `g/2`.
Chernoff gives

\[
 \Pr_\eta\left\{\sum_jY_j<g/4\right\}=e^{-\Omega(m)}.
\]

Averaging over `S` and then fixing one frame function proves the claim.
QED.

## 4. Typical cell dimension

For a fixed set `X` and a uniformly random frame on its stratum, the local
cell dimension `D_j` is

\[
 D_j=\begin{cases}
 0,&|X\cap Q_j|=0\hbox{ or }4,\\
 1,&|X\cap Q_j|=1\hbox{ or }3,\\
 0\text{ with probability }1/3,
   \ 2\text{ with probability }2/3,&|X\cap Q_j|=2.
 \end{cases}                                         \tag{4.1}
\]

For a uniformly random middle set, the local-rank frequencies are the
central hypergeometric analogue of the binomial weights

\[
                   1,4,6,4,1.                       \tag{4.2}
\]

Let `D_eta(X)` be the complete product-cell dimension, including the final
pair in the odd case.  A stronger deterministic statement holds.  In each
local rank slice the cell-dimension multiset is

\[
 (0),\quad(1,1),\quad(0,0,2),\quad(1,1),\quad(0),
                                                               \tag{4.3}
\]

for ranks zero through four, independently of which of the three
resolutions is chosen.  Since a dimension-`d` cell has `2^d` vertices,
Cartesian products show that **every** frame function `eta` has the same
global vertex-weighted dimension histogram as the canonical fixed-matching
partition.  Explicitly,

\[
 \#\{X:D_\eta(X)=d\}
 =\binom md2^d\binom{m-d}{(m-d)/2},                 \tag{4.4}
\]

when `m-d` is even, and is zero otherwise.  In particular,

\[
 \mathbb E_XD_\eta(X)=\frac{m^2}{2m-1}
 =(1/2+o(1))m.                                      \tag{4.5}
\]

For the canonical matching, `D` is the number of split pairs and changes
by at most two under a selected/unselected slice transposition.  Its
bounded-difference tail, transferred through the exact histogram identity,
gives uniformly for every deterministic `eta`

\[
 \Pr_X\{D_\eta(X)<m/4\}=e^{-\Omega(m)}.              \tag{4.6}
\]

Thus every quartet wreath partition--not merely one obtained by
averaging--has all but `e^{-Omega(m)}W` middle vertices in physical cells
of dimension at least `m/4`.

The threshold `m/4` is deliberately nonoptimal.  Only a fixed positive
linear dimension is needed.

## 5. What is and is not solved

Theorems 2--3 and Corollary 4 supply three facts that the previous pivot
partitions lacked:

1. exact disjoint coverage of the middle layer;
2. a cellwise pairing frame chosen from `3^g` product frames;
3. `Theta(sqrt(m))` marginal type diffusion on every set with `Theta(m)`
   local rank-two packets, together with a deterministic choice having
   `Omega(m)` nonreference free supports at almost every middle vertex.

They do not yet supply:

* a radius/SCD label distribution;
* cycle tilings whose consecutive windows have globally distinct shadows;
* protection for atypical targets having few rank-two packets;
* one simultaneous choice of `eta`, cycle supports, and cycle orders that
  covers every central-band target;
* a bound of `o(W)` on all shadow omissions.

The next mathematical target is therefore a **wreath shadow theorem**:
combine a small number of independently conjugated quartet systems and
choose the frame function and linear-cycle tilings so that, through
`H=sqrt(m) omega(m)`, the total lower and upper omission is `o(W)`.

The theorem of `PIVOT_SHADOW_CAPACITY.md` does not apply to this target.
That theorem assumes one global native matching and only `O(d)=o(H)`
nonnative pivot directions in a radius-`d` cell.  The quartet partition is
not a radius-pure BK partition, its frame changes with the rank-vector
sector, and Corollary 4 gives a choice with `Omega(m)` nonreference free
directions in the cells containing all but `e^{-Omega(m)}W` middle
vertices.

A full-pair statistic can still be defined relative to any chosen reference
matching.  What is unavailable is the sparse-direction premise used there
to conclude that only `o(q)` directions in almost every depth-`q` window
can affect that statistic.

This genuinely evades the hypotheses and the particular fixed-type
capacity proof.  It does **not** prove that the new directions occur in the
right cyclic windows, that their shadows are injective, or that any target
is covered.  An analogous capacity obstruction adapted to sector-dependent
frames is not ruled out.
